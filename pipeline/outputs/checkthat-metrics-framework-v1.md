# CheckThat Metrics Framework

<metadata>
purpose: Definitive spec for CheckThat's AI brand perception measurement — 5 core metrics, 3 composites, operational metrics
audience: Product, engineering, leadership
related: pipeline/scratchpad/2026-02-18-checkthat-ontology-product-roadmap-v1.md, context/knowledge/aeo/prompt-taxonomy-and-ontology-v1.md
domain: product-strategy
confidence: high
sensitivity: internal
context_tier: 1
last_updated: 2026-02-13
</metadata>

---

## The Framework

CheckThat surveys AI engines the way brands survey consumers. The measurement framework borrows from brand research — awareness, favorability, accuracy, influence — and applies it to what AI engines say when buyers ask questions.

Three tiers of metrics, each serving a different audience:

```
TIER 1: CORE METRICS ─── The five dimensions of AI brand perception
  Visibility       Does AI mention us?                [output]
  Reputation       How does AI describe us?            [output]
  Alignment        Does AI match our truth?            [output]
  Influence        What shapes AI's perception of us?  [input]
  Lift             Is it getting better?               [change]

TIER 2: COMPOSITES ──── Three headline numbers for leadership
  AI Brand Health        Overall perception score
  AI Share of Voice      Our presence vs competitors
  AI Endorsement         How strongly AI recommends us

TIER 3: OPERATIONAL ─── Daily-use metrics for practitioners
  Position, Stability Index, Cross-Engine Spread,
  Source Pages, Attribute Map, Narrative Frame,
  Feature Accuracy, Pricing Accuracy, etc.
```

The first three core metrics are **output metrics** — what AI says about you. Influence is the **input metric** — what's driving what AI says. Lift is the **change metric** — whether it's moving in the right direction.

This structure has a purpose. Visibility, Reputation, and Alignment tell you what's happening. Influence tells you *why* it's happening and where you have leverage. Lift tells you whether your actions are working. Together they form a complete diagnostic: what, why, and whether.

---

## Core Metric 1: Visibility

**Question:** Does AI mention us?

**Brand research analog:** Brand awareness (unaided and aided)

**Why it matters:** The most fundamental question. If AI doesn't name your brand when buyers ask about your category, nothing else matters. You can have perfect alignment and stellar reputation, but if you're invisible, buyers never see it.

### Sub-metrics

**Visibility Rate** — the headline number

The percentage of tracked prompts where AI mentions your brand.

```
Visibility Rate = (prompts where brand is mentioned / total tracked prompts) × 100
```

Split into two flavors:
- **Unaided Visibility** — mentions in unbranded prompts (category questions, best-of lists, alternatives). The buyer didn't ask about you specifically. AI volunteered your name. This is the high-signal metric — it's the "unaided brand awareness" test.
- **Aided Visibility** — mentions in branded prompts (direct questions about your brand). The buyer asked about you. AI knows who you are. Lower bar but still valuable — some brands aren't even recognized when asked directly.

Data source: `ProbeMention` records where `brand_id` matches workspace brand. Split by `Prompt.branded` flag.

Industry comparison: maps to Brand Mention Rate (Search Engine Land), Inclusion Rate (buyer evaluation playbook), Brand Visibility Score (industry standard).

---

**Position** — where you appear in the response

Not just "are you mentioned?" but "are you first or an afterthought?"

```
Categories:
  1st Mention    — named first in the response
  2nd Mention    — named second
  3rd Mention    — named third
  Listed         — in a list without prominence
  Afterthought   — mentioned in caveats, footnotes, or "you could also consider..."

Position Score = weighted average (1st=5, 2nd=4, 3rd=3, Listed=2, Afterthought=1)
```

Computed by: parsing response text for brand mention location relative to other brands mentioned. LLM-assisted for ambiguous cases.

Aggregate: Position Distribution (% in each category) + average Position Score.

Industry comparison: maps to Position or Rank of Mention, First Mention Rate.

---

**Stability Index** — how consistent is your visibility?

The research is emphatic: AI visibility is volatile. Only 30% of brands maintain stable visibility. Less than 1% of ChatGPT responses produce identical lists across two runs. A brand that shows up 80% of the time is in a fundamentally different position than one that fluctuates between 20% and 80%.

