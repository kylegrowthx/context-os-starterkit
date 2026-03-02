# Pod F Weekly

<metadata>
date: 2026-01-29
time: 17:00 UTC
duration: 28 minutes
organizer: Katya Luscomb (katya@growthx.ai)
participants:
  - name: Katya Luscomb
    affiliation: GrowthX
    role: Engagement Manager
    email: katya@growthx.ai
  - name: Felix Morgan
    affiliation: GrowthX
    role: Content Producer
    email: felix@growthx.ai
  - name: Simran Sethi
    affiliation: GrowthX
    role: Content Producer
    email: simran@growthx.ai
  - name: Jessalynn (invited, did not attend)
    affiliation: GrowthX
    email: jessalynn@growthx.ai
fathom_recording_id: 118230226
fathom_url: https://fathom.video/calls/548093702
share_url: https://fathom.video/share/gq_5EXc_sGy9MYa-W48Job1kzjiKq7EW
source: fathom
enriched_on: 2026-02-28 15:45 UTC
</metadata>

---

## Summary

Pod F team discussed standardizing Airtable workflows across all client accounts with new required columns (Week, Content Calendar, Sent to Client, In Looker) and automations to streamline reporting. Team members will now own content calendars and contribute 2-week production recaps to client agendas, freeing up Engagement Manager bandwidth. For the "Anything" client scaling project, the team adopted a speed-focused quality standard accepting "good enough" articles since the client publishes without review.

---

## Context

GrowthX's content delivery team operates across multiple client accounts (Udemy, Understory, Monograph, Metronome, "Anything" client). Katya Luscomb, the team's Engagement Manager, identified fragmentation in Airtable workflows across accounts—inconsistent column structures, missing automations, and limited visibility into content pipeline status. This fragmentation created bottlenecks in reporting (Monday updates) and required manual effort to track content across pipeline stages (4 Weeks Out → 3 Weeks Out → 2 Weeks Out → 1 Week Out → Current Week → Shared with Client). Concurrently, the "Anything" client initiated a scaling initiative requiring rapid content production.

The meeting established a new operating model: standardized Airtable structures across all accounts, delegated content calendar ownership to Felix and Simran, and introduced client agenda recaps (2-week production summaries) to improve client visibility and communication efficiency. This shift required team agreement on a tiered quality standard—maintaining baseline standards while deprioritizing perfectionism for clients without approval workflows.

---

## Relevance

- **For content producers (Felix, Simran):** Defines new Airtable structure, ownership of content calendars, and responsibility for 2-week client agenda recaps. Clarifies which views to prioritize and how much customization autonomy they have.
- **For engagement managers:** Establishes a scalable workflow for managing multiple accounts, automating Monday updates, and streamlining client communication. Provides a template (Udemy Airtable) for rolling out to other accounts.
- **For leadership:** Demonstrates delegation strategy freeing up Engagement Manager time and building team autonomy. Shows how process standardization supports both internal efficiency and client experience.
- **For scaling initiatives:** Clarifies the quality-speed tradeoff for high-velocity clients without approval workflows, establishing a realistic minimum bar (headers, CTA placement, fact-check, no jargon).

---

## Overview

- **Airtable Standardization:** Implement a standard Airtable setup across all clients by next Wednesday. This includes new columns (e.g., `Week`, `Sent to Client`) and automations to streamline reporting and improve visibility.
- **New Responsibilities:** Team members will now own their clients' content calendars and contribute 2-week production recaps to client agendas, freeing up Engagement Manager time.
- **"Anything" Content Strategy:** For the "Anything" client, prioritize speed over perfection. A "good enough" standard is acceptable because the client does not review articles before publication.

---

## Key Topics

### Airtable Standardization

  - **Goal:** Create a consistent Airtable structure across all clients to simplify reporting and enable future automation of tasks like Monday updates.
  - **Required Columns:**
      - `Content Calendar`: A single-select field to manage the weekly content pipeline (e.g., `Current Week`, `1 Week Out`).
      - `Week`: A number field to track the week of the engagement (e.g., `Week 20`).
          - **Action:** Backdate this column for all content published since January 1st.
      - `Sent to Client`: A date field (US time zone) that will be populated by an automation.
      - `Current Date`: A hidden formula field (`NOW()`) that triggers the `Sent to Client` automation.
      - `In Looker`: A checkbox to confirm URLs have been added to Looker.
          - **Why:** Ensures performance data is current and enables seamless handoffs during OOO periods.
      - **Optional (for clients with approval workflows):**
          - `Topic Approval`: Single-select field for client feedback (e.g., `Approved`, `Needs Revision`).
          - `Topic Feedback`: Long-text field for client notes.
          - `Article Approval`: Single-select field for client review status.
  - **View Customization:**
      - Team members have full ownership to create personal views that suit their workflow.
      - **Caution:** Do not modify client-facing views.
      - **Recommendation:** Use the Udemy Airtable as a reference for the new setup.

