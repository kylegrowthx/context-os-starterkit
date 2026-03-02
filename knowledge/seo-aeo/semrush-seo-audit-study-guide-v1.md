# Comprehensive SEO Audit Using SEMRush: Study Guide

> **For:** GrowthX team members running SEO audits on client domains
> **Goal:** Execute a full-scope SEO audit using SEMRush's app and API, surface actionable findings, and deliver client-ready recommendations
> **Time Investment:** 8-12 hours to learn, 4-8 hours per audit once proficient
> **Last Updated:** 2026-02-26

---

## How to Use This Guide

This guide walks through every phase of a comprehensive SEO audit using SEMRush. Each section covers the "what and why," the SEMRush app workflow, and the equivalent API call. You don't need to memorize the API endpoints — use this as a reference when building automation or pulling data programmatically.

Work through Parts 1-6 in order for your first audit. After that, you'll develop your own rhythm and can skip around.

---

## Part 1: Foundations — What a Comprehensive SEO Audit Actually Covers

A comprehensive SEO audit examines everything that affects a domain's organic search performance. It's not a checklist exercise — it's a diagnostic process that connects technical health, content quality, backlink authority, and competitive positioning into a single picture of where a domain stands and what to fix first.

### The 7 Pillars of a Full SEO Audit

1. **Technical SEO** — Can search engines crawl and index the site efficiently? Are there structural problems (broken links, redirect chains, duplicate content, slow pages)?
2. **Core Web Vitals & Performance** — Does the site meet Google's page experience signals? LCP under 2.5s, INP under 200ms, CLS under 0.1.
3. **On-Page Optimization** — Are title tags, meta descriptions, headers, and content properly optimized for target keywords and search intent?
4. **Content Quality & Gaps** — Is the content comprehensive, fresh, and aligned with what the audience is searching for? What topics are competitors covering that you're not?
5. **Backlink Profile** — Is the link profile healthy? Are there toxic links to disavow? How does it compare to competitors?
6. **Competitor Benchmarking** — Where do competitors outperform the domain? What keyword and content gaps exist?
7. **AI Visibility (2026 addition)** — Is the site structured for AI engines? Does it have llms.txt, proper structured data, and authority signals that AI models can interpret?

### SEMRush Tools Mapped to Each Pillar

| Audit Pillar | SEMRush App Tool | API Equivalent |
|---|---|---|
| Technical SEO | Site Audit | Projects API → Site Audit |
| Core Web Vitals | Site Audit → Core Web Vitals report | Projects API → Site Audit |
| On-Page | On Page SEO Checker | N/A (app only) |
| Content & Keywords | Keyword Gap, Organic Research, Content Audit | Analytics API → Domain Reports, Keyword Reports |
| Backlinks | Backlink Audit, Backlink Analytics | Analytics API → Backlinks |
| Competitors | Domain Overview, Traffic Analytics, Organic Research Competitors | Analytics API → Domain Reports, Overview Reports |
| AI Visibility | Manual checks + structured data validation | N/A |

### Common Misconceptions

**"An SEO audit is a one-time thing."** Wrong. Audits should run quarterly at minimum. SEMRush lets you schedule recurring crawls so you catch new issues before they compound.

**"Just fix all the errors."** Not all errors matter equally. A single orphaned high-traffic page costs more than 50 missing alt tags. Prioritize by business impact, not issue count.

**"The Site Health Score is the audit."** The Site Health Score is a starting point. A real audit connects technical findings to keyword rankings, traffic trends, and revenue impact. The score alone tells you nothing about content gaps or competitive positioning.

---

## Part 2: Setting Up and Running the Technical Audit

### Step 1: Create the Project

Every audit in SEMRush starts with a project. One project per domain.

**In the app:**
1. Log into SEMRush → Dashboard → "Create Project"
2. Enter the domain (without www)
3. Name the project (use the client name + domain for easy identification)

**Via API:**
```
POST https://api.semrush.com/management/v1/projects
Headers: Authorization: Bearer {API_KEY}
Body: { "url": "example.com", "name": "ClientName - example.com" }
```

### Step 2: Configure the Site Audit Crawl

Configuration matters. Default settings miss things.

**In the app:** Navigate to Site Audit → Settings and configure:

