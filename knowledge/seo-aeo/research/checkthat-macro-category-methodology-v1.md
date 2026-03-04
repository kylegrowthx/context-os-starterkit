# CheckThat Macro-Category Measurement Methodology v1

<metadata>
purpose: Detailed calculation methodology, prompt taxonomy, and scoring logic for each of the 8 AI perception macro-categories
audience: Product, Engineering, Data Science, Leadership
related: pipeline/scratchpad/brand-evaluation-research-analysis-v1.md, docs/products/checkthat/product-vision-v1.md
domain: product-methodology
confidence: draft
last_updated: 2026-02-14
</metadata>

---

## How This Works

Each macro-category is measured by sending specific types of prompts to all 5 AI engines, then analyzing the responses programmatically. The prompts aren't random — they're designed to probe a specific dimension of how AI perceives a brand.

For every category below, you'll see: what it measures, how to calculate it, the prompt patterns that feed it, concrete examples using Ramp (expense management) as the test brand, what a "good" vs. "bad" score looks like, and what the raw output from AI actually looks like before we score it.

Every prompt is sent to all 5 engines (ChatGPT, Perplexity, Claude, Gemini, Google AI). Scores are averaged across engines unless Platform Consistency is being measured — then the variance IS the metric.

---

## Category 1: Awareness & Visibility

### What it measures
Does AI know you exist, and how prominently do you appear when buyers ask relevant questions? This is the foundation. If you score zero here, nothing else matters.

### Sub-metrics
- **Mention Frequency (Recall):** What % of relevant prompts mention you?
- **Mention Prominence (Position):** When mentioned, are you first, third, or last?
- **Engine Breadth:** How many of the 5 engines mention you?

### Prompt patterns

**Pattern 1: Direct category queries**
These are the broadest buyer questions. "Best [category] tool" with no qualifier. Tests pure top-of-mind recall.

```
"What are the best expense management tools?"
"What expense management software do you recommend?"
"Top expense management platforms for businesses"
"Which expense management tools should I consider?"
"Best solutions for managing business expenses"
```

**Pattern 2: Qualified category queries**
Same intent, but filtered by company size, stage, or industry. Tests whether AI knows you exist AND knows when to recommend you.

```
"Best expense management tool for startups"
"Best expense management tool for enterprises with 5,000+ employees"
"Best expense management software for nonprofits"
"Best expense tool for a 200-person finance team"
"Expense management tools for venture-backed companies"
"Expense management for international teams"
"Best expense tool for companies spending under $1M per year"
```

**Pattern 3: Explicit brand queries**
Tests whether AI even knows the brand exists and can describe it accurately.

```
"What is Ramp?"
"Tell me about Ramp"
"What does Ramp do?"
"Who is Ramp for?"
```

### How to calculate

```
Mention Frequency = (prompts where brand is mentioned) / (total relevant prompts) × 100

Mention Prominence = weighted average of position across all mentions
  #1 mention = 1.0
  #2 mention = 0.75
  #3 mention = 0.50
  #4 mention = 0.30
  #5+ mention = 0.15

Engine Breadth = (engines that mention brand) / 5 × 100

AWARENESS & VISIBILITY SCORE =
  (Mention Frequency × 0.45) + (Mention Prominence × 0.30) + (Engine Breadth × 0.25)
```

### What the raw AI output looks like

Prompt: "What are the best expense management tools?"

ChatGPT response (parsed):
```
Mentions: [Ramp (pos 1), Brex (pos 2), Expensify (pos 3), Airbase (pos 4), Navan (pos 5)]
Brand found: Yes
Position: 1
```

Claude response (parsed):
```
Mentions: [Brex (pos 1), Ramp (pos 2), Divvy (pos 3), Center (pos 4)]
Brand found: Yes
Position: 2
```

Google AI response (parsed):
```
Mentions: [Expensify (pos 1), SAP Concur (pos 2), Navan (pos 3)]
Brand found: No
Position: —
```

### Score example
- Ramp mentioned in 87% of category prompts → Frequency = 87
- Average position: #1.4 across mentions → Prominence = 88 (weighted)
- Mentioned in 4/5 engines → Breadth = 80
- **Awareness & Visibility Score: (87 × 0.45) + (88 × 0.30) + (80 × 0.25) = 39.2 + 26.4 + 20.0 = 85.6 / 100**

