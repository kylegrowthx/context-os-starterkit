# Redis <> GrowthX - Weekly Sync

<metadata>
date: 2025-12-11
time: 17:30 UTC
duration: 28 minutes
organizer: team@growthxlabs.com
participants: Erik O'Brien, Aida Knezevic, Tyler Pavlas, Alexis Ruiz-Pedregon, Fung-Lin Wu, Reet Mand, Megan Boone, Rebekah Reddis, Andy Varshneya, Allison Gregory, Cody Henshaw
fathom_recording_id: 108109813
fathom_url: https://fathom.video/calls/502140504
share_url: https://fathom.video/share/PUNAVufGwBX3urVT3JAzJES2vtt8Trzg
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

GrowthX and Redis discussed Phase 1 progress: two blog articles are live with one already indexed by Google, and a Looker dashboard is tracking content performance by topic cluster with notably high LLM-referred engagement rates (>50%). The team confirmed Phase 2 approval and identified key workflow improvements including GrowthX creating blog thumbnails using Redis's Canva templates and building custom AI artifacts to streamline PMM review cycles.

---

## Context

Redis is a partner on a content marketing engagement with GrowthX designed to produce 40+ high-quality technical blog articles per quarter targeting developer and data engineer audiences. The engagement is structured in phases: an initial 8-week trial (Phase 1) ending in December 2025, followed by Phase 2 contingent on Redis's satisfaction with quality, workflow, and team performance. This meeting represents week 7 of the trial, where the team reviewed production progress, performance metrics from the Looker dashboard, and workflow optimizations for scaling thumbnail creation and streamlining content review.

---

## Relevance

**To GrowthX Delivery:**
- Looker dashboard is operational and tracking content performance by topic cluster and LLM referral source, enabling data-driven optimization
- GrowthX will build custom AI artifacts ("Examples of Good") trained on Redis's approved articles to improve draft quality and reduce review cycles
- Phase 1 PMM review process is lighter than expected (minimal feedback from Cody/Allison), validating the team's article generation pipeline; post-trial goal is to remove PMM from the process entirely
- Blog thumbnail generation will be built into the agentic article pipeline using Katya (GrowthX designer) to replicate Redis's Canva templates, eliminating a bottleneck for scaling to 40 articles/quarter

**To GrowthX Business Development:**
- Redis has confirmed Phase 2 approval in writing, removing renewal risk through at least Q1 2026
- Client satisfaction is high: Fung-Lin stated "I think for answers, we're happy with this partnership so far"
- Expansion signal: Redis plans to move from tight PMM resource constraints to a hands-off model, suggesting team confidence in GrowthX's capability and willingness to scale

**To CheckThat:**
- LLM referral data reveals ChatGPT, Perplexity, and Google Gemini as top citation sources; Redis's GrowthX-authored content is positioned to capture LLM visibility in developer and infrastructure verticals
- Engagement rate from LLM traffic (>50%) far exceeds overall site engagement, indicating strong content-audience fit for AEO-optimized content targeting AI agents

---

## Overview

- **Content Live:** Two articles are live; "Top AI Use Cases in Financial Services" is already indexed by Google, signaling quality.
- **Performance Tracking:** A new Looker dashboard tracks GrowthX content performance by topic cluster and LLM referral, revealing high engagement (\>50%) from LLM traffic.
- **Workflow Streamlined:** GrowthX will now create blog thumbnails using Redis's Canva templates, removing a bottleneck for the Redis team.
- **Phase 2 Approved:** Fung-Lin confirmed the partnership will continue, moving past the initial 8-week trial.

---

## Key Topics

### Content Production & Review

  - **Live Content:** Two articles are published.
      - "Top AI Use Cases in Financial Services" is already indexed by Google, confirming its quality and comprehensiveness.
  - **Backlog:** Last week's batch of 5 articles is ready for review.
      - **Status:** 3 articles are ready to publish; 2 require minor edits based on Allison's feedback.
      - **Process:** Fung-Lin will coordinate with the PMM team for a final review.
  - **Future State:** The goal is to reduce PMM review time after the initial 8-week sprint to enable scaling to 40 articles/quarter.
      - GrowthX will build a "Examples of Good" artifact from approved articles to train its AI on Redis's tone, improving draft quality.

