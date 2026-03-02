# Data Sources

Three primary sources: Fireflies (call transcripts), Slack (channel communications), Notion (account metadata and EM scores).

---

## Source A: Fireflies — Call Transcripts

### MCP Tools
- `fireflies_get_transcripts` — List recent transcripts, filter by client name
- `fireflies_get_transcript` — Fetch full transcript by ID
- `fireflies_get_summary` — Get AI-generated call summary by ID
- `fireflies_search` — Search across transcripts by topic/keyword

### Gather
All client calls from the last 60-90 days. Tag each with date for exponential decay weighting.

### Extract Per Dimension

| Dimension | What to Extract |
|-----------|--------------------|
| Relationship | Conversation tone, decision-maker presence/absence, rapport, trust indicators |
| Quantity | Delivery timeline discussion, missed deadlines, publishing blockers, "where is X?" |
| Content Quality | Piece-level feedback, revision cycles, calibration progress, praise or complaints |
| Performance/ROI | Results discussed, KPI mentions, ROI expectations, impatience, board pressure |
| Strategy | Plan clarity, alignment confirmation, pivots, "what's next" conversations |

### EM Assessment (Optional — from calls, include only if user requests EM evaluation)
- What questions does the EM ask? Do they cover all 5 dimensions?
- Probing for strategic context vs. running through status updates?
- Does the EM address or deflect client concerns?
- Which dimensions does the EM never raise?

### Recency Weighting — Exponential Decay

Apply continuous exponential decay with a **14-day half-life**:

**Formula:** `weight = 2^(-days_ago / 14)`

| Days Ago | Weight | Meaning |
|----------|--------|---------|
| 0 (today) | 1.00 | Full weight |
| 7 days | 0.71 | ~70% weight |
| 14 days | 0.50 | Half weight |
| 28 days | 0.25 | Quarter weight |
| 42 days | 0.13 | ~13% weight |
| 60 days | 0.05 | Near-zero, context only |

No hard cutoffs — a call from 3 days ago naturally outweighs one from 10 days ago. The math handles the gradient.

---

## Source B: Slack — Channel Communications

### Channels

| Channel | Pattern | Time Window |
|---------|---------|-------------|
| Internal | `#d-int-{clientslug}` | Last 60-90 days |
| External | `#d-ext-{clientslug}` | Last 60-90 days |
| At-Risk | `#d-at-risk-alerts` | All time |

### Extract Per Dimension

| Dimension | What to Extract |
|-----------|--------------------|
| Relationship | Client tone (friendly vs. terse), silence gaps, escalation signals, communication frequency |
| Quantity | Publishing blockers, delivery delays, CMS issues, editorial calendar status |
| Content Quality | Content feedback, revision discussions, calibration mentions, praise/complaints |
| Performance/ROI | Performance data shared, results questions, ROI discussions, goalpost-moving |
| Strategy | Strategy discussions, pivot mentions, alignment conversations |

### EM Slack Behavior
Extract from both internal and external channels:
- **Response frequency** — How often does the EM post/reply? Any multi-day gaps?
- **Follow-up patterns** — Does the EM follow up on open items, or do threads go cold?
- **Proactive vs. reactive** — Does the EM initiate updates and share context, or only respond when pinged?
- **Engagement gaps** — Periods where EM is absent from client channels despite active client messages

### Key Signals to Flag
- Client silence (no messages in 2+ weeks in external channel) → Relationship
- Internal escalation threads → cross-dimension
- At-risk alert posts → note date, who flagged, reason, resolution
- Leadership messages (Andi, Marcel, Bridget) → escalation context

---

## Source C: Notion — Account Data & EM Scores

### MCP Tools
- `notion-search` — Search for pages by client name
- `notion-fetch` — Fetch specific Notion page content
- `notion-query-data-sources` — Query Notion databases

### 1. ClientDB — EM Scores & Metadata
Search for client name in ClientDB. Extract:
- EM-reported health scores (all 5 dimensions)
- Health Flag (Red/Yellow/Green), MRR, Renewal Date
- Pod, EM, ME
- Historical score entries (for trend)

### 2. Sprint Tracker — Engagement Stage
Database ID: `2102ba60-bc74-8058-b988-000b509f811f`. Extract:
- Sprint Kickoff Date, Sprint Length, Transition Date, Sprint Status

### 3. Sync Notes — Recent Context
Search for "{Client Name}" sync/meeting notes, last 60-90 days. Extract:
- Discussion points, client feedback, action items, performance data

---

## Engagement Stage Classification

| Stage | Criteria | Performance/ROI Effect |
|-------|----------|------------------------|
| SPRINT | Pre-Transition Date | Foundation-building criteria |
| NEW | 0-3 months since Transition Date | Foundation-building criteria |
| ESTABLISHED | 3+ months since Transition Date | Outcomes criteria |

---

## Evidence Buckets

After gathering, sort ALL evidence into per-dimension buckets before scoring:

1. **Relationship** — relationship signals only
2. **Quantity** — delivery/contractual signals only
3. **Content Quality** — quality/feedback signals only
4. **Performance/ROI** — results/KPI signals only
5. **Strategy** — plan/alignment signals only
6. **EM Assessment** (optional — only if user requested EM evaluation) — question quality, dimension coverage, communication patterns, Slack behavior

When scoring a dimension, use ONLY that dimension's bucket. This enforces independence.
