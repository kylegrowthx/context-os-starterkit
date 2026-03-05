# Pixis <> GrowthX Weekly Sync

<metadata>
date: 2025-04-16
time: 17:01 UTC
duration: 30 minutes
organizer: aida@growthxlabs.com
participants: Aida Knežević, Rachel Pasche, Jakub Rudnik, Colin Campbell, Evan Dunn, Deepak Kundnani, Jason Widup
fathom_recording_id: 57680080
fathom_url: https://fathom.video/calls/277025612
share_url: https://fathom.video/share/ZDA9hs1WEwJs6Jckwdxhz-oMKRk_u2Vq
source: fathom
enriched_on: 2026-03-04 18:45 UTC
</metadata>

---

## Summary

Pixis and GrowthX aligned on content delivery with three weeks remaining before the May 11 contract end date. Traffic surged 84% following the site migration, and the team discussed analytics anomalies, CMS workflow for the Craft migration, and upcoming deliverables including 25 additional glossary terms. Colin and Rachel committed to prioritizing assignments from the 46 items in Airtable to maintain the 6-7 articles/week pace needed to hit the 50,000-word contract target.

---

## Context

Pixis is a GrowthX content client on a marketing engagement ending May 11, 2025. This weekly sync is the primary touchpoint for content strategy alignment, delivery tracking, and problem-solving. The Pixis team includes Colin Campbell (reviewing and prioritizing content), Rachel Pasche (editing articles), Evan Dunn (analytics), and other team members. GrowthX's delivery team (Aida Knežević project lead, Jakub Rudnik, Rachel Pasche) manages the pipeline, content operations, and CMS coordination. The contract specifies 50,000 words delivered at a pace of 6-7 articles per week (averaging 2,000-2,500 words each). The relationship is progressing toward close-out with focus on maximizing output in the remaining three weeks.

---

## Relevance

- **To GrowthX Delivery:** Content velocity is on track to deliver 50,000 words by May 11 at 6-7 articles/week (~2,000-2,500 words each). Craft CMS workflow differs from previous platform: modular content blocks, two-step publishing (Enable + Publish Site). Aida needs Craft login access and glossary terms list. Statistics articles are prioritized for backlink potential.

