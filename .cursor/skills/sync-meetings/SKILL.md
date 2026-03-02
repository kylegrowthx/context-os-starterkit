---
name: sync-meetings
description: Sync past calendar meetings into records/meetings/ with transcript linking and contact updates. Use when the user wants to sync meetings, pull calendar history, create meeting records, log past meetings, or reconcile calendar with transcripts. Triggers on "sync meetings", "pull my calendar", "log meetings", "meeting history", "calendar sync", "what meetings did I have", or any request to review/record past meetings from Google Calendar.
---

# Sync Meetings

Pull past meetings from Google Calendar, create structured meeting records in `records/meetings/`, match them against Fireflies transcripts, and update contact dossiers.

## Inputs / Outputs

| | What | Example |
|---|---|---|
| **Input** | Time range (default: since last sync) | "Sync my meetings from last week" |
| **Tools** | Google Calendar MCP, Fireflies MCP, filesystem | — |
| **Output** | Meeting records in `records/meetings/YYYY-MM/`, updated contact dossiers, transcript cross-links | `records/meetings/2026-02/2026-02-23-growthx-coralogix-partnership.md` |

## Overview

This skill:
1. Reads the last sync timestamp from `records/meetings/.last-sync`
2. Pulls all calendar events from Google Calendar since that timestamp
3. Filters out non-meetings (personal blocks, all-day events, solo events)
4. For each real meeting, searches Fireflies for a matching transcript
5. Creates a structured meeting record in `records/meetings/`
6. Updates or creates contact dossiers for external attendees
7. Writes the new sync timestamp

## Workflow

### Step 1: Determine Time Range

Check for `records/meetings/.last-sync` file:
- **If it exists:** read the ISO date inside and use it as the start date
- **If it doesn't exist:** ask the user how far back to go (suggest "past 2 weeks" as default for first run)
- **If user specifies a range:** use that instead (e.g., "sync meetings from last week")

