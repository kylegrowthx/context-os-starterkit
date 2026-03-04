# Panther <> GrowthX Marketing Ops

<metadata>
date: 2026-01-30
time: 16:01 UTC
duration: 16 minutes
organizer: kathy@growthx.ai
enriched_on: 2026-02-28 00:15 UTC
fathom_recording_id: 118547267
fathom_url: https://fathom.video/calls/549544476
share_url: https://fathom.video/share/DrsfwWeMynZyo13uN-r1vSesjzUKPqLQ
source: fathom

participants:
  - name: Aida Knezevic
    email: aida@growthxlabs.com
    company: GrowthX
    role: Content Marketing Lead
  - name: Allie Kalas
    email: allie.kalas@ext.runpanther.io
    company: Panther
    role: Marketing Operations
  - name: Ana Milosavic
    email: ana.milosavic@panther.com
    company: Panther
    role: Marketing & Partnerships
  - name: Kathy Lam
    email: kathy@growthx.ai
    company: GrowthX
    role: Director, Client Success
  - name: Katie Campisi
    email: katie.campisi@panther.com
    company: Panther
    role: Product/Leadership (mentioned, not present)
</metadata>

---

## Summary

GrowthX and Panther aligned on a tracking strategy to measure content marketing ROI through direct lead attribution (UTMs in HubSpot) and influenced lead tracking (GA4 exploration reports). The team also discussed CTA strategy, LLM referral tracking, and resolved blockers around production freeze timelines.

---

## Context

Panther is using GrowthX's Atlas platform to publish topical authority content on its blog. The challenge is visibility: GrowthX can see traffic metrics (GA4, GSC, SEMrush), but Panther lacks lead generation and pipeline progression data. This meeting established the mechanics for linking content to lead value. Allie (Panther Ops) will implement UTM tracking in HubSpot workflows. Aida (GrowthX) will build GA4 exploration reports to show indirect influence (users who visit blog posts and then convert on key pages like Solutions or Case Studies). The team also identified interest in tracking referrals from ChatGPT and Perplexity, and creating blog CTAs with granular tracking.

---

## Relevance

**Content Marketing & Analytics**
- Direct KPI tracking: attributing leads and pipeline value to specific blog URLs
- Influenced tracking: showing content's halo effect on key conversion pages
- GA4 constraints: 90-day retention window requires periodic data exports for long-term history

**Technical Integration**
- UTM implementation across Airtable content calendar → HubSpot workflows
- LLM referral stamping in HubSpot (ChatGPT, Perplexity capture)
- GA4 exploration reports with user pathing and referral domain filtering

**Operational Blockers**
- Production freeze at Pixel 1 blocking content publication
- Need for coordination across Panther teams (Pixel 1 admin, blog ops)

---

## Overview

- **Tracking Plan:** Panther will use UTMs on all GrowthX-published blog URLs to track direct leads in HubSpot.
- **Influence Reporting:** GrowthX will build a GA4 Exploration Report to show how blog traffic influences visits to key pages (e.g., Solutions, Case Studies), demonstrating content's indirect value.
- **CTA Strategy:** Panther will build blog CTAs with UTMs for granular conversion tracking. GrowthX will provide copy for these CTAs.
- **Production Freeze:** A production freeze is currently blocking content publication. Ana will investigate the timeline for its removal.

---

## Key Topics

### Goal: Track Content's Impact on Leads

  - GrowthX's Atlas platform will publish content to Panther's blog to build authority, drive traffic, and improve keyword rankings.
  - **Challenge:** GrowthX lacks visibility into lead generation and pipeline progression from this content.
  - **Objective:** Enable Panther to attribute leads and pipeline value directly to specific blog URLs.

### Solution: Direct & Influenced Tracking

  - **Direct Lead Tracking (HubSpot):**
      - Panther's HubSpot workflows already track leads by source via UTMs.
      - **Plan:** Add UTMs to all blog URLs from the Airtable content calendar to attribute direct leads.
  - **Influenced Lead Tracking (GA4):**
      - **Goal:** Measure content's indirect value by showing how blog visitors engage with other key site pages.
      - **Method:** GrowthX will build a GA4 Exploration Report to track user paths from blog posts to pages like Solutions or Case Studies.
      - **Constraint:** GA4 Exploration Reports have a 90-day data retention limit. GrowthX may need to export data periodically for long-term historical analysis.

