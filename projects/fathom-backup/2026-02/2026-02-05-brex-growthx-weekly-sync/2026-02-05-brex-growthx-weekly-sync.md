# Brex <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-05
time: 20:30 UTC
duration: 31 minutes
organizer: team@growthxlabs.com
participants:
  - Jon Kowieski (Brex, Senior Director of Content/Product)
  - George Haikal (GrowthX, Design/Product Lead)
  - Marcel Santilli (GrowthX, Founder/CEO)
  - Aida Knezevic (GrowthX)
  - Arudyak (Brex)
fathom_recording_id: 120204946
fathom_url: https://fathom.video/calls/556077750
share_url: https://fathom.video/share/_UrPTKGS6BCwdnWZ3hugg2TrYhmwW-jx
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

George presents Charge Finder approval with critical data corrections needed (remove customer IDs and usage metrics for legal compliance), while Jon provides extensive UI feedback on the Resources Hub V1—including requests for "View All" buttons, smaller subtitle fonts, and more prominent CTAs—ahead of required internal design review with Brex's Chief Design Officer.

---

## Context

This weekly sync between Brex (represented by Jon Kowieski, Senior Director of Content/Product) and GrowthX (George Haikal and team) focuses on three major deliverables for Brex's content platform: the Charge Finder tool for identifying transaction charges, a redesigned Resources Hub consolidating all Brex content, and redesigns for the Case Studies and supporting content pages.

Jon raised critical legal and UX concerns with the Charge Finder data that required immediate course correction—specifically removing customer-identifying numbers and metrics that could expose sensitive usage patterns. George acknowledged the feedback and flagged that the team is ready to build and iterate quickly, with Kirkland (likely Kirkland Lemons or a GrowthX developer) gaining repo access to move forward in Brex's system. The meeting also surfaced that the Resources Hub redesign, while strong, will face internal review from Bingo (Brex's Chief Design Officer), requiring comparison documentation and strategic framing to gain approval for a significant site overhaul.

---

## Relevance

- **Content Strategy & Product**: Three major initiatives advancing Brex's content experience—charge visibility, resource discovery, and case study accessibility
- **Legal & Compliance**: Data security and privacy controls embedded in design to avoid exposing customer usage metrics or identifying information
- **Design & UX**: Significant site overhaul including tagging systems, navigation patterns, and layout templates that will cascade across multiple pages
- **Stakeholder Management**: Internal approval workflow highlighted; need to prepare comparison docs and build consensus with design leadership (Chief Design Officer)
- **GrowthX Execution**: Programmatic tool building, multi-week delivery across platform redesigns, and repo collaboration with Brex engineering
- **Content Operations**: Decisions on spend trends categories, outdated content removal, and cross-page template alignment

---

## Overview

- **Charge Finder Approved:** The tool is approved for development, but with critical data corrections. The team must remove customer-identifying numbers from charge variations and delete the "customers charged per month" metric to avoid legal risks.
- **Resources Hub V1 Reviewed:** The new hub UI was reviewed. Key feedback includes adding "View All" buttons to content sections and preparing for a potentially contentious internal review, as the design represents a major site overhaul.
- **Case Studies Page Redesign:** The current page will be redesigned to fix its poor UX and add a requested "industry" filter, creating a new template for other content pages like eBooks.

---

## Key Topics

