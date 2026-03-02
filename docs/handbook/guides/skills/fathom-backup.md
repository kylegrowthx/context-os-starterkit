<metadata>
purpose: Download and archive Fathom meeting data as raw JSON
source: https://handbook.growthx.ai/guides/skills/fathom-backup
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Fathom backup

Downloads raw meeting data from Fathom's API and saves it as organized JSON files. Supports single meetings, batches, or a full archive of thousands of meetings.

## Trigger phrases

- "Backup fathom" or "download fathom meetings"
- "Fathom backup" or "archive meetings from fathom"
- "Continue fathom backup" or "resume fathom download"

## What it does

Uses a shell script (`dump-meeting.sh`) that queries Fathom's API with a narrow time-window lookup for speed (~2-3 seconds per meeting). Each meeting produces 7 JSON files: full API response, metadata, participants, summary, transcript, raw transcript, action items, and CRM matches.

Tracks download status in an INDEX.md file (`[x]` downloaded, `[ ]` pending). Supports three workflows: single meeting by recording ID, batch download (oldest-first or by month), and full archive mode for thousands of meetings.

The downloaded JSON serves as the source data for the convert-fathom-transcript and enrich-fathom-transcript skills.

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/fathom-backup
curl -o .cursor/skills/fathom-backup/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/fathom-backup/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/fathom-backup
curl -o .agents/skills/fathom-backup/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/fathom-backup/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private). Also requires the companion `dump-meeting.sh` script and Fathom API access.
</Note>
