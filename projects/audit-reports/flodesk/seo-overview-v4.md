# SEO & AI Visibility Overview: flodesk.com (v4)

**Date:** February 28, 2026
**Domain:** flodesk.com

---

## 1. Core metrics snapshot

| # | Metric | Current (Feb 2026) | Aug 2025 | 6mo Change |
|---|--------|--------------------|----------|------------|
| 1 | Site authority score | **46** | 46 | — |
| 2 | Referring domains | **36,931** | 38,455 | -4.0% |
| 3 | Total organic traffic | **65,668/mo** | 68,667/mo | -4.4% |
| 4 | Total pages indexed | **2,187** | 2,408 | -9.2% |
| 5 | Total pages getting organic traffic | **575** | 651 | -11.7% |
| 6 | Total content pages | **935** | 956 | -2.2% |
| 7 | Content pages getting organic traffic | **466** | 498 | -6.4% |
| 8 | Organic traffic per page (w/ traffic) | **114.2** | 105.5 | +8.3% |
| 9 | Organic traffic per content page (w/ traffic) | **31.6** | 46.8 | -32.5% |

Metric #8 (traffic per page) went up despite total traffic going down because 76 pages lost traffic entirely — the tail got cut, which raised the average. Don't read this as improvement.

### 12-month trend

| Period | Organic Traffic | Trend |
|--------|----------------|-------|
| Feb 2025 | 48,102 | Baseline |
| Mar–Apr 2025 | 51,633 → 64,663 | +34% surge |
| May–Jul 2025 | 64,102 → 65,485 | Plateau |
| Aug–Sep 2025 | 68,667 → 79,491 | +16% climb |
| Oct–Dec 2025 | 79,036 → 80,413 | Peak (~80K) |
| Jan 2026 | 74,716 | -7% decline starts |
| Feb 2026 | 65,668 | -18% from peak |

Flodesk grew organic traffic 67% from Feb to Dec 2025 (48K → 80K), driven by aggressive content publishing in `/tips/`. But Feb 2026 has given back most of that gain. The current 65,668 is nearly flat vs. where they were in May 2025.

---

## 2. Site structure & technical

### Authority is flat, but the link base is eroding

Authority score of 46 hasn't moved in 6 months. But referring domains dropped from 38,455 to 36,931 — a net loss of 1,524 linking domains. Total backlinks also declined from 14.2M to 13.7M. The authority score is holding thanks to score recalibration (it jumped from 40 to 46 in Aug 2025), but the underlying link base is shrinking.

Most of the 36,931 referring domains likely come from embed forms and signup widgets distributed across customer sites (5M form-based backlinks in the profile). As customers churn or rebuild their sites, those links disappear.

### The homepage carries everything

The homepage alone drives **44,652 of the 65,668 monthly organic visits — 68% of all organic traffic.** That's a branded search moat, not a content engine. And that branded traffic actually grew over 6 months (39,772 → 46,701, +17.4%), masking the content decline.

### Page breakdown by type

| Type | Pages | 6mo | Keywords | 6mo | w/ Traffic | 6mo | Traffic | 6mo | Traffic/Page | 6mo |
|------|-------|-----|----------|-----|-----------|-----|---------|-----|--------------|-----|
| Brand | 11 | +1 | 2,362 | -33.7% | 6 | -2 | 46,486 | +17.3% | 7,748 | +44.2% |
| Content | 935 | -21 | 17,418 | -3.7% | 466 | -32 | 14,730 | -36.8% | 31.6 | -32.6% |
| Templates | 7 | +1 | 134 | -6.9% | 2 | 0 | 215 | -17.9% | 107.5 | -17.9% |
| Transactional | 14 | +2 | 1,142 | +153.2% | 6 | 0 | 3,278 | -3.1% | 546 | -3.1% |
| Education | 27 | +2 | 112 | +15.5% | 3 | 0 | 15 | +25.0% | 5.0 | +25.0% |
| Support | 170 | -23 | 1,131 | -8.6% | 34 | -33 | 469 | -71.1% | 13.8 | -43.2% |
| User-generated | 1,016 | -183 | 2,746 | -5.1% | 56 | -9 | 345 | -35.3% | 6.2 | -24.8% |
| Docs | 4 | 0 | 16 | +14.3% | 1 | 0 | 65 | +85.7% | 65.0 | +85.7% |
| Other | 3 | 0 | 40 | — | 1 | 0 | 65 | — | 65.0 | — |
| **Total** | **2,187** | **-221** | **25,101** | **-5.3%** | **575** | **-76** | **65,668** | **-4.4%** | **114.2** | **+8.3%** |

