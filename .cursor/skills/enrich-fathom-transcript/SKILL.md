---
name: enrich-fathom-transcript
description: Enrich a Fathom transcript that was already converted to markdown by the convert-fathom-transcript skill. Fixes speaker labels, rewrites the summary, generates Context and Relevance sections, cleans the raw transcript, and fixes action items. Use whenever the user wants to clean up, enrich, fix, or improve a Fathom transcript .md file — including fixing speaker names, removing noise, writing analysis sections, or making a transcript production-ready. Triggers on "enrich transcript", "clean up transcript", "fix transcript", "fix speakers", "enrich fathom", "clean fathom", "production-ready transcript", "finish transcript".
---

# Enrich Fathom Transcript

Take a script-generated Fathom transcript `.md` file and make it production-ready. The `convert-to-transcript.py` script does the mechanical JSON-to-markdown conversion. This skill handles everything after that: fixing speaker labels, identifying people, writing analysis sections, and cleaning the raw transcript.

This is a standalone enrichment skill. Run the `convert-fathom-transcript` skill first if the `.md` file doesn't exist yet.

## Inputs / Outputs

| | What | Example |
|---|---|---|
| **Input** | A converted `.md` file plus its source JSON files | `projects/fathom-backup/2026-02/2026-02-02-fieldwire-growthx-kick-off/` |
| **Output** | The same `.md` file, enriched in place | Speaker labels fixed, Summary/Context/Relevance written, transcript cleaned |

## Source Files

Each meeting folder in `projects/fathom-backup/YYYY-MM/YYYY-MM-DD-meeting-slug/` contains:

| File | What's inside | Required? |
|------|--------------|-----------|
| `*.md` | The script-generated transcript to enrich | Yes |
| `participants.json` | Calendar invitees with emails, domains, `is_external` flags | Yes |
| `metadata.json` | Meeting title, timestamps, recorded_by | Yes |
| `transcript.json` | Raw transcript with speaker display names and timestamps | Yes |
| `action-items.json` | Action items with assignee names and emails | Optional (older meetings lack this) |

**Read all source files before making any changes.** The JSON files contain ground truth that the `.md` file may have gotten wrong.

## Workflow

### Step 1: Identify All Speakers

This is the most important step. Fathom often labels speakers with device names, numbers, or display names that don't match real names.

**How to match speakers to real people:**

1. Read `participants.json`. Each entry has `name`, `email`, `email_domain`, `is_external` (true = client, false = GrowthX), and `matched_speaker_display_name` (if Fathom matched them).

2. List every unique speaker label in the transcript. Watch for problematic labels: numbers (`"2"`, `"3"`), device names (`"06 - Oatmeal"`, `"Conference Room B"`), email-derived names (`"john.doe"`).

3. Match using transcript evidence:
   - **Direct name address**: Someone says "Well, Gavin, do you want to start?" and the next speaker responds — that speaker is Gavin.
   - **Role/context clues**: "On our side at GrowthX..." — cross-reference with `is_external` flags.
   - **Action item context**: "Dave, we talked about you doing X" followed by "Yeah, I'll do that" — that speaker is Dave.
   - **Third-person references**: "I'm glad Gavin had this insight" — find who presented that insight.

4. Watch for **shared devices** — one speaker label addressed by different names at different points. If you can't distinguish who's speaking, add a `speaker_note` metadata field explaining the situation.

**What to write:**
- Update `participants` metadata: real names only, GrowthX people first, then external. Remove non-person entries like "Team GrowthX".
- Add `speaker_note` if any identification was ambiguous.

### Step 2: Fix the Metadata Block

Check every field against source JSON:

| Field | Source | Watch for |
|-------|--------|-----------|
| `date` | `metadata.json` → `recording_start_time` | May differ from scheduled date if meeting ran past midnight UTC |
| `time` | `metadata.json` → `recording_start_time` | Always append `UTC` |
| `duration` | `recording_end_time` minus `recording_start_time` in minutes, rounded up | Script usually correct |
| `organizer` | `metadata.json` → `recorded_by.email` | May differ from actual organizer |
| `participants` | Your corrected list from Step 1 | Real names, comma-separated |
| `fathom_recording_id` | `metadata.json` → `recording_id` | Should be correct |
| `fathom_url` / `share_url` | `metadata.json` | Should be correct |
| `source` | Always `fathom` | Don't change |
| `enriched_on` | Current UTC timestamp when enrichment completes | Format: `YYYY-MM-DD HH:MM UTC`. Add this field — it won't exist in script-generated files. |

### Step 3: Rewrite the Summary

The script extracts Fathom's "Meeting Purpose" which is usually a single vague sentence. Rewrite it as 2-3 sentences that answer:

1. **What happened?** — Main topic and what was discussed
2. **What was decided?** — Key decisions or alignments
3. **What's next?** — Most important next steps

Lead with the most important outcome. Include specific details: company names, tool names, numbers, deadlines. Use active voice.

**Example — before:**
> Align on the new content strategy and define next steps.

