# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-03
time: 16:00 UTC
duration: 25 minutes
organizer: Stevie Kim (GrowthX)
participants: Stevie Kim (GrowthX), Estevão Mascarenhas (GrowthX), Jose Farias (GrowthX), Marcel Santilli (CheckThat), Daniel Lopes (CheckThat), Jason Gong (GrowthX), Pedro Steimbruch (GrowthX), Leonardo Carpenedo Steffen (GrowthX)
fathom_recording_id: 119304090
fathom_url: https://fathom.video/calls/552870636
share_url: https://fathom.video/share/qmyzG6sD22KxARmuvEjG81QJQtdFysUg
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

The team confirmed soft launch readiness for Wednesday with hard launch Thursday, identifying one critical blocker: overview charts fail to backfill when users change prompts, causing data integrity issues. Jose will prioritize a fix strategy today while Estevão completes the Stripe production credentials deployment and sign-up flow replacement. Billing integration is production-ready, onboarding bugs are fixed, and analytics tracking is being finalized with PostHog aggregate analysis planned post-launch.

---

## Context

CheckThat is GrowthX's proprietary AI visibility index product launching this week. This meeting brings together the GrowthX product and engineering team (Stevie, Estevão, Jose, Leonardo, Pedro) and two CheckThat co-founders (Marcel Santilli, Daniel Lopes) for final launch coordination. The team is 72 hours from soft launch and addressing critical infrastructure and feature bugs discovered during final QA to ensure production readiness. This is a tactical sync focused on resolving blockers before go-live.

---

## Relevance

**Product Launch (CheckThat)**
- Soft launch confirmed for Wednesday 2026-02-05, hard launch Thursday 2026-02-06. Team is on track for both milestones pending prompt backfill fix.
- Critical data integrity issue identified with chart backfilling after prompt changes, affecting product reliability for data-intensive users (EMs).
- Chart backfill bug must be resolved today; failure to do so creates user-facing data accuracy problems at launch.

**Engineering & Infrastructure**
- Postgres database replication lag is the bottleneck preventing chart backfills, not S3 speed or lack of data warehouse. This is a core infrastructure constraint requiring strategic thinking.
- Backfill write volume strain will be a recurring issue; Jose flagged data warehouse as medium-term solution post-launch.
- Onboarding bugs fixed (primary subcategorization now persists correctly), unblocking go-live.

**Monetization & Billing**
- Stripe integration production-ready with real credentials deployed, enabling live transaction processing at launch.
- Sign-up flow replaces waitlist this week; Erickson conducting final card validation with real GrowthX card.

**Analytics & Operations**
- PostHog aggregate functionality missing from current plan, limiting per-workspace analysis (the billing unit). This is a post-launch priority for retention insights.
- Onboarding event tracking partially configured but lacks workspace_id tags in some events, reducing data granularity for cohort analysis.
- Intercom setup complete with Jason added as support teammate for launch day.

---

## Decisions & Commitments

**Launch Schedule (Confirmed)**
- Soft launch: Wednesday 2026-02-05
- Hard launch: Thursday 2026-02-06
- No delay unless prompt backfill issue cannot be resolved today

**Backfill Strategy (Assigned to Jose)**
- Jose to explore and present multiple options today: scheduled daily backfills, safeguards on frequency, or launch-and-monitor approach
- Team to decide on strategy by end of day based on feasibility and tradeoffs
- Jose will deliver recommendation on infrastructure load and user experience impact

**Stripe Production Deployment (Assigned to Estevão)**
- Real Stripe credentials PR ready for deployment
- Erickson to validate with real GrowthX card before go-live
- Sandbox testing will be disabled after deployment

**Sign-up Flow Replacement (Assigned to Estevão)**
- Replace waitlist with sign-up onboarding flow this week
- Complete full test pass before hard launch
- Address identified polish items post-soft launch if needed

---

## Open Questions

**Chart Backfill Strategy**
- What frequency of prompt changes would strain infrastructure under each proposed solution?
- How many users typically change prompts bulk-remove vs. single-remove during onboarding vs. steady-state?
- Would scheduled daily backfills be acceptable to EMs or other power users?

