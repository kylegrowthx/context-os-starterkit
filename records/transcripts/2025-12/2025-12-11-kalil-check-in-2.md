# Kalil: Check-In 2

<metadata>
date: 2025-12-11
time: 18:47 UTC
duration: 38 minutes
organizer: kalil@growthx.ai
participants: Kalil Magtoto, Matthew Panzarino
fathom_recording_id: 108148191
fathom_url: https://fathom.video/calls/500377366
share_url: https://fathom.video/share/CnNJJuHqwLg48DVFFUhEe-1x8TUBSG1y
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Kalil walked Matthew through significant progress on the PSEO ketamine pipeline (V3), which is now hitting nearly all targets after fixing misclassifications in V2 through a new classification structure. The team discussed outlier research times (e.g., 54 minutes) caused by external server timeouts rather than pipeline issues, and identified tools to optimize performance: the Convergence Report in Flow Studio for finding instruction ambiguities that drive inefficient iteration churn, and a request to add the Evaluation Report to the Atlas UI for the proofreader step.

---

## Context

This is an internal GrowthX check-in between Kalil Magtoto (product engineer) and Matthew Panzarino (likely CTL or strategic advisor). Kalil is responsible for a PSEO (Programmatic SEO) ketamine content pipeline project that aims to generate high-quality SEO content using templated processes and AI agents. Matthew appears to be reviewing progress and providing feedback on pipeline iterations. The pipeline operates within GrowthX's AI workflow system (using tools like Flow Studio and Atlas), and Kalil has been iterating on the pipeline design to improve output quality and consistency. This check-in is part of ongoing product development and optimization work.

---

## Relevance

**To GrowthX Delivery:**
- PSEO pipeline progress demonstrates significant improvement in output quality and consistency; V3 now hitting nearly all targets after fixing V2 misclassifications through classification structure.
- Identified key tools for pipeline optimization: Convergence Report (Flow Studio) for instruction ambiguities and iteration churn reduction; Evaluation Report needed in Atlas UI for proofreader step diagnostics.
- External server timeouts (research agent) identified as source of slow runs; team aware this is not a pipeline instruction issue but infrastructure constraint.

**To CheckThat:**
- Pipeline optimization work aligns with broader AI visibility and AEO capabilities; pipeline quality directly impacts CheckThat's content audit feature and beta deliverables.

**To GrowthX Business Development:**
- PSEO ketamine vertical pipeline is tracking well; successful pattern can be replicated across other verticals and content templates.
- Matthew's involvement suggests internal stakeholder confidence in pipeline progress; ready for next phase (beta link delivery to clients, advanced auditing features).

---

## Overview

- The PSEO ketamine pipeline (V3) is nearly hitting all targets, a major improvement over V2's misclassifications.
- Slow research times (e.g., 54 min) are outliers caused by external server timeouts, not pipeline issues; the team is aware.
- Use the "Convergence Report" in Flow Studio to find and fix instruction ambiguities that cause inefficient iteration churn.
- Request the "Evaluation Report" be added to the Atlas UI for the proofreader step, as it's a critical tool for identifying pipeline gaps.

---

## Key Topics

### Pipeline Performance & Debugging

  - Kalil's PSEO ketamine pipeline (V3) is nearly hitting all targets, a significant improvement over V2's misclassifications.
  - A key fix was adding a classification structure to help the pipeline triage articles correctly.
  - **Research Time:** A 54-minute research run was identified as an outlier.
      - **Cause:** Matthew's Temporal analysis confirmed it was an external server timeout, not a pipeline flaw.
      - **Context:** The researcher is the only agent with internet access; its speed is not directly controllable by pipeline instructions.
      - **Guidance:** Focus on the quality of the final article, not just speed. A fast pipeline producing bad content is useless.

### Tools for Optimization

  - **Convergence Report (Flow Studio):** This report flags instruction ambiguities that cause inefficient iteration churn.
      - **Example:** It found inconsistent word count targets and a missing URL for a required anchor text link.
      - **Action:** Clarifying these instructions can reduce the number of drafting iterations, speeding up the pipeline.
  - **Evaluation Report (Proofreader Step):** This report is a critical tool for identifying pipeline gaps.
      - **Problem:** It's visible in Flow Studio but missing from the Atlas UI in some pipelines.
      - **Solution:** Request the pipeline builder to add the `evaluation_report` field to the proofreader step's output in Atlas.

### Path for Continued Improvement

  - **Process:** Kalil's current method is effective: manually edit outputs, document changes, and use that data to refine pipeline instructions.
  - **Focus:** Shift from structural tasks to higher-level strategic thinking.
      - **Rationale:** LLMs excel at information delivery but struggle with narrative and storytelling.
      - **Goal:** Use pipeline automation to create capacity for strategic work, such as proactively developing content clusters for future product launches.
  - **Upcoming Tool:** Matthew is polishing a "Content Audit Pipeline" that will analyze content for AI cruft, narrative flow, and storytelling.
      - **Benefit:** Provides a rubric for editorial quality and pinpoints specific areas for pipeline improvement.
      - **Action:** Kalil will be a beta tester.

---

## Action Items

**Kalil Magtoto (GrowthX)**
- Add build team status Slack channel to daily checks
- Establish research baseline; run 2–3 overnight; if avg >60m, file ticket w/ Kirkland/Marcus
- Review Convergence Report; align word count ranges and add at-home linking URL
- File ticket to add Proofreader evaluation report to Atlas (rich text, below Result); reference Academy for X

**Matthew Panzarino (GrowthX)**
- Email Kalil content audit pipeline beta link when ready

---

## Transcript
**Kalil Magtoto:** Hey, how's it going?

**Kalil Magtoto:** Hello, sir.

**Kalil Magtoto:** It is going great.

**Kalil Magtoto:** Good.

**Kalil Magtoto:** Feeling more confident every day.

**Kalil Magtoto:** And then I'm faced with more overwhelm.

**Kalil Magtoto:** It's like the ebbs and flows of like, oh, , I'm finally doing my job right.

**Kalil Magtoto:** And then it's like, nope, let's correct you.

**Kalil Magtoto:** But honestly, like, I'm in a much better place now.

**Kalil Magtoto:** I know where I can make improvements, even further improvements.

**Kalil Magtoto:** But I wanted to share with you this little kind of side by side comparison of where we were at last week and where we're at this week.

**Matthew Panzarino:** Share.