### New Responsibilities & Automation

  - **Content Calendar Ownership:**
      - Team members will now own their clients' content calendars.
      - **Weekly Task:** Select new assignments for the `4 Weeks Out` bucket.
      - **Why:** Provides a clear runway for content planning, enabling proactive keyword research and strategy discussions.
  - **Content Calendar Automation:**
      - A weekly automation (runs Saturdays at midnight PT) will shift content through the pipeline.
      - **Execution Order:** Must run in a specific sequence to prevent errors.
        1.  `4 Weeks Out` → `3 Weeks Out`
        2.  `3 Weeks Out` → `2 Weeks Out`
        3.  `2 Weeks Out` → `1 Week Out`
        4.  `1 Week Out` → `Current Week`
        5.  `Current Week` → `Shared with Client`
  - **"Sent to Client" Automation:**
      - This automation populates the `Sent to Client` date field, providing a clear delivery timestamp for reporting.
      - **Trigger:** Varies by client workflow.
          - **Review Process:** Triggered when status changes to `Ready for Client Review`.
          - **Auto-Publish:** Triggered when status changes to `Published`.
  - **Client Agenda Recaps:**
      - Team members will contribute a 2-week production recap to each client's agenda.
      - **Why:** Provides clients with a summary of recent work and allows for flagging specific articles for discussion.
      - **Deadline:** 12 hours before the client meeting.

### "Anything" Content Production

  - **Strategy:** Prioritize speed and volume over perfection to meet the client's scaling goals.
  - **Rationale:** The client does not review articles before publication, making a "good enough" standard acceptable. Marcel (CEO) has already aligned with the client on scaling expectations.
  - **Minimum Quality Bar:**
      - Correct headers (sentence case).
      - Accurate CTA placement.
      - Quick fact-check for glaring errors.
      - No absurd jargon.
  - **Resource Management:** Felix flagged potential capacity constraints; Katya will triage publishing to keep the client satisfied and ensure resources are flagged early if constraints become critical.

---

## Action Items

**Katya Luscomb (GrowthX, Engagement Manager)**
- Share Anything scaling guidance with Sucheta
- Set up Notion automation for weekly sync agenda; post link + Fathom recording in Pod F space
- Define + document content calendar automations; record Loom walkthrough
- Set up client agenda automations; notify Felix/Simran to fill 2-week recap 12h pre-meeting
- Build Udemy content calendar (priority: complete by Friday)

**Felix Morgan (GrowthX, Content Producer)**
- Generate Anything articles; edit 1–2; update Katya on capacity
- Standardize Airtable for Metronome and Monograph: add Week/Content Calendar/Sent to Client/Current Date/In Looker; backdate Week to Jan; hide Current Date

**Simran Sethi (GrowthX, Content Producer)**
- Standardize Airtable for Udemy and Understory: add Week/Content Calendar/Sent to Client/Current Date/In Looker; backdate Week to Jan; hide Current Date

**All Team Members**
- Complete Monday updates by EOD Friday
- Contribute 2-week production recaps to client agendas at least 12 hours before client meetings

---

## Transcript

**Katya Luscomb:** No worries.

**Katya Luscomb:** I think it's just going to be you and Simran and I.

**Katya Luscomb:** Jessalyn might join, but I don't, I'm not sure if she's working today or not.

**Felix Morgan:** Okay, I think I got my headphones connected.

**Felix Morgan:** Can you hear me?

**Felix Morgan:** I can, yeah.

**Felix Morgan:** I always forget to do that if I haven't had a meeting yet.

**Katya Luscomb:** Oh, good.

**Katya Luscomb:** No worries.

**Katya Luscomb:** We've got a second, so.

**Felix Morgan:** Because I'm the type of person who sits here with these headphones listening to nothing.

**Felix Morgan:** I just, like, just silence.

**Felix Morgan:** Nice.

**Katya Luscomb:** I, um, gosh, it's nine.

**Katya Luscomb:** I feel like I've been going for hours.

**Felix Morgan:** I feel behind already because I'm just trying to generate these.

**Felix Morgan:** I'm like, I can't tell how long it's going to take me to edit anything until I generate anything.

**Felix Morgan:** Yeah.

**Katya Luscomb:** Well, and so with, with the anything articles, because we're scaling, um, and something that I probably should share with Sucheta too.

**Katya Luscomb:** Um.

**Katya Luscomb:** Um.

**Katya Luscomb:** Um, Thank

**Katya Luscomb:** Obviously, we don't want to send them total slop, but if we need to give a little bit on the overall quality and have it not be perfect, they don't do a review, for one.

