# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-04
time: 15:59 UTC
duration: 29 minutes
organizer: Stevie Kim (GrowthX)
participants: Stevie Kim (GrowthX), Jose Farias (GrowthX), Pedro Steimbruch (GrowthX), Estevão Mascarenhas (GrowthX), Leonardo Carpenedo Steffen (GrowthX), Jason Gong (GrowthX)
fathom_recording_id: 119685426
fathom_url: https://fathom.video/calls/554488514
share_url: https://fathom.video/share/KrDK8Tya6MQHxyQ6FYjEsjYudP9FtLtx
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

The CheckThat team conducted a final launch readiness review before the soft launch. The primary blocker—a "Generating Context" workflow stall (CHG698)—will be fixed immediately by Pedro, and the team decided to proceed with the soft launch to trusted customers today. Teams are monitoring PostHog and Intercom for friction points while Estevão completes onboarding polish and Clerk email restrictions.

---

## Context

This was the CheckThat launch team's final readiness meeting before going live. The 6-person GrowthX engineering team (led by Stevie Kim, the product lead) met to confirm they could launch today. CheckThat is GrowthX's strategic software bet—an AI visibility index for B2B that generates competitive research at scale. The soft launch targets friendly customers who understand the product is actively being polished, with a hard launch to follow.

---

## Relevance

**CheckThat Launch**
- Critical blocker (CHG698) identified in onboarding workflow and will be fixed today by Pedro before launch
- Soft launch to trusted customers proceeding today; hard launch follows after initial user feedback
- PostHog monitoring for rage-clicking and friction points during onboarding; Intercom monitored for support issues

**Product Development**
- Onboarding polish (UI/UX refinement of brand selection, subcategory selection, backfill steps) on track to complete in hours
- Clerk sign-up restrictions (personal email domain blocklist, single sub-email per address) required before launch
- Prompt backfill debouncing (5-minute window from first change) deployed to prevent system overload during active prompt editing

**Backlog & Priorities**
- Ticket #687 (subcategory and competitor cap limits) will follow immediately after onboarding polish
- Ticket #657 (brand data quality—detecting empty profiles and mismatched names) deprioritized during launch window, will resume post-launch
- Database documentation PR ready for merge; webhook fix PR pending merge after probe window

---

## Overview

- **Launch Blocker:** A critical bug (`CHG698`) prevents new users from completing onboarding by stalling on the "Generating Context" page.
- **Immediate Fix:** Pedro will investigate and fix `CHG698` immediately after the call to unblock the launch.
- **Launch Plan:** The soft launch will proceed today, starting with trusted customers who understand the product is in active development.
- **User Monitoring:** Stevie will use PostHog to monitor user behavior for friction points (e.g., rage-clicking) caused by the prompt backfill debouncing.

---

## Key Topics

### Onboarding Blocker: "Generating Context" Page

  - **Problem:** The onboarding workflow stalls on the "Generating Context" page, preventing users from proceeding.
  - **Impact:** Blocks all new users, including internal customers, from accessing the product.
  - **Root Cause Investigation:**
      - **Hypothesis 1:** Webhook failures related to Cloudflare.
      - **Hypothesis 2:** Issues with the new `output workflows repository`.
      - **Initial Check:** Stevie found no failed Temporal workflows in the `output` service.
  - **Rejected Workaround:** Allowing manual context entry was rejected due to a race condition where the automated workflow could overwrite user data.

### Launch Strategy & User Monitoring

  - **Decision:** Proceed with the soft launch today, targeting trusted customers.
  - **Rationale:** Prioritize getting user feedback over delaying for final polish.
  - **Monitoring Plan:**
      - **Intercom:** Leonardo will monitor for support requests.
      - **PostHog:** Stevie will analyze user recordings for behavior patterns (e.g., rage-clicking) to identify friction points.

### Pre-Launch Tasks

  - **Onboarding Polish:** Estevão to complete UI/UX improvements for the onboarding flow.
  - **Clerk Email Restrictions:** Estevão to implement two sign-up restrictions:
      - **Personal Emails:** Block common domains (e.g., Gmail, Outlook) using a blocklist.
      - **Sub-addresses:** Limit usage of email sub-addresses (`+test`) to a single sign-up per user.
  - **Prompt Backfill Debouncing:** Jose implemented a 5-minute debounce on backfills triggered by prompt changes to prevent system overload.
      - **Mechanism:** The timer starts on the *first* change in a session; subsequent changes within 5 minutes are ignored.
      - **Rationale:** This approach is simpler to implement and avoids user confusion compared to a "wait 5 minutes after the *latest* change" model.

