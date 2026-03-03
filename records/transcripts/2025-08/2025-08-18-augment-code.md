# Augment Code

<metadata>
date: 2025-08-18
time: 21:46 UTC
duration: 19 minutes
organizer: dave@growthx.ai
participants: Dave Capone, George Haikal
fathom_recording_id: 81293429
fathom_url: https://fathom.video/calls/384253167
share_url: https://fathom.video/share/49tAzDToCgn8vjdJgkfVpvzzeteh2NQ4
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

Dave and George reviewed Augment Code's strong early SEO performance (~10k impressions, ~100 clicks in under one month) and aligned on solutions to automate weekly reporting and build a 12-month content forecast. Dave committed to delivering a data-driven content strategy including existing topics plus new areas (AI coding database, learning to code, prompt engineering) by Wednesday morning for the client meeting. Suleman will build an automated Google Sheet with Google Search Console API integration to replace manual weekly data pulls.

---

## Context

Augment Code is an AI code auditing platform that GrowthX is running a major content engagement with—publishing ~30 articles per week in their /guide section. The client has a large brand and significant budget, including a committed $10k backlink campaign targeting "AI coding" and related keywords. GrowthX's editorial strategy is performing ahead of expectations after just under one month, with strong indexing and initial organic traffic generating meaningful impressions despite the low CTR (which George and Dave analyzed as normal for new content). The client values clear ROI tracking and wants weekly reporting to answer to internal stakeholders, which currently requires George to manually pull data from Google Search Console every week. This call addressed how to make reporting and forecasting more efficient and data-driven so GrowthX can deliver better visibility into results and future potential.

---

## Relevance

- **To GrowthX Delivery:** Identified opportunity to build an automated reporting dashboard (Google Sheets + GSC API or Looker) for a high-volume content engagement; this is reusable methodology for other clients. Manual reporting is a delivery friction point worth solving systematically.
- **To GrowthX Delivery:** Dave's 12-month content forecast methodology (based on competitor traffic analysis and winnable topic identification) is an underutilized asset—this call shows client appetite for data-driven content planning that goes beyond initial strategy, with $10k+ budget available for backlink support.
- **To GrowthX Business Development:** Augment Code is signal-rich for expansion: aggressive growth posture, willingness to invest, clear focus on ROI, and existing metrics showing results. Expansion potential into adjacent services (backlinks, competitive keyword analysis, larger-scale content) is evident.
- **To GrowthX Delivery:** Performance metrics discussion revealed opportunity to optimize page titles for higher CTR; shows need for ongoing optimization guidance and weekly check-in rituals with client stakeholders.

---

## Overview

- Augment Code's /guide content has generated ~10,000 impressions and ~100 clicks in under one month with average position of 8 (page 1-2 results); CTR stabilized at ~0.7%, which is normal for new content
- Current reporting is fully manual: George pulls Google Search Console data weekly and manually updates Notion; ROI calculator exists but is outdated
- Dave will create a 12-month data-driven content forecast by Wednesday (including existing strategies plus new topics: AI coding database, learning how to code, prompt engineering) for client meeting
- Suleman will build an automated Google Sheet with Google Search Console API integration for auto-populating weekly performance metrics; Looker dashboard is a secondary option if needed

---

## Key Topics

### Current Reporting Process

  - George manually pulls data from Google Search Console (GSC) weekly
  - Tracks metrics like articles assigned, published, indexed, impressions, and clicks
  - Uses Notion for documentation and ROI calculator for forecasting
  - Process is functional but time-consuming and lacks forward-looking projections

### Content Performance Analysis

  - Augment Code content (/guide section) showing strong early results despite low CTR:
      - ~10,000 impressions, ~100 clicks in under one month
      - Average position of 8 (page 1-2 results)—excellent for new content; typically see page 2 ranking for new content in first month
      - CTR started high then stabilized at ~0.7%, which is normal performance
  - Top performing query: "108 top AI engines for auditing code at scale" with 2.3 average position but low click volume
  - Other tracked queries: "Augmented code competitors," "AI for large code bases," "Best AI code date" (partially captured)
  - Opportunity: Optimize page titles for higher CTR on high-impression, low-click queries to improve conversion

