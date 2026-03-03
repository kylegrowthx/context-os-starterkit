# Airbyte <> GrowthX Weekly Sync

<metadata>
date: 2025-07-14
time: 15:30 UTC
duration: 20 minutes
organizer: Marcel Santilli
participants: Marcel Santilli, George Haikal, Jakub Rudnik, David Galic, Mario Moscatiello, Tanmay Sarkar, Nithin M
fathom_recording_id: 73936794
fathom_url: https://fathom.video/calls/349833693
share_url: https://fathom.video/share/5P1kyZZxkCtfPvwRrQ7TgyeKsxmZmm6B
source: fathom
enriched_on: 2025-03-03 12:45 UTC
speaker_note: "Board Room" label identified as George Haikal (GrowthX). "5 - Glacier" device label identified as Tanmay Sarkar (Airbyte) based on transcript context and role references.
</metadata>

---

## Summary

GrowthX and Airbyte aligned on three major workstreams: automated publishing (new API-driven config system launching to beta), content refresh (728 URLs identified, 100-URL batch this week), and website redesign strategy. George and Marcel emphasized topic page architecture (inspired by Helpline and Wise) to build semantic relevance and avoid content sprawl—critical as Airbyte scales from Webflow. Tanmay and Jakub will test auto-publishing this week while monitoring refresh metrics (impressions, CTR, bounce rate) starting next week.

---

## Context

Airbyte is a data integration platform with a large, complex Webflow site (multiple content collections, 728+ indexable URLs). GrowthX is the content and SEO services partner, working with Tanmay and Mario on scaling content production and SEO performance. The relationship spans three major initiatives: (1) automating Webflow publishing workflows to handle scale, (2) refreshing and analyzing existing content for SEO lift, and (3) restructuring the site architecture as Airbyte plans a rebrand and redesign. This meeting focused on project updates and strategic guidance on content structure—particularly George's recommendation to adopt topic pages and flatten the IA to avoid repeating mistakes of sites like Clay.com that lost traffic due to low-relevance content scaling.

---

## Relevance

**To GrowthX Delivery:**
- Built reusable API-based config system for field mapping in Webflow — reduces engineering overhead per client to near-zero and enables scaling publishing workflows (high-ROI pattern for future Webflow clients).
- Topic page template and flat IA strategy (tagging-based discovery) proven at scale by Helpline and Wise — repeatable playbook for content-heavy clients avoiding content sprawl penalties.
- Refresh testing workflow (100-URL cohort, delta tracking via seotesting.com) quantifies content refresh ROI (impressions, CTR, click volume, engagement) — data foundation for future refresh projects.
- Defined scope transition: finish refresh + redesign in Webflow, then evaluate tech stack for migration (CMS + frontend) — client planning clarity reduces churn risk.

**To GrowthX Business Development:**
- Airbyte launching new hybrid deployment platform in next few weeks → content strategy expansion opportunity (new vertical content for healthcare, etc.). Mario and Tanmay planning category/recipe content in next 2-3 weeks.
- Account health: strong execution, clear roadmap, Mario empowered and collaborative. Reference-ready for similar scale clients (data, infra, complex Webflow sites).
- Potential migration project (Webflow → CMS) in 3-4 months — early visibility, scope scoping opportunity.

**To CheckThat:**
- Airbyte's hybrid deployment content (healthcare, data sovereignty, compliance-focused verticals) potentially valuable for CheckThat AEO research on regulated industries.
- Site structure recommendation (flat IA with semantic tagging) aligns with AEO best practices for topical authority and E-E-A-T signals.

---

## Overview

- Auto-publishing progress: New system built to automate field mapping and content publishing, saving time and improving efficiency.
- Content refresh strategy: 728 URLs identified for potential refresh, with 100 selected for this week's batch.
- Website redesign: Airbyte is in the design phase of a website rebrand and restructure, focusing on main pages and product pages.
- SEO strategy: Emphasis on creating topic pages and improving content structure to enhance topical relevance and SEO performance.

---

## Key Topics

