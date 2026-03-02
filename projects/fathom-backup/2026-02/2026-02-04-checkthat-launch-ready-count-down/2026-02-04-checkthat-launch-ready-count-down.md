# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-04
time: 15:59 UTC
duration: 29 minutes
organizer: Stevie Kim
participants: Jason Gong, Pedro Steimbruch, Jose Farias, Estevão Mascarenhas, Leonardo Carpenedo Steffen, Stevie Kim
fathom_recording_id: 119685426
fathom_url: https://fathom.video/calls/554488514
share_url: https://fathom.video/share/KrDK8Tya6MQHxyQ6FYjEsjYudP9FtLtx
source: fathom
enriched_on: 2026-02-27 14:33 UTC
</metadata>

---

## Summary

Team cleared CheckThat for soft launch today, accepting known friction points (UI polish, onboarding blocker CHG698) with the understanding that getting real user feedback matters more than final polish before public launch. Pedro will immediately debug and fix the context-generation workflow; team will monitor user behavior through PostHog and Intercom while Estevão handles pre-launch sign-up restrictions.

---

## Context

CheckThat is preparing for soft launch to trusted customers. The team discovered a critical onboarding issue (CHG698) where users get stuck on the "Generating Context" page when the automated workflow fails to complete. Rather than delay for investigation, the team decided to proceed with launch targeting friendly customers who understand the product is in active development, prioritizing real-world feedback over perfect polish. This reflects CheckThat's launch philosophy: shipping fast with early adopters allows the team to iterate on actual user behavior data instead of hypothetical edge cases. Parallel to launch, the team is implementing pre-launch safeguards (email restrictions, subcategory caps) and monitoring infrastructure (PostHog for session replay, Intercom for support requests) to catch friction early.

---

## Relevance

- **Launch & Go-to-Market:** Soft launch decision, target audience selection, and timing for CheckThat's first external customer cohort.
- **Engineering (CheckThat):** Critical blocker fix (CHG698), workflow debugging, webhook verification, onboarding UX polish, sign-up restrictions.
- **Product (CheckThat):** Onboarding experience, data validation logic (flagging bad brands), sub-address email handling, competitor/subcategory caps.
- **Analytics & Monitoring:** PostHog setup for user session recording, Intercom monitoring, rage-click detection, friction point identification.
- **Architecture:** Temporal workflow failures, Cloudflare webhook integration, output workflows repository, prompt backfill debouncing logic.

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

## Action Items

**Pedro Steimbruch** (GrowthX Engineering)
- Fix onboarding context-generation (CHG698); unhide page, remove loading, add manual-entry note
- Send DB docs PR; verify webhooks
- Implement brand-name checks on profile updates; share admin flagging plan

**Jason Gong** (GrowthX Go-to-Market)
- Send soft-launch invites to friendly customers

**Leonardo Carpenedo Steffen** (GrowthX Support/Product)
- Monitor Intercom for user issues
- Reschedule 1:1s with Stevie and Estevão

**Estevão Mascarenhas** (GrowthX Frontend/Product)
- Restrict Clerk sign-ups: block personal domains; allow 1 sub-email per address
- Cap subcategories and competitors in onboarding

**Jose Farias** (GrowthX Backend/Architecture)
- Create ticket re: prompt-pool backfill debounce
- Merge prompt-pool backfill changes

---

## Transcript

**Stevie Kim:** I think top of mind for me is the onboarding issue with the workflow. You can't cancel it, you can't move on. I don't want to hide that page because we're doing the soft launch externally to specific users, but we're also onboarding our internal customers. I want to make sure that page is visible because it's filled out for our internal customers. If there's a way to allow manual creation or have the workflow not kick off during onboarding, which I thought we had done last week, but it's still kicking off and just not finishing or doing anything.

**Jason Gong:** Is this ready for me to share with like a few hundred people now for a soft launch? Because I know everyone wants to do that today.

**Stevie Kim:** We're good as soon as we decide and implement how we're going to work around that issue. Unless someone else knows something outstanding that is a blocker.

**Leonardo Carpenedo Steffen:** CHG698 — context generation tanks, definitely. And it is in to-do.

**Estevão Mascarenhas:** I checked this morning on production. We had two workspaces created by people we don't know, and they did everything like picking competitors and subcategories, everything worked well, but they didn't have the context. This morning I was able to run the new output workflows repository that Daniel migrated, but I could not trigger it yet on my local app. There was a thread where Pedro was discussing with Marcos that we were getting some webhook failures, so it could also be that. I hid that page because it wasn't working, but I agree we can show it and maybe just remove the loading message for now. I'm trying to get some polishing work done because I want to finish today before tomorrow. The current state works but it's not at my minimal design quality bar.

