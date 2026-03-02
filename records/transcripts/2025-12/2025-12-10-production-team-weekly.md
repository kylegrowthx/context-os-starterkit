# Production Team Weekly 

<metadata>
date: 2025-12-10
time: 15:58 UTC
duration: 60 minutes
organizer: saskia@growthx.ai
participants: Aida Knezevic, Andi Bailey, Andrew, Bailey Seybolt, Bisera, Carly Piekos, Carrie Chowske, Ehtisham Hussain, Erik O'Brien, Fatima, Felix Morgan, Gabrielle Brogan, Ifeoluwa, Iana, Jakub Rudnik, Jenny Macrohon Dabon, Jenn Peters, Jessalynn, Jo Kaminska, Josip Sovar, Kalil, Katya Luscomb, Kathy Lam, Kelvin Njiru, Kirkland Gee, Lawrence Neves, Leah Myers, Liz Kushnereit, Marcus Derencius, Martha Martins, Matthew Alves-Hill, Matthew Panzarino, Mariana Marins, Megan Dickey, Nathalie Schrans, Nathan Navidzadeh, Oluwatimilehin Ademosu, Pamela Weber, Patricia, Rachel, Saskia Wartnaby, Simran Sethi, Sydney Go, Sucheta, Tamara, Usman Adepoju, Usman Ghani, Victor, Vivek, William Leborgne
fathom_recording_id: 107712116
fathom_url: https://fathom.video/calls/500566393
share_url: https://fathom.video/share/JbPQYekLhY6G_SAAtTzECLXT8AqhV5mj
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Matthew Panzarino reset expectations around how GrowthX's production team uses Atlas, the agentic content pipeline, addressing three critical inefficiencies: over-engineered assignment directions that confuse agents, misuse of external LLMs for rewrites (which bypasses Atlas's success rubrics), and failure to feed learnings from manual edits back into the system. The team committed to simplifying assignment briefs to goal-oriented frameworks with word count ranges, adopting an outcomes-first mindset (growth over literary perfection), and using Claude for specific diagnostic tasks only. Holiday coverage logistics were finalized: no publishing Dec 25–Jan 1, with one-person-per-pod daily check-in coverage coordinated through EMs, and Matthew assigned three action items including distributing the meeting agenda and sharing Marcus's convergence report (an experimental diagnostic tool for identifying slow agentic runs).

---

## Context

This is the GrowthX production team's weekly sync, where delivery and operations teams align on how to best use the company's agentic content pipeline called Atlas. The meeting was led by Matthew Panzarino, who manages the production operations, and recorded by Saskia Wartnaby. The team had recently completed "Week 1 mandatory" setup tasks (editorial checklists, operating manuals, artifact conflict checks) and was preparing for the December holiday break. The context for this meeting is that Atlas, which leverages Claude-based agentic workflows, has been in active use but the team discovered widespread inefficiencies in how people structure assignment briefs and use external tools, leading to slow pipeline runs and excessive manual editing. The discussion aimed to reset how 60+ GrowthX production staff approach pipeline workflows to maximize efficiency and focus on business outcomes.

---

## Relevance

- **To GrowthX Delivery:** Standardized workflow for simplified assignment directions (basic frameworks with word count ranges) will reduce post-processing edits from hours to minutes, scaling delivery efficiency across all 60+ production team members. Week 1 mandatory tasks (editorial checklists, operating manuals, artifact conflict checks) must be completed before the Dec 22 deadline for every account to prevent delivery gaps during the quiet week.

- **To GrowthX Delivery & Process:** "Outcomes-first" mindset shift—focus on growth metrics (traffic, conversions) rather than literary perfection—justifies faster, scalable processes and may unlock new pricing/delivery models. Established that agents should not be fed overly specific constraints (word counts, complex formatting rules) which cause agents to loop and produce awkward output.

- **To Atlas / Product:** Convergence Report (experimental diagnostic tool in Flow Studio, not yet in Atlas UI) helps diagnose why agentic drafts take >10–15 minutes; feedback will be critical for improving the drafter and identifying which conflicting instructions or artifacts cause slowdowns. The tool is available via Marcus Derencius's Slack comment in Flow Studio.

- **To Team Execution & Hiring:** Holiday planning logistics clarified—no publishing Dec 25–Jan 1, one-person-per-pod daily check-in coverage, EMs coordinate client expectations, content must be generated ahead by Dec 22. Team must validate that simplified assignment directions still produce quality output before rolling out team-wide (testing on "a few articles" suggested by Matthew).

---

## Overview

- **Simplify Assignment Directions:** Replace complex, task-based briefs with simple, goal-oriented frameworks. This prevents agent confusion and reduces post-processing edits from hours to minutes.
- **Prioritize Pipeline Improvement:** Focus on fixing the pipeline itself, not just its output. This builds leverage, saving far more time in the long run than manual editing.
- **Use LLMs for Specific Tasks Only:** Avoid using Claude for full article rewrites. Instead, use it for precise tasks (e.g., generating post-processing checklists) and to diagnose pipeline issues, then feed those learnings back into the system.
- **Adopt an "Outcomes-First" Mindset:** Shift from a "content agency" to an "outcomes company." The goal is growth (traffic, conversions), not literary perfection, which justifies using efficient, scalable processes.

---

## Key Topics

### Problem: Inefficient Pipeline Usage

  - Common issues causing slow, inconsistent output and excessive manual work:
      - **Over-engineered Assignment Directions:** Overly detailed briefs with specific word counts and complex constraints confuse agents, forcing them to reconcile contradictions and producing awkward writing (e.g., convoluted sentences, excessive M-dashes).
      - **Misuse of External LLMs:** Using Claude for full article rewrites after Atlas has drafted them is inefficient and inconsistent. It bypasses Atlas's agentic system, which uses a success rubric and iterative loops to ensure quality and adherence.
      - **Lack of Pipeline Improvement:** Failing to analyze manual edits and feed those learnings back into the pipeline (via artifacts, directions, or new workflows) prevents the system from improving.

### Solution: A New Workflow & Mindset

  - **Simplify Assignment Directions:**
      - Provide a basic framework (e.g., "Intro," "Body," "Conclusion").
      - Use word count *ranges* instead of exact numbers.
      - Focus on high-level goals, not specific tasks.
      - Reinforce non-negotiable client requirements, but avoid duplicating general style guidelines already in artifacts.
  - **Adopt an "Outcomes-First" Mindset:**
      - **GrowthX is an outcomes company, not a content agency.** Our value is delivering growth (traffic, conversions) via software-enabled processes.
      - Content must be directionally correct and serve its goal (e.g., top-of-funnel awareness vs. bottom-of-funnel conversion).
      - The focus is on "solid, workmanlike content" that is factually correct and narratively sound, not on achieving literary perfection.
  - **Use LLMs for Specific Tasks:**
      - **Pipeline Builder:** A Claude project to help build or modify pipelines, offering contextual advice and suggesting best practices.
      - **Artifact Updater:** A Claude project to manage artifacts, check for conflicts, and ensure consistency.
      - **Article Editor:** A Claude project to perform precise edits, which can then be captured and used to improve pipeline workflows.

### Tool: The Convergence Report

  - **Purpose:** An experimental diagnostic tool in Flow Studio that helps identify why the agentic drafter is taking too long (e.g., \>10–15 minutes).
  - **Function:** It analyzes agent behavior (e.g., excessive loops, poor output quality) and suggests fixes for conflicting instructions or artifacts.
  - **Access:** Available in Flow Studio (not yet in the Atlas UI). A Slack link will be provided.
  - **Use Case:** A valuable tool for optimizing pipelines during setup or when troubleshooting slow runs.

### Admin: Holiday Planning

  - **Publishing Schedule:**
      - Publishing continues through the week of Dec 22.
      - No publishing from Dec 25–Jan 1.
  - **Content Generation:**
      - Front-load content generation now to cover the Dec 22 week if taking time off.
      - Publish extra articles per week in early December to build a buffer.
  - **On-Call Coverage:** EMs are coordinating a one-person-per-pod daily check-in during the quiet week.

---

## Action Items

**Matthew Panzarino (GrowthX)**
- Ensure EMs manage holiday expectations w/ clients; coordinate pod coverage Dec 25–Jan 1
- Share Slack link to Marcus's convergence report comment
- Distribute written agenda w/ links to team

---

## Transcript
**William Leborgne:** So quiet, I had to check my sound.

**William Leborgne:** Good morning, everybody.

**Nathan Navidzadeh:** Good morning.

**Kathy Lam:** Morning, William.

**William Leborgne:** Hi, Kathy.

**Marisol Smith:** Who's leading this?

**Kathy Lam:** Did you just volunteer me yourself?

**Marisol Smith:** No, no, no, no, no.

