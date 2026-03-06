# SEMRush MCP — Complete Reference Guide

<metadata>
purpose: Definitive reference for every report available through the SEMRush MCP server, with parameters, column codes, filter syntax, and GrowthX usage patterns
access: build-team
last_updated: 2026-03-05
</metadata>

---

## How the MCP Works

The SEMRush MCP uses a **3-step pattern** for every data request:

```
Step 1: Discovery    →  Call a *_research tool (e.g. organic_research) to list available reports
Step 2: Schema       →  Call get_report_schema(report="report_name") to get parameters
Step 3: Execute      →  Call execute_report(report="report_name", params={...}) to pull data
```

There are **11 discovery tools** exposing **84 reports** across the categories below. One additional category (Traffic Analytics / `trends_research`) requires a separate subscription and is not available on the current plan.

---

## Column Code Glossary

SEMRush returns data using short column codes. This table covers every code referenced across the API.

### Domain and Ranking

| Code | Meaning |
|------|---------|
| Db | Database (regional market code) |
| Dn | Domain name |
| Dt | Date of snapshot (YYYYMMDD) |
| Rk | SEMRush rank (by organic traffic volume) |

### Organic Search

| Code | Meaning |
|------|---------|
| Or | Organic keywords — count of keywords in Google top 100 |
| Ot | Organic traffic — estimated monthly visits from organic search |
| Oc | Organic cost — estimated value of organic traffic in Google Ads terms (USD) |

### Paid Search

| Code | Meaning |
|------|---------|
| Ad | Adwords keywords — count of keywords in paid search |
| At | Adwords traffic — estimated monthly visits from paid search |
| Ac | Adwords cost — estimated monthly ad spend (USD) |

### Keyword and Position

| Code | Meaning |
|------|---------|
| Ph | Keyword phrase |
| Po | Position (1–100) in Google organic results; 0 = not ranked |
| Pp | Previous position |
| Pd | Position difference (current minus previous) |
| Nq | Search volume — average monthly searches over last 12 months |
| Cp | CPC — average cost per click for that keyword (USD) |
| Co | Competition — advertiser density (0.00–1.00; 1 = highest) |
| Kd | Keyword difficulty — ranking difficulty index (0–100) |
| Nr | Number of results — total organic results for the keyword in Google |
| In | Search intent — 0 Commercial, 1 Informational, 2 Navigational, 3 Transactional |

### Traffic Estimates

| Code | Meaning |
|------|---------|
| Tr | Traffic share (%) — % of total domain organic traffic from a keyword |
| Tc | Traffic cost share (%) — % of total domain traffic cost from a keyword |
| Tg | Traffic — estimated absolute organic visits from a keyword |
| Td | Trends — 12-month search volume trend (comma-separated monthly values) |
| Ts | Traffic share (absolute, for URL reports) |

### URL and Page

| Code | Meaning |
|------|---------|
| Ur | URL of the ranking page |
| Pc | Keyword count — number of keywords the page ranks for |
| Sr | SERP features count |
| St | Estimated total traffic for the page |
| Fp | SERP feature positions |
| Fk | Featured keyword position |
| Vu | Visible URL in paid search |

### Competitor Reports

| Code | Meaning |
|------|---------|
| Cr | Competitor relevance score (0–1; higher = more overlap) |
| Np | Number of common keywords with target domain |

### Rank Difference (Winners/Losers)

| Code | Meaning |
|------|---------|
| Om | Organic traffic previous month |
| Tm | Traffic rank previous month |
| Um | Organic keywords previous month |
| Am | Adwords keywords previous month |
| Bm | Adwords traffic previous month |
| Cm | Adwords cost previous month |

### Backlink Reports

| Code | Meaning |
|------|---------|
| total | Total backlinks |
| domains_num | Total referring domains |
| urls_num | Total referring URLs |
| ips_num | Total referring IPs |
| ipclassc_num | Total referring Class C IPs |
| follows_num | Follow links count |
| nofollows_num | Nofollow links count |
| score | Authority Score (0–100) |
| trust_score | Trust Score |
| texts_num | Text link count |
| forms_num | Form link count |
| frames_num | Frame link count |
| images_num | Image link count |
| page_score / page_ascore | Page Authority Score of the linking page |
| domain_score / domain_ascore | Domain Authority Score of the referring domain |
| source_url | URL of the linking page |
| source_title | Title of the linking page |
| target_url | URL being linked to |
| anchor | Anchor text |
| external_num | External links on the source page |
| internal_num | Internal links on the source page |
| first_seen | Date backlink was first discovered |
| last_seen | Date backlink was last seen active |
| backlinks_num | Number of backlinks from a referring domain |
| domain | Referring domain name |
| ip | IP address of referring domain |
| country | Country of referring domain (by IP) |

### Position Tracking

| Code | Meaning |
|------|---------|
| Sh | Share of Voice |
| Sv | Search Visibility |

---

## Common Parameters

### database (Regional Database)

Required by most domain/keyword reports. Two-letter country code identifying the Google search market.

**Most-used values for GrowthX:**

