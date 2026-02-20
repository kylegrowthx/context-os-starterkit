# Keyword Optimization & Clustering Study Guide

<metadata>
purpose: Comprehensive study guide on keyword optimization and clustering — frameworks, tool methodologies, evidence, and best practices
audience: B2B content marketing practitioners, agency leaders
related: ../context/voice/writing-style-context-v2.md, knowledge/aeo/README.md
domain: content, SEO
confidence: research
sensitivity: public
context_tier: 2
last_updated: 2026-02-19
</metadata>

> **For:** Content marketing practitioners who already do keyword work — and want to understand *why* things work, not just *how* to click buttons
> **Goal:** Build a defensible methodology for keyword optimization and clustering that's grounded in evidence, tool logic, and practitioner wisdom
> **Time Investment:** 5–8 hours
> **Last Updated:** February 2026

---

## How to Use This Guide

Start with Part 1 if you want the mental models. Skip to Part 2 if you want frameworks you can use this week. Part 3 breaks down how the major tools actually think about clustering — useful for choosing tools and explaining your methodology to clients. Part 4 covers what the evidence says. Part 5 is the emerging frontier: AEO and AI search. The appendices have your reading list and learning path.

---

## Part 1: Foundations — How to Think About Keywords in 2026

### The Core Mental Shift: Keywords → Topics → Intent → Entities

The discipline has evolved through four distinct eras, and understanding each one prevents you from using outdated tactics dressed up in modern language.

**Era 1: String Matching (pre-2013).** Google matched exact query strings to on-page text. Keyword density mattered. You could rank by repeating a phrase enough times. This is dead, but the instinct lives on in content briefs that obsess over exact-match counts.

**Era 2: Semantic Understanding (2013–2019).** Google's Hummingbird update (2013) introduced semantic search — understanding meaning, not just matching strings. BERT (2019) deepened this by processing the context of every word in a query. The implication: Google can now understand that "best running shoes for flat feet" and "top sneakers for overpronation" serve the same intent, even though they share almost no words.

**Era 3: Topical Authority (2019–2024).** Google started rewarding sites that demonstrate comprehensive expertise on a topic, not just individual pages that target individual keywords. Kevin Indig's "Topic Share" framework captures this well — it's not about ranking for one keyword, it's about owning a meaningful share of all keywords in a topic space. A 2024 study by Graphite found that pages with high topical authority gain traffic 57% faster than those with low authority.

**Era 4: Entity & Answer Optimization (2024–present).** Google's Knowledge Graph, AI Overviews, and LLM-based search (ChatGPT, Perplexity) now understand entities — people, products, concepts — not just keywords. Dixon Jones's work on Entity SEO captures this shift: Google is ranking entities, not pages. Your keyword strategy must account for how you show up in AI-generated answers, not just blue links.

### Core Concepts Every Practitioner Should Know

**Search Intent** is the reason behind a query. The standard four-type framework (informational, navigational, transactional, commercial investigation) originated from Andrei Broder's 2002 taxonomy and was expanded by academic research. The key insight: more than 80% of web queries are informational, according to a study by Jansen, Booth, and Spink published on ResearchGate. But intent is not always clean — a query like "best project management software pricing" contains both commercial investigation and transactional signals simultaneously.

**Keyword Clustering** is grouping related keywords that should be targeted on the same page. The fundamental logic: if Google ranks the same pages for two different keywords, those keywords share intent and belong together. If Google shows different results, they need separate pages. This is the foundation all serious clustering tools are built on.

**Keyword Cannibalization** happens when multiple pages on your site compete for the same keyword. It's one of the most common and most damaging SEO mistakes at scale. A Keyword Insights case study found that fixing cannibalization for a travel client increased organic traffic by 110%. A separate e-commerce case study by Orka Socials showed a 200% traffic increase after resolving cannibalization issues — in under a month.

**Topical Authority** is the degree to which a site demonstrates comprehensive expertise on a topic. Kevin Indig measures this as "Topic Share" — the percentage of traffic a site captures from all keywords in a topic space. For example, analyzing ecommerce-related keywords, Shopify holds about 11% Topic Share vs. Bigcommerce at 10%.

