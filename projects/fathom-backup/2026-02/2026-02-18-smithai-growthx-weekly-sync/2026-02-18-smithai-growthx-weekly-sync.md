# SmithAI <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-18
time: 18:30 UTC
duration: 25 minutes
organizer: Andi Bailey (GrowthX)
participants: Maddy Martin (Smith.ai CEO), Andi Bailey (GrowthX), Jo Kaminska (GrowthX), Julian Wan (Smith.ai), Volodomir (Smith.ai - GA4 contact)
fathom_recording_id: 123441912
fathom_url: https://fathom.video/calls/570059796
share_url: https://fathom.video/share/ivHr-xsW89d3PMGcc3xDNENpNi4Ar_bN
source: fathom
enriched_on: 2026-02-27T00:00:00Z
client: Smith.ai
engagement_type: Weekly Sync
</metadata>

---

## Summary

Smith.ai needs GrowthX's reporting to shift from static snapshots to multi-month trend analysis that connects content production to lead generation and revenue impact. Key gap: current reports show raw data without context, making it difficult to justify the significant investment to leadership. Secondary focus: CheckThat tool refinement to prioritize high-intent queries (e.g., "best call center") and eliminate low-value monitoring keywords.

---

## Context

Smith.ai operates a dual-funnel business model: a high-touch sales team driving ~$1,000/month enterprise deals (primary revenue) and a low-touch self-serve funnel generating ~$100/month SaaS plans. GrowthX's content marketing supports both funnels but visibility into ROI is limited. Maddy Martin (CEO) emphasized that leadership needs concrete proof that the "significant investment" in content is moving the needle on lead generation and customer acquisition, not just traffic metrics. The company recently re-signed with GrowthX and is A/B testing pricing page positioning to attract more committed, multi-employee businesses buying annual plans. Data sources include GA4, Amplitude, Salesforce (capturing Calendly UTMs), and post-purchase surveys—but attribution remains complex due to multi-channel customer journeys and the company's emphasis on streamlining checkout (reducing pre-purchase form friction).

---

## Relevance

- **Reporting & Analytics:** Gap between current snapshot reporting and needed trend analysis; need for conversion definitions and older content inclusion.
- **Lead Attribution:** Multi-channel attribution complexity; Calendly bookings as primary lead capture; post-purchase survey data incompleteness.
- **Product Strategy:** Dual buyer targeting (sales-driven vs. self-serve); pricing page A/B test; content hub building effectiveness unclear.
- **CheckThat Tool:** New LLM visibility index needs curation; geo-targeting and bias mitigation questions; junior analyst (Usman) to filter prompts.
- **Organizational Changes:** Julian Wan departing; Volodomir becomes new GA4 and event tracking contact.

---

## Overview

- **Reporting Must Show ROI:** Reports must shift from simple snapshots to trend analysis, connecting content to leads to justify the significant investment to leadership.
- **Focus on High-Value Leads:** Prioritize sales-driven leads (~$1k/mo plans) over low-touch self-serve buyers (~$100/mo plans).
- **Check That Tool Needs Refinement:** The new LLM monitoring tool requires curation to focus on relevant, high-intent queries (e.g., "best call center") and filter out low-value ones.
- **New Data Contact:** Volodomir is the new technical contact for GA4 and event tracking, replacing Julian.

---

## Key Topics

### Reporting Gaps & New Requirements

- **Problem:** Current reports are static snapshots that don't connect activities to outcomes, making it hard to prove ROI.
- **Requirement:** Reports must show trends over several months to link content production to traffic and lead generation.
- **Specific Gaps:**
    - **Context:** Show data relative to prior periods.
    - **Attribution:** Connect traffic sources (keywords, referrals) to conversions.
    - **Analysis:** Provide insights beyond raw data pulls.
    - **Conversion Tracking:** Report on key events like Calendly bookings, not just generic clicks.

### Smith.ai's Business Model & Lead Strategy

- **Dual Buyer Funnel:**
    - **Sales-Driven:** High-value leads for white-glove service, generating ~$1,000/month plans.
    - **Self-Serve:** Low-value buyers for smaller plans (~$100/month).
- **Strategic Focus:** Prioritize sales-driven leads, as they represent the vast majority of revenue.
- **Pricing Test:** A/B testing the pricing page to feature annual plans, targeting more committed, larger small businesses.

### Check That Tool Feedback

- **Tool Overview:** GrowthX's new tool monitors Smith.ai's visibility in LLM search results.
- **Feedback:** The tool needs refinement to focus on relevant, high-intent queries.
    - **Example:** "best call center" is a high-value query; "AI agents trained" is low-value.
