# Meeting Records

Calendar-sourced meeting records synced from Google Calendar.

## What's Here

Structured records of past meetings, each containing attendees, metadata, and links to Fireflies transcripts when available. These are lighter-weight than full transcript files in `records/transcripts/` — they capture *that* a meeting happened, *who* was there, and *where* to find the full transcript.

## How Records Are Created

Records are created by the `sync-meetings` skill, which:
1. Pulls events from Google Calendar
2. Filters to real meetings (excludes personal blocks, solo events)
3. Matches against Fireflies transcripts
4. Creates a structured record with attendee info and transcript links
5. Updates contact dossiers for external attendees

## Structure

Files are organized by year-month:

```
records/meetings/
├── INDEX.md          # Full index with transcript status
├── README.md         # This file
├── .last-sync        # Last sync timestamp
├── 2026-02/          # February 2026 (84 meetings)
│   ├── 2026-02-02-checkthat-weekly-check-in.md
│   └── ...
├── 2026-01/          # January 2026 (70 meetings)
│   ├── 2026-01-05-carilu-marcel.md
│   └── ...
└── YYYY-MM/          # Future/past months
```

**File naming:** `YYYY-MM-DD-descriptive-meeting-name.md`

## Relationship to Transcripts

- `records/meetings/` = calendar-sourced metadata (who, when, links)
- `records/transcripts/` = full Fireflies transcripts with summaries, action items, and dialogue

A meeting record links *to* its transcript via the `transcript_file` metadata field (e.g., `records/transcripts/2026-02/filename.md`). The transcript is the richer document. If you need the full conversation, follow the link to `records/transcripts/`.

## Sync State

- `.last-sync` — ISO date of the last successful sync
- `.sync-log` — append-only log of sync runs (date, count, errors)

## Related

- `records/transcripts/` — Full meeting transcripts from Fireflies
- `records/contacts/` — Contact dossiers linked from meeting attendees
- `.cursor/skills/sync-meetings/` — The skill that creates these records
- `.cursor/skills/pull-meeting/` — Pull full transcripts from Fireflies
