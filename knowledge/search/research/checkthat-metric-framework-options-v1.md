# CheckThat Metric Framework Options v1

<metadata>
purpose: Six options for simplifying CheckThat's measurement framework into 4-5 core metrics with composite scores
audience: Marcel, Product, Leadership
related: pipeline/scratchpad/checkthat-macro-category-methodology-v1.md
domain: product-strategy
confidence: draft
last_updated: 2026-02-15
</metadata>

---

## The Problem We're Solving

8 macro-categories with 20+ sub-metrics is a research framework, not a product. Customers don't want a PhD — they want four numbers they can check on Monday morning and act on by Friday. The goal: collapse 77 attributes into 4-5 scores that are instantly understandable, defensible, and actionable.

Marcel's starting instinct — Visibility, Position/Perception, Alignment, Lift — is the right shape. Four metrics. Each one answers a question. Each one drives a different action. Here are six ways to cut it.

---

## Option 1: Brand Intelligence Model
*Aligned to how brand research and monitoring work (Brandwatch, YouGov, Kantar)*

Traditional brand tracking uses Awareness → Perception → Preference → Advocacy. This translates that to AI.

### The Four Metrics

**AWARENESS** — Does AI know you exist?
Rolls up: Mention Frequency, Engine Breadth, Category Association.
One number: "You appear in 72% of relevant AI answers."

**PERCEPTION** — How does AI describe you?
Rolls up: Sentiment Quality, Contextual Accuracy, Feature Accuracy, Narrative Depth.
One number: "AI describes you positively and accurately 81% of the time."

**PREFERENCE** — Does AI recommend you?
Rolls up: Mention Prominence (position), Competitive Rank, Category Ownership, Recommendation Confidence.
One number: "AI recommends you as a top-3 choice in 64% of competitive prompts."

**MOMENTUM** — Is it getting better?
Rolls up: Visibility Trend, Perceived Trajectory, Narrative Freshness.
One number: "Your AI perception improved 6% in the last 30 days."

### Why this framing

This is the language CMOs already speak. They track brand awareness, brand perception, brand preference, and brand momentum in traditional channels. Telling them "same framework, new surface" requires zero education on what the metrics mean. They immediately know that awareness without preference is a problem, that perception without accuracy is dangerous, and that momentum tells them if their work is paying off.

### What it's best at
Selling to marketing leaders who already run brand tracking programs. They'll understand it instantly and see CheckThat as filling a gap in their existing measurement stack.

### What it misses
Doesn't speak the language of SEO/AEO practitioners. Doesn't map cleanly to "what should I do about it?" — a CMO might know their Perception score is low but not know that the fix is updating their Wikipedia page or publishing more technical content.

### How it maps to the 8 macro-categories

| This metric | Absorbs these categories |
|---|---|
| Awareness | Awareness & Visibility |
| Perception | Product Capability, Trust & Credibility, Customer Experience |
| Preference | Market Position, Value & Differentiation |
| Momentum | Momentum, Strategic Vision |

---

## Option 2: AEO Performance Model
*Aligned to Answer Engine Optimization practice*

AEO practitioners think in terms of: Am I indexed? Am I ranking? Is the answer right? Am I improving? This model speaks their language directly.

### The Four Metrics

**RECALL** — Are you in the answer?
Rolls up: Mention Frequency across all tracked prompts and engines.
One number: "AI mentions you in 72% of tracked prompts."
Think of it as: the AEO equivalent of "is my page indexed?"

**RANK** — Where are you in the answer?
Rolls up: Mention Prominence, Competitive Rank, Engine-by-Engine Position.
One number: "You're a top-3 recommendation in 64% of answers where you appear."
Think of it as: the AEO equivalent of "what position am I ranking?"

**ACCURACY** — Is the answer right?
Rolls up: Contextual Accuracy, Feature Accuracy, Sentiment Quality, Citation Authority, Hallucination Rate.
One number: "AI gets your story right 81% of the time."
Think of it as: "is my search snippet accurate?" — but the stakes are higher because AI answers are the whole experience.

**LIFT** — Are you trending up or down?
Rolls up: 30-day trend in Recall, Rank, and Accuracy. Plus Perceived Trajectory and Narrative Freshness.
One number: "+6% overall improvement in the last 30 days."
Think of it as: the AEO equivalent of "am I gaining or losing rank?"

### Why this framing

If CheckThat's market positioning is "the AEO platform," the metrics should sound like AEO. Recall and Rank map directly to SEO concepts people already know (indexation and ranking). Accuracy is the new dimension that makes AEO different from SEO — in search, Google shows your snippet; in AI, the engine writes its own description of you, and it can be wrong. Lift is the trend.

