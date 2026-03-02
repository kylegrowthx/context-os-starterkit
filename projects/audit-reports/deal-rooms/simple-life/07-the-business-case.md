---
section: 7
title: "The Business Case"
subtitle: "What this is worth, what it costs, and why the math works even in the downside"
stats:
  - label: "M12 Monthly LTV (10/week)"
    value: "$62,020"
    delta: "vs. $30,000 cost"
  - label: "M12 CPA (Content)"
    value: "$34"
    delta: "Decreasing every month"
  - label: "Equivalent Ad Spend (M12)"
    value: "$211,110/mo"
    delta: "7.0x the content investment"
  - label: "24-Month Cumulative ROI"
    value: "+56%"
    delta: "$1.12M LTV vs. $720K invested"
tables:
  - id: "scenario-financials"
    caption: "Financial comparison across scenarios"
    columns: ["Metric", "10/week", "20/week"]
    rows:
      - ["Monthly cost", "$30,000", "$45,000"]
      - ["M12 monthly LTV", "$62,020", "$90,720"]
      - ["M12 monthly margin", "+$32,020", "+$45,720"]
      - ["M12 CPA", "$34", "$35"]
      - ["Cash-flow positive", "Month 6", "Month 6"]
      - ["Cumulative breakeven", "Month 14", "Month 14"]
      - ["24-month cumulative ROI", "+56%", "+57%"]
  - id: "cpa-comparison"
    caption: "CPA comparison: content vs. paid"
    columns: ["Channel", "Monthly Cost", "M12 Purchases", "CPA", "Trend"]
    rows:
      - ["Meta ads (current)", "~$1,000,000", "~757 (site-wide)", "Rising", "Increasing"]
      - ["Content 10/week", "$30,000", "886 incremental", "$34", "Decreasing"]
      - ["Content 20/week", "$45,000", "1,296 incremental", "$35", "Decreasing"]
  - id: "equivalent-ad-spend"
    caption: "What this traffic would cost in ads"
    columns: ["Scenario", "M12 Incremental Visits", "Equivalent Ad Spend", "vs. Content Cost"]
    rows:
      - ["10/week", "113,500", "$211,110/mo", "7.0x"]
      - ["20/week", "165,500", "$307,830/mo", "6.8x"]
  - id: "cumulative-roi"
    caption: "Cumulative investment vs. LTV created"
    columns: ["Time Horizon", "10/week Investment", "10/week LTV", "20/week Investment", "20/week LTV"]
    rows:
      - ["12 months", "$360,000", "$297,500", "$540,000", "$453,000"]
      - ["18 months", "$540,000", "$660,000", "$810,000", "$1,020,000"]
      - ["24 months", "$720,000", "$1,120,000", "$1,080,000", "$1,700,000"]
callouts:
  - text: "By month 12, both scenarios generate traffic worth 7x the monthly content investment in equivalent ad spend."
    type: "highlight"
  - text: "Bear case (-20% on all assumptions): both scenarios stay cash-flow positive. 10/week at +$10,600/mo margin. 20/week at +$14,850/mo."
    type: "highlight"
  - text: "By month 24, the 10/week program generates $84,000/month in LTV against $30,000/month in cost."
    type: "highlight"
---

## Building vs. renting

**Building (organic + AI).** You build equity. Every improvement increases the value of everything you've already built. When you stop building, you still own the asset. The more you invest, the cheaper each visit gets.

**Renting (paid + outbound).** You get what you need, right when you need it. But equity is zero. When you stop paying, everything goes to zero. And the longer you rent, the more the landlord charges.

Organic compounds. Paid diminishes. Over any 12+ month window, organic wins on total ROI.

---

## The numbers

### CPA trajectory

Content CPA drops every month because the asset keeps producing without additional per-unit cost:

| Timeline | 10/week CPA | 20/week CPA |
|---|---|---|
| Month 6 | $55 | $61 |
| Month 12 | $34 | $35 |
| Month 18 | $27 | $30 |
| Month 24 | $25 | $28 |

Meta ads move the other direction. Every dollar spent after saturation yields less. Simple's current Meta budget is ~$1M/month.

### Revenue projection (10/week, recommended)

| Metric | Month 6 | Month 12 | Month 18 | Month 24 |
|---|---|---|---|---|
| Incremental purchases/month | 547 | 886 | 1,100 | 1,200 |
| Monthly LTV created | $38,290 | $62,020 | $77,000 | $84,000 |
| Monthly engagement cost | $30,000 | $30,000 | $30,000 | $30,000 |
| Monthly net cash flow | +$8,290 | +$32,020 | +$47,000 | +$54,000 |
| Cumulative investment | $180,000 | $360,000 | $540,000 | $720,000 |
| Cumulative LTV created | $90,100 | $297,500 | $660,000 | $1,120,000 |
| Cumulative ROI | -50% | -17% | +22% | +56% |

### Asset value

If Simple stopped investing at month 12, the content would continue generating traffic and purchases. Assuming a 3-year productive life with gradual decay:

| Scenario | M12 Monthly LTV | 3-Year Residual Value (NPV at 10%) | Total Program Value |
|---|---|---|---|
| 10/week | $62,020/mo | ~$1,540,000 | ~$2,000,000 |
| 20/week | $90,720/mo | ~$2,250,000 | ~$2,700,000 |

The 10/week scenario creates an asset worth ~$2M over its productive life against $360K of investment. 5.6x return on invested capital.

---

## The downside check

### Bear case: everything underperforms by 20%

All assumptions at -20%. Lower traffic per page, lower conversion rates, slower AEO ramp:

| Scenario | M12 Purchases (Bear) | Multiple | Monthly LTV | vs. Monthly Cost |
|---|---|---|---|---|
| 10/week | 580 | 10.8x | $40,600 | +$10,600/mo |
| 20/week | 855 | 15.5x | $59,850 | +$14,850/mo |

Even in the bear case, both scenarios stay cash-flow positive with healthy margins. 10/week still exceeds 10x baseline.

### Bull case: AEO overperforms

AEO at +50%, visit-to-download at +20%:

| Scenario | M12 Purchases (Bull) | Multiple | Monthly LTV |
|---|---|---|---|
| 10/week | 1,180 | 21.0x | $82,600 |
| 20/week | 1,700 | 29.8x | $119,000 |

The bull case comes from AEO overperformance. Market AI referral traffic is growing at 527% YoY. Simple is starting from zero, so the upside is asymmetric.

---

## What this adds up to

By month 24, the 10/week program generates $84,000/month in LTV against $30,000/month in cost. CPA drops every month. The content keeps producing whether you keep investing or not.

Stop paying for ads and the traffic disappears. Stop investing in content and it keeps working.
