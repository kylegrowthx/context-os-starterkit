# Lane Sync: Client Ops Kick-Off

<metadata>
date: 2025-11-04
time: 18:00 UTC
duration: 32 minutes
organizer: daniel@growthxlabs.com
participants: Marcus Derencius, Stevie Kim, Nicolas Castellanos, Andi Bailey, Daniel Lopes, Kirkland Gee, Suleiman
fathom_recording_id: 99099211
fathom_url: https://fathom.video/calls/462001431
share_url: https://fathom.video/share/53oy7gQKDKqNkJZ6ZCFH4CWbz7tySyo1
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

GrowthX's client ops team aligned on urgent delivery priorities to handle a growing backlog of agentic pipelines and critical publishing automation. Andi Bailey prioritized unassigned tickets, identifying Webflow (expansion opportunity), Search.ai (30 articles/week), Otto, and Tavern as high-priority pipelines to start immediately. The team also confirmed that the critical Webflow table formatting bug is fixed, unblocking automated publishing workflows — Marcus will implement fixes as teams reopen publishing tickets. Nicolas is building a post-processing workflow to fix persistent code block formatting errors in the "Strappy" pipeline, which Stevie will replicate for agentic pipelines this week.

---

## Context

This is a weekly internal sync for GrowthX's client operations and delivery team. The group manages the production pipeline for client content and automation work, including content generation pipelines, publishing workflows, and template systems. Stevie Kim leads the team, with Marcus, Nicolas, and Kirkland handling pipeline development and fixes. Andi Bailey represents the customer success side, highlighting priority client needs and capacity constraints. Daniel Lopes organizes from the broader GrowthX team.

---

## Relevance

- **To GrowthX Delivery:** Critical blocker (Webflow table bug) is removed, enabling rapid scale-up of publishing automation. Team capacity increases as Marcus becomes available after Thursday and Nicolas returns from leave on Thursday. Post-processing workflow patterns (being developed for "Strappy" code block issues) will be reusable across new agentic pipelines.
- **To GrowthX Business Development:** Multiple client expansion opportunities flagged: Webflow (paying more for new agentic pipeline), Search.ai (30 articles/week demand requiring dedicated pipeline), and capacity recovery for team strain at Otto and Tavern. Manual publishing bottleneck (Suleiman published 30+ articles over the weekend) is critical risk to solve to prevent burnout and enable growth.
- **To GrowthX Clients:** Webflow, Search.ai, Otto, and Tavern will see accelerated pipeline builds this week. Publishing automation enables faster time-to-publication and reduces manual work, directly improving content velocity for clients.

---

## Overview

- **Top Priorities:** New agentic pipelines (Webflow, Search.ai, Otto, Tavern) and automated publishing.
- **Critical Blocker Removed:** The Webflow table formatting bug is fixed, unblocking the automation of publishing for multiple clients.
- **"Strappy" Pipeline Fix:** A post-processing workflow will be implemented to correct persistent code block formatting errors.
- **Team Capacity:** Marcus is available after Thursday; Nicolas returns Thursday; Stevie will focus on agentic pipeline backlog.

---

## Key Topics

### Client Priorities & Backlog

  - Andi prioritized the unassigned backlog to focus the team's capacity.
  - **High Priority:**
      - **Webflow:** New agentic pipeline for an expansion opportunity.
      - **Otto & Tavern:** Agentic pipelines to support teams coming out of strategy sprints and to alleviate team strain.
      - **Search.ai:** Agentic pipeline to support a 30-article/week volume.
  - **Medium Priority:** Airbyte, Diligent.
  - **Blocked:** Deep Grim (awaiting client info).

### Automated Publishing

  - **Problem:** Manual publishing is a major bottleneck (e.g., Suleiman published \>30 articles over the weekend).
  - **Solution:** Prioritize automating publishing workflows.
  - **Enabler:** The Webflow table formatting bug is fixed.
      - **Action:** Andi will ask teams to reopen relevant tickets.
      - **Action:** Marcus will implement fixes as tickets are reopened.

### Pipeline Fixes & Updates

  - **"Strappy" Pipeline (Code Blocks):**
      - **Problem:** Incorrect code block formatting persists in both old and agentic pipelines.
      - **Hypothesis:** The error originates in the outline generation step and propagates to the article.
      - **Fix:** Nicolas is testing a post-processing workflow for the old pipeline; Stevie will implement a similar fix for agentic pipelines.
  - **Glossary Pipeline:**
      - **Plan:** Copy the existing Base 10 glossary pipeline to fulfill a new client request.
  - **Template Generator:**
      - **Status:** In progress; the main challenge is ensuring high-quality, polished output.
  - **Sentinel One:**
      - **Status:** Final review today for a Thursday launch.

