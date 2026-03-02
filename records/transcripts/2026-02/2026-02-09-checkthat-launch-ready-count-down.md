# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-09
time: 16:01 UTC
duration: 28 minutes
organizer: Stevie Kim
participants: Stevie Kim, Jose Farias, Pedro Steimbruch, Estevão Mascarenhas, Leonardo Carpenedo Steffen, Marcel Santilli, Daniel Lopes
fathom_recording_id: 120810692
fathom_url: https://fathom.video/calls/559090219
share_url: https://fathom.video/share/tHsE8De5YNFv8g5K4F2cxF1izJYsfo-C
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

The CheckThat team finalized launch readiness with three critical outcomes: merging the subcategory feature tomorrow (which allows users to change categories post-onboarding without deactivating previous prompts), confirming the performance risk is manageable after Pedro runs prompt count analysis, and identifying a urgent problem through user feedback—niche categories like "ASC software" in healthcare are returning irrelevant prompts. The team is pivoting toward building a prompt recommendation engine (leveraging existing brand context, personas, and product info) as the core solution, and Stevie will update the ticket and discuss long-tail category support strategy with Marcel and Daniel in an afternoon cross-functional meeting.

---

## Context

This is the CheckThat product team's stand-up focused on launch readiness for the subcategory feature and critical product issues discovered through user feedback. The team includes GrowthX engineers (Pedro, Jose, Leonardo, Estevão) and product leadership (Stevie), with observers from GrowthX leadership (Marcel) and the broader product team (Daniel). The discussion surfaces a core tension in CheckThat's design: the category system is broken for niche users, affecting both user retention and willingness to upgrade—this has become a priority issue as the product scales and receives more real-world usage.

---

## Relevance

**To CheckThat Product:**
- Subcategory feature launches tomorrow (pending prompt count validation). Reduces user friction by allowing post-onboarding category changes without data loss.
- **Critical insight:** User feedback reveals niche-category problem is not just categorization but prompt relevance. Recommendation engine (using brand context, personas, product info) is higher leverage than better categorization alone.
- PostHog dashboards now live with actionable metrics (day 1/2/3 return rates for user stickiness cohorts). List of top 18 active users ready for feedback outreach—creates new data-driven loop.
- Brand flagging system deployed: ~30 brands with incomplete profiles. Manual unflag UI and name-matching improvements coming tomorrow.

**To GrowthX Delivery:**
- Healthcare may be a long-tail category requiring strategic decision on investment level. Daniel's perspective on LLM mistakes and category coverage will inform resource allocation.

**To GrowthX Business Development:**
- Strong usage signals: new users returning day 1/2/3. Newsletter sponsorships announced (dates TBD)—expect user influx requiring support readiness.
- Intercom feedback loop established; Stevie will field requests and escalate to product. Healthcare user (Intercom contact) is a reference candidate if recommendation engine solves the problem.

---

## Decisions & Commitments

- **Subcategory Feature:** Will launch tomorrow. Does not deactivate old prompts (preserves user work and data). Decision made to avoid user confusion and data loss risk.
- **Performance Risk Mitigation:** Proceed with current synchronous implementation after Pedro confirms average prompt counts are low. Defer async solution (`perform_all_later`) for future iteration.
- **Prompt Relevance Solution:** Prompt recommendation engine (not just better categorization) is the strategic priority. Will leverage existing brand context, personas, and product info to suggest highly relevant prompts.
- **Cross-Functional Discussion:** Strategy on long-tail category investment (e.g., healthcare) will be discussed in afternoon meeting with Marcel and Daniel. Key question: How much development time should CheckThat invest in supporting niche categories?

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

  - **Brand Flagging:** A new admin flag identifies ~30 brands with incomplete profiles.
      - **Tomorrow's Tasks:** Add a manual unflag option and improve name-matching logic to reduce false positives.
  - **Cadence Work:** Jose is working on this, targeting completion by tomorrow.
  - **Sources Page:** Jacopo will resume optimization after pagination is re-added.

### Analytics & Feedback Outreach

  - **PostHog Dashboards Live:** New dashboards focus on actionable metrics (user stickiness cohorts: day 1, 2, 3 return rates).
  - **User Feedback Campaign:** List of top 18 active users from past 14 days ready for email outreach to gather feedback.

---

## Open Questions

- How much development time should CheckThat invest in supporting long-tail / niche categories (e.g., healthcare ASC software)? Will be discussed in cross-functional meeting with Marcel and Daniel.
- Are average prompt counts per subcategory low enough to safely proceed with synchronous backfill, or do we need an async solution?