**Marisol Smith:** I don't.

**Marcus Derencius:** Is this the Friday meeting that we changed for Wednesday?

**Nathan Navidzadeh:** Yeah, think so.

**Marcus Derencius:** Nice.

**Marcus Derencius:** Well, any questions about the A-C-T-Pipeline?

**Marcus Derencius:** Did you check the convergence report in the draft step?

**Nathan Navidzadeh:** I have not.

**Nathan Navidzadeh:** Looking at the numbers, it's cool to see the new number feature that was added last week sometime, you can see how much time is spent in total for each run and all of that.

**Nathan Navidzadeh:** But the way that I run my pipelines right now, it like, it always looks really crazy, right?

**Nathan Navidzadeh:** Because I basically get it to draft a bunch of things on one day, and then the next day, or even the following day, I'm actually going in and making the post-processing edits.

**Nathan Navidzadeh:** So the timeline looks like three days per thing, you know?

**Nathan Navidzadeh:** Also, it doesn't capture where I actually do most of my work, which is before putting anything into the pipeline.

**Nathan Navidzadeh:** So generating the content structure, which is mostly done on Cloud for me.

**Nathan Navidzadeh:** So getting the outline ready, making sure the outline has all the keywords.

**Nathan Navidzadeh:** Bulk of my effort goes in there, kind of based on the philosophy of put something good in, you're going to get something good out.

**Nathan Navidzadeh:** So that's why we're always, I'm always kind of refining that.

**Nathan Navidzadeh:** It's also because of how I've been introduced to this, where we didn't have the agentic pipeline yet.

**Nathan Navidzadeh:** And so we had to focus most of our efforts.

**Nathan Navidzadeh:** So I'm still in a transition phase of figuring out what I can cut down on that initial process, and that will still produce something beautiful in the agentic pipeline.

**Nathan Navidzadeh:** So figuring that out.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Hi, everybody.

**Matthew Panzarino:** So, yeah, we'll talk about that a little bit, too, because I think people are spending a lot of effort there, and frankly, I think we need to reset our expectations around that.

**Matthew Panzarino:** But let's talk through some things first.

**Matthew Panzarino:** Let me work my way through an agenda this morning.

**Matthew Panzarino:** Good morning, everybody.

**Matthew Panzarino:** Let's go.

**Matthew Panzarino:** Let me pull up my agenda here.

**Matthew Panzarino:** Let's see.

**Matthew Panzarino:** Ah, I've got it.

**Matthew Panzarino:** It's amazing.

**Matthew Panzarino:** Okay, so a couple of things here.

**Matthew Panzarino:** We're going to dive into a handful of things.

**Matthew Panzarino:** So to do with working with the agentic pipelines and eliminating some inefficiencies here.

**Matthew Panzarino:** Last week, we talked about the mandatory baseline.

**Matthew Panzarino:** artifact conflicts, your editorial checklists, and kind of refining that process a little bit.

**Matthew Panzarino:** And so we're going to talk a little bit in this meeting about how you work with Atlas day to day.

**Matthew Panzarino:** There are several fatal mistakes that I see people making over and over.

**Matthew Panzarino:** I'm having a lot of one-on-ones.

**Matthew Panzarino:** I'm talking with people and kind of seeing a lot of the same things over and over.

**Matthew Panzarino:** So we're going to, I think, have a little discussion about some of the ways that you're using Atlas and other tools and kind of reset some expectations around that.

**Matthew Panzarino:** A quick recap of week one mandatory stuff.

**Matthew Panzarino:** Have you finalized the editorial checklist for every client?

**Matthew Panzarino:** Have you completed your operating manual for every client?

**Matthew Panzarino:** Have you run the conflict?

**Matthew Panzarino:** What checks and all your artifacts?

**Matthew Panzarino:** And are your assignment directions stripped back to a skeleton and tested from there?

**Matthew Panzarino:** If you haven't completed those, do that this week.

**Matthew Panzarino:** I don't want to go into the holiday period without all of these being completed for every account.

**Matthew Panzarino:** And then we'll talk about building up a little bit on that.

**Carrie Chowske:** Pansar, part of the reason I haven't done mine yet is that some of the accounts I got from previous managing editors haven't been done, so I've been having to figure things out.

**Carrie Chowske:** So there's not time for me to go back and do the ones that I'm no longer working on as a checklist.

**Carrie Chowske:** Like, should I just do the checklist then for my new ones?

**Matthew Panzarino:** Like, I don't, you see what I'm saying?

**Matthew Panzarino:** Like, I just, like, I haven't.

**Matthew Panzarino:** If you own the account currently, it's your task to get it done.

**Matthew Panzarino:** So if somebody else owns the account that you had before and they own it now, it's their responsibility.

**Matthew Panzarino:** If they have to ask you questions about that, then please be responsive and answer those questions.

**Carrie Chowske:** Okay, Mark.

**Matthew Panzarino:** Okay, holiday coverage.

**Matthew Panzarino:** Plan ahead for...

**Matthew Panzarino:** So, can your your holiday publishing schedule.

**Matthew Panzarino:** The expectation is that we have a quiet week between December 25th to January 1st, with no publishing.

**Matthew Panzarino:** But we are publishing the week of December 15th and December 22nd.

**Matthew Panzarino:** So, on the content generation stuff, it should happen this week or the week of December 22nd.

**Matthew Panzarino:** What this means for you, or through the week of December 22nd, what this means for you is if you're taking time off, get ahead on your content generation now to cover your out-of-office time.

**Matthew Panzarino:** You can publish extra articles per week, early December, to front-loads, you could have articles staged and ready for the week of December 22nd.

**Matthew Panzarino:** At Gnostic, that's obviously a client-facing, and EMs will manage that expectation with clients.

**Matthew Panzarino:** If you are going to be around, there's like a one-person-per-pod check Slack daily period during the quiet week, December 25th of January 1st.

**Matthew Panzarino:** If you have out-of-office, please coordinate with your EMs and understand who is going to be around to answer any questions.

**Matthew Panzarino:** The EMs mostly will be responsible for that, so this is likely not going to be your heavy lift. I'm just flagging for you that everybody should kind of talk with each other to make sure that that's good.

**Matthew Panzarino:** There is an expectation on the client side of a consistent delivery through December 22nd.

**Matthew Panzarino:** So, let's, you know, get going on that.

**Matthew Panzarino:** If you can't prepare two weeks ahead, your process will probably need some work, right?

**Matthew Panzarino:** So, reach out, let's figure it out.

**Matthew Panzarino:** But you've gotta get that stuff done so that everybody can have a chill holiday.

**Matthew Panzarino:** Okay, that's it on the holiday stuff. There is something I'll just call this out. I wanted to move this up, but it's down. Let me find it. Are you talking about the Atlas thing? I think we moved it. It's right after the holiday or right before something like that.

**Matthew Panzarino:** The 10th agenda is once again out of sync on my end.

**Andrew:** It's okay.

**Matthew Panzarino:** I just refreshed it and it appeared.

**Matthew Panzarino:** Okay, the convergence report, I just wanted to flag that really quickly.

**Matthew Panzarino:** So, Marcus worked on adding a convergence report to the agentic drafter.

**Matthew Panzarino:** What is this?

**Matthew Panzarino:** It basically is like an additional check, layer of checks that he added to the drafter.

**Matthew Panzarino:** It produces a report that you can view.

**Matthew Panzarino:** It's not exposed in the Atlas front end yet.

**Matthew Panzarino:** So, I would consider this to be an experimental advanced analytics tool that you can use to see what's going on with the pipelines.

**Matthew Panzarino:** There will be a link to this, to Marcus's comment on this in Slack, so you can see how to access it.

**Matthew Panzarino:** But long story short, you access it through Flow Studio, which is the platform that actually runs the workflows.

**Matthew Panzarino:** Atlas is a front end.

**Matthew Panzarino:** If you are unfamiliar, it's basically a website that accesses Flow Studio.

**Matthew Panzarino:** If you are unfamiliar, it's basically a website that accesses Flow Studio.

**Matthew Panzarino:** Flow Studio is what actually runs our workflows.

**Matthew Panzarino:** And the convergence report is designed to understand whether the agentic drafter is having trouble generating the draft because it encountered issues or conflicts, specifically with the instructions it's being given and the artifacts that it's using.

**Matthew Panzarino:** So it's basically like, hey, the drafter just took 25 minutes, and it shouldn't.

**Matthew Panzarino:** And I have some thoughts on why that is.

**Matthew Panzarino:** And that is currently in Flow Studio.

**Matthew Panzarino:** Eventually, I think it should be exposed in the Atlas front end, but it's kind of still an experimental thing.

