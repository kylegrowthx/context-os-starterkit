# CheckThat Weekly Check In

<metadata>
date: 2025-12-22
time: 18:00 UTC
duration: 36 minutes
organizer: Marcel Santilli
source: fireflies
fireflies_id: 01KCMP5SWN5RBEN1S0K2PCHMT8
transcript_url: https://app.fireflies.ai/view/01KCMP5SWN5RBEN1S0K2PCHMT8
enriched_on: 2026-03-01 00:00 UTC
participants:
  - Marcel Santilli (GrowthX, CEO)
  - Stevie Kim (CheckThat, Operations)
  - Jacopo Beschi (CheckThat, Frontend Engineering)
  - Jose Farias (CheckThat, Backend Architecture)
  - Daniel Lopes (CheckThat)
  - Estevão Mascarenhas (CheckThat)
  - Jason Gong (CheckThat)
  - Leonardo (CheckThat)
</metadata>

---

## Summary

The CheckThat team validated organic growth momentum as essential to sustaining ~$200k/month operational costs. A 24-hour impression spike outpaced the prior week's total, with clicks rising to 2–3/day through meta title optimization—confirming meta tags as a high-ROI SEO lever. The team committed to shipping end-to-end user experience improvements: onboarding flows, CMS usability, data visualization, and frontend performance. Key blockers identified: 13,000+ prompts require categorization for onboarding scale; frontend paint metrics degrade UX and SEO until Jose's architecture merge; workspace ID exposure in URLs creates privacy and competitive risk. Jacopo will implement cookie-based ID encryption as interim mitigation.

---

## Context

CheckThat is GrowthX's strategic software bet—a B2B AI visibility tool that scans competitor and prospect deployments for AI usage, keywords, and prompts. The platform is pre-revenue and currently under heavy engineering optimization to improve product fundamentals (UX, performance, data visualization) before launch. Weekly check-ins align the co-founder, operations lead, and engineering leads (frontend and backend architecture) on metrics, blockers, and prioritization. The team is approaching a critical inflection: validated organic growth signals (meta title tweaks yielding 2-3 clicks/day) indicate product-market demand, but operational costs and engineering bottlenecks (slow frontend, disorganized prompt library) require simultaneous focus on growth validation and product hardening.

---

## Relevance

**CheckThat Product & Growth**
- Organic growth validation: 24-hour impression spike and 2–3 clicks/day demonstrate meta tag optimization ROI
- Onboarding and prompt organization: 13,000+ prompts need categorization to convert traffic into signups
- Customer success: workspace content (Rex, Galileo, Airbyte) requires editorial QA and management

**Technical & Performance**
- Frontend performance: First/Largest Contentful Paint degrading SEO and UX; monitoring ongoing, optimization deferred until backend rearchitecture completes
- URL privacy: Workspace ID sequence numbers expose growth rates and workspace counts to competitors; cookie-based encryption proposed as quick fix

**Business & Monetization**
- Cost justification: $200k/month spend requires sustained organic growth to validate monetization model
- Launch readiness: Pricing strategy and onboarding flow optimization pending team input

---

## Decisions & Commitments

1. **Prioritize organic growth validation** through continuous impression and click monitoring to justify operational costs
2. **Defer frontend optimization** until Jose completes backend/frontend rearchitecture to avoid wasted effort
3. **Implement encrypted cookies** to obscure workspace IDs in URLs (interim privacy/competitive mitigation; long-term aspiration: clean URLs like Canva)
4. **Organize 13,000+ prompts** into manageable subgroups to improve onboarding UX and reduce manual setup friction
5. **Editorial team validates workspace content** (Rex, Galileo, Airbyte tickets) for prompt relevance and quality
6. **Monetization & onboarding strategy** requires team feedback before next launch milestone

---

## Open Questions

- What is the optimal onboarding flow and pricing strategy integration? Current onboarding paused pending team input.
- How should the 13,000+ prompt library be categorized? What subgroups serve the most critical user segments?
- How soon will Jose's rearchitecture merge? (Determines when frontend optimization work can begin.)
- What is the launch readiness checklist? Current focus areas: monitoring, onboarding flows, cost validation.

---

## Overview & Key Topics

**Metrics & Growth**
- Impressions: 24-hour spike outpaced entire prior week
- Clicks: Rising to 2–3/day (driven by meta title updates)
- Backend performance: Request times <1s (admin: <5s)
- Frontend metrics: First/Largest Contentful Paint currently poor (SEO and UX impact)

**Product & UX**
- Onboarding flow: Paused pending pricing strategy input
- Prompt library: 13,000+ prompts; requires categorization for scale
- Data visualization: Clarity improvements needed
- Content management: Editorial team QA in progress (Rex, Galileo, Airbyte)

**Technical Roadmap**
- Backend/frontend rearchitecture: Major refactor underway; Jose leading
- Cookie-based workspace ID encryption: Quick-fix for URL privacy; Jacopo to implement
- Long-term: Clean URL architecture (e.g., Canva-style)

**Business & Strategy**
- Cost baseline: ~$200k/month operational spend
- Validation goal: Prove organic growth can sustain costs
- Monetization & pricing docs: Marcel to share for team feedback

---

## Action Items

