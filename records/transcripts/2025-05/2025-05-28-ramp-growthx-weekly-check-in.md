# Ramp<>GrowthX Weekly Check-In

<metadata>
date: 2025-05-28
time: 18:00 UTC
duration: 24 minutes
organizer: vivek@growthxlabs.com
participants: Vivek Shankar, Mara Leighton, Luke Tubinis, Matt Angelosanto, Victoria Naef, Ali Mercieca, Nika Narimanidze, Kyle Gaudreau, Bisera Stankovska, Abigail Deak, Shaun Hinklein
fathom_recording_id: 65185607
fathom_url: https://fathom.video/calls/310616508
share_url: https://fathom.video/share/6i74Pp75z3yyGa_W3Rd79QsLXcmb46-d
source: fathom
enriched_on: 2026-03-04 12:00 UTC
</metadata>

---

## Summary

Ramp and GrowthX reviewed performance across five page categories: block pages are experiencing a drastic drop in clicks attributed to LLM overviews (185 pages showing up in 2,600 keywords), tuning pages show volatility that warrants another week of monitoring, and treasury pages are performing well with the liquidity position report leading. The teams aligned on scaling vendor pages from the current 22-23/week to potentially 400+ URLs, identifying workflow bottlenecks (Aerox platform constraints and repetitive content review) that GrowthX plans to solve by transitioning to a custom platform in coming weeks. Matt Angelosanto took over the zero traffic page refresh project with a go/no-go cannibalization check in Airtable before rewrites begin.

---

## Context

Ramp is a corporate spend management platform and a key GrowthX client undergoing an ambitious content expansion program. This weekly sync is part of GrowthX's ongoing content delivery engagement, where GrowthX owns content strategy and production for multiple page categories (block pages, tuning pages, treasury pages, and vendor pages). Vivek Shankar (GrowthX) leads the technical execution and reporting, while the Ramp team provides strategic direction and quality review. The conversation surfaces a critical scaling challenge: Ramp wants to grow vendor pages from dozens to 400+ URLs quickly, but GrowthX's current platform (Aerox) requires one-by-one page generation, creating a manual bottleneck despite Sanity's reusable component architecture on Ramp's side.

---

## Relevance

**To GrowthX Delivery:**
- Confirmed need to transition away from Aerox platform constraints; custom platform in weeks will unlock bulk generation workflows and reduce manual content review overhead (currently 22-23 pages/week max, targeting 100+/week for Ramp)
- Zero traffic page refresh is a new content category requiring brand guideline refinement based on first-batch outputs; Matt Angelosanto's review of 5-10 initial rewrites will feed back into production process
- Vendor page production is bottlenecked on content review overhead (sections are reusable in Sanity but content is generated per-page); workflow optimization needed before scaling attempt
- LLM overview impact on block pages (185 pages, 2,600 keywords) requires ongoing performance monitoring; no immediate action but tracking for pattern changes

**To GrowthX Business Development:**
- Ramp is signaling strong intent to expand vendor content footprint significantly (400+ URLs); successful scaling here could strengthen relationship and create expansion opportunity into other page categories
- Willingness to test batch processing of "a couple hundred" pages shows client confidence and appetite for experimentation
- Account health is strong: vendor pages showing upward 4-week trend despite modest absolute numbers (25-26 sessions/week), treasury pages performing well, tuning pages recovering post-refresh

---

## Overview

- Block pages showing declining performance; potentially due to LLM overviews
- Tuning pages experiencing volatility; team to monitor for another week
- Zero traffic pages refresh to begin; Matt taking over project management
- Vendor pages scaling discussed; aiming for significant expansion (potentially 400+ URLs)
- Current workflow limitations identified; GrowthX moving to custom platform in weeks to enable scaling

---

## Key Topics

### Performance Reports Analysis

  - Block pages: Declining performance (185 pages across 2,600 keywords)
      - Drastic drop in clicks, potentially due to LLM overviews
      - More data needed for deeper analysis
  - Tuning pages:
      - GA4 shows dip, GSC data volatile with impression spike
      - No significant drops for individual pages
      - Team to monitor for another week before further action
  - Second batch tuning pages:
      - Post-refresh showing improvement (more sessions/views/clicks)
      - Performance not "super exciting" but better than pre-refresh
  - Treasury pages:
      - Higher performance this week (sessions and views up)
      - Liquidity position report page top performer (\~30 views, 10-15 sessions)
  - Vendor pages:
      - Performance hovering around 25-26 sessions, \~100 views
      - Upward trend over past four weeks

### Content Strategy Updates

  - Zero traffic pages refresh:
      - Matt taking over project management
      - Team to start with low-traffic pages
      - Process: Create separate Airtable tab, use go/no-go system for potential cannibalization
  - Best bank pages: No further edits needed on Ramp's site
  - Vendor pages:
      - Victoria updated statuses for CMS addition
      - Main page to be added in upcoming batch
      - Data wrapper ID to be provided

