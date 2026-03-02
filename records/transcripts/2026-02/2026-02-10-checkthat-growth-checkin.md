# CheckThat Growth Checkin

<metadata>
date: 2026-02-10
time: 17:21 UTC
duration: 24 minutes
organizer: saskia@growthx.ai
participants: Jason Gong, Stevie Kim, Kavishka Kanayake, Saskia Wartnaby
fathom_recording_id: 121257223
fathom_url: https://fathom.video/calls/560667608
share_url: https://fathom.video/share/B7DHYH98qxGxxfnuZqRsaq9hM4tqACoQ
source: fathom
enriched_on: 2026-03-01 00:00 UTC
speaker_note: Only four speakers participated in the recorded portion of this meeting (Jason Gong, Stevie Kim, Kavishka Kanayake, and Saskia Wartnaby). Other calendar invitees may have been present but did not speak during the recorded segment.
</metadata>

---

## Summary

The CheckThat growth team aligned on engineering priorities and ticket workflow by introducing a new process where the "To Do" column is limited to the top 5 growth tickets, ranked internally by the growth team while engineering uses low/medium/high priority for their own system. Two urgent workflow tickets assigned to Daniel take priority, followed by three interlinking tickets addressing critical indexing issues that can be bundled into a single PR. The team also identified a new ticket need for heading style improvements (H2/H3/H4) to improve content skimmability on detailed answer pages, and flagged that adding more cross-links to brand pages will require design input to maintain readability.

---

## Context

CheckThat is GrowthX's AI visibility software product that launched recently. This was a weekly growth sync between the CheckThat growth team (Jason, Saskia, Kavishka) and Stevie Kim, who leads CheckThat engineering. Post-launch, the team shifted from "ship everything possible" to a more deliberate pace, discovering that some architectural decisions weren't fully thought through—like how categories are treated in the system. With the product now live and user feedback coming in via Intercom and session recordings, the team is working to help users reach the "aha moment" faster. A new Friday strategy session with Daniel (who appears to be another engineer), Marcel, and Stevie is being established to bridge growth priorities and engineering execution.

---

## Relevance

**To CheckThat Product & Engineering:**
- New "top 5" prioritization discipline reduces engineering distraction and clarifies growth team expectations. All new tickets now flow through Triage for formal review before backlog/work column placement.
- Three interlinking tickets addressing indexing problems are critical to user discovery and can be batched into one PR — a quick win with medium priority.
- Heading structure work (H2/H3/H4 improvements) is deprioritized to backlog but signals UX friction in detailed answer pages that limits content skimmability.

**To CheckThat Delivery & Content:**
- Designer/design thinker (potentially Renan) may be needed to shape the "Related brands" section on brand pages as growth tickets add more cross-link data. Current layout is already dense.
- Workflow improvements and new content pipelines are being scoped separately from backend architectural work, allowing lighter-weight content engineering to proceed in parallel.
- Post-launch content regeneration (e.g., for article rewrites) is deprioritized until underlying workflows are fixed—manual regen is acceptable as interim solution.

**To GrowthX Account Health:**
- Engagement signal: CheckThat is actively shipping improvements and iterating on architecture based on user feedback. Team is balancing velocity with thoughtful design.

---

## Overview

- **New Prioritization Process:** To improve engineering focus, the "To Do" column will be limited to the top 5 growth tickets. The growth team will rank these tickets internally, as the engineering team uses the `low/medium/high` priority field for their own system.
- **Top 5 Tickets:** The immediate focus is on two workflow tickets (assigned to Daniel) and three interlinking tickets. The interlinking tickets are a higher-medium priority, as they address critical indexing issues.
- **Design Support Needed:** The "Related brands" section on brand pages is already dense; adding more cross-links requires design input to maintain readability. The team will explore pulling in design-focused resources like Renan.
- **New Ticket Process:** All new tickets must be filed in the "Triage" column. This ensures they are reviewed and formally prioritized by the engineering team before being moved to the backlog or a work column.

---

## Key Topics