**Jose Farias (CheckThat, Backend Architecture)**
- Add status updates on data visualization improvements and performance metrics during next meeting
- Continue backend/frontend rearchitecture; expected completion soon

**Stevie Kim (CheckThat, Operations)**
- Distribute next week's agenda earlier for team review and input
- Collaborate with editorial team to review and QA workspace tickets (Rex, Galileo, Airbyte, and others)

**Marcel Santilli (GrowthX, CEO)**
- Share monetization and pricing strategy documents with team for feedback
- Collect team input on onboarding flow pricing strategy and optimal account setup processes
- Continue monitoring impressions, clicks, and SEO signals; share updates with team weekly

**Jacopo Beschi (CheckThat, Frontend Engineering)**
- Monitor frontend performance metrics (First Contentful Paint, Largest Contentful Paint); document observations
- Defer deep frontend optimization until Jose's rearchitecture merges to avoid wasted effort
- Implement encrypted cookie solution to obscure workspace IDs in URLs (privacy and competitive risk mitigation)

---

## Transcript

**Marcel Santilli:** This meeting is being recorded. Let me get everyone's attention here.

**Stevie Kim:** Okay everyone, let's get started. Quick agenda review.

**Marcel Santilli:** Good. So I want to outline our core focus areas today. First, organic growth through impressions, clicks, mentions, indexing. Second, customer success and end-to-end experience including onboarding, CMS usability, data visualization clarity, and performance speed for editors and customers.

**Stevie Kim:** That's right. We're tracking those metrics closely.

**Marcel Santilli:** I want to highlight something important. In the last 24 hours, impressions outpaced the entire prior week. And we're seeing clicks rising to 2-3 per day. This is critical because we're spending nearly $200,000 monthly. This organic growth is what validates our monetization strategy.

**Jose Farias:** That's excellent progress.

**Marcel Santilli:** Small tweaks like updating meta titles are driving more clicks. These are positive signals for search ranking. Our goal is to keep doubling impressions while steadily increasing clicks.

**Stevie Kim:** We need to stay focused on enhancing end-to-end customer experience. That includes onboarding, content management, data visualization performance, and loading speed.

**Daniel Lopes:** Understood. What about the prompt management?

**Marcel Santilli:** Right. The current library holds over 13,000 prompts. The goal is to organize them into manageable subgroups for better user experience. Better management will allow new users immediate access to relevant prompts without manual setup.

**Stevie Kim:** That will increase trust in the system from evaluation through adoption.

**Jose Farias:** The many-to-many prompt management feature is key here.

**Stevie Kim:** Editorial support is helping validate workspace content and prompt relevance for key clients like Rex, Galileo, and Airbyte.

**Marcel Santilli:** Good. Now on the technical side, backend request times are mostly under 1 second, with admin requests allowed up to 5 seconds. That's stable.

**Jacopo Beschi:** But frontend metrics like first contentful paint and largest contentful paint are poor right now.

**Marcel Santilli:** How poor are we talking?

**Jacopo Beschi:** Pretty slow for user perception and SEO impacts.

**Jose Farias:** I'm rewriting major parts of the frontend and backend architecture. That should address these issues. Expected to conclude soon.

**Jacopo Beschi:** Until the rearchitecture is finished, I'll hold off on deep frontend optimizations to avoid wasted work. I'll continue monitoring though.

**Marcel Santilli:** That makes sense. The public-facing pages share components with the private side, so improvements will benefit both.

**Marcel Santilli:** Now let's talk about the URL structure issue. Current workspace URLs reveal sequence numbers that could allow external parties to estimate user growth and workspace counts.

**Jacopo Beschi:** That's a privacy and competitive risk.

**Marcel Santilli:** Exactly. Free accounts could be used daily to monitor workspace creation numbers, revealing growth rates publicly.

**Jose Farias:** It's mostly aesthetic, but obscuring those IDs could improve social sharing and backlink quality.

**Marcel Santilli:** The question is engineering investment. Do we rearchitect for clean URLs now or find a quicker solution?

**Jacopo Beschi:** We could obscure this via encrypted cookies. Hide the workspace ID even from the user without heavy rearchitecture.

**Marcel Santilli:** That's a good interim solution. Jacopo, can you tackle the cookie encryption approach?

**Jacopo Beschi:** Yes, I can add that to my work during the rearchitecture phase.

**Marcel Santilli:** Good. Longer term we can aspire to clean URLs like Canva, but that requires significant engineering resources.

**Stevie Kim:** What about the monetization strategy and launch readiness?

**Marcel Santilli:** I have two main validation goals: proving organic growth to sustain costs, and achieving launch readiness with reliable monitoring and onboarding workflows. Let me share the pricing and monetization docs with everyone for feedback.

**Jose Farias:** That will help us move forward.

**Marcel Santilli:** Also, I want input on the onboarding flow pricing strategy and optimal account setup. Currently the onboarding flow is paused pending that input.

**Stevie Kim:** The focus should be on converting increased traffic into customer signups.

**Marcel Santilli:** Right. So let's keep tracking these metrics and maintain momentum. Any other issues?

**Jacopo Beschi:** Just keep monitoring. Frontend work is on track with Jose's rearchitecture.

**Marcel Santilli:** Great. Keep up the good work everyone. Let's maintain this positive trajectory.
