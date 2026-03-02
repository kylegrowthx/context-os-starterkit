# SS ProjMgmt: System Framework MCP model

<metadata>
date: 2026-02-12
time: 15:01 UTC
duration: 22 minutes
organizer: william@growthx.ai
participants: Leah Myers, William Leborgne
fathom_recording_id: 121937512
fathom_url: https://fathom.video/calls/564335192
share_url: https://fathom.video/share/B1eh3FZF9_26P_yF11ScEqcEwm-y8n2E
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

William and Leah aligned on the scope and design of a new project management system to consolidate the delivery team's workflow. William is narrowing focus to PM only (deferring broader process improvements) due to capacity constraints managing seven clients while leading the team. The system will combine HubSpot as a source of truth for client data, Notion with an MCP framework as the PM layer, and a lightweight UI that surfaces key milestones by week. The hybrid design includes a health score (five signals updated weekly by EMs per Marcel's directive), an embedded Kanban board for pending tasks, and toggles between EM and ME task views. William will provide Leah with screenshots of his simplified Trello task lists to define the template, Leah will build a draft and demo it with William, Ada, and Sydney before presenting to the team in a sprint meeting.

---

## Context

William Leborgne (Team Lead/EM) and Leah Myers (Operations/RevOps) met to design a new project management system for GrowthX's delivery team. William is stretched managing seven active clients while leading the team, making broad process improvements infeasible. Leah has been focused on consolidating client data into HubSpot and recently learned about the MCP (Model Context Protocol) framework in San Francisco, which she wants to apply here. The current workflow requires EMs to check multiple tools (Notion, ClientDB) for a complete client picture, and Linear task templates are overly complex with optional tasks that overwhelm users. This meeting determined the scope, architecture, and phased rollout for a simplified system.

---

## Relevance