**Kalil Magtoto:** Share.

**Kalil Magtoto:** All right.

**Kalil Magtoto:** So just for your quick reference, V1 is the initial output from the original pipeline as I was given it.

**Kalil Magtoto:** V2.

**Kalil Magtoto:** was my initial tweak, and v3 is where we're at right now, and where there are opportunities to make more edits.

**Kalil Magtoto:** PLDR v2 overcorrected, and this is for the PSEO ketamine stuff.

**Kalil Magtoto:** I also made tweaks to other pipelines.

**Kalil Magtoto:** Lots of different kinds of feedback across the pipelines that I need to implement, but the PSEO one is my favorite use case.

**Kalil Magtoto:** But if you see this table, it's basically like across the board.

**Kalil Magtoto:** It's hitting, initially when I made tweaks, it didn't hit any of the targets, like it failed, misclassified the article, I added a classification structure to help the triage process.

**Kalil Magtoto:** Yeah, good call.

**Kalil Magtoto:** And it made things good, and then it misclassified, then I had to find out where it misclassified.

**Kalil Magtoto:** Found out, fixed it, and then...

**Kalil Magtoto:** Now it's like almost there across the board.

**Kalil Magtoto:** It's like a different category.

**Kalil Magtoto:** So like it does bottom level up front now, bottom line up front.

**Kalil Magtoto:** Research is doing better.

**Kalil Magtoto:** Issue there, I think you're going to flag this for sure, is like research is taking really long.

**Kalil Magtoto:** This is like 54 minutes and this is across all the different types of pipelines that I've got going on.

**Matthew Panzarino:** So yeah, the team's aware of it.

**Matthew Panzarino:** The researcher is slow right now.

**Matthew Panzarino:** There's not a whole thing you can do about it, you know, so I don't.

**Kalil Magtoto:** What's that?

**Kalil Magtoto:** It might not be me.

**Matthew Panzarino:** I doubt it.

**Matthew Panzarino:** Like, you know, the research is informed by, course, the topic and well, like if you look at input, like click on research and click on input.

**Matthew Panzarino:** So these are the inputs here that this takes.

**Matthew Panzarino:** It takes, obviously, the instruction.

**Matthew Panzarino:** And it also takes the topic and it takes, if you scroll down past instructions, you'll see what else it takes.

**Matthew Panzarino:** Not much, right?

**Matthew Panzarino:** So it's basically like, hey, here's the topic and here's the instruction set and go off and do this, right?

**Matthew Panzarino:** But if you look at the instruction set, you can try to look through there for things that it's like, here's the source requirements because that comes from, it creates, let me start from the beginning.

**Matthew Panzarino:** I'm sorry.

**Matthew Panzarino:** I'm recurring and I don't want to confuse you.

**Matthew Panzarino:** This instruction set here is like a compilation of instructions from your assignment directions and anything in writing guidelines that guides research and obviously company context and personas, right?

**Matthew Panzarino:** Because it has to do research to provide the pipeline, the raw material to actually perform its task.

**Matthew Panzarino:** And the rest of the pipeline, unless you have specifically added a workflow that does this,

**Matthew Panzarino:** The rest of the pipeline does not access the internet at all, right?

**Matthew Panzarino:** So the researcher is the last, and you want that, trust me, because you don't want to introduce random variables.

**Matthew Panzarino:** You need like a source of truth for like, hey, here's the raw material that we have confidence in.

**Matthew Panzarino:** Now write the article using this raw material.

**Matthew Panzarino:** Now, obviously, some asterisks on that are linking, right?

**Matthew Panzarino:** Like internal linking, you know, looks at links on their site and, you know, stuff like that, right?

**Matthew Panzarino:** But as far as the drafting bit of it, the article drafter does not access the internet.

**Matthew Panzarino:** So this is important to know because it can help you isolate.

**Matthew Panzarino:** Like, where is this stuff coming from, right?

**Matthew Panzarino:** Like, where did this appear?

**Matthew Panzarino:** Why did this, what?

**Matthew Panzarino:** If it's not in the research, it won't be in the article.

**Matthew Panzarino:** Like, that's the way to think about it.

**Matthew Panzarino:** The converse is also true.

**Matthew Panzarino:** Are you giving the researcher a lot of tasks that aren't really all that important?

**Matthew Panzarino:** Like, are you giving it, like, stuff to do?

**Matthew Panzarino:** That is taking a really long time.

**Matthew Panzarino:** And is that really necessary, right, for it to do?

**Matthew Panzarino:** So when the researcher decides to do its job, it actually is going out and forming a plan.

**Matthew Panzarino:** And I'll show you, let me show you, let me take over screen sharing for just a second to show you how you're doing.

**Matthew Panzarino:** Yes, of course.

**Matthew Panzarino:** I think your rubric is great.

**Matthew Panzarino:** Like, I think this is an extremely organized and wonderful way to think about it.

**Matthew Panzarino:** And I haven't even done this for most people.

**Matthew Panzarino:** So I think this is really great.

**Matthew Panzarino:** You know, just kind of identifying what's working, your progress towards good, that sort of stuff.

**Matthew Panzarino:** You know, having Claude build that or maintaining that and understanding where you are is a great way to, like, work your way towards efficiency.

**Matthew Panzarino:** So I think that's fantastic.

**Matthew Panzarino:** And might even ask you to kind of share what you did here at some point, because I think it could be helpful to some people who are a little bit still kind of like struggling to go like, yeah, but how do I progress towards better?

**Matthew Panzarino:** And I can make sweeping suggestions for them on calls like this or in documentation where I'm like, hey, try this, try that.

**Matthew Panzarino:** But this iterative approach, I think, and very analytical approach is great because the pipelines will do best when they're given like articulated instructions and you know what's failing and you can work towards better.

**Matthew Panzarino:** So all of that is great.

**Matthew Panzarino:** So good, good job there.

**Matthew Panzarino:** Let me do this.

**Matthew Panzarino:** I'm just going to share, let's do Chrome here.

**Matthew Panzarino:** I was just helping Jen with outreach.

**Matthew Panzarino:** Let me get back out of here.

**Matthew Panzarino:** So let's look at one of these.

**Kalil Magtoto:** Is this the one you're working with or this one here?

**Matthew Panzarino:** Yes, yes.

**Matthew Panzarino:** Yeah, okay.

**Matthew Panzarino:** So let's just take a look at the research run here.

