# Fathom Transcript Enrichment Instructions

Step-by-step instructions for an AI agent to take a script-generated Fathom transcript `.md` file and make it production-ready. The script (`convert-to-transcript.py`) does the mechanical conversion from JSON to markdown. Your job is the enrichment: fixing errors, identifying people, writing analysis sections, and cleaning up the transcript.

---

## Before You Start

You need access to these files for each meeting you're enriching:

1. **The generated `.md` file** — the script output you're improving
2. **`participants.json`** — calendar invitees with emails, domains, and `is_external` flags
3. **`metadata.json`** — meeting title, timestamps, recorded_by info
4. **`transcript.json`** — raw transcript with speaker display names and timestamps
5. **`action-items.json`** — action items with assignee names and emails (may not exist for older meetings)

All of these live in the same meeting folder. Read them all before making any changes.

---

## Step 1: Identify All Speakers

This is the most important step. Fathom often labels speakers with device names, numbers, or display names that don't match real names.

### How to do it

1. **Read `participants.json`**. Each entry has:
   - `name` — sometimes a real name, sometimes an email address
   - `email` — always present
   - `email_domain` — tells you which company they're from
   - `is_external` — `true` = client/external, `false` = GrowthX team
   - `matched_speaker_display_name` — if Fathom matched this invitee to a transcript speaker, this shows the speaker label

2. **Read the transcript** and list every unique speaker label. Common problematic labels:
   - **Numbers** like `"2"`, `"3"` — Fathom couldn't identify the speaker
   - **Device names** like `"06 - Oatmeal"`, `"Conference Room B"` — the speaker's device/room name
   - **Email-based names** like `"john.doe"` — Fathom extracted from email

3. **Match speakers to participants** using these techniques:
   - **Direct name address**: Search the transcript for lines where someone says a first name. Example: `"Well, Gavin, do you want to start?"` followed by a response from `"06 - Oatmeal"` tells you `06 - Oatmeal` = Gavin.
   - **Role/context clues**: If someone says `"On our side at GrowthX..."` they're GrowthX. Cross-reference with `is_external` flags.
   - **Action item context**: If Bailey says `"Dave, we talked about you doing X"` and the next speaker responds `"Yeah, I'll do that"`, that speaker is Dave.
   - **Third-person references**: If Bethany says `"I'm glad Gavin had this insight"` and only one unidentified speaker presented that insight, that's Gavin.

4. **Watch for shared devices**: Sometimes two people share one microphone (same room/device). Clues:
   - One speaker label is addressed by multiple different names at different points
   - The speaking style or topic suddenly shifts
   - If you can't distinguish who's speaking, note it in the metadata `speaker_note` field

### What to write

- In the `participants` metadata field, list real names only. Order: GrowthX people first, then external. Remove non-person entries like `"Team GrowthX"`.
- If a speaker was on a shared device, add a `speaker_note` metadata field explaining the situation. Example:
  ```
  speaker_note: "06 - Oatmeal" in the original Fathom transcript is Gavin Graham (confirmed at 00:12:03 when Bethany addresses him by name). Dave White was likely on the same device.
  ```

---

## Step 2: Fix the Metadata Block

Check every field against the source JSON:

| Field | Where to get it | Common issues |
|-------|----------------|---------------|
| `date` | `metadata.json` > `recording_start_time` (date portion) | Sometimes the scheduled date differs from recording date if meeting ran late past midnight UTC |
| `time` | `metadata.json` > `recording_start_time` (time portion) | Always append `UTC` |
| `duration` | Calculate: `recording_end_time` minus `recording_start_time` in minutes, rounded up | Script usually gets this right |
| `organizer` | `metadata.json` > `recorded_by.email` | May be different from who actually organized the meeting |
| `participants` | Your corrected list from Step 1 | Must be real names, comma-separated |
| `fathom_recording_id` | `metadata.json` > `recording_id` | Should be correct from script |
| `fathom_url` | `metadata.json` > `url` | Should be correct from script |
| `share_url` | `metadata.json` > `share_url` | Should be correct from script |
| `source` | Always `fathom` | Don't change |

---

## Step 3: Rewrite the Summary

The script extracts Fathom's "Meeting Purpose" which is often a single vague sentence like "Align on the new content strategy and define next steps."

### What a good summary looks like

