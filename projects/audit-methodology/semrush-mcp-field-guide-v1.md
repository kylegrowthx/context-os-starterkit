# SEMRush MCP — Expert Field Guide

<metadata>
purpose: Practitioner's field guide to SEMRush data through the SEO/AEO expert lens — what to pull, why it matters, how to interpret it, and where it connects to AI visibility strategy
access: build-team
related: knowledge/seo-aeo/seo-ranking-factors-study-guide-v1.md, knowledge/seo-aeo/aeo-content-quality-factors-study-guide-v1.md, context/roles/seo-content-quality-expert-v1.md, context/roles/aeo-expert-v1.md
last_updated: 2026-03-05
</metadata>

---

## How to Use This Guide

This is not a tool manual. It's organized by the questions a practitioner actually asks, with each section explaining what data answers the question, which SEMRush reports provide it, what the results mean, and where SEMRush data connects to AI visibility strategy.

**If you need the raw MCP mechanics** — the 3-step call pattern, column codes, filter syntax, and every report's parameters — see the technical reference in Part 4. That's the lookup table. This guide is the thinking layer on top.

**Five parts:**

1. **Why SEMRush Data Matters in 2026** — The evidence base for what SEMRush measures and why it still matters when AI is changing everything
2. **The Data You Need** — Seven practitioner questions, the reports that answer them, expert interpretation, and AEO connections
3. **The SEMRush-to-AEO Bridge** — How traditional SEO data maps to AI visibility signals
4. **Technical Reference** — MCP mechanics, column glossary, filter syntax, complete report catalog
5. **GrowthX Recipes** — Named workflows for common audit scenarios

---

# Part 1: Why SEMRush Data Matters in 2026

## The Search Landscape Has Split

Google still processes 8.5 billion searches per day. But 94% of B2B buyers now use LLMs in the buying process, and about half start in a chatbot before they ever touch Google. Search visibility and AI visibility are diverging into two channels that share common inputs but produce different outputs.

SEMRush measures the traditional search channel comprehensively. It does not measure AI visibility — that's CheckThat's domain. But the data SEMRush provides is critical to *both* channels, because the signals that drive organic rankings overlap significantly with the signals that drive AI citations.

The question isn't "does SEMRush data still matter?" It's "what does SEMRush data tell you about AI visibility that you can't see any other way?"

## What Google Actually Confirmed

The 2024 API leak and DOJ antitrust trial gave us the closest thing to ground truth we've ever had about how Google works. The most relevant findings for interpreting SEMRush data:

**Every page gets two master scores: Quality (Q\*) and Popularity (P\*).**
- Q\* measures trustworthiness and authority, heavily influenced by PageRank (distance from known good sources)
- P\* measures popularity through Chrome visit data and NavBoost click signals
- SEMRush's Authority Score (backlinks_overview) is a reasonable proxy for Q\*, while Organic Traffic (Ot) reflects P\*

**NavBoost uses 13 months of click data.** It tracks "goodClicks," "badClicks," and "lastLongestClicks" from the SERP. This means organic traffic trends (from `domain_rank_history`) don't just reflect past performance — they reflect a compounding feedback loop that Google actively uses for future rankings.

**siteAuthority exists as a real metric.** Despite years of denial, Google computes a site-wide authority signal. SEMRush's Authority Score (from `backlinks_overview`) approximates this. The correlation isn't perfect, but the directional signal is useful.

**siteFocusScore and siteRadius measure topical concentration.** Google quantifies how concentrated a site's content is around core topics. This confirms that subfolder and subdomain analysis (measuring traffic distribution across `/blog/`, `/docs/`, `/templates/`) directly reflects a signal Google uses.

## The Ranking Factor Evidence Base

Across five major correlation studies in 2025-2026, the factors consistently measured by SEMRush data show clear patterns:

| Factor | Evidence | SEMRush Signal |
|--------|----------|----------------|
| Content relevance and depth | 90.6% of top-10 results match query intent (SEMRush study) | Keyword position distribution, search intent (In column) |
| High-quality referring domains | r=0.85 (DollarPocket, 10M results) | Authority Score, referring domains (`backlinks_refdomains`) |
| Topical authority | 13% weight (FirstPageSage); 5-10 interlinked pages = recognized authority | Subfolder traffic distribution, keyword clustering by URL pattern |
| Backlinks | Declining (27% → 22% weight, DollarPocket) but still significant | `backlinks_overview`, `backlinks_historical` |
| User engagement | Fastest-growing factor: 11% → 15% (DollarPocket) | Organic traffic trends as a proxy (`domain_rank_history`) |
| Brand signals | r=0.664 correlation with rankings (Fishkin); stronger than backlinks | Brand-term keyword volume from `phrase_this` |
| Text relevance | Appeared in 90.6% of top-10 results | Keyword-URL mapping from `domain_organic` |

**What SEMRush doesn't measure but matters:** User engagement signals (dwell time, pogo-sticking, CTR), E-E-A-T quality markers, content freshness at the content level, and AI visibility. SEMRush shows you the outcomes of these signals — traffic changes, position shifts — not the signals themselves.

## The AEO Connection

Here's where it gets interesting. The AEO content quality research (120+ sources, 40+ factors) found that the signals driving AI citations overlap with — but diverge from — traditional ranking factors:

| Signal | Traditional SEO Correlation | AI Citation Correlation | Implication |
|--------|---------------------------|------------------------|-------------|
| Organic keywords | 0.41 (moderate) | 0.41 (consistent) | Keywords matter equally for both channels |
| Brand search volume | Emerging (~0.664 for rankings) | **0.334** (strongest AI predictor) | Brand visibility predicts AI visibility |
| Domain authority | Still significant | **r=0.18** (nearly useless) | Authority Score matters for SEO, not for AI |
| Backlink quality | r=0.85 (strong) | r=0.37 (weak) | Links still matter for SEO; much less for AI |
| Third-party validation | Important | **6.5x multiplier** | The biggest divergence between channels |
| Content freshness | Moderate | Critical (platform-specific) | SEMRush shows trajectory; freshness windows vary by AI engine |

**The takeaway:** SEMRush data is essential for the overlapping signals (keywords, brand volume, content trajectory) and reveals the SEO baseline that informs AI visibility strategy. But it cannot tell you about AI citations, source mapping, or alignment — that's where CheckThat picks up.

## The Four-Layer SEO Stack

Every domain audit maps to a four-layer model. SEMRush provides data for all four:

```
Layer 4: VISIBILITY    ← Am I being seen? (Rankings, traffic, AI citations)
Layer 3: AUTHORITY     ← Do others trust me? (Backlinks, mentions, brand signals)
Layer 2: CONTENT       ← Is the content good? (Keywords, pages, trajectories)
Layer 1: TECHNICAL     ← Can it be crawled? (Site audit, Core Web Vitals, structure)
```

| Layer | SEMRush Reports | What It Answers |
|-------|----------------|-----------------|
| Technical | Site Audit suite, subfolder/subdomain analysis | Can search engines and AI crawlers access the content? |
| Content | `domain_organic`, `domain_organic_unique`, `url_organic`, `url_rank_history` | Is the content working? What's growing, declining, or dead? |
| Authority | Backlink suite, `domain_organic_organic` (competitors) | How does the domain's authority compare to competitors? |
| Visibility | `domain_rank`, `domain_rank_history`, position tracking | What's the actual traffic and ranking outcome? |

Problems at lower layers undermine everything above. A brilliant content strategy on a broken site produces nothing. The audit moves bottom-up: Technical → Content → Authority → Visibility.

---

# Part 2: The Data You Need

## 1. "How Healthy Is This Domain?"

**The diagnostic question:** Is this domain growing, stable, or declining — and why?

### Reports