### Performance Tracking (Looker Dashboard)

  - Aida demoed the new Looker dashboard for tracking GrowthX content performance.
  - **Key Features:**
      - **Cohorts Page:** Filters data to show only GrowthX content, broken down by topic cluster.
      - **LLM Referral Report:** Shows traffic from Large Language Models (LLMs).
          - **Top Sources:** ChatGPT, Perplexity, Google Gemini.
          - **Insight:** LLM-referred traffic has a high engagement rate (\>50%), indicating strong content-audience fit.
  - **Action:** Aida will add a table to track individual article performance.

### Blog Thumbnails

  - **Requirement:** Thumbnails are needed for all blog posts for social sharing and the main blog page.
  - **Solution:** GrowthX will create them.
      - **Process:** Alexis will provide screenshots of Redis's Canva templates (including color palettes). GrowthX's designer will then replicate the style.
      - **Action:** GrowthX will generate thumbnails for all previously delivered articles.

### Phase 2 & Future Initiatives

  - **Phase 2 Confirmation:** Fung-Lin confirmed the partnership will continue beyond the 8-week trial.
  - **Upcoming Deliverables:**
      - **Phase 1 Summary:** A report on progress and plans for Phase 2.
      - **Technical SEO Audit:** A list of site issues to resolve for improved SEO and performance.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Add URLs of published Redis blog posts to GrowthX Looker dashboard
- Send this week's 5 articles to Cody/Allison in Slack; then publish on approval
- Resolve Allison's comments on 'Vector Similarity' and 'Database Performance Optimization'
- Send Fung-Lin Slack thread link for last week's batch
- Update 'What is an AI agent?' blog post date in CMS

**Fung-Lin Wu (Redis)**
- Ping PMM re: last week's batch; then send green light to Aida

**Alexis Ruiz-Pedregon (Redis)**
- Send Aida thumbnail screenshots/templates; then GrowthX implement generator + backfill

---

## Transcript

**Erik O'Brien:** This meeting is being recorded.

**Erik O'Brien:** Hey, Alexis.

**Alexis Ruiz:** How are you all?

**Aida Knezevic:** Good, how are you?

**Alexis Ruiz:** Good, good.

**Alexis Ruiz:** Yes.

**Alexis Ruiz:** It seems like everyone else is running a bit late.

**Aida Knezevic:** No worries.

**Aida Knezevic:** No worries.

**Aida Knezevic:** Thank you.

**Alexis Ruiz:** There's Reet.

**Reet Mand:** Hello.

**Reet Mand:** Hi, Team.

**Erik O'Brien:** Hey there.

**Reet Mand:** Hello.

**Reet Mand:** Are you waiting on anyone that has this?

**Alexis Ruiz:** Yes, Fung-Lin, and I think Cody also said, but maybe we could get started.

**Reet Mand:** Okay.

**Reet Mand:** I think we can get started without Cody.

**Reet Mand:** I don't know if we need Fung-Lin.

**Reet Mand:** I don't know.

**Reet Mand:** If we do, then we can wait for her.

**Aida Knezevic:** Oh, there she is.

**Aida Knezevic:** Oh, there she is.

**Reet Mand:** Yeah.

**Alexis Ruiz:** Perfect.

**Fung-Lin Wu:** Hi.

**Fung-Lin Wu:** Sorry.

**Aida Knezevic:** Hi.

**Fung-Lin Wu:** How are you all?

**Aida Knezevic:** Good.

**Aida Knezevic:** How are you?

**Fung-Lin Wu:** Good.

**Aida Knezevic:** Great.

**Aida Knezevic:** All right.

**Aida Knezevic:** I think Cody is also going, because he's also supposed to join, but I think we can get started.

**Fung-Lin Wu:** Yeah, I don't think Cody can make it.

**Aida Knezevic:** Okay.

**Fung-Lin Wu:** All right.

**Fung-Lin Wu:** That makes sense.

**Aida Knezevic:** All right.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** So, yeah, I dropped the agenda in our Slack.

**Aida Knezevic:** channel, but I'm going to go and share my screen as well.

**Aida Knezevic:** So to give you a quick update of what's been going on on the content production side.

**Aida Knezevic:** So we published two articles.

**Aida Knezevic:** Cody was able to, like, verify yesterday that we staged the content correctly in your CMS, did everything look good, and he published those two live.

**Aida Knezevic:** The new one, this one, the top AI use cases and financial services, it's already been indexed by Google.