### Scaling Vendor Pages

  - Goal: Significantly expand vendor page footprint (potentially 400+ URLs)
  - Current max output: \~22-23 pages/week
  - Limitations:
      - Content review overhead due to repetitive section generation
      - Aerox platform constraints (one-by-one page creation)
  - Potential solutions:
      - GrowthX moving to custom platform in weeks
      - Possibility of building custom workflow for scaling
      - Exploring bulk generation options to reduce manual work

### Workflow Optimization

  - Sanity CMS structure allows section reuse, but content still produced individually
  - Team considering new workflow to reduce content review time
  - Exploring possibilities of API integration with Sanity for direct publishing
  - GrowthX to internally review processes for potential bulk generation methods

---

## Action Items

**Matt Angelosanto (Ramp)**
- Review first 5-10 zero traffic page rewrites; refine brand guidelines based on output


**Vivek Shankar (GrowthX)**
- Send list of zero traffic page URLs to Matt via Airtable for review
- Add main pages for vendor content in addition to alternatives/versus pages; complete by tomorrow
- Review content production workflow for vendor pages; consider optimization strategies
- Investigate possibility of API integration with Sanity for direct publishing


**Victoria Naef (Ramp)**
- Provide data wrapper ID for vendor pages to Vivek's team


**Luke Tubinis (Ramp)**
- Provide specific target number of vendor pages to be created in next batch

---

## Transcript

**Vivek Shankar:** Good, thanks. Hey, Mara. Hey, how's it going?

**Mara Leighton:** Hey, Luke, how are you? Good. Vivek, how's the weather in Portugal?

**Vivek Shankar:** It's probably somewhere around 38 Celsius today, so yeah.

**Mara Leighton:** Toasty, yes. That's awesome. In New York, it's like this consistent overcast of ominous rain that hasn't quite broken yet, but whatever, it'll be swamp-like in a few weeks, so I actually shouldn't complain. How's the weather for you?

**Luke Tubinis:** I'm in Maine. Which part of Maine? It's called Bailey Allen's in Casco Bay. Cool.

**Mara Leighton:** That's awesome. I hope you eat a lot of lobster rolls.

**Luke Tubinis:** Hey, everyone.

**Mara Leighton:** Hello. Are we waiting for anyone else, or does it look like we kind of have everyone?

**Victoria Naef:** How's it going?

**Mara Leighton:** I think we have everyone, yeah.

**Vivek Shankar:** Can you just share my screen? So, yeah, just diving into the performance reports for the block pages. And just like a preface to this, I sort of readjusted the grid lines in the background so that they weren't looking as messy. So you might see the sessions line a bit deeper in the graph now just because of the scales being adjusted a bit. Additional data on what's going on over here, unfortunately, it seems to be dropping. The only thing we can think of is perhaps LLM overviews, but even then, the drop seems pretty drastic for that. Generally, compared to last week, SEMrush is now showing even more URLs showing up in AI overviews. Currently, 185 of these pages are showing up across about 2,600 keywords. We seem to be showing up from a bunch of different types of keywords, not all of them connected to expense categories. It helps with visibility for sure, but we definitely have lost a lot of clicks over here, and it seems to be heading downward for now, but we just have to see whether they stabilize at some point. And until we have more data, unfortunately, we can't really dig into this more. So that's kind of where we're at right now.

**Vivek Shankar:** For the tuning pages, we saw a bit of a dip in GA4 data for this week, but then GSC data showed us something else with this weird spike for the impressions. Again, not sure why. GSC has been pretty volatile. So this drop in clicks isn't as drastic as it seems here in GA4. Generally, we think waiting another week just to see if this plays out or if it averages out, as is usually the case between GSC and GA4, is the best move. If this continues, then we'll dig deeper and see whether there's anything that has changed in regards to competitor positions in the SERP. There weren't any significant drops for any single page. It just seemed like a lot of the pages all lost one session here and there, which kind of dragged performance down.

For the second batch of tuning pages, not super exciting performance, unfortunately, but as we can see from this chart, post-refresh we are getting more sessions, views, and clicks on these pages compared to pre-refresh. So generally good news. Obviously, we'd like to see much more, but given where these pages were, we certainly are in a much better position.

The treasury pages saw some higher performance this week, generally higher sessions and views. The liquidity position report page was the top performer, which is interesting because it doesn't seem to have any direct keyword searches in Google, at least not high-volume ones. But generally the pages seem to be in a range of about 30 views and 10-15 sessions or thereabout.

Regarding the vendor pages, we're seeing performance hover around 25-26 sessions and close to 100 views. So we seem to be in this particular range generally, though as we can see over the past four weeks, we seem to be trending upwards, so that's quite encouraging. But yeah, that's generally the overview of all the different page categories. Any questions I can answer about any of this, or any clarifications?

