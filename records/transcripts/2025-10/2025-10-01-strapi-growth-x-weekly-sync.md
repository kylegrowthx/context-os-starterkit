# Strapi <> Growth X -  Weekly Sync

<metadata>
date: 2025-10-01
time: 16:30 UTC
duration: 27 minutes
organizer: mara@growthx.ai
participants: Victor Coisne, Golzar Yaghoubpour, Paul Bratslavsky, Theodore Kelechukwu Onyejiaku, Vivek Shankar, Mara Leighton
fathom_recording_id: 91165760
fathom_url: https://fathom.video/calls/427049799
share_url: https://fathom.video/share/YHCmNxhk8MeDJSE1ng_xrfQ39sYehMCx
source: fathom
enriched_on: 2026-03-02 10:30 UTC
</metadata>

---

## Summary

Strapi and GrowthX aligned on shifting from content refresh to sustained production (9 articles this week, 7-8 weekly going forward) while addressing workflow bottlenecks in images and Medium formatting. Vivek shared performance updates showing overall stability despite Google algorithm changes affecting GA4/GSC accuracy, strong LLM visibility for Strapi across most prompt clusters, and identified opportunity areas in security and database CMS content. The team discussed three new automation initiatives — social post creation, content gap discovery via community listening, and trending content curation — and tasked engineering with assessing feasibility and timelines for each.

---

## Context

GrowthX is a content marketing agency working with Strapi, a leading open-source headless CMS platform. This was a weekly sync between the Strapi team (Victor Coisne, Golzar Yaghoubpour, Paul Bratslavsky, Theodore Kelechukwu Onyejiaku) and the GrowthX delivery team (Vivek Shankar, Mara Leighton) to align on content strategy execution, performance tracking, and technical automation improvements. The meeting occurred on Strapi's 10th anniversary, and the team used it to review recent content production milestones and plan the next phase of content initiatives — moving from completing a refresh cycle into ongoing performance optimization and new content creation. This is part of a broader engagement where GrowthX manages content and CheckThat visibility strategy for Strapi's developer audience.

---

## Relevance

**To GrowthX Delivery:**
- Content production is scaling from refresh cycle to ongoing output: 9 articles this week, stabilizing to 7-8 weekly. Validates sustainable production workflow.
- Technical bottleneck identified: image workflow requires engineering focus on text-heavy/technical images; Medium workflow H2/H3 formatting issue near resolution.
- Integration pages workflow delayed due to competing engineering priorities but expected within sprint — demonstrates need for clearer priority alignment.
- Three new automation requests signal expansion of scope: social post creation, content gap discovery, trending content curation — all require engineering assessment and resourcing decisions.

**To CheckThat:**
- Strapi shows strong LLM visibility across most prompt clusters but has opportunity gaps in two areas: "security best practices for CMS" and "database options for content management." These represent concrete content gaps to address.
- Slight increase in LLM-referred traffic observed; GPT remains top referrer. Citation rate at 6% is lower than expected but competitor rates similarly low — suggests either strong query focus or LLM variability.
- Content strategy linked to ICP (ideal customer profile) — team is cross-referencing trending topics against Strapi's ICP to determine content angles, indicating mature approach to audience-first strategy.

**To GrowthX Business Development:**
- Account showing healthy engagement and multi-layered requests signal strong partnership health and potential for scope expansion.
- HubSpot access issue flagged (expired link/no dashboard visibility) — should be resolved quickly to maintain tracking integrity; Golzar awaiting Tori's response.
- Strapi's willingness to invest in automation (four separate requests) and collaborative problem-solving indicates receptiveness to higher-value service offerings and potential upsell opportunity for workflow optimization consulting.

---

## Overview

- Content refresh complete; shifting to performance updates + new content (9 articles this week, 7-8 weekly thereafter)
- Medium workflow nearly finished; integration pages workflow in progress
- Performance metrics steady but unreliable due to Google update
- New automation requests: social post creation, content gap discovery, trending content curation

---

## Key Topics

### Content Production & Workflow Updates

  - 5 refreshed pages delivered last week, completing Sydney's earmarked content
  - 9 articles scheduled this week; 7-8 weekly moving forward
  - Action item database updated
  - Image workflow still in progress; engineering addressing text-heavy/technical images
  - Medium workflow updates nearly complete (H3 vs H2 formatting issue remaining)
  - Integration pages workflow (metatitles update) delayed but expected within next sprint