**Matthew Panzarino:** But the idea is, if you are, if you're seeing drafting times that are above, I'm going to be loose here, let's use a range, but if it's above 10 to 15 minutes, that's on the outside.

**Matthew Panzarino:** Ademilade, by the way, drafters typically, if the instructions are given correctly, should take no more than a handful of minutes to run, you know, five minutes to eight minutes to actually run and generate an article, but if it is taking longer for whatever reason, maybe it's deep context, maybe you've got a ton of artifacts, maybe the artifacts are big, etc., there can be times where it exceeds a threshold and it says, hey, this is like having issues, right?

**Matthew Panzarino:** The draft workflow taking five plus loops through the agent process to actually execute.

**Matthew Panzarino:** The output quality is still poor.

**Matthew Panzarino:** If you're just doing an optimization pass on your pipeline, which we're all kind of doing right now in some ways, if you're setting up new pipelines, that kind of thing, you can jump in through the instructions that you'll see and you can look at it.

**Matthew Panzarino:** You can look at that report after the drafter has run in Flow Studio, and it will suggest a

**Matthew Panzarino:** A handful of fixes, like updating artifacts, tweaking your assignment directions, simplifying some complexity in your assignment directions, or artifacts or instructions elsewhere in the pipeline.

**Matthew Panzarino:** It basically is saying, hey, the instructions that the drafter was given are too complex, conflicting, or have issues, and you should take a look at those instructions and rectify them.

**Matthew Panzarino:** This would be very much the same as if a writer came back to you with a drafter, and you're like, how did you come up with this, and why did it take you so long?

**Matthew Panzarino:** And the writer's like, well, I don't know, you told me to do this, and you also told me to do this, and I was having a really hard time with those two things.

**Matthew Panzarino:** And you're like, oh, okay, okay, see, okay, just don't do this one, or maybe do it in this way.

**Matthew Panzarino:** And they're like, ah, got it, got it, this will be way faster now.

**Matthew Panzarino:** It's the same thing, right?

**Matthew Panzarino:** The agent has a rubric by which it judges its success, and it runs the task, judges itself against that rubric, and then performs any updates it needs to drive those scores higher.

**Matthew Panzarino:** If it has conflicting instructions or issues, it, of course, is going to labor at those tasks.

**Matthew Panzarino:** So this is one way to sort of pre-diagnose or at least allow it to raise its own hand and say, hey, I have some suggestions for you, right?

**Matthew Panzarino:** That's basically what it's doing.

**Matthew Panzarino:** So it's proactively saying, I don't know if you noticed, but like, you know, I'm having some issues and here's why, right?

**Matthew Panzarino:** That's the basic kind of premise of this.

**Matthew Panzarino:** It's just in the drafter step for now, Khalil.

**Matthew Panzarino:** We'll see if it happens, if it's necessary in other steps.

**Matthew Panzarino:** The drafter is really the issue largely with this kind of thing because it sets the kind of baseline that the rest of the pipeline works with.

**Matthew Panzarino:** Everything else is tweaking that draft.

**Matthew Panzarino:** So in order to establish a really solid draft, you know, that is kind of where it needs to be.

**Matthew Panzarino:** I'm pretty sure it does find stuff.

**Matthew Panzarino:** Is Marcus here?

**Matthew Panzarino:** Is Marcus with us?

**Matthew Panzarino:** Yes, yes.

**Matthew Panzarino:** Yeah, yeah, Marcus, go ahead.

**Matthew Panzarino:** You can chime in if you have anything that I said there that you think needs clarification.

**Marcus Derencius:** That's exactly that.

**Marcus Derencius:** It gets the drafter during the drafting process.

**Marcus Derencius:** It has large feedbacks on each attempt.

**Marcus Derencius:** And this report at the end is just summarizing the issues it had during the process and try to suggest how to improve the director or the writing guideline if it's hard to fulfill.

**Marcus Derencius:** So, yeah, give it a try and see.

**Marcus Derencius:** I can add that to Atlas.

**Marcus Derencius:** I just have to keep editing each pipeline to display the report at the end.

**Marcus Derencius:** So, but it's easy.

**Marcus Derencius:** It's right now in Flow Studio.

**Marcus Derencius:** You can easily go from Atlas to the Flow Studio and see that.

**Marcus Derencius:** But I can't include in the...

**Marcus Derencius:** As soon as I keep changing pipelines.

**Matthew Panzarino:** Yeah, and so to be clear, like, this was always possible, and I do it all the time for people, you know, when they come to me and they're like, oh, my pipeline, you know, what's happening?

**Matthew Panzarino:** I would generally go into the drafter run in Flow Studio and look at it, and like read through and parse it, but it's a lot, right?

**Matthew Panzarino:** And each step kind of dumps out, like, hey, here's the assessment, here's what my plan is to improve it, etc.

**Matthew Panzarino:** It does that for every rubric metric for every step and every iteration.

**Matthew Panzarino:** So it can be sometimes hard to collate out of there, okay, what's the underlying problem here?

**Matthew Panzarino:** And so this little synopsis diagnosis, whatever, is just basically helping people to understand a little bit better what's going on there.

**Matthew Panzarino:** So thanks, yeah.

**Matthew Panzarino:** I wouldn't, like, I wouldn't eat up cycles exposing in an atlas quite yet.

**Matthew Panzarino:** Like, because that does require manually editing pipelines across, you know, 40 clients or 60 clients and, you know, all that stuff.

**Matthew Panzarino:** I think this is a good diagnosis option when your runs are taking a long time and it's not hard to look at a flow studio.

**Matthew Panzarino:** So, for now, I think we're okay.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** I want to move on to a couple of other things.

**Matthew Panzarino:** Let's talk about some big mistakes that I think people are making.

**Matthew Panzarino:** One of them, and this is probably a big one, is taking your output out of Atlas into Cloud and then basically asking it to one-shot a new article.

**Matthew Panzarino:** I saw this happening a few times.

**Matthew Panzarino:** Be very, very careful about how you use Cloud or any LLM after Atlas has done its job.

**Matthew Panzarino:** It is absolutely fine for you to use those tools, but I would absolutely use those in a way that is precise.

**Matthew Panzarino:** Have it perform specific tasks for you, like the post-processing instructions that I've talked with many of you about how we developed the post-processing in Cloud and then use that as inspiration for

**Matthew Panzarino:** Or a post-processing checklist in Atlas, those tasks are usually great, but I have seen some instances of people basically dropping the entire article into Claude and saying, hey, I have like a standards of good, you know, golden path for our articles here, or I have existing articles that are good.

**Matthew Panzarino:** Could you rewrite this article to match those standards?

**Matthew Panzarino:** Why?

**Matthew Panzarino:** Like, why?

**Matthew Panzarino:** You know, like, if you were going to do that, just use Claude to write the article.

**Matthew Panzarino:** You know, there's, there's no reason to do that again, because you're just introducing a bunch of inconsistent things that you cannot track.

**Matthew Panzarino:** Because Claude can be really good today, and really crappy tomorrow.

**Matthew Panzarino:** And so you're never going to get consistent results out of it if you do that.

**Matthew Panzarino:** Even if it is helping you get your work done now, you need to stop and find a new way to get that work done that is more consistent.

**Matthew Panzarino:** the reason Atlas exists, and the reason that it is able to produce consistent results.

**Matthew Panzarino:** When used properly, it has these rails that Claude does not have.

**Matthew Panzarino:** It has expectations being given to it.

**Matthew Panzarino:** Claude is not an agent.

**Matthew Panzarino:** The default Claude chat is not an agent.

**Matthew Panzarino:** It has no rubric for success.

**Matthew Panzarino:** It builds a rubric on the fly when you just fire something off into it and does a deterministic process on it and then delivers it back to you.

**Matthew Panzarino:** It has no evaluations.

**Matthew Panzarino:** It has no loops there.

**Matthew Panzarino:** It has no rails.

**Matthew Panzarino:** And it lacks some of the context that the pipeline has.

**Matthew Panzarino:** In some cases.

**Matthew Panzarino:** And it can have things fall out of context where the agents in Atlas can recapture that context every time they make an evaluation.

**Matthew Panzarino:** So it's just bad practice.

**Matthew Panzarino:** If you're making adjustments in Claude, make sure that they are precise.

**Matthew Panzarino:** That you're adjusting things in a very specific way.

**Matthew Panzarino:** And, of course, as we have talked about before, make sure you're capturing those edits, capturing those failures that are basically like, hey, I wish this happened.

**Matthew Panzarino:** Let's see.

**Matthew Panzarino:** The pipeline, but it didn't, and then finding a way to articulate that either into your artifacts or assignment directions or into workflows that can be inserted into the pipeline.

**Matthew Panzarino:** So I think that's a big one.