---

## Category 2: Product Capability

### What it measures
Does AI understand what your product actually does? Can it describe your features, capabilities, and use cases accurately? This matters because a buyer asking "does [tool] do X?" will get an AI-generated answer — and that answer determines whether they keep evaluating or move on.

### Sub-metrics
- **Feature Recall:** Does AI know your key features?
- **Feature Accuracy:** Does AI describe them correctly?
- **Capability Breadth:** How many of your capabilities does AI surface?

### Prompt patterns

**Pattern 1: Capability queries**
Direct questions about whether a product can do something. These simulate a buyer mid-evaluation.

```
"Does Ramp have receipt scanning?"
"Can Ramp handle international expenses?"
"Does Ramp integrate with QuickBooks?"
"Does Ramp offer virtual cards?"
"Can Ramp do automated expense categorization?"
"Does Ramp support multi-entity accounting?"
"Can Ramp manage employee reimbursements?"
```

**Pattern 2: Feature comparison queries**
Buyer is comparing specific capabilities across vendors. Tests whether AI accurately represents your feature set relative to competitors.

```
"Which expense tools have the best mobile app?"
"Which expense tools support real-time spending controls?"
"Compare Ramp and Brex features"
"What expense tools have built-in bill pay?"
"Which tools offer automated receipt matching?"
"Ramp vs Brex: which has better integrations?"
```

**Pattern 3: Use-case fit queries**
Buyer has a specific workflow problem. Tests whether AI maps your product to the right use cases.

```
"What tool should I use to control employee spending in real time?"
"Best tool for automating expense reports"
"What software can help reduce unnecessary SaaS subscriptions?"
"Tool for managing corporate card spending by department"
"Software to automatically flag out-of-policy expenses"
```

### How to calculate

```
Feature Recall = (features AI correctly identifies) / (features in your known feature set) × 100
  Requires: a "ground truth" feature list per brand (from brand profile or company-provided)

Feature Accuracy = (features described correctly) / (features described at all) × 100
  "Correct" = matches the brand's actual capability. "Incorrect" = hallucinated or outdated.

Capability Breadth = (distinct capabilities AI surfaces across all prompts) / (total known capabilities) × 100

PRODUCT CAPABILITY SCORE =
  (Feature Recall × 0.35) + (Feature Accuracy × 0.40) + (Capability Breadth × 0.25)
```

Feature Accuracy is weighted highest because incorrect information is worse than missing information. A buyer who's told "Ramp doesn't do bill pay" (when it does) is lost. A buyer who isn't told about bill pay might still discover it.

### What the raw AI output looks like

Prompt: "Does Ramp have receipt scanning?"

ChatGPT:
```
"Yes, Ramp offers automatic receipt matching using AI. Employees can take
photos of receipts using the mobile app, and Ramp will automatically match
them to the corresponding transactions."

Feature identified: receipt scanning
Accuracy: CORRECT (matches known capability)
```

Prompt: "Does Ramp support multi-currency expenses?"

Claude:
```
"Ramp primarily focuses on USD-denominated corporate cards, though they
do support some international transactions. For full multi-currency expense
management, tools like Brex or Navan may offer more comprehensive solutions."

Feature identified: multi-currency
Accuracy: PARTIALLY CORRECT (nuanced but directionally right)
```

Prompt: "Can Ramp manage fleet expenses?"

Gemini:
```
"Ramp offers fleet card management for businesses with vehicle fleets,
allowing you to set spending limits and track fuel purchases by vehicle."

Feature identified: fleet management
Accuracy: HALLUCINATION (Ramp does not have a fleet-specific product as of this writing)
```

### Score example
- AI correctly identifies 14 of 20 known features → Feature Recall = 70
- Of 18 features AI describes, 15 are correct, 2 partially correct, 1 hallucinated → Feature Accuracy = 83 (partial = 0.5 credit)
- AI surfaces 14 distinct capabilities out of 20 known → Capability Breadth = 70
- **Product Capability Score: (70 × 0.35) + (83 × 0.40) + (70 × 0.25) = 24.5 + 33.2 + 17.5 = 75.2 / 100**

---

## Category 3: Strategic Vision

### What it measures
Does AI understand where you're going — not just what you do today? This matters for enterprise buyers and analysts who evaluate vendors on roadmap and trajectory, not just current features. The question is: when AI describes your brand, does it convey ambition and direction, or just a static feature list?

