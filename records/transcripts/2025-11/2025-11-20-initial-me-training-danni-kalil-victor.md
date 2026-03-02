# Initial ME training - Danni, Kalil, Victor

<metadata>
date: 2025-11-20
time: 16:58 UTC
duration: 78 minutes
organizer: Victor Alagbe
participants: Danni Roseman, Kalil Magtoto, Victor Alagbe, Matthew Panzarino
fathom_recording_id: 103196800
fathom_url: https://fathom.video/calls/480099364
share_url: https://fathom.video/share/eMY-EL_6ohjcMTyMp2s788mbk1VjVkU-
source: fathom
enriched_on: 2026-03-02 15:30 UTC
</metadata>

---

## Summary

Matthew Panzarino onboarded three new Managing Editors (Danni Roseman, Kalil Magtoto, Victor Alagbe) to GrowthX's Atlas platform and defined the primary KPI: reduce post-pipeline editing time per deliverable from 1–1.5 hours to 15 minutes, enabling the services team to scale from ~70 to 100+ clients. The session covered the four-step improvement workflow (refine prompt/context artifacts, file engineering tickets, edit pipeline YAML), demonstrated Atlas's flexibility through the Metronome pricing directory project (data scraping + sentiment analysis → structured JSON), and explained how agents self-correct using rubric-based scoring. Danni will focus on defining output formats for community content; Kalil and Victor will run 5 Atlas items each, tracking editing time and compiling proofreader checklists to establish the editing baseline.

---

## Context

Matthew Panzarino (Head of Operations) conducted this training as part of onboarding three new Managing Editors (MEs) to the content operations team at GrowthX. The organization is at an inflection point: currently serving ~70 clients with high satisfaction rates, but facing a scaling bottleneck in content operations. Atlas, GrowthX's AI-powered content generation platform, is the core tool for addressing this bottleneck. The new MEs bring diverse backgrounds (Kalil from biopharma content, Victor from tech/web storage) and will be paired with experienced mentors (Danni is working directly with the Growth team). The session was foundational training on Atlas architecture, workflow optimization, and the four pathways available to improve pipeline output when results fall short of expectations.

---

## Relevance

**To GrowthX Delivery:**
- The 15-minute editing target is now the primary operational KPI for all MEs. Success here directly enables the jump from 70 to 100+ clients without proportional headcount growth.
- MEs have four concrete levers to improve Atlas pipeline output: (1) refine assignment prompts, (2) fix context artifacts, (3) file engineering tickets with clear before/after examples, or (4) self-serve pipeline YAML edits. Panzarino strongly prefers starting with artifact refinement before escalating to eng.
- The Metronome project demonstrates Atlas's flexibility beyond articles: data scraping, sentiment analysis, and structured JSON output are now viable workflows. MEs should recognize similar opportunities across the portfolio.
- Agents self-correct via rubric-based scoring (up to 10 iterations by default). High iteration counts (9+) signal broken inputs or scope creep; this is a diagnostic signal to refine requirements rather than a feature.