### Performance Metrics

  - Google update causing data inconsistencies across GA4, GSC, etc.
  - Overall sessions slightly dipped; engaged sessions stable
  - Conversion events declined slightly but remain at healthy levels
  - Headless CMS and ecosystem cohorts dipped in sessions but improved engagement
  - Integration pages performing well

### LLM Traffic & Visibility

  - Slight increase in LLM-referred sessions
  - GPT remains a top referrer
  - Strapi showing strong presence across most prompt clusters
  - Areas for improvement: security best practices for CMS, database options for content management

### Social Post Automation Request

  - Automated process for creating social posts from published Strapi content (excluding GrowthX content)
  - Platforms: Twitter, LinkedIn (primary), Facebook, Instagram
  - Proposed workflow: content publish trigger → AI-generated post + image → UTM link → save to Google Sheets/direct to HubSpot
  - Engineering team to assess feasibility and provide ETA

### Content Gap Discovery Automation

  - Leverage social listening (Reddit, Twitter) and Kappa AI for community questions
  - Automate process to identify potential topics for GrowthX articles
  - Engineering to explore implementation after receiving list of desired sources

### Trending Content Curation Agent

  - Proposed automated process to create blog posts on trending web dev topics
  - Concept: "Top 5 things" style content based on trending discussions
  - Need to define sources and trending metrics for effective implementation

---

## Action Items

**Vivek Shankar (GrowthX)**
- Share results of completed Medium workflow updates this week
- Take social post automation request to engineering team; get ETA for implementation (Twitter, LinkedIn, Facebook, Instagram)

**Golzar Yaghoubpour (Strapi)**
- Follow up with Tori re: HubSpot access response; decide next steps based on reply

**Paul Bratslavsky (Strapi)**
- Send Vivek list of sources to monitor for content gap discovery (social, Kappa, GitHub)
- Follow up on Slack re: research agent for content curation; provide YouTube channels & email subscriptions as potential sources

---

## Transcript
**Victor Coisne:** Hey, Mara, how are you?

**Mara Leighton:** How are you?

**Mara Leighton:** I'm doing well.

**Victor Coisne:** Awesome.

**Victor Coisne:** Hey, hello, everyone.

**Victor Coisne:** Can you hear me?

**Victor Coisne:** Yeah.

**Vivek Shankar:** Yeah, okay, cool.

**Mara Leighton:** All right.

**Vivek Shankar:** It was a bit thrown off because it used to be Google Meet and now it's Zoom, so.

**Mara Leighton:** Oh, yeah.

**Mara Leighton:** That happened while you were out.

**Mara Leighton:** That makes sense.

**Mara Leighton:** Yeah, we were saying it's throwing everyone for a loop.

**Mara Leighton:** But, yeah, it seems like all of our calls are now on Zoom, which I kind of prefer, but.

**Vivek Shankar:** Yeah.

**Victor Coisne:** Paul, you look scary.

**Paul Bratslavsky:** I don't know what's happening to my camera. Zoom doesn't play nice with my camera. But it's like, hey, actually, I'm scared myself at this point.

**Mara Leighton:** I like the drama. Let me just switch to my computer.

**Paul Bratslavsky:** There you go. I know that's very dramatic. I used the MacBook Pro camera.

**Mara Leighton:** That's so funny.

**Vivek Shankar:** I think, are we waiting on Theo?

**Victor Coisne:** I think we should be.

**Theodore Kelechukwu Onyejiaku:** Hi, everyone.

**Theodore Kelechukwu Onyejiaku:** Sorry for coming late.

**Mara Leighton:** No worries.

**Theodore Kelechukwu Onyejiaku:** Thank you.

**Mara Leighton:** Oh, also, I think we saw, is it Strappy's 10th anniversary today?

**Victor Coisne:** It is, yeah.

**Mara Leighton:** Happy Huge.

**Mara Leighton:** Yeah.

**Mara Leighton:** Cool.

**Mara Leighton:** Are you doing anything to celebrate?

**Victor Coisne:** Yeah, just have a, just published a fun blog post and being like a challenge for people to engage on so far.

**Mara Leighton:** Nice.

**Mara Leighton:** Cool.

