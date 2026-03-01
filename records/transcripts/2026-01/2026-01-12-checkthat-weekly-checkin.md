# CheckThat Weekly Check In

---
title: CheckThat Weekly Check In
date: 2026-01-12
meeting_type: weekly sync
duration: 37 minutes
host: Marcel Santilli (GrowthX)
participants:
  - Estevão Mascarenhas (CheckThat)
  - Leo Steffen (CheckThat)
  - Daniel Lopes (CheckThat)
  - Pedro (CheckThat)
  - Stevie Kim (CheckThat)
  - Marcel Santilli (GrowthX)
  - Jason Gong (GrowthX)
  - Jose Farias (CheckThat)
source: fireflies
fireflies_id: 01KE7SZKEJCAT1PNWDWW8K9W5E
transcript_url: https://app.fireflies.ai/view/01KE7SZKEJCAT1PNWDWW8K9W5E
enriched_on: 2026-03-01 00:00 UTC
---

## Summary

The CheckThat team committed to shipping the onboarding flow by end of week to close the self-serve conversion loop. Marcel set a concrete north star: 10 organic, non-customer pro plan users by end of January. Wins this week: Daniel delivered an annotation system that's already improving content quality via prompt fixes; organic traffic is at 108 visits/week plus 60% additional from LLM referrals; Estevão's onboarding is 90% done (UI complete, phone validation skipped, backend pairing with Jose underway). Next: deploy test environment today, skip phone validation if needed, and model free/pro plan limits.

## Context

CheckThat is GrowthX's strategic software diversification play—an AI visibility index for B2B companies. Unlike the core services business (which relies on sales and existing customer relationships), CheckThat needs to prove strangers will pay for self-serve software. The product is already generating organic traffic through content marketing and LLM referrals (Perplexity, Gemini, ChatGPT). The team has been building for months but hasn't yet validated the core funnel: someone finds CheckThat organically, signs up without knowing anyone on the team, and pays for the pro plan.

Marcel is emphasizing urgency because Q1 is the fiscal proof point—without validating self-serve monetization by end of January, continued investment at current levels becomes harder to justify. The February board meeting is the next major milestone. The product positioning is clear; the challenge is pure funnel validation with real money.

## Relevance to GrowthX

### Product & Revenue Diversification
CheckThat is the proof-of-concept for recurring software revenue at GrowthX. Success validates the company's ability to build products that scale beyond consulting engagements. The 10 organic pro users goal is the minimum viable signal—one paid stranger validates the entire hypothesis.

### Board Meeting & Fiscal Planning
The February board meeting requires concrete proof: either organic users have converted and paid, or the bet is recalibrated. This week's work on the onboarding flow directly impacts what Marcel can show to investors.

### Team & Execution Learning
The annotation system Daniel built for CheckThat will become the template for Contentos (another content project). The onboarding flow teaches the team fast shipping under constraint—a skill that compounds across all GrowthX products.

## Overview

- **Content Generation Enhancements:** Daniel demoed the annotation and review system for QA. Admin panel captures quick and deep reviews, logs issues to JSON, filters by date. Prompt fixes deployed this week address FAQ improvements, transitions, and link behavior (external links to open in new tabs—deferred to rendering layer).
- **Organic Traffic Growth:** 108 organic visits last week, 50-second average session time. LLM referrals (Perplexity, Gemini, ChatGPT) add ~60% more traffic. Core traffic estimate: ~200 visits/week. Highest-intent pages (pricing, reviews) driving strongest conversion signals.
- **Onboarding Flow Status:** 90% complete. Brand creation, category selection, competitor adding all functional. Phone validation is the only mockup remaining—team opting to ship without it. Estevão deploying to isolated test environment today.
- **API Integration Blockers:** AI Overview and AI Mode support are near-emergency priority because probing data is unrecoverable once missed. Daniel spending one hour today on API research (Gemini with Google Search, Perplexity, ChatGPT APIs). Pedro to implement after Daniel's writeup.
- **Plan Limits & Tiering:** Jose modeling free (50 prompts) vs pro tiers. Admin panel toggle for manual customer tier management. All new users default to free plan with admin access blocked.
- **Cost Roadmap:** Future migration from Anthropic to AWS Bedrock will significantly reduce AI processing costs. Not urgent for next two weeks; planned for later this quarter.