**Matthew Panzarino:** So I think when you're going to take an article out of Atlas, your basic process should be that you are editing it manually first.

**Matthew Panzarino:** Like the first time you run anything out of Atlas, let's say that you take over an account, edit that thing manually.

**Matthew Panzarino:** This is my process.

**Matthew Panzarino:** I really strongly believe that it would benefit anybody, especially the first time that they're running a pipeline or delivering for a client.

**Matthew Panzarino:** Edit the first piece or two, three, whatever, first week, just edit it by hand.

**Matthew Panzarino:** What would I do to make this great?

**Matthew Panzarino:** And of course, you can use whatever tools you need to pull research or additional things.

**Matthew Panzarino:** I know sometimes citations, et cetera, you need to find one.

**Matthew Panzarino:** I'm not saying you can't use LLMs, but editing it manually yourself will tell you a lot about the quality of content.

**Matthew Panzarino:** And the quality of the pipeline, and how things are happening, and if you don't establish that baseline for yourself, it can be really difficult to understand where the issues lie, and you can basically be following somebody else's instructions that were already wrong, so if you have an operating manual for your account, and you're firing off stuff based on that, you shouldn't just take it that everything is going to be copacetic, evaluate for yourself, your editors, you're here for a reason, take a look at it, build the principles and understanding of how that content is being developed, and whether or not you like the quality.

**Matthew Panzarino:** And doing that pass can teach you a lot about what's missing, help you refine instructions that the pipeline is being given, either in the assignment directions, or artifacts, or even adding additional workflows.

**Matthew Panzarino:** Analyze the edits.

**Matthew Panzarino:** What's the same across multiple articles that I've edited?

**Matthew Panzarino:** Oh, these are the commonalities.

**Matthew Panzarino:** Are these style issues?

**Matthew Panzarino:** Put them in writing guidelines.

**Matthew Panzarino:** Is this a structural issue?

**Matthew Panzarino:** Update assignment directions.

**Matthew Panzarino:** Is it a factual issue?

**Matthew Panzarino:** Probably company I don't know.

**Matthew Panzarino:** Maybe research instructions.

**Matthew Panzarino:** Maybe a fact-checking pass.

**Matthew Panzarino:** So you've to feed those patterns back into the pipeline, otherwise it won't improve.

**Matthew Panzarino:** And yes, exactly, Nathan, you absolutely can edit directly in Atlas.

**Matthew Panzarino:** There's no reason you have to go out to Google Docs to do those passes.

**Matthew Panzarino:** And eventually, very soon, because Nathaniel's working on it hard, any of those edits that you make will basically result in a report that says, hey, you've been editing these things a lot.

**Matthew Panzarino:** Here's some suggestions for you on how to improve this.

**Matthew Panzarino:** the artifacts.

**Matthew Panzarino:** Or maybe even hopefully at some point automatically improving the artifacts or assignment directions.

**Matthew Panzarino:** And Atlas can do that for you.

**Matthew Panzarino:** So might as well get in the habit now.

**Matthew Panzarino:** The mental model is Atlas is your writer, your junior writer, that will follow your instructions fairly literally and does not really understand metatextual philosophy.

**Matthew Panzarino:** So your job is to give it better instructions until it improves at its task.

**Matthew Panzarino:** And your job is not to take that junior writer's output and give it to another dumber junior writer and have it rewrite the entire thing, right?

**Matthew Panzarino:** Like, that is, it's like, think of that model and adjust accordingly.

**Matthew Panzarino:** So, please, if your current process includes, now take the article from Atlas, drop it into Claude, and one-shot me a new article, reset.

**Matthew Panzarino:** So, number one.

**Matthew Panzarino:** Number two, over-engineered assignment directions.

**Matthew Panzarino:** Right now, people are putting in incredibly detailed briefs into assignment directions.

**Matthew Panzarino:** I'm just going to tell you, it's probably causing you more issues than it's solving.

**Matthew Panzarino:** If you're having outputs that come out of Atlas with incredibly detailed assignment direction, and you're able to edit those articles within 15 minutes and deliver them to client reliably every time, then ignore me.

**Matthew Panzarino:** But I guess...

**Matthew Panzarino:** I guarantee you that most of those people that are having issues editing articles for 90 minutes, 120 minutes, longer, after they come out of Atlas, are trying to fix the problem by giving it more and more detailed assignment directions, and they're just shooting toes off, one by one.

**Matthew Panzarino:** Like, you're really, that's not the way that these pipelines operate.

**Matthew Panzarino:** It's just not the way that they work.

**Matthew Panzarino:** The agents know SEO best practices and principles.

**Matthew Panzarino:** They were built, the agentic drafter was built from the ground up to understand SEO best practices.

**Matthew Panzarino:** You do not have to babysit the agentic drafter in telling it how to insert keywords into an article.

**Matthew Panzarino:** Amongst all the things that we have to tell the drafter how to do better, that is one you do not have to tell it to do better.

**Matthew Panzarino:** Now, if you have very specific ideas about what you want each H2 or H3 to be, hey.

**Matthew Panzarino:** time, everyone.

**Matthew Panzarino:** Ladies.

**Matthew Panzarino:** That sounds like a human edit problem.

**Matthew Panzarino:** Get everything else done, get best principles in, get in a great solid draft out, and then spend your 15 minutes tweaking the headlines to be nice, right?

**Matthew Panzarino:** According to your mouthfeel.

**Matthew Panzarino:** But trying to one shot all that stuff into assignment directions and hoping for the best and kind of adding additional detail when you're like, oh, if only it did this, this, and this, and this, and this, and this, and this, is going to cause you more problems than you're going to have if you don't.

**Matthew Panzarino:** So if you have problems right now editing stuff because of adherence issues, I would highly, highly encourage you, in fact, say you pretty much must at least try, try, run a few rows with this philosophy, creating a generic version of any outline or structure that you've already done.

**Matthew Panzarino:** And you can take the one, so I know that you've all read articles with detailed outlines, I've seen them, take those, ask Claude, you can use Claude, or you can write it yourself, but you can say, hey, I'd like a relatively standardized, generic version of these kinds of outlines that offer some flexibility, because these articles aren't templatized, unless they are, in which case, you know, you should just have a template in there.

**Matthew Panzarino:** And pop that in.

**Matthew Panzarino:** And I'm talking about, like, hey, introduction, cover this basic stuff in the introduction.

**Matthew Panzarino:** Cool, thank you.

**Matthew Panzarino:** Body, write a few paragraphs of good stuff about XYZ.

**Matthew Panzarino:** And then conclusion, hey, write a nice punchy conclusion.

**Matthew Panzarino:** And then just give it that.

**Matthew Panzarino:** Because right now, what you're doing, in many cases, is you're giving it an impossible task.

**Matthew Panzarino:** You're giving it a list of, like, dozens of constraints.

**Matthew Panzarino:** Specific word count.

**Matthew Panzarino:** C pallox per section.

**Matthew Panzarino:** Not ranges.

**Matthew Panzarino:** Specific word counts per section.

**Matthew Panzarino:** Asking for eight or seven complex ideas in 150 words.

**Matthew Panzarino:** If you ask a human writer to do that do you think it will take longer to do that than to just write what they think is a good introduction?

**Matthew Panzarino:** Absolutely.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** It forces bad writing, weird compound sentences, awkward punctuation.

**Matthew Panzarino:** Sometimes the M dashes and colons exist because you are asking it to do gymnastics.

**Matthew Panzarino:** You are saying hey, I want these six ideas in these three sentences.

**Matthew Panzarino:** And it's like, okay, cool, I can do that.

**Matthew Panzarino:** I have to make them compound, massively so, right?

**Matthew Panzarino:** And that's, then you're having to go back and edit all those out, because you're like, oh, man, what's all these compound sentences?

**Matthew Panzarino:** What's this all X then Y, if not Y then X?

**Matthew Panzarino:** It's because that's how it fits complex ideas into shorter sentences.

**Matthew Panzarino:** Because all too often, our writing guidelines are like, hey, be concise.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** I'll be concise.

**Matthew Panzarino:** Concise, to me, is one sentence, but it's one sentence with six ideas in it, right?

**Matthew Panzarino:** So, I think it's important that you reset there.

**Matthew Panzarino:** It'll also affect generation times, right?

**Matthew Panzarino:** Because it's going to try to reconcile all those contradictions and those crazy requirements in such short spaces.

**Matthew Panzarino:** So, give it a framework.

**Matthew Panzarino:** Give it word ranges instead of exact counts.

**Matthew Panzarino:** Create, like, goals from that outline rather than specific tasks.

**Matthew Panzarino:** And then let the agentic system work.

**Matthew Panzarino:** I think a lot of this basically came from using either the deterministic workflows, the ones we were using previously before the agentic workflows, where you had to give them a lot of very explicit tasks because they were a deterministic process versus an agentic process.

