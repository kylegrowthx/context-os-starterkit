# Zuplo <> GrowthX Weekly Syncs

<metadata>
date: 2025-03-06
time: 19:32 UTC
duration: 32 minutes
organizer: Kyle Gaudreau
participants: Jenn Peters, Adrian Machado, Deya Bhattacharya, Kyle Gaudreau
fathom_recording_id: 50624388
fathom_url: https://fathom.video/calls/248060826
share_url: https://fathom.video/share/szEzDmsf8HPY8L3rnjgRRM5_UpDLXDPS
source: fathom
enriched_on: 2025-03-04 19:45 UTC
</metadata>

---

## Summary

GrowthX and Zuplo discussed content strategy progress, hiring challenges with fraudulent candidates, and plans for an API directory that would drive brand visibility and owned audience growth. The team reviewed indexing performance of recently published content, confirmed a 43% week-over-week increase in LLM engine traffic (106 visits from Gemini, Perplexity, and ChatGPT), and planned to spread content publication throughout the week to improve Google's indexing pipeline. Adrian will develop a dedicated API index/directory section modeled on RapidAPI's approach, with Kyle and Jenn supporting through content structure and performance tracking via Looker Studio.

---

## Context

This is a weekly sync between GrowthX's content and SEO team (led by Jenn Peters) and Zuplo, an API management platform, where Adrian Machado is the product lead. Zuplo is a client of GrowthX's content marketing services. The relationship focuses on content strategy for Zuplo's blog and technical documentation to drive organic traffic, lead generation through owned audience growth, and product visibility. This meeting occurred as Zuplo was in the early stages of a content publishing initiative (12 articles scheduled across blog and API categories) and evaluating infrastructure improvements like transitioning from manual publishing to automated workflows.

---

## Relevance

**To GrowthX Delivery:**
- Publishing strategy refinement: spreading content across the week improves Google's indexing pipeline performance vs. batch publishing.
- Programmatic content production requires different workflow templates and quality assurance approaches than manual blog posts; GitHub Copilot code review may be sufficient for automated pages.
- Infrastructure scaling: transitioning from manual uploads (bottleneck at 1 person) to automated publishing and VA delegation improves content velocity.

**To CheckThat:**
- LLM traffic monitoring is now critical to content strategy success. 106 visits from Gemini, Perplexity, and ChatGPT (up 43% week-over-week) shows early AEO impact without ranking #1.
- Brand mentions and content quality matter more for LLM visibility than traditional SEO ranking position; Reddit posting is now a distribution channel to maximize LLM crawl.

**To GrowthX Business Development:**
- Zuplo account shows healthy engagement and content partnership maturity: asking for performance dashboards (Looker Studio), wanting to differentiate traffic sources, planning 2-3 week planning sessions for structural content strategy.
- Potential expansion: API directory project could evolve into a content platform generating leads through owned audience (newsletter) and open-source product funnel (API scoring, documentation features).

---

## Overview

- Zuplo and Zuplo's partners are experiencing hiring fraud: scammers creating fake LinkedIn profiles and using AI face filters to appear as different people in interviews, targeting multiple jobs simultaneously.
- Plans to develop a structured API directory/index to improve site authority and user experience, modeled on RapidAPI's approach, moving beyond basic blog content.
- Content performance tracking will be enhanced using Looker Studio with GSC data filtering and LLM traffic monitoring (Gemini, Perplexity, ChatGPT).
- Spreading out content publication throughout the week may improve indexing rates compared to batch publishing, reducing Google's indexing queue bottlenecks.
- LLM traffic is now a major channel: 106 visits in L7 from AI search engines (up 43% from previous week), driven by brand mentions and content quality rather than ranking position alone.

---

## Key Topics

### Hiring Challenges

  - Remote companies facing issues with fake candidates using AI filters during interviews
  - Scammers target remote positions, attempting to secure multiple jobs simultaneously
  - Similar issues observed in content mill spaces with writers outsourcing work

### API Directory Development

  - Plans to create a dedicated API index or directory section on the website
  - Goal to emulate successful examples like RapidAPI's directory
  - Focus on structuring content around use cases and problem-solving rather than just API definitions
  - Potential to include API scoring and documentation features to drive engagement