---

## Action Items

**Pedro Steimbruch (GrowthX)**
- Run numbers on prompts per subcategory; enforce cap in categorization PR; then run visibility-prompts backfill
- Add manual unflag option on brand show page; improve name-matching logic for overview flags
- Backfill brand perception citation rate

**Stevie Kim (GrowthX)**
- Review prompt-recommendation ticket; assign to Pedro; add Intercom healthcare customer feedback to prioritize

**Jose Farias (GrowthX)**
- Fix Intercom notification dings (currently not pinging/alerting on new messages)

---

## Transcript

**Pedro Steimbruch:** Thank you.

**Jose Farias:** Again, you've merged that, right?

**Pedro Steimbruch:** The categorization, the ability to change it, I didn't. It's in review yet.

**Jose Farias:** Oh, okay.

**Pedro Steimbruch:** I was just checking the conversation you guys had on Friday. I missed that. And I noticed you mentioned it would be good to do the onboarding backfill again. When the categorization changes, I want you to review how I'm doing the backfill. Maybe I can just throw an onboarding backfill there.

**Jose Farias:** I think not the onboarding. The visibility prompts change. I made a mistake saying onboarding.

**Pedro Steimbruch:** Sorry about that. Yeah, I'm doing the visibility changes, but I also need to do some prompt performance work.

**Jose Farias:** Right, so we would take a look at the bulk update endpoint for archiving and activating prompts.

**Pedro Steimbruch:** Not archiving, activating from the library is what I meant. Yeah, I think I checked that and the way it does, it iterates and does the single. And I did that, that's the way it's implemented in PR if you check it. But my concern is if the user enables 10 subcategories, then we can do potentially a thousand creations in a single endpoint request. It should be capped.

**Jose Farias:** Stevon implemented a cap that I don't know if we're enforcing. We should enforce that in this PR as well if we're not yet.

**Pedro Steimbruch:** Okay.

**Jose Farias:** That way you can't add that many subcategories.

**Pedro Steimbruch:** Yeah, but we can still have, let's say, 200 prompts in a subcategory, and then we will have the same issue there. Because then we are creating like 500 backfills in a single request. We have two issues: a lot of backfills happening that may be an issue or not. And the second issue is that the latency for the request will be high, right? Because we're doing so many commits to the database.

**Jose Farias:** There's a perform_all_later method in active job.

**Pedro Steimbruch:** But even with that, because we are creating backfills at that point. That's my concern.

**Jose Farias:** Let's just run some numbers, see how many prompts we actually have per subcategory on average. I think we'll be fine. The system should be able to evolve to eventually handle constant backfilling. We're not there yet. It's a hard problem. But eventually we should be able to get there. So I think for now, let's get a sense of how many prompts there actually are. And if there aren't that many, I think we can just merge.

**Pedro Steimbruch:** Okay. I will only merge tomorrow, if that's okay. I need to address some of the PR comments and I will leave after the call.

**Jose Farias:** I think the bigger bug was the one that you already addressed. So I think since we merged that, it's fine to merge tomorrow.

**Pedro Steimbruch:** Yeah. I felt the same.

**Jose Farias:** For context, Pedro found a bug where we weren't persisting the primary category as primary. When onboarding, you create a workspace, you follow a brand, we weren't copying the brand's categorizations the same. We were copying the subcategorizations, but not the primary part.

**Stevie Kim:** Is that why I kept seeing that bug?

**Jose Farias:** No. The one that you're referencing is the one in the overview page, where you had a different subcategory than the one that you made primary in your onboarding. That was purely visual. The data was correct. It was just displaying the wrong thing. And then this bug that Pedro just fixed, the data was actually wrong.

**Stevie Kim:** You had different primary category altogether?

**Jose Farias:** It was still one of the ones that you picked. It's just, it wasn't the primary one. But he's fixed that. And that's the big one.

**Stevie Kim:** Okay, nice.

**Jose Farias:** And then the one that's going to go out tomorrow is not a bug, more like a feature—being able to change your subcategories from the dashboard. And for the record, we haven't merged yet, but Pedro and I had a conversation about this. We are going with the version where you don't deactivate any previous prompts.

**Stevie Kim:** Okay. That's fine, right? I think we're all in agreement that that was the way to go.

**Jose Farias:** Yeah.