**Matthew Panzarino:** Oh, this one's 17 minutes.

**Matthew Panzarino:** That's not so bad.

**Matthew Panzarino:** Let's take a look at a long one.

**Kalil Magtoto:** This one was like something went wrong yesterday and it took forever.

**Kalil Magtoto:** Oh, that one?

**Kalil Magtoto:** Yeah, that one, like.

**Matthew Panzarino:** an outlier, like this, if it's an outlier, I wouldn't, I honestly wouldn't, like.

**Kalil Magtoto:** Try to tweak it?

**Matthew Panzarino:** No, I wouldn't, I wouldn't.

**Matthew Panzarino:** If it's an outlier, don't, don't stay up late thinking about this.

**Matthew Panzarino:** Like, it's not, sometimes, I mean, these are services, and sometimes they're bad, right?

**Matthew Panzarino:** Like, it's a Cloudflare issue, or if it's a dependency problem, or, like, a lot of times, if something's taking an abnormally long time, and I notice it, I can just go look.

**Matthew Panzarino:** Actually, the, the build team has a Slack channel that has system statuses for services like Cloud.

**Matthew Panzarino:** So you can go look at that.

**Matthew Panzarino:** I, sometimes I'll go just check that Slack channel, and be like, oh, yeah, Cloud's down, or Cloud's, you have an issue, or whatever.

**Matthew Panzarino:** And that way, I know that it's not, you know, I don't want to drive myself crazy by going, like, what did I do here, you know?

**Matthew Panzarino:** Right.

**Matthew Panzarino:** In any case, the researcher is, the speed of the researcher is not something you can govern.

**Matthew Panzarino:** don't know.

**Matthew Panzarino:** So if we go look, I'm just going to use this as an example.

**Matthew Panzarino:** So I mentioned the instructions here.

**Matthew Panzarino:** This is a compilation of instructions from various places.

**Matthew Panzarino:** Your assignment directions, the writing guidelines, the company context, that sort of thing.

**Matthew Panzarino:** If we go inspect this, I just want to show you what it's actually doing.

**Matthew Panzarino:** The very first thing it does is generate a plan, right?

**Matthew Panzarino:** So it says, given the inputs that I have here, what's the plan for me?

**Matthew Panzarino:** What are questions I need to answer?

**Matthew Panzarino:** And how should I go about answering them, right?

**Matthew Panzarino:** So as an example, like item one, planning error.

**Matthew Panzarino:** Well, I think we just figured out why this thing took so long.

**Matthew Panzarino:** It had some sort of issue here, right?

**Matthew Panzarino:** This planning, it had a planning error of some sort that caused...

**Matthew Panzarino:** Something.

**Matthew Panzarino:** Probably one of these processes to take an enormously long time.

**Matthew Panzarino:** So I think this is probably one of those things where you're like, wow, let's take a long time.

**Matthew Panzarino:** What happened?

**Matthew Panzarino:** Oh, well, there is a error.

**Matthew Panzarino:** But let's skip over that for just a second.

**Matthew Panzarino:** just want to show you generally what happens.

**Matthew Panzarino:** It creates questions for itself.

**Matthew Panzarino:** So what's the clinical diagnostic definition of grief, complicated grief, and PGD?

**Matthew Panzarino:** And what are the prevalence statistics?

**Matthew Panzarino:** It needs to know this for very obvious reasons, because it needs to be able to define it clearly in the article, accurately, right?

**Matthew Panzarino:** So then it says, okay, what's the depth of this?

**Matthew Panzarino:** This is advanced.

**Matthew Panzarino:** This is a clinical disorder.

**Matthew Panzarino:** I really need to do some good research on this.

**Matthew Panzarino:** What's the success criteria?

**Matthew Panzarino:** Must include at least three peer-reviewed sources from Tier 1 medical sources.

**Matthew Panzarino:** Priority, critical, critical, obviously very much needed.

**Matthew Panzarino:** And then you notice this requirement, you probably recognize this.

**Kalil Magtoto:** This comes from our requirements in the writing guidelines.

**Matthew Panzarino:** Yeah, what kind of sources should use, right?

**Matthew Panzarino:** So I'll just give you one.

**Matthew Panzarino:** For if you were to tell it like, hey, I want to do these things, how many sources of DSM-5-TR criteria are there, do you think, in the world?

**Matthew Panzarino:** And how hard is it going to have to look to find those, right?

**Matthew Panzarino:** And I'm not saying you shouldn't ask for this, especially if the client wants it.

**Matthew Panzarino:** But I'm just showing you, like, if you give it requirements and writing guidelines, those have second-order effects.

**Matthew Panzarino:** Like, they aren't just like, you're not just saying, oh, you know, I'd love it if you did this.

**Matthew Panzarino:** Because it's going to really try  hard to do those things.

**Matthew Panzarino:** And so if you give it something that is a very, very tough task to accomplish or a research that's very difficult, expect it to take more time, right?

**Matthew Panzarino:** Just, it will take more time.

**Matthew Panzarino:** But I'm not saying that that is an issue.

**Matthew Panzarino:** I'm just pointing it out.

**Matthew Panzarino:** Like, if you were, like, seeing something taking forever, and you're like, I wonder if I really need this amount of criticality here.

**Matthew Panzarino:** And so you can detune that a little bit, know, pull back a little bit and say, all right, let me ease up.

**Matthew Panzarino:** up on my hardcore requirements here and see where we're at, you know, and go from there.

**Matthew Panzarino:** But I honestly think you're probably fine because the other ones are taking 17 minutes, which is great, you know, for a resource.

**Kalil Magtoto:** It's like sometimes it takes forever, sometimes it takes less.

**Kalil Magtoto:** Overall, like is 90, I'm seeing it's like an hour and a half.

**Kalil Magtoto:** I don't have an issue with that because I'm doing other stuff too on the side while it's happening.

**Kalil Magtoto:** But I don't know, there was a point where the pipeline was like 35 minutes, 30 minutes, that's like on the faster end.

**Matthew Panzarino:** If you get like, here's a way to think about it too.

**Matthew Panzarino:** If you were running the pipeline and it was taking 35 minutes, but the output was crap, then that doesn't matter.

**Matthew Panzarino:** That 35 minutes, yeah, ignore that metric, right?

**Matthew Panzarino:** It's like, hey, it takes me 35 minutes to write a bad article.

**Matthew Panzarino:** Well, I don't care.

