---
name: process-transcript
description: Process meeting transcripts into clean, structured, agent-readable documents and update client context. Use when the user asks to "process a transcript", "clean up this transcript", "save this meeting", "update context from the call", "extract action items", "what happened in this meeting", or any transcript ingestion and processing task.
---

# Process Transcript

Process any meeting transcript into a clean, standardized document with structured extractions, then propose updates to the client context file.

## Inputs / Outputs

| | What | Example |
|---|---|---|
| **Input** | Fireflies meeting (URL, name, or ID), pasted transcript, or existing file path | `"process the Vercel call from today"`, pasted text, file path |
| **Context** | Client context file (always load if client-related) | `clients/[client]/[client]-client-context-v1.md` |
| **Context** | Transcript template (reference for output format) | `records/transcripts/meeting-transcript-template-v1.md` |
| **Tool** | Fireflies MCP for transcript retrieval | `fireflies_search`, `fireflies_get_transcript`, `fireflies_get_summary` |
| **Output 1** | Cleaned, standardized transcript | `clients/[client]/transcripts/YYYY-MM-DD-client-meeting-type-transcript-v1.md` |
| **Output 2** | Proposed client context updates | Presented to user for approval, then applied to context file |
| **Output 3** | Follow-up document (optional) | Delegates to `meeting-follow-up` skill if requested |

## Quick Start

1. Get the transcript (Fireflies MCP, pasted text, or file path)
2. Identify the client and load their context file
3. Clean, standardize, and extract structured data
4. Save the processed transcript to the client's `transcripts/` directory
5. Propose updates to the client context file
6. Ask if the user wants a follow-up document (delegates to `meeting-follow-up` skill)

## Workflow

### Step 1: Ingest and Identify

**Get the raw transcript from one of three sources:**

1. **Fireflies MCP.** If the user provides a meeting name, URL, date, or keyword:
   - Search with `fireflies_search` using relevant filters (`keyword`, `from`/`to` dates, `participants`)
   - Pull the full transcript with `fireflies_get_transcript` using the meeting ID
   - Pull the AI summary with `fireflies_get_summary` using the same ID
   - Use both: the transcript for completeness, the summary for quick reference and to cross-check your extraction

2. **Pasted text.** If the user pastes a transcript directly, use it as-is.

3. **Existing file.** If the user points to a file already in the repo, read it and process from there.

**Identify meeting metadata:**

- **Client name:** Match to a directory under `clients/`. If ambiguous, ask.
- **Meeting date:** Extract from the transcript, Fireflies metadata, or ask.
- **Meeting type:** Categorize as one of: `weekly-sync`, `strategy-call`, `kickoff`, `deep-dive`, `sales-handoff`, `partnership-scope`, `internal-sync`, or a custom descriptor.
- **Participants:** Extract names and companies/roles from the transcript.
- **Duration:** From Fireflies metadata or estimate from transcript length.

**Load context:**

- Read the client context file: `clients/[client]/[client]-client-context-v1.md`
- Note the current Active Workstreams, Engagement History, and Relationship Context sections. You will compare against these in Step 4.

### Step 2: Clean and Standardize

Transform the raw transcript into the standard format.

**Speaker labels.** Normalize all speaker references to a consistent format:
- Format: `**Speaker Name (Company):**`
- Example: `**George Haikal (GrowthX):**`, `**Jon Kowieski (Brex):**`
- If the company is unknown, use the name only: `**Speaker Name:**`
- Replace inconsistent labels (first name only, misspellings, "Speaker 1") with the correct full name

**Content cleaning.** Improve readability while preserving meaning:
- Remove verbal fillers (um, uh, like, you know, I mean) when they add no meaning
- Remove false starts and repeated phrases
- Fix obvious transcription errors (wrong words from speech-to-text)
- Preserve the speaker's actual words and tone. Do not rephrase or paraphrase. The goal is a cleaner version of what was said, not a rewrite.
- Keep technical terms, product names, and proper nouns exactly as spoken

**Structure.** Organize the transcript body:
- Add topic section headers (`### Topic Name`) when the conversation shifts to a distinct new subject
- Use the topics to create a navigable document, not just a wall of dialogue
- Keep section headers descriptive: `### SEO Strategy for AI Gateway`, not `### Topic 3`

**File naming.** Use the convention: `YYYY-MM-DD-client-meeting-type-transcript-v1.md`
- Examples: `2026-03-03-vercel-ai-gateway-seo-transcript-v1.md`, `2026-02-26-brex-weekly-sync-transcript-v1.md`
- For internal meetings (no client), use: `YYYY-MM-DD-meeting-description-transcript-v1.md`

### Step 3: Extract and Analyze

Extract structured data from the transcript into the sections below. This is the most important step. Be thorough, specific, and accurate. Do not invent information not present in the transcript.

**Decisions made.**
- What was decided, by whom, and why
- Include the reasoning or context behind each decision
- Format: `**Decision name.** One sentence explaining what was decided and why.`