**Mara Leighton:** I guess you're all in different places, so like a giant cake in the break room doesn't make as much sense, but cool.

**Mara Leighton:** Awesome.

**Mara Leighton:** Awesome.

**Mara Leighton:** Well, also, I know that we'll jump in.

**Mara Leighton:** Sorry, Vivek, also just to close the loop on something that I made.

**Mara Leighton:** You're probably up to date on, but Victor responded to your comment on the images, so shouldn't be good there.

**Mara Leighton:** Thank you for sharing them.

**Mara Leighton:** We've shared them with engineering.

**Mara Leighton:** Vivek, this was on the strappy team's design notion.

**Mara Leighton:** I'll share with you just so you have like full visibility, but no action needed there, but just so you know what the invite is.

**Mara Leighton:** And that's it for me.

**Mara Leighton:** Just jump in.

**Vivek Shankar:** All right.

**Vivek Shankar:** Let me share my screen.

**Vivek Shankar:** Sorry, I'm figuring out Zoom.

**Vivek Shankar:** Okay, there we go.

**Vivek Shankar:** Hopefully everyone can see.

**Vivek Shankar:** Can everybody see my screen?

**Mara Leighton:** Yeah, you're good.

**Vivek Shankar:** Okay, cool.

**Vivek Shankar:** I'm just worried.

**Vivek Shankar:** All right, just some quick updates.

**Vivek Shankar:** So we delivered five refreshed pages last week.

**Vivek Shankar:** And if I'm not mistaken, I think we're at the end of the pages that needed.

**Vivek Shankar:** cool.

**Vivek Shankar:** we're at

**Vivek Shankar:** Refreshing for content that Sydney had earmarked.

**Vivek Shankar:** So from this week and next week forward, we'll basically be refreshing old blog content that we have delivered.

**Vivek Shankar:** Basically refreshing them for performance, et cetera, and producing new content as well.

**Vivek Shankar:** So that's why we have nine articles scheduled for this week.

**Vivek Shankar:** And from next week on, it will be around seven or eight.

**Vivek Shankar:** Just a quick update on all the workflows.

**Vivek Shankar:** So we updated the action item database, and then we're still working on the image and workflow.

**Vivek Shankar:** We hope to have updates over there soon.

**Vivek Shankar:** We've shared the sort of reference images with our engineering team.

**Vivek Shankar:** I think the sticking point was some of the more text-heavy and technical images.

**Vivek Shankar:** That's what we heard from last, but we hope to have a more detailed update soon.

**Vivek Shankar:** The medium workflow updates are almost complete.

**Vivek Shankar:** There's only, I think, one outstanding issue, which we...

**Vivek Shankar:** tested it today, actually.

**Vivek Shankar:** All the headers are being formatted as H3s instead of H2s versus H3s, so it seems like a pretty small thing.

**Vivek Shankar:** We should be good to go on there by the end of this week, almost certainly.

**Vivek Shankar:** And then the integration pages workflow where updating all the metatitles, etc., engineering is working on it.

**Vivek Shankar:** There were some other items that unfortunately were higher priority than this one, so that's why it's being delayed a little bit.

**Vivek Shankar:** But either way, we'll definitely have it within the next sprint, so it should not be an issue.

**Vivek Shankar:** Moving on to the performance side of things, so just a general caveat, Google introduced an update last week where you cannot anymore preview like 100 results per page.

**Vivek Shankar:** And it seems to have had a lot of knock-on effects.

**Vivek Shankar:** I've included a reference article over here just to sort of give you an idea of what's happening.

**Vivek Shankar:** But there seem to be some really...

**Vivek Shankar:** weird sort of side effects.

**Vivek Shankar:** We haven't seen too many of these with Strapeze data, but we are seeing this across the board for a lot of clients where the number of sessions being reported in GA4, the number of clicks and impressions, especially reported in GSC, they're basically inaccurate.

**Vivek Shankar:** So we're seeing a lot of fluctuations that don't make sense.

**Vivek Shankar:** You know, comparing it to CMS analytics versus GSC numbers, they just aren't matching up.

**Vivek Shankar:** So with that caveat, just to say that, you know, performance seems to have held pretty steady this past week, but again, it's probably not best to draw deep conclusions from any of this data.

**Vivek Shankar:** Generally speaking, if you go into Looker and you look at the non-branded impressions, you will see a drop.