**Katya Luscomb:** We just publish content and it goes live, and they're not going to look at 10 articles in detail.

**Katya Luscomb:** So I think if the big things are there, like making sure that all of the headers are sentence case and that there's nothing glaringly gross about it.

**Katya Luscomb:** But I know there were some issues with fact-checking that Jesselyn was working on with the pipeline.

**Katya Luscomb:** Yeah, just making sure there's like, you know, the CTA is right at the end.

**Katya Luscomb:** A quick fact-check.

**Katya Luscomb:** There's no like absurd jargon and that the headers are correct.

**Katya Luscomb:** And I think that's going to give us enough, like if it takes a long time to generate.

**Katya Luscomb:** So that would be my take on getting through these.

**Felix Morgan:** I know you're only doing them all generated today and edit at least one today, but I have a lot of stuff I wanted to do on Met's Films pipeline today.

**Felix Morgan:** Yeah.

**Felix Morgan:** So it's going to be mostly me working on anything tomorrow, but it's going to try and prime the pump today to like get one or two and then be able to tell you like, yes, I can definitely get through those or like, no, I can't quite get through.

**Felix Morgan:** But I'll try to do that as early today as I can, but I'm already like, how is it 11 a.m.

**Felix Morgan:** here already?

**Felix Morgan:** Yeah, no, that's fair.

**Katya Luscomb:** It goes, it goes so fast.

**Katya Luscomb:** I will ask with, with the anything production, if, let me share this screen differently because I just shared this tab.

**Katya Luscomb:** If you are, if you're not going to be able to get it done, like, please flag that as early as you can so that I can try and see if we can pull some more resources in.

**Felix Morgan:** The second one of these is done, I'm going to edit it and type it and so I can, you know, I'm going to do that different because I also don't want to be like working until 10 p.m.

**Felix Morgan:** on a Friday because we weren't able to get, you know, other things.

**Felix Morgan:** Yeah.

**Katya Luscomb:** And like I said, for this particular client, like.

**Katya Luscomb:** It's going to be a case of good enough because we are doing that scaling.

**Katya Luscomb:** Marcel had a conversation with their point of contact already.

**Katya Luscomb:** Got it.

**Katya Luscomb:** And so, like I said, we don't want swap, but we're kind of aiming for really fast growth.

**Katya Luscomb:** reassuring.

**Felix Morgan:** Yeah.

**Katya Luscomb:** We also, I know that Sulewan is like swamped with publishing requests.

**Katya Luscomb:** So I have actually been publishing.

**Katya Luscomb:** If generated and ready, I can triage that a little bit so that I'm just trying to keep the client happy to make sure they know that we've got a bunch of stuff moving.

**Katya Luscomb:** All right.

**Katya Luscomb:** Give me just one second.

**Katya Luscomb:** Simran, how are you?

**Felix Morgan:** Hey, Katya.

**Felix Morgan:** Doing well.

**Felix Morgan:** Hey, Felix.

**Felix Morgan:** Hello.

**Felix Morgan:** All right.

**Felix Morgan:** Let me...

**Katya Luscomb:** Window, where are you?

**Katya Luscomb:** have too many, sorry, have too many things going on.

**Katya Luscomb:** Zoom will tell me when I'm clicking which window, and Google doesn't, and it's annoying.

**Katya Luscomb:** Okay.

**Katya Luscomb:** That is annoying.

**Katya Luscomb:** Yeah, cool.

**Katya Luscomb:** So a couple things that I wanted to chat about, and some of this is in the works, I was throwing it together this morning, but there's definitely some action items to start on.

**Katya Luscomb:** So I think I had flagged last time that I've got this weekly sync notes.

**Katya Luscomb:** I'm working on creating more of a standardized bit where I think like I'm going to put in my updates and then have a space for you all if there's like burning questions for the group, things you're stuck on, things that you had like a breakthrough that you really want to share.

**Katya Luscomb:** I'd love to use this as a little bit of a collaborative time while also respecting all of our time to like keep things moving outside of calls.

**Katya Luscomb:** So similar to how I've done the Monday updates, I'm going to try and set it so that when I, like that it's on an auto timer to just create this agenda for us before the meeting happens.

**Katya Luscomb:** And then

**Katya Luscomb:** Send a note probably to our pod F space to let you all know that it's ready because I'm in love with Notion automations now.

**Katya Luscomb:** They're great.

**Katya Luscomb:** So, yeah.

**Katya Luscomb:** So just wanted to let you guys know that's kind of coming down the pipeline.

**Katya Luscomb:** And I put that note here at the bottom.

**Katya Luscomb:** The big thing, I guess there's a few.

**Katya Luscomb:** I really want to work on standardizing our Airtable platforms.

**Katya Luscomb:** And I think Simran, yours are probably going to be really close to this because this is a lot of what I did across.

