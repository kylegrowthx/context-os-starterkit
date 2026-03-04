# Monograph <> Growth X - Weekly Sync

<metadata>
date: 2026-01-14
time: 18:01 UTC
duration: 18 minutes
organizer: katya@growthx.ai
participants: Katya Luscomb (Growth X), Allison Terres (Monograph)
fathom_recording_id: 114280299
fathom_url: https://fathom.video/calls/530900248
share_url: https://fathom.video/share/uhVom5EDV-xa5gKd63NP8ufcYZf8dww4
source: fathom
enriched_on: 2026-02-28 10:45 UTC
</metadata>

---

## Summary

Katya Luscomb and Allison Terres align on Growth X's SEO performance tracking and strategy for Monograph. The Looker dashboard (GSC/GA4) was shared for self-serve access to pillar-level metrics. Critical competitive threat identified: Dell Tech is outranking Monograph for AI keywords, requiring analysis of site-wide optimization strategy. Monograph's Metabase report on Sales Qualified Opportunities (SQOs) will be integrated into Growth X's reporting. Future content strategy will balance high-volume top-of-funnel traffic with high-intent keywords aligned to Monograph's ideal customer profile.

---

## Context

Monograph engaged Growth X to improve organic content performance and drive qualified inbound traffic. This meeting occurs mid-January 2026 following initial performance reporting and dashboard setup. Growth X had recently completed a Looker dashboard pulling from Google Search Console and Google Analytics 4, filterable by content pillar. Monograph's internal team requested deeper visibility into performance metrics and expressed concern about competitors (specifically Dell Tech) gaining ranking advantage in AI-related keywords. The meeting also addresses Monograph's move toward more intentional keyword targeting and SQO attribution tracking.

---

## Relevance

For Growth X: Demonstrates dashboard implementation, competitive threat analysis, and integration of client data sources (Metabase/SQOs). Shows positioning of Growth X's in-house AI visibility tracker versus third-party tools like Scrunch. Highlights need for deeper analysis of competitor SEO strategies and site-wide optimization. Establishes ongoing reporting cadence with monthly SQO export. For Monograph: Establishes shared dashboards and clear metrics for content performance, directly linking organic traffic to pipeline impact (SQOs). Identifies competitive vulnerability in AI keywords that demands strategic response.

---

## Overview

Four key outcomes emerged from this weekly sync:

1. **Looker Dashboard Shared:** Growth X's Looker dashboard now provides Monograph with real-time access to performance metrics (Google Search Console clicks/impressions and Google Analytics 4 sessions) filterable by pillar and Growth X content only. Enables self-serve exploration of performance across content clusters.

2. **Competitive Dell Tech Threat:** Dell Tech is outranking Monograph for AI-related keywords, likely due to site-wide optimization rather than individual article-level SEO. Growth X will investigate Dell's strategy and loop in in-house AI optimization experts for strategic recommendations.

3. **SQO Attribution Integrated:** Monograph will export their internal Metabase report (tracking Sales Qualified Opportunities influenced by organic content, via last-touch attribution) monthly. Growth X will integrate this into performance reporting to show direct pipeline impact.

4. **Strategy Rebalancing:** Future content strategy will deliberately balance high-volume top-of-funnel content with high-intent, ICP-aligned keywords (e.g., "billing and invoicing architect software"). Keyword tracking by pillar will be added to Looker to track wins over time.

---

## Key Topics

### AI Ranking Threat: Dell Tech

  - **Problem:** Dell Tech is outranking Monograph for AI-related keywords.
  - **Hypothesis:** Dell Tech's entire site is better optimized for AI, not just specific content.
  - **Urgency:** This is a critical threat that must be addressed immediately to avoid falling behind.
  - **Data Source:** Current AI insights come from the Scrunch platform, which provides site-wide data, not per-article breakdowns.
  - **Future Tool:** Growth X is building an in-house AI visibility tracker with a richer prompt library for deeper insights.