**Matthew Panzarino:** And that means that they performed a list of tasks in a row and then fired that off into the next step.

**Matthew Panzarino:** They did not think about the consequences.

**Matthew Panzarino:** did not think about whether that actually adhered to the tasks that you had given it.

**Matthew Panzarino:** They just did it and ran.

**Matthew Panzarino:** So the agentic workflows work differently, and I believe that we are giving them bad raw material in many cases.

**Matthew Panzarino:** Your assignment directions, and I'm not being arbitrary about this, please, but understand that in general, they should be pretty damn short.

**Matthew Panzarino:** Like, they should not be pages and pages of assignment directions.

**Matthew Panzarino:** You should not be scrolling for several seconds in that field.

**Matthew Panzarino:** It's just not, it's not going to be good.

**Matthew Panzarino:** It's not going to be a good prompt, because that's what it is.

**Matthew Panzarino:** It's a prompt.

**Matthew Panzarino:** So think about the last prompt you wrote.

**Matthew Panzarino:** How long was it?

**Matthew Panzarino:** I guarantee you, it was, it probably wasn't 3,000 words, right?

**Matthew Panzarino:** So be careful about that.

**Matthew Panzarino:** Reset your expectations around that structure.

**Matthew Panzarino:** You can give it a handful of basic instructions, a rough framework, and then let it run.

**Matthew Panzarino:** I think that bad.

**Matthew Panzarino:** behavior also just comes from the fact that if you were to do this in Claude, would probably need to write something that long.

**Matthew Panzarino:** But you don't.

**Matthew Panzarino:** Any questions about that before I move on to the next step?

**Matthew Panzarino:** Gabby?

**Gabrielle Brogan:** Hi, yeah.

**Gabrielle Brogan:** When you're kind of mentioning about reducing the amount of text in the assignment direction, does that include kind of what's automatically pre-populated in there?

**Matthew Panzarino:** Or are you more referring to assignment directions that we would be adding on top of that?

**Matthew Panzarino:** Yeah, good question.

**Matthew Panzarino:** So the pre-population is only a quality of life thing.

**Matthew Panzarino:** So nothing technically has to be pre-populated in there.

**Matthew Panzarino:** Or you can have as much as you want pre-populated in there.

**Matthew Panzarino:** So as an example, if you're writing stuff for a client where every row you run has a pretty different structure.

**Matthew Panzarino:** Like let's say you're running like two or three different kinds of articles through there.

**Matthew Panzarino:** You can do one of two things.

**Matthew Panzarino:** You can either adjust that pre-fill.

**Matthew Panzarino:** Lisbon.

**Matthew Panzarino:** can one

**Matthew Panzarino:** Daniel To where it has a blank spot for structure that you can sort of like type in or have a template that you paste in and it says like, hey, do this kind of article this time and maybe the next row I'm going to do a different kind of article.

**Matthew Panzarino:** You can absolutely do that.

**Matthew Panzarino:** That section is just text.

**Matthew Panzarino:** And in the code of the pipeline, you can type whatever you want in that section of the text.

**Matthew Panzarino:** So it can just be blank.

**Matthew Panzarino:** It can be, you know, a seaming structure every time.

**Matthew Panzarino:** It can have insertion points for you to fill.

**Matthew Panzarino:** Daniel your choice.

**Matthew Panzarino:** If you are doing, let's say, dozens of articles in one kind of format or structure or type, let's call it like listicles or editorial or whatever, right?

**Matthew Panzarino:** You can do a pipeline for that.

**Matthew Panzarino:** And then you can just copy that pipeline and then create a new set of pre-filled instructions for a different kind.

**Matthew Panzarino:** So you have two pipelines.

**Matthew Panzarino:** One is your listicles pipeline.

**Matthew Panzarino:** One is your, you know, standard editorial top of funnel pipeline.

**Matthew Panzarino:** is Familydy if that's the easy way to order

**Matthew Panzarino:** And it for you, that's fine.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** Like, the pipelines are not some sort of, like, weird stone tablet thing.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** They just, they exist as a set of instructions to call workflows.

**Matthew Panzarino:** So you can say, you know what, I want a new set of instructions for this task.

**Matthew Panzarino:** And as long as it's clear, and of course, you update that in your operating manual so people know which pipelines to use for what, that's fine.

**Matthew Panzarino:** And then you can pre-fill whatever you like in there.

**Matthew Panzarino:** And the pre-fill is, once again, a quality of life thing.

**Matthew Panzarino:** And you could easily have it blank and then paste or type in there every time, if that's what you want.

**Matthew Panzarino:** But generally speaking, there's a handful of things that are useful to have in there, kind of setting up some expectations for it.

**Matthew Panzarino:** Sometimes it is nice to reinforce a handful of things in there or to test reinforcements in there.

**Matthew Panzarino:** So you can say, hey, it's really critical that you do this.

**Matthew Panzarino:** The client really needs this or really, you know, hates this, et cetera.

**Matthew Panzarino:** It's okay to reinforce things there, even things that also appear in writing guidelines.

**Matthew Panzarino:** And many of them currently do.

**Matthew Panzarino:** You know, I see things like word count as one example.

**Matthew Panzarino:** In...

**Matthew Panzarino:** And assignment directions, no problem, right?

**Matthew Panzarino:** You can absolutely have like, hey, I would like this article to be between 1,000 and 1,200 words, just as an expectation set right at the top.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** However, make sure that that word count is the exact same one that's in your writing guidelines.

**Matthew Panzarino:** Otherwise, it will have a conflict, even if it's similar.

**Matthew Panzarino:** I saw one the other day that was like, hey, write an article between 1,000 and 1,200 words.

**Matthew Panzarino:** And in the writing guidelines, it says write a 1,200 word article.

**Matthew Panzarino:** And it was like, I don't know which of these to follow, right?

**Matthew Panzarino:** And it was having issues, basically.

**Matthew Panzarino:** So, I think it's important that adherence, you know, that continuity is present, but you can basically create whatever you want in there.

**Gabrielle Brogan:** Thank you.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah, Victor, no problem.

**Matthew Panzarino:** You can review the recording later.

**Matthew Panzarino:** See ya.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Any other questions on that section?

**Matthew Panzarino:** Does that make sense to everybody?

**Matthew Panzarino:** I mean, I understand that you have definitely gone down this path and you're like, man, I'm seeing some good results from like putting a lot of detail in there.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Thank

**Matthew Panzarino:** I get it.

**Matthew Panzarino:** It's probably a placebo.

**Matthew Panzarino:** Like you're probably getting close to where you want to be, but then you're still probably doing a decent chunk of editing on the back end.

**Matthew Panzarino:** You know, and that would be my guess.

**Matthew Panzarino:** And I would say experimenting with this is one of those things where it's really a couple of minutes of your time to set up a handful of rows and run them with a basic framework and then come back to it later and compare it to the outputs that you're getting from your detailed framework and see where you're at.

**Matthew Panzarino:** And I think you'll be shocked.

**Matthew Panzarino:** Yeah, Nathan.

**Nathan Navidzadeh:** So my usual process is building a big outline, right?

**Nathan Navidzadeh:** Which is because of the deterministic pipelines that we used to run.

**Nathan Navidzadeh:** That's how we would do it, right?

**Nathan Navidzadeh:** So I go as in detail.

**Nathan Navidzadeh:** So I want to compare, okay, this is what I do for deterministic, paring this down for a gentick.

**Nathan Navidzadeh:** What does that look like?

**Nathan Navidzadeh:** You talked about changing from a bunch of tasks to give it to giving it a goal instead, for example.

**Nathan Navidzadeh:** So what I currently do is I get essentially a full outline that I've looked over.

**Nathan Navidzadeh:** I'll probably spend about half hour building that's got the headings essentially to the point that I want from H2s to H3s and that each H2 section, each H3 section also has either bullet points or writing guidelines, you know, like two, three sentences worth that describe what I want that section to cover with the topics that I want it to cover.

**Nathan Navidzadeh:** I also do have a word count assigned to each H2 section, each H3 section, and the full outline, and those usually work well together.

**Nathan Navidzadeh:** I don't have any word count stuff in the writing guidelines or artifacts, but that's really helpful to know because with the deterministic one, sometimes it does go over the word count, and that's fine.

**Nathan Navidzadeh:** I can do little edits, but if it's going to cause issues in the agentic one because of just trying to get it back down to that and then adding all these M dashes and stuff to try to really condense it, then that was really good to know.

**Nathan Navidzadeh:** But what I want to know is the amount of detail that I'm going to provide for an agentic assignment direction, is it still okay to provide a heading, for example?

**Nathan Navidzadeh:** Have you seen success where...

