# Vizcom <> Growth X - Weekly Syncs

<metadata>
date: 2026-01-27
time: 17:30 UTC
duration: 37 minutes
organizer: team@growthxlabs.com
source: fathom
fathom_recording_id: 117502549
fathom_url: https://fathom.video/calls/544435745
share_url: https://fathom.video/share/xPiB-HyzhCqDr4sqzL7pR3EsK1JCTM5B
enriched_on: 2026-02-28 14:32 UTC

participants:
  - name: Kim Lu
    email: kimberley.lu@vizcom.co
    affiliation: Vizcom
    role: Project lead
    speaker: true
  - name: Maura Kelly
    email: maura.kelly@vizcom.co
    affiliation: Vizcom
    role: Content lead
    speaker: true
  - name: Carly Piekos
    email: carly@growthx.ai
    affiliation: GrowthX
    role: Content strategist & SEO lead
    speaker: true
  - name: Aida Knezevic
    email: aida@growthx.ai
    affiliation: GrowthX
    speaker: false
  - name: Andreina Coronado
    email: andreina.coronado@vizcom.co
    affiliation: Vizcom
    speaker: false
  - name: Emily Lonetto
    email: emily.lonetto@vizcom.co
    affiliation: Vizcom
    speaker: false
  - name: Sophia Silver
    email: sophia.silver@vizcom.co
    affiliation: Vizcom
    speaker: false
  - name: Chris
    email: chris@vizcom.co
    affiliation: Vizcom
    speaker: false
</metadata>

---

## Summary

Weekly sync to unblock article publication (12 staged articles waiting for images), resolve technical SEO issues post-migration, and align on 2026 goals: driving signups and demo requests via organic content. Carly (GrowthX) walked through Google Search Console errors, robots.txt optimization, and CheckThat platform for AEO tracking. Kim Lu (Vizcom) confirmed baseline data needed to prove ROI of non-branded content strategy.

---

## Context

