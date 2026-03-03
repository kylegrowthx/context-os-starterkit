# Deepgram <> Growth X - Weekly Sync

<metadata>
date: 2025-09-24
time: 17:00 UTC
duration: 44 minutes
organizer: Erik O'Brien (GrowthX)
participants: Aida Knezevic (GrowthX), Erik O'Brien (GrowthX), Praveen Rangnath, Sam Lee, Delano Fernando, Jose Francisco, Patricia Mitter, Nikko Lobato, Hasan Jilani, Pippin Bongiovanni, Justin Epstein, Natalie Abeysena
fathom_recording_id: 89555700
fathom_url: https://fathom.video/calls/419534986
share_url: https://fathom.video/share/iLKyrsPsitp-Aj86sBETqnCan-f-Vsxy
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

GrowthX and Deepgram aligned on content production strategy: 30 blog assignments were approved to scale content output, with the first calibration blog on voice activity detection shared for review and feedback. The team introduced a new Looker dashboard combining Google Search Console and GA4 data to track content performance and SEO metrics, revealing a critical finding that Deepgram's AI apps pages (especially Cutout Pro) drive 62,000 clicks but may be hurting site relevance — Aida committed to delivering a comprehensive content pruning plan next week combining data from GSC, SEMrush, and lead attribution.

---

## Context

Deepgram is a speech-to-text and voice AI platform that engaged GrowthX for content marketing and SEO strategy. This is a weekly operational sync where GrowthX team members (Aida and Erik) discuss content production, audit findings, and analytics setup with Deepgram stakeholders including Praveen (appears to be a product or strategy lead), Hasan (technical/product perspective), and Justin (possibly SEM/marketing). The engagement is focused on producing high-quality blog content around voice activity detection, speech-to-text APIs, and language-specific use cases, while simultaneously auditing existing content for relevance and SEO performance. The meeting reveals a tension between traffic quantity (especially from off-topic AI app pages) and content relevance — a concern that will drive the pruning strategy work.

---

## Relevance

- **To GrowthX Delivery:** Calibration process for blog content shows successful alignment on tone, depth, and technical accuracy; custom article generation pipeline can be extended for API-focused developer content. Content pruning methodology (combining GSC, SEMrush, lead data, engagement rates) is a replicable framework Aida developed with Jacob (ex-G2) that can be applied to other accounts.

- **To GrowthX Business Development:** Account health signals are positive — client approved 30 assignments upfront, showing confidence in GrowthX's strategy. Looker dashboard adoption by Justin (SEM strategy) indicates deepening integration across client's marketing function. Risk: content pruning decision requires Deepgram alignment on keeping vs. deleting 62,000-click Cutout Pro page — Aida correctly flagged need for GA4 exploration reports to prove ROI before deletion.

- **To GrowthX Content & SEO:** Data-driven pruning approach addresses a critical gap: "Best speech to text APIs" article dropped from 7,200 to 2,781 clicks (66% decline), yet still ranks page-one for "speech to text API." Blog last refreshed April 2025 (5+ months old); Aida flagged for refresh because LLMs cite content from past 3 months. Site-wide relevance hypothesis (unconfirmed but based on G2 pattern) suggests low-engagement content drags down rankings for high-value pages — validates pruning ROI.

---

## Overview

- 30 content assignments approved; GrowthX to scale content production
- Content audit underway; pruning strategy to be presented next week
- New Looker dashboard provides comprehensive traffic and SEO insights
- Significant traffic from AI apps pages (e.g., Cutout Pro) needs further analysis for relevance and impact

---

## Key Topics

### Content Production and Calibration

  - 30 assignments approved; content clusters align with SEO goals
  - First calibration blog on voice activity detection shared
  - GrowthX to produce 3 more blogs; team to review and provide feedback
  - Custom article generation pipeline possible for specific needs (e.g., more technical API information)

