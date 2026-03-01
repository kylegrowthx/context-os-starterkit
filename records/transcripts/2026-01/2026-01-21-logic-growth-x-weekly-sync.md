# Logic <> Growth X - Weekly Sync

<metadata>
date: 2026-01-21
time: 18:29 UTC
duration: 61 minutes
organizer: Bailey Seybolt (GrowthX)
participants:
  - Azzam Aijazi, Founder & CEO, Logic
  - Joe, Logic (did not speak)
  - Jess Garms, Logic (did not speak)
  - Steve Krenzel, VP Engineering, Logic
  - Bailey Seybolt, GrowthX
fathom_recording_id: 116072931
fathom_url: https://fathom.video/calls/538013026
share_url: https://fathom.video/share/Zz15SjFxo1vz6xeGHaAydGL-uZis8diY
source: fathom
enriched_on: 2026-02-28 18:15 UTC
</metadata>

---

## Summary

Bailey and Azzam align on fixing Logic's content pipeline by integrating two new artifacts (product/features doc and competitive analysis) to provide the pipeline with proper context on Logic's capabilities and positioning. The team will pause current articles in review, incorporate the new artifacts, and refresh all 8 articles by January 31st while implementing a new watercolor-style header image strategy.

---

## Context

Logic, an AI agent platform, contracted GrowthX for content marketing. The content pipeline—which produces blog articles comparing Logic to competitors—has been generating inconsistent outputs due to insufficient context about Logic's specific features and competitive position. Bailey conducted an emergency review with the engineering and editorial teams to diagnose the root cause: the pipeline doesn't have enough directional guidance to compare Logic appropriately. Rather than comparing against everything, the pipeline needs explicit context on what Logic does and how to position it competitively. The solution is two-fold: Azzam will update his internal product/features documentation and competitor analysis, and GrowthX will integrate these as pipeline artifacts. Simultaneously, the team is implementing header images for blog posts (approved watercolor style, text-free) and building an internal visibility tracking platform to replace Scrunch with better user control over prompts and context.

---

## Relevance

**For Logic (Azzam, Steve):**
- Product narrative clarity: ensuring the pipeline accurately reflects what Logic does today versus future roadmap
- Content velocity: refreshing 5 in-progress and 3 in-review articles on Jan 31st deadline
- Visual identity: watercolor header images, text-free design for flexible layout reuse
- Platform planning: 2026 goals and metrics to inform content strategy refresh

**For GrowthX (Bailey):**
- Pipeline quality control: debugging why consistent feedback (e.g., "agents" vs "features") isn't propagating
- Artifact management: integrating product/features and competitor docs into the workflow
- Content calendar: tracking new posts and retroactive image generation
- Tooling roadmap: launching new visibility tracking platform next week, updating Scrunch prompts

---

## Overview

- **Pipeline Paused:** The content pipeline is paused to fix inconsistent outputs (e.g., using "features" vs. "agents"). All articles in review are moved to "in production" to prevent wasted effort.
- **New Artifacts:** Two new artifacts—a detailed product/features doc and a competitor analysis—will be integrated to provide the pipeline with the specific context it needs.
- **New Goal:** The pipeline will be fixed and all 8 existing articles (5 in progress, 3 in review) will be refreshed with new content and header images by January 31st.
- **Image Style:** The "watercolor" style is approved, but images must be text-free to avoid visual clutter and enable more flexible use.

---

## Key Topics

### Content Pipeline Issues

  - **Problem:** The content pipeline lacks direction, leading to inconsistent outputs.
  - **Symptom:** Repeated feedback on core terminology (e.g., "features" vs. "agents") across multiple articles.
  - **Root Cause:** The pipeline lacks specific context on Logic's features and competitive position, causing it to generate generic comparisons.

### Solution: New Artifacts & Process

  - **Product/Features Doc:** Azzam's internal doc will be updated and integrated to provide a definitive source of truth on Logic's capabilities.
  - **Competitor Analysis:** Azzam's new doc will be integrated as a separate artifact to guide competitive positioning.
  - **New Process:**
    1.  **Pause Pipeline:** All articles in review are moved to "in production."
    2.  **Update Artifacts:** GrowthX will integrate the new docs.
    3.  **Rerun Articles:** All 8 articles will be re-processed with the updated artifacts.
    4.  **Resume Review:** Azzam will review the re-processed articles.

### Image Strategy & Implementation

  - **Style:** The "watercolor" style is approved.
  - **Constraint:** Images must be text-free.
      - **Rationale:** Avoids visual clutter and enables flexible use across different layouts.
  - **Implementation:**
      - **New Articles:** Steve will add a field to Storyblock to store header images.
      - **Existing Articles:** Images will be generated automatically when articles are re-processed for the January 31st refresh.

### Tooling & Future Strategy

  - **Scrunch Prompts:** Will be updated after the new artifacts are integrated to avoid resetting the signal-gathering period.
  - **New Platform:** GrowthX's new visibility tracking platform will be demoed next week.
      - **Function:** Replaces Scrunch, offering direct user control over context and prompts.
  - **Future Planning:** A sync will be scheduled to refresh the content strategy based on Logic's 2026 goals and metrics.