```
Stability Index = 100 − (standard deviation of weekly visibility rates / mean visibility rate) × 100
Clamped to 0-100 scale.
```

High stability (>80) = your position is entrenched. Low stability (<40) = you're volatile, could disappear any week.

Industry comparison: maps to Stability Index (buyer evaluation playbook, metrics deep research), Visibility Volatility.

---

**Cross-Engine Coverage** — which engines know about you?

```
Cross-Engine Coverage = (engines mentioning brand for a prompt / total engines tracked) × 100
Averaged across all tracked prompts.
```

A brand visible on ChatGPT but invisible on Perplexity has a coverage problem — and given ChatGPT = 87% of AI referral traffic, which engines matter more is a strategic question.

Industry comparison: maps to Cross-Engine Recall.

---

## Core Metric 2: Reputation

**Question:** How does AI describe us?

**Brand research analog:** Brand favorability, brand perception, brand positioning perception

**Why it matters:** Being visible isn't enough. If AI mentions you but frames you as "outdated," "complex," or "only suitable for enterprise," your reputation is working against you. Reputation captures the full picture of how AI characterizes your brand — not just positive/negative, but what concepts it associates with you, what story it tells, and how enthusiastically it recommends you.

### Sub-metrics

**Sentiment Score** — the overall valence

```
Scale: −100 to +100
Computed by: NLP-based classification of probe responses into positive/neutral/negative
Aggregate: weighted average across all probe responses mentioning the brand
```

This is the existing metric, enhanced. It's the baseline — most competitors offer this. Our differentiation is in the sub-metrics below.

Industry comparison: maps to Sentiment Score (SE Visible), Sentiment Distribution.

---

**Attribute Map** — what concepts does AI associate with you?

The most actionable Reputation sub-metric. Not just "positive or negative" but specifically *what* AI thinks about you.

```
Computed by: LLM-as-judge extracts top attributes from probe responses
Output: ranked list of attributes with frequency and per-attribute sentiment

Example output:
  "affordable"      — mentioned in 67% of responses, positive framing
  "enterprise-grade" — mentioned in 45% of responses, positive framing
  "complex setup"    — mentioned in 34% of responses, negative framing
  "innovative"       — mentioned in 28% of responses, positive framing
```

This tells a brand: "AI thinks you're affordable and enterprise-grade (good) but also that setup is complex (problem)." That's actionable.

Industry comparison: maps to Attribute Association. No direct competitor equivalent at this depth — most stop at polarity. This is CheckThat differentiation.

---

**Narrative Frame** — what story does AI tell about you?

Beyond individual attributes to the overall narrative. Every brand gets cast in a role by AI.

```
Computed by: LLM-as-judge classifies the dominant narrative across responses

Categories:
  Market Leader       — "the leading platform for..."
  Established Player  — "a well-known option..."
  Rising Challenger   — "a fast-growing alternative..."
  Niche Specialist    — "best suited for [specific use case]..."
  Budget Option       — "an affordable alternative to..."
  Legacy/Declining    — "traditionally used for... but newer options..."

Output: primary frame + confidence + supporting quotes from responses
```

Strategic value: if your positioning says "market leader" but AI frames you as "budget option," that's a narrative misalignment you can act on — and it connects directly to the Alignment metric.

Industry comparison: no direct competitor equivalent. CheckThat unique.

---

**Recommendation Strength** — how enthusiastically does AI recommend you?

The closest thing to NPS in the AI world. When a buyer asks "what should I use?" — does AI champion you or hedge?

```
Computed by: LLM-as-judge classifies recommendation language in probe responses

Categories and scores:
  Strong Endorsement (5)    — "You should use [brand]" / "[brand] is the best choice for..."
  Conditional (4)           — "If you need [X], [brand] is a good option"
  Mentioned Positively (3)  — "[brand] is one of several options worth considering"
  Listed Without Opinion (2) — "[brand]" (just named in a list, no recommendation)
  Mentioned With Caveats (1) — "[brand] works but has limitations..." / "consider [brand] if budget is a constraint"

Aggregate: average score across all probe responses mentioning the brand
```

Industry comparison: maps to Recommendation Rate. Our version is richer — we distinguish 5 levels of enthusiasm, not just "recommended or not."

---

