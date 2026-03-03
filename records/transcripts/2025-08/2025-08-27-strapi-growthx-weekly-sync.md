# Strapi<>GrowthX Weekly Sync

<metadata>
date: 2025-08-27
time: 16:30 UTC
duration: 26 minutes
organizer: Vivek Shankar
participants: Vivek Shankar, Golzar Yaghoubpour, Victor Coisne, Paul Bratslavsky, Theodore Onyejiaku
fathom_recording_id: 83311630
fathom_url: https://fathom.video/calls/391031634
share_url: https://fathom.video/share/USP6vBgq2ZfWuwCYHe5smFPLjVxkfJrj
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

Strapi and GrowthX discussed content strategy updates, performance tracking, and technical delays. The team is refreshing content monthly (up from quarterly) due to increased LLM surfacing, launched a new comparison pages automation pipeline starting next week, and delayed image generation to early September due to adapting images to Strapi brand guidelines and other client priorities. Victor requested top 10 performing content visibility and explicit metrics on posts/pages published weekly.

---

## Context

Strapi is a headless CMS platform and a longstanding content marketing client of GrowthX, generating substantial engagement through technical blog content and documentation. This weekly sync is a standing meeting between Strapi's content leadership (Victor, Theodore, Golzar, Paul) and GrowthX's delivery team (Vivek) to align on content performance, refresh strategy, and automation improvements. The relationship centers on producing high-quality, SEO-optimized content targeting developers and architects evaluating CMS solutions, with a focus on Next.js and React integration content that performs best.

---

## Relevance

- **To GrowthX Delivery:** Monthly content refresh cycles are now standard practice (vs. quarterly) to combat LLM content surfacing and maintain rankings. Automation pipelines for comparison pages and staging workflows are reducing manual workload. Image generation tool selection and implementation has become a multi-week engineering challenge requiring trade-offs between internal infographic generation, Napkin AI (external service), and custom Strapi brand compliance — decisions here will inform other client work.

- **To GrowthX Business Development:** Strapi is actively expanding content depth (12 new pieces in pipeline per week, 6-7 moving to staging weekly). Account momentum is strong with faster content review cycles and increasing volume. However, visibility into top-performing content and conversion metrics is limited — tracking is currently funnel-based rather than click-event-based, creating reporting blind spots Strapi is pushing to close.

- **To CheckThat / AEO:** Strapi is explicitly monitoring LLM content surfacing and adjusting strategy accordingly. Comparison pages launching next week could be a strong use case for visibility testing. Competitor query-level data remains inaccessible via Google, forcing brute-force prompt testing — this is a CheckThat research opportunity.

---

## Overview

- Content refresh strategy shifting to monthly updates due to LLM content surfacing
- New comparison pages automation pipeline ready; implementation starts next week
- Image generation workflow delayed; ETA early September
- Performance tracking to focus on top 10 performing content pieces for optimization

---

## Key Topics

### Content Refresh and New Content Updates

- New format: Links to Strapi documentation added to tops of refreshed articles
- Refreshing ~4 posts/week; 6-7 new blog posts moved to staging weekly
- Shifting to monthly content refreshes (previously quarterly) due to LLM content surfacing
- 12 new pieces in pipeline for this week

### Technical Updates

- Staging automation in final stages; testing with this week's content
- Medium distribution credentials need updating (Victor to provide)
- Image generation workflow delayed due to adapting to Strapi guidelines and engineering prioritization

### Performance Tracking

- Victor requested top 10 performing content pieces for optimization
- Next.js and React integrations pages performing best
- Conversion events stable; tracked for overall website, not specific to GrowthX URLs
- Anomalous traffic spike observed; cause unclear due to limited Google query data

### Content Categorization and Tracking

- Using Airtable agent to categorize content into clusters
- Tracking content cohorts in Looker for performance analysis

### CTA and Conversion Tracking

- Inline CTA clicks tracked through funnel exploration report, not as specific events
- Team to review conversion trends monthly

---

## Action Items

**Victor Coisne (Strapi)**
- Provide updated Medium login credentials to Vivek for distribution automation

