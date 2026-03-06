# CheckThat Citation Share Analysis

<metadata>
purpose: Analyze top cited domains across all CheckThat evaluation-stage prompts
audience: Marcel, leadership
domain: product, data-analysis
access: company
last_updated: 2026-03-04
</metadata>

## Scope

- **Data source:** CheckThat production database (all workspaces)
- **Prompts:** Shared library only (`workspace_id IS NULL`), evaluation funnel stage
- **Prompts in scope:** 10,077 distinct evaluation prompts
- **Date range:** Last 30 days vs previous 30 days (as of March 5, 2026)
- **Exclusion:** `vertexaisearch.cloud.google.com` removed (Gemini self-citing Google search — noise)

## Total Citations

| Period | Citations | Probes | Change |
|--------|-----------|--------|--------|
| Last 30 days | 7,638,396 | 1,046,412 | — |
| Previous 30 days | 5,847,071 | — | — |
| **Delta** | **+1,791,325** | — | **+30.6%** |

---

## Top 20 Cited Domains — Last 30 Days vs Previous 30 Days

| Rank | Domain | Last 30d | Prev 30d | Change | Share |
|------|--------|----------|----------|--------|-------|
| 1 | www.youtube.com | 162,337 | 128,795 | +26.0% | 2.13% |
| 2 | www.gartner.com | 135,668 | 47,704 | +184.4% | 1.78% |
| 3 | www.techradar.com | 130,320 | 104,725 | +24.4% | 1.71% |
| 4 | www.capterra.com | 79,234 | 43,494 | +82.2% | 1.04% |
| 5 | www.g2.com | 76,744 | 77,708 | -1.2% | 1.00% |
| 6 | zapier.com | 69,769 | 67,181 | +3.9% | 0.91% |
| 7 | en.wikipedia.org | 59,184 | 48,085 | +23.1% | 0.78% |
| 8 | www.reddit.com | 52,935 | 57,216 | -7.5% | 0.69% |
| 9 | www.sentinelone.com | 45,205 | 22,496 | +101.0% | 0.59% |
| 10 | monday.com | 43,840 | 29,188 | +50.2% | 0.57% |
| 11 | thectoclub.com | 33,319 | 23,835 | +39.8% | 0.44% |
| 12 | thedigitalprojectmanager.com | 33,219 | 31,437 | +5.7% | 0.43% |
| 13 | www.zendesk.com | 30,364 | 16,215 | +87.3% | 0.40% |
| 14 | peoplemanagingpeople.com | 30,249 | 20,001 | +51.2% | 0.40% |
| 15 | www.salesforce.com | 25,310 | 16,473 | +53.7% | 0.33% |
| 16 | github.com | 23,024 | 17,687 | +30.2% | 0.30% |
| 17 | learn.g2.com | 22,893 | 20,256 | +13.0% | 0.30% |
| 18 | www.softwarereviews.com | 22,885 | 18,324 | +24.9% | 0.30% |
| 19 | solutionsreview.com | 22,795 | 8,797 | +159.1% | 0.30% |
| 20 | www.forbes.com | 20,881 | 28,329 | -26.3% | 0.27% |

**Top 20 total:** 1,120,175 citations (14.7% of all evaluation citations)

### Biggest movers

- **Gartner (+184%)** — driven almost entirely by Anthropic's Claude, which now cites Gartner 89K times (66% of all Gartner citations). Claude barely existed as a citation source in the previous period.
- **SolutionsReview (+159%)** — broad-based growth across Perplexity and Google AI Overview.
- **SentinelOne (+101%)** — doubled, with Perplexity and Anthropic driving most of the growth.
- **Zendesk (+87%)** — Anthropic and Google AI Overview drove the increase.
- **Forbes (-26%)** — the only significant decliner. Lost ground with Perplexity (near-zero) while still cited by Google AI Overview and OpenAI.

---

## Citation Volume by Engine

