# Anything <> GrowthX - Weekly Sync

<metadata>
date: 2025-12-18
time: 21:59 UTC
duration: 24 minutes
organizer: team@growthxlabs.com
participants: Dhruv Amin, Katya Luscomb
fathom_recording_id: 109926886
fathom_url: https://fathom.video/calls/509862987
share_url: https://fathom.video/share/AZCc27KARTCPToDzZTLu4xyxEzN2qwJC
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Katya presented month-one performance data for GrowthX's content engagement with Anything, showing 1k impressions and 15 clicks—a significant gap from what's needed to support Anything's aggressive growth targets ($7M current ARR, $10M goal next year). Dhruv emphasized the critical need to connect content performance directly to revenue impact and flagged a strategic disconnect: the original sprint goals established with Eric weren't being tracked against current execution. Katya committed to defining specific performance goals, investigating how to track content-to-signup conversions in Looker, and returning with a comprehensive plan in early January.

---

## Context

Anything is a no-code AI application builder experiencing rapid growth ($7M ARR). Dhruv Amin is driving fundraising efforts for the next round and is focused on ensuring all growth channels—including content marketing—are positioned to scale aggressively. GrowthX began a content engagement with Anything in November 2025, initially working through a strategy sprint team (Eric) to establish goals and content pillars. The account then transitioned to Katya Luscomb as the engagement manager for ongoing execution with supporting writers. This weekly sync is reviewing performance data from the first month of published content and aligning on next steps to drive both traffic and ultimately revenue impact.

---

## Relevance

**To GrowthX Delivery:**
- Performance gap signals need to refine content pillars and article positioning; the "AI app builder guide" cluster is outperforming others, suggesting that actionable, builder-focused content may drive better engagement than broader content.
- Strategic sprint-to-execution handoff created a context loss—original goals and keyword volume targets established with Eric are not being actively tracked against by Katya, requiring process improvement to maintain alignment across team transitions.
- Analytics setup (GA4 + Search Console) is currently insufficient for proving ROI; need to implement anonymous-user-to-signup tracking to move beyond traffic metrics and justify investment in revenue terms.

**To GrowthX Business Development:**
- Account health signal: Dhruv is in fundraising mode and performance is top-of-mind; early underperformance could put renewal/expansion at risk if revenue impact can't be demonstrated within 1-2 months.
- Expansion opportunity: If revenue tracking is successfully implemented, could become a referenceable case for other high-growth clients struggling with content attribution.
- Risk mitigation: Anything's rapid growth and aggressive scaling goals mean they may quickly deprioritize content if it doesn't show direct revenue impact; execution speed and clear metrics are critical to retention.

---

## Overview

- **Urgent Need for Revenue Connection:** Dhruv needs to link content performance to revenue to justify the investment, driven by Anything's rapid growth ($7M ARR, targeting $10M next year).
- **Performance Gap:** GrowthX content generated only 1k impressions and 15 clicks in its first month, far below the aggressive scaling required.
- **Strategy Disconnect:** Dhruv flagged a disconnect from the original strategy sprint goals, which were not tracked in the review.
- **Action Plan:** Katya will define specific performance goals and investigate tracking content-to-signup conversions to bridge the revenue gap.

---

## Key Topics

### Anything's Growth Imperative

  - Anything's rapid growth ($7M ARR, targeting $10M next year) requires all channels to scale aggressively.
  - This urgency drives the need to connect content performance directly to revenue, not just traffic metrics.

### Content Performance Review (Month 1)

  - **GrowthX Content Metrics:**
      - **Impressions:** \~1k
      - **Clicks:** 15
  - **Site-Wide Context:**
      - The blog drives \~50% of the site's search clicks, a surprising finding that needs further investigation.
      - **Clarification:** These are *search impressions* (views in search results), not on-site page views.
  - **LLM Referrals:**
      - Consistent click-throughs from LLMs (ChatGPT, Perplexity, Claude) started after publication began, indicating content is being discovered and cited.
  - **Top-Performing Cluster:**
      - The "AI app builder guide" cluster is outperforming others, signaling an opportunity to optimize future content strategy.

