# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-01-27
time: 15:59 UTC
duration: 27 minutes
organizer: Stevie Kim (GrowthX)
participants:
  - name: Pedro Steimbruch
    affiliation: GrowthX
    role: Engineer
  - name: Estevão Mascarenhas
    affiliation: GrowthX
    role: Engineer
  - name: Jose Farias
    affiliation: GrowthX
    role: Engineer
  - name: Leonardo Carpenedo Steffen
    affiliation: GrowthX
    role: Operations
  - name: Stevie Kim
    affiliation: GrowthX
    role: Product Lead
  - name: Marcel Santilli
    affiliation: GrowthX Labs
    role: CEO
  - name: Daniel Lopes
    affiliation: GrowthX Labs
    role: Advisor
fathom_recording_id: 117444431
fathom_url: https://fathom.video/calls/544866011
share_url: https://fathom.video/share/AfaGhbUXTRQtYJbJM6ioATBjXYMYYD28
source: fathom
enriched_on: 2026-02-28 14:30 UTC
</metadata>

---

## Summary

The CheckThat team completed a tight, focused sync on final launch readiness with five critical systems shipping today: billing deployment, UUID migration validation, Track Company button merge, brand deduping feature, and SEO improvements. The team organized work by task owner (Pedro, Estevão, Jose, Stevie) with clear sequencing to unblock parallel streams.

---

## Context

CheckThat is launching imminently and the team has been laser-focused on shipping core systems. This meeting served as the final synchronization before launch deployment, with work organized across billing (Estevão), database migrations (Jose), user experience flows (Pedro), and product refinement (Stevie). The meeting was notably efficient—Stevie explicitly noted the team had met twice the previous day, so this session focused purely on actionable updates and blockers. Key dependencies were surfaced: the UUID migration Jose completed unlocks Jose's brand deduping work, which in turn impacts Estevão's billing schema; Pedro's user role feature is prerequisite for Estevão's owner-only billing access. The tone was pragmatic and execution-oriented, with team members flagging non-blockers explicitly and validating priorities in real time.

---

## Relevance

**For GrowthX Leadership (Marcel, Daniel)**
- Final validation that CheckThat engineering team is synchronized and unblocked on critical launch systems
- Clear visibility into deployment sequencing, risk surfaces, and team confidence levels
- Confirmation of SEO strategy alignment (P1 focus on category/subcategory descriptions)

**For CheckThat Product & Engineering (Stevie, Pedro, Jose, Estevão)**
- Explicit prioritization alignment: SEO improvements are P1 (not blockers, but high urgency)
- Unblocking signals: UUID migration complete, allowing Jose to ship brand deduping and unblock Estevão's schema changes
- Clear action ownership with team accountability on same-day shipping (billing, brand deduping, button merge)

**For Future Post-Launch Work**
- Product insight summaries inspired by Profound (overview page dashboard)
- Weekly/daily digest reports for brand ranking changes
- Subscriber Slack notifications for team celebration and tracking
- Date filter implementation on Prompt page (non-trivial UX decision pending)

---

## Overview

- **Billing is shipping today:** Estevão will deploy the billing PR, flip Stripe to live mode, and post a test coupon to the channel for team validation.
- **UUID migration is complete:** Jose's successful migration unblocks the brand deduping feature, which he will ship today.
- **"Track Company" button logic is defined:** Pedro is merging the button, which will guide users through onboarding, authentication, or to the waitlist based on their status.
- **SEO tickets are P1:** Marcel's new SEO tickets, including adding descriptions to categories/subcategories, are now a high priority.

---

## Key Topics

