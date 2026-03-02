# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-03
time: 16:00 UTC
duration: 25 minutes
organizer: Stevie Kim (GrowthX)
participants: Stevie Kim (GrowthX), Jose Farias (GrowthX), Estevão Mascarenhas (GrowthX)
fathom_recording_id: 119304090
fathom_url: https://fathom.video/calls/552870636
share_url: https://fathom.video/share/qmyzG6sD22KxARmuvEjG81QJQtdFysUg
source: fathom
enriched_on: 2026-02-27 14:35 UTC
</metadata>

---

## Summary

Final pre-launch technical sync for CheckThat soft launch (Wednesday) and hard launch (Thursday). Team addressed critical chart backfill bug that occurs when users change prompts, confirmed billing integration is production-ready, and discussed onboarding QA findings. Jose prioritized backfill strategy exploration as the main blocker.

---

## Context

CheckThat is GrowthX's B2B AI visibility index software—currently in final prep for public launch. This meeting gathered the core CheckThat team (Estevão on billing/frontend, Jose on backend/infrastructure, Stevie on analytics/support) to work through remaining technical blockers and confirm launch readiness. The soft launch brings the public signup flow live while limiting external visibility; the hard launch goes to full public promotion. This was the last full-team sync before Wednesday's go-live.

---

## Relevance

**CheckThat Product**
- Critical chart backfill bug exposed data integrity risk and required prioritized fix before launch
- Stripe billing integration is production-ready with real credentials deploying before soft launch
- Onboarding bug (missing primary subcategorization) fixed; sign-up flow test pass underway
- Data warehouse gap identified as long-term infrastructure need post-launch

**Launch Execution**
- Soft launch confirmed for Wednesday; hard launch Thursday
- Estevão focused on replacing waitlist with sign-up flow and polishing onboarding before hard launch
- Analytics tracking needs improvement (PostHog lacks workspace-level aggregation; onboarding events missing workspace_id)
- Intercom ramped up for launch support with Jason added as teammate

---

## Overview

- **Launch Blocker:** A critical bug was found where overview charts fail to backfill after prompt changes. This creates a data integrity issue, as the charts become inaccurate.
- **Root Cause:** The backfill process strains the Postgres DB with high write volume, causing replication lag. This is the bottleneck, not S3 download speed or the lack of a data warehouse.
- **Launch Plan:** The soft launch is confirmed for Wednesday, with the hard launch on Thursday. Jose is prioritizing a fix for the backfill bug today.
- **Billing Ready:** The Stripe integration is complete, with production credentials ready for deployment.

---

## Key Topics

### Launch Blocker: Chart Backfilling

  - **Problem:** Overview charts do not backfill when a user changes their prompts (e.g., adding/removing from the library).
  - **Impact:** This causes data integrity issues, as the 60-day charts become inaccurate.
  - **Inconsistency:** The system *does* backfill charts when a user changes competitors, highlighting the bug.
  - **Root Cause:** The backfill process generates high write volume, straining the Postgres DB and causing replication lag.
      - **Note:** This is the bottleneck, not S3 download speed or the lack of a data warehouse. A data warehouse would speed up snapshots but not solve the DB strain.
  - **Proposed Solutions:**
      - **Safeguard:** Limit how often users can change prompts.
          - **Risk:** Frustrates users who make mistakes or need to quickly iterate on their prompt selection.
      - **Scheduled Backfill:** Run backfills once daily.
          - **Risk:** Data remains inaccurate for up to 24 hours.
      - **Launch & Monitor:** Deploy without a fix and address it post-launch.
          - **Risk:** High likelihood of user complaints, especially from data-intensive users (e.g., EMs).