## Decisions & Commitments

- **Skip phone validation in initial deploy** — Clerk integration deferred. Ship without it today; add as gating requirement later if needed. Reason: unblock sign-ups, reduce scope, avoid losing more days.
- **Deploy onboarding to production immediately after test** — Current preview environments share the production database. Estevão spinning up isolated test environment today, then move to live. Every day without live sign-ups is lost validation data.
- **Free plan limit: 50 prompts; Pro plan: higher limits** — Jose modeling exact tiers in admin panel. All new users default to free. Admin access blocked by default.
- **Daniel owns API research for AI Overview and AI Mode** — One-hour investigation today on Gemini, Google Search, Perplexity APIs. Pedro takes implementation after writeup. Marked as near-emergency because probing data can't be recovered retroactively.
- **Focus obsessively on the 10 organic pro users goal** — Any work that doesn't directly impact organic traffic growth, conversion rate, or onboarding flow gets zero priority. Futures, nice-to-haves, features all paused.
- **Migrate from Anthropic to AWS Bedrock** — Not urgent for next two weeks, but on roadmap for cost reduction. Daniel flagged for later planning.

## Key Topics

### Content Quality and Annotation System
Daniel demonstrated the new annotation system for capturing page quality feedback. The admin panel supports two review modes: quick review (single issue per page) and deep review (select chunks, log multiple issues). All issues are logged, filterable by date, and exportable as JSON for analysis. Daniel cross-referenced this JSON with Linear tickets to identify prompt changes needed. Fixes deployed this week include FAQ improvements, better transitions between sections, and a deferred item on external links opening in new tabs (should be handled at the React/Rails rendering layer, not in generation). This same workflow will become the template for Contentos.

### Organic Traffic and Conversion Urgency
Marcel emphasized that the team has achieved baseline traffic (108 organic visits + ~60% boost from LLM referrals = ~200 visits/week), but conversion is the real unknown. Average session time is 50 seconds—decent but not conclusive. The highest-intent pages (pricing, reviews) are already generating the strongest signals. Every week without a live sign-up flow is lost validation data that can't be recovered. The fiscal plan depends on knowing real conversion rates before Q1 ends.

### The 10 Pro Users North Star
Marcel set an explicit goal: 10 pro plan users from organic traffic by end of January. These must be strangers—not friends, not existing GrowthX customers, not anyone the team knows personally. They must find CheckThat through search, complete the entire funnel (sign up, choose a plan, provide payment), and actually convert. One user validates the hypothesis; 10 proves it's real. This is the north star for all decisions this week.

### Onboarding Flow Status & Shipping Decision
Estevão is 90% complete. Brand creation, category selection, and competitor management all work end-to-end. The only unfinished piece is phone validation (Clerk integration), which the team decided to skip for the initial deploy. Rationale: shipping 90% is better than shipping 80% while waiting for the last 10%. Phone validation can be added later as a gating requirement if needed. Estevão is spinning up an isolated test environment today to avoid conflicts with the production database shared by preview instances. Jose will sync on backend changes in parallel.

### AI Overview & AI Mode API Research (Near-Emergency)
These integrations are blockers for customer support. Last week the team deprioritized them during the onboarding sprint, but Marcel reactivated them as near-emergency priority. Reason: probing-related work is time-sensitive because lost data can't be recovered. Example: Brex customers lost a week of AI Overview data last week and have no way to backfill it. Daniel committed to one hour of API research today investigating which APIs are available (Gemini with Google Search, Perplexity, ChatGPT). He'll document workflows and trade-offs; Pedro will handle implementation after. Jose will do the Gemini work off-band after focusing on plan tiering first.

