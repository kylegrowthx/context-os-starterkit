# Webstacks <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-05
time: 17:30 UTC
duration: 39 minutes
organizer: Kyle Gaudreau (kyle@growthxlabs.com)
participants:
  - Kyle Gaudreau (kyle@growthxlabs.com, GrowthX) — Organizer, Head of Operations
  - Katya Luscomb (katya@growthx.ai, GrowthX) — Account Lead
  - Nikan Shahidi (nshahidi@webstacks.com, Webstacks) — External participant
  - Jesse Schor (jschor@webstacks.com, Webstacks) — Lead technical contact
  - Andi Bailey (andi@growthx.ai, GrowthX) — Team member
fathom_recording_id: 120117568
fathom_url: https://fathom.video/calls/557236388
share_url: https://fathom.video/share/Vs2uzs9Kz8cfy1X-KoDZ4-NGaR8wENFr
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

GrowthX and Webstacks diagnosed a post-refresh traffic drop driven by Googlebot crawl degradation (reduced requests, slower response times) and 600+ article sitemap changes, with root cause potentially stemming from Vercel's full-rebuild sitemap logic. Both teams discussed shifting strategy from broad organic traffic to high-quality LLM-referred leads using Check That, and explored contracting terms to justify Webstacks' annual engagement.

---

## Context

Webstacks recently completed a website refresh that inadvertently triggered a significant drop in organic search traffic. Kyle Gaudreau (GrowthX) analyzed Google Search Console crawl data and discovered reduced crawler requests and elevated response times correlating with the refresh and a subsequent sitemap update affecting 600+ articles. Jesse Schor (Webstacks) has already removed non-Webstacks scripts and investigated bot traffic anomalies, but the core crawl performance issue persists. The conversation explores whether Vercel's build automation triggers unnecessary full-site sitemap updates on every change, creating a recrawl cycle that overwhelms the server.

Beyond SEO diagnostics, both teams are using this engagement to pivot strategy. GrowthX recently launched Check That, an AI visibility tool for tracking answer engine optimization (AEO) signals. The teams discussed shifting Webstacks' content focus from top-of-funnel broad reach to high-quality leads attracted by LLM-referred traffic, using Check That and social listening research to identify high-intent topics. This requires closer alignment on business context and content themes, which the teams plan to formalize through recurring business calls and Gong recording shares.

---

## Relevance

**For Webstacks:**
- Technical diagnosis points to Vercel build configuration as root cause of crawl performance degradation; actionable fix required before organic recovery is possible.
- Shift to AEO/LLM-driven strategy opens new value proposition for GrowthX engagement and differentiates from traditional SEO-only focus.
- Contract renewal contingent on proving incremental value beyond current 3-month flexibility; annual term requires CFO-level justification.

**For GrowthX:**
- Check That (AI visibility index) has immediate application in diagnosing and monitoring AEO opportunity for client content strategy.
- Webstacks' traffic recovery and LLM-led content shift create concrete proof point for GrowthX's methodology and product-market fit.
- Establishing recurring business context calls (Gong recordings, customer insights) strengthens strategic positioning and deepens account engagement.

**Cross-cutting:**
- Crawl issue is solvable but requires technical depth from Webstacks (Vercel logs, sitemap audit) and judgment from GrowthX (engineering partnership, GSC consultation).
- YouTube and Reddit identified as underexplored channels for Webstacks; content strategy should prioritize AEO signals in these platforms as social listening foundation.

---

## Overview

- **Traffic Drop Diagnosis:** A post-refresh traffic drop is linked to a Googlebot crawl issue (fewer requests, slower response times) and compounded by a sitemap update for 600+ articles.
- **Root Cause Hypothesis:** The issue may stem from Vercel build processes that trigger full sitemap updates on every change, causing excessive recrawl requests.
- **Strategic Shift:** The focus will shift from top-of-funnel organic traffic to high-quality, LLM-referred leads, using Check That and social listening to inform strategy.
- **Contract Discussion:** An annual contract requires a clear value-add (e.g., discount, new services) to secure CFO approval over the current flexible 3-month term.

---

## Key Topics