**To GrowthX Delivery:**
- New PM system will reduce tool sprawl (currently Notion, ClientDB, Linear, Trello) and centralize client state via HubSpot + Notion, improving EM efficiency.
- Health score updated weekly by EMs (5 signals per Marcel's framework) will standardize client status reporting.
- Embedded Kanban and task filtering (EM vs. ME) will simplify sprint reviews and individual task management.
- Phased rollout: William, Ada, Sydney test → demo → team adoption in sprint meeting, reducing change friction.

**To GrowthX Operations:**
- HubSpot becomes single source of truth for revenue, attribution, dates — eliminating data silos in ClientDB.
- MCP framework layered on top of Notion will enable future AI-powered context queries (e.g., "It's week 4, check these milestones").
- Lightweight UI will surface proactive milestones and reduce context-switching between tools.

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

**William Leborgne (GrowthX)**
- Add EM needs to requirements doc
- Send Trello screenshots of active EM/ME tasks to Leah; then Leah builds draft, shares w/ Ada & Sydney, schedules demo, hands off

**Leah Myers (GrowthX)**
- Collect requirements from Ada & Sydney

---

## Transcript
**Leah Myers:** Same.

**Leah Myers:** It's been a week of trying to distill and coalesce all of the learnings and stuff.

**Leah Myers:** So, yeah, I'm feeling relatively unprepared for this meeting, like I should have done something.

**Leah Myers:** But I didn't want to push it because I think the most valuable thing to do is probably connect and see where you're at.

**Leah Myers:** We did a great job mapping last week, and I've seen Sydney start to put some commentary in the use case form that I set up last week.

**Leah Myers:** So that's a good start.

**William Leborgne:** But how are you doing?

**William Leborgne:** Yeah, honestly, same.

**William Leborgne:** I'm definitely behind on all this stuff.

**William Leborgne:** I was out Monday, Tuesday.

**William Leborgne:** had some surgery I needed to do.

**William Leborgne:** But outside of that, I'm just catching up.

**William Leborgne:** I feel like I'm flying by the seat of my pants, and I'm very excited to do this.

**William Leborgne:** But I have not had any time to sit down.

**William Leborgne:** So I'm very much in the same boat.

**William Leborgne:** I don't feel prepared for this.

**Leah Myers:** I don't have anything specific.

**Leah Myers:** All I can tell you is that...

**William Leborgne:** Ada was like, hey, when is our new project management going to be ready?

**William Leborgne:** So obviously there's a desire for it, which is great.

**William Leborgne:** So, I mean, this meeting can be pretty short in the sense of like we can just say, hey, this is what we're going to do and then set up another meeting for when we actually have time to do those things.

**William Leborgne:** I was just talking to Ella about this yesterday and I was saying that like right now it's just very difficult for me because I'm handling seven clients while also trying to, you know, be a team leader while also trying to then find time to how do I improve the process.

**William Leborgne:** And I basically told her, was like, I don't think I can do this like all three.

**William Leborgne:** I think I, the, the improving the process thing, I need to just give myself time until I'm able to hire some more EMs who then can replace me and really take over my, my plate of work.

**William Leborgne:** But like, it's just so much work to do this, to do that.

**William Leborgne:** The client strategies and everything else.

**William Leborgne:** long story short, the project management piece of it is the one that I still want to do.

**William Leborgne:** There's a lot of other improvements that I think I'm not going to push for right now.

**William Leborgne:** I think we still, like some of the core things that we talked about, which is like bringing the calibration up and having a check-in and trying to integrate the MEs and EMs more is something I can still push for.

**William Leborgne:** But anything beyond that, I'm not going to push very hard right now because otherwise I'm going to die.

**Leah Myers:** Yeah, yeah.

**Leah Myers:** That makes perfect sense to me.

**Leah Myers:** And I had a very similar conversation with Andy, honestly, before I left San Francisco.

**Leah Myers:** Like, this is what's on my plate en masse.

**Leah Myers:** And if I try to do all of it, I'm not going to do a good job at any of it.

**William Leborgne:** Yeah, exactly.

**Leah Myers:** What I believe will deliver the most value across the board is the path I'm currently on, which is building out just core field functionality in HubSpot.

**Leah Myers:** That's our CRM.

**Leah Myers:** That's where revenue is recognized.

**Leah Myers:** That's where, like, we're seeing a lot of crossover in client DB for the attribution that really should be in HubSpot.

**Leah Myers:** So I'm building out date fields, building out timeline, like, integer fields there, along with revenue and blah, blah, blah, so that I could lay on top of it an MCP framework.

**Leah Myers:** And I didn't know what MCP meant going into San Francisco last week, but now I do, and I have, like, the AI helped me generate a plan.

**Leah Myers:** I was actually on my own personal Claude instance last night on the couch, like, just trying to crack through it because wrapping one's head around it is difficult, I've found.

**Leah Myers:** Not that hard, but, um, so what I think I can do is facilitate an MCP setup that the team can then plug their individual Claude instances into, so, like, it'll be, like, RevOps MCP that utilizes Notion as project management.

**Leah Myers:** Using that framework in there, and then HubSpot as our CRM, traditional CRM stuff, and then create a UI that ultimately, like, is attached to a lightweight database.

**Leah Myers:** I'm not going to get into too much, but like a UI, like a surface that then we can query for context that will remind you, general you, like EM in strategy spread.

**Leah Myers:** It is week four.

**Leah Myers:** We need to be checking on these milestones, like, that we identified, right?

**Leah Myers:** So, like, bringing them to the surface rather than the EM having to go to six different surfaces to, like, identify this is where we're at, just coalescing all that into one thing.

**Leah Myers:** That's where my head's at, and it's a tangled mess, and I feel, it's not a tangled mess in the sense, like, I'm not confident in it.

**Leah Myers:** I am, but it's a tangled mess in that it's a work in progress from ideation, and when parts of it are being articulated, but I have nothing to show.

**William Leborgne:** The place that we will look at twice a week as a team and say, okay, let's look at this client versus this like kind of crappy Kanban board thing that we currently use.

**William Leborgne:** And I think that was like the original idea that we had discussed of what you had built with the pods.

**William Leborgne:** It would be similar, but really tailored to us.

**William Leborgne:** And what my core thing is simplified.

**William Leborgne:** It's got to be simple so that everyone can like just knows where to go.

**William Leborgne:** I don't think we need a ton of different views and stuff.

**William Leborgne:** I think maybe two views, which is like the client view and then your own personal view of like what do you need to do is probably sufficient.

**William Leborgne:** Maybe there's like a more complex version for me specifically if I'm overlooking the team.

**William Leborgne:** But that's kind of what's on my mind.

**William Leborgne:** But I'm not trying to say like this is what you should do.

**William Leborgne:** I'm saying this is what I would like for us to do.

**William Leborgne:** And then you tell me, you know, what.

**William Leborgne:** Thank you.

**William Leborgne:** Okay, great.

**William Leborgne:** So I will, let me just add this as a task for myself.

**William Leborgne:** Need add EM needs in the doc.

**William Leborgne:** There we go.

**William Leborgne:** Okay, great.

**William Leborgne:** Okay, I will do that.

**William Leborgne:** A chance to create some initial draft version of it.

**William Leborgne:** We can review it as a team, make sure it works really well between Ada, myself, and Sydney.

**William Leborgne:** And then I just need a plan of action for implementing it.

**William Leborgne:** I wonder if you'd be open to, in the next sprint stand-up, maybe not the next one, maybe it's Thursday or something, once the three of us have been able to play around with it and get a bit more used to it, is to present it to the team and give them a little bit of a walkthrough.

**Leah Myers:** And then I could do the walkthrough, and then from there, you run the sprint meeting.

**Leah Myers:** I haven't attended in weeks, I'm so sorry.

**William Leborgne:** But then you run the sprint meeting from what I just walked through to further drive adoption sort of thing.

**William Leborgne:** Exactly.

**Leah Myers:** yep, absolutely.

**William Leborgne:** Cool.

**William Leborgne:** Okay, let's just jump into the one you already built for the pod.

**Leah Myers:** Yeah.

**William Leborgne:** Real quickly.

**William Leborgne:** Real Yeah.

**Leah Myers:** Do you want to drive?

**William Leborgne:** Yes, if I can.

**Leah Myers:** Absolutely.

**William Leborgne:** Well, I'm thinking if I can because I need to remember, is it, it's not this, is it?

**William Leborgne:** Or is it this?

**Leah Myers:** It's, that's part of it, but it's actually PodHQ.

**Leah Myers:** So in the search bar, it's not ClientDB, though.

**Leah Myers:** ClientDB is a related database.

**William Leborgne:** PodHQ.

**Leah Myers:** Yep.

**William Leborgne:** Okay.

**Leah Myers:** So it's nested in here.

**Leah Myers:** If you click on PodZ, actually, that one is stood up for your team.

**William Leborgne:** Yeah.

**Leah Myers:** And then further down on the page, there's a, oh, we're back on PodHQ.

**Leah Myers:** So if you want to see one that's actively used, Katya uses hers, I believe, pretty religiously.

**Leah Myers:** And there's an embedded table, the client project and tasks view.


**William Leborgne:** This is that we can quickly see the clients and we can quickly see where they are in the sprint.

**William Leborgne:** Oh, and then the thirdly is we can quickly see who is responsible for it.

**William Leborgne:** I think that is a helpful view.

**William Leborgne:** When I'm looking at this, this is by person.

**William Leborgne:** So it would be like each person going through and being able to say, so I'm just thinking about like that.

**William Leborgne:** I'm just using the use case of we're in a team meeting and I'm trying to talk to my team and say, hey, where are we at with this?

**William Leborgne:** Would it be, because when I'm jumping over, let's say to a client view, it's sort of a Kanban, but of that client of tasks that need to happen versus like a status.

**William Leborgne:** I almost wonder if we still have something like this because then we can quickly look through and go, okay, it looks like all these things are pending.

**William Leborgne:** Where are we at?

**William Leborgne:** But I still think we need somewhere where we are adding a little bit of the status of the company.

**William Leborgne:** Ooh, actually, this is, I remember this is, this is part of what I was interested in, is exactly this.

**William Leborgne:** Like, I do think we need something like this, where we, where we are having the EMs fill out health scores before the meeting.

**William Leborgne:** So, it's almost a hybrid of, or maybe the view is this.

**William Leborgne:** Maybe the view is, like, we're going to each client.

**William Leborgne:** I don't think we need all this additional information, like ICPs and all this stuff, like a sort of smaller view, where you have, okay, what is the health?

**William Leborgne:** What, what is the latest, like, information that we need to just note down?

**William Leborgne:** And then the Kanban of, like, what's, what tasks are pending?

**Leah Myers:** Yep.

**William Leborgne:** Does that make sense?

**Leah Myers:** That does make sense, because you're saying, like, the stuff, you're identifying the stuff that should be in HubSpot, really.

**Leah Myers:** Like, we don't need this on our product management tracker.

**William Leborgne:** Correct.

**Leah Myers:** That needs to go to HubSpot.

**Leah Myers:** And what we do need are these project management aspects.

**Leah Myers:** So, yes, that does make sense.

**Leah Myers:** If we had an embedded view of, like, open tasks rather than that health score embedded view near the bottom of the page, if that was instead, like, these are the pending tasks, would that?

**William Leborgne:** Yeah, exactly.

**William Leborgne:** Yes.

**William Leborgne:** Like, exactly.

**William Leborgne:** Like, these are the pending tasks.

**William Leborgne:** Yeah, exactly.

**William Leborgne:** Like, a Kanban, like, of all the tasks.

**William Leborgne:** So we could, we could, we could, I like this, like, action items from the week blockers and callouts.

**William Leborgne:** Like, that having this progress, actually, all four of these are great.

**William Leborgne:** Like, I think it's good to structure it in this way.

**William Leborgne:** I also think it's good to have some kind of a flag and a grading like this, like the health score.

**William Leborgne:** I think this is good.

**William Leborgne:** But I, like we had talked about last week, like, I think it does need to be simplified.

**Leah Myers:** it do need to ofition.

**Leah Myers:** Yeah.

**William Leborgne:** But it's Okay.

**William Leborgne:** Maybe like three metrics that we grouped together.

**Leah Myers:** I hear you, but we're not going to win on that because Marcel is really pushing the five signals.

**Leah Myers:** So I just want to throw that out there.

**Leah Myers:** It'll be five signals on every account.

**William Leborgne:** Yeah, fine.

**William Leborgne:** Okay, five signals.

**William Leborgne:** That's fine.

**William Leborgne:** But in any case, I think let's, in a way, we'll need, we'll want to have that.

**William Leborgne:** Maybe we're not going to have that.

**William Leborgne:** We'll probably have the EMs fill those out once a week, not twice for each meeting.

**William Leborgne:** Maybe on like a Friday and then we review it that next Tuesday and be like, okay, looks like the health score is this and looks like the flag is this.

**William Leborgne:** What are the action items?

**William Leborgne:** What are the blockers?

**William Leborgne:** How are we doing on like progressing towards the performance?

**William Leborgne:** Again, we're going to tweak all these things a little bit, but in essence, it's like, are you focused on the North Star of the client?

**William Leborgne:** Like a reminder again, and then how are you progressing with actually showing them results?

**William Leborgne:** Okay, good, good, good.

**William Leborgne:** And then we're going to go over and if we need to see like all the pending tasks.

**William Leborgne:** And be like, okay, it looks like we're in week three, looks like you did half of these, and some of these are pending, where are we at with those things?

**William Leborgne:** And then it's super clean, then the experience is like, seamless in my mind.

**Leah Myers:** Yeah, that's completely reasonable, doable ask.

**William Leborgne:** Awesome.

**William Leborgne:** Yeah.

**William Leborgne:** That's what comes to my mind as we're looking at it and talking.

**William Leborgne:** But I think obviously, like, you can ingest this and then just what Ada and myself and Sydney write in your document as, like, things that we want to make sure we have.

**William Leborgne:** Yeah.

**William Leborgne:** The one little nugget, the challenge that you might come across is when you go in linear and you look at, you've probably already done this, but just for, you know, oops, did I close that?

**William Leborgne:** Okay.

**William Leborgne:** I mean, trying to find, am I closing these when I'm, okay, nope, that's not it.

**William Leborgne:** Where?

**William Leborgne:** I feel like I'm closing them instead of opening them.

**William Leborgne:** This is confusing.

**William Leborgne:** Give me a client.

**William Leborgne:** I have too many tasks open.

**William Leborgne:** Here we go.

**William Leborgne:** Well, this is actually not a good one.

**William Leborgne:** There we go.

**William Leborgne:** Okay.

**William Leborgne:** So this is an example of one where we had, there's like so many tasks and you'll see a lot of these are, you have like optional or you have certain things where I'm like, it only happens once in a while.

**William Leborgne:** Um, discuss image preferences, for instance, some of these, like, I don't think we need them.

**William Leborgne:** I guess what I'm getting at is we, there's like, there's going to be a core set of tasks that are needed.

**William Leborgne:** And this is more than that.

**Leah Myers:** Okay.

**William Leborgne:** Like the, the, the, the template that they've built here, I think has more stuff than people actually typically do.

**William Leborgne:** And so it ends up, um, overwhelming you.

**Leah Myers:** Mm-hmm.

**William Leborgne:** Uh,

**William Leborgne:** A good way to exemplify that is, where is my, oh, did I close it?

**William Leborgne:** Yeah, is this, where you're seeing mine are, there's a lot fewer tasks here.

**William Leborgne:** Like by each week, there's a lot fewer tasks.

**William Leborgne:** And obviously this is just the EMs tasks.

**William Leborgne:** But then I also wonder if like, no, that wouldn't work.

**William Leborgne:** We could not.

**William Leborgne:** If there was a filter for, if we could switch between ME and EM tasks.

**Leah Myers:** That would be, that would be badass.

**Leah Myers:** Yeah, we could do that.

**William Leborgne:** Or just tag, yeah, tag the tasks.

**Leah Myers:** Fathom, call out, toggle between EM and ME tasks.

**Leah Myers:** Hopefully it'll catch that in the notes.

**Leah Myers:** Yeah, if you want to, for your requirement gathering, you could literally take a screenshot of like, these are the actual tasks I am paying attention to.

**Leah Myers:** Just screenshot the Trello board and then I'll just write parallel tasks.

**Leah Myers:** Just make it as easy on yourself as possible.

**William Leborgne:** Use the work you've already built.

**Leah Myers:** I can translate it.

**Leah Myers:** Or...

**Leah Myers:** Or I have many AI tools now that can do a lot of work for me.

**William Leborgne:** There you go.

**Leah Myers:** Yeah, this is a super rational way.

**Leah Myers:** I appreciate the way you walk through it.

**Leah Myers:** Yes, just yes.

**Leah Myers:** So drop some stuff in there.

**Leah Myers:** I'm going to use you pinging me and saying, like, I'm comfortable with the amount of requirements I've given you start to work.

**Leah Myers:** And I will use that as, like, my shift into, I'm going to stand this up, okay?

**William Leborgne:** Okay, great.

**William Leborgne:** We'll do that.

**Leah Myers:** Awesome.

**Leah Myers:** Awesome.

**William Leborgne:** Super.

**Leah Myers:** Thank you, William.

**Leah Myers:** I hope that you have a wonderful day.

**William Leborgne:** Thank you.

**Leah Myers:** Thanks.

**Leah Myers:** Bye.

**Leah Myers:** Bye.
