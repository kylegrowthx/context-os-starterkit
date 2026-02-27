# CheckThat Weekly Check In

<metadata>
date: 2025-12-29
time: 18:00 UTC
duration: 49 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Estevão Mascarenhas, Jacopo Beschi, Jose Farias, Pedro, Daniel Lopes, Stevie Kim, Jason Gong, Jose Farias, Leonardo, Leonardo
fireflies_id: 01KD3KPN73XC8KZSH5XHCEF3E6
transcript_url: https://app.fireflies.ai/view/01KD3KPN73XC8KZSH5XHCEF3E6
</metadata>

---

## Summary

The team discussed strong organic growth with a 9% increase in impressions and over 1,000 pages now indexed, indicating strong momentum. Cost management emerged as a critical concern with monthly spending reaching $150,000, with Gina accounting for $45,000. The RE architecture simplification has been mostly merged, improving codebase maintainability with fewer expected bugs. The prompt management system with many-to-many relationships and 13,000+ prompts needs better organization. The onboarding flow remains a blocker pending input on pricing strategy. Frontend performance improvements are a priority, with the team deferring optimizations until Jose's rearchitecture is complete to avoid redundant work.

---

## Action Items

**Jose Farias**
- Review Pedro's PR for many-to-many prompts and subcategories after the call
- Drop an implementation plan for onboarding and unblock the team by clarifying technical risks
- Verify frontend PageSpeed indexes and loading performance post-backfill
- Add status updates related to data vitrologies and visualizations during next meeting

**Pedro**
- Handle conflict resolution and reapply UI standardization changes for filter bar and selectors
- Re-add pagination on brand logos in charts after Jose's refactor
- Continue fixing assigned bugs especially related to brand management and charts

**Stevie Kim**
- Assign blockers and open tickets related to brand management and charts
- Investigate adding Groq to AI monitoring services and report back
- Prepare and distribute next week's agenda earlier for team review and input
- Collaborate with editorial team to review and QA workspace tickets

**Daniel Lopes**
- Collaborate with Estevão on decoupling workflows from ContentOS pipelines for page generation
- Join Marcel and Jose for onboarding flow review call

**Estevão Mascarenhas**
- Share existing workflows for page generation with Daniel

**Marcel Santilli**
- Lead design and progression of editorial improvements on category pages for SEO
- Share links to monetization and pricing strategy documents for team review
- Collect team input on onboarding flow pricing strategy and optimal account setup processes
- Continue monitoring impressions, clicks and SEO signals, share updates with team

**Jacopo Beschi**
- Continue monitoring site performance and finalize frontend fixes for PageSpeed optimization
- Monitor frontend performance metrics, especially first and largest contentful paint
- Implement encrypted cookie solution to obscure workspace IDs in URLs

---

## Transcript

**Marcel Santilli:** This meeting is being recorded. Hello. How's it going?

**Jose Farias:** Hey. Morning.

**Marcel Santilli:** How y'all doing?

**Jose Farias:** Yes.

**Marcel Santilli:** Everybody have a good Christmas?

**Pedro:** Lots of kids at home.

**Daniel Lopes:** Getting used to having the three boys running around the house on vacation.

**Marcel Santilli:** Nice. How's the new baby?

**Jose Farias:** Great. He might be getting sick, which is the news today. Just like a cold, minor stuff, but unfortunate timing.

**Stevie Kim:** Kids is kind of like the wild west. It's impossible to.

**Marcel Santilli:** Good, good. I messed around with the meeting agenda a little bit just to organize it slightly different to see if it works well.

**Stevie Kim:** Okay, cool. Yeah, I checked it out, but I didn't have time to see all the new updates.

**Marcel Santilli:** All good. But quick update maybe before we jump in. I know folks saw some results but really encouraging stuff so far.

**Marcel Santilli:** So quick update on organic. We're really in a good place. Impressions up about 9%. Surpassed like over 1000 pages indexed.

**Jose Farias:** That's very encouraging and a big milestone to hit.

**Marcel Santilli:** Yeah. Yeah. It's like small things like meta title tweaks are definitely driving like a positive click through. And we're expecting this compounding effect to continue.

**Daniel Lopes:** That's great momentum.

