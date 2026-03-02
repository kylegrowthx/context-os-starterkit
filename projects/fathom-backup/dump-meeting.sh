#!/bin/bash
#
# dump-meeting.sh — Pull everything from Fathom for a single meeting and save raw JSON
#
# Usage:
#   ./dump-meeting.sh <recording_id>
#   ./dump-meeting.sh 125647422
#   ./dump-meeting.sh --list              # show recent meetings
#   ./dump-meeting.sh --list 20           # show 20 recent meetings
#   ./dump-meeting.sh --list-after 2026-02-01   # meetings after a date

set -euo pipefail

API_KEY="egY4k0wxa9bCbwKENdVBaQ.V8AnJy_b1e-tZe-St3QtHkdhvs9mFW9xIg8w29e0WeA"
BASE_URL="https://api.fathom.ai/external/v1"
BACKUP_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ $# -lt 1 ]; then
  echo "Usage:"
  echo "  $0 <recording_id>                Dump a single meeting"
  echo "  $0 --list [count]                List recent meetings"
  echo "  $0 --list-after YYYY-MM-DD       List meetings after a date"
  echo "  $0 --dump-all-after YYYY-MM-DD   Dump ALL meetings after a date"
  exit 1
fi

fetch() {
  curl -s -f -H "X-Api-Key: $API_KEY" -H "Content-Type: application/json" "$1"
}

# --list mode
if [ "$1" = "--list" ]; then
  echo "Fetching recent meetings..."
  RAW=$(fetch "$BASE_URL/meetings")
  echo "$RAW" | python3 -c "
import json, sys
from datetime import datetime
data = json.load(sys.stdin)
for m in data.get('items', []):
    dt = datetime.fromisoformat(m['recording_start_time'].replace('Z','+00:00')).strftime('%Y-%m-%d %H:%M')
    title = m.get('title') or m.get('meeting_title') or '(no title)'
    rid = m['recording_id']
    print(f'  {rid}  {dt}  {title}')
" | head -n "${2:-10}"
  exit 0
fi

# --list-after mode
if [ "$1" = "--list-after" ]; then
  DATE="${2:?Provide a date like 2026-02-01}"
  echo "Fetching meetings after $DATE..."
  RAW=$(fetch "$BASE_URL/meetings?created_after=${DATE}T00:00:00Z")
  echo "$RAW" | python3 -c "
import json, sys
from datetime import datetime
data = json.load(sys.stdin)
for m in data.get('items', []):
    dt = datetime.fromisoformat(m['recording_start_time'].replace('Z','+00:00')).strftime('%Y-%m-%d %H:%M')
    title = m.get('title') or m.get('meeting_title') or '(no title)'
    rid = m['recording_id']
    print(f'  {rid}  {dt}  {title}')
"
  exit 0
fi

