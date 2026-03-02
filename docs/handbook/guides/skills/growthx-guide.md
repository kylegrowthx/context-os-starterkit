<metadata>
purpose: Create handbook guide pages matching GrowthX voice and quality standards
source: https://handbook.growthx.ai/guides/skills/growthx-guide
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# GrowthX guide writer

Produces handbook guides in GrowthX's voice — direct, clear, real. Each guide is an MDX file that follows a consistent structure, uses Mintlify components correctly, and passes both voice quality checks and AI-tell detection.

## Trigger phrases

- "Write a guide" or "handbook page"
- Creating `.mdx` content for the handbook
- Rewriting or auditing existing guide quality

## What it does

Walks through an 8-step writing workflow: research and outline, write the opening hook, write each section, apply Mintlify components, run AI-tell cleanup (kill list scan, em dash removal, structure scan), MDX validation, quality checks (first-sentence test, read-aloud test, cut test, Graham test), and cross-linking audit.

Includes domain adaptations for finance, product/technical, and client-facing topics. Enforces the GrowthX voice: conversational precision, one idea per sentence, active voice, grounded in specifics.

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/growthx-guide
curl -o .cursor/skills/growthx-guide/SKILL.md \
  https://raw.githubusercontent.com/growthxai/handbook/main/.skills/skills/growthx-guide/growthx-guide/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/growthx-guide
curl -o .agents/skills/growthx-guide/SKILL.md \
  https://raw.githubusercontent.com/growthxai/handbook/main/.skills/skills/growthx-guide/growthx-guide/SKILL.md
```

</CodeGroup>

**Source repo:** [growthx-handbook](https://github.com/growthxai/handbook) (public)
