# Simple.Life — ROI Model v2: Three Production Scenarios

<metadata>
purpose: ROI projection model comparing three content production scenarios (5/week, 10/week, 20/week) for Simple.Life, built on a bottom-up analysis of 1,000 page-level opportunities with keyword-calibrated traffic estimates
audience: GrowthX strategy team, Simple Life GTM leadership
related: records/customers/simple-life/simple-life-1000-opportunities-v1.md, records/customers/simple-life/simple-life-roi-model-v1.md
domain: client-deliverable
confidence: high
sensitivity: client
context_tier: 2
last_updated: 2026-02-23
</metadata>

---

## Executive Summary

We identified 1,000 specific page opportunities across 20 clusters that together represent **175,000+ monthly visits** of addressable content traffic for Simple.Life. This model projects the ROI of capturing that opportunity across three production scenarios.

### The three scenarios at month 12

| Metric | 5 pages/week | 10 pages/week | 20 pages/week |
|---|---|---|---|
| Pages published | 260 | 520 | 1,040 |
| Organic content traffic (new) | 48,200 | 80,500 | 115,800 |
| Existing page refresh lift | +3,000 | +4,500 | +5,500 |
| Topical authority compound | +4,200 | +8,500 | +14,200 |
| **Total organic content traffic** | **55,400** | **93,500** | **135,500** |
| AEO referral traffic | 8,000 | 12,000 | 18,000 |
| Brand lift traffic | 5,000 | 8,000 | 12,000 |
| **Total incremental traffic** | **68,400** | **113,500** | **165,500** |
| Incremental purchases/month | 528 | 886 | 1,296 |
| **Multiple vs. baseline (59/mo)** | **9.9x** | **16.0x** | **23.0x** |
| Monthly LTV created | $36,960 | $62,020 | $90,720 |
| Monthly engagement cost | $22,000 | $38,000 | $65,000 |
| **Month-12 monthly ROI** | **+68%** | **+63%** | **+40%** |
| Cumulative ROI (12 months) | -27% | -35% | -42% |
| Cash-flow positive month | Month 8 | Month 9 | Month 10 |
| Cumulative breakeven month | Month 16 | Month 17 | Month 19 |

**The headline:** Even the lightest scenario (5/week) nearly 10x-es content-attributed purchases by month 12. The 10/week scenario reaches 16x. The 20/week scenario reaches 23x but requires significantly more investment and takes longer to achieve cumulative breakeven.

**The recommendation:** Start at 10 pages/week. It delivers the best balance of speed-to-10x (month 8-9), monthly ROI efficiency, and opportunity coverage. Scale to 20/week in Q3 if the first cohorts validate the model.

---

## Part 1: Current State Baseline

### January 2026 numbers

| Metric | Value | Source |
|---|---|---|
| Total organic traffic (site-wide) | 45,500/month | Analytics |
| Blog organic traffic | 8,650/month | Search Console |
| **Content page traffic (non-branded)** | **~5,800/month** | SEMrush (excluding homepage, help, TOS) |
| Content pages published | ~50 | SEMrush |
| Pages actively generating traffic | ~35 (70%) | SEMrush |
| Avg traffic per content page | ~166 | Calculated |
| App downloads/month | 20,000 | Analytics |
| Total purchases/month | 757 | Analytics |
| Visit-to-download rate (content) | 17.5% | Analytics (midpoint 15-20%) |
| Download-to-purchase rate | 3.9% | Analytics (midpoint 3.8-4%) |
| **Content-attributed purchases** | **~59/month** | Calculated: 8,650 × 17.5% × 3.9% |
| LTV (1-year confirmed) | $70 | Finance |
| Monthly paid ad budget (Meta) | ~$1M | Marketing |
| AI/LLM referral traffic | **Zero** | Site blocking AI indexation |

### Current content → purchase funnel

| Funnel step | Rate | Monthly volume |
|---|---|---|
| Blog organic visits | — | 8,650 |
| Visit-to-download | 17.5% | 1,514 |
| Download-to-purchase | 3.9% | **59 purchases** |
| Revenue from blog purchases | $70 LTV | **$4,130/month** |

**Baseline: 59 content-attributed purchases/month = $4,130/month = $49,560/year.**

---

## Part 2: The Opportunity Inventory

From the companion document (simple-life-1000-opportunities-v1.md), we identified 1,000 specific page opportunities across 20 clusters:

| Priority | Clusters | Pages | Net Capture (80% success) | % of Total |
|---|---|---|---|---|
| **Tier 1** (months 1–3) | Calculators, Schedules, Science, Meal Plans, Break a Fast | 230 | 62,200/month | 35% |
| **Tier 2** (months 4–6) | Food Lists, Blood Sugar, Populations, Results, Weight Loss, What to Eat | 275 | 59,320/month | 34% |
| **Tier 3** (months 7–9) | Keto/IF Food Evals, Recipes, Programmatic, Longevity, Diet Comparisons, Drinks | 325 | 37,200/month | 21% |
| **Tier 4** (months 10–12) | Exercise, Side Effects, Supplements | 95 | 11,960/month | 7% |
| **Buffer / refresh** | Existing page optimization | 75 (refreshes) | 5,000/month | 3% |
| **TOTAL** | 20 clusters | **1,000** | **175,460/month** | 100% |

