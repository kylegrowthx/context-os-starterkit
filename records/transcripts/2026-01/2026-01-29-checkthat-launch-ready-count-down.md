# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-01-29
time: 16:00 UTC
duration: 20 minutes
organizer: stevie@growthx.ai
source: fathom
fathom_recording_id: 118190437
fathom_url: https://fathom.video/calls/548093505
share_url: https://fathom.video/share/sDHwaRvr-J4mqzDk-Ycopv8xF58u-ycq
enriched_on: 2026-02-28 12:00 UTC
participants:
  - name: Marcel Santilli
    email: marcel@growthxlabs.com
    affiliation: GrowthX (CEO)
    spoke: false
  - name: Daniel Lopes
    email: daniel@growthxlabs.com
    affiliation: GrowthX (External)
    spoke: false
  - name: Jason Gong
    email: jason@growthx.ai
    affiliation: GrowthX
    spoke: false
  - name: Pedro Steimbruch
    email: pedro@growthx.ai
    affiliation: CheckThat (Backend Engineer)
    spoke: true
  - name: Jose Farias
    email: jose@growthx.ai
    affiliation: CheckThat (Backend Engineer)
    spoke: true
  - name: Estevão Mascarenhas
    email: estevao@growthx.ai
    affiliation: CheckThat (Frontend Engineer)
    spoke: true
  - name: Leonardo Carpenedo Steffen
    email: leonardo@growthx.ai
    affiliation: CheckThat (QA Lead)
    spoke: true
  - name: Stevie Kim
    email: stevie@growthx.ai
    affiliation: CheckThat (Product Lead)
    spoke: true
</metadata>

---

## Summary

The CheckThat team confirmed launch readiness with only 6 remaining "Instabilized" tickets on the Linear board, all on track for closure. Key fixes in progress include onboarding stability (1-minute timeout for brand research, catalog lookup bypass), QA coverage, and investigation of a Sources page performance bottleneck related to the `sortable_pointers` table. One unresolved product decision—default Unlimited vs. Pro plan for new customers—is not a launch blocker and will be discussed internally.

---

## Context

CheckThat is shipping soon. This meeting occurred during the final countdown to launch, with the team focused on resolving remaining blockers and ensuring stability. The team has been iterating rapidly on the onboarding flow, performance optimization, and QA—particularly around billing integration, which is critical for go-live. The meeting also flagged a disagreement on pricing strategy (Unlimited vs. Pro as default), which needs alignment with leadership but is not a launch blocker since customers will be managed by GrowthX EMs initially.

---

## Relevance

**Product Readiness**
- Final QA pass confirms onboarding, billing, and core product flows are stable
- Only 6 remaining "Instabilized" tickets, all assigned and in progress
- Linear board tracking confirms alignment on priority and task ownership

**Engineering Decisions**
- Onboarding stability strategy: graceful degradation (timeout + manual fallback) over complex state tracking
- Group trend lines use aggregation from individual snapshots to avoid infrastructure strain
- Sources page performance fix options: query optimization vs. data purging (both viable)

**Business/GTM**
- Default plan decision (Unlimited vs. Pro) requires alignment with Bridget and Marcel before launch
- EMs will manage customer tier selection, reducing direct customer complexity
- Pricing strategy affects customer experience but not launch timing

**Technical Debt & Future Work**
- Workflow failure handling needs generalization beyond onboarding use case
- `sortable_pointers` table design may need revisiting as platform scales
- SEO regression fixes indicate potential quality gaps from recent changes

---

## Overview

- **Launch Readiness:** The team is in good shape, with only 6 "Instabilized" tickets remaining on the Linear board.
- **Onboarding Fixes:** The brand research flow is being stabilized with a 1-minute timeout to unblock users and a fix for a bug where a catalog lookup prevents description updates.
- **Performance Bottleneck:** The "Sources" page is slow due to `GROUP BY` operations on text columns in the large `sortable_pointers` table; potential fixes include optimizing queries or purging old data.
- **Plan Disagreement:** Bridget opposes the default Unlimited plan for new customers, arguing the Pro plan is sufficient. Stevie will discuss this internally, but it is not a launch blocker.

