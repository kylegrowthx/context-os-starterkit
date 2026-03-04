# Otto <> Growth X - Weekly Sync

<metadata>
date: 2025-11-20
time: 18:01 UTC
duration: 14 minutes
organizer: team@growthxlabs.com
participants: Bailey Seybolt, Jason Flateboe
fathom_recording_id: 103235726
fathom_url: https://fathom.video/calls/480042643
share_url: https://fathom.video/share/J3zwZ_3xkaxsit4-quJyKW-QyakfyqHB
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Bailey and Jason aligned on three key initiatives: implementing FAQ content and schema markup across Otto's blog and homepage to boost LLM visibility, resolving outstanding article comments and launching five new articles into production using the feature matrix as a source of truth, and preparing for Otto's general release in early-mid December with a focus on tracking traffic from press coverage versus search and LLM sources. Strong performance signals are already trending positive, with citation ownership growing 70% week-over-week and LLM traffic engagement remaining high despite small absolute numbers.

---

## Context

Otto is a GrowthX B2B content marketing client working on AI visibility strategy for their product launch. Bailey Seybolt (GrowthX) and Jason Flateboe (Otto, Product/Marketing) conduct weekly syncs to coordinate on content production, technical implementation, and performance analysis. This is a mid-cycle check-in with Otto's general release delayed two weeks to early-mid December, creating an opportunity to refine traffic attribution and test LLM visibility tactics before the launch spike.

---

## Relevance

**To GrowthX Delivery:**
- FAQ + schema markup strategy proving effective across client accounts for LLM visibility lift
- Feature matrix as content source of truth reducing hallucination in LLM-generated recommendations
- Blog cohort clustering in Looker enabling granular performance analysis by topic area
- General release timing provides controlled test case for measuring press vs. organic vs. LLM traffic attribution

**To CheckThat:**
- Real-world validation of FAQ schema impact on LLM visibility metrics
- Citation ownership growing 70% WoW signals effective AI visibility tactics
- LLM traffic engagement high despite small base, early indication of strong LLM product-market signal

**To GrowthX Business Development:**
- Otto account trajectory positive across all metrics (traffic, search, LLM, citations)
- No expansion risks signaled; solid content pipeline and weekly cadence
- Press coverage expected mid-December creates reference/case study opportunity

---

## Overview

- **New SEO Tactic:** Add per-article FAQs and site-wide FAQ schema to boost LLM visibility, a strategy proven effective on other client accounts.
- **Content Pipeline:** The content pipeline now uses a feature matrix as its source of truth to prevent generating non-existent features. Five new articles are in production.
- **Strong Performance Signals:** Key metrics are trending positively, including high LLM traffic engagement and a 70% WoW increase in citation ownership.
- **Launch Rescheduled:** The general release is pushed back two weeks to early-mid December, creating a new opportunity to analyze traffic sources (search vs. LLM) from the expected press coverage.

---

## Key Topics

### Content Pipeline & Quality

  - All outstanding article comments are now resolved.
  - Five new articles are in production, with delivery expected by EOW.
  - The pipeline now uses the feature matrix as its source of truth.
      - **Rationale:** To prevent generating non-existent features and ensure greater detail accuracy.
      - **Status:** GrowthX will monitor its effectiveness.

### New SEO Tactic: FAQs & Schema

  - **Proposal:** Add per-article FAQs and site-wide FAQ schema to boost LLM visibility.
      - **Rationale:** This strategy has driven significant traffic lifts on other GrowthX client accounts.
  - **Implementation Plan:**
      - **FAQ Content:** GrowthX will generate the per-article FAQ content.
      - **FAQ Schema:** Jason will implement the technical schema markup in Webflow.
          - **Rationale:** A one-time backend update is expected to apply the schema site-wide.
          - **Action:** Jason will investigate existing schema setup from a previous contractor.
      - **Scope:** Apply schema to all core pages, including the homepage.

### Performance & Reporting

  - **Looker Dashboard:** Cohorts are now updated to match blog clusters, enabling more granular performance analysis.
  - **Deep Dive:** Jacob (GrowthX) will conduct a deep dive into account reporting during the week of Dec 8.
      - **Action:** Jason to provide specific questions or areas of concern via Slack before the deep dive.
  - **Key Performance Signals:**
      - **Traffic:** Strong WoW growth across all sources.
      - **Search:** Positive momentum; organic clicks are small but growing.
      - **LLM Traffic:** Growing with high engagement.
          - **CTR Impact:** Top search position → 58% CTR vs. 40% for middle positions.
      - **Citation Ownership:** Grew 70% WoW (from a small base).

