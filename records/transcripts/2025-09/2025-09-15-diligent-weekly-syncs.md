# Diligent Weekly Syncs

<metadata>
date: 2025-09-15
time: 16:00 UTC
duration: 34 minutes
organizer: jo@growthx.ai
participants: Jo Kaminska (GrowthX), Megan Dickey (GrowthX), Kezia Farnham (Diligent), Festus Shodipo (Diligent)
fathom_recording_id: 87261703
fathom_url: https://fathom.video/calls/404617726
share_url: https://fathom.video/share/uQyhz7nRtSuC5-bNbFKYZ7UELtxe_Y3D
source: fathom
enriched_on: 2026-03-03 11:30 UTC
</metadata>

---

## Summary

GrowthX and Diligent aligned on restructuring weekly reporting to break down deliverables by Diligent's four solution categories (VLC, ERM, IRC, EMT) to streamline internal systems integration. The team reviewed GrowthX's new NetNew content calibration framework and confirmed 22 topics still in "considering" status, including AI compliance monitoring which aligns with new prompts uploaded to Scrunch. Diligent is pursuing a unified dashboard combining GA4, Google Search Console, Ahrefs, and internal Glean AI data for week-over-week metrics, competitor benchmarks, and regional breakdowns—with GrowthX's analytics team exploring custom build options and GA4 optimization to support this integration.

---

## Context

Diligent is a major GrowthX content marketing client working on expanding their SEO visibility and content strategy across four key solution areas: Valuation, Litigation & Compliance (VLC); Enterprise Risk Management (ERM); Internal Revenue Compliance (IRC); and Entity Management & Tracking (EMT). This weekly sync is part of GrowthX's ongoing delivery to help Diligent produce NetNew content and optimize their reporting infrastructure. Diligent is actively modernizing their internal workflows by centralizing content performance data into their proprietary Glean AI system to enable faster decision-making and reduce manual reporting work across teams.

The meeting reflects a maturation in the engagement—Diligent is moving beyond basic content production and dashboard access to asking for system-level integrations and custom analytics solutions that require coordination between GrowthX's content, delivery, and engineering teams. Megan Dickey's involvement signals potential scope expansion or contract restructuring may be needed.

---

## Relevance

**To GrowthX Delivery:**
- NetNew content calibration framework (meta, pain points, definitions, expert quotes, SEO sections, use cases, trends, Diligent product focus) is now standardized and ready for content managers to use directly in production. 22 "considering" topics should be moved to "ready to start" — AI compliance monitoring is high-priority per new Scrunch-tagged prompts.
- Weekly deliverable Slack message format needs restructuring to split by VLC/ERM/IRC/EMT solution categories so Diligent can paste results directly into internal systems. Jo owns implementation; Kezia will provide category definitions.
- Content strategy discussions revealed multi-topic pieces (e.g., boards + risk = VLC) should list both solution categories with cross-reference notes, giving Diligent visibility into secondary impact areas.

**To CheckThat:**
- Diligent's move toward AI-powered search (Glean AI) over manual reporting creates potential for CheckThat integration into their internal systems. AI compliance monitoring content aligns with updated CheckThat prompts uploaded to Scrunch.

**To GrowthX Business Development:**
- Account health signal: Diligent is expanding scope and asking for custom engineering solutions, indicating willingness to invest in deeper integration. Megan's involvement signals potential scope expansion or contract restructuring conversation.
- Diligent wants everything "within their ownership" (non-negotiable) and needs version 1 of dashboard ASAP. This is a speed/efficiency play, not a technical limitation — opportunity for upsell if GrowthX invests engineering time.
- GA4 optimization and MQL tracking setup are potential add-on services if Diligent wants qualified lead attribution beyond current content delivery.

---

## Overview

- Need to adjust weekly deliverable reports in Slack to align with Diligent's internal solution categories (VLC, ERM, IRC, EMT)
- Aiming to create a comprehensive dashboard view combining multiple data sources (GA4, GSC, Ahrefs, etc.) for more efficient reporting and AI tool integration
- Exploring options to automate weekly reporting and integrate with Diligent's internal systems (Glean AI) to reduce manual work

---

## Key Topics

### Content Strategy Updates

  - Reviewed calibration piece for NetNew content structure
  - Outline includes meta info, pain points, definitions, expert quotes, SEO sections, use cases, trends, and Diligent product focus
  - 22 topics still in "considering" status, including AI compliance monitoring which aligns with new prompts

### Reporting Structure Changes

  - Request to break down weekly deliverable reports by Diligent's main solution categories
  - Categories: VLC, ERM, IRC, EMT
  - Jo to implement changes based on details Kezia will provide via Slack

### Dashboard Integration Goals

  - Create a single-view dashboard combining multiple data sources
  - Aim to upload weekly view into internal AI tool for easier access and searchability
  - Include competitor information, target metrics, and various data streams (Ahrefs, GSC, GA4, Scrunch)
  - Desire for regional breakdowns and executive-level reporting

