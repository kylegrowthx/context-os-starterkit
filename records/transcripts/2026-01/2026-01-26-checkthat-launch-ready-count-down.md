# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-01-26
time: 16:00 UTC
duration: 25 minutes
organizer: stevie@growthx.ai
participants:
  - name: Estevão Mascarenhas
    email: estevao@growthx.ai
    affiliation: GrowthX
  - name: Marcel Santilli
    email: marcel@growthxlabs.com
    affiliation: GrowthX Labs (External)
  - name: Jason Gong
    email: jason@growthx.ai
    affiliation: GrowthX
  - name: Jose Farias
    email: jose@growthx.ai
    affiliation: GrowthX
  - name: Pedro Steimbruch
    email: pedro@growthx.ai
    affiliation: GrowthX
  - name: Daniel Lopes
    email: daniel@growthxlabs.com
    affiliation: GrowthX Labs (External)
  - name: Leonardo Carpenedo Steffen
    email: leonardo@growthx.ai
    affiliation: GrowthX
  - name: Stevie Kim
    email: stevie@growthx.ai
    affiliation: GrowthX
fathom_recording_id: 117070103
fathom_url: https://fathom.video/calls/543288400
share_url: https://fathom.video/share/ZWRysyP_Y9at9ZS4MnUUXgBYTzPxBctt
source: fathom
enriched_on: 2026-02-28 00:00 UTC
</metadata>

---

## Summary

CheckThat launch readiness sync narrowed blockers to 3 P0 items targeting Jan 31st closure. Jose is executing a critical workspace ID migration (BN to UUID) with ~2-hour downtime this morning, pending Render checkpoint completion. The auth flow remains blocked on an invitation design decision (email-tied vs. user-selected login) that Jose will escalate to Marcel and Daniel via Slack poll.

---

## Context

The CheckThat team is in final pre-launch preparation with daily standups replacing normal cadence to ensure shipping readiness. Over the weekend, Stevie reduced blocker count through ticket review, removing duplicates and obsolete items. The infrastructure migration to UUID-based identifiers is the critical path item required before launch, while product decisions around authentication flows need immediate resolution to unblock the auth PR. Team morale and progress remain strong with clear visibility into remaining work.

---

## Relevance

- **Critical Infrastructure Migration:** Database-level change converting workspace IDs from big integers to UUIDs requires full app shutdown and ~2-hour maintenance window, with rollback capability via Render checkpoint.
- **Authentication Design Decision:** Unresolved question on invitation flow blocking auth PR merge—affects UX friction for multi-email users and security posture for former employees.
- **Launch Blockers:** Ticket review discovered and removed duplicate/obsolete work; P0 count down to 3 with Jan 31st target achievable.
- **UI/UX Polish:** Prompt table grouping and clickability improvements improve user discoverability; minor right-click UX edge case identified for super-users.

---

## Overview

- **Launch Blockers Reduced:** The P0 blocker count is down to 3, with the Jan 31st target still in sight.
- **Critical Migration Today:** Jose will run a ~2-hour maintenance migration to convert workspace IDs to UIDs, requiring a full app shutdown.
- **Invitation Flow Decision Pending:** The auth flow is blocked pending a decision on whether to tie invitations to a specific email or let users choose their login.
- **UI/UX Refinements:** The prompt table now groups pending items, and a UI fix makes prompt rows clickable for better discoverability.

---

## Key Topics

### Launch Readiness & Blockers

- Ticket review over the weekend revealed and removed several duplicate or obsolete tickets.
- **Current Blocker Status:**
  - **P0 Blockers:** 3 remaining (target: Jan 31st).
  - **Launch Blockers:** A larger, unspecified number remain.

### Critical Task: Workspace ID Migration