| Report | What It Returns | Key Columns |
|--------|----------------|-------------|
| `domain_rank` | Current snapshot: rank, keywords, traffic, cost | Rk, Or, Ot, Oc, Ad, At, Ac |
| `domain_rank_history` | Monthly snapshots over time | Rk, Or, Ot, Oc, Dt (sorted dt_desc) |
| `domain_ranks` | Same domain across all regional databases | Db, Dn, Rk, Or, Ot, Oc |
| `backlinks_overview` | Authority score, total links, referring domains | score, total, domains_num |

### How to Read the Results

**Organic traffic (Ot) is the vital sign.** Everything else is context for why traffic is moving.

| Pattern | What It Means | Root Cause |
|---------|---------------|------------|
| Ot rising, Or rising | Healthy growth — gaining keywords and traffic | Content strategy is working |
| Ot falling, Or stable | **Position erosion** — same keywords, worse positions | Competitors gaining, content aging, or algorithm shift |
| Ot stable, Or rising | **Ranking for junk** — gaining low-value keywords | Content targeting is off; chasing volume over relevance |
| Ot falling, Or falling | Losing both keywords and traffic | Possible penalty, technical issue, or competitive displacement |
| Ot flat, everything flat | Plateau — not growing, not dying | Needs new content investment or competitive repositioning |

**Organic cost (Oc) is an underused proxy.** It estimates what the organic traffic would cost in Google Ads. Rising Oc with stable Ot means the keywords you rank for are becoming more commercially valuable. Falling Oc means the opposite — your traffic is shifting toward lower-value queries.

**The Authority Score tells a different story.** From `backlinks_overview`, the score (0-100) approximates site-wide authority. Compare it to competitors. But remember: for AI visibility, domain authority correlates at only r=0.18. A high Authority Score helps SEO but doesn't guarantee AI citations.

### AEO Bridge

Organic traffic trends are one of the strongest indirect signals for AI visibility trajectory. Sites with growing organic presence tend to accumulate the brand signals and content depth that AI engines recognize. But the relationship isn't automatic — a site can rank well for keywords that AI engines never surface (e.g., navigational queries, very long-tail terms).

The most AI-relevant metric from this dataset is the trend direction of branded keyword volume. Pull `phrase_this` for the brand name to check — this correlates at 0.334 with AI citation likelihood, the strongest single predictor in the AEO research.

### MCP Call Pattern

```
Step 1: domain_rank        → params: { domain: "example.com", database: "us" }
Step 2: domain_rank_history → params: { domain: "example.com", database: "us", display_limit: 50, display_sort: "dt_desc" }
Step 3: backlinks_overview  → params: { target: "example.com", target_type: "root_domain" }
Step 4: phrase_this         → params: { phrase: "brand name", database: "us" }
```

---

## 2. "What Content Is Working and What's Failing?"

**The diagnostic question:** Which pages drive traffic, which are declining, and where are the opportunities?

### Reports

| Report | What It Returns | Key Columns |
|--------|----------------|-------------|
| `domain_organic` | Every keyword the domain ranks for | Ph, Po, Nq, Ur, Tr, Tc, Kd, In |
| `domain_organic_unique` | Every indexed page with aggregated metrics | Ur, Pc, Tg, Tr |
| `url_organic` | Keywords for a specific URL | Ph, Po, Nq, Cp, Tr, Tc |
| `url_rank_history` | Historical traffic for a specific URL | Or, Ot, Oc, Dt |

### How to Read the Results

**Page classification comes first.** Before analyzing content performance, classify every indexed page by URL pattern:

| Type | URL Patterns | What It Represents |
|------|-------------|-------------------|
| Brand | Homepage, /pricing, /about, /product, /features | Core product and company pages |
| Content | /blog/, /resources/, /guides/, /articles/ | SEO-driven content marketing |
| Templates | /templates/ | Programmatic/product-led pages |
| Docs | /docs/, /api/, developers.* | Technical documentation |
| Support | /help/, /faq/, help.* | Customer support content |
| Education | /courses/, /academy/, university.* | Educational resources |
| Transactional | /login, /sign-up, /checkout | User action pages (rarely rank) |

Pull `domain_organic_unique` with a high `display_limit` (5,000-10,000) to get every indexed page. The Tg (traffic) column shows each page's contribution. Sort by `tr_desc` to find the pages driving the most traffic.

**Content trajectory analysis reveals the story.** For content pages, pull `url_rank_history` and classify the trajectory:

| Trajectory | Criteria | What It Means |
|------------|----------|---------------|
| Surging | >100% traffic gain in 6 months, or new | Content resonating; double down |
| Growing | +25% to +100% gain | Healthy momentum; optimize for more |
| Stable | -10% to +25% change | Working but not accelerating |
| Declining | -10% to -50% loss | Aging or outcompeted; needs refresh |
| Freefall | >50% loss | Structural problem; urgent fix or retire |
| Dead | Zero or near-zero throughout | Never worked; reevaluate or remove |

**Quick wins identification.** Filter `domain_organic` for positions 4-20 with search volume >100. These are keywords where a small ranking improvement could yield significant traffic gains:

```
display_filter: +|Po|Gt|3|+|Po|Lt|21|+|Nq|Gt|100
```

**Zero-traffic page ratio.** The percentage of indexed pages generating zero organic traffic reveals index efficiency. A site with 6,000 indexed pages where 4,000 get zero traffic has a serious crawl budget and quality dilution problem.

### AEO Bridge

Content trajectory analysis maps directly to AI citation freshness windows:

| AI Engine | Freshness Window | SEMRush Signal |
|-----------|-----------------|----------------|
| Perplexity | 2-3 day decay | Pages must be actively updated; url_rank_history shows if content is current |
| ChatGPT | 30-day optimal window | 76.4% of cited content updated within 30 days |
| Google AI Overviews | 90-180 day tolerance | 85% of citations from content published in the last 2 years |

Pages in "Declining" or "Freefall" trajectory are almost certainly outside AI citation windows. The content trajectory classification doubles as an AI visibility freshness audit.

Additionally, the `In` (search intent) column from `domain_organic` maps to the AEO Expert's 16 prompt-type taxonomy. Informational keywords (In=1) align with Problem Recognition and Solution Exploration prompts. Commercial keywords (In=0) and Transactional keywords (In=3) align with Evaluation-stage prompts — which carry the highest AEO weight.

### MCP Call Pattern

```
Step 1: domain_organic_unique → params: { domain: "example.com", database: "us", display_limit: 10000, display_sort: "tr_desc" }
Step 2: domain_organic        → params: { domain: "example.com", database: "us", display_limit: 10000, export_columns: ["Ur","Ph","Po","Nq","Tr","Tc","In","Kd"] }
Step 3: url_rank_history      → params: { url: "example.com/blog/specific-post", database: "us", display_limit: 50, display_sort: "dt_desc" }
```

For the quick wins filter:
```
domain_organic → display_filter: "+|Po|Gt|3|+|Po|Lt|21|+|Nq|Gt|100"
```

---

## 3. "Who Are the Real Competitors and Where Do They Beat Us?"

**The diagnostic question:** Which domains compete for our keywords, where do they outperform us, and what can we learn?

### Reports

| Report | What It Returns | Key Columns |
|--------|----------------|-------------|
| `domain_organic_organic` | Organic competitors ranked by keyword overlap | Dn, Cr, Np, Or, Ot |
| `domain_domains` | Keyword gap: shared, unique, missing keywords between domains | Ph, P0-P4, Nq, Kd |
| `domain_adwords_adwords` | Paid search competitors | Dn, Cr, Np |
| `backlinks_comparison` | Side-by-side backlink profiles | Per-domain metrics |

### How to Read the Results

**Competitor relevance (Cr) is keyword overlap, not business competition.** A domain with Cr=0.35 shares 35% keyword overlap with your domain. This often surfaces unexpected competitors — documentation sites, media publications, or adjacent-category players that compete for the same queries without competing for the same customers.

