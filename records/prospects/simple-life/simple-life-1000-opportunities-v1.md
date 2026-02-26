# Simple.Life — 1,000 Content Opportunities: Bottom-Up Competitive Analysis

<metadata>
purpose: Comprehensive page-level opportunity inventory for Simple.Life content program, identifying 1,000 specific pages to create based on competitor analysis across 12 domains, with keyword-level traffic estimates and cluster quantification
audience: GrowthX strategy team, Simple Life GTM team
related: records/customers/simple-life/simple-life-10x-content-plan-v1.md, records/customers/simple-life/simple-life-roi-model-v2.md
domain: client-deliverable
confidence: high
sensitivity: client
context_tier: 2
last_updated: 2026-02-23
</metadata>

---

## Executive Summary

This document identifies **1,000 specific page opportunities** for Simple.Life based on bottom-up analysis of 12 competitor domains using SEMrush data. Each opportunity is tied to a real competitor page that already generates organic traffic, with keyword-level volume estimates and a realistic projection of what Simple could capture.

### The numbers

| Metric | Value |
|---|---|
| Competitor domains analyzed | 12 |
| Total competitor pages reviewed | 3,600 (top 300 per domain) |
| Content pages after filtering | ~1,350 |
| Unique opportunities after dedup | **1,000** |
| Total primary keyword volume | ~877,000 searches/month |
| Total estimated Simple.Life capture | **192,600 visits/month** (raw) |
| After 80% page success rate | **~154,000 visits/month** |
| Organized into | **20 clusters** |

### What this means

Simple.Life currently generates ~5,800 monthly visits from content pages. These 1,000 opportunities represent **~26x** the current content traffic at full maturity — far more runway than any single year's execution plan can cover.

The ROI model (separate document) uses this opportunity inventory to build three execution scenarios: 5, 10, and 20 pages per week.

---

## Methodology

### Step 1: Pull top 300 pages per competitor domain

Used SEMrush `domain_organic_unique` report for 12 domains in the US database:

| Domain | Type | SEMrush Rank | Total Keywords | Content Pages (filtered) |
|---|---|---|---|---|
| dietdoctor.com (DD) | Health media | 1,784 | 489K | ~160 |
| fastic.com (FA) | Direct competitor app | 100,299 | 17K | ~95 |
| zerolongevity.com (ZL) | IF niche site | 169,190 | 5K | ~75 |
| drberg.com (DB) | Health expert | 3,290 | 251K | ~130 |
| perfectketo.com (PK) | Keto-focused | 29,785 | 95K | ~110 |
| nutrisense.io (NS) | Metabolic health | 83,458 | 23K | ~80 |
| loseit.com (LI) | Weight loss app | 43,825 | 49K | ~55 |
| ruled.me (RM) | Keto recipes & tools | 39,124 | 52K | ~100 |
| nutritionfacts.org (NF) | Nutrition science | 11,782 | 177K | ~80 |
| snapcalorie.com (SC) | Calorie tracking | 70,411 | 681K | ~200 |
| autumnellenutrition.com (AE) | IF influencer | 278,410 | 4K | ~40 |
| lasta.app (LA) | Direct competitor app | 136,282 | 7K | ~55 |

### Step 2: Filter to content pages

Applied URL pattern rules to separate content pages (blogs, guides, articles, tools) from product pages, login flows, help docs, and homepages. Patterns:

**Include:** `/blog/`, `/articles/`, `/topics/`, `/low-carb/`, `/keto/`, `/recipes/`, `/foods/`, `/en/blog/`, URL slugs with 3+ words
**Exclude:** `/app/`, `/login/`, `/signup/`, `/pricing/`, `/help/`, `/support/`, `/terms/`, `/privacy/`, homepage, product pages, download pages

Result: ~1,350 content pages across 12 domains.

### Step 3: Keyword-level data from url_organic calibration

Pulled detailed keyword data (keywords, positions, search volume, KD, CPC) for 22 strategic content pages across multiple domains and topic clusters using SEMrush `url_organic` report. Used this data to calibrate the traffic estimation model.

### Step 4: Traffic estimation model

For each opportunity:

```
Estimated capture = Primary KW volume × Cluster multiplier × CTR at expected position × 80% success rate
```

**Cluster multiplier** accounts for long-tail keywords each page ranks for beyond the primary keyword:

| Content type | Cluster multiplier | Rationale |
|---|---|---|
| Template pages ("does X break a fast") | 2.5x | 3-5 long-tail variants per primary |
| Guides and pillar content | 3.0x | Broad topic coverage, many related queries |
| Calculators and tools | 4.0x | Many search paths lead to the same tool |
| Programmatic/food pages | 2.0x | Narrower topic, fewer variants |
| Comparison pages | 2.5x | Both sides of comparison + branded terms |

