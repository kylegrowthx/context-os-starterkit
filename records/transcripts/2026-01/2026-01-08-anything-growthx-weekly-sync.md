# Anything <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-08
time: 21:59 UTC
duration: 78 minutes
organizer: team@growthxlabs.com
participants:
  - Dhruv Amin (Create, CEO)
  - Kyle Gaudreau (GrowthX, VP Customer Growth)
  - Katya Luscomb (GrowthX)
  - Zaria Zinn (Create)
  - Kallie (Create)
fathom_recording_id: 112928895
fathom_url: https://fathom.video/calls/524334775
share_url: https://fathom.video/share/Ms45TED55LAfLK7PK7cCC4h9kX1a28tS
source: fathom
enriched_on: 2026-02-28T14:32:00Z
</metadata>

---

## Summary

GrowthX and Create (an AI prompt platform) discussed misaligned expectations around SEO growth for anything.com, with Create pushing for aggressive results to hit $10M ARR by month-end while GrowthX reported 275 weekly organic sessions as "on track." The meeting surfaced three critical blockers: a domain consolidation strategy conflict (Create fears losing traffic from legacy domains), a missing analytics integration (GA4 not connected to Segment/PostHog), and a team execution gap that left the original strategy unmapped to action.

---

## Context

Create is an AI-powered software platform focused on product-led growth (PLG), currently at $7M ARR with an aggressive goal to reach $10M by month-end. GrowthX was contracted to drive SEO growth for anything.com as a primary revenue channel, completing an initial strategy sprint in late 2025. However, by early 2026, the handoff to Create's execution team surfaced tensions: the performance report (275 weekly sessions) is framed as "on track" by GrowthX, but Create views it as insufficient to hit their revenue targets and worries that GrowthX lacks urgency or ownership. Adding to this, Create's team made a domain consolidation decision in December (moving to anything.com) without full alignment from GrowthX, and Create's analytics stack (Segment → PostHog) was never connected to GA4, blocking the ability to measure organic traffic contribution to revenue.

---

## Relevance

- **Client Relationship Health:** Signals early-stage misalignment on success metrics and delivery pace. Create views GrowthX as under-delivering; GrowthX views Create as unrealistic. Escalation required.
- **GTM Strategy:** Highlights the difference between "on track" reporting (incremental growth) and "aggressive growth" (hockey stick trajectory). Create expects the latter; GrowthX is optimizing for the former.
- **Technical Execution:** Domain migration decision made without coordinated tracking setup creates risk of traffic loss and inability to measure revenue impact. GA4-Segment integration is critical dependency.
- **Team & Process:** Poor handoff from strategy to execution is a repeating pattern. Needs remediation to prevent further context loss.
- **Programmatic SEO Opportunity:** Brief mention of programmatic SEO as a growth lever. GrowthX should explore and present to Create.

---

## Overview

- **Strategic Misalignment:** A major disconnect exists between GrowthX's "on track" report (275 weekly sessions) and Create's aggressive growth goals, which require SEO to be a primary revenue driver.
- **Domain Migration Conflict:** GrowthX recommends immediate 301 redirects to consolidate SEO authority on `anything.com`. Create is hesitant, fearing a traffic loss from high-ranking legacy domains, citing conflicting advice from advisor Eli Schwartz.
- **Critical Tracking Gap:** Create's Segment/PostHog analytics stack is not integrated with GA4, preventing revenue attribution for organic traffic. GrowthX can consult, but Create must own the technical implementation.
- **Process Breakdown:** Create cited a poor team transition from the strategy sprint to the execution team, leading to lost context, a lack of urgency, and a feeling that GrowthX is not owning the strategy.

---

## Key Topics

### Strategic Misalignment & Growth Goals

- Create's primary concern is the slow pace of SEO growth, which is not meeting the urgency required to hit aggressive company revenue goals ($7M ARR → $10M ARR by month-end).
- The performance report's "on track" status (275 weekly sessions) is seen as insufficient and misaligned with the initial strategy sprint's promise of aggressive growth.
- Create's expectation is for SEO to be a primary revenue driver, not a slow-burn brand-building exercise.

