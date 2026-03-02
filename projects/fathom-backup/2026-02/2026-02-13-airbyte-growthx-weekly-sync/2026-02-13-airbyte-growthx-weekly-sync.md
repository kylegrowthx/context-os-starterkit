# Airbyte <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-13
time: 16:29 UTC
duration: 32 minutes
organizer: team@growthxlabs.com
participants:
  - Tanmay Sarkar (Airbyte)
  - Nithin Mahalingam (Airbyte)
  - Kushal Chatterjee (Airbyte)
  - Erik O'Brien (GrowthX)
  - Mario Moscatiello (Airbyte, not speaking)
  - Kyle Gaudreau (GrowthX, not speaking)
fathom_recording_id: 122335322
fathom_url: https://fathom.video/calls/565597919
share_url: https://fathom.video/share/pxQzZpD4sWxy5bvd7Q1fBmmdt__HovhM
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

Weekly coordination between Airbyte and GrowthX on content strategy, keyword prioritization, and publishing workflow ahead of the Airbyte product launch (delayed to Tuesday). Team aligned on shifting focus from zero-volume topics to high-intent competitor keywords, established a new workflow where Erik drafts in Webflow and Nithin publishes post-launch to prevent accidental go-live, and identified website fixes needed on the Agent Connectors page (missing Granola icon and misplaced Salesforce section).

---

## Context

The Airbyte <> GrowthX partnership is executing content strategy and visibility for Airbyte's new AI visibility product launch. This week the launch slipped from mid-week to the following Tuesday due to product fixes and team bandwidth, but all website, design, and content work is ready. The team has been managing a large content backlog in Airtable, but identified a critical strategic issue: many topics with zero search volume were being prioritized, wasting effort and yielding no organic traffic. Tanmay completed competitor research and collected a new keyword list with significant search volume that should form the basis of future content. The team also needs to refine the CheckThat prompts (the AI tool that monitors how LLMs answer questions) to focus on tool-based queries where Airbyte is a direct answer, rather than informational queries that don't drive traffic or user intent.

---

## Relevance

- **Content Strategy**: Shift from volume-based backlog to search-volume-driven prioritization; established new keyword cluster in Airtable with competitor research findings
- **CheckThat Product**: Refined prompt strategy to target tool-based, company-specific queries (e.g., "platforms for building AI agents with direct connectors") where Airbyte can rank as a direct answer
- **Publishing Workflow**: New process to prevent accidental site go-live: Erik drafts in Webflow, Nithin publishes after launch (critical given automated publishing issues with tables and code)
- **Website QA**: Identified and assigned fixes for Agent Connectors page (Granola icon, misplaced Salesforce section) before public launch
- **Agentic Data Content**: 15 articles in review stage, 2 more in progress; Erik managing drafts while Nithin handles publishing to maintain control during launch week

---

## Overview

- **Content Strategy Shift:** Prioritize high-volume keywords from competitor research to capture demand and drive initial traffic, deprioritizing topics with no search volume.
- **"Check That" Tool Refocus:** Revise prompts to target tool-based queries (e.g., "AI tools for data integration") where Airbyte can be a direct answer, driving high-intent traffic.
- **New Publishing Workflow:** Erik will draft all new articles in Webflow; Nithin will publish them post-launch to prevent accidental publication before the site is ready.
- **Website Fixes:** The "Agent Connectors" page requires fixes for a missing Granola icon and a misplaced Salesforce section.

---

## Key Topics

### Content Strategy & Keyword Prioritization

  - **Problem:** The Airtable topic backlog contains many topics with zero search volume, yielding no traffic.
  - **Solution:** Shift focus to high-volume keywords from competitor research to capture demand and drive initial traffic.
  - **Action:** Tanmay will review the competitor keyword list and the Airtable backlog, then share a prioritized list with Erik.
  - **Implementation:** Erik will add these to Airtable, potentially in a new "Competitor Keywords" cluster for clear tracking.

### "Check That" Tool Strategy

  - **Problem:** Current prompts for the "Check That" tool (which monitors how LLMs answer questions) are too generic, leading to informational answers that don't drive traffic to Airbyte.
  - **Solution:** Revise prompts to target tool-based queries where Airbyte can be a direct answer.
      - **Example:** "Platforms for building AI agents with direct connectors."
  - **Action:** Tanmay will send a new list of tool-based prompts to Erik.
  - **Implementation:** Erik will add these to the tool, using tags to group and filter prompts by topic.

### Publishing Workflow & Website Updates

  - **Context:** The main product launch is delayed until next Tuesday.
  - **New Workflow:** To prevent accidental publication before the site is ready, Erik will draft all new articles in Webflow, and Nithin will publish them after the launch.
  - **Website Fixes:**
      - **Agent Connectors Page:**
          - **Granola Icon:** Missing because it's not a "Data Replication" connector. Erik has a draft fix in Webflow.
          - **Salesforce Section:** A misplaced Salesforce section appears at the bottom of the Granola page. Erik will investigate with Kurt.
      - **Process:** All fixes must be staged for review before publishing. Nithin will monitor new connectors added via GitHub to ensure they display correctly.

---

## Action Items

**Kushal Chatterjee (Airbyte)**
- Review Erik's 'The Decline of RAG' article

**Erik O'Brien (GrowthX)**
- Draft all articles in Webflow; coordinate w/ Nithin to publish post-launch
- Create 'New Keywords' cluster in Airtable; import Tanmay's prioritized competitor keyword list
- Send CheckThat UI feedback to product team re: single-line prompts (currently multi-line is hard to read)
- Coordinate w/ Kurt to fix Granola page issue (misplaced Salesforce section); stage updates, don't publish
- Add 2 new agentic data articles to draft for review

