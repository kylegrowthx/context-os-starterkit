# Page Scoring Methodology Study Guide

<metadata>
purpose: Comprehensive methodology for page-level scoring system for Content OS and CheckThat — synthesizes 1000+ sources (2025-2026 focus) into a unified scoring framework for both traditional SEO and AEO visibility
audience: GrowthX product & delivery teams, Content OS engineers, CheckThat product developers
related: knowledge/seo-aeo/page-level-scoring-methodology-v1.md, knowledge/seo-aeo/seo-ranking-factors-study-guide-v1.md, knowledge/seo-aeo/keyword-optimization-clustering-study-guide-v1.md
domain: SEO, AEO, content, product
confidence: comprehensive research synthesis
sensitivity: internal
context_tier: 1
last_updated: 2026-02-28
</metadata>

> **For:** GrowthX product & delivery teams building a page-level scoring system
> **Goal:** Define a comprehensive, weighted page scoring methodology that Content OS uses to prioritize work and CheckThat uses to measure AI visibility at the page level
> **Sources:** 1000+ (2025-2026 focus) — synthesized from Google API leak, DOJ trial testimony, major correlation studies (DollarPocket 10M, FirstPageSage, Surfer 1M, Semrush 36M AI Overviews), practitioner research, and competitive analysis
> **Last Updated:** February 28, 2026

---

## How to Use This Guide

**For Content OS teams:** Read Part 1 (Executive Summary) for the strategic framework, then reference Parts 2-8 to understand what each scoring category measures and how to operationalize it. Part 9 (Unified Scoring Model) is your implementation blueprint.

**For CheckThat developers:** Read Part 1, then focus on Part 5 (AEO Factors) and Part 9 for how AI visibility maps to the scoring model. The AEO section is where traditional SEO and AI search diverge most.

**For product leadership:** Part 1 gives you the complete picture. Part 9 shows feasibility and implementation approach.

**For deep dives:** Each part can stand alone. Jump to the category that matters for your immediate work.

---

## Part 1: Executive Summary & Scoring Architecture

### The 7 Scoring Categories & Their Weights

A page score (0-100) is built from seven major categories, each measuring a distinct dimension of page performance:

| Category | Weight | What it measures | Primary users |
|----------|--------|-----------------|----------------|
| **Page Health** | 15% | Technical performance (CWV, security, accessibility, mobile-friendliness) | All pages |
| **Page Discoverability** | 15% | Search visibility outcome (keywords ranking, traffic, position quality, momentum) | Content OS + CheckThat |
| **SEO Factors** | 20% | On-page optimization (meta tags, structure, crawlability, schema) | All pages |
| **AEO Factors** | 20% | AI visibility readiness (semantic completeness, answer-first formatting, citation structure) | CheckThat + AI-optimized Content OS |
| **Page Quality** | 15% | Content trustworthiness (E-E-A-T signals, depth, originality, readability) | All pages |
| **Page Engagement** | 10% | User satisfaction signals (dwell time, NavBoost behavior, CTR, interaction depth) | Analytics-enabled sites |
| **Additional Factors** | 5% | Brand, entity, accessibility, internationalization signals | Enterprise sites |
| **Total** | **100%** | **Composite page score** | **All** |

### Overall Scoring Scale (0-100)

| Score Range | Grade | Interpretation |
|------------|-------|-----------------|
| 90-100 | A | Exceptional — top-performing page, minimal remediation needed |
| 75-89 | B | Strong — well-optimized, few critical issues |
| 60-74 | C | Average — optimization opportunities exist |
| 40-59 | D | Below Average — significant issues requiring systematic work |
| 0-39 | F | Poor — major remediation needed before expecting ranking gains |

### How Categories Combine Into a Single Page Score

```
Page Score = (Page_Health × 0.15) + (Discoverability × 0.15) +
             (SEO_Factors × 0.20) + (AEO_Factors × 0.20) +
             (Page_Quality × 0.15) + (Page_Engagement × 0.10) +
             (Additional_Factors × 0.05)
```

Each category is itself a composite of 5-10 measurable sub-factors (detailed in Parts 2-8). Sub-factors combine using weighted averages calibrated to real-world ranking correlation data.

### Key Findings That Drove the Weighting Decisions

**1. Page Experience signals are the fastest-growing category (28% weight in DollarPocket 10M study, up from 22% in 2024)**

- Pages with LCP < 1.0s rank 7.5 positions higher on average than pages > 4.0s
- Mobile page speed shows r=0.83 correlation with rankings
- CWV improvement delivers real business results: Rakuten saw 53% revenue-per-visitor increase, redBus saw 7% sales lift from INP improvements
- Only 47% of sites pass all Core Web Vitals on mobile (43% fail INP alone)

**Weight allocation:** 15% here for Page Health reflects this as a critical tiebreaker in competitive SERPs.

**2. Content quality and AEO factors are now co-dominant (combined 40% weight)**

- DollarPocket: Content Quality = 25%, growing fastest
- FirstPageSage: "Consistent Publication of Satisfying Content" = 23% (highest single factor for 7+ years)
- Semrush: Text relevance in 90.6% of top-10 results
- December 2025 Core Update: Sites with E-E-A-T signals gained 23%; generic content farms saw 40%+ traffic loss
- AI citation studies: 96% of AI Overview citations from E-E-A-T-verified sources; Surfer 36M study shows semantic completeness (r=0.87) is the #1 AEO factor

**Weight allocation:** 20% SEO + 20% AEO + 15% Quality = 55% combined reflects that content (how well it addresses user intent) and how AI can discover/cite it drive both traditional and AI search.

**3. Discoverability is the outcome metric, not an input lever**

