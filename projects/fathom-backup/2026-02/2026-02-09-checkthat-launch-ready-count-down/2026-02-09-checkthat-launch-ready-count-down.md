# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-09
time: 16:01 UTC
duration: 28 minutes
organizer: stevie@growthx.ai
participants: Estevão Mascarenhas, Marcel Santilli, Jason Gong, Jose Farias, Pedro Steimbruch, Daniel Lopes, Leonardo Carpenedo Steffen, Stevie Kim
fathom_recording_id: 120810692
fathom_url: https://fathom.video/calls/559090219
share_url: https://fathom.video/share/tHsE8De5YNFv8g5K4F2cxF1izJYsfo-C
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

The team finalized subcategory feature launch (PR merging tomorrow), confirmed performance parameters are acceptable, and identified prompt relevance as a critical user pain point requiring a recommendation engine. Analytics dashboards are live and a list of active users is ready for feedback outreach, enabling a data-driven product improvement cycle.

---

## Context

CheckThat is preparing for a major product milestone with the subcategory feature—allowing users to change their category assignments post-onboarding. The team spent significant time evaluating performance risks from the backfill process, ultimately deciding to proceed with the current implementation after confirming average prompt counts. In parallel, user feedback revealed a systemic issue: categories like "healthcare" are too broad, leading to irrelevant prompt recommendations for niche users like ASC software practitioners. This validates the strategic importance of a prompt recommendation engine that leverages brand context (personas, product info) rather than relying solely on better categorization. The team is also operationalizing analytics for product-led growth: PostHog dashboards tracking user stickiness and activation are now live, and they've identified the top 18 most active users from the last 14 days for targeted feedback interviews.

---

## Relevance

- **Product Development:** Subcategory feature launch timing, performance risk mitigation, prompt relevance as core product gap
- **User Feedback:** Intercom customer reveals niche category problem; identifies need for smarter prompt recommendations over better categorization
- **Analytics & Metrics:** PostHog dashboards live; vanity metrics filtered out in favor of actionable metrics; user stickiness cohort tracking now available
- **Team Execution:** Clear action items on brand flagging cleanup, cadence work completion, analytics sharing across team
- **Strategic Priority:** Tension between supporting long-tail categories (healthcare, niche verticals) vs. core market focus; to be discussed in cross-functional meeting

---

## Overview

- **Subcategory Feature Merging Tomorrow:** The new subcategory feature will merge tomorrow, enabling users to change categories post-onboarding. The implementation will *not* deactivate old prompts, a decision made to preserve user work and avoid data loss.
- **Performance Risk Mitigated:** The feature's backfill process poses a performance risk (high latency, DB load). The team will proceed after confirming average prompt counts are low, deferring a complex async solution for now.
- **Prompt Relevance is a Critical Issue:** A user's feedback ("irrelevant prompts") highlights a core problem: the current category system fails niche users. The proposed solution is a prompt recommendation engine, not just better categorization.
- **New Analytics & Feedback Pipeline:** PostHog dashboards are live for key metrics (e.g., user stickiness), and a list of active users is ready for feedback outreach, creating a new data-driven feedback loop.

---

## Key Topics

### Subcategory Feature & Performance Risk

  - The subcategory feature PR is in review and will merge tomorrow.
  - **Implementation:** New subcategories activate prompts from the library; old prompts are *not* deactivated.
  - **Performance Risk:** The backfill process is synchronous, creating a risk of high latency and DB load if a user activates many subcategories with hundreds of prompts each.
  - **Decision:** Proceed with the current implementation after confirming average prompt counts are low. This defers a more complex async solution (e.g., `perform_all_later`) for now.
  - **Context:** A recent bug fix (merged) correctly persists the *primary* category during onboarding, resolving a data integrity issue.

### Prompt Relevance & User Feedback

  - A user's Intercom feedback ("irrelevant prompts") highlighted a critical issue: the current category system fails niche users (e.g., "ASC software" in healthcare).
  - **Root Cause:** The user's category ("healthcare") is too broad, leading to a poor prompt experience.
  - **Proposed Solution:** A prompt recommendation engine, leveraging existing brand context (personas, product info), to suggest highly relevant prompts. This is seen as more valuable than just better categorization.
  - **Strategic Question:** How much development time should be invested in supporting long-tail categories? This will be discussed in the cross-functional meeting.
  - **Action:** Stevie will update the "prompt recommendation" ticket with this user feedback to boost its priority.

