---
name: content-pages-audit
description: |
  **Content Pages Audit**: Pull per-page SEO data for every content page on a domain, compare current vs 6 months ago, then run page-level performance/SEO/accessibility audits on the top pages. Produces two files: a detailed per-page traffic comparison and a scored audit of blog/content pages.
  - MANDATORY TRIGGERS: content pages audit, content page detail, blog audit, audit content pages, per-page SEO audit, page-level audit
---

# Content Pages Audit

Per-page SEO data pull and quality audit for all content pages on a domain. Compares current vs 6-month-ago organic data from SEMRush, then layers on PageSpeed performance, on-page SEO, security headers, and accessibility audits for the top pages.

## Inputs

Before starting, confirm or gather:

1. **Domain** — the website to audit (e.g., `vercel.com`)
2. **Content URL patterns** — which URL paths count as "content" (e.g., `/blog/`, `/tips/`, `/resources/`, `/guides/`, `/kb/`). Inspect the domain's URL structure first.
3. **Output directory** — default: `projects/audit-reports/{client}/`
4. **Comparison period** — default: 6 months ago (via SEMRush `display_date`)
5. **Audit depth** — how many top pages to run full audits on (default: all content pages with traffic, up to 50)

## MCP Tools Required

- `user-semrush` — `domain_organic` (current + historical with `display_date`)
- `user-pagespeed` — `performance_audit`, `onpage_seo_audit`, `security_headers_audit`
- `user-a11y` — `audit_webpage`

**Before calling any MCP tool, always read the tool's JSON schema first.**

## Workflow

### Step 1 — Identify Content URL Patterns

Before pulling data, inspect the domain's URL structure:

1. Pull a small sample of `domain_organic` (top 200 by traffic) to understand the URL taxonomy
2. Identify which URL patterns are "content pages" — editorial, blog, resource center, KB, guides, etc.
3. Confirm the patterns with the user if ambiguous

Common patterns:

| Type | Typical Patterns |
|------|-----------------|
| Blog | `/blog/`, `/articles/`, `/news/` |
| Tips/Resources | `/tips/`, `/resources/`, `/guides/` |
| Knowledge Base | `/kb/`, `/help/`, `/support/` |
| Docs (if content-like) | `/docs/` (only if the docs section serves as educational content) |
| Changelog | `/changelog/`, `/updates/` |

### Step 2 — Pull Current Content Page Data

Run SEMRush `domain_organic`:
- `database`: `us`
- `display_limit`: high enough to capture all content pages (start with 2000, increase if needed)
- `display_sort`: `tr_desc` (traffic descending)
- `display_filter`: filter for content URL patterns if possible, or pull all and filter locally
- `export_columns`: `Ur,Ph,Po,Nq,Tr,Tc`

Save raw response.

### Step 3 — Pull Historical Content Page Data (6 months ago)

Run the same `domain_organic` call with:
- `display_date`: `YYYYMM15` format for 6 months ago (e.g., if current is Feb 2026, use `20250815`)
- Same filters and columns as Step 2

Save raw response.

### Step 4 — Aggregate Per-Page Metrics

For both current and historical data:

1. **Extract unique URLs** from the keyword-URL pairs
2. For each unique URL, aggregate:
   - Total keywords (count of keyword-URL pairs for that URL)
   - Total traffic (sum of traffic % × total domain traffic)
   - Top keyword (highest traffic keyword for that URL)
   - Best position

3. **Classify each URL** into content sections based on URL pattern (e.g., `/blog/` = Blog, `/tips/` = Tips, `/kb/` = Knowledge Base)

### Step 5 — Calculate 6-Month Changes

For each content page that appears in either current or historical data:

1. **Keywords change** = current keywords - historical keywords
   - If page is new (not in historical): mark as "new"
   - If page disappeared: include but note it

2. **Traffic change** = current traffic - historical traffic
   - If page is new: mark as "new"

3. **Historical traffic** = the traffic value from 6 months ago (for reference)

### Step 6 — Write content-pages-detail.md

Format the output as:

```
# Content Pages with Organic Traffic — {domain}

**Date:** {date}
**Source:** SEMRush (US database)
**Scope:** All content pages ({section names}) with organic traffic > 0
**Total pages:** {count}

## Summary

| Section | Pages | Keywords | 6mo | Traffic | 6mo | Traffic/Page |
|---------|-------|----------|-----|---------|-----|--------------|
| {section} | {n} | {total kw} | — | {total traffic} | {pct change} | {avg} |
...
| **Total** | **{n}** | **{total}** | — | **{total}** | **{pct}** | **{avg}** |

---

## {Section name} ({n} pages)

| # | URL | Keywords | 6mo KW | Traffic | 6mo Traffic | Aug Traffic |
|---|-----|----------|--------|---------|-------------|-------------|
| 1 | {full url} | {kw count} | {+/-/new} | {current traffic} | {+/- change} | {historical} |
...
```

