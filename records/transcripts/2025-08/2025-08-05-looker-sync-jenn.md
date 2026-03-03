# Looker sync - Jenn

<metadata>
date: 2025-08-05
time: 16:00 UTC
duration: 29 minutes
organizer: vivek@growthxlabs.com
participants: Jenn Peters, Vivek Shankar, Sulaman Ahmed
fathom_recording_id: 78564385
fathom_url: https://fathom.video/calls/369707253
share_url: https://fathom.video/share/baw1wmhUWgxN2aRuWFeaWCYb7xLZmbL3
source: fathom
enriched_on: 2026-03-03 10:45 UTC
</metadata>

---

## Summary

Vivek gave Jenn a detailed walkthrough of the Looker dashboard for the Discern account, covering all dashboard tabs (Overall, Non-Branded, Conversion Events, Cohorts, Landing Pages, and LLM Referrals) and explaining key metrics like engagement rates, data sources (GA4 and Search Console), and how to use filters for segmentation. The critical update: after data integrity issues, the team shifted from automatic Airtable-to-Looker exports to a manual weekly process that content managers should run on Mondays before client syncs. Long-term, the team plans to build custom dashboards directly into Atlas rather than relying on the temporary Looker solution.

---

## Context

Jenn Peters (GrowthX Delivery) was getting up to speed on using Looker dashboards for the Discern client account after receiving multiple dashboard updates from Vivek and Sulaman. Vivek, who manages several accounts and oversees the Looker rollout, walked through the platform's capabilities and the recent operational shift. Previously, the team had automated the pipeline from Airtable to Looker, but persistent data-blending issues and sampling errors forced a switch to manual updates. Sulaman, who built the export process and created tutorial videos, joined to answer technical questions and coordinate next steps.

---

## Relevance

- **To GrowthX Delivery:** Looker dashboards are now the primary client reporting tool, requiring weekly manual updates by content managers every Monday or before client syncs. Vivek's workflow shows CMs prepare agenda templates with images pasted from Looker, then Vivek reviews and adds commentary. Ten-minute manual export job is straightforward but critical to client deliverables.

- **To GrowthX Business Development:** Discern is seeing strong LLM referral growth (7 to 20+ sessions), indicating their content is well-positioned for AI visibility. Engagement rates of 50-60% are benchmark; Discern often exceeds this. This positions the account for potential upsells or case study opportunities.

- **To CheckThat:** The meeting highlighted how GA4 and Search Console data are the sources of truth for Looker, and the team is tracking LLM referrals from ChatGPT and Perplexity. This is core to CheckThat value proposition — real-time AI visibility in client dashboards.

- **To GrowthX Ops:** Automatic Airtable-to-Looker export pipeline failed due to data-blending issues; long-term fix is custom dashboards in Atlas (being discussed with Andy). Temporary manual workaround is sustainable but creates a recurring weekly task for each account.

---

## Overview

- Looker dashboard pulls data directly from Google Analytics 4 and Search Console
- Manual process now required for exporting data from Airtable to Looker (temporary solution)
- Content managers should update data weekly, ideally on Mondays before client syncs
- Engagement rate benchmark is 50-60%, with higher rates indicating strong performance

---

## Key Topics

### Dashboard Overview and Data Sources

  - Dashboard pulls data directly from Google Analytics 4 and Search Console
  - Overall tab shows data for entire website, while other tabs focus on specific metrics
  - URL cohorts filter allows isolation of GrowthX-created content
  - Session medium typically filtered to organic and referral traffic
  - Engagement rate defined as 1+ minute on page or clicking to another page

### Non-Branded Performance Metrics

  - Non-branded tab excludes brand keywords (e.g., "discern", "discern.io")
  - Click data for individual searches is inaccurate due to Google limitations
  - Impression data and overall trends remain accurate and useful

### Conversion Events and Content Pillars

  - Conversion events tab pulls all GA4 events, allowing custom tracking
  - Cohorts tab breaks down performance by content pillars
  - Landing pages tab allows tracking of individual URL performance over time

### LLM Referrals and Benchmarks

  - LLM tab shows referral traffic from AI platforms (e.g., ChatGPT, Perplexity)
  - Engagement rate benchmark is 50-60%, with higher rates indicating strong performance
  - Discern seeing significant growth in LLM referrals (7 to 20+ sessions)

