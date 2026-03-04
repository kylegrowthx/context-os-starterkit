# Ramp<>GrowthX Weekly Check-In

<metadata>
date: 2025-07-09
time: 18:01 UTC
duration: 15 minutes
organizer: vivek@growthxlabs.com
participants: Luke Tubinis, Matt Angelosanto, Victoria Naef, Vivek Shankar, Mara Leighton
fathom_recording_id: 73160929
fathom_url: https://fathom.video/calls/346248428
share_url: https://fathom.video/share/XYStcvN1ku73FNcUkWXAATW3Wf7yxuUc
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

Ramp and GrowthX reviewed blog performance metrics showing steady overall traffic with targeted declines in some state-specific pages, and advanced their automated vendor page publishing workflow to testing phase with a new daily sync mechanism. The team discussed content refresh strategy, noting that high-performing content like the managed travel post may benefit from keyword expansion rather than full rewrites, and committed to exploring optimization solutions with the engineering team. Immediate next steps include testing the automated publishing workflow next week, publishing underpages by July 14th, and creating data wrapper IDs for three new vendor categories.

---

## Context

Ramp is an expense management platform providing spend visibility and automation. GrowthX works with Ramp on content strategy and SEO, focusing on blog performance, vendor page optimization, and technical implementation of automated content publishing workflows. This weekly check-in is part of the ongoing client management cadence, with Vivek Shankar (GrowthX) leading the update on blog metrics and publishing status while collaborating with Luke Tubinis and Victoria Naef on technical implementation details.

---

## Relevance

- **To GrowthX Delivery:** Automated vendor page publishing workflow is now in testing phase with daily syncs and draft mode testing — a significant scalability improvement for similar client work. New "vendor spend data" object architecture on pages demonstrates data integration best practices worth documenting for future projects.
- **To CheckThat:** Managed travel content ranking top three for major keywords with strong AEO (Answer Engine Optimization) visibility — first citation in answer engines is retained. Raises questions about keyword expansion strategy versus content refresh for high-ranking pages.
- **To GrowthX Business Development:** Account is healthy and progressing well. Ramp team engaged on technical details and collaborative problem-solving. Opportunity to expand into refresh optimization services if GrowthX can build programmatic meta-tweak solutions for high-performing content.

---

## Overview

- Blog performance stable; slight drop in deep pages (possibly seasonal)
- New automated publishing workflow for vendor pages developed; testing phase begins
- Content updates: AI batch pages delayed due to data wrapper issues; Salesforce pages on hold
- Refresh strategy for high-performing content needs refinement to avoid potential negative impacts

---

## Key Topics

### Blog Performance Review

  - Overall performance steady; no major changes or alarming trends
  - Deep pages: slight drop in sessions (potentially seasonal)
      - Montana, Kansas, New Mexico lost most traffic
      - Montana: unusually high number of .gov pages in SERPs
  - Expense category pages stabilized
  - Tuning pages:
      - Increased views and sessions
      - Key contributors: "assets vs liabilities" and "NPV log"
      - "Budget variance analysis" gained significant sessions
  - Treasury pages: slight decline from previous week
  - Vendor pages: generally slow week
  - New pages:
      - Increasing volumes leading to more sessions
      - "Notion vs Smartsheet" generated most clicks
      - "Versus" pages outperforming alternatives and overviews

### Automated Publishing Workflow

  - Test workflow developed for vendor pages (starting with overview pages)
  - Testing strategy:
      - Create drafts by appending "draft." to the ID
      - Use actual vendor data for testing
      - New sync process runs daily, publishes the next day
      - New "vendor spend data" object added to vendor pages
  - Team to test and report back next week

### Content Updates

  - Editorial content on schedule for the week
  - Underpages:
      - Few blockers encountered
      - Publishing shifted to Friday, July 14th
  - Zendesk articles on hold
  - Salesforce pages unpublished/in draft status
      - Action: Remove Salesforce from assigned category to hide data block
  - AI batch: Mistral AI data wrapper issue to be resolved
  - Pats of Ender Pages:
      - One batch publishing today (live overnight)
      - BigCommerce and remaining AI pages to be published by tomorrow

### Content Refresh Strategy

  - Concern raised about refreshing high-performing content (e.g., managed travel post)
  - Current refresh flow more suited for underperforming articles
  - Potential improvements:
      - Consider average rank in Google Search Console
      - Focus on expanding keyword opportunities for high-ranking content
      - Engineering team to explore solutions for meta tweaks on well-performing content

---

## Action Items

**Vivek Shankar (GrowthX)**
- Test automated publishing workflow for vendor overview pages using draft mode
- Publish underpages by Friday (July 14th)
- Address Matt's edits on the refresh blog
- Schedule new batch of pages for next week
- Discuss with engineering team about optimizing well-performing posts (e.g. managed travel)

