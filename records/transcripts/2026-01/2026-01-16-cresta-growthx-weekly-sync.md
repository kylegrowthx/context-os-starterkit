# Cresta <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-16
time: 16:00 UTC
duration: 27 minutes
organizer: team@growthxlabs.com
participants:
  - Aida Knezevic (GrowthX)
  - Annie Andrews (Cresta)
  - Devon Mychal (Cresta)
  - Russell Banzon (Cresta)
  - Nicky Budd-thanos (Cresta)
  - Courtney Ogawa (Cresta)
  - Shreha Jain (Cresta)
  - Erik O'Brien (GrowthX)
fathom_recording_id: 114905468
fathom_url: https://fathom.video/calls/534425192
share_url: https://fathom.video/share/X9vEoPtM3Y7CHmADfcatSkVr8Wrc8sta
source: fathom
enriched_on: 2026-02-28 18:42 UTC
</metadata>

---

## Summary

GrowthX and Cresta team synchronized on technical SEO remediation, lead attribution tracking, and strategic platform updates. The team resolved a critical canonicalization issue affecting indexing, defined lead SLA processes, demoed GrowthX's new "Check" AI visibility platform, and established a framework for maintaining competitive guide accuracy in a fast-moving market.

---

## Context

Cresta is an AI customer engagement platform competing in the contact center and customer service software space. GrowthX has been contracted for content marketing and SEO work to drive organic visibility and lead generation. This sync occurred during Phase 1 of the engagement, focusing on auditing and fixing foundational technical SEO issues while establishing clear metrics for content impact. The timing was critical due to recent discoveries of indexing problems affecting newly published guide content.

---

## Relevance

**Technical SEO & Site Health**
- Canonicalization fix directly impacts Cresta's ability to get content indexed at scale
- Web agency remediation progress (broken redirects, 404s) feeds into broader site audit
- GSC monitoring will inform content strategy and identify systemic indexing barriers

**Content & Lead Attribution**
- GA4 reporting ties content performance to lead generation outcomes
- HubSpot lead scoring and SLA enforcement determine which content drives qualified leads
- BOFU vs TOFU content distinction critical for measuring both guide and blog impact

**Platform Strategy & Tools**
- "Check" platform shift from Scrunch will unlock AI visibility data for competitive analysis
- Persona and funnel stage tagging enables more targeted content creation
- Planned integrations (GA4, Search Console, Fathom) unify reporting across tools

**Competitive Content**
- Quarterly guide review automation prevents outdated information from ranking
- LLM-based update checks reduce manual review overhead while maintaining accuracy

---

## Overview

- **Canonicalization fixed:** The web agency resolved the `www` vs. non-`www` URL conflict, which was causing indexing delays. Aida will monitor Google Search Console to confirm the fix and assess its full impact.
- **Lead tracking defined:** Cresta's HubSpot-based process assigns MQLs to owners with strict SLAs (1-hr for demo requests, 8-hr for content leads). Annie will build a GA4 report to track content-driven leads.
- **New AI tool demoed:** GrowthX demoed "Check," its internal AI visibility platform replacing Scrunch. It tracks Cresta and 29 competitors across \~200 prompts, using a more realistic "web search off" method for ChatGPT data.
- **Competitive content strategy set:** To keep guides current in a fast-moving market, GrowthX will build an Airtable automation to trigger quarterly reviews, using LLMs to check for competitor updates.

---

## Key Topics

### Technical SEO Audit & Fix

  - **Problem:** New content in the "guide" section was being discovered but not indexed, a symptom of a technical issue on an established site.
  - **Cause:** A canonicalization error where URLs incorrectly pointed to a `www` version, creating a conflict with the actual non-`www` site structure.
  - **Resolution:** Cresta's web agency implemented a fix in \<24 hours. The agency is also addressing other issues (broken redirects, 404s) with a target completion of EOW next week.
  - **Impact:** Aida will analyze Google Search Console to assess the issue's full scope and confirm the fix resolves indexing delays across the entire site.

### Lead Generation & Attribution

  - **Cresta's HubSpot Process:**
      - All forms → HubSpot for lead ingestion.
      - Behavior-based lead scoring triggers MQL status.
      - MQLs routed to prospecting owners with strict SLAs:
          - **1-hour:** Demo requests, Signal AI agent leads.
          - **8-hour:** Content leads.
      - Missed SLAs trigger manager alerts or lead rerouting.
  - **Attribution Need:** Aida requested reports on content-driven leads to measure the impact of both bottom-of-funnel (BOFU) and top-of-funnel (TOFU) content.
  - **Reporting Plan:** Annie will build a GA4 report to track lead generation by page, as direct HubSpot access is not feasible.