**Matthew Panzarino:** You know, I don't how long it takes you to write a bad article.

**Matthew Panzarino:** I care how long it takes you to write a good one.

**Matthew Panzarino:** So establish new...

**Matthew Panzarino:** Baselines for yourself.

**Matthew Panzarino:** And then you can identify outliers, right?

**Matthew Panzarino:** Where it's like, hey, you know, the research roughly takes 20 minutes.

**Matthew Panzarino:** And now this one took 50.

**Matthew Panzarino:** Okay, that's an outlier.

**Matthew Panzarino:** Let me run two or three more tomorrow or overnight, hopefully, you know, that's the best cadence, run it all overnight.

**Matthew Panzarino:** And then, you know, or the end of your day, and then next day, you're able to come in and see what's going on.

**Matthew Panzarino:** However, you can run those and you'd be like, oh, no, now I am averaging about an hour per research.

**Matthew Panzarino:** Then you can be like, hey, Kirkland, Marcus, or file a quick ticket.

**Matthew Panzarino:** Like, hey, could you check this to see where there's a possible issue?

**Matthew Panzarino:** And Marcus has a bunch of tools that he uses to identify like why things are slow, right?

**Matthew Panzarino:** And why issues are there.

**Matthew Panzarino:** Like some of those auto flags that we already showed folks, like in the drafter, it'll auto flag for you.

**Matthew Panzarino:** Like, hey, maybe you have some conflicts here or whatever.

**Matthew Panzarino:** And I'll show you that in a second just to refresh your memory.

**Matthew Panzarino:** But anyhow, long story short, it goes through and creates a plan and then executes that plan.

**Matthew Panzarino:** Afterwards, right?

**Matthew Panzarino:** So first steps, first things first, you can scroll through here and just see what is its plan?

**Matthew Panzarino:** Like how many questions does it have to ask?

**Matthew Panzarino:** And obviously, more questions equals longer time.

**Matthew Panzarino:** So you're like, hey, I don't need it to do some of these things.

**Matthew Panzarino:** It's not germane.

**Matthew Panzarino:** It's not important.

**Matthew Panzarino:** You can just elide those from your instructions or tweak it, you know, for this kind of article.

**Matthew Panzarino:** I honestly don't think 17 minutes is all that bad, to be honest, for these, so I wouldn't panic.

**Matthew Panzarino:** I don't think you need to adjust anything.

**Matthew Panzarino:** I just want to show you.

**Matthew Panzarino:** You can quickly scroll here to see what it's actually doing, right?

**Matthew Panzarino:** Then you can, if you really want to debug, look and see, okay, look, it gave me, it got results and it synthesized those results all together.

**Matthew Panzarino:** And if you were like wondering where it got something, you can see why it included those here.

**Matthew Panzarino:** gives you rationale.

**Matthew Panzarino:** And then it'll do then an evaluation of its research.

**Matthew Panzarino:** So it produces a report here where it says like,

**Matthew Panzarino:** Hey, does this research meet all the criteria?

**Matthew Panzarino:** No, it doesn't, right?

**Matthew Panzarino:** It gave me the score of 30% on this.

**Matthew Panzarino:** It said, you missed some stuff.

**Matthew Panzarino:** Here's some gaps.

**Matthew Panzarino:** Critical misalignment with article type classification.

**Matthew Panzarino:** Research concludes this is type B, comorbid support, but evidence actually suggests type C, or no treatment approach.

**Matthew Panzarino:** So this is basically like your instructions about alignment with what kind of like, you know, type of treatment this should be.

**Matthew Panzarino:** It's finding that.

**Matthew Panzarino:** That's great.

**Matthew Panzarino:** You know, it's noticing that there's an issue.

**Matthew Panzarino:** And I'm not going to belabor the point, but it also found these other issues, right?

**Matthew Panzarino:** So then it says, this research, blah, blah, blah, tier one sources.

**Matthew Panzarino:** However, there are critical gaps.

**Matthew Panzarino:** The research concludes type B classification confirmed, but the evidence presented no trials, no FDA approval, safety concerns, disassociation potentially interfering with grief processing more closely resembles a type C.

**Matthew Panzarino:** Contraindication criteria or a minimum requires a heavily modified type B, right?

**Matthew Panzarino:** So this is good.

**Matthew Panzarino:** This is a great thing.

**Matthew Panzarino:** It's finding this so that you don't later have to go like, wait a minute, this classified it completely wrong.

**Matthew Panzarino:** It says it could be treated with ketamine and it cannot, you know, like you have to then go like, well, this article sucks, you know?

**Matthew Panzarino:** So that's great.

**Matthew Panzarino:** This is good.

**Matthew Panzarino:** This is why agents exist.

**Matthew Panzarino:** They're grading themselves on their own work, right?

**Matthew Panzarino:** So that you don't have to grade them.

**Matthew Panzarino:** Then it generates additional questions to try and figure that out, right?

**Matthew Panzarino:** So it's like, what's the onset of time?

**Matthew Panzarino:** It's like basically trying to dig into this more and really try to understand what's going on here.

**Matthew Panzarino:** Then it synthesizes those results.

**Matthew Panzarino:** Then it evaluates.

**Matthew Panzarino:** So it did two loops basically here, right?

**Matthew Panzarino:** And the second one, 0.88, right?

**Matthew Panzarino:** Hey, this is good.

**Matthew Panzarino:** 88%.

**Matthew Panzarino:** This meets the criteria.

**Matthew Panzarino:** Now we have what we need to write this article.

**Matthew Panzarino:** Rigorous medical sourcing.

**Matthew Panzarino:** Critical article type classification.

**Matthew Panzarino:** Correct.

**Matthew Panzarino:** Fathom identifies this as type B.

**Matthew Panzarino:** With crystal clear reasoning, ketamine has no direct evidence for treating grief.

**Kalil Magtoto:** Yeah, it was this.

**Kalil Magtoto:** This is what I wanted.

**Kalil Magtoto:** Because initially it was saying there's no use at all.

**Kalil Magtoto:** But what we wanted to say was it doesn't treat the first bit.

**Kalil Magtoto:** It treats the second bit.

**Kalil Magtoto:** And then it fixed it.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Has strong evidence for treating depression, anxiety, and PTSD, right?

**Matthew Panzarino:** So, yes, it can't solve grief.

**Matthew Panzarino:** That's what alcohol is for.

