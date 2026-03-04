# Page Audit: "Just Checking In" Email Alternatives

**URL:** https://flodesk.com/blog/just-checking-in-email-alternatives/
**Date:** February 28, 2026
**Tool:** SquirrelScan v0.0.38 (surface scan, 1 page)
**Audit ID:** 7571d73a

---

## Overall Score: 42/100 (Grade F)

| Category | Score |
|----------|-------|
| Analytics | 100 |
| Internationalization | 100 |
| Legal Compliance | 100 |
| Mobile | 100 |
| Structured Data | 100 |
| Social Media | 100 |
| URL Structure | 100 |
| Content | 91 |
| Crawlability | 90 |
| Core SEO | 82 |
| Accessibility | 75 |
| Links | 75 |
| Performance | 72 |
| Security | 60 |
| E-E-A-T | 58 |
| Images | 45 |

**Summary:** 98 passed, 37 warnings, 8 errors

---

## Critical Issues (Errors)

### 1. Sitemap validation failures
**Rule:** `crawl/sitemap-valid` | [Docs](https://docs.squirrelscan.com/rules/crawl/sitemap-valid)

8 sitemaps return "Unknown sitemap format" errors. Standard paths (/sitemap.xml, /sitemap_index.xml, etc.) are all failing — the site likely serves a non-standard or JavaScript-rendered sitemap.

### 2. Oversized JavaScript bundle
**Rule:** `perf/js-file-size` | [Docs](https://docs.squirrelscan.com/rules/perf/js-file-size)

`main.js` is 351.7 KB (limit: 250 KB). Appears unminified with 12 comments and ~229.7 KB potential savings.

### 3. Accessibility: buttons without names
**Rule:** `a11y/button-name`, `a11y/aria-labels` | [Docs](https://docs.squirrelscan.com/rules/a11y/button-name)

2 buttons (`.close-btn`, `.toc-close-btn`) lack accessible names. Screen readers can't identify their purpose.

### 4. Accessibility: 13 command elements without names
**Rule:** `a11y/aria-command-name` | [Docs](https://docs.squirrelscan.com/rules/a11y/aria-command-name)

Submit buttons and social share links (Twitter, Facebook, LinkedIn) are missing accessible names.

---

## Key Warnings

### Core SEO
- **Title truncation risk** — Title is 63 chars ("Replacing the 'Just Checking In' Email | 15 Better..."). Likely truncated in SERPs.
- **Missing og:image** — Social shares will have no imagery.
- **Twitter card missing image** — `summary_large_image` card declared but no image provided.

### Security
- **Leaked API keys** — Amplitude API key and a generic API key are exposed in inline scripts. Needs manual verification.
- **Missing security headers** — No Content-Security-Policy, no HSTS, no X-Frame-Options.
- **10 external links missing `rel="noopener"`** — Social share links open in new tabs without noopener protection.
- **HTTP links on HTTPS page** — 8 links downgrade to HTTP (mostly old social share URLs using http://).

### Links
- **3 broken external links:**
  - `http://twitter.com/home/?status=...` → 520 error
  - `http://www.facebook.com/sharer.php?u=...` → 500 error
  - `https://www.dooly.ai/blog/sales-follow-up-statistics/` → 404
- **Duplicate social share links** — Two different sets of social sharing buttons with different URL formats (one uses relative paths, one uses full URLs with `/blog/blog/` double path).
- **3 links with generic anchor text** ("here", "categories" pointing to different URLs).

### Images
- **3 images over 1 MB:**
  - `Screen-Shot-2022-07-16-at-9.14.03-PM.png` — 1.5 MB (PNG screenshot)
  - `Petra_Headshot.png` — 1.3 MB (author headshot as PNG)
  - `12_Dreamworld—Form-Animation.gif` — 1.2 MB (animated GIF)
- **6 images missing alt text**
- **3 images missing width/height** — causes cumulative layout shift (CLS).
- **No next-gen formats** — 9 images could use WebP/AVIF.
- **LCP image not preloaded** — The hero image (`flodesk-emails.png`) has no `<link rel="preload">`.

### Performance
- **Total page weight: 5,113 KB** — very heavy for a blog post.
- **No caching headers** on the page itself.
- **4 critical request chains** — CSS and JS blocking render.
- **Large DOM** — element with 100 children.

### E-E-A-T
- **No author byline** on the page.
- **No datePublished** — search engines can't determine freshness.
- **No about page, contact page, or privacy policy** linked/discoverable from this page.

### Accessibility
- **Heading skip** — jumps from H1 to H3 (no H2).
- **11 links with no accessible text** (SVG icons in social share buttons).
- **No skip-link** for keyboard navigation.
- **No `<main>` landmark.**
- **Color contrast issues** — 3 combinations below 4.5:1 ratio.

---

## Priority Fix Recommendations

| Priority | Issue | Impact | Owner |
|----------|-------|--------|-------|
| 1 | Fix broken social share links (duplicate sets, broken URLs) | Links, SEO | Dev |
| 2 | Add og:image and complete social meta | Core SEO, Social | Dev |
| 3 | Compress/convert images to WebP, add alt text + dimensions | Images, Performance, Accessibility | Dev |
| 4 | Add author byline and publish date | E-E-A-T | Content |
| 5 | Fix heading hierarchy (H1 → H2 → H3) | Accessibility, Content | Content |
| 6 | Add accessible names to buttons and social links | Accessibility | Dev |
| 7 | Preload LCP image | Performance | Dev |
| 8 | Add security headers (CSP, HSTS, X-Frame-Options) | Security | DevOps |
| 9 | Minify/split main.js bundle | Performance | Dev |
| 10 | Verify and rotate exposed API keys | Security | Dev |

---

## Context

This is Flodesk's highest-traffic blog post (1,142 organic visits/mo, 213 keywords). Despite strong content and good keyword coverage, the page scores poorly due to legacy WordPress issues — oversized unoptimized images, missing security headers, broken social share widgets, and no E-E-A-T signals. These are likely site-wide template issues, not specific to this post.

**Raw audit data:** `raw-just-checking-in-audit.txt`
