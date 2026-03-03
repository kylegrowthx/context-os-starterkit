# Ramp <> GrowthX Weekly Check-In

<metadata>
date: 2025-08-07
time: 18:01 UTC
duration: 14 minutes
organizer: vivek@growthxlabs.com
participants: Vivek Shankar, Mara Leighton, Luke Tubinis, Victoria Naef
fathom_recording_id: 79206880
fathom_url: https://fathom.video/calls/371935530
share_url: https://fathom.video/share/TsZsBFxM3gn8a3PsPxxehZbWydTcKy9b
source: fathom
enriched_on: 2026-03-03 00:00 UTC
</metadata>

---

## Summary

Ramp and GrowthX reviewed Q2 content recovery with strong performance in late fees and cash flow hedge content, and discussed vendor pages where "versus" pages are driving the most traffic with AI being the top-performing category. GrowthX automated vendor overview page publishing and flagged a potential GA4 engagement rate threshold issue and a duplicate content problem on alternatives pages that needs cleanup. Next steps include gathering the next batch of vendor pages for automation testing, preparing an initial plan for using existing vendor data to create granular content by segments/industries, and auditing all vendor pages to remove duplicate alternatives sections.

---

## Context

Ramp is a financial operations platform for companies, and GrowthX is delivering content marketing services to them. This is a recurring weekly check-in led by Vivek Shankar from GrowthX, covering SEO performance metrics and content delivery progress on Ramp's vendor comparison and review pages. The meeting focuses on monitoring traffic patterns across different content categories (blog, per diem, expenses, treasury, vendor pages) via Looker dashboards pulling GA4 and GSC data, discussing automation progress for vendor page publishing, and aligning on the next batch of content refreshes and strategic initiatives around using vendor data for more targeted, granular content by industry segments.

---

## Relevance

**To GrowthX Delivery:**
- Successfully implemented vendor overview page automation in CMS (all manual steps except image generation); alternatives and versus page automation in progress
- Identified duplicate content issue: alternatives section appears both on main vendor page and separate alternatives page, impacting organic performance; audit and cleanup needed
- Looker dashboard provides GA4 + GSC integration for comprehensive traffic analysis; new color scheme and Vendor Cohorts tab added for better reporting
- Ramp procurement articles performing well in targeted cluster, indicating strong demand for vertical-specific content

**To GrowthX Business Development:**
- Ramp's "versus" pages driving 40%+ of vendor page traffic (highest performer), with AI category at top; indicates strong market fit and opportunity for category expansion
- Potential expansion to granular, segment- and industry-level content using existing vendor data; Vivek to present initial plan next week
- Two RefreshPages being delivered, with positive feedback loop on quality and delivery timeline
- Suspiciously high GA4 engagement rates (98-99%) on vendor pages may indicate GA4 threshold configuration issue, suggesting data quality concern to monitor

---

## Overview

- Blog traffic recovered from Q2 losses; cash flow and late fees content performed well
- Vendor pages saw increased sessions, with "versus" pages and AI cluster driving most traffic
- Automated publishing for vendor overview pages implemented; alternatives and versus page automation in progress
- Plan needed for leveraging existing vendor data for more granular content (segments/industries)

---

## Key Topics

### Content Performance Updates

  - Blog: Cash flow hedge vs. fair value and late fees on invoices saw significant jumps
  - Per Diem: Slight session loss (Texas, Florida, Virginia most affected); likely seasonal
  - Expense category: Gained sessions, reversing recent trend; stamp duty, security system, pest control, and signage pages performed well
  - Tuning pages: Stable performance; assets, liabilities, and audit trails continued strong
  - Treasury: Liquidity position report unexpectedly gained clicks
  - Vendor pages: Higher overall sessions; "versus" pages driving most traffic
      - AI cluster highest traffic, followed by content creation and project management

### Looker Reporting Upgrades

  - New color scheme implemented
  - Vendor Cohorts tab added: Shows versus pages driving most traffic, followed by overview pages
  - Alternatives pages underperforming
  - Engagement rates suspiciously high (98-99%); potential GA4 threshold issue to investigate