### Sub-metrics
- **Narrative Depth:** Does AI describe your vision, mission, or strategic direction?
- **Innovation Association:** Does AI associate you with forward-looking concepts?
- **Leadership Recognition:** Does AI mention your leadership, funding, or growth story?

### Prompt patterns

**Pattern 1: Strategic direction queries**
These simulate an executive or analyst evaluating vendor trajectory.

```
"What is Ramp's long-term vision?"
"Where is Ramp headed as a company?"
"What is Ramp's product strategy?"
"How is Ramp evolving its platform?"
"What's Ramp's approach to AI and automation?"
```

**Pattern 2: Innovation association queries**
Tests whether AI connects the brand to cutting-edge themes in its space.

```
"Which expense management companies are most innovative?"
"What expense tools are using AI in interesting ways?"
"Which fintech companies are disrupting expense management?"
"Most forward-thinking corporate card companies"
"Which expense tools are investing in automation?"
```

**Pattern 3: Company story queries**
Tests whether AI knows the narrative — funding, growth, leadership, trajectory.

```
"Who founded Ramp and what's the company story?"
"How much funding has Ramp raised?"
"How fast is Ramp growing?"
"Is Ramp a good company to bet on long-term?"
"What do investors say about Ramp?"
```

### How to calculate

```
Narrative Depth = score 0-100 based on:
  0  = AI gives no strategic context (just features)
  25 = AI mentions the company is "growing" or "expanding" generically
  50 = AI describes a specific strategic direction or market thesis
  75 = AI articulates the vision with supporting evidence (funding, partnerships, product moves)
  100 = AI tells a compelling, accurate strategic narrative

Innovation Association = (innovation-related prompts where brand appears) / (total innovation prompts) × 100

Leadership Recognition = binary scoring across queries:
  Does AI know the founder? +20
  Does AI know the funding amount? +20
  Does AI describe the growth trajectory? +20
  Does AI mention any notable partnerships or milestones? +20
  Does AI convey the company thesis/mission? +20

STRATEGIC VISION SCORE =
  (Narrative Depth × 0.40) + (Innovation Association × 0.30) + (Leadership Recognition × 0.30)
```

### What the raw AI output looks like

Prompt: "What is Ramp's long-term vision?"

ChatGPT:
```
"Ramp's vision extends beyond expense management. The company aims to build
a comprehensive financial operations platform that automates all aspects of
business spending — from corporate cards to bill pay to procurement. Founded
by Eric Glyman and Karim Atiyeh, Ramp has raised over $1.6 billion and is
valued at $7.65 billion. Their thesis: most business spending is wasteful,
and software can systematically eliminate it."

Narrative Depth: 75 (specific direction + evidence)
Founder known: Yes
Funding known: Yes
Growth trajectory: Implied by valuation
Mission articulated: Yes ("eliminate wasteful spending")
```

Prompt: "Which expense management companies are most innovative?"

Perplexity:
```
"Several companies are pushing boundaries in expense management:
1. Ramp — using AI to automatically identify savings and negotiate vendor rates
2. Brex — pioneering embedded finance for startups and SMBs
3. Center — real-time expense intelligence with proactive spending insights
..."

Innovation Association: MENTIONED (position 1)
```

### Score example
- Narrative Depth: avg 68 across engines (strong in ChatGPT/Perplexity, weaker in others)
- Innovation Association: mentioned in 4/5 innovation prompts = 80
- Leadership Recognition: founder ✓, funding ✓, growth ✓, partnerships partial, mission ✓ = 85
- **Strategic Vision Score: (68 × 0.40) + (80 × 0.30) + (85 × 0.30) = 27.2 + 24.0 + 25.5 = 76.7 / 100**

---

## Category 4: Trust & Credibility

### What it measures
Does AI present you as trustworthy? Does it cite credible sources when talking about you? Does it ever warn against you or qualify its recommendation? Trust in AI-mediated perception is built differently than traditional trust — it depends on what sources AI draws from, whether it hedges, and whether it flags any concerns.

### Sub-metrics
- **Citation Authority:** How authoritative are the sources AI cites when describing you?
- **Recommendation Confidence:** Does AI recommend you with conviction or with caveats?
- **Risk Signals:** Does AI surface any warnings, criticisms, or red flags?