**Kalil Magtoto:** No kidding.

**Matthew Panzarino:** But, no, it has no direct evidence for solving grief.

**Matthew Panzarino:** But the symptoms or comorbidities of grief, you know, it can't help there.

**Matthew Panzarino:** So, that's – you can see what it's doing.

**Matthew Panzarino:** It's doing the right thing.

**Matthew Panzarino:** It's trying to see if it found enough information to correctly classify.

**Matthew Panzarino:** And it's saying, I didn't.

**Matthew Panzarino:** I just – I couldn't quite get there.

**Matthew Panzarino:** So, let me ask some more questions.

**Matthew Panzarino:** And then it asked some more questions.

**Matthew Panzarino:** It got answers.

**Matthew Panzarino:** Then it evaluated itself again and said, I got it.

**Matthew Panzarino:** And it's not – it's type B.

**Matthew Panzarino:** You know, here's

**Matthew Panzarino:** So then it just does, I don't even know what these things do.

**Matthew Panzarino:** And then it stores it in Atlas.

**Matthew Panzarino:** So it basically says, okay, cool.

**Matthew Panzarino:** I've now got a package and I'm going to store this in Atlas.

**Matthew Panzarino:** In this case, this took a hell of a long time.

**Matthew Panzarino:** That's not necessarily a panic mode unless it starts to do that every time.

**Matthew Panzarino:** And then you're like, wait a minute, like what's going on?

**Matthew Panzarino:** But let's just look at it.

**Matthew Panzarino:** You don't even have to go this deep, by the way, almost ever.

**Matthew Panzarino:** It's just, this is something that like Marcus would look at or another client office engineer to understand like what part of the process took so dang long, right?

**Matthew Panzarino:** And so this is, Temporal is the platform that actually runs the workflows, right?

**Matthew Panzarino:** So Atlas is the front end.

**Matthew Panzarino:** Flow Studio stores the workflows and all the code and says like, defines what they are and handles the scripting.

**Matthew Panzarino:** And then Temporal actually executes them, runs them in order, right?

**Matthew Panzarino:** Um, but if we look here, so like this one, this workflow task.

**Matthew Panzarino:** Timed out here, right?

**Matthew Panzarino:** So this particular workflow, December 9th, 5.50, this one timed out.

**Matthew Panzarino:** Any timeouts are probably just lack of response from the server side.

**Matthew Panzarino:** So most likely this was trying to use Tably or Exa or whatever engine, and it wasn't responding.

**Matthew Panzarino:** Maybe they had a service outage, maybe they had something going on.

**Matthew Panzarino:** So anytime you see red in here, it's probably just something that it found where it was like, hey, you know, I couldn't do this.

**Matthew Panzarino:** So it looks like it took, yeah, so it started the task, it timed out, and so it started it again.

**Matthew Panzarino:** So there's some issues there.

**Matthew Panzarino:** The thing that took the most amount of time, though, was the validator.

**Matthew Panzarino:** So this is the, like, hey, is this, what is the definition of grief, complicated grief?

**Matthew Panzarino:** This is critical.

**Matthew Panzarino:** So this validator that says, did this do a good job?

**Matthew Panzarino:** That's the one that took the most amount of time.

**Kalil Magtoto:** Looks like it took 31 minutes.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** So that I think is an easy way to identify, hey, this is the one that was probably, it was cranking on and having a hard time executing.

**Matthew Panzarino:** And then if you look at another run, so let's look at one that was like 17 minutes as an example.

**Matthew Panzarino:** And let's just go look at the actual run of it.

**Matthew Panzarino:** This is much better because it's like, it's using, it's doing like, so it took four minutes, 55 seconds, and it took three minutes, 55 seconds to do each of these validators.

**Matthew Panzarino:** That's how long the validators should have taken.

**Matthew Panzarino:** So in my opinion, it was probably just a server side, like service oriented error, especially because you're doing roughly the same exact article over and over.

**Matthew Panzarino:** So, you know, these shouldn't be wildly different.

**Matthew Panzarino:** So...

**Matthew Panzarino:** All of that, like the Flow Studio stuff is helpful for, because it's human readable.

**Matthew Panzarino:** You can see what's going on, what it's actually doing.

**Matthew Panzarino:** The temporal stuff is not necessary, but sometimes if you want to dig in, it can tell you like, oh, what's, what happened?

**Matthew Panzarino:** You know, what's the outlier?

**Matthew Panzarino:** What happened there?

**Matthew Panzarino:** However, I think you're absolutely on the right track with your rubric, and I think you are fine here.

**Matthew Panzarino:** I think these are good questions.

**Matthew Panzarino:** It clearly is identifying the key, the critical classification thing that you had.

**Matthew Panzarino:** So that aligns with your chart of progress, right?

**Matthew Panzarino:** Like, hey, it wasn't, and now it is classifying properly.

**Matthew Panzarino:** So that's all good.

**Matthew Panzarino:** So that's fantastic.

**Matthew Panzarino:** I think it's a great approach to improving your process there and getting closer to, hey, I feel like this is actually doing the tasks I asked it to do.

**Kalil Magtoto:** Yeah, I think what's, what's becoming clear to me now is, you said this last week, and I really like, kind of like, drilled down on it is, I need to go in and just like, edit it myself, document.

**Kalil Magtoto:** And everything that I do, and then, you know, I'll get Claude's help to see if like, did I do anything extra or just like do a side by side.

**Kalil Magtoto:** And then I just have that running as like its own, it's its own like chat where like I dropped an A and I drop a B and then document it.

**Kalil Magtoto:** And then I, okay, onto the next thing, A, B, onto the next thing.

**Kalil Magtoto:** then it just compiles this massive document for me at the end.

**Kalil Magtoto:** And then like, I drop it into the pipeline or my plan is to drop it into the pipeline builder.

**Kalil Magtoto:** And then say, hey, I have all this documentation.

**Kalil Magtoto:** Let's go ahead and improve the pipeline based on this.

**Kalil Magtoto:** And then, and then I have to go again.

**Kalil Magtoto:** I will go and repeat this over and over and over until I get too close to one shot.

**Kalil Magtoto:** It's getting there.

**Kalil Magtoto:** Like, I was able to do five edits yesterday in like three and a half hours, which was awesome.

**Kalil Magtoto:** Today, Matt just messaged me.

**Kalil Magtoto:** He was like, hey, Kalil, I'm out of office tomorrow.