### Content Strategy and Performance

  - Current content batch showing good performance, with some indexing delays
  - Spreading content publication throughout the week may improve indexing rates
  - Exploring ways to differentiate traffic driven by different content types (e.g., programmatic vs. manual)
  - Implementing Looker Studio for more comprehensive performance tracking

### LLM and Alternative Search Engine Traffic

  - Observed 106 visits from Gemini, Perplexity, and ChatGPT last week (43% increase)
  - LLM traffic becoming increasingly important to monitor
  - Quality content and brand mentions may be more critical for LLM visibility than traditional SEO metrics

### Content Distribution and Visibility

  - Posting quality content on Reddit to increase visibility, as LLMs are likely scraping from these sources
  - Discussion on the growing importance of Reddit for SEO and content distribution

---

## Action Items

**Kyle Gaudreau (GrowthX)**
- Connect with Jenn re: Looker Studio for Zuplo content performance reporting — set up GSC data filtering and dashboard for individual article tracking

**Adrian Machado (Zuplo)**
- Analyze traffic from AI search engines (Gemini, Perplexity, ChatGPT); prep report for Zuplo investors
- Plan dedicated session (2-3 weeks out) to design API index/directory structure with Jenn and Kyle, including wireframes and interlinking strategy

---

## Transcript

**Jenn Peters:** previous meaning about onboarding and hiring, and Kyle also doing the same. And how much time that actually takes on the front end of like, yeah, it's great to get all these people to help you do stuff, but you have to tell them how to do stuff.

**Adrian Machado:** With hiring, one thing that we've run into a couple of times is fake candidates. They'll create fake LinkedIn profiles. One of the startups we work with closely even had someone wearing an AI face filter to change their appearance on the hiring call. The way they test it is, hey, put your hand in front of your face, and the filter breaks. Yeah, they built a profile on LinkedIn and used the image to filter their face in the meeting.

**Deya Bhattacharya:** Was it genuinely a job seeker or who was it?

**Adrian Machado:** So typically what we've seen, these people are sitting on the ground with a wall background, and you can see other people doing interviews in the background. Their plan is to get as many jobs as possible in parallel among their group, trying to get as much money as possible before they get fired. They typically target companies like us because we hire remote.

**Jenn Peters:** So they'll even fake their location details.

**Adrian Machado:** Like, you say you were born in Detroit, Michigan, but you have an Indian accent? I don't know how that's possible.

**Deya Bhattacharya:** I've been to Detroit, I know what they sound like.

**Adrian Machado:** It's very distinct for sure.

**Jenn Peters:** I've seen that in the content mill space. I'd hire people for content, and at first it went great. They'd produce a couple pieces, then I'd get something with a wildly different tone of voice or style that raised red flags. The more I dug into it, I realized I was talking to like 20 people. I found out when I went into a Google Doc and saw other people's names.

**Deya Bhattacharya:** If you want to run a scam, do it convincingly. Like, I'm in the doc seeing some other random person I never gave access to.

**Jenn Peters:** I reached out to the person I thought I was dealing with, and they said, "Oh, that's just somebody else's computer. My computer isn't working or whatever."

**Adrian Machado:** They don't necessarily cover their tracks the same way as Nigerian Prince scams, which are designed to filter for people dumb enough to fall for them. It's a prioritization exercise.

**Jenn Peters:** If they do it a hundred times, every 10 failures maybe gets one bite.

**Adrian Machado:** I mean, I'm from India and I've been in the content space a long time. Those people are giving genuine writers a bad name. That's why writers from third world countries can't get the same rates as someone located in the first world. At least we know everyone on this team is real.

**Jenn Peters:** We're all a real team. Kyle's helping with best practices and filtering for face filters now. That's a real thing.

**Kyle Gaudreau:** We have some things in our automated recruiting process that help us filter this out.

**Jenn Peters:** So we have 12 articles scheduled to go up between today and tomorrow—10 standard ones and 2 APIs. I'm finishing the API pieces today. There was a workflow issue yesterday, but that's fixed now. I took the existing ESP homepage and top performing ones, fed them into a model to build out a template, then used that template in the workflow to get them as close to programmatic and standardized as we can. Same headers, code samples, structure and stuff.

