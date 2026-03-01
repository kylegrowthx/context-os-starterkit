# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-01-23
time: 15:59 UTC
duration: 43 minutes
organizer: Stevie Kim (GrowthX)
participants:
  - Marcel Santilli (GrowthX CEO)
  - Daniel Lopes (GrowthX)
  - Jason Gong (GrowthX)
  - Pedro Steimbruch (GrowthX Engineering)
  - Jose Farias (GrowthX Engineering)
  - Estevão Mascarenhas (GrowthX Engineering)
  - Leonardo Carpenedo Steffen (GrowthX)
  - Stevie Kim (GrowthX)
fathom_recording_id: 116701379
fathom_url: https://fathom.video/calls/542568447
share_url: https://fathom.video/share/-yrBd6sPx-s7BiYeJbDFwYALDNNxKJ5C
source: fathom
enriched_on: 2026-02-28 02:15 UTC
</metadata>

---

## Summary

The team synchronized on Jan 31 launch readiness with one week to go. All major blockers are handleable: billing and paywall implementation is underway (Estevão), workspace invites PR is nearly complete (Pedro), and a critical UUID migration will unblock brand deduplication and category charts (Jose). Key UX decisions made include auto-accepting workspace invites during signup, renaming the default workspace to the user's brand, and implementing a 14-day credit card trial with workspace-level prompt limits.

---

## Context

CheckThat is CheckThat's Jan 31 launch date is imminent with the team targeting a coordinated release of core features: onboarding, workspace management, billing, and prompt tracking with AI visibility analytics. The team has been working through the "blockers week," addressing technical debt and product experience issues that need resolution before launch. This meeting brings all engineering leads together to sync on remaining work, unblock interdependencies (particularly the UUID migration that's blocking both billing and brand deduplication), and confirm the 14-day trial strategy with CEO Marcel. With one week remaining, the team is focused on keeping the launch on schedule while ensuring a solid onboarding experience and sustainable billing model.

---

## Relevance

- **Strategy**: Billing and trial model directly impact GTM and unit economics post-launch. 14-day credit card trial with workspace-level limits is the agreed go-to-market motion.
- **Engineering**: UUID migration is critical path blocker; Jose's timing coordination will determine when Pedro, Estevão, and others can unblock downstream work.
- **Product**: Onboarding workspace naming and auto-accept invite logic are core UX improvements that reduce friction for new users and teams.
- **Decision**: Post-launch downgrade logic deferred to manual handling; team will build automation after seeing real user behavior.
- **Launch Risk**: All identified blockers are now either resolved or in active progress with clear owners and daily coordination.

---

## Overview

- **Launch on Track for Jan 31:** All blockers are handleable, with key progress on billing (Estevão) and workspace invites (Pedro).
- **Critical UUID Migration:** Jose will migrate the `workspaces` table to UUIDs today, requiring a brief downtime, to unblock brand deduplication and category charts.
- **Onboarding Flow Redesign:** The confusing "Stevie Kim workspace" will be fixed by renaming the workspace to the user's brand during onboarding, creating a more intuitive flow.
- **Billing Strategy Decisions:** A 14-day credit card trial will be implemented, with prompt limits applied at the workspace level to prevent abuse.

---

## Key Topics

### Onboarding & Workspace Flow

  - **Problem:** The onboarding flow is disorienting. A user's brand-focused journey ends in a generic "Stevie Kim workspace," creating a disconnect.
  - **Root Cause:** The workspace is created too early in the flow (on email input), before the user provides a brand name.
  - **Solution:** Rename the workspace to the user's brand name immediately after it's provided. This is a quick fix that avoids a full re-architecture.
  - **Invite Flow Integration:**
      - **Goal:** Streamline the invite acceptance process.
      - **New Logic:** During Clerk sync, the system will check for an invite. If one exists, the user is automatically enrolled in that workspace. If not, a new workspace is created.
      - **Rationale:** This removes a friction-filled "accept/ignore" screen, as leaving a workspace is a simpler alternative.

### Billing & Payments

  - **Status:** Estevão has a working billing implementation and is now testing edge cases (trial end, cancellation, upgrade).
  - **Blocker:** The billing implementation is blocked by the `workspaces` table's `bigint` primary key, which conflicts with the `UUID` foreign keys used by the subscription model.
  - **Trial Period Strategy:**
      - **Decision:** Implement a 14-day credit card trial.
      - **Abuse Prevention:** To prevent users from creating 1,500 prompts on a trial and then canceling, prompt limits will be applied at the workspace level during the trial.
  - **Downgrade Logic (Post-Launch):**
      - **Problem:** When a user downgrades (e.g., from 500 prompts to the 50-prompt free plan), the system must decide which prompts to disable.
      - **Decision:** This is a post-launch task. The team will handle initial cases manually to inform the design of an automated job.
  - **Customer Handling:**
      - **Current Customers:** Will remain on the "unlimited" plan.
      - **New Prospects:** Will be given full access during strategy sprints. A manual "offboarding" process will be used to transition them to a paid plan or remove access.

