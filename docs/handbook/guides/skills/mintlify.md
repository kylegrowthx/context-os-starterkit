<metadata>
purpose: Build and maintain documentation sites with Mintlify
source: https://handbook.growthx.ai/guides/skills/mintlify
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Mintlify

Teaches your AI editor how to build and maintain Mintlify documentation sites — creating pages, configuring navigation, using components, and setting up API references. Includes writing standards, file conventions, and the full workflow from research to deployment.

## Trigger phrases

- Creating docs pages or configuring navigation
- Adding Mintlify components to `.mdx` files
- Setting up API references
- Any documentation site maintenance

## What it does

Gives your AI editor deep knowledge of Mintlify's platform: the `docs.json` configuration schema, all available MDX components (accordions, tabs, steps, cards, callouts), page frontmatter options, and deployment workflows. It enforces writing standards — second-person voice, active language, sentence case headings, no marketing fluff — and knows how to organize navigation using tabs, groups, anchors, and dropdowns.

The skill also includes a verification checklist: frontmatter validation, code block language tags, internal link format, and broken link checks.

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/mintlify
curl -o .cursor/skills/mintlify/SKILL.md \
  https://raw.githubusercontent.com/growthxai/handbook/main/.cursor/skills/mintlify/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/mintlify
curl -o .agents/skills/mintlify/SKILL.md \
  https://raw.githubusercontent.com/growthxai/handbook/main/.cursor/skills/mintlify/SKILL.md
```

</CodeGroup>

**Source repo:** [growthx-handbook](https://github.com/growthxai/handbook) (public)