**Data Warehouse Timeline**
- How far out is a data warehouse solution and what other recurring issues might it solve beyond backfill?

**Analytics Granularity**
- What's the timeline to upgrade PostHog for aggregate functionality and tag all events with workspace_id?

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
- Share draft PR link with Jose
- Prepare PR to deploy real Stripe production credentials
- Replace waitlist with sign-up onboarding flow and conduct full test pass

**Jose Farias (GrowthX)**
- Explore backfill strategy options for prompt changes (scheduled daily, safeguards, launch-and-monitor)
- Present recommendation to team with infrastructure load and user experience tradeoffs
- Review Estevão's draft billing PR

---

## Transcript

**Stevie Kim (GrowthX):** Thank you.

**Stevie Kim:** Hey, sorry, was multitasking.

**Stevie Kim:** Hey.

**Estevão Mascarenhas (GrowthX):** Hey.

**Stevie Kim:** Yeah.

**Stevie Kim:** Everyone was...

**Stevie Kim:** So quiet, realize y'all were on.

**Stevie Kim:** So yeah, if anyone wants to share the linear board, that would be great.

**Stevie Kim:** I'll take notes as usual.

**Stevie Kim:** And anyone can start.

**Estevão Mascarenhas:** Yeah, I can share it.

**Estevão Mascarenhas:** Can you guys see it?

**Jose Farias (GrowthX):** Yep.

**Jose Farias:** Okay.

**Estevão Mascarenhas:** Yeah, I can start, I guess.

**Estevão Mascarenhas:** So yesterday, I merged this upgrade flow backfilling.

**Estevão Mascarenhas:** Sorry, backfilling for when there is an upgrade on the account.

**Estevão Mascarenhas:** Sorry, I'm a bit slow.

**Estevão Mascarenhas:** Slept poorly last night.

**Estevão Mascarenhas:** So yeah, thanks, Jose, for the review.

**Estevão Mascarenhas:** I have a draft PR.

**Estevão Mascarenhas:** I'm tired.

**Estevão Mascarenhas:** There's a delta you left a comment about.

**Estevão Mascarenhas:** I'm not sure.

**Estevão Mascarenhas:** It's in draft.

**Estevão Mascarenhas:** I'm not sure that's the solution.

**Estevão Mascarenhas:** But if you want to take a look, I will work on that after I flip on the sign-up flow.

**Estevão Mascarenhas:** But yeah, just a heads up.

**Estevão Mascarenhas:** Yeah, so the billing.

**Estevão Mascarenhas:** So what I'm doing this morning, I prepared the PR that flips our credentials that we use in production.

**Estevão Mascarenhas:** For Stripe, the real mode.

**Estevão Mascarenhas:** So after it goes live, we're not going to be able to test in Sandbox anymore.

**Estevão Mascarenhas:** It's going to be real transactions.

**Estevão Mascarenhas:** I'm going to ping Erickson so he can use a real GrowthX card to test it.

**Estevão Mascarenhas:** I also did some branding on our customer portal and the Stripe checkout.

**Estevão Mascarenhas:** It's not great, but at least there's our logo there.

**Estevão Mascarenhas:** Yeah, so Stripe, I think it's ready to go.

**Estevão Mascarenhas:** What I'm doing now is I'm preparing a PR to replace the waitlist with our sign-up onboarding flow.

**Estevão Mascarenhas:** I'm also doing a test pass on that.

**Estevão Mascarenhas:** So just to make sure that we don't have any critical bugs there.

**Estevão Mascarenhas:** I'm going to test it before release.

**Estevão Mascarenhas:** And afterwards, I'm going to go back to the draft PR I mentioned.

**Estevão Mascarenhas:** And yeah, perhaps fix any bugs.

**Estevão Mascarenhas:** And go to polish the onboarding.

**Estevão Mascarenhas:** I have some things I want to address there before we do the hard launch.

**Estevão Mascarenhas:** Okay, I think that's it for me.

**Jose Farias:** Nice.

**Jose Farias:** Yeah, link me to the draft PR.

**Jose Farias:** I'm happy to take a look.

**Jose Farias:** I'll just go, if that sounds good.

**Jose Farias:** Yesterday, I was working on the cadence for probing, and then I switched focus because I felt the pressure of launching.