### Reporting Automation Solutions

  - Dave suggested two main options:
    1.  Google Sheets with GSC API integration for auto-populating data
    2.  Looker dashboard for visualizing weekly performance
  - Suleman to assist in building automated reporting solution
  - Goal: Eliminate manual data entry and provide rolling weekly view of key metrics

### Content Strategy and Forecasting

  - Dave to create 12-month content forecast for Augment Code by Wednesday
  - Will use competitor data to identify winnable traffic opportunities
  - Forecast to include current strategy plus potential new topic areas:
      - AI coding database
      - Learning how to code
      - Prompt engineering
  - Augment Code open to aggressive growth strategies with clear ROI

### Additional Initiatives

  - Augment Code considering $10k investment in backlink strategy campaign
  - Targeting rankings for "AI coding" and 2-3 other keywords
  - Weekly reporting crucial for stakeholder updates

---

## Action Items

**Dave Capone (GrowthX)**
- Create 12-month data-driven content forecast for Augment Code. Include current strategy plus new topics (AI coding database, learning how to code, prompt engineering). Use competitor traffic data to identify winnable keywords. Deliver by Wednesday morning for client meeting.
- Add context in Slack chat with Suleman and George about creating Google Sheet with Google Search Console API auto-updating integration for weekly Augment Code reporting.

**Suleman (GrowthX)**
- Develop automated reporting solution: Google Sheet with Google Search Console API integration for weekly auto-population of Augment Code metrics (articles assigned, published, indexed, impressions, clicks).

---

## Transcript
**George Haikal:** You're muted.

**Dave Capone:** Hey, man.

**Dave Capone:** Sorry about that.

**Dave Capone:** There was traffic on the way back, and yeah, it's tough.

**Dave Capone:** Usually we have, you know, he goes to therapy on Mondays, and we don't have school yet, so that won't start until next week.

**Dave Capone:** So usually I have, like, transportation taken care of for this, but, like, this week it was just a  show.

**George Haikal:** Dude, no problem at all, man.

**George Haikal:** Yeah, man.

**George Haikal:** I get it.

**George Haikal:** I get it.

**George Haikal:** Cool.

**George Haikal:** How's everything else going?

**Dave Capone:** It's going.

**Dave Capone:** I got a lot of projects up in the air that I'm trying to get done this week.

**George Haikal:** That's good.

**Dave Capone:** And I think it follows you around like crazy.

**Dave Capone:** That's awesome.

**George Haikal:** I'm fixing my chair.

**Dave Capone:** You the only one in the office today?

**George Haikal:** Marcel and Daniel are here, too.

**George Haikal:** Cool.

**George Haikal:** They're at a meeting right now, but.

**George Haikal:** My day is usually pretty slow on Fridays, very slow.

**George Haikal:** Wednesdays, I'm from home.

**George Haikal:** So, not too bad at all.

**George Haikal:** Cool.

**George Haikal:** So, I was on a call with Jason earlier today, and he showed me some of the work he did for Abnormal.

**George Haikal:** And basically, what I wanted to do is I just know there's a better way to be doing the reporting that we're currently doing for Augment Code on all of the editorial progress that we're making.

**George Haikal:** And so, I kind of wanted your thoughts on, like, how you could help, because right now it's super manual.

**George Haikal:** I'm just going to Google Search Console, pulling in the new numbers for the week.

**George Haikal:** And I made, like, a separate ROI calculator that kind of forecasts out what we think the predictions are, but we don't really even use that week-to-week anymore.

**George Haikal:** That was more just to sell.

**George Haikal:** And so, there's a better way to be tracking, like, or forecasting or projecting out, like, where we're at now versus where we want to go, basically.

**George Haikal:** Right.

**George Haikal:** Thank

**George Haikal:** And so I think you did a good job for that for Abnormal, and I wanted to see if there's any way that you could help us here with Augment code based on the way we're currently working.

**Dave Capone:** Yeah, so I saw with Augment, we have dashboards, so we can use Looker to kind of pull the weekly numbers and stuff, so I can pull together a Looker dashboard to get all that information in there.

**Dave Capone:** Do you know if we have access to their, like, Google Search Console and analytics data?

**George Haikal:** Yeah, we do.

**Dave Capone:** Okay, so that's an easy fix where we can, like, put weekly performance in a quick dashboard for folks so they don't have to pull that every week.

**Dave Capone:** We can literally just, like, have the dashboard, you know, show week-over-week performance, and it could be something simple for them to do.

