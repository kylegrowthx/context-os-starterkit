# Page-Level Scoring Methodology

<metadata>
purpose: Scoring framework for automated page-level SEO audits — 5 scores (0-100) computed from SEMRush, PageSpeed/Lighthouse, DataForSEO, a11y, and SquirrelScan tool output
audience: GrowthX Engagement Managers, technical SEO practitioners
related: knowledge/seo-aeo/seo-ranking-factors-study-guide-v1.md, knowledge/seo-aeo/semrush-seo-audit-study-guide-v1.md
domain: SEO, content, technical
confidence: methodology
sensitivity: internal
context_tier: 2
last_updated: 2026-02-28
</metadata>

> **For:** GrowthX practitioners running page-level SEO audits using automated tools.
> **Goal:** Define a repeatable scoring methodology that turns raw tool output into five diagnostic scores per page.
> **Last Updated:** February 2026.

---

## Overview

Five scores, each 0-100. Four diagnostic dimensions plus one composite.

| Score | Question it answers | Type |
|-------|-------------------|------|
| **Discoverability** | Is this page being found? | Outcome |
| **SEO** | Is this page properly optimized for search? | Input |
| **Content Quality** | Is this content worth ranking? | Input |
| **Page Health** | Is this page technically sound? | Input |
| **Overall** | How does this page stack up? | Composite |

Discoverability is the outcome. SEO, Content Quality, and Page Health are inputs — the levers you can pull. Overall is the weighted composite.

### How this relates to existing frameworks

The SEO operating guide defines two manual frameworks: a Site Score (8 dimensions, 1-5, max 40) for site-wide assessment and a Content Score (7 dimensions, 1-5, max 35) for pre-publish content review. Both are subjective and manual.

This framework is different. It's automated, per-page, 0-100, and computed from tool output. It's designed for batch diagnostics — auditing hundreds of pages at once and tracking improvement over time. It complements the manual frameworks; it doesn't replace them.

### Grade scale

| Score | Grade | Meaning |
|-------|-------|---------|
| 90-100 | A | Excellent — minor polish only |
| 80-89 | B | Good — few issues to address |
| 70-79 | C | Fair — moderate fixes needed |
| 50-69 | D | Poor — significant issues |
| 0-49 | F | Critical — major work required |

---

## Score 1: Discoverability (0-100)

**Question:** Is this page being found in search?

**What it measures:** The search visibility outcome — how many keywords the page ranks for, how much traffic it gets, how strong those positions are, and whether it's gaining or losing ground.

**Why it matters:** This is the result of everything else. A page can have perfect technical health and great content, but if it's not showing up in search, something is off — either the topic is wrong, the competition is too strong, or the site lacks authority. Discoverability tells you whether the inputs are producing results.

### Data sources

| Tool | What it provides |
|------|-----------------|
| SEMRush `url_research` / `organic_research` | Keywords ranking, organic traffic, position data, 6-month trends |
| DataForSEO `dataforseo_labs_google_ranked_keywords` | Keywords, positions, search volume, SERP features (AI overview references) |

### Sub-components

All thresholds are calibrated for B2B content marketing where 50-200 organic visits/month to a targeted page is solid performance. In B2B, 10 high-intent keywords ranking is more valuable than 200 vanity terms.

#### Keyword breadth (0-25 pts)

How many organic keywords the page ranks for (any position).

| Keywords ranking | Points |
|-----------------|--------|
| 0 | 0 |
| 1-3 | 8 |
| 4-10 | 12 |
| 11-30 | 17 |
| 31-75 | 22 |
| 75+ | 25 |

**Evidence:** Pages ranking for more keywords signal stronger topical relevance — confirmed by Google's siteFocusScore and siteRadius metrics in the API leak. Semrush found text relevance appears in 90.6% of top-10 results. Broader keyword coverage indicates the page matches multiple related search intents.

#### Traffic volume (0-25 pts)

Monthly organic visits to the page.

