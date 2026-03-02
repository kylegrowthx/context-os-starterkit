# Redis <> GrowthX - Weekly Sync

<metadata>
date: 2025-12-18
time: 17:30 UTC
duration: 15 minutes
organizer: team@growthxlabs.com
participants: Aida Knezevic, Erik O'Brien, Alexis Ruiz-Pedregon, Reet Mand, Allison Gregory, Andy Varshneya, Cody Henshaw, Fung-Lin Wu, Megan Boone, Rebekah Reddis
fathom_recording_id: 109816794
fathom_url: https://fathom.video/calls/509862979
share_url: https://fathom.video/share/5_QW9GsT5RmP8Dxox-8_yb-HmzysyKrC
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Redis aligned on a "publish first, refine later" content strategy to accelerate article release and gather real-world traffic data before investing in heavy editorial review. Three articles are ready to publish; two are blocked by a missing CMS file and a duplicate topic. The team discussed how to streamline the PMM review process, confirmed a two-week holiday pause (Dec 25 & Jan 1), and introduced Erik O'Brien as the main point of contact as the project transitions to Phase 2.

---

## Context

GrowthX is providing content marketing services to Redis as part of a multi-week engagement. The Redis team (led by Alexis Ruiz and Reet Mand) is working with GrowthX to produce and publish technical content articles focused on Redis topics like vector search and stream processing. The relationship entered Phase 2 during this meeting, with operations transitioning from Aida Knezevic to Erik O'Brien as the primary GrowthX contact. The meeting occurred right before the holiday shutdown, so it focused on wrapping up the week's publishing work and confirming communication protocols for the two-week pause.

---

## Relevance

**To GrowthX Delivery:**
- Validated the "publish first, refine later" methodology — only 1 of ~6 reviewed articles required meaningful revision (Stream Processing definition clarification), proving minimal PMM overhead is needed for quality content.
- Established a performance review cadence: once 4-5 articles are live, GrowthX will begin analyzing traffic patterns in Looker and identify high-performing content clusters to double down on.
- Secured commitment to streamline review: PMM team will shift from pre-publication review to post-publication refinement, reducing bottleneck and enabling weekly article volume.