### What it's best at
Selling to growth/SEO/content teams who think in optimization terms. They'll immediately start asking "how do I improve my Recall?" and "what's dragging down my Accuracy?" — which is exactly the behavior that drives engagement and upgrades.

### What it misses
Doesn't resonate with executives who don't think in SEO terms. "Recall" sounds technical. "Rank" sounds like search. Could feel niche to a CMO or CEO who isn't in the AEO weeds.

### How it maps to the 8 macro-categories

| This metric | Absorbs these categories |
|---|---|
| Recall | Awareness & Visibility |
| Rank | Market Position, Value & Differentiation |
| Accuracy | Product Capability, Trust & Credibility, Customer Experience, Strategic Vision |
| Lift | Momentum (plus trends from all other metrics) |

---

## Option 3: Buyer Journey Model
*Aligned to how B2B buyers actually evaluate and decide*

B2B buying follows a path: discover options → evaluate them → validate the shortlist → decide. This model maps to each stage, so each metric tells you where in the funnel you're winning or losing.

### The Four Metrics

**DISCOVERY** — Do buyers find you when they start looking?
Rolls up: Mention Frequency in broad category queries, Engine Breadth, Category Association Strength.
One number: "Buyers discover you through AI in 72% of initial searches."
Prompt types that feed this: "Best [category] tools," "what options exist for [problem]," unbranded exploratory queries.

**CONSIDERATION** — When buyers dig deeper, do you make the shortlist?
Rolls up: Mention Prominence in comparison queries, Competitive Rank in head-to-heads, Feature Recall in capability queries.
One number: "AI includes you on the shortlist in 64% of evaluative queries."
Prompt types: "[Brand] vs [competitor]," "compare top [category] tools," "which [category] tool is best for [use case]."

**VALIDATION** — When buyers do due diligence, does AI back you up?
Rolls up: Sentiment Quality, Trust signals, Citation Authority, Customer Experience description, Recommendation Confidence, Hallucination Rate.
One number: "AI validates your brand positively in 81% of due-diligence queries."
Prompt types: "Is [brand] trustworthy?", "reviews of [brand]", "downsides of [brand]", "[brand] vs [competitor] which is better?"

**TRAJECTORY** — Is your position strengthening over time?
Rolls up: All trends — Recall, Consideration, Validation changes over 30/60/90 days. Plus Momentum signals.
One number: "+6% stronger across the buyer journey vs. last month."

### Why this framing

This is the most actionable framework for revenue teams. Sales and CS immediately understand: "We're strong in Discovery but weak in Validation — buyers find us but AI raises concerns when they dig deeper." That diagnosis maps directly to a fix: improve trust signals, get better reviews, address the objections AI is surfacing.

### What it's best at
Selling to revenue-focused buyers (VPs of Marketing, demand gen leaders, CROs) who think in pipeline and funnel terms. Every metric maps to a stage they already optimize. It also makes the connection between CheckThat data and revenue impact obvious — "we're leaking at Validation" is something a CRO will pay to fix.

### What it misses
Less intuitive for pure brand marketers or SEO practitioners. The "buyer journey" framing assumes the user thinks in funnel terms, which not everyone does. Also, the boundary between Discovery and Consideration can feel blurry in AI (buyers often get all their info in one query, not in a linear funnel).

### How it maps to the 8 macro-categories

| This metric | Absorbs these categories |
|---|---|
| Discovery | Awareness & Visibility |
| Consideration | Market Position, Product Capability, Value & Differentiation |
| Validation | Trust & Credibility, Customer Experience, Strategic Vision |
| Trajectory | Momentum (plus trends from all other metrics) |

---

## Option 4: Signal Strength Model
*Completely different: borrowed from radio/communications engineering*

Think of AI perception like a broadcast signal. Is your signal reaching the receiver? Is it clear? Is it saying the right thing? Is it getting stronger?

### The Four Metrics

**REACH** — How far does your signal travel?
How many AI engines, across how many prompts, in how many categories do you appear?
One number: "Your brand signal reaches 72% of relevant AI conversations."

**CLARITY** — How clean is the signal?
Is AI's description of you accurate, specific, and free of noise (hallucinations, outdated info, competitor confusion)?
One number: "Your brand signal is 81% accurate — 19% contains noise."

**RESONANCE** — Does the signal land?
When AI describes you, does it convey the right message? Does it position you the way you want to be positioned? Does it differentiate you?
One number: "Your intended positioning resonates in 68% of AI descriptions."