| Monthly organic visits | Points |
|-----------------------|--------|
| 0 | 0 |
| 1-5 | 8 |
| 6-25 | 12 |
| 26-100 | 17 |
| 101-300 | 22 |
| 300+ | 25 |

**Evidence:** Traffic volume is the direct outcome of ranking well for relevant keywords. It correlates with NavBoost engagement signals — pages that get consistent traffic generate the "goodClicks" and "lastLongestClicks" that NavBoost uses to reinforce rankings (confirmed under oath in the DOJ antitrust trial). In B2B, 100+ organic visits/month to a targeted page is strong.

#### Position quality (0-25 pts)

What percentage of the page's ranking keywords are in the top 10.

| % of keywords in top 10 | Points |
|-------------------------|--------|
| 0% (no rankings) | 0 |
| 1-10% | 8 |
| 11-25% | 12 |
| 26-50% | 17 |
| 51-75% | 22 |
| 75%+ | 25 |

**Evidence:** Position quality separates pages that rank broadly (many keywords in positions 30-100) from pages that actually win clicks. The top 3 organic results capture the majority of clicks. Pages with LCP under 1.0 second rank 7.5 positions higher on average (DollarPocket, 10M results). Position quality tracks whether a page is competing or just showing up.

#### Momentum (0-25 pts)

6-month traffic trend — is the page gaining or losing ground?

| 6-month traffic change | Points |
|-----------------------|--------|
| Declining > 50% | 0 |
| Declining 10-50% | 5 |
| Stable (-10% to +10%) | 10 |
| Growing 10-50% | 15 |
| Growing 50%+ | 20 |
| New page and growing | 25 |

**Evidence:** Google's freshness signals are granular — the API leak revealed multiple attributes tracking how recently content was created, modified, and how fresh the information is. The December 2025 Core Update specifically enhanced behavioral signal weighting. Pages gaining traffic are being rewarded by the algorithm; pages losing traffic are being demoted.

### Discoverability formula

```
Discoverability = keyword_breadth + traffic_volume + position_quality + momentum
```

Sum of four sub-components. Range: 0-100.

---

## Score 2: SEO (0-100)

**Question:** Is this page properly optimized for search?

**What it measures:** On-page technical SEO — the "prerequisite" signals. You don't get bonus points for passing. You get penalized for failing.

**Why it matters:** Meta title alone accounts for ~14% of Google's algorithm weight (FirstPageSage). Crawlability is prerequisite — confirmed by the Trawler/Alexandria architecture in the API leak. Schema drives 82% higher CTR in rich results. These are the table-stakes signals that Google uses to understand what a page is about and whether it should be indexed.

### Data sources

| Tool | What it provides |
|------|-----------------|
| SquirrelScan `Core SEO` category | Title, description, canonical, h1, favicon, robots meta, OG tags, Twitter Cards |
| SquirrelScan `Crawlability` category | Sitemap inclusion, canonical chains, robots.txt compliance |
| SquirrelScan `Structured Data` category | JSON-LD presence, schema types, validation |
| SquirrelScan `URL Structure` category | URL length, hyphens, keyword signals |
| PageSpeed MCP `onpage_seo_audit` | Heading hierarchy, internal/external link ratio, image alt coverage |
| PageSpeed MCP `technical_seo_audit` | Meta tags, canonical URLs, hreflang, OG, Twitter Cards, JSON-LD |
| DataForSEO `on_page_instant_pages` | Page-specific on-page optimization data |

### Sub-components

