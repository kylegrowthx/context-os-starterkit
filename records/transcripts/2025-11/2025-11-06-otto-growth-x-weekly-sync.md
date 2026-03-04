# Otto <> Growth X - Weekly Sync

<metadata>
date: 2025-11-06
time: 18:01 UTC
duration: 17 minutes
organizer: bailey@growthx.ai
participants: Bailey Seybolt (GrowthX), Jason Flateboe (Otto)
fathom_recording_id: 99794455
fathom_url: https://fathom.video/calls/464819490
share_url: https://fathom.video/share/2N2uiLNyHsaVHNhWgsZa9zecgEJqtjky
source: fathom
enriched_on: 2026-03-02 12:45 UTC
speaker_note: Michael Gulmann was invited but did not attend. Jakub Rudnik and Erik O'Brien were invited but did not speak during this call.
</metadata>

---

## Summary

Bailey and Jason synced on Otto's content pipeline strategy, production improvements, and early performance metrics from the new blog. Bailey outlined plans to build a content buffer ahead of the holidays, with Jason to review and curate the topic list by adding 20-30 suggestions and flagging irrelevant topics. The team rolled out a new agentic production pipeline launching next week with improved research, contextual linking, and product feature accuracy; Bailey also fixed table rendering issues in live articles and updated writing guidelines to prevent feature invention. Early signals showed growing impressions and strong LLM engagement, though citation rates are naturally low for a new, unindexed blog—a key metric to monitor as the content library grows.

---

## Context

Bailey Seybolt (GrowthX) and Jason Flateboe (Otto) are collaborating on content and blog performance for Otto, the AI agent product. Otto is a B2B tool (likely for business automation or workflow), and GrowthX is delivering content marketing services. The relationship is client-vendor with weekly sync meetings to align on content pipeline, production workflow, performance tracking, and product feature documentation. Bailey drives the content operations from GrowthX; Jason manages Otto's blog and coordinates editorial decisions. This sync occurred as Otto was preparing to launch a redesigned content pipeline and scale blog publishing ahead of the holiday season—a critical time to maintain audience engagement and accumulate content as a resource library.

---

## Relevance

**To GrowthX Delivery:**
- New agentic production pipeline launching week after this call targets deeper research, better contextual linking (internal and external), and more nuanced product feature descriptions—expect to see quality improvements and higher link density in Otto articles.
- Writing guidelines updated to prevent feature invention and overselling; requires Jason to provide timely product context artifact updates when new features launch (reporting and expense management currently flagged as incomplete).
- Table rendering issue resolved by moving to text-based format instead—now standard for Otto articles; CMS risk reduced unless content explicitly demands table comparisons.
- Holiday buffer strategy and topic curation workflow established; Jason owns topic list review and suggests 20-30 additions to maintain 2+ month publishing runway.

**To GrowthX Business Development:**
- Otto blog is tracking impressions growth and first clicks on new content; early LLM performance metrics show good engagement and improved position quality over the past month (via Scrunch dashboard).
- Citation rate currently very low (targeting 3rd-party sources, not ottotheagent.com domain) but expected for new, unindexed blog—key expansion metric as content library grows and gets indexed.
- Scrunch beta feature (high-intent prompt discovery) may inform future content strategy by surfacing prompts Otto isn't yet ranking for; represents expansion opportunity for content roadmap.

**To CheckThat:**
- Otto blog performance tracking via Scrunch dashboard demonstrates AEO visibility tooling in action; low internal citation rate and strong external positioning indicates opportunity for later product mentions as blog matures.

---

## Overview

- **Content Pipeline:** Jason will review the topic list to build a holiday content buffer. Growth X is testing a new agentic pipeline to improve research and linking quality.
- **Production Fix:** Tables were replaced with text in live articles to fix a Webflow bug. This is now the standard format, as tables are not critical for current content types.
- **Performance Signals:** Early data shows growing impressions and good LLM engagement (position quality, sentiment). The low citation rate is expected for a new blog and will be a key metric to track.
- **Blog Hero:** Jason will manage the blog hero section, as it's a minor UI element for browsing users and has no direct SEO impact.