2-3 sentences that answer:
1. **What happened?** — The main topic and what was discussed
2. **What was decided?** — Key decisions or alignments reached
3. **What's next?** — The most important next steps

### Rules

- Lead with the most important outcome, not the meeting purpose
- Include specific details: company names, tool names, numbers, deadlines
- Use active voice: "Bailey followed up on..." not "Follow-ups were discussed..."
- Don't repeat the meeting title

### Example

**Bad** (script output):
> Align on the new content strategy and define next steps.

**Good** (enriched):
> GrowthX and Relay aligned on a major content strategy pivot — shifting from broad top-of-funnel content to deep-dive verticals, starting with General Contracting and HVAC. Bailey followed up on action items from Marcel's call with the Relay team the day before, including getting GA4 access for a GrowthX SEO expert, auditing CheckThat prompts for home services, and building a new Looker view for week-over-week page performance. Bethany flagged that approvals are still hard to attribute to specific pages, so the team agreed to focus on early-signal metrics before expecting conversion data.

---

## Step 4: Write the Context Section

1-2 paragraphs explaining the background. Answer these questions:

1. **Who is the client?** — Company name, domain, what they do (if you can tell from the transcript)
2. **What's the relationship?** — GrowthX client, prospect, partner? How long? Who manages it?
3. **Why did this meeting happen?** — Regular sync? Follow-up to another meeting? Triggered by a specific event?
4. **What's the backstory?** — Any recent changes, pivots, or events that led to this discussion?

### Where to find this information

- The transcript itself (people reference past events, other meetings, etc.)
- The meeting title and participant list
- `is_external` flags in `participants.json` tell you who's client vs. GrowthX

### Rules

- Don't invent facts. Only state what you can derive from the transcript and metadata.
- If you don't know something (like what the client's product does), either omit it or say what you can observe (e.g., "Relay appears to operate in financial services based on the discussion of approvals pipelines").
- Reference specific people and their roles as observed in the call.

---

## Step 5: Write the Relevance Section

Bullet points grouped by area of relevance to GrowthX. Always consider these areas:

### Standard relevance areas

- **To GrowthX Delivery:** — How does this affect how GrowthX delivers content/SEO services? New methodologies, tools, processes, client-specific requirements.
- **To CheckThat:** — Any mention of AI visibility, AEO, CheckThat specifically, replacing Scrunch, prompt auditing, etc.
- **To GrowthX Business Development:** — Signals about account health, expansion, renewal risk, reference potential, cross-account patterns.

### Rules

- Only include areas that are actually relevant. Don't force a section if there's nothing meaningful.
- Each bullet should be specific and actionable, not vague.
- Include names, numbers, tools, and deadlines when available.
- 3-5 bullets per area is typical. Don't pad with filler.

---

## Step 6: Review the Overview

The script extracts Fathom's "Key Takeaways" section. Review it for:

1. **Accuracy**: Does each bullet accurately reflect what was discussed? Remove anything that's misleading.
2. **Completeness**: Are there major topics discussed in the call that aren't captured? Add them.
3. **Formatting**: Bullets should start with `- `. Use `**bold**` for key terms or labels.
4. **No redundancy with Summary**: The overview should have different content than the summary. Overview = bullet-level details. Summary = narrative.

---

## Step 7: Review the Key Topics

The script extracts Fathom's "Topics" section with H3 subsections. Review for:

1. **Accuracy**: Spot-check claims against the transcript. Fix anything wrong.
2. **Missing topics**: If a significant discussion isn't covered, add a subsection.
3. **Formatting**: H3 headers (`### Topic Name`) with bullet lists underneath. Use `**bold**` labels for sub-points.
4. **Don't rewrite from scratch** unless the section is badly wrong. The Fathom summary is usually decent for topics.

---

## Step 8: Fix the Action Items

The script groups action items by assignee name from `action-items.json`. Fix these issues:

1. **Replace device/display names** with real names (from Step 1). Example: `**06 - Oatmeal**` → `**Gavin Graham (Relay)**`
2. **Add company affiliation** in parentheses after each name: `**Bailey Seybolt (GrowthX)**`, `**Bethany Cantor (Relay)**`
3. **Split shared-device items**: If "06 - Oatmeal" was two people, read the transcript context around each action item's timestamp to determine who it actually belongs to. The `recording_timestamp` field in `action-items.json` tells you where in the call this was discussed.
4. **Add missing items**: If someone committed to something in the transcript that Fathom didn't capture, add it.
5. **Merge duplicates**: Fathom sometimes captures the same action item twice with slightly different wording.