---

## Action Items

- **Andi:** Ask teams to reopen Webflow publishing tickets.
- **Marcus:**
    - Start the Search.ai agentic pipeline.
    - Implement Webflow publishing fixes as tickets are reopened.
    - Follow up on the spreadsheet-to-article generator.
- **Nicolas:**
    - Test the post-processing fix for the "Strappy" pipeline.
    - Build the comparator articles publishing pipeline.
- **Stevie:**
    - Implement a post-processing fix for "Strappy" agentic pipelines.
    - Focus on the agentic pipeline backlog (Otto, Tavern).
    - Copy the Base 10 glossary pipeline.

---

## Decisions & Commitments

- **Prioritize four high-impact pipelines immediately:** Webflow (expansion opportunity), Search.ai (30 articles/week demand), Otto and Tavern (post-sprint support). Stevie will own these alongside her existing backlog.
- **Accelerate publishing automation:** With the Webflow table bug now fixed, Marcus commits to implementing publishing fixes as teams reopen tickets. This is critical to prevent publisher burnout (Suleiman working 30+ articles/weekend).
- **Deploy post-processing workflows for code block errors:** Nicolas will finish testing the "Strappy" pipeline fix this week; Stevie will replicate the pattern for agentic pipelines. This fixes a critical quality blocker that's affecting both old and new pipeline outputs.
- **Maintain team capacity planning:** Marcus available after Thursday; Nicolas returns Thursday; Stevie focuses on agentic backlog. Publishing ticket reopenings will be handled by Marcus in parallel.

---

## Open Questions

- **Deep Grim pipeline:** Blocked pending client information. Andi tagged Eric to follow up (status unclear from this meeting).
- **Webflow publishing tickets:** How many tickets will teams reopen? Timeline for reopening?
- **"Strappy" code block root cause:** Is the issue truly in outline generation, or elsewhere? Nicolas and Stevie testing independent hypotheses — need to consolidate findings.

---

## Transcript
**Marcus Derencius:** This meeting is being recorded.

**Stevie Kim:** Hey, how's it going?

**Marcus Derencius:** Pretty good.

**Stevie Kim:** How are you?

**Stevie Kim:** Oh, pretty good.

**Stevie Kim:** It was a busy start to the work week on Monday.

**Marcus Derencius:** Let me get my phone.

**Marcus Derencius:** Let me share my view.

**Stevie Kim:** Oh, where are you at?

**Marcus Derencius:** I mean, the northeast of Brazil.

**Stevie Kim:** Nice, that's gorgeous.

**Marcus Derencius:** Yeah, it's a good place to do kite surfing.

**Marcus Derencius:** Oh, very I just did a little bit of kite surfing in my lunch break.

**Stevie Kim:** Oh my gosh, you're inspiring me.

**Stevie Kim:** I need to find a, well, yeah, I need to find a dog sitter so I can go somewhere for a couple weeks and go on a long surf trip.

**Stevie Kim:** I used to surf, but I don't, I haven't for about five or six years.

**Stevie Kim:** been, yeah, since like 2019.

**Marcus Derencius:** Okay, so, yeah.

**Marcus Derencius:** My home seat back in Brazil is a surf city.

**Marcus Derencius:** And this is a kite surfing city.

**Stevie Kim:** I've never done kite surfing.

**Stevie Kim:** That's always scared me because...

**Stevie Kim:** I feel like I'm too clumsy.

**Marcus Derencius:** There's too much going on.

**Marcus Derencius:** But here it is nice and safe.

**Marcus Derencius:** And other places can be, there's cats.

**Marcus Derencius:** Yeah, it's much easier than surfing.

**Stevie Kim:** Really?

**Marcus Derencius:** Yeah, yeah.

**Marcus Derencius:** that's, the gear is more advanced, but it's much easier.

**Stevie Kim:** Oh, see, I feel like anytime there's too much equipment, that's when I start to kind of, yeah, lose it.

**Marcus Derencius:** Yeah, no, that's a problem.

**Marcus Derencius:** But, yeah, here in this area of Brazil, they do a VIP service.

**Marcus Derencius:** they help you with everything.

