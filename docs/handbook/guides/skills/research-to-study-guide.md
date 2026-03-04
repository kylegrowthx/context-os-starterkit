<metadata>
purpose: Deep research on any topic synthesized into a comprehensive study guide
source: https://handbook.growthx.ai/guides/skills/research-to-study-guide
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Research to study guide

Transform any topic into a comprehensive study guide through systematic research, quality validation, and audience-focused synthesis. Takes a topic and learner profile, conducts structured web research, and produces a guide with foundations, frameworks, key practitioners, examples, and a curated source library.

## Trigger phrases

- "Research [topic]" or "create a study guide"
- "Learn about [topic]" or "deep dive into [topic]"
- "Become an expert in [topic]"

## What it does

Runs a 4-phase workflow: setup (audience analysis), generate research questions across 6 categories (foundations, frameworks, practitioners, sources, examples, skills), execute research with source quality scoring (1-5 scale), quality checkpoint (targets: 3+ frameworks, 5+ experts, 30+ sources, 5+ examples), and synthesis into a structured study guide.

Includes anti-hallucination rules (never guess URLs, never invent sources, cite everything), subdirectory routing for output files, and a detailed template for the final guide including learning paths and curated appendices.

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/research-to-study-guide
curl -o .cursor/skills/research-to-study-guide/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/research-to-study-guide/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/research-to-study-guide
curl -o .agents/skills/research-to-study-guide/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/research-to-study-guide/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private).
</Note>