**Theodore Onyejiaku (Strapi)**
- Share Slack thread with comments on React.js overview and cloud providers content to Vivek

**Vivek Shankar (GrowthX)**
- Add number of posts/pages published weekly to performance reports
- Make top 10 performing content pieces explicit in reporting
- Adjust Looker dashboard to filter out pre-existing integration pages (not net-new content) from performance analysis
- Inform engineering team not to delete staged content during automation tests

---

## Transcript

**Theodore Onyejiaku:** Hi Vivek, good day, can you hear me?

**Vivek Shankar:** I can hear you, yeah, you seem to be freezing a little bit, but I can hear you, yes.

**Vivek Shankar:** Okay, how about now?

**Vivek Shankar:** Yeah, it's better.

**Vivek Shankar:** Hello everybody, I'm going to check my sounds.

**Paul Bratslavsky:** Hi Paul.

**Paul Bratslavsky:** Sorry.

**Paul Bratslavsky:** Hello, hello.

**Paul Bratslavsky:** Hey Victor, how are you?

**Victor Coisne:** I'm good, how are you doing?

**Victor Coisne:** How was your vacation?

**Paul Bratslavsky:** Yeah, was great, that's great.

**Victor Coisne:** Good to be back in the US.

**Paul Bratslavsky:** Yeah, nice.

**Vivek Shankar:** So I think Mara's not going to be joining today, she's had an emergency actually. But yeah, we can get started. Let me share my screen. And Victor, we'll just walk through your questions that you left in motion one by one.

**Vivek Shankar:** All right. Just a quick update. So for the refreshes, we're proceeding as planned for the new format. So just for more context, the new format, as we discussed last week and a couple weeks back, was basically, instead of refreshing the full article, we're adding links on top, directing people to Strapi's new documentation or relevant documentation. That's basically how we're proceeding with it.

**Vivek Shankar:** We're also planning refreshes of older content that we generated — these are regular blogs, not technically oriented blogs that were proving to be a bit of a hiccup. So we'll start doing that from next week onwards for the older GrowthX content. For new content, we are on track, nothing major over there.

**Vivek Shankar:** The comparison pages — we built out the automation pipeline for that, so that will start next week, and you'll be seeing those for review.

**Vivek Shankar:** Regarding the image generation workflow, Victor, one of the issues that we had was adapting the images to Strapi guidelines. One of the stumbling blocks was that we have an internal flow that generates infographics based on the text. The problem is that turning those infographics into visual elements — kind of like how Napkin works, where you highlight text and it gives you an image based on the theme — a lot of the text elements that were showing up were a bit problematic, so we had to devote more engineering resources to this.

**Vivek Shankar:** We're trying to push it through GPT, et cetera, because the image generation firepower is a bit more demanding at the moment. So we're experimenting with that. We should have something over the next couple of weeks, so apologies for the delay there.

**Vivek Shankar:** Generally, what's also been happening is that we've been prioritizing a lot of workflows across many clients. There's been a situation where we've had to decide which is the most mission critical from a product perspective. So that's why image generation, unfortunately, it got deprioritized a little bit. But we have been pushing it with our engineering team, and we should see something there over the next couple of weeks. Any questions about that I can answer?

**Victor Coisne:** Yeah, I mean, we could just have a bit of a clearer ETA than the next couple of weeks. Can we expect it in early September?

**Vivek Shankar:** That's the latest that we've heard. But if that changes, I will certainly let you know.

**Theodore Onyejiaku:** I was going to mention Napkin AI, which you already mentioned. Like, I tried it out, and it's really great. I wanted to suggest it, but I think you already have an idea of it.

**Vivek Shankar:** So for one of our other clients, we were doing this a few months back. We were using Napkin externally to basically generate images based on posts. And these were inline images. And what we would then do is we would send it to their graphic designer. They had one in-house. And this person would change the image from Napkin per their brand guidelines. So my understanding is that would be too much of a hurdle for Strapi. So that's why we're trying to automate that as well. And that's kind of where the challenges come in.