### Common Misconceptions to Unlearn

**"Higher search volume = better keyword."** A keyword with 100 monthly searches and high purchase intent can outperform a 10,000-volume vanity term. Volume is a starting filter, not a decision criterion.

**"Keyword difficulty scores are accurate."** They're directional at best. Ahrefs' KD is based primarily on referring domain counts (intentionally excluding on-page factors). Semrush uses a multi-factor approach including domain authority. A study comparing them found that Ahrefs frequently scores 0 for keywords that are genuinely competitive but have competitors with weak backlink profiles. Neither tool's score reliably predicts whether *you* can rank — because they don't know your domain's specific authority and content quality.

**"One keyword per page."** This is a relic of the string-matching era. Modern pages should target clusters of semantically related keywords. The clustering approach — where pages are optimized for groups of similar keywords — lets pages rank for significantly more keywords and signals topical depth to search engines.

**"Keyword research is a one-time task."** Research shows 31% of high-value keywords change significantly in intent or volume every six months. The discipline requires ongoing monitoring and iteration.

---

## Part 2: Frameworks & Process

### Framework 1: The SERP Overlap Method (Industry Standard)

**What it is:** The most reliable method for determining whether two keywords belong on the same page. Compare the top 10 Google results for two keywords. The more URLs they share, the more likely they should be clustered together.

**How it works:**
- Pull the top 10 organic results for each keyword
- Count how many URLs appear in both result sets
- Apply a threshold to decide: same page or separate pages?

**Threshold guidelines (from practitioner consensus):**
- **70%+ overlap** (7+ shared URLs): High confidence — same page
- **40–70% overlap** (4–6 shared URLs): Likely same page, but validate manually
- **30–40% overlap** (3–4 shared URLs): Borderline — check intent carefully
- **Below 30%** (0–2 shared URLs): Different intent — separate pages

The industry sweet spot is 40–60% overlap (4–6 shared URLs out of 10). Most SERP-based tools default to around 30–40% and let you adjust upward for tighter clusters.

**Critical caveat from Keyword Insights co-founder Andy Chadwick:** Google no longer consistently shows 10 traditional organic links due to AI Overviews, Featured Snippets, and other SERP features. Keyword Insights adjusted their maximum threshold from 10 to 7 to account for this. Your thresholds may need similar recalibration.

**When to use:** Any time you need to decide whether two keywords belong on the same page or need separate content. This is the backbone of content planning at scale.

---

### Framework 2: The Topic Cluster / Pillar Page Model (HubSpot)

**What it is:** A content architecture where one comprehensive "pillar page" covers a broad topic, linked to multiple "cluster pages" that go deep on subtopics. The internal linking structure signals to Google that your site has depth and authority on the topic.

**Evidence it works:**
- HubSpot's own study found websites with topic clusters saw a 43% increase in organic traffic
- A HireGrowth 2025 analysis found content grouped into clusters drives about 30% more organic traffic and holds rankings 2.5x longer than standalone pieces
- One e-commerce implementation grew organic blog traffic from 500 to 190,000 visitors per month
- Agency-side implementations have shown 7–10x organic growth over 12 months

**How to build one:**
1. Identify your core topic (the pillar)
2. Research all subtopics and questions within that topic
3. Cluster the subtopics using SERP overlap analysis
4. Create the pillar page covering the full topic at a high level
5. Create cluster pages going deep on each subtopic
6. Interlink everything — every cluster page links to the pillar, the pillar links to every cluster page

**Key best practice:** The pillar page should be ungated (no forms or passwords blocking it), sit at a top-level URL, and cover the topic comprehensively enough to rank on its own — while leaving room for cluster pages to go deeper on specifics.

---

### Framework 3: Kevin Indig's Topic-First SEO

**Source:** Growth Memo newsletter (growth-memo.com)

**What it is:** A strategic framework that inverts the traditional keyword-first approach. Instead of starting with keyword lists and building pages, you start with the topics your audience cares about, map the full conceptual territory, and then use keywords as the tactical layer.