### Analytics & User Feedback Pipeline

  - New PostHog dashboards are live, focusing on actionable metrics over vanity metrics.
      - **Key Dashboard:** User stickiness (day 1, 2, 3 return rates).
  - A list of the top 18 active users from the last 14 days is ready for feedback outreach.
  - **Action:** Share all new dashboards and insights with the team to prevent duplicated work.

### Other Dev Updates

  - **Brand Flagging:** A new admin flag identifies \~30 brands with incomplete profiles.
      - **Tomorrow's Tasks:** Add a manual unflag option and improve name-matching logic to reduce false positives.
  - **Cadence Work:** Jose is working on this, targeting completion by tomorrow.
  - **Sources Page:** Jacopo will resume optimization after pagination is re-added.

---

## Action Items

**Pedro Steimbruch**
- Run numbers on prompts/subcat; enforce cap; merge categorization PR; then run visibility-prompts backfill
- Add manual unflag on brand show; improve name matching for overview flags
- Backfill brand perception citation rate

**Stevie Kim**
- Review prompt-recommendation ticket; assign to Pedro; add Intercom healthcare feedback

**Jose Farias**
- Fix Intercom notification dings

---

## Transcript

### Subcategory Feature & Performance Risk

**Jose Farias:** Again, you've merged that, right?

**Pedro Steimbruch:** The categorization feature, the ability to change it—I didn't merge it yet. It's in review.

**Pedro Steimbruch:** I was checking the Friday conversation. I noticed you mentioned doing a visibility-prompts backfill when categorization changes.

**Jose Farias:** Right, we need to look at the bulk update endpoint for activating prompts from the library.

**Pedro Steimbruch:** My concern is if a user enables 10 subcategories, we could potentially create a thousand prompt activations in a single endpoint request. That should be capped. But even with a cap on subcategories, we could have 200 prompts per subcategory, creating 500+ backfills in a single request.

**Pedro Steimbruch:** We have two issues: a lot of backfills happening and high latency for the request because we're doing so many database commits.

**Jose Farias:** Let's just run some numbers on how many prompts we actually have per subcategory on average. I think we'll be fine. The system should eventually handle constant backfilling, but we're not there yet—it's a hard problem. For now, let's get a sense of the actual prompt counts, and if there aren't that many, we can just merge.

**Pedro Steimbruch:** I'll merge tomorrow after addressing review comments.

**Jose Farias:** That's fine. The bigger bug was the one you already fixed. Since we merged that, it's fine to merge tomorrow.

**Jose Farias:** For context, Pedro found a bug where we weren't persisting the primary category during onboarding. We were copying subcategorizations but not marking which was the primary category.

**Stevie Kim:** Is that why I kept seeing that bug?

**Jose Farias:** No, different bug. Yours was purely visual—the data was correct, but we were displaying the wrong category. This one Pedro fixed, the data was actually wrong.

**Jose Farias:** The feature going out tomorrow lets users change subcategories from the dashboard. We're not deactivating any previous prompts.

**Stevie Kim:** We're all in agreement that was the right approach. So do we need to discuss that doc in the cross-functional meeting with Marcel and Daniel?

**Jose Farias:** I think some of this is still worth discussing. There are tensions here. Miscategorizing shouldn't happen ideally, but Daniel will probably say it's inevitable with LLMs—and I agree. The strategic question is: how much do we care about long-tail categories like healthcare? Maybe the product just isn't geared towards them. But we should still make it useful if possible. Let's bring it up when we discuss your document.

### Prompt Relevance & User Feedback

**Pedro Steimbruch:** We got interesting Intercom feedback today from a user who manages ASC (Ambulatory Surgery Centers) software—a healthcare IT niche. He said the closest category is "healthcare," but a lot of prompts are irrelevant. He specifically wanted an ASC software category.

