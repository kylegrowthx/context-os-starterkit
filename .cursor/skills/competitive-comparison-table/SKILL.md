---
name: competitive-comparison-table
description: |
  **Competitive Comparison Table**: Produce a comprehensive multi-axis comparison document combining SEO performance metrics (traffic, keywords, momentum, efficiency) and AI visibility metrics (visibility score, presence rate, position, source control) for a set of competitors. Includes combined ranking with SEO-vs-AEO gap analysis.
  - MANDATORY TRIGGERS: competitive comparison table, side-by-side competitor comparison, compare all competitors SEO and AI, competitive benchmark table, SEO vs AI comparison
---

# Competitive Comparison Table

Produce a single document with three tables — SEO performance, AI visibility, and combined ranking — for a set of competitors. Designed as a standalone reference artifact that cross-references organic search strength against AI recommendation presence.

## Inputs

Before starting, confirm or gather:

1. **Competitor list** — names and domains for all brands to include
2. **Exclusions** — brands to exclude (e.g., platform-wide domains)
3. **Existing data** — check for prior outputs from:
   - Competitive SEO Landscape skill → `competitive-landscape-v1.md`, `competitors-raw/`
   - AEO Audit skill → `aeo/competitive-visibility-dump-v1.md`, `aeo/presence-score-analysis-v1.md`
4. **Output directory** — default: `projects/audit-reports/{client}/`

If existing data files are found, read them first. Only pull fresh API data for metrics not covered by existing files.

## MCP Tools Required

- `user-semrush` — domain_rank, domain_rank_history
- `user-dataforseo` — dataforseo_labs_google_domain_rank_overview

AI visibility data comes from CheckThat (read from existing AEO audit outputs or pull fresh).

## Workflow

### Step 1 — Gather SEO Data

For each competitor, collect:

| Metric | Source | Notes |
|--------|--------|-------|
| Organic traffic (current) | SEMRush `domain_rank` | Feb 2026 snapshot |
| Organic traffic (6mo ago) | SEMRush `domain_rank_history` | Aug 2025 snapshot |
| Organic keywords (current) | SEMRush `domain_rank` | |
| Organic keywords (6mo ago) | SEMRush `domain_rank_history` | |
| Traffic value | SEMRush `domain_rank` | Organic Cost column |
| KW rising | DataForSEO `domain_rank_overview` | is_new field |
| KW declining | DataForSEO `domain_rank_overview` | is_down field |

Calculate derived metrics:
- **Traffic 6mo change %** — `(current - historical) / historical × 100`
- **KW 6mo change %** — `(current - historical) / historical × 100`
- **KW Net** — `is_new - is_down` (simplified momentum)
- **Traffic/KW** — `organic_traffic / organic_keywords`
- **Traffic/KW 6mo change %** — derived from historical traffic/KW

Batch SEMRush calls in groups of 8. Pull DataForSEO for all competitors (not just a subset).

### Step 2 — Gather AI Visibility Data

For each competitor, collect from CheckThat data:

| Metric | Source |
|--------|--------|
| AI visibility score (average) | competitive-visibility-dump or CheckThat DB |
| Visibility range (min–max) | Daily score extremes |
| Position quality (1-5 scale) | presence-score-analysis |
| Presence rate (%) | presence-score-analysis |
| Source control (%) | presence-score-analysis |

If no AEO data exists for a competitor (not tracked in CheckThat), mark as "n/a" in the table.

### Step 3 — Build SEO Performance Table

Sort by organic traffic descending:

```markdown
| SEO # | Company | Traffic | Traf Δ | KW | KW Δ | KW Net | Traf/KW | T/KW Δ |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
```

Column definitions (include below the table):
- **Traffic** — Monthly organic visits (SEMRush US)
- **Traf Δ** — 6-month traffic change percentage
- **KW** — Total ranking keywords (SEMRush US)
- **KW Δ** — 6-month keyword count change percentage
- **KW Net** — Keyword momentum: new minus declining (DataForSEO)
- **Traf/KW** — Traffic per keyword (ranking efficiency)
- **T/KW Δ** — 6-month change in traffic per keyword

Highlight the focal domain in **bold**.

### Step 4 — Build AI Visibility Table

Sort by AI visibility score descending:

```markdown
| AEO # | Company | AI Vis | Range | Position | Presence % | Source Ctrl |
|---:|---|---:|---|---:|---:|---:|
```

Column definitions:
- **AI Vis** — Average AI visibility score (0-100)
- **Range** — Visibility trough–peak
- **Position** — Average position quality when mentioned (1-5 scale)
- **Presence %** — Percentage of evaluation probes mentioning the brand
- **Source Ctrl** — Percentage of citation-bearing probes citing brand's own domain

### Step 5 — Build Combined Ranking Table

Sort by company name alphabetically or by SEO rank:

```markdown
| Company | SEO # | AEO # | Gap | Traffic | AI Vis |
|---|---:|---:|---:|---:|---:|
```

**Gap** = SEO rank minus AEO rank:
- **Negative gap** = AI underperforms relative to SEO position (company is stronger in search than in AI)
- **Positive gap** = AI overperforms relative to SEO position (company is stronger in AI than in search)

Include interpretation note below the table.

### Step 6 — Write Narrative Analysis

After the three tables, include a "What the data reveals" section:

1. **SEO and AI are different games** — identify companies where the gap is largest in both directions. Name specific examples.

2. **Focal domain's gap** — where does it sit? Better or worse than peers? What's the path to improvement?

3. **Companies declining on both fronts** — filter for negative traffic trend AND net-negative keyword momentum. Table them. Note which have AI visibility as a buffer.

4. **Companies winning both channels** — filter for positive traffic trend AND positive keyword momentum AND top-half AI visibility. Table them.

5. **Source Control separates contenders** — highlight the top source control performers and what it means.

### Step 7 — Write the Document

Produce `competitive-comparison-v1.md`:

```markdown
# Competitive Comparison: SEO + AI Visibility

**Date, sources, methodology notes**

> **Note:** [any caveats about data availability]

---

## SEO Performance
[Table + column definitions]

---

## AI Visibility
[Table + column definitions]

---

## Combined Ranking
[Table + gap interpretation]

---

## What the data reveals
[5 narrative subsections]

---

## Raw data references
[List of supporting files]
```

## Output Files

| File | Contents |
|------|----------|
| `competitive-comparison-v1.md` | The full comparison document |

Saved to `projects/audit-reports/{client}/`.

## Key Rules

- **All three tables in one document.** This is a single-file reference artifact, not split across multiple documents.
- **Consistent competitor set.** The same companies appear in all three tables. If a company lacks AI data, include it with "n/a" values — don't omit it.
- **Highlight the focal domain.** Bold in every table.
- **Gap analysis drives the narrative.** The combined ranking table is the most valuable part. The narrative should focus on what the gaps mean.
- **No fabricated AI metrics.** If a competitor isn't tracked in CheckThat, mark as n/a. Don't estimate.