**Core principles:**
- **Topics are the atomic unit of SEO, not keywords.** Google understands concepts through the Knowledge Graph. Your strategy should map to concepts, not strings.
- **Topic Share is your KPI.** Measure the percentage of traffic you capture from all keywords in a topic space. Compare this to competitors to identify where you're winning and where you have gaps.
- **ICP alignment over volume.** Prioritize keywords that match your Ideal Customer Profile's questions, even if volume is lower. Relevance beats volume for B2B.

**Practical application:** Score how well you currently cover each subtopic within your core topics. Focus resources on topics where Google already sees you as an authority — that's where you'll get the fastest ROI. Then expand strategically into adjacent topics.

---

### Framework 4: Eli Schwartz's Product-Led SEO

**Source:** *Product-Led SEO* (book, 2021)

**What it is:** A philosophy that argues SEO strategy should be built around your product's value proposition and user experience, not keyword volume. The product itself becomes the SEO asset.

**Core argument:** Starting with keyword research tools — sorting by volume and difficulty — leads you to the same generic content everyone else is publishing. Instead, start with user problems. What non-obvious content would prospects on the outskirts of your current user base find valuable? That's where differentiation lives.

**Key principle for keyword work:** Don't ask "what keywords have volume?" Ask "what problems does our product solve that people are searching for?" The keywords emerge from the product-market fit, not from a spreadsheet sorted by search volume.

**Why it matters for agencies:** This framework helps you move clients beyond "we need to rank for [obvious keyword]" toward strategies that actually differentiate them and build engaged audiences — not just traffic.

---

### Framework 5: The Intent-Clustering Matrix

**What it is:** A practical framework for organizing keywords along two dimensions: topic similarity AND intent similarity. Two keywords might be topically identical but have completely different intents — and vice versa.

**The classic example (from Keyword Insights):** "Vaporizer parts" and "Vaporizer accessories" look semantically identical. NLP-based clustering would group them together. But SERP analysis shows only 11.8% overlap — Google treats them as fundamentally different intents, requiring separate pages.

**How to use it:**
1. Cluster keywords by SERP overlap first (this captures intent)
2. Then organize clusters into topic groups (this captures topical relationships)
3. The result: a two-level hierarchy — topic groups containing intent-specific clusters
4. Each cluster becomes a page; each topic group becomes a content hub

This two-level approach prevents both cannibalization (targeting the same intent on multiple pages) and content gaps (missing intents within a topic).

---

## Part 3: How the Major Tools Think

Understanding tool methodologies helps you choose the right tool, interpret outputs correctly, and explain your approach to clients.

### Ahrefs: Parent Topic Clustering

**Methodology:** Ahrefs clusters keywords using a proprietary metric called "Parent Topic." For any keyword, they look at the #1 ranking page and find which keyword sends the most traffic to that page. That keyword becomes the Parent Topic, and all keywords sharing the same Parent Topic get grouped together.

**Speed advantage:** Can cluster up to 10,000 keywords in seconds — because it's leveraging existing ranking and traffic data, not running live SERP comparisons.

**Key limitation (acknowledged by Ahrefs):** Less accurate than full SERP-overlap tools because it only looks at the top-ranking result, not the entire SERP. This makes it fast but means it can miss nuances where the #2–10 results would tell a different story.

**SERP Similarity Score:** Ahrefs also offers a 0–100 score comparing two specific keywords. High score = cluster. Low score = don't. Middle = use judgment.

**Best for:** Quick, directional clustering during early research. Fast enough to iterate and explore. Not the final word for high-stakes content planning.

---

### Semrush: Multi-Signal Clustering (Keyword Strategy Builder)

**Methodology:** Semrush's Keyword Strategy Builder clusters based on SERP overlap plus additional signals: semantic similarity, search volume patterns, and SERP feature presence. It automatically identifies pillar page candidates and subpage opportunities.

**Unique feature:** Semrush factors in your specific domain's authority and topical relevance — other tools generally don't. This gives you a personalized view of keyword difficulty.

