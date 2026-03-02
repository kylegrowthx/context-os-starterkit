# Lane Sync: Client Ops Kick-Off

<metadata>
date: 2025-11-18
time: 17:58 UTC
duration: 30 minutes
organizer: daniel@growthxlabs.com
participants: Marcus Derencius, Kirkland Gee, Andi Bailey, Nicolas Castellanos, Stevie Kim, Daniel Lopes
fathom_recording_id: 102519021
fathom_url: https://fathom.video/calls/477466946
share_url: https://fathom.video/share/zjPXAFVsLZ6yLx9bjNyCGDs-s6MYRdzu
source: fathom
enriched_on: 2026-03-02 02:15 UTC
</metadata>

---

## Summary

GrowthX's client operations team met to wrap up the agentic pipeline rollover project and establish new workflows for onboarding clients. The agentic rollover is nearly complete with only one task remaining; Interwell and Town tickets were moved out to allow project closure. The team agreed to streamline new client onboarding by duplicating existing agentic pipelines and having Kirkland perform quick quality checks on artifacts. Separately, Nicolas shared progress on Loadable's highly automated pipeline that generates product specs and templates, plus a proposed GitHub Actions integration for publishing without a CMS.

---

## Context

This is an internal GrowthX client operations and delivery team sync. Stevie Kim leads the meeting as the operations lead, coordinating with Daniel Lopes (engineering/frameworks), Kirkland Gee (delivery/pipeline quality), Andi Bailey (strategy sprints and client relationships), Marcus Derencius (technical implementation), and Nicolas Castellanos (specialized pipeline development). The meeting follows the team's shift toward pod-based delivery structures and marks the transition from the multi-week agentic pipeline rollover project to sustainable workflows for future client onboarding. Success criteria include closing out the rollover project cleanly and establishing repeatable, quality-controlled processes for new client pipeline setup.

---

## Relevance

**To GrowthX Delivery:**
- New client pipeline workflow now uses templated duplicates + Kirkland's artifact sanity checks, reducing setup friction from days to ~30 minutes per client
- Agentic rollover project closing clears capacity for strategy sprint support (Airbyte in sprint now; two new pipelines/week anticipated)
- Framework migration strategy starting with simple Webflow publishing workflows (no router needed) before tackling complex agentic pipelines
- Analytics rollout and Pages feature setup identified as high-value, low-effort bandwidth opportunities

**To GrowthX Business Development:**
- Pod structure increases bandwidth for continuous pipeline review and optimization — key differentiator vs. static templates
- Loadable GitHub Actions proposal demonstrates automation/CMS-free publishing capability; applicable to other GitHub-native clients like Vap
- Small backlog (only 5 unassigned tickets) positions team well for Q1 account expansion and new client intake
- Template-driven approach reduces delivery risk and improves reproducibility for reference-ability

---

## Overview

- **Agentic Rollover Nearing Completion:** The project is nearly finished, with only 1 "To Do" ticket remaining. The "Town" ticket is being removed, and "Interwell" is backlogged, clearing the path to close the project.
- **New Client Pipeline Workflow:** To accelerate onboarding, new clients will receive a duplicated agentic pipeline. Kirkland will perform a quick sanity check on the artifacts to ensure quality before delivery.
- **Internal Project Prioritization:** Client work is the top priority. Internal projects (e.g., website dev, new framework migration) will only be tackled with surplus bandwidth after all client commitments are met.
- **Loadable Pipeline Innovation:** Nico's pipeline generates product specs from articles, enabling automated creation of hundreds of templates. A proposed GitHub Actions integration would also provide a scalable publishing model for clients without a CMS.

---

## Key Topics

### Agentic Rollover Status

  - The project is nearing completion, with the following status:
      - In Progress: 4
      - In Review: 3
      - To Do: 1
      - Backlog: 4
  - **Blocked Tickets:**
      - **Town:** Being removed from the project.
      - **Interwell:** Moved to the general backlog.
          - **Rationale:** The client is paused pending a site mapping fix. The ticket, created Oct 16, is still relevant to their strategy and will be revisited later.