### Charge Finder Tool

  - **Status:** Approved for development.
  - **Critical Data Corrections:**
      - Remove customer-identifying numbers from charge variations (e.g., `AMZN MKTPL IND-PRIVIA`).
      - Delete the "customers charged per month" metric.
      - **Rationale:** To avoid legal risks and provide a cleaner, more accurate user experience.
  - **Design Feedback:**
      - Approved the overall design, layout, and "Instantly" orange color.
      - **Suggestion:** For large companies (e.g., Amazon), show only the top 10–20 most common charge variations.
  - **Implementation:**
      - Built programmatically by GrowthX.
      - Will be hosted in the Brex repo, with Kirkland gaining necessary Slack access.
      - [**URL Structure:** `brex.com/tools/charge-finder/[company-name]`](https://fathom.video/share/_UrPTKGS6BCwdnWZ3hugg2TrYhmwW-jx?tab=summary&timestamp=551.0)

### Brex Resources Hub V1 UI Review

  - **Goal:** Consolidate all Brex content into a single, navigable hub.
  - **Key Features:**
      - Breadcrumbs and sticky nav for easy navigation.
      - Content tagged by category, topic, and persona.
      - Sections for featured articles, topics, tools, and trends.
  - **Feedback & Revisions:**
      - **Hero Section:**
          - Reduce font size of "Insights, Tools, and Guides" subtitle.
          - Make article CTAs (e.g., "Read Now") more prominent.
      - **Content Sections:**
          - Add "View All" buttons to each section (e.g., Topics, Tools, Webinars).
          - Increase image size in the "Explore Topics" section.
      - **Content Strategy:**
          - Remove outdated content (e.g., old podcasts, webinars).
          - Add a dedicated "Case Studies" section.
          - Consider limiting "Spend Trends" categories to the top 4 performers.
  - **Internal Review Strategy:**
      - **Challenge:** The hub's design is a major site overhaul and will require approval from the Chief Design Officer (Bingo).
      - **Action:** Jon will prepare for the review by comparing the new design to the current site to justify the changes.

### Case Studies Page Redesign

  - **Problem:** The current case studies page has poor UX and significant white space.
  - **Requirement:** Segment Marketing requested an "industry" filter be added.
  - **Solution:** Redesign the page to fix its UX and add the filter. This new, improved layout will then serve as a template for other content pages (e.g., eBooks, blog).

---

## Action Items

**George Haikal (GrowthX, Design/Product Lead)**
- Build Charge Finder in Brex repo; exclude customer counts; cap variations for large vendors (top 10-20 only); add Google verification check; use URL structure `/tools/charge-finder/[vendor-name]`
- Build third tool; demo next week to Jon
- Update Resources Hub: reduce "Insights, Tools, and Guides" subtitle font size; make article CTAs (e.g., "Read Now") more prominent with oval styling; increase image size in "Explore Topics" section; add "View All" buttons to each content section; add dedicated "Case Studies" section; remove outdated podcasts and webinars
- Redesign Case Studies page: add industry filter (requested by Segment Marketing); remove large whitespace; align layout to serve as template for eBooks and other content pages
- Propose global nav changes to Jon; recommend removing webinars/events links due to outdated content

**Jon Kowieski (Brex, Senior Director of Content/Product)**
- Decide which Spend Trends categories to prioritize (currently leaning toward top 4: corporate cards, business banking, expense management, credit cards); inform George
- Prepare Resources Hub/Charge Finder design comparison for internal review; share with Bingo (Chief Design Officer); request formal feedback

---

## Transcript

**George Haikal:** This meeting is being recorded.

---

### Charge Finder Tool Review

**Jon Kowieski:** I spoke with someone on my team yesterday about the ChargeFinder data. The numbers at the end of most statement charges are actually company identifiers. We went through a Ramp example and he made clear we should not display customer-identifying numbers or mention how many customers are charged per month. There's legal risk involved.

**George Haikal:** Okay.

**Jon Kowieski:** I realized that wasn't something I knew until yesterday. We should look at the most common charges normally appear.

**George Haikal:** Yeah, we're already working on the next tool as well. Kirkland is getting final access in your private Slack channels to run commands. We'll build this out in your repo directly. Kirkland gaining that access is critical for moving forward.

**Jon Kowieski:** I think the design looks really good. The one thing I was thinking—there's so many different Amazon charge variations, certain larger companies have so many different charges that I didn't think through until yesterday.

**George Haikal:** Like the same variations—Amazon, MKTPL IND-PRIVIA?

**Jon Kowieski:** Yeah. Those are identifiers the average customer doesn't need. It's probably just Amazon Marketplace. Is there a way to Google stuff like this to make sure it's accurate? Maybe we show only the top ten or top twenty variations?

**George Haikal:** That's helpful. For now, I'll consider this good to go and let the team sprint on getting it built. The other tools will follow these design elements and look unique but consistent.

**Jon Kowieski:** Then the URL structure would be like Brex.com/tools/charge-finder and then the vendor name—Amazon, Uber, whoever?

**George Haikal:** Yes.

---

### Brex Resources Hub V1 UI Review

**George Haikal:** I wanted to show you the V1 UI for the Brex Resources Hub. Breadcrumbs on the left, sticky nav on the right. There's a big hero, featured content, and different highlighted types. We added categories and tags—persona-level and category-level. You can click into topics like expense management, financial planning, travel and spend. Below are trending and popular articles, and we're calling out Spend Trends specifically.

**Jon Kowieski:** If you have an example of a similar website, that would help right away. One thing—the font size of "Insights, Tools, and Guides" might need to be smaller than the actual "Brex Resources Hub" text. There will absolutely be notes from the design team. I'm thinking through it.

**George Haikal:** I kind of want these article CTAs to pop a little more. Almost like the download guide button—we can keep the colors but make them highlighted and oval.

**Jon Kowieski:** I'm doing a comparison to what exists now. You have a download guide CTA, but for the others, you don't technically have a CTA. "Read Now" is probably fine as is, but keep that in mind.

**Jon Kowieski:** I like the Explore Topics section. The images might need to be a little bigger because there's white space, but I'm fine either way. I'd be curious if a "View All" CTA would drive clicks.

**George Haikal:** Yeah, we can add a view all button to each section.

**Jon Kowieski:** Yeah, my guess is that will be what they want.

---

### Content Strategy & Spend Trends

**Jon Kowieski:** Are we manually selecting the most popular or the newest articles?

**George Haikal:** I want to highlight the best performing and have it easily accessible.

**Jon Kowieski:** That might be a manual thing. The podcasts are all super old, so it doesn't make sense to mention them. But for webinars, I don't think we've done any recently. Case studies—I think they'll want that on this page.

**George Haikal:** Okay, we'll have Case Studies.

**Jon Kowieski:** Yeah, I was talking to someone today about case studies. They want a feature—an industry filter. The current case studies page has poor UX and huge white space. It doesn't make sense.

**George Haikal:** The tags should be here across topic, segment, and industry.

**Jon Kowieski:** The layout we design for this should be a template for the eBooks page and other content pages. The Brex blog needs it too, but I don't know if they'll take any of it.

**George Haikal:** Yeah, we can fix that once Kirk gets access.

**Jon Kowieski:** Also, is the thought to put every Spend Trends category? Certain categories don't do as much for us—accounting, for example. Credit card does much better. If we only had to put four, I'd do that. Odds of putting all categories are probably low. So be prepared to limit it, but I'll try to fight for at least the top performers.

**George Haikal:** You definitely know better than me.

---

### Global Navigation & Approval Process

**George Haikal:** We're going to recommend global nav changes as well. What we think it should look like.

**Jon Kowieski:** Sadly, most of my advice on global nav never gets followed. I fight tooth and nail for the footer. Customer stories is under customers tab—it's confusing. The charge finder looked good. There will be a lot of comments during review. The one thing I'll try to do is make sure there's not too many cooks in the kitchen—too many creative directors with different recipes turns into conflict and slows us down.

**George Haikal:** I would love if you could help streamline that. We can move super fast and hit high quality.

**Jon Kowieski:** The tools pages don't need as much approval. But the main Resources Hub page needs that approval. They may want to see these layouts. I'll have to share them to Bingo—he's the Chief Design Officer. He has the final call.

**George Haikal:** Thank you. Great progress. I appreciate you.

**Jon Kowieski:** I need to hop into another meeting. If you have anything else, just Slack me.

**George Haikal:** Awesome. Talk soon.