**Nathan Navidzadeh:** Where, like, the headings are provided, the H2s, the H3s, and what they should be covered, instead of the goal of it?

**Matthew Panzarino:** Or, um...

**Matthew Panzarino:** Yeah, you can, look, you can.

**Matthew Panzarino:** I just, you don't need to.

**Matthew Panzarino:** Like, I don't know how many times I say this, but, like, the, you absolutely can.

**Matthew Panzarino:** And, like, if the, if the client, I'm going to talk about something else in just a second.

**Matthew Panzarino:** It wasn't on the agenda, but I think it's important to, to establish for everyone.

**Matthew Panzarino:** But it's, I think, important, like, if the client is saying, like, I really want X, Y, or Z, and it's hyper-specific, yeah, like, pair that down to the, the nut of, like, what you want and put one sentence in.

**Matthew Panzarino:** And it says, make sure this covers this stuff in this section, you know, in addition to whatever else you are going to cover.

**Matthew Panzarino:** And just like you would, like, sketch out for a writer, like, hey, they really, you know, if they, if we don't have these things in there, they're going to be pissed, right?

**Matthew Panzarino:** Like, that's fine.

**Matthew Panzarino:** I get it.

**Matthew Panzarino:** I would actually say, though, I would be shocked if you gave it a topic and you actually...

**Matthew Panzarino:** If that topic properly, like it's a well-written title and not just like a random set of keywords, and you gave it a rough structure and it didn't cover those things.

**Matthew Panzarino:** You know what I mean?

**Matthew Panzarino:** Like it's probably going to cover those things because I highly doubt in most cases that they're not going to be like best principles stuff to cover.

**Matthew Panzarino:** Like it's very rare, I would say.

**Matthew Panzarino:** And now if it is something where they have a hyper-specific thing where they're like, our conclusion must mention that we are not FDA, whatever, you know, you can put it in there.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Like, you know, make sure it's in there.

**Matthew Panzarino:** I get it.

**Matthew Panzarino:** So I'm not like trying to be super arbitrary about the way these look or feel.

**Matthew Panzarino:** And I can show you some examples of ones and I'm sure other folks can show examples of ones where they've used relatively skeletal ones and they're like, hey, this is producing pretty good results.

**Matthew Panzarino:** However, it's not, I don't want to like get too heavy-handed with this because I know that clients have specific needs and unfortunately some of their expectations are weird and hyper-specific and don't know just

**Matthew Panzarino:** Stakeholders just don't get that this is about growth and not, you know, Shakespeare.

**Matthew Panzarino:** So I understand that you have some specific needs.

**Matthew Panzarino:** So I'm not saying you can't do that.

**Matthew Panzarino:** But it's going to save you hours every week not pre-writing the article and putting it in there.

**Matthew Panzarino:** Because basically you've already rewritten the article.

**Matthew Panzarino:** All you need to do is fill out some adverbs, right?

**Matthew Panzarino:** And, like, I think that that's, like, not necessary to do with the agentic pipelines at all in order to get solid results out of it.

**Matthew Panzarino:** And it will save people an enormous amount of time and help you build leverage.

**Matthew Panzarino:** Which dovetails into this thing, which I'm going to insert into this agenda before I move on to the next salient point.

**Matthew Panzarino:** But this is an issue for the company at large.

**Matthew Panzarino:** And so leadership is aware of it.

**Matthew Panzarino:** we're talking about it.

**Matthew Panzarino:** But I want to kind of let you know, like, your EMs are going to have instructions about how we set expectations with

**Matthew Panzarino:** And those expectations are around outcomes.

**Matthew Panzarino:** Like, GrowthX is not a content agency.

**Matthew Panzarino:** Just putting that out into the ether.

**Matthew Panzarino:** Like, we are not a content agency.

**Matthew Panzarino:** We are an outcomes, a software-driven outcomes company.

**Matthew Panzarino:** In other words, we go to these clients and we say, we are going to provide growth for you in the form of organic traffic, top-funnel, mid-funnel, conversions, et cetera.

**Matthew Panzarino:** How we achieve those goals is, generally speaking, through some sort of content or, in many cases, projects like directories, programmatic efforts, websites, et cetera.

**Matthew Panzarino:** Our job is to provide growth through software-enabled processes.

**Matthew Panzarino:** It is not to write content for you.

**Matthew Panzarino:** And the problem with that expectation of like...

**Matthew Panzarino:** Like, oh, these people write us content, is that then they're like, let me read all the content and get really specific about the content.

**Matthew Panzarino:** Hey, no.

**Matthew Panzarino:** Like, A, you are probably not good at content.

**Matthew Panzarino:** That's why you hired us.

**Matthew Panzarino:** Otherwise, you would do it yourself.

**Matthew Panzarino:** But B, most people get lost in the sauce very rapidly and kind of get obsessed with how a certain thing is said or how a certain thing is positioned or really hyper-specific, like, requirements on the way content is presented.

**Matthew Panzarino:** And they lose the track of the fact that it's like, hey, we can do those things, but guess what?

**Matthew Panzarino:** It's either not going to change the performance at all or it'll probably be less performant because you don't know what you're doing.

**Matthew Panzarino:** And so, like, I think it's just an expectation-setting thing, but I would think of it in similar ways where you want to make sure that your content is directionally correct, that it's driving towards the goal that the client has.

**Matthew Panzarino:** So if that's bottom of funnel, like, you know, make sure it's specific and it has the right tone for a piece of bottom of funnel content that is supposed to drive conversions, you're like driving towards messaging that says, hey, this client's tool is necessary to solve this problem, et cetera.

**Matthew Panzarino:** And of course, if it's top of funnel, it's broad interest, et cetera, that's pretty much hit pocket.

**Matthew Panzarino:** The agentic pipeline is really good at that stuff.

**Matthew Panzarino:** But the Shakespearean ethos has to stop, right?

**Matthew Panzarino:** And that's for everybody.

**Matthew Panzarino:** That's for all of you.

**Matthew Panzarino:** And that, of course, has to translate through to the EMs and client expectations and, of course, into our sales process.

**Matthew Panzarino:** Like, people have to come into this and through the sprint understanding this.

**Matthew Panzarino:** So just know that there are other people on this task, not just you.

**Matthew Panzarino:** But it also is important to remember, like, we are driving towards goals here.

**Matthew Panzarino:** Get the content out.

**Matthew Panzarino:** Like, we're not writing the most wonderfully phrased content in the entire universe.

**Matthew Panzarino:** That's not our job, but we are writing workmanlike content that serves the goal, that does not abuse the reader, you know, that drives towards best principles and practices and is not clickbait in all senses of the term.

**Matthew Panzarino:** It's solid stuff that provides a real chance of growth for the client.

**Matthew Panzarino:** And I think that is a good expectation to set up for yourself because given that we're all content people, we're all creativists, we're all writers, we are absolutely going to hold ourselves to higher standards.

**Matthew Panzarino:** And you're going to look at it and you're going to be like, oh my God, right?

**Matthew Panzarino:** And you're going to see some instructions from me now and then where it's like, hey, these things are egregious, et cetera.

**Matthew Panzarino:** A lot of it really is correcting the foibles of LLMs, right?

**Matthew Panzarino:** And just the way that they interpret pattern matching in the human language and because of their ingestion model.

**Matthew Panzarino:** However, I think it's important to be like, let us reset, right, around this.

**Matthew Panzarino:** And given that some of our clients who have been with us for a year or so,

**Matthew Panzarino:** Like, have different expectations.

**Matthew Panzarino:** It is going to be a struggle with some of those to reset those expectations, but, you know, that's, the EMs are going to be given this task.

**Matthew Panzarino:** The directors will be given this task.

**Matthew Panzarino:** Like, we're going to have to sort of jostle with that a bit, and we're going to have to fire some clients, to be honest, you know?

**Matthew Panzarino:** So it is what it is.

**Matthew Panzarino:** But just so you know, like, the expectation is solid workmanlike conduct that drives towards a goal, and of course, is fundamentally sound.

**Matthew Panzarino:** We don't want to produce trash.

**Matthew Panzarino:** We want to produce quality stuff, but it does not have to be, like, the most eloquent thing that has ever been produced.

**Matthew Panzarino:** That is not its task, right?

**Matthew Panzarino:** Nobody's reading it like that.

**Matthew Panzarino:** Nobody's consuming it like that.

**Matthew Panzarino:** They're saying, did this honor its promise to me?

**Matthew Panzarino:** Did the title and introduction and promise of the, even the slug, did it drive towards that?

**Matthew Panzarino:** Did it give me what I wanted?

**Matthew Panzarino:** Did it actually compare these things reliably?

**Matthew Panzarino:** Did it actually present me factually correct information?