**Key limitation:** Uses a "black box" approach with no user-adjustable SERP overlap threshold. Limited to 2,000 keywords per run. Critics have noted it sometimes merges keywords that arguably need separate pages (e.g., "ai content marketing" and "ai content marketing tools" in one cluster with only 2 overlapping URLs).

**Best for:** Integrated workflow from research to content planning, especially if you're already in the Semrush ecosystem.

---

### Keyword Insights: Configurable SERP Clustering

**Methodology:** Pure SERP-based clustering with full user control. For each keyword, it examines the top 7 results (adjusted down from 10 due to SERP feature proliferation). Keywords sharing 40%+ of URLs in common get clustered together — and you can adjust this threshold.

**Co-founder Andy Chadwick's philosophy:** "We don't use NLP to do the clustering. We use live SERP data." The reasoning: NLP clustering can be "intent blind," grouping keywords that look semantically similar but trigger completely different SERPs.

**Unique features:**
- Adjustable overlap threshold (so you can run tight or loose clusters)
- Supports up to 200,000 keywords per run
- Identifies cannibalization automatically
- Builds "hubs" (clusters of clusters) using NLP on top of the SERP clusters

**Best for:** High-volume, high-precision clustering work. The gold standard for SERP-based methodology with maximum control.

---

### Surfer SEO: Content-First Clustering

**Methodology:** Combines SERP reverse-engineering, NLP entity analysis, and intent classification. Analyzes the top 5–20 ranking pages for a keyword across 500+ on-page signals (word count, keyword usage, NLP entities, heading structure, image frequency).

**Content Score (0–100):** A live, dynamic indicator of how well your content is optimized compared to what's already ranking. Based on correlation analysis of top-ranking pages — not a direct measure of quality.

**NLP engine:** Uses Google Cloud NLP and its own engine to extract entities and sentiment from top-ranking content. Suggests terms to include based on what high-ranking pages have in common.

**Key caution:** The Content Score can encourage over-optimization. Chasing A+ grades can lead to unnatural keyword stuffing. Practitioners note that a naturally-written B+ piece sometimes outperforms a forced A+.

**Best for:** On-page optimization once you've already decided what keyword cluster to target. Not the primary clustering tool — it's the optimization layer.

---

### Clearscope: Comprehensiveness Grading

**Methodology:** Analyzes the top 20 search results for a target keyword, then grades your content (A+ to F) on relevance and comprehensiveness compared to competitors. Uses NLP from Google Cloud, IBM Watson, and OpenAI GPT to identify semantically related concepts — not just synonym matching.

**Key philosophy:** The grade reflects topic coverage, not keyword density. It identifies the concepts and entities that top-ranking pages discuss and measures whether your content addresses them.

**Best for:** Content editing and quality assurance. Particularly valuable for teams where writers need clear, measurable targets for topic coverage.

---

### DIY: Python + SERP API Clustering