**Type definitions:**
- **Brand** — Homepage, pricing, product pages (/email, /link-in-bio, /workflow), careers, partners
- **Templates** — /templates/ gallery and individual template preview pages
- **Content** — /tips/ and /blog/ editorial pages (see content breakdown in section 3)
- **Transactional** — Sign-in, sign-up, checkout, forms, legal pages
- **Education** — university.flodesk.com courses and resources
- **Docs** — developers.flodesk.com, grain.flodesk.com (design system)
- **Support** — help.flodesk.com
- **User-generated** — view.flodesk.com email previews and landing pages, usercontent.flodesk.com PDFs
- **Other** — Campaign shortlinks (/c/), uncategorized

### Half the index is customer-hosted content

1,016 pages on `view.flodesk.com` (hosted email previews and landing pages) are indexed by Google. They drive only 345 visits total. This is potential index bloat — Google is spending crawl budget on low-value customer content pages instead of Flodesk's editorial pages.

### Templates gallery is a missed opportunity

7 pages under `/templates/email` are indexed. The main gallery page drives 212 visits/month from 121 keywords — stronger than 97% of blog posts. But individual template pages use hash IDs (`/templates/email/619314...`) and get almost no traffic. Category pages, tagging, and proper URL structure could unlock significantly more search traffic.

---

## 3. Content health

### By section

| Section | Pages | 6mo | Keywords | 6mo | w/ Traffic | 6mo | Traffic | 6mo | Traffic/Page | 6mo |
|---------|-------|-----|----------|-----|-----------|-----|---------|-----|--------------|-----|
| Tips (/tips/) | 752 | -9 | 14,256 | +6.8% | 415 | -11 | 12,828 | -39.6% | 30.9 | -38.1% |
| Blog (/blog/) | 183 | -12 | 3,162 | -33.1% | 51 | -21 | 1,902 | -6.5% | 37.3 | +33.9% |
| **Content total** | **935** | **-21** | **17,418** | **-3.7%** | **466** | **-32** | **14,730** | **-36.8%** | **31.6** | **-32.6%** |

Content traffic dropped **36.8% in 6 months** — from 23,309 to 14,730 visits/month. The per-page yield tells the same story: traffic per content page fell from 46.8 to 31.6 (-32.5%). Flodesk published roughly the same number of content pages (956 → 935), but 32 fewer pages are getting any traffic at all (498 → 466).

### Content page trajectory (all 467 pages with traffic)

Every content page was categorized by its 6-month traffic change:

| Category | Threshold | Pages | % of Pages | Traffic Now | Aug Traffic | 6mo Change | Avg/Page |
|----------|-----------|------:|---:|---:|---:|---:|---:|
| Freefall | Lost >50% | 140 | 30% | 3,233 | 12,930 | -9,697 | 23.1 |
| Declining | Lost 10–50% | 61 | 13% | 3,720 | 5,547 | -1,827 | 61.0 |
| Stable | -10% to +25% | 40 | 9% | 1,705 | 1,557 | +148 | 42.6 |
| Growing | +25% to +100% | 46 | 10% | 1,965 | 1,323 | +642 | 42.7 |
| Surging | >+100% or new | 180 | 39% | 4,109 | 820 | +3,289 | 22.8 |
| **Total** | | **467** | **100%** | **14,732** | **22,177** | **-7,445** | **31.5** |

**By section:**