# --dump-all-after mode
if [ "$1" = "--dump-all-after" ]; then
  DATE="${2:?Provide a date like 2026-02-01}"
  echo "Fetching all meetings after $DATE..."
  MEETINGS_JSON=$(fetch "$BASE_URL/meetings?created_after=${DATE}T00:00:00Z&include_transcript=true&include_summary=true&include_action_items=true&include_crm_matches=true")
  
  IDS=$(echo "$MEETINGS_JSON" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for m in data.get('items', []):
    print(m['recording_id'])
")

  COUNT=$(echo "$IDS" | wc -l | tr -d ' ')
  echo "Found $COUNT meetings. Dumping each..."
  
  for ID in $IDS; do
    "$0" "$ID"
    echo ""
  done
  
  echo "Batch dump complete."
  exit 0
fi

# --- Single meeting dump ---
RECORDING_ID="$1"

echo "Fetching meeting $RECORDING_ID with all includes..."

# Use the raw index JSON to find the meeting's date, then fetch a narrow window
MEETING=$(python3 << PYEOF
import urllib.request, json, sys, time
from datetime import datetime, timedelta, timezone

API_KEY = "$API_KEY"
BASE_URL = "$BASE_URL"
TARGET_ID = $RECORDING_ID
INDEX_JSON = "$BACKUP_DIR/all-meetings-raw.json"

# Look up this meeting's date from our cached index to narrow the search window
created_at = None
try:
    with open(INDEX_JSON) as f:
        cached = json.load(f)
    for m in cached:
        if m.get("recording_id") == TARGET_ID:
            created_at = m.get("created_at") or m.get("recording_start_time")
            break
except Exception:
    pass

if created_at:
    # Fetch a narrow 24-hour window around the meeting date
    dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    after = (dt - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    before = (dt + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    url = f"{BASE_URL}/meetings?include_transcript=true&include_summary=true&include_action_items=true&include_crm_matches=true&created_after={after}&created_before={before}"
    print(f"  Searching narrow window: {after} to {before}", file=sys.stderr)
    cursor = None
    while True:
        req_url = url + (f"&cursor={cursor}" if cursor else "")
        req = urllib.request.Request(req_url, headers={"X-Api-Key": API_KEY})
        with urllib.request.urlopen(req) as resp:
            data = json.load(resp)
        for m in data.get("items", []):
            if m.get("recording_id") == TARGET_ID:
                print(json.dumps(m))
                sys.exit(0)
        cursor = data.get("next_cursor")
        if not cursor:
            break
        time.sleep(1.1)

# Last resort: full pagination
print("  Not found in window, falling back to full pagination...", file=sys.stderr)
cursor = None
page = 1
while True:
    url = f"{BASE_URL}/meetings?include_transcript=true&include_summary=true&include_action_items=true&include_crm_matches=true"
    if cursor:
        url += f"&cursor={cursor}"
    req = urllib.request.Request(url, headers={"X-Api-Key": API_KEY})
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)
    for m in data.get("items", []):
        if m.get("recording_id") == TARGET_ID:
            print(json.dumps(m))
            sys.exit(0)
    cursor = data.get("next_cursor")
    if not cursor:
        break
    page += 1
    time.sleep(1.1)

print("NOT_FOUND", file=sys.stderr)
sys.exit(1)
PYEOF
)

if [ -z "$MEETING" ]; then
  echo "Meeting $RECORDING_ID not found."
  exit 1
fi

# Extract year-month and folder name
read -r YEAR_MONTH FOLDER_NAME <<< $(echo "$MEETING" | python3 -c "
import json, sys, re
from datetime import datetime
m = json.load(sys.stdin)
dt = datetime.fromisoformat(m['recording_start_time'].replace('Z','+00:00'))
ym = dt.strftime('%Y-%m')
date = dt.strftime('%Y-%m-%d')
title = m.get('title') or m.get('meeting_title') or str(m['recording_id'])
slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
print(f'{ym} {date}-{slug}')
")

OUT_DIR="$BACKUP_DIR/$YEAR_MONTH/$FOLDER_NAME"
mkdir -p "$OUT_DIR"

echo "Saving to: $YEAR_MONTH/$FOLDER_NAME/"

# Save the full meeting JSON
echo "$MEETING" | python3 -m json.tool > "$OUT_DIR/meeting-full.json"
echo "  -> meeting-full.json"

# Extract and save individual sections
echo "$MEETING" | python3 -c "
import json, sys, os

m = json.load(sys.stdin)
out = '$OUT_DIR'

meta = {k: v for k, v in m.items() if k not in ('transcript', 'default_summary', 'action_items')}
with open(os.path.join(out, 'metadata.json'), 'w') as f:
    json.dump(meta, f, indent=2)

if m.get('transcript'):
    with open(os.path.join(out, 'transcript.json'), 'w') as f:
        json.dump(m['transcript'], f, indent=2)

if m.get('default_summary'):
    with open(os.path.join(out, 'summary.json'), 'w') as f:
        json.dump(m['default_summary'], f, indent=2)

if m.get('action_items'):
    with open(os.path.join(out, 'action-items.json'), 'w') as f:
        json.dump(m['action_items'], f, indent=2)

if m.get('crm_matches'):
    with open(os.path.join(out, 'crm-matches.json'), 'w') as f:
        json.dump(m['crm_matches'], f, indent=2)

if m.get('calendar_invitees'):
    with open(os.path.join(out, 'participants.json'), 'w') as f:
        json.dump(m['calendar_invitees'], f, indent=2)
"
echo "  -> metadata.json, transcript.json, summary.json, action-items.json, crm-matches.json, participants.json"

# Hit the dedicated transcript endpoint (may differ from embedded transcript)
echo "Fetching standalone transcript..."
fetch "$BASE_URL/recordings/$RECORDING_ID/transcript" | python3 -m json.tool > "$OUT_DIR/transcript-raw.json" 2>/dev/null && \
  echo "  -> transcript-raw.json" || \
  echo "  -> transcript-raw.json (not available)"

echo "Done: $YEAR_MONTH/$FOLDER_NAME/"
