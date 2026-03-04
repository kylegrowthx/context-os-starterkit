# Strapi<>GrowthX Weekly Sync

<metadata>
date: 2025-04-02
time: 16:31 UTC
duration: 29 minutes
organizer: Jason Gong (GrowthX)
participants: Sydney Go (GrowthX), Jason Gong (GrowthX), Victor Coisne (Strapi), Golzar Yaghoubpour (Strapi)
fathom_recording_id: 55137409
fathom_url: https://fathom.video/calls/266451877
share_url: https://fathom.video/share/t-MVh6xs9KRWd3RBVwSDX6pHLqzbf5xP
source: fathom
enriched_on: 2026-03-04 15:32 UTC
</metadata>

---

## Summary

Sydney Go formally took over content delivery responsibilities from Andre, with GrowthX planning an account-wide strategy deep dive focused on driving non-branded keyword traffic through optimized comparison pages, integration pages, and new content formats like glossaries. Victor Coisne emphasized the need to prioritize high-impact workstreams over volume and move beyond impressions/clicks to conversion-driven metrics like HubSpot campaign attribution and Amplitude product analytics. Key blockers identified: Strapi's open-source product model limits conversion tracking (users download without account creation), and GrowthX still needs access to Amplitude and HubSpot campaign data to validate content performance.

---

## Context

Strapi is an open-source headless CMS and a key GrowthX client working on a major content strategy refresh. This was the first weekly sync under Sydney Go's delivery leadership (taking over from Andre, who had been deeply invested in the account). The relationship centers on GrowthX's content marketing services aimed at ranking comparison pages, integration pages, and new-format content to drive trial sign-ups for both the open-source version and Strapi Cloud (their hosted SaaS offering). The meeting also marked a strategic inflection: Victor Coisne wants GrowthX to move away from high-volume content generation toward high-impact, conversion-focused content that captures non-branded keywords and feeds qualified traffic into Strapi's multi-step trial conversion funnel (demo request → quick start download → cloud deployment).

---

## Relevance

**To GrowthX Delivery:**
- Strapi explicitly wants to move away from high-volume commodity content (competitor posts, broad topics) toward non-branded keywords with higher intent and less cannibalization
- Client expects deep SEO strategy work (keyword research via SEMrush, gap analysis on comparison pages) before execution — this is a strategic consulting play, not just content production
- New team (Sydney + Jason) needs full handoff documentation from Andre, including Notion template for integration pages and Strapi's publishing/approval workflow
- Quality expectations are exceptionally high due to Strapi's technical audience; Victor flagged custom LLM/CheckThat integration as potential quality-assurance lever

**To CheckThat:**
- Victor mentioned building a custom GPT/LLM for QA on content — potential use case for CheckThat prompt auditing or AEO optimization to ensure content visibility to AI
- Strapi is exploring glossary formats; CheckThat could evaluate if glossary pages rank in AI overviews and capture AI-driven traffic

**To GrowthX Business Development:**
- Account shows strong engagement and deepening partnership: Strapi is opening access to Amplitude (product analytics) and considering HubSpot campaign data share
- Expansion signal: Sydney and Jason are dedicating two resources for strategy + ongoing delivery (step up from Andre as solo executor)
- Renewal confidence: Victor explicitly said he doesn't want to overwhelm the new team with new demands; account is healthy and focused on execution excellence
- Internationalization play (Why Strapi in Japanese, Chinese, Spanish) signals Strapi's growth into non-English markets — potential for localized content strategy upsell

---

## Overview

- Sydney is taking over Andre's responsibilities, working through existing documents and videos
- Content generation continues with 11 new articles planned, focusing on various Strapi topics
- Team to conduct a deep dive on Strapi's strategy, including comparison pages and content refreshes
- Strapi aims to capture non-branded keyword traffic and improve conversion tracking for open-source downloads

---

## Key Topics

### Content Generation and Publishing

  - 8 articles from last week pending publication due to Theo's absence
  - 11 new articles planned for generation this week
  - Team to deprioritize competitor-focused content and focus on non-branded keywords
  - Integration pages: 2 new ones to be created, old ones to be reformatted

