# Fathom Backup

Raw JSON dumps of meeting data pulled from Fathom via the [Fathom API](https://api.fathom.ai/external/v1).

## Structure

```
projects/fathom-backup/
├── dump-meeting.sh          # The backup script
├── README.md
├── 2026-02/
│   ├── 2026-02-26-relay-growthx-bi-weekly-sync/
│   │   ├── meeting-full.json      # Complete API response
│   │   ├── metadata.json          # Title, dates, URLs, recorded_by
│   │   ├── participants.json      # Calendar invitees, emails, external flags
│   │   ├── summary.json           # Fathom AI summary
│   │   ├── transcript.json        # Transcript (from meeting endpoint)
│   │   ├── transcript-raw.json    # Transcript (from dedicated endpoint)
│   │   ├── action-items.json      # Action items with assignees
│   │   └── crm-matches.json       # CRM contacts/companies/deals
│   └── 2026-02-25-adventures-group-growthx-weekly-sync/
│       └── ...
├── 2026-03/
│   └── ...
```

## Usage

```bash
# Dump a single meeting by recording ID
./dump-meeting.sh 125647422

# List recent meetings (default 10)
./dump-meeting.sh --list
./dump-meeting.sh --list 20

# List meetings after a date
./dump-meeting.sh --list-after 2026-02-01

# Dump ALL meetings after a date
./dump-meeting.sh --dump-all-after 2026-02-01

# Download all remaining (rate-limited, 4 parallel agents)
./run-parallel-backup.sh [num_agents] [delay_sec]
./run-parallel-backup.sh 4 9   # default: 4 agents, 9s delay ≈ 27 meetings/min
```

**Parallel backup:** `run-parallel-backup.sh` reads remaining IDs from INDEX.md (or `.remaining-ids.txt`), splits them across 4 agents, and runs each with a 9s delay between meetings so total rate stays under Fathom’s 60 req/min. Logs: `.parallel-backup.log`, `.parallel-logs/agent-*.log`. When finished it updates INDEX.md and clears the remaining list.

## What gets saved per meeting

| File | What's inside |
|------|---------------|
| `meeting-full.json` | Complete API response — everything in one file |
| `metadata.json` | Title, dates, recording info, URLs, recorded_by (no transcript/summary) |
| `participants.json` | Calendar invitees with names, emails, external flags, domains |
| `summary.json` | Fathom's AI-generated meeting summary |
| `transcript.json` | Speaker-labeled transcript with timestamps (from meeting payload) |
| `transcript-raw.json` | Speaker-labeled transcript (from dedicated `/transcript` endpoint) |
| `action-items.json` | Action items with assignees, timestamps, completion status |
| `crm-matches.json` | Matched CRM contacts, companies, and deals |

## Rate limits

Fathom API allows 60 requests per minute. For bulk dumps, the script processes sequentially.

## Config

- MCP server: `~/fathom-mcp/dist/index.js`
- Cursor MCP config: `~/.cursor/mcp.json` (under `fathom` key)
- API base: `https://api.fathom.ai/external/v1`