---

## Step 9: Clean Up the Transcript

Go through the full transcript and make these fixes:

### Speaker label replacement

Replace all instances of display-name artifacts with real names:
- `**06 - Oatmeal:**` → `**Gavin Graham:**`
- `**2:**` → `**Dave White:**` (or whoever you identified)

### Remove noise

Remove lines that are pure transcription noise with no information value:
- Standalone `"."` or `"..."` lines (transcription artifacts)
- Duplicate back-to-back lines where the speaker said the same thing
- Lines that are clearly garbled beyond comprehension (like `"not is really you're part content you."`)

### Light cleanup (do this)

- Fix obvious transcription errors where the meaning is clear from context: `"ChatGBT"` → `"ChatGPT"`, `"know"` → `"I know"` where dropped words are obvious
- Merge fragmented sentences where a speaker's thought was split across multiple short lines and the meaning is clearer as one line. Only do this when the fragments are clearly one continuous thought.
- Remove pure filler lines that add zero content: single-word acknowledgments between longer statements

### Do NOT do this

- Do not rewrite what people said. Keep their actual words.
- Do not remove conversational interjections that show dynamics (like "Oh, she's on!" — that shows Bethany joined late, which is useful context).
- Do not add words people didn't say. If a sentence is garbled, either leave it or remove it. Don't invent what they meant.
- Do not change the order of lines.

---

## Step 10: Final Review Checklist

Before saving, verify:

- [ ] All speaker labels are real names (no device names, no numbers)
- [ ] Participant list has only real people (no shared calendar entries like "Team GrowthX")
- [ ] Summary is 2-3 sentences with specific details
- [ ] Context is 1-2 paragraphs with who/what/why
- [ ] Relevance has grouped bullet points with specific, actionable insights
- [ ] Action items use real names with company affiliations
- [ ] No `_To be generated by LLM._` placeholders remain
- [ ] Transcript is clean: no device names, no noise lines, no garbled fragments left
- [ ] `speaker_note` metadata field added if any speaker identification was ambiguous
- [ ] All metadata fields are correct (date, time, duration, organizer, participants)

---

## Reference: Complete File Structure

The final file should follow this exact structure:

```markdown
# Meeting Title

<metadata>
date: YYYY-MM-DD
time: HH:MM UTC
duration: X minutes
organizer: email@example.com
participants: Name1, Name2, Name3
fathom_recording_id: 12345678
fathom_url: https://fathom.video/calls/...
share_url: https://fathom.video/share/...
source: fathom
speaker_note: (only if speaker identification was ambiguous)
</metadata>

---

## Summary

<2-3 sentences. Lead with outcome, include specifics, active voice.>

---

## Context

<1-2 paragraphs. Who is the client, what's the relationship, why this meeting, what's the backstory.>

---

## Relevance

**To GrowthX Delivery:**
- Specific insight with names/numbers
- Another insight

**To CheckThat:**
- Specific insight

**To GrowthX Business Development:**
- Specific insight

---

## Overview

- Bullet point with specific detail
- Another bullet

---

## Key Topics

### Topic Name

- Detail
- Another detail

### Another Topic

- Detail

---

## Action Items

**Person Name (Company)**
- Action item with deadline if available
- Another action

**Another Person (Company)**
- Their action items

---

## Transcript
**Speaker Name:** Dialogue text.

**Another Speaker:** Response text.
```

---

## Example: Before and After

See the Relay bi-weekly sync for a complete worked example:

- **Before** (script output): `2026-02-26-relay-growthx-bi-weekly-sync.md` as generated by `convert-to-transcript.py`
- **After** (enriched): the same file after applying these instructions

Key changes made in that example:
1. `"06 - Oatmeal"` identified as Gavin Graham via transcript evidence (Bethany calls him by name)
2. `"Team GrowthX"` removed from participants (shared calendar entry, not a person)
3. Summary expanded from 1 vague sentence to 3 specific sentences
4. Context section written from scratch using transcript evidence
5. Relevance section written with 3 areas (Delivery, CheckThat, Business Development)
6. Action items split between Gavin and Dave based on transcript context at each timestamp
7. Transcript cleaned: speaker labels fixed, noise lines removed, garbled fragments cleaned up