### Reporting & Data Access

  - **Looker Dashboard:** Now shared with Allison.
      - **Data Sources:** GSC (clicks/impressions) & GA4.
      - **Key Feature:** Filterable by "Growth X specific content" and by content pillar.
  - **Metabase Report (SQOs):** Monograph's internal report will be integrated into Growth X's reporting.
      - **Purpose:** Track organic content's influence on Sales Qualified Opportunities (SQOs).
      - **Attribution:** Last-touch influence (e.g., blog visit → demo request).
      - **Performance:** 11 SQOs in Dec 2025; 9 already in Jan 2026.
      - **Action:** Allison will export the report monthly for Katya. Katya may request direct Metabase access.

### Performance Deep Dive

  - **AI Implementation Pillar:** Engagement data is skewed by a mix of content types.
      - **High-Intent Pages:** Lower traffic but higher engagement.
      - **Listicles:** High traffic but lower engagement.
  - **CRM Pillar:** November data is not a reliable baseline.
      - **Reason:** Only 3 articles were published in November.
      - **Action:** Analyze December data (from \~15 articles) for a more accurate view.

### Future Strategy & Tracking

  - **New Pillars:** Allison shared updated content pillars. Katya will review them to adjust Looker cohorts.
  - **Keyword Tracking:** Allison requested keyword tracking by pillar, especially for high-intent topics like "billing and invoicing architect software," to demonstrate clear wins.
      - **Status:** Keyword data is in Airtable; Katya will investigate adding it to Looker.

---

## Action Items

**Katya Luscomb (Growth X)**
- Post Slack recap to Allison with Looker dashboard link
- Analyze AI Implementation pillar engagement and traffic/engagement mix; share findings with Allison
- Analyze CRM pillar performance using December data (now with ~15 articles vs. 3 in November); share findings with Allison
- Review Allison's new content pillars; propose Looker cohort adjustments; investigate keyword tracking by pillar in Looker; set up specific tracking for "billing and invoicing architect software" and other high-intent keywords
- Investigate Dell Tech's AI ranking strategy; loop in Growth X's AO (AI Optimization) experts; share findings and recommendations with Allison
- Add monthly Metabase SQO export to Growth X's reporting checklist for ongoing monthly integration

**Allison Terres (Monograph)**
- Review Looker dashboard; post Slack comments to Katya regarding any missing visualizations or needed adjustments
- Export Metabase SQO report at month-end; send to Katya monthly (starts with January 2026 numbers); request direct Metabase access for Katya if needed

---

## Transcript

**Katya Luscomb:** Hey, Allison. Oh, you're muted.

**Allison Terres:** Hey, how's it going? How are you doing? Good.

**Katya Luscomb:** Good. Thank you. Thanks for all the feedback and questions on the performance report. Definitely got some follow-up. I had some initial investigations and some points I figured we could kind of chat about briefly, but I do want to dig more into each of those to make sure that I'm highlighting the most actionable steps.

**Allison Terres:** Cool. Okay, perfect. Yeah, this is me getting more involved. That's great. One thing I was curious about is I think I did pull out a comment a few times about visualizations, which I always find really helpful when talking about SEO and growth and all this data stuff.

**Katya Luscomb:** Yeah, so I've actually linked it here. I realized that it was only shared with Robert this morning when you asked. We've got this Looker dashboard. It's linked in the agenda, and I'll send it over in Slack as well. It's got a variety of visualizations. I need to poke around and see if it has all of the specific visualizations that you were asking about, because there's a heap of different things in here. And potentially, if there's a visualization that you would like that's not reflected in here, I can chat with my team, who have a lot more expertise on the technical end of setting this up to see what we might be able to incorporate.

**Allison Terres:** Perfect. Yeah, and you shared this with me already? Okay, very cool. I'll take a look through this. There might be, it might be good enough here that you don't need to add any additional visualizations.

**Katya Luscomb:** I'll just share it in a call recap, too, so you've got it in Slack.

**Allison Terres:** No, I see it right. Performance report shared yesterday. Looker dashboard. Oh, perfect. Okay, this is really exciting. Yeah, I'll compare my notes, and I can make any comments in Slack and let you know of specific visualizations that we might be able to add as well.

