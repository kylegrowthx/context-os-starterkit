# Presence Score Analysis — Flodesk & Competitors

<metadata>
purpose: Calculated Presence Scores for Flodesk and 28 tracked competitors using the CheckThat tiered component model
audience: GrowthX delivery team, Flodesk stakeholders
related_files:
  - projects/audit-reports/flodesk/aeo/aeo-audit-report-v1.md
  - projects/audit-reports/flodesk/aeo/competitive-visibility-dump-v1.md
  - projects/audit-reports/flodesk/aeo/source-analysis-v1.md
domain: AEO audit
confidence: high — calculated from 109,509 probes across 20 weeks of data
last_updated: 2026-03-01
</metadata>

## Methodology

Scores calculated using the CheckThat Presence Score formula — a **tiered component model** where Presence Rate is the foundation (70% of total points) and four quality tiers contribute the remaining 30 points, each gated by Rate so they can't inflate a near-zero score.

### Formula

```
TIER 1 — VISIBILITY (0-70 pts)    = 70 × (Rate / 100)
TIER 2 — DURABILITY (0-9 pts)     = 9 × (Stability / 100) × (Rate / 100)
TIER 3 — POSITION (0-8 pts)       = 8 × (Position / 100) × √(Rate / 100)
TIER 4 — SOURCE CONTROL (0-8 pts) = 8 × (SourceControl / 100) × √(Rate / 100)
TIER 5 — COVERAGE (0-5 pts)       = 5 × (CrossEngine / 100) × √(Rate / 100)

PRESENCE SCORE = T1 + T2 + T3 + T4 + T5   (Scale: 0-100)
```

### Data inputs

| Sub-metric | Definition | Source |
|---|---|---|
| **Presence Rate** | % of evaluation-stage, unbranded probes where brand is mentioned | `probe_mentions` / total probes (109,509) |
| **Stability Index** | 100 − coefficient of variation of weekly presence rates | Standard deviation / mean of 20 weekly rate snapshots |
| **Position** | Average rank quality when mentioned (Recommended=5, 1st=4, 2nd-3rd=3, Listed=2, Afterthought=1), normalized to 0-100 | `probe_mentions.rank` mapped to position tiers |
| **Source Control** | % of citation-bearing probes that cite the brand's own domain | `probe_citations.domain` matched to brand domain |
| **Cross-Engine Coverage** | % of tracked AI engines (5) that mention the brand | Distinct `probes.vendor` per brand |

### Interpretation scale

| Range | Rating | Meaning |
|---|---|---|
| 85-100 | Exceptional | Near-perfection. Practically unreachable. |
| 70-84 | Strong | Dominant category presence. Very few B2B brands reach this. |
| 50-69 | Moderate | Clear presence with room to grow. Upper end of what leaders achieve. |
| 30-49 | Low | Inconsistent. ~Coin-flip chance buyers see you. Typical for established brands. |
| 10-29 | Weak | Rarely recommended. Most AI-assisted shortlists miss you. |
| 0-9 | Invisible | AI doesn't mention you during evaluation. |

---

## Presence Score Rankings