**Matthew Panzarino:** Did it do it in a narratively sound way that didn't make me want to tear my eyeballs out, right?

**Matthew Panzarino:** And yeah, you know, the language can get florid, it can get convoluted, it can get, you know, and stakeholders matter, right?

**Matthew Panzarino:** Like the exact person on the other side of that call on the EM's call can matter.

**Matthew Panzarino:** And we're resetting expectations around that too, you know, because it's like, hey, do we have the right person in your org?

**Matthew Panzarino:** To run this?

**Matthew Panzarino:** Or is it a person who's like, you know, I did creative writing, and, you know, I minored in creative writing, and now I'm in marketing, and I wish I was a novel, I wish I was an author.

**Matthew Panzarino:** And this is how I get my editor wiggles out, right?

**Matthew Panzarino:** And so like, there's massive difference between that, and I've spoken to both these types.

**Matthew Panzarino:** There's a massive difference between that and the CEO who's like, my investor is breathing down my neck about my margins and about my growth, and I want results.

**Matthew Panzarino:** And I...

**Matthew Panzarino:** really don't give a , pardon my language, but there's a delta there and we need to land somewhere in between because we do care.

**Matthew Panzarino:** We do give everything, right?

**Matthew Panzarino:** We want it to be good, but it also does not need to land at the end of the spectrum where it's like every letter of this has been examined and, you know, the quill pin has come out, right?

**Matthew Panzarino:** So, you know, yeah, Natalie, so many of us frustrated authors, et cetera, you know, I've probably written, I've probably written hundreds of books, but nobody's ever read it because it was all editorial letters to my staff, you know, but anyhow, long story short, I just want to like put that out into the ether as well.

**Matthew Panzarino:** When you're thinking about all of your processes, process it through that lens.

**Matthew Panzarino:** Like, am I just doing too much in the colloquial sense?

**Matthew Panzarino:** Like not in the actual sense, know, do the work, but am I just getting extra with this process for no reason?

**Matthew Panzarino:** Because the pipelines themselves.

**Matthew Panzarino:** Do already understand the fundamentals of SEO, and in some shades already Geo, although we are going to get, you know, better at that.

**Matthew Panzarino:** The pipelines will get better at that.

**Matthew Panzarino:** They'll have additional rules in there.

**Matthew Panzarino:** The good news is that they're mostly adherent already, but there will be some things and learnings that we have, especially now that we have checked that, of course, but now that we have that and we are gathering data about what prompts in, you know, work and what content surfaces for prompts, all of that knowledge will be fed back into the pipelines and they will get better at writing geo-visible content as well as SEO-visible content.

**Matthew Panzarino:** But I'm going to tell you, they're probably already better at SEO than most of us are.

**Matthew Panzarino:** And on an individual basis, you may be better than the pipeline.

**Matthew Panzarino:** I just want put that out there.

**Matthew Panzarino:** I firmly believe that.

**Matthew Panzarino:** Otherwise, why are you here?

**Matthew Panzarino:** On an individual basis, with any piece, you may be better at saying like, Oh, for this H3,

**Matthew Panzarino:** Maybe this is going to play better for SEO or whatever.

**Matthew Panzarino:** But you can't do that dozens of times a week at speed.

**Matthew Panzarino:** It's just not possible.

**Matthew Panzarino:** Like, if I give you 60 hours of work and I ask you to work 40 hours, you're going to be mad, right?

**Matthew Panzarino:** You're going to be frustrated, you're going to feel overworked, you're going to feel like you're under-delivering.

**Matthew Panzarino:** The answer is, let the pipeline do the work.

**Matthew Panzarino:** Like, you are probably doing a lot of work that the pipeline can do for you and can do it well enough to meet the goals of the client.

**Matthew Panzarino:** So, I think that's a lot of the stuff that I'm talking about here, like, theme-wise, is along the same vein.

**Matthew Panzarino:** That's the only reason I'm kind of, like, mentioning that.

**Matthew Panzarino:** Like, pre-writing articles and then distilling an outline out of those articles and then putting that outline into assignment directions.

**Matthew Panzarino:** Taking an article out of Atlas and essentially rewriting the entire thing with prompts, you know, things like that.

**Matthew Panzarino:** let's If You're

**Matthew Panzarino:** If you are rewriting the article entirely because it's so off, then there's a problem from the get, right?

**Matthew Panzarino:** Like if you were, if somebody built a car and you had 8, 9, 10, 11 issues, that's why we have the Lemon Law.

**Matthew Panzarino:** You take it back to the dealer and say, give me a new car.

**Matthew Panzarino:** So if you run something through the pipeline and you have to spend hours editing it, you probably just need to ask the outline or ask the pipeline to do it again.

**Matthew Panzarino:** And perhaps give it better instructions to do that job, right?

**Matthew Panzarino:** So reset expectations around like how much time you want to spend with everything there.

**Matthew Panzarino:** Okay, let me move on to a couple other things because I want to get through a couple more items.

**Matthew Panzarino:** Let me look here.

**Matthew Panzarino:** What's important before we wrap up?

**Matthew Panzarino:** I'm going to distribute once again, I'll do one of these agendas with appropriate links and all of this kind of like written.

**Matthew Panzarino:** In written form after this call.

**Matthew Panzarino:** So you'll get that later today.

**Matthew Panzarino:** And in there, we kind of put an ideal workflow of like an end-to-end process of like, okay, what should it actually look like?

**Matthew Panzarino:** I'm also working on an editorial runbook for the editorial workstreams.

**Matthew Panzarino:** And that will basically be like in Zapruder-like detail.

**Matthew Panzarino:** What is my job?

**Matthew Panzarino:** Like, what does it look like?

**Matthew Panzarino:** And you can look through there.

**Matthew Panzarino:** And of course, put it out there.

**Matthew Panzarino:** Some sections may not apply to you particularly because of what you're doing or what your client expects or whatever.

**Matthew Panzarino:** But it's sort of like, what is the detail of everything here, right?

**Matthew Panzarino:** What should I be doing?

**Matthew Panzarino:** And the ideal workflow looks something like create an assignment in Atlas with a clean topic, human-readable topic and title.

**Matthew Panzarino:** I just say write a title.

**Matthew Panzarino:** Once again, if it does not adhere to the writing guidelines, don't write it as a topic.

**Matthew Panzarino:** So if you're writing guidelines, say no colon.

**Matthew Panzarino:** Don't put a colon in your topic.

**Matthew Panzarino:** Because that's...

**Matthew Panzarino:** That's part of the prompt, and then we'll confuse it, right?

**Matthew Panzarino:** Basic structure framework, research priorities.

**Matthew Panzarino:** You can absolutely give the researcher tasks.

**Matthew Panzarino:** Please research these three things.

**Matthew Panzarino:** Super important for this article.

**Matthew Panzarino:** Thank you, right?

**Matthew Panzarino:** Totally fine to include in article directions.

**Matthew Panzarino:** You don't need to.

**Matthew Panzarino:** It'll probably get it.

**Matthew Panzarino:** But if you really want to make sure that a researcher has a particular topic or a particular thing worked well, you can include it in there.

**Matthew Panzarino:** And then some non-negotiable client-specific stuff to reinforce.

**Matthew Panzarino:** What not to include.

**Matthew Panzarino:** Detailed outlines with exact word counts with no ranges.

**Matthew Panzarino:** Sentence-by-sentence instructions.

**Matthew Panzarino:** Everything that you already put in writing guidelines does not need to be duplicated in there.

**Matthew Panzarino:** It's fine to reinforce some big important points, but don't go crazy.

**Matthew Panzarino:** The pipelines already have all these best practices built in.

**Matthew Panzarino:** They were designed to do good SEO writing.

**Matthew Panzarino:** That's what they do.

**Matthew Panzarino:** Then you run the pipeline.

**Matthew Panzarino:** Don't intervene necessarily unless you need to.

**Matthew Panzarino:** Take that output, either edit it in Atlas or in Google Docs.

**Matthew Panzarino:** See what you're changing.

**Matthew Panzarino:** Build lists of things that you would love to see improved.

**Matthew Panzarino:** Analyze those changes, style, structure, content, compliance.

**Matthew Panzarino:** Where do these belong?

**Matthew Panzarino:** And then update your artifacts or your assignment directions.

**Matthew Panzarino:** Or, of course, file a ticket if you need to.

**Matthew Panzarino:** Say, hey, this pipeline is not doing this really complex weird thing.

**Matthew Panzarino:** I'm really not sure where to put this.

**Matthew Panzarino:** I would love to know if this is a good recipe for an additional workflow, etc.

**Matthew Panzarino:** And then we'll feed it back into the pipeline.

**Matthew Panzarino:** So then there's an improvement in the pipeline.

