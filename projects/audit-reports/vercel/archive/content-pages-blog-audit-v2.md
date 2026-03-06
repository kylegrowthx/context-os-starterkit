# Blog Content Pages Audit — vercel.com (v2)

**Date:** February 28, 2026
**Source:** SEMRush (US database, full organic pull) + PageSpeed Insights + On-Page SEO Audit
**Scope:** All blog pages — 379 indexed, 25 with organic traffic, 354 dead
**Total blog organic traffic:** 3,450/mo (2.1% of domain total)
**Total blog pages in index:** 437 (379 current + 58 lost from index since Aug 2025)

---

## Blog index health

| Metric | Value |
|--------|-------|
| Total blog pages (current index) | 379 |
| Pages with organic traffic | 25 (6.6%) |
| Pages with zero traffic | 354 (93.4%) |
| Pages lost from index (had traffic in Aug 2025) | 19 |
| Pages dropped from index entirely | 58 |
| Total blog keyword-URL pairs | 4,912 |
| Blog traffic share of domain | 2.1% |
| Blog traffic 6mo change | +63.5% |

**93.4% of blog pages generate zero organic traffic.** This is the single most important finding from the full data pull. v1 reported 51 blog pages — that was only the pages visible in the top-1,000 keyword-URL pairs. The actual blog index is 7.4x larger (379 pages) and overwhelmingly dead.

The 354 dead pages represent years of product announcements, case studies, and feature posts that have aged out of search relevance. They consume crawl budget and may dilute the blog's topical authority signal.

---

## Audit score summary

Scores from Lighthouse (mobile) and on-page SEO analysis on the top 6 blog pages:

| Metric | Average | Range | Notes |
|--------|---------|-------|-------|
| **Performance** | **57/100** | 51–65 | Grade C across the board — heavy JS |
| **Accessibility** | **88/100** | 88 | Consistent template score |
| **Best Practices** | **97/100** | 96–100 | Strong |
| **SEO (Lighthouse)** | **100/100** | 100 | Perfect Lighthouse SEO score |
| **Image Alt Coverage** | **49%** | 13–91% | Wide variance, many posts missing alt text |
| **Security Headers** | **14%** | 1/7 | Only HSTS present, 6 headers missing |

| | Total (6 audited pages) | Per page avg |
|--|-------------------------|-------------|
| Opportunities flagged | 12 | 2 |
| Image alt issues | 23 of 51 images | 3.8/page |

---

## Site-wide issues (affect all blog pages)

These are template and infrastructure issues — fixing them lifts every page:

1. **Massive unused JavaScript** (Performance) — every blog page ships ~2.9s worth of unused JS on mobile. The primary bundle blocks interactivity until 15–19s. This is the #1 performance bottleneck.

2. **Unused CSS** (Performance) — 0.5–0.8s of unused CSS on every page. Combined with JS bloat, this pushes LCP to 7–14s on mobile.

3. **Missing security headers** (Security) — only HSTS is present. Missing: CSP, X-Content-Type-Options, X-Frame-Options, X-XSS-Protection, Referrer-Policy, Permissions-Policy. Score: 1/7 headers (14%).

4. **Poor image alt text coverage** (Images/A11y) — averaging 49% alt coverage across audited pages. One post had only 13% (13 of 15 images missing alt text). This hurts both accessibility and image SEO.

5. **Footer navigation inflates heading count** (Content) — every blog post has 11+ H2s from the site-wide footer nav (Get Started, Build, Scale, Secure, Resources, etc.). This dilutes heading structure for content-specific headings.

6. **LCP consistently above 6s** (Performance) — Largest Contentful Paint ranges from 6.9s to 14.0s on mobile. Google's "good" threshold is 2.5s. Every blog page fails Core Web Vitals for LCP.

7. **TBT consistently above 200ms** (Performance) — Total Blocking Time ranges from 290ms to 740ms. Google's "good" threshold is 200ms. Main thread is blocked by JS execution.

8. **93% blog index bloat** (SEO) — 354 pages with zero organic traffic remain indexed, consuming crawl budget and diluting topical signals. This is a structural SEO issue not visible in page-level audits.

---

## Audited blog pages

| # | URL | KW | 6mo KW | Traffic | 6mo | Aug | Perf | A11y | BP | SEO | Alt% | Words |
|---|-----|-----|--------|---------|-----|-----|------|------|-----|-----|------|-------|
| 1 | /blog/introducing-the-new-v0 | 44 | new | 976 | new | 0 | 51 | 88 | 96 | 100 | 13% | 1,133 |
| 2 | /blog/v0-app | 143 | +17 | 656 | +148 | 508 | 57 | 88 | 96 | 100 | 67% | 735 |
| 3 | /blog/introducing-chat-sdk | 43 | +13 | 303 | +201 | 102 | 55 | 88 | 96 | 100 | 25% | 666 |
| 4 | /blog/series-f | 18 | new | 202 | new | 0 | 65 | 88 | 96 | 100 | 91% | 1,225 |
| 5 | /blog/turbopack | 23 | +10 | 219 | +168 | 51 | 56 | 88 | 100 | 100 | — | — |
| 6 | /blog/how-were-adapting-seo-for-llms-and-ai-search | 56 | +34 | 50 | -14 | 64 | 61 | 88 | 100 | 100 | — | — |