| Category | Tips | Blog | Tips % | Blog % |
|----------|-----:|-----:|-------:|-------:|
| Freefall | 119 | 21 | 29% | 41% |
| Declining | 57 | 4 | 14% | 8% |
| Stable | 37 | 3 | 9% | 6% |
| Growing | 42 | 4 | 10% | 8% |
| Surging | 161 | 19 | 39% | 37% |

**43% of pages are losing traffic** (freefall + declining = 201 pages). These pages hold 47% of current content traffic (6,953 visits) but lost 11,524 visits in 6 months. The freefall category alone accounts for 9,697 lost visits — 130% of the total net decline, meaning growth elsewhere is partially offsetting the collapse.

**Only 9% of pages are stable.** A healthy content portfolio would show a bell curve centered on stable. Flodesk's distribution is bimodal — pages are either collapsing or growing, with almost nothing in between. This suggests a systemic shift (algorithm change, competitive displacement, or content aging) rather than normal organic fluctuation.

**Blog pages are disproportionately in freefall.** 41% of blog pages with traffic are in freefall (vs. 29% of tips pages). Blog content is more fragile despite having higher per-page yield.

### The /tips/ section

752 pages following the pattern `{topic}-email-templates` or `{niche}-newsletters`. This is a programmatic-style play targeting long-tail email template searches. 415 of 752 tips pages get some traffic, but yield per page is low (30.9 visits/mo average). Tips traffic dropped 39.6% in 6 months. The strategy has breadth but lacks depth on any single topic.

### Blog is underperforming

183 blog pages, but only 51 get organic traffic (27%). Total blog traffic: 1,902/mo. Blog traffic declined less than tips (-6.5% vs -39.6%), suggesting blog content is more resilient — it just needs more of it working.

---

## 4. Competitive SEO positioning

SEMRush domain metrics and DataForSEO keyword position data were pulled for 32 direct competitors across three competitive tiers. Full analysis in `competitive-landscape-v1.md`.

### Where Flodesk ranks among 32 competitors (by organic traffic)

| Organic Rank | Company | Tier | Organic Traffic | Organic KW | Traffic Value ($) | Traffic/KW |
|---:|---|---|---:|---:|---:|---:|
| 7 | beehiiv | 2 | 133,584 | 99,356 | $218,443 | 1.34 |
| 8 | ActiveCampaign | 1 | 84,347 | 43,688 | $836,780 | 1.93 |
| 9 | Kit | 2 | 82,960 | 41,006 | $241,526 | 2.02 |
| 10 | Campaign Monitor | 2 | 81,057 | 46,461 | $772,008 | 1.74 |
| 11 | Kajabi | 2 | 72,818 | 18,782 | $255,608 | 3.88 |
| 12 | MailerLite | 2 | 66,636 | 37,099 | $393,666 | 1.80 |
| **13** | **Flodesk** | **3** | **65,132** | **24,777** | **$220,951** | **2.63** |
| 14 | Ghost | 3 | 61,041 | 26,487 | $121,238 | 2.30 |
| 15 | Brevo | 1 | 55,106 | 31,994 | $430,934 | 1.72 |
| 16 | Omnisend | 2 | 47,041 | 53,757 | $234,434 | 0.88 |
| 17 | Systeme.io | 3 | 38,870 | 17,529 | $210,102 | 2.22 |

Flodesk is 13th of 32 by organic traffic — ahead of tier-1 player Brevo ($220M revenue, €500M in funding) and tier-2 players Omnisend, GetResponse, Keap, Drip, and AWeber. For a bootstrapped company scored 20th overall, this organic position is a genuine competitive advantage.

### Keyword position distribution