**Marcus Derencius:** So if you go like Portugal or other places, you have to do everything on your own.

**Marcus Derencius:** So it's more risk.

**Marcus Derencius:** here, they watch you, they help you.

**Stevie Kim:** So that's why.

**Stevie Kim:** Nice.

**Stevie Kim:** Oh, that's perfect.

**Marcus Derencius:** Yeah.

**Stevie Kim:** I'm getting less, I'm getting, like, certain things, I feel like I'm getting more adventurous in my older age, and then other things, I'm getting less adventurous.

**Stevie Kim:** I'm like, if it takes too much time to prepare, or, you know, or, like, too many, I keep track of, I don't want to do that.

**Marcus Derencius:** But yet, I'm, I've never done skydiving, and I'm like, yeah, I'm finally, like, wanting to do that.

**Marcus Derencius:** Oh, really?

**Stevie Kim:** I don't get it.

**Stevie Kim:** Well, yeah, because, well, if you go with someone, and you're just, like, doing the tandem with an instructor, you don't have to worry about the equipment, so, that's where I'm at.

**Marcus Derencius:** Or you can learn how to fly an airplane, as Nico.

**Stevie Kim:** Oh, you're, you're getting your pilot's license, or you have it?

**Stevie Kim:** Nico?

**Nicolas:** Oh, sorry, I was, um, yeah, I'm getting it.

**Nicolas:** Uh, I'm, I'm still, like, I don't know, maybe now.

**Nicolas:** Oh, it's like 10 hours away from it, maybe five, something like that.

**Nicolas:** wow.

**Nicolas:** Yeah, I still need to do like, it's like navigate from like airport to airport during the night.

**Nicolas:** So I need to prepare for that one.

**Nicolas:** And then I can, I think I can do the test and get the license.

**Stevie Kim:** Oh, wow.

**Marcus Derencius:** That's cool.

**Stevie Kim:** Congratulations.

**Stevie Kim:** You're super close then.

**Nicolas:** Yeah.

**Nicolas:** But I think I'll never do skydiving.

**Nicolas:** I'll only fly with wings.

**Stevie Kim:** Not just a lot of them.

**Stevie Kim:** That's too funny.

**Stevie Kim:** Cool.

**Stevie Kim:** Well, we can just get started.

**Stevie Kim:** We kind of have like, we were in a good position, I think on mid-cycle review, but I think we just got a lot of new tickets or something because looking at, there's like a ton of new ones that are unassigned.

**Stevie Kim:** Okay.

**Stevie Kim:** Okay.

**Stevie Kim:** And we still have a lot of agentic ones to do, but I've definitely picked up the pace on that.

**Stevie Kim:** And so we're in a better spot there.

**Nicolas:** I think I'll be back.

**Stevie Kim:** Oh, yeah.

**Nicolas:** Probably Thursday.

**Stevie Kim:** Oh, good, good.

**Stevie Kim:** Yeah, because you're only supposed to be gone in two cycles, I think.

**Stevie Kim:** Yeah.

**Stevie Kim:** But I think this is going on number four.

**Stevie Kim:** Cool.

**Stevie Kim:** No, that's really good to know.

**Stevie Kim:** Okay.

**Stevie Kim:** How has that gone?

**Nicolas:** Anyway, just out of curiosity.

**Nicolas:** Good.

**Nicolas:** I mean, we have the templates done.

**Nicolas:** We have guides done.

**Nicolas:** Guides are like blog posts, but in a different place.

**Nicolas:** We got the templates.

**Nicolas:** Now, what I'm trying to finish is the template generator, but pipeline for automatically just generating templates.

**Nicolas:** It's a bit of a challenge because they need to be super polished.

**Nicolas:** figure out that are

**Nicolas:** And, and everything, but it's, we're slowly getting there.

**Stevie Kim:** Very cool.

**Stevie Kim:** Nice.

**Stevie Kim:** Okay.

**Marcus Derencius:** Okay.

**Marcus Derencius:** So.

**Marcus Derencius:** And hopefully also on similar note, I'm also finishing the Sentinel one.

**Marcus Derencius:** That was taking half of my time during the week, the last two weeks.

**Marcus Derencius:** So they are supposed to do a final review today to know if you can launch the site on Thursday.

**Marcus Derencius:** So, so maybe I have more ability to see as well.

**Stevie Kim:** Okay.

**Stevie Kim:** Great.