### Domain Migration Conflict

- Create's current setup keeps three domains (`create.xyz`, `createanything.com`, `anything.com`) live to avoid traffic loss from high-ranking legacy pages.
- GrowthX's recommendation: Implement immediate 301 redirects from legacy domains to `anything.com`.
  - **Rationale:** The current setup dilutes SEO authority, sends mixed signals to Google, and risks a penalty.
  - **Risk:** Create fears an immediate traffic hit, citing conflicting advice from advisor Eli Schwartz, who suggested keeping legacy domains live.

### Performance Tracking & Revenue Attribution

- A critical gap prevents tracking organic traffic to revenue.
- **Current Setup:** Create uses Segment → PostHog for product analytics.
- **Problem:** GA4 is not integrated with this stack, making revenue attribution impossible.
- **Ownership:** GrowthX can consult on the tracking strategy, but Create must own the technical implementation.

### Process & Team Transition Issues

- Create cited a poor team transition from the initial strategy sprint (led by Eric) to the current execution team.
- **Impact:** This transition caused lost context, a lack of urgency, and a feeling that GrowthX is not owning the strategy.
- **Specific Examples:**
  - The domain migration, which occurred in early December, was not flagged by GrowthX until Dhruv mentioned it in January.
  - A content approval backlog in December was caused by a disconnect between the teams.

---

## Action Items

**Katya Luscomb (GrowthX)**
- Reschedule 1:1 w/ Kyle for Jan 9 or Jan 13
- Update all new content/sitemaps to anything.com; update internal links in old posts

**Kyle Gaudreau (GrowthX)**
- Audit GA4/Segment/PostHog; recommend tracking fixes; share w/ Dhruv Amin (Create)
- Draft domain migration plan (301s, GSC, sitemaps, homepage edge); share w/ Dhruv Amin (Create)
- Escalate internally; schedule call w/ Eric + Dhruv Amin (Create); share aggressive plan + projections

---

## Transcript

**Katya Luscomb:** Hey, Dhruv. How's it going? Happy New Year.

**Dhruv Amin:** Happy New Year. We're good. We're busy at start of the year, so just really focusing on PLG growth. But we're doing well. We just crossed like 7 million run rate and we're on track to try and hit like 10 by the end of the month.

**Katya Luscomb:** Nice. I'm quickly going to introduce Kyle. He's our VP of Customer Growth. Kyle, this is Dhruv from Create.

**Kyle Gaudreau:** Great to meet you, Dhruv. I've been at GrowthX for a little over a year now. Previously, I had 20 years in digital and growth, helping brands diversify their channels. Organic was usually a big part of that. I worked at places like Anaplan, Sendoso, and most recently Homebase, where I was actually the first GrowthX customer. So I've seen all angles of what GrowthX does.

**Dhruv Amin:** Oh, hey, Dhruv. Nice to meet you.

**Kyle Gaudreau:** What I lead here is kind of like a strategy SWAT team. So when certain things come up that need further support, I help dig in. Looking at what you guys are doing, I wanted to give you an early sense of what we're seeing and where we think things stand.

**Dhruv Amin:** So let's jump into the SEO performance and the domains. One of the biggest things on my mind is the pace of growth. We're at $7M ARR and trying to hit $10M by month-end. I need SEO to be a primary revenue driver for us, not just a slow-burn brand thing. We've been publishing five articles a week, and right now we're seeing about 275 weekly organic sessions. My question is: is this actually on track for what we need?

**Kyle Gaudreau:** I want to be fair here. The 275 is an early signal. Typically, at this phase, we're looking for compounding impression growth. Clicks can be volatile week to week. We're really trying to balance not reacting too fast, but also not too slow. Google is testing your content to see if it'll stick. Around month three, we usually see the first spike in clicks. We're at about seven or eight weeks now and we saw an early spike, which is actually a promising indicator.

**Dhruv Amin:** But that doesn't feel aggressive enough for where I think we need to be. When we did the strategy sprint, it felt like we were locked on metrics, on driving toward something specific. Right now, it feels like we're publishing content and hoping it works. And honestly, it doesn't feel like anyone on the GrowthX side is really owning this in an aggressive way. If I heard you say "275 now, but we see these signs and we think by March we'll be here," that would feel different. But right now it just feels like we're in a ho-hum, publish five a week and see what happens.

