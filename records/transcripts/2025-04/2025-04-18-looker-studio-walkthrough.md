# Looker Studio Walkthrough

<metadata>
date: 2025-04-18
time: 02:16 UTC
duration: 5 minutes
organizer: sydney@growthx.ai
participants: Sydney Go
fathom_recording_id: 58012135
fathom_url: https://fathom.video/calls/280099920
share_url: https://fathom.video/share/1NWh1ydusy321ybwERMmayNd3kJe-X45
source: fathom
enriched_on: 2026-03-04 14:30 UTC
</metadata>

---

## Summary

Sydney walked through a custom content performance dashboard she built using Looker Studio that aggregates data from Google Search Console, Google Analytics, and Ahrefs to track blog content metrics (impressions, clicks, CTR, rankings, and organic traffic). The dashboard automates weekly reporting with manual copy-paste on Mondays to keep data static, and clients can view week-on-week performance and filter by recently published articles. Current limitations include Ahrefs accuracy issues for keyword rankings and the need to automate the weekly data refresh process.

---

## Context

This was a solo walkthrough recording where Sydney demonstrated a dashboard built for GrowthX clients to track their content performance. The dashboard integrates multiple Google products (Search Console and Analytics) with Ahrefs to give clients visibility into how their published articles are performing in organic search. This is part of GrowthX's content marketing services where the company helps clients measure the ROI of their content strategy.

---

## Relevance

**To GrowthX Delivery:**
- Client-facing dashboard using Looker Studio as the visualization layer — a replicable template for content performance reporting that can be scaled to other clients
- Identifies process bottleneck: manual weekly copy-paste step to lock values could be automated with Apps Script
- Highlights Ahrefs limitations for keyword position tracking — may need to evaluate alternative data sources (SEMrush, Moz, DataBox) or build custom lookup

**To CheckThat:**
- Dashboard focuses on organic search metrics (impressions, rankings, CTR) — CheckThat could enhance this with AI visibility data showing how clients rank in AI search results (ChatGPT, Claude, Gemini) alongside traditional SEO

**To GrowthX Business Development:**
- Dashboard is a strong proof point of GrowthX's ability to measure content outcomes — useful for new sales pitches and renewals
- Weekly automated reporting improves client experience and engagement with the GrowthX relationship

---

## Overview

- Custom dashboard integrates data from Google Search Console, Analytics, and Ahrefs to track content performance metrics (impressions, clicks, CTR, rankings)
- Automated weekly reporting process feeds into a Looker studio visualization for easy client access
- Current limitations: Ahrefs data accuracy issues, manual steps for weekly updates, ongoing refinement of branded keyword filtering

---

## Key Topics

### Data Sources and Integration

  - Primary sources: Google Search Console, Google Analytics
  - Secondary source: Ahrefs (currently used for backlink data, accuracy concerns noted)
  - Custom formulas pull data from these sources into a master spreadsheet
  - Google Search Console data retrieved using "Search Analytics for Sheets" extension
  - Filters applied to focus on blog content and remove branded keywords

### Metrics Tracked

  - Impressions, clicks, CTR (Click-Through Rate), and average position from Google Search Console
  - Page views and organic traffic from Google Analytics
  - Keyword rankings and positions (currently from Ahrefs, seeking improvement)
  - Top keyword position per URL highlighted in the report

### Reporting Process

  - Master report aggregates data from various sheets (impressions, CTR, position, etc.)
  - Weekly data report automatically sums data when date range is complete
  - Manual step: Every Monday, copy and paste values to keep weekly data static
  - Data flows into Looker Studio for visual dashboard creation

### Dashboard Features

  - Week-on-week performance comparisons
  - Filtering for recently published articles (within the last week)
  - Scrollable view of all published articles with associated performance stats
  - Custom date range selection for flexible reporting

### Ongoing Improvements

  - Addressing Ahrefs data accuracy issues for keyword positions
  - Refining branded keyword filtering process
  - Updating and maintaining data accuracy in Looker Studio visualizations

---

## Action Items