| Setting | Recommended Value | Why |
|---|---|---|
| Scope | Root domain (include all subdomains) | Catches subdomain issues (blog.example.com, shop.example.com) |
| Crawl source | Website (breadth-first) | Mimics how Googlebot discovers pages |
| Page limit | Maximum allowed by your plan | You want full coverage |
| User agent | SiteAuditBot-Mobile | Google uses mobile-first indexing |
| Crawl delay | Minimum delay between pages | Faster crawl, more complete data |
| Disallow | Exclude staging/dev subdomains | Don't crawl non-production environments |

**Also configure:**
- Connect Google Analytics and Google Search Console for richer data
- Enable JavaScript rendering if the site is a SPA or uses heavy client-side rendering
- Set up scheduled re-crawls (weekly recommended)

**Via API — Enable Site Audit for a project:**
```
POST https://api.semrush.com/projects/{project_id}/siteaudit/enable
```

Then configure and launch the crawl through the Site Audit management endpoints.

### Step 3: Read the Results

When the crawl finishes, you get a Site Health Score (0-100%) based on the ratio of errors, warnings, and notices to total checks performed. Errors carry the most weight.

**Key thematic reports to review (in order of priority):**

1. **Crawlability** — Pages blocked by robots.txt, noindex issues, orphan pages, redirect chains and loops, 4xx/5xx errors
2. **HTTPS** — Mixed content, insecure pages, certificate issues
3. **Core Web Vitals** — LCP, INP, CLS scores with specific page-level data
4. **Site Performance** — Page load times, large files, uncompressed resources, render-blocking scripts
5. **Internal Linking** — Broken internal links, pages with too few internal links, link depth issues
6. **Markup** — Missing or broken structured data, Open Graph tags, hreflang issues
7. **International SEO** — hreflang conflicts, language targeting issues (if applicable)

**New in 2025-2026:** SEMRush now includes AI Fix Suggestions that propose line-level code edits, and a Server-Side Rendering (SSR) detector that flags pages relying on client-side JavaScript rendering.

### Prioritization Framework

Don't hand the client a list of 200 issues. Categorize them:

| Priority | Criteria | Examples |
|---|---|---|
| P0 — Fix immediately | Blocks indexing or causes significant traffic loss | Noindex on key pages, 5xx errors, redirect loops |
| P1 — Fix this week | Degrades ranking or user experience | Slow LCP, missing canonical tags, duplicate content |
| P2 — Fix this month | Optimization opportunities | Missing alt tags, thin meta descriptions, internal linking gaps |
| P3 — Backlog | Low impact, nice-to-have | Minor HTML validation issues, HTTP links in non-critical resources |

---

## Part 3: On-Page Optimization & Content Analysis

### On-Page SEO Checker

The On Page SEO Checker analyzes your pages against top-ranking competitors for each target keyword and gives specific recommendations.

**In the app:**
1. Set up On Page SEO Checker in your project
2. Import target keywords (from Position Tracking or manual entry)
3. Review recommendations per page: content length, keyword usage, semantic terms, readability, technical elements, backlink suggestions

**What it checks per page:**
- Strategy ideas (keyword targeting, SERP feature opportunities)
- Content ideas (word count, readability, TF-IDF terms to add)
- Semantic ideas (related keywords to include)
- Backlink ideas (pages linking to competitors but not you)
- Technical ideas (page speed, structured data)
- UX ideas (layout, readability)

### Content Audit

**In the app:** Content Audit tool → connect Google Analytics + Search Console → SEMRush categorizes all your content by performance.

Content gets bucketed into:
- **Rewrite or remove** — Low traffic, low engagement, outdated
- **Need to update** — Declining traffic, stale content, missing keywords
- **Quick review** — Moderate performance, small tweaks needed
- **Poor content** — Thin pages (under 250 words) that dilute site authority

### Keyword Gap Analysis

This is where you find the money. Keyword Gap shows you what competitors rank for that you don't.

**In the app:**
1. Go to Competitive Research → Keyword Gap
2. Enter your domain + up to 4 competitors
3. Click Compare
4. Focus on the "Missing" and "Weak" tabs

**Missing** = competitors rank, you don't. **Weak** = competitors rank higher than you.

**Via API — Domain Organic Search Keywords:**
```
GET https://api.semrush.com/analytics/v1/?type=domain_organic
    &key={API_KEY}
    &display_limit=100
    &export_columns=Ph,Po,Nq,Cp,Ur,Tr
    &domain=example.com
    &database=us
```