**Katya Luscomb:** Awesome. Some just quick, high-level elements of how this is set up. It pulls from GSC and GA4. So this main view is GA4. GSC data is primarily in this non-branded section. It really just looks at clicks and impressions. For especially in this section with GA4 data, one of the things that we do is separate out sessions, so we've got your site-wide, which is all of these, and then we can also distinguish between different kinds of sessions, so we can filter out, like, some paid media and things as we're looking at Growth X specific content. And then if you want to see just Growth X, then you just unclick that box. And you also break it down by the pillars.

**Allison Terres:** Oh, and you also break it down by the pillars.

**Katya Luscomb:** Yes. And so that's where the visualization is, in cohorts. So this gives probably the most detailed view of the pillars. Again, you're going to want to filter out the non-Growth X URLs because otherwise there's so many pages on your whole site. And then this gives that visualization for each cluster in terms of overall sessions.

**Allison Terres:** Very cool. Love this.

**Katya Luscomb:** Yeah. So there's lots of different functionality you can play around with. If you've got any questions, feel free to let me know.

**Allison Terres:** Okay, cool. And honestly, I might even use it to track overall growth. But I think one thing that is standing out to me is Dell Tech and competitors managing to start beating us via AI rankings. And I'm wondering if that is because their entire website is more optimized for AI rankings rather than what we've been focusing on with you, which is just optimizing the specific organic content. So I do think there's a case for evaluating overall data to figure out whether that is why Dell Tech has managed to get in front of us with AI rankings.

**Katya Luscomb:** Yeah. And one of the other things. So we've got some LLM tracking here. This is really just looking at where LLMs are referring. It doesn't have that competitor breakdown that comes from Scrunch, which is a separate dashboard that, unfortunately, I can't give access to. But on our side, we're actually building an in-house LLM AI visibility tracker. The difference between what we've got is that we're going to be launching it pretty soon, so stay tuned for that. I'll give you more information as we get it. But Scrunch, you have to create your own prompts and kind of guess at what makes the most sense to track across various prompts. And what we've built basically pulls from a library of prompts across different enterprises and clusters that we know are important to track and know are being tracked across industries to give a little bit deeper insight so you're not having to start from scratch. So a lot of the AI insights on that report come specifically from Scrunch. It's an imperfect science at this point. A lot of those platforms are still figuring out the best way to actually measure across those. And the Scrunch data, it's not split up by specific article.

**Allison Terres:** It's really site-wide that it's looking at.

**Katya Luscomb:** Cool. Just figured I'd answer some of those questions in bulk.

**Allison Terres:** Yeah, that's great.

**Katya Luscomb:** Awesome. Other quick things that I wanted to flag looking into some of the questions as far as engagement goes. When it comes to the AI Implementation pillar, I'm definitely going to dig in a little bit more here. What it looks like is that we've got kind of a mix of engagement from high intent and lower intent between top and bottom funnel within that cluster. So we've got some listicles that spiked traffic, but the engagement didn't necessarily follow as that traffic shot way up. Whereas some of your other more high intent pages have lower overall traffic, but higher engagement. And so that's creating kind of a skewed view in that cluster. And then for the CRM pillar in particular, I dug into that a little bit. We only published three pieces in the CRM cluster in November. So the data that we have now for December is really going to be a better baseline. We've got about 15 articles published now, so we can look into that to see if we can get a better gauge on what's really working within that cluster versus not. But just wanted to flag that the November stats are a little bit skewed because it was just based on those three content pieces.

**Allison Terres:** Got it. Okay, good to know. No, I do think as we go forward, like I did share the new pillars with you. But when we decide what the new pillars are that we're going to be tracking, if there's a way to do targeted keyword tracking by pillar, that would be really helpful just to understand, okay, by pillar, what are the keywords that we're targeting with this content? And are we getting there? But I think before I make any huge adjustments, take a look at the pillars that I sent you, see if we want to adjust our main cohorts, and then we can start working towards more specific keyword tracking for those cohorts.

**Katya Luscomb:** Perfect. Yeah, I plan on digging into those this week, early next week, and can have some thoughts over to you regarding any adjustments that we might want to make. I know that we do have keyword tracking. I don't know if it is split by cohort in Looker specifically. I'll dig into that a little bit. We do have the keywords split out by cluster in Airtable. So in the worst case, I can make sure that in my report, the way my report is compiled, that I'm trying to parse that for a little bit more insight too.