**Vivek Shankar:** That seems to be one of the side effects, at least according to everybody in the SEO world, seems to be one of the side effects of the update that Google released.

**Vivek Shankar:** So generally speaking, um, the, um,

**Vivek Shankar:** Overall sessions, we saw a slight dip, but the engaged sessions remained pretty much the same.

**Vivek Shankar:** Even if we included the strapi created integration pages, the trend was pretty much the same as when we excluded.

**Vivek Shankar:** Conversion events declined slightly week on week, and generally we're still at healthy levels, but these events keep fluctuating a bit.

**Vivek Shankar:** And then going into the cohort performance, generally speaking, you know, the two biggest sort of cohorts that tend to perform the best for us, which is headless CMS and ecosystem, they dipped slightly, but the engagement improved for the ecosystem.

**Vivek Shankar:** Tutorials and use case sessions also increased, and then generally the integration pages seem to be doing quite well.

**Vivek Shankar:** Any questions about this before I dive into the LLM traffic side of things, anything I can answer at all?

**Vivek Shankar:** All right.

**Vivek Shankar:** So going into the LLM traffic, generally, again, the number of sessions we received, it comes from GA4, so the data is a bit iffy, but, you know, we saw an increase, not a massive one, but we saw a slight increase.

**Vivek Shankar:** GPT remains a top referrer.

**Vivek Shankar:** And generally speaking, given all these images are from scrunch, by the way, so in terms of visibility in LLMs for the queries that we've been tracking, it seems pretty healthy.

**Vivek Shankar:** Strapi is showing up more often than not for, you know, compared to the rest of the competition.

**Vivek Shankar:** The number of citations over here, which is this little 6% blue circle over here in this image, it seems to be a little low, but competitor citations are also low.

**Vivek Shankar:** So we're still trying to figure out exactly what this means in terms of, you know, does it mean that our queries are on point, or does it just mean that, you know, the LLMs are...

**Vivek Shankar:** They're a bit too variable in terms of what they're suggesting as answers.

**Vivek Shankar:** So we're still digging into that.

**Vivek Shankar:** But generally speaking, strapi's presence is pretty healthy overall, as you can see from these dashboards.

**Vivek Shankar:** Across all prompt clusters as well, strapi's presence is pretty strong.

**Vivek Shankar:** There's just a couple ones where we're lagging a bit.

**Vivek Shankar:** So we'd sort of group all the prompts we're tracking into various categories.

**Vivek Shankar:** One of these was security best practices for CMS.

**Vivek Shankar:** And the other one was database options for content management.

**Vivek Shankar:** So these have a few prompts where strapi's presence has been a little, it's falling off a bit.

**Vivek Shankar:** So we are taking a look at those prompts and seeing whether there's any content tweaks we can make to boost strapi's presence over there.

**Vivek Shankar:** So that wraps up the performance side of things. Happy to answer any questions you might have.

**Vivek Shankar:** Okay, so moving on, the talking points, so basically the medium workflow will be completed this week and we'll share the results, pretty optimistic about it as I mentioned, and then we've added the topics that Theo and Paul had suggested for next week onwards, it's actually for the next week and the week after that.

**Vivek Shankar:** Following up regarding the HubSpot access, I know Golzar and I had spoken about this on Slack, we don't seem to have HubSpot access, the link either has expired or we can't see the dashboard, but generally if this is too much of a lift, perhaps creating a custom event in GA4, and then embedding that across all the content that we've created is probably the best way of tracking conversions, et cetera, from our content.

**Vivek Shankar:** So, yeah, that's pretty much the update.

**Vivek Shankar:** Any

**Vivek Shankar:** Any questions, et cetera, can answer any clarifications.

**Golzar Yaghoubpour:** I tagged Tori in that Slack message, and he got back today.

**Golzar Yaghoubpour:** He was out of office yesterday.

**Golzar Yaghoubpour:** So let's see what he says when he responds, and then we can decide what the best force of action is.

**Vivek Shankar:** Yep, makes sense.

**Victor Coisne:** Yeah, if you can go back to sharing the screen.

**Vivek Shankar:** Oh, sorry.

**Victor Coisne:** Yeah, for the action item, can we use the database that we created that we add to the database?

**Victor Coisne:** Yeah.

