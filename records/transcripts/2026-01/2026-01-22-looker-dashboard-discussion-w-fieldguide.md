# Looker dashboard discussion w Fieldguide

<metadata>
date: 2026-01-22
time: 17:30 UTC
duration: 11 minutes
organizer: team@growthxlabs.com
participants:
  - name: Aida Knezevic
    affiliation: GrowthX
    email: aida@growthxlabs.com
    role: Strategist
  - name: Talal Syed
    affiliation: GrowthX
    email: talal@growthx.ai
    role: Technical SEO & Analytics Expert
  - name: Lindsay Walker
    affiliation: Fieldguide
    email: lindsay@fieldguide.io
    role: Paid Search Manager
fathom_recording_id: 116409099
fathom_url: https://fathom.video/calls/539596563
share_url: https://fathom.video/share/ZX9os7ZAtaK-5LkTAQMQ5F3EZ2MkVE6y
source: fathom
enriched_on: 2026-02-28 14:32 UTC
</metadata>

---

## Summary

Fieldguide's paid search manager seeks to prove their new branded search campaign (launched late Sept) is additive rather than cannibalizing organic traffic. GrowthX team will refactor the Looker dashboard with unified axes for click comparison and CTR-based impressions analysis to make performance differences immediately visible.

---

## Context

Fieldguide invested in a paid search campaign targeting branded terms in late September, and Lindsay Walker needs to demonstrate its value to internal stakeholders. The existing Looker dashboard uses dual Y-axes that obscure relative performance between organic and paid channels, making it difficult to prove additivity. The team identified two core problems: (1) monthly and weekly click comparison charts with misaligned scales that hide true performance differences, and (2) branded impressions vs. clicks chart where vastly different metrics (tens of thousands of impressions vs. thousands of clicks) appear incomparable due to axis scaling.

GrowthX, handling the Looker build-out as part of their engagement, sees this as an opportunity to strengthen the partnership and demonstrate the broader value of SEO and paid search investments.

---

## Relevance

- **Fieldguide Success**: Proving paid search additivity strengthens internal justification for continued spend and supports broader paid + organic SEO strategy.
- **GrowthX Delivery**: Dashboard refinement is within scope and demonstrates data storytelling capability to quantify marketing ROI.
- **Partnership Building**: Direct collaboration on client dashboards and analysis signals GrowthX's willingness to support strategic decision-making beyond content.

---

## Overview

- **Goal:** Prove the new paid search campaign (launched late Sept) is additive to organic traffic, not cannibalizing it.
- **Action 1:** Unify axes on click-comparison charts to show organic vs. paid clicks on a single, relative scale.
- **Action 2:** Replace clicks with Click-Through Rate (CTR) on the impressions chart to show if click share is maintained as impressions grow.
- **Comms:** Aida will notify Lindsay via DM when the updated dashboard is ready for review.

---

## Key Topics

### Proving Paid Search Value

  - **Problem:** The dashboard's dual Y-axes obscure the relative performance of paid vs. organic channels, making it difficult to prove the paid campaign's value.
  - **Objective:** Demonstrate that paid search spend on branded terms is additive to overall queries and clicks, not cannibalizing organic traffic.

### Dashboard Refinements

  - **Monthly/Weekly Click Charts**
      - **Issue:** Dual axes prevent a direct, relative comparison of organic vs. paid clicks.
      - **Solution:** Unify both metrics on a single Y-axis.
  - **Branded Impressions & Clicks Chart**
      - **Issue:** The dual-axis view (impressions vs. clicks) is confusing because the metrics are on vastly different scales (thousands vs. tens of thousands).
      - **Solution:** Replace clicks with Click-Through Rate (CTR) on a separate axis.
          - **Rationale:** This directly shows if the click share is maintained as impressions increase, proving the campaign's efficiency.

---

## Action Items

**Talal Syed (GrowthX)**
- Update Looker dashboard with three specific refinements: (1) unify organic and paid clicks on a single Y-axis for monthly/weekly click comparison; (2) remove the secondary axis; (3) replace clicks with Click-Through Rate (CTR) on the branded impressions chart to show whether click share is maintained as impressions grow
- Notify Lindsay Walker via DM when the updated dashboard is ready for review

---

## Transcript

**Talal Syed:** This meeting is being recorded.

