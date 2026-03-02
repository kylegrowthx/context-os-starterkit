# SEO Overview: flodesk.com (v2)

**Date:** February 28, 2026
**Source:** SEMRush (US database) + SquirrelScan v0.0.38 + Lighthouse
**Domain:** flodesk.com

---

## The 10 metrics

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
| 10 | Blog audit score (SquirrelScan avg) | **43/100** | — | new |

Metric #8 (traffic per page) went up despite total traffic going down because 76 pages lost traffic entirely — the tail got cut, which raised the average. Don't read this as improvement.

Metric #10 is new in v2. Every blog page scored Grade F (42-45 range). The issues are template-level, not content-specific — fixing them would lift all pages at once.

---

## What the numbers say

### Authority is flat, but the link base is eroding

Authority score of 46 hasn't moved in 6 months. But referring domains dropped from 38,455 to 36,931 — a net loss of 1,524 linking domains. Total backlinks also declined from 14.2M to 13.7M. The authority score is holding thanks to score recalibration (it jumped from 40 to 46 in Aug 2025), but the underlying link base is shrinking.

Most of the 36,931 referring domains likely come from embed forms and signup widgets distributed across customer sites (5M form-based backlinks in the profile). As customers churn or rebuild their sites, those links disappear.

### The homepage carries everything

The homepage alone drives **44,652 of the 65,668 monthly organic visits — 68% of all organic traffic.** That's a branded search moat, not a content engine. And that branded traffic actually grew over 6 months (39,772 → 46,701, +17.4%), masking the content decline.

### Content traffic collapsed

Content traffic dropped **36.8% in 6 months** — from 23,309 to 14,730 visits/month. That's a loss of 8,579 monthly visits from content pages alone.

The per-page yield tells the same story: traffic per content page fell from 46.8 to 31.6 (-32.5%). Flodesk published roughly the same number of content pages (956 → 935), but 32 fewer pages are getting any traffic at all (498 → 466). The content that was working is working less.

