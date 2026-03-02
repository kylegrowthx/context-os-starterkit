<metadata>
purpose: Sync Google Calendar meetings into structured records with transcript linking
source: https://handbook.growthx.ai/guides/skills/sync-meetings
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Sync meetings

Pulls past meetings from Google Calendar, creates structured meeting records, matches them against Fireflies transcripts, and updates contact dossiers. Runs both on-demand and as a scheduled weekly task.

## Trigger phrases

- "Sync meetings" or "pull my calendar"
- "Log meetings" or "meeting history"
- "Calendar sync" or "what meetings did I have"

## What it does

Reads the last sync timestamp, pulls all calendar events since then, filters out non-meetings (personal blocks, all-day events, admin time) using smart title matching, then for each real meeting:

1. Checks for existing records to avoid duplicates
2. Searches Fireflies for matching transcripts (by date, title keywords, and participant emails)
3. Creates a structured meeting record with attendees table, transcript links, and metadata
4. Updates or creates contact dossiers for external attendees
5. Updates INDEX files and writes the new sync timestamp

Includes intelligent filtering with exclude patterns for personal blocks, admin time, and non-meeting calendar events. Supports incremental syncs via `.last-sync` file and batch processing for first-run historical syncs.

<Warning>
Requires the Google Calendar MCP server and optionally the Fireflies MCP server for transcript matching.
</Warning>

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/sync-meetings
curl -o .cursor/skills/sync-meetings/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/sync-meetings/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/sync-meetings
curl -o .agents/skills/sync-meetings/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/sync-meetings/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private).
</Note>
