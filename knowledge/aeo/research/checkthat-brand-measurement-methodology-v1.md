# CheckThat Brand Measurement Methodology

*How CheckThat measures brands in AI. Four scores. One framework. Built on brand research principles applied to a new surface.*

**Status:** Draft v1
**Last updated:** 2026-02-16

<metadata>
purpose: Comprehensive methodology for CheckThat's 4-score brand measurement framework — Presence, Reputation, Perception, Influence — with deep specification of the Perception Score's 6 attributes
audience: Marcel, Product, Engineering, Leadership
related: pipeline/outputs/checkthat-ontology-product-roadmap-v1.md, pipeline/outputs/checkthat-metrics-framework-v1.md, pipeline/research/perception-score-methodology.md, pipeline/scratchpad/checkthat-metric-framework-options-v1.md, pipeline/scratchpad/checkthat-macro-category-methodology-v1.md
domain: product-methodology
confidence: draft
last_updated: 2026-02-16
</metadata>

---

## Section 1: The Framework

### The Core Idea

CheckThat surveys AI engines the way brands survey consumers. Brand research has well-established disciplines — brand lift studies, brand tracking, awareness surveys, NPS. They all work the same way: define what truth looks like, build instruments to probe perception, measure the gap between truth and perception over time.

CheckThat does this for AI. The "consumers" are AI engines. The "survey questions" are prompts. The "perception" is what ChatGPT, Perplexity, Claude, Gemini, and Google say when buyers ask about your category.

94% of B2B buyers now use LLMs during their buying process. Half start in a chatbot before they touch Google. The brands that win the AI recommendation are the ones that show up, get described correctly, and have leverage over the narrative.

### Four Scores, Four Questions

Every brand needs to answer four questions about their AI presence. Each question maps to a score.

| Score | Question | What It Measures | Type |
|---|---|---|---|
| **Presence** | When buyers evaluate, does AI recommend you? | Whether AI includes you in evaluation-stage answers where buyers don't name you | Output |
| **Reputation** | What does the world think? | External market signals — reviews, press, community, analysts | Input |
| **Perception** | What story does AI tell about you? | The narrative AI constructs across 6 buyer-relevant attributes | Output |
| **Influence** | How much impact can I have? | Your leverage over the other 3 scores — source control, citation authority, actionability | Control |

The first three are **what's happening**. Influence is **what you can do about it**.

These four scores compose the **CheckThat AI Benchmark** — a 2x2 visualization published per category where Presence is the X-axis, Perception is the Y-axis, Reputation is the dot size, and trend arrows show momentum. Four quadrants: AI Leaders, Hidden Gems, At Risk, Off the Map. See Section 7 for the full framework.

### How the Scores Relate

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│   PRESENCE ─── "When buyers evaluate, does AI recommend you?"│
│   The foundation. If AI doesn't include you when buyers      │
│   evaluate solutions, nothing else matters. Always unaided,  │
│   always evaluation-stage.                                   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   REPUTATION ── "What does the world think?"                 │
│   The external truth. What review platforms, analysts,       │
│   communities, and press say about you. This is the          │
│   raw material AI learns from. It exists independent         │
│   of AI — it's the world's opinion.                          │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   PERCEPTION ── "What story does AI tell about you?"         │
│   The AI-native narrative. What AI engines actually          │
│   say when buyers ask. Shaped by Reputation, but not         │
│   identical — AI filters, recombines, and sometimes          │
│   invents. Measured across 6 attributes.                     │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   INFLUENCE ─── "How much impact can I have?"                │
│   The lever. How much control you have over your             │
│   Presence, Reputation, and Perception. Internal             │
│   (your content) vs External (third-party sources).          │
│   This turns diagnosis into action.                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### The Data Flow

```
YOUR CONTENT ──────────────┐
(website, docs, schema,     │
 pricing pages)             │
                            ├──→ AI ENGINES ──→ PRESENCE (recommended during evaluation?)
EXTERNAL SOURCES ──────────┤    (ChatGPT,       PERCEPTION (what story?)
(G2, Reddit, press,        │     Perplexity,
 Wikipedia, competitors)    │     Claude,
                            │     Gemini,
REPUTATION DATA ───────────┘     Google)
(review scores, analyst
 coverage, social proof)

INFLUENCE = how much of what feeds AI you can control
```

Reputation feeds AI. Perception is what comes out. Presence is whether you show up at all. Influence measures how much leverage you have over the entire chain.

### How This Evolved

This framework builds on several iterations:

1. **8 macro-categories** — research-grade depth (Awareness, Product Capability, Strategic Vision, Trust, Customer Experience, Market Position, Value & Differentiation, Momentum). Too many dimensions for a product.
2. **6 framework options** — explored Brand Intelligence, AEO Performance, Buyer Journey, Signal Strength, Control, and Scorecard models. Each had strengths; none was complete.
3. **5 core metrics** — Visibility, Reputation, Alignment, Influence, Lift. Closer, but Alignment and Lift didn't hold as standalone scores.
4. **Perception Score research** — 6-attribute framework grounded in 30,000+ buyer survey respondents, 4 review platform scoring systems, 5 analyst frameworks, and 2.2M real AI prompts.

**Now:** 4 scores that are instantly understandable, collectively exhaustive, and actionable.

### Key Architecture Decisions

**Where Alignment went.** Previously a standalone metric ("Does AI match our truth?"). Now absorbed into Perception. The 6 Perception attributes inherently measure narrative accuracy — Feature Accuracy lives under Capability, Pricing Accuracy under Value, Positioning Match under Innovation. Alignment isn't gone; it's woven into every attribute as the gap between what you claim and what AI says.

**Where Lift went.** Previously a standalone metric. Now a cross-cutting trend layer applied to all 4 scores. Every score has a 30-day trend, competitive shift, and cross-engine spread delta. Lift isn't a score — it's how all scores move over time.

**How Reputation differs from Perception.** Reputation = what the world says about you on external platforms (G2, Gartner, Reddit, press). Perception = what AI engines specifically say about you in response to buyer queries. Reputation is an *input* to AI's perception, but they're not identical. AI filters, recombines, and sometimes invents.

