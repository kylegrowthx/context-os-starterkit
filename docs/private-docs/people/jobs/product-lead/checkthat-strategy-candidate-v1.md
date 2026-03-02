# CheckThat: How AI Perceives Brands

*Strategy document. Defines how CheckThat conceptualizes, classifies, and measures AI brand perception.*

---

## Where We Are

CheckThat launched in the first week of February 2026 after four months of building. What you see in the product is what made the cut. We made hard prioritization calls to get here. Not everything in this document exists in the product yet.

The current team: three full-stack engineers (one backend/architecture focused, one UI-heavy, one generalist), a designer available as needed, and a project manager. We could add more help here if once we have strong conviction on roadmap/needs.

This document describes how we think about the product and the direction we want to take. Some of it is built. Some of it is next. Some of it is further out. Your job in this assignment is to use the product, read this document, and help us figure out what comes next, in what order.

---

## The Core Idea

CheckThat doesn't "monitor prompts." It surveys AI engines the way brands survey consumers.

Brand research has well-established disciplines: brand lift studies, brand tracking, awareness surveys, NPS. These all work the same way. You define what truth looks like (your brand, your positioning), you build instruments to probe perception (survey questions), and you measure the gap between truth and perception over time.

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

| Element | What It Captures | Example |
| --- | --- | --- |
| **Company** | Name, description, founding, stage, size | "Ramp: Corporate card and expense management for startups and mid-market" |
| **Products** | What they sell, key features, differentiators | "Corporate cards, expense management, bill pay, accounting automation" |
| **Positioning** | How they want to be perceived | "The finance automation platform that saves companies 5% on spend" |
| **Personas / Buyers** | Who buys, their roles, their pain points | "CFO at 200-person SaaS company tired of manual expense reports" |
| **Competitors** | Who they compete with directly | "Brex, Mercury, Divvy, SAP Concur" |
| **Differentiators** | What makes them different (claimed) | "Only platform that combines cards + AP + accounting automation" |

Brand context is the **answer key**. When we measure AI alignment later, we're comparing AI's description against this.

### 1.2 Market Context

The structure of the market a brand operates in.

| Element | What It Captures | Example |
| --- | --- | --- |
| **Category** | The market segment or software type | "Expense Management Software" |
| **Category definition** | What this category means to buyers | "Tools that help companies track, manage, and automate employee spending" |
| **Players** | All brands in the category | Ramp, Brex, Mercury, Divvy, SAP Concur, Navan, Airbase... |
| **Category dynamics** | How the category is evolving | "Shift from standalone expense tools to full finance platforms" |
| **Adjacent categories** | Related markets | "Corporate Banking", "Accounting Software", "Procurement" |

Market context gives us the **competitive landscape**. We need to understand all the players, not just the one brand being tracked.

### 1.3 Buyer Context

How buyers in this category think, search, and decide.

| Element | What It Captures | Example |
| --- | --- | --- |
| **Buyer personas** | The roles that evaluate and buy | CFO, VP Finance, Controller, Head of Ops |
| **Buying criteria** | What matters in the purchase decision | "Integration with existing accounting software, ease of deployment, cost savings" |
| **Buying journey** | How they move from problem to purchase | "Pain with manual processes > research solutions > evaluate 3-4 vendors > pilot > buy" |
| **Key questions** | The actual questions buyers ask at each stage | "What's the best expense tool for a startup?" / "Ramp vs Brex for Series A?" |
| **Decision triggers** | What pushes them to act | "Audit finding, growth milestone, switching accounting systems" |

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

| Brand Research | CheckThat |
| --- | --- |
| Survey population | AI engines (ChatGPT, Perplexity, Claude, Gemini, Grok) |
| Survey questions | Prompts |
| Sample size | Number of runs per prompt (min 30, ideal 60-100) |
| Survey wave | Tracking cadence (weekly, bi-weekly) |
| Survey panel | The set of prompts tracked over time |
| Control group | Competitor prompts (same questions, measuring their visibility) |
| Test group | Your brand's visibility in the same prompts |

### Prompt Concepts

