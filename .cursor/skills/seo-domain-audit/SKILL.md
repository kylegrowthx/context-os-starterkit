---
name: seo-domain-audit
description: |
  **SEO Domain Audit**: Pull a comprehensive SEO snapshot for a single domain using SEMRush and DataForSEO APIs. Classifies all indexed pages by type, calculates 6-month deltas, runs content trajectory analysis, computes efficiency metrics, and produces a narrative overview with raw data archive.
  - MANDATORY TRIGGERS: SEO audit on {domain}, audit {domain}, domain overview for {domain}, pull SEO metrics for {domain}, SEO snapshot, organic traffic audit
---

# SEO Domain Audit

Comprehensive SEO audit for a single domain. Pulls all data from SEMRush and DataForSEO, classifies every indexed page, calculates 6-month changes, and produces a narrative analysis document plus raw data files.

## Inputs

Before starting, confirm or gather:

1. **Domain** — the website to audit (e.g., `flodesk.com`)
2. **Client name** — used for output directory (e.g., `flodesk`)
3. **Output directory** — default: `projects/audit-reports/{client}/`
4. **Comparison period** — default: 6 months (current vs 6 months ago from SEMRush history)

## MCP Tools Required

- `user-semrush` — domain_rank, domain_rank_history, backlinks_overview, domain_organic
- `user-dataforseo` — dataforseo_labs_google_domain_rank_overview
- `user-pagespeed` (optional) — page-level Lighthouse audits
- `user-a11y` (optional) — accessibility audits via axe-core

**Before calling any MCP tool, always read the tool's JSON schema first.**

## Workflow

### Step 1 — Pull Core Domain Metrics

Run these SEMRush calls in parallel:

1. `domain_rank` (database: `us`) — SEMRush Rank, organic keywords, organic traffic, traffic value, adwords metrics
2. `domain_rank_history` (database: `us`, display_limit: 15, display_sort: `dt_desc`) — monthly snapshots for 12+ months
3. SEMRush `backlinks_overview` — total backlinks, referring domains, authority score

Save raw responses as:
- `raw-domain-overview.md`
- `raw-domain-history.md`
- `raw-backlinks-overview.md`

### Step 2 — Pull All Indexed Pages

Use the keyword count from Step 1 to determine the pull size. The goal is to capture **every keyword-URL pair** so that per-page metrics (keywords, traffic) are accurate — not just the top slice.

1. Set `display_limit` equal to or greater than the organic keyword count from `domain_rank` (e.g., if 76,267 keywords, set `display_limit: 80000`)
2. Use `display_sort: tr_desc` and `export_columns: Ur,Ph,Po,Nq,Tr,Tc`
3. If the keyword count exceeds 100,000, paginate: pull 100,000 at `display_offset: 0`, then 100,000 at `display_offset: 100000`, etc.

**Stop-and-ask gate:** If the domain has more than **10,000 organic keywords**, pause and confirm with the user before pulling. Large pulls consume significant API credits. Present the keyword count and ask whether to:
- Pull all (full accuracy, higher cost)
- Pull top 5,000 by traffic (fast, captures ~90%+ of traffic but undercounts pages)
- Pull a custom limit

Run SEMRush `domain_organic`:
- `database`: `us`
- `display_limit`: determined above
- `display_sort`: `tr_desc`
- `export_columns`: `Ur,Ph,Po,Nq,Tr,Tc`

Save raw response as `raw-organic-pages.md`.

### Step 3 — Pull Keyword Position Distribution

Run DataForSEO `dataforseo_labs_google_domain_rank_overview`:
- target: the domain
- location_name: "United States"
- language_code: "en"

This returns keyword counts by position bucket (pos 1, 2-3, 4-10, 11-20, etc.) plus rising/declining/new keyword momentum.

### Step 4 — Classify Pages

Classify every indexed page into one of these types based on URL pattern and subdomain:

| Type | URL Patterns |
|------|-------------|
| Brand | Homepage, `/pricing`, `/about`, `/product`, `/features`, `/careers`, `/partners`, product-specific pages |
| Content | `/blog/`, `/tips/`, `/resources/`, `/articles/`, `/guides/` — editorial pages |
| Templates | `/templates/` — gallery and individual template pages |
| Transactional | `/sign-in`, `/sign-up`, `/checkout`, `/login`, `/register`, legal pages (`/terms`, `/privacy`) |
| Education | `university.*`, `/courses/`, `/academy/`, `/learn/` |
| Support | `help.*`, `support.*`, `/help/`, `/support/`, `/faq/` |
| User-generated | `view.*`, `usercontent.*`, hosted customer content |
| Docs | `developers.*`, `docs.*`, `/docs/`, `/api/`, design system pages |
| Other | Anything not matching above patterns |