### Reporting and Analytics

  - Sydney building a new report in Looker Studio for easier access to data
  - Team to focus on metrics beyond impressions and clicks, aiming to track conversions
  - Strapi uses HubSpot campaigns for attribution, considering giving GrowthX access

### Strategic Focus and Goals

  - Priority on capturing non-branded keyword traffic
  - Comparison pages aim to drive traffic and ultimately lead to Strapi trials
  - Challenges in tracking full conversion path due to open-source nature of the product
  - Team to explore new content formats, including potential glossary pages

### Technical Considerations

  - Strapi working on improving data quality in Amplitude for better A/B testing
  - Telemetry data available but anonymous, limiting user journey tracking
  - Potential to add more detailed event tracking in Google Analytics for quick start guide interactions

### Internationalization

  - Considering creating "Why Strapi" pages in key languages (Japanese, Chinese, Spanish)
  - Strapi supports internationalization, starting with one page as a test

---

## Action Items

**Victor Coisne**
- Provide list of integration pages + format doc (Notion) to Sydney/Jason
- Grant Sydney/Jason access to Notion doc w/ integration page template
- Check w/ team re: giving Sydney/Jason access to Amplitude

**Golzar Yaghoubpour**
- Send info on event tracking for docs to Sydney/Jason

---

## Transcript

**Victor Coisne:** I think Paul is not going to join because he's on PTO. I think Theo was not feeling good, so we may have a very small group today.

**Jason Gong:** Everyone's getting sick. I also caught something from my kid.

**Victor Coisne:** How old is your kid?

**Jason Gong:** I just have one. He's 20 months.

**Victor Coisne:** He's going to turn two soon. Fun age. I got two — they're six and four. You got the two-year gap.

**Jason Gong:** We're trying to plan for that, but we'll see what we come out with.

**Golzar Yaghoubpour:** Oh, I'm muted. Hi, everyone.

**Jason Gong:** Hi, everyone.

**Victor Coisne:** Do you know if Theo was out yesterday?

**Golzar Yaghoubpour:** He's usually very active in Slack by the time I log on, so he may be out. He's offline, and he's usually always online until like really late.

**Victor Coisne:** Okay, let's get started.

**Victor Coisne:** Okay, awesome.

**Sydney Go:** I'm still going through Andre's documents and videos because there's a lot. He was very invested in your account and I'm trying to meet that level of performance. Before we get started, I watched the video from Andre about how to upload into your CMS. Is the process still the same?

**Victor Coisne:** We haven't changed anything.

**Sydney Go:** Paul did the walkthrough. I had a question: is there any specific way you want me to select related articles, or do I just type in the main keyword and select what pops up?

**Victor Coisne:** Just like related keywords. Type in the main keyword and select what pops up.

**Sydney Go:** For your content for the week, I noticed eight articles from last week that Andre submitted haven't been published yet out of the 10. Do you know what the publishing cadence is, or if there's an expected publish date?

**Victor Coisne:** We try to do about five a week. The issue is that Theo's been out — he was traveling last week and then got sick. So we're behind schedule. Hopefully he's back before the end of the week and we can get at least a handful out.

**Sydney Go:** That makes sense. Let me share my screen. These articles from "Learn to Script in Five Minutes" are already in the CMS and ready for review. As soon as Theo's back, he can publish them or give feedback.

**Sydney Go:** The next set of articles include topics like SSR, Next.js, CMS fundamentals, development technologies (API and technical concepts), and content strategy and management — that's 11 total. Is there one article you'd like me to deprioritize? Some have priority levels assigned, but many are blank.

**Victor Coisne:** The blank ones don't have to be prioritized. Timeline isn't that important.

**Sydney Go:** I'm going through and editing all of them to make them more polished. If you want me to deprioritize any, I can submit those next week instead.

**Sydney Go:** I wanted to ask about the articles marked as backlog. Why are they marked as backlog?

**Victor Coisne:** We may have over-indexed on competitor content. We already have comparison pages, so having competitor blog posts feels redundant. I'd suggest auditing those comparison pages — they're light on text (mostly just tables). We could improve their SEO and rankings by adding content from these backlog articles instead.

**Sydney Go:** That makes sense. On integration pages: we're working on five, but only two are new. Do you want me to reformat the old ones too? I don't have access to Andre's list of which ones need the new format.