**Stevie Kim:** Yeah, I actually, so for some reason in my mind, I thought like that was part of some of what you were doing was agentic pipelines, but then they, you know, the ME pinged me and they asked when their agentic pipeline was coming.

**Stevie Kim:** So I just did a quick one yesterday, last night.

**Stevie Kim:** Reviewing that.

**Stevie Kim:** So if there's anything that needs to be in the agentic pipeline, like I just took it off of their, you know, created it off their, like simple old pipeline, but I think you're working on something else, right?

**Marcus Derencius:** Is it like public?

**Marcus Derencius:** Kirkland was working most on the agent pipelines and he was doing the reviews.

**Marcus Derencius:** I was doing Sentinel One, that's for the PSO pages.

**Marcus Derencius:** And also fixing a lot of bugs.

**Marcus Derencius:** So I was not doing an agentic pipeline, so yeah, you have to know which ones the latest templates we are using to, is there something, there's a new one.

**Stevie Kim:** Perfect then.

**Stevie Kim:** Okay, so this is like the ticket that I feel is just haunting me.

**Stevie Kim:** Publishing.

**Stevie Kim:** Publishing.

**Nicolas:** Yeah, got a ton of the, not a ton, but like the main three issues fixed.

**Nicolas:** And right now I'm working on, they want to limit the related posts they send to just three.

**Nicolas:** I got that in place.

**Nicolas:** And also there's still an issue with the code blocks.

**Nicolas:** I fixed most of them, but then there is some weird thing on the current pipeline that's like, for some reason, like adding code blocks to pieces that, where it shouldn't.

**Nicolas:** I think the issue, it's not the pipeline, but maybe the assignment, it should get fixed probably by the authentic pipeline.

**Nicolas:** Because the pipe, the authentic pipeline will be able to like detect that it's like messing up things and adding code blocks where it shouldn't.

**Nicolas:** But I'm creating a workflow to make those fixes using AI in the meantime.

**Stevie Kim:** Well, so they already have an agentic pipeline.

**Stevie Kim:** I created them one long time ago.

**Nicolas:** I'm not using it yet because they want to have all fixed on the old one and then apply the same fixes to the agentic one.

**Stevie Kim:** Right, right.

**Stevie Kim:** So it's blocked because of that.

**Stevie Kim:** I did everything except for just waiting for those changes, but I was going to say that it's still having the code generation issue as far as the formatting goes in the agentic pipelines.

**Nicolas:** You still get those issues in the agentic one?

**Stevie Kim:** Yeah.

**Nicolas:** Yeah.

**Nicolas:** That's good.

**Stevie Kim:** Okay.

**Nicolas:** Yeah, I'm looking on this workflow to just go through the content and fix everything that doesn't make sense.

**Nicolas:** That's good.

**Nicolas:** Yeah.

**Stevie Kim:** I'll you

**Stevie Kim:** Maybe I'll play around with the instructions because I was just waiting on your fix, but if you're still having issues with it, then maybe I'll just try to fix it in the prompt and see if that works.

**Stevie Kim:** You know, it might be something that we need.

**Stevie Kim:** It's probably what we need is the post-processing workflow specifically for that.

**Stevie Kim:** It just sometimes, like, you just have to be really careful about it rewriting other parts of the article.

**Stevie Kim:** But that sounds like it's probably going to have to have a post-processing step to fix that.

**Nicolas:** Yeah, what I saw in this case for this particular issue that keeps happening is that even the outline gets, like, generated in the wrong way.

**Nicolas:** It gets, like, backticks on pieces of the outline when it shouldn't be.

**Nicolas:** And I think that is what it's being, like, dragged into.

**Nicolas:** The article, because if the outline, it's wrong formatted, then probably that's what making the actual article get bad.

**Stevie Kim:** Well, in the Agentec Pipelines, though, they're not using any outline, so, yeah.

**Nicolas:** Yeah, I hope, that's why I was hoping the Agentec Pipeline wouldn't have these issues.

**Stevie Kim:** Yeah.

**Nicolas:** We will be able to figure it out, but it's super weird, because, I mean, it's almost worse, I think.

**Stevie Kim:** But, yeah, I'll try this week to do a post-processing step to fix that, and the Agentec ones, and see how far I can get with that.

**Nicolas:** Okay.

**Marcus Derencius:** And can I help?

**Marcus Derencius:** Like, I tried to fix, in other pipelines, it was also breaking the code blocks.

**Marcus Derencius:** I think it was related to Strap, as well, so working, right, so.