**Victoria Naef (Ramp)**
- Create data wrapper IDs for 3 new categories by end of tomorrow

---

## Transcript

**Victoria Naef:** Hi, Victoria.

**Victoria Naef:** Hello.

**Victoria Naef:** Hey, Luke.

**Vivek Shankar:** Hi.

**Vivek Shankar:** All right, so this is explaining Nika unfortunately he kind of fell sick through the day, so that's why we were a bit delayed in sending out the agenda. Just sent it, so really sorry about sending it late. I'm just going to walk through it real quick.

**Vivek Shankar:** So this is a performance review for the blog pages. Overall performance, we didn't see any major changes or anything alarming to report this week. Blog pages were pretty much steady. For deep pages, we saw a bit of a drop in sessions. We're still waiting to see if this was seasonal or not, so we think it is seasonal so far. There's no major changes in terms of positions, et cetera. Generally speaking, we saw these three states lose the most: Montana, Kansas, and New Mexico. Something curious about Montana was that they seem to have far more .gov pages than the average state. There was, like, four or five different .govs showing up in the first few results, so just pushing everybody else down.

**Vivek Shankar:** Expense category for a change stabilized, so no news here. We're just kind of continuing to watch this. With the tuning pages, we saw a jump in the number of views, a little jump in sessions as well. The major contributors came from assets versus liabilities and the NPV log. For the second batch, budget variance analysis gained a lot of sessions, which was what accounted for the jump in sessions. It's been a bit volatile lately, so we're just observing this, seeing if there's any changes we need to make or recommend.

**Vivek Shankar:** There was a slight decline in treasury pages compared to last week. Again, no major changes in positions. Generally seemed like a slow week all around with the vendor pages. With the new pages, as the volumes are increasing, we are seeing more sessions. Notion versus Smartsheet gave the most clicks, and generally speaking, we're seeing higher number of sessions of the versus pages compared to the alternatives and overviews, so it kind of makes sense from an SEO perspective.

**Vivek Shankar:** So that's the overall performance review. The main thing is a pretty big update we have. We have developed a test workflow to automate publishing the vendor pages, so we've done the overview page so far. Wanted to check with you as to what's the best way to test this, because we don't want to mess up the actual data. Is it possible to set up some kind of a dummy vendor within your CMS so that we can test it on there and see whether the publishing is working or not?

**Luke Tubinis:** We're just creating drafts with the automatic publish stuff we use.

**Vivek Shankar:** We just create drafts?

**Luke Tubinis:** Yeah, yeah, you just append "draft." to the ID.

**Vivek Shankar:** So you can create whatever you want.

**Luke Tubinis:** Just create drafts.

**Vivek Shankar:** But the thing is, we need the data as well. Just want to check, like, if we use actual vendor data, will that break something on your end?

**Luke Tubinis:** We're hopefully syncing. We have a new way of getting data over, which is automatic, which will be great. So what will happen is you'll create the drafts. The sync runs every day, and then we'll publish the next day. You'll notice on the vendor object, there's a new vendor spend data object on the vendor page itself. You don't have to do anything. If you just create the new vendor, the sync will pick up the new vendors. And if we have the vendor on the source, it'll hopefully match and sync the data over. And then we'll publish.

**Vivek Shankar:** So if we manually create something like "Notion test," will it still pull in actual Notion data? It's not going to break anything, right?

**Luke Tubinis:** Currently, if you just choose in the Snowflake vendor field, if you just choose any vendor, it'll pull in data. Hopefully it doesn't unpublish. I'm not entirely sure on that. But if you don't publish, it'd be fine.

**Vivek Shankar:** OK, we'll leave it on draft then just to make absolutely sure. OK, so we will test that through next week and we'll let you know how it goes. So like I said, so far we're doing the overview pages, which I think is really the hardest part. So once we do that, I think the versus and the alternatives should be a lot easier to get through because we already have the data from us.

**Vivek Shankar:** The editorials are on schedule for this week. For these underpages, Nika just wanted to note there were a few blockers. Victoria, we were going back and forth on that. So the publishing for those, we'd like to shift it to this Friday. Hopefully it should be done by today and tomorrow. We're already working on it, but just to hedge ourselves, mentioning July 14th.

**Vivek Shankar:** Yeah, we put the Zendesk articles on hold. The Salesforce pages are also unpublished or in draft status. And then for the AI batch, the Mistral AI data wrapper was missing. So that's the blocker over there. And generally, I just wanted to check whether there's anything we can do for the Salesforce or if for now we just leave it as is?

**Victoria Naef:** For the Salesforce, for now, just leave it as it is. What we're doing is we're removing Salesforce from the category that it's assigned. So this way that data block won't appear on the page. So yeah, just hold it for now. And which blocker did you say you have for the AI pages?