**Pedro Steimbruch:** His feedback is that he's only seeing irrelevant prompts. But we have good context on his company—personas and brand info. We can solve this by suggesting specific prompts, not just better categorization. It's more valuable to recommend the right prompts themselves.

**Stevie Kim:** We have a ticket for recommended prompts, but that's more about custom prompts to help them upgrade tiers. But what you're saying makes sense. Let me look at our prompt recommendation ticket—when I was busy, I sometimes just put placeholders in. I'll make sure it has real information.

**Stevie Kim:** I'll look at the ticket and see what we need. I can assign it to Pedro and you can add this Intercom feedback so we track it and prioritize it properly.

**Jose Farias:** Let's bring up the long-tail strategy question. How much development time should we invest in supporting niche categories like healthcare?

**Stevie Kim:** Healthcare is tough because we also need to think about how well our GrowthX team can perform on that category. We had constraints with Biologica and other enterprise clients that had difficult requirements.

**Pedro Steimbruch:** I'm not focused on healthcare specifically. I'm more interested in this user's feedback. If we have good brand context—product features, personas—we should suggest good prompts for him.

**Stevie Kim:** We want him to create custom prompts for his use case. But if we recommend 15 library prompts that are actually useful, he'd be happy. That's out of scope for the subcategory conversation, but it pushes the need for the prompt recommendation feature.

### Operational Updates & Analytics

**Jose Farias:** I've started the cadence work and should have it done today or early tomorrow.

**Jose Farias:** Do we know when the next announcement is going out? We bought newsletter sponsorships, so I'm bracing for an influx of users.

**Stevie Kim:** I haven't been on Slack yet. Here's a note on Intercom: keep it open in your browser and it'll give you a notification ding. It's unique, so you can't mistake it for other notifications. Please jump on it anytime.

**Jose Farias:** I have it open but it's not dinging. I'll figure that out.

### Brand Flagging & Admin Tools

**Pedro Steimbruch:** I pushed a flag for brands without profiles or brand names in the admin brands page. You'll see about 30 flagged brands that you can now filter for.

**Pedro Steimbruch:** Tomorrow I'll add two improvements: a way to manually unflag brands on the brand show page, and improved name matching for the overview flags. More than half of the flagged brands have empty profiles, so deep research should help.

**Pedro Steimbruch:** I've also changed the brand perception citation rate. I'm not pressed on time since we're not using it yet—I'll backfill that tomorrow.

### Analytics Infrastructure & User Feedback Pipeline

**Pedro Steimbruch:** I explored PostHog MCP—it's amazing. I extracted the top 18 active users from the past 14 days who are good candidates for feedback outreach via email.

**Stevie Kim:** I haven't thought much about how we'll do deeper contextual interviews with customers. I typically work with customer success since I have existing relationships from enterprise work. This will be a different approach, but it's good to have those deeper conversations about what they're trying to achieve.

**Stevie Kim:** Any dashboards you make, please share them with the whole team and any insights. Let's make sure we're not duplicating work and have eyes on everything.

**Pedro Steimbruch:** I shared a Notion doc with the dashboards over the weekend. Today I did another iteration, trying to identify actionable metrics instead of vanity metrics.

**Pedro Steimbruch:** It's implemented in PostHog with four dashboards. There's a nice feedback Notion document we can implement into PostHog, and Claude can probably automate it all.

**Stevie Kim:** I have about four visualizations in the product analytics dashboard already. We could consolidate or create separate dashboards depending on what they track. Marcel will probably want reports.

**Pedro Steimbruch:** The interesting cohort metric shows: if users sign up today, are they coming back in day 1, 2, 3? That gives us good stickiness understanding.

**Stevie Kim:** I had a stickiness dashboard but removed it after talking to Daniel—we need to focus on activation vs. engagement right now. We'll definitely do cohorts and engagement later. PostHog docs are really good.

**Jose Farias:** Just a note: Jacopo is holding off on optimizing the sources page until we add pagination back. Just let him know whenever that's ready.

**Pedro Steimbruch:** Yeah, I think it's with him already.