- **To GrowthX Business Development:** Pixis traffic increased 84% despite site migration and Google core update, indicating strong content performance. Glossary terms generating traffic and could continue driving long-tail SEO value post-contract. Team sentiment positive on content quality and editing process (Rachel's specific, actionable comments cited as effective). Contract wrapping cleanly with three weeks remaining.

- **To Analytics/Operations:** Post-migration GA4 tracking issues: "/blogs" redirecting to "/blog" causing first-touch attribution to old path; 1,600 sessions with "not set" landing pages; homepage showing unexpected 19,000 sessions (likely LinkedIn announcement + redirect re-attribution). Evan Dunn can investigate with GA4 custom dimensions or Regex in Looker Studio. Re-indexing timeline will resolve redirect attribution gradually.

---

## Overview

- Contract end date is May 11th; ~3 weeks remaining to wrap up deliverables
- Content performance is strong despite recent site migration and core update (84% traffic increase)
- Some GA4 tracking anomalies noted post-migration; likely due to redirects and re-indexing
- Glossary content needs migration to new CMS (Craft); Aida to provide 25 additional terms

---

## Key Topics

### Content Strategy and Deliverables

  - 46 assignments in Airtable ready for approval
  - Aiming for 6-7 articles/week (2000-2500 words each) to meet 50,000-word contract
  - Colin to review and prioritize assignments, leaving comments for urgent pieces
  - Statistics articles prioritized for backlink potential

### Website Performance

  - Traffic up 84% in the last week
  - Top performing blogs: Meta ads formats, LLMs for marketing, AI prompts for marketing
  - Niche topics (e.g., insurance marketing) showing lower but notable traffic

### Analytics and Tracking Issues

  - Post-migration: '/blog' subfolder replacing '/blogs', causing tracking discrepancies
  - Large number of "not set" landing pages in GA4 (1,600 sessions)
  - Unexpected spike in homepage traffic (19,000 sessions)
  - Likely due to re-indexing and redirect attribution in GA4

### CMS Migration and Content Management

  - New Craft CMS workflow explained
  - Modular content blocks for easy formatting
  - Two-step publishing process: Enable content, then "Publish Site"

### Glossary Content

  - Previously published terms in Airtable
  - Some terms already generating traffic
  - Aida to provide 25 additional glossary terms

---

## Action Items

**Colin Campbell (Pixis)**
- Approve new assignments in Airtable for next week's content (from 46 in Considering column)
- Prioritize articles in Airtable ready-to-start section; add comments for Rachel on priorities
- Review topic clusters to ensure coverage; add new article ideas to Airtable if gaps found
- Give Aida Knežević access to Craft CMS (send login details via Slack)

**Aida Knežević (GrowthX)**
- Compile 25 additional glossary terms; add docs to Airtable this week or next

---

## Transcript

*(Note: Meeting began with ~10 minutes of casual conversation about plants and workspace setup before transitioning to business discussion around timestamp 00:11:00.)*

**Aida Knežević:** So I think our last date is May 11. If there's anything that we should know or any way that we can help you during that time — doing additional content that you might need or switching focus on something else — we can do that. Obviously we're wrapping up, so the original strategy isn't as relevant anymore. If you have anything you want us to work on, just let us know.

**Colin Campbell:** What does our balance of work look like? I know we've been a bottleneck. Are we up to speed, or is there much we have to produce together in the next three weeks?

**Aida Knežević:** Content is covered for this week. For next week, we need to approve new assignments. There are 46 assignments in the Considering column in Airtable. You can look through and move any to Ready to Start. If you can't find other assignments you like, let me know and I'll do more research. There should be enough for at least two weeks. This week and next week we're prioritizing statistics articles since those have been attracting backlinks.

**Colin Campbell:** There's 181 total assignments, 29 in backlog, 46 in Considering. So how many total articles should I expect we have published by May 11? That would help me communicate to the team.

**Aida Knežević:** Our contract is up to 50,000 words. That amounts to about 10 articles per week at 1,200 words each, but most of our articles have been longer. We've been delivering about 7 to 8 articles per week. Rachel, what's the average word count you're seeing?

**Rachel Pasche:** They're definitely closer to 2,000 words — probably 7 or 8 pages on average. Looking at one right now, it's 2,500 words and seven pages.

**Aida Knežević:** Yeah, so we could go through and compile all published articles to get exact word count, but I don't think that's necessary.

**Colin Campbell:** Yeah, that sounds like a pain. I'm comfortable aiming for 6 to 8 articles per week, and we've been on pace. I just want to make sure I can communicate to Jason how we're going to wrap up. Rachel, if you're going through assignments and want to prioritize some, feel free to leave comments in Airtable and I'll keep an eye out for those in the Ready to Start section.

**Rachel Pasche:** That would be great. Otherwise it's up to my discretion what gets to the pipeline first. Specific comments really help.

**Colin Campbell:** I want to make sure I've covered at least one or two articles in all topic clusters. Maybe I'll introduce some new ideas, or I'll prioritize approving what's there. I'll add comments where I see gaps.

**Aida Knežević:** Great. Performance-wise, last week was the biggest yet. Traffic was up 84% — top performers were Meta ads formats, LLMs for marketing, AI prompts for marketing. Niche topics like insurance marketing are getting lower traffic but still notable since they're low-volume keywords.

**Colin Campbell:** I noticed something weird in the analytics and asked Evan to look at it. The old /blogs subfolder is now /blog on the new site. All the URLs that used to get traffic now show nothing. I might create a custom dimension in GA4 or handle it with a Regex in Looker Studio. But there's another issue — there's a big chunk of landing pages showing "not set," and a huge spike in homepage traffic at 19,000 sessions. I don't think a LinkedIn announcement drove that. Do you have any idea what's going on? I'm not too familiar with GA4.

**Aida Knežević:** Whenever I see "not set" in Google Analytics driving huge traffic spikes, yeah, I had a client at a previous agency going through the exact same thing. We never figured it out.

**Jakub Rudnik:** I'd caveat this — I try to avoid relying too heavily on GA4 data right now. But I'd look at other dimensions to try to understand. You had a big spike, so first, is your total traffic normal? When you break it down by "not set," sometimes you can identify that those views should be attributed elsewhere. You might be missing a thousand views over here and have a thousand over there — it looks one to one. I'd check that. Also, you could have an internal support subdomain now being crawled and indexed that wasn't supposed to be. That might be contributing.

**Colin Campbell:** That's possible. But the homepage spike doesn't seem to match that. We did do a big LinkedIn announcement, but I don't think that drove 19,000 sessions.

**Jakub Rudnik:** You could get some organic traffic from LinkedIn. 15,000 clicks from a campaign would be in the 99th percentile of an announcement, but it's not impossible. The /blog URIs showing no traffic is a different issue. You're seeing traffic still going to /blogs on the old domain. Google is going to slowly re-index and recognize the redirects. Right now GA is attributing first-touch to /blogs, even though it's immediately redirected. That will sort itself out as Google re-indexes.

**Colin Campbell:** Okay, that makes sense. Do you still have the glossary on your new site? I checked last week and it was gone.

**Colin Campbell:** It's on the agency's to-do list. In Craft, there's no pre-built object that works well for glossaries. They're either building something or rigging existing objects to work.

**Aida Knežević:** Got it. Just to let you know, all glossary terms are in Airtable marked as published or not. Some were staged but I wasn't publishing 10 per week to avoid overwhelming crawlers. Some are getting traffic. They might need to be restaged. And I owe you 25 more terms — I'll do those this week or next and add them to Airtable.

**Colin Campbell:** Let me show you how Craft works. When you log in, you see Entries — all the pages. Global doesn't have categories. Assets is images. You do everything from within Entries. They call content types Channels, but everything you produce is a blog. You click Entry, add Title, Feature Image, Category, Intro Paragraph. But I'm going to leave intro empty because we don't like the way they formatted it. You add a content area with text blocks — you can add it all in one block or modular. For images, you'd do text block, then image block. The SEO section lets you write title, description, select images for social, add author. The quirk is publishing — you click Enable first, then Publish Site to push it live.

**Aida Knežević:** That's like Framer — you publish something, then update the site for it to actually go live.

**Colin Campbell:** Should I give you access directly to Craft? I'll send your team email login details via Slack.

**Aida Knežević:** That's right, I have that. Okay, thank you.

**Colin Campbell:** So next steps, we just need more content approvals and I'll get glossary pages to you soon.