**To GrowthX Business Development:**
- Account health signal: Matthew Panzarino is acting as both engagement manager and director for high-touch clients like Metronome. This hybrid role has proven effective for rescuing struggling accounts (e.g., Metronome's editorial strategy was "a mess" due to client feedback overload; pivoting to a programmatic pricing directory solved the problem).
- Expansion opportunity: Once Danni defines the CMS/output format for community content, Atlas can be extended to build courses, syllabi, and module outlines—expanding GrowthX's serviceable market.
- New tooling discovery: The session revealed a library of Atlas workflows that not all MEs know about. Standardizing workflow visibility (e.g., a shared registry in Slack) could unlock productivity gains.

**To CheckThat:**
- Metronome's pricing directory includes a sentiment analysis component pulling from G2 and Capterra. This workflow could be productized into a CheckThat module for B2B SaaS pricing intelligence.
- Flow Studio (Atlas's debugging backend) reveals agent failure modes with precision (e.g., "Writing Guidelines" score 0.3). This diagnostic transparency is valuable for CheckThat's competitive positioning vs. generic LLM tools.

---

## Overview

- **Primary KPI is Efficiency:** Reduce post-pipeline editing time per deliverable. The goal is a 15-minute benchmark, down from a typical 1–1.5 hours, to enable scaling to 100+ clients without proportional headcount growth.
- **Improve Pipelines Systematically:** Fix poor output by refining inputs (prompts, context artifacts) first. If the issue is systemic, file an ENG ticket. For self-solving, edit the pipeline's YAML code directly.
- **Atlas is a Flexible Platform:** Atlas can generate more than just articles. The Metronome project example showed it building a programmatic pricing directory by scraping data, analyzing sentiment, and delivering structured JSON.
- **Debugging is Transparent:** Use Flow Studio to inspect agent logic and self-correction loops. This reveals why an agent failed (e.g., a "Writing Guidelines" score of 0.3) and how it attempted to fix the issue.

---

## Key Topics

### The Scaling Challenge & ME Role

  - **Goal:** Scale the services side from \~70 to 100+ clients.
  - **Blocker:** Current content operations are not efficient enough.
  - **ME Role:** Improve Atlas pipelines to increase leverage and enable scaling.
      - **Core Task:** Reduce post-pipeline editing time per deliverable.
      - **Benchmark:** Aim for 15 minutes, down from a typical 1–1.5 hours.
      - **Method:** Systematically identify and eliminate manual editing steps.

### Improving Pipeline Output

  - **Four-Step Improvement Process:**
    1.  **Refine Assignment Directions:** Adjust the initial prompt.
    2.  **Refine Context Artifacts:** Fix conflicts or add specificity.
          - **Common Issue:** A new persona's preferences conflict with existing writing guidelines.
    3.  **File an ENG Ticket:** For systemic issues (e.g., agent hallucination).
          - **Requirement:** Provide clear examples of bad vs. desired output.
    4.  **Edit Pipeline YAML:** Self-solve by modifying the human-readable script.
          - **Method:** Use a cloud project (e.g., Claude) to generate the YAML.
          - **Example:** Add a post-processing agent to remove all EM dashes.

### Atlas Capabilities: The Metronome Project

  - **Problem:** The Metronome client's editorial strategy was unsustainable due to excessive feedback from their team.
  - **Solution:** Pivot to a programmatic pricing directory.
      - **Process:** A director created a spec doc → ENG built the pipeline → MEs refined the output.
      - **ME Contributions:**
          - Identified that companies with multiple pricing models (e.g., subscription + API) needed separate pages.
          - Advised removing negative customer sentiment to avoid alienating partners.
          - Refined the "Metronome's Take" section to be less judgmental, making it suitable for a marketing page.
  - **Outcome:** A new, scalable workstream delivering structured JSON for the client's CMS.

### Debugging with Flow Studio

  - Flow Studio is the backend for Atlas, providing transparency into agent execution.
  - **How it Works:**
      - An agent executes a task (e.g., drafting).
      - It self-evaluates against a rubric (e.g., "Writing Guidelines" score 0.3).
      - If it fails, it plans improvements and iterates (e.g., 9 rounds of drafting).
  - **Insight:** Reveals specific failure points (e.g., a word count rule that's too strict) to guide pipeline refinement.

---

## Action Items

**Danni Roseman (GrowthX)**
- Define community content CMS/output format; then draft Atlas pipeline requirements for ENG

**Kalil Magtoto (GrowthX)**
- Run 5 Atlas items; edit in Google Docs (Suggest mode); log edits/time; compile proofreader checklist

**Victor Alagbe (GrowthX)**
- Run 5 Atlas items; edit in Google Docs (Suggest mode); log edits/time; compile proofreader checklist

---

## Transcript
**Kalil Magtoto:** Hey, Victor.

**Kalil Magtoto:** Good afternoon.

**Victor Alagbe:** Hi, man.

**Victor Alagbe:** So.

**Kalil Magtoto:** Oh, wait.

**Victor Alagbe:** How's it going?

**Kalil Magtoto:** I do not hear you right now.

**Victor Alagbe:** Can you hear me now?

**Kalil Magtoto:** Is it better?

**Kalil Magtoto:** Oh, yeah.

**Kalil Magtoto:** That was on me.

**Kalil Magtoto:** How are you doing?

**Victor Alagbe:** I'm good.

**Victor Alagbe:** You?

**Kalil Magtoto:** Oh, man.

**Kalil Magtoto:** This is, uh, my brain is, like, like, filled to the top.

**Kalil Magtoto:** Yeah.

**Victor Alagbe:** Hi, Danni.

**Danni Roseman:** How's it going?

**Danni Roseman:** Hi.

**Danni Roseman:** Yeah, that's what I posted about last night, Kalil.

**Danni Roseman:** I was like, do you ever put yourself getting smarter?

**Kalil Magtoto:** I'm like, my brain is growing in real time right now.

**Kalil Magtoto:** Yeah.

**Kalil Magtoto:** Yeah.

**Kalil Magtoto:** I'm just glad that we have, uh, imagine doing...

**Kalil Magtoto:** This, all of this, well, I guess it wouldn't be possible because the whole premise is AI, but like imagine doing this without the help of AI, like there's no way, so happy we have these tools.

**Victor Alagbe:** It's going to take much longer to ramp up without that assistance.

**Kalil Magtoto:** Yeah, yeah, 100%.

**Danni Roseman:** So what is your, what are you guys' speciality?

**Danni Roseman:** Because we're, we're in different, I'm doing something different here because I'm on the community side.

**Kalil Magtoto:** So what is it like for you?

**Kalil Magtoto:** What are you guys doing?

**Kalil Magtoto:** I don't know yet.

**Kalil Magtoto:** We will, we will see.

**Kalil Magtoto:** I'm hoping that this call will, will give me more of that.

**Kalil Magtoto:** I just filled in the, and I think Victor, you would have gotten this too, the, there's that form that asks what you're good at, what you would prefer.

**Kalil Magtoto:** Uh, prior to here, I was in biopharma, uh, doing digital content, uh, and not just written, it was like everything from.

**Kalil Magtoto:** Video to graphics to whatever they needed.

**Kalil Magtoto:** I was like, sole content guy.

**Kalil Magtoto:** You, Victor?

**Victor Alagbe:** Yeah, so before now, I've mostly worked in Imagine Tech, but recently in the web storage space.

**Victor Alagbe:** But I think for this, you and I, Kalil, are managing editors, and Danni's on the community side.

**Kalil Magtoto:** Managing editor community, yes.

**Victor Alagbe:** So I think we've been assigned a few.

**Victor Alagbe:** If you look at the piece that Andy shared.

**Kalil Magtoto:** Are our names already there?

**Victor Alagbe:** Yeah, so I think Panzer's probably going to provide us with more context around this, I suppose, on this call.

**Victor Alagbe:** But as any of you have been playing with Atlas, I've looked at it, and it's just like, it's like the old idea of cloud projects, now supercharged.

**Danni Roseman:** That's way I think about it.

**Danni Roseman:** I have my Atlas walkthrough on Monday.

**Danni Roseman:** Okay.

**Danni Roseman:** With my buddy.

**Victor Alagbe:** Lucky you.

**Kalil Magtoto:** I don't have a buddy yet.

**Kalil Magtoto:** I'm looking forward to getting one.

**Kalil Magtoto:** I didn't know if I should, like, ask or if it was like, oh, don't preempt what's going to come.

**Kalil Magtoto:** So hopefully this will provide that.

**Danni Roseman:** I think it's because I already had my, I had my one-to-one with my manager already.

**Danni Roseman:** So that's why I think I got my buddy.

**Danni Roseman:** But yeah.

**Danni Roseman:** Yes.

**Danni Roseman:** It's coming.

**Victor Alagbe:** And I also think, Danni, you're working more directly with somebody in the growth team.

**Kalil Magtoto:** I think that will also be a few different things.

**Kalil Magtoto:** Jason, Jason is cool, at least from what I have read on LinkedIn.

**Kalil Magtoto:** So I'd love to also meet him.

**Kalil Magtoto:** Hey, folks.

**Danni Roseman:** Hey, Panzer.

**Matthew Panzarino:** How's it going?

**Victor Alagbe:** Good.

**Kalil Magtoto:** My brain is full.

**Danni Roseman:** Wait, am I supposed to be on this call if I'm not, if I'm not reporting to you, Matthew?

**Matthew Panzarino:** Or should I be on he's

**Matthew Panzarino:** It's about reports, honestly.

**Matthew Panzarino:** mean, sure, you know, it's fine, but it's really more about just getting you acclimated.

**Matthew Panzarino:** I'm here to be sort of an anchor for understanding how to operate a lot of the machinery that we, you know, kind of need to be here.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** So it's less about like, oh, here are your OPRs and more about like, hey, how are you doing?

**Matthew Panzarino:** What's the lay of the land?

**Matthew Panzarino:** Where do you need to be pointed to?

**Matthew Panzarino:** That sort of thing.

**Matthew Panzarino:** And then, of course, going forward as well, you know, you're always welcome to reach out.

**Matthew Panzarino:** So I definitely am in deep with like, you know, the Atlas improvements and the cycles that we go through there.

**Matthew Panzarino:** And then more importantly, like the ground level operations of it.

**Matthew Panzarino:** You know, I've worked very closely with the former CMs, now MEs, and many of the current CMs, and have observed at close range and have operated the pipelines myself to generate client work.

**Matthew Panzarino:** So I know exactly what's going to happen when you press buttons and I can

**Matthew Panzarino:** Probably point you in the right direction to improving those, or if you've discovered a new and novel issue, which happens all the time, I can help you to figure out how to bring the right people into the loop to tackle that, or file the proper ticket, or whatever the case may be.

**Matthew Panzarino:** So, happy to help you with any of that.

**Matthew Panzarino:** But overarching, just love to hear how you're doing.

**Matthew Panzarino:** Say hi, welcome you to the org.

**Matthew Panzarino:** It is a time of change for us, but all of you were interviewed with this understanding in mind, so your skill set was evaluated for the job that we have for you, and for what we need, and all that stuff.

**Matthew Panzarino:** So, don't worry about any of that.

**Matthew Panzarino:** We brought you into this picture knowing exactly where we're headed.

**Matthew Panzarino:** The basic ground truth of the org right now is that we have, you know, like 70 or so clients, and most of them are pretty happy.

**Matthew Panzarino:** The satisfaction rates are fairly high.

**Matthew Panzarino:** Obviously, there's always some issues with client work here and there, but in general, the org.

**Matthew Panzarino:** It's fairly healthy.

**Matthew Panzarino:** You just obviously saw Marcel's business update on the call, so I won't belabor that point, but it's pretty good.

**Matthew Panzarino:** The issue or problem or world that you're coming into is that we know that we need to scale to 100 companies and beyond on the services side.

**Matthew Panzarino:** We will also have a self-service side, a customer-facing side of Atlas, and some of those tools will start to be opened up fairly quickly for them.

**Matthew Panzarino:** Largely in analytics and LLM visibility and stuff like that with the launch of Check That, et cetera.

**Matthew Panzarino:** But for now, we still have a significant amount of work to do to get the content operations to scale.

**Matthew Panzarino:** And a lot of that has to do with operating the tools that we've built correctly and identifying any issues or necessary improvements in those tools.

**Matthew Panzarino:** For brass tax purposes, that's largely Atlas.

**Matthew Panzarino:** You've got ideas, you've got opportunities, you've got concepts coming in from your strategy work or from the client's discussion or from like account managers, kind of him and him back and forth on weekly or biweekly calls.

**Matthew Panzarino:** And you now have some opportunities to create content and you need to kind of use Atlas to do that.

**Matthew Panzarino:** Right now, there are some kinds of content that Atlas is incredibly good at.

**Matthew Panzarino:** And there are other kinds that it's like, wow, this needs some help, right?

**Matthew Panzarino:** We need to figure out how to improve this pipeline's process through one of three major inputs.

**Matthew Panzarino:** Your directions that you give it, your base prompt, your context artifacts.

**Matthew Panzarino:** Basically, are these artifacts well-defined?

**Matthew Panzarino:** Are they clear?

**Matthew Panzarino:** Is the pipeline, aka a series of agents, able to take those bits of context and read them properly and then apply them logically?

**Matthew Panzarino:** Basically, a lot of times what we find.

**Matthew Panzarino:** A

**Matthew Panzarino:** Issues with this conflict between your instructions and one or more of the artifacts, or even internal conflicts between artifacts, or worst case scenario, an internal conflict in the same artifact.

**Matthew Panzarino:** This happens a lot because the clients say a lot of stuff.

**Matthew Panzarino:** We add a lot of stuff to the context artifacts, like the company context or the audience personas.

**Matthew Panzarino:** They're like, we want to go after Persona X.

**Matthew Panzarino:** know, like, okay, cool.

**Matthew Panzarino:** Describe them.

**Matthew Panzarino:** You know, like, let's talk.

**Matthew Panzarino:** We'll do a little discovery.

**Matthew Panzarino:** We'll do some research on our side and we'll come up with something we can add to our artifacts to represent that new Persona.

**Matthew Panzarino:** But something that that Persona prefers or hates, you know, loves or needs may conflict with the current writing guidelines, as an example, right?

**Matthew Panzarino:** The third major artifact.

**Matthew Panzarino:** And so looking for opportunities to improve those generally nets fairly large performance gains in the pipeline.

**Matthew Panzarino:** So you've got an idea, you've run it through, you've seen the results of the pipelines giving you and you're like,

**Matthew Panzarino:** Hey, this is great.

**Matthew Panzarino:** Like, I don't have to do all this research.

**Matthew Panzarino:** That's awesome.

**Matthew Panzarino:** You know, but there's like a lot of stylistic issues or structural issues here that isn't going to take me, say, I don't know, and let's put it in an extreme case, maybe two hours to rework this piece of content to something that I feel confident I can deliver to the client.

**Matthew Panzarino:** Or in your case, Danni, that I feel confident we can ship to the community, right?

**Matthew Panzarino:** And like that kind of output is an opportunity.

**Matthew Panzarino:** It is not an end state and never think of it that way.

**Matthew Panzarino:** There's always some way to improve it and to improve your leverage.

**Matthew Panzarino:** So when the light is darkest is usually when you're like, wow, I have like 20 deliverables, two hours a piece.

**Matthew Panzarino:** You're running the math.

**Matthew Panzarino:** You're like, this is not going to work, right?

**Matthew Panzarino:** This is not compute.

**Matthew Panzarino:** And that's when you're, you kind of like crab walk towards the end of the tunnel, the light, which is refining your inputs, instructions, refining the context artifacts.

**Matthew Panzarino:** And then the third major pillar, which is identifying where the pipeline is.

**Matthew Panzarino:** It's not operating correctly and either bringing in peer review help in the same org.

**Matthew Panzarino:** Maybe it's myself.

**Matthew Panzarino:** Maybe it's a couple of the people that have worked with me to manipulate pipelines like Nana or Yana, who you will meet.

**Matthew Panzarino:** Or it's let's file a ticket.

**Matthew Panzarino:** Let's talk to ENG.

**Matthew Panzarino:** Hey, this is not operating properly.

**Matthew Panzarino:** Or at the very least, I think your job should be I'm going to clearly articulate for you the ways in which this is not delivering.

**Matthew Panzarino:** And then give you some examples.

**Matthew Panzarino:** Examples are not only very important for LLMs, but also very important for engineers who have a lot of similarities sometimes.

**Matthew Panzarino:** But you want to say, hey, this thing is broken in this way or not performing to function in this way.

**Matthew Panzarino:** I'd love for it to improve in way X.

**Matthew Panzarino:** So here's a bad example.

**Matthew Panzarino:** Here's an example of the way it should look.

**Matthew Panzarino:** Maybe here's a couple across a couple of runs so that they know, hey, I've tried this a couple of different ways.

**Matthew Panzarino:** And we file a ticket and that gets into a client operations.

**Matthew Panzarino:** Engineering review cycle, right?

**Matthew Panzarino:** So they can basically say, cool, I can see how this is probably out of your domain.

**Matthew Panzarino:** I'm going to add some reinforcement in the pipeline for you, that kind of thing.

**Matthew Panzarino:** And then there's a sort of fourth opportunity for you.

**Matthew Panzarino:** And that is how it really depends on how much or how much appetite you have for it.

**Matthew Panzarino:** So I'm going to put an asterisk on this that it's not for everybody.

**Matthew Panzarino:** It's not everybody's cup of tea.

**Matthew Panzarino:** But the pipelines themselves are just a set of YAML code, basically human readable script.

**Matthew Panzarino:** It is not like that's not the actual pipeline, actual pipelines code and all that stuff.

**Matthew Panzarino:** But that's the way we call it.

**Matthew Panzarino:** That's the way it is assembled in Atlas.

**Matthew Panzarino:** And I'll show you that in just a second to ground it for you.

**Matthew Panzarino:** But it is possible to just tweak that and try something else, right?

**Matthew Panzarino:** You're not going to break anything at that level.

**Matthew Panzarino:** You know, you're not manipulating any code or changing any code base that the...

**Matthew Panzarino:** You can, if you have the appetite, work to understand the way the pipelines are assembled and add workflows to the pipeline.

**Matthew Panzarino:** So as an example, the standard pipelines consist of a researcher, which researches the topic, a drafter that drafts a first draft of the article, integrating the research, of course, the company context, the writing guidelines, all of those artifacts.

**Matthew Panzarino:** Then it goes through a couple of post processes that include things like linking, either internal linking or external linking, you know, metadata and tagging, that sort of thing.

**Matthew Panzarino:** And then we also usually in the standard agentic pipelines have a proofreader agent, basically, that goes back through and says, hey, can you check up for these things?

**Matthew Panzarino:** Usually a list of, say, 10 items that you have for yourself, right, or anyone you've ever built.

**Matthew Panzarino:** you can say, hey, go look at this article and assess it for these things.

**Matthew Panzarino:** And it is also a general.

**Matthew Panzarino:** Which means that it, to define this for you, since we're going to be talking a lot about these over the time you're here, an agent is simply a non-deterministic workflow.

**Matthew Panzarino:** So a deterministic workflow executes a series of steps and then passes its output along and then it's done, right?

**Matthew Panzarino:** goes to sleep.

**Matthew Panzarino:** An agentic workflow has agents that perform tasks.

**Matthew Panzarino:** They are given a definition of their role.

**Matthew Panzarino:** They are given a task to accomplish.

**Matthew Panzarino:** And then they are given a rubric to evaluate themselves on that job.

**Matthew Panzarino:** And so they are able to check.

**Matthew Panzarino:** They're able to run a pass of their job, go out and do their job.

**Matthew Panzarino:** Then they're able to flip open their spec sheet and go like, did I do this?

**Matthew Panzarino:** Did I do that?

**Matthew Panzarino:** Evaluate me on all these.

**Matthew Panzarino:** It scores itself on all of those points.

**Matthew Panzarino:** Then it goes back and says, hey, I scored poorly on me's.

**Matthew Panzarino:** Let's do a round of iteration.

**Matthew Panzarino:** And it'll do as many rounds as you tell it.

**Matthew Panzarino:** The default, I think, on most of our pipelines is, about three, although it can go up to 10.

**Matthew Panzarino:** You know, if it goes to 10, usually there's something wrong.

**Matthew Panzarino:** Usually it's like artifacts or instructions or scope.

**Matthew Panzarino:** Something is creepy there, right?

**Matthew Panzarino:** However, that agentic process allows it to get things right that a one-shot LLM prompt will not.

**Matthew Panzarino:** You know, you've all done it.

**Matthew Panzarino:** You type something into an LLM and you're like, that is not what I asked for, right?

**Matthew Panzarino:** Well, that's probably because either there's a semantic issue or the LLM just wandered out of context.

**Matthew Panzarino:** This could happen with large prompts or very large contextual documents that you give it, which some of our documents are, right?

**Matthew Panzarino:** Some of them are big.

**Matthew Panzarino:** They're laborious or detailed because the client has all kinds of real hyper-specificity that they're interested in.

**Matthew Panzarino:** So, the agent will score itself and then rerun the tasks until it achieves what it thinks is a high enough score or it runs out of tries, right?

**Matthew Panzarino:** And nine times out of 10, it'll achieve the score.

**Matthew Panzarino:** But, you know, the 10th time, it'll be like, you know, okay, sure, it's great.

**Matthew Panzarino:** And you're like, no, it's not.

**Matthew Panzarino:** see what happened here.

**Matthew Panzarino:** You ran out of tries, right?

**Matthew Panzarino:** And then it's really time to refine, right?

**Matthew Panzarino:** Time to refine those artifacts.

**Matthew Panzarino:** But that proofreader is, there's no reason you can't, like, add more of those.

**Matthew Panzarino:** Like, let's say the client has a very, very hyper-specific, detailed thing.

**Matthew Panzarino:** Like, I want double spaces after every third sentence in this specific context.

**Matthew Panzarino:** Okay, sure, right?

**Matthew Panzarino:** That seems like it's an instruction that should happen at the end, right?

**Matthew Panzarino:** After everything else is done.

**Matthew Panzarino:** So let's add a specific post-processing step to this pipeline that will do that.

**Matthew Panzarino:** Well, by default, our pipelines don't have that because this is a random, like, really hyper-specific client request.

**Matthew Panzarino:** And you need to then integrate that into the pipeline.

**Matthew Panzarino:** So you can add that using, honestly, very simple method, which is have a cloud project that's dedicated to editing pipelines.

**Matthew Panzarino:** You just say, hey, here's an example of our pipeline.

**Matthew Panzarino:** Here's what's good about these pipelines.

**Matthew Panzarino:** Here's what the variables are, et cetera.

**Matthew Panzarino:** Now, please edit this pipeline to do this thing for me.

**Matthew Panzarino:** It's incredibly simple to set this up because the pipelines themselves, the code that you're giving them is not very complex.

**Matthew Panzarino:** You know, you don't have to feed it a code base and all of this stuff.

**Matthew Panzarino:** You just need to say, hey, this is the format that I expect, and here's the name of the variables that I'm working with.

**Matthew Panzarino:** And I can show you how that works at some point.

**Matthew Panzarino:** I just want to show you that this, or talk to you about the fact that it's possible.

**Matthew Panzarino:** We don't have to cover that on this call, right?

**Matthew Panzarino:** So don't panic.

**Matthew Panzarino:** But you can do that.

**Matthew Panzarino:** So if you are achieving something that is so close to what you want, or maybe a little far off from what you want, and you're trying to kind of wrap your head around how to fix it, one of those four methods will typically solve the issue.

**Matthew Panzarino:** So it is either adjusting your assignment directions, a.k.a.

**Matthew Panzarino:** your input or prompt, adjusting the contextual artifacts, filing an engineering ticket, or fiddling around with an experimental pipeline to see if maybe you can self-solve.

**Matthew Panzarino:** you We don't

**Matthew Panzarino:** And that fourth option is not for everyone.

**Matthew Panzarino:** Just want to put that out there.

**Matthew Panzarino:** But if you want to experiment with it, it allows you to get an intimate understanding of Atlas and of our tools and, frankly, do a little bit of skill building of your own.

**Matthew Panzarino:** Why not?

**Matthew Panzarino:** Right?

**Matthew Panzarino:** So it's up to you if you want to tackle that.

**Matthew Panzarino:** If not, the ticket is always there.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** Or a peer review is always there.

**Matthew Panzarino:** I have had plenty of people come to me and like, oh, I wonder if we can do this.

**Matthew Panzarino:** And I'm like, you know what?

**Matthew Panzarino:** We just did that with this other client or with this other pipeline and this other pod.

**Matthew Panzarino:** Let's put one in here for you and see if that helps you.

**Matthew Panzarino:** And they're like, yeah, this is great.

**Matthew Panzarino:** So that's always an option.

**Matthew Panzarino:** know, mind share is always an option.

**Matthew Panzarino:** The Slack channels across the org are largely open.

**Matthew Panzarino:** So you can peek in anywhere you would like.

**Matthew Panzarino:** You're like, I wonder if, you know, oh, they mentioned on the call that they had solved this.

**Matthew Panzarino:** Let me go look, you know, and see what they're talking about with the client.

**Matthew Panzarino:** Or let me go look in their project in Atlas, right?

**Matthew Panzarino:** Because all the clients in Atlas, you can go check out their pipelines and see how they're being run.

**Matthew Panzarino:** And you're like, you know, I noticed you have

**Matthew Panzarino:** This thing in your pipeline, what does this do, right?

**Matthew Panzarino:** Because it's, there's new stuff, you know, all the time coming either out of eng or out of a client request.

**Matthew Panzarino:** And it all gets codified in a library of workflows.

**Matthew Panzarino:** So the engineers know that they're there, but not everybody across the org knows that they're there.

**Matthew Panzarino:** So they're accessible and some people are using them.

**Matthew Panzarino:** Some people aren't, et cetera.

**Matthew Panzarino:** And I would love to say that it'd be easy to standardize that.

**Matthew Panzarino:** Oh, let's make one giant pipeline for everybody and just add toggles.

**Matthew Panzarino:** But, you know, client work is weird.

**Matthew Panzarino:** You know, they always have super specific things that they want and adding stuff that's not necessary is just kind of a recipe for mess.

**Matthew Panzarino:** So I know that was a little bit of a monologue and I'm so sorry, but I just kind of like brain dump you on, on that kind of stuff.

**Matthew Panzarino:** And happy to hear from you and happy to hear about that or talk to me about where you are.

**Kalil Magtoto:** I have a question.

**Kalil Magtoto:** I put it in the chat, but once we're tinkering.

**Kalil Magtoto:** I'm I don't look at chat when I'm on, I try to look at Oh, no, no, no, okay.

**Kalil Magtoto:** It's for me.

**Kalil Magtoto:** But when it comes to tinkering workflows, I know compute costs money.

**Kalil Magtoto:** Are there restraints, risks, anything that we should be aware of before we just start, like, bombing the thing with, like, 10 loops of, you know, agents?

**Matthew Panzarino:** Yeah, no, we, you know, it's an accepted cost, right?

**Matthew Panzarino:** Like, there's a reason we raised venture capital.

**Matthew Panzarino:** We are actually cash flow positive, which is great, most months, including the last several, so that's great.

**Matthew Panzarino:** So we're not running out of money or anything.

**Matthew Panzarino:** But at the same time, we also raised it because the biggest risk is not trying.

**Matthew Panzarino:** Like, if you're sitting there going, like, oh, I don't know if I want to do another run of this pipeline to see if this thing works or not, that's a starvation mindset.

**Matthew Panzarino:** We're not going to win, you know?

**Matthew Panzarino:** And, like, that is the reason that you enter into the VC game at all.

**Matthew Panzarino:** Otherwise, just bootstrap, right?

**Matthew Panzarino:** And watch your costs and tell the client, hey, we can run 10 iterations for you and that's it, right?

**Matthew Panzarino:** Like, build that into your model, etc.

**Matthew Panzarino:** But that's not built into ours.

**Matthew Panzarino:** So by...

**Matthew Panzarino:** By default, just run stuff.

**Matthew Panzarino:** Generally speaking, the workflows that have been defined for your use are going to be constrained on their own to be not enormously expensive.

**Matthew Panzarino:** There are exceptions to that.

**Matthew Panzarino:** There are some products that we've built like our LLM visibility tool called Check That, which costs us a significant amount of money every month.

**Matthew Panzarino:** Because it's running hundreds or even thousands in some cases of prompts, right?

**Matthew Panzarino:** That's separate from Atlas and not something you really have to worry about.

**Matthew Panzarino:** So in Atlas, if you're defining pipelines, if you've got one and you want to run a dozen tests or whatever, great.

**Matthew Panzarino:** Like to give you some scope here, our advice is don't run any more than 500 ideas at a time.

**Matthew Panzarino:** You know what mean?

**Matthew Panzarino:** So feel free to run a dozen.

**Matthew Panzarino:** It's not going to kill anything.

**Matthew Panzarino:** And not only that, it helps you get more shots on goal, right?

**Matthew Panzarino:** Especially when you're learning the pipeline.

**Matthew Panzarino:** I highly suggest that you run like two or three or four of any given thing you're doing at any given time because there are some parts of the pipeline that just take time and are unavoidable.

**Matthew Panzarino:** Research is hard, right?

**Matthew Panzarino:** It's hard for humans.

**Matthew Panzarino:** It's hard for LLMs to do right, right?

**Matthew Panzarino:** So the researcher could take 20 minutes, you know, the agent could take 20, 25 minutes to run.

**Matthew Panzarino:** And, you know, if you want to get your client work out or if you're working on things that you want to experiment with, fire off five or six shots on goal, like different ideas, different topics, different assignment directions, and see what results.

**Matthew Panzarino:** And then you can kind of narrow it down from there.

**Matthew Panzarino:** My advice is change one major variable per run.

**Matthew Panzarino:** You know, this is just scientific.

**Matthew Panzarino:** This is just the scientific method.

**Matthew Panzarino:** But if you change a bunch of variables per run, it's hard to determine, hey, well, wait, why did this work?

**Matthew Panzarino:** Why didn't it work?

**Matthew Panzarino:** So that's my only advice.

**Matthew Panzarino:** But no, feel free to just run stuff.

**Danni Roseman:** I'm interested in seeing some...

**Danni Roseman:** Cases of Atlas that don't involve client work, direct client work, or creating, I mean, articles maybe, but I guess I'm trying to understand how I can make the most use out of it for the type of stuff that I'll be doing for the community.

**Danni Roseman:** And I know that it's valuable, but I haven't been able to play around with it enough to see how it would work for my case.

**Matthew Panzarino:** You said you have not been able to play around with it enough?

**Danni Roseman:** Yeah, have a call with Marisol on Monday to go through it, but I have logged in, and I've seen a lot of labels and a lot of logos, and then I've tried to read through the documentation at least twice, and then I saw code, and then I got a little bit sweaty.

**Matthew Panzarino:** Yeah, okay, so I'll show you a couple of things.

**Matthew Panzarino:** One thing that I would say for you is you're going to very much live in custom land, because you're going to be basically saying, hey, here's what I would like to

**Matthew Panzarino:** Like, I need a, I need to feed it, let me give you an example, I'm just going to riff here, so don't, don't, it's not saying you have to do this, but I would like to feed it a syllabus and get back product X, which is, let's say, a series of modules that are, that have outlines, and then I would like those modules to be fed into something that fleshes out those outlines with editorial content, right?

**Matthew Panzarino:** Like, that pipeline can be built, Atlas can do this, it's not impossible for it to do this.

**Matthew Panzarino:** Then the architecture of it, like actually putting it into a usable format, is really a matter of deciding what your host is.

**Matthew Panzarino:** Like, are we going to build a custom website for this?

**Matthew Panzarino:** If so, and like, talk to N, see if we have the cycles, make the case, okay, cool, we're going to just build a bucket to pour this data into, and the pipeline can format it in the proper way.

**Matthew Panzarino:** Thank

**Matthew Panzarino:** To deliver it into that bucket.

**Matthew Panzarino:** If you're just going to use a pre-existing CMS of some sort that takes a specific type of format or input, let's say you're going to use like a Udemy self-serve type thing, and you're going to like say, hey, I'm going to design my own course, and I'm going to put data into these buckets, you just need to figure out what it wants, and then basically tell the pipeline to deliver the data in that way.

**Matthew Panzarino:** So as an example of this, we have a client here, Metronome, where we are doing a pricing directory for them, and this is not editorial content, it is data scraping and research.

**Matthew Panzarino:** So if you look at these pipelines here, any given run of them allows us to basically feed it a URL, so let's say take a company like Proplexity and feed it their pricing page.

**Matthew Panzarino:** And then this workflow will go through, and it will do research on their pricing and technical.

**Matthew Panzarino:** We specifications of that pricing to generate an editorial section.

**Matthew Panzarino:** Well, I say editorial.

**Matthew Panzarino:** Really just like kind of a summary section about what their pricing model is and that sort of thing.

**Matthew Panzarino:** And then it also goes out and does research on their what kind of pricing that they have, what their pricing history was, etc.

**Matthew Panzarino:** And this is all data, right?

**Matthew Panzarino:** It's looking for data here about what changes they've made to their price over time, etc.

**Matthew Panzarino:** And that research, you can see this took like 34 minutes to go out and do this research.

**Matthew Panzarino:** It went out and grabbed all of the data that it needs to then compile this stuff.

**Matthew Panzarino:** And then we also have a separate section of this page that is customer sentiment.

**Matthew Panzarino:** And so the customer sentiment analysis has to be done.

**Matthew Panzarino:** So like pull customer sentiment from sources like G2 or Capterra or other places.

**Matthew Panzarino:** Then we do a pricing analysis.

**Matthew Panzarino:** So this analysis is like, okay, do we think this pricing...

**Matthew Panzarino:** model is good or bad.

**Matthew Panzarino:** Does it align with things like best practices, et cetera?

**Matthew Panzarino:** Then we go out and scrape some customer sentiment and say, hey, let's structure this in positive or negative feedback, et cetera.

**Matthew Panzarino:** And then here's the result.

**Matthew Panzarino:** Then we process metronome's tape, which we took a body of work from metronome, which is internal documentation on each of these various pricing models, and then parsed it into an instruction set that allows us to assess any given company to metronome's internal standards.

**Matthew Panzarino:** Like how do they think about token-based pricing?

**Matthew Panzarino:** And is this company adhering to best practices when it comes to token-based pricing?

**Matthew Panzarino:** Then we just do some general post-processing to get it into shape.

**Matthew Panzarino:** The output of this is this sheet here, which is really marked down.

**Matthew Panzarino:** And if you look at it, it's like, at a glance, the snapshot of pricing, the overall...

**Matthew Panzarino:** Overview, the key features, the pricing model analysis, the timeline of pricing over time, the customer sentiment, positive and negative, metronomes take, so a little bit of editorial here, right?

**Matthew Panzarino:** We delivered this to them in JSON because that's what they want for ingesting into their CMS.

**Matthew Panzarino:** And then I will show you, here is what it looks like.

**Matthew Panzarino:** Just to grab it for you.

**Matthew Panzarino:** Um.

**Matthew Panzarino:** Boo, boo, boo.

**Matthew Panzarino:** Here we go.

**Matthew Panzarino:** Sorry.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** So this is a mock that I built for them when we were doing, we were setting this project up.

**Matthew Panzarino:** This is just easiest.

**Matthew Panzarino:** They have a Figma now that shows their actual work on it, but they're basically just building off of the mock we gave them.

**Matthew Panzarino:** So this is how that manifests, right?

**Matthew Panzarino:** So this is, I just threw this together in Lovable, but they're obviously building it on their own site with their eng team.

**Matthew Panzarino:** And if you go into any individual page, you can see that this is all of the data that the pipeline gathered and fact-checked and collated into the proper formats.

**Matthew Panzarino:** And now it gets delivered on this page, just like this, right?

**Matthew Panzarino:** So this is just an example of content that is not editorial.

**Matthew Panzarino:** It's not write a blog post.

**Matthew Panzarino:** It is programmatic in nature and allows us to run a pipeline on any given, they could give us a company today and I could have this data for them, you know, within an hour, right?

**Matthew Panzarino:** Or a new page, let's call it within an hour.

**Matthew Panzarino:** That ability comes from the flexibility of Atlas's workflows.

**Matthew Panzarino:** Like, they could do a lot of things.

**Matthew Panzarino:** So there's no reason that it couldn't do things like building courses, as an example.

**Matthew Panzarino:** So does that make sense?

**Matthew Panzarino:** Does that give you, like, an example or a view of other things it can do?

**Danni Roseman:** It does.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** And the building of that pipeline and, like, how do I instruct it to do this thing, all of that, you're not responsible for that.

**Matthew Panzarino:** Like, you're responsible for writing this back, right?

**Matthew Panzarino:** For saying, here are the things that I needed to do in detail.

**Matthew Panzarino:** Here's the clear articulation of what I would like to happen.

**Matthew Panzarino:** And here, please do this for me.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** And that's what the ENG team can do for you.

**Kalil Magtoto:** So I have a question about the setup of this.

**Kalil Magtoto:** So, you know, first principles, how did we get to the workflow?

**Kalil Magtoto:** Pricing ability users, pricing evolution, just using this as the example, who did that?

**Kalil Magtoto:** And then I assume...

**Kalil Magtoto:** assume an ME would go in.

**Kalil Magtoto:** Okay.

**Kalil Magtoto:** Yeah, cool.

**Kalil Magtoto:** I assume an ME would go in and change the input and then make tweaks and modify that area.

**Kalil Magtoto:** Where did the direction come from?

**Kalil Magtoto:** How is it like working with the clients?

**Kalil Magtoto:** Okay.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Got it.

**Matthew Panzarino:** So for Metronome, as an example, I am acting as a sort of combination engagement manager and director, right?

**Matthew Panzarino:** So like the director might come along at the beginning of this process to help define this whole new thing for Metronome.

**Matthew Panzarino:** I did that work because we needed to rescue this client, just to be frank.

**Matthew Panzarino:** Like we had an editorial strategy for them, which was really more to do with them than us.

**Matthew Panzarino:** And we had a nice call with our point of contact over there recently where it was just like, hey, you know that the editorial part of this was a mess because of you, right?

**Matthew Panzarino:** And they're like, yeah, sorry, right?

**Matthew Panzarino:** Our marketing team is a mess.

**Matthew Panzarino:** And we just kind of like got it sorted out.

**Matthew Panzarino:** But basically their editorial strategy.

**Matthew Panzarino:** Coming out of our sprint process, which usually lasts about eight to 12 weeks, was very, it was a very short runway.

**Matthew Panzarino:** They were launching a white paper and we were producing content around that white paper for them, just editorial content, blog posts, you know, to go alongside the white paper to market the concepts and ideas contained within.

**Matthew Panzarino:** That's fine.

**Matthew Panzarino:** Valid use of, you know, agency work and all that.

**Matthew Panzarino:** But it really wasn't a long-term strategy of any sort.

**Matthew Panzarino:** You know, it's just like, okay, we launched the white paper, now what, right?

**Matthew Panzarino:** So as I was trying to prepare for our next tranche of work with them, like to keep them engaged and make sure that they saw our value and we had new work to do, I basically was like, hey, you know, what would be most valuable to you?

**Matthew Panzarino:** And they had this idea that the seed of this came from their side and they were like, oh, we were thinking, because you told us you could do directories and indexes, we were thinking of doing like a directory of pricing models.

**Matthew Panzarino:** And I said, so you know more, let me go noodle on this.

**Matthew Panzarino:** So I went and basically created the spec for this, which is basically a PRD, you know, in developer terms.

**Matthew Panzarino:** You're creating a spec doc for this kind of product.

**Matthew Panzarino:** I can actually show you that document.

**Matthew Panzarino:** It's not all that readable or instantly parsable.

**Matthew Panzarino:** It's readable, hopefully, but it's not all that instantly parsable because it's pretty deep.

**Matthew Panzarino:** But let me go here.

**Matthew Panzarino:** And this is all in the client space for Metronome, the way, right?

**Matthew Panzarino:** So like any of the documentation would just live in the client space in Notion.

**Matthew Panzarino:** Let me do that.

**Matthew Panzarino:** So this programmatic SEO proposal is basically what I sent them.

**Matthew Panzarino:** And you can see it was last updated in August.

**Matthew Panzarino:** I don't remember when I initially sent it to them.

**Matthew Panzarino:** But it's like objective, create a programmatic directory.

**Matthew Panzarino:** Here's your goals, here's your opportunity size.

**Matthew Panzarino:** This is just a content strategy, right?

**Matthew Panzarino:** Same stuff you would do for anybody creating any content strategy.

**Matthew Panzarino:** You're like, hey, here's the size of opportunity, all this.

**Matthew Panzarino:** This is director-level work, right?

**Matthew Panzarino:** This is what the directors are supposed to be doing, you know, talking to the client, parsing and understanding their needs, developing a content strategy, and then pitching it to them so that we can keep them.

**Matthew Panzarino:** Now, theoretically, a lot of this work is done in the sprint process.

**Matthew Panzarino:** But when we need to renegotiate that account strategy or change it in some major way, let's say their goals change.

**Matthew Panzarino:** Hey, we're pivoting the company.

**Matthew Panzarino:** Okay, we need to pivot your content plan in too, right?

**Matthew Panzarino:** Or we're launching a major new product.

**Matthew Panzarino:** Great, your content plan should reflect that major new product, right?

**Matthew Panzarino:** So anytime you're instituting a big change, you'll want to do this exercise, or the director will.

**Matthew Panzarino:** And basically do the analysis.

**Matthew Panzarino:** Then you can see the page structure here.

**Matthew Panzarino:** This is the structure, breadcrumbs, the H1, the at-a-glance cards.

**Matthew Panzarino:** You can see that this is basically in text form, exactly what that page looks like.

**Matthew Panzarino:** The analysis, the customer sentiment, the impact, the competitive context.

**Matthew Panzarino:** We trimmed some of these sections just from feedback from them, and we were like, you know, do you want this, do you not want this, that sort of thing.

**Matthew Panzarino:** But that's basically it.

**Matthew Panzarino:** Then we've got the structure here, the slugs, the breadcrumbs, that sort of thing.

**Matthew Panzarino:** Then, I won't belabor the point, but data requirements, this is how we basically say, what kind of data do we need for each of these things?

**Matthew Panzarino:** The SEO strategy that goes along with it.

**Matthew Panzarino:** Engineering requirements, okay, we need to do these things.

**Matthew Panzarino:** We're doing quarterly cadence updates.

**Matthew Panzarino:** What do we need from our side?

**Matthew Panzarino:** What do we need from their side?

**Matthew Panzarino:** Who's responsible for what?

**Matthew Panzarino:** Timelines and then investments, that sort of thing, right?

**Matthew Panzarino:** So this spec doc was what I used to kind of put our thoughts in order and pitch it to them.

**Matthew Panzarino:** And in the pitch, instead of just giving them this doc, I just made that thing lovable.

**Matthew Panzarino:** So I fed Lovable this spec doc, and I said, could you just build one of these for me, please?

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** And of course, I had a little back and forth with it.

**Matthew Panzarino:** took me an hour and a half or so to build that thing Lovable.

**Matthew Panzarino:** Most of that time was just finding their colors team off their website, inspecting element, grabbing their colors to make sure that it was presented properly.

**Matthew Panzarino:** And then I was able to walk into that meeting with, of course, this document so they could see that we've done the work, but then also something for them to look at and say like, oh, I see what you mean, a pricing index.

**Matthew Panzarino:** This looks great.

**Matthew Panzarino:** Oh, it's even in our colors.

**Matthew Panzarino:** Look, it has our logo.

**Matthew Panzarino:** That kind of stuff is more about client relationships than it is about actually building a product because we're not using that Lovable thing to actually ship.

**Matthew Panzarino:** You know, they're building it on their infrastructure, but it doesn't mean we couldn't, right?

**Matthew Panzarino:** It just depends on the scale and what we've pitched them and frankly, how much they pay us.

**Matthew Panzarino:** Because like engineering and design work is extra, right?

**Matthew Panzarino:** Like that is not standard in the contract.

**Matthew Panzarino:** So this kind of.

**Matthew Panzarino:** The process here would typically be an entire new work stream.

**Matthew Panzarino:** So this is something we would sell them for like 10, 15K a month, right?

**Matthew Panzarino:** But in this case, it replaced our existing 10 to 15K a month work stream for them, where we were like, hey, we don't have a long tail editorial strategy beyond this white paper thing that you've given us.

**Matthew Panzarino:** I have an idea.

**Matthew Panzarino:** And we pitched them this.

**Matthew Panzarino:** And there was two reasons for this.

**Matthew Panzarino:** One of those was, hey, we need something new to keep them engaged.

**Matthew Panzarino:** The other one was their marketing org, which now has shed a lot of these people.

**Matthew Panzarino:** But like there were like six people up in our business every time we shipped an article, like really closely reading and like punctuating and like changing things around that were frankly unnecessary.

**Matthew Panzarino:** It just seemed like a lot of people justifying their job, you know?

**Matthew Panzarino:** I'm sure you've all seen it where you're like, who are all these people commenting on this document?

**Matthew Panzarino:** And what do they have to do with anything, right?

**Matthew Panzarino:** And you can tell that most of them don't have any real editorial experience.

**Matthew Panzarino:** Right.

**Matthew Panzarino:** So they're changing things and you're like, okay, sure I can, but like semantically this makes no difference or whatever.

**Matthew Panzarino:** So there was a lot of that business.

**Matthew Panzarino:** So this allows us to sidestep a lot of that because it's largely data.

**Matthew Panzarino:** So it's just like, hey, okay, I see where this is headed.

**Matthew Panzarino:** I've got a new idea for you.

**Matthew Panzarino:** We can deliver this at scale.

**Matthew Panzarino:** So we can start off with 20 pages on day one and then ship 10 pages for you a week for, you know, six months and observe and, you know, see what the opportunities are here to expand.

**Matthew Panzarino:** then in addition, this can become a hub for editorial content so that we can ease ourselves back into editorial content where we're like, I'm so glad we got the first hundred companies live for you.

**Matthew Panzarino:** This project has been a success.

**Matthew Panzarino:** It's ranking.

**Matthew Panzarino:** It's indexed.

**Matthew Panzarino:** We've even seen some LLM citations on these pages.

**Matthew Panzarino:** This is great.

**Matthew Panzarino:** Now I have a new idea for you.

**Matthew Panzarino:** And that idea is let's take each one of these pages and start to build editorial content off of them, right?

**Matthew Panzarino:** Take each one as a hub and spoke some editorial content.

**Matthew Panzarino:** Which can be lead gen for the product itself, and authority building, and of course, Google loves it, et cetera, right?

**Matthew Panzarino:** So anyhow, that's walking you through a product that we built for, and a work stream that we built for a client that is not, hey, publish some blog posts on our blog, you know?

**Kalil Magtoto:** Where do we come in and help you?

**Kalil Magtoto:** Because you did the hard stuff.

**Kalil Magtoto:** Where do we slot in?

**Matthew Panzarino:** Yeah, so in this case, the, I don't know if it's the hard stuff.

**Matthew Panzarino:** It's a lot of talking is what it is, usually.

**Matthew Panzarino:** A lot of selling.

**Matthew Panzarino:** But the ME layer comes in when it's like, hey, we filed a ticket, and I filed a ticket basically, not with this, with an internal facing version of this that was like more of a brass tacks PRD of like, hey, this is what the pipeline needs to do.

**Matthew Panzarino:** Here's all the data it needs to gather.

**Matthew Panzarino:** Here's what it needs to spit out the other end, right?

**Matthew Panzarino:** Eng went and built that, and then shipped that pipe.

**Matthew Panzarino:** So it appeared in the metronome workspace.

**Matthew Panzarino:** I'm like, great.

**Matthew Panzarino:** Now I'm a hands-on kind of person.

**Matthew Panzarino:** So I'm like, cool.

**Matthew Panzarino:** I'm going to go run some stuff.

**Matthew Panzarino:** So I started running some stuff.

**Matthew Panzarino:** But also I engaged Jana, who was acting as the ME for that account in our pod.

**Matthew Panzarino:** And I said, Jana, we've got our pipeline finally, right?

**Matthew Panzarino:** Let's go take a look at it.

**Matthew Panzarino:** Let's start running some stuff.

**Matthew Panzarino:** And she's like, great.

**Matthew Panzarino:** I'll start piping some stuff through.

**Matthew Panzarino:** She notices a handful of things right away.

**Matthew Panzarino:** She's making tweaks either to the inputs or outputs or making, you know, recording them for a ticket to say, hey, let's get a rev on this thing.

**Matthew Panzarino:** And then, of course, reviewing the data afterwards and saying, hey, here, I see some issues here.

**Matthew Panzarino:** Like one thing she noticed right away as an example was that some of the companies have wildly different pricing models.

**Matthew Panzarino:** And how are we going to represent that?

**Matthew Panzarino:** So she fed that to me and I fed that to the client, right?

**Matthew Panzarino:** She's like, hey, I'm flagging for you.

**Matthew Panzarino:** I just ran Perplexity and Perplexity has their $20 a month subscription.

**Matthew Panzarino:** But they also have API pricing, right?

**Matthew Panzarino:** So yeah, they have

**Matthew Panzarino:** All usage-based pricing and they have a subscription model.

**Matthew Panzarino:** So are we going to represent both of those in this index?

**Matthew Panzarino:** And I said, good question.

**Matthew Panzarino:** I don't know, right?

**Matthew Panzarino:** Should we shove them on the same page or should we create separate pages?

**Matthew Panzarino:** So we proposed that to them and they're like, oh, no, separate pages is the way.

**Matthew Panzarino:** I'm like, great, sounds good.

**Matthew Panzarino:** So I said, okay, Jana, let's run one for the sub and one for the usage-based, right?

**Matthew Panzarino:** So we did that.

**Matthew Panzarino:** So that is something she discovered and we ran.

**Matthew Panzarino:** Some other things that she discovered in that.

**Matthew Panzarino:** And you can also get it straight from the horse's mouth, too, and feel free to reach out to her.

**Matthew Panzarino:** She's very read in on Atlas and has done a great job of kind of like building and manipulating pipelines, too.

**Matthew Panzarino:** But another thing we noticed was that the customer sentiments were a little bit negative.

**Matthew Panzarino:** And it's like, that's not surprising.

**Matthew Panzarino:** People love to complain.

**Matthew Panzarino:** very few people, like, you know, 10 to 1.

**Matthew Panzarino:** Anybody who's been in CS knows this, right?

**Matthew Panzarino:** It's 10 to 1 complaints versus compliments, if not 100 to 1.

**Matthew Panzarino:** So we...

**Matthew Panzarino:** We were like, okay, there's a philosophical decision to be made here.

**Matthew Panzarino:** Do we even want negative customer sentiment on these pages?

**Matthew Panzarino:** And instead, maybe it's just customer highlights.

**Matthew Panzarino:** Because they had initially specced out highlights and lowlights.

**Matthew Panzarino:** And we're like, maybe not, right?

**Matthew Panzarino:** Maybe you don't want honest truth on these.

**Matthew Panzarino:** Because these people, some of them are their partners, right?

**Matthew Panzarino:** Some of them, because Metronova is a pricing engine, right?

**Matthew Panzarino:** Or a usage-based pricing platform.

**Matthew Panzarino:** So it allows people to spin up usage-based pricing models by integrating Metronome.

**Matthew Panzarino:** Do you really want to piss off potential clients or existing clients?

**Matthew Panzarino:** Not so much, right?

**Matthew Panzarino:** And it is marketing at any base.

**Matthew Panzarino:** This isn't journalism, right?

**Matthew Panzarino:** So it lied, the negative stuff.

**Matthew Panzarino:** Cool, no problem.

**Matthew Panzarino:** Then the Metronome's take, the first pass we had at it, was too honest.

**Matthew Panzarino:** It took their internal documentation and judged these companies based off of what Metronome knows to be true.

**Matthew Panzarino:** Because they have a lot of data on how these models work.

**Matthew Panzarino:** And it was like, this company is missing a huge opportunity because they have a pricing gap.

**Matthew Panzarino:** There's an umbrella

**Matthew Panzarino:** Is that useful analysis to someone?

**Matthew Panzarino:** Sure.

**Matthew Panzarino:** Is it useful on a marketing page?

**Matthew Panzarino:** Probably not, right?

**Matthew Panzarino:** So like we've discovered, we were able to use their internal body of data to discover things about these pricing models that you know, they're probably, they're biz people should already be aware of, but aren't necessarily something that you want on this page.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** That's great.

**Matthew Panzarino:** Let's tweak the instruction set.

**Matthew Panzarino:** We gave that workflow to say, hey, here's how we want you to represent these companies.

**Matthew Panzarino:** You know, let's tweak the sentiment, et cetera.

**Matthew Panzarino:** So all of that tweak, all of those tweaks were done by her.

**Matthew Panzarino:** I did not do any of this, right?

**Matthew Panzarino:** I was like, I gave her my thoughts.

**Matthew Panzarino:** And then she's like, cool, I'm going to go tweak the instructions that we gave the pipeline.

**Matthew Panzarino:** And then she tweaks the prompt or tweaks the context.

**Matthew Panzarino:** And then it takes that and we see a new run of it.

**Matthew Panzarino:** And we're like, oh, this is great.

**Matthew Panzarino:** This is much better, right?

**Matthew Panzarino:** And then we give it to metronome and metronome is like, oh, actually, this is much better.

**Matthew Panzarino:** I like this.

**Matthew Panzarino:** You know, this tone is less acerbic or whatever.

**Matthew Panzarino:** And then they like it.

**Matthew Panzarino:** That's the client review cycle.

**Matthew Panzarino:** So, that's the work, right?

**Matthew Panzarino:** And then, obviously, part of that is just delivery.

**Matthew Panzarino:** So, in this case, we delivered JSON files in Airtable for them.

**Matthew Panzarino:** So, in Airtable, they can go see all their deliverables, all their pages.

**Matthew Panzarino:** They can see the JSON file.

**Matthew Panzarino:** The rest of it is human-readable for the marketing people over there.

**Matthew Panzarino:** But then the JSON file is important to their front-end team because they're, like, grabbing them, throwing them in there, formatting them on the page, all that stuff.

**Matthew Panzarino:** Does answer that question?

**Matthew Panzarino:** Oh, and then, really quickly, I wanted to show you, I have to go in just a second, but, I'm going to show you this just so you can get a view.

**Matthew Panzarino:** And I'll show you something that's relatively standard so it doesn't have too many, like, highly custom weird wrinkles.

**Matthew Panzarino:** But I just want to show you what else.

**Matthew Panzarino:** So, this is obviously a client workspace.

**Matthew Panzarino:** This is placeholder.

**Matthew Panzarino:** So, these metrics aren't live yet.

**Matthew Panzarino:** This is in active development, though.

**Matthew Panzarino:** They're ducks feet on this page.

**Matthew Panzarino:** But the workflow spaces down here, you can see there's a couple down here from Monograph, but we really use editorial here.

**Matthew Panzarino:** Each of these is a pipeline, but they're not all in use.

**Matthew Panzarino:** Some of these are experimental.

**Matthew Panzarino:** And some of them are deprecated.

**Matthew Panzarino:** Right now, we don't have an easy, we can archive them.

**Matthew Panzarino:** So, like, we've archived several, but we don't have an easy way to, like, prioritize or mark, like, hey, this is the one that's active and this is not.

**Matthew Panzarino:** I've talked to Andrew about this.

**Matthew Panzarino:** We'll figure it out.

**Matthew Panzarino:** But these are various things that we have messed around with.

**Matthew Panzarino:** And you can see that we've got some playground ones in here where we're just messing around.

**Matthew Panzarino:** But then each of these does a different thing or is kind of, like, organized in a different way.

**Matthew Panzarino:** talking just you.

**Matthew Panzarino:** But just to give you a general idea, I'll pick one.

**Matthew Panzarino:** let's call it, let's do, let's do, okay, this is a little bit more complicated than a standard one, but not much.

**Matthew Panzarino:** We'll do this one.

**Matthew Panzarino:** So this is like an article generator, obviously.

**Matthew Panzarino:** These names up here are just the actual raw workflow names.

**Matthew Panzarino:** I've been lobbying to get these changed forever.

**Matthew Panzarino:** We'll figure it out one day.

**Matthew Panzarino:** But these are just the actual names of the workflow that the engineers have defined.

**Matthew Panzarino:** If you click into any run, you'll see what they actually do here.

**Matthew Panzarino:** Like this is what they're actually accomplishing, these bold names here.

**Matthew Panzarino:** So this workflow researches, drafts, adds internal links, adds source links to the claims, does case study integration for us, because we have an artifact defined with a bunch of case studies that they can reference.

**Matthew Panzarino:** So this is...

**Matthew Panzarino:** This workflow, basically the instructions are, go check out the set stories that are mentioned in the text.

**Matthew Panzarino:** If there is less than one mentioned, integrate case studies naturally into the article.

**Matthew Panzarino:** In other words, throw a case study in here.

**Matthew Panzarino:** They gave us like 50.

**Matthew Panzarino:** And so I'm sure one of them is applicable.

**Matthew Panzarino:** So please weave that in here somewhere.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** And then we gave it some rules about doing it, right?

**Matthew Panzarino:** Like just right here.

**Matthew Panzarino:** And this is not all that hard to generate because Claude's pretty good at this.

**Matthew Panzarino:** You say, hey, I have some case studies.

**Matthew Panzarino:** I need to tell this HF Tech workflow to do these things.

**Matthew Panzarino:** Can you tell me how to do that?

**Matthew Panzarino:** Right?

**Matthew Panzarino:** And it says, sure, yeah.

**Matthew Panzarino:** Tell it to do this.

**Matthew Panzarino:** And then you refine it from there, right?

**Matthew Panzarino:** Critical thinking comes in where you run it and you're like, uh-oh, no.

**Matthew Panzarino:** And then you need to tweak the instructions.

**Matthew Panzarino:** But you can start off there.

**Matthew Panzarino:** But this case study integration, just to give you a view of where that information comes from, it is, in our context artifacts, we have defined a, this is an aged code.

**Matthew Panzarino:** Client, the way, this client's been with us for months.

**Matthew Panzarino:** So there's a lot more artifacts in here than you will see in like new clients.

**Matthew Panzarino:** But I'm pretty sure it is, I'm pretty sure, oh, it's this one right here.

**Matthew Panzarino:** So it's Death Stories, right?

**Matthew Panzarino:** So this is just basically a cleaned up version of a database that they gave us where it's like, okay, what's the company?

**Matthew Panzarino:** Here's the, we classified them by size of firm because many of the articles relate to like, you know, large firms, medium firms.

**Matthew Panzarino:** Small firms, sort of thing.

**Matthew Panzarino:** A company called Woodhull, they have 25 people.

**Matthew Panzarino:** They previously used BQE Core.

**Matthew Panzarino:** When they switched to Monograph, they had 66, apparently, can't say it, 66% time saved on admin, right?

**Matthew Panzarino:** So it's like, hey, Woodhull, when they switched, they saved 66% of the time on admin.

**Matthew Panzarino:** That gets integrated into the article, right?

**Matthew Panzarino:** This is just basically stats for it to pull from that don't exist or are harder to find on admin.

**Matthew Panzarino:** So

**Matthew Panzarino:** Just on the web, right?

**Matthew Panzarino:** The researcher may not find these or may find other stuff that is not germane.

**Matthew Panzarino:** And we can tell it, no, no, no, I have a great source for you.

**Matthew Panzarino:** Go pull from here, right?

**Matthew Panzarino:** And that's why that workflow exists inside this pipeline.

**Matthew Panzarino:** So this case study integration is an example, prime example, of one where we were like, we have these case studies for Monograph, and it knows it can link to them because they exist on Monograph's site, but we want them narratively integrated and we want a way for it to sort of point at those.

**Matthew Panzarino:** So I told Vianna, I said, hey, why don't you add a workflow to this pipeline that is just a post-processor that goes through it and looks for opportunities to add these, define an artifact, put these in there.

**Matthew Panzarino:** And she's like, yeah, it makes sense.

**Matthew Panzarino:** So she went and did that work to integrate these things.

**Matthew Panzarino:** And here's how she did it, just to ground this for you.

**Matthew Panzarino:** If you hit the edit button up here in any given pipeline, this is the pipeline itself.

**Matthew Panzarino:** Don't be intimidated.

**Matthew Panzarino:** This is literally largely plain English text.

**Matthew Panzarino:** It's not anything super complex.

**Matthew Panzarino:** It's just at the top, it defines the inputs.

**Matthew Panzarino:** Okay, what do we want as input?

**Matthew Panzarino:** Including a default instruction set, which is right here.

**Matthew Panzarino:** See this?

**Matthew Panzarino:** Write me an article for these people that's this long.

**Matthew Panzarino:** That's it.

**Matthew Panzarino:** This is Jay.

**Matthew Panzarino:** Just, you know, standard stuff.

**Matthew Panzarino:** Like, here's some formatting things and here's a quality checklist.

**Matthew Panzarino:** This is very short, very, very brief.

**Matthew Panzarino:** And this outputs articles that are really good.

**Matthew Panzarino:** And this is not much.

**Matthew Panzarino:** This is not a big prompt, right?

**Matthew Panzarino:** Because the agent does a pretty good job at this.

**Matthew Panzarino:** But that, that pipeline, this YAML code here, is it takes that input, it defines output, and then it has steps.

**Matthew Panzarino:** And you'll see that these map to the exact steps you see.

**Matthew Panzarino:** So research, draft, internal links, then each one of them has just a little bit of inputs and outputs defined here.

**Matthew Panzarino:** This process of creating these things can be done by ing, so you can file a ticket and have them improve that, have them tweak that for you, et cetera, but you can also play with it.

**Matthew Panzarino:** And one of the best ways to do that is by just creating yourself a little cloud project that you can use to manipulate pipelines.

**Matthew Panzarino:** Let me, I have like six different cloud accounts, so I need to like log into the right one.

**Matthew Panzarino:** I'll show you this.

**Matthew Panzarino:** And you can, um, look at, um, ah, here we go.

**Matthew Panzarino:** You can look at our pod account.

**Matthew Panzarino:** each pod has its own cloud account.

**Matthew Panzarino:** So you'll be getting access to a full cloud pro account.

**Matthew Panzarino:** It'll just be wherever you land in the org.

**Matthew Panzarino:** We just split them up that way because of usage.

**Matthew Panzarino:** We have like a dozen of them.

**Matthew Panzarino:** But you will get access to your own.

**Matthew Panzarino:** But you can absolutely just go look in our pod.

**Matthew Panzarino:** And our pod is pod F.

**Matthew Panzarino:** When I say ours, I mine, Nana's, and Yana's.

**Matthew Panzarino:** Because we do a lot of experimental work.

**Matthew Panzarino:** But this is our pod F account.

**Matthew Panzarino:** And if you look at our projects, we've built a bunch of projects in here that help us with different tasks.

**Matthew Panzarino:** And one of them is a pipeline builder.

**Matthew Panzarino:** So this pipeline builder, as context, we've offered it the benchmark pipeline example.

**Matthew Panzarino:** Like here's the example of like a pipeline that we're working with.

**Matthew Panzarino:** Here's the generic one.

**Matthew Panzarino:** This is the standard template that comes out of the Atlas when you just fire off.

**Matthew Panzarino:** And then here's some documentation on what these do, what is the behavior of each of these workflows, right?

**Matthew Panzarino:** And then I can literally go in here and ask it, hey, here's a pipeline for u.com.

**Matthew Panzarino:** I'd like to insert new assignment directions.

**Matthew Panzarino:** The assignment directions are as follows, blah, blah, blah, right?

**Matthew Panzarino:** And it's like, hey, oh, by the way, and I was giving it an old pipeline to work with, and it said, I found a monograph in here, and you're like, you're right, I missed a monograph reference, right?

**Matthew Panzarino:** So it fixed that for me, and then here's the modified assignment directions, and I was like, that's great, but, like, you're the best.

**Matthew Panzarino:** However, I would like the complete pipeline to paste, thank you, and then it gave me the entire pipeline.

**Matthew Panzarino:** I can literally just copy this, and then go paste it into Atlas, and then save the pipeline.

**Matthew Panzarino:** Done.

**Matthew Panzarino:** New pipeline, right?

**Matthew Panzarino:** So, like, it's not very complex, and Claude is extremely good at it, because it's basically rudimentary code.

**Matthew Panzarino:** It's script, you know, and it's done that way on purpose.

**Matthew Panzarino:** Boom, because the Edge team, in order to deploy...

**Matthew Panzarino:** New stuff, new pipelines in the front end.

**Matthew Panzarino:** They want to be able to rapidly deploy and rapidly change things.

**Matthew Panzarino:** If a pipeline is not working, or excuse me, if a workflow, which is a component of the pipeline, is not working at some fundamental level, that's engine work.

**Matthew Panzarino:** You know, they're going off, they're opening their code base, seeing what's going on, making tweaks, et cetera.

**Matthew Panzarino:** But remember, anytime they tweak any of those workflows, that affects every workflow across the entire org.

**Matthew Panzarino:** So this has to be some sort of systemic issue.

**Matthew Panzarino:** Let's say the researcher is having a real tough time hallucinating, you know, statistics, and it needs some reinforcement or whatever.

**Matthew Panzarino:** And I'm like, hey, Daniel, I've flagged three accounts so far.

**Matthew Panzarino:** They're having a heck of a time with hallucinations, et cetera.

**Matthew Panzarino:** And he's like, okay, we'll go look at the researcher and we'll do a pass.

**Matthew Panzarino:** You know, and like, that's basically the way that that goes.

**Matthew Panzarino:** But if it's something where the workflows are just not giving you the desired output, it's a lot of times useful to just either.

**Matthew Panzarino:** Tweet the inputs, tweak the pipeline itself in YAML, you know, to add a different post-processor, et cetera, or tweak the context artifacts.

**Matthew Panzarino:** And yes, Yana did this.

**Matthew Panzarino:** I didn't do this.

**Matthew Panzarino:** So to add that to the monograph pipeline, I didn't do that.

**Matthew Panzarino:** There's no need for me to do it because once we've established the project and, you know, the first time, I mean, I got about a 90-minute call somewhere where, like, Yana and Nana and I walked through, like, in laborious detail, each step of a pipeline of a client where it was, like, why is it doing this?

**Matthew Panzarino:** What's going on?

**Matthew Panzarino:** What's happening here, et cetera, to debug so that we could write a ticket.

**Matthew Panzarino:** It's not necessary to do that.

**Matthew Panzarino:** I do that, and I drag them along with me because it's important that I understand, you that I'm able to articulate those things to the Inge team.

**Matthew Panzarino:** But your task is much more like what I just showed you in Claude.

**Matthew Panzarino:** If so, if you choose to use it, you do not have to do that right off the bat, and especially early on.

**Matthew Panzarino:** But I want to show you.

**Matthew Panzarino:** What's possible?

**Matthew Panzarino:** Because it's not like, you're not working in some black box dead end where you're like, oh, I guess as soon as any team fixes this, that my life will be easier.

**Matthew Panzarino:** Well, no, you could probably make your life easier now, you know, like in some ways.

**Matthew Panzarino:** So I think it's important to see that.

**Matthew Panzarino:** And then one last thing, and we have like five minutes, but one last thing I want to show you is this pipeline, the same pipeline.

**Matthew Panzarino:** I just want to show you this.

**Matthew Panzarino:** It goes through these steps, right?

**Matthew Panzarino:** And then it has an output.

**Matthew Panzarino:** If you're trying to debug what's happening, there are two major ways to do that.

**Matthew Panzarino:** And by debug, I mean like, it did this, and I don't want it to do this.

**Matthew Panzarino:** When did it do this, right?

**Matthew Panzarino:** This is the final output here.

**Matthew Panzarino:** This is what I'm looking at.

**Matthew Panzarino:** I would love for it not to put this colon in here.

**Matthew Panzarino:** I told it not to use colons.

**Matthew Panzarino:** Like, where did it do this, right?

**Matthew Panzarino:** Not this example, but you get the example, or you get the idea.

**Matthew Panzarino:** If you want to debug any of these, there are two major ways to do that.

**Matthew Panzarino:** it.

**Matthew Panzarino:** Let's do do do do Let's Let's

**Matthew Panzarino:** Let's say we want to debug the case study integration step, this step specifically.

**Matthew Panzarino:** I can go look at inputs and see what inputs we're given, the rules, the content, the context, and instructions, and you can see the iterations here, et cetera.

**Matthew Panzarino:** This is everything it is given to do its job, the process, right?

**Matthew Panzarino:** The context is whatever lists, guidelines, or artifacts, et cetera, that you have.

**Matthew Panzarino:** Of course, for this step, the context is that artifact I showed you earlier, right?

**Matthew Panzarino:** This is best stories artifact.

**Matthew Panzarino:** So this is where that is represented in this run of the pipeline.

**Matthew Panzarino:** You can see it right here.

**Matthew Panzarino:** You can see what it's pulling.

**Matthew Panzarino:** And, of course, the content is just the content.

**Matthew Panzarino:** And then the rules, the task here, is what is defined in the pipeline to, like, actually do this.

**Matthew Panzarino:** That's in the YAML, right?

**Matthew Panzarino:** That's in, like, the, hey, now you're going to go do this step in the YAML code.

**Matthew Panzarino:** And, like, this tells us what's different.

**Matthew Panzarino:** If I want to see the execution of this live or post-live, if I hit inspect here, you will have a login to this.

**Matthew Panzarino:** This takes us to something called Flow Studio.

**Matthew Panzarino:** Flow Studio is what is actually running the workflows.

**Matthew Panzarino:** Atlas is the front end, right?

**Matthew Panzarino:** So Flow Studio is our backend, let's call it.

**Matthew Panzarino:** Just on like any website, you click on something, something happens.

**Matthew Panzarino:** It didn't happen on the website, it happened in the backend.

**Matthew Panzarino:** That's what this is.

**Matthew Panzarino:** You can see what it does here.

**Matthew Panzarino:** It parses the instructions, which this doesn't really have any, it basically says like, hey, I'm going to, I've got this workflow, I'm going to see what I have to do here, etc.

**Matthew Panzarino:** Then it evaluates the content.

**Matthew Panzarino:** It goes through, it looks at the overall assessment.

**Matthew Panzarino:** This article, blah, blah, blah, successfully integrates monograph case studies naturally within the content.

**Matthew Panzarino:** The evaluation found that the minimum requirement of one case study has been met with high quality integration.

**Matthew Panzarino:** So basically, it passed.

**Matthew Panzarino:** It's already integrated.

**Matthew Panzarino:** It's already good.

**Matthew Panzarino:** So it does not really need to do anything here.

**Matthew Panzarino:** So if you see it says past confidence 0.95, which in engineering speak is 95%.

**Matthew Panzarino:** And then you go reasoning.

**Matthew Panzarino:** It tells you like why it thought that it passed.

**Matthew Panzarino:** High confidence.

**Matthew Panzarino:** No separate sections for case studies.

**Matthew Panzarino:** We didn't want that to happen.

**Matthew Panzarino:** That also passed.

**Matthew Panzarino:** It's basically going through all the rules.

**Matthew Panzarino:** See?

**Matthew Panzarino:** And it's saying, did this pass?

**Matthew Panzarino:** Did it fail?

**Matthew Panzarino:** Et cetera.

**Matthew Panzarino:** And then it goes through an improvement cycle.

**Matthew Panzarino:** There is no improvement cycle because it was successful.

**Matthew Panzarino:** So I just want to kind of show you like there is a way to see exactly what's happening in each of these steps if you need to see.

**Matthew Panzarino:** Now, the drafter is significantly more noisy in this left-hand column.

**Matthew Panzarino:** Because drafting is a messy process.

**Matthew Panzarino:** For a human too, right?

**Matthew Panzarino:** Just like it is for agents.

**Matthew Panzarino:** So it does a handful of things.

**Matthew Panzarino:** It stores the research data, it generates the draft, then it runs evals.

**Matthew Panzarino:** These run in loops.

**Matthew Panzarino:** So you can see it runs an evaluation, then it plans an improvement cycle, and then executes the improvements.

**Matthew Panzarino:** And you can see it did one, two, three, four, five, six, seven, eight, nine rounds of drafts on this, right?

**Matthew Panzarino:** And each one is examinable.

**Matthew Panzarino:** So run the eval, okay?

**Matthew Panzarino:** Let's just take one groundedness, score one, that's great.

**Matthew Panzarino:** I'm gonna skip that one.

**Matthew Panzarino:** Oh, here we go.

**Matthew Panzarino:** Writing guidelines, score point three, fail, F minus, right?

**Matthew Panzarino:** Looking at this content, I need to evaluate major issues.

**Matthew Panzarino:** Voice and tone, uses generic business language instead of any professional and professional authenticity.

**Matthew Panzarino:** Lacks the lived experience perspective required by guidelines.

**Matthew Panzarino:** Missing design technical metaphors.

**Matthew Panzarino:** Resonate with artifacts, engineers, et cetera, right?

**Matthew Panzarino:** Then it plans some improvements.

**Matthew Panzarino:** So it says, okay, here's my plan.

**Matthew Panzarino:** I need to go through here and here's like, look, I'm going to take strategic and move it to practical or focused.

**Matthew Panzarino:** I'm to take comprehensive and change to complete to thorough, you know, planning out its improvements.

**Matthew Panzarino:** This is something that normally happens in here for humans.

**Matthew Panzarino:** Like you don't normally go, okay, I'm going to change comprehensive to complete and then go change comprehensive to complete.

**Matthew Panzarino:** You just change it, right?

**Matthew Panzarino:** But this process is the here process that's super important for agents.

**Matthew Panzarino:** Then we have the execution.

**Matthew Panzarino:** So it basically takes it and says, I'm to take these and go do this plan, right?

**Matthew Panzarino:** Now, once you've gotten down to the last iterations of these things, you can see what it's doing.

**Matthew Panzarino:** It's like, actually, this is fairly minimal, last thing.

**Danni Roseman:** You know, it's only doing like one or two things.

**Danni Roseman:** Sorry, I have to jump.

**Danni Roseman:** I have an ALG.

**Matthew Panzarino:** Bye.

**Matthew Panzarino:** Bye.

**Matthew Panzarino:** But you can see this last one here, looking at the evaluation scores.

**Matthew Panzarino:** Look, writing guidelines is now 0.75 instead of 0.3.

**Matthew Panzarino:** So perfection is never going to happen, but I'll get a lot closer, right, than we were before.

**Matthew Panzarino:** And you can see there's two critical improvements in this last round.

**Matthew Panzarino:** Word account, like currently 1,450, needs 1,500.

**Matthew Panzarino:** Okay, it's been a little hard on itself.

**Matthew Panzarino:** And maybe this is something we can examine.

**Matthew Panzarino:** Maybe give it a bigger range.

**Matthew Panzarino:** Like this is easily something that's an improvement for this pipeline that I just noticed, you know, where it's like, okay, that's a little strict, you know, 1,500 to 1,800, maybe 1,200 to 1,800.

**Matthew Panzarino:** Give it a little bit of a swing in case, you know, that way it doesn't word stuff just to get you to a word count, you know.

**Matthew Panzarino:** Because, like, now it's going to expand this section, add two to three sentences to the section to get you your word count.

**Matthew Panzarino:** Is that really necessary?

**Matthew Panzarino:** Probably not.

**Matthew Panzarino:** You know, so there's a room for improvement here.

**Matthew Panzarino:** Which is why it's nice sometimes to see how it's actually performing the work in here.

**Matthew Panzarino:** So I wanted to show you that really briefly as well.

**Matthew Panzarino:** So I know your elevator is probably full on that, but this call is recorded and it's got a transcript.

**Matthew Panzarino:** So you can always buzz through it if you need to.

**Matthew Panzarino:** But yeah, that's the kind of the concept there.

**Matthew Panzarino:** I think like your tools of the trade, to answer your last question there, is largely going to be nine times out of ten, and it's going to be the assignment directions or the context artifacts.

**Matthew Panzarino:** Like something there usually needs tweaking if you're not happy with your outputs.

**Matthew Panzarino:** And then of course, long tail, it's the pipeline itself or an engineering ticket or that sort of thing.

**Matthew Panzarino:** Those are the tools to improve how the pipeline is performing.

**Victor Alagbe:** Thank you so much.

**Victor Alagbe:** It's been a really insightful session.

**Victor Alagbe:** I just thought it was more like a meta question.

**Victor Alagbe:** I know that this...

**Victor Alagbe:** Restructure, MEs generally won't have like, won't engage with the clients.

**Victor Alagbe:** So we are not really client facing as well.

**Victor Alagbe:** So I wanted to ask you what or where you expect MEs to have like the biggest impact in the first, in the short time, say 30 to 60 days.

**Victor Alagbe:** Like, so based on everything you showed us, isn't like improving the atlas prompts or diagnosing workflow?

**Victor Alagbe:** Yeah.

**Victor Alagbe:** Something else?

**Matthew Panzarino:** Like what would you be like?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Here's how you're going to win.

**Matthew Panzarino:** Like I'm going to define, I'm working on defining new KPIs and all that stuff for this new world that we're in, but I'll give you like one primary KPI and a lot of stuff is going to drop by from this.

**Matthew Panzarino:** And that is efficiency, right?

**Matthew Panzarino:** And that, that, the way that that materializes very explicitly is from the time it exits the pipeline.

**Matthew Panzarino:** So from the time you get an output to the time you deem it client delivery ready, you're like, I am, I am proud of this.

**Matthew Panzarino:** I'm happy to deliver it to the client.

**Matthew Panzarino:** It's going to serve their goals.

**Matthew Panzarino:** It's human readable.

**Matthew Panzarino:** It's crisp.

**Matthew Panzarino:** It has all the elements that we want.

**Matthew Panzarino:** It's going to be performant.

**Matthew Panzarino:** Hopefully, obviously, you never can tell completely until it's out there.

**Matthew Panzarino:** But I believe strongly for this to be performant.

**Matthew Panzarino:** How long did that take you for each piece of deliverable?

**Matthew Panzarino:** From the moment the pipeline finished running and you set your eyes on that content, how long did it take you to get that edited into a shape for the client to look at it?

**Matthew Panzarino:** I would guess for a brand new raw pipeline that we just created for a client, that would hover around an hour to an hour and a half.

**Matthew Panzarino:** It isn't always the case.

**Matthew Panzarino:** Sometimes you get lucky.

**Matthew Panzarino:** You're like, wow, this nailed it, right?

**Matthew Panzarino:** That's cool.

**Matthew Panzarino:** Especially if their content is very like tofu and easily understandable.

**Matthew Panzarino:** If it's very top of funnel, very broad, very straightforward content.

**Matthew Panzarino:** Again, the pipeline is probably going to nail it, if I'm being honest with you, because it just knows how to write that kind of content.

**Matthew Panzarino:** But the more specificity that the client has, the more demands that they have, et cetera, the more time it will take, right?

**Matthew Panzarino:** However, that is not the end, right?

**Matthew Panzarino:** The improvement cycle is, okay, this took me an hour this time.

**Matthew Panzarino:** Why?

**Matthew Panzarino:** Why did it take me so long?

**Matthew Panzarino:** I had to manually check every link.

**Matthew Panzarino:** Okay, let me write that down.

**Matthew Panzarino:** I had to change, I had to remove a dozen EM dashes.

**Matthew Panzarino:** The client doesn't like them, right?

**Matthew Panzarino:** Because they think it's AI generated, even though, let's not go on that rant.

**Matthew Panzarino:** I had to remove a dozen of those.

**Matthew Panzarino:** That took me like 12 minutes.

**Matthew Panzarino:** I don't like timer myself.

**Matthew Panzarino:** What I do is just use the Google Docs timestamps.

**Matthew Panzarino:** Like, drop it into a Google Doc, and especially early on.

**Matthew Panzarino:** Like, we want everybody to edit an Atlas eventually, but we know pragmatically you can't, right?

**Matthew Panzarino:** Right now.

**Matthew Panzarino:** Do a lot of like the broad editing work in Atlas because the editor is not feature rich enough.

**Matthew Panzarino:** So if you're say, grab the output and you can do some of the work in Atlas because it has an AI assistant right there, especially if you're doing a couple of things like reflowing and stuff like that.

**Matthew Panzarino:** The AI assistant works very well.

**Matthew Panzarino:** However, if you drop it into a doc and time yourself, I view this as like my prime directive if I get a new account.

**Matthew Panzarino:** If somebody handed me a new account today, first thing I would do is run five items out of the pipeline, take all five of those, put them into a Google Doc, and edit the absolute bejesus out of them, and record everything I did.

**Matthew Panzarino:** So I'm used to just mode or record it, or even if I'm doing something systemic where I'm like, I'm going use the cloud for this, record what prompts that I used in cloud, right?

**Matthew Panzarino:** There's nothing to say you have to manually edit.

**Matthew Panzarino:** I personally like to because I like boots on the ground like to start so that I can like feel the dirt in my hands.

**Matthew Panzarino:** Then I can take a step outwards from there and tell Claude, hey, here's the things that I was doing manually.

**Matthew Panzarino:** Can you do these to this article?

**Matthew Panzarino:** And then refine.

**Matthew Panzarino:** My prompts there, et cetera, right?

**Matthew Panzarino:** The two ways that you record that are either manually, use suggest mode, or use your edit history to understand what you did.

**Matthew Panzarino:** The timestamps can tell you how long it took you, so they'll record it for you.

**Matthew Panzarino:** Okay, I opened the doc, and I made my first change at 10.42, my last change at 11.36.

**Matthew Panzarino:** I know how long this took me to edit, right?

**Matthew Panzarino:** Then recording the steps and everything that you did gives you the seed of a prompt library.

**Matthew Panzarino:** And that prompt library is a set of instructions that can be basically a proofreader.

**Matthew Panzarino:** So that proofreader workflow I showed you, you could just give it those instructions and say, this is what I had to do to this concept to get it ready, so can you just do this for me so I don't have to, please?

**Matthew Panzarino:** You know?

**Matthew Panzarino:** And, like, that agent will take that list and run with it.

**Matthew Panzarino:** That's how we did it.

**Matthew Panzarino:** Like, before the agentic pipelines were even a thing, we were, like, doing post-processing in Claude and came up with a list of post-processing instructions, and then once the agents rolled around, we're, like, oh, thank God, I can hand this

**Matthew Panzarino:** To an agent and have it run these, evaluate itself on whether it did those tasks and then run them again, et cetera, until it knocked it into shape.

**Matthew Panzarino:** Then your hour just turned into 35 minutes.

**Matthew Panzarino:** And then you run another pass of revision.

**Matthew Panzarino:** Okay, what did I have to do this time?

**Matthew Panzarino:** Okay, what did I have to do this time?

**Matthew Panzarino:** Right?

**Matthew Panzarino:** And you want to get yourself, my personal benchmark is 15 minutes.

**Matthew Panzarino:** Like if it takes me any longer than 15 minutes, let's look for ways to improve the pipeline.

**Matthew Panzarino:** And if that's systemic, if it's instruction set, if it's artifacts or conflicts, or if it's engine time, I don't care what it is.

**Matthew Panzarino:** My job, I view, like your job should be to make your job easier every day.

**Matthew Panzarino:** Like efficiency is the prime directive and it will be for everyone.

**Matthew Panzarino:** And you'll probably hear me say the same thing I was talking to you about on an all hands soon, right?

**Matthew Panzarino:** Like it's like the prime directive because we know we need to scale bigger on the services side.

**Matthew Panzarino:** But we cannot do.

**Matthew Panzarino:** We

**Matthew Panzarino:** That's silly, you know, A, it's exhausting to everyone involved, but it also doesn't make sense at the scale we have.

**Matthew Panzarino:** So if we were telling Kalil, we need you to take four clients, right?

**Matthew Panzarino:** And you're like, okay, how many deliverables per client?

**Matthew Panzarino:** And we're like, five.

**Matthew Panzarino:** And you're like, oh, okay, if it takes me like five to 10 minutes to check out each of these pieces of content, that's totally doable, right?

**Matthew Panzarino:** Like, you know, I'll run one client a day and then have the afternoon to do pipeline improvements and, you know, kind of do mind share and whatever.

**Matthew Panzarino:** That's a very livable life, you know, like an hour and a half per piece of content with four clients is a recipe for burnout, you know, and like disaster and you're feeling overwhelmed and all this.

**Matthew Panzarino:** I cannot promise you will be there to start, which is why nobody has five clients right now, right?

**Matthew Panzarino:** Like max three, you know, and we will slowly inch our way further down, but it is all.

**Matthew Panzarino:** So the way that you can succeed and we're like, hey, wow, know, Kalil and Victor are doing great.

**Matthew Panzarino:** This is awesome.

**Matthew Panzarino:** I'm glad they're here, etc.

**Matthew Panzarino:** The thing that will elicit that response is I took my review time from an hour per piece down to 30 minutes per piece through these actions, right?

**Matthew Panzarino:** And that could be I reviewed the conflicts or reviewed the artifacts for conflict and found a few and that shortened the generation time, but also improved the output, right?

**Matthew Panzarino:** And then I reviewed the instructions that I was giving it and I just could be more, I just could be clearer about this semantically.

**Matthew Panzarino:** And it did, it improved, you know, it removed this problem.

**Matthew Panzarino:** So identifying problems and then identifying solutions.

**Matthew Panzarino:** And sometimes those solutions will be ones you can affect as somebody who's in direct control of the artifacts and prompting.

**Matthew Panzarino:** And some of it is, hey, let's tag the entity in on this because I just don't know how to untangle this thorny knot.

**Matthew Panzarino:** You know, they have these things that we need to integrate and I don't quite know how to do that.

**Matthew Panzarino:** A, I'm new, or B, don't, you know, this is hard to do, seems hard, etc.

**Matthew Panzarino:** But that's the win condition, basically.

**Victor Alagbe:** That's incredibly helpful.

**Victor Alagbe:** Thank you so much.

**Victor Alagbe:** Because it actually really then ties into what Marcel was saying on the all-lands.

**Victor Alagbe:** If we're going to scale to 100 clients and we continue at two hours, then we need to bring in more MEs and CMS.

**Matthew Panzarino:** And we can't continue doing that until we get to 1,000 clients.

**Victor Alagbe:** So, yeah.

**Matthew Panzarino:** Thanks for me.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** Like, there is an efficiency level.

**Matthew Panzarino:** It's like, we can, I'm happy to hire more people ad nauseum.

**Matthew Panzarino:** I love working with people.

**Matthew Panzarino:** I love editors and all that stuff.

**Matthew Panzarino:** Clearly, you know, I've spent my entire career doing it.

**Matthew Panzarino:** But at some point, you have to go, cool, where's the balance between more people and, like, a productive environment and, like, high leverage?

**Matthew Panzarino:** And really, at this point, we're much more on the people end of the spectrum than the leverage end of the spectrum.

**Matthew Panzarino:** We have plenty...

**Matthew Panzarino:** We have plenty...

**Matthew Panzarino:** Of people to serve the clients that we have.

**Matthew Panzarino:** Like we have, you know, like 45 plus people and like 70 clients.

**Matthew Panzarino:** Okay, you know, that's not a good, great ratio.

**Matthew Panzarino:** And we all know that.

**Matthew Panzarino:** And the way that we improve that is, of course, of course, the English team is hard at work.

**Matthew Panzarino:** Like you're not alone.

**Matthew Panzarino:** They're working on improving this stuff every day.

**Matthew Panzarino:** But as people close to the ground, you have the best, you are our first customers, right?

**Matthew Panzarino:** And you are Atlas's first customers.

**Matthew Panzarino:** And that is super important.

**Matthew Panzarino:** Because we need to understand at a ground truth level, what is it capable of?

**Matthew Panzarino:** What is it failing at?

**Matthew Panzarino:** You know, et cetera.

**Matthew Panzarino:** And that also brings up the point, like, never be leery of saying like, oh, Atlas is not performing in this way.

**Matthew Panzarino:** Or this pipeline is not doing this thing that I want it to do.

**Matthew Panzarino:** Speak up.

**Matthew Panzarino:** Like early and often and vociferously.

**Matthew Panzarino:** Because we need that feedback loop.

**Matthew Panzarino:** And if you are failing at building leverage for yourself.

**Matthew Panzarino:** Therefore, it.

**Matthew Panzarino:** it.

**Matthew Panzarino:** or the pipeline is failing ability to leverage for you, knowing can help us to help you near-term and long-term.

**Matthew Panzarino:** Near-term by saying, okay, cool, let's get somebody in there to help you get with client deliverables this week, but then also long-term, how do we fix this leverage problem, right?

**Matthew Panzarino:** So speak up, for sure.

**Matthew Panzarino:** Sweet.

**Matthew Panzarino:** Okay, I have to bounce.

**Matthew Panzarino:** I've got to give like a minute before my next meeting, but thanks so much.

**Matthew Panzarino:** And this won't be the last time we speak.

**Matthew Panzarino:** Just our first hello and all that.

**Matthew Panzarino:** So we'll continue talking and feel free to reach out at a talk at any time.

**Matthew Panzarino:** Just for the note takers in the room to summarize a couple of the resources that I pointed out to you.

**Matthew Panzarino:** Iana and Nana are both fantastic at pipelines and manipulation.

**Matthew Panzarino:** So if you are ever looking for a resource or kind of wondering something about pipelines, please feel free to tap on them.

**Matthew Panzarino:** We also have an Atlas Learnings channel.

**Matthew Panzarino:** So in Slack, there is a channel called D Learnings Atlas.

**Matthew Panzarino:** Listen.

**Matthew Panzarino:** So Delivery Learnings Atlas, that's kind of a mindshare channel that you can ask questions in, no question too stupid or silly, you know, just ask.

**Matthew Panzarino:** And then the documentation, of course, is there for you if you need it.

**Matthew Panzarino:** And then our PodF Cloud project.

**Matthew Panzarino:** So the PodF Cloud project is accessible by logging in with pod-f at growthx.ai.

**Matthew Panzarino:** And then it will send myself, Yana, or Nana a link, and they'll have to send you that link to log in.

**Matthew Panzarino:** That's just the way they work.

**Matthew Panzarino:** But you're more than welcome to go in there and look at all of our projects and see all of the things that we've done.

**Matthew Panzarino:** We've built a ton of specific tools for our clients that are really useful to us.

**Matthew Panzarino:** Things like client-specific pipelines or client-specific tooling, that kind of thing.

**Matthew Panzarino:** Some of these tools are so specific to the client that it is just the best course of action to create a quick cloud project and do it that way, rather than to file a ticket to get engine to build this thing that's just like...

**Matthew Panzarino:** You do also have to think about that.

**Matthew Panzarino:** They only have so many hours in the day.

**Matthew Panzarino:** Is this going to benefit the whole org or not?

**Matthew Panzarino:** But feel free to take a look at any of that that you wish.

**Matthew Panzarino:** And then, yeah, that's about it.

**Matthew Panzarino:** Sweet.

**Victor Alagbe:** All right.

**Matthew Panzarino:** Thank you so much.

**Matthew Panzarino:** Great.

**Matthew Panzarino:** Thanks.

**Matthew Panzarino:** Glad to have you.

**Kalil Magtoto:** Ciao, ciao.

**Kalil Magtoto:** Thank you.

**Kalil Magtoto:** Bye.

**Kalil Magtoto:** Bye.