| Code | Market |
|------|--------|
| `us` | United States (default for most audits) |
| `uk` | United Kingdom |
| `ca` | Canada |
| `au` | Australia |
| `de` | Germany |
| `fr` | France |

**Mobile databases** use a `mobile-` prefix: `mobile-us`, `mobile-uk`, etc.

**Extended databases** use an `-ext` suffix: `il-ext`, `tr-ext`, `dk-ext`, `no-ext`, `se-ext`, `fi-ext`, `ch-ext`.

Full list: `us uk ca ru de fr es it br au ar be ch dk fi hk ie il mx nl no pl se sg tr jp in hu` and 80+ more country codes.

### display_limit and display_offset

Pagination controls.

| Parameter | Default | Max | Notes |
|-----------|---------|-----|-------|
| display_limit | 50 | 4,000,000 (most); 100,000 (first page) | Set to 30–50 for exploration, higher for full exports |
| display_offset | 0 | — | Add to display_limit when paginating past 100k rows |

To get rows 100,001–200,000: `display_limit=200000, display_offset=100000`.

Backlink reports have a lower max of 100,000 (except `backlinks` which allows 1,000,000).

### display_date

Historical data access. Format: `YYYYMM15` for monthly snapshots (e.g., `20231215` for December 2023).

- Omit for latest data
- Use `display_daily` (format `YYYYMMDD`) for daily changes in the last 31 days (supported by `domain_organic`, `domain_rank_history`, `url_rank_history`)

### display_sort

Sort column and direction. Format: `column_asc` or `column_desc`. Values vary by report — listed under each report below.

### display_filter

See the dedicated **Filter Syntax** section below.

### export_columns

Comma-separated list of column codes to return. Omit to get default columns. Use this to reduce response size and focus on needed data.

### export_escape

Set to `"1"` to wrap column values in double quotes. Useful when values contain commas.

### export_decode

Set to `"0"` for URL-encoded responses, `"1"` for raw. Typically leave unset.

---

## Report Catalog

### 1. Domain Overview (`overview_research`)

5 reports for high-level domain metrics, rankings, and trends.

---

#### domain_rank

**Domain ranking in one regional database.** The starting point for any domain audit.

| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| domain | Yes | string | e.g. `vercel.com` |
| database | Yes | string | e.g. `us` |
| display_date | No | date | YYYYMM15 |
| export_columns | No | string[] | Default: Dn, Rk, Or, Ot, Oc, Ad, At, Ac |

**GrowthX usage:** Called by `seo-domain-audit` skill as the first step of every audit. Returns the single-row domain snapshot.

---

#### domain_rank_history

**Historical ranking trends.** Monthly organic traffic, keywords, and cost over time.

| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| domain | Yes | string | |
| database | Yes | string | |
| display_limit | No | int | Default 50; set higher for full history |
| display_daily | No | date | YYYYMMDD for daily changes (last 31 days) |
| display_sort | No | string | `dt_asc`, `dt_desc` |
| export_columns | No | string[] | Default: Rk, Or, Ot, Oc, Ad, At, Ac, Dt |

**GrowthX usage:** Called by `seo-domain-audit` to build 12–15 month trend charts. Use `display_limit=50` with `display_sort=dt_desc` to get the most recent 50 months.

---

#### domain_ranks

**Domain rankings across all databases.** Multi-region overview in a single call.

| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| domain | Yes | string | |
| database | No | string | Omit for all databases (~140 rows) |
| display_date | No | date | |
| display_limit | No | int | Default 50 |
| display_sort | No | string | rk/or/ot/oc/ad/at/ac + _asc/_desc |
| export_columns | No | string[] | Default: Db, Dn, Rk, Or, Ot, Oc, Ad, At, Ac, Sh, Sv |

**When to use:** International brands or multi-market comparisons. Avoid for single-region audits — use `domain_rank` instead.

---

#### overview_rank

**Top domains by traffic rank.** Market leaderboard for a given database.

| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| database | Yes | string | |
| display_date | No | date | |
| display_limit | No | int | Default 50 |
| display_filter | No | string | Filter by rank, traffic, etc. |
| export_columns | No | string[] | Default: Dn, Rk, Or, Ot, Oc, Ad, At, Ac |

**When to use:** Finding the biggest players in a market. Not useful for specific domain analysis.

---

#### rank_difference

**Winners and losers — ranking changes between periods.**

| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| database | Yes | string | |
| display_date | No | date | |
| display_limit | No | int | Default 50 |
| display_sort | No | string | om/tm/um/am/bm/cm/srm/stm/scm + _asc/_desc |
| export_columns | No | string[] | Default: Dn, Rk, Or, Ot, Oc, Ad, At, Ac, Tm, Um, Am, Bm, Cm |

**When to use:** Market movement analysis — who's gaining/losing organic traffic. Not for single-domain focus.

---

### 2. Organic Research (`organic_research`)

12 reports for organic keywords, competitors, paid search, domain comparison, and shopping.

---

#### domain_organic

**All organic keywords a domain ranks for.** The workhorse report for keyword analysis.

| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| domain | Yes | string | |
| database | Yes | string | |
| display_date | No | date | YYYYMM15 or YYYYMMDD |
| display_daily | No | date | YYYYMMDD; requires display_positions |
| display_limit | No | int | Default 50; max 4M |
| display_offset | No | int | |
| display_sort | No | string | po/tg/tr/tc/nq/co/kd/cp/nr/ts + _asc/_desc |
| display_filter | No | string | See filter syntax |
| display_positions | No | string | `new`, `lost`, `rise`, `fall` |
| display_positions_type | No | string | `organic` (default), `all`, `serp_features` |
| export_columns | No | string[] | Default: Ph, Po, Pp, Pd, Nq, Cp, Ur, Tr, Tc, Co, Nr, Td |

**GrowthX usage:** Core report for `seo-domain-audit` and `content-pages-audit`. Typically called with:
- `export_columns=Ur,Ph,Po,Nq,Tr,Tc` for audit data
- `display_limit=10000` or higher for full domain export
- `display_filter` to isolate content pages (e.g., URLs containing `/blog/`)

**Quick wins filter:** `+|Po|Gt|3|+|Po|Lt|21|+|Nq|Gt|100` (positions 4–20 with volume > 100)

---

#### domain_organic_unique

**Unique pages ranking in Google top 100.** One row per URL with aggregated metrics.

| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| domain | Yes | string | |
| database | Yes | string | |
| display_date | No | date | |
| display_limit | No | int | Default 50 |
| display_sort | No | string | pc/tg/tr/sr/st + _asc/_desc |
| display_filter | No | string | |
| export_columns | No | string[] | Default: Ur, Pc, Tg, Tr |

**GrowthX usage:** Called by `seo-domain-audit` to get all indexed pages and their traffic contribution. This is how we classify pages by type (Brand, Content, Templates, etc.).

---

#### domain_organic_organic

**Organic competitors.** Domains sharing the most keyword overlap.

| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| domain | Yes | string | |
| database | Yes | string | |
| display_date | No | date | |
| display_limit | No | int | Default 50 |
| display_sort | No | string | np_desc/np_asc/cr_desc/cr_asc |
| export_columns | No | string[] | Default: Dn, Cr, Np, Or, Ot, Oc, Ad |

**GrowthX usage:** Used by `competitive-seo-landscape` to discover the competitor set when none is provided.

---

#### domain_organic_subdomains

**Subdomains ranking in Google top 100.** Shows how traffic distributes across subdomains.

| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| domain | Yes | string | |
| database | Yes | string | |
| display_date | No | date | |
| display_limit | No | int | Default 50 |
| display_sort | No | string | pc/tg/tr/sr/st + _asc/_desc |
| export_columns | No | string[] | Default: Ur, Pc, Tg, Tr |

**When to use:** Understanding information architecture — how much traffic goes to docs.*, help.*, blog.*, etc.

---

#### domain_domains

**Keyword gap analysis between multiple domains.** The most powerful competitive report.

| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| domains | Yes | string | Special format (see below) |
| database | Yes | string | |
| display_date | No | date | |
| display_limit | No | int | Default 50 |
| display_sort | No | string | p0–p4/nq/co/cp/nr + _asc/_desc |
| display_filter | No | string | |
| export_columns | No | string[] | Default: Ph, P0, P1, P2, P3, P4, Nr, Cp, Nq, Kd, Co, Td |

**Domain format syntax:**

Each domain in the `domains` string follows: `<sign>|<type>|<domain>` separated by `|`.

- Sign: `*` (anchor), `+` (include), `-` (exclude), `/` (unique to one)
- Type: `or` (organic) or `ad` (paid)

**Common combinations:**

| Goal | Format |
|------|--------|
| Shared keywords | `*\|or\|domain1\|*\|or\|domain2\|*\|or\|domain3` |
| All keywords | `*\|or\|domain1\|+\|or\|domain2\|+\|or\|domain3` |
| Unique to domain1 | `*\|or\|domain1\|-\|or\|domain2\|-\|or\|domain3` |
| Missing from domain1 | `*\|or\|domain2\|*\|or\|domain3\|-\|or\|domain1` |
| Untapped for domain1 | `*\|or\|domain2\|+\|or\|domain3\|-\|or\|domain1` |

---

#### domain_adwords

**Paid search keywords a domain bids on.**

| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| domain | Yes | string | |
| database | Yes | string | |
| display_date | No | date | |
| display_limit | No | int | Default 50; max 1M |
| display_sort | No | string | po/tg/tr/tc/nq + _asc/_desc |
| display_filter | No | string | |
| display_positions | No | string | new/lost/rise/fall |
| export_columns | No | string[] | Default: Ph, Po, Pp, Pd, Nq, Cp, Vu, Tr, Tc, Co, Nr, Td |

---

#### domain_adwords_adwords

**Paid search competitors.** Domains competing in Google Ads for the same keywords.

Same parameter pattern as `domain_organic_organic`.

---

#### domain_adwords_historical

**Paid search keyword history.** Keywords a domain bid on in the last 12 months.

Same parameter pattern as `domain_organic` with `display_positions` support.

---