### Content Refresh and Automation

  - Procurement articles performing well in small cluster
  - Two more pages to be delivered tomorrow
  - Vendor overview page publishing automated, except for image generation
  - Next steps: Test automation with live pages, build out alternatives and versus page automation

### Vendor Page Strategy

  - Plan needed for leveraging existing vendor data for more granular content (segments/industries)
  - GrowthX to present initial plan in next week's call

### Alternatives Page Performance Issue

  - Potential duplicate content problem identified (alternatives section on main page + separate alternatives page)
  - Action: Remove hardcoded alternatives list from vendor pages, update template

---

## Action Items

**Victoria Naef (Ramp)**
- Gather next batch of vendor pages for automation testing
- Review and provide feedback on 2 new RefreshPages being delivered tomorrow

**Vivek Shankar (GrowthX)**
- Prepare initial plan for using existing vendor data to create more granular content (segments/industries). Present next week.
- Audit all vendor pages. Remove duplicate alternatives section where present. Update template if needed.

**Luke Tubinis (Ramp)**
- Review and provide feedback on 2 new RefreshPages being delivered tomorrow

---

## Transcript
**Luke Tubinis:** Good, thanks.

**Vivek Shankar:** How did the QBR session go yesterday?

**Luke Tubinis:** Well, pretty good. Yeah, we've recovered a lot of the traffic we lost in Q2.

**Vivek Shankar:** Okay, I think Mara might join a bit late, so we can get started real quick.

**Vivek Shankar:** Let me share my screen.

**Vivek Shankar:** Okay, so just going through the updates for each category.

**Vivek Shankar:** So we've upgraded our Looker reporting a little bit, so you can see some fancy new colors over here.

**Vivek Shankar:** I'll just run through the Looker report itself in a bit, but just going through the different categories, we saw a jump for the blog page, for the blog pages, the cash flow.

**Vivek Shankar:** Hedge versus Fair Value, that particular block saw the most jump, and calculating late fees on invoices as well.

**Vivek Shankar:** For the Per Diem pages, we were continuing to lose a few sessions over the past couple of weeks now.

**Vivek Shankar:** Texas, Florida, Virginia lost the most.

**Vivek Shankar:** Generally, no change in average positions, but still we're losing a few clicks.

**Vivek Shankar:** So far, we think it's seasonal.

**Vivek Shankar:** For the expense category pages, for a change, we had a gain, reversing the trend over the past few weeks.

**Vivek Shankar:** Pretty much every page saw a gain in overall sessions.

**Vivek Shankar:** Stamp duty, security system, pest control, and signage were the most prolific pages.

**Vivek Shankar:** And generally, we saw higher CTRs in this cluster last week.

**Vivek Shankar:** So yeah, good news over here.

**Vivek Shankar:** For the tuning pages, pretty much maintain performance at the usual sort of range.

**Vivek Shankar:** What I'm used to, assets liabilities and audit trails, which have been traditionally the best performers over here, continued their performance for the second batch of tuning pages, budget variance and quarterly taxes gained a few clicks, but generally it was a low week compared to a couple of weeks ago for the treasury pages.

**Vivek Shankar:** Again, a pretty small batch of pages, but you have the liquidity position report, which unexpectedly has been doing quite well, gained a lot of clicks, so we saw good performance there.

**Vivek Shankar:** For the vendor pages, overall, we saw a higher level of sessions.

**Vivek Shankar:** Generally, again, and I'll walk through the Looker just shortly, but generally, you know, in the Looker, we've broken down vendor pages by the type of page as well as the category.

**Vivek Shankar:** So, the versus pages, you know, as we can see from this chart over here, is driving the most traffic.

**Vivek Shankar:** The AI cluster is also the highest in terms of traffic, followed by content creation, and project management for the past month has also been doing quite well.