- **Task:** Migrate workspace IDs from big integers (BNs) to Universal Unique Identifiers (UUIDs).
- **Rationale:** A necessary pre-launch task to ensure data integrity and scalability.
- **Execution Plan:**
  - **Timing:** This morning, after the Render point-in-time recovery checkpoint completes.
  - **Downtime:** ~2 hours, with the app in maintenance mode to prevent database writes during the ID swap.
  - **Communication:** Jose will post notices in the `#checkthat` and `#ask-checkthat` Slack channels.

### Blocked Task: Invitation Flow

- **Blocker:** The auth PR is blocked pending a decision on the invitation flow.
- **Decision Point:** Should invitations be tied to a specific email, or should users be allowed to choose their login account?
- **Rationale:**
  - **User Choice →** Prevents friction from email mismatches (e.g., `growthx.ai` invite vs. `growthxlabs.com` login).
  - **Email Tie →** Mitigates security risks like former employees retaining access to old company accounts.
- **Decision:** Jose will post the question to Marcel and Daniel in Slack for a final decision.

### UI/UX Refinements

- **Prompt Table Grouping:**
  - Pedro implemented a UI to group prompts that are "waiting to be probed" (i.e., still processing).
  - These items are now collapsible at the top of the table.
  - **Action:** Jose requested clearer user-facing language, as "probe" is internal jargon.
- **Prompt Row Clickability:**
  - Stevie fixed a bug to make the entire prompt row clickable, improving discoverability.
  - **Known Issue:** Right-click shortcuts (e.g., "Open in new tab") only work when hovering over the text, not the entire row. This is a minor inconsistency for super-users.

---

## Action Items

**Pedro Steimbruch (GrowthX)**
- Update prompt table header copy to clarify 'waiting to be probed' for users
- Post Loom walkthrough of auth/invite flows in Slack for Jose, Stevie
- Sync w/ Stefan re: taking tickets 609, 406; else start stabilization week
- Cancel afternoon check-in w/ Stevie, Jose

