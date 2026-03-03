# Engine Weekly Sync

<metadata>
date: 2025-08-07
time: 18:30 UTC
duration: 28 minutes
organizer: darrell@growthx.ai
participants: Carrie Chowske, Darrell Etherington, Joel Murphy, James Winter
fathom_recording_id: 79225804
fathom_url: https://fathom.video/calls/373390833
share_url: https://fathom.video/share/s7e7uwt6TVK1UakfHmGDA5es_DmbzRkd
source: fathom
enriched_on: 2025-08-07 20:15 UTC
</metadata>

---

## Summary

Hotel Engine's content team confirmed strong production momentum: 16 approved topics ready to publish and 18 in production gives them a 6-week buffer at their target pace of 5 articles per week. The team handoff content review from James to Joel, with Carrie managing publishing cadence, while Joel builds Amplitude dashboards to track blog performance and attribute conversions to GrowthX-created content. Hotel Engine's new sentiment analysis tool trained on customer call language presents a valuable opportunity to refine content prompts and improve pre-editing output quality.

---

## Context

Hotel Engine is a travel platform operating in the business and leisure travel space. GrowthX is executing a content marketing strategy for Hotel Engine's blog, focused on the business travel vertical with planned coverage of topics like credit cards, discounts, rewards, and general travel considerations. This is the weekly operational sync where Carrie Chowske (GrowthX COO) provides production updates, Joel Murphy (Hotel Engine) updates analytics and tracking, and James Winter (Hotel Engine) provides feedback on content quality and direction. The team has moved through the initial ramp phase and is now in steady-state production, managing review workflows, analytics attribution, and content categorization as the volume of published pieces grows.

---

## Relevance

**To GrowthX Delivery:**
- Workflow refinement opportunity: Joel's sentiment analyzer tool trained on Hotel Engine customer call transcripts could be applied to refine content prompts and improve pre-edit output quality before human review.
- Content performance: Google Search Console shows GrowthX-created business travel content generating increased clicks and impressions over the past 4 weeks, indicating strong visibility gains despite AI overviews stealing traffic from competitors.
- Review process optimization: Transition from James to Joel as content reviewer requires clear SLAs and regular publishing cadence (targeting 5 per week average with flexibility).

**To GrowthX Business Development:**
- Account health signal: Client is confidently increasing publishing velocity (6 weeks of content buffer) and investing in analytics infrastructure (Amplitude dashboards), suggesting strong engagement and confidence in the engagement.
- Expansion potential: Hotel Engine's custom sentiment tool and customer language data are valuable assets that could support content refinement at scale or inform other verticals.
- Renewal indicators: Strong content production momentum, established workflows, and cross-team collaboration suggest healthy account trajectory.

**To CheckThat:**
- Relevance: Hotel Engine's use of customer sentiment analysis to guide content creation demonstrates real-world application of tonality and sentiment analysis in B2B content strategy.

---

## Overview

- Content production is on track with 16 approved topics and 18 in production
- Joel will be the new point person for content review, replacing James
- Analytics discussion focused on conversion tracking and isolating GrowthX-created content
- Hotel Engine's custom sentiment analysis tool could provide valuable insights for content creation

---

## Key Topics

### Content Production Progress

  - 16 approved topics ready for publication
  - 18 topics in production
  - Over 30 articles available, providing 6 weeks of content buffer
  - 12 articles ready for Joel's review
  - Publishing goal: average of 5 articles per week

### Analytics and Tracking

  - Joel working on Amplitude dashboard for blog performance
  - Key metrics: blog visits, sign-up clicks, form submissions
  - Discussing appropriate conversion funnel timeframe (1 day vs. 7 days)
  - Exploring ways to isolate GrowthX-created content for accurate tracking
  - Considering unique CTA links for GrowthX content to track conversions

### Custom Sentiment Analysis Tool

  - Hotel Engine developed a tonality and sentiment analyzer
  - Tool trained on customer language from call transcripts
  - Potential to use for refining content prompts and improving pre-edit output
  - James offered to run queries through the tool to provide insights