| Company | Total KW | Top 3 | Top 3 % | Top 10 | Top 10 % | KW Rising | KW Declining | Net |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Mailchimp | 112,466 | 4,155 | 3.7% | 14,099 | 12.5% | 35,996 | 30,315 | +5,681 |
| beehiiv | 56,709 | 1,354 | 2.4% | 6,981 | 12.3% | 29,982 | 13,292 | +16,690 |
| Klaviyo | 26,699 | 931 | 3.5% | 3,134 | 11.7% | 12,257 | 6,329 | +5,928 |
| Kit | 23,578 | 385 | 1.6% | 2,045 | 8.7% | 10,206 | 6,617 | +3,589 |
| Omnisend | 21,471 | 621 | 2.9% | 2,220 | 10.3% | 6,030 | 9,943 | -3,913 |
| ActiveCampaign | 17,123 | 720 | 4.2% | 1,769 | 10.3% | 6,197 | 5,059 | +1,138 |
| MailerLite | 15,981 | 411 | 2.6% | 1,775 | 11.1% | 6,083 | 5,205 | +878 |
| **Flodesk** | **13,954** | **889** | **6.4%** | **2,654** | **19.0%** | **4,800** | **5,625** | **-825** |
| Ghost | 13,406 | 299 | 2.2% | 1,094 | 8.2% | 6,244 | 2,732 | +3,512 |
| Systeme.io | 7,599 | 109 | 1.4% | 511 | 6.7% | 3,229 | 2,132 | +1,097 |

**Flodesk has the highest top-3 concentration (6.4%) and top-10 concentration (19%) of any competitor.** Nearly 1 in 5 ranking keywords sits on Google's first page — compared to 12.5% for Mailchimp, 11.7% for Klaviyo, and just 8.7% for Kit. The content Flodesk publishes ranks well. The problem is volume.

The warning sign: Flodesk is one of only two companies (alongside Omnisend) with a net-negative keyword trajectory. beehiiv is adding keywords at a 2.3:1 ratio; Flodesk is losing them.

### Organic efficiency

| Metric | Flodesk | Rank | Context |
|---|---|---|---|
| Traffic per content page (w/ traffic) | 31.6 | — | Down from 46.8 six months ago (-32.5%) |
| Traffic per page (all w/ traffic) | 114.2 | — | Artificially up because 76 pages dropped out of the traffic set |
| Keywords per page (all indexed) | 11.5 | — | 25,101 keywords across 2,187 pages |
| Traffic per keyword | 2.63 | **3rd of 32** | Behind Kajabi (3.88) and Mailchimp (2.89) |
| Top-3 keyword concentration | 6.4% | **1st of 10** | 889 keywords in positions 1–3 — 52% more than next closest (ActiveCampaign 4.2%) |
| Top-10 keyword concentration | 19.0% | **1st of 10** | Highest quality-to-quantity ratio in the competitive set |

Flodesk's organic efficiency is genuinely strong. The gap is breadth: 24.8K keywords vs. beehiiv's 99K, Kit's 41K, or even Moosend's 39K. Doubling the keyword footprint at current efficiency would put Flodesk in the top 10 by organic traffic.

### Direct competitive threats

**Kit (ConvertKit)** is the most direct competitor. Kit's organic footprint (41K keywords, 83K traffic) is 66% larger by keyword count but only 27% larger by traffic — Flodesk's higher traffic-per-keyword (2.63 vs. 2.02) means it converts rankings to clicks more efficiently. Kit serves 600K+ creators vs. Flodesk's 100K.

**MailerLite** matches Flodesk's simplicity promise at a lower price ($9/mo vs. $25/mo), with more features and a generous free plan. Its organic profile (37K keywords, 67K traffic) is nearly identical to Flodesk's — making it the closest organic peer.

**beehiiv** is the rising threat. 99K keywords, 134K traffic, and a 2.3:1 rising-to-declining keyword ratio — all from a 110-person company founded in 2021. Its publisher-hosted newsletters create a natural UGC content flywheel that Flodesk lacks. beehiiv is growing from $30M to a projected $50M in 2026.

---

## 5. AI visibility

Data from the CheckThat AI Visibility Index: 201 evaluation-stage, unbranded buyer prompts tracked daily across ChatGPT, Perplexity, Claude, Gemini, and Google AI Overviews over 74 days (Dec 18, 2025 – Mar 1, 2026). 28 competitors tracked.

### Visibility score and trend

| Metric | Value |
|---|---|
| AI visibility score | **3.51 / 100** |
| Rank among 29 tracked brands | **17th** |
| Feb 2026 average | 3.09 (down 20.4% from Jan) |
| Latest 2-week avg (Feb 15–28) | 2.84 (continued decline) |

