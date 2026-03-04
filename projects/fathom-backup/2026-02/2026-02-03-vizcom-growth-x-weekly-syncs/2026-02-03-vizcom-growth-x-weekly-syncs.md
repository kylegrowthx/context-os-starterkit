# Vizcom <> Growth X - Weekly Syncs

<metadata>
date: 2026-02-03
time: 17:29 UTC
duration: 34 minutes
organizer: Team GrowthX
participants: Kim Lu (Vizcom), Carly Piekos (GrowthX), Sophia Silver (Vizcom), Maura Kelly (Vizcom)
speakers: 4
fathom_recording_id: 119362446
fathom_url: https://fathom.video/calls/552943287
share_url: https://fathom.video/share/rX4BYLVBNrrLodT-z_dD_Cuk49ZGKwt1
source: fathom
enriched_on: 2026-02-27 14:30 UTC
</metadata>

---

## Summary

Vizcom and GrowthX aligned on blog publishing strategy (targeting 10 articles/week to avoid page overload), reviewed content pipeline status (12 drafts, 25 staged articles), and introduced CheckThat, a new LLM-powered competitive intelligence platform replacing Scrunch. The team discussed conversion goals (550-650 weekly signups, 90-100 demo requests) and mapped blog CTAs to funnel stage.

---

## Context

Vizcom is rolling out large volumes of SEO-focused content alongside existing brand-driven posts (product launches, customer stories, feature updates). Publishing too many articles at once risks overwhelming the blog page, diluting the brand experience, and triggering spam detection. GrowthX and Vizcom are optimizing the content pipeline and conversion funnels to maximize organic traffic, signups, and demo requests post-migration. Performance metrics show positive upward trends since the migration, but signup conversions (330-450/week) are below the pre-migration baseline (550/week), indicating opportunity to drive uplift through improved CTAs and content alignment.

---

## Relevance

- **Content & SEO:** Blog layout optimization, publishing cadence (10 articles/week), alt tag implementation, structured data via GTM/Webflow, technical SEO audit for AI visibility
- **Analytics & Conversion:** Signup goals (550-650/week), demo request goals (90-100/week), CTA mapping to funnel stage (ToFu → product pages, BoFu → demo request), attribution pipeline setup
- **Competitive Intelligence:** CheckThat platform rollout, real-time competitor visibility across 1,500+ categories, content gap analysis, industry benchmarking (e.g., Blender -24%)
- **Project Management:** Content pipeline status (12 drafts, 25 staged, 5 in progress), Monday updates, Airtable/Notion integration for action tracking

---

## Overview

- **New Analytics Tool:** Growth X is replacing Scrunch with "CheckThat," a new LLM-powered platform providing real-time competitor visibility and content gaps. Vizcom gets 90-day Business Premium access to provide feedback.
- **Blog Publishing Strategy:** To avoid "chunking," Growth X will propose new blog layouts and a staggered publishing schedule (est. 10 articles/week). The team will also fix a bug causing new posts to appear at the bottom of the blog page.
- **Conversion Goals & CTAs:** Weekly targets are set to regain pre-migration signup levels (550+) and increase demo requests (90–100+). Blog CTAs will be tailored to content funnel stage (e.g., ToFu → Product Page, BoFu → Demo Request).
- **Technical SEO:** Vizcom will implement structured data via GTM using provided guides. Growth X will add alt tags to all new and backlogged content to improve image SEO.

---

## Key Topics

### Blog Publishing Strategy

  - **Problem:** Publishing a large volume of new SEO content risks "chunking" the main blog page, overwhelming users and diluting the brand experience.
  - **Bug:** A new test post appeared at the bottom of the blog page, not the top. Growth X will investigate.
  - **Solution:** Growth X will propose new blog layouts and a staggered publishing schedule (est. 10 articles/week) to maintain a steady flow without overwhelming the page.

### Content Pipeline & Technical SEO

  - **Content Status:**
      - 12 drafts ready for Vizcom review.
      - 25 articles staged in the CMS.
      - 5 working drafts in progress.
  - **Alt Tag Backlog:** Growth X will add alt tags to all new content and the existing backlog to improve image SEO.
  - **Structured Data:** Implementation guides for Webflow and GTM are in the shared Google Drive.
  - **AI Visibility:** An Adobe LLLM Optimizer check flagged low bot readability on some pages, likely due to JavaScript. Growth X will conduct a full technical audit next week.

