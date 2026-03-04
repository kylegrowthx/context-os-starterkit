<metadata>
purpose: Convert mermaid diagrams into styled infographics
source: https://handbook.growthx.ai/guides/skills/mermaid-to-infographic
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Mermaid to infographic

Converts any mermaid diagram into a high-fidelity, on-brand "Nano Banana" infographic using Gemini image generation. Takes the abstract structure of a mermaid diagram and produces a polished visual with precise typography, color coding, and layout.

## Trigger phrases

- "Make this diagram look good"
- "Generate an infographic from this mermaid code"
- "Visualize this process/flowchart/mindmap"
- "Turn this into a stylized graphic"

## What it does

Analyzes the mermaid diagram's structure (root concept, branches, leaf nodes, edge labels), selects the right layout template (hierarchy, process flow, or comparison matrix), and constructs a detailed image generation prompt following the "Nano Banana" style guide.

The style guide defines specific hex colors (`#0118D8` blue for actions, `#E82561` pink for execution, `#FFCC00` yellow for highlights, `#00C4CC` teal for metrics), typography hierarchy, card styling, and the signature hand-drawn pink marker circle accent.

<Warning>
Requires **Gemini 3 Pro** or equivalent high-reasoning model for prompt construction.
</Warning>

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/mermaid-to-infographic
curl -o .cursor/skills/mermaid-to-infographic/SKILL.md \
  https://raw.githubusercontent.com/growthxai/handbook/main/.agents/skills/mermaid-to-infographic/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/mermaid-to-infographic
curl -o .agents/skills/mermaid-to-infographic/SKILL.md \
  https://raw.githubusercontent.com/growthxai/handbook/main/.agents/skills/mermaid-to-infographic/SKILL.md
```

</CodeGroup>

**Source repo:** [growthx-handbook](https://github.com/growthxai/handbook) (public)