#### domain_adwords_unique

**Unique ad copies.** Ad texts SEMRush observed in paid results.

Same parameter pattern as `domain_organic_unique`.

---

#### domain_shopping / domain_shopping_shopping / domain_shopping_unique

**Shopping ads data for e-commerce domains.** Only works for domains with active shopping campaigns. Not relevant to most GrowthX B2B clients.

---

### 3. Backlink Analytics (`backlink_research`)

15 reports for analyzing link profiles. Uses `target` + `target_type` instead of `domain` + `database`.

**Common parameters for all backlink reports:**

| Parameter | Required | Type | Values |
|-----------|----------|------|--------|
| target | Yes | string | Domain, subdomain, or URL |
| target_type | Yes | string | `root_domain`, `domain` (for subdomains), `url` |

---

#### backlinks_overview

**High-level backlink metrics.** Total links, referring domains, authority score.

| Parameter | Required | Notes |
|-----------|----------|-------|
| target | Yes | |
| target_type | Yes | |
| export_columns | No | Default: total, domains_num, ips_num, follows_num, nofollows_num, score, trust_score, urls_num, ipclassc_num, texts_num, forms_num, frames_num, images_num |

**GrowthX usage:** Called by `seo-domain-audit` for the backlink summary in every audit.

---

#### backlinks

**Complete backlink list.** Every individual link with anchor text and authority scores.

| Parameter | Required | Notes |
|-----------|----------|-------|
| target | Yes | |
| target_type | Yes | |
| display_limit | No | Default 50; max 1,000,000 |
| display_sort | No | page_ascore/last_seen/first_seen + _asc/_desc |
| display_filter | No | Note: `urlanchor` filter doesn't work for large profiles |
| export_columns | No | Default: page_score, source_title, source_url, target_url, anchor, external_num, internal_num, first_seen, last_seen |

---

#### backlinks_refdomains

**Referring domains.** One row per domain linking to the target.

| Parameter | Required | Notes |
|-----------|----------|-------|
| target | Yes | |
| target_type | Yes | |
| display_limit | No | Default 50; max 100,000 |
| display_sort | No | domain_ascore/backlinks_num/last_seen/first_seen + _asc/_desc |
| export_columns | No | Default: domain, backlinks_num, domain_score, domain_trust_score, first_seen, last_seen, ip, country |

---

#### backlinks_anchors

**Anchor text distribution.** What text other sites use to link to the target.

| Parameter | Required | Notes |
|-----------|----------|-------|
| target | Yes | |
| target_type | Yes | |
| display_limit | No | Default 50; max 100,000 |
| display_sort | No | domains_num/backlinks_num/first_seen/last_seen + _asc/_desc |

---

#### backlinks_pages

**Indexed pages of the target domain.** Pages receiving backlinks.

| Parameter | Required | Notes |
|-----------|----------|-------|
| target | Yes | |
| target_type | Yes | |
| display_limit | No | Default 50; max 100,000 |
| display_sort | No | backlinks_num/domains_num/last_seen + _asc/_desc |

---

#### backlinks_historical

**Monthly backlink trends.** Historical count of backlinks and referring domains.

| Parameter | Required | Notes |
|-----------|----------|-------|
| target | Yes | Root domain only |
| target_type | Yes | Must be `root_domain` |
| display_limit | No | Default 50 |
| export_columns | No | Default: date, backlinks_num, domains_num, score |

---

#### backlinks_competitors

**Backlink competitors.** Domains with the most similar backlink profiles.

| Parameter | Required | Notes |
|-----------|----------|-------|
| target | Yes | |
| target_type | Yes | |
| display_limit | No | Default 50 |

---

#### backlinks_comparison

**Compare backlink profiles across multiple domains.**

| Parameter | Required | Notes |
|-----------|----------|-------|
| targets | Yes | String array of domains/URLs (max 200) |
| target_types | Yes | Parallel string array: `root_domain`, `domain`, or `url` for each target |
| export_columns | No | |

**Example params:**
```json
{
  "targets": ["vercel.com", "netlify.com", "cloudflare.com"],
  "target_types": ["root_domain", "root_domain", "root_domain"]
}
```

---

#### backlinks_matrix

**Matrix comparison of backlink metrics.** Referring domains that link to multiple targets.

| Parameter | Required | Notes |
|-----------|----------|-------|
| targets | Yes | String array |
| target_types | Yes | Parallel string array |
| display_limit | No | Default 50; max 100,000 |
| display_sort | No | domain_score/matchesnum/backlinksnum_N + _asc/_desc (N = 0–5) |

---

#### backlinks_ascore_profile

**Authority Score distribution.** How referring domains break down by authority score ranges.

| Parameter | Required | Notes |
|-----------|----------|-------|
| target | Yes | |
| target_type | Yes | |

Minimal parameters — just target and type.

---

#### backlinks_geo

**Geographic distribution of referring domains** (by IP address).

| Parameter | Required | Notes |
|-----------|----------|-------|
| target | Yes | |
| target_type | Yes | |
| display_limit | No | Default 50 |
| display_sort | No | domains_num/backlinks_num + _asc/_desc |

