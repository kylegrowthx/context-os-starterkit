# GrowthX Engagement Manager Operating Guide to SEO

<metadata>
purpose: Distilled operating guide for EMs. Mental models, site scoring, content scoring.
audience: GrowthX Engagement Managers
related: knowledge/content/seo-ranking-factors-study-guide-v1.md, knowledge/content/keyword-optimization-clustering-study-guide-v1.md
domain: delivery, SEO
confidence: synthesis
sensitivity: internal
context_tier: 1
last_updated: 2026-02-19
</metadata>

> This guide is your operating system for SEO at GrowthX. It distills two deep research guides (ranking factors + keyword optimization) into what you actually need to run engagements. Mental models to think with. Scoring frameworks to evaluate with. No fluff.

---

## The Mental Model: How SEO Actually Works in 2026

Forget the "200 ranking factors" lists. Google's ranking system, confirmed by their own leaked documents and antitrust testimony, runs on two master signals:

**Quality (Q\*):** How trustworthy and authoritative is this content? Driven by PageRank (still central, confirmed under oath), E-E-A-T signals, and site-level quality scores.

**Popularity (P\*):** How much do real people engage with this content? Driven by NavBoost (Google's confirmed click system), Chrome browsing data, branded search volume, and dwell time.

Everything else is a sub-signal feeding into one of these two buckets.

### The GrowthX SEO Stack

Think of SEO as four layers. Each layer depends on the one below it. Skip a layer and the ones above it collapse.

```
┌─────────────────────────────────────┐
│  LAYER 4: VISIBILITY                │
│  AI citations, featured snippets,   │
│  brand signals, entity presence     │
├─────────────────────────────────────┤
│  LAYER 3: AUTHORITY                 │
│  Backlinks, topical authority,      │
│  E-E-A-T, brand recognition        │
├─────────────────────────────────────┤
│  LAYER 2: CONTENT                   │
│  Topic architecture, intent match,  │
│  keyword clusters, depth, freshness │
├─────────────────────────────────────┤
│  LAYER 1: TECHNICAL FOUNDATION      │
│  Core Web Vitals, crawlability,     │
│  mobile-first, HTTPS, indexing      │
└─────────────────────────────────────┘
```

**Layer 1: Technical Foundation.** Prerequisites. You don't get bonus points for having them, but you get penalized for lacking them. Fast loading (LCP under 2.5s), responsive on mobile, HTTPS, clean crawl paths. If a client's site fails here, nothing else matters until it's fixed.

**Layer 2: Content.** This is where we spend most of our time. Topics organized into clusters. Each page targeting a group of related keywords (not single keywords. That's a 2015 approach). Content that matches the searcher's actual intent, with enough depth to demonstrate expertise. Refreshed quarterly so Google sees it as current.

**Layer 3: Authority.** Content alone won't rank in competitive spaces. You need external validation. Backlinks from relevant, authoritative sources. Topical authority built through consistent, deep coverage of your niche. Author credentials that demonstrate real experience. This layer compounds over time.

**Layer 4: Visibility.** The new frontier. Being cited in AI Overviews, ChatGPT, Perplexity. Getting featured snippets. Building brand recognition so people search for your client by name. This layer is where the game is shifting fastest.

### The Key Insight for EMs

Every week serving the same client should make the next week easier. That's the compounding nature of good SEO work. Topical authority builds. Backlink profiles strengthen. Brand signals accumulate. Content clusters become more interconnected.

Your job is to make sure the work compounds. Not to chase one-off tactics.

---

## The Evidence Hierarchy

When a client asks "why are we doing this?" or when you're evaluating an SEO recommendation, use this hierarchy to grade the evidence:

| Level | What It Means | Example |
|-------|--------------|---------|
| 1. Confirmed | Google said it under oath or it's in official docs | PageRank matters (antitrust testimony) |
| 2. Leaked | Found in Google's own internal documents | siteAuthority, NavBoost, siteFocusScore |
| 3. Studied | Large-scale correlation studies (1M+ data points) | Dwell time r=0.84 (DollarPocket, 10M results) |
| 4. Tested | Practitioner case studies with before/after data | Topic clusters +43% traffic (HubSpot) |
| 5. Consensus | Expert agreement without formal study | Brand signals matter, anchor text diversity |
| 6. Speculation | Opinions, outdated claims, unsupported theories | Social signals as direct ranking factor |

When you're building strategy, lean hard on Levels 1-3. Use Level 4 for tactical decisions. Be skeptical of anything that lives only at Level 5-6.

---

## What Actually Moves Rankings (The Priority Stack)

Based on every major study from 2025-2026, here's what matters most. Ordered by evidence strength and impact.

### Must-Haves (prerequisites, penalized if missing)

1. **Technical health.** Mobile-first, Core Web Vitals in green, HTTPS, crawlable. Pages with LCP under 1 second rank 7.5 positions higher on average than pages over 4 seconds. Only 44% of WordPress sites pass all CWV metrics on mobile. That's a real competitive advantage when fixed.

2. **Content relevance.** Text relevance appears in 90.6% of top-10 results (Semrush). Content must match the searcher's intent. Not just contain the right keywords. Actually answer what they're looking for, in the format they expect.

3. **Keyword in meta title.** 14% of Google's algorithm weight according to FirstPageSage. Simple, but still one of the highest-ROI optimizations. Google confirmed that anchor text and title tags provide "valuable clues" to relevance.

### Amplifiers (where real competitive advantage lives)

4. **Content depth and topical authority.** Google's leaked docs confirm siteFocusScore and siteRadius. They literally measure how deep and focused your coverage is. Pages with high topical authority gain traffic 57% faster (Graphite study). Content grouped into clusters drives 30% more organic traffic and holds rankings 2.5x longer than standalone pieces (HireGrowth, 2025).

5. **Backlinks from relevant, authoritative sources.** Still significant at 22% of the algorithm (DollarPocket). But declining. Quality over quantity. PageRank measures "distance from a known good source" (confirmed under oath). One editorial link from a respected industry publication beats 100 directory links. 85% of page-one sites have 1,000+ referring domains (Gotch SEO, 11.8M results).

6. **User satisfaction.** NavBoost uses 13 months of rolling click data. It tracks good clicks, bad clicks, and "lastLongestClicks" (the final click that satisfied the user). User engagement grew from 11% to 15% of algorithm weight in one year. If users bounce, rankings erode. Doesn't matter how good your backlinks are.

### Competitive Edge (what separates good from great)

7. **Brand signals.** Branded search volume, unlinked mentions, entity consistency. Rand Fishkin's advice after analyzing the API leak: "Build a notable, popular, well-recognized brand in your space, outside of Google search."

8. **Schema markup and structured data.** Not a direct ranking factor, but drives rich results (82% higher CTR) and increasingly important for AI citation.

9. **Content freshness.** 85% of AI Overview citations come from content published in the last 2 years. Quarterly content refreshes keep you in the game.

10. **AI search optimization.** Answer-first formatting, citation-ready content, semantic completeness. 47% of AI Overview citations come from pages ranking below position 5. You can get cited in AI even without traditional top rankings.

### What to Stop Doing

The evidence is clear on what doesn't work:

- **Keyword density optimization.** Zero correlation with rankings (Surfer, 1M SERPs).
- **Keywords in URL paths.** Near-zero correlation.
- **Chasing link quantity over quality.** Google's own team says "very few links" are needed. Quality matters.
- **Publishing AI-only content.** Average position 16.8 vs. 5.2 for human content (DollarPocket). AI assists, humans create.
- **One keyword per page.** Outdated. Cluster related keywords on single pages.

---

## How Keywords Work Now

### The Mental Shift: Keywords → Topics → Intent → Entities

Google doesn't match strings anymore. BERT (2019) gave it semantic understanding. The Knowledge Graph gives it entity awareness. AI Overviews give it answer synthesis. Your keyword strategy has to account for all of this.

**The clustering principle:** If Google ranks the same pages for two keywords, those keywords belong on the same page. If Google shows different results, they need separate pages. This is the SERP Overlap Method. The backbone of all serious keyword work.

**SERP overlap thresholds:**
- 70%+ overlap (7+ shared URLs in top 10): Same page, high confidence
- 40-70% overlap (4-6 shared URLs): Likely same page, validate manually
- Below 40% overlap: Different intent, separate pages

**The architecture:** Every client engagement should produce a topic map. Not a keyword list. Pillar pages covering core topics. Cluster pages going deep on subtopics. Everything interlinked. This is how you build topical authority systematically.

### How to Think About Keyword Difficulty

Tool scores are directional, not precise. Ahrefs KD only measures referring domain counts (ignoring on-page factors). Semrush adds more signals but still can't predict whether *your* client can rank.

Better questions than "what's the KD?":
- Does our client already have authority in this topic? (If yes, KD matters less.)
- What formats rank? (If it's all tools and product pages, a blog post won't win.)
- What does the top-ranking content look like? (Can we create something meaningfully better?)
- Is this a term our ideal buyer actually searches? (Relevance beats volume.)

---

## Site Scoring Framework

Use this when evaluating a client's current SEO health or scoping a new engagement. Score each dimension 1-5. The total gives you a quick read on where they stand and where to focus.

### Scoring Rubric

| Score | What It Means |
|-------|--------------|
| 1 | Critical issues. This dimension is actively hurting rankings. |
| 2 | Below average. Major gaps that need attention. |
| 3 | Adequate. Meets baseline expectations but won't win competitive SERPs. |
| 4 | Strong. Clear competitive advantage in this dimension. |
| 5 | Excellent. Best-in-class execution. |

### The 8 Dimensions

#### 1. Technical Foundation (Layer 1)

| Signal | How to Check | Score 1 | Score 3 | Score 5 |
|--------|-------------|---------|---------|---------|
| Core Web Vitals | PageSpeed Insights, CrUX data | All metrics failing | Mixed pass/fail | All green on mobile and desktop |
| Mobile experience | Mobile-friendly test, manual spot check | Broken mobile layout, unresponsive | Functional but slow or clunky | Fast, clean, fully responsive |
| Crawlability | Screaming Frog or Sitebulb crawl | Major crawl errors, broken sitemap, blocked resources | Clean crawl with minor issues | Clean crawl, logical URL structure, efficient crawl budget |
| HTTPS & security | Browser check, SSL Labs | No HTTPS or mixed content | HTTPS with minor mixed content | Full HTTPS, no warnings |
| Indexing health | Google Search Console (Coverage report) | Significant pages not indexed, index bloat | Most important pages indexed | All target pages indexed, no bloat |

**How to score:** Average across the five signals. Round to nearest whole number.

#### 2. Content Quality (Layer 2)

| Signal | How to Check | Score 1 | Score 3 | Score 5 |
|--------|-------------|---------|---------|---------|
| Intent match | Manual SERP comparison for top 10 target keywords | Content format mismatches what ranks (e.g., blog for transactional keyword) | Partial match. Right topic, wrong depth or format | Content format and depth match SERP expectations precisely |
| Depth and comprehensiveness | Surfer/Clearscope score, manual review | Thin content (under 500 words on topics that need depth) | Covers main points but misses subtopics | Comprehensive. Covers the topic as well or better than anything ranking |
| E-E-A-T signals | Manual review — author bios, credentials, firsthand experience | No author attribution, generic content, no experience signals | Author bios exist but thin; some experience markers | Named expert authors, detailed bios, clear firsthand experience, unique data |
| Originality | Manual review — unique insights, data, perspectives | Commodity content that could be on any site | Some unique angles but mostly standard coverage | Original research, proprietary data, perspectives unavailable elsewhere |
| Freshness | Check publish/update dates on key pages | Key pages haven't been updated in 2+ years | Some pages updated in the last year | Key content refreshed quarterly; dates visible |

**How to score:** Average across the five signals. Round to nearest whole number.

#### 3. Keyword Architecture (Layer 2)

| Signal | How to Check | Score 1 | Score 3 | Score 5 |
|--------|-------------|---------|---------|---------|
| Topic cluster structure | Site audit — content mapping | No discernible topic organization | Some loose topic groupings | Clear pillar-cluster architecture with internal linking |
| Keyword cannibalization | GSC — multiple URLs ranking for same queries | Widespread cannibalization across core topics | Some cannibalization in secondary topics | No significant cannibalization; clean keyword-to-page mapping |
| Intent segmentation | SERP spot-checks for target keywords | Informational, commercial, transactional mixed on same pages | Mostly separated but some overlaps | Each page targets a distinct intent cluster |
| Topic coverage | Gap analysis vs. competitors (Ahrefs Content Gap) | Major topic gaps — competitors cover 3-5x more subtopics | Moderate coverage — some gaps in key areas | Comprehensive coverage matching or exceeding top competitors |
| ICP alignment | Manual review — does the content match their ideal buyer? | Content targets high-volume vanity terms with no buyer intent | Mix of buyer-relevant and vanity content | Content clearly maps to buyer journey stages and ICP questions |

**How to score:** Average across the five signals. Round to nearest whole number.

#### 4. Backlink Profile (Layer 3)

| Signal | How to Check | Score 1 | Score 3 | Score 5 |
|--------|-------------|---------|---------|---------|
| Referring domain quality | Ahrefs/Semrush — DR/DA distribution, manual spot check | Mostly spam or irrelevant domains | Mix of quality — some editorial links, many low-value | Strong editorial links from relevant, authoritative publications |
| Referring domain quantity | Ahrefs — referring domains count vs. competitors | Significantly fewer referring domains than competitors | Comparable to mid-tier competitors | Matches or exceeds top competitors |
| Topical relevance of links | Manual review of top linking domains | Links come from unrelated industries | Some relevant, some random | Most links come from topically relevant, industry-specific sources |
| Anchor text distribution | Ahrefs — anchors report | Over-optimized (exact match dominated) or all branded | Reasonable mix with some over-optimization | Natural distribution — branded, topical, and URL anchors |
| Link velocity | Ahrefs — referring domains over time | Flat or declining | Steady but slow growth | Consistent, growing link acquisition |

**How to score:** Average across the five signals. Round to nearest whole number.

#### 5. User Engagement (Layer 2-3)

| Signal | How to Check | Score 1 | Score 3 | Score 5 |
|--------|-------------|---------|---------|---------|
| Organic CTR | GSC — CTR for target keywords | Well below SERP position averages | In line with position averages | Above-average CTR for position (compelling titles/descriptions) |
| Engagement metrics | GA4 — engagement rate, average engagement time | High bounce, low time on page across the board | Average engagement, some pages perform well | Strong engagement metrics; users spend time and interact |
| Return visits | GA4 — returning users from organic | Negligible return organic traffic | Some return visits | Meaningful returning organic audience |

**How to score:** Average across the three signals. Round to nearest whole number.

#### 6. Brand & Entity Signals (Layer 3-4)

| Signal | How to Check | Score 1 | Score 3 | Score 5 |
|--------|-------------|---------|---------|---------|
| Branded search volume | GSC or Ahrefs — brand name searches | Negligible branded search | Moderate branded search; growing | Strong branded search volume relative to category |
| Entity consistency | Manual check — NAP, schema, cross-platform profiles | Inconsistent or missing across platforms | Mostly consistent with gaps | Fully consistent across website, social, directories, schema |
| Schema markup | Schema validator, Rich Results Test | No schema or only basic | Organization + some content schema | Comprehensive schema — org, authors, articles, FAQ, products |
| Unlinked mentions | Brand monitoring tool or manual search | Rare or no mentions | Occasional industry mentions | Regular mentions in relevant publications and forums |

**How to score:** Average across the four signals. Round to nearest whole number.

#### 7. AI Search Readiness (Layer 4)

| Signal | How to Check | Score 1 | Score 3 | Score 5 |
|--------|-------------|---------|---------|---------|
| Answer-first formatting | Manual review — do key pages lead with clear answers? | Wall-of-text format, no clear answers extractable | Some pages have answer formats; inconsistent | Key pages structured for extraction — clear answers in first 100 words |
| AI citation presence | Manual check — search key topics in ChatGPT, Perplexity, Google AI Overview | Not appearing in any AI-generated answers | Occasional citations for brand or niche terms | Regularly cited across AI platforms for core topics |
| Multi-modal content | Manual review — images, video, structured data on key pages | Text-only content | Some images and video on select pages | Rich multi-modal content (text + images + video + data) on key pages |
| Content freshness for AI | Date check on key pages | Most content older than 2 years | Mix of fresh and dated content | Core content published or updated within 6 months |

**How to score:** Average across the four signals. Round to nearest whole number.

#### 8. Competitive Position

| Signal | How to Check | Score 1 | Score 3 | Score 5 |
|--------|-------------|---------|---------|---------|
| Organic visibility vs. competitors | Semrush/Ahrefs — visibility index, competitor comparison | Significantly behind all major competitors | Mid-pack. Comparable to some, behind leaders | Leading or matching top competitors on key topic areas |
| Content gap size | Ahrefs Content Gap tool | Competitors rank for 5x+ keywords the client doesn't | Moderate gaps. Some unique coverage, some missing | Minimal content gaps; client covers most of what competitors do |
| Topic Share | Ahrefs Keywords Explorer, Traffic Share by Domains report | Below 5% in core topic areas | 10-20% in some core areas | 20%+ in core topic areas |

**How to calculate Topic Share:** Pick a core topic (e.g., "enterprise data platform"). Pull all keywords in that topic space using Ahrefs Keywords Explorer. Run the "Traffic share by domains" report. Your client's percentage is their Topic Share. Compare against top 3 competitors. Kevin Indig's Growth Memo newsletter has the full methodology.

**How to score:** Average across the three signals. Round to nearest whole number.

---

### Interpreting the Site Score

Add up all 8 dimension scores (each 1-5). Maximum possible: 40.

| Total Score | Rating | What It Means |
|-------------|--------|---------------|
| 32-40 | Strong | Fine-tune and expand. Focus on Layer 4 (AI visibility, brand). |
| 24-31 | Solid | Good foundation. Identify 2-3 weakest dimensions and invest there. |
| 16-23 | Developing | Significant gaps. Prioritize Layer 1-2 fixes before amplifiers. |
| 8-15 | Critical | Major overhaul needed. Start with technical foundation and basic content quality. |

**Where to focus first:** Always fix the lowest-scoring dimension in the lowest layer. Technical problems in Layer 1 block everything above. Content gaps in Layer 2 make authority building (Layer 3) inefficient. Work from the foundation up.

---

## Content Scoring Framework

Use this when evaluating a piece of content your team creates, before it publishes. Score each dimension 1-5.

### The 7 Dimensions of Content Quality

#### 1. Intent Match

Does this content match what the searcher actually wants?

| Score | What It Looks Like |
|-------|-------------------|
| 1 | Wrong format entirely (e.g., blog post for a transactional keyword where product pages rank) |
| 2 | Right topic, wrong approach. Too broad, too narrow, or wrong angle vs. what ranks |
| 3 | Generally aligned. Covers the topic but doesn't nail the specific intent |
| 4 | Strong match. Format, depth, and angle align with what ranks in the top 5 |
| 5 | Perfect match. And adds something the current top results don't have |

**How to check:** Pull up the top 5 results for the target keyword cluster. Does your content look like it belongs? Is it in the same format? Covering the same depth? Answering the same core question?

#### 2. Depth and Comprehensiveness

Does this content cover the topic thoroughly enough to demonstrate expertise?

| Score | What It Looks Like |
|-------|-------------------|
| 1 | Surface-level. Says obvious things anyone could write. Under 500 words on a topic that needs depth. |
| 2 | Covers the basics but misses important subtopics competitors cover |
| 3 | Solid coverage. Hits the main points, comparable to average top-10 content |
| 4 | Thorough. Covers subtopics competitors miss, with specific details |
| 5 | Definitive. The most complete treatment of this topic available, with unique angles |

**How to check:** Run through Surfer or Clearscope to check topic coverage. But don't chase a perfect score. A naturally-written B+ piece often outperforms a forced A+ that reads like a keyword-stuffed encyclopedia.

#### 3. E-E-A-T Signals

Does this content demonstrate real Experience, Expertise, Authoritativeness, and Trustworthiness?

| Score | What It Looks Like |
|-------|-------------------|
| 1 | No author attribution. Generic content that could have come from anyone. No evidence of firsthand knowledge. |
| 2 | Author name exists but no bio, no credentials, no experience markers |
| 3 | Author bio with relevant credentials. Some first-person experience references. |
| 4 | Strong expertise signals. Specific case studies, named tools used, quantified results from real work |
| 5 | Undeniable authority. Original data, unique research, verifiable credentials, specific results with context |

**How to check:** Would Google's quality raters see this as coming from someone with genuine experience? Is there anything here a person without real-world experience couldn't write?

#### 4. Originality and Value-Add

Does this content offer something the reader can't get elsewhere?

| Score | What It Looks Like |
|-------|-------------------|
| 1 | Rewritten version of what already ranks. No unique perspective, data, or insight. |
| 2 | Mostly derivative with one or two mildly different points |
| 3 | Competent synthesis. Adds some organization or clarity but no new information |
| 4 | Clear value-add. Original frameworks, proprietary data, unique practitioner perspective |
| 5 | Genuinely new. Original research, data no one else has, perspective that changes how the reader thinks |

**How to check:** If we removed this page from the internet, would anything be lost? If the answer is "no, there's identical content elsewhere," score it low.

#### 5. Structure and AI-Readiness

Is this content structured for both human readers and AI extraction?

| Score | What It Looks Like |
|-------|-------------------|
| 1 | Wall of text. No headings, no clear structure, no extractable answers. |
| 2 | Basic headings but answers buried in paragraphs |
| 3 | Clear heading hierarchy. Some direct answers but not consistently formatted for extraction. |
| 4 | Well-structured with answer-first formatting. Key questions answered clearly in the first paragraph of each section. |
| 5 | Optimized for extraction. Concise answers near the top, FAQ section, schema markup, clear heading hierarchy matching likely queries |

**How to check:** Could an AI system easily pull a clear, accurate answer from this content? Is the core answer in the first 100 words? (44% of AI citations come from the first 30% of content.)

#### 6. Technical On-Page Optimization

Are the basics done right?

| Score | What It Looks Like |
|-------|-------------------|
| 1 | No target keyword in title. No meta description. No internal links. Duplicate title tag. |
| 2 | Keyword in title but poorly written. Thin meta description. Minimal internal links. |
| 3 | Solid title with keyword. Decent meta description. A few internal links. |
| 4 | Compelling title (optimized for CTR + keywords). Strong meta description. Strategic internal links to/from relevant cluster pages. Image alt text. |
| 5 | All of the above plus schema markup, optimized URL, strong internal linking within the topic cluster, multi-modal elements (images, video, embeds) |

**How to check:** Run through a quick checklist: title tag, meta description, H1, internal links, image alt text, schema, URL structure.

#### 7. Readability and Voice

Does this read well? Does it feel like something a real expert wrote?

| Score | What It Looks Like |
|-------|-------------------|
| 1 | Obviously AI-generated with no editing. Stilted, repetitive, or filled with jargon. |
| 2 | Technically correct but bland. Reads like a Wikipedia article |
| 3 | Readable and clear. Professional but not memorable. |
| 4 | Engaging. Has a clear voice, flows well, uses concrete examples and specific language |
| 5 | Excellent. Reads like it was written by a smart expert who cares about the reader's time. You'd share it. |

**How to check:** Read it aloud. If you wouldn't say it to a smart friend, rewrite it. (DollarPocket found AI-only content averages position 16.8 vs. 5.2 for human content. Voice and quality matter.)

---

### Interpreting the Content Score

Add up all 7 dimension scores (each 1-5). Maximum possible: 35.

| Total Score | Rating | Action |
|-------------|--------|--------|
| 30-35 | Publish-ready | Ship it. Minor polish only. |
| 24-29 | Strong draft | One more editing pass. Address any dimension below 4. |
| 17-23 | Needs work | Significant revision needed. Focus on the lowest-scoring dimensions. |
| 7-16 | Rework | Major issues. Likely needs substantial rewrite or new approach. |

**Minimum publishing threshold:** No dimension below 3. If any dimension is a 1 or 2, fix it before publishing. A single weak dimension can undermine the whole piece.

**Content that typically performs:** Scores 28+ with no dimension below 4. This is your target for competitive keywords.

---

## Putting It Together: The EM Playbook

### When Scoping a New Engagement

1. Run the Site Scoring Framework. Takes about 2 hours with the right tools.
2. Identify which layers need the most work (technical → content → authority → visibility).
3. Build the engagement roadmap starting from the lowest-performing layer.
4. Set expectations: Layer 1-2 fixes show results in weeks. Layer 3-4 work compounds over months.

### When Planning Content

1. Build the topic map. Clusters, not keyword lists.
2. Prioritize by ICP alignment and existing authority, not by volume.
3. Use SERP analysis to validate every clustering decision.
4. For each content piece, define the target score before writing starts.

### When Reviewing Content

1. Score every piece against the Content Scoring Framework before publishing.
2. Nothing ships below 24/35. Nothing ships with any dimension below 3.
3. Focus revision energy on the lowest-scoring dimensions first.
4. Track content scores over time. Your team should be getting better.

### When Reporting to Clients

1. Use the Site Score to show progress across dimensions.
2. Connect improvements to the evidence hierarchy. "We're doing this because Google confirmed X under oath" lands differently than "this is SEO best practice."
3. Track the metrics that matter at each layer: technical health (CWV pass rate), content performance (organic traffic per cluster), authority (referring domains, Topic Share), visibility (AI citations, featured snippets).

---

## Quick Reference Card

### What Google confirmed works (Level 1-2 evidence)

- PageRank / link quality (antitrust testimony)
- NavBoost click signals: good clicks, bad clicks, last longest click (API leak + testimony)
- siteAuthority score (API leak)
- siteFocusScore / topical authority (API leak)
- Core Web Vitals (official documentation)
- E-E-A-T as quality framework (official guidelines)
- Freshness signals (API leak)
- Anchor text relevance (antitrust testimony)

### What major studies show matters most

- Content relevance: appears in 90.6% of top-10 results (Semrush)
- Dwell time: r=0.84 correlation (DollarPocket, 10M results)
- Quality backlinks: r=0.85 correlation (DollarPocket)
- Mobile page speed: r=0.83 correlation (DollarPocket)
- Topic clusters: +30% organic traffic, 2.5x longer rankings (HireGrowth)
- Topical authority: 57% faster traffic gains (Graphite)

### What doesn't work

- Keyword density: zero correlation (Surfer, 1M SERPs)
- Keywords in URL: near-zero correlation (Surfer)
- AI-only content: avg position 16.8 vs. 5.2 for human content (DollarPocket)
- Link quantity without quality: Google says "very few links" needed

---

*This guide synthesizes findings from the GrowthX SEO Ranking Factors Study Guide and Keyword Optimization & Clustering Study Guide. For full evidence, source citations, and learning paths, see those documents in `knowledge/content/`.*