**Kalil Magtoto:** Like, I need to get these things done really quickly.

**Kalil Magtoto:** And between 10 a.m.

**Kalil Magtoto:** and this call, and I had a meeting in between, I finished four articles.

**Kalil Magtoto:** So I was like, wait a second, it's getting fast now.

**Matthew Panzarino:** So we're getting there.

**Kalil Magtoto:** I'm really pleased.

**Kalil Magtoto:** So, yeah.

**Matthew Panzarino:** Yeah, that's awesome.

**Matthew Panzarino:** Yeah, progress is great.

**Matthew Panzarino:** It can feel really good when you're kind of making those little breakthroughs.

**Matthew Panzarino:** And, you they add up.

**Matthew Panzarino:** Sometimes you're like, oh, I only saved myself a few minutes.

**Kalil Magtoto:** But, like, eventually, trust me, they will add up, you know?

**Kalil Magtoto:** Yeah.

**Matthew Panzarino:** And remember, too, that you do have a little tool that Marcus shipped to help with some of that.

**Matthew Panzarino:** And that is in, so in the, like, the drafting step, if you go to inspect in studio here, in the studio, you can see this convergence report that he created.

**Matthew Panzarino:** And this actually says, like, this is doing a good job, right?

**Matthew Panzarino:** Like, there's minor specification gaps causing iteration churn, but overall,

**Matthew Panzarino:** This is a pretty efficient version of the instruction set, and you can see here, like, there's no direct contradictions detected, so your conflict checks worked, but it does say there's some ambiguity in word count target range, so direction, target word count this, guidelines, total before FAQ this, right?

**Matthew Panzarino:** So I would say align these two a little bit, maybe, you know, so overlapping but inconsistent ranges just may cause it.

**Matthew Panzarino:** Here, gap analysis, anchor text linking, guideline says state first at-home mentioned links to at-home benefits page, but directions doesn't specify the URL or reinforce this requirement, right?

**Matthew Panzarino:** So there's a handful of things in here you may want to look through and see if, and parse to see if you like those or agree, because, you know, it kind of, like, could slow it down, right?

**Matthew Panzarino:** It's just a slightly less efficient than it could be, and that is right here in the convergence report tab, inflows to

**Matthew Panzarino:** And this is documented, by the way, in the last editor update that we did, so it's linked, and there's an explanation in case you forget, like, you know, it will be documented.

**Matthew Panzarino:** And he's coming up with new tools like this all the time, so I'll try and make sure we surface those.

**Matthew Panzarino:** He's already got another new fun tool that integrates some of my content audits into our report.

**Matthew Panzarino:** But, like, that's basically what's going on here.

**Matthew Panzarino:** So I would say, like, this could be helpful to you just to highlight some things, but this already is a great sign.

**Matthew Panzarino:** like, 85%, you know, quality is good, and there's only minor issues.

**Matthew Panzarino:** But there's some, the five iterations of this article drafter are the reason that this took 41 minutes.

**Matthew Panzarino:** 41 minutes, yeah.

**Matthew Panzarino:** And so if you can eliminate one or two iterations by clarifying directions a little bit, it'll speed that up, right?

**Matthew Panzarino:** And it'll make your life easier.

**Matthew Panzarino:** So something to take a peek at there.

**Kalil Magtoto:** Can I show you something?

**Kalil Magtoto:** Something that I found, which I haven't, it's in Immubit.

**Kalil Magtoto:** There is a final proofreading.

**Kalil Magtoto:** So this is V2 of the pipeline.

**Kalil Magtoto:** It's working decently.

**Kalil Magtoto:** And in here, when I go into final proofreading, it gives me an evaluation report.

**Kalil Magtoto:** And I love this evaluation report because what I do is I'll just take it.

**Kalil Magtoto:** And I'll drop it into my first, like, go in Claude.

**Kalil Magtoto:** I'll say, like, hey, this was the evaluation report.

**Kalil Magtoto:** Also, we found these gaps right now in the current pipeline.

**Kalil Magtoto:** And because I'm shipping out five articles this week, then, like, okay, I'm going to prioritize shipping it out first.

**Kalil Magtoto:** And then on Friday, then I can go into pipeline improvements again.

**Matthew Panzarino:** Do an iteration, yeah.

**Kalil Magtoto:** But this was super useful.

**Kalil Magtoto:** And I don't actually know where in the – I haven't taken a look at it.

**Kalil Magtoto:** So I'm going to just, like, like, noodling.

**Kalil Magtoto:** Now, with you, but it shows up here, but it doesn't show up in Interwell, in the proofreading section.

**Kalil Magtoto:** Like, I'm like, I don't know what I did right to get this evaluation report, but it doesn't show up in the Interwell BSEO.

**Kalil Magtoto:** Like, when I go into here, like, I'll do this, and then there's, like, a proofreader.

**Kalil Magtoto:** It, oh, no, okay, so it does it for this.

**Kalil Magtoto:** It doesn't do it for the generic one.

**Matthew Panzarino:** Oh, okay.

**Kalil Magtoto:** one.

**Kalil Magtoto:** There's, like, I have, like, another one, and final proofreader.

**Kalil Magtoto:** It doesn't see it.

**Matthew Panzarino:** Yeah, it's missing here.

**Kalil Magtoto:** You can actually, you should be able to, okay, so, like, if you go to inspect there.

**Kalil Magtoto:** Yep.

**Matthew Panzarino:** In the right corner.

**Kalil Magtoto:** Yeah.

**Matthew Panzarino:** Yep.

**Matthew Panzarino:** You should be able to, like.

**Matthew Panzarino:** Is this it?

**Matthew Panzarino:** Yes, it is.

**Matthew Panzarino:** You see, right here.

**Matthew Panzarino:** here.

**Matthew Panzarino:** go.

**Matthew Panzarino:** Now, you can look at it here, but it does not mean that you cannot have this in Atlas.

**Matthew Panzarino:** All you've got to do is ask the pipeline builder to add that as an output to that step.

**Matthew Panzarino:** hey, make sure that you add the evaluation report to the output.

**Matthew Panzarino:** It's just a field.

**Matthew Panzarino:** That's all it is.

**Matthew Panzarino:** It's just a field that's not shown there.

**Matthew Panzarino:** So theoretically, yes, you could file a ticket for this and be like, hey, I need this field added to this step in the workflow.

**Kalil Magtoto:** could probably just do this.