**Action items.**
- Specific tasks with clear ownership
- Include deadlines if mentioned, or flag as "no deadline mentioned"
- Format: `- [ ] Task description with enough context to act on. **(Owner)**`

**Key themes and topics.**
- Group discussion points by workstream or topic area
- For each theme: one-line summary of what was discussed and where it landed
- Connect themes to Active Workstreams in the client context file when possible

**Open questions.**
- Items raised but not resolved in the meeting
- Questions directed at external parties (client, partner)
- Internal questions the team needs to answer
- Format: `- Question or unresolved item. **(Who needs to answer)**`

**Stakeholder signals.**
- New people mentioned or introduced (potential additions to Relationship Context)
- Communication preferences revealed (e.g., "send me a doc before the call")
- Concerns, pushback, or enthusiasm expressed by stakeholders
- Internal dynamics hinted at (reporting lines, decision-making, politics)

**Scope changes.**
- Anything that shifted the engagement scope, strategy, or priorities
- New workstreams added or existing ones deprioritized
- Budget, timeline, or resource changes discussed

**Notable quotes.**
- Direct quotes that capture important positions, commitments, or insights
- Include speaker attribution and enough context to understand the quote standalone
- Format: `> "Quote text here." - Speaker Name, on [topic]`
- Limit to 3-5 most important quotes. These are for future reference, not a highlights reel.

### Step 4: Generate Outputs

**Primary output: Processed transcript file.**

Apply the standard template structure from `records/transcripts/meeting-transcript-template-v1.md`:

```
# YYYY-MM-DD: Meeting Description

<metadata>
purpose: Meeting transcript
audience: Team members reviewing meeting context
summary: [One sentence describing what was discussed]
token_estimate: [small/medium/large based on transcript length]
source: [Fireflies/Fathom/manual]
participants: [comma-separated list]
domain: client
confidence: current
context_tier: 3
last_updated: YYYY-MM-DD
</metadata>

---

## Meeting Details

| Field | Value |
|-------|-------|
| **Date** | YYYY-MM-DD |
| **Duration** | XX minutes |
| **Participants** | Names (Company/Role) |
| **Recording tool** | Fireflies / Fathom / manual |

## Summary

[2-3 sentences: what was discussed, what was decided, what happens next]

## Key Decisions

1. **Decision name.** What was decided and why.
2. **Another decision.** Context.

## Action Items

- [ ] Task description. **(Owner)**
- [ ] Another task. Deadline: [date]. **(Owner)**

## Key Themes

### [Theme/Workstream Name]
- What was discussed and where it landed

### [Another Theme]
- Summary

## Open Questions

- Question or unresolved item. **(Who needs to answer)**

## Stakeholder Signals

- [Signal with context]

## Notable Quotes

> "Quote text." - Speaker Name, on [topic]

## Transcript

### [Topic Section Header]

**Speaker Name (Company):** Dialogue text here.

**Another Speaker (Company):** Response text here.

### [Next Topic]

...
```

**Token estimate guide:**
- Small: under 200 lines
- Medium: 200-800 lines
- Large: 800+ lines

**Save location:**
- Client meetings: `clients/[client]/transcripts/`
- Internal meetings (no client): `records/transcripts/`
- Non-meeting transcripts (interviews, podcasts, etc.): `pipeline/research/` or ask the user

### Step 5: Update Client Context

This step is what makes transcript processing compound over time. Compare your extractions against the current client context file and propose specific updates.

**Read the current client context file** and check each section:

**Active Workstreams.** Compare the transcript's themes and action items against the listed workstreams.
- Are there new workstreams to add?
- Did any workstream's status change (blocked, unblocked, completed, deprioritized)?
- Did owners or priorities shift?
- Draft the updated workstream entries with specific language.

**File Map.** The new transcript should be added to the Transcripts section of the file map.
- Add a row: `| transcripts/[filename] | [one-line description of what was discussed] |`
- If new deliverables were created or referenced, add those too.

**Engagement History.** Only update if the transcript reveals a significant change:
- New engagement phase starting
- Scope expansion or reduction
- Major strategic pivot
- If yes, draft the new phase entry.

**Relationship Context.** Update if the transcript reveals:
- New stakeholders who should be documented
- Updated communication preferences
- New information about decision-making dynamics
- If yes, draft the additions.

**Open Items & Flags.** If the client context file has this section (e.g., Vercel):
- Mark resolved items as resolved
- Add new blockers or open items

**`last_updated` date.** Always update to today's date.

**How to present updates:**

Show the user a clear before/after for each proposed change:

```
**Proposed context updates for [Client] context file:**

1. **Active Workstreams**: [what changed]
   - Current: [existing text]
   - Proposed: [new text]

2. **File Map > Transcripts**: Add new transcript
   - Add: `| transcripts/[filename] | [description] |`

3. **last_updated**: Update to YYYY-MM-DD
```

Wait for user approval before applying changes. Apply all approved changes in a single edit pass.

### Step 6: Offer Follow-up (Optional)

After processing, ask the user:

> "Want me to create a follow-up document from this? (Internal action items, external questions, or both)"