### Content Audit and Pruning Strategy

  - Combining data from Google Search Console, SEMrush, and lead reports
  - Analyzing 6-month periods for clicks, impressions, and keyword rankings
  - Will provide recommendations for pruning irrelevant content
  - Hypothesis: Google considers overall website relevance for rankings

### SEO Performance Analysis

  - "Best speech to text APIs" article shows 66% drop in clicks (7,200 to 2,781)
  - Article ranks on page one for "speech to text API"
  - Team to refresh and update important articles, especially for LLM citations

### Looker Dashboard Introduction

  - Combines data from Google Search Console and GA4
  - Tracks sessions, engaged sessions, landing page performance, and conversions
  - Allows filtering by content clusters, date ranges, and traffic sources
  - Provides query rankings and non-branded keyword performance

### AI Apps Traffic Analysis

  - Cutout Pro drives significant traffic (62,000 clicks) despite being unrelated to Deepgram's core offering
  - Team to investigate user journeys from AI apps pages using GA4 exploration reports
  - Concern about potential negative impact on Google's perception of site relevance

### LLM Referral Traffic

  - Dashboard shows breakdown of traffic from various LLMs
  - Unexpected referrals from queries like "Vedic astrology" noted

---

## Action Items

**Hasan Jilani (Deepgram)**
- Provide wireframes for language-specific programmatic content pages to GrowthX team
- Review voice activity detection blog post shared by Aida, leave comments on doc

**Jose Francisco (Deepgram)**
- Review voice activity detection blog post shared by Aida, leave comments on doc

**Justin Epstein (Deepgram)**
- Review voice activity detection blog post shared by Aida, leave comments on doc
- Integrate Looker dashboard into SEM strategy

**Aida Knezevic (GrowthX)**
- Compile data (GSC, SEMrush, lead data) into single spreadsheet for content pruning analysis
- Prepare concrete content pruning plan to present next week

---

## Transcript
**Sam Lee:** This meeting is being recorded.

**Sam Lee:** How's it going, guys?

**Aida Knezevic:** Good.

**Erik O'Brien:** How are you doing, Sam?

**Sam Lee:** Doing good.

**Praveen Rangnath:** Hi, everyone.

**Aida Knezevic:** Hey.

**Erik O'Brien:** Hey, Praveen.

**Praveen Rangnath:** Hello, hello.

**Aida Knezevic:** How are you guys doing?

**Aida Knezevic:** Good.

**Praveen Rangnath:** How are you?

**Praveen Rangnath:** Good.

**Praveen Rangnath:** Doing great.

**Aida Knezevic:** Are we waiting on anybody else today?

**Praveen Rangnath:** We can go ahead and get started.

**Praveen Rangnath:** Some other folks might join, but we can start.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** So, first things first, we saw that you approved around 30 assignments last night.

**Aida Knezevic:** So, I wanted to get your thoughts on the, you the ones that we provided, if there was anything missing, just general thoughts.

**Praveen Rangnath:** I thought that they were on the right track.

**Praveen Rangnath:** So, I should have asked how many you wanted me to approve.

**Praveen Rangnath:** I just kind of went down the list.

**Praveen Rangnath:** I did it a little willy-nilly.

**Praveen Rangnath:** But yeah, like the content clusters, I think are right.

**Praveen Rangnath:** We went through that.

**Praveen Rangnath:** think like some of the topics there are good and interesting.

**Praveen Rangnath:** You know, I'm also trusting that we're aligned in terms of like what search terms we want to rank for in SEO and kind of what sort of GEO queries we want to rank for.

**Praveen Rangnath:** So that content list seemed to support those goals.

**Praveen Rangnath:** So it seemed fairly aligned to me.

**Praveen Rangnath:** I didn't like give it a super in-depth look, but it all seemed aligned to me.

**Praveen Rangnath:** So I thought that list is like a good list to start with.

**Praveen Rangnath:** Yeah, that was one thought.

**Praveen Rangnath:** And then my second thought was like, so that's a list of blogs.