### New Client Pipeline Workflow

  - **Problem:** New clients need agentic pipelines quickly but often lack a clear content strategy.
  - **Solution:** Duplicate an existing pipeline as a starting point.
      - **Why:** This provides a functional setup for clients to experiment with artifacts and refine their strategy.
  - **Quality Control:** Kirkland will perform a quick sanity check on the duplicated artifacts.
      - **Why:** To ensure the writing guidelines and prompts are sound, as they significantly impact pipeline output.
  - **Future State:** Daniel's project with Brad will automate workspace setup and pipeline creation, eliminating the need for manual tickets.

### Backlog & Internal Project Prioritization

  - The current backlog is small, creating an opportunity for strategic internal work.
  - **Unassigned Tickets:**
      - **Airbyte:** High priority, as the client is in a strategy sprint.
      - **Sunbit:** Low priority, flexible timing.
      - **Discern:** Programmatic client needing a pipeline refresh.
  - **Internal Projects (Lower Priority):**
      - **GrowthX Website (Next.js/Sanity):** Defer until client work is complete.
      - **Analytics Rollout:** Use surplus bandwidth to help clients adopt the new tool.
      - **New Framework Migration:**
          - **Why:** To replace the old codebase and learn the new framework.
          - **Strategy:** Start by migrating simple publishing workflows (e.g., Webflow) that don't require the new router.
      - **Newsletter Pipeline Template:** Kirkland will connect with Nathan to review the DataGrid newsletter as a potential model.

### Loadable Pipeline Innovation

  - Nico is developing a highly automated pipeline for Loadable.
  - **Process:**
    1.  **Generate Specs:** The agentic pipeline generates hundreds of product specs from articles.
    2.  **Create Templates:** Specs are fed into another pipeline to create templates.
    3.  **Human Polish:** A contractor performs final polishing (\~1–1.5 hrs/template).
  - **Proposed GitHub Integration:**
      - **Why:** To provide a scalable publishing solution for clients without a CMS.
      - **How:** An integration creates a PR → GitHub Actions auto-merges after CI passes.

---

## Action Items

- **Stevie Kim (GrowthX):**
    - Move "Interwell" ticket to the general backlog.
    - Remove "Town" ticket from the agentic rollover project.
- **Andi Bailey (GrowthX):**
    - Connect Kirkland with Nathan to review the DataGrid newsletter.
- **Kirkland Gee (GrowthX):**
    - Perform sanity checks on new client pipeline artifacts as they're set up.
- **Daniel Lopes (GrowthX):**
    - Test the new framework this week.
    - Request simple publishing workflows from Marcus to begin migration.
- **Nicolas Castellanos (GrowthX):**
    - Continue work on the Loadable pipeline and GitHub integration proposal.

---

## Transcript
**Stevie Kim:** Hey, Marcus.

**Marcus Derencius:** Hey, hey.

**Marcus Derencius:** HTV, how are you?

**Stevie Kim:** I'm doing well, except I'm cold, and I don't like being cold.

**Marcus Derencius:** Cold, like sick or cold in the weather?

**Stevie Kim:** Weather, weather.

**Stevie Kim:** I'm wearing a flannel and a long sleeve shirt, and I'm still cold.

**Stevie Kim:** I need to just remember that it's hoodie season and not deviate from that.

**Kirkland Gee:** What you need to get is just a fireplace in your office.

**Kirkland Gee:** Oh, my camera went off.

**Kirkland Gee:** But I literally had, like, my office is in our basement, and we don't.

**Kirkland Gee:** We have heat in our basement at all.

**Kirkland Gee:** It's just like baseboard heat, know, you like radiators.

**Kirkland Gee:** And so a few months after I moved in, I put these gas logs in.

**Stevie Kim:** Oh, I'm so doing that.

**Kirkland Gee:** Shut the door over there and it gets so toasty so fast.

