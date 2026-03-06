# DataForSEO MCP — Complete Reference Guide

<metadata>
purpose: Definitive reference for every tool available through the DataForSEO MCP server, with parameters, expert context on why each matters, and GrowthX usage patterns
access: build-team
related: projects/audit-methodology/semrush-mcp-field-guide-v1.md, context/roles/seo-content-quality-expert-v1.md, context/roles/aeo-expert-v1.md, context/roles/aeo-content-quality-expert-v1.md
last_updated: 2026-03-05
</metadata>

---

## How the MCP Works

The DataForSEO MCP exposes **79 tools** across **9 categories**. Unlike the SEMRush MCP (which requires a 3-step discovery/schema/execute pattern), DataForSEO tools are **called directly by name** with JSON parameters.

```
Call tool_name with { param1: value1, param2: value2 }
```

No discovery step. No schema lookup. Every tool is a direct endpoint.

The 9 categories:

| # | Category | Tools | What It Covers |
|---|----------|-------|----------------|
| 1 | **DataForSEO Labs** | 21 | Domain rankings, keyword intelligence, competitor analysis, content gap |
| 2 | **AI Optimization** | 13 | LLM mentions, ChatGPT scraping, AI search volume, LLM responses |
| 3 | **Backlinks** | 20 | Link profiles, referring domains, anchors, intersection, spam, time series |
| 4 | **SERP** | 7 | Live Google/YouTube search results |
| 5 | **Content Analysis** | 3 | Web citation data, sentiment, phrase trends |
| 6 | **Keyword Data** | 7 | Google Ads volume, Google Trends, DFS Trends, demographics |
| 7 | **On Page** | 3 | Lighthouse, page-level SEO, content parsing |
| 8 | **Domain Analytics** | 4 | Technology detection, WHOIS |
| 9 | **Business Data** | 1 | Google Maps business listings |

**Current GrowthX usage:** Only `dataforseo_labs_google_domain_rank_overview` is used — by 3 skills (`seo-domain-audit`, `competitive-seo-landscape`, `competitive-comparison-table`). The remaining 78 tools are untapped. The AI Optimization category is the highest-priority expansion area.

---

## Common Parameters

### Location and Language

Most tools accept `location_name` and `language_code`. Defaults vary by category.

| Parameter | Format | Default | Notes |
|-----------|--------|---------|-------|
| `location_name` | Full country name | `"United States"` (Labs), varies elsewhere | Country only for Labs; hierarchical for SERP (e.g., `"San Francisco,California,United States"`) |
| `language_code` | ISO 639-1 | `"en"` | Two-letter code: `en`, `de`, `fr`, `es`, `ja`, etc. |

Utility tools for discovering valid location/language combinations:
- `ai_opt_kw_data_loc_and_lang` — AI Optimization keyword data
- `ai_opt_llm_ment_loc_and_lang` — LLM mentions
- `serp_locations` — Google SERP
- `serp_youtube_locations` — YouTube SERP
- `kw_data_google_ads_locations` — Google Ads keyword data

### Pagination

| Parameter | Default | Max | Notes |
|-----------|---------|-----|-------|
| `limit` | 10 | 1,000 | Number of results to return |
| `offset` | 0 | — | Skip N results for pagination |

### Sorting

`order_by` is an array of strings in `"field,direction"` format. Maximum 3 sorting rules.

```json
["keyword_data.keyword_info.search_volume,desc"]
["keyword_data.keyword_info.search_volume,desc", "keyword_data.keyword_info.cpc,desc"]
```

### Filter Syntax

Filters follow a shared format across all tools. Array-based with logical operators.

**Single filter:**
```json
[["field_name", "operator", "value"]]
```

**Multiple filters with logical operators:**
```json
[["field_a", ">", 1000], "and", ["field_b", "<>", "paid"]]
```

**Nested filters:**
```json
[["field_a", "<>", 0], "and", [["field_b", "<>", "paid"], "or", ["field_c", "=", false]]]
```

**Available operators:**

| Operator | Meaning |
|----------|---------|
| `=` | Equals |
| `<>` | Not equals |
| `<`, `<=`, `>`, `>=` | Numeric comparison |
| `in`, `not_in` | Value in/not in array |
| `like`, `not_like` | Pattern match (`%` wildcard) |
| `ilike`, `not_ilike` | Case-insensitive pattern match |
| `regex`, `not_regex` | Regular expression match |
| `match`, `not_match` | Full-text match |
| `has`, `has_not` | Array contains / doesn't contain |

**Logical connectors:** `"and"`, `"or"` — must be strings connecting two filter arrays.

**Limits:** Maximum 8 filters per request. Maximum 3 sort rules per request.

Each category has a filter documentation utility (`*_available_filters`) that lists all filterable fields.

---

## 1. DataForSEO Labs — Domain & Keyword Intelligence

**21 tools.** The keyword and domain intelligence engine. Provides ranking data, keyword metrics, competitor discovery, keyword gap analysis, and content ideation. This is DataForSEO's equivalent to SEMRush's organic research, but built on a different crawl index with independent data.

**Why a second data source matters:** No single SEO tool has complete data. SEMRush and DataForSEO crawl at different frequencies, use different estimation models, and often disagree on absolute numbers. Cross-referencing both sources catches blind spots and validates signals. When both sources agree on a trend (rising, declining, stable), confidence is high. When they disagree, that's a signal to investigate deeper.

---

### dataforseo_labs_google_domain_rank_overview

Ranking and traffic data from organic and paid search for a domain. Returns keyword position distribution across SERP buckets and directional momentum (rising, declining, new keywords).

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain name without protocol |
| `location_name` | string | No | `"United States"` | Country only |
| `language_code` | string | No | `"en"` | |
| `ignore_synonyms` | boolean | No | `true` | More accurate when true |

**Why it matters:** Position distribution tells you more than total keyword count. A domain with 50,000 keywords but 90% in positions 50+ is weaker than one with 10,000 keywords concentrated in the top 10. The momentum metrics (is_new, is_up, is_down) reveal whether a domain is gaining or losing ground — critical for competitive analysis and for detecting the impact of algorithm updates.

**GrowthX usage:** Core tool in 3 skills. Called for every domain in competitive analysis. Key derived metrics:
- Top-3 concentration = `(pos_1 + pos_2_3) / total_keywords`
- Top-10 concentration = `(pos_1 + pos_2_3 + pos_4_10) / total_keywords`
- KW Net momentum = `is_new - is_down`

---

### dataforseo_labs_google_ranked_keywords

Keywords a domain or page ranks for, with SERP element data, impressions, search volume, and position.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain (no protocol) or page URL (with protocol) |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | Up to 8 filters |
| `order_by` | array | No | `rank_group,asc` | Up to 3 sort rules |
| `include_subdomains` | boolean | No | — | Include subdomain keywords |
| `include_clickstream_data` | boolean | No | `false` | Adds real-user click metrics |
| `item_types` | array | No | `["organic"]` | `organic`, `paid`, `featured_snippet`, `local_pack`, `ai_overview_reference` |

**Why it matters:** This is the detailed keyword portfolio. Where `domain_rank_overview` gives you distribution, this gives you the actual keywords. The `item_types` parameter is particularly valuable — you can filter for `ai_overview_reference` to see which keywords trigger AI Overviews that cite this domain. That's a direct bridge between SEO and AEO.

**Opportunity:** Cross-validate against SEMRush's `domain_organic` report. Use `item_types: ["ai_overview_reference"]` to identify which of a domain's keywords are getting AI Overview citations — feeds directly into AEO strategy.

**Useful filters:**
```json
// High-value keywords in striking distance
[["ranked_serp_element.serp_item.rank_group", "<=", 20], "and", ["keyword_data.keyword_info.search_volume", ">", 100]]

// Featured snippet opportunities
[["ranked_serp_element.serp_item.type", "=", "featured_snippet"]]
```

---

### dataforseo_labs_google_keyword_overview

