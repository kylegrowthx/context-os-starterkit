---
name: competitive-seo-landscape
description: |
  **Competitive SEO Landscape**: Pull SEMRush domain metrics and DataForSEO keyword momentum for a set of competitors. Produces tiered competitive landscape with traffic rankings, keyword position distribution, efficiency metrics, and direct threat analysis.
  - MANDATORY TRIGGERS: competitive landscape for {domain}, competitor SEO analysis, benchmark {domain} against competitors, SEO competitive comparison, competitive SEO landscape
---

# Competitive SEO Landscape

Pull SEMRush and DataForSEO metrics for a set of competitors. Rank by organic traffic, calculate efficiency metrics, analyze keyword momentum, and produce a tiered competitive landscape document.

## Inputs

Before starting, confirm or gather:

1. **Focal domain** — the domain being benchmarked (e.g., `flodesk.com`)
2. **Competitor list** — names, domains, and tiers. Accept as:
   - A markdown table or list provided by the user
   - A reference to an existing competitor list file
   - A request to build the list from scratch (use web research + the focal domain's market)
3. **Tier definitions** — default: Tier 1 (market leaders), Tier 2 (strong challengers), Tier 3 (peer group). User may provide custom tier criteria.
4. **Business metrics** (optional) — revenue, employees, funding per competitor. Enriches efficiency calculations.
5. **Output directory** — default: `projects/audit-reports/{client}/`
6. **Exclusions** — competitors to exclude from the analysis (e.g., platform-wide domains like Substack, Zoho)

## MCP Tools Required

- `user-semrush` — domain_rank, domain_rank_history
- `user-dataforseo` — dataforseo_labs_google_domain_rank_overview

**Before calling any MCP tool, always read the tool's JSON schema first.**

## Workflow

### Step 1 — Resolve Competitor List

If the user provides a list, validate each domain is reachable. If building from scratch:

1. Research the focal domain's market category
2. Identify 20-35 direct and adjacent competitors
3. Assign tiers based on revenue, funding, market position
4. Present the list for user approval before pulling data

### Step 2 — Pull SEMRush Domain Metrics (Batch)

For each competitor domain, call SEMRush `domain_rank` (database: `us`):

- Batch in groups of 8-10 parallel calls
- Extract: SEMRush Rank, Organic Keywords, Organic Traffic, Organic Cost (traffic value), Adwords metrics

Also pull for the focal domain if not already available from a prior SEO Domain Audit.

Save raw output as `competitors-raw/semrush-domain-rank-all.csv` in semicolon-delimited format:

```
Domain;Rank;Organic Keywords;Organic Traffic;Organic Cost;Adwords Keywords;Adwords Traffic;Adwords Cost
```

### Step 3 — Pull SEMRush History (Batch)

For each competitor, call SEMRush `domain_rank_history` (database: `us`, display_limit: 15, display_sort: `dt_desc`).

- Batch in groups of 8 parallel calls
- Extract the row closest to 6 months ago and the most recent row
- Calculate 6-month changes for: traffic, keywords, traffic/keyword

### Step 4 — Pull DataForSEO Keyword Momentum

For each competitor (or at minimum the top 10-15 by traffic), call DataForSEO `dataforseo_labs_google_domain_rank_overview`:
- target: competitor domain
- location_name: "United States"
- language_code: "en"

Extract:
- Total keyword count
- Position distribution: pos_1, pos_2_3, pos_4_10 (for top-3 and top-10 concentration)
- Keyword momentum: is_new (rising), is_up, is_down
- Calculate: KW Net = is_new + is_up - is_down (simplified) or is_new - is_down (net new vs lost)

Save raw output as `competitors-raw/dataforseo-domain-rank-overview.json`.

### Step 5 — Build Rankings and Efficiency Tables

**All competitors ranked by organic traffic:**

| Organic Rank | Company | Tier | Organic Traffic | Organic KW | Traffic Value ($) | Traffic/KW | SEMRush Rank |
|---:|---|---|---:|---:|---:|---:|---:|

**Keyword position distribution (DataForSEO subset):**

| Company | Total KW | Top 3 | Top 3 % | Top 10 | Top 10 % | KW Rising | KW Declining | Net |
|---|---:|---:|---:|---:|---:|---:|---:|---:|

**Efficiency metrics:**

| Metric | Focal Domain | Rank (of N) | Context |
|---|---|---|---|

Calculate:
- Traffic per keyword — `organic_traffic / organic_keywords`
- Top-3 keyword concentration — `(pos_1 + pos_2_3) / total_dataforseo_keywords`
- Top-10 keyword concentration — `(pos_1 + pos_2_3 + pos_4_10) / total_dataforseo_keywords`
- Traffic value per employee — `organic_cost / employees` (only if employee data available)

### Step 6 — Identify Direct Competitive Threats

For the 3-5 closest competitors (by audience overlap, market position, or organic proximity):

Write 1 paragraph each covering:
- Organic footprint comparison (keywords, traffic, traffic/KW)
- Key strategic difference (pricing, features, audience)
- Rising or declining trajectory
- What this means for the focal domain

### Step 7 — Write the Landscape Document

Produce `competitive-landscape-v1.md`:

```
# Competitive Landscape: {Focal Domain} — Tiers 1-3 with SEMRush Domain Metrics

**Date, sources, methodology note**

---

## Executive Summary
- 2-3 paragraph overview of focal domain's position
- Headline finding (e.g., "ranks Xth by traffic but Yth by efficiency")

## Focal Domain Profile
- Company attributes table
- SEMRush snapshot table

## Scoring Methodology
- How tiers were assigned (dimensions and weights)

## Tier 1: Market Leaders
- Business metrics table
- SEMRush domain metrics table
- 1-paragraph narrative per major player

## Tier 2: Strong Challengers
- Same structure

## Tier 3: Peer Group
- Same structure (focal domain highlighted in bold)

## All Competitors Ranked by Organic Traffic
- Full ranking table

## Keyword Position Distribution
- Comparison table for top competitors

## Efficiency Metrics
- Traffic value per employee
- Traffic per keyword
- Rankings and context

## What the Organic Data Reveals
- Narrative analysis (strengths, gaps, threats, declining trends)

## Key Competitive Threats
- 3-5 competitor deep-dives

## Data Sources
- Table of sources with descriptions
```

### Step 8 — Archive Raw Data

Create `competitors-raw/README.md` documenting:
- What files are in the folder
- Data source, pull date, and parameters for each
- Known limitations (e.g., "DataForSEO backlinks API not available")

## Output Files

| File | Contents |
|------|----------|
| `competitive-landscape-v1.md` | Full tiered analysis |
| `competitors-raw/semrush-domain-rank-all.csv` | Raw SEMRush data for all competitors |
| `competitors-raw/dataforseo-domain-rank-overview.json` | Raw DataForSEO keyword data |
| `competitors-raw/README.md` | Archive documentation |

All files saved to `projects/audit-reports/{client}/`.

## Key Rules

- **Exclude platform-wide domains.** Substack, Zoho, and similar platform domains inflate metrics. Note them with asterisks if included, or exclude per user instruction.
- **Batch API calls.** Never call 30 domains sequentially — batch in groups of 8-10 parallel calls.
- **Save raw data before processing.** If analysis fails, the raw data is preserved for retry.
- **Highlight the focal domain.** Use bold formatting in every ranking table to make the focal domain easy to find.
- **Narrative per tier.** Don't just show tables — each tier section needs 1-2 paragraphs of analysis explaining what the numbers mean.