**Stevie Kim:** It's nice.

**Stevie Kim:** Oh, that sounds so warm and cozy.

**Kirkland Gee:** I love that idea.

**Kirkland Gee:** It's honestly, like, I'm not going to say essential, but I will say worth every single penny with how much time I have to spend down here.

**Stevie Kim:** Yeah, that's fair.

**Stevie Kim:** I sometimes, like, move around.

**Stevie Kim:** I'll be in my kitchen for a little bit or back in the office, but I've noticed when it gets colder, I do prefer my office just because I have my comfortable chair and everything, you know.

**Stevie Kim:** But, yeah, it's, yeah, I'm not a fan of being cold.

**Stevie Kim:** I'm a wimp.

**Stevie Kim:** All right, well, we can.

**Stevie Kim:** Just get started.

**Stevie Kim:** We actually have, or at least, I don't know, maybe I'm the only one that's going to be excited about this.

**Stevie Kim:** But I think we are in a really good place to finish up the rollover, the agentic rollover.

**Stevie Kim:** So I started like three yesterday, I think, and testing those.

**Stevie Kim:** And then, yeah, so we've got four in progress, three in review, one is in to do, and then four in backlog.

**Stevie Kim:** I did want to get a quick check on these two that are blocked because of where, you know, there's some issues with the account, they're on pause, stuff like that, interwell in town.

**Stevie Kim:** And so I'm not sure if we should just take these, you know, off, they're like, they're...

**Stevie Kim:** Thank you.

**Stevie Kim:** You know, I don't know, the Interwell one.

**Stevie Kim:** sorry.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** I'm always in favor of, like, if it's been six weeks and no one's said anything, they probably don't need it.

**Kirkland Gee:** And if they do, they can ask for it again and we can do it.

**Stevie Kim:** But I don't see the point in holding on to something that's been sitting for that long. Those are my thoughts too.

**Daniel Lopes:** I'm going to double check with Andi, but my hunch is that they are both paused.

**Andi Bailey:** I'm for sure.

**Andi Bailey:** They're giving the whole product.

**Andi Bailey:** Yeah.

**Andi Bailey:** Tom is...

**Andi Bailey:** Sorry.

**Andi Bailey:** Town is paused.

**Andi Bailey:** And then Interwell, I would backlog that.

**Stevie Kim:** Well, the thing is, is we don't want to...

**Andi Bailey:** It isn't backlogged.

**Andi Bailey:** October 16th was when that went in.

**Stevie Kim:** So this has been sitting for the past six weeks. I can take these two out of this project and just put them in our normal backlog.

**Stevie Kim:** I just wanted to make sure that they will eventually need these, you know, Interwell will, because what happened with Interwell was we gave them, we did like a site audit and gave them a bunch of things that they needed to change on their site.

**Andi Bailey:** And then their dev team, like, messed up the, like, site mapping.

**Andi Bailey:** And so, before we do any more publishing, they want to fix that.

**Andi Bailey:** And so, I think this, like, since it came on October 16th, that's within the timeframe that we did, like, the revamp of strategy.

**Andi Bailey:** So, I do think that this will still be relevant.

**Andi Bailey:** I can check in with Matt on this one, though.

**Andi Bailey:** But town, yeah, I don't think town matters.

**Stevie Kim:** Okay, cool.

**Stevie Kim:** So, I'll just move Interwell's to our normal backlog, since we have no idea.

**Stevie Kim:** I mean, and we can always just.

**Stevie Kim:** Do it, too.

**Kirkland Gee:** Yeah, it's less about, like, whether we're going to do it or not, and more like, can we call this project closed out, and then if there's one or two that have a request in a week or two, not a big deal at all.

**Kirkland Gee:** But just to be like, okay, everything that is doable and needs doing right now is done, that would feel really, it's just like a psychological thing, it would feel nice.

**Stevie Kim:** hundred percent, absolutely.

**Kirkland Gee:** So that makes sense, Aidy.