### Plan Tiering & Limits
Jose is modeling the free vs pro tiers in the database and admin panel. Free plan: 50 prompts (configurable). Pro plan: higher limits (TBD). All new users default to free. Admin access is blocked by default for new users. Marcel wants a simple dropdown in the admin panel so the team can manually adjust customer tier if needed. This blocks the ability to charge anyone, which is fine for now—the goal is end-to-end validation, not immediate monetization.

## Open Questions

- **Phone validation approach**: Clerk vs Twilio vs defer entirely? Marcel indicated research already done; team needs clarity on VoIP/disposable number handling.
- **Current vs new customer plan limits**: Stevie to surface this in the growth meeting. Are there different tier rules for existing GrowthX customers vs brand-new organic sign-ups?
- **LLM referral tracking**: Jason investigating whether Perplexity, Gemini, ChatGPT referrals can be grouped separately from organic. Current analytics conflate them under "referral" or "not set."
- **Conversion rate baseline**: Unknown. Even conservative fiscal assumptions could be wrong. Depends on actual organic sign-up behavior once live.
- **Contentos annotation system rollout**: Daniel proved the workflow on CheckThat. What's the timeline and team assignment for rolling out to Contentos?

## Action Items

### Daniel Lopes (CheckThat)
- Spend one hour researching API availability for AI Overview and AI Mode (Gemini, Google Search, Perplexity, ChatGPT)
- Write up implementation workflows and constraints for Pedro
- Create Linear ticket for external link target blank fix (defer to rendering layer)
- Flag migration from Anthropic to AWS Bedrock for future planning

### Estevão Mascarenhas (CheckThat)
- Deploy onboarding flow to isolated test environment with separate database
- Share test link and testing instructions with team
- Sync with Jose on backend changes before production push

### Jose Farias (CheckThat)
- Push backend changes to Estevão's development branch
- Model free tier (50 prompts) and pro tier limits in database
- Implement plan tier controls in admin panel with toggle for manual adjustment

### Pedro (CheckThat)
- Fix date range filtering bug on sources page (current blocker)
- Implement AI Overview/AI Mode integration after Daniel's API research writeup
- Prioritize Gemini integration given market share growth

### Marcel Santilli (GrowthX)
- Coordinate free vs pro plan implementation details
- Monitor infrastructure cost post-launch
- Provide clarity on plan limits for existing vs new customers (for growth meeting)

### Jason Gong (GrowthX)
- Move growth meeting to avoid all-hands scheduling conflict
- Investigate analytics approach for grouping LLM referrals vs organic traffic

### Stevie Kim (CheckThat)
- Coordinate blockers and prioritize assignments
- Prepare questions on current vs new customer limits for growth meeting

## Full Transcript

**Estevão Mascarenhas:** This meeting is being recorded.

**Daniel Lopes:** I wanted to give a quick update on what I did first, then I can leave to work on other stuff. I'll share my screen to show the annotation system for Kavishkam Kerry. This will be very similar to what we'll roll out to Contentos.

**Daniel Lopes:** I built an annotation system for page quality feedback. The admin panel has quick review (single issue per page) and deep review (select chunks, log multiple issues). All issues are logged and exportable as JSON. I cross-referenced yesterday's export with Linear tickets to identify needed prompt changes. Fixes deployed include FAQ improvements, better transitions, and a deferred fix: external links should open with target blank at the rendering layer, not generation. Everything else from the feedback list is fixed. I'll create a ticket for the external link item.

**Marcel Santilli:** Nice.

**Stevie Kim:** That's great. It's awesome to have feedback right in the app.

**Daniel Lopes:** This system validates the workflow we'll use for Contentos. The way we organize data and pass it will be the same across both projects.