### Auto-publishing and Workflow Improvements

  - New system built to automate field mapping and content publishing in Webflow
  - Ingest API and config file created to map fields automatically
  - Saves significant time and improves efficiency for both teams
  - Will allow for scaling of content production and quality improvements
  - Testing phase beginning today, moving into beta soon

### Content Production and Review

  - 22 new articles ready for review
  - Additional 22 pieces of content planned for this week
  - Formatting issues for competitor articles resolved

### Content Refresh Strategy

  - 728 URLs identified as candidates for refresh
  - 100 URLs selected for this week's batch
  - Process includes analyzing:
      - Number of keywords
      - Average keyword difficulty
      - Last publication/update date
  - Tracking delta between refreshed and non-refreshed pages
  - Metrics to monitor: impressions, click-through rates, raw clicks, time on page, bounce rates

### Website Redesign and Structure

  - Airbyte in design phase of website rebrand and restructure
  - Focus on main pages and product pages
  - Blog and articles to receive a reskin initially
  - Considering implementation of topic pages and improved content structure
  - Drawing inspiration from successful sites like Helpline.com and Wise.com

### SEO Strategy and Best Practices

  - Recommendation to create topic pages similar to blog index pages
  - Emphasis on flat structure with effective use of tags and subtopics
  - Goal: Create a web of topical semantics to show relevance to core business
  - Avoid creating large volumes of loosely related content

### Website Migration Considerations

  - Currently managing redirects directly in Webflow
  - GrowthX offered assistance with future migration planning
  - Potential for exploring new tech stack options after redesign

---

## Action Items

**Jakub Rudnik (GrowthX)**
- Test auto-publishing feature for various article types and nuances

**David Galic (GrowthX)**
- Update OS with 22 new articles ready for review; move to appropriate status

**George Haikal (GrowthX)**
- Post 3-4 async updates on refresh workflow progress throughout the week

---

## Transcript
**Jakub Rudnik:** Marcel, what's up?

**Jakub Rudnik:** Morning.

**Tanmay Sarkar:** Hey, Marcel, hi, Jacob.

**Jakub Rudnik:** How's it going?

**Jakub Rudnik:** Happy Monday.

**Tanmay Sarkar:** Happy Monday.

**George Haikal:** Good morning.

**Mario Moscatiello:** Good morning.

**George Haikal:** You guys hear us okay?

**Mario Moscatiello:** Yeah, all good.

**George Haikal:** Sweet. All right. Jacob, do you want to kick us off?

**Jakub Rudnik:** Yeah, sure. I can give an overview on the day-to-day stuff, plus the progress we made on auto-publishing and refresh workflow. I think it's really important we get to talk about alignment on next steps for new strategies, which is key — obviously why George and Marcel are joining. Let me share my screen, David. Thanks for putting this together. We'll come back to the next steps at the top.

**Jakub Rudnik:** We've been working with our engineering team on auto-publishing. We need to scale content production and save time on both sides. We're working with Tanmay on how to automate FAQs and schema markup. It should free up everyone's time and improve quality. There's definitely some nuance with different article types, so there's a bunch to test. We'll be testing today and moving into beta tomorrow.

**George Haikal:** So I connected with the engineering team on this. You all have the gnarliest Webflow instance of any customer we've worked with — so many different content types and collections. Even 15-30 minutes of engineering time per new collection would have been the blocker. What we built is an API ingest plus a config file that specifies the field mapping workflows. So field mapping is now completely automated. That's great value for other clients too, but it means we never have to do manual field mapping again.

**Mario Moscatiello:** In the next few months we'll probably move to a CMS plus frontend solution because Webflow isn't scalable for our content volume. We'll work with you guys on that. But for now this is great.

**George Haikal:** These migrations take forever, so this delivers serious short-term value. That's why it took longer than expected, but now we should be fully on track.

**Jakub Rudnik:** Thanks for translating the engineering. On article publishing: we have 22 new articles ready for review. There will be another 22 this week. David, can we confirm the competitor articles formatting? I remember there was an issue.

**David Galic:** Yeah, we were formatting competitor-related articles differently. Tanmay included a how-to in last week's notes, and the content team updated everything accordingly. I wanted to confirm with Tanmay that we're good to go now.