**Vivek Shankar:** Regarding the staging automation, apologies for the random pages showing up in draft yesterday. But we are in the final stages of that, and that should be done as of today. So actually, for this week, all of the content that we are publishing, we'll be testing it through the automation.

**Vivek Shankar:** The Medium distribution, Theo, just wanted to check with you the username and password you'd sent. I passed it on to Engineering, but we couldn't log in with it. Just wanted to check if that was the correct one or if there is another ID and password.

**Theodore Onyejiaku:** I guess it must have changed. But I think Victor could help you with that because I shared with you the one we could use to sign into Twitter, which perhaps must have changed for Medium. So I think you should ask Victor about that, now that he's around.

**Vivek Shankar:** I will follow up after the call and add it in there. So moving on to the performance report, regarding Victor, the number of posts and pages published, yes, I will add that to the updates following next week. Generally, what we've been doing is we've been refreshing about four posts per week. And we've been publishing, or rather moving into staging, net new, about six to seven new blog posts for your review. And then in terms of publishing, I think it depends on how soon CEO gets through everything. So there's no stable number there, but we can certainly update it based on whatever happens moving forward.

**Theodore Onyejiaku:** Yeah, like, as of now, we have no draft, no content in the draft, so if you could increase it, it would be fine because I noticed the volume kind of decreased. But it would be great if we could have more, because I think things are getting better now — the review is kind of faster, and based on the suggestions I've given so far, they've been incorporated. So our volume will increase, since our focus is more on volume.

**Vivek Shankar:** I think there are actually a few URLs for your review. I can just open the Airtable real quick. There were a few older posts that I noticed are still marked as under Strapi review. So we have like 13 posts — like "Best Content Management Systems," "Setting Up Multi-Language Strapi," and all of these. We've left the staging links, but yeah, go ahead.

**Theodore Onyejiaku:** Yeah, this content — when Sydney was around, I already brought it up several times for your review because I left some suggestions. Perhaps if you look at the React.js overview or the cloud providers content, there were some comments I left, which I don't know if they have been addressed. I can share you the link.

**Vivek Shankar:** Okay, yeah, please go ahead. Did you leave the comments in Airtable or somewhere else?

**Theodore Onyejiaku:** Yeah, on Slack, there's a thread for it.

**Vivek Shankar:** Okay, yeah, if you could please just CC me on those because I think it must have slipped during the transition. My apologies, but we'll adjust those real quick. But these ones here, like "Solid Design" and "Omnichannel," I think these are new ones because I know Timmy generated these. Yeah, Timmy and Usman were working on this last week. So you'll see more coming in this week — we have about 12 in the pipeline for this week. So you'll be seeing all of those come in. And yeah, that volume should increase.

**Victor Coisne:** So Vivek, in terms of performance, in addition to getting a sense of volume, I think what would be helpful is understanding maybe the top 10 content that's bringing most of the sessions. We get a sense of which ones are really hitting the spot so we keep making those content better and better. I think that's really important to me. If we see we're getting a lot of traffic, some keywords are really ranking, and we want to make sure we keep investing into making that content better so we stay at the top. I think that's the first question, and maybe getting an idea of when new content hits a bit of a breakthrough and we see they are getting picked up. So just so we have those on our radar and we can keep looking for ways to make it better. What are some additional trusted sources that we could maybe interview and kind of add to the credibility of the post?

**Vivek Shankar:** Totally hear you on that. That is part of the internal reviews that I do usually. As you can see on this page here, the data is in Looker, and I use these dashboards basically for my analysis. I can certainly make it far more explicit in terms of the reporting itself so that you have a view into it. But basically, this table over here lists the performance of pretty much every blog post. And this is for your overall website as well. So if you just uncheck non-GrowthX URLs, it shows the ones that we produced. If you check it, it shows performance for your entire website. So it's pretty versatile in that sense.

**Vivek Shankar:** Generally, I think I mentioned this a couple of weeks back, the Next.js and React integrations pages are the best performing, but then we have some of these as well that have performed quite well over the past few months. And what we do generally, to your point about looking to enrich content, is given the way content is being surfaced in LLMs these days, we're prioritizing refreshes on a more frequent basis. So previously, we prioritized refreshes every three months or so, but now we're actually looking at refreshes every month.

