# Nathalie 1:1 - Feedback and next steps

<metadata>
date: 2025-12-03
time: 23:02 UTC
duration: 59 minutes
organizer: Nathalie Schrans
participants: Nathalie Schrans, Matthew Panzarino
fathom_recording_id: 106145844
fathom_url: https://fathom.video/calls/494214263
share_url: https://fathom.video/share/vLizEXDjz5j7RMiKcihDA4gwcsj422h8
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Matthew Panzarino (Nathalie's new manager) set expectations for Nathalie's shift to the Strategy Sprints team, centering the team's KPI on efficiency: reducing post-Atlas editing time from 1.5–2 hours per article to enable Marketing Engineers to manage 3–5+ clients. The core issue is misuse of Atlas—MEs are bypassing the tool and manually editing content in Claude and Google Docs, creating unsustainable overhead. Matthew outlined a new pipeline-optimization workflow: manually edit an article, have Claude reverse-engineer the edits into reusable instructions, then embed those instructions back into the Atlas pipeline. Nathalie will join the Strategy Sprints team, take ownership of this workflow, and help build custom pipelines for their clients.

---

## Context

Nathalie Schrans is a Marketing Engineer at GrowthX who was working across multiple teams (Augment Code and Surge) but is transitioning back to the Strategy Sprints team. Matthew Panzarino, her new manager, conducted this 1:1 to provide feedback and set clear expectations for her new role. The meeting happens at a critical juncture for GrowthX's content delivery operations—the company is experiencing unsustainable editing overhead in its content pipeline (1.5–2 hours of manual post-processing per article) that prevents Marketing Engineers from scaling to manage multiple clients. Matthew is driving a fundamental shift in how the team uses Atlas and structures pipeline optimization, moving away from ad-hoc manual workarounds toward a systematic, reusable approach using Claude projects to reverse-engineer and standardize post-processing instructions.

---

## Relevance

**To GrowthX Delivery:**
- New KPI for Marketing Engineers is post-Atlas editing efficiency (currently 1.5–2 hrs/article, target is much lower)
- New pipeline-optimization workflow using Claude projects to reverse-engineer and standardize post-processing instructions
- Standardization across clients via tiered approach: Self-Service (platform-only), Core ICP (high-performing pipelines like Monograph), Custom (high-touch engineering for Surge, Biologica)
- Monograph case study demonstrates 92–94% time savings (5–8 min vs. 1.5–2 hrs) and contributed to 400% traffic increase

**To GrowthX Business Development:**
- Efficiency improvements enable MEs to scale from 1–2 clients to 3–5+ clients, supporting business growth and account expansion
- Client tiering will determine which engagements get custom engineering support
- New Client Ops Engineer role will formalize the partnership between delivery and pipeline optimization, improving client satisfaction and retention

---

## Overview

- **Primary KPI is Efficiency:** Reduce post-Atlas editing time (currently 1.5–2 hrs/article) to enable MEs to manage 3–5+ clients.
- **Problem: Misused Atlas:** Overly detailed prompts and manual workarounds create conflicts, leading to poor output and high editing overhead.
- **Solution: A New Workflow:** Use a Claude project to iteratively refine pipelines. The process: manually edit an article → ask Claude to reverse-engineer the edits into a post-processing instruction set → embed this set in the pipeline.
- **New Role: Client Ops Engineer:** These engineers will partner with MEs to build custom pipelines, freeing MEs to focus on client strategy and content quality.

---

## Key Topics

### The Problem: Inefficient Content Production

  - **High Editing Overhead:** Post-Atlas editing takes 1.5–2 hours per article, making the current process unsustainable.
  - **Root Cause: Misused Atlas:**
      - **Overly Detailed Prompts:** Specific instructions (e.g., "H2 must have 6 points in 150 words") create conflicts with artifacts and guidelines, resulting in poor drafts.
      - **Manual Workarounds:** MEs bypass Atlas for manual editing in Claude or Google Docs, which is inefficient and prevents platform improvement.
  - **Consequence:** This inefficiency prevents MEs from scaling to manage 3–5+ clients, which is a key company goal.

### The Solution: A New Workflow for Pipeline Optimization

  - **Goal:** Build "leverage" by making 60 hours of work achievable in 40 hours.
  - **Recommended Workflow:**
    1.  **Create a Claude Project:** Dedicate a project per client/task (e.g., "Interwell Pipeline Builder") to leverage Claude's project-specific memory.
    2.  **Seed the Project:** Provide context like the GitHub `README` (for YAML structure), a benchmark pipeline, and agentic workflow docs.
    3.  **Iterate to Refine:**
          - **Initial Draft:** Give Atlas a simple topic and structure.
          - **Manual Edit:** Manually edit the output to meet client standards.
          - **Reverse-Engineer:** Ask Claude to analyze the edits and generate a post-processing instruction set.
          - **Embed in Pipeline:** Add the instruction set to the Atlas pipeline (e.g., in a `content post-processing agentic workflow`).
          - **Test & Repeat:** Run new articles and refine the instructions based on the output.
  - **Example: Monograph Client:** This process reduced post-Atlas editing to 5–8 minutes per article and contributed to a 400% traffic increase.

### Supporting Structure: Client Tiers & Client Ops Engineers

  - **Client Tiering:** To manage resources, clients will be categorized:
      - **Self-Service:** Platform-only access with pre-built workflows.
      - **Core ICP:** Standard clients with high-performing pipelines (e.g., Monograph).
      - **Custom:** High-touch clients requiring custom engineering (e.g., Surge, Biologica).
  - **Client Ops Engineers:** These engineers will partner with MEs to build and optimize pipelines, enabling MEs to focus on client strategy and content quality.

---

## Action Items

**Nathalie Schrans (GrowthX)**
- Ask Marcus for Flow Studio README + workflow library enumeration method
- Ask Nana to set up Atlas sandbox for Nathalie to test pipeline-optimization workflows

**Matthew Panzarino (GrowthX)**
- Engage Ismail, Sucheta, and Martha regarding Surge production rewrite; apply the pipeline-builder approach

---

## Transcript
**Matthew Panzarino:** Hey.

**Nathalie Schrans:** Hey, Panzer.

**Matthew Panzarino:** How's it going?

**Nathalie Schrans:** Going all right, thanks.

**Nathalie Schrans:** Just finished working on some huge keyword lists for OctaCode.

**Nathalie Schrans:** That is done by now, unless I get some feedback that I need to add something.

**Matthew Panzarino:** It's like over 2,000 keywords, so hopefully there's not much more to add.

**Matthew Panzarino:** All right, sounds good.

**Matthew Panzarino:** How are things going?

**Nathalie Schrans:** Things are going okay.

**Nathalie Schrans:** Andy just told me this morning that I'll be moving back to the Strategy Sprints team.

**Nathalie Schrans:** And so after this, like, wrapping up with Augment Code this week, I won't be doing anything for Augment Code and Surge starting next week.

**Nathalie Schrans:** But, yeah, I still wanted to meet with you because I know you'll be my manager moving forward and wanted to get kind of...

**Nathalie Schrans:** And, like, I guess feedback from you based on, like, the reporting structure and also, I guess, go over, like, what I've been working on because I know I've been kind of, like, back and forth between, like, different clients or, like, processes and things.

**Nathalie Schrans:** So I wanted to kind of update you on what I've been working on as well and just, you know, me and, like, set a direction together.

**Matthew Panzarino:** Sure.

**Matthew Panzarino:** Yeah, I mean, we're going to be doing some expectation setting and direction setting for the whole team.

**Matthew Panzarino:** So I really don't – we don't need to go into that super deep.

**Matthew Panzarino:** But directionally speaking, obviously, aside from client work, which is, you know, going to be a priority for anybody, in your case, sprint team, it'll be new people and new projects, which is cool in its own way.

**Matthew Panzarino:** But aside from that, the overarching KPI for everybody is efficiency.

**Matthew Panzarino:** So that is, what is the time it takes to deliver content to a client after it's exited the pipeline?

**Matthew Panzarino:** How do we build efficiency there?

**Matthew Panzarino:** Is it a process?

**Matthew Panzarino:** Is

**Matthew Panzarino:** Is Is it a learning component?

**Matthew Panzarino:** Is it an architecture component?

**Matthew Panzarino:** Something that is engineering related?

**Matthew Panzarino:** You know, that sort of thing.

**Matthew Panzarino:** The answer is yes.

**Matthew Panzarino:** You know, it's all various things.

**Matthew Panzarino:** And you're not obviously on the hook for writing code to improve the base components of Atlas.

**Matthew Panzarino:** However, it's all of the ME layer, the delivery layer is going to be focused on building that efficiency.

**Matthew Panzarino:** And what I have found, brass tacks, is as I talk to and look at the way people are using Atlas or the processes that they are using to deliver content, it's still all over the map a little bit.

**Matthew Panzarino:** So we're getting to standardize some things.

**Matthew Panzarino:** People are using the tools incorrectly.

**Matthew Panzarino:** They are dropping stuff out of Atlas and into Cloud and frankly screwing it up.

**Matthew Panzarino:** Like there's just no reason to use a lot of these tools in a very haphazard way.

**Matthew Panzarino:** And that is unfortunately the state that they are in.

**Matthew Panzarino:** Instead of using Atlas, refining the process, giving it the proper...

**Matthew Panzarino:** It's not sustainable.

**Matthew Panzarino:** frankly causes more messes than it solves.

**Matthew Panzarino:** And eventually people get something shippable, but usually through a lot of manual labor.

**Matthew Panzarino:** So average editing time can hover in the hour and a half to two hours per piece of content, which is not feasible.

**Matthew Panzarino:** You know, you can't scale that way.

**Matthew Panzarino:** Um, we want everybody to be able to handle obviously in the near term upwards of three clients, but it could be five or more by Q2 next year.

**Matthew Panzarino:** Um, and if we want that to happen, if we want that pathway to open to us, everybody needs to build leverage.

**Matthew Panzarino:** Like I'm not going to give somebody 60 hours of work and tell them to work 40 hours and get that work done.

**Matthew Panzarino:** Instead, I want to find a way to make that 60 hours, 40 hours.

**Nathalie Schrans:** Right.

**Matthew Panzarino:** So like that, that's all about efficiency and just leaning into the process of like refining.

**Matthew Panzarino:** And getting a better handle on the way Atlas actually.

**Matthew Panzarino:** The the way it works, the way it functions, and the way it functions the best.

**Matthew Panzarino:** And usually I've been able to kind of knock some breakthroughs through for most people.

**Matthew Panzarino:** If I have them walk me through how they are utilizing Atlas, how they are actually generating content with it.

**Matthew Panzarino:** Typically these conversations, as you can imagine, start with like, oh, you know, it's taking me like two hours to fix this content after it comes out of Atlas.

**Matthew Panzarino:** I'm like, oh, interesting.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Why?

**Matthew Panzarino:** You know, what was the deal here?

**Matthew Panzarino:** And the reasons for it are varied, but there is an undercurrent here that is showing up in a couple of major ways.

**Matthew Panzarino:** One, people don't really understand the impact that artifacts have on the process and are not configuring those correctly, to be honest.

**Matthew Panzarino:** They're just too laborious.

**Matthew Panzarino:** They have internal conflicts or conflicts between one another or conflicts between themselves and the directions that are being given.

**Matthew Panzarino:** The second big problem.

**Matthew Panzarino:** A big issue people have working with Atlas is giving it way too detailed instructions, like the assignment directions, like incredibly laboriously detailed and, you know, way over-engineered.

**Matthew Panzarino:** So they're saying like, hey, I want section one to have these six ideas impacted to 150 words.

**Matthew Panzarino:** And I'm going to give you really specific instructions for each one of those, starting off on the wrong foot.

**Matthew Panzarino:** So, you know, the process is going to like churn forever on that.

**Matthew Panzarino:** It's going to try to like reconcile all of those things with the artifacts and other instructions, you know, yada, yada.

**Matthew Panzarino:** And it just doesn't need that.

**Matthew Panzarino:** To be honest, most of the time, most people would be better off giving it a topic and saying, hey, write me an article that's kind of like this shape of an article about this.

**Matthew Panzarino:** Thank you, bye.

**Matthew Panzarino:** Like they would do a better job than what they're doing.

**Matthew Panzarino:** And take less time.

**Matthew Panzarino:** Writing.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Oh, yeah.

**Nathalie Schrans:** Take me less time to edit.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** you're having...

**Matthew Panzarino:** As you probably know, it's way easier to sort of go like, oh, this idea is missing, let me add it, than it is to untangle a thread of wrong ideas from the entire piece.

**Matthew Panzarino:** And like, it's just, yeah, it's taking a finished sculpture and trying to like, subtract stuff from it and add stuff back versus taking a piece of marble and going like, ah, just whack this off on that offer, now I'm done.

**Matthew Panzarino:** Yeah, I see.

**Nathalie Schrans:** Okay.

**Matthew Panzarino:** So the, I think that's just like a reset that needs to be done there.

**Matthew Panzarino:** And I probably just need to do some more training and then, you know, kind of drilling down on it.

**Matthew Panzarino:** I'm going to be honest though, some people are probably just not going to get it.

**Matthew Panzarino:** And if they're not going to get it, they probably shouldn't work here.

**Matthew Panzarino:** And not in a bad way, you know, they're very clever and talented people.

**Matthew Panzarino:** But if they don't, if they can't acclimate to that process, then it's probably best that they don't work on this product, right?

**Matthew Panzarino:** It's just not, not the right thing for them.

**Matthew Panzarino:** Because I, the fact of the really reason I mentioned that.

**Matthew Panzarino:** That's because I've said a of these things.

**Matthew Panzarino:** You know what mean?

**Matthew Panzarino:** I've, like, said them in all hands.

**Matthew Panzarino:** I've said them one-to-one.

**Matthew Panzarino:** I've recorded videos.

**Matthew Panzarino:** But it's okay.

**Matthew Panzarino:** We'll do more, right?

**Matthew Panzarino:** We'll make sure everybody's extremely well-informed, has clear expectations, as I mentioned earlier, like the major metrics that we're tracking.

**Matthew Panzarino:** We will find ways to track them honestly and openly so everybody understands that we are not looking for ways to, like, blame people for the process being slow.

**Matthew Panzarino:** Because, as I mentioned, it's a multi-factor rationale, you know?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Like, maybe it is context engineering.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Let's dive in.

**Matthew Panzarino:** Maybe it is just process.

**Matthew Panzarino:** Maybe, though, it's a bug.

**Matthew Panzarino:** Maybe the pipeline needs to be engineered.

**Matthew Panzarino:** So that's why, as you can see, if you look at the new org chart, there are client ops engineers that are going to be embedded to help people to engineer stuff.

**Matthew Panzarino:** You know, that's absolutely necessary.

**Matthew Panzarino:** The vast majority of pipelines.

**Matthew Panzarino:** Yeah, I agree.

**Matthew Panzarino:** Across the company are just not performant for a variety of reasons.

**Matthew Panzarino:** for us.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** And some of those reasons cannot or will not or should not live in the arms of the editors or anybody else.

**Matthew Panzarino:** It needs to live in the arms of somebody who can straddle the worlds of engineering, workflow engineering, and editorial, and work hand in hand with the editors to implement the improvements that they desire.

**Matthew Panzarino:** And, like, as you get into the thick of that process, sometimes it's a revelation where you're like, oh, you know, like, you're not pulling this lever.

**Matthew Panzarino:** Like, you need to pull this lever.

**Matthew Panzarino:** And they're like, oh, I didn't even know what that lever was for.

**Matthew Panzarino:** So, like, sometimes there is that, just to be honest.

**Matthew Panzarino:** And then other times, though, it is like, hey, I've really tried to massage these things as much as I can.

**Matthew Panzarino:** I'm being really proactive.

**Matthew Panzarino:** I'm trying to lean in here.

**Matthew Panzarino:** And it's just, like, not functioning correctly.

**Matthew Panzarino:** And it's like, hey, well, maybe we can add a workflow to this pipeline.

**Matthew Panzarino:** Maybe we can tweak the existing one.

**Matthew Panzarino:** Maybe we can create a custom solution because this client has a custom need.

**Matthew Panzarino:** Unfortunately, clients all have their own needs, right?

**Matthew Panzarino:** Their own needs.

**Matthew Panzarino:** All special flowers.

**Matthew Panzarino:** And sometimes you need to service those flowers with their own fertilizers, not to stretch the analogy too far.

**Matthew Panzarino:** But you definitely, we need some in the thick of it engineering work, not just engineering work done over the fence and then like the throwing modules over.

**Matthew Panzarino:** Hey, try this, try that.

**Matthew Panzarino:** It's like, no, let's actually gear this up.

**Matthew Panzarino:** And there could be positivity that flywheels for everybody out of that.

**Matthew Panzarino:** Because if a client ops engineer works on a specific solution and then we find a way to publicize that properly across the org and read people in on why an improvement has been made, there hopefully will be lights going on for people going, I had the same problem.

**Matthew Panzarino:** I'm so glad you made this because we put this in ours, you know, and like that's inevitably that will occur.

**Matthew Panzarino:** And right now that the pathways for doing that are not absolutely clear.

**Matthew Panzarino:** Like Kirkland and Marcus can only kind of glom onto so many problems per week, right?

**Matthew Panzarino:** So we need to staff that up a bit and we will.

**Matthew Panzarino:** But yeah, that's the general.

**Matthew Panzarino:** A picture for like efficiencies, what we're looking at and where we're headed with that.

**Nathalie Schrans:** Yeah, no, that all makes sense.

**Nathalie Schrans:** And, you know, I've been working with like super custom clients for the past several weeks.

**Nathalie Schrans:** And I definitely see how kind of like continuing the way that we have been is not very sustainable.

**Nathalie Schrans:** And that's something I know that is being worked on, at least for Surge, because we kind of had to like revamp everything that we did for content production.

**Nathalie Schrans:** So I think those are kind of like the two, like Surge and Augment are like the two edge cases, I think.

**Nathalie Schrans:** Yeah, unfortunately, you have been living in like crazy places too.

**Matthew Panzarino:** They're wild clients and not standard.

**Matthew Panzarino:** We don't want a lot of those, you know, they exist for a variety of reasons on our docket.

**Matthew Panzarino:** But yeah, we can't have 80 of those, you know, we would just.

**Nathalie Schrans:** Yeah, definitely.

**Nathalie Schrans:** Yeah, no, I mean, of course, there's benefits to working with them.

**Nathalie Schrans:** But yeah, that was just kind of like in the past, like couple of months of just working them.

**Nathalie Schrans:** My concern was just that, like, how is this?

**Nathalie Schrans:** Because I know like the overall goal of everything that we're supposed to do, right, is to like build the platform.

**Nathalie Schrans:** Thank Thank

**Nathalie Schrans:** And a lot of the time, just in terms of like, because you have to meet client expectations and deliverables and everything, that wasn't always what we were working towards.

**Nathalie Schrans:** So I think having like this whole edition of client ops engineers will really help with that.

**Nathalie Schrans:** But that's not really what I'm going be working on moving forward.

**Nathalie Schrans:** It's just like my observation for the past few weeks.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** I mean, you were sort of like at the edge of where that is not just, oh, this would be nice, but it's like absolutely necessary, right?

**Matthew Panzarino:** Like those are custom clients, really we're doing custom engineering for those.

**Matthew Panzarino:** And really we're thinking about clients in a couple of buckets, well, three major buckets going, you know, into the future.

**Matthew Panzarino:** And one is self-service, right?

**Matthew Panzarino:** There's some times where it's like, hey, you know, here's a platform.

**Matthew Panzarino:** We now have analytics built.

**Matthew Panzarino:** We have a content library built.

**Matthew Panzarino:** And we've built this really cool stuff with CheckDot where you can see opportunities that are driven by LLM visibility.

**Matthew Panzarino:** And here is an engine that you can use to build pipelines.

**Matthew Panzarino:** Pipelines, these self-service customers will never see the pipelines that you see, that you and I look at every

**Matthew Panzarino:** They will never see that.

**Matthew Panzarino:** And frankly, at some point, neither will any means.

**Matthew Panzarino:** It's just not necessary, and it creates too much confusion, if we're being honest.

**Matthew Panzarino:** I just think the machinery is a little too complex to expect 50 people to operate with a delicate hand.

**Matthew Panzarino:** Anyhow, long story short, that first bucket of self-service is like, hey, here's an editorial workflow that you can play with.

**Matthew Panzarino:** Here's a bunch of inputs that you have, but, you know, plug yourself in, get stuff out, edit it, be on your way.

**Matthew Panzarino:** Then there's a second bucket, which is core ICP clients, you know, like the ones that, like a monograph, for example, is extremely happy.

**Matthew Panzarino:** It takes about, it takes less than half an hour to edit any piece of content that comes out of that pipeline to get it ready for delivery.

**Matthew Panzarino:** In some cases, five to eight minutes, you know.

**Matthew Panzarino:** Wow, yeah.

**Matthew Panzarino:** And it's performant, we're up, like, I think it's like a last, uh...

**Matthew Panzarino:** Last quarter, this quarter, I think we're up like 400% traffic.

**Nathalie Schrans:** Like, you know, it's, well, it's good, right?

**Nathalie Schrans:** Like, it's a good status.

**Nathalie Schrans:** like a case study.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** Right.

**Matthew Panzarino:** And we have some efforts there.

**Matthew Panzarino:** But yeah, it's like their content is not insanely technical.

**Matthew Panzarino:** It requires accuracy, but it is not like, here's seven blocks of code or here's 15 medical claims that will get us sued if we're wrong about them.

**Matthew Panzarino:** You know, it's a good, solid core ICB claim.

**Matthew Panzarino:** Then there's that body.

**Matthew Panzarino:** And then there is custom clients, which obviously Surge would fit more into.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** you know, other clients, even like Biologica, you know, that's really not like, it's not in our core ICB.

**Matthew Panzarino:** They have an MD, an ND, a lawyer and a co-founder review every article.

**Matthew Panzarino:** Right.

**Nathalie Schrans:** So it's medical.

**Nathalie Schrans:** Correct.

**Nathalie Schrans:** It's a supplement product.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** It's covered by DCA regulations.

**Matthew Panzarino:** There's all kinds of stuff, right?

**Nathalie Schrans:** It's from.

**Matthew Panzarino:** It's fraught.

**Matthew Panzarino:** Anyhow, long story short, we have that third bucket of custom clients.

**Matthew Panzarino:** And you've got to be honest about the needs, demands, and timelines, and cost for all of this.

**Matthew Panzarino:** And so for a custom client, okay, let's charge them a buttload of money.

**Matthew Panzarino:** But frankly, if you charge them a buttload of money and then still operate in the same mode that you are with a core ICP client, it doesn't matter how much money you charge.

**Nathalie Schrans:** We'll never deliver well.

**Matthew Panzarino:** We'll never be performant there.

**Matthew Panzarino:** I mean, technically speaking, you could probably charge enough money to be like, let's burn people out working this client.

**Matthew Panzarino:** But in all reality, that's not good business, you know.

**Matthew Panzarino:** So anyhow, long story short, those three buckets will help to clarify some of the work and the resources that are allocated to the clients and expectations around those.

**Matthew Panzarino:** And then the other component of it is, of course, better tooling, better training, better onboarding.

**Matthew Panzarino:** All of that stuff has to be kind of brushed up.

**Nathalie Schrans:** Yeah.

**Nathalie Schrans:** Yeah.

**Nathalie Schrans:** Okay.

**Nathalie Schrans:** Yeah, that all makes sense.

**Nathalie Schrans:** And honestly, this is like a big reason why I was excited to join GrowthX in the first place is like I had been building my own AI workflows and being able to do it in a more like, you know, impactful way, like larger scale way is why I was really excited to join.

**Nathalie Schrans:** And, you know, given like the custom clients I've been working on, I haven't been able to make the impact that I had imagined.

**Nathalie Schrans:** So I'm really excited to get back to strategy sprints and work on that and really like improve in Atlas and get to work on the platform that way.

**Matthew Panzarino:** So I'm really looking forward to that.

**Matthew Panzarino:** in the strategy sprint, like I know, you know, obviously you'll have the demands of whatever sprint is going on and whatever client is going on.

**Matthew Panzarino:** But really, I would say as a person, like somebody on the strategy sprint team, an ME on the strategy sprint team as opposed to an ME not on the strategy sprint team.

**Matthew Panzarino:** You might have some KPIs or directional stuff.

**Matthew Panzarino:** Anyway, I don't know if it's, it's to the degree of a custom KPI, but it really is like a directional thing like, hey, how am I winning?

**Matthew Panzarino:** And I honestly think

**Matthew Panzarino:** On a personal level, you should look at it as an opportunity to skill up, like make yourself more valuable, make yourself more, enrich your knowledge and your understanding and all of that.

**Matthew Panzarino:** On a pragmatic level, what that means is probably like, look at everything through the lens of, hey, there is 150 workflows in Flow Studio.

**Matthew Panzarino:** Like, which of these can I mix and match in Atlas to make my life easier tomorrow?

**Matthew Panzarino:** Right, right.

**Matthew Panzarino:** And like, the way that I have set it up for myself is that I have a cloud project with the readme file from our GitHub.

**Nathalie Schrans:** So, you can ask Marcus for it.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** It's the readme file that basically explains what all the major workflows do in the editorial pipeline.

**Matthew Panzarino:** And you could ask him for like, hey, what's a good way to get like the workflow library, you know, enumerated so that I understand what most of them do or can query, you know, know, like using cloud code or, or, or just.

**Matthew Panzarino:** Search on our flow studio for certain functions.

**Matthew Panzarino:** Sometimes I just do that.

**Matthew Panzarino:** I open up studio and I'm like, I wonder if we've done a PDF to, you know, whatever workflow, you know, and I can search it in there and see like, oh, okay.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Oh, Marcus just updated this yesterday.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** This is current.

**Matthew Panzarino:** You know, like this is where we can, I can use this.

**Matthew Panzarino:** And then I'll go to Claude and I'll say, hey, can you wire up this workflow into this pipeline?

**Matthew Panzarino:** I want it to kind of, I want it to accomplish this function and I want it to happen after this step, before this step, unless you think different.

**Nathalie Schrans:** You know, tell me if I'm wrong, right?

**Matthew Panzarino:** And like, and then have it, because it knows what the YAML is and what the pipeline should do and look like and what the taxonomy is, it can recompose pipelines for you very quickly and very well.

**Nathalie Schrans:** In Claude code specifically?

**Matthew Panzarino:** No, no, just Claude.

**Matthew Panzarino:** Just Claude.

**Matthew Panzarino:** You can use Claude code too.

**Matthew Panzarino:** There's no problem with that.

**Matthew Panzarino:** Um, but you don't have to, uh, and even like turning on Claude code in Claude is sometimes.

**Matthew Panzarino:** It was useful, but it's not absolutely necessary.

**Matthew Panzarino:** I just use bone standard clod projects for that.

**Nathalie Schrans:** Like I'll give you an example.

**Matthew Panzarino:** I have to remember, I have three different clod instances opened at all times, so I have to remember which one it's in.

**Matthew Panzarino:** Sorry, hold on.

**Matthew Panzarino:** Yeah, just the one.

**Matthew Panzarino:** So if I go here to, and this is in pod F, so you can look at it.

**Matthew Panzarino:** That's my Robin Hood.

**Matthew Panzarino:** Let's not look at how bad my stocks are doing.

**Matthew Panzarino:** If you look in here in the pipeline builder project, this is in our pod F account, so feel free to dive in there.

**Matthew Panzarino:** I think Nana or somebody can give you access.

**Nathalie Schrans:** They have to give you the link, you know how it works.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** But if you go into our projects, we have set this up pretty well.

**Matthew Panzarino:** By me, Nana, and Yana, we were working in our little pod on some clients for a while, so obviously this is.

**Matthew Panzarino:** It's all artifacts or byproducts of the processes that we've built.

**Matthew Panzarino:** But we try to create a project per client per task so that we don't cross wires.

**Matthew Panzarino:** So, yes, there is an overarching memory.

**Matthew Panzarino:** know, Claude now has memory if you turn it on, if you go into the account and turn it on, which ours is on.

**Matthew Panzarino:** But it also has a project memory.

**Matthew Panzarino:** And training a project to do a certain thing is a real thing.

**Matthew Panzarino:** Like, you work in a project for a while, it will learn.

**Nathalie Schrans:** It does have memory.

**Matthew Panzarino:** You can even look at the project memory and see what the deal is with it if you've turned it on.

**Matthew Panzarino:** And doing the same thing over and over in there will make it better at it.

**Matthew Panzarino:** It will understand your requirements for it, et cetera.

**Matthew Panzarino:** I don't want to belabor this.

**Matthew Panzarino:** You probably already know this.

**Matthew Panzarino:** But I just want to state that that's why we isolate functions.

**Matthew Panzarino:** So, if I'm updating artifacts for a client, that happens in the artifact updater for that.

**Nathalie Schrans:** Client.

**Matthew Panzarino:** It does not happen in the article editor for that client.

**Matthew Panzarino:** It does not happen in the pipeline builder for that client.

**Matthew Panzarino:** Whatever.

**Matthew Panzarino:** know what I Like, process function per client per task is how I recommend setting up Claude.

**Matthew Panzarino:** Or, frankly, a custom GPT, it's the same thing.

**Matthew Panzarino:** You would never, like, spin up a custom GPT for a task and then give it some other random task, right?

**Matthew Panzarino:** You would think, oh, it's not good at this.

**Matthew Panzarino:** Or it doesn't know all the context.

**Matthew Panzarino:** Anyhow, long story short, we built a pipeline builder.

**Matthew Panzarino:** I gave it the README file.

**Matthew Panzarino:** The README file basically just says, like, hey, here's the structure of the YAML files.

**Matthew Panzarino:** Here are the major variables, that sort of stuff.

**Matthew Panzarino:** This is nothing you need to memorize or even care about.

**Matthew Panzarino:** It's just a definitions file.

**Matthew Panzarino:** Like a glossary for the pipelines.

**Matthew Panzarino:** Then I gave it a pipeline example, like a benchmark, one that I like.

**Matthew Panzarino:** I gave it the documentation about agentic workflows and what they do.

**Matthew Panzarino:** And then I gave it the generic pipeline template.

**Nathalie Schrans:** Literally the one that when you hit new pipeline, this is what comes

**Matthew Panzarino:** I just gave it a generic stuff.

**Matthew Panzarino:** Now, I can go in here and tweak pipelines anytime I want.

**Matthew Panzarino:** So you can see we do a lot of tweaking over the pipeline.

**Matthew Panzarino:** Most people, most MEs, most even, you know, EMs, anybody, like most of them never have done any of this.

**Matthew Panzarino:** It's definitely a level up, and it's something that you on the sprint team, I think, should be like old hat at very quickly.

**Matthew Panzarino:** As fast as you can, because it will save you a lot of grief, and it will give you the ability to go, hey, I slammed this one together, and it's working pretty well, and you just need to tweak it, and the edge team can, like, fix problems for you.

**Matthew Panzarino:** As opposed to, like, filing a ticket and waiting for, hopefully, somebody to come along and, like, build a new pipeline.

**Matthew Panzarino:** You can build new pipelines.

**Matthew Panzarino:** It's not going to break anything to just throw new pipelines in there and mess around with them, you know?

**Matthew Panzarino:** Right, okay.

**Matthew Panzarino:** So if you go, like, as an example, I was just on with Khalil earlier today, and his default instructions in there.

**Matthew Panzarino:** I was like, this is not, he's like, I'm like, where did these come from?

**Matthew Panzarino:** And he's like, oh, like, generate them in Cloud.

**Matthew Panzarino:** I'm like, don't do this.

**Matthew Panzarino:** Just use like regular H1s, H2s, like basic structure and throw it in there and start from there.

**Matthew Panzarino:** Like a basic outline is fine, but there was like hyper detail.

**Matthew Panzarino:** And I was like, this is going to cause conflict, you know, and it's going to make it hard for it to do its job.

**Matthew Panzarino:** You know, it's going to take a long time and it's going to introduce oddities because it's trying to reconcile all of these instructions with the writing guidelines because you're prompting it and you're giving it like hybrid detail per section prompts of like five different things you need in each section and all of this stuff.

**Matthew Panzarino:** You know, not necessary, probably.

**Matthew Panzarino:** Just tell it, write a section on this and see what it comes back with.

**Matthew Panzarino:** Start from there, you know.

**Matthew Panzarino:** So, um, anyway, long story short, it was like, I'm like, okay, cool.

**Matthew Panzarino:** No problem.

**Matthew Panzarino:** I'm going to grab your pipeline.

**Matthew Panzarino:** And then I told Claude, go look at this.

**Matthew Panzarino:** I want to give you some new instructions.

**Matthew Panzarino:** And it's like, cool.

**Matthew Panzarino:** I understand.

**Matthew Panzarino:** I'm like, great.

**Matthew Panzarino:** Here's the new instructions.

**Matthew Panzarino:** This is the new assignments.

**Matthew Panzarino:** Boom.

**Matthew Panzarino:** It updated the instructions field for that.

**Matthew Panzarino:** And then because I'm lazy, I was like, hey, that's great.

**Matthew Panzarino:** I'm glad you updated that.

**Matthew Panzarino:** Can you just give me the entire pipeline so I can just copy it all at once?

**Matthew Panzarino:** And then I just copy this and then open up Atlas.

**Matthew Panzarino:** Not logged into Atlas here.

**Matthew Panzarino:** Of course not.

**Matthew Panzarino:** I'm only logged in Safari.

**Matthew Panzarino:** So then I would go into Atlas here.

**Nathalie Schrans:** Do you recommend using Safari specifically or is that?

**Matthew Panzarino:** It's just more memory efficient.

**Nathalie Schrans:** I really hate.

**Matthew Panzarino:** I just detest how much of a memory hog Chrome is.

**Matthew Panzarino:** It's the absolute worst.

**Matthew Panzarino:** And it's just a personal thing.

**Matthew Panzarino:** have like everything built on Safari, automations and all that stuff.

**Matthew Panzarino:** So no, I don't recommend it.

**Matthew Panzarino:** It's just what I use.

**Matthew Panzarino:** There's no material benefit as far as I know.

**Matthew Panzarino:** Interwell?

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** I was just kidding there.

**Matthew Panzarino:** Um, so in the editorial here, so they have this Interwell egyptic article generation, and they were kind of using this to generate multiple types of articles, like some general purpose.

**Matthew Panzarino:** I Some, you know, more PSCO.

**Matthew Panzarino:** And I said, okay, well, if you want specific instructions, and it's the same every time, you should create a format.

**Matthew Panzarino:** And he's like, oh, we have one.

**Matthew Panzarino:** I'm like, oh, great.

**Matthew Panzarino:** And so I grabbed it, and then I asked that Claude project, hey, hey, can you take this pipeline and just put these default instructions in here?

**Nathalie Schrans:** I didn't have it.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** I could have done that manually, but why, you know?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Oh, no, I missed the semicolon, and it cost me 20 minutes.

**Matthew Panzarino:** Like, just, you know, have Claude build it for you.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** You can see the Interwell ketamine for X.

**Matthew Panzarino:** This is the literal format.

**Matthew Panzarino:** It's like ketamine for behavioral therapy, ketamine for anxiety, ketamine for whatever, you know, ketamine for boils.

**Matthew Panzarino:** I don't know.

**Matthew Panzarino:** So if you go in here, what the...

**Matthew Panzarino:** So this is like what the research says about ketamine's treatment for Alzheimer's, right?

**Matthew Panzarino:** That was the topic for this one.

**Matthew Panzarino:** But in this pipeline, if you hit edit here, this is where I literally pasted this.

**Matthew Panzarino:** I said new pipeline, and then I pasted it.

**Matthew Panzarino:** If I was to update it, I would edit and then just whack it in here.

**Matthew Panzarino:** So I would literally select all and then paste it in because I told it, give me the whole pipeline, right?

**Matthew Panzarino:** Already.

**Matthew Panzarino:** So I just pasted it in and then saved it.

**Matthew Panzarino:** The reason that I am doing that is because this default assignment for article writing is all pre-filled now, right?

**Matthew Panzarino:** And you don't, this is not very repeatable, but if we go to add new, you can see it's all pre-filled here, right?

**Matthew Panzarino:** That's why I added this.

**Matthew Panzarino:** And this is a very straightforward, not, I wouldn't even call it a brief, I would call it a scale, right?

**Matthew Panzarino:** Like, you know, a framework.

**Matthew Panzarino:** And it's like formatting guidelines.

**Matthew Panzarino:** And I didn't create this.

**Matthew Panzarino:** They had this.

**Matthew Panzarino:** And I was like, hey, actually, this is good, right?

**Matthew Panzarino:** And I'll show you what.

**Matthew Panzarino:** I thought it was bad that they were doing, but like this here, H1, ketamine therapy for X, literally, this is what this is.

**Matthew Panzarino:** It's the guide to ketamine therapy for X.

**Matthew Panzarino:** Three short paragraphs, hook, context preview, H2, what is condition?

**Matthew Panzarino:** What is Alzheimer's, right?

**Matthew Panzarino:** Define it, mention key symptoms, no common comorbidities.

**Matthew Panzarino:** Great.

**Matthew Panzarino:** Sounds good.

**Matthew Panzarino:** 150 words, no problem.

**Matthew Panzarino:** That should be doable, you know, thereabouts.

**Matthew Panzarino:** H3, traditional treatments for condition, and their limitations, blah, blah, blah, right?

**Matthew Panzarino:** You get the gist.

**Matthew Panzarino:** It's like, take the condition and do this thing to it.

**Nathalie Schrans:** Do this format to it, right?

**Matthew Panzarino:** And then drop the topic in, and then I said, okay, we're going to send this one in and see what it comes back with.

**Matthew Panzarino:** I looked at this, aside from these line breaks, which could be instructed out, tell it, hey, whatever the hell these are, don't do these, you know?

**Matthew Panzarino:** I can just put that in the pipeline.

**Matthew Panzarino:** can tweak the instructions.

**Matthew Panzarino:** But aside from those, this is...

**Matthew Panzarino:** Sound.

**Matthew Panzarino:** Like I took a look at this earlier after it finished running and I'm like, this is pretty good.

**Matthew Panzarino:** Not only is it texturally better, but it's like, it's like this, some nice, like it broke this up with some bullet points.

**Matthew Panzarino:** All the links to the appropriate length.

**Matthew Panzarino:** It has the rough out, like if you mentioned, remember that first bit we asked to do these things here.

**Matthew Panzarino:** What's Alzheimer's?

**Matthew Panzarino:** This is roughly, I would say it's more like 180 if I had to guess, but it's really close to 150 words.

**Matthew Panzarino:** It gives a broad definition.

**Matthew Panzarino:** It has a pretty authentic source here.

**Matthew Panzarino:** You've got the signs of it and then the comorbidities, right?

**Matthew Panzarino:** Like, you know, you've got, it's fine.

**Nathalie Schrans:** It's close.

**Matthew Panzarino:** And you can always tweak, you know, you can always make changes from here.

**Matthew Panzarino:** So this turned out something that was pretty decent.

**Matthew Panzarino:** Like, I think you could probably grab this, drop it in, edit it according to their thing, their design.

**Matthew Panzarino:** But obviously I have not done this, so I'm not going to run roughshod over this and say this is a panacea, but it gives you a really good starting point because from here you can tweak, you know, you can tweak a variety of things.

**Matthew Panzarino:** I will tell you their artifacts are too big.

**Matthew Panzarino:** Like the company context for Interwell is 8,000 words and it does not need to be way too big.

**Matthew Panzarino:** So there are probably some other massive improvements here.

**Matthew Panzarino:** I just did this in 10 minutes on the line with him, you know, and so like this kind of work though in massaging a pipeline into shape is very doable with Claude and you are more than welcome to do it.

**Matthew Panzarino:** And I would love anybody to want to do it, but obviously not everybody is capable or wants to, and that's fine.

**Matthew Panzarino:** We'll figure it out.

**Matthew Panzarino:** That's kind of what the engineers are there for, the client ops engineers, right?

**Matthew Panzarino:** Because it's like, oh, I really have like this detailed list of things that I want to do.

**Matthew Panzarino:** And they're like, great, I'll build you a pipeline that does that.

**Matthew Panzarino:** And then you tell me if it works.

**Matthew Panzarino:** Nath, right?

**Matthew Panzarino:** That cycle.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** But on the sprint team, if you're like wanting to make your life easier, in your personal space, in Atlas, you have a test space, right?

**Matthew Panzarino:** Like, I think we probably created one for you.

**Matthew Panzarino:** But you can just mess around in there, you know, create tools for yourself.

**Matthew Panzarino:** So in like my test space, in my sandbox here, or you may have one.

**Nathalie Schrans:** Do we have one for you?

**Nathalie Schrans:** I'm not sure.

**Nathalie Schrans:** I don't, I don't think I have.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** It's okay.

**Matthew Panzarino:** It's no big deal.

**Matthew Panzarino:** Have Nana set you one up.

**Matthew Panzarino:** Because she just knows the, it's not like you probably can't, but she knows the process.

**Nathalie Schrans:** So it's easy.

**Nathalie Schrans:** Yeah, I'll ask her.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Yeah, you can set up a sandbox.

**Matthew Panzarino:** And it's just like you as a client, right?

**Matthew Panzarino:** And then I've got a bunch of weird things that I've played with in here.

**Matthew Panzarino:** And people are like, oh, troubleshoot this for me.

**Matthew Panzarino:** I'm like, all right, let me go build one.

**Matthew Panzarino:** You know, let me see what's up.

**Matthew Panzarino:** Rather than messing around in there, in their space.

**Matthew Panzarino:** And then my artifacts are like kind of messy.

**Matthew Panzarino:** It's a bunch of weird, big stuff.

**Matthew Panzarino:** I was like, what is the 24,000 token, you know, thing do here?

**Matthew Panzarino:** I'm just messing around.

**Matthew Panzarino:** So you can absolutely feel free to do that in your own space.

**Matthew Panzarino:** But honestly, inside the client space, there's no reason you can't create a pipeline.

**Matthew Panzarino:** That's not going to break anything, right?

**Matthew Panzarino:** As long as you know what's going on, you are the operator, right?

**Matthew Panzarino:** That's your space.

**Matthew Panzarino:** So you can make something and play around in there and see what's up.

**Matthew Panzarino:** So like in Biologica, as an example, we have, ignore the two editorials, the messy client.

**Matthew Panzarino:** But we've got a bunch of stuff in here, right?

**Matthew Panzarino:** And these are all different tests or different things that we're doing.

**Matthew Panzarino:** Like you can see the image generation.

**Matthew Panzarino:** These can all be archived.

**Matthew Panzarino:** We don't even do images for them anymore because we gave up.

**Matthew Panzarino:** Not sort of, not really.

**Matthew Panzarino:** But we created good images.

**Matthew Panzarino:** They just didn't like them.

**Matthew Panzarino:** But we can archive those.

**Matthew Panzarino:** But you can see this one is article gen agentic plus an FDA and CTA fix.

**Nathalie Schrans:** Like we're just testing.

**Matthew Panzarino:** It's like, hey, add a workflow.

**Matthew Panzarino:** Claude, please.

**Matthew Panzarino:** Add a workflow to this that appends a compliance disclaimer.

**Matthew Panzarino:** Add one that formats medical annotations a specific way.

**Matthew Panzarino:** Add one that annotates medical claims.

**Matthew Panzarino:** Add one that validates writing claims.

**Matthew Panzarino:** Add one that makes sure that biological products are mentioned in the right way.

**Matthew Panzarino:** You know, all of that stuff.

**Matthew Panzarino:** You can do any of this.

**Matthew Panzarino:** It's completely malleable.

**Matthew Panzarino:** Most of these are, the same workflow under the hood.

**Matthew Panzarino:** Under the hood, they are the content post-processing agentic workflow.

**Nathalie Schrans:** It's basically an agent that does post-processing, right?

**Nathalie Schrans:** Now it's just different tasks.

**Matthew Panzarino:** Correct.

**Matthew Panzarino:** We've just given them different tasks.

**Matthew Panzarino:** And you can see it right here, right?

**Matthew Panzarino:** The input is this rules artifact, this ingredient compliance rules artifact.

**Matthew Panzarino:** And then it's, this is the whole artifact here.

**Matthew Panzarino:** Obviously, they need all this stuff mentioned in really hyper-specific ways.

**Nathalie Schrans:** That's why this is.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** And then violations, common violations, blah, blah, blah.

**Matthew Panzarino:** But.

**Matthew Panzarino:** But then what it does is it reads those instructions, then it evaluates it.

**Matthew Panzarino:** Hey, this is strong accuracy, but there should improve with moderate revisions.

**Matthew Panzarino:** We've gotten this good enough to where it almost is almost good.

**Matthew Panzarino:** Like this is actually not finding much anymore, but we really needed it at the beginning, trust me.

**Matthew Panzarino:** But like priority one compliance passed, all ingredients comply with approved list.

**Matthew Panzarino:** Like you took these instructions from that rules, right?

**Matthew Panzarino:** But you can see how it's executing on that in here.

**Matthew Panzarino:** But I don't want to dive too deep into biologically.

**Matthew Panzarino:** It is so weird, but I just want to show you it is completely possible to like add stuff to this pipeline or tweak it or reorder it according to logic.

**Matthew Panzarino:** You know, just think quickly about it.

**Matthew Panzarino:** Like, you know, oh, okay, I wanted to make sweeping changes to the article.

**Matthew Panzarino:** Okay, you should, you can even ask Claude, where should this go so that we end up with the best output?

**Matthew Panzarino:** And a lot of times it'll tell you, well, you should put it after this step because it'll conflict if you put it after this step, right?

**Matthew Panzarino:** Like, or it'll reintroduce issues.

**Matthew Panzarino:** Like, just as a simple example.

**Matthew Panzarino:** example.

**Matthew Panzarino:** If you tell it, please remove all EM dashes, you know, in a post-processing instruction, and then you tell it, please add three sections, guess what?

**Matthew Panzarino:** You know, EM dashes are going to reappear in those new sections.

**Matthew Panzarino:** So it's just a simple, like, logic puzzle there.

**Matthew Panzarino:** But God can help, once again.

**Matthew Panzarino:** But, like, the validate writing guidelines step, which most of the agentic ones have, the reason this exists is because we did this process.

**Matthew Panzarino:** Like, Nana and I, and Yana to some degree, sat down and we're like, what do we need to happen to this content before it exits Atlas so we don't have to do so much after it exits Atlas?

**Nathalie Schrans:** All the manual edits, yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** I mean, that drives directly to the prime KPI, which is how can we shorten the amount of time between Atlas exit and client delivery?

**Matthew Panzarino:** So, if we're able to compress that, then...

**Matthew Panzarino:** We win.

**Matthew Panzarino:** That's it.

**Matthew Panzarino:** That's the way it works.

**Matthew Panzarino:** If we're able to compress that enough, we will win.

**Matthew Panzarino:** Everything will be cool.

**Matthew Panzarino:** If we can't compress it enough, we will not win.

**Matthew Panzarino:** So the idea behind that checklist was simply that.

**Matthew Panzarino:** How do we increase our leverage?

**Matthew Panzarino:** And the way that that coalesced is if we go into our cloud projects.

**Matthew Panzarino:** Remember I mentioned we had ones for specific tasks.

**Matthew Panzarino:** So like the pipeline builder, obviously, but let me go.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Biological article editor, right?

**Matthew Panzarino:** This has all the contextual artifacts, plus some examples of good articles that we liked, some examples of good CTAs, you know, all anything it might need to like make changes or updates.

**Matthew Panzarino:** You can see that we are legal software.

**Matthew Panzarino:** It's she

**Matthew Panzarino:** Still doing some revision stuff in Claw because like after client review, as an example, we can use this.

**Matthew Panzarino:** It's not like you can't use Claw.

**Matthew Panzarino:** It's just you shouldn't have to do hours and hours of work in here or manually after it exits the pipeline.

**Matthew Panzarino:** What you are looking for is a recipe.

**Matthew Panzarino:** Like what instruction set, what prompt library can I give the pipeline to shorten that amount of editing time?

**Matthew Panzarino:** What do I need to happen to this stuff so I don't have to do it myself?

**Matthew Panzarino:** Like that is the answer or the question that you have to answer.

**Matthew Panzarino:** This proofreader checklist for Biologica was that answer for us.

**Matthew Panzarino:** It was like what needs to happen?

**Matthew Panzarino:** Okay, here's the things that need to happen.

**Matthew Panzarino:** You need to – well, these are instructions on how to do this.

**Matthew Panzarino:** But basically it's like compound sentences, numbers.

**Matthew Panzarino:** Like we want certain things to happen with these numbers.

**Matthew Panzarino:** Like always present them this way, never this way.

**Nathalie Schrans:** I mean remember I told you they are super picky, right?

**Matthew Panzarino:** But there's really hyper-specific stuff here that we were having to do manually or semi-manually with Claude every time.

**Matthew Panzarino:** This did not come out fully formed.

**Matthew Panzarino:** This checklist did not appear out of the ether.

**Matthew Panzarino:** It happened because I manually edited the articles.

**Matthew Panzarino:** I took the article out, put it in Google Docs, edited the crap out of it until I thought it was perfect, gave it to the client.

**Matthew Panzarino:** They loved it, came back, a couple revisions, edited it again.

**Matthew Panzarino:** And then I said, hey, Claude, what did I do to this article?

**Matthew Panzarino:** Or to myself, what did I do to this article?

**Matthew Panzarino:** What needs to happen to this?

**Matthew Panzarino:** And the answers became my first version of this, right?

**Matthew Panzarino:** The first version of this list, this checklist.

**Matthew Panzarino:** This is an editorial checklist of sorts, right?

**Matthew Panzarino:** A proofreading or editorial checklist that anybody would have, any human would have for a client, you know, to make sure that everything is good.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** But this was built piece by piece over time.

**Matthew Panzarino:** I cannot even show you the earlier one because there's so much water under the bridge with this client.

**Matthew Panzarino:** But like the earlier versions of these, look here, show you, I'll show you this.

**Matthew Panzarino:** This is a different client, but it doesn't matter.

**Matthew Panzarino:** Process is the same.

**Matthew Panzarino:** The earliest versions of these were actually in my own cloud account because I was just experimenting.

**Matthew Panzarino:** And I'm like, oh, I need to move this to a pod.

**Matthew Panzarino:** That's why everybody has pod accounts now because I'm like, hey, we need pod accounts.

**Matthew Panzarino:** But then this right here, let me do like this one.

**Matthew Panzarino:** So this is like four months ago when we just started this process with Monograph, why I took over the account.

**Matthew Panzarino:** And I'm like, why is this so crap coming out of the pipeline?

**Matthew Panzarino:** What needs to be better about this?

**Matthew Panzarino:** I edited them manually.

**Matthew Panzarino:** Then after doing that.

**Matthew Panzarino:** I went into Claude and started giving it those prompts that I'd come up with, those instructions.

**Matthew Panzarino:** And I said, hey, do this one.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** It pulled in the context.

**Matthew Panzarino:** It does the thing.

**Matthew Panzarino:** It gives me a report.

**Matthew Panzarino:** I'm like, cool, that's great.

**Matthew Panzarino:** Apply those.

**Matthew Panzarino:** Then do the next thing, just this one.

**Matthew Panzarino:** And then I'm basically testing.

**Matthew Panzarino:** Does it understand these instructions?

**Nathalie Schrans:** Will it do this?

**Matthew Panzarino:** And if not, let me refine.

**Matthew Panzarino:** Like my first one was just replace M dashes with more appropriate punctuation.

**Matthew Panzarino:** I didn't get that.

**Matthew Panzarino:** didn't understand that.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** Then I was like, okay, wait, wait, wait.

**Matthew Panzarino:** Use columns and some of my columns.

**Matthew Panzarino:** You know what mean?

**Matthew Panzarino:** Like this evolved.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** But then I'm still firing this off and like observing closely.

**Matthew Panzarino:** Okay, tell me what you did here.

**Matthew Panzarino:** Oh, okay, I see.

**Matthew Panzarino:** Yeah, that's fine.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Now, use this resource.

**Matthew Panzarino:** Use these examples to look for opportunities to reference them as supporting statistics.

**Matthew Panzarino:** They gave us a nice, big, chunky site full of case studies.

**Nathalie Schrans:** So it's like, hey, go look at this case study site for statistics to pepper in.

**Nathalie Schrans:** Right?

**Matthew Panzarino:** And it's like, yeah, yeah, no problem, I can do that.

**Matthew Panzarino:** I see what you mean.

**Matthew Panzarino:** I searched, I found it, you know, eight relevant sections, and then I'll add these statistics.

**Matthew Panzarino:** That's great.

**Matthew Panzarino:** Budget risk ban, I added 66% fewer budget over a statistic when discussing project risk-binding.

**Matthew Panzarino:** And it has a source for that, because they gave it to us, which is great.

**Matthew Panzarino:** So that's awesome.

**Matthew Panzarino:** Then linking, you know, so on and so forth.

**Matthew Panzarino:** That's all one at a time, observing, understanding, tweaking.

**Matthew Panzarino:** Then, once I have gotten that flow down, I'm able to see this post-process instructions now.

**Matthew Panzarino:** This is just a collated version of all of those instructions.

**Matthew Panzarino:** And now, when we go to, like, edit an article for, for a monograph, most of this stuff should already be done.

**Matthew Panzarino:** But, if we need to, now we can just tell it, please run the commands done in post-processing instructions.

**Nathalie Schrans:** Thanks, bye.

**Matthew Panzarino:** So it's a one-shot.

**Matthew Panzarino:** The project has learned.

**Matthew Panzarino:** We have refined the prompts.

**Matthew Panzarino:** We've understood it, you know, et cetera.

**Matthew Panzarino:** And it goes out and looks.

**Matthew Panzarino:** And it says it made it look compliance.

**Matthew Panzarino:** Yep.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** So it changed this, changed to monograph.

**Matthew Panzarino:** Okay, that's fine.

**Matthew Panzarino:** Yeah, yeah, yeah, yeah, yeah.

**Matthew Panzarino:** And it did all that, right?

**Matthew Panzarino:** And then we can look at it, give me it.

**Matthew Panzarino:** And then this one is like some additional hyperlinking thing we were testing.

**Matthew Panzarino:** But that was pretty much it.

**Matthew Panzarino:** It was like one command.

**Matthew Panzarino:** I will say, though, that that instruction set is mostly done.

**Matthew Panzarino:** It didn't do much, actually.

**Matthew Panzarino:** Now, because that is in the monograph pipeline.

**Matthew Panzarino:** Like, those instructions are in a post processor that I showed you in the monograph pipeline.

**Nathalie Schrans:** And it does those.

**Matthew Panzarino:** And it does a pretty good job.

**Matthew Panzarino:** So, like, editing their articles is pretty quick once it comes out.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** So, that is the feedback loop, right?

**Nathalie Schrans:** Right.

**Matthew Panzarino:** So, let's see, you get a client.

**Matthew Panzarino:** If with Sprint and you're trying to like engineer a pipeline to do them, it's about saying like, oh, okay, they need this to happen.

**Matthew Panzarino:** Let's say they have a really hyper-specific CTA format.

**Matthew Panzarino:** They're like, we want one paragraph that says this, second paragraph sets this up, and third paragraph says, you know, try it out with this link, right?

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** You can spend all day trying to figure out like what the right format for that is, or like instructions to get that exact format every time, or you can write two or three of them, put them in an artifact, and then add a post processor to the pipeline that says, look at the CTA's good artifact, and insert a CTA at the end of the article with those characteristics.

**Matthew Panzarino:** Please do not write this content, or copy this content exactly, only use it as inspiration, thank you very much, and then fire it off, and then you run some tests, and see what happens.

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** But I can tell you from experience it.

**Matthew Panzarino:** Because that's what we do for Monograph.

**Nathalie Schrans:** Monograph has one.

**Matthew Panzarino:** And it's basically like, hey, go look at this artifact and, you know, do this.

**Matthew Panzarino:** Now, you don't even have to make that a post-processor.

**Matthew Panzarino:** Like, we're going through the stages here of the brain explosion meme, right?

**Matthew Panzarino:** The beams.

**Matthew Panzarino:** It's like, the euphoria phase of this is the end stage is you can actually tell Claude to have the artifact draft or the article drafter call that.

**Matthew Panzarino:** So you can say, hey, when you're drafting this article, make sure that the article drafter knows that we need a CTA like this and show it this artifact, you know.

**Nathalie Schrans:** It's not a post-processing step anymore.

**Matthew Panzarino:** It's really a in-process step or whatever you want to call it.

**Matthew Panzarino:** Yeah, Whatever it should be called.

**Nathalie Schrans:** Yeah, it's not post, it's not free.

**Matthew Panzarino:** It is now.

**Matthew Panzarino:** It's home.

**Matthew Panzarino:** But yeah, that's pretty much it.

**Matthew Panzarino:** It's basically like, hey, you can tell it to reference other things.

**Matthew Panzarino:** Like there's no reason that article drafter can't reference other artifacts, ideas, concepts.

**Matthew Panzarino:** If it's in Atlas, it can see it, you know?

**Nathalie Schrans:** It's just the standard is the three main artifacts.

**Matthew Panzarino:** Yes, correct.

**Matthew Panzarino:** It's like, you gotta have some baseline, right?

**Matthew Panzarino:** And the baseline is who are we writing for?

**Matthew Panzarino:** What are we writing about?

**Matthew Panzarino:** And how do we write about that?

**Matthew Panzarino:** Right?

**Matthew Panzarino:** And like, that is, that's like the baseline bit, but it does not mean that's where you have to stop.

**Matthew Panzarino:** This is clay, right?

**Matthew Panzarino:** Like it is malleable clay and it does not, you do not have to like, just let it be whatever it is.

**Matthew Panzarino:** You can make tweaks, you can make tweaks, it, you can, you know, get more complex.

**Matthew Panzarino:** The article drafter and the post-processor.

**Matthew Panzarino:** you.

**Matthew Panzarino:** are pretty much the ones, you know, that you want to focus on, but it doesn't mean you can't pull in specific workflows that have been built or file tickets for new workflows to be built, right?

**Matthew Panzarino:** Where you're like, hey, we really need a workflow that does this.

**Matthew Panzarino:** Like as an example for any PSCO engagement, right?

**Matthew Panzarino:** So you, hey, we need a workflow that scrapes data from this source and formats it in this way.

**Nathalie Schrans:** Cool.

**Matthew Panzarino:** File a ticket.

**Matthew Panzarino:** You know, that's not, you don't have to figure that out.

**Matthew Panzarino:** File a ticket and get them to do it, you know?

**Matthew Panzarino:** So like, I think that's, you know, that's an example of one where you would want to go like, hey, well, let's file a ticket for this.

**Matthew Panzarino:** Like, let me not take this into my own hands and do it.

**Matthew Panzarino:** It's nothing saying you can't do it, but it's understandably going to be a more complex process, right?

**Nathalie Schrans:** Yeah.

**Nathalie Schrans:** And what's more productive.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** So like right here, this one for metronome, it takes the URL of a company and then it scrapes...

**Matthew Panzarino:** Data, right?

**Matthew Panzarino:** It like scrapes pricing data, does customer sentiment research analysis, and then pulls customer sentiment out of it.

**Matthew Panzarino:** It does a pricing analysis to like, hey, what is this pricing and how does it fit?

**Matthew Panzarino:** Then it formats all this stuff.

**Matthew Panzarino:** It does a metronome's take, which takes internal documentation that we solicited from a metronome about their thoughts and feelings and vibes about certain pricing models, and synthesizes a metronome's take summary.

**Matthew Panzarino:** Using that documentation as its knowledge base, right?

**Matthew Panzarino:** And then it says like, hey, here you go.

**Matthew Panzarino:** Here's what metronome thinks about that.

**Matthew Panzarino:** And then it packages that it does a bunch of post-processing and then packages it, right?

**Matthew Panzarino:** So here's the post-processing, or here's the actual page right here.

**Matthew Panzarino:** So it has the pricing snapshot for Luminance.

**Matthew Panzarino:** It has the product overview, the key features, the pricing model analysis, the pricing evolution timeline.

**Matthew Panzarino:** Here they changed in 2016, 2017, so on and so forth.

**Matthew Panzarino:** Here's the source for that, you know, for that pricing.

**Matthew Panzarino:** Here's the customer sentiment highlights and lowlights.

**Matthew Panzarino:** And then we actually exercise.

**Matthew Panzarino:** Oh, no, here it is.

**Matthew Panzarino:** Yeah, here's a metronome stake.

**Matthew Panzarino:** Luminance operates a sophisticated licensing model.

**Matthew Panzarino:** Here's what we think about that.

**Matthew Panzarino:** Here's why it's cool.

**Matthew Panzarino:** You know, whatever.

**Matthew Panzarino:** And this is all packaged up in JSON, and it's sent over to them, and then they deploy it on their site in the pricing directory.

**Matthew Panzarino:** So the workflows are capable of all of this.

**Matthew Panzarino:** It's just a matter of like, wrapping your head around the requirements is a large portion of it, right?

**Matthew Panzarino:** And the requirements in the case of an editorial workflow are what do we need to include in this process at the beginning?

**Matthew Panzarino:** And then of course, what do we need to post process?

**Matthew Panzarino:** What are we missing?

**Matthew Panzarino:** What's the edits we need to make consistently over and over?

**Matthew Panzarino:** And I think it's just important to remember that

**Matthew Panzarino:** That it is, if something is bad in the output, by that I mean coming out of Atlas and you know you need to change X before you would ever send it to a client, right?

**Matthew Panzarino:** That is bad.

**Matthew Panzarino:** Wrong.

**Matthew Panzarino:** It's a zero, not a one.

**Matthew Panzarino:** If that is bad, there are basically a handful of things that you can alter.

**Matthew Panzarino:** The context, the instructions, or the pipeline, right?

**Matthew Panzarino:** That's the knobs you have to twiddle.

**Matthew Panzarino:** And the pipeline sometimes is you, as I just showed you, or feel free, experiment, play, whatever.

**Matthew Panzarino:** Sometimes it's Inge.

**Matthew Panzarino:** Sometimes it's like, hey, I really need this complex thing to happen.

**Matthew Panzarino:** And frankly, I don't know if any of these workflows do it, you know?

**Matthew Panzarino:** And they're like, actually, we built one.

**Matthew Panzarino:** You probably don't know about it, but here it is, you know?

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** Great.

**Matthew Panzarino:** Add it to the pipeline and we'll test away, right?

**Matthew Panzarino:** Sometimes it's, there is an internal conflict between artifacts that is causing...

**Matthew Panzarino:** Some sort of loggerhead issue or weirdness.

**Matthew Panzarino:** then sometimes, as I illustrated with the, like, oh, I never showed you the why I changed it bit from Interwell.

**Matthew Panzarino:** But, like, sometimes it's, like, a bit of wrong think about how the pipelines work that is contributing to, frankly, giving, like, generating problems where there are none.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** And it's, like, that example that I showed you, those instructions here, the original instructions for this particular article are, like, incredibly detailed.

**Matthew Panzarino:** Like, you know, here's this three short paragraphs, hook, you've got to do this about Alzheimer's, you've got to do this about this.

**Matthew Panzarino:** H2, what is Alzheimer's?

**Matthew Panzarino:** Look at this.

**Matthew Panzarino:** One, two, three, four, five, six points.

**Matthew Panzarino:** It's got to fit into 150 words.

**Matthew Panzarino:** And there has to be these specific things or else you're screwed.

**Matthew Panzarino:** And I was like, hey, where did this come from?

**Matthew Panzarino:** And he's like, oh, we generated it in Claude.

**Matthew Panzarino:** Why?

**Matthew Panzarino:** You know, like, why?

**Matthew Panzarino:** This uses Sonic 4.5 to generate the article.

**Matthew Panzarino:** So just tell it to do the same thing.

**Matthew Panzarino:** know, tell it the basic structure that you want.

**Matthew Panzarino:** And it will do these things.

**Matthew Panzarino:** It's like additional steps for no reason, first of all.

**Matthew Panzarino:** And that's time.

**Matthew Panzarino:** What does it take you?

**Matthew Panzarino:** 20 minutes to do that?

**Matthew Panzarino:** You, like, go over it, prompt it, look at it, adjust it, tweak it, copy it out, piece it in here.

**Matthew Panzarino:** You know, that's like an additional 15 minutes for every piece of content, right?

**Matthew Panzarino:** But then in addition to that, it also adds an enormous surface area for conflict and oddity.

**Matthew Panzarino:** Like, how am I, like, oh, in 190 words, how am I supposed to juggle all this and adhere to the writing guidelines and adhere to the persona language that you gave me?

**Matthew Panzarino:** You know what I mean?

**Matthew Panzarino:** Like, that's a lot.

**Matthew Panzarino:** And it's a recipe for getting, like, weird words.

**Matthew Panzarino:** Balls of text or really strange sentence structures or kludges like colons, right?

**Matthew Panzarino:** Because like what does it do when it's trying to cram a bunch of ideas into a sentence?

**Matthew Panzarino:** It uses for shortening, aka m dashes, colons, semicolons, a lot of odd punctuations that allow it to like cram clauses into sentences so they can meet the word count rather than just saying something in plain English and moving on to this day, right?

**Matthew Panzarino:** So like that's how these things are interpreted.

**Matthew Panzarino:** And if you see these things, it can be hard to untangle when you've got an 8,000 character, you know, piece of context and you think you're doing it a favor by giving it really detailed instructions up front.

**Matthew Panzarino:** Like all of these instructions, like, oh man, I gave it everything.

**Matthew Panzarino:** you don't, you need to get, it, it's problem.

**Matthew Panzarino:** It's confused, you know?

**Nathalie Schrans:** Yeah, that works when you're just working in ChatGPT or something, when you don't have a whole platform built.

**Matthew Panzarino:** For sure.

**Matthew Panzarino:** If I hand wrote this and gave it to Claude, I would expect a pretty solid result out of it, right?

**Matthew Panzarino:** However, Claude is not an agent, right?

**Matthew Panzarino:** Like, this is an agentic process.

**Matthew Panzarino:** It has a job to be done that's defined.

**Matthew Panzarino:** It has a rubric for good.

**Matthew Panzarino:** And it has a looping architecture.

**Matthew Panzarino:** So it's going to go out there and try and do this job.

**Matthew Panzarino:** And when it goes out to the draft it, you can see what it does.

**Matthew Panzarino:** It goes out and it stores the data.

**Matthew Panzarino:** generates the draft.

**Matthew Panzarino:** Then it runs three different evals on it, runs plans, and executes improvement three different times.

**Matthew Panzarino:** The last time, it looks like it didn't.

**Matthew Panzarino:** It ran two plans, and by the second one, it gave up.

**Matthew Panzarino:** It either thought it was good enough or it gave up, right?

**Matthew Panzarino:** But you can see what it's doing here by going into Flow Studio.

**Matthew Panzarino:** And you can see exactly what it's doing.

**Matthew Panzarino:** Okay, what are the critical things?

**Matthew Panzarino:** I need to add this missing FAQ section.

**Nathalie Schrans:** Exactly 250 words, probably a problem.

**Matthew Panzarino:** Probably an issue, you know?

**Matthew Panzarino:** Answer new H2, include these four questions with detailed answers.

**Matthew Panzarino:** Each issue will reach exactly 250.

**Matthew Panzarino:** I mean, this is going to drive it crazy trying to do this, you know?

**Matthew Panzarino:** So there's instructions and stuff like that, too, you know?

**Matthew Panzarino:** So that's just our attempt.

**Matthew Panzarino:** So anyhow, sorry for brain dumping on you.

**Nathalie Schrans:** No, this is really helpful.

**Matthew Panzarino:** Because you're going be in Sprint, it could be useful, you know?

**Nathalie Schrans:** Yeah, no, I agree.

**Nathalie Schrans:** And that's what I'm really looking forward to, getting back into strategy with Sprint and Stewing.

**Nathalie Schrans:** Because I was kind of working on, like, one strategy Sprint client.

**Nathalie Schrans:** But because most of my time was being dedicated to these super custom clients, I wasn't able to, you know, do as much of this type of work as I'd like.

**Nathalie Schrans:** So I'm really excited to get back to that and, you know, experiment.

**Nathalie Schrans:** And I really appreciate, you know, you taking the time to show me, like, your process and, like, examples of how you've been doing things.

**Matthew Panzarino:** Because that's true.

**Matthew Panzarino:** So I really appreciate the time there.

**Matthew Panzarino:** Yeah, you bet.

**Matthew Panzarino:** Of course.

**Matthew Panzarino:** I'm happy to help anybody build leverage.

**Matthew Panzarino:** And, you know, it's, it is fun when you're able to, like, you know, run, do reps on it and know that you have some clay to play with, you know, versus the thing where you're like, ah, this pipeline just really isn't working and I'm going to go, like, bare knuckle this thing and, like, you know, get my fingers all bloody, getting this stuff out.

**Matthew Panzarino:** You know, that's not fun.

**Matthew Panzarino:** It's, you know, it works, right?

**Matthew Panzarino:** Of course.

**Matthew Panzarino:** Like, I can manually write all these articles for a client, sure.

**Matthew Panzarino:** But it wouldn't be, you know, fun or sustainable.

**Matthew Panzarino:** So this kind of work, I think, is the fun bit.

**Matthew Panzarino:** So hopefully you can get your hands dirty there a little bit.

**Nathalie Schrans:** Yeah, definitely.

**Nathalie Schrans:** I think that's the problem that I've encountered and I've heard from other people is having to prioritize delivering to clients means having to basically bypass these ways of improving the platform.

**Nathalie Schrans:** Like, that's why people end up working outside just to get something that's ready to deliver.

**Nathalie Schrans:** To a client.

**Nathalie Schrans:** So I think at least from my experience and what I've heard from other people, I think that's the main challenge.

**Matthew Panzarino:** So it just depends, I guess.

**Matthew Panzarino:** Yeah, I mean, I empathize, right?

**Matthew Panzarino:** Like it is.

**Matthew Panzarino:** Yes, it is the main challenge.

**Matthew Panzarino:** You got it because that's efficiency, right?

**Matthew Panzarino:** So it all ties in.

**Matthew Panzarino:** Unfortunately, it's like, I think a lot of it is, I hesitate to use the word operator error, but it is operator misalignment.

**Matthew Panzarino:** Like, you know, they're, they're going like, Hey, this isn't producing it right.

**Matthew Panzarino:** I just kind of like step out and do this in Claude.

**Matthew Panzarino:** Okay, but you're, you're using it wrong, literally.

**Nathalie Schrans:** Right.

**Matthew Panzarino:** And like, that's wrong.

**Nathalie Schrans:** And so it's, because a lot of people, yeah, a lot of people do those super custom assignment directions.

**Nathalie Schrans:** Like I was talked to someone who said they do like full manual analysis of the top pages on the SERP, take notes on what they should cover, then create like assignment directions using Claude.

**Nathalie Schrans:** And it's like really long detailed assignment directions.

**Nathalie Schrans:** And you know, the output was good.

**Nathalie Schrans:** The drafts were good, but I didn't know that's what was happening kind of like in the beginning stages.

**Nathalie Schrans:** And that's just, that's what I used to do, like, before we had all these tools, like manually doing all That's what I would do too, of course.

**Matthew Panzarino:** Yeah, you're basically doing the research at that point.

**Matthew Panzarino:** Like, you don't need the researcher and all that.

**Matthew Panzarino:** But yeah, you don't need to do it.

**Matthew Panzarino:** That's why the tools are here.

**Matthew Panzarino:** And, like, the instinct to do that is just really born, I think, of the fact that, like, people go into these things thinking they need to be so detailed and give it so much instruction.

**Matthew Panzarino:** And unsurprisingly, what they get back is gibberish.

**Matthew Panzarino:** And they're like, oh, I guess I have to, like, give it more.

**Matthew Panzarino:** I'd say no.

**Nathalie Schrans:** No.

**Matthew Panzarino:** You're going to give it less, right?

**Matthew Panzarino:** Like, let it do its thing.

**Matthew Panzarino:** It is a self-guided process to some degree.

**Matthew Panzarino:** You just need to give it directionality.

**Matthew Panzarino:** And it knows what it's doing, frankly.

**Matthew Panzarino:** Like, if you went in there for a client that you're having issues getting good, decent content out, and you literally just gave it a title and said, hey, write me an article like this.

**Matthew Panzarino:** You would probably be closer than you are getting with, like, incredibly detailed.

**Nathalie Schrans:** Right, all the pre-processing, essentially.

**Nathalie Schrans:** Yeah.

**Nathalie Schrans:** Yeah, okay.

**Matthew Panzarino:** Yeah, I think honestly.

**Nathalie Schrans:** there, you know?

**Nathalie Schrans:** Yeah, yeah, I agree.

**Nathalie Schrans:** I think it might be worth for whatever's happening with Surge, because I'm not going to be involved with that after this week, just for your knowledge of what's happening there, because everything is super custom, and they're basically rewriting everything from scratch right now.

**Nathalie Schrans:** And I think it would be helpful for the people working on that account to, like, see it from this perspective, because I know that's been a big challenge for them.

**Matthew Panzarino:** Yeah, who's working to, who's moving to that account?

**Nathalie Schrans:** Ismael is the one leading, like, all of this, like, redoing content production, and then it's also Sucheta and Martha who are working on content production moving forward.

**Matthew Panzarino:** Yeah, yeah, cool.

**Matthew Panzarino:** Yeah, I'll get in the mix there a little bit.

**Matthew Panzarino:** But because it's a custom client, I basically just, I want

**Matthew Panzarino:** I concentrate on the ones that have the highest impact.

**Matthew Panzarino:** Yeah, yeah, of course.

**Nathalie Schrans:** I just think, I mean, just like based on like what would, when Ismail and I were working together and what I know is happening with the workflow, I think it would benefit from this because I learned so much.

**Matthew Panzarino:** Yeah, good, good.

**Matthew Panzarino:** I mean, I think all of them really need a client opposite engineer.

**Matthew Panzarino:** I'm a poor substitute, frankly, for somebody working in close loop and like, you know, helping people to customize pipelines.

**Matthew Panzarino:** I'll do my best, but it is certainly, everybody needs that close read and close loop.

**Matthew Panzarino:** And leadership knows this, right?

**Matthew Panzarino:** Like I've communicated it, we're aware of it.

**Matthew Panzarino:** We need it to happen because if we don't get that loop going and get that improvement cycle going, building leverage will be tough.

**Matthew Panzarino:** I can't hire enough unicorns who happen to be engineers, pipeline engineers, and LLM engineers, and good editors.

**Nathalie Schrans:** And you know what I mean?

**Matthew Panzarino:** Like sure, every once in a while you're lucky and somebody's willing to jump in like yourself or...

**Matthew Panzarino:** milestone That's Thank

**Matthew Panzarino:** They already have some previous code experience.

**Matthew Panzarino:** Kirkland, as an example, started out in journalism and now he's an engineer.

**Matthew Panzarino:** Sure, there are a handful of those people out there, but not a lot.

**Matthew Panzarino:** And you can't hire enough of them.

**Matthew Panzarino:** So you really need to hire people who are client ops engineers, who can do a close read and do that in lockstep with the editors who are like, here's the flavor that I want, here's the feel that I need from this, and then find a way to engineer that in.

**Matthew Panzarino:** But yeah, I agree with you.

**Matthew Panzarino:** I mean, think everybody could do it.

**Matthew Panzarino:** If only I had the time to like do these sessions with everybody in a really short order, I will, but a lot more long term.

**Matthew Panzarino:** So we got to hire some people to get in there and engineer these pipelines.

**Nathalie Schrans:** So yeah, I think they'll definitely benefit from that because it's so very custom and the client has very particular pace.

**Nathalie Schrans:** So I think there's a lot of potential for success there.

**Nathalie Schrans:** think it's just a lot of work for them.

**Matthew Panzarino:** So yeah, I think it'll be good though.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Thank you very much.

**Matthew Panzarino:** so much, Panzer.

**Matthew Panzarino:** I appreciate it.

**Matthew Panzarino:** Ciao, ciao.
