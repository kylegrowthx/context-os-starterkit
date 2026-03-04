# Jason / Nathalie - Surge + Augment Code updates

<metadata>
date: 2025-09-17
time: 16:44 UTC
duration: 47 minutes
organizer: nathalie@growthx.ai
participants: Jason Gong (GrowthX), Nathalie Schrans (GrowthX)
fathom_recording_id: 87936309
fathom_url: https://fathom.video/calls/414274502
share_url: https://fathom.video/share/Lx2EiWoiNWYS-1n1dFzNXUYaXpxECNYF
source: fathom
enriched_on: 2026-03-03 12:45 UTC
</metadata>

---

## Summary

Jason and Nathalie aligned on a parallel approach to Augment content: publish easy, high-volume content (like "How to sort an array in C++") to buy time while quality issues are fixed systematically. They committed to building an automated Airtable dashboard for weekly performance reporting, pulling traffic and presence metrics from PostHog, Beehive, VGSC, and Scrunch. Nathalie will create a structured content roadmap mapping topic clusters to content types (listicles, comparisons, alternatives), identify 20-30 high-potential articles for refresh, and document content quality gaps by category so Jason can work with Marisol and engineering on workflow improvements.

---

## Context

Jason and Nathalie are core team members at GrowthX working on Augment (CheckThat's AI visibility product). This meeting was a working session reviewing progress on two tracks: Surge (GrowthX's external social media brand for founder Edwin) and Augment (content, tracking, and publishing). For Surge, they discussed voice and positioning — making sure social content resonates with technical audiences (Hacker News, HN comment threads) rather than defaulting to corporate tone. The bulk of the meeting focused on Augment: the team had been trying to report manually on content performance, but Jason wanted to systematize that with an automated dashboard. In parallel, Nathalie was beginning to notice quality issues across articles (structure problems in listicles and comparisons, fact-checking gaps in new content on spec-driven development and agentic swarms). Rather than redesign workflows immediately, they agreed to identify and document the problems first, then involve engineering.

---

## Relevance

**To GrowthX Delivery:**
- Nathalie's discovery of structured article issues (listicles and comparisons lack consistent format despite good underlying content) reveals a pattern that should inform how GrowthX approaches content template design and workflow automation for other clients
- The decision to separate high-volume publishing (simple topics) from quality improvement (20-30 article refresh list) is a delivery model shift: manage client expectations by setting a pace, then incrementally improve without disrupting output
- Plan to document issues category-by-category before engineering work ensures better spec writing and reduces rework cycles

**To CheckThat / Augment:**
- Backlink strategy for "Best AI Coding Tools 2025" article is producing measurable results — the article is now ranking for more keywords and being picked up by LLM prompts. Plan to update titles to include year and add "last updated" dates to signal recency to LLMs
- Critical finding: ChatGPT and other LLMs appear to be searching variations of article titles (e.g., "best AI coding tools 2025") in the background when prompts are executed. Adding publication year and last-updated dates directly to articles is now a core tactic for AEO visibility
- Current Augment prompt tracking (180 prompts in Scrunch) needs standardization — wording should be consistent (e.g., all "X as an alternative to Y" format) and comprehensively mapped to planned content (listicles, comparisons, alternatives clusters)

**To GrowthX Business Development:**
- Cadence of content roadmap updates (2-3 weeks out) and structured refresh plan shows operational maturity. Communicating this to prospects and clients demonstrates planning discipline
- Strong engagement on both Surge (founder voice positioning) and Augment (internal tool building) signals healthy team capacity and strategic diversification

---

## Overview

- Need to develop a structured content roadmap for upcoming weeks, focusing on high-potential topics and improving quality
- Implement automated performance tracking dashboard using Airtable for efficient reporting
- Review and optimize tracking of prompts for Augment, ensuring comprehensive coverage of relevant clusters
- Prioritize refreshing high-potential listicles and comparison articles to improve content quality

---

## Key Topics

### Content Strategy and Roadmap

  - Nathalie to create a content roadmap, outlining topic clusters and content types for the next 2-3 weeks
  - Focus on easily producible content (e.g., "How to sort an array in C++") to buy time for quality improvements
  - Identify 20-30 high-potential articles for refreshing, starting with 1-2 per week
  - Prioritize listicles, comparisons, and alternatives as high-performing content types

### Performance Tracking Dashboard

  - Implement automated Airtable dashboard for weekly reporting
  - Key metrics: articles published, newsletter stats, traffic (pages, impressions), signups, email subscribers
  - Include presence metrics for Augment (percentage and total number of prompts with presence)
  - Jason to task Suleman with setting up the dashboard, pulling data from various sources (PostHog, Beehive, VGSC, Scrunch)

