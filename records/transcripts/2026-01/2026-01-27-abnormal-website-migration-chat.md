# Abnormal - Website migration chat

<metadata>
date: 2026-01-27
time: 21:00 UTC
duration: 30 minutes
organizer: jo@growthx.ai
participants:
  - name: Jo Kaminska
    email: jo@growthx.ai
    affiliation: GrowthX
    role: Director, Content Marketing
  - name: Meaghan Winston
    email: mwinston@abnormal.ai
    affiliation: Abnormal Security
    role: Web Content Manager
  - name: Kyle Gaudreau
    email: kyle@growthxlabs.com
    affiliation: GrowthX Labs
    role: (Invited, not present)
  - name: W Duff
    email: wduff@abnormalsecurity.com
    affiliation: Abnormal Security
    role: (Invited, not present)
fathom_recording_id: 117606925
fathom_url: https://fathom.video/calls/547357528
share_url: https://fathom.video/share/hoN54sxcYa3Y82YctJZgDLcVhY7J85bS
source: fathom
enriched_on: 2026-02-28 12:00 UTC
</metadata>

---

## Summary

Jo Kaminska (GrowthX) and Meaghan Winston (Abnormal Security) aligned on the website migration strategy for Abnormal's ContentStack migration (Feb 6 - Mar 31, 2026). Blog URLs remain unchanged to preserve SEO value; the `/ai-glossary/` subfolder consolidates into `/glossary/` with 301 redirects. A new `/educational-hub/` subfolder will host experimental content with A/B testing and personalization capabilities. The team will audit ~500 articles using a shared migration spreadsheet to categorize content as keep, merge, or retire based on performance data.

---

## Context

Abnormal Security is migrating its website to ContentStack as part of a larger product and web strategy redesign. GrowthX provides content marketing services to Abnormal and produces blog and glossary content published on the company's website. This migration requires careful URL planning to avoid breaking existing organic search rankings and internal link structures. The current site has redundant glossaries (AI glossary and regular glossary), inconsistent URL structures for resources and solutions pages, and needs content consolidation. A structured migration spreadsheet will be the single source of truth for tracking which content to keep, consolidate, or retire.

---

## Relevance

**Strategic Importance**
- Website migration directly affects GrowthX's published content; URL changes could impact organic traffic and SEO metrics
- New `/educational-hub/` subfolder creates opportunities for A/B testing and content experimentation at scale
- Content consolidation strategy aligns with GrowthX's emphasis on quality over quantity

**Operational Impact**
- GrowthX must track ~500 articles across the migration and identify performance data (traffic, keywords, rankings)
- Post-migration internal link audit using Screaming Frog will be needed to fix broken links in Solutions/Resources sections
- Monday status updates from Jo will keep the project on track

**Future Considerations**
- Resources URLs will be restructured to include asset type (e.g., `/resources/report/` instead of just `/resources/`)
- Product pages may adopt a parent-child URL structure (e.g., `/products/cloud-email-security/feature-x/`) post-MVP
- Solutions pages will be reorganized under a new `/what-we-protect/` directory (redirects required)

---

## Overview

- **Blog URLs are unchanged** to preserve SEO value. The `/ai-glossary/` subfolder is being consolidated into `/glossary/` with 301 redirects to improve user experience.
- **A new `/educational-hub/` subfolder** will be created for new content, enabling A/B testing and personalization in ContentStack.
- **A shared migration spreadsheet** will be used to audit \~500 GrowthX articles, informing decisions to keep, merge, or retire content based on performance data.
- **URL structures for `Solutions` and `Resources` will change**, requiring a post-migration audit to fix broken internal links.

---

## Key Topics

### URL Structure & SEO Strategy

  - **Blog Content:** URLs will remain unchanged to preserve existing SEO value.
  - **Glossary Consolidation:** The `/ai-glossary/` subfolder will be merged into `/glossary/`.
      - **Rationale:** Improves user experience and simplifies reporting.
      - **Action:** All `/ai-glossary/` pages will be redirected via permanent 301s.
  - **New Educational Hub:** A new `/educational-hub/` subfolder will be created for all new content.
      - **Rationale:** Enables experimentation (A/B testing, personalization) in ContentStack to optimize for conversion.
  - **Content Culling:** Older, underperforming content (e.g., from 2020–2022) will be retired to improve SEO efficiency.

