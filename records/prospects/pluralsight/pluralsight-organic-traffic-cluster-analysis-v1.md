# Pluralsight Organic Traffic: Page Cluster Analysis

<metadata>
purpose: Organic traffic cluster analysis — 10,027 URLs, page performance, content gap identification (Ahrefs data)
audience: GrowthX strategy, Pluralsight client team
domain: client-research
confidence: high
sensitivity: client
context_tier: 2
last_updated: 2026-02-13
</metadata>

---

## The Big Picture

Pluralsight's organic footprint is enormous (10K+ pages) but hollow. Just **1.3% of pages drive 93% of all traffic.** 87% of indexed URLs get zero visits. The site generates ~125K estimated monthly organic visits, but nearly half of that (51%) is branded/navigational traffic hitting the homepage and Cloud Guru page — leaving only ~61K visits for actual content discovery.

The blog (`/resources/blog/`) is the real organic engine, pulling 35,900 visits across 2,332 pages. Everything else — courses (4,658 pages), labs (1,028 pages), learning paths (678 pages) — is essentially invisible to search.

---

## Structural Clusters (by URL path)

| Cluster | Pages | Traffic | % of Total | Avg/Page | Trend |
|---------|------:|--------:|-----------:|---------:|-------|
| Homepage + brand pages | 6 | 63,524 | 50.8% | 10,587 | +3,414 |
| Blog (`/resources/blog/`) | 2,332 | 35,922 | 28.7% | 15.4 | -10,454 |
| Cloud Guru (`/cloud-guru`) | 13 | 14,625 | 11.7% | 1,125 | -1,004 |
| Learning Paths (`/paths/`) | 678 | 2,386 | 1.9% | 3.5 | — |
| Product pages | 20 | 1,781 | 1.4% | 89.1 | — |
| Courses (`/courses/`) | 4,658 | 1,332 | 1.1% | 0.3 | — |
| Careers | 6 | 1,264 | 1.0% | 211 | — |
| Authors | 282 | 772 | 0.6% | 2.7 | — |
| Labs (`/labs/`) | 1,028 | 367 | 0.3% | 0.4 | — |
| Everything else | 1,004 | 1,110 | 0.9% | 1.1 | — |

**Key takeaway:** 6,364 pages across courses, labs, and professional services sections generate less than 2% of traffic combined. This is an enormous indexing footprint producing almost nothing — and likely diluting crawl budget.

---

## Blog Topic Clusters

The blog's 35,900 visits break down into clear topic territories. Here's how they perform:

| Topic Cluster | Pages | Traffic | Avg/Page | Info Intent | Trend |
|--------------|------:|--------:|---------:|------------:|------:|
| Cloud General / DevOps | 339 | 9,644 | 28.4 | 74% | -4,122 |
| AI / Machine Learning | 170 | 4,397 | 25.9 | 82% | -3,118 |
| Certifications / Career | 76 | 2,966 | 39.0 | 86% | -394 |
| Design / UX | 21 | 2,944 | 140.2 | 95% | +500 |
| AWS (specific) | 208 | 2,045 | 9.8 | 85% | +199 |
| Linux / Command Line | 34 | 1,903 | 56.0 | 97% | +22 |
| Guides (misc) | 401 | 1,698 | 4.2 | 91% | -117 |
| Networking / IT Ops | 90 | 1,669 | 18.5 | 90% | -981 |
| Google Cloud (GCP) | 24 | 1,246 | 51.9 | 86% | +417 |
| Azure (specific) | 112 | 1,191 | 10.6 | 97% | -58 |
| JavaScript / TypeScript | 336 | 1,188 | 3.5 | 59% | -275 |
| Java / JVM | 24 | 681 | 28.4 | 99% | -87 |
| Cybersecurity | 59 | 617 | 10.5 | 73% | +54 |
| Python | 76 | 501 | 6.6 | 90% | +173 |
| SQL / Databases | 28 | 422 | 15.1 | 78% | +107 |
| Data Science / Analytics | 94 | 108 | 1.1 | 99% | -32 |
| Other (3D, game dev, misc) | 196 | 2,640 | 13.5 | 92% | -2,705 |

---

## What's Working

**High-efficiency clusters** (strong traffic per page):