**Victor Coisne:** I think we should embed that in everything else.

**Mara Leighton:** Yep, sure.

**Mara Leighton:** Totally.

**Mara Leighton:** Yeah, and I also probably missed giving you some context on that, Vivek, when you were back.

**Victor Coisne:** But yeah, we can just drop things in here.

**Victor Coisne:** That's a great idea.

**Vivek Shankar:** Yep, no worries.

**Vivek Shankar:** We'll do that.

**Victor Coisne:** And yeah, I think we have a...

**Victor Coisne:** A topics we covered, I'll let Paul and Golzar, think Golzar, you have something around social, and Paul, have something around some of the other things we discussed on Friday.

**Victor Coisne:** So I'll let the team cover that.

**Golzar Yaghoubpour:** Yeah, I think Paul summarized my request.

**Golzar Yaghoubpour:** Actually, we were chatting right before this call.

**Golzar Yaghoubpour:** So basically, we want to know, we want to be able to add to the workflow a automation for social post creation.

**Golzar Yaghoubpour:** Thanks.

**Golzar Yaghoubpour:** Is that possible today?

**Vivek Shankar:** Is there any platform you had in mind?

**Paul Bratslavsky:** Is it just Twitter and LinkedIn?

**Paul Bratslavsky:** Yeah, wanted to give you some context, I guess, and then you could correct me.

**Golzar Yaghoubpour:** Yeah, go ahead.

**Paul Bratslavsky:** to make an automated social post creation process.

**Paul Bratslavsky:** And the idea we had, since we're already publishing content, is to have a fork that's triggered every time.

**Paul Bratslavsky:** We publish new content, and the way Golzar's been scheduling posting content is through HubSpot, and the easiest way to do bulk import is use a CSV file.

**Paul Bratslavsky:** So the workflow that I was thinking about is literally every time strapi content is published, we fetch the content using AI generate the social post, add an image, either from the existing article or AI generated card, etc.

**Paul Bratslavsky:** And then create a UTM link that we could add in HubSpot ourselves.

**Paul Bratslavsky:** And then basically this is all going to be saved to Google Sheets that Golzar could easily export via CSV to do bulk scheduling.

**Paul Bratslavsky:** So the flow is publish content, create the post, and save it to Google Sheets.

**Vivek Shankar:** But is this for, which platforms are this for?

**Paul Bratslavsky:** Is it just LinkedIn or?

**Paul Bratslavsky:** So this is going be Twitter.

**Paul Bratslavsky:** Yeah, yeah, Twitter, LinkedIn, and so forth.

**Golzar Yaghoubpour:** Twitter.

**Golzar Yaghoubpour:** Twitter, and Twitter, LinkedIn, I would say are the most important.

**Golzar Yaghoubpour:** And then we also post to Facebook and Instagram as well.

**Golzar Yaghoubpour:** And so just, Paul, thank you for walking us through this.

**Golzar Yaghoubpour:** It's excellent.

**Golzar Yaghoubpour:** And I just wanted to add a call out.

**Golzar Yaghoubpour:** So it would be for strappy published content, not the AI generated content.

**Golzar Yaghoubpour:** Just I want to make sure that's clear.

**Golzar Yaghoubpour:** Is this something that is doable?

**Vivek Shankar:** I think technically, yes.

**Vivek Shankar:** I think in terms of our backlog, that's the only question.

**Vivek Shankar:** So the best step, I think, is taking it to engineering and just seeing, like, what kind of VTA they can give us.

**Vivek Shankar:** But we can definitely check.

**Vivek Shankar:** And I don't think technically it's a huge thing because we've done it for Medium as well.

**Vivek Shankar:** It makes sense to expand it to the other platforms too.

**Paul Bratslavsky:** And I think from, like...

**Paul Bratslavsky:** Kind of something that's going to help our team.

**Paul Bratslavsky:** would probably prioritize this first, but two additional items I have, and I just added quick my call-outs.

**Victor Coisne:** One second, before you go into the other topics.

**Victor Coisne:** Today we don't really promote on social growthx content, because we prioritize promoting internal content.

**Victor Coisne:** And also that's a good way to track how much those posts are bringing in organically.

**Victor Coisne:** So, how do you, you know, is this for only growthx content?

**Victor Coisne:** Is it for every content?