**GAIN** — Is the signal amplifying?
Are all three above metrics trending up? Is the overall trajectory positive?
One number: "+6% signal strength over the last 30 days."

### Why this framing

It's metaphorical but intuitive. "Your signal is strong but noisy" is immediately understood — you're showing up but AI is getting the story wrong. "Your signal reaches far but doesn't resonate" — you're visible but not differentiated. The language is neutral enough for any audience (marketing, product, executive) and avoids both brand-jargon and SEO-jargon.

### What it's best at
Creating a distinctive CheckThat vocabulary. No one else uses this language for AI perception. It's ownable, memorable, and makes for good marketing ("What's your signal strength in AI?"). Works across personas — a CMO, a content marketer, and an SEO lead would all understand it.

### What it misses
It's metaphorical, which means there's a learning curve. "Resonance" could mean different things to different people. And the engineering metaphor might feel forced to some buyers — not everyone thinks in signal-processing terms.

### How it maps to the 8 macro-categories

| This metric | Absorbs these categories |
|---|---|
| Reach | Awareness & Visibility, Market Position (breadth dimension) |
| Clarity | Product Capability, Trust & Credibility, Customer Experience |
| Resonance | Value & Differentiation, Strategic Vision, Market Position (depth dimension) |
| Gain | Momentum (plus trends from all other metrics) |

---

## Option 5: Control Model
*Completely different: borrowed from product/growth analytics (Amplitude, Mixpanel thinking)*

Product teams think in inputs and outputs. What can you control, what can you measure, what's the outcome? This model separates "what's happening" from "what you can do about it."

### The Five Metrics (one more than the others — the extra one earns its place)

**PRESENCE** — Are you in the room?
Binary-flavored: what % of the time does AI include you when the topic is relevant?
One number: "You're present in 72% of conversations where you should be."

**POSITION** — Where are you in the room?
When present, are you the recommendation or the also-ran?
One number: "You're a top-3 choice in 64% of answers where you appear."

**NARRATIVE** — What are they saying about you?
Is the story AI tells about you accurate, positive, and differentiated?
One number: "AI tells your story correctly 81% of the time."

**SOURCES** — Who's feeding the story?
What sources does AI cite when talking about you? Are they authoritative, current, and under your influence?
One number: "68% of citations come from sources you can influence."

**DELTA** — What changed?
The unified trend metric. Which of the above went up, which went down, and why?
One number: "+6% net improvement across all metrics."

### Why this framing

Sources is the killer differentiator here. No other framework isolates it. But it's the most actionable metric in AEO — if you know that ChatGPT cites G2 and your G2 profile is weak, you know exactly what to fix. If Claude cites your documentation and it's outdated, you know the fix. This framework turns measurement into a task list.

### What it's best at
Selling to hands-on practitioners who want to DO something with the data, not just report on it. The Sources metric in particular creates immediate "aha" moments: "Oh, AI is citing our competitor's case study page because we don't have one." It bridges the gap between data and action better than any other framework.

### What it misses
Five metrics instead of four is slightly more complex. "Narrative" and "Position" could feel overlapping to some users. And the Sources metric, while powerful, requires CheckThat to build a robust source classification system — it's the hardest to calculate well.

### How it maps to the 8 macro-categories

| This metric | Absorbs these categories |
|---|---|
| Presence | Awareness & Visibility |
| Position | Market Position, Value & Differentiation |
| Narrative | Product Capability, Strategic Vision, Customer Experience |
| Sources | Trust & Credibility (Citation Authority specifically) |
| Delta | Momentum (plus trends from all other metrics) |

---

## Option 6: Scorecard Model
*Completely different: borrowed from NPS / credit scores — one number + a breakdown*

What if the primary metric isn't four numbers — it's ONE number, with four diagnostic dimensions underneath?

### The Structure

**AI VISIBILITY SCORE: 81 / 100**
That's the headline. One number. Like NPS, like a credit score, like Domain Authority. Everyone understands "81 out of 100" instantly. It travels in a sentence: "Our AI Visibility Score is 81." It goes in board decks, Slack messages, LinkedIn posts.

Then four diagnostic dimensions that explain the score:

**VISIBLE** (weight: 30%) — Are you showing up?
Recall %, engine breadth, category coverage.
"You appear in 72% of relevant AI conversations across 4 of 5 engines."

**ACCURATE** (weight: 30%) — Is AI getting you right?
Feature accuracy, sentiment correctness, hallucination rate, citation quality.
"AI describes you correctly 81% of the time."

**DIFFERENTIATED** (weight: 25%) — Does AI know what makes you special?
Competitive position, value prop clarity, use-case specificity, unique narrative.
"AI can articulate your differentiators in 68% of competitive queries."