| Rank | Brand | Presence Score | Rating | T1 Visibility | T2 Durability | T3 Position | T4 Source Ctrl | T5 Coverage |
|---:|---|---:|---|---:|---:|---:|---:|---:|
| 1 | Klaviyo | **47.0** | Low | 35.2 | 4.3 | 3.0 | 1.0 | 3.5 |
| 2 | Mailchimp | **46.4** | Low | 34.7 | 4.2 | 3.5 | 0.6 | 3.5 |
| 3 | Brevo | **45.1** | Low | 33.9 | 4.1 | 3.0 | 0.7 | 3.5 |
| 4 | HubSpot | **41.7** | Low | 31.6 | 3.5 | 2.9 | 0.3 | 3.4 |
| 5 | Omnisend | **41.1** | Low | 31.5 | 3.7 | 2.3 | 0.3 | 3.4 |
| 6 | ActiveCampaign | **40.6** | Low | 30.5 | 3.7 | 2.9 | 0.3 | 3.3 |
| 7 | MailerLite | **37.2** | Low | 27.5 | 3.3 | 2.9 | 0.3 | 3.1 |
| 8 | GetResponse | **23.1** | Weak | 17.1 | 1.9 | 1.5 | 0.1 | 2.5 |
| 9 | Moosend | **21.7** | Weak | 15.6 | 1.6 | 1.6 | 0.5 | 2.4 |
| 10 | Constant Contact | **19.7** | Weak | 14.4 | 1.5 | 1.5 | 0.0 | 2.3 |
| 11 | Kit | **19.4** | Weak | 14.3 | 1.3 | 1.4 | 0.0 | 2.3 |
| 12 | Sender | **18.4** | Weak | 12.7 | 1.3 | 1.4 | 0.8 | 2.1 |
| 13 | Campaign Monitor | **8.3** | Invisible | 5.4 | 0.6 | 0.9 | 0.1 | 1.4 |
| 14 | Drip | **7.9** | Invisible | 5.2 | 0.6 | 0.8 | 0.0 | 1.4 |
| 15 | EmailOctopus | **7.2** | Invisible | 4.7 | 0.5 | 0.7 | 0.0 | 1.3 |
| 16 | Mailjet | **4.5** | Invisible | 2.7 | 0.2 | 0.5 | 0.0 | 1.0 |
| **17** | **Flodesk** | **3.8** | **Invisible** | **2.2** | **0.2** | **0.5** | **0.0** | **0.9** |
| 18 | SendPulse | **3.0** | Invisible | 1.7 | 0.1 | 0.4 | 0.0 | 0.8 |
| 19 | Benchmark Email | **2.8** | Invisible | 1.5 | 0.1 | 0.4 | 0.0 | 0.7 |
| 20 | Customer.io | **2.7** | Invisible | 1.4 | 0.1 | 0.4 | 0.0 | 0.7 |
| 21 | Ghost | **2.3** | Invisible | 1.1 | 0.1 | 0.4 | 0.0 | 0.6 |
| 22 | Keap | **2.2** | Invisible | 1.0 | 0.1 | 0.5 | 0.0 | 0.6 |
| 23 | AWeber | **2.1** | Invisible | 1.1 | 0.1 | 0.3 | 0.0 | 0.5 |
| 24 | Squarespace | **1.3** | Invisible | 0.5 | 0.1 | 0.3 | 0.0 | 0.4 |
| 25 | Ontraport | **1.3** | Invisible | 0.4 | 0.0 | 0.5 | 0.0 | 0.4 |
| 26 | iContact | **1.3** | Invisible | 0.6 | 0.0 | 0.2 | 0.0 | 0.4 |
| 27 | Systeme.io | **0.6** | Invisible | 0.2 | 0.0 | 0.2 | 0.0 | 0.3 |
| 28 | Kajabi | **0.2** | Invisible | 0.1 | 0.0 | 0.1 | 0.0 | 0.1 |
| 29 | Kartra | **0.1** | Invisible | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

---

## Sub-Metric Detail

### Presence Rate (drives 70% of score)

The percentage of 109,509 evaluation-stage, unbranded probes where AI mentions the brand.

| Brand | Probes Mentioned | Presence Rate |
|---|---:|---:|
| Klaviyo | 55,133 | 50.35% |
| Mailchimp | 54,316 | 49.60% |
| Brevo | 53,003 | 48.40% |
| HubSpot | 49,502 | 45.20% |
| Omnisend | 49,216 | 44.94% |
| ActiveCampaign | 47,696 | 43.55% |
| MailerLite | 43,056 | 39.32% |
| GetResponse | 26,719 | 24.40% |
| Moosend | 24,414 | 22.29% |
| Constant Contact | 22,475 | 20.52% |
| Kit | 22,403 | 20.46% |
| Sender | 19,919 | 18.19% |
| Campaign Monitor | 8,456 | 7.72% |
| Drip | 8,095 | 7.39% |
| EmailOctopus | 7,403 | 6.76% |
| Mailjet | 4,209 | 3.84% |
| **Flodesk** | **3,466** | **3.17%** |
| SendPulse | 2,670 | 2.44% |
| Benchmark Email | 2,380 | 2.17% |
| Customer.io | 2,239 | 2.04% |
| Ghost | 1,784 | 1.63% |
| AWeber | 1,746 | 1.59% |
| Keap | 1,561 | 1.43% |
| iContact | 878 | 0.80% |
| Squarespace | 782 | 0.71% |
| Ontraport | 623 | 0.57% |
| Systeme.io | 297 | 0.27% |
| Kajabi | 84 | 0.08% |
| Kartra | 16 | 0.01% |

### Stability Index

How consistent the weekly presence rate is over time. Higher = more entrenched. Calculated as 100 − (coefficient of variation of weekly rates).