**Jose Farias:** So I started QAing some basic flows.

**Jose Farias:** I did find a bug in the onboarding, and I'm realizing now I misrepresented that this morning, Estevão.

**Jose Farias:** The bug was that going through the onboarding, we did save the subcategorization, but we didn't mark it as primary.

**Jose Farias:** That was the bug.

**Jose Farias:** And so it looked like everything worked because it did have a subcategory, but if you went to the subcategory chart in the overview, it was empty because there's no primary subcategorization.

**Jose Farias:** They're regular ones, but not a primary.

**Jose Farias:** So that was a bug.

**Jose Farias:** It was a bit hidden, hard to tell, but in any case, that's what it was.

**Jose Farias:** Fixed that.

**Jose Farias:** And now I found another thing.

**Jose Farias:** This is an annoying one because the overview charts are calculated based on the prompts that you're following from the library as well as your custom ones.

**Jose Farias:** But when those change, do we backfill the full chart?

**Jose Farias:** We don't currently, but should we?

**Jose Farias:** Probably, I think.

**Stevie Kim:** Sorry, could you repeat this scenario?

**Stevie Kim:** I missed that.

**Jose Farias:** Yeah, so the charts in the overview page, we use the prompts that you're following to populate that, right?

**Jose Farias:** But when those change, for whatever reason, do we recalculate the full chart, the full 60 days?

**Jose Farias:** I think probably, right?

**Stevie Kim:** Yeah, yeah.

**Stevie Kim:** I actually, I mean, I assumed we did, but it's not something that's noticeable unless you remove a bunch of prompts at once. And it's not something that you can really tell unless the prompts you removed greatly impacted your scores.

**Stevie Kim:** So, yeah, if we can get to it, that would be awesome, but I don't know how noticeable it would be.

**Stevie Kim:** I've never noticed it, but I would guess the EMs probably would, because they really look at those numbers a lot closer than anyone else, even more than customers.

**Jose Farias:** Yeah.

**Stevie Kim:** But there's that notification where we let you know that things aren't calculated right away.

**Stevie Kim:** But I guess that's just with when they're added, not when they're removed, right?

**Jose Farias:** We should. So we should be able to reuse that.

**Jose Farias:** But the thing is, there's potential for really causing a strain on our infrastructure if users significantly change their prompts multiple times in a short period of time.

**Jose Farias:** If you do that, we're recalculating 60 days every time you change your prompts.

**Jose Farias:** So just thinking out loud about the possibilities here.

**Jose Farias:** We could just accept that risk and assume that no one's going to do it.

**Jose Farias:** Or we could introduce a safeguard, like: hey, you just changed your prompts, you need to hold off before you change anything again.

**Jose Farias:** I think that might be acceptable, actually.

**Stevie Kim:** Well, you know, I'm just thinking about how I've done things.

**Stevie Kim:** The problem with that is that it's super easy to just make a mistake.

**Stevie Kim:** Like, oh, I forgot to add this filter when I was bulk removing prompts.

**Stevie Kim:** And so I need to do it again.

**Stevie Kim:** And now I have to wait.

**Stevie Kim:** And so now the data isn't representative of my new prompt or the updated prompts.

**Stevie Kim:** I do hesitate.

**Stevie Kim:** I don't know if a threshold would work, because obviously, if they remove one prompt, we should not recalculate everything.

**Stevie Kim:** That seems silly.

**Stevie Kim:** But if they're bulk removing prompts, then it's going to be way off if we don't recalculate things.

**Jose Farias:** Yep.

**Jose Farias:** You're right.

**Jose Farias:** Tricky one.

**Jose Farias:** Part of me wants to launch and see how much of an issue it is.

**Jose Farias:** But I don't know if collectively, as a company, we have the stomach to tolerate people writing in angry that we didn't do it from the get-go.

**Stevie Kim:** So we never recalculate the prompts?

**Jose Farias:** How it works currently is going forward.

**Jose Farias:** The daily captures of the chart will consider the new subset of prompts.

**Jose Farias:** And when you change it, this is where it gets weird, because when you change your competitors, we do recalculate your subcategory chart fully.

**Jose Farias:** So it's weird that we do it when you change your competitors, but not when you change the prompts.