If yes, load the `meeting-follow-up` skill and use the already-extracted data. Do not re-process the transcript. Pass the structured extractions (decisions, action items, open questions, timeline) directly to the follow-up workflow.

## Meeting Type Guidance

Different meeting types emphasize different extractions:

| Meeting Type | Prioritize | De-emphasize |
|-------------|-----------|-------------|
| **Weekly sync** | Action items, workstream status, blockers | Long-term strategy |
| **Strategy call** | Decisions, scope changes, notable quotes | Granular tasks |
| **Kickoff** | Stakeholder signals, scope definition, communication preferences | Historical context |
| **Sales handoff** | Relationship context, expectations, success criteria | Technical details |
| **Deep dive** | Key themes, technical findings, notable quotes | Administrative items |
| **Internal sync** | Action items, ownership, decisions | Client relationship signals |

## Quality Checks

Before finishing, verify:

- [ ] Transcript has `<metadata>` tags with all required fields filled in
- [ ] File name follows `YYYY-MM-DD-client-meeting-type-transcript-v1.md` convention
- [ ] All speaker labels use consistent `**Name (Company):**` format
- [ ] Summary is 2-3 sentences covering what, decided, and next steps
- [ ] Every action item has an owner in `**(Name)**` format
- [ ] Key Decisions section has numbered entries with context, not just bullet points
- [ ] Transcript body has topic section headers for navigation
- [ ] No filler words remain (um, uh, like, you know) unless they carry meaning
- [ ] Notable quotes have speaker attribution and topic context
- [ ] Client context update was proposed (or explicitly noted as not needed)
- [ ] New transcript was added to the client context file map
- [ ] No em dashes anywhere in the output. Use periods, commas, or colons.
- [ ] No invented information. Everything traces back to the transcript.

## Edge Cases

- **Fireflies MCP unavailable:** Ask the user to paste the transcript or provide a file path. Proceed with whatever is available.
- **No client match:** If the meeting is not client-related (internal team meeting, interview, podcast), save to `records/transcripts/` and skip the client context update step.
- **Very short transcript (under 50 lines):** Some transcripts are stubs or link-only (e.g., "Full transcript available in Fireflies: [url]"). If the content is too thin to extract from, note this and ask the user if they want to pull the full transcript from Fireflies.
- **Multiple clients in one meeting:** Pick the primary client (whose account the meeting serves). Note other parties in the participants list.
- **Transcript already exists in the repo:** If a file with the same date and meeting type already exists, ask before overwriting. If the existing file is a stub, replace it. If it has content, ask the user whether to update or create a v2.
- **No clear action items or decisions:** Some meetings are exploratory or informational. Note this explicitly in the Summary: "This was an exploratory discussion. No binding decisions were made." Still extract themes and open questions.
- **Sensitive content:** If the transcript contains compensation, legal, HR, or confidential information, flag it to the user before saving. Ask if any content should be redacted.
- **Non-English transcript:** Process as-is. Do not translate unless the user asks.

## Example Usage

**User request:** "Process the Vercel AI Gateway call from today"

**Steps taken:**
1. Searched Fireflies for today's Vercel meeting using `fireflies_search`
2. Pulled full transcript via `fireflies_get_transcript` and summary via `fireflies_get_summary`
3. Loaded `clients/vercel/vercel-client-context-v1.md` to understand current workstreams
4. Cleaned speaker labels, removed filler, added topic headers
5. Extracted: 4 decisions, 7 action items, 3 key themes, 2 open questions, 1 notable quote
6. Saved processed transcript to `clients/vercel/transcripts/2026-03-03-vercel-ai-gateway-seo-transcript-v1.md`
7. Proposed context updates: updated Active Workstreams with AI Gateway status, added transcript to File Map, updated `last_updated` to 2026-03-03
8. User approved updates. Applied changes to `clients/vercel/vercel-client-context-v1.md`
9. Asked about follow-up document. User said yes, internal only. Loaded `meeting-follow-up` skill.

**User request:** "Clean up this transcript and save it" (with pasted text)

**Steps taken:**
1. Identified client from participant names and meeting context
2. Loaded client context file
3. Cleaned and standardized the pasted transcript
4. Extracted structured data (decisions, action items, themes)
5. Saved to `clients/[client]/transcripts/YYYY-MM-DD-client-meeting-type-transcript-v1.md`
6. Proposed context updates. User approved partial updates (workstreams only).
7. Applied approved changes.

## Deep Reference

- Transcript template: `records/transcripts/meeting-transcript-template-v1.md`
- Client context template: `clients/client-context-template-v1.md`
- Meeting follow-up skill: `.cursor/skills/meeting-follow-up/SKILL.md`
- Client work agent: `agent-docs/client-work-agent.md`
- Fireflies MCP tools: `fireflies_search`, `fireflies_get_transcript`, `fireflies_get_summary`, `fireflies_fetch`
- Example processed transcripts: `clients/vercel/transcripts/`, `clients/brex/transcripts/`, `clients/daylight/transcripts/`