### "Check" AI Visibility Platform Demo

  - **Context:** GrowthX is replacing Scrunch with "Check," its new internal AI visibility platform.
  - **Key Features:**
      - Shared index of AI visibility across industries.
      - Tracks Cresta and 29 competitors across \~200 prompts.
      - Provides visibility and sentiment analysis for each prompt.
      - Identifies top-cited URLs to inform content strategy.
  - **ChatGPT Data Method:**
      - Uses a "web search off" method to simulate a typical user query, avoiding inflated visibility from citations.
      - Aida is confirming if the platform will also offer a "web search on" view for comparison.
  - **Integrations:** Planned for GA4, Search Console, Fathom, and PostHog. A Looker integration was requested.
  - **Access:** Cresta will gain access once the platform is ready for customers; no firm date is available.

### Content Strategy & Updates

  - **New Content:**
      - **5 articles:** Shared for review in Airtable.
      - **3 articles:** Awaiting product team feedback.
      - **3 articles:** Published by Russell yesterday.
  - **Competitive Guide Maintenance:**
      - **Problem:** Guides quickly become outdated in a fast-moving market (e.g., Sierra's new assist feature).
      - **Solution:** GrowthX will build an Airtable automation to trigger quarterly reviews for competitive guides.
      - **Process:** The review will use LLMs to compare current competitor announcements against the guide's content and flag inconsistencies.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Monitor GSC for indexing recovery; review discovered-not-indexed across site
- Schedule 20-min images feedback w/ Steve & Katya, Tue 10:30 PT
- Confirm w/ Check team ChatGPT web-search approach; update Devon
- Tag Check prompts by persona & funnel stage
- Check product team review status for 3 articles; publish if cleared
- Reschedule weekly sync 1 hr later via Slack w/ Netta
- Set up Airtable automation for competitive-guide updates; include LLM check + 'checked' flag
- Post Slack summary to Cresta team: Check AI visibility updates + new content drafts

**Annie Andrews (Cresta)**
- Build GA4 report showing leads by page/content type

**Russell Banzon (Cresta)**
- Review Phase 2 summary internally; provide feedback to GrowthX

---

## Transcript

**Aida Knezevic (GrowthX):** This meeting is being recorded.

**Aida Knezevic (GrowthX):** Really happy the web agency was able to resolve the canonicalization issue. I hope it wasn't too big of a lift.

**Annie Andrews (Cresta):** No, they turned it around in less than 24 hours. They're working on all the other issues from broken redirects to 404s. They said it shouldn't be a problem finishing that by end of next week. I'll keep you updated as they make progress.

**Aida Knezevic:** Happy that the first issue is resolved and things are moving in the right direction. That's perfect.

I knew something was wrong when I noticed some content we published was indexed while other content was discovered but not indexed. That only happens on brand new websites, not on established sites like Cresta with domain authority. I looped in Kyle and the technical SEO team and they discovered the canonicalization issues. I'll be monitoring Google Search Console to see if anything else shows up.

**Annie Andrews:** Cool. Thanks for flagging that.

**Aida Knezevic:** Russell, Devon, welcome. I know Nicky might be joining from her car, but let's get started. I have a couple updates on the technical SEO front. As part of Phase 1 deliverables, we conducted a technical SEO audit because we noticed indexing issues on the guide section. We identified the issue and your web agency implemented the fix. I'll be looking at Google Search Console to confirm the indexing recovery.

**Russell Banzon:** What's the core nature of the issue?

**Aida Knezevic:** The issue was canonicalization. Some canonical URLs were pointing to a www version while the actual site doesn't use www. That was causing the indexing delays. I'll look at Google Search Console to see the full scope across your entire site and confirm the fix resolves it.

**Russell Banzon:** That makes sense. How has this probably impacted us more generally outside of the guides?

**Aida Knezevic:** It delays how fast pages get indexed by Google. I can check all discovered-but-not-indexed pages on your site, not just the guides, to see how far the issue has spread. Hopefully once it's resolved, we can index all that content.

**Russell Banzon:** Got it. Quick scheduling note—I need to set up a 20-minute image feedback session with Steve and Katya. When works for you?

**Aida Knezevic:** Tuesday or Wednesday are best for me. Thursdays are already packed.

**Russell Banzon:** How about Tuesday at 10:30 AM PT?

**Aida Knezevic:** Perfect. I'll schedule that.

**Aida Knezevic:** We've also prepared the Phase 1 Summary so you understand the deliverables and the rough plan for Phase 2. I also wanted to discuss how Cresta monitors lead generation from your website so we can track content impact long-term.

**Russell Banzon:** I haven't reviewed the Phase 1 Summary yet, unfortunately.

**Aida Knezevic:** No worries.

**Devon Mychal:** I didn't have any questions on it, Aida.

**Aida Knezevic:** It made sense to me.

**Aida Knezevic:** My bigger question is around lead generation monitoring—specifically leads from organic search, and your attribution for tracking leads from blogs, webinars, and case studies.

**Russell Banzon:** That's definitely important for the long-term. Let me walk through our process.

All forms flow through HubSpot. Every lead gets a lead score based on behavior, which triggers MQL status. MQLs get routed to prospecting owners with SLAs. Demo requests get 1-hour SLAs, content leads get 8-hour SLAs. If an SLA is missed, managers get alerted and the lead is either followed up on or rerouted.

The main hand-raiser actions are demo requests and leads from our AI agent, Signal. Content leads are the other predominant type.

**Aida Knezevic:** Can you track what pages a lead visited before they signed up?

**Russell Banzon:** Yeah, we can.

**Aida Knezevic:** Do you have reports you could share? I'd like to understand how many leads different pages generate—resources, case studies, etc.

**Russell Banzon:** Annie, can we build something in GA4?

**Annie Andrews (Cresta):** Yeah, we can build something in GA4. We don't have heavy reporting built out yet, but I can put something together.

**Aida Knezevic:** That would be really helpful. We're creating a lot of bottom-of-funnel content like listicles and comparisons, so monitoring those is important. But top-of-funnel content matters too—even if someone doesn't book a demo, if they explore a product page, that's still a signal that they were intrigued by something they read.

**Russell Banzon:** That makes sense. Does Scrunch have a Looker integration?

**Aida Knezevic:** Actually, we're doing away with Scrunch. We're transitioning to our new AI visibility platform, "Check," which we're using internally. Pretty soon we'll open access to customers. The planned integrations are GA4, Search Console, Fathom, and PostHog. Russell, did you want a Looker integration as well?

**Russell Banzon:** That would be ideal if possible.

**Aida Knezevic:** I'll note that down and add it to the request. Let me show you your Check workspace real quick. We've been gathering data for a while.

Check is different from Scrunch because it's a shared index of AI visibility, not just a prompt-generation tool. We're already tracking competitors on the platform even if they're not paying customers—it helps create this visibility index so you can see how competitors are doing on evaluation-stage prompts. We have your products and features set up, along with 29 competitors you want to track.

We're tracking roughly 200 prompts using the "web search off" method like most users do, which gives more realistic visibility data. The interface shows your visibility and sentiment across prompts as well as competitor visibility for each one.

I flagged an important question with the Check team about ChatGPT data methods. There are two ways to pull data: "web search on" (Scrunch's method) which inflates visibility with constant citations, versus "web search off" which is more realistic. From my analysis, Check is using the latter. Perplexity has citations by default which balances things out. I'll confirm the approach.

The platform also shows top-cited URLs across all tracked prompts, including competitors and non-competitors. If we see articles ranking high for prompts you want to target, we can build content clusters around those topics immediately. NICE is one of the top domains for citations.

**Devon Mychal (Cresta):** Is there value in looking at both "web search on" and "web search off" approaches?

**Aida Knezevic:** Good question. I'll confirm the team's thinking and get back to you. The platform is still being actively built and improving daily—things will get better as we go.

One more thing I need to do: tag all your prompts by persona and funnel stage—awareness, evaluation, comparison, decision, and post-purchase. That'll give us better funnel visibility.

**Russell Banzon:** When will Cresta have access to Check?

**Aida Knezevic:** I need to check with Jason and the team. I can't give a firm date, but it's a super high priority—you're not the only ones asking. I know it's top of mind for the team.

**Aida Knezevic:** Quick content update for Nicky: we've shared five new articles for review in Airtable, and three more are in product team review. I'll check on Monday for feedback.

**Russell Banzon:** We published three blogs yesterday, so we're making progress on the publishing front.

**Aida Knezevic:** Great! Let me also summarize today's action items. One last thing—can we reschedule this weekly sync for an hour later? Devon and Nicky have scheduling conflicts.

**Russell Banzon:** Good idea. I'll have Netta coordinate with you on the new time. Did we come to a decision on Phase 2, or should we wait?

**Aida Knezevic:** Let me know what you decide after talking internally.

**Devon Mychal (Cresta):** One other tactical question—as we build more competitive guides, how do we keep them up to date? The space moves fast. For example, Sierra just announced their new AI assist feature, but one of our guides still says they don't have it. What's the update cycle on those guides as we get to 80 or more?

**Aida Knezevic:** For competitive guides, we always note the last update date. We can set up an Airtable automation that reminds our editing team every three months to audit for accuracy. We can use Perplexity or our Check platform internally to see what's changed. Then flag inconsistencies for manual review.

**Devon Mychal:** That would be great. And yeah, it seems pretty easy to do it with an LLM—just ask it to look at their latest announcements versus the update date and flag any inconsistencies.

**Aida Knezevic:** Absolutely.

**Russell Banzon:** In Airtable, we need a specific "checked" flag where someone physically confirms the review happened, even if using LLM notes for comparison.

**Aida Knezevic:** Perfect. I'll set that up.

That covers all the updates. I'll follow up in Slack with the action items and links to the new drafts. Have a great weekend, and I'll see you next week.

**Russell Banzon:** Thanks, Aida.

**Annie Andrews (Cresta):** Thank you. Bye!