### Engineering Workflow & Prioritization

  - **Problem:** The "To Do" column is cluttered, making it difficult for engineering to identify and execute on top priorities.
  - **Solution:** Limit the "To Do" column to the top 5 growth tickets.
      - The growth team will rank these 5 tickets internally.
      - The engineering team will use the `low/medium/high` priority field for their own system.
  - **New Ticket Flow:** All new tickets must be filed in "Triage" for formal review and prioritization by the engineering team.

### Top 5 Growth Tickets

  - **Urgent Priority (Assigned to Daniel):**
      - Two workflow tickets.
  - **Higher-Medium Priority (Unassigned):**
      - Three interlinking tickets.
      - **Rationale:** These tickets address critical indexing issues that are currently blocking user discovery.
      - **Note:** These tickets are low-lift and can be bundled into a single PR.
  - **Deprioritized:**
      - The ticket for regenerating articles.
      - **Rationale:** This is not urgent and can be handled manually until the underlying workflows are updated.

### Design & Layout Needs

  - **Problem:** The "Related brands" section on brand pages is already dense. Adding more cross-links without design input will make the page unreadable.
  - **Solution:** Pull in design-focused resources (e.g., Renan) to shape the layout and ensure a good user experience.

### New Ticket: Heading Structure

  - **Problem:** The current heading structure hinders skimmability, especially on detailed "answer" pages.
      - `H3` is too similar to bolded text.
      - No `H4` style exists, forcing content creators to use bolded text as a workaround, which further reduces clarity.
  - **Proposed Solution:**
      - Increase the font size of `H2` and `H3`.
      - Introduce a distinct `H4` style.
  - **Action:** Saskia will create a ticket for this in the "Triage" column.

---

## Decisions & Commitments

- **Top 5 Growth Ticket Limit:** The "To Do" column will be limited to the top 5 growth tickets, ranked by the growth team internally. Engineering will use the low/medium/high priority field for their own system.
- **New Ticket Flow:** All new tickets must go to Triage first for formal review by the engineering team before moving to backlog or work columns.
- **Priority Tiers for Current Top 5:** Two workflow tickets (assigned to Daniel) are marked urgent. Three interlinking tickets are higher-medium priority and can be bundled into one PR.
- **Design Input on Brand Pages:** Layout design work will be needed for the "Related brands" section before adding more cross-linking content. Team will explore pulling in design resources (e.g., Renan).
- **Article Regeneration:** Deprioritized until underlying workflow improvements are complete. Manual regen is acceptable as interim solution.
- **Weekly Cadence:** Growth team will sync with engineering weekly to ensure the top 5 tickets remain correctly prioritized.
- **Friday Strategy Session:** New weekly strategy meeting Friday with Daniel, Marcel, and Stevie to translate growth discussions into engineering priorities. Jason to confirm attendance with Marcel.

---

## Action Items

**Saskia Wartnaby (GrowthX)**
- Duplicate Glean pricing assignment in Content OS; add comment noting AI vs .com source
- File Linear ticket re: heading styles (H2/H3/H4); set low priority; place in Triage

**Stevie Kim (GrowthX)**
- Deprioritize regenerate articles ticket in Linear

**Jason Gong (GrowthX)**
- Ask Marcel re: Fri strategy session invite

---

## Transcript
**Jason Gong:** This meeting is being recorded.

**Saskia Wartnaby:** Kavishka, just quickly, when I googled Glean pricing, both sites came up.

**Saskia Wartnaby:** Is there a way I can indicate, like, maybe just in the content OS, which one I chose?

**Saskia Wartnaby:** Because I did search, and there is only one assignment for Glean pricing.

**Saskia Wartnaby:** So should I maybe make another one?

**Kavishka Kanayake:** Yeah, I think just duplicate the assignment, and then maybe, like, add a comment or something, saying, you this is AI and this is .com.

**Saskia Wartnaby:** Okay, I'll do that.

**Saskia Wartnaby:** Hi, Stevie.

**Stevie Kim:** Hey, how's it going?

**Jason Gong:** How was the week after Check That Launching?