This is the total addressable inventory. Each scenario selects from this inventory based on production capacity, prioritizing by per-page traffic value.

---

## Part 3: Conversion Model by Channel

Three traffic channels, each with distinct conversion characteristics:

| Channel | Visit-to-Download | Download-to-Purchase | Effective Visit-to-Purchase | Revenue/Visit |
|---|---|---|---|---|
| **Organic search (content)** | 17.5% | 3.9% | **0.68%** | $0.48 |
| **AEO referral traffic** | 35% | 3.9% | **1.37%** | $0.96 |
| **Brand lift (awareness → search)** | 40% | 3.9% | **1.56%** | $1.09 |

### Why AEO converts 2x organic

When an AI engine recommends Simple in response to "what's the best intermittent fasting app?" — the visitor arrives pre-qualified, endorsed by a third party, and informed. Research shows AI referral traffic converts 2-5x organic. We apply a conservative 2x on download rate.

### Brand lift mechanics

Every incremental visitor (search or AI) has a probability of becoming a future brand searcher:
- 20% become brand-aware
- 15% of those brand-search within 3 months
- Effective rate: 3% of incremental traffic → brand searches (2-month lag)
- Brand search converts at 1.56% visit-to-purchase (highest rate)

---

## Part 4: Content Maturation Curve

New pages don't generate traffic immediately. The model applies this ramp:

| Months After Publish | % of Peak Traffic | What's Happening |
|---|---|---|
| Month 1 | 0% | Indexing. Google crawls, no meaningful traffic. |
| Month 2 | 25% | Initial rankings, positions 10-30. |
| Month 3 | 50% | Rankings improve, CTR building. |
| Month 4+ | 100% | Steady-state. Page at natural ranking. |

**Post-peak growth:** +2%/month for clusters with 15+ pages (topical authority compounding). Applied to fully matured pages only.

**Exception:** Calculator/tool pages ramp 30% faster (month 2: 30%, month 3: 65%, month 4: 100%) because they target high-volume, lower-competition queries and earn links/shares.

---

## Part 5: Scenario A — 5 Pages/Week (260 pages in year 1)

### Production plan

~22 pages/month, prioritized by per-page traffic value. Covers the top 260 opportunities from the 1,000.

| Quarter | Pages/Month | Focus | Cumulative Pages |
|---|---|---|---|
| Q1 (M1-3) | 22/mo | Calculators (15), top science (8), top schedules (12), break-a-fast expansion (31) | 66 |
| Q2 (M4-6) | 22/mo | Blood sugar (15), meal plans (15), results (12), populations (10), food lists (14) | 132 |
| Q3 (M7-9) | 22/mo | Recipes (15), weight loss (15), diet comparisons (10), drinks (10), keto evals (16) | 198 |
| Q4 (M10-12) | 20/mo | Exercise (10), supplements (10), safety (10), longevity (10), remaining high-value (22) | 260 |

**Plus:** Ongoing refresh of 8-10 existing pages/month starting month 3.

### Per-cohort traffic values

Pages published first are the highest value (prioritized selection):

| Monthly Cohort | Pages | Avg Peak Traffic/Page | Content Mix |
|---|---|---|---|
| M1 | 22 | 680 | 5 calculators, 4 science pillars, 8 break-a-fast, 5 schedules |
| M2 | 22 | 520 | 5 calculators, 3 science, 7 break-a-fast, 7 schedules |
| M3 | 22 | 400 | 5 calculators, 5 blood sugar, 6 break-a-fast, 6 meal plans |
| M4 | 22 | 310 | 8 meal plans, 6 results, 4 populations, 4 food lists |
| M5 | 22 | 260 | 6 food lists, 6 results, 5 populations, 5 weight loss |
| M6 | 22 | 220 | 6 weight loss, 6 food lists, 5 comparisons, 5 recipes |
| M7 | 22 | 180 | 8 recipes, 6 keto evals, 4 drinks, 4 break-a-fast |
| M8 | 22 | 155 | 6 keto evals, 6 programmatic, 5 recipes, 5 drinks |
| M9 | 22 | 130 | 6 programmatic, 5 exercise, 6 supplements, 5 keto evals |
| M10 | 22 | 110 | 5 safety, 5 longevity, 6 exercise, 6 remaining |
| M11 | 22 | 95 | 5 supplements, 5 safety, 6 programmatic, 6 remaining |
| M12 | 18 | 80 | Remaining long-tail from underrepresented clusters |

### Month-by-month traffic projection

