# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-01-30
time: 16:00 UTC
duration: 28 minutes
organizer: Stevie Kim (stevie@growthx.ai)
participants:
  - name: Marcel Santilli
    role: CEO/Founder
    affiliation: GrowthX
    email: marcel@growthxlabs.com
  - name: Daniel Lopes
    role: Advisor
    affiliation: GrowthX
    email: daniel@growthxlabs.com
  - name: Jason Gong
    role: Team Member
    affiliation: GrowthX
    email: jason@growthx.ai
  - name: Pedro Steimbruch
    role: Backend Engineer
    affiliation: CheckThat (GrowthX)
    email: pedro@growthx.ai
  - name: Jose Farias
    role: Backend Engineer
    affiliation: CheckThat (GrowthX)
    email: jose@growthx.ai
  - name: Estevão Mascarenhas
    role: Fullstack Engineer
    affiliation: CheckThat (GrowthX)
    email: estevao@growthx.ai
  - name: Leonardo Carpenedo Steffen
    role: QA/Release Engineer
    affiliation: CheckThat (GrowthX)
    email: leonardo@growthx.ai
  - name: Stevie Kim
    role: Product Manager
    affiliation: CheckThat (GrowthX)
    email: stevie@growthx.ai
fathom_recording_id: 118538808
fathom_url: https://fathom.video/calls/549531355
share_url: https://fathom.video/share/yL1di7AsU8xx4nyjmR_q4UkpbSFHM14G
source: fathom
enriched_on: 2026-02-28 09:15 UTC
</metadata>

---

## Summary

CheckThat team conducted a final launch readiness sync covering billing restrictions, data cost optimization, performance improvements, and release process updates. Key decisions: implement "Contact Sales" for Business plan, migrate GrowthX customers to Pro, optimize data probing cadence, and establish a lightweight review process with Leonardo as QA gatekeeper.

---

## Context

CheckThat is approaching launch with a focus on operational readiness. The team is aligning billing models with the new pricing structure, where the Business plan shifts from self-serve to "Contact Sales" only. This required moving existing GrowthX customers from unlimited plans to Pro, necessitating careful backfill logic to avoid performance degradation. Concurrently, the backend team is optimizing costs by transitioning from daily to every-other-day data probing, which creates technical challenges around trendline visualization. Pedro has made significant performance gains on the Sources page, and the team is implementing a new release review workflow to ensure quality without adding process overhead. Leonardo will serve as the final QA checkpoint, reviewing completed work before moving to Done.

---

## Relevance

- **Product Launch**: Critical pre-launch coordination on billing, data infrastructure, and release readiness
- **Technical Debt**: Addressing performance and data efficiency concerns before go-live
- **Process**: Establishing lightweight QA and release workflows to support rapid iteration
- **Cost Optimization**: Balancing data freshness with operational expenses
- **Team Coordination**: Clear ownership and dependencies among engineering roles

---

## Overview

- **Billing Logic:** The Business plan is now "Contact Sales." GrowthX customers will be moved from "unlimited" to "Pro" to align with the new pricing model.
- **Data Cadence:** Probing will shift to every other day to cut costs. Jose is resolving how to display trendlines with missing data points, exploring options like omitting days or using trailing averages.
- **Performance:** Pedro optimized the Sources page query from \~9s to 2.5s by adding missing indexes, significantly improving user experience.
- **Process:** Leonardo will now conduct a final sanity review of all completed tasks before release, acting as a second pair of eyes.

---

## Key Topics

### Billing & Plan Management

  - **Business Plan:** Now "Contact Sales" only, preventing self-service upgrades.
      - **UI:** Button opens a pre-filled email to the sales team.
  - **GrowthX Customer Migration:**
      - **Action:** Move all GrowthX customers from "unlimited" to "Pro" plan.
      - **Rationale:** Aligns with the new pricing model.
      - **Ticket:** Estevão will create a ticket to perform this migration and build an admin action for future use.
  - **Backfill Logic for Upgrades:**
      - **Problem:** Upgrading a workspace triggers a data backfill, which could cause performance issues if many users upgrade simultaneously.
      - **Solution:** Implement a new `free_to_pro_upgrade` backfill type.
          - **Trigger:** Immediately upon a user clicking the "Pro" upgrade button.
          - **Logic:** Only backfill data for the missing 14-day gap (from 45 days to 14 days) if the workspace is newer than the standard backfill period.