| Engine | Last 30d | Prev 30d | Change | Share |
|--------|----------|----------|--------|-------|
| Perplexity | 2,197,262 | 2,355,016 | -6.7% | 28.8% |
| Anthropic (Claude) | 2,172,830 | 76,063 | +2,757% | 28.4% |
| Google AI Overview | 1,379,080 | 1,224,817 | +12.6% | 18.1% |
| OpenAI (ChatGPT) | 1,322,033 | 1,078,290 | +22.6% | 17.3% |
| Gemini | 583,720 | 1,112,885 | -47.6% | 7.6% |

**Key shift:** Anthropic went from 1.3% to 28.4% of all citations in one month — a 28x increase. This single change reshapes the entire domain ranking (Gartner and Capterra surged because Claude cites them heavily). Gemini dropped by half.

---

## Top 20 Domains by Engine (Last 30 Days)

### Perplexity (2.2M citations — 28.8% share)

| Rank | Domain | Citations |
|------|--------|-----------|
| 1 | www.youtube.com | 88,302 |
| 2 | www.g2.com | 39,541 |
| 3 | zapier.com | 27,082 |
| 4 | monday.com | 19,457 |
| 5 | www.sentinelone.com | 17,976 |
| 6 | thedigitalprojectmanager.com | 13,935 |
| 7 | www.capterra.com | 13,462 |
| 8 | www.softwarereviews.com | 11,992 |
| 9 | solutionsreview.com | 10,956 |
| 10 | peoplemanagingpeople.com | 10,802 |
| 11 | www.zendesk.com | 9,811 |
| 12 | www.techradar.com | 9,237 |
| 13 | www.salesforce.com | 7,531 |
| 14 | learn.g2.com | 6,492 |
| 15 | thectoclub.com | 6,099 |
| 16 | github.com | 2,884 |
| 17 | en.wikipedia.org | 1,638 |
| 18 | www.gartner.com | 20 |
| 19 | www.reddit.com | 2 |
| 20 | www.forbes.com | 0 |

Perplexity's profile: heavily favors YouTube, G2, and product-specific sites. Nearly zero citations of Gartner, Reddit, or Forbes.

### Anthropic / Claude (2.2M citations — 28.4% share)

| Rank | Domain | Citations |
|------|--------|-----------|
| 1 | www.gartner.com | 89,162 |
| 2 | www.capterra.com | 57,300 |
| 3 | thectoclub.com | 23,732 |
| 4 | peoplemanagingpeople.com | 16,102 |
| 5 | www.sentinelone.com | 15,858 |
| 6 | zapier.com | 15,686 |
| 7 | thedigitalprojectmanager.com | 15,542 |
| 8 | www.g2.com | 15,140 |
| 9 | monday.com | 14,434 |
| 10 | www.techradar.com | 13,696 |
| 11 | www.zendesk.com | 10,676 |
| 12 | www.softwarereviews.com | 7,223 |
| 13 | learn.g2.com | 5,707 |
| 14 | solutionsreview.com | 5,651 |
| 15 | www.salesforce.com | 4,911 |
| 16 | github.com | 3,701 |
| 17 | en.wikipedia.org | 1,722 |
| 18 | www.forbes.com | 5 |
| 19 | www.reddit.com | 2 |
| 20 | www.youtube.com | 1 |

Claude's profile: strongly favors analyst/review sites (Gartner, Capterra, G2). Almost never cites YouTube, Reddit, Forbes, or Wikipedia. The most "professional source" engine.

### Google AI Overview (1.4M citations — 18.1% share)

| Rank | Domain | Citations |
|------|--------|-----------|
| 1 | www.youtube.com | 73,443 |
| 2 | www.reddit.com | 49,162 |
| 3 | www.gartner.com | 31,125 |
| 4 | zapier.com | 18,438 |
| 5 | www.sentinelone.com | 9,947 |
| 6 | monday.com | 7,977 |
| 7 | www.zendesk.com | 7,545 |
| 8 | www.forbes.com | 6,892 |
| 9 | www.g2.com | 5,563 |
| 10 | www.salesforce.com | 4,787 |
| 11 | www.techradar.com | 3,489 |
| 12 | www.softwarereviews.com | 3,298 |
| 13 | github.com | 3,279 |
| 14 | solutionsreview.com | 2,847 |
| 15 | www.capterra.com | 2,449 |
| 16 | learn.g2.com | 1,095 |
| 17 | peoplemanagingpeople.com | 781 |
| 18 | thedigitalprojectmanager.com | 661 |
| 19 | en.wikipedia.org | 566 |
| 20 | thectoclub.com | 325 |