**Example — after:**
> GrowthX and Relay aligned on a major content strategy pivot — shifting from broad top-of-funnel content to deep-dive verticals, starting with General Contracting and HVAC. Bailey followed up on action items from Marcel's call with the Relay team the day before, including getting GA4 access for a GrowthX SEO expert and auditing CheckThat prompts for home services. Bethany flagged that approvals are still hard to attribute to specific pages, so the team agreed to focus on early-signal metrics before expecting conversion data.

### Step 4: Write the Context Section

1-2 paragraphs answering: Who is the client? What's the relationship? Why did this meeting happen? What's the backstory?

Derive everything from the transcript and metadata — don't invent facts. If you can't determine something (like what the client does), either omit it or state what you can observe ("Relay appears to operate in financial services based on the discussion of approvals pipelines").

### Step 5: Write the Relevance Section

Bullet points grouped by area. Standard areas:

- **To GrowthX Delivery:** — Impact on how GrowthX delivers services. New methodologies, tools, processes, client requirements.
- **To CheckThat:** — AI visibility, AEO, CheckThat mentions, prompt auditing.
- **To GrowthX Business Development:** — Account health signals, expansion, renewal risk, reference potential.

Only include areas that are actually relevant. 3-5 specific, actionable bullets per area. Include names, numbers, tools, deadlines.

### Step 6: Review the Overview

Check Fathom's "Key Takeaways" bullets for accuracy, completeness, and formatting. Add missing topics. Remove misleading bullets. Make sure it doesn't duplicate the Summary.

### Step 7: Review the Key Topics

Spot-check Fathom's "Topics" H3 subsections against the transcript. Fix errors, add missing topics. Don't rewrite from scratch unless badly wrong.

### Step 8: Fix the Action Items

1. Replace device/display names with real names from Step 1
2. Add company affiliation: `**Bailey Seybolt (GrowthX)**`
3. Split shared-device items using `recording_timestamp` from `action-items.json` to determine who actually committed
4. Add missing items that were committed to in the transcript but not captured
5. Merge duplicates

### Step 9: Clean Up the Transcript

**Speaker label replacement:** Replace all display-name artifacts with real names (`**06 - Oatmeal:**` → `**Gavin Graham:**`).

**Remove noise:**
- Standalone `"."` or `"..."` lines (transcription artifacts)
- Duplicate back-to-back identical lines
- Garbled-beyond-comprehension lines

**Light cleanup:**
- Fix obvious transcription errors where meaning is clear: `"ChatGBT"` → `"ChatGPT"`
- Merge fragmented sentences that are clearly one continuous thought
- Remove pure filler lines (single-word acknowledgments between longer statements)

**Do NOT:**
- Rewrite what people said
- Remove conversational interjections that show dynamics ("Oh, she's on!" shows someone joined late)
- Add words people didn't say
- Change the order of lines

### Step 10: Final Review

Verify before saving:

- [ ] All speaker labels are real names (no device names, no numbers)
- [ ] Participant list has only real people
- [ ] Summary is 2-3 sentences with specific details
- [ ] Context is 1-2 paragraphs with who/what/why
- [ ] Relevance has grouped bullets with specific, actionable insights
- [ ] Action items use real names with company affiliations
- [ ] No `_To be generated by LLM._` placeholders remain
- [ ] Transcript is clean: no device names, no noise, no garbled fragments
- [ ] `speaker_note` added if any speaker identification was ambiguous
- [ ] All metadata fields are correct
- [ ] `enriched_on` timestamp added with current UTC date and time

## Batch Mode

For enriching multiple meetings at once:

1. User specifies a month or date range
2. Find all `.md` files in the relevant `projects/fathom-backup/YYYY-MM/` folders that still have `_To be generated by LLM._` placeholders
3. Process 3-4 at a time using Task agents if available
4. Each agent reads the `.md` file and its sibling JSON files, applies the full 10-step process
5. Report results in a summary table

| # | Date | File | Duration | Status |
|---|------|------|----------|--------|
| 1 | Feb 2 | `fieldwire-growthx-kick-off.md` | 45m | enriched |
| 2 | Feb 2 | `navan-growthx-weekly-sync.md` | 30m | enriched |

## Writing Guidelines

- **Direct and clear** — no corporate jargon
- **Lead with the point** — most important info first
- **Active voice** — "Marcel outlined" not "It was outlined by Marcel"
- **Ground in specifics** — numbers, names, dates, concrete details
- **Connect to company context** — reference GrowthX services, CheckThat, content strategy as relevant

## Edge Cases

- **No `action-items.json`**: Older meetings lack this file. Use "Next Steps" from the summary, or leave as-is if there are none.
- **No transcript data**: If both `transcript.json` and `transcript-raw.json` are empty, you can still enrich the metadata, summary, context, and relevance from `summary.json`.
- **All speakers already identified**: If the script correctly matched all speakers, skip Step 1 but still verify.
- **Solo recordings**: Some meetings have only 1 speaker (e.g., Marcel recording a voice memo). Skip speaker matching; adjust Context to reflect it's a solo recording.