**Matthew Panzarino:** very easy to do by saying, hey, there's an evaluation report field that I would like to appear in the output for the proofreader step.

**Matthew Panzarino:** Could you please make sure that it appears there as well?

**Kalil Magtoto:** And it'll just...

**Matthew Panzarino:** Nice.

**Matthew Panzarino:** That's it.

**Matthew Panzarino:** Excellent.

**Matthew Panzarino:** So yeah, is the same thing.

**Matthew Panzarino:** This is the report right here.

**Matthew Panzarino:** I actually like reading it in here because it's more readable.

**Matthew Panzarino:** The other dump is more raw text.

**Matthew Panzarino:** But I think you may even be able to specify that.

**Matthew Panzarino:** So fine.

**Matthew Panzarino:** Try that.

**Matthew Panzarino:** I haven't even tried it because I've just been, I have, you know, a million things on my plate.

**Matthew Panzarino:** But you could also try telling it, hey, I'd like that output report to be a rich text field, you know, not a raw text field or a plain text field.

**Kalil Magtoto:** And then it shows up, it would show up here.

**Matthew Panzarino:** It'll show up like that.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Yeah, it'll show up just like the one you're seeing here.

**Matthew Panzarino:** But yeah, exactly.

**Matthew Panzarino:** Say, below the result, I would like a, below the result field, because you can tell it where, you know, you want it to.

**Matthew Panzarino:** You'd be a little product designer.

**Matthew Panzarino:** Say, below the result field, I would like the evaluation report.

**Matthew Panzarino:** Please.

**Kalil Magtoto:** Thank you.

**Kalil Magtoto:** Bye.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** And if it's appearing in another pipeline, you can say, and you're working the same pipeline builder, you can say, hey, I'm giving you this other pipeline that I'm working on for Interwell.

**Matthew Panzarino:** You may notice that in the Academy for X pipeline, it's got a proofreader field that appears, or excuse me, an evaluation report.

**Matthew Panzarino:** I need one like that in this pipeline, right?

**Matthew Panzarino:** Simple.

**Matthew Panzarino:** You don't have to get too crazy about it.

**Matthew Panzarino:** It'll find it and add it for you.

**Matthew Panzarino:** You could even, obviously, just go in and edit the outputs here in the code, but why?

**Matthew Panzarino:** Yeah, I don't want to mess anything up.

**Matthew Panzarino:** might call in and, yeah, yeah, exactly.

**Matthew Panzarino:** But yeah, exactly.

**Matthew Panzarino:** So you can always, that report is always generated.

**Matthew Panzarino:** It's a byproduct of the egyptic process.

**Matthew Panzarino:** It needs to make that so that it knows whether or not to run another loop.

**Matthew Panzarino:** But you do not, if you don't see it, there's no reason you can't pull it in and have it present to you.

**Kalil Magtoto:** Very cool.

**Kalil Magtoto:** Yeah, this was a breakthrough week.

**Kalil Magtoto:** Well, guess technically every week so far has been a breakthrough.

**Kalil Magtoto:** I'm just, I'm freaking loving it here, man.

**Kalil Magtoto:** I hope, I don't want to come across as kiss .

**Kalil Magtoto:** It's like the worst thing in the world when I look at all the, all the stuff that I put into Slack and I'm just like, dude, man.

**Kalil Magtoto:** If I was here for six months, a year, I would look at myself and be like, God, this guy's trying to piss us here.

**Matthew Panzarino:** But I'm just loving it so much.

**Kalil Magtoto:** It's weird.

**Matthew Panzarino:** I like it.

**Matthew Panzarino:** It is a place, like, it's definitely a time in the technological adaptation and adoption of AI and LLM technology where any company you work at needs to offer you the opportunity to, like, skill build and to make yourself into this new kind of person.

**Matthew Panzarino:** Because, yes, you're doing content work here, but it's not like these skills aren't transferable, right?

**Matthew Panzarino:** Like, having the ability to learn this rapidly is one of the most exciting things for me here.

**Matthew Panzarino:** And it's, like, the reason I'm here.

**Matthew Panzarino:** You know, I want to learn.

**Matthew Panzarino:** I want to understand these things more rapidly.

**Matthew Panzarino:** You know, sometimes I'm learning just ahead of what everybody asks every day.

**Matthew Panzarino:** And that's wonderful.

**Matthew Panzarino:** I love that.

**Matthew Panzarino:** I knew how to do my old job extremely well.

**Matthew Panzarino:** And I did that for a decade.

**Matthew Panzarino:** And I was bored out of my mind.

**Matthew Panzarino:** Like as much as the endorphin rush of any given billionaire texting me at midnight pissed about a story was, that's fine.

**Matthew Panzarino:** I don't need that.

**Matthew Panzarino:** That's not what excites me, right?

**Matthew Panzarino:** So like all of the stuff that and I don't really care.

**Matthew Panzarino:** Like I have no ego about being a celebrity or being famous and all that stuff like a lot of editor in chiefs seem to do, right?

**Matthew Panzarino:** Like you're all I'm gonna parlay this into a not novelist career or a broadcast career or whatever, right?

**Matthew Panzarino:** Like that's the path.

**Matthew Panzarino:** You know, I'm gonna go like work for a big co big corporation and then like become a name and you know, all of that, right?

**Matthew Panzarino:** And then maybe parlay that into a political career or a speaking tour or whatever.

**Matthew Panzarino:** I don't care about any of that.

**Matthew Panzarino:** Like I want to learn new things.

**Matthew Panzarino:** And I love technology and I love building product.

**Matthew Panzarino:** And so like, that's what attracted me to this, you know, company and to Daniel and to Marcel.

**Matthew Panzarino:** So the opportunities there are endless.

**Matthew Panzarino:** And if you're executing well, can

**Matthew Panzarino:** Um, alongside learning.

**Matthew Panzarino:** mean, that's best case scenario, obviously.

**Matthew Panzarino:** Um, and it offers you endless, you know, opportunities to sort of learn and grow and add to your skillset and, you know, keep being a more fully fleshed out person.

**Matthew Panzarino:** So, um, happy that you're excited about it.

**Matthew Panzarino:** I am too.

**Matthew Panzarino:** Nice.

**Matthew Panzarino:** Yeah.

**Kalil Magtoto:** How do I, um, I'll leave you with this.

**Kalil Magtoto:** How do I continue, uh, improving?

