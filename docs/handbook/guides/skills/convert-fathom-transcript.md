<metadata>
purpose: Convert Fathom JSON backups into formatted transcript markdown
source: https://handbook.growthx.ai/guides/skills/convert-fathom-transcript
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Convert Fathom transcript

Converts raw JSON data from Fathom backups into formatted markdown transcript files. A two-phase process: deterministic script conversion (no LLM needed) followed by optional LLM enrichment for Context and Relevance sections.

## Trigger phrases

- "Convert fathom" or "fathom to transcript"
- "Import fathom meetings" or "process fathom dump"

## What it does

Phase 1 is a Python script (`convert-to-transcript.py`) that reads Fathom's JSON files (metadata, summary, transcript, action items, participants) and produces a structured markdown file with all sections filled deterministically. Supports single meetings, batch by month, or all downloaded meetings. Handles deduplication, missing data gracefully, and requires no external dependencies (Python 3 stdlib only).

Phase 2 is optional LLM enrichment: generating the Context and Relevance sections, fixing participant name deduplication, and identifying unrecognized speakers. Can be run immediately or deferred.

<Warning>
Requires the `convert-to-transcript.py` script and raw JSON data from the fathom-backup skill.
</Warning>

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/convert-fathom-transcript
curl -o .cursor/skills/convert-fathom-transcript/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/convert-fathom-transcript/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/convert-fathom-transcript
curl -o .agents/skills/convert-fathom-transcript/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/convert-fathom-transcript/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private). Also requires the companion `convert-to-transcript.py` script.
</Note>
