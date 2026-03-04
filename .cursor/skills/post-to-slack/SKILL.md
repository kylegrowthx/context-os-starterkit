---
name: post-to-slack
description: Post messages to Slack channels using the Slack MCP server. Use when the user wants to send a message to Slack, post an update, share content to a channel, or mentions posting to Slack.
---

# Post to Slack

Post messages to Slack channels via the Slack MCP server. Uses the full channel directory for lookup — no guessing, no API calls to find channels.

## Inputs / Outputs

| | What | Example |
|---|---|---|
| **Input** | Message content + channel name or description | "Post our Q1 update to #leaders" |
| **Tool** | Slack MCP server (`user-slack/slack_post_message`) | -- |
| **Output** | Confirmation of posted message | "Posted to #ceo-os" |

## Channel Lookup

**Always resolve channel names from the directory before posting.**

### Step 1 — Check quick-reference channels

| Channel | ID | Notes |
|---------|-----|-------|
| ceo-os | `C0AC7SMJLQ5` | **Default** — use when no channel specified |
| leaders | `C07EVDWTZ1D` | Leadership team |
| b-founders-only | `C08LG3LGTR7` | Founders only |
| ceo-support | `C081EG0U2DU` | CEO support |
| all-general | `C03066Q6BTL` | Company-wide |
| all-announcements | `C08MLAXQSAU` | Company-wide announcements |
| all-watercooler | `C03067PBPTM` | Casual / social |
| all-kudos | `C07U8NBEN0J` | Wins and shoutouts |
| b-epd | `C07PHGWKMB2` | Engineering, Product, Design |
| b-sales | `C087G6UU490` | Sales team |
| b-ops-general | `C08GJ0TFFJ5` | Ops team |
| d-general | `C07HD4ZALCW` | Delivery team |
| d-announcements | `C08LHTLUVFZ` | Delivery announcements |
| office-marcel | `C07C8KVNVRP` | Marcel's delegation channel |

### Step 2 — Read the full channel directory

If the channel is not in the quick-reference table above, **read the full channel directory**:

```
records/slack/slack-channel-index-v1.md
```

This file contains all 403 channels with their IDs, organized by category:
- `all-*` — Company-wide
- `b-*` — Business (sales, ops, EPD, GTM, projects)
- `d-*` — Delivery (general, pods, client channels)
- `d-ext-*` — External client channels (shared with client)
- `d-int-*` — Internal client channels (team only)
- `ext-*` — External partner / Slack Connect channels
- `proj-*` — Cross-functional project channels

**Search the file** for the channel name or a keyword from the user's request. Each row has the channel name, ID, and description.

### Step 3 — Fuzzy matching

When the user refers to a channel informally, match intent to the right channel:
- "post to the EPD channel" → `b-epd` (`C07PHGWKMB2`)
- "send to the Abnormal client channel" → `d-ext-abnormal` (`C08AM0P083B`)
- "post in the internal Brex channel" → `d-int-brex` (`C0A12B7RC0G`)
- "share in watercooler" → `all-watercooler` (`C03067PBPTM`)
- "post to kudos" → `all-kudos` (`C07U8NBEN0J`)
- "send to the sales channel" → `b-sales` (`C087G6UU490`)
- "post in the Webflow external channel" → `d-ext-webflow` (`C088VHW0G0K`)
- "share with the delivery team" → `d-general` (`C07HD4ZALCW`)

### Step 4 — Fallback

Only if the channel is not found in the directory file, use `slack_list_channels` MCP tool as a last resort.

## How to Post

```
Server: user-slack
Tool: slack_post_message
Arguments:
  - channel_id: The channel ID (from lookup above)
  - text: The message content
```

## Formatting

Slack uses its own markdown variant (mrkdwn):
- `*bold*` for **bold**
- `_italic_` for _italic_
- `~strikethrough~` for ~~strikethrough~~
- ``` `code` ``` for inline code
- `\n` for line breaks
- `•` for bullet points in message text
- `>` for blockquotes
- `<url|display text>` for named links

## Workflow

1. **Identify channel** — Check quick-reference table first, then read `records/slack/slack-channel-index-v1.md` if needed
2. **Confirm if ambiguous** — If the user's intent could match multiple channels, ask which one
3. **Compose message** — Format content using Slack mrkdwn syntax
4. **Post** — Call `slack_post_message` with the resolved channel_id and text
5. **Confirm** — Tell the user where the message was posted (channel name + link)

## Channel Naming Patterns

Use these patterns to quickly find the right channel type:

| User says | Channel pattern | Example |
|-----------|----------------|---------|
| "client channel for X" | `d-ext-{client}` | `d-ext-webflow` |
| "internal channel for X" | `d-int-{client}` | `d-int-webflow` |
| "the X pod" | `d-pod-{name}` | `d-pod-bailey` |
| "EPD alerts" | `b-epd-{type}` | `b-epd-alerts` |
| "the X project" | `b-proj-{name}` | `b-proj-ai-growth-summit` |
| "partner channel for X" | `ext-{partner}` | `ext-vercel-growthx` |
