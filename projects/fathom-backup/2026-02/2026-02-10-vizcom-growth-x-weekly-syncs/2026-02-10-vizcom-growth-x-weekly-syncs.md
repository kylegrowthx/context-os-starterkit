# Vizcom <> Growth X - Weekly Syncs

<metadata>
date: 2026-02-10
time: 17:30 UTC
duration: 29 minutes
organizer: team@growthxlabs.com
participants: Carly Piekos (GrowthX), Sophia Silver (Vizcom), Kim Lu (Vizcom), Andreina Coronado (Vizcom), Emily Lonetto (Vizcom), Maura Kelly (Vizcom), Chris (Vizcom)
fathom_recording_id: 121257893
fathom_url: https://fathom.video/calls/561182206
share_url: https://fathom.video/share/hmA3ezWeyc4o1u7zj8osXUQ8hqvzb6yb
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

Carly Piekos reported on critical technical SEO findings from a post-migration audit, including a rare server loopback issue, 22 404 pages, and 44 orphaned URLs. The team discussed restructuring Vizcom's blog around category subpaths to improve UX and SEO, with breadcrumb navigation guiding users through a clearer hierarchy. Kim Lu requested view-only GTM access for Carly to troubleshoot undefined variables blocking dynamic schema configuration, while the content pipeline continues with 14 drafts ready for review and comparative listicles on hold pending internal alignment on competitor content strategy.

---

## Context

Vizcom is a B2B SaaS company working with GrowthX on SEO, content strategy, and technical site health following a recent website migration. The team manages a substantial blog content pipeline (~10 articles/week to clear backlog, then 5/week cadence) and is focused on improving organic visibility through better site architecture, content hierarchy, and schema implementation. Kim Lu leads technical GTM work while Carly Piekos, GrowthX's content strategist, audits site performance and guides content prioritization. This weekly sync serves as the primary forum for aligning on technical debt, content strategy adjustments, and publishing roadmap decisions.

---

## Relevance

- **SEO & Site Health:** Critical post-migration technical issues require immediate resolution (server loopback, 404s, orphaned URLs, missing H1s).
- **Schema & LLM Visibility:** GTM schema configuration is blocking rich results and LLM visibility; dynamic variable setup needs expert review.
- **Content Strategy:** Blog redesign with category subpaths aligns with UX best practices and creates better information architecture for users and search engines.
- **Publishing & Backlog:** Content pipeline status review ensures alignment on what ships this week and what stays paused pending internal approvals.
- **Access & Tooling:** Kim Lu must grant Carly GTM view-only access to unblock troubleshooting; roadway performance reports needed for next week's sync.

---

## Overview

- **GTM Schema Blocked:** Dynamic schema setup is blocked by undefined variables in GTM. Carly will investigate after receiving view-only access.
- **Blog Redesign Approved:** The blog will be restructured with category subpaths (e.g., `/blog/product-updates/`) to improve UX and create a clear SEO hierarchy.
- **Critical Site Issues Found:** A technical audit revealed a server loopback issue, 22 404s, and 44 orphaned URLs requiring immediate attention.
- **Content Pipeline Paused:** 14 drafts are ready for review, but comparative listicles are on hold pending internal alignment on competitor-focused content strategy.

---

## Key Topics

### Technical SEO Audit Findings

  - A technical crawl identified several critical issues post-migration.
  - **Major Issues:**
      - **Server Loopback:** A rare server issue affecting all indexed pages. Carly is researching a fix.
      - **404 Errors:** 22 pages return 404s; Vizcom must decide whether to redirect or restore them.
      - **Orphaned URLs:** 44 pages exist in the sitemap but have no internal links, preventing them from being crawled and ranked.
      - **Missing H1s:** Several URLs lack H1 tags, a key SEO element.
      - **Empty Content Pages:** Indexable pages with placeholder content were found, suggesting they were published accidentally.
  - **Warnings:** Minor issues like links without internal outlinks were noted but are not high priority.

### GTM Schema Implementation

  - **Problem:** Dynamic schema setup in GTM is failing due to undefined variables (e.g., `page title`, `meta description`).
  - **Diagnosis:** The GTM preview and Google's Rich Results Test both confirm the variables are not being pulled correctly.
  - **Action:** Carly will investigate the correct dynamic variable configuration after receiving view-only GTM access.
  - **Note:** The `Organization` schema tag must be restricted to the homepage only.