---

#### backlinks_tld

**TLD distribution of referring domains** (.com, .org, .edu, etc.).

Same parameter pattern as `backlinks_geo`.

---

#### backlinks_categories

**Categories the target domain belongs to.** Returns category names with confidence ratings (0–1).

| Parameter | Required | Notes |
|-----------|----------|-------|
| target | Yes | |
| target_type | Yes | `root_domain`, `subdomain`, or `url` |

---

#### backlinks_categories_profile

**Categories of referring domains.** What types of sites link to you.

| Parameter | Required | Notes |
|-----------|----------|-------|
| target | Yes | |
| target_type | Yes | |
| display_limit | No | Default 50 |

---

#### backlinks_refips

**Referring IP addresses.** IP-level analysis of backlink sources.

| Parameter | Required | Notes |
|-----------|----------|-------|
| target | Yes | |
| target_type | Yes | |
| display_limit | No | Default 50 |
| display_sort | No | domains_num/backlinks_num/first_seen/last_seen + _asc/_desc |

---

### 4. Keyword Research (`keyword_research`)

10 reports for analyzing individual keywords — volume, difficulty, SERP, related terms.

---

#### phrase_this

**Single keyword overview.** Volume, CPC, competition in one database.

| Parameter | Required | Notes |
|-----------|----------|-------|
| phrase | Yes | Single keyword or phrase |
| database | Yes | |
| display_date | No | |
| export_columns | No | Default: Ph, Nq, Cp, Co, Nr |

---

#### phrase_all

**Single keyword across all databases.** Global volume and competition data.

| Parameter | Required | Notes |
|-----------|----------|-------|
| phrase | Yes | |
| database | No | Omit for all databases |
| export_columns | No | Default: Dt, Db, Ph, Nq, Cp, Co |

---

#### phrase_these

**Batch keyword analysis.** Multiple keywords in one call.

| Parameter | Required | Notes |
|-----------|----------|-------|
| phrase | Yes | Semicolon-separated: `keyword1;keyword2;keyword3` |
| database | Yes | |
| display_date | No | |
| export_columns | No | Default: Ph, Nq, Cp, Co, Nr, Td |

---

#### phrase_organic

**SERP analysis for a keyword.** Which domains rank and at what positions.

| Parameter | Required | Notes |
|-----------|----------|-------|
| phrase | Yes | |
| database | Yes | |
| display_date | No | |
| display_limit | No | Default 50 |
| positions_type | No | `organic` (default), `all` (includes SERP features) |
| export_columns | No | Default: Dn, Ur, Fk |

---

#### phrase_related

**Semantically related keywords.** For content expansion and topic clustering.

| Parameter | Required | Notes |
|-----------|----------|-------|
| phrase | Yes | |
| database | Yes | |
| display_limit | No | Default 50 |
| display_sort | No | nq/cp/co/nr/rr/kd + _asc/_desc |
| display_filter | No | |
| export_columns | No | Default: Ph, Nr, Cp, Co, Nq, Td, Rr |

---

#### phrase_fullsearch

**Broad match keywords.** All queries containing the target phrase or variations.

| Parameter | Required | Notes |
|-----------|----------|-------|
| phrase | Yes | |
| database | Yes | |
| display_limit | No | Default 50; max 100,000 |
| display_sort | No | nq/cp/co/nr/kd + _asc/_desc |
| display_filter | No | |
| export_columns | No | Default: Ph, Nr, Cp, Co, Nq, Td |

---

#### phrase_questions

**Question-format keywords.** Questions related to the target keyword.

| Parameter | Required | Notes |
|-----------|----------|-------|
| phrase | Yes | |
| database | Yes | |
| display_limit | No | Default 50; **max 100** |
| display_sort | No | nq/cp/co/nr/kd + _asc/_desc |
| display_filter | No | |
| export_columns | No | Default: Ph, Nr, Cp, Co, Nq, Td |

**Gotcha:** Maximum results capped at 100, not 100,000 like other reports.

---

#### phrase_kdi

**Keyword difficulty index.** Batch difficulty scoring.

| Parameter | Required | Notes |
|-----------|----------|-------|
| phrase | Yes | Semicolon-separated (1–100 keywords) |
| database | Yes | |
| export_columns | No | Default: Ph, Kd |

---

#### phrase_adwords

**Paid search SERP for a keyword.** Which domains are bidding.

| Parameter | Required | Notes |
|-----------|----------|-------|
| phrase | Yes | |
| database | Yes | |
| display_date | No | |
| display_limit | No | Default 50; **max 100** |
| export_columns | No | Default: Dn, Vu |

---

#### phrase_adwords_historical

**Historical paid search positions for a keyword.**

Same pattern as `phrase_adwords` with date range support.

---

### 5. URL Analytics (`url_research`)

5 reports for page-level keyword and ranking data.

---

#### url_organic

**Keywords driving organic traffic to a specific URL.**

