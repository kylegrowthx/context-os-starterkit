# CheckThat Prompt Patterns — Comprehensive Reference

<metadata>
purpose: Pattern library for prompt tracking campaigns — maps to CheckThat's 4-score measurement framework
audience: Product, engineering, marketing
related: pipeline/scratchpad/checkthat-ontology-product-roadmap-v1.md, pipeline/outputs/checkthat-metrics-framework-v1.md
domain: product-strategy
confidence: working-draft
sensitivity: internal
context_tier: 2
last_updated: 2026-02-18
</metadata>

---

## How to Use This Document

This is a **lookup reference**, not a methodology guide. Every pattern block follows a consistent format: pattern ID, score routing, template with variables, and a concrete example. Find the score you want to measure, find the pattern type, copy and customize.

**The one rule you must know before using any pattern:** If the brand name is NOT in the prompt, it feeds **Presence**. If the brand name IS in the prompt, it feeds **Perception**. This routing rule determines which section you need. Sections 2 and 2.5 are Presence (unbranded). Sections 3-4 are Perception (branded). Sections 5-6 are advanced structures that apply to both.

**Sibling documents for methodology depth:**
- Prompt writing methodology: `knowledge/aeo/guides/prompt-writing-methodology.md`
- Buyer evaluation playbook: `knowledge/aeo/guides/buyer-evaluation-prompt-playbook.md`
- Full methodology & pattern library: `knowledge/aeo/research/prompt-methodology-and-pattern-library.md`
- CheckThat measurement framework: `products/checkthat-methodology.mdx`

---

## Section 1: The Routing Rule

Every prompt you write feeds exactly one CheckThat score (sometimes two). The routing is mechanical:

```
Is the brand name in the prompt?
├── NO  → Is it evaluation-stage? (buyer building a shortlist)
│         ├── YES → PRESENCE
│         └── NO  → Early Presence (Tier 3 — awareness, not shortlisting)
└── YES → PERCEPTION (which of the 6 attributes depends on the question type)
```

### Score-to-Prompt Routing Table

| Score | Brand in prompt? | Buyer stage | What it measures | Prompt types |
|-------|-----------------|-------------|-----------------|--------------|
| **Presence** | Never | Evaluation only | Does AI recommend you when buyers build shortlists? | Best-of-category, Landscape, Alternatives-to, Unbranded comparison |
| **Perception** | Always | Any stage | What story does AI tell about you? (6 attributes) | All 16 question types when branded |
| **Reputation** | N/A | N/A | External market signals — measured from review platforms, community, press | Not directly prompted; monitored via Section 5 |
| **Influence** | N/A | N/A | Source citation analysis — how much of what AI reads you control | Not directly prompted; measured from citation data |

### Edge Cases