**Stevie Kim:** So do you guys think that we even need to discuss that doc I started for the cross-functional meeting later today with Marcel and Daniel?

**Jose Farias:** Let me read that again because I just skimmed over it.

**Stevie Kim:** Yeah. I mean, it just kind of encompasses the thoughts everyone had. I just really wanted to get the problems and scenarios in place so we didn't miss anything.

**Jose Farias:** I think some of this is still worth discussing. There's still some tensions here. Miscategorizing in general shouldn't happen. It's great that they can change it, but ideally, that shouldn't be necessary. I think Daniel's opinion on that will be that it's inevitable, and I tend to agree. LLMs will make mistakes inevitably. And then not having suitable categories—we need a flow for that.

**Stevie Kim:** You know, it's debatable, because you can get away with it through competitors. If we had the ability to tag competitors, then it would be a lot easier. And I do have a ticket for that because that's necessary if you're trying to filter by specific product lines. But right now they have to contact us through support saying, "hey, I need help." And that's not going to be the greatest experience because a lot of people won't bother. If they don't see a category during onboarding, they'll just think, "oh, this doesn't apply to me. I don't belong here." And then they'll bounce.

**Pedro Steimbruch:** Yeah, I have something to add on that. Today we received an interesting contact on Intercom. It was a user with clinics—healthcare IT software. They said, "Please make key categories for healthcare IT software. The closest is healthcare, and a lot of the prompts are irrelevant. Specifically, I would like an ASC software category." It's a niche for healthcare IT ASC software. And then we always get wrong subcategorizations, right? It's inevitable. But his feedback is that he's only seen irrelevant prompts. So I think it becomes pressing for us to address this because I checked, and we have good context on his company. We have personas. So we can solve that by suggesting prompts, right? It's not just a subcategorization. The prompts themselves are more valuable.

**Stevie Kim:** Oh, for sure. It trickles down. Yeah. And we have a ticket for recommended prompts. But those were more around recommended custom prompts. Because, obviously, we want to encourage them to create more custom prompts. Because that is the lever to switch tiers. But so you're saying if we could recommend better prompts? Is healthcare in the niche category?

**Pedro Steimbruch:** I'm not sure.

**Stevie Kim:** I was just wondering why it was so irrelevant. Because like, if we get the subcategories and the right categories, you'd think that some of the prompts would be fairly relevant, even if they weren't super specific. So basically, I'm trying to figure out where the line is. Useful library prompts need to be useful to a certain degree. But the reason for custom prompts is for them to create those specific prompts for their use case and company product so they can really track how they're showing up.

**Jose Farias:** It is in the niche category. Think strategically. There's a strategic angle to this. How much do we care? How much in the long tail is healthcare, for example? Maybe the product just isn't geared towards them. And of course, we should still be able to make it useful to them, but I don't know how much time is worth investing in making it as seamless as the other categories. Healthcare is a big one, but other categories might not be as relevant. Let's just bring it up when we discuss your document, Stevie. This is a good call out, Pedro.

**Stevie Kim:** Healthcare is a tough one because we also want to think about how well our GrowthX team can perform on that specific category. How well can we execute?

**Jose Farias:** Like Biologica and CHURN—we didn't do well.

**Stevie Kim:** They had a lot of specific requirements that were difficult to execute on. We do have certain constraints on how well we perform.

**Pedro Steimbruch:** I'm not referring to healthcare specifically. I'm more interested in his feedback. The issue is that he doesn't find the prompts he's seeing relevant for his brand. But we have good context on his brand. We have personas. The categorization can be a bit misleading. But if we have good context overall—brand context, product and features, and personas—then we should be able to suggest good prompts for him.

**Stevie Kim:** Well, we want him to create those custom prompts, so we can suggest those custom prompts.

**Pedro Steimbruch:** Yeah, because if he's on healthcare and the library prompts are kind of useless for him, but if we came up with, let's say, 15 prompts that he said, "Oh, that's so cool, these 15 prompts are what I'm looking for," then he's happy.

**Stevie Kim:** Yeah, that's out of scope for the subcategory conversation. I was trying to keep the prompts out of it because we do have separate tickets to tackle those issues. We already have the prompt recommendation ticket. But it does push the need. I'll definitely look at it and see what we need. And I can assign it to you if you want, and you can put that feedback from the Intercom customer in that ticket so we can track that and it helps us prioritize. And yeah, maybe after we get the subcategory thing and some tagging I was talking about—which would help give a lot more flexibility in how they're viewing their data—we can look at that and tackle it because it'll help them create more custom prompts, find more usefulness, and upgrade.