---

## Key Topics

### Content Pipeline & Strategy

  - **Goal:** Build a content buffer for the holidays to ensure continuous publishing despite team time off.
  - **Action:** Jason will review the topic list to streamline the pipeline.
      - **Option 1:** Approve a large batch of topics.
      - **Option 2:** Flag irrelevant topics for removal.
  - **Rationale:** This review helps Growth X plan future keyword research and maintain a relevant content calendar.

### Content Production Updates

  - **Pipeline Upgrade:** Growth X is testing a new agentic pipeline for content production, launching next week.
      - **Expected Improvements:** Deeper, more accurate research; better contextual linking (internal & external); more nuanced product feature descriptions.
      - **Action:** Jason to report any quality issues observed in next week's content.
  - **Writing Guidelines:** Updated to prevent "overselling" or inventing non-existent features (e.g., for reporting/expense management).
      - **Action:** Jason to provide timely updates on new features to keep the "product context artifact" accurate.
  - **Table Fix:** Replaced tables with text in live articles to resolve a Webflow bug.
      - **Decision:** This is now the standard format. Tables are not needed for current content types and are less user-friendly.

### Performance & Reporting

  - **Looker Dashboard:** Bailey identified a bug in the blog post cohort setup and will investigate.
  - **Early Signals:** Impressions are growing, and first clicks on new content are occurring.
  - **LLM Performance (via Scrunch):**
      - **Engagement:** High.
      - **Position Quality:** Improved over the last month.
      - **Citation Rate:** Low (currently citing 3rd-party sources, not ottotheagent.com).
          - **Rationale:** This is normal for a new blog with a small, unindexed library. It will be a key metric to watch as the content library grows.
  - **New Feature (Beta):** Scrunch is testing a tool that finds relevant, high-intent prompts the blog isn't currently ranking for. This may inform future content strategy.

### Blog Hero Section Management

  - **Context:** The Webflow blog page has a hero section controlled by a "hero toggle" on each article.
  - **Decision:** Jason will manage the hero section.
      - **Rationale:** It's a minor UI element for browsing users, not a primary SEO driver. It's best used for internal priorities (e.g., product announcements) or featuring top-performing articles.

---

## Action Items

**Jason Flateboe**
- Add 20–30 content topic suggestions to calendar
- Review calendar; flag irrelevant topics w/ comments; add suggestions

**Bailey Seybolt**
- Investigate Looker cohorts mismatch; update Jason

---

## Transcript
**Jason Flateboe:** Hey, sorry, I was on mute.

**Bailey Seybolt:** No worries.

**Jason Flateboe:** We got Michael here, too.

**Jason Flateboe:** I'm just dialing in so you can see my face.

**Bailey Seybolt:** Oh, hi, everyone.

**Jason Flateboe:** What's new?

**Bailey Seybolt:** Not much.

**Bailey Seybolt:** How are you all doing?

**Bailey Seybolt:** It feels like winter over here in Vermont.

**Jason Flateboe:** Yeah, we're in the rainy, dark season now, but we're cranking along.

**Bailey Seybolt:** It's good.

**Bailey Seybolt:** I think it's just going to be the three of us today.

**Bailey Seybolt:** Jacob will, like we talked about, join sometimes, especially around more deep dive and reporting, but probably not every time.

**Bailey Seybolt:** But I will be capturing anything that he needs to sort of be aware of and bring to his attention as well.

**Jason Flateboe:** Okay, sounds good.

**Jason Flateboe:** Nice thing.

**Jason Flateboe:** We can just loop him in if we have a specific.

**Bailey Seybolt:** Yeah, exactly.

**Bailey Seybolt:** And if there's anything specific too, like, you can always throw questions in Slack.

**Bailey Seybolt:** And if there's something specific you want to talk about during that he should be there for, he can kind of plan to drop into those meetings as well.