**Stevie Kim:** Thanks for sharing. Let me pull up the Notion doc for this weekly sync.

**Marcel Santilli:** On organic traffic: we had 108 visits last week from organic search. Average session time: 50 seconds. We're also getting Perplexity, Gemini, and ChatGPT referrals amounting to about 60% of organic traffic. So combined, we're looking at roughly 200 visits per week.

**Marcel Santilli:** Jason, can you investigate a cleaner way to group LLM referrals versus organic in analytics? Right now they're scattered across "referral" and "not set."

**Marcel Santilli:** The core question isn't traffic—it's conversion. Are we converting at 1%, 0.1%, or somewhere else? That's a huge delta for our fiscal plan. Can someone who found us organically actually sign up and pay $200 for the pro plan? We're operating on conservative assumptions, but we don't know if we're conservative in a good or bad direction. Speed to validate this is critical.

**Marcel Santilli:** One week in this phase is meaningful. When we asked whether pages are getting indexed, we saw positive signals a few days later. Once we focused on what actually matters—indexing, impressions, hypothesis validation—the data became clear. By end of Q1, we need to prove monetization is possible. The market is real; other vendors are capturing it. We're confident demand exists.

**Marcel Santilli:** The urgency is about closing the full loop. We need one stranger who found CheckThat organically, signed up, and paid. Once we have that, we scale. We're not trying to move fast for speed's sake; we're trying to validate self-serve before layering in sales. Sales is always an option, but it's a band-aid if we can't prove self-serve works.

**Marcel Santilli:** North star: 10 pro plan users from organic traffic by end of January. Not friends, not customers we know. Strangers. Once we hit that, we understand our levers: click-through rates, organic traffic growth, conversion rates, monetization strength, value prop. Anything that doesn't directly impact getting to 10 organic pro users should get zero mental bandwidth.

**Jason Gong:** So to clarify: you mean someone who came in cold through organic search, went through the full funnel, and converted. Not asking Mario to swipe a card.

**Marcel Santilli:** Exactly.

**Stevie Kim:** Anything else before we dig into details?

**Marcel Santilli:** High-intent pages—pricing, reviews—are already showing stronger conversion signals. That's my hypothesis: clusters of high-intent content will outperform generic content. George Main has been working on improved landing pages. We also have a CTA bar and CTA widget ready. The strategy is: ship the onboarding flow first (even without monetization), then swap in all the CTAs. Once the sign-up MVP works, we measure conversions and drop-off. We can refine messaging and value props after validating the funnel works.

**Stevie Kim:** I have a question on George Main's mockups and how they fit with the onboarding flow prioritization.

**Marcel Santilli:** Those mockups aren't onboarding flows. If you're logged out and visit Overview, Prompts, or Sources tabs, the pages are out of context and broken. George designed proper landing pages for those. They're design-ready; we just swap them in. The CTA still points to a wait list until the full onboarding flow works.

**Stevie Kim:** I need a quick status update on the onboarding flow. What's blocking you?

**Estevão Mascarenhas:** I'm about 90% done. I planned to ship just the UI by Friday, but decided to make it work end-to-end first. Jose is reviewing backend changes. Current status: brand creation, category selection, competitor management all work. Phone validation is the only mockup. I'm setting up an isolated test environment today (our preview instances share production database). By end of day, I'll have a test link and instructions. One or two days of polishing needed, but it'll be functional.

**Marcel Santilli:** For phone validation—Clerk has it. VoIP and disposable number handling are configurable. If it's a bottleneck, we skip it. Traffic is already coming in; we can't afford to lose days. Ship what works.

**Daniel Lopes:** Drop phone validation for now. Deploy the working 90% and add it later.

**Estevão Mascarenhas:** Got it. I'll deploy to production after syncing with Jose. We'll test live.

**Marcel Santilli:** Sounds good.