**Aida Knezevic:** That means that Google's crawlers, like, discovered it automatically and indexed it, so it can already start appearing in search results, which is great, because Google's crawlers and generally search engines, they don't want to serve content that's thin and unhelpful.

**Aida Knezevic:** So by being indexed, it means that the content is comprehensive enough.

**Aida Knezevic:** So

**Aida Knezevic:** So, yeah, we're going to add this URL and the subsequent URLs that we publish, we're going to add them to our Looker dashboard so we can start tracking the performance of these blog posts that we've been publishing.

**Aida Knezevic:** And then the next step is to publish last week's batch of content.

**Fung-Lin Wu:** Is there a separate Looker dashboard you guys are creating for us?

**Aida Knezevic:** There is a Looker dashboard, there's a report in the dashboard called Cohorts, and it's going to just focus on GrowthX content performance.

**Aida Knezevic:** I can share it right now.

**Fung-Lin Wu:** Yeah, yeah, I would love that.

**Fung-Lin Wu:** don't know if we have.

**Alexis Ruiz:** Yeah, I don't have it.

**Alexis Ruiz:** Yeah, I don't remember getting it either, but maybe we're just waiting till we publish content, I think.

**Aida Knezevic:** Let me just check.

**Aida Knezevic:** We have it set up for you.

**Aida Knezevic:** Yeah, we have shared it, but this was probably a few weeks ago, so...

**Aida Knezevic:** Let me just show my screen again.

**Aida Knezevic:** All right.

**Aida Knezevic:** So, yeah, this is the Looker report.

**Aida Knezevic:** I'll drop the link in chat so you can bookmark it.

**Aida Knezevic:** So, yeah, it's a multi-page report.

**Aida Knezevic:** And the content performance of GrowthX content is going to be here in cohorts.

**Aida Knezevic:** So, this page filters non-GrowthX content performance from GrowthX.

**Aida Knezevic:** So, and it pulls data from both, like, Google Analytics 4, which is this table right here.

**Aida Knezevic:** So, you can see the engagement rate.

**Aida Knezevic:** And then it pulls data from Google Search Console, which is just Google Search traffic.

**Aida Knezevic:** So, we can see the impact on just, like, Google Search and Google, like, overall, like, performance.

**Aida Knezevic:** And then for, I mean, these two tables.

**Aida Knezevic:** The way that they display the traffic is that they categorize the content into the topic clusters that we have, like, right here.

**Alexis Ruiz:** these are the topic clusters that we're targeting with our initial strategy.

**Alexis Ruiz:** Alexis, you're not able to.

**Alexis Ruiz:** I'll share access with you.

**Aida Knezevic:** Okay, thank you.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So these are the topic clusters that we're targeting with our content.

**Aida Knezevic:** And then it's this, they are going to show up in this table once we start, like, once the content, like, starts getting impressions and clicks.

**Aida Knezevic:** But we can also add an additional table that's just going to show the performance of individual, like, blog pages that we publish.

**Aida Knezevic:** So that allows us to kind of go really granular and see how the individual blog posts are performing.

**Aida Knezevic:** And I think another really interesting page in this report is the LLM referral report.

**Aida Knezevic:** report.

**Aida Knezevic:** This is data from Google Analytics, and it breaks down the traffic that comes to your website from different LLMs.

**Aida Knezevic:** So we just have to wait a little bit for the traffic, for the data to load.

**Aida Knezevic:** But here you can see, like, what are the biggest drivers of LLM traffic?

**Aida Knezevic:** So obviously, ChatGPT is at the top, followed by Perplexity and Google Gemini.

**Aida Knezevic:** And then you can also see the landing pages that are getting the most traffic from LLMs.

**Aida Knezevic:** And this is where we're also going to be tracking the performance of our blogs.

**Aida Knezevic:** So as we start, like, publishing more and more, we want to start seeing our blog posts also appear in LLM citations and driving traffic to your site from LLMs.

**Aida Knezevic:** Yeah, so this is the kind of a graph breakdown of LLM traffic to your site.

**Aida Knezevic:** This is for the entire year.

**Fung-Lin Wu:** This is really helpful.

**Alexis Ruiz:** Yeah, I love this.

**Fung-Lin Wu:** Especially the breakdown of OM.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** And I was able to access the report.

**Aida Knezevic:** It was an issue on my end.

**Aida Knezevic:** Okay, yeah, it was probably the wrong email.