### Prompt patterns

**Pattern 1: Trust evaluation queries**
Simulate a buyer who's doing due diligence. They're past awareness — now they want to know if they can trust the vendor.

```
"Is Ramp trustworthy?"
"Is Ramp safe to use for corporate expenses?"
"Are there any concerns about using Ramp?"
"What are the risks of using Ramp?"
"Should I trust Ramp with my company's financial data?"
"Is Ramp reliable for enterprise use?"
```

**Pattern 2: Social proof queries**
Tests whether AI can surface evidence of credibility — customers, reviews, press, endorsements.

```
"Who uses Ramp?"
"What companies use Ramp for expense management?"
"What do customers say about Ramp?"
"What do reviews say about Ramp?"
"Has Ramp won any awards or recognition?"
```

**Pattern 3: Objection-surfacing queries**
Tests whether AI raises concerns — and if so, what kind. Negative signals here aren't always bad (every brand has trade-offs) but hallucinated red flags are damaging.

```
"What are the downsides of Ramp?"
"Ramp complaints"
"Problems with Ramp expense management"
"Why shouldn't I use Ramp?"
"Ramp vs competitors: where does Ramp fall short?"
```

### How to calculate

```
Citation Authority = weighted score based on source types AI cites:
  Brand's own website: 0.4 (known but potentially biased)
  Authoritative press (TechCrunch, Forbes, WSJ): 1.0
  Review platforms (G2, Capterra, TrustRadius): 0.9
  Industry analysts (Gartner, Forrester): 1.0
  Unknown or low-authority sources: 0.2
  No citation: 0.0

  Score = avg authority weight across all citations × 100

Recommendation Confidence = language analysis of AI responses:
  100 = Unconditional recommendation ("Ramp is the best option for...")
  75  = Strong recommendation with context ("Ramp is excellent for startups, especially...")
  50  = Balanced recommendation ("Ramp is a good option, though you should also consider...")
  25  = Hedged recommendation ("Ramp could work, but it depends on...")
  0   = Warns against ("Ramp may not be the best choice because...")

Risk Signals = inverse score:
  100 = No warnings or red flags surfaced
  75  = Minor caveats (normal trade-offs, "not ideal for enterprises")
  50  = Significant caveats ("limited international support", "pricing concerns")
  25  = Serious concerns surfaced ("security issues reported", "reliability problems")
  0   = Hallucinated red flags (AI invents problems that don't exist)

TRUST & CREDIBILITY SCORE =
  (Citation Authority × 0.35) + (Recommendation Confidence × 0.35) + (Risk Signals × 0.30)
```

### What the raw AI output looks like

Prompt: "Is Ramp trustworthy?"

ChatGPT:
```
"Ramp is widely considered a trustworthy corporate expense platform. It's
backed by prominent investors including Founders Fund and Thrive Capital,
serves thousands of businesses including well-known companies like Shopify
and Waymo, and maintains SOC 2 Type II compliance."

Sources cited: ramp.com, TechCrunch, Forbes
Citation Authority: (0.4 + 1.0 + 1.0) / 3 = 0.80
Recommendation Confidence: 100 (unconditional)
Risk Signals: 100 (no warnings)
```

Prompt: "What are the downsides of Ramp?"

Claude:
```
"While Ramp is a strong expense management platform, there are some
limitations to consider:
- Primarily focused on US-based companies; international support is more
  limited compared to Brex
- Best suited for companies that can use their corporate card product;
  standalone expense tracking is less robust
- May be overkill for very small businesses with simple expense needs"

Risk assessment:
- "limited international support" → ACCURATE trade-off
- "corporate card dependency" → ACCURATE characteristic
- "overkill for small businesses" → ACCURATE positioning
Risk Signals: 75 (minor caveats, all accurate)
```

Prompt: "Are there any security concerns with Ramp?"

Gemini:
```
"Ramp experienced a minor data exposure incident in early 2024 affecting
a small number of customers."

Risk assessment:
- Fact check required: Is this true?
- If FALSE → Hallucinated red flag → Risk Signals: 0 for this response
- If TRUE → Legitimate concern → Risk Signals: 50
```