**Marcus Derencius:** So, if there's an example of where it's breaking.

**Marcus Derencius:** I get my code code to refine the prompts.

**Nicolas:** But it's not only that, it's adding like backticks to pieces of content when it doesn't make sense.

**Nicolas:** My bet is it's the outline that has them.

**Nicolas:** And because of that, it's generating the article with those.

**Nicolas:** What I have right now, it's about to merge.

**Nicolas:** It's up here that it's basically another workflow that will clean up the article.

**Nicolas:** Yeah, maybe that will fix it.

**Nicolas:** I still need to test it.

**Nicolas:** I'll merge it and give it a few runs and see if that fixes it.

**Nicolas:** But it should be almost there.

**Marcus Derencius:** Well, yeah.

**Stevie Kim:** No, that's good to know.

**Stevie Kim:** Because that wouldn't be applicable to the agentic one.

**Stevie Kim:** So it'll just need a separate step.

**Stevie Kim:** So I won't be blocked anymore on that.

**Stevie Kim:** So I'll finish the strappy one because that's all I was kind of waiting on, I

**Stevie Kim:** I think.

**Stevie Kim:** And then after that, are you going to do the publishing ticket then?

**Nicolas:** What's the publishing about?

**Stevie Kim:** Sorry.

**Stevie Kim:** That's just actually on the automation side.

**Stevie Kim:** So they gave an example of a pipeline.

**Nicolas:** we just talked about for the comparator articles.

**Stevie Kim:** Yeah.

**Nicolas:** Yeah, yeah, I'll do that.

**Stevie Kim:** Cool.

**Stevie Kim:** Okay.

**Stevie Kim:** And then I thought Daniel was going to take this, but yeah, it's assigned to him, but and it's not critical.

**Stevie Kim:** So I'm going to just leave that assigned to him for now.

**Stevie Kim:** And

**Stevie Kim:** Yeah, that's not, that's, I think we can just kind of leave that as is, because it's not, I think we have, like, more critical ones that we need to focus on.

**Stevie Kim:** This one, let's see.

**Stevie Kim:** Oh, yeah, this is the outline that they're requesting.

**Stevie Kim:** And I honestly think everybody, for the agentic pipelines, they're all going to want a kind of draft or outline step, because a lot of clients want to review the outline before it goes through the pipeline.

**Stevie Kim:** Oh, I'm sorry, I'm sorry, my bad.

**Stevie Kim:** I got confused about what this ticket was.

**Stevie Kim:** This is a glossary ticket.

**Stevie Kim:** Okay, so, yeah, Daniel already made a glossary pipeline for base 10, and so, we should be able to just use that.

**Stevie Kim:** Copy, okay.

**Stevie Kim:** Yeah.

**Marcus Derencius:** Do we have the pipeline here?

**Marcus Derencius:** What's that?

**Marcus Derencius:** That can copy?

**Stevie Kim:** Yeah, yeah.

**Stevie Kim:** So the base 10 one, I'll just link it and I'll take it.

**Stevie Kim:** Okay, okay.

**Stevie Kim:** This one's a different base 10 pipeline.

**Stevie Kim:** But yeah, I'll, because they do have a few that are in various, like workspaces.

**Stevie Kim:** Okay, cool.

**Stevie Kim:** These ones are just like waiting on delivery team.

**Stevie Kim:** And so this is really where we probably should spend most of our time is these are all the new a new assigned tickets that we have.

**Stevie Kim:** We've

**Stevie Kim:** Some of these were pushed from, I mean, they weren't pushed from other cycles, they were just never slated for earlier cycles, and some of them are new from triage.

**Stevie Kim:** And so, yeah, if, I mean, let's see, this one is an article.

**Stevie Kim:** This one, I'm trying to get them to, like, separate tickets instead of, because this one is both new workflow and existing workflow.

**Stevie Kim:** Yeah.

**Stevie Kim:** And that's, like, too much work for one ticket, so, I mean, feel, like, if, for anyone who takes this, feel free to split it up into two tickets, because this isn't.

**Marcus Derencius:** Yeah, can make less of the tasks.

**Stevie Kim:** Yeah.

**Stevie Kim:** Yeah, because this is, like, a big one.

**Marcus Derencius:** But it's.

**Marcus Derencius:** Yes.

**Marcus Derencius:** Yesterday, got a tag from Search.ai, so it was...

**Stevie Kim:** What's that?

**Marcus Derencius:** Because yesterday, I just want to check if there's a ticket for this Search.ai that they asked, they were asking a pipeline.