**Praveen Rangnath:** And I'm sort of still wondering a little bit like what's the programmatic, is there also an accompanying AI programmatic, like create a lot of webpages effort as part of this as well, which would be like.

**Praveen Rangnath:** Like, you know, voice agents for financial services, voice agents for healthcare, voice agents for retail, you know, so on and so forth.

**Aida Knezevic:** Yeah, in terms of programmatic, so what we discussed last week was the language-related programmatic content.

**Aida Knezevic:** So I think maybe, Erik, do you have an update on this front?

**Erik O'Brien:** Did you get a chance to sync with the dev team?

**Erik O'Brien:** Yep, so they've got it in their backlog to start working on the pipeline to support this.

**Erik O'Brien:** And so now that we've got it registered on their end, we should start getting engineering resources sooner than later.

**Erik O'Brien:** I think the only thing that we asked from your guys' end was for, like, simple wireframes of what you would want the site structure to look like so that we can kind of adhere to that.

**Erik O'Brien:** And then I believe we took what was in the brief and provided that to our team.

**Erik O'Brien:** So keyword pattern of, like, speech-to-text, transcribe, language.

**Erik O'Brien:** And so we can continue to revise that or kind of take our team and put their creative spin on it, but that's at least the priority for now for programmatic is to focus on those language-specific pages.

**Praveen Rangnath:** Okay.

**Praveen Rangnath:** So from the deepgram side, who on our side can get them those wireframes?

**Praveen Rangnath:** Who would be the right person?

**Erik O'Brien:** I believe Hassan was the one that mentioned he could get them last week.

**Praveen Rangnath:** Okay.

**Praveen Rangnath:** All right.

**Praveen Rangnath:** If you did, feel free to just ping him in Slack and he'll get you what you need.

**Praveen Rangnath:** Wonderful.

**Praveen Rangnath:** Yeah.

**Aida Knezevic:** Okay.

**Praveen Rangnath:** Perfect.

**Praveen Rangnath:** Yeah.

**Praveen Rangnath:** Before anything else, Justin, Sam, Delano, Jose, anything else you guys want to add before we start?

**Jose Francisco:** Nothing on my end.

**Justin Epstein:** Yep.

**Justin Epstein:** I'm good.

**Praveen Rangnath:** Okay.

**Praveen Rangnath:** I think we have three GrowthX note-takers.

**Praveen Rangnath:** We have one deepgram assistant.

**Praveen Rangnath:** We literally...

**Praveen Rangnath:** We have two people from GrowthX, but we have three note takers.

**Aida Knezevic:** How did that happen?

**Aida Knezevic:** You know, I think there's one that's just a team note taker.

**Aida Knezevic:** So, yeah, the customer calls are recorded also with the team account.

**Praveen Rangnath:** Okay, excellent.

**Aida Knezevic:** All right.

**Praveen Rangnath:** Yeah, it's the new world.

**Praveen Rangnath:** So, yeah, Natalie A., if there's anything else you wanted to join, say before we started, just let us know.

**Praveen Rangnath:** Otherwise, we can get going.

**Natalie Abeysena:** Yeah, go ahead.

**Praveen Rangnath:** Yeah, okay.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** Yeah, mean, the 30 approved assignment, that's great.

**Aida Knezevic:** We want to, you know, approve as much as possible, you know, at the beginning so we can, like, just start scaling the content production as quickly as possible.

**Aida Knezevic:** I wanted, if at any point you think something's missing, just let us know and we can go back and, like, do additional research.

**Aida Knezevic:** But for now, the topics that we've identified, we're going to focus on them.


**Aida Knezevic:** We are linking to speech-to-text API.

**Aida Knezevic:** We're mentioning speech-to-text API throughout the content, so that's something that we're keeping in mind.

**Aida Knezevic:** Last night, I mean, last night, my time, yesterday, I shared our first calibration blog about voice, hold on, let me, voice activity detection.

**Praveen Rangnath:** Did you get the chance to take a look at that?