| Component | Weight | Primary source | What it checks |
|-----------|--------|---------------|----------------|
| Core meta tags | 30% | SquirrelScan `Core SEO` score | Title present + proper length, meta description, canonical URL, h1 uniqueness, favicon, robots meta, OG tags, Twitter Cards |
| On-page structure | 25% | PageSpeed `onpage_seo_audit` | Heading hierarchy (h1 > h2 > h3), internal/external link count and ratio, image alt text coverage, keyword placement in key elements |
| Crawlability | 20% | SquirrelScan `Crawlability` score | Page in sitemap, no canonical chain issues, robots.txt not blocking, no redirect chains |
| Structured data | 15% | SquirrelScan `Structured Data` score | JSON-LD present, schema types appropriate (Article, FAQ, HowTo, Organization), valid per schema.org |
| URL structure | 10% | SquirrelScan `URL Structure` score | Reasonable length, hyphens between words, lowercase, no special characters, keyword-relevant |

### SEO formula

```
SEO = (core_meta × 0.30) + (onpage_structure × 0.25) + (crawlability × 0.20) + (structured_data × 0.15) + (url_structure × 0.10)
```

Each sub-component is on a 0-100 scale. SquirrelScan category scores are used directly (already 0-100). PageSpeed `onpage_seo_audit` results need conversion: count passed checks vs total checks, multiply by 100. DataForSEO `on_page_instant_pages` provides a direct score.

**When multiple tools provide the same signal:** Average them. If SquirrelScan gives Core SEO = 82 and PageSpeed `technical_seo_audit` gives meta tag coverage = 90, use (82 + 90) / 2 = 86 for the Core meta tags component.

### Evidence rationale for weights

- **Core meta tags (30%):** Keywords in meta title = 14% of algorithm (FirstPageSage). Anchor text provides "a valuable clue" to relevance (confirmed under oath). OG tags don't affect ranking directly but drive social traffic that feeds NavBoost engagement signals.
- **On-page structure (25%):** Heading hierarchy and internal linking reveal content architecture to both crawlers and ranking systems. Internal links are ~3% of algorithm (FirstPageSage). Clean heading structure enables BERT/RankBrain semantic understanding.
- **Crawlability (20%):** If Google can't crawl or index a page, nothing else matters. The API leak revealed Trawler (crawler) and Alexandria (indexer) as separate microservices — crawl efficiency directly impacts how quickly content enters Google's index.
- **Structured data (15%):** Not a direct ranking factor, but pages with schema markup earn rich results 82% more often (SearchPilot A/B tests). Increasingly critical for AI citation — AI systems use structured data to build accurate entity-aware summaries.
- **URL structure (10%):** Keywords in URL path show near-zero correlation with rankings (Surfer, 1M SERPs). But clean URLs are still a user experience and crawlability signal. Low weight reflects the evidence.

---

## Score 3: Content Quality (0-100)

**Question:** Is this content worth ranking?

**What it measures:** The structural signals of content quality — E-E-A-T markers, content depth, visual quality, link integrity. This maps to Google's Quality (Q*) signal.

**Why it matters:** Content quality + relevance is the single most correlated factor across every major ranking study. Semrush found text relevance in 90.6% of top-10 results. Google's Quality Rater Guidelines place Trustworthiness as "the most important member of the E-E-A-T family." The December 2025 Core Update hit sites without E-E-A-T signals hardest, with sites demonstrating experience and expertise seeing 23% gains.

**Important limitation:** Content *quality* — depth of insight, originality, expertise — cannot be fully automated. This score measures the structural signals of quality (does the page have an author? a date? sufficient depth? working links?). It does not measure whether the content is actually good. The manual Content Scoring Framework in the SEO operating guide should still be used for human evaluation of depth, originality, and voice.

### Data sources

| Tool | What it provides |
|------|-----------------|
| SquirrelScan `E-E-A-T` category | Author attribution, publish/update dates, about page links, credential signals |
| SquirrelScan `Content` category | Heading quality, word count, readability, content-to-code ratio |
| SquirrelScan `Images` category | Alt text, dimensions, next-gen formats, file sizes |
| SquirrelScan `Links` category | Broken links, anchor text quality, HTTPS link integrity |
| DataForSEO `on_page_content_parsing` | Word count, heading count, unique internal links, plain text content density |

### Sub-components

