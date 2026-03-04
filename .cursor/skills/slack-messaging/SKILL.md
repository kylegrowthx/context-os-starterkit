---
name: slack-messaging
description: Send messages, reply to threads, and interact with Slack channels using proper formatting and user tagging. Use when the user asks to "send a slack message", "post to slack", "message someone on slack", "reply in slack", "tag someone", or any Slack communication task.
---

# Slack Messaging

Send properly formatted Slack messages with correct user mentions, channel routing, and contextual awareness.

## Inputs / Outputs

| | What | Example |
|---|---|---|
| **Input** | Message content, target channel/person, people to tag | "Send a message to #proj-vercel tagging Kirkland" |
| **User directory** | `records/slack-user-directory-v1.md` (always load first) | Name-to-ID lookup |
| **Tool** | MCP server: `project-0-context-os-starterkit-slack` | `slack_post_message`, `slack_reply_to_thread` |
| **Context tool** | MCP server: `user-fireflies` (if referencing a meeting) | `fireflies_search`, `fireflies_get_transcript` |
| **Output** | Sent Slack message with confirmation | Message timestamp and channel |

## Workflow

### Step 1: Resolve Users

1. Read `records/slack-user-directory-v1.md`
2. Find every person mentioned in the request by matching against real name, display name, or first name
3. If a person is NOT found in the directory, re-paginate ALL users via `slack_get_users` (follow pagination cursors until `next_cursor` is empty), find the match, and update the directory file
4. If still not found after full pagination, ask the user for the person's Slack username or email
5. Store resolved IDs for use in the message draft

**Never use plain text @names. Every mention must be `<@USER_ID>` format.**

### Step 2: Resolve Channel

1. If the user provides a channel ID (starts with `C`, `D`, or `G`), use it directly
2. If the user provides a channel name, use `slack_list_channels` with pagination to find the matching channel ID
3. If the channel is private and lookup fails (missing `groups:read` scope), ask the user for the channel ID directly

### Step 3: Pull Meeting Context (if applicable)

If the message references a meeting, call, sync, or conversation:

1. Search Fireflies using `fireflies_search` with relevant keywords and today's date
2. Pull the summary or full transcript using `fireflies_get_summary` or `fireflies_get_transcript`
3. Extract key points, action items, and relevant context to inform the draft
4. Skip this step if the message is not meeting-related

### Step 4: Check Channel History

1. Read the last 5-10 messages via `slack_get_channel_history` for the target channel
2. Check for ongoing conversations or context that the message should acknowledge or avoid repeating
3. Note any active threads that the message might be better suited as a reply to

### Step 5: Decide Message Type

Determine how to send:

- **New message**: Use `slack_post_message` for standalone messages to a channel
- **Thread reply**: Use `slack_reply_to_thread` if responding to an existing message (requires `thread_ts`)
- **DM**: Use `slack_post_message` with a user ID as the `channel_id` (requires `im:write` scope)

If unclear, ask the user: "Should this be a new message in the channel or a reply to an existing thread?"

### Step 6: Draft the Message

Apply Slack formatting conventions:

| Element | Slack Syntax |
|---------|-------------|
| Bold | `*text*` |
| Italic | `_text_` |
| Link | `<url\|label>` |
| User mention | `<@USER_ID>` |
| Channel mention | `<#CHANNEL_ID>` |
| Inline code | `` `code` `` |
| Blockquote | `> text` |
| Numbered list | `1. item` (plain text, Slack renders it) |

**Bot identity awareness**: Messages are sent as the bot ("George Cursor Agent"), not as the user. For personal, sensitive, or high-stakes messages, flag this and suggest the user copy/paste and send manually from their own account.

### Step 7: User Confirms

1. Show the full drafted message to the user exactly as it will appear
2. Call out who will be tagged and in which channel
3. Wait for explicit confirmation before sending
4. Never send without approval

### Step 8: Send and Verify

1. Post the message using the appropriate tool (`slack_post_message` or `slack_reply_to_thread`)
2. Confirm success and share the message timestamp for reference
3. If tagging failed or mentions didn't resolve, offer to send a follow-up thread reply with proper `<@USER_ID>` tags

## Quality Checks

Before sending, verify:

- [ ] All person mentions use `<@USER_ID>` format (no plain text @names)
- [ ] Links use `<url|label>` Slack syntax
- [ ] Bold uses `*text*` not `**text**`
- [ ] Message has been previewed and confirmed by the user
- [ ] Channel/thread routing is correct
- [ ] Bot identity flagged if message is personal or sensitive

## Bot Scope Reference

The bot (`project-0-context-os-starterkit-slack`) currently has:

| Scope | What it does |
|-------|-------------|
| `chat:write` | Send messages |
| `channels:read` | List public channels |
| `channels:history` | Read public channel history |
| `reactions:write` | Add emoji reactions |
| `users:read` | List users |
| `users.profile:read` | View user profiles |

**Known limitations (missing scopes):**

| Missing Scope | Impact | Workaround |
|---------------|--------|------------|
| `groups:read` | Cannot list private channels | Ask user for channel ID |
| `chat:update` | Cannot edit sent messages | Send correction as follow-up |
| `im:write` | Cannot initiate DMs | Add scope or user sends manually |
| `im:history` | Cannot read DM history | N/A |

## Edge Cases

- **User not in directory or API**: Ask for their Slack username or email, then update the directory
- **Private channel lookup fails**: Ask user for the channel ID (visible in Slack channel details)
- **Message references a meeting**: Pull Fireflies transcript before drafting (Step 3)
- **Sensitive or personal message**: Flag bot identity, suggest manual send
- **Directory is stale**: If a lookup fails, re-paginate all users and update `records/slack-user-directory-v1.md` before giving up
- **Multiple people with similar names**: Show matches and ask user to confirm which person

## Example Usage

**User request:** "Send a slack message to Kirkland and Tamy in proj-vercel about tomorrow's kickoff"

**Steps taken:**
1. Loaded `records/slack-user-directory-v1.md`, found Kirkland Gee (`U08JG4CFCGM`) and Tamyres Ogasawara (`U0A054TT7KP`)
2. Resolved channel "proj-vercel" to `C0AH2PAFQN8` via `slack_list_channels`
3. Checked Fireflies for related meeting transcripts, pulled context
4. Read last 10 messages in channel for context
5. Drafted message with `<@U08JG4CFCGM>` and `<@U0A054TT7KP>` mentions
6. Showed draft to user, got confirmation
7. Sent via `slack_post_message`, confirmed success