### General Release & Press

  - **Launch Rescheduled:** General release moved from this week to early-mid December.
      - **Impact:** Expect a traffic spike from press coverage and direct marketing.
      - **Opportunity:** Analyze traffic sources (search vs. LLM) during the launch.
  - **Press Page:** Jason will create a press page in the Webflow CMS to centralize all coverage.
      - **Action:** Jason to flag high-value press links (e.g., tool roundups) for the GrowthX pipeline to target.

---

## Action Items

**Bailey Seybolt**
- Add per-article FAQ to all new blog posts
- Send async update to Jason on Nov 26
- Add early–mid Dec general release to calendar

**Jason Flateboe**
- Research Webflow FAQ/schema; then implement FAQPage schema sitewide incl homepage
- Add Dec 8 deep-dive reporting to calendar
- Flag press links to Bailey for pipeline targeting

---

## Transcript

**Bailey Seybolt:** This meeting is being recorded.

**Bailey Seybolt:** So one thing I want to call out is I see that there are a few articles that you left comments on that we have not closed out, which we are going to do after this.

**Jason Flateboe:** They kind of slipped through the cracks.

**Bailey Seybolt:** So we did get those all moved through today.

**Bailey Seybolt:** And then there are five more articles in production.

**Jason Flateboe:** Some of it will come to you today and probably some tomorrow, but all by the end of this week.

**Jason Flateboe:** Okay, sounds good.

**Bailey Seybolt:** And we've got a good runway of approved topics right now.

**Bailey Seybolt:** So we're kind of all good there.

**Jason Flateboe:** Unless there's anything you want to flag for us.

**Jason Flateboe:** No, I don't think so.

**Bailey Seybolt:** I think we're looking good.

**Bailey Seybolt:** Yeah, and so I have updated the artifacts in the pipeline based on the features detail that you sent. So that's all updated.

**Bailey Seybolt:** And I'm hoping that that's going to kind of like catch some of the issues we were having where it was going a little too far in recommending features or like creating features that don't exist.

**Bailey Seybolt:** So we've sort of set that to really use that as the source of truth.

**Bailey Seybolt:** So I'm going to continue to keep an eye on how it's treating that, but I'm hoping it will give a little more detail.

**Jason Flateboe:** Yeah, that was a good thing to set up.

**Jason Flateboe:** Yeah, definitely.

**Bailey Seybolt:** So another one, actually one other thing I wanted to talk about is we've seen across some other client accounts that have been experimenting with this.

**Jason Flateboe:** Yeah.

**Bailey Seybolt:** Adding an FAQ to the, and there's sort of two things.

**Bailey Seybolt:** There's like the FAQ and then there's the schema, which is like what you would add to those sort of the blog posts on your end.

**Bailey Seybolt:** And we've seen that both of those seem to have, offer a lift in terms of LLM traffic.

**Bailey Seybolt:** So I think one of the things that I might recommend if you're opening, if you're open to it is sort of just adding a short FAQ section at the bottom of blog posts as just standard practice.

**Jason Flateboe:** That's something we can build into the pipeline.

**Bailey Seybolt:** And either across the board or, you know, if you don't like that idea, we can also like experiment and do it on some of them.

**Bailey Seybolt:** But we have seen it have an impact on LLM traffic.

**Jason Flateboe:** So I think it's worth considering.

**Jason Flateboe:** Yeah, no, let's do it.

**Jason Flateboe:** Would it be the same like shared FAQ across all the articles or it would be specific to each article?

**Bailey Seybolt:** It would be specific to each article.

**Jason Flateboe:** Okay, and so you're saying that would be set up on my end?

**Bailey Seybolt:** So we would do the FAQ content. The schema is something that's a little bit different.

**Bailey Seybolt:** That's something added to the template of the blog post, like on your end, like the setup of code.

**Bailey Seybolt:** So it's usually something that you only have to update once, is my understanding.