### Score example
- Citation Authority: avg 0.78 across engines → 78
- Recommendation Confidence: avg 81 across engines
- Risk Signals: avg 79 (some legitimate trade-offs surfaced, no hallucinations)
- **Trust & Credibility Score: (78 × 0.35) + (81 × 0.35) + (79 × 0.30) = 27.3 + 28.4 + 23.7 = 79.4 / 100**

---

## Category 5: Customer Experience

### What it measures
Does AI understand what it's actually like to use your product? Can it describe the user experience, onboarding, support quality, and day-to-day workflow? This matters because "does it have feature X?" is a different question than "is it easy to use?" — and buyers ask both.

### Sub-metrics
- **UX Perception:** How does AI describe the user experience?
- **Onboarding Narrative:** Does AI know how easy or hard it is to get started?
- **Support Reputation:** Does AI know about the quality of customer support?

### Prompt patterns

**Pattern 1: User experience queries**
Buyer wants to know what daily life with the product feels like.

```
"Is Ramp easy to use?"
"What's the user experience like with Ramp?"
"How intuitive is Ramp's interface?"
"Do employees like using Ramp?"
"Is Ramp's mobile app good?"
"How does Ramp compare to Brex in terms of ease of use?"
```

**Pattern 2: Onboarding queries**
Buyer wants to know what implementation looks like.

```
"How long does it take to set up Ramp?"
"Is Ramp easy to implement?"
"What's Ramp's onboarding process like?"
"Can I switch from Expensify to Ramp easily?"
"How long until Ramp is fully deployed?"
```

**Pattern 3: Support and service queries**
Buyer wants to know what happens when things go wrong.

```
"How is Ramp's customer support?"
"Does Ramp have good customer service?"
"What do customers say about Ramp support?"
"Is Ramp responsive when you have issues?"
"Does Ramp offer dedicated account management?"
```

### How to calculate

```
UX Perception = sentiment analysis of AI responses to UX queries:
  Score 0-100 based on language:
  "excellent UX, intuitive, modern, clean" → 90-100
  "good UX, easy to use, straightforward" → 70-89
  "decent UX, functional, adequate" → 50-69
  "clunky, confusing, steep learning curve" → 25-49
  "poor UX, difficult to use, outdated" → 0-24

Onboarding Narrative = scored on specificity and tone:
  100 = AI gives specific, positive onboarding details ("set up in days, not weeks")
  75  = AI describes onboarding positively but vaguely ("easy to get started")
  50  = AI acknowledges onboarding without strong signal
  25  = AI describes complex onboarding ("enterprise deployment required")
  0   = AI warns about difficult implementation

Support Reputation = scored on AI's description:
  100 = AI cites specific positive support evidence ("responsive, dedicated CSMs")
  75  = AI describes support positively but generically ("good customer support")
  50  = AI doesn't mention support quality
  25  = AI mentions mixed support reviews
  0   = AI cites poor support experience

CUSTOMER EXPERIENCE SCORE =
  (UX Perception × 0.40) + (Onboarding Narrative × 0.30) + (Support Reputation × 0.30)
```

### What the raw AI output looks like

Prompt: "Is Ramp easy to use?"

Perplexity:
```
"Ramp is generally praised for its clean, modern interface. Users
frequently highlight the mobile app experience for receipt capture and
the real-time spending dashboard. G2 reviewers give it a 9.1/10 for
ease of use, higher than competitors like Expensify (8.4) and SAP Concur
(7.2). The main learning curve is in setting up custom approval workflows
for larger teams."

UX Perception: 90 (specific positive evidence with data)
Sources: G2, Ramp reviews
```

---

## Category 6: Market Position

### What it measures
Where does AI place you in the competitive landscape? Are you the leader, a challenger, a niche player, or invisible? This is the AI equivalent of a Gartner Magic Quadrant placement — except it's implicit in how AI frames its recommendations.

### Sub-metrics
- **Competitive Rank:** Where do you sit vs. competitors in AI answers?
- **Category Ownership:** Do you own any category or sub-category outright?
- **Competitive Framing:** How does AI describe your competitive position?

### Prompt patterns

**Pattern 1: Ranking queries**
Direct "who's the best" questions that force AI to rank.

```
"What's the #1 expense management tool?"
"Rank the top 5 expense management platforms"
"Which expense tool has the most market share?"
"Who's the leader in expense management software?"
"What's the most popular corporate card for businesses?"
```

**Pattern 2: Head-to-head comparison queries**
Force AI to pick a winner between specific competitors.