**Katya Luscomb:** Udemy and understory already.

**Katya Luscomb:** for you, I'm going to have you go through and check that all of these are already in place.

**Katya Luscomb:** I'm to understand the setup and the intention.

**Katya Luscomb:** And Felix, I know we've talked a little bit about like having some of these for metronome.

**Katya Luscomb:** One of them is like having the week in there for all your clients, which was a carryover from Biologica that I think is really helpful.

**Katya Luscomb:** Basically looking at like how we can standardize these so that I can see things really quickly in a consistent view.

**Katya Luscomb:** You all can kind of see things and

**Katya Luscomb:** In the future, we can start automating Monday updates, like whether it's just, you know, Airtable sending something to Slack that you all can like copy, paste and put into the Monday updates and agendas.

**Katya Luscomb:** My goal is to try and make this as painless for all of us to do some of those administrative things.

**Katya Luscomb:** So I just don't have time to go through all now seven accounts and make sure that these are standardized.

**Katya Luscomb:** I'm looking for you gals to support across each of your accounts to make sure this is consistent.

**Katya Luscomb:** Udemy is pretty much already set up for this.

**Katya Luscomb:** So I've linked to their Airtable if you want to take a look.

**Katya Luscomb:** And I put together a smattering of a walkthrough.

**Katya Luscomb:** It's a little bit stream of consciousness.

**Katya Luscomb:** So if anything in here doesn't make sense, please just come ask me.

**Katya Luscomb:** And then I've also created a little write-up of each of the different sections.

**Katya Luscomb:** This is still kind of a work in progress.

**Katya Luscomb:** I'm probably going to migrate it to its own Notion page once I'm done.

**Katya Luscomb:** So we just have it.

**Katya Luscomb:** But essentially, if.

**Katya Luscomb:** If I look at Udemy, I created, I just created this weekly roundup tab so that it just gives a really easy view without the bloat of all of the other columns that are kind of excessive.

**Katya Luscomb:** I would also encourage you in any views that you're actively using, like if there's fields that you don't need, because so many of these have a lot of extra, like please hide those, make it easy for yourself, you know, make sure that you're, you know, what you're looking at.

**Katya Luscomb:** In a couple of weeks, I'd like to make sure that clients have interfaces so that it makes their life a little bit easier too.

**Katya Luscomb:** They're easier on the eyes personally, but we'll get into that later.

**Katya Luscomb:** So what I've done here basically is I just took the raw assignments and I filtered it by anything that was like approved through published so that we can kind of get a glimpse.

**Katya Luscomb:** You can also add like, you if you want to look at the topics pending approval, if there's a lot of that that we wait on and we send them updates and requests on approving things.

**Katya Luscomb:** That might be helpful for you all.

**Katya Luscomb:** And then I also have it sorted by content calendar.

**Katya Luscomb:** So basically anything that's already in the calendar, want to be able to see that.

**Katya Luscomb:** And so what you're going to want to make sure is that each of your clients has a content calendar column.

**Katya Luscomb:** And we're also going to be making sure that they all have a week column.

**Katya Luscomb:** Ideally, the labels in the week map to the week of the engagement so that when I make an agenda that says, you know, week of like week 20, that I can also come in here and just really quickly see like, hey, here's the week 20 content that we're looking at.

**Katya Luscomb:** And same for the client because they have that visibility too.

**Katya Luscomb:** So for Udemy, I already backdated.

**Katya Luscomb:** Don't feel like you need to go backdate through the entire engagement for your accounts.

**Katya Luscomb:** If we can just backdate about that.

**Felix Morgan:** No, that would kind of be insane.

**Katya Luscomb:** I did for Udemy because I wanted to see how much a pain it would be and like needed a better visualization of where things were at.

**Katya Luscomb:** But if you can backdate through January.

**Katya Luscomb:** For these week assignments across your accounts, that would be super helpful.

**Katya Luscomb:** And this is all written out in the notes document as well.

**Katya Luscomb:** The other columns you're going to make sure, you're going to add a sent to client column.

**Katya Luscomb:** This is a date and it's actually going to be automated.

**Katya Luscomb:** So you just need to make sure that it's set for date and then US time zone.

**Katya Luscomb:** And then the column that we need to automate it is this current date column.

**Katya Luscomb:** And this is a formula right here.

**Katya Luscomb:** And again, like there's pictures of this and the formula itself.

**Katya Luscomb:** So you can see that for easy reference.

**Katya Luscomb:** And this just automatically updates, I think like every couple of minutes.

**Katya Luscomb:** Once this is set, you can hide it.

**Katya Luscomb:** You don't actually need to see it.

**Katya Luscomb:** We just need it in their air table so that some automations can run in the back end.

