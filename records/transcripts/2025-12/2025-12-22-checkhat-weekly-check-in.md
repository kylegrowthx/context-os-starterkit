# CheckThat Weekly Check In

<metadata>
date: 2025-12-22
time: 18:00 UTC
duration: 36 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Estevão Mascarenhas, Jacopo Beschi, Jose Farias, Pedro, Daniel Lopes, Stevie Kim, Jason Gong, Jose Farias, Leonardo
fireflies_id: 01KCMP5SWN5RBEN1S0K2PCHMT8
transcript_url: https://app.fireflies.ai/view/01KCMP5SWN5RBEN1S0K2PCHMT8
</metadata>

---

## Summary

The team confirmed organic growth as the top priority to sustain operations given high monthly costs of approximately $200,000. A massive jump in impressions over the last 24 hours outpaced the entire prior week, with clicks rising to 2-3 per day, showing that small meta title changes drive user engagement and positive SEO signals. Focus remains on improving the end-to-end customer experience including onboarding, content management, data visualization clarity, and loading performance. The prompt management system with over 13,000 prompts needs better organization to streamline onboarding. Frontend performance is a key priority for SEO rankings and user perception, with monitoring ongoing while major optimizations are deferred until Jose's rearchitecture merge completes. URL structure and workspace ID exposure present privacy and competitive risks, with cookie encryption proposed as a quick fix.

---

## Action Items

**Jose Farias**
- Add status updates related to data vitrologies and visualizations during next meeting

**Stevie Kim**
- Prepare and distribute next week's agenda earlier for team review and input
- Collaborate with editorial team to review and QA workspace tickets (Rex, Galileo, Airbyte, others)

**Marcel Santilli**
- Share links to monetization and pricing strategy documents for team review
- Collect team input on onboarding flow pricing strategy and optimal account setup processes
- Continue monitoring impressions, clicks and SEO signals, share updates with team

**Jacopo Beschi**
- Monitor frontend performance metrics, especially first and largest contentful paint, document observations but defer optimization until Jose's rearchitecture merge
- Implement encrypted cookie solution to obscure workspace IDs in URLs, enhancing privacy and preventing workspace-count exposure

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