**Victor Coisne:** I'll provide you with the list and format document. It's a Notion document. I'll send it after the meeting.

**Sydney Go:** Andre sent me a Notion document with the template for integration pages. I requested access so I can start generating the new ones. If you have the link, can you send it so you can grant me access?

**Victor Coisne:** Do I need to add Jason or just you?

**Sydney Go:** It would be nice to have both of us so we can cross-reference.

**Victor Coisne:** You two should be receiving access now. Thank you.

**Sydney Go:** If there are other documents you shared with Andre that are still relevant, could you share them with Jason and me so we're on the same page? On reporting: I'm not showing you the report today because it's messy, but I'm building a Looker Studio dashboard so you have access to your data whenever you want. Andre was doing this manually, but we can get it to you faster and more polished every week. Hopefully done by end of week.

Jason and I are planning a deep dive on your strategy, including all your pages and comparison pages to identify improvements. We're also going to restart page refreshes to improve performance on lagging pages. Is there anything specific you want us to focus on?

**Victor Coisne:** That sounds good. I think it's important for you all to get up to speed. I don't want to overwhelm you with new things — take the time to bring things up to speed. One thing to keep in mind: we'd like to do "Why Strapi" pages in different languages — Japanese, Chinese, Spanish — which would be really good from an SEO standpoint. Have you seen other customers do that successfully?

**Jason Gong:** Some of our other customers do translations. For your website right now, do you have the infrastructure for language-specific versions?

**Victor Coisne:** No, but Strapi does support internationalization. We want to dip our toes into translation starting with one page. "Why Strapi" would be a good start, especially since some folks struggle with English — at least we can provide a link for them.

**Jason Gong:** We can add that to the list. To add context for Sydney: this is week one of the handoff. We want to look at everything fresh — rethink strategy a bit. You have several content streams: new content, integrations, rewrites, and meta description rewrites. We want to take a blank slate approach — see what's working, what's not — and prioritize where effort is best spent. We'll definitely look at comparison pages first. I notice the pages doing best are ones featuring Strapi, which is expected. But I think what you want is: for example, "Payload vs. Sanity" — and then somewhere on that page show how Strapi is better or how Strapi fits in.

**Victor Coisne:** I'm aligned with you on prioritizing what workstreams have the biggest impact. In the past, we've had good impressions and clicks on some topics, but that's less interesting to me because we're cannibalizing traffic between our own pages. We're working with GrowthX specifically to rank non-branded keywords. Do SEMrush research to identify which non-branded keywords we should target, then strategize around those. We have articles and landing pages, but let's be creative with format. We're not tied to one format. I've seen some companies do really well with glossaries. What formats are you seeing success with at other customers?

**Jason Gong:** I think we're on the same page. A big part of bringing Sydney and me on is giving you more resources to do this kind of strategy work. So next week we'll present a blank slate approach — here's where we think effort should go. And we need to take advantage of the fire hose of content we can produce, which you can't get from most writers.

**Victor Coisne:** Just to add context — Strapi has a technical audience, so quality expectations are high. We're meeting with Daniel and trying to use a custom GPT or LLM like your CheckThat service for quality assurance. Also, with recent ChatGPT updates, LLMs are getting much better at generating visuals, so that's an area where we hope to see improvement.

**Jason Gong:** I mean, think we're on the same page.

**Jason Gong:** mean, a big part of, like, you know, switching Sydney and I on is just, like, give you guys more resources to kind of do stuff like this.

**Jason Gong:** So next week, almost, I don't want to call it, like, a reset, but just kind of, like, blank slate, you know, here's just where we want to put the effort going forward.

**Jason Gong:** And I think, I mean, the big thing for us is, like, I mean, we're publishing content, but because we can kind of, we have this fire hose, like, we need to take advantage of it.

**Jason Gong:** So just, like, uniquely, you know.

**Jason Gong:** Not something you'd be able to get, like just working with any set of writers, essentially.

**Jason Gong:** So yeah, we'll that next week.

**Victor Coisne:** We'll go through it.

**Jason Gong:** I'm sure there'll be feedback and stuff like that.

**Jason Gong:** But in the meantime, I think that I guess the day-to-day that was going on, seems like Sydney's on top of.