**Bailey Seybolt:** So I can get more details because the technical part of it is not my area of expertise.

**Jason Flateboe:** But it should be something that you think you can add once on the backend and then get produced across.

**Jason Flateboe:** If that's the case, yeah, that was going to be my next question.

**Bailey Seybolt:** Yeah, if that's the case, let's give it a shot.

**Bailey Seybolt:** Yeah, and if it's not something, if it's something you have questions about doing on your end, I can like back down more specific, like how that works in Webflow, because everything is a little bit different.

**Bailey Seybolt:** And in terms of schema, like it's something that you can add to all the core pages on your website.

**Bailey Seybolt:** And I know that other people, both our clients and also.

**Bailey Seybolt:** Just based on what people are talking about on LinkedIn in terms of seeing traffic and other companies that have really leaned into LLM visibility, they're seeing an uptick in traffic when they add schema to the core pages of their website.

**Jason Flateboe:** Okay.

**Jason Flateboe:** So yeah, this is interesting because so before I joined Otto, they had hired a marketing contractor part-time to make some updates to the Webflow website.

**Jason Flateboe:** Right.

**Jason Flateboe:** And I noticed that he had set up some, I guess you call them FAQ type schema pages in the CMS system.

**Jason Flateboe:** And I don't think we've linked to those pages.

**Jason Flateboe:** And I was kind of confused about exactly why he did that and how it works.

**Jason Flateboe:** But that's in my mind too.

**Jason Flateboe:** Like as we approach this, like I should look at all that and make sure that's what we want.

**Bailey Seybolt:** And, you know, is that making sense?

**Bailey Seybolt:** So yeah, I think it's something to think about.

**Bailey Seybolt:** I know.

**Bailey Seybolt:** I know, like Webflow just publicly released.

**Bailey Seybolt:** I think they did some experimentation around this, adding this kind of schema markup to both their content and also like their blog content and also just the core pages of their website and said that they did tie it to like a big lift in LLM visibility.

**Bailey Seybolt:** And it's one of those things, too, where it can't hurt, right?

**Bailey Seybolt:** Like it just makes it's like search, right?

**Jason Flateboe:** It just makes your page easier for them to even understand what's going on.

**Bailey Seybolt:** So I feel like these things where it feels like it's not even going to impact, you know, the experience from a user perspective, it can only help in terms of both search and LLM visibility feels like a bit of a like, why not?

**Jason Flateboe:** Yeah, perfect.

**Jason Flateboe:** And so, yeah, once I wrap my head around all this, I'll make sure to do it for our homepage, too, because, you know, that's like 90% of the pages that I own that actually, you know, that matter.

**Jason Flateboe:** So if I can do it on the page to start with, at least.

**Jason Flateboe:** Because we actually do have a small FAQ type, like that's user facing, like, you know, five or six questions.

**Jason Flateboe:** But yeah, if we can get something more behind the scenes going to that, that should be good.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** And it's something where I would like for us at GrowthX to pull together best practices based on what we're seeing across accounts. I'm not sure that exists yet, but this is something I wanted to flag.

**Jason Flateboe:** Because there's certain things we can do on our end, and then obviously there's other stuff you can do on your end.

**Jason Flateboe:** Okay.

**Jason Flateboe:** Well, maybe before we meet next time, I'll try to look into all that, and then I'll just come back with questions, and we can kind of talk in more in depth when I've taken a look.

**Bailey Seybolt:** yeah, that sounds good.

**Bailey Seybolt:** And I'll see if I gather anything else that feels like good context, I can also drop it in Slack.

**Jason Flateboe:** Okay, great.

**Bailey Seybolt:** Oh, I want to touch base next week. I will be off on Thursday for Thanksgiving. Are you okay with doing an async, or we could move our meeting until Wednesday?

**Jason Flateboe:** Let's just do an async. We've got a bunch of people out.

**Bailey Seybolt:** Yeah, that sounds good. So I'll just plan to send out async updates on Wednesday then.

**Jason Flateboe:** Okay.

**Jason Flateboe:** Great.

**Bailey Seybolt:** So in terms of reporting, we did update the cohorts in your looker now.

**Bailey Seybolt:** So they'll match the blog clusters, which I think will be useful going forward to kind of still be able to see, you know, what's performing really well.