### Content Quality Improvement

  - Nathalie to document issues and gaps found during editing process
  - Focus on improving structure for listicles and comparisons
  - Separate immediate manual improvements from long-term workflow enhancements
  - Schedule call with Jason and Marisol to create engineering tickets for workflow improvements

### Augment Prompt Tracking

  - Review and optimize current prompt tracking in Scrunch
  - Ensure comprehensive coverage of relevant clusters (e.g., alternatives, best tools)
  - Standardize prompt wording for consistency (e.g., "X as an alternative to Y")
  - Nathalie to map tracked prompts to planned content topics

### SEO and Backlink Strategy

  - Backlink strategy showing positive results, improving keyword rankings
  - Update article titles to include year (e.g., "Best AI Coding Tools in 2025") for better LLM visibility
  - Add "last updated" dates to articles to signal recency to LLMs

---

## Action Items

**Jason Gong (GrowthX)**
- Task Suleman to set up automated reporting in Airtable. Pull data from PostHog, Beehive, VGSC, Scrunch. Dashboard should include weekly counts for articles published, traffic (pages, impressions), signups, email subscribers, and Augment presence metrics (percentage and total number of prompts with presence).

**Nathalie Schrans (GrowthX)**
- Create structured content roadmap doc mapping topic clusters, content types (listicles, comparisons, alternatives, coding questions, use cases), and planned articles for next 2-3 weeks. Share with Jason by tomorrow morning.

- Identify and select 2 high-potential articles (listicles or comparisons) from PostHog for refresh this week. Document improvement process and any repeated issues found.

- Document content quality gaps and issues found during editing, organized by category (structure, fact-checking, consistency). Prepare for call with Jason and Marisol to create engineering tickets for workflow improvements.

- Review and optimize Augment prompt tracking in Scrunch (currently 180 prompts). Ensure comprehensive coverage of all relevant clusters. Standardize prompt wording (e.g., "X as an alternative to Y"). Map tracked prompts to planned content topics.

- Update "Best AI Coding Tools" article: add "2025" to title, ensure "last updated" date is visible. Both signals help LLMs determine recency when generating responses.

---

## Transcript

**Nathalie Schrans:** This meeting is being recorded.

**Jason Gong:** Yeah, so ping me when you need help there.

**Nathalie Schrans:** Then for Augment. What's the GitHub for?

**Jason Gong:** So basically there's a feature in Cloud Projects where you're giving it a bunch of files. GitHub is just a way to manage that. For example, this is my search social admin thing.

**Nathalie Schrans:** Perfect.

**Jason Gong:** And one way to do it is it just syncs to your cloud project. Oh, that's cool. You got text files and stuff like this, and it'll automatically update.

**Nathalie Schrans:** Yeah, so if I add to it or if you add to it.

**Jason Gong:** Right. I mean, you'll have to learn how to use GitHub.

**Nathalie Schrans:** What's another tool that I have to learn?

**Jason Gong:** It's fine. This is the thing you put together for Edwin.

**Jason Gong:** I think we should change this a little bit. This is positioning narrative. And then this is tone.

**Nathalie Schrans:** This is Edwin's tone?

**Jason Gong:** This is the company narrative. I go through that in the video.

**Nathalie Schrans:** And I just had it on when I was writing.

**Nathalie Schrans:** What kind of feedback have you gotten from Edwin?

**Jason Gong:** Edwin changes his mind a lot, but in general we have the tone he's happy with. This one he liked, this one he thought was a little awkward.

**Nathalie Schrans:** I remember it was posted and he said it was fine. The new one?

**Jason Gong:** Yeah, it's a little too corporate. There are a few pillars he wants to hit: the quality of workers, how many have PhDs or are scientists, healthcare professionals.

**Jason Gong:** I think the benchmark in my head is Hacker News — what would resonate with that audience. For example, if we do post-training as a topic, you can read what people are saying on Hacker News. People are really skeptical, so if that's the voice in your head, I think it would help.

**Nathalie Schrans:** As references for voice?

**Jason Gong:** As a good voice, yeah. LinkedIn is harder to find good examples of technical leaders posting regularly. But what we wrote for Edwin is fine — you're almost refusing to play the engagement game with stupid hooks, while still doing that. The Hacker News comment threads on OpenAI or Anthropic releases have interesting perspectives. I'm looking for people trying to actually educate, not just picking apart details.