### Content Categorization and LLMs.txt

  - Wedding-based content deprioritized until proper categorization is determined
  - Dave (GrowthX) working on LLMs.txt implementation using top 25-30 traffic posts

### Review Process and Publishing Cadence

  - Joel to set a regular day for content review
  - Carrie will manage the publishing schedule and remind Joel as needed
  - Flexibility in publishing schedule (e.g., 5 per week on average, but can vary)

---

## Action Items

**Joel Murphy (Hotel Engine)**
- Review 12 articles ready for approval in Airtable

- Finalize Amplitude charts/dashboard tracking blog URL visits, sign-up clicks, form submissions, and conversion impact analysis (with both 1-day and 7-day conversion windows)

- Implement unique query parameter on CTAs for tracking GrowthX content conversions separately from other blog content

- Determine categorization method for wedding-based content before republishing


**Carrie Chowske (GrowthX)**
- Grant Joel access to Airtable for content approvals and reviews


**James Winter (Hotel Engine)**
- Share custom GPT prompt based on Hotel Engine customer language with Darrell for use in GrowthX content creation pipelines

---

## Transcript

[Opening chat about ChatGPT 5, tool integration, and AI hallucinations — 5 minutes of off-agenda discussion]

**Darrell Etherington:** Hi, Joel.

**Joel Murphy:** Hey, Darrell.

**Darrell Etherington:** How are you doing?

**Joel Murphy:** I'm not too bad today.

**Darrell Etherington:** We were just talking about our internal tooling and then also a little bit about ChatGPT 5, which just came out, but I haven't had a chance to use that.

**Joel Murphy:** Yeah, it sounds great, but is it great? ChatGPT is particularly bad at documentation updates. Like, with Amplitude — I ask it how to do something and it hallucinates. It drives me crazy. It'll say click this, but those things aren't there anymore. I'm just like, just say when you don't know.

**Darrell Etherington:** Yeah, and it's like, "Oh, you're absolutely right, I'm making this up, here's the real way." And then you're still making stuff up.

[Carrie joins and shares a tangent about AI psychosis and how LLMs affirm user suggestions rather than thinking independently — 10 minutes]

**Carrie Chowske:** It's fascinating because it reminds me of how ChatGPT just agrees with you. You can give it guidelines, but if you suggest changing something, it's like "Oh, you're absolutely right" every time.

**Darrell Etherington:** I tend to anthropomorphize all the technology and talk to it politely, just in case the robot revolt happens.

**Carrie Chowske:** I figure politeness is good insurance.

[Discussion winds down; Darrell apologizes for going off-agenda]

**Darrell Etherington:** Sorry, James, I'm cutting us off here.

**James Winter:** All good.

**Darrell Etherington:** Carrie, you want to kick us off on the actual agenda?

**Carrie Chowske:** I was having fun with that, but yes, let me share my screen.

**Carrie Chowske:** Okay, so we're really chugging along. We've got 16 approved topics ready to go and 18 in production. That's over 30 articles, which gives us six weeks of content buffer — plenty of padding. We're planning to publish five per week on average, so even if reviews batch up, we have refreshes we can use. Right now, there are 12 articles ready for your review in whatever order makes sense.

**James Winter:** Joel's going to be your point person going forward with these.

**Carrie Chowske:** Got it, Joel, you're now on this. I'll share the Airtable approval matrix link. You might need access to our Airtable.

**Joel Murphy:** I'll check if I already have it.

**Carrie Chowske:** Let me know if not. I think I have the settings configured so you can approve directly.

**Carrie Chowske:** I reviewed the Graphite recommendations you shared. I added their optimization suggestions to our list, removed duplicates, and filtered out ones we'd already reviewed. It's a manageable task now — not nearly as big as it looked at first. I also went through the delete and redirect lists with the same approach. Once we get Amplitude access, we'll shift focus to conversions and make sure we have the performance signals you need.