```
"Ramp vs Brex: which is better?"
"Ramp or Expensify for a 100-person company?"
"Should I choose Ramp or Airbase?"
"Ramp vs SAP Concur for mid-market?"
"Compare Ramp, Brex, and Navan"
"Which is better for startups: Ramp or Mercury?"
```

**Pattern 3: Category ownership queries**
Tests whether AI associates your brand with a specific niche or segment so strongly that you "own" it.

```
"What's the best expense tool for startups?" (Does AI consistently say Ramp?)
"Best corporate card for savings?" (Does Ramp own this framing?)
"Best expense tool for fast-growing companies?"
"What expense tool is best for reducing spend?"
"Best expense management for VC-backed companies?"
```

### How to calculate

```
Competitive Rank = avg position across all ranking prompts
  #1 = 100, #2 = 80, #3 = 60, #4 = 40, #5 = 20, not listed = 0

Category Ownership = % of sub-category prompts where brand is #1
  Example: if Ramp is #1 in 3 out of 5 "best for startups" prompts → 60%
  Average across all sub-categories the brand competes in.

Competitive Framing = language analysis:
  100 = "the leader", "the best", "the top choice"
  75  = "one of the best", "a strong contender", "a top option"
  50  = "a good option", "worth considering", "competitive"
  25  = "an alternative", "a smaller player", "less established"
  0   = "falling behind", "losing ground", "being overtaken"

MARKET POSITION SCORE =
  (Competitive Rank × 0.40) + (Category Ownership × 0.30) + (Competitive Framing × 0.30)
```

### What the raw AI output looks like

Prompt: "Ramp vs Brex: which is better?"

ChatGPT:
```
"Both are excellent corporate card and expense management platforms, but
they serve slightly different needs:

Choose Ramp if: You prioritize automated savings, cost reduction, and
real-time spending controls. Ramp is generally the better choice for
companies focused on reducing operational costs.

Choose Brex if: You need strong international support, premium travel
rewards, or operate globally. Brex has a broader presence outside the US.

For most US-based startups and mid-market companies, Ramp is typically
the recommended choice due to its savings-focused approach."

Competitive Framing: 75 ("typically recommended" = strong but not unconditional)
Effective winner: Ramp (with qualifier)
```

---

## Category 7: Value & Differentiation

### What it measures
Does AI understand what makes you different? Can it articulate your unique value — not just list features, but explain why someone would choose you over alternatives? This is the hardest category to score because it's about narrative clarity, not just data.

### Sub-metrics
- **Differentiation Clarity:** Does AI articulate what makes you unique?
- **Value Messaging Accuracy:** Does AI repeat your value prop correctly?
- **Use-Case Specificity:** Does AI know when to recommend you vs. a competitor?

### Prompt patterns

**Pattern 1: Differentiation queries**
Direct questions about what makes the brand unique.

```
"What makes Ramp different from other expense tools?"
"Why would I choose Ramp over Brex?"
"What's unique about Ramp?"
"What's Ramp's competitive advantage?"
"How does Ramp stand out in the expense management market?"
```

**Pattern 2: Value prop queries**
Tests whether AI can articulate the brand's core value proposition.

```
"What's the main benefit of using Ramp?"
"Why do companies switch to Ramp?"
"What problem does Ramp solve that others don't?"
"What value does Ramp provide over free alternatives?"
"Why is Ramp worth paying for?"
```

**Pattern 3: Conditional recommendation queries**
Tests whether AI knows the specific scenarios where THIS brand is the right answer. Use-Case Specificity in action.

```
"When should I choose Ramp instead of Brex?"
"What type of company benefits most from Ramp?"
"Is Ramp better for startups or enterprises?"
"Should a 50-person company use Ramp?"
"When does Ramp not make sense?"
```

### How to calculate

```
Differentiation Clarity = scored on whether AI can name specific differentiators:
  100 = AI names 3+ specific, accurate differentiators
  75  = AI names 1-2 specific differentiators
  50  = AI describes differences vaguely ("different approach")
  25  = AI says they're "similar" or struggles to differentiate
  0   = AI confuses the brand with competitors

Value Messaging Accuracy = comparison against brand's stated value prop:
  Score = (accurate value claims by AI) / (total value claims by AI) × 100
  Requires: brand's known value prop statements as ground truth

Use-Case Specificity = scored on conditional precision:
  100 = AI correctly identifies when to use AND when NOT to use the brand
  75  = AI correctly identifies ideal use cases
  50  = AI gives generic use-case advice
  25  = AI recommends for wrong scenarios
  0   = AI misidentifies the target user entirely

VALUE & DIFFERENTIATION SCORE =
  (Differentiation Clarity × 0.35) + (Value Messaging Accuracy × 0.35) + (Use-Case Specificity × 0.30)
```