**Alexis Ruiz:** Yeah, it was the wrong email for some reason.

**Alexis Ruiz:** was trying my personal, which was weird because I'm logged in with my work email.

**Aida Knezevic:** Yes, I meant thank you.

**Aida Knezevic:** By you're all editors on this dashboard, so that should allow you to kind of, like, change the dates here and, like, play around with the data.

**Aida Knezevic:** But, yeah, this does look, I mean, ChatGPT is, like, the biggest driver of LLM traffic for every single client that we have.

**Aida Knezevic:** But, like, Google Gemini has been, like, gaining ground steadily.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So, Um...

**Aida Knezevic:** All right.

**Aida Knezevic:** And then you can also, for this report, it's super important to kind of see the engagement rate.

**Aida Knezevic:** I think I broke this down when I was first presenting the performance report, but basically the engagement rate is the opposite of bounce rate.

**Aida Knezevic:** So an engaged session is a session that lasts longer than 10 seconds, or it includes a page scroll or includes somebody clicking on a link on your site.

**Aida Knezevic:** So what's really interesting is that for a lot of these landing pages that are getting clicks from LLMs, your engagement rate is quite high.

**Aida Knezevic:** So over 50% for like the vast majority of these, of these URLs.

**Aida Knezevic:** And what's interesting is that when you go to your like overall like sessions versus engaged sessions, is that overall your engagement rate is quite low compared to the totality of your traffic.

**Aida Knezevic:** So that's something to kind of explore in the sense that we want to be able to see like, okay, what are the traffic, like what are the, at least when we're publishing our blog content, we want to be able to see like what blog posts get more engagement versus less engagement and how can we optimize what's not performing well to get more engagement.

**Aida Knezevic:** And this typically means just making the content easier to like more readable.

**Aida Knezevic:** So like making the sections, like, you know, chunking them and like making it very clear what each section is going to cover.

**Aida Knezevic:** But yeah, so that's kind of an interesting thing that I wanted to flag to you.

**Aida Knezevic:** All right, and then if you have any requests for how you want us to customize this performance report, let us know and I'll check in with our team to see what we can do.

**Aida Knezevic:** We have been able to like create additional reports or like additional views to.

**Aida Knezevic:** So, like, just, like, provide the insights that you're really looking for more easily.

**Aida Knezevic:** All right.

**Aida Knezevic:** And then for the content that we are working on this week, so the five new articles for this week are already ready for review.

**Aida Knezevic:** I'll send them in the external channel and tag both Cody and Allison.

**Aida Knezevic:** I know that Allison reviewed last week's batch of content.

**Aida Knezevic:** These are five blogs.

**Aida Knezevic:** I was wondering if we should wait on Cody to review that batch as well or if we could just go ahead and publish.

**Aida Knezevic:** Because his feedback so far, I believe, hasn't been very extensive.

**Fung-Lin Wu:** So maybe, I don't know if he feels comfortable with us just moving forward with publishing.

**Fung-Lin Wu:** see what the batch?

**Fung-Lin Wu:** Do you mind showing me the batch real quick?

**Aida Knezevic:** Sure.

**Aida Knezevic:** Sure.

**Aida Knezevic:** So let

**Aida Knezevic:** just open Slack really quickly.

**Aida Knezevic:** Okay, so these are, what is stream processing?

**Aida Knezevic:** Sorry, these are ready to publish.

**Aida Knezevic:** Yeah, so what is stream processing, hybrid search, how to evaluate RAG systems, AI use cases, this has already been published, and this has already been published.

**Aida Knezevic:** So these are, these three should be ready to publish.

**Aida Knezevic:** I think Allison left just two comments in the other two, which are vector similarity and database performance optimization that we just need to resolve, and that those two should also be ready to publish.

**Fung-Lin Wu:** Got it, okay.

**Fung-Lin Wu:** Yeah, let me just, I'll take a look at them, and I'll, let me just ping the PMM team real quick on it, and then I can try to get back to

**Fung-Lin Wu:** We wanted to do our due diligence of like checking these maybe like the first two months and then before we just kind of just couldn't be more hands-off, so.

**Alexis Ruiz:** And it's actually checking the content, right?

**Alexis Ruiz:** Like, so they would be clicking on this, it would be these Google Doc links and they'd be reading through the content, right?

**Alexis Ruiz:** Because I think, yeah.

