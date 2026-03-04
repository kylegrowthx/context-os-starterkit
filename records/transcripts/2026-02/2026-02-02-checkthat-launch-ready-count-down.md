# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-02
time: 17:29 UTC
duration: 40 minutes
organizer: Stevie Kim (GrowthX)
participants: Estevão Mascarenhas, Leonardo Carpenedo Steffen, Daniel Lopes, Jose Farias, Stevie Kim
participants_external: None
fathom_recording_id: 118984526
fathom_url: https://fathom.video/calls/550962473
share_url: https://fathom.video/share/G5aSZtgsbqQMtmHaxj7PgNi6e2-c2xcx
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

The CheckThat product is nearly launch-ready with core features complete: the team finalized the historical data upgrade path, billing flow, and Stripe configurations. Immediate priorities are polishing the onboarding UI, removing the waitlist for internal testing today, and establishing scalability safeguards through a separate backfill worker. The phased launch will begin with internal testing, followed by staged customer invitations, supported by Intercom with an AI co-pilot for initial user support.

---

## Context

CheckThat is GrowthX's AI visibility index software—a strategic bet on B2B content marketing insights. The core team includes Estevão (product/infrastructure), Leonardo (billing and deployment), Daniel (workflows and customer data), Jose (backend/scalability), and Stevie (operations and support). This final pre-launch sync happened on February 2, 2026, with the team in sprint mode to lock down product stability, support infrastructure, and customer communication workflows before opening access to the waitlist. The meeting doubled as a working session to resolve blocking issues and confirm assignments for launch day.

---

## Relevance

### CheckThat (Product)

- **Launch readiness:** Historical data upgrade path, billing flow, and onboarding UI are the final blockers before production launch.
- **Scalability strategy:** Separating the backfill worker isolates database load, enabling independent scaling during traffic spikes without degrading core app performance.
- **Product polish:** Onboarding UI needs visual refinement; brand lookup logic requires fix to prevent incorrect domain matches (branch.io → branch.co).
- **Support infrastructure:** Intercom with AI co-pilot trained on internal knowledge base enables fast, consistent customer support at launch scale.
- **Customer data stack:** RudderStack routes user events to Customer.io (email campaigns), PostHog (analytics), and Intercom (support), creating a connected martech ecosystem for lifecycle engagement.

### Delivery & Operations

- **Phased rollout plan:** Remove waitlist today, enable self-serve signups for internal testing, then staged customer invitations followed by public announcement.
- **Billing automation:** Stripe UI configured for automated receipts, invoices, and cancellation reminders; Customer.io handles complex lifecycle emails later.
- **Action items:** 11 concrete tasks distributed across team; most blocking items assigned to Estevão and Leonardo for immediate completion.
- **Workflows framework:** Output.ai on Temporo provides isolated namespace for CheckThat workflows; separate Render services (API, worker, Redis) with autoscaling worker handle execution; notification gap on failure identified for follow-up.

---

## Overview

- **Launch Readiness:** The product is nearly ready, with the historical data upgrade path and billing flow complete. The main focus is now on polishing the onboarding UI, enabling self-serve signups, and finalizing support infrastructure.
- **Scalability Plan:** The backfill process is being split into a separate worker to isolate its heavy database load. This allows for independent scaling to manage traffic spikes without impacting core app performance. Two queues manage backfill priority: critical (last 7 days required for app access) and low-priority (older data).
- **Support Strategy:** Intercom will serve as the initial support channel, using an AI co-pilot trained on an internal knowledge base to provide fast, consistent answers and capture user questions for future help content. The admin panel includes an activity feed to provide context on user behavior.
- **Phased Rollout:** A phased launch is planned to manage initial load. The waitlist will be removed today for internal testing, followed by exporting emails to Customer.io for staged invitations, then a wider public announcement.

---

## Key Topics

### Launch Strategy & Phased Rollout

- **Goal:** A phased launch to manage initial load and test system stability.
- **Today:** Remove the waitlist for internal testing and enable self-serve signups.
- **Launch Day:** Export waitlist emails → import to Customer.io → send invites with personalized onboarding.
- **Communication:** A small, contained announcement will precede a larger public post (e.g., on LinkedIn).
- **Rationale:** Testing in production with a trusted group reduces risk and gathers real-world feedback before full public access.

### Scalability & Performance

- **Problem:** Unpredictable load from backfilling historical data could degrade core app performance during a launch traffic spike.
- **Solution:** Split the backfill process into a separate worker with its own queues, deployed on Render with autoscaling.
  - **Critical Queue:** Processes the last 7 days of data, which is required before a user can enter the app.
  - **Low-Priority Queue:** Handles all older data asynchronously.
