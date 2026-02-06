# CheckThat Prompt Taxonomy & Ontology

*Strategy document. Defines how prompts are conceptualized, classified, and connected in the CheckThat system.*

**Status:** Draft v1
**Last updated:** 2026-02-06

---

## The Core Idea

CheckThat doesn't "monitor prompts." It surveys AI engines the way brands survey consumers.

Brand research has well-established disciplines: brand lift studies, brand tracking, awareness surveys, NPS. These all work the same way — you define what truth looks like (your brand, your positioning), you build instruments to probe perception (survey questions), and you measure the gap between truth and perception over time.

CheckThat does the same thing, except the "consumers" are AI engines. The "survey questions" are prompts. And the "perception" is what ChatGPT, Perplexity, Claude, and Gemini say when buyers ask about your category.

This document defines the three layers of that system: **Context** (the truth), **Instruments** (the questions), and **Measurement** (what we learn).

---

## The Three-Layer Model

```
┌─────────────────────────────────────────────────────┐
│  LAYER 1: CONTEXT                                    │
│  The ground truth. What IS true about your brand,    │
│  your market, your buyers.                           │
│                                                      │
│  Brand Context · Market Context · Buyer Context      │
├─────────────────────────────────────────────────────┤
│  LAYER 2: INSTRUMENTS                                │
│  The questions. How we probe AI engines to           │
│  understand their "perception" of the market.        │
│                                                      │
│  Prompts, classified by topic, intent, type,         │
│  buyer stage, context modifiers, and purpose.        │
├─────────────────────────────────────────────────────┤
│  LAYER 3: MEASUREMENT                                │
│  What we learn. The gap between AI perception        │
│  and brand truth, tracked over time.                 │
│                                                      │
│  Recall · Sentiment · Alignment · Lift               │
└─────────────────────────────────────────────────────┘
```

Each layer depends on the one above it. You can't build good instruments without context. You can't measure meaningfully without good instruments.

---

## Layer 1: Context

Context is the source of truth. It's what we know about a brand, its market, and its buyers BEFORE we ask AI anything. Without context, AI responses are just text. With context, they become measurable signals.

### 1.1 Brand Context

Everything that defines a specific brand from its own perspective.

| Element                     | What It Captures                                  | Example                                                                     |
| --------------------------- | ------------------------------------------------- | --------------------------------------------------------------------------- |
| **Company**           | Name, description, founding, stage, size, funding | "Ramp — Corporate card and expense management for startups and mid-market" |
| **Products**          | What they sell, key features, differentiators     | "Corporate cards, expense management, bill pay, accounting automation"      |
| **Positioning**       | How they want to be perceived                     | "The finance automation platform that saves companies 5% on spend"          |
| **Pricing**           | Plans, price points, model                        | "Free, Plus ($12/user/mo), Enterprise (custom)"                             |
| **Personas / Buyers** | Who buys, their roles, their pain points          | "CFO at 200-person SaaS company tired of manual expense reports"            |
| **Competitors**       | Who they compete with directly                    | "Brex, Mercury, Divvy, SAP Concur"                                          |
| **Differentiators**   | What makes them different (claimed)               | "Only platform that combines cards + AP + accounting automation"            |

Brand context is the **answer key**. When we measure AI alignment later, we're comparing AI's description against this.

### 1.2 Market Context

The structure of the market a brand operates in.

| Element                       | What It Captures                                      | Example                                                                   |
| ----------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------- |
| **Category**            | The market segment or software type                   | "Expense Management Software"                                             |
| **Category definition** | What this category means to buyers                    | "Tools that help companies track, manage, and automate employee spending" |
| **Players**             | All brands in the category (with their brand context) | Ramp, Brex, Mercury, Divvy, SAP Concur, Navan, Airbase...                 |
| **Category dynamics**   | How the category is evolving                          | "Shift from standalone expense tools to full finance platforms"           |
| **Adjacent categories** | Related markets                                       | "Corporate Banking", "Accounting Software", "Procurement"                 |