**Aida Knezevic:** Sorry, go ahead.

**Alexis Ruiz:** Sorry, was going to say that.

**Alexis Ruiz:** I think the other ones, it was just to review like how it looked on the actual site, right?

**Aida Knezevic:** Once it was staged.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** So like we, so the first time we staged the content in your CMS, we like to just ping the team to make sure we didn't like do anything wrong.

**Aida Knezevic:** But then from that point on, we just stage and publish.

**Aida Knezevic:** But this is more for the review.

**Aida Knezevic:** So primarily just to make sure that the product messaging is on point.

**Aida Knezevic:** It's correct.

**Aida Knezevic:** It's It's correct.

**Aida Knezevic:** correct.

**Aida Knezevic:** Yeah, like we want to.

**Aida Knezevic:** Avoid, like, any errors there.

**Alexis Ruiz:** Got it.

**Alexis Ruiz:** Okay.

**Aida Knezevic:** All right.

**Aida Knezevic:** I'll, let me just, Fung-Lin, I'm going to send you the link to the Slack thread where you can just find, like, last week's batch to make it easier for you.

**Aida Knezevic:** All right.

**Aida Knezevic:** Cool.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So, whenever we get the green light from you, can go ahead and publish those as well.

**Aida Knezevic:** I know that, so, Cody let us know last night that we do need thumbnail images for all of these blogs.

**Aida Knezevic:** We were under the impressions that we actually don't need them because you don't have any on your site.

**Aida Knezevic:** But when you send the link to someone, obviously, it needs to have an image.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** And the most recent blog also has the image.

**Alexis Ruiz:** Like, if you go to, like, the actual just blog page, the most recent blog will show the image as well.,のでVE Great,

**Fung-Lin Wu:** We do have like a Canva template that either we can give you guys access to probably.

**Alexis Ruiz:** Or I can create them.

**Alexis Ruiz:** Yeah, I create them easy.

**Fung-Lin Wu:** It takes like a minute.

**Alexis Ruiz:** You don't to get in a space where you're creating like 40 of these once we start scaling.

**Alexis Ruiz:** Yeah, that's true.

**Alexis Ruiz:** Okay, maybe we can ask Allison to give them access.

**Fung-Lin Wu:** would be, I think.

**Fung-Lin Wu:** What's easier?

**Aida Knezevic:** What we actually do is we can.

**Fung-Lin Wu:** Because I remember you guys created it.

**Aida Knezevic:** Yeah, because we can build this into our article generation pipeline.

**Aida Knezevic:** So where we create articles, the last step can be generate cover image.

**Aida Knezevic:** And we have a designer, Katya, who can literally copy this.

**Aida Knezevic:** Like copy the colors, the fonts.

**Aida Knezevic:** And this is like pretty simple because it uses like the text overlay with your logo.

**Aida Knezevic:** And then we can have like you can send us like what are the colors that you're using?

**Aida Knezevic:** And then she can just mimic that.

**Aida Knezevic:** And you don't have to use Canva.

**Aida Knezevic:** Canva.

**Fung-Lin Wu:** Yeah, Alexis, are you okay sharing?

**Fung-Lin Wu:** Because we have like, I can't remember, I think we have like four or three different color, and we try to rotate them.

**Alexis Ruiz:** It's yeah, it's like.

**Fung-Lin Wu:** And we rotate which one to use so that it's not just like one bland color on our site.

**Fung-Lin Wu:** So Alexis, can you maybe take screenshots and send it to Aida, and then that way you guys will know what to rotate between.

**Alexis Ruiz:** Yes, I could do that right now.

**Alexis Ruiz:** Yeah, I'll just download the templates so you guys can see what they look like.

**Aida Knezevic:** Yeah, that definitely works.

**Aida Knezevic:** So yeah, we'll set that up for you ASAP, and then we can like go back and like regenerate images for every single one of the blog posts that we've already delivered so that it's very quick to publish.

**Aida Knezevic:** Okay, great.

**Aida Knezevic:** and then for...

**Aida Knezevic:** Okay,

**Aida Knezevic:** So, the article that we refreshed, which is, what is an AI agent?

**Aida Knezevic:** I was wondering if it's possible to change the date so that it's updated.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** That's just important for Google and LLMs to be able to see that, like, what was the last date that it was updated.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** All right.

**Aida Knezevic:** And then, yeah.