Five distinct concepts live in the instrument layer:

**Prompt Pattern** - A reusable template with variables.
- Example: `"Best [category] for [industry]"`
- Patterns are the building blocks. They encode question structures that work across categories.

**Prompt Instance** - A concrete, trackable question.
- Example: `"Best expense management tool for healthcare companies"`
- Instances are what actually get run against AI engines.

**Prompt Cluster** - A group of semantically similar instances.
- Example: "Best expense tool for startups" / "Top startup expense management solutions" / "Which expense app should a startup use?"
- Clusters address the Law of Sensitivity (one word change = 10-78% shift in AI responses). You need clusters to get a true signal, not a single prompt.

**Prompt Sequence** - An ordered set of prompts that mimics a buyer conversation.
- Example: Turn 1: "What is expense management?" > Turn 2: "Best expense tools for startups" > Turn 3: "Ramp vs Brex" > Turn 4: "Ramp pricing"
- Sequences reveal how visibility changes across a conversation.

**Response** - What an AI engine returns for a prompt instance at a point in time.
- Responses are the raw data. A single prompt instance generates many responses (across engines, across time).

### Prompt Classification

Every prompt instance is tagged on multiple independent axes. This is a multi-dimensional tagging system, not a hierarchy.

#### Axis 1: Market (WHERE)

- **Category** - The market segment (e.g., "Expense Management", "CRM")
- **Topic** - A thematic cluster within the category (e.g., "Expense tools for startups", "CRM pricing landscape")

#### Axis 2: Intent (WHAT cognitive action)

| Intent | What the Buyer Is Doing | Examples |
| --- | --- | --- |
| **Learn** | Understanding a problem or concept | "What is expense management?" |
| **Explore** | Surveying the landscape of options | "Who are the main players in expense management?" |
| **Compare** | Evaluating specific options head-to-head | "Ramp vs Brex" |
| **Validate** | Confirming a decision with evidence | "Ramp reviews" / "Is Ramp SOC2 compliant?" |
| **Act** | Taking action (implement, buy, switch) | "How to set up Ramp" |

#### Axis 3: Buyer Stage (WHEN in the journey)

| Stage | What's Happening |
| --- | --- |
| **Problem Recognition** | "I have a problem. How bad is it?" |
| **Solution Exploration** | "What kinds of solutions exist?" |
| **Evaluation & Shortlisting** | "Which specific vendors should I consider?" |
| **Decision & Validation** | "Should I buy this? What are the risks?" |
| **Post-Purchase** | "How do I implement? Was this the right call?" |

#### Axis 4: Question Type (WHAT kind of question)

16 types grouped by stage:

**Problem Recognition:** Problem Definition, Category Education
**Solution Exploration:** Approach Comparison, Landscape / Market Map
**Evaluation:** Direct Comparison, Alternatives To, Best-of-Category, Review & Reputation, Pricing & Cost, Feature & Integration
**Decision:** Implementation & Migration, Risk & Compliance, ROI & Business Case, Expert Opinion & Social Proof
**Post-Purchase:** How-To & Implementation, Trend & Future

#### Axis 5: Context Modifiers (WHO is asking)

| Modifier | What It Captures | Example Values |
| --- | --- | --- |
| **Industry** | Buyer's business domain | Healthcare, FinTech, SaaS, Manufacturing |
| **Company Size** | Scale of org | Startup, SMB, Mid-market, Enterprise |
| **Buyer Role** | Who is asking | CFO, VP Marketing, Head of Ops, Founder |
| **Use Case** | Specific problem or workflow | Expense tracking, AP automation, travel management |
| **Geography** | Location/regulatory constraints | US, EU/GDPR, UK, APAC |
| **Tech Stack** | Current tools | QuickBooks, NetSuite, Salesforce, HubSpot |

#### Axis 6: Measurement Purpose (WHY we're asking)