Market context gives us the **competitive landscape**. We need to understand all the players, not just the one brand being tracked.

### 1.3 Buyer Context

How buyers in this category think, search, and decide.

| Element                     | What It Captures                              | Example                                                                                    |
| --------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Buyer personas**    | The roles that evaluate and buy               | CFO, VP Finance, Controller, Head of Ops                                                   |
| **Buying criteria**   | What matters in the purchase decision         | "Integration with existing accounting software, ease of deployment, cost savings"          |
| **Buying journey**    | How they move from problem to purchase        | "Pain with manual processes → research solutions → evaluate 3-4 vendors → pilot → buy" |
| **Key questions**     | The actual questions buyers ask at each stage | "What's the best expense tool for a startup?" / "Ramp vs Brex for Series A?"               |
| **Decision triggers** | What pushes them to act                       | "Audit finding, growth milestone, switching accounting systems"                            |

Buyer context tells us **which questions matter** and why. It's the bridge between context and instruments.

### How Context Layers Connect

```
Brand Context ─────┐
                    ├──→ Market Context ──→ Buyer Context ──→ Instruments
Brand Context ─────┤    (all players       (how buyers      (the prompts
(competitor 1) ────┤     in category)       think & ask)      we track)
Brand Context ─────┘
(competitor 2)
```

Every brand in a category gets its own brand context. Those combine into market context. Buyer context emerges from understanding the category and its players. Instruments (prompts) are built from buyer context.

---

## Layer 2: Instruments

Instruments are the prompts we use to "survey" AI engines. They're not random questions. They're designed research instruments, built from buyer context, classified for analysis.

### The Analogy

| Brand Research    | CheckThat                                                       |
| ----------------- | --------------------------------------------------------------- |
| Survey population | AI engines (ChatGPT, Perplexity, Claude, Gemini, Grok)          |
| Survey questions  | Prompts                                                         |
| Sample size       | Number of runs per prompt (min 30, ideal 60-100)                |
| Survey wave       | Tracking cadence (weekly, bi-weekly)                            |
| Survey panel      | The set of prompts tracked over time                            |
| Control group     | Competitor prompts (same questions, measuring their visibility) |
| Test group        | Your brand's visibility in the same prompts                     |

### Prompt Concepts (Definitions)

Five distinct concepts live in the instrument layer:

**Prompt Pattern** — A reusable template with variables.

- Example: `"Best [category] for [industry]"`
- Patterns are the building blocks. They encode question structures that work across categories.

**Prompt Instance** — A concrete, trackable question.

- Example: `"Best expense management tool for healthcare companies"`
- Instances are what actually get run against AI engines.
- Generated from patterns × context variables, or written manually.

**Prompt Cluster** — A group of semantically similar instances.

- Example: "Best expense tool for startups" / "Top startup expense management solutions" / "Which expense app should a startup use?"
- Clusters address the Law of Sensitivity (one word change = 10-78% shift in AI responses). You need clusters to get a true signal, not a single prompt.

**Prompt Sequence** — An ordered set of prompts that mimics a buyer conversation.

- Example: Turn 1: "What is expense management?" → Turn 2: "Best expense tools for startups" → Turn 3: "Ramp vs Brex" → Turn 4: "Ramp pricing"
- Sequences reveal how visibility changes across a conversation (you might appear in turn 2 but disappear by turn 4).

**Response** — What an AI engine returns for a prompt instance at a point in time.

- Responses are the raw data. They're what we analyze to produce measurements.
- A single prompt instance generates many responses (across engines, across time).

### Prompt Classification

Every prompt instance is tagged on multiple independent axes. This is a multi-dimensional tagging system, not a hierarchy.

#### Axis 1: Market (WHERE)

Where in the market does this question live?

- **Category** — The market segment (e.g., "Expense Management", "CRM")
- **Topic** — A thematic cluster within the category (e.g., "Expense tools for startups", "CRM pricing landscape")

Topics are more granular than categories. A category might have 20-50 topics. Topics group related prompts.

#### Axis 2: Intent (WHAT cognitive action)