**Comparative Reputation** — how does AI describe you vs competitors?

In responses that mention both your brand and a competitor, how does AI frame the relationship?

```
Computed by: LLM-as-judge classifies relative framing in multi-brand responses

Categories:
  Preferred Over   — AI recommends you over the competitor
  Equal To         — AI treats you as equivalent options
  Alternative To   — AI positions you as an alternative (competitor is primary)
  Inferior To      — AI suggests the competitor is better

Output: per-competitor comparison matrix
```

Industry comparison: maps to Comparative Mention Index. Our version classifies the *direction* of comparison, not just co-occurrence.

---

## Core Metric 3: Alignment

**Question:** Does AI match our truth?

**Brand research analog:** Message recall accuracy, positioning perception vs intent, information accuracy

**Why it matters:** This is the killer feature. No other AEO tool has it. Every competitor shows you what AI says. Only CheckThat tells you if AI is *right*.

Alignment compares AI's description of your brand against your own stated truth — the brand context answer key from Layer 1. If you say your pricing is "Free, Pro at $249/mo, Business at $1,500/mo" and AI says "pricing starts at $99/mo" — that's a measurable alignment failure that costs you deals.

**Hard dependency:** Brand context must be populated (Layer 1). Without the answer key, there's nothing to align against. Minimum requirement: company overview + product features (2 of 7 fields). Full alignment requires 3+ fields.

### Sub-metrics

**Overall Alignment Score** — the headline number

```
Scale: 0-100
Computed by: average of the six dimension scores below, each scored 0-100

Technical approach: LLM-as-judge with brand context as "expected answer"
and probe response as "actual answer." Structured evaluation rubric
provides the 6 dimensions with scoring criteria.
```

---

**Feature Accuracy** — does AI correctly describe what you do?

```
Compared against: brand_context.product_features

Output per feature:
  Correct        — AI describes this feature accurately
  Incorrect      — AI describes this feature but gets details wrong
  Missing        — AI doesn't mention this feature at all
  Not Mentioned  — Feature topic didn't come up in this prompt

Aggregate: (correct features / total features mentioned) × 100
```

---

**Pricing Accuracy** — does AI have correct pricing?

```
Compared against: brand_context.pricing_model

Output:
  Correct    — AI cites the right pricing
  Outdated   — AI cites old pricing (common — training data lag)
  Incorrect  — AI cites wrong pricing
  Missing    — AI doesn't mention pricing

Specific discrepancies flagged: "AI says $99/mo, actual is $249/mo"
```

Critical because: wrong pricing in an AI response = lost or confused prospects.

---

**Positioning Match** — does AI position you the way you want?

```
Compared against: brand_context.positioning

Scored 1-5 by LLM-as-judge:
  5 = AI's description matches your intended positioning exactly
  4 = Close match with minor differences
  3 = Partially aligned — some elements match, some don't
  2 = Significant mismatch — AI positions you differently than you intend
  1 = Opposite positioning — AI's frame contradicts your intent

Output: match score + key divergences with quotes
```

Example: Brand says "enterprise finance platform." AI says "startup expense tracker." Score: 2.

---

**Differentiator Recognition** — does AI know what makes you different?

```
Compared against: brand_context.differentiators

Per differentiator:
  Recognized    — AI mentions this differentiator
  Not Recognized — AI doesn't mention it
  Attributed to Competitor — AI assigns your differentiator to someone else (worst case)

Aggregate: (recognized differentiators / total claimed differentiators) × 100
```

---

**Narrative Alignment** — is the story AI tells the story you want told?

```
Compared against: brand_context.positioning + brand_context.differentiators

Scored 1-5 by LLM-as-judge:
  5 = AI's narrative matches your desired narrative
  1 = AI tells a completely different story

This is the qualitative complement to the quantitative metrics above.
It captures the "vibe" — is AI's overall characterization what you'd want?
```

---

**Factual Accuracy** — are basic facts correct?

```
Compared against: all brand_context fields

Checks: founding year, headquarters, company size, key integrations,
        supported platforms, customer base claims

Output: per-fact correct/incorrect with specific errors flagged
```

---

## Core Metric 4: Influence

**Question:** What shapes AI's perception of us — and how much of it do we control?

**Brand research analog:** No direct equivalent. This is new. The closest concept is "earned media influence" or "share of voice by source."

