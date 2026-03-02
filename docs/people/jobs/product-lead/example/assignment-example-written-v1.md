# Example Submission: Written Doc + Q&A Format

*This simulates what a strong candidate would submit as a structured written analysis before a live Q&A session.*

---

# CheckThat Product Analysis

## Executive Summary

CheckThat launched two weeks ago after four months of focused building with a team of three engineers. The team made deliberate prioritization calls, and they were the right ones.

The strategy doc describes a three-layer system: Context (brand truth), Instruments (prompts), and Measurement (what we learn). The team shipped the Instruments layer first: a shared prompt library, multi-engine tracking, custom prompts, and category pages built for organic discovery. They also delivered solid Recall metrics as the first measurement capability.

This was the correct sequence. The open index and category pages are the organic growth engine. You can't monetize or build higher-order features without traffic and users. Ship the infrastructure first, prove traction, then build up the stack.

The next phase is about connecting meaning to data. The strategy doc's strongest ideas, alignment scoring and the brand research analogy, depend on Context (Layer 1) being built. With context in place, CheckThat becomes something genuinely different from every other AEO tool in the market.

This analysis covers what I observed in the product, what I'd build next with the current team, and the risks and trade-offs involved.

---

## Part 1: Product Observations

I spent 6 hours with CheckThat. Tracked two brands, explored the open index, and tested the custom prompt workflow.

### What the Team Shipped Well

**The shared prompt library is the real product.** Before adding a single custom prompt, I could see how AI engines perceive brands in my category. This inverts the typical SaaS onboarding: value first, configuration later. That's hard to get right and the team nailed it.

**Category pages are strong SEO assets.** Well-structured, data-rich, answer real buyer questions. Two weeks post-launch is too early to see organic results, but the pages are built for it. This validates the core growth thesis at the content level.

**Tracking infrastructure works.** Multi-engine probing, consistent data updates, reliable responses. The backend/architecture engineer clearly built something solid. This is the kind of plumbing that's invisible when it works and catastrophic when it doesn't.

**Fast signup-to-value.** I was seeing data within minutes. No lengthy onboarding, no required configuration. Smart choice for a product betting on organic traffic where bounce rate matters.

### What I'd Build On Next

**Competitive framing.** The data exists to show me alongside competitors, but it isn't the default experience. Nobody tracks their brand in isolation. Making the competitive view primary would immediately increase perceived value.

**Score context.** I see a recall rate of 65%. Is that good for my category? Better or worse than last week? Compared to competitors? The raw number needs framing to be useful.

**Actionable direction.** After my session, I understood what AI says about my brand. I didn't know what to do about it. The strategy doc's vision of "here's what to fix" recommendations is the next value unlock.

### What Was Clearly Intentional

The strategy doc describes features (brand context, alignment scoring, composites, lift metrics) that don't exist in the product yet. After reading the doc, the sequencing makes sense:

- **Context was deferred** because the tracking engine and open index needed to ship first to prove organic traction. You can't build alignment scoring without an audience.
- **Alignment scoring was deferred** because it depends on context. You can't measure "is AI right about you?" until you know what "right" means.
- **Composites and recommendations were deferred** because they depend on both context and alignment.

The team built bottom-up. Instruments first, basic measurement second, everything else queued. With three engineers in four months, that was the right call.

---

## Part 2: What I'd Build Next

### Constraint: The Team We Have

Three full-stack engineers (one backend/architecture, one UI-heavy, one generalist), a designer as needed, one PM. That's roughly 3 engineering-months per month. I'd plan in 4-week blocks and keep two parallel workstreams maximum.

### Phase 1: Brand Context Capture (Weeks 1-4)

**What:** A guided flow where users define their brand truth. Positioning, key differentiators, primary competitors.

**Why now:** This is the prerequisite for alignment scoring, which is the strategy doc's identified killer feature. Without it, we can't build the most differentiated thing in the vision.

**How I'd scope it:**
- Start with 3-5 structured fields, not the full brand context model from the strategy doc. Positioning statement, top 3 differentiators, top 3 competitors, primary buyer persona.
- Pre-populate from public data where possible (company description, competitor suggestions from our index data).
- Under 5 minutes to complete. If it takes longer, completion rates will tank.
- Versionable. Brands change positioning. The "answer key" should evolve.

**Team allocation:**
- Backend/architecture eng: Data model, API, storage. Design for future expansion (the full brand context model from the strategy doc) even though we're shipping a subset.
- Generalist eng: Integration with existing onboarding flow, pre-population logic.
- Designer: Onboarding UX for the context flow.
- PM: Coordinate with editorial on which fields matter most, write copy for the guidance text.

**Activation risk:** Adding a step before users see value could hurt activation. Mitigation: don't gate the core product on context. Users get the open index immediately. Context is positioned as "unlock deeper insights about your brand" after they've already seen value.

### Phase 2: Alignment Scoring (Weeks 3-7, overlapping)