**Paul Bratslavsky:** No, this is for just published content, that content we create internally.

**Paul Bratslavsky:** And so basically we would exclude all the content that has the ecosystem tag, which is basically all the content that's published by growthx.

**Paul Bratslavsky:** So this is for us to promote our content, but have an automated process.

**Golzar Yaghoubpour:** Yeah, so that was the call-out that I...

**Golzar Yaghoubpour:** I had just shared that it's not for AI-generated content, it's for internal written content.

**Vivek Shankar:** Okay.

**Vivek Shankar:** I think, yeah, we can take it to our engineering team.

**Vivek Shankar:** We'll come back to you with regards to ETA, et cetera.

**Golzar Yaghoubpour:** Excellent.

**Golzar Yaghoubpour:** And I think, so HubSpot provides a pretty simple template.

**Golzar Yaghoubpour:** And I think sometimes it does generate errors.

**Golzar Yaghoubpour:** So we'll probably have to, like, work through a couple rounds of this.

**Golzar Yaghoubpour:** But I'm curious to hear what your engineering team has to say about it.

**Golzar Yaghoubpour:** So I'll wait for them first to provide feedback.

**Victor Coisne:** And one thing, like, ideally, in my opinion, we should bypass the Google Sheet step and try to schedule stuff as draft directly, just to avoid a manual step.

**Victor Coisne:** So if we can automate that step, I think it's even better.

**Paul Bratslavsky:** I didn't look into that process, so if there is HubSpot API that you have access to, don't see why that would be a problem, but yeah, that's a good call out, Victor.

**Vivek Shankar:** Okay.

**Vivek Shankar:** There was one thing I wanted to point out.

**Vivek Shankar:** It's not in this table, and I think, Paul, you and I had spoken about this before I went out of office.

**Vivek Shankar:** The comparison page is the huge table that's up front.

**Vivek Shankar:** We had spoken about maybe minimizing that or removing it because we already have the at-a-glance table on the page.

**Vivek Shankar:** Just wanted to check in on that, and maybe if I should add it as an item here.

**Paul Bratslavsky:** Okay.

**Paul Bratslavsky:** So, yeah.

**Paul Bratslavsky:** So, basically, the way it gets rendered on the front-end, we have other comparison pages that have that table.

**Paul Bratslavsky:** So, Victor and I, we wanted to wait until all the comparison pages were done, and once those are done, we will remove that table completely from the front-end website.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Cool.

**Vivek Shankar:** Makes sense.

**Vivek Shankar:** All right.

**Paul Bratslavsky:** Thank you for that.

**Paul Bratslavsky:** Yeah, and then the two other items that I wanted to bring up, we wanted to kind of create an automated process for discovering content gaps, and we wanted to leverage social listening, websites like Reddit, Twitter, etc.

**Paul Bratslavsky:** We also have access to Kappa AI, which have community ask questions, including GitHub issues, and we wanted to see if there's going to be a way to create an automated process, which kind of will take all those accounts into consideration.

**Paul Bratslavsky:** and maybe create a report of topics that would be good additions for growthx articles.

**Vivek Shankar:** So when you say content gaps, are you talking about, that's a big scope.

**Vivek Shankar:** So currently, there is the easy way, which is basically like pulling the content gap report from your standard SEO tool, but I'm assuming you also want to look at gaps within Kappa community, Discord, etc.

**Vivek Shankar:** So, yeah.

**Paul Bratslavsky:** So to clarify, is to basically human-sourced questions.

**Paul Bratslavsky:** So like Social, Kappa, and GitHub, it's questions from our community.

**Paul Bratslavsky:** So this would be like an additional source outside of the SEO research.

**Paul Bratslavsky:** So if you see commonly asked questions that are repeating, maybe there's content that we could create around that topic.

**Vivek Shankar:** Yeah, that's, yeah, definitely makes sense.

**Vivek Shankar:** We'll take it to engineering again, because I can't give an answer exactly on the ETA there.

**Vivek Shankar:** But I think for certain, it's a flow that we've been brainstorming internally as well.

**Vivek Shankar:** So, and we're doing it to a certain extent, manually plus automated for some clients.

**Vivek Shankar:** But yeah, we can definitely explore that for Strapi in terms of the sources.

**Vivek Shankar:** The only thing I would request is if you could please send me a list of the sources you wish to monitor, because then...