| Component | Weight | Primary source | What it checks |
|-----------|--------|---------------|----------------|
| E-E-A-T signals | 35% | SquirrelScan `E-E-A-T` score | Author byline present, publish date visible, last-updated date, about/contact page links, author bio or credentials |
| Content structure | 30% | SquirrelScan `Content` score | Heading hierarchy used effectively, sufficient word count for the topic, readable (not keyword-stuffed), good content-to-code ratio |
| Visual quality | 15% | SquirrelScan `Images` score | Images have alt text, proper dimensions declared, reasonable file sizes, next-gen formats (WebP/AVIF) |
| Link quality | 10% | SquirrelScan `Links` score | No broken outbound links, anchor text is descriptive (not "click here"), all links use HTTPS, no excessive external links |
| Content depth | 10% | DataForSEO `on_page_content_parsing` | Word count relative to topic complexity, heading density (subtopics covered), internal link count (connected to topic cluster), content density (text vs boilerplate) |

### Content Quality formula

```
Content_Quality = (eeat × 0.35) + (content_structure × 0.30) + (visual_quality × 0.15) + (link_quality × 0.10) + (content_depth × 0.10)
```

Each sub-component is on a 0-100 scale. SquirrelScan category scores are used directly.

**Content depth from DataForSEO:** Convert `on_page_content_parsing` output to a 0-100 score using these thresholds:

| Signal | Poor (0-30) | Fair (31-60) | Good (61-80) | Excellent (81-100) |
|--------|-------------|-------------|-------------|-------------------|
| Word count | < 300 | 300-800 | 800-2000 | 2000+ |
| Heading count | 0-1 | 2-4 | 5-10 | 10+ |
| Internal links | 0 | 1-3 | 4-10 | 10+ |
| Content density (text/total) | < 20% | 20-40% | 40-60% | 60%+ |

Average the four signal scores to get the content depth sub-component.

### Evidence rationale for weights

- **E-E-A-T signals (35%):** Google's Quality Rater Guidelines call Trustworthiness "the most important member of the E-E-A-T family." After the December 2025 Core Update, sites demonstrating experience and expertise gained 23%. 96% of AI Overview citations come from verified authoritative sources. Author attribution and dates are the most measurable proxies for trust.
- **Content structure (30%):** Content comprehensiveness showed moderate positive correlation with rankings (Surfer, 1M SERPs). Consistent publication of satisfying content is the #1 factor for 7+ years (FirstPageSage, ~23% weight). Good heading structure enables semantic understanding.
- **Visual quality (15%):** Multi-modal content (text + images + video + structured data) sees 156% higher AI Overview selection rates (r=0.92, Surfer 36M AI Overviews). Images with proper alt text serve both accessibility and SEO.
- **Link quality (10%):** Internal linking is ~3% of algorithm weight (FirstPageSage). Broken outbound links signal neglect and hurt user experience — feeding negative NavBoost signals.
- **Content depth (10%):** HireGrowth (2025) found content grouped into topic clusters drives ~30% more organic traffic. Word count alone doesn't matter, but depth relative to topic complexity is a proxy for comprehensiveness.

---

## Score 4: Page Health (0-100)

**Question:** Is this page technically sound?

**What it measures:** Performance, accessibility, security, and mobile-friendliness. This maps to Google's "page experience" factor — 28% of algorithm weight (DollarPocket) and the fastest-growing category.

**Why it matters:** Pages with LCP under 1.0 second rank 7.5 positions higher on average than those over 4.0 seconds. Mobile page speed shows r=0.83 correlation with rankings (DollarPocket). Only 44% of WordPress sites pass all Core Web Vitals on mobile — which means fixing performance creates real competitive advantage. HTTPS is a confirmed ranking signal since 2014. Accessibility is a prerequisite that correlates with broader code quality and user experience.

### Data sources