---

## Key Topics

### Launch Readiness & Ticket Status

  - **Linear Board:** 6 tickets remain in "Instabilized."
  - **Pedro:**
      - **Deployed:** "Unified trend decimals"
      - **Next:** "Updates on the prompts page after we update a prompt"
      - **Resolved:** "Workspace cookie" bug (caused by a missing workspace ID in the `useSWR` key).
  - **Jose:**
      - **Deployed:** "Overview page subcategory charts fix" (required backfilling data with a new snapshot scope).
      - **In Progress:** "Group trend lines" (for prompts table).
          - **Strategy:** Aggregate totals from individual prompt snapshots, then average. This avoids creating a new snapshot type and straining infrastructure.
  - **Estevão:**
      - **Onboarding Fixes:**
          - **Brand Research Timeout:** If research fails after 1 min, users can proceed with empty categories to fill manually.
          - **Brand Description Bug:** A catalog lookup for a similar-named company (e.g., "branch" vs. "branch.io") prevents the new brand's description from being updated.
              - **Fix:** Skip the catalog lookup during onboarding if the user confirms it's a new company.
              - **Dependency:** This fix is on hold until Daniel migrates workflows to avoid conflicts.
      - **Other Tasks:**
          - Fix: Hide "Billing" menu item for workspaces without a subscription.
          - Pulled 2 SEO regression fixes from P1.
          - Next: Polish onboarding UI.
  - **Stevie & Leo:**
      - **Stevie:** Performing a final QA pass on areas with recent changes, including the billing flow.
      - **Leo:** Updating test plans and coordinating with Stevie.

### Performance Issue: Sources Page

  - **Problem:** The "Sources" page is slow.
  - **Root Cause:** The page uses `sortable_pointers` and requires `GROUP BY` operations on text columns (domain/URL) to aggregate data.
  - **Contributing Factor:** The `sortable_pointers` table is very large (3-4x the size of the `snapshots` table) because it captures multiple pointers per snapshot.
  - **Potential Solutions:**
      - Optimize the query.
      - Purge old data from the `sortable_pointers` table, as only the latest capture date is typically used.

### Product Decision: Default Plan

  - **Issue:** Bridget opposes the default Unlimited plan for new customers, arguing the Pro plan is sufficient.
  - **Context:** The decision was based on the assumption that EMs will manage the platform for customers, making the plan tier less critical for the customer's direct experience.
  - **Resolution:** Stevie will discuss this internally. It is not a launch blocker.

---

## Action Items

**Stevie Kim (CheckThat)**
- Sync w/ Marcel & Daniel re: default plan (Unlimited vs Pro)
- QA billing flow

**Jose Farias (CheckThat)**
- Ship grouped trend lines for Prompts Index (tags/personas)

**Estevão Mascarenhas (CheckThat)**
- Fix missing description bug (onboarding)
- Hide Billing menu for workspaces w/o Stripe subscription
- Fix 2 SEO regressions

**Leonardo Carpenedo Steffen (CheckThat)**
- Schedule afternoon sync w/ Stevie

**Pedro Steimbruch (CheckThat)**
- Investigate Sources page slowness (Sentry trace); check indexes, grouping, sortable pointers

---

## Transcript

**Leonardo Carpenedo Steffen:** Where are things going?

**Stevie Kim:** Yeah, let's get started. Someone can share their screen of the Linear board and we can go through the open tickets. I was seeing quite a few tickets move over the past few days. When I checked yesterday there were more instabilized tickets, but we've ripped through a lot since then. Looking at it now, I'm showing six instabilized.