### Traffic Drop Diagnosis

  - A significant traffic drop followed the recent website refresh, accelerating in the last 1.5 weeks.
  - **Diagnosis:** Googlebot crawl data shows a sharp decline in crawl requests and a significant increase in response times.
      - This pattern is unusual and suggests a technical issue, not a content or 404 problem.
  - **Compounding Factor:** A sitemap update for 600+ articles occurred around the same time, likely sending a large, confusing signal to Google.
  - **Webstacks' Initial Fixes:**
      - Removed non-Webstacks scripts from the Sanity template \~1.5 weeks ago.
      - Noted a drop in bot traffic (via PostHog) that may be affecting impression data.
      - **Significance:** These fixes haven't resolved the core crawl issue, as response times continue to worsen.

### Root Cause Hypothesis

  - **Hypothesis:** The issue is a Vercel build process that triggers a full sitemap update on every page change.
      - **Impact:** This would force Google to recrawl the entire site repeatedly, overwhelming the server and causing the observed crawl performance degradation.
  - **Additional Finding:** An AI tool (Claude) was blocked by Cloudflare with a 403 error.
      - **Significance:** This suggests a potential issue with bot access that may also be affecting Googlebot.

### Content & Sanity Updates

  - **FAQ/TLDR Modules:**
      - **Request:** Add dedicated Sanity modules for FAQs and TLDRs to blog posts.
      - **Status:** The FAQ module exists for site pages but not blog posts. The TLDR can use the existing `excerpt` field.
      - **Action:** Jesse will investigate adding the FAQ module to the blog schema.