**Praveen Rangnath:** I looked at it briefly, but Hasan and Jose, and also Justin, like, in the team, I want you guys to also take a look at it and make sure it makes sense from your guys' perspective as well.

**Hasan Jilani:** Yeah, sounds good.

**Hasan Jilani:** I haven't had a chance yet.

**Aida Knezevic:** Okay, okay, no problem.

**Aida Knezevic:** We're going to move forward with doing an additional three, just to kind of keep things going.

**Aida Knezevic:** If, you know, if it turns out that we need to kind of make major updates to the writing guidelines.

**Aida Knezevic:** We'll do that, but, you know, just feel free to leave any comments in the doc, you know, anything related to voice tone, the, like, content depth as well.

**Aida Knezevic:** I think it's important for us to cover things in detail, and I also wanted to make sure to let you know that, if you remember, I presented the article generation pipeline a few weeks ago, and that pipeline, it's just the standard pipeline that everybody starts with.

**Aida Knezevic:** We can customize it.

**Aida Knezevic:** So, let's say, for example, you want the content to contain just more technical information about APIs, you know, something that maybe a developer would expect.

**Aida Knezevic:** We can work with our dev team to add an additional step in the article generation workflow that kind of goes back into the content and then provides that kind of information.

**Aida Knezevic:** So, you know, anything that comes to mind, just let us know.

**Aida Knezevic:** We, you know, the point of the calibration process to understand, like, okay, what part of the, you

**Aida Knezevic:** But what, how is the content good and how should the content be improved?

**Aida Knezevic:** So that's kind of what, you know, we're aiming to do here.

**Aida Knezevic:** But yeah, I'll be, I'll be waiting for your comments then.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** And then I wanted to kind of give you an update on the content audit because last week we were also talking about potentially pruning some of your content.

**Aida Knezevic:** And that's why I was looking for the lead data.

**Aida Knezevic:** So Erik and I synced with Jacob.

**Aida Knezevic:** He's one of the managing directors at GrowthX. He previously worked at G2 and ActiveCampaign, and has implemented content pruning in both of those roles.

**Aida Knezevic:** And he kind of gave us some advice and he was the one that actually brought up the fact that, hey, you need actually that conversion data.

**Aida Knezevic:** Because there could be blog pages about different topics that could have maybe contributed to leads from a client at some point, and we want to keep that in mind. So right now, let me share my screen — I'm going to show you what we're going to do. I have your 12-month lead report here, and I'm compiling all of this data in a single spreadsheet. What we're going to be looking at is the pages data from your blog — this is the learn part of your website — and I'm comparing the data for the last six months and then the preceding six months.

**Aida Knezevic:** I think that gives us a good enough range. Sometimes we do three months, but in this case, I want to do six months. We're going to be looking at the clicks and also the impressions.

**Aida Knezevic:** One thing that I did notice when I was looking at the traffic data was that your impressions, overall impressions for the blog have increased.

**Aida Knezevic:** Although the clicks have decreased.

**Aida Knezevic:** And there are a couple of reasons for this.

**Aida Knezevic:** A lot of websites are now seeing more impressions and less clicks due to AI overviews.

**Aida Knezevic:** So your website is still appearing in search results, but people might not be noticing it or like actually clicking through.

**Aida Knezevic:** And another reason could be that you are just kind of further down the search results.

**Aida Knezevic:** So you do appear on the SERP in front of a user, but you're too far down for them to actually click through.

**Aida Knezevic:** So I'm going to be combining the data from Google Search Console with the SEMrush data, specifically the number of keywords a URL ranks for, to give us an idea of what's doing really well in search. But we don't blindly follow this data — for example, these types of blogs rank for a lot of keywords, understandably.

**Aida Knezevic:** But we do want to understand, like, okay, is this ranking for anything?

**Aida Knezevic:** And we're also going to combine that with the lead data here.

**Aida Knezevic:** So, you know, we're aiming to get a single view across all of these data sources.