---

## Action Items

**Azzam Aijazi (Logic)**
- Review/update product & features doc; send to Bailey by EOD (high priority); then Bailey shares w/ team, updates artifacts, runs post-processing, notifies Azzam
- Gather and share image style examples/preferences for header images
- Review re-processed articles once artifacts are updated (on rolling basis, all 8 to be delivered)

**Bailey Seybolt (GrowthX)**
- Move all 3 in-review articles to "In Production" (pause Azzam reviews until artifacts updated)
- Notify Rachel to pause tagging Azzam in Slack for reviews
- Send image comps to Azzam today
- Review/integrate Azzam's product/features doc and competitor analysis docs into pipeline
- Rerun all 8 articles (5 in progress, 3 in review) through updated artifacts
- Create content calendar: plan new posts + retroactive image generation for refresh
- Update Scrunch prompts to incorporate "agents" terminology (after artifact integration)
- Schedule 2026 content strategy refresh sync based on Logic's goals and metrics
- Demo new visibility tracking platform next week to Azzam and team

**Steve Krenzel (Logic)**
- Add header-image field to Storyblock
- Update landing page to reference header images
- Approve watercolor image style with text-free constraint

---

## Transcript

**Bailey Seybolt:** Hey, how are you doing?

**Azzam Aijazi:** Pretty good. Can't complain.

**Azzam Aijazi:** I don't know which recorders are ours anymore, so I'm just going to assume things are okay.

**Bailey Seybolt:** Oh, the note takers? [laughs] Yeah, we're recording, transcribing, and documenting this. The robots have outnumbered the people in the room now.

**Bailey Seybolt:** All right. I'm going to share the agenda.

**Bailey Seybolt:** So the agenda is a little informal because I just came from meeting with our engineering and editorial teams. I wanted to understand what's happening with the pipeline so I could give you concrete next steps and get your feedback on direction.

**Bailey Seybolt:** So I got the editorial and engineering teams in one room to look at outputs, review artifacts, and understand the pipeline's direction. The engineering feedback is that the pipeline lacks enough direction to determine what angle to take. It's comparing Logic against everything when we should be giving it more context on what to compare Logic to. What would really help is an artifact that describes all of Logic's features and what they solve in detail.

**Azzam Aijazi:** So we have something to base this on.

**Bailey Seybolt:** Can you see the doc I just shared?

**Azzam Aijazi:** I was going to recommend the same thing. I provide a doc like this to my cloud instance for context. It might not be completely up to date, but it helps ground my Claude instance with what Logic actually does today and can do.

**Azzam Aijazi:** Claude will often say Logic offers end-to-end tracing to see the entire thought process of agent decisions, which it doesn't actually do yet. So I want to explicitly list the features Logic does have and what it doesn't do yet versus what's planned. That would be helpful for both your content and my internal work. Transparently, I use my Claude instance to proofread and review what you guys are writing—I get really good feedback based on the context I've given it. So the issue might be that you need to shape your context more precisely. I'm happy to help provide whatever context you need.

**Bailey Seybolt:** That sounds exactly right. Anything you want to share in terms of documentation that shapes context correctly—that's what engineering asked for. More context is helpful.

**Azzam Aijazi:** I can take one more pass at it. It looks fairly accurate, but I haven't done a comprehensive review in a few weeks.

**Bailey Seybolt:** Perfect. I can do that and get back to you today. Then I can share it with the team and fill in any gaps you identify. I think this should be most of what we need.

**Azzam Aijazi:** I also shared a competitor analysis doc yesterday, which lists competitors and how Logic compares. I'm using that to ground my own AI instance, and I'd recommend you incorporate it into the pipeline too.

**Bailey Seybolt:** I saw you shared those two docs. I haven't reviewed them yet, but I shared them with Rachel. For the competitive positioning one, I'd recommend making that its own artifact. Then apply any changes from the other doc to all our artifacts.


**Azzam Aijazi:** One thing I was thinking about this morning: when I give feedback on an article, can we incorporate that back into the approved artifacts? I keep giving the same feedback across different articles. For instance, let's call what we make agents, not features. I'd like to give that feedback once or twice and see it incorporated in other articles.

**Bailey Seybolt:** That should be happening. When you leave feedback like "we call our product X," Rachel from editorial should update the artifacts. There might be a lag sometimes because articles are already in the pipeline, but if you see feedback that doesn't propagate, tag it for post-processing.

**Azzam Aijazi:** Here's what would be helpful: I'll share the product and competitor docs. Can you pause for a day, incorporate them across the pipeline, then let me know so I can review articles that already have those changes applied? I'd rather take a little more time than give redundant feedback.

**Bailey Seybolt:** That totally makes sense. We'll focus on updating the artifacts. All articles in review now move to "In Production" so you know not to review them. Once we've updated artifacts, we'll run all 8 through and let you know. We did publish one today and have two more to stage, so we can get back to publishing.

**Azzam Aijazi:** I'm fine reviewing articles now. I just don't want to give feedback that the pipeline would apply anyway.