**Katya Luscomb:** Questions about any of this so far?

**Katya Luscomb:** I'm going kind of fast.

**Felix Morgan:** No.

**Felix Morgan:** Cool.

**Katya Luscomb:** The other piece, I think I chatted with you both about making sure there's an in-looker column.

**Katya Luscomb:** Thank

**Katya Luscomb:** And making sure this gets checked off every week when you add URLs to Looker.

**Katya Luscomb:** One, it's super helpful for me to see how recently content has been updated based on what performance stats I'm pulling.

**Katya Luscomb:** Because I don't want to pull performance for like the last week if those haven't been updated when I'm actually in Looker pulling data.

**Katya Luscomb:** And if for some reason you're ever out of office, it also makes it really easy for whoever's covering to come in and be like, oh, I need to go in and add all of these URLs.

**Katya Luscomb:** If your client is really hands-on with topic approvals, I also want to make sure we've got a topic approval column.

**Katya Luscomb:** And I think we can standardize the approval selection as well.

**Katya Luscomb:** And basically for most of mine, I've got like, is it approved, need revision, rejected, or pending review?

**Katya Luscomb:** Basically, like if it's a new assignment, it'd pending review.

**Katya Luscomb:** And otherwise, they'll change these.

**Katya Luscomb:** And then we can create automations that when they...

**Katya Luscomb:** If they reject something, it automatically goes to archive.

**Katya Luscomb:** If they approve it, it automatically goes to approve to start.

**Katya Luscomb:** Some clients will only reject things.

**Katya Luscomb:** They don't want to click approve on every single one, and that's fine.

**Katya Luscomb:** And so in that case, we can just do a reject or needs revision, and it gives us a really easy way to see what they want to change.

**Katya Luscomb:** I also have a topic feedback column here.

**Katya Luscomb:** I know Udemy has used this a little bit.

**Katya Luscomb:** If they do reject something or want us to revise it, then they put some notes in here, so it's easy to see.

**Katya Luscomb:** And then an article approval column, and this is more about if they have a review step of the content that we send them.

**Katya Luscomb:** And this would probably be more tailored to the specific client's process.

**Katya Luscomb:** So in Udemy's case, they review it, and then revisions needed is when they flag that their review is done, and it will automatically update our status to back to GrowthX.

**Katya Luscomb:** I know some clients will...

**Katya Luscomb:** We'll just update the status in Airtable.

**Katya Luscomb:** Makes me a little bit nervous to have them changing our statuses and moving things around.

**Katya Luscomb:** So way easier if they just have this particular view that can shift it.

**Katya Luscomb:** Revisions applied would be for us to indicate that those revisions applied.

**Katya Luscomb:** And again, it would automatically update the status with growthx for review to ready for client or ready for publishing, depending on what that step looks like.

**Katya Luscomb:** And then in Udemy's case, they are the ones that actually publish the content.

**Katya Luscomb:** This would be similar for Metronome if we can potentially get Chris on board.

**Katya Luscomb:** And then that also would update the status to published.

**Katya Luscomb:** And then, you know, if you guys want, like we can set up notifications for you in Slack so that you would get a ping when things do get published.

**Katya Luscomb:** And then, you know, to go in and like update Looker and all that good stuff.

**Katya Luscomb:** Questions?

**Katya Luscomb:** No, I think this all seems pretty straightforward.

**Felix Morgan:** One thing that I get confused about sometimes is which view we're using.

**Felix Morgan:** So like as we add views.

**Felix Morgan:** Like, is this just, like, the one we should spend time in for?

**Felix Morgan:** Is there, like, reason to go into other views?

**Felix Morgan:** You see what I'm saying?

**Felix Morgan:** Like, I do know, like, I have already been switching between, obviously, this doesn't have backlog and considering and, like, stuff like that.

**Felix Morgan:** So for, like, Monograph, for example, like, you know, I have to go in there to get, like, new assignments.

**Felix Morgan:** But is the idea that, like, this would be the primary view that you and me are using, like, 90% of the time or no?

**Felix Morgan:** So, no, I don't think so.

**Katya Luscomb:** And you don't even need to create this view in particular.

**Katya Luscomb:** I just wanted to give a snapshot of the specific columns and how they're going to relate together.

**Katya Luscomb:** This view, honestly, would probably be more for me, potentially for you all, if you wanted something similar to be able to, like, do Monday updates really easily.

**Katya Luscomb:** I think this view is, like, well-organized to facilitate that.

**Katya Luscomb:** If, so, I mean, primarily when I was doing content generation, I mostly just hung out in the raw assignments view.

**Katya Luscomb:** Because it just had everything that I

**Katya Luscomb:** The idea behind having a lot of these views was that the client could be in here, like, and they would know that these were specific, you know, like, is there content ready for them to review?

