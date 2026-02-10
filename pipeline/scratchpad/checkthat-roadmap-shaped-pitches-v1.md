# CheckThat Roadmap — Shaped Pitches

*6 bets for the next 8-10 weeks. Shaped using Ryan Singer's Shape Up methodology. Each pitch has: Problem, Appetite, Solution, Rabbit Holes, No-Gos.*

**Shaped by:** Marcel + AI  
**Date:** 2026-02-09  
**Status:** Draft — needs betting table review

---

## The Dependency Chain

Everything flows from taxonomy. Without it, the rest is guesswork.

```
CYCLE 1 (Weeks 1-2)          CYCLE 2 (Weeks 3-4)          CYCLE 3 (Weeks 5-7)      CYCLE 4 (Weeks 8-9)
┌──────────────┐              ┌──────────────────┐          ┌──────────────────┐      ┌───────────────┐
│  TAXONOMY    │──────────┬──→│ PROMPT           │──┬──────→│ METRICS &        │─────→│ REPORTS /     │
│  (foundation)│          │   │ SUGGESTIONS      │  │       │ DASHBOARD        │      │ INSIGHTS      │
└──────────────┘          │   └──────────────────┘  │       │ RETHINK          │      └───────────────┘
       │                  │   ┌──────────────────┐  │       └──────────────────┘
       └──────────────────┤──→│ ONBOARDING v2    │──┘
                          │   │ (the wow moment) │
┌──────────────┐          │   └──────────────────┘
│  AUTO TAG    │──────────┘
│  (classify)  │
└──────────────┘
```

**The logic:** Taxonomy creates the structure. Auto Tag applies it. Prompt Suggestions use it to be intelligent. Onboarding v2 makes it the first thing users experience. Metrics Rethink builds on classified, structured data. Reports/Insights interpret everything.

---

## Bet 1: Taxonomy — Auto-Generate Workspace Ontology

### Appetite: 2 weeks (small batch)

### Problem

When a user sets up a workspace in CheckThat, the system has no structured understanding of their market. There's no concept of "this is an expense management company competing with Brex and Ramp, selling to CFOs at mid-market SaaS companies."

Without that structure:
- Prompts are a flat list with no organization
- Reports can't slice by buyer stage, question type, or topic
- There's no "answer key" to measure alignment against
- Competitive positioning is manual guesswork
- Every downstream feature is dumber than it should be

The taxonomy doc defines this perfectly as the three-layer model. Layer 1 (Context) is the source of truth. Without it, Layer 2 (Instruments) and Layer 3 (Measurement) are noise. We need to auto-generate Layer 1.

### Solution

A workflow that takes workspace context and auto-generates the full ontology.

**Input:** Company URL or name + any context the user provides (description, products, competitors).

**Auto-generates:**

1. **Brand Context** (the answer key)
   - Company description, products, positioning, pricing model
   - Key differentiators (claimed)
   - Target buyer personas with roles and pain points

2. **Market Context**
   - Primary category (e.g., "Expense Management Software")
   - Category definition (what it means to buyers)
   - Adjacent categories
   - Competitor graph (top 5-10 competitors with their brand context)
   - Category dynamics (how the market is evolving)

3. **Buyer Context**
   - Buyer personas (roles that evaluate and buy)
   - Buying criteria (what matters in the purchase decision)
   - Key questions by buyer stage (the bridge to instruments)

4. **Classification Schema**
   - Topic clusters for their category (20-50 topics)
   - Relevant context modifiers (which industries, sizes, roles matter)
   - Primary measurement purposes per topic

**Output format:** Structured data that becomes the workspace's taxonomy. User reviews, edits, and confirms. The system applies it everywhere.

**How the auto-generation works:**
1. Start with company URL → scrape + LLM research
2. Match to existing categories in our 1,740-category index
3. Pull competitor data from shared index (we already track 5,828 brands)
4. Use LLM to fill gaps (buyer context, category dynamics)
5. Present as "Here's what we found — edit anything that's wrong"

### Rabbit Holes

