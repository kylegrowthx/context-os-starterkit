# Datagrid <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-19
time: 18:00 UTC
duration: 21 minutes
organizer: team@growthxlabs.com
participants: Kaitlin Quimby (Toric), Liz Kushnereit (GrowthX), Thiago da Costa (Datagrid)
fathom_recording_id: 123792481
fathom_url: https://fathom.video/calls/571614057
share_url: https://fathom.video/share/RbpTytsgxmvJ1EkFQegjZrWz_ypvd4DH
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

Liz walked through the aggressive 6-week website cutover plan (Feb 3 - Mar 16), covering the new agent-centric architecture, contract blockers tied to an ~$11k budget increase, and the content strategy pivot to building agent clusters. Both teams aligned on prioritizing the top 5-6 agents and will coordinate on Q1 payment logistics.

---

## Context

This is a key weekly sync on the Datagrid-CheckThat website replatforming project. Kaitlin (Toric, acquired parent) and Thiago (Datagrid, engineering) are coordinating with Liz (GrowthX, content/strategy lead) on a mid-March launch. The project has grown significantly in scope since the initial Feb 3 kickoff, requiring a formal project plan for internal visibility and blocker escalation. The contract is partially stalled on budget alignment and Q1 payment mechanics due to Toric's acquisition, but work is proceeding. Traffic remains stable despite the publishing pause, likely boosted by recent content refreshes and the acquisition announcement.

---

## Relevance

- **Timeline & Delivery:** 6-week aggressive cutover (Feb 3 - mid-March) now serves as the baseline. The forward-deployed engineer is returning early next week with critical answers on migration expectations, deadlines, and long-term maintenance.
- **Budget & Commercial:** ~$11k budget increase (verbal agreement between Tiago and Marcel) needs formalization. Q1 payment structure must be clarified—Toric pays quarterly and may owe an additional amount for this new scope.
- **Content & Product:** Agent-centric architecture replaces legacy structure. Publishing paused during migration; new cadence is scaffolded around agent clusters. Top 5-6 agents are highest priority for content build-out.
- **Risk & Blockers:** No immediate blockers on Datagrid/Toric as of this call. Main unknowns: engineering capacity post-PTO, contract/budget sign-off, and content taxonomy for migration (merge, redirect, delete) without losing high-performing legacy SEO value.

---

## Overview

- **Aggressive 6-Week Cutover:** The full site migration is targeted for a mid-March launch, with a new project plan now serving as the source of truth for tracking progress and escalating blockers.
- **Contract & Budget Blockers:** The contract is stalled by an \~$11k budget increase and payment logistics post-acquisition. Both teams will investigate Q1 payment status to resolve this.
- **Agent-Centric Architecture:** The new site architecture uses agents as the central hub, routing users to related content (guides, connectors) to drive engagement and activation.
- **Content Strategy:** Publishing is paused during the migration. The new strategy will build content clusters around agents, starting with the top 5–6 agents based on current data.

---

## Key Topics

### Project Timeline & Plan

  - An aggressive but realistic 6-week cutover is planned, targeting a mid-March launch.
      - **Start Date:** Feb 3rd (date of the initial presentation to Kaitlin & Tiago).
  - A new project plan was created to manage the project's growing scope.
      - **Purpose:** Provide internal visibility and serve as the source of truth for tracking progress and escalating blockers.
      - **Shared With:** Kaitlin (new email) and Tiago (old email).
  - The forward-deployed engineer (dev work) is on PTO, returning early next week.
      - **Action:** Liz will get answers on migration expectations, deadlines, and long-term maintenance upon their return.

### Contract & Budget

  - The contract is stalled by two issues:
      - **Budget Increase:** An \~$11k increase, based on a verbal agreement between Tiago and Marcel, needs to be formalized.
      - **Payment Logistics:** The acquisition complicates payment. Kaitlin will confirm if Toric pays quarterly and if a Q1 payment is due for the new scope.
  - The Statement of Work (SoW) focuses on editorial content (SEO), not dev work.
      - **Rationale:** The long-term plan is SEO content, while the dev work is a prerequisite for that strategy.

### New Site Architecture & Prototype

  - Liz demoed the prototype (from the Loom video) to illustrate the new architecture.
  - **Core Concept:** Agents are the central hub, routing users to related content to drive activation.
      - **Improved UI/UX:** Cleaner design with linkable inputs/outputs on agent pages.
      - **Navigation:** Routes users to a "Connectors Hub" and "Related Guides."
  - **Content Migration Strategy:**
      - **Process:** Merge, redirect, or delete legacy content.
      - **Safeguard:** High-performing legacy content will be protected to preserve SEO value.
  - **Agent Forking:** Pushed to a post-launch MVP.
      - **Rationale:** Technical validation of agent cloning is complete, de-risking the feature for a later release.