**Aida Knezevic:** So, I am going to, right now, I am working on a summary of just phase one.

**Aida Knezevic:** So, what we've done so far, and it's also going to include, like, a breakdown of what we're planning to do for phase two.

**Aida Knezevic:** We're also working on a technical SEO audit for you.

**Aida Knezevic:** So, it's going to just include a list of any potential issues that we've found on your site that should be resolved to just boost your overall SEO and just, like, website performance.

**Aida Knezevic:** And, yeah.

**Aida Knezevic:** That's kind of the week seven, like, checkpoint that we're at right now.

**Fung-Lin Wu:** Yeah, I think so far we're really happy with it.

**Fung-Lin Wu:** Obviously, it's a lot of the hard part is, like, us reviewing the content, but we're hoping that's a short-term pain for our end.

**Fung-Lin Wu:** We don't use Airtable internally, so it's really hard for us to go between, like, Airtable and Notion because we don't use either.

**Fung-Lin Wu:** Right.

**Fung-Lin Wu:** So, but again, I think for us, I'm hoping this is more like a short-term pain since the goal eventually is, like, we won't, we can just, we just have to focus more on the reporting side and outcome.

**Aida Knezevic:** Yeah, exactly.

**Aida Knezevic:** Now, the, what are you using internally?

**Fung-Lin Wu:** We use Asana, and then we use Asana, and then, Asana for, yeah, Asana Asana, for Airtable, and then for Notion, we use Google Docs.

**Alexis Ruiz:** Yeah, got it.

**Aida Knezevic:** Got it.

**Aida Knezevic:** Yeah, I think with, um...

**Aida Knezevic:** So where we're at right now is that the reviews during the sprint, we do more detailed reviews because that just allows us to catch any potential issues.

**Aida Knezevic:** And then once we're really out of the sprint, then we could get to publishing very consistently and the reviews don't have to be extensive.

**Aida Knezevic:** You can just kind of give it like a quick look before it's published on your site.

**Aida Knezevic:** And I mean, the team that's been like generating your content, they've really been like taking into account all of the feedback and like just constantly like improving the article generation pipeline.

**Aida Knezevic:** So I think, you know, our goal really is to kind of like make sure you're not spending a ton of time doing these reviews.

**Aida Knezevic:** And my understanding is that the feedback from Allison and Cody hasn't been like super, super extensive.

**Aida Knezevic:** So I'm like just happy to know that like they don't have to spend a lot of time just reviewing this.

**Fung-Lin Wu:** Yeah, same.

**Fung-Lin Wu:** I think for us, it's just like, obviously right now for us, it's just like using a different tool and getting your views in.

**Fung-Lin Wu:** But again, I think this is, for us, like we're hoping once, because our PMM is pretty tight on resources, so that's always been hard for getting the, and that was our struggle when we had an SEO agency was really like the internal PMM review side.

**Fung-Lin Wu:** But when I spoke with Cody, I think the group, we both had an understanding that this is more just like an eight-week sprint, like an eight-week sprint, and then we're hoping that PMM can be removed from the process.

**Fung-Lin Wu:** Yeah, absolutely.

**Fung-Lin Wu:** So yeah, I think we're happy.

**Fung-Lin Wu:** So I think for answers, we're happy with this partnership so far.

**Aida Knezevic:** Cool.

**Reet Mand:** I'm happy to hear that.

**Reet Mand:** Lynn, I wonder if there are some, if some of these assets who are like deeper technical, I don't know how technical we are going to get in these, but if it is, like I wonder if we can, if PMMs are busy, then we can ask like somebody from the essay team to just give a look to make sure.

**Reet Mand:** It's technically accurate, you know?

**Fung-Lin Wu:** Yeah, for sure.

**Fung-Lin Wu:** think we've also, Cody's also been handing some of them off to the technical marketing team, but the original, like, I think when Megan's original goal was because the goal is to launch up to 40 a quarter, it's impossible internally to scale at that level.

**Fung-Lin Wu:** So I think once we feel good, generally speaking, about that technical accuracy in the first two months, we'd want to be as hands-off.

**Fung-Lin Wu:** But yeah, I think if, unless it's, like, super technical, then we would definitely get someone involved to review.

**Reet Mand:** Yeah.

**Reet Mand:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** I don't, I think those are all of the updates that we had for you.

**Erik O'Brien:** Erik, was there anything else on your end?