**Jason Gong:** Is it crazier or is it more chill?

**Stevie Kim:** It's both in different ways.

**Stevie Kim:** So I think things have slowed down in the sense of we're not just trying to ship, you know, everything that we can possibly ship.

**Stevie Kim:** We're trying to slow down to go faster because, you know, some things weren't thought through from the beginning that ended up, you know, making things difficult.

**Stevie Kim:** Like the way we were treating category categories and stuff is this major architectural need versus like, no, this is just a way to group thing information together.

**Stevie Kim:** So Daniel's Daniel did some changes that I haven't actually.

**Stevie Kim:** Been a week for to be able to look at on the onboarding flow and we'll be making some changes.

**Stevie Kim:** then, yeah, so certain things have been just like, okay, let's think through things a little bit more.

**Stevie Kim:** But then there's also like more surface area because now we have intercom, we have post hoc analytics and recordings to go through.

**Stevie Kim:** And so, yeah, it's a little bit different, but I don't think it's ever going to, maybe a year from now, we'll be like, okay.

**Saskia Wartnaby:** Maybe, maybe.

**Stevie Kim:** Maybe.

**Stevie Kim:** But yeah, it feels good because, yeah, there's different things to focus on.

**Stevie Kim:** Speaking of which, one of those things is going to be tackling some of those growth tickets.

**Stevie Kim:** And so I kind of wanted to make sure.

**Stevie Kim:** I did move some from to do to backlog because everything was in to do.

**Stevie Kim:** So it was really hard to like, just kind of, you know, narrow down prioritization.

**Stevie Kim:** I kept the ones that you mentioned last week, but I also kept some ones that I wasn't sure about.

**Stevie Kim:** So if you could kind of go through what is still in, you know, marked labeled as growth in to do to see to make sure I've got your priorities, right?

**Stevie Kim:** I mean, there's still a lot of tickets in there.

**Stevie Kim:** And so I might move some out that you're like, yeah, these aren't top priority.

**Stevie Kim:** Because I'm just trying to keep things a little bit cleaner for engineering to just be able to execute where I don't have to just, you know, tell them for every little thing, what's the priority.

**Jason Gong:** Yeah, let's do that now.

**Jason Gong:** think just like high level, basically, all of our tickets either fall into like one of three categories, I guess it's either about indexing.

**Jason Gong:** So it's like how everything links together.

**Jason Gong:** I'm going to go

**Jason Gong:** We actually made a little tag for that.

**Jason Gong:** Or it's about, like, the quality of the workflows, which is about, like, cool, these pages, you know, they kind of show up on Google, but they're all the way on page 10.

**Jason Gong:** And the main way to move that is to, you know, make the content better.

**Jason Gong:** And then the last bucket is kind of a little bit more of a mixed bag, but it's like, well, we want a new, you know, content pipeline for a new type of content.

**Jason Gong:** Or, you know, some of the things like this, it's like a quality of life.

**Jason Gong:** You know, I think we're spending a lot of time just, like, deleting and recreating pages that we're rewriting, and it would be nice to have a button.

**Jason Gong:** So everything fits into one of those categories.

**Jason Gong:** And then, yeah, I guess on priority, like, maybe, what is the best way to use this linear board so that kind of, that's communicated, like, as effectively as possible?

**Stevie Kim:** Yeah, so, like, I mean.

**Stevie Kim:** I you're like top five in to do.

**Stevie Kim:** Like right now, there's still too many.

**Stevie Kim:** For some reason, I thought I had removed enough to where it was like a little bit more manageable because then it's like if there's that many, then we don't know like the ranking accordingly.

**Stevie Kim:** But yeah, so I think just making sure we sink in this meeting to make sure the right things are in to do would be the best.

**Stevie Kim:** Everything else just needs to stay in backlog because, you know, we have non-growth tickets, just as many non-growth tickets, you know, in to do.

**Stevie Kim:** And so it just becomes so cluttered that we can't really, you know, prioritize very well.

**Stevie Kim:** So yeah, I think like the top five would be good.

