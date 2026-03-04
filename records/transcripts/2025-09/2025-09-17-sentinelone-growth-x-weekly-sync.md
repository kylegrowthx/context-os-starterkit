# SentinelOne <> Growth X - Weekly Sync

<metadata>
date: 2025-09-17
time: 13:31 UTC
duration: 23 minutes
organizer: nicolas.castellanos@growthx.ai
participants: Ankit Pahuja, Mansi Bhalothia, Aida Knezevic, Nicolas Castellanos, Marisol Smith
fathom_recording_id: 87843315
fathom_url: https://fathom.video/calls/412708384
share_url: https://fathom.video/share/HKsJdZc1xptysFyF9t1oYV8f375cBhTu
source: fathom
enriched_on: 2026-03-03 00:15 UTC
</metadata>

---

## Summary

GrowthX and SentinelOne aligned on the vulnerability database architecture, confirming that Nicolas will review code before integration with Content Stack while the web teams coordinate on component reuse—plus finalizing the search and filtering UX for the CVE index page. SentinelOne's AI visibility jumped 30% over the last 12 weeks (now 45% vs competitors in the last 7 days), with strong performance on "AI-driven cybersecurity solutions" content, while the team shipped the Engineering Hacking blog and has four more articles in review. GrowthX committed to delivering a Looker dashboard combining GA4 and GSC data (including LLM referral traffic) for next week's sync so the team can track how published content is performing in LLMs.

---

## Context

SentinelOne is a leading endpoint security platform that GrowthX is helping scale through content marketing and AI visibility optimization. This is a weekly working sync between the SentinelOne product and marketing team (Ankit Pahuja, Mansi Bhalothia) and GrowthX's project team (Aida Knezevic, Nicolas Castellanos, Marisol Smith, plus Sydney Go from content ops). The relationship centers on three concurrent workstreams: building a vulnerability database (CVE index) as part of SentinelOne's content expansion into deeper technical resources, creating high-quality content on cybersecurity topics to drive organic visibility, and tracking SentinelOne's AI visibility metrics through Scrunch (an AI visibility tool) to understand how well the platform's content appears in LLM responses. Nicolas joined this call briefly to discuss the code review requirements for integrating the database with Content Stack but handed it off to the web team for deeper technical work.

---

## Relevance