### Strategic Alignment & Revenue Tracking

  - **Strategy Disconnect:**
      - Dhruv noted a disconnect from the original strategy sprint goals, which were not tracked in the review.
      - **Context:** The account transitioned from the initial sprint team (Eric) to Katya for ongoing execution.
  - **Revenue Tracking Challenge:**
      - The current analytics setup (GA4, Search Console) cannot track the full user journey from article read → signup.
      - **Goal:** Track the anonymous user through to signup to connect content to revenue.

---

## Action Items

**Katya Luscomb**
- Deep-dive GSC page-level impressions; report findings to Dhruv
- Confirm LLM referral source in Looker; report to Dhruv
- Investigate Looker signup-to-revenue tracking; propose approach to Dhruv

---

## Transcript

**Katya Luscomb:** Hey, hey.

**Katya Luscomb:** Oh, I think you're muted.

**Dhruv Amin:** How's it going?

**Katya Luscomb:** Good, thanks.

**Dhruv Amin:** Good.

**Katya Luscomb:** Let me pull up my agenda.

**Katya Luscomb:** This is the week before all the holidays — how's it treating you?

**Dhruv Amin:** It's pretty intense.

**Dhruv Amin:** We're talking to a bunch of investors for the next round. Give me one second.

**Dhruv Amin:** Between us, Anything just crossed $7M run rate in revenue, and we're on track to hit $10M by next year. If we keep executing well, we'll hit $100M the year after that.

**Dhruv Amin:** What's really on my mind is growth — looking across all our channels and making sure they're set up for the next level of scale. That's why I'm asking: how is performance doing on the GrowthX content?

**Dhruv Amin:** Are we seeing the early signs that we're on track? And if not, do we need to adjust to actually get this ramping quicker?

**Katya Luscomb:** Yeah, that makes sense. I'm totally on board with that. One of the things on my mind is compiling monthly reports.

**Katya Luscomb:** Ideally at the start of each month, I compile a detailed performance review of the prior month, comparing it to others to watch those trends — not just clicks and impressions, but also clusters and individual articles performing well so we spot granular patterns and can execute.

**Katya Luscomb:** I've been sharing quick project management updates via Slack about articles and things coming down the pipeline.

**Katya Luscomb:** I flagged that we have 10 articles coming to you by the end of this week, covering content for this week and next. The 29th is quiet for us.

**Katya Luscomb:** As for performance, I dug in a little bit.

**Katya Luscomb:** Overall, we're seeing good traffic growth site-wide. Early in an engagement, we want to see steady traffic growth. We might not see huge spikes in the first couple of months, but trajectory-wise, we're in the right direction.

**Dhruv Amin:** Can we zoom in on this?

**Katya Luscomb:** Yeah, I can make them bigger. Sorry — I'm on a big desktop at home and it's showing really small on my other screen.

**Katya Luscomb:** These are from Search Console — comparing site-wide traffic to blog traffic. Your blog is driving the majority of your traffic, around 50% of your clicks.

**Dhruv Amin:** Wait — the blog is driving most of the traffic to the site? That's surprising.

**Katya Luscomb:** According to what Search Console has access to, yes.

**Katya Luscomb:** Impressions are views in search, and clicks are when people click through to the actual page.

**Dhruv Amin:** Got it — so it's search impressions, not page views on site.

**Katya Luscomb:** That's surprising though, because your site shows up for queries like "create," "Anything" — a bunch of keywords — and the blog impressions are already that high relative to the rest of the site.

**Katya Luscomb:** I can do a deeper dive and break out specific pages getting more impressions, because it could be a couple of blog posts driving a lot.

**Katya Luscomb:** I want to be clear — blog traffic overall isn't necessarily GrowthX traffic, since you have other blog content too. But we saw a dip during Thanksgiving week across all accounts — everyone went to eat turkey instead of reading content. The first week we started publishing, we saw good uptick in the second week, and good recovery after the Thanksgiving slump.

**Katya Luscomb:** I need to update a few things in Looker — it's having some trouble pulling data consistently for the week following this week in December. That's not abnormal; it takes a while for Looker to catch up to Search Console sometimes.

**Katya Luscomb:** I'm keeping a close eye on that through the rest of the month.

**Dhruv Amin:** So we're one month in — 1K impressions on GrowthX content, 15 clicks. Is that where we're at?

**Katya Luscomb:** Yes, 15 clicks from search traffic.

**Dhruv Amin:** Where were we expecting to get to, and on what timescale?