**Jose Farias (GrowthX)**
- Post Slack poll re: invite email vs login email; tag Marcel, Daniel; then review/merge auth PR
- Post maintenance notice in Slack (#checkthat, #ask-checkthat); then run workspace ID migration

---

## Transcript

**Jose Farias:** Hey, hey, good morning.

**Stevie Kim:** Good morning.

**Jose Farias:** Seems like we have two check-ins today.

**Jose Farias:** I don't know if that's necessary.

**Jose Farias:** I don't think it is.

**Stevie Kim:** Yeah, the later one today was our normal one.

**Stevie Kim:** Like this daily stand-up is just a temporary thing to get us post-launch.

**Jose Farias:** Sounds good.

**Jose Farias:** I think that's the purpose of this.

**Stevie Kim:** So, yeah.

**Stevie Kim:** Okay.

**Stevie Kim:** We can just get started.

**Pedro Steimbruch:** Hey, good morning.

**Pedro Steimbruch:** Good morning.

**Stevie Kim:** Morning.

**Stevie Kim:** Um, yeah, so we can kind of go through this. I just wanted to mention I didn't get a whole lot done this weekend, but I got a couple things done, a couple tickets done.

**Stevie Kim:** And then I actually was going through them a little closer, seeing what was left.

**Stevie Kim:** There were a couple duplicates, and then some, I think one or two that weren't necessary anymore because of them being fixed through other changes, either like UI changes or bug fixes.

**Stevie Kim:** So yeah, that was good.

**Stevie Kim:** So we have less to work on.

**Stevie Kim:** Um, so yeah, there's only like three in the P0 blockers, which I think we had that the 30 to the goal to get those done the 31st.

**Stevie Kim:** And then there's still a decent amount in the launch.

**Stevie Kim:** Um, and yeah, Pedro, I assigned a couple to you that they, a couple of them are kind of related, like the fixed logo fallback when brand fetch returns no logo.

**Stevie Kim:** And then I think the other one, I don't know where that went.

**Stevie Kim:** Oh, you already have it in progress.

**Pedro Steimbruch:** I'm about to merge it.

**Stevie Kim:** Oh, cool.

**Stevie Kim:** Okay.

**Stevie Kim:** Yeah.

**Stevie Kim:** So just wanted to touch on, you're already aware of them.

**Stevie Kim:** Um, but anyway, those are the only things that I just wanted to touch on.

**Stevie Kim:** So if we want to go around and yeah, talk about anything blocking us or anything that we're working on or got already done, feel free.

**Stevie Kim:** Do you want to jump first, Jose, or can I?

**Jose Farias:** Go ahead.

**Jose Farias:** Yeah.

**Pedro Steimbruch:** So yesterday or maybe on Saturday, I worked on clarifying handling of prompts with no citation data. We discussed where prompts still waiting to be probed or get the metrics consolidated were at first in the table.

**Pedro Steimbruch:** So I decided on a straightforward solution. We quickly discussed about making them collapsible in the beginning of the table.

**Pedro Steimbruch:** I can share my screen. Do you guys want to see it now or do I do a loom later?

**Pedro Steimbruch:** What do you guys think?

**Stevie Kim:** Oh, go ahead and show us now.

**Stevie Kim:** Yeah.

**Pedro Steimbruch:** We have time.

**Stevie Kim:** I don't want to.

**Pedro Steimbruch:** Yeah.

**Pedro Steimbruch:** So I'm not sure if I will be able to find this one.

**Pedro Steimbruch:** Let's see if this one has it.

**Pedro Steimbruch:** And then I noticed, oh, this one doesn't.

**Pedro Steimbruch:** So let me see locally.

**Pedro Steimbruch:** I have some data locally that will give you an idea of how it looks like.

**Pedro Steimbruch:** So, yeah.

**Pedro Steimbruch:** This is a table.

**Pedro Steimbruch:** What? I don't have the metrics here because it's stale data on my database, but we have the example here.

**Pedro Steimbruch:** Okay, so I can see the prompts in here that are still waiting to be probed.

**Pedro Steimbruch:** So these prompts are either waiting to be probed by AI models or the metrics are still being calculated.

**Pedro Steimbruch:** Results typically appear in 24 hours.

**Pedro Steimbruch:** And yeah, which is nice is that the select here and the actions will work seamlessly when I have prompts below.

**Pedro Steimbruch:** So let me see if Navvan has.

**Pedro Steimbruch:** I don't remember that actually has prompts.

**Pedro Steimbruch:** Not Navvan.

**Pedro Steimbruch:** Either way, that's how it will appear.

**Pedro Steimbruch:** Okay.

**Pedro Steimbruch:** Check that.

**Pedro Steimbruch:** I think this works great.

**Jose Farias:** I think we can do a better job of explaining what's going on because probe is sort of like internal language. They don't know what that means. But yeah, we can just explain that better. I think this works.

**Pedro Steimbruch:** Yeah, I can definitely improve here. Then, oh, sorry, quick question.

**Jose Farias:** I just realized there's a checkbox beside those. What does that do?

**Jose Farias:** It selects.

**Pedro Steimbruch:** It selects and allows me to change them.

**Jose Farias:** Yeah, if you have more prompts, not probes, more prompts in the table that actually do have data, they all behave the same way, like you can bulk edit all of them?

**Pedro Steimbruch:** Yeah, yeah, yeah, yeah.

**Pedro Steimbruch:** Got it.

**Pedro Steimbruch:** And then, yeah, exactly.

**Pedro Steimbruch:** Then this one, and then we have this one in review, Jose.

**Jose Farias:** Yes, I'm blocking that out.

**Pedro Steimbruch:** Yeah, I want to, I should have done that already. I apologize for not doing it, but I will probably record a loom of all the flows and post the channel so people can also, you know, throw their opinions on it, if that makes sense for you, Jose.

**Pedro Steimbruch:** I don't think so.

**Jose Farias:** Sorry, I just, so what's happening there is I need to review it more closely. It's an auth related thing. I'm just expecting for like the recording and Stevie. It's an auth related thing. We need to get those flows right. Pedro and I were having a conversation last week about whether to tie invitations to a specific email or let the person that's the recipient of the invitation decide how. So the use case there is, for example, us, if they invite, for example, say Daniel with his at growthx.ai email, but he actually uses the old one, growthxlabs.com to log in. If we tie the invitation to the email, then there has to be a back and forth about, oh, you invited the wrong email, you just re-invite the correct one, et cetera. Whereas if we let Daniel decide how he logs in to CheckThat already, we can just link it to the proper one. He receives the invitation in the growthx.ai, and then he logs in with the growthxlabs.com, and it all works seamlessly. So I don't want to involve too many people, is the thing. Like, I don't want to design by committee there. Let's just bring it up right now, what do folks think, and let's make a decision, if we can.

**Pedro Steimbruch:** But do you all have an opinion on this?

**Stevie Kim:** I don't think that I have, yeah, I don't really, I mean, whatever is the most.

**Pedro Steimbruch:** Yeah, I will bring my, I know you brought your example, Jose, from the agencies you worked with. I remember my first time at GrowthX, and I was invited to maybe even Linear or Notion, I think. And I received an invitation email, I went away, accepted it, I was signed in in Notion with my personal email, I accepted the invitation with my personal email. And then the guy from IT, sorry, I forgot his name, Yusuf, Yusuf asked me to accept it with GrowthX email.

**Jose Farias:** Yeah, the thing about that is that Notion is something that you could feasibly use personally. Worth, CheckThat. It's like, I think it's unusual. But, I mean, it says something that Notion works that way. I know Basecamp works that way, too.

**Pedro Steimbruch:** Basically, when you get an invitation, you're asked, like, do you already have an account?

**Jose Farias:** And you can be like, yes, I already have an account, and we can link them. Here, CheckThat, more like business software. I'm unsure you would have a personal account. If you already have a work account that you can sign into, usually you would want to use the same one, I think.

**Pedro Steimbruch:** What do you mean by personal?

**Stevie Kim:** Oh, you mean, so we don't accept personal emails.

**Stevie Kim:** We don't even accept personal emails.

**Stevie Kim:** True.

**Stevie Kim:** True.

**Jose Farias:** So, what could happen there is, like, say you use CheckThat at one company.

**Jose Farias:** True.

**Jose Farias:** Thank you.

**Jose Farias:** So an account, you use that, and then you're fired from that company, and then you CheckThat with your next company, and you're still signed in, and no one kicked you out of the old account, that's a risk. Like, if you accept an invitation, you're still signed into your old work account. We would link both, essentially.

**Stevie Kim:** Yeah, I mean, there's, like, tons of user management stuff like that this kind of bubbles up, that we were not prepared, quite prepared to tackle yet. For a long time.

**Jose Farias:** Right, in that case, like, I feel like that's an edge case, like, we shouldn't build for that. Specifically, if that happens, they can reach out, and we can fix things manually. Okay, so let's say, just so we can move on. My opinion is that the user should be able to decide how they log in. That said, it doesn't seem like we have strong opinions in this group. So let's just ask Marcel and Daniel, like point blank in the Slack. I can write it up since it's my issue that I brought up. So I'll write it up and then we can discuss in Slack and make the decision there in writing. And I can't say move forward yet. Sorry, I need, I'm a little bit of a bottleneck here, but I need to review that PR.

**Pedro Steimbruch:** One thing that I noticed, I was reviewing Jacopo's PR on, it's not a PR yet, it's just a branch. I was reviewing the invitations branch he has on Atlas. And I noticed he used the invitation feature from Clerk. I was about to talk to him. Today, to understand why he decided to use that and what are the benefits, but he's out of office until next week. So, I just didn't understand what's the benefit of using the Clerk's invitation feature solely. I know they have an organization, which is a bigger feature. I didn't go through the docs, but I think it's just for sending email, I think it's just fine to have a mailer on our side because everything else is even more cluttered because then you need to send an API request, work with webhooks when the invitation is accepted and stuff if we are using the Clerk invitation system.

**Jose Farias:** Yes, I, we decided against using Clerk organizations because it's that much more data to sync. And also we wanted the organizations called workspaces here to be a first-class thing. I don't know if we have that in Atlas. If we don't, then that might be the reason. I think what you have is it makes sense. We're almost there. I just need to review it and probably make tiny changes and then merge. Okay, sounds good.

**Pedro Steimbruch:** Yeah.

**Jose Farias:** Okay, sounds good.

**Pedro Steimbruch:** Yeah.

**Pedro Steimbruch:** Now I'm about to...

**Pedro Steimbruch:** Sorry, go ahead.

**Jose Farias:** I was just going to say, I don't like holding us back in this stage. It's just auth-related. It's like, yeah, we don't have that many blockers. I'll get to it today. I completely get it.

**Pedro Steimbruch:** I think it makes sense if it's just one to two or three days to get it right from the first time, and it's just fine.

**Pedro Steimbruch:** I appreciate it.

**Pedro Steimbruch:** Yeah, so, and then I will finish this one about log override in a few, and then I will sync with Stefan if he wants me to tackle the track company and the others, the 609 and 406 for him. Otherwise, I will start tackling stabilization week. That's all from my side.

**Stevie Kim:** So, wait, did you say, oh, okay, yeah, never mind. I thought you said Stefan, and I was like, wait, what?

**Pedro Steimbruch:** Stefan, Stefan, sorry.

**Stevie Kim:** That's all good. I was just like, wait, which team am I on right now?

**Pedro Steimbruch:** I'm sorry.

**Jose Farias:** I'll do mine, I have like three tickets in progress, they block each other, they're all like almost finished, I just need to work up the courage to execute on the migrating workspaces from big Ns to UIDs. It's hairier than I thought, to be honest, we're code complete, but we're going to touch a bunch of tables and two of them are like in the millions, like multiple millions of rows. So when I was joining the call, we were in the middle of a point in time recovery checkpoint with Render, which means it's checkpointing our database so we can return to this point in time if necessary. I want it to complete before I execute so that if something goes wrong, we can just revert. What that means is we would lose all the data from 7 a.m. my time today to like right now, something like that, which shouldn't be that many rights, but it can happen. I think that's fine. I don't think we're doing anything that can't be redone. All the more reason to do it now before we launch, to be honest, I will be putting the app in a maintenance mode. Which basically means the public pages stay available, but everything else is locked down. You'll see a migration or a maintenance in progress screen instead of like the actual usual app. You won't be able to use the admin or the dashboard, and that is so that you don't write to the database while we're juggling IDs. I expect it to take like about two hours, something like that. Other than that, we should be good. After I merge that, the other two tickets that I have in progress should be straight shots. That's it. Let me know if anyone has any objections to me putting it in maintenance mode.

**Stevie Kim:** No, but when are you planning to do that?

**Jose Farias:** So this morning?

**Jose Farias:** Sorry not to give a specific time.

**Stevie Kim:** Oh, no.

**Stevie Kim:** I just, yeah.

**Stevie Kim:** I mean, just we'll need to communicate it across, not just for Daniel and Marcel, but also just in the Ask CheckThat channel.

**Stevie Kim:** Yeah.

**Stevie Kim:** Because if they're in there, they're going to be like, you know, asking us like, what's going on?

**Jose Farias:** Yeah.

**Jose Farias:** Yeah, I can do that.

**Jose Farias:** So I have two messages I need to send. One is to verify the invitation behavior, which I know I didn't want to design by committee, but we didn't arrive at an answer. So I...

**Jose Farias:** Looks like we're gonna have to do that.

**Jose Farias:** And then this, I'll also ping the channel about this, both channels, CheckThat and ask, CheckThat.

**Pedro Steimbruch:** Wonderful.

**Jose Farias:** And that's it for me.

**Stevie Kim:** Um, yeah, so I'm just planning to do some more QA. I got a couple things done over the weekend. One of them was like a bug related to being able to click the whole row for the prompt index. So the prompt page. And so I fixed that. Um, and I mean, um, yeah, there's some, we don't, like, we don't have to click the whole row. We could just make the text look more like a link. The intention was to make it easy for people to understand that they're, where to find the prompt response and, you know, more information on each prompt. Um, because it was not, I mean, if you didn't scroll, if your cursor never went over that text, you would never know that that was clickable. Right. Um, but yeah, so that's fixed. If you do hover over a blank spot, though, on the prompt row, um, you can't, like, use some shortcuts like command, you know, to open up a new tab or right click to open up a tab. But that works everywhere else on the row. Um, so that's a little bit wonky. And I put it in the PR as a comment or as a commit message. So if we want to do something else and not have that whole clickable, but just to make sure the text is obviously clickable, then we can do that. I just don't know how to make that look good. Yeah, I think otherwise, if you're going to have me do it, it's going to be like a blue link underlined and we don't want that.

**Jose Farias:** That's all good. Just for my own curiosity, what are we doing currently? Are we wrapping the whole thing in an anchor tag or just a text?

**Stevie Kim:** So previously, it was just the text that had, yeah. And we're using Inertia and yeah. So both forms, I think Daniel had a concern that and further and. And the way I had fixed it or changed it did a full page reload, but I looked it up and it actually doesn't. So that's not a concern, but it did break the shortcuts and being able to right click and have the capability of opening up a new tab and stuff. So yeah, that's the part that I updated to fix that. But as I said, like the only thing that's a little wonky is that that only, that right click only works like for the text. You can't do it for the whole row. So, but again, we could come up with a different solution, but that's kind of an edge case and that's a super user kind of, you know, not the right click to tab, but some of the other shortcuts that that enabled are kind of more edge cases for super users, but you can still open it up in a new tab. Now you just have to be over the text. So it is a little bit inconsistent, but so, yeah. Again, I'm open to other ways of making that obvious to users that, you know, to get to that response page or the prompt details, whatever we're calling it.

**Stevie Kim:** Sounds good.

**Jose Farias:** Yeah, for what it's worth, table links are always, they're always a nuisance.

**Jose Farias:** Yeah.

**Jose Farias:** There's all kinds of considerations.

**Stevie Kim:** I haven't done UI development also for a very, very, very long time.

**Stevie Kim:** That's all good. But yeah, besides that, just got a couple, I got something else done. I can't even remember what it was. It's something simple, but yeah, I did try to put some, get some more clarity on some tickets that didn't have either clarity or that maybe weren't, maybe we're already taken care of. Yeah. They just hadn't had their status changed. So kind of waiting on that. Otherwise, we're in a really good spot. And I'm just going to continue QA. I think I'm in the phase three of the QA doc, partially through that, like the competitor's page or the competitor's section I already did. And then prompts. I mean, I've already dug through that a lot over the past couple of weeks, but I'm going to do, you know, like the official QA pass. On that, too, today. That's it for me.

**Jose Farias:** Perfect. So are we calling off the meeting this afternoon?

**Stevie Kim:** Yeah, I think that we could use that time back for focus time.

**Pedro Steimbruch:** Sounds good.

**Jose Farias:** All right.

**Jose Farias:** Thanks, everyone.

**Jose Farias:** Thanks.

**Jose Farias:** Seeing you all.

**Jose Farias:** Bye.

**Jose Farias:** Bye-bye.

**Jose Farias:** Bye.