### Blog Strategy & Redesign

  - **Problem:** The current blog hub page is visually overwhelming due to large featured posts and a flat structure, creating a poor user experience.
  - **Solution:** Restructure the blog around category subpaths.
      - **Hub Page:** Feature one hero post and small grids for each category (e.g., Product Updates, Community).
      - **Category Pages:** Each category becomes a dedicated page with its own URL (e.g., `/blog/product-updates/`).
      - **Breadcrumbs:** Implement breadcrumb navigation on individual articles to show the user's path (e.g., Home \> Blog \> Category \> Article).
  - **Rationale:** This creates a clear hierarchy for users and search engines, improving UX and SEO.

### Content Pipeline & Publishing

  - **Status:**
      - 14 drafts are ready for review.
      - 5 new drafts are in progress.
      - 4 articles are being revised today based on Vizcom's feedback.
  - **Publishing Plan:**
      - **Cadence:** Publish \~10 articles/week to clear the backlog, then return to the standard 5/week.
      - **Blocker:** Comparative listicles are on hold pending internal alignment on competitor-focused content strategy.
  - **Next Step:** Vizcom to approve topics in the "Considering" tab of the content tracker.

---

## Action Items

**Carly Piekos (GrowthX)**
- Upload meeting recording to call notes
- Set listicle/comparative blog drafts to 'waiting' status
- Re-check Google indexing for published articles
- Upload technical crawl report to shared Drive; send Kim 404s + H1-missing lists
- Investigate server loopback; send step-by-step fix to Kim
- Investigate placeholder-content indexable pages; report findings to Kim

**Kim Lu (Vizcom)**
- Grant Carly GTM view-only access (carly@growthx.do.ai); coordinate with Kaylin if needed for admin approval
- Approve blog topics in 'Considering' doc; then Carly finish editing listicles
- Email Carly roadway, signups, demo request reports

---

## Transcript

**Sophia Silver:** This meeting is being recorded.

**Carly Piekos:** Hello, everyone. Happy Tuesday. How's everything going?

**Sophia Silver:** So far, so good. We might have our CEO, Jordan, join us today, but he's in an on-site in Oregon so it's TBD.

**Carly Piekos:** All right. Well, I'll get to our agenda. Is there anything top of mind from the last week?

**Kim Lu:** Yes, Google Tag Manager. I was setting up the schema implementation and ran into an error with the variables. I'm not sure if I need to add variables for featured image, meta description, and others directly in GTM.

**Carly Piekos:** Let me take a look. Can you show me what the error looks like?

**Kim Lu:** I just followed the Google Doc you provided, which was very helpful. When I run preview, it gives an error that the variable in the HTML snippet is not defined.

**Carly Piekos:** Let me see the variables section. Can you open that? I just want to see what it looks like.

**Kim Lu:** All the variables seem undefined—page title, featured image, everything.

**Carly Piekos:** Let me check the configuration. So it says data variable not defined and there's no meta variable. I don't think that should be a big issue. Did you test this in the preview?

**Kim Lu:** Right, when I run preview, it says page title not found.

**Carly Piekos:** OK, within this schema we need to fill out: page title, description, meta description, featured image, publisher. If we're going to do a generalized approach for the blog path pages meta descriptions, we need to figure out how to dynamically pull that in. Let me look into this further before you put more effort into it. Good call on not publishing it yet. Did you test this in Google's Rich Results Test?

**Kim Lu:** No, I didn't.

**Carly Piekos:** Let's test it there. You can paste the schema code and it will tell you where the errors are. Let me see... "No items detected." I think it's because we have the Organization schema set to all pages, but it should be restricted to the homepage only. I've always done this by page, so I'm trying to figure out the dynamic approach. Let me look further into this before you go any further. I'll get back to you today.

**Kim Lu:** Yeah, no worries. Do you have access to our Tag Manager?

**Carly Piekos:** I don't have access, but if you could give me view-only access that would be super helpful. My email is carly@growthx.do.ai. This is medium to low priority—mainly for LLM visibility boost.

**Sophia Silver:** That might be a Kaylin request, Kim. He might be an admin in Tag Manager.

**Carly Piekos:** View-only is fine so you know I'm not doing anything in the background. I just want to see it without having to inspect the code on the site since it's not published yet.

**Kim Lu:** Cool. I'll get that sorted.

**Carly Piekos:** Great. What I did uncover today are a few technical issues I wanted to go over. The revisions will be complete today—about four articles need edits. We're working on five new drafts this week, and you have 14 drafts ready for review. I broke everything out by publishing week.

**Kim Lu:** I've reviewed those 14 drafts and commented on the Google Docs.

**Carly Piekos:** Perfect. Google Docs is ideal because I can check the version history and see when you commented. Jenny will get an alert and can make edits almost immediately.

**Kim Lu:** One small note—some of this batch are comparative listicle content. We might want to hold off on publishing those given our uncertain stance on comparative content.