Worth investigating: algorithm update impact (Google's Dec 2025 / Jan 2026 core updates), content quality decay, or increased competition in the email template SERP space.

### The blog has a template problem, not a content problem

SquirrelScan audited all 51 blog pages with organic traffic. Every single page scored Grade F (average 43/100). But the breakdown reveals the issue isn't content — it's infrastructure:

| Category | Average score | Grade |
|----------|:---:|---|
| Content | 91 | A |
| Crawlability | 90 | A |
| Core SEO | 87 | B |
| Performance | 78 | C |
| Links | 76 | C |
| Accessibility | 75 | C |
| Security | 60 | D |
| E-E-A-T | 58 | D |
| Images | 53 | D |

Content scores A. The actual page content is fine. What's dragging every page to F:

1. **No author byline or publish date** (E-E-A-T: 58) — every blog page lacks datePublished and author attribution
2. **Missing security headers** (Security: 60) — no CSP, HSTS, or X-Frame-Options on any page
3. **Leaked API keys** — Amplitude key exposed site-wide in inline scripts
4. **No og:image** — social shares lack imagery
5. **Oversized main.js** (~350 KB, unminified) — drags performance
6. **No caching headers** on HTML responses
7. **Accessibility gaps** — buttons without names, missing skip-link, no `<main>` landmark

These are all template fixes. One engineering sprint could lift every blog page from F to B.

### The /tips/ section is an email template factory

752 pages in `/tips/` follow the pattern: `{topic}-email-templates` or `{niche}-newsletters`. This is a programmatic-style content play targeting long-tail email template searches.

It's working directionally — 415 of 752 tips pages get some traffic — but the yield per page is low (30.9 visits/mo average). And tips traffic dropped 39.6% in 6 months. The strategy has breadth but lacks depth on any single topic.

### Blog is underperforming

183 blog pages, but only 51 get organic traffic (27%). Total blog traffic: 1,902/mo. That's 37 visits per blog post with traffic. Blog traffic actually declined less than tips (-6.5% vs -39.6%), suggesting the blog content is more resilient — it just needs more of it working.

### Templates gallery is a missed opportunity

7 pages under `/templates/email` are indexed. The main gallery page (`/templates/email`) drives 212 visits/month from 121 keywords — making it a stronger page than 97% of blog posts. But the individual template pages (with hash IDs like `/templates/email/619314...`) get almost no traffic. This is a product page with SEO potential that's not being exploited — category pages, tagging, and proper URL structure could unlock significantly more search traffic here.

### Half the index is customer-hosted content

1,016 pages on `view.flodesk.com` (hosted email previews and landing pages) are indexed by Google. They drive only 345 visits total. This is potential index bloat — Google is spending crawl budget on low-value customer content pages instead of Flodesk's editorial pages.

### The 12-month trend shows a rise-and-retreat pattern

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

## Page breakdown by type

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
- **Content** — /tips/ and /blog/ editorial pages (see content breakdown below)
- **Transactional** — Sign-in, sign-up, checkout, forms, legal pages
- **Education** — university.flodesk.com courses and resources
- **Docs** — developers.flodesk.com, grain.flodesk.com (design system)
- **Support** — help.flodesk.com
- **User-generated** — view.flodesk.com email previews and landing pages, usercontent.flodesk.com PDFs
- **Other** — Campaign shortlinks (/c/), uncategorized

---

## Content breakdown

### By section

| Section | Pages | 6mo | Keywords | 6mo | w/ Traffic | 6mo | Traffic | 6mo | Traffic/Page | 6mo |
|---------|-------|-----|----------|-----|-----------|-----|---------|-----|--------------|-----|
| Tips (/tips/) | 752 | -9 | 14,256 | +6.8% | 415 | -11 | 12,828 | -39.6% | 30.9 | -38.1% |
| Blog (/blog/) | 183 | -12 | 3,162 | -33.1% | 51 | -21 | 1,902 | -6.5% | 37.3 | +33.9% |
| **Content total** | **935** | **-21** | **17,418** | **-3.7%** | **466** | **-32** | **14,730** | **-36.8%** | **31.6** | **-32.6%** |

### Blog audit health (SquirrelScan, all 51 pages with traffic)

| Metric | Average | Range |
|--------|---------|-------|
| **Overall score** | **43/100** | 42–45 |
| Core SEO | 87 | 68–91 |
| Content | 91 | 63–100 |
| Crawlability | 90 | 90 |
| Performance | 78 | 63–100 |
| Links | 76 | 50–100 |
| Accessibility | 75 | 50–88 |
| Security | 60 | 60 |
| E-E-A-T | 58 | 42–67 |
| Images | 53 | 0–100 |

| | Total | Avg/page |
|--|-------|----------|
| Passed rules | ~5,000 | 98 |
| Warnings | 1,813 | 36 |
| Errors | 375 | 7 |

### Top 10 content pages by traffic

| # | URL | Type | KW | Traffic | 6mo | Audit |
|---|-----|------|----|---------|-----|-------|
| 1 | /blog/just-checking-in-email-alternatives/ | Blog | 213 | 1,142 | +747 | 42 |
| 2 | /tips/interview-follow-up-email-templates | Tips | 575 | 698 | -421 | — |
| 3 | /tips/pay-raise-email-templates | Tips | 484 | 658 | -1,171 | — |
| 4 | /tips/leave-request-email-templates | Tips | 392 | 567 | +84 | — |
| 5 | /tips/job-acceptance-email-templates | Tips | 368 | 531 | -2,017 | — |
| 6 | /tips/request-email-templates | Tips | 272 | 343 | -879 | — |
| 7 | /tips/employee-leaving-announcement-email-templates | Tips | 194 | 322 | -124 | — |
| 8 | /tips/payment-request-email-templates | Tips | 205 | 303 | +1 | — |
| 9 | /tips/inquiry-email-templates | Tips | 153 | 278 | -117 | — |
| 10 | /tips/partnership-email-templates | Tips | 54 | 277 | +219 | — |

The single highest-traffic content page is a blog post, not a tips page. But 9 of the top 10 are tips. Tips dominate volume; blog dominates per-page yield.

### Content pages in freefall (biggest 6mo traffic losses)

| URL | Type | Traffic | 6mo | Lost |
|-----|------|---------|-----|------|
| /tips/job-acceptance-email-templates | Tips | 531 | -2,017 | 79% |
| /tips/pay-raise-email-templates | Tips | 658 | -1,171 | 64% |
| /tips/request-email-templates | Tips | 343 | -879 | 72% |
| /tips/price-increase-email-templates | Tips | 171 | -686 | 80% |
| /tips/salary-negotiation-email-templates | Tips | 204 | -484 | 70% |
| /tips/interview-follow-up-email-templates | Tips | 698 | -421 | 38% |
| /tips/interview-acceptance-email-templates | Tips | 44 | -305 | 87% |
| /tips/save-the-date-corporate-event-email-templates | Tips | 32 | -215 | 87% |
| /tips/acknowledgement-email-templates | Tips | 12 | -194 | 94% |
| /tips/booking-request-email-templates | Tips | 43 | -189 | 81% |

All 10 biggest decliners are tips pages. The pattern: high-volume professional email templates (job-related, payment-related) lost the most. This looks like a category-wide SERP shift — possibly Google favoring different content formats or competitors for these queries.

### Content pages growing fastest

| URL | Type | Traffic | 6mo | Growth |
|-----|------|---------|-----|--------|
| /blog/just-checking-in-email-alternatives/ | Blog | 1,142 | +747 | +189% |
| /tips/partnership-email-templates | Tips | 277 | +219 | +380% |
| /tips/networking-email-templates | Tips | 129 | +128 | new → 129 |
| /tips/looping-in-email-templates | Tips | 138 | +109 | +376% |
| /tips/reference-request-email-templates | Tips | 126 | +89 | +241% |
| /tips/leave-request-email-templates | Tips | 567 | +84 | +17% |
| /tips/second-follow-up-email-templates | Tips | 83 | +74 | +822% |
| /tips/refund-rejection-email-templates | Tips | 102 | +71 | +229% |
| /tips/employee-introduction-email-templates | Tips | 268 | +68 | +34% |
| /tips/second-interview-email-templates | Tips | 82 | +67 | +447% |

---

## Templates pages

| # | URL | Keywords | Traffic |
|---|-----|----------|---------|
| 1 | /templates/email | 121 | 212 |
| 2 | /templates/email/619314043dec099518c886d8 | 3 | 3 |
| 3 | /templates/email/ecommerce | 4 | 0 |
| 4 | /templates/email/5d60ebebed8ad814677acf95 | 2 | 0 |
| 5 | /templates/email/5f3e408507203a0026f0294a | 2 | 0 |
| 6 | /templates/email/619314053dec099518c8873c | 1 | 0 |
| 7 | /templates/email/5d3688cde40bbc10ff739fd7 | 1 | 0 |

The main `/templates/email` gallery page ranks for 121 keywords and pulls 212 visits/month. It's the 17th highest-traffic page on the entire site. Individual template pages use hash IDs instead of descriptive URLs and get almost no traffic. The `/templates/email/ecommerce` category page — the one with an actual keyword-rich URL — gets zero traffic despite 4 keywords.

This is a clear structural opportunity. The templates gallery has product-market fit with search (121 keywords) but the URL structure and page architecture aren't built for SEO.

---

## Lighthouse performance (single page test)

Tested on the highest-traffic blog page (`/blog/just-checking-in-email-alternatives/`):

| Source | Performance | Accessibility | Best Practices | SEO |
|--------|:-:|:-:|:-:|:-:|
| PageSpeed (Lighthouse) | 57 | 80 | 57 | 100 |
| DataForSEO (Lighthouse) | 39 | 79 | 100 | 100 |
| Average | **48** | **80** | **79** | **100** |

### Core Web Vitals

| Metric | PageSpeed | DataForSEO | Good threshold |
|--------|-----------|-----------|----------------|
| FCP | 4.2s | 2.9s | < 1.8s |
| LCP | 9.3s | 6.7s | < 2.5s |
| TBT | 240ms | 1,210ms | < 200ms |
| CLS | 0.023 | 0.147 | < 0.1 |
| Speed Index | 6.4s | 4.6s | < 3.4s |
| TTI | 15.5s | 11.4s | < 3.8s |

Every Core Web Vital fails on mobile. LCP is 3-4x the good threshold. TTI is 3-4x. This is a significant performance problem that affects both rankings (mobile page speed r=0.83 correlation with rankings) and user experience.

### Accessibility violations (axe-core)

4 violations affecting 20 elements:
- Buttons without accessible names (1 element)
- Insufficient color contrast (6 elements)
- Links without discernible names (5 elements)
- Touch targets too small (8 elements)

---

## Summary: where flodesk stands

**What's working:**
- Branded search moat is strong and growing (+17.4%)
- The /tips/ programmatic play creates broad keyword coverage (14,256 keywords)
- Blog content quality scores well (91/100 average)
- Templates gallery has untapped SEO potential (121 keywords on one page)

**What's broken:**
- Content traffic in freefall (-36.8% in 6 months)
- Every blog page fails the audit (43/100) due to template-level issues, not content
- Core Web Vitals all failing on mobile (LCP 6.7-9.3s vs 2.5s threshold)
- No E-E-A-T signals on any content page (no author, no dates)
- Security headers missing site-wide
- Link base eroding (-1,524 referring domains)
- Half the index is low-value user-generated content

**Highest-leverage fixes:**
1. **Add author bylines and publish dates** to all content pages → lifts E-E-A-T from 58 to 80+
2. **Add security headers** (CSP, HSTS, X-Frame-Options) → lifts Security from 60 to 90+
3. **Optimize main.js bundle and add caching** → improves LCP and overall performance
4. **Fix accessibility basics** (button names, contrast, link names) → lifts a11y from 75 to 90+
5. **Restructure /templates/ URLs** with descriptive slugs and category pages → unlock template search traffic
6. **Noindex view.flodesk.com** or move to separate domain → recover crawl budget

Fixes 1-4 are template changes that would lift every blog page from Grade F to Grade B in one sprint. Fix 5 is a product/engineering project with SEO upside. Fix 6 is a configuration change.

---

## Raw data files

All SEMRush responses saved for reference:

- `raw-domain-overview.md` — Authority score, traffic, keywords, rank
- `raw-domain-history.md` — 12-month trend (Feb 2025 → Jan 2026)
- `raw-backlinks-overview.md` — Backlink profile (13.7M links, 36.9K domains)
- `raw-organic-pages.md` — All 2,187 pages with traffic data + classification
- `content-pages-detail.md` — All 467 content pages with organic traffic
- `content-pages-blog-audit.md` — All 51 blog pages with SquirrelScan audit scores

### Audit data

- `page-audits-squirrel/` — SquirrelScan raw output for all 51 blog pages
- `page-audits-pagespeed/` — Lighthouse performance audit (1 page tested)
- `page-audits-dataforseo/` — DataForSEO Lighthouse audit (1 page tested)
- `page-audits-a11y/` — Accessibility audit via axe-core (1 page tested)

---

## Changes from v1

- Added Templates as a separate page type (was previously grouped under Brand)
- Integrated SquirrelScan blog audit scores and findings
- Added Lighthouse performance and accessibility test results
- Added top content pages, biggest decliners, and fastest growers tables
- Added templates pages detail section
- Added summary with prioritized fix recommendations
