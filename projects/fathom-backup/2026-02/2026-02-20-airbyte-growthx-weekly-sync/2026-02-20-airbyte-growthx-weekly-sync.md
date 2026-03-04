# Airbyte <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-20
time: 16:29 UTC
duration: 18 minutes
organizer: team@growthxlabs.com
participants: Tanmay Sarkar (Airbyte), Nithin M (Airbyte), Mario Moscatiello (Airbyte), Kyle Gaudreau (GrowthX), Kushal Chatterjee (Airbyte), Erik O'Brien (GrowthX), Team GrowthX
fathom_recording_id: 124096761
fathom_url: https://fathom.video/calls/573489651
share_url: https://fathom.video/share/yBZGE3hsGPhAiLvwqehCBmN1Y4KnFvzm
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

GrowthX and Airbyte discussed restarting the content publishing pipeline after a two-week pause (41 pending articles), creating a hybrid writing style that balances Kushal's thought leadership feedback with SEO best practices, and a major Profound account cleanup focused exclusively on the Agent Engine product. Direct traffic has doubled to 50% of total traffic, likely from AI bots/scrapers with unusual device signatures (800x600 resolution), requiring deeper analysis to isolate real user data.

---

## Context

This is a weekly tactical sync between Erik O'Brien (GrowthX, content strategy lead) and Tanmay Sarkar (Airbyte, content/product owner), with mentions of other Airbyte team members (Kushal Chatterjee - writing feedback, Nithin M - Airtable management, Mario Moscatiello) and GrowthX team. The meeting occurred after Airbyte's website launch, which created a two-week publishing pause. GrowthX serves as a strategic content partner for Airbyte's content and thought leadership strategy.

The core focus is operational execution: unblocking the publishing pipeline, aligning writing standards across quality and SEO performance, managing the content topic backlog, and ensuring product measurement infrastructure (Profound platform) reflects current product focus on Agent Engine.

---

## Relevance

- **Content Strategy**: Writing style alignment, SEO vs. thought leadership balance, publishing workflow and approval processes
- **Product Focus**: Profound account restructuring to track Agent Engine; coverage of zero-visibility product features
- **Analytics & Data**: Distinguishing bot traffic from real users; direct traffic spike from China/Singapore scrapers (800x600 resolution anomaly)
- **Project Management**: Publishing pipeline unblocking, Airtable topic management, design partner feedback loops
- **GrowthX Engagement**: Content partnership execution, hybrid style guidelines development, account cleanup and measurement support

---

## Overview

- **Content Pipeline Unblocked:** Tanmay will review 41 pending articles (29 old, 12 new) to restart publishing after a two-week pause for the website launch.
- **New Hybrid Writing Style:** Erik will create a hybrid style merging Kushal's V2 thought leadership with V1's SEO best practices (tables, bullets) to balance quality and search performance.
- **Profound Account Cleanup:** Tanmay will audit the cluttered Profound account to remove outdated content, streamline tracking for the "Agent Engine" product, and add topics for zero-visibility prompts.
- **Traffic Anomaly:** Direct traffic has doubled to \~50% of total traffic, likely due to AI bots/scrapers. GrowthX is investigating to isolate real user data.

---

## Key Topics

### Content Pipeline & Publishing

  - **Problem:** Publishing paused for two weeks due to the website launch, creating a backlog of 41 articles.
  - **Action:** Tanmay will review all pending articles after Erik tags them in Notion.
  - **Thought Leadership:** V2 of the next piece is ready for review; Erik will follow up with Kishal and John.