**Bailey Seybolt:** Exactly—no double work. I'll touch base with Rachel after this. She won't tag you in Slack yet on reviewed articles. So we have 5 in progress and 3 in review. I hope to give you all 8 to review on a rolling basis once we integrate the artifacts.

**Bailey Seybolt:** I'll also circle back on Slack if there's anything else we need for the product and features document from the Eng Team. Anything else blog specific?

**Azzam Aijazi:** I think we're on the same page about what we want to do.

**Bailey Seybolt:** Images. I owe you some comp images—I didn't pull them together over the long weekend, but I'll get them to you today. We have watercolor-style options already in the pipeline.

**Azzam Aijazi:** I'll pull together some examples too.

**Bailey Seybolt:** Feel free to share examples—our image generation pipeline is really flexible. I think it can handle almost anything.

**Azzam Aijazi:** That's great to hear.

**Azzam Aijazi:** Steve, what would it take to start incorporating header images into our blog posts?

**Steve Krenzel (Seattle):** Where are the images in Storyblock right now? They're being generated but we're not storing them anywhere?

**Azzam Aijazi:** Right, we haven't been using images yet. We published one article this week but without images.

**Steve Krenzel (Seattle):** Step one is adding a section in Storyblock to store them, then set up the landing page to reference them. Assuming they're being generated, it's straightforward.

**Azzam Aijazi:** Okay. And how hard would it be to retroactively generate images for our previous published articles?

**Bailey Seybolt:** Not very hard. We'd rerun them through the pipeline.

**Azzam Aijazi:** That would take a few hours?

**Bailey Seybolt:** Yeah.

**Azzam Aijazi:** And we're probably doing that anyway to update the content?

**Bailey Seybolt:** Yes.

**Bailey Seybolt:** When we update with new positioning, it would generate new images too. So it won't take extra time.

**Azzam Aijazi:** Right, no extra time. I think we're getting close to a quality of output that should require relatively little intervention. Can I propose a goal: by January 31st, we have our pipeline ironed out and all previous articles refreshed and live?

**Bailey Seybolt:** Yeah, that seems reasonable. Once we have this next round and you feel good about all of them, we can start refreshing the older ones. I'd also pull together a content calendar—chunk the old blog posts and aim for a certain number of new ones and updates every week to maintain publishing velocity.

**Azzam Aijazi:** That works. Let me know what I can do to help. I'm happy to produce more artifacts, videos, whatever it takes.

**Bailey Seybolt:** The key is the product/features doc. The faster you can review it, give detail, and confirm accuracy, the better. Then we update and test to make sure it fixes the issue.

**Steve Krenzel (Seattle):** I missed the call last week when you reviewed images. Can you have one or two examples handy?

**Bailey Seybolt:** We put examples in the calibration blog posts. We're following a watercolor hand-drawn style. I pulled examples for each article.

**Steve Krenzel (Seattle):** I love the tackle box image and the river ones. These are awesome.

**Bailey Seybolt:** The other one is an LLM Extraction image with a pipe. This was based on the style you shared. Azzam wanted to see comps of other image types we've produced, to confirm we're going all-in on this style. We're producing so many different kinds—very reflective of the breadth we're creating.

**Steve Krenzel (Seattle):** One note: images should have no text at all. The tackle box is perfect—no words. But the pipeline image with "messy input / clean outputs" text competes with other text on the page.

**Azzam Aijazi:** I agree strongly with that.

**Bailey Seybolt:** We can definitely adjust. Text-free looks better and you can use it more flexibly. Less chance of weird hallucinations. I'll note that and put together comps.

**Bailey Seybolt:** We updated Scrunch prompts a few weeks ago and are starting to see signal. I didn't update the "agents" language yet because it takes about a week to see results—didn't want to reset. But now with these changes, I'll review the prompts in both Scrunch and our internal tool. Once we start publishing, we'll adjust Looker to tag new content clusters.

**Bailey Seybolt:** I mentioned the visibility tracking platform we're building. Next week we'll demo it to customers and onboard you so you can use it directly.

**Steve Krenzel (Seattle):** Does that replace Looker or is it in addition?

**Bailey Seybolt:** In addition to Looker. It would replace Scrunch—a version of Scrunch we built that does better for B2B buying stage tagging. You'd have control to update context, add custom prompts, add competitors, instead of waiting for Scrunch updates.

**Bailey Seybolt:** Once we stabilize, I want to schedule a sync to review 2026 strategy and metrics. Lots has changed since we started this pivot, even the way you're talking about your company. We'll want a keyword refresh at minimum.

**Bailey Seybolt:** We'll review the strategy based on how you're measuring success for Logic in 2026. That's all from me. Anything else you want to touch on?

**Azzam Aijazi:** No, this sounds good.

**Steve Krenzel (Seattle):** This is good.

**Bailey Seybolt:** Great. Azzam, take a look at the product/features sheet and verify accuracy. I'll share it with the team once you confirm.

**Azzam Aijazi:** Sounds good. This is high priority for me—I'll get it to you today.

**Bailey Seybolt:** Perfect. I'll have them read it right away.

**Azzam Aijazi:** Thank you.

**Bailey Seybolt:** Thank you both.

**Bailey Seybolt:** Thank you.