What is the buyer trying to accomplish with this question? Separated from buyer stage because the same intent can appear at different stages.

| Intent             | What the Buyer Is Doing                  | Examples                                                                                |
| ------------------ | ---------------------------------------- | --------------------------------------------------------------------------------------- |
| **Learn**    | Understanding a problem or concept       | "What is expense management?" / "Why do startups need corporate cards?"                 |
| **Explore**  | Surveying the landscape of options       | "Who are the main players in expense management?" / "Types of corporate card solutions" |
| **Compare**  | Evaluating specific options head-to-head | "Ramp vs Brex" / "Compare top 5 expense tools"                                          |
| **Validate** | Confirming a decision with evidence      | "Ramp reviews" / "Is Ramp SOC2 compliant?" / "Ramp case studies"                        |
| **Act**      | Taking action (implement, buy, switch)   | "How to set up Ramp" / "How to migrate from Concur to Ramp"                             |

#### Axis 3: Buyer Stage (WHEN in the journey)

Where the buyer is in their purchasing process. Related to but distinct from intent — a buyer in the Evaluation stage might Learn (reading a comparison guide), Compare (running head-to-head), and Validate (checking reviews) all in one session.

| Stage                               | What's Happening                               |
| ----------------------------------- | ---------------------------------------------- |
| **Problem Recognition**       | "I have a problem. How bad is it?"             |
| **Solution Exploration**      | "What kinds of solutions exist?"               |
| **Evaluation & Shortlisting** | "Which specific vendors should I consider?"    |
| **Decision & Validation**     | "Should I buy this? What are the risks?"       |
| **Post-Purchase**             | "How do I implement? Was this the right call?" |

#### Axis 4: Question Type (WHAT kind of question)

The structural category of the question. 16 types grouped by stage, but any type can appear at any stage.

**Problem Recognition Types:**

1. Problem Definition — "What are the challenges with...?"
2. Category Education — "What is [category]?"

**Solution Exploration Types:**
3. Approach Comparison — "Build vs buy for [solution]"
4. Landscape / Market Map — "Who are the main players in [category]?"

**Evaluation Types:**
5. Direct Comparison — "[Brand A] vs [Brand B]"
6. Alternatives To — "Alternatives to [Brand]"
7. Best-of-Category — "Best [category] for [constraint]"
8. Review & Reputation — "[Brand] reviews" / "[Brand] pros and cons"
9. Pricing & Cost — "[Brand] pricing" / "Best [category] under $X"
10. Feature & Integration — "Does [Brand] have [feature]?"

**Decision Types:**
11. Implementation & Migration — "How hard is it to switch to [Brand]?"
12. Risk & Compliance — "Is [Brand] SOC2 compliant?"
13. ROI & Business Case — "What's the ROI of [Brand]?"
14. Expert Opinion & Social Proof — "What does Reddit say about [Brand]?"

**Post-Purchase Types:**
15. How-To & Implementation — "How to [use feature] in [Brand]"
16. Trend & Future — "Is [category] the future of [domain]?"

#### Axis 5: Context Modifiers (WHO is asking)

The buyer context that shapes the question. These are the variables that multiply prompt patterns into specific instances.

| Modifier               | What It Captures                | Example Values                                     |
| ---------------------- | ------------------------------- | -------------------------------------------------- |
| **Industry**     | Buyer's business domain         | Healthcare, FinTech, SaaS, Manufacturing           |
| **Company Size** | Scale of org                    | Startup, SMB, Mid-market, Enterprise               |
| **Buyer Role**   | Who is asking                   | CFO, VP Marketing, Head of Ops, Founder            |
| **Use Case**     | Specific problem or workflow    | Expense tracking, AP automation, travel management |
| **Geography**    | Location/regulatory constraints | US, EU/GDPR, UK, APAC                              |
| **Tech Stack**   | Current tools                   | QuickBooks, NetSuite, Salesforce, HubSpot          |
| **Budget**       | Price sensitivity               | Free, <$100/mo, $100-500/mo, enterprise            |
| **Timeline**     | Urgency                         | Immediate, this quarter, next year                 |