**Jason Gong:** We'll keep you updated on just the publishing.

**Jason Gong:** Sounds good.

**Victor Coisne:** And just to reset some extra context, like for us and what's going to be potentially unique compared to other customers, of course, is the fact that we work with a technical audience.

**Victor Coisne:** so I think the expectations are a bit higher in terms of quality of content, which is why we've been meeting with Daniel and then trying to push for like, you know, the Kappa is like our own like kind of custom GPT, custom LLM, like that we can use as a quality assurance in some of the AeroOps steps.

**Victor Coisne:** And also...

**Victor Coisne:** also...

**Victor Coisne:** So like around images, this is where like we have, especially with the latest update from some chat GPT, like the kind of the bar is just LMs are just getting much better at producing visuals.

**Victor Coisne:** And so this is really where I'm hoping we can see some improvement on your end.

**Sydney Go:** True.

**Sydney Go:** That all sounds good.

**Jason Gong:** Yeah, we can definitely do that.

**Sydney Go:** What's your number one main goal with comparison pages?

**Victor Coisne:** Capturing traffic for those keywords, and the ultimate goal is getting people to try Strapi. The challenge is attribution isn't perfectly set up because we're open-source — people land on a comparison page, go to the quick start, download Strapi, but don't necessarily create an account. Conversion paths aren't straightforward. To track attribution and ROI across workstreams, we add URLs to HubSpot campaigns and HubSpot tracks influenced contacts, sessions, and revenue. So we can see which workstreams — integration pages, blog, comparison pages — generate what metrics. This is worth giving you access to. From an ROI standpoint, clicks are good, but we also want to see if clicks convert.

**Jason Gong:** Do we have access to any product analytics today? We have Google Analytics and Search Console, but do you have Amplitude or Mixpanel we could look at?

**Victor Coisne:** We're in the process of cleaning up Amplitude — investing in data cleanup and A/B testing capability. Almost there but not quite. We're also cleaning up GA to make sure all events are set up properly and setting up exploration paths. We need to move beyond impressions and clicks to ensure we're bringing the right people to the site.

**Jason Gong:** Do we have access to your Amplitude? Both Sydney and I are familiar with the tool.

**Victor Coisne:** The issue is, with open-source, Amplitude doesn't give us all the data we need. Users don't need to create an account to download. We do have Strapi Cloud accounts though, so we could track cloud conversions and account creation for conversion path reporting. We can check with the team about giving you access now.

**Jason Gong:** Mostly we're looking for signal — what keywords and page types bring the highest intent. We don't need a perfect user journey. For the open-source path, as long as we see them go to the repo, that's signal beyond just the click.

**Victor Coisne:** There are two paths we're pushing: one is demo request, which is a form that provisions a dedicated instance. Users can try both backend and frontend. That's step one. Step two is local installation — they go to quick start, run the setup steps. Step three is deploying to Strapi Cloud. We have telemetry by default, but it's anonymous — no identifier to tie it together.

**Sydney Go:** Is there a Google Analytics event that shows if someone did a quick start?

**Victor Coisne:** We have many events. We could add more — scroll events, copy button clicks on the command, etc. But we don't currently track actual installation, just clicks.

**Golzar Yaghoubpour:** We're in the middle of cleaning this up with a contractor. I'll verify and get back to you.

**Jason Gong:** So we have two routes: demo (full visibility) or quick start (we can track clicks on the copy button or how deep they read the docs). Either way, we get intent signal.

**Victor Coisne:** So the goal is to set reports in Looker, or are you comfortable building some in Google Analytics?

**Sydney Go:** We'll pull data from Google Analytics and display it in Looker Studio so it's prettier and more digestible than just raw GA data.

**Jason Gong:** We can get the insights however we can — building reports in GA or Studio.

**Victor Coisne:** That sounds good. I think that's all from me.

**Sydney Go:** Does anyone else have anything to add?

**Victor Coisne:** I think that's a good first meeting. I like where you're headed, and we have good action items. If you need anything in the meantime, let us know.

**Sydney Go:** Thank you so much. We're excited to work on this account. See you next week.

**Victor Coisne:** I'll get you the article list by end of week.

**Sydney Go:** Awesome. See you later.