| Month | New Pages (Cumul.) | Matured Pages | New Page Organic | Refresh Lift | Authority Compound | AEO | Brand Lift | **Total Incremental** | **Purchases** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 22 | 0 | 0 | 0 | 0 | 0 | 0 | **0** | **0** |
| 2 | 44 | 0 | 3,740 | 0 | 0 | 200 | 0 | **3,940** | **29** |
| 3 | 66 | 22 | 9,800 | 300 | 0 | 600 | 100 | **10,800** | **82** |
| 4 | 88 | 44 | 20,300 | 600 | 500 | 1,500 | 300 | **23,200** | **178** |
| 5 | 110 | 66 | 28,500 | 1,000 | 1,200 | 2,800 | 700 | **34,200** | **268** |
| 6 | 132 | 88 | 34,800 | 1,500 | 2,000 | 4,000 | 1,500 | **43,800** | **350** |
| 7 | 154 | 110 | 39,200 | 2,000 | 2,800 | 5,200 | 2,500 | **51,700** | **413** |
| 8 | 176 | 132 | 42,800 | 2,400 | 3,300 | 6,200 | 3,200 | **57,900** | **461** |
| 9 | 198 | 154 | 45,500 | 2,700 | 3,700 | 7,000 | 3,800 | **62,700** | **497** |
| 10 | 220 | 176 | 47,100 | 2,900 | 4,000 | 7,500 | 4,300 | **65,800** | **519** |
| 11 | 242 | 198 | 47,800 | 3,000 | 4,100 | 7,800 | 4,700 | **67,400** | **528** |
| 12 | 260 | 220 | 48,200 | 3,000 | 4,200 | 8,000 | 5,000 | **68,400** | **528** |

### Purchase breakdown by channel (month 12)

| Channel | Traffic | Visit-to-Purchase | Purchases |
|---|---|---|---|
| Organic content (new + refresh + compound) | 55,400 | 0.68% | 377 |
| AEO referral | 8,000 | 1.37% | 110 |
| Brand lift | 5,000 | 1.56% | 78 |
| **Total incremental** | **68,400** | | **528** (+59 existing = 587) |
| **Multiple vs. baseline** | | | **9.9x** |

### Financial projection — 5/week

| Metric | Month 6 | Month 12 | Month 18 | Month 24 |
|---|---|---|---|---|
| Incremental purchases/month | 350 | 528 | 680 | 750 |
| Monthly LTV created | $24,500 | $36,960 | $47,600 | $52,500 |
| Monthly engagement cost | $22,000 | $22,000 | $22,000 | $22,000 |
| Monthly net cash flow | +$2,500 | +$14,960 | +$25,600 | +$30,500 |
| Cumulative investment | $132,000 | $264,000 | $396,000 | $528,000 |
| Cumulative LTV created | $57,600 | $192,600 | $424,000 | $720,000 |
| **Cumulative ROI** | **-56%** | **-27%** | **+7%** | **+36%** |

**Cash-flow positive:** Month 8 (monthly LTV > monthly cost)
**Cumulative breakeven:** ~Month 16
**By month 24:** +36% cumulative ROI, generating $52,500/month LTV against $22,000 cost

### Cost structure — 5/week

| Line Item | Monthly Cost | Notes |
|---|---|---|
| Content strategist (fractional) | $4,000 | Keyword research, briefs, editorial calendar |
| Writers (2-3 freelance) | $8,000 | 22 pages/month × ~$360/page avg |
| SEO specialist (fractional) | $3,000 | Technical SEO, schema, internal linking |
| Designer / tool development | $3,000 | Calculator UIs, infographics, visual assets |
| AEO optimization | $2,000 | AI indexation, structured data, CheckThat monitoring |
| Project management | $2,000 | GrowthX oversight, QA, analytics |
| **Total** | **$22,000/month** | **$264,000/year** |

---

## Part 6: Scenario B — 10 Pages/Week (520 pages in year 1)

### Production plan

~44 pages/month. Covers the top 520 opportunities — fully addressing Tier 1 and 2, with strong coverage of Tier 3.

| Quarter | Pages/Month | Focus | Cumulative Pages |
|---|---|---|---|
| Q1 (M1-3) | 44/mo | All calculators (15), full science (30), full schedules (40), break-a-fast (47) | 132 |
| Q2 (M4-6) | 44/mo | Full blood sugar (45), full meal plans (40), full results (30), populations (17) | 264 |
| Q3 (M7-9) | 44/mo | Full food lists (50), full populations (23), recipes (30), keto evals (29) | 396 |
| Q4 (M10-12) | 42/mo | Full weight loss (50), diet comparisons (25), remaining from Tier 3 (51) | 520 |

### Per-cohort traffic values

| Monthly Cohort | Pages | Avg Peak Traffic/Page |
|---|---|---|
| M1 | 44 | 500 |
| M2 | 44 | 380 |
| M3 | 44 | 300 |
| M4 | 44 | 240 |
| M5 | 44 | 200 |
| M6 | 44 | 170 |
| M7 | 44 | 145 |
| M8 | 44 | 125 |
| M9 | 44 | 110 |
| M10 | 44 | 95 |
| M11 | 44 | 80 |
| M12 | 36 | 70 |