**Tier your competitors by traffic ratio:**

| Tier | Traffic Ratio (vs. target) | Implication |
|------|---------------------------|-------------|
| Tier 1: Leaders | 10x+ traffic | Aspirational; study their content strategy |
| Tier 2: Challengers | 2-10x traffic | Direct competitive threat; look for gaps to exploit |
| Tier 3: Peers | 0.5-2x traffic | True peers; head-to-head battle |
| Tier 4: Trailing | <0.5x traffic | Not a threat; may be catching up |

**The keyword gap analysis is the highest-value competitive report.** Use `domain_domains` to find:

| Gap Type | Format | What It Reveals |
|----------|--------|-----------------|
| Missing keywords | `*\|or\|competitor1\|*\|or\|competitor2\|-\|or\|yourdomain` | Keywords ALL competitors rank for that you don't |
| Untapped keywords | `*\|or\|competitor1\|+\|or\|competitor2\|-\|or\|yourdomain` | Keywords ANY competitor ranks for that you don't |
| Unique keywords | `*\|or\|yourdomain\|-\|or\|competitor1\|-\|or\|competitor2` | Keywords only you rank for (your moat) |
| Shared keywords | `*\|or\|yourdomain\|*\|or\|competitor1\|*\|or\|competitor2` | Keywords everyone ranks for (battleground) |

**Content gap vs. authority gap.** If a competitor ranks for keywords you don't, there are two possible reasons: they have content you lack (content gap), or they have content on the same topic but rank higher due to stronger authority (authority gap). Compare `domain_rank` metrics alongside the gap analysis to distinguish.

### AEO Bridge

Competitive SEO position is a strong predictor of AI visibility: 99% of URLs in Google AI Mode appear in the top 20 organic results. This means the keyword gap analysis doubles as an AEO opportunity map — topics where competitors rank organically are topics where they're likely to appear in AI answers too.

More specifically, the keyword gap reveals content topics where you could build pages optimized for both SEO and AI citation. The AEO Expert's prompt library should be informed by competitive keyword gaps: if three competitors rank for "best project management tools for remote teams" and you don't, that's both an SEO content gap and likely an AEO prompt gap.

The `backlinks_comparison` report reveals which third-party sources link to competitors but not to you. Since third-party validation carries a 6.5x multiplier for AI citations, these linking domains are high-priority targets for outreach — not just for link building, but for earning the third-party mentions that AI engines weigh heavily.

### MCP Call Pattern

```
Step 1: domain_organic_organic → params: { domain: "example.com", database: "us", display_limit: 20 }
Step 2: domain_domains         → params: { domains: "*|or|competitor1.com|*|or|competitor2.com|-|or|example.com", database: "us", display_limit: 500, display_sort: "nq_desc" }
Step 3: backlinks_comparison   → params: { targets: ["example.com","competitor1.com","competitor2.com"], target_types: ["root_domain","root_domain","root_domain"] }
```

---

## 4. "What Keywords Should We Target?"

**The diagnostic question:** Which keywords represent the best opportunities given our authority, content, and audience?

### Reports

| Report | What It Returns | Key Columns |
|--------|----------------|-------------|
| `phrase_this` | Single keyword overview: volume, CPC, competition | Ph, Nq, Cp, Co, Nr |
| `phrase_these` | Batch analysis (semicolon-separated, up to 100) | Ph, Nq, Cp, Co, Nr, Td |
| `phrase_related` | Semantically related keywords | Ph, Nq, Cp, Co, Rr, Kd |
| `phrase_fullsearch` | Broad match: all queries containing the phrase | Ph, Nq, Cp, Co, Kd |
| `phrase_questions` | Question-format queries (max 100 results) | Ph, Nq, Cp, Co |
| `phrase_kdi` | Keyword difficulty scores (batch, semicolon-separated) | Ph, Kd |
| `phrase_organic` | Which domains rank for a keyword | Dn, Ur, Fk |

### How to Read the Results

**Keyword difficulty (Kd) is an effort signal, not a verdict.** Kd 0-29 means you can rank with good content and basic optimization. Kd 30-49 requires strong content plus some authority. Kd 50-69 needs significant authority and optimized content. Kd 70+ requires a dominant position or an exceptional content angle.

**Search intent (In) shapes the content format:**

| In Value | Intent Type | Content Format | SEO Priority | AEO Priority |
|----------|-------------|---------------|-------------|-------------|
| 0 | Commercial | Comparison pages, buying guides | High | Very High (evaluation-stage) |
| 1 | Informational | Blog posts, guides, explainers | Medium | High (problem recognition) |
| 2 | Navigational | Homepages, branded pages | Low (already ranked or not) | Low |
| 3 | Transactional | Product pages, pricing, signup | High | Medium (decision-stage) |

**The volume/difficulty sweet spot.** The best keyword opportunities sit in the zone where volume is high enough to matter (Nq > 100) but difficulty is low enough to be achievable (Kd < 50). Filter `phrase_related` or `phrase_fullsearch` for this:

```
display_filter: +|Nq|Gt|100|+|Kd|Lt|50
```

**Question keywords deserve special attention.** `phrase_questions` returns question-format queries related to your topic. These are uniquely valuable because:
- They're the format buyers use with AI engines ("What is the best CRM for small teams?")
- They map to featured snippet and AI Overview opportunities
- They reveal the actual language of buyer intent

**The Td (trends) column reveals seasonality.** It returns 12 monthly search volume values. A keyword with steady Nq=500 is different from one that spikes to 2,000 in January and drops to 100 in July.

### AEO Bridge

Question keywords from `phrase_questions` map directly to how buyers ask AI engines. The AEO Expert's 16 prompt-type taxonomy aligns with keyword intent categories:

| Keyword Pattern | AEO Prompt Type | Buyer Stage |
|----------------|-----------------|-------------|
| "what is [category]" | Category Education | Problem Recognition |
| "how to [solve problem]" | Problem Definition | Problem Recognition |
| "[product A] vs [product B]" | Direct Comparison | Evaluation |
| "best [category] for [use case]" | Best-of-Category | Evaluation |
| "alternatives to [product]" | Alternatives To | Evaluation |
| "[product] pricing" | Pricing & Cost | Evaluation |
| "[product] reviews" | Review & Reputation | Evaluation |
| "how to implement [product]" | Implementation | Decision/Post-Purchase |

When building a CheckThat prompt library, the keyword research from SEMRush provides the raw language of buyer intent. The highest-value prompts are derived from high-volume question keywords with commercial intent (In=0) — these are the queries buyers ask both Google and AI engines.

### MCP Call Pattern

```
Step 1: phrase_related   → params: { phrase: "project management software", database: "us", display_limit: 200, display_filter: "+|Nq|Gt|100|+|Kd|Lt|50" }
Step 2: phrase_questions → params: { phrase: "project management", database: "us", display_limit: 100 }
Step 3: phrase_kdi       → params: { phrase: "keyword1;keyword2;keyword3", database: "us" }
Step 4: phrase_organic   → params: { phrase: "best project management tool", database: "us", display_limit: 20 }
```

---

## 5. "How Strong Is Our Authority?"

**The diagnostic question:** How does our backlink profile compare to competitors, and where are the authority gaps?

### Reports