**Stevie Kim:** Yeah.

**Stevie Kim:** That's definitely weird.

**Stevie Kim:** Yeah, that doesn't seem right.

**Jose Farias:** I think what's happening is that initially, when someone onboards, they're going to mess around with their prompts quite a bit.

**Stevie Kim:** And then it's going to taper off and they might do some pruning here and there. But that initial onboarding phase, however long that lasts, is where they get their workspace and data to where it's most valuable for them.

**Stevie Kim:** So maybe for the first couple of weeks that someone onboards, there might be a lot of prompt editing, removal, and adding.

**Stevie Kim:** But I think later on, as they stick with a product, it's going to be more ad hoc.

**Stevie Kim:** That's my guess.

**Jose Farias:** Yeah.

**Estevão Mascarenhas:** What if, for certain kinds of backfilling, we just do it once a day, scheduled? So the user can change the prompts around during the day and at some point, we backfill once per day. Just thinking if that could solve it for now.

**Jose Farias:** That could be a good stopgap solution.

**Jose Farias:** I think what we're getting at, ultimately, is that we need to build out the data warehouse layer.

**Jose Farias:** That's the reason snapshotting for seven days takes like 40 seconds.

**Jose Farias:** Well, not actually, sorry, I'm just thinking out loud here. The backfills that we would have to do when changing the prompts aren't a full backfill, it's just a subset of all the backfill.

**Jose Farias:** So say for seven days, it could take like 20 seconds, 10 seconds, but we're doing 60 days, right?

**Jose Farias:** So we're doing seven on a priority queue and then 60 on the low priority queue.

**Jose Farias:** And if you do that multiple times because you're switching prompts, we're putting a real strain on our infrastructure there. And it's not even because of the data warehouse. The bottleneck is not downloading from S3 necessarily. It's the replication lag. That's the problem. It's Postgres, because we're writing a ton of data at once.

**Jose Farias:** Okay, I don't think we're going to arrive at an answer right now. I'll do some thinking offline.

**Jose Farias:** And yeah, I guess I'll make that my priority today, more than the cadence stuff.

**Estevão Mascarenhas:** Yeah, that sounds good.

**Stevie Kim:** Yeah, sorry, go ahead.

**Stevie Kim:** Oh, I was just going to say that sounds good, just because, as I said, like, if someone does remove a bunch of prompts at once, especially because we fill them from the library during onboarding. In the subcategory, like if they're like, oh, these are trash, and they remove all of them and just keep other custom ones, then yeah, the charts are going to be pretty messed up.

**Estevão Mascarenhas:** I was going to ask, Jose, how far do you think we are from having a data warehouse?

**Estevão Mascarenhas:** Because I think this is going to be a recurring issue.

**Estevão Mascarenhas:** Like, yeah, even if it's not user triggered, if you want to add some feature that requires backfilling all the workspaces, I mean, I think we should start doing that.

**Estevão Mascarenhas:** I was thinking if maybe Peter and I can focus on bug fixes post-launch, and you get focused on the data warehouse.

**Estevão Mascarenhas:** I'm not sure, like, it feels to me that the earlier we have a data warehouse, the best. All those problems will go away, or get better, at least.

**Jose Farias:** I agree with you.

**Jose Farias:** Maybe I'll just include that in my explorations from today.

**Jose Farias:** My intuition about this problem specifically is that it's not the speed.

**Jose Farias:** So having a data warehouse would speed up the snapshotting.

**Jose Farias:** That's what we would gain.

**Jose Farias:** But the speed is not the problem here.

**Jose Farias:** It's the strain on the DB.

**Jose Farias:** Which would happen independently, like whether we have a warehouse or not.

**Jose Farias:** We still have to write to the datamart, which is the snapshots.

**Jose Farias:** I'll explore.

**Jose Farias:** I'll let you all know what I land on.

**Jose Farias:** Hopefully, maybe I'll find a way to do this today and we can launch with this.

**Jose Farias:** Okay.

**Jose Farias:** Yeah.

**Jose Farias:** I guess that's me. Unanswered questions. Hopefully I'll answer them today.

**Stevie Kim:** Thanks.