### Month-by-month traffic projection

| Month | Cumul. Pages | New Page Organic | Refresh + Authority | AEO | Brand Lift | **Total Incremental** | **Purchases** |
|---|---|---|---|---|---|---|---|
| 1 | 44 | 0 | 0 | 0 | 0 | **0** | **0** |
| 2 | 88 | 5,500 | 0 | 300 | 0 | **5,800** | **43** |
| 3 | 132 | 15,900 | 500 | 1,000 | 200 | **17,600** | **136** |
| 4 | 176 | 32,200 | 1,200 | 2,500 | 600 | **36,500** | **286** |
| 5 | 220 | 45,800 | 2,200 | 4,200 | 1,500 | **53,700** | **425** |
| 6 | 264 | 56,500 | 3,500 | 5,800 | 3,000 | **68,800** | **547** |
| 7 | 308 | 64,800 | 5,000 | 7,500 | 4,500 | **81,800** | **651** |
| 8 | 352 | 71,200 | 6,500 | 9,000 | 5,800 | **92,500** | **736** |
| 9 | 396 | 75,800 | 8,000 | 10,200 | 6,800 | **100,800** | **802** |
| 10 | 440 | 78,500 | 10,000 | 11,000 | 7,500 | **107,000** | **851** |
| 11 | 484 | 79,800 | 12,000 | 11,500 | 7,800 | **111,100** | **874** |
| 12 | 520 | 80,500 | 13,000 | 12,000 | 8,000 | **113,500** | **886** |

### Purchase breakdown by channel (month 12)

| Channel | Traffic | Visit-to-Purchase | Purchases |
|---|---|---|---|
| Organic content (new + refresh + compound) | 93,500 | 0.68% | 636 |
| AEO referral | 12,000 | 1.37% | 164 |
| Brand lift | 8,000 | 1.56% | 125 |
| **Total incremental** | **113,500** | | **886** (+59 existing = 945) |
| **Multiple vs. baseline** | | | **16.0x** |

### Financial projection — 10/week

| Metric | Month 6 | Month 12 | Month 18 | Month 24 |
|---|---|---|---|---|
| Incremental purchases/month | 547 | 886 | 1,100 | 1,200 |
| Monthly LTV created | $38,290 | $62,020 | $77,000 | $84,000 |
| Monthly engagement cost | $38,000 | $38,000 | $38,000 | $38,000 |
| Monthly net cash flow | +$290 | +$24,020 | +$39,000 | +$46,000 |
| Cumulative investment | $228,000 | $456,000 | $684,000 | $912,000 |
| Cumulative LTV created | $90,100 | $297,500 | $660,000 | $1,120,000 |
| **Cumulative ROI** | **-60%** | **-35%** | **-4%** | **+23%** |

**Cash-flow positive:** Month 9 (monthly LTV > monthly cost)
**Cumulative breakeven:** ~Month 17
**By month 24:** +23% cumulative ROI, generating $84,000/month LTV against $38,000 cost

### Cost structure — 10/week

| Line Item | Monthly Cost | Notes |
|---|---|---|
| Content strategist (full-time) | $6,000 | Keyword research, briefs, editorial calendar, QA |
| Writers (5-6 freelance) | $14,000 | 44 pages/month × ~$320/page avg (bulk discount) |
| SEO specialist (full-time) | $5,000 | Technical SEO, schema, linking, analytics |
| Designer / tool development | $5,000 | Calculator UIs, infographics, templates |
| AEO optimization | $3,000 | AI indexation, structured data, CheckThat monitoring |
| Project management | $3,000 | GrowthX oversight, editorial workflow |
| Technology / tools | $2,000 | SEMrush, CMS, content production tools |
| **Total** | **$38,000/month** | **$456,000/year** |

---

## Part 7: Scenario C — 20 Pages/Week (1,040 pages in year 1)

### Production plan

~88 pages/month. Covers all 1,000+ opportunities — every cluster fully built out including programmatic content at scale.

| Quarter | Pages/Month | Focus | Cumulative Pages |
|---|---|---|---|
| Q1 (M1-3) | 88/mo | All Tier 1 (230), start Tier 2 (34) | 264 |
| Q2 (M4-6) | 88/mo | Complete Tier 2 (241), start Tier 3 (23) | 528 |
| Q3 (M7-9) | 88/mo | Complete Tier 3 (302), start Tier 4 (38) | 792 |
| Q4 (M10-12) | 82/mo | Complete Tier 4 (57), programmatic at scale (80), expansion (111) | 1,040 |

### Per-cohort traffic values

| Monthly Cohort | Pages | Avg Peak Traffic/Page |
|---|---|---|
| M1 | 88 | 380 |
| M2 | 88 | 280 |
| M3 | 88 | 220 |
| M4 | 88 | 180 |
| M5 | 88 | 150 |
| M6 | 88 | 125 |
| M7 | 88 | 105 |
| M8 | 88 | 90 |
| M9 | 88 | 75 |
| M10 | 88 | 65 |
| M11 | 88 | 55 |
| M12 | 72 | 45 |