### Launch Readiness & QA

  - **Billing (Estevão):**
      - Merged the upgrade flow backfilling feature.
      - Prepared a PR to deploy real Stripe production credentials.
          - **Note:** This will disable Sandbox testing. Erickson will use a real GrowthX card for final validation.
      - Added basic branding (logo) to the Stripe customer portal and checkout.
      - Next: Replace the waitlist with the sign-up flow and conduct a final test pass.
  - **Onboarding (Jose):**
      - Fixed a bug where the primary subcategorization was not saved during onboarding.
      - **Impact:** This caused the subcategory chart in the overview to appear empty.
  - **Analytics & Support (Stevie):**
      - **PostHog:** Discovered the current plan lacks aggregate functionality, preventing analysis by workspace (the billing unit).
      - **Intercom:** Ramping up on the new interface and added Jason as a teammate for launch support.
      - **Onboarding Events:** Confirmed onboarding events are tracked, but some events lack a `workspace_id`, limiting analysis.

---

## Action Items

**Estevão Mascarenhas (GrowthX)**
- Share draft PR link with Jose for review

**Jose Farias (GrowthX)**
- Explore backfill strategy options for prompt changes and report findings to team

---

## Transcript
**Stevie Kim:** So yeah, if anyone wants to share the linear board, that would be great. I'll take notes as usual. And anyone can start.

**Estevão Mascarenhas:** Yeah, I can share it. Can you guys see it?

**Jose Farias:** Yep, okay.

**Estevão Mascarenhas:** Yeah, I can start. So yesterday, I merged the upgrade flow backfilling—backfilling for when there is an upgrade on the account. Thanks to Jose for the review.

**Estevão Mascarenhas:** I have a draft PR with a delta that you left a comment about. I'm not sure that's the solution yet.

**Estevão Mascarenhas:** But if you want to take a look, I will work on that after I flip on the sign-up flow.

**Estevão Mascarenhas:** But yeah, just a heads up.

**Estevão Mascarenhas:** Yeah, so the billing.

**Estevão Mascarenhas:** So what I'm doing this morning, I prepared the PR that flips our credentials that we use in production.

**Estevão Mascarenhas:** For Stripe, the real mode.

**Estevão Mascarenhas:** So after it gets live, we're not going to be able to test in Sandbox anymore.

**Estevão Mascarenhas:** It's going to be real transactions.

**Estevão Mascarenhas:** I'm going to ping Erickson so he can use a test, growthx real card to test it.

**Estevão Mascarenhas:** I also did some branding on our customer portal and the Stripe checkout.

**Estevão Mascarenhas:** It's not so great, but at least there's our logo there.

**Estevão Mascarenhas:** Yeah, so Stripe, I think it's ready to go.

**Estevão Mascarenhas:** What I'm doing now is I'm preparing a PR to replace the waitlist with our sign-up onboarding flow.

**Estevão Mascarenhas:** I'm also doing a test pass on that.

**Estevão Mascarenhas:** So just to make sure that we don't have like any critical bug there.

**Estevão Mascarenhas:** So I'm going to test it before release.

**Estevão Mascarenhas:** And afterwards, I'm going to go back to the PR in draft that I mentioned, just mentioned.

**Estevão Mascarenhas:** And yeah, and perhaps fix any bugs.

**Estevão Mascarenhas:** And yeah, and go to polish the onboarding.

**Estevão Mascarenhas:** I have some things that I want you to do there before we do the hard launch.

**Estevão Mascarenhas:** Okay, I think that's it for me.

**Jose Farias:** Nice.

**Jose Farias:** Yeah, link me to the draft PR. I'm happy to take a look. I'll just go, if that sounds good.

**Jose Farias:** Yesterday, I was working on the cadence for probing, and then I switched focus because I felt the pressure of shipping, of launching, rather.

**Jose Farias:** So I started QAing some basic flows.

**Jose Farias:** I did find a bug in the onboarding, and I'm realizing now I misrepresented that this morning, Estevão.

**Jose Farias:** The bug was that going through onboarding, we did save the subcategorization, but we didn't mark it as primary. Everything looked like it worked because it had a subcategory, but if you went to the subcategory chart in the overview, it was empty because there was no primary subcategorization. It was a bit hidden but that was it. Fixed that.