**Carly Piekos:** Is this something that just came up or do you need more strategic thinking around it?

**Kim Lu:** It's been a theme about how we want to talk about competitors in our written content. We're not confident as a team yet, so let's hold off on those for now. Everything else should be good to publish.

**Carly Piekos:** Would you like me to change the listicle status to "waiting" instead of staged?

**Kim Lu:** Yes, that would be helpful. But we'll review everything in Webflow before we publish anyway.

**Carly Piekos:** All right. For published articles, I ran them through Google Search Console and requested indexing for pages that weren't indexed. I'll do another check next week to confirm everything's indexed properly. It should take about a week to see traction. For the publishing cadence, I suggest around 10 articles/week to clear the backlog, then back to 5/week. We'll need you to approve additional topics in the "Considering" tab. I didn't pull performance data today since the articles need time to gain traction. That's for next week.

**Kim Lu:** Sounds good. We'll also want to publish the next batch to cascade the momentum.

**Carly Piekos:** Absolutely. So I did a technical crawl and I'm putting the report in our shared Google Drive. I found several critical issues post-migration. One is a rare server loopback issue—I've only come across this twice in my career. It might affect about 100 pages that are currently indexed. I'll provide a detailed step-by-step analysis on how to fix it. You also have 22 pages returning 404s. I'm not sure if these need redirects or if they're pages of value. I'll send you the list with descriptions and fix recommendations. The sitemap updates dynamically, so I crawled again this morning. The 44 orphaned URLs haven't changed. We need to review them and add internal links so they can be crawled and ranked. Several URLs are also missing H1s, and I'll send those lists too. There are also indexable pages with placeholder content—I wonder if those are published accidentally.

**Sophia Silver:** That could be a page that's published when it shouldn't be.

**Carly Piekos:** Yeah, that's possible. I'll investigate further. Your warnings are mostly fine. JavaScript issues are outside your control. We have about seven major issues and a couple of warnings to address.

**Kim Lu:** Got it.

**Carly Piekos:** Now let me go over the blog layout. I put together UX improvements and recommendations based on what other clients are doing and best practices for blogs in Webflow. The current issue is that you have four large feature posts with massive images, author headshots, and long excerpts—it's a visual overload. What I'd recommend is using one hero featured post that feeds into category pages, then having mini grids for each category instead of everything on one page. The expected impact is about a 50% reduction in cognitive overload. Having that hierarchy is also more helpful for LLM visibility and SEO.

**Sophia Silver:** So you mean the card grids we have below—move those up?

**Carly Piekos:** Let me pull up the page. You have cards here organized by category. Right now you have "All," which is redundant since we're on the All page. We could make Product Updates, Insights, Community, Creators as their own separate hub pages. So Product Updates would be at /blog/product-updates/, and the breadcrumb would flow from there. Each tag would become an individual page.

**Sophia Silver:** So the tags would become individual pages themselves?

**Carly Piekos:** Exactly. The structure would be Home > Blog > Product Updates > Article. This creates much better UX. Breadcrumbs are great for blogs because people don't get overwhelmed by content, and they can navigate the user journey. Structurally, subpaths are better than query parameters for SEO and LLM visibility.

**Kim Lu:** Is the subpath better than our current tag-based URL structure?

**Carly Piekos:** Yes, for most cases. In your case, the subpath would be really useful for navigating back and forth. Usually breadcrumbs go at the top of the page, but for this design I'd just have them in the URL structure. Then when you click into a category, you'd see the breadcrumb display at the top of the page—Home > Blog > Product Updates > Article. Breaking it into mini hubs and category pages makes sense when you have this much content. It helps with UX and search engine crawlability. I've put this in our shared folder with effort level and timeline estimates.

**Kim Lu:** Thank you. This is really helpful.

**Carly Piekos:** Of course. The effort level is moderate. We can do redirects and configure gradually. It's not urgent, but it's the best user experience for your visitors and LLM models. So I'll investigate the schema markup, make sure the revisions are good to go, and once I get GTM access I'll test everything. I'll also keep an eye on performance tracking using the goals we discussed last week.

**Kim Lu:** Perfect. I'll also email you the roadway, signups, and demo request reports.

**Carly Piekos:** Great. Those will be helpful for tracking performance. Are there any other questions or adjustments?

**Kim Lu:** No, I don't think so.

**Carly Piekos:** That's wonderful. If you need anything this week, let me know. I'll test that schema and get you an update by end of week.

**Sophia Silver:** Sounds great. Thank you.

**Kim Lu:** Thank you. Have a great rest of your week.

**Carly Piekos:** You too. Bye.