**To GrowthX Business Development:**
- Project is proceeding on schedule through Phase 2, now with more senior GrowthX ownership (Erik O'Brien replacing Aida Knezevic).
- Redis team responsive and aligned on strategy; holiday pause provides clean handoff point for Phase 2 operations.
- Featured image pipeline created; minor quality refinement needed (requesting individual design elements instead of composite images).

---

## Overview

- **New Review Process Proposed:** To accelerate publishing, GrowthX proposed a "publish first, refine later" model, with PMMs reviewing only high-performing articles. Alexis will discuss this with the PMM team.
- **Publishing Blocked:** Three articles are ready for publication, but two are blocked: one by a missing CMS file (`Vector Similarity Explained`) and another by a duplicate topic (`Vector Search`).
- **POC Transition:** Erik O'Brien will become the main point of contact, taking over from Aida Knezevic as the project enters Phase 2.
- **Holiday Schedule:** Syncs pause for two weeks (Dec 25 & Jan 1), with async updates provided. Meetings resume the first full week of January.

---

## Key Topics

### Content Review & Publishing

  - **Problem:** The current PMM review process is a bottleneck, delaying publication.
  - **Proposed Solution:** A "publish first, refine later" model.
      - **Rationale:** Prioritize publishing to gather real-world traffic data, then use that data to identify and refine high-performing articles.
      - **Validation:** A recent PMM review for the "Stream Processing" article confirmed this approach is viable, as feedback was minor (a definition tweak) and did not require a full rewrite.
  - **Status of Articles:**
      - **Ready to Publish (3):** Staged in CMS.
      - **Blocked (2):**
          - `Vector Similarity Explained` (refresh): The original article cannot be found in the CMS.
          - `Vector Search`: A duplicate of a recently published internal article.
      - **In Review (3):** Two with Allison, one with Jim (PMM).
      - **New Submissions (5):** Shared yesterday; PMM review is on hold until early January due to holiday bandwidth.

### Blocked Article Solutions

  - **`Vector Similarity Explained` (CMS Issue):**
      - **Action:** Alexis will ask the web team to locate the article.
      - **Contingency:** If the original file is unrecoverable, publish the refresh as a new article and set up a 301 redirect from the old URL to the new one.
  - **`Vector Search` (Duplicate Topic):**
      - **Decision:** Do not publish the GrowthX version to avoid content overlap.
      - **Contingency:** If the internal article underperforms, merge the two versions to create a single, stronger piece.

### Project & Process Updates

  - **Performance Reporting:**
      - **Timing:** Begin reviewing the Looker dashboard once 4–5 new articles are live.
      - **Action:** Add performance reviews to future weekly syncs to identify and double down on successful content clusters.
  - **Featured Image Pipeline:**
      - **Status:** Pipeline created in Atlas.
      - **Feedback:** Images appear blurry; this is due to large file size, not low resolution.
      - **Action:** Alexis will ask the brand team to provide individual design elements (e.g., logos, icons) for better quality control.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Post async updates to Alexis/Reet during holiday weeks (Dec 25 & Jan 1)
- Comment in Airtable re: Hybrid Search PMM review; tag Erik O'Brien; set status to Editorial
- Publish 3 staged articles in Redis CMS
- Send 5 new articles to Alexis/Reet next week
- Update Looker dashboard after this week's publishes
- Post Slack update to Alexis/Reet when articles are published

**Alexis Ruiz-Pedregon (Redis)**
- Ask web team to locate 'Vector Similarity Explained' in CMS; coordinate with Aida on update/publish + 301 redirect
- Meet with PMM team early January to align on publish-first review model

---

## Transcript

**Aida Knezevic:** This meeting is being recorded.

**Erik O'Brien:** Hey there. That vector search article, was that just a blind spot for us? Not on their content calendar?

**Aida Knezevic:** It was not on their content calendar. I asked Kavishka to check and it wasn't.

**Erik O'Brien:** Just on the same page.

**Alexis Ruiz:** Hello.

**Aida Knezevic:** Hi, Alexis.

**Alexis Ruiz:** How are you all?

**Aida Knezevic:** Good.

**Alexis Ruiz:** I think it will probably just be me. Everyone else is out of office now for the holidays.

**Aida Knezevic:** I think we have a couple of updates on the content production side and a couple of questions. But before we dive in, considering next Thursday is Christmas and then the week after that is the New Year, we can provide async updates during those two weeks if you want.

**Alexis Ruiz:** Yeah, that's fine. And then meeting on the first full week again of January works, because I'll be out the next two weeks and I think pretty much everyone will be as well.

**Aida Knezevic:** Awesome. Okay, great. So to give you an update on the content side of things, we shared five new articles yesterday. Fung-Lin had some questions around streamlining PMM reviews and enabling us to publish without getting as many people involved in the review process.

The way we approach the work at GrowthX is to really pay attention to the high performers. Once we start publishing, there will always be articles that don't perform as well as others. It's a bigger priority for us to publish and get traffic and understand what's working rather than go into super small details on every piece. For the high-performing blogs that do really well and get a lot of traffic, we can have a subject matter expert read them and provide suggestions to elevate them. But we don't want this to be a burden on anyone. For us, it's important to understand what's working, publish, and get results.

**Alexis Ruiz:** And then we can refine and enrich articles and go back and iterate them. That's something Fung-Lin and I talked about as well. I know that there was one article, the stream processing one, that one of our tech marketers let us know needed some updates.

**Aida Knezevic:** Yeah, exactly. The article was about stream processing and the feedback was about batch processing. We were comparing stream processing to batch processing and they wanted us to update the definition of batch processing. We adjusted the definition wherever batch processing was mentioned. When I saw the message I thought it would be major, but when we went into the article itself, the feedback didn't require heavy intervention.

**Alexis Ruiz:** Got it. Well, great, then that is perfect. On the other five newer ones, Fung-Lin mentioned that with the holidays and PMM bandwidth being very low right now, we most likely won't get to those till the beginning of the year. But for the ones we have out, two are ready and pending Allison's review. We also have one that Jim, the PMM, reviewed on the hybrid search one. I wanted to ask you, when that's ready to go, how would you like me to communicate that?

**Aida Knezevic:** I think you can drop a comment in Airtable and tag Erik. Put it to Editorial.

**Alexis Ruiz:** Okay, got it.

**Aida Knezevic:** We do have five that are ready to publish. These have been reviewed by both Allison and the PMM Team. We staged these three in your CMS and we can publish them today.

**Alexis Ruiz:** Okay, great.

**Aida Knezevic:** We just had two questions. This article that was a refresh, Vector Similarity Explained, we can't find it in your CMS. We don't know where it is and we can update the copy. I'm not sure if you've ever had anything like that before, but we would appreciate your help in finding this one.

**Alexis Ruiz:** Oh, okay. Let me make a note and I'll look into it after and ask the web team.

**Aida Knezevic:** It's just not showing up in the CMS for some reason. And then there was this article we did and it seems like we were working on the same thing at the same time, but this article wasn't in your internal content calendar. We did this article about vector search, and then when we went to stage this article, we noticed you published an article that's very similar on the same thing.

**Alexis Ruiz:** Oh. I think that was left over from previous articles that we had that just got published. Sorry about that. There shouldn't hopefully be too much overlap as we move forward.

**Aida Knezevic:** No worries. We do check your internal content calendar, so anything in there we're aware of. If this doesn't perform well, we can go back and merge the two articles together.

**Alexis Ruiz:** I was going to ask if that could be done.

**Aida Knezevic:** Totally. So we will go ahead and publish these three. And as soon as we find this one, we'll update it as well. We did create the featured image pipeline in Atlas. These are pretty similar to what you shared.

**Alexis Ruiz:** Yeah, they do look a bit blurry to me.

**Aida Knezevic:** They're not blurry, they're just quite large, so that's why they look that way. But they should be pretty sharp once you zoom in.

**Alexis Ruiz:** Okay. The next step is I could have our brand team have Claudia send over each of the elements together instead of the composite images I sent over, if you all needed them.

**Aida Knezevic:** That works too. Our designer is out of office until maybe Tuesday, so anything that needs updating will be updated next week. I'll also follow up with Fung-Lin and respond in Slack because she did ask me. Next week you will get five articles as usual. The week of December 29th is our quiet week, so that's when we pause publishing and then resume everything in January.

**Alexis Ruiz:** Okay, awesome. We're also going to meet with the PMM team right at the beginning of the year to talk through whether it's okay to have you all publish without their review. Like you mentioned earlier, we can just in real time change something if we see it needs it.

**Aida Knezevic:** Yeah, exactly. They've already reviewed maybe half a dozen blogs and only one had a definition that was slightly off that needed to be expanded a little bit. I think if you put that into perspective, we're asking them to do a lot of work and the content is fine. It's better to publish and then retroactively make changes rather than asking them to do all this work up front.

**Alexis Ruiz:** Agreed. Do you have any other updates, Erik?

**Erik O'Brien:** No, I think this is week eight, so we're transitioning to phase two. Aida won't be around much anymore and I will be the main point of contact. Just excited to keep things moving with you guys and move into the New Year with the team ready to go.

**Alexis Ruiz:** Great. I do have a question. With the dashboard and the performance report you all shared, when would it be best to start reviewing that to see how our content is doing? And will we be doing that in future meetings going forward?

**Erik O'Brien:** Yes, absolutely. Once we get enough published, we can start seeing the signals and which cohorts and clusters are picking up more traction than others, so we can double down on what's working. We can definitely fold in performance reviews in our weekly syncs moving forward.

**Alexis Ruiz:** Yeah, that would be awesome.

**Aida Knezevic:** Since we're publishing at least three to four articles this week, we're going to update Looker at the same time. That's when we start monitoring traffic. Once we have four or five pieces up, that's when we really start looking at what's going on.

**Alexis Ruiz:** And last question, the refresh that you can't find on the site — if it's not on our CMS anymore, could we just publish it as a new article?

**Aida Knezevic:** The issue is that the previous article still exists. So what we could do is set up a redirect from the old article to the new one. Then anytime somebody clicks on it, they'd be redirected to the new version. That way we don't have duplicate content since it's still live somewhere on the site.

**Alexis Ruiz:** Got it. I'll reach out to the web team right now and see if they can help me find that.

**Aida Knezevic:** Thank you. Anything else?

**Alexis Ruiz:** I don't have anything unless Reet does.

**Reet Mand:** No. Good progress. I just joined mainly to see if our team has the internal resources to review this stuff. Looks like we're making progress on that.

**Aida Knezevic:** I'll follow up in Slack with when we publish the new articles and we'll keep you posted on the performance as well.

**Alexis Ruiz:** Thank you. Great.

**Aida Knezevic:** Happy holidays.

**Aida Knezevic:** Happy holidays.

**Aida Knezevic:** Bye-bye.