| Purpose | What It Measures | Prompt Example |
| --- | --- | --- |
| **Recall** | Does AI mention/remember the brand? | "Best expense management tools for startups" (unaided) |
| **Sentiment** | How does AI describe the brand? | "Ramp pros and cons" |
| **Alignment** | Does AI's description match brand truth? | "What is Ramp?" / "Ramp pricing" |
| **Competitive Position** | How does AI rank the brand vs competitors? | "Ramp vs Brex" / "Alternatives to Brex" |

### The Generation Engine

How patterns x context variables = the prompt library at scale.

```
Prompt Pattern (template)
    x Category (market segment)
    x Relevant Context Modifiers (industry, size, role, etc.)
    = Prompt Instances (concrete questions)

Example:
    Pattern: "Best [category] for [industry] [company_size]"
    x Category: "Expense Management"
    x Industry: Healthcare, FinTech, SaaS
    x Size: Startup, Mid-market, Enterprise

    = 9 prompt instances:
      "Best expense management tool for healthcare startups"
      "Best expense management tool for healthcare mid-market companies"
      ... etc.
```

Not all combinations are meaningful. The editorial team's job is deciding which combinations reflect real buyer behavior.

### Shared vs. Custom Prompts

**Shared Library (Open Index)**
- Curated by CheckThat's editorial team
- Quality-scored, prioritized, reviewed
- Powers public answer pages and free tier visibility
- Every user benefits from this library

**Custom Prompts (Personal Tracking)**
- Added by users for their specific brand
- Inherit the same classification schema
- Often more niche: specific competitors, specific features, specific positioning
- Can feed back into shared library if quality threshold met

---

## Layer 3: Measurement

Measurement is what we learn from surveying AI engines. This is where CheckThat's value lives. Not in the raw responses, but in the structured intelligence extracted from them.

### The Four Core Metrics

#### RECALL - "Does AI remember us?"

The most fundamental question. If AI doesn't mention your brand, nothing else matters.

| Sub-Metric | Definition | Brand Research Analog |
| --- | --- | --- |
| **Unaided Recall** | Does AI mention you without being asked directly? | Unaided brand awareness |
| **Aided Recall** | Does AI know about you when asked directly? | Aided brand awareness |
| **Recall Rate** | % of relevant questions where your brand appears | Brand awareness % |
| **Recall Position** | Where you appear in the response (1st, 2nd, listed, afterthought) | Top-of-mind vs. total awareness |
| **Recall Stability** | How consistent is recall across runs and time | Tracking consistency |
| **Cross-Engine Recall** | % of engines where you appear for the same question | Cross-channel awareness |

#### SENTIMENT - "How does AI describe us?"

| Sub-Metric | Definition | Brand Research Analog |
| --- | --- | --- |
| **Sentiment Polarity** | Positive, neutral, or negative tone | Brand favorability |
| **Attribute Association** | What concepts does AI associate with you? | Brand attribute perception |
| **Narrative Frame** | What "story" does AI tell about you? | Brand positioning perception |
| **Recommendation Strength** | Does AI recommend you enthusiastically or with caveats? | Consideration vs. preference |

#### ALIGNMENT - "Does AI match our truth?"

This is unique to CheckThat. You define what's TRUE about your brand (Layer 1: Context), then measure how well AI's description matches.

| Sub-Metric | Definition |
| --- | --- |
| **Feature Accuracy** | Does AI correctly describe what you do? |
| **Pricing Accuracy** | Does AI have correct pricing? |
| **Positioning Match** | Does AI position you the way you want? |
| **Differentiator Recognition** | Does AI understand what makes you different? |
| **Narrative Alignment** | Is the story AI tells the story you want told? |
| **Factual Accuracy** | Are the basic facts correct? |

**This is the killer feature.** No other tool has the concept of alignment against a brand source of truth. They just show you what AI says. We tell you if AI is *right*.

#### LIFT - "Is it getting better?"

| Sub-Metric | Definition |
| --- | --- |
| **Content Lift** | Change in metrics after publishing content |
| **Authority Lift** | Change after third-party mentions, reviews, PR |
| **Temporal Trend** | Directional movement over weeks/months |
| **Competitive Shift** | How your metrics move relative to competitors |
| **Cross-Engine Spread** | Change in how many engines cite you over time |