**Vivek Shankar:** So something that was published that was maybe even refreshed last month, we're again looking to refresh it this month and so on. So that's one of the reasons why we're prioritizing the new blog content that we created both recently and a few months ago. We're looking to refresh that as well, not just the older content that had been flagged by Sydney before the transition.

**Vivek Shankar:** With the enrichment itself, we look at a few things. We're looking at, first of all, if the content itself could use an updating in terms of competitor moves. That's something we look at. Scrunch data, right now, doesn't give us full visibility into which competitor is showing up exactly for which query. That is just the nature of the space at the moment because the LLMs don't share that data. So it's kind of very brute force right now — we just have to prompt as much as possible and see what comes.

**Vivek Shankar:** But that data is certainly something we are looking at on a more frequent basis. So say, for example, if a competitor shows up for a particular query that we are interested in tracking and our presence has dipped, we certainly go back and we refresh the content, make sure that we are associating ourselves well with that particular query. So there's a lot of things in motion over there because that's the nature of the space. But I just want to let you know that it is something we're looking at and tracking as well.

**Victor Coisne:** One quick note as well on the top performing content. I see the integration Next.js and React and AWS. I'm not entirely sure this makes sense to include. I mean, I may be wrong, but I feel like those were like content that was mostly written by Paul and Theo. So I'm not sure to what extent it makes sense to include them here because I think it might be making the data a bit flooded.

**Vivek Shankar:** I think we included this because based on what Sydney told me, we were interested in tracking integrations. We can always filter these out. It's not that much of an issue, really. So we can certainly filter it just for, say, the blog URLs, and remove them.

**Victor Coisne:** I think it maybe makes sense too for the ones that were created from scratch, like the net new ones. I think it makes sense to include, but for the ones that were already existing, I think it's a bit misleading because those pages were already ranking and already bringing a lot of traffic.

**Vivek Shankar:** This is one that needs some customization in Looker. We can certainly do it. But yeah, for sure. Generally speaking, we can certainly pull that data in. Also, just want to point out, we are tracking the content cohorts as well. On the front end, within Strapi CMS, we are categorizing everything as ecosystem, so that it shows up below the fold. But generally, on our end, we're running that agent that we have in Airtable that's been there for a while, and we're categorizing it, and we're tracking everything over here. So generally, we're looking at quite a lot of data, and that's where the content recommendations as well as the refresh plans are coming from.

**Vivek Shankar:** Just the non-branded impression source of the spike — we're not quite sure, to be honest. It was a very, very odd spike. I can show you once this thing filters. But let me go back a bit to October. This will take a while to sort of come through because Looker is generally a little slow.

**Vivek Shankar:** Generally, the spike itself, we're not quite sure what happened. There was just a massive spike, and then it fell back down. It looks like an anomaly. We weren't able to locate the reason for it. But yeah, it was just a very odd thing because one of the reasons we're not able to locate it is because Google does not share the query level volume data with us. So it's all very indicative. We're not quite able to pin down exactly what happened.

**Vivek Shankar:** The conversion events, to answer your question, this is for the overall website. There's no way of isolating conversions just from GrowthX URLs because these events are not tied to our particular URLs. So this is for the overall website from organic channels. And this past week, we saw an increase in it. But generally speaking, we're not seeing massive swings in conversion, either up or down. It is sort of within a certain range, much like how overall performance is as well.

**Vivek Shankar:** And that was the reason why we recommended last week that we can certainly start prioritizing content where we have a bit of a gap to competitors. So that's what the new topics were, which CEO has reviewed. So that's the plan essentially moving forward to prioritize that.

**Victor Coisne:** So a question on that, and maybe that's a bit of a question for Golzar as well — I know we integrated inline banners. Do we have dedicated events for that, like kind of tagging it as a growthx inline CTA event, so that way we can track? Because those ones are like the ones mostly from the top nav.