| Parameter | Required | Notes |
|-----------|----------|-------|
| url | Yes | Full URL of the page |
| database | Yes | |
| display_date | No | |
| display_limit | No | Default 50; max 4M |
| display_sort | No | po/tg/tr/tc/nq + _asc/_desc |
| display_filter | No | |
| display_positions_type | No | `organic`, `all`, `serp_features` |
| export_columns | No | Default: Ph, Po, Nq, Cp, Co, Tr, Tc, Nr, Td, Fp, Ts |

**GrowthX usage:** Used in Vercel audit to pull per-page keyword data for every content URL. Files stored in `projects/audit-reports/vercel/page-audits/url-organic/`.

---

#### url_rank_history

**Historical keyword rankings for a URL.** Monthly or daily rank snapshots.

| Parameter | Required | Notes |
|-----------|----------|-------|
| url | Yes | |
| database | Yes | |
| display_limit | No | Default 50 |
| display_daily | No | YYYYMMDD for daily (last 31 days) |
| display_sort | No | dt_asc, dt_desc |
| export_columns | No | Default: Rk, Or, Ot, Oc, Ad, At, Ac, Dt |

**Note:** Rk returns 0 for URLs — it only returns rank data for root domains.

**GrowthX usage:** Used in Vercel audit for per-page traffic trajectory analysis. Files stored in `projects/audit-reports/vercel/page-audits/url-rank-history/`.

---

#### url_rank

**Current keyword rankings for a URL** in a single database.

Same parameters as `url_rank_history` without `display_daily`.

---

#### url_ranks

**URL rankings across all databases.**

| Parameter | Required | Notes |
|-----------|----------|-------|
| url | Yes | |
| database | No | Omit for all databases |

---

#### url_adwords

**Paid search keywords for a URL.**

Same pattern as `url_organic` but for paid positions.

---

### 6. Subdomain Analytics (`subdomain_research`)

7 reports mirroring the URL/domain pattern but scoped to subdomains.

---

#### subdomain_organic

**Organic keywords for a subdomain** (e.g., `docs.vercel.com`).

Same parameter pattern as `domain_organic`, with `domain` param taking the subdomain.

---

#### subdomain_organic_unique

**Unique pages of a subdomain ranking in top 100.**

Same as `domain_organic_unique`.

---

#### subdomain_rank / subdomain_rank_history / subdomain_ranks

**Ranking snapshots for a subdomain** — single-db, historical, or all-db.

Same patterns as the corresponding `domain_rank*` reports.

---

#### subdomain_adwords / subdomain_adwords_unique

**Paid search data for a subdomain.**

Same patterns as the corresponding `domain_adwords*` reports.

---

### 7. Subfolder Analytics (`subfolder_research`)

7 reports mirroring subdomain analytics but scoped to URL path prefixes.

**Important:** Subfolder values require a trailing slash (e.g., `vercel.com/blog/`).

---

#### subfolder_organic

**Organic keywords for a subfolder** (e.g., `vercel.com/templates/`).

Same parameter pattern as `domain_organic`, with `domain` param taking the subfolder path.

---

#### subfolder_organic_unique

**Unique pages within a subfolder ranking in top 100.**

---

#### subfolder_rank / subfolder_rank_history / subfolder_ranks

**Ranking snapshots for a subfolder.**

---

#### subfolder_adwords / subfolder_adwords_unique

**Paid search data for a subfolder.**

---

### 8. Position Tracking (`tracking_research`)

13 reports for monitoring keyword rankings over time within SEMRush projects. Requires an active Position Tracking campaign.

**Prerequisite:** Use `list_projects` → `campaigns` to find your project_id and campaign_id.

---

#### campaigns

**List campaigns for a project.**

| Parameter | Required | Notes |
|-----------|----------|-------|
| project_id | Yes | From `list_projects` or the SEMRush UI URL |

---

#### tracking_campaign_dates

**Dates when campaign data was harvested.**

| Parameter | Required | Notes |
|-----------|----------|-------|
| campaign_id | Yes | |

---

#### tracking_overview_organic

**Keyword distribution and changes.** How many keywords in top 3, top 10, top 100, plus new/lost/improved/declined.

| Parameter | Required | Notes |
|-----------|----------|-------|
| campaign_id | Yes | |
| url | Yes | Domain with mask (e.g., `*.vercel.com/*`) |
| date_begin / date_end | No | YYYYMMDD |
| display_tags | No | Filter by tags; `\|` = OR, `-tag` = exclude |
| linktype_filter | No | Include/exclude local pack, hotel rankings |

---

#### tracking_overview_adwords

**Same as above but for paid positions.**

---

#### tracking_position_organic

**Per-keyword positions and changes.** The detailed keyword-by-keyword view.

| Parameter | Required | Notes |
|-----------|----------|-------|
| campaign_id | Yes | |
| url | Yes | Domain with mask |
| date_begin / date_end | No | |
| display_limit | No | Default 10 |
| display_sort | No | Complex sort options (see schema) |
| display_filter | No | Filter on Ph, Nq, Cp |
| display_tags | No | |
| top_filter | No | `top_3`, `top_1page`, `top_2page`, `top_100` + _income/_leave/_down/_up |
| serp_feature_filter | No | Filter by SERP feature presence |
| use_volume | No | `national`, `regional`, `local` |