**Marcel Santilli:** So we're really focused on like building topic authority per brand hub.

**Stevie Kim:** So the organic growth is looking really green right now. But launch readiness I'd say is still in yellow status because onboarding and payment are still blockers.

**Daniel Lopes:** Yes. And there's a cost concern.

**Marcel Santilli:** Yeah. We hit 150K on our ramp card. Gina alone is 45K of that. So we really need to focus on cost visibility and optimization.

**Daniel Lopes:** Exactly. We need to split and track expenses across various scraping tools and products. I'm working with Leo to build a detailed expense tracking spreadsheet.

**Marcel Santilli:** Yes. So we want to split cost views into two categories for line-by-line analysis to quickly identify major drivers and address them.

**Jose Farias:** The RE architecture simplification is mostly merged. Delivering substantial codebase simplification and fewer merge conflicts now.

**Daniel Lopes:** The main benefit is fewer bugs in the future due to removing multiple code paths. User-facing improvements will be minor, mainly slight speed gains.

**Pedro:** I completed the many-to-many prompts subcategories feature. Awaiting Jose's review for merging tomorrow.

**Jose Farias:** Yes, I'll get to that right after this call. It's crucial for enhancing content management and prompt organization.

**Marcel Santilli:** Great. And the prompt management workflow... we're looking at about 13,000 prompts with many-to-many relationships now.

**Stevie Kim:** Right. We proposed a warm-up probing period of 7 days for every new prompt, followed by backoff to reduced frequency based on prompt type and user plan.

**Marcel Santilli:** This manual control over probe frequency aims to significantly reduce operational costs.

**Jose Farias:** Sounds straightforward. Any team member could implement it.

**Daniel Lopes:** We also need to clarify cost per service per prompt to inform gating decisions for free vs. paid plans.

**Stevie Kim:** And Estevão, can you share the existing workflows for page generation with Daniel?

**Estevão Mascarenhas:** Yes, I'll share those after this call.

**Daniel Lopes:** We should decouple workflows from ContentOS pipelines to avoid relying on that buggy system.

**Marcel Santilli:** Agreed. We want editors like Carrie and Kavishka to provide style and quality input to define what great content looks like.

**Pedro:** And for category pages, we should lightly editiorialize with enhanced H1s and descriptions to improve SEO without altering core features.

**Marcel Santilli:** Right. Every page should be one or two clicks away from key category and brand pages.

**Stevie Kim:** UI standardization for filters and selectors is underway. We're looking at reducing user confusion from inconsistent placements.

**Jose Farias:** Some filters may not need to be universally shared. We should question each filter's necessity.

**Marcel Santilli:** The goal is layout uniformity rather than feature parity.

**Stevie Kim:** The onboarding flow is the largest upcoming work area with significant implications for user experience and conversion.

**Jose Farias:** I suggest we focus on implementing onboarding first before tackling billing and team workspace features.

**Marcel Santilli:** Agreed. Let's schedule a follow-up call to review the onboarding docs and unblock development.

**Jacopo Beschi:** Frontend performance is slow currently. First and largest contentful paint metrics are poor.

**Marcel Santilli:** Jose, you're rewriting major parts of the frontend and backend architecture, right?

**Jose Farias:** Yes, that should help. Expected to conclude soon. Until then, we should defer major frontend fixes to avoid wasted work.

**Jacopo Beschi:** I'll continue monitoring but hold off on deep optimizations until the rearchitecture is complete.

**Marcel Santilli:** The public pages share many components with the private side, so improvements will benefit both.

**Marcel Santilli:** Lastly, there's the workspace URL structure issue where we're exposing sequence numbers.

**Jose Farias:** It's mostly aesthetic but obscuring those IDs could improve social sharing.

**Marcel Santilli:** Free accounts could be used to monitor workspace creation numbers, revealing growth rates publicly. That's a privacy concern.

**Jacopo Beschi:** We could obscure this via encrypted cookies without heavy rearchitecture.

**Marcel Santilli:** Good idea. Jacopo, can you tackle moving workspace IDs to encrypted cookies?

**Jacopo Beschi:** Yes, I can add that to my list.

**Marcel Santilli:** Great. So let's keep monitoring our organic growth metrics closely.