**Stevie Kim:** Oh, it's, yeah, I needed...

**Stevie Kim:** Yeah, we were waiting on information there.

**Andi Bailey:** Wait, I think that they provided it in that link.

**Stevie Kim:** Did you look at that link, the agentic pipeline documentation?

**Stevie Kim:** No, huh?

**Marcus Derencius:** Yeah, so, yeah, so big.

**Marcus Derencius:** And they were, was that work in progress?

**Andi Bailey:** Yeah, yesterday.

**Andi Bailey:** Wait, so what do they need?

**Marcus Derencius:** Because those are drop-downs, so is that not...

**Stevie Kim:** Yeah.

**Stevie Kim:** I don't know, I haven't looked at it since it was...

**Stevie Kim:** Okay, can we check?

**Andi Bailey:** It hours ago.

**Andi Bailey:** Yeah, it is a...

**Andi Bailey:** Yeah.

**Andi Bailey:** Marcus, can you see if that's what you need?

**Marcus Derencius:** Yeah, it looks like it has a lot.

**Marcus Derencius:** So I will start working on that, and then hopefully they can.

**Marcus Derencius:** Daniel made a new pipeline that should work as I start.

**Marcus Derencius:** So then I will start.

**Marcus Derencius:** Then they can start.

**Marcus Derencius:** I'll start the pipeline.

**Marcus Derencius:** Then they can start with bringing and playing to get feedback, and we start with find.

**Marcus Derencius:** So I should be able to start working on this, so I'm working on this today.

**Stevie Kim:** So is this one ticket, Marcus, or is this something that needs to be split up into multiple?

**Marcus Derencius:** Yeah, it looks like one ticket with the whole pipeline, so they have a lot of structures.

**Stevie Kim:** Okay, cool.

**Marcus Derencius:** Is that a JT one?

**Marcus Derencius:** Okay, cool.

**Stevie Kim:** Okay, cool.

**Stevie Kim:** Thank

**Andi Bailey:** Yeah, because it's 30 articles a week, so without this it'll be really hard.

**Stevie Kim:** Okay, so really this is just a request for the agentic pipeline?

**Marcus Derencius:** Yeah, and they have a lot of instructions in that documentation, so the work will be more compiling all those instructions and put in the pipeline.

**Stevie Kim:** Okay.

**Stevie Kim:** That needs to be tracked in this project, then, because we're a customer.

**Stevie Kim:** I'll figure out what milestone it is.

**Stevie Kim:** Yeah, it doesn't really matter at this point.

**Stevie Kim:** Cool, okay.

**Stevie Kim:** Okay.

**Stevie Kim:** Oh, back to the unassigned.

**Stevie Kim:** Okay.

**Marcus Derencius:** So, yeah, they have the priority, because I have, after tomorrow, or at the end of the day, tomorrow, I have a lot of availability to work on tickets, so I'll start.

**Stevie Kim:** Okay.

**Marcus Derencius:** I'll free my cues.

**Stevie Kim:** And same with, and Nico has more time after Thursday.

**Stevie Kim:** So, yeah, then why don't, we don't have to go through these separately.

**Stevie Kim:** I just wanted to make sure, you know, like, Andy, if there's any that stand out to you in this unassigned list that should be, you know, like, assigned right now, so we make sure they're going to be worked on sooner rather than later.

**Stevie Kim:** That'd be helpful.

**Andi Bailey:** What's the TLDR one?

**Stevie Kim:** Oh, Alex AI.

**Stevie Kim:** Okay.

**Stevie Kim:** Okay.

**Andi Bailey:** Yeah, mean, auto is just coming out of strategy sprints, so it would be nice to set them up for success sooner rather than later.

**Andi Bailey:** And then Tavern, like, that team's pretty strapped.

**Andi Bailey:** I just moved to Sam out of the team.

**Andi Bailey:** So I think those are the two that I would prioritize over the other ones in that backlog, just from a quick look.

**Stevie Kim:** Sorry, who was the other one?

**Andi Bailey:** Tavern at the top, second, eight, three, nine, two.

**Stevie Kim:** Okay, I'm just going to change these to highs so we're aware of the priority, even though they say in the ticket that they're medium.

**Stevie Kim:** Cool.

**Stevie Kim:** Okay, so, yeah, just take the high ones, the Tavern, and the auto ones, and then.

**Andi Bailey:** Oh, actually, I would put Webflow above both of those.