### Data Updates and Reporting Process

  - Manual process now required for exporting data from Airtable to Looker
  - Content managers should update data weekly, ideally on Mondays
  - CMs prepare initial client meeting agendas, including performance updates

---

## Action Items

**Jenn Peters (GrowthX)**
- Open ticket to request table showing keywords ranked by position

- Add "discern.com" to brand keywords list for non-branded filtering

- Watch Sulaman's videos on Looker dashboard updates and manual export process

- Implement weekly manual Looker dashboard updates (Mondays or before client syncs)

**Sulaman Ahmed (GrowthX)**
- Attach Looker export process video to Linear ticket for Jenn's reference

---

## Transcript
**Vivek Shankar:** The looker you had mentioned, this is for Discern, right?

**Vivek Shankar:** Yeah, Discern is the one that I haven't had a chance to look at.

**Jenn Peters:** Hey Sulaman, you just sent me the updates to the other ones that were done, and I haven't had a chance to look at them yet.

**Jenn Peters:** But I am seeing that the Discern one is broken for me, so I just don't know what I'm doing wrong.

**Jenn Peters:** Okay, so which one do you want to take a look at?

**Jenn Peters:** Discern would be great, because it's currently broken on my end.

**Vivek Shankar:** Okay, Discern, there we go.

**Vivek Shankar:** So what is broken?

**Jenn Peters:** Okay, good question.

**Jenn Peters:** So let me just make sure I'm seeing an updated...

**Jenn Peters:** Okay, so maybe it's just that mine is not the same as yours.

**Jenn Peters:** Are you looking at the one which has these hyphens in the title?

**Vivek Shankar:** Yeah, and just making...

**Jenn Peters:** Sure.

**Jenn Peters:** There's so many versions of this now, I don't even know which one is the right one.

**Jenn Peters:** I looked at the one from the link, but now I'm seeing that my order is different.

**Jenn Peters:** So now I'm thinking, yeah, like yours starts with overall, and the one that I'm looking at starts with non-branded, and that's broken.

**Jenn Peters:** Yeah, that's the old one.

**Jenn Peters:** Okay.

**Jenn Peters:** Can you show me the link in the chat?

**Jenn Peters:** Because, yeah, somehow I got the other link shared, I think.

**Vivek Shankar:** Yeah, I think Sulaman had sent the rest link in linear as well, so it's going to be there.

**Jenn Peters:** Just bear with me, I'm trying to see where you're sharing this.

**Jenn Peters:** I was saying to Sulaman, I had yesterday off as a stat holiday, and that just means I've crippled my work today.

**Jenn Peters:** Okay, I don't have access to that one under go through, you go through team.

**Jenn Peters:** Okay, let me just try again.

**Jenn Peters:** Okay, cool.

**Jenn Peters:** Okay, yeah, so this will probably solve a lot of my questions.

**Jenn Peters:** I think one of my questions was around, like, conversion events.

**Jenn Peters:** Okay, cool.

**Vivek Shankar:** We can go through one by There's something I want to point out.

**Vivek Shankar:** You do need to add whoever you want to share with in here.

**Vivek Shankar:** Okay.

**Jenn Peters:** For the clients and everything — just as a reminder.

**Vivek Shankar:** I thought I could just walk through the tabs.

**Vivek Shankar:** Yeah, that would be awesome, and then that would help you with probably all of them.

**Vivek Shankar:** So the overall tab is basically, we're pulling in data for their entire website, right?

**Vivek Shankar:** Right.

**Vivek Shankar:** So it's all here.

**Vivek Shankar:** The URL cohorts, this filter on top over here, this one helps you isolate only the URLs we've created versus everything else.

**Vivek Shankar:** So if you uncheck non-growthx URLs, this shows stuff, you know, only that we've created.

**Jenn Peters:** Very cool. Yeah, awesome.

**Jenn Peters:** This is a...

**Vivek Shankar:** Engagement filter, pretty straightforward. And then this session medium — this is from GA4, so usually I isolate to organic and referral because LLM traffic is part of referral. We're pulling in social media traffic as well, but I'd get their thoughts on it and just let them know that we're doing organic and referral here.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So this graph is sessions versus engaged sessions, so sessions is obviously how many times somebody has visited a page, and engaged sessions is basically the opposite of the bounce rate, so an engaged session, Google defines it as when someone spends at least one minute on page.