Keyword data including CPC, competition, search volume, intent classification, and monthly search trends.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keywords` | string[] | Yes | — | Up to 700 keywords (max 80 chars, 10 words each) |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `include_clickstream_data` | boolean | No | `false` | Real-user click metrics |

**Why it matters:** Bulk keyword lookup with intent classification. The intent data is particularly useful — knowing whether a keyword is informational, commercial, navigational, or transactional determines what content format should target it. The monthly search volume trends (12-month breakdown) reveal seasonality that aggregate volume hides.

---

### dataforseo_labs_google_historical_keyword_data

Historical keyword data going back to August 2021. Monthly snapshots of volume, CPC, and competition.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keywords` | string[] | Yes | — | Up to 700 keywords |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |

**Why it matters:** Keyword trajectory over years. A keyword showing steady growth over 18 months is a fundamentally different investment than one that peaked and is declining. Also reveals which keywords are trending toward zero — content targeting dying queries is wasted effort.

---

### dataforseo_labs_google_historical_rank_overview

Historical ranking and traffic trends for a domain over time.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain name |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `ignore_synonyms` | boolean | No | `true` | |
| `include_clickstream_data` | boolean | No | `false` | |

**Why it matters:** Domain-level trajectory. Shows how a domain's total organic keywords, traffic, and paid presence have changed over time. Critical for establishing whether a domain is on an upward or downward trajectory before recommending strategy. A domain that lost 40% of traffic in the last 6 months needs a very different playbook than one that's been steadily growing.

**Opportunity:** Use alongside SEMRush's `domain_rank_history` for cross-validated trend analysis. Where they agree, you have strong evidence. Where they diverge, the truth often lies between them.

---

### dataforseo_labs_google_historical_serp

Historical Google SERPs for a specific keyword. Shows who ranked where over time.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keyword` | string | Yes | — | Target keyword |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |

**Why it matters:** Shows the competitive history of a SERP. Who held position 1 last year? Who displaced them? This reveals SERP volatility (high-churn SERPs are more attackable) and the types of content Google has rewarded over time for that query.

---

### dataforseo_labs_google_competitors_domain

Competitor domains based on keyword overlap. Returns domains that rank for similar keywords with relevance scoring.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain name |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `exclude_top_domains` | boolean | No | `true` | Removes Wikipedia, YouTube, etc. |
| `include_clickstream_data` | boolean | No | `false` | |
| `item_types` | array | No | — | `organic`, `paid`, `featured_snippet`, `local_pack` |

**Why it matters:** Algorithmic competitor discovery. Your SEO competitors are rarely the companies you compete with commercially — they're whoever Google surfaces for the same queries. This tool finds them by overlap, not assumption. The `exclude_top_domains` flag filters out Wikipedia and YouTube, which would otherwise dominate every competitor list.

---

### dataforseo_labs_google_domain_intersection

Keywords two domains both rank for in the same SERP.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target1` | string | Yes | — | First domain |
| `target2` | string | Yes | — | Second domain |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `ignore_synonyms` | boolean | No | `true` | |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `intersections` | boolean | No | `true` | When true, both domains must appear in same SERP |
| `include_clickstream_data` | boolean | No | `false` | |
| `item_types` | array | No | — | `organic`, `paid`, `featured_snippet`, `local_pack` |

**Why it matters:** Head-to-head keyword gap analysis. Shows exactly which keywords you and a competitor both target, and who ranks higher for each. When `intersections` is false, it returns ALL keywords either domain ranks for — including gaps where one ranks and the other doesn't. That gap is your content opportunity map.

**Opportunity:** Pair with SEMRush's `domain_domains` report for comprehensive gap analysis. Each tool catches keywords the other misses.

---

### dataforseo_labs_google_page_intersection

Keywords for which specified pages rank together in the same SERP. Supports up to 20 pages with wildcard matching.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `pages` | string[] | Yes | — | Up to 20 absolute URLs (supports `*` wildcard) |
| `exclude_pages` | string[] | No | — | Up to 10 URLs to exclude |
| `intersection_mode` | string | No | — | `union` or `intersect` |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `ignore_synonyms` | boolean | No | `true` | |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `include_clickstream_data` | boolean | No | `false` | |
| `item_types` | array | No | — | `organic`, `paid`, `featured_snippet`, `local_pack` |

**Why it matters:** Page-level gap analysis. Unlike domain intersection (which finds overlapping keywords between domains), this finds overlapping keywords between specific pages. Use wildcards like `https://competitor.com/blog/*` to compare entire blog sections. The `intersect` mode finds keywords ALL specified pages rank for — the shared battleground. The `union` mode finds keywords ANY specified page ranks for — the total addressable space.

---

### dataforseo_labs_google_relevant_pages

Page-level rankings and traffic data for a domain. Shows which pages drive the most organic value.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain name |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `ignore_synonyms` | boolean | No | `true` | |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `exclude_top_domains` | boolean | No | `true` | |
| `item_types` | array | No | — | `organic`, `paid`, `featured_snippet`, `local_pack` |
| `include_clickstream_data` | boolean | No | `false` | |

**Why it matters:** Identifies a domain's most valuable pages by organic traffic contribution. In most domains, 10-20% of pages drive 80%+ of traffic. Finding those pages — and understanding which keywords drive them — is the foundation of any content optimization strategy.

---

### dataforseo_labs_google_subdomains

Subdomains with their ranking and traffic breakdown.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain name |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `ignore_synonyms` | boolean | No | `true` | |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `item_types` | array | No | — | |
| `include_clickstream_data` | boolean | No | `false` | |

**Why it matters:** Information architecture analysis. Shows how traffic distributes across `blog.`, `docs.`, `help.`, `app.`, etc. A domain where 90% of traffic goes to the docs subdomain has a very different SEO opportunity than one where the blog drives the most traffic. Also reveals orphaned subdomains that might be diluting authority.

---

### dataforseo_labs_google_serp_competitors

Domains ranking for a given set of keywords. Finds who competes in specific keyword clusters.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keywords` | string[] | Yes | — | Up to 200 keywords |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `include_subdomains` | boolean | No | — | |
| `item_types` | array | No | — | `organic`, `paid`, `featured_snippet`, `local_pack` |

**Why it matters:** Keyword-driven competitor discovery. Instead of asking "who competes with this domain?" you ask "who ranks for these specific keywords?" This is how you find competitors for a specific content cluster or product category rather than at the whole-domain level.

---

### dataforseo_labs_google_keyword_suggestions

Keywords containing the seed keyword with volume, CPC, and competition data.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keyword` | string | Yes | — | Seed keyword |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `include_clickstream_data` | boolean | No | `false` | |

**Why it matters:** Long-tail expansion. Given a head term, returns variations that contain it. The `include_clickstream_data` option adds real user engagement metrics beyond Google's estimated volume — revealing which variations people actually click on, not just search for.

---

### dataforseo_labs_google_related_keywords

"Searches related to" keywords — the semantic neighbors of a seed keyword.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keyword` | string | Yes | — | Seed keyword |
| `depth` | number | No | 1 | 0–4; deeper = more tangential results |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `include_clickstream_data` | boolean | No | `false` | |

**Why it matters:** Semantic expansion for content clustering. Unlike keyword suggestions (which find variations containing the seed), related keywords find topically adjacent terms. At depth 1, you get close neighbors. At depth 4, you reach tangential topics. This maps the semantic territory around a topic — essential for building topical authority clusters that Google rewards with 30% more traffic (per correlation studies).

---

### dataforseo_labs_google_keyword_ideas

Keyword ideas from product or service categories.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keywords` | string[] | Yes | — | Up to 200 seed keywords |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `include_clickstream_data` | boolean | No | `false` | |

**Why it matters:** Category-level keyword discovery. Takes multiple seed keywords and returns ideas from the broader category, not just variations of the inputs. Useful when building out a content strategy for a new topic area.

---

### dataforseo_labs_google_keywords_for_site

Keywords relevant to a specific domain.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain name |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `include_subdomains` | boolean | No | — | |
| `include_clickstream_data` | boolean | No | `false` | |