### Month-by-month traffic projection

| Month | Cumul. Pages | New Page Organic | Refresh + Authority | AEO | Brand Lift | **Total Incremental** | **Purchases** |
|---|---|---|---|---|---|---|---|
| 1 | 88 | 0 | 0 | 0 | 0 | **0** | **0** |
| 2 | 176 | 8,400 | 0 | 500 | 0 | **8,900** | **66** |
| 3 | 264 | 22,400 | 800 | 1,500 | 300 | **25,000** | **194** |
| 4 | 352 | 44,000 | 2,000 | 3,500 | 1,000 | **50,500** | **396** |
| 5 | 440 | 61,500 | 3,500 | 6,000 | 2,500 | **73,500** | **581** |
| 6 | 528 | 76,200 | 5,500 | 8,500 | 4,500 | **94,700** | **751** |
| 7 | 616 | 87,800 | 8,000 | 11,000 | 6,500 | **113,300** | **900** |
| 8 | 704 | 97,500 | 10,500 | 13,500 | 8,500 | **130,000** | **1,034** |
| 9 | 792 | 105,200 | 12,500 | 15,000 | 9,500 | **142,200** | **1,132** |
| 10 | 880 | 110,300 | 15,000 | 16,500 | 10,500 | **152,300** | **1,210** |
| 11 | 968 | 113,500 | 17,500 | 17,500 | 11,200 | **159,700** | **1,262** |
| 12 | 1,040 | 115,800 | 19,700 | 18,000 | 12,000 | **165,500** | **1,296** |

### Purchase breakdown by channel (month 12)

| Channel | Traffic | Visit-to-Purchase | Purchases |
|---|---|---|---|
| Organic content (new + refresh + compound) | 135,500 | 0.68% | 921 |
| AEO referral | 18,000 | 1.37% | 247 |
| Brand lift | 12,000 | 1.56% | 187 |
| **Total incremental** | **165,500** | | **1,296** (+59 existing = 1,355) |
| **Multiple vs. baseline** | | | **23.0x** |

### Financial projection — 20/week

| Metric | Month 6 | Month 12 | Month 18 | Month 24 |
|---|---|---|---|---|
| Incremental purchases/month | 751 | 1,296 | 1,500 | 1,580 |
| Monthly LTV created | $52,570 | $90,720 | $105,000 | $110,600 |
| Monthly engagement cost | $65,000 | $65,000 | $65,000 | $65,000 |
| Monthly net cash flow | -$12,430 | +$25,720 | +$40,000 | +$45,600 |
| Cumulative investment | $390,000 | $780,000 | $1,170,000 | $1,560,000 |
| Cumulative LTV created | $115,400 | $453,000 | $1,020,000 | $1,700,000 |
| **Cumulative ROI** | **-70%** | **-42%** | **-13%** | **+9%** |

**Cash-flow positive:** Month 10 (monthly LTV > monthly cost)
**Cumulative breakeven:** ~Month 19
**By month 24:** +9% cumulative ROI, generating $110,600/month LTV against $65,000 cost

### Cost structure — 20/week

| Line Item | Monthly Cost | Notes |
|---|---|---|
| Content lead + strategist | $10,000 | Full-time content lead with strategic capability |
| Writers (10-12 freelance) | $22,000 | 88 pages/month × ~$250/page avg (volume + template pricing) |
| SEO team (2 people) | $8,000 | Full-time technical SEO + content SEO analyst |
| Design + tool development | $8,000 | Calculator UIs, programmatic templates, visual system |
| AEO optimization | $4,000 | AI indexation, structured data, CheckThat, proactive monitoring |
| Project management | $5,000 | GrowthX oversight, editorial workflow, QA |
| Technology / tools / infrastructure | $3,000 | SEMrush, CMS, automation tools, staging environments |
| Content QA / editing | $5,000 | Quality control at scale — fact-checking, brand voice |
| **Total** | **$65,000/month** | **$780,000/year** |

---

## Part 8: Scenario Comparison

### Month 12 comparison

| Metric | 5/week | 10/week | 20/week |
|---|---|---|---|
| Pages published | 260 | 520 | 1,040 |
| Total incremental traffic | 68,400 | 113,500 | 165,500 |
| Traffic per dollar spent/month | 3.1 visits/$1 | 3.0 visits/$1 | 2.5 visits/$1 |
| Incremental purchases | 528 | 886 | 1,296 |
| Purchase multiple vs. baseline | 9.9x | 16.0x | 23.0x |
| Monthly LTV created | $36,960 | $62,020 | $90,720 |
| Monthly cost | $22,000 | $38,000 | $65,000 |
| Monthly margin | $14,960 | $24,020 | $25,720 |
| CPA (month 12 only) | $42 | $43 | $50 |
| Cash-flow positive | Month 8 | Month 9 | Month 10 |
| Cumulative breakeven | Month 16 | Month 17 | Month 19 |

### Efficiency comparison

