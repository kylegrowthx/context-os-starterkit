# SS ProjMgmt: System Framework MCP model

<metadata>
date: 2026-02-12
time: 15:01 UTC
duration: 22 minutes
organizer: william@growthx.ai
participants: Leah Myers (RevOps), William Leborgne (Services Lead)
fathom_recording_id: 121937512
fathom_url: https://fathom.video/calls/564335192
share_url: https://fathom.video/share/B1eh3FZF9_26P_yF11ScEqcEwm-y8n2E
source: fathom
enriched_on: 2026-02-27T12:00:00Z
</metadata>

---

## Summary

Leah and William aligned on a simplified PM system for GrowthX's Services team, combining HubSpot (CRM), Notion (Kanban + health scores), and a lightweight UI to surface client milestones. William will focus exclusively on this PM tool, deferring broader process improvements due to capacity constraints (7 clients + team lead duties). The team will test a draft version before rolling out to Ada and Sydney, with William running the subsequent sprint meeting from the new tool to drive adoption.

---

## Context

Both Leah and William are at or near capacity, facing competing demands across revenue operations, client delivery, and process improvement. Leah is investing heavily in HubSpot infrastructure (date fields, revenue fields, attribution fields) to serve as a single source of truth, while contending with data silos (ClientDB redundancies, scattered task tracking). William carries a client load of 7 accounts plus team leadership responsibilities, making broad operational improvements unfeasible. They agreed to narrow scope: William will pursue only the PM system redesign while deferring calibration improvements, check-in structures, and EM/ME integration work until hiring reduces his client load. Leah introduced the MCP (Model Context Protocol) framework, learned in San Francisco, as a foundation for structuring the PM tool using HubSpot as the CRM layer, Notion as the execution layer, and a new UI surface for proactive milestone reminders.

---

## Relevance

- **Delivery Operations:** Simplifies how EMs track client work and team capacity; reduces tool switching from 6+ surfaces to one PM view.
- **Revenue Operations:** Validates HubSpot as single source of truth for revenue, attribution, and client timeline data; eliminates ClientDB redundancy.
- **Team Scaling:** Confirms that process improvement is blocked until William hires more EMs; unblocks PM tool as the only improvement William can execute.
- **Technology Strategy:** Tests MCP framework applied to RevOps; establishes pattern for using Claude instances + Notion + HubSpot for AI-assisted ops.

---

## Overview