**Vivek Shankar:** I think Mistral was missing the data wrapper. You can check the spreadsheet, but I remember Nika was telling me this is where the blocker was.

**Victoria Naef:** It should be there. Yeah, it's there.

**Vivek Shankar:** So I will check that. Okay. We'll add that to the queue as well. And yeah, so here we have the AI batch pages, so we're publishing one batch today. They should be going live basically overnight, and then hopefully by tomorrow we should have the remaining, the BigCommerce pages and the other AI pages should be published by this time tomorrow.

**Vivek Shankar:** And then, yeah, Matt noted your edits on the refresh blog, so we will address those as well this week. And yeah, generally, those are the updates. And Victoria, not on the agenda, but we will schedule the new batch of pages for next week, as well as update you on the publishing status.

**Victoria Naef:** That sounds good. And I'll create the data wrapper IDs for the three categories that you guys just delivered by the end of the day tomorrow. For this batch you're planning to start publishing next week, right? Just to make sure.

**Vivek Shankar:** Yes. Okay. All right. Good. That was pretty much it.

**Matt Angelosanto:** Yeah, sorry. The only thing I wanted to mention was on one of the refreshes that I took a look at earlier this week, the managed travel post. I'm wondering if, you know, thinking back to when we initially looked over that sheet to approve or disapprove whether we wanted to refresh. The posts, we were looking mostly at, I believe, clicks, right? And so I've just been kind of spot checking the posts as we've been reviewing to see where are they currently ranking? Like, do we have room to improve?

**Matt Angelosanto:** And on the managed travel posts for most of the major keywords that we were targeting, we're ranking in the top three, and we have the first citation in the AO. So the only reason why that's a concern for me is that one of the KPIs that we report out on is share of voice. And so having that level of visibility on that keyword is an overall positive for our share of voice, right? And so rewriting it from scratch may not yield results in terms of clicks because we don't really have anywhere to go on the page.

**Matt Angelosanto:** So I'm wondering, if there's a way we can account for that looking ahead, if we do another batch of these, right? Like, do we look at average rank and then try to dig in a little bit there? Basically just trying to balance the need for this to be more programmatic versus making sure that we're not potentially shooting ourselves in the foot.

**Vivek Shankar:** Yeah, it's a good question. So the refresher flows that we have right now, they're more tuned to work for articles that are not performing well. The ones that are already performing well that maybe need a few meta tweaks, et cetera, we don't have a huge use case for that as yet. We're still working on it, mainly because the majority of refreshers we've been focused on, even for other clients, have been zero traffic, not ranking anywhere, that kind of thing.

**Vivek Shankar:** It's something we could certainly look at. We can take it to our engineering team and see, okay, we don't need a full refresh, just a few meta tweaks. I think one of the reasons we also haven't done that is because technically speaking, it's a bit of a heavier lift because if something already works well, how do you figure out what is not working? So we can certainly take that to our engineering team and see whether we can build something out.

**Vivek Shankar:** For the short term, I think we can focus on blogs that are absolutely not performing. I think that might be a better use of resources now as opposed to blogs like these.

**Matt Angelosanto:** Yeah, I mean, I think the fact that it showed up on your end at all means that it wasn't really performing, right? But the thing that I want to try to account for is ranking, right? Like we could be ranking number one and it might not be driving any traffic. Which is what it is, but we don't really have anywhere to go from there. So if we could also take a look at average rank in GSC, that would be helpful.

**Vivek Shankar:** Maybe. So are you saying, for that particular blog, I think when you ran those analyses, we focused mostly on declining traffic or very low traffic. So for that particular blog, sometimes what happens is it's ranking in the top three for a bunch of keywords, but maybe those keywords don't have good search volume. So I think the expansion, maybe the way to improve that would be to see, okay, is there any opportunity for a higher volume keyword? And look at it that way, instead of looking at it from just the content perspective, which is what we're doing right now.

**Vivek Shankar:** So that's the only idea off the top of my head. But yeah, we'll take it to engineering and see what we can put together and hopefully have an answer for you.

**Matt Angelosanto:** All right. Okay, cool. Yeah, appreciate that.

**Vivek Shankar:** That's pretty much it. Mara, was there anything?

**Mara Leighton:** Sorry, everyone, I'm joining a little bit late. I had another call run over and couldn't leave earlier. But no, nothing huge to share. If there are any lingering questions, please feel free to ping me. Always available to hop on a call. Any other questions that the group might have that we should spend time on?

**Vivek Shankar:** Before that, just want to let you know I'll be out of office next week. But Nika is going to be here and Mara is going to be here. So I'm handing it over to Mara in case there was anything.

**Mara Leighton:** Cool. All right, great.

**Vivek Shankar:** Thanks, everyone. Nice to see you.

**Mara Leighton:** Thank you. Bye.