**Golzar Yaghoubpour:** We don't have a dedicated event click per se on the integration pages. The way I look at conversion is in HubSpot, on the form submissions. Because the way the inline CTA works, we don't have like a dedicated event click, but we have it in a funnel exploration report. And I remember investigating this a while ago, and Maxine said that it was kind of due to however way the inline code works. So anyway, in summary, we can look at it from a funnel standpoint, like an exploration report, but not like a specific click. And the reason for that is because it filters on the name of the button, not the name of the event.

**Victor Coisne:** Okay, I got it. Yeah, I think it might be good for us internally to review on a monthly basis — okay, like, are we seeing an upward trend on overall conversion of those posts? And like, is it moving in the right direction? And are we doing everything to make sure there's some CTA, so it's not just like a touch point in the prospect and sales journey, but more like also a top-of-the-funnel conversion event. So yeah, I guess we can talk about it separately.

**Vivek Shankar:** Yeah, so regarding your question, Victor, cohort is just the content cluster, not the keyword cluster. So basically, as I mentioned, we are running that agent in Airtable, figuring out which is the appropriate content cluster for each URL we're creating. And based on that, we're tracking everything in Looker. So yeah, coming back to the non-branded, there's a couple spikes here, as we can see. Like, there's this massive spike in December, which happened right around the new year, actually. But we know where this one is coming from.

**Victor Coisne:** It was like a spam on our forum.

**Vivek Shankar:** Yeah, and then I'm referring to this particular spike over here, which took off to like 20k impressions and then fell. The number of URL clicks is not indicative because Google doesn't give us that data on a query level. But yeah, you can see some of these pages kind of spiked. It was basically the homepage that spiked the most by the looks of it. And yeah, we weren't able to isolate as to why this happened. There were like some forum links showing up over here. But yeah, that's kind of where it's at.

**Vivek Shankar:** So yeah, it seems to have subsided and we're coming back down to regular levels over here. But yeah, obviously the graph looks flat mainly because of this anomaly, but the reality is we have been sort of steadily increasing and we're seeing good performance over there. So yeah, that's kind of the update we had for this week. Obviously, we're going to continue prioritizing those two topics based on reducing the gaps, et cetera. The comparison pages should help as well with LLM visibility. And yeah, we should be seeing that come through next week.

**Victor Coisne:** I may have missed the update from when I was off, but I think you have access to Octave now. Were you able to pull the data in there as a replacement to your knowledge base artifacts?

**Vivek Shankar:** We did pull it in manually at this point. The automation had a bit of a hitch. As I mentioned, we had to prioritize a lot of requests that just came in from a bunch of clients. And because of that, the Octave integration was kind of deemed as a one-off thing because nobody else is using it. So for now, we decided just to do it manually. As and when the backlog clears, we'll prioritize that and get that automated.

**Theodore Onyejiaku:** I wanted to ask about the engineering team automation on the publishing of blog posts. Like, the tests that are being carried out — have they been able to fix it? Because I noticed when they publish posts from the workflow, it gets reflected on our blog. So what's the status? And then also, when they delete a blog post, I think it's best they allow us do it internally, because they might mistakenly delete a blog post from us.

**Vivek Shankar:** So my understanding is they are not publishing it correctly. There was a bit of a technical challenge in terms of figuring out whether something is being staged versus something is being published. So my understanding is they have fixed it. So now the blog post will only be staged and not published. And regarding the deletion, they were deleting it from the CMS, but there was something happening with Algolia. So they were deleting it from the CMS, but Algolia was preserving it, which is why it was still being preserved on your website.

**Vivek Shankar:** But in terms of deleting it, I don't think we'll be running any more tests. They'll just be the ones that basically me and Usman — who is filling in for Timmy this week — will be running those tests this week, so you shouldn't see anything else. But I will pass on the message to the developers that, yeah, if they stage it, don't delete it.

**Theodore Onyejiaku:** Thank you.

**Vivek Shankar:** So that was it for this week. Any other questions, anything else I can answer?

**Vivek Shankar:** All right, thanks, everyone. I'll see you on Slack.

**Victor Coisne:** Thanks, everyone.

**Paul Bratslavsky:** Bye.

**Golzar Yaghoubpour:** Bye.