Key columns: Ph (keyword phrase), Po (position), Nq (search volume), Cp (CPC), Ur (URL), Tr (traffic estimate).

To compare two domains programmatically, pull organic keywords for both domains and diff the keyword sets in your own code.

### Position Tracking

Set up Position Tracking to monitor how the client's rankings change after audit fixes are implemented.

**In the app:** Projects → Position Tracking → Add keywords → Choose location and device type → Enable daily tracking.

**Via API:**
```
POST https://api.semrush.com/projects/{project_id}/tracking/keywords/add
Body: { "keywords": ["keyword1", "keyword2"], "location": "US", "device": "desktop" }
```

Then pull ranking data:
```
GET https://api.semrush.com/projects/{project_id}/tracking/keywords
```

---

## Part 4: Backlink Audit & Off-Page Analysis

### Running the Backlink Audit

Toxic backlinks can tank rankings. The Backlink Audit tool identifies them.

**In the app:**
1. Set up Backlink Audit in your project
2. Connect Google Search Console (gives the most complete backlink data)
3. Wait for the audit to complete
4. Review the Toxicity Score breakdown

**Toxicity Score:** 0-100 scale. Focus on links scoring 60+ first.

SEMRush uses 45+ toxic markers including: links from spammy sites, non-indexed sites, sites with malware, link networks, excessive reciprocal links, and suspicious anchor text patterns.

**Action workflow:**
1. Filter for Toxicity Score ≥ 60
2. Review each flagged link manually (not everything flagged is actually toxic)
3. Add confirmed toxic links to the Remove List (for manual outreach to webmasters)
4. Add unresponsive/impossible-to-remove links to the Disavow List
5. Export the disavow file and submit to Google Search Console

### Backlink Analytics (Broader Analysis)

Beyond toxicity, you need to understand the overall link profile.

**In the app:** Backlink Analytics → enter domain → review:
- Total backlinks and referring domains (trend over time)
- New vs. lost links (are you gaining or losing authority?)
- Anchor text distribution (should look natural, not over-optimized)
- Link types (follow vs. nofollow, text vs. image)
- TLD and country distribution
- Referring domain authority scores

**Via API — Backlinks Overview:**
```
GET https://api.semrush.com/analytics/v1/?type=backlinks_overview
    &key={API_KEY}
    &target=example.com
    &target_type=root_domain
```

Default response columns: total backlinks, referring domains, referring IPs, follow/nofollow count, authority score, trust score.

**Via API — Referring Domains:**
```
GET https://api.semrush.com/analytics/v1/?type=backlinks_refdomains
    &key={API_KEY}
    &target=example.com
    &target_type=root_domain
    &display_limit=100
```

**Via API — Anchors:**
```
GET https://api.semrush.com/analytics/v1/?type=backlinks_anchors
    &key={API_KEY}
    &target=example.com
    &target_type=root_domain
```

### Competitor Backlink Comparison

**In the app:** Backlink Gap tool → enter your domain + competitors → see which domains link to competitors but not you. These are your highest-probability outreach targets.

---

## Part 5: Competitor Benchmarking

### Domain Overview

Start every competitor analysis here. Domain Overview gives you a snapshot of any domain's organic and paid performance.

**In the app:** Enter a competitor domain → see organic keywords, traffic, backlinks, top pages, traffic trend.

**Via API — Domain Overview:**
```
GET https://api.semrush.com/analytics/v1/?type=domain_rank
    &key={API_KEY}
    &export_columns=Dn,Rk,Or,Ot,Os,OC,Ad,At,Ac
    &domain=competitor.com
    &database=us
```

Columns: Dn (domain), Rk (SEMRush rank), Or (organic keywords), Ot (organic traffic), Os (organic cost), Ad (paid keywords), At (paid traffic).

### Organic Research — Competitors Report

**In the app:** Organic Research → Competitors tab → lists all domains competing for the same keywords, ranked by competition level and common keywords.

**Via API:**
```
GET https://api.semrush.com/analytics/v1/?type=domain_organic_organic
    &key={API_KEY}
    &display_limit=20
    &export_columns=Dn,Cr,Np,Or,Ot,Os,OC
    &domain=example.com
    &database=us
```

### Traffic Analytics

Traffic Analytics goes beyond SEO data. It estimates total traffic (organic, paid, social, referral, direct), engagement metrics, audience overlap, and traffic journey.