**Bailey Seybolt:** What's not.

**Bailey Seybolt:** So, oh, and I also wanted to flag.

**Bailey Seybolt:** So we are planning, Jacob's planning to do sort of a deep dive reporting on your account that week of December 8th.

**Bailey Seybolt:** Just so you sort of have that on your calendar.

**Bailey Seybolt:** And if you have any kind of specific questions around what you're seeing or things you'd specifically like to see, you know, you can let us know or drop that in Slack.

**Bailey Seybolt:** And he can kind of speak to, I think he'll speak generally to everything, but.

**Jason Flateboe:** If you have like specific concerns or questions moving forward, it'd be a time to raise them ahead of that.

**Bailey Seybolt:** So in terms of signals we're seeing this week, the numbers are going up and to the right. We've seen pretty strong growth in traffic over the last week. As always, week-over-week it's sometimes hard to tell what's signal and what's noise, but still good to see. Same thing with search momentum — the number of clicks coming from organic content is still small, but those early signals are good to see and it's all trending in the right direction.

**Bailey Seybolt:** In terms of LLM traffic, same thing — the numbers aren't huge, but it's growing and the signals are positive. The engagement is really high on LLM referral traffic, which is good to see.

**Bailey Seybolt:** And I also noticed comparing the Scrunch dashboard with the Looker Google Search Console data — top versus middle versus bottom positions makes a difference in click rate. It's hard to tell how much of a difference these things make, but in terms of engagement, staying in that top position moved the average click rate to 58% versus 40%. So it's interesting to know.

**Bailey Seybolt:** And then one big growth area — in terms of citation ownership it's still small, but it grew 70% in the last week. Small numbers, but all trending in the direction we like. So it'll be exciting to see the numbers in more months.

**Jason Flateboe:** Yeah, I should let you know we were anticipating our general release happening this week, but we pushed that back two weeks. We're expecting much more direct traffic and press coverage. That'll be happening early to mid-December.

**Bailey Seybolt:** Okay, that's good to know. We'll make sure that's on our calendar. It's always fun to see the spike in traffic that comes. And it's also interesting to see the spike in traffic around a launch — you get to see when it comes through search versus when it comes through LLMs. It serves as an interesting experiment to understand how that stuff tends to trickle in.

**Jason Flateboe:** Yeah.

**Jason Flateboe:** And I do anticipate it being more of a trickle. I don't think there's going to be a particular date where it's everything and then it just falls off. It'll probably be rolling with hopefully some different press articles coming out.

**Bailey Seybolt:** And I think the press stuff is hugely important for LLMs because you get those third-party citations. Sometimes we've seen big lifts around that.

**Jason Flateboe:** Yeah, totally.

**Jason Flateboe:** And so one of the things that's on my list to do in the next week or so is add a press page. Every time there's a new article, I'll set up a photo and a link to it. I'll do that in the CMS so we capture all that stuff and have it on our site.

**Bailey Seybolt:** Yeah, that would be interesting. If you end up in tool roundups and stuff, it would be good to flag those links for our system as links to drive to as well.

**Bailey Seybolt:** It should be the research stage of the pipeline that does that, but it would be good to be aware of those to make sure you're flagging them.

**Jason Flateboe:** Okay, yeah, I'll flag that and keep track of those as I see them.

**Bailey Seybolt:** Yeah, and I imagine you'll be adding them to your website too, so we can always check there. I'll be curious to see if it does a good job with that and make sure we're on it on our end.

**Bailey Seybolt:** All right, I think that is it for me today.

**Jason Flateboe:** Unless you have anything else you want to chat about?

**Jason Flateboe:** No, I don't. Have a good vacation or time off or whatever you're doing.

**Bailey Seybolt:** Happy Thanksgiving. We'll be doing the turkey and everything. We're just staying home though. It's kind of nice when you don't have to travel actually. Sometimes those are the best holidays.

**Jason Flateboe:** Yeah, no traffic. Thanksgiving is supposed to be the worst traffic holiday. It's so condensed, like all the travel is happening at the same time.

**Bailey Seybolt:** Well, sounds good. In the meantime, feel free to reach out on Slack if anything comes up.

**Jason Flateboe:** Sounds good. Thank you. Bye.

**Bailey Seybolt:** Bye.
