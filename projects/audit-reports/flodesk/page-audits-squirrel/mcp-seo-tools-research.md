# MCP Servers for Page-Level SEO, Performance & Content Audits

**Date:** February 28, 2026
**Purpose:** Evaluate available MCP servers for page-level website auditing (SEO, technical, performance, content, accessibility)
**Context:** We're auditing 467 Flodesk content pages. SquirrelScan gives us 230+ rule audits per page. What else is out there?

---

## The landscape

There are three tiers of tools:

1. **Page-level auditors** — crawl a single URL, run checks, return issues (what we need)
2. **SEO data platforms** — keyword rankings, backlinks, traffic (what SEMRush MCP already does)
3. **Web scrapers** — extract content for analysis (useful as input, not audit output)

Most "SEO MCP servers" are tier 2 — they give you keyword and backlink data, not technical page audits. True page-level auditing via MCP is still a thin market.

---

## Comparison: 24 tools evaluated

### Tier 1: Page-Level Technical Auditors (what we need)

| Tool | MCP? | Page audit | Perf | A11y | Security | Content | On-page SEO | Pricing | Notes |
|------|------|-----------|------|------|----------|---------|-------------|---------|-------|
| **SquirrelScan** | CLI (skill) | 230+ rules | Yes (CWV) | Yes | Yes | Yes | Yes | Free (CLI) | What we're using. Broadest single-page coverage. |
| **SEO Audit MCP** (richarddillman) | Yes | Yes | Lighthouse | Basic | No | Yes | Yes | Free (OSS) | Runs Lighthouse + custom page analysis. Needs Chrome. |
| **Lighthouse MCP** (danielsogl) | Yes | Perf only | Full CWV | Yes | No | No | Yes | Free (OSS) | Pure Lighthouse wrapper. Deep performance + a11y scores. |
| **Lighthouse MCP** (priyankark) | Yes | Perf only | Full CWV | Yes | No | No | Yes | Free (OSS) | Alternative Lighthouse MCP. Mobile/desktop throttling. |
| **PageSpeed Insights MCP** | Yes | Perf only | Full CWV | Yes | No | No | Yes | Free (Google API) | Wraps Google's PSI API. Real-world CrUX data + lab data. |
| **Chrome DevTools MCP** | Yes | Manual | Yes | No | No | No | No | Free (OSS, 27K stars) | Direct browser control. Profile perf, inspect network. Not automated audit. |
| **axe MCP Server** (Deque) | Yes | A11y only | No | WCAG full | No | No | No | Included w/ axe DevTools | Gold standard for accessibility. WCAG 2.1 AA. One-click fixes. |
| **A11y MCP** (open source) | Yes | A11y only | No | axe-core | No | No | No | Free (OSS) | Open-source axe wrapper. Lighter than Deque's. |
| **DataForSEO On-Page API** | Yes (MCP) | 60+ metrics | Lighthouse | No | No | Yes | Yes | $0.000125–$0.00425/page | Full crawl + Lighthouse. Pay-per-page. Best API-based auditor. |
| **SEO Inspector MCP** (mgsrevolver) | Yes | Basic | No | No | No | No | Yes | Free (OSS) | Titles, meta, H1, canonical, schema validation only. Lightweight. |
| **Screaming Frog** | No MCP (CLI) | 300+ rules | Yes | Yes (axe) | No | Yes | Yes | £199/yr | Industry standard. Headless CLI. No MCP but scriptable. |
| **Sitebulb** | No MCP | 300+ rules | Yes | Yes | No | Yes | Yes | £95/mo (cloud) | Deep crawling. No API or MCP. Desktop/cloud only. |

### Tier 2: SEO Data Platforms (keyword/backlink data, not page audits)

| Tool | MCP? | What it provides | Page audit? | Pricing | Notes |
|------|------|-----------------|-------------|---------|-------|
| **SEMRush** | Yes | Keywords, traffic, backlinks, domain metrics | Only w/ project | Subscription | What we already use. Site audit needs project setup. |
| **Ahrefs MCP** | Yes | Keywords, backlinks, content gaps, rank tracking | Only w/ project | Subscription | Similar to SEMRush. Site audit requires Ahrefs project. |
| **SE Ranking MCP** | Yes | Keywords, rank tracking, backlinks, site audit | Yes (w/ project) | Subscription | Has on-page checker + site audit via API. Docker deploy. |
| **Moz API** | Via Apify | DA/PA, spam score, link metrics | No | $5–$10K/mo | No official MCP. Apify actor for bulk DA/PA. |
| **SEO Review Tools MCP** | Yes | DA, backlinks, keyword data, traffic estimates | No | Freemium | Good for quick domain metrics. No page-level audit. |
| **FetchSERP MCP** | Yes | SERP data, keywords, backlinks, domain info | Basic | 250 free credits | 21+ endpoints. Moz DA included. Light page analysis. |
| **SerpAPI MCP** | Yes | SERP results from 40+ engines | No | $75/mo+ | Live search results, not page auditing. |
| **Google Search Console MCP** | Yes | Search performance, indexing, URL inspection | Indexing only | Free (needs GSC) | Great for search data. Not technical audit. |

