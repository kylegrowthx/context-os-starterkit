# SmithAI <> GrowthX Weekly Sync

<metadata>
date: 2025-09-10
time: 17:30 UTC
duration: 33 minutes
organizer: megan@growthx.ai
participants: Maddy Martin, Julian Wan, Jo Kaminska, Megan Dickey
fathom_recording_id: 86353942
fathom_url: https://fathom.video/calls/405511853
share_url: https://fathom.video/share/8mcb2aGsYyVevg7qzY26sTPpxXgDAccr
source: fathom
enriched_on: 2026-03-03 00:15 UTC
</metadata>

---

## Summary

SmithAI and GrowthX aligned on progress with the industry page refresh (9 of 16 published) and reviewed the new Looker dashboard for automated performance tracking across Google Analytics and Google Search Console. The team discussed critical data exclusions (careers pages, chat keywords, internal users), event tracking priorities (CTA clicks and engagement time), and the need to monitor keyword cannibalization between landing pages and blog posts using SEMrush data. Jo also clarified access to Smith's Scrunch account to add prompts for new landing pages.

---

## Context

Smith.ai is a multi-location AI receptionist service. GrowthX is executing a major content refresh for Smith's website, publishing industry-specific landing pages to improve visibility in AI-driven search and traditional SEO. Julian Wan is Smith's senior growth lead, responsible for website development, CTAs, and page navigation; Maddy Martin manages the overall partnership and strategy. This weekly sync is part of ongoing content delivery to support Smith's growth metrics, particularly around LLM visibility (ChatGPT referrals) and commercial keyword rankings. The team is moving from manual reporting to automated Looker dashboards, which required establishing clean data hygiene rules.

---

## Relevance