**What:** For branded prompts, compare AI's response against the user's brand context. Score alignment on key dimensions. Surface specific gaps.

**Why now:** This is what the strategy doc calls "the killer feature" and the market supports it. Every other tool shows what AI says. CheckThat would be the first to tell you if AI is right.

**How I'd scope it:**
- LLM-as-judge evaluation against brand context fields. Three dimensions first: Feature Accuracy, Positioning Match, Factual Accuracy.
- Run on all branded/factual prompts where we have context. "What is [Brand]?", "[Brand] pricing", "Does [Brand] integrate with [tool]?"
- Output: alignment score + specific callouts. "AI says you're an expense tool. You say you're a finance platform. This is a gap."
- Conservative confidence thresholds. Show "insufficient data" rather than wrong assessments. Trust erodes fast if scoring is inaccurate.

**Team allocation:**
- Backend/architecture eng: Evaluation pipeline, LLM-as-judge integration, scoring logic.
- UI eng: Dashboard updates to show alignment scores, gap callouts, drill-down views.
- Generalist eng: Support on API integration between context and scoring systems.

**Technical risk:** LLM-as-judge accuracy. Mitigation: human calibration study on a sample before launching broadly. Understand error rate. Only score dimensions where confidence is high.

### Phase 3: Competitive Default + Recommendations (Weeks 6-10)

**What:** Make the competitive comparison view the primary dashboard. Add rule-based recommendations for the biggest gaps.

**Why now:** With alignment data flowing, we can tell users not just "here's your score" but "here's what's wrong and what to do." This is what converts users from monitoring to action.

**How I'd scope it:**
- Default dashboard: your brand alongside top competitors (from context or auto-detected from category).
- Simple recommendations engine (rule-based, not ML): "AI gets your pricing wrong. Consider updating your pricing page." / "You don't appear in 'best of' category questions. Publish a comparison page."
- Track whether users act on recommendations. This creates the Lift measurement data for free.

### What I'd Skip

**Multi-turn tracking.** Strategy doc leans toward deferring this. Agree. Single-prompt improvement gives 80% of value at 20% of complexity.

**Prompt clustering.** Important for measurement accuracy but not blocking the core value unlock. Add after alignment is shipping.

**Custom-to-shared promotion.** Not enough volume. Manual editorial curation is fine.

**Composite score weighting.** The strategy doc asks whether weighting should be configurable per brand. Ship with equal weights. Make configurable when enough users ask for it.

---

## Part 3: Open Question Responses

The strategy doc lists seven open questions. Here's my take on the ones most relevant to the near-term roadmap.

**#3 Alignment Scoring Methodology.** LLM-as-judge with structured evaluation rubrics derived from brand context. Simple entity/keyword checks as a baseline validation layer. Human review on a sample to calibrate before launch. Start conservative, expand as confidence grows.

**#5 Composite Score Weighting.** Equal weights by default. Don't over-engineer this. The first version of the AI Brand Health Score should just work. Make weighting configurable later when we understand what users actually care about.

**#7 Engine Weighting.** Show per-engine data side-by-side. Don't hide information behind weighted averages. Add an aggregate view with market-share weighting as a secondary metric, not the primary one.

**#1 Topic Granularity.** Topics should be broad (10-50 prompts each). Let context modifiers handle the segmentation. "CRM for healthcare" is a topic. "CRM for healthcare startups" is a topic + company size modifier.

---

## Part 4: Risks

**Risk 1: Context adoption.** If users don't fill in brand context, alignment can't work. Mitigation: make context optional, position it as an upgrade, show a preview of what alignment insights look like before asking for input. "AI says you're X. Is that right? Tell us what you actually are."

**Risk 2: Alignment accuracy.** Wrong alignment scores erode trust in the entire product. Mitigation: conservative thresholds, human calibration, "insufficient data" fallback.

**Risk 3: Team bandwidth.** Three phases in 10 weeks with three engineers is aggressive. Phase 1 and 2 have overlap, which means careful coordination. If velocity is slower than expected, I'd cut Phase 3 scope (skip recommendations, keep competitive view) rather than rush alignment.

**Risk 4: Premature optimization.** The product launched two weeks ago. We might learn things from early user behavior that change these priorities entirely. I'd commit to Phase 1 and keep Phase 2-3 as strong hypotheses that we validate with Phase 1 learnings and early user data.

---

## Part 5: What I'd Do in Week 1

- **Monday-Tuesday:** Go through the codebase with the team. Understand architecture, data model, deployment pipeline. Map what's easy to change and what's load-bearing.
- **Wednesday:** Talk to 5-10 early users. Not surveys. Calls. "Why did you sign up? What did you do? What confused you? What would make you pay?"
- **Thursday:** Sit with each engineer individually. Understand their strengths, what they're excited about, where they feel stretched.
- **Friday:** Write the real Phase 1 spec based on everything I learned that week.

---

*Prepared for Q&A. Happy to go deeper on any section, especially the technical approach to alignment scoring and the context data model design.*
