---
name: pull-meeting
description: Pull a meeting from Fireflies and save it to /transcripts with full context. Use when the user wants to pull, download, or retrieve a meeting transcript, or mentions Fireflies meetings. Triggers on "pull meeting", "get meeting", "fireflies", "meeting transcript", "download transcript".
---

# Pull Meeting

Pull a meeting from Fireflies and save it to `/records/transcripts` with full context.

## Inputs / Outputs

| | What | Example |
|---|---|---|
| **Input** | Meeting name, date, or participant from user | "Pull the strategy standup from Jan 27" |
| **Tool** | Fireflies MCP server (`fireflies_search`, `fireflies_get_summary`, `fireflies_get_transcript`) | -- |
| **Output** | Formatted transcript saved to records | `records/transcripts/2026-01-27-strategy-standup.md` |

## Overview

This skill:
1. Searches Fireflies for the specified meeting
2. Downloads meeting details (summary, action items, metadata)
3. Downloads raw transcript (speakers, sentences)
4. Formats transcript using the bundled formatter script
5. Combines into properly formatted markdown
6. Saves to `/records/transcripts/YYYY-MM-DD-meeting-name.md`

## Workflow

### Step 1: Identify the Meeting

Ask the user: **"What meeting do you want to pull? (provide a name, date, or participant)"**

Then search Fireflies with options:
- By keyword: `keyword:"standup"`
- By date range: `from:2026-01-20 to:2026-01-27`
- By participant: `participants:marcel@growthxlabs.com` or `participants:marcel@growthx.ai`
- Combined: `keyword:"weekly" from:2026-01-01 participants:marcel@growthxlabs.com`

**Note:** Marcel's meetings may appear under either `marcel@growthxlabs.com` or `marcel@growthx.ai`. When searching for Marcel's meetings, try `marcel@growthxlabs.com` first (primary), then `marcel@growthx.ai` if results seem incomplete.

### Step 2: Confirm Selection

Present results to user:
- Meeting title
- Date
- Duration
- Participants

Ask: **"Is this the meeting? (Yes/No, or specify which one)"**

### Step 3: Fetch Meeting Details

Use the meeting ID to get the summary with:
- Title, date, time, duration
- Organizer and participants
- Meeting link and transcript URL
- Keywords
- Overview/gist
- Shorthand bullet points
- Notes (detailed)
- Action items with assignees

### Step 4: Fetch Raw Transcript

Get the full transcript with:
- Speakers list
- All sentences with speaker attribution

**For large transcripts** (which go to cache as `.txt` files in the agent-tools directory), use the bundled formatter script to convert to markdown rather than reading into context:

```bash
python3 .cursor/skills/pull-meeting/format-transcript.py CACHE_FILE.txt > /tmp/meeting_transcript.md
```

This converts each `Speaker: text` line into `**Speaker:** text` markdown format.

**For transcripts returned inline** (smaller meetings), the raw dialogue is already in context and can be formatted directly into the file.

### Step 5: Generate Context Sections

Using the summary data, write these sections in GrowthX style:

**Summary** (2-3 sentences)
- What the meeting covered
- Key outcomes or decisions

**Context** (1-2 paragraphs)
- Why this meeting happened
- Where it fits in ongoing work
- Relevant background

**Relevance** (bullet points)
- Group by area (e.g., "To GrowthX Services:", "To CheckThat:", "To Community:")
- Why this meeting matters to each area
- Specific numbers, names, deadlines

### Step 6: Format and Save

**Filename:** `YYYY-MM-DD-descriptive-meeting-name.md`
- Use meeting date
- Convert title to lowercase with hyphens
- Remove special characters
- Examples: `2026-01-27-strategy-sprint-standup.md`, `2026-01-14-marcel-jason-weekly.md`

**File Structure:**

```markdown
# Meeting Title

<metadata>
date: YYYY-MM-DD
time: HH:MM UTC
duration: X minutes
organizer: email@example.com
participants: Name1, Name2, Name3
fireflies_id: <meeting_id>
meeting_link: <zoom/meet link if available>
transcript_url: https://app.fireflies.ai/view/<meeting_id>
</metadata>

---

## Summary

<2-3 sentence summary of what was covered and key outcomes>

---

## Context

<1-2 paragraphs explaining why this meeting happened and where it fits>

---

## Relevance

**To <Area 1>:**
- Bullet points on impact/relevance
- Include specific numbers, names, deadlines

**To <Area 2>:**
- More relevant points

---

## Overview

<Bullet points from shorthand_bullet or overview>

---

## Key Topics

### <Topic 1>

<Content from notes section, organized by theme>

### <Topic 2>

<More organized content>

---

## Action Items

**<Person 1>**
- Action item with deadline if available
- Another action

**<Person 2>**
- Their action items

---

## Transcript

**Speaker Name:** Dialogue text here.

**Another Speaker:** Their response goes here.

<Continue full transcript with speaker labels>
```

**Assembling the file efficiently:**

For single meetings, write the full file inline. For batch processing or large transcripts:
1. Write the header through `## Transcript\n` using the Write tool
2. Append the formatted transcript using shell: `cat /tmp/meeting_transcript.md >> "FILEPATH"`