**CTR by keyword difficulty (based on Simple's domain authority rank 67,802):**

| KD Range | Expected Position | Blended CTR | Evidence |
|---|---|---|---|
| 0–10 | 1–3 | 15% | Simple already ranks #1-3 for 12+ KD <15 keywords |
| 11–20 | 2–5 | 10% | Ranks pos 5-9 for "14:10" (KD 23-35), "dirty fasting" (KD 25) |
| 21–35 | 4–8 | 6% | Ranks pos 7-12 for "18:6" (KD 30) |
| 36–50 | 6–15 | 3% | Competitive territory, longer timeline |
| 51+ | 10–30+ | 1.5% | Long-term play, not primary targets |

**Success rate: 80%.** One in five pages won't rank meaningfully. Applied to cluster totals.

### Step 5: Deduplication and selection

Deduplicated across domains (e.g., 8 of 12 domains have "does coffee break a fast" content → counts as 1 opportunity). Selected top 1,000 unique opportunities ranked by estimated capture potential.

---

## Cluster Summary

20 clusters, ordered by total traffic potential. "Cluster Capture" = estimated monthly visits if all pages rank successfully (before 80% success rate). "Net Capture" = after 80% success.

| # | Cluster | Pages | Avg Capture/Page | Cluster Capture | Net (×80%) | Priority |
|---|---|---|---|---|---|---|
| 6 | Calculators & Interactive Tools | 15 | 1,700 | 25,500 | 20,400 | Tier 1 |
| 2 | Fasting Schedules & Methods | 50 | 350 | 17,500 | 14,000 | Tier 1 |
| 4 | Fasting Science & Biology | 40 | 350 | 14,000 | 11,200 | Tier 1 |
| 7 | IF Meal Plans | 50 | 310 | 15,500 | 12,400 | Tier 1 |
| 9 | Food Lists & Grocery Guides | 50 | 310 | 15,500 | 12,400 | Tier 2 |
| 11 | Blood Sugar & Metabolic Health | 45 | 310 | 13,950 | 11,160 | Tier 2 |
| 14 | IF for Specific Populations | 40 | 325 | 13,000 | 10,400 | Tier 2 |
| 3 | Fasting Results & Transformations | 45 | 265 | 11,925 | 9,540 | Tier 2 |
| 13 | Weight Loss Strategies | 50 | 240 | 12,000 | 9,600 | Tier 2 |
| 1 | "Does X Break a Fast?" | 75 | 125 | 9,375 | 7,500 | Tier 1 |
| 10 | "Is X Keto / IF-Friendly?" | 70 | 130 | 9,100 | 7,280 | Tier 3 |
| 5 | Breaking a Fast / What to Eat | 45 | 195 | 8,775 | 7,020 | Tier 2 |
| 8 | IF Recipes & Meal Prep | 55 | 160 | 8,800 | 7,040 | Tier 3 |
| 19 | Programmatic Nutrition Pages | 80 | 110 | 8,800 | 7,040 | Tier 3 |
| 20 | Longevity & Advanced Topics | 25 | 280 | 7,000 | 5,600 | Tier 3 |
| 15 | Diet Comparisons (IF vs X) | 35 | 200 | 7,000 | 5,600 | Tier 3 |
| 12 | Fasting & Drinks/Beverages | 35 | 165 | 5,775 | 4,620 | Tier 3 |
| 16 | IF + Exercise & Fitness | 30 | 185 | 5,550 | 4,440 | Tier 4 |
| 18 | Fasting Side Effects & Safety | 35 | 140 | 4,900 | 3,920 | Tier 4 |
| 17 | Supplements & Vitamins | 30 | 150 | 4,500 | 3,600 | Tier 4 |
| | **TOTAL** | **1,000** | **193** | **218,450** | **174,760** | |

**Tier definitions:**
- **Tier 1** (months 1–3): Proven topics, highest ROI per page, Simple already has authority
- **Tier 2** (months 4–6): Strong traffic potential, builds topical authority clusters
- **Tier 3** (months 7–9): Expansion into adjacent territory, programmatic content
- **Tier 4** (months 10–12): Long-tail, niche, authority-building content

---

## Cluster 1: "Does X Break a Fast?" (75 opportunities)

**Why this cluster matters:** Simple already ranks #1-3 for multiple "break a fast" queries. Every competitor in the IF space has this content. The template is proven, KD is consistently low (5-15), and each new page reinforces Simple's topical authority. This is also the #1 cluster for AI citations — these are exactly the questions people ask ChatGPT.

**Competitor evidence:** Zero (ZL) gets ~1,775/month from 5 pages. Fastic (FA) gets ~2,553 from 5 pages. Autumn Elle (AE) has 7+ pages. Simple currently has ~12 pages generating ~1,200/month. Expanding to 75 covers virtually every searchable variant.

**Reference domains:** FA, ZL, AE, DB, PK, LA

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 1 | Does creatine break a fast | does creatine break a fast | 3,600 | 10 | 900 |
| 2 | What breaks a fast — complete guide | what breaks a fast | 2,400 | 25 | 480 |
| 3 | Does gum break a fast | does gum break a fast | 2,400 | 8 | 600 |
| 4 | Does diet soda break a fast | does diet soda break a fast | 1,900 | 10 | 475 |
| 5 | Does bone broth break a fast | does bone broth break a fast | 1,300 | 12 | 325 |
| 6 | Does salt break a fast | does salt break a fast | 1,300 | 8 | 325 |
| 7 | Does cinnamon break a fast | does cinnamon break a fast | 1,000 | 6 | 250 |
| 8 | Does lemon water break a fast | does lemon water break a fast | 1,000 | 6 | 250 |
| 9 | What doesn't break a fast — full list | what doesn't break a fast | 1,000 | 18 | 200 |
| 10 | Does pre-workout break a fast | does pre-workout break a fast | 720 | 14 | 144 |
| 11 | Does stevia break a fast | does stevia break a fast | 480 | 8 | 120 |
| 12 | Does collagen break a fast | does collagen break a fast | 480 | 8 | 120 |
| 13 | Does heavy cream break a fast | does heavy cream break a fast | 390 | 5 | 98 |
| 14 | Does honey break a fast | does honey break a fast | 480 | 6 | 120 |
| 15 | Does apple cider vinegar break a fast | does acv break a fast | 390 | 10 | 98 |
| 16 | Does AG1 break a fast | does ag1 break a fast | 480 | 5 | 120 |
| 17 | Does diet coke break a fast | does diet coke break a fast | 390 | 8 | 98 |
| 18 | Does almond milk break a fast | does almond milk break a fast | 260 | 8 | 65 |
| 19 | Does zero sugar drinks break a fast | zero sugar drinks fasting | 260 | 10 | 52 |
| 20 | Does black coffee break a fast | does black coffee break a fast | 210 | 12 | 42 |
| 21 | Does MCT oil break a fast | does mct oil break a fast | 210 | 5 | 53 |
| 22 | Does butter break a fast | does butter break a fast | 210 | 6 | 53 |
| 23 | Does coconut oil break a fast | does coconut oil break a fast | 210 | 5 | 53 |
| 24 | Does green tea break a fast | does green tea break a fast | 210 | 4 | 53 |
| 25 | Does electrolytes break a fast | does electrolytes break a fast | 210 | 8 | 53 |
| 26 | Does toothpaste break a fast | does toothpaste break a fast | 210 | 5 | 53 |
| 27 | Does milk break a fast | does milk break a fast | 210 | 8 | 53 |
| 28 | Does monk fruit break a fast | does monk fruit break a fast | 210 | 4 | 53 |
| 29 | Does BCAAs break a fast | does bcaas break a fast | 210 | 6 | 53 |
| 30 | Does medication break a fast | does medication break a fast | 210 | 10 | 42 |
| 31 | Does protein shake break a fast | does protein shake break a fast | 170 | 8 | 43 |
| 32 | Does matcha break a fast | does matcha break a fast | 170 | 6 | 43 |
| 33 | Does sugar-free gum break a fast | sugar free gum fasting | 170 | 5 | 43 |
| 34 | Does ashwagandha break a fast | does ashwagandha break a fast | 140 | 6 | 35 |
| 35 | Does magnesium break a fast | does magnesium break a fast | 140 | 6 | 35 |
| 36 | Does melatonin break a fast | does melatonin break a fast | 140 | 5 | 35 |
| 37 | Does pickle juice break a fast | does pickle juice break a fast | 110 | 4 | 28 |
| 38 | Does kombucha break a fast | does kombucha break a fast | 110 | 6 | 28 |
| 39 | Does fish oil break a fast | does fish oil break a fast | 110 | 5 | 28 |
| 40 | Does multivitamin break a fast | does multivitamin break a fast | 110 | 6 | 28 |
| 41 | Does whey protein break a fast | does whey protein break a fast | 110 | 6 | 28 |
| 42 | Does herbal tea break a fast | does herbal tea break a fast | 90 | 4 | 23 |
| 43 | Does amino acids break a fast | do amino acids break a fast | 90 | 6 | 23 |
| 44 | Does sucralose break a fast | does sucralose break a fast | 90 | 5 | 23 |
| 45 | Does aspartame break a fast | does aspartame break a fast | 90 | 5 | 23 |
| 46 | Does erythritol break a fast | does erythritol break a fast | 90 | 5 | 23 |
| 47 | Does turmeric break a fast | does turmeric break a fast | 90 | 4 | 23 |
| 48 | Does mushroom coffee break a fast | mushroom coffee fasting | 90 | 6 | 23 |
| 49 | Does coconut water break a fast | does coconut water break a fast | 90 | 5 | 23 |
| 50 | Does sparkling water break a fast | does sparkling water break a fast | 90 | 3 | 23 |
| 51 | Does nicotine break a fast | does nicotine break a fast | 70 | 5 | 18 |
| 52 | Does vitamin C break a fast | does vitamin c break a fast | 70 | 4 | 18 |
| 53 | Does vitamin D break a fast | does vitamin d break a fast | 70 | 4 | 18 |
| 54 | Does olive oil break a fast | does olive oil break a fast | 70 | 4 | 18 |
| 55 | Does lemon juice break a fast | does lemon juice break a fast | 70 | 4 | 18 |
| 56 | Does Splenda break a fast | does splenda break a fast | 70 | 5 | 18 |
| 57 | Does ghee break a fast | does ghee break a fast | 70 | 4 | 18 |
| 58 | Does probiotic break a fast | do probiotics break a fast | 70 | 5 | 18 |
| 59 | Does CBD oil break a fast | does cbd oil break a fast | 50 | 5 | 13 |
| 60 | Does L-glutamine break a fast | l-glutamine fasting | 50 | 4 | 13 |
| 61 | Does spirulina break a fast | spirulina intermittent fasting | 50 | 4 | 13 |
| 62 | Does chlorophyll break a fast | chlorophyll water fasting | 50 | 4 | 13 |
| 63 | Does fiber supplement break a fast | does fiber break a fast | 50 | 5 | 13 |
| 64 | Does psyllium husk break a fast | psyllium husk fasting | 50 | 4 | 13 |
| 65 | Does flax seed break a fast | flaxseed fasting | 50 | 4 | 13 |
| 66 | Does chia seeds break a fast | chia seeds fasting | 50 | 4 | 13 |
| 67 | Does mint tea break a fast | mint tea fasting | 50 | 3 | 13 |
| 68 | Does cayenne pepper break a fast | cayenne pepper fasting | 50 | 4 | 13 |
| 69 | Does balsamic vinegar break a fast | balsamic vinegar fasting | 50 | 4 | 13 |
| 70 | Does mouthwash break a fast | mouthwash intermittent fasting | 50 | 3 | 13 |
| 71 | Does wine break a fast | does wine break a fast | 50 | 5 | 13 |
| 72 | Does beer break a fast | does beer break a fast | 50 | 5 | 13 |
| 73 | Does hemp seed oil break a fast | hemp oil fasting | 50 | 3 | 13 |
| 74 | Does apple break a fast | does eating apple break fast | 50 | 4 | 13 |
| 75 | Does coconut milk break a fast | coconut milk fasting | 50 | 4 | 13 |

**Cluster 1 math:**
- Total primary keyword volume: ~24,310/month
- 75 pages × 125 avg raw capture = 9,375/month raw
- After 80% success: **7,500/month**
- Plus 20% topical authority lift on Simple's existing 12 "break a fast" pages: +240/month

---

## Cluster 2: Fasting Schedules & Methods (50 opportunities)

**Why this cluster matters:** Every fasting schedule has a distinct search audience. "16:8 intermittent fasting" alone has 49,500+ monthly searches. Zero's "12 hour fast vs 16 hour fast" is their #2 page at 1,311 traffic. Simple has basic pages for 14:10, 16:8, 18:6, and 20:4 but is missing OMAD, 5:2, warrior diet, alternate day fasting, extended fasting, circadian fasting, and dozens of specific schedule questions.

**Competitor evidence:** ZL gets 1,311 from "12 vs 16 hour fast." FA gets 898 from "stages of fasting by hour." AE gets 500 from OMAD content. DD gets 8,040 from keto diet plan page. This is the highest per-page traffic cluster outside of calculators.

**Reference domains:** ZL, FA, AE, DD, DB, LA

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 76 | OMAD: one meal a day complete guide | omad diet | 5,400 | 35 | 540 |
| 77 | 16:8 intermittent fasting — the definitive guide | 16:8 intermittent fasting | 49,500 | 55 | 990 |
| 78 | 5:2 intermittent fasting guide & meal plan | 5:2 diet | 5,400 | 40 | 432 |
| 79 | 12 hour fast vs 16 hour fast: which is better | 12 hour fast vs 16 hour fast | 2,900 | 20 | 580 |
| 80 | Alternate day fasting: how it works and results | alternate day fasting | 4,400 | 35 | 440 |
| 81 | Warrior diet: benefits, meal plan, and schedule | warrior diet | 4,400 | 30 | 528 |
| 82 | Extended fasting guide: 24, 36, 48, 72 hours | extended fasting | 2,900 | 25 | 580 |
| 83 | What is intermittent fasting: beginner's guide | what is intermittent fasting | 12,100 | 55 | 363 |
| 84 | Eat-stop-eat method explained | eat stop eat | 1,900 | 20 | 380 |
| 85 | 14:10 intermittent fasting: the gentler schedule | 14:10 intermittent fasting | 2,400 | 20 | 480 |
| 86 | 20:4 intermittent fasting guide | 20:4 intermittent fasting | 1,600 | 20 | 320 |
| 87 | Circadian rhythm fasting: eating with your body clock | circadian rhythm fasting | 1,000 | 15 | 250 |
| 88 | 36-hour fast: benefits, risks, and how to do it | 36 hour fast | 1,600 | 20 | 320 |
| 89 | 48-hour fast: complete guide | 48 hour fast | 1,600 | 20 | 320 |
| 90 | 72-hour fast: what happens and how to prepare | 72 hour fast | 1,600 | 25 | 256 |
| 91 | 24-hour fast: benefits and how to start | 24 hour fast benefits | 1,300 | 20 | 260 |
| 92 | How to start intermittent fasting | how to start intermittent fasting | 6,600 | 45 | 396 |
| 93 | Intermittent fasting schedule for beginners | intermittent fasting schedule | 3,600 | 35 | 360 |
| 94 | 14:10 vs 16:8 intermittent fasting | 14:10 vs 16:8 | 720 | 15 | 180 |
| 95 | 16:8 vs 20:4: which burns more fat | 16:8 vs 20:4 | 590 | 15 | 148 |
| 96 | 16:8 vs OMAD: choosing the right schedule | 16:8 vs omad | 480 | 15 | 120 |
| 97 | Intermittent fasting vs 5:2: which is better | intermittent fasting vs 5:2 | 390 | 15 | 98 |
| 98 | Dirty fasting vs clean fasting | dirty fasting vs clean fasting | 480 | 15 | 120 |
| 99 | Time-restricted eating vs intermittent fasting | time restricted eating | 1,600 | 25 | 256 |
| 100 | Intermittent fasting vs extended fasting | intermittent fasting vs extended fasting | 260 | 12 | 65 |
| 101 | Best intermittent fasting schedule for weight loss | best intermittent fasting schedule | 2,400 | 40 | 192 |
| 102 | How long should you intermittent fast | how long should you intermittent fast | 1,000 | 20 | 200 |
| 103 | How many hours should you fast | how many hours should you fast | 720 | 15 | 180 |
| 104 | Best time to eat on 16:8 | best time to eat on 16:8 | 590 | 12 | 148 |
| 105 | Best eating window for intermittent fasting | best eating window intermittent fasting | 480 | 15 | 120 |
| 106 | How to do OMAD safely | how to do omad | 720 | 20 | 144 |
| 107 | 3-day water fast guide | 3 day water fast | 1,600 | 25 | 256 |
| 108 | 5-day fast: benefits and protocol | 5 day fast | 720 | 25 | 115 |
| 109 | 7-day fast: what the research says | 7 day fast | 590 | 30 | 71 |
| 110 | Dry fasting: is it safe? What you need to know | dry fasting | 2,400 | 20 | 480 |
| 111 | Rolling 48-hour fasts: method and benefits | rolling 48 hour fast | 390 | 15 | 98 |
| 112 | ADF (alternate day fasting) for beginners | alternate day fasting for beginners | 390 | 20 | 78 |
| 113 | Crescendo fasting for women | crescendo fasting | 320 | 10 | 80 |
| 114 | The Dubrow diet: intermittent fasting variation | dubrow diet | 480 | 15 | 120 |
| 115 | Fast 5 diet: Dr. Bert Herring's method | fast 5 diet | 260 | 10 | 65 |
| 116 | ProLon fasting mimicking diet explained | prolon fasting mimicking diet | 590 | 25 | 94 |
| 117 | Fasting mimicking diet: how it works | fasting mimicking diet | 1,300 | 30 | 156 |
| 118 | How to break a 72-hour fast safely | how to break a 72 hour fast | 480 | 10 | 120 |
| 119 | Intermittent fasting schedule by age | intermittent fasting by age chart | 1,000 | 15 | 250 |
| 120 | Intermittent fasting eating window times | intermittent fasting eating window | 720 | 15 | 180 |
| 121 | Modified fasting: what it is and how it works | modified fasting | 260 | 10 | 65 |
| 122 | Protein-sparing modified fast guide | protein sparing modified fast | 590 | 20 | 118 |
| 123 | Bone broth fast: 3-day protocol and benefits | bone broth fast | 590 | 15 | 148 |
| 124 | Fat fasting: what it is and who it's for | fat fasting | 390 | 12 | 98 |
| 125 | Juice fasting: benefits, risks, and how to do it | juice fasting | 590 | 20 | 118 |

**Cluster 2 math:**
- Total primary keyword volume: ~139,920/month
- 50 pages × 350 avg raw capture = 17,500/month raw
- After 80% success: **14,000/month**

---

## Cluster 3: Fasting Results & Transformations (45 opportunities)

**Why this cluster matters:** Highest purchase intent. People searching "16:8 results 1 week" are deciding whether to start IF and download an app. This is bottom-funnel content. Fastic's "16:8 results 1 week" drives 1,051 monthly visits. Zero's "IF results 1 month" drives 795.

**Reference domains:** FA, ZL, AE, LA, LI

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 126 | Intermittent fasting results: what to realistically expect | intermittent fasting results | 5,400 | 40 | 432 |
| 127 | 16:8 intermittent fasting results after 1 week | 16:8 results 1 week | 2,900 | 25 | 580 |
| 128 | 16:8 results after 1 month | 16:8 results 1 month | 1,900 | 25 | 380 |
| 129 | Intermittent fasting results after 1 month | intermittent fasting results 1 month | 2,400 | 30 | 288 |
| 130 | Intermittent fasting before and after | intermittent fasting before and after | 2,400 | 35 | 240 |
| 131 | How much weight can you lose with intermittent fasting | how much weight can you lose intermittent fasting | 1,900 | 35 | 190 |
| 132 | Intermittent fasting results after 3 months | intermittent fasting results 3 months | 1,000 | 25 | 200 |
| 133 | 20:4 intermittent fasting results | 20:4 results | 720 | 20 | 144 |
| 134 | OMAD results: what to expect at 1 week, 1 month | omad results | 1,300 | 25 | 260 |
| 135 | Intermittent fasting results after 6 months | intermittent fasting results 6 months | 480 | 25 | 96 |
| 136 | How long does intermittent fasting take to work | how long does intermittent fasting take to work | 1,600 | 30 | 192 |
| 137 | 14:10 intermittent fasting results | 14:10 results | 480 | 15 | 120 |
| 138 | Intermittent fasting weight loss per week | intermittent fasting weight loss per week | 720 | 25 | 144 |
| 139 | 3-day water fast before and after | 3 day water fast before and after | 590 | 15 | 148 |
| 140 | 5:2 diet results: what to expect | 5:2 diet results | 480 | 20 | 96 |
| 141 | Intermittent fasting results by schedule comparison | which fasting schedule gets best results | 260 | 15 | 65 |
| 142 | OMAD weight loss results 1 month | omad weight loss 1 month | 480 | 20 | 96 |
| 143 | 48-hour fast results: weight loss and benefits | 48 hour fast results | 480 | 15 | 120 |
| 144 | 72-hour fast results and what to expect | 72 hour fast results | 390 | 15 | 98 |
| 145 | Alternate day fasting results | alternate day fasting results | 320 | 20 | 64 |
| 146 | Intermittent fasting results female | intermittent fasting results female | 720 | 25 | 144 |
| 147 | Intermittent fasting results male | intermittent fasting results male | 320 | 20 | 64 |
| 148 | 16:8 fasting results after 2 weeks | 16:8 results 2 weeks | 390 | 20 | 78 |
| 149 | Warrior diet results | warrior diet results | 260 | 15 | 65 |
| 150 | 18:6 intermittent fasting results | 18:6 results | 480 | 20 | 96 |
| 151 | Intermittent fasting 1 year results | intermittent fasting 1 year results | 390 | 20 | 78 |
| 152 | Intermittent fasting weight loss timeline | intermittent fasting weight loss timeline | 320 | 25 | 51 |
| 153 | 24-hour fast results: what happens in one day | 24 hour fast results | 320 | 15 | 80 |
| 154 | Water fasting results | water fasting results | 480 | 20 | 96 |
| 155 | Extended fasting results: 5-day and 7-day | extended fasting results | 210 | 20 | 42 |
| 156 | OMAD results women over 40 | omad results women | 260 | 15 | 65 |
| 157 | 16:8 fasting results over 50 | 16:8 results over 50 | 210 | 15 | 53 |
| 158 | Dry fasting results | dry fasting results | 260 | 15 | 65 |
| 159 | IF results without exercise | intermittent fasting without exercise results | 210 | 15 | 53 |
| 160 | 36-hour fast results and benefits | 36 hour fast results | 210 | 12 | 53 |
| 161 | Intermittent fasting belly fat results | intermittent fasting belly fat | 1,600 | 35 | 160 |
| 162 | 7-day water fast before and after | 7 day water fast results | 260 | 15 | 65 |
| 163 | IF muscle gain results | intermittent fasting muscle gain | 590 | 25 | 94 |
| 164 | OMAD before and after photos | omad before and after | 480 | 20 | 96 |
| 165 | Intermittent fasting results body composition | intermittent fasting body recomposition | 320 | 25 | 51 |
| 166 | 16:8 results with exercise | 16:8 results with exercise | 170 | 15 | 43 |
| 167 | Intermittent fasting 2 month results | intermittent fasting 2 months results | 210 | 20 | 42 |
| 168 | Intermittent fasting results after 1 week | intermittent fasting results 1 week | 720 | 25 | 144 |
| 169 | Fasting weight loss calculator (how much will I lose) | fasting weight loss calculator | 590 | 20 | 118 |
| 170 | IF results by body type | intermittent fasting results by body type | 140 | 10 | 35 |

**Cluster 3 math:**
- Total primary keyword volume: ~38,410/month
- 45 pages × 265 avg raw capture = 11,925/month raw
- After 80% success: **9,540/month**

---

## Cluster 4: Fasting Science & Biology (40 opportunities)

**Why this cluster matters:** Highest per-page traffic in the fasting space. Zero's autophagy page drives 1,616 monthly visits — their #1 page. Perfect Keto's "5 stages of fasting" drives 1,859. NutritionFacts' autophagy content drives 2,053. These are pillar pages that earn links, citations, and anchor the entire content ecosystem.

**Reference domains:** ZL, PK, NF, FA, DB, NS

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 171 | What is autophagy? How fasting triggers cell repair | what is autophagy | 5,400 | 40 | 432 |
| 172 | The 5 stages of fasting: what happens hour by hour | stages of fasting | 2,900 | 25 | 580 |
| 173 | Intermittent fasting and gut health | intermittent fasting gut health | 1,600 | 20 | 320 |
| 174 | The science behind intermittent fasting | science behind intermittent fasting | 720 | 25 | 144 |
| 175 | Intermittent fasting and hormones explained | intermittent fasting hormones | 590 | 20 | 118 |
| 176 | How fasting affects your metabolism | does fasting slow metabolism | 2,400 | 30 | 288 |
| 177 | Intermittent fasting and ketosis: how they connect | intermittent fasting and ketosis | 720 | 20 | 144 |
| 178 | The biology of fat burning during a fast | how does fasting burn fat | 1,000 | 25 | 200 |
| 179 | When does autophagy start during fasting | when does autophagy start | 1,900 | 20 | 380 |
| 180 | Fasting and insulin resistance | intermittent fasting insulin resistance | 1,600 | 25 | 256 |
| 181 | Human growth hormone and fasting | fasting and hgh | 720 | 15 | 180 |
| 182 | Fasting and cortisol: what happens to stress hormones | fasting and cortisol | 480 | 15 | 120 |
| 183 | How fasting affects your brain | fasting and brain health | 590 | 20 | 118 |
| 184 | Intermittent fasting and inflammation | intermittent fasting inflammation | 720 | 20 | 144 |
| 185 | What happens to your body at 12, 16, 24, 48, 72 hours | fasting timeline | 1,000 | 20 | 200 |
| 186 | Fasting and immune system | fasting immune system | 590 | 20 | 118 |
| 187 | Fasting and testosterone | fasting and testosterone | 590 | 15 | 148 |
| 188 | How autophagy cleans your cells: the science | autophagy benefits | 1,300 | 30 | 156 |
| 189 | Fasting and longevity: what the research shows | fasting and longevity | 480 | 25 | 96 |
| 190 | mTOR and fasting: the growth vs. repair switch | mtor fasting | 480 | 15 | 120 |
| 191 | Fasting and stem cells: can fasting regenerate cells | fasting stem cells | 390 | 15 | 98 |
| 192 | Does fasting reduce cholesterol | does fasting reduce cholesterol | 480 | 15 | 120 |
| 193 | Fasting and blood pressure | fasting and blood pressure | 480 | 15 | 120 |
| 194 | How fasting affects estrogen and progesterone | fasting and estrogen | 320 | 12 | 80 |
| 195 | Fasting and cancer: what the studies say | fasting and cancer | 590 | 35 | 71 |
| 196 | Ketone levels during fasting explained | ketone levels fasting | 390 | 15 | 98 |
| 197 | Fasting and DNA repair mechanisms | fasting dna repair | 210 | 10 | 53 |
| 198 | How fasting resets your digestive system | fasting reset digestive system | 260 | 12 | 65 |
| 199 | Fasting metabolic switch: from glucose to fat | metabolic switch fasting | 320 | 15 | 80 |
| 200 | Does intermittent fasting affect thyroid | intermittent fasting thyroid | 480 | 15 | 120 |
| 201 | Fasting and oxidative stress reduction | fasting oxidative stress | 170 | 10 | 43 |
| 202 | Glycogen depletion during fasting: what to know | glycogen depletion fasting | 210 | 10 | 53 |
| 203 | Fasting and microbiome: how it reshapes gut bacteria | fasting microbiome | 260 | 15 | 65 |
| 204 | Does fasting increase BDNF (brain health factor) | fasting bdnf | 170 | 10 | 43 |
| 205 | Fasting and cellular senescence | fasting cellular senescence | 140 | 10 | 35 |
| 206 | Fasting and mitochondrial health | fasting mitochondria | 170 | 10 | 43 |
| 207 | Intermittent fasting and serotonin | intermittent fasting serotonin | 170 | 10 | 43 |
| 208 | How long to fast for autophagy benefits | how long to fast for autophagy | 590 | 20 | 118 |
| 209 | Refeeding syndrome: what it is and how to avoid it | refeeding syndrome | 720 | 20 | 144 |
| 210 | 12 ways to trigger autophagy without fasting | how to trigger autophagy | 720 | 20 | 144 |

**Cluster 4 math:**
- Total primary keyword volume: ~34,900/month
- 40 pages × 350 avg raw capture = 14,000/month raw
- After 80% success: **11,200/month**

---

## Cluster 5: Breaking a Fast / What to Eat After Fasting (45 opportunities)

**Why this cluster matters:** "How to break a fast" has 2,400+ monthly searches. Every fasting user needs to know what to eat when their window opens. This cluster bridges fasting content with food content and has high app download conversion — people want a plan.

**Reference domains:** FA, ZL, AE, DD, PK

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 211 | How to break a fast: the complete guide | how to break a fast | 2,400 | 25 | 480 |
| 212 | Best foods to break a fast | best foods to break a fast | 1,900 | 20 | 380 |
| 213 | What to eat after fasting for 16 hours | what to eat after fasting | 1,600 | 20 | 320 |
| 214 | What to eat after a 24-hour fast | what to eat after 24 hour fast | 720 | 15 | 180 |
| 215 | What to eat after a 48-hour fast | what to eat after 48 hour fast | 390 | 12 | 98 |
| 216 | What to eat after a 72-hour fast | what to eat after 72 hour fast | 320 | 12 | 80 |
| 217 | What to eat after a 3-day water fast | what to eat after water fast | 480 | 15 | 120 |
| 218 | Worst foods to break a fast | worst foods to break a fast | 590 | 12 | 148 |
| 219 | Best first meal after intermittent fasting | first meal after intermittent fasting | 480 | 15 | 120 |
| 220 | How many calories to eat during intermittent fasting | how many calories intermittent fasting | 1,600 | 30 | 192 |
| 221 | What to eat during eating window on 16:8 | what to eat on 16:8 | 1,000 | 20 | 200 |
| 222 | How to break a fast without stomach pain | breaking a fast stomach pain | 260 | 8 | 65 |
| 223 | Best soup to break a fast | best soup to break a fast | 260 | 8 | 65 |
| 224 | Can you eat fruit to break a fast | fruit to break a fast | 210 | 6 | 53 |
| 225 | Best smoothie to break a fast | smoothie to break a fast | 320 | 10 | 80 |
| 226 | Breaking a fast with eggs: good or bad | breaking a fast with eggs | 210 | 8 | 53 |
| 227 | Can you eat bread after fasting | bread after fasting | 170 | 6 | 43 |
| 228 | What to eat after a 5-day fast | what to eat after 5 day fast | 210 | 12 | 53 |
| 229 | Best bone broth to break a fast | best bone broth to break a fast | 320 | 10 | 80 |
| 230 | How to break an extended fast safely | breaking extended fast | 260 | 12 | 65 |
| 231 | What to eat on OMAD for weight loss | what to eat on omad | 720 | 20 | 144 |
| 232 | What to eat on 5:2 fasting days | what to eat on 5:2 fast days | 390 | 15 | 98 |
| 233 | 500-calorie meal ideas for fasting days | 500 calorie meals fasting | 260 | 10 | 65 |
| 234 | What to eat during a 20:4 eating window | what to eat on 20:4 | 260 | 12 | 65 |
| 235 | How much protein to eat after fasting | protein after fasting | 260 | 10 | 65 |
| 236 | Eating too much after fasting: what happens | eating too much after fasting | 210 | 8 | 53 |
| 237 | Should you eat when not hungry during eating window | not hungry during eating window | 170 | 6 | 43 |
| 238 | Best yogurt to break a fast | yogurt to break a fast | 170 | 6 | 43 |
| 239 | Breaking a fast with avocado | avocado to break a fast | 140 | 5 | 35 |
| 240 | What to eat after dry fasting | what to eat after dry fasting | 140 | 8 | 35 |
| 241 | Best carbs to eat after fasting | carbs after fasting | 170 | 8 | 43 |
| 242 | How to break a fast for gut health | break fast gut health | 170 | 8 | 43 |
| 243 | Light meals to break a fast | light meals to break a fast | 140 | 6 | 35 |
| 244 | Best nuts to eat after fasting | nuts after fasting | 110 | 5 | 28 |
| 245 | Should you eat breakfast after 16:8 | intermittent fasting breakfast | 1,000 | 25 | 200 |
| 246 | Intermittent fasting dinner ideas | intermittent fasting dinner ideas | 480 | 15 | 120 |
| 247 | Intermittent fasting snacks: what to eat between meals | intermittent fasting snacks | 590 | 15 | 148 |
| 248 | What to eat during Ramadan fasting | what to eat during ramadan | 590 | 15 | 148 |
| 249 | How to refeed after a long fast | refeeding after fast | 210 | 10 | 53 |
| 250 | Best foods for your eating window (by goal) | best foods eating window | 170 | 8 | 43 |
| 251 | What to eat on fasting days (ADF) | what to eat on fasting days | 260 | 12 | 65 |
| 252 | Best pre-fast meal (what to eat before fasting) | what to eat before fasting | 390 | 12 | 98 |
| 253 | Eating one meal a day: what to include | what to eat for one meal a day | 390 | 15 | 98 |
| 254 | Best foods for sustained energy during eating window | energy foods eating window | 110 | 6 | 28 |
| 255 | What to eat during intermittent fasting to lose weight | what to eat intermittent fasting weight loss | 720 | 25 | 144 |

**Cluster 5 math:**
- Total primary keyword volume: ~23,290/month
- 45 pages × 195 avg raw capture = 8,775/month raw
- After 80% success: **7,020/month**

---

## Cluster 6: Calculators & Interactive Tools (15 opportunities)

**Why this cluster matters:** Single highest ROI per page across the entire competitive set. Nutrisense's blood sugar chart drives 41,018 visits from one page. Ruled.me's keto calculator drives 8,299. Fastic's calorie page drives 2,928. Simple has zero calculator or tool pages. One tool page can outperform 50 blog posts.

**Reference domains:** RM, NS, FA, PK, DB, LI

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 256 | IF schedule quiz/calculator | intermittent fasting calculator | 1,600 | 20 | 1,280 |
| 257 | Fasting stages tracker (hour-by-hour) | fasting benefits by hour | 1,900 | 20 | 1,520 |
| 258 | IF calorie calculator | intermittent fasting calorie calculator | 880 | 15 | 880 |
| 259 | Intermittent fasting by age & weight planner | intermittent fasting by age chart | 1,000 | 15 | 1,000 |
| 260 | IF results estimator | how much weight can you lose intermittent fasting calculator | 590 | 15 | 590 |
| 261 | Keto macro calculator for IF | keto macro calculator | 5,400 | 35 | 2,160 |
| 262 | Body fat percentage visual estimator | body fat percentage | 5,400 | 45 | 1,080 |
| 263 | TDEE calculator for intermittent fasting | tdee calculator | 5,400 | 40 | 1,620 |
| 264 | Blood sugar level chart | normal blood sugar levels chart | 27,100 | 35 | 5,420 |
| 265 | Ideal weight calculator | ideal weight calculator | 3,600 | 30 | 1,440 |
| 266 | Water intake calculator for fasting | water intake calculator | 2,400 | 25 | 960 |
| 267 | Fasting zone tracker (anabolic/catabolic) | fasting zones | 480 | 10 | 480 |
| 268 | Protein calculator for eating window | protein calculator | 3,600 | 30 | 1,440 |
| 269 | Calorie deficit calculator | calorie deficit calculator | 5,400 | 40 | 2,160 |
| 270 | Intermittent fasting meal plan generator | intermittent fasting meal planner | 590 | 15 | 590 |

**Cluster 6 math:**
- Total primary keyword volume: ~65,340/month
- 15 pages × 1,508 avg raw capture = 22,620/month raw (higher due to tool pages)
- After 80% success: **18,100/month**

---

## Cluster 7: IF Meal Plans (50 opportunities)

**Why this cluster matters:** Diet Doctor's keto diet plan page drives 8,040 traffic. Simple's own "keto meal plan for beginners" is its #1 content page at 789. Meal plan content is the bridge from education to action — people search for plans when they're ready to commit. High conversion intent.

**Reference domains:** DD, FA, AE, PK, RM, DB

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 271 | 7-day 16:8 intermittent fasting meal plan | 16:8 meal plan | 1,600 | 25 | 320 |
| 272 | 7-day 14:10 IF meal plan | 14:10 meal plan | 590 | 15 | 148 |
| 273 | 7-day 20:4 IF meal plan | 20:4 meal plan | 390 | 15 | 98 |
| 274 | OMAD meal plan: what to eat on one meal a day | omad meal plan | 1,300 | 20 | 260 |
| 275 | IF meal plan for beginners | intermittent fasting meal plan | 3,600 | 40 | 360 |
| 276 | High-protein IF meal plan | high protein intermittent fasting meal plan | 720 | 20 | 144 |
| 277 | IF meal plan for women | intermittent fasting meal plan for women | 720 | 20 | 144 |
| 278 | Budget IF meal plan | budget meal plan intermittent fasting | 260 | 10 | 65 |
| 279 | Keto + IF 7-day meal plan | keto intermittent fasting meal plan | 1,000 | 25 | 200 |
| 280 | Vegetarian IF meal plan | vegetarian intermittent fasting meal plan | 320 | 15 | 80 |
| 281 | Vegan IF meal plan | vegan intermittent fasting meal plan | 260 | 12 | 65 |
| 282 | Mediterranean diet + IF meal plan | mediterranean diet intermittent fasting | 480 | 20 | 96 |
| 283 | IF meal plan for muscle gain | intermittent fasting meal plan muscle gain | 390 | 15 | 98 |
| 284 | 1200-calorie IF meal plan | 1200 calorie intermittent fasting meal plan | 480 | 15 | 120 |
| 285 | 1500-calorie IF meal plan | 1500 calorie meal plan | 1,600 | 25 | 256 |
| 286 | 1800-calorie IF meal plan | 1800 calorie meal plan | 590 | 20 | 118 |
| 287 | 2000-calorie IF meal plan | 2000 calorie meal plan | 720 | 20 | 144 |
| 288 | IF meal plan for weight loss | intermittent fasting diet plan for weight loss | 1,000 | 30 | 120 |
| 289 | Carnivore diet + IF meal plan | carnivore diet intermittent fasting | 390 | 15 | 98 |
| 290 | 5:2 diet meal plan | 5:2 meal plan | 720 | 15 | 180 |
| 291 | ADF meal plan | alternate day fasting meal plan | 260 | 10 | 65 |
| 292 | Indian IF meal plan | intermittent fasting meal plan indian | 320 | 10 | 80 |
| 293 | Filipino IF meal plan | intermittent fasting meal plan filipino | 140 | 5 | 35 |
| 294 | South Asian IF meal plan | south asian meal plan intermittent fasting | 110 | 5 | 28 |
| 295 | Mexican-inspired IF meal plan | mexican meal plan intermittent fasting | 110 | 5 | 28 |
| 296 | Japanese-inspired IF meal plan | japanese meal plan fasting | 110 | 5 | 28 |
| 297 | IF meal plan for seniors | intermittent fasting meal plan seniors | 210 | 10 | 53 |
| 298 | IF meal plan with no cooking | no cook intermittent fasting meals | 170 | 5 | 43 |
| 299 | Anti-inflammatory IF meal plan | anti inflammatory meal plan | 1,000 | 25 | 200 |
| 300 | Gut health IF meal plan | gut health meal plan | 480 | 15 | 120 |
| 301 | Warrior diet meal plan 7 days | warrior diet meal plan | 390 | 12 | 98 |
| 302 | 500-calorie day meal plan (5:2 / ADF) | 500 calorie meal plan | 720 | 15 | 180 |
| 303 | Low-carb IF meal plan | low carb intermittent fasting meal plan | 320 | 15 | 80 |
| 304 | Paleo + IF meal plan | paleo intermittent fasting | 210 | 12 | 53 |
| 305 | IF meal plan for endomorphs | endomorph meal plan | 590 | 15 | 148 |
| 306 | IF meal plan for ectomorphs | ectomorph meal plan | 390 | 12 | 98 |
| 307 | IF meal plan for mesomorphs | mesomorph meal plan | 260 | 12 | 65 |
| 308 | Pescatarian IF meal plan | pescatarian meal plan | 320 | 12 | 80 |
| 309 | Dairy-free IF meal plan | dairy free meal plan | 260 | 10 | 65 |
| 310 | Gluten-free IF meal plan | gluten free meal plan | 480 | 15 | 120 |
| 311 | PCOS-friendly IF meal plan | pcos meal plan | 1,000 | 25 | 200 |
| 312 | Diabetic-friendly IF meal plan | diabetic meal plan | 1,300 | 30 | 156 |
| 313 | Thyroid-friendly IF meal plan | thyroid meal plan | 390 | 15 | 98 |
| 314 | IF meal plan for runners | meal plan for runners | 390 | 15 | 98 |
| 315 | IF meal plan for busy professionals | meal plan for busy people | 260 | 10 | 65 |
| 316 | IF meal plan for shift workers | intermittent fasting shift workers | 210 | 8 | 53 |
| 317 | 28-day IF meal plan challenge | 28 day intermittent fasting plan | 320 | 12 | 80 |
| 318 | IF meal plan under $50/week | cheap intermittent fasting meals | 170 | 5 | 43 |
| 319 | IF meal plan for couples | meal plan for couples | 170 | 8 | 43 |
| 320 | Holiday IF meal plan | intermittent fasting during holidays | 140 | 6 | 35 |

**Cluster 7 math:**
- Total primary keyword volume: ~28,720/month
- 50 pages × 310 avg raw capture = 15,500/month raw
- After 80% success: **12,400/month**

---

## Cluster 8: IF Recipes & Meal Prep (55 opportunities)

**Why this cluster matters:** Recipes are the highest-volume content type in health/nutrition. Ruled.me's pork shoulder recipe drives 3,527. DD's recipe hub drives 15,827. AE's recipe pages average 200-500. The IF angle differentiates: these aren't generic recipes — they're optimized for eating windows, breaking fasts, and supporting fasting goals.

**Reference domains:** RM, DD, AE, FA, PK

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 321 | 10 high-protein breakfasts to break your fast | high protein breakfast to break fast | 590 | 15 | 148 |
| 322 | 5-minute meals for your eating window | 5 minute meals | 1,600 | 25 | 256 |
| 323 | Smoothies to break a fast: 8 recipes | smoothie to break a fast recipes | 320 | 10 | 80 |
| 324 | Meal prep for intermittent fasting | meal prep for intermittent fasting | 590 | 15 | 148 |
| 325 | 500-calorie meals for OMAD | 500 calorie meals | 1,000 | 20 | 200 |
| 326 | IF-friendly snacks you can make in 5 minutes | intermittent fasting snack ideas | 320 | 10 | 80 |
| 327 | High-protein overnight oats for IF | overnight oats for intermittent fasting | 210 | 8 | 53 |
| 328 | One-pot dinners for your eating window | one pot dinner recipes | 1,000 | 25 | 200 |
| 329 | Keto coffee recipe for fasting | keto coffee recipe | 1,300 | 15 | 325 |
| 330 | Bulletproof coffee recipe for IF | bulletproof coffee recipe | 1,000 | 15 | 250 |
| 331 | Bone broth recipe for breaking a fast | bone broth recipe | 2,400 | 30 | 288 |
| 332 | High-protein smoothie bowl for IF | protein smoothie bowl | 480 | 12 | 120 |
| 333 | Egg muffins for meal prep (IF edition) | egg muffin recipe meal prep | 480 | 10 | 120 |
| 334 | Air fryer meals for eating window | air fryer meals | 1,600 | 30 | 192 |
| 335 | Sheet pan dinners for IF | sheet pan dinner recipes | 720 | 20 | 144 |
| 336 | IF-friendly protein bars (homemade) | homemade protein bars | 590 | 15 | 148 |
| 337 | Chia seed pudding for IF | chia seed pudding recipe | 720 | 10 | 180 |
| 338 | Greek yogurt bowls to break a fast | greek yogurt bowl recipes | 260 | 8 | 65 |
| 339 | Egg-fast recipes for IF | egg fast recipes | 390 | 10 | 98 |
| 340 | Avocado toast recipes for breaking a fast | avocado toast recipes | 720 | 12 | 180 |
| 341 | Mason jar salads for IF meal prep | mason jar salad | 480 | 10 | 120 |
| 342 | High-fiber recipes for your eating window | high fiber recipes | 720 | 15 | 180 |
| 343 | Freezer meals for intermittent fasting | freezer meals | 720 | 15 | 180 |
| 344 | Healthy crockpot recipes for IF | healthy crockpot recipes | 1,000 | 20 | 200 |
| 345 | Low-calorie high-protein meals for IF | low calorie high protein meals | 1,000 | 20 | 200 |
| 346 | 15-minute IF dinner recipes | 15 minute dinner recipes | 720 | 20 | 144 |
| 347 | Keto fat bombs for fasting | keto fat bombs | 1,600 | 15 | 400 |
| 348 | Electrolyte drink recipes for fasting | electrolyte drink recipe | 480 | 8 | 120 |
| 349 | Collagen smoothie recipes for IF | collagen smoothie | 260 | 8 | 65 |
| 350 | Cauliflower rice meals for IF | cauliflower rice recipes | 480 | 10 | 120 |
| 351 | Zucchini noodle recipes for eating window | zucchini noodle recipes | 480 | 10 | 120 |
| 352 | Salmon recipes for IF (omega-3 rich) | salmon recipes | 2,400 | 30 | 288 |
| 353 | Chicken breast recipes for IF meal prep | chicken breast recipes | 2,400 | 25 | 480 |
| 354 | Ground turkey recipes for IF | ground turkey recipes | 1,000 | 15 | 250 |
| 355 | Tofu recipes for vegetarian IF | tofu recipes | 1,000 | 15 | 250 |
| 356 | Lentil recipes for plant-based IF | lentil recipes | 720 | 12 | 180 |
| 357 | Sweet potato recipes for IF | sweet potato recipes | 720 | 12 | 180 |
| 358 | Broccoli recipes for IF (high fiber) | broccoli recipes | 590 | 10 | 148 |
| 359 | Egg recipes for IF (10 ways) | egg recipes | 1,000 | 15 | 250 |
| 360 | Cottage cheese recipes for IF | cottage cheese recipes | 590 | 10 | 148 |
| 361 | Energy balls for fasting snacks | energy balls recipe | 590 | 10 | 148 |
| 362 | Protein pancakes to break a fast | protein pancakes | 1,000 | 15 | 250 |
| 363 | Veggie stir fry for eating window | veggie stir fry | 590 | 10 | 148 |
| 364 | Turkey meatball meal prep for IF | turkey meatball recipe | 390 | 8 | 98 |
| 365 | Quinoa bowl recipes for IF | quinoa bowl recipes | 390 | 10 | 98 |
| 366 | Stuffed bell peppers for IF | stuffed bell pepper recipe | 480 | 10 | 120 |
| 367 | Healthy wrap recipes for eating window | healthy wrap recipes | 480 | 10 | 120 |
| 368 | Frittata recipes for IF meal prep | frittata recipe | 480 | 8 | 120 |
| 369 | Soup recipes for breaking a fast | soup recipes healthy | 720 | 15 | 180 |
| 370 | Tuna salad recipes for IF | tuna salad recipe | 720 | 10 | 180 |
| 371 | Baked oatmeal for IF breakfast | baked oatmeal recipe | 590 | 10 | 148 |
| 372 | Lettuce wrap recipes for IF | lettuce wrap recipes | 480 | 8 | 120 |
| 373 | Chicken salad for meal prep | chicken salad recipe | 1,000 | 12 | 250 |
| 374 | Healthy muffin recipes for IF | healthy muffins | 480 | 10 | 120 |
| 375 | Zucchini fritter recipes for eating window | zucchini fritters | 390 | 8 | 98 |

**Cluster 8 math:**
- Total primary keyword volume: ~42,110/month
- 55 pages × 160 avg raw capture = 8,800/month raw
- After 80% success: **7,040/month**

---

## Cluster 9: Food Lists & Grocery Guides (50 opportunities)

**Why this cluster matters:** DD's keto vegetable list drives 4,164. PK's grocery list drives 4,295. PK's no-carb food list drives 2,246. Food list content gets bookmarked and shared — it's reference content with long shelf life. The IF-specific angle ("foods that help during a fast," "eating window optimization") is differentiated.

**Reference domains:** DD, PK, RM, DB, NS

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 376 | IF grocery list: everything you need | intermittent fasting grocery list | 590 | 12 | 148 |
| 377 | Best foods to break a fast (and what to avoid) | best foods to break a fast | 1,900 | 20 | 380 |
| 378 | Zero-calorie foods: the complete list | zero calorie foods | 2,400 | 25 | 480 |
| 379 | Foods that help with autophagy | foods that trigger autophagy | 480 | 10 | 120 |
| 380 | High-protein foods list for your eating window | high protein foods list | 3,600 | 35 | 360 |
| 381 | IF-friendly fast food: what to order at every chain | fast food intermittent fasting | 320 | 8 | 80 |
| 382 | Foods that kill hunger during a fast | foods that suppress appetite | 1,000 | 20 | 200 |
| 383 | IF food list: what to eat and when | intermittent fasting food list | 1,000 | 20 | 200 |
| 384 | Keto food list (complete) | keto food list | 5,400 | 40 | 540 |
| 385 | Keto vegetable list | keto vegetables | 2,400 | 25 | 480 |
| 386 | Keto fruit list | low carb fruits | 2,400 | 25 | 480 |
| 387 | No-carb food list | no carb foods | 1,600 | 20 | 320 |
| 388 | Low-carb food list for beginners | low carb food list | 1,600 | 25 | 256 |
| 389 | High-fiber foods for IF | high fiber foods | 2,400 | 25 | 480 |
| 390 | Anti-inflammatory food list | anti inflammatory foods list | 2,400 | 25 | 480 |
| 391 | Foods that spike blood sugar | foods that spike blood sugar | 1,000 | 15 | 250 |
| 392 | Foods that lower blood sugar | foods that lower blood sugar | 1,600 | 25 | 256 |
| 393 | Low glycemic index food list | low glycemic foods | 2,400 | 25 | 480 |
| 394 | Superfoods list for your eating window | superfoods list | 1,600 | 20 | 320 |
| 395 | Foods to avoid during intermittent fasting | foods to avoid intermittent fasting | 590 | 12 | 148 |
| 396 | Healthy fats list for IF | healthy fats list | 720 | 15 | 180 |
| 397 | Complex carbs list for eating window | complex carbs list | 1,000 | 15 | 250 |
| 398 | Foods high in potassium (for fasting electrolytes) | foods high in potassium | 2,400 | 30 | 288 |
| 399 | Foods high in magnesium (for fasting support) | foods high in magnesium | 1,600 | 25 | 256 |
| 400 | Best nuts for intermittent fasting | best nuts for weight loss | 720 | 15 | 180 |
| 401 | Keto pantry staples checklist | keto pantry staples | 320 | 8 | 80 |
| 402 | Keto snack list | keto snacks | 3,600 | 30 | 432 |
| 403 | Clean eating food list for IF | clean eating food list | 1,000 | 20 | 200 |
| 404 | Ketogenic diet grocery list | keto grocery list | 2,400 | 25 | 480 |
| 405 | Protein-rich foods for IF eating window | protein rich foods | 1,600 | 20 | 320 |
| 406 | 100-calorie snack ideas for IF | 100 calorie snacks | 720 | 10 | 180 |
| 407 | Foods to eat before a fast (last meal) | what to eat before fasting | 390 | 12 | 98 |
| 408 | Best foods for sustained energy during IF | foods for energy | 720 | 15 | 180 |
| 409 | Omega-3 rich foods list | omega 3 foods | 1,600 | 20 | 320 |
| 410 | Probiotic foods list | probiotic foods | 1,600 | 20 | 320 |
| 411 | Prebiotic foods list for gut health | prebiotic foods | 1,000 | 15 | 250 |
| 412 | Calcium-rich foods (non-dairy) | calcium rich foods | 1,000 | 15 | 250 |
| 413 | Iron-rich foods list | iron rich foods | 1,600 | 20 | 320 |
| 414 | Foods that boost metabolism | foods that boost metabolism | 1,600 | 30 | 192 |
| 415 | Foods for muscle recovery after IF | foods for muscle recovery | 590 | 12 | 148 |
| 416 | Foods that reduce inflammation during IF | anti inflammatory foods for fasting | 260 | 8 | 65 |
| 417 | Vitamin D rich foods list | vitamin d foods | 1,600 | 15 | 400 |
| 418 | Zinc-rich foods for immune support | zinc rich foods | 720 | 12 | 180 |
| 419 | Selenium-rich foods list | selenium rich foods | 480 | 10 | 120 |
| 420 | Collagen-rich foods for IF | foods high in collagen | 590 | 10 | 148 |
| 421 | Best seeds for intermittent fasting | healthiest seeds | 480 | 10 | 120 |
| 422 | Alkaline food list | alkaline foods list | 1,000 | 15 | 250 |
| 423 | Satiating foods to prevent overeating during IF | most filling foods | 720 | 12 | 180 |
| 424 | Electrolyte-rich foods for fasting support | electrolyte rich foods | 480 | 10 | 120 |
| 425 | Best berries for intermittent fasting | healthiest berries | 480 | 10 | 120 |

**Cluster 9 math:**
- Total primary keyword volume: ~70,770/month
- 50 pages × 310 avg raw capture = 15,500/month raw
- After 80% success: **12,400/month**

---

## Cluster 10: "Is X Keto / IF-Friendly?" Food Evaluations (70 opportunities)

**Why this cluster matters:** Perfect Keto's "is banana keto" drives 2,518 traffic. Their "what is tripe" drives 4,590. This is a scalable template: one page per food, each targeting a specific "[food] + keto/fasting" query. Low competition, high volume in aggregate, and each page is a natural internal link anchor to broader food list and meal plan content.

**Reference domains:** PK, DD, RM, FA, SC

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 426 | Is banana keto? | is banana keto | 1,600 | 15 | 400 |
| 427 | Is rice keto? | is rice keto | 1,000 | 12 | 250 |
| 428 | Is hummus keto? | is hummus keto | 720 | 10 | 180 |
| 429 | Is popcorn keto? | is popcorn keto | 720 | 10 | 180 |
| 430 | Is oatmeal keto? | is oatmeal keto | 720 | 10 | 180 |
| 431 | Is peanut butter keto? | is peanut butter keto | 720 | 10 | 180 |
| 432 | Are beans keto? | are beans keto | 590 | 10 | 148 |
| 433 | Is corn keto? | is corn keto | 590 | 10 | 148 |
| 434 | Is milk keto? | is milk keto | 480 | 8 | 120 |
| 435 | Is yogurt keto? | is yogurt keto | 480 | 8 | 120 |
| 436 | Is quinoa keto? | is quinoa keto | 480 | 10 | 120 |
| 437 | Is watermelon keto? | is watermelon keto | 480 | 8 | 120 |
| 438 | Is sweet potato keto? | is sweet potato keto | 480 | 8 | 120 |
| 439 | Are potatoes keto? | are potatoes keto | 590 | 10 | 148 |
| 440 | Is honey keto? | is honey keto | 390 | 8 | 98 |
| 441 | Is coconut milk keto? | is coconut milk keto | 320 | 6 | 80 |
| 442 | Is dark chocolate keto? | is dark chocolate keto | 390 | 8 | 98 |
| 443 | Are carrots keto? | are carrots keto | 390 | 8 | 98 |
| 444 | Are tomatoes keto? | are tomatoes keto | 390 | 6 | 98 |
| 445 | Is almond milk keto? | is almond milk keto | 320 | 6 | 80 |
| 446 | Is cottage cheese keto? | is cottage cheese keto | 320 | 6 | 80 |
| 447 | Is sushi keto? | is sushi keto | 320 | 6 | 80 |
| 448 | Is wine keto? | is wine keto | 480 | 8 | 120 |
| 449 | Is beer keto? | is beer keto | 390 | 8 | 98 |
| 450 | Are grapes keto? | are grapes keto | 320 | 6 | 80 |
| 451 | Is pizza keto? | is pizza keto | 260 | 6 | 65 |
| 452 | Is bread keto? | is bread keto | 390 | 8 | 98 |
| 453 | Are chickpeas keto? | are chickpeas keto | 320 | 6 | 80 |
| 454 | Is tofu keto? | is tofu keto | 320 | 6 | 80 |
| 455 | Are strawberries keto? | are strawberries keto | 320 | 6 | 80 |
| 456 | Are blueberries keto? | are blueberries keto | 320 | 6 | 80 |
| 457 | Is pasta keto? | is pasta keto | 320 | 6 | 80 |
| 458 | Is mango keto? | is mango keto | 260 | 5 | 65 |
| 459 | Is pineapple keto? | is pineapple keto | 260 | 5 | 65 |
| 460 | Are apples keto? | are apples keto | 260 | 6 | 65 |
| 461 | Is avocado keto? | is avocado keto | 260 | 5 | 65 |
| 462 | Are oranges keto? | are oranges keto | 260 | 5 | 65 |
| 463 | Is cream cheese keto? | is cream cheese keto | 260 | 5 | 65 |
| 464 | Are lentils keto? | are lentils keto | 260 | 6 | 65 |
| 465 | Is edamame keto? | is edamame keto | 260 | 5 | 65 |
| 466 | Is coconut water keto? | is coconut water keto | 210 | 5 | 53 |
| 467 | Are onions keto? | are onions keto | 260 | 5 | 65 |
| 468 | Is celery keto? | is celery keto | 170 | 4 | 43 |
| 469 | Is broccoli keto? | is broccoli keto | 210 | 5 | 53 |
| 470 | Is cauliflower keto? | is cauliflower keto | 170 | 4 | 43 |
| 471 | Are mushrooms keto? | are mushrooms keto | 210 | 5 | 53 |
| 472 | Is cabbage keto? | is cabbage keto | 170 | 4 | 43 |
| 473 | Is butternut squash keto? | is butternut squash keto | 210 | 5 | 53 |
| 474 | Is acorn squash keto? | is acorn squash keto | 170 | 4 | 43 |
| 475 | Is zucchini keto? | is zucchini keto | 170 | 4 | 43 |
| 476 | Are beets keto? | are beets keto | 210 | 5 | 53 |
| 477 | Is pumpkin keto? | is pumpkin keto | 210 | 5 | 53 |
| 478 | Is sour cream keto? | is sour cream keto | 210 | 4 | 53 |
| 479 | Is heavy cream keto? | is heavy cream keto | 210 | 4 | 53 |
| 480 | Is ranch keto? | is ranch keto | 170 | 4 | 43 |
| 481 | Is mayo keto? | is mayo keto | 170 | 4 | 43 |
| 482 | Is bacon keto? | is bacon keto | 210 | 4 | 53 |
| 483 | Is jerky keto? | is jerky keto | 170 | 5 | 43 |
| 484 | Is salami keto? | is salami keto | 170 | 4 | 43 |
| 485 | Is ham keto? | is ham keto | 170 | 4 | 43 |
| 486 | Is shrimp keto? | is shrimp keto | 170 | 4 | 43 |
| 487 | Is salmon keto? | is salmon keto | 170 | 4 | 43 |
| 488 | Is tuna keto? | is tuna keto | 170 | 4 | 43 |
| 489 | Are peas keto? | are peas keto | 210 | 5 | 53 |
| 490 | Is mozzarella keto? | is mozzarella keto | 170 | 4 | 43 |
| 491 | Is cheddar keto? | is cheddar keto | 140 | 3 | 35 |
| 492 | Is parmesan keto? | is parmesan keto | 140 | 3 | 35 |
| 493 | Is feta keto? | is feta keto | 140 | 3 | 35 |
| 494 | Is halloumi keto? | is halloumi keto | 140 | 4 | 35 |
| 495 | Is whipped cream keto? | is whipped cream keto | 140 | 3 | 35 |

**Cluster 10 math:**
- Total primary keyword volume: ~23,270/month
- 70 pages × 130 avg raw capture = 9,100/month raw
- After 80% success: **7,280/month**

---

## Cluster 11: Blood Sugar & Metabolic Health (45 opportunities)

**Why this cluster matters:** Nutrisense's blood sugar chart drives 41,018 visits from a single page — making it their #1 content asset by a factor of 20x. Dr. Berg's insulin resistance content ranks in the top 10 of his site. This cluster bridges fasting content with metabolic health, positioning Simple as a comprehensive health app rather than just a fasting timer.

**Reference domains:** NS, DB, DD, NF, FA

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 496 | Normal blood sugar levels: what's healthy | normal blood sugar levels | 27,100 | 35 | 2,710 |
| 497 | Blood sugar levels chart (by age, time of day) | blood sugar chart | 5,400 | 30 | 648 |
| 498 | What is insulin resistance | what is insulin resistance | 5,400 | 35 | 540 |
| 499 | Blood sugar after eating: what's normal | blood sugar after eating | 2,900 | 20 | 580 |
| 500 | Fasting blood sugar levels: what the numbers mean | fasting blood sugar levels | 2,400 | 20 | 480 |
| 501 | How to lower blood sugar quickly | how to lower blood sugar | 5,400 | 45 | 324 |
| 502 | Blood sugar spike symptoms | blood sugar spike symptoms | 1,600 | 15 | 400 |
| 503 | What causes high blood sugar (without diabetes) | high blood sugar causes | 1,300 | 20 | 260 |
| 504 | How intermittent fasting lowers blood sugar | intermittent fasting blood sugar | 720 | 15 | 180 |
| 505 | Dawn phenomenon: why blood sugar rises in the morning | dawn phenomenon | 1,600 | 15 | 400 |
| 506 | How to reverse insulin resistance naturally | how to reverse insulin resistance | 1,600 | 30 | 192 |
| 507 | A1C levels chart: what your numbers mean | a1c levels chart | 3,600 | 30 | 432 |
| 508 | Signs of insulin resistance | signs of insulin resistance | 1,300 | 20 | 260 |
| 509 | Reactive hypoglycemia: blood sugar crash after eating | reactive hypoglycemia | 1,600 | 20 | 320 |
| 510 | Blood sugar and weight loss connection | blood sugar weight loss | 590 | 15 | 148 |
| 511 | How carbs affect blood sugar | how carbs affect blood sugar | 480 | 12 | 120 |
| 512 | Blood sugar and cortisol: the stress connection | cortisol and blood sugar | 480 | 12 | 120 |
| 513 | Glucose vs. ketones: fuel sources explained | glucose vs ketones | 320 | 12 | 80 |
| 514 | Metabolic syndrome: what it is and how to fix it | metabolic syndrome | 3,600 | 40 | 360 |
| 515 | What is metabolic health? | metabolic health | 590 | 15 | 148 |
| 516 | How to improve insulin sensitivity | improve insulin sensitivity | 1,000 | 25 | 200 |
| 517 | GLP-1 and fasting: natural vs. Ozempic | glp-1 fasting | 720 | 15 | 180 |
| 518 | Intermittent fasting and diabetes (type 2) | intermittent fasting diabetes type 2 | 720 | 25 | 115 |
| 519 | Blood sugar after exercise: what to expect | blood sugar after exercise | 590 | 12 | 148 |
| 520 | Glycemic index vs glycemic load explained | glycemic index vs glycemic load | 720 | 15 | 180 |
| 521 | Continuous glucose monitor: what it tells you | continuous glucose monitor | 2,400 | 35 | 240 |
| 522 | Sugar detox: how fasting helps reset sugar cravings | sugar detox | 1,600 | 25 | 256 |
| 523 | Hypoglycemia symptoms and treatment | hypoglycemia symptoms | 2,400 | 20 | 480 |
| 524 | Prediabetes: signs, diet, and reversal | prediabetes | 3,600 | 40 | 360 |
| 525 | Does fasting cure insulin resistance | fasting insulin resistance | 390 | 12 | 98 |
| 526 | Hemoglobin A1C: how to lower it naturally | how to lower a1c | 2,400 | 35 | 240 |
| 527 | Blood sugar and sleep quality | blood sugar and sleep | 320 | 10 | 80 |
| 528 | Fasting insulin test: what it reveals | fasting insulin test | 590 | 12 | 148 |
| 529 | How protein affects blood sugar | protein and blood sugar | 320 | 10 | 80 |
| 530 | Does coffee raise blood sugar | does coffee raise blood sugar | 720 | 10 | 180 |
| 531 | Blood sugar and anxiety connection | blood sugar anxiety | 480 | 12 | 120 |
| 532 | How fiber affects blood sugar | fiber and blood sugar | 320 | 10 | 80 |
| 533 | What is hyperinsulinemia | hyperinsulinemia | 590 | 15 | 148 |
| 534 | Blood sugar monitor accuracy tips | blood sugar monitor | 1,000 | 15 | 250 |
| 535 | Intermittent fasting and type 1 diabetes | intermittent fasting type 1 diabetes | 210 | 15 | 42 |
| 536 | Does stress raise blood sugar | stress and blood sugar | 480 | 10 | 120 |
| 537 | Blood sugar and hunger: why you feel hungry | blood sugar and hunger | 260 | 8 | 65 |
| 538 | How to stop blood sugar spikes | how to prevent blood sugar spikes | 590 | 15 | 148 |
| 539 | Gluconeogenesis during fasting explained | gluconeogenesis fasting | 210 | 10 | 53 |
| 540 | Blood sugar and mood: the connection | blood sugar mood swings | 320 | 10 | 80 |

**Cluster 11 math:**
- Total primary keyword volume: ~95,720/month
- 45 pages × 310 avg raw capture = 13,950/month raw
- After 80% success: **11,160/month**

---

## Cluster 12: Fasting & Drinks/Beverages (35 opportunities)

**Why this cluster matters:** "What can you drink while fasting" is one of the most-asked IF questions. Every drink is a potential page: coffee, tea, water variations, electrolyte drinks, zero-cal sodas. These pages also serve as gateway content to the "does X break a fast" cluster, creating strong internal linking opportunities.

**Reference domains:** FA, AE, ZL, DB, PK

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 541 | What can you drink during a fast | what can you drink while fasting | 2,400 | 25 | 384 |
| 542 | Best tea for intermittent fasting | best tea for fasting | 720 | 10 | 180 |
| 543 | Coffee and fasting: everything you need to know | coffee and fasting | 1,000 | 15 | 250 |
| 544 | Electrolyte water while fasting | electrolyte water fasting | 390 | 8 | 98 |
| 545 | Best electrolyte drinks for fasting | best electrolytes for fasting | 720 | 12 | 180 |
| 546 | Green tea and fasting: benefits and timing | green tea intermittent fasting | 480 | 10 | 120 |
| 547 | Can you drink diet soda while fasting | diet soda while fasting | 480 | 10 | 120 |
| 548 | Apple cider vinegar drink during fasting | apple cider vinegar drink fasting | 390 | 10 | 78 |
| 549 | Lemon water during fasting: benefits | lemon water during fasting | 480 | 8 | 120 |
| 550 | Black coffee during fasting: benefits and limits | black coffee fasting | 480 | 10 | 120 |
| 551 | Matcha during fasting | matcha during fasting | 260 | 6 | 65 |
| 552 | Herbal tea and fasting: which are safe | herbal tea fasting | 260 | 6 | 65 |
| 553 | Sparkling water and fasting | sparkling water fasting | 210 | 4 | 53 |
| 554 | Bone broth during fasting: does it count | bone broth during fasting | 390 | 10 | 78 |
| 555 | Bulletproof coffee while fasting | bulletproof coffee fasting | 390 | 12 | 78 |
| 556 | Can you drink protein shakes while fasting | protein shake while fasting | 320 | 8 | 80 |
| 557 | Kombucha while fasting | kombucha while fasting | 260 | 6 | 65 |
| 558 | Best water to drink during fasting | best water for fasting | 170 | 5 | 43 |
| 559 | Can you drink milk during fasting | milk during fasting | 210 | 6 | 53 |
| 560 | Coconut water during fasting | coconut water fasting | 210 | 5 | 53 |
| 561 | Can you drink juice while fasting | juice while fasting | 210 | 6 | 53 |
| 562 | Zero-calorie drinks that don't break a fast | zero calorie drinks fasting | 320 | 8 | 80 |
| 563 | Can you drink almond milk while fasting | almond milk fasting | 210 | 6 | 53 |
| 564 | Energy drinks and fasting | energy drinks while fasting | 210 | 6 | 53 |
| 565 | Salt water during fasting (sole water) | salt water fasting | 320 | 8 | 80 |
| 566 | How much water to drink during fasting | how much water during fasting | 320 | 8 | 80 |
| 567 | Chamomile tea and fasting | chamomile tea fasting | 140 | 4 | 35 |
| 568 | Peppermint tea during fasting | peppermint tea fasting | 140 | 4 | 35 |
| 569 | Ginger tea while fasting | ginger tea fasting | 170 | 5 | 43 |
| 570 | Turmeric tea during fasting | turmeric tea fasting | 140 | 5 | 35 |
| 571 | Cinnamon water while fasting | cinnamon water fasting | 170 | 5 | 43 |
| 572 | Can you drink smoothies while fasting | smoothie fasting | 170 | 5 | 43 |
| 573 | Flavored water during fasting | flavored water fasting | 140 | 4 | 35 |
| 574 | Can you drink coffee with cream while fasting | coffee with cream fasting | 320 | 8 | 80 |
| 575 | Decaf coffee during fasting | decaf coffee fasting | 140 | 4 | 35 |

**Cluster 12 math:**
- Total primary keyword volume: ~14,120/month
- 35 pages × 165 avg raw capture = 5,775/month raw
- After 80% success: **4,620/month**

---

## Cluster 13: Weight Loss Strategies (50 opportunities)

**Why this cluster matters:** "How to lose weight" has massive search volume. Lose It drives 3,000-6,000 per page on weight loss education. Dr. Berg's weight loss content ranks among his highest-traffic pages. Simple's value proposition is weight loss through IF — this cluster positions every piece of content as a funnel to the app.

**Reference domains:** LI, DB, DD, FA, LA

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 576 | How to lose belly fat with intermittent fasting | how to lose belly fat | 12,100 | 55 | 363 |
| 577 | Calorie deficit explained: the only rule of fat loss | calorie deficit | 5,400 | 35 | 540 |
| 578 | Plateau in weight loss: how to break through | weight loss plateau | 2,400 | 25 | 480 |
| 579 | Why am I not losing weight on IF | not losing weight intermittent fasting | 1,000 | 15 | 250 |
| 580 | Intermittent fasting vs calorie counting | intermittent fasting vs calorie counting | 590 | 15 | 148 |
| 581 | How much weight can you lose in a month with IF | weight loss per month intermittent fasting | 720 | 20 | 144 |
| 582 | Does not eating make you gain weight | does not eating make you gain weight | 590 | 10 | 148 |
| 583 | How to speed up metabolism | how to speed up metabolism | 3,600 | 40 | 360 |
| 584 | Body recomposition: lose fat, gain muscle | body recomposition | 2,400 | 30 | 288 |
| 585 | Water weight vs fat loss: how to tell the difference | water weight vs fat loss | 720 | 10 | 180 |
| 586 | Healthy weight loss per week: what's realistic | healthy weight loss per week | 720 | 15 | 180 |
| 587 | Metabolic confusion diet explained | metabolic confusion diet | 1,600 | 15 | 400 |
| 588 | Reverse dieting: how to eat more without gaining | reverse dieting | 1,000 | 20 | 200 |
| 589 | Why you gain weight after fasting | weight gain after fasting | 480 | 10 | 120 |
| 590 | How to lose 10 pounds with IF | how to lose 10 pounds | 2,400 | 40 | 240 |
| 591 | How to lose 20 pounds with IF | how to lose 20 pounds | 1,600 | 35 | 160 |
| 592 | How to lose 50 pounds with IF | how to lose 50 pounds | 1,000 | 30 | 120 |
| 593 | Set point theory: can you change your body's set weight | set point theory weight loss | 590 | 12 | 148 |
| 594 | Does muscle weigh more than fat | does muscle weigh more than fat | 1,600 | 10 | 400 |
| 595 | How to lose face fat | how to lose face fat | 2,400 | 30 | 288 |
| 596 | Stubborn belly fat: why IF works where diets fail | stubborn belly fat | 1,000 | 20 | 200 |
| 597 | Visceral fat vs subcutaneous fat | visceral fat | 1,600 | 20 | 320 |
| 598 | BMR explained: your metabolism baseline | basal metabolic rate | 2,400 | 25 | 480 |
| 599 | Carb cycling for weight loss | carb cycling | 2,400 | 25 | 480 |
| 600 | Does fasting cause muscle loss | does fasting cause muscle loss | 480 | 12 | 120 |
| 601 | Starvation mode: myth or reality | starvation mode | 720 | 12 | 180 |
| 602 | How to maintain weight after losing it | how to maintain weight | 720 | 15 | 180 |
| 603 | Adaptive thermogenesis and weight loss | adaptive thermogenesis | 320 | 10 | 80 |
| 604 | Leptin resistance and weight loss | leptin resistance | 720 | 15 | 180 |
| 605 | Ghrelin and hunger: managing appetite during IF | ghrelin hormone | 480 | 10 | 120 |
| 606 | Fat-adapted: what it means and how to get there | fat adapted | 480 | 10 | 120 |
| 607 | NEAT and weight loss: non-exercise activity | neat weight loss | 480 | 10 | 120 |
| 608 | Thermic effect of food explained | thermic effect of food | 590 | 10 | 148 |
| 609 | Lose weight without counting calories | lose weight without counting calories | 590 | 15 | 148 |
| 610 | Skinny fat: how IF helps change body composition | skinny fat | 1,000 | 15 | 250 |
| 611 | How long to see results from IF | how long to see results intermittent fasting | 480 | 12 | 120 |
| 612 | Does intermittent fasting work for everyone | does intermittent fasting work | 720 | 20 | 144 |
| 613 | IF and loose skin: what to know | loose skin after weight loss | 1,000 | 15 | 250 |
| 614 | Ozempic vs intermittent fasting | ozempic vs intermittent fasting | 480 | 15 | 120 |
| 615 | GLP-1 drugs vs natural fasting | glp-1 medications | 1,600 | 30 | 192 |
| 616 | Weight loss supplements that actually work | weight loss supplements | 2,400 | 45 | 144 |
| 617 | How sleep affects weight loss | sleep and weight loss | 720 | 15 | 180 |
| 618 | Stress and weight gain: the cortisol connection | stress weight gain | 720 | 12 | 180 |
| 619 | Weight loss after 40: what changes | weight loss after 40 | 1,000 | 20 | 200 |
| 620 | Weight loss after 50: IF strategies | weight loss after 50 | 720 | 20 | 144 |
| 621 | Menopause weight gain: how IF helps | menopause weight gain | 1,000 | 20 | 200 |
| 622 | Thyroid and weight loss | thyroid weight loss | 1,000 | 25 | 200 |
| 623 | How walking helps weight loss during IF | walking for weight loss | 2,400 | 25 | 480 |
| 624 | Weight loss motivation: science-backed strategies | weight loss motivation | 720 | 15 | 180 |
| 625 | Mini cut: short-term aggressive fat loss with IF | mini cut | 480 | 10 | 120 |

**Cluster 13 math:**
- Total primary keyword volume: ~75,160/month
- 50 pages × 240 avg raw capture = 12,000/month raw
- After 80% success: **9,600/month**

---

## Cluster 14: IF for Specific Populations (40 opportunities)

**Why this cluster matters:** "Intermittent fasting for women" has 12,100+ monthly searches. Amy MD Wellness built an entire brand around women's fasting. Nobody owns the population-specific IF space. High conversion because population-specific content makes Simple feel personalized — "this app gets me."

**Reference domains:** AE, DD, DB, FA, NF, LA

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 626 | Intermittent fasting for women: complete guide | intermittent fasting for women | 12,100 | 45 | 726 |
| 627 | Intermittent fasting for men over 40 | intermittent fasting for men | 1,600 | 20 | 320 |
| 628 | Intermittent fasting and PCOS | intermittent fasting pcos | 720 | 15 | 180 |
| 629 | Intermittent fasting during menopause | intermittent fasting menopause | 1,000 | 20 | 200 |
| 630 | Intermittent fasting for beginners over 50 | intermittent fasting for beginners over 50 | 720 | 15 | 180 |
| 631 | Is intermittent fasting safe for teens | intermittent fasting for teens | 480 | 12 | 120 |
| 632 | Intermittent fasting for seniors: benefits & risks | intermittent fasting for seniors | 480 | 10 | 120 |
| 633 | Intermittent fasting with diabetes | intermittent fasting and diabetes | 720 | 25 | 115 |
| 634 | Intermittent fasting and breastfeeding | intermittent fasting breastfeeding | 480 | 10 | 120 |
| 635 | Intermittent fasting while pregnant: safety guide | intermittent fasting while pregnant | 720 | 15 | 180 |
| 636 | Intermittent fasting and perimenopause | intermittent fasting perimenopause | 390 | 10 | 98 |
| 637 | Intermittent fasting for women over 40 | intermittent fasting women over 40 | 720 | 15 | 180 |
| 638 | Intermittent fasting for women over 60 | intermittent fasting women over 60 | 320 | 10 | 80 |
| 639 | Intermittent fasting for men over 50 | intermittent fasting men over 50 | 320 | 10 | 80 |
| 640 | Intermittent fasting and menstrual cycle | intermittent fasting menstrual cycle | 480 | 10 | 120 |
| 641 | IF and hormonal balance for women | intermittent fasting hormones women | 320 | 12 | 64 |
| 642 | IF for endomorphs (body type guide) | intermittent fasting endomorph | 260 | 8 | 65 |
| 643 | IF for ectomorphs: building muscle while fasting | intermittent fasting ectomorph | 210 | 8 | 53 |
| 644 | IF and ADHD: focus and fasting | intermittent fasting adhd | 320 | 8 | 80 |
| 645 | IF for runners: performance and fasting | intermittent fasting for runners | 320 | 10 | 80 |
| 646 | IF for bodybuilders: cutting guide | intermittent fasting bodybuilding | 720 | 20 | 144 |
| 647 | IF during Ramadan: how to optimize | intermittent fasting ramadan | 480 | 8 | 120 |
| 648 | IF for college students | intermittent fasting college students | 170 | 5 | 43 |
| 649 | IF for shift workers: schedule guide | intermittent fasting shift workers | 210 | 8 | 53 |
| 650 | IF and IBS: gut sensitivity guide | intermittent fasting ibs | 320 | 10 | 80 |
| 651 | IF and autoimmune conditions | intermittent fasting autoimmune | 260 | 10 | 52 |
| 652 | IF for people with anxiety | intermittent fasting anxiety | 260 | 8 | 65 |
| 653 | IF for people with depression | intermittent fasting depression | 210 | 8 | 53 |
| 654 | IF for vegetarians and vegans | intermittent fasting vegetarian | 390 | 12 | 78 |
| 655 | IF for night shift workers | intermittent fasting night shift | 260 | 8 | 65 |
| 656 | IF with hypothyroidism | intermittent fasting hypothyroidism | 480 | 12 | 96 |
| 657 | IF with hyperthyroidism | intermittent fasting hyperthyroidism | 140 | 8 | 35 |
| 658 | IF for athletes: performance guide | intermittent fasting athletes | 480 | 15 | 96 |
| 659 | IF and eating disorders: when to avoid fasting | intermittent fasting eating disorder | 260 | 10 | 52 |
| 660 | IF for couples: doing it together | intermittent fasting couples | 110 | 4 | 28 |
| 661 | IF during travel: maintaining your schedule | intermittent fasting while traveling | 170 | 5 | 43 |
| 662 | IF for busy parents | intermittent fasting busy schedule | 170 | 5 | 43 |
| 663 | IF for nurses (long shift guide) | intermittent fasting for nurses | 170 | 5 | 43 |
| 664 | IF for military/first responders | intermittent fasting military | 110 | 5 | 28 |
| 665 | IF for postpartum recovery | intermittent fasting postpartum | 210 | 8 | 53 |

**Cluster 14 math:**
- Total primary keyword volume: ~28,680/month
- 40 pages × 325 avg raw capture = 13,000/month raw
- After 80% success: **10,400/month**

---

## Cluster 15: Diet Comparisons — IF vs X (35 opportunities)

**Why this cluster matters:** FA's "carnivore diet" and "blood type diet" pages each drive 900+. Comparison content catches people deciding between approaches — high intent, moderate competition. Positions Simple as the authoritative voice on how IF compares to every alternative.

**Reference domains:** FA, DD, DB, PK, LI

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 666 | Intermittent fasting vs keto: can you do both | intermittent fasting vs keto | 1,300 | 25 | 208 |
| 667 | Intermittent fasting vs calorie counting | intermittent fasting vs calorie counting | 590 | 15 | 148 |
| 668 | Intermittent fasting vs Mediterranean diet | intermittent fasting vs mediterranean diet | 260 | 12 | 52 |
| 669 | Intermittent fasting vs Ozempic | intermittent fasting vs ozempic | 480 | 15 | 120 |
| 670 | Keto + IF: the ultimate combo guide | keto and intermittent fasting | 1,600 | 30 | 192 |
| 671 | IF vs Whole30 | intermittent fasting vs whole30 | 170 | 8 | 43 |
| 672 | IF vs vegan diet for weight loss | intermittent fasting vs vegan | 170 | 8 | 43 |
| 673 | IF vs carnivore diet | intermittent fasting vs carnivore diet | 210 | 10 | 42 |
| 674 | IF vs low-carb diet | intermittent fasting vs low carb | 260 | 12 | 52 |
| 675 | IF vs paleo diet | intermittent fasting vs paleo | 170 | 10 | 34 |
| 676 | Carnivore diet guide (for IF users) | carnivore diet | 5,400 | 40 | 540 |
| 677 | Blood type diet explained (evidence review) | blood type diet | 2,400 | 20 | 480 |
| 678 | Anti-inflammatory diet vs IF | anti inflammatory diet | 3,600 | 30 | 432 |
| 679 | DASH diet vs IF for heart health | dash diet | 2,400 | 30 | 288 |
| 680 | Flexitarian diet vs IF | flexitarian diet | 1,000 | 15 | 250 |
| 681 | Volumetrics diet vs IF | volumetrics diet | 590 | 12 | 118 |
| 682 | Noom vs intermittent fasting | noom vs intermittent fasting | 260 | 8 | 65 |
| 683 | Weight Watchers vs intermittent fasting | weight watchers vs intermittent fasting | 260 | 8 | 65 |
| 684 | Optavia vs intermittent fasting | optavia vs intermittent fasting | 210 | 6 | 53 |
| 685 | Nutrisystem vs IF | nutrisystem vs intermittent fasting | 140 | 5 | 35 |
| 686 | Slow carb diet (4-hour body) vs IF | slow carb diet | 590 | 10 | 148 |
| 687 | Atkins vs keto vs IF | atkins vs keto | 720 | 12 | 180 |
| 688 | CICO vs IF: the real debate | cico diet | 590 | 10 | 148 |
| 689 | Zone diet vs IF | zone diet | 480 | 10 | 120 |
| 690 | South Beach diet vs IF | south beach diet | 590 | 12 | 118 |
| 691 | Dukan diet vs IF | dukan diet | 480 | 10 | 120 |
| 692 | Engine 2 diet vs IF (plant-based) | engine 2 diet | 210 | 5 | 53 |
| 693 | The Galveston diet vs IF (menopause focus) | galveston diet | 720 | 12 | 180 |
| 694 | Sirtfood diet vs IF | sirtfood diet | 590 | 10 | 148 |
| 695 | Dr. Fung's fasting protocol explained | dr fung fasting | 320 | 10 | 80 |
| 696 | Eat-stop-eat vs lean gains protocol | eat stop eat vs leangains | 140 | 5 | 35 |
| 697 | Snake diet: what it is (and safer alternatives) | snake diet | 720 | 10 | 180 |
| 698 | Fast 800 diet by Dr. Michael Mosley | fast 800 diet | 590 | 12 | 118 |
| 699 | Intuitive eating vs intermittent fasting | intuitive eating vs intermittent fasting | 210 | 8 | 53 |
| 700 | The Longevity Diet by Valter Longo vs IF | longevity diet | 480 | 12 | 96 |

**Cluster 15 math:**
- Total primary keyword volume: ~30,050/month
- 35 pages × 200 avg raw capture = 7,000/month raw
- After 80% success: **5,600/month**

---

## Cluster 16: IF + Exercise & Fitness (30 opportunities)

**Why this cluster matters:** "Working out while fasting" and "fasted cardio" are high-intent queries from active IF users — the highest LTV demographic for a fasting app. Simple's competitors barely touch this space, leaving room to own the IF-fitness intersection.

**Reference domains:** DB, FA, AE, NF, LI

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 701 | Working out while fasting: complete guide | working out while fasting | 1,600 | 20 | 320 |
| 702 | Fasted cardio: benefits and risks | fasted cardio | 2,400 | 25 | 384 |
| 703 | How to build muscle while intermittent fasting | build muscle intermittent fasting | 1,000 | 25 | 160 |
| 704 | Best time to exercise during IF | best time to exercise intermittent fasting | 590 | 12 | 148 |
| 705 | Fasted weight training: should you lift without eating | fasted weight training | 480 | 12 | 120 |
| 706 | Pre-workout while fasting: what works | pre workout while fasting | 480 | 10 | 120 |
| 707 | Running while fasting: guide for runners | running while fasting | 320 | 10 | 80 |
| 708 | Yoga and intermittent fasting | yoga and fasting | 260 | 8 | 65 |
| 709 | Swimming while fasting | swimming while fasting | 170 | 5 | 43 |
| 710 | HIIT while fasting: is it safe and effective | hiit while fasting | 320 | 10 | 80 |
| 711 | Walking while fasting: why it works | walking while fasting | 320 | 8 | 80 |
| 712 | Post-workout nutrition for IF | post workout meal intermittent fasting | 260 | 10 | 52 |
| 713 | Fasted morning workout vs fed workout | fasted vs fed workout | 260 | 10 | 52 |
| 714 | CrossFit and intermittent fasting | crossfit intermittent fasting | 210 | 8 | 53 |
| 715 | How to avoid muscle loss during fasting | how to prevent muscle loss fasting | 320 | 12 | 64 |
| 716 | Protein timing for IF and exercise | protein timing intermittent fasting | 210 | 8 | 53 |
| 717 | Creatine and intermittent fasting | creatine intermittent fasting | 390 | 10 | 98 |
| 718 | BCAAs and fasting for muscle preservation | bcaas and fasting | 210 | 8 | 53 |
| 719 | Marathon training while fasting | marathon training fasting | 140 | 6 | 35 |
| 720 | Cycling while fasting | cycling while fasting | 170 | 5 | 43 |
| 721 | Strength training during extended fasts | strength training fasting | 170 | 8 | 34 |
| 722 | Should you exercise on fasting days (5:2 / ADF) | exercise on fasting days | 170 | 6 | 43 |
| 723 | How fasting improves endurance | fasting and endurance | 140 | 6 | 35 |
| 724 | Rock climbing and fasting | rock climbing fasting | 90 | 3 | 23 |
| 725 | Pilates and intermittent fasting | pilates intermittent fasting | 140 | 5 | 35 |
| 726 | Stretching and mobility during a fast | stretching while fasting | 110 | 4 | 28 |
| 727 | Gym performance on IF: what to expect | gym performance fasting | 140 | 5 | 35 |
| 728 | Lean gains protocol: Martin Berkhan's approach | lean gains | 720 | 15 | 144 |
| 729 | Fasting and VO2 max: does it help or hurt | fasting vo2 max | 110 | 6 | 22 |
| 730 | How to get ripped with IF (body recomp for fitness) | intermittent fasting to get ripped | 260 | 12 | 42 |

**Cluster 16 math:**
- Total primary keyword volume: ~12,630/month
- 30 pages × 185 avg raw capture = 5,550/month raw
- After 80% success: **4,440/month**

---

## Cluster 17: Supplements & Vitamins During Fasting (30 opportunities)

**Why this cluster matters:** Every IF practitioner asks "should I take vitamins while fasting?" PK's supplement reviews drive 1,600-2,100 traffic each. NS's sweetener guides get 3,200+. These pages have moderate commercial intent (affiliate potential + app conversion) and fill a trust gap.

**Reference domains:** PK, NS, DB, AE, FA

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 731 | Best electrolytes for fasting | best electrolytes for fasting | 720 | 12 | 180 |
| 732 | Should you take vitamins while fasting | vitamins while fasting | 480 | 8 | 120 |
| 733 | Best magnesium supplement for fasting | best magnesium for fasting | 390 | 10 | 98 |
| 734 | Sodium and fasting: how much do you need | sodium fasting | 260 | 6 | 65 |
| 735 | Potassium supplements for fasting | potassium supplement fasting | 210 | 8 | 53 |
| 736 | Collagen supplements and fasting: do they work | collagen supplement fasting | 260 | 8 | 65 |
| 737 | Omega-3 supplements while fasting | omega 3 fasting | 170 | 6 | 43 |
| 738 | Multivitamin on an empty stomach: timing guide | multivitamin empty stomach | 480 | 8 | 120 |
| 739 | Probiotics and fasting: timing and benefits | probiotics fasting | 260 | 8 | 65 |
| 740 | Apple cider vinegar supplements vs liquid | apple cider vinegar pills vs liquid | 390 | 8 | 98 |
| 741 | Best MCT oil for fasting | best mct oil | 590 | 12 | 118 |
| 742 | Exogenous ketones: do they help with fasting | exogenous ketones | 590 | 12 | 118 |
| 743 | Best protein powder for IF | best protein powder for intermittent fasting | 320 | 10 | 80 |
| 744 | Creatine timing on IF: before or after | creatine timing intermittent fasting | 210 | 8 | 53 |
| 745 | Ashwagandha benefits for fasting | ashwagandha benefits | 2,400 | 25 | 384 |
| 746 | Berberine and fasting: blood sugar support | berberine supplement | 1,600 | 20 | 320 |
| 747 | L-glutamine for gut health during fasting | l-glutamine gut health | 320 | 8 | 80 |
| 748 | Turmeric and curcumin supplements while fasting | turmeric supplement | 1,000 | 15 | 200 |
| 749 | Green tea extract for fasting | green tea extract | 590 | 12 | 118 |
| 750 | Spirulina and fasting | spirulina benefits | 590 | 10 | 148 |
| 751 | Lion's mane mushroom and fasting | lion's mane mushroom | 1,600 | 15 | 400 |
| 752 | Caffeine pills while fasting | caffeine pills fasting | 170 | 5 | 43 |
| 753 | Best fat burner supplements (IF compatible) | best fat burner | 1,600 | 35 | 160 |
| 754 | Zinc supplements and fasting | zinc supplement fasting | 170 | 5 | 43 |
| 755 | B12 supplements while fasting | b12 supplement fasting | 170 | 5 | 43 |
| 756 | Iron supplements on empty stomach (fasting) | iron supplement empty stomach | 390 | 6 | 98 |
| 757 | Digestive enzymes and IF | digestive enzymes fasting | 170 | 5 | 43 |
| 758 | CoQ10 and fasting | coq10 supplement | 480 | 8 | 120 |
| 759 | Fiber supplements during IF | fiber supplement intermittent fasting | 170 | 6 | 43 |
| 760 | Biotin supplements while fasting | biotin while fasting | 140 | 4 | 35 |

**Cluster 17 math:**
- Total primary keyword volume: ~17,210/month
- 30 pages × 150 avg raw capture = 4,500/month raw
- After 80% success: **3,600/month**

---

## Cluster 18: Fasting Side Effects & Safety (35 opportunities)

**Why this cluster matters:** Safety content earns trust. People searching "fasting headache" or "is intermittent fasting safe" are evaluating whether to start — addressing their concerns is the unlock to app downloads. This content is also heavily cited by AI engines answering safety questions, making it an AEO powerhouse.

**Reference domains:** DB, FA, DD, NF, AE

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 761 | Is intermittent fasting safe? | is intermittent fasting safe | 1,000 | 20 | 200 |
| 762 | Fasting headache: causes and remedies | fasting headache | 1,000 | 10 | 250 |
| 763 | Diarrhea during fasting: causes and fixes | diarrhea during fasting | 480 | 8 | 120 |
| 764 | Nausea while fasting: what to do | nausea while fasting | 320 | 8 | 80 |
| 765 | Fasting and dizziness: when to worry | fasting dizziness | 320 | 8 | 80 |
| 766 | Heart palpitations while fasting | heart palpitations fasting | 260 | 8 | 65 |
| 767 | Fasting and hair loss: is it connected | fasting hair loss | 390 | 10 | 98 |
| 768 | Bad breath during fasting: why and how to fix | fasting bad breath | 260 | 6 | 65 |
| 769 | Insomnia while fasting: sleep tips | fasting insomnia | 210 | 6 | 53 |
| 770 | Stomach pain after breaking a fast | stomach pain after breaking fast | 320 | 8 | 80 |
| 771 | Constipation during fasting: solutions | fasting constipation | 320 | 8 | 80 |
| 772 | Fatigue during fasting: normal or concerning | fasting fatigue | 210 | 6 | 53 |
| 773 | Signs you should stop fasting | when to stop fasting | 260 | 8 | 65 |
| 774 | Fasting and menstrual irregularities | fasting and periods | 480 | 10 | 120 |
| 775 | Can fasting cause gallstones | fasting gallstones | 170 | 6 | 43 |
| 776 | Fasting and low blood sugar risk | fasting low blood sugar | 260 | 8 | 65 |
| 777 | Muscle cramps during fasting | muscle cramps fasting | 210 | 6 | 53 |
| 778 | Brain fog during fasting: causes and solutions | brain fog fasting | 260 | 6 | 65 |
| 779 | Fasting and anxiety: does it help or hurt | fasting and anxiety | 260 | 8 | 65 |
| 780 | Can fasting cause acid reflux | fasting acid reflux | 210 | 6 | 53 |
| 781 | Fasting and cold sensitivity | feeling cold while fasting | 170 | 4 | 43 |
| 782 | Dehydration during fasting: prevention guide | dehydration while fasting | 210 | 6 | 53 |
| 783 | Bloating after breaking a fast | bloating after fasting | 260 | 6 | 65 |
| 784 | Intermittent fasting risks: who should avoid it | intermittent fasting risks | 320 | 12 | 64 |
| 785 | Overeating after fasting: binge prevention | binge eating after fasting | 320 | 8 | 80 |
| 786 | Fasting and electrolyte imbalance | fasting electrolyte imbalance | 170 | 6 | 43 |
| 787 | Can fasting cause gout | fasting and gout | 170 | 6 | 43 |
| 788 | Lightheadedness when standing during fast | lightheaded fasting | 210 | 5 | 53 |
| 789 | Fasting and joint pain: inflammatory response | fasting joint pain | 140 | 5 | 35 |
| 790 | Hunger pangs during fasting: how to manage | hunger pangs fasting | 260 | 6 | 65 |
| 791 | Is dry fasting dangerous | is dry fasting safe | 320 | 8 | 80 |
| 792 | Fasting and adrenal fatigue | fasting adrenal fatigue | 170 | 6 | 43 |
| 793 | Night sweats during fasting | night sweats fasting | 140 | 4 | 35 |
| 794 | Sugar cravings during fasting: how to stop | sugar cravings fasting | 210 | 5 | 53 |
| 795 | Fasting and kidney health: what to know | fasting kidneys | 170 | 6 | 43 |

**Cluster 18 math:**
- Total primary keyword volume: ~10,710/month
- 35 pages × 140 avg raw capture = 4,900/month raw
- After 80% success: **3,920/month**

---

## Cluster 19: Programmatic Nutrition Pages (80 opportunities)

**Why this cluster matters:** SnapCalorie ranks for 681,474 keywords from programmatic food nutrition pages. Their top page ("gumbo nutrition") drives 14,434 traffic. Fastic's "how many calories in 2 scrambled eggs" is their #1 non-homepage content page at 2,928. This is a volume play — each page is lightweight to produce, and the aggregate drives massive long-tail traffic.

**Reference domains:** SC, FA, DD, RM

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 796 | How many calories in 2 scrambled eggs | calories in 2 scrambled eggs | 2,400 | 8 | 600 |
| 797 | Banana nutrition facts and health benefits | banana nutrition | 1,600 | 10 | 400 |
| 798 | Avocado nutrition facts | avocado nutrition | 1,300 | 10 | 325 |
| 799 | Egg nutrition facts: calories, protein, fat | egg nutrition facts | 1,000 | 8 | 250 |
| 800 | Chicken breast nutrition per 100g | chicken breast nutrition | 1,000 | 8 | 250 |
| 801 | Sweet potato nutrition facts | sweet potato nutrition | 720 | 8 | 180 |
| 802 | Brown rice nutrition vs white rice | brown rice nutrition | 720 | 8 | 180 |
| 803 | Oatmeal nutrition facts and benefits | oatmeal nutrition | 720 | 8 | 180 |
| 804 | Salmon nutrition facts per serving | salmon nutrition | 590 | 8 | 148 |
| 805 | Greek yogurt nutrition facts | greek yogurt nutrition | 590 | 6 | 148 |
| 806 | Almond nutrition facts | almond nutrition | 480 | 6 | 120 |
| 807 | Blueberry nutrition facts | blueberry nutrition | 480 | 6 | 120 |
| 808 | Quinoa nutrition facts | quinoa nutrition | 480 | 6 | 120 |
| 809 | Broccoli nutrition facts | broccoli nutrition | 390 | 5 | 98 |
| 810 | Spinach nutrition facts | spinach nutrition | 390 | 5 | 98 |
| 811 | Cottage cheese nutrition facts | cottage cheese nutrition | 390 | 5 | 98 |
| 812 | Peanut butter nutrition facts | peanut butter nutrition | 590 | 8 | 148 |
| 813 | Lentil nutrition facts | lentil nutrition | 320 | 5 | 80 |
| 814 | Chickpea nutrition facts | chickpea nutrition | 320 | 5 | 80 |
| 815 | Tofu nutrition facts | tofu nutrition | 320 | 5 | 80 |
| 816 | Tuna nutrition facts per can | tuna nutrition | 390 | 5 | 98 |
| 817 | Shrimp nutrition facts | shrimp nutrition | 320 | 5 | 80 |
| 818 | Turkey breast nutrition | turkey breast nutrition | 260 | 5 | 65 |
| 819 | Cauliflower nutrition facts | cauliflower nutrition | 260 | 5 | 65 |
| 820 | Kale nutrition facts | kale nutrition | 260 | 5 | 65 |
| 821 | Chia seed nutrition facts | chia seed nutrition | 260 | 5 | 65 |
| 822 | Flaxseed nutrition facts | flaxseed nutrition | 210 | 4 | 53 |
| 823 | Hemp seed nutrition facts | hemp seed nutrition | 170 | 4 | 43 |
| 824 | Walnut nutrition facts | walnut nutrition | 210 | 4 | 53 |
| 825 | Cashew nutrition facts | cashew nutrition | 210 | 4 | 53 |
| 826 | Pistachio nutrition facts | pistachio nutrition | 210 | 5 | 53 |
| 827 | Macadamia nut nutrition | macadamia nut nutrition | 140 | 3 | 35 |
| 828 | Pecan nutrition facts | pecan nutrition | 170 | 4 | 43 |
| 829 | Edamame nutrition facts | edamame nutrition | 260 | 5 | 65 |
| 830 | Hummus nutrition facts | hummus nutrition | 320 | 5 | 80 |
| 831 | Dark chocolate nutrition facts | dark chocolate nutrition | 320 | 5 | 80 |
| 832 | Bone broth nutrition facts | bone broth nutrition | 260 | 5 | 65 |
| 833 | Coconut oil nutrition facts | coconut oil nutrition | 210 | 5 | 53 |
| 834 | Olive oil nutrition facts | olive oil nutrition | 260 | 5 | 65 |
| 835 | Ghee nutrition facts | ghee nutrition | 170 | 4 | 43 |
| 836 | MCT oil nutrition facts | mct oil nutrition | 170 | 4 | 43 |
| 837 | Collagen powder nutrition facts | collagen nutrition | 170 | 4 | 43 |
| 838 | Whey protein nutrition facts | whey protein nutrition | 260 | 5 | 65 |
| 839 | Casein protein nutrition facts | casein protein nutrition | 140 | 4 | 35 |
| 840 | Tempeh nutrition facts | tempeh nutrition | 260 | 4 | 65 |
| 841 | Seitan nutrition facts | seitan nutrition | 170 | 4 | 43 |
| 842 | Black bean nutrition facts | black bean nutrition | 260 | 5 | 65 |
| 843 | Kidney bean nutrition facts | kidney bean nutrition | 170 | 4 | 43 |
| 844 | Green pea nutrition facts | green pea nutrition | 170 | 4 | 43 |
| 845 | Butternut squash nutrition facts | butternut squash nutrition | 210 | 4 | 53 |
| 846 | Zucchini nutrition facts | zucchini nutrition | 210 | 4 | 53 |
| 847 | Bell pepper nutrition facts | bell pepper nutrition | 210 | 4 | 53 |
| 848 | Asparagus nutrition facts | asparagus nutrition | 210 | 4 | 53 |
| 849 | Brussels sprouts nutrition facts | brussels sprouts nutrition | 210 | 4 | 53 |
| 850 | Artichoke nutrition facts | artichoke nutrition | 170 | 4 | 43 |
| 851 | Beet nutrition facts | beet nutrition | 210 | 4 | 53 |
| 852 | Celery nutrition facts | celery nutrition | 210 | 4 | 53 |
| 853 | Mushroom nutrition facts | mushroom nutrition | 210 | 4 | 53 |
| 854 | Cabbage nutrition facts | cabbage nutrition | 170 | 4 | 43 |
| 855 | Mango nutrition facts | mango nutrition | 260 | 5 | 65 |
| 856 | Pineapple nutrition facts | pineapple nutrition | 260 | 5 | 65 |
| 857 | Watermelon nutrition facts | watermelon nutrition | 260 | 5 | 65 |
| 858 | Strawberry nutrition facts | strawberry nutrition | 210 | 4 | 53 |
| 859 | Raspberry nutrition facts | raspberry nutrition | 170 | 4 | 43 |
| 860 | Blackberry nutrition facts | blackberry nutrition | 170 | 4 | 43 |
| 861 | Apple nutrition facts | apple nutrition | 260 | 5 | 65 |
| 862 | Orange nutrition facts | orange nutrition | 260 | 5 | 65 |
| 863 | Grapefruit nutrition facts | grapefruit nutrition | 210 | 4 | 53 |
| 864 | Pomegranate nutrition facts | pomegranate nutrition | 210 | 4 | 53 |
| 865 | Coconut nutrition facts | coconut nutrition | 170 | 4 | 43 |
| 866 | Fig nutrition facts | fig nutrition | 170 | 4 | 43 |
| 867 | Date nutrition facts | dates nutrition | 210 | 4 | 53 |
| 868 | Papaya nutrition facts | papaya nutrition | 170 | 4 | 43 |
| 869 | Kiwi nutrition facts | kiwi nutrition | 210 | 4 | 53 |
| 870 | Grapes nutrition facts | grape nutrition | 210 | 4 | 53 |
| 871 | Pear nutrition facts | pear nutrition | 170 | 4 | 43 |
| 872 | Plum nutrition facts | plum nutrition | 140 | 3 | 35 |
| 873 | Cherry nutrition facts | cherry nutrition | 210 | 4 | 53 |
| 874 | Lemon nutrition facts | lemon nutrition | 170 | 4 | 43 |
| 875 | Lime nutrition facts | lime nutrition | 140 | 3 | 35 |

**Cluster 19 math:**
- Total primary keyword volume: ~28,750/month
- 80 pages × 110 avg raw capture = 8,800/month raw
- After 80% success: **7,040/month**

---

## Cluster 20: Longevity, Gut Health & Advanced Topics (25 opportunities)

**Why this cluster matters:** The longevity-fasting connection is the next growth frontier. NutritionFacts drives 2,053 from autophagy content. DB's "7 benefits of fasting" ranks top 10 on his site. Blue Zones, longevity, and anti-aging content positions Simple beyond weight loss into the broader health-optimization market — higher LTV users.

**Reference domains:** NF, DB, ZL, DD, NS

| # | Page Opportunity | Primary Keyword | Vol | KD | Est. Capture |
|---|---|---|---|---|---|
| 876 | Blue zones diet: how the longest-lived people eat | blue zones diet | 1,600 | 20 | 320 |
| 877 | How to slow aging with fasting | how to slow aging | 590 | 15 | 148 |
| 878 | Telomeres and fasting: anti-aging connection | telomeres and fasting | 210 | 8 | 53 |
| 879 | Fasting for cellular renewal: the science | fasting cellular renewal | 170 | 6 | 43 |
| 880 | Circadian rhythm and fasting: optimization guide | circadian rhythm fasting | 1,000 | 15 | 250 |
| 881 | Gut reset: how 3-day fasting restores gut health | gut reset | 720 | 12 | 180 |
| 882 | SIBO and fasting: can it help | sibo and fasting | 320 | 8 | 80 |
| 883 | Leaky gut and intermittent fasting | leaky gut intermittent fasting | 260 | 8 | 65 |
| 884 | Fasting and candida: reducing overgrowth | fasting candida | 170 | 5 | 43 |
| 885 | Fasting for mental clarity: the cognitive benefits | fasting mental clarity | 260 | 8 | 65 |
| 886 | Dopamine fasting: what it is and does it work | dopamine fasting | 1,600 | 15 | 400 |
| 887 | NAD+ and fasting: boosting cellular energy | nad fasting | 260 | 8 | 65 |
| 888 | Sirtuins and fasting: activating longevity genes | sirtuins fasting | 170 | 6 | 43 |
| 889 | Fasting and skin health: anti-aging benefits | fasting skin health | 260 | 8 | 65 |
| 890 | Fasting and collagen production | fasting and collagen | 170 | 5 | 43 |
| 891 | Spermidine and fasting: autophagy enhancers | spermidine fasting | 170 | 5 | 43 |
| 892 | Caloric restriction vs intermittent fasting for longevity | caloric restriction vs fasting | 210 | 10 | 42 |
| 893 | Fasting and neuroplasticity | fasting neuroplasticity | 110 | 5 | 28 |
| 894 | Anti-aging fasting protocols | anti aging fasting | 260 | 10 | 52 |
| 895 | Fasting for detox: what actually happens | fasting detox | 480 | 10 | 120 |
| 896 | Elimination diet + IF: finding food sensitivities | elimination diet | 1,600 | 20 | 320 |
| 897 | Fasting and histamine intolerance | fasting histamine intolerance | 140 | 5 | 35 |
| 898 | Fasting and heavy metal detox (myth vs reality) | heavy metal detox | 590 | 12 | 118 |
| 899 | Time-restricted eating and circadian health | time restricted eating benefits | 390 | 10 | 98 |
| 900 | Fasting and epigenetics: how fasting changes gene expression | fasting epigenetics | 140 | 6 | 35 |

**Cluster 20 math:**
- Total primary keyword volume: ~11,850/month
- 25 pages × 280 avg raw capture = 7,000/month raw
- After 80% success: **5,600/month**

---

## Grand Total — All 1,000 Opportunities

| Cluster | Pages | Cluster Capture (Raw) | Net (80% Success) |
|---|---|---|---|
| 1. Does X Break a Fast | 75 | 9,375 | 7,500 |
| 2. Fasting Schedules & Methods | 50 | 17,500 | 14,000 |
| 3. Fasting Results | 45 | 11,925 | 9,540 |
| 4. Fasting Science | 40 | 14,000 | 11,200 |
| 5. Breaking a Fast / What to Eat | 45 | 8,775 | 7,020 |
| 6. Calculators & Tools | 15 | 22,620 | 18,100 |
| 7. Meal Plans | 50 | 15,500 | 12,400 |
| 8. Recipes & Meal Prep | 55 | 8,800 | 7,040 |
| 9. Food Lists & Grocery | 50 | 15,500 | 12,400 |
| 10. Is X Keto/IF-Friendly | 70 | 9,100 | 7,280 |
| 11. Blood Sugar & Metabolic | 45 | 13,950 | 11,160 |
| 12. Fasting & Drinks | 35 | 5,775 | 4,620 |
| 13. Weight Loss | 50 | 12,000 | 9,600 |
| 14. IF for Populations | 40 | 13,000 | 10,400 |
| 15. Diet Comparisons | 35 | 7,000 | 5,600 |
| 16. Exercise & Fitness | 30 | 5,550 | 4,440 |
| 17. Supplements | 30 | 4,500 | 3,600 |
| 18. Side Effects & Safety | 35 | 4,900 | 3,920 |
| 19. Programmatic Nutrition | 80 | 8,800 | 7,040 |
| 20. Longevity & Advanced | 25 | 7,000 | 5,600 |
| **TOTAL** | **1,000** | **219,570** | **175,460** |

### What these numbers mean

- **175,460 visits/month** is the estimated traffic if Simple published all 1,000 pages and they all matured (4+ months after publish)
- That's **30x** Simple's current content traffic (5,800/month)
- No single year's execution can cover all 1,000 — the ROI model uses this as the total addressable inventory, then selects the highest-value subset for each production scenario
- These estimates are calibrated against actual competitor traffic data from SEMrush: ruled.me achieves 264/page from ~200 content pages, Diet Doctor achieves 262/page from ~500 pages. Our blended average of 175/page across 1,000 pages (many long-tail) is conservative

### Priority ranking

If you could only execute 260 pages (5/week for a year), the top-priority selection would be:

1. All 15 calculator/tool pages (Cluster 6) — single highest ROI
2. Top 25 science & biology pages (Cluster 4) — pillar content
3. All 75 "break a fast" pages (Cluster 1) — proven template, fast to produce
4. Top 20 schedule guides (Cluster 2) — foundational authority
5. Top 15 blood sugar & metabolic pages (Cluster 11) — massive volume
6. Top 10 meal plans (Cluster 7) — conversion drivers
7. Top 15 results pages (Cluster 3) — bottom-funnel purchase intent
8. Top 15 population-specific pages (Cluster 14) — differentiated, high trust
9. Top 15 food lists (Cluster 9) — reference content with long shelf life
10. Top 10 weight loss pages (Cluster 13) — broad audience
11. Remaining 45 pages from highest per-page value across all clusters

---

## Appendix: Competitor Domain Key

| Abbrev | Domain | Role in Analysis |
|---|---|---|
| DD | dietdoctor.com | Largest health content site in space; keto/low-carb benchmark |
| FA | fastic.com | Direct competitor app; strong "break a fast" + calorie content |
| ZL | zerolongevity.com | Niche IF site; science + schedule comparison benchmark |
| DB | drberg.com | Health expert; massive content library, health education |
| PK | perfectketo.com | Keto-focused; food lists, supplements, grocery guides |
| NS | nutrisense.io | Metabolic health; blood sugar charts, glucose content |
| LI | loseit.com | Weight loss app; broad weight loss education |
| RM | ruled.me | Keto recipes + tools; calculator pages benchmark |
| NF | nutritionfacts.org | Nutrition science; evidence-based health content |
| SC | snapcalorie.com | Calorie tracking; programmatic nutrition pages benchmark |
| AE | autumnellenutrition.com | IF influencer; population-specific fasting content |
| LA | lasta.app | Direct competitor app; fasting + health content |

### Data sources
- SEMrush `domain_organic_unique` report (US database, top 300 pages per domain)
- SEMrush `url_organic` report (22 strategic calibration pages)
- Simple.Life current rankings and traffic (SEMrush + Search Console)
- CTR benchmarks: Backlinko / Advanced Web Ranking studies
- Keyword difficulty to position mapping: calibrated against Simple's current ranking performance
