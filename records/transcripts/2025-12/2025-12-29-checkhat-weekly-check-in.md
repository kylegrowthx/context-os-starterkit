# CheckThat Weekly Check In

<metadata>
date: 2025-12-29
time: 18:00 UTC
duration: 49 minutes
organizer: marcel@growthxlabs.com
participants:
  - name: Marcel Santilli
    company: GrowthX
    role: CEO/Organizer
  - name: Estevão Mascarenhas
    company: CheckThat
    role: Engineering
  - name: Jacopo Beschi
    company: CheckThat
    role: Frontend/Performance
  - name: Jose Farias
    company: CheckThat
    role: Backend Architecture
  - name: Pedro
    company: CheckThat
    role: Frontend
  - name: Daniel Lopes
    company: CheckThat
    role: Infrastructure/Cost
  - name: Stevie Kim
    company: CheckThat
    role: Product/Operations
source: fireflies
fireflies_id: 01KD3KPN73XC8KZSH5XHCEF3E6
transcript_url: https://app.fireflies.ai/view/01KD3KPN73XC8KZSH5XHCEF3E6
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Context

CheckThat's weekly engineering and product sync on Dec 29, just after the Christmas break. The team reported strong organic growth (9% impressions increase, 1,000+ pages indexed) but highlighted mounting cost pressures—$150K monthly spend, with Gina (likely an inference service) consuming $45K alone. The focus is on scaling the platform's SEO visibility while managing infrastructure costs and unblocking the onboarding flow, which is critical for launch readiness.

---

## Relevance

**CheckThat (Product & Engineering)**
- Organic SEO performance: 9% impressions growth, 1,000+ pages indexed
- Cost management: $150K/month monthly burn, Gina service at $45K
- RE architecture simplification: Merged, reduces technical debt
- Prompt management: 13,000+ prompts with many-to-many relationships requiring optimization

**Frontend & Performance**
- First Contentful Paint and Largest Contentful Paint metrics degraded
- Deferring major optimizations until Jose's backend rearchitecture completes
- UI standardization for filters and selectors to reduce user confusion
- Workspace URL privacy: obscuring IDs via encrypted cookies

**Content & SEO**
- Editorial improvements on category pages (H1 enhancements, descriptions)
- Building topic authority per brand hub
- Meta title tweaks driving positive CTR
- Decoupling workflows from ContentOS to avoid reliance on buggy system

---

## Summary

Strong organic growth momentum with 9% impressions increase and 1,000+ pages indexed, but cost management is critical—monthly spend at $150K with Gina alone consuming $45K. RE architecture simplification merged successfully, reducing technical debt. The many-to-many prompt system with 13,000+ prompts and new probing cadence aims to optimize operational costs. Onboarding flow remains the critical blocker for launch; frontend performance improvements deferred until Jose's rearchitecture completes.

---

## Decisions & Commitments

- **Cost visibility priority**: Daniel and Leo to build detailed expense tracking spreadsheet; split costs into two categories for line-by-line analysis
- **Onboarding unblock**: Schedule follow-up call with Marcel, Jose, and Daniel to review onboarding docs and clarify pricing strategy
- **Frontend optimization deferral**: Hold major PageSpeed fixes until Jose's rearchitecture concludes to avoid redundant work
- **Prompt management**: Implement 7-day warm-up probing period followed by frequency backoff based on prompt type and user plan
- **Editorial improvements**: Marcel to lead design/progression of category page enhancements for SEO with Carrie and Kavishka input
- **Workspace ID privacy**: Implement encrypted cookie solution to obscure IDs in URLs (Jacopo to implement)

---

## Open Questions

- What is the optimal pricing strategy for the onboarding flow (free vs. paid plan gating)?
- How should cost per service per prompt be calculated to inform feature gating?
- What is the timeline for Jose's backend rearchitecture completion?
- Should all proposed filters for UI standardization be universally shared, or can some be context-specific?
- How will the team monitor and validate the 7-day probing period effectiveness?

---

## Overview & Key Topics

- Organic SEO growth and strategy
- Cost management and expense tracking
- Architecture improvements (RE simplification, backend rearchitecture)
- Prompt management system optimization
- Onboarding flow and launch readiness
- Frontend performance and optimization
- Content and editorial improvements
- Privacy and security (workspace URL obscuring)

---

---

## Action Items

**Jose Farias** (CheckThat)
- Review Pedro's PR for many-to-many prompts and subcategories
- Drop an implementation plan for onboarding and clarify technical risks to unblock team
- Verify frontend PageSpeed indexes and loading performance post-backfill
- Provide timeline estimate for backend rearchitecture completion

**Pedro** (CheckThat)
- Handle conflict resolution and reapply UI standardization changes for filter bar and selectors
- Re-add pagination on brand logos in charts after Jose's refactor
- Continue fixing assigned bugs related to brand management and charts

**Stevie Kim** (CheckThat)
- Assign blockers and open tickets related to brand management and charts
- Investigate adding Groq to AI monitoring services and report findings
- Prepare and distribute next week's agenda earlier for team review
- Collaborate with editorial team to review and QA workspace tickets

**Daniel Lopes** (CheckThat)
- Build detailed expense tracking spreadsheet with Leo to split costs across tools and products
- Collaborate with Estevão on decoupling workflows from ContentOS pipelines
- Join Marcel and Jose for onboarding flow review call

**Estevão Mascarenhas** (CheckThat)
- Share existing workflows for page generation with Daniel

**Marcel Santilli** (GrowthX)
- Lead design and progression of editorial improvements on category pages for SEO
- Share monetization and pricing strategy documents with team for review
- Collect team input on onboarding flow pricing strategy and account setup
- Continue monitoring impressions, clicks, and SEO signals; share updates with team