#### Axis 6: Measurement Purpose (WHY we're asking)

This is new. It connects instruments to measurements. Every prompt has a primary measurement purpose — what it's designed to reveal about AI's perception.

| Purpose                        | What It Measures                           | Prompt Example                                                                       |
| ------------------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------ |
| **Recall**               | Does AI mention/remember the brand?        | "Best expense management tools for startups" (unaided — we don't mention the brand) |
| **Sentiment**            | How does AI describe the brand?            | "Ramp pros and cons" / "Is Ramp worth it?"                                           |
| **Alignment**            | Does AI's description match brand truth?   | "What is Ramp?" / "Ramp pricing" / "Does Ramp integrate with QuickBooks?"            |
| **Competitive Position** | How does AI rank the brand vs competitors? | "Ramp vs Brex" / "Alternatives to Brex"                                              |

This maps to the measurement layer below.

### Prompt Structure Types

How the prompt is constructed (orthogonal to the axes above):

| Structure                     | What It Is                                           | When to Use                                                                            |
| ----------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Simple**              | Plain question, no context                           | "Best CRM for startups" — good for unaided recall testing                             |
| **Persona-Injected**    | Question with buyer context prepended                | "I'm a CFO at a 200-person SaaS company..." — good for segment-specific visibility    |
| **Generated-Knowledge** | Forces AI to generate criteria before recommending   | "List 5 criteria for evaluating [category], then recommend top 3" — stabilizes output |
| **Multi-Turn**          | Sequence of related prompts mimicking a conversation | Turn 1 → Turn 2 → Turn 3 — reveals how visibility changes across a conversation     |

### The Generation Engine

How patterns × context variables = the prompt library at scale.

```
Prompt Pattern (template)
    × Category (market segment)
    × Relevant Context Modifiers (industry, size, role, etc.)
    = Prompt Instances (concrete questions)

Example:
    Pattern: "Best [category] for [industry] [company_size]"
    × Category: "Expense Management"
    × Industry: Healthcare, FinTech, SaaS
    × Size: Startup, Mid-market, Enterprise

    = 9 prompt instances:
      "Best expense management tool for healthcare startups"
      "Best expense management tool for healthcare mid-market companies"
      "Best expense management tool for healthcare enterprise"
      "Best expense management tool for fintech startups"
      ... etc.
```

Not all combinations are meaningful. The editorial team's job is deciding which combinations reflect real buyer behavior.

### Shared vs. Custom Prompts

**Shared Library (Open Index)**

- Curated by CheckThat's editorial team
- Quality-scored, prioritized, reviewed
- 100K+ prompts across 172 categories
- Powers public answer pages and free tier visibility
- Every user benefits from this library

**Custom Prompts (Personal Tracking)**

- Added by users for their specific brand
- Inherit the same classification schema
- Often more niche: specific competitors, specific features, specific positioning
- Paid feature (50 free / 500 Pro / 2,000 Business)
- Can feed back into shared library if quality threshold met

---

## Layer 3: Measurement

Measurement is what we learn from surveying AI engines. This is where CheckThat's value lives — not in the raw responses, but in the structured intelligence extracted from them.

### The Four Core Metrics

Think of these like the core metrics in brand research.

#### RECALL — "Does AI remember us?"

The most fundamental question. If AI doesn't mention your brand, nothing else matters.

| Sub-Metric                    | Definition                                                                                  | Brand Research Analog                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Unaided Recall**      | Does AI mention you without being asked about you directly? (in category/best-of questions) | Unaided brand awareness: "Name three expense management tools" |
| **Aided Recall**        | Does AI know about you when asked directly? (in branded questions)                          | Aided brand awareness: "Have you heard of Ramp?"               |
| **Recall Rate**         | % of relevant questions where your brand appears                                            | Brand awareness %                                              |
| **Recall Position**     | Where you appear in the response (1st, 2nd, listed, afterthought)                           | Top-of-mind vs. total awareness                                |
| **Recall Stability**    | How consistent is recall across runs and time                                               | Tracking consistency                                           |
| **Cross-Engine Recall** | % of engines where you appear for the same question                                         | Cross-channel awareness                                        |

**How to probe it:** Run unbranded questions (category, best-of, alternatives) and check if your brand appears. This is the "unaided awareness" test for AI engines.

#### SENTIMENT — "How does AI describe us?"

Not just positive/negative — it's the full picture of how AI characterizes your brand.

| Sub-Metric                        | Definition                                                                           | Brand Research Analog        |
| --------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------- |
| **Sentiment Polarity**      | Positive, neutral, or negative tone                                                  | Brand favorability           |
| **Attribute Association**   | What concepts does AI associate with you?                                            | Brand attribute perception   |
| **Comparative Sentiment**   | How does AI describe you vs competitors?                                             | Competitive perception       |
| **Narrative Frame**         | What "story" does AI tell about you? (market leader? scrappy upstart? niche player?) | Brand positioning perception |
| **Recommendation Strength** | Does AI recommend you enthusiastically, conditionally, or with caveats?              | Consideration vs. preference |

**How to probe it:** Run review prompts, pros/cons prompts, and branded questions. Analyze the language, not just the mention.

#### ALIGNMENT — "Does AI match our truth?"

This is unique to CheckThat. You define what's TRUE about your brand (Layer 1: Context), then measure how well AI's description matches.

| Sub-Metric                           | Definition                                                      | Brand Research Analog             |
| ------------------------------------ | --------------------------------------------------------------- | --------------------------------- |
| **Feature Accuracy**           | Does AI correctly describe what you do?                         | Message recall accuracy           |
| **Pricing Accuracy**           | Does AI have correct pricing?                                   | Price perception accuracy         |
| **Positioning Match**          | Does AI position you the way you want?                          | Positioning perception vs. intent |
| **Differentiator Recognition** | Does AI understand what makes you different?                    | Unique selling proposition recall |
| **Narrative Alignment**        | Is the story AI tells the story you want told?                  | Brand message alignment           |
| **Factual Accuracy**           | Are the basic facts correct (founding, features, integrations)? | Information accuracy              |

**How to probe it:** Run factual prompts ("What is Ramp?", "Ramp pricing", "Does Ramp integrate with QuickBooks?") and compare AI's response against your brand context (the answer key).

**This is the killer feature.** No other AEO tool has the concept of alignment against a brand source of truth. They just show you what AI says. We tell you if AI is *right*.

#### LIFT — "Is it getting better?"

The impact of your actions on recall, sentiment, and alignment over time.

| Sub-Metric                    | Definition                                                    | Brand Research Analog         |
| ----------------------------- | ------------------------------------------------------------- | ----------------------------- |
| **Content Lift**        | Change in recall/sentiment/alignment after publishing content | Ad lift (exposed vs. control) |
| **Authority Lift**      | Change after third-party mentions, reviews, PR                | Brand awareness lift          |
| **Temporal Trend**      | Directional movement of metrics over weeks/months             | Brand tracking trend          |
| **Competitive Shift**   | How your metrics move relative to competitors                 | Share of voice trend          |
| **Cross-Engine Spread** | Change in how many engines cite you over time                 | Channel expansion             |

**How to probe it:** Track the same prompts over time. Identify when metrics shift. Correlate with content actions, PR events, competitor moves.

### How Metrics Map to Prompt Types

Not every prompt measures every metric equally. The measurement purpose axis (from Layer 2) guides this.

| Prompt Type           | Primary Metric                            | Secondary Metrics    |
| --------------------- | ----------------------------------------- | -------------------- |
| Best-of-Category      | **Recall**                          | Competitive Position |
| Direct Comparison     | **Competitive Position**            | Recall, Sentiment    |
| Alternatives To       | **Recall**                          | Competitive Position |
| Review & Reputation   | **Sentiment**                       | Alignment            |
| Pricing & Cost        | **Alignment**                       | Sentiment            |
| Feature & Integration | **Alignment**                       | Recall               |
| Problem Definition    | **Recall** (early-stage)            | Sentiment            |
| Category Education    | **Alignment** (category definition) | Recall               |
| Implementation        | **Alignment**                       | Sentiment            |
| Risk & Compliance     | **Alignment**                       | Sentiment            |
| ROI & Business Case   | **Sentiment**                       | Alignment            |
| Expert & Social Proof | **Sentiment**                       | Recall               |
| Trend & Future        | **Sentiment**                       | Recall               |

### Composite Scores

Individual metrics combine into higher-level scores (like NPS combines into one number from a simple question).

**AI Brand Health Score** — A composite of Recall + Sentiment + Alignment, weighted by importance to the brand's goals. This is CheckThat's equivalent of an overall brand health metric.

**AI Recommendation Score** — How likely is AI to recommend you? Derived from recall position (1st mention = strong recommend) + sentiment (positive vs caveats) + narrative frame (primary solution vs afterthought). This is our NPS analog.

**Competitive Position Score** — Your share of voice, recall rate, and sentiment relative to competitors across the same prompts. This tells you if you're winning or losing the AI recommendation game.

---

## The AI Survey Analogy (Full Mapping)

This is how CheckThat's concepts map to established brand research disciplines.

| Brand Research Concept             | CheckThat Equivalent                                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Brand Lift Study**         | Measure RECALL + SENTIMENT + ALIGNMENT before/after a content campaign. Did publishing that comparison page change how AI talks about you?                               |
| **Brand Awareness Survey**   | Run category and best-of prompts across engines. Measure unaided recall (do you appear?) and aided recall (do they know you?).                                           |
| **Brand Tracking Study**     | Ongoing weekly/bi-weekly measurement of RECALL, SENTIMENT, ALIGNMENT across your prompt library. Detect trends, correlate with actions.                                  |
| **NPS**                      | AI Recommendation Score — how likely is AI to recommend you when a buyer asks? Derived from recall position + sentiment + narrative frame.                              |
| **CSAT**                     | ALIGNMENT score — how accurately does AI represent your brand at specific touchpoints (pricing page accuracy, feature description accuracy)?                            |
| **CES**                      | Not directly applicable, but could map to: how easy does AI make it for buyers to find and evaluate you? (Presence in multi-turn sequences, consistency across engines.) |
| **Ad Recall Survey**         | Content citation tracking — does AI cite YOUR content as a source? Not just mentioning you, but linking to your pages.                                                  |
| **Purchase Intent Survey**   | AI recommendation position + strength. When AI recommends you, is it a strong "you should use this" or a weak "you could also consider this"?                            |
| **Brand Perception Survey**  | SENTIMENT sub-metrics: attribute association, narrative frame, comparative sentiment. What story does AI tell about you vs what you want it to tell?                     |
| **Competitive Benchmarking** | Same prompts, all competitors tracked. Share of voice, recall rate, sentiment, alignment — all compared head-to-head.                                                   |

### The Fundamental Difference

In traditional brand research, you survey **people** who may or may not have seen your ads.
In AI brand research, you survey **AI engines** that may or may not have learned from your content.

The "exposed vs control" framework from brand lift studies maps perfectly:

- **Exposed:** AI engines that have crawled/trained on your content
- **Control:** AI engines that haven't (or the baseline before your content was published)
- **Lift:** The measurable change in recall, sentiment, and alignment

---

## Entity Relationships

How prompt-related concepts connect to CheckThat's entity model.

### The Entity Graph

```
CONTEXT LAYER                    INSTRUMENT LAYER              MEASUREMENT LAYER

┌──────────┐
│ Category │──has many──→ Topics
└──────────┘                │
      │                     │
  has many              maps to
      │                     │
      ▼                     ▼
┌──────────┐         ┌───────────────┐          ┌───────────┐
│  Brand   │◄─refs───│Prompt Instance│──yields──→│ Response  │
└──────────┘         └───────────────┘          └───────────┘
      │                     │                         │
  has context          generated from            analyzed as
      │                     │                         │
      ▼                     ▼                         ▼
┌──────────┐         ┌───────────────┐          ┌───────────┐
│  Brand   │         │Prompt Pattern │          │ Recall    │
│  Context │         └───────────────┘          │ Sentiment │
│  (truth) │                │                   │ Alignment │
└──────────┘          classified by             │ Lift      │
                            │                   └───────────┘
                            ▼
                     ┌───────────────┐
                     │ Question Type │
                     │ Intent        │
                     │ Buyer Stage   │
                     │ Purpose       │
                     │ Context Mods  │
                     └───────────────┘
```

### Key Relationships

| From            | Relationship       | To                        | Description                                           |
| --------------- | ------------------ | ------------------------- | ----------------------------------------------------- |
| Category        | has many           | Topics                    | A category contains thematic clusters                 |
| Category        | has many           | Brands                    | Brands belong to categories                           |
| Brand           | has                | Brand Context             | The source of truth for alignment measurement         |
| Brand           | appears in         | Responses                 | AI mentions the brand in response to prompts          |
| Topic           | maps to            | Prompt Instances          | Topics organize related prompts                       |
| Prompt Pattern  | generates          | Prompt Instances          | Patterns × context variables = instances             |
| Prompt Instance | grouped into       | Prompt Cluster            | Semantically similar prompts tracking same intent     |
| Prompt Instance | yields             | Responses                 | Each prompt generates responses per engine per run    |
| Prompt Instance | tagged with        | Classification (all axes) | Multi-dimensional tagging                             |
| Prompt Instance | editorialized into | Answer Page               | Public page built on prompt data (not 1:1)            |
| Response        | analyzed as        | Metrics                   | Recall, Sentiment, Alignment extracted from responses |
| Metrics         | compared to        | Brand Context             | Alignment = response vs truth                         |
| Metrics         | tracked over       | Time                      | Lift = change in metrics over time                    |

---

## The Prompt Lifecycle

How a prompt goes from concept to tracked intelligence.

```
1. DEFINE CONTEXT
   Brand context + Market context + Buyer context
   "We know who we are, who our competitors are,
    and what questions our buyers ask."
                    ↓
2. GENERATE INSTRUMENTS
   Prompt patterns × context variables = instances
   Classify on all axes. Score quality. Prioritize.
   "We've built the survey."
                    ↓
3. DEPLOY SURVEY
   Run prompts across AI engines.
   Multiple runs for statistical significance (30-100+).
   Weekly or bi-weekly cadence.
   "We're in the field."
                    ↓
4. EXTRACT MEASUREMENT
   Analyze responses for RECALL, SENTIMENT, ALIGNMENT.
   Compare against brand context (the answer key).
   Calculate composite scores.
   "We have results."
                    ↓
5. IDENTIFY GAPS
   Where recall is missing, sentiment is negative,
   or alignment is off.
   "We know what's wrong."
                    ↓
6. TAKE ACTION
   Content creation, optimization, authority building,
   third-party mentions.
   "We're fixing it."
                    ↓
7. MEASURE LIFT
   Re-run the same prompts. Compare before/after.
   Correlate with actions.
   "Did it work?"
                    ↓
   (Repeat from step 3)
```

---

## Prompt Quality & Prioritization

### Quality Score (5 dimensions, 1-5 each)

| Dimension                             | Low (1)                                   | High (5)                                |
| ------------------------------------- | ----------------------------------------- | --------------------------------------- |
| **Buyer Realism**               | Nobody would ask this                     | Verbatim from sales calls               |
| **Commercial Intent**           | Pure information, no buying signal        | Active purchase decision                |
| **Measurement Value**           | Response is generic, can't extract signal | Clear recall/sentiment/alignment signal |
| **Competitive Differentiation** | All brands show up the same               | Clear winners and losers                |
| **Volume Proxy**                | Niche query nobody asks                   | Maps to high-volume search behavior     |

### Priority Tiers

| Tier             | Score | Action                                          |
| ---------------- | ----- | ----------------------------------------------- |
| **Tier 1** | 20-25 | Track weekly. Immediate content action on gaps. |
| **Tier 2** | 15-19 | Track weekly. Queue content work.               |
| **Tier 3** | 10-14 | Track bi-weekly. Monitor.                       |
| **Tier 4** | <10   | Deprioritize or remove.                         |

### Sources for High-Quality Prompts (ranked)

1. **Sales call transcripts** — Exact questions prospects ask
2. **Customer support tickets** — Post-sale questions that mirror pre-sale evaluation
3. **Reddit threads** — Raw buyer language (cited in 40%+ of Perplexity responses)
4. **G2 / Capterra reviews** — How buyers describe products in their own words
5. **LinkedIn discussions** — How professionals frame comparisons
6. **Search data** — Query patterns from people already searching
7. **Editorial generation** — Pattern × context variable generation (lower quality but scalable)

---

## Open Questions

Decisions that need to be made as we move from strategy to implementation.

### 1. Topic Granularity

How granular should topics be? Is "CRM for healthcare" a topic, or is it "CRM for healthcare startups" (with company size as a separate modifier)? The answer affects how many topics per category and how the UI organizes prompts.

**Lean:** Topics should be broad enough to contain 10-50 prompts each. Context modifiers (industry, size, role) refine within the topic, not create new topics.

### 2. Cluster Definition

How do we define prompt clusters? Manually? By semantic similarity score? By shared intent? Clusters are important (they address AI variability) but the mechanics matter.

**Lean:** Start with manual clustering by editorial team. Automate with embedding similarity later.

### 3. Alignment Scoring Methodology

How do we compute alignment between AI response and brand context? This is the hardest technical problem. Options range from simple keyword matching to LLM-as-judge evaluation.

**Lean:** Use LLM-as-judge with structured evaluation criteria derived from brand context. Start simple, iterate.

### 4. Custom-to-Shared Promotion

When does a user's custom prompt get promoted to the shared library? What's the quality threshold? Who decides?

**Lean:** Automatic flagging when a custom prompt meets quality score + tracking volume thresholds. Editorial review for promotion.

### 5. Composite Score Weighting

How should Recall, Sentiment, and Alignment be weighted in the AI Brand Health Score? Should it be configurable per brand?

**Lean:** Default equal weighting. Allow brands to adjust based on their priorities (e.g., a new brand might weight Recall higher; an established brand might weight Alignment higher).

### 6. Multi-Turn Tracking Scope

How much do we invest in multi-turn sequence tracking vs single-prompt tracking? Multi-turn is more realistic but exponentially more complex.

**Lean:** Ship single-prompt first. Add sequence tracking as a v2 capability. Tag prompts with their typical sequence position so the data model supports it from day one.

### 7. Engine Weighting

Should metrics be weighted by engine market share (ChatGPT = 87% of AI referral traffic) or treated equally? A brand invisible on ChatGPT but visible on Perplexity is in trouble, but equal weighting hides this.

**Lean:** Report per-engine AND aggregate. Aggregate uses market-share weighting by default.

---

## What This Means for Product

### For the UI

- Users should see their AI Brand Health Score front and center (the composite)
- Drill-down: Recall → Sentiment → Alignment → Lift, each with sub-metrics
- Competitive comparison should be native (not an add-on)
- Context (brand truth) should be editable by the user — it's THEIR answer key

### For Editorial Ops

- The prompt generation pipeline (patterns × context variables) is how we scale the shared library
- Quality scoring and tier prioritization guide what to track and what to editorialize
- Answer pages are built from prompt data, not the other way around

### For Engineering (Later)

- The classification axes become database fields / tags on prompt instances
- Brand context becomes a structured data object (the "answer key")
- Alignment scoring needs an evaluation pipeline (LLM-as-judge or similar)
- Responses are time-series data (prompt × engine × timestamp → response)

---

*This document synthesizes from the AEO methodology docs, CheckThat product vision, organic growth strategy, and brand research frameworks. It's a living document — iterate as we build.*
