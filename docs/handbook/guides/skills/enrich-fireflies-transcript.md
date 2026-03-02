<metadata>
purpose: 10-step enrichment for Fireflies transcripts
source: https://handbook.growthx.ai/guides/skills/enrich-fireflies-transcript
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Enrich Fireflies transcript

Takes a script-generated Fireflies transcript markdown file and makes it production-ready. Fixes speaker labels, rewrites the summary, generates analysis sections, cleans action items, and polishes the raw transcript.

## Trigger phrases

- "Enrich fireflies transcript" or "enrich transcript"
- "Clean up fireflies" or "fix fireflies transcript"
- "Production-ready transcript" or "finish transcript"

## What it does

Reads the full file (including transcript) and performs 10-step enrichment:

1. **Verify speaker labels** — match device names and numbers to real people using transcript evidence (direct name address, role clues, self-identification)
2. **Fix metadata** — verify dates, times, participants, add `enriched_on` timestamp
3. **Rewrite summary** — 2-3 sentences answering what happened, what was decided, what's next
4. **Write context** — who are these people, what's the relationship, why did this meeting happen
5. **Write relevance** — multi-dimensional impact analysis grouped by GrowthX business areas
6. **Write decisions and commitments** — explicit agreements and promises
7. **Write open questions** — unresolved items needing follow-up
8. **Review overview and key topics** — accuracy and completeness checks
9. **Fix action items** — add company affiliations, fix names, merge duplicates
10. **Clean transcript** — replace incorrect labels, remove noise, light cleanup

Also renames the file from `draft-{id}.md` to a descriptive name. Supports batch mode for processing multiple transcripts.

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/enrich-fireflies-transcript
curl -o .cursor/skills/enrich-fireflies-transcript/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/enrich-fireflies-transcript/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/enrich-fireflies-transcript
curl -o .agents/skills/enrich-fireflies-transcript/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/enrich-fireflies-transcript/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private).
</Note>
