---
name: fathom-backup
description: Download and archive Fathom meeting data as raw JSON into projects/fathom-backup/. Use when the user wants to backup, download, or archive Fathom meetings — individually, in batches, or the full archive. Triggers on "backup fathom", "dump fathom", "download fathom meetings", "fathom backup", "archive meetings from fathom", "download all fathom data", "batch download fathom", "continue fathom backup", "resume fathom download".
---

# Fathom Backup

Download raw meeting data from Fathom's API and save as JSON files, organized by year-month. Can run as a single meeting, a batch, or the full archive.

## Paths

| What | Where |
|------|-------|
| Backup root | `projects/fathom-backup/` |
| Script | `projects/fathom-backup/dump-meeting.sh` |
| Index | `projects/fathom-backup/INDEX.md` |
| Raw meeting list | `projects/fathom-backup/all-meetings-raw.json` |
| Downloaded meetings | `projects/fathom-backup/YYYY-MM/YYYY-MM-DD-meeting-slug/` |

## File structure per meeting

```
YYYY-MM/YYYY-MM-DD-meeting-slug/
├── meeting-full.json       # Complete API response (everything)
├── metadata.json           # Title, dates, URLs, recorded_by
├── participants.json       # Calendar invitees, emails, external flags
├── summary.json            # Fathom AI summary (raw)
├── transcript.json         # Transcript from meeting list endpoint
├── transcript-raw.json     # Transcript from dedicated /transcript endpoint
├── action-items.json       # Action items with assignees and timestamps
└── crm-matches.json        # CRM contacts/companies/deals
```

## INDEX.md format

The index tracks every known meeting and download status:

```
| [x] | 2026-02-26 | 16:00 | Relay <> GrowthX | 125647422 | 27m | Bethany Cantor +3 | `2026-02/2026-02-26-relay-growthx-bi-weekly-sync` |
| [ ] | 2026-02-25 | 19:31 | Logic <> GrowthX  | 125386246 | 26m | Azzam Aijazi +2  | `2026-02/2026-02-25-logic-growthx-listening-tour` |
```

- `[ ]` = not yet downloaded
- `[x]` = downloaded

## Script reference

```bash
# Single meeting by recording ID
./dump-meeting.sh <recording_id>

# List recent meetings (find IDs)
./dump-meeting.sh --list [count]

# List meetings after a date
./dump-meeting.sh --list-after YYYY-MM-DD

# Dump all meetings after a date (uses pagination)
./dump-meeting.sh --dump-all-after YYYY-MM-DD
```

The script uses `all-meetings-raw.json` to look up each meeting's timestamp before fetching, so it only queries a narrow 2-hour window per meeting — very fast (~2-3s each).

---

## Workflows

### Workflow 1: Download a single meeting

Use when user names a specific meeting or provides a recording ID.

1. If no ID given, search the index: `grep "Meeting Title" projects/fathom-backup/INDEX.md`
2. Extract the recording ID from the `| ID |` column
3. Run the dump:
   ```bash
   cd "/Users/marcelsantilli_mac2/Dropbox/GrowthX AI/Projects/growthx-context/projects/fathom-backup"
   ./dump-meeting.sh <recording_id>
   ```
4. Mark as downloaded in the index (flip `[ ]` → `[x]` on that row, increment the Downloaded counter)

---

### Workflow 2: Download a batch

Use when user asks for "next batch", "do 50 more", "download [month]", or similar.

**Step 1 — Pick the IDs to download**

For chronological batches (oldest first):
```bash
grep "| \[ \]" projects/fathom-backup/INDEX.md | tail -N  # oldest N
```

For newest first:
```bash
grep "| \[ \]" projects/fathom-backup/INDEX.md | head -N  # newest N
```

For a specific month (e.g. 2025-06):
```bash
grep "| \[ \]" projects/fathom-backup/INDEX.md | grep "| 2025-06-"
```

Extract recording IDs:
```bash
grep "| \[ \]" projects/fathom-backup/INDEX.md | tail -50 | grep -oE '\| [0-9]{6,} \|' | tr -d '| '
```

**Step 2 — Run the batch**

```bash
BACKUP="/Users/marcelsantilli_mac2/Dropbox/GrowthX AI/Projects/growthx-context/projects/fathom-backup"
IDS=(id1 id2 id3 ...)  # paste extracted IDs

for ID in "${IDS[@]}"; do
  echo "=== $ID ==="
  "$BACKUP/dump-meeting.sh" "$ID"
  echo ""
done
```

**Step 3 — Update the index**

After a batch completes, mark all downloaded IDs as `[x]` and increment the Downloaded counter. Use this Python snippet:

```python
import re

path = "/Users/marcelsantilli_mac2/Dropbox/GrowthX AI/Projects/growthx-context/projects/fathom-backup/INDEX.md"
ids = {id1, id2, ...}  # the set of recording IDs just downloaded

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
result = re.sub(r'\*\*Downloaded:\*\* \d+ / \d+', f'**Downloaded:** {old_dl + marked} / {total}', result)

with open(path, 'w') as f:
    f.write(result)

print(f"Marked {marked} meetings. Total: {old_dl + marked}/{total}")
```

---

### Workflow 3: Download the full archive

Use when user asks to "download everything", "get all meetings", or "run the full backup". This is a long-running job (~3-4 hours for 6,700+ meetings).

**Recommended approach: run in batches of 100, oldest-first**

```bash
BACKUP="/Users/marcelsantilli_mac2/Dropbox/GrowthX AI/Projects/growthx-context/projects/fathom-backup"

# Extract all not-yet-downloaded IDs, oldest first
IDS=$(grep "| \[ \]" "$BACKUP/INDEX.md" | tail -100 | grep -oE '\| [0-9]{6,} \|' | tr -d '| ' | tr '\n' ' ')

for ID in $IDS; do
  "$BACKUP/dump-meeting.sh" "$ID"
done
```

Then update the index. Repeat until `grep "| \[ \]" INDEX.md | wc -l` returns 0.

**Rate limits:** The script is safe — it uses the narrow-window lookup from `all-meetings-raw.json`, so each meeting only hits the API 2 times (lookup + transcript). At ~2-3s per meeting, 100 meetings takes ~5 minutes.

**Progress check:**
```bash
grep -c "\[x\]" projects/fathom-backup/INDEX.md   # downloaded
grep -c "\[ \]" projects/fathom-backup/INDEX.md   # remaining
```

---

## After downloading

Once meetings are downloaded, raw JSON is available for:

| Task | File to use |
|------|-------------|
| Read/process transcript | `transcript-raw.json` |
| Extract action items | `action-items.json` |
| Get meeting summary | `summary.json` |
| Check participants | `participants.json` |
| Cross-reference with CRM | `crm-matches.json` |

These are separate tasks — this skill only handles the download and index tracking.

## Current state (as of 2026-02-26)

- **Total meetings in index:** 6,738
- **Downloaded:** 11
- **Date range:** 2024-04-09 → 2026-02-26
- **Index file:** `projects/fathom-backup/INDEX.md`
- **Raw meeting list cached:** `projects/fathom-backup/all-meetings-raw.json` (6,853 entries incl. filtered ones)