**To GrowthX Delivery:**
- Content refresh workflow proven effective: 9 industry pages published with strong engagement rates comparable to overall session volume (per Jo's cohort analysis)
- Webflow workflow optimized: Vol as primary admin, Julian as backup for urgent changes — reduces dependency on single resource
- Data hygiene critical to reporting: exclusion rules for /careers, /now-hiring, and chat keywords must be applied consistently across all dashboards and reports
- Event tracking discipline needed: prioritizing CTA clicks and engagement time over noise metrics (scroll depth) — key for conversion focus

**To CheckThat / AI Visibility:**
- LLM referral tracking now live and actionable: ChatGPT expected to dominate; dashboard tracks which landing pages attract AI-sourced traffic
- Keyword cannibalization risk high: blog posts ranking for commercial keywords (e.g., "AI receptionist") displace higher-converting landing pages; requires ongoing SEMrush monitoring
- Scrunch prompts (190 currently) need refresh: Julian's new pages ("multi-location business," "custom instructions") require prompt updates to validate topic visibility in LLM queries

**To GrowthX Business Development:**
- Account health positive: proactive reporting setup, willingness to exclude noisy data, focus on conversion metrics indicate mature partnership
- Expansion opportunity: Julian's team seeking deeper event tracking (Rudderstack, Amplitude integration) — potential upsell for analytics consulting
- Renewal signal: Team moving beyond vanity metrics (traffic volume) to conversion accountability — suggests confidence in GrowthX's content strategy

---

## Overview

- Industry page refresh at 56% complete: 9 of 16 published; partner page staged and awaiting design direction (homepage and Aether product page as references)
- Looker dashboard now live with Overall, Non-branded, Cohorts, LLM traffic, and Landing pages tabs; filters by date, medium, and URL clusters
- Data exclusions required: /careers, /now-hiring, chat-related keywords; internal user exclusion remains challenging but essential for clean conversion metrics
- LLM traffic tracking shows ChatGPT as expected primary source; keyword cannibalization risk flagged for "answering service" vs. "AI receptionist" synonymy
- Event tracking priorities: CTA clicks and engagement time; Rudderstack and Amplitude integration under exploration; Scrunch account access clarified (team@growthxlabs.com)

---

## Key Topics

### Website Refresh Updates

  - 9 additional industry pages published, 7 remaining to complete the set
  - Partner page updates in progress; Megan working on non-live version for tweaks
  - Design direction: Use homepage and Aether product page as references, moving away from intermediate blue design

### Looker Dashboard Implementation

  - Automated reporting replacing previous screenshot-based updates
  - Data sources: Google Analytics and Google Search Console (no SEMrush data)
  - Key sections: Overall tab, Non-branded report, Cohorts, LLM traffic, and Landing pages
  - Ability to filter by date range, medium, and specific URLs or clusters

### Data Exclusion and Refinement

  - Need to exclude careers-related pages (/careers, /now-hiring) from all reports
  - Importance of focusing on non-branded keywords and queries
  - Discussion on excluding chat-related keywords and other irrelevant terms

### Event Tracking and Conversion Focus

  - Plans to incorporate key GA events into the dashboard
  - Primary focus on page engagement time and CTA clicks
  - Potential integration with Rudderstack and Amplitude data for more granular tracking
  - Challenge: Reliably excluding internal users (agents, staff) from engagement metrics

### LLM Referral Tracking

  - New report showing which LLMs drive traffic to the website
  - ChatGPT expected to be the primary source due to market share
  - Useful for validating hypotheses about topic visibility in AI-driven search

### SEO Strategy and Keyword Tracking

  - Need for more detailed keyword performance tracking, similar to Ahrefs functionality
  - Focus on preventing keyword cannibalization between landing pages and blog posts
  - Plans to identify and monitor top commercial keywords, ensuring landing pages rank for these terms

### Scrunch Account Management

  - Smith's Scrunch account (team@growthxlabs.com) is the official account; currently has 190 prompts
  - New landing pages require custom prompts to validate topic visibility in LLM queries (e.g., "multi-location business," "custom instructions for handling AI calls")

---

## Action Items

**Maddy Martin (Smith.ai)**
- Review staged referral page and templates on Webflow
- Provide Jo a list of important events to track after confirming with Julian

**Megan Dickey (GrowthX)**
- Update partner page text and modules once Vol provides edit access to non-live version

**Jo Kaminska (GrowthX)**
- Update Looker dashboard to exclude /careers and /now-hiring URLs across all reports
- Add SEMrush data to Looker and track specific commercial keywords and ranking pages
- Log into correct Smith.ai Scrunch account (team@growthxlabs.com) and add prompts for new landing pages

---

## Transcript
**Megan Dickey:** Yeah, yeah, yeah, my mouth still tastes like metal.

**Maddy Martin:** Hey, how are you?

**Maddy Martin:** Good, how are you?

**Megan Dickey:** How was the, I saw your little emoji, how was the nose work camp?

**Maddy Martin:** Yeah, yeah, it was great.

**Maddy Martin:** It was really fun.

**Maddy Martin:** We had, like, almost four full days of nose work instruction and, like, instructors from all over the country.

**Maddy Martin:** They put on, like, three of them every year in PA, Georgia, and Colorado, I think.

**Maddy Martin:** So, yeah, it was a really great group.

**Maddy Martin:** There were, like, 75 teams there.

**Maddy Martin:** So we took over, like, the entire camp, and it was awesome.

**Megan Dickey:** And so are you, like, competing or, like?

**Megan Dickey:** That's not a competition, but we do, yeah, as a team.

**Maddy Martin:** I mean, he's the nose and I'm the handler. If I do my job well, then we do well. He's very good at it. It's really fun and awesome.

**Megan Dickey:** I feel like my dogs would love that, but they're also not great around other dogs. I actually ended up looking up San Francisco Nosework. They said if your dog has leash reactivity, maybe skip.

**Maddy Martin:** I'm going to find another group because the Nosework programs that work with shelter dogs are actually becoming well known because they build confidence. I can send you a couple resources. For right now, check out the online courses. They have great stuff. They partnered with the National Association for Canine Centwork and other groups. The instructors are amazing. You get started with primary reinforcement — just food and toys. You don't even need odor to play the games. My reactive dog used to struggle being near other dogs, but now he can be in the same room and it's amazing.

**Jo Kaminska:** I'll check that out. I'll find a different organization that's more welcoming.

**Maddy Martin:** We're typically in a highly populous area where there's plenty of options.

**Megan Dickey:** I actually don't think we have officially.

**Julian Wan:** Oh, my God.

**Julian Wan:** We haven't.

**Julian Wan:** Hi, Joe.

**Julian Wan:** Hi, Megan.

**Julian Wan:** I'm Julian.

**Megan Dickey:** Yeah, actually, I don't mean to hijack the meeting.

**Julian Wan:** I have one quick question for GrowthX about managing our Scrunch account. We're launching two new pages and want you to build prompts for them. We want to test if AI thinks we're the best multi-location business and if we have the best custom instructions for handling AI calls for customers. I'll share the pages in the chat.

**Maddy Martin:** Those are very low volume search terms right now and you'll need to provide some guidance. Can you clarify what you mean by "custom instructions" — are we talking franchise locations? Maybe you can share the pages with Jo so she understands the context better.

**Jo Kaminska:** We currently have 190 prompts in the Scrunch account, so we can add custom prompts whenever needed. Send over these pages and we'll add a couple of new prompts.

**Julian Wan:** I did add two already but wanted to check in with you guys first since Maddy's been leading that. Let me find time with you this week.

**Maddy Martin:** Good to meet you, Julian. I'll finish his introduction. Julian is a senior growth lead responsible for all things website. He's talented with Figma but we don't ask him to do much design work because we have Aether, existing components, and we want to focus his time on higher-impact work. He's responsible for launching new pages, owns the online funnel, all the CTAs on the site, page navigation and development — mostly focused on high-growth pages. We don't typically involve him in blog work, which is more maintenance and SEO for the team.

**Jo Kaminska:** Yeah, awesome.

**Megan Dickey:** Sweet.

**Megan Dickey:** Okay, so on the topic of the website refresh, Vol was able to stage the referral page that we've been iterating on, pulling modules from the homepage onto that page. You can now click around and explore to make sure everything is set.

**Maddy Martin:** I'll review that and the templates as part of my catch-up, and we'll look over the dashboard today. Thank you for working closely with Vol. If he's ever unavailable and something is urgent, Julian has almost the same level of familiarity and access to Webflow, so he's a good backup.

**Megan Dickey:** We've published nine additional industry pages. There are just seven left to go. Then we're moving on to the partner page — the overarching one. I've asked Vol to give me edit access to a non-live version so I can make tweaks. We can update the text and pull some modules from the homepage to that page.

**Maddy Martin:** Right, the partner page is really their introduction to Smith.ai and functions as a landing page for partners. Use the homepage and Aether product page as design direction. The intermediate blue design was a hurry-up approach. Julian mentioned the multi-location and custom instructions pages are also new, so pull those new pages from that design framework too.

**Megan Dickey:** Let's go to Jo — pull up the Looker dashboard.

**Jo Kaminska:** Previously you were getting screenshots. This Looker dashboard is automated — new pages automatically update it without manual intervention. We have Overall, Non-branded, Cohorts, LLM traffic, and Landing pages tabs. Data sources are Google Analytics and Google Search Console — no SEMrush, so this is the most accurate data for Smith.ai. The Overall tab shows sessions and engaged sessions by landing page, referrer, and query distribution. We can filter to GrowthX-worked URLs only. Engagement rates look good. Query distribution comes from Google Search Console showing keyword rankings by position.

**Maddy Martin:** The critical thing is we need to exclude careers and hiring pages across the entire Looker dashboard — /careers and /now-hiring.

**Jo Kaminska:** We can update it. The non-branded report is the best one since non-branded shouldn't include career pages. I'll talk with our analytics team to apply the exclusion across all reports. Non-branded means anything that doesn't include your brand name variation. Most reports are done by cohort. It's better to exclude specific URLs. Once we apply that exclusion, we can see week-by-week progress on clicks, impressions, and CTR.

**Maddy Martin:** Average position isn't as important as tracking specific keywords. Looking at all this data en masse makes it hard to get a directional sense of performance. The most important thing is tracking top keywords.

**Jo Kaminska:** Yeah, you can also see, like, week by week, so as you said, like, after weeks with careers, we can actually see, you know, like, the progress when it comes to clicks, impressions, CTR, average position.

**Jo Kaminska:** And average position, I wouldn't say that's very important because the average of positions, like, which is, like, too much of a metric.

**Jo Kaminska:** Right.

**Maddy Martin:** The most important keywords, like, that's, you know, a requirement that we would probably care about because looking at all this, like, you know, en masse, it's really hard to get a directional, you know, sense of is it good or not, right?

**Maddy Martin:** So how do you read this report? What stands out to you?

**Jo Kaminska:** I focus on cohorts, LLM traffic, and landing pages. Queries are a good report to see where you rank for specific terms. The all queries report shows which searches drive clicks.

**Maddy Martin:** Answering service and AI receptionist keywords are converging. Google and LLMs are uncertain about the definitions, so these keywords are more synonymous in search than in the real world. It's not necessarily something to avoid — people searching for "AI receptionist" sometimes search for "answering service" instead. They may not type "AI" because they assume everyone offers AI. It depends on their industry maturity and peer network. We don't always include "AI" in the keyword. Also, there's a brand overlap with terms like "Chatsmith" — we don't care about chat keywords. So we need exclusion rules for careers, chat, and any brand-related terms.

**Jo Kaminska:** Chat should also be excluded from non-branded reports. I can check exceptions and use regex filtering. For the reports I check most — cohorts are important, plus LLM traffic. We can see what content we produced divided by topic clusters versus non-GrowthX URLs.

**Jo Kaminska:** So I think like particularly industry refresh pages are very important because like, I don't know, like comparing, like considering the whole August, for example.

**Jo Kaminska:** So here we always compare data to the previous period, so August to July.

**Jo Kaminska:** So basically like seeing industry refreshes, you know, the growth in when it comes to sessions, engagement rate is slightly lower, but still pretty, pretty high.

**Jo Kaminska:** So engaged sessions compared to the overall sessions.

**Jo Kaminska:** Depending on the project type, I check data accordingly. For industry page refreshes, we're driving more sessions with similar engagement — a good sign. I track month-over-month. For quarterly reporting, we do screenshots and detailed description summaries.

**Maddy Martin:** With GA, now that we have solid event data from Julian (he's the primary event tracking person, I'm backup), we can layer in the most important events. We want to focus on CTA clicks and page engagement time — not scroll depth or time on page. The key is whether they spent any time on the page and whether they clicked a CTA.

**Jo Kaminska:** Which events are most important to you right now? We can filter to conversion-focused events and see which pages are driving those events. We can also build a landing page dashboard showing sessions and events by URL.

**Maddy Martin:** I have a meeting with Julian in an hour. I'll make sure my list of important events matches his and I'll provide it to you. We're also using Rudderstack and Amplitude for events, so Julian might prefer those as data sources over GA. If so, we can get you Looker Studio access for those data points.

**Jo Kaminska:** We don't typically connect other analytics platforms, but I've worked with clients who switched from GA to Amplitude for granular conversion tracking and reported within Amplitude on top of Looker dashboards.

**Maddy Martin:** The main challenge for us is excluding internal users reliably. We have hundreds of agents plus ops, marketing, and sales staff. We need to exclude anyone logging in as staff from our engagement metrics before the data is clean. It affects GA but more significantly Amplitude. IP addresses sometimes work, but there's no perfect solution.

**Maddy Martin:** You have to pick a lane and stick to the criteria. All the data sources — Scrunch, Google Analytics, Google Search Console, SEMrush, Ahrefs — point in the same direction of where the website is going. There's always some discrepancy, but they're directional. We also have Facebook audiences built from site engagement criteria. Those events are both direct and indirect — they contribute to audiences we retarget later. Even if they don't convert directly, they build the audience. Prior engagement might get them added to that audience.

**Jo Kaminska:** The last report shows Scrunch data with custom prompts and results. The LLM referral breakdown shows which LLMs drive traffic to your website. ChatGPT is usually first due to market share, but it's good to track which pages get LLM traffic — this confirms your hypothesis about topic visibility.

**Maddy Martin:** This is very helpful. At a high level, this dashboard works well, but operationally it's very bird's eye. I'd also like an Ahrefs-like view — pick a topic like "AI receptionist," see the top 10 ranking keywords in that bucket, and track how they've changed over the last 30 days. I want to make sure we're not losing ground on the most important keywords. Also, which page ranks for each keyword? That changes over time. It's risky when a blog post suddenly ranks instead of the primary landing page — conversion rate tanks and we lose the position eventually. We need to manage keyword cannibalization and prevent that.

**Jo Kaminska:** We can add SEMrush data using the organic research tab to see which pages rank for specific keywords. For commercial keywords, landing pages should rank. If a blog post ranks for commercial terms, we should merge it or change its intent. Landing pages are money pages with higher conversion rates. Blog posts have lower probability. We can track important commercial keywords and monitor for abnormal week-over-week changes.

(Technical issue: Megan lost power connection; team planned to continue async.)

**Megan Dickey:** Quick thing before I jump to another call — Smith has their own Scrunch account. If you log in with your personal GrowthX email, you'll see a Smith account, but Smith created their own Scrunch account. You should log in with the team@growthxlabs.com account to access the Smith Scrunch. Elvis set this up before I came on board.

**Jo Kaminska:** I'll check it out and confirm I'm using the correct account so we can add the new landing page prompts.

**Megan Dickey:** Yeah. We can also get clarity on how they came up with the existing prompts. Let's chat about that next week.