**To GrowthX Delivery:**
- Vulnerability database project is moving to dev phase; code review and web team collaboration (with SentinelOne's web team) needed before Content Stack integration—archetype for reusable component libraries
- Content publishing workflow clarified: SentinelOne will handle publishing; GrowthX's role is drafting and staging
- Looker dashboard combining GA4 + GSC with LLM referral traffic tracking will be model for tracking AI visibility impact on organic traffic for other CheckThat clients

**To CheckThat:**
- SentinelOne's AI visibility metrics demonstrate strong CheckThat performance: 30% growth over 12 weeks, 45% vs competitors in last 7 days, overwhelmingly positive sentiment
- "AI-driven cybersecurity solutions" topic showing 20%+ visibility increase—concrete evidence of topic optimization driving LLM appearance
- Behavioral analysis and threat prevention prompts showing slight decline—opportunity for content strategy adjustment to improve performance on specific keywords

**To GrowthX Business Development:**
- SentinelOne expansion opportunity: successful content execution (5+ articles in flight) shows strong account health and content appetite
- Potential reference case: vulnerability database + content strategy delivering measurable AI visibility wins
- Sydney Go now has Content Stack access and is actively staging content—sign of deepened integration and account momentum

---

## Overview

- Vulnerability database design finalization in progress; filtering logic and UX to be determined
- Content publishing process clarified; SentinelOne to handle publishing in Content Stack
- AI visibility increased by 30% over 12 weeks; SentinelOne outperforming competitors
- Looker dashboard combining GA4 and GSC data to be prepared for next week

---

## Key Topics

### Vulnerability Database Development

  - Code review needed before integration with Content Stack
  - Web team collaboration required for component alignment and optimization
  - Filtering and search logic for index page to be finalized
  - List of filters shared by Ankit; Loom video to be recorded for implementation guidance
  - George Main to finalize designs this week for dev team integration

### Content Strategy and Publishing

  - Sydney now has Content Stack access for content staging
  - Status updates on various articles:
      - Engineering hacking blog published today
      - AI compliance, prompt injection attack, adversarial attack with PMM for review
      - NIST article under Mansi's review
      - Penetration testing article pending delivery
  - Five new topics for this week shared in chat
  - SentinelOne to handle content publishing in Content Stack

### AI Visibility and Scrunch Updates

  - 30% growth in AI visibility over last 12 weeks
  - 45% visibility compared to competitors in last 7 days (up from 40% in last 90 days)
  - Overwhelmingly positive sentiment; SentinelOne mostly appearing at top or middle of LLM responses
  - 12% of citations from SentinelOne's website; majority from third-party sites (normal trend)
  - "AI-driven cybersecurity solutions" topic visibility increased by over 20%
  - Some prompts (e.g., behavioral analysis for cyber threat prevention) showing slight decline

### Design Assets and Brand Guidelines

  - Font files received; additional brand color kits requested
  - Christian identified as point of contact for design, font, and icon assets

---

## Action Items

**Mansi Bhalothia (SentinelOne)**
- Review NIST article
- Review new topics (5 listed in chat), share any notes/feedback

**Ankit Pahuja (SentinelOne)**
- Record Loom video explaining vulnerability type implementation for CVE database filters

**Aida Knezevic (GrowthX)**
- Contact George Main to ensure he has all needed info to finalize Figma designs this week
- Prepare Looker dashboard combining GA4 & GSC data, including LLM referral traffic page, for next week's meeting

---

## Transcript
**Ankit Pahuja:** Hi.

**Aida Knezevic:** Hi.

**Nicolas Castellanos:** Hi.

**Nicolas Castellanos:** Hello.

**Aida Knezevic:** How's it going?

**Ankit Pahuja:** Good.

**Ankit Pahuja:** How's it for you both?

**Aida Knezevic:** Good, pretty busy.

**Aida Knezevic:** Are we waiting on anybody else?

**Ankit Pahuja:** Are we good to start? I think we can begin. We can wait a moment for Mahati to join.

**Aida Knezevic:** Okay.

**Aida Knezevic:** So Nicolas is here today because Sydney mentioned you need to do a code review before we push code to Content Stack. We wanted to get a better idea of what that would look like.

**Ankit Pahuja:** That's right.

**Aida Knezevic:** That's more on the web team, particularly with Mahati and the other web team she works with.

**Ankit Pahuja:** That's why I requested to set up another call later, since they're all based out of PST.

**Ankit Pahuja:** They'll be able to help unlock the integration. On the last call with Shudru (VP of brand), Mahati, and Sydney, the idea was to integrate what you folks have built on the database side while ensuring we know what's getting integrated. Meanwhile, SentinelOne is migrating to Content Stack—Cybersecurity 101 is the first section. We're building some components and reusing others that are already in the roadmap to align both teams and avoid duplicating work.

**Ankit Pahuja:** This call isn't ideal for Nicolas since there are no web folks here. I'm setting up a weekly call with the web teams until we launch the vulnerability database because getting them together will help both teams achieve a sooner go-live.

**Aida Knezevic:** Okay, okay, sounds good.

**Aida Knezevic:** I'll take this back to Andy and we can set something up. The CVE design structure—the H2s and such—isn't going to change much, so Nicolas can already start building the data structure for the CVE pages.

**Aida Knezevic:** I had a quick question regarding the feedback on the Figma designs.

**Aida Knezevic:** Do you think anybody else will be providing feedback?

**Aida Knezevic:** Because if not, then our designer can just start incorporating all of that feedback and just finalize everything.

**Ankit Pahuja:** No more feedback. Drew gave the last feedback last week, so we're good. It's time to see a final front-end version. If something comes up, we'll go back to stakeholders, but we should be ready to move forward.

**Aida Knezevic:** That sounds good. George Main is going to book time on Friday to finalize everything, but I'll follow up to make sure that's locked in.

**Ankit Pahuja:** All right.

**Ankit Pahuja:** One thing I think is missing from the design side is how filtering and search logic will work on the index. Let me share my screen. We discussed filtering last week with Sydney—should we keep filters visible or create a sidebar for better filtering? And when someone searches a CVE ID, what happens? Is it a new page, a modal, a filtered table? Does it use the same design as this page? I have a list of filters to share, and I have thoughts on the UX around what happens when people search or apply filters here.

**Aida Knezevic:** Got it.

**Ankit Pahuja:** I'll share the filter list on Notion with my thoughts on implementation.

**Aida Knezevic:** That sounds good.

**Aida Knezevic:** Nicolas, I don't think we need you on this call. You can take the time back and focus on the other work.

**Nicolas Castellanos:** Yeah, I'll be in touch about the web team meeting. Thanks.

**Ankit Pahuja:** All right.

**Aida Knezevic:** Got it.

**Aida Knezevic:** Sydney now has Content Stack access and can stage content. For the five blogs I shared in the agenda, if you're ready to publish, Sydney can stage them.

**Mansi Bhalothia:** Quick update: the Engineering Hacking blog is being published today. AI Compliance, Prompt Injection Attack, and Adversarial Attack are with PMM for factual review. NIST is under my review.

**Mansi Bhalothia:** Can you help me get the Penetration Testing document? It was supposed to be delivered last week but I'm missing the doc link.

**Aida Knezevic:** Marisol, what's the status on that article?

**Marisol:** Sydney was reviewing it.

**Aida Knezevic:** Her comments are in. You just need to go through them.

**Marisol:** We can deliver it to SentinelOne once those are addressed.

**Mansi Bhalothia:** Got it.

**Mansi Bhalothia:** Can you help me with the new topics we're supposed to get this week?

**Aida Knezevic:** Yes, let me drop them into chat. These are the five topics we're working on this week. Do you have any notes we should know about while drafting?

**Mansi Bhalothia:** I'll take a quick look after this call and share any feedback.

**Aida Knezevic:** Great.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Those are the content updates. We'll get the remaining article from last week ASAP. Once it publishes, let us know on Slack and we'll update Airtable.

**Mansi Bhalothia:** We published the Prompt Hacking article. I'll send you the live link.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** I wanted to show you a Scrunch update. Scrunch recently updated their platform to allow historical data lookup. Previously you could only see 90 days of data, now we can track further back. Over the last 12 weeks, your AI visibility grew by 30%. Over the last 7 days it's up to 45% vs competitors, compared to 40% over 90 days. You're outperforming CrowdStrike and other competitors.

**Aida Knezevic:** Sentiment is overwhelmingly positive. You're positioned at the top or middle of LLM responses, rarely at the bottom. Most citations come from third-party sites, with your website featured 12% of the time—very normal across industries. LLMs prefer sites like G2, Trust Radius, Reddit for specific solutions. Your competitors are at similar percentages, so this isn't a performance issue.

**Ankit Pahuja:** Are there any changes to the list of topics and prompts we're tracking?

**Aida Knezevic:** We started with one set of prompts, then you provided additional ones to track. We haven't changed them recently. Adding new prompts skews the data since we start from zero tracking them, which could drop visibility temporarily while we collect data. We've been tracking the current set for a couple of weeks. There's a spreadsheet of the prompts we shared, but I can also add it to Notion for easier access.

**Aida Knezevic:** Looking at topics over the last 12 weeks, almost everything is in green except behavioral analysis for cyber threat prevention, which is down slightly. "AI-driven cybersecurity solutions" visibility increased over 20%, which is great news given AI visibility was an issue a few weeks ago. However, the prompt "who provides the best cybersecurity platform that uses behavioral analysis" is hurting overall visibility. CrowdStrike, Falcon, and Palo Alto show up there instead. This is important for content strategy.

**Aida Knezevic:** Mansi, thoughts on the content as you've been reviewing? Sydney mentioned to leave comments visible so you're not redoing feedback.

**Mansi Bhalothia:** Overall content is coming out nicely.

**Aida Knezevic:** Great to hear.

**Aida Knezevic:** Anything else you want to discuss?

**Ankit Pahuja:** A couple of things on the database progress. You're finalizing the front-end design. Can we touch on the filtering questions and that list?

**Aida Knezevic:** Let me open the Figma file. George Main looked at the font files—they're ready to go. Do you have any brand color kits to share?

**Ankit Pahuja:** Christian is the person to ask for design, font, and icon assets.

**Aida Knezevic:** Got it.

**Aida Knezevic:** The bigger question is how the menu will look once someone searches and what shows up. I'll discuss that with George Main. I have everything I need from you right now. I'll reach out on Slack if we need anything else.

**Aida Knezevic:** Marisol, do we need anything else from SentinelOne?

**Marisol:** We're good. We need to discuss filter strategy for SEO—rendering the same view with filtered tables is better for time on page. Nicolas needs to check how to connect the backend.

**Aida Knezevic:** That's a discussion for Nicolas and SentinelOne's web team. We'll set up a call with them.

**Ankit Pahuja:** I've pasted the filters I want to use. These are straightforward information from CVE pages except vulnerability type. I'll record a Loom video showing how to implement vulnerability type as a direction, then you can explore the rest.

**Aida Knezevic:** Got it.

**Ankit Pahuja:** I'll record a Loom showing vulnerability type implementation. I've got 500 tabs open, which is freezing my video.

**Aida Knezevic:** I feel that.

**Aida Knezevic:** I'll reach out to George Main to make sure he has everything he needs to finalize designs this week so Nicolas and the dev team can start integrating. On the publishing front, you'll handle publishing—we won't stage or publish content?

**Ankit Pahuja:** That's right, we're comfortable doing that.

**Aida Knezevic:** Got it. We'll prepare a Looker dashboard for next week. It combines GA4 and Google Search Console data with multiple traffic breakdowns, including LLM referral traffic. Combined with Scrunch data, you'll see which pages perform well in LLMs and how that correlates to your visibility.

**Ankit Pahuja:** We'll have it ready for next week.

**Aida Knezevic:** Thanks. I'll keep you posted.

**Ankit Pahuja:** Sounds good.

**Aida Knezevic:** Bye.