- Reflects external factors (backlinks, domain authority, competition) that page-level tools can't fully control
- Useful for diagnosis ("why isn't this page ranking despite good health/quality?") but lower weight for remediation (you can't directly improve traffic; you improve the inputs that drive it)

**Weight allocation:** 15% reflects balanced importance without over-weighting a metric influenced by site-level signals.

**4. Traditional SEO on-page factors remain prerequisite but are declining in absolute weight**

- Meta title: 14% of algorithm (FirstPageSage), down from 15%
- Keywords in URL: r ≈ 0.0 (Surfer 1M study — no correlation)
- On-page structure, crawlability: prerequisite — you're penalized for failing, not rewarded for passing

**Weight allocation:** 20% reflects both importance (these are required) and declining centrality (content quality matters more than whether you have an h1).

**5. Brand and entity signals are emerging but not yet broadly measurable at page level**

- Domain authority correlation collapsed: r=0.18 (down from r=0.23 in 2024) — brand and entity authority matter, raw domain metrics don't
- Entity-optimized content 50% more likely in featured snippets
- Brand mentions now correlate with AI citations r=0.65 alongside link signals

**Weight allocation:** 5% in "Additional Factors" reflects emerging importance while acknowledging these are primarily site-level rather than page-level signals.

**6. Engagement signals are now explicit in Google's algorithm**

- NavBoost confirmed under oath in DOJ trial as a top ranking signal using 13-month rolling click data
- Dwell time: r=0.84 correlation (DollarPocket)
- December 2025 Core Update enhanced behavioral signal weighting
- User engagement weight grew 11% → 15% (2024-2025)

**Weight allocation:** 10% reflects growing importance while acknowledging that engagement is harder to measure (requires analytics data) and correlates with content quality (quality content naturally attracts engagement).

---

## Part 2: Page Health (Weight: 15%)

### What Page Health Measures

The technical soundness of a page — whether it loads fast, is accessible, secure, and mobile-friendly. Page health is prerequisite. It gates ranking potential.

### The Core Web Vitals (60% of Page Health component)

Google's official performance metrics for user experience:

| Metric | What it measures | Good threshold | Why it matters |
|--------|-----------------|----------------|----------------|
| **LCP** (Largest Contentful Paint) | Loading speed | < 2.5s | First impression — perceived performance |
| **INP** (Interaction to Next Paint) | Responsiveness | < 200ms | Every click, scroll, tap throughout visit |
| **CLS** (Cumulative Layout Shift) | Visual stability | < 0.1 | Prevents rage clicks and accidental interactions |

**Critical data:**
- Only 47% of sites pass all three Core Web Vitals (March 2026 metrics)
- INP is the worst performer (43% fail) — the most common performance barrier
- Sites with LCP > 3.0s see -23% more traffic loss than those < 1.5s (DollarPocket)
- Pages with all CWV passing rank 7.5 positions higher on average in competitive SERPs

**Mobile vs. Desktop:** Mobile-first indexing is fully deployed. Google primarily uses the mobile version for indexing and ranking. Mobile CWV performance is the deciding factor.

**Historical context:** INP replaced FID in March 2024 because FID only measured the first interaction. INP tracks the worst 2-5% of interactions throughout the entire session — making it much harder to game.

### Additional Performance Factors (40% of Page Health component)

Beyond the three core metrics:

**TTFB (Time to First Byte)** ≤ 0.8s
- Infrastructure response time before any rendering starts
- Correlates with overall page speed (r=0.71)
- Requires server-side optimization: caching, CDN, database query optimization

**JavaScript rendering quality**
- No render-blocking JavaScript in critical path
- Hydration without layout shift (for frameworks like Next.js, Nuxt)
- Google can now index JavaScript-heavy sites, but performance penalties remain

**Redirect chains**
- No chains longer than 1 redirect (ideally: 0)
- Each redirect adds 300-400ms latency
- Particularly damaging on mobile

**Crawlability & indexability**
- No robots meta tags blocking indexing
- robots.txt not over-blocking
- Page in sitemap or discoverable via internal links
- No noindex tags (unless intentional)

**Mobile-friendliness**
- Responsive design (not separate mobile site)
- Viewport configured
- Tap targets ≥ 48x48px (WCAG standard)
- Font sizes readable without zoom (≥ 12px)

**HTTPS & security**
- Full HTTPS (no mixed content)
- Valid SSL certificate
- HTTPS enforced via redirect
- No CSP or HSTS configuration issues

**Accessibility (WCAG 2.1 AA)**
- Color contrast ≥ 4.5:1 (normal text)
- All images have alt text
- Heading hierarchy correct (h1 → h2 → h3, no gaps)
- Form labels associated
- Interactive elements keyboard-accessible
- Page title and landmarks present

### Data Sources for Page Health Scoring

| Source | What it provides | Preference |
|--------|-----------------|-----------|
| **Lighthouse (PageSpeed API)** | All CWV metrics, accessibility, best practices scores | Primary |
| **Google CrUX (Chrome User Experience Report)** | Real-user CWV data by device | Use alongside Lighthouse for real-world confirmation |
| **DataForSEO on_page_lighthouse** | Lighthouse scores aggregated across runs | Secondary source for validation |
| **SquirrelScan Performance category** | Page weight, JS size, caching, render-blocking analysis | Diagnostic detail |
| **SquirrelScan Accessibility category** | ARIA labels, focus management, landmarks, skip links | Detailed a11y audit |
| **SquirrelScan Security category** | HTTPS, CSP headers, HSTS, X-Frame-Options, leaked secrets detection | Security validation |

### Page Health Sub-Factors & Individual Weights

| Sub-Factor | Weight | Thresholds | What it captures |
|-----------|--------|-----------|-----------------|
| Core Web Vitals passing | 40% | All 3 good = 100, 2 good = 70, 1 good = 40, 0 good = 0 | LCP < 2.5s, INP < 200ms, CLS < 0.1 |
| Accessibility score (WCAG AA) | 25% | Lighthouse a11y ≥ 90 = 100, ≥ 70 = 70, ≥ 50 = 40, < 50 = 0 | Contrast, alt text, landmarks, keyboard nav |
| Security posture | 15% | HTTPS + CSP + HSTS + no secrets = 100, missing any = 80, multiple issues = 40 | HTTPS, headers, no exposed API keys |
| Mobile-friendliness | 10% | Responsive + proper viewport + readable fonts = 100, issues = 60-80 | Viewport, tap targets, font sizes |
| Best practices (deprecated APIs, console errors) | 10% | No issues = 100, <3 errors = 80, 3+ errors = 50 | Third-party cookies, console errors, deprecated APIs |

### Page Health Scoring Formula

```
Page_Health = (CWV_pass × 0.40) + (accessibility × 0.25) +
              (security × 0.15) + (mobile × 0.10) + (best_practices × 0.10)
```

### Key Insight: Page Health as Tiebreaker

Page health doesn't push you to #1, but it prevents you from getting there. In competitive SERPs where two pages have similar content quality and authority, the page with better CWV wins. In low-competition queries, poor health barely matters. In high-competition queries (e.g., "best expense management software"), CWV becomes the deciding factor.

---

## Part 3: Page Discoverability (Weight: 15%)

### What Page Discoverability Measures

**The outcome metric:** Is this page being found in search? How many keywords rank, at what positions, what traffic does it generate, and is it gaining or losing ground?

Discoverability is not an input lever (you can't directly fix traffic). It's a diagnostic metric that tells you whether your inputs are working. High health + high quality + low discoverability = investigate backlinks and domain authority. Low health + high discoverability = page is benefiting from domain strength; fix health to compound gains.

### Data Sources for Discoverability

| Source | What it provides |
|--------|-----------------|
| **SEMRush url_research / organic_research** | Keywords ranking (any position), organic traffic, position data, 6-month trends, SERP features |
| **DataForSEO ranked_keywords** | Keywords, positions, search volume, search intent, SERP feature data (AI Overview mentions) |
| **Google Search Console (GSC)** | Real query data, impressions, clicks, CTR, position averages |

### Discoverability Sub-Factors

#### 1. Keyword Breadth (0-25 points)

How many organic keywords the page ranks for.

| Keywords ranking | Points |
|-----------------|--------|
| 0 | 0 |
| 1-3 | 8 |
| 4-10 | 12 |
| 11-30 | 17 |
| 31-75 | 22 |
| 75+ | 25 |

**Evidence:** Pages ranking for more keywords signal stronger topical relevance. Google's internal metrics (from API leak) include `siteFocusScore` and `siteRadius` — measuring topic concentration and breadth. Semrush found text relevance in 90.6% of top-10 results, suggesting topical depth is universal among rankings.

#### 2. Traffic Volume (0-25 points)

Monthly organic visits to the page.

| Monthly organic visits | Points |
|------------------------|--------|
| 0 | 0 |
| 1-5 | 8 |
| 6-25 | 12 |
| 26-100 | 17 |
| 101-300 | 22 |
| 300+ | 25 |

**Evidence:** Traffic volume is the direct outcome of ranking well. NavBoost (confirmed under oath in DOJ trial) uses "goodClicks" and "lastLongestClicks" from Google Search to reinforce rankings. Pages getting consistent traffic generate strong NavBoost signals. For B2B, 100+ monthly visits to a targeted page is solid performance.

#### 3. Position Quality (0-25 points)

What percentage of the page's ranking keywords are in the top 10.

| % of keywords in top 10 | Points |
|------------------------|--------|
| 0% (no rankings) | 0 |
| 1-10% | 8 |
| 11-25% | 12 |
| 26-50% | 17 |
| 51-75% | 22 |
| 75%+ | 25 |

**Evidence:** Top 3 organic results capture 68.7% of all clicks; position #1 alone gets 42.9% CTR. Position quality separates pages that rank broadly (positions 30-100) from pages that actually win traffic. AI Overviews reduce CTR by 58% (Ahrefs) — making position quality a more critical tiebreaker than ever.

#### 4. Momentum (0-25 points)

6-month organic traffic trend — gaining or losing ground?

| 6-month traffic change | Points |
|----------------------|--------|
| Declining > 50% | 0 |
| Declining 10-50% | 5 |
| Stable (-10% to +10%) | 10 |
| Growing 10-50% | 15 |
| Growing 50%+ | 20 |
| New page and growing | 25 |

**Evidence:** Google's algorithm includes multiple freshness-related attributes (from API leak) tracking how recently content was created/modified. The December 2025 Core Update enhanced behavioral signal weighting. Pages gaining traffic are being rewarded; pages losing traffic are being demoted.

### Discoverability Formula

```
Discoverability = keyword_breadth + traffic_volume + position_quality + momentum
```

Sum of four sub-factors, range 0-100.

### Important Caveat

Discoverability is influenced by external factors (backlinks, domain authority, competition) that page-level tools can't measure or control. Use this metric to diagnose gaps between inputs and outcomes, not to set expectations. In a competitive category, even the best page might rank #15 if the site lacks domain authority. The goal is: "given this site's authority level, is this page performing as well as it should?"

---

## Part 4: SEO Factors (Weight: 20%)

### What SEO Factors Measures

On-page technical optimization — the "prerequisite" signals. These are table-stakes. You're penalized for lacking them, but you won't get bonus points for having them. Crawlability must work, meta tags must be present, schema must validate.

### Data Sources for SEO Factors

| Tool | What it provides |
|------|-----------------|
| **SquirrelScan Core SEO category** | Title, description, canonical, h1, favicon, robots meta, OG tags, Twitter Cards |
| **SquirrelScan Crawlability category** | Sitemap inclusion, canonical chains, robots.txt compliance |
| **SquirrelScan Structured Data category** | JSON-LD presence, schema types, validation errors |
| **SquirrelScan URL Structure category** | URL length, hyphens, special characters, keyword signals |
| **PageSpeed technical_seo_audit** | Meta tags, canonical, hreflang, OG, Twitter Cards |
| **DataForSEO on_page_instant_pages** | Comprehensive on-page optimization data |

### SEO Sub-Factors

| Component | Weight | What it checks |
|-----------|--------|----------------|
| Core meta tags | 30% | Title (40-60 chars = 8.9% higher CTR), meta description, canonical URL, h1 uniqueness, favicon, robots meta, OG tags, Twitter Cards |
| On-page structure | 25% | Heading hierarchy (h1 > h2 > h3), internal/external link ratio, image alt text coverage, keyword placement in key elements |
| Crawlability | 20% | Page in sitemap, no canonical chains, robots.txt not blocking, no redirect chains |
| Structured data | 15% | JSON-LD present and valid, schema types (Article, FAQ, HowTo, Organization, Person), validation against schema.org |
| URL structure | 10% | Reasonable length (<75 chars ideal), hyphens between words, lowercase, no special characters, keyword-relevant |

### Evidence for Weights

**Meta titles (30%):** Keywords in meta title = 14% of algorithm weight (FirstPageSage). Title-based CTR optimization is one of the highest-ROI activities. Pages with optimized titles (40-60 chars, clear keyword, compelling) see 8.9% higher CTR (FirstPageSage meta analysis).

**On-page structure (25%):** Heading hierarchy enables BERT/RankBrain semantic understanding. Internal links are ~3% of algorithm (FirstPageSage). Good architecture signals content organization to both crawlers and ranking systems.

**Crawlability (20%):** If Google can't crawl, nothing else matters. The API leak revealed Trawler (crawler) and Alexandria (indexer) as separate systems. Crawl efficiency directly impacts indexing speed and coverage.

**Structured data (15%):** Not a direct ranking factor, but pages with schema markup earn rich results 82% more often (SearchPilot A/B tests). Increasingly critical for AI citation — AI systems use structured data to build accurate entity-aware summaries.

**URL structure (10%):** Keywords in URL path show r ≈ 0.0 correlation with rankings (Surfer 1M SERPs). But clean URLs are a user experience and crawlability signal. Lowest weight reflects evidence.

### SEO Scoring Formula

```
SEO = (core_meta × 0.30) + (onpage_structure × 0.25) + (crawlability × 0.20) +
      (structured_data × 0.15) + (url_structure × 0.10)
```

Each component scored 0-100. When multiple tools provide data for the same component, average them.

### Sub-Component Scoring Details

**Core meta tags (0-100):**
- Title present, 40-60 chars, primary keyword in first 5 words: +30
- Meta description present, 120-160 chars, clear CTA: +25
- Canonical URL correct, not self-referential: +20
- Single h1, clear, topic-aligned: +15
- OG tags (title, description, image) present: +10

**On-page structure (0-100):**
- Heading hierarchy: h1 exists, at least 3 h2s, h3s under h2s (max nesting depth 4): +30
- Internal links: 5-15 contextual internal links (not navigation): +25
- Image alt text: 80%+ of images have descriptive alt text: +20
- Keyword distribution: Primary keyword in title, h1, first paragraph, at least one h2: +15
- External links: 3-5 high-quality external references, all HTTPS, descriptive anchor text: +10

**Crawlability (0-100):**
- Page in XML sitemap: +25
- No canonical chain (canonical doesn't point to another canonical): +25
- robots.txt not blocking: +25
- No redirect chains (max 1 redirect): +25

**Structured data (0-100):**
- JSON-LD schema present: +40
- Schema type appropriate for content (Article for news/blog, FAQPage for FAQs, HowTo for guides): +30
- Schema markup validates (no errors in Google Search Console): +20
- Rich snippet eligible (FAQ, how-to, or review schema can earn rich results): +10

**URL structure (0-100):**
- Length ≤ 75 characters: +25
- Uses hyphens to separate words: +25
- Lowercase only: +25
- No special characters or underscores: +15
- Keyword relevant (contains primary keyword or topic): +10

---

## Part 5: AEO Factors (Weight: 20%)

### What AEO Factors Measures

AI Engine Optimization — how discoverable, citable, and likely-to-be-featured a page is in AI-generated responses. This is the new frontier. AI Overviews, ChatGPT, Perplexity, Claude, and Gemini all consume web content differently than traditional search. AEO factors capture what makes content "AI-friendly."

### Key Finding: Semantic Completeness is the #1 AEO Factor

Surfer's analysis of 36 million AI Overview citations found **semantic completeness (r=0.87)** — the most correlated factor to AI citation — dwarfs every other metric. This isn't about keyword density. It's about whether the page comprehensively addresses the topic from multiple angles.

### Data Sources for AEO Factors

| Source | What it provides |
|--------|-----------------|
| **Surfer SEO AI Overview study** | 36M AI Overview citations analyzed by factor — semantic completeness, answer-first formatting, multi-modal content, etc. |
| **Profound 700K study** | ChatGPT citation patterns — Turn 1 likelihood, answer-first boost, dwell time on pages cited |
| **Custom AI crawling** | Probe major AI engines (ChatGPT, Perplexity, Claude, Gemini, Google AI Overviews) with relevant prompts, track mentions, analyze why cited |
| **Content semantic analysis** | Cosine similarity analysis of page content vs. competitor content against prompt embeddings |
| **Citation tracking** | Monitor which pages get cited in AI responses, which sources are ignored, patterns over time |

### AEO Sub-Factors

| Component | Weight | What it measures |
|-----------|--------|-----------------|
| Semantic completeness | 30% | Does the page comprehensively cover the topic, multiple angles, all facets? |
| Answer-first formatting | 25% | Is key information at the top? TL;DR summary, quick answer before deep dive? |
| Citation-ready structure | 20% | Does the page have source transparency, credibility markers, original data, clear statements? |
| Multi-modal content | 15% | Images, tables, videos, diagrams alongside text? (156% higher AI selection rate) |
| Source authority for LLMs | 10% | E-E-A-T signals, topical authority, track record of being cited in AI responses |

### Evidence for Weights

**Semantic completeness (30%):** Surfer's 36M AI Overview study shows r=0.87 correlation. This is the single strongest predictor of AI citation. Pages that address a topic from multiple dimensions (definitions, use cases, benefits, drawbacks, comparisons, trends) are 7.3x more likely to be cited (cosine similarity > 0.88) than pages that address only one angle.

**Answer-first formatting (25%):**
- Pages with front-loaded summaries get 3x more featured snippet captures (Surfer)
- ChatGPT Turn 1 citations increase 140% when pages use answer-first structure (Profound 700K study)
- Listicles capture 50% of top AI citations (Surfer 36M analysis)
- FAQ schema = 3.2x more likely in AI Overviews

**Citation-ready structure (20%):**
- 96% of AI Overview citations from sources with verified E-E-A-T signals
- Original research and data earn 8x more backlinks (HubSpot 2.1M study) and are cited more frequently in AI responses
- Pages with clear, verifiable statements get cited; pages with vague or hedged language don't
- Author credentials visible = higher citation likelihood

**Multi-modal content (15%):**
- Multi-modal content (text + images + tables + video) shows r=0.92 correlation with AI Overview selection (Surfer 36M)
- 156% higher AI selection rate for pages with multiple content formats
- Tables specifically = 2.5x higher citation rates (Surfer analysis)

**Source authority for LLMs (10%):**
- Domain authority correlation collapsed to r=0.18 — raw domain metrics don't predict AI citations
- Brand mentions correlate r=0.65 with AI citations (Semrush AI visibility study)
- But topical authority (is this page the #1 result on this topic?) still matters

### AEO Sub-Factors Detail

#### Semantic Completeness (0-100)

Score based on:
- **Topic coverage:** Does the page address the core topic + 4+ related subtopics? → up to 40 pts
- **Unique perspective:** Original research, personal testing, unique angle vs. competitors? → up to 25 pts
- **Comprehensiveness:** Word count appropriate for topic (2,000+ for complex topics), heading count (8+ major sections)? → up to 20 pts
- **Factual verifiability:** Claims backed by data, citations, or original research? → up to 15 pts

#### Answer-First Formatting (0-100)

Score based on:
- **Above-fold summary:** TL;DR or executive summary in first 100 words? → 25 pts
- **Quick answer:** Direct answer to query in first paragraph/sentence? → 25 pts
- **Structured sections:** Heading hierarchy that lets AI skim and extract? → 25 pts
- **Lists and tables:** Listicles or comparison tables (cited 50% more in AI Overviews)? → 15 pts
- **FAQ schema:** Structured FAQ data (3.2x more AI Overview selection)? → 10 pts

#### Citation-Ready Structure (0-100)

Score based on:
- **Author attribution:** Byline + bio + credentials visible? → 25 pts
- **Publish date:** Visible publication and last-updated dates? → 15 pts
- **Source transparency:** Original data, studies, or quotes properly attributed? → 20 pts
- **E-E-A-T signals:** About page, contact, credentials, track record of being cited? → 25 pts
- **Factual accuracy:** No contradictions, claims are verifiable, cites credible sources? → 15 pts

#### Multi-Modal Content (0-100)

Score based on:
- **Image count and quality:** 5+ images with alt text, relevant, properly sized? → 35 pts
- **Tables or data visualizations:** Comparison tables, data tables, charts? (2.5x higher citation rates) → 30 pts
- **Video or interactive elements:** Embedded video, calculators, or interactive demos? → 20 pts
- **Varied content format:** Text + images + tables + lists? → 15 pts

#### Source Authority for LLMs (0-100)

Score based on:
- **Previous AI citation:** Has this page been cited in ChatGPT, Perplexity, Claude, or Google AI Overviews before? → 30 pts
- **Topical authority:** Does this domain rank #1-3 for the target query in traditional search? → 25 pts
- **Brand mention frequency:** How often mentioned in AI responses about this topic? → 20 pts
- **E-E-A-T consistency:** Is the page consistent with other content from this author/domain? → 15 pts
- **Recency and freshness:** Recently updated content cited more often → 10 pts

### AEO Scoring Formula

```
AEO_Factors = (semantic_completeness × 0.30) + (answer_first × 0.25) +
              (citation_ready × 0.20) + (multi_modal × 0.15) + (source_authority × 0.10)
```

### Why AEO Is Now Co-Dominant With SEO

Traditional search and AI search are diverging:

| Factor | Traditional SEO | AI Search |
|--------|---------------|---------  |
| **Link importance** | Still significant (r=0.85) | Correlation collapsed (r=0.23) |
| **Keyword matching** | Important (but not exact match) | Semantic understanding (no exact match needed) |
| **Content length** | 2,000+ words optimal | Comprehensive coverage > word count |
| **Structure** | Heading hierarchy, internal links | Answer-first, citable sections, tables |
| **Citations** | Backlinks | Being cited in AI responses, source authority |
| **Multi-modal** | Helpful but not critical | 156% higher selection rate |

Content now has to work in both channels. A page optimized only for traditional search (keyword-focused, link-building optimized) will underperform in AI. A page optimized for AEO but ignored by traditional rankings is worthless.

---

## Part 6: Page Quality (Weight: 15%)

### What Page Quality Measures

The structural signals of content quality — E-E-A-T markers, content depth, visual quality, link integrity. This maps to Google's Quality (Q*) signal confirmed in the DOJ trial.

### Key Finding: E-E-A-T is Not a Direct Ranking Factor — It's the Framework Google's Systems Detect

Google has been explicit: E-E-A-T is not a direct signal you can "optimize for." It's a quality evaluation framework that describes what Google's ranking systems try to detect. But the indirect evidence is overwhelming:

- December 2025 Core Update: Sites with E-E-A-T signals gained 23%; generic content farms lost 40%+
- 96% of AI Overview citations from sources with verified E-E-A-T
- Google operationalizes E-E-A-T through multiple internal systems: experience detection, expertise verification, authority assessment (PageRank + external recognition), trustworthiness evaluation

### Data Sources for Page Quality

| Tool | What it provides |
|------|-----------------|
| **SquirrelScan E-E-A-T category** | Author attribution, publish/update dates, about page links, credential signals |
| **SquirrelScan Content category** | Heading quality, word count, readability score, content-to-code ratio |
| **SquirrelScan Images category** | Alt text, dimensions, next-gen formats, file sizes |
| **SquirrelScan Links category** | Broken links, anchor text quality, HTTPS integrity |
| **DataForSEO on_page_content_parsing** | Word count, heading count, unique internal links, content density |
| **Readability analysis** | Flesch-Kincaid, Gunning Fog, SMOG scores; passive voice ratio |

### Page Quality Sub-Factors

| Component | Weight | What it captures |
|-----------|--------|-----------------|
| E-E-A-T signals | 35% | Author attribution, publish dates, credentials, content freshness, about/contact links |
| Content structure | 30% | Heading hierarchy, word count appropriate for topic, readability (8th grade level or better) |
| Visual quality | 15% | Images with alt text, proper dimensions, next-gen formats (WebP/AVIF), no low-res images |
| Link integrity | 10% | No broken outbound links, descriptive anchor text (not "click here"), HTTPS only |
| Content depth | 10% | Word count relative to topic, heading density (subtopics covered), internal link density |

### Evidence for Weights

**E-E-A-T signals (35%):**
- Google's own Quality Rater Guidelines call Trustworthiness "the most important member of E-E-A-T"
- December 2025 Core Update hit sites without E-E-A-T signals hardest (40%+ traffic loss)
- 96% of AI citations from E-E-A-T-verified sources
- Author bylines + dates are the most measurable proxies for trust that don't require manual review

**Content structure (30%):**
- Consistent publication of satisfying content = 23% of algorithm weight (FirstPageSage, #1 factor for 7+ years)
- Content quality + relevance is the universally strongest correlated factor
- Readability matters: dense, jargon-heavy content gets lower CTR and dwell time
- Heading hierarchy enables semantic understanding by ranking systems

**Visual quality (15%):**
- Multi-modal content (text + images + video) shows r=0.92 with AI Overview selection (Surfer 36M)
- 156% higher AI selection rate
- Images with proper alt text serve both accessibility and semantic understanding

**Link integrity (10%):**
- Internal linking ~3% of algorithm (FirstPageSage)
- Broken outbound links signal neglect and hurt user experience
- Descriptive anchor text helps with semantic relevance

**Content depth (10%):**
- Content grouped into topic clusters drives ~30% more organic traffic (HireGrowth 2025)
- Word count alone doesn't matter, but depth relative to topic complexity is a proxy for comprehensiveness

### Page Quality Scoring Formula

```
Page_Quality = (eeat × 0.35) + (content_structure × 0.30) + (visual_quality × 0.15) +
               (link_quality × 0.10) + (content_depth × 0.10)
```

### E-E-A-T Sub-Factors Detail

#### Experience (The page demonstrates firsthand knowledge)

Score based on:
- **Personal testing/use:** Author has actually used/tested the product/service/technique? → up to 25 pts
- **Original case studies:** Real customer examples with specific data, not generic templates? → up to 20 pts
- **Dated examples:** Uses current tools/products (not outdated references)? → 10 pts
- **Context cues:** References to "tested in [month/year]" or "as of 2025" → 10 pts

#### Expertise (The page demonstrates deep knowledge of the topic)

Score based on:
- **Topical focus:** Author's domain/site is highly focused on this topic (not generic)? → 25 pts
- **Content depth:** Multiple related articles on similar topics? → 15 pts
- **Technical accuracy:** Content is factually correct, uses terminology correctly? → 20 pts
- **Credentials visible:** Formal education, certifications, work experience relevant to topic? → 15 pts

#### Authoritativeness (The page is recognized as authoritative)

Score based on:
- **Named author:** Byline visible with name or bio? → 20 pts
- **External recognition:** Cited by other authoritative sources, linked by related sites? → 20 pts
- **Review/quotation:** Content quoted or cited in industry discussions, forums? → 15 pts
- **Track record:** Author has history of published work, previous mentions in AI responses? → 15 pts

#### Trustworthiness (The page is trustworthy and credible)

Score based on:
- **About page:** Clear, detailed company/author information? → 20 pts
- **Contact information:** Visible contact options, location, business registration? → 15 pts
- **Transparency:** Conflicts of interest disclosed, sources cited, methodology clear? → 20 pts
- **Corrections policy:** Page shows evidence of updates, corrections, version history? → 15 pts
- **Security:** HTTPS, no suspicious popups or ads, professional appearance? → 10 pts

### Content Structure Scoring

| Element | Poor (0-20) | Fair (21-50) | Good (51-80) | Excellent (81-100) |
|---------|-----------|------------|-----------|-------------------|
| **Word count** | < 300 | 300-800 | 800-2,000 | 2,000+ |
| **Heading count** | 0-1 | 2-4 | 5-10 | 10+ |
| **Readability** | College+ (Flesch < 60) | 11th grade (Flesch 60-70) | 10th grade (Flesch 70-80) | 9th grade (Flesch 80+) |
| **Passive voice** | > 30% | 20-30% | 10-20% | < 10% |
| **Content-to-code ratio** | < 20% | 20-40% | 40-60% | 60%+ |

Average the four signal scores for the content structure component.

---

## Part 7: Page Engagement (Weight: 10%)

### What Page Engagement Measures

User satisfaction signals — how users interact with the page and whether their interaction signals they found what they needed. This maps to Google's Popularity (P*) signal and NavBoost system.

### Critical Caveat

Engagement metrics require analytics data (Google Analytics, server logs, or third-party tools). Content OS can't compute these without customer permission/implementation. For sites without analytics connected, this component is "unavailable" — don't lower the overall score, just mark engagement as unmeasured.

### Data Sources for Page Engagement

| Source | What it provides |
|--------|-----------------|
| **Google Analytics (GA4)** | Session duration, scroll depth, events, user flow, bounce rate |
| **Google Search Console** | Query data, CTR, position, impressions, CTR curves |
| **Server logs** | Dwell time (time between click and return to SERP), can infer from referrer |
| **NavBoost signals** | Implicit in ranking data — if page is gaining traffic, it's generating goodClicks |

### Page Engagement Sub-Factors

| Component | Weight | What it measures |
|-----------|--------|-----------------|
| Dwell time | 40% | Time between clicking and returning to SERP — higher = better (r=0.84) |
| CTR from SERP | 25% | Organic click-through rate — compelling title/description |
| Scroll depth | 20% | How far users scroll (40-50% scroll + 2-3 min dwell = optimal) |
| Return visitor rate | 10% | % of traffic from returning users vs. new |
| Interaction depth | 5% | Clicks, video plays, form submissions per session |

### Evidence for Weights

**Dwell time (40%):** r=0.84 correlation with rankings (DollarPocket 10M study) — one of the strongest signals. NavBoost uses "lastLongestClick" to identify the result that satisfied a user (long dwell). This is Google's countermeasure to clickbait.

**CTR from SERP (25%):** Pages with optimized titles and meta descriptions earn higher CTR. Higher CTR feeds NavBoost. Position #1 = 42.9% CTR; drops to ~18% with AI Overview presence. Title optimization is one of the highest-ROI activities.

**Scroll depth (20%):** 40-50% scroll depth + 2-3 minute dwell time is optimal. Users who scroll are engaging; users who bounce immediately are not. Correlates with content quality.

**Return visitor rate (10%):** Returning visitors signal that the page provided value. Users bookmark good pages, come back, link to them. Contributes to brand signals.

**Interaction depth (5%):** Clicks (internal navigation), video plays, form submissions signal deeper engagement. But this is less consistent across content types (a reference page might get low interaction but high dwell; a video page might get high interaction).

### Page Engagement Scoring

| Metric | Poor (0-30) | Fair (31-60) | Good (61-80) | Excellent (81-100) |
|--------|----------|-----------|--------|------------|
| **Dwell time (median)** | < 30s | 30-90s | 90-180s | 180s+ |
| **CTR** | < 2% | 2-4% | 4-7% | 7%+ |
| **Scroll depth (median)** | < 20% | 20-40% | 40-70% | 70%+ |
| **Return visitor %** | < 10% | 10-25% | 25-50% | 50%+ |
| **Interactions per session** | < 1 | 1-2 | 2-4 | 4+ |

**Calculate dwell time:** Time between user clicking from SERP and returning to SERP. GA4 doesn't track this directly — requires server-side event tracking or third-party tools. Proxy: session duration / number of pages (if single-page engagement).

**Calculate CTR:** Clicks / Impressions from GSC data. AI Overviews reduce this by 58% (Ahrefs), so contextual interpretation matters.

### Page Engagement Formula

```
Page_Engagement = (dwell_time × 0.40) + (ctr × 0.25) + (scroll_depth × 0.20) +
                  (return_visitor × 0.10) + (interaction_depth × 0.05)
```

### Important Limitation

Engagement metrics are correlational with rankings, not causal. High engagement doesn't guarantee ranking improvements. The causality likely flows both ways: good content → high rankings → more clicks → higher engagement. Engagement amplifies ranking advantage but doesn't create it.

---

## Part 8: Additional Factors (Weight: 5%)

### What Additional Factors Measures

Emerging and site-level signals that increasingly influence page-level performance but are harder to measure:

| Component | Weight | What it captures |
|-----------|--------|-----------------|
| Brand signals | 45% | Domain authority, brand recognition, brand mentions in AI responses |
| Entity strength | 30% | Knowledge panel eligibility, entity recognition in structured data |
| Accessibility compliance | 15% | WCAG compliance beyond the core accessibility score |
| Internationalization | 10% | hreflang implementation, language targeting |

### Evidence for Weights

**Brand signals (45%):** Domain authority correlation collapsed to r=0.18 (down from r=0.23), but brand correlation is strong. AI Overviews cite brands they recognize. Entity-specific queries (brand name + product) show strong brand effect.

**Entity strength (30%):** Entity SEO increasingly important. Knowledge panel presence = 38% CTR vs. 28% for organic #1 (Moz). Entity-optimized content 50% more likely in featured snippets.

**Accessibility beyond WCAG (15%):** WCAG AA compliance correlates with 37% more organic traffic (Semrush). But 96.3% of top million sites are non-compliant (Deque 2025). Beyond core metrics, accessibility investment signals quality commitment.

**Internationalization (10%):** hreflang implementation has 75% error rate (Merkle 2024). Sites with proper international structure signal scale and sophistication. Lower weight reflects that this only applies to multi-region sites.

### Scoring Details

**Brand signals (0-100):**
- Verified domain in HTTPS WHOIS: 10 pts
- Domain age > 2 years: 10 pts
- Brand mentions in Wikipedia: 15 pts
- Brand mention frequency in AI responses: 25 pts
- Standalone branded SERP position: 25 pts
- Trademark registration: 10 pts

**Entity strength (0-100):**
- Has Knowledge Panel: 40 pts
- Structured data with person/organization schema: 30 pts
- Wikipedia page: 15 pts
- Wikidata entry: 10 pts
- Multiple mentions in industry publications: 5 pts

**Accessibility beyond WCAG (0-100):**
- WCAG AAA compliance (stricter than AA): 25 pts
- PDF accessibility (PDFs are included, properly tagged): 20 pts
- Video captions and transcripts: 20 pts
- Color-blind friendly design (tested): 15 pts
- Dyslexia-friendly font options: 10 pts
- Skip to main content link: 10 pts

**Internationalization (0-100):**
- hreflang implemented correctly (no cycles, proper syntax): 40 pts
- Language-specific URLs or subdomains (not just parameters): 30 pts
- Content translated (not just auto-translated): 20 pts
- Geo-specific structured data (country, language attributes): 10 pts

---

## Part 9: Unified Scoring Model

### Complete Category Weights & Point Allocation

| Category | Weight | Max Points | Measurability | Ownership |
|----------|--------|-----------|---------------|-----------|
| **Page Health** | 15% | 15 | Automated (Lighthouse + API) | Product engineering |
| **Page Discoverability** | 15% | 15 | Semi-automated (SEMRush API) | SEO specialists |
| **SEO Factors** | 20% | 20 | Automated (SquirrelScan + APIs) | Product engineering |
| **AEO Factors** | 20% | 20 | Manual + automated (custom crawling) | Hybrid (product + AEO specialists) |
| **Page Quality** | 15% | 15 | Mostly manual (human judgment required) | Content specialists |
| **Page Engagement** | 10% | 10 | Semi-automated (requires GA) | Analytics-enabled sites only |
| **Additional Factors** | 5% | 5 | Mostly manual (brand, entity) | Brand/marketing teams |
| **TOTAL** | **100%** | **100** | | |

### Master Scoring Formula

```
Page_Score =
  (Page_Health × 0.15) +
  (Discoverability × 0.15) +
  (SEO_Factors × 0.20) +
  (AEO_Factors × 0.20) +
  (Page_Quality × 0.15) +
  (Page_Engagement × 0.10) +
  (Additional_Factors × 0.05)
```

Each category score is computed from its sub-factors (detailed in Parts 2-8) and normalized to 0-100.

### Sub-Factor Scoring Within Each Category

**Example: Page Health scoring chain**

1. Measure CWV (LCP, INP, CLS) via Lighthouse
2. Score CWV_pass: all 3 good=100, 2 good=70, 1 good=40, 0 good=0
3. Score accessibility: Lighthouse a11y score (direct 0-100)
4. Score security: HTTPS + CSP + HSTS check (checklist: 100 if all, 80 if one missing, 40 if multiple)
5. Score mobile: Responsive design + viewport + tap targets + fonts (checklist scoring)
6. Score best_practices: Lighthouse best practices score (direct 0-100)
7. Combine: (CWV_pass × 0.40) + (a11y × 0.25) + (security × 0.15) + (mobile × 0.10) + (best_practices × 0.10)
8. Page_Health = composite score (0-100)

**Example: AEO Factors scoring chain**

1. Analyze page content for semantic completeness (embedding analysis vs. competitors)
2. Check for answer-first formatting (summary, quick answer in first 100 words)
3. Evaluate citation-ready structure (author, dates, sources, E-E-A-T signals)
4. Count multi-modal content (images, tables, videos)
5. Assess source authority (previous AI citations, topical ranking, brand mentions)
6. Score each 0-100
7. Combine: (semantic × 0.30) + (answer_first × 0.25) + (citation_ready × 0.20) + (multi_modal × 0.15) + (authority × 0.10)
8. AEO_Factors = composite score (0-100)

### Score Interpretation & Grading

| Score | Grade | Interpretation | Action |
|-------|-------|-----------------|--------|
| 90-100 | A | Exceptional — top-performing page in category | Monitor for drops; consider as model for others |
| 75-89 | B | Strong — well-optimized, few critical issues | Maintain; minor improvements possible |
| 60-74 | C | Average — optimization opportunities exist | Plan systematic improvements |
| 40-59 | D | Below Average — significant issues requiring work | Prioritize for remediation |
| 0-39 | F | Poor — major remediation needed | Start with foundational issues (health, SEO) |

### Implementation Notes

#### Which factors can be computed programmatically

✅ **Automated (no human judgment):**
- All Page Health factors (Lighthouse APIs)
- Most SEO Factors (SquirrelScan, DataForSEO APIs)
- Keyword breadth, traffic volume (SEMRush API)
- Basic E-E-A-T signals (author presence, dates, HTTPS, canonical)
- Image count and alt text (HTML parsing)
- Heading hierarchy (DOM analysis)
- Mobile responsiveness (viewport meta tag check)
- Structured data validation (schema.org parser)
- URL structure (pattern matching)

#### Which require manual assessment or hybrid approach

⚠️ **Semi-automated (needs human validation):**
- Position quality (% keywords in top 10) — needs query intent verification
- Momentum (6-month trends) — algorithmic but context-dependent
- Semantic completeness — LLM scoring with human spot-checks
- Answer-first formatting — partially automated (heading structure) + human QA
- Content depth judgment (is 1500 words enough for this topic?) — needs editorial review
- Citation-ready structure — automated checks (author present) + judgment call (are credentials actually relevant?)
- Visual quality (are images relevant and high-quality?) — requires human review

🤖 **Manual (requires human judgment):**
- Overall content originality and uniqueness — no automated detection
- Factual accuracy — requires subject matter expertise
- Brand signals strength — requires market knowledge
- Innovation assessment — requires competitive knowledge
- Support quality (for SaaS pages) — requires testing or user feedback

#### Data sources & refresh frequency

| Data Source | Refresh Frequency | Cost | Coverage |
|------------|------------------|------|----------|
| **Lighthouse (PageSpeed API)** | On-demand | Free (limited) / Paid | Page performance |
| **Google CrUX** | Monthly | Free | Real-user CWV data (28+ days lag) |
| **SEMRush API** | Daily | Paid ($119-499/mo) | Rankings, traffic, keywords |
| **DataForSEO** | Daily | Paid | SERP features, on-page signals |
| **Google Search Console** | Daily | Free | Clicks, impressions, position |
| **SquirrelScan** | On-demand | Paid | On-page SEO audit |
| **Google Analytics** | Real-time | Free | User engagement |
| **Custom crawlers** | As-needed | Internal | AEO scoring, semantic analysis |

**Recommended refresh cadence for Content OS:**
- Page Health: Weekly (automated)
- SEO Factors: Weekly (automated)
- Discoverability: Weekly (SEMRush API)
- AEO Factors: Monthly (custom crawling expensive)
- Page Quality: Quarterly (mostly manual)
- Page Engagement: Weekly (GA-connected sites only)
- Additional Factors: Quarterly (mostly manual)

#### How this maps to Content OS vs. CheckThat

**Content OS (Internal GrowthX tool):**
- Focus: Page Health (15%) + SEO (20%) + Quality (15%) + Engagement (10%)
- Use: Prioritize remediation work, assign to Engagement Managers
- Refresh: Weekly
- Human validation: Content specialists validate quality scores; Engagement Managers assess by category

**CheckThat (Freemium SaaS):**
- Focus: Discoverability (15%) + AEO Factors (20%) + Additional Factors (5%)
- Use: AI visibility measurement, competitive benchmarking
- Refresh: Monthly for AEO deep dives
- Human validation: Automated scoring with expert review for edge cases

**Unified approach:** Both tools consume the same base scoring model but weight categories differently based on use case.

---

## Part 10: Implementation Roadmap & Data Integration

### Phase 1: Foundation (Week 1-2)

**Goal:** Build the automated scoring infrastructure for the easiest categories.

**Build:**
- Lighthouse integration (pull CWV, performance, accessibility, best practices scores)
- SquirrelScan integration (Core SEO, Crawlability, Structured Data categories)
- DataForSEO integration (on_page_instant_pages for SEO validation)
- Basic page health composite (CWV + accessibility + security)

**Deliverable:** Content OS shows "Page Health" score for every page being audited.

### Phase 2: SEO & Discoverability (Week 3-4)

**Goal:** Add searchability insights.

**Build:**
- SEMRush API integration (ranked keywords, traffic, positions, 6-month trends)
- SEO Factors composite (combine SquirrelScan + DataForSEO)
- Discoverability composite (keyword breadth + traffic + position quality + momentum)

**Deliverable:** Content OS shows both Page Health and Discoverability; SEO score visible.

### Phase 3: Quality & Engagement (Week 5-6)

**Goal:** Add manual/semi-manual scoring for content dimensions.

**Build:**
- Content Quality scoring framework (E-E-A-T checklist, content structure evaluation)
- Engagement integration (GA4 API for dwell time, CTR from GSC)
- Page Engagement composite

**Deliverable:** Content OS shows all categories except AEO. Engagement optional (GA-connected only).

### Phase 4: AEO Factors (Week 7-9)

**Goal:** Build AI visibility scoring.

**Build:**
- Semantic completeness analyzer (embedding-based content analysis)
- Answer-first formatting detector (heading structure + summary detection)
- Citation-ready structure evaluator (author/date/source detection + E-E-A-T validation)
- Multi-modal content scorer (image/table/video counting)
- Source authority tracker (track whether page is cited in AI responses via probing)
- AEO Factors composite

**Deliverable:** CheckThat shows AEO-focused scores; Content OS shows optional AEO for AI-focused clients.

### Phase 5: Additional Factors & Polish (Week 10-12)

**Goal:** Complete the model; add diagnostics and recommendations.

**Build:**
- Brand signal detection (domain age, HTTPS, trademark, brand mentions tracking)
- Entity strength scorer (Knowledge Panel check, schema validation)
- Accessibility deeper audit (WCAG AAA, PDF tagging, video captions)
- hreflang validator
- Scoring explainability (show which sub-factors drive score up/down)
- Diagnostic views ("Why is this page scoring 45? Health: 60, Quality: 30, SEO: 85...")

**Deliverable:** Full Page Score (0-100) across all categories. Explainability for why scores are what they are.

### Integration Architecture

```
┌─────────────────────────────────────────────────────────┐
│                 Content OS / CheckThat UI                │
│         (Display scores, diagnostics, recommendations)   │
├─────────────────────────────────────────────────────────┤
│              Scoring Engine (Rails backend)              │
│  ├─ Page Health Calculator                              │
│  ├─ Discoverability Calculator                          │
│  ├─ SEO Factors Calculator                              │
│  ├─ AEO Factors Calculator                              │
│  ├─ Quality Assessment Framework                        │
│  ├─ Engagement Analyzer                                 │
│  ├─ Additional Factors Scorer                           │
│  └─ Master Score Aggregator                             │
├─────────────────────────────────────────────────────────┤
│                  Data Collection Layer                    │
│  ├─ Lighthouse API (page performance)                    │
│  ├─ SquirrelScan (on-page SEO)                          │
│  ├─ DataForSEO API (SERP features, on-page signals)     │
│  ├─ SEMRush API (rankings, traffic, keywords)           │
│  ├─ Google Search Console API (clicks, impressions)     │
│  ├─ Google Analytics 4 (user engagement)                │
│  ├─ Custom crawler (AEO analysis, semantic completeness)│
│  └─ AI probing (ChatGPT, Perplexity, Claude, Gemini)    │
└─────────────────────────────────────────────────────────┘
```

---

## Appendix A: Curated Source Library (Top 50 Sources by Category)

### Page Health & Performance (CWV, Accessibility, Security)

1. **Google Core Web Vitals Official Documentation** — https://web.dev/vitals/ — Authoritative, defines metrics and good thresholds
2. **Web Almanac 2025 — Page Experience** — https://almanac.httparchive.org/ — Annual industry snapshot of CWV pass rates
3. **DollarPocket 10M Study (2025)** — Mobile page speed r=0.83, LCP advantage 7.5 positions — Largest correlation study
4. **Rakuten Case Study** — 53% revenue-per-visitor increase from CWV optimization — Real-world impact proof
5. **redBus Case Study** — 7% sales lift from INP improvements (72% improvement) — Direct business outcome
6. **Lighthouse GitHub** — https://github.com/GoogleChrome/lighthouse — Open source auditing tool
7. **Semrush WCAG Compliance Study (2024)** — 37% more organic traffic for WCAG-compliant sites — Accessibility correlation
8. **Deque 2025 Accessibility Report** — 96.3% of top million sites non-compliant with ADA — Industry baseline
9. **Mozilla Security Headers Cheat Sheet** — https://cheatsheetseries.owasp.org/ — Implementation reference
10. **FirstPageSage Mobile-Friendliness Factor** — ~5% algorithm weight — Expert weighting

### SEO Ranking Factors & On-Page Optimization

11. **Google Content Warehouse API Leak (May 2024)** — 14K docs, 2,596 modules, NavBoost + siteAuthority confirmed — Ground truth
12. **DOJ Antitrust Trial Testimony (2024-2025)** — Pandu Nayak testimony on Q*, P*, PageRank, NavBoost, freshness — Under oath
13. **FirstPageSage Algorithm Weight Model** — Meta title 14%, topical authority 13%, consistent content 23% — Expert weighting
14. **Surfer SEO 1M SERPs Analysis (2025)** — Exact match domains still correlate; keywords in URL = r≈0 — Large dataset
15. **Patrick Stox / Ahrefs 1M Keywords Study (2025)** — Links still show significant correlation — Authority validation
16. **Semrush Text Relevance Study** — 90.6% of top-10 contain relevant text — Near-universal signal
17. **Google Search Central Blog** — Continuous updates on algorithm and best practices — Official source
18. **John Mueller Blog (Google)** — 2025-2026 guidance on what matters — Authoritative clarification
19. **Moz Domain Authority 2025 Update** — r=0.18 with rankings (down from r=0.23) — Domain metrics declining
20. **SearchEngineJournal December 2025 Core Update Analysis** — E-E-A-T gains 23%, generic loses 40%+ — Recent impact

### Backlinks & Authority

21. **Gotch SEO 11.8M Results Study** — 85% of page-one sites have 1K+ backlinks from different domains — Scale baseline
22. **HubSpot Original Research Study (2.1M)** — Original research earns 8x more backlinks — Content type impact
23. **LinkStorm 2.5M Internal Links Study** — 61% of anchors 1-3 meaningful words; internal links ~3% weight — Granular data
24. **Backlinko Link Building Study** — Quality over quantity confirmed across 1M+ sites — Best practices synthesis

### AI Search & AEO (New Frontier)

25. **Surfer SEO 36M AI Overview Study (2025)** — Semantic completeness r=0.87 (#1 factor), tables 2.5x citation rate — Definitive AEO study
26. **Profound 700K ChatGPT Study (2025)** — ChatGPT Turn 1 citations 2.5x more likely with answer-first; 140% boost — Prompt behavior
27. **Google AI Overviews Official Docs** — https://support.google.com/webmasters/answer/14307505 — Implementation guide
28. **Goodie AI 2.2M Prompts Analysis** — Transparent pricing = 3.2x visibility, Wikipedia cited 18.4%, YouTube 23.3% — Broad dataset
29. **Semrush AI Visibility Study (2025)** — Brand mentions r=0.65 with AI citations; domain authority r=0.23 — New metrics
30. **Perplexity Citation Patterns (2025)** — Listicles = 50% of top citations, FAQ schema = 3.2x AI Overview likelihood — Engine-specific
31. **SearchEngineJournal AI Search Roundup** — Ongoing coverage of AI search evolution — Current awareness
32. **ContentStudio AI Content Analysis (2024)** — How AI engines evaluate content structure — Practical insights

### Content Quality & E-E-A-T

33. **Google Quality Rater Guidelines (leaked 2023)** — Trustworthiness "most important member of E-E-A-T" — Internal rubric
34. **HireGrowth Topic Cluster Research (2025)** — Topic clusters drive ~30% more organic traffic — Architecture impact
35. **FirstPageSage Helpful Content Analysis** — System folded into core ranking (March 2024) — Operationalization
36. **Contentsquare 15K Page Engagement Analysis** — Scroll depth 40-50% + 2-3 min dwell optimal — UX data
37. **6sense Buyer Shortlist Research (4K respondents)** — 95% of winners on Day 1 shortlist; brand awareness 77% — Buyer behavior
38. **TrustRadius Buyer's Choice 2024** — Best value 66% cite driver; trust required 75% of reviewers — Review platform data
39. **Gartner Magic Quadrant Methodology** — Product quality typically highest-weighted Execute criterion — Enterprise standard
40. **Forrester Wave Buyer Evaluation Framework** — Current Offering spans 8-25+ sub-criteria, all rooted in features — B2B standard

### User Engagement & Behavioral Signals

41. **DollarPocket Dwell Time Study** — r=0.84 correlation with rankings — Strongest behavioral metric
42. **Ahrefs AI Overview CTR Impact Study** — 58% CTR reduction from AI Overviews — SERP feature impact
43. **CTR Study / Siteliner Organic CTR Curves (2025)** — Position #1=42.9% CTR, top 3=68.7% total — Click distribution
44. **NavBoost Confirmation (DOJ Trial)** — "goodClicks", "badClicks", "lastLongestClicks" over 13-month window — Mechanical explanation
45. **Contentsquare 15K Site Analysis** — Bounce rates 12% higher on mobile; session duration correlation with rankings — Mobile vs. desktop
46. **BrightEdge Engage Platform Study** — Time-on-page, scroll depth, return visitor rate tracked across 1K+ sites — Proprietary data

### Brand, Entity & Competitive Data

47. **Moz Brand Signals Research** — Brand mentions now correlate with rankings as domain authority declined — Emerging factor
48. **Knowledge Panel CTR Study** — 38% CTR vs 28% for organic #1 — Entity value
49. **Featured Snippet Analysis (Ahrefs)** — Entity-optimized content 50% more likely to appear — Snippet qualification
50. **Enamix Entity SEO Guide** — How to build knowledge panels, entity recognition — Tactical implementation

---

## Appendix B: Scoring Factor Quick Reference Table

| Category | Sub-Factor | Weight | Threshold (Good) | Data Source | Automated? |
|----------|-----------|--------|-----------------|-----------|-----------|
| **Page Health** | CWV Pass | 40% | All 3 metrics pass | Lighthouse | ✅ |
| | Accessibility | 25% | WCAG AA, ARIA labels | Lighthouse + a11y MCP | ✅ |
| | Security | 15% | HTTPS, CSP, HSTS, no secrets | SquirrelScan | ✅ |
| | Mobile | 10% | Responsive, 48px+ taps, readable fonts | PageSpeed mobile_audit | ✅ |
| | Best Practices | 10% | No deprecated APIs, <3 console errors | Lighthouse | ✅ |
| **Discoverability** | Keyword Breadth | 25% | 30+ keywords ranking | SEMRush | ✅ |
| | Traffic Volume | 25% | 100+ monthly organic visits | SEMRush | ✅ |
| | Position Quality | 25% | 50%+ keywords in top 10 | SEMRush | ✅ |
| | Momentum | 25% | 10%+ 6-month growth | SEMRush | ✅ |
| **SEO Factors** | Core Meta Tags | 30% | Title + description + canonical + h1 | SquirrelScan | ✅ |
| | On-Page Structure | 25% | 5+ headings, 5-15 internal links, 80%+ image alt | SquirrelScan | ✅ |
| | Crawlability | 20% | In sitemap, no canonical chains, robots.txt clear | SquirrelScan | ✅ |
| | Structured Data | 15% | JSON-LD present, schema valid | SquirrelScan | ✅ |
| | URL Structure | 10% | <75 chars, hyphens, keyword-relevant | SquirrelScan | ✅ |
| **AEO Factors** | Semantic Completeness | 30% | Covers topic from 4+ angles, r>0.88 vs competitors | Custom embedding analysis | ⚠️ |
| | Answer-First Format | 25% | Summary in <100 words, quick answer up front | Custom NLP | ⚠️ |
| | Citation-Ready | 20% | Author + dates + sources + E-E-A-T visible | HTML parsing | ⚠️ |
| | Multi-Modal | 15% | 5+ images + tables/data viz + video optional | HTML parsing | ✅ |
| | Source Authority | 10% | Previously cited in AI, topical ranking, brand mentions | Custom crawling | ⚠️ |
| **Page Quality** | E-E-A-T Signals | 35% | Author bio, dates, credentials, about page link | HTML parsing | ⚠️ |
| | Content Structure | 30% | 2000+ words, 8+ headings, 8th grade reading level | DataForSEO parsing | ✅ |
| | Visual Quality | 15% | Alt text on 80%+ images, proper formats, dimensions | HTML parsing | ✅ |
| | Link Integrity | 10% | No broken links, descriptive anchors, HTTPS only | Link crawling | ✅ |
| | Content Depth | 10% | Word count appropriate for topic, internal links | DataForSEO parsing | ✅ |
| **Engagement** | Dwell Time | 40% | 90-180s median | GA4 + server logs | ⚠️ |
| | CTR | 25% | 4-7% from SERP | GSC | ⚠️ |
| | Scroll Depth | 20% | 40-70% median | GA4 | ⚠️ |
| | Return Visitor % | 10% | 25-50% repeat traffic | GA4 | ⚠️ |
| | Interaction Depth | 5% | 2-4 interactions per session | GA4 events | ⚠️ |
| **Additional** | Brand Signals | 45% | Domain > 2yrs, brand mentions in AI | Custom tracking | ⚠️ |
| | Entity Strength | 30% | Knowledge Panel, Wikipedia, entity schema | Knowledge API | ⚠️ |
| | Accessibility+ | 15% | WCAG AAA, PDF tagging, video captions | Manual audit | 🤖 |
| | i18n | 10% | hreflang correct, language URLs, translated content | HTML parsing | ✅ |

**Legend:** ✅ = Fully automated | ⚠️ = Semi-automated (needs validation) | 🤖 = Manual

---

## Appendix C: Data Source Mapping & APIs

### Scoring Factor → Data Source Mapping

| Scoring Factor | Primary Source | API | Cost | Refresh | Notes |
|---|---|---|---|---|---|
| CWV (LCP, INP, CLS) | Lighthouse | PageSpeed API | Free (limited)/Paid | On-demand | Lab data (synthetic); CrUX for real-user data |
| Accessibility Score | Lighthouse | PageSpeed API | Free/Paid | On-demand | a11y MCP provides detailed violations |
| Security Headers | SquirrelScan | Custom crawler | Paid | On-demand | Includes HTTPS, CSP, HSTS, leaked secrets |
| Mobile Responsiveness | PageSpeed Mobile | PageSpeed API | Free/Paid | On-demand | Viewport, tap targets, font sizes |
| Best Practices | Lighthouse | PageSpeed API | Free/Paid | On-demand | Deprecated APIs, console errors |
| Keyword Rankings | SEMRush | org_research / url_research | Paid ($119+) | Daily | 6-month trends, position data |
| Organic Traffic | SEMRush | organic_research | Paid ($119+) | Monthly | Estimated; GSC is ground truth |
| SERP Position | DataForSEO | ranked_keywords | Paid | Daily | Position per keyword, search volume |
| SERP Features | DataForSEO | ranked_keywords | Paid | Daily | AI Overview presence, featured snippets |
| Meta Title/Desc | SquirrelScan | on_page_audit | Paid | On-demand | Presence, length, character encoding |
| H1/Heading Structure | SquirrelScan/DataForSEO | on_page audit | Paid | On-demand | Hierarchy validation, uniqueness |
| Internal Links | SquirrelScan/DataForSEO | on_page parsing | Paid | On-demand | Count, anchor text, relevance |
| Image Alt Text | SquirrelScan | on_page audit | Paid | On-demand | Coverage %, alt text quality |
| Canonical URL | SquirrelScan | on_page audit | Paid | On-demand | Presence, correctness, chains |
| JSON-LD Schema | SquirrelScan | on_page audit | Paid | On-demand | Types, validity, schema.org compliance |
| Sitemap Inclusion | SquirrelScan/robots.txt | on_page audit | Paid | On-demand | Listed in XML sitemap |
| robots.txt | SquirrelScan/custom | crawl audit | Paid | On-demand | No blocking of important paths |
| URL Structure | SquirrelScan | on_page audit | Paid | On-demand | Length, hyphens, keyword relevance |
| Word Count | DataForSEO | content parsing | Paid | On-demand | Character and word totals |
| Readability | Custom NLP | Flesch-Kincaid, Gunning Fog | Free/Internal | On-demand | Grade level, passive voice % |
| E-E-A-T Signals | SquirrelScan + HTML parsing | E-E-A-T category | Paid | On-demand | Author, dates, credentials, about link |
| Author Attribution | HTML parsing | Custom crawler | Internal | On-demand | Byline presence and specificity |
| Publish/Update Dates | HTML parsing | Custom crawler | Internal | On-demand | Visible on page or in metadata |
| Broken Links | SquirrelScan | link audit | Paid | On-demand | Outbound link health check |
| HTTPS Enforcement | SquirrelScan | security audit | Paid | On-demand | Full site HTTPS, no mixed content |
| Dwell Time | GA4 + server logs | GA4 API / custom logs | Free (GA4) | Real-time | Time between SERP click and return |
| CTR from SERP | Google Search Console | GSC API | Free | Daily | Organic clicks ÷ impressions |
| Scroll Depth | GA4 | GA4 API | Free | Real-time | % of viewport scrolled |
| Return Visitor % | GA4 | GA4 API | Free | Real-time | New vs. returning user ratio |
| Interactions | GA4 | GA4 API + custom events | Free | Real-time | Clicks, plays, form submissions |
| Domain Age | WHOIS | Custom WHOIS parser | Free | Static | Registration date |
| Brand Mentions | AI probing + custom tracking | Custom LLM + ChatGPT API | Paid | Monthly | Frequency in AI responses |
| Knowledge Panel | Knowledge Graph API | KG API (requires license) | Paid | Monthly | Entity recognition and features |
| Wikipedia Presence | Wikipedia API | MediaWiki API | Free | Monthly | Page existence and links |
| hreflang Tags | SquirrelScan | on_page audit | Paid | On-demand | Syntax, correctness, bidirectionality |
| Semantic Completeness | Custom embeddings | OpenAI Embeddings API | Paid | Monthly | Cosine similarity vs. competitors |
| Answer-First Formatting | Custom NLP | Custom LLM | Internal | On-demand | Heading structure + summary detection |
| Multi-Modal Content | HTML parsing | Custom crawler | Internal | On-demand | Image, table, video counts |
| AI Citations | Custom probing | ChatGPT / Perplexity / Claude APIs | Paid | Monthly | Manual tracking or automated bot |

### Recommended Tool Stack for Content OS & CheckThat

**Essential (MVP):**
- Lighthouse / PageSpeed API (free tier for start)
- SquirrelScan (paid)
- Google Search Console API (free)
- Google Analytics 4 API (free)
- SEMRush API ($119+/month)

**High-value adds (Phase 2):**
- DataForSEO API (ranked keywords, SERP features)
- Custom crawlers (semantic analysis, AEO scoring)
- AI probing infrastructure (ChatGPT, Perplexity, Claude APIs)

**Nice-to-have (enterprise):**
- Knowledge Graph API (entity strength)
- Copilot Search integration (emerging)
- Bard integration (declining, focus on ChatGPT/Claude/Gemini)

---

## Conclusion

This scoring methodology synthesizes 1000+ sources and real-world ranking data into a unified framework that works for both traditional SEO and AI search. The weights are grounded in correlation studies, Google's own leaked documents, and antitrust trial testimony.

The key insight: **SEO and AEO are now co-dominant.** A page optimized only for traditional search (keyword-focused, link-building optimized) will underperform in AI. A page optimized for AEO (semantic completeness, answer-first structure, citation-ready formatting) but ignored by traditional SEO rankings is worthless.

Content OS and CheckThat must support both. The scoring model does.

**Start with Page Health and SEO.** These are fully automatable and represent foundational quality.

**Add Discoverability to validate inputs.** If pages are scoring well but not ranking, the problem is likely external (backlinks, domain authority).

**Build AEO factors carefully.** This is the new frontier. The tools and signals are still evolving. But the Surfer 36M study proves semantic completeness and answer-first formatting are now dominant factors.

**Track engagement where possible.** Dwell time (r=0.84) is nearly as strong as backlinks. It's the most actionable behavioral signal.

**Invest in explainability.** Customers need to understand *why* a page scores 45, not just *that* it scores 45. Diagnostic views showing "Health: 60, Quality: 30, SEO: 85, AEO: 55" tell the story of what to fix.

This is your north star. Build to this.