**What Presence measures (and doesn't).** Other AEO tools measure "AI visibility" — a vague metric that counts mentions across all contexts, all stages, branded and unbranded. CheckThat's Presence is narrower and sharper: evaluation-stage only, unaided only. If your brand name is in the prompt, it's not Presence — it feeds Perception. If the prompt is awareness-stage ("what is expense management?"), it's not Presence. Presence answers one question: when a buyer asks AI to recommend solutions without naming you, are you there?

**What Influence measures.** Broader than prior framings. Not just "what shapes AI's perception" but "how much impact can I have on all 3 other scores?" This encompasses source authority, citation control, content leverage, and actionability. It's the score that turns monitoring into action.

---

## Section 2: Presence Score

**The question:** When buyers evaluate solutions, does AI recommend you?

**One-sentence definition:** The rate at which AI engines include your brand in evaluation-stage answers where the buyer didn't ask about you by name.

**Brand research analog:** Unaided brand awareness

### Why Presence Is Different from "AI Visibility"

Every AEO tool on the market measures "AI visibility" — are you mentioned somewhere in AI? That metric is vague and doesn't mean anything. A brand can have 90% "AI visibility" because AI knows their name when asked directly, or because they show up in awareness-stage queries like "what is expense management?" Neither tells you whether buyers will find you at the moment that matters.

Presence measures something specific: **when a buyer is actively evaluating solutions and asks AI for recommendations without naming you, does AI include you?**

The boundary is crisp:

- **If your brand name is in the prompt, it's not Presence.** Branded queries ("What is Ramp?", "Ramp pricing", "Ramp vs Brex") feed the Perception Score — they measure what story AI tells when asked about you.
- **If the prompt is awareness-stage or post-purchase, it's not Presence.** Only evaluation-stage prompts count — the moment buyers build shortlists.
- **Presence is always unaided.** AI must volunteer your name. The buyer asks about the category, the problem, or a competitor — and AI decides to include you.

This is the "unaided brand awareness" test for AI engines. In traditional brand research, you ask consumers "name three expense management tools" without prompting them. In CheckThat, you ask AI "best expense management tools for startups" and see if it names you.

### Why Presence Is First

If AI doesn't recommend you when buyers evaluate your category, nothing else matters. You can have perfect Perception and stellar Reputation, but if you're invisible during the evaluation moment, buyers never see it. Presence is the foundation — it must be non-zero before the other scores have meaning.

The data: only 30% of brands maintain stable AI visibility. Less than 1% of responses produce identical brand lists across two runs. 67.4% of domains are cited by exactly one AI platform. And 95% of the time, the winning vendor was already on the buyer's Day One shortlist (6sense). If AI builds that shortlist and you're not on it, you've lost before the conversation started.

### Sub-Metrics

#### Presence Rate (the headline number)

The percentage of evaluation-stage, unbranded prompts where AI mentions your brand.

```
Presence Rate = (evaluation prompts where brand is mentioned / total evaluation prompts tracked) x 100
```

Only unbranded prompts count. Only evaluation-stage prompts count. This is the number that tells you: when buyers ask AI for recommendations in your category, how often does AI include you?

#### Position

Not just "are you mentioned?" but "are you recommended or listed as an afterthought?"

```
Position categories:
  Recommended    — named as a primary recommendation or solo answer
  1st Mention    — named first in a list of options
  2nd-3rd        — named early but not first
  Listed         — in a list without prominence
  Afterthought   — mentioned in caveats, footnotes, or "you could also consider..."

Position Score = weighted average (Recommended=5, 1st=4, 2nd-3rd=3, Listed=2, Afterthought=1)
```

Being the recommended answer is fundamentally different from being listed 5th in a comma-separated list. A solo recommendation ("I recommend Ramp for startups") carries 5x the weight of an afterthought mention ("you could also consider Ramp").

#### Stability Index

How consistent is your presence over time?

```
Stability Index = 100 - (standard deviation of weekly presence rates / mean presence rate) x 100
Clamped to 0-100 scale.
```

High stability (>80) = your position is entrenched. Low stability (<40) = you're volatile, could disappear any week. High-authority domains maintain <10% volatility. Building authority signals (brand search volume, Wikipedia presence, review platforms, structured data) reduces volatility.

#### Cross-Engine Coverage

Which engines recommend you during evaluation?

```
Cross-Engine Coverage = (engines mentioning brand for evaluation prompts / total engines tracked) x 100
Averaged across all tracked evaluation prompts.
```

A brand recommended on ChatGPT but invisible on Perplexity during evaluation has a coverage problem. Given ChatGPT = 87% of AI referral traffic, which engines matter is a strategic question. Only 6.5% of brands achieve presence across 5+ platforms.

### What Prompts Measure Presence

All Presence prompts share two properties: (1) they are evaluation-stage — the buyer is building a shortlist or comparing solutions, and (2) they are unbranded — your brand name does not appear in the prompt.

**Pattern 1: Best-of category** — the shortlist builders. The most important evaluation prompts.

```
"Best [category] tools for [constraint]"
"Top [category] platforms for [industry]"
"What [category] software do you recommend for [company size]?"
"Best [category] with [integration/feature]"
```

**Pattern 2: Landscape and market map** — buyers understanding the field before shortlisting.

```
"Who are the main players in [category]?"
"What are the leading [category] solutions?"
"Map the [category] software market"
```

**Pattern 3: Alternatives-to-competitor** — high-intent switching queries. Your name is NOT in the prompt; the competitor's name is.

```
"Alternatives to [Competitor]"
"Best [Competitor] alternatives for [use case]"
"What can I use instead of [Competitor]?"
```

**Pattern 4: Unbranded comparison** — AI generates a comparison without being told which brands to include.

```
"Compare top [category] tools for [use case]"
"Which [category] tools should I evaluate for [constraint]?"
"Rank the best [category] options for [industry]"
```

**What does NOT count as Presence:** Any prompt containing your brand name. "[Your Brand] vs [Competitor]", "[Your Brand] pricing", "[Your Brand] reviews", "What is [Your Brand]?" — all of these feed the Perception Score, not Presence. If the buyer already named you, Presence already did its job.

### How to Calculate the Composite Presence Score

```
PRESENCE SCORE =
  (Presence Rate x 0.40) +
  (Position Score [normalized 0-100] x 0.25) +
  (Stability Index x 0.15) +
  (Cross-Engine Coverage x 0.20)

Scale: 0-100
```

Presence Rate is weighted highest because the most fundamental question is binary: when buyers evaluate, are you there or not? Position captures whether AI recommends you or just lists you. Coverage ensures you're not dependent on a single engine. Stability ensures your presence is durable, not a one-week fluke.

### Score Interpretation

| Range | Meaning |
|---|---|
| 80-100 | AI consistently recommends you when buyers evaluate your category. Strong, stable, multi-engine presence. |
| 60-79 | AI includes you regularly during evaluation but with gaps — missing engines, inconsistent position, or volatile week to week. |
| 40-59 | AI includes you sometimes during evaluation. Significant gaps. Buyers have a coin-flip chance of seeing you. |
| 20-39 | AI rarely recommends you during evaluation. Most buyers using AI to build a shortlist will miss you. |
| 0-19 | Invisible during evaluation. Buyers using AI to shortlist solutions will not find you. |

---

## Section 3: Reputation Score

**The question:** What does the world think?

**One-sentence definition:** The aggregate signal from external platforms — review sites, analyst firms, press coverage, community mentions, and social proof — that represents the market's opinion of your brand independent of what AI says.

**Brand research analog:** Brand favorability, NPS, review scores, analyst ratings

### Why Reputation Is Separate from Perception

This is a critical distinction. Perception (Section 4) measures what AI engines *say* about you. Reputation measures what the *world* says about you on external platforms. They're related — Reputation is a major input to AI's Perception — but they're not the same thing.

AI doesn't just parrot review scores. It filters, recombines, and sometimes invents. A brand with 4.8 stars on G2 might get described by AI as "good but complex to set up" because AI weighted one specific dimension of reviews. A brand with modest review scores might get glowing AI descriptions because a TechCrunch article hit at the right time.

Reputation is the external truth. Perception is AI's interpretation of it. Both matter.

### Why Reputation Matters for a Brand

The world's opinion shapes everything:

- **95% of the time, the winning vendor was already on the buyer's Day One shortlist** (6sense). Reputation builds that shortlist before AI even enters the picture.
- **78% of buyers shortlist products they've already heard of** — 86% among enterprise buyers (TrustRadius).
- **Reddit is cited in 40%+ of Perplexity responses** and is a top-10 most-cited domain across all AI engines.
- **G2 accounts for 8.25% of ChatGPT citations** for evaluation queries.

Reputation feeds AI. Low Reputation almost guarantees low Perception.

### Data Sources

Reputation aggregates signals from external platforms that buyers and AI engines both rely on:

| Source | What It Captures | Signal Type |
|---|---|---|
| **G2** | User reviews, satisfaction scores, feature ratings, Grid placement | Review quality, buyer satisfaction |
| **Capterra** | User reviews, Overall/Ease of Use/Support/Value scores | Review breadth, category coverage |
| **TrustRadius** | trScore, Buyer's Choice criteria (capabilities, value, relationship) | Enterprise buyer sentiment |
| **Gartner Peer Insights** | Overall rating, Service & Support, Integration & Deployment, Product Capabilities | Enterprise analyst-adjacent signal |
| **Reddit** | Subreddit mentions, sentiment, upvote ratios, comment depth | Community authenticity, raw buyer language |
| **Press coverage** | TechCrunch, Forbes, industry publications — recency, sentiment, prominence | Authority signal, news freshness |
| **Social proof** | LinkedIn discussions, X/Twitter mentions, community forum presence | Professional network signal |
| **Wikipedia** | Page existence, accuracy, freshness, edit history | Foundational knowledge signal (12.1% of ChatGPT citations) |

### How to Calculate Reputation Score

Reputation doesn't require running prompts against AI engines. It's computed from external data.

```
REVIEW PLATFORM SIGNAL (50% weight):
  Aggregate normalized scores from G2, Capterra, TrustRadius, Gartner PI
  Each platform score normalized to 0-100 scale
  Weighted by platform reach and credibility:
    G2: 35% (largest review volume, most cited by AI)
    Capterra/Software Advice: 25% (broad SMB coverage)
    TrustRadius: 20% (enterprise depth, trScore rigor)
    Gartner Peer Insights: 20% (enterprise authority)
  Average of available platforms (not all brands are on all platforms)

COMMUNITY SIGNAL (25% weight):
  Reddit presence score (0-100):
    Active in relevant subreddits? (+25)
    Mentioned positively in recommendations? (+25)
    Recent mentions (last 90 days)? (+25)
    Response/engagement from brand? (+25)
  Social proof score (0-100):
    LinkedIn discussion mentions (+40)
    Professional community presence (+30)
    Social media sentiment (+30)

AUTHORITY SIGNAL (25% weight):
  Press recency and quality (0-100):
    Major press coverage in last 6 months? (+40)
    Industry analyst mentions? (+30)
    Wikipedia page exists and is current? (+30)

REPUTATION SCORE =
  (Review Platform Signal x 0.50) +
  (Community Signal x 0.25) +
  (Authority Signal x 0.25)

Scale: 0-100
```

### Score Interpretation

| Range | Meaning |
|---|---|
| 80-100 | Strong market reputation. Well-reviewed, well-covered, strong community presence. AI has good material to work with. |
| 60-79 | Solid reputation with gaps — maybe strong reviews but weak press, or good press but thin community presence. |
| 40-59 | Moderate reputation. Some signals strong, others weak or absent. AI has mixed material to draw from. |
| 20-39 | Weak reputation. Few reviews, minimal press, thin community presence. AI has little external signal. |
| 0-19 | Near-zero market signal. AI has almost nothing to work with from external sources. |

### The Relationship to Perception

Reputation is the *input*. Perception is the *output*. The gap between them is diagnostic:

| Pattern | Diagnosis |
|---|---|
| High Reputation + High Perception | The system works. External signals translate correctly into AI narrative. |
| High Reputation + Low Perception | AI isn't reading the room. Your external reputation is strong but AI doesn't reflect it. Likely a source citation or crawlability problem. |
| Low Reputation + High Perception | Rare and fragile. AI has a positive view that isn't backed by market evidence. Likely temporary — will correct as AI models update. |
| Low Reputation + Low Perception | Expected. Low external signal = low AI narrative quality. Fix Reputation first. |

---

## Section 4: Perception Score

**The question:** What story does AI tell about you?

**One-sentence definition:** The narrative AI constructs about your brand, measured across six buyer-relevant attributes that together capture what matters to every B2B purchase decision.

**Brand research analog:** Brand perception survey, brand attribute study, positioning perception audit

### Why Perception Is the Heart of CheckThat

Presence tells you if AI recommends you during evaluation. Reputation tells you what the world thinks. Perception tells you what AI *actually says* about you — the narrative it builds across the dimensions buyers care about.

This is the score no one else can produce. Traditional brand tracking surveys humans. Review platforms aggregate ratings. CheckThat reads the actual AI-generated narrative and scores it across six attributes.

The old "Alignment" metric measured whether AI matched brand truth. Perception goes further — it measures the *quality* of the narrative AI builds, not just its accuracy. A brand can be accurately described by AI and still get a mediocre Perception score if AI positions them as "basic" or "narrow" when they're actually comprehensive and innovative.

**Where branded queries live.** Presence is always unaided — your brand name never appears in the prompt. Branded evaluation queries ("Ramp vs Brex," "Ramp pricing," "Does Ramp have X?", "Ramp reviews") feed Perception, not Presence. When a buyer asks about you by name, Presence already did its job — now the question is what story AI tells. That's Perception. This means Perception draws from both branded and unbranded AI responses. Any response that mentions your brand and contains narrative content about your capabilities, usability, value, trust, support, or innovation is scored by the Perception classifier.

### Architecture: 6 Attributes

Six attributes. One word each. Scored 0-10. Together they compose the Perception Score.

```
┌───────────────────────────────────────────────────┐
│  PERCEPTION SCORE (0-100)                          │
│                                                    │
│  ┌──────────────┐  ┌──────────────┐               │
│  │  CAPABILITY  │  │  USABILITY   │               │
│  │    (0-10)    │  │    (0-10)    │               │
│  └──────────────┘  └──────────────┘               │
│  ┌──────────────┐  ┌──────────────┐               │
│  │    VALUE     │  │    TRUST     │               │
│  │    (0-10)    │  │    (0-10)    │               │
│  └──────────────┘  └──────────────┘               │
│  ┌──────────────┐  ┌──────────────┐               │
│  │   SUPPORT    │  │  INNOVATION  │               │
│  │    (0-10)    │  │    (0-10)    │               │
│  └──────────────┘  └──────────────┘               │
│                                                    │
│  Composite = unweighted average x 10               │
│  (e.g., avg of 7.2 = Perception Score of 72)       │
└───────────────────────────────────────────────────┘
```

### Why These Six

Every B2B vendor evaluation framework in existence collapses to a small number of dimensions. Gartner uses 15 criteria but two axes. Forrester uses three dimensions. G2 uses two. TrustRadius uses one composite score. The platforms that last are the ones that pick the right abstractions.

We tested each attribute against three filters:

1. **Does a CMO instantly understand it?** No jargon. No explanation needed. If you have to define the word, it's wrong.
2. **Can an LLM reliably score it from AI-generated text?** We're not surveying humans. We're classifying language. The attribute must map to detectable patterns in how AI engines talk about brands.
3. **Does it map to a distinct buyer concern with zero overlap?** Six attributes means zero waste. Each one must stand on its own.

We started with 10 attributes. We collapsed to 6. Scalability folded into Capability. Integration/Ecosystem folded into Capability. AI/Automation folded into Capability. Reliability folded into Trust. Market Position was cut (it's an outcome of the other scores). Differentiation folded into Innovation.

### Attribute 1: Capability

**The question it answers:** Does AI describe your product as powerful and complete, or limited and narrow?

**What it absorbs:** Core features, functionality, scalability, AI/automation capabilities, integration and ecosystem fit, product depth and breadth.

**How we score it:**

We classify every AI-generated mention of a brand for language related to product capabilities, feature completeness, scalability, integrations, and technical depth.

**Positive signals:** "comprehensive," "feature-rich," "handles enterprise scale," "robust API," "integrates with," "full-featured," "covers the full workflow"

**Negative signals:** "limited," "basic," "lacks," "doesn't support," "standalone tool," "narrow scope," "feature gaps"

**Scale:**
- 0-3: AI describes the product as limited, basic, or narrow in scope
- 4-6: AI describes adequate functionality with noted gaps
- 7-8: AI describes strong, comprehensive capabilities
- 9-10: AI positions the product as best-in-class across multiple dimensions

**Why Capability is first:** Every evaluation framework starts here. Gartner's Product/Service criterion is typically the heaviest-weighted factor in Magic Quadrant evaluations. Forrester's Current Offering axis spans 8-25+ sub-criteria, all rooted in what the product actually does. G2's "Meets Requirements" is one of only three HIGH-weight satisfaction dimensions.

89% of B2B buyers in 2025 purchased solutions with AI features baked in (6sense, n=4,000). 81% rated AI functionality as important or very important (G2 2024). Feature/attribute scores on review platforms are valued highest by enterprise buyers at 22% when evaluating software reviews.

**Alignment embedded:** Feature Accuracy from the old Alignment metric now lives here. When we score Capability, we're inherently measuring whether AI accurately represents what the product can do. A hallucinated feature is a Capability signal (inaccurate). A missing feature is a Capability signal (incomplete).

**Prompt patterns:**

```
Capability queries:
  "Does [Brand] have [feature]?"
  "Can [Brand] handle [use case]?"
  "Does [Brand] integrate with [platform]?"
  "Which [category] tools have the best [capability]?"

Feature comparison queries:
  "Compare [Brand A] and [Brand B] features"
  "Which [category] has the most comprehensive [capability]?"
  "[Brand A] vs [Brand B]: which has better integrations?"

Use-case fit queries:
  "What tool should I use to [specific workflow]?"
  "Best tool for automating [process]"
  "Software to [solve specific problem]"
```

**Review platform mapping:**

| Platform | Dimension | Weight |
|---|---|---|
| G2 | Meets Requirements | HIGH |
| Capterra | Functionality | 50% of usability axis |
| Gartner PI | Product Capabilities | Required rating (1 of 3) |
| TrustRadius | Product capabilities | Core component of trScore |
| Forrester Wave | Current Offering | Primary axis (8-25+ sub-criteria) |
| Gartner MQ | Product/Service | Typically highest-weighted Execute criterion |

---

### Attribute 2: Usability

**The question it answers:** Does AI describe your product as easy to use and fast to implement, or complex and painful to adopt?

**What it absorbs:** Ease of use, implementation speed, onboarding complexity, time to value, learning curve, UX quality, ease of administration.

**How we score it:**

We classify AI-generated text for language about user experience, setup complexity, learning curve, and time to value.

**Positive signals:** "intuitive," "easy to set up," "minimal training," "quick onboarding," "user-friendly interface," "modern UX," "self-service"

**Negative signals:** "steep learning curve," "complex setup," "requires training," "difficult to configure," "clunky," "heavy implementation," "requires dedicated admin"

**Scale:**
- 0-3: AI describes a product that's hard to use, slow to implement, and frustrating
- 4-6: AI describes a product that's functional but requires effort to adopt
- 7-8: AI describes a product that's intuitive with reasonable onboarding
- 9-10: AI describes an exceptional user experience with near-instant time to value

**Why Usability stands alone:** The most consistently high-weighted dimension across every review platform. G2 weights "Ease of Use" as HIGH in its satisfaction scoring — one of only three dimensions at that level. Capterra gives "Ease of Use" 50% weight on its entire usability axis.

57% of B2B buyers expect ROI within three months of purchase. 11% expect it immediately (G2 2024). 58% report regretting purchases partly due to onboarding challenges. Usability isn't just about daily experience — it's about how fast a buyer gets value.

Bain's B2B Elements of Value research: for IT infrastructure buyers, 7 of the top 10 most important value elements sit within the "ease of doing business" level, not the functional level.

**Alignment embedded:** Implementation accuracy from the old Alignment metric now lives here. When AI says "easy to set up in minutes" but the real implementation takes weeks, that's a Usability misalignment we can flag by comparing against brand context.

**Prompt patterns:**

```
User experience queries:
  "Is [Brand] easy to use?"
  "What's the user experience like with [Brand]?"
  "Do employees like using [Brand]?"
  "How does [Brand] compare to [Competitor] in ease of use?"

Onboarding queries:
  "How long does it take to set up [Brand]?"
  "Is [Brand] easy to implement?"
  "What's [Brand]'s onboarding process like?"
  "Can I switch from [Competitor] to [Brand] easily?"

Time-to-value queries:
  "How quickly can I get results with [Brand]?"
  "What does the learning curve look like for [Brand]?"
```

**Review platform mapping:**

| Platform | Dimension | Weight |
|---|---|---|
| G2 | Ease of Use | HIGH |
| G2 | Ease of Setup | MEDIUM |
| G2 | Ease of Admin | MEDIUM |
| Capterra | Ease of Use | 50% of usability axis |
| Gartner PI | Integration & Deployment | Additional sub-rating |
| TrustRadius | Implementation & onboarding sentiment | Component of trScore |
| Forrester Wave | Ease of implementation | Sub-criterion within Current Offering |

---

### Attribute 3: Value

**The question it answers:** Does AI position you as worth the money, or as expensive relative to what you deliver?

**What it absorbs:** Pricing, affordability, ROI, total cost of ownership, pricing transparency, contract flexibility, cost efficiency.

**How we score it:**

We classify AI-generated text for language about pricing, cost, ROI, and financial value.

**Positive signals:** "affordable," "competitive pricing," "strong ROI," "transparent pricing," "good value," "free tier," "saves money," "cost-effective"

**Negative signals:** "expensive," "overpriced," "hidden costs," "not worth it," "pricing complexity," "costly," "budget-prohibitive"

**Scale:**
- 0-3: AI describes the product as expensive with unclear value
- 4-6: AI describes adequate value with pricing caveats
- 7-8: AI describes strong value relative to capabilities
- 9-10: AI positions the product as best-in-class value in the category

**Why Value is the #1 purchase driver:** TrustRadius: 66% of buyers selected their product because it "met our needs for the best price" — the single most cited purchase driver across 2,164 respondents. Gartner Digital Markets: 49% name price a top consideration during search (n=2,499).

CFOs now hold final decision-making power in 79% of purchases. Products with transparent pricing achieved 3.2x more AI visibility than those without (Goodie AI, 2.2M prompts analyzed).

Value absorbs total cost of ownership. Buyers don't evaluate sticker price in isolation. They evaluate implementation costs, training, maintenance, customization, and migration costs.

**Alignment embedded:** Pricing Accuracy from the old Alignment metric now lives here. When AI cites your pricing, we compare it against brand context. Wrong pricing in an AI response = lost or confused prospects. "AI says $99/mo, actual is $249/mo" is a critical Value misalignment.

**Prompt patterns:**

```
Pricing queries:
  "[Brand] pricing"
  "How much does [Brand] cost?"
  "[Brand] vs [Competitor] pricing"
  "Best [category] under $[price point] per month"
  "Free [category] tools"

ROI queries:
  "What's the ROI of [Brand/category]?"
  "Is [Brand] worth the price?"
  "Why is [Brand] worth paying for?"
  "Cost of [Brand] vs doing nothing"

Value comparison queries:
  "Best value [category] tool"
  "[Brand] free tier vs paid"
  "Most affordable [category] for [company size]"
```

**Review platform mapping:**

| Platform | Dimension | Weight |
|---|---|---|
| G2 | Ease of Doing Business With | MEDIUM |
| Capterra | Value for Money | 25% of satisfaction axis |
| TrustRadius | Best Value for Price | 1 of 3 Buyer's Choice criteria |
| Gartner MQ | Sales Execution/Pricing | Ability to Execute criterion |
| Forrester Wave | Business Model | Strategy sub-criterion |

---

### Attribute 4: Trust

**The question it answers:** Does AI describe you as a safe, reliable, secure choice, or as a risk?

**What it absorbs:** Security, compliance, reliability, uptime, data protection, brand credibility, enterprise-readiness, vendor stability, breach history.

**How we score it:**

We classify AI-generated text for language about security posture, compliance certifications, reliability, data handling, and enterprise-readiness.

**Positive signals:** "SOC 2 compliant," "enterprise-grade security," "reliable," "trusted by," "99.9% uptime," "GDPR compliant," "ISO certified," "proven at scale"

**Negative signals:** "security concerns," "data breach," "reliability issues," "downtime," "not enterprise-ready," "compliance gaps," "risk factors"

**Scale:**
- 0-3: AI raises security concerns or describes unreliable/risky product
- 4-6: AI describes adequate security without strong trust signals
- 7-8: AI references specific certifications and enterprise readiness
- 9-10: AI positions the product as the safe, trusted standard in the category

**Why Trust is the biggest collapse:** Trust collapses the most sub-dimensions into one word. Security, compliance, reliability, brand credibility, and vendor stability all answer the same buyer question: can I bet my job on this?

Security alone is the #1 consideration across six major department types (G2 2024). 81% of enterprise buyers consider vendor breach history. 97% involve a security stakeholder at some point.

Brand trust is the gatekeeper. 95% of the time, the winning vendor was on the buyer's Day One shortlist (6sense). 77% purchased from their preliminary favorite before any vendor contact. Forrester's MaxDiff analysis: competency (18.5%), consistency (17.0%), and dependability (16.8%) are the top three trust attributes.

Buyers don't separate these. "Is this safe to choose?" covers data security AND reliability AND vendor stability AND brand credibility simultaneously. In AI text, these signals cluster together.

**Alignment embedded:** Factual Accuracy from the old Alignment metric maps here when it touches security claims, compliance certifications, and reliability track record. If AI says "SOC 2 compliant" and the brand isn't, that's a Trust misalignment.

**Prompt patterns:**

```
Trust evaluation queries:
  "Is [Brand] trustworthy?"
  "Is [Brand] safe for enterprise use?"
  "Are there any concerns about using [Brand]?"
  "What are the risks of using [Brand]?"
  "[Brand] security and compliance"

Social proof queries:
  "Who uses [Brand]?"
  "What companies use [Brand]?"
  "What do customers say about [Brand]?"
  "Has [Brand] won any awards?"

Objection-surfacing queries:
  "What are the downsides of [Brand]?"
  "[Brand] complaints"
  "Problems with [Brand]"
  "Why shouldn't I use [Brand]?"
```

**Review platform mapping:**

| Platform | Dimension | Weight |
|---|---|---|
| G2 | Quality of Support + Market Presence signals | Combined effect |
| TrustRadius | Best Customer Relationship | 1 of 3 Buyer's Choice criteria |
| Capterra | Profile completeness + verified reviews | Ranking signal |
| Gartner PI | Service & Support + review diversity | Required rating + methodology |
| Gartner MQ | Overall Viability | Ability to Execute criterion |
| Forrester Wave | Customer Feedback (dot size) | Third dimension |

---

### Attribute 5: Support

**The question it answers:** Does AI describe your support as responsive and helpful, or slow and frustrating?

**What it absorbs:** Customer support quality, responsiveness, documentation, self-service resources, success management, onboarding assistance.

**How we score it:**

We classify AI-generated text for language about support quality, responsiveness, and customer success.

**Positive signals:** "excellent support," "responsive team," "great documentation," "dedicated success manager," "24/7 support," "proactive customer success," "helpful community"

**Negative signals:** "poor support," "slow response," "limited documentation," "no phone support," "long wait times," "hard to reach," "ticket-based only"

**Scale:**
- 0-3: AI describes support as a significant weakness
- 4-6: AI describes adequate support with noted limitations
- 7-8: AI describes strong, responsive support
- 9-10: AI positions support as a competitive advantage and differentiator

**Why Support can't fold into anything else:** We tried. It doesn't collapse cleanly.

Support isn't Trust (that's about whether you're safe to choose). Support isn't Usability (that's about whether you can figure it out yourself). Support is what happens when things break, when implementation stalls, when a buyer needs help.

Every review platform measures it independently. Capterra gives Customer Support a staggering 50% weight on its entire satisfaction axis. G2 rates Quality of Support as one of only three HIGH-weight satisfaction dimensions. Gartner Peer Insights requires a Service & Support sub-rating as one of only three mandatory ratings. TrustRadius's Buyer's Choice award requires best customer relationship alongside best capabilities and best value.

At the renewal stage, support quality is one of the strongest predictors of retention. Best-in-class SaaS companies achieve 85-87% annual logo retention, and proactive customer success management is the common thread.

Support also absorbs customer success — proactive guidance, strategic reviews, and outcome-driven engagement. When AI says "offers dedicated account management," that's a Support signal even though it's technically a success function.

**Prompt patterns:**

```
Support quality queries:
  "How is [Brand]'s customer support?"
  "Does [Brand] have good customer service?"
  "What do customers say about [Brand] support?"
  "Is [Brand] responsive when you have issues?"

Documentation queries:
  "[Brand] documentation quality"
  "Does [Brand] have good help resources?"
  "[Brand] knowledge base"

Success management queries:
  "Does [Brand] offer dedicated account management?"
  "[Brand] onboarding support"
  "How much help do you get setting up [Brand]?"
```

**Review platform mapping:**

| Platform | Dimension | Weight |
|---|---|---|
| G2 | Quality of Support | HIGH |
| Capterra | Customer Support | 50% of satisfaction axis |
| Gartner PI | Service & Support | Required rating (1 of 3) |
| TrustRadius | Best Customer Relationship | 1 of 3 Buyer's Choice criteria |
| Forrester Wave | Support (sub-criterion) | Weighted within Current Offering |
| Gartner MQ | Customer Experience | Ability to Execute criterion |

---

### Attribute 6: Innovation

**The question it answers:** Does AI describe you as forward-thinking and evolving, or stagnant and falling behind?

**What it absorbs:** Product vision, roadmap, differentiation, competitive uniqueness, R&D investment, emerging capabilities, market leadership trajectory.

**How we score it:**

We classify AI-generated text for language about product direction, uniqueness, and forward momentum.

**Positive signals:** "rapidly improving," "recently launched," "innovative approach," "unique in that," "leading the way," "pioneering," "disruptive," "category-defining"

**Negative signals:** "hasn't changed," "falling behind," "legacy," "stagnant," "no clear roadmap," "generic," "outdated," "me-too"

**Scale:**
- 0-3: AI describes a stagnant product with no differentiation
- 4-6: AI describes a product with some unique aspects but limited vision
- 7-8: AI describes an actively evolving product with clear differentiation
- 9-10: AI positions the product as a category-defining innovator

**Why Innovation absorbs Differentiation:** CEB research found that only 14% of companies offer benefits customers find truly unique. An attribute that scores 86% of brands the same way isn't useful.

But the signal matters. When AI says "uniquely strong at real-time spend controls," that's meaningful. It's just that the signal lives under Innovation, not a separate attribute. Innovation captures both "where are you going?" (vision, roadmap) and "what makes you different?" (uniqueness, competitive separation).

Gartner's Completeness of Vision axis evaluates market understanding, innovation investment, and offering strategy. Forrester's Strategy dimension covers roadmap, innovation commitment, and business model. Both combine trajectory with differentiation. We're doing the same.

Innovation is the hardest attribute to score from AI text. AI engines discuss product direction less frequently than features, pricing, or reviews. But when they do, it's highly differentiating.

**Alignment embedded:** Positioning Match and Differentiator Recognition from the old Alignment metric now live here. Does AI correctly convey what makes you different? Does it tell the story you want told about where you're going? Innovation is where narrative alignment matters most.

**Prompt patterns:**

```
Innovation queries:
  "Which [category] companies are most innovative?"
  "What [category] tools are using AI in interesting ways?"
  "Most forward-thinking [category] companies"
  "Which [category] tools are investing in automation?"

Differentiation queries:
  "What makes [Brand] different from other [category] tools?"
  "Why would I choose [Brand] over [Competitor]?"
  "What's unique about [Brand]?"
  "What's [Brand]'s competitive advantage?"

Vision and trajectory queries:
  "What is [Brand]'s long-term vision?"
  "Where is [Brand] headed as a company?"
  "Is [Brand] growing or declining?"
  "Is [Brand] a good company to bet on long-term?"
```

**Review platform mapping:**

| Platform | Dimension | Weight |
|---|---|---|
| G2 | Product Direction (Satisfaction) | LOW (but published) |
| G2 | Momentum Grid | Separate report on trajectory |
| Gartner MQ | Completeness of Vision (full axis) | 50% of placement |
| Gartner MQ | Innovation | Vision sub-criterion |
| Forrester Wave | Strategy (full axis) | Primary dimension |
| IDC MarketScape | Strategies (full axis) | 3-5 year strategic alignment |
| GigaOm Radar | Innovation criterion | Explicit, product-focused |

---

### How We Calculate the Perception Score

#### Input

Every AI-generated response about a brand, tracked across ChatGPT, Perplexity, Claude, Gemini, and Google AI Overviews. Thousands of responses per brand, collected across hundreds of prompts per category.

#### Classification

Each response runs through a classification layer (LLM-as-judge) that scores each relevant attribute on a 0-10 scale based on the language used.

Not every response contains signals for every attribute. A response about pricing won't score on Innovation. A response about product roadmap won't score on Support. The classifier only scores what's present.

The LLM-as-judge evaluates against clear rubrics for each attribute. The rubrics are defined by the positive/negative signal lists and the scoring scales above.

#### Aggregation

For each attribute, we aggregate all classified scores across all responses:

- **Weight by recency** — recent responses count more than older ones. AI models update. The freshest signal is the most representative.
- **Weight by engine diversity** — appearing positive across multiple engines is a stronger signal than one engine's opinion. Cross-engine agreement increases confidence.
- **Normalize against category peers** — a 7 in CRM means something different than a 7 in DevOps tooling. Normalization ensures scores are meaningful within a category context.

#### Output

Six attribute scores (0-10 each) plus a composite Perception Score.

```
PERCEPTION SCORE = (avg of 6 attribute scores) x 10

Example:
  Capability:  7.8
  Usability:   8.2
  Value:       6.5
  Trust:       7.0
  Support:     7.4
  Innovation:  6.1

  Average: 7.17
  Perception Score: 71.7 → 72 / 100
```

The composite Perception Score is the unweighted average of all six attributes. Equal weight by default. In the dashboard, paying users can apply custom weights to match what matters most in their category (e.g., Trust might matter more in security software; Usability might matter more in design tools).

#### How Alignment Is Embedded

The old Alignment metric asked: "Does AI match our truth?" That question didn't disappear. It's now answered through each Perception attribute:

| Old Alignment Dimension | Now Lives In | How |
|---|---|---|
| Feature Accuracy | Capability | Comparing AI's feature descriptions against brand context feature list |
| Pricing Accuracy | Value | Comparing AI's pricing claims against brand context pricing model |
| Positioning Match | Innovation | Comparing AI's narrative about differentiation and direction against brand positioning |
| Differentiator Recognition | Innovation | Checking whether AI mentions claimed differentiators |
| Narrative Alignment | All 6 (holistic) | The overall gap between AI's story and the brand's intended story |
| Factual Accuracy | Trust + Capability | Checking basic facts (founding, features, compliance) against brand context |

When brand context is populated, each Perception attribute gains an alignment dimension: the gap between what AI says and what the brand claims. This surfaces as "misalignment flags" in the dashboard — "AI says your pricing is $99/mo, but your actual pricing is $249/mo" under the Value attribute.

---

## Section 5: Influence Score

**The question:** How much impact can I have on my Presence, Reputation, and Perception?

**One-sentence definition:** The degree of control you have over what AI says about you, measured by how much of AI's source material is yours, how authoritative your content is, and where the leverage points are.

**Brand research analog:** No direct equivalent. Closest concepts are "earned media influence," "share of voice by source," and "brand narrative control."

### Why Influence Exists

The other three scores measure *what's happening*. Influence measures *what you can do about it*.

Without Influence, a user sees: "Your Perception Score is 45." They don't know where to start.

With Influence, they see: "Your Perception Score is 45. 72% of AI's information about you comes from an outdated G2 review from 2024. Your own domain accounts for only 8% of citations. Fix your G2 profile first, then improve your own content's citability."

Influence turns monitoring into action. It's the diagnostic metric that connects every other score to a specific fix.

### Two Dimensions

Influence splits into **Internal** (your domain's influence on AI) and **External** (third-party domains' influence on AI). Together they explain where AI gets its information about you and how much control you have over the narrative.

### Internal Influence

How much weight your own content carries in shaping AI's perception.

**Own-Domain Citation Rate** — when AI talks about you, does it reference YOUR content?

```
Own-Domain Citation Rate = (citations to your domain / total probes mentioning your brand) x 100
```

The most direct measure of internal influence. High own-domain citation rate = AI trusts your content. When you update your pricing page, AI's pricing answer will eventually follow.

**Own-Domain Citation Share** — your citations as a percentage of ALL citations in responses about you.

```
Own-Domain Citation Share = (citations to your domain / total citations in responses about you) x 100
```

AI might cite 5 sources when answering about you. If 3 are yours, you have 60% citation share — strong internal influence. If 0 are yours, AI's description of you is built entirely from third-party sources. You have no direct lever.

**Source Authority Rank** — where your domain ranks among all cited sources in your category.

```
Aggregate all citations across all prompts in your category.
Rank domains by citation frequency.
Output: your rank position among all domains.
```

Top 5 = strong source authority. Top 20 = moderate. Not ranked = AI doesn't consider your domain a source in your category.

**Content Responsiveness** (v2) — when you change your content, does AI's description change?

```
User marks content update dates.
System correlates with changes in Perception attribute scores for related prompts.
Output: responsiveness score (0-100) measuring how quickly AI reflects your content changes.
```

The ultimate internal influence metric. It answers: "If I fix my pricing page, will AI actually update what it says about my pricing?" Requires time-series data and event correlation. V2 feature.

### External Influence

Which third-party sources shape AI's narrative about you, and whether they're helping or hurting.

**Third-Party Source Map** — which external domains drive AI's perception of you?

```
Aggregate all non-brand-domain citations in responses about your brand.
Group and rank by domain.

Output (example):
  G2:            34% of external citations about you
  Reddit:        22%
  TechCrunch:    15%
  Competitor X:  12%
  Wikipedia:      8%
  Other:          9%
```

Directly actionable. If G2 drives 34% of AI's perception, your G2 profile matters enormously. If a competitor's blog drives 12%, that's a threat you can counter.

**External Source Accuracy** — are third-party sources saying correct things about you?

```
Cross-reference content of top external sources against brand context (the answer key).

Output per source:
  G2:         73% accurate (pricing outdated, features correct)
  Reddit:     45% accurate (mixed opinions, some misinformation)
  TechCrunch: 91% accurate (recent article, facts correct)
```

This connects Influence to Perception. If your Perception score is low, this metric tells you whether the problem is YOUR content (internal) or THIRD-PARTY content (external). Different diagnosis, different remedy.

**External Source Sentiment** — are third-party sources positive or negative about you?

```
Analyze sentiment of third-party citations about your brand.

Output per source:
  G2:         Positive (4.2/5 rating reflected in citations)
  Reddit:     Mixed (positive on features, negative on pricing)
  Competitor: Negative (positions you as inferior alternative)
```

**Signal Concentration** — how concentrated is external influence?

```
Signal Concentration = (citations from top source / total external citations) x 100
```

High concentration (>50% from one source) = single point of failure. If that one G2 review changes, your entire AI narrative shifts. Low concentration = more resilient but harder to influence strategically.

### How to Calculate the Influence Score

```
INTERNAL INFLUENCE (50% weight):
  Own-Domain Citation Rate (0-100): 40% of internal
  Own-Domain Citation Share (0-100): 35% of internal
  Source Authority Rank (normalized 0-100): 25% of internal

EXTERNAL INFLUENCE (50% weight):
  Source Map Diversity (inverse of Signal Concentration): 30% of external
  External Source Accuracy (avg across top sources): 40% of external
  External Source Sentiment (avg across top sources): 30% of external

INFLUENCE SCORE =
  (Internal Influence x 0.50) + (External Influence x 0.50)

Scale: 0-100
```

### The Diagnostic Matrix

Influence's real power is in diagnosis. Cross any score with Influence to understand cause and recommended action:

| Situation | Diagnosis | Action |
|---|---|---|
| Low Presence + Low Internal Influence | AI has no source material from you | Establish source authority from scratch — publish content, build schema markup, get indexed |
| Low Presence + High External Influence | Third parties talk about you but AI doesn't mention you | Leverage those mentions — AI knows about you but isn't connecting the dots. Fix crawlability and content structure. |
| Low Perception + High Internal Influence | Your own content is misleading AI | Fix your content — pricing page, feature descriptions, positioning. The problem is yours to solve. |
| Low Perception + High External Influence | Third parties are misleading AI | Fix external sources — update G2 profile, respond to Reddit threads, pitch press corrections |
| Low Perception + Low Influence overall | AI is hallucinating with no reliable source | Establish any source authority — you're in the worst position. Need owned and third-party content from scratch. |
| High Presence + Low Internal Influence | Mentioned but your content isn't cited | Technical AEO problem — improve crawlability, add schema, restructure content for AI extraction |
| High Presence + Low Perception | Visible but misrepresented | AI knows you exist but gets the story wrong. Use Influence data to identify which sources are feeding the bad narrative. |
| Good scores + High Signal Concentration | Strong but fragile — dependent on one source | Diversify. If 60% of your citations come from G2, a single negative review shift can tank your scores. Build alternative authority signals. |

### Score Interpretation

| Range | Meaning |
|---|---|
| 80-100 | Strong influence. High citation rates from owned content. Diverse external sources mostly accurate and positive. Changes you make will flow through to AI. |
| 60-79 | Moderate influence. Some owned content authority but significant third-party dependency. Gaps in source accuracy or diversity. |
| 40-59 | Limited influence. AI's perception of you is shaped more by external sources than your own content. You have some levers but not enough. |
| 20-39 | Weak influence. Almost no owned-content citation. External sources dominate and may be inaccurate. Hard to move the needle without major effort. |
| 0-19 | No influence. AI has no reliable source material. Perception is essentially hallucinated or based on fragments. Everything needs building. |

---

## Section 6: Composite Scores and Relationships

### AI Brand Health — The One Number

A composite of all 4 scores. The NPS of AI visibility. One number (0-100) that goes on the dashboard, in board decks, and in LinkedIn posts. AI Brand Health is the individual brand metric — what you check Monday morning. The CheckThat AI Benchmark (Section 7) is the category-level visualization — the 2x2 chart where every brand in a category is plotted and compared. They serve different audiences: AI Brand Health summarizes your position in one number. The AI Benchmark shows your position relative to every competitor in the category.

```
AI BRAND HEALTH = weighted average of four scores:
  Presence Score (0-100)   x weight
  Reputation Score (0-100) x weight
  Perception Score (0-100) x weight
  Influence Score (0-100)  x weight

Default weights: equal (25/25/25/25)
Configurable per workspace.

Scale: 0-100
```

**Why Influence is in the composite:** A brand with 90% Presence, 85% Reputation, 80% Perception, but 10% Influence has a fragile position — their scores are high but they have no control over maintaining them. Including Influence rewards brands that have durable, self-controlled AI presence.

**Provisional thresholds:**
- 80+ **Strong** — AI knows you, describes you accurately, and you have the levers to maintain it
- 60-80 **Moderate** — AI knows you but has gaps in narrative accuracy or source control
- 40-60 **Needs Work** — Significant issues in one or more dimensions
- <40 **Critical** — AI doesn't know you, misrepresents you, or you have no control

### How Lift Works (Cross-Cutting Trend Layer)

Lift is not a score. It's a meta-layer applied to all 4 scores. Every score has:

**Temporal Trend** — directional movement over time

```
Computed by: linear regression of weekly scores over the lookback period (default: 4 weeks)

Output per score:
  Presence:    ↑ +8% over 4 weeks (confidence: high)
  Reputation:  → flat (confidence: moderate)
  Perception:  ↓ -12% over 4 weeks (confidence: high)
  Influence:   ↑ +15% over 4 weeks (confidence: moderate)

Categories: Improving / Stable / Declining
Magnitude: % change over period
Confidence: based on sample size and variance
```

**Competitive Shift** — your movement relative to competitors

```
Your metric delta minus average competitor metric delta for same period.

Output:
  Gaining ground  — your scores improving faster than competitors
  Holding steady  — moving at the same rate
  Losing ground   — competitors improving faster than you
```

**Cross-Engine Spread** — change in which engines know about you

```
Cross-engine coverage this period minus previous period.

Output:
  Expanding   — appearing on more engines
  Stable      — same engines as before
  Contracting — disappearing from engines
```

**Content Lift** (v2) — metric changes correlated with content actions

```
User marks content publication dates.
System measures before/after on matched prompts.

Output:
  "After publishing the comparison page on Feb 1:
   Presence for Direct Comparison prompts: +23%
   Perception Value attribute: +15%
   Influence internal citation rate: +8%"
```

This is the brand lift study analog. The most valuable measurement for proving ROI of content investment.

### Score Relationships and Diagnostics

The 4 scores are related but independent. The gaps between them are diagnostic:

| Pattern | What It Means | Priority Action |
|---|---|---|
| High Presence + Low Perception | AI mentions you but gets the story wrong | Fix content accuracy and positioning. Use Influence data to identify bad sources. |
| High Presence + Low Reputation | AI mentions you but the world's opinion is weak | Invest in reviews, press, community. The AI data will follow. |
| High Reputation + Low Presence | The world loves you but AI doesn't mention you | Technical AEO problem. Content structure, schema markup, crawlability. |
| High Reputation + Low Perception | Strong external signals but AI misinterprets them | AI is filtering or weighting sources incorrectly. Adjust content for AI consumption. |
| High Perception + Low Influence | AI tells a good story but you have no control over maintaining it | Fragile position. Build owned-content authority before a source shift breaks your narrative. |
| Low Everything | Starting from scratch | Build Reputation first (reviews, press, community). Then Presence (content, schema). Perception and Influence follow. |
| High Everything | Strong position | Monitor and maintain. Watch for competitive shifts and source changes. |

### Additional Composites

**AI Share of Voice** — competitive metric

```
Combines three signals:
  Visibility Share = (your mentions / total mentions across all tracked brands) x 100
  Citation Share = (your citations / total citations) x 100
  Position-Weighted Share = mentions weighted by position (1st=3x, 2nd=2x, 3rd=1.5x, Listed=1x, Afterthought=0.5x)

AI Share of Voice = average of the three shares
```

**AI Endorsement** — how strongly AI advocates for you

```
Combines:
  Recommendation Strength from Perception: 40% weight
  Position Score from Presence: 25% weight
  Narrative Frame (from AI responses): 20% weight
  Comparative framing (preferred/equal/alternative): 15% weight

Scale: 0-100
```

A high AI Endorsement means: when buyers ask for recommendations, AI champions your brand.

---

## Section 7: The CheckThat AI Benchmark

### What It Is

The CheckThat AI Benchmark is CheckThat's signature category visualization. Two axes, four quadrants, dot size for market reputation, and trend arrows for momentum. One chart that shows every brand in a category and how AI perceives them.

Gartner measures how analysts see you. G2 measures how users see you. The CheckThat AI Benchmark measures how AI sees you — and AI is where 94% of B2B buyers are now starting their research.

Every major evaluation framework uses two primary axes. Gartner: Ability to Execute vs Completeness of Vision. Forrester: Current Offering vs Strategy. G2: Satisfaction vs Market Presence. IDC: Capabilities vs Strategies. The structure is universal because it works — it compresses complex vendor evaluation into an instantly readable chart.

The CheckThat AI Benchmark follows the same structure but measures a surface none of them can touch. Both axes are AI-native and proprietary. No analyst firm, review platform, or competitor tool can produce either axis — because no one else surveys AI engines at scale, tracks brand mentions across evaluation-stage prompts, and classifies AI narratives across buyer-relevant attributes.

### The Axes

```
                        PERCEPTION SCORE
                    (What story does AI tell?)
                              100
                               │
                 HIDDEN GEMS   │   AI LEADERS
              (Low Presence,   │  (High Presence,
            High Perception)   │  High Perception)
                               │
           0 ──────────────────┼────────────────── 100
                               │              PRESENCE SCORE
              OFF THE MAP      │   AT RISK    (Does AI recommend
            (Low Presence,     │  (High Presence,  you during
           Low Perception)     │  Low Perception)  evaluation?)
                               │
                               0
```

**X-axis: Presence Score (0-100)** — When buyers are evaluating solutions and ask AI for recommendations without naming you, does AI include you? This is always unaided, always evaluation-stage. Your brand name is never in the prompt. See Section 2 for full methodology.

**Y-axis: Perception Score (0-100)** — What story does AI tell about your brand? Scored across six attributes: Capability, Usability, Value, Trust, Support, Innovation. Each scored 0-10, composited into a 0-100 score. See Section 4 for full methodology.

Together, the axes answer two distinct questions. Presence asks: are you in the conversation? Perception asks: is the conversation any good? A brand needs both. Being recommended by AI is worthless if AI describes you as "basic" or "overpriced." Being described brilliantly is worthless if AI never mentions you.

### The Four Quadrants

#### AI Leaders (Top-Right: High Presence + High Perception)

AI mentions you frequently during buyer evaluation and tells a strong story when it does. This is the winning position — AI both recommends you and describes you accurately, favorably, and with differentiation.

**What it means:** You've earned AI's trust on both dimensions. Buyers using AI to evaluate your category will find you and hear a compelling narrative. This is the position every brand aspires to.

**Reputation dot interpretation:** A big Reputation dot means the market agrees — external reviews, press, and community validate what AI is saying. A small Reputation dot means you're winning in AI before the broader market has caught up. Either way, protect this position. Monitor for competitive displacement and narrative drift.

**What to do here:** Defend. Track weekly for stability. Watch for competitors gaining ground. Ensure your brand context stays current so the AI narrative doesn't become stale. Expand coverage into sub-segments and adjacent categories.

#### At Risk (Bottom-Right: High Presence + Low Perception)

AI mentions you a lot during buyer evaluation, but the narrative is weak. Maybe you're the "old guard" that gets mentioned but described as legacy. Maybe AI surfaces pricing concerns, feature gaps, or support complaints. High visibility with a bad story is arguably worse than low visibility — buyers find you and then hear reasons not to choose you.

**What it means:** You have the presence but the story is wrong. AI is recommending you to buyers and then undermining you in the same breath. This is the most urgent quadrant to fix because you're actively losing deals to a bad AI narrative.

**Reputation dot interpretation:** A big Reputation dot here is alarming — the market thinks well of you but AI doesn't. Something is broken in how AI synthesizes information about you. A small Reputation dot suggests the narrative problem runs deeper than just AI.

**What to do here:** Fix the narrative. Use the Perception attribute scores to identify exactly which of the 6 attributes are dragging you down. Use Influence data to find which sources are feeding the bad story. Update your content, fix inaccurate external sources, and publish the kind of structured, AI-friendly content that corrects the narrative.

#### Hidden Gems (Top-Left: Low Presence + High Perception)

When AI does mention you, it says great things. But it rarely mentions you during evaluation. The product story is strong — AI describes your capabilities, usability, value, and differentiation well. The distribution problem is solvable.

**What it means:** Your content is good enough that when AI finds it, AI tells a compelling story. You just haven't built enough signal for AI to volunteer your name when buyers ask for recommendations. This is the opportunity quadrant — the hardest part (building a great narrative) is already done.

**Reputation dot interpretation:** A big Reputation dot here means the market already knows you but AI hasn't caught up. This is a technical AEO problem — crawlability, schema markup, content structure, third-party citations. A small Reputation dot means both AI and the market are still discovering you. Build external credibility first.

**What to do here:** Solve the distribution problem. Build more third-party citations (Reddit, G2, press coverage, guest posts). Implement structured data and schema markup. Create comparison and "best of" content that AI can cite. Your narrative is already strong — you just need to get it in front of more AI engines, more often.

#### Off the Map (Bottom-Left: Low Presence + Low Perception)

AI doesn't know you exist, and when it does find you, the story isn't compelling. This is where most brands start. It's not a judgment — it's a starting position.

**What it means:** You haven't yet built the signals AI needs to discover you or describe you accurately. There's no shortcut. But the path is clear and well-traveled by every brand that's moved to the upper-right.

**Reputation dot interpretation:** A big Reputation dot here is actually good news — the market already has a favorable view that AI will eventually learn from. Your external reputation is an asset waiting to be discovered. A small Reputation dot means you need to build credibility from the ground up, both for AI and for the market.

**What to do here:** Build Reputation first. Get reviews on G2 and Capterra. Participate on Reddit. Get press coverage. Build a Wikipedia page if you qualify. AI learns from these sources. As external credibility builds, Presence follows. In parallel, structure your own content for AI consumption — answer-first format, schema markup, clear positioning.

### The Third and Fourth Dimensions

**Dot size = Reputation Score** — what the external market thinks, independent of what AI says.

The Reputation dot adds a critical layer of context. Two brands can sit in the same quadrant but tell very different stories based on dot size:

- AI Leader with a big dot: the complete package. AI recommends you, describes you well, AND the market agrees.
- AI Leader with a small dot: winning in AI but the market hasn't caught up. Fragile if AI models retrain and external signals are weak.
- Hidden Gem with a big dot: the market loves you but AI doesn't recommend you yet. Biggest opportunity on the chart — the signal is there, AI just hasn't picked it up.
- Off the Map with a big dot: market reputation exists but isn't translating to AI. Technical AEO problem, not a brand problem.

**Trend arrow = 30-90 day movement** — direction and magnitude of change.

Arrows show momentum. A brand moving toward the top-right is improving. A brand moving toward the bottom-left is losing ground. Arrows create urgency ("we're sliding toward At Risk") and reward action ("our content changes moved us from Hidden Gem toward AI Leader").

Like Everest Group's Star Performer designation and IDC's +/neutral/- growth symbols, trend arrows recognize that position alone doesn't tell the full story. A Hidden Gem with an arrow pointing right is about to become an AI Leader. An AI Leader with an arrow pointing down is about to become At Risk.

### How It's Published

**Per category.** Like Gartner publishes a Magic Quadrant per market, CheckThat publishes an AI Benchmark per category. "The CheckThat AI Benchmark for Expense Management." "The CheckThat AI Benchmark for CRM." Every brand in the category plotted on the same chart.

**Updated continuously.** Not annually like Gartner. Not quarterly like G2. The AI Benchmark reflects live data — updated as new probes run and new responses are captured. Real-time data, living visualization. This is a structural advantage: AI perception shifts weekly, and the measurement should match.

**Public and free.** This is the anti-Gartner. No paywall. No $30,000-$45,000 reprint fees. The AI Benchmark lives on CheckThat's category pages as part of the open index. Anyone can see where any brand sits. Transparency is the positioning.

**Shareable.** Brands can earn and display their position: "AI Leader on the CheckThat AI Benchmark 2026." Badges for websites, press releases, and LinkedIn. The goal is for "CheckThat AI Leader" to carry the same weight as "G2 Leader" or "Gartner Leader" — except it measures the surface that actually matters now.

### How It Maps to the Four Scores

| Score | Role in the AI Benchmark |
|---|---|
| **Presence** | X-axis position. Does AI recommend you during evaluation? |
| **Perception** | Y-axis position. What story does AI tell about you? |
| **Reputation** | Dot size. Does the market validate what AI says? |
| **Influence** | Not on the visualization. It's the diagnostic layer underneath — drill into WHY you're where you are and WHAT to do about it. |

Influence is deliberately excluded from the public visualization. It's the "what to do about it" score, not the "where you are" score. When a brand asks "why am I in the At Risk quadrant?" — Influence tells them whether the problem is their own content, a third-party source, or AI hallucination. It powers the recommendations, not the placement.

**AI Brand Health** (from Section 6) is the single-number summary of all four scores — the dashboard metric. The AI Benchmark is the category-level visualization — the chart brands share externally. They serve different audiences: AI Brand Health is what you check on Monday morning. The AI Benchmark is what you put in board decks and on your website.

---

## Section 8: Open Questions

### 1. Reputation Data Pipeline

**Question:** How do we reliably pull external reputation data from G2, Capterra, TrustRadius, Reddit?

**Context:** Some platforms have APIs. Some require scraping. Some are gated behind partnerships. The Reputation Score depends on consistent, fresh external data.

**Lean:** Start with publicly available review scores (G2 and Capterra have public profiles). Add platform partnerships over time. Reddit data is accessible via API. Press coverage via news APIs or manual curation. Don't let perfect pipeline block v1 — even manually curated Reputation data for top categories is valuable.

### 2. Perception Attribute Weighting

**Question:** Should the 6 Perception attributes be equally weighted in the composite, or should some matter more?

**Context:** Equal weight is the simplest default. But Capability and Trust are arguably more important for most B2B purchases than Support or Innovation. Category-specific weighting would make scores more meaningful but adds complexity.

**Lean:** Equal weight as default. Allow workspace-level custom weights. Show what the score would be under different weightings in settings. Study real data before hardcoding non-equal defaults.

### 3. LLM-as-Judge Accuracy for Perception Scoring

**Question:** How accurate does the LLM classifier need to be at scoring each attribute from AI response text?

**Context:** Target 80% agreement with human evaluators. Build a test set of 200 response examples. Have 2 humans score them on all 6 attributes. Measure LLM agreement with human consensus per attribute.

**Lean:** Some attributes are easier to classify than others. Capability and Value will score well (concrete language). Innovation and Support may be harder (subtler signals). Ship with attribute-level confidence scores. Don't delay launch waiting for 90% accuracy on Innovation.

### 4. Reputation vs. Perception Boundary for "Sentiment"

**Question:** The old framework had a "Reputation" metric that measured AI's sentiment about you. Now Reputation means external market data. Where does AI sentiment live?

**Resolution:** AI's sentiment about you is embedded in Perception. Specifically: the aggregate tone across all 6 attributes captures overall sentiment. If AI describes your Capability positively, Value strongly, but Trust with caveats, the attribute scores reflect that. There is no standalone "sentiment" metric anymore — it's decomposed into the 6 attributes, which are richer.

### 5. Composite Score Weights

**Question:** How should Presence, Reputation, Perception, and Influence be weighted in AI Brand Health?

**Lean:** Equal (25/25/25/25) as default. Per-workspace override capability. Arguments for non-equal:
- Presence should be higher (if you're invisible, nothing else matters)
- Influence should be lower (it's a control metric, not a perception metric)

Counter-argument: equal weight forces brands to address all dimensions. A brand that's visible but inaccurate (high Presence, low Perception) shouldn't get a good composite score.

Start equal. Study real data. Adjust in v2 if patterns emerge.

### 6. Reputation Score Without Full Data

**Question:** What happens if a brand doesn't have G2 reviews, Capterra listings, or press coverage?

**Lean:** Score based on available data only. Show a "data completeness" indicator: "Reputation based on 2 of 5 sources — add more for a more accurate score." Don't penalize for missing data — normalize against available signals. Nudge: "Claim your G2 profile to improve your Reputation Score."

### 7. Cross-Score Correlation Monitoring

**Question:** If Reputation and Perception are highly correlated (external data predicts AI narrative), does one become redundant?

**Lean:** Monitor correlation but expect divergence. The interesting cases are when they diverge — high Reputation but low Perception means AI isn't reading the room, which is a specific problem with a specific fix. If they always agree, we still want both because Reputation is leading (you can change it) and Perception is lagging (AI updates later).

### 8. Engine Weighting

**Question:** Should scores be weighted by engine market share (ChatGPT = 87% of AI referral traffic)?

**Lean:** Market-share weighted as default with an equal-weight toggle. Report per-engine AND aggregate. The default tells the truth; the toggle gives the full picture. A brand invisible on ChatGPT but visible on Perplexity is in trouble — equal weighting hides this.

### 9. Minimum Prompt Volume for Reliable Scoring

**Question:** How many prompts per attribute do we need for a reliable Perception Score?

**Lean:** Based on the macro-category methodology work:

| Attribute | Min prompts | Recommended | Notes |
|---|---|---|---|
| Capability | 8 | 15-25 | One per major feature/capability |
| Usability | 5 | 10-15 | UX, onboarding, learning curve |
| Value | 5 | 10-15 | Pricing, ROI, cost comparison |
| Trust | 5 | 10-15 | Security, reliability, social proof |
| Support | 5 | 8-12 | Quality, responsiveness, documentation |
| Innovation | 5 | 8-12 | Vision, differentiation, trajectory |
| **TOTAL** | **33** | **66-94** | Fits within Free (50) to Pro (500) tiers |

A Free tier user can get a rough Perception Score. A Pro user gets a reliable one. A Business user gets granular, per-attribute drill-downs.

---

*This methodology consolidates months of research — 30,000+ buyer survey respondents, 4 review platform scoring systems, 5 analyst frameworks, 2.2M real AI prompts analyzed, and 8 rounds of framework iteration — into 4 scores a CMO can understand in 30 seconds and act on in a week.*

*Four questions. Four scores. One framework.*

*Do you exist in AI? What does the world think? What story does AI tell about you? How much impact can I have?*

*Everything else is a drill-down.*