- **Scope Reduced:** William will focus only on the PM system, deferring other process improvements to manage his workload (7 clients + team lead).
- **Hybrid Design:** The new system will combine a client health score (using Marcel's 5 signals) with an embedded Kanban board for pending tasks.
- **HubSpot as Source of Truth:** All revenue, attribution, and client data will live in HubSpot to eliminate data silos like ClientDB.
- **Phased Rollout:** William, Ada, and Sydney will test the initial build before a team walkthrough, with William running the subsequent sprint meeting from the new tool to drive adoption.

---

## Key Topics

### Problem: Overwhelmed Team & Inefficient Process

  - Both Leah and William are at capacity, making broad process improvements unfeasible.
  - The current PM process is inefficient, requiring EMs to check multiple tools (e.g., Notion, ClientDB) to get a full client picture.
  - The existing Linear task templates are overly complex, containing many optional tasks that overwhelm users.

### Solution: Simplified PM System

  - The new system will be simple and focused, with only two core views:
    1.  **Client View:** A single source of truth for team meetings.
    2.  **Personal View:** An EM's individual task list.
  - **Core Components:**
      - **HubSpot:** The central CRM for all client data, including new fields for revenue, dates, and attribution.
      - **Notion:** The PM layer, built on the "MCP framework" (a new concept Leah learned in San Francisco).
      - **UI:** A lightweight surface to query data and proactively surface key milestones (e.g., "It's week 4, check these milestones").

### Design: Hybrid Health Score & Kanban

  - The design will adapt the existing PodHQ template to create a more focused client view.
  - **Key Elements:**
      - **Health Score:** EMs will update 5 signals weekly (per Marcel's directive) to provide a high-level status.
      - **Embedded Kanban:** A view of only pending tasks, replacing the current static health score table.
      - **Task Filtering:** A toggle to switch between EM and ME tasks.
      - **Standard Sections:** Action Items, Blockers, and Callouts.

---

## Action Items

**William Leborgne** (Services)
- Document EM needs and constraints in the requirements doc (capacity, task volume, decision-making flow).
- Send Trello screenshots of active EM/ME tasks to Leah as input for the draft design.

**Leah Myers** (RevOps)
- Collect requirements from Ada and Sydney (Services team feedback on the draft once William shares screenshots).
- Build initial draft of the PM system in Notion based on William's Trello screenshots and requirements.
- Share draft with Ada, Sydney, and William for feedback.
- Schedule demo/walkthrough with the Services team (William, Ada, Sydney).
- Hand off to William to run the sprint meeting from the new tool (post-demo).

---

## Transcript

**Leah Myers:** It's been a week of trying to distill and coalesce all of the learnings and stuff. I'm feeling relatively unprepared for this meeting, but I didn't want to push it because I think the most valuable thing to do is probably connect and see where you're at. We did a great job mapping last week, and I've seen Sydney start to put some commentary in the use case form that I set up last week. So that's a good start.

**William Leborgne:** Yeah, honestly, same. I'm definitely behind on all this stuff. I was out Monday, Tuesday with some surgery I needed to do. But outside of that, I'm just catching up. I feel like I'm flying by the seat of my pants, and I'm very excited to do this. But I have not had any time to sit down. So I'm very much in the same boat. I don't feel prepared for this.

**William Leborgne:** Ada was like, "Hey, when is our new project management going to be ready?" So obviously there's a desire for it. Right now I'm handling seven clients while also trying to be a team leader while also trying to improve the process. I basically told Ella, I don't think I can do all three. The improving the process thing, I need to just give myself time until I'm able to hire some more EMs. But the project management piece is the one that I still want to do. There's a lot of other improvements that I'm not going to push for right now. I think bringing calibration up, having a check-in, and trying to integrate the MEs and EMs more is something I can still push for. But anything beyond that, I'm not going to push very hard right now because otherwise I'm going to die.

**Leah Myers:** That makes perfect sense to me. I had a very similar conversation with Andy before I left San Francisco. If I try to do all of it, I'm not going to do a good job at any of it. What I believe will deliver the most value is building out core field functionality in HubSpot—that's our CRM, that's where revenue is recognized. We're seeing a lot of crossover in ClientDB for attribution that really should be in HubSpot. I'm building out date fields, timeline fields, and revenue fields so that I can lay on top of it an MCP framework. I didn't know what MCP meant going into San Francisco, but now I do. I was on my own personal Claude instance trying to crack through it because wrapping one's head around it is difficult. What I think I can do is facilitate an MCP setup that the team can plug their individual Claude instances into—a RevOps MCP that utilizes Notion as project management and HubSpot as our CRM, then create a UI surface attached to a lightweight database. A UI that we can query for context that will remind you: "It is week four. We need to be checking on these milestones." So rather than the EM having to go to six different surfaces to identify where we're at, we coalesce all that into one thing. That's where my head's at. It's a work in progress from ideation—it's not a tangled mess in the sense I'm not confident in it. I am. It's a tangled mess in that parts of it are being articulated, but I have nothing to show yet.

**William Leborgne:** The place that we will look at twice a week as a team and say, okay, let's look at this client versus this crappy Kanban board thing that we currently use. What we had discussed with the pods would be similar, but really tailored to us. My core thing is simplified. It's got to be simple so that everyone knows where to go. I don't think we need a ton of different views. I think two views—the client view and then your own personal view of what you need to do—is probably sufficient. Maybe there's a more complex version for me if I'm overseeing the team. But I'm not saying this is what you should do. I'm saying this is what I would like for us to do.

**William Leborgne:** So I will add this as a task for myself: need to add EM needs in the doc. We can create an initial draft version, review it as a team to make sure it works really well between Ada, myself, and Sydney. I wonder if you'd be open to presenting it in the next sprint stand-up, maybe Thursday or something, once the three of us have been able to play around with it and get more used to it.

**Leah Myers:** I could do the walkthrough, and then from there, you run the sprint meeting to further drive adoption.

**William Leborgne:** Exactly.

**William Leborgne:** Okay, let's jump into the PodHQ template you built. Looking at a client view, we can quickly see the clients, where they are in the sprint, and who's responsible. When I look at a client view, it's sort of a Kanban of tasks that need to happen versus status. But I still think we need somewhere where we're capturing the status of the company—the health score. It's almost a hybrid. We're going to each client, but I don't think we need all this additional information like ICPs. We need a smaller view: what is the health? What information do we need to note? And then the Kanban of pending tasks. Does that make sense?

**Leah Myers:** That makes sense. You're identifying the stuff that should be in HubSpot. We don't need this on our product management tracker. What we do need are these project management aspects.

**William Leborgne:** Exactly. A Kanban of all the tasks. I like the structure of action items, blockers, and callouts. I also think it's good to have some kind of flag and grading like the health score. But I think it needs to be simplified. Maybe three metrics?

**Leah Myers:** I hear you, but we're not going to win on that because Marcel is really pushing the five signals. It'll be five signals on every account.

**William Leborgne:** Yeah, fine. Five signals. That's fine. We'll probably have the EMs fill those out once a week—on Friday, then we review it Tuesday and say, okay, here's the health score and the flag. What are the action items? What are the blockers? How are we progressing towards the performance? Are you focused on the North Star of the client, and how are you progressing with actually showing them results? And then we'll see all the pending tasks. It looks like we're in week three, you did half of these, some are pending—where are we at? Then it's super clean and seamless.

**Leah Myers:** Yeah, that's completely reasonable and doable.

**William Leborgne:** The challenge is that the Linear template has so many tasks. There's a lot of optional stuff. Discuss image preferences—I don't think we need them. There's a core set of tasks that are needed, and this is more than that. The template overwhelms you. But if we could switch between EM and ME tasks, that would be badass.

**Leah Myers:** Yeah, we could do that. For requirement gathering, just take a screenshot of your Trello board showing the actual tasks you're paying attention to, and I'll translate it. Or I have many AI tools now that can do a lot of work for me.

**William Leborgne:** There you go. Just use the work you've already built.

**Leah Myers:** I'm going to use you pinging me saying you're comfortable with the requirements you've given me as my signal to start standing this up.

**William Leborgne:** Okay, great. We'll do that.
