#!/bin/bash
#
# run-parallel-backup.sh — Download all remaining Fathom meetings using 4 parallel
# agents with rate limiting (8s delay per meeting per agent = 30 meetings/min total,
# under Fathom's 60 requests/min limit).
#
# Usage: ./run-parallel-backup.sh [num_agents]
# Default: 4 agents. Each meeting = 2 API calls, so 4 agents × 1 meeting per 8s = 30/min.

set -euo pipefail

BACKUP_DIR="$(cd "$(dirname "$0")" && pwd)"
IDS_FILE="$BACKUP_DIR/.remaining-ids.txt"
NUM_AGENTS="${1:-4}"
DELAY_SEC="${2:-9}"   # delay between meetings per agent (9s × 4 agents ≈ 27/min, under 60 req/min)

if [ ! -f "$IDS_FILE" ]; then
  echo "Refreshing remaining IDs from INDEX.md (only meetings not yet on disk)..."
  python3 -c "
import re, os, sys
BACKUP = sys.argv[1]
INDEX = os.path.join(BACKUP, 'INDEX.md')
OUT = os.path.join(BACKUP, '.remaining-ids.txt')
with open(INDEX) as f:
    lines = f.readlines()
remaining = []
for line in lines:
    if not line.strip().startswith('| [') or '|' not in line:
        continue
    m_id = re.search(r'\|\s*(\d{6,})\s*\|', line)
    m_folder = re.search(r'\x60([^\x60]+)\x60', line)
    if not m_id or not m_folder:
        continue
    rid, folder = m_id.group(1), m_folder.group(1).strip()
    if not os.path.exists(os.path.join(BACKUP, folder, 'meeting-full.json')):
        remaining.append(rid)
with open(OUT, 'w') as f:
    f.write('\n'.join(remaining) + '\n')
print(f'  {len(remaining)} meetings to download (skipping already on disk)')
" "$BACKUP_DIR"
fi

TOTAL=$(wc -l < "$IDS_FILE" | tr -d ' ')
if [ "$TOTAL" -eq 0 ]; then
  echo "No remaining meetings to download."
  exit 0
fi

CHUNK_SIZE=$(( (TOTAL + NUM_AGENTS - 1) / NUM_AGENTS ))
echo "Downloading $TOTAL meetings with $NUM_AGENTS agents (delay ${DELAY_SEC}s between meetings per agent)"
echo "Estimated time: $(( TOTAL * DELAY_SEC / NUM_AGENTS / 60 )) minutes"
echo ""

LOG_DIR="$BACKUP_DIR/.parallel-logs"
mkdir -p "$LOG_DIR"
echo "Logs: $LOG_DIR/agent-*.log"

run_chunk() {
  local agent_id=$1
  local line_start=$2   # 1-based first line
  local line_count=$3
  local line_end=$(( line_start + line_count - 1 ))
  local log="$LOG_DIR/agent-$agent_id.log"
  local id
  local i=0
  echo "[$(date -Iseconds)] Agent $agent_id started (lines $line_start..$line_end)" >> "$log"
  while read -r id; do
    [ -z "$id" ] && continue
    echo "[$(date -Iseconds)] $id" >> "$log"
    if "$BACKUP_DIR/dump-meeting.sh" "$id"; then
      : $(( i += 1 ))
    fi
    sleep "$DELAY_SEC"
  done < <(sed -n "${line_start},${line_end}p" "$IDS_FILE")
  echo "[$(date -Iseconds)] Agent $agent_id finished ($i meetings)" >> "$log"
}

for a in $(seq 0 $(( NUM_AGENTS - 1 ))); do
  start=$(( a * CHUNK_SIZE ))
  [ "$start" -ge "$TOTAL" ] && continue
  end=$(( start + CHUNK_SIZE ))
  [ "$end" -gt "$TOTAL" ] && end=$TOTAL
  count=$(( end - start ))
  ( run_chunk "$a" "$(( start + 1 ))" "$count" ) &
done

wait
echo ""
echo "All agents finished. Updating INDEX.md..."

python3 -c "
import re, sys

path = sys.argv[1] + '/INDEX.md'
ids_file = sys.argv[2]

with open(ids_file) as f:
    ids = {int(line.strip()) for line in f if line.strip()}

with open(path) as f:
    content = f.read()

lines = content.split('\n')
marked = 0
updated = []
for line in lines:
    for rid in ids:
        if f'| {rid} |' in line and line.startswith('| [ ]'):
            line = line.replace('| [ ]', '| [x]', 1)
            marked += 1
            break
    updated.append(line)

result = '\n'.join(updated)
dl_match = re.search(r'\*\*Downloaded:\*\* (\d+) / (\d+)', result)
old_dl = int(dl_match.group(1))
total = dl_match.group(2)
new_dl = old_dl + marked
result = re.sub(r'\*\*Downloaded:\*\* \d+ / \d+', f'**Downloaded:** {new_dl} / {total}', result)

with open(path, 'w') as f:
    f.write(result)

print(f'Marked {marked} meetings. Total downloaded: {new_dl}/{total}')
" "$BACKUP_DIR" "$IDS_FILE"

rm -f "$IDS_FILE"
echo "Done. Remaining list cleared; re-run to continue from INDEX.md."