**Adrian Machado:** I'll probably review those to make sure they're good. I've been driving a lot of TOFU traffic with the ESPN one. I want to make this more programmatic going forward with dedicated pages for these APIs rather than just blog posts. I want to have a section on our website called an API directory or index.

**Jenn Peters:** I was thinking about that in the same way. Possibly building it out as a different section outside the blog base. I looked at Kong's structure—they have a blog and separate resources section. I did a deep dive on what queries drive to certain pages. Looking at API pages, "What is an API" is a top trending topic. It's a super hard keyword to rank for, but it got me thinking about these programmatic definition and FAQ repository pages. APIs for Dummies is actually a top topic.

**Kyle Gaudreau:** A lot of those already exist in your blog section. Pulling them out to top-level resource pages like Kong has could differentiate for readers and also help with interlinking and tracking.

**Adrian Machado:** I wonder if Kong has success because they already have high domain authority and page authority. Salesforce ranks above Amazon for "what is an API," but the page isn't that great. Obviously ranking ahead of Amazon isn't easy, but in terms of quality and authority building, we could do better.

**Jenn Peters:** Yeah, the domain authority is like 99. The challenge is competing with that, but creating this page makes sense. Ideally, we get into the top 10 over time. Maybe we look for lower-opportunity keywords first that aren't as difficult. I dumped a bunch of API search terms in there from the past month. Some you might have, some aren't useful because they're short-term topics. But I'm thinking about where these pages should live structurally and from a sitemap perspective.

**Kyle Gaudreau:** At a certain point, we should explore the right depth of content for good user experience. We can't just default to blog posts. Most websites go with solution pages, product pages, use case pages, or blogs. The key is being mindful of personas, what they care about, what's behind the search, and creating something scalable that fits into them. That's the secret sauce of good programmatic work. We wireframe things up to kick off the conversation.

**Adrian Machado:** That'd be good to chat about in 2 or 3 weeks. I want a dedicated session to design the API index or directory using programmatic SEO. I definitely have lots of ideas. I want to make sure we're doing interlinking and structuring properly. That's in-depth work. I talked to Greg Dax and Marcel because I wanted to recreate RapidAPI's directory. That's a canonical example of programmatic SEO. We have the content to prove there's demand in these queries. Now it's whether we can scale it and whether it drives real business results.

**Kyle Gaudreau:** When I was leading growth at Trey, I spent time on this. They did it a little bit, but priorities changed. API-based content has become quite saturated. We need to consider a unique angle and experiment. The approach is to make API pages pillars with use-case clusters underneath. If pure head terms are hard to rank for, we find traction through use cases and eventually lift those broader API rankings. That adds complexity for programmatic, but there are possibilities.

**Adrian Machado:** What does it enable? That's the angle. In terms of ultimate goals, given the TOFU nature, we probably don't seek direct leads. First, we want owned audience—getting them into a newsletter. Second, upsell of our open-source solutions to get them into our ecosystem. We'd discuss an API, then feature our API scoring product or documentation feature. They input their API, see the analysis, and become an open-source qualified lead. It's a flywheel versus direct conversion.

**Kyle Gaudreau:** When I was at Trev, I was excited about this. It was hard to execute at scale. Customers would say, "This API is a nightmare to deal with." If we create a directory scraping technical details together, there are layers. You leverage different sources to inform content. The structure could show the path to documentation and the essential things you need to know to work with an API—authentication, key calls, that kind of thing.

**Adrian Machado:** Yeah, I think that's all very good. We should park this and have a longer discussion.

**Kyle Gaudreau:** This is pretty cool stuff.

**Jenn Peters:** I'm really interested to learn about it. Going forward as content is getting indexed, week-over-week things look really good. There was a dip on March 1st, which happens sometimes after dumping a bunch of content, but traffic is up. Compare this Saturday to the prior Saturday. One thing I wanted to ask about—I'm not an expert on this—how long does indexing usually take? Some pages from the batch at the end of February are indexed, a couple aren't. How unusual is that?

**Kyle Gaudreau:** When we start publishing at a higher rate, indexing is slower at first but does kick off. We want to validate it's getting added to the sitemap correctly. In the early going, we can go into GSC and request indexing. I'm not sure if that button does anything anymore.