**Joel Murphy:** I don't think I can give you guys direct access to Amplitude. What I've built instead are shared dashboards we can collaborate on. So far I have metrics for blog visits, sign-up clicks, and form submissions. I'm also working on an impact analysis — basically, what's the connection between viewing a blog post and a form submission, and how long does that take? I want to show both metrics to give us a fuller picture, both near-term (1 day) and longer-term (7 days) conversion windows.

**Darrell Etherington:** That makes sense to start. Do both time windows — I don't want to guess at the right window size without more buyer data.

**Carrie Chowske:** Anything that shows whether they interacted with our content at all is a win. It doesn't matter where in the funnel they land — if they find it useful and book, we're doing something right. Real humans using it is the signal.

**Joel Murphy:** Right, so the next step is journey analysis — when they view a blog post, what do they do next? How long until they book?

**Joel Murphy:** One more thing on analytics: can we identify and isolate just the content you guys created from the rest of the blog?

**Carrie Chowske:** We could use date range — publish dates since early July. Or better: if we put a unique query parameter on GrowthX CTAs, we can track those conversions directly. My click and impression data is already filtered that way from the last month-plus since we started publishing.

**Darrell Etherington:** We're already doing regex-based filtering on some dashboards. Query parameter on the CTA is probably easiest for Amplitude.

**Joel Murphy:** Yeah, I'll use a custom query param instead of UTM, so it doesn't override original visit source.

**Carrie Chowske:** Our full dashboard pulls from Airtable to show cohort-based performance — just the content we've created compared to Google Search Console data. The business travel subfolder content is seeing more clicks and impressions than historical. It's a big win considering AI overviews are stealing traffic from other clients. We're early in the project, but moving fast.

**Joel Murphy:** The chart's up and to the right regardless of time window.

**Darrell Etherington:** I shared a document with you of all our keyword queries from Scrunch so you can cross-reference with your data. Dave also pinged me separately about the LLMs.txt project — he needs your top 25-30 traffic posts for the year to build the skeleton. He's already actioning it, so that should move fast. We're also looking at building our own lightweight version of Peak because the current tool isn't quite fitting our needs.

**Joel Murphy:** One more thing — we have a new tool on our team. James, what would you call Rory's sentiment analyzer?

**James Winter:** It's a tonality and sentiment analyzer. We did categorization, chunking, and sentiment analysis on all our customer calls. It's basically a chatbot trained on the exact language our customers use.

**Darrell Etherington:** So you could ask it how customers express concern about a specific topic, for example.

**Joel Murphy:** We could run your content prompts through that to see how well they align with customer language.

**James Winter:** I can't expose the tool directly because of PII concerns, but I can run queries and send you results. I also created a custom GPT prompt that speaks in customer language.

**Darrell Etherington:** Perfect. Ship me that GPT prompt — I'm going to use it as an artifact in our content pipelines to see if it improves pre-edit output.

**Carrie Chowske:** That's great. This reminds me of when sentiment analysis first came to social media tracking with Hootsuite — it completely changed what was possible with tracking and optimization.

**Carrie Chowske:** One more thing: wedding-based content is still in production but I'm deprioritizing it until we determine the right categorization so we're not publishing it under business travel. We also have traffic data showing that credit cards, discounts, and rewards are big query drivers on your site — good future topic opportunity. And on the publishing cadence: we're aiming for an average of 5 per week, but we have flexibility. We have enough buffer that if you're backlogged one week, we can shift content around. Just set a day and let me know your target, and I'll work around that. I'll ping you regularly when we need articles published.

**Joel Murphy:** Got it. I'll make sure I'm not the blocker. Let's set a consistent day.

**Carrie Chowske:** Sounds good. Anything else?

**Joel Murphy:** I think that's everything for me. James?

**James Winter:** Nope, all good.

**Darrell Etherington:** Great. Thanks all.