| Tool | What it provides |
|------|-----------------|
| PageSpeed MCP `performance_audit` / `run_pagespeed_test` | Lighthouse performance score, Core Web Vitals (LCP, TBT, CLS, FCP, SI, TTI) |
| DataForSEO `on_page_lighthouse` | Lighthouse scores for performance, accessibility, best practices, SEO |
| a11y MCP `audit_webpage` | axe-core accessibility violations with severity and affected elements |
| SquirrelScan `Performance` category | Page weight, JS size, caching, CLS hints, LCP hints, render-blocking resources |
| SquirrelScan `Accessibility` category | ARIA labels, focus management, landmarks, skip links, heading order |
| SquirrelScan `Security` category | HTTPS, CSP, HSTS, X-Frame-Options, leaked secrets, noopener |
| PageSpeed MCP `security_headers_audit` | HTTPS status, security header presence and configuration |
| PageSpeed MCP `mobile_audit` | Viewport, tap targets, font sizes, responsive images, PWA readiness |

### Sub-components

| Component | Weight | Primary source(s) | What it checks |
|-----------|--------|-------------------|----------------|
| Performance / CWV | 40% | Lighthouse performance score | LCP (< 2.5s good), TBT/INP (< 200ms good), CLS (< 0.1 good), FCP, Speed Index, TTI |
| Accessibility | 25% | Lighthouse a11y score + a11y MCP | ARIA attributes, color contrast, link/button names, heading order, landmarks, tap targets |
| Security | 15% | SquirrelScan `Security` score | HTTPS enforced, CSP header present, HSTS enabled, X-Frame-Options set, no leaked secrets, rel=noopener on external links |
| Mobile | 10% | PageSpeed `mobile_audit` | Viewport configured, tap targets sized correctly, fonts readable, content fits viewport, responsive images |
| Best practices | 10% | Lighthouse best-practices score | No deprecated APIs, no console errors, HTTPS used for all resources, source maps available |

### Page Health formula

```
Page_Health = (performance × 0.40) + (accessibility × 0.25) + (security × 0.15) + (mobile × 0.10) + (best_practices × 0.10)
```

Each sub-component is on a 0-100 scale.

**When multiple tools provide the same signal:** Use the approach most appropriate to the context:

- **Performance:** Average Lighthouse score from PageSpeed and DataForSEO runs. If only one is available, use it. If SquirrelScan Performance is also available, use it as a tiebreaker (it measures different things — page weight and resource optimization rather than load timing).
- **Accessibility:** Average of Lighthouse a11y score and a11y MCP violation-based score. For a11y MCP, convert violation count to a score: 0 violations = 100, 1-3 = 80, 4-8 = 60, 9-15 = 40, 16+ = 20. Weight critical violations 2x.
- **Security:** Use SquirrelScan Security score directly. Cross-reference with PageSpeed `security_headers_audit` — if they disagree significantly (> 20 points), investigate and use the lower score (security should be conservative).

### Core Web Vitals reference thresholds

These are Google's official thresholds. Pages meeting "Good" on all three are considered passing.

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | < 2.5s | 2.5-4.0s | > 4.0s |
| INP (Interaction to Next Paint) | < 200ms | 200-500ms | > 500ms |
| CLS (Cumulative Layout Shift) | < 0.1 | 0.1-0.25 | > 0.25 |

Note: Lighthouse lab tests report TBT (Total Blocking Time) as a proxy for INP, since INP requires real user data (CrUX). TBT < 200ms approximates good INP.

### Evidence rationale for weights

