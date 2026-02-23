# SEO Ranking Factors Study Guide

<metadata>
purpose: Evidence-based study guide on SEO ranking factors — what Google actually measures, what studies prove, and what practitioners should prioritize in 2025-2026
audience: B2B content marketing practitioners, agency leaders
related: knowledge/content/keyword-optimization-clustering-study-guide-v1.md, knowledge/aeo/README.md
domain: content, SEO
confidence: research
sensitivity: public
context_tier: 2
last_updated: 2026-02-19
</metadata>

> **For:** Content marketing practitioners and agency leaders who need to separate signal from noise on what actually drives rankings
> **Goal:** Build an evidence-based understanding of ranking factors grounded in studies, leaks, trial testimony, and practitioner testing — not speculation
> **Time Investment:** 8–12 hours
> **Last Updated:** February 2026

---

## How to Use This Guide

This guide is organized by evidence quality. Part 1 covers what we now know from Google's own leaked documents and antitrust trial testimony — the closest thing to ground truth we've ever had. Part 2 breaks down the major correlation studies from 2025-2026 with their specific data points. Parts 3-8 go deep on each factor category with the latest evidence. Part 9 covers AI search visibility factors — the new frontier. Part 10 gives you the practitioner playbook.

When you see a correlation value (like r=0.84), remember: correlation ≠ causation. But directional signals from million-keyword datasets are worth paying attention to, especially when multiple studies converge.

---

## Part 1: What Google Actually Confirmed — The Leak & The Trial

### The Google Content Warehouse API Leak (May 2024)

In May 2024, over 14,000 internal Google API documents leaked via GitHub, exposing 2,596 modules with ranking attributes Google had publicly denied for years. Rand Fishkin and Mike King published the analysis. Google confirmed the leak was real.

**What the leak revealed:**

**NavBoost — Click signals are a top ranking signal.** NavBoost is mentioned 84 times in the leaked documents. It uses 13 months of rolling click data to boost, demote, or reinforce rankings. The system tracks "goodClicks," "badClicks," and "lastLongestClicks." It geo-fences data by country and state, and differentiates mobile from desktop. Google had denied using click data for rankings for over a decade.

**siteAuthority exists.** Despite years of Google spokespeople denying any "domain authority" metric, the leak shows Google computes a feature called "siteAuthority" stored as part of Compressed Quality Signals on a per-document basis. It's not identical to Moz's Domain Authority, but it functions similarly — aggregating page-level signals into a site-wide quality score.

**Chrome data is used.** The documentation shows Chrome browsing data feeds into ranking calculations, despite public denials.

**A sandbox for new sites exists.** A "hostAge" attribute is used to handle newer domains differently, contradicting Google's denial of a sandbox effect.

**siteFocusScore and siteRadius.** These metrics assess how concentrated a site's content is around core topics — confirming the concept of topical authority as a measurable signal.

**Small personal sites get special treatment.** A feature called "smallPersonalSite" suggests Google can identify and potentially boost smaller, more personal websites.

**Freshness signals are granular.** Multiple freshness-related attributes track how recently content was created, modified, and how "fresh" the information itself is — not just the page date.

**Critical caveat from the leak analysis community:** These documents show what Google *measures*, not necessarily what it *weighs* or how it *uses* each signal. Fields can exist without being active ranking factors. The architecture could change at any time.

---

### The DOJ Antitrust Trial (2024-2025)

Google's VP of Search, Pandu Nayak, testified under oath about ranking architecture. This is the most authoritative public account of how Google Search actually works.

**The Two Master Signals: Quality (Q\*) and Popularity (P\*).**

Every webpage gets scored on two fundamental dimensions:

1. **Quality (Q\*)** — Assesses trustworthiness and authority. Heavily influenced by PageRank, which measures a site's "distance from a known good source." This is effectively a trust chain — sites closely linked to known-trustworthy sources score higher.

2. **Popularity (P\*)** — Measures how widely visited and well-linked a page is. Directly powered by Chrome visit data and NavBoost user interaction signals.

**PageRank is still central.** Under oath, Nayak confirmed PageRank remains a key quality signal, settling the periodic industry debate about whether links still matter.

**Anchor text provides "a valuable clue"** to page relevance — confirmed in testimony.

**Freshness boosting is real-time.** A system called "Instant Glue" uses a 24-hour rolling log of user interaction data to elevate fresh results for time-sensitive queries.

**Machine learning refines, not replaces.** RankBrain and BERT act as final refinement layers for semantic understanding. They don't replace the foundational link + click + quality signals — they make those signals more effective.

**User interaction signals are "important."** Nayak confirmed that how users interact with search results — click-through rates, time on page, and return-to-SERP behavior — directly influence rankings through NavBoost.

**The ruling:** In August 2024, Judge Mehta ruled Google a monopolist. The September 2025 remedies imposed behavioral restrictions including banning exclusive default search agreements (Google paid Apple $18 billion in 2021 alone for Safari default placement).