- **Action:** A junior analyst (e.g., Usman) should curate the monitored prompts.
- **Technical Questions:**
    - How does the tool avoid search bias (e.g., from a bot's own history)?
    - Does the bot simulate geo-tagged searches?

### Data & Tracking Infrastructure

- **Smith.ai's Data Stack:**
    - **Analytics:** GA4, Amplitude.
    - **CRM:** Salesforce (captures Calendly UTMs).
- **Lead Capture:** Calendly bookings are the primary lead source; post-purchase surveys are secondary.
- **New Contact:** Volodomir is the new technical contact for GA4 and event tracking.

---

## Action Items

**Andi Bailey (GrowthX)**
- Update reporting dashboard: add multi-month trend bars to show content production vs. traffic volume; define conversion events (Calendly bookings, not just generic clicks); add top-5 traffic sources by keyword/referral/geo; include performance of older content to assess compounding impact
- Email Maddy Martin (Smith.ai) re: CheckThat prompt methodology—specifically geo-targeting approach and bias mitigation to avoid model knowledge of Smith.ai; then curate/prune low-value prompts and invite Maddy for review
- Define and implement inflection-point tracking with Maddy: identify which pages drive conversions when, map to content production timelines, integrate Amplitude events, Calendly UTM data, and Salesforce lead records

---

## Transcript

**Maddy Martin (Smith.ai):** This meeting is being recorded.

**Andi Bailey (GrowthX):** Hey Maddy, how are you?

**Maddy Martin:** Good. We've been crazy busy.

**Maddy Martin:** One biggest issue right now is our entire industry is booming. It's hard to know if the water's rising for all boats or if ours is higher. We were having problems with Semrush—that tool isn't reliable anymore, causing visibility loss. I think you have another tool that could supplement it. When I look at SEO agency reports, they show historical context, not snapshots. My feedback: can we get bars for previous months? Show trend, not just a snapshot. That hasn't been fully resolved yet.

**Maddy Martin:** Event tracking requires GA4 integration. Julian is leaving—only here another week and a half. But Volodomir knows your entire event tracking system and will be the point of contact. We'll backfill. What I ask: more visibility into the production value of your work relative to where we were recently and historically. The main thing is communicating to our leadership that this significant investment has meaningful impact—not just eyeballs, but actual lead generation.

We're seeing a substantial increase in self-serve buyers (~$100/month)—very light-touch—but we haven't invested in that product experience. Historically, we've been high white-glove service at premium pricing. The vast majority of revenue comes through our sales team, generating ~$1,000/month plans. Self-serve buyers typically buy our smallest plan without talking to sales. Our help docs and navigation don't support that. We're A/B testing our pricing page now—showing annual plans vs. monthly tiers—to target committed, multi-employee small businesses.

**Andi Bailey:** Are you doing point-of-purchase surveys for self-serve buyers?

**Maddy Martin:** We ask "where did you hear about us?" because we track partner referrals. We spend ~$250k/month on ads, but surveys are post-purchase because we streamlined checkout. Data is incomplete. And it's multi-channel: they see a Facebook ad, search for us, read a review, might attribute to Google or Facebook. Unlikely they convert from a blog post immediately—they get retargeted with Facebook ads later. Multi-channel attribution is the real challenge.

**Andi Bailey:** Let's look at current reporting and talk through how you'd want it different. We're close but missing something.

**Maddy Martin:** There are no real conversions here. I don't even know what event you're tracking. Is it global event count? Could be scroll depth. Add a comment to the chart. You have "Get Started Expedited Click"—good. But does it show Calendly bookings? And relative to what? Are these new blog posts only? Why isn't last year's content showing? Is it not productive, or a filter? I'd expect new content to show up slower. You need a data analyst asking: what does the client really need to know? Are older articles compounding? Are we cannibalizing them? What's part of the hub? When you pull from Looker Studio with no analysis, it's just a screenshot—an interactive one. You need another layer of insight. What drives those landing pages? Of the top five, where's traffic coming from—keyword, source, referral, geo, LLMs, organic search? What's the intent level? Remember: some pages are audience-building retargeting; others are bottom-funnel.

**Andi Bailey:** I can show you CheckThat. Jo mentioned it. We focus on bottom-of-funnel prompts with evaluation criteria.

**Maddy Martin:** Haven't seen it yet.

**Andi Bailey:** Well done. CheckThat just launched—login bug, so no access now, but I'll invite you. We pulled all tracked prompts. See competitive presence—really good positioning. Filter by LLM, track daily, see position, sentiment, changes. These are links cited for you. Look at sources overall—URLs across all prompts, most-cited and changes. Helps identify traction and competitive gaps. But for prompts specifically—

**Maddy Martin:** Those are really specific prompts at the top. What's the sort order?

**Andi Bailey:** Visibility.

**Maddy Martin:** Someone junior at GrowthX could curate—maybe Usman now that he knows your brand. Concern: some we don't care about. Don't care if visible on certain keywords. But "best call center"—that's what real people search. "AI agents trained" isn't common. Surprised there are 60 responses. What does that mean?

**Andi Bailey:** Number of times we've asked the question.

**Maddy Martin:** You're automatically asking? Changing geo tags? Or always one location?

**Andi Bailey:** I believe so, but I'll double-check.

**Maddy Martin:** How does the model avoid bias from past searches? Clear its knowledge base? If I ask ChatGPT "Who's the best answering service?" it knows I work for Smith.ai—there's bias. "Best call center" is what people actually search. You write specific content; the bot expects you care about all those things. But look at our actual search prompts—that's not it.

**Andi Bailey:** I'll get answers on anonymizing to eliminate bias.

**Maddy Martin:** Good. Positive: those queries don't change much—need persists as markets shift. Businesses want calls answered. Queries change marginally, not majorly. Always price, availability, features, relevance—core buying factors.

**Andi Bailey:** We'll edit prompts before showing again and provide those answers. On tracking—I was thinking inflection points: which pages drive conversions, when, as you produce them. Use PostHog or similar?

**Maddy Martin:** Amplitude and other tools. Data pipes from Calendly to Salesforce—Calendly tracks prior UTMs. Most leads from Calendly bookings (no on-site forms)—main capture point. Phone calls too—receptionists capture source. You have GA4, Amplitude, Calendly UTMs, and Salesforce data to work with.

**Andi Bailey:** I'll work with our team on best tracking approach. I have a lot of follow-ups.

**Maddy Martin:** Anything else I can help with?

**Andi Bailey:** No, this is great. Glad we had this chat.

**Maddy Martin:** Me too. Thanks for catching up.

**Andi Bailey:** Bye, Maddy.

**Maddy Martin:** Bye.