### New Analytics Platform: CheckThat

  - **Rationale:** Replaces Scrunch with a new LLM-powered platform for deeper competitive intelligence.
  - **Key Features:**
      - **Real-time Visibility:** Tracks competitor performance on a shared library of 100k prompts.
      - **Content Gap Analysis:** Identifies topics where competitors are ranking but Vizcom is not.
      - **Competitor Profiles:** Provides detailed overviews (products, personas, pricing) for strategic research.
  - **Access:** Vizcom gets 90-day Business Premium access to provide feedback during the beta period.
  - **Context:** Industry-wide visibility drops (e.g., Blender -24%) provide context, showing if Vizcom's performance is an isolated issue or part of a broader trend.

### Performance & Conversion Goals

  - **Performance:** Organic sessions and engagement rates show a positive upward trend since the site migration.
  - **Weekly Conversion Goals:**
      - **Signups:** Increase from the current 330–450 average to a 550–650 target.
      - **Demo Requests:** Maintain or increase the current 90–100 average.
  - **Attribution:** Blog CTAs will be tailored to the content's funnel stage to drive specific conversions.
      - **Top of Funnel (ToFu):** Link to product overview pages.
      - **Bottom of Funnel (BoFu):** Link directly to the demo request page.

---

## Action Items

**Kim Lu (Vizcom)**
- Investigate vizcom.com/blog sort order; fix new posts to show newest first
- Align w/ GrowthX on CTA mapping (demo vs signup vs product); then update blog CTAs
- Review 12 blog drafts; send CTA recs to Carly
- Share GA4 signups/demo reporting w/ Carly

**Carly Piekos (GrowthX)**
- Send blog layout/categorization examples to Kim; align on pillars/cadence
- Update status of 'Automotive Materials' blog in CMS
- Add remaining Vizcom competitors to CheckThat
- Send CheckThat access/beta invite to Kim, Sophia, Maura

---

## Transcript
**Kim Lu:** Hello.

**Carly Piekos:** Hello, how are you?

**Kim Lu:** I'm good. How was your weekend?

**Carly Piekos:** It was good. How was yours?

**Kim Lu:** Not too bad either. I was just chatting with Maura about exploring co-working cafes in New York, which is always a struggle.

**Carly Piekos:** They're always full. I actually just left an agency in New York. Where are you located?

**Kim Lu:** I'm currently in Long Island City.

**Carly Piekos:** Is everybody in the New York area?

**Maura Kelly:** I'm in Brooklyn.

**Carly Piekos:** We're mostly in San Francisco, but I live in Asbury Park in New Jersey. All right, let's get started. Is there anything on top of mind that you want to discuss that I can add to the agenda?

**Kim Lu:** I think the one thing is, based on what you've seen with other clients, how to format the blog rollout without chunking all the content at once while keeping our brand style.

**Carly Piekos:** When you say chunking, could you share a bit more?

**Kim Lu:** We have a mix of different content on our blog—product launches, customer stories, features. As we roll out SEO-focused content, we want to avoid clogging the vizcom.com/blog page.

**Carly Piekos:** This is different by use case. If you put all content on the page, it continuously scrolls instead of grouping and categorizing.

**Maura Kelly:** I noticed one blog went live and it appeared at the bottom, not the top.

**Kim Lu:** I published this one today as a test, and it went straight to the bottom instead of the newest to the top. We can investigate this internally.

**Carly Piekos:** I'll send you a couple of ideas this week on how to organize content pillars. We can discuss how to structure the navigation at the top of the page.

**Carly Piekos:** Let me share my screen. We still have 12 drafts ready for review. If you've reviewed them, I can mark them as reviewed and have Jenny stage them. We have 25 articles staged in the blog right now. I'm sending Monday updates as an automation to keep you in the loop, and I created an actions page in Notion to keep us organized without clutter so we can sort our week at the beginning.

**Carly Piekos:** Are there any other adjustments you'd like to the status updates for the staged CMS? I was thinking we could add a last week, next week, this week queue so we know what's being published without clogging the blog pages.

**Kim Lu:** Yeah, that sounds good.

**Carly Piekos:** Which blog did you just publish?

**Kim Lu:** The automotive one.

**Maura Kelly:** "Automotive Materials: Choosing the Right Surfaces for Interior and Exterior."

**Carly Piekos:** Got it. I'll update the status on that and group the articles. We can do about 10 blogs a week without it being flagged as spam. We have five working drafts this week.

**Carly Piekos:** For alt tag recommendations, I've got that sorted. She'll add alt tags to all new content moving forward and work through the backlog.