**Katya Luscomb:** Significant growth in clicks typically takes three months to see real progress and six months to see steady growth — it's not an immediate hockey stick. I can get you specific projections based on what we're seeing for the next month and two months, if that would be helpful.

**Dhruv Amin:** Sorry, also — there was a plan when we got started about where we could get to based on keyword volume and content strategy. How are we tracking against that plan? Are we on track or off track? Are we changing strategies or pillars?

**Dhruv Amin:** I know we're seeing traffic, but is it enough to drive actual outcomes? We're in a rush to scale and drive immediate impact. The disconnect for me is: how do we start connecting impressions and clicks to revenue?

**Katya Luscomb:** Looker doesn't always do well tracking leads. We can ask your team for lead data and cross-compare, which shows how content is actually impacting your prospects. We can also look at conversion signals like demo signups. I'll dig into how your Looker is set up and circle back on performance goals — I think that got buried in other content I was reviewing. When I put together comprehensive reports, I'll cross-reference to those goals so you have a clearer picture.

**Dhruv Amin:** What happened to the other people on the account — Eric and the others in the onboarding phase?

**Katya Luscomb:** They're still in the background at GrowthX. The strategy sprint to phase two transition works like this: the sprint team gets content up and running, calibrates tone and goals, then hands off to phase two. That's me as engagement manager with writers in the background. I resource out to our director team if there's a strategic shift or performance concerns. The sprint team specializes in prepping the initial plan and handing off for consistent execution.

**Dhruv Amin:** It feels like there's been a big context loss. We were tracking toward a plan, and now I'm asking for numbers but you're asking what that plan was. I need to know: we think we can hit X by Y, and we're either on track or not. We need to adjust week to week, not just "we get content out and see what happens." If we publish 50 articles but still can't hit X, it helps me understand what we're actually trying to drive to.

**Katya Luscomb:** That makes total sense, and I appreciate that feedback. I have more stats here, but if it's better use of your time for me to dig back into those specific goals, I'm happy to do that.

**Dhruv Amin:** I'll take the insights.

**Dhruv Amin:** What's this looking at — ChatGPT sessions?

**Katya Luscomb:** I looked at LLM performance. I went back to September to get a baseline of what you had before we started publishing. Before publication, there were fairly inconsistent referrals from large language models.

**Dhruv Amin:** How do you track this?

**Katya Luscomb:** This is in Looker — we pulled it from Search Console. Looker doesn't always show this particularly well.

**Katya Luscomb:** Dark purple is ChatGPT, light purple is Perplexity, green is Claude. We're seeing distribution across different models. Since publication started, we've seen more consistent referrals from large language models — this shows when folks see your content in an LLM and click through to your site.

**Dhruv Amin:** These are clicks?

**Katya Luscomb:** Yes, clicks. Interesting signal.

**Katya Luscomb:** Those are the highlights I wanted to flag before I do the deeper dive in early January. I was also looking at clusters — the "AI app builder guide" is getting more sessions than others, even though we've published fewer of those. That's a nice signal. The opportunity is to optimize content, maybe making it more actionable across other clusters.

**Dhruv Amin:** What's the next step? What goal are we trying to hit by when? And how quickly can we tie it to revenue?

**Dhruv Amin:** We're two months in now, and at this scale, it doesn't seem like it would impact revenue at all. I'm curious about that.

**Katya Luscomb:** I'm happy to circle back on that. I'll have more for you in our first meeting the first week of January.

**Dhruv Amin:** The key question for me is: how fast can we scale and tie it back to revenue? One more thing — your search traffic in Looker comes from Search Console, GA4? What's the source?

**Katya Luscomb:** We pull from Google Analytics 4 and Search Console, combined. It depends on the chart which one is sourced.

**Dhruv Amin:** Can we join that to site visitors or signups?

**Katya Luscomb:** We can track specific events like demo clicks. Tracking which article drove which signup is trickier — we need to define specific joining events, and there's limited access depending on those events. Demo clicks are straightforward when there's a distinct link; other events are stickier.

**Dhruv Amin:** The Anything site has a signup action on user events. If we can join the anonymous user to track through to revenue, that would help. What do we need to do to get there?

**Katya Luscomb:** I can definitely follow up on linking those closer for you.

**Dhruv Amin:** Anything else?

**Katya Luscomb:** Nope, that's it. Thanks. Have a good one.