**Tanmay Sarkar:** Perfect.

**Jakub Rudnik:** Those are the standard weekly items. Maybe George and Marcel can speak to the new workstreams. Where do we want to focus?

**George Haikal:** Let me show some of the work we've done. We've quantified the URLs to refresh. We identified 728 candidates so far. We're analyzing keyword count, average keyword difficulty, and last publication date. We picked a really good batch of 100 for this week. Now that publishing is streamlined, we should move aggressively. We're running through the same workflow — making FAQs more comprehensive, for example. We're tracking the delta between refreshed and control pages. Around this time next week, we should start seeing signals. For sure the following week. We'll do another batch next week and figure out: one, our capacity — how aggressive can we be weekly? And two, the long-term value. We'll look at impressions, click-through rates, raw clicks per page, time on page, and bounce rates. We could instrument scroll depth later if you want.

**Mario Moscatiello:** You're saying we need something to analyze all that at scale?

**George Haikal:** Yeah, there are tools like seotesting.com that compare deltas between keyword average, clicks, impressions. Search Console is harder for clustering and comparing URL cohorts. We use seotesting for progress tracking over time.

**Mario Moscatiello:** This should give us two to three months of work, plus the editorial content we'll pick up in a couple of weeks. Tanmay and I will plan the editorial strategy then. We're launching a new platform with fully hybrid deployments. Following up on the chat with Marcel last week, we want to create categories: "If you're in healthcare, here's what you need to know about data sovereignty, hybrid deployments," etc. Tanmay and I will nail down the categories and obstacles in the next couple weeks and build the structure.

**George Haikal:** Perfect. One more thing — can you give us a quick update on the website revamp? We want to track timelines since those tend to be all-hands-on-deck as launch approaches. Are you in design or dev?

**Mario Moscatiello:** We're in design. I can send everything. We have a Whimsical with the new nav bar. It's mostly a rebrand and redesign, changing the structure of main pages and product pages. Blog and articles will get a reskin initially since we're refreshing them anyway.

**George Haikal:** I want to show you something quickly. Mario, what we've seen work really well: one, are there pages with higher conversion propensity outside sign-ups and the homepage? Of those, which drive the most sign-ups? If you have that data, we can map the next best logical step and A-B test. Since you're refreshing, you can be intentional about that. Our best practice is topic pages that look like blog index pages but work for any topic. Helpline.com scaled to over 150,000 pages successfully. They keep the structure flat but use a lot of listing pages with good tags leading to topic and subtopic pages. Those listing pages serve both content in that structure and related content anywhere. So you're dynamically creating a web of topical semantics showing Google how it all connects to your core business. That's different from sites like Clay.com that scaled 10,000 pages around "what is headquarters" — low relevance to their main business, so they got hit. All paths should lead to your core business.

**Mario Moscatiello:** That makes sense. Given the refresh focus, we can nail down the structure in the next two or three weeks and build it intentionally. Also, if you spot opportunities to reorganize content differently, let us know. Tanmay's the one-person team for content and SEO, so collaborative ideas help a lot.

**George Haikal:** How are you managing redirects if you prune categories?

**Tanmay Sarkar:** These categories were created programmatically via Airtable. We can do 301 redirects. My thinking is we refresh and keep the categories, but create one page with everything — data engineering, resources, talks, tutorials — in one place.

**George Haikal:** Webflow manages redirects, or you could use Cloudflare. Where are you handling them now?

**Tanmay Sarkar:** We manage them directly in Webflow's redirect section.

**George Haikal:** Good. As you get closer to migration, we can help. We've done tons of these and there are always gotchas. Even I miss things.

**Mario Moscatiello:** For now we're redesigning in Webflow. Once that's done, we'll kick off migration and figure out the tech stack together.

**George Haikal:** As long as you can use Prismic. Well, thanks, team. We appreciate it. We'll post at least three or four async updates this week as we make progress, and next week same thing. We'll look at signals within a few days after publishing starts. Thanks, everyone.