**Jacopo Beschi** (CheckThat)
- Continue monitoring site performance and hold major optimizations until rearchitecture completes
- Monitor First Contentful Paint and Largest Contentful Paint metrics closely
- Implement encrypted cookie solution to obscure workspace IDs in URLs

---

## Transcript

**Marcel Santilli:** This meeting is being recorded. Hey everyone. How's it going? Everybody have a good Christmas?

**Pedro:** Lots of kids at home.

**Daniel Lopes:** Getting used to having the three boys running around the house on vacation.

**Marcel Santilli:** Nice. How's the new baby?

**Jose Farias:** Great. He might be getting sick—just a cold, minor stuff, but unfortunate timing.

**Stevie Kim:** Kids are kind of like the wild west.

**Marcel Santilli:** Good, good. I reorganized the meeting agenda a bit to see if the new structure works better.

**Stevie Kim:** Cool, yeah, I checked it out but didn't have time to see all the updates.

**Marcel Santilli:** No problem. Quick update before we jump in—really encouraging stuff so far. Our organic growth is looking solid. Impressions up about 9%, and we've surpassed 1,000 pages indexed.

**Jose Farias:** That's very encouraging—a big milestone to hit.

**Marcel Santilli:** Small things like meta title tweaks are definitely driving positive click-through. We're expecting this compounding effect to continue. We're really focused on building topic authority per brand hub.

**Daniel Lopes:** That's great momentum.

**Stevie Kim:** The organic growth is looking really green right now. But launch readiness is still in yellow status because onboarding and payment are still blockers.

**Daniel Lopes:** Yes. And there's a cost concern.

**Marcel Santilli:** We hit 150K on our ramp card. Gina alone is 45K of that. We really need to focus on cost visibility and optimization.

**Daniel Lopes:** Exactly. We need to split and track expenses across various scraping tools and products. I'm working with Leo to build a detailed expense tracking spreadsheet.

**Marcel Santilli:** Right. We want to split cost views into two categories for line-by-line analysis to quickly identify major drivers and address them.

**Jose Farias:** The RE architecture simplification is mostly merged. It's delivering substantial codebase simplification and fewer merge conflicts now.

**Daniel Lopes:** The main benefit is fewer bugs in the future due to removing multiple code paths. User-facing improvements will be minor—mostly slight speed gains.

**Pedro:** I completed the many-to-many prompts subcategories feature. Awaiting Jose's review for merging.

**Jose Farias:** Yes, I'll get to that right after this call. It's crucial for enhancing content management and prompt organization.

**Marcel Santilli:** Great. The prompt management workflow—we're looking at about 13,000 prompts with many-to-many relationships now.

**Stevie Kim:** Right. We proposed a warm-up probing period of 7 days for every new prompt, followed by backoff to reduced frequency based on prompt type and user plan.

**Marcel Santilli:** This manual control over probe frequency aims to significantly reduce operational costs.

**Jose Farias:** Sounds straightforward. Any team member could implement it.

**Daniel Lopes:** We also need to clarify cost per service per prompt to inform gating decisions for free vs. paid plans.

**Stevie Kim:** Estevão, can you share the existing workflows for page generation with Daniel?

**Estevão Mascarenhas:** Yes, I'll share those after this call.

**Daniel Lopes:** We should decouple workflows from ContentOS pipelines to avoid relying on that buggy system.

**Marcel Santilli:** Agreed. We want editors like Carrie and Kavishka to provide style and quality input to define what great content looks like.

**Pedro:** For category pages, we should lightly editorialize with enhanced H1s and descriptions to improve SEO without altering core features.

**Marcel Santilli:** Right. Every page should be one or two clicks away from key category and brand pages.

**Stevie Kim:** UI standardization for filters and selectors is underway. We're reducing user confusion from inconsistent placements.

**Jose Farias:** Some filters may not need to be universally shared. We should question each filter's necessity.

**Marcel Santilli:** The goal is layout uniformity rather than feature parity.

**Stevie Kim:** The onboarding flow is the largest upcoming work area with significant implications for user experience and conversion.

**Jose Farias:** I suggest we focus on implementing onboarding first before tackling billing and team workspace features.

**Marcel Santilli:** Agreed. Let's schedule a follow-up call to review the onboarding docs and unblock development.

**Jacopo Beschi:** Frontend performance is slow currently. First and Largest Contentful Paint metrics are poor.

**Marcel Santilli:** Jose, you're rewriting major parts of the frontend and backend architecture, right?

**Jose Farias:** Yes, that should help. Expected to conclude soon. Until then, we should defer major frontend fixes to avoid wasted work.

**Jacopo Beschi:** I'll continue monitoring but hold off on deep optimizations until the rearchitecture is complete.

**Marcel Santilli:** The public pages share many components with the private side, so improvements will benefit both.

**Marcel Santilli:** Lastly, there's the workspace URL structure issue—we're exposing sequence numbers.

**Jose Farias:** It's mostly aesthetic, but obscuring those IDs could improve social sharing.

**Marcel Santilli:** Free accounts could be used to monitor workspace creation numbers, revealing growth rates publicly. That's a privacy concern.

**Jacopo Beschi:** We could obscure this via encrypted cookies without heavy rearchitecture.

**Marcel Santilli:** Good idea. Jacopo, can you tackle moving workspace IDs to encrypted cookies?

**Jacopo Beschi:** Yes, I can add that to my list.

**Marcel Santilli:** Great. Let's keep monitoring our organic growth metrics closely.