The end date is always "now" (today's date minus a few hours buffer — don't sync meetings that haven't happened yet).

### Step 2: Pull Calendar Events

Use `gcal_list_events` with:
- `calendarId`: `primary`
- `timeMin`: start of range
- `timeMax`: end of range (now)
- `timeZone`: `America/New_York` (Marcel's timezone)
- `condenseEventDetails`: `false` (we need attendee lists)
- `maxResults`: `250`

Paginate if `nextPageToken` is returned — keep pulling until all events are collected.

### Step 3: Filter to Real Meetings

Not every calendar event is a meeting worth recording. Apply these filters:

**Include** if ALL of these are true:
- Has 2+ attendees (not just Marcel)
- Marcel's response is `accepted` or `tentative` (not `declined`)
- Duration is between 10 minutes and 4 hours
- Not an all-day event

**Exclude** events matching these patterns (case-insensitive title substring match):
- Personal blocks: "deep work", "buffer", "lunch", "break", "focus time", "heads down", "blocked", "hold", "commute", "gym", "workout", "personal"
- Admin: "OOO", "out of office", "PTO", "vacation", "holiday"
- Routine / filler: "prep", "travel", "dinner", "breakfast", "coffee chat", "end of day", "morning routine", "wind down", "wrap up", "do not book", "block", "busy", "reserved"
- Personal appointments: "therapy", "family time", "daycare", "coaching", "reservation at", "reservation for"
- Tasks (not meetings): "set up social", "set up posting"

**Also exclude** exact title matches (case-insensitive) for known non-meetings like restaurant names.

When in doubt, include the event — it's better to have a record you can delete than to miss a meeting.

### Step 4: Check for Existing Records

Before creating records, check what's already in `records/meetings/YYYY-MM/`:
- Determine the year-month subfolder from the event date (e.g., `2026-02/`)
- Create the subfolder if it doesn't exist
- List all files in the subfolder
- For each calendar event, check if a file already exists with a matching date prefix and similar title keywords (2+ word overlap)
- Also check `records/transcripts/YYYY-MM/` — if a full transcript already exists for this meeting, still create a meeting record but mark it as `has_transcript: true` and link to it
- Skip events that already have meeting records

### Step 5: Match Against Fireflies Transcripts

For each meeting that needs a record, search Fireflies:
- Search by date range: the meeting's date ±1 day (timezone shifts)
- Search by keyword: key words from the meeting title
- Search by participant: if attendee emails are available

A match is good if:
- The Fireflies meeting date is within ±1 day of the calendar event
- Title keywords overlap (2+ words match)
- OR participant emails overlap

If matched, capture the Fireflies `meeting_id` and `transcript_url`.

**Batch this efficiently:** Don't search Fireflies one-by-one for each meeting. Instead:
1. Pull a broad Fireflies search for the entire sync date range: `from:YYYY-MM-DD to:YYYY-MM-DD participants:marcel@growthxlabs.com limit:50`
2. Also search with `participants:marcel@growthx.ai` if results seem incomplete
3. Build a lookup table of Fireflies meetings by date + title keywords
4. Match calendar events against this lookup table

### Step 6: Create Meeting Records

For each meeting, create a file in `records/meetings/YYYY-MM/` (the year-month subfolder matching the event date).

**Filename:** `YYYY-MM-DD-descriptive-meeting-name.md`
- Use the calendar event date
- Convert the event title to lowercase with hyphens
- Remove special characters, angle brackets, company separators like `<>` or `|`
- Example: `2026-02-23-growthx-coralogix-partnership-next-steps.md`

**File structure:**

```markdown
# Meeting Title

<metadata>
date: YYYY-MM-DD
time: HH:MM ET
duration: X minutes
organizer: email@example.com
attendees: Name1 (email1), Name2 (email2)
calendar_event_id: <google calendar event id>
has_transcript: true | false
fireflies_id: <meeting_id or empty>
transcript_url: https://app.fireflies.ai/view/<meeting_id> (or empty)
transcript_file: records/transcripts/YYYY-MM/YYYY-MM-DD-meeting-name.md (if exists in records/)
last_updated: YYYY-MM-DD
</metadata>

---

## Attendees

| Name | Email | Role | Company | Contact File |
|------|-------|------|---------|--------------|
| Marcel Santilli | marcel@growthxlabs.com | CEO | GrowthX | (internal) |
| Brian Mullen | brian@coralogix.com | CMO | Coralogix | [dossier](../contacts/brian-mullen-v1.md) |

---

## Notes

_No notes yet. Run `pull meeting` to fetch the full transcript, or add notes manually._
```

If the meeting has a Fireflies transcript that's already been pulled into `records/transcripts/`, add a link:

```markdown
## Transcript

Full transcript available: [View transcript](../transcripts/YYYY-MM-DD-meeting-name.md)
```

If there's a Fireflies match but the transcript hasn't been pulled yet:

```markdown
## Transcript

Transcript available in Fireflies but not yet pulled. Run: `pull meeting <meeting title>`
Fireflies URL: https://app.fireflies.ai/view/<meeting_id>
```

### Step 7: Update Contact Dossiers

For each meeting record created, process external attendees:

1. **Identify external attendees** — anyone not @growthxlabs.com or @growthx.ai
2. **Check for existing dossier** in `records/contacts/`
3. **If dossier exists:**
   - Add the meeting to the `## Meeting Transcripts` section (or create a `## Meetings` section if that's more appropriate for non-transcript meetings)
   - Add a timeline entry: `| YYYY-MM-DD | Calendar meeting: Meeting Title |`
   - Update `last_updated`
4. **If no dossier exists** and the person is a significant contact (decision-maker, client contact, spoke in meeting, appeared in 2+ meetings):
   - Auto-create a minimal dossier using the contact-dossier skill template
   - Set `confidence: low`
   - Populate what's known: name, email, company (from email domain or calendar event)

### Step 8: Update INDEX Files

After all records are created:

1. **`records/meetings/INDEX.md`** — add rows for all new meeting records
2. **`records/contacts/INDEX.md`** — add rows for any newly created contact dossiers

### Step 9: Update Sync Timestamp

Write today's date (ISO format) to `records/meetings/.last-sync`:
```
2026-02-26
```

### Step 10: Report Summary

Present results in a summary table:

```
## Sync Complete

**Range:** Feb 20 – Feb 26, 2026
**Events scanned:** 47
**Filtered to meetings:** 18
**Already recorded:** 5
**New records created:** 13
**With Fireflies transcripts:** 8
**Transcripts not yet pulled:** 3

| Date | Meeting | Duration | Transcript | Contacts |
|------|---------|----------|------------|----------|
| Feb 23 | GrowthX <> Coralogix Partnership | 30m | ✓ linked | Brian Mullen (updated) |
| Feb 23 | CheckThat Weekly Check In | 30m | ✓ available | — (internal) |
| Feb 22 | Brex Content Review | 60m | ✗ none | Jon Kowieski (updated) |

**Contacts updated:** 5 existing dossiers
**New contacts created:** 2 (confidence: low)
**Transcripts to pull:** Run `pull meeting` for: CheckThat Weekly, Strategy Sprint
```

## Attendee Resolution

Calendar events often only have email addresses. To get names:
1. Check existing contact dossiers for email matches
2. Parse the email (firstname.lastname@company.com → Firstname Lastname)
3. Check HubSpot contacts if available
4. Use the display name from the calendar event if provided

## Edge Cases

### Recurring meetings
Each occurrence is a separate record. Don't create duplicate records for the same occurrence.

### Cancelled or declined meetings
Skip events where `status` is `cancelled` or `myResponseStatus` is `declined`.

### External calendar invites
Meetings organized by people outside GrowthX should still be recorded — the organizer email just won't be @growthxlabs.com.

### Large syncs (first run)
For the first sync or syncs covering > 2 weeks, process in batches:
- Pull calendar events in 1-week chunks
- Pull Fireflies results for the full range once
- Create records sequentially (don't overload the filesystem)

### Meetings with no attendee info
Some calendar events don't list attendees (e.g., manually created events). If the title suggests it's a real meeting (contains a person's name or company name), include it but mark attendees as `unknown`.

## Scheduling

This skill is designed to run both on-demand and as a scheduled weekly task. The `.last-sync` file makes incremental syncs efficient — each run only processes new meetings since the last sync.

When run as a scheduled task, the skill should:
- Not ask any clarifying questions (use defaults)
- Use `.last-sync` for the time range
- Create records silently
- Save a sync log to `records/meetings/.sync-log` (append mode) with date, count, and any errors
