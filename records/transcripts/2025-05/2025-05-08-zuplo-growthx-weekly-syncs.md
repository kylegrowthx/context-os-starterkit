# Zuplo <> GrowthX Weekly Syncs

<metadata>
date: 2025-05-08
time: 18:32 UTC
duration: 34 minutes
organizer: Jenn Peters (GrowthX)
participants: Adrian Machado (Zuplo), Jenn Peters (GrowthX), Carrie Chowske (GrowthX), Dave (GrowthX)
fathom_recording_id: 61594271
fathom_url: https://fathom.video/calls/295204373
share_url: https://fathom.video/share/XsHKSq219-pcy4je61iCftqrdB6YAFxL
source: fathom
enriched_on: 2026-03-03 18:45 UTC
</metadata>

---

## Summary

Zuplo and GrowthX aligned on major content strategy shifts to drive Answer Engine Optimization (AEO) alongside SEO, including increasing transactional content from 30% to 50% and developing a programmatic SEO (PSEO) model for API directory pages. The team also covered indexing fixes (archiving dev.to posts to allow Google to index Zuplo's site directly), a new performance dashboard with LLM traffic filters, and team structure changes where Carrie Chowske takes over account management with Jenn Peters shadowing. CTA optimization emerged as a priority due to underperformance (less than 5 clicks in 30 days), with plans to redesign wording, placement, and customize CTAs by article type.

---

## Context

Zuplo is an API management platform that GrowthX has been delivering content marketing services to as part of a strategic engagement. This weekly sync is a standing sync between the Zuplo product team (Adrian Machado) and GrowthX's account and delivery teams (Jenn Peters, Dave, Carrie Chowske) to track performance, align on content strategy, and troubleshoot technical issues. The team is increasingly focused on AEO as a differentiator — Zuplo's board has flagged that SEO-only visibility is becoming less reliable for conversion due to zero-click searches and LLM traffic patterns, and they've already seen two demos booked from ChatGPT mentions without any Google search involved. The relationship is at an inflection point where they're evaluating whether to expand the engagement or shift to different content models (podcasts, outbound, diverse media).

---

## Relevance

**To GrowthX Delivery:**
- PSEO methodology is being operationalized at Zuplo (data sourcing, structure, content generation at scale) — replicable model for similar clients with repetitive content categories
- AEO is now table stakes for tech/API content; shifting from 30% to 50% transactional queries and evaluating with TouchApt and Scrunch tools
- CTA optimization on technical content is critical — Zuplo's inline CTAs are underperforming (<5 clicks/30 days) and need redesign by article type (tutorial vs. transactional vs. rate limiting)
- Dev.to indexing issues solved by archiving posts and extending syndication delay from 2 weeks to 1 month post-publication

**To CheckThat:**
- Direct AEO signal: Two demos traced back to ChatGPT mentions (not Google SERP clicks) on cost-effective API management queries
- Brand mention strategy is evolving as key AEO lever; Zuplo questioning how to increase mentions across web (PR, outbound, interviews, podcasts)

**To GrowthX Business Development:**
- Contract renewal decision point at end of month — Zuplo evaluating whether to expand the engagement or pivot to custom workstreams (podcasts, outbound content, reverse content from podcast)
- Dave (head of pod) needs visibility into these meetings and strategy decisions for account expansion conversations
- API directory pages (Kelsey, Bitbucket) driving strong traffic; prioritization of top 20 pages for refresh creates content refresh roadmap

---

## Overview

- API directory pages are performing well, with new additions like Kelsey and Bitbucket showing strong traffic
- Team is shifting focus towards Answer Engine Optimization (AEO) alongside SEO, with plans to increase transactional content to 50%
- GrowthX team structure is changing, with Carrie taking over account management in coming weeks
- CTA optimization needed as current inline CTAs are underperforming

---

## Key Topics

### Performance Update

  - API directory pages showing strong performance
  - New additions like Kelsey and Bitbucket quickly gaining traffic
  - Team to prioritize refreshing top 20 API pages

### Content Refresh Project

  - Adrian to send topics for content refresh today
  - Team aims to start generating refreshed content next week
  - Design updates may follow content generation

### Dev.to Indexing

  - Adrian archived dev.to posts for non-indexed Zuplo pages
  - Changed syndication timing from 2 weeks to 1 month post-publication
  - Team to manually request indexing for important pages (10/day limit)

### New Performance Dashboard

  - Dave building new dashboard with LLM filters
  - Will provide insights on LLM traffic sources and performance

### Team Structure Changes

  - Carrie taking over account management in coming weeks
  - Jenn to shadow and support during transition, especially for GitHub processes
  - Dave remains head of pod, team aims to include him in future meetings

### AEO Focus

  - Board feedback suggests increasing importance of AEO
  - Team to shift towards 50% transactional queries in content
  - Adrian to evaluate performance using tools like TouchApt and Scrunch
  - Discussion on potential strategies to increase brand mentions across web

### CTA Optimization

  - Current inline CTAs underperforming (less than 5 clicks in 30 days)
  - Team to consider rewording CTAs, adding more contextual options
  - Potential redesign to make CTAs more visually distinct

### URL Structure

  - Proposal to remove dates from blog URLs for evergreen content
  - Team decides to delay implementation until current indexing issues stabilize

---

## Action Items

**Adrian Machado (Zuplo)**
- Send 2-3 API directory pages to Dave for PSEO calibration
- Review content refresh sheet, send prioritized topics to GrowthX team today
- Manually request indexing for unindexed pages (10/day limit)
- Adjust content strategy to 50% transactional queries starting next week
- Verify CTA click logging accuracy; <5 clicks in 30 days seems low
- Draft CTA redesign ideas including wording, placement, and custom variations by article type (tutorial, transactional, rate limiting)

---


## Transcript

**Adrian Machado:** I think you're muted.

**Jenn Peters:** Never do that. Damn it. How's it going? How are you? I'm doing pretty good.

**Adrian Machado:** Been busy as usual, but I've been catching up on some of the stuff you've asked me to do today.

**Jenn Peters:** I feel like we always have something we're asking each other to do, so that's a good thing. That means we're always busy doing something with the site.

**Adrian Machado:** Always collaborating. Yeah, that's awesome.

**Jenn Peters:** Yeah, same over here on this end. It's always busy and chatting to Dave a lot about the programmatic stuff too.

**Adrian Machado:** Is Dave not able to make these meetings? I thought we moved it so it would be easier for him.

**Jenn Peters:** Yeah, I thought so too, but I wasn't sure if you had settled on a time or not. Generally, he would like to be here for the weeklies. I know he has another call at the same time.

**Adrian Machado:** 11:30 is always fine. I can sometimes do 10:30 Pacific every other week. So like this week I can't, but next week we can. I'm also okay moving it to Wednesday or Friday if that's easier.

**Jenn Peters:** I definitely prefer if he's here just to get questions answered. And with Carrie being here as well, she's going to be taking over this account in the coming weeks.

**Adrian Machado:** Okay, great.

**Jenn Peters:** I couldn't get my sound to work at first. Anyway, we have lots to cover today with all our various projects going on, so we can just jump into stuff.

**Jenn Peters:** I won't spend too much time on performance, but all in all, things are looking really nice. API directory pages are killing it on the site overall. This past week we've had some new performance with Kelsey and Bitbucket. They're great. It's pretty much that if we put a new one up there, it's going to be earning traffic and impressions for us.

**Jenn Peters:** With that in mind, I think as we go through and look at refreshes, we definitely want to look at those top 20 API pages as priority.

**Adrian Machado:** Yeah, I went through the Google Sheet you sent me. I left a few comments on some of them. Generally it's all good. I think the ones we're prioritizing make sense. A lot of them probably need updating every few months just because APIs change and there are new features. If we want to stay relevant and competitive, we need to keep up with that.

**Jenn Peters:** I think putting them on a rotating cadence based on performance and how old they are is a good idea. As soon as other sites start seeing we're doing well with these, they're going to want to copy.

**Adrian Machado:** That's kind of why we're aiming for the PSEO model with Dave. Once we crack the formula for what content on these pages does well, we can break that up into different sections, structure them on the page, add in more content and start generating these at scale. That's the efficiency we're going for.

**Jenn Peters:** If we know which sections are the ones we'll want to be refreshing, we can just go in and update those more easily.

**Adrian Machado:** Dave is reviewing the proposal I put together. I think he wants you to pick a couple of them for calibration — just to see your preferences on which ones to look at first, to make sure they look okay and the flow is functioning as we want.

**Jenn Peters:** Yeah, that makes sense. There are all the data sources we discussed, and we have to structure them and make them relevant. It'll probably take a few iterations.

**Adrian Machado:** That's perfect. I'll send some over in this meeting.

**Jenn Peters:** That's going to be really exciting to see that scale out. So we already kind of talked about the content refresh project. We were thinking we'd start next week, but it's up to you.

**Adrian Machado:** Yeah, I'll send over the topics today. If we can start generating them, you can send me examples next week. There'll be some lead time for designing the page, but I don't think that'll take long. It's better to get the content out and then optimize the page later than not have it in the first place.

**Jenn Peters:** One thing I wanted to make sure I was totally updated on was your dev.to indexing situation. My impression from Dave was that you took some of those pages down so Google will index them from Zuplo's site.

**Adrian Machado:** Yeah, for pages we've seen that haven't been indexed yet, I took some and searched them up. I saw the dev.to version was indexed, so I took down those dev.to posts. I just archived them—they're not gone forever, but they're not public anymore. There's no way to set up a redirect. Eventually those pages will get recrawled.

**Adrian Machado:** This was most relevant for pages before the 22nd, because after that I changed how we do syndication. I automated it to syndicate content older than two weeks, but I've changed it to one month instead. That's more reasonable and should help a lot.

**Jenn Peters:** A post should be indexed within a month. Otherwise we have bigger problems.

**Adrian Machado:** Yeah, I really hope so.

**Jenn Peters:** Should we just sit tight and see if Google notices, or do you think we should manually request indexing?

**Adrian Machado:** If we have the request budget, we should do it. It's 10 per day.

**Jenn Peters:** I don't see why not do it, just because they've been sitting around a while. Some of them are API pieces, so they'll do well in traffic. Basically, any time you mark a post as published, Deya tags stuff because we're already uploading to Looker. I get all those URLs, put them in a CSV, and manually go through to see what's indexing. It's a pain because it's only 10 per day, but it's better than nothing.

**Adrian Machado:** Yeah, exactly. Might as well get them indexed. I also went through the top 10 most viewed pages on dev.to and looked if they were getting Google traffic. Some of them were still getting Google traffic, so I archived those as well. It'll take some time to see what happens. Sometimes Google might just prefer the dev.to version.

**Jenn Peters:** Yeah, we should see a huge boost in traffic, because it's quite a few pages.

**Adrian Machado:** So I think this should be fixed going forward.

**Jenn Peters:** Yeah, okay, moving to the new dashboard. Dave is building a new performance tracking dashboard with LLM filters built in. I've already seen a trial demo for another account. It's really good — it's like the regular performance dashboard with filters by weekly and keyword, but then there's a separate filter for LLM.

**Adrian Machado:** Oh, perfect. Yeah, looks really cool.

**Jenn Peters:** It'll take him some time to do it for all the accounts. There are different ways of tracking LLM traffic — sometimes there's a UTM from ChatGPT, but others use the referrer, for example.

**Adrian Machado:** I'm interested to see what he comes up with. I've built this on my own side too, so it'd be good to compare what your data looks like.

**Jenn Peters:** Yeah, so that'll be good to see. I'm not sure exactly when, but he's already doing it for other accounts. So with our team growing, one thing to note is that Carrie is going to be taking over this account in the coming weeks. But I'm still here, and so is Dave. We're just doing some shuffling around. I'll be here supporting Carrie on the Zuplo stuff, especially when it comes to GitHub staging. I'd like to be present for shadowing on GitHub so I'm doing checks before they get passed to you. We've done full walkthroughs, but Carrie needs hands-on experience to actually stage stuff herself.

**Adrian Machado:** Okay.

**Jenn Peters:** Dave is still the head of the pod, and I'd like to make sure he can get into these meetings as well. So moving on to AEO focus. We had a board meeting recently, and they're seeing that answer engine optimization is going to be a big part of growth funnels going forward. The board and our CEO are a little concerned about the future of SEO as a conversion lever based on the metrics we're seeing. Impressions might be growing, but the bar to getting a click is higher now. There are a lot more zero-click searches taking place. We think the way to address this is twofold. On the SEO side, since a lot of AI reviews apply to informational queries, we should double down more on transactional queries. They've been pretty good so far at actually answering questions and getting Zuplo mentioned into the flow.

**Adrian Machado:** I asked for 30% transactional, but I think we can move to 50% starting next week, then continue up from there depending on performance. I'll evaluate this using tools like TouchApt and Scrunch. We've also had two demos in the last couple of weeks where people mentioned they asked ChatGPT about this thing and you guys were mentioned. That's the whole reason we're talking to you. That's a very direct conversion funnel.

**Jenn Peters:** Did they say which LLM?

**Adrian Machado:** I need to ask them. I think it was ChatGPT. They were looking for something like low-cost API management. That's very straightforward and direct. If you Google that same thing, there are so many articles from companies far more established than us, but the fact that they're getting mentioned is very good.

**Jenn Peters:** Yeah, and it's not necessarily an on-page mention. It's a cross-the-web-mention type situation. The thing is, I don't think it's just one thing. There's many things we need to think about in terms of outbound and strategy — what other types of media can we look at? Interviews and podcasts, for example.

**Adrian Machado:** The main reason I bring this up is because probably at the end of this month is when we need to start thinking about what our relationship with GrowthX is going to look like. Are we going to expand the relationship? Are we going to do a different type of content? I just want to know how you guys are thinking about AEO and if those offerings are going to evolve or change based on the new landscape.

**Jenn Peters:** Yeah, it's like a daily topic across the accounts. That's the whole reason it's getting built into our dashboards. From what I'm seeing, there are definitely accounts that have custom-built workstreams different than just editorial, content optimization, and backlinking. Some clients are doing podcasts and we're building content for their podcasts. There's the reverse too — podcasts where they want editorial based off of that. It's custom, I guess is what I would say.

**Adrian Machado:** I just want to understand how things are changing over time so we can evaluate. I need to come up with a plan probably at the end of this month. What are we going to do about AEO?

**Jenn Peters:** Yeah, and another reason it'd be great to have Dave in this conversation is because he has more direct touch with the team. If we could synthesize what your big asks are, what would an ideal workstream look like for you going forward, and how could we adjust it based on evolving changes like AEO? What can we do for you?

**Adrian Machado:** Okay, we'll think about it a little bit more for next week. Moving on to CTA optimization. I was looking at the numbers for our inline CTA. It only has gotten maybe less than five clicks in the last 30 days. So I'm clearly not doing something great with CTA here. It looks nice though.

**Jenn Peters:** Yeah, I think it's the wording. "Learn more" is not my favorite.

**Adrian Machado:** We're working on redesigning our website right now. You might see some changes. I'll probably change some of the CTAs. I might add a second inline CTA somewhere — maybe one in the top third and one in the lower two-thirds.

**Jenn Peters:** Another option we talked about is having two or three CTAs that we rotate based on what fits better for the article. If it's a rate-limiting article versus a tutorial versus a transactional piece, they'd all have different CTAs.

**Carrie Chowske:** Just from an outsider perspective, it took me a while to realize it was meant to be a mid-page CTA. The Twitter/X format is one that jumps out to me. It looks more like it's meant to be in line with the rest of the article.

**Adrian Machado:** The way I got this idea is from LogRocket, which is a very well-known tech company that does a lot of SEO, especially for front-end development. I kind of stole their strategy. Why not?

**Jenn Peters:** I was going to say, with the differentiation between end-of-text "try free today" and "book a demo," that's something we want to look at. Which pieces are more demo-focused where the reader would relate more to booking a demo versus just defaulting to "try it today for free"? Demo might be more appropriate for higher-level topics.

**Adrian Machado:** Okay, one more thing — Jimmy suggested we remove dates from our blog URLs before he left. Do you guys think we should still do that?

**Jenn Peters:** When you update an article, it's going to have that old URL, right?

**Adrian Machado:** Actually, we changed the URL structure of our blogs entirely. Our blog URLs are zuplo.com/blog/year/month/day/slug. His suggestion was to remove the year/month/day and just have /blog/slug instead.

**Jenn Peters:** That's definitely my feeling. I think it's an evergreen differentiator.

**Adrian Machado:** So I could do permanent redirects from the old links, but I'm worried if we keep using the old URL in articles, will Google ignore the canonical?

**Jenn Peters:** My only thing with redirects is speed. As long as speed is okay, it should be fine. I have another account where they had to do a ton of redirects for site mapping. With all the other indexing changes happening right now, it might be something to wait for to see stabilization. If we're changing that as well right now, we don't have a baseline to gauge if the dev.to project is fixing things or not.

**Adrian Machado:** So the sitemap would completely change. Would that affect indexing? Because we already have a bunch that are uncrawled and some crawled but not indexed.

**Jenn Peters:** No, it's just a matter of resubmitting. But we're doing so much other stuff with indexing right now. It's harder to track if our dev.to project is working if we're messing with everything at the same time.

**Adrian Machado:** Yeah, I'm with you on that. So I think I'll wait until maybe next month.

**Jenn Peters:** Yeah, let's try to get some stabilization with indexing first. Let's get the actual pages indexed and see if we can start seeing traffic results. Once there's stability, then we can fix this down the line. In general, I'm not a fan of dates in URLs anyway.

**Adrian Machado:** Okay, cool. Yeah, sorry for running over. I hope you didn't have another meeting.

**Jenn Peters:** No, no, I'm good. Okay, awesome. Yeah, lots of stuff to cover. Thanks for your time. I'm going to sync with Dave after this and pass this all on. I'll put you two in touch to work out a time for rescheduling that works for all of us.

**Adrian Machado:** Okay, perfect. I'll catch you later, Jenn. Talk to you soon.