### Composite Scores

**AI Brand Health Score** - A composite of Recall + Sentiment + Alignment, weighted by importance to the brand's goals. CheckThat's equivalent of an overall brand health metric.

**AI Recommendation Score** - How likely is AI to recommend you? Derived from recall position + sentiment + narrative frame. This is our NPS analog.

**Competitive Position Score** - Your share of voice, recall rate, and sentiment relative to competitors across the same prompts.

---

## The Prompt Lifecycle

```
1. DEFINE CONTEXT
   Brand context + Market context + Buyer context
                    |
2. GENERATE INSTRUMENTS
   Prompt patterns x context variables = instances
   Classify on all axes. Score quality. Prioritize.
                    |
3. DEPLOY SURVEY
   Run prompts across AI engines.
   Multiple runs for statistical significance.
                    |
4. EXTRACT MEASUREMENT
   Analyze responses for RECALL, SENTIMENT, ALIGNMENT.
   Compare against brand context (the answer key).
                    |
5. IDENTIFY GAPS
   Where recall is missing, sentiment is negative,
   or alignment is off.
                    |
6. TAKE ACTION
   Content creation, optimization, authority building.
                    |
7. MEASURE LIFT
   Re-run the same prompts. Compare before/after.
                    |
   (Repeat from step 3)
```

---

## Prompt Quality & Prioritization

### Quality Score (5 dimensions, 1-5 each)

| Dimension | Low (1) | High (5) |
| --- | --- | --- |
| **Buyer Realism** | Nobody would ask this | Verbatim from sales calls |
| **Commercial Intent** | Pure information, no buying signal | Active purchase decision |
| **Measurement Value** | Response is generic, can't extract signal | Clear recall/sentiment/alignment signal |
| **Competitive Differentiation** | All brands show up the same | Clear winners and losers |
| **Volume Proxy** | Niche query nobody asks | Maps to high-volume search behavior |

### Sources for High-Quality Prompts (ranked)

1. **Sales call transcripts** - Exact questions prospects ask
2. **Customer support tickets** - Post-sale questions that mirror pre-sale evaluation
3. **Reddit threads** - Raw buyer language
4. **G2 / Capterra reviews** - How buyers describe products in their own words
5. **LinkedIn discussions** - How professionals frame comparisons
6. **Search data** - Query patterns from people already searching

---

## Open Questions

These are real product decisions we're working through.

### 1. Topic Granularity
How granular should topics be? Is "CRM for healthcare" a topic, or is it "CRM for healthcare startups" (with company size as a separate modifier)?

### 2. Cluster Definition
How do we define prompt clusters? Manually? By semantic similarity score? By shared intent?

### 3. Alignment Scoring Methodology
How do we compute alignment between AI response and brand context? Options range from simple keyword matching to LLM-as-judge evaluation.

### 4. Custom-to-Shared Promotion
When does a user's custom prompt get promoted to the shared library? What's the quality threshold?

### 5. Composite Score Weighting
How should Recall, Sentiment, and Alignment be weighted in the AI Brand Health Score? Should it be configurable per brand?

### 6. Multi-Turn Tracking Scope
How much do we invest in multi-turn sequence tracking vs single-prompt tracking? Multi-turn is more realistic but exponentially more complex.

### 7. Engine Weighting
Should metrics be weighted by engine market share or treated equally?

---

## What This Means for Product

### For the UI
- Users should see their AI Brand Health Score front and center
- Drill-down: Recall > Sentiment > Alignment > Lift, each with sub-metrics
- Competitive comparison should be native (not an add-on)
- Context (brand truth) should be editable by the user. It's THEIR answer key

### For Editorial Ops
- The prompt generation pipeline (patterns x context variables) is how we scale the shared library
- Quality scoring and tier prioritization guide what to track and what to editorialize

### For Engineering
- The classification axes become database fields / tags on prompt instances
- Brand context becomes a structured data object (the "answer key")
- Alignment scoring needs an evaluation pipeline (LLM-as-judge or similar)
- Responses are time-series data (prompt x engine x timestamp > response)