**Vivek Shankar:** Just hopping over to the Looker, the link is at the top of the agenda over here, so you can just click that at any time.

**Vivek Shankar:** So yeah, we just have the usual tabs over here.

**Vivek Shankar:** We're pulling in data from GA4 and GSC.

**Vivek Shankar:** We weren't sure which of these would be highly relevant to you, so if you do have some requests for additional metrics or additional deep ties, please let us know.

**Vivek Shankar:** The tab over here, Vendor Cohorts, this is where really we're pulling in data on the vendor pages itself.

**Vivek Shankar:** So I've just filtered this for the past month.

**Vivek Shankar:** So as we can see, generally, the versus pages are driving the most traffic, followed by the overview.

**Vivek Shankar:** Alternatives, as we've observed so far, they don't seem to be attracting much attention in general.

**Vivek Shankar:** In terms of the sort of page categories themselves, we have quite a few, but generally AI has been the best performer in terms of overall clicks, followed by content creation, project management, DevOps as well, has been doing pretty recently.

**Vivek Shankar:** We're seeing pretty high engagement rates over here. I was wondering if in your GA4, maybe if the threshold is set a little too low, perhaps.

**Vivek Shankar:** Not sure if, you know, it's not a major reporting metric, I think for these pages, but just wanted to flag that, like we're seeing 98% engagement rates, which is a bit of an anomaly.

**Vivek Shankar:** So just something we wanted to check.

**Vivek Shankar:** But yeah, generally, you know, please do let us know if you wanna see something else in terms of reporting, you'd be happy to build that out.

**Vivek Shankar:** So yeah, I'm gonna stop monologuing. Any questions?

**Victoria Naef:** Are you measuring engagement rate?

**Vivek Shankar:** We're just pulling this directly from GA4. So I think, yeah, we're not applying any filters to it.

**Luke Tubinis:** Yeah.

**Vivek Shankar:** So usually it's set at a minute, I believe that's the threshold, but just looking at these numbers, I'm wondering if, yeah, like DevOps is like 99%, which is over a hundred sessions.

**Vivek Shankar:** So it's quite a lot.

**Victoria Naef:** Could you scroll up a bit back to, this is really helpful, by the way.

**Victoria Naef:** Thank you for putting it together.

**Victoria Naef:** I'm just curious, trying to see if the versus pages, I mean, we have a lot more versus pages than the others.

**Victoria Naef:** If this is the total or if it's like an average per page.

**Vivek Shankar:** The total. So we can build out an average as well.

**Victoria Naef:** Okay.

**Vivek Shankar:** So yeah, that was the performance update in general.

**Vivek Shankar:** Just hopping over the content refreshes.

**Vivek Shankar:** We don't have many URLs in general here, but the procurement articles are generally doing quite well in this small cluster.

**Vivek Shankar:** We are delivering two more pages tomorrow.

**Vivek Shankar:** So yeah, waiting for your feedback and edits on that.

**Vivek Shankar:** Just want to give an update.

**Vivek Shankar:** We have automated the overview page publishing for the vendor pages.

**Vivek Shankar:** There's just one part which is not automated yet, which is the image generation.

**Vivek Shankar:** So generating the two images for each.

**Vivek Shankar:** vendor.

**Vivek Shankar:** We do have that portion of the request in progress.

**Vivek Shankar:** So that part is still manual, but generally we can publish pages into your CMS automatically.

**Vivek Shankar:** We use a few test vendors.

**Vivek Shankar:** So with the next patch, we'd like to get started with like live pages.

**Vivek Shankar:** The process stages the page.

**Vivek Shankar:** It does not directly publish it.

**Vivek Shankar:** So we're still doing a manual review just to make sure that, you know, the QA is good.

**Vivek Shankar:** But yeah, next step there is, you know, whenever we get started with the next patch, we'll test it out in production.

**Vivek Shankar:** And then we're also building out the automation for the alternatives and versus pages.

**Vivek Shankar:** So pretty, pretty good news over there.

**Vivek Shankar:** So yeah.

