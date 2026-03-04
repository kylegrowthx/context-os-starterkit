---
name: meeting-follow-up
description: Create Slack-friendly meeting follow-ups with action items, owners, and next steps. Use when the user asks to "create a follow-up", "write next steps", "summarize the meeting", "meeting recap", "action items from the call", or any post-meeting documentation task.
---

# Meeting Follow-up

Create Slack-friendly follow-up documents from meeting transcripts or notes with clear ownership, next steps, and questions for external stakeholders.

## Inputs / Outputs

| | What | Example |
|---|---|---|
| **Input** | Meeting transcript (Fireflies), raw notes, or both | Fireflies ID, pasted notes |
| **Context** | Client context file if client-related | `clients/[client]/[client]-client-context-v1.md` |
| **Tool** | Fireflies MCP for transcript retrieval | `fireflies_search`, `fireflies_get_transcript`, `fireflies_get_summary` |
| **Output** | Slack-formatted follow-up doc | `clients/[client]/deliverables/[project]/` or `pipeline/outputs/` |

## Workflow

### Step 1: Gather Meeting Content

1. If user provides a Fireflies URL or meeting name, search via `fireflies_search` and pull transcript + summary via `fireflies_get_transcript` and `fireflies_get_summary`
2. If user provides raw notes, use those as the primary source
3. If both are available, use the transcript for completeness and the raw notes for emphasis and priorities
4. Save the transcript to the appropriate `transcripts/` directory if it's client-related

### Step 2: Identify the Outputs

Ask or infer what's needed:

- **Internal follow-up only:** Action items and next steps for the team
- **Internal + external:** Internal follow-up plus questions or requests to send to an external party
- **External only:** A message or document to send to the other party

### Step 3: Draft the Follow-up

Use the Slack-friendly format described below. Extract:

- Action items with clear ownership
- Deadlines or timing
- Open questions that need answers
- Decisions that were made
- Technical findings or issues raised
- Scope boundaries (what's in, what's out)

### Step 4: Save and Offer to Send

1. Save the follow-up to the appropriate deliverables directory
2. If the user wants it posted to Slack, load the `slack-messaging` skill and send it

## Slack-Friendly Formatting Rules

These rules produce documents that paste cleanly into Slack without broken formatting.

**Do:**
- Use `**bold**` for section headers (renders as bold in Slack)
- Use flat bullet lists (`- [ ]` for action items, `-` for info) with owner in bold parentheses at the end: `**(Hassan)**`
- Use `**bold**` for emphasis within numbered lists
- Use `---` between sections for visual separation
- Keep everything in a single flat list per section, no nested sub-bullets
- Put the owner name in bold parentheses at the end of each task: `**(Name)**`, not as a separate heading

**Don't:**
- Don't use markdown headers (`#`, `##`, `###`). They don't render in Slack.
- Don't use markdown tables (`| col |`). They break in Slack.
- Don't use italic (`*single asterisks*`) for headers. Use bold (`**double asterisks**`).
- Don't group tasks under per-person headings. Use a flat list with `(Name)` at the end of each item.
- Don't use nested bullets or deep indentation. Keep it flat.

## Follow-up Template

```
**[Section Name]**

One-line description of what this section covers.

- [ ] Task description with enough context to act on. **(Owner)**
- [ ] Another task. **(Owner)**
- [ ] A third task that depends on the first. **(Owner + Owner)**

---

**[Next Section]**

- Item or finding with context
- Another item

---

**Timeline**

- Deliverable name: by [date] **(Owner)**
- Another deliverable: by [date] **(Owner)**

---

**Key Decisions**

1. **Decision name.** One sentence explaining what was decided and why.
2. **Another decision.** Context.
```

## Quality Checks

Before finishing, verify:

- [ ] No markdown headers (`#`) used anywhere in the body
- [ ] No markdown tables used
- [ ] All section titles use `**bold**` not headers or italics
- [ ] Every action item has an owner in bold parentheses `**(Name)**`
- [ ] Flat bullet lists only, no nesting
- [ ] Sections separated by `---`
- [ ] Decisions and timeline are present if applicable
- [ ] Document pastes cleanly into Slack

## Edge Cases

- **No transcript available (Fireflies MCP down):** Use raw notes only. Ask user to paste transcript if needed.
- **Internal + external outputs:** Create two separate documents. The internal one has full context. The external one is polished and appropriate for the other party.
- **No clear owners:** Ask the user to assign ownership before finalizing.
- **Multiple meetings to synthesize:** Combine into one follow-up but note which items came from which meeting.

## Example Usage

**User request:** "Create a follow-up from today's Vercel meeting with next steps for the team"

**Steps taken:**
1. Searched Fireflies for today's meeting, pulled transcript and summary
2. Saved transcript to `clients/vercel/transcripts/`
3. Extracted action items, grouped by phase, added owners in parentheses
4. Used flat bullet lists with bold section headers
5. Saved to `clients/vercel/deliverables/[project]/`
6. Offered to post to Slack

## Reference

- Existing example: `clients/vercel/deliverables/ai-gateway/ai-gateway-internal-follow-up-2026-03-03-v1.md`