**Estevão Mascarenhas:** Oh, by the way, I moved this from P0 to P1 because it's not a blocker.

**Estevão Mascarenhas:** It's the basic research tweak that I need to do.

**Estevão Mascarenhas:** It's not a blocker, but I'm prioritizing it after what I have left already.

**Stevie Kim:** Yeah, that sounds good.

**Stevie Kim:** So my eye's better, so that's good.

**Stevie Kim:** Not completely, but improved.

**Stevie Kim:** So yeah, yesterday I did not get a lot done in the evening. I actually got a little bit done just checking out what we have in PostHog.

**Stevie Kim:** And yeah, I think like one of the issues that we might run into is that we didn't upgrade to get the aggregate functionality.

**Stevie Kim:** So you can't really look at things per workspace. It's per user, and we don't charge per user.

**Stevie Kim:** And so all the product analytics that I'm going to be looking at are going to be tied to monetization and the retention metrics that will need to be grouped.

**Stevie Kim:** So I think there might be a way to do it without upgrading, but anyway.

**Stevie Kim:** So I'm just kind of looking into what we have there and setting some stuff up. I haven't used these fancy marketing tools. I've always just had to query BigQuery or Postgres or Snowflake directly and build things from scratch.

**Stevie Kim:** So it's ramping up on these tools.

**Stevie Kim:** It's kind of fun.

**Stevie Kim:** It makes things a lot easier.

**Stevie Kim:** But I'm also continually going through and queuing. Like I'm constantly seeing new things that have popped up, like the search and the sidebar.

**Stevie Kim:** Oh, that's new, you know.

**Stevie Kim:** So kind of looking at that and there's some stuff in the admin that's new.

**Stevie Kim:** So I'm just making sure that I'm at least aware of things that maybe I didn't look at and make sure everything's functioning.

**Stevie Kim:** I synced with Jason yesterday to talk a little bit about the analytics and launch and everything.

**Stevie Kim:** So we're good for soft launch on Wednesday and hard launch on Thursday.

**Stevie Kim:** We're aligned on that.

**Stevie Kim:** Jason and Marcel actually joined that meeting yesterday that Daniel said he canceled.

**Stevie Kim:** So I think they rescheduled it for tomorrow.

**Stevie Kim:** So that will be on your calendar.

**Stevie Kim:** And I'm just going to continue doing QA and analytics and make sure that I'm getting more comfortable with Intercom. It's changed significantly since I last used it.

**Stevie Kim:** So I'm just going to try to get more comfortable with the new functionality and layout.

**Stevie Kim:** So we can hit the ground running.

**Stevie Kim:** I added Jason also as a teammate in Intercom because he was expecting to help a lot, especially with launch support, which is great.

**Stevie Kim:** So that's it for me.

**Stevie Kim:** Anything else?

**Estevão Mascarenhas:** Hey, Stevie, just a question.

**Estevão Mascarenhas:** I noticed that I don't think we are tracking events throughout the onboarding, and I think it would be cool to see how it's performing, like if there's a dropout in some step or something like that.

**Estevão Mascarenhas:** I'm not going to do it right now because I would test it, so we don't have a moving target for that, but I'm just wondering if we should have a task at least for that.

**Stevie Kim:** We do.

**Stevie Kim:** Jason brought it up a while back to Daniel.

**Stevie Kim:** And so, yeah, onboarding is in there.

**Stevie Kim:** And then, yeah, I'm actually looking to make sure that we have events around identifying which workspace, because some of the tracking that we have isn't quite granular enough or it doesn't tie things together.

**Stevie Kim:** Like you can look at a prompt event and you have no idea what workspace they're in.

**Stevie Kim:** So I think there's some work that needs to be done, but yeah, onboarding is in there.

**Estevão Mascarenhas:** Cool.

**Estevão Mascarenhas:** Okay.

**Estevão Mascarenhas:** Thanks.

**Jose Farias:** I think that's it.

**Estevão Mascarenhas:** Bye.

**Stevie Kim:** Thanks, y'all.

**Jose Farias:** All right.

**Jose Farias:** Thank you, team.

**Stevie Kim:** Bye.

**Stevie Kim:** See you tomorrow.

**Jose Farias:** Bye-bye.

**Jose Farias:** See you.