Sort each section by current traffic descending. Include ALL content pages with traffic > 0.

### Step 7 — Run Page-Level Audits

For each content page (up to audit depth limit), run these tools **in parallel batches of 3-5**:

1. `performance_audit` (strategy: `mobile`) — Core Web Vitals, Lighthouse scores
2. `onpage_seo_audit` (with top keyword as `targetKeyword`) — heading structure, content length, images, links
3. `security_headers_audit` — HSTS, CSP, X-Frame-Options
4. `audit_webpage` (a11y) — WCAG violations

**Rate limiting:** Space batches ~2 seconds apart to avoid overwhelming the target server.

For each page, extract and normalize scores:

| Category | Source | Score Range |
|----------|--------|-------------|
| Core SEO | `onpage_seo_audit` | 0–100 (normalize from findings) |
| Content | `onpage_seo_audit` | 0–100 (heading structure, word count, readability) |
| Performance | `performance_audit` | 0–100 (Lighthouse performance score) |
| Images | `onpage_seo_audit` | 0–100 (alt text coverage, optimization) |
| Links | `onpage_seo_audit` | 0–100 (broken links, anchor quality) |
| Accessibility | `audit_webpage` or `performance_audit` | 0–100 (WCAG pass rate) |
| Security | `security_headers_audit` | 0–100 (header coverage) |
| E-E-A-T | `onpage_seo_audit` | 0–100 (author, dates, structured data) |

**Overall score** = weighted average (or simple average) of all category scores.

### Step 8 — Identify Site-Wide Issues

After auditing multiple pages, look for patterns:

1. Issues that appear on **every page** — these are template/infrastructure issues
2. Issues that appear on **most pages** (>80%) — likely template-level
3. Issues unique to specific pages — content-specific fixes

Group site-wide issues into a prioritized list.

### Step 9 — Write content-pages-blog-audit.md

Format:

```
# Blog Content Pages Audit — {domain}

**Date:** {date}
**Source:** SEMRush (US database) + PageSpeed + a11y
**Scope:** All {n} blog pages with organic traffic
**Total organic traffic:** {traffic}/mo

---

## Audit score summary

| Metric | Average | Range |
|--------|---------|-------|
| **Overall score** | **{avg}/100** | {min}–{max} |
| Core SEO | {avg} | {range} |
| Content | {avg} | {range} |
| Performance | {avg} | {range} |
| Images | {avg} | {range} |
| Links | {avg} | {range} |
| Accessibility | {avg} | {range} |
| Security | {avg} | {range} |
| E-E-A-T | {avg} | {range} |

---

## Site-wide issues (affect all/most blog pages)

1. **{issue}** ({category}) — {description}
...

---

## All blog pages with audit scores

| # | URL | KW | 6mo KW | Traffic | 6mo | Aug | Score | SEO | Content | Perf | Images | Links | A11y | Sec | EEAT | Warn | Err |
|---|-----|-----|--------|---------|-----|-----|-------|-----|---------|------|--------|-------|------|-----|------|------|-----|
...

---

## Score definitions
...

## Category definitions
...
```

## Output Files

| File | Contents |
|------|----------|
| `content-pages-detail.md` | Per-page traffic data with 6mo comparison, all content sections |
| `content-pages-blog-audit.md` | Blog pages with audit scores and site-wide issue analysis |

All files saved to `projects/audit-reports/{client}/`.

## Key Rules

- **Pull historical data with `display_date`.** The 6-month comparison requires two SEMRush `domain_organic` pulls — one current, one historical. Don't interpolate.
- **Aggregate per-page, not per-keyword.** Each page may rank for many keywords. Sum keyword counts and traffic across all keyword-URL pairs for each unique URL.
- **Traffic is percentage-based in SEMRush.** The `Tr` column is a percentage of total domain traffic. Convert to absolute traffic by multiplying by `total_domain_traffic / 100`.
- **Include ALL content pages.** Don't truncate. Even pages with traffic of 1 should appear in the detail file.
- **Batch audit calls.** Running 50+ page audits sequentially is slow. Batch 3–5 concurrent calls, then wait for results.
- **Flag template issues first.** If an issue appears on every page, it's a template fix — one change lifts all pages.
- **The detail file is data, the audit file is diagnosis.** `content-pages-detail.md` is a pure data table. `content-pages-blog-audit.md` adds qualitative scoring and issue identification.