**Vivek Shankar:** And yeah, following up on that to let us know about the next patch of vendor pages, we just wanted to check in terms of, you know, your plans for the timeline, etc.

**Vivek Shankar:** Just wanted to check up regarding that.

**Victoria Naef:** Yeah, so I'll gather the next vendors, but I also wanted to move, like, at the same time, I wanted to make progress on using the existing data we have there for these vendors and going more granular, as we were talking about, like, with the segments or industries.

**Victoria Naef:** So do you think you could, maybe we can discuss next week, like, on next week's call, like, an initial plan on how you think would be the best way for us to do that?

**Victoria Naef:** Yeah, sure, not a problem.

**Vivek Shankar:** We can, we'll put that together, yeah.

**Victoria Naef:** That'd be great, thank you.

**Vivek Shankar:** And yeah, RefreshPages are coming your way, two of those tomorrow. I'm looking forward to your feedback on the existing ones.

**Vivek Shankar:** So, yeah, that's pretty much it for the update.

**Vivek Shankar:** So, yeah, if there's any other questions, we can answer.

**Luke Tubinis:** What images need to be generated?

**Vivek Shankar:** The review is basically the vendor image.

**Vivek Shankar:** We have two images.

**Vivek Shankar:** It's the image of the logo.

**Vivek Shankar:** So there's a vendor logo, and there's a vendor logo and the name.

**Vivek Shankar:** So it's, like, two images.

**Vivek Shankar:** And it's a bit finicky because I think the background needs to be transparent.

**Vivek Shankar:** It needs to be a certain size.

**Vivek Shankar:** So that's the only part that's manual.

**Luke Tubinis:** I wonder if the alternatives are not doing very well because on the primary review page, we've got an alternative section, and then we've got another, like, we've got alternatives each.

**Luke Tubinis:** And then we've got an alternatives, another H2, like duplicate H2s and like the written part is on the main page.

**Luke Tubinis:** And then like the link itself, the alternatives page is competitors.

**Luke Tubinis:** You know what I mean, Victoria?

**Luke Tubinis:** Which page are you looking at?

**Victoria Naef:** I'm just on active campaign.

**Luke Tubinis:** I could share real quick. I think we could make these changes pretty quickly.

**Luke Tubinis:** So I'm just on the primary active campaign. We've got this alternative section, which I bet is getting crawled quite a lot because that's what LLMs are after. And then we've got this alternative H2, and then the link to the alternatives page is competitors.

**Victoria Naef:** Yeah, we talked about this—not including that section, the one that lists competitors, only leaving the one that's already hard coded. So I think we should, as we move forward, delete that section from the pages that are already live. I think we did that for a few batches at the beginning.

**Vivek Shankar:** Yeah, I remember Nika doing it for one of the earlier batches. I'll check why it wasn't deleted for the active campaign and we'll check the other pages as well, just to make sure the hard coded lists are not in there.

**Victoria Naef:** Yeah, yeah, but good catch, Luke.

**Victoria Naef:** Okay.

**Luke Tubinis:** Yeah, we have to make fixes in the template.

**Victoria Naef:** I'm looking at a few other ones, like 1Password, and they don't have that section. So if you can go through them and see which ones we still have that alternatives section and delete that, that would be great.

**Vivek Shankar:** Yep, we will do that.

**Vivek Shankar:** I think the latest batches don't have it.

**Vivek Shankar:** It's some of the batches in between that I think we missed that.

**Vivek Shankar:** So we will take a look at it and we'll fix it.

**Vivek Shankar:** Cool, awesome.

**Victoria Naef:** Thank you.

**Vivek Shankar:** Mara, was there anything else?

**Mara Leighton:** Sorry to join late again, you guys.

**Mara Leighton:** My call right before this tends to run over.

**Mara Leighton:** And anyway, thank you for starting and nothing else to add.

**Luke Tubinis:** All right, thanks, everyone.

**Mara Leighton:** Good to see all of you. Bye.