| Brand | Avg Weekly Rate | CV% | Stability Index | Weeks |
|---|---:|---:|---:|---:|
| MailerLite | 39.50% | 6.03% | 93.97 | 20 |
| Klaviyo | 50.23% | 6.12% | 93.88 | 20 |
| ActiveCampaign | 43.26% | 6.80% | 93.20 | 20 |
| Brevo | 48.18% | 6.97% | 93.03 | 20 |
| Mailchimp | 48.95% | 7.01% | 92.99 | 20 |
| Omnisend | 45.15% | 7.78% | 92.22 | 20 |
| HubSpot | 44.81% | 13.53% | 86.47 | 20 |
| GetResponse | 24.19% | 13.97% | 86.03 | 20 |
| Squarespace | 0.70% | 16.70% | 83.30 | 20 |
| Campaign Monitor | 7.65% | 16.11% | 83.89 | 20 |
| Constant Contact | 20.63% | 16.48% | 83.52 | 20 |
| Drip | 7.57% | 16.95% | 83.05 | 20 |
| Moosend | 22.48% | 20.24% | 79.76 | 20 |
| Sender | 18.44% | 19.65% | 80.35 | 20 |
| Keap | 1.40% | 21.28% | 78.72 | 20 |
| EmailOctopus | 6.71% | 25.25% | 74.75 | 20 |
| Kit | 20.13% | 28.26% | 71.74 | 20 |
| AWeber | 8.14% | 28.47% | 71.53 | 5 |
| Mailjet | 3.73% | 27.91% | 72.09 | 20 |
| **Flodesk** | **2.99%** | **30.27%** | **69.73** | **20** |
| Customer.io | 2.13% | 30.26% | 69.74 | 20 |
| Ghost | 1.68% | 33.30% | 66.70 | 20 |
| Benchmark Email | 2.29% | 35.71% | 64.29 | 20 |
| SendPulse | 2.30% | 36.97% | 63.03 | 20 |
| Ontraport | 0.54% | 36.54% | 63.46 | 19 |
| iContact | 0.82% | 40.93% | 59.07 | 20 |
| Kartra | 0.03% | 41.14% | 58.86 | 10 |
| Systeme.io | 0.29% | 63.20% | 36.80 | 18 |
| Kajabi | 0.08% | 71.63% | 28.37 | 19 |

### Position Score

Average quality of rank when mentioned. Scale: Recommended=5, 1st=4, 2nd-3rd=3, Listed=2, Afterthought=1. Normalized to 0-100%.

| Brand | Avg Position Score (1-5) | Position % |
|---|---:|---:|
| Ontraport | 4.36 | 87.2% |
| Mailchimp | 3.08 | 61.5% |
| MailerLite | 2.89 | 57.8% |
| ActiveCampaign | 2.75 | 55.0% |
| Brevo | 2.71 | 54.1% |
| HubSpot | 2.66 | 53.2% |
| Klaviyo | 2.63 | 52.5% |
| Keap | 2.51 | 50.1% |
| Squarespace | 2.32 | 46.4% |
| Omnisend | 2.14 | 42.8% |
| Moosend | 2.08 | 41.6% |
| Constant Contact | 2.04 | 40.9% |
| Sender | 2.03 | 40.6% |
| Kartra | 2.00 | 40.0% |
| Kit | 1.96 | 39.3% |
| GetResponse | 1.95 | 39.1% |
| Campaign Monitor | 1.95 | 39.0% |
| Ghost | 1.89 | 37.9% |
| Systeme.io | 1.88 | 37.5% |
| Customer.io | 1.76 | 35.2% |
| Drip | 1.75 | 35.0% |
| **Flodesk** | **1.72** | **34.4%** |
| AWeber | 1.71 | 34.2% |
| Benchmark Email | 1.71 | 34.2% |
| Mailjet | 1.68 | 33.7% |
| EmailOctopus | 1.60 | 32.0% |
| SendPulse | 1.53 | 30.6% |
| iContact | 1.51 | 30.3% |
| Kajabi | 1.48 | 29.5% |

### Source Control

Share of citation-bearing probes (77,042 total) that cite the brand's own domain.