**Katya Luscomb:** As we develop interfaces for them, it kind of eliminates the need for a lot of those tabs.

**Katya Luscomb:** So when it comes to, like, the right tab to use, I don't think there is a specific answer to that.

**Katya Luscomb:** It really depends on your working style.

**Katya Luscomb:** I would say just make sure that you have a view that you consistently go into that has, like, all of the metadata that you're going to need to update.

**Katya Luscomb:** Anything that you need to be filling in or making sure it's filled in correctly to see the status, you know, any kind of assignment information, keyword details, all of that.

**Katya Luscomb:** And I would encourage you, like, especially in these raw assignments views, if you need to go and, like, hide certain things to tidy it up for yourself and make sure it's like this should probably have an in-looker.

**Katya Luscomb:** Like, you can go in and mess with this a little bit as well.

**Katya Luscomb:** I know anything in client views I would caution.

**Katya Luscomb:** And making changes too, just in case you have a client that goes in and updates a lot of that.

**Katya Luscomb:** For sure.

**Felix Morgan:** I guess that was my question was like, number one, like how much ownership could we have to like make this how it makes sense to us?

**Felix Morgan:** And number two, which of these values, because I do see the value in several of these automations and stuff.

**Felix Morgan:** Although I guess you're right that if it's like automatically updating the status, I don't need to be in that view for that to be working.

**Felix Morgan:** I guess what I was saying is like, are any of these new fields that you're introducing for automations, things I should bring back into my view, you know, like, and I guess I'll just kind of see if any of those are useful.

**Felix Morgan:** Yeah.

**Katya Luscomb:** So I would potentially poke around Udemy's.

**Katya Luscomb:** That's what I was thinking as I'm going go.

**Felix Morgan:** Yeah.

**Katya Luscomb:** And so like, I mean, in, in raw assignments, I moved some of this around, like, I'm probably going to hide this current date because it doesn't need to be there anymore.

**Katya Luscomb:** Um, but like poke around.

**Katya Luscomb:** So basically, I would say, like, set it up so that the views make sense in your brain.

**Katya Luscomb:** And for metronome, like those two, wouldn't mess with too much.

**Katya Luscomb:** If you need another view separate, like add another one.

**Felix Morgan:** Yeah, you just make one that's nice and clean.

**Felix Morgan:** I'm thinking of monograph.

**Felix Morgan:** There are so many random like columns and views in monograph that I'm just like, I'm itching to clean them up.

**Felix Morgan:** But I don't want to get rid of anything useful, but I would love a more streamlined approach there.

**Felix Morgan:** Metronome is great.

**Felix Morgan:** It's like I can just add a looker and be like, great.

**Felix Morgan:** There's a reason.

**Katya Luscomb:** And I'm happy like if you if you're getting into your air tables and feeling like they're really messy and really clunky and want to workshop that a little bit more in a one on one.

**Katya Luscomb:** We can do that as well as far as like what columns really make sense to keep.

**Katya Luscomb:** I've gotten a better understanding of like what we need to upload and how it is linked between various tabs and things.

**Katya Luscomb:** So I'm happy to workshop that with you all a little bit as well.

**Katya Luscomb:** Just flag free in advance.

**Katya Luscomb:** That's something that you want to talk about on your calls so that I can go in and look at how things are set up.

**Katya Luscomb:** And have some ideas on like tips and tricks to share with you all.

**Katya Luscomb:** Cool.

**Felix Morgan:** And I know you always do, but if we can make sure we have the recording for this one, it always helps me to watch it back while I'm doing it.

**Katya Luscomb:** Yes, I am going to actually start sharing a link to the Fathom recording and the agenda in our pod space as well.

**Katya Luscomb:** Amazing.

**Felix Morgan:** You're not going to get the fancy recaps that the clients get because I trust you all.

**Felix Morgan:** I'm perfectly capable.

**Felix Morgan:** Plus, I have my own note taker as do we all.

**Felix Morgan:** So I've got multiple.

**Felix Morgan:** It's just when the screen share, you know, the text notepakers are not great at screen share.

**Felix Morgan:** Yeah.

**Katya Luscomb:** So what I would say in terms of your views and adding these and implications for what you're going to be responsible for making sure are up to date, ideally for the, and I can help like finesse content calendars, but especially Felix for you, like you've got a really good sense of like big picture strategy and things.

**Katya Luscomb:** And like, as, um,

**Katya Luscomb:** What am I trying to say?

**Katya Luscomb:** Yeah, like I had built out a lot of the content calendars for Udemy and UnderStory already.

**Katya Luscomb:** like Simran, you and I have kind of talked about having you start to like play with that a little bit more as more of that gets built out and us collaborating.

**Katya Luscomb:** Felix, I'd love for you to like take ownership because you already have such a good sense.