**Tanmay Sarkar (Airbyte)**
- Review Airtable keyword sheet; identify and remove zero-volume topics; share prioritized competitor keyword list w/ Erik
- Send updated CheckThat prompts list to Erik (tool-based, company-specific queries only); Erik will upload and tag them
- Draft use-case landing page; research structure and share initial version w/ Erik next week

**Nithin Mahalingam (Airbyte)**
- Check internally if content exists for all CheckThat prompts; flag gaps
- Publish Granola icon on Agent Connectors page (Webflow) after Erik stages
- Monitor GitHub for new connectors added by engineering team; ensure all display correctly on website

---

## Transcript

**Erik O'Brien (GrowthX):** Hey, Nithin. Just saw Tanmay said he was going to be about 5, 10 minutes late. How's the week been? Big launch week?

**Nithin (Airbyte):** Actually, we couldn't launch it. It is pushed to next week—Tuesday. All the website, tech, content design, everything is ready. We just need to go live.

**Kushal (Airbyte):** Thank you. Okay, I'm on my commute, so let's just talk. Do you need anything from me? You guys can wait for Tame if you need anything from him.

**Erik O'Brien:** Yeah, I sent over the new Thought Leadership article for this week, "The Decline of RAG," so I think that's the only action item for you.

**Kushal:** Okay, sweet. I'll take a look at it probably early next week.

**Erik O'Brien:** Sounds like a plan. Any questions on that updated list I sent over earlier this week?

**Nithin:** Just a couple things. I'm pulling it up, Erik. Looking at the Airtable master list: apart from published, all the others have not been written, correct?

**Erik O'Brien:** Correct.

**Nithin:** Are there any that are written but not published?

**Erik O'Brien:** No, any of them that we had written have been published. There's just one that I forgot to flip to published.

**Tanmay Sarkar (Airbyte):** Eric, yeah, I think we can start. It's been a busy week. Our yearly meetup happened—back-to-back workshops, events, party. So I'm very tired.

**Erik O'Brien:** And then Nithin was saying the launch got pushed back to next week.

**Tanmay Sarkar:** Yes, because everyone was busy and there was some error in the product. So we fixed it. That took the whole week. Moving forward, here's what I recommend: Erik, you draft all new articles in Webflow. Nithin, you can publish them after the launch goes live. That way we prevent accidental publication before the site is ready.

**Erik O'Brien:** Yeah, we've been trying automated publishing through Airtable, but it's been giving us issues with tables and code snippets. So we'll do it manually.

**Tanmay Sarkar:** That's fine. I think we've done competitor research and collected some keywords that we'll share with you. The problem with our current backlog is that many topics have zero search volume, yielding no traffic. Moving forward, our priority should be writing the competitor keywords we've researched—those have huge search volume. We need initial traction on the website since this is a product we're building from scratch.

**Erik O'Brien:** Absolutely. So I'll add those to Airtable and create a new cluster for "Competitor Keywords" for clear tracking.

**Nithin:** I've been reviewing content against our topic list. Looking at agentic data topics, we need to align the prompts with actual content we've written. Some prompts don't map to Airbyte as a direct answer—they're more informational.

**Tanmay Sarkar:** Exactly. The CheckThat tool should target tool-based queries where Airbyte is a direct answer. For example: "Platforms for building AI agents with direct connectors." When someone asks about KV caching, that's informational—they won't click through to Airbyte. We should focus on prompts where we show up as a solution, not just as supporting content. Nithin, Airbyte shouldn't rank for definitional queries. Let's narrow to company and tool-based keywords.

**Erik O'Brien:** Got it. So we tag them separately to filter by tool-based recommendations?

**Tanmay Sarkar:** Yes. And we need to add tagging support to the UI. Currently we don't have any tags. We can start from scratch as we add prompts. Nithin, can you check internally if we have content for all these prompts?

**Nithin:** Yeah, I can do that.

**Tanmay Sarkar:** The third thing I want to discuss is the use-case landing page. I've reviewed what you sent, Erik. I'm doing research on how to structure it. I'll work on that next week and share it with you. We'll need to think about how to build it programmatically to scale.

**Erik O'Brien:** Okay, that works. Just a quick note on the Agent Connectors page. Granola is a new connector that wasn't supported by Data Replication, so it's missing its icon. I drafted the update in Webflow, but I didn't hit publish yet.

**Tanmay Sarkar:** Okay, I also noticed there's a misplaced Salesforce section at the bottom of the Granola page. Is that part of the design?

**Erik O'Brien:** I don't know if it was in the template and got pulled over. I'll check with Kurt and coordinate to stage it properly.

**Tanmay Sarkar:** Just make sure you don't publish anything—stage it for review. And Nithin, whenever the engineering team adds a new connector to GitHub, it populates automatically on our site. Keep an eye on that to make sure everything displays correctly.

**Nithin:** Will do.

**Erik O'Brien:** I know we didn't get to the typical update this week, but we've got 15 agentic data articles in the review stage, and two more we're wrapping up today.

**Tanmay Sarkar:** I'll check all the agentic articles. You can add them to draft, and Nithin will handle publishing for this week until we go live.

**Erik O'Brien:** Sounds like a plan.

**Tanmay Sarkar:** Thanks, Erik. Have a good weekend, and safe travels next week.

**Erik O'Brien:** Thanks, guys. See you.