**Pedro Steimbruch:** Yeah, you can see six here. So, I can start. I had a late start today with some errands to run. I pushed "Unified trend decimals" to production today. I also pushed a workspace competitor pin yesterday. Now I'm going to work on updates on the prompts page after we update a prompt, and then I'll just keep grabbing from the top.

**Stevie Kim:** Sounds good. Yeah, it looks like we're in good shape.

**Jose Farias:** Where's the workspace cookie one—where did that end up?

**Pedro Steimbruch:** I've solved that already.

**Jose Farias:** Oh, you did? When was that?

**Pedro Steimbruch:** It was a useSWR key missing the workspace ID, so it was using the cache. I deployed that yesterday or the day before.

**Jose Farias:** That makes sense. I ran into this yesterday morning, so it was probably before we deployed.

**Pedro Steimbruch:** Exactly.

**Jose Farias:** Good to know. So I can go. Sure. I'm just flagging something that might be worth noting. I don't think Bridget is a fan of our decision to have customers automatically on the Unlimited plan. She's been asking Marcel about this for a week and is still waiting to hear her confirmation.

**Stevie Kim:** Yeah, I'll try to coordinate because I get where she's coming from. I wasn't either, but that's kind of the assumption we made. I don't think it's something we really need to worry about too much because the EMs are the ones actually doing the work for the customers. Customers don't want to actually manage this thing—they view us to do that. So I don't think we have to be too concerned about it. But if we put them on the Pro plan, that would be more than sufficient. I'll talk to them about it.

**Jose Farias:** Thanks for flagging that. I mean, it just seems important to her, so probably worth keeping an eye on, but I think we can launch and figure it out later.

**Stevie Kim:** Right, yeah.

**Jose Farias:** So I'll talk about my tickets. Yesterday I shipped the overview page subcategory charts fix. I had to backfill some data. We now have a new snapshot scope we're using. For the group trend lines—if you group the prompts index table by tags or personas, we're now showing the trend lines for the group. I need to ship that. Our first iteration won't require a new kind of snapshot. What we're doing is capturing aggregated metrics in our brand performance snapshotables, but we're not capturing the raw counts. So what we're doing now is capturing the totals. When we want to show group performance, we use a tool to aggregate from the individual prompt performances and then average those out. That's what we'll use. I think that will be fast enough. The alternative is creating a new kind of snapshot, which is doable but puts unnecessary strain on our infrastructure. I'll try to avoid that. That's what's on my plate for today. I'm aiming to ship that soon. Marcel is demoing today, so I don't think this would break anything. I'll probably ship anyway, but just something to be aware of today.

**Stevie Kim:** After this, I'll just grab another ticket.

**Jose Farias:** And that's me.

**Estevão Mascarenhas:** Cool. So on my side, I was working on the brand step of the onboarding flow based on our discussion yesterday. What I did is now, if the basic research fails for some reason—like after a minute—I let the user proceed with onboarding. The categories are going to be empty and they'll have to pick those up manually. That was the simplest fix. What I was trying to do before was something more complex. It's tracking the workflow run status so we could have better visibility on that. It's on a branch here, but I think that's more complex. With Daniel migrating workflows, I wanted to hold that off for now. But I think we'll probably need this kind of handling of workflow failures for a lot of features we're going to build going forward. Maybe we can build something more agnostic that we can use in other features. I also found the missing description bug that Jose reported a few dailies ago. The basic research tries to look up existing brands in our database. So if I onboard a company called branch.io and we don't have that company with that domain in our database, it triggers the basic research. But the lookup found another company in our catalog called "branch" with a different domain because it's a different company. So we don't update the brand description in that scenario. What we need to do is when we run basic research during onboarding, we don't want that lookup anymore. Now when the user types a domain, I show a list of similar companies in our catalog. That lookup is already being done in the onboarding. So if the user says no, this is a different company, then the basic research should just research and we skip the lookup. I created an issue on P0, maybe it's a P1, but just to capture that. This needs to be done after Daniel migrates stuff, so I don't touch that. Right now what I'm doing is fixing a bug where we're showing the billing menu item for workspaces without a subscription. That breaks because there's no Stripe subscription for them to manage. I'll hide those for those workspaces. I pulled two SEO-related tasks from P1 because I think those are regressions, so those should be easy to fix. And afterwards, my plan is to polish a little bit more the onboarding UI and then pick something next if possible.

