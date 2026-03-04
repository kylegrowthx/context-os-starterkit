#!/bin/bash
# status.sh — One-line status for parallel Fathom backup. Run every 3 min: watch -n 180 ./status.sh
BACKUP="$(cd "$(dirname "$0")" && pwd)"
N=$(find "$BACKUP" -maxdepth 3 -name "meeting-full.json" 2>/dev/null | wc -l | tr -d ' ')
if pgrep -f "run-parallel-backup" >/dev/null 2>&1; then
  echo "$(date '+%H:%M:%S') RUNNING  $N / 6738"
else
  echo "$(date '+%H:%M:%S') STOPPED   $N / 6738"
fi
tail -1 "$BACKUP/.parallel-backup.log" 2>/dev/null | sed 's/^/  /'
