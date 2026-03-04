---
name: aeo-audit
description: |
  **AEO Audit Report**: Generate a comprehensive AI Engine Optimization audit for a brand tracked in CheckThat's AI Visibility Index. Covers visibility score and trend, presence analysis, citation and source analysis, competitive positioning, root cause analysis, presence score calculation, and phased recommendations.
  - MANDATORY TRIGGERS: AEO audit for {brand}, AI visibility report, how visible is {brand} to AI, AI engine optimization audit, AI visibility audit, AEO report, CheckThat audit
---

# AEO Audit Report

Produce a comprehensive AI visibility audit for a brand using data from the CheckThat AI Visibility Index. Covers visibility scoring, mention analysis, citation/source mapping, competitive rankings, root cause diagnosis, and actionable recommendations.

## Prerequisites

This skill requires an **active CheckThat workspace** with:
- A tracked brand (the audit target)
- At least 30 days of tracking data (60+ days preferred)
- Evaluation-stage, unbranded buyer prompts activated
- Competitors configured in the workspace

The skill reads data from the CheckThat production database. Access method depends on available tooling — direct DB queries, CheckThat API, or pre-exported data files.

## Inputs

Before starting, confirm or gather:

1. **Brand name** — the brand to audit (e.g., "Flodesk")
2. **Brand domain** — primary domain (e.g., `flodesk.com`)
3. **CheckThat workspace ID** — the workspace UUID
4. **Tracking period** — date range of available data
5. **Output directory** — default: `projects/audit-reports/{client}/aeo/`
6. **Competitor context** — whether a separate SEO competitive landscape exists (for cross-referencing)

## Workflow

### Step 1 — Extract Visibility Data

Pull from the CheckThat workspace:

1. **Daily visibility scores** for the target brand — full tracking period
2. **Monthly averages** — aggregate by calendar month
3. **Latest 2-week average** — most recent window
4. **Peak and trough** — daily extremes

Calculate:
- Overall average visibility score
- Month-over-month trend (% change)
- Rank among all tracked competitors

### Step 2 — Extract Mention and Presence Data

Pull mention-level data:

1. **Total mentions** across all probes
2. **Rank distribution** — count of mentions at each rank position (1, 2, 3, ... 10, 11+)
3. **Average rank when mentioned**
4. **Top 1-3 mentions** — count and percentage
5. **Sentiment breakdown** — positive, neutral, negative counts and percentages

Calculate:
- **Presence Rate** — probes mentioning the brand / total probes
- Mode rank position
- Rank distribution histogram (text-based)

### Step 3 — Extract Citation and Source Data

Pull citation data:

1. **Own-domain citation count** — how often the brand's domain appears as a cited source
2. **Own-domain citation rate** — own citations / total citation-bearing probes
3. **Which brand URLs get cited** — list with citation counts and content type
4. **Days the domain is cited** — out of total tracked days

Pull source ecosystem data:

1. **Top cited domains** — all domains cited across the workspace, with days-cited counts
2. **Competitor domain citation frequency** — days cited for each tracked competitor

Classify all cited domains into these types:

| Type | Description |
|------|------------|
| Competitor | Tracked competitor domains |
| Review Platform | G2, Capterra, Clutch, TrustRadius, etc. |
| Tech Media | TechRadar, PCMag, ZDNet, The Verge, etc. |
| Press / News | Forbes, Business Insider, Entrepreneur, etc. |
| Aggregator / Comparison | emailtooltester, Zapier, SeedProd, etc. |
| Community | Reddit, LinkedIn, Medium, forums |
| Reference / Educational | Wikipedia, Coursera, AMA, dictionaries |
| Video | YouTube |
| Adjacent Software | Non-competitor tools in the ecosystem |

### Step 4 — Extract Competitive Rankings

Pull competitive visibility data:

1. **All-time average visibility** for every tracked competitor
2. **Latest 2-week visibility** for every competitor
3. **Monthly trend** for the target brand
4. **Mention volumes** — total mentions, sentiment, average rank for top competitors

Build competitive tier classification:

| Tier | Visibility Range | Description |
|------|-----------------|-------------|
| Tier 1: AI Leaders | >30 | Dominate AI responses |
| Tier 2: Established Presence | 10-30 | Regularly mentioned, not leading |
| Tier 3: Emerging/Low Presence | 3-10 | Occasionally mentioned |
| Tier 4: Invisible | <3 | AI doesn't recommend them |

### Step 5 — Calculate Presence Score

Apply the CheckThat Presence Score formula:

```
TIER 1 — VISIBILITY (0-70 pts)    = 70 × (Rate / 100)
TIER 2 — DURABILITY (0-9 pts)     = 9 × (Stability / 100) × (Rate / 100)
TIER 3 — POSITION (0-8 pts)       = 8 × (Position / 100) × √(Rate / 100)
TIER 4 — SOURCE CONTROL (0-8 pts) = 8 × (SourceControl / 100) × √(Rate / 100)
TIER 5 — COVERAGE (0-5 pts)       = 5 × (CrossEngine / 100) × √(Rate / 100)

PRESENCE SCORE = T1 + T2 + T3 + T4 + T5   (Scale: 0-100)
```

Sub-metrics:
- **Presence Rate** — % of probes where brand is mentioned
- **Stability Index** — 100 − coefficient of variation of weekly presence rates
- **Position** — average rank quality normalized (Recommended=5, 1st=4, 2nd-3rd=3, Listed=2, Afterthought=1) to 0-100
- **Source Control** — % of citation-bearing probes citing the brand's own domain
- **Cross-Engine Coverage** — % of tracked AI engines (typically 5) that mention the brand

Calculate for the target brand AND all competitors. Rank accordingly.

Interpretation scale:

| Range | Rating |
|-------|--------|
| 85-100 | Exceptional |
| 70-84 | Strong |
| 50-69 | Moderate |
| 30-49 | Low |
| 10-29 | Weak |
| 0-9 | Invisible |

### Step 6 — Root Cause Analysis

Diagnose why the brand's visibility is what it is. Evaluate each factor:

1. **Source footprint** — is the brand's domain cited by AI? How often vs competitors?
2. **Listicle presence** — is the brand featured on the most-cited "best of" roundups?
3. **Content volume and type** — does the brand produce content AI cites (glossary, comparison, educational)?
4. **Content positioning** — is the content narrow (only alternatives pages) or broad (full buyer journey)?
5. **Third-party presence** — review platforms (G2, Capterra), Reddit, media coverage
6. **Homepage citeability** — is the homepage structured for AI extraction?

For each factor, compare the target brand against the top performers.

### Step 7 — Write Output Documents

Produce 4 files:

**1. `aeo-audit-report-v1.md`** — Main audit document:

```
# {Brand} AEO Audit Report

*Analysis Date, data source, tracking period, prompt count, AI engines, competitor count*

---

## Executive Summary (3-5 paragraphs)

## 1. Visibility Assessment
- Overall score, peak, trough, monthly trend table
- Visibility gap to competitors table

## 2. Presence Analysis
- Mention volume and position table
- Rank distribution histogram
- Sentiment breakdown

## 3. Citation and Source Analysis
- Own-domain citation rate
- Brand URLs that get cited (table)
- Dominant third-party sources
- Category-defining URLs

## 4. Competitive Tier Positioning
- AI visibility map (4 tiers with brands)
- Revenue-visibility paradox analysis

## 5. Root Cause Analysis
- Why AI does/doesn't recommend this brand (5 root causes)
- What the brand does well in AI

## 6. Recommendations
- Immediate (0-30 days)
- Short-term (30-90 days)
- Medium-term (90-180 days)

## 7. Appendices
- Key data points, supporting files, methodology
```

**2. `source-analysis-v1.md`** — Deep source classification:
- All cited domains classified by type
- Content type analysis of top 300 URLs
- Competitor source strategy breakdown
- Competitor listicle problem analysis

**3. `competitive-visibility-dump-v1.md`** — Raw competitive data:
- Full visibility rankings table
- Latest 2-week rankings
- Monthly trend for target brand
- Mention volume comparison table
- Key metrics comparison (target vs top 7)
- Tier classification

**4. `presence-score-analysis-v1.md`** — Presence score details:
- Full rankings table with component scores
- Sub-metric detail tables (rate, stability, position, source control, coverage)
- Target brand deep dive with tier-by-tier diagnosis
- Distance to competitive tiers
- Strategic implications

## Key Rules

- **Data-driven root causes.** Every root cause must reference specific data points (e.g., "cited 13 of 73 days" not "low citation rate").
- **Competitor context is essential.** Every metric about the target brand should be compared to competitors.
- **Separate the bright spots.** Even low-visibility brands have positive signals (sentiment, specific prompt angles). Always document them.
- **Recommendations are phased.** 0-30, 30-90, 90-180 days. Immediate actions should be concrete and specific.
- **No fabricated data.** If a data point isn't available, note it as unavailable. Don't estimate AI visibility metrics.