**Why it matters:** Visibility, Reputation, and Alignment measure *outputs* — what AI says. Influence measures the *inputs* — what's driving what AI says. This is the diagnostic metric. It tells you not just that your alignment is low, but *why* it's low and *where to fix it*.

A brand with high visibility but zero internal influence is in a fragile position. Their AI perception is shaped entirely by third parties — G2 reviews, Reddit threads, competitor blog posts. If those sources change, the brand's perception changes, and they have no lever to pull.

A brand with high internal influence has their own content shaping AI's perception. When they update their pricing page, AI eventually updates its pricing answer. They have leverage. Content actions move the needle.

### Two dimensions

Influence splits into **Internal** (your domain's influence) and **External** (third-party domains' influence). Together they explain where AI gets its information about you and how much control you have over the narrative.

### Internal Influence — Your Domain

How much weight your own content carries in shaping AI's perception.

**Own-Domain Citation Rate** — when AI talks about you, does it reference YOUR content?

```
Own-Domain Citation Rate = (citations to your domain / total probes mentioning your brand) × 100

Data source: ProbeCitation where cited URL domain matches brand domains
             divided by ProbeMention count for the brand
```

This is the most direct measure of internal influence. High own-domain citation rate = AI trusts your content.

---

**Own-Domain Citation Share** — your citations as a percentage of ALL citations in responses about you

```
Own-Domain Citation Share = (citations to your domain / total citations in responses about you) × 100
```

AI might cite 5 sources when answering about you. If 3 are yours, you have 60% citation share — strong internal influence. If 0 are yours, AI's description of you is built entirely from third-party sources.

Industry comparison: related to Top Source Share (Profound), but inverted — we measure from the brand's perspective, not the platform's.

---

**Source Authority Rank** — where your domain ranks among all cited sources in your category

```
Computed by: aggregate all citations across all prompts in your category,
             rank domains by citation frequency

Output: your rank position + total domains + your citation count
```

Top 5 = strong source authority. Top 20 = moderate. Not ranked = AI doesn't consider your domain a source in your category.

---

**Content Responsiveness** (v2) — when you change your content, does AI's description change?

```
Computed by: user marks content update dates, system correlates with
             changes in alignment scores for related prompts

Output: responsiveness score (0-100) measuring how quickly AI reflects your content changes
```

This is the ultimate internal influence metric. It requires time-series tracking and event correlation, which makes it a v2 feature. But it answers the most important question: "If I fix my pricing page, will AI actually update what it says about my pricing?"

---

### External Influence — Other Domains

Which third-party sources shape AI's narrative about you, and whether they're helping or hurting.

**Third-Party Source Map** — which external domains drive AI's perception of you?

```
Computed by: aggregate all non-brand-domain citations in responses about your brand,
             group and rank by domain

Output: ranked list with percentages
  "G2:           34% of external citations about you"
  "Reddit:       22%"
  "TechCrunch:   15%"
  "Competitor X: 12%"
  "Wikipedia:     8%"
  "Other:         9%"
```

Directly actionable: if G2 drives 34% of AI's perception of you, your G2 profile matters enormously. If a competitor's blog drives 12%, that's a threat you can counter.

Industry comparison: related to Source Diversity Index and Citation Concentration Index from the metrics research. Our version is brand-specific.

---

**External Source Accuracy** — are third-party sources saying correct things about you?

```
Computed by: cross-reference content of top external sources against brand context (the answer key)

Output per source:
  G2:         73% accurate (pricing outdated, features correct)
  Reddit:     45% accurate (mixed opinions, some misinformation)
  TechCrunch: 91% accurate (recent article, facts correct)
```

This connects Influence to Alignment. If your alignment score is low, this metric tells you whether the problem is YOUR content (internal) or THIRD-PARTY content (external). Different diagnosis, different remedy.

---

**External Source Sentiment** — are third-party sources positive or negative about you?

```
Computed by: analyze sentiment of third-party citations about your brand

Output per source:
  G2:         Positive (4.2/5 rating reflected in citations)
  Reddit:     Mixed (positive on features, negative on pricing)
  Competitor: Negative (positions you as inferior alternative)
```

This connects Influence to Reputation. If your reputation score is low, is it your own content or a negative G2 review dragging you down?

---