- **Contingency Plan:**
  - **Slow Backfills:** Increase worker count.
  - **Database Lag (Replication/Contention):** Decrease worker count or upgrade the database tier.
  - **CPU Probing:** Daniel to verify Render's workflow worker CPU metrics configuration with support.
- **Trade-off:** Accept slower backfills for new users in exchange for maintaining core app stability and preventing cascading failures.

### Product & Billing

- **Historical Data Upgrade Path:**
  - **Status:** Wrapping up today (Estevão completing PR).
  - **Functionality:** Users on free/lower-tier plans see a lock icon for data older than their plan allows. Clicking it triggers an upgrade modal.
  - **Post-Upgrade:** The system automatically backfills the newly unlocked data period asynchronously.
  - **Scope:** Unlimited historical data for the Business plan is deferred to a follow-up PR to prioritize production testing and avoid scope creep.
- **Billing Flow:**
  - **Status:** Complete; all core payment and plan management features functional.
  - **Gap:** No automated transactional emails (e.g., receipts, cancellations).
  - **Plan:** Use Stripe's UI settings to automate receipts, invoices, and cancellation reminders for launch. More complex lifecycle emails (upgrade encouragement, churn prevention) will be built in Customer.io.
- **Onboarding UI:**
  - **Status:** Functional, but needs polish for a better first impression.
  - **Action:** Estevão will polish the UI today; can be enabled for internal testing even before public launch.
- **Onboarding Brand Lookup Fix:**
  - **Problem:** Brand lookup in the onboarding flow returned incorrect matches (e.g., "branch.io" matched unrelated "branch.co").
  - **Solution:** Skip the lookup if user explicitly selects "No" when shown initial search results; prevents incorrect data association.

### Support & Analytics Stack

- **Intercom:**
  - **Function:** Primary support channel for launch and beyond.
  - **Knowledge Base:** Populated from Notion and code; used to train an AI co-pilot for fast, consistent answers.
  - **Process:** User questions → "All inbox" → team member assignment → AI-assisted reply option.
  - **Admin Panel:** Includes activity feed to view user events (page views, actions) for rich support context.
  - **Future:** Stevie to draft support guidelines and review Intercom KB with team to identify content for future public help center.
- **Martech Stack:**
  - **RudderStack:** Central event router that connects app events to downstream tools.
  - **Customer.io:** Receives full user data and events for email campaigns, lifecycle engagement, and onboarding.
  - **PostHog:** Receives events and offers superior session recording for debugging and UX insights.
  - **Intercom:** Receives basic user data (name, email) for support context.
  - **Google Analytics (GA):** Jason to verify Google Tag Manager configuration to resolve console errors.

### Workflows Framework

- **Platform:** Output.ai workflows running in an isolated `checkthat` namespace on Temporal (distributed workflow engine).
- **Architecture:**
  - **Repo:** `checkthat-workflows` (owned by Daniel).
  - **Structure:** Workflows in `source/workflows`; shared agents in `source/gx` (do not modify).
  - **Deployment:** Separate Render services (API, worker, Redis) with worker autoscaling to handle variable load.
  - **Documentation:** Daniel to share workflow env in CheckThat vault and docs link (docs.ai/output.ai) with team.
- **Known Gap:** No notification from workflows back to the app on failure. This is a potential source of "stuck" processes and will be addressed in a follow-up.
- **Cleanup:** Daniel to ship workflow execution cleanup: cancel runs >4 hours, purge records >30 days to prevent database bloat.

---

## Decisions & Commitments

- **Remove Waitlist Today:** Estevão will remove the waitlist and enable self-serve signups to allow internal team testing in production.
- **Stripe Automation:** Leonardo will configure Stripe UI to automate receipts, invoices, and cancellation reminders for launch.
- **Billing Admin Panel:** Estevão will add billing info and plan change functionality to the admin panel for custom support scenarios.
- **Customer.io Export & Training:** Daniel will create Linear ticket to export waitlist emails, import to Customer.io, and record Loom walkthrough explaining the platform to the team.
- **Phased Launch Confirmation:** Daniel will confirm the phased launch plan with Jason (who handles GTM announcements).
- **Intercom Knowledge Base:** Stevie will draft support guidelines and review internal KB with team to seed a future public help center.

---

## Open Questions