**Allison Terres:** Cool. And it's really only going to be super important for the keywords that are really specific to the new pillars that I've outlined. So for billing and invoicing, I think it would be really nice for "billing and invoicing architect software" to be able to track it over time. And a lot of it's because we have so much opportunity. It's really nice to be able to point to wins there. So with just the high intent ones even, it would be helpful to see over time our wins.

**Katya Luscomb:** Perfect. I do like this next step though, of digging into the AI Implementation pillar engagement and doing a deeper dive into high engagement articles, intent messaging, and structure. Yeah, I want to make sure that we're optimizing where we can and really digging into the specific content that is winning as much as the content that's not, so that we can look at the best ways to leverage all that.

**Allison Terres:** Yeah. I do almost think I might star this action item here. I have on Geo right now and AO. And I think my fear is if we don't attack Dell Tech and try to figure out exactly where they're beating us there, then we won't be able to keep up, or they'll just get really ahead of us. And I think that that would be a big story internally if we missed that mark. Let's dig into that and see what needs to happen, whether it's on Growth X content or whether it's suggestions that you have for the main website as well.

**Katya Luscomb:** Perfect. Yeah, we will definitely dig in. I'll probably loop in some AO experts that we have here as well for their insight too.

**Allison Terres:** Okay, I love that. Thank you.

**Katya Luscomb:** Yeah, no worries. Anything else top of mind for you? I know we covered a lot last week and appreciate you hopping in quickly this week as well.

**Allison Terres:** Yeah, no, this is perfect. Actually, I do have one thing top of mind. At the bottom of the performance report, you mentioned wanting to track SDR support metrics and identify which content types drive the warmest inbound leads. So I do actually have an internal Metabase report. This is populated with Google Analytics, and it's technically a segment for SEO. It tracks how many opportunities we are generating from organic content. I think this is last-touch attribution, so if the last touch was a blog and then they requested a demo or got into a demo somehow, that is how this is attributed. So in January, we have already driven nine SQOs. I think the final number for December was 11 SQOs from organic content. We have the firm size breakdown here. It tells us exactly what pages those were that drove the SQOs.

**Katya Luscomb:** But it overall is going to tell you which content is driving opportunities. What's top of mind, this could actually be helpful for me as I am looking at performance reports from our side of all the different elements of clusters and things. If you could export a version of this potentially, like the end of each month and send it over, that would be amazing. And I can do some thinking about the best ways to potentially integrate that into my reporting as well.

**Allison Terres:** Just because this is another layer of the story that we can tell about where we're winning, right? Totally. Yeah, absolutely. I might need a reminder. So like, when you start diving into the performance report, just at me and remind me to send it over your way.

**Katya Luscomb:** And I will just add this export to the checklist right now. And that gives me something to play with and test out the best way that we can integrate that. Let me know if you need access into Metabase.

**Allison Terres:** I don't know how strict we are with that access. I don't think it's too strict. So if you just would prefer to get access in there, I think that we could get it to you.

**Katya Luscomb:** Great. Yeah, I'll let you know about that as well. Because that was actually one of my other questions. Otherwise, any questions, any concerns top of mind for you as we go into 2026? I can't believe January is already halfway over.

**Allison Terres:** No, it's crazy. I think aligning on the new pillars and then really those targets. Because I think we're doing such a good job with top of funnel content and driving traffic, but I do think there's a little bit of misalignment between super high top of funnel stuff and the quality of that traffic. So I think it's like a general effort to try and balance that and say, yes, we still want tons of traffic, but we do want it to be aligned with our ICP in some ways. Not let's drive in students, but let's do it because at some point they will be architects and build trust over time. But I think figuring out that line of, okay, we are working on this, but we're also working on these like high intent software-aligned keywords as well.

**Katya Luscomb:** Yeah, that makes sense. And making sure we've got the balance there so we don't lose one versus the other. There's plenty for me to work with and dig in here. So excited to get started. And I'll keep you posted next week on progress.

**Allison Terres:** Awesome.

**Katya Luscomb:** Thank you so much.

**Allison Terres:** Yeah, no worries. Have a good one.

**Katya Luscomb:** You too. Bye.