**Signal Concentration** — how concentrated is external influence?

```
Signal Concentration = citations from top source / total external citations × 100
```

High concentration (>50% from one source) = single point of failure. If that one G2 review changes, your entire AI narrative shifts. Low concentration = more resilient but harder to influence.

---

### The Strategic Payoff: Why Influence Changes the Conversation

Without Influence, a user sees: "Your Alignment score is 45%." They don't know where to start.

With Influence, they see: "Your Alignment score is 45%. 72% of AI's information about you comes from an outdated G2 review from 2024. Your own domain accounts for only 8% of citations. Fix your G2 profile first, then improve your own content's citability."

The diagnosis matrix:

| Situation | Diagnosis | Action |
|-----------|----------|--------|
| Low Alignment + High Internal Influence | Your own content is misleading AI | Fix your content (pricing page, feature descriptions, positioning) |
| Low Alignment + High External Influence | Third parties are misleading AI | Fix external sources (update G2 profile, respond to Reddit threads, pitch press corrections) |
| Low Alignment + Low Influence overall | AI is hallucinating with no reliable source | Establish any source authority — publish authoritative content, get cited, build schema markup |
| High Visibility + Low Internal Influence | You're mentioned but AI doesn't use your content | Technical AEO problem — improve crawlability, add schema, restructure content for AI consumption |
| Low Visibility + High External Influence | Third parties talk about you but AI doesn't mention you | Leverage those third-party mentions — they validate you exist but AI isn't connecting the dots |

---

## Core Metric 5: Lift

**Question:** Is it getting better?

**Brand research analog:** Brand tracking trend, brand lift studies, share of voice trend

**Why it matters:** A snapshot is interesting. A trend is actionable. Lift turns every other metric into a trajectory. Without it, you know where you stand today but not whether you're gaining or losing ground — and whether your actions are making a difference.

### Sub-metrics

**Temporal Trend** — directional movement of each metric over time

```
Computed by: linear regression of weekly scores over the lookback period

Output per metric:
  Visibility: ↑ +8% over 4 weeks (confidence: high)
  Reputation: → flat (confidence: moderate)
  Alignment:  ↓ -12% over 4 weeks (confidence: high)
  Influence:  ↑ +15% over 4 weeks (confidence: moderate)

Categories: Improving / Stable / Declining
Magnitude: % change over period
Confidence: based on sample size and variance
```

Applied independently to all four other core metrics. Lift is the meta-metric — it measures how the other metrics are changing.

---

**Competitive Shift** — your movement relative to competitors

```
Computed by: your metric delta minus average competitor metric delta for same period

Output:
  Gaining ground  — your metrics improving faster than competitors
  Holding steady  — moving at the same rate
  Losing ground   — competitors improving faster than you
```

This is the share-of-voice trend. Not just "am I getting better?" but "am I getting better *faster than the competition*?"

---

**Cross-Engine Spread** — change in which engines know about you

```
Computed by: cross-engine coverage this period minus previous period

Output:
  Expanding  — appearing on more engines (e.g., 3→5)
  Stable     — same engines as before
  Contracting — disappearing from engines (e.g., 5→3)
```

Expanding cross-engine spread is a leading indicator of growing AI visibility. Contracting is an early warning sign.

---

**Content Lift** (v2) — metric changes correlated with content actions

```
Computed by: user marks content publication dates,
             system measures before/after on matched prompts

Output:
  "After publishing the comparison page on Feb 1:
   Visibility for Direct Comparison prompts: +23%
   Alignment for pricing prompts: +15%
   Citation rate: +8%"
```

This is the brand lift study analog. The most valuable measurement for proving ROI of content investment. Requires event tracking infrastructure (user marks "I published X on date Y").

---

**Authority Lift** (v2) — metric changes after third-party signals

```
Computed by: detect new third-party mentions (reviews, press, Reddit),
             correlate with metric changes

Output:
  "After TechCrunch article on Jan 15:
   Visibility: +18% across all engines
   Citation rate: +32% (article being cited directly)
   Influence (external): TechCrunch now 20% of external citations"
```

Hardest to attribute but most valuable signal. v2 feature.

---

## Composite 1: AI Brand Health

**What it measures:** Your overall AI brand perception health. One number. The NPS of AI visibility.