**Vivek Shankar:** Okay, that was my question, how much time is that?

**Vivek Shankar:** Yeah, it's one minute on page, or they clicked onto another page on the website, either one of those.

**Jenn Peters:** Okay.

**Vivek Shankar:** That's one.

**Vivek Shankar:** If a-minute threshold that is customizable, they can change it in their GA4 packet.

**Vivek Shankar:** So if they say, like, oh, one minute is not enough, well, you can change it to 10 minutes if you want.

**Vivek Shankar:** This table here, landing page performance, is pretty straightforward — it just shows you the URLs.

**Vivek Shankar:** So I think you had a question about this slash and what are those about?

**Vivek Shankar:** This is coming directly from GA4. A slash only — sorry, not backslash, just slash — usually means their homepage.

**Jenn Peters:** Okay.

**Jenn Peters:** Yeah.

**Vivek Shankar:** And "not set" is basically pages like the privacy policy and terms of use — pages that we can safely ignore and don't need to pay attention to.

**Jenn Peters:** Yeah, we don't need to.

**Vivek Shankar:** Usually, if you remove the non-grouped XURL filter, those will disappear because obviously we didn't create the homepage.

**Jenn Peters:** Okay.

**Jenn Peters:** Cool.

**Jenn Peters:** So here we have.

**Vivek Shankar:** Sessions, Engage Sessions, and Engagement Rate, which is, you know, pretty much the same metrics as a good card.

**Vivek Shankar:** The Deltas over here show you the comparison to the previous period you selected.

**Vivek Shankar:** So you can see here the timeline is selected at July 6th to August 4th, which is roughly a month.

**Jenn Peters:** Yeah.

**Jenn Peters:** Yeah.

**Vivek Shankar:** So the Delta measures the same period previous, right?

**Vivek Shankar:** So if you want to do like a weekly or a monthly, you just change this over here, change the timeline over here, and the Delta will show you the preceding period for that timeline.

**Vivek Shankar:** So you can do any number of comparative periods.

**Vivek Shankar:** Okay, great.

**Vivek Shankar:** It's pretty much the same.

**Jenn Peters:** Yeah.

**Vivek Shankar:** The Sessions by Referrer is pretty straightforward, you know, how much we're getting for Google, Bing, et cetera, et cetera.

**Vivek Shankar:** But something I want to point out, coming back to the date period, the week ends on a Sunday.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Right.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** So that's why.

**Vivek Shankar:** You're seeing this ridiculously small bar over here, August 3rd, the week starts on a Monday and finishes on a Sunday, so let's say I put, I want to do it for one month, I'm going to do roughly June 30th, which is a Monday, and August 3rd, which is the latest of the previous Sunday, so now you get this video, which looks like we're doing great, so.

**Jenn Peters:** Much better.

**Vivek Shankar:** Yeah, and then this thing just kind of breaks down the total sources — pretty straightforward. Query ranking distribution needs a little explanation. This chart tells you how many keywords we rank for based on position. If you look at the numbers here, it says 162, which means we are ranking in number one in Google for 62 keywords.

**Jenn Peters:** Okay, cool, that's what I thought it was, but I wasn't sure how do we see which keywords from.

**Vivek Shankar:** If you need it, we can build a pretty simple table below this that lists all the keywords.

**Vivek Shankar:** If you need that, just open a ticket and leave it in here.

**Vivek Shankar:** It's pretty straightforward.

**Jenn Peters:** Okay, awesome.

**Jenn Peters:** That's great.

**Jenn Peters:** Yeah.

**Vivek Shankar:** Something I want to point out because I'm having discussions with clients about this. A lot of clients sometimes check SEMrush and come back saying SEMrush only shows they rank number one for five keywords. Here you see much more. We want to tell them this data is directly from Google — we're not modifying it in any way. SEMrush is behind the curve.

**Vivek Shankar:** Right.

**Vivek Shankar:** Google tends to just give you, like, if you rank number one for even, let's say, five seconds over the past month for a keyword, it'll show up on this chart because Google includes it.