**Katya Luscomb:** Like you're the one picking assignments anyway.

**Katya Luscomb:** And we can obviously like we'll talk about big picture strategy and distribution of what content needs to be prioritized when.

**Katya Luscomb:** But what I would like you gals to own, one thing I need to add in here are the automations for the content calendar.

**Katya Luscomb:** But if you look in here, there are automations that like will automatically update the status.

**Katya Luscomb:** And so each week at some point, doesn't need to happen early necessarily, but each week you'll need to go in and update the like select new assignments for the week four.

**Katya Luscomb:** And that will also give you a really good view.

**Katya Luscomb:** Like, do we need more assignments?

**Katya Luscomb:** Like, do you need to go do keyword research?

**Katya Luscomb:** Do I need to support with some, like, keyword research and strategy around new ideas and content?

**Katya Luscomb:** And let's have those conversations a month out rather than, you know, super last minute.

**Katya Luscomb:** Which you both have been really good about flagging all of that for me as well.

**Katya Luscomb:** So super appreciate.

**Katya Luscomb:** But just wanting to make sure, like, this gives us even more visibility of where are we pointing?

**Katya Luscomb:** How much runway do we have?

**Katya Luscomb:** Where do we need to be prioritizing our time to make sure we're prepared for the future?

**Katya Luscomb:** And it also makes it really easy, again, like, if there's a sudden outage or, like, if you're taking a couple weeks off, someone can just come in and it's immediately obvious where they need to be.

**Katya Luscomb:** So the way I have these automations set up is that every Saturday at, like, midnight, essentially, Pacific time, it will update.

**Katya Luscomb:** And you have to do it in a certain order.

**Katya Luscomb:** I'll make a little loom about this as well.

**Katya Luscomb:** But essentially, you want it to update, like, the.

**Katya Luscomb:** Current week to share it with client, one week out to current, two weeks out to one week, three weeks out to two, four weeks out to three.

**Katya Luscomb:** And you want it in this order because if you do one week out to current and then current week to share it with client, you're going to have everything become shared with client instead.

**Katya Luscomb:** And so I've separated these by like 15 minute increments.

**Katya Luscomb:** But it will also mean that each week that four week out chunk will then be missing.

**Katya Luscomb:** And so the selection in, like I made myself a content calendar view.

**Katya Luscomb:** So again, like you can go poke around this.

**Katya Luscomb:** And the way I did this is so that I can see everything that's coming up in the current week.

**Katya Luscomb:** And depending on what I'm trying to do, I'll go in.

**Katya Luscomb:** And then I also want to see backlog assignments so that I can.

**Katya Luscomb:** And in their case, I have it grouped by pillar because we do, we do chunks of pillars at a time for them.

**Katya Luscomb:** And so here I can go in like, okay, I know that we've done a lot of content.

**Katya Luscomb:** We haven't done a lot of content recently.

**Katya Luscomb:** And so I'm going look at what's approved, what's in the backlog, and then I'm going to pick my five for four weeks out so that I'm kind of pacing that.

**Katya Luscomb:** Does that make sense?

**Felix Morgan:** Okay.

**Felix Morgan:** Cool.

**Katya Luscomb:** And then when you update the content calendar, also make sure that the week is reflected there just to save yourself some time as a routine thing.

**Katya Luscomb:** So anytime you add something for four weeks out, go in and you'll just add the next week.

**Katya Luscomb:** So in this case, you can just manually type in like week 21, and then it will auto update in this field here.

**Katya Luscomb:** I'm going to delete that because that's not actually where I want it.

**Katya Luscomb:** But yeah, so basically like each week, content calendar, add the week, and then that'll be done.

**Katya Luscomb:** And then whenever, the one thing that gets a little bit tricky is this sent to client automation.

**Katya Luscomb:** That is going to vary slightly depending on the client.

**Katya Luscomb:** So the way I have it set up, because Udemy has a review stage, this automation gets triggered whenever Simran changes it to ready for Udemy review.

**Katya Luscomb:** And then it will add in, in the sent to client field, it adds in the current date based on what is in the current date field.

**Katya Luscomb:** So you can kind of see how that logic is set up.

**Katya Luscomb:** For clients who auto-publish, like for Monograph, Felix, they're pretty straightforward.

**Katya Luscomb:** Like you're going to want to do when status is published.

**Katya Luscomb:** And then we can just see, I mean, not only does it give you the publish date, but again, it gives me a really easy round of like, when did we actually deliver that content?

**Katya Luscomb:** So that I can also pull that if, you know, if there's ever questions of how much did you get done this month?

**Katya Luscomb:** Like what, what does that actually look like?

**Katya Luscomb:** Like, um, was chewing on the idea of changing it to like when the content calendar updates, but that would mean, Thank