**Jason Flateboe:** Jason, you're in another video, by the way.

**Bailey Seybolt:** You guys matching. It's so funny.

**Jason Flateboe:** You're matching. We're sitting in the same booth.

**Bailey Seybolt:** Oh, one of the double wides.

**Jason Flateboe:** Yeah.

**Bailey Seybolt:** You know, those are so funny because it's so hard to share them.

**Bailey Seybolt:** Like, you can't be on the same screen.

**Bailey Seybolt:** So I guess they're more for people, like, collaborating together.

**Jason Flateboe:** But it's very awkward.

**Jason Flateboe:** It's good for just a quick one-on-one when you're in a pretty open office environment like we are.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** So I'll share our agenda for today.

**Bailey Seybolt:** There's not a ton of, like, urgent business to cover.

**Bailey Seybolt:** So more just.

**Bailey Seybolt:** So we've got a good, we've got like, I think 12 like articles that are approved to start.

**Jason Flateboe:** So we've got a good content runway.

**Bailey Seybolt:** I wanted to flag that with the holidays coming up, I am going to try to start working towards getting us a bit ahead on content.

**Bailey Seybolt:** So that way, if you go out of town, if our team, people are taking time off, we can make sure that those are kind of like ideally queued up and staged, and then you can set them to publish.

**Bailey Seybolt:** And then don't have to worry about, you know, if you want to publish something on December 23rd, and you're offline, it will be there waiting for you.

**Jason Flateboe:** So we're fine now.

**Jason Flateboe:** But for next week, it'd be great to go in there and pick out a few topics that we can start working towards that over the next couple months.

**Jason Flateboe:** Okay, I can go in and I'll just add a couple dozen or something that'll keep us going, you know.

**Bailey Seybolt:** Yeah, that's perfect.

**Bailey Seybolt:** That's great.

**Bailey Seybolt:** And then we'll also know kind of when you get to the end of, you know, if you hit a wall and the rest of the topics aren't relevant, then we'll know to sort of plan to do additional keyword research.

**Jason Flateboe:** And have that coming down our content calendar as well. Would it, alternately, be useful to go through the whole list and just remove any that were like no's, and then work through everything else?

**Bailey Seybolt:** Yeah.

**Jason Flateboe:** Because I feel like 90% of what's in there is, yeah, that could be an article.

**Bailey Seybolt:** Maybe another approach.

**Bailey Seybolt:** I think that's really helpful.

**Bailey Seybolt:** I mean, and you can see it too, if you want to go in, if it makes more sense to just go in and flag the ones that aren't relevant, and especially if you end up leaving a comment, just letting us know why, like that always helps inform your research.

**Bailey Seybolt:** So I think either way works.

**Bailey Seybolt:** You can go in and kind of like pick the ones that are approved to start, or you could just flag the ones that feel not relevant.

**Jason Flateboe:** And we'll just pull those out and assume the other ones we can just build into our content calendar. Yeah, that makes sense.

**Jason Flateboe:** There may be a few, too, that we could add as suggestions, just like, hey, can we do something in this area?

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** That's perfect.

**Bailey Seybolt:** Perfect.

**Bailey Seybolt:** And yeah, and that'll help us kind of plan ahead and know when we should be queuing up additional research as well and kind of planning for that.

**Jason Flateboe:** Okay.

**Bailey Seybolt:** Awesome.

**Bailey Seybolt:** So we've got four more in production, I think, this week, which will be sent to you all today and tomorrow.

**Bailey Seybolt:** We updated the live articles with the tables.

**Bailey Seybolt:** We just replaced those with text.

**Bailey Seybolt:** So they stopped breaking Webflow.

**Bailey Seybolt:** I think we do have another fix on our end, but I'm going to see how it goes with other clients before we go down that road again.

**Bailey Seybolt:** Because unless it's really worth it, it may just not be worth messing with the CMS unless the content really demands that table.

**Jason Flateboe:** Yeah.

**Jason Flateboe:** I think I just have a general preference towards just regular content anyway.