**Vivek Shankar:** I know Matt had mentioned this last week, but for the zero traffic pages refresh, do you want us to go ahead and get started with that? Or is there any internal testing you'd like to run before we begin?

**Matt Angelosanto:** So I'm going to be taking over that going forward. Basically, before we start the rewrites, do we want to take another look at these pages for overlap or cannibalization concerns? Or do we just push it and then address any issues later once we have time to do a deeper dive?

**Luke Tubinis:** Yeah, I think we just want to have really good visibility into what's in the queue and what's been done. So if we tune something and it does really well, it doesn't take from something we're super focused on. I'm thinking Airtable for this, since I don't think others besides Matt will join unless they're working on a specific project.

**Vivek Shankar:** So we can follow the same process we use for vendor pages. We can create a separate tab for these articles and put the list in there with a go/no-go system. If you feel like there might be some cannibalization concerns, you can flag it to us and we'll skip over it.

**Matt Angelosanto:** No, I think that should be fine. The way I have the workflow set up for P2 stuff right now, it shouldn't surface anything that would wind up on the rewrite list, so I'm not concerned about overlap. In terms of visibility into what we're actually touching, I think the GrowthX Airtable is the place to start as the source of truth. Then I was also thinking we should add GrowthX as a publishing team in Sanity so we can look at those posts specifically in Looker and tag them as SEO and GrowthX. That way if we have a report that pulls for those posts, we'll see everything that's been touched.

**Vivek Shankar:** All right. So I can send over the list of URLs, put it in Airtable, and tag you for review. We have those first batch of articles ready.

**Vivek Shankar:** And I just wanted to check in regarding the vendor pages best bank pages. Have you had a chance to look at those? Anything you can change over there?

**Ali Mercieca:** Nothing is needed on the best banks articles on your site anymore.

**Vivek Shankar:** Okay, great. And for the vendor pages, Victoria, I see you've changed the status for a few to be added to the CMS.

**Victoria Naef:** Right. For the previous batch, you guys added the alternatives and versus pages. I'm hoping that for this upcoming batch, we can add the main page as well. I recorded a Loom with details on that. I'll get the data wrapper ID to you, and we should be good to move forward.

**Vivek Shankar:** We'll get on that by tomorrow and finish it off. Thank you.

**Luke Tubinis:** If we were to make 20 times the number of these vendor pages, is there anything preventing that from happening? I'm sure there's many things, but I think this test is going to round out positively, and we'd like to very much expand the footprint. If there's anything you think is very slow that would cause us to need two months to put up 400 URLs instead of a couple weeks, we'd definitely want to hear about it.

**Victoria Naef:** One thing we discussed is the way pages are structured in Sanity. There are reusable sections we add to the main page that don't need to be added to child pages. But right now, the workflow still creates these sections over and over. Maybe we can put together a new workflow that saves time on content review, because right now we're outputting a lot more content than will actually be needed. The maximum we've been able to get per week is around 22 pages.

**Vivek Shankar:** Changing the workflow to have less content to review would increase the number of pages per week.

**Luke Tubinis:** Do you have a specific target number in mind?

**Vivek Shankar:** Luke mentioned 400, but we can give you a better target. We can take it to our engineering team and see if we can build a custom workflow. I'm not sure if it's possible to API into Sanity and directly publish, though we do that quite a bit with Webflow.

**Luke Tubinis:** Anytime our content team speaks about a vendor or includes them in a spend report, we'd want the vendor page up within a business day. For high priority software companies our outbound team is targeting, we'd want them very quickly. For this next batch, we'd like to see what happens if we try a couple hundred at once or within a shorter timeframe.

**Vivek Shankar:** We'll take a look internally and see if we can tweak the flows and generate more. Because like Victoria said, we're following a process where we have to generate these one by one. If there's a way to generate some in bulk with a few clicks, it might help you guys much more.

**Victoria Naef:** What exactly is preventing bulk production versus one-by-one? What would we be losing?

**Vivek Shankar:** It's a limitation of Aerox right now. We have to generate one article per row in the grid. We cannot build a custom workflow on Aerox that creates a batch of pages all at once with a few clicks. We're moving to a custom platform in a few weeks away from Aerox. That's why we could take this to the engineering team and build something custom for you that allows us to scale. We can increase from 22 a week to maybe 30 a week, but that doesn't match your definition of bulk. Truly at scale, it needs a custom workflow, which we can build out and will be in a better position to do in a few weeks.

**Luke Tubinis:** The only solution to go from 30 to 100 is to throw more bodies at the problem.

**Vivek Shankar:** Yes, it's just a limitation of Aerox right now. All right, thanks everyone. I'll follow up with everything else on Slack and get back to you.