Google AI Overview's profile: YouTube and Reddit dominate (Google's own properties / UGC bias). Broader spread across source types than other engines.

### OpenAI / ChatGPT (1.3M citations — 17.3% share)

| Rank | Domain | Citations |
|------|--------|-----------|
| 1 | www.techradar.com | 103,373 |
| 2 | en.wikipedia.org | 55,341 |
| 3 | www.g2.com | 15,336 |
| 4 | www.gartner.com | 13,920 |
| 5 | www.forbes.com | 13,476 |
| 6 | github.com | 11,648 |
| 7 | learn.g2.com | 9,627 |
| 8 | www.salesforce.com | 7,789 |
| 9 | www.capterra.com | 5,965 |
| 10 | www.reddit.com | 3,411 |
| 11 | www.zendesk.com | 2,184 |
| 12 | zapier.com | 1,929 |
| 13 | solutionsreview.com | 1,676 |
| 14 | www.sentinelone.com | 1,213 |
| 15 | monday.com | 943 |
| 16 | www.softwarereviews.com | 288 |
| 17 | peoplemanagingpeople.com | 266 |
| 18 | thedigitalprojectmanager.com | 52 |
| 19 | thectoclub.com | 52 |
| 20 | www.youtube.com | 0 |

ChatGPT's profile: extreme concentration on TechRadar (#1 by far) and Wikipedia (#2). Prefers established media and reference sites. Near-zero YouTube or niche sites.

### Gemini (584K citations — 7.6% share)

| Rank | Domain | Citations |
|------|--------|-----------|
| 1 | zapier.com | 6,686 |
| 2 | thectoclub.com | 3,130 |
| 3 | thedigitalprojectmanager.com | 3,051 |
| 4 | peoplemanagingpeople.com | 2,321 |
| 5 | solutionsreview.com | 1,688 |
| 6 | www.gartner.com | 1,579 |
| 7 | github.com | 1,520 |
| 8 | www.g2.com | 1,261 |
| 9 | monday.com | 1,075 |
| 10 | www.youtube.com | 804 |
| 11 | www.techradar.com | 644 |
| 12 | www.forbes.com | 535 |
| 13 | www.reddit.com | 479 |
| 14 | www.salesforce.com | 320 |
| 15 | www.sentinelone.com | 247 |
| 16 | www.zendesk.com | 184 |
| 17 | www.capterra.com | 138 |
| 18 | www.softwarereviews.com | 106 |
| 19 | en.wikipedia.org | 20 |
| 20 | learn.g2.com | 6 |

Gemini's profile: lowest citation volume of any engine. Spreads citations thinly across niche content sites. Dropped 48% month-over-month.

---

## Engine Source Preferences — Summary Matrix

Which engines cite which sources most (relative to their own total):

| Domain | Perplexity | Claude | Google AIO | ChatGPT | Gemini |
|--------|-----------|--------|------------|---------|--------|
| youtube.com | **#1** | — | **#1** | — | low |
| gartner.com | — | **#1** | #3 | #4 | low |
| techradar.com | mid | mid | low | **#1** | low |
| capterra.com | mid | **#2** | low | mid | — |
| g2.com | **#2** | mid | mid | #3 | low |
| zapier.com | **#3** | mid | #4 | low | **#1** |
| wikipedia.org | low | low | low | **#2** | — |
| reddit.com | — | — | **#2** | low | low |
| sentinelone.com | #5 | #5 | #5 | low | low |
| monday.com | #4 | mid | #6 | low | low |

**Key patterns:**
- **Perplexity** favors YouTube, G2, and product sites
- **Claude** favors analyst firms (Gartner, Capterra) and avoids UGC/media
- **Google AIO** favors YouTube and Reddit (Google-owned/UGC)
- **ChatGPT** favors TechRadar and Wikipedia (editorial/reference)
- **Gemini** has low volume across the board, leans toward niche content sites
