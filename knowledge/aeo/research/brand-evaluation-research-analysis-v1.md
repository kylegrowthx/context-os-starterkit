# Analysis: Brand Evaluation Research & CheckThat Implications

<metadata>
purpose: Analysis of the brand evaluation frameworks research and what it means for CheckThat's taxonomy, product, and positioning
audience: Marcel, Product, Leadership
related: pipeline/scratchpad/checkthat-screens-v1.md, docs/products/checkthat/product-vision-v1.md
domain: product-strategy
confidence: analysis
last_updated: 2026-02-14
</metadata>

---

## What the Research Says (Summary)

The paper analyzes 15+ brand evaluation frameworks — Gartner, Forrester, IDC, G2, Capterra, Brandwatch, SimilarWeb, plus foundational models like Aaker, Keller, and Kantar — and finds they all converge on the same core architecture: "what you can do today" vs. "where you're going tomorrow." It identifies 77 distinct brand attributes that cluster into 8 macro-categories, then maps those categories to their AI-perception equivalents. The core argument: CheckThat can build its measurement taxonomy on battle-tested foundations rather than inventing from scratch, while differentiating on AI-native metrics no existing framework measures.

---

## What's Strong

**The convergence finding is the backbone.** Every major framework — Gartner, Forrester, G2, IDC — uses the same dual-axis structure. Execution vs. Vision. Satisfaction vs. Market Presence. Capabilities vs. Strategy. This isn't coincidence; it's a settled pattern for how the market evaluates technology vendors. CheckThat should adopt this shape. The proposed "AI Perception Quality vs. AI Visibility Scale" dual-axis is the right instinct and it would let buyers immediately understand CheckThat data because the frame is already familiar.

**The 10 emerging AI-perception attributes are well-identified.** Mention Frequency, Mention Prominence, Citation Authority, Sentiment Quality, Contextual Accuracy, Category Association Strength, Platform Consistency, Temporal Stability, Competitive Positioning, Use-Case Specificity. This is a clean, defensible list. It covers what matters without over-indexing on edge cases.

**The buyer committee segmentation insight is underrated.** Different stakeholders evaluate brands through different lenses — CMO cares about positioning, CTO about capabilities, CFO about value. The research correctly identifies that AI systems describe brands differently depending on the implied role in the query. This means CheckThat shouldn't just track prompts generically — it should segment by buyer persona, which would be a genuine product differentiator over every tool currently in market.

**The 94% stat anchors the entire thesis.** 94% of B2B buyers using LLMs during their buying process (6sense 2025). Trust in AI tools at 80%, up 19 points YoY. This isn't theoretical anymore. If you were going to build this product, these are the numbers that confirm the timing is right.

**The gap identification is precise.** Hallucination Rate, Contextual Accuracy, Citation Authority, Platform Consistency — four attributes with zero analogs in traditional brand measurement. This is where CheckThat has exclusive positioning. No analyst firm, no review platform, no brand tracker can measure these because they don't monitor AI outputs.

---

## What's Missing

**No mapping to what CheckThat already tracks.** The research proposes 10 AI-perception attributes but doesn't reconcile them against CheckThat's existing metrics (Recall, Sentiment, Alignment, Lift, Engine Coverage). Some of these map cleanly — Mention Frequency = Recall, Platform Consistency = Engine Coverage, Temporal Stability = Lift. Others are genuinely new — Citation Authority, Contextual Accuracy, Hallucination Rate. The gap between "what we already measure" and "what this research says we should measure" needs to be explicit.

Here's the mapping:

| Research Attribute | CheckThat Current Metric | Status |
|---|---|---|
| Mention Frequency | Recall % | Already tracking |
| Mention Prominence | Position (#1, #2, etc.) | Already tracking |
| Sentiment Quality | Sentiment (pos/neu/neg) | Already tracking |
| Platform Consistency | Engine Coverage (X/5) | Already tracking |
| Temporal Stability | Trend / Lift (30-day %) | Already tracking |
| Competitive Positioning | Benchmarks (win/lose/gap) | Already tracking (Pro+) |
| Citation Authority | Sources Cited | Partially — we show citations but don't score authority |
| Contextual Accuracy | Alignment | Partially — we flag misalignment but don't score accuracy |
| Category Association Strength | — | Not tracking |
| Use-Case Specificity | — | Not tracking |
| Hallucination Rate | — | Not tracking |
| Misattribution Rate | — | Not tracking |

CheckThat already covers 6 of the 10 proposed attributes. Two more are partially there. Four are genuinely new build. That's a strong starting position.

**No prioritization of what to build when.** The research treats all 10 attributes as equally important. They're not. For launch and early traction, Recall, Sentiment, Engine Coverage, and Trend are the right foundation (and they're already built). The next tier — Citation Authority, Contextual Accuracy, Use-Case Specificity — should be the post-launch roadmap. Hallucination Rate and Misattribution Rate are interesting but operationally hard and niche in appeal.

Suggested build order:

- **Now (launch):** Recall, Sentiment, Engine Coverage, Trend, Position, Competitive Positioning
- **Next (months 1-3):** Citation Authority scoring, Contextual Accuracy scoring, Use-Case Specificity tagging
- **Later (months 3-6):** Category Association Strength index, Hallucination Rate, Misattribution Rate

**No scoring methodology proposed.** The research identifies what to measure but not how to score it. What makes Recall "good"? Is 60% strong or weak? The AI Visibility Score (the composite 0-100 metric on the Insights screen) needs a weighting model. The research should propose one, or at least suggest weights. A starting point:

| Attribute | Suggested Weight | Rationale |
|---|---|---|
| Recall | 25% | Most fundamental — are you visible at all? |
| Sentiment Quality | 20% | Being mentioned negatively is worse than not being mentioned |
| Platform Consistency | 15% | Breadth matters — one engine isn't enough |
| Mention Prominence | 15% | #1 recommendation vs. also-mentioned is a big gap |
| Temporal Stability | 10% | Volatility signals weakness |
| Contextual Accuracy | 10% | Are they getting the story right? |
| Citation Authority | 5% | Nice to have, harder to influence |

This would let CheckThat generate a defensible composite score from day one, with room to add attributes later.

**The 8 macro-categories are a framework, not a product feature.** The taxonomy (Awareness & Visibility, Product Capability, Strategic Vision, Trust & Credibility, Customer Experience, Market Position, Value & Differentiation, Momentum) is clean for a research paper. But it's too abstract to turn directly into a product screen. Customers don't think in "macro-categories." They think: Am I showing up? What are they saying? What should I do? The Insights screen already nails this framing. The taxonomy should live underneath — powering the score, structuring the data — but not surface directly to users.

**No practical guidance on buyer persona segmentation.** The research identifies that AI answers differently depending on the implied role in the query, and that CheckThat should enable segmentation by buyer persona. This is a compelling insight. But how? The prompts would need to be tagged by implied persona: "What's the best expense tool for my finance team?" (CFO lens) vs. "What expense tool has the best API?" (engineering lens) vs. "What expense tools are easiest to set up?" (end user lens). This could be a powerful differentiation, but it needs a concrete plan: who tags the prompts, how many personas, how is it surfaced in the dashboard.

**SimilarWeb's AI Visibility Metrics deserve more attention.** The research mentions in passing that SimilarWeb added AI Visibility Metrics in 2025-26 (Visibility Score, Brand Mention Share, Citation Share, Sentiment Distribution). This is a direct competitor signal. SimilarWeb has massive distribution, brand recognition, and existing enterprise contracts. If they're entering this space, CheckThat needs to understand exactly what they're offering and where the differentiation is. The research should have gone deeper here.

---

## What This Means for the Product

### Three things to do now

**1. Formalize the AI Visibility Score.** Use the taxonomy as the intellectual foundation for the composite score shown on the Insights screen. Start with the 6 attributes CheckThat already tracks, apply the weight model above, and ship a 0-100 score at launch. It doesn't need to be perfect — it needs to be defensible, explainable, and better than what anyone else offers (which right now is nothing).

**2. Add Citation Authority as a first-class metric.** CheckThat already captures which URLs AI engines cite. The gap is turning that raw data into a scored metric. How authoritative are the sources citing you? Is AI pulling from your owned content (strong signal) or from third-party aggregators (weaker signal)? This is low-effort to build on top of existing data and would be a strong differentiator — no competitor tracks this.

**3. Plan the persona segmentation feature.** Don't build it yet. But tag the shared prompt library by implied buyer persona (executive, technical, end-user, financial) and plan the UX for filtering insights by persona. When it ships, it could be the Pro→Business upgrade trigger: "See how AI describes you to technical buyers vs. executive buyers."

### Three things to plan for post-launch

**4. Contextual Accuracy scoring.** Develop a methodology for scoring whether AI's description of a brand is actually correct. This requires knowing what the brand says about itself (positioning, features, messaging) and comparing it to what AI says. For existing brands in the index, this data exists in the brand profiles. The score would be: "AI gets you 74% right — here's what it's wrong about."

**5. Competitive Intelligence integration.** The research identifies that Crayon, Klue, and Kompyte share a 5-stage CI architecture. CheckThat isn't a CI tool, but the "AI perception" layer is complementary to competitive intelligence. Explore partnerships or data integrations with these platforms — they have enterprise distribution, CheckThat has data they can't replicate.

**6. Dual-axis visualization.** Build toward the Gartner-style quadrant view for categories. Y-axis: AI Perception Quality (accuracy, sentiment, description depth). X-axis: AI Visibility Scale (frequency, engine breadth, competitive share). Plot every brand in a category on this grid. This would be the signature visualization — immediately recognizable, immediately valuable, and directly comparable to Gartner's output.

---

## What This Means for Positioning

The research confirms CheckThat's positioning but also sharpens it. Here's the updated way to talk about what CheckThat measures vs. what exists:

| Framework | What it measures | What it misses |
|---|---|---|
| Gartner / Forrester / IDC | Analyst opinion of vendor capability and strategy | How AI engines actually describe vendors |
| G2 / Capterra / TrustRadius | User satisfaction and review data | Whether AI even surfaces the brand at all |
| Brandwatch / Sprout | Social sentiment and share of voice | AI-generated brand perception |
| SimilarWeb | Traffic, search, and emerging AI metrics | Depth of AI perception (context, accuracy, citations) |
| Traditional brand tracking | Survey-based awareness and consideration | Real-time AI answer monitoring at scale |
| **CheckThat** | **AI-generated brand perception: who AI recommends, how it describes them, what it gets right, and what's changing** | *(This is the new layer)* |

The story to customers: "Gartner tells you what analysts think. G2 tells you what users think. CheckThat tells you what AI thinks — and AI is where 94% of your buyers are now starting."

---

## Bottom Line

The research is solid. It correctly identifies the convergence across frameworks, proposes a clean taxonomy, and pinpoints the AI-native gap. What it needs is operationalization — weights, build order, scoring methodology, and practical product guidance. The biggest strategic takeaway is that CheckThat doesn't need to invent a new way of measuring brands; it needs to measure an entirely new surface (AI answers) using a structure buyers already understand (the dual-axis, capability-vs-vision pattern). That combination — familiar framework, unfamiliar data — is the fastest path to trust and adoption.