**Aida Knezevic:** And then we can see what the data looks like.

**Aida Knezevic:** But anything that's irrelevant for your business and hasn't been getting any clicks, impressions, or leads — that's something we're going to recommend you prune.

**Aida Knezevic:** And we're going to combine this in a spreadsheet.

**Aida Knezevic:** We can provide our recommendations and we'll leave a column for you to decide whether to keep something or not. We can also suggest pages that you can redirect deleted pages to, to make things easier.

**Aida Knezevic:** We can also suggest pages that you can redirect deleted pages to, to make things easier.

**Praveen Rangnath:** Okay.

**Praveen Rangnath:** Makes sense.

**Praveen Rangnath:** That's great.

**Praveen Rangnath:** I love it.

**Praveen Rangnath:** I love the methodology and the effort.

**Praveen Rangnath:** I'll show you one thing that was interesting.

**Praveen Rangnath:** The first tab you showed, which, yeah, this exact one.

**Praveen Rangnath:** Oh, sorry.

**Aida Knezevic:** Pages.

**Aida Knezevic:** Pages.

**Praveen Rangnath:** Okay.

**Praveen Rangnath:** It's, it's interesting that the, the, the learn post for best speech to text APIs last six months clicks 27, you know, 100 and previous six months, 7,200.

**Praveen Rangnath:** Right.

**Praveen Rangnath:** So that's like a, you know, one where it's one thirds or it's sort of 66% drop in, uh, in an article.

**Praveen Rangnath:** That's like pretty much exactly what we do.

**Praveen Rangnath:** Uh, so that's like, this will also be interesting.

**Praveen Rangnath:** Like when we show, um, over time, let's say in six months from now, we say, uh, uh, uh,

**Praveen Rangnath:** You know, the next six months clicks, right?

**Praveen Rangnath:** So tracking across three time periods. I'm curious what we can get that 2,781 up to.

**Praveen Rangnath:** It'll be really interesting to track that.

**Praveen Rangnath:** And yeah, it's just such an important topic for us.

**Praveen Rangnath:** Is that lower because the article is appearing lower, or is it something else when people search for "speech to text API"?

**Praveen Rangnath:** What's the reason for the lower clicks?

**Hasan Jilani:** So this is actually one of our best performing articles from an SEO perspective.

**Hasan Jilani:** It actually ranks on page one if you search for "speech to text API".

**Hasan Jilani:** So it's a really important article.

**Aida Knezevic:** Yeah, yeah, it is.

**Aida Knezevic:** So let's take a look at the SEMrush data.

**Aida Knezevic:** So right now it's ranking in the top three for one keyword.

**Aida Knezevic:** And let's say, let's take it back to maybe January of this year.

**Aida Knezevic:** It was just ranking for more keywords, more prominently.

**Aida Knezevic:** Definitely.

**Aida Knezevic:** So we could try, I mean, it was last refreshed in April 2025, which, you know, it's been five or six months.

**Aida Knezevic:** So we could, we could update that one.

**Aida Knezevic:** And, you know, we could, we could also highlight, you know, blogs that, you know, or we recommend refreshing as well.

**Praveen Rangnath:** Okay.

**Praveen Rangnath:** Yeah, I think that would be a big thing, because that's an important blog for us.

**Praveen Rangnath:** And if you scroll back up to the SEMrush page, there was a, the graph here, organic and paid traffic.

**Praveen Rangnath:** So organic traffic.

**Praveen Rangnath:** And this is including AI apps, the organic traffic, like how come this, this one, like the bottom one, organic keywords shows the AI app spike, but the, oh, I guess it does.

**Praveen Rangnath:** I guess it does sort of triple.

**Praveen Rangnath:** Yeah.

**Praveen Rangnath:** Cause AI apps was mainly 20, the first half of 2020.

**Praveen Rangnath:** Interesting.

**Praveen Rangnath:** It's interesting that there's a spike in November of 2024 for organic traffic.