### Data Cadence & Trendline Display

  - **Problem:** Shifting to every-other-day probing to cut costs will create data gaps, breaking the current trendline display logic which assumes daily snapshots.
  - **Proposed Solutions:**
    1.  **Omit Missing Days:** Let the `recharts` library handle the gaps by connecting the available data points.
    2.  **Trailing Average:** Display a 7-day trailing average, a method preferred by Marcel for smoothing data.
    3.  **Probe Daily, Display by Plan:** Probe daily and use plan tiers to limit data visibility (e.g., Free plan sees every-other-day data, Pro plan sees daily). This creates an upgrade path but increases costs.
  - **Decision:** Jose will research the best approach and consult Daniel on the cost implications of daily probing.

### Performance & Bug Fixes

  - **Sources Page Optimization:**
      - **Problem:** The slowest query on the Sources page was taking \~9 seconds.
      - **Solution:** Pedro added missing indexes, identified with help from Claude.
      - **Result:** Query time reduced to 2–2.5 seconds, significantly improving page load speed.
  - **Prompt Index Table Metrics:**
      - **Problem:** The backfill for new group metrics (1.5M records) is running slowly.
      - **Solution:** Jose will pivot from individual record processing to a faster, batched backfill method.
  - **Other Fixes:**
      - **Rounding:** Numbers now round consistently (0 decimals everywhere except the overview page, which uses 1).
      - **Counts:** Fixed incorrect counts on the prompts page and ensured they update correctly after activating/retiring prompts.
      - **UI:** Added a tooltip to the prompt stage selector to clarify that library prompts can be changed.

### Release Review Process

  - **Goal:** Add a final sanity check before release without creating process overhead.
  - **New Workflow:**
      - **Devs:** Tag Leonardo in the comments of completed tickets.
      - **Leonardo:** Filters by his tag, reviews the work, and moves the ticket to "Done."
  - **Rationale:** This provides a second pair of eyes for quality assurance while keeping the process lightweight, especially for minor UI fixes.

---

## Action Items

**Estevão Mascarenhas**
- Move GrowthX customers to Pro; create admin action; tag EMs/directors to prune >500 prompts
- Create 'Free to Pro upgrade' backfill; trigger on onboarding Pro click; add age guard

**Jose Farias**
- Batch-backfill prompt index group metrics
- Research sparse trendlines; loop Daniel re: cost/cadence; share approach w/ team

**Pedro Steimbruch**
- Review pghero for index recommendations
- Enforce board process: tag Leo; Leo moves to Done

**Leonardo Carpenedo Steffen**
- Perform sanity review of this week's changes; sync w/ Stevie

---

## Transcript

**Stevie Kim:** Yesterday I tested billing and we needed to make sure business plan is not self-serve. I went through the backlog of tickets to make sure we're not missing anything. Going to review the analytics stack Daniel implemented.

**Estevão Mascarenhas:** We already have the guard for the business plan so users can't self-service it. When a user selects the business plan, we show "Contact Sales" as the button, and clicking it opens a pre-filled email to the sales team. The backend wiring is already done. We need to trigger the backfill when there's a plan change. We need to be careful because setting GrowthX customers to unlimited could trigger lots of backfilling at the same time. I'll handle the onboarding UI improvements.

**Jose Farias:** For backfills, GrowthX customers already have 17 days of backfill data, so we don't need to backfill them. When upgrading to Pro, we should check if the workspace is older than our standard backfill period. If it's not, we need to create a new backfill type. We have onboarding, competitor change, and prompt addition backfill types already. I suggest calling it "free to pro upgrade" backfill. We'd trigger it when they click Pro in onboarding and backfill from 45 to 14 days—the gap for newer workspaces.

