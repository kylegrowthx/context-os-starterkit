# Website SEO Sync

<metadata>
date: 2025-03-10
time: 15:04 UTC
duration: 14 minutes
organizer: Prateek Gupta (GrowthX)
participants: Prateek Gupta (GrowthX), Jimmy Pal (GrowthX), Ritesh Kewlani (Firework), Cameron Brown (Firework), Yi Jin (Firework)
fathom_recording_id: 51014118
fathom_url: https://fathom.video/calls/248086013
share_url: https://fathom.video/share/FPFnzS6Xu4i_2msbAtU81PqErktx385T
source: fathom
enriched_on: 2026-03-04 10:35 UTC
</metadata>

---

## Summary

GrowthX and Firework aligned on implementing a new visitor tracking tool to capture 1-2% of blog visitors without form submission, with expected weekly conversions of 20-30 leads from ~1,000 blog visitors. Prateek will document the tracking tool details and analyze Firework's recent drop in form submissions (only 1 contact last week), while Cameron will build an automated system to dynamically assign lead magnets based on blog categories. Ritesh will allocate existing lead magnets across blog categories, and the team will begin pixel implementation this week.

---

## Context

Firework is a video/content platform client where GrowthX is supporting lead generation and conversion optimization. This meeting was a tactical sync between Prateek (GrowthX delivery) and Ritesh (Firework product/operations) to address declining blog-to-lead conversion rates. The team had recently committed to implementing a visitor tracking tool and needed to align on execution, scope, and the dynamic lead magnet system to improve lead quality and volume. Cameron joined from Firework's engineering side to assess technical feasibility.

---

## Relevance

**To GrowthX Delivery:**
- Visitor tracking tool implementation is a new lead-generation methodology for blog traffic — 1-2% capture rate with LinkedIn/email/company data without form friction
- Dynamic lead magnet assignment by blog category is an advanced segmentation pattern — requires mapping content topics to relevant lead offers and CMS customization in Webflow
- Blog conversion troubleshooting (form submission decline) involves multi-level analysis: traffic volume trends, CTA effectiveness, user journey mapping, and form placement validation

**To Firework Account Health:**
- Form submission drop (1 contact last week vs. historical baseline) is a material conversion signal — requires urgent investigation across traffic sources, CTA performance, and page-level metrics
- Lead magnet quality/relevance is a potential root cause — moving to dynamic assignment by topic should improve fit and conversion
- Prateek flagged technical concerns about whether Webflow CMS can accommodate custom lead magnet override rules; Cameron needs to scope feasibility by Thursday call

**To GrowthX Business Development:**
- Account engagement is strong (14-minute sync focused on concrete execution vs. strategy) — Ritesh driving automation and process improvement signals expansion readiness
- Multiple concurrent workstreams (tracking tool, form analysis, dynamic lead magnets, industry report publishing) suggest Firework is scaling content and growth operations

---

## Overview

- Implementing new visitor tracking tool to capture 1-2% of visitor data without form submission
- Dynamic lead magnet allocation based on blog categories to be developed
- Investigating recent drop in form submissions from blog traffic
- Pixel implementation and data collection to begin this week

---

## Key Topics

### Visitor Tracking Implementation

  - New tool captures visitor data (name, email, company) without form submission
  - Typically tracks 1-2% of visitors due to various technical constraints
  - More efficient and cost-effective than previous solutions
  - Expected to capture data for 20-30 people weekly from \~1000 blog visitors

### Dynamic Lead Magnet Allocation

  - Plan to dynamically push visitors to different landing pages based on ICP targeting
  - Cameron to develop automated system assigning lead magnets based on blog categories
  - Initial approach: Add fields in Webflow CMS to override default CTA/lead magnet
  - Advanced version: Automate lead magnet selection based on blog category tags
  - Pratik to provide spreadsheet mapping blogs to appropriate lead magnets

### Blog Conversion Rate Analysis

  - Recent decline in form submissions (only 1 contact from blogs last week)
  - Pratik to investigate:
    1.  Changes in blog visitor numbers
    2.  Performance of lead magnets and CTAs
    3.  User journey and form submission locations

### Website Pixel Implementation

  - Discussed briefly; needs to be implemented this week
  - Team to start reading data from the pixel immediately after implementation

---

## Action Items

**Prateek Gupta (GrowthX)**
- Send document with details on website visitor tracking tool to Ritesh and Cameron
- Investigate drop in form submissions — analyze visitor numbers, CTA effectiveness, and user journey across blog pages
- Share form submission analysis results with Ritesh and Cameron before next weekly call
- Create spreadsheet mapping blog articles to appropriate lead magnets for dynamic lead magnet system

**Cameron Brown (Firework)**
- Implement automated lead magnet assignment based on blog categories — scope technical feasibility with Webflow CMS by Thursday call
- Propose implementation approach: either manual overrides per blog in CMS editor or fully automated tag-based routing

**Ritesh Kewlani (Firework)**
- Allocate existing lead magnets across different blog categories for dynamic lead addition feature
- Partner with Prateek on blog-to-lead-magnet mapping spreadsheet to guide Cameron's implementation