**George Haikal:** So here, yeah, look what we're currently doing.

**George Haikal:** Pulling up my screen.

**George Haikal:** Let me show you what we're currently doing.

**George Haikal:** So we have broken down, like, what we're actually, the lanes we're executing on, right?

**George Haikal:** And then we meet every week.

**George Haikal:** Link to the meeting is what we're going to talk about, where some manual stuff is pulled, like the highlights.

**George Haikal:** The highlights for the guides page and then for the MCP directory. Right now I'm pulling screenshots.

**George Haikal:** And then we have the newsletter stuff, which you can't help with right now, I'm assuming.

**George Haikal:** then scrunch is just linked because there's no better way to do that than we haven't found yet.

**George Haikal:** And then this is the work stream progress track.

**George Haikal:** This is where tracking, like, our weekly goals for editorial and programmatic.

**George Haikal:** And monthly, if we hit it or not.

**George Haikal:** And this is how I'm tracking.

**Dave Capone:** It's super manual right now.

**George Haikal:** That's fine, because we just started and we're ramping up numbers, so it's good to track week over week. This is how I'm doing it: tracking by week—articles assigned, what's published, what's indexed, pages getting impressions, pages getting clicks—and I'm literally just going to Google Search Console to pull all that.

**Dave Capone:** Ouch.

**George Haikal:** Make sure I already have it saved here.

**George Haikal:** And it's super easy, because all of our stuff for augment code is under this hidden slash guide section, everything we're posting for them, so the filtering is super easy, it's literally just search results.

**George Haikal:** It's pretty sick, as you'll see.

**Dave Capone:** Oh, yeah.

**George Haikal:** In less than one month.

**Dave Capone:** Isn't that pretty nuts? Just under 100 clicks and almost 10,000 impressions. That's pretty good.

**George Haikal:** Obviously, they have a massive brand, but we have, like, full-time.

**George Haikal:** They're not even checking the stuff we're writing.

**George Haikal:** And so it's, like, way easier for us to, like, we're doing 30 articles per week now for them.

**Dave Capone:** Just a big number.

**George Haikal:** But that's pretty good, right?

**George Haikal:** We're seeing what's working, which is the comparison pages.

**Dave Capone:** Oh, I didn't include that.

**George Haikal:** Everything's kind of looking good.

**George Haikal:** So, yeah, this is kind of how we're already working.

**George Haikal:** And so any way to make this better would be super, super, super helpful.

**George Haikal:** Also, this is crazy—20,000 impressions.

**Dave Capone:** So if you click up on the top right, you have position and CTR. Yeah, so it looks like CTR started high, then kind of became standard.

**Dave Capone:** It looks like CTR flatlined at 0.7%, which is normal. Impressions are still high. Average position is about 8, which is really good—typically you'd see page 2 rankings for new content, and this is less than one month in.

**George Haikal:** Basically one month, less than one.

**Dave Capone:** Yeah, that's actually really good for one month.

**Dave Capone:** So if you see 20,000 impressions and 39 clicks, your average position is six—you're in the middle of the page. That's a 0.2% CTR, which would indicate to me that I'd look at the page title and see if there's any way to make it more clickable to entice a click.

**Dave Capone:** So that one's working. You can actually click on that and show the keywords—double click and hit "queries" there. We can see what query is actually driving traffic if you sort by impressions.

**Dave Capone:** So that one is "108 top AI engines for auditing code at scale." You're at position 2.3 on that, but you're not getting clicks on that stuff. Let me look at the clicks—"Augmented code competitors," "AI for large code bases," "Best AI code date." That's interesting. So it's almost like we should take a look at the page title of that one and see if it can improve performance. But from a reporting standpoint, everything we do is pretty standard.

**Dave Capone:** So if you needed help filling out that information on your Notion page, I don't think there's an API for Notion to pull Google Search Console data directly. You could replicate it in a Google Sheet with the Google Search Console API and then copy-paste it into Notion, which might work and save you some time.

**George Haikal:** But I'm just trying to think of ways to save time. I mean, it doesn't have to be Notion, right? There's just a better way to do it all.

**Dave Capone:** You could create a dashboard with all those data points that refreshes every week. It could be a rolling weekly view of all those things to avoid having to manually enter that information.

**George Haikal:** And then also, the forward-looking projections are pretty important. I can show you what I tried making for that.