**Stevie Kim:** That's good. Yeah, so for me, I'd like to say I'm done with QA, but because we've done so many other tickets, I want to do another pass on a couple areas that we've changed a lot since I initially went through them. I've gone through everything except for billing. I know that's been gone through by a couple of other people, but I should probably still go through so I'm familiar with anything that's new or that I forgot about. So yeah, probably today I'll just go through the onboarding and the billing flow and see if I missed anything else. I feel pretty good about having gone through most scenarios. And that's pretty much it for me, except for answering questions and syncing and doing all that fun stuff.

**Leonardo Carpenedo Steffen:** Yeah, I'll be working on testing as well. I've got some other test plan updating and other activities that I paused. So we'll be taking care of that. And let's touch base this afternoon, Stevie.

**Stevie Kim:** Yeah, I think I have some time. I have a few other meetings today.

**Leonardo Carpenedo Steffen:** I'll look at your calendar.

**Stevie Kim:** Sounds good.

**Leonardo Carpenedo Steffen:** Thank you all.

**Jose Farias:** Real quick, something to flag. Pedro, this might be worth putting on your radar if you have the bandwidth. It's just that you work on this recently. Marcel just said that the sources page is a bit slow. Estevão linked a trace from Sentry pointing to the query. I think that might be worth a look. If I remember correctly, we're using sortable pointers there.

**Pedro Steimbruch:** Yeah, but sources are not a first-class entity, so we need to group. That's probably the issue.

**Jose Farias:** Group by what exactly?

**Pedro Steimbruch:** Domain or URL.

**Jose Farias:** Ah, I see what you mean. Which is a text column, is what you're saying.

**Pedro Steimbruch:** Yeah. I can check that and see what we can do there. There's probably some options, but that's the main issue. We have many sortable pointers per domain and per URL.

**Jose Farias:** Yeah. Do we have an index on the snapshotable?

**Pedro Steimbruch:** Yeah, that's something I need to check. I don't remember it, to be honest.

**Jose Farias:** We do. Yeah. So, we could take it offline, but for what it's worth, the sortable pointers abstraction in general—I'm not sold on. I just want to make sure I communicate that. That's not a hard set thing that we need to use.

**Pedro Steimbruch:** I remember. However, I'm not—it's pretty direct. It's like one-to-one, sort the thing and point to it, so.

**Jose Farias:** Yeah. I would be surprised if going through the snapshots was faster.

**Pedro Steimbruch:** I don't think so, because as you mentioned, sortable pointers is good. We just need one join. Otherwise we'd need to group and aggregate for sorting. You're right, I agree with that.

**Jose Farias:** The thing to look out for is that the table is so huge because we capture multiple pointers per snapshot. So it's like three or four times larger than the snapshots table. Something to consider is—I don't think we use the pointers more than a couple days in the past. So we could trim the table and purge it on a schedule so it doesn't grow too much.

**Pedro Steimbruch:** To be honest, yeah. We're only using it for the latest capture date, right? That's the only thing we use.

**Jose Farias:** If that's the case, then we can trim it considerably.

**Pedro Steimbruch:** Yeah, okay.

**Jose Farias:** We can take it offline. Something I wanted to put on your radar.

**Jose Farias:** We can talk about it. Okay.

**Pedro Steimbruch:** Thank you.

**Estevão Mascarenhas:** Bye-bye.

**Estevão Mascarenhas:** Thanks, y'all.

**Stevie Kim:** Have a good one.

**Stevie Kim:** You too.

**Jose Farias:** Bye-bye.