**SERP feature codes:** aai (Ask AI), aio (AI overview), fsn (Featured snippet), geo (Local pack), kng (Knowledge panel), rel (People also ask), shp (Shopping), vid (Video), and 30+ more.

---

#### tracking_position_adwords

**Same as above but for paid positions.**

---

#### tracking_competitors_organic / tracking_competitors_adwords

**Competitor visibility within the tracking campaign.**

| Parameter | Required | Notes |
|-----------|----------|-------|
| campaign_id | Yes | |
| url | Yes | |
| date_begin / date_end | No | |

---

#### tracking_landing_pages_organic / tracking_landing_pages_adwords

**Landing pages from tracking campaign results.**

---

#### tracking_visibility_organic / tracking_visibility_adwords

**Visibility score and changes over time.**

---

#### locations

**Location lookup.** Search for tracking locations by ID, type, or name.

| Parameter | Required | Notes |
|-----------|----------|-------|
| (see schema) | | Used for setting up tracking campaigns |

---

### 9. Site Audit (`siteaudit_research`)

8 reports for technical SEO audits. Requires an active Site Audit project.

**Prerequisite:** Use `list_projects` to get your project ID. Site Audit must be enabled and have completed at least one crawl.

---

#### snapshots

**List audit snapshots for a project.** Starting point for site audit analysis.