**Stevie Kim:** And then, you know, on a weekly cadence, just making sure the right things are in the in that to do list would be really.

**Stevie Kim:** And then, and then within those five ranking them, like, you know, within the ticket, like I, like I said, okay, this is, this is really important to the growth team, this blocks something, and then, you know, I can change the, the priority accordingly, compare, comparatively, respective to the rest of the tickets we have.

**Jason Gong:** Cool.

**Jason Gong:** Um, all right, so that's, that's pretty straightforward, we can do the, um, let's see, okay, I, I think it's some combination of this, like, a lot of the indexing tickets are, like, comparatively much smaller, um, was there any ticket, like, just, I don't it's on the spot, but, like, here, where there was, like, a big question mark in your mind that might block them being worked on, or, like,

**Stevie Kim:** I think I got clarity on the ones that I needed to, I just, you know, opened up a discussion like in the comments for a couple of them, just to make sure that, you know, we understood.

**Stevie Kim:** think Daniel's got the context.

**Stevie Kim:** He said that he was going to start working on these this week, the workflow, I think, once.

**Stevie Kim:** Um, the answers, yeah, I think I got clarity where I needed to on the, on like where to put some of that information because right now the, that newer related brands is, um, there's kind of a lot there.

**Stevie Kim:** You know, um, and so, yeah, just trying to figure.

**Stevie Kim:** Figure out, like, how to best organize that information to where it's grokkable.

**Stevie Kim:** Like, you don't want just, like, this massive amount of content.

**Stevie Kim:** So I'm curious about, I think, yeah, think Savio would have the best context and then also just, like, you know, good design sense to be able to do that.

**Stevie Kim:** If you guys think that we need Ren on, you know, making sure, like, that newer information flows well, then we can pull him in.

**Stevie Kim:** But, yeah, if you guys have any strong opinions about how the page is and the sidebar, you know, nav should be designed, let me know.

**Stevie Kim:** That was, like, kind of the only.

**Stevie Kim:** That's only concern I had for adding content to brand pages.

**Jason Gong:** Should we think about there being different lanes for work?

**Jason Gong:** For example, if I just had five internal linking tickets, it's a little different than half those tickets are for internal linking, half those tickets are for workflow improvements.

**Jason Gong:** Like are those different people where it helps to have like one of each and then maybe there's even another group like Renan, George Mayne, for example, I see them more as like, you know, things that require a bit more product thinking or design.

**Stevie Kim:** Yeah, yeah, absolutely.

**Stevie Kim:** I mean, so the, I mean, they're not, they were just helping out, you know, for a short bit there.

**Stevie Kim:** But if they have bandwidth, you know, certainly.

**Stevie Kim:** The Check That team, the Check That team, engineering team is very experienced.

**Stevie Kim:** And incredibly, you know, like very senior, very can run with things.

**Stevie Kim:** But when it comes to like the shaping, the design side, you know, making sure it, you know, it makes sense within the page, I think that help there would be good.

**Stevie Kim:** So any tickets that are maybe less on the technical, more front end, if we can pull someone that has a lot of design sense, I think that would be beneficial to us.

**Jason Gong:** Okay, so the kind of the lanes are good, because I remember when we did this, like initially the ask was just cool, Ren, could you kind of brainstorm and think through how we would surface more data on these pages?

**Jason Gong:** And then that, they kind of just built in, I was like, oh, cool, that's, that's awesome.

**Jason Gong:** So that's like, maybe less kind of dealing with, like all the data and all the backend stuff.

**Jason Gong:** And it's more just the packaging of

**Jason Gong:** And shifting some things around, that's like one area.

**Jason Gong:** There's like the kind of more serious, like, hey, if we wanted a thing to like categorize brands differently or something, that would just be like a totally different kind of engineering ask.

**Jason Gong:** And then the last bucket is more workflow asks, like, hey, our workflow for alternatives pages could be better in this or that way.

**Jason Gong:** Like, it seems like those are all different people.