- **Design / UX** — Only 21 pages but 2,944 visits (140 avg/page). Growing. Punches way above its weight, driven by foundational topics like hex colors and graphic design balance.
- **Linux / Command Line** — 34 pages, 1,903 visits (56 avg). Extremely stable. Practical how-to content (`bash scripting`, `file permissions`, `sudo`) with near-pure informational intent.
- **GCP** — 24 pages generating 1,246 visits (52 avg) and *growing* (+417). Efficient cluster with momentum.
- **Certifications / Career** — 76 pages, 2,966 visits (39 avg). Includes the "which certification" comparison pages that pull commercial intent traffic.

**Pages with momentum** (biggest traffic gains):

- Hexadecimal colors explainer (+577, now 2,305 visits)
- "What is GCP" (+436, now 1,181)
- AWS jobs/certifications (+427, now 554)
- Learning to code with AI (+413, new entry at 413)
- Azure certification guide (+283, now 589)

---

## What's Bleeding

**The blog lost 10,454 visits net.** The biggest hits:

- **"What is Go/Golang"** — down 4,057 (was ~7,400, now 3,345). Still the top blog post but in steep decline.
- **"What is Claude AI"** — down 3,560 (was ~6,100, now 2,525). Likely losing to Anthropic's own content and newer competitor pages.
- **AI & Data category overall** — down 47.5%. The most severe decline by percentage. AI-related content is being outcompeted quickly.
- **Cloud category** — down 20%. The largest absolute loss as the biggest cluster.
- **Software Development** — down 22.7%. 3D/VFX content (ambient occlusion, subsurface scattering, animation) is collapsing.
- **Tech Operations** — down 29%. VMware and legacy IT content aging out.

---

## Intent Profile

**Site-wide:** 57% navigational (people typing "pluralsight" into Google), 29% informational, 14% commercial, 4% transactional.

**Blog only:** 84% informational, 11% commercial, 10% navigational, 2% transactional. The blog is almost entirely top-of-funnel awareness content. Very little of it captures purchase-intent queries.

The clusters with the highest commercial intent mix are AWS (36% of keywords) and Cybersecurity (31%) — certification-adjacent content where people are evaluating options.

---

## The Dead Weight Problem

**8,742 pages (87%) get zero traffic.** The worst offenders:

| Section | Zero-Traffic Pages | Still Indexed Keywords |
|---------|-------------------:|-----------------------:|
| Courses | 4,431 | 12,556 |
| Blog | 1,760 | 11,372 |
| Labs | 982 | 3,614 |
| Learning Paths | 517 | 3,530 |
| Professional Services | 319 | 1,842 |

The courses section alone has 4,431 dead pages. These are individual course listing pages that don't rank for anything meaningful. They exist in the index, consuming crawl budget, but producing nothing.

---

## Untapped Opportunities

**51 blog pages have 50+ ranking keywords but ≤10 traffic** — meaning they're indexed and showing up in results but not yet clicking. Top candidates:

- "Best paying tech jobs 2025" (223 keywords, 4 visits)
- "Create your first mobile game" (214 keywords, 3 visits)
- "What is augmented reality" (186 keywords, 8 visits)
- "CI/CD tools and pipelines" (140 keywords, 7 visits)
- "Public cloud vs private cloud" (109 keywords, 4 visits)

These pages are ranking for many queries but at low positions. They're the lowest-hanging fruit for content refresh and on-page optimization.

---

## Summary of Findings

1. **Extreme concentration** — 0.2% of pages (21) drive 80% of traffic. The long tail is nearly worthless.
2. **The blog is the only real organic asset** beyond brand — and it's declining (-10K visits).
3. **AI content is getting crushed** — down 47.5%, likely outcompeted by primary sources (Anthropic, OpenAI blogs).
4. **Cloud and certifications remain the core** — still the strongest topic clusters, but both trending down.
5. **Design/UX and Linux are the bright spots** — high efficiency, stable or growing, evergreen content.
6. **Courses, labs, and paths are SEO dead weight** — 6,364 pages generating 4,085 visits total. That's 0.64 visits per page.
7. **Almost no commercial-intent content** — the blog is 84% informational. The gap between awareness content and conversion content is wide.
8. **51 high-keyword/low-traffic pages** are the quickest optimization wins available.