**Erik O'Brien:** No, I think from a production standpoint, that covers everything.

**Erik O'Brien:** I think just for, I know we pinged about it in the channel, but for phase two, we just need kind of a...

**Erik O'Brien:** Verbal or written agreement that you guys are kind of in line with going forward with us.

**Erik O'Brien:** We do have this eight-week period of kind of, we call it dating, making sure that you guys are happy with the production and making sure that kind of the workflow works for you.

**Erik O'Brien:** So I think as long as everything looks good there, we'll just need kind of confirmation on moving forward to Phase 2.

**Fung-Lin Wu:** Sorry, I'm slacking you guys right now with the written verbal confirmation.

**Erik O'Brien:** Wonderful.

**Aida Knezevic:** Cool.

**Fung-Lin Wu:** Okay, I just left it, so we're good to go.

**Aida Knezevic:** Okay, thank you.

**Aida Knezevic:** All right, and I just wanted to, oh, hi, Tyler.

**Tyler Pavlas:** No, hey there.

**Tyler Pavlas:** Just wanted to say hello to the team, and Reet, nice to meet you.

**Tyler Pavlas:** I'm on, you know, the sales team at GrowthX, so if you have any questions about the commercials or, you know, what you get out of the partnership, just let us know.

**Tyler Pavlas:** But I'll stay out of the team's way here and just an extra resource if you need me.

**Tyler Pavlas:** All right.

**Tyler Pavlas:** All All

**Aida Knezevic:** Awesome.

**Aida Knezevic:** All right.

**Aida Knezevic:** Anything else, Team, that you need help with or wanted to discuss?

**Fung-Lin Wu:** I don't think so.

**Aida Knezevic:** No?

**Aida Knezevic:** All right.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** I just, before we jump, I wanted to kind of show you just one thing that the team has been kind of experimenting with for your content.

**Aida Knezevic:** Because, you know, from our conversation with Allison, like, we know that it's, like, really important to kind of hit the right tone.

**Aida Knezevic:** And in our artifacts, we, this is like your workspace.

**Aida Knezevic:** And we created, like, a custom artifact that's called Examples of Good.

**Aida Knezevic:** And it's just two articles that capture your tone and are good examples of the kind of content that we want to emulate.

**Aida Knezevic:** And it's just, like, the articles that you, like, you know, that hit the mark with Allison.

**Aida Knezevic:** And then during the content generation process, towards...

**Aida Knezevic:** Once the article is drafted, AI can compare the draft to these good examples and grade the draft and find areas for improvement.

**Aida Knezevic:** And this is just one example of a custom artifact that we can generate for you, but anything that comes from the PMM team, it's just important that any feedback from them is communicated to us so that we can build a custom artifact here for just any repetitive feedback that they have for us or anything that's super important for us to bring up in content.

**Aida Knezevic:** There really is no, there's nothing that, I feel like it's too custom here in terms of just customizing the workflow to make sure that the articles look the way you want them to look.

**Aida Knezevic:** And we're quite flexible in building these and adding them on an ad hoc basis.

**Fung-Lin Wu:** Got it.

**Fung-Lin Wu:** How, what's the best way for our PMMs or technical marketers to share?

**Fung-Lin Wu:** Share artifacts?

**Fung-Lin Wu:** Should I do it through Slack?

**Fung-Lin Wu:** Should I do it through?

**Aida Knezevic:** Typically, we generate the artifacts.

**Aida Knezevic:** However, anything that they want to share with us, they can just Slack us.

**Fung-Lin Wu:** We'll just give you any docs as we have updated information.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah, exactly.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** And then we also have in the workflow projects, we have the agentic article generation here.

**Aida Knezevic:** And then we can, like, add, like, we have already have the workflow for generating cover images, but we just need to update the backend so that it looks like your Canva images.

**Aida Knezevic:** So that's what we're going to do.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Awesome.

**Aida Knezevic:** Well, I think those are all the updates.

**Fung-Lin Wu:** In the meantime, just send me a message on Slack if you have any other questions.

**Fung-Lin Wu:** Sounds good.

**Aida Knezevic:** Thank you.

**Aida Knezevic:** Thank you.

**Aida Knezevic:** I'll see you next week.

**Fung-Lin Wu:** Bye-bye.

**Fung-Lin Wu:** Bye.

**Fung-Lin Wu:** Bye-bye.