- **Workflow Failure Notifications:** Currently no alert from workflows back to the app when execution fails; potential source of stuck processes. This will be addressed in a follow-up.
- **Database Upgrade Path for Business Plan:** Unlimited historical data for Business plan deferred to follow-up PR to avoid launch delays; team will test and measure production load first.
- **GTM Console Errors:** Jason to verify Google Tag Manager configuration; exact issue to be diagnosed separately.

---

## Transcript

**Leonardo Carpenedo Steffen:** We're waiting for more people to join? I don't know if everyone's joining today.

**Stevie Kim:** I don't think they're joining.

**Leonardo Carpenedo Steffen:** Let me check. Pedro declined. Marcel declined. Jason is optional.

**Daniel Lopes:** I'm ready.

**Leonardo Carpenedo Steffen:** How do you guys want to do this?

**Stevie Kim:** So usually like Pedro or someone else shows their screen—the linear board—while I take live notes. Since my vision's not great right now, I'll just rely on the note takers, but if someone wants to share the linear board, the launch ready board, that would be wonderful.

**Stevie Kim:** Let me share the linear board here.

**Leonardo Carpenedo Steffen:** First time doing this, so you guys can help me next time if needed.

**Stevie Kim:** Yeah, so everybody can give their status updates and if there's anything blocking or needs discussion, we discuss it live here. Treat it as a working session.

**Leonardo Carpenedo Steffen:** Cool.

**Estevão Mascarenhas:** Can I start?

**Leonardo Carpenedo Steffen:** Yeah, go ahead.

**Estevão Mascarenhas:** So for the historical data upgrade path, I'm wrapping it up today. Basically, users on the free plan who want to see data older than what their plan allows will see a lock icon on that option. When they click it, they see the upgrade modal. When they upgrade, we start backfilling that period for them. So it's almost there. Just one thing I'm leaving out for this PR—I'll open a follow-up—is unlimited historical for the business plan. I want to test this in production first because it worked locally. So I'm wrapping it up today.

The billing task, I intended to break it down and document the progress there but just rushed through it. I'll leave a message there so Leo can see what we're missing. For example, we're not sending transactional emails. We can handle lifecycle emails later—like when a subscription is ending, we can try to engage the user with coupons.

**Daniel Lopes:** That can also be part of it. If you trigger the events—for example, when billing events happen—we can put an event on them. Yeah, great. That's one of the key parts for email campaigns. Now all emails can be controlled from Customer.io. You can have lifecycle emails, subscription reminders, that kind of stuff. Ideally all done through there.

**Leonardo Carpenedo Steffen:** Yeah. I noticed receipts aren't sent automatically. I logged into Stripe and sent them to myself while testing. You can send cancellation or...

**Daniel Lopes:** Receipts make sense. Yeah, receipts would be ideal, but all the engagement stuff—upgrade reminders, that kind of thing—we can add through Customer.io. It's pretty easy to build campaigns there. But if Stripe supports turning on invoices and other stuff automatically, that would be ideal.

**Stevie Kim:** I'm going to do that. We can do some of that through the UI already, but I wasn't sure exactly what we wanted. There should be settings for everything—reminding people they're about to get charged, receipts, invoices. I want to make sure everything's consistent though, because a lot of stuff I originally set up in the UI is now done on the backend.

**Estevão Mascarenhas:** Yeah, perfect.

**Leonardo Carpenedo Steffen:** So we'll look at the Stripe configs to make sure we can automate at least receipts and cancellation emails for launch, until we have a more elaborate email policy. I'll do that.

**Estevão Mascarenhas:** Okay. My plan for today is adding billing-related information to our admin panel and the ability to change plans there, just in case we want to customize that for customers. And I want to get to polishing the onboarding UI. It's functional and working, but we can improve it for a better first impression at launch. It's not bad, but I want to spend time there.

**Daniel Lopes:** Can we already turn it on for just us, before we announce, so it's way in production?

**Leonardo Carpenedo Steffen:** Yeah, I think so.

**Estevão Mascarenhas:** I can remove the waitlist today as well. We're getting a couple of people every other day signing up. We can just go through and test ourselves.

**Daniel Lopes:** We can export the waitlist data and load it into Customer.io on launch day. I can record a Loom explaining how Customer.io works so everybody has context, even if Jason is the one doing it. But I can document it.

**Estevão Mascarenhas:** And just one final task: I need to remove the brand lookup from the onboarding when a user says 'No'. We had issues where typing "branch.io" matched "branch.co"—a totally different South African company. The lookup was returning the wrong company description. So when the user selects 'No' to the initial search results, we'll skip the lookup. That's the change I need to do.

**Stevie Kim:** So is Jason going to be responsible for getting those waitlist emails and sending invites, or Daniel?