**Stevie Kim:** Cool.

**Stevie Kim:** Okay, so, yeah.

**Stevie Kim:** That's exciting.

**Stevie Kim:** We'll be able to close that out.

**Stevie Kim:** There weren't a lot that I needed clarification on.

**Stevie Kim:** There weren't actually any.

**Stevie Kim:** We, I actually also went, this is for this current cycle, I also went through our backlog, and it's, there's surprisingly not that much.

**Stevie Kim:** So I'm pretty excited.

**Stevie Kim:** This This is a really good time to, um.

**Stevie Kim:** As we're breaking off into these pods, I feel like we're in a really good place to do that organizationally.

**Stevie Kim:** So, yeah, I'm pretty excited about how much work we've done, especially in the last few cycles.

**Stevie Kim:** There are a few that don't have anyone assigned to them.

**Stevie Kim:** Discern was originally a ticket for the agentic workloads, but they mostly do programmatic work. They did want a refresher pipeline though. There are a couple others I haven't seen that maybe came up when I was out last week. If anyone wants to put their name on these, that would be great. This is Airbyte, which is new programmatic. None of these are urgent, I think.

**Andi Bailey:** There's like a mix of medium and low.

**Andi Bailey:** Airbyte is in strategy sprint right now.

**Andi Bailey:** So I think Airbyte would be one that I would prioritize.

**Andi Bailey:** And that brings me to my other question, which like we can close out the agentic project, but every week we're going to start a new a pipeline for two clients who are going through strategy sprint.

**Andi Bailey:** So how do we want to keep track of like, like we should just anticipate that we're generating two agentic pipelines a week kind of.

**Stevie Kim:** No, so, so that project was specifically for rolling over current customers.

**Stevie Kim:** Yeah.

**Stevie Kim:** So the new ones, just you create a ticket like you normally would for CPD.

**Andi Bailey:** Okay.

**Andi Bailey:** And then can we prioritize those?

**Andi Bailey:** I mean, I'm just thinking, like, we know which clients are going to start every, like, we're, clients kick off week one, week three, we need a pipeline.


**Andi Bailey:** So just flagging that if there's, if anybody ends up with, like, extra time, that's always one.

**Andi Bailey:** Like, it's sort of an evergreen ticket, and I don't know if we want to handle those differently, essentially.

**Stevie Kim:** No, I mean, it's the, basically, it's just the same as how it would have been if they needed a regular workflow.

**Stevie Kim:** So treating that the same, it's, it just happens to be our new code base that we're using.

**Andi Bailey:** Okay.

**Kirkland Gee:** Just to, I'm just gonna throw this out there as a question.

**Kirkland Gee:** So when new customers come on board and need an agentic pipeline, they don't have a super clear idea of what the end content needs to look like. They're still understanding tone and voice. So my question is, is there a reason we can't just start with duplicating something that already exists, generate all the artifacts, let them play with it, and tweak it from there?

**Andi Bailey:** Yeah, well, that was kind of what I was thinking was like, is there something that we could do to like get them started so that we're not starting from behind on that?

**Kirkland Gee:** Who sets up Atlas workspaces for new customers?

**Kirkland Gee:** Is that a strategy sprint folks thing right now?

**Andi Bailey:** yeah.

**Andi Bailey:** I think like the CM does it today.

**Andi Bailey:** And we have just been like duplicating existing agentic pipelines.

**Andi Bailey:** I just don't know if like, I think in the long term, Client Ops wants to take that back.

**Andi Bailey:** Um, just because otherwise we'll have like a bunch of different versions out there that nobody that we don't have track of.

**Kirkland Gee:** Yep.

**Kirkland Gee:** So that's kind of what I'm, is like, I don't even know that we need to think about this necessarily from like a ticket that needs to be scoped perspective, if that's all it is.

**Kirkland Gee:** It takes five or ten minutes to copy something over, make sure it's roughly okay, and put it in their hands to play with the artifacts.