**Branded comparisons** ("[Brand A] vs [Brand B]") are **dual-measurement**. They feed Perception (how AI characterizes your brand in the comparison) AND can reveal Presence signals (whether AI recommends competitors you weren't tracking). See Section 4.

**Alternatives-to prompts** ("Alternatives to [Competitor]") where YOUR brand is NOT named feed **Presence** — you want to appear as the alternative. If YOUR brand IS named ("Alternatives to [Your Brand]"), it feeds **Perception** — what does AI recommend instead of you?

**Problem recognition prompts** (unbranded, early-stage: "What causes data silos?") are **not Presence** by CheckThat's definition. Presence requires evaluation-stage intent. These are labeled Early Presence / Tier 3 in Section 2.5.

---

## Section 2: Presence Patterns

*All patterns in this section are unbranded. The brand name never appears in the prompt. These measure whether AI recommends you when buyers are building shortlists.*

*Sub-metrics fed: Presence Rate, Position, Stability Index, Cross-Engine Coverage.*

### 2.1 Best-of-Category Patterns

The highest-priority Presence patterns. These directly correspond to shortlist-building moments — when buyers ask AI "who should I consider?"

**[P-001] Best-of-Category — Core**
Score: Presence | Stage: Evaluation | Type: Best-of-Category | Intent: Explore | Priority: T1

TEMPLATE: `"Best [category] tools for [company type]"`
EXAMPLE: "Best expense management tools for mid-market SaaS companies"

> Feeds: Presence Rate, Position, Cross-Engine Coverage

**[P-002] Best-of-Category — By Company Size**
Score: Presence | Stage: Evaluation | Type: Best-of-Category | Intent: Explore | Priority: T1

TEMPLATE: `"Best [category] for [company size] companies"`
EXAMPLE: "Best CRM for startups with under 50 employees"

> Feeds: Presence Rate, Position (segment-specific visibility)

**[P-003] Best-of-Category — By Industry**
Score: Presence | Stage: Evaluation | Type: Best-of-Category | Intent: Explore | Priority: T1

TEMPLATE: `"Best [category] for [industry]"`
EXAMPLE: "Best project management software for healthcare organizations"

> Feeds: Presence Rate, Position (industry-specific visibility)

**[P-004] Best-of-Category — By Buyer Role**
Score: Presence | Stage: Evaluation | Type: Best-of-Category | Intent: Explore | Priority: T1

TEMPLATE: `"Best [category] for [role/team]"`
EXAMPLE: "Best marketing automation tools for growth marketers"

> Feeds: Presence Rate, Position (persona-specific visibility)

**[P-005] Best-of-Category — By Use Case**
Score: Presence | Stage: Evaluation | Type: Best-of-Category | Intent: Explore | Priority: T1

TEMPLATE: `"Best [category] for [specific use case]"`
EXAMPLE: "Best data integration platform for real-time analytics"

> Feeds: Presence Rate, Position (use-case visibility)

**[P-006] Best-of-Category — By Integration**
Score: Presence | Stage: Evaluation | Type: Best-of-Category | Intent: Explore | Priority: T1

TEMPLATE: `"Best [category] that integrates with [platform]"`
EXAMPLE: "Best CRM that integrates with HubSpot"

> Feeds: Presence Rate (integration-qualified visibility)

**[P-007] Best-of-Category — By Feature**
Score: Presence | Stage: Evaluation | Type: Best-of-Category | Intent: Explore | Priority: T1

TEMPLATE: `"Best [category] with [key capability]"`
EXAMPLE: "Best expense management platform with AI-powered receipt scanning"

> Feeds: Presence Rate (capability-qualified visibility)

**[P-008] Best-of-Category — By Budget**
Score: Presence | Stage: Evaluation | Type: Best-of-Category | Intent: Explore | Priority: T1

TEMPLATE: `"Best [category] under $[price point] per month"`
EXAMPLE: "Best project management tools under $20 per user per month"

> Feeds: Presence Rate (budget-segment visibility)

**[P-009] Best-of-Category — By Geography/Compliance**
Score: Presence | Stage: Evaluation | Type: Best-of-Category | Intent: Explore | Priority: T2

TEMPLATE: `"Best [category] for [geography/compliance requirement]"`
EXAMPLE: "Best CRM software for GDPR-compliant companies in Europe"

> Feeds: Presence Rate (regulatory-qualified visibility)

**[P-010] Best-of-Category — Time-Qualified**
Score: Presence | Stage: Evaluation | Type: Best-of-Category | Intent: Explore | Priority: T1

TEMPLATE: `"Best [category] tools [year]"`
EXAMPLE: "Best marketing automation platforms 2026"

> Feeds: Presence Rate (recency-filtered visibility)

**[P-011] Best-of-Category — Top-N**
Score: Presence | Stage: Evaluation | Type: Best-of-Category | Intent: Explore | Priority: T1

TEMPLATE: `"Top [N] [category] tools for [constraint]"`
EXAMPLE: "Top 5 expense management tools for Series B startups"

> Feeds: Presence Rate, Position (forced-ranking visibility)

**[P-012] Best-of-Category — Recommendation Request**
Score: Presence | Stage: Evaluation | Type: Best-of-Category | Intent: Compare | Priority: T1

TEMPLATE: `"What [category] should I evaluate?"`
EXAMPLE: "What CRM platforms should I evaluate for a 200-person company?"

> Feeds: Presence Rate, Position (open-ended recommendation)

---

### 2.2 Landscape / Market Map Patterns

These establish whether AI names the brand when mapping the competitive space. Lower direct conversion than Best-of-Category but important for narrative authority and market positioning.

**[P-013] Market Map — Main Players**
Score: Presence | Stage: Solution Exploration | Type: Landscape | Intent: Explore | Priority: T1

TEMPLATE: `"Who are the main players in [category]?"`
EXAMPLE: "Who are the main players in the marketing automation space?"

> Feeds: Presence Rate, Position

**[P-014] Market Map — Market Structure**
Score: Presence | Stage: Solution Exploration | Type: Landscape | Intent: Explore | Priority: T2

TEMPLATE: `"Map the [category] software market"`
EXAMPLE: "Map the expense management software market"

> Feeds: Presence Rate (market-narrative inclusion)

**[P-015] Market Map — Solution Types**
Score: Presence | Stage: Solution Exploration | Type: Landscape | Intent: Learn | Priority: T2

TEMPLATE: `"What types of [category] solutions exist?"`
EXAMPLE: "What types of CRM solutions exist?"

> Feeds: Presence Rate (category-association strength)

**[P-016] Market Map — Emerging Players**
Score: Presence | Stage: Solution Exploration | Type: Landscape | Intent: Explore | Priority: T2

TEMPLATE: `"Emerging players in [category]"`
EXAMPLE: "Emerging players in AI visibility monitoring"

> Feeds: Presence Rate (innovation-narrative inclusion)

**[P-017] Market Map — Competitive Landscape**
Score: Presence | Stage: Solution Exploration | Type: Landscape | Intent: Explore | Priority: T2

TEMPLATE: `"What's the competitive landscape for [category] in [year]?"`
EXAMPLE: "What's the competitive landscape for cloud backup in 2026?"

> Feeds: Presence Rate, Cross-Engine Coverage

---

### 2.3 Alternatives-To Patterns

The highest-conversion Presence patterns. These are buyers actively looking to switch or expand their shortlist. Your brand must NOT be in the prompt — you want to appear as the recommended alternative.

**[P-018] Alternatives — Standard**
Score: Presence | Stage: Evaluation | Type: Alternatives-To | Intent: Compare | Priority: T1

TEMPLATE: `"Alternatives to [Competitor]"`
EXAMPLE: "Alternatives to Salesforce"

> Feeds: Presence Rate (competitive displacement)

**[P-019] Alternatives — Use-Case Qualified**
Score: Presence | Stage: Evaluation | Type: Alternatives-To | Intent: Compare | Priority: T1

TEMPLATE: `"Best [Competitor] alternatives for [use case]"`
EXAMPLE: "Best Salesforce alternatives for small sales teams"

> Feeds: Presence Rate (segment-specific displacement)

**[P-020] Alternatives — Replacement Intent**
Score: Presence | Stage: Evaluation | Type: Alternatives-To | Intent: Compare | Priority: T1

TEMPLATE: `"What can I use instead of [Competitor]?"`
EXAMPLE: "What can I use instead of HubSpot for marketing automation?"

> Feeds: Presence Rate (active switching signal)

**[P-021] Alternatives — Constraint-Filtered**
Score: Presence | Stage: Evaluation | Type: Alternatives-To | Intent: Compare | Priority: T2

TEMPLATE: `"[Adjective] alternatives to [Competitor]"`
EXAMPLE: "Cheaper alternatives to Salesforce for startups"

> Feeds: Presence Rate (value-positioning displacement)

**[P-022] Alternatives — Architecture-Filtered**
Score: Presence | Stage: Evaluation | Type: Alternatives-To | Intent: Compare | Priority: T2

TEMPLATE: `"[Architecture/approach] alternatives to [Competitor]"`
EXAMPLE: "Cloud-native alternatives to on-premises backup tools"

> Feeds: Presence Rate (approach-displacement)

**[P-023] Alternatives — Category Migration**
Score: Presence | Stage: Evaluation | Type: Alternatives-To | Intent: Compare | Priority: T2

TEMPLATE: `"Modern alternatives to [legacy tool type]"`
EXAMPLE: "Modern alternatives to legacy expense management spreadsheets"

> Feeds: Presence Rate (category-migration visibility)

---

### 2.4 Unbranded Comparison Patterns

The brand name is absent but the prompt invites comparison and ranking. Critical for establishing competitive position without naming any specific brand.

**[P-024] Unbranded Comparison — Category**
Score: Presence | Stage: Evaluation | Type: Direct Comparison (unbranded) | Intent: Compare | Priority: T1

TEMPLATE: `"Compare the best [category] platforms"`
EXAMPLE: "Compare the best cloud backup platforms"

> Feeds: Presence Rate, Position

**[P-025] Unbranded Comparison — Use-Case**
Score: Presence | Stage: Evaluation | Type: Direct Comparison (unbranded) | Intent: Compare | Priority: T1

TEMPLATE: `"Compare [category] tools for [use case]"`
EXAMPLE: "Compare CRM tools for B2B SaaS sales teams"

> Feeds: Presence Rate, Position

**[P-026] Unbranded Comparison — Capability**
Score: Presence | Stage: Evaluation | Type: Direct Comparison (unbranded) | Intent: Compare | Priority: T1

TEMPLATE: `"Which [category] tools have the best [capability]?"`
EXAMPLE: "Which marketing automation tools have the best lead scoring?"

> Feeds: Presence Rate, Position (capability-leadership signal)

**[P-027] Unbranded Comparison — Ranking**
Score: Presence | Stage: Evaluation | Type: Direct Comparison (unbranded) | Intent: Compare | Priority: T1

TEMPLATE: `"Rank the best [category] options for [company type]"`
EXAMPLE: "Rank the best expense management options for enterprise companies"

> Feeds: Presence Rate, Position (forced-rank signal)

---

### 2.5 Problem Recognition / Early Presence Patterns

These are unbranded but pre-evaluation-stage. They build category association and early trust, but do NOT feed Presence in CheckThat's strict definition (which requires evaluation-stage intent). Track these at Tier 3 as leading indicators.

**[P-028] Problem Definition**
Score: Early Presence (Tier 3) | Stage: Problem Recognition | Type: Problem Definition | Intent: Learn | Priority: T3

TEMPLATE: `"What are the main challenges with [problem area] at [company type]?"`
EXAMPLE: "What are the main challenges with managing expenses at a growing startup?"

> Feeds: Category association, early trust signal

**[P-029] Category Education**
Score: Early Presence (Tier 3) | Stage: Problem Recognition | Type: Category Education | Intent: Learn | Priority: T3

TEMPLATE: `"What is [category] and why does it matter?"`
EXAMPLE: "What is AI visibility monitoring and why does it matter?"

> Feeds: Category-defining authority

**[P-030] Category Need**
Score: Early Presence (Tier 3) | Stage: Problem Recognition | Type: Category Education | Intent: Learn | Priority: T3

TEMPLATE: `"Do I need a [category] tool?"`
EXAMPLE: "Do I need a dedicated project management tool or is a spreadsheet enough?"

> Feeds: Category relevance association

**[P-031] Approach Comparison**
Score: Early Presence (Tier 3) | Stage: Solution Exploration | Type: Approach Comparison | Intent: Explore | Priority: T3

TEMPLATE: `"[Approach A] vs [Approach B] for [use case]"`
EXAMPLE: "Build vs buy for marketing automation"

> Feeds: Approach-level visibility

---

## Section 3: Perception Patterns — By Attribute

*All patterns in this section include the brand name. These measure what story AI tells about the brand, scored across six buyer-relevant attributes.*

*Each attribute is scored 0-10 by an LLM-as-judge that evaluates AI-generated responses against defined rubrics. When brand context is populated, each attribute also gains an accuracy dimension — comparing AI's narrative against the brand's stated truth.*

### Quick-Reference: Question Type to Attribute Mapping

| Question Type | Primary Attribute | Secondary Attribute |
|---------------|------------------|---------------------|
| Feature & Integration (what it does) | Capability | Innovation |
| Feature & Integration (ease of use) | Usability | — |
| Implementation & Migration | Usability | Support |
| Pricing & Cost | Value | — |
| ROI & Business Case | Value | Trust |
| Risk & Compliance | Trust | — |
| Review & Reputation | Trust | Support |
| Expert Opinion & Social Proof | Trust | Innovation |
| Direct Comparison (why choose us) | Innovation | Capability |
| Trend & Future | Innovation | — |
| How-To & Implementation | Support | Usability |

---

### 3.1 Capability Patterns

*"Does AI describe the brand as powerful and complete, or limited and narrow?"*
*Probes: features, scalability, integrations, AI/automation, product depth.*

**[P-032] Feature Validation**
Score: Perception (Capability) | Stage: Evaluation | Type: Feature & Integration | Intent: Validate | Priority: T1

TEMPLATE: `"Does [Brand] have [feature]?"`
EXAMPLE: "Does HubSpot have AI-powered lead scoring?"

> Feeds: Perception (Capability) — feature accuracy check

**[P-033] Feature Depth**
Score: Perception (Capability) | Stage: Evaluation | Type: Feature & Integration | Intent: Validate | Priority: T1

TEMPLATE: `"Does [Brand] support [specific capability]?"`
EXAMPLE: "Does Notion support real-time collaboration on databases?"

> Feeds: Perception (Capability) — depth-of-feature accuracy

**[P-034] Feature Comparison**
Score: Perception (Capability) + Presence | Stage: Evaluation | Type: Feature & Integration | Intent: Compare | Priority: T1

TEMPLATE: `"Which [category] tools have the best [capability]?"`
EXAMPLE: "Which CRM tools have the best email automation?"

> Feeds: Dual — Capability narrative + competitive visibility. Note: This is a borderline Presence pattern when your brand is not named. If branded ("Does [Brand] have the best [capability]?"), it's pure Perception.

**[P-035] Integration Check**
Score: Perception (Capability) | Stage: Evaluation | Type: Feature & Integration | Intent: Validate | Priority: T1

TEMPLATE: `"Does [Brand] integrate with [platform]?"`
EXAMPLE: "Does Ramp integrate with NetSuite?"

> Feeds: Perception (Capability) — integration accuracy

**[P-036] Integration Listing**
Score: Perception (Capability) | Stage: Evaluation | Type: Feature & Integration | Intent: Validate | Priority: T2

TEMPLATE: `"[Brand] integrations"`
EXAMPLE: "Monday.com integrations"

> Feeds: Perception (Capability) — integration breadth

**[P-037] Use-Case Fit**
Score: Perception (Capability) | Stage: Evaluation | Type: Feature & Integration | Intent: Compare | Priority: T1

TEMPLATE: `"Is [Brand] good for [specific use case]?"`
EXAMPLE: "Is Asana good for managing marketing campaigns?"

> Feeds: Perception (Capability) — use-case narrative

**[P-038] Scalability**
Score: Perception (Capability) | Stage: Decision | Type: Feature & Integration | Intent: Validate | Priority: T2

TEMPLATE: `"Can [Brand] handle [scale requirement]?"`
EXAMPLE: "Can Airtable handle 100,000+ records per base?"

> Feeds: Perception (Capability) — scalability narrative

**[P-039] API/Developer**
Score: Perception (Capability) | Stage: Evaluation | Type: Feature & Integration | Intent: Validate | Priority: T2

TEMPLATE: `"Does [Brand] have an API?" / "[Brand] API documentation"`
EXAMPLE: "Does Stripe have a webhook API for subscription events?"

> Feeds: Perception (Capability) — developer-readiness

**[P-040] Product Breadth**
Score: Perception (Capability) | Stage: Evaluation | Type: Feature & Integration | Intent: Validate | Priority: T2

TEMPLATE: `"What can [Brand] do?" / "[Brand] features overview"`
EXAMPLE: "What can Notion do beyond note-taking?"

> Feeds: Perception (Capability) — product narrative breadth

---

### 3.2 Usability Patterns

*"Does AI describe the brand as easy to use and fast to deploy, or painful to adopt?"*
*Probes: ease of use, implementation speed, onboarding, learning curve, UX quality.*

**[P-041] Ease of Use**
Score: Perception (Usability) | Stage: Evaluation | Type: Feature & Integration | Intent: Validate | Priority: T2

TEMPLATE: `"Is [Brand] easy to use?"`
EXAMPLE: "Is Salesforce easy to use for small teams?"

> Feeds: Perception (Usability) — ease-of-use narrative

**[P-042] Setup Time**
Score: Perception (Usability) | Stage: Decision | Type: Implementation & Migration | Intent: Validate | Priority: T2

TEMPLATE: `"How long does it take to set up [Brand]?"`
EXAMPLE: "How long does it take to set up HubSpot CRM?"

> Feeds: Perception (Usability) — time-to-value narrative

**[P-043] Onboarding Experience**
Score: Perception (Usability) | Stage: Decision | Type: Implementation & Migration | Intent: Validate | Priority: T2

TEMPLATE: `"What's the onboarding process like for [Brand]?"`
EXAMPLE: "What's the onboarding process like for Intercom?"

> Feeds: Perception (Usability) — onboarding narrative

**[P-044] Learning Curve**
Score: Perception (Usability) | Stage: Evaluation | Type: Feature & Integration | Intent: Validate | Priority: T2

TEMPLATE: `"What's the learning curve for [Brand]?"`
EXAMPLE: "What's the learning curve for Jira?"

> Feeds: Perception (Usability) — complexity narrative

**[P-045] Technical Requirements**
Score: Perception (Usability) | Stage: Decision | Type: Implementation & Migration | Intent: Validate | Priority: T2

TEMPLATE: `"Does [Brand] require [technical complexity]?"`
EXAMPLE: "Does Datadog require dedicated DevOps to maintain?"

> Feeds: Perception (Usability) — infrastructure burden narrative

**[P-046] Implementation Process**
Score: Perception (Usability) | Stage: Decision | Type: Implementation & Migration | Intent: Validate | Priority: T2

TEMPLATE: `"What does [Brand] implementation look like?"`
EXAMPLE: "What does Workday implementation look like for a mid-market company?"

> Feeds: Perception (Usability) — implementation narrative

**[P-047] Migration Path**
Score: Perception (Usability) | Stage: Decision | Type: Implementation & Migration | Intent: Act | Priority: T2

TEMPLATE: `"How do I migrate from [Current Tool] to [Brand]?"`
EXAMPLE: "How do I migrate from Asana to Monday.com?"

> Feeds: Perception (Usability) — migration difficulty narrative

**[P-048] Small Team Fit**
Score: Perception (Usability) | Stage: Evaluation | Type: Feature & Integration | Intent: Validate | Priority: T2

TEMPLATE: `"Can a small team manage [Brand]?"`
EXAMPLE: "Can a 3-person marketing team manage HubSpot?"

> Feeds: Perception (Usability) — team-size-appropriateness narrative

**[P-049] Comparative Usability**
Score: Perception (Usability) | Stage: Evaluation | Type: Direct Comparison | Intent: Compare | Priority: T2

TEMPLATE: `"Is [Brand] easier to use than [Competitor]?"`
EXAMPLE: "Is ClickUp easier to use than Jira?"

> Feeds: Perception (Usability) — comparative ease narrative

**[P-050] Deployment Speed**
Score: Perception (Usability) | Stage: Decision | Type: Implementation & Migration | Intent: Validate | Priority: T3

TEMPLATE: `"Can [Brand] be deployed in [timeframe]?"`
EXAMPLE: "Can Linear be deployed in a single day?"

> Feeds: Perception (Usability) — speed-to-value narrative

---

### 3.3 Value Patterns

*"Does AI position the brand as worth the money, or expensive?"*
*Probes: pricing, ROI, total cost of ownership, pricing transparency.*

**[P-051] Pricing — Direct**
Score: Perception (Value) | Stage: Evaluation | Type: Pricing & Cost | Intent: Validate | Priority: T1

TEMPLATE: `"[Brand] pricing"`
EXAMPLE: "Notion pricing"

> Feeds: Perception (Value) — pricing accuracy. Critical: if AI returns outdated or incorrect pricing, it eliminates brands from shortlists.

**[P-052] Pricing — Question Form**
Score: Perception (Value) | Stage: Evaluation | Type: Pricing & Cost | Intent: Validate | Priority: T1

TEMPLATE: `"How much does [Brand] cost?"`
EXAMPLE: "How much does Figma cost for a team of 20?"

> Feeds: Perception (Value) — pricing narrative

**[P-053] Pricing Model**
Score: Perception (Value) | Stage: Evaluation | Type: Pricing & Cost | Intent: Validate | Priority: T2

TEMPLATE: `"[Brand] pricing model"`
EXAMPLE: "Twilio pricing model — how does usage-based billing work?"

> Feeds: Perception (Value) — pricing structure accuracy

**[P-054] Pricing Comparison**
Score: Perception (Value) | Stage: Evaluation | Type: Pricing & Cost | Intent: Compare | Priority: T1

TEMPLATE: `"[Brand] vs [Competitor] pricing"`
EXAMPLE: "Slack vs Microsoft Teams pricing comparison"

> Feeds: Perception (Value) — comparative value narrative

**[P-055] Budget-Filtered**
Score: Perception (Value) + Presence | Stage: Evaluation | Type: Pricing & Cost | Intent: Compare | Priority: T2

TEMPLATE: `"Best [category] under $[price point] per month"`
EXAMPLE: "Best project management tools under $15 per user per month"

> Feeds: Dual — Value positioning + budget-segment Presence

**[P-056] Free Tier**
Score: Perception (Value) | Stage: Evaluation | Type: Pricing & Cost | Intent: Validate | Priority: T2

TEMPLATE: `"[Brand] free tier" / "Does [Brand] have a free plan?"`
EXAMPLE: "Does Notion have a free plan? What are the limitations?"

> Feeds: Perception (Value) — free tier accuracy

**[P-057] ROI**
Score: Perception (Value) | Stage: Decision | Type: ROI & Business Case | Intent: Validate | Priority: T2

TEMPLATE: `"What's the ROI of [Brand]?"`
EXAMPLE: "What's the ROI of investing in HubSpot Marketing Hub?"

> Feeds: Perception (Value) + Perception (Trust) — ROI narrative

**[P-058] Business Case**
Score: Perception (Value) | Stage: Decision | Type: ROI & Business Case | Intent: Validate | Priority: T2

TEMPLATE: `"How to justify [Brand/category] spend to leadership"`
EXAMPLE: "How to justify marketing automation spend to the CFO"

> Feeds: Perception (Value) — business-case narrative

**[P-059] Total Cost of Ownership**
Score: Perception (Value) | Stage: Decision | Type: Pricing & Cost | Intent: Compare | Priority: T2

TEMPLATE: `"Total cost of ownership for [Brand] vs [Competitor]"`
EXAMPLE: "Total cost of ownership for Salesforce vs HubSpot CRM"

> Feeds: Perception (Value) — TCO comparison narrative

**[P-060] Case Studies**
Score: Perception (Value) | Stage: Decision | Type: ROI & Business Case | Intent: Validate | Priority: T3

TEMPLATE: `"[Brand] case studies for [industry]"`
EXAMPLE: "Datadog case studies for fintech companies"

> Feeds: Perception (Value) + Perception (Trust) — evidence narrative

**[P-061] Cost Reduction**
Score: Perception (Value) | Stage: Decision | Type: ROI & Business Case | Intent: Validate | Priority: T2

TEMPLATE: `"How does [Brand] reduce [cost area]?"`
EXAMPLE: "How does Ramp reduce corporate spending waste?"

> Feeds: Perception (Value) — cost-saving narrative

---

### 3.4 Trust Patterns

*"Does AI describe the brand as safe, reliable, and credible?"*
*Probes: security, compliance, reliability, vendor stability, brand credibility.*

**[P-062] General Trust**
Score: Perception (Trust) | Stage: Evaluation | Type: Review & Reputation | Intent: Validate | Priority: T2

TEMPLATE: `"Is [Brand] trustworthy?" / "Is [Brand] reliable?"`
EXAMPLE: "Is Monday.com reliable for enterprise project management?"

> Feeds: Perception (Trust) — trust narrative

**[P-063] Security**
Score: Perception (Trust) | Stage: Decision | Type: Risk & Compliance | Intent: Validate | Priority: T1

TEMPLATE: `"Is [Brand] SOC2 compliant?" / "[Brand] security"`
EXAMPLE: "Is Notion SOC2 Type II compliant?"

> Feeds: Perception (Trust) — security accuracy. Critical for regulated industries.

**[P-064] Compliance Standards**
Score: Perception (Trust) | Stage: Decision | Type: Risk & Compliance | Intent: Validate | Priority: T1

TEMPLATE: `"Is [Brand] [compliance standard] compliant?"`
EXAMPLE: "Is Stripe HIPAA compliant?"

> Feeds: Perception (Trust) — compliance accuracy

**[P-065] Data Privacy**
Score: Perception (Trust) | Stage: Decision | Type: Risk & Compliance | Intent: Validate | Priority: T2

TEMPLATE: `"[Brand] data privacy policy"`
EXAMPLE: "Zoom data privacy policy — where is data stored?"

> Feeds: Perception (Trust) — privacy narrative

**[P-066] Uptime/Reliability**
Score: Perception (Trust) | Stage: Decision | Type: Risk & Compliance | Intent: Validate | Priority: T2

TEMPLATE: `"[Brand] uptime and reliability"`
EXAMPLE: "Slack uptime and reliability history"

> Feeds: Perception (Trust) — reliability narrative

**[P-067] Vendor Stability**
Score: Perception (Trust) | Stage: Decision | Type: Risk & Compliance | Intent: Validate | Priority: T2

TEMPLATE: `"Is [Brand] enterprise-ready?" / "How established is [Brand]?"`
EXAMPLE: "Is Linear enterprise-ready or still a startup tool?"

> Feeds: Perception (Trust) — vendor stability narrative

**[P-068] Reviews**
Score: Perception (Trust) | Stage: Evaluation | Type: Review & Reputation | Intent: Validate | Priority: T1

TEMPLATE: `"[Brand] reviews [year]"`
EXAMPLE: "Asana reviews 2026"

> Feeds: Perception (Trust) + Perception (Support) — review-sourced narrative

**[P-069] Pros and Cons**
Score: Perception (Trust) | Stage: Evaluation | Type: Review & Reputation | Intent: Validate | Priority: T1

TEMPLATE: `"[Brand] pros and cons"`
EXAMPLE: "Jira pros and cons"

> Feeds: Perception (Trust) — balanced evaluation narrative

**[P-070] Complaints/Problems**
Score: Perception (Trust) | Stage: Evaluation | Type: Review & Reputation | Intent: Validate | Priority: T2

TEMPLATE: `"[Brand] customer complaints" / "[Brand] problems"`
EXAMPLE: "Salesforce customer complaints 2026"

> Feeds: Perception (Trust) — negative narrative monitoring

**[P-071] Downsides**
Score: Perception (Trust) | Stage: Evaluation | Type: Review & Reputation | Intent: Validate | Priority: T2

TEMPLATE: `"What are the downsides of [Brand]?"`
EXAMPLE: "What are the downsides of using Notion for project management?"

> Feeds: Perception (Trust) — weakness narrative

**[P-072] Social Proof**
Score: Perception (Trust) | Stage: Decision | Type: Expert Opinion & Social Proof | Intent: Validate | Priority: T2

TEMPLATE: `"What do customers say about [Brand]?"`
EXAMPLE: "What do customers say about Intercom's support quality?"

> Feeds: Perception (Trust) — customer-voice narrative

**[P-073] Analyst Coverage**
Score: Perception (Trust) | Stage: Decision | Type: Expert Opinion & Social Proof | Intent: Validate | Priority: T2

TEMPLATE: `"What do analysts say about [Brand]?"`
EXAMPLE: "What does Gartner say about Snowflake?"

> Feeds: Perception (Trust) + Perception (Innovation) — analyst narrative

**[P-074] Community Opinion**
Score: Perception (Trust) | Stage: Decision | Type: Expert Opinion & Social Proof | Intent: Validate | Priority: T2

TEMPLATE: `"[Brand] on Reddit" / "What does Reddit say about [Brand]?"`
EXAMPLE: "What does Reddit say about ClickUp vs Notion?"

> Feeds: Perception (Trust) — community narrative. Reddit is cited in 40%+ of Perplexity responses.

---

### 3.5 Support Patterns

*"Does AI describe the brand's support as responsive and helpful?"*
*Probes: customer support quality, documentation, success management, onboarding help.*

**[P-075] Support Quality**
Score: Perception (Support) | Stage: Evaluation | Type: Review & Reputation | Intent: Validate | Priority: T2

TEMPLATE: `"How is [Brand]'s customer support?"`
EXAMPLE: "How is Zendesk's customer support?"

> Feeds: Perception (Support) — support quality narrative

**[P-076] Responsiveness**
Score: Perception (Support) | Stage: Evaluation | Type: Review & Reputation | Intent: Validate | Priority: T3

TEMPLATE: `"Is [Brand] responsive when you have issues?"`
EXAMPLE: "Is AWS responsive when you have billing issues?"

> Feeds: Perception (Support) — responsiveness narrative

**[P-077] Documentation Quality**
Score: Perception (Support) | Stage: Post-Purchase | Type: How-To & Implementation | Intent: Validate | Priority: T2

TEMPLATE: `"[Brand] documentation quality"`
EXAMPLE: "Stripe documentation quality — is it developer-friendly?"

> Feeds: Perception (Support) — documentation narrative

**[P-078] Help Resources**
Score: Perception (Support) | Stage: Post-Purchase | Type: How-To & Implementation | Intent: Validate | Priority: T3

TEMPLATE: `"Does [Brand] have good help resources?"`
EXAMPLE: "Does Figma have good tutorials and learning resources?"

> Feeds: Perception (Support) — self-service support narrative

**[P-079] Community Support**
Score: Perception (Support) | Stage: Post-Purchase | Type: How-To & Implementation | Intent: Validate | Priority: T3

TEMPLATE: `"Does [Brand] have an active community?"`
EXAMPLE: "Does Tailwind CSS have an active community for help?"

> Feeds: Perception (Support) — community-support narrative

**[P-080] Comparative Support**
Score: Perception (Support) | Stage: Evaluation | Type: Review & Reputation | Intent: Compare | Priority: T3

TEMPLATE: `"[Brand] support vs [Competitor] support"`
EXAMPLE: "HubSpot support vs Salesforce support — which is more responsive?"

> Feeds: Perception (Support) — comparative support narrative

**[P-081] Onboarding Support**
Score: Perception (Support) | Stage: Decision | Type: Implementation & Migration | Intent: Validate | Priority: T2

TEMPLATE: `"Does [Brand] provide onboarding support?"`
EXAMPLE: "Does Amplitude provide onboarding support for new customers?"

> Feeds: Perception (Support) + Perception (Usability) — onboarding support narrative

---

### 3.6 Innovation Patterns

*"Does AI describe the brand as forward-thinking and differentiated, or stagnant?"*
*Probes: product vision, roadmap, differentiation, competitive uniqueness.*

**[P-082] Differentiation**
Score: Perception (Innovation) | Stage: Evaluation | Type: Direct Comparison | Intent: Compare | Priority: T1

TEMPLATE: `"What makes [Brand] different from other [category] tools?"`
EXAMPLE: "What makes Linear different from other project management tools?"

> Feeds: Perception (Innovation) — differentiation narrative

**[P-083] Competitive Advantage**
Score: Perception (Innovation) | Stage: Evaluation | Type: Direct Comparison | Intent: Compare | Priority: T1

TEMPLATE: `"Why would I choose [Brand] over [Competitor]?"`
EXAMPLE: "Why would I choose Notion over Confluence?"

> Feeds: Perception (Innovation) + Perception (Capability) — competitive narrative

**[P-084] Uniqueness**
Score: Perception (Innovation) | Stage: Evaluation | Type: Direct Comparison | Intent: Compare | Priority: T2

TEMPLATE: `"What's unique about [Brand]?"`
EXAMPLE: "What's unique about Figma compared to other design tools?"

> Feeds: Perception (Innovation) — uniqueness narrative

**[P-085] Growth Trajectory**
Score: Perception (Innovation) | Stage: Decision | Type: Trend & Future | Intent: Validate | Priority: T2

TEMPLATE: `"Is [Brand] growing?"`
EXAMPLE: "Is Vercel growing? What's their trajectory?"

> Feeds: Perception (Innovation) — momentum narrative

**[P-086] Vision**
Score: Perception (Innovation) | Stage: Decision | Type: Trend & Future | Intent: Validate | Priority: T3

TEMPLATE: `"What is [Brand]'s long-term vision?"`
EXAMPLE: "What is Notion's long-term product vision?"

> Feeds: Perception (Innovation) — vision narrative

**[P-087] Category Leadership**
Score: Perception (Innovation) | Stage: Evaluation | Type: Trend & Future | Intent: Validate | Priority: T2

TEMPLATE: `"Is [Brand] a leader in [category]?"`
EXAMPLE: "Is Datadog a leader in observability?"

> Feeds: Perception (Innovation) — leadership narrative

**[P-088] Innovation Recognition**
Score: Perception (Innovation) + Presence | Stage: Evaluation | Type: Trend & Future | Intent: Explore | Priority: T2

TEMPLATE: `"Which [category] companies are most innovative?"`
EXAMPLE: "Which DevOps companies are most innovative in 2026?"

> Feeds: Dual — Innovation narrative + competitive Presence

**[P-089] Future/Trends**
Score: Perception (Innovation) | Stage: Post-Purchase | Type: Trend & Future | Intent: Learn | Priority: T3

TEMPLATE: `"Is [Brand/category] the future of [domain]?"`
EXAMPLE: "Is AI-native CRM the future of sales technology?"

> Feeds: Perception (Innovation) — trajectory narrative

**[P-090] Category Creation**
Score: Perception (Innovation) | Stage: Any | Type: Trend & Future | Intent: Learn | Priority: T2

TEMPLATE: `"What is [Brand's proprietary concept]?" / "Who created [concept]?"`
EXAMPLE: "What is Cloud Backup Posture Management? Who coined the term?"

> Feeds: Perception (Innovation) — category-creation authority

**[P-091] Category Trends**
Score: Perception (Innovation) | Stage: Post-Purchase | Type: Trend & Future | Intent: Learn | Priority: T3

TEMPLATE: `"[Category] trends [year]"`
EXAMPLE: "Marketing automation trends 2026"

> Feeds: Perception (Innovation) — trend-association narrative

---

## Section 4: Branded Comparison Patterns (Presence + Perception)

*These are dual-measurement patterns. The brand name appears in the prompt AND the response reveals competitive positioning. They feed Perception (how AI characterizes your brand) AND can surface Presence signals (which competitors AI recommends alongside or above you).*

*These are among the highest-intent, highest-conversion prompts in any library.*

### 4.1 Head-to-Head Comparison Patterns

**[P-092] Direct Head-to-Head**
Score: Presence + Perception | Stage: Evaluation | Type: Direct Comparison | Intent: Compare | Priority: T1

TEMPLATE: `"[Brand] vs [Competitor]"`
EXAMPLE: "HubSpot vs Salesforce"

> Feeds: Perception (all attributes surfaced in the comparison) + competitive positioning

**[P-093] Use-Case Comparison**
Score: Presence + Perception | Stage: Evaluation | Type: Direct Comparison | Intent: Compare | Priority: T1

TEMPLATE: `"[Brand] vs [Competitor] for [use case]"`
EXAMPLE: "Notion vs Confluence for engineering documentation"

> Feeds: Perception (Capability, Usability) + segment-specific competitive positioning

**[P-094] Size-Qualified Comparison**
Score: Presence + Perception | Stage: Evaluation | Type: Direct Comparison | Intent: Compare | Priority: T1

TEMPLATE: `"[Brand] vs [Competitor] for [company size]"`
EXAMPLE: "Ramp vs Brex for Series A startups"

> Feeds: Perception (Value, Usability) + size-segment competitive positioning

**[P-095] Multi-Vendor Comparison**
Score: Presence + Perception | Stage: Evaluation | Type: Direct Comparison | Intent: Compare | Priority: T1

TEMPLATE: `"Compare [Brand], [Competitor A], and [Competitor B]"`
EXAMPLE: "Compare Asana, Monday.com, and ClickUp for marketing teams"

> Feeds: Perception (all attributes) + multi-way competitive positioning

**[P-096] Conditional Choice**
Score: Presence + Perception | Stage: Evaluation | Type: Direct Comparison | Intent: Compare | Priority: T2

TEMPLATE: `"When should I choose [Brand] instead of [Competitor]?"`
EXAMPLE: "When should I choose Linear instead of Jira?"

> Feeds: Perception (Innovation, Capability) — conditional recommendation narrative

**[P-097] Conditional Choice (Inverse)**
Score: Presence + Perception | Stage: Evaluation | Type: Direct Comparison | Intent: Compare | Priority: T2

TEMPLATE: `"When would [Competitor] be better than [Brand]?"`
EXAMPLE: "When would Salesforce be better than HubSpot?"

> Feeds: Perception (all attributes) — inverse recommendation narrative. Important for understanding where AI positions your weaknesses.

**[P-098] Fit Question**
Score: Presence + Perception | Stage: Evaluation | Type: Direct Comparison | Intent: Compare | Priority: T2

TEMPLATE: `"What type of company benefits most from [Brand]?"`
EXAMPLE: "What type of company benefits most from Figma?"

> Feeds: Perception (Capability, Value) — ideal customer narrative

**[P-099] Pricing Comparison**
Score: Presence + Perception (Value) | Stage: Evaluation | Type: Pricing & Cost | Intent: Compare | Priority: T1

TEMPLATE: `"[Brand] vs [Competitor] pricing comparison"`
EXAMPLE: "Slack vs Microsoft Teams pricing comparison"

> Feeds: Perception (Value) + competitive value positioning

### 4.2 Competitive Position Patterns

**[P-100] Ranking Context**
Score: Presence + Perception | Stage: Evaluation | Type: Direct Comparison | Intent: Compare | Priority: T2

TEMPLATE: `"Is [Brand] better than [Competitor] for [use case]?"`
EXAMPLE: "Is Datadog better than New Relic for Kubernetes monitoring?"

> Feeds: Perception (Capability) + competitive ranking

**[P-101] Segment Fit**
Score: Presence + Perception | Stage: Evaluation | Type: Direct Comparison | Intent: Compare | Priority: T2

TEMPLATE: `"Is [Brand] better for [segment A] or [segment B]?"`
EXAMPLE: "Is HubSpot better for startups or enterprise?"

> Feeds: Perception (Value, Capability) — segment-fit narrative

**[P-102] Limitation Scope**
Score: Perception | Stage: Decision | Type: Review & Reputation | Intent: Validate | Priority: T2

TEMPLATE: `"When does [Brand] not make sense?"`
EXAMPLE: "When does Notion not make sense as a project management tool?"

> Feeds: Perception (Capability, Value) — limitation narrative

---

## Section 5: Reputation-Feeding Signal Patterns

*Reputation is the INPUT score — raw material AI learns from, measured independent of what AI says. You can't directly "prompt" for Reputation. But you can monitor which external signals are shaping AI's narrative about you, and build signals in the right places.*

*This section defines monitoring patterns (what to watch in AI responses) paired with content actions (what to build or fix).*

### 5.1 Review Platform Signals

**Signal source:** G2 (8.25% of ChatGPT evaluation citations), Capterra, TrustRadius, Gartner Peer Insights

**What to monitor in AI responses:**
- When AI cites review scores, check which platform it pulls from
- When AI says "users report..." or "according to reviews...", track the source
- Watch for outdated review data being cited (common with Capterra)

**Diagnostic prompts to run (branded):**
- `"[Brand] reviews"` — what source does AI cite?
- `"[Brand] G2 rating"` — is the rating accurate and current?
- `"[Brand] customer satisfaction"` — what narrative does AI construct?

**Content actions:**
| Signal gap | Action |
|-----------|--------|
| AI cites outdated review score | Update G2 profile, push for fresh reviews |
| AI cites Capterra but not G2 | Prioritize G2 review generation (higher citation rate) |
| AI says "mixed reviews" | Investigate specific criticism themes, respond to reviews |
| No review data cited at all | Build active review program across G2, Capterra, TrustRadius |

### 5.2 Community Signals

**Signal source:** Reddit (40%+ of Perplexity citations, top-10 most-cited domain across all engines), LinkedIn, forums

**What to monitor in AI responses:**
- When AI says "Reddit users recommend..." — track which subreddits
- When AI surfaces specific community sentiment — track positive vs negative
- Watch for old Reddit threads being cited over newer, more accurate ones

**Diagnostic prompts to run (branded):**
- `"[Brand] Reddit"` / `"What does Reddit say about [Brand]?"` — what threads surface?
- `"[Brand] community"` — does AI associate the brand with an active community?
- `"[Competitor] Reddit complaints"` — how does competitor sentiment compare?

**Content actions:**
| Signal gap | Action |
|-----------|--------|
| Negative Reddit threads dominating AI responses | Authentic engagement in subreddits; don't astroturf — participate genuinely |
| No Reddit presence at all | Start consistent, weekly participation in 3-5 relevant subreddits |
| Old threads cited over newer reality | Create fresh discussion threads with updated context |
| Strong competitor Reddit presence | Monitor competitor subreddits; participate where appropriate |

### 5.3 Authority/Press Signals

**Signal source:** Wikipedia (12.1% of ChatGPT citations overall), analyst firms (Gartner, Forrester), press/media, industry publications

**What to monitor in AI responses:**
- When AI cites Wikipedia for brand facts — check accuracy
- When AI references analyst rankings — verify currency
- When AI says "according to [publication]..." — track the source

**Diagnostic prompts to run (branded):**
- `"What is [Brand]?"` — does AI pull from Wikipedia? Is the info correct?
- `"[Brand] Gartner"` — what analyst narrative surfaces?
- `"[Category] industry reports"` — is the brand mentioned in analyst context?

**Content actions:**
| Signal gap | Action |
|-----------|--------|
| Wikipedia page missing or outdated | If notable enough, create/update Wikipedia page with accurate facts |
| AI cites incorrect founding year/HQ/size | Update Wikipedia and all web-indexed brand pages |
| No analyst coverage cited | Build analyst relationships; pursue inclusion in relevant reports |
| Press coverage not surfacing in AI | Ensure press releases are indexed; structured data on news pages |
| Third-party mentions low (85% of brand mentions come from third parties) | Invest in PR, guest posts, podcast appearances, partnerships |

---

## Section 6: Advanced Prompt Structures

*These techniques are orthogonal to Sections 2-4. They can be applied to any pattern to deepen the signal.*

### 6.1 Persona-Injected Patterns

Adding buyer context to the beginning of a prompt changes what AI recommends. The same question from a startup founder and an enterprise CTO gets different answers.

**The Variable Stack (ranked by impact on AI response):**

1. **Title/Role** — Most impactful. Determines complexity level and focus area.
2. **Company size** — Revenue or headcount. Determines scale of recommendation.
3. **Current tools** — What they already use. Determines integration recommendations.
4. **Specific pain point** — What's not working. Determines which features get highlighted.
5. **Budget stage** — "Exploring" vs "ready to buy." Determines how actionable the response is.
6. **Timeline** — When they need it. Determines urgency framing.

**Five Canonical Persona Templates:**

**[P-103] CMO / VP Marketing Persona**
Score: Any | Stage: Any | Priority: High for enterprise tracking

TEMPLATE:
```
"I'm a [VP of Marketing / CMO] at a [company size]-person [industry] company
([revenue range] ARR). My team is [team size] people. We use [current tools].
[Specific pain point]. [Question]."
```
EXAMPLE: "I'm a VP of Marketing at a 200-person B2B SaaS company ($50M ARR). My team is 12 people. We use HubSpot and Semrush. We're seeing declining organic traffic from AI search and need to understand our AI visibility. What AEO tools should I evaluate?"

**[P-104] CTO / Technical Leader Persona**
Score: Any | Stage: Any | Priority: High for technical products

TEMPLATE:
```
"I'm the [CTO / VP Engineering] at a [company size]-person [industry] company.
Our stack includes [tech stack]. We need [technical requirement].
Security and compliance are [priority level]. [Question]."
```
EXAMPLE: "I'm the CTO at a 150-person fintech company. Our stack includes AWS, Kubernetes, and PostgreSQL. We need automated cloud backup with cross-region replication. Security and compliance are critical — we need SOC2 and PCI DSS. What backup platforms should I evaluate?"

**[P-105] CFO / Financial Decision-Maker Persona**
Score: Any | Stage: Decision | Priority: High for ROI-sensitive products

TEMPLATE:
```
"I'm the [CFO / Head of Finance] at a [company size]-person company
([revenue range]). We spend [budget] annually on [category].
I need to understand [ROI / TCO / cost comparison]. [Question]."
```
EXAMPLE: "I'm the CFO at a 500-person company ($80M ARR). We spend $120K annually on marketing tools. I need to understand total cost of ownership for consolidating onto HubSpot vs keeping our current stack. What should I consider?"

**[P-106] Founder / CEO Persona**
Score: Any | Stage: Solution Exploration | Priority: High for startup-focused products

TEMPLATE:
```
"I'm the [founder / CEO] of a [stage]-stage [industry] startup.
We have [team size] people and [funding level] in funding.
I'm trying to figure out [strategic question]. [Question]."
```
EXAMPLE: "I'm the founder of a seed-stage B2B SaaS startup. We have 8 people and $3M in funding. I'm trying to figure out whether to invest in marketing automation now or wait until we have product-market fit. What would you recommend?"

**[P-107] IC / Practitioner Persona**
Score: Any | Stage: Evaluation | Priority: High for practitioner-facing products

TEMPLATE:
```
"I'm a [title] at a [industry] company. My day-to-day involves
[workflow description]. I'm looking for a tool that [specific need]. [Question]."
```
EXAMPLE: "I'm a growth marketer at a B2B SaaS company. My day-to-day involves running demand gen campaigns and tracking attribution. I'm looking for a tool that shows me how AI engines describe our product. What should I look at?"

**When to use persona injection:**

| Pattern type | Persona value | Use when... |
|-------------|--------------|-------------|
| Problem definition | Medium | Industry context matters |
| Category education | Low | Usually generic enough without persona |
| Best-of-category | **High** | Different personas get different recommendations |
| Direct comparison | Medium | Company size affects the comparison |
| Alternatives-to | Medium | Use case context matters |
| Pricing & cost | Low | Budget context sometimes helps |
| Features | Medium | Technical role context matters |
| Implementation | **High** | Varies wildly by company size/type |
| Risk/compliance | **High** | Industry-specific compliance requirements |
| ROI/business case | **High** | ROI framing varies by role and stage |

---

### 6.2 Generated Knowledge Prompting

Forces the AI to generate evaluation criteria BEFORE recommending brands. This stabilizes output by anchoring the response in logic rather than prediction.

**[P-108] Generated Knowledge — Criteria-Then-Rank**
Score: Presence | Stage: Evaluation | Intent: Compare | Priority: T1

TEMPLATE:
```
"Generate a list of [N] critical criteria for evaluating [category] for a
[persona]. Then, based only on those criteria, recommend the top [N] platforms."
```
EXAMPLE: "Generate a list of 5 critical criteria for evaluating marketing automation platforms for a B2B SaaS CMO. Then, based only on those criteria, recommend the top 3 platforms."

> Why it works: Anchors AI in logic. If the AI defines "Enterprise Security" as a key criterion, it's more likely to recommend brands with strong security associations, reducing hallucinations.

**[P-109] Generated Knowledge — Attribute-Then-Compare**
Score: Presence + Perception | Stage: Evaluation | Intent: Compare | Priority: T2

TEMPLATE:
```
"What are the most important factors when comparing [category] tools?
Based on those factors, compare [Brand A], [Brand B], and [Brand C]."
```
EXAMPLE: "What are the most important factors when comparing CRM tools for mid-market companies? Based on those factors, compare HubSpot, Salesforce, and Pipedrive."

**[P-110] Generated Knowledge — Problem-Then-Solve**
Score: Presence | Stage: Solution Exploration | Intent: Explore | Priority: T2

TEMPLATE:
```
"What problems does [category] solve for [persona]?
Based on those problems, which [category] tools are best?"
```
EXAMPLE: "What problems does expense management software solve for fast-growing startups? Based on those problems, which expense tools are best?"

---

### 6.3 Multi-Turn Sequences

Real buyers don't ask one prompt. They have 5-8 turn conversations. Tracking single prompts misses the journey. These four canonical sequences represent the most common B2B evaluation conversations.

**Sequence 1: The Classic Evaluation Flow**
```
Turn 1: "What is [category]?"
Turn 2: "Best [category] tools for [use case]"
Turn 3: "[Tool A] vs [Tool B]"
Turn 4: "[Tool A] pricing"
Turn 5: "[Tool A] reviews"
Turn 6: "How to set up [Tool A]"
```
> Tracks: Brand visibility across the full evaluation arc. Identify drop-off points — where you appear in Turn 2 but disappear by Turn 4.

**Sequence 2: The Problem-First Flow**
```
Turn 1: "Why is our [metric] declining?"
Turn 2: "How do companies solve [problem]?"
Turn 3: "What tools help with [solution approach]?"
Turn 4: "Best [category] for [our situation]"
Turn 5: "Compare [top 3 recommendations]"
Turn 6: "Should we buy [Tool A]?"
```
> Tracks: Whether AI connects the brand to the problem. Brands that appear by Turn 3 have strong problem-association. Brands that only appear at Turn 5 are commoditized.

**Sequence 3: The Competitive Switch Flow**
```
Turn 1: "[Current tool] alternatives"
Turn 2: "Why are companies leaving [current tool]?"
Turn 3: "[Current tool] vs [Alternative A] vs [Alternative B]"
Turn 4: "How hard is it to migrate from [current tool] to [alternative]?"
Turn 5: "[Alternative] pricing for [our size]"
Turn 6: "[Alternative] implementation timeline"
```
> Tracks: Whether AI recommends you as a switch candidate and sustains recommendation through decision validation.

**Sequence 4: The Persona-Driven Deep Dive**
```
Turn 1: "I'm a [persona]. I need help with [problem]."
Turn 2: "Which of those options works best for [constraint]?"
Turn 3: "Tell me more about [recommended tool]"
Turn 4: "What are the downsides of [recommended tool]?"
Turn 5: "How does [recommended tool] compare to [alternative]?"
Turn 6: "What would implementation look like for a company like mine?"
```
> Tracks: AI's full recommendation journey from persona match to implementation. If AI recommends you at Turn 1 but switches at Turn 4, your weakness narrative is stronger than your strength narrative.

---

### 6.4 Cluster Design

The Law of Sensitivity: a synonym change can shift results by 10-78%. A single prompt is unreliable. Build clusters of 3-5 semantically similar prompts per pattern to get a true signal.

**How to build a cluster:**

1. Start with the base pattern
2. Generate 2 synonymic variations (replace key nouns/verbs with synonyms)
3. Generate 1 context variation (add or change one constraint)
4. Generate 1 format variation (question form vs declarative)

**Example cluster for P-001 (Best-of-Category — Core):**
```
1. "Best expense management tools for mid-market companies"        [base]
2. "Top expense management software for mid-market organizations"  [synonymic]
3. "Leading expense management platforms for mid-market"           [synonymic]
4. "Best expense management tools for 200-500 person companies"    [context variation]
5. "What expense management tool should a mid-market company use?" [format variation]
```

**Reporting from clusters:** Report the percentage across all runs of all cluster members. Example: "We appear in 65% of runs across the Best-of-Category cluster (N=150 total runs across 5 prompts)."

---

## Section 7: Context Variables Matrix

*Any pattern from Sections 2-4 can be multiplied across context variables. This is how 100 patterns become a 10,000+ prompt library.*

### 7.1 The Eight Dimensions

| # | Dimension | What it captures | Example values |
|---|-----------|-----------------|----------------|
| 1 | **Industry Vertical** | Buyer's business domain | Healthcare, FinTech, SaaS, Manufacturing, Legal, Education, Government, Retail, Real Estate |
| 2 | **Company Size** | Scale and complexity | Startup (1-50), SMB (50-200), Mid-market (200-1000), Enterprise (1000+) |
| 3 | **Buyer Role / Persona** | Who is asking | CMO, VP Marketing, Head of Growth, CTO, CFO, Procurement, Founder, IC Marketer |
| 4 | **Use Case** | Specific problem or workflow | Varies by category (e.g., lead scoring, expense tracking, incident management) |
| 5 | **Geographic / Regulatory** | Location constraints | US, EU/GDPR, UK, APAC, specific country regulatory requirements |
| 6 | **Tech Stack / Integration** | Current tools and platforms | HubSpot, Salesforce, Semrush, GA4, Slack, AWS, custom integrations |
| 7 | **Budget** | Price sensitivity | Free, under $100/mo, $100-500/mo, $500-2K/mo, enterprise budget |
| 8 | **Timeline / Urgency** | How fast they need to act | Immediate, this quarter, planning for next year, exploring |

### 7.2 Combinatorial Generation

Take any pattern and cross with relevant variables:

**Pattern P-003:** `"Best [category] for [industry]"`

**Generated prompts:**
```
By industry:
  "Best marketing automation for healthcare companies"
  "Best marketing automation for fintech startups"
  "Best marketing automation for B2B SaaS"
  "Best marketing automation for manufacturing"

By company size:
  "Best marketing automation for startups"
  "Best marketing automation for enterprise"
  "Best marketing automation for mid-market companies"

Combined:
  "Best marketing automation for a Series B SaaS company under $500/month"
  "Best marketing automation for healthcare mid-market companies using HubSpot"
```

**The math:** For a single category: 16 question types x 9 industries x 4 company sizes x 8 buyer roles = **23,040 possible prompts**. Most combinations aren't meaningful. Use the quality filter below.

### 7.3 The "Would a Buyer Say This?" Test

Before adding any generated prompt to the library:

1. **Is this how a human talks?** — "Best CRM for mid-market B2B SaaS companies in the healthcare vertical with Salesforce integration requirements" is not how humans talk. "I need a CRM that works with Salesforce for our healthcare startup — what are my options?" is.

2. **Does this reflect a real buying moment?** — "Compare the API documentation quality of Brand A vs Brand B" might be real for developer tools. For marketing software, probably not.

3. **Would this prompt appear in a sales discovery call?** — If a prospect wouldn't ask this to a sales rep, it's probably not worth tracking.

### 7.4 Prompt Quality Scoring

Rate each prompt 1-5 on five dimensions:

| Dimension | Score 1 (Low) | Score 5 (High) |
|-----------|--------------|-----------------|
| **Buyer Realism** | Nobody would actually ask this | Verbatim from sales call transcripts |
| **Commercial Intent** | Pure information, no buying signal | Active purchase decision |
| **Brand Differentiation** | Every competitor shows up the same way | Clear winners and losers in AI response |
| **Actionable Signal** | Response is generic, nothing to optimize | Clear gaps you can close with content |
| **Volume Proxy** | Niche query, low search volume equivalent | High-volume search term equivalent |

**Priority Tiers:**
- **Tier 1 (20-25):** Track weekly, immediate content action on gaps
- **Tier 2 (15-19):** Track weekly, queue content work
- **Tier 3 (10-14):** Track bi-weekly, monitor
- **Tier 4 (<10):** Deprioritize or remove

### 7.5 Sources for High-Quality Prompts

Ranked by quality:

| Source | Quality | What to extract |
|--------|---------|----------------|
| **Sales call transcripts** | Highest | Exact questions prospects ask during discovery and evaluation |
| **Customer support tickets** | High | Post-sale questions that mirror pre-sale evaluation |
| **Reddit threads** | High | Raw, unfiltered buyer language (cited in 40%+ of Perplexity responses) |
| **G2 / Capterra reviews** | High | How buyers describe products in their own words |
| **LinkedIn discussions** | Medium-High | How professionals frame comparisons and debates |
| **Quora threads** | Medium | Longer-form questions with more context |
| **Search Console data** | Medium | Query patterns from people already finding you |
| **Competitor content** | Medium | What questions competitors are answering |
| **Internal brainstorming** | Low-Medium | Good for coverage but often doesn't match buyer language |

### 7.6 Starting Volume by Maturity

| Stage | Prompt count | Focus |
|-------|-------------|-------|
| **Just starting** | 50-100 | Top 3 competitors, primary use case, evaluation stage only |
| **Growing program** | 200-500 | Add personas, industries, expand to all funnel stages |
| **Mature program** | 500-2,000 | Full matrix coverage, persona-injected variants, multi-language |
| **Enterprise** | 2,000+ | Multi-region, multi-product line, competitive intelligence |

---

## Section 8: Engine-Specific Dialect Guide

Each AI engine processes prompts differently. The same pattern may need slight adaptation per engine for optimal signal.

### 8.1 ChatGPT

**Dialect:** Conversational and contextual. Loves personas and back-and-forth.
**Market share:** 87.4% of AI referral traffic, 800M+ weekly active users.
**Source bias:** Heavy Wikipedia reliance (12.1% of citations). Strong UGC presence (Reddit, LinkedIn, Medium).

**Best for:** Persona-injected prompts, Generated Knowledge Prompting, multi-turn sequences.
**Adaptation:** Add conversational context. Instead of `"Best CRM tools"`, use `"My company is a 50-person SaaS startup. We need a CRM that integrates with HubSpot. What are our options?"`

### 8.2 Perplexity

**Dialect:** Search-first and fact-based. Loves specific, search-query-style questions.
**Source bias:** Favors Reddit (40%+ of citations), recent articles, academic sources. Strong recency preference.

**Best for:** Specific feature queries, review-based queries, Reddit-signal prompts.
**Adaptation:** Add specificity and recency markers. Instead of `"Best CRM tools"`, use `"Best CRM software 2026 reddit"` or `"[Brand] vs [Competitor] 2026"`. Include year or "reddit" when relevant.

### 8.3 Claude

**Dialect:** Analytical and cautious. Frames recommendations as analysis rather than advice.
**Source bias:** Careful about source quality. Growing 8-10x faster than ChatGPT. Developer and technical buyer focus.

**Best for:** Framework-driven comparison prompts, market map prompts, analytical assessments.
**Adaptation:** Frame as analysis, not recommendation. Instead of `"Recommend CRM tools"`, use `"Analyze the market landscape for CRM tools for B2B SaaS companies"`.

### 8.4 Google Gemini / AI Mode

**Dialect:** Keyword-anchored. Triggers best on traditional long-tail search queries.
**Source bias:** 99% of URLs in AI Mode appear in top 20 organic results. Traditional SEO still matters.

**Best for:** Question-format prompts matching "People Also Ask" patterns.
**Adaptation:** Use PAA-style questions. Instead of `"Best CRM tools"`, use `"What is the best CRM software for small businesses?"` Mirror how people type into Google.

### 8.5 Cross-Engine Strategy

- **67.4%** of domains are cited by exactly one AI platform. Only **6.5%** achieve presence across 5+ platforms.
- Never average across engines — report per-engine AND aggregate separately. Being #1 on Perplexity and invisible on ChatGPT averages to "mediocre," hiding the real problem.
- Signals that achieve cross-engine presence: Wikipedia, Reddit, G2, structured content, brand search volume (0.334 correlation — the strongest single predictor).

---

## Section 9: Prompt-to-Measurement Routing Map

*The master cross-reference. For any question type, this table shows what it feeds, what a gap looks like, and what to do about it.*

| Question Type | Brand in prompt? | CheckThat Score | Sub-metric(s) | What a gap looks like | Content action |
|--------------|-----------------|-----------------|---------------|----------------------|---------------|
| Best-of-Category | No | Presence | Presence Rate, Position | Not appearing in "best of" lists | Build category-defining content; improve structured data |
| Landscape / Market Map | No | Presence | Presence Rate | Not named as a "main player" | PR, analyst coverage, Wikipedia presence |
| Alternatives-To | No | Presence | Presence Rate | Not appearing as competitor alternative | Build comparison pages; target competitor weakness content |
| Unbranded Comparison | No | Presence | Presence Rate, Position | Not included in comparative responses | Comparison tables, head-to-head content |
| Direct Comparison | Yes (both brands) | Presence + Perception | Position, all Perception attributes | Unfavorable comparison narrative | Update competitive positioning content; address specific weaknesses |
| Feature & Integration | Yes | Perception (Capability) | Capability Score | AI says "limited" or misses key features | Update product pages with feature details; add schema markup |
| Implementation & Migration | Yes | Perception (Usability) | Usability Score | AI says "complex" or "steep learning curve" | Publish implementation guides; customer success stories |
| Pricing & Cost | Yes | Perception (Value) | Value Score | AI cites wrong pricing or says "expensive" | Update pricing pages; add structured pricing data; publish ROI content |
| ROI & Business Case | Yes | Perception (Value + Trust) | Value Score, Trust Score | No ROI narrative in AI responses | Publish case studies; build ROI calculator content |
| Risk & Compliance | Yes | Perception (Trust) | Trust Score | AI says "unclear" on compliance | Dedicated compliance/security pages; schema markup |
| Review & Reputation | Yes | Perception (Trust + Support) | Trust Score, Support Score | AI surfaces negative reviews or no reviews | Active review management; respond to criticism |
| Expert Opinion / Social Proof | Yes | Perception (Trust + Innovation) | Trust Score, Innovation Score | No analyst or community validation in AI | Build analyst relationships; Reddit participation |
| How-To & Implementation | Yes | Perception (Support) | Support Score | AI says "limited documentation" | Improve docs, tutorials, knowledge base |
| Trend & Future | Yes | Perception (Innovation) | Innovation Score | AI says "stagnant" or doesn't mention in trends | Thought leadership content; press coverage |
| Problem Definition | No | Early Presence (Tier 3) | Category association | Not mentioned when AI discusses the problem space | Problem-framing content; thought leadership |
| Category Education | No | Early Presence (Tier 3) | Category-defining authority | Not cited as category authority | Category-defining pillar content |

---

## Appendix A: Quick-Start Prompt Starter Kit

*50 ready-to-use prompts across all pattern categories. Fill in [your brand], [your category], [your competitor] to customize.*

### Presence Prompts (20)

```
 1. "Best [your category] tools for [your primary market]"
 2. "Best [your category] for startups"
 3. "Best [your category] for enterprise"
 4. "Best [your category] for [your top industry]"
 5. "Top 5 [your category] tools in 2026"
 6. "What [your category] should I evaluate?"
 7. "Who are the main players in [your category]?"
 8. "Emerging players in [your category]"
 9. "Alternatives to [Competitor 1]"
10. "Alternatives to [Competitor 2]"
11. "Best [Competitor 1] alternatives for [your primary use case]"
12. "What can I use instead of [Competitor 3]?"
13. "Compare the best [your category] platforms"
14. "Compare [your category] tools for [your primary use case]"
15. "Which [your category] tools have the best [your key differentiator]?"
16. "Rank the best [your category] options for [your primary market]"
17. "Best [your category] under $[your price point] per month"
18. "Best [your category] that integrates with [common platform]"
19. "What is [your category] and why does it matter?"
20. "[Approach A] vs [Approach B] for [your use case]"
```

### Perception Prompts (25)

```
Capability:
21. "Does [your brand] have [your top feature]?"
22. "Does [your brand] integrate with [common platform]?"
23. "Is [your brand] good for [your primary use case]?"
24. "[your brand] features overview"

Usability:
25. "Is [your brand] easy to use?"
26. "How long does it take to set up [your brand]?"
27. "What's the learning curve for [your brand]?"
28. "How do I migrate from [Competitor 1] to [your brand]?"

Value:
29. "[your brand] pricing"
30. "How much does [your brand] cost?"
31. "[your brand] vs [Competitor 1] pricing"
32. "What's the ROI of [your brand]?"

Trust:
33. "[your brand] reviews 2026"
34. "[your brand] pros and cons"
35. "Is [your brand] SOC2 compliant?"
36. "What does Reddit say about [your brand]?"

Support:
37. "How is [your brand]'s customer support?"
38. "[your brand] documentation quality"

Innovation:
39. "What makes [your brand] different from other [your category] tools?"
40. "Is [your brand] a leader in [your category]?"
41. "Why would I choose [your brand] over [Competitor 1]?"

Comparisons (Presence + Perception):
42. "[your brand] vs [Competitor 1]"
43. "[your brand] vs [Competitor 2]"
44. "[your brand] vs [Competitor 1] for [your primary use case]"
45. "Compare [your brand], [Competitor 1], and [Competitor 2]"
```

### Advanced Structures (5)

```
Generated Knowledge:
46. "Generate a list of 5 critical criteria for evaluating [your category]
    for a [your primary persona]. Then, based only on those criteria,
    recommend the top 3 platforms."

Persona-Injected:
47. "I'm a [your buyer's title] at a [size]-person [industry] company.
    We use [common tools]. We need [requirement]. What [your category]
    tools should I evaluate?"

Multi-Turn (start sequence):
48. "What is [your category]?" → "Best [your category] for [use case]"
    → "[your brand] vs [Competitor 1]" → "[your brand] pricing"
    → "[your brand] reviews" → "How to set up [your brand]"

Cluster (run all 5 for one signal):
49a. "Best [your category] tools for [your primary market]"
49b. "Top [your category] software for [your primary market]"
49c. "Leading [your category] platforms for [your primary market]"
49d. "Best [your category] for [specific constraint within primary market]"
49e. "What [your category] tool should a [primary market] company use?"

Competitive Switch:
50. "[Competitor 1] alternatives" → "Why are companies leaving [Competitor 1]?"
    → "[Competitor 1] vs [your brand] vs [Competitor 2]"
    → "How hard is it to migrate from [Competitor 1] to [your brand]?"
```

---

## Appendix B: Pattern ID Reference Index

| ID | Pattern Name | Score | Section |
|----|-------------|-------|---------|
| P-001 | Best-of-Category — Core | Presence | 2.1 |
| P-002 | Best-of-Category — By Company Size | Presence | 2.1 |
| P-003 | Best-of-Category — By Industry | Presence | 2.1 |
| P-004 | Best-of-Category — By Buyer Role | Presence | 2.1 |
| P-005 | Best-of-Category — By Use Case | Presence | 2.1 |
| P-006 | Best-of-Category — By Integration | Presence | 2.1 |
| P-007 | Best-of-Category — By Feature | Presence | 2.1 |
| P-008 | Best-of-Category — By Budget | Presence | 2.1 |
| P-009 | Best-of-Category — By Geography/Compliance | Presence | 2.1 |
| P-010 | Best-of-Category — Time-Qualified | Presence | 2.1 |
| P-011 | Best-of-Category — Top-N | Presence | 2.1 |
| P-012 | Best-of-Category — Recommendation Request | Presence | 2.1 |
| P-013 | Market Map — Main Players | Presence | 2.2 |
| P-014 | Market Map — Market Structure | Presence | 2.2 |
| P-015 | Market Map — Solution Types | Presence | 2.2 |
| P-016 | Market Map — Emerging Players | Presence | 2.2 |
| P-017 | Market Map — Competitive Landscape | Presence | 2.2 |
| P-018 | Alternatives — Standard | Presence | 2.3 |
| P-019 | Alternatives — Use-Case Qualified | Presence | 2.3 |
| P-020 | Alternatives — Replacement Intent | Presence | 2.3 |
| P-021 | Alternatives — Constraint-Filtered | Presence | 2.3 |
| P-022 | Alternatives — Architecture-Filtered | Presence | 2.3 |
| P-023 | Alternatives — Category Migration | Presence | 2.3 |
| P-024 | Unbranded Comparison — Category | Presence | 2.4 |
| P-025 | Unbranded Comparison — Use-Case | Presence | 2.4 |
| P-026 | Unbranded Comparison — Capability | Presence | 2.4 |
| P-027 | Unbranded Comparison — Ranking | Presence | 2.4 |
| P-028 | Problem Definition | Early Presence | 2.5 |
| P-029 | Category Education | Early Presence | 2.5 |
| P-030 | Category Need | Early Presence | 2.5 |
| P-031 | Approach Comparison | Early Presence | 2.5 |
| P-032 | Feature Validation | Perception (Capability) | 3.1 |
| P-033 | Feature Depth | Perception (Capability) | 3.1 |
| P-034 | Feature Comparison | Perception (Capability) + Presence | 3.1 |
| P-035 | Integration Check | Perception (Capability) | 3.1 |
| P-036 | Integration Listing | Perception (Capability) | 3.1 |
| P-037 | Use-Case Fit | Perception (Capability) | 3.1 |
| P-038 | Scalability | Perception (Capability) | 3.1 |
| P-039 | API/Developer | Perception (Capability) | 3.1 |
| P-040 | Product Breadth | Perception (Capability) | 3.1 |
| P-041 | Ease of Use | Perception (Usability) | 3.2 |
| P-042 | Setup Time | Perception (Usability) | 3.2 |
| P-043 | Onboarding Experience | Perception (Usability) | 3.2 |
| P-044 | Learning Curve | Perception (Usability) | 3.2 |
| P-045 | Technical Requirements | Perception (Usability) | 3.2 |
| P-046 | Implementation Process | Perception (Usability) | 3.2 |
| P-047 | Migration Path | Perception (Usability) | 3.2 |
| P-048 | Small Team Fit | Perception (Usability) | 3.2 |
| P-049 | Comparative Usability | Perception (Usability) | 3.2 |
| P-050 | Deployment Speed | Perception (Usability) | 3.2 |
| P-051 | Pricing — Direct | Perception (Value) | 3.3 |
| P-052 | Pricing — Question Form | Perception (Value) | 3.3 |
| P-053 | Pricing Model | Perception (Value) | 3.3 |
| P-054 | Pricing Comparison | Perception (Value) | 3.3 |
| P-055 | Budget-Filtered | Perception (Value) + Presence | 3.3 |
| P-056 | Free Tier | Perception (Value) | 3.3 |
| P-057 | ROI | Perception (Value) | 3.3 |
| P-058 | Business Case | Perception (Value) | 3.3 |
| P-059 | Total Cost of Ownership | Perception (Value) | 3.3 |
| P-060 | Case Studies | Perception (Value) | 3.3 |
| P-061 | Cost Reduction | Perception (Value) | 3.3 |
| P-062 | General Trust | Perception (Trust) | 3.4 |
| P-063 | Security | Perception (Trust) | 3.4 |
| P-064 | Compliance Standards | Perception (Trust) | 3.4 |
| P-065 | Data Privacy | Perception (Trust) | 3.4 |
| P-066 | Uptime/Reliability | Perception (Trust) | 3.4 |
| P-067 | Vendor Stability | Perception (Trust) | 3.4 |
| P-068 | Reviews | Perception (Trust) | 3.4 |
| P-069 | Pros and Cons | Perception (Trust) | 3.4 |
| P-070 | Complaints/Problems | Perception (Trust) | 3.4 |
| P-071 | Downsides | Perception (Trust) | 3.4 |
| P-072 | Social Proof | Perception (Trust) | 3.4 |
| P-073 | Analyst Coverage | Perception (Trust) | 3.4 |
| P-074 | Community Opinion | Perception (Trust) | 3.4 |
| P-075 | Support Quality | Perception (Support) | 3.5 |
| P-076 | Responsiveness | Perception (Support) | 3.5 |
| P-077 | Documentation Quality | Perception (Support) | 3.5 |
| P-078 | Help Resources | Perception (Support) | 3.5 |
| P-079 | Community Support | Perception (Support) | 3.5 |
| P-080 | Comparative Support | Perception (Support) | 3.5 |
| P-081 | Onboarding Support | Perception (Support) | 3.5 |
| P-082 | Differentiation | Perception (Innovation) | 3.6 |
| P-083 | Competitive Advantage | Perception (Innovation) | 3.6 |
| P-084 | Uniqueness | Perception (Innovation) | 3.6 |
| P-085 | Growth Trajectory | Perception (Innovation) | 3.6 |
| P-086 | Vision | Perception (Innovation) | 3.6 |
| P-087 | Category Leadership | Perception (Innovation) | 3.6 |
| P-088 | Innovation Recognition | Perception (Innovation) + Presence | 3.6 |
| P-089 | Future/Trends | Perception (Innovation) | 3.6 |
| P-090 | Category Creation | Perception (Innovation) | 3.6 |
| P-091 | Category Trends | Perception (Innovation) | 3.6 |
| P-092 | Direct Head-to-Head | Presence + Perception | 4.1 |
| P-093 | Use-Case Comparison | Presence + Perception | 4.1 |
| P-094 | Size-Qualified Comparison | Presence + Perception | 4.1 |
| P-095 | Multi-Vendor Comparison | Presence + Perception | 4.1 |
| P-096 | Conditional Choice | Presence + Perception | 4.1 |
| P-097 | Conditional Choice (Inverse) | Presence + Perception | 4.1 |
| P-098 | Fit Question | Presence + Perception | 4.1 |
| P-099 | Pricing Comparison | Presence + Perception (Value) | 4.1 |
| P-100 | Ranking Context | Presence + Perception | 4.2 |
| P-101 | Segment Fit | Presence + Perception | 4.2 |
| P-102 | Limitation Scope | Perception | 4.2 |
| P-103 | CMO / VP Marketing Persona | Any | 6.1 |
| P-104 | CTO / Technical Leader Persona | Any | 6.1 |
| P-105 | CFO / Financial Decision-Maker Persona | Any | 6.1 |
| P-106 | Founder / CEO Persona | Any | 6.1 |
| P-107 | IC / Practitioner Persona | Any | 6.1 |
| P-108 | Generated Knowledge — Criteria-Then-Rank | Presence | 6.2 |
| P-109 | Generated Knowledge — Attribute-Then-Compare | Presence + Perception | 6.2 |
| P-110 | Generated Knowledge — Problem-Then-Solve | Presence | 6.2 |

---

*This document consolidates prompt patterns from: prompt-taxonomy-and-ontology-v1.md, prompt-writing-methodology.md, buyer-evaluation-prompt-playbook.md, prompt-methodology-and-pattern-library.md, and the Eon Top 500 Prompts Guide. It extends those sources with the Routing Rule decision gate, Reputation-feeding signal patterns, the Prompt-to-Measurement Routing Map, Pattern IDs, and the Quick-Start Starter Kit.*

*Maintained by the GrowthX team. Last updated: February 2026.*