**Jose Farias:** The main point to clarify is whether we can launch, and I think we can. Before making any rash decisions, if we remove the loading state, do we not run into a race condition where if the workflow completes, it'll overwrite whatever the user inputted? So I think the thing to do is try to rush the fix. Let's timebox it. Right after the call, let's try to fix it. If we can't pick up on what the complexity is going to be in the next 15 to 30 minutes, then we can start talking about workarounds.

**Pedro Steimbruch:** I could pick it up after the call.

**Jose Farias:** Thanks, Pedro. Jason is going, so everyone's aware we are going to start getting users.

**Stevie Kim:** Just that we should keep our eye on Intercom. It's going to be easy to forget with all the other things we're trying to juggle.

**Leonardo Carpenedo Steffen:** I'll definitely keep my focus there today. I'm tagged and I added a tag for me, so I'm going to be taking a look. I have a bunch of meetings today, so if any of you want to reschedule your one-on-ones, just feel free to drop a note.

**Estevão Mascarenhas:** I should be done with the polishing in a few hours. It's mostly on the start of the onboarding, like when you pick a brand and go all the way to the backfill step. The brand part is almost done. After that, I'm going to restrict the emails in Clerk. Two restrictions: personal emails (block common domains like Gmail, Outlook, Yahoo) and sub-email addresses (allow only one sub-address per email like firstname+test@gmail.com). Just before launch we need to put that in place. After that, I can cap subcategories and competitors in onboarding if we have bandwidth.

**Jose Farias:** I think capping subcategories and competitors is probably worth shipping soon.

**Estevão Mascarenhas:** I can take it. Pedro offered but it conflicts with changes I'm doing in onboarding, so I'll pick it up and get it done.

**Jose Farias:** I'm working on the prompt pool changes for visibility prompts. Our worry was that if you made a ton of changes in quick succession, you'd overwhelm our system because we'd be backfilling 60 to 90 days for every single change. We're doing debouncing: from the first change, we wait five minutes before we actually start backfilling. When you make the first change, you can keep making changes for five minutes, then the backfill starts and we update the data. If you make another change after those five minutes, we backfill again in five minutes. Does that sound good? Is five minutes too much?

**Pedro Steimbruch:** Wouldn't it be better to wait five minutes after the latest change?

**Jose Farias:** I think I'll hold off on that because users could be confused. Why isn't this updating ever? And they keep making changes, not realizing they're pushing the backfill further in the future. Let's accept that we might be backfilling every five minutes for a certain workspace. Doing it every five minutes, I think it's fine. It's doing it every second that would bring the system down.

**Stevie Kim:** I don't think five minutes is too long. I'll keep my eyes on PostHog. I'll keep an eye on user recordings to see if they're clicking a bunch, rage-clicking, going from prompts to the overview to check if the data has changed. If people sign up from the soft launch today, we'll get a little bit of data to make any quick changes before the hard launch.

**Jose Farias:** I did ship the debouncing. I am yet to ship the actual backfilling when the prompt pool changes, but I have the PR ready. I'll merge it this morning.

**Jose Farias:** Instead of trying to run output locally, let's look at the temporal changes in production or the failures, and see if there's any missing webhooks there.

**Pedro Steimbruch:** Today I was able to push a few minor fixes to production. I double-checked on Monday the metrics with Marcel, and the way we have the database is what he wants. I changed the docs to reflect what we have in the codebase. I have this one ready to go. I will send it now and see how the webhooks work after that. I was also working on detecting brands with empty profiles or mismatched names. The way I'm thinking about it: do Navy checks to see if the brand name is in the TLDR or in the profile description, and do these checks on every profile update. If one check fails — if there's no brand name in the profile description or TLDR, or every profile field is empty — then we send the brand to private and allow filtering for flagged brands so we can manage them. I'm not sure if that's the ideal UX, or even if moving brands to private would be an issue with SEO if that brand's page is already indexed.

**Estevão Mascarenhas:** I think the second part is the most important because Marcel reported that the Vercel brand was showing something totally different. It was showing the HashiCorp description.

**Stevie Kim:** It seems like that's the only way that would actually happen. The workflows are pretty good about doing it. There are some empty ones, which I caught a couple manually. It's trying to future-proof those types of errors. If it's easy to fix, go in the admin and fix it. If it's something way more important, go ahead and hide it. Use your best judgment.

**Estevão Mascarenhas:** I added the paper trail to brand and brand profile a couple of days ago. So if it happens again, we should take a look at what's going on.

**Pedro Steimbruch:** I'll come up with something and share it along with how it will work on the admin side to manage the flagged brands. Then I will work on the context generation, which we were discussing.

**Stevie Kim:** Can we prioritize that one? This one is a lot more critical.

**Pedro Steimbruch:** Awesome, I will start on it right after the call.

**Stevie Kim:** You guys have rocked everything. I've only been on this for a couple of months, but you guys have done amazing work. Feel really good about it.

**Leonardo Carpenedo Steffen:** Thank you.

**Jose Farias:** Take care.