### Strategic Roadmap & AEO

  - **Goal:** Shift strategy from top-of-funnel organic traffic to high-quality, LLM-referred leads.
  - **Methodology:** Use Check That (GrowthX's new AI visibility tool) and social listening to inform a data-driven content strategy.
  - **Key Insight:** YouTube is currently the strongest signal for driving AEO (Answer Engine Optimization) visibility.
      - **Action:** Explore a strategy for YouTube and Reddit, where Webstacks has a limited presence.
  - **Process:** Establish a recurring cadence for sharing business context (e.g., Gong calls, customer patterns) to inform content themes.

### Contract Discussion

  - **GrowthX's Goal:** Transition to an annual contract.
  - **Webstacks' Requirement:** CFO approval requires a clear value-add to justify moving from the current flexible 3-month term.
      - **Examples:** A discount or new services.

---

## Action Items

**Katya Luscomb** (GrowthX)
- Email Jesse Check That demo + custom setup by Feb 7
- Schedule recurring discovery call with Jesse (Webstacks) and Kyle for weekly business context + content strategy alignment

**Jesse Schor** (Webstacks)
- Email Kyle PostHog bot traffic trends analysis (clarify non-Googlebot impact)
- Investigate crawl response time issue with Nikan (Webstacks); review Vercel build/deployment logs
- Audit Vercel build/sitemap logic; fix noindex directives; stop daily full-site rebuilds if present
- Confirm blog FAQ module exists in Sanity schema; implement if missing
- Email Katya + Kyle batch of recent Gong call recordings for content insights

**Kyle Gaudreau** (GrowthX)
- Email Jesse re: Cloudflare 403 error blocking AI tool access; propose GrowthX engineering support to diagnose impact on Googlebot
- Email Jesse AEO/social listening tool recommendations (YouTube, Reddit focus)

---

## Transcript

### Opening & Check That Launch (00:00–02:30)

**Kyle Gaudreau:** We just officially launched Check That—it's our AI visibility tool. We're super excited.

**Katya Luscomb:** I'm going to send you a demo of your setup by the end of the week. I wanted to dive into that traffic drop article you sent over. Kyle helped look into the performance issues and compiled recommended actions around the crawling problem we noticed.

**Kyle Gaudreau:** Yeah, let's run through it real quick, then we can go into questions.

---

### Traffic Drop Diagnosis (02:30–14:00)

**Kyle Gaudreau:** There's a pretty notable traffic drop. It was hard to spot initially because it was a slow burn, but it's been precipitous in the past week and a half. I investigated 404s, internal linking changes, and articles themselves—none of that explains it. But once we dove into the crawl data, it really stood out.

Crawl requests have plummeted and response speeds have gone up significantly. There are also headwinds with Googlebot mobile rendering. This happened around the time of the website refresh, but took a bit longer to show up. Additionally, your sitemap had a wide-scale change—600+ articles with a last-modified date around when traffic started dropping more. I think it's compounding negative signals post-refresh.

**Jesse Schor:** Yeah, a couple of things. I noticed this as well last week. One was non-Webstacks scripts on pages we copied over. We have a Sanity template with backend components, and I found tags that weren't ours. We removed those about a week and a half ago.

The other thing was bot traffic. We use PostHog and over the last six months we've been getting more international traffic. I didn't put much weight into it initially, but digging deeper, a lot of that bot traffic has fallen off, and that seems to be impacting impressions and traffic sources.

**Kyle Gaudreau:** To clarify, bot traffic wouldn't necessarily apply to Googlebot crawl requests. But there's a clear correlation with when you did the refresh. I'm not saying what you shared wouldn't have influence, but if I had to pin the number-one cause, I'd be surprised if it wasn't related to the crawl issue.

**Jesse Schor:** Regarding response times—that's something I definitely want to dig into more because that seems odd and new.

---

### Root Cause & Vercel Investigation (14:00–20:00)

**Kyle Gaudreau:** When I dig into GSC, I can see different reports. The crawl inefficiency suggests something technical on your end—probably Vercel. My hypothesis is that every time you deploy, Vercel triggers a full sitemap update, which forces Google to recrawl everything repeatedly. This overwhelms the server and creates the degradation we're seeing.

**Jesse Schor:** That's a good hypothesis. I'll investigate the Vercel build logs and audit the sitemap logic. If daily full rebuilds are happening, we need to stop that. I'll also check if there are noindex directives we're missing.

**Kyle Gaudreau:** Nikan, can you look at this with Jesse? Understand the why behind the crawl request drop.

---

### Content & Sanity (20:30–25:00)

**Katya Luscomb:** One thing—do you have FAQ modules for blog posts?

**Jesse Schor:** The FAQ module exists for site pages but not blog posts. We can use the existing excerpt field for TLDRs.

**Katya Luscomb:** Can you confirm that's in the Sanity schema and implement if missing?

**Jesse Schor:** Yeah, I'll do that.

---

### Cloudflare & Bot Access (25:00–28:00)

**Kyle Gaudreau:** One more thing—we ran an AI crawler on your site and got a 403 error from Cloudflare. That's blocking access. Can we explore what's happening there? If bots are being blocked, Googlebot might be affected too.

**Jesse Schor:** I'll look into that. We might need to adjust Cloudflare rules or get engineering support to understand the impact.

---

### Strategic Shift: AEO & Content Strategy (28:00–37:00)

**Kyle Gaudreau:** Here's where Check That comes in. We're shifting strategy from broad organic traffic to high-quality, LLM-referred leads. YouTube is the strongest AEO signal right now, and Reddit is also underexplored for Webstacks.

**Katya Luscomb:** To make this work, we need to understand your business context better. Can we establish a recurring cadence—maybe monthly—to share customer themes, Gong calls, and sales patterns? That informs what content we create.

**Jesse Schor:** That makes sense. We're already trending toward Sanity partnerships because that's where customer conversations are happening. If we create a two-way street where you share what you're seeing and we implement it, that's more efficient. We generate a ton of content and insights—hard to know what's valuable for you.

**Kyle Gaudreau:** Yeah, and layering in lead data insights helps us evolve. Having some frequency to these conversations is key because things shift over time. It's not guessing; it's based on signals from Reddit, Gong Calls, and other sources.

**Jesse Schor:** We can send over a batch of recent Gong recordings and we can organize them however is most helpful—top hits or a mix of consistent themes.

**Kyle Gaudreau:** That would be amazing. If you can organize by theme and export them, we'll run through them. Between Reddit, Gong Calls, and your context, we can validate themes.

**Katya Luscomb:** Perfect. That'd be great. Thank you, Jesse.

---

### Contract Discussion (Not heavily detailed in transcript)

The teams discussed transitioning to an annual contract. Webstacks' CFO requires clear value-add (e.g., discount, new services) to justify moving from the current flexible 3-month term.

---

### Closing

**Katya Luscomb:** Was there anything else top of mind before we wrap?

**Jesse Schor:** No, good here.

**Katya Luscomb:** Great. Thank you for the time and all the digging in. Appreciate it.

**Jesse Schor:** See you, bye-bye.