**Jose Farias:** We need to plan what happens after onboarding. Plans aren't coded yet. Permissions are wide open—users could add unlimited custom prompts and blow our infrastructure costs. Practically, I don't think anyone will cause meaningful impact, so we can deploy with permissions on and figure out limits later.

**Marcel Santilli:** Implement free vs pro plan limits. Quick admin panel dropdown to toggle free, pro, and an unlimited (monitored) tier. New sign-ups default to free with 50-prompt limit. Block admin access by default.

**Leo Steffen:** When moving to production, I want to bucket CheckThat API keys separately so we can track costs.

**Daniel Lopes:** Admin access needs to be blocked for new users too.

**Jose Farias:** Correct. New users default to admin flag: false. I'll push changes to the branch and model the plan tiering in parallel.

**Marcel Santilli:** Sounds good. This will feel fast, but we've spent months on foundation. We need to prove it works by end of January. Board meeting in early February.

**Pedro:** This is one of the big bets of the year.

**Marcel Santilli:** Exactly. We've invested for months. If we can validate someone signed up and paid by end of January, that's a story for the board. Similar to Community—60k ARR now. We planned, then launched, and people paid. Same playbook here.

**Stevie Kim:** I have questions on current vs new customer plan limits for the growth meeting tomorrow. That overlaps with all-hands. Jason, can you move it?

**Jason Gong:** Yes, I'll move it.

**Marcel Santilli:** I have to run to HubSpot in 5 minutes. Catch me async on other blocks. The main one is AI Overview and AI Mode support. What's the status?

**Stevie Kim:** Still to do. We need to prioritize.

**Marcel Santilli:** AI Overview and AI Mode. These are probing-related, which is near-emergency because lost data can't be recovered. Daniel, can you spend an hour researching available APIs?

**Marcel Santilli:** Unless there's a good reason to deprioritize, flag it. Daniel and I decide priority; anyone else trying to change it—ignore them. Last week it was deprioritized for onboarding; now we have capacity.

**Stevie Kim:** Pedro, can you handle the AI Overview/AI Mode integration?

**Pedro:** I'm currently fixing a date range filtering bug on the sources page. If that's lower priority, I can switch.

**Daniel Lopes:** I can spend one hour today researching which APIs are available (Gemini, Google Search, Perplexity). I built the original workflows, so I can document implementation patterns. Pedro can implement after. But I need to flag: Gemini grew fast—five times bigger than Perplexity in market share the last two months. We also need to migrate CheckThat to our output framework eventually, but that's separate.

**Marcel Santilli:** Context for the future: probing-related work is near-emergency because data loss is permanent. Last week we lost a week of AI Overview data for our Brex customer. Fifty customers with zero data, zero recovery path. Every day without probing is lost data. Any probing provider failure should be treated as drop-everything priority.

**Jose Farias:** After Daniel finishes the API writeup, I think Pedro is the best choice for implementation. I need to focus on plan tiering first.

**Daniel Lopes:** But they have the two, two, two modes. Right. And I don't think they're going to support the same level of APIs because they didn't, they didn't have an AI mode API back then like a month, like a month and a half ago.

**Marcel Santilli:** I've got to run to HubSpot. Catch me async on anything else. Thanks team.

**Stevie Kim:** That covers the blockers. Daniel, one more thing: cost migration?

**Daniel Lopes:** We'll need to migrate from Anthropic to AWS Bedrock eventually. All processing cost moves to AWS—much cheaper. Not urgent for the next two weeks, but plan for it. Post-processing and brand extraction will need the same treatment. Even if we launch with higher Anthropic costs now, the bedrock migration is doable. Fallback to Llama if needed. Ticket for next week or the quarter.

**Stevie Kim:** Anything else?

**Jose Farias:** I'm prioritizing the backend plan modeling first, then Daniel's API writeup can go to Pedro for implementation. Google integrations can happen off-band.

**Stevie Kim:** Perfect. That's it. Thanks, everyone.