### Analytics and Integration Challenges

  - Current Looker Studio setup limited to GSC and GA4 data
  - Unable to directly integrate Ahrefs or SEMrush data due to internal GrowthX constraints
  - Potential need for custom solution or expanded scope to achieve desired integrations

### Next Steps for Reporting Improvements

  - Kezia to provide list of desired integrations, metrics, and internal tracking methods
  - Explore possibilities for custom dashboard development or alternative solutions
  - Review current GA4 setup and potential optimizations for better lead tracking

---

## Action Items

**Jo Kaminska (GrowthX)**
- Update weekly deliverable Slack message format to split by VLC, ERM, IRC, EMT solution categories
- Review each Looker Studio report with Kezia in next meeting

**Kezia Farnham (Diligent)**
- Provide category breakdown and definitions for VLC, ERM, IRC, EMT to Jo for Slack formatting
- Send comprehensive list of desired integrations, metrics, and internal HMQL tracking methods to GrowthX team
- Review content topics in Airtable and move "considering" items to "ready to start" (particularly AI compliance monitoring)

**Megan Dickey (GrowthX)**
- Discuss dashboard integration options with GrowthX client ops and engineering teams
- Assess feasibility and cost of custom dashboard build vs. alternative solutions (e.g., GA4 optimization, Amplitude integration, Excel automation)

---

## Transcript

**Kezia Farnham:** Thanks so much for sharing the link to the Looker Studio. I think that's really helpful to see and have a little bit more access to what's already going on. For some reason I think I might have missed where this link was, because after you showed me on the last call, I was like, where am I looking for this? I do have access now, so appreciate you re-sharing that.

**Kezia Farnham:** And maybe if it's okay, I could dig into a couple more things that we might want to add and share what the end goal is to give a little bit more context so we're all on the same page.

**Kezia Farnham:** I definitely wanted to touch on that, and then I also had one more request. The deliverable notes are super useful. I'm wondering if it's possible on Fridays when you send those through in Slack to break them up into our main internal theme structure so we can then easily take that and paste it into our internal systems so everyone has access.

**Kezia Farnham:** I'll put that into Slack to break down the four key areas. For instance, if we have three pieces on ERM, we'd have "ERM: one, two, three - here's what they are." This would be a huge time saver as we move forward with our new internal reporting method.

**Jo Kaminska:** Yeah, it makes sense. I can use these granular topics from our content. So if that's fine, I would include this tag.

**Kezia Farnham:** What would be super helpful for the weekly deliverables on Slack is if we could split into our solution breakdown—VLC, ERM, IRC, and EMT. I can send you that breakdown on Slack so it's not just more Diligent jargon.

**Jo Kaminska:** One thing to keep in mind: usually we mention more than one problem in specific content pieces. Should we lead with the main one? We agreed boards and governance are most important, so should we prioritize that as a tag?

**Kezia Farnham:** If a piece hits a need for both ERM and governance—like the BLC around boards and risk—let's include it in both places but with a bracket note that it's one piece between the two. That shows we're making a difference in multiple areas, which is still important.

**Jo Kaminska:** Please send a list with all the abbreviations so we can go back and forth until we get into a good flow.

**Jo Kaminska:** I wanted to present a calibration piece for NetNew content. I don't want you to review it on the call, just take a look at how we structured it. The calibration shows how we think about producing NetNew content so our content managers can produce straight away without breaking it into outline and draft.

**Jo Kaminska:** For a virtual data room, we start with meta title/description, intro around a specific pain point, definition, preview, and expert quotes—using the quotes you provided. Then regular SEO sections: mixing what is/features with pain point solution content, essential features, primary use cases, trends, selection criteria, and best practices. We tie it to topics Diligent covers and go from top-level SEO into practical middle-funnel content. Then we focus on Diligent products with overview, features, key benefits, practical examples, inline CTAs, FAQ, and conclusion with optimized headline and call to action.

**Kezia Farnham:** This looks really good. Would you send me a link so I can add comments after a closer look? The outline seems appropriate. Depending on term volume, there might be opportunities to add more.

**Kezia Farnham:** Before we move on, Festus—anything jump out to you?

**Festus Shodipo:** I think having FAQs before the CTAs is an interesting idea. I like it and it makes sense.

**Jo Kaminska:** FAQs usually go at the end, but you have a call to action to request a demo at the end. I think both solutions work. Thanks for the feedback—it's great to align early so we can speed up production going forward.

**Jo Kaminska:** Speaking about topics generally, Kezia, I saw all your comments in Airtable. I sorted them out and provided additional context for our account manager. I think we're good to go with the topics in the content OS. We still have 22 in "considering" status. Some of these—like AI compliance monitoring—are good to realize because based on the new prompts you provided to Scrunch that we uploaded by tags, there's not much visibility in the AI compliance space. These are very good topics to cover to increase LLM visibility. There's so many good topics in considering that we should move to ready to start.