**Kim Lu:** Once I organize the publishing schedule, she'll add the alt tags, so you don't have to worry about it.

**Carly Piekos:** I've added your structured data to the Google Drive under SEO Technical Resources. Do you have access to the Drive?

**Kim Lu:** I don't recall being added. Sophia, Maura, do you have access?

**Sophia Silver:** I need to double check.

**Maura Kelly:** I don't believe so.

**Carly Piekos:** Let me reshare it in the chat. That's where I'll also put your tech audit for next week.

**Carly Piekos:** I ran an AI visibility checker on one of your blog pages. I spot check with this tool to ensure your content is readable by AI models. Your citation readability might be affected by JavaScript, which AI models struggle to read. The Adobe LLLM Optimizer shows what humans see versus what bots see. One client we worked with had only 10% visibility. Your robots.txt looks fine for now. We can optimize crawl directives later if needed.

**Kim Lu:** Is the structured data accessible?

**Carly Piekos:** Yes. In the structured data folder, you'll find a Webflow implementation guide and quick reference guide. Fill in the code templates with your data and publish via Google Tag Manager.

**Kim Lu:** We do have Google Tag Manager. I'll run this by the Webflow team.

**Carly Piekos:** It's very easy and won't break anything in GTM. Now let's review CheckThat.

**Carly Piekos:** Here's your CheckThat performance dashboard. We use a shared library of 100,000 prompts tracked across 1,500+ categories. In Design & Creative, for example, Blender is down 24% this week. I've moved your prompts from Scrunch and added them slowly to get clean data. We also added your business context and buyer personas (Designer, Product Designer) to customize the prompts. When you select prompts, you get historic data immediately since we're already tracking them.

You'll have 90-day Business Premium access for beta feedback. The platform is still rough around the edges, but customer feedback will improve it. I'll send you access this afternoon. The generic prompt generators use a competitor approach with your business context. If you go into Sources, you'll see where you're competing for specific prompts and how to pivot your strategy.

**Carly Piekos:** The Categories view is best. You can see competitor tracking, visibility, mentions, and trends week over week. The Citations & Mentions section shows what you should write about, plus company overviews with products, target market, buyers, personas, and pricing.

**Kim Lu:** This could help with competitive research to find content gaps.

**Carly Piekos:** Exactly. You can add competitors by clicking the button and entering the URL. Regarding brands that lose visibility, it's usually seasonality or lower search volume across the industry. If you drop 5% but competitors drop 15-30%, you're doing relatively well.

For specific prompts, you can see presence across ChatGPT, Google AI Overview, Google AI Mode, Perplexity, and Claude. Note that Claude doesn't do citations, so focus on ChatGPT, Google, and Perplexity.

**Kim Lu:** I'll get access and start digging in?

**Carly Piekos:** I'll send you access info today and include you in the beta group.

**Carly Piekos:** Your performance has been trending upward since November—organic sessions, engaged sessions, and engagement rate are all increasing. This is great post-migration since migrations typically cause drops. We'll break down performance by content pillars as you publish, so we can identify which content performs best and double down on those categories. Then we can figure out attribution to your actual conversions.

**Kim Lu:** We need to nail down signups and demo request goals. Before the launch, we were at 550 signups/week. Now we're averaging 330-450/week. Let's target 550-650 weekly signups and maintain 90-100 demo requests.

**Carly Piekos:** Are you tracking these in Broadway or GA4?

**Kim Lu:** Broadway pulls GA4 data. Demo requests are manual counts from Google Sheets, but we're implementing tracking on all submit buttons now.

**Carly Piekos:** Share that data so I can create realistic goals. I want to build a blog attribution pipeline and tailor CTAs by content type. Right now all CTAs push to the homepage. We should map them to specific pages: Top-of-Funnel → product pages, Bottom-of-Funnel → demo requests.

**Sophia Silver:** Could the product overview page be another CTA destination?

**Kim Lu:** Good idea. We can recommend CTAs as we review drafts this week. Top-of-funnel content might be too cold for direct demo requests—we need a landing pad approach for middle-funnel content.

**Carly Piekos:** I'll note the signup and demo goals. We'll do a migration tech audit next week. I'm sending Monday updates instead of Slack alerts to avoid overwhelming you. I'll tag the Vizcom team in the actions tab.

**Kim Lu:** We'll review those 12 drafts and get you reporting access or share graphs from the Webflow team.

**Carly Piekos:** Perfect. Thank you. Have a great week.

**Kim Lu:** Likewise. Bye.