| Report | What It Returns | Key Columns |
|--------|----------------|-------------|
| `backlinks_overview` | Total links, referring domains, authority score | score, total, domains_num, follows_num |
| `backlinks_refdomains` | Every domain linking to the target | domain, backlinks_num, domain_ascore |
| `backlinks_anchors` | Anchor text distribution | anchor, domains_num, backlinks_num |
| `backlinks_historical` | Monthly backlink and referring domain trends | date, backlinks_num, domains_num, score |
| `backlinks_competitors` | Domains with similar backlink profiles | (competitor domains) |
| `backlinks_comparison` | Side-by-side metrics for multiple domains | Per-target metrics |
| `backlinks_matrix` | Referring domains that link to multiple targets | domain_ascore, matchesnum |
| `backlinks_pages` | Which pages on your site receive backlinks | (page URLs, backlink counts) |
| `backlinks_geo` | Geographic distribution of referring domains | country, domains_num |
| `backlinks_tld` | TLD distribution (.com, .org, .edu, etc.) | TLD, domains_num |
| `backlinks_categories` | Categories the domain belongs to | category, rating |
| `backlinks_categories_profile` | Categories of referring domains | category, rating |

### How to Read the Results

**Authority Score is directional, not absolute.** SEMRush's score (0-100) combines link signals, organic traffic signals, and spam signals into a composite. It approximates Google's siteAuthority concept confirmed in the leak. Use it for competitive comparison, not as a standalone quality metric.

**Referring domain count matters more than total backlinks.** 100 links from 1 domain count less than 100 links from 100 different domains. The `domains_num` from `backlinks_overview` is the primary health metric.

**Anchor text distribution reveals health or risk:**

| Distribution | What It Signals |
|-------------|-----------------|
| Mostly branded anchors (60-70%) | Natural, healthy profile |
| Mostly exact-match keyword anchors (>30%) | Potential over-optimization risk |
| Heavy "click here" / naked URL (>40%) | Unintentional link building; low value |
| Diverse mix with branded + topical | Ideal distribution |

**Historical trends show momentum.** Pull `backlinks_historical` to see whether referring domains are growing, stable, or declining. A declining trend with stable rankings means you're consuming authority capital without replenishing it — a lead indicator of future ranking loss.

**The backlinks_matrix reveals shared referring domains.** For competitive analysis, this shows which authoritative domains link to multiple competitors but not to you. These are the highest-priority outreach targets.

### AEO Bridge

This is where SEO and AEO data diverge most sharply.

**For traditional SEO:** Backlink quality remains a strong signal (r=0.85 for high-quality referring domains in the DollarPocket study). Authority Score matters. Link building works.

**For AI visibility:** Domain authority correlation with AI citations has dropped to r=0.18 — nearly useless. Backlink quality shows only r=0.37 correlation with AI citations. The link-based authority model that dominates SEO is fading in the AI channel.

**But the backlink data still has AEO value — reframed.** The referring domains from `backlinks_refdomains` and `backlinks_matrix` reveal which third-party sources talk about your domain. Since third-party validation carries a 6.5x multiplier for AI citations, the referring domain list is essentially a map of your third-party validation ecosystem. Cross-reference this with CheckThat's source analysis to see which linking domains AI engines actually cite.

The `backlinks_categories_profile` report shows the types of sites linking to you (tech press, review platforms, competitor blogs, etc.). This maps to the AEO Expert's source domain classification (Review Platform, Community, Press, Analyst, Competitor, etc.) — and reveals where your third-party validation is concentrated versus where it's missing.

### MCP Call Pattern

```
Step 1: backlinks_overview   → params: { target: "example.com", target_type: "root_domain" }
Step 2: backlinks_refdomains → params: { target: "example.com", target_type: "root_domain", display_limit: 100, display_sort: "domain_ascore_desc" }
Step 3: backlinks_historical → params: { target: "example.com", target_type: "root_domain", display_limit: 50 }
Step 4: backlinks_matrix     → params: { targets: ["example.com","competitor1.com","competitor2.com"], target_types: ["root_domain","root_domain","root_domain"], display_limit: 50 }
```

---

## 6. "How Are Specific Sections Performing?"

**The diagnostic question:** How does traffic distribute across the site's content sections, and where is topical authority concentrated?

### Reports

| Report | What It Returns | Key Columns |
|--------|----------------|-------------|
| `subfolder_organic` | Keywords for a URL path (e.g., `example.com/blog/`) | Ph, Po, Nq, Tr |
| `subfolder_organic_unique` | Unique pages within a subfolder ranking | Ur, Pc, Tg, Tr |
| `subfolder_rank_history` | Historical traffic for a subfolder | Or, Ot, Oc, Dt |
| `subdomain_organic` | Keywords for a subdomain (e.g., `docs.example.com`) | Ph, Po, Nq, Tr |
| `subdomain_rank_history` | Historical traffic for a subdomain | Or, Ot, Oc, Dt |
| `domain_organic_subdomains` | All subdomains with their traffic share | Ur, Pc, Tg, Tr |

**Important:** Subfolder values require a trailing slash (e.g., `example.com/blog/`).

### How to Read the Results

**Information architecture analysis.** Pull `domain_organic_subdomains` first to see the full structural map. Then drill into specific subfolders to understand section performance.

Typical B2B SaaS IA and what the traffic distribution reveals:

| Section | Healthy Sign | Warning Sign |
|---------|-------------|--------------|
| /blog/ or /resources/ | 15-40% of total traffic | <5% (content isn't working) or >60% (brand pages failing) |
| /docs/ or developers.* | Significant if product is developer-facing | Zero traffic = docs not indexed or not useful |
| /templates/ or /tools/ | Growing traffic = product-led SEO working | Declining = competitors winning programmatic game |
| Main domain (brand pages) | Stable, dominant | Declining faster than content grows |

**Topical authority measurement.** The SEO Content Quality Expert scores topical authority based on "5-10 interlinked pages around a theme = recognized authority; 30% more traffic." Subfolder analysis lets you test this: does the `/blog/category/` subfolder with 8 related posts generate more traffic per post than orphan content?

Pull `subfolder_rank_history` for each major section to see which are growing and which are declining. Sections in decline need content investment or structural reform.

### AEO Bridge

Section-level performance reveals topical authority clusters — which is directly relevant to AI citation. AI engines don't evaluate individual pages in isolation; they assess whether a domain has depth on a topic. A site with 8 interlinked posts about "B2B email marketing" is more likely to be cited for email marketing queries than one with a single comprehensive guide.

The subfolder traffic data reveals where your topical depth exists (and where it doesn't). Compare this to your CheckThat category presence: if you have strong SEO performance in `/blog/email-marketing/` but low AI visibility for email marketing prompts, the gap is likely structural (content not formatted for AI extraction) rather than topical (you have the depth; AI just can't use it).

### MCP Call Pattern

```
Step 1: domain_organic_subdomains → params: { domain: "example.com", database: "us", display_limit: 50 }
Step 2: subfolder_organic         → params: { domain: "example.com/blog/", database: "us", display_limit: 5000 }
Step 3: subfolder_rank_history    → params: { domain: "example.com/blog/", database: "us", display_limit: 24, display_sort: "dt_desc" }
```

---

## 7. "What Technical Issues Are Hurting Us?"

**The diagnostic question:** Are there crawlability, indexability, or performance problems limiting rankings?

### Reports

**Site Audit** (requires an active SEMRush project with Site Audit enabled):

| Report | What It Returns |
|--------|----------------|
| `list_projects` | All projects with IDs |
| `snapshots` | Audit snapshot list for a project |
| `snapshot` | Audit overview: score, issue counts, checks |
| `info` | Most recent audit summary |
| `meta_issues` | Issue descriptions and explanations |
| `issue_details` | URLs affected by a specific issue |
| `page_list` | Search for pages by URL |
| `page_info` | Detailed page-level issues |
| `history` | Audit scores over time |

**Position Tracking** (requires an active tracking campaign):

| Report | What It Returns |
|--------|----------------|
| `campaigns` | Campaign list for a project |
| `tracking_overview_organic` | Keyword distribution across position ranges |
| `tracking_position_organic` | Per-keyword positions and changes over time |
| `tracking_visibility_organic` | Visibility score and trend |

### How to Read the Results

**The Site Health Score is a starting point, not a conclusion.** A score of 85% means 15% of checks found issues. The number alone doesn't tell you whether those issues are blocking traffic or cosmetic. Prioritize by business impact:

| Priority | Criteria | Examples |
|----------|----------|---------|
| P0 — Fix now | Blocking indexation or rendering | Broken canonical tags, noindex on key pages, server errors on high-traffic URLs |
| P1 — Fix this week | Degrading rankings | Duplicate title tags on money pages, slow LCP on key landing pages, redirect chains |
| P2 — Fix this month | Best practices | Missing alt tags, orphan pages with some traffic, HTTP images on HTTPS pages |
| P3 — Backlog | Low impact | Overly long URLs, minor redirect chains on low-traffic pages |

**Connect technical issues to traffic impact.** A redirect chain on a page getting 10,000 visits/month is P1. The same chain on a page with zero traffic is P3. Use `domain_organic_unique` data to weight technical issues by the traffic of affected pages.

### AEO Bridge

Technical SEO is table stakes for AI visibility. AI crawlers (GPTBot, Perplexity-Bot, ClaudeBot) follow the same basic signals search engines do: robots.txt, sitemaps, page speed, mobile rendering. A site that blocks GPTBot or fails to render on mobile loses AI visibility entirely.

Specific technical factors with AI citation impact:
- **Mobile optimization** (53.68% of AI-sourced traffic is mobile; AI crawls mobile version)
- **Schema markup** (FAQ schema = +89% to +221% citation lift; Article schema shows high citation probability)
- **Page speed** (FCP <0.4s = 3x more citations than FCP >1.13s)
- **Semantic HTML** (proper heading hierarchy, 0.65 correlation with AI citation)

The Site Audit doesn't measure all of these directly, but it catches the blocking issues (broken pages, crawl errors, mobile rendering failures) that would prevent any visibility — traditional or AI.

### MCP Call Pattern

```
Step 1: list_projects → params: { filter: "own" }
Step 2: snapshots     → params: { id: "PROJECT_ID" }
Step 3: snapshot      → params: { id: "PROJECT_ID", snapshot_id: "SNAPSHOT_ID" }
Step 4: issue_details → params: { id: "PROJECT_ID", snapshot_id: "SNAPSHOT_ID", issueid: ISSUE_ID, limit: 50 }
```

---

# Part 3: The SEMRush-to-AEO Bridge

## Why This Section Exists

GrowthX operates at the intersection of traditional SEO and AI visibility. No other company connects SEMRush data to AI citation strategy. This section makes that connection explicit.

**The core insight:** SEMRush data measures the traditional search channel. CheckThat data measures the AI channel. The overlap between what drives performance in each channel is significant but not total — and the divergences are where the strategic opportunities live.

## Mapping SEMRush Signals to AEO Scoring

The AEO Content Quality Expert scores content across 9 weighted categories. Here's which SEMRush data informs each:

| AEO Score Category | Weight | SEMRush Data Available | What It Shows | What It Can't Show |
|-------------------|--------|----------------------|---------------|-------------------|
| E-E-A-T & Verified Expertise | 20% | Authority Score, backlink profile quality | Domain-level trust signals | Page-level expertise, author credentials |
| Content Structure & Extractability | 15% | Site Audit (heading hierarchy, schema presence) | Technical structure issues | Whether content is "AI-extractable" |
| Freshness & Update Cadence | 15% | `url_rank_history` trajectory | Whether content is gaining or losing traffic (proxy for freshness) | Actual content update dates |
| Third-Party Validation | 12% | `backlinks_refdomains`, `backlinks_categories_profile` | Which external domains link to you | Whether AI engines actually cite those domains |
| Entity Recognition | 10% | Not directly available | — | Entity count requires content analysis |
| Schema & Structured Data | 8% | Site Audit (structured data checks) | Presence/absence of schema markup | Schema quality or completeness |
| Semantic Completeness | 8% | Keyword count per URL (`url_organic` Pc column) | How many queries a page answers | Whether the content is self-contained |
| Multimodal Content | 7% | Not directly available | — | Requires page-level content audit |
| Brand Authority Signals | 5% | `phrase_this` for brand name volume; `backlinks_overview` score | Brand search demand; domain authority | Cross-platform brand mention frequency |

**SEMRush fully informs:** Third-party validation (12%), Brand authority (5%), and provides strong proxies for Freshness (15%) and Structure (15%).

**SEMRush partially informs:** E-E-A-T (20%) and Semantic completeness (8%) — domain-level signals only.

**SEMRush cannot inform:** Entity recognition (10%) and Multimodal content (7%) — these require content-level analysis tools.

## The Five SEMRush Metrics That Predict AI Visibility

Based on the AEO research correlations, these are the most AI-relevant data points available through SEMRush:

### 1. Brand Search Volume (correlation: 0.334 — strongest predictor)

**Report:** `phrase_this` with the brand name as the phrase.

**What it tells you:** How many people actively search for the brand by name. This is the single strongest predictor of whether AI engines will mention the brand. Brands with no search demand are invisible to AI because they lack the training data footprint and authority signals that AI models use.

**Action threshold:** If brand search volume is <500/month in the US, AI visibility will be an uphill battle. The first priority is building brand awareness through the channels that create search demand: PR, thought leadership, social media, industry events.

### 2. Organic Keyword Count (correlation: 0.41 — outperforms backlinks)

**Report:** `domain_rank` → the Or column.

**What it tells you:** How many keywords the domain ranks for in Google's top 100. This correlates with AI citation at 0.41 — stronger than backlinks (0.218) and nearly as strong as brand search volume. A large keyword footprint signals broad topical coverage, which AI engines interpret as expertise.

**Action threshold:** Compare to competitors via `domain_organic_organic`. If your Or is <50% of the average competitor, your content footprint is too thin for competitive AI visibility.

### 3. Third-Party Referring Domain Profile (6.5x multiplier for AI citations)

**Reports:** `backlinks_refdomains`, `backlinks_categories_profile`.

**What it tells you:** Which external domains link to you, and what categories they belong to. Since 85% of brand mentions in AI answers come from third-party pages (not the brand's own domain), the referring domain profile reveals your third-party validation ecosystem.

**What to look for:**
- **Review platforms** (G2, Capterra, TrustRadius) — 84-88% of review citations in AI answers come from these
- **Press/media** (TechCrunch, Forbes, industry publications) — 95%+ earned media citations
- **Wikipedia** — Nearly 1 in 6 ChatGPT answers cite Wikipedia
- **Reddit** — Top-10 most-cited domain across AI engines
- **Competitor blogs** — If competitors cite you, AI engines weight this heavily

**Action:** Cross-reference `backlinks_refdomains` with CheckThat source analysis. Domains that link to you but don't show up as AI citation sources represent unrealized AEO potential. Domains that show up as AI citation sources for competitors but don't link to you are priority outreach targets.

### 4. Content Trajectory (proxy for freshness — critical for AI citation windows)

**Reports:** `url_rank_history`, `domain_rank_history`.

**What it tells you:** Whether content is gaining or losing traffic over time. Declining content is aging out of AI citation windows. Content in "Freefall" (>50% traffic loss) is almost certainly invisible to Perplexity (2-3 day freshness) and likely invisible to ChatGPT (30-day window).

**Action:** Build a content freshness dashboard. Pull `url_rank_history` for your top 50 content pages. Classify each trajectory. Any page in Declining or Freefall needs a substantive update (not cosmetic) to re-enter AI citation windows.

### 5. Competitive Keyword Gaps (AEO opportunity map)

**Report:** `domain_domains` with gap analysis operators.

**What it tells you:** Topics where competitors rank organically but you don't. Since 99% of URLs in Google AI Mode appear in the top 20 organic results, organic keyword gaps are strongly predictive of AI visibility gaps.

**Action:** Run the "missing keywords" analysis against your top 3 competitors. Filter for commercial and informational intent (In=0 or In=1) with volume >200. These are the topics where competitors are likely visible in AI answers and you're not. Feed this list directly into CheckThat prompt library design — these gaps should become tracked prompts.

## Where SEMRush Ends and CheckThat Begins

| Question | SEMRush Answers | CheckThat Answers |
|----------|----------------|-------------------|
| Does AI mention us? | No — inferred from organic position only | Yes — direct measurement across 5 engines |
| What does AI say about us? | No | Yes — sentiment, narrative, attribute analysis |
| Is AI getting our story right? | No | Yes — alignment scoring against brand truth |
| Which sources drive AI perception? | Partially — referring domain analysis | Yes — source mapping with citation attribution |
| How do we compare to competitors in AI? | Partially — organic competitive position | Yes — visibility score, presence rate, position |
| What's changing over time? | Organic trends only | AI visibility trends, lift measurement |
| What content should we create? | Keyword gaps, content trajectory | Prompt gaps, visibility gaps, content gap loop |

**The handoff workflow:**

```
SEMRush: Domain health → Content analysis → Competitive gaps → Keyword opportunities
                                    ↓
                    Identifies topics and competitive position
                                    ↓
CheckThat: AI visibility measurement → Source analysis → Alignment scoring → Action priorities
                                    ↓
                    Identifies AI perception gaps and citation opportunities
                                    ↓
Content Strategy: Informed by BOTH channels — optimized for search AND AI visibility
```

---

# Part 4: Technical Reference

## How the MCP Works

Every data request follows a 3-step pattern:

```
Step 1: Discovery    →  Call a *_research tool to list available reports
Step 2: Schema       →  Call get_report_schema(report="name") to get parameters
Step 3: Execute      →  Call execute_report(report="name", params={...}) to pull data
```

11 discovery tools expose 84 reports. Traffic Analytics (`trends_research`) requires a separate subscription.

## Column Code Glossary

### Domain and Ranking

| Code | Meaning |
|------|---------|
| Db | Database (regional market code) |
| Dn | Domain name |
| Dt | Date of snapshot (YYYYMMDD) |
| Rk | SEMRush rank (by organic traffic) |

### Organic Search

| Code | Meaning |
|------|---------|
| Or | Organic keywords — count in Google top 100 |
| Ot | Organic traffic — estimated monthly visits |
| Oc | Organic cost — traffic value in Google Ads terms (USD) |

### Paid Search

| Code | Meaning |
|------|---------|
| Ad | Adwords keywords count |
| At | Adwords traffic — estimated monthly visits |
| Ac | Adwords cost — estimated monthly spend (USD) |

### Keyword and Position

| Code | Meaning |
|------|---------|
| Ph | Keyword phrase |
| Po | Position (1-100); 0 = not ranked |
| Pp | Previous position |
| Pd | Position difference |
| Nq | Search volume (avg monthly, last 12 months) |
| Cp | CPC (USD) |
| Co | Competition / advertiser density (0.00-1.00) |
| Kd | Keyword difficulty (0-100) |
| Nr | Number of organic results in Google |
| In | Search intent: 0=Commercial, 1=Informational, 2=Navigational, 3=Transactional |

### Traffic Estimates

| Code | Meaning |
|------|---------|
| Tr | Traffic share (%) of total domain organic traffic |
| Tc | Traffic cost share (%) |
| Tg | Traffic — estimated absolute visits from a keyword |
| Td | Trends — 12-month search volume (comma-separated) |
| Ts | Traffic share (absolute) |

### URL and Page

| Code | Meaning |
|------|---------|
| Ur | URL of the ranking page |
| Pc | Keyword count for the page |
| Sr | SERP features count |
| St | Estimated total traffic for the page |
| Fp | SERP feature positions |
| Fk | Featured keyword position |
| Vu | Visible URL in paid search |

### Competitor Reports

| Code | Meaning |
|------|---------|
| Cr | Competitor relevance (0-1; higher = more keyword overlap) |
| Np | Number of common keywords |

### Rank Difference

| Code | Meaning |
|------|---------|
| Om, Tm, Um, Am, Bm, Cm | Previous-month values for organic/paid metrics |

### Backlink Reports

| Code | Meaning |
|------|---------|
| total | Total backlinks |
| domains_num | Total referring domains |
| urls_num | Total referring URLs |
| ips_num / ipclassc_num | Referring IPs / Class C IPs |
| follows_num / nofollows_num | Follow / nofollow link counts |
| score / trust_score | Authority Score / Trust Score |
| page_score / page_ascore | Page authority of linking page |
| domain_score / domain_ascore | Domain authority of referring domain |
| source_url / source_title | Linking page URL / title |
| target_url | Page being linked to |
| anchor | Anchor text |
| external_num / internal_num | Links on the source page |
| first_seen / last_seen | Discovery / last active date |
| backlinks_num | Backlinks from a referring domain |
| domain / ip / country | Referring domain, IP, country |

### Position Tracking

| Code | Meaning |
|------|---------|
| Sh | Share of Voice |
| Sv | Search Visibility |

## Common Parameters

### database

Two-letter country code. Most-used: `us`, `uk`, `ca`, `au`, `de`, `fr`. Mobile: `mobile-us`, `mobile-uk`, etc.

### display_limit and display_offset

| Parameter | Default | Max | Notes |
|-----------|---------|-----|-------|
| display_limit | 50 | 4,000,000 (most reports) | Use 30-50 for exploration; higher for exports |
| display_offset | 0 | — | Add to display_limit when paginating past 100k |

### display_date

Format: `YYYYMM15` for monthly (e.g., `20231215`). Use `display_daily` (format `YYYYMMDD`) for daily changes in the last 31 days. Omit for latest data.

### display_sort

Format: `column_asc` or `column_desc`. Values vary by report.

## Filter Syntax

Format: `<sign>|<field>|<operation>|<value>`

| Component | Values |
|-----------|--------|
| Sign | `+` (include) or `-` (exclude) |
| Field | Any column code (Ph, Nq, Po, Ur, Co, Kd, etc.) |
| Operation | Eq, Co (contains), Bw (begins with), Ew (ends with), Lt, Gt, Le, Ge |

Multiple filters separated by `|`. Max 25 per request.

**Common filters:**

| Goal | Filter |
|------|--------|
| Blog pages only | `+\|Ur\|Co\|/blog/` |
| Quick wins (pos 4-20, vol >100) | `+\|Po\|Gt\|3\|+\|Po\|Lt\|21\|+\|Nq\|Gt\|100` |
| Exclude branded terms | `-\|Ph\|Co\|brandname` |
| Low-difficulty opportunities | `+\|Kd\|Lt\|40\|+\|Nq\|Gt\|500` |
| High-volume keywords | `+\|Nq\|Gt\|1000` |

## Complete Report Catalog

### Domain Overview (`overview_research`) — 5 reports

| Report | Description | Required Params |
|--------|-------------|----------------|
| `domain_rank` | Domain ranking in one database | domain, database |
| `domain_rank_history` | Historical ranking trends | domain, database |
| `domain_ranks` | Rankings across all databases | domain |
| `overview_rank` | Top domains by traffic rank | database |
| `rank_difference` | Winners/losers ranking changes | database |

### Organic Research (`organic_research`) — 12 reports

| Report | Description | Required Params |
|--------|-------------|----------------|
| `domain_organic` | Organic keywords and positions | domain, database |
| `domain_organic_unique` | Unique pages ranking in top 100 | domain, database |
| `domain_organic_organic` | Organic competitors | domain, database |
| `domain_organic_subdomains` | Subdomains ranking in top 100 | domain, database |
| `domain_domains` | Keyword gap between domains | domains (special format), database |
| `domain_adwords` | Paid search keywords | domain, database |
| `domain_adwords_adwords` | Paid search competitors | domain, database |
| `domain_adwords_historical` | Paid keyword history (12 months) | domain, database |
| `domain_adwords_unique` | Unique ad copies | domain, database |
| `domain_shopping` | Shopping ads data | domain, database |
| `domain_shopping_shopping` | Detailed shopping data | domain, database |
| `domain_shopping_unique` | Unique shopping ads | domain, database |

### Backlink Analytics (`backlink_research`) — 15 reports

| Report | Description | Required Params |
|--------|-------------|----------------|
| `backlinks_overview` | High-level metrics: links, domains, authority | target, target_type |
| `backlinks` | Complete backlink list | target, target_type |
| `backlinks_refdomains` | Referring domains | target, target_type |
| `backlinks_anchors` | Anchor text distribution | target, target_type |
| `backlinks_pages` | Pages receiving backlinks | target, target_type |
| `backlinks_historical` | Monthly backlink trends | target (root_domain only) |
| `backlinks_competitors` | Similar backlink profiles | target, target_type |
| `backlinks_comparison` | Compare multiple domain profiles | targets[], target_types[] |
| `backlinks_matrix` | Shared referring domains across targets | targets[], target_types[] |
| `backlinks_ascore_profile` | Authority Score distribution | target, target_type |
| `backlinks_geo` | Geographic distribution | target, target_type |
| `backlinks_tld` | TLD distribution | target, target_type |
| `backlinks_categories` | Domain categories | target, target_type |
| `backlinks_categories_profile` | Referring domain categories | target, target_type |
| `backlinks_refips` | Referring IP addresses | target, target_type |

### Keyword Research (`keyword_research`) — 10 reports

| Report | Description | Required Params |
|--------|-------------|----------------|
| `phrase_this` | Single keyword overview (one database) | phrase, database |
| `phrase_all` | Single keyword across all databases | phrase |
| `phrase_these` | Batch keyword analysis (semicolon-separated) | phrase, database |
| `phrase_organic` | Domains ranking for a keyword | phrase, database |
| `phrase_related` | Semantically related keywords | phrase, database |
| `phrase_fullsearch` | Broad match / all containing queries | phrase, database |
| `phrase_questions` | Question-format queries (max 100) | phrase, database |
| `phrase_kdi` | Keyword difficulty (batch, 1-100 keywords) | phrase, database |
| `phrase_adwords` | Paid search SERP for a keyword | phrase, database |
| `phrase_adwords_historical` | Historical paid positions | phrase, database |

### URL Analytics (`url_research`) — 5 reports

| Report | Description | Required Params |
|--------|-------------|----------------|
| `url_organic` | Keywords driving traffic to a URL | url, database |
| `url_rank_history` | Historical rankings for a URL | url, database |
| `url_rank` | Current rankings (one database) | url, database |
| `url_ranks` | Rankings across all databases | url |
| `url_adwords` | Paid keywords for a URL | url, database |

### Subdomain Analytics (`subdomain_research`) — 7 reports

| Report | Description | Required Params |
|--------|-------------|----------------|
| `subdomain_organic` | Organic keywords for a subdomain | domain, database |
| `subdomain_organic_unique` | Unique pages ranking | domain, database |
| `subdomain_rank` | Current rankings | domain, database |
| `subdomain_rank_history` | Historical rankings | domain, database |
| `subdomain_ranks` | Rankings across all databases | domain |
| `subdomain_adwords` | Paid keywords | domain, database |
| `subdomain_adwords_unique` | Unique ad copies | domain, database |

### Subfolder Analytics (`subfolder_research`) — 7 reports

Same pattern as subdomain; requires trailing slash on subfolder paths.

| Report | Description | Required Params |
|--------|-------------|----------------|
| `subfolder_organic` | Organic keywords for a subfolder | domain (with path/), database |
| `subfolder_organic_unique` | Unique pages ranking | domain, database |
| `subfolder_rank` | Current rankings | domain, database |
| `subfolder_rank_history` | Historical rankings | domain, database |
| `subfolder_ranks` | Rankings across all databases | domain |
| `subfolder_adwords` | Paid keywords | domain, database |
| `subfolder_adwords_unique` | Unique ad copies | domain, database |

### Position Tracking (`tracking_research`) — 13 reports

Requires active SEMRush project with Position Tracking campaign.

| Report | Description | Required Params |
|--------|-------------|----------------|
| `campaigns` | List campaigns for a project | project_id |
| `tracking_campaign_dates` | Dates data was harvested | campaign_id |
| `tracking_overview_organic` | Keyword distribution and changes | campaign_id, url |
| `tracking_overview_adwords` | Paid position overview | campaign_id, url |
| `tracking_position_organic` | Per-keyword positions and changes | campaign_id, url |
| `tracking_position_adwords` | Per-keyword paid positions | campaign_id, url |
| `tracking_competitors_organic` | Competitor visibility | campaign_id, url |
| `tracking_competitors_adwords` | Paid competitor visibility | campaign_id, url |
| `tracking_landing_pages_organic` | Landing pages from tracking | campaign_id, url |
| `tracking_landing_pages_adwords` | Paid landing pages | campaign_id, url |
| `tracking_visibility_organic` | Visibility score over time | campaign_id, url |
| `tracking_visibility_adwords` | Paid visibility over time | campaign_id, url |
| `locations` | Location lookup for tracking | (varies) |

### Site Audit (`siteaudit_research`) — 8 reports

Requires active SEMRush project with Site Audit enabled.

| Report | Description | Required Params |
|--------|-------------|----------------|
| `snapshots` | List audit snapshots | id (project) |
| `snapshot` | Audit overview (score, issues, checks) | id, snapshot_id |
| `info` | Most recent audit summary | id |
| `history` | Audit results over time | id |
| `meta_issues` | Issue descriptions | id |
| `issue_details` | URLs affected by an issue | id, snapshot_id, issueid |
| `page_list` | Search pages by URL | id, url |
| `page_info` | Detailed page issues | id, pageid |

### Project Management (`projects_research`) — 2 reports

| Report | Description | Required Params |
|--------|-------------|----------------|
| `list_projects` | All projects | filter (optional) |
| `get_project` | Single project details | (project ID) |

### Traffic Analytics (`trends_research`)

**Not available on current plan.** Requires separate subscription at semrush.com/analytics/traffic/trends-api. Would provide website traffic estimates, audience demographics, and competitive traffic analysis.

---

# Part 5: GrowthX Recipes

Named workflows for common audit scenarios. Each recipe lists the objective, reports in sequence, key parameters, what to look for, and where to go next.

## Recipe 1: Strategy Sprint Week 1 Audit

**Objective:** Baseline assessment of a new client's organic and content health within the first week of a Strategy Sprint engagement.

**Duration:** 2-4 hours for data pull; 2-4 hours for analysis.

### Steps

| Step | Report | Parameters | Purpose |
|------|--------|-----------|---------|
| 1 | `domain_rank` | database=us | Domain snapshot |
| 2 | `domain_rank_history` | database=us, display_limit=24, display_sort=dt_desc | 24-month trend |
| 3 | `backlinks_overview` | target_type=root_domain | Authority baseline |
| 4 | `domain_organic_unique` | database=us, display_limit=10000, display_sort=tr_desc | All indexed pages |
| 5 | `domain_organic` | database=us, display_limit=10000, export_columns=Ur,Ph,Po,Nq,Tr,Tc,In,Kd | Full keyword list |
| 6 | `domain_organic_organic` | database=us, display_limit=20 | Competitor discovery |
| 7 | `phrase_this` | phrase="brand name", database=us | Brand search volume |

### What to Look For

- **Health trajectory:** Is Ot trending up, down, or flat over 12-24 months?
- **Content vs. brand split:** What percentage of traffic goes to content pages vs. brand pages? (Classify from step 4)
- **Index efficiency:** What percentage of indexed pages get zero traffic?
- **Authority baseline:** How does the Authority Score compare to the competitors found in step 6?
- **Brand search volume:** Is there enough demand to support AI visibility? (<500/month = warning)
- **Quick wins:** Filter step 5 for positions 4-20, volume >100

### Where to Go Next

- If the domain is in decline → Run the Content Trajectory Analysis recipe to identify which sections are failing
- If competitors are significantly ahead → Run the Competitive Deep Dive recipe
- If the site has technical issues → Set up a Site Audit project and run the technical assessment
- Always → Feed brand search volume and competitor list into CheckThat for AI visibility assessment

**Cross-reference:** `seo-domain-audit` skill automates steps 1-5.

---

## Recipe 2: Quarterly Domain Review

**Objective:** Track progress against the baseline established in Week 1. Identify what's improved, what's degraded, and where to invest next quarter.

**Duration:** 1-2 hours.

### Steps

| Step | Report | Parameters | Purpose |
|------|--------|-----------|---------|
| 1 | `domain_rank` | database=us | Current snapshot |
| 2 | `domain_rank_history` | database=us, display_limit=6, display_sort=dt_desc | Last 6 months vs. baseline |
| 3 | `domain_organic` | display_positions=new, database=us, display_limit=100 | New keywords gained |
| 4 | `domain_organic` | display_positions=lost, database=us, display_limit=100 | Keywords lost |
| 5 | `backlinks_historical` | target_type=root_domain, display_limit=12 | Authority trend |
| 6 | `phrase_this` | phrase="brand name", database=us | Brand volume check |

### What to Look For

- **Net keyword change:** Are you gaining more keywords than losing?
- **Traffic per keyword efficiency:** Is Ot/Or improving? (More traffic per keyword = better position quality)
- **Lost keyword analysis:** Are the lost keywords low-value (acceptable) or high-value (concerning)?
- **Authority momentum:** Is the referring domain count growing, stable, or declining?
- **Brand trajectory:** Is brand search volume growing? This predicts AI visibility trajectory.

---

## Recipe 3: Competitive Deep Dive

**Objective:** Understand how a specific competitor outperforms the client domain and where the opportunities are.

**Duration:** 2-3 hours.

### Steps

| Step | Report | Parameters | Purpose |
|------|--------|-----------|---------|
| 1 | `domain_rank` | For both domains, database=us | Side-by-side snapshot |
| 2 | `domain_rank_history` | For both domains, display_limit=24 | Trend comparison |
| 3 | `domain_domains` | Missing keywords format, database=us, display_limit=500 | What they rank for that you don't |
| 4 | `domain_domains` | Shared keywords format, display_sort=nq_desc | Battleground keywords |
| 5 | `backlinks_comparison` | Both domains as targets | Authority comparison |
| 6 | `backlinks_matrix` | Both domains, display_limit=50 | Shared vs. unique referring domains |
| 7 | `domain_organic_unique` | Competitor domain, display_limit=5000 | Their content structure |

### What to Look For

- **Traffic ratio:** What tier is the competitor? (Leader, Challenger, Peer, Trailing)
- **Missing keyword themes:** Group missing keywords by topic. Which themes represent the biggest gaps?
- **Content gap vs. authority gap:** For shared keywords where they outrank you, is the difference content or authority?
- **Their linking sources:** From the matrix, which authoritative domains link to them but not to you?
- **Content structure:** How does their page mix (brand/content/docs/templates) compare to yours?

### AEO Application

Feed the missing keyword themes into CheckThat prompt library design. If the competitor ranks for "best [category] for [use case]" keywords you don't, those are almost certainly AI visibility gaps too. The referring domains that link to the competitor but not to you are high-priority for third-party validation outreach.

**Cross-reference:** `competitive-seo-landscape` skill automates steps 1-2 across multiple competitors.

---

## Recipe 4: Content Trajectory Analysis

**Objective:** Classify every content page by performance trajectory to prioritize refresh, expand, or retire decisions.

**Duration:** 3-5 hours (depends on content volume).

### Steps

| Step | Report | Parameters | Purpose |
|------|--------|-----------|---------|
| 1 | `domain_organic_unique` | database=us, display_limit=10000, display_filter=+\|Ur\|Co\|/blog/ | All content pages |
| 2 | `domain_organic` | database=us, display_date=6 months ago | Historical keyword data |
| 3 | `url_rank_history` | For top 50-100 pages, display_limit=15, display_sort=dt_desc | Per-page trajectory |
| 4 | `url_organic` | For pages in Freefall or Declining | Current keyword portfolio |

### Classification

For each content page, compare current Ot to 6-months-ago Ot:

| Change | Trajectory | Action |
|--------|-----------|--------|
| >+100% or new | **Surging** | Scale: create supporting content, build internal links |
| +25% to +100% | **Growing** | Optimize: add schema, update for AI extractability, target adjacent keywords |
| -10% to +25% | **Stable** | Maintain: update quarterly, monitor for decline signals |
| -10% to -50% | **Declining** | Refresh: substantive content update, add original research, update data |
| >-50% loss | **Freefall** | Triage: major rewrite, redirect, or retire |
| Zero throughout | **Dead** | Evaluate: is the topic worth pursuing? If yes, complete rewrite. If no, remove. |

### AEO Application

Pages classified as Declining or Freefall are outside AI citation freshness windows. Prioritize these for content refresh — not just for SEO recovery, but to re-enter the 30-day (ChatGPT) and 2-3 day (Perplexity) citation windows. A declining page that gets a substantive update can simultaneously recover organic traffic and become AI-visible again.

Pages classified as Surging or Growing are your strongest candidates for AI citation optimization: add FAQ schema (+89-221% citation lift), ensure clear H2/H3 hierarchy, add answer capsules at the top of each section.

**Cross-reference:** `content-pages-audit` skill automates steps 1-2 and produces the traffic comparison.

---

## Recipe 5: Brand Authority Assessment

**Objective:** Evaluate the domain's authority position and third-party validation ecosystem for both SEO and AEO implications.

**Duration:** 1-2 hours.

### Steps

| Step | Report | Parameters | Purpose |
|------|--------|-----------|---------|
| 1 | `backlinks_overview` | target_type=root_domain | Authority baseline |
| 2 | `backlinks_refdomains` | display_limit=200, display_sort=domain_ascore_desc | Top referring domains by authority |
| 3 | `backlinks_categories_profile` | target_type=root_domain | What types of sites link to you |
| 4 | `backlinks_anchors` | display_limit=50, display_sort=domains_num_desc | Anchor text health |
| 5 | `backlinks_historical` | target_type=root_domain, display_limit=24 | 24-month authority trend |
| 6 | `phrase_this` | phrase="brand name", database=us | Brand search volume |
| 7 | `backlinks_competitors` | target_type=root_domain, display_limit=20 | Domains with similar link profiles |

### What to Look For

- **Authority Score vs. competitors:** How does it compare?
- **Referring domain quality:** What percentage of top referring domains are authoritative (score >50)?
- **Category distribution:** Are links coming from relevant industry sources, or generic directories?
- **Anchor text health:** Is the distribution natural (60-70% branded)?
- **Authority momentum:** Is the referring domain count growing or declining month-over-month?
- **Brand demand:** What's the monthly search volume for the brand name?

### AEO Application

Reframe the referring domain list as a **third-party validation map**:
- Which review platforms (G2, Capterra, TrustRadius) link to you? These drive 84-88% of AI review citations.
- Is Wikipedia linking to you? This drives ~16% of ChatGPT citations.
- Which press/media domains link to you? These drive 95%+ of AI earned media citations.
- Which competitor or industry blogs link to you? These create the cross-reference signals AI engines use for evaluation.

Domains that link to you but aren't showing up in CheckThat source analysis represent untapped AEO potential. Domains that appear in competitor CheckThat source analysis but don't link to you are the highest-priority outreach targets.