---

## Transcript

**Ritesh Kewlani:** Can you help us explain what this will help us with?

**Prateek Gupta:** So basically, what happens is visitors are coming on our website. It will start profiling them — their position, what type of company they work in — and we'll be able to capture their name, ID, and all their details.

**Prateek Gupta:** It's more like getting visitors' data without them filling in a form. That way, we're able to send them emailers and everything.

**Ritesh Kewlani:** So what information will we be able to track?

**Prateek Gupta:** LinkedIn, email, ID, their name, their company — lots of things.

**Ritesh Kewlani:** We heard back from you last week saying you'd implement the tracking. If this is implemented today, we'll start getting data this week, correct?

**Prateek Gupta:** Generally it depends on tool to tool, but you typically get data from 1-2% of visitors. So if you're getting around 1,000 blog visitors right now, you'd get data from 20-30 people weekly. People have to log in with the same Gmail ID used with LinkedIn, the same browser — lots of permutations. But that's the accuracy of these tools.

**Ritesh Kewlani:** Can you send us a document so we can go through it? We want to understand this better. Right after this, we'll be dynamically pushing people to different landing pages based on ICP targeting. Are we using the same tool or a different one?

**Prateek Gupta:** Confirmed, the one I'm using is more efficient and faster. It's also more cost-effective.

**Ritesh Kewlani:** When you say efficient, do you mean we'll get more than 1%?

**Prateek Gupta:** Yes, more than 1% and also lower cost.

**Ritesh Kewlani:** UTM tracking is already done. Is there anything else we need to cover? I think one trend we're seeing week on week is that form submissions are going down. Last week, we only got one contact from the blogs. Can you do a deep dive and figure out where people were coming from earlier and why there's a drop now? What has changed?

**Prateek Gupta:** I'll look at a couple of levels: first, whether the visitors to these blocks are reduced. If visitors haven't dropped, we'll look at whether the lead magnets are working or if there's an issue with the CTA. I'll also look at the user journey — which form they filled and whether they came from the same block or visited another page.

**Ritesh Kewlani:** Can you share this analysis with me and Cameron before the next call? I want to make sure we review it together.

**Ritesh Kewlani:** What was this dynamic lead addition?

**Prateek Gupta:** This is where if someone is visiting a beauty playbook, we give them the beauty lead magnet. If they're visiting a fashion article, they get the fashion lead magnet — custom lead magnets based on page type.

**Ritesh Kewlani:** Okay, how do we go ahead with this? What help do you need from Cameron?

**Prateek Gupta:** First, we have to give Cameron rules — like, these 20 blocks get this lead magnet, 50 blocks get that lead magnet, etc. But before that, I want to check with Cameron: do we have the functionality to accommodate custom lead magnet rules for specific pages?

**Cameron Brown:** And I think if that's the ask, I can try to get that version where lead magnets are automatically built based on the blog category. My initial thought to make it easy to roll out is to add fields to the blog CMS in Webflow where you can override the CTA and lead magnet with custom values. But that means editing blogs retroactively if you want to change the inline CTA.

**Cameron Brown:** Alternatively, I can skip that first version and go right to having everything be automated based on blog category. I'd just need to know: if the category is beauty, which lead magnet do I show? If it's industry insights, which one?

**Ritesh Kewlani:** Can you please build that out at a high level? I just wanted us to start working through the list. We have a lot of different resources. Let's start with a list of all the blogs. Pratik, help us identify which blogs we want to add data to. You and I already know what lead magnets we have, so I can help allocate those across different blogs. We can set the logic and keep it simple for now, then add more complexity later.

**Prateek Gupta:** We're also launching the industry report this week, so I can help you map it out. Let me start with the spreadsheet. Here's a quick example: we have an article on shoppable video for the fashion industry. The article has two types — if it has shoppable video, show the shoppable video lead magnet; if it's fashion-tagged, show fashion-related lead magnets. I can't make promises if it'll be done by the Thursday meeting — we just had a meeting this morning and there's a lot of work — but I'd love to get it done.

**Cameron Brown:** Yeah, I'll do my best to get something to show.

**Yi Jin:** I'm good with this.

**Cameron Brown:** Thanks for organizing this. I know you're in your car. I organized this and forgot the timezone difference. We'll make sure it starts at noon next week so you're not joining on your commute. Is that okay?

**Prateek Gupta:** It would become too late for me. Could we do an hour later? One hour later works completely.

**Ritesh Kewlani:** I'm fine with that. Did Jimmy drop off?

**Prateek Gupta:** He just dropped off.

**Ritesh Kewlani:** So the only thing we have to discuss with him is the pixel. We need to make sure that's implemented and start reading the data this week. Anything else? No, all good. Let's take this conversation on Slack. There are a lot of action items — you need to investigate conversion data, we need to figure out dynamic lead addition, and we need to publish more blocks this week. Let's keep discussing tomorrow and the day after. Please escalate if you need help. We have our call on Thursday. Perfect. Thanks, everyone.