---

## Part 2: The Major Correlation Studies (2025-2026)

### Study 1: Surfer SEO — 1 Million SERPs (2025)

Surfer analyzed 1 million search results using Spearman's rank correlation. Key findings:

- **Keyword density shows almost no correlation** with rankings. Exact-match keyword usage is statistically irrelevant. The era of keyword stuffing is empirically dead.
- **Exact match domains (EMDs) still correlate strongly** — domains containing the target keyword still perform significantly better in the dataset.
- **Keywords in URL path** showed almost no correlation with rankings.
- **TTFB and page load time** showed growing correlation over successive studies, confirming speed as a persistent ranking factor.
- **Content comprehensiveness** (measured by topic coverage relative to competitors) showed moderate positive correlation.

---

### Study 2: DollarPocket — 10 Million Search Results (2025)

The largest ranking factor correlation study of 2025 analyzed 10 million search results and proposed weighted factor categories:

| Factor Category | Weight | Change from 2024 |
|----------------|--------|-------------------|
| Page Experience Signals | 28% | ↑ (fastest growing) |
| Content Quality | 25% | Stable |
| Backlinks | 22% | ↓ (was 27% in 2024) |
| User Engagement | 15% | ↑ (was 11%) |
| Other Factors | 10% | — |

**Specific correlation data:**
- High-quality referring domains: r = 0.85
- Dwell time: r = 0.84
- Mobile page speed: r = 0.83
- Bounce rate: r = -0.68 (lower is better)
- Desktop page speed: r = 0.61
- Pages with LCP under 1.0 second rank 7.5 positions higher on average than those over 4.0 seconds
- Fully AI-generated content (80-100% AI likelihood) averages position 16.8 vs. position 5.2 for mostly human content

---

### Study 3: FirstPageSage — Weighted Algorithm Analysis (Q1 2025)

FirstPageSage maintains a continuously updated weighted model based on observed algorithm behavior. Their Q1 2025 weights:

| Factor | Weight | Trend |
|--------|--------|-------|
| Consistent Publication of Satisfying Content | ~23% | #1 factor for 7+ years |
| Keywords in Meta Title Tag | 14% | ↓ (was 15%) |
| Niche Expertise (Topical Authority) | 13% | Stable |
| Backlinks | 13% | ↓ (was 15%) |
| Searcher Engagement | 12% | ↑ (was 11%) |
| Trustworthiness | ~8% | Stable |
| Mobile-Friendliness | ~5% | Stable |
| Page Speed | ~3% | Stable |
| Internal Links | ~3% | Stable |
| 23 additional factors | ~1% combined | Includes schema, header tags, URL keywords |

**Key insight from FirstPageSage:** Some factors are "prerequisite" — you won't be penalized for having them, but you *will* be penalized for lacking them. These include: keyword in meta title, searcher engagement, trustworthiness, mobile-friendliness, and page speed.

---

### Study 4: Semrush — Text Relevance Dominance

Semrush's ongoing studies found that **text relevance** (how well content matches query intent) appeared in 90.6% of top-10 results — the single most consistent factor.

---

### Study 5: Patrick Stox (Ahrefs) — 1 Million Keywords (2025)

Analysis of 1 million keywords confirmed links remain a crucial ranking factor with significant correlation values between rankings and various link metrics (referring domains, domain-level authority, anchor text relevance).

---

### Where Studies Agree (Consensus Factors)

Across all major 2025-2026 studies, the factors that consistently show strong correlation:

1. **Content relevance and depth** — universally the strongest signal
2. **High-quality backlinks** — declining in weight but still significant
3. **User engagement/satisfaction signals** — growing fastest
4. **Page speed / Core Web Vitals** — consistent tiebreaker in competitive SERPs
5. **Topical authority / niche expertise** — increasingly important
6. **Brand signals** — emerging as a major factor for both traditional and AI search

---

## Part 3: Content Quality & E-E-A-T

### E-E-A-T: Framework, Not Direct Signal

Google has been explicit: E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) is not a direct ranking factor. It's a quality evaluation framework that describes what Google's ranking systems try to detect and reward. As John Mueller stated in 2025: "You can't sprinkle some experiences on your web pages."

But the indirect evidence is overwhelming:

- After the December 2025 Core Update, generic content farms saw significant traffic drops while sites demonstrating experience and expertise saw 23% gains.
- 96% of AI Overview citations come from verified authoritative sources.
- The leaked PQ (Page Quality) rating system from quality rater guidelines appears in Google's internal documentation — confirming these principles are operationalized.

### How Google Operationalizes Each E-E-A-T Component

**Experience:** Google looks for evidence of firsthand interaction — unique images, personal case studies with specific data, mention of tools/products personally used, and context cues like "Tested in September 2025." Google quantifies how difficult content is to replicate (low-effort generic content → lower rankings) and measures novelty (prioritizing information unavailable elsewhere).

