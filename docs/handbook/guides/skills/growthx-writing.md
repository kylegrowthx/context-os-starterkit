<metadata>
purpose: Write and review content using GrowthX voice and style
source: https://handbook.growthx.ai/guides/skills/growthx-writing
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# GrowthX writing

Write like a smart friend explaining something important. This skill teaches your AI editor GrowthX's voice — direct, clear, real — and applies it to blog posts, newsletters, thought leadership, product copy, and content reviews.

## Trigger phrases

- "Write", "draft", "edit", or "review" content
- Creating blog posts, newsletters, or thought leadership
- Any content that needs GrowthX voice

## What it does

Loads the GrowthX writing style guide and applies it to everything: lead with the point, maximum clarity with minimum words, write like you talk, ground in specifics. Channels writers like Paul Graham (conversational precision), Naval (compressed wisdom), and Hemingway (raw simplicity).

Includes a content review framework with severity levels (must fix, improve, optional), quality checks (main point in first two sentences, would you say this to a friend, can you cut 20%), and before/after transformation examples.

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/growthx-writing
curl -o .cursor/skills/growthx-writing/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/growthx-writing/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/growthx-writing
curl -o .agents/skills/growthx-writing/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/growthx-writing/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private).
</Note>
