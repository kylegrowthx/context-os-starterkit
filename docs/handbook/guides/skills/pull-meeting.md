<metadata>
purpose: Pull meetings from Fireflies with full transcript enrichment
source: https://handbook.growthx.ai/guides/skills/pull-meeting
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Pull meeting

Master orchestrator that fetches a meeting from Fireflies, formats the raw data into markdown, enriches it with LLM analysis, and syncs all related records. Chains three skills together into a single pipeline: pull, enrich, and link.

## Trigger phrases

- "Pull meeting" or "get meeting"
- "Fireflies" or "meeting transcript"
- "Download transcript"

## What it does

Searches Fireflies by keyword, date range, or participant, then runs a 3-skill pipeline:

1. **Fetch and format** — calls Fireflies MCP for summary and transcript, runs `format-meeting.py` to produce a structured markdown file
2. **Enrich** — delegates to the enrich-fireflies-transcript skill for 10-step LLM enrichment (speaker fixes, summary rewrite, context, relevance, decisions, open questions)
3. **Link records** — delegates to the link-transcript-records skill to update meeting records, contact dossiers, and INDEX files

Supports both single meetings and batch mode (pull all meetings not yet saved). Each skill in the pipeline can also run independently.

<Warning>
Requires the Fireflies MCP server and the `format-meeting.py` script from the growthx-context repo.
</Warning>

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/pull-meeting
curl -o .cursor/skills/pull-meeting/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/pull-meeting/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/pull-meeting
curl -o .agents/skills/pull-meeting/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/pull-meeting/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private). Also requires the companion `format-meeting.py` script from the same skill directory.
</Note>