**Why it matters:** Reverse-engineers a domain's keyword universe. Different from `ranked_keywords` (which shows what you rank for) — this shows keywords DataForSEO's algorithms consider relevant to your domain based on content analysis and SERP co-occurrence. Reveals keyword opportunities you're not yet targeting.

---

### dataforseo_labs_google_top_searches

Top searches from DataForSEO's 7B+ keyword database.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `include_clickstream_data` | boolean | No | `false` | |

**Why it matters:** Market-level search intelligence. What are people searching for most? Useful for identifying emerging trends and validating whether a target topic has meaningful search demand.

---

### dataforseo_labs_bulk_traffic_estimation

Traffic estimates for up to 1,000 domains, subdomains, or pages in a single call.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `targets` | string[] | Yes | — | Up to 1,000 targets |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |
| `ignore_synonyms` | boolean | No | `true` | |
| `item_types` | array | No | `["organic"]` | `organic`, `paid`, `featured_snippet`, `local_pack` |

**Why it matters:** Batch competitive benchmarking. Get traffic estimates for an entire competitive set in one call. Perfect for the competitive landscape tier analysis that GrowthX does — sort 30+ competitors by estimated traffic in a single API call.

**Opportunity:** Replace multiple individual `domain_rank_overview` calls in the competitive landscape skill with a single bulk call for traffic data.

---

### dataforseo_labs_bulk_keyword_difficulty

Keyword Difficulty scores (0–100) for up to 1,000 keywords in a single call.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keywords` | string[] | Yes | — | Up to 1,000 keywords |
| `location_name` | string | No | `"United States"` | |
| `language_code` | string | No | `"en"` | |

**Why it matters:** Content prioritization. Keyword difficulty estimates how hard it will be to rank in the top 10. Combined with search volume, this produces the ROI prioritization matrix: high volume + low difficulty = quick wins. High volume + high difficulty = long-term investments.

---

### dataforseo_labs_search_intent

Search intent classification (informational, navigational, commercial, transactional) for up to 1,000 keywords.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keywords` | string[] | Yes | — | Up to 1,000 keywords |
| `language_code` | string | No | `"en"` | |

**Why it matters:** Intent determines content format. Informational queries need guides and explainers. Commercial queries need comparisons and reviews. Transactional queries need product pages. Mismatching content format to intent is one of the most common SEO mistakes — and one of the easiest to fix once you have intent data at scale.

---

### dataforseo_labs_available_filters

Documentation utility listing all filterable fields for Labs endpoints.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `tool` | string | No | — | Specific tool name to get filters for |

---

## 2. AI Optimization — LLM Visibility & Mentions

**13 tools.** The AEO-specific category. Measures how AI models (ChatGPT, Gemini, Claude, Perplexity) mention, cite, and reference brands and domains. This is where DataForSEO uniquely complements CheckThat — it provides a different angle on AI visibility through its own crawl of LLM responses.

**Why this category is transformative for GrowthX:** CheckThat measures AI visibility through its own prompt methodology (RECALL, SENTIMENT, ALIGNMENT, LIFT). DataForSEO's AI Optimization tools provide a complementary data source: aggregated LLM mention metrics from their own crawl of AI responses. Cross-referencing both sources — CheckThat's structured brand research approach and DataForSEO's broad crawl data — produces a more complete picture of AI visibility than either alone.

**Key AEO context:** 87% of AI referral traffic comes from ChatGPT. 67% of domains are cited by only one AI engine. Brand search volume is the strongest predictor of AI citations (0.334 correlation). Third-party validation produces 6.5x more citations than owned content. These numbers from GrowthX's own research should inform how you interpret every tool in this category.

---

### ai_optimization_llm_response

Query any supported LLM directly and get a structured response.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `llm_type` | string | Yes | — | `claude`, `gemini`, `chat_gpt`, `perplexity` |
| `user_prompt` | string | Yes | — | Up to 500 characters |
| `model_name` | string | Yes | — | Model name + version (use `ai_optimization_llm_models` to discover) |
| `temperature` | number | No | — | Randomness of response; higher = more diverse |
| `top_p` | number | No | — | Token diversity control |
| `web_search` | boolean | No | — | Enable current web info access |

**Why it matters:** Direct AI engine probing. Send the same prompt to ChatGPT, Claude, Gemini, and Perplexity and compare responses. This is what CheckThat does at scale, but DataForSEO's version gives you API-level access for ad-hoc queries and spot checks.

**AEO expert context:** This is functionally an AI brand research instrument. Remember the three laws: sensitivity (one-word change = 10-78% shift), sycophancy (leading prompts produce vanity data), and entropy (< 1% chance of identical results). Use neutral interrogatives. A single response is anecdotal, not data — you need 30-100 runs for statistical significance.

---

### ai_optimization_llm_models

Lists available models for a given LLM type.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `llm_type` | string | Yes | — | `claude`, `gemini`, `chat_gpt`, `perplexity` |

**Usage:** Call before `llm_response` to discover valid model names and versions.

---

### ai_optimization_chat_gpt_scraper