**Vivek Shankar:** I can take it to engineering and be like, okay, these are the exact things we need to look at.

**Paul Bratslavsky:** Okay, yeah, I'll add that to my action items.

**Paul Bratslavsky:** And we could continue the conversation with Slack.

**Paul Bratslavsky:** did add those items so we could keep the talk there.

**Paul Bratslavsky:** And then the last item I had, I think this will be really good, is to see if it's possible to create a research agent for content curation.

**Paul Bratslavsky:** So basically being able to see what's trending in the web dev space and then seeing if we could basically create an agent that creates a blog post that kind of covers what's trending.

**Paul Bratslavsky:** Like top five things to swap the tag kind of idea and have that automatic process to write the blog post.

**Vivek Shankar:** Yeah, like a weekly digest.

**Vivek Shankar:** Like this is what people are talking about.

**Vivek Shankar:** This is what is trending, et cetera.

**Vivek Shankar:** In terms of trending, well, I don't know if an agent can measure what is trending in terms of

**Vivek Shankar:** of views and clicks, et cetera, you can certainly measure what's trending, you know, if it goes to Reddit or a forum in terms of upvotes, et cetera, that would be an easy measure.

**Vivek Shankar:** But again, I think the best place to start over there would be to define the sources or define the places we wish to monitor.

**Vivek Shankar:** So once we get that, we can then figure out how to define what's trending, if that makes sense.

**Paul Bratslavsky:** Yeah, like, mean, the idea is to, yeah, so I'll think more about this, but the general idea is to basically, okay, yeah, I'll think more about it, but let just keep it short and I'll add it in Slack.

**Vivek Shankar:** All right, makes sense, yeah.

**Vivek Shankar:** We, again, that is something we do with a mixture of manual plus automation.

**Vivek Shankar:** Like, example, for one client, there is a YouTube channel that we monitor, just looking at which new videos were published, for example, how many views they're getting.

**Vivek Shankar:** So that's like a quasi sort of popularity, you know, measurement.

**Vivek Shankar:** But yeah, we can certainly add more sources to it and see like, you know, maybe keep tabs on competitors like, okay, this is what they published.

**Vivek Shankar:** This is what they're talking about on social.

**Vivek Shankar:** You know, that might be maybe V2 for this flow, but we can certainly get that going and brainstorm with engineering.

**Paul Bratslavsky:** Okay, so you've done something similar like this where you had like an external YouTube channel, which you used to monitor.

**Paul Bratslavsky:** And so, yeah, I could probably come up with some sources for YouTube channels that cover trending tech topics.

**Paul Bratslavsky:** There's also a couple of good email subscriptions that go out monthly, and maybe you can use those as sources as well.

**Vivek Shankar:** Yeah, I mean, we could even like, so the way we're doing it, the flow that I just mentioned, it's not like I would say, it's not a flow in Atlas right now.

**Vivek Shankar:** It's kind of a flow that we're running on the side.

**Vivek Shankar:** Basically, we look at that.

**Vivek Shankar:** We look at all the topics that have been published over the past week or past month, etc., depending on how far back we want to go.

**Vivek Shankar:** And then we cross-reference it with the ICP just to see what kind of an angle we can take here, whether we need to enrich this topic, whether it's a new topic, etc.

**Vivek Shankar:** So the logic is kind of built into the flow.

**Vivek Shankar:** And I think since we already have strapi's ICP constantly being updated, you know, we can maybe cross-reference it that way and then come up with suitable content angles for human review and then just build on that.

**Paul Bratslavsky:** Okay.

**Paul Bratslavsky:** Sounds good.

**Paul Bratslavsky:** And I'll continue this conversation with you on Slack so we could keep pushing this forward.

**Vivek Shankar:** Perfect.

**Vivek Shankar:** Thank you.

**Vivek Shankar:** Yep.

**Vivek Shankar:** Makes sense.

**Vivek Shankar:** All right.

**Vivek Shankar:** I think, uh, that's it.

**Vivek Shankar:** So in case there's no other questions, um, we will follow up on Slack.

**Victor Coisne:** Thanks, Tim.

**Mara Leighton:** Thanks.

**Paul Bratslavsky:** Thanks, everyone.

**Paul Bratslavsky:** Thanks so much, everyone.

**Mara Leighton:** Bye.