**Kirkland Gee:** So we talked about us getting more involved with strategy sprints in general.

**Kirkland Gee:** So I don't know, I just think it's worth it.

**Daniel Lopes:** I think it might be a good idea to just have at least like a review process, even if it's just a copy and paste, because like you all have a better understanding of what is insanity in the writing guideline versus not, you know?

**Daniel Lopes:** So, or like what will like affect the prompt a ton.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** But you can at least take like a sanity check on the, on the artifact, because the artifacts impact the pipeline a lot more than just a copy of the pipeline.

**Daniel Lopes:** With the feature I'm working on with Brad, workspace setup will be automatic and the workspace will come with the pipelines, so they won't have to file tickets anymore. In the interim, between now and when that's live, we'll still need that review process.

**Stevie Kim:** Yeah, we'll still want to track these, just because we'll want to make sure, it's just easier, you know, that they know that this is done, we've tested it, just like we're doing with the agentic rollovers, it's just the same thing, so.

**Kirkland Gee:** I'm happy to just be the person that reviews them when they're set up. It doesn't take very long — maybe 30 minutes a week to look them over and make sure everything's okay.

**Stevie Kim:** That would be helpful. Whenever they're setting them up, I can make sure we track it.

**Daniel Lopes:** I'm happy to be the one doing it too. Just make sure I don't forget.

**Andi Bailey:** Yeah, that would be helpful.

**Andi Bailey:** Thank you.

**Stevie Kim:** So as mentioned, just making sure that we don't ignore the ones that haven't been assigned.

**Stevie Kim:** There's the Sunbit one.

**Stevie Kim:** It says it's low and flexible timing.

**Stevie Kim:** again, whatever we have already, you know, in like assigned to us, especially if it's a higher priority or an ICP, those take precedence.

**Stevie Kim:** But I was just going to say, as you, you know, have time picking these up, but the air bite one sounds like it does need to be done.

**Daniel Lopes:** soon.

**Daniel Lopes:** Let's discuss this one.

**Daniel Lopes:** All right.

**Daniel Lopes:** For this cycle, we have 5-1 that are not assigned, and everything else is in review or in progress.

**Stevie Kim:** Is that right?

**Stevie Kim:** These are stuff I just prioritized for this cycle or that others added while I was out. All the to-do items, both assigned and unassigned, are here. There really aren't that many. Looking yesterday, I was pretty surprised — we've done a really good job getting rid of a lot of the backlog items. I didn't need much clarification on anything.

**Daniel Lopes:** Not to add to the scope, but Ren is asking if any of our back-end folks could be available for working on our website, and I'm trying to decide if it's a good idea.

**Daniel Lopes:** It's a Next.js site integrated with Sanity. Ren has two agencies that can do that work, but I think if we have bandwidth, learning our own codebase would be good. If anyone wants to get better at Next.js, this could be a good opportunity. Ren wants to finish by end of year, but we can reduce scope if needed. It's not a client, so we can simplify things. I was thinking I'd tell him no and keep people on clients, but if we have room, either Nico, Marcus, or Kirkland could take it on. But it's up to you, Stevie.

**Stevie Kim:** I don't want to lose momentum. We're in a good spot now, and I really want to finish the agentic work.

**Stevie Kim:** Um, I, so my opinion is that let's focus on what we have in this sprint.

**Stevie Kim:** Um, if we bang the, all this stuff out in a week, then that Halloween week, someone can go over, but I'd really rather us like, get this out.

**Daniel Lopes:** So yeah, makes sense.

**Daniel Lopes:** I don't think I forgot to say is, uh, we also.

**Daniel Lopes:** We analytics ready to roll out, and I think the guys are kind of struggling to, like, set that up with everyone else, and we have pages that really rolled out yesterday.

**Daniel Lopes:** So any bandwidth that we get here, it could be a good idea to create to-dos for us to just, like, try to set that up for the clients and see what happens, too, you know?

**Daniel Lopes:** Because that will replace the looker and all the other stuff that the content team is, like, trying to set up.