**Jenn Peters:** Okay.

**Vivek Shankar:** That's just how it is. The keywords that show up in the table will look a bit nonsensical and won't match up with SEMrush, so just want to let clients know.

**Vivek Shankar:** So, sorry, any other questions about this thing?

**Jenn Peters:** Nope, that's all pretty straightforward.

**Jenn Peters:** Yeah, that looks awesome.

**Jenn Peters:** Thank you.

**Vivek Shankar:** So non-branded is pretty much the same thing, except we are measuring everything only for non-branded keywords.

**Vivek Shankar:** So if you go on the back end over here, if you check the, you know, we're basically excluding all the brand keywords, right?

**Vivek Shankar:** discern, if you have other brand keywords, do send it our way.

**Vivek Shankar:** We'll just add it over here.

**Vivek Shankar:** So Discern, discern.io, discern.com, whatever — if you have other brand keywords, send them our way.

**Jenn Peters:** Like blog content or in this case, they call it slash resources.

**Jenn Peters:** It's just really anything without the brand keyword — you can filter by it.

**Vivek Shankar:** So again, it's for the entire website, but if you uncheck non-GrowthX, it isolates it just to our URLs.

**Vivek Shankar:** Something important to note: the click data is incorrect because Google doesn't share accurate click data for individual searches. However, the trends are indicative. You can see it increased here and then leveled off a bit — so I'd pay attention to the trends, not the absolute numbers. The impressions, though, are correct and accurate.

**Jenn Peters:** And is that the same in the Overall tab?

**Vivek Shankar:** No, the Overall tab is absolutely correct.

**Jenn Peters:** Okay, cool. I just wanted to make sure I'm giving clients accurate performance data.

**Vivek Shankar:** The Overall tab data is accurate. It's only individual search term click data that Google doesn't share for privacy reasons. Impressions, positions, everything else is accurate.

**Vivek Shankar:** Then this table is pretty much the same thing — it breaks out the data and gives you the exact URL. Pretty self-explanatory.

**Vivek Shankar:** This is the weekly breakdown — the deltas work the same way. If you want a weekly comparison, just change the timeline.

**Jenn Peters:** Everything on the page changes.

**Vivek Shankar:** The non-branded query ranking over time is the same as the previous page, except filtered for non-branded keywords.

**Vivek Shankar:** Conversion Events pulls in every event they've set up in GA. You can ask them which conversions they want to track and filter the data accordingly. The deltas compare the selected period to the previous period of the same length.

**Vivek Shankar:** Cohorts shows your content pillars. I'd always filter out non-GrowthX content and use organic and referral. The chart shows which cohort drives the most traffic.

**Jenn Peters:** Okay.

**Vivek Shankar:** And then if you scroll a bit down, the reason for this gap is because sometimes, you know, we have a lot of cohorts, in this case, we don't.

**Vivek Shankar:** So if you scroll down, this shows you clicks, right?

**Vivek Shankar:** It shows you clicks, impressions, CTR, and position.

**Vivek Shankar:** So this one is sessions and engagement rate, whereas this one is clicks and position and all that stuff.

**Vivek Shankar:** Right.

**Jenn Peters:** So, yes.

**Vivek Shankar:** And you can also click on any one of these.

**Vivek Shankar:** All of these are clickable, by the way.

**Vivek Shankar:** Oh, if you click on this, it isolates it just to, you know.

**Vivek Shankar:** How many prior that time period.

**Jenn Peters:** Okay.

**Jenn Peters:** And then you just click on it again to deselect.

**Vivek Shankar:** And then we come to Landing Pages. Usually this is more of a page for users or clients. They can paste a URL and see performance over time.

**Jenn Peters:** I love this for myself — it's how I inform content refreshes. I often export and track performance over time periods, so this is super helpful.

**Vivek Shankar:** Just a fair warning — this filters for every URL on the website. You can click on the homepage to show just that, or paste a specific URL to track just that one.

**Jenn Peters:** Got it. I exported everything and pulled out specific resources.

**Vivek Shankar:** That makes sense. This page is useful when clients ask how specific pages are performing — just paste the URL and show them. It breaks down performance daily, weekly, or monthly.