- **Performance / CWV (40%):** Mobile page speed shows r=0.83 correlation with rankings (DollarPocket, 10M results). LCP < 1.0s = 7.5 position advantage. Page experience signals are 28% of algorithm weight and the fastest-growing category. Rakuten saw 53% revenue per visitor increase after CWV optimization.
- **Accessibility (25%):** Lighthouse a11y is part of Google's page experience evaluation. WCAG compliance correlates with broader code quality. Touch targets, contrast ratios, and ARIA labels directly affect mobile user experience — and mobile is 58% of web traffic. Increasingly required for legal compliance.
- **Security (15%):** HTTPS is a confirmed ranking signal (Google, 2014). CSP and HSTS affect trust evaluation — the leaked API docs show Google evaluates technical integrity as part of page quality. Leaked API keys and missing security headers are red flags that affect E-E-A-T trustworthiness assessment.
- **Mobile (10%):** Mobile-first indexing is fully established. Google primarily uses the mobile version for indexing and ranking. Mobile-friendliness is ~5% of algorithm weight (FirstPageSage). This is a prerequisite — you get penalized for failing, not rewarded for passing.
- **Best practices (10%):** Deprecated APIs, console errors, and third-party cookie issues don't directly affect rankings but signal code quality and maintenance. They also affect user experience, which feeds NavBoost signals.

---

## Score 5: Overall (0-100)

**Question:** How does this page stack up across all dimensions?

**What it measures:** Weighted composite of the four diagnostic scores.

### Overall formula

```
Overall = (Content_Quality × 0.30) + (Page_Health × 0.25) + (SEO × 0.25) + (Discoverability × 0.20)
```

### Weight rationale

| Score | Weight | Why |
|-------|--------|-----|
| Content Quality | 30% | Universally the #1 factor across every study. Content quality + relevance = ~25% of algorithm (DollarPocket). E-E-A-T is the quality framework Google operationalizes. |
| Page Health | 25% | Page experience signals = 28% of algorithm (DollarPocket, fastest growing). Performance is the tiebreaker in competitive SERPs. |
| SEO | 25% | On-page optimization is prerequisite. Meta title = 14% of algorithm. Crawlability gates everything else. |
| Discoverability | 20% | Outcome metric, not input. Influenced by external factors (backlinks, brand, competition) that page-level tools can't measure. Lower weight reflects that this score is partially dependent on forces outside the page itself. |

---

## Tool-to-Score Mapping

Complete reference showing which tool feeds which score component.

| Tool | Discoverability | SEO | Content Quality | Page Health |
|------|:-:|:-:|:-:|:-:|
| **SEMRush** url/organic research | Keywords, traffic, positions, trends | — | — | — |
| **DataForSEO** ranked_keywords | Keywords, positions, SERP features | — | — | — |
| **DataForSEO** on_page_instant_pages | — | On-page optimization checks | — | — |
| **DataForSEO** on_page_content_parsing | — | — | Word count, headings, links, density | — |
| **DataForSEO** on_page_lighthouse | — | — | — | Performance, a11y, best practices |
| **PageSpeed** performance_audit | — | — | — | CWV, performance score |
| **PageSpeed** technical_seo_audit | — | Meta, canonical, schema, hreflang | — | — |
| **PageSpeed** onpage_seo_audit | — | Headings, links, images, keyword | — | — |
| **PageSpeed** security_headers_audit | — | — | — | Security headers |
| **PageSpeed** mobile_audit | — | — | — | Mobile-friendliness |
| **a11y** audit_webpage | — | — | — | Accessibility violations |
| **SquirrelScan** Core SEO | — | Meta tags, canonical, h1, OG | — | — |
| **SquirrelScan** Content | — | — | Content structure, word count | — |
| **SquirrelScan** E-E-A-T | — | — | Author, dates, trust signals | — |
| **SquirrelScan** Images | — | — | Alt text, formats, sizes | — |
| **SquirrelScan** Links | — | — | Broken links, anchors | — |
| **SquirrelScan** Performance | — | — | — | Page weight, JS, caching |
| **SquirrelScan** Accessibility | — | — | — | ARIA, focus, landmarks |
| **SquirrelScan** Security | — | — | — | HTTPS, CSP, HSTS |
| **SquirrelScan** Crawlability | — | Sitemap, canonical chains | — | — |
| **SquirrelScan** Structured Data | — | JSON-LD, schema validation | — | — |
| **SquirrelScan** URL Structure | — | URL format, length | — | — |