**Daniel Lopes:** Also, the sitemap work from the Interwell situation is part of the Pages feature.

**Daniel Lopes:** It does page speed analysis on every client regularly. That's another opportunity. So I'll tell Ren to have George Main work on the UI first — just do the static UI, and then in a couple of weeks we can engage whoever has availability.

**Stevie Kim:** We'll definitely have availability next cycle, unless something crazy happens.

**Daniel Lopes:** We have Brex and Zapier coming in the pipeline.


**Kirkland Gee:** And Zapier is going to be a thing, for sure.

**Stevie Kim:** Yeah.

**Stevie Kim:** Yeah, that's true, too.

**Kirkland Gee:** I helped Tyler scope a lot of that, so I have a lot of context. It's going to take some effort to do what they want to do.

**Stevie Kim:** I did want to ask about the pods — how that's going to affect client ops. Daniel, you talked to me a little about it in our last one-on-one and then the announcement today, but I think getting some clarification around that would be good.

**Andi Bailey:** I would say for the short term, it shouldn't impact you very much, like, the system for picking up tickets and everything will still be the same.

**Andi Bailey:** The goal is to get more help for the pods, especially, I think, one thing that we don't essentially have time to do right now with our bandwidth is the, like, continuous review and revision as the agentic pipelines are changing.

**Andi Bailey:** And so putting sort of a forward-deployed client ops embedded more deeply in pods will give us that ability to start to, like, shape pipelines.

**Andi Bailey:** I mean, like, Kirkland, if we get more people operating pipelines like Panzer is, and if we think about that.

**Andi Bailey:** Like, that's just so much work that they're, and if we start to add work streams to clients, which is the goal to expand, those would be the ways that that additional headcount would be really beneficial.

**Andi Bailey:** But in the immediate term, you guys shouldn't see changes to the way that you're working.

**Stevie Kim:** Got it.

**Kirkland Gee:** I feel like we need more of us before we can really change much of what we're doing is the biggest problem.

**Andi Bailey:** Exactly, yeah.

**Daniel Lopes:** Good news — Sergei verbally accepted yesterday. He's joining December 1st, pending final paperwork.

**Daniel Lopes:** The framework guys have things in a pretty good state. I'm going to test it this week. We can migrate workflows to the new framework and remove the old codebase slowly using a splitting router — incoming requests get routed to both the new and old workflows so we can test and learn.

**Stevie Kim:** Is that ready to go?

**Daniel Lopes:** The framework works, but the router isn't finished yet. It should be done this week, then we can deploy live.

**Stevie Kim:** Awesome.

**Marcus Derencius:** We can start migrating the publishing workflows first since we can easily check if they work. They don't perform LLM calls, so we don't need the router — if they work, we can just flip the switch. We have about 20 Webflow publishing workflows doing the same thing, so we could migrate those quickly without the router.

**Daniel Lopes:** Yeah, that's a good idea.

**Daniel Lopes:** Like I was asking them to migrate the harder ones first, like the agentic ones, just to see if the framework actually works.

**Daniel Lopes:** But then deploy, I can deploy these ones.

**Marcus Derencius:** Yeah.

**Marcus Derencius:** Yeah.

**Marcus Derencius:** So, because I'm creating new workflows that just do simple things that could easily be in the new system already.

**Marcus Derencius:** And we are just, yeah, we don't have to reveal much of the content, if it works or not.

**Daniel Lopes:** Can you send me like some of the publishing ones for me to take a look?

**Daniel Lopes:** Because that's going to be part of the feature that I'm working with Brad as well.

**Daniel Lopes:** Ideally, we'll have a bunch of content types when you set up the workspace — content types will be prepackaged pipelines. We'll have a feature where you connect a workflow for publishing in that content type, associated to the CMS. I want to see how you guys are doing the publishing now.

**Kirkland Gee:** It's a mess, but it works. Some OAuth integration for Webflow to map fields would be really helpful — we're doing all that in code right now.

