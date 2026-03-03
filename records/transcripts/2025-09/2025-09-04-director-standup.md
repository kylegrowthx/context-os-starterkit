# Director Standup

<metadata>
date: 2025-09-04
time: 19:30 UTC
duration: 35 minutes
organizer: andi@growthx.ai
participants: Andi Bailey, Megan Dickey, Jakub Rudnik, Matthew Panzarino, Jason Gong, Mara Leighton
fathom_recording_id: 85117723
fathom_url: https://fathom.video/calls/399155435
share_url: https://fathom.video/share/wgjVRMtyDs1PpTxR-H6-MiqQMGYghsWD
source: fathom
enriched_on: 2026-03-02 14:30 UTC
speaker_note: "Lake Tahoe" display name in transcript refers to Jason Gong. Mara Leighton is the external participant from GrowthX Labs.
</metadata>

---

## Summary

GrowthX's director team aligned on rigorous tracking methodologies for content refresh experiments across four key initiatives: validating LLM citation impact for Smith (8% branded presence increase over 12 weeks), building Looker dashboards for LLMS.txt authoritative URL tracking at Smith and Monograph, planning TLDR vs. FAQ placement experiments at Monograph (5 articles/week, scaled testing for September), and clarifying Scrunch's prompt tracking methodology to isolate refresh-related content clusters from broader tracking efforts. The team decided to establish a dedicated Slack channel for research and experiments, with ML consultant Katya joining to help design statistically valid tests and identify citation-content correlations.

---

## Context

This is GrowthX's weekly director standup focused on LLM (large language model) visibility and AI experimentation. The meeting brought together delivery leadership (Andi Bailey, Megan Dickey, Jakub Rudnik, Jason Gong, Matthew Panzarino) and external consultant Mara Leighton from GrowthX Labs to review progress on content refresh tracking and plan new experiments. The session reflected GrowthX's shift toward systematic experimentation: rather than treating content refreshes as standalone recommendations, the team is building instrumentation (dashboards, cohorts, prompt tracking) to measure whether specific content changes (publish dates, TLDR sections, topic updates) actually drive LLM citations. This matters because LLM visibility has become a core component of GrowthX's AEO (AI-enabled SEO) delivery methodology.

---

## Relevance

**To GrowthX Delivery:**
- Content refresh experiments need rigorous tracking via Looker cohorts + SEO testing + Scrunch prompt alignment, not just casual recommendations
- Need to document what gets changed in refreshes (publish dates, intro paragraphs, topic alignment) to correlate with LLM citation impact
- LLMS.txt file implementation at Smith, Monograph, and Airbyte requires separate tracking infrastructure (Looker tabs for authoritative URLs + bot traffic analysis)
- Monograph experiment: testing TLDR at top vs. FAQ at bottom of articles (5 articles/week baseline, extra batch for September testing) — requires cohort tracking for citation differences

**To CheckThat:**
- Scrunch prompt tracking methodology unclear — need clarification on whether overlapping prompts are deduplicated or tracked separately, and whether prompt changes actually affect the aggregate citation counts
- Team is building correlation research (with ML consultant Katya) to understand what content properties drive LLM citations — finding that publish date changes alone might influence citations like SEO signals
- Monograph has only 1 article cited by LLMs across 5 weeks of 5 articles/week output — early data but useful for A/B testing once citation velocity increases