---

## Handling Missing Data

Not every tool will be run on every page. The framework degrades gracefully:

| Available tools | How to score |
|----------------|-------------|
| All tools | Full methodology as described above |
| SquirrelScan + SEMRush only | SEO uses SquirrelScan categories directly. Content Quality uses SquirrelScan. Page Health uses SquirrelScan Performance + Accessibility + Security (no Lighthouse data — label as "partial"). Discoverability uses SEMRush. |
| Lighthouse + SEMRush only | Page Health uses Lighthouse scores directly. SEO uses Lighthouse SEO score (note: this is narrower than SquirrelScan). Content Quality = Lighthouse SEO score as a rough proxy (label as "partial"). Discoverability uses SEMRush. |
| SEMRush only | Only Discoverability can be computed. Other scores marked "not available." |

When data is partial, mark the affected scores with a `(partial)` flag and note which tools were missing.

---

## Interpreting Scores in Practice

### The diagnostic pattern

The relationship between scores tells a story:

- **High SEO + High Content + High Health + Low Discoverability:** The page is well-built but not being found. Problem is likely external — weak backlinks, low domain authority, or strong competition. Investigate backlink profile and topical authority at the site level.
- **High Discoverability + Low Content + Low Health:** The page ranks despite itself — likely on the strength of domain authority or topic monopoly. Fixing Content and Health will compound the existing ranking advantage.
- **Low SEO + Everything else OK:** Quick wins. Fix meta tags, canonical issues, and structured data. Fastest path to improvement.
- **Low Health + Everything else OK:** Template-level issues. Fixing performance and security headers lifts every page on the site. Highest leverage for sites with many content pages.
- **Everything low:** Start with Page Health (Layer 1 in the four-layer stack), then SEO (Layer 2). Don't invest in content quality until the foundation is solid.

### Score comparisons across pages

When comparing pages on the same site, the most useful views:

- **Rank by Overall, investigate outliers.** Pages scoring 20+ points above or below the site average reveal either templates behaving differently or content quality variation.
- **Sort by Discoverability descending.** Your highest-traffic pages should also be your highest-quality. If top-traffic pages have low Content Quality, they're vulnerable to the next core update.
- **Sort by Page Health ascending.** The lowest health scores reveal infrastructure problems. If they cluster (most pages score 40-45), it's a template issue. If they vary widely, it's page-specific.

---

## Calibration Notes

### B2B-specific thresholds

The Discoverability thresholds are calibrated for B2B content marketing where:

- 50-200 organic visits/month to a targeted page is solid
- 10-30 ranking keywords on a niche topic is healthy
- Top-10 positioning on 25%+ of keywords is strong
- Steady growth matters more than explosive gains

For consumer/ecommerce sites with higher traffic baselines, adjust the Discoverability thresholds upward (roughly 3-5x).

### Tool variance

Lighthouse scores vary between runs (especially performance). DataForSEO and PageSpeed MCP can return different performance scores for the same URL because they run Lighthouse from different infrastructure. When both are available, average them. When tracking over time, use the same tool consistently.

SquirrelScan scores are more stable across runs because they're primarily checking for the presence/absence of elements rather than measuring load timing.

### What this framework cannot measure

- **Content originality and depth of insight** — requires human judgment. Use the manual Content Scoring Framework.
- **Backlink profile** — a site-level signal, not page-level. Use the Site Scoring Framework's Dimension 4.
- **User engagement (NavBoost signals)** — click data, dwell time, and pogo-sticking aren't available through these tools. Use Google Analytics and GSC data separately.
- **Brand signals and entity strength** — site-level. Use the Site Scoring Framework's Dimension 6.
- **AI citation presence** — requires checking ChatGPT, Perplexity, and AI Overviews manually. Use the Site Scoring Framework's Dimension 7.
- **Topical authority** — a site-level signal dependent on content architecture across many pages. Use Topic Share analysis from SEMRush/Ahrefs.