- **Don't build a custom ontology editor UI.** v1 is auto-generated, user reviews in a simple accept/reject/modify flow. A full taxonomy editor is a 6-week bet by itself.
- **Don't try to make the taxonomy perfectly hierarchical.** Flat tags with relationships are simpler and more flexible than deep trees. A topic like "CRM for healthcare" should be a tag with category=CRM and industry=Healthcare, not a node three levels deep.
- **The LLM research step doesn't need to be exhaustive.** Good enough > perfect. Users know their own market — we just need a starting point they can refine.
- **Don't create custom schemas per workspace.** Every workspace uses the same six classification axes from the ontology doc. The *values* are custom (your topics, your competitors), the *structure* is universal.

### No-Gos

- No manual "build your own taxonomy from scratch" flow. Auto-generate first, always.
- No cross-workspace taxonomy management (shared taxonomies between workspaces).
- No taxonomy versioning in v1. When a user edits, it overwrites.
- No custom classification axes beyond the standard six.

---

## Bet 2: Auto Tag — Classify All Prompts on the Taxonomy

### Appetite: 1 week (small batch, ships with Taxonomy)

### Problem

The shared library has 100K+ prompts. Custom prompts are added daily. Most are untagged or partially tagged. Without consistent classification across the six axes (Market/Topic, Intent, Buyer Stage, Question Type, Context Modifiers, Measurement Purpose), you can't:
- Slice reports by buyer stage
- Identify coverage gaps (no prompts for Decision stage in healthcare)
- Understand which question types drive your visibility
- Connect prompts to measurement purpose (is this measuring Recall or Alignment?)

Manual tagging doesn't scale. An editorial team can review 50-100 prompts a day. We have 100K.

### Solution

A batch classification workflow that:

1. **Takes untagged/partially-tagged prompts** from any source (shared library, custom)
2. **Classifies on all six axes** using LLM-as-judge:
   - Axis 1: Market (category + topic)
   - Axis 2: Intent (Learn, Explore, Compare, Validate, Act)
   - Axis 3: Buyer Stage (Problem Recognition → Post-Purchase)
   - Axis 4: Question Type (16 types from the taxonomy doc)
   - Axis 5: Context Modifiers (industry, size, role, use case, etc.)
   - Axis 6: Measurement Purpose (Recall, Sentiment, Alignment, Competitive Position)
3. **Maps to workspace taxonomy** (uses the topic clusters and context modifiers from Bet 1)
4. **Scores confidence per tag** (high/medium/low)
5. **Auto-applies high-confidence tags**, flags low-confidence for human review
6. **Runs incrementally** — new prompts get classified as they're added

**The classification prompt uses the taxonomy doc's definitions as the rubric.** The 16 question types, 5 intents, 5 buyer stages, and 4 measurement purposes are all defined with examples. Feed those to the LLM as the classification schema.

### Rabbit Holes