**Vivek Shankar:** Queries works the same way — type in a search query. You can filter by country. For example, typing "franchising" shows performance for that keyword, and you can filter to U.S. results.

**Vivek Shankar:** You can also see keywords like "Discern Inc." and other related terms. If you hover over a keyword, you see the click volume — you can click on any keyword to see which landing pages it drives traffic to.

**Vivek Shankar:** Then we come to LLMs. You can filter by GrowthX URLs only. If you set the date range ending on August 3 instead of 4, the chart looks better. Discern has seen massive growth in LLM referrals — from 7 to 20+ sessions.

**Jenn Peters:** They have perfect content for LLM referral — very informational and structured for AI answers.

**Vivek Shankar:** The table shows which landing pages are driving LLM traffic and their engagement rates. For engagement rate benchmarks: 50-60% is good, above 60% is very good. Discern is hitting 70-100% on some pages. The benchmark is that engagements are a positive indicator.

**Vivek Shankar:** That covers all your questions.

**Jenn Peters:** Yeah, this has been really helpful. My last question is about Airtable — how is the export set up? How often does it update?

**Vivek Shankar:** Good news and bad news. The good news is the Looker dashboards work perfectly. The bad news is we now have a manual process for exporting data from Airtable. Sulaman, did you get a chance to send the video to Jenn?

**Sulaman Ahmed:** I did send videos earlier.

**Jenn Peters:** For this specific account or the others? I got videos for other accounts when I was off.

**Vivek Shankar:** Sulaman, let's attach the video to the Linear ticket for Jenn's reference.

**Jenn Peters:** If it's about manually updating Regex formulas, I know how to do that already. But is that what we have to do now? We're not exporting from Airtable automatically anymore?

**Vivek Shankar:** Right, we're not doing automatic exports because that's what was breaking everything. The automatic Airtable export had data-blending issues that caused sampling errors.

**Jenn Peters:** So for the three accounts you set up, what date are they updated through?

**Vivek Shankar:** Check the date that Sulaman sent you.

**Sulaman Ahmed:** In the message, there are three Looker dashboard links and one video link with the guidance. Each dashboard shows the last update date, so you can continue from there.

**Jenn Peters:** How often are you doing this? Are you having your content managers do it?

**Vivek Shankar:** I'd have the CMs do it. It takes about 10 minutes, and I have my guys do it at the start of each week on Mondays, because we publish on Fridays. That timing makes sense for the weekly client syncs.

**Jenn Peters:** When do you do it? Every Monday?

**Vivek Shankar:** Actually, I have them do it when they prepare the client meeting agendas. They set up the Notion page, and I review it and add the performance details from the Looker dashboard.

**Jenn Peters:** Can you show me an example?

**Vivek Shankar:** Sure. The template has them add attendees, fill out fields, then there's a performance update section where they paste the Looker screenshot, and I write the commentary.

**Vivek Shankar:** More experienced CMs try to add commentary themselves. I review and modify. I'm not creating from scratch because I don't have time.

**Jenn Peters:** That's really helpful. That's my questions for now. I'll watch the videos. I'm a bit strapped this week — one of my content managers got pulled for another project, so I might get back to you later with follow-up questions, but this is all pretty straightforward. I really appreciate your time.

**Sulaman Ahmed:** One quick question just for learning — when you select a time interval like July to August and it shows a delta, does it compare to the same period last year or the previous period?

**Vivek Shankar:** It's the previous period. So if you select 30 days, it compares to the 30 days before that.

**Jenn Peters:** Thanks. I'm not thrilled about manual updates, but at least the data will be accurate. The automatic export kept breaking — it would work for a day, then throw data configuration errors. Once we have our internal Airtable replacement, we should be able to build better exports.

**Vivek Shankar:** Right now we're migrating everything to the new template I showed you. Once that's done, Sulaman has some ideas for better solutions.

**Sulaman Ahmed:** Eventually, the plan is to build custom dashboards directly in Atlas, so we're not using this as a permanent solution. We'll discuss with Andy.

**Jenn Peters:** That would be amazing. In the meantime, thanks for your patience with my questions. I'm sure I'll have more as I get up to speed. I really appreciate your time.

**Jenn Peters:** Thanks a lot. Talk to you soon.

**Jenn Peters:** Bye, bye.