**To GrowthX Business Development:**
- Smith: 8% branded presence lift over 12 weeks with refreshes — solid early indicator for reference value
- Airbyte: 4-week refresh impact unclear on branded presence (data timeframe may be too short)
- Tame: new site launch at end of September opens experimental runway; team is very interested in collaboration
- Monograph scaling to September-long publishing blitz with zero content review overhead (Robert's team freed up) — opportunity for aggressive experimentation

---

## Overview

- Implementing more rigorous tracking for content refreshes and their impact on LLM citations
- Exploring LLMS.txt file implementation and tracking for multiple clients
- Planning new experiments around TLDR/FAQ placement and content refresh strategies
- Need to clarify Scrunch's prompt tracking methodology and optimize its use for experiments

---

## Key Topics

### Content Refresh Tracking

  - Implementing Looker dashboards to track LLM citations for refreshed URLs
  - Creating SEO testing cohorts for refreshed content
  - Ensuring Scrunch prompts align with refreshed topics
  - Documenting specific changes made during refreshes (e.g., publish date updates, intro paragraph changes)

### LLMS.txt File Implementation

  - Smith, Monograph, and potentially Airbyte implementing LLMS.txt
  - Creating Looker tabs to track authoritative URLs listed in LLMS.txt
  - Exploring bot traffic tracking for 2-3 clients (requires engineering work)

### New Experiments

  - Homebase: Adding TLDR sections to blog posts
  - Monograph: Testing TLDR at top vs. FAQ at bottom of articles
  - Tame: Potential for various experiments after new site launch (late September)
  - Exploring publish date changes and minimal content updates to test LLM impact

### Scrunch Tracking Optimization

  - Clarifying how Scrunch processes and tracks prompts
  - Investigating potential overlap in prompt tracking
  - Pushing Scrunch to provide more tailored solutions for GrowthX's needs

### Client Updates

  - Smith: 8% increase in branded presence over 12 weeks
  - Airbyte: Refresh impact not yet clear in 4-week timeframe
  - Monograph: Publishing 5 articles/week, planning scaled experiment for September

---

## Action Items

**Mara Leighton (GrowthX Labs)**
- Ask Scrunch about prompt tracking/overlap in tomorrow's call; share findings with team


**Megan Dickey (GrowthX)**
- Create Looker tab for Smith's LLMS.txt authoritative URLs; track LLM citations


**Jason Gong (GrowthX)**
- Ask Jesse re implementing LLMS.txt tracking for WebSax
- Set up TLDR vs FAQ experiment for Monograph articles; publish extra batch


**Jakub Rudnik (GrowthX)**
- Set up tracking (Looker/SEO testing) for Homebase TLDR pages experiment

---

## Transcript

**Megan:** Hey, Jakub.

**Jakub Rudnik:** Hey, Megan. Not too bad. How are you?

**Megan:** Yeah, not too bad.

**Jakub Rudnik:** No dog on your lap today?

**Megan:** Chasing him down the block?

**Jakub Rudnik:** Yeah, just barking. She had groceries delivered and was chasing after the delivery guy.

**Megan:** Hey, Andi.

**Andi Bailey:** Hello. Cool. We've been doing refreshes for Smith, right?

**Megan:** Yeah, it's like all we've been doing. Website page refreshes, not blog post refreshes, but content on the main website.

**Andi Bailey:** We've gone up like 8% in the last 12 weeks in terms of branded presence. That's looking really positive. I wanted to see what other clients were doing straight refreshes on.

**Matthew Panzarino:** Let me put it on here. I'm not doing any refreshes for any mine, so I don't have any input there. Yeah, I'm in the office, Andi. Jason's next to me.

**Andi Bailey:** Well, today's LLM day, our weekly LLM day. I was looking at experiments and I know we don't really have any kicked off, but the thing we've been most active about in terms of LLM visibility is refreshes. That's the most tangible advice we're giving. I wanted to do a spot check on performance in Scrunch for clients where we've been doing refreshes to see if it's moving the needle.

**Jason Gong:** Well, do we update the clusters of prompts we're tracking to match the refreshes we're doing? For example, with Airbyte, over the last four weeks when we started doing refreshes, are we updating the prompts?

**Andi Bailey:** That's a great question. I believe these prompts are targeted at what we were thinking about, but I have not uploaded the new prompts. We started maybe six to eight weeks ago.

**Jason Gong:** Yeah, I just have a curiosity. If we're doing refreshes around these topics, we might want to create a new cluster so we can track. That's what I'm doing with Monograph. When we start a new cluster, I create a new group of keywords in Scrunch to track.

**Andi Bailey:** So one action item for us is in instances where we're doing refreshes to make sure the topics align.

**Jason Gong:** One thing to do might be to create a Looker tab specifically targeted at the URLs we're updating, then look at LLM citations on those URLs. You can pull contemporaneous data and see how it affects over the next weeks after you refresh. You can probably also look at historical data for that URL.

**Andi Bailey:** That's a good idea, because Jakub, for Airbyte, we are doing SEO testing. We're using it for traffic and SEO performance, but we should also be looking at LLM performance in the same categories.

**Jakub Rudnik:** Yeah, agreed. If we were starting from now with a batch of refreshes, I would create that Looker tab, create the SEO testing cohort, and look at those three things together. With refreshes, I'd also want to document what we're changing. Refresh is a broad thing. We'd want to know if it's not having SEO performance, it's having LLM performance. One test I'm trying to build is what if we just change publish dates? Force re-index on some stuff, maybe change the intro paragraph and do nothing else?

**Jason Gong:** That would be amazing if we found a 40% lift or something.

**Jakub Rudnik:** I remember seeing similar moves work in SEO. Subjects get stale, they haven't been crawled in years, and people publish on top of you.

**Andi Bailey:** Should we add this to experiments since we're already doing refreshes? And Mara, we're about to start refreshes on Galileo, right?

**Mara Leighton:** We're already doing refreshes for Galileo. But we can start setting up the specific dashboard or tab you mentioned, Panzer, for Looker, and track the GA4 data specifically. For the Scrunch aspect, I'll look at what we need to do to track reliably, which prompts correlate to the refreshes we're doing, and try to isolate those prompts from the rest of the group. We have a call with Scrunch tomorrow so I can ask for their input.

**Andi Bailey:** Yeah, we should just be a little more rigorous here as we're starting to do this. It's a recommendation that comes up all the time. Having indicators we can point to from clients would be useful.

**Jason Gong:** I added everyone to a new channel, Geo Research. Katya, who's our ML researcher, is going to be in there. Let's use this channel to talk about research projects and experiments. If we're thinking about a refresh experiment, we can jump in and help design it. We're also going to do a Reddit experiment. Because tracking that is tricky—I was talking it out with Robert and I have some theories but we'll see.

**Andi Bailey:** Yeah, I was looking at that too.

**Jason Gong:** Katya does ML stuff at Mercury and has time to help us. We talked to her Tuesday and she's getting up to speed. The two to-dos for her are immediate: if we have an experiment, help us design it so we can isolate what we're measuring, and design some experiments to find correlations between what gets cited and how content is different. The goal is to get started immediately.

**Andi Bailey:** Awesome. And are we tracking LLMS.txt? Who's implementing it yet?

**Jason Gong:** Monograph has it installed. I can find when we installed it and track from there. I don't know how we cohort that data or measure the impact. If you put it in the table or flag it in Slack, I can track it.

**Megan:** Yeah, Joe and I are working with Smith to finesse that document. It should get uploaded to Webflow within the next few days. I'll mark the Notion doc with when it starts.

**Jason Gong:** Are you including a list of authoritative URLs in your format with them?

**Megan:** Yeah, yeah, we are.

**Jason Gong:** Why don't you grab those URLs and create a Looker tab for those URLs? For LLM citations. Name it like LLMS.txtcited or whatever. You can see if there's any impact from it. Obviously there's a baseline of citations you already get, but at least you can cohort from this date forward and see if there's a delta.

**Megan:** Oh, okay, smart.

**Andi Bailey:** Okay, so we're trying it with at least three clients. Noah from Interwell asked about it but they're using Prismic, so godspeed.

**Jason Gong:** On LLMS.txt, I think it'd be nice to have two or three customers where we actually did the work to get bot traffic tracking. That requires engineering work. I think we could probably get it for Airbyte. The people who can tell their engineers what to do are better. It's easier when it's a smaller company that can move quickly.

**Andi Bailey:** So it would probably have to be somebody smaller then.

**Jakub Rudnik:** I met with Tame yesterday about experimentation. They're launching their new site at the end of this month. Once they get past that threshold, we can test basically anything. They have CRO experiments lined up but want to do a lot of testing after the launch. WebSax is probably similar, though getting engineering is tougher. But Jesse has autonomy, just needs resources.

**Andi Bailey:** Jason, ask Jesse since he's there.

**Jason Gong:** Good point. Now you have something to talk about at the happy hour.

**Andi Bailey:** Okay, and the other experiment we should track is Homebase and their TLDR pages. That's their hypothesis, Jakub, right?

**Jakub Rudnik:** Yeah, just adding TLDR to the top of blogs. LLMs only look at chunks of your content, so putting that right up top matters. It's good for users too, they can skim quicker. It's like jump links in a table of contents but summarized.

**Andi Bailey:** Since we're already doing it for them, maybe we could track those pages specifically somewhere.

**Jakub Rudnik:** Yeah, same thing.

**Jason Gong:** Should set up those keywords in Scrunch and then do a cohort. Either Looker or SEO testing, depending on how big this is. We could do a cohort with Monograph too. They'll do anything we tell them. Right now all their articles have an FAQ at the end. But maybe we could do a batch with a TLDR at the top and no FAQ at the bottom. See if there's any difference. The only issue is literally only one of our articles has been cited by LLMs. We've been going five weeks with decent organic traffic and three or four articles cited.

**Andi Bailey:** But really only one that's caught traction with citations.

**Jason Gong:** And so we might be too early to generate useful data.

**Andi Bailey:** But if they're both at zero, it could be interesting to see if some grow more quickly. Might as well start the experiment now.

**Jason Gong:** I guess no variable is a variable, right?

**Jakub Rudnik:** That makes sense. How much are you publishing for them each week?

**Jason Gong:** Five a week right now. I have five weeks worth of content ready, so we can publish them all at once and run a bunch of tests. Robert loves scale and would love to go faster. For September they have nobody to review our content, so he's like publish away. For all of September we can publish basically whatever we want. Maybe I'll do that. I hate to use up our runway because I'll inevitably hit a crisis.

**Jakub Rudnik:** Could it be positioned as putting more resources into doing three weeks of content on one published date, then the next weeks more about tracking?

**Jason Gong:** Yeah, that's definitely what I would do. He's totally fine with whatever we decide. I gave him an extra week for content because his review guy was leaving. So he's fine with us doing that. Just say we're going to publish all this month's content on one day and then track it because we're running experiments.

**Andi Bailey:** I'm sure he'd be totally game.

**Andi Bailey:** Yeah, I think my main thought is we are doing some of this stuff when we're making recommendations. So let's try and track them wherever possible.

**Jason Gong:** Yeah, the main thing missing is are we tracking the prompts? Everyone can just flag that somewhere. Slack is probably the best place. I'll definitely jump on that and try to get Katya's help.

**Andi Bailey:** I think everybody here has admin access to at least their clients. So we should be able to update the prompts to align with the content we're refreshing.

**Jason Gong:** Yeah. As you're picking prompts, don't worry about paying more for them. If you're tracking a thousand prompts, just do it.

**Mara Leighton:** My question for Scrunch tomorrow is something I can't quite wrap my head around. If all these prompts we're pulling together get scrunched down into basic keywords on the backend, aren't they all just being filtered to the same smaller pool? Are we duplicating efforts if they're not each individual?

**Jason Gong:** I know what you mean. You create an additional cluster and you wonder how similar the questions are for this cluster versus the other. They're keyword related but it doesn't work that way. It takes the question you ask and doesn't generate keywords to track. It generates more questions to ask. If you drill down, it's not just keywords. It's a bunch of ways you could say that question or ways you could ask it.

**Mara Leighton:** I think maybe it's a semantics thing. I think it's the search query, the truncated version of the prompt. How much overlap is there if there's too much between prompts?

**Jason Gong:** I've thought about the same thing. How many variations do you have to ask before they all give the same answer? Do I track a million or just ten? It's like decently close.

**Mara Leighton:** And depending on what percentage of prompts cover that basic topic, does that then... I don't know how to quite knit this together.

**Jason Gong:** Yeah, basically the prompts we pick shape whether that chart goes up or not. You can ask different prompts and the chart would be like this or like that. It matters how specific your question is.

**Mara Leighton:** Okay, well, cool. I'll let you guys know what we learn, and if anyone has questions for Scrunch in particular, we only have thirty minutes tomorrow with Andrew. If there are questions valuable to ask live, I'm happy to ask.

**Jason Gong:** Yeah, I think with Scrunch, if you can add me optional, I want to join. We're a huge account for them and I want to push them to do things for us. I'd literally like to show them like hey, we're thinking about refreshing these founder pages. Can you come up with how you'd do this? I want to get them to do things for us.

**Mara Leighton:** Totally. Does anyone use Scrunch's site audit? I'd be curious what you guys think generally of the tool.

**Mara Leighton:** The CSV we downloaded for Scrapy just feels inconsistent with the dashboard. I'll ask them to help me interpret that data and see if it's consistent across other accounts. It's just struggling with figuring out how to present reliable data with all the necessary caveats to clients who are really bullish on Scrunch. But giving them access would be useful.

**Jason Gong:** Stratby is one where I think giving Victor access would be fun. I would not give his team access though. If he wants to share his account that's fine, but we can give Victor access.

**Mara Leighton:** Yeah, we're going to give Victor access and one person on Galileo, just because I'd rather them experience the main point than us be the ones.

**Jason Gong:** Cool. Bye, everyone.

**Mara Leighton:** See you.