**Aida Knezevic:** These are organic traffic estimates from SEMrush.

**Aida Knezevic:** But usually around late November, December, and January, there's a drop in organic traffic across all websites because of the holidays.

**Aida Knezevic:** But yeah, think this one could definitely be updated just to keep it relevant.

**Aida Knezevic:** Also, LLMs, they tend to cite content that was published in the last, I think, three months.

**Aida Knezevic:** I think that's kind of like they like fresh content.

**Praveen Rangnath:** So we can flag this for a refresh.

**Praveen Rangnath:** And even on the sheet, then maybe with Hassan, maybe there's like probably five to 10 of these that we might just want to do a refresh on for that exact purpose.

**Praveen Rangnath:** of LLMs looking for the only back to the last three months, potentially.

**Hasan Jilani:** Yeah, for sure.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** So I'll be working on this later this week.

**Aida Knezevic:** Hopefully by next week, we'll be able to present you with like a concrete like pruning plan so that we can kind of action on that as well.

**Aida Knezevic:** And when we were meeting in our meeting with Jacob, he mentioned something really interesting.

**Aida Knezevic:** He has a lot of his former co-workers from G2 who have launched websites that are kind of adjacent to what G2 is doing.

**Aida Knezevic:** And one of the people in his network, this is not like a confirmed ranking factor, but from his experience, he believes that like Google looks at the entirety of your website and how relevant the content is for the industry that you're in.

**Aida Knezevic:** And so let's say you have...

**Aida Knezevic:** You know, 50% of your content, people land on it, and they don't spend a lot of time.

**Aida Knezevic:** They bounce from it pretty quickly.

**Aida Knezevic:** And that is, like, Google does measure the engagement rate with your content.

**Aida Knezevic:** So whenever, every time you publish something new, Google has this data where, like, okay, 50% of your content is working, but the other half isn't.

**Aida Knezevic:** So it kind of impacts kind of the rankings right off the bat.

**Aida Knezevic:** Obviously, this is just, you know, hearsay.

**Aida Knezevic:** It's like people are just making assumptions.

**Aida Knezevic:** But, you know, the fact that people have been, you know, implementing these types of pruning strategies in D.C., pretty lit organic traffic lifts, does kind of support that claim.

**Aida Knezevic:** So I'll keep you updated with our progress here.

**Praveen Rangnath:** Okay, excellent.

**Praveen Rangnath:** Yeah, it does seem to make intuitive sense to me that if you have a lot of irrelevant web pages, Google will think, oh, this is not a great, informative, useful site.

**Praveen Rangnath:** So even if you have a new piece of content, it's kind of looked at with a grain of salt.

**Aida Knezevic:** Exactly — it seems intuitive.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Before we move on, I wanted to walk you through your Looker dashboard.

**Aida Knezevic:** So I'm going to share access with everyone here.

**Aida Knezevic:** You'll get an email invite.

**Aida Knezevic:** So we use Looker dashboards to combine data from Google Search Console and GA4.

**Aida Knezevic:** So we have an easier time tracking just your traffic performance in general and also our performance.

**Aida Knezevic:** So the performance of growthx content.

**Aida Knezevic:** So the first page gives you kind of a quick breakdown of sessions versus engaged sessions.

**Aida Knezevic:** Engaged sessions are sessions that last longer than 10 seconds or include a scroll or a click on a link on your site.

**Aida Knezevic:** So that means the user is engaged.

**Aida Knezevic:** The percentage of engaged sessions is always lower than overall sessions. I'll give you editing access so you'll be able to change the views and manipulate the data. For example, if you want to see just referral traffic, you can filter it. You can also change the date range. This table below gives you an overview of your landing page performance and a breakdown of your sessions by all traffic sources — search, social, and others.

**Aida Knezevic:** And it also gives you a breakdown of your query rankings.

**Aida Knezevic:** So, you know, like this is data from Google search consults.