**Daniel Lopes:** Can you add a ticket, Leo, for me to export those users and load in Customer.io and record a Loom?

**Leonardo Carpenedo Steffen:** Yeah, I can do it.

**Daniel Lopes:** I can do that.

**Leonardo Carpenedo Steffen:** Okay, sounds good.

**Daniel Lopes:** Okay, I can share my update. The CheckThat workflows project structure is finalized. All workflows live in the `checkthat-workflows` repo under `source/workflows`. The shared agents in `source/gx` should not be modified—they'll be separated into an NPM package. Content-related pipeline changes are prototypes of what we're building in ContentOS, so please coordinate with me before modifying those. Everything else is fair game.

**Daniel Lopes:** The docs are at docs.ai (password: output.ai) with getting started guides and installation instructions. Regarding the martech stack: RudderStack routes all data to Customer.io (full user data and events), Intercom (user names only), and PostHog (events and session recording). GA is configured through Google Tag Manager but had some misconfiguration errors—Jason will verify it in production.

**Daniel Lopes:** For Intercom, Alice loaded our internal knowledge base from Notion and code. When users ask questions, they pop up in the "All inbox." We can use the AI co-pilot to draft answers from the knowledge base and adjust as needed. This approach means we don't need to hire support staff this month; we can assess load next month and decide on dedicated support then. The internal KB also becomes a foundation for a future public help center and automated support (FIN agent).

**Daniel Lopes:** For support context, I added activity feeds to the admin panel showing page views and user events (workspace switches, etc.), so you can understand what a user did when they reach out. We have workflow execution cleanup shipping today: cancel runs over 4 hours, purge records over 30 days. The one gap: no notification from workflows back to the app on failure, so stuck processes won't alert us. We'll address that in a follow-up.

**Daniel Lopes:** All workflows run in an isolated `checkthat` namespace on Temporal. The deployment on Render includes three services: API, worker, and Redis. The worker autoscales and is handling the probing load well. The CPU is warming under load, so I need to check with Render support on CPU probing configuration.

**Jose Farias:** Great work on that. Using Output.ai will be excellent. I've been working on tying probing cadence to pricing tiers and paused that to focus on launch. The backfill strategy is key: we're splitting backfill into its own worker isolated from core app operations (webhooks, Ahoy events, etc.). This lets us scale backfill independently.

**Jose Farias:** When a user onboards, we backfill the last 7 days in a critical queue (required before they can use the app). All older data goes in a low-priority queue. If backfills get slow, we increase workers. If we see replication lag or database contention from high write volume, we decrease workers or upgrade the database. This is a pragmatic tradeoff: slower backfills for new users to keep the core app stable.

**Jose Farias:** The 7-day critical backfill is per workspace, so even large Business plan accounts don't block others. If we go viral, that's a great problem—we have the levers to respond. My recommendations: monitor for slow backfills, replication lag, and database contention. Adjust worker count or database tier accordingly. I'm wrapping up the backfill worker separation and will resume work on tying probing cadence to pricing tiers.

**Jose Farias:** One note on feedback: as we launch, the whole team will get feature requests and questions. That's normal and healthy. Some will be phrased as "why didn't you just do this?" We did a ton of work to get here. Let's take feedback one at a time and make the people that matter most happy.

**Stevie Kim:** In terms of priorities, we have some P1 polish tickets but nothing more critical than onboarding and performance. The team did a great job fixing blank chart issues, making metrics more intuitive. There's always more polish possible, but we're in a solid position.

**Leonardo Carpenedo Steffen:** I noticed we don't have a help page. While testing, I couldn't find any documentation for users.

**Daniel Lopes:** Intercom will cover support initially. Then we build a public help center. The knowledge base I set up is a foundation for both. After launch, next week or the following one, we can turn on the public help center.

**Stevie Kim:** There's also the Learning Center and Masterclass that Marcel and Jason are working on—those are more product marketing. But we need a practical help center explaining how metrics work and how probing works. I've talked with Nigel who has good context on common user questions. We should review the internal Intercom KB and extract content for the public help center.

**Daniel Lopes:** We need a support guidelines doc so everyone answers consistently. If we can identify competitors or spam accounts in the session data, we adjust our transparency level accordingly. For legitimate customers, be as transparent as they need.

**Daniel Lopes:** Also, due to workflow execution cleanup: Daniel to ship code that cancels runs >4 hours and purges records >30 days. The workflow failure notification gap is a known issue for follow-up.

**Stevie Kim:** Thanks, everybody. Appreciate you all working through this. I think we're in a really strong position for launch.