This avoids reading large transcripts into context.

### Step 7: Update Contact Dossiers & Index Files

**This step is NOT optional.** After saving the transcript, apply the full **contact–transcript linking** rule (`.cursor/rules/contact-transcript-linking.mdc`):

1. **Identify** all named external participants from the transcript
2. **Match** against existing dossiers in `records/contacts/`
3. **Update existing dossiers:** add transcript to Meeting Transcripts, add Timeline entry, merge any new details, bump `last_updated`
4. **Auto-create dossiers** for significant new contacts (speakers, decision-makers, repeat contacts) — don't ask, just create with `confidence: low`
5. **Tag the transcript** with a `## Related Contacts` section linking to all participant dossiers
6. **Update `records/contacts/INDEX.md`** — add rows for any newly created dossiers
7. **Update `records/transcripts/INDEX.md`** — add the new transcript entry

### Step 8: Report Back

After saving, confirm:
- File saved to: `/records/transcripts/<filename>.md`
- Meeting: <title>
- Date: <date>
- Duration: <duration> minutes
- Participants: <count> people
- Key topics: <3-5 main topics>
- Contacts updated: <list of existing dossier files updated>
- New dossiers created: <list of new contact files auto-created>
- INDEX files updated: contacts/INDEX.md, transcripts/INDEX.md

## Writing Guidelines

When generating Summary, Context, and Relevance sections:
- **Direct and clear** - No corporate jargon
- **Lead with the point** - Most important info first
- **Use active voice** - "Marcel outlined" not "It was outlined by Marcel"
- **Ground in specifics** - Numbers, names, dates, concrete details
- **Connect to company context** - Reference GrowthX services, CheckThat, content strategy as relevant

## Edge Cases

### No audio captured
Some meetings have no transcript from Fireflies (Zoom recording issues, bot didn't join, etc.). When `fireflies_get_transcript` returns empty or no sentences:
- Still save the file with metadata, summary, and action items from the summary data
- In the Transcript section, write: `No transcript captured (audio not available).`

### Timezone shifts
Fireflies uses UTC timestamps. A meeting at 10pm UTC on Feb 4 may correspond to a file dated Feb 5 in local time (or vice versa). When comparing against existing files for deduplication, check +/- 1 day on the date prefix.

## Batch Mode

To pull multiple meetings at once (e.g., "pull all my meetings not yet saved"):

### Step 1: Search Fireflies
Search with participant filter and date range:
```
participants:marcel@growthxlabs.com from:2026-01-01 to:2026-02-11 limit:50
```
Extract titles, dates, IDs, and durations using a shell script to parse the JSON results.

### Step 2: List existing transcripts
List files in `records/transcripts/` to get all already-saved meetings.

### Step 3: Deduplicate
Compare Fireflies results against existing files:
- Match by date prefix + title keyword overlap (2+ matching words = likely same meeting)
- Account for UTC timezone shifts (+/- 1 day)
- Skip meetings under 5 minutes
- Skip untitled meetings (e.g., "marcel@growthxlabs.com - Untitled")
- Flag potential duplicates to the user rather than silently skipping

Use a Python script for this comparison (parse filenames, normalize titles, check overlap).

### Step 4: Present missing meetings
Show user a numbered table of meetings not yet saved:

| # | Date | Meeting | Duration |
|---|------|---------|----------|
| 1 | Feb 9 | Strategy Sprint Standup | 66m |
| 2 | Feb 5 | Deliver swat team check-in | 63m |

Ask: **"Pull all, select specific numbers (e.g., '1, 3, 5'), or skip short ones (under X minutes)?"**

### Step 5: Process in parallel
- For 1-3 meetings: process sequentially (fetch summary + transcript, write file)
- For 4+ meetings: use Task agents to process in parallel batches of 3-4
- Each Task agent fetches summaries + transcripts, formats using the script, and writes complete files

### Step 6: Format transcripts efficiently
Always use the formatter script for batch processing:
```bash
python3 .cursor/skills/pull-meeting/format-transcript.py CACHE_FILE.txt > /tmp/meeting_name_transcript.md
```
Then write header sections and append transcript via shell.

### Step 7: Update Contact Dossiers & Index Files
**This step is NOT optional.** After all transcripts are saved, run the full contact–transcript linking rule (`.cursor/rules/contact-transcript-linking.mdc`) as a batch:
- Collect all external participants across all new transcripts, deduplicate
- Update existing contact dossiers with new transcript links, timeline entries, and any new details
- Auto-create dossiers for significant new contacts (speakers, decision-makers, repeat contacts) with `confidence: low`
- Tag every new transcript with a `## Related Contacts` section
- Update `records/contacts/INDEX.md` with any new dossier entries
- Update `records/transcripts/INDEX.md` with all new transcript entries

### Step 8: Report summary
After all meetings are saved, report a summary table:

| # | Date | File | Duration | Key Topics |
|---|------|------|----------|------------|
| 1 | Feb 9 | `2026-02-09-strategy-sprint-standup.md` | 66m | Client status, kickoffs |

Note any meetings where audio was not captured. List contact dossiers that were updated and new ones that were auto-created. Confirm INDEX.md files were updated.