**Aida Knezevic:** So if you're ranking in the first position for a specific query, that's the green line, and then the others are color-coded here as well.

**Aida Knezevic:** Google has made changes to the SERP, making it harder to track page rankings. You might see reports of query rankings dropping, not because they're actually dropping, but because Google removed page numbers (page one, two, three, etc.), making it harder to track rankings accurately. I wanted to flag that for you.

**Aida Knezevic:** The non-branded page tracks keywords that don't contain your brand name.

**Aida Knezevic:** And then the conversion events track data from your GA4.

**Aida Knezevic:** And these conversions already exist in your Google Analytics 4.

**Aida Knezevic:** So they can only show what you've already set up.

**Aida Knezevic:** So you have, for example, video complete, file download, contact us.

**Aida Knezevic:** So there's a lot of conversion events here.

**Aida Knezevic:** You can let us know which one is most important to track, depending on what's most relevant for your blog.

**Aida Knezevic:** And then the cohorts.

**Aida Knezevic:** This is going to be more relevant once we start publishing content.

**Aida Knezevic:** Right now we're only seeing non-GrowthX URLs, but once we start publishing content, you'll see the content clusters we're suggesting. This allows us to track our content performance compared to your general website and see which clusters are driving more traffic.

**Aida Knezevic:** We also have the landing page performance report, which shows the traffic for different landing pages.

**Aida Knezevic:** So you can, for example, filter here by blog or by glossary, and this data is pulled directly from Google Search Console.

**Aida Knezevic:** So URL, clicks, impressions, click-through rate, and average position.

**Aida Knezevic:** The queries are the keywords from Google Search Console that drive users to your website.

**Praveen Rangnath:** While this is loading, Justin, is this helpful for your SEM strategy as well?

**Justin Epstein:** Yeah, for sure.

**Justin Epstein:** I was just thinking about how super useful this is and organized.

**Justin Epstein:** So, yeah, I think we can definitely integrate this into, yeah, like our SEM strategy.

**Praveen Rangnath:** Great.

**Aida Knezevic:** Yeah, that's great to hear.

**Aida Knezevic:** Yeah, so here you can see kind of like the average position over time by query.

**Aida Knezevic:** If you scroll down, you can actually see the queries that are driving users to your site.

**Aida Knezevic:** Most of them are going to be branded.

**Aida Knezevic:** But, for example, you also have competitor searches that lead to your website.

**Aida Knezevic:** Can you cut that one really quickly?

**Praveen Rangnath:** There's a few things I want to see is Cutout Pro and 11 Labs.

**Praveen Rangnath:** Cutout Pro is an AI apps page — it's a graphic design tool. We get a ton of impressions on it.

**Praveen Rangnath:** Are we actually getting signups from Cutout Pro?

**Praveen Rangnath:** Yeah.

**Praveen Rangnath:** Does this measure that or no?

**Aida Knezevic:** No, this doesn't measure signups. We can see that you have a couple of pages ranking for Cutout Pro. We can dig into SEMrush to see what's ranking for this query.

**Praveen Rangnath:** It's interesting — Deepgram is at the top. How is this sorted? Oh, by URL clicks. So what does URL clicks mean?

**Aida Knezevic:** It means the number of people who click on your webpage in the search results for that query.

**Aida Knezevic:** So you're getting 62,000 clicks from the Cutout Pro query — that's 62,000 people searching for Cutout Pro and clicking through to your website.

**Aida Knezevic:** Yes.

**Praveen Rangnath:** Okay.

**Praveen Rangnath:** Which is fascinating because that's 25% of people that come by searching on our actual company name, right?

**Praveen Rangnath:** Cutout Pro is a visual graphics design tool — it has nothing to do with voice AI. It's an AI app, and I think some of the other queries on that list are similar.

**Aida Knezevic:** Yeah, it's crazy how much traffic we get from these.

**Aida Knezevic:** AI apps, Cutout Pro.