### Post-Launch Priorities

  - **Ticket \#687 (Subcategory/Competitor Cap):** Estevão will implement this after completing the onboarding polish.
  - **Ticket \#657 (Flagging Bad Brands):** Pedro paused work on this to prioritize the `CHG698` blocker.
      - **Goal:** Automatically detect and flag brands with empty profiles or mismatched names to ensure data quality.
      - **Proposed Action:** Move flagged brands to "private" and enable admin filtering for review.

---

## Decisions & Commitments

- **DECIDED:** Proceed with soft launch to trusted customers today, targeting those with good relationships who understand the product is in active development.
- **DECIDED:** Timebox the CHG698 fix to 15-30 minutes immediately after the call; if complexity is unclear by then, evaluate workarounds.
- **DECIDED:** Implement 5-minute debounce on prompt backfill (from first change in session) rather than "wait 5 minutes after latest change" to simplify implementation and avoid user confusion.
- **COMMITTED:** Stevie will monitor PostHog user recordings for friction points (rage-clicking, navigation patterns) during soft launch.
- **COMMITTED:** Leonardo will actively monitor Intercom for support issues and user feedback.

---

## Open Questions

- **Post-launch data quality strategy for Ticket #657:** Should flagged brands (with mismatched or empty profiles) be moved to "private" status, or managed differently? (Potential SEO implications if pages are already indexed.)
- **Webhook failures in production:** Are temporal workflow failures from Cloudflare issues or the new output workflows repository, or something else? (Pedro to investigate in production first.)

---

## Action Items