- **Don't classify 100K prompts in one batch.** Process by category, run incrementally. Target: classify a workspace's relevant prompts (typically 500-2,000) within minutes, not the entire shared library at once.
- **Confidence thresholds matter.** Be conservative — better to flag uncertain tags than to auto-apply wrong ones. Start with 80% confidence threshold for auto-apply.
- **The six axes are independent.** Some prompts will be crystal clear on Intent (it's obviously a Compare) but ambiguous on Buyer Stage (could be Evaluation or Decision). That's fine. Partial tagging > no tagging.
- **Don't build a custom ML classifier.** LLM-as-judge with the taxonomy doc as the prompt is the v1 approach. A fine-tuned classifier is a future optimization.

### No-Gos

- No user-editable tag schemas (use the standard six axes, always)
- No crowd-sourced tagging
- No re-tagging of already-classified prompts unless taxonomy changes
- No custom confidence thresholds per workspace

---

## Bet 3: Prompt Suggestions — Intelligence-Driven Prompt Generation

### Appetite: 2 weeks (small batch)

### Problem

Users sign up and face an empty custom prompt library. They don't know what to track. The shared library has 100K+ prompts but there's no intelligence connecting a user's context to the RIGHT prompts.

Today: "Here's 100,000 prompts. Good luck."
Goal: "Based on your market, competitors, and buyers, here are the 50 prompts you should track right now."

The methodology doc defines the generation engine: patterns × context variables = instances. We have the patterns (16 categories × templates from Part 12). We have the context variables (from the workspace taxonomy, Bet 1). We just need to connect them.

### Solution

**The Generation Flow:**

1. **Load workspace taxonomy** (brand context, competitors, buyer personas, topics)
2. **Run the generation engine:**
   - Cross prompt patterns (from methodology doc's Part 12 templates) with workspace-specific context variables
   - Generate candidate prompts for each buyer stage
   - Focus on Tier 1 and Tier 2 patterns first (evaluation stage, critical priority)
3. **Deduplicate against shared library:**
   - Embedding-based similarity check
   - If a shared library prompt covers the same intent + topic, surface the shared prompt instead of the custom one
   - Mark workspace-specific variants that ADD something the shared library doesn't cover
4. **Score using the 5-point quality framework:**
   - Buyer Realism (does this match how people actually talk?)
   - Commercial Intent (is there a buying signal?)
   - Measurement Value (can we extract Recall/Sentiment/Alignment?)
   - Competitive Differentiation (do winners and losers emerge?)
   - Volume Proxy (does this map to real search behavior?)
5. **Present suggestions organized by:**
   - Buyer stage (5 stages)
   - Measurement purpose (Recall, Sentiment, Alignment, Competitive Position)
   - Priority tier (Tier 1 first, then Tier 2)
6. **One-click accept/reject.** Accepted prompts go to custom tracking. Rejected prompts get deprioritized for this workspace.

**Volume control:** Generate top 50-100 suggestions per workspace. Not thousands. Quality > quantity for custom tracking.

### Rabbit Holes

- **Semantic dedup is hard.** "Best CRM for startups" and "Top CRM tools for startup companies" are the same intent. Start with embedding similarity (cosine > 0.85 = duplicate), iterate from there. Don't try to build perfect dedup.
- **Don't generate ALL possible combinations.** The math is 23,040 per category. Nobody needs that. The editorial judgment is: which combinations reflect REAL buyer behavior? Use the quality score to filter aggressively.
- **Quality scoring should use LLM-as-judge initially.** Feed the 5 dimensions with definitions and examples. Don't try to build a custom scoring model.
- **Persona-injected variants are v2.** v1 generates simple and best-of prompts. Persona-injected prompts are a separate capability.

### No-Gos

- No user-created prompt patterns (system-generated templates only in v1)
- No multi-turn sequence suggestions (single prompts only)
- No "suggest back to shared library" flow
- No prompt editing during the suggestion flow (accept/reject only, edit later)

---

## Bet 4: Onboarding v2 — The Wow Moment

### Appetite: 2 weeks (small batch, ships after Taxonomy + Suggestions)

### Problem

Current onboarding is utilitarian. Sign up → add brand → empty dashboard. There's no "aha moment." Users don't understand what they're looking at or why it matters. The time-to-value is too long. High setup friction, low perceived value in the first session.

The best B2B onboarding makes you feel like the product already knows you. Slack shows you messages. Figma shows you templates. Canva shows you designs. CheckThat should show you: "Here's how AI sees your brand RIGHT NOW."

### Solution

A guided flow that uses Taxonomy (Bet 1) + Prompt Suggestions (Bet 3) to create an immediate wow.

**The Flow (target: under 3 minutes):**

**Step 1: Enter your brand** (15 seconds)
- User enters company URL or name
- "Let me analyze your market..."

**Step 2: "Here's what we know"** (30 seconds)
- Auto-generated brand context: "You're [company], a [category] company competing with [competitors]. Your buyers are [personas]."
- User confirms or edits (lightweight — checkboxes and toggles, not forms)

**Step 3: "Here's how AI sees you"** (the wow)
- Pull from shared index data (we already have it!)
- Show: Recall rate across AI engines, top competitor comparison, any misalignment flags
- This is data they've NEVER seen before. This is the moment.

**Step 4: "Here's what to track"** (suggestions)
- Top 20 prompt suggestions from the generation engine (Bet 3)
- Organized by priority: "These 5 are most important for your brand right now"
- One-click "Start tracking all" button

**Step 5: "You're live"**
- Dashboard populated with their data from shared index
- Custom prompts activated
- First tracking run scheduled
- "Come back in 24 hours for fresh results"

**The wow is:** Within 2 minutes of signing up, you see exactly how AI perceives your brand, where you stand vs competitors, and what to do about it. No other AEO tool does this because they don't have the open index data.

### Rabbit Holes

- **The auto-detection from URL needs to work well enough.** Use our existing 5,828 brand database first. If the brand exists, pull its data. If not, research via LLM + web. Don't make users wait more than 10 seconds.
- **Don't show empty states during onboarding.** If we don't have data for a specific metric, show competitive context instead. "We don't have your recall data yet, but here's how your category performs."
- **The "initial scores" come from shared index data, not fresh runs.** Fresh runs take time. The wow moment uses existing data from the shared library tracking. Custom prompt results come later.
- **Don't try to make Step 2 (brand context) perfect.** 80% accurate is enough. Users will fix the 20%. The speed matters more than perfection.

### No-Gos

- No manual "build your profile from scratch" — always auto-generate first
- No full dashboard customization during onboarding
- No team/multi-user setup during onboarding (solo experience)
- No "skip onboarding" option — it's the value prop demo
- No historical trend data shown during onboarding (new workspace = no history)

---

## Bet 5: Metrics & Dashboard Rethink

### Appetite: 3 weeks (big batch)

### Problem

The current dashboard shows surface-level data. Mentions, basic sentiment, maybe some trends. But the taxonomy doc defines a much richer measurement framework that maps to established brand research:

- **Recall** (6 sub-metrics): Unaided, Aided, Rate, Position, Stability, Cross-Engine
- **Sentiment** (5 sub-metrics): Polarity, Attribute Association, Comparative, Narrative Frame, Recommendation Strength
- **Alignment** (6 sub-metrics): Feature Accuracy, Pricing Accuracy, Positioning Match, Differentiator Recognition, Narrative Alignment, Factual Accuracy
- **Lift** (5 sub-metrics): Content, Authority, Temporal Trend, Competitive Shift, Cross-Engine Spread

Plus three composite scores:
- **AI Brand Health Score** (the NPS of AI visibility)
- **AI Recommendation Score** (how likely AI is to recommend you)
- **Competitive Position Score** (your share of voice vs competitors)

None of this is reflected in the current dashboard. The taxonomy doc says: "Users should see their AI Brand Health Score front and center." That's not happening.

The brand research analogy is powerful: brand tracking studies, awareness surveys, NPS — these are concepts every marketer understands. The dashboard should speak this language.

### Solution

**Rearchitect around the three-layer model:**

**Primary View: The Score**
- AI Brand Health Score — one number, front and center, with trend arrow
- Sub-scores visible: Recall, Sentiment, Alignment (each as a card with score + trend)
- Competitive comparison: your score vs top 3 competitors

**Drill-Down: The Four Metrics**

Each metric gets its own view:

*Recall View:*
- Unaided recall rate by buyer stage (where do you show up without being asked?)
- Recall position distribution (1st, 2nd, 3rd, listed, afterthought)
- Cross-engine recall map (per engine visibility)
- Stability over time

*Sentiment View:*
- Polarity breakdown (positive/neutral/negative)
- Attribute associations (word cloud or list: what concepts does AI associate with you?)
- Recommendation strength (enthusiastic, conditional, with caveats)
- Narrative frame (market leader? scrappy startup? niche player?)

*Alignment View:* (THE KILLER FEATURE)
- Overall alignment score vs brand context (the answer key)
- Feature accuracy flags (correct/incorrect/missing per feature)
- Pricing accuracy (is AI citing the right pricing?)
- Positioning match (does AI describe you the way you want?)
- Differentiator recognition (does AI know what makes you different?)

*Lift View:*
- Temporal trends (all metrics over time)
- Before/after content actions
- Competitive movement (are you gaining or losing ground?)
- Cross-engine spread changes

**Coverage View: The Gaps**
- Which buyer stages have strong coverage? Which are weak?
- Which question types are well-tracked? Which are missing?
- Topic clusters: where are you visible vs invisible?
- This directly enables the Gap-to-Content Loop from the methodology doc

**Engine View:**
- Per-engine breakdown of all metrics
- Market-share-weighted aggregate as default
- Engine-specific insights (e.g., "You're invisible on Perplexity but strong on ChatGPT")

### Rabbit Holes

- **Don't implement all sub-metrics at once.** Start with the four core metrics (one score each) plus the AI Brand Health composite. Sub-metrics roll out incrementally.
- **Alignment scoring needs the brand context (Layer 1) populated.** Hard dependency on Bet 1. If no taxonomy, no alignment score. Show this as a "complete your profile to unlock alignment insights" prompt.
- **Engine weighting is a philosophical decision.** Ship with both options: per-engine view + market-share-weighted aggregate. Let users toggle. ChatGPT = 87% of AI referral traffic means equal weighting is misleading.
- **Composite score weighting should be simple.** Default: equal weight to Recall, Sentiment, Alignment. Allow brands to adjust (new brand = weight Recall higher, established brand = weight Alignment higher). Don't build a complex weighting engine.
- **The alignment scoring pipeline (LLM-as-judge) is the hardest technical problem.** Don't try to perfect it. Start with structured evaluation criteria derived from brand context. Compare AI response against the answer key on 5-6 dimensions. Score 1-5 each. Average. Ship it. Iterate.
- **Historical data: don't recompute old metrics on the new framework.** Start fresh with new metric calculations. Show old data in legacy views if needed, but the new dashboard starts with new data.

### No-Gos

- No custom metric definitions (everyone uses the standard framework)
- No API for custom dashboards in v1
- No real-time updates (daily refresh is fine)
- No multi-brand view in a single dashboard (one brand per workspace)
- No PDF report export in v1 (dashboard only)

---

## Bet 6: Reports & Insights — The "So What?" Layer

### Appetite: 2 weeks (small batch)

### Problem

Users can see data but can't extract meaning. The dashboard shows numbers. It doesn't answer: "So what? What should I DO?"

When recall drops for a specific question type, what content should I create? When a competitor gains in a topic cluster, what's the right response? When alignment is off on pricing, what page do I fix?

The methodology doc has a full Gap-to-Content Loop (Part 11). But today, users have to figure out those connections themselves.

### Solution

**An insights engine with three layers:**

**Layer 1: Automated Change Detection**
- Monitor week-over-week changes across all metrics
- Flag significant movements (not noise — use statistical significance thresholds)
- Categorize: Recall changes, Sentiment shifts, Alignment gaps, Competitive movements

**Layer 2: Contextual Interpretation**
Using the taxonomy, translate changes into meaningful insights:
- "Your recall dropped 15% for *Best-of-Category* prompts in the *Healthcare* topic cluster"
- "Competitor X gained 3 positions in *Direct Comparison* prompts this week"
- "AI is describing your pricing incorrectly in 40% of pricing-related prompts" (alignment gap)
- "You're invisible in *Problem Recognition* prompts — you have no early-stage visibility"

**Layer 3: Action Recommendations**
Map insights to the Gap-to-Content Loop:

| Insight | Recommended Action |
|---------|-------------------|
| Not appearing in "[X] vs [Y]" | Create definitive comparison page |
| Not appearing for "alternatives to [competitor]" | Build alternatives content, target competitor weaknesses |
| Not appearing for "best [category] for [use case]" | Create industry-specific landing pages and case studies |
| Incorrect information appearing | Update pricing pages, add schema markup, refresh FAQ |
| Mentioned but not cited | Improve content structure, lead with answers, add schema |
| Negative sentiment | Address criticism directly, publish counter-evidence |
| Appear early but drop off later | Build deeper evaluation-stage content |

**Delivery:** 
- Weekly digest view in dashboard ("This Week's Top Insights")
- Each insight is clickable → drill into supporting data
- Sorted by impact (biggest metric movers first)

### Rabbit Holes

- **Don't build a fully automated content recommendation engine.** Pattern-matched insights are enough. "Your recall dropped in healthcare best-of prompts" + "Create industry-specific landing pages" is actionable without being prescriptive.
- **Significance thresholds need tuning.** AI visibility is volatile (only 30% of brands maintain stable visibility). Don't alert on normal fluctuation. Use the Stability Index to determine what's signal vs noise.
- **Don't try to attribute metric changes to specific content actions.** Correlation ≠ causation. Show temporal correlation ("recall improved 2 weeks after you published X") but don't claim causation.
- **The Gap-to-Content mapping from the methodology doc is the playbook.** Use it as the recommendation engine's rule set. Don't try to be more creative than the framework.

### No-Gos

- No automated content generation from insights
- No Slack/email notification system in v1 (dashboard-only)
- No custom insight rules or thresholds
- No cross-workspace insight aggregation
- No predictive insights ("we think X will happen") — only observed changes

---

## Recommended Sequencing

### Cycle 1: Foundation (Weeks 1-2)
**Bet:** Taxonomy + Auto Tag  
**Why first:** Everything depends on it. Can't suggest prompts, can't build meaningful metrics, can't create a wow onboarding without the ontology layer.  
**Ship criteria:** A workspace can auto-generate its taxonomy from company context, and existing prompts get classified across all 6 axes.

### Cycle 2: Intelligence (Weeks 3-4)
**Bet:** Prompt Suggestions + Onboarding v2  
**Why second:** These are the user-facing expression of the taxonomy. Prompt Suggestions make custom tracking intelligent. Onboarding v2 makes the first experience magical. Together they solve the "empty state" problem.  
**Ship criteria:** New user goes from signup to "wow, I can see how AI perceives my brand" in under 3 minutes. Existing users get smart prompt suggestions based on their taxonomy.

### Cycle 3: Measurement (Weeks 5-7)
**Bet:** Metrics & Dashboard Rethink  
**Why third:** Needs classified data (from Cycle 1) and users who understand their market structure (from Cycle 2). This is the biggest bet — 3 weeks. The dashboard is where customers live daily.  
**Ship criteria:** AI Brand Health Score on the primary dashboard. Four core metrics with drill-downs. Competitive comparison native to every view.

### Cycle 4: Action (Weeks 8-9)
**Bet:** Reports & Insights  
**Why last:** Needs the new metric framework (from Cycle 3) to generate meaningful insights. Without rich metrics, insights are "your mentions went up" instead of "your alignment on pricing is off — fix your pricing page."  
**Ship criteria:** Weekly digest with 3-5 actionable insights per workspace. Each insight maps to a recommended content action.

---

## The Big Picture

What we're building across these 4 cycles is the full realization of the taxonomy doc's three-layer model:

**Before:** A dashboard that shows mentions. That's it.

**After:**
- **Layer 1 (Context):** Auto-generated, structured brand truth — the answer key (Taxonomy)
- **Layer 2 (Instruments):** Intelligently classified prompts, suggested based on your market (Auto Tag + Prompt Suggestions)
- **Layer 3 (Measurement):** Rich metrics (Recall, Sentiment, Alignment, Lift) with composite scores and gap analysis (Metrics Rethink + Reports)
- **The Experience:** A new user sees their AI Brand Health Score within 2 minutes (Onboarding v2)

This is what makes CheckThat the AI brand research platform, not just another AEO monitoring tool. The taxonomy doc's killer insight: "No other AEO tool has the concept of alignment against a brand source of truth. They just show you what AI says. We tell you if AI is RIGHT."

These 6 bets are how we ship that.

---

## Open Questions for Betting Table

1. **Appetite reality check:** Is 2 weeks realistic for Taxonomy given the LLM workflow complexity? Or is this a 3-week bet?
2. **Auto Tag scope:** Should we classify the ENTIRE shared library (100K prompts) or only prompts relevant to active workspaces?
3. **Metrics data:** Can we compute the new metrics on existing response data, or do we need new analysis pipelines?
4. **Alignment scoring:** How good does the LLM-as-judge need to be at launch? 80% accuracy? 90%? What's the "good enough" bar?
5. **Engine weighting default:** Market-share-weighted (ChatGPT dominates) or equal weight? This changes the story for every customer.
6. **Onboarding wow dependency:** If taxonomy auto-generation is slow (>10 seconds), does the onboarding flow break? Do we need a loading experience?

---

*Next step: Review at betting table. Each bet gets a go/no-go. Adjust appetite based on team capacity. Shape any bet that needs more definition.*