**Jose Farias:** And now I found another thing.

**Jose Farias:** This is an annoying one because the overview charts, they're calculated based on the prompts that you're following from the library as well as your custom ones.

**Jose Farias:** Um, but when those change, do we backfill the full chart?

**Jose Farias:** We don't currently, but should we?

**Jose Farias:** Probably, I think.

**Jose Farias:** But that's...

**Stevie Kim:** Sorry, could you repeat this scenario?

**Stevie Kim:** I missed that.

**Jose Farias:** Yeah, so the charts in the overview page—we use the prompts that you're following to populate them, right? But when those change, do we recalculate the full chart over 60 days?

**Jose Farias:** I think probably, right?

**Stevie Kim:** I assumed we did, but it's not something you can really tell unless you remove a bunch of prompts at once and the removed prompts greatly impacted your scores.

**Stevie Kim:** If we can get to it, that would be awesome, but I'm not sure how noticeable it would be. I'd guess the EMs probably would notice, because they look at those numbers way closer than anyone else.

**Jose Farias:** Yeah.

**Stevie Kim:** There's that notification where we let users know things aren't calculated right away, but I guess that's just when prompts are added, not removed, right?

**Jose Farias:** We should be able to reuse that.

**Jose Farias:** But the thing is, there's, like, potential for really causing a strain on our infrastructure if they really want to, which is significantly changing your prompts multiple times in a short period of time.

**Jose Farias:** If you do that, we're recalculating 60 days every time you changed your prompts.

**Jose Farias:** So just try and just take it out loud about the possibilities here.

**Jose Farias:** We could just accept that risk and assume that no one's going to do.

**Jose Farias:** Or we could introduce a safeguard, being like, hey, you just changed your prompts.

**Jose Farias:** You need to hold off before you change anything again.

**Jose Farias:** I think that might be acceptable, actually.

**Jose Farias:** Sorry to interrupt.

**Stevie Kim:** The problem with that is it's super easy to make a mistake—like, I forgot to add a filter when bulk removing prompts and now I need to do it again. But I have to wait, and now the data isn't representative of my updated prompts.

**Stevie Kim:** I hesitate. I don't know if it's a threshold thing. Obviously, if they remove one prompt, we shouldn't recalculate everything.

**Stevie Kim:** That seems silly.

**Stevie Kim:** But if they're bulk removing prompts, it's going to be way off if we don't recalculate.

**Jose Farias:** Yep.

**Jose Farias:** You're right.

**Jose Farias:** Tricky one.

**Jose Farias:** Part of me wants to launch and see how much of an issue it is.

**Jose Farias:** But I don't know if collectively, as a company, we have the stomach to tolerate, like, people writing in angry that we didn't do it from the get-go, you know?

**Stevie Kim:** So we never recalculate the prompts?

**Jose Farias:** How it works currently is going forward. The daily captures of the chart will consider the new subset of prompts.

**Jose Farias:** And when you change it, so this is where it gets weird, because when you change your competitors, we do recalculate your subcategory chart fully.

**Jose Farias:** So it's weird that we do it when you change your competitors, but not when you change the prompts.

**Stevie Kim:** That's definitely weird. Yeah, that doesn't seem right.

**Stevie Kim:** I'm assuming the behavior will be: initially when someone onboards, they'll mess around with their prompts quite a bit. Then it tapers off and they do some pruning here and there. During that initial onboarding phase, there's a lot of prompt editing, removal, and adding.

**Stevie Kim:** But later, as they stick with the product, it's going to be more ad hoc.

**Jose Farias:** Yeah.

**Estevão Mascarenhas:** What if for certain kinds of backfilling, we do it just once a day—scheduled—so users can change prompts during the day and we backfill once per day? That could be a stopgap solution.

