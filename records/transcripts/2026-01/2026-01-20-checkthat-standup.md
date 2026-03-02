# CheckThat Standup

<metadata>
date: 2026-01-20
time: 15:59 UTC
duration: 42 minutes
organizer: Stevie Kim (stevie@growthx.ai)
participants:
  - Marcel Santilli (GrowthX Labs, CEO)
  - Stevie Kim (GrowthX, Lead PM)
  - Jose Farias (GrowthX, Engineer)
  - Pedro Steimbruch (GrowthX, Engineer)
  - Estevão Mascarenhas (GrowthX, Engineer)
  - Daniel Lopes (GrowthX, QA Lead)
  - Jason Gong (GrowthX, Engineer)
fathom_recording_id: 115597160
fathom_url: https://fathom.video/calls/536979071
share_url: https://fathom.video/share/8pqroG4xDM1JEV4UqSaFBPpWhrCSHyih
source: fathom
enriched_on: 2026-02-28 14:30 UTC
</metadata>

---

## Summary

Daily standup to sync on progress, blockers, and launch readiness for CheckThat. The team confirmed all critical blockers are achievable this week. Key work includes fixing UI backfill for competitor changes (Jose), optimizing data handling (Pedro), defining billing MVP with Stripe Checkout (Estevão/Marcel), and improving data integrity validation processes.

---

## Context

CheckThat is preparing for an imminent product launch with a tightly compressed timeline. This standup established a new cadence for synchronization—daily standups with live note-taking to capture action items and critical decisions in a Notion doc, since automated transcripts alone tend to miss nuanced concerns or requirements. Marcel emphasized the need for visual reference points (Linear board) during discussions to maintain clarity on prioritized work. The team is managing overlapping work streams: blocking fixes needed for launch, foundational stabilization post-launch, and parallel infrastructure improvements. Data integrity and UI responsiveness have emerged as key user trust factors.

---

## Relevance