**Stevie Kim:** Sorry, I didn't see Webflow there.

**Stevie Kim:** Okay.

**Stevie Kim:** Okay.

**Stevie Kim:** And is this, do they already have a pipeline?

**Andi Bailey:** They have a couple, but this is an expansion opportunity.

**Andi Bailey:** So they're gonna pay us more money, I think, for this.

**Stevie Kim:** I'm just kind of trying to figure out like if I should just, if I should just take this one.

**Stevie Kim:** Okay, so, yeah, I can, Yeah, let's take this one.

**Marcus Derencius:** At least it's starting, so.

**Stevie Kim:** What's that?

**Marcus Derencius:** I don't just saying, if you can just start it, it's good stuff.

**Marcus Derencius:** They have other, they have a lot of pipelines, so maybe it would be easier to clock.

**Stevie Kim:** Yeah, I mean, I'm assuming it's just they're moving over their, rather.

**Stevie Kim:** I

**Stevie Kim:** The regular article generation one, but I'll ping the ME on it or the CM to make sure if it's not in this ticket.

**Stevie Kim:** There's a lot of information in this ticket.

**Stevie Kim:** So, okay.

**Stevie Kim:** Yeah, I can tackle that this week.

**Stevie Kim:** And then, yeah.

**Stevie Kim:** And then, as I said, I'll tackle the post-processing step for Strappy to try to get, like, that code generation thing fixed.

**Stevie Kim:** Anything else, Andi?

**Stevie Kim:** This is no assignee, but I can change the filter.

**Stevie Kim:** This one has been in the queue for a long time, but we're still...

**Andi Bailey:** Oh, yeah.

**Andi Bailey:** That's...

**Andi Bailey:** What are we...

**Stevie Kim:** Oh, are we still blocked?

**Stevie Kim:** Yeah.

**Stevie Kim:** We haven't gotten any new information on it.

**Stevie Kim:** So it's not, this isn't enough information to create this pipeline.

**Andi Bailey:** Okay.

**Andi Bailey:** Okay.

**Andi Bailey:** I just messaged him in the channel.

**Andi Bailey:** And I think that the Webflow ticket is a new ticket or a new pipeline rather than a replacement for a current one.

**Stevie Kim:** Right.

**Stevie Kim:** Yeah, it's, Kirkland had requested to get more information to move forward and that hasn't happened.

**Stevie Kim:** So Yeah.

**Andi Bailey:** Yeah.

**Andi Bailey:** Okay.

**Andi Bailey:** Yeah, no, that's, yeah, the Deep Grim one I just tagged, Eric.

**Andi Bailey:** I'm just, I was just going back to the Webflow one.

**Andi Bailey:** I think we need, I think that that's a new ticket versus like a replacement for an existing because we're expanding our offerings for them.

**Stevie Kim:** Yeah, yeah.

**Stevie Kim:** And that's what it says.

**Stevie Kim:** This is a new Webflow needed.

**Marcus Derencius:** But.

**Andi Bailey:** Yeah, yeah, that's fine.

**Andi Bailey:** That's fine.

**Andi Bailey:** But it sounds like in the comments, Kirkland just needed more context.

**Andi Bailey:** Yeah, yeah, no, I was talking about a different ticket.

**Andi Bailey:** Oh.

**Andi Bailey:** I was switching context too quickly, sorry.

**Andi Bailey:** Which ticket were you talking The Webflow one that we were talking about before that you're going to take it on.

**Stevie Kim:** Oh, oh, the agentic one?

**Andi Bailey:** Mm-hmm.

**Stevie Kim:** And what were you saying about it?

**Andi Bailey:** Oh, it's it.

**Andi Bailey:** I think it's not a replacement.

**Stevie Kim:** I think it's new.

**Stevie Kim:** okay.

**Stevie Kim:** Okay.

**Stevie Kim:** Okay.

**Stevie Kim:** That will take more time.

**Stevie Kim:** And so I'm going to leave it unassigned for now and look at what we have left to do on the agentic ones that are rolling over because I'm trying to just bash them as fast as possible.

**Andi Bailey:** So then it is above Otto and Tavern, the other two that you just set as high, like for the backlog, it would be above both of those.

**Stevie Kim:** Okay.

**Stevie Kim:** Then maybe someone else should take this so I can just focus on, I don't know where my view is.

**Stevie Kim:** Sorry.

**Stevie Kim:** Sorry.

**Stevie Kim:** I'm like, where is it?