**Pedro Steimbruch (GrowthX)**
- URGENT: Fix onboarding context-generation blocker (CHG698)—investigate temporal failures in production, check webhook status, determine root cause
- Send database documentation PR (updates done, ready to merge)
- Verify webhook fix PR is merged after probe window
- Implement brand-name checks on profile updates (Ticket #657); share admin flagging plan with team

**Jason Gong (GrowthX)**
- Send soft-launch invitations to trusted/friendly customers today

**Leonardo Carpenedo Steffen (GrowthX)**
- Monitor Intercom actively for user support requests and feedback
- Reschedule 1:1 meetings with Stevie and Estevão as needed

**Estevão Mascarenhas (GrowthX)**
- Complete onboarding UI/UX polish (brand selection, subcategory selection, backfill step)
- Implement Clerk email sign-up restrictions: block personal domains (Gmail, Yahoo, Outlook, etc.) and limit sub-email addresses (+test) to one per user
- Implement Ticket #687 (cap subcategories and competitors in onboarding) after polish/Clerk work

**Jose Farias (GrowthX)**
- Create Linear ticket for prompt-pool backfill debounce implementation (5-minute window from first change)
- Merge prompt-pool backfill PR this morning

**Stevie Kim (GrowthX)**
- Monitor PostHog user recordings for onboarding friction points and behavior patterns (e.g., rage-clicking after prompt changes)

---

## Transcript

**Jose Farias:** Good morning. Ready for launch. As ready as I can be.

**Leonardo Carpenedo Steffen:** How y'all doing today? That's good.

**Pedro Steimbruch:** All right.

**Stevie Kim:** Good morning, everyone. Let's get started. I'll take notes. If someone wants to share their screen, we can go through it together. I want to keep this page visible because we're both doing a soft launch to external customers and onboarding our internal users, and they need to see it. I noticed the onboarding workflow stalls on the "Generating Context" page—you can't cancel it or move on. It would be good to either allow manual context entry or stop the workflow from triggering during onboarding. I also want to monitor how people navigate the site.

**Pedro Steimbruch:** I started sharing.

**Jason Gong:** Quick question: is this ready for me to share with a few hundred people for the soft launch? Everyone wants to do it today.

**Leonardo Carpenedo Steffen:** There are 11 tickets in review I wanted to go through. I was out yesterday handling an emergency.

**Stevie Kim:** I don't think we need to block launch on those—I'm more concerned about the context page issue. As soon as we decide how to handle it, we're good, unless there's another blocker.

**Leonardo Carpenedo Steffen:** CHG698—context generation stalls. That's the one.

**Estevão Mascarenhas:** I checked this morning. Two unknown workspaces were created and everything worked—they picked competitors, subcategories—but neither had context generated. I was able to run the new output workflows repository locally but couldn't trigger it on my local app yet. There might also be webhook failures—I think Pedro was discussing that with Marcos. I hid the page because it wasn't working, but I can unhide it and remove the loading message if someone else investigates. I'm focused on polishing the onboarding UI first. The current state works, but it's below my quality bar.

**Jose Farias:** Before we remove the loading state, we need to think about the race condition. If the workflow completes, it overwrites user input. The main question is whether we can launch, and I think we can. Maybe we start with customers we have good relationships with who understand we're polishing final edges. If we delay for polish, we'll never ship. Instead of workarounds, let's fix the root issue and timebox it. If we find it's complex in 15-30 minutes, we can discuss alternatives. Can we launch if we timebox the fix right now?

**Pedro Steimbruch:** I can pick it up after the call. I'll first check production for temporal failures and Cloudflare webhook issues.

**Stevie Kim:** From my investigation last night, I didn't see failed temporal workflows from output.

**Jose Farias:** We should have at least a couple if there's an issue.

**Stevie Kim:** I'll let someone else take that investigation.

**Jose Farias:** Okay, Pedro—you're on the fix. Let us know if it's bigger than expected. By the way, I should create a ticket for the prompt backfill work.

**Stevie Kim:** We should keep a close eye on Intercom today—it'll be easy to forget with everything else.

**Leonardo Carpenedo Steffen:** I'll focus on Intercom monitoring. I'm tagged there already. I also have a bunch of meetings, so Stevie and Estevão, feel free to reschedule our 1:1s if needed.

**Estevão Mascarenhas:** I'll reschedule—I want to keep focused on polishing.

**Estevão Mascarenhas:** I should be done with onboarding polish in a few hours. It's mostly UI/UX improvements for brand selection through the backfill step. Then I'll implement two Clerk sign-up restrictions: blocking personal email domains (Gmail, Yahoo, Outlook, etc.) via a blocklist, and limiting email sub-addresses (like +test) to one sign-up per address. Both need to be in place before launch. After that, I'll pick up Ticket #687—capping subcategories and competitors.

**Stevie Kim:** Make sure we're not missing higher-priority items. We can review them, but Ticket #687 seems important to ship soon.

**Jose Farias:** I'll give my update. I've been working on the prompt pool backfill debouncing. When users change prompts, we backfill 60-90 days of data. Without debouncing, rapid changes overload the system. Currently, we debounce from the *first* change in a session—wait five minutes, then start backfilling. Any changes within that window are ignored. After five minutes, if there's another change, we wait another five minutes and backfill again. It's simpler than constantly pushing the timer back, and it's clearer for users. Five minutes is reasonable. I'll merge the PR this morning and create the ticket.

**Stevie Kim:** Five minutes is fine. I'll monitor PostHog for user behavior—rage-clicking, checking if data updated after prompt changes. If we get soft-launch signups today, we'll have real data before the hard launch.

**Pedro Steimbruch:** For the webhook investigation, instead of running output locally, let's check temporal failures in production first. I'll start there, then set up locally if needed. I also pushed minor fixes and updated database docs to match what we have. On Ticket #657—flagging brands with empty profiles or mismatched names—I'm checking if the brand name appears in the profile description or TLDR, and flagging on every profile update. If a check fails, we mark the brand private and allow filtering for admin review. Marcel reported seeing the Vercel brand showing HashiCorp's description, so detecting those mismatches is critical.

**Estevão Mascarenhas:** The brand name check is the most important. Those mismatches probably came from when we imported initial brands. I added paper trail logging recently, so if it happens again, we'll see what went wrong.

**Stevie Kim:** If there are mismatches, use your judgment—fix in the admin if it's easy, hide if you're swamped with something more critical. CHG698 takes absolute priority.

**Stevie Kim:** All right, anything else? Great work, everyone. I've only been here a couple months, and you've rocked this. Thanks.

**Leonardo Carpenedo Steffen:** Thank you.

**Jose Farias:** Take care.

**Pedro Steimbruch:** Bye.