**Kezia Farnham:** It's on my list to go back and review. I'll wait until you're done your first batch and then go through them and move any further ones into approved.

**Kezia Farnham:** Are we good to jump into the dashboard view and what we're trying to achieve? We're trying to get a single view that can be uploaded into our internal system and connect back to our AI tools. If someone has a question, they can quickly search and resurface information. We want different views for different audiences—operational (more detailed) and executive-level.

**Kezia Farnham:** What you have in Looker Studio is great information. We want to compile those pieces plus a few additional ones into a simple table. It could be a literal screenshot or an integration—we'll look into that. Either way, we want to bring in Ahrefs, Google Search Console, GA4, and Scrunch data all into one table view. It doesn't need to look pretty, just give us week-over-week metrics, competitor numbers, and our target figures all together.

**Kezia Farnham:** For target figures, we look at last year, what we'd expect if nothing changed, market shifts we're seeing (like organic traffic declines we factor in), and how much we're trying to grow. Then we break it down into the solution buckets we mentioned earlier and eventually into regional views for different stakeholders. But right now, we just need a simple table we can feed into our AI tool to help us operationally and at the exec level.

**Jo Kaminska:** Thanks for sharing all the details. For Looker Studio, we can connect Google Search Console and Google Analytics, which are already present. If you have regional channel grouping set up in GA4, we can pull that as a report. Otherwise, it requires analytics setup. Google Search Console is more straightforward—we have impressions, click-through rate, and average positions available without modification.

**Jo Kaminska:** For conversion data, MQL measurement depends on your CRM type and how it connects to Google Analytics via a shared identifier. I see you're tracking lead form submissions, but I don't see MQL-related events. We'd need to know how you're tracking MQLs to build that dashboard. One option is Amplitude, which other clients use for granular conversion data by product and region without resetting Google Analytics setup.

**Jo Kaminska:** We cannot connect Ahrefs or SEMrush to Looker Studio—our team is working on integrations through Atlas platform as work in progress.

**Kezia Farnham:** Is there an internal reason GrowthX can't get Ahrefs data? I know there's a connection possible. And does GrowthX have expertise setting up GA4 events and channels?

**Megan Dickey:** We have the expertise, but it's about resource allocation. We're hiring an SEO specialist, but getting that next level of support requires revisiting the contract. Right now we provide content, Looker dashboard, and eventually our own analytics dashboard that's more robust than Looker. Anything extra requires a different scope conversation.

**Kezia Farnham:** We're open to reallocating resources or scoping this out. The key is: 100% ownership is non-negotiable, integration into our AI tools is critical, and we need version one running ASAP. Can we work through a list of desired integrations and KPIs, figure out what's possible now vs. requiring changes, and explore GA4 solutions?

**Megan Dickey:** That breakdown would be helpful.

**Megan Dickey:** I need a better understanding of what Diligent is using internally to track this. Is it GA4, Tableau, and your own AI tool? Is the goal for all data from us to automatically feed into your internal systems?

**Kezia Farnham:** We're shifting toward uploading a weekly view of deliverables—performance week-over-week and year-over-year, tracking against targets and factoring in market shifts, and comparing against top competitors. Right now we're in the messy middle with monthly views and manual weekly reporting. We want to automate that. If we have everything in one place—whether Looker Studio or GA4—and can download and upload it into our systems, we can focus on analysis instead of just moving numbers around week to week.

**Megan Dickey:** What internal system are you using?

**Kezia Farnham:** Glean AI. It connects our entire ecosystem and we're integrating as many systems as possible because it makes workflows faster, more efficient, and gives us much better visibility.

**Megan Dickey:** I'll chat with our client ops and engineering teams to see what's possible, figure out cost or reallocation, and we can determine direction. I think we'd almost need to custom build this because it doesn't exist right now. But our engineering team loves a good challenge. The question is bandwidth. Start with a clear list of ideal integrations.

**Kezia Farnham:** We can look at the ideal state, what's sub-tier to that, and alternative options like GA4 or Excel exports—whatever gets us the least amount of work every week.

**Jo Kaminska:** That's always the goal. We have weekly overviews in Looker. Next week we can go over each report and explain how they work. I also checked your GA setup. You're tracking leads but not qualified or converted leads. You'd need specific channel grouping to optimize GA and get MQL data. Each company tracks differently, so if we understand your requirements and how you measure internally, we can check with engineering what's viable.

**Kezia Farnham:** On my list: provide a list of integrations, metrics, and how you track HMQLs internally, plus the category breakdown for Slack updates. Thanks so much for that.

**Jo Kaminska:** Thank you so much for today.