**Product & Development**
- Critical bug fix (Ticket #549) for UI refresh when changing competitors; backfill takes 45-60 seconds with "working on it" UX
- Data latency and integrity concerns: app data is 1-2 days old; need to prevent systemic failures (blank results) that erode trust
- Ticket #549 is multi-part; team needs to break it into smaller tickets for better tracking

**Engineering & Infrastructure**
- Jose monitoring data volume/infrastructure strain from backfill operations; Pedro's snapshotting work has reduced risk
- Pedro adding pagination to Overview page comparators list; implementing Brandfetch colors in charts for visual distinction

**Onboarding & Monetization**
- Estevão progressing on company context and persona generation in onboarding flow
- Billing MVP uses Stripe Checkout (external payment link): Free plan = 14 days history + 50 custom prompts; Pro = 500 custom prompts
- All AI engines available to free users at launch; engine-gating deferred as fast-follow
- Marcel to draft Stripe checkout copy once Stevie provides character limits

**Operations**
- New standup process: live Notion doc to capture action items and key decisions
- Need manual review of key workspaces (Augment, Brax) to surface systemic data issues before launch
- Leo should be added to future standup invites

---

## Overview

- **Critical Bug Fix (Ticket #549):** Jose is fixing a bug where UI updates (e.g., changing competitors) require a manual refresh. The fix, due today, will show a "working on it" message during the 45–60 second data backfill.
- **Probing Data Integrity:** The team will defer a full retry/validation system for launch. Instead, the immediate focus is on preventing systemic data failures (e.g., blank results from core services) that erode user trust.
- **Billing MVP Defined:** The launch MVP will use Stripe Checkout for a simple payment link experience. Free plan limits are set at 14 days of data history and 50 custom prompts.
- **New Standup Process:** A live Notion doc will be used to capture action items and key decisions, ensuring critical points are not lost in automated transcripts.

---

## Key Topics

### Standup Process & Note-Taking

  - **Goal:** Use standups for quick status updates and surfacing blockers, not for deep problem-solving.
  - **Action Items:** Must be captured live in a Notion doc to avoid losing critical information from automated transcripts.

### Data Integrity & Probing

  - **Problem:** Systemic data failures (e.g., blank results from core services like ChatGPT) erode user trust by showing impossible or incorrect data.
  - **Solution:** Defer a full retry/validation system for launch. The immediate priority is preventing systemic failures.
      - **Action:** Create a ticket for a manual review of key workspaces (Augment, Brax) to find and report systemic data issues.
  - **Data Latency:** The app's data is based on yesterday's probes, with a potential 2-day delay during the Europe morning.
      - **Action:** Improve UI/UX to clearly communicate this data latency to users.

### Ticket \#549: UI Refresh Bug

  - **Problem:** Ticket \#549 is a complex, multi-part bug causing UI updates to require a manual refresh.
  - **Fix (Jose):** A backfill process will run when users change competitors, taking 45–60 seconds. A "working on it" message will be displayed during this time.
  - **Action:** Break Ticket \#549 into smaller, more manageable tickets.

### Development Updates

  - **Jose:**
      - **Completed:** Backfill plumbing for UI updates.
      - **Concern:** Infrastructure strain from data volume. Pedro's recent work on snapshotting has reduced this risk, but Jose will monitor it.
  - **Pedro:**
      - **Completed:** Snapshotting optimization and prompt refactor.
      - **Next:** Add pagination to the Overview page's comparators list.
      - **Action:** Create a ticket to implement Brandfetch colors in charts, which is a key visual improvement for readability.
  - **Estevão:**
      - **Completed:** Competitor suggestion logic improvements.
      - **In Progress:** Company context and persona generation in the onboarding flow.
      - **Next:** Draft the Billing RFC.
          - **Reference:** Use the simple payment link experience from `mentions.so` as a model for the MVP.

### Billing & Monetization

  - **MVP Plan:** Use Stripe Checkout for a simple, external payment link experience.
  - **Free Plan Limits:**
      - 14 days of data history.
      - 50 custom prompts.
  - **Pro Plan:** 500 custom prompts.
  - **Engine Access:** All engines will be available to free users at launch to simplify execution. Engine-gating will be a fast-follow feature.
  - **Action:** Marcel will provide copy for the Stripe checkout page once Stevie provides character limits.

---

## Action Items

**Stevie Kim (GrowthX, PM)**
- Create Notion doc for standup notes; share w/ team
- Create Linear issue: validate probes/prompts across key workspaces w/ Leo
- Send Stripe Checkout copy constraints to Marcel; Marcel drafts copy
- Add Leo to future standup invites

**Jose Farias (GrowthX, Engineer)**
- Break out ticket #549 into smaller tickets
- Raise data-volume/infra concerns in tomorrow's standup

**Estevão Mascarenhas (GrowthX, Engineer)**
- Create Linear issue: use Brandfetch colors in charts
- Review mentions.so billing flow; draft RFC for billing

**Marcel Santilli (GrowthX Labs, CEO)**
- Provide copy for Stripe checkout page (pending character limits from Stevie)

---

## Transcript
**Marcel Santilli:** Thank you.

**Marcel Santilli:** What's up, everyone?

**Stevie Kim:** Good morning.

**Stevie Kim:** Good morning.

**Marcel Santilli:** All right.

**Stevie Kim:** I can kick off just to quickly give a status update on what I'm working on.

**Marcel Santilli:** Can we make sure we're capturing action items? We don't want to just talk for 15 minutes and forget what we said.

**Marcel Santilli:** The goal is to have a quick daily sync. We're not problem-solving on this call—mostly surfacing what we worked on, what we're working on, and any blockers or priorities. We can take deeper discussion offline as needed. There are so many Slack threads with important discussions, and it's easy to lose context, so we need to capture the key points.

**Marcel Santilli:** I figured we have enough note-takers here that we probably don't need to take handwritten notes. But if you'd rather have that, I can create a doc. It's mostly so that tomorrow, we're not going to send out an entire transcript for everybody to read. Where are you going to put the notes?

**Marcel Santilli:** So every day we just have action items.

**Marcel Santilli:** Everybody that has a note-taker should have the action items. But automated action items aren't going to be as accurate.

**Marcel Santilli:** Like, if you ever open Fireflies and look at the action items, there's like 50 action items, right? It's mostly just a curated version of what comes out of the standups.

**Stevie Kim:** Okay, that's totally fair.

**Stevie Kim:** I'll create an ocean doc right now so someone else can start.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** Awesome.

**Marcel Santilli:** Let's go around.

**Marcel Santilli:** Jose, want to kick us off?

**Jose Farias:** Sure. We've been having some discussions on the blockers.

**Jose Farias:** We all three have tickets assigned. One limitation of Linear is that Pedro and I have been working on a complicated, all-encompassing ticket with multiple things on it. I think we should break that into smaller tickets for better tracking.

**Jose Farias:** We have tickets segmented into blockers, stabilizing, parallel work, and post-launch. Looking at the Linear board, I don't see anything we shouldn't be able to accomplish this week. Feel free to fact-check me on that, Pedro.

**Jose Farias:** I can go into specific updates if anything specific is on your mind, Marcel.

**Marcel Santilli:** The main thing is working or referencing what we have in the QA plan that Daniel put together.

**Jose Farias:** Let me open that because I was looking at the linear board.

**Pedro Steimbruch:** I think the linear board is kind of truthful to the plan.

**Marcel Santilli:** Or we can open the linear board then, Stevie, can you share your screen maybe on that?

**Marcel Santilli:** And then we can look at the linear board together.

**Marcel Santilli:** That way I'm just like a visual person.

**Marcel Santilli:** I need a visual reference. If I'm not looking at something while we're talking, my brain doesn't work as well.

**Stevie Kim:** So I had it open, but then I was creating the Notion doc.

**Stevie Kim:** And so now I'm trying to find the linear board again because that's what I was going to use.

**Stevie Kim:** But I have the...

**Jose Farias:** I can share.

**Jose Farias:** I have it open.

**Jose Farias:** Okay.

**Jose Farias:** So this is, like, let's start here.

**Stevie Kim:** so wait, do we want to go through the linear board?

**Stevie Kim:** Because I was going to actually, sorry, actually, I was going to go through the Notion doc because Daniel put that together with the launch plan and it's got, I, okay, this isn't, this isn't turning into a normal standout, but it's going up there else.

**Stevie Kim:** But anyway, so the launch plan, I added a column to just, so we can see the status of these different tickets that Daniel put in.

**Stevie Kim:** So we could, I figured we could go through that, but I thought we were going to do this in the later meeting today.

**Stevie Kim:** I thought this was just going to be a traditional, like, standups, like, status, update, blockers, and so on and so forth.

**Marcel Santilli:** Yeah, exactly. We should reference the actual work we're doing, not just talk abstractly. I need a visual reference point versus just effort estimates.

**Marcel Santilli:** My brain doesn't work well without seeing something. I can't just listen for 15 minutes. I need to know what everyone is looking at and working on each day so we can frame the standup around that.

**Marcel Santilli:** I'm going to try to pay attention and take notes. I'm not great at multitasking.

**Stevie Kim:** I usually take the, the, the notes from the note takers and condense them, but I'm going to try to do it live.

**Marcel Santilli:** So forgive me if look like.

**Stevie Kim:** I throw you off here.

**Marcel Santilli:** Like, if Jose says, "I'm really concerned about XYZ about this task," and we just talk without noting it, we might miss it when reviewing the transcript later. And if it's a critical point, we don't want that to get dropped.

**Marcel Santilli:** So the note-taking isn't to transcribe what we're saying verbatim. It's to flag important points someone mentions so we capture them, because there's so much going on leading up to launch.

**Stevie Kim:** Oh, wasn't planning on that anyway. I'm not that good of a touch typer.

**Stevie Kim:** I'm good, but not that good.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Okay.

**Stevie Kim:** I'm actually just going to take handwritten notes because I'm sure it's great.

**Marcel Santilli:** Jose, so is this roughly or in linear, what's the view that you and team are kind of like looking at mostly?

**Jose Farias:** It matches this.

**Jose Farias:** I don't know if much is exactly, but looking at the top tickets, that is what we're working on.

**Jose Farias:** So I guess we can just start talking about them top to bottom.

**Jose Farias:** The second item, Navan competitor visibility, is complex because there are multiple bugs. I've been working on the main issue: we need to backfill data when you change competitors, since the visibility data changes when tracking different things.

**Jose Farias:** We're doing that now. It takes 45 seconds to a minute, and we show a "working on it, we're backfilling" screen during that time.

**Marcel Santilli:** So the competitors in the watch list are always evolving. When that changes, you need to backfill data to recompute all the charts.

**Jose Farias:** Right, only when you choose to follow different competitors. In the competitors tab, you can change which companies you're tracking. We backfill the new snapshots for the other company.

**Pedro Steimbruch:** The main impact is in the overview.

**Pedro Steimbruch:** So, okay, cool.

**Jose Farias:** Does this also capture the issue where you add new prompts but don't see them in the counter? That's another part of this ticket. What's displayed in the prompt counter is how many prompts we have data for, not how many you've added. We might need to adjust the copy or change what's displayed.

**Stevie Kim:** So that's the mismatch, right?

**Jose Farias:** Yeah, you might be expecting to see all the prompts you've added, but we haven't probed them yet. That's another ticket—we need to probe immediately after adding new prompts.

**Marcel Santilli:** But those are custom probes, right?

**Marcel Santilli:** Like, that shouldn't happen with, like, if you go into the share library and do that, right?

**Jose Farias:** Right.

**Jose Farias:** I don't think you should check.

**Jose Farias:** If it does happen, then that's a bug.

**Jose Farias:** Like, we have some, yeah, we need to do some QA there.

**Marcel Santilli:** To me, the core flow here, right, like, that for launches the magical experience is you, like, log in and you see, like, 8,000 probes, right?

**Marcel Santilli:** Like, after you set up everything, you know, and it's just like, whoa, this is amazing, right?

**Marcel Santilli:** And then you go into the prompts field ground, and it's pretty, you know, although, like, it might not be perfectly intuitive day zero, but it's like you can deactivate a prompt that's like, you know, this one is not super relevant, and go into the share library and add a few more from the share library.

**Marcel Santilli:** Ideally, and within a reasonable number of seconds, not zero, but also not five minutes, you see things update, right?

**Marcel Santilli:** And as long as we let users know somehow that things are running or things are updating, and until then, they don't see anything either completely broken or blank or just off, then they won't have the experience that every other app gives them, which is like blank, right?

**Marcel Santilli:** Then for the, anytime they add new, like a new prompt, then what other apps do is they try to as quickly as humanly possible probe it, right?

**Marcel Santilli:** And, but that's a separate, a separate thing, you know, and, and later on, like, as we, later on, can figure out where are the places.

**Marcel Santilli:** As well.

**Marcel Santilli:** Where these things can happen where like you just edit a probe and like instead of showing it as broken or blank, there should be like a message like, hey, we're capturing or like places where we can kind of like let users know we're working on it and they're going to be completely okay with it.

**Marcel Santilli:** But it's just like looking at a blank and not having a status of working, then just seems like it might be broken or not working and then they keep refreshing it, right?

**Jose Farias:** Right.

**Jose Farias:** Right.

**Jose Farias:** So the work that is almost wrapped up is having the plumbing to basically do that exactly.

**Jose Farias:** And I do expect that for later today, we would have every single place that we need to backfill covered.

**Jose Farias:** Essentially, you added a prompt, we show you, hey, we're working on it for a couple seconds and then you're good.

**Jose Farias:** Like you can see the prompt and its history there.

**Jose Farias:** Same for changing your competitors and same for creating a new account, both from the onboarding experience and from the admin panel.

**Jose Farias:** So that's what I'm working on in terms of like the standard stand up when I'm working.

**Jose Farias:** That's what I've been working on yesterday.

**Jose Farias:** I plan to wrap it up today.

**Jose Farias:** I'm personally not blocked, and I do think I should call out that that ticket wrote to, that ticket 549, contains a couple of things.

**Jose Farias:** So there's another one that Stevie might be thinking about already, which is changing your workspace requires a refresh to see the new information.

**Jose Farias:** That's definitely a bug.

**Jose Farias:** Yeah, we need to break that out into, like, multiple tiny tickets.

**Jose Farias:** I don't think any of them are particularly complex.

**Jose Farias:** It's just worth calling out, because that ticket seems like one thing, but it's actually, like, five.

**Marcel Santilli:** Cool.

**Marcel Santilli:** As far as your, what you're working on, is there anything you're working on blocking anybody else from progressing, or?

**Jose Farias:** Um, Pedrans, Tomon, in check me on this.

**Jose Farias:** I don't think I'm blocking anyone.

**Jose Farias:** The one thing that's, that's worth calling out is, uh, other people not on, on this call might be surprised, like, oh, I added a prompt, there's no data.

**Jose Farias:** Like, I'm...

**Jose Farias:** And that's exactly what I'm working on.

**Marcel Santilli:** So don't panic.

**Marcel Santilli:** We'll have it fixed today.

**Jose Farias:** Yeah.

**Marcel Santilli:** If you don't mind, I don't know if you've done that already on the ask, check that.

**Stevie Kim:** I'm in there all day, all the time.

**Stevie Kim:** That's where this ticket came from.

**Stevie Kim:** 549.

**Marcel Santilli:** Or if people start asking too much, it's just mostly like we can just post something there saying, hey, for the next 24, 48 hours, you should expect this, this, this, and this that we're working on.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Just as a forewarning.

**Marcel Santilli:** I've been doing that.

**Stevie Kim:** Yeah.

**Stevie Kim:** For, for all these, you know, things that I know are in flight.

**Marcel Santilli:** Awesome.

**Marcel Santilli:** Any, any other blockers or anything that's slowing you down?

**Jose Farias:** Just one thing comes to mind, which is we, this was, this is a recent development.

**Jose Farias:** I was, I used to be quite worried about the infrastructure strain that we could incur from the data volume.

**Jose Farias:** This, this just changed today because Petra and I worked on, it was mostly.

**Jose Farias:** Pedro, but I reviewed the PR, worked on snapshotting less as a side effect of other things that were going on.

**Jose Farias:** So I'm not as worried today, but this is so recent that I need to do some more thinking on this and bring it up again tomorrow.

**Jose Farias:** So that's just what I'm thinking.

**Jose Farias:** Thankfully, it doesn't seem like it's going to be a problem.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Do you think it's important post-launch for us to kind of think through like, what are the areas that could potentially cause downtime or broken experiences for users that if we decide we want to touch that, like, how do we do it in a way that's the least disruptive possible, you know, but we don't need to spend too much, too many mental cycles now.

**Marcel Santilli:** But certainly it's like, if, like, we have this tiny window of like, if you find out something now, there's less people.

**Marcel Santilli:** They're mostly just going bug us and Stevie on the Ask, check that, but pretty soon then there's going to be potential SLAs and things with paid accounts, but all good.

**Jose Farias:** I have documented the three things that I think, if anything went south regarding data volume, it would be one of those three things.

**Jose Farias:** The one thing that could trigger that early on is going viral, right?

**Jose Farias:** So, I don't think it's going to be a problem, especially after Pedro's work.

**Jose Farias:** But again, let me bring it up again tomorrow.

**Jose Farias:** Sounds good.

**Marcel Santilli:** Pedro?

**Pedro Steimbruch:** Yeah, so I finished this snapshot thing and the prompt refactor to be based on actual prompt mentioned brands and not comparers.

**Pedro Steimbruch:** Now, I need to pick something else to work on, and I have a few things on my plate already, so I will probably...

**Pedro Steimbruch:** Add pagination to the overview, comparators list in the overview, but there are a few others that I could tackle too.

**Pedro Steimbruch:** I know we have...

**Marcel Santilli:** pagination, I don't want to add scope, but just so I understand, like, I remember, I think Estevão's view, like, with the brand fetch colors matching in the graphs, like, where is that?

**Marcel Santilli:** I just want to make sure it doesn't get lost.

**Marcel Santilli:** We don't need to add scope, but I want to make it look like it was done at some point, but then never got implemented, so I wasn't sure, like, what happened to it.

**Pedro Steimbruch:** This was done in the public page, the leaderboard.

**Pedro Steimbruch:** This was done by Estevão.

**Pedro Steimbruch:** Correct if I'm wrong, Estevão.

**Pedro Steimbruch:** Oh, yeah, that's correct, but not the brand colors.

**Estevão Mascarenhas:** We didn't do that yet.

**Estevão Mascarenhas:** I don't think we have an issue for that.

**Estevão Mascarenhas:** We should probably do it.

**Estevão Mascarenhas:** I can create one now.

**Estevão Mascarenhas:** So, basically, we didn't have a brand fetch account until, like, two weeks ago.

**Estevão Mascarenhas:** Now we have, and we have access to their API.

**Estevão Mascarenhas:** it's...

**Estevão Mascarenhas:** should be easy to attach a color to the brand and we show it in the chart, but it's not done yet.

**Marcel Santilli:** Okay, if we can track this issue, I don't want to scope to anything.

**Marcel Santilli:** This is one of those that visually outside of pagination, it's very, very hard to make sense of the charts because it's just like random colors.

**Marcel Santilli:** And then you look to the right, it's the random logos and you can't possibly know which belongs to which.

**Marcel Santilli:** So you have to like hover over and then look over and then look over here and then like, you know, not a blocker, but it was, I just want to make sure we're tracking so that that doesn't get lost through the cracks, if you will, you know.

**Pedro Steimbruch:** There is one more issue that I could also, that's on my plate for a while now, that's about probing as soon as the custom prompt is created.

**Pedro Steimbruch:** But I would have to sync with Jose for doing that because I don't think it's easy as just probing it because the user can now.

**Pedro Steimbruch:** Add 200 prompts at once.

**Pedro Steimbruch:** And then we have batches for the, for library, for, for, for, for doing regular probes, right?

**Pedro Steimbruch:** We are probing in a 12 hours window, I think, and do it in batches.

**Pedro Steimbruch:** So there is some magic case, like adding a prompt during the, the window.

**Pedro Steimbruch:** Does it make sense to probe it right away?

**Pedro Steimbruch:** We need to, to understand how the screens will change, because today the overview is only based on yesterday's probes, and we are probing today.

**Pedro Steimbruch:** This won't affect the overview as it is today, so we need to think about that too.

**Jose Farias:** I think we need to be very practical about that, because if we start solving for all the edge cases, we're never going to finish that.

**Jose Farias:** But you raised some good points.

**Jose Farias:** I think the answer is, when you add a prompt, we probe it.

**Jose Farias:** Immediately, we don't consider it for any aggregated views, essentially.

**Jose Farias:** So it won't be materialized into the overview, won't be materialized into subcategory leaderboards or anything like that.

**Jose Farias:** We will just do enough work to show you the prompt show page, essentially.

**Jose Farias:** And that's it.

**Jose Farias:** And then, just to be thorough, I did assign that ticket to myself.

**Jose Farias:** Feel free to pick it up if you free up.

**Jose Farias:** It's just that I have some ideas there, but we can sync.

**Jose Farias:** If it comes to your next, to when you're ready to pick a next ticket, we can sync on it.

**Marcel Santilli:** So just so I lay back so I understand, right now, everything you see in the app is like yesterday and backwards.

**Marcel Santilli:** Yep.

**Marcel Santilli:** So almost no action that happens, unless it's adding things that have data for that time period, will have any impact whatsoever on any charts.

**Marcel Santilli:** that's So

**Marcel Santilli:** I need summarized or computed data and charts, right?

**Marcel Santilli:** And did I understand that correctly?

**Marcel Santilli:** Yes.

**Jose Farias:** Okay.

**Marcel Santilli:** That's completely okay and acceptable.

**Marcel Santilli:** And actually, like, it's a behavior that's common, like, Search Console.

**Marcel Santilli:** Analytics is just more real-time and people expect real-time.

**Marcel Santilli:** With this, like, it's more of, like, how do we set that expectation?

**Marcel Santilli:** Because it's not super clear when we say, like, last seven days that it's, like, not include today.

**Marcel Santilli:** You know?

**Marcel Santilli:** And so later on, we'll just need to – that's just a UX, UI issue of, like, how do we communicate to the users?

**Marcel Santilli:** Like, GSC sometimes is three days behind if you put last seven days.

**Marcel Santilli:** You know?

**Marcel Santilli:** Like, and so – but it's super clear on the charts that that date start, like, ends, like, you know, two days ago.

**Marcel Santilli:** And so, yeah.

**Marcel Santilli:** On that note, like, if we do what you're saying, Jose, I think that makes a lot of sense.

**Marcel Santilli:** It would be cool.

**Marcel Santilli:** If we also have a state in the table that shows that this got probed and it will be calculated tomorrow.

**Marcel Santilli:** So maybe a UI state that displays that is, we got the data and it's going to be aggregated tomorrow.

**Pedro Steimbruch:** Because there is one more caveat still is that if it's not, if today we haven't yet calculated snapshots for yesterday, we are still showing two days behind, right, Jose?

**Pedro Steimbruch:** It's not just yesterday.

**Jose Farias:** It depends.

**Jose Farias:** It should be.

**Jose Farias:** It depends on whether we've captured the snapshots for yesterday already.

**Jose Farias:** if we haven't, there's a period of time mostly in the Europe morning where we're two days behind.

**Marcel Santilli:** Yeah, that's what I, yeah.

**Marcel Santilli:** The data not biased towards the hour of the day.

**Marcel Santilli:** Got it.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** It's 12 hours.

**Marcel Santilli:** The main thing that I know it's somewhat unrelated here.

**Marcel Santilli:** It's like, it's okay that we're like probing throughout the day and whatever.

**Marcel Santilli:** As long as we're super, super consistent.

**Marcel Santilli:** We when a day starts and when a day ends type of thing, right?

**Jose Farias:** We are.

**Marcel Santilli:** And then like we communicate what we're doing.

**Marcel Santilli:** I think the situations we're seeing before where that can look a little bit confusing is, for instance, like we add a new service to a probe or to a prompt.

**Marcel Santilli:** And it's kind of unclear in the prompt detail, like how we're calculating things because there might be blanks.

**Marcel Santilli:** And then there's also sometimes the errors.

**Marcel Santilli:** And so then the errors, like I'll give you a very clear example with augment code, right?

**Marcel Santilli:** If there's a prompt that says, is augment code a good platform?

**Marcel Santilli:** Like I'll just give an example, but it's clearly like it's going to mention augment code.

**Marcel Santilli:** So then the expectation is like when you go into any branded prompt and you click on it and you see like a bunch of things that says no brand mentions, you're like, wait, that is physical.

**Marcel Santilli:** It's physically impossible that it won't mention the brand, right?

**Marcel Santilli:** And then when you click into it, it's usually like some kind of error or some kind of thing that says, sorry, I can't answer that.

**Marcel Santilli:** Because it's like we're using Meany for JudgePT, and then for others, like it's returning an error or something else, you know?

**Marcel Santilli:** And then that's messing up the data.

**Marcel Santilli:** So those are the edge cases on probing that are more important for us to address are the things that break trust, right?

**Marcel Santilli:** Like a thing that's like this, I'm clearly expecting this, and then when I drill down, I see not that, right?

**Marcel Santilli:** And so, yeah, like for instance, like, and I don't think I made it clear on that one ticket I submitted on the augment code, but it's like if we, like if they see, for example, like two out of 10 probes in one of the services, like failing or clearly being wrong because of that, then it's really bad.

**Marcel Santilli:** It's almost better to not show the row at all.

**Marcel Santilli:** You know, so that there might be some minor level of like filtering when we're probing or validation, if you will, or unit tests, basics, you know, or at least some kind of trigger that causes like a human review queue at some point, because it's really bad when it happens, because we're just showing them everything.

**Marcel Santilli:** And then they're like, oh, wow, their system sucks.

**Marcel Santilli:** You know, like, I don't remember seeing that in the shortlist for launch.

**Jose Farias:** Is it?

**Marcel Santilli:** Does someone else remember?

**Marcel Santilli:** No, I don't think it is.

**Marcel Santilli:** think we should have.

**Marcel Santilli:** Okay.

**Jose Farias:** Yeah.

**Jose Farias:** Yeah.

**Marcel Santilli:** Okay.

**Marcel Santilli:** It's good to have it on the radar then, but yeah.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Is even a ticket for that?

**Stevie Kim:** No.

**Marcel Santilli:** I don't, I don't think so, but I can show, so sorry, let me, I have way too many  screens, but I'll, I'll share a, an example here.

**Marcel Santilli:** Give me two seconds.

**Marcel Santilli:** Can you take note of that, Stevie?

**Stevie Kim:** Yeah, I'm taking it out right now.

**Stevie Kim:** now.

**Stevie Kim:** Create a ticket for it.

**Marcel Santilli:** Yeah, because I think what I saw, like, with Augment Code that was, like, really tricky was that, like, I was demoing Augment Code, and then Augment Code just looked, like, insanely more visible than everything else.

**Marcel Santilli:** And part of the reason was because whoever's managing this added, like, literally, like, 700, and, like, half of these are, like, branded, and it's just, like,  up everything, right?

**Marcel Santilli:** Right.

**Marcel Santilli:** But it was one of those where, yeah, where...

**Marcel Santilli:** We should probably put that in the list for Leo to, like, go to all the workspace and look for things that doesn't make sense, because I think he might be doing it from scratch.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah, like, things like this, you see?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Like, there's a lot of blanks.

**Pedro Steimbruch:** I've seen, yeah, I've seen a few blanks for Google AI overview specifically, and I have a ticket for investigating that.

**Pedro Steimbruch:** Okay.

**Pedro Steimbruch:** Yeah.

**Marcel Santilli:** And so I don't know if there's like a way.

**Stevie Kim:** Did you want to share your screen, Marcel?

**Marcel Santilli:** Oh, can you guys not see my screen?

**Pedro Steimbruch:** Oh, sorry.

**Stevie Kim:** I forget about the tabs, so.

**Stevie Kim:** Oh, okay.

**Marcel Santilli:** Yeah, I'm not seeing the example, but there was a couple where it wasn't just blank.

**Marcel Santilli:** It was actually like an error.

**Marcel Santilli:** And it was like a standard response.

**Marcel Santilli:** That gesture can't that.

**Marcel Santilli:** Can you answer that, Marcel?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And it was 5.2 mini.

**Pedro Steimbruch:** There is one without mention there.

**Pedro Steimbruch:** There is one without mention there.

**Pedro Steimbruch:** the first, right there, January 16th for Cloud.

**Pedro Steimbruch:** Which is, yeah, no mentions.

**Pedro Steimbruch:** Augment.

**Pedro Steimbruch:** Oh, it's mentioned as Augment only.

**Pedro Steimbruch:** Look at the right side.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** It's a different brand.

**Pedro Steimbruch:** Yeah.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** So, so anyways, like there's some of those that like, now we have enough data between the workspaces that, that I think will be.

**Marcel Santilli:** see.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Okay.

**Marcel Santilli:** But with the probes, some level of it is acceptable, but on the core services, for instance, what I would expect in a case, let's say, if we look at ChatGPT as an engine, and we look at the probes and see if there's any issues, and if we see consistent issues popping up, just like we need to kind of investigate.

**Marcel Santilli:** But then also have triggers that if it fails, or certain words are contained in it that are not the expected answer, to retry a few times, and then if it fails again, then there's like, hey, this probe fail, and there's like, just like with Sentry array, like, hey, there's like something.

**Marcel Santilli:** I think that it does make sense.

**Marcel Santilli:** I think we basically need a mini-e eval inside the probing system, but I think I'm also going to have to try to migrate our entire ChatGPT to the output framework this week.

**Marcel Santilli:** Okay, so we can do like, adding changes to the...

**Marcel Santilli:** Okay.

**Marcel Santilli:** To the workflows now would be better to wait a bit.

**Marcel Santilli:** So, like, if we could just, like, I think, like, some of the things that we're talking about, it sucks, but we can ship without it.

**Marcel Santilli:** Yeah, yeah, I agree.

**Marcel Santilli:** So, those are the things that we really need to focus, like, heavy on the first, right after.

**Marcel Santilli:** But now as well, that's the time to try to solve it.

**Marcel Santilli:** Well, I'm more worried on, like, consistent blanks or consistent, like, things erring, like, entire services for, like, most accounts where every single user is going to see it if they drill down.

**Marcel Santilli:** It's more of that than, like, the trigger system or the retry system.

**Marcel Santilli:** It's more of, like, systemic, like, issues with the probe data because it looks really bad when one of the core services, like, ChadDPT, is going to have, like, blanks for a bunch of dates.

**Marcel Santilli:** And, you know, that's going to just look bad, you know?

**Marcel Santilli:** And so, those are the ones that, like, if we can't recover the data, if it's just, like, a show, like, the way we're showing is showing blank for whatever reason.

**Marcel Santilli:** And that's a, you know, fixable bug.

**Marcel Santilli:** That's fine.

**Marcel Santilli:** But if it's like, we don't have the data or we have a bunch of error data systemically happening, then those, we can't go back in time, you know?

**Marcel Santilli:** So that's the ones I worry more about, you know?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** No, I agree.

**Marcel Santilli:** And I think even like that case of the augment that just showed, that sucks, but it's not that bad compared to what you're saying.

**Marcel Santilli:** Like what you're saying.

**Marcel Santilli:** But if all chat to BT is blank or all AI overview is blank and then we keep tracking data.

**Marcel Santilli:** And then a month in, it's like, sorry, I can't even tell you how you're doing.

**Marcel Santilli:** yeah.

**Marcel Santilli:** No, that's a major problem.

**Marcel Santilli:** I think like we need to, like Stevie, like if we can work with Leo to like go through some of our existing accounts and try to actually make sense of everything to uncover things like this, you know?

**Marcel Santilli:** Yeah.

**Stevie Kim:** So what should the ticket be focused on then since there seems to be a few different things that we're talking about?

**Marcel Santilli:** Validating across workspaces that...

**Marcel Santilli:** So that probes or prompts are, you know, are like showing and probing correctly for the most part, you know, like meaning like go through some of our important workspaces like Augment, Brax, a few others that seem to have activity and the ones that have more custom prompts and look through and kind of like take a...

**Marcel Santilli:** Yeah, it's mostly like you're inspecting to find any issues that seem systemic, you know?

**Marcel Santilli:** Yeah, it seems systemic and there's small ones too.

**Marcel Santilli:** Like this Augment one should be the bug.

**Marcel Santilli:** Like if Leo was clicking around, then he should fire that as a bug.

**Marcel Santilli:** It's not a super high priority bug, but it's a bug.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Awesome.

**Marcel Santilli:** Estevão, like just to keep us on time because I got to wrap here, but do you want to do just a quick update if any blockers or things are logging it down?

**Estevão Mascarenhas:** Yeah, sure.

**Estevão Mascarenhas:** So yesterday, I think...

**Estevão Mascarenhas:** I wrapped the competitors' work, so I checked multiple workspaces for the brands that I know and I was aware, and the competitor's suggestion I think is much better now, but if someone else, I don't know myself if you have time, or Stevie, can take a look at other workspaces just to make sure that we don't have anything spotting wrong there.

**Estevão Mascarenhas:** So now I'm back to getting the company context and the personas generation from the onboarding flow.

**Estevão Mascarenhas:** That's the last part that I paused on Friday.

**Estevão Mascarenhas:** So I'm wrapping up today, and then I will work on the draft for the RFC to billing.

**Estevão Mascarenhas:** So my plan is to output this RFC so you guys can take a look, at least Jose, if you can take a look on that.

**Estevão Mascarenhas:** Meanwhile, like while someone else reveals it, I will keep polishing the onboarding.

**Estevão Mascarenhas:** I don't think we have any bugs, major bugs there, but I will keep polishing, and then I will switch to start working on billing.

**Estevão Mascarenhas:** At least that's...

**Marcel Santilli:** Link site, like, check out mentions.so, because they're the, like, most scrappy one of the bunches that actually have a pretty good experience.

**Marcel Santilli:** They're, it's like this group of people, they own, like, Contact Studio, which is a content agency, and then they have three other SES, and this is one of the SES that they have.

**Marcel Santilli:** They're doing, like, 60K and MRR already on it, like, so they're, like, the closest to what we're doing, essentially, of, like, not being VC funded and just, like, and so I would just take a look at how they do billing, because it's very much just, like, the payment link, and then it redirects you back when you're done.

**Marcel Santilli:** And so it's, like, super simple, like, I couldn't, I just, just to make sure, like, you're using that as a reference, you know, as the, here's a super simple, fast implementation version of it, because that's one of the benefits with, with Stripes.

**Marcel Santilli:** It's, like, you can fully integrate and have everything native, but a lot of the competitors that I looked at is just, like, a link that takes you to the, to.

**Marcel Santilli:** The, you know, Stripe version of that page.

**Marcel Santilli:** Like, you know, nothing loads in the ‑‑ If we do that for the control panel, there are still, like, that we're probably going to have to handle to webhooks.

**Marcel Santilli:** Like, if somebody opens a subscription account and cancel, we need to get notified through a webhook that the account is turned off.

**Marcel Santilli:** But there are things like that.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** It's that Stripe control panel that we should enter.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Just look at that experience that way when you're writing that RFC.

**Marcel Santilli:** Like, use that as a reference.

**Marcel Santilli:** Because that seems like a pretty standard, like, way where, you know, like, cool.

**Marcel Santilli:** Anything you're blocked on?

**Marcel Santilli:** No, no.

**Estevão Mascarenhas:** Awesome.

**Estevão Mascarenhas:** I just wanted to give a quick status update because I might be blocking people.

**Stevie Kim:** So, as far as the Stripe account setup, I did, you know, the, I would say, bare bones setup.

**Stevie Kim:** I did have some questions.

**Stevie Kim:** I put in Slack over the weekend.

**Stevie Kim:** I'll take a look at see if those aren't answered.

**Stevie Kim:** But I want to make sure that I'm not blocking anyone from doing what they need to do on the back end.

**Stevie Kim:** I did set up the sandbox.

**Stevie Kim:** So, you know, that can be used to test those web hooks and stuff.

**Stevie Kim:** But I did have a question kind of about how much I wasn't sure if we were going to put the exact, like, bullet points of what features are in one tier versus the other.

**Stevie Kim:** Or if we wanted to just have a general description of that.

**Stevie Kim:** So I didn't know how granular we wanted to have that because we did decide to use, like, the Stripe.

**Marcel Santilli:** Yeah, the core thing here, right, is 14 days.

**Marcel Santilli:** Anything past 14 days, the free version should not have, right?

**Marcel Santilli:** And the easiest way to...

**Marcel Santilli:** Implement that.

**Marcel Santilli:** Again, not a blocker to launch, but it's like, it should be a very fast follow.

**Marcel Santilli:** But ideally, it's very similar to like Crunchbase and others, where everywhere that filter is, there's a lock button.

**Marcel Santilli:** And if you click that lock button, it takes you to the upgrade, you know, screen.

**Marcel Santilli:** And so that's one.

**Marcel Santilli:** And then the second one is around how many custom prompts.

**Marcel Santilli:** And so in my original prototype, I don't know if y'all remember, there was like a place at the top, close to where the filters are, that was constantly showing you like how many custom prompts you were using and how many you had.

**Marcel Santilli:** That's the simplest way to do it.

**Marcel Santilli:** That's how Peak AI does it and a few others.

**Marcel Santilli:** And again, like that is not a blocker to launch either.

**Marcel Santilli:** But so the MVP here is for us to communicate those things, which is in the pricing and monetization doc.

**Marcel Santilli:** And even if at first, like we don't have a lot of like upgrade triggers everywhere.

**Marcel Santilli:** Just have it there and putting some limits behind the scenes.

**Marcel Santilli:** And then later on, we can have a better way to communicate where those two things are.

**Marcel Santilli:** There are more features, but some of the ones that I had put in the free versus pro are not yet live or might not be relevant quite yet.

**Marcel Santilli:** Those are the two main ones.

**Marcel Santilli:** So free is 14 days and 50 prompts with all engines. Pro is 500 prompts. Ideally, we reserve some engine for pro only. But to simplify execution, let's just give all engines to free users now and remove them later for the free plan. The critical blocker is not letting people add more than 50 prompts—that we need to enforce now.

**Jose Farias:** We have that enforced on the back end.

**Stevie Kim:** I was more talking about the front end—what users see in the Stripe checkout.

**Marcel Santilli:** I have some copy in the monetization prototype I can adapt. If you give me a placeholder with character limits and screen specs, I can work on the copy for that.

**Marcel Santilli:** There's copy in the onboarding and signup doc in Notion I can adapt. Stripe is limited in what you can display—no free-form text or tables, just a short description with maybe bullets. It's a mini elevator pitch. You don't want to overwhelm people, just give them the value prop and get them to checkout.

**Stevie Kim:** Right, when I was charging for workshops, it was very limited.

**Marcel Santilli:** Can you add Leo to future meetings? He's still involved in this work now. Sorry, that's my bad.

**Stevie Kim:** Got it. Anything else?

**Marcel Santilli:** We can circle back on these at the meeting this afternoon. Thanks, team. Appreciate it.

**All:** Bye.