Scrapes actual ChatGPT search results for a keyword.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keyword` | string | Yes | — | Up to 2,000 characters; `%25` for `%`, `%2B` for `+` |
| `language_code` | string | Yes | — | e.g., `"en"` |
| `location_name` | string | No | `"United States"` | |
| `force_web_search` | boolean | No | — | Force the AI to use web search |

**Why it matters:** ChatGPT drives 87% of AI referral traffic. Scraping its actual search results shows exactly what URLs it surfaces for a given query. Unlike `llm_response` (which gets a generated answer), this gets the search-augmented results with citations — closer to what real users see.

**AEO expert context:** The `force_web_search` flag is important. Without it, ChatGPT may answer from training data alone. With it, you see which sites get cited in search-augmented mode — the mode that's growing fastest and most commercially relevant.

---

### ai_optimization_chat_gpt_scraper_locations

Utility for available locations for ChatGPT scraping.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `country_iso_code` | string | No | — | ISO 3166-1 alpha-2 (e.g., `US`, `GB`) |
| `location_name` | string | No | — | Location or partial name |

---

### ai_opt_llm_ment_search

Search for LLM mentions of domains or keywords with aggregated metrics.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | array | Yes | — | Up to 1,000 target objects (see target format below) |
| `location_name` | string | No | — | |
| `language_code` | string | No | — | |
| `platform` | string | No | — | `chat_gpt` or `google` |
| `filters` | array | No | — | Up to 8 filters |
| `order_by` | array | No | — | |
| `limit` | number | No | 10 | Max 1,000 |

**Target format — domain:**
```json
{
  "domain": "vercel.com",
  "search_filter": "include",
  "search_scope": ["answer"]
}
```

**Target format — keyword:**
```json
{
  "keyword": "deployment platform",
  "match_type": "word_match",
  "search_filter": "include",
  "search_scope": ["question", "answer"]
}
```

**Target properties:**

| Property | Type | Required | Values | Notes |
|----------|------|----------|--------|-------|
| `domain` | string | Yes (domain target) | — | Domain to search for |
| `keyword` | string | Yes (keyword target) | — | Keyword to search for |
| `match_type` | string | No | `word_match`, `partial_match` | Keywords only |
| `search_filter` | string | No | `include`, `exclude` | |
| `search_scope` | string[] | No | `any`, `question`, `answer` | Where to look |

**Why it matters:** Measures how often and where a domain or keyword appears across LLM-generated content. The `search_scope` parameter is particularly valuable: filtering by `answer` only shows mentions where the LLM actually recommends or references the domain — not just when users ask about it. The distinction between appearing in questions vs. answers maps directly to the RECALL vs. ALIGNMENT framework.

**AEO expert context:** This tool answers the most fundamental AEO question: "When people ask AI about topics relevant to my business, does AI mention me?" The `platform` filter matters — ChatGPT and Google AI produce different citation patterns. Never blend platforms. Report separately.

---

### ai_opt_llm_ment_agg_metrics

Aggregated metrics for LLM mentions of given keywords or domains.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | array | Yes | — | Up to 1,000 target objects (same format as search) |
| `location_name` | string | No | — | |
| `language_code` | string | No | — | |
| `platform` | string | No | — | `chat_gpt` or `google` |
| `filters` | array | No | — | Up to 8 filters |

**Why it matters:** The summary view. Where `llm_ment_search` returns individual mentions, this returns aggregate counts and metrics. Use it when you need the numbers (how many times? what's the trend?) rather than the individual data points.

---

### ai_opt_llm_ment_cross_agg_metrics

Aggregated metrics grouped by custom keys — designed for competitive comparison.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `targets` | array | Yes | — | 2–10 objects, each with `aggregation_key` and `target` array |
| `location_name` | string | No | — | |
| `language_code` | string | No | — | |
| `platform` | string | No | — | `chat_gpt` or `google` |
| `filters` | array | No | — | Up to 8 filters |
| `internal_list_limit` | number | No | — | |

**Target format:**
```json
{
  "targets": [
    {
      "aggregation_key": "vercel",
      "target": [{ "domain": "vercel.com" }]
    },
    {
      "aggregation_key": "netlify",
      "target": [{ "domain": "netlify.com" }]
    }
  ]
}
```

**Why it matters:** Head-to-head AI visibility comparison. Group multiple domains under custom labels and compare their LLM mention metrics side by side. This is the competitive benchmarking layer — the AEO equivalent of comparing organic traffic between competitors.

**AEO expert context:** This maps directly to CheckThat's competitive positioning analysis. Use it to validate CheckThat's competitive data with a second source, or to quickly benchmark a new prospect's AI visibility against their competitors.

---

### ai_opt_llm_ment_top_pages

LLM mentions metrics grouped by most-mentioned pages.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | array | Yes | — | Up to 1,000 target objects |
| `location_name` | string | No | — | |
| `language_code` | string | No | — | |
| `platform` | string | No | — | `chat_gpt` or `google` |
| `links_scope` | string | No | — | `sources` or `search_results` |
| `initial_dataset_filters` | array | No | — | Up to 8 filters |
| `items_list_limit` | number | No | — | 1–10 |
| `internal_list_limit` | number | No | — | 1–10 |

**Why it matters:** Identifies which specific pages LLMs cite most. Not which domains — which URLs. This tells you exactly which content earns AI citations. Study the structure, format, and depth of those pages to reverse-engineer what makes content citation-worthy.

**AEO expert context:** Pages scoring 8.5+/10 on semantic completeness are 4.2x more likely to be cited by AI. FAQ schema markup adds +89% to +221% citation lift. Cross-reference the top-cited pages against these quality factors to understand why they win.

---

### ai_opt_llm_ment_top_domains

LLM mentions metrics grouped by most-mentioned domains.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | array | Yes | — | Up to 1,000 target objects |
| `location_name` | string | No | — | |
| `language_code` | string | No | — | |
| `platform` | string | No | — | `chat_gpt` or `google` |
| `links_scope` | string | No | — | `sources` or `search_results` |
| `initial_dataset_filters` | array | No | — | Up to 8 filters |
| `items_list_limit` | number | No | — | 1–10 |
| `internal_list_limit` | number | No | — | 1–10 |

**Why it matters:** The authority layer. Shows which domains AI engines trust most for a given topic. Wikipedia, Reddit, and G2 consistently dominate (Wikipedia = 12.1% of ChatGPT citations, Reddit = top-10 most-cited domain). If a third-party domain dominates AI citations for your keywords, getting mentioned or linked from that domain becomes a high-priority tactic.

---

### ai_optimization_keyword_data_search_volume

Search volume estimated from AI/LLM usage patterns (not Google Ads).

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keywords` | string[] | Yes | — | Up to 1,000 keywords |
| `language_code` | string | Yes | — | |
| `location_name` | string | No | `"United States"` | |

**Why it matters:** AI-native search volume. Google Ads volume measures what people type into Google. This measures what people ask AI engines. As AI search usage grows (Perplexity at 370% growth, Claude at 10.3x growth), the gap between these two numbers widens. A keyword with 10,000 monthly Google searches and 50,000 AI queries represents a very different optimization opportunity.

---

### ai_optimization_llm_mentions_filters

Documentation utility listing all filterable fields for LLM mentions endpoints.

No parameters.

---

### ai_opt_kw_data_loc_and_lang

Utility for available locations and languages for AI keyword data.

No parameters.

---

### ai_opt_llm_ment_loc_and_lang

Utility for available locations and languages for LLM mentions endpoints.

No parameters.

---

## 3. Backlinks — Link Intelligence

**20 tools.** Link profile analysis covering individual backlinks, referring domains, anchor text, intersection analysis, time series, and bulk operations. DataForSEO's backlink index operates independently of SEMRush and Ahrefs, offering a third perspective on link data.

**Why backlinks still matter in the AI era:** Domain Authority's correlation with AI citations dropped to r=0.18 — nearly useless. But backlinks remain a strong Google ranking signal (and 99% of URLs in AI Overviews appear in the top 20 organic results). The shift is from quantity to quality: third-party validation (6.5x citation multiplier) and earned authority signals now matter more than raw link volume.

---

### backlinks_summary

Backlink profile overview for a domain, subdomain, or page.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain (no protocol), subdomain, or full page URL |
| `include_subdomains` | boolean | No | `true` | Include indirect links |
| `exclude_internal_backlinks` | boolean | No | `true` | Exclude internal subdomain links |

**Why it matters:** Quick backlink health check. Total backlinks, referring domains, follow/nofollow ratio, top-level domain distribution. The ratio of referring domains to total backlinks reveals link quality — a profile with 10,000 links from 100 domains is weaker than one with 5,000 links from 3,000 domains.

---

### backlinks_backlinks

Individual backlink list with detailed data and filtering.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain, subdomain, or page URL |
| `mode` | string | No | `"as_is"` | `as_is`, `one_per_domain`, `one_per_anchor` |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | Up to 8 filters |
| `order_by` | array | No | — | |

**Why it matters:** The raw link data. The `mode` parameter controls deduplication — `one_per_domain` gives you unique referring domains, `one_per_anchor` reveals anchor text diversity. Heavy concentration on one anchor is a spam signal.

---

### backlinks_referring_domains

Referring domains pointing to the target.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain, subdomain, or page URL |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |

**Why it matters:** Referring domain quality matters more than raw link count. Filter by rank to find high-authority referring domains. Filter by country to identify geographic link patterns.

---

### backlinks_anchors

Anchor text distribution for links pointing to the target.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain, subdomain, or page URL |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |

**Why it matters:** Anchor text profile is a core link quality signal. Healthy profiles have diverse anchors: branded terms, naked URLs, generic ("click here"), and topical. Profiles dominated by exact-match keyword anchors suggest manipulation.

---

### backlinks_competitors

Domains sharing parts of the backlink profile with the target.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain, subdomain, or page URL |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `main_domain` | boolean | No | `true` | Only main domain |
| `exclude_large_domains` | boolean | No | `true` | Exclude mega-domains |
| `exclude_internal_backlinks` | boolean | No | `true` | |

**Why it matters:** Link-based competitor discovery. Finds domains that share linking sources with you — meaning the same sites link to both of you. These are your link competitors. The overlap reveals which linking opportunities you're competing for.

---

### backlinks_domain_intersection

Domains linking to a set of domains or pages — link gap analysis.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `targets` | string[] | Yes | — | Up to 20 domains/subdomains/pages |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |

**Why it matters:** The link gap report. Shows which domains link to your competitors but not to you. These are proven linkers in your space who already link to similar content — they're the highest-probability outreach targets.

---

### backlinks_page_intersection

Domains linking to a set of specific pages.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `targets` | string[] | Yes | — | Up to 20 domains/subdomains/pages |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |

**Why it matters:** Page-level link gap. More granular than domain intersection. Shows who links to specific competitor pages — useful when you've created content on the same topic and want to find linkers who'd value your version.

---

### backlinks_domain_pages

Domain pages with their backlink data.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain, subdomain, or page URL |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |

**Why it matters:** Identifies the pages on a domain that attract the most links. These are the "link magnets" — usually original research, tools, or comprehensive guides. Understanding what earns links on a domain informs content strategy.