### Content Strategy & Prioritization

  - Publishing is paused during the migration to focus all resources on the cutover.
      - **Rationale:** Current traffic is stable, likely due to recent refreshes and the acquisition. Liz will monitor weekly for any dips.
  - **New Publishing Cadence:**
      - **Week 1:** Build guides that surround a specific agent.
      - **Week 2:** Map programmatic and connector content related to that agent.
      - **Goal:** Build out 18 agent clusters.
  - **Agent Prioritization:**
      - Kaitlin confirmed the first 5–6 agents in the current list are the top priority.
      - **Action:** GrowthX will start building content clusters around these top agents.

---

## Action Items

**Kaitlin Quimby (Toric)**
- Confirm Q1 billing/payment for new scope; coordinate w/ Liz on invoicing
- Review Loom prototype; send feedback to Liz

**Liz Kushnereit (GrowthX)**
- Confirm Q1 billing/payment for new scope; coordinate w/ Kaitlin on invoicing
- Get answers from forward-deployed engineer on migration expectations, deadlines, and long-term maintenance upon return from PTO

---

## Transcript

**Liz Kushnereit:** Can you hear me now?

**Kaitlin Quimby:** Yeah, sorry, I was on a different speaker—I'm eating lunch and off camera.

**Liz Kushnereit:** No worries. Quick note: I'll need to know if we should set up a separate Slack channel for you on the Procore side.

**Kaitlin Quimby:** Right, so Toric moved us to a Procore Slack. I can't add you guys yet—we have to set it up through a specific external approval process, but we're working on it.

**Liz Kushnereit:** Got it. Okay, so today I wanted to give a high-level overview since this has gotten very complex. Let me walk through the main pieces.

### Contract & Budget

**Liz Kushnereit:** First, a quick contract update. There's about an $11k difference based on a verbal agreement between Tiago and Marcel. We need to sort out how that gets formalized, and I know the acquisition complicates things.

**Kaitlin Quimby:** Yeah, that's why I wanted to confirm—budget-wise, I need to know if this comes from a specific Toric pot. Also, I'm 90% sure we pay quarterly. Are we owed an additional Q1 payment for this new scope?

**Liz Kushnereit:** Good question. Let me double-check that internally, and you can confirm from your side.

**Kaitlin Quimby:** Exactly. We'll do this in parallel.

**Liz Kushnereit:** On the contract itself, the Statement of Work focuses on editorial content and SEO, not the dev work. We're doing all the dev work, but long-term, the plan is SEO content.

### Project Timeline

**Liz Kushnereit:** So I sat down and mapped this out because it got complex. An aggressive but realistic timeline for a full cutover is six weeks, starting from our Feb 3 kickoff conversation, which puts us at mid-March for launch. That's doable unless our forward-deployed engineer—who's on PTO and returning early next week—tells me otherwise. I'll get answers from him on migration expectations, deadlines, and long-term maintenance.

I created a formal project plan covering architecture, migration, design, implementation, and content strategy. It's shared with your new email and Tiago's old email. It's the source of truth for tracking progress and escalating blockers. Right now, I don't have anything blocked on your end.

### Content & Publishing

**Liz Kushnereit:** We've paused publishing to focus on the cutover. Traffic is holding up well—I think that's from the recent refreshes and the acquisition. If it dips significantly, I'll react. Otherwise, I'll monitor weekly.

**Kaitlin Quimby:** Okay.

**Liz Kushnereit:** Did you get a chance to look at the Loom prototype from last week?

**Kaitlin Quimby:** Not yet, but I'd love to see it.

**Liz Kushnereit:** Quick overview: the new site puts agents at the center. They have improved UI/UX with linkable inputs and outputs. Users route to a Connectors Hub and Related Guides. That's the core concept—agents as the backbone driving activation.

For content migration, we'll merge, redirect, or delete legacy pages. We'll protect high-performing pieces to preserve SEO. Agent forking is pushed to post-launch MVP. We've already validated that cloning is technically proven.

Our publishing cadence is scaffolded: Week 1 builds guides around one agent, Week 2 maps programmatic and connector content for that agent. We'll build out 18 full agent clusters. Any agent prioritization on your end?

**Kaitlin Quimby:** The first five or six agents in our current list are definitely the top priority.

**Liz Kushnereit:** Perfect, we'll start there.