**Matthew Panzarino:** If they're stylistic, it's probably writing guidelines.

**Matthew Panzarino:** If it's structure-based, it's probably assignment directions.

**Matthew Panzarino:** If there are specific tasks that you need accomplished on that article and you're doing those tasks manually every time, maybe a post-processing workflow, right?

**Matthew Panzarino:** Editorial checklist that just checks on those things.

**Matthew Panzarino:** So I think that's important.

**Matthew Panzarino:** You'll see this basic structure.

**Matthew Panzarino:** We'll get more detailed about it, but I just want to set some expectation, especially because we have a lot of new folks, and I know many of you have asked me, like, wait a minute, like, okay, what is it like to do this job?

**Matthew Panzarino:** Like, what is the operating thing?

**Matthew Panzarino:** And we just haven't had a lot of documentation about that, so I'm making sure that we have some written forms of it that are easy for you to look at and reference and understand.

**Matthew Panzarino:** I also want to just take a moment here to, like, honor Claude, because I've talked a lot about, like, don't try and rewrite your articles or one-shot stuff, but it can be and is a very useful tool in many, many ways.

**Matthew Panzarino:** And so I don't want you to think that you can't use LLMs, custom GPTs, Claude, et cetera.

**Matthew Panzarino:** There are absolutely uses for it.

**Matthew Panzarino:** Like, a handful of really primary use cases, the pipeline builder, like, you should probably have a pipeline builder project that helps you to either build or recompose pipelines.

**Matthew Panzarino:** Like the one that Gabby mentioned as an example, she could take the existing pipeline, she could say, hey, I'd love this new pipeline to be pre-filled with a structure of this kind of article, and here's that structure, so give it the pipeline, give it the structure, in a pipeline builder, and that pipeline builder, by the way, is very simple, it's just a cloud project with some basic instructions about what those pipelines look like, and the best practices, and we have one set up, and we have some examples of what that should look like for you, so you will be able to see it and reference it.

**Matthew Panzarino:** You can check that in our podf account as well, of course, in cloud, so you can always take a gander at that, the way we do it, if you need inspo.

**Matthew Panzarino:** But once it understands what the pipelines look like, it could do so many cool things for you, because it can give you contextual advice about how you're applying these instructions, or in what order you are applying the instructions, and tell you, hey,

**Matthew Panzarino:** Hey, you're establishing a standard in writing guidelines that's probably going to be screwed up by this post-processing step that you have here, so maybe you want to swap these, right?

**Matthew Panzarino:** And then you can say, oh, that's awesome.

**Matthew Panzarino:** Can you just do that for me?

**Matthew Panzarino:** And then put that into your pipeline, and now you have a pipeline that's corrected.

**Matthew Panzarino:** This is very light, like it's light cream cheese engineering, right?

**Matthew Panzarino:** It is super lightweight.

**Matthew Panzarino:** It's basically scripting.

**Matthew Panzarino:** Like, that's what this is.

**Matthew Panzarino:** And Claude is great at that.

**Matthew Panzarino:** It's really good at that.

**Matthew Panzarino:** You know, probably the best of the world, you know?

**Matthew Panzarino:** It's why all of our engineers use Claude code, right?

**Matthew Panzarino:** Because they're like, why should I do it when Claude knows how to do this stuff really well, right?

**Matthew Panzarino:** And then the job is, of course, judgment from there.

**Matthew Panzarino:** So, pipeline builder is great.

**Matthew Panzarino:** An artifact updater is another good Claude project to have.

**Matthew Panzarino:** And the reason that I mention these as separate ones is because Claude projects have memory, and they do learn your expectations over time.

**Matthew Panzarino:** sure, on them.

**Matthew Panzarino:** So, So,

**Matthew Panzarino:** And we'll get better at those tasks.

**Matthew Panzarino:** If you give them a half dozen different tasks, chat after chat, it can become harder for it to establish context.

**Matthew Panzarino:** And it can absolutely make it more difficult for it to suggest things for you and fix major issues, et cetera.

**Matthew Panzarino:** So take a look at that.

**Matthew Panzarino:** Artifact Updater would, of course, contain all of the artifacts that currently exist for the company.

**Matthew Panzarino:** And then you can update them, check for conflicts in there, as we mentioned.

**Matthew Panzarino:** So conflict passes are great to do in there.

**Matthew Panzarino:** And then we have an article editor as well for all of our clients.

**Matthew Panzarino:** And all it does is edit articles, right?

**Matthew Panzarino:** So as we mentioned before, like taking something to Claude is not an evil thing to do.

**Matthew Panzarino:** It's very useful when you're trying to figure out how to articulate to the pipeline what you want done, right?

**Matthew Panzarino:** So you can go take it into Claude and say, I really want X, Y, or Z to happen.

**Matthew Panzarino:** And then, you know, Opus does its thing, or Sonnet, if you prefer, and it's just like, hey, here's how I would correct this.

**Matthew Panzarino:** And you're like, that's a great idea.

**Matthew Panzarino:** And then you go to your pipeline builder, and you're like, hey, can I add a post-processing workflow that does this?

**Matthew Panzarino:** Or can I update my post-processing workflow, my post-processing checklist artifact, to say this in your artifact updater?

**Matthew Panzarino:** So there are absolutely ways for you to, like, unblock yourselves that don't require that you file a ticket for Ange and wait.

**Matthew Panzarino:** Now, there are absolutely people coming to help.

**Matthew Panzarino:** So we are hiring client ops engineers.

**Matthew Panzarino:** These folks will be in a closed loop with you to help you to execute these pipeline improvements and that sort of thing.

**Matthew Panzarino:** So especially if the tasks are more complex.

**Matthew Panzarino:** But I just want you to know that the tools are in your hands to make improvements for yourself today.

**Matthew Panzarino:** So if you're like, hey, this is all great philosophy talk, but, like, I have seven articles due this week, and I really need to work out the door.

**Matthew Panzarino:** I just want to tell you right now, like, I'm going to have to skip a couple of things, but one thing I really wanted to tell you is like, I don't have time to fix the pipeline of deliverables.

**Matthew Panzarino:** I hear that a lot, and I understand.

**Matthew Panzarino:** I get it.

**Matthew Panzarino:** Because I definitely manage clients, right?

**Matthew Panzarino:** I just came off of managing much clients.

**Matthew Panzarino:** I get how full the week gets with that.

**Matthew Panzarino:** However, my counter to that is you don't have time not to do that.

**Matthew Panzarino:** Because fixing a pipeline can take you an hour, 45 minutes, 30 minutes, way faster once you get good at it.

**Matthew Panzarino:** And then it'll save you probably 10 hours that week.

**Matthew Panzarino:** Like, that's how much, how important it can be, because it's all about leverage.

**Matthew Panzarino:** So I really think that if you sprint yourself on your pipeline for a week and make sure your artifacts are conflict-free, making sure your assignment directions are direct and not too laborious, and checking to see if there are any major improvements to a post-processor.

**Matthew Panzarino:** Or the pipeline itself, you're going to save enormous amounts of time and build a ton of leverage for yourself.

**Matthew Panzarino:** So, yeah.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Sweet.

**Matthew Panzarino:** I think that's about it.

**Matthew Panzarino:** Any questions anybody has in the last few minutes we have?

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Well, review this doc, obviously.

**Matthew Panzarino:** You know, take a look at it.

**Matthew Panzarino:** It goes through all the things I have in here.

**Matthew Panzarino:** There's also a bit of extra detail.

**Matthew Panzarino:** I'm going to try to produce these basically as editorial letters.

**Matthew Panzarino:** You know, they come to the production team with the things that I see most important every week.

**Matthew Panzarino:** That way you have some references there.

**Matthew Panzarino:** And then, of course, as I have my one-on-ones, those inform these conversations.

**Matthew Panzarino:** So, as we're all talking, you know, hopefully you'll see shades.

**Matthew Panzarino:** Some of you have.

**Matthew Panzarino:** I've spoken to you, you'll see shades of that appearing here, so I apologize for any repetition, but that's how I get a bead on what's actually important and what's going on with everybody, and then we'll provide these updates regularly, and then, of course, out of this will also come needs for documentation, you know, about certain processes or things like that that I'm like, oh, you should do this, and then I'm like, is that, wait, is that documented anywhere?

**Matthew Panzarino:** Ugh, you know, let's build one, right, and then we'll get new documentation for you so that it's all written down.

**Matthew Panzarino:** But yeah, hopefully this would be a good reference for you, and then hopefully this was a good chat, and reach out if you have any questions.

**Matthew Panzarino:** Thanks, folks.

**Matthew Panzarino:** Appreciate it.

**Matthew Panzarino:** Ciao, ciao.

**Matthew Panzarino:** Thank you.
