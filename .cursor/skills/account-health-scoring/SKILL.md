---
name: account-health-scoring
description: |
  **Account Health Scoring**: Generate focused numerical health scores (1-5) for GrowthX client accounts across 5 dimensions (Relationship, Quantity, Content Quality, Performance/ROI, Strategy). Compare agent-generated scores against EM self-reported scores to identify misalignment. Optionally evaluate EM effectiveness from call transcripts and Slack activity (include only if user requests).
  - MANDATORY TRIGGERS: score {client}, health scores on {client}, how healthy is {client}, weekly health check on {client}, compare my scores for {client}, account health score
---

# Account Health Scoring

Score a GrowthX client account 1-5 on 5 dimensions using Andi's rubric, compare against EM self-reported scores, flag misalignment. Compact scorecard (~1,000-1,500 words), not a narrative report.

## Architecture: Sequential Data Gathering

Data gathering is **heavy** — Fireflies transcripts, Slack history, and Notion pages can each be large. Gather each source sequentially, extracting only the relevant signals before moving on. Never dump raw transcripts or message histories into the output — distill findings into structured evidence summaries.

```
Workflow:
  1. Clarify scope
  2. Determine engagement stage (Notion)
  3. Gather Fireflies evidence → extract structured summary
  4. Gather Slack evidence → extract structured summary
  5. Gather Notion evidence → extract structured summary
  6. Assemble evidence buckets per dimension
  7. Score each dimension against rubric
  8. Compare, analyze, save
```

## Workflow

### Step 1 — Clarify Scope

1. Ask which client to score
2. Resolve client slug for Slack channels (`#d-int-{clientslug}`, `#d-ext-{clientslug}`)
3. Optionally ask if there's a specific concern (does NOT override independence rule — all 5 dimensions still scored independently)

### Step 2 — Determine Engagement Stage

Query Sprint Tracker (Notion DB `2102ba60-bc74-8058-b988-000b509f811f`) for the client.

| Stage | Criteria | Performance/ROI Scoring |
|-------|----------|------------------------|
| SPRINT | Pre-Transition Date | Foundation-building |
| NEW | 0-3 months since Transition Date | Foundation-building |
| ESTABLISHED | 3+ months since Transition Date | Outcomes-based |

### Step 3 — Gather Evidence (3 Sources, Sequential)

For each source, read the data-sources reference file first for extraction targets.

**Reference file:** `references/data-sources.md`

#### Source A — Fireflies

1. Use Fireflies MCP tools to find all calls for this client from the last 60-90 days
2. For each call, fetch the transcript and/or summary
3. Tag each call with its date

Extract a structured summary organized by dimension:

- **Calls Found:** List each with title and date
- **Evidence by Dimension:** Relationship, Quantity, Content Quality, Performance/ROI, Strategy — with specific signals and dates
- **EM Assessment (Optional):** Questions asked, dimensions covered/missing, communication style
- **Red Flags / Green Flags observed**

#### Source B — Slack

Search these channels:
1. `#d-int-{clientslug}` — last 60-90 days (internal)
2. `#d-ext-{clientslug}` — last 60-90 days (external/client-facing)
3. `#d-at-risk-alerts` — all time, filter for client name

Extract structured summary:
- **Channels Searched:** message count / date range per channel
- **Evidence by Dimension:** with dates
- **Key Signals:** silence periods, escalation threads, at-risk alerts, leadership messages
- **EM Slack Behavior (Optional):** response frequency, follow-up patterns, proactive vs reactive
- **Red Flags / Green Flags observed**

**IMPORTANT:** Never quote DMs. Paraphrase only.

#### Source C — Notion

Gather from 3 Notion sources:

1. **ClientDB** — EM-reported health scores (all 5 dimensions), Health Flag, MRR, Renewal Date, Pod, EM, ME, historical scores
2. **Sprint Tracker** (DB ID: `2102ba60-bc74-8058-b988-000b509f811f`) — Sprint Kickoff Date, Sprint Length, Transition Date, Sprint Status
3. **Sync Notes** — last 60-90 days, key discussion points, client feedback, action items

Extract structured summary:
- **Account Metadata:** Client, Pod, EM, ME, MRR, Renewal, Health Flag
- **EM-Reported Scores** (latest table)
- **Historical Scores** if available
- **Engagement Stage Data** with calculated stage
- **Evidence by Dimension** from sync notes

### Step 4 — Assemble Evidence Buckets

Combine all structured summaries into **per-dimension buckets**:

1. **Relationship** — Relationship sections from all 3 sources
2. **Quantity** — Quantity sections from all 3 sources
3. **Content Quality** — Content Quality sections from all 3 sources
4. **Performance/ROI** — Performance sections + engagement stage
5. **Strategy** — Strategy sections from all 3 sources
6. **EM Assessment** (optional) — only if user requested

Also collect: red flags, green flags, data gaps, evidence source metadata.

### Step 5 — Score Each Dimension

Read `references/scoring-rubric.md` for full criteria, flags, and independence rules.

Score in order: Relationship → Quantity → Content Quality → Performance/ROI → Strategy.

For each dimension:
1. **Isolate** — use ONLY this dimension's evidence bucket
2. **Apply rubric** — map evidence to 1-5 criteria
3. **Check flags** — identify red/green flags present
4. **Recency weight** — apply exponential decay: weight = 2^(-days_ago / 14). 14-day half-life.
5. **Score** — assign 1-5 with 1-2 sentence justification citing specific evidence
6. **Self-check** — "If I cover up all other scores, does THIS score still make sense based ONLY on THIS dimension's criteria?"
7. **Confidence** — High (multiple recent sources) / Medium (1-2 sources or older data) / Low (minimal evidence)

Performance/ROI: use engagement stage (NEW = foundation criteria, ESTABLISHED = outcomes criteria).

**After all 5 scored:** Check for halo/horn contamination — all scores identical or all moving same direction without dimension-specific justification → re-score affected dimensions.

### Step 6 — Compare, Analyze, Save

Read `assets/output-template.md` for the exact output format.

1. **Retrieve prior agent scores:** Search `Reports/` for the most recent prior health score file for this client (pattern: `{Client_Name}_Health_Score_*.md`). Extract the previous agent scores per dimension.
2. Build scorecard: Agent Score | EM Score | Gap for each dimension
3. Flag misalignment where |Agent - EM| >= 2
4. *(Optional)* Write EM Effectiveness Assessment if user requested
5. List action triggers per rubric (score <= 2 → director ticket; drop >= 1 → flag; red flag → document). No added recommendations — just which thresholds fired.
6. Document data gaps
7. Save to `Reports/{Client_Name}_Health_Score_{YYYY-MM-DD}.md`

Read `references/rules.md` for scope boundaries, DM rules, and the verification checklist.

## Key Rules

- **Independence is mandatory.** Each dimension scored in isolation.
- **Rubric is source of truth.** Apply Andi's criteria exactly.
- **Always score.** Never refuse due to missing data. Score with confidence qualifier (H/M/L) and document gaps.
- **No DM quotes.** Paraphrase only.
- **No compensation info.** Never include salary, bonus, or raise details.
- **Compact output.** ~1,000-1,500 words. Scorecard with numbers, not prose narrative.
- **No recommendations.** Action triggers flag which thresholds fired — Andi decides what to do.
- **Quantity scores low even if client is the blocker.** Explicitly stated in rubric.
