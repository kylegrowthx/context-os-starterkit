---
name: enrich-fireflies-transcript
description: Enrich a Fireflies transcript that was already converted to markdown by the pull-meeting skill's format-meeting.py script. Reads the full file including transcript, then performs 10-step enrichment — fixing speakers, rewriting summary, generating Context/Relevance/Decisions/Open Questions, cleaning action items and transcript. Triggers on "enrich fireflies transcript", "enrich transcript", "clean up fireflies", "fix fireflies transcript", "production-ready transcript", "finish transcript".
---

# Enrich Fireflies Transcript

Take a script-generated Fireflies transcript `.md` file and make it production-ready. The `format-meeting.py` script does the mechanical data-to-markdown conversion. This skill handles everything after that: fixing speaker labels, writing analysis sections, and cleaning the transcript.

This is a standalone enrichment skill. Run it on any Fireflies transcript `.md` that has `<!-- LLM:` placeholder comments.

## Inputs / Outputs

| | What | Example |
|---|---|---|
| **Input** | A script-generated `.md` file from `format-meeting.py` | `records/transcripts/2026-02/draft-01KJ66C4GC7TV3CBG6SEA0S3MS.md` |
| **Output** | The same `.md` file, enriched in place and renamed | Speaker labels fixed, all analysis sections written, transcript cleaned |

## Prerequisites

The `.md` file should already exist with the standard section structure produced by `format-meeting.py`. If it doesn't exist yet, run the `pull-meeting` skill first.

## Workflow

**Read the entire file before making any changes.** The LLM needs the full transcript to write accurate analysis sections.

### Step 1: Verify Speaker Labels

Fireflies occasionally misidentifies speakers or uses device names, numbers, or partial names.

**How to match speakers to real people:**

1. Read the participant list from metadata.
2. List every unique speaker label in the transcript. Watch for: numbers (`"2"`, `"3"`), device names (`"Conference Room B"`), email-derived names, partial names.
3. Match using transcript evidence:
   - **Direct name address**: Someone says "Well, Natalie, what do you think?" and the next speaker responds — that speaker is Natalie.
   - **Role/context clues**: "On our side at GrowthX..." — cross-reference with known GrowthX employees.
   - **Self-identification**: "This is Tyler from GrowthX" — that speaker is Tyler.
   - **Action item context**: "Marcel, can you send that over?" followed by "Yeah, I'll do that" — that speaker is Marcel.
4. Watch for **shared devices** — one speaker label addressed by different names. Add a `speaker_note` metadata field if ambiguous.

**What to update:**
- Fix all speaker labels throughout the transcript
- Update `participants` metadata: real full names, GrowthX people first, then external
- Add `speaker_note` if any identification was ambiguous

### Step 2: Fix Metadata

Verify and enrich the metadata block:

| Field | Action |
|-------|--------|
| `date` | Verify against transcript content |
| `time` | Always include `UTC` suffix |
| `duration` | Fill in if `unknown` — estimate from transcript length or timestamps |
| `organizer` | Verify |
| `participants` | Full names, GrowthX first, then external. Remove non-person entries. |
| `meeting_link` | Add if available |
| `enriched_on` | Add current UTC timestamp: `YYYY-MM-DD HH:MM UTC` |
| `source` | Should be `fireflies` — don't change |

### Step 3: Rewrite the Summary

The script inserts Fireflies' `Short Summary` as a starting draft. Rewrite it as 2-3 sentences that answer:

1. **What happened?** — Main outcome, not a topic list
2. **What was decided?** — Key decisions or alignments
3. **What's next?** — Most important next steps

Lead with the most important outcome. Use active voice. Include specific details: company names, numbers, deadlines.

**Before** (Fireflies draft):
> "The team discussed a 20-30% decline in organic traffic linked to Google's AI summary rollout and price changes, raising concerns as organic traffic represents 20% of total traffic."

**After** (enriched):
> "GrowthX pitched Flodesk on a comprehensive SEO and AEO strategy to reverse a 20-30% organic traffic decline caused by Google's AI summaries. Flodesk has 1,200 content pages but 90% of traffic is branded — a clear gap GrowthX can fill. Both teams aligned on an 8-week strategy sprint as the next step."

### Step 4: Write the Context Section

1-2 paragraphs answering: Who are these people? What's the relationship? Why did this meeting happen? What happened before this meeting that matters?

This is the section that makes transcripts useful months later. Include:
- Meeting type (client check-in, sales call, internal standup, partnership scoping)
- Relationship stage (new prospect, active client, partner, internal team)
- Relevant backstory (previous meetings, ongoing projects, active deals)
- Key people and their roles

Derive everything from the transcript and metadata — don't invent facts. If you can't determine something, either omit it or state what you can observe.

### Step 5: Write the Relevance Section

Multi-dimensional impact analysis grouped by GrowthX business areas:

- **To GrowthX Services/Delivery** — engagement implications, methodology
- **To CheckThat** — product implications, AI visibility data
- **To GrowthX Business Development** — pipeline, revenue, positioning
- **To [specific area]** — whatever else applies

Only include areas that are actually relevant. 3-5 specific, actionable bullets per area. Each bullet must be concrete with numbers, names, and deadlines.

**Meeting-type-aware signals** — weave into Relevance rather than creating a separate section:

- **Sales/prospect calls**: buying signals, objections raised, competitive mentions, urgency indicators, decision-maker engagement level
- **Client check-ins / listening tours**: satisfaction signals (explicit ratings, complaints, praise), churn risk indicators, expansion opportunities, content quality feedback
- **Internal standups**: blockers, resource conflicts, escalation needs, team morale signals
- **Partnership scoping**: alignment/misalignment, mutual value propositions, next steps clarity

### Step 6: Write Decisions & Commitments

Extract from the transcript:

- **Decisions made** — explicit agreements ("We'll go with the 8-week sprint model")
- **Commitments** — promises by specific people ("Tyler will send the proposal by Friday")
- **Pricing/terms discussed** — any numbers, timelines, or deal structures mentioned

This section is different from Action Items. Action Items are tasks. Decisions & Commitments are agreements and promises that shape what happens next.

If no explicit decisions were made, write "No formal decisions made — exploratory discussion."

### Step 7: Write Open Questions

Items raised but not resolved. Things that need follow-up or answers. This prevents important loose threads from getting lost. Examples:

- "Flodesk team needs to discuss internally whether they can support fast publishing cycles"
- "Unclear who on Flodesk side owns the programmatic SEO folder — needs clarification"

If no open questions, write "None identified."

### Step 8: Review Overview & Key Topics

Check the Fireflies-generated Overview and Key Topics (Notes) sections for:
- Accuracy against the actual transcript
- Completeness — add missing topics
- Errors — fix factual mistakes
- Formatting — clean up emoji cruft, fix markdown headers

Don't rewrite from scratch unless they're badly wrong. Light edits and additions are preferred.

### Step 9: Fix Action Items

1. Add company affiliations: `**Tyler Pavlas (GrowthX)**`
2. Replace wrong speaker names with corrected names from Step 1
3. Add missing action items that were committed to in the transcript but not captured
4. Merge duplicates
5. Remove timestamp references like `(26:14)` — they don't add value in the final file

### Step 10: Clean the Transcript

**Speaker label replacement:** Replace all incorrect labels with real full names throughout.

**Remove noise:**
- Standalone `"."` or `"..."` lines (transcription artifacts)
- Duplicate back-to-back identical lines
- Garbled-beyond-comprehension lines

**Light cleanup:**
- Fix obvious transcription errors where meaning is clear: `"ChatGBT"` → `"ChatGPT"`, `"Growth X"` → `"GrowthX"`
- Merge fragmented sentences that are clearly one continuous thought from the same speaker
- Remove pure filler lines (single-word acknowledgments between longer statements) only when they add no conversational context

**Do NOT:**
- Rewrite what people said
- Remove conversational interjections that show dynamics ("Oh, she's on!" shows someone joined late)
- Add words people didn't say
- Change the order of lines

### Step 11: Rename the File

Rename from `draft-{id}.md` to a descriptive filename:

**Format:** `YYYY-MM-DD-descriptive-meeting-name.md`
- Use meeting date from metadata
- Convert title to lowercase with hyphens
- Remove special characters, angle brackets, pipes
- Examples: `2026-02-26-flodesk-growthx-intro.md`, `2026-02-26-strategy-sprint-standup.md`

### Final Checklist

Before saving, verify:

- [ ] All speaker labels are real full names (no device names, no numbers)
- [ ] Participant list is clean (real people only, GrowthX first)
- [ ] Summary is 2-3 sentences with specific outcomes — no placeholder comments
- [ ] Context is 1-2 paragraphs with who/what/why
- [ ] Relevance has grouped bullets with concrete details
- [ ] Decisions & Commitments section is populated (or "No formal decisions made")
- [ ] Open Questions section is populated (or "None identified")
- [ ] Action items have company affiliations
- [ ] No `<!-- LLM:` placeholder comments remain
- [ ] Transcript is clean: no device names, no noise, no garbled fragments
- [ ] `enriched_on` timestamp added to metadata
- [ ] `source: fireflies` tag present
- [ ] File renamed from `draft-{id}.md` to descriptive name

## Batch Mode

For enriching multiple Fireflies transcripts at once:

1. User specifies files or a date range
2. Find all `.md` files in `records/transcripts/` that have `<!-- LLM:` placeholder comments and `source: fireflies` in metadata
3. Process 3-4 at a time using Task agents
4. Each agent reads the full file and applies the complete 11-step workflow
5. Report results in a summary table

| # | Date | File | Duration | Status |
|---|------|------|----------|--------|
| 1 | Feb 26 | `flodesk-growthx-intro.md` | 60m | enriched |
| 2 | Feb 26 | `strategy-sprint-standup.md` | 63m | enriched |

## Writing Guidelines

- **Direct and clear** — no corporate jargon
- **Lead with the point** — most important info first
- **Active voice** — "Marcel outlined" not "It was outlined by Marcel"
- **Ground in specifics** — numbers, names, dates, concrete details
- **Connect to company context** — reference GrowthX services, CheckThat, content strategy as relevant

## Edge Cases

- **All speakers already correct**: If Fireflies got all speakers right, skip Step 1 but still verify.
- **No transcript data**: If the transcript section says "No transcript captured", you can still enrich metadata, summary, context, and relevance from the Overview and Key Topics sections.
- **Very short meetings** (< 10 minutes): Keep analysis proportional. Summary can be 1 sentence. Context and Relevance can be brief.
- **Internal-only meetings**: Skip contact-related signals in Relevance. Focus on operational implications.