| Metric | 5/week | 10/week | 20/week |
|---|---|---|---|
| Traffic per page (at maturity) | 263/page | 218/page | 169/page |
| Purchases per page (at maturity) | 2.0/page/mo | 1.7/page/mo | 1.2/page/mo |
| LTV created per dollar invested (12 months) | $0.73 | $0.65 | $0.58 |
| LTV created per dollar invested (24 months) | $1.36 | $1.23 | $1.09 |
| Opportunity coverage (of 1,000) | 26% | 52% | 100%+ |

**Key insight:** 5/week has the highest per-page and per-dollar efficiency because it cherry-picks only the top 260 opportunities. But 10/week generates the most absolute monthly margin ($24,020 vs $14,960) while maintaining good efficiency. 20/week delivers the most traffic and purchases but at diminishing returns per dollar.

### Time to milestones

| Milestone | 5/week | 10/week | 20/week |
|---|---|---|---|
| First 1,000 incremental visits | Month 2 | Month 2 | Month 2 |
| First 100 incremental purchases/month | Month 3 | Month 3 | Month 3 |
| Monthly cash-flow positive | Month 8 | Month 9 | Month 10 |
| 5x baseline (295 purchases/month) | Month 5 | Month 4 | Month 4 |
| 10x baseline (590 purchases/month) | Month 13 | Month 7 | Month 6 |
| 15x baseline (885 purchases/month) | Never (caps ~10x) | Month 12 | Month 8 |
| 20x baseline (1,180 purchases/month) | Never | Month 18+ | Month 10 |
| Cumulative breakeven | Month 16 | Month 17 | Month 19 |

### Scenario decision matrix

| If the priority is... | Choose | Why |
|---|---|---|
| Fastest path to 10x | 20/week | Hits 10x at month 6. Aggressive but fast. |
| Best ROI efficiency | 5/week | Highest per-page and per-dollar returns. Nearly 10x by M12. |
| **Best balance of speed + ROI** | **10/week** | **10x by month 7-8. Strong monthly margin. Good opportunity coverage. Can scale up if validated.** |
| Lowest risk | 5/week | Smallest investment. Breaks even earliest. Still nearly 10x. |
| Maximum competitive moat | 20/week | Covers all 1,000 opportunities. Hard for competitors to match. |

---

## Part 9: The AEO Multiplier

AEO (AI Engine Optimization) is the single largest swing factor in all three scenarios. Simple currently has **zero AI referral traffic** because the site blocks AI indexation.

### AEO ramp by scenario

| Phase | 5/week AEO Traffic | 10/week AEO Traffic | 20/week AEO Traffic |
|---|---|---|---|
| M1-2: Unblock + index | 0-200 | 0-300 | 0-500 |
| M3-4: First citations | 600-1,500 | 1,000-2,500 | 1,500-3,500 |
| M5-6: Building presence | 2,800-4,000 | 4,200-5,800 | 6,000-8,500 |
| M7-9: Compounding | 5,200-7,000 | 7,500-10,200 | 11,000-15,000 |
| M10-12: Accelerating | 7,500-8,000 | 11,000-12,000 | 16,500-18,000 |

**Why more content = more AEO:** Each page is a potential citation target. An AI engine answering "what should I eat to break a 24-hour fast" needs a source — the site with the most comprehensive, authoritative content on that topic gets cited. 20/week builds the largest citation surface.

### AEO purchase contribution (month 12)

| Scenario | AEO Visits | AEO Purchases | % of Total Purchases |
|---|---|---|---|
| 5/week | 8,000 | 110 | 21% |
| 10/week | 12,000 | 164 | 19% |
| 20/week | 18,000 | 247 | 19% |

AEO accounts for ~20% of total purchases across all scenarios — from a channel that currently generates zero. This is the highest-ROI unlock: going from blocked to optimized.

### What accelerates AEO

1. **Unblock AI indexation** (week 1): Remove robots.txt and meta restrictions for AI crawlers
2. **Schema markup** (months 1-2): FAQ, HowTo, and Article structured data on all content
3. **Calculator pages** (months 1-3): Interactive tools are heavily cited by AI
4. **Reddit presence** (months 2+): r/intermittentfasting (2M+ members); Reddit = 40.1% of AI citations
5. **CheckThat monitoring** (month 2+): Track which queries cite Simple vs. competitors

---

## Part 10: Sensitivity Analysis

### Variables with the largest impact

| Variable | Default | +20% Impact on M12 Purchases | -20% Impact | Controllability |
|---|---|---|---|---|
| Visit-to-download rate | 17.5% | +95 purchases | -95 purchases | High (CTA optimization, page design) |
| Content volume (pages produced) | Scenario-dependent | +80-120 purchases | -80-120 purchases | High (budget/team decision) |
| Avg visits/page at peak | Varies by cluster | +90-110 purchases | -90-110 purchases | Medium (content quality, targeting) |
| AEO referral volume | 8-18K/month | +22-49 purchases | -22-49 purchases | Medium (technical + content) |
| Download-to-purchase rate | 3.9% | +65 purchases | -65 purchases | Low (product/pricing) |
| AEO download rate | 35% | +22-49 purchases | -22-49 purchases | Low (product/landing page) |
| Brand lift % | 3% effective | +19-40 purchases | -19-40 purchases | Low (brand equity) |