**Who uses it:** CMOs, VPs of Marketing, leadership reporting. The number you track monthly and report to the board.

```
AI Brand Health = weighted average of four core metrics:
  Visibility Score (0-100)  × weight
  Reputation Score (0-100)  × weight
  Alignment Score (0-100)   × weight
  Influence Score (0-100)   × weight

(Lift excluded — it's a meta-metric about change, not a snapshot of current health)

Default weights: equal (25/25/25/25)
Configurable per workspace

Scale: 0-100
Update frequency: daily
```

Provisional thresholds (calibrate with real data):
- 80+ **Strong** — AI accurately represents your brand, cites your content, and recommends you
- 60-80 **Moderate** — AI knows you but has gaps in accuracy or recommendation strength
- 40-60 **Needs Work** — Significant issues in one or more dimensions
- <40 **Critical** — AI doesn't know you, misrepresents you, or relies on wrong sources

**Why Influence is in the composite:** A brand with 90% Visibility, 85% Reputation, 80% Alignment, but 10% Influence has a fragile position — their scores are high but they have no control over maintaining them. Including Influence rewards brands that have durable, self-controlled AI presence.

---

## Composite 2: AI Share of Voice

**What it measures:** Your presence vs competitors across the same prompts. The competitive metric.

**Who uses it:** Competitive intelligence, product marketing, category strategy.

```
AI Share of Voice combines three signals:
  Visibility Share = (your mentions / total mentions across all tracked brands) × 100
  Citation Share   = (your citations / total citations across all brands) × 100
  Position-Weighted Share = mentions weighted by position
                           (1st=3x, 2nd=2x, 3rd=1.5x, Listed=1x, Afterthought=0.5x)

AI Share of Voice = average of the three shares

Output: your % share + competitive breakdown
  "You: 23% | Competitor A: 31% | Competitor B: 19% | Competitor C: 14% | Others: 13%"

Update frequency: daily
```

This is the metric marketing teams present to leadership. "We have 23% AI Share of Voice, up from 18% last quarter."

Industry comparison: maps to AI Share of Voice (Level Agency, Avenue Z, seoClarity). Our computation is richer — we include position weighting and citation share, not just raw mention counts.

---

## Composite 3: AI Endorsement

**What it measures:** How strongly AI advocates for your brand when buyers ask for recommendations. The NPS analog.

**Who uses it:** Demand gen, product marketing, growth teams. Answers "is AI helping us win deals?"

```
AI Endorsement combines:
  Recommendation Strength (from Reputation)  — 40% weight
  Position Score (from Visibility)           — 25% weight
  Narrative Frame Score (from Reputation)    — 20% weight
  Comparative Reputation Score (from Rep)    — 15% weight

Narrative Frame scoring:
  Market Leader = 100, Established = 80, Rising = 70,
  Niche = 50, Budget = 30, Legacy = 10

Scale: 0-100
Update frequency: daily
```

A high AI Endorsement score means: when buyers ask AI for recommendations, AI champions your brand — first position, enthusiastic recommendation, market leader narrative, preferred over competitors.

---

## Operational Metrics (Tier 3)

These are the daily-use metrics practitioners track at the prompt level. Most are sub-metrics of the cores that surface in drill-down views and prompt-level detail.

| Metric | Parent Core | What it measures |
|--------|------------|-----------------|
| Unaided Visibility Rate | Visibility | % of unbranded prompts where brand appears |
| Aided Visibility Rate | Visibility | % of branded prompts where brand is recognized |
| First Mention Rate | Visibility | % of appearances where brand is mentioned first |
| Per-Engine Visibility | Visibility | Visibility rate broken down by engine |
| Per-Attribute Sentiment | Reputation | Sentiment score per extracted attribute |
| Recommendation Category | Reputation | Distribution across the 5 recommendation levels |
| Per-Feature Accuracy | Alignment | Correct/incorrect/missing per product feature |
| Per-Dimension Alignment | Alignment | Individual scores for pricing, positioning, etc. |
| Own-Domain Citation Rate | Influence | % of probes that cite your domain |
| Top Cited Pages | Influence | Your most-cited URLs ranked by frequency |
| Top External Sources | Influence | Third-party domains ranked by citation frequency |
| Week-over-Week Delta | Lift | Change in any metric vs prior week |
| Competitive Delta | Lift | Your change vs competitors' change |