**Stevie Kim:** I would say that the workflows will, I mean, eventually the whole engineering team will need to be comfortable with working on them because we use workflows internally, right?

**Stevie Kim:** Like, so that's just, it's not just a content thing.

**Stevie Kim:** But for the content ones right now, yeah, it's just kind of whoever has the extra time because we were just hyper-focused on launch.

**Stevie Kim:** So I wouldn't say, I would say that those, you know, blend in with the other deeper engineering.

**Stevie Kim:** But, yeah, for the content, they're lighter weight workflows than, you know, say the probing ones, right?

**Jason Gong:** Oh, okay.

**Jason Gong:** I see.

**Jason Gong:** Okay.

**Jason Gong:** That's helpful.

**Jason Gong:** I think I just want to make sure we do a good job, like, kind of keeping that queue always filled, like, not just having a bunch of tickets just for design, then we're leaving other available resources.

**Jason Gong:** Kind of, you know, like, not underutilized, for lack of a better word, because there's just so much.

**Stevie Kim:** Yeah, there's definitely no, I don't think anyone's underutilized.

**Jason Gong:** Yeah, I know.

**Jason Gong:** Or just how could we pull, you know, as much.

**Stevie Kim:** yeah, yeah.

**Stevie Kim:** As I said, like, for more of, like, the layout, the design, I don't, you know, like, we do only have maybe one person that is, want.,兄.

**Stevie Kim:** Thanks

**Stevie Kim:** Has that, you know, sense versus, so if we can pull someone in that's not working on anything critical and stuff on, like, the content OS stuff that, like, Ren or, that would be great.

**Stevie Kim:** But for little stuff like this, I mean, I don't think, like, we need, you know, like, someone, it's, could you actually go back real quick to that related section, though, on the brand page?

**Stevie Kim:** Because I did kind of want it, like, if you scroll down, yeah, all the way, yeah, so the above that, so that's what I was kind of trying to, you know, I got clarity on, you know, a little bit of clarity, but yeah.

**Stevie Kim:** So, like, a lot of the related information that some of those tickets are specifically, like, for cross-linking and stuff.

**Stevie Kim:** That might need a little design love, because it already is kind of a lot that's in there right now.

**Jason Gong:** Oh, I see.

**Stevie Kim:** Just like this.

**Stevie Kim:** adding to it is going to be a little bit gnarly looking, maybe.

**Jason Gong:** Okay.

**Jason Gong:** That's a good call.

**Jason Gong:** Oh, related categories.

**Stevie Kim:** think that one should be in to do, right?

**Stevie Kim:** Wasn't that?

**Stevie Kim:** Or, I can't remember.

**Stevie Kim:** Was that one of the cross-linking ones?

**Stevie Kim:** Because there were, like, there were a few, and so it would be easy to do, like, the ones that are very similar to each other.

**Jason Gong:** Yeah, there's quite a lot of interlinks.

**Stevie Kim:** Because those can be, like, done in the same PR, probably.

**Stevie Kim:** If it's basically doing the same thing, just for different...

**Jason Gong:** Yeah, it's kind of these two.

**Jason Gong:** All right, is there anything else worth calling out, Vishka and Saskia, like tickets?

**Jason Gong:** Do you think this rough cluster of tickets is the most important?

**Saskia Wartnaby:** Looks good to me.

**Kavishka Kanayake:** Yeah, and if I'm being honest, the one about regenerating articles, now that I think about it, probably not super urgent.

**Kavishka Kanayake:** Like, we'll only really need to regenerate articles if the work, like, the underlying workflow is updated and fixed, So this will probably have to come, like, I could do it manually until we have the workflows done.

**Kavishka Kanayake:** So we can deprioritize that.

**Jason Gong:** That's pretty cool.

**Jason Gong:** Yeah, I think that's it.

**Stevie Kim:** And within those five...

**Stevie Kim:** Like, you've got the urgent on the workflows or whatever, but what about the other ones?

**Stevie Kim:** Are they all median, like, median priorities?

**Stevie Kim:** You don't have to change the prioritization, but is that about right, or does any, like, two, one or two stand out?

