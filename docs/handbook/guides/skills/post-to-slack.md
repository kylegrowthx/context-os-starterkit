<metadata>
purpose: Send messages to Slack channels via MCP
source: https://handbook.growthx.ai/guides/skills/post-to-slack
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Post to Slack

Posts messages to Slack channels using the Slack MCP server. Includes a full channel directory with 400+ channels so your AI editor can resolve channel names instantly — no API calls to look up channels.

## Trigger phrases

- "Post to Slack" or "send a message to [channel]"
- "Share this in [channel]" or "post an update"

## What it does

Resolves channel names from a built-in quick-reference table (14 common channels with IDs) or the full 403-channel directory file. Supports fuzzy matching — "post to the EPD channel" resolves to `b-epd`, "send to the Abnormal client channel" resolves to `d-ext-abnormal`.

Formats messages using Slack's mrkdwn syntax (`*bold*`, `_italic_`, `>` blockquotes, `<url|display text>` links) and posts via the Slack MCP server.

Channel naming patterns: `d-ext-*` for external client channels, `d-int-*` for internal client channels, `b-*` for business channels, `all-*` for company-wide, `proj-*` for cross-functional projects.

<Warning>
Requires the Slack MCP server and the `slack-channel-index-v1.md` directory file.
</Warning>

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/post-to-slack
curl -o .cursor/skills/post-to-slack/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/post-to-slack/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/post-to-slack
curl -o .agents/skills/post-to-slack/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/post-to-slack/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private).
</Note>