### Tier 3: Web Scrapers & Content Extractors (input tools, not auditors)

| Tool | MCP? | What it provides | Pricing | Notes |
|------|------|-----------------|---------|-------|
| **Firecrawl MCP** | Yes | Page scraping, markdown extraction, JS rendering | $16–$83/mo | Best for extracting content to analyze. Not an auditor. |
| **Bright Data MCP** | Yes | SERP scraping, web scraping, anti-bot bypass | Pay-per-request | 5K free MCP requests. Enterprise scraping. |
| **Apify SEO Checker** | Yes (actor) | On-site SEO elements extraction | $8/mo + usage | Crawls and extracts SEO elements. Light audit. |
| **Apify Pro SEO Audit** | Yes (actor) | Broken links, missing images, recommendations | $9.99/mo + usage | More audit-focused than the checker. |
| **Apify Metadata Extractor** | Yes (actor) | Meta tags, robots, sitemaps, JSON-LD, tech detection | $3/mo + usage | Good metadata extraction. Not full audit. |
| **ScrapeGraphAI MCP** | Yes | AI-powered scraping and crawling | Varies | Content extraction, not auditing. |

---

## What matters for our use case

We're auditing 467 individual pages on a site we don't own. We need:

1. **Zero-setup** — no project creation, no account on the target domain
2. **Single-page audit** — not a full site crawl
3. **Broad coverage** — SEO, performance, accessibility, security, content, links
4. **Machine-readable output** — for combining with SEMRush data
5. **Batch-friendly** — 467 pages means ~1 hour of runtime max

### Best stack for page-level auditing

| Layer | Tool | What it covers | Status |
|-------|------|---------------|--------|
| **Broad audit** | SquirrelScan (CLI) | 230+ rules across 21 categories | Already running |
| **Performance deep-dive** | Lighthouse MCP or PageSpeed Insights MCP | Core Web Vitals, LCP, CLS, FCP, TTFB | Add this |
| **Accessibility deep-dive** | axe MCP Server | WCAG 2.1 AA compliance, detailed violations | Add this |
| **SEO data** | SEMRush MCP | Keywords, traffic, backlinks, rankings | Already running |
| **Content extraction** | Firecrawl MCP or Bright Data MCP | Raw content for quality analysis | Optional |

### Recommended additions

**1. PageSpeed Insights MCP** — Free, uses Google's own data (including real-world CrUX metrics when available). Would add actual Core Web Vitals scores that SquirrelScan approximates.

**2. DataForSEO On-Page API** — Most comprehensive API-based page auditor. 60+ on-page metrics + Lighthouse integration. Pay-per-page pricing ($0.000125/page basic, $0.00425/page with JS rendering). For 467 pages that's $0.06–$2.00 total. The MCP server is official and well-maintained.

**3. axe MCP Server** — If accessibility matters for the audit (it should for a content site), this is the gold standard. Free with axe DevTools.

---

## Tools NOT worth adding

| Tool | Why not |
|------|---------|
| Screaming Frog | No MCP, no API. CLI exists but requires license + desktop install. Redundant with SquirrelScan. |
| Sitebulb | No MCP, no API. Desktop only. |
| Ahrefs MCP | Requires project setup on their domain. Largely overlaps with SEMRush for our use case. |
| SE Ranking MCP | Would need a project. Overlaps with SEMRush. |
| SerpAPI / Serper | SERP data, not page auditing. |
| Moz | No MCP. DA/PA available via FetchSERP already. |
| Firecrawl | Content extraction, not auditing. We already have the pages via SquirrelScan crawl. |

---

## Summary

The MCP ecosystem for **page-level technical auditing** is surprisingly thin. Most SEO MCP servers focus on keyword/backlink data (tier 2). For actual page-by-page auditing:

- **SquirrelScan** (what we have) is the broadest single-tool option
- **DataForSEO On-Page API** is the best API/MCP option for adding depth — 60+ metrics, Lighthouse built-in, pennies per page
- **PageSpeed Insights MCP** adds real Google CWV data for free
- **axe MCP** adds proper accessibility auditing

Everything else is either redundant with what we have, requires project setup on the target domain, or doesn't do page-level auditing at all.