### Migration Spreadsheet & Audit Plan

  - A shared spreadsheet will be the single source of truth for the audit.
      - Jo will add performance data (traffic, keywords) to Meaghan's existing list of \~500 GrowthX articles.
      - **Action Categories:**
          - **Keep:** High-performing content.
          - **Merge:** Overlapping content → consolidate into a single page.
          - **Retire:** Underperforming content.
  - **Internal Link Audit:** A post-migration crawl (Screaming Frog) will identify and fix broken links.
      - **Rationale:** Necessary due to URL changes in `Solutions` and `Resources`.

### Future URL Changes (Post-MVP)

  - **Resources:** URLs will be updated to include asset type (e.g., `/resources/report/`).
  - **Product Pages:** A parent-child structure is planned for better organization.
      - **Example:** `/products/cloud-email-security/feature-x/`
      - **Rationale:** Prioritizes user experience over potential URL length concerns.
  - **Solutions:** Pages will be moved under a new `/what-we-protect/` directory.
      - **Rationale:** The current `Solutions` pages are mislabeled platform descriptions, not true solutions.

---

## Action Items

**Jo Kaminska (GrowthX)**
- Analyze AI glossary traffic; share findings w/ Meaghan
- Share migration template w/ Meaghan; then build migration sheet on her tab
- Audit internal links to Solutions/Resources; then run post-migration Screaming Frog crawl
- Discuss product parent-child URL options w/ GrowthX team; share feedback w/ Meaghan
- Send Monday migration status update to Meaghan (due: 2026-02-03)

**Meaghan Winston (Abnormal Security)**
- Share Solutions/Resources URL structure and redirect plan w/ Jo (due: 2026-01-30, by Thursday)
- Finalize navigation structure with CEO; provide comprehensive write-up of all URL changes to GrowthX team

---

## Transcript

**Jo Kaminska:** This meeting is being recorded.

**Meaghan Winston:** Hi, how are you?

**Jo Kaminska:** I'm good. I actually moved a bit to be in a better climate. I'm in Columbia right now, which is pleasant—spring-like temperature.

**Meaghan Winston:** Oh, I'm jealous! I'm in New Orleans. I'm from here originally. I lived in Chicago, then Nashville, then moved back in 2021. We don't usually get proper winters, but the last few years have been colder—a few weeks in January where it's around 30 degrees.

**Jo Kaminska:** I normally live in Lisbon, which is pretty much the same—humid and around 50 degrees Fahrenheit, but no central heating, so you end up wearing five layers inside while it's warmer outside.

**Meaghan Winston:** I almost moved to Belgium last year. I spent a lot of time in Europe and really wanted to go to Portugal, but haven't had the chance yet. It's on my list for this year. I hear wonderful things about Lisbon.

**Jo Kaminska:** Yeah, Lisbon is great. Thanks for joining the call.

**Meaghan Winston:** Thank you.

**Jo Kaminska:** So I think we should talk about the plan. I prepared a couple of assets. This will be our main hub for everything migration-related. We have the confirmed dates: February 6th through March. Your requests align well with what we plan to check. I wanted to chat about the new website structure and URL strategy, because that's my biggest concern. Especially since what we produce for you is blog articles and glossary pages.

**Meaghan Winston:** So my plan was not to change the blog URL structure for this first iteration. It would cause too much confusion to change URLs from the old system to the new system, especially with about 500 pieces of content. Let's keep the URLs the same. What will change is the glossaries. In our existing system, we have an AI glossary and a regular glossary, but we won't have two glossaries in the new system. Everything will be under /glossary/ without the AI subdirectory. All /ai-glossary/ pages will be redirected via permanent 301s.