---

## What We Don't Track (and Why)

| Industry metric | Why we exclude it |
|----------------|------------------|
| AI Referral Traffic / Conversion | Outside our scope — that's GA4 territory. We measure what AI says, not what users do after. |
| Technical AEO signals (schema markup, content freshness) | These are input optimizations. We measure output. We may recommend technical fixes in Intelligence (Layer 6) but don't track them as metrics. |
| Prompt volume estimates | That's keyword research, not brand research. Different product surface. |
| Source Diversity Index (overall) | An ecosystem metric, not a brand metric. Interesting for the open index, not for individual workspaces. |
| AI Referral CAC | Revenue attribution is outside our measurement scope. |

---

## Industry Coverage Check

Every significant metric tracked by competitors is covered:

| Competitor metric | Our equivalent | Coverage |
|---|---|---|
| Brand Mention Rate (Search Engine Land) | Visibility Rate | Covered |
| Brand Visibility Score (industry) | Visibility Rate | Covered |
| Citation Frequency (Profound) | Own-Domain Citation Rate | Covered — now inside Influence |
| Overall Citation Volume (Profound) | Citation Share | Covered — inside Influence |
| Top Source Share (Profound) | Source Authority Rank | Covered — inside Influence |
| Position/Rank of Mention | Position (Visibility sub-metric) | Covered |
| AI Share of Voice (Level Agency, Avenue Z) | AI Share of Voice composite | Covered — richer computation |
| Sentiment Score (SE Visible, -100 to +100) | Sentiment Score (Reputation sub-metric) | Covered |
| Sentiment Distribution | Sentiment Score breakdown | Covered |
| Accuracy Rate (industry) | Alignment sub-metrics | Covered — much richer (6 dimensions) |
| Stability Index (buyer playbook) | Stability Index (Visibility sub-metric) | Covered |
| Recommendation Rate (industry) | Recommendation Strength (Reputation) | Covered — 5-level scale vs binary |
| Cross-Engine Coverage (industry) | Cross-Engine Coverage (Visibility) | Covered |
| Citation Churn (research) | Citation Stability (Influence) | Covered |
| Comparative Mention Index (research) | Comparative Reputation (Reputation) | Covered — classifies direction |
| Contextual Citation Depth (research) | Citation Depth (Influence) | Covered |

**Metrics unique to CheckThat (no competitor equivalent):**
- Alignment (entire core metric — comparing AI output against brand truth)
- Influence (entire core metric — internal vs external source analysis)
- Narrative Frame (what story does AI tell?)
- Attribute Map (what specific concepts does AI associate with you?)
- External Source Accuracy (are third-party sources right about you?)
- AI Endorsement composite (how strongly does AI advocate for you?)

---

## Computation Dependencies

```
What each metric needs to be computed:

Visibility    Needs: ProbeMention data, Prompt.branded flag
              No dependency on Layer 1 (Context)
              Available from day one.

Reputation    Needs: ProbeMention data + LLM-as-judge analysis workflow
              Sentiment Score: no dependency on Layer 1
              Attribute Map, Narrative Frame, Recommendation Strength:
                need new post-probe analysis workflow

Alignment     Needs: Brand Context (Layer 1) minimum 2 of 7 fields
              Hard dependency. No answer key = no alignment.
              This is gated. Show "complete your context to unlock."

Influence     Internal: needs ProbeCitation data + brand domain matching
              External: needs ProbeCitation data + third-party source analysis
              Mostly works with existing data infrastructure.
              External Source Accuracy needs Layer 1 (brand context for comparison).

Lift          Needs: any other metric tracked over 2+ weeks
              Pure time-series computation on existing data.
              Available once other metrics have history.

Composites    Needs: all four core metric scores computed
              AI Brand Health = Vis + Rep + Align + Inf
              AI Share of Voice = competitive Vis + Citation + Position
              AI Endorsement = Rec Strength + Position + Narrative + Comparative
```

---

*This framework gives CheckThat five dimensions of measurement that cover everything the industry tracks, plus two unique angles (Alignment and Influence) that no competitor offers. The internal/external Influence split transforms "your score is low" into "your score is low because of [specific source] — here's where to fix it." That's the leap from monitoring tool to intelligence platform.*