**Jose Farias:** Cool. I guess I'll give my stand-up update. I have started on the cadence work, working on it still. I think I should be able to have it done either today or early tomorrow. Someone answered unanswered questions there, but I don't think anything too daunting. If anything, I'll just post it in the chat. And I think that's it for me today.

**Jose Farias:** Do we know when another announcement is going to go out? I know we bought some newsletter sponsorships. So just bracing for another influx of users.

**Stevie Kim:** I do not know. I haven't been on Slack yet today. So that's news. The newsletters are news to me.

**Stevie Kim:** Here's the deal with Intercom. I just keep it open in my browser and it'll give you an annoying notification ding. It's a unique sound, so you can't mistake it for like a Google notification. So anytime you hear that and you're not heads down on something, please jump on. Thank you.

**Jose Farias:** I have it open, but it's not dinging.

**Jose Farias:** I'll figure that out.

**Stevie Kim:** Yeah. I'm just going to be catching up on everything probably for the first half of the day. And yeah, I'll look at that ticket for the prompt. I'll assign it to Pedro and make sure it's got some content. When we were really busy, I started putting placeholders in tickets instead of real information. I'll make sure there's some information in there. And just let me know if you guys need any help with prioritization or anything like that. I might also review the P1s to make sure that makes sense for us to work on before some of the other things.

**Pedro Steimbruch:** Yeah, I pushed the flag for brands without profile or without the brand name in the profile and overview. If you check the admin brands, you'll see there is a warning with about 30 flagged brands. You can filter for flagged brands. Tomorrow I will add a way to manually unflag a brand in the brand show page. More than half of these brands have empty profiles, so running a deep research on them should be enough. I also need to improve the name matching to the overview because I identified a few flagged brands that are being flagged for a brand not mentioned in the overview, but they are actually being mentioned. Everything is for tomorrow. I changed the brand perception citation rate. Jose, we discussed that last week. I'm not pressed on time there because we are not using it yet. I'll probably do that tomorrow. I also got feedback from Intercom that I thought was interesting, and I did some work with PostHog MCP. I was extracting the active users for the past 14 days that are good candidates for us to reach out to through email asking for feedback. We have the last 18 active users. I think we have a couple of users that interacted a lot with the product already, so might be good to check in and ask for feedback.

**Stevie Kim:** Yeah, I haven't really thought of how we're going to do deeper dive contextual interviews with our customers. I'll have to think about that. But typically, I work with customer success. I already have relationships with our customers from working in enterprise for so long. So this will be a little different approach trying to get some time because it's always good to have deeper dive conversations, especially on what they're trying to achieve and what they're expecting. So thank you. Just share any dashboards and insights with the whole team so we're not duplicating work and have eyes on all the things.

**Pedro Steimbruch:** Yeah, I shared an Notion doc with the dashboards, and today I did one more iteration trying to identify metrics that are actionable. We have vanity metrics, which are more about massaging your ego, and those are not actionable, right? It's implemented in PostHog with four dashboards. And there's a nice feedback Notion document there that we can implement into PostHog, and Claude can probably do it all.

**Stevie Kim:** I think I have maybe four visualizations set up in the product analytics dashboard. So we could see if it makes sense to put them in there or in a different dashboard if it's tracking different things. But yeah, it'll be great to have visibility into a lot of this stuff. Because I'm sure that Marcel is going to want reports.

**Pedro Steimbruch:** Yeah, I think the interesting one that Claude came up with is a user cohort—users that sign up today and return in day one, two, three. That will give us a good understanding of stickiness.

**Stevie Kim:** Yeah, I've got a stickiness metric. I removed it after talking to Daniel. He was like, we need to focus more on activation versus engagement right now. But we will definitely want to do the cohorts and engagement one. Yeah, I created that one. It's easy. It's super easy to create. The PostHog docs are really good too.

**Jose Farias:** Just wanted to call out Pedro. Jacopo told me that he was going to hold off on trying to optimize the sources page until we add the pagination back. Just let Jacopo know whenever you get to where this is.

**Pedro Steimbruch:** Yeah, I think it's with him already.

**Jose Farias:** Ah, okay.

**Pedro Steimbruch:** Cool.

**Jose Farias:** Cool. Okay.

**Stevie Kim:** I'll see you guys later. Bye-bye.

**Stevie Kim:** Bye.
