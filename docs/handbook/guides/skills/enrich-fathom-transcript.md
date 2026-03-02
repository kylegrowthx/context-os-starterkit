<metadata>
purpose: Make Fathom transcripts production-ready with speaker fixes and analysis
source: https://handbook.growthx.ai/guides/skills/enrich-fathom-transcript
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Enrich Fathom transcript

Takes a script-generated Fathom transcript and makes it production-ready. Uses both the markdown file and the original JSON source files to fix speaker labels, rewrite the summary, write Context and Relevance sections, clean action items, and polish the transcript.

## Trigger phrases

- "Enrich fathom transcript" or "clean up fathom"
- "Fix fathom speakers" or "fix transcript"
- "Production-ready transcript"

## What it does

Reads all source JSON files (participants.json, metadata.json, transcript.json, action-items.json) alongside the markdown file for ground-truth speaker identification. Then runs a 10-step workflow:

1. **Identify speakers** — match device names, numbers, and display names to real people using participants.json, direct name address in transcript, role/context clues, and action item attribution
2. **Fix metadata** — verify every field against source JSON, add `enriched_on` timestamp
3. **Rewrite summary** — 2-3 sentences with specific outcomes, decisions, and next steps
4. **Write context** — who is the client, relationship stage, backstory
5. **Write relevance** — grouped bullets by GrowthX business area with specifics
6. **Review overview** — check Fathom's key takeaways for accuracy
7. **Review key topics** — spot-check topic subsections against transcript
8. **Fix action items** — real names with company affiliations, split shared-device items
9. **Clean transcript** — replace device names, remove noise, light cleanup
10. **Final review** — verification checklist

Supports batch mode with parallel processing of 3-4 transcripts at a time.

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/enrich-fathom-transcript
curl -o .cursor/skills/enrich-fathom-transcript/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/enrich-fathom-transcript/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/enrich-fathom-transcript
curl -o .agents/skills/enrich-fathom-transcript/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/enrich-fathom-transcript/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private).
</Note>