**Stevie Kim:** Yeah.

**Stevie Kim:** I mean, I've been, as you can see, just really hammering out these, you know, ones that are pretty much just rolling, rolling them over and not anything new.

**Stevie Kim:** And so just to do a...

**Stevie Kim:** Anity check with you, are there any ones that, let's see, we already covered Surge and Otto, are there any ones in the backlog that I should, like, that are important that we need, that makes us need to split our time here between, like, maybe the, you know, Marcus or Kirkland or Nico taking the, the, the Webflow, Otto, you know, the, the Surge.ai data annotation, I don't know if that's different than the other Surge ticket, but, yeah, it is, okay, so then can we, yeah, okay, then I would say Airbyte is, like, we've got, like, a bunch of stuff going on with them, so I would add them, and, diligent is a nice to have.

**Andi Bailey:** For now, what's up?

**Andi Bailey:** What's the abnormal ticket?

**Stevie Kim:** Is that just for an agentic pipeline?

**Stevie Kim:** Yeah.

**Andi Bailey:** Okay.

**Andi Bailey:** Those are all just agentic.

**Andi Bailey:** Okay, yeah.

**Andi Bailey:** If we have extra capacity, would actually like us to go back to like any publishing tickets that we have, or like automated publishing.

**Andi Bailey:** I know we like keep dropping, like those keep dropping, but I just saw that Suleiman, our publisher, worked over the weekend and had to publish more than 30 articles.

**Andi Bailey:** And so if we can like go back to auto-automating publishing for any web flow.

**Stevie Kim:** The only one we have is for Strapi right now.

**Andi Bailey:** Okay.

**Stevie Kim:** We actually don't have any in our queue.

**Andi Bailey:** Can we pull that up?

**Andi Bailey:** And then I think the other reason, the reason that we don't have other ones in the queue is because of the...

**Andi Bailey:** A table issue with publishing and webflow.

**Marcus Derencius:** It's fixed.

**Andi Bailey:** The table issue is fixed.

**Andi Bailey:** That table issue is fixed?

**Andi Bailey:** Okay, so then maybe we can look at some of those closed tickets and try.

**Andi Bailey:** I'll ask the team to try and reopen some of those so that we can automate publishing and webflow for those clients.

**Stevie Kim:** Yeah, because I think like Suleiman's going to break soon.

**Stevie Kim:** Okay, that makes sense.

**Stevie Kim:** So in that case, let me just keep the webflow one.

**Stevie Kim:** Okay.

**Stevie Kim:** The GenTech one, because if, yeah, if we need to focus on some of the publishing ones, Yeah.

**Stevie Kim:** Since I haven't ever, you know, done those, then it's best to just leave that to the core team here.

**Andi Bailey:** Okay, cool.

**Marcus Derencius:** Yeah, and just about the publishing, I just need them to report or reopen the tickets or tag me, because now that the table issue is fixed, so I think...

**Marcus Derencius:** It's kind of working, so they just need to report me, and it's kind of easy and quick to fix, so yeah, we just have to find it.

**Andi Bailey:** perfect.

**Stevie Kim:** Perfect.

**Stevie Kim:** Okay, so it sounds like the priority are those agentic pipelines that we talked about, and then the publishing tickets, is that right?

**Andi Bailey:** Yeah, yeah.

**Stevie Kim:** That sounds good.

**Stevie Kim:** Anything else?

**Marcus Derencius:** Just a quick update.

**Marcus Derencius:** I heard that from the tech group generate articles from a spreadsheet with Mariana, so I built a first.

**Marcus Derencius:** Bye

**Marcus Derencius:** I plan generating the articles, so I need to follow up with any feedback, and then prepare for the next articles for spreadsheets.

**Stevie Kim:** And that's the tag one, right?

**Stevie Kim:** Yeah.

**Stevie Kim:** Cool.

**Stevie Kim:** Okay, awesome.

**Stevie Kim:** Yeah, so that's actually in progress.

**Stevie Kim:** Cool.

**Marcus Derencius:** Yeah, I just moved to in progress, so.

**Stevie Kim:** Awesome.

**Stevie Kim:** Yeah, I mean, that's it for me.

**Stevie Kim:** Anything else, Andi?

**Andi Bailey:** No, thanks, guys.

**Stevie Kim:** All right, thanks, y'all.

**Stevie Kim:** Have a good one.

**Stevie Kim:** Thank you.

**Marcus Derencius:** Bye.