- Investigate alternatives to Ahrefs for more accurate keyword position data
- Finalize branded keyword filtering to improve data cleanliness
- Automate the weekly data copy-paste process to reduce manual work
- Update Looker Studio dashboard with latest refinements and branded keyword exclusions

---

## Transcript
**Sydney Go:** Hey, team, so I just wanted to show you how this recording dashboard works really quickly.

**Sydney Go:** So this is the Looker Studio dashboard, and this is all our growth and performance with impressions, clicks, CTR, average position, whatever.

**Sydney Go:** So what I've done here is—sorry, the window I'm using.

**Sydney Go:** So what I've done here is, I've set up formulas in this page to pull from data that I get from Google search console.

**Sydney Go:** Data is also Google Search Console, Google Analytics, and Google Analytics data.

**Sydney Go:** Backlink data currently is from Ahrefs, so it's not as accurate as I'd like it to be, but I'm working on figuring that out.

**Sydney Go:** But anyway, so here what I've done is impressions, clicks, and CTR will go to

**Sydney Go:** Google Search Console data, then the way that I pull this is I go to search, make sure this one, tools, extensions, Search Analytics for Sheets, open the sidebar.

**Sydney Go:** And then basically I do a Search Console request.

**Sydney Go:** So I set the properties, and then change up the dates—whatever, I'm not going to do that right now, just in case.

**Sydney Go:** And then what I'm going to do is group dimensions by page and query.

**Sydney Go:** And then I added a filter.

**Sydney Go:** So I want it to have "blog," then I added a query filter.

**Sydney Go:** Sorry, let me just copy and paste.

**Sydney Go:** And this one does not want to match all branded keywords.

**Sydney Go:** Query doesn't match.

**Sydney Go:** This one contains.

**Sydney Go:** And then I ask it to pull keyword data from the sheet I set up for it.

**Sydney Go:** So that it should retrieve all of it.

**Sydney Go:** And then all of this information should now feed the master report.

**Sydney Go:** So for example here, this, the full URL you can find it here.

**Sydney Go:** Where is it?

**Sydney Go:** So this ranking at number 86 and I have it set up so that it pulls the one we're ranking the highest for per URL.

**Sydney Go:** So this one for example, that one's the same.

**Sydney Go:** So and then I do it for all of the sheets.

**Sydney Go:** Impressions, CTR, average position all come from this sheet. Clicks and CTR position, pages and organic traffic from Google Analytics views, then organic.

**Sydney Go:** I have it set up so that it filters for the session medium position. Keyword position is from—oh no, that's wrong, it's a total keyword.

**Sydney Go:** So this is from Ahrefs, and it's not super accurate either, which is why it's all blank for now because I'm still trying to figure that out. Top keyword position, and then I have a weekly data report that basically sums all of the data in here as soon as the date range is past—the date range is past a week from the date in here.

**Sydney Go:** So here I'm still editing these, as you can see, and then every time the week is over, every Monday basically, I just copy.

**Sydney Go:** copy the values in here, and then paste it as a value instead of a formula so that doesn't change and it stays static, and then it shows up in looker looking like this basically.

**Sydney Go:** Sorry, not that.

**Sydney Go:** It shows up in looker looking like this.

**Sydney Go:** I've not updated this.

**Sydney Go:** Updating these branded keyword filters, which is why these aren't done yet.

**Sydney Go:** then, yeah, so it should end up looking like this, basically.

**Sydney Go:** This is set so that it pulls data from the sheet.

**Sydney Go:** If the published date of an article is within the week, then it'll show up within last week, it'll show up here, it's set up for Monday to Sunday, week on week performance, and all of this as well.

**Sydney Go:** Impressions clicks, all of this come from the weekly sheet.

**Sydney Go:** This one comes from the month, the master report, and this also comes from the master report.

**Sydney Go:** Basically, our customers can scroll through all of their published articles and then all of the stats that we pulled for them.

**Sydney Go:** And this is on a week by week basis as well.

**Sydney Go:** Hope that helps.