**Most controllable high-impact variables:** Content volume and visit-to-download rate. Both are within GrowthX + Simple's direct control.

### Bear case (everything goes wrong)

All assumptions at -20%:

| Scenario | M12 Purchases (Bear) | Multiple | Monthly LTV | vs. Cost |
|---|---|---|---|---|
| 5/week | 345 | 6.8x | $24,150 | +$2,150/mo |
| 10/week | 580 | 10.8x | $40,600 | +$2,600/mo |
| 20/week | 855 | 15.5x | $59,850 | -$5,150/mo |

Even in the bear case: 5/week hits nearly 7x and is still cash-flow positive. 10/week still exceeds 10x. Only 20/week runs a monthly deficit in the bear case — but it's building a massive asset.

### Bull case (AEO overperforms + higher conversion)

AEO at +50%, visit-to-download at +20%:

| Scenario | M12 Purchases (Bull) | Multiple | Monthly LTV |
|---|---|---|---|
| 5/week | 720 | 13.2x | $50,400 |
| 10/week | 1,180 | 21.0x | $82,600 |
| 20/week | 1,700 | 29.8x | $119,000 |

The bull case is driven by AEO overperformance. Market AI referral traffic is growing at 527% YoY. If Simple captures even a fraction of that momentum (starting from zero), the bull case is plausible.

---

## Part 11: Revenue & Cost Comparison

### Equivalent ad spend

What would the incremental traffic cost in paid advertising at Simple's organic traffic value of $1.86/visit?

| Scenario | M12 Incremental Visits | Equivalent Ad Spend | vs. Content Cost |
|---|---|---|---|
| 5/week | 68,400 | $127,224/month | 5.8x content cost |
| 10/week | 113,500 | $211,110/month | 5.6x content cost |
| 20/week | 165,500 | $307,830/month | 4.7x content cost |

By month 12, every scenario generates traffic worth 5-6x the monthly content investment in equivalent ad spend.

### Cost per acquisition comparison

| Channel | Monthly Cost | M12 Purchases | CPA | Trend |
|---|---|---|---|---|
| Meta ads (current) | ~$1,000,000 | ~757 (site-wide) | Rising | Increasing |
| Content 5/week (M12) | $22,000 | 528 incremental | **$42** | Decreasing |
| Content 10/week (M12) | $38,000 | 886 incremental | **$43** | Decreasing |
| Content 20/week (M12) | $65,000 | 1,296 incremental | **$50** | Decreasing |

Content CPA drops every month because the asset keeps producing. By month 18:
- 5/week CPA: $32
- 10/week CPA: $35
- 20/week CPA: $43

By month 24:
- 5/week CPA: $29
- 10/week CPA: $32
- 20/week CPA: $41

### Cumulative LTV created (12, 18, 24 months)

| Time Horizon | 5/week | 10/week | 20/week |
|---|---|---|---|
| 12-month cumulative LTV | $192,600 | $297,500 | $453,000 |
| 18-month cumulative LTV | $424,000 | $660,000 | $1,020,000 |
| 24-month cumulative LTV | $720,000 | $1,120,000 | $1,700,000 |
| 12-month investment | $264,000 | $456,000 | $780,000 |
| 18-month investment | $396,000 | $684,000 | $1,170,000 |
| 24-month investment | $528,000 | $912,000 | $1,560,000 |
| **24-month ROI** | **+36%** | **+23%** | **+9%** |

### Asset value at month 24

If Simple stopped investing at month 12, the content would continue generating traffic and purchases. The ongoing value of the content asset (assuming 3-year productive life with gradual decay):

| Scenario | M12 Monthly LTV | 3-Year Residual Value (NPV at 10%) | Total Program Value |
|---|---|---|---|
| 5/week | $36,960/month | ~$920,000 | ~$1,180,000 |
| 10/week | $62,020/month | ~$1,540,000 | ~$2,000,000 |
| 20/week | $90,720/month | ~$2,250,000 | ~$2,700,000 |

The 10/week scenario creates an asset worth ~$2M over its productive life against $456K of investment — 4.4x return on invested capital.

---

## Part 12: What Makes This Work

### The five levers (in order of impact)

**1. Calculators & tool pages (Cluster 6)**
15 tool pages alone can generate 18,000+ monthly visits — more than 3x Simple's current content traffic. These are the single highest-ROI content type and should be prioritized in all scenarios.

**2. Unblocking AI indexation**
Going from zero to something on AEO. The IF space is one of the most heavily queried categories in AI. Simple's existing content would earn citations today if it weren't blocked. This is the highest-leverage technical change.

**3. Topical authority compounding**
Clusters with 15+ pages see 15-20% lifts across all pages. At 10/week, most major clusters reach 15+ pages by month 6, unlocking this multiplier for the second half of the year.