| Parameter | Required | Notes |
|-----------|----------|-------|
| id | Yes | Project ID (from URL: semrush.com/projects/**6647718**) |

---

#### snapshot

**Audit overview.** Score, issue counts, crawl stats.

| Parameter | Required | Notes |
|-----------|----------|-------|
| id | Yes | Project ID |
| snapshot_id | Yes | From `snapshots` response |

---

#### info

**Most recent audit summary.** Quick status check.

| Parameter | Required | Notes |
|-----------|----------|-------|
| id | Yes | Project ID |

---

#### history

**Audit results over time.**

| Parameter | Required | Notes |
|-----------|----------|-------|
| id | Yes | Project ID |
| limit | No | Default 7 |
| offset | No | Default 0 |

---

#### meta_issues

**Issue descriptions and explanations.** What each issue ID means.

| Parameter | Required | Notes |
|-----------|----------|-------|
| id | Yes | Project ID |

---

#### issue_details

**URLs affected by a specific issue.**

| Parameter | Required | Notes |
|-----------|----------|-------|
| id | Yes | Project ID |
| snapshot_id | Yes | |
| issueid | Yes | Integer; from `snapshot` or `meta_issues` |
| limit | No | Default 10 |
| page | No | Default 1 |
| sort | No | Default DESC |

---

#### page_list

**Search for pages by URL.** Returns page IDs needed for `page_info`.

| Parameter | Required | Notes |
|-----------|----------|-------|
| id | Yes | Project ID |
| url | Yes | URL substring to match |
| limit | No | |

---

#### page_info

**Detailed page information and issues.**

| Parameter | Required | Notes |
|-----------|----------|-------|
| id | Yes | Project ID |
| pageid | Yes | From `page_list` response |

---

### 10. Project Management (`projects_research`)

2 reports for managing SEMRush projects.

---

#### list_projects

**List all projects.**

| Parameter | Required | Notes |
|-----------|----------|-------|
| filter | No | `all`, `own` (default), `shared`, `corporate` |

---

#### get_project

**Single project details.**

| Parameter | Required | Notes |
|-----------|----------|-------|
| (project ID in path) | Yes | |

---

### 11. Traffic Analytics (`trends_research`)

**Requires a separate subscription** — not available on the current SEMRush plan.

Would provide: website traffic estimates, audience demographics, traffic sources, and competitive traffic analysis.

To enable: Purchase a Traffic Analytics plan at https://www.semrush.com/analytics/traffic/trends-api

---

## Filter Syntax

The `display_filter` parameter uses a structured format to narrow results.

### Format

```
<sign>|<field>|<operation>|<value>
```

| Component | Values | Meaning |
|-----------|--------|---------|
| sign | `+` | Include rows matching this condition |
| | `-` | Exclude rows matching this condition |
| field | Column code | Ph, Nq, Po, Ur, Co, Kd, etc. |
| operation | See table below | Comparison type |
| value | string/number | What to compare against |

### Operations

| Code | Meaning | Works with |
|------|---------|------------|
| Eq | Equals | All types |
| Co | Contains | Strings |
| Bw | Begins with | Strings |
| Ew | Ends with | Strings |
| Lt | Less than | Numbers |
| Gt | Greater than | Numbers |
| Le | Less than or equal | Numbers |
| Ge | Greater than or equal | Numbers |

### Combining Filters

Separate multiple filters with `|` at the end of each filter expression. Maximum 25 filters per request.

### Examples

| Goal | Filter |
|------|--------|
| Blog pages only | `+\|Ur\|Co\|/blog/` |
| High-volume keywords | `+\|Nq\|Gt\|1000` |
| Positions 4–20 | `+\|Po\|Gt\|3\|+\|Po\|Lt\|21` |
| Quick wins (pos 4–20, vol > 100) | `+\|Po\|Gt\|3\|+\|Po\|Lt\|21\|+\|Nq\|Gt\|100` |
| Exclude branded terms | `-\|Ph\|Co\|vercel` |
| Low competition | `+\|Co\|Lt\|0.5` |
| Easy keywords to rank for | `+\|Kd\|Lt\|40\|+\|Nq\|Gt\|500` |
| Content pages losing traffic | `+\|Ur\|Co\|/blog/` (combine with `display_positions=lost`) |

---

## GrowthX Usage Patterns

How our audit skills use the SEMRush MCP today.

### seo-domain-audit

The foundation audit. Pulls these reports in sequence:

| Step | Report | Parameters | Purpose |
|------|--------|-----------|---------|
| 1 | `domain_rank` | database=us | Domain snapshot — Rk, Or, Ot, Oc |
| 2 | `domain_rank_history` | database=us, display_limit=50, display_sort=dt_desc | 12–15 month trend |
| 3 | `backlinks_overview` | target_type=root_domain | Backlink summary |
| 4 | `domain_organic_unique` | database=us, display_limit=10000 | All indexed pages for classification |
| 5 | `domain_organic` | database=us, display_limit=10000, export_columns=Ur,Ph,Po,Nq,Tr,Tc | All keywords for position distribution |

After pulling: pages are classified by URL pattern into Brand / Content / Templates / Transactional / Education / Support / UGC / Docs / Other. Six-month deltas are calculated by comparing `display_date` snapshots.

### competitive-seo-landscape

Pulls competitor data in batch:

| Step | Report | Parameters | Purpose |
|------|--------|-----------|---------|
| 1 | `domain_organic_organic` | database=us | Discover competitor set |
| 2 | `domain_rank` | For each competitor | Competitor snapshots |
| 3 | `domain_rank_history` | For each competitor | Competitor trends |

Competitors are tiered: Tier 1 (Leaders — 10x+ traffic), Tier 2 (Challengers — 2–10x), Tier 3 (Peers — 0.5–2x).

### content-pages-audit

Deep per-page analysis:

| Step | Report | Parameters | Purpose |
|------|--------|-----------|---------|
| 1 | `domain_organic` | database=us, display_filter=+\|Ur\|Co\|/blog/ | Content page keywords |
| 2 | `domain_organic` | display_date=6 months ago | Historical comparison |
| 3 | `url_organic` | Per top page | Detailed keyword portfolio |
| 4 | `url_rank_history` | Per top page | Traffic trajectory |

The `Tr` column is a percentage of total domain traffic. Convert to absolute: `absolute_traffic = Tr × total_domain_traffic / 100`.

### Vercel deep dive scripts

The Node.js scripts in `projects/audit-reports/vercel/page-audits/` demonstrate production use:

- `url_organic` JSON files are pulled for each of 523 content pages
- `url_rank_history` JSON files are pulled for 548 pages (15-month span)
- `audit-utils.js` classifies trends using the data: Accelerating, Growing, Stable, Peaked, Declining, New, Dead
- `generate-overview-v3.js` aggregates all data into the SEO overview

---

## Subscription Notes

| Feature | Current Plan | Required Plan |
|---------|-------------|---------------|
| Domain Overview | Available | SEO plan |
| Organic Research | Available | SEO plan |
| Backlink Analytics | Available | SEO plan |
| Keyword Research | Available | SEO plan |
| URL Analytics | Available | SEO plan |
| Subdomain/Subfolder | Available | SEO plan |
| Position Tracking | Available | SEO plan + active project |
| Site Audit | Available | SEO plan + active project |
| Traffic Analytics | **Not available** | Separate purchase at semrush.com/analytics/traffic/trends-api |

API costs are per-row. Large exports (10,000+ rows) consume significant API units. Use `display_limit` judiciously when exploring.

---

## Quick Reference — Report Count by Category

| Category | Discovery Tool | Reports | Key Reports |
|----------|---------------|---------|-------------|
| Domain Overview | `overview_research` | 5 | domain_rank, domain_rank_history |
| Organic Research | `organic_research` | 12 | domain_organic, domain_organic_unique, domain_domains |
| Backlink Analytics | `backlink_research` | 15 | backlinks_overview, backlinks_refdomains, backlinks_historical |
| Keyword Research | `keyword_research` | 10 | phrase_this, phrase_related, phrase_kdi, phrase_questions |
| URL Analytics | `url_research` | 5 | url_organic, url_rank_history |
| Subdomain Analytics | `subdomain_research` | 7 | subdomain_organic, subdomain_rank_history |
| Subfolder Analytics | `subfolder_research` | 7 | subfolder_organic, subfolder_rank_history |
| Position Tracking | `tracking_research` | 13 | tracking_position_organic, tracking_overview_organic |
| Site Audit | `siteaudit_research` | 8 | snapshot, issue_details, page_info |
| Project Management | `projects_research` | 2 | list_projects |
| Traffic Analytics | `trends_research` | N/A | Requires separate subscription |
| **Total** | **11** | **84** | |