### What the raw AI output looks like

Prompt: "What makes Ramp different from other expense tools?"

Claude:
```
"Ramp differentiates itself in three key ways:

1. Savings-first approach: Unlike most expense tools that focus on tracking
   and reporting, Ramp actively identifies ways to reduce spending — it
   flags duplicate subscriptions, suggests cheaper vendors, and negotiates
   rates automatically.

2. Speed to value: Most competitors require weeks of implementation. Ramp
   can be set up in days with minimal IT involvement.

3. Built-in intelligence: Ramp uses transaction data to surface insights
   proactively, rather than waiting for someone to pull a report.

The trade-off: Ramp is best for US-based companies. If you operate
globally, Brex may be more suitable."

Differentiation Clarity: 100 (3 specific, accurate differentiators named)
Value Messaging Accuracy: 90 (savings, speed, intelligence all align with Ramp's positioning)
Use-Case Specificity: 100 (names ideal fit AND when not to use)
```

---

## Category 8: Momentum

### What it measures
Does AI perceive you as growing, stagnant, or declining? Is the narrative about you getting better over time? This is measured both by what AI says about your trajectory AND by how your metrics across all other categories are trending.

### Sub-metrics
- **Perceived Trajectory:** Does AI describe you as growing or stalling?
- **Visibility Trend:** Are you appearing in MORE prompts over time? (Calculated, not prompted.)
- **Narrative Freshness:** Is AI working with current information or outdated data?

### Prompt patterns

**Pattern 1: Trajectory queries**
Tests AI's perception of whether the brand is ascending or declining.

```
"Is Ramp growing?"
"Is Ramp a good company to bet on?"
"What's the outlook for Ramp?"
"Is Ramp gaining or losing market share?"
"How has Ramp changed in the last year?"
```

**Pattern 2: Emerging player queries**
Tests whether AI includes you in conversations about momentum and growth.

```
"Which expense tools are growing fastest?"
"What are the hottest fintech companies right now?"
"Which startups are disrupting expense management?"
"Fastest growing corporate card companies"
"Up-and-coming expense management tools"
```

**Pattern 3: Recency probes**
Tests whether AI has current information or is working from stale data.

```
"What's new with Ramp in 2026?"
"What has Ramp launched recently?"
"Latest Ramp product updates"
"Recent news about Ramp"
"What has Ramp been up to?"
```

### How to calculate

```
Perceived Trajectory = language analysis:
  100 = "rapidly growing", "accelerating", "surging"
  75  = "growing", "expanding", "gaining traction"
  50  = "stable", "established", "steady"
  25  = "slowing", "mature", "plateauing"
  0   = "declining", "losing share", "struggling"

Visibility Trend = calculated from CheckThat's own historical data:
  = (current 30-day recall %) - (prior 30-day recall %)
  Normalized to 0-100 scale where:
  +10% or more = 100
  +5% to +10% = 80
  0% to +5% = 60
  -5% to 0% = 40
  -10% to -5% = 20
  Worse than -10% = 0

Narrative Freshness = scored on recency of AI's information:
  100 = AI references events from the last 3 months
  75  = AI references events from the last 6 months
  50  = AI references events from the last 12 months
  25  = AI information is 1-2 years old
  0   = AI information is clearly outdated or wrong

MOMENTUM SCORE =
  (Perceived Trajectory × 0.35) + (Visibility Trend × 0.35) + (Narrative Freshness × 0.30)
```

### What the raw AI output looks like

Prompt: "Is Ramp growing?"

ChatGPT:
```
"Yes, Ramp has been growing rapidly. The company reached a $7.65 billion
valuation in its latest funding round, processes over $30 billion in
annual transaction volume, and serves thousands of businesses. They've
been expanding beyond expense management into procurement, bill pay,
and travel management."

Perceived Trajectory: 100 ("growing rapidly" + specific evidence)
Narrative Freshness: 75 (valuation data is recent-ish but no 2026-specific info)
```