### Core Web Vitals detail

| Page | FCP | LCP | TBT | CLS | Speed Index | TTI |
|------|-----|-----|-----|-----|-------------|-----|
| introducing-the-new-v0 | 2.3s | **11.0s** | **690ms** | 0.001 | 5.3s | 15.8s |
| v0-app | 1.8s | **10.7s** | **580ms** | 0.001 | 4.0s | 15.4s |
| introducing-chat-sdk | 2.9s | **14.0s** | **410ms** | 0.001 | 5.6s | 19.1s |
| series-f | 2.3s | **9.6s** | **290ms** | 0.001 | 3.8s | 15.6s |
| turbopack | 1.7s | **6.9s** | **740ms** | 0.006 | 4.0s | 16.0s |
| seo-for-llms | 2.0s | **10.9s** | **410ms** | 0.001 | 4.6s | 15.1s |

Every page fails Google's LCP threshold (2.5s). TBT consistently exceeds the 200ms "good" target.

### On-Page SEO detail

| Page | H1 | H2s (content) | Word Count | Internal Links | External Links | KW in Title | KW in H1 | KW in Meta |
|------|-----|---------------|-----------|----------------|----------------|-------------|-----------|-----------|
| introducing-the-new-v0 | Introducing the new v0 | 4 | 1,133 | 129 | 23 | Yes | Yes | Yes |
| v0-app | v0.dev -> v0.app | 2 | 735 | 125 | 24 | Yes | Yes | Yes |
| introducing-chat-sdk | Introducing Chatbot Template | 0 | 666 | 122 | 37 | **No** | **No** | **No** |
| series-f | Towards the AI Cloud: Our Series F | 3 | 1,225 | 126 | 31 | **No** | **No** | **No** |

The Chat SDK post ranks #1 for "chat sdk" but titles itself "Introducing Chatbot Template" — a keyword mismatch. The Series F post similarly doesn't target "vercel funding" in its on-page elements.

---

## Security headers detail

Verified against `https://vercel.com/blog/introducing-the-new-v0` (representative of all blog pages):

| Header | Present | Value |
|--------|---------|-------|
| Strict-Transport-Security | Yes | max-age=63072000; includeSubDomains; preload |
| Content-Security-Policy | **No** | — |
| X-Content-Type-Options | **No** | — |
| X-Frame-Options | **No** | — |
| X-XSS-Protection | **No** | — |
| Referrer-Policy | **No** | — |
| Permissions-Policy | **No** | — |

**Score: 1/7 (14%)**

HSTS configuration is excellent (2-year max-age with preload). But 6 security headers are missing.

---

## Recommendations (prioritized by impact)

1. **Noindex dead blog pages.** 354 blog posts generate zero organic traffic. Add `noindex` to pages that haven't had traffic for 6+ months to reduce index bloat by ~7.5% of the entire domain index. Alternatively, redirect or consolidate thin posts into comprehensive hub pages.

2. **Reduce JS bundle size.** 2.9s of unused JavaScript on every page. Tree-shake the blog template, defer non-critical scripts, and consider route-based code splitting.

3. **Fix LCP.** 7–14s LCP is catastrophic for mobile. Prioritize static rendering of above-the-fold content and preload critical assets.

4. **Add missing security headers.** CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, and Permissions-Policy. One-time infrastructure changes.

5. **Fix image alt text.** Averaging 49% coverage. Set a policy requiring descriptive alt text before publishing.

6. **Clean up footer heading pollution.** Switch footer navigation H2 tags to non-heading elements.

7. **Align title/H1 with ranking keywords.** Chat SDK and Series F posts have keyword-title mismatches.

8. **Implement content refresh cadence.** The 19 pages that lost all traffic include valuable topics (MCP explainer, React 19, React Server Components). Update and re-optimize rather than letting them decay.

---

## Score definitions

| Score | Grade | Meaning |
|-------|-------|---------|
| 90–100 | A | Excellent — minor polish only |
| 80–89 | B | Good — few issues to address |
| 70–79 | C | Fair — moderate fixes needed |
| 50–69 | D | Poor — significant issues |
| 0–49 | F | Critical — major fixes required |

## Category definitions

| Category | What it measures | Tool |
|----------|-----------------|------|
| Performance | Lighthouse scores, CWV, load time | PageSpeed Insights (mobile) |
| Accessibility | WCAG compliance, a11y score | PageSpeed Insights |
| Best Practices | HTTPS, no console errors, CSP | PageSpeed Insights |
| SEO (Lighthouse) | Meta tags, crawlability, mobile-friendly | PageSpeed Insights |
| Image Alt Coverage | % of images with alt text | On-Page SEO Audit |
| Security Headers | HSTS, CSP, X-Frame-Options, etc. | Security Headers Audit |
| Content | Word count, heading structure, readability | On-Page SEO Audit |

---

*Audits run March 2026 via PageSpeed Insights API (mobile strategy) and on-page SEO analysis. Security headers checked via HTTP response inspection. Blog index data from full SEMRush organic pull (74,542 keyword-URL pairs). v2 supersedes v1 — primary change is inclusion of full blog index health data (379 pages vs v1's 51 visible pages).*