**Katya Luscomb:** I mean that everything gets changed on Saturday because of the automations, and that would be messy.

**Felix Morgan:** think the status is the easier way to go.

**Katya Luscomb:** There are some clients, mostly noting this for Justin, if she watches this recording, like I know she has a few where sometimes they review articles, and sometimes articles go straight to publishing.

**Katya Luscomb:** So she and I will probably work on tailoring this automation in particular for that account.

**Katya Luscomb:** But for most folks, it's going to be pretty straightforward.

**Katya Luscomb:** I've done a lot of talking at you all.

**Katya Luscomb:** Do you have any questions?

**Felix Morgan:** No, I might want to start getting into it, but it all makes sense to me so far.

**Felix Morgan:** Perfect.

**Katya Luscomb:** In our agenda, I've written out as far as those key columns to have in.

**Katya Luscomb:** There's some notes on some automations.

**Katya Luscomb:** I need to finish filling this out.

**Katya Luscomb:** But by next Wednesday, if you can prioritize getting these calls.

**Katya Luscomb:** Columns added.

**Katya Luscomb:** And if you have clients that do approvals, making sure that those are in there as well, that would be super helpful.

**Katya Luscomb:** And we talked about, yeah, that you guys are going to start supporting with like actually setting that content calendar as well.

**Katya Luscomb:** And then just a quick call out.

**Katya Luscomb:** You guys have been great.

**Katya Luscomb:** Really appreciate it.

**Katya Luscomb:** But making sure that those Monday updates, if you can have those filled in by Friday at the end of the day, because I'm going to try and go back in and backfill as well.

**Katya Luscomb:** And like worst case, if you can't get to it until Monday, like I get on it like 8 a.m.

**Katya Luscomb:** PST typically, sometimes a little bit earlier.

**Katya Luscomb:** So just as long as I have those to glance over Monday morning, that would be great.

**Katya Luscomb:** And then the other piece on my radar, just as I try and like make sure that we're all kind of coordinating our time where it makes the most sense.

**Katya Luscomb:** There's a section in each client agenda that we have, that the MEs have been asked to, sorry.

**Katya Luscomb:** Engagement Manager.

**Katya Luscomb:** There's a long agenda that we've been asked to put together.

**Katya Luscomb:** There's a section in there that is a recap similar to the Monday updates, but instead of being a, here's what we did in the past week, it's a here's we did in the past two weeks.

**Katya Luscomb:** And so I'd love for you gals to start supporting and filling that out as well.

**Katya Luscomb:** And I'll put a little bit more information in here.

**Katya Luscomb:** Again, I'm going to set up automations for each one so that when the agenda is created, it will just send you all a note in each internal client channel that says like, hey, this agenda is updated, please go in and fill out XYZ.

**Katya Luscomb:** Hopefully, like it should only take you maybe five to 10 minutes to do a quick recap of of the like actual content production that happened in the last couple weeks.

**Katya Luscomb:** Please also note in there, like if there's any changes to, like if there's a specific article you want to call out or need some reflection, like that's a great place to put that.

**Katya Luscomb:** So that I

**Katya Luscomb:** I know that's something that I need to follow up with a client.

**Katya Luscomb:** You can flag it for me or like I will come to you and ask if there's any, if I've got any questions.

**Katya Luscomb:** My goal is to have these agendas created at least a day before the meeting.

**Katya Luscomb:** So we have 24 hours for you guys to go in, fill things out.

**Katya Luscomb:** My request is to do like 12 hours before I meet with them so that I can come to you with any questions that I've got.

**Katya Luscomb:** Does that seem realistic for you all?

**Katya Luscomb:** Yeah.

**Felix Morgan:** Yeah.

**Felix Morgan:** Perfect.

**Katya Luscomb:** All right.

**Katya Luscomb:** That is everything that I had that I just bashed through in 30 minutes.

**Katya Luscomb:** Before we hop off, do you guys have any specific questions, things that you're stuck on that I can help kind of triage immediately this week?

**Katya Luscomb:** And if not, then we can connect in your one-on-ones next week.

**Simran Sethi:** Nothing major, but just want to check if the calendar for Udemy was built out.

**Simran Sethi:** It's not yet.

**Simran Sethi:** It's That's all.

**Katya Luscomb:** I actually fortunately have two days that I don't have any client calls.

**Katya Luscomb:** So that is one of my priorities to do today and tomorrow.

**Katya Luscomb:** Okay.

**Katya Luscomb:** Thank you.

**Simran Sethi:** Yep.

**Simran Sethi:** I got to jump for another meeting.

**Felix Morgan:** No worries.

**Felix Morgan:** Bye.

**Felix Morgan:** All right.

**Felix Morgan:** Bye.

**Felix Morgan:** Bye.