### Writing Style Strategy

  - **Conflict:** A new "V2" writing style (Kushal's feedback) improves flow but sacrifices SEO features (e.g., comparison tables) present in the "V1" style.
  - **Goal:** Create a hybrid style that balances thought leadership quality with SEO performance.
  - **Action:** Erik will use Claude to merge V1 and V2 guidelines; Tanmay will review the result.

### Airtable & New Topic Ideas

  - **Status:** All new topic ideas are merged into Airtable.
  - **Action:** Tanmay will identify "zero-visibility" prompts in Profound and add them to the Airtable backlog to ensure coverage for all product features.

### Profound Account Cleanup

  - **Problem:** The Profound account is cluttered with outdated content and poor tracking, hindering visibility and measurement.
  - **Goal:** Clean up the account to focus exclusively on the "Agent Engine" product.
  - **Action:** Tanmay will audit the account and create a cleanup checklist for Erik.
  - **Design Partner Role:** Erik requested Tanmay's feedback on missing features, leveraging Tanmay's experience with 25-30 other AI platforms.

### Traffic Performance Anomaly

  - **Observation:** Direct traffic has doubled, now accounting for \~50% of total traffic (400-500 weekly visits vs. 200 without direct).
  - **Hypothesis:** The spike is from AI bots/scrapers (e.g., from China/Singapore), evidenced by unusual screen resolutions (800x600).
  - **Action:** GrowthX is analyzing the data to differentiate real users from bots.

### Agent Use Case Wireframe

  - **Status:** Tanmay is finalizing a V1 wireframe for the Agent use case.
  - **Action:** Tanmay will share the V1 wireframe on Monday for initial feedback from Erik and the internal team.

---

## Action Items

**Erik O'Brien (GrowthX)**
- Tag Tanmay in Notion with pending articles (29 in review + 12 new); Tanmay then reviews and publishes
- Create hybrid writing guidelines merging V1 SEO features and V2 thought leadership style; share with Tanmay for review
- Follow up with Kushal Chatterjee and John on V2 thought leadership piece for review

**Tanmay Sarkar (Airbyte)**
- Review all 41 pending articles (29 old, 12 new) after Erik tags them in Notion
- Share Agent use case wireframe V1 with Erik and internal team by Monday
- Ask Nithin M to review Airtable for zero-visibility prompts; export and match with current content list
- Draft Profound account cleanup checklist (tags, docs, categories); share with Erik for execution planning
- Monitor direct traffic data to differentiate bots (800x600 resolution anomaly) from real users; share analysis with Erik

---

## Transcript

**Tanmay Sarkar (Airbyte):** Ready to start.

**Erik O'Brien (GrowthX):** Yeah, absolutely. I think the biggest thing I wanted to talk through is we've got 29 articles still in review and 12 that were just uploaded today, but it's been two weeks since we've published.

**Tanmay:** Yeah, that's because the last two weeks we couldn't publish due to the website launch. Now we can start continuing with publishing. Can you tag me in Notion?

**Erik O'Brien:** In Slack?

**Tanmay:** No, here in Notion. Just comment and tag me.

**Erik O'Brien:** Oh, yeah, yeah. Yeah. Perfect. And then we've got version two of the next thought leadership piece ready for review. So I'll ping Kushal and John again. I sent it over Wednesday, but I'll give them a nudge. And we'll deliver one more today. That covers the content updates.

On the Agent use case wireframe, you said you were working on a different version. Any updates?

**Tanmay:** Yes, I'm almost done. I can share it probably on Monday. And it's not final—I'll share with you and our internal team, gather feedback, rework it, and make a final version. But this is the V1.

**Erik O'Brien:** Perfect.

**Tanmay:** I think first I'll do the pending articles review. Kushal shared some writing style feedback. Have you applied that to the unpublished articles in the backlog, or will it be for new articles?

**Erik O'Brien:** For new articles starting next week. We did one test with one of the new articles. So V1 is the current pipeline, V2 is Kushal's writing instructions.

**Tanmay:** What's the difference? Can you tell me in layman's terms?

**Erik O'Brien:** My initial read is it feels more aligned with thought leadership. I even had our chief content officer look at it. He said it's drastically different from what we'd aim for in SEO or AEO articles. But he said if we're happy with the output, we can do it. However, it does go against most of our SEO best practices.

**Tanmay:** Yeah, I'm seeing that. In version two, I don't see any comparison tables like you had in version one. Can we make sure we use all the SEO features? Bullet points, comparison tables—those kinds of things. Version two is fine, but try to accumulate these elements so we find the perfect balance.

**Erik O'Brien:** Yeah, that's what I wanted to spend more time on today. I'll use Claude to take our existing writing guidelines and mesh them together so we don't lose the SEO and AEO best practices but improve the flow and reduce the choppiness. I'll come up with a hybrid version that gets us closer to what we're looking for.

**Tanmay:** Yes, that would be better. In current version two, I just see text. There's nothing tabular or structural. I understand thought leadership, but our goal is to get traction. If it doesn't serve that, there's no point producing it that way.

**Erik O'Brien:** Yep, I agree.

**Tanmay:** Once you make the hybrid version, just share it with me. I'll review and let you know.

I've also seen the Airtable you shared. Where can I find the whole updated list?

**Erik O'Brien:** You can share your screen. Yes, I went in and merged everything into Airtable. I pushed most into the review stage. I put the approved ones in to start.

**Tanmay:** That's fine. We can go ahead with the list. What I want now is to work with Nithin. We have some prompts on Profound with zero visibility. We need to write those prompts as topics and add them to the backlog so we have a pipeline for coming weeks.

**Erik O'Brien:** Perfect.

**Tanmay:** I'll ask Nithin to review the Airtable and let you know. We can export and match it with the current list.

The next thing is how to set up and clean the Profound account. It's currently cluttered with poor tracking. How do we use tags for each item? I'm seeing the context is about the new product. We deleted the data engineering content and are only focusing on Agent Engine, correct?

**Erik O'Brien:** Yes, I went through and did that last week of January.

**Tanmay:** Cool. So I'll spend time on this, talk to Nithin, and we can share a checklist of what to do. That way, we have clear visibility of what we're tracking and how to measure it, which we can showcase internally too. I noticed the overview was rewritten to the old one. We need to delete that and clean up. I'll make a list of docs—what's there and what we need to remove or replace.

**Erik O'Brien:** Yeah. And then for categories?

**Tanmay:** I didn't find any relevant categories, so I'm not sure. But I can see everything and create a doc to share with you.

**Erik O'Brien:** Okay, perfect. As you go through that, we have you guys tagged as a design partner. We want your input on what's missing and what's a top priority.

**Tanmay:** Yeah, I've given a lot of feedback to Profound over the past year. I've seen demos of about 25 to 30 AI platforms, so I have plenty of feedback.

**Erik O'Brien:** I get what we're trying to do—having a library of prompts with historical data makes it more valuable than a cold start. But we're missing basic functionalities that would make it much more powerful for users. Any feedback or recommendations on features and functionality, we'll take.

**Tanmay:** Sure, I'll let you know.

**Erik O'Brien:** Good. Those are the things I wanted to discuss. Now, on performance: with the publishing slowdown, we're seeing a traffic slowdown too. But we've noticed direct traffic is picking up across all accounts. Without direct traffic, we're at 200 per week. With it, we're at 400 to 500. It's almost a 50% difference. We've attributed it to bots from China and Singapore.

**Tanmay:** I read an interesting article recently about considering AI bots as traffic—like agents moving forward.

**Erik O'Brien:** That's what we're trying to decipher—which direct traffic is crawlers versus AI bots. We're seeing weird 800x600 resolutions. Unless you're on a 1988 desktop, it's not real. We're seeing that pop up across every account. We're doing deeper analysis to understand if it's AI bots crawling pages or people scraping for content. Historically, we included direct traffic since it hadn't spiked like this. But we'll monitor it going forward to see the delta between real direct traffic and bots.

**Tanmay:** Yes, absolutely. I think that's a good flag. I'll monitor this internally too.

**Erik O'Brien:** Awesome.

**Tanmay:** Cool. Thanks, Erik. Have a great weekend.

**Erik O'Brien:** Thanks. You too. See you next week.

**Tanmay:** Bye, see you.

**Erik O'Brien:** Bye.