---

### backlinks_domain_pages_summary

Summary backlink metrics per page of a domain.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain, subdomain, or page URL |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |

---

### backlinks_referring_networks

Referring networks (by IP address or subnet) pointing to the target.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain, subdomain, or page URL |
| `network_address_type` | string | No | `"ip"` | `ip` or `subnet` |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |

**Why it matters:** Spam detection. If a large percentage of backlinks come from the same IP subnet, it suggests a Private Blog Network (PBN). Natural link profiles have diverse IP distributions.

---

### backlinks_timeseries_summary

Backlink metrics over time for a domain.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain (no protocol) |
| `date_from` | string | No | — | `yyyy-mm-dd` (min: 2019-01-30) |
| `date_to` | string | No | today | `yyyy-mm-dd` |
| `group_range` | string | No | `"month"` | `day`, `week`, `month`, `year` |

**Why it matters:** Link velocity. The rate of new link acquisition signals content momentum. A sudden spike might indicate a viral piece or a link-building campaign. A sudden drop might indicate disavow activity or content removal.

---

### backlinks_timeseries_new_lost_summary

Time series of new and lost backlinks and referring domains.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain |
| `date_from` | string | No | — | |
| `date_to` | string | No | today | |
| `group_range` | string | No | — | `day`, `week`, `month`, `year` |

**Why it matters:** Net link growth. New links minus lost links = net momentum. If a domain is losing links faster than gaining them, the backlink profile is eroding — and rankings will follow.

---

### Backlinks Bulk Operations (7 tools)

Bulk operations process up to 1,000 targets in a single call. Ideal for competitive analysis where you need the same metric across many domains.

#### backlinks_bulk_backlinks

Live backlink count for up to 1,000 targets.

| Parameter | Type | Required | Default |
|-----------|------|----------|---------|
| `targets` | string[] | Yes | — |

#### backlinks_bulk_referring_domains

Referring domain count for up to 1,000 targets.

| Parameter | Type | Required | Default |
|-----------|------|----------|---------|
| `targets` | string[] | Yes | — |

#### backlinks_bulk_pages_summary

Bulk backlink summary for up to 1,000 targets.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `targets` | string[] | Yes | — | Max 100 domains (1,000 for subdomains/pages) |
| `include_subdomains` | boolean | No | `true` | |

#### backlinks_bulk_ranks

Rank score (0–1,000) for up to 1,000 targets.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `targets` | string[] | Yes | — | |
| `rank_scale` | string | No | `"one_thousand"` | `one_hundred` or `one_thousand` |

#### backlinks_bulk_spam_score

Spam score (0–100) for up to 1,000 targets.

| Parameter | Type | Required | Default |
|-----------|------|----------|---------|
| `targets` | string[] | Yes | — |

**Why it matters:** The only bulk spam scoring endpoint. Quickly flag suspicious domains in a competitor's backlink profile or identify spammy referring domains pointing to your client.

#### backlinks_bulk_new_lost_backlinks

New and lost backlink counts for up to 1,000 targets.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `targets` | string[] | Yes | — | |
| `date_from` | string | No | 1 month ago | Min: 1 year ago |

#### backlinks_bulk_new_lost_referring_domains

New and lost referring domain counts for up to 1,000 targets.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `targets` | string[] | Yes | — | |
| `date_from` | string | No | — | Min: 1 year ago |

---

### backlinks_available_filters

Documentation utility listing filterable fields for Backlinks endpoints.

| Parameter | Type | Required | Default |
|-----------|------|----------|---------|
| `tool` | string | No | — |

---

## 4. SERP — Live Search Results

**7 tools.** Captures actual Google and YouTube search results in real time. Unlike Labs (which uses historical crawl data), SERP tools fetch live results at the moment of the call.

**Why live SERP data matters:** Historical keyword data tells you what ranked yesterday. Live SERP data tells you what ranks right now. For time-sensitive audits — post-algorithm-update analysis, competitor monitoring, SERP feature tracking — live data is irreplaceable. The People Also Ask expansion is particularly valuable for content ideation and understanding how Google maps related questions.

---

### serp_organic_live_advanced

Live Google, Yahoo, or Bing organic search results for a keyword.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keyword` | string | Yes | — | Search keyword |
| `language_code` | string | Yes | — | e.g., `"en"` |
| `search_engine` | string | No | `"google"` | `google`, `yahoo`, `bing` |
| `location_name` | string | No | `"United States"` | Hierarchical: `"City,Region,Country"` |
| `depth` | number | No | 10 | 10–700 results |
| `max_crawl_pages` | number | No | 1 | 1–7 crawl pages |
| `device` | string | No | `"desktop"` | `desktop`, `mobile` |
| `people_also_ask_click_depth` | number | No | — | 1–4 PAA expansion depth |

**Why it matters:** The ground truth of search. Everything else is an estimate — this is what actually appears when someone searches. The `people_also_ask_click_depth` parameter is a content goldmine: expanding PAA boxes 3-4 levels deep reveals dozens of related questions that represent real search behavior. Each PAA question is a potential content section or standalone piece.

**AEO expert context:** Run searches on `mobile` device to see how AI Overviews render. 53.68% of traffic is mobile, and AI crawls the mobile version of content. Mobile SERP features differ from desktop, especially for AI-generated content.

---

### serp_youtube_organic_live_advanced

Live YouTube search results for a keyword.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keyword` | string | Yes | — | |
| `location_name` | string | Yes | — | Hierarchical location |
| `language_code` | string | Yes | — | |
| `device` | string | No | `"desktop"` | `desktop`, `mobile` |
| `os` | string | No | `"windows"` | `windows`, `macos`, `android`, `ios` |
| `block_depth` | number | No | 20 | 1–700 result blocks |

**Why it matters:** YouTube is the second-largest search engine and a major AI training data source. Understanding which videos rank for target keywords reveals content format preferences (tutorial, review, comparison) and competitive landscape on a platform most SEO audits ignore.

---

### serp_youtube_video_info_live_advanced

Metadata for a specific YouTube video.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `video_id` | string | Yes | — | YouTube video ID |
| `location_name` | string | Yes | — | |
| `language_code` | string | Yes | — | |
| `device` | string | No | `"desktop"` | |
| `os` | string | No | — | |

---

### serp_youtube_video_comments_live_advanced

Comments on a YouTube video.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `video_id` | string | Yes | — | |
| `location_name` | string | Yes | — | |
| `language_code` | string | Yes | — | |
| `device` | string | No | `"desktop"` | |
| `os` | string | No | — | |
| `depth` | number | No | 20 | Max 700 |

**Why it matters:** Comments reveal real audience questions, objections, and language patterns. This is buyer language — the same language that should inform both SEO content and AEO prompt libraries. Comments on competitor videos are particularly valuable for content gap analysis.

---

### serp_youtube_video_subtitles_live_advanced

Subtitles/captions for a YouTube video, with optional translation.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `video_id` | string | Yes | — | |
| `location_name` | string | Yes | — | |
| `language_code` | string | Yes | — | |
| `subtitles_language` | string | No | — | Original subtitle language |
| `subtitles_translate_language` | string | No | — | Translation target language |
| `device` | string | No | `"desktop"` | |
| `os` | string | No | — | |

**Why it matters:** Video content analysis at scale. Extract the full text of competitor videos without watching them. Analyze the topics, terminology, and structure they use. Subtitles are also training data for LLMs — understanding what's in popular video content reveals what AI models have absorbed.

---

### serp_locations / serp_youtube_locations

Location utilities for Google and YouTube SERP tools.

| Parameter | Type | Required | Default |
|-----------|------|----------|---------|
| `country_iso_code` | string | Yes | — |
| `search_engine` | string | No | `"google"` (SERP only) |
| `location_type` | string | No | — |
| `location_name` | string | No | — |

---

## 5. Content Analysis — Web Citation Intelligence

**3 tools.** Tracks how brands and keywords appear across web content, with sentiment analysis. This is web-level citation data — complementary to the AI-level citation data from the AI Optimization category.