**In the app:** Traffic Analytics → enter up to 5 domains → compare side by side.

This data is available via the Trends API (separate from the standard Analytics API, requires Trends subscription).

### Building the Competitive Picture

For each top 3-5 competitors, document:
1. Domain authority and trust score
2. Total organic keywords and estimated traffic
3. Top 10 performing pages (what content drives their traffic?)
4. Keyword gaps (what do they rank for that you don't?)
5. Backlink advantages (who links to them but not you?)
6. Content format patterns (do they use guides? tools? calculators?)

This gives the client a clear "here's where you stand and here's the gap to close" narrative.

---

## Part 6: The SEMRush API — Reference Guide

### Getting Access

The API requires a Business-tier SEO Toolkit subscription. After subscribing:
1. Go to Subscription Info → API Units
2. Generate your API key
3. Store it securely (treat it like a password)

### Authentication

All requests include your API key as a query parameter (`key={API_KEY}`) for v3, or as a Bearer token in the Authorization header for v4.

### Rate Limits

| Limit | Value |
|---|---|
| Requests per second | 10 |
| Concurrent requests | 10 |
| Default monthly requests | 10,000 (can purchase more) |

### API Unit Costs

Requests cost "units" based on report type and data freshness:
- Live data: ~10 units per line of response
- Historical data: ~50 units per line
- Plan unit costs accordingly when pulling large datasets

### Response Format

All v3 Analytics API endpoints return CSV. Parse accordingly in your scripts.

### Key API Families

**Analytics API (data retrieval):**

| Report Family | What You Get |
|---|---|
| Domain Reports | Organic keywords, paid keywords, competitors, ranking history |
| Keyword Reports | Volume, CPC, competition, SERP features, related keywords |
| Backlinks Reports | Overview, referring domains, anchors, TLD distribution, historical data |
| Overview Reports | Domain summary (organic + paid snapshot) |
| URL Reports | Page-level keyword and backlink data |
| Subfolder Reports | Section-level analysis |

**Projects API (campaign management):**

| Endpoint Family | What You Can Do |
|---|---|
| Projects | Create, list, update, delete projects |
| Site Audit | Enable, configure, launch crawls, pull audit reports |
| Position Tracking | Create campaigns, add keywords, pull ranking data |

### Useful Endpoint Quick Reference

```
# Domain organic keywords
GET /analytics/v1/?type=domain_organic&domain={domain}&database={db}

# Domain paid keywords
GET /analytics/v1/?type=domain_adwords&domain={domain}&database={db}

# Domain organic competitors
GET /analytics/v1/?type=domain_organic_organic&domain={domain}&database={db}

# Keyword overview
GET /analytics/v1/?type=phrase_all&phrase={keyword}&database={db}

# Backlinks overview
GET /analytics/v1/?type=backlinks_overview&target={domain}&target_type=root_domain

# Backlinks referring domains
GET /analytics/v1/?type=backlinks_refdomains&target={domain}&target_type=root_domain

# Backlinks anchors
GET /analytics/v1/?type=backlinks_anchors&target={domain}&target_type=root_domain

# List projects
GET /management/v1/projects

# Position tracking keywords
GET /projects/{id}/tracking/keywords
```

All base URL: `https://api.semrush.com`

### When to Use API vs. App

| Scenario | Use |
|---|---|
| One-off client audit | App — faster, visual, easy to screenshot |
| Recurring audits across 10+ clients | API — automate data pulls, build dashboards |
| Client reporting with custom formatting | API → pipe to Google Sheets, Looker, or custom reports |
| Exploring a new domain quickly | App — Domain Overview gives you everything in 30 seconds |
| Historical trend analysis | API — pull monthly data going back years |
| Backlink toxicity review | App — the manual review workflow needs the UI |
| Keyword gap analysis at scale | API — compare programmatically across many domains |

---

## Part 7: Putting It All Together — The GrowthX Audit Workflow

Here's the recommended sequence for running a client audit:

### Phase 1: Discovery (Day 1)
1. Run Domain Overview on client domain + 3-5 competitors (app)
2. Pull organic keyword and traffic snapshots via API for historical context
3. Set up the project and configure Site Audit crawl
4. Launch the crawl

### Phase 2: Technical Audit (Day 2-3)
5. Review Site Audit results — prioritize P0 and P1 issues
6. Check Core Web Vitals report
7. Review crawlability and indexing issues
8. Document findings with screenshots

### Phase 3: Content & On-Page (Day 3-4)
9. Run On Page SEO Checker for top landing pages
10. Execute Keyword Gap analysis vs. top 3 competitors
11. Run Content Audit to identify pages to update, consolidate, or remove
12. Document content opportunities

### Phase 4: Backlinks (Day 4-5)
13. Run Backlink Audit — flag toxic links
14. Analyze overall backlink profile health and trends
15. Run Backlink Gap vs. competitors
16. Identify high-value outreach targets

### Phase 5: Competitive Analysis (Day 5)
17. Compile competitor benchmarks (traffic, keywords, backlinks, content)
18. Identify competitor content formats and strategies worth emulating
19. Map the competitive gap with specific recommendations

### Phase 6: Synthesis & Recommendations (Day 6-7)
20. Prioritize all findings using the P0-P3 framework
21. Group recommendations by implementation team (dev, content, outreach)
22. Estimate impact and effort for each recommendation
23. Build the client deliverable

### Post-Audit
24. Set up Position Tracking for target keywords
25. Schedule recurring Site Audit crawls (weekly)
26. Establish a monthly check-in cadence to track progress

---

## Appendix A: Curated Source Library

### Official SEMRush Resources
- [SEMRush Site Audit Configuration Guide](https://www.semrush.com/kb/539-configuring-site-audit) — How to configure crawl settings
- [SEMRush Blog: How to Perform a Complete SEO Audit in 17 Steps](https://www.semrush.com/blog/seo-audit/) — Their own step-by-step guide
- [SEMRush Blog: Complete SEO Audit Template (Free PDF)](https://www.semrush.com/blog/ultimate-site-audit-with-semrush-free-pdf/) — Downloadable audit template
- [SEMRush Knowledge Base: How Site Audit Works](https://www.semrush.com/kb/31-site-audit) — Technical docs on the crawl engine
- [SEMRush Knowledge Base: Backlink Audit Overview](https://www.semrush.com/kb/1090-backlink-audit-overview) — How toxicity scoring works
- [SEMRush Knowledge Base: Toxic Markers Explained](https://www.semrush.com/kb/965-toxic-markers-description) — All 45+ toxic markers defined
- [SEMRush Knowledge Base: Keyword Gap](https://www.semrush.com/kb/28-keyword-gap) — How to use the keyword gap tool
- [SEMRush Knowledge Base: Site Audit Thematic Reports](https://www.semrush.com/kb/959-site-audit-thematic-reports) — Breakdown of each report type

### SEMRush API Documentation
- [SEMRush API Introduction](https://developer.semrush.com/api/basics/introduction/) — Getting started, auth, rate limits
- [Domain Reports API](https://developer.semrush.com/api/v3/analytics/domain-reports/) — All domain-level endpoints
- [Backlinks API](https://developer.semrush.com/api/v3/analytics/backlinks/) — All backlink endpoints
- [Keyword Reports API](https://developer.semrush.com/api/v3/analytics/keyword-reports/) — Keyword data endpoints
- [Projects API](https://developer.semrush.com/api/v3/projects/projects/) — Project management endpoints
- [Site Audit API](https://developer.semrush.com/api/v3/projects/site-audit/) — Site Audit campaign endpoints
- [Position Tracking API](https://developer.semrush.com/api/v3/projects/position-tracking/) — Rank tracking endpoints
- [API FAQ](https://developer.semrush.com/api/basics/faq/) — Common questions and troubleshooting

### SEMRush Academy (Free Courses)
- [SEO Toolkit Crash Course](https://www.semrush.com/academy/courses/seo-toolkit-crash-course/) — Hands-on tool walkthroughs
- [Technical SEO and AI Search Essentials](https://www.semrush.com/academy/courses/techincal-seo-and-ai-search-essentials-with-semrush/) — Technical audit + AI visibility
- [Beginner SEO with Semrush](https://www.semrush.com/academy/courses/seo-essentials-with-semrush/) — Fundamentals if anyone needs a refresher
- [All Free SEO Courses](https://www.semrush.com/academy/courses/seo/) — Full course catalog

### Expert Practitioner Resources
- [Aleyda Solis: How to Develop Actionable SEO Audits (SP2 Framework)](https://www.aleydasolis.com/en/search-engine-optimization/how-to-winning-seo-website-audit-growth/) — The gold standard for audit methodology
- [LearningSEO.io: SEO Audits & Recommendations](https://learningseo.io/seo_roadmap/execute-seo/seo-audits-recommendations/) — Curated free guides, templates, and tools (also by Aleyda)
- [Backlinko: 18-Step SEO Audit Checklist](https://backlinko.com/seo-site-audit) — Brian Dean's checklist with downloadable template
- [Single Grain: Semrush Site Audit Step-by-Step 2026 Guide](https://www.singlegrain.com/blog/semrush-site-audit/) — Detailed walkthrough with screenshots

### Supplemental Guides
- [99signals: Quick SEO Audit with Semrush](https://www.99signals.com/seo-audit-semrush/) — Streamlined walkthrough
- [Search Engine Land: SEO Gap Analysis Guide](https://searchengineland.com/guide/gap-analysis) — Keyword and content gap methodology
- [SEMRush Blog: Content Gap Analysis Step-by-Step](https://www.semrush.com/blog/content-gap-analysis/) — Content-specific gap analysis
- [SEMRush Blog: Technical SEO Audit in 10 Steps](https://www.semrush.com/blog/technical-seo-audit/) — Technical-focused deep dive

---

## Appendix B: Key Frameworks

### Aleyda Solis' SP2 Audit Framework

The most respected audit methodology in the industry. An effective audit is:

- **Context Aware** — considers the site's business model and technical stack
- **Goal Oriented** — validates how each issue impacts revenue and rankings vs. competitors
- **Solutions Focused** — describes the root cause and specific steps to fix
- **Resource Specific** — includes estimated effort and who needs to implement
- **Prioritized** — orders recommendations by impact × difficulty
- **Concise** — fast to develop, easy to understand, scannable by stakeholders
- **Preventive** — establishes monitoring to catch issues before they recur

The key insight: the best audits don't just list problems. They function as project plans with clear ownership, timelines, and success metrics.

### The P0-P3 Prioritization Matrix

| Priority | Impact | Effort | Action |
|---|---|---|---|
| P0 | High | Any | Fix immediately — blocking revenue/indexing |
| P1 | High | Low-Medium | Fix this sprint — quick wins with outsized impact |
| P2 | Medium | Medium | Schedule this month — optimization improvements |
| P3 | Low | Any | Backlog — address when capacity allows |

### The 7-Day Audit Timeline

| Day | Phase | Activities |
|---|---|---|
| 1 | Discovery | Domain overview, competitor identification, crawl setup |
| 2-3 | Technical | Site Audit review, Core Web Vitals, crawlability |
| 3-4 | Content | On-page checker, keyword gaps, content audit |
| 4-5 | Backlinks | Toxicity audit, profile analysis, competitor gap |
| 5 | Competition | Full competitive benchmarking |
| 6-7 | Synthesis | Prioritize, document, build deliverable |

---

## Appendix C: Learning Path

### Week 1: Get Comfortable with the Tools
1. Complete the [SEO Toolkit Crash Course](https://www.semrush.com/academy/courses/seo-toolkit-crash-course/) on SEMRush Academy (free, ~2 hours)
2. Run a Site Audit on growthxlabs.com or a test domain
3. Explore every thematic report — click through each one

### Week 2: Run a Practice Audit
4. Pick a real client domain (or a prospect)
5. Follow the Phase 1-6 workflow in Part 7 of this guide
6. Document everything — practice building the deliverable

### Week 3: Learn the API
7. Generate your API key
8. Make your first API call (Domain Overview is the easiest starting point)
9. Build a simple script that pulls organic keywords for a domain
10. Compare the API output to what you see in the app

### Week 4: Build Speed and Judgment
11. Run a second full audit — aim to cut your time by 30%
12. Read Aleyda Solis' [SP2 framework article](https://www.aleydasolis.com/en/search-engine-optimization/how-to-winning-seo-website-audit-growth/)
13. Practice prioritizing findings — focus on telling the "so what" story, not listing issues
14. Review your work with a teammate for feedback

### Ongoing
- Complete the [Technical SEO and AI Search Essentials](https://www.semrush.com/academy/courses/techincal-seo-and-ai-search-essentials-with-semrush/) course
- Browse [LearningSEO.io's audit section](https://learningseo.io/seo_roadmap/execute-seo/seo-audits-recommendations/) for new templates and techniques
- Schedule weekly re-crawls on all active client domains
- Build API automation as you identify repetitive data pulls