### Solution: CTA & LLM Tracking

  - **Call-to-Action (CTA) Tracking:**
      - **Plan:** Panther will build CTA sections for the blog. GrowthX will provide copy for these CTAs.
      - **Execution:** All CTA links will include UTMs for granular conversion tracking.
  - **LLM Referral Tracking (ChatGPT, Perplexity):**
      - Panther has seen leads from ChatGPT and wants to track this source for new content.
      - **Plan:**
          - **GA4:** GrowthX will filter Exploration Reports by referral domain (e.g., `chat.openai.com`).
          - **HubSpot:** Allie will review the existing workflow that stamps LLM referrals to ensure it's functioning correctly for new content.

### Blocker: Production Freeze

  - A production freeze is currently blocking the publication of new content.
  - Ana will follow up with the Pixel 1 admin to get an estimated timeline for its removal.

---

## Action Items

**Allie Kalas (Panther)**
- Review GrowthX Airtable content calendar; define UTMs and tracking structure for GrowthX blog URLs
- Audit HubSpot LLM referral workflow; confirm ChatGPT and Perplexity capture is functional for new content

**Aida Knezevic (GrowthX)**
- Draft blog CTA copy for GrowthX content; share with Allie for UTM implementation
- Build GA4 exploration report to measure influenced lead tracking (LLM referrals + key-page user pathing)

**Ana Milosavic (Panther)**
- Build blog CTA sections per design specifications
- Follow up with Pixel 1 admin on production freeze timeline; update GrowthX with status

**Kathy Lam (GrowthX)**
- Email Airtable content calendar link to Allie (completed during call)

---

## Transcript

**Aida Knezevic:** This meeting is being recorded.

**Kathy Lam:** Hi everyone. My apologies for the late start. I'm out of the country in Hong Kong visiting family and I've been having network issues with VPN.

**Allie Kalas:** No worries. So we have everyone except Katie?

**Ana Milosavic:** Right, Katie's not joining. I'll be here if you need anything, but this is mainly Allie's meeting.

**Kathy Lam:** Perfect. The goal is to make sure we tie into the success KPIs and analytics for Panther. What do we need to send you, or what do you need to send us, so we can integrate everything into our Looker dashboard?

**Allie Kalas:** Maybe we could backtrack a bit. You guys tell me the goal and I'll figure out how to report on it.

**Aida Knezevic:** Sure. So basically, GrowthX provides a content marketing engine. We have our own in-house content generation platform called Atlas. We develop a content strategy for each client that focuses on specific topic clusters where we want you to build authority. The goal is to grow brand visibility, get more traffic to your site, and rank for high-value keywords. Traffic is one part of success—we can report on that easily. We have access to your GA4, GSC, and our Looker dashboard, where we can see how much traffic you're getting every week from the content we're publishing, as well as your overall website. We use SEMrush to track keyword rankings.

Where we don't have visibility is lead generation and pipeline. Specifically, how are you monitoring user progression once they land on your site? What pages do they explore? Do you track which pages they visited before converting to a lead? That's what we need to understand so your marketing team can see: how many leads were influenced by this content? Did we get any leads directly from specific URLs?

**Allie Kalas:** That's really helpful. So we track everything by source using UTMs in HubSpot. I have workflows set up by UTM or channel. We're stamping that data. We don't currently have lead scoring or triggers based on page views, but we could build that out. I was thinking: should we add UTMs to your published pages so I can track them? Or should we set up specific page triggers?

**Aida Knezevic:** Yeah, so we have a content calendar in Airtable that we can give you access to. There's a "Published" view with URLs for all the content we publish. Will that work?

**Allie Kalas:** Yeah, 100%. Once I get access, I can figure out how we'd track those. Where are these being used? On your site or other channels?

**Aida Knezevic:** They're living on the Panther blog. We're set to publish the first blog this week.

**Allie Kalas:** Okay, let me think through how we can track that once I have access.

**Aida Knezevic:** Let me share my screen and pull up the content calendar.

**Kathy Lam:** And I'm adding you to Airtable right now, Allie.

**Allie Kalas:** Thank you.

**Aida Knezevic:** So this is the content calendar with different views. If you go to "Published Blogs," you'll see all the links with published URLs and dates. We also categorize them by topic cluster—that's not applied yet since we haven't published anything. But here are the topic clusters we've identified for Panther. This is another data point you could use in HubSpot to organize content.