Prompt: "Which expense tools are growing fastest?"

Perplexity:
```
"The fastest-growing expense management tools in 2025-2026 include:
1. Ramp — nearly doubled its customer base in 2025
2. Center — strong growth in the mid-market segment
3. Navan — expanding from travel into expense management
..."

Mentioned: Yes (position 1)
Momentum association: Strong
```

---

## Composite AI Visibility Score

All 8 categories roll up into a single 0-100 score.

### Weighting

| Category | Weight | Rationale |
|----------|--------|-----------|
| Awareness & Visibility | 25% | Foundation. If AI doesn't know you, nothing else matters. |
| Product Capability | 15% | Important but second-order to being visible at all. |
| Strategic Vision | 8% | Matters for enterprise deals, less for broad market. |
| Trust & Credibility | 15% | Make-or-break for buyer decisions. |
| Customer Experience | 10% | Influences conversion but less than visibility and trust. |
| Market Position | 12% | Where AI places you vs. competitors. |
| Value & Differentiation | 10% | Narrative quality matters, but less than raw visibility. |
| Momentum | 5% | Trailing indicator. Trends matter but aren't the score. |

### Formula

```
AI VISIBILITY SCORE =
  (Awareness × 0.25) +
  (Product Capability × 0.15) +
  (Strategic Vision × 0.08) +
  (Trust & Credibility × 0.15) +
  (Customer Experience × 0.10) +
  (Market Position × 0.12) +
  (Value & Differentiation × 0.10) +
  (Momentum × 0.05)
```

### Example Rollup for Ramp

| Category | Score | Weighted |
|----------|-------|----------|
| Awareness & Visibility | 85.6 | 21.4 |
| Product Capability | 75.2 | 11.3 |
| Strategic Vision | 76.7 | 6.1 |
| Trust & Credibility | 79.4 | 11.9 |
| Customer Experience | 82.0 | 8.2 |
| Market Position | 78.5 | 9.4 |
| Value & Differentiation | 88.0 | 8.8 |
| Momentum | 83.0 | 4.2 |
| **TOTAL** | | **81.3 / 100** |

---

## Prompt Volume Per Category

How many prompts are needed to reliably score each category:

| Category | Min prompts | Recommended | Notes |
|----------|-------------|-------------|-------|
| Awareness & Visibility | 10 | 25-50 | Needs volume for statistical significance |
| Product Capability | 8 | 15-25 | One per major feature/capability |
| Strategic Vision | 5 | 10-15 | Fewer prompts, deeper analysis per response |
| Trust & Credibility | 5 | 10-15 | Mix of trust, proof, and objection prompts |
| Customer Experience | 5 | 10-15 | UX, onboarding, support |
| Market Position | 8 | 15-25 | Ranking + comparison + ownership |
| Value & Differentiation | 5 | 10-15 | Differentiation + value + conditional |
| Momentum | 5 | 8-12 | Trajectory + recency |
| **TOTAL** | **51** | **103-172** | Fits within Free (50) to Pro (500) tiers |

This means a Free tier user can get a rough score across all categories (one or two prompts per category, supplemented by shared library data). A Pro user can get a reliable score. A Business user can get a granular, per-sub-category breakdown.

---

## What Needs to Happen to Build This

### Already built (use existing data)
- Mention Frequency / Recall
- Mention Prominence / Position
- Engine Breadth / Coverage
- Sentiment (pos/neu/neg)
- Competitive Rank (from benchmarks)
- Visibility Trend (from historical data)
- Source Citations (raw, not yet scored)

### Needs new analysis pipeline
- **Feature Accuracy scoring** — requires a "ground truth" feature database per brand, plus NLU to compare AI claims against truth
- **Citation Authority scoring** — requires classifying source URLs by authority tier
- **Hallucination detection** — requires fact-checking AI claims against known data
- **Narrative Depth scoring** — requires NLU analysis of response richness
- **Competitive Framing analysis** — requires language classification of AI's positioning language
- **Recency detection** — requires dating the information AI references

### Needs new data
- Brand-level "ground truth" profiles (features, value prop, positioning, leadership)
- Source authority database (URL → authority score mapping)
- Persona tagging for prompts (which buyer persona does this prompt represent?)