### Billing System

  - Estevão completed testing and will deploy the billing PR today.
  - **Deployment Plan:**
    1. Ship PR to production.
    2. Perform pre-testing.
    3. Flip Stripe account to live mode.
    4. Test with a 100% discount coupon.
    5. Post coupon to the channel for team-wide testing.
  - **Post-Launch Work:**
      - Set workspace name to brand name.
      - Implement "owner-only" billing access (requires Pedro's user role feature).
      - Build the paywall and competitor page.

### UUID Migration & Brand Deduping

  - Jose completed the UUID migration, which unblocks the brand deduping feature.
  - **Significance:** The migration was a success despite Render timeouts, updating millions of rows with no data integrity issues.
  - **Today's Plan:**
    1. Ship the brand deduping feature.
    2. Fix subcategory overview charts.
  - **Future Work:** Jose will add notes to the "Brands can select their own category" ticket, explaining the new, simpler implementation now that workspaces are categorizable.

### "Track Company" Button

  - Pedro is merging the "Track Company" button, which will guide users based on their status:
      - **Onboarded & Logged In:** Triggers a confirmation modal → auto-tracks company & backfills data.
      - **Onboarding Incomplete:** Redirects to the missing step, with the selected company pre-filled.
      - **Not Authenticated:** Redirects to the login/signup page, with the company ID persisted.
      - **Pre-Launch (Not Authenticated):** Redirects to the waitlist form.
  - **Other Tasks:**
      - Add brand logo to admin panel (Loom sent).
      - Address Marcel's comments on Workspace invite teasers.
      - Archive "Fix logo fallback" ticket (4.2.3) as the fix is already live.

### SEO & Product Strategy

  - **SEO Tickets:** Marcel created 5 programmatic SEO tickets (e.g., adding links to cards).
  - **Category/Subcategory Descriptions:**
      - **Requirement:** Add short descriptions to both categories and subcategories for SEO.
      - **Decision:** P1 priority. Jose will add a note to the ticket about storing descriptions directly in the tables if they are short.
  - **Competitive Analysis:**
      - Stevie reviewed data vendors (Data for SEO, Bright Data) for historical data.
      - **Conclusion:** Focus on improving our own generator and adding fan-out queries.
  - **Product Insight Summaries:**
      - **Idea:** Add a summary of key insights (e.g., AI visibility changes) to the overview page, inspired by Profound.
      - **Action:** Create tickets for this and other proactive product improvements.

---

## Action Items

**Pedro Steimbruch (GrowthX)**
- Address Marcel's comments on invite teasers
- Create Linear ticket: persist competitor ID across auth/onboarding
- Implement date filter on Prompt page; tag Stevie in PR
- Close outdated category/subcategory PR
- Test brand logo fallback; archive task if working
- Add short descriptions to categories and subcategories

**Estevão Mascarenhas (GrowthX)**
- Ship billing PR; flip Stripe live; post 100% coupon in Slack; test w/ Leo; set Slack sub alerts
- Implement workspace owner check for billing changes

**Jose Farias (GrowthX)**
- Ship brand deduping; then fix subcategory overview charts

**Stevie Kim (GrowthX)**
- Continue Phase 3 queuing work
- Create tickets for post-launch product improvements

**Leonardo Carpenedo Steffen (GrowthX)**
- Test billing system deployment with Estevão

---

## Transcript

**Leonardo Carpenedo Steffen:** Hello, team. Happy Tuesday.

**Pedro Steimbruch:** Yeah, happy Tuesday.

**Stevie Kim:** Okay, here's the Linear board. I feel like this one can be pretty short since we had two meetings yesterday.

**Pedro Steimbruch:** Yeah, so I'll start here. I finished the workspace invite teasers today and sent a Loom. I need to address minor comments from Marcel there. I'll do that after our call.

**Pedro Steimbruch:** I shipped the add brand logo to the admin panel and added a Loom so you can see how it's done.

**Stevie Kim:** Awesome, thanks.

**Pedro Steimbruch:** Now I'm about to merge the Track Company button to the company profile. If you have onboarding complete and you're signed in, it will ask for a confirmation modal, then auto-track the company and backfill data.

**Pedro Steimbruch:** If you don't have onboarding complete, it sends you to the missing step with the company pre-filled. If you're not authenticated, it redirects to the login page with the company ID persisted. And before launch, if not authenticated, it goes to the waitlist form.

**Pedro Steimbruch:** When we launch, we need to persist the competitor ID across auth and onboarding so it's pre-selected. I'll probably add a ticket for that.

**Estevão Mascarenhas:** I can go next. Today I wrapped up testing the billing system. I have one extra thing to finalize before we ship to production. After lunch, I'll ship the PR, do pre-testing in production, flip Stripe to live mode, test with a 100% discount coupon on my credit card, then post the coupon to the channel for team testing.

**Leonardo Carpenedo Steffen:** Can you ping me after lunch? Maybe in two hours?

**Estevão Mascarenhas:** Yeah, sure. I'll ping you.

**Estevão Mascarenhas:** After billing is validated, I'll set the workspace name to the brand name. Then I'll wrap up onboarding and handle the paywall and competitor page.

**Pedro Steimbruch:** Hey Estevão, when I merge the user invite feature, I'm adding a role column to enrollments. We need to make sure only workspace owners can change billing.

**Estevão Mascarenhas:** That's not something I need to do before shipping, but thanks for flagging it.

**Jose Farias:** That owner check should be trivial to add. Ship what you have, then once both are merged, we can introduce an authorization check in the controller. No need to delay.

**Jose Farias:** The UUID migration is finished. It took all day—I ran into Render timeouts but had to keep monitoring it. No exceptions, no data integrity issues. We updated millions of rows. It was a big migration but successful.

**Jose Farias:** This unblocks brand deduping because now workspaces can be subcategorizable using UUIDs as foreign keys. That impacts your billing work, Estevão—you mentioned needing to change a column to UUIDs?

**Estevão Mascarenhas:** I already rebased this morning, so it's already using UUIDs. All set.

**Jose Farias:** Great. I'll ship brand deduping first, then fix subcategory overview charts. I expect to ship both today, then grab items from the board.

**Stevie Kim:** Awesome, that sounds good.

**Stevie Kim:** I went through the backlog since I couldn't test on site. I spent time looking at data vendors for historical data—Data for SEO, Bright Data. Most are doing what we're doing with proxies. Data for SEO has fan-out queries on our roadmap. Bright Data does scraping but it's all proxies. They do panel data but it's a million a year and wouldn't license to us anyway.

**Stevie Kim:** I think if we focus on making our generator better, adding fan-out queries, and polishing things on our side, we'll be in good shape.

**Stevie Kim:** I also reviewed the backlog. There's a lot of little things. If anyone hasn't created tickets for post-launch work, definitely put those on the board so we can plan better.

**Stevie Kim:** Today I'm getting back into queuing and working on that all day.

**Stevie Kim:** One question: over the weekend I looked at the date filter. Marcel wanted the same date filter on the Prompt page. But it's not straightforward because of how we're fetching data differently on that page. Some decisions need to happen on how to handle it.

**Pedro Steimbruch:** Sounds good. I'll tackle that today or tomorrow and tag you in the PR so you can see the approach.

**Stevie Kim:** Yeah, I'd like to understand because it might change how we communicate things—tooltips and consistency.

**Pedro Steimbruch:** Hey Jose, the brands category selection ticket—now that workspaces are subcategorizable, we can probably handle it at the workspace level. Is that P1?

**Pedro Steimbruch:** Remember when Marcel said we should be able to change the subcategory for different prompts?

**Jose Farias:** Right. My work unlocks that considerably. Since it's P2, I'll write a note explaining how to do it now that workspaces are categorizable, then we can throw it back in the backlog.

**Jose Farias:** Assign it to me so I remember to comment.

**Pedro Steimbruch:** I'll close the PR I had opened since it doesn't make sense anymore.

**Jose Farias:** Right, it made sense then but now with workspaces being categorizable, we'd do it differently.

**Estevão Mascarenhas:** Hey Pedro, quick note on the fix logo fallback task 4.2.3. I think I already did that. When Fetch doesn't have a logo, it returns a 404, and we handle it in the brand logo component.

**Pedro Steimbruch:** I'll test it and archive it. Thanks for flagging.

**Jose Farias:** Marcel dropped five linear tickets about SEO in Slack. Not sure how to prioritize them. They're small, so any of us can tackle them. Someone needs to pick them up.

**Stevie Kim:** Are they related to content?

**Jose Farias:** Programmatic. Things like adding links to cards in certain places.

**Stevie Kim:** Okay.

**Pedro Steimbruch:** Do we have descriptions on categories and subcategories?

**Jose Farias:** I don't think so.

**Pedro Steimbruch:** There's a ticket asking for short descriptions on both categories and subcategories for SEO.

**Jose Farias:** There are a couple hundred categories. We could LLM them.

**Jose Farias:** Actually, I keep thinking—are categories and subcategories the same thing? We have a hard architectural dependency on subcategories. If they were just records in the categories table, it would be hidden. If we add descriptions, we'd need to add them in two tables, which is weird.

**Pedro Steimbruch:** I'm trying to see if we need descriptions in categories. It doesn't seem like it. But for subcategories, yes—we need short descriptions on both.

**Jose Farias:** Whoever picks it up should be careful about description length. If they're short, fine to store in the same table. If they're long text columns, we don't want them on the same table because we'd load them every time. Keep descriptions short.

**Pedro Steimbruch:** Is this on the board?

**Jose Farias:** I don't think so. It's probably P1—we want to do this soon.

**Stevie Kim:** Let's mark it P1 because it's not a true blocker, but we should tackle it. We wouldn't push this ahead of functionality though.

**Pedro Steimbruch:** I agree.

**Jose Farias:** Can we tag Linear in that Slack thread to add this tag to all the SEO tickets?

**Stevie Kim:** I spent time in Profound yesterday. They have a nice summary on their overview page—what your AI visibility was, the changes, what's new. It seems like it wouldn't be a huge lift. Not saying we'll do it for launch, but it's a nice way to quickly understand what's happening holistically without looking at all the charts and individual prompts.

**Stevie Kim:** As we go through the product, if you think of anything else that makes it easy for users, put it in a ticket and prioritize it.

**Estevão Mascarenhas:** I discussed this with Daniel months ago. We talked about a weekly or daily digest that generates a report—which brands are jumping ranks, dropping, just an overview of the week.

**Estevão Mascarenhas:** I'm very interested in this.

**Stevie Kim:** Make tickets for these ideas. We can get ahead of it instead of waiting for customer feedback. Especially if we see something a competitor has and we have good ideas.

**Estevão Mascarenhas:** Quick question before we wrap: how do you feel about a Slack notification when we get a subscription? Not a blocker, but maybe this weekend or next week we set it up. Small celebrations.

**Leonardo Carpenedo Steffen:** I'm on board. That's what we're trying to prove—that people will buy this.

**Stevie Kim:** We want 10 subscriptions in the first month after launch, a hundred in a quarter. Definitely on board.

**Estevão Mascarenhas:** Okay, let's do it. I'll set it up.

**Leonardo Carpenedo Steffen:** Ping me when you get it in prod. I'd like to help you test.

**Stevie Kim:** Yeah, Leo testing billing would be great so I can stay focused on Phase 3 of queuing.

**Leonardo Carpenedo Steffen:** I'll work with Estevão on testing.

**Stevie Kim:** Okay, if that's it, we can close out. Thanks, everyone.