**Jose Farias:** That could be a good stopgap. Ultimately, we need to build out the data warehouse layer. The backfills when changing prompts aren't a full backfill, just a subset.

**Jose Farias:** For seven days, it could be 10-20 seconds, but we're doing 60. We queue seven on priority and 60 on low priority. If you do that multiple times because you're changing prompts repeatedly—

**Jose Farias:** We're putting real strain on infrastructure. The bottleneck is Postgres replication lag, not S3 download speed or lack of data warehouse—we're writing a ton of data at once. I don't think we'll arrive at an answer now, so I'll think offline.

**Jose Farias:** That's my priority today over the cadence work.

**Estevão Mascarenhas:** Yeah, that sounds good.

**Stevie Kim:** That sounds good. If someone removes a bunch of prompts at once, especially since we fill them from the library during onboarding—

**Stevie Kim:** If they say "these are trash" and remove all library prompts, keeping only custom ones, the charts are going to be pretty messed up.

**Estevão Mascarenhas:** Jose, how far are we from having a data warehouse? This feels like it'll be a recurring issue.

**Estevão Mascarenhas:** Even if it's not user-triggered, if we want to add a feature requiring backfill of all workspaces, we should address this. I was thinking Peter and I could focus on bug fixes post-launch while you focus on the data warehouse.

**Estevão Mascarenhas:** The earlier we have a data warehouse, the better—those problems will go away or at least get better.

**Jose Farias:** I agree. I'll include that in my explorations today. My intuition is that a data warehouse would speed up snapshotting, but the bottleneck here is DB strain, not speed. We'd still write to the datamart even with a warehouse. I'll explore and report back. Hopefully I'll find a way to handle this today and launch with it.

**Stevie Kim:** Thanks.

**Estevão Mascarenhas:** Oh, by the way, I moved this from P0 to P1 because it's not a blocker.

**Estevão Mascarenhas:** It's the basic research tweak that I need to do.

**Estevão Mascarenhas:** It's not a blocker, but I'm prioritizing it after what I have left already.

**Estevão Mascarenhas:** that sounds good.

**Stevie Kim:** Don't perform in it.

**Stevie Kim:** Yeah.

**Stevie Kim:** So my eye's better, so that's good.

**Stevie Kim:** Not completely, but I don't think...

**Stevie Kim:** Oh, improved.

**Stevie Kim:** So yeah, yesterday I did not get a lot done in the...

**Stevie Kim:** In the evening, I actually got a little bit of done just around the, just kind of checking out what we have in post-hog.

**Stevie Kim:** One issue we might hit: we didn't upgrade PostHog for aggregate functionality, so we can't look at things per workspace—only per user. Since we charge per workspace, not per user, this limits how we can analyze monetization and retention metrics. I'm ramping up on PostHog features and exploring the new interface. There's new stuff in search, sidebar, and admin, so I'm getting oriented.

**Stevie Kim:** I synced with Jason on analytics and launch. We're aligned on soft launch Wednesday and hard launch Thursday. Jason and Marcel joined the meeting that Daniel canceled and rescheduled it for tomorrow—that should be on the calendar.

**Stevie Kim:** I'm going to continue QA and analytics work. Intercom changed significantly since I last used it, so I'm ramping up on new functionality so we can hit the ground running. I added Jason as a teammate in Intercom to help with launch support.

**Estevão Mascarenhas:** I noticed we're not tracking events throughout onboarding. It would be cool to see performance and dropouts at each step. I won't do it now to avoid a moving target, but should we have a task?

**Stevie Kim:** We do. Jason brought it up a while back to Daniel, and onboarding events are tracked. But I'm working on making sure we have workspace-level tracking. Some current tracking isn't granular enough—like, you can look at a prompt event and have no idea what workspace it's from. There's work to do, but onboarding is captured.

**Estevão Mascarenhas:** Cool. Thanks.

**Jose Farias:** I think that's it. Thank you, team.

**Stevie Kim:** Thanks, y'all. See you tomorrow.