**Jason Gong:** I think it really is, like, it really is these two.

**Jason Gong:** Well, those are already assigned to Daniel, right?

**Stevie Kim:** Like, these, the other ones are assigned, except for 512 is another one that's assigned.

**Jason Gong:** Yeah, so minus those, I think these three basically are all interlinking.

**Jason Gong:** I would put them lower priority than the workflow, but, like, as a whole, like, we have a lot of indexing problems, so it's still, yeah, like, I would put that as, like, a higher or medium versus urgent.

**Stevie Kim:** Okay, yeah, because someone else can work on those if Daniel's going to tackle the workflows.

**Jason Gong:** Yeah.

**Jason Gong:** That's it on our end.

**Jason Gong:** Yeah, so let me know how we can help, and then we'll keep an eye on these tickets.

**Jason Gong:** I'm very bad at checking linear sometimes, but if there is, yeah, just flags and comments, and we'll reply if there's any outstanding questions.

**Stevie Kim:** Yeah, we should be able to get to those pretty quickly.

**Stevie Kim:** I mean, they don't seem like a big engineering lift, so that's just a matter of, like, working on finishing up some other priorities that we've got going on.

**Stevie Kim:** So it'd be more like probably end of the week, towards the end of the week.

**Jason Gong:** Sounds good.

**Jason Gong:** I know all the product stuff is, like, important.

**Jason Gong:** And spending a bunch of money driving more sign-ups, but if they hit a wall, it kind of sucks.

**Stevie Kim:** Yeah.

**Stevie Kim:** Yeah, yeah.

**Stevie Kim:** So we're working on kind of helping them get to that aha moment a lot faster or at all for them after.

**Jason Gong:** You know, if we're doing some sort of like road mapping session, Marcel mentioned it in the office last week.

**Stevie Kim:** So we're going to do, so we did update some meetings because, you know, that was always the intention post-launch.

**Stevie Kim:** So we're going to, engineering, we're going to get rid of the daily stand-up and go back to our like engineering focused weekly stand-up, or not stand-up, but kind of discussion session.

**Stevie Kim:** But a lot of the discussion is going to happen asynchronously in Slack.

**Stevie Kim:** And Fridays, it's going to be Daniel, Marcel, and I, and if you're not invited, Daniel said that, know, you can join when.

**Stevie Kim:** You have time or bandwidth, but that's going to be kind of a messier strategy meeting that basically I'm going to do a lot of just kind of translating what, you know, their thoughts are and discussions are and trying to guide that as much as I can, but translate that to, you know, what engineering needs to work on for the following week kind of thing.

**Jason Gong:** That's good.

**Jason Gong:** I'm to talk to Marcel later.

**Jason Gong:** I'll just ask him if he wants me there.

**Jason Gong:** If not, I'll focus on growing and selling.

**Jason Gong:** It's on our side.

**Jason Gong:** Appreciate it.

**Saskia Wartnaby:** Jason, I just have a question for you before you go.

**Jason Gong:** Yes.

**Saskia Wartnaby:** All right.

**Saskia Wartnaby:** Stevie, if you want to go, you're...

**Jason Gong:** Yeah, feel free to drop.

**Stevie Kim:** Well, thanks guys for letting me take...

**Stevie Kim:** Kind of like take that over a little bit, but I just thought it'd be, I'm trying to kind of clean stuff up so we can narrow our focus a little bit tighter.

**Saskia Wartnaby:** Oh, sure.

**Saskia Wartnaby:** Thank you so much.

**Stevie Kim:** Take care.

**Stevie Kim:** Bye.

**Saskia Wartnaby:** Bye.

**Saskia Wartnaby:** Very quick one.

**Saskia Wartnaby:** I did run this by Kavishka, but I just wanted to run by you as well.

**Saskia Wartnaby:** Let me just find the tab and share my screen.

**Saskia Wartnaby:** Okay.

**Saskia Wartnaby:** Share screen.

**Saskia Wartnaby:** Oh, turn my video.