For teams that want full control (or can't justify tool costs), building your own clustering pipeline is viable:

**Core approach:**
1. Compile your keyword list
2. Pull top 10 SERP results for each keyword via API (Serper.dev, SerpApi, etc.)
3. Build a graph: keywords are nodes, edges connect keywords that share ranking URLs
4. Apply clustering algorithm (community detection via NetworkX, or simple overlap thresholds)
5. Output clustered keyword groups

**Common libraries:** NetworkX (graph-based clustering), scikit-learn (K-means, DBSCAN), sentence-transformers (for semantic layer), Serper.dev or SerpApi (SERP data).

**Cost consideration:** SERP-based clustering via APIs costs money — roughly $2,900 for 1 million keywords. For small-to-medium projects, Serper.dev's free tier (2,500 queries) is sufficient.

**Practical tutorials:** Oncrawl published a Google Colab notebook walkthrough. Search Engine Journal has a step-by-step Python guide focused on intent clustering. PEMAVOR open-sourced a graph-based approach using NetworkX community detection.

---

## Part 4: What the Evidence Says

### Academic Research

**Meta-analysis of SEO effectiveness (2024, ResearchGate):** Analyzed 10 studies conducted between 2022–2024. Found SEO implementation consistently associated with significant increases in organic rankings and traffic, with an effect size (d) of 1.049 (high). Content quality, keyword optimization, and backlinks were the three variables with significant influence on SEO effectiveness.

**Long-term keyword economics (Journal of Business Research, 2022):** Analyzed the long-run cost evolution of branded vs. unbranded organic keywords. Provided empirical evidence that long-term keyword strategy (choosing the right keywords to invest in over years, not months) has measurable economic impact on estimated CPC savings.

**SEO evolution study (Cogent Business & Management, 2025):** Found content quality, technical SEO, backlink quality, and mobile friendliness all had significant positive impact on search rankings. Notably, the study frames the evolution from keyword matching to user experience as the defining shift.

### Industry Studies & Data Points

**Topic clusters vs. standalone content (HireGrowth, 2025):** Content grouped into clusters drives ~30% more organic traffic and holds rankings 2.5x longer than standalone pieces.

**HubSpot pillar page study:** 43% increase in organic traffic after implementing topic clusters.

**Graphite topical authority study (2024):** Pages with high topical authority gain traffic 57% faster than those with low authority.

**Keyword volatility (industry data):** 31% of high-value keywords change significantly in intent or volume every 6 months. This is the strongest argument for treating keyword research as an ongoing practice, not a one-time project.

**Keyword Insights cannibalization case studies:** 110% traffic increase for a travel client after fixing cannibalization. A franchise company found 17 pieces of cannibalizing content for a single topic because content strategy wasn't centralized.

### The Evidence Gap

Most "studies" in SEO are industry reports and case studies, not controlled experiments. There's relatively little rigorous academic research on keyword clustering specifically. The strongest evidence comes from:
- Correlation studies (Semrush's KD accuracy study of 120,000 keywords)
- Before/after case studies (HubSpot, Keyword Insights, Helium SEO)
- Industry data aggregations (HireGrowth, Graphite)

This means: the directional signals are strong, but treat any specific number with appropriate skepticism. Your own testing and measurement matters more than any external benchmark.

---

## Part 5: The Emerging Frontier — AEO & AI Search

### Why Keyword Strategy Must Evolve for AI

The ground is shifting. Zero-click searches grew from 56% in 2024 to 69% in 2025. Google AI Overviews now appear in 16% of all US desktop searches. Google's top organic CTR dropped 32% after AI Overviews rolled out (from 28% to 19%). Gartner predicts 25% of organic traffic will shift to AI chatbots by 2026.

This doesn't make keyword optimization irrelevant — it changes what "winning" looks like. Increasingly, the goal isn't just ranking in blue links, but being cited as a source in AI-generated answers.

### Answer Engine Optimization (AEO) Principles

**Citation-readiness over keyword density.** AI systems surface the clearest, most contextually relevant answers — regardless of traditional keyword rankings. Structure content so AI can extract and cite your answers directly.

**Entity clarity over keyword matching.** AI engines understand entities (people, companies, products, concepts) through knowledge graphs. Your content needs to clearly establish what entity you are, what entities you're connected to, and what authority you have.

**Answer-first formatting.** Add concise, direct answers near the top of content pieces. Follow with depth and nuance. This serves both AI extraction and human reading patterns.

**Structured data and schema.** AI engines heavily rely on structured data to understand content. Schema markup, clear heading hierarchies, and FAQ formatting all increase your chances of being cited.

### Practical Implications for Keyword Clustering

Your clustering work doesn't change fundamentally — you still need to understand which keywords share intent and which need separate pages. But you need to add a layer:

1. **For each cluster, identify the core question it answers.** This becomes your AEO target.
2. **Structure content to answer that question clearly in the first 100 words.** Then go deep.
3. **Include structured data** that makes the answer machine-extractable.
4. **Update content quarterly.** AI engines favor fresh, maintained content. Forrester reports 89% of B2B buyers use generative AI as a central source in their buying process — your content needs to be what those AI systems cite.

---

## Part 6: Skills & Practice

### What Great Keyword Strategists Do Differently

**They think in architectures, not lists.** Average practitioners produce keyword lists. Great ones produce content architectures — topic maps with clear hierarchy, intent mapping, and internal linking strategies.

**They validate with SERPs, not assumptions.** Before committing to a content plan, they manually check SERPs for the most important keywords. Tools give you direction; SERP validation gives you confidence.

**They balance volume with intent quality.** They know when a 500-volume keyword with high commercial intent is worth more than a 50,000-volume informational keyword.

**They treat keyword research as continuous.** Not a quarterly project, but an ongoing practice of monitoring rankings, spotting cannibalization, identifying new opportunities, and pruning outdated targets.

**They can explain the "why" to non-SEO stakeholders.** They don't just say "we need to target this keyword." They explain the intent, the competitive landscape, the content gap, and the business case.

### How to Practice

**Exercise 1: SERP Dissection.** Pick any keyword relevant to a client. Manually analyze the top 10 results. What types of content rank? What intents are being served? What formats dominate (listicles, guides, tools, product pages)? Do this for 10 keywords across different intents.

**Exercise 2: Clustering Challenge.** Take a list of 100 keywords in one topic area. Cluster them manually using SERP overlap. Then run them through a tool. Compare your manual clusters to the tool output. Where do they agree? Where do they diverge? Why?

**Exercise 3: Cannibalization Audit.** Pick a client site with 50+ pages. Use Google Search Console to identify keywords where multiple URLs receive impressions. Determine which cases are true cannibalization vs. intentional multi-ranking. Build a remediation plan.

**Exercise 4: Topic Authority Map.** For one core topic, map every subtopic and question. Use keyword research to quantify the opportunity. Score your current coverage (are there existing pages? How do they rank?). Identify the gaps. Build a content plan to fill them.

---

## Appendix A: Curated Source Library

### Books

| Title | Author | Why It's Essential |
|-------|--------|-------------------|
| Product-Led SEO | Eli Schwartz | Challenges keyword-first thinking; builds business-aligned SEO strategy |
| Entity SEO | Dixon Jones | Foundational for understanding how Google's Knowledge Graph changes keyword strategy |
| The Art of SEO (4th ed.) | Enge, Spencer, Stricchiola | Comprehensive reference covering keyword research, technical SEO, and link building |
| The SEO Blueprint | Ryan Stewart | Systems-focused; practical keyword research process for agencies |
| SEO for Growth | Jantsch & Singleton | Connects keyword strategy to lead generation and business growth |

### Newsletters & Blogs

| Source | Author/Org | Why It's Essential |
|--------|-----------|-------------------|
| Growth Memo (growth-memo.com) | Kevin Indig | Topic-first SEO, topical authority measurement, strategic frameworks |
| Ahrefs Blog (ahrefs.com/blog) | Ahrefs team | Data-driven keyword research, clustering tutorials, tool methodology transparency |
| Semrush Blog (semrush.com/blog) | Semrush team | Keyword clustering guides, KD methodology studies, content strategy |
| Keyword Insights Blog (keywordinsights.ai/blog) | Andy Chadwick et al. | Deep clustering methodology, cannibalization case studies, SERP analysis |
| Clearscope Blog (clearscope.io/blog) | Clearscope team | Topical authority measurement, content optimization benchmarks |
| Search Engine Journal (searchenginejournal.com) | Various | Python clustering tutorials, practitioner guides, algorithm update analysis |

### Tools

| Tool | Type | Best For |
|------|------|----------|
| Keyword Insights | SERP-based clustering | High-precision clustering with configurable thresholds; up to 200K keywords |
| Ahrefs Keywords Explorer | Parent Topic clustering | Fast directional research; SERP similarity scoring |
| Semrush Keyword Strategy Builder | Multi-signal clustering | Integrated content planning with domain-specific difficulty |
| Surfer SEO | Content optimization + clustering | On-page optimization after clustering decisions are made |
| Clearscope | Content grading | Comprehensiveness benchmarking during writing and editing |
| Serper.dev / SerpApi | SERP data APIs | DIY Python-based clustering |
| ContentGecko | Free SERP clustering | Budget-friendly SERP-based clustering |

### Key Practitioners

| Name | Affiliation | Known For |
|------|------------|-----------|
| Kevin Indig | Growth Memo, former Shopify | Topic Share metric, topic-first SEO framework |
| Eli Schwartz | Independent consultant | Product-Led SEO philosophy |
| Andy Chadwick | Keyword Insights, Snippet Digital | SERP-based clustering methodology, cannibalization research |
| Cyrus Shepard | Zyppy, former Moz | SEO scientific studies, ranking factors research |
| Dixon Jones | InLinks | Entity SEO, Knowledge Graph optimization |

---

## Appendix B: Key Decisions Checklist

Use this when planning keyword strategy for a new client or topic:

**1. Architecture Decision**
- [ ] Have I mapped the full topic space (not just obvious keywords)?
- [ ] Does my architecture use topic clusters or standalone pages?
- [ ] Have I identified pillar page candidates?

**2. Clustering Decision**
- [ ] Am I using SERP overlap to validate clusters (not just semantic similarity)?
- [ ] What overlap threshold am I using, and why?
- [ ] Have I checked for cannibalization in existing content?

**3. Intent Decision**
- [ ] For each cluster, have I confirmed the dominant intent via SERP analysis?
- [ ] Am I separating informational, commercial investigation, and transactional keywords?
- [ ] Do my content formats match the intent? (guides for informational, comparison pages for commercial, product pages for transactional)

**4. Prioritization Decision**
- [ ] Am I prioritizing by business impact, not just volume?
- [ ] Have I considered ICP alignment?
- [ ] Am I accounting for existing authority? (Easier to win where Google already trusts you)

**5. AEO Decision**
- [ ] For key clusters, have I identified the core question to answer?
- [ ] Is content structured for AI extraction (answer-first, schema markup)?
- [ ] Am I planning for content freshness (quarterly updates)?

---

## Appendix C: Learning Path

### Quick Start (If You Only Have 3 Hours)

1. Read Kevin Indig's "Topic-First SEO" article (growth-memo.com) — 20 min
2. Read Keyword Insights' clustering guide (keywordinsights.ai/blog/keyword-clustering-guide/) — 30 min
3. Read Ahrefs' keyword clustering tutorial (ahrefs.com/blog/keyword-clustering/) — 20 min
4. Do Exercise 1 (SERP Dissection) for 10 keywords in your niche — 90 min
5. Read the AEO comprehensive guide on CXL (cxl.com/blog/answer-engine-optimization-aeo-the-comprehensive-guide/) — 30 min

### Full Curriculum (5–8 Hours Over 2 Weeks)

**Week 1: Foundations & Frameworks**
- Read this study guide in full — 60 min
- Read Eli Schwartz's Product-Led SEO (book) — 3 hours
- Study Kevin Indig's topical authority measurement framework (growth-memo.com) — 30 min
- Do Exercise 2 (Clustering Challenge) — 90 min

**Week 2: Tools, Practice & AEO**
- Read Keyword Insights' full clustering methodology and case studies — 45 min
- Study the SERP overlap threshold research (ContentGecko semantic vs SERP comparison) — 30 min
- Do Exercise 3 (Cannibalization Audit) — 90 min
- Read HubSpot's AEO trends article (blog.hubspot.com/marketing/answer-engine-optimization-trends) — 20 min
- Do Exercise 4 (Topic Authority Map) for one client — 90 min

### Deep Dive (If You Want Mastery)
- Build a DIY clustering pipeline in Python using the Oncrawl tutorial
- Read Dixon Jones's Entity SEO book
- Study the Semrush KD accuracy study (120,000 keyword analysis)
- Run a topic authority scorer using Kevin Indig's workflow
- Test your clustering methodology against 3 different tools and compare outputs

---

## Appendix D: Research Notes

Full research scratchpad with all raw findings, source ratings, and gap analysis: `pipeline/scratchpad/keyword-optimization-clustering-research-scratchpad.md`