**Why citation tracking matters:** Third-party mentions produce 6.5x more AI citations than owned content. 85% of brand mentions come from third-party pages. Understanding where and how a brand is discussed across the web — with what sentiment, in what context — reveals both the authority signals AI engines absorb and the content gaps a brand needs to fill.

---

### content_analysis_search

Citation data for a target keyword. Find where a brand or topic is mentioned across the web.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keyword` | string | Yes | — | Use `\"double quotes\"` for exact phrase |
| `keyword_fields` | object | No | — | Filter by `title`, `main_title`, `previous_title`, `snippet` |
| `page_type` | string[] | No | — | `ecommerce`, `news`, `blogs`, `message-boards`, `organization` |
| `search_mode` | string | No | — | `as_is` or `one_per_domain` |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | Up to 8 filters |
| `order_by` | array | No | — | |

**Why it matters:** Brand mention mapping. Find every page across the web that mentions a brand or keyword. The `page_type` filter is valuable — filtering by `news` reveals press coverage, `blogs` reveals editorial mentions, `message-boards` reveals community discussion. Each type carries different authority weight with both search engines and AI models.

**AEO expert context:** Reddit presence is in the top-10 most-cited domains across AI engines. G2 accounts for 8.25% of ChatGPT citations. Use `page_type: ["message-boards"]` to specifically assess community presence, and cross-reference with brand search volume (0.334 correlation with AI citations — the strongest single predictor).

---

### content_analysis_summary

Citation overview with sentiment analysis for a target keyword.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keyword` | string | Yes | — | |
| `keyword_fields` | object | No | — | Filter by fields |
| `page_type` | string[] | No | — | |
| `initial_dataset_filters` | array | No | — | |
| `positive_connotation_threshold` | number | No | 0.4 | 0–1; probability threshold for positive sentiment |
| `sentiments_connotation_threshold` | number | No | 0.4 | 0–1; probability threshold for sentiment classification |
| `internal_list_limit` | number | No | 1 | 1–20 |

**Why it matters:** Sentiment aggregation. Not just where a brand is mentioned, but whether the sentiment is positive, negative, or neutral. Negative sentiment in third-party content is an AI citation risk — AI engines absorb sentiment patterns, and negative narratives compound across responses.

**AEO expert context:** This maps to CheckThat's SENTIMENT measurement layer. If web content about a brand is predominantly negative, that negative sentiment will appear in AI responses. This tool helps identify sentiment problems before they manifest in AI answers.

---

### content_analysis_phrase_trends

Citation trends for a keyword over a date range.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keyword` | string | Yes | — | |
| `date_from` | string | Yes | — | `yyyy-mm-dd` |
| `keyword_fields` | object | No | — | |
| `page_type` | string[] | No | — | |
| `initial_dataset_filters` | array | No | — | |
| `date_to` | string | No | — | |
| `date_group` | string | No | `"month"` | `day`, `week`, `month` |
| `internal_list_limit` | number | No | 1 | 1–20 |

**Why it matters:** Citation velocity. Is a brand being mentioned more or less over time? Rising citation trends correlate with growing AI visibility — the LIFT metric from CheckThat's framework. Declining trends signal eroding authority.

---

## 6. Keyword Data — Volume, Trends & Demographics

**7 tools.** Search volume from Google Ads, trend data from Google Trends and DataForSEO's proprietary index, plus demographic and regional breakdowns.

---

### kw_data_google_ads_search_volume

Search volume directly from Google Ads.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keywords` | string[] | Yes | — | |
| `location_name` | string | No | `"United States"` | Hierarchical: `"City,Region,Country"` |
| `language_code` | string | No | — | |

**Why it matters:** Official Google volume data. All other search volume estimates (SEMRush, DataForSEO Labs, Ahrefs) are approximations. Google Ads data is the closest to ground truth, though Google rounds and groups similar terms.

---

### kw_data_google_trends_explore

Google Trends data across web, news, images, shopping, and YouTube.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keywords` | string[] | Yes | — | Up to 5 keywords |
| `type` | string | No | `"web"` | `web`, `news`, `youtube`, `images`, `froogle` (shopping) |
| `location_name` | string | No | — | |
| `language_code` | string | No | — | |
| `date_from` | string | No | — | `yyyy-mm-dd` |
| `date_to` | string | No | — | |
| `time_range` | string | No | — | `past_hour`, `past_4_hours`, `past_day`, `past_7_days`, `past_30_days`, `past_90_days`, `past_12_months`, `past_5_years` |
| `item_types` | string[] | No | — | `google_trends_graph`, `google_trends_map`, `google_trends_topics_list`, `google_trends_queries_list` |
| `category_code` | number | No | — | Use `kw_data_google_trends_categories` to discover |

**Why it matters:** Trend comparison. Google Trends shows relative interest over time — invaluable for comparing competing topics, detecting seasonal patterns, and validating whether a topic is growing or declining. The `youtube` type reveals video content demand separately from web search.

---

### kw_data_google_trends_categories

Returns all Google Trends category codes.

No parameters.

---

### kw_data_dfs_trends_explore

DataForSEO's own trend data for keyword popularity.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keywords` | string[] | Yes | — | Up to 5 keywords |
| `type` | string | No | `"web"` | `web`, `news`, `ecommerce` |
| `location_name` | string | No | — | |
| `date_from` | string | No | — | |
| `date_to` | string | No | — | |
| `time_range` | string | No | — | `past_4_hours` through `past_5_years` |

**Why it matters:** Independent trend data source. DataForSEO's own clickstream and SERP data produces trend signals that may differ from Google Trends (which is sample-based). Cross-referencing both catches artificial spikes and validates real trends.

---

### kw_data_dfs_trends_subregion_interests