Adapt patterns to the specific domain. Inspect the first 50 URLs to identify the domain's URL structure before classifying.

### Step 5 — Calculate 6-Month Changes

Using `domain_rank_history`, identify the snapshot closest to 6 months ago and the current snapshot. Calculate percentage changes for:

- Organic traffic
- Organic keywords
- Referring domains (if available from backlinks history)
- Pages indexed (count from organic pages pull vs historical)
- Pages with traffic
- Traffic per page

For each page type from Step 4, calculate:
- Pages (count and 6mo change)
- Keywords (sum and 6mo change)
- Pages with traffic (count and 6mo change)
- Traffic (sum and 6mo change)
- Traffic per page (average and 6mo change)

### Step 6 — Content Page Trajectory Analysis

For all content pages (blog + editorial sections) that have traffic:

1. Calculate the percentage traffic change over 6 months for each page
2. Categorize into five buckets:

| Category | Threshold |
|----------|-----------|
| Freefall | Lost >50% of traffic |
| Declining | Lost 10-50% |
| Stable | -10% to +25% |
| Growing | +25% to +100% |
| Surging | >+100% or new (no traffic 6mo ago) |

3. For each category, calculate:
   - Page count and percentage of total
   - Current aggregate traffic
   - Historical aggregate traffic
   - Net traffic change
   - Average traffic per page

4. Break down by content section (e.g., tips vs blog)

Save detailed per-page data as `content-pages-detail.md`.

### Step 7 — Compute Efficiency Metrics

Calculate these metrics for the domain:

| Metric | Formula |
|--------|---------|
| Traffic per keyword | organic_traffic / organic_keywords |
| Traffic per page (all with traffic) | organic_traffic / pages_with_traffic |
| Traffic per content page (with traffic) | content_traffic / content_pages_with_traffic |
| Keywords per page (all indexed) | organic_keywords / total_pages |
| Top-3 keyword concentration | (pos_1 + pos_2_3) / total_dataforseo_keywords |
| Top-10 keyword concentration | (pos_1 + pos_2_3 + pos_4_10) / total_dataforseo_keywords |

### Step 8 — Write the Overview Document

Produce `seo-overview-v1.md` with these sections:

```
# SEO Overview: {domain} (v1)

**Date:** {date}
**Source:** SEMRush (US database) + DataForSEO
**Domain:** {domain}

---

## Core metrics snapshot
- Headline metrics table (9 metrics with current, historical, 6mo change)
- 12-month trend table

## Site structure & technical
- Authority and link profile analysis
- Homepage traffic share
- Page breakdown by type (full table with all types)
- Index bloat analysis (user-generated content)
- Templates / structural opportunities

## Content health
- Content breakdown by section
- Content page trajectory analysis (all 5 buckets)
- Section-by-section diagnosis
- Efficiency metrics table

## Summary & highest-leverage fixes
- What's working (bullet points)
- What's broken (bullet points)
- Prioritized fix recommendations

## Raw data files
- List of all raw data files produced
```

### Step 9 — (Optional) Page-Level Audits

If requested, run Lighthouse and accessibility audits on the highest-traffic pages:

1. Select 1-3 pages to audit (highest-traffic content page, homepage, key landing page)
2. Run PageSpeed MCP tool for Lighthouse scores
3. Run a11y MCP tool for accessibility violations
4. Save results to `page-audits-pagespeed/` and `page-audits-a11y/`
5. Add findings to the overview document

## Output Files

| File | Contents |
|------|----------|
| `seo-overview-v1.md` | Main analysis document |
| `raw-domain-overview.md` | SEMRush domain_rank response |
| `raw-domain-history.md` | SEMRush domain_rank_history response |
| `raw-backlinks-overview.md` | SEMRush backlinks_overview response |
| `raw-organic-pages.md` | All indexed pages with classification |
| `content-pages-detail.md` | All content pages with per-page traffic data |

All files saved to `projects/audit-reports/{client}/`.

## Key Rules

- **Save raw data first.** Always persist API responses before processing. If a step fails, raw data is preserved.
- **Classification is domain-specific.** Inspect actual URLs before applying patterns. Every domain has a different structure.
- **6-month comparison uses SEMRush history.** Match the closest monthly snapshot to 6 months ago — don't interpolate.
- **Narrative over tables.** The overview document tells a story. Every table should have a "what this means" paragraph.
- **Flag anomalies.** If traffic-per-page goes up while total traffic goes down, explain why (tail pages dropping out raises the average).