**Praveen Rangnath:** And so if you click there, like, you'll see, like, it's not, it's just, it's an AI apps page.

**Praveen Rangnath:** And so 68,000 people are coming here.

**Praveen Rangnath:** Do we know what they do after they get here?

**Aida Knezevic:** You can build an exploration report in Google Analytics 4 that analyzes user journeys from that landing page. It should be pretty straightforward.

**Praveen Rangnath:** Here's my concern: someone searching for Cutout Pro lands on this page. They see Cutout Pro mentioned, but then it says "try Deepgram." They don't know what Deepgram is, so they probably click away. From Google's perspective, this looks like a bad user experience — people search for Cutout Pro, find your website, but bounce immediately because it's irrelevant to them.

**Praveen Rangnath:** The second highest search driving people to our domain is Cutout Pro, right after our brand name. So from Google's perspective: Deepgram searches find Deepgram, but the second thing people search for is Cutout Pro — unrelated to your core business — and they arrive at your website and immediately bounce.

**Praveen Rangnath:** Right, so Google might think this is a low-quality website. Looking at the list: Lensgo AI, Dream Comparison, Crayon, Lensgo, Songtel — those are all AI apps, not voice AI products.

**Praveen Rangnath:** Of the top 10 queries driving traffic, three are Deepgram, one is 11 Labs which is intentional, and the rest are AI apps. It's a lot of off-topic traffic.

**Aida Knezevic:** I see what you're saying. AI apps is a separate section that brings traffic, but we need to understand what those users are actually doing. I'd set up an exploration report in GA4 to see if they're visiting other parts of the website or just bouncing.

**Praveen Rangnath:** We've been hesitant to remove Cutout Pro because there's so much traffic — we worried we'd lose signups. But the flip side is it might be hurting us. Having thousands of people land on something irrelevant to them is damaging. So it's critical to understand: are these AI app visitors actually converting or signing up, or are they just hurting our site relevance?

**Aida Knezevic:** You can set up an exploration report with all user sessions from the AI apps section. That would give you a clear picture of what those users are doing and whether it's worth keeping. But this is a broader conversation the team needs to align on. I'd start with that analysis.

**Praveen Rangnath:** The histogram here or the Marameco, that thing is, again, it's like cutout pros right there.

**Praveen Rangnath:** It's kind of magic.

**Aida Knezevic:** Yeah, yeah, I get it.

**Aida Knezevic:** Okay, and just really quickly, I wanted to show you.

**Aida Knezevic:** So the last page contains a breakdown of AI referral traffic.

**Aida Knezevic:** So it allows you to see which LLMs are driving the most sessions to your website, how many of those sessions are engaged sessions.

**Aida Knezevic:** So you can see the engagement rate right here as well.

**Aida Knezevic:** You can also see the landing pages getting the most LLM traffic and a breakdown of different LLMs.

**Praveen Rangnath:** One weird thing I notice: "Vedic astrology" shows up as number eight or nine on the LLM traffic list. That's another AI app, so somehow ChatGPT is recommending your site for Vedic astrology queries — which have nothing to do with voice AI.

**Aida Knezevic:** These are probably queries for Vedic astrology apps. Either way, the concern is the same — you're getting referral traffic to unrelated content.

**Praveen Rangnath:** As long as ChatGPT doesn't start thinking Deepgram is irrelevant the way Google might. I don't want LLMs associating us with off-topic content.

**Aida Knezevic:** Exactly. We want to build topical authority in your core clusters, so you attract more qualified traffic.

**Aida Knezevic:** I'm going to share access to the Looker dashboard in about 30 minutes. Erik and I have another call, but if you have questions, feel free to ask in our Slack channel.

**Praveen Rangnath:** Okay, sounds good.

**Aida Knezevic:** Thank you so much.

**Praveen Rangnath:** All right, I'll see you next week.

**Aida Knezevic:** Sounds good.

**Praveen Rangnath:** Thanks so much.

**Justin Epstein:** Thank you. Bye.