**TRENDING** (weight: 15%) — Is it getting better?
30-day trend across all above metrics.
"+6% improvement across all dimensions."

### Why this framing

One number is inherently viral. "What's your AI Visibility Score?" is a question that spreads. It's the metric you put on the homepage, the one that converts free users ("Your score is 43 — here's how to improve it"), and the one that lands in board decks. The four dimensions underneath give it depth without complexity — you only drill into them when you need to diagnose a problem.

This is also the most natural fit for the open index. Every brand page shows a public AI Visibility Score. Categories show score distributions. Comparisons show scores side by side. It becomes CheckThat's currency.

### What it's best at
Marketing, virality, and simplicity. The score creates urgency ("yours is 43, your competitor's is 78"). It's benchmarkable. It's tweetable. It makes CheckThat's data tangible without requiring the user to understand four separate metrics. The Visible / Accurate / Differentiated / Trending breakdown is plain English — no jargon, no metaphors, no frameworks to learn.

### What it misses
Any single composite score sacrifices nuance. A brand could be highly visible but totally inaccurate (score looks good, reality is bad). The weighting of the composite becomes a philosophical debate. And some serious buyers will dismiss a single score as too reductive — they'll want the underlying data.

### How it maps to the 8 macro-categories

| This metric | Absorbs these categories |
|---|---|
| Visible | Awareness & Visibility |
| Accurate | Product Capability, Trust & Credibility, Customer Experience |
| Differentiated | Market Position, Value & Differentiation, Strategic Vision |
| Trending | Momentum (plus trends from all other metrics) |

---

## Comparison Matrix

| | Option 1 | Option 2 | Option 3 | Option 4 | Option 5 | Option 6 |
|---|---|---|---|---|---|---|
| **Name** | Brand Intelligence | AEO Performance | Buyer Journey | Signal Strength | Control | Scorecard |
| **Metrics** | Awareness, Perception, Preference, Momentum | Recall, Rank, Accuracy, Lift | Discovery, Consideration, Validation, Trajectory | Reach, Clarity, Resonance, Gain | Presence, Position, Narrative, Sources, Delta | Score + Visible, Accurate, Differentiated, Trending |
| **Best audience** | CMOs, brand marketers | SEO/AEO practitioners, growth teams | Revenue leaders, demand gen | Cross-functional, broad | Hands-on practitioners | Everyone (broadest appeal) |
| **Familiar to** | Brand trackers | SEO tools | CRM/pipeline tools | Novel vocabulary | Product analytics | NPS, credit scores |
| **Actionability** | Medium | High | High | Medium | Highest | Medium-High |
| **Simplicity** | High | High | High | Medium (metaphor) | Medium (5 metrics) | Highest (1 number) |
| **Virality** | Low | Medium | Low | Medium | Low | Highest |
| **Differentiation** | Low (familiar frame) | Medium | Medium | High (ownable) | High (Sources metric) | High (score becomes currency) |
| **Buildability** | Easy (mostly built) | Easy (mostly built) | Easy (reframe existing) | Easy (reframe existing) | Medium (Sources needs new pipeline) | Easy (composite of existing) |

---

## My Recommendation

**Combine Option 6 (Scorecard) as the packaging with Option 2 (AEO Performance) as the engine.**

Here's why:

The AI Visibility Score is the top-level metric. One number. It goes on brand pages, category pages, the dashboard, board decks, and marketing materials. It's what makes CheckThat data viral and benchmarkable. "What's your AI Visibility Score?" becomes the question.

Underneath, use the AEO-aligned breakdown — but with plain-English names:

**AI Visibility Score: 81 / 100**

| Dimension | Plain-English Name | AEO Concept | Score |
|---|---|---|---|
| **Visible** | "Are you showing up?" | Recall | 87 |
| **Accurate** | "Is AI getting you right?" | Accuracy | 81 |
| **Positioned** | "Are you winning?" | Rank / Competitive Position | 74 |
| **Trending** | "Is it getting better?" | Lift | +6% |

Four dimensions. Four questions. One composite score. No jargon. No metaphors. No frameworks to learn.

This gives you:

- **The viral hook** (one number, from Scorecard)
- **The actionable depth** (four clear dimensions, from AEO)
- **The plain language** (questions, not jargon)
- **The build simplicity** (these metrics are mostly already tracked)

And it maps perfectly to the screen design from the earlier doc. The Dashboard shows the score + four dimensions. The Insights screen drills into each dimension. The Benchmarks screen compares scores and dimensions against competitors. The public brand pages show the score prominently.