**Jason Flateboe:** I don't know that even humans are going to really want to look through a 5x10 grid of a table.

**Bailey Seybolt:** that's fair, yeah.

**Bailey Seybolt:** I think the only place that often comes in handy, especially in really long articles, like if you have a super long tool comparison article.

**Bailey Seybolt:** Sometimes it's nice to have that recap as a table at the end, especially if it's really qualitative and you're like doing a features comparison, but that's not really content that I think we have encountered right now in our pipeline anyway.

**Jason Flateboe:** So I think for the most part, we can just stay away from them.

**Bailey Seybolt:** I did want to flag that this week we are moving auto.

**Bailey Seybolt:** We've developed a new agentic pipeline for auto.

**Bailey Seybolt:** So we're going to be moving content production onto that new pipeline, I think, starting next week.

**Bailey Seybolt:** So we're testing it this week, and I should be diving in later today to take a look at the results.

**Bailey Seybolt:** In terms of what you see, it probably won't change anything.

**Bailey Seybolt:** Like it certainly shouldn't be making anything worse.

**Bailey Seybolt:** I think what it's really good at, it's often much better at providing research, like contextual links, both within Otto's blog as you build out a bigger library and also...

**Bailey Seybolt:** Linking to outside research as well.

**Bailey Seybolt:** It's just much better at understanding, doing the research and understanding the context.

**Bailey Seybolt:** And then I think it's also much more powerful at nuances around product features and context—going deeper into that as well.

**Bailey Seybolt:** So we may be calibrating a little bit as we move on to that because it has certain things it does in the pipeline.

**Bailey Seybolt:** And so we sort of update our writing guidelines to reflect that. So if you notice anything that feels off in next week's content, let us know.

**Bailey Seybolt:** But you probably won't see anything different on your end.

**Bailey Seybolt:** If anything, it should just continue to get better.

**Jason Flateboe:** Okay.

**Bailey Seybolt:** Great.

**Bailey Seybolt:** And I did update our writing guidelines to address sort of the tendency we were noticing to oversell on some of the features and, you know, make up features or suggest that there are features that don't really exist.

**Bailey Seybolt:** So we're, you know, editing that out when we see it, but hopefully that that won't be an issue going forward, especially with this agenda.

**Jason Flateboe:** Yeah, it was mainly just on the reporting and expense management stuff that just, that was the main area.

**Bailey Seybolt:** We'll get there.

**Bailey Seybolt:** We're just not there yet.

**Bailey Seybolt:** And I guess it's on us to tell you too when things change because we're adding new features too.

**Bailey Seybolt:** So that's like, hey, now we can do X.

**Bailey Seybolt:** Yeah, that would be really helpful because we do have like a product context artifact.

**Bailey Seybolt:** And the more we can update that, that would be great to know when those features get added.

**Bailey Seybolt:** Because I think what it's trying to do right now is like map auto to like every point in the article to make it clear how relevant it is.

**Jason Flateboe:** And it's just like, it's just over, it's doing, it's going too far, I think.

**Bailey Seybolt:** It's sort of what's happening now.

**Bailey Seybolt:** So we updated our artifacts to pull it back to reality a little bit and not invent features, which might be great, you know.

**Bailey Seybolt:** I don't even know.

**Jason Flateboe:** Okay, sounds good.

**Bailey Seybolt:** Okay, awesome.

**Bailey Seybolt:** And then in terms of reporting, like we mentioned,

**Bailey Seybolt:** Jacob will do more of a deep dive on sort of a more monthly cadence, but there's two things.

**Bailey Seybolt:** One, I was in the Looker dashboard right before this, and I noticed that I think there's an issue with the way the cohorts are set up for blog posts.

**Bailey Seybolt:** So if you're in there and you're looking and it feels like the cohorts aren't matching reality, you are correct, and I'm going to look into that right after this to see what's going on there.

**Bailey Seybolt:** I don't think it's a problem with the content because it's showing like clicks and impressions.