Yesterday I shipped the group metrics for the prompt index table. The code is live but we need to backfill 1.5 million records. I'm going to speed that up this morning, then look at the data cadence issue. We're shifting to every-other-day probing to cut costs, but our current trendline system assumes a snapshot for every day. I need to figure out how to handle the gaps—what value should we display when there's no daily snapshot?

**Pedro Steimbruch:** When you shift to every-other-day probing, will there not be snapshots for every day?

**Jose Farias:** Exactly. Right now we iterate through dates and find the snapshot. When we start probing every other day, we can't iterate on days anymore because there won't be a snapshot for every day. We need to flip the loop to iterate on available snapshots instead.

**Stevie Kim:** In my mind, what users get doesn't have to mirror what we're doing behind the scenes. We could probe daily but show snapshots based on what they're paying for. Free plan might see every-other-day data, Pro sees daily.

**Jose Farias:** That's an interesting approach for creating an upgrade path. We could sell the availability of daily data.

**Stevie Kim:** Every-other-day probing would cut costs in half. Let's loop Daniel in—he's very focused on data quality, so we should get his input on the cost implications before we deploy.

**Jose Farias:** I'll put it in the chat and tag Daniel. I'll take the cadence ticket today.

**Estevão Mascarenhas:** Another idea for trendlines: we could show the trailing average of the past seven days. Marcel prefers showing trailing averages for metrics.

**Jose Farias:** Do we support that? Pedro, you coded that, right?

**Pedro Steimbruch:** I used it for the prompt show page, but I removed it when I refactored to use the database directly.

**Jose Farias:** I'll dig up the code and see if I can reuse it.

**Pedro Steimbruch:** You could also just omit missing days from the dataset. The recharts library should handle drawing the trendline with gaps.

**Stevie Kim:** Customers just want to see trends—is it going up or down? They don't care about specific days.

**Pedro Steimbruch:** To be honest, we don't even show dates on the prompt trendlines.

**Jose Farias:** We could skip this complexity. I'll figure it out and let everyone know.

**Pedro Steimbruch:** One more thing about your backfill—I noticed you were doing individual record processing. Why don't you just use the batched method?

**Jose Farias:** That's exactly what I was thinking. I did it for all our clients over 45 days and it took less than half an hour.

**Pedro Steimbruch:** Yesterday I fixed rounding to be consistent—0 decimals everywhere except the overview page, which uses 1. Fixed incorrect counts on the prompts page. Also fixed counts not updating after activating or retiring prompts. Yesterday I started the Sources page optimization and merged it this morning. The slowest query was taking 9 seconds; now it's 2 to 2.5 seconds. We were missing a few indexes—thanks Claude for finding them. Today I also sent brand colors via the BrandFetch API. Costs went over: we're at 500 dollars instead of 125 because I'm fetching colors for every brand. About 200 brands are still being processed. I improved the prompt stage selector with a tooltip explaining that library prompts can be changed. I'm going to grab another P1 ticket.

**Jose Farias:** There's a library called pghero we should probably use. It catches index issues and recommends better indexes. Open source and free.

**Pedro Steimbruch:** Interesting, I'll check it out.

**Leonardo Carpenedo Steffen:** I'll review everything we've moved this week to do a sanity test before release. I'll look at everything to make sure nothing broke and be a second pair of eyes.

**Pedro Steimbruch:** Do we need a different workflow column, or should items stay in review until someone moves them to done?

**Leonardo Carpenedo Steffen:** I was thinking developers could just tag me in comments. But I can filter for my tag and review items myself. I don't think we need a new column.

**Stevie Kim:** We haven't been doing formal reviews for each item anyway. I'm checking things as I go. For small UI fixes, we don't need formal review. For bigger changes that could break things, let's keep them in review longer. But these small fixes don't need formal review.

**Leonardo Carpenedo Steffen:** So everybody tag me in comments when work is done, and I'll filter by my tag, review, and move to Done. I'll add a green tag when ready to move.

**Stevie Kim:** That works. Just tag Leo and I don't care if things stay in review or move to done as long as they're not stuck.

**Jose Farias:** Thanks, everyone. Thanks, y'all.

**Stevie Kim:** Happy Friday.

**Pedro Steimbruch:** Happy Friday. Bye.