**Expertise:** Measured through content depth, accuracy, and creator credentials. Google detects how focused or diluted a domain is — highly focused sites produce stronger expertise signals. A vector representation of thematic alignment classifies a site's niche, and internal linking structure reveals which pages are pillars of expertise.

**Authoritativeness:** Built externally through recognition — other credible sources cite you, link to you, or mention you. Combined reputation metrics include links, mentions, content quality, and engagement. PageRank still matters, especially at the domain level.

**Trustworthiness:** Google's own Quality Rater Guidelines state this is "the most important member of the E-E-A-T family because untrustworthy pages have low E-E-A-T no matter how Experienced, Expert, or Authoritative they may seem." Trust is evaluated through both editorial quality and technical integrity (HTTPS, transparent authorship, corrections policy).

### YMYL Amplification

For Your Money or Your Life topics — anything that could influence medical decisions, legal actions, or financial choices — Google demands stronger E-E-A-T signals. Formal credentials matter more than personal experience for medical/legal/financial content. For product reviews and how-to content, personal experience carries more weight.

### The Content Quality Signals That Moved in 2025

**Helpful Content is now baked into core updates.** Google stopped launching separate Helpful Content Updates because the system was folded into core ranking in March 2024. The signal is sitewide — one section of low-quality content can drag down an entire domain.

**AI-generated content penalties are real but nuanced.** The DollarPocket study found fully AI-generated content averages position 16.8 vs. 5.2 for mostly human content. Google's position is technology-neutral ("we focus on quality, not how content is produced"), but the data suggests AI-only content underperforms — likely because it lacks the firsthand experience and original insight signals that E-E-A-T rewards.

---

## Part 4: Backlinks & Authority

### The Declining-but-Still-Critical Signal

Backlinks have been declining in algorithmic weight for a decade. The trajectory is clear:

- Once over 50% of the algorithm (Google's early years)
- FirstPageSage tracked: 15% → 13% (2024-2025)
- DollarPocket tracked: 27% → 22% (2024-2025)
- Gary Illyes (Google, 2023): Links "aren't one of the top three ranking factors anymore"
- Google officially dropped the word "important" from link documentation, now describing links as just "a signal"

But the evidence also shows they still matter significantly:

- Patrick Stox's 1-million-keyword study (2025) found significant correlation between link metrics and rankings.
- Gotch SEO's analysis of 11.8 million results: 85% of page-one sites had 1,000+ backlinks from different domains.
- 91% of content fails to rank without quality backlinks (industry aggregate data).
- 95% of SEO professionals in 2025 still rank backlinks as "critical" or "very important" — though 72% note the shift to quality over quantity.

### Quality Over Quantity — The Data

The shift from "more links = better" to "right links = better" is the defining change:

- PageRank was confirmed in antitrust testimony as measuring "distance from a known good source" — it's a trust chain, not a popularity contest.
- Topical relevance of linking domains matters more than raw domain authority scores.
- A single editorial link from a respected, relevant publication can outperform hundreds of directory or guest post links.
- The leaked API documents show Google evaluates link velocity, anchor text distribution, and the authority of linking pages — not just counts.

### The Causality Question

The elephant in the room: do links cause rankings, or do high-ranking pages attract more links? Most studies measure correlation, not causation. The honest answer is: both. Links help pages rank (confirmed by Google's testimony), AND high-ranking pages attract more links naturally. This creates a compounding effect.

### Backlinks in AI Search

Semrush's AI citation study found link quality shows correlation values of r=0.65 (Pearson) and r=0.57 (Spearman) with AI search visibility — the strongest relationship in their AI ranking report. Domain authority alone shows weaker correlation (r=0.23-0.36). The quality of your backlink profile matters for AI citations, even as traditional search weight declines.

---

## Part 5: User Behavior & Engagement Signals

### NavBoost: The Confirmed Click System

The API leak and antitrust trial confirmed what the SEO industry suspected for years: Google uses click data extensively through the NavBoost system.

**How NavBoost works:**
- Uses 13 months of rolling click data from Google Search
- Tracks three key signal types: "goodClicks" (satisfactory visits), "badClicks" (quick returns to SERP), and "lastLongestClicks" (the final click that satisfied the user)
- Geo-fences data by country and state/province
- Differentiates between mobile and desktop behavior
- Functions as one of Google's strongest ranking signals

**The "lastLongestClick" is particularly powerful** — it's a direct countermeasure to clickbait. If users click a result and stay (long dwell time), it's a good click. If they bounce back quickly, it's a bad click. The *last* click that kept the user satisfied signals the winning result.

### Dwell Time is Contextual

Dwell time (time between clicking a search result and returning to the SERP) matters, but context determines what "good" means:

- For a query like "what is the capital of Australia," 5 seconds of dwell time is satisfactory — the user got their answer.
- For "how to build a backyard deck," 5 seconds signals failure — the content didn't deliver on a complex need.
- Google's systems understand this distinction. They analyze expected dwell time by query type, aggregating patterns across thousands of users.

### Pogo-Sticking as a Negative Signal

Pogo-sticking — when a user clicks a result, immediately returns to the SERP, and clicks a different result — is a strong negative satisfaction signal. Unlike bounce rate (which doesn't specify where the user went), pogo-sticking specifically indicates the user rejected your content in favor of a competitor's.

### December 2025 Core Update Enhanced Behavioral Weighting

Google's December 2025 core update specifically enhanced the weighting of behavioral signals — including pogo-sticking, dwell time, and return visits. This aligns with the broader trend: user engagement signals increased from 11% to 15% weight in the DollarPocket study (2024 → 2025), making it the fastest-growing factor category.

### Organic CTR as a Ranking Signal

Click-through rate from the SERP itself is a confirmed input to NavBoost. Pages with compelling titles and meta descriptions that earn higher CTR get a ranking boost — which in turn earns more clicks, creating a virtuous cycle. This makes title tag optimization one of the highest-ROI activities in SEO, even though its direct algorithmic weight has declined slightly.

---

## Part 6: Technical SEO & Core Web Vitals

### Core Web Vitals: The Tiebreaker

The current Core Web Vitals metrics (as of 2026):

| Metric | What It Measures | Good Threshold |
|--------|-----------------|----------------|
| LCP (Largest Contentful Paint) | Loading performance | < 2.5 seconds |
| INP (Interaction to Next Paint) | Responsiveness | < 200 milliseconds |
| CLS (Cumulative Layout Shift) | Visual stability | < 0.1 |

**INP replaced FID in March 2024.** Unlike FID (which only measured the first interaction), INP tracks every single interaction throughout a visitor's session and reports the worst 2-5% of interactions. This makes it harder to game — you can't just optimize the first click.

**Ranking impact:** Industry analysis estimates Core Web Vitals weigh approximately 10-15% in Google's algorithm. They function as a tiebreaker: poor CWV won't tank a site with excellent content and authority, but they prevent you from reaching full ranking potential. When competing pages have similar content and authority, CWV performance determines the winner.

**The data is compelling:**
- Pages with LCP under 1.0 second rank 7.5 positions higher on average than pages over 4.0 seconds (DollarPocket study).
- Mobile page speed shows r=0.83 correlation with rankings vs. r=0.61 for desktop.
- Rakuten optimized CWV and saw 53% increase in revenue per visitor, 33% higher conversion rate.
- redBus improved INP by 72% → 7% increase in sales.
- One agency reported clients gaining 5-10 positions for competitive keywords from CWV improvements alone.

**WordPress reality check:** As of July 2025, only 44% of WordPress sites pass all three CWV metrics on mobile. This means over half the web's most popular CMS platform is underperforming — creating opportunity for sites that optimize.

### Mobile-First Indexing

Mobile-first indexing is now fully established. Google primarily uses the mobile version of your content for indexing and ranking. With mobile devices representing ~58% of all web traffic in 2026, mobile CWV performance is the primary factor in Google's page experience evaluation.

### HTTPS

SSL/HTTPS has been a confirmed ranking signal since 2014. In 2026 it's effectively a prerequisite — not having HTTPS creates a penalty rather than having it creating a boost.

### Crawlability & Indexing

Technical SEO fundamentals remain prerequisites: proper robots.txt, clean sitemap.xml, canonical tags, hreflang for international content, and efficient site architecture that ensures Google can discover and index all important pages. The API leak revealed Google's crawling system (Trawler) and indexing system (Alexandria) as distinct microservices — confirming that crawl efficiency directly impacts how quickly and completely your content enters Google's index.

---

## Part 7: Brand Signals & Entity SEO

### Brand Is the New Authority

Rand Fishkin's takeaway from the API leak: "Build a notable, popular, well-recognized brand in your space, outside of Google search." This isn't just pundit advice — the data supports it.

**Branded search volume** (people searching for your brand name) is a strong trust signal. It indicates real-world awareness and preference that can't be easily manufactured.

**Unlinked brand mentions** function as signals even without hyperlinks. Google is sophisticated enough to associate textual brand mentions with your entity, contributing to overall authority scores.

**Entity optimization** is the modern expression of brand SEO. Google doesn't rank pages in isolation — it ranks entities. Your website, Google Business Profile, social profiles, reviews, mentions, and user behavior are evaluated together as a unified entity.

### The Entity Framework (Dixon Jones / InLinks)

Entity SEO operates on the principle that Google's Knowledge Graph understands relationships between concepts, people, products, and organizations. When your content clearly establishes what entity you are, what entities you're connected to, and what authority you have, Google can rank you more confidently.

**Practical entity signals:**
- Consistent NAP (Name, Address, Phone) across all platforms
- Schema markup defining your organization, authors, products, and content
- Author pages with verifiable credentials and cross-linked profiles
- Wikipedia and Wikidata presence (for established brands)
- Consistent brand messaging across website, social media, and third-party profiles

### Brand Signals in AI Search

Brand matters even more for LLM-based search. When AI systems (ChatGPT, Perplexity, Google AI Overviews) generate answers, they rely on entity relationships to build accurate summaries. Brands that are frequently and consistently mentioned in authoritative contexts get cited more. Semrush found that brand popularity (measured by search volume) has the highest correlation with AI chatbot mentions.

---

## Part 8: Topical Authority & Content Architecture

### The Evidence That Topical Authority Is Real

The API leak confirmed Google uses "siteFocusScore" and "siteRadius" metrics to assess how concentrated a site is around core topics. SiteFocus measures depth within a subject area; siteRadius evaluates how far content strays from that focus.

**The Graphite study (2024)** found pages with high topical authority gain traffic 57% faster than those with low authority.

**HubSpot's pillar page study** documented a 43% increase in organic traffic after implementing topic clusters.

**HireGrowth's 2025 analysis** found content grouped into clusters drives ~30% more organic traffic and holds rankings 2.5x longer than standalone pieces.

### How to Measure Topical Authority

There's no single metric. The best approaches:

**Topic Share (Kevin Indig, Growth Memo):** Measure the percentage of traffic you capture from all keywords in a topic space. Compare to competitors. This is the most actionable measurement framework available. You can calculate it using the "Traffic share by domains" report in Ahrefs' Keywords Explorer.

**Topical Authority Ratio (SEOwind):** Measures how much content a site produces for a specific subject vs. how well it performs in SERPs. If you've written extensively but aren't ranking, your content may lack authority signals.

**Content Coverage Scoring:** Map all subtopics within your core topics. Score each on a 0-3 scale (0 = no coverage, 1 = thin, 2 = solid, 3 = best-in-class). Identify gaps. Build a content plan to fill them.

### Building Topical Authority: The Architecture

The pillar-cluster model remains the most proven content architecture:

1. **Pillar page:** Comprehensive overview of the core topic at a top-level URL
2. **Cluster pages:** Deep dives on each subtopic, interlinked to the pillar
3. **Internal linking:** Every cluster links to the pillar; the pillar links to every cluster
4. **Consistent publication:** Google rewards sites that publish regularly on their topic — this is FirstPageSage's #1 factor

The key principle: depth within your niche beats breadth across many topics. A 50-page site deeply covering one topic domain can outperform a 5,000-page site with shallow coverage across hundreds of topics.

---

## Part 9: AI Search Visibility — The New Frontier

### The Scale of the Shift

The numbers that define the transition from traditional to AI search:

- Zero-click searches grew from 56% in 2024 to 69% in 2025
- AI Overviews now appear in ~16% of US desktop searches
- Google's top organic CTR dropped 32% after AI Overviews (from 28% to 19%)
- Gartner predicts 25% of organic traffic will shift to AI chatbots by 2026
- ChatGPT has 700 million weekly users processing 2.5 billion+ prompts daily
- Forrester: 89% of B2B buyers use generative AI as a central source in their buying process

### AI Overview Ranking Factors (2025-2026 Studies)

Based on Surfer SEO's analysis of 36 million AI Overviews, the AI Mode Boost study of 15,847+ results, and other 2025-2026 research:

**Semantic completeness is the #1 factor (r=0.87).** Content that provides complete, self-contained answers in 134-167 word units is 4.2x more likely to appear in AI Overviews than incomplete content.

**Multi-modal content integration (r=0.92).** Pages combining text + images + video + structured data see 156% higher AI Overview selection rates. In 2024, text-only content could still compete. By 2025, 78% of featured sources include multi-modal elements.

**Real-time factual verification.** Content with verifiable citations and cross-referenced data sources shows 89% higher selection probability.

**Traditional SEO metrics are declining for AI.** Traditional ranking correlation dropped to r=0.18 (from r=0.43 pre-2024). 47% of AI Overview content comes from pages ranking below position 5. Domain authority shows negative correlation (r=-0.12) in some verticals.

**Content freshness matters.** 85% of AI Overview citations were published in the last two years. 44% are from 2025. Consistent publication accounts for approximately 23% of the algorithm's weight.

### Who Gets Cited in AI?

Surfer's 36-million AI Overview analysis found extreme concentration:
- YouTube (~23.3%), Wikipedia (~18.4%), and Google.com (~16.4%) dominate citations
- Reddit, LinkedIn, and Facebook follow
- Top 20 domains account for 66.18% of all citations
- Top 5 domains account for 38.13%

**Where in your content gets cited:**
- 44.2% of LLM citations come from the first 30% of text (the intro)
- 31.1% from the middle third
- 24.7% from the last third

This means: put your best, most citable answers early in the content.

### Traffic Impact of AI Overviews

The data cuts both ways:
- Organic CTR drops 61% on searches that trigger AI Overviews (from 1.76% to 0.61%)
- BUT: pages cited inside AI Overviews earn 35% more organic clicks and 91% more paid clicks than uncited competitors
- Major websites experienced 8-55% traffic declines year-over-year, largely attributed to AI Overviews
- Traditional news outlets suffered the most severe losses

**The strategic implication:** Being cited in AI is now more valuable than ranking #1 and not being cited. This fundamentally changes what "winning" looks like in SEO.

---

## Part 10: The Practitioner Playbook

### The Evidence-Based Priority Stack

Based on synthesizing all the research above, here's what the data says matters most — ordered by evidence strength and impact:

**Tier 1: Foundation (Must Have)**
1. **Content quality and relevance** — The single most correlated factor across every study. Publish content that comprehensively and accurately answers the searcher's query. Match the content format to the intent.
2. **E-E-A-T signals** — Not a direct signal, but the framework that Google's ranking systems operationalize. Focus on demonstrating genuine experience and expertise, not performing it.
3. **Technical health** — Mobile-first, fast loading (CWV in green), HTTPS, crawlable, properly indexed.

**Tier 2: Amplifiers (Significant Impact)**
4. **Backlinks from authoritative, relevant sources** — Quality over quantity. One editorial link from a respected industry publication > 100 directory links.
5. **Topical authority / content architecture** — Build pillar-cluster structures. Demonstrate depth within your niche.
6. **User satisfaction signals** — If NavBoost is measuring goodClicks and lastLongestClicks, your content needs to *actually satisfy* the user. This is not gameable — it requires genuine value.

**Tier 3: Competitive Edge**
7. **Brand signals** — Branded search volume, entity consistency, unlinked mentions. Hard to build but compounding.
8. **Schema markup & structured data** — Not a direct ranking factor, but drives rich results (82% higher CTR), and is increasingly important for AI citation.
9. **Content freshness** — Quarterly updates for key content. 85% of AI citations come from content published in the last 2 years.
10. **Multi-modal content** — Text + images + video + structured data. 156% higher AI Overview selection for multi-modal pages.

**Tier 4: Emerging (Monitor and Invest)**
11. **AI search optimization** — Answer-first formatting, citation-ready content, semantic completeness.
12. **Entity optimization** — Knowledge Graph presence, author entities, consistent cross-platform identity.

### What to Stop Doing

The evidence is equally clear about what doesn't work:

- **Keyword density optimization** — Surfer's 1M SERP study: zero correlation.
- **Keywords in URL path** — Near-zero correlation.
- **Pursuing low-quality link volume** — Google's own employees say "very few links" are needed; quality is what matters.
- **Publishing AI-only content** — Average position 16.8 vs. 5.2 for human content. AI can assist, but human expertise and editing are essential.
- **Ignoring user satisfaction** — NavBoost is a confirmed top signal. If users bounce, your rankings will erode regardless of your backlink profile.

### How Great Practitioners Think About Ranking Factors

**They think in systems, not factors.** Great SEO doesn't come from optimizing one signal. It comes from building a system where content quality, technical health, user satisfaction, authority, and brand signals all reinforce each other.

**They weight evidence over opinion.** When an SEO guru says "X is the most important factor," great practitioners ask: what study? What sample size? Correlation or causation? Replicated?

**They understand the prerequisite/amplifier distinction.** Some factors are prerequisites — you get penalized for lacking them, but not boosted for having them (HTTPS, mobile-friendliness, title tags). Other factors are amplifiers — they create competitive advantage (topical authority, brand signals, content depth). Knowing the difference prevents wasted effort.

**They track their own data.** The best ranking factor study is the one you run on your own sites. Track what changes you make, measure the impact, and build your own evidence base.

---

## Part 11: Local SEO Ranking Factors (Supplement)

### Whitespark's 2026 Local Search Ranking Factors Report

The definitive local SEO study, released November 2025, surveyed 47 experts who rated 187 ranking signals. For the first time, it also covered AI search visibility factors for local.

**Top Local Pack Factors:**
1. **Google Business Profile signals** (~32% of local pack ranking) — Primary category, business name, reviews, photos, posts, Q&A
2. **Reviews & review recency** (~15%) — Steady stream of new reviews matters more than total count
3. **On-page signals** — Local landing pages with dense, factual content
4. **Backlink signals** — Links from locally relevant, authoritative sources
5. **Entity & brand signals** — Consistent NAP, schema markup, cross-platform identity

**The 90-day recency principle:** Google now evaluates recent behavior more heavily than historical completeness. What a business did in the last 90 days matters more than what it did two years ago. If you stop getting new reviews, local rankings slip.

**Google's three official local factors:** Relevance, distance, and prominence. Prominence is explicitly described as being influenced by links, reviews, and overall web presence.

---

## Appendix A: Curated Source Library

### Major Studies & Reports

| Study | Org | Sample Size | Year | Key Finding |
|-------|-----|------------|------|-------------|
| 1M SERPs Analysis | Surfer SEO | 1M SERPs | 2025 | Keyword density: zero correlation. Speed: growing correlation |
| 10M Search Results | DollarPocket | 10M results | 2025 | Page experience: 28% weight. Dwell time: r=0.84 |
| Google Algorithm Weights | FirstPageSage | Ongoing model | Q1 2025 | Satisfying content: #1 factor for 7+ years |
| 1M Keyword Link Study | Patrick Stox / Ahrefs | 1M keywords | 2025 | Links remain significant correlation with rankings |
| 11.8M Results Analysis | Gotch SEO | 11.8M results | 2025 | 85% of page-one sites have 1,000+ referring domains |
| Text Relevance Study | Semrush | Ongoing | 2025 | Text relevance appears in 90.6% of top-10 results |
| 36M AI Overviews | Surfer SEO | 36M AIO | 2025 | Semantic completeness r=0.87; multi-modal r=0.92 |
| 15,847 AI Overview Results | AI Mode Boost | 15,847 results | 2025 | 47% of cited content ranks below position 5 |
| Local Ranking Factors | Whitespark | 47 experts, 187 signals | 2025/2026 | GBP signals: ~32% of local pack ranking |
| Topical Authority | Graphite | Not disclosed | 2024 | High TA pages gain traffic 57% faster |
| Topic Clusters | HireGrowth | Not disclosed | 2025 | Clusters: 30% more traffic, 2.5x longer rankings |
| Pillar Page Impact | HubSpot | Internal data | 2024 | 43% increase in organic traffic |
| CWV Business Impact | Rakuten | Internal data | 2025 | 53% revenue per visitor increase after CWV optimization |
| AI Citation Study | Semrush | Not disclosed | 2025 | Link quality r=0.65 for AI visibility; DA only r=0.23-0.36 |

### Primary Source Documents

| Document | What It Reveals |
|----------|----------------|
| Google Content Warehouse API Leak (May 2024) | 14,014 attributes across 2,596 modules. NavBoost, siteAuthority, siteFocusScore confirmed |
| DOJ v. Google Antitrust Trial Testimony (2024-2025) | Q* + P* ranking architecture, PageRank confirmation, NavBoost click signals |
| Google Search Quality Rater Guidelines (latest) | E-E-A-T framework, YMYL standards, page quality evaluation criteria |
| Google Search Central Documentation | Official ranking guidance, structured data requirements, Core Web Vitals thresholds |

### Key Practitioners

| Name | Affiliation | Known For |
|------|------------|-----------|
| Rand Fishkin | SparkToro | API leak analysis, brand-first SEO philosophy |
| Mike King | iPullRank | API leak technical analysis, information retrieval expertise |
| Kevin Indig | Growth Memo | Topic Share framework, topical authority measurement |
| Eli Schwartz | Independent | Product-Led SEO, business-aligned strategy |
| Dixon Jones | InLinks | Entity SEO, Knowledge Graph optimization |
| Cyrus Shepard | Zyppy | Scientific ranking factor studies |
| Darren Shaw | Whitespark | Local search ranking factors research |
| Lily Ray | Amsive | E-E-A-T expertise, algorithm update analysis |
| Barry Schwartz | Search Engine Roundtable | Algorithm update tracking and documentation |
| Glenn Gabe | G-Squared Interactive | Core update recovery analysis |
| Patrick Stox | Ahrefs | Large-scale ranking studies |
| Andy Chadwick | Keyword Insights | SERP-based clustering, cannibalization research |

### Books

| Title | Author | Why It's Essential |
|-------|--------|-------------------|
| Product-Led SEO | Eli Schwartz | Business-aligned SEO strategy beyond keyword chasing |
| Entity SEO | Dixon Jones | How Knowledge Graph changes ranking factor dynamics |
| The Art of SEO (4th ed.) | Enge, Spencer, Stricchiola | Comprehensive reference on all ranking factor categories |
| The Executive SEO Playbook | Jessica Bowman | Enterprise-level SEO implementation and buy-in |

### Newsletters & Blogs

| Source | Why It's Essential |
|--------|-------------------|
| Growth Memo (Kevin Indig) | Strategic frameworks, topical authority, data-driven analysis |
| Search Engine Roundtable (Barry Schwartz) | Real-time algorithm update tracking |
| Search Engine Land | Industry news, study summaries, expert analysis |
| Search Engine Journal | Practitioner guides, algorithm history, technical tutorials |
| Ahrefs Blog | Data-driven studies, tool methodology transparency |
| Semrush Blog | Ranking factor studies, competitive analysis |
| iPullRank Blog (Mike King) | Technical SEO, information retrieval, API leak analysis |
| Hobo Web (Shaun Anderson) | DOJ trial analysis, leak documentation, Google contradictions |

---

## Appendix B: The Ranking Factor Evidence Hierarchy

Not all evidence is created equal. Use this hierarchy when evaluating claims:

**Level 1: Confirmed by Google (under oath or in official docs)**
- PageRank as quality signal (antitrust testimony)
- NavBoost click signals (antitrust testimony + API leak)
- Core Web Vitals as ranking signal (official documentation)
- E-E-A-T as evaluation framework (Quality Rater Guidelines)
- HTTPS as ranking signal (official blog post, 2014)
- Mobile-first indexing (official documentation)

**Level 2: Revealed by leaked documentation**
- siteAuthority metric
- siteFocusScore / siteRadius (topical authority)
- Chrome data usage
- hostAge (sandbox effect)
- smallPersonalSite feature
- Freshness attributes

**Level 3: Supported by large-scale correlation studies**
- Content relevance/depth correlation (Semrush, DollarPocket)
- Backlink correlation (Stox, Gotch SEO)
- Page speed correlation (Surfer, DollarPocket)
- Dwell time correlation (DollarPocket)
- AI Overview selection factors (Surfer 36M, AI Mode Boost)

**Level 4: Supported by practitioner testing and case studies**
- Topic cluster traffic impact (HubSpot, HireGrowth)
- Cannibalization resolution (Keyword Insights cases)
- Schema markup CTR impact (SearchPilot A/B tests)
- CWV business impact (Rakuten, redBus)

**Level 5: Expert consensus without formal study**
- Brand signals importance
- Anchor text diversity
- Content freshness cadence
- Internal linking optimization

**Level 6: Speculation / outdated claims**
- Social signals as direct ranking factor
- Keyword density thresholds
- Exact URL keyword matching
- Domain age as a significant factor

---

## Appendix C: Learning Path

### Quick Start (If You Only Have 3 Hours)

1. Read Mike King's API leak analysis on iPullRank — 30 min
2. Read Supple Digital's "6 Takeaways for SEOs from Google's Antitrust Trial" — 20 min
3. Read FirstPageSage's weighted ranking factors breakdown — 20 min
4. Read Surfer SEO's AI Citation Report (surferseo.com/blog/ai-citation-report/) — 30 min
5. Read Whitespark's 2026 Local Search Ranking Factors summary — 20 min
6. Do Exercise 1 (Factor Audit) below — 60 min

### Full Curriculum (8-12 Hours Over 3 Weeks)

**Week 1: Ground Truth**
- Read this study guide in full — 90 min
- Study the API leak analysis (Mike King + Rand Fishkin) — 2 hours
- Read the Hobo Web DOJ trial documentation — 1 hour
- Do Exercise 2 (Evidence Grading) — 60 min

**Week 2: The Studies**
- Read Surfer's 1M SERP study (surferseo.com/blog/ranking-factors-study/) — 30 min
- Study DollarPocket's 10M results analysis — 30 min
- Read Semrush's branding + SEO analysis (semrush.com/blog/seo-branding/) — 30 min
- Read the Search Engine Land backlinks importance analysis — 20 min
- Do Exercise 3 (Correlation Challenge) — 90 min

**Week 3: Applied Practice**
- Read Kevin Indig's topical authority measurement guide (growth-memo.com/p/how-to-measure-topical-authority) — 30 min
- Study the AI Overview ranking factors deep dive — 45 min
- Read Hobo Web's E-E-A-T guide (hobo-web.co.uk/what-is-e-e-a-t-in-seo/) — 30 min
- Do Exercise 4 (Client Audit) — 2 hours

### Deep Dive (If You Want Mastery)
- Read the full Google Search Quality Rater Guidelines (170+ pages)
- Study the complete API leak documentation on GitHub
- Read Dixon Jones's Entity SEO book
- Build a custom topical authority scorer using Kevin Indig's framework
- Attend or watch recordings from SearchLove, BrightonSEO, or MozCon

---

## Appendix D: Practice Exercises

**Exercise 1: Factor Audit.** Pick a client site. For each Tier 1-3 factor in the Priority Stack (Part 10), score the site 1-5. Identify the three weakest areas. Build a 90-day improvement plan focused on those three.

**Exercise 2: Evidence Grading.** Find 10 SEO articles that make claims about ranking factors. For each claim, assign an evidence level using the hierarchy in Appendix B. How many claims are Level 1-2 vs. Level 5-6? This exercise builds critical thinking about SEO advice.

**Exercise 3: Correlation Challenge.** Take the DollarPocket correlation values (dwell time r=0.84, backlinks r=0.85, mobile speed r=0.83). For each, brainstorm: could this be reverse causation? What would a controlled experiment look like? What confounding variables exist? This builds the analytical muscle to evaluate studies properly.

**Exercise 4: Client Audit.** For a real client, run a complete ranking factor audit: CWV scores (PageSpeed Insights), backlink profile (Ahrefs/Semrush), topical authority score (Kevin Indig's method), content quality assessment (E-E-A-T checklist), brand signal strength (branded search volume, mentions). Produce a one-page strategic recommendation prioritizing the highest-impact improvements.

---

## Appendix E: Research Notes

Full research scratchpad with raw findings, source ratings, and gap analysis: `pipeline/scratchpad/2026-02-19-seo-ranking-factors-research-scratchpad.md`