**Jenn Peters:** It's like pushing a button at a crosswalk over and over. My husband and I were just talking about this a couple days ago. It's like, it's going to happen anyway.

**Adrian Machado:** I've never done it manually, but I think one benefit of spreading content out throughout the week is Google probably treats it differently in its indexing pipeline. It probably has a priority queue for domains. If everything dumps on one day, it might not process it the same way.

**Jenn Peters:** Yeah, as we scale our pod and get more help, it should get easier. Next week, let's talk about starting Monday and spreading throughout the week. It's just a matter of time to upload each day. That's been the major constraint so far.

**Kyle Gaudreau:** We can bring in VAs for publishing. As we get to more auto-publishing soon, it becomes easier. The tricky part is making sure the team is structured right. It's easier with tools like Webflow.

**Jenn Peters:** I'm happy to bring on somebody to help upload. Adrian spent time showing me how to do it. I'd rather be showing another person than having Adrian do more training.

**Adrian Machado:** Let's make the process as streamlined as possible. For programmatic content, I might relax guardrails since I probably won't need to review programmatic pages. There's not much value I can add.

**Jenn Peters:** We can set up a bot or automated review.

**Adrian Machado:** We added GitHub Copilot code review, which might be sufficient. We just got it yesterday. The main reason I keep code reviews is it's part of our software compliance. We need code in our repositories to be reviewed. I think it applies to the website too.

**Jenn Peters:** It's been useful for me. I'm learning how to read Vercel error messages. Your end is fast—you're reviewing quickly. My end takes time. I'm still a beginner, but I'm already faster than last week. I was aiming for less than six minutes per review, and I'm getting close.

**Adrian Machado:** We're going to send you the next 10 topics tomorrow so you can review them next week while you have time.

**Jenn Peters:** I should be able to review them at some point next week, after the conference. I'm glad you're adding table of contents. I'll review the ones you've uploaded today later, and more are coming today and tomorrow. One ask: can you report on the performance of articles you're uploading? I'm also producing what I'd call B2B content with demos. I want to differentiate between traffic I'm driving and traffic your content drives.

**Jenn Peters:** Everything's going up and to the right, which is nice. I just want to know where it's coming from.

**Jenn Peters:** I have a spreadsheet tracking individual things, but I do it all manually. Is there a way to build a separate table in Search Console?

**Kyle Gaudreau:** We can take that offline. This is easy. We can filter for certain URLs. There's literally a thread with folks about this. I caught up this morning. We're leveraging Looker Studio more and more. The TLDR is you dump URLs in a spreadsheet as you post, and it pulls data from GSC. We've started building this with some accounts. We're also starting to monitor LLM traffic more.

**Adrian Machado:** I'm happy to connect my GA if you need. One thing on my bucket list is to look into traffic from Perplexity. To give you an idea, I did an analysis. Last week, we saw about 106 visits between Gemini, Perplexity, and ChatGPT. That's up 43% from the previous week. Not crazy, but pretty good. Let me know if there's a way to integrate that into reporting. I'll start reporting it offline to our organization because investors are interested.

**Kyle Gaudreau:** Yeah, LLM traffic is becoming super important. One of our accounts is early stage in publishing but seeing normalish traction in rankings. The LLM side is actually where a lot happens. If we didn't look at that, we'd miss what's really happening.

**Adrian Machado:** LLMs look at 10 to 15 sources at a time, so you don't need to rank #1. It's about quality content and brand mentions.

**Kyle Gaudreau:** Exactly. ChatGPT leaned heavily on review sites early on because they don't have the indexing coverage Google has. Generally, it comes back to good content and brand presence across mediums. That's what LLMs digest. A strong brand presence makes it more likely they'll surface you, outside of good quality content.

**Adrian Machado:** I try to post good quality content to Reddit frequently because they're buying Reddit data. They're mining it, right? So many mentions there as possible.

**Kyle Gaudreau:** It's an interesting world. A lot of people are buying up accounts. It's like astroturfing. Reddit's topic traffic grew insanely over the past year because Google favors it now.

**Adrian Machado:** My conspiracy is that the people doing this are also investors in Reddit.

**Jenn Peters:** Yeah, thank you so much for your time. We'll talk next week.

**Adrian Machado:** Okay. Bye.