**Allie Kalas:** That's helpful. Can you show me that one more time?

**Allie Kalas:** Okay, I see it.

**Allie Kalas:** And do we have any CTAs on the blog?

**Aida Knezevic:** That's a great question. Right now we don't have any CTAs. We're just incorporating product mentions throughout the content. But if you have existing CTAs on your website, we could add them in the content depending on the topic.

**Allie Kalas:** I was assuming no for now, but yeah, we could build that out if it makes sense.

**Aida Knezevic:** If we help write copy for a couple of CTAs, we could rotate them depending on the topic. Would you use UTM codes in the CTA to track visitors?

**Allie Kalas:** Yeah, probably depends on the CTA, but we could track that.

**Aida Knezevic:** Sounds good. Do you have any data on your organic leads? What pages do they land on? Which pages are they interacting with? It would be helpful to know your most important pages for lead generation.

**Ana Milosavic:** We have information in GA4. We don't have a huge amount of website traffic, but it's not bad. Our goal is to elevate our brand this year and increase traffic through all our activations with you and others. Our website isn't currently a huge driver for lead generation. Our existing blogs don't get much traffic, and even our AI pages don't generate leads directly.

But I do have a question about CTAs. If we add a CTA with a UTM and they convert, that's trackable. But do we also want to see traffic if they don't convert? Can we track where they go in GA4?

**Aida Knezevic:** Yeah, I actually did this for another client. I created a simple GA4 exploration report that tracked all our published URLs and checked whether users visited key pages—case studies, solutions, product page—even if they didn't book a demo. The idea is to show the influence of content. Even if someone doesn't convert right away, we can show they're moving through your website.

**Ana Milosavic:** That would be really insightful. I think if we could build that out with the UTM tracking Allie puts together, that would work great.

**Aida Knezevic:** Definitely. Once we start publishing, we have access to your GA4, so it's just about setting up the exploration report. One limitation: GA4 exploration reports only go back 90 days. For historical data over six or twelve months, we might need to export periodically to create a historical database. GA4 isn't very user-friendly unfortunately.

**Ana Milosavic:** No problem, thank you.

**Aida Knezevic:** I think those were all my main questions.

**Kathy Lam:** Any other questions? I know Katie was excited about traffic from ChatGPT. We want to track that for new blogs too and see if we can tie those views to influencing. Is that feasible, Allie?

**Aida Knezevic:** We have an LLM referral view in Looker, so we can track traffic from LLMs to blogs. We could do the same with GA4 exploration reports—filter for referral traffic by domain name to flag ChatGPT, Perplexity, and others.

**Ana Milosavic:** I'm not sure how that works in HubSpot though. Allie, the ChatGPT lead that came through specified ChatGPT. Did you set that up, or is that how it comes through from the source?

**Allie Kalas:** I have to check that specific one. I remember stamping that in a workflow I built, but let me dig in and see if anything needs updating. We should be able to see the pages they viewed as well.

**Ana Milosavic:** Okay, that's helpful. Thank you. I think that's it for me. We sent over what we want the CTA sections to look like on the blog, so I'm going to work with the team to build that out. Hopefully we can move forward on the CTA sections soon.

**Aida Knezevic:** Perfect.

**Kathy Lam:** I think that covers all the topics. Allie, I sent you the Airtable link in chat, but I can also send it via email after the call.

**Allie Kalas:** I see it. Perfect, I have access.

**Aida Knezevic:** I have access too.

**Kathy Lam:** Great. One more thing—are we still in a production freeze?

**Ana Milosavic:** Let me check with the Pixel 1 admin. I see you tried to get added to a channel and need approval. It should be automatic on our end, so it's probably waiting on Pixel 1.

**Kathy Lam:** Yeah, that makes sense.

**Ana Milosavic:** I'll follow up with them. There's still a production freeze in place, but let me find out when they expect to lift it and get back to you.

**Kathy Lam:** Great, thanks for looking into that. Thanks everyone for jumping on this quickly. I really appreciate everyone's time.

**Ana Milosavic:** Of course. And I'm sure it's a weird time for you in Hong Kong!

**Kathy Lam:** Ha, yeah it is. Thanks, everyone. Have a good one.

**Ana Milosavic:** You too.

**Allie Kalas:** Thanks, bye.

**Aida Knezevic:** Bye everyone.