**Jo Kaminska:** Okay, so this is the only major URL change? I can check the current traffic for those AI glossary pieces, since glossary is currently the majority of our organic traffic. But with permanent 301 redirects, it shouldn't be an issue.

**Meaghan Winston:** Yeah, I expect a small dip post-migration—we always see that. But I wanted to maintain consistency. Having two glossaries is confusing for users, and housing them in one place makes more sense. Plus, it simplifies reporting.

**Jo Kaminska:** Absolutely, and these glossary pages could technically be the Educational Hub, but I wouldn't retroactively tag them as such. I'd just migrate them as you suggest—keep the blog structure as-is, and then Educational Hub will be a separate subfolder where we start building from scratch.

**Meaghan Winston:** I like that plan. It gives you more flexibility in what you build. This program is important and has executive buy-in, so I don't want to be a blocker. ContentStack lets us do A/B testing and personalization natively, which gives us flexibility in learning how to optimize. Our current blog templates aren't optimized for conversion, so this is exciting.

**Jo Kaminska:** Right. We could do A/B testing once we get more traffic to the hub. For current blog pages, we're doing one-to-one redirects to the blog—no changes before migration. Many are performing well, but the next step is identifying underperforming content to retire. Usually, reducing page count increases overall traffic because the SEO budget is more efficient.

**Meaghan Winston:** Exactly. That's what I was trying to do with this migration plan. We have too much content overall. We're not carrying over most blogs from 2020–2022, only a select few with high traffic or strong brand relevance. I'm trying to get the team to cull content, especially given the volume we're now producing.

**Jo Kaminska:** Do you have the migration spreadsheet? I'm planning to build one as well so we can cross-check.

**Meaghan Winston:** Yeah, let me share what I have. I pulled titles and author IDs from our system. I marked content authored by Jason as GrowthX content. We need to update the migration status and mark which entries are currently disabled. I'm working with an AI manager on this.

**Jo Kaminska:** If you send access to the spreadsheet, I could copy it to our folder or copy the tab and use formulas to check what stays unpublished and what we're publishing.

**Meaghan Winston:** How about I move all the GrowthX blog content to a new tab?

**Jo Kaminska:** That would be great. I'll send you a migration template. I'm planning to include URL path, published date, number of keywords, organic traffic (last 30/90 days), primary keyword ranking, indexation status, source page, target page (if redirected), and recommended action (keep, merge, or retire). For keep, we migrate one-to-one. For merge, we consolidate overlapping URLs. For retire, we remove underperforming pages.

**Meaghan Winston:** That structure makes sense. The only other major URL change is Resources. We're updating the structure to include asset type, so it'll be like /resources/report/ instead of just /resources/. All resources will be redirected.

**Jo Kaminska:** I'm expecting some traffic dip for that as well. This is definitely better for your strategy. Let me also check internal backlinks to Solutions and Resources so we can identify what needs to be updated.

**Meaghan Winston:** Because we are changing Solutions pages. They're not really solutions—they're platform descriptions. We're moving them under a new /what-we-protect/ directory. I'll provide the new URL structure and target pages by Thursday. Best practice for B2B cybersecurity is different from what we have now.

**Jo Kaminska:** Do you have the new URL structure for these? It matters because we might have linked to solutions pages in our content.

**Meaghan Winston:** Great question. I'll follow up with you on that by Thursday. I can also do a comprehensive write-up once our CEO finalizes the navigation structure, highlighting everything that's changing so you can account for it with content moving forward.

**Jo Kaminska:** Perfect. I'll work on your spreadsheet using the tab you created. I wanted to create a quick checklist to make sure we cover everything. Feel free to add anything missing.

**Meaghan Winston:** Very helpful. Thank you so much for all your work. I really appreciate your support.

**Jo Kaminska:** Thank you for the feedback. Feel free to reach out if you have anything to add. I'll send a Monday update next week about everything related to the migration.

**Meaghan Winston:** Awesome. Thank you so much. Have a good day.

**Jo Kaminska:** You too. Ciao.