Vizcom partnered with GrowthX to establish a non-branded, organic content strategy aimed at driving signups and demo requests. The engagement includes weekly content production (5 articles/week target, currently 12 staged), technical SEO support post-site migration, and access to CheckThat (GrowthX's proprietary AEO tracking platform). This sync focused on operational blockers delaying publication and technical debt from the recent site migration that was wasting crawl budget and preventing new pages (e.g., University courses) from being indexed. GrowthX is using weekly Looker Studio dashboards to track performance metrics (organic/referral traffic, engagement) and CheckThat to monitor how Vizcom ranks across multiple AI search engines (ChatGPT, Perplexity, Claude, Google Gemini, Google AI Overviews).

---

## Relevance

**Content Operations**
- Publishing bottleneck: 12 staged articles + unknown number of December imports cannot launch without images. Blocking momentum on content ROI proof.
- Image generation workflow finalized: AI-generated images now staged directly in CMS with minor "sketchy elements." Vizcom will approve/reject and request alternatives if needed.
- Slack automation: Auto-alert when articles staged in Webflow; notifies Kim Lu and Maura Kelly for review/publish decisions.

**Technical SEO & Migration Cleanup**
- 404 errors from migration creating crawl budget waste. Redirects needed for all non-existent pages to priority pages (e.g., webinar).
- New pages (University courses) not auto-indexed; manual URL inspection in Google Search Console required to trigger crawl priority.
- Sitemap status unclear: may be static (requires manual page additions) or dynamic. Vizcom checking with Kaelin (developer).
- Robots.txt needs optimization: disallow crawling of parameter URLs (?, #) to focus budget on content that drives business value.

**AEO & Performance Tracking**
- CheckThat platform: GrowthX proprietary tool tracking Vizcom's visibility across 5 AI engines. Team access costs extra; GrowthX provides reporting baseline.
- Looker Studio: Weekly dashboard (updates Sundays) showing organic/referral traffic, engagement rate, session counts. Carly will email access link.
- 2026 North Star: 50/50 or 60/40 split between self-serve signups and sales-assisted demo requests. Kim Lu pulling quarterly targets for Carly.
- Competitive monitoring: Vizcom competitor list in CheckThat; Kim Lu reviewing additions with team.
- Non-branded content ROI: Kim Lu requesting baseline data (pre/post migration) for non-branded queries to prove case to CEO that organic investment drives net new traffic.

---

## Overview

- **Publishing Blocked:** 12 new articles and an unknown number of older drafts are ready but lack images, preventing publication.
- **Image Workflow Resolved:** GrowthX will now add images directly to the CMS staging environment, unblocking the publishing queue.
- **Technical SEO Plan:** A plan was set to fix Google Search Console errors (404s, crawl budget waste) via redirects, sitemap updates, and a `robots.txt` file.
- **2026 Goal Defined:** The primary objective is to drive signups and demo requests, with a target 50/50 split between self-serve and sales-assisted leads.

---

## Key Topics

### Content Publishing Blockers

  - **Problem:** Articles are ready but cannot be published without images.
      - **New Articles:** 12 drafts are ready for review in the Airtable interface.
      - **Older Drafts:** An unknown number of articles imported in December also lack images.
  - **Solution:** GrowthX will now add images directly to the CMS staging environment, unblocking the publishing process.
      - **Rationale:** This bypasses the previous workflow of sharing images in Google Docs, which was inefficient for review and upload.
      - **Image Quality:** AI-generated images have minor "sketchy elements" due to current AI limitations. Vizcom will review them and can request alternatives.
  - **Process Improvement:** GrowthX will set up an auto-alert in the shared Slack channel when articles are staged, ensuring Vizcom has immediate visibility.

### Technical SEO & Indexing

  - **Problem:** Google Search Console (GSC) shows indexing errors, wasting crawl budget and hurting visibility.
  - **Analysis:**
      - **Expected:** Redirects from the recent site migration are normal.
      - **Critical:** 404 "Not Found" errors must be fixed with redirects to prevent crawl budget waste.
      - **New Pages:** New pages (e.g., University courses) require manual URL inspection in GSC to prompt faster indexing.
  - **Solution:**
      - **Redirects:** Implement 301 redirects for all 404 pages.
      - **Sitemap:** Verify if the sitemap is dynamic; if not, new pages must be added manually.
      - **`robots.txt`:** Update the file to disallow crawling of low-value pages (e.g., URLs with `?` or `#`), focusing crawl budget on important content.
      - **Technical Audit:** GrowthX will run a Screaming Frog audit to identify and prioritize 3-4 urgent post-migration fixes.

### Performance Tracking & Goals

  - **Tooling:**
      - **Looker Studio:** The existing dashboard tracks organic and referral traffic, updating weekly. Vizcom will receive access.
      - **CheckThat:** GrowthX's proprietary AEO tracking platform. GrowthX will provide reporting; direct team access is an extra cost.
  - **2026 North Star Goal:** Drive signups and demo requests.
      - **Target Split:** 50/50 or 60/40 between self-serve signups and sales-assisted demo requests.
      - **Key Metric:** Prove the ROI of non-branded content to justify investment.
  - **GrowthX Support:** GrowthX will pull baseline data and keyword recommendations to support the non-branded content strategy.

---

## Action Items

**Kim Lu (Vizcom)**
- Export list of staged articles missing images; share with Carly Piekos (GrowthX)
- Set up 301 redirect for 404 webinar page
- Start thread with Kaelin (dev) re: dynamic sitemap functionality
- Review CheckThat competitor list; send additions to Carly Piekos (GrowthX)
- Share quarterly signup/demo targets with Carly Piekos (GrowthX)

**Carly Piekos (GrowthX)**
- Add alt-tag recommendations to staged articles
- Create 'Technical' Drive folder; add robots.txt, sitemap, and structured-data implementation docs
- Update robots.txt to disallow parameter URLs (?); then run Screaming Frog technical audit
- Inspect/index 'Discovered - currently not indexed' URLs in Google Search Console (manual priority crawl requests)
- Email Looker Studio access link to Kim Lu and Maura Kelly (Vizcom)
- Pull Google Search Console baseline data (pre/post migration) for non-branded queries
- Provide low-difficulty, high-impact non-branded keyword recommendations
- Set up Slack auto-alert for when articles are staged in Webflow; notify Kim Lu and Maura Kelly for review/publish

---

## Transcript

### Image Generation & Article Staging

**Kim Lu (Vizcom):** This meeting is being recorded. Let's discuss the image situation and technical SEO issues.

**Carly Piekos (GrowthX):** I have updates. Maura and I met Friday with our image generator. The managing editor regenerated all images for the staged articles. They'll go into the staging environment with multiple options to pick from. I created a simplified Airtable interface for you to see what needs review this week.

**Maura Kelly (Vizcom):** I don't think I've been tagged for any images yet.

**Carly Piekos:** You're one of the editors. Images will be in Google Docs or a Drive folder. All staged ones are approved—I just need to confirm the delivery format with our image generator.

**Kim Lu:** We have 12 articles staged recently, plus older articles from December that also need images. I want to make sure we're covering both. I can pull a list.

**Carly Piekos:** She's working on five drafts for next week. Once we get the images, I'll add alt-tag recommendations. The AI images have minor sketchy elements, so she's selecting the best ones.

### Technical SEO & Google Search Console

**Kim Lu:** I noticed some pages aren't being indexed in Google Search Console. Anything we need to fix on our end?

**Carly Piekos:** Pages with question marks, hashtags, or special characters don't need to be indexed. What matters is that important pages are indexed in HTTPS. Redirects from the migration are expected. The real issue is 404 errors wasting crawl budget.

**Kim Lu:** Should we set up 301 redirects for the 404 pages?

**Carly Piekos:** Yes. For new pages like your University courses, manually inspect the URL in Google Search Console to prioritize crawling. Your sitemap has 146 pages—check if it's dynamic or static. If static, you need to manually add new pages to it.

**Kim Lu:** I'll check with Kaelin about dynamic sitemap generation.

**Carly Piekos:** Good. I'm also updating your robots.txt to disallow crawling of parameter URLs (ones with ? marks). I'll create a Technical folder with robots.txt, sitemap, and structured-data implementation docs for you. Then I'll run a Screaming Frog audit to identify 3-4 urgent post-migration fixes.

### CheckThat Platform & Competitive Analysis

**Kim Lu:** What is CheckThat? Is that an in-house tool for AEO tracking?

**Carly Piekos:** Yes. CheckThat is GrowthX's proprietary AEO tracking platform. It replaces Scrunch for this year—you get it free with the contract. It tracks how you rank across ChatGPT, Perplexity, Claude, Google Gemini, and Google AI Overviews. Team access costs extra, but I provide reporting and insights as part of the engagement.

**Kim Lu:** I see competitive analysis in CheckThat. Can we use that to understand how competitors rank for AEO and SEO?

**Carly Piekos:** Absolutely. I've already added your competitors to CheckThat. Can you review the list and send back additions?

### Performance Tracking & 2026 Goals

**Carly Piekos:** You have access to a Looker Studio dashboard that tracks organic and referral traffic. It updates every Sunday. I'll send you the access link. What's your North Star goal for 2026?

**Kim Lu:** Driving signups and demo requests. We're currently demo-request heavy but want to build the self-serve side. We're targeting a 50/50 or 60/40 split between self-serve signups and sales-assisted demo requests.

**Carly Piekos:** Do you have quarterly targets? The more specific you are, the better I can optimize content, internal linking, and site health to funnel traffic to demo/signup pages.

**Kim Lu:** I can pull quarterly targets. The bigger ask—we've never invested in non-branded search. Can you show baseline data (pre/post migration) on how non-branded content drives net new traffic? That will help us justify the investment to our CEO.

**Carly Piekos:** Absolutely. I'll pull Google Search Console baseline data on queries and pages before/after. I'll also provide low-difficulty, high-impact non-branded keyword recommendations. SEO isn't dead—we want to rank on page one for non-branded queries and get your brand visibility up.

### Closing & Next Steps

**Kim Lu:** When articles are staged, can you ping us on Slack so we know which ones to review and publish?

**Carly Piekos:** Yes. I'll set up an auto-alert in Slack when articles are staged in Webflow and notify you and Maura. The images will be in staging—once you approve them, you can hit publish.