**Dave Capone:** So Suleman can help with that part.

**George Haikal:** The forward stuff, I could probably help with it. Let me show you what I have. There's a bunch of inputs: average visits per page, percent of aging in traffic. Investment is 50K, but for editorial it's only 30K.

**George Haikal:** So this is good at a high level, but it doesn't really show actuals that well. It was useful when we wanted to sell this—showing long-term revenue and how many potential customers could come from it. But I think what you did for Abnormal (Jason showed me today) is different. I'm not sure if I have access to it.

**Dave Capone:** He pulled it up on his screen. Yeah, so what I do with this forecast is I take actual search volume data from competing sites. I get all the traffic from your four or five competitors, break that down into winnable traffic, and then forecast a content plan to build that competing content over a year—12 months. It can be anywhere from millions in search volume with 50-100 articles per month. It's really up to you. But that gives you a good baseline: if we invest in these topics over this period with X dollars, here's our ROI. I did that for Jason. I can do that for Augment Code. We could take the current strategy and add more pages to plan the next 12 months of content. With current topics plus new silos or new topics to go after, how aggressive do they want to go? What's their goal?

**George Haikal:** As aggressive as possible. Right now we're pitching a backlink strategy campaign where we're trying to rank for "AI coding" and two or three other keywords. They're going to invest $10K just to attempt that. Augment Code has a ton of money, but they also want to see a clear ROI. They're really focused on week-over-week reporting because the stakeholder has to answer to people as well.

**Dave Capone:** Yeah, so the week-over-week stuff, I'm pretty sure Suleman can help with building that. For the forecast, he could do a Google Sheet if you wanted to, or we can build a dashboard in Looker. If you give me a screenshot of your current layout, I can put time together for the three of us to talk through it.

**George Haikal:** Oh, just this. It's super simple. I manually pull the data.

**Dave Capone:** You want to just put it in the chat with us three?

**George Haikal:** Yeah, that's fine.

**Dave Capone:** And then that'll be something he can knock out. It shouldn't be too hard for him to do. Even if it's in a Google Sheet, we can use the Google Search Console API for Google Sheets, which would auto-populate all this stuff for you. You don't even have to worry about it—it'll just pop in there. The forecast stuff would probably depend on what you want. Do you want existing strategy plus new strategy, or just all new topics to go after?

**George Haikal:** So right now, based on what's working—comparing pages, we're putting all our focus onto those moving forward. We're following those signals based on the content inventory we started with.

**Dave Capone:** Yeah, we could do a whole AI coding database section, learning how to code, prompt engineering articles, all sorts of stuff.

**George Haikal:** Yeah, we're already running pretty wild in a good way. So yeah, anything that can help inform more of this is helpful. We have some constraints the next two weeks, but it's pretty open moving forward. We're going to try the backlink campaign and other things. Any new strategy informed by data is going to be helpful, and we can pivot based on that.

**Dave Capone:** Okay, let me get some numbers on Augment Code and get a good baseline of how much volume I think we could probably go after. When do you need something by?

**George Haikal:** By Wednesday morning. I didn't tell the client we're doing this—it's just a nice-to-have for them. Is that too tight of a timeline?

**Dave Capone:** I can make it work. That'd be sweet.

**George Haikal:** Then I can get Suleman in if you want to put us in a chat—us three.

**Dave Capone:** Yeah, I'll talk to him. Where's the chat?

**George Haikal:** Internal Augment Code.

**Dave Capone:** Got it. Yeah, I'll add context to that and let him know we need something in a Google Sheet that's easy to update, with auto-updates using the GSC API. Do you also need that by Wednesday? Because that might be pretty tough to get.

**George Haikal:** No, I can manually update the numbers by Wednesday.

**Dave Capone:** All right. So I'll get to work. I'm going to knock out two audits, and once I get that done, I'll knock this out. So probably tonight sometime or tomorrow morning.

**George Haikal:** Sweet, man. I appreciate it. Is the audit process that you're going through recorded?

**Dave Capone:** The audit process will—I have SEO office hours on Wednesday that I'm going to record. I'll go through the basics of the audit.

**George Haikal:** Cool, man. I'll join if I can. If not, I'll catch up on the recording on Wednesday. Sounds interesting. All right, man. Thank you. Appreciate it.

**Dave Capone:** Yep.