### Technical Blockers & Progress

  - **UUID Migration (Jose):**
      - **Action:** Migrate the `workspaces` table from `bigint` to `UUID` primary keys.
      - **Why:** To resolve a foreign key type mismatch that blocks brand deduplication and category chart fixes.
      - **Impact:** This is a non-trivial migration that will cause a brief downtime. Jose will coordinate the timing to avoid demos.
  - **New Prompt Display (Pedro):**
      - **Problem:** New prompts have no trend data, but the current UI shows misleading empty trend lines.
      - **Solution:** Display an empty state message ("Hold on for data") instead of a chart.
      - **UI Decision:** New prompts will be shown in a separate section above the main table, with a toggle to hide/show them.
      - **Implementation:** Use two separate queries (one for prompts with data, one without) to simplify front-end rendering.
  - **Workspace Invites (Pedro):**
      - **Status:** PR is reviewed and nearly complete.

---

## Action Items

**Pedro Steimbruch (GrowthX Engineering)**
- Implement prompts index: empty-state trends, separate data/no-data queries, no-data section/filter
- Complete workspace invites PR

**Stevie Kim (GrowthX Product)**
- Pick up UI/UX blocker tickets this weekend
- Confirm 14-day trial strategy with Marcel; coordinate with Estevão on workspace-level trial limits implementation

**Jose Farias (GrowthX Engineering)**
- Execute workspaces table UUID migration today, coordinate timing to avoid demos and demo conflicts
- Create ticket: onboarding workspace name update to brand name
- Implement Clerk sync: auto-accept invites; if no invite create workspace
- Ship brand deduplication and category chart fixes after UUID migration

**Estevão Mascarenhas (GrowthX Engineering)**
- Add paywalls to billing PR, target completion by Monday
- Implement workspace-level trial limits (following Marcel confirmation from Stevie)
- Create ticket: post-downgrade prompt management (disable/retire prompts when user downgrades)

---

## Transcript

**Pedro Steimbruch:** Hi, Steve. Hey. How's it going?

**Stevie Kim:** Oh, pretty good. Oh my gosh, all these little things. I didn't realize that the meeting was moved back, so I woke up early anyway. I didn't get much sleep, but it was good because I took time to water all my plants this morning.

**Pedro Steimbruch:** That sounds good. Yeah, I had changed my lunchtime with family, and then I was, okay, let's lunch now because the meeting is not going to happen.

**Stevie Kim:** That's good. Okay. Let's see here. If someone wants to share their screen on the linear board with the launch ready, I can take notes. Yeah, I can share with you an AI companion thing. There's so many AI notetakers and companions now. So I just put a quick agenda on the Notion doc and had a couple things I wanted to discuss. But pretty much just going through status updates and what we've been doing is having a working session to unblock each other and align on how these things should work. We probably need to review some priorities if anyone has questions around priorities.

**Jose Farias:** Trying to figure out the right size for my screen. Is this too big or is it good? Okay. So we've added a couple of blocker cards since yesterday. Things like the brand logo override, which Estevão talked about yesterday. And then this is new as well. We have a decision to make here on the new prompt display. Currently, when you add a prompt, immediately we don't have trend data for it, of course, because we haven't been tracking it. And we can't backfill it because we don't have the data. Currently, what we're doing is we're adding it to the top of the table so when you go to the prompts index, you're not like, where'd my prompt go? Like, it's right here, but we don't have data for it. So it's suboptimal in two ways. One way is easily fixable, which is we're currently showing empty trend lines with 0% all the way through. And that makes no sense because it seems like we've measured it when we haven't. So I think just displaying an empty state there, like "hey, you obviously just added this today, like hold on for data."

**Stevie Kim:** That makes sense to me. I think what we would need to do is have some text at the top saying that prompts added within X days aren't shown until there's data or something like that. Just so people aren't looking for them because they will.

**Pedro Steimbruch:** You could spot a checkbox where we can say we have X number of prompts without data that are not being displayed below, and you can check to display them. Because even if we are not listing them, you may want to see what you have added, right?

**Stevie Kim:** That's true. Because otherwise they might forget and add the same prompt.

**Jose Farias:** I think a checkbox works, or an accordion, or even what we could do is just make them very small at the top, like "these are the five that you just added." They're tiny and it says there's a legend there like "these don't have data" and then the rest could be a separate section or in the same table. On the technical side, I just think they should be two different queries. Currently we're doing a left join. So I just think we do two queries, one for the ones without data, and that'll be super easy to handle in the front end because they're separate in the JSON. So it's like these are the ones that don't have data and then these are the ones that do. Rendering them is super trivial. Anyway, I think we've gone on long enough about this. That's something we need to tackle soon-ish. That's a new blocker, arguably maybe not a blocker, but then again.