**Kalil Magtoto:** I feel like I've hit the, like, bare, bare minimum expectations.

**Kalil Magtoto:** Um, I, I, I try to benchmark myself against these other, my peers.

**Kalil Magtoto:** Um, some of them come from, editorial backgrounds like yourself.

**Kalil Magtoto:** I don't, uh, transparently.

**Kalil Magtoto:** Like, I'm, I'm just like a content guy, like a general content guy.

**Kalil Magtoto:** I, I came from video.

**Kalil Magtoto:** That's my, that's my world.

**Kalil Magtoto:** Um, but I'm happy to learn very quickly.

**Kalil Magtoto:** So, like, how do I continue progressing?

**Kalil Magtoto:** What kind of skills do I need to, like, continue?

**Matthew Panzarino:** Yeah, mean, I think that the vast majority of things that LLMs are bad at are about, like, transitions and narrative flow, right?

**Matthew Panzarino:** Like, they're very good at packing information in, but they're really not good at storytelling.

**Matthew Panzarino:** And I think that's where I would concentrate a large amount of your effort is making sure that you are sweeping all of the structural and architectural stuff into the Atlas bucket.

**Matthew Panzarino:** So that you can concentrate on to, hey, is this telling a good story?

**Matthew Panzarino:** Is this driving towards the customer goal?

**Matthew Panzarino:** Like, it allows you to, like, it allows you breathing room between looking at, like, you know, copying and pasting and moving all the stuff all around.

**Matthew Panzarino:** It allows you breathing room between that work and being able to step back and say, hey, I remember what the EM was saying to them on my last call.

**Matthew Panzarino:** They really want to drive towards this.

**Matthew Panzarino:** We're planting these seeds now.

**Matthew Panzarino:** I know it's going to take 60 to 90 days to, like, bear fruit.

**Matthew Panzarino:** So I need to think.

**Matthew Panzarino:** Think ahead, like, are they, they mentioned that they're introducing this new product.

**Matthew Panzarino:** Should we say, hey, who's your EM on this account?

**Matthew Panzarino:** Matt.

**Matthew Panzarino:** Okay, so you say Matt.

**Matthew Panzarino:** And I thought, like, you know, Interweb was talking about, or you put in your notes, that Interweb is launching a new, you know, strawberry-favored ketamine.

**Matthew Panzarino:** Whatever.

**Matthew Panzarino:** No, they're launching this new product, and they're, like, positioning it in a different way, and they're just sort of talking to you about that.

**Matthew Panzarino:** But I think that we can lean into that now, spin up a new cluster, we'll do a little keyword research, spin up a new cluster, and start planting those seeds now.

**Matthew Panzarino:** Present that to them, and say, hey, because there's no reason you can't, like, talk about strategy with Matt.

**Matthew Panzarino:** It's not like it's all Matt's responsibility, and you can't, you have no say.

**Matthew Panzarino:** Because you're operating at a ground truth level, and you can tell whether or not things are driving towards their goal.

**Matthew Panzarino:** So,

**Matthew Panzarino:** You can say, like, you know, I think we can spin up a new pipeline to generate content like this that is architected in a way that will speak to this new product.

**Matthew Panzarino:** And we'll start planting seeds now so that when they do launch it, they already are attracting the audience that is right for this, right?

**Matthew Panzarino:** Like, those kinds of things aren't possible to think about until you've built leverage for yourself, you know?

**Matthew Panzarino:** Like, you know, you're in the flow.

**Matthew Panzarino:** You're like, God, I can't even think about that.

**Matthew Panzarino:** I got to get this work done out this week, right?

**Matthew Panzarino:** And, like, that, I think, is the huge thing.

**Matthew Panzarino:** That's how you get, that's the ideal, like, zen moment where you're like, hey, I'm in full command of my deliverables.

**Matthew Panzarino:** The pipelines are operating well within the bounds of, you know, adjustment.

**Matthew Panzarino:** And I have the time to actually think about outcomes.

**Matthew Panzarino:** And, like, outcomes is so vital to, like, reset our expectations around.

**Kalil Magtoto:** As I talked a little bit about on the last call.

**Matthew Panzarino:** It's like, it does not matter how great you were.

**Matthew Panzarino:** So the parts that matter are like, are we telling the right story to drive the right outcomes overall?

**Matthew Panzarino:** And that part of it, I think, applies to video and other types of storytelling and marketing as well as it does to any content.

**Matthew Panzarino:** So the content labor of punctuation or formatting and all of that stuff that you have a hip pocket understanding of as a content person over time isn't as vital to understand or learn anymore.

**Matthew Panzarino:** It's really more about that gut instinct of, hey, yes, this is factually accurate, logically sound, and formatted properly, but it actually is telling the wrong story.

**Matthew Panzarino:** And that's the bits that I think is important to kind of understand.

**Matthew Panzarino:** Now, on a more pragmatic level, there is a content audit pipeline that I have just started to polish up because I want everybody to be able to use it, but I've been using it for my...

**Matthew Panzarino:** Content audits.

**Matthew Panzarino:** And as soon as I get a beta of that, I will point you at it and you can play around with it and run some of your content through it because it will give you my rubrics for success along with some research paper in it and some stuff I've integrated for various research papers to kind of show you where the pipeline is falling over in terms of like AI cruft, like just AI crap words or phrases, but also storytelling and narrative, like linking stuff logically.

**Matthew Panzarino:** together, narrative flow from one section to another, things like that, that you can then hopefully translate into pipeline improvements and your own editorial rubric understanding, right?

**Matthew Panzarino:** So it'll kind of benefit that side of it where you're like, hey, I don't have as much experience in that world.

**Matthew Panzarino:** This will give you some visibility and like open your eyes, hopefully to some of those things.

**Matthew Panzarino:** But then also on a very practical perspective, it can show you pointedly in your content where these things are appearing and then you can make corrections or adjustments to the pipeline.

**Kalil Magtoto:** Nice.

**Matthew Panzarino:** I'm looking forward to that.

**Matthew Panzarino:** Cool.

**Kalil Magtoto:** Very cool.

**Matthew Panzarino:** Thank you very much.

**Matthew Panzarino:** to on with beta testers.

**Kalil Magtoto:** Yes, happy to.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Sweet.

**Matthew Panzarino:** Thanks.

**Kalil Magtoto:** Ciao.

**Kalil Magtoto:** Have a good one.

**Kalil Magtoto:** You too.