**Saskia Wartnaby:** Where is the share screen button?

**Jason Gong:** See it?

**Saskia Wartnaby:** Oh, my goodness.

**Saskia Wartnaby:** Just kill me.

**Saskia Wartnaby:** Okay.

**Jason Gong:** It's been a long day.

**Jason Gong:** Can you guys see this phone?

**Jason Gong:** Yep.

**Saskia Wartnaby:** Okay.

**Saskia Wartnaby:** So, basically, I wanted to ask you if it's worth filing it.

**Saskia Wartnaby:** Ticket about the headings.

**Saskia Wartnaby:** So I know we don't normally, so first of all, the H3 is very similar to the bolded text.

**Saskia Wartnaby:** And this becomes an issue when you want an H4.

**Saskia Wartnaby:** So I know we're not really like supposed to use H4s, but a lot of the articles that generate are so detailed that like you have an H3 and then there are headings underneath that.

**Saskia Wartnaby:** And currently the AI kind of just bolds it and you end up with these really long, weird paragraphs or like bullet lists that aren't bullet lists.

**Saskia Wartnaby:** And it's really weird.

**Saskia Wartnaby:** So I've been using bolder text as an H4, but that is really similar to the H3.

**Saskia Wartnaby:** So my request would be, can we make the H2 a bit bigger, the H3 a bit bigger, and then add an H4 and just have that like distinction between the headings?

**Saskia Wartnaby:** Because right now it's really hard to skim read.

**Jason Gong:** That sounds fun to me, I guess.

**Jason Gong:** Yeah, just feel like you should avoid them if possible, but, you know, I'm thinking through, like, the alternatives articles, and it's just, like, you have multiple layers, so.

**Saskia Wartnaby:** Yeah, it's mainly for the, I've noticed it's mainly for the answer pages, where it really dives into detail, and, yeah, I just, it's really not skimmable at the moment, and with H4s, just a few of them would really help, but mainly the problem is the H3s being so small.

**Saskia Wartnaby:** Yeah, that makes sense.

**Jason Gong:** Um, one, one tactical thing for tickets, it seems like the engineering team wants to use the, like, low, medium, high for their, um.

**Jason Gong:** Yes, it's, it's, it's, like, didn't want us to do that.

**Jason Gong:** Maybe, I wonder what we could do, like, I guess we could do, like, uh, maybe for all these tickets, um, I guess we have it here, so on, Yeah.

**Jason Gong:** Tickets with this, I guess that'll take place, but then tickets without, uh,

**Jason Gong:** Um, if you can just do like a, you know, uh, okay, you know, like, let me do that.

**Saskia Wartnaby:** And then I'm just going to put this ticket in backlog.

**Jason Gong:** Is that right?

**Jason Gong:** Uh, yeah, put it in, I actually, I think you should put it in triage.

**Saskia Wartnaby:** Okay.

**Jason Gong:** So I think the flow is like everything is in triage, Stevie and the team look at periodically and then they'll move it into like another column.

**Saskia Wartnaby:** Okay, cool.

**Saskia Wartnaby:** And so just add the priority.

**Saskia Wartnaby:** I'll just put it as low.

**Jason Gong:** Yeah, like I was just saying, maybe we could just do something like this.

**Jason Gong:** Just add it to the font.

**Jason Gong:** Um, cool.

**Jason Gong:** All right.

**Jason Gong:** Well, you shared it.

**Jason Gong:** Oh, Oh, no.

**Jason Gong:** think I could.

**Saskia Wartnaby:** We're good for now.

**Jason Gong:** The workflows and stuff are running, so fingers crossed that stays and we can use Fathom.

**Saskia Wartnaby:** Yeah.

**Saskia Wartnaby:** All right.

**Saskia Wartnaby:** Cool.

**Saskia Wartnaby:** Thank you, Jason.

**Saskia Wartnaby:** Thanks Kavishka.

**Kavishka Kanayake:** See you.

**Saskia Wartnaby:** Bye.

**Saskia Wartnaby:** Bye.
