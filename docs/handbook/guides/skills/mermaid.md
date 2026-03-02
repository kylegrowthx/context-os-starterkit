<metadata>
purpose: Create mermaid diagrams in Mintlify documentation
source: https://handbook.growthx.ai/guides/skills/mermaid
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Mermaid diagrams

Teaches your AI editor how to create mermaid diagrams in `.mdx` files. Use it to replace ASCII art with proper visual flows, process diagrams, relationship maps, architectures, and sequence diagrams.

## Trigger phrases

- Replacing ASCII art with diagrams
- Visualizing flows, processes, or architectures in docs
- Creating sequence diagrams or org charts
- Any request for a visual diagram in `.mdx` files

## What it does

Covers when to use mermaid vs tables or prose, all node shapes and arrow styles, subgraph grouping, and Mintlify-specific options like hiding interactive controls. Includes critical syntax rules — no markdown inside node labels, real line breaks instead of `\n`, proper quoting for special characters, and MDX-safe angle bracket handling.

Common patterns included: linear flows, top-down hierarchies, fan-in/fan-out, and subgraph grouping.

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/mermaid
curl -o .cursor/skills/mermaid/SKILL.md \
  https://raw.githubusercontent.com/growthxai/handbook/main/.agents/skills/mermaid/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/mermaid
curl -o .agents/skills/mermaid/SKILL.md \
  https://raw.githubusercontent.com/growthxai/handbook/main/.agents/skills/mermaid/SKILL.md
```

</CodeGroup>

**Source repo:** [growthx-handbook](https://github.com/growthxai/handbook) (public)