**Kyle Gaudreau:** I hear you. We don't want to paint lipstick on a pig here. If things aren't going well, we want to understand that. We need to make sure we're aligned on your actual goals at a deep level. I'll say, I encouraged Katya to do projections, but I pushed back on that initially because of the volatility from the domain migration.

**Dhruv Amin:** The domain migration is another huge concern. We migrated in early December. Nobody on the GrowthX side seemed to notice or flag it until I mentioned it in January. Every other partner managing a channel for us caught it immediately. So I was expecting GrowthX to be monitoring the metrics closely and see that change. That's when I sent a message saying, hey, let's update content to point to anything.com for interlinking.

**Kyle Gaudreau:** That's a fair point. We should have caught that. You're right.

**Dhruv Amin:** And then there's the domain consolidation question itself. We're keeping three domains live: create.xyz, createanything.com, and anything.com. Our strategy was to avoid losing traffic from pages that rank well on the legacy domains. But honestly, I'm getting conflicting advice. Eli Schwartz was saying to keep the domains live, but I'm not sure that's the right call.

**Kyle Gaudreau:** Our strong recommendation would be to accelerate the domain migration with 301 redirects. The current setup dilutes your SEO authority and sends mixed signals to Google. You risk a penalty. We should draft a migration plan that covers the 301 redirects, GSC updates, sitemaps, and how to handle the homepage edge case.

**Dhruv Amin:** How confident are you in that approach?

**Kyle Gaudreau:** I've seen it work on multiple accounts. The key is doing it thoughtfully, not reactively. We can work through a traffic-loss analysis so you understand the risk.

**Dhruv Amin:** What about tracking? Because right now I have no idea how much revenue this SEO work is actually generating.

**Katya Luscomb:** That's a critical issue. Your Segment and PostHog stack isn't connected to GA4, so you can't attribute organic revenue. We can consult on how to integrate them, but the technical implementation is on your team.

**Dhruv Amin:** Okay, that needs to get fixed. Can we at least figure out the tracking piece quickly?

**Kyle Gaudreau:** Yes. I'll audit your GA4, Segment, and PostHog setup and give you specific recommendations. But you're right, this has to be a shared priority.

**Dhruv Amin:** The last thing is the team transition. Eric led the strategy sprint, and then the strategy passed to Katya. In that handoff, we lost a lot of context. There was an approval backlog in December that didn't get flagged. And it just feels like the original strategy's energy got lost somewhere.

**Katya Luscomb:** I own that miss. I came in after the strategy sprint and there was definitely some knowledge loss in the transition. Our first live call was the second week of December, and that's when I flagged the backlog. We pushed through that quickly and cleared it out. I know that's something we can improve going forward.

**Kyle Gaudreau:** On that front, I think we should escalate this. Dhruv, would it help to talk directly with Eric so there's no more knowledge loss?

**Dhruv Amin:** Yeah, that would be great. And maybe whoever else is involved in the bigger picture here. Right now it feels like something's missing, or maybe it's me, but I want to make sure we're aligned on what excellent looks like for this partnership.

**Kyle Gaudreau:** I understand. Our strong recommendation would be: one, a more accelerated domain migration strategy; two, a deeper look at your tracking and making sure there are no gaps; and three, we explore what a programmatic SEO bet could look like to accelerate growth further. Typically, I'd want to lock this in over the next few weeks to see if we're getting compounding growth in these topics, and then what it would actually take to launch a bigger play.

**Dhruv Amin:** I like that. Let's get those projections locked in, escalate with Eric, and figure out the tracking piece.

**Katya Luscomb:** Sounds good. We'll reconvene with a clearer plan.

**Kyle Gaudreau:** Thanks for the time, Dhruv. We'll get moving on this.

**Dhruv Amin:** Appreciate you guys. I need to jump, but let's follow up on Slack on next steps.

**Katya Luscomb:** Will do. Thanks. Bye.