**Pedro Steimbruch:** I will probably get to it today. I'm wrapping up the invite users to Workspace feature and look at it today.

**Jose Farias:** Cool. And then I know Estevão is running late, but I know we've been talking about this. He is well underway with the billing side of things. So that's going well. And I think that's the last big thing in the blockers list. So I know we haven't wrapped this up and it's Friday and we ideally would have wrapped this up this week, but I mean, we're close. I'm not worried.

**Stevie Kim:** So sorry, I was adding a note. That's the problem with taking notes. I can't focus. So you said the ones in progress, ideally we would have wrapped up the billing and onboarding or were you talking about anything else?

**Jose Farias:** It's just there's some tension here because the tag is called "blockers week." And so there's an expectation to wrap them up in that week. And we have had to spend a lot of time on these blockers because they're actually quite complex, right?

**Stevie Kim:** Right. So we have just a few more days.

**Jose Farias:** Yeah. And a lot of them are interconnected.

**Stevie Kim:** Right. So the UUID migration – that's Jose's task?

**Jose Farias:** Yeah, that's my task. And that's also, that's probably the thing that blocks a lot of other things. Because brand deduplication and category chart fixes are all dependent on that being done.

**Stevie Kim:** Right. So that's blocking Estevão's – it's blocking a bunch of things.

**Jose Farias:** Exactly. Yeah. So I think the UUID migration is probably the most critical thing to unblock.

**Stevie Kim:** Okay. And that's happening today?

**Jose Farias:** Yeah, I'll do it today. I need to coordinate the timing so we don't have any demos or anything happening.

**Stevie Kim:** Right. And it'll cause a bit of downtime?

**Jose Farias:** Yeah, there will be a brief downtime, but I'll coordinate it.

**Pedro Steimbruch:** I'm almost through with the workspace invites. So once Jose does the migration, I can finish off some of the blocker tasks after that.

**Stevie Kim:** And Estevão, do we know where he is in the billing?

**Jose Farias:** He's got a working implementation. He's testing edge cases now – trial end, cancellation, upgrade. But it's blocked by the UUID migration because of the foreign key mismatch.

**Stevie Kim:** Right. So once Jose's done, Estevão can probably push that through pretty quickly.

**Jose Farias:** Yeah. And he mentioned wanting to ship it by Monday, I think. So once the migration is done, he can wrap up the billing and paywall stuff.

**Stevie Kim:** Okay. And the onboarding workspace name thing – that's a separate task or is that tied to the billing?

**Jose Farias:** That's a separate task that I'll create a ticket for. It's about renaming the workspace to the user's brand name during onboarding, which is a UX improvement.

**Stevie Kim:** Right. And the Clerk sync auto-accept invites thing?

**Jose Farias:** Yeah, that's also something I'll be tackling. So during Clerk sync, if there's an invite for the user, we automatically enroll them in that workspace. If there's no invite, we create a new workspace. It removes the friction-filled accept/ignore screen.

**Stevie Kim:** Got it. So that's better UX. Okay. So what about the 14-day trial thing?

**Jose Farias:** So we've decided on a 14-day credit card trial. And to prevent abuse – like someone creating 1,500 prompts during trial and then canceling – we'll apply prompt limits at the workspace level during the trial.

**Stevie Kim:** Okay. So I need to confirm that with Marcel, and then Estevão can implement the workspace-level limits.

**Jose Farias:** Exactly. And we're also deferring post-launch downgrade logic. So when someone downgrades, like from 500 prompts to 50, we'll handle those cases manually at first to understand the behavior. We can automate it later.

**Stevie Kim:** Okay. So I'll confirm the trial with Marcel, and we'll create a ticket for the post-downgrade logic for after launch.

**Jose Farias:** Right. And current customers will remain on unlimited. New prospects will get full access during strategy sprints, and we'll manually transition them when they're ready to pay or lose access.

**Stevie Kim:** Got it. Okay. So action items: Jose, UUID migration today and then the workspace onboarding name thing and Clerk sync. Pedro, wrapping up workspace invites today and then the prompts display fix. Estevão, billing and paywalls targeting Monday, and workspace-level trial limits once I confirm with Marcel. And I'll pick up some UI/UX blocker tickets this weekend and confirm the trial with Marcel. And then we'll create a ticket for the post-downgrade logic. Does that cover everything?

**Jose Farias:** Yeah, I think so. The UUID migration is the critical path blocker, so once that's done, things should move pretty quickly.

**Stevie Kim:** Okay. Sounds good. Let's get to it.
