<metadata>
purpose: Sync local markdown files to Notion pages
source: https://handbook.growthx.ai/guides/skills/update-notion-doc
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Update Notion doc

Updates Notion pages from local markdown files while preserving Notion-specific elements like callouts, child pages, and databases. Handles the conversion from markdown to Notion's format automatically.

## Trigger phrases

- "Update Notion" or "sync to Notion"
- Providing a Notion URL and asking to update it

## What it does

Fetches the existing Notion page to understand its structure, reads the local markdown source, converts markdown tables to Notion XML format, and uses targeted content replacement to update the page while preserving elements that only exist in Notion (Related Docs callouts, child pages, embedded databases).

Includes a formatting reference for Notion-specific elements: callout icons and colors, empty blocks, page links, child page references, and database references. Supports both full page replacement and targeted range updates.

<Warning>
Requires the Notion MCP server (`user-Notion`).
</Warning>

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/update-notion-doc
curl -o .cursor/skills/update-notion-doc/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/update-notion-doc/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/update-notion-doc
curl -o .agents/skills/update-notion-doc/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/update-notion-doc/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private).
</Note>