| Brand | Probes Citing Domain | Source Control % |
|---|---:|---:|
| Sender | 17,744 | 23.03% |
| Klaviyo | 13,065 | 16.96% |
| Moosend | 10,805 | 14.02% |
| Brevo | 9,619 | 12.49% |
| Mailchimp | 8,030 | 10.42% |
| MailerLite | 4,902 | 6.36% |
| HubSpot | 4,823 | 6.26% |
| Omnisend | 3,937 | 5.11% |
| ActiveCampaign | 3,833 | 4.98% |
| Campaign Monitor | 2,347 | 3.05% |
| GetResponse | 1,251 | 1.62% |
| Mailjet | 834 | 1.08% |
| Drip | 765 | 0.99% |
| Constant Contact | 764 | 0.99% |
| Kit | 567 | 0.74% |
| Customer.io | 466 | 0.60% |
| iContact | 419 | 0.54% |
| Keap | 364 | 0.47% |
| Ontraport | 364 | 0.47% |
| SendPulse | 316 | 0.41% |
| Benchmark Email | 284 | 0.37% |
| EmailOctopus | 246 | 0.32% |
| AWeber | 161 | 0.21% |
| Systeme.io | 106 | 0.14% |
| Ghost | 48 | 0.06% |
| **Flodesk** | **46** | **0.06%** |
| Squarespace | 32 | 0.04% |
| Kartra | 12 | 0.02% |
| Kajabi | 5 | 0.01% |

### Cross-Engine Coverage

Percentage of 5 tracked AI engines that mention the brand for evaluation prompts.

| Brand | Engines | Coverage |
|---|---:|---:|
| 26 brands | 5/5 | 100% |
| AWeber | 4/5 | 80% |
| Kajabi | 3/5 | 60% |
| Kartra | 3/5 | 60% |

Nearly all brands achieve full engine coverage — this sub-metric provides minimal differentiation in this category.

---

## Flodesk Deep Dive

### Score breakdown

| Component | Raw Metric | Contribution | Max |
|---|---|---:|---:|
| **T1 — Visibility** | Rate: 3.17% | 2.2 | 70 |
| **T2 — Durability** | Stability: 69.73 | 0.2 | 9 |
| **T3 — Position** | Position: 34.4% | 0.5 | 8 |
| **T4 — Source Control** | Source Control: 0.06% | 0.0 | 8 |
| **T5 — Coverage** | Coverage: 100% | 0.9 | 5 |
| **TOTAL** | | **3.8** | **100** |

### What this means

Flodesk ranks **#17 of 29** tracked competitors with a Presence Score of **3.8** — rated **Invisible**.

The score is almost entirely Tier 1 (Visibility). With a 3.17% Presence Rate, Flodesk is mentioned in only ~1 in 32 evaluation-stage probes. The gating functions mean the quality tiers (Position, Source Control, Coverage) can barely contribute — even though Flodesk has 100% engine coverage, that excellent coverage only adds 0.9 points because the sqrt gate at 3.17% Rate caps it.

### Tier-by-tier diagnosis

**T1 — Visibility (2.2 / 70):** The core problem. Flodesk is mentioned in 3,466 of 109,509 probes. The top 7 competitors are mentioned in 40-50% of probes. This is a 13-16x gap.

**T2 — Durability (0.2 / 9):** Stability Index of 69.73 is below average (most leaders are >90). But with such a low Rate, the linear gate means this metric barely registers. Even if Flodesk had perfect stability (100), T2 would only contribute 0.3 points.

**T3 — Position (0.5 / 8):** When Flodesk IS mentioned, its average position score is 1.72/5 — meaning it's typically "Listed" or "Afterthought" rather than "Recommended." This is near the bottom of all competitors.

**T4 — Source Control (0.0 / 8):** Only 46 of 77,042 citation-bearing probes cite flodesk.com. This is functionally zero. AI engines don't use Flodesk's content as source material. Compare to Sender (23%), Klaviyo (17%), Moosend (14%).

**T5 — Coverage (0.9 / 5):** The one bright spot. Flodesk is mentioned across all 5 tracked engines. But the sqrt gate at 3.17% Rate means this can only contribute 0.9 of 5 possible points.

### Distance to competitive tiers