**Daniel Lopes:** For now, if we normalize input and output, the Atlas side can just build and test.

**Marcus Derencius:** About 10% works as is, 10% we have custom implementations for clients.

**Daniel Lopes:** All right.

**Daniel Lopes:** Anything else?

**Kirkland Gee:** Quick question, Andi — a couple of things have been sitting for a while. There's this newsletter pipeline ticket from about three months ago.

**Andi Bailey:** For DataGrid?

**Kirkland Gee:** Yeah, DataGrid, Augment, and Monograph originally.

**Kirkland Gee:** And it's just been, like, sitting in, like, hey, can we have a meeting to talk about it?

**Kirkland Gee:** Or, like, can we figure out what we want to do?

**Andi Bailey:** And I just haven't, like, heard anything.

**Andi Bailey:** Yeah.

**Andi Bailey:** Nathan came up with a draft newsletter for DataGrid.

**Andi Bailey:** I don't know what pipeline he used, so maybe I'll connect you guys.

**Andi Bailey:** Augment is on pause on our newsletter.

**Andi Bailey:** And I think mom...

**Andi Bailey:** Monograph is, we decided not to do it.

**Andi Bailey:** I think this was more about building out a template for what a newsletter workstream would look like.

**Andi Bailey:** So it's like a P2, but maybe we can talk about what data grids looks like, because I think that's the model that we want to go with going forward.

**Andi Bailey:** It's essentially like a product marketing newsletter on new feature launches, which would be kind of nice to be able to, like, templatize.

**Kirkland Gee:** I've looked through it and thought about it, but it's fairly vague right now about what we want it to be. I didn't want to build something that's not useful. I'd like to connect with Nathan and maybe set up a channel to figure out what we need. DataGrid could be a good template model for us going forward.

**Kirkland Gee:** And then I think the Deepgram one, I've pinged Eric a bunch on this one, but I think we're still just waiting on them.

**Andi Bailey:** Yes.

**Andi Bailey:** Yes.

**Kirkland Gee:** Okay, I think those are the main things. There are a few other tickets just sitting, but I think that makes sense.

**Daniel Lopes:** Cool.

**Daniel Lopes:** What's the state of loadable, Nico?

**Nicolas:** Give me a second — I was looking at something else. We just published a new set of guides and templates, and we have the pipeline for generating templates from product specs. We're planning to have a contractor do final polishing — about 1 to 1.5 hours per template. Content generation for the template page on Loadable's site is done. Right now I'm trying to speed up the contractor's polishing process.

**Nicolas:** What I'm trying to do is use the agentic pipeline for generating articles, but for generating full product specs for each of the categories we want to tackle.

**Nicolas:** That way we can spin up a ton of different templates per category, and we don't need a human basically going and deciding what's a good product spec.

**Daniel Lopes:** That's a great idea.

**Daniel Lopes:** Who is in charge of figuring out the contract?

**Nicolas:** Is George owning the contractor part?

**Andi Bailey:** Yeah.

**Daniel Lopes:** Okay, because he had people doing the Loadable bulk work.

**Nicolas:** We just sent a proposal for a GitHub integration so we can handle publishing. I'll be working on that if they accept it.

**Daniel Lopes:** How are you going to do it?

**Nicolas:** GitHub Actions plus an integration. The integration will create a PR, and the action will auto-merge it after CI passes.

**Daniel Lopes:** That's interesting.

**Daniel Lopes:** Is that...

**Daniel Lopes:** Yeah, okay.

**Daniel Lopes:** Makes sense.

**Daniel Lopes:** Because we have a lot of clients with, like, no CMS.

**Daniel Lopes:** And, like, this could be, like, a playbook for GitHub publishing.

**Daniel Lopes:** Vap was like that.

**Nicolas:** Uh-huh.

**Daniel Lopes:** Cool.

**Daniel Lopes:** Done.

**Daniel Lopes:** Thanks, everybody.

**Andi Bailey:** Thanks. Bye.