Keyword popularity broken down by subregion.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keywords` | string[] | Yes | — | Up to 5 keywords |
| `type` | string | No | — | `web`, `news`, `ecommerce` |
| `location_name` | string | No | — | |
| `date_from` | string | No | — | |
| `date_to` | string | No | — | |
| `time_range` | string | No | — | |

**Why it matters:** Geographic demand signals. A keyword with high national volume but concentrated in one region has different content implications than one with even distribution. Also valuable for local SEO targeting.

---

### kw_data_dfs_trends_demography

Keyword popularity broken down by age group and gender.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `keywords` | string[] | Yes | — | Up to 5 keywords |
| `type` | string | No | — | `web`, `news`, `ecommerce` |
| `location_name` | string | No | — | |
| `date_from` | string | No | — | |
| `date_to` | string | No | — | |
| `time_range` | string | No | — | |

**Why it matters:** Audience validation. If your target persona is "VP of Engineering, 35-50" and the keyword's demographic skews 18-24, there's a mismatch between your content strategy and reality.

---

### kw_data_google_ads_locations

Locations available for Google Ads keyword data.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `country_iso_code` | string | Yes | — | ISO 3166-1 alpha-2 |
| `location_type` | string | No | — | TV Region, City, Country, State, etc. |
| `location_name` | string | No | — | |

---

## 7. On Page — Page-Level Technical Analysis

**3 tools.** Lighthouse audits, page-level SEO extraction, and content parsing. These tools analyze individual pages rather than domains.

**Why page-level matters:** AI engines extract content at the page level, not the domain level. A domain with strong overall authority but poorly structured individual pages will underperform in both SERP rankings and AI citations. Pages scoring 8.5+/10 on semantic completeness are 4.2x more likely to appear in AI Overviews.

---

### on_page_lighthouse

Google Lighthouse audit for performance, accessibility, SEO, and best practices.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `url` | string | Yes | — | Full page URL |
| `enable_javascript` | boolean | No | — | Enable JS rendering |
| `custom_user_agent` | string | No | — | |
| `accept_language` | string | No | — | |
| `full_data` | boolean | No | — | Full response vs. reduced |

**Why it matters:** The industry-standard page quality audit. Performance (Core Web Vitals), Accessibility (WCAG), SEO (meta tags, crawlability), and Best Practices (HTTPS, image optimization). Mobile optimization is critical — 53.68% of traffic is mobile and AI engines crawl the mobile version.

**GrowthX usage:** Used in past Flodesk audits for page-level scoring. The `content-pages-audit` skill currently uses the PageSpeed and a11y MCPs instead, but Lighthouse provides a more comprehensive single-call alternative.

---

### on_page_instant_pages

Page-level SEO and optimization data extraction.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `url` | string | Yes | — | Full URL |
| `enable_javascript` | boolean | No | — | |
| `custom_js` | string | No | — | Custom JavaScript to execute |
| `custom_user_agent` | string | No | — | |
| `accept_language` | string | No | — | |

**Why it matters:** Extracts the SEO-relevant elements of a page: title, meta description, headings, canonical URL, hreflang, open graph tags, structured data, and on-page optimization metrics. This is the technical SEO checklist in API form.

---

### on_page_content_parsing

Extracts page content: links, anchors, headings, and text.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `url` | string | Yes | — | Full URL |
| `enable_javascript` | boolean | No | — | |
| `custom_user_agent` | string | No | — | |
| `accept_language` | string | No | — | |

**Why it matters:** Structured content extraction. Gets the actual text, heading hierarchy, internal/external links, and anchor text from a page. Useful for content quality analysis (heading structure, link density, text-to-HTML ratio) and for feeding content into further analysis.

**AEO expert context:** AI engines extract content in chunks. Clear H2/H3 hierarchy makes content 40% more likely to be cited. This tool lets you verify whether a page's heading structure supports AI extraction.

---

## 8. Domain Analytics — Technology & WHOIS

**4 tools.** Technology stack detection and domain registration data.

---

### domain_analytics_technologies_domain_technologies

Technology stack detected on a domain.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `target` | string | Yes | — | Domain (no protocol) |

**Why it matters:** Reveals the technology stack: CMS (WordPress, Next.js), analytics (GA4, Amplitude), marketing tools (HubSpot, Marketo), CDN, hosting, and more. For competitive analysis, knowing a competitor uses WordPress vs. a headless CMS reveals their technical constraints and capabilities.

---

### domain_analytics_whois_overview

WHOIS data combined with backlink and ranking metrics.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `is_claimed` | boolean | No | `true` | |

**Why it matters:** Domain age, registrar, registration date, and expiration. Domain age is a weak but real ranking signal. More practically, WHOIS data confirms domain ownership and helps verify competitor corporate structures.

---

### domain_analytics_technologies_available_filters / domain_analytics_whois_available_filters

Filter documentation utilities for their respective endpoints.

| Parameter | Type | Required | Default |
|-----------|------|----------|---------|
| `tool` | string | No | — |

---

## 9. Business Data — Local Listings

**1 tool.** Google Maps business listing data.

---

### business_data_business_listings_search

Business listings from Google Maps with filtering.

| Parameter | Type | Required | Default | Notes |
|-----------|------|----------|---------|-------|
| `description` | string | No | — | Business description (up to 200 chars) |
| `title` | string | No | — | Business name (up to 200 chars) |
| `categories` | string[] | No | — | Up to 10 categories |
| `location_coordinate` | string | No | — | `latitude,longitude,radius_km` (1–100,000) |
| `limit` | number | No | 10 | Max 1,000 |
| `offset` | number | No | 0 | |
| `filters` | array | No | — | |
| `order_by` | array | No | — | |
| `is_claimed` | boolean | No | `true` | Google Maps verified |

**Why it matters:** Local SEO data. For B2B clients with physical locations or local market presence, Google Maps listings are a significant discovery channel. Claimed and verified listings also function as an authority signal that AI engines factor into brand recognition.

---

## GrowthX Usage Patterns

### Current State

Only **1 of 79 tools** is in active use:

| Tool | Skills Using It |
|------|----------------|
| `dataforseo_labs_google_domain_rank_overview` | `seo-domain-audit`, `competitive-seo-landscape`, `competitive-comparison-table` |

### High-Priority Expansion Opportunities

Ranked by impact on GrowthX's audit methodology:

**Tier 1 — Immediate value, directly extends current skills:**

| Tool | Why | Skill It Would Enhance |
|------|-----|------------------------|
| `ai_opt_llm_ment_search` | Cross-validate CheckThat data with DataForSEO's LLM mention index | `aeo-audit` |
| `ai_opt_llm_ment_cross_agg_metrics` | Competitive AI visibility comparison | `competitive-comparison-table` |
| `ai_opt_llm_ment_top_pages` | Identify which competitor pages earn AI citations | `aeo-audit`, `content-pages-audit` |
| `ranked_keywords` with `item_types: ["ai_overview_reference"]` | Find which keywords trigger AI Overviews citing a domain | `seo-domain-audit` |
| `bulk_traffic_estimation` | Replace N individual calls with 1 bulk call for competitive landscape | `competitive-seo-landscape` |

**Tier 2 — Valuable additions to methodology:**

| Tool | Why | New Capability |
|------|-----|----------------|
| `content_analysis_summary` | Sentiment-aware brand mention tracking across the web | Brand perception layer for audits |
| `domain_intersection` | Keyword gap analysis using a second data source | Cross-validated competitive gaps |
| `backlinks_summary` + `bulk_spam_score` | Link health assessment for domain audits | Backlink quality section |
| `on_page_lighthouse` | Single-call Lighthouse for page-level scoring | Replaces or supplements PageSpeed + a11y MCPs |
| `serp_organic_live_advanced` | Live SERP with PAA expansion for content opportunities | Content ideation section |

**Tier 3 — Specialized use cases:**

| Tool | Why |
|------|-----|
| `ai_optimization_llm_response` | Ad-hoc LLM probing for specific audit questions |
| `search_intent` | Bulk intent classification for keyword portfolios |
| `historical_rank_overview` | Cross-validated domain trajectory |
| `backlinks_timeseries_summary` | Link velocity analysis |
| `content_analysis_phrase_trends` | Citation trend monitoring |

---

## DataForSEO vs. SEMRush — When to Use Which

Both MCPs are available. They have different strengths.

### Where DataForSEO is stronger

| Capability | DataForSEO | SEMRush |
|------------|-----------|---------|
| **AI Optimization / LLM mentions** | 14 dedicated tools | Not available |
| **Bulk operations** | Up to 1,000 targets per call (backlinks, traffic, keywords) | Limited bulk support |
| **Spam scoring** | Dedicated `bulk_spam_score` endpoint | No equivalent |
| **Content sentiment** | Sentiment analysis built into Content Analysis | Not available |
| **Live SERP + PAA** | PAA expansion to depth 4 | Not available via MCP |
| **AI Overview tracking** | `item_types: ["ai_overview_reference"]` in ranked_keywords | Not available |
| **YouTube data** | Video info, comments, subtitles extraction | Not available |
| **Direct call pattern** | Simple tool_name + JSON params | 3-step discovery/schema/execute |

### Where SEMRush is stronger

| Capability | SEMRush | DataForSEO |
|------------|---------|------------|
| **Report depth** | 84 reports across 11 categories | 79 tools across 9 categories |
| **Historical depth** | Monthly snapshots going back years | Limited historical endpoints |
| **Position tracking** | Dedicated tracking with share of voice | No position tracking |
| **Keyword gap** | Multi-domain comparison in one call (`domain_domains`) | Pairwise only (`domain_intersection`) |
| **Organic research** | Page-level URL reports, position changes (new/lost/rise/fall) | Less granular organic data |
| **Authority score** | 0–100 Domain Authority Score | Rank score on different scale |
| **Advertising data** | PLA, display ads, shopping research | No advertising data |
| **Traffic analytics** | Full traffic analytics suite (separate subscription) | Bulk traffic estimation only |

### The Complementary Approach

For GrowthX audits, the strongest approach is using both:

1. **SEMRush for the SEO foundation:** Domain snapshots, organic keywords, page classification, historical trends, keyword gap analysis, backlink authority score
2. **DataForSEO for the AEO layer:** LLM mentions, AI Overview references, content sentiment, cross-validated traffic estimates
3. **Both for validation:** When SEMRush and DataForSEO agree on a trend or metric, confidence is high. When they disagree, investigate deeper.

The AI Optimization category is the single biggest reason to expand DataForSEO usage — it provides data that exists nowhere else in the GrowthX toolchain except CheckThat, and adds a complementary perspective.

---

## Quick Reference — All 79 Tools

| # | Category | Tool Name | One-Line Description |
|---|----------|-----------|---------------------|
| 1 | Labs | `dataforseo_labs_google_domain_rank_overview` | Domain ranking + traffic + position distribution |
| 2 | Labs | `dataforseo_labs_google_ranked_keywords` | Keywords a domain/page ranks for |
| 3 | Labs | `dataforseo_labs_google_keyword_overview` | Keyword volume, CPC, intent, monthly trends |
| 4 | Labs | `dataforseo_labs_google_historical_keyword_data` | Historical keyword data since Aug 2021 |
| 5 | Labs | `dataforseo_labs_google_historical_rank_overview` | Domain ranking/traffic over time |
| 6 | Labs | `dataforseo_labs_google_historical_serp` | Historical SERP results for a keyword |
| 7 | Labs | `dataforseo_labs_google_competitors_domain` | Competitor domains by keyword overlap |
| 8 | Labs | `dataforseo_labs_google_domain_intersection` | Keyword gap between two domains |
| 9 | Labs | `dataforseo_labs_google_page_intersection` | Keyword overlap at page level (up to 20 pages) |
| 10 | Labs | `dataforseo_labs_google_relevant_pages` | Page-level rankings and traffic |
| 11 | Labs | `dataforseo_labs_google_subdomains` | Subdomain ranking/traffic breakdown |
| 12 | Labs | `dataforseo_labs_google_serp_competitors` | Domains ranking for given keywords |
| 13 | Labs | `dataforseo_labs_google_keyword_suggestions` | Keyword suggestions containing seed |
| 14 | Labs | `dataforseo_labs_google_related_keywords` | Semantically related keywords |
| 15 | Labs | `dataforseo_labs_google_keyword_ideas` | Keyword ideas from categories |
| 16 | Labs | `dataforseo_labs_google_keywords_for_site` | Keywords relevant to a domain |
| 17 | Labs | `dataforseo_labs_google_top_searches` | Top searches from 7B+ keyword database |
| 18 | Labs | `dataforseo_labs_bulk_traffic_estimation` | Bulk traffic estimates (up to 1,000 targets) |
| 19 | Labs | `dataforseo_labs_bulk_keyword_difficulty` | Bulk keyword difficulty (up to 1,000) |
| 20 | Labs | `dataforseo_labs_search_intent` | Intent classification (up to 1,000 keywords) |
| 21 | Labs | `dataforseo_labs_available_filters` | Filter documentation |
| 22 | AI Opt | `ai_optimization_llm_response` | Query ChatGPT / Claude / Gemini / Perplexity |
| 23 | AI Opt | `ai_optimization_llm_models` | List available LLM models |
| 24 | AI Opt | `ai_optimization_chat_gpt_scraper` | Scrape ChatGPT search results |
| 25 | AI Opt | `ai_optimization_chat_gpt_scraper_locations` | ChatGPT scraper locations |
| 26 | AI Opt | `ai_opt_llm_ment_search` | Search LLM mentions of domains/keywords |
| 27 | AI Opt | `ai_opt_llm_ment_agg_metrics` | Aggregated LLM mention metrics |
| 28 | AI Opt | `ai_opt_llm_ment_cross_agg_metrics` | Cross-comparison LLM mention metrics |
| 29 | AI Opt | `ai_opt_llm_ment_top_pages` | Most-mentioned pages by LLMs |
| 30 | AI Opt | `ai_opt_llm_ment_top_domains` | Most-mentioned domains by LLMs |
| 31 | AI Opt | `ai_optimization_keyword_data_search_volume` | AI-estimated search volume |
| 32 | AI Opt | `ai_optimization_llm_mentions_filters` | LLM mentions filter documentation |
| 33 | AI Opt | `ai_opt_kw_data_loc_and_lang` | AI keyword data locations/languages |
| 34 | AI Opt | `ai_opt_llm_ment_loc_and_lang` | LLM mentions locations/languages |
| 35 | BL | `backlinks_summary` | Backlink profile overview |
| 36 | BL | `backlinks_backlinks` | Individual backlink list |
| 37 | BL | `backlinks_referring_domains` | Referring domains |
| 38 | BL | `backlinks_anchors` | Anchor text distribution |
| 39 | BL | `backlinks_competitors` | Backlink-based competitors |
| 40 | BL | `backlinks_domain_intersection` | Link gap analysis (domains) |
| 41 | BL | `backlinks_page_intersection` | Link gap analysis (pages) |
| 42 | BL | `backlinks_domain_pages` | Pages with backlink data |
| 43 | BL | `backlinks_domain_pages_summary` | Per-page backlink summary |
| 44 | BL | `backlinks_referring_networks` | Referring IPs/subnets |
| 45 | BL | `backlinks_timeseries_summary` | Backlink metrics over time |
| 46 | BL | `backlinks_timeseries_new_lost_summary` | New/lost backlinks over time |
| 47 | BL | `backlinks_bulk_backlinks` | Bulk backlink count (1,000 targets) |
| 48 | BL | `backlinks_bulk_referring_domains` | Bulk referring domain count |
| 49 | BL | `backlinks_bulk_pages_summary` | Bulk page backlink summary |
| 50 | BL | `backlinks_bulk_ranks` | Bulk rank score (0–1,000) |
| 51 | BL | `backlinks_bulk_spam_score` | Bulk spam score (0–100) |
| 52 | BL | `backlinks_bulk_new_lost_backlinks` | Bulk new/lost backlinks |
| 53 | BL | `backlinks_bulk_new_lost_referring_domains` | Bulk new/lost referring domains |
| 54 | BL | `backlinks_available_filters` | Backlink filter documentation |
| 55 | SERP | `serp_organic_live_advanced` | Live Google/Yahoo/Bing SERP results |
| 56 | SERP | `serp_youtube_organic_live_advanced` | Live YouTube search results |
| 57 | SERP | `serp_youtube_video_info_live_advanced` | YouTube video metadata |
| 58 | SERP | `serp_youtube_video_comments_live_advanced` | YouTube video comments |
| 59 | SERP | `serp_youtube_video_subtitles_live_advanced` | YouTube video subtitles |
| 60 | SERP | `serp_locations` | Google SERP locations |
| 61 | SERP | `serp_youtube_locations` | YouTube SERP locations |
| 62 | Content | `content_analysis_search` | Web citations for a keyword |
| 63 | Content | `content_analysis_summary` | Citation overview with sentiment |
| 64 | Content | `content_analysis_phrase_trends` | Citation trends over time |
| 65 | KW Data | `kw_data_google_ads_search_volume` | Google Ads search volume |
| 66 | KW Data | `kw_data_google_trends_explore` | Google Trends data |
| 67 | KW Data | `kw_data_google_trends_categories` | Google Trends categories |
| 68 | KW Data | `kw_data_dfs_trends_explore` | DataForSEO trend data |
| 69 | KW Data | `kw_data_dfs_trends_subregion_interests` | Regional keyword popularity |
| 70 | KW Data | `kw_data_dfs_trends_demography` | Keyword demographics |
| 71 | KW Data | `kw_data_google_ads_locations` | Google Ads locations |
| 72 | On Page | `on_page_lighthouse` | Lighthouse page quality audit |
| 73 | On Page | `on_page_instant_pages` | Page-level SEO data |
| 74 | On Page | `on_page_content_parsing` | Content extraction (links, headings, text) |
| 75 | Domain | `domain_analytics_technologies_domain_technologies` | Technology stack detection |
| 76 | Domain | `domain_analytics_whois_overview` | WHOIS + ranking data |
| 77 | Domain | `domain_analytics_technologies_available_filters` | Tech filter documentation |
| 78 | Domain | `domain_analytics_whois_available_filters` | WHOIS filter documentation |
| 79 | Business | `business_data_business_listings_search` | Google Maps business listings |
