# Blog Content Pages Audit — flodesk.com

**Date:** February 28, 2026
**Source:** SEMRush (US database) + SquirrelScan v0.0.38
**Scope:** All 51 blog pages with organic traffic
**Total organic traffic:** 1,902/mo

---

## Audit score summary

Every blog page scored Grade F. The issues are template-level, not content-specific.

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

---

## Site-wide issues (affect all/most blog pages)

These are template and infrastructure issues — fixing them would lift every page's score:

1. **No author byline or publish date** (E-E-A-T) — every blog page lacks datePublished and author attribution
2. **Missing security headers** — no CSP, HSTS, or X-Frame-Options on any page
3. **Leaked API keys in inline scripts** — Amplitude key exposed site-wide
4. **Broken/duplicate social share buttons** — HTTP links returning 500/520 errors, duplicate share widgets with malformed URLs
5. **No og:image on most pages** — social shares lack imagery
6. **Oversized main.js bundle** (~350 KB, unminified)
7. **No caching headers** on HTML responses
8. **Accessibility gaps** — buttons without names, missing skip-link, no `<main>` landmark, heading hierarchy skips
9. **Sitemap validation errors** — standard sitemap paths return invalid format

---

## All blog pages with audit scores

| # | URL | KW | 6mo KW | Traffic | 6mo | Aug | Score | SEO | Content | Perf | Images | Links | A11y | Sec | EEAT | Warn | Err |
|---|-----|-----|--------|---------|-----|-----|-------|-----|---------|------|--------|-------|------|-----|------|------|-----|
| 1 | /blog/just-checking-in-email-alternatives/ | 213 | +48 | 1142 | +747 | 395 | **42** | 82 | 91 | 72 | 45 | 75 | 75 | 60 | 58 | 37 | 8 |
| 2 | /blog/thank-you-for-your-purchase-email/ | 94 | -29 | 161 | -159 | 320 | **43** | 91 | 91 | 72 | 51 | 74 | 75 | 60 | 58 | 37 | 8 |
| 3 | /blog/landing-page/ | 7 | -7 | 128 | +40 | 88 | **44** | 68 | 63 | 88 | 93 | 88 | 75 | 60 | 53 | 34 | 5 |
| 4 | /blog/how-to-sell-on-pinterest/ | 28 | +9 | 60 | new | 0 | **43** | 91 | 91 | 75 | 57 | 75 | 75 | 60 | 58 | 38 | 6 |
| 5 | /blog/small-business-thank-you-message/ | 370 | -171 | 49 | -172 | 221 | **43** | 91 | 91 | 71 | 57 | 75 | 75 | 60 | 58 | 39 | 6 |
| 6 | /blog/newsletter-subject-lines/ | 34 | -42 | 33 | -88 | 121 | **43** | 91 | 91 | 75 | 57 | 75 | 75 | 60 | 58 | 38 | 6 |
| 7 | /blog/email-subject-lines-for-events/ | 42 | -5 | 32 | -1 | 33 | **43** | 91 | 91 | 79 | 47 | 75 | 75 | 60 | 58 | 34 | 8 |
| 8 | /blog/welcome-email-subject-lines/ | 7 | -9 | 29 | +23 | 6 | **43** | 91 | 91 | 79 | 47 | 75 | 75 | 60 | 61 | 34 | 8 |
| 9 | /blog/author/jordyn-e-kerr/ | 6 | +3 | 26 | +25 | 1 | **43** | 79 | 84 | 73 | 66 | 75 | 76 | 60 | 58 | 35 | 8 |
| 10 | /blog/newsletter-introduction-examples/ | 25 | -8 | 25 | -137 | 162 | **43** | 84 | 100 | 79 | 47 | 75 | 75 | 60 | 58 | 34 | 8 |
| 11 | /blog/newsletter-header/ | 21 | -11 | 22 | +4 | 18 | **43** | 84 | 91 | 75 | 47 | 75 | 75 | 60 | 58 | 36 | 8 |
| 12 | /blog/how-to-build-an-email-list/ | 46 | -65 | 19 | +18 | 1 | **43** | 91 | 91 | 79 | 47 | 75 | 78 | 60 | 51 | 37 | 8 |
| 13 | /blog/link-in-bio-examples/ | 51 | -31 | 16 | -28 | 44 | **44** | 91 | 91 | 79 | 69 | 75 | 75 | 60 | 58 | 34 | 7 |
| 14 | /blog/spring-newsletter-ideas/ | 7 | -11 | 15 | +4 | 11 | **43** | 91 | 91 | 79 | 47 | 75 | 75 | 60 | 58 | 34 | 8 |
| 15 | /blog/win-back-email/ | 24 | +1 | 14 | -13 | 27 | **43** | 91 | 91 | 72 | 51 | 75 | 75 | 60 | 58 | 37 | 8 |
| 16 | /blog/email-marketing-for-photographers/ | 5 | -1 | 13 | +9 | 4 | **43** | 75 | 91 | 79 | 47 | 75 | 75 | 60 | 58 | 36 | 8 |
| 17 | /blog/compelling-abandoned-cart-email-subject-lines-tips/ | 18 | +1 | 12 | -22 | 34 | **43** | 100 | 91 | 72 | 48 | 75 | 75 | 60 | 58 | 36 | 8 |
| 18 | /blog/best-email-sign-off/ | 141 | -194 | 11 | -23 | 34 | **43** | 84 | 91 | 77 | 54 | 75 | 75 | 60 | 58 | 38 | 6 |
| 19 | /blog/add-multiple-links-to-instagram-bio/ | 79 | -52 | 9 | -17 | 26 | **44** | 91 | 91 | 84 | 47 | 75 | 75 | 60 | 58 | 34 | 7 |
| 20 | /blog/meet-elliot-ulm-graphic-design-content-creator-and-really-cool-guy/ | 6 | -4 | 8 | +3 | 5 | **43** | 91 | 100 | 77 | 48 | 75 | 74 | 60 | 58 | 40 | 7 |
| 21 | /blog/newsletter-footer/ | 3 | -1 | 7 | new | 0 | **43** | 82 | 91 | 79 | 47 | 75 | 75 | 60 | 58 | 35 | 8 |
| 22 | /blog/instagram-bio-for-small-business/ | 111 | -27 | 7 | -2 | 9 | **43** | 82 | 91 | 79 | 47 | 75 | 75 | 60 | 58 | 35 | 8 |
| 23 | /blog/website-pop-up-examples/ | 64 | +2 | 6 | -14 | 20 | **44** | 91 | 100 | 79 | 47 | 75 | 75 | 60 | 58 | 33 | 8 |
| 24 | /blog/nonprofit-newsletter/ | 24 | -8 | 5 | -8 | 13 | **43** | 91 | 91 | 72 | 51 | 75 | 75 | 60 | 58 | 37 | 8 |
| 25 | /blog/how-to-format-a-newsletter/ | 41 | -15 | 5 | -13 | 18 | **42** | 82 | 91 | 72 | 51 | 75 | 75 | 60 | 58 | 38 | 8 |
| 26 | /blog/product-launch-email-template/ | 5 | +0 | 3 | new | 0 | **43** | 91 | 91 | 75 | 47 | 75 | 75 | 60 | 58 | 35 | 8 |
| 27 | /blog/newsletter-signup-examples/ | 32 | -49 | 3 | -12 | 15 | **43** | 91 | 91 | 75 | 47 | 75 | 75 | 60 | 58 | 35 | 8 |
| 28 | /blog/marketing-tools/alternatives-comparison/ | 1 | -1 | 3 | -6 | 9 | **45** | 76 | 63 | 88 | 93 | 88 | 75 | 60 | 53 | 33 | 5 |
| 29 | /blog/how-to-measure-welcome-email-effectiveness/ | 1 | new | 3 | new | 0 | **43** | 82 | 91 | 79 | 47 | 75 | 75 | 60 | 58 | 35 | 8 |
| 30 | /blog/flodesk-templates/ | 7 | -4 | 3 | -6 | 9 | **43** | 68 | 68 | 81 | 69 | 88 | 75 | 60 | 53 | 34 | 7 |
| 31 | /blog/email-template-builders/ | 16 | -13 | 3 | -1 | 4 | **43** | 91 | 91 | 79 | 47 | 75 | 75 | 60 | 58 | 34 | 8 |
| 32 | /blog/ecommerce-newsletter-examples/ | 9 | +3 | 3 | new | 0 | **43** | 84 | 100 | 79 | 54 | 75 | 75 | 60 | 58 | 34 | 7 |
| 33 | /blog/travel-newsletter-examples/ | 7 | -2 | 2 | +1 | 1 | **43** | 84 | 100 | 79 | 47 | 75 | 75 | 60 | 58 | 34 | 8 |
| 34 | /blog/sale-page-templates/ | 46 | -5 | 2 | -39 | 41 | **43** | 82 | 100 | 76 | 42 | 75 | 75 | 60 | 58 | 35 | 8 |
| 35 | /blog/newsletter-layout-design-ideas/ | 57 | -15 | 2 | -6 | 8 | **43** | 75 | 91 | 79 | 47 | 75 | 75 | 60 | 58 | 36 | 8 |
| 36 | /blog/newsletter-examples/ | 118 | -6 | 2 | -5 | 7 | **43** | 84 | 91 | 76 | 57 | 75 | 75 | 60 | 58 | 37 | 7 |
| 37 | /blog/lead-magnet-ideas-for-photographers/ | 6 | +3 | 2 | new | 0 | **43** | 82 | 91 | 79 | 47 | 75 | 75 | 60 | 61 | 35 | 8 |
| 38 | /blog/how-to-price-digital-downloads/ | 7 | +2 | 2 | new | 0 | **44** | 91 | 91 | 83 | 54 | 75 | 75 | 60 | 58 | 35 | 6 |
| 39 | /blog/clickfunnels-alternatives/ | 24 | -27 | 2 | -13 | 15 | **43** | 91 | 100 | 64 | 57 | 75 | 77 | 60 | 58 | 37 | 8 |
| 40 | /blog/best-time-to-send-newsletter/ | 14 | -16 | 2 | new | 0 | **43** | 91 | 91 | 75 | 54 | 75 | 75 | 60 | 61 | 38 | 6 |
| 41 | /blog/upsell-emails/ | 4 | +3 | 1 | new | 0 | **43** | 91 | 91 | 79 | 47 | 75 | 75 | 60 | 58 | 34 | 8 |
| 42 | /blog/sendinblue-alternatives/ | 6 | +0 | 1 | new | 0 | **43** | 91 | 100 | 75 | 54 | 75 | 75 | 60 | 58 | 34 | 7 |
| 43 | /blog/sales-funnel-builders/ | 62 | -19 | 1 | -1 | 2 | **44** | 84 | 100 | 83 | 54 | 75 | 75 | 60 | 58 | 35 | 6 |
| 44 | /blog/re-engagement-email-subject-lines/ | 8 | +0 | 1 | new | 0 | **43** | 91 | 91 | 79 | 47 | 75 | 75 | 60 | 58 | 34 | 8 |
| 45 | /blog/must-have-flodesk-email-templates-from-our-members/ | 11 | -7 | 1 | -2 | 3 | **44** | 92 | 91 | 77 | 66 | 75 | 75 | 60 | 58 | 34 | 7 |
| 46 | /blog/how-to-write-a-newsletter/ | 23 | -23 | 1 | new | 0 | **44** | 91 | 91 | 83 | 47 | 75 | 75 | 60 | 58 | 35 | 7 |
| 47 | /blog/how-to-create-waitlist/ | 16 | -12 | 1 | -1 | 2 | **44** | 91 | 91 | 83 | 47 | 75 | 75 | 60 | 58 | 35 | 7 |
| 48 | /blog/flodesk-integrations-youll-love/ | 7 | new | 1 | new | 0 | **43** | 82 | 91 | 86 | 54 | 75 | 76 | 60 | 58 | 37 | 6 |
| 49 | /blog/event-invitation-email/ | 33 | -32 | 1 | new | 0 | **43** | 91 | 91 | 79 | 47 | 75 | 76 | 60 | 58 | 36 | 8 |
| 50 | /blog/7-ways-to-create-a-memorable-email-newsletter-sign-off/ | 7 | +0 | 1 | -6 | 7 | **43** | 82 | 91 | 79 | 47 | 75 | 75 | 60 | 58 | 35 | 8 |
| 51 | /blog/2023-5-day-growth-challenge-honing-your-energetic-mindset-to-achieve-big-goals/ | 4 | +2 | 1 | +0 | 1 | **43** | 91 | 91 | 84 | 47 | 75 | 76 | 60 | 58 | 37 | 7 |

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

| Category | What it measures |
|----------|-----------------|
| Core SEO | Meta titles, descriptions, canonical URLs, Open Graph |
| Content | Heading structure, content quality, word count |
| Performance | Page weight, JS size, caching, CLS, LCP |
| Images | Alt text, file size, dimensions, next-gen formats |
| Links | Broken links, HTTPS downgrades, anchor text quality |
| Accessibility | ARIA labels, color contrast, landmarks, skip links |
| Security | Headers (CSP, HSTS), leaked secrets, noopener |
| E-E-A-T | Author bylines, dates, about/contact pages |
| Crawlability | Sitemaps, canonical chains, robots.txt |

**Raw audit data:** `page-audits-squirrel/raw-{slug}.txt` for each page