| Target | Required Rate | Gap from Current | What it means |
|---|---:|---|---|
| Exit Invisible (≥10) | ~14% | +11 pts Rate | AI mentions Flodesk in 1 of 7 evaluation probes |
| Match Sender (#12) | ~18% | +15 pts Rate | Comparable to the low end of "Weak" tier |
| Match Kit (#11) | ~20% | +17 pts Rate | Regular appearance in shortlists |
| Match GetResponse (#8) | ~24% | +21 pts Rate | Consistent mid-tier presence |
| Match category leaders | ~45-50% | +42-47 pts Rate | Top 7 all cluster here |

---

## Competitive Tiers

### Tier 1 — The Leaders (Score 37-47)

Seven brands form a tight competitive cluster with Presence Scores of 37-47, all rated "Low" but far ahead of everyone else. They share: >39% Presence Rate, >92 Stability Index, and 100% engine coverage.

| Brand | Score | Rate | Stability | Position | Source Ctrl | Coverage |
|---|---:|---:|---:|---:|---:|---:|
| Klaviyo | 47.0 | 50.35% | 93.88 | 52.5% | 16.96% | 100% |
| Mailchimp | 46.4 | 49.60% | 92.99 | 61.5% | 10.42% | 100% |
| Brevo | 45.1 | 48.40% | 93.03 | 54.1% | 12.49% | 100% |
| HubSpot | 41.7 | 45.20% | 86.47 | 53.2% | 6.26% | 100% |
| Omnisend | 41.1 | 44.94% | 92.22 | 42.8% | 5.11% | 100% |
| ActiveCampaign | 40.6 | 43.55% | 93.20 | 55.0% | 4.98% | 100% |
| MailerLite | 37.2 | 39.32% | 93.97 | 57.8% | 6.36% | 100% |

**Key insight:** No brand in this category reaches "Moderate" (50+). This is a crowded, contested market where even leaders can't dominate. Klaviyo barely edges Mailchimp despite higher Rate because Mailchimp has significantly better Position (61.5% vs 52.5%).

### Tier 2 — Established Challengers (Score 18-23)

Five brands with consistent but limited presence. They appear in roughly 1 in 4-5 evaluation probes.

| Brand | Score | Rate | Stability | Position | Source Ctrl | Coverage |
|---|---:|---:|---:|---:|---:|---:|
| GetResponse | 23.1 | 24.40% | 86.03 | 39.1% | 1.62% | 100% |
| Moosend | 21.7 | 22.29% | 79.76 | 41.6% | 14.02% | 100% |
| Constant Contact | 19.7 | 20.52% | 83.52 | 40.9% | 0.99% | 100% |
| Kit | 19.4 | 20.46% | 71.74 | 39.3% | 0.74% | 100% |
| Sender | 18.4 | 18.19% | 80.35 | 40.6% | 23.03% | 100% |

**Key insight:** Sender has the highest Source Control of ANY brand (23%) but ranks only #12 overall because its Rate is too low. Moosend similarly punches above its weight on Source Control (14%). These brands have strong owned content that AI cites, but the category conversation still passes them by.

### Tier 3 — Fringe (Score 7-9)

Three brands at the edge of visibility. Mentioned in ~7-8% of probes.

| Brand | Score | Rate |
|---|---:|---:|
| Campaign Monitor | 8.3 | 7.72% |
| Drip | 7.9 | 7.39% |
| EmailOctopus | 7.2 | 6.76% |

### Tier 4 — Invisible (Score 0-5)

**Thirteen brands including Flodesk** that AI effectively doesn't recommend during evaluation.

| Brand | Score | Rate |
|---|---:|---:|
| Mailjet | 4.5 | 3.84% |
| **Flodesk** | **3.8** | **3.17%** |
| SendPulse | 3.0 | 2.44% |
| Benchmark Email | 2.8 | 2.17% |
| Customer.io | 2.7 | 2.04% |
| Ghost | 2.3 | 1.63% |
| Keap | 2.2 | 1.43% |
| AWeber | 2.1 | 1.59% |
| Squarespace | 1.3 | 0.71% |
| Ontraport | 1.3 | 0.57% |
| iContact | 1.3 | 0.80% |
| Systeme.io | 0.6 | 0.27% |
| Kajabi | 0.2 | 0.08% |
| Kartra | 0.1 | 0.01% |

---

## Strategic Implications for Flodesk

### The math is clear

At 3.17% Presence Rate, the gating functions ensure that no quality improvement can meaningfully move the score. If Flodesk somehow achieved perfect Position (5/5 on every mention), perfect Stability (100), maximum Source Control, and full Coverage — the score would still be under 7. **Rate is the only lever that matters at this level.**

### Source Control is the structural weakness

Flodesk's 0.06% Source Control is the lowest of all established brands. Only 46 probes out of 77,042 cite flodesk.com as a source. This means:
- AI engines don't use Flodesk's website as reference material
- Flodesk's presence is entirely dependent on third-party content
- Any visibility Flodesk has is fragile and can shift without warning

Compare: Sender (23%), Klaviyo (17%), Moosend (14%) — these brands have defensible presence because AI cites their own content.

### Position quality is also weak

When Flodesk IS mentioned, it scores 1.72/5 on Position — meaning it's typically listed as an afterthought rather than recommended. The top brands score 2.6-3.1, and Mailchimp reaches 3.08 (regularly named as a primary recommendation).

### Priority actions

1. **Build citeable content on flodesk.com** — comparison pages, feature guides, pricing pages, "best of" lists for the use cases Flodesk wins (creators, designers, visual email)
2. **Target the prompts where Flodesk should win** — Flodesk's differentiator (beautiful email design for creators) doesn't map to generic "best email marketing" probes. Building content around specific niches could establish presence in a subset of evaluation queries
3. **Earn third-party coverage** — listicles, review sites, and comparison articles that name Flodesk prominently (not as an afterthought)
4. **Improve crawlability and structured data** — ensure AI engines can discover and index Flodesk's content as source material

---

## Raw Sub-Metric Data

### All brands — complete calculation inputs

| Brand | Rate % | Stability | Position % | Source Ctrl % | Coverage % | **Score** |
|---|---:|---:|---:|---:|---:|---:|
| Klaviyo | 50.35 | 93.88 | 52.5 | 16.96 | 100 | **47.0** |
| Mailchimp | 49.60 | 92.99 | 61.5 | 10.42 | 100 | **46.4** |
| Brevo | 48.40 | 93.03 | 54.1 | 12.49 | 100 | **45.1** |
| HubSpot | 45.20 | 86.47 | 53.2 | 6.26 | 100 | **41.7** |
| Omnisend | 44.94 | 92.22 | 42.8 | 5.11 | 100 | **41.1** |
| ActiveCampaign | 43.55 | 93.20 | 55.0 | 4.98 | 100 | **40.6** |
| MailerLite | 39.32 | 93.97 | 57.8 | 6.36 | 100 | **37.2** |
| GetResponse | 24.40 | 86.03 | 39.1 | 1.62 | 100 | **23.1** |
| Moosend | 22.29 | 79.76 | 41.6 | 14.02 | 100 | **21.7** |
| Constant Contact | 20.52 | 83.52 | 40.9 | 0.99 | 100 | **19.7** |
| Kit | 20.46 | 71.74 | 39.3 | 0.74 | 100 | **19.4** |
| Sender | 18.19 | 80.35 | 40.6 | 23.03 | 100 | **18.4** |
| Campaign Monitor | 7.72 | 83.89 | 39.0 | 3.05 | 100 | **8.3** |
| Drip | 7.39 | 83.05 | 35.0 | 0.99 | 100 | **7.9** |
| EmailOctopus | 6.76 | 74.75 | 32.0 | 0.32 | 100 | **7.2** |
| Mailjet | 3.84 | 72.09 | 33.7 | 1.08 | 100 | **4.5** |
| **Flodesk** | **3.17** | **69.73** | **34.4** | **0.06** | **100** | **3.8** |
| SendPulse | 2.44 | 63.03 | 30.6 | 0.41 | 100 | **3.0** |
| Benchmark Email | 2.17 | 64.29 | 34.2 | 0.37 | 100 | **2.8** |
| Customer.io | 2.04 | 69.74 | 35.2 | 0.60 | 100 | **2.7** |
| Ghost | 1.63 | 66.70 | 37.9 | 0.06 | 100 | **2.3** |
| Keap | 1.43 | 78.72 | 50.1 | 0.47 | 100 | **2.2** |
| AWeber | 1.59 | 71.53 | 34.2 | 0.21 | 80 | **2.1** |
| Squarespace | 0.71 | 83.30 | 46.4 | 0.04 | 100 | **1.3** |
| Ontraport | 0.57 | 63.46 | 87.2 | 0.47 | 100 | **1.3** |
| iContact | 0.80 | 59.07 | 30.3 | 0.54 | 100 | **1.3** |
| Systeme.io | 0.27 | 36.80 | 37.5 | 0.14 | 100 | **0.6** |
| Kajabi | 0.08 | 28.37 | 29.5 | 0.01 | 60 | **0.2** |
| Kartra | 0.01 | 58.86 | 40.0 | 0.02 | 60 | **0.1** |
