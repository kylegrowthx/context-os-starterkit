---
name: pull-meeting
description: Pull a meeting from Fireflies and save it to /records/transcripts with full context. Master orchestrator that fetches data, runs the format script, then delegates to enrich-fireflies-transcript and link-transcript-records skills. Triggers on "pull meeting", "get meeting", "fireflies", "meeting transcript", "download transcript".
---

# Pull Meeting

Pull a meeting from Fireflies, format it with a script, enrich it with LLM analysis, and sync all related records.

## Inputs / Outputs

| | What | Example |
|---|---|---|
| **Input** | Meeting name, date, or participant from user | "Pull the Flodesk intro from Feb 26" |
| **Tools** | Fireflies MCP, `format-meeting.py` script, enrich + link skills | — |
| **Output** | Enriched transcript + updated meeting record + updated contacts | `records/transcripts/2026-02/2026-02-26-flodesk-growthx-intro.md` |

## Architecture

This skill orchestrates a 3-skill pipeline:

1. **pull-meeting** (this skill) — fetch from Fireflies + run format script
2. **enrich-fireflies-transcript** — 10-step LLM enrichment (separate skill)
3. **link-transcript-records** — update meeting records, contacts, INDEX files (separate skill)

Each skill can also run independently.

## Workflow

### Step 1: Identify the Meeting

Ask the user: **"What meeting do you want to pull? (provide a name, date, or participant)"**

Then search Fireflies with `fireflies_search`:
- By keyword: `keyword:"standup"`
- By date range: `from:2026-01-20 to:2026-01-27`
- By participant: `participants:marcel@growthxlabs.com` or `participants:marcel@growthx.ai`
- Combined: `keyword:"weekly" from:2026-01-01 participants:marcel@growthxlabs.com`

**Note:** Marcel's meetings may appear under either `marcel@growthxlabs.com` or `marcel@growthx.ai`. Try `marcel@growthxlabs.com` first (primary).

### Step 2: Confirm Selection

Present results to user:
- Meeting title
- Date
- Duration
- Participants

Ask: **"Is this the meeting? (Yes/No, or specify which one)"**

### Step 3: Fetch Raw Data

Call both MCP tools and save raw outputs to temp files:

```bash
# Agent calls fireflies_get_summary, saves output:
# → /tmp/ff_summary_{meeting_id}.txt

# Agent calls fireflies_get_transcript, saves output:
# → /tmp/ff_transcript_{meeting_id}.txt
```

These are mechanical steps — no analysis needed. Just call the tools and write the output to files.

**Important:** When the MCP tool output goes to a cache file (large output), note the cache file path. That IS the file to pass to the script.

### Step 4: Run the Format Script

```bash
python3 .cursor/skills/pull-meeting/format-meeting.py \
  /tmp/ff_summary_{id}.txt \
  /tmp/ff_transcript_{id}.txt \
  --duration {minutes} \
  --meeting-link "{zoom_or_meet_link}" \
  -o "records/transcripts/YYYY-MM/draft-{id}.md"
```

Pass `--duration` and `--meeting-link` from the search results if available. Create the `YYYY-MM/` subdirectory if it doesn't exist.

The script produces a complete `.md` with:
- All deterministic sections filled (metadata, overview, key topics, action items, transcript)
- LLM placeholder comments for sections that need enrichment

### Step 5: Enrich the Transcript

Invoke the **enrich-fireflies-transcript** skill on the draft file:

> "Enrich the Fireflies transcript at `records/transcripts/YYYY-MM/draft-{id}.md`"

This skill reads the full file (including transcript) and performs 10-step enrichment: speaker fixes, metadata cleanup, summary rewrite, context, relevance, decisions & commitments, open questions, action item affiliations, transcript cleanup.

The enrichment skill also renames the file from `draft-{id}.md` to a descriptive name like `YYYY-MM-DD-flodesk-growthx-intro.md`.

### Step 6: Link Records

Invoke the **link-transcript-records** skill on the enriched file:

> "Link transcript records for `records/transcripts/YYYY-MM/YYYY-MM-DD-filename.md`"

This skill:
- Updates the matching meeting record in `records/meetings/`
- Updates contact dossiers for external participants
- Updates INDEX files

### Step 7: Report Back

After all steps complete, confirm:
- File saved to: `records/transcripts/YYYY-MM/YYYY-MM-DD-filename.md`
- Meeting: title
- Date: date
- Duration: X minutes
- Participants: count
- Key topics: 3-5 main topics
- Meeting record updated: path
- Contacts updated: list
- New dossiers created: list

## Batch Mode

To pull multiple meetings at once (e.g., "pull all my meetings not yet saved"):

### Step 1: Search Fireflies
Search with participant filter and date range:
```
participants:marcel@growthxlabs.com from:2026-01-01 to:2026-02-27 limit:50
```

### Step 2: List existing transcripts
List files in `records/transcripts/` to get already-saved meetings.

### Step 3: Deduplicate
Compare Fireflies results against existing files:
- Match by date prefix + title keyword overlap (2+ matching words)
- Account for UTC timezone shifts (+/- 1 day)
- Skip meetings under 5 minutes
- Skip untitled meetings

### Step 4: Present missing meetings
Show user a numbered table:

| # | Date | Meeting | Duration |
|---|------|---------|----------|
| 1 | Feb 26 | Flodesk <> GrowthX - Intro | 60m |
| 2 | Feb 26 | Strategy Sprint Standup | 63m |

Ask: **"Pull all, select specific numbers (e.g., '1, 3'), or skip short ones?"**

### Step 5: Process

For each selected meeting:
1. Fetch summary + transcript (Stage 1)
2. Run format script (Stage 2)
3. Enrich with enrich-fireflies-transcript skill (Stage 3)
4. Link with link-transcript-records skill (Stage 4)

For 4+ meetings, use Task agents to process in parallel batches of 3-4.

### Step 6: Report summary table

| # | Date | File | Duration | Key Topics |
|---|------|------|----------|------------|
| 1 | Feb 26 | `2026-02-26-flodesk-growthx-intro.md` | 60m | SEO, AEO, organic traffic |

Note any meetings where audio was not captured. List contacts updated/created.

## Edge Cases

### No audio captured
Some meetings have no transcript. Still save the file with metadata, summary, and action items. In the Transcript section, write: `No transcript captured (audio not available).`

### Timezone shifts
Fireflies uses UTC timestamps. A meeting at 10pm UTC on Feb 4 may correspond to a file dated Feb 5 in local time. When deduplicating, check +/- 1 day.

### Large transcript output
When `fireflies_get_transcript` output goes to a cache file, pass that cache file path directly to format-meeting.py. Don't try to read it into context.