**4. Template content scaling**
"Does X break a fast" (75 pages), "Is X keto" (70 pages), and programmatic nutrition (80 pages) represent 225 pages that follow a repeatable template. Production cost per page is 40-60% lower than bespoke content while maintaining quality. This is what makes 20/week feasible.

**5. Conversion optimization over time**
As Simple's content portfolio grows, the visit-to-download rate should increase because:
- More content means more touchpoints (multi-visit journeys convert higher)
- Better internal linking means more pages per session
- Content builds trust, and trust improves conversion
- App recommendation naturally fits IF content ("track your fast in Simple")

### What could accelerate the model

1. **Quiz funnel optimization:** If 25% of incremental traffic goes through the quiz (1.5% purchase rate but 2.5x LTV of $175), the revenue per visitor increases even if purchase count stays flat.
2. **Seasonal surge:** January is peak for health/fitness. If the content program is ramped by December, the January surge delivers an outsized month.
3. **AEO growing faster than projected:** 527% YoY market growth vs. our conservative projections.
4. **Reddit strategy:** r/intermittentfasting (2M+ members). Reddit = 40.1% of AI citations.
5. **Partner citations:** Getting Simple cited on review sites, expert blogs, and listicle articles drives direct traffic and increases AI citation rates.

### What could slow the model

1. **Technical SEO issues:** Crawl problems, Core Web Vitals, indexation delays.
2. **Content quality misses:** Pages that don't match intent or aren't differentiated.
3. **Google algorithm volatility:** Mitigated by building genuine topical authority across 20 clusters.
4. **Lower conversion rates:** If visit-to-download is closer to 12% than 17.5%, purchases drop ~30%.
5. **Competitive response:** If Fastic, Zero, or Lasta aggressively invest in content simultaneously.

---

## Part 13: Recommendation

### Start at 10 pages/week

The 10/week scenario is the recommended starting point because:

1. **Reaches 10x by month 7-8** — fast enough to demonstrate ROI within two quarters
2. **Best monthly margin** — $24,020/month by M12, highest absolute margin of any scenario
3. **Good efficiency** — 218 visits/page and $0.65 LTV per dollar, only 12% less efficient than 5/week
4. **52% opportunity coverage** — addresses the most important half of the 1,000-opportunity inventory
5. **Scalable** — if first cohorts validate, scaling to 20/week in Q3 captures the remaining opportunity
6. **Competitive moat** — publishes enough content to establish dominance in core clusters before competitors can respond

### Phased approach

| Phase | Timeline | Pace | Investment | Milestone |
|---|---|---|---|---|
| **Phase 1: Validate** | Months 1-3 | 10/week | $38K/month | First cohorts ranking. AEO unblocked. Calculators live. |
| **Phase 2: Scale** | Months 4-6 | 10→15/week | $38-50K/month | 5x baseline achieved. Topical authority building. |
| **Phase 3: Accelerate** | Months 7-9 | 15→20/week (if validated) | $50-65K/month | 10x achieved. Expand into Tier 3 clusters. |
| **Phase 4: Optimize** | Months 10-12 | 15-20/week + refresh | $50-65K/month | Maximize existing pages. Full programmatic rollout. |

This phased approach starts at $38K/month, validates the model with real data, and only scales investment after proving the assumptions. If the first cohorts underperform by >30%, the plan adjusts downward without having committed to the full 20/week budget.

---

## Appendix: Math Behind the Model

### Organic search purchase calculation

```
Monthly organic purchases = Σ (Pages in cohort × Peak traffic/page × Maturation % × 0.80 success) × 0.68% visit-to-purchase
```

### AEO purchase calculation

```
Monthly AEO purchases = AI referral visits × 35% download rate × 3.9% purchase rate
```

### Brand lift purchase calculation

```
Monthly brand purchases = (Previous month total incremental visits × 3% brand lift rate) × 40% download rate × 3.9% purchase rate
```

Delayed 2 months from the traffic that generated the brand awareness.

### Total monthly purchases

```
Total = Organic purchases + AEO purchases + Brand purchases
```

### Monthly LTV

```
Monthly LTV = Total incremental purchases × $70
```

### Cumulative ROI

```
Cumulative ROI = (Cumulative LTV created - Cumulative investment) / Cumulative investment × 100
```

### Topical authority compound

Applied when a cluster has 15+ published pages. All matured pages in that cluster receive a 15-20% traffic lift (modeled at 17.5%). This is conservative relative to research showing 20-40% lifts for topically dense content clusters.

### Data sources

- 1,000 opportunities: SEMrush `domain_organic_unique` (12 domains × 300 pages) + `url_organic` (22 calibration pages)
- Conversion rates: Simple.Life analytics (January 2026 baseline)
- CTR benchmarks: Backlinko / Advanced Web Ranking
- AEO growth rates: Evertune / BrightEdge research (527% YoY market growth)
- Content maturation: GrowthX ROI model defaults, validated against client cohort data