**Aida Knezevic:** Nice to finally meet you.

**Talal Syed:** Yeah, likewise. I feel like we've been going back and forth in Linear and Slack for a while now.

**Aida Knezevic:** No, thank you. I think for what we're trying to do in Looker — oh, Lindsay just hopped on.

**Lindsay Walker:** Hi, Aida, can you hear me?

**Aida Knezevic:** Hi, yes. Thank you for hopping on.

**Lindsay Walker:** How are you?

**Aida Knezevic:** Good. You can call me Aida.

**Aida Knezevic:** So, I have Talal here. He is our resident technical SEO expert and also analytics expert. He's been customizing your Looker dashboard for the past couple of weeks. I wanted to get on a call with you to better understand what you want to see in this view. I'm going to share my screen so we can talk through it.

**Talal Syed:** Could you scroll down a bit?

**Lindsay Walker:** Sorry, my Wi-Fi is really going in and out, so I'm going to turn off my camera.

**Aida Knezevic:** Got it. No worries. I had the same thing yesterday. What was the last thing you heard?

**Lindsay Walker:** Just the introduction.

**Aida Knezevic:** Okay. Today I thought we could all get together. I've shared the view that we've been working on. We would love to hear what you'd like to get from this view and how we can help build that for you in Looker.

**Lindsay Walker:** Thank you for hopping on. I'm sure it's much easier to do this in person than back and forth. My main concern is that I launched a paid search campaign targeting branded terms in the last week of September. What I want to do is prove that this paid search investment is additive — that we're not just cannibalizing from organic search. My main goal is to show that our impressions and total clicks are increasing, and I want to see everything on the same relative scale so I can see where paid sits relative to organic.

**Talal Syed:** So what changes would you like us to make to the current view?

**Lindsay Walker:** Yeah, I think if we look at the monthly view — the axes are different, right? So we have organic clicks and paid clicks. I'd like to put these on the same axis rather than different axes, maybe even as a stacked bar chart, so I can see the actual numerical difference.

**Talal Syed:** Okay, so basically put both of these on the same Y-axis and remove the right axis completely?

**Lindsay Walker:** Yeah, exactly. So we can see the difference numerically.

**Talal Syed:** Yeah, I can make that change.

**Lindsay Walker:** Great. And then the weekly view is the same deal. And then this one — it looks like impressions are lower than clicks, which doesn't make sense for organic and paid.

**Talal Syed:** So for this graph, we're comparing two sets of numbers that are wildly different. Clicks are in the thousands, while impressions are in the tens of thousands. The branded clicks and branded sessions are on the left Y-axis. The branded impressions and ad impressions are on the right Y-axis. If you hover over any of these numbers, you can see clicks are around 1,000 to 3,000, while impressions are 44,000 to 98,000. That's how to read the graph right now.

**Lindsay Walker:** Okay, I see. So what I'd like to do is immediately see if impressions are going up and whether we're still maintaining our share of clicks. Maybe we can change the clicks to click-through rate and have that on a separate axis?

**Talal Syed:** I can try doing that, but adding a third set measured completely differently might not be super useful. Let me see what I can do — I might have to create a new graph.

**Lindsay Walker:** Yeah, you can get rid of the clicks. Just have impressions and then CTR. That'll tell us whether as impressions rise, we're losing CTR — whether we're not capturing the same proportion of clicks or maintaining the level.

**Talal Syed:** Yeah, that makes sense. Okay.

**Lindsay Walker:** Fabulous. I think that was it.

**Aida Knezevic:** Yep, that's it. Okay, cool. Glad we were able to help. I will keep you updated. I don't know if you're part of our external channel with Fieldguide or just in a DM with me and Yasin?

**Lindsay Walker:** I think I'm just in a DM at this point.

**Aida Knezevic:** Okay, no worries. So I will DM you when the updated version of the dashboard is ready. And yeah, we can take it from there.

**Lindsay Walker:** Okay, I appreciate this. I mean, I don't even know if this kind of thing is in your remit or under scope. So I really appreciate your partnership with us. I think it all goes towards helping management see that the investment we put in paid and SEO is valuable.

**Aida Knezevic:** Thank you. And we want to do the same thing. It does help us as well.

**Lindsay Walker:** Okay, great. Thanks again.