| Month | Avg Visibility | Change |
|-------|---------------|--------|
| Dec 2025 (18–31) | 3.59 | Baseline |
| Jan 2026 | 3.88 | +8.1% |
| Feb 2026 | 3.09 | -20.4% |

The January spike (peak 5.39 on Jan 6–7) likely correlates with Flodesk's AI-powered design announcement and CEO transition news. The signal was short-lived — visibility decayed back to baseline within two weeks and continued declining through February.

### Competitive AI visibility gap

| Rank | Brand | AI Visibility | Gap vs Flodesk | SEO Rank (organic traffic) |
|---:|---|---:|---|---:|
| 1 | Klaviyo | 61.74 | 17.6x higher | 6th |
| 2 | Omnisend | 53.70 | 15.3x higher | 16th |
| 3 | Brevo | 46.80 | 13.3x higher | 15th |
| 4 | Mailchimp | 45.31 | 12.9x higher | 4th |
| 5 | ActiveCampaign | 41.87 | 11.9x higher | 8th |
| 6 | MailerLite | 41.14 | 11.7x higher | 12th |
| 7 | HubSpot | 36.26 | 10.3x higher | 2nd |
| 8 | GetResponse | 23.39 | 6.7x higher | 18th |
| 9 | Moosend | 20.97 | 6.0x higher | 20th |
| 10 | Sender | 18.47 | 5.3x higher | 26th |
| 11 | Constant Contact | 17.48 | 5.0x higher | 5th |
| 12 | Kit | 11.87 | 3.4x higher | 9th |
| **17** | **Flodesk** | **3.51** | **—** | **13th** |

The revenue-visibility paradox: Flodesk's business position (top 10 by ARR, top 10 by customer count) dramatically outperforms its AI presence (17th). Buyers who research email marketing through AI will almost never encounter Flodesk on the shortlist.

Notable: Omnisend (16th in SEO) is 2nd in AI visibility. Sender (26th in SEO) is 10th. Moosend (20th in SEO) is 9th. These companies have cracked AI visibility through content strategy, not organic scale — proving AI visibility is a separate axis from SEO strength.

### Mentions and sentiment

| Metric | Flodesk | Tier 1 Avg | Gap |
|---|---|---|---|
| Total mentions (74 days) | 3,465 | 50,409 | 14.6x fewer |
| Average rank when mentioned | 9.5 | 4.8 | 2x worse position |
| Top 1–3 mentions | 188 (5.4%) | — | Rarely first choice |
| Positive sentiment | 86.5% | — | Zero negative mentions |

Sentiment is the bright spot. When AI engines mention Flodesk, the narrative is overwhelmingly positive (86.5%) with zero negative mentions. AI understands Flodesk's value prop — design quality, ease of use, flat-rate pricing — it just doesn't mention it often enough.

### Why Flodesk is invisible to AI

**Source gap.** Flodesk's domain is cited ~24 times over 73 days. Every major competitor domain is cited daily (73/73 days). Flodesk's homepage was cited once. Every competitor homepage is cited daily.

**Absent from the listicles that run the show.** ~40% of the top 300 URLs AI engines cite are "best email marketing" listicles. Moosend, Sender, Brevo, Omnisend, and Klaviyo all publish their own daily-cited listicles. Flodesk doesn't appear on them, and doesn't publish its own.

**No glossary or definition content.** Mailchimp and Campaign Monitor own the glossary layer with daily-cited definition pages ("What is email marketing?", "What is email automation?"). These pages literally define the terms AI uses to describe the category. Flodesk has nothing equivalent.

**Narrow content positioning.** The few flodesk.com URLs AI does cite are comparison/alternatives posts (e.g., `/tips/campaign-monitor-alternatives`). No product documentation, educational content, or category-defining thought leadership makes it into AI responses.

**Third-party presence gap.** G2, Reddit, emailtooltester, and TechRadar are cited by AI engines every single day. Flodesk's presence on these platforms is insufficient to influence AI recommendations.

### What's working in AI