**Bailey Seybolt:** It's just not being reflected on that cohorts page, which maps to your different content clusters, and I'm not sure why.

**Bailey Seybolt:** So I will look into that after this.

**Bailey Seybolt:** But in terms of just general kind of signals, you know, impressions are growing.

**Bailey Seybolt:** We're kind of seeing first clicks on content.

**Bailey Seybolt:** In terms of LLM traffic, you know, we're seeing like good signals here.

**Bailey Seybolt:** You know, the engagement is high.

**Bailey Seybolt:** You know, the position quality is in.

**Bailey Seybolt:** improved over, like, the last month in terms of, like, where you're appearing in the answers.

**Bailey Seybolt:** I think the citation rate is still very low, but that's kind of expected because the blog is new and there's just not that much content for it to send people to yet.

**Bailey Seybolt:** So I think that's something that we see grow, you know, significantly as the content gets scraped and indexed and as we just have a growing library of content.

**Bailey Seybolt:** But, you know, I think it's nice to sometimes see where the baseline is and see where these early signals are.

**Jason Flateboe:** It's nice to see us sitting right above Expedia in some metric.

**Jason Flateboe:** Yeah, right?

**Jason Flateboe:** What is the question that we're looking for here or how is this calculated?

**Bailey Seybolt:** Yeah, so this is sort of looking at basically when we set up your Scrunch dashboard—which is what Ada set up—it's basically setting up tracking a certain number of prompts that are relevant for your business.

**Bailey Seybolt:** And so it will...

**Bailey Seybolt:** Track kind of where you are appearing in comparison to the competitors in these prompts.

**Bailey Seybolt:** So like what percentage you're showing up on and then, you know, where you show up in the response, like what is the sentiment when you show up and then where is it like citing owned material from your brand and sending people to your site?

**Jason Flateboe:** Okay, so our brand is low.

**Jason Flateboe:** We're getting mainly third-party citations at this point.

**Bailey Seybolt:** Yes, which is what exactly what would be, I think first this number, I mean, I think even when brands are doing really well, like you're seeing numbers in 20%, like you're never getting 100% of your, you know, citations from your brand.

**Bailey Seybolt:** But I think this means you're getting mentioned contextually, but they are not yet citing material from your website itself—they're not sending people to your blogs most of the time.

**Bailey Seybolt:** But again, that's.

**Bailey Seybolt:** But based on where we are right now, that's absolutely what we'd expect.

**Bailey Seybolt:** So this is the number that I think, I mean, all of it, we'll see trending up is what we want.

**Bailey Seybolt:** But for sure, this one for a new blog publication with not much content and content that's still indexing, especially in that first month, this is like totally normal on what we'd expect to see.

**Bailey Seybolt:** So this is one that we'll definitely want to keep an eye on and like, you know, reporting, especially after we've been publishing for a couple months.

**Bailey Seybolt:** Like this is, I think, one of the more, the most interesting ones to see what's changing.

**Bailey Seybolt:** And they've also just released a new feature, which is still in beta, but it's pretty interesting that sort of scrapes prompts—basically questions people are asking that you're not showing up for but that you could be showing up for that feel relevant—which is often different from the SEO keyword. Sometimes there's overlap there, but sometimes it's quite different. And sometimes they're very specific prompts, which can be useful, but wouldn't necessarily be reflected in keyword research—these kind of hyper-specific, high-intention prompts. So that's sort of an interesting feature.

**Bailey Seybolt:** And like I said, it's still in beta, but I think it'll be something to keep an eye on. Down the road when we're planning out content, it could be useful to see what kind of prompts they've come up with and consider those as well.

**Jason Flateboe:** Right.

**Jason Flateboe:** Yeah.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** Well, I think that is it from my end.

**Bailey Seybolt:** Is there anything else you all wanted to chat about today?

**Jason Flateboe:** I had one question.

**Jason Flateboe:** So I have the Webflow blog page, right, that has all of the different articles on it.

**Jason Flateboe:** I have a hero section on that.