**Nathalie Schrans:** Do you know Dan Shipper from Every? He's active on LinkedIn, mostly reposts though.

**Jason Gong:** Setting up GitHub will take a bit of time, so we'll have someone help with that. These writing references are more for writers than technical audiences. Researcher personal blogs are too technical. Hacker News and general tech news is probably the best source.

**Nathalie Schrans:** Anything else before Augment?

**Jason Gong:** I don't think so.

**Jason Gong:** Augment, let's go through the different lanes. How do you feel about the content things we talked about earlier?

**Nathalie Schrans:** I want to make sure I have the right numbers in the Workstream Progress Tracker.

**Jason Gong:** The data you pulled makes sense — pages that are indexed, impressions, clicks. But we should figure out who was pulling the data before and from where. Let's just start defining what we want, then get somebody to create it.

**Jason Gong:** I think we'll have to do it in Airtable, not Notion, because we need it automated. Let me split this out: outputs (articles published, newsletter) and performance (traffic, signups, email subscribers, and Augment presence metrics).

**Nathalie Schrans:** For presence, do we want both percentage and total number of prompts with presence?

**Jason Gong:** Yes, presence covers citations and mentions together. That's good. The dashboard should be a North Star metric — they can click into it for deeper details.

**Jason Gong:** I'll task Suleman to set this up. Articles published is manual, but the rest pulls from PostHog, Beehive, VGSC, and Scrunch into Airtable. I'll send him the recording.

**Nathalie Schrans:** That makes sense. Should I put the lanes update under content?

**Jason Gong:** Yeah, content is just a lane. Do you feel we'll have clear things to publish or refresh every week for the next few weeks?

**Nathalie Schrans:** Marisol is finishing keyword research. I've done some research already and found patterns that repeat across programming languages and verticals. We should have enough for two to three weeks, then mix new and refreshed content. I'll create a roadmap tomorrow while I'm in the office.

**Jason Gong:** Great. Share the research doc. In general, there's not enough structure to what we're publishing — it feels ad-hoc. A plan showing content tree, pillars, clusters, listicles, comparisons, coding questions, and use cases would help. Every week we'd have clarity on what's next.

**Jason Gong:** But we also need to fix quality in parallel. We can do simple topics like "How to sort an array in C++" — super easy, high impressions, buys us time while we improve. Listicles and comparisons are high-performing content types.

**Nathalie Schrans:** I've edited enough to know the issues. Listicles and comparisons have structure problems — inconsistent formatting, even though the content is good. I'm now editing Marisol's new pieces on spec-driven development and agentic swarms, which require fact-checking since I'm not an expert.

**Jason Gong:** So categorize by content type. For each category, what's our process to create a better version? For listicles, show me what a good one looks like — highest potential articles worth refreshing.

**Nathalie Schrans:** Understood. I'll go into PostHog, pick two high-potential listicles or comparisons this week, refresh them, and document the gaps. Then we schedule a call with you and Marisol to create engineering tickets.

**Jason Gong:** Perfect. That's the two-track approach: one or two articles refreshed each week (using whatever method works), and documenting workflow gaps so we can work with engineering. Don't redesign workflows yet.

**Jason Gong:** On the other thing — the prompts we're tracking for Augment. We have about 180 prompts in Scrunch. I want to audit everything to make sure we're tracking what we should. Listicles, comparisons, alternatives — there are some duplicate or unclear ones.

**Nathalie Schrans:** I've thought about this. For a prompt, citations come from 20-25 types of articles. We should add that to article titles. And LLMs use published date and last updated date to determine recency.

**Jason Gong:** That's exactly what I was thinking. We should update "Best AI Coding Tools" to include 2025 in the title and ensure a last updated date is visible.

**Jason Gong:** On prompts, if you're doing from scratch, standardize the wording — "X as an alternative to Y" format — across all variants. Then map them to the content you're actually planning to create.

**Nathalie Schrans:** Can you send me that link?

**Jason Gong:** Sure. Newsletter is fine on hold. The other category is still under development — design person gave minor comments. We're pushing forward there. The backlink strategy is working — the "Best AI Coding Tools" article is showing up in more keywords now. Once it's on pages one through five of SERPs, LLMs pick it up because they're so authoritative.

**Nathalie Schrans:** I need to leave for a meeting with Andy, but I'll go through everything and prioritize social posts for Surge today so you can review.

**Jason Gong:** Sounds good. Let's do that Augment exercise tomorrow if you're in the office.

**Nathalie Schrans:** I'll be there.

**Jason Gong:** Great. See you tomorrow.