- **Zero negative sentiment.** No AI engine characterizes Flodesk negatively.
- **86.5% positive mentions.** AI correctly understands the design-first value proposition and ease of use.
- **109 rank-1 mentions.** There are specific prompt angles — likely design-focused, creator-focused, or flat-rate queries — where Flodesk wins. These are the prompts to study and replicate.
- **Comparison content has traction.** The pages AI does cite are comparison-style posts. This content type works and can be scaled.

---

## 6. Summary & highest-leverage fixes

### What's working

- Branded search moat is strong and growing (+17.4%)
- The /tips/ programmatic play creates broad keyword coverage (14,256 keywords)
- Templates gallery has untapped SEO potential (121 keywords on one page)
- Organic efficiency is top-tier: 3rd in traffic/keyword, 1st in top-3 and top-10 keyword concentration
- Organic traffic ranks 13th of 32 competitors — ahead of Brevo, Omnisend, GetResponse, and several better-funded players
- AI sentiment is 86.5% positive with zero negative mentions

### What's broken

- Content traffic in freefall (-36.8% in 6 months, -8,579 visits/mo)
- Link base eroding (-1,524 referring domains)
- Half the index is low-value user-generated content (1,016 pages, 345 visits)
- Keyword trajectory is net-negative (-825), one of only two competitors losing ground
- Keyword breadth (24.8K) is half that of direct peers Kit (41K) and MailerLite (37K)
- AI visibility is 17th of 29, declining 20.4% month-over-month
- flodesk.com cited by AI engines only 13 of 73 tracked days (competitors: daily)
- Absent from the listicles, glossary pages, and review platforms that feed AI recommendations

### Highest-leverage fixes

**SEO:**

1. **Restructure /templates/ URLs** with descriptive slugs and category pages → unlock template search traffic from the most promising non-content section
2. **Noindex view.flodesk.com** or move to separate domain → recover crawl budget from 1,016 low-value pages
3. **Expand keyword footprint** — current content ranks well (19% in top 10), the gap vs. competitors is volume not quality; doubling keywords at current efficiency = top 10 organic traffic
4. **Investigate tips traffic collapse** — 39.6% decline across the entire /tips/ section suggests algorithmic or competitive shift, not isolated decay

**AI visibility:**

5. **Get on the daily-cited listicles** — audit the top 20 most-cited "best email marketing" roundups and pursue inclusion; this single content format drives ~40% of AI recommendations
6. **Build glossary and educational content** — create a `/glossary` or `/learn` hub defining email marketing, automation, newsletters; competitors' glossary pages are cited by AI engines daily
7. **Strengthen G2 and review platform presence** — G2, Capterra, and Reddit are cited every day by AI engines; review volume directly feeds AI recommendations
8. **Make the homepage AI-citeable** — every competitor homepage is cited daily by AI; Flodesk's was cited once; restructure for clear, extractable product information

> **Data pulled:** SEMRush (Feb 28, 2026), DataForSEO (Feb 28, 2026), CheckThat AI Visibility Index (Dec 18, 2025 – Mar 1, 2026, 201 prompts, 5 AI engines).

---

## Changes from v3

- Removed Lighthouse performance section and Core Web Vitals data
- Removed "traffic value per employee" efficiency metric
- Revised organic efficiency to focus on: traffic per content page, traffic per page, keywords per page, traffic per keyword, and top-3/top-10 keyword concentration
- Added AI visibility section synthesizing AEO audit report, source analysis, and competitive visibility data
- Consolidated data sources into a footnote in the summary section
- Reduced from 7 to 6 top-level sections

### Supporting files

- `competitive-landscape-v1.md` — Full 32-competitor analysis with business and SEMRush domain metrics
- `content-pages-detail.md` — All 467 content pages with organic traffic data
- `aeo/aeo-audit-report-v1.md` — Full AI visibility audit with recommendations
- `aeo/source-analysis-v1.md` — Domain and URL classification of AI-cited sources
- `aeo/competitive-visibility-dump-v1.md` — Complete competitive AI visibility rankings
- `competitors-raw/` — Raw SEMRush and DataForSEO API outputs