**Jason Flateboe:** And it is, there's a toggle that turns on.

**Jason Flateboe:** Any article can be placed in the hero.

**Bailey Seybolt:** Just.

**Jason Flateboe:** And it's been just the same featured article this whole time.

**Jason Flateboe:** So I guess the question is, is that something that you guys would like me to, you know, determine and manage?

**Jason Flateboe:** Or is there a benefit to having you guys sort of say, oh, this, we think this is a good candidate to be in the hero section.

**Jason Flateboe:** I just wonder what you think the best process for that would be.

**Bailey Seybolt:** And where is that, is that visible?

**Bailey Seybolt:** Is that sort of when you land on your blog's homepage or is that like drive anywhere from your, like your homepage?

**Jason Flateboe:** It's only, it's only when you hit the blog, when you go to the homepage, you click blog and the navigation, it sits at the top of the blog page.

**Bailey Seybolt:** It's a little bit bigger and, you know.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** I think I would look to see in terms of like user behavior, the way traffic lands on your blog, like whether people tend to find content that way and land on that blog homepage, or if they're really going through to more specific content, because it may be one of those.

**Jason Flateboe:** Things that doesn't matter that much, if that's not the way they're discovering content.

**Jason Flateboe:** I think that's probably true.

**Jason Flateboe:** And if that's the case, I'm happy to kind of, you know, keep an eye on it and hit the top of myself.

**Jason Flateboe:** And, you know, there may be content that we care about, too, internally.

**Jason Flateboe:** Like, you know, when we have a launch announcement post, I'll probably just put that on as the hero.

**Jason Flateboe:** We can manage that.

**Jason Flateboe:** Do the search engines or the LMs, as far as we can tell, so far care if it's in the hero position or somewhere else?

**Jason Flateboe:** I'd be surprised if they even knew.

**Bailey Seybolt:** Yeah, I don't think that's something that they directly would care about.

**Bailey Seybolt:** It may be, like I said, if people are coming to that page, like, they'll be more likely to click on it if it's at the top and it's in a hero position.

**Bailey Seybolt:** And so it may be one of those ones if we find that, you know, a blog post is performing really well or you're getting, you know, conversions to, like, sign up for, you know, it may be worth featuring a blog post that seems to be performing really well because, you know, it can help.

**Bailey Seybolt:** Why not, right?

**Bailey Seybolt:** Or if there's, like, something you specifically want.

**Bailey Seybolt:** A highlight, like, yeah, like a product announcement, because presumably anyone who comes to that homepage, their behavior is more like they're browsing to see what else you have.

**Bailey Seybolt:** So I would think that that's sort of why they're there, is they're probably not looking for something specific.

**Bailey Seybolt:** They maybe come in through a piece of content and they're, like, curious what else is there.

**Bailey Seybolt:** So I would think, yeah, more about matching the user behavior that lands there.

**Bailey Seybolt:** But I'm also happy to ask around and see if, like, there are any kind of other best practices around.

**Jason Flateboe:** Okay, yeah, if you have any more thoughts about it, I'd be interested to hear.

**Jason Flateboe:** But I think I'm comfortable, too, just kind of managing as it is.

**Jason Flateboe:** And we can, you guys don't have to worry about that.

**Bailey Seybolt:** Yeah, I would think so.

**Bailey Seybolt:** Because I think most, like, most traffic that we're targeting is coming through search or through LLM citations.

**Bailey Seybolt:** And that's sort of not the way they're going to discover your content.

**Bailey Seybolt:** So my impulse would be to say, like, don't worry too much about it.

**Bailey Seybolt:** But, you know, why not?

**Bailey Seybolt:** Like, that space to help.

**Jason Flateboe:** If it's not something that's doing well or that's important to you.

**Jason Flateboe:** Okay.

**Jason Flateboe:** Sounds good.

**Jason Flateboe:** Excellent.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** Well, if that's it, then it's good to see you and have a good week.

**Bailey Seybolt:** You too.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** Bye.
