# Atlas Agentic Checks

<metadata>
date: 2025-12-05
time: 16:59 UTC
duration: 70 minutes
organizer: Saskia Wartnaby
participants: Ademilade Shodipe-dosunmu, Andi Bailey, Aida Knezevic, Carrie Chowske, Ehtisham Hussain, Erik O'Brien, Fatima, Felix Morgan, Gabrielle Brogan, Hassan, Iana Medvedeva, Ifeoluwa, Jakub Rudnik, Jenn Peters, Jenny Macrohon Dabon, Jessalynn, Jo Kaminska, Josip Sovar, Kalil, Katya Luscomb, Kavishka Kanayake, Kelvin Njiru, Kyle Gaudreau, Lawrence Neves, Liz Kushnereit, Marcus Derencius, Mariana Marins, Martha Martins, Matthew Alves-Hill, Matthew Panzarino, Megan Dickey, Najam Ahmed, Nathalie Schrans, Oluwatimilehin Ademosu, Patricia, Rachel, Saskia Wartnaby, Simran Sethi, Sydney Go, Sucheta, Tamara, Usman Adepoju, Usman Ghani, Victor, Vivek, William Leborgne, Will
fathom_recording_id: 106668105
fathom_url: https://fathom.video/calls/495861395
share_url: https://fathom.video/share/v_-q3zs_NApwcJC14aoLjpAsWyEZhGcf
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Matthew Panzarino introduced three mandatory process improvements to reduce post-pipeline editing time across all Editorial Managers: finalizing Operating Manuals and Editorial Checklists for every account, running Claude-based conflict checks on all artifacts and assignment directions, and simplifying assignment directions to skeletal outlines rather than detailed briefs. The team also committed to a new "Time to Delivery" KPI, with a golden path goal of less than 15 minutes from pipeline completion to client-ready content, addressing widespread issues where editing times were exceeding two hours due to conflicting instructions and overly complex prompts.

---

## Context

This meeting was called by Matthew Panzarino to address widespread inefficiencies in GrowthX's content delivery pipeline. Editorial Managers (MEs) across the organization have been conducting one-on-one sessions where Panzarino discovered that many are facing similar problems: post-pipeline editing times often exceed two hours, content comes out convoluted and hard to polish, and workflows take unusually long times (e.g., 20-30 minute drafting cycles). The root cause analysis identified that these issues stem not from technical failures but from conflicting instructions within or between artifacts, overly detailed assignment direction prompts that confuse agents, and general inconsistency in how different accounts are operated. The meeting serves as a knowledge-sharing session to codify best practices discovered in individual conversations and distribute them across the team so that all MEs can adopt standardized, efficient processes.

---

## Relevance

- **To GrowthX Delivery:** Implementing standardized documentation (Operating Manuals and Editorial Checklists), conflict-checking processes, and simplified assignment directions are table-stakes practices that reduce post-pipeline editing time from 2+ hours to a target of under 15 minutes. Conflict checks must be mandatory across all MEs and accounts. Assignment directions should be skeletal (H1/H2 structure with ranges, not specific word counts) to avoid agent loops and convoluted output.

- **To GrowthX Operations:** The new "Time to Delivery" KPI is the primary success metric for all Editorial Managers. The organization is exploring automated time-tracking solutions (with API integrations) while recommending self-tracking with timers in the interim. Panzarino emphasized that any manual post-pipeline work that repeats should be eliminated through pipeline workflows (e.g., dedicated CTA insertion steps) or artifact-based approaches.

- **To GrowthX Product Strategy:** Matthew Panzarino noted that ContentOS improvements and assignment direction architecture changes are underway in Daniel's domain, with future tools to come. The discovery that agents struggle with overly detailed instructions informs product design for more intuitive human-AI workflows in agentic systems.

---

## Overview

- **Mandatory Documentation:** Create an `Operating Manual` and `Editorial Checklist` for every account to ensure operational continuity and streamline onboarding.
- **Mandatory Conflict Checks:** Use Claude to check all artifacts and assignment directions for internal and cross-document conflicts. This prevents agent loops (e.g., 20-min draft times) and poor-quality output.
- **Simplify Assignment Directions:** Reset assignment directions to a skeletal outline (`H1`/`H2`s) with broad word count ranges. Overly detailed prompts cause agent confusion and long post-pipeline edits.
- **Primary KPI: Time to Delivery:** The core metric is the time from pipeline completion to client-ready state. The golden path goal is **\<15 minutes** per article.

---

## Key Topics

### The Problem: Inefficient Pipelines & Long Edits

  - Post-pipeline editing time is too high, often exceeding two hours.
  - This inefficiency stems from agent confusion caused by:
      - **Conflicting Instructions:** Contradictory rules within or between artifacts.
      - **Overly Detailed Prompts:** Complex assignment directions that agents struggle to interpret.
  - **Result:** Agent loops (e.g., 20-min drafts), convoluted content, and high manual effort.

### The Solution: Mandatory Process Improvements

  - **1. Finalize Documentation**
      - **Operating Manual:** A guide for anyone to operate the account.
          - **Contents:** Stakeholders, deliverables, pipelines used, and workflow summaries.
          - **Purpose:** Enables seamless coverage for vacations or assistance.
          - **Creation Tip:** Use Claude to explain pipeline YAML code for the workflow summaries.
      - **Editorial Checklist:** A pre-delivery checklist of client-specific requirements.
          - **Creation Tip:** Feed an existing operating manual to Claude to generate a draft.
  - **2. Run Conflict Checks**
      - **Process:** Use a Claude project with full context to identify logic errors.
          - **Inputs:** All artifacts, assignment directions, and the pipeline's YAML code.
          - **Prime Claude:** Explain the pipeline's purpose and request a conflict pass.
      - **Rationale:** The pipeline's YAML code shows the execution order, helping Claude find sequential conflicts (e.g., a post-processing step that undoes a previous one).
  - **3. Simplify Assignment Directions**
      - **Principle:** Use assignment directions as a directional prompt, not a detailed brief.
      - **Action:** Reset to a skeletal outline (`H1`/`H2`s) with broad word count ranges.
      - **Test:** For accounts with long edits, try running a topic with blank assignment directions to establish a baseline.
      - **Rationale:** The agentic drafter is designed to fill in the details. Over-specification causes confusion and poor output.

### The Goal: Time to Delivery KPI

  - **Definition:** Time from pipeline completion to client-ready state.
  - **Target:** **\<15 minutes** per article.
  - **Method:** Eliminate all repeatable manual steps.
      - **Example:** Automate CTA insertion with a dedicated workflow calling an artifact of approved examples.
  - **Measurement:** Start self-tracking with a timer; a holistic system is in development.

---

## Action Items

**Matthew Panzarino (GrowthX)**
- Rename 'Agentic Checks' to 'Pipeline Training and Updates'
- Schedule 1:1s w/ all MEs
- Ensure all MEs finalize editorial checklist + operating manual (incl metadata, pipeline YAML, workflows)
- Ensure all MEs run Claude conflict checks on artifacts + assignment directions
- Ensure all MEs reset assignment directions to skeleton (H1/H2, ranges); test in Add box; move to YAML
- Update Relay assignment directions template
- Distribute KPI guidance to MEs
- Explore/implement time-tracking for post-pipeline editing; share interim self-tracking guidance

**Najam Ahmed (GrowthX)**
- Draft and share Notion recap of this call

**Mariana Marins (GrowthX)**
- Send link to Pod F Claude prompts/files page to team

---

## Transcript
**Matthew Panzarino:** Good morning, everybody.

**Matthew Panzarino:** Hello, hello, your phone, it is.

**Carrie Chowske:** Hanser, with the color of your shirt, I thought you were just wearing a very low cut sweater.

**Carrie Chowske:** So did I, I was like, whoa, is that a house coat?

**Matthew Panzarino:** Sorry, didn't think more camera appropriate shirt colors.

**Carrie Chowske:** Very provocative, yes.

**Matthew Panzarino:** Yeah, I was like, bye Friday, be starting like, okay.

**Matthew Panzarino:** Yeah, let me get a cocktail.

**Jenn Peters:** Yeah, it was giving, like, lounge wear a little bit.

**Carrie Chowske:** Although, I feel like he could pull off, like, a smoking jacket, right?

**Carrie Chowske:** Like, does his hair, like, with, like, cigar in some old-timey library.

**Jenn Peters:** Oh, my God.

**Matthew Panzarino:** I wear, like, a type of, a type of kimono a lot, like, just, like, a noragi, which is basically, like, a working jacket, like, a, just a house-co-working jacket type thing.

**Matthew Panzarino:** And I wear them a lot.

**Matthew Panzarino:** And, unfortunately, on camera, it often looks like I'm wearing a bathrobe.

**Matthew Panzarino:** So, I was doing, like, Disrupt Remote in 2020, and it was, like, hey, are you wearing a bathrobe?

**Jenn Peters:** And I'm, like, no, but I could be.

**Matthew Panzarino:** Appropriate indoor wear.

**Matthew Panzarino:** Okay, okay.

**Matthew Panzarino:** Hello, everybody.

**Matthew Panzarino:** This meeting is being recorded.

**Matthew Panzarino:** A few things today.

**Matthew Panzarino:** The item, honestly, is just a very simple, like, we're going to find a better time for this meeting, because I think Friday, and I know, you know, a lot of you folks overseas, this is, like, very late on Friday for you, et cetera, and I want to, like, attendance for this.

**Matthew Panzarino:** This meeting is going to be mandatory for all MEs going forward, and we're also going to change the name from agentic checks to basically, like, pipeline training and updates or something.

**Matthew Panzarino:** I'm going to make it more descriptive, because really what I want this meeting to be is, I talk to many of you one-on-one throughout the week, and will continue to do so, so I will have a one-on-one with everybody over the next, you know, couple of months.

**Matthew Panzarino:** Obviously, holidays won't interrupt, but I will speak to everybody one-on-one, and of course, if you have anything that you need to speak to me about, you can always reach out, and then we'll find some time to schedule, but she will already be scheduling one-on-ones with all the MEs going forward.

**Matthew Panzarino:** Just to, I need to keep the pulse, we need to talk, et cetera, but in all of those one-on-one conversations...

**Matthew Panzarino:** Almost every single one, there is some sort of revelatory thing that I come across where I'm like, oh, you're doing it this way.

**Matthew Panzarino:** Oh, that's interesting.

**Matthew Panzarino:** Probably not the best, right?

**Matthew Panzarino:** And this is nobody's fault, really, but mine.

**Matthew Panzarino:** And so we will try to rectify that.

**Matthew Panzarino:** Obviously, those conversations are important and great, and I'm happy to have them, and it's all good, and never be afraid to be like, you know, oh, I do it this way.

**Matthew Panzarino:** And don't worry if I'm like, hey, don't do that.

**Matthew Panzarino:** That's what those conversations are for.

**Matthew Panzarino:** But those conversations need to pay forward into actually distributing that knowledge, right?

**Matthew Panzarino:** So we will collate conversations like that and other ideas and concepts that we have, and then produce, of course, either updated documentation, training on calls like this, or training documentation.

**Matthew Panzarino:** And then, of course, you know, more materials about best practices.

**Matthew Panzarino:** So that information, one of my main goals.

**Matthew Panzarino:** for the next quarter is to help a lot of the information that gets kind of discovered in one-on-one conversations or work sessions with any of you into something that can be distributed and can be widely shared.

**Matthew Panzarino:** Frankly, the fact is I talk to people that are doing the same wrong things or having the same issues because of those things a lot, and it doesn't make any sense.

**Matthew Panzarino:** You know, we have all of the ability in the world to share information and knowledge, and it's just my job to make sure that it's done in a way that makes the most sense for everybody and it makes it clear to everyone.

**Matthew Panzarino:** So, anyhow, that's what this meeting will be going for.

**Matthew Panzarino:** It'll be less like, oh, we just rolled out agentic pipelines.

**Matthew Panzarino:** What do those do?

**Matthew Panzarino:** And more ongoing training.

**Matthew Panzarino:** Hey, let's move forward.

**Matthew Panzarino:** Let's figure out what's going on.

**Matthew Panzarino:** So, in that vein, I'll talk about a couple of things on this particular call.

**Matthew Panzarino:** Let's my whole list because there's just a lot.

**Matthew Panzarino:** But, um...

**Matthew Panzarino:** The, I want to talk about a couple of mandatory things that I want every ME to do, and we will, I don't want to share this agenda yet, Nana, we put together an agenda for this call, but I want to clean it up a little bit more, and just, it'll be more of a reminder list about things we talked about on this call, and of course, you'll have the transcript, that's fine, but sometimes a Notion doc is cool too.

**Matthew Panzarino:** There are a couple of mandatory items that I want all MEs to do.

**Matthew Panzarino:** One is finalize the editorial checklist and make sure that your operating manual is in order.

**Matthew Panzarino:** Those two documents for every account really should be mandatory.

**Matthew Panzarino:** There's no excuse not to have them.

**Matthew Panzarino:** You already have all of that information, otherwise you wouldn't be delivering for clients, right?

**Matthew Panzarino:** Like, you know how to operate that account, obviously, and then you know what needs to be done before you can present it to the client, you know, the checklist of items that needs to happen, the wants, desires, and needs of the client, the, you know.

**Matthew Panzarino:** Um, logistics of delivering, you know, okay, they want this, we need to have this, we need a bit of tags, need to have, you know, the first paragraph needs to mention this, the CTA needs to have that, that is in a standard editorial checklist, and I'm sure a lot of you will be like, yeah, of course we have one, but some of you are like, ooh, you know, I don't know if we have a holistic document, please create those two documents.

**Matthew Panzarino:** Uh, the operating manual, uh, which Nana can share a template with you, and I'm sure Andy has already, um, in some cases, it's very straightforward, it's how do I do this job for the client, how do I operate this account, and this, the reason for that document's existence is very simple, what if you go on vacation, what if you need time off, what if you need assistance, right, like, instead of saying, oh, cool, now I have to take an hour and a half call to, like, explain to somebody in detail how to do my job, so that I can take vacation, you can be like, hey, here's the operating manual, the operating manual has everything from stakeholders in it to

**Matthew Panzarino:** How, what the expectations are, what you're actually delivering, like what work stream are you doing for the client, what the pipelines are that are actually being used, because, you we all experiment, maybe there's a bunch of pipelines in there, which one's the right one, there's no worries about that now, you can check the operating manual.

**Matthew Panzarino:** It, of course, would also have instructions on how to operate that pipeline, and what the workflows inside the pipeline do, just on a rough basis, it doesn't have to be incredibly detailed, but you should be able to enumerate, this workflow checks for this, this workflow adds these items, this workflow does this, right?

**Matthew Panzarino:** In some cases, this will be standard, the drafter workflow drafts articles, okay, but in many cases, for many accounts, there are specific workflows that do specific things, and for somebody new coming in and operating the account, they need to be aware of what it does, so that they can observe its inputs and outputs, right?

**Matthew Panzarino:** So, those two documents, I think, are pretty, pretty straightforward, we need those, there will be a template.

**Matthew Panzarino:** Or there already is a template, and you can look at that to see what we mean by that, and frankly, Claude is pretty good at that, so you can feed it things like your documents from your client workspace, any personal documents you have about operating the account, and then the template, and then have it help you craft that.

**Matthew Panzarino:** One quick tip for you, by the way, on the pipeline section, is you can just go into the pipeline, and hit the edit button, and grab the code for the pipeline, and then just give that to Claude, say, hey, explain to me what this pipeline does, you know, and then just paste that into the what the pipeline does section, it's pretty straightforward, you know, and if you then need to go, I hesitate, I just want to say this, you then need to go actually read it, and edit it, because it won't know everything, it won't know all the context, but it can at least tell you, hey, here's the basic workflows, here's what they do, etc., and then you can add in, because the client wanted X to happen, so we added this, right, and it's just,

**Matthew Panzarino:** Table Stakes.

**Matthew Panzarino:** We need those documents.

**Matthew Panzarino:** Please have them.

**Matthew Panzarino:** Oh, and Nana's pro tip and what she has done for some of you is if you already have an operating manual but no editorial checklist, then it's a good seed for the checklist.

**Matthew Panzarino:** So you can feed the operating manual to something like a club project and say, hey, I need an editorial checklist for all items that are coming out of this.

**Matthew Panzarino:** I'd like them to be adherent.

**Matthew Panzarino:** So you can start there and then, of course, check it for any client requirements, et cetera.

**Mariana Marins:** We have a template as well for the checklist.

**Mariana Marins:** So what I've been doing, and I will probably do some more for more of you today and Sam for your review is I get the operating menu.

**Mariana Marins:** If it exists, I give the operating menu and the template to Claude and I ask it to fill in the things in Claude.

**Mariana Marins:** What has been happening in the templates.

**Mariana Marins:** I'm sorry.

**Mariana Marins:** What has been happening in most of all the ones that I have done.

**Mariana Marins:** Is that most of the operating menus don't have metadata fields.

**Mariana Marins:** So like, what do you deliver to the client?

**Mariana Marins:** URL, URL slug, meta title.

**Mariana Marins:** So think about this as well when you are doing your operating menus.

**Mariana Marins:** And also, most of you have done the operating menus already.

**Mariana Marins:** Most of the accounts that don't have operating menus, it's because you haven't, like the account hasn't changed hands.

**Mariana Marins:** It's still with the same folds from the beginning.

**Mariana Marins:** But we still need the operating menu because things might happen.

**Mariana Marins:** Like this week, I've been helping in some accounts.

**Mariana Marins:** And luckily, these accounts had the operating menu.

**Mariana Marins:** So I didn't have to, I didn't have to pester the ME asking questions.

**Mariana Marins:** I just read the menu, you know.

**Mariana Marins:** So that's it.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Well, you can see from the template and from examples, if you want to look at examples, of course, Biologica has an operating manual.

**Matthew Panzarino:** Many of your other accounts have an operating

**Matthew Panzarino:** You can go look at those and see what we mean by that.

**Matthew Panzarino:** Two, second mandatory item, run a conflict check on your artifacts.

**Matthew Panzarino:** Check for internal conflicts within individual artifacts and then conflicts between artifacts.

**Matthew Panzarino:** And then also check with conflicts between your artifacts and the assignment directions that you're giving your account.

**Matthew Panzarino:** We'll talk about assignment directions in a second.

**Matthew Panzarino:** But I think this is just a mandatory task that everyone must do.

**Matthew Panzarino:** I don't really think there's any excuse not to do this.

**Matthew Panzarino:** Not only is it not that hard, it also will have the potential to save you and the workflows a bunch of time.

**Matthew Panzarino:** So what do I mean by that?

**Matthew Panzarino:** I mean feeding your artifacts and assignment directions to a cloud project that has the appropriate context.

**Matthew Panzarino:** It has those as artifacts, but then you're going to put it into a chat and say, hey, here are these artifacts and here's the assignment directions.

**Matthew Panzarino:** directions that I give, and I would like you to check for conflicts between these.

**Matthew Panzarino:** There's a little setup that I think is probably wise for you before you just drop these into a rando-claw chat.

**Matthew Panzarino:** I do feel that you need to create a claw project for this or utilize any claw project you already used to manipulate the artifacts for your claim so that it has some context for what it's doing.

**Matthew Panzarino:** The artifact or the context that I would suggest giving that project is the artifacts themselves, of course.

**Matthew Panzarino:** I would give it the pipeline.

**Matthew Panzarino:** So, once again, take the code of the pipeline itself and paste it into an artifact as a project artifact in the claw project.

**Matthew Panzarino:** I would then prime it.

**Matthew Panzarino:** So, talk to it for a couple of minutes about what you're about to do.

**Matthew Panzarino:** Say, hey, I'm running a pipeline.

**Matthew Panzarino:** It creates an editorial output or a content output.

**Matthew Panzarino:** It runs a series of steps I've provided.

**Matthew Panzarino:** I've

**Matthew Panzarino:** That for you.

**Matthew Panzarino:** Let me know if you can see it.

**Matthew Panzarino:** Oh, yes, I see it here, right?

**Matthew Panzarino:** Here it is.

**Matthew Panzarino:** I also have some artifacts.

**Matthew Panzarino:** You can see the artifacts here, and you can see where they're called in the pipeline.

**Matthew Panzarino:** I would like you to check for conflicts that may arise in executing instructions based on these artifacts throughout this pipeline.

**Matthew Panzarino:** Then I would like you to check.

**Matthew Panzarino:** Let it do its thing.

**Matthew Panzarino:** It's probably going to have a lot of information for you.

**Matthew Panzarino:** I would highly doubt it wouldn't find some conflict or potential conflict.

**Matthew Panzarino:** Now, you may disagree, and that's cool.

**Matthew Panzarino:** You don't have to take all of its advice, but almost 9 times out of 10, 9.8 times out of 10, we find some sort of conflict, either within an artifact itself, where you have just added stuff because the client has been yammering about stuff, and you're like, okay, cool, let add that.

**Matthew Panzarino:** You know, writing guidelines or whatever.

**Matthew Panzarino:** And at the top of the guidelines, it says, never use a CTA that links to blah, blah, blah.

**Matthew Panzarino:** And at the bottom, it says, always use a CTA that links to blah, blah, blah.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** Like,

**Matthew Panzarino:** This kind of stuff is death to agents.

**Matthew Panzarino:** Not only will it make your run times incredibly long on any given workflow, like the drafter workflow may take 20 minutes, right?

**Matthew Panzarino:** That's insane.

**Matthew Panzarino:** It should not take 20 minutes.

**Matthew Panzarino:** should take under five minutes to actually draft the article.

**Matthew Panzarino:** The researcher is different, right?

**Matthew Panzarino:** Like, that's Marcus's job to figure out, not yours.

**Matthew Panzarino:** But the drafter, if it's taking 20 to 30 minutes, huge red flag, magenta flag, neon glowing, pulsating, blood-soaked red flag.

**Matthew Panzarino:** Because it means that the agent is going out and trying to accomplish its task and running into some sort of blocker or issue, and then it's going and trying over and over and over again to rectify.

**Matthew Panzarino:** And it sometimes is fixing the issue and then running into the conflict and fixing that issue.

**Matthew Panzarino:** And then when it comes back around and says, oh, I've got a conflict again.

**Matthew Panzarino:** I need to fix this issue.

**Matthew Panzarino:** And so that recursion, it causes me.

**Matthew Panzarino:** It also can make your content insanely convoluted.

**Matthew Panzarino:** It can try to accomplish the tasks by using enormously weird compound sentences, odd paragraph structures, abrupt transitions where it's like, hey, you only gave me 150 words to do X, and you're telling me that I need to keep it brief, and yet I need to fit these eight details in here, so I'm going to just give you one line of each and then bounce.

**Matthew Panzarino:** With no transitionary sentences and no narrative flow, and you're like, wow, this is bad, know, the pipelines are so bad at this job.

**Matthew Panzarino:** Yeah, but why?

**Matthew Panzarino:** Why are they bad?

**Matthew Panzarino:** That's your whole job here, is why are the pipelines bad, right?

**Matthew Panzarino:** To make your life easier.

**Matthew Panzarino:** So, anyhow, conflict check.

**Matthew Panzarino:** If you need any assistance on how to do that, you can check in pod F.

**Matthew Panzarino:** Nina can point you to the project that we have used to do that in the past.

**Matthew Panzarino:** There are some of you here who have done it, so peer assistance.

**Matthew Panzarino:** You also be useful.

**Matthew Panzarino:** You can use the Atlas Learnings channel to solicit peer assistance.

**Matthew Panzarino:** I don't want to put all the burden on Nana or Yana, who have both done this kind of work before, or anybody else individually, because she's got a lot to do.

**Matthew Panzarino:** But she can be of assistance to you in some ways.

**Matthew Panzarino:** And then we can also probably create a training document, or at least a brief outline of how we accomplish this.

**Matthew Panzarino:** But it's just not that hard.

**Matthew Panzarino:** To be honest, all it would take is for, I mean, like, table stakes, you could just feed it into a raw cloud chat, and it could probably still find conflicts, because it's just a logic puzzle.

**Matthew Panzarino:** The reason that you give it the additional context, like the pipeline itself and the artifacts, is that the more context it has, the more it can help you find complex conflicts, like a conflict between an article draft step and a post-processing step.

**Matthew Panzarino:** Because just saying, hey, here's the post-processing checklist that I give you, that I give it, and it happens at this step.

**Matthew Panzarino:** And Claude is like, well, you say at this step.

**Matthew Panzarino:** And so then it does that, and then it does this, and then you say at this step to do this thing that's oppositional, and so it changes.

**Matthew Panzarino:** So it can just get a little bit of context about how the pipeline is constructed, and then it can offer you advice on resolving those conflicts.

**Matthew Panzarino:** Does that make sense?

**Matthew Panzarino:** Just want to make sure everybody understands what I'm saying there with the conflict thing and all of that.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** The other major source of conflict besides artifacts either internally within themselves or between each other is the assignment directions.

**Matthew Panzarino:** Assignment directions are often created in wildly different ways across the organization, and that means that whatever instructions you're giving there, which are a prompt, by the way, like what is assignment directions?

**Matthew Panzarino:** What is that field?

**Matthew Panzarino:** It's a prompt.

**Matthew Panzarino:** It's a So...

**Matthew Panzarino:** Remember that when you're writing this, it's not some sort of, it's not some sort of like detailed fill in the blanks or Mad Libs.

**Matthew Panzarino:** It is a prompt, which means that it will be interpreted as a prompt by Sonnet, which is what it is called to interpret that prompt by the workflow.

**Matthew Panzarino:** So when you're writing assignment directions, just as you would with the prompt, you want to do two major things.

**Matthew Panzarino:** One, check for conflicts between that and your contextual artifacts, because if you're telling it to do something in assignment directions that is oppositional to what writing and guidelines is saying, then it's going to run into issues the moment that the drafter calls both the assignment directions and the writing guidelines and tries to rectify, right?

**Matthew Panzarino:** So that is also part of your conflict pass.

**Matthew Panzarino:** The second thing that's really important here is that assignment directions really are directional.

**Matthew Panzarino:** They are not hyper explicit.

**Matthew Panzarino:** So

**Matthew Panzarino:** You do not need to, nor should you, create an enormously complicated, detailed, full brief and paste it into assignment directions.

**Matthew Panzarino:** That is the wrong way to go.

**Matthew Panzarino:** You are, like, paddling up the wrong creek very, very fast.

**Matthew Panzarino:** It is not impossible that you will get something workable out of it, but I guarantee you that your end processing times will likely be higher.

**Matthew Panzarino:** And by that, I mean, once it exits the pipeline, how long does it take you to get a client deliverable, which we'll talk about in minute.

**Matthew Panzarino:** But I guarantee you those times will be higher if you give it a laborious amount of information in that field.

**Matthew Panzarino:** Because it's a prompt.

**Matthew Panzarino:** You can't write a 2,500-word prompt and expect it to adhere to every single item in that.

**Matthew Panzarino:** It's just not viable.

**Matthew Panzarino:** Not only that, but if you give it an incredibly detailed outline, especially, like many of you do, which is fine.

**Matthew Panzarino:** It's not a big deal.

**Matthew Panzarino:** But like many

**Matthew Panzarino:** Many of you put in word counts per section because you kind of want it to take a certain shape.

**Matthew Panzarino:** Understandable.

**Matthew Panzarino:** It's fine.

**Matthew Panzarino:** Most of time it works.

**Matthew Panzarino:** Sometimes it doesn't.

**Matthew Panzarino:** We all know this.

**Matthew Panzarino:** But if you tell it, I would like you to cover these eight points in high detail in 150 words, like what do you think is going to happen?

**Matthew Panzarino:** Like if you told a human to do that, how long would it take them to do that, to figure that out?

**Matthew Panzarino:** Like what gymnastics would they have to pull to do like seven or eight different major thought exercises in 150 words?

**Matthew Panzarino:** It usually results in compound sentences, wild constructions, colons, because colons are great for that, M dashes, of course, because if you need a sentence to encompass two or three different thoughts, are you going to do?

**Matthew Panzarino:** Throw an M dash in it, right?

**Matthew Panzarino:** It also results in just awkward phrasing and abrupt transitions, once again, between one section and another, because it's like, I finally got...

**Matthew Panzarino:** All the ideas in here, I really don't have time for niceties, like introducing you to the next concept we're about to talk about in the next section, or having a graceful exit from this narrative into the next narrative, right?

**Matthew Panzarino:** So, I would suggest that you strip down and reset your assignment directions to a skeleton, and by a skeleton, I mean, like bare bones, H1s maybe, a couple H2s, I'll be honest with you, if you're having like a hell of a time, like I'm going to tell you really flatly on this call, like, if you are taking two plus hours to edit any piece of content coming out of the pipeline, you're doing something wrong, let's just, I'm going to be frank with you, you're doing something wrong, and by you, I want to be, soften that slightly, by something is happening incorrectly in the pipeline, and because you are the operator of it, you are responsible for it, right?

**Matthew Panzarino:** So, something is happening that's awry, there's no reason

**Matthew Panzarino:** Reason in the long run that anything should take you that long to edit once it comes out of the pipeline.

**Matthew Panzarino:** Because otherwise, why don't we have a pipeline?

**Matthew Panzarino:** I could write any article we produce for a client in two and a half hours.

**Matthew Panzarino:** You know what mean?

**Matthew Panzarino:** Like, and so could many of you.

**Matthew Panzarino:** It's not me special, but I'm saying any of you could do that.

**Matthew Panzarino:** If you had the research done for you, you could write the rest of it in two and a half hours for sure.

**Matthew Panzarino:** So editing or manipulating a piece of content for two and a half hours after it comes out of an automated process is like, don't do that.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** It's bad.

**Matthew Panzarino:** It's evil in my mind.

**Matthew Panzarino:** Otherwise, why are we even a company?

**Matthew Panzarino:** So how do we make it better?

**Matthew Panzarino:** A lot of ways.

**Matthew Panzarino:** Article complex is one.

**Matthew Panzarino:** You know, pipeline improvements is another.

**Matthew Panzarino:** Like either engineering makes an improvement and we adopt it and we're like, oh, great.

**Matthew Panzarino:** This is great.

**Matthew Panzarino:** This actually made a huge difference in my workflow or whatever.

**Matthew Panzarino:** Or manipulating the task that you are giving the pipeline.

**Matthew Panzarino:** And that task is the assignment directions.

**Matthew Panzarino:** Thank

**Matthew Panzarino:** And I think it is, it's not only, I mean, it's probably the most important thing that you do with any pipeline, is what prompt you're giving it.

**Matthew Panzarino:** And that prompt includes the topic and the assignment directions.

**Matthew Panzarino:** So I'll talk about topic in a second, but to concentrate on assignment directions, strip down your assignment directions to basic structure.

**Matthew Panzarino:** I would honestly suggest that if you're having a heck of a time and having a really long edit cycle, that you try deleting everything from your assignment directions and just telling it to write you an article about this topic and see what happens.

**Matthew Panzarino:** I think you might be shocked at how much better it is than whatever laborious assignment directions you were giving it.

**Matthew Panzarino:** Like, you can literally say, hey, write me a how-to article about topic X, give me an intro, a couple of supporting paragraphs, and a CTA.

**Matthew Panzarino:** Oh, here's this kind of CTA I want.

**Matthew Panzarino:** Don't write it exactly like

**Matthew Panzarino:** Kind of like this.

**Matthew Panzarino:** Okay, bye.

**Matthew Panzarino:** And then send that through.

**Matthew Panzarino:** I almost guarantee you that some of you who have come to me going like, ah, you know, I don't know what's going on.

**Matthew Panzarino:** It's like 2,500 words and it's like crazy and I'm editing it for hours.

**Matthew Panzarino:** I guarantee you this would like change your life.

**Matthew Panzarino:** So give it a try.

**Matthew Panzarino:** Not only that, but the article will generate in like two minutes.

**Matthew Panzarino:** So you can like regenerate the article a bunch of times.

**Matthew Panzarino:** You let the research stand because the research is probably fine.

**Matthew Panzarino:** And then run the article a handful of times and see what kind of different results you get.

**Matthew Panzarino:** Just the generation step, you know, the second step and see what you get.

**Matthew Panzarino:** But I honestly think that this is a big issue across the org.

**Matthew Panzarino:** So in this cluster of three things, three major things that I want you to concentrate on, I think that is a big one.

**Matthew Panzarino:** You know, so obviously internal conflicts, finalize those editorial checklists and operating manuals, and then reset your assignment directions to more of a skeleton.

**Matthew Panzarino:** Overall structure.

**Matthew Panzarino:** Perfection purposes, you could do rough word count ranges, I suggest ranges rather than hard word counts, because all too often somebody would be like, I'm having a heck of a time, I'll go in there and look, and I'll look at what the pipeline is executing, and the actual pipeline, or the workflow, excuse me, will tell you, hey, you said I have to do 150 words here, so I'm going to go add a few random words to make it 150 words.

**Matthew Panzarino:** Like, it'll literally tell you what it's doing.

**Matthew Panzarino:** It's pretty verbose, if you look in the actual flow of it executing in Flow Studio.

**Matthew Panzarino:** And, like, that, that's a problem.

**Matthew Panzarino:** We don't need it to be 150 words, we want it to be about 150 words.

**Matthew Panzarino:** So, I would suggest ranges, and maybe even don't do word counts at all, and see what happens.

**Matthew Panzarino:** And if you are finding, oh, wow, I wrote a 8,000 word intro to a 2,000 word article, fine, okay, you know, maybe put a range in there.

**Matthew Panzarino:** But in all honesty, it's, it's going to pattern match off of the existing articles, and most

**Matthew Panzarino:** Articles have roughly the same size of intro, right?

**Matthew Panzarino:** They're mostly between 100 and 350 words.

**Matthew Panzarino:** So I would suggest that you give it a range to try word counts instead of specific word counts.

**Matthew Panzarino:** You can keep client-specific requirements in there, obviously, if the client very, very, very, very much wants a certain section, you say, please include an FAQ.

**Matthew Panzarino:** You can even give it like a brief kind of structure of how you want it, Q&A, but it knows what an FAQ is.

**Matthew Panzarino:** You don't have to belabor the point, to be honest.

**Matthew Panzarino:** If they want a TLDR, you know, if they want client-specific sections in there, feel free to do that.

**Matthew Panzarino:** And then run a few articles and see what happens.

**Matthew Panzarino:** I think you would be massively surprised.

**Matthew Panzarino:** Yes, Dina.

**Mariana Marins:** Just two minutes, because I talked to a bunch of people this week, and I also listened to a bunch of calls and, I don't know, did a bunch of things.

**Mariana Marins:** So, two tips that...

**Mariana Marins:** I have found useful is assignment direction is kind of hard-coded in the YAML, right?

**Mariana Marins:** Which means that if you want to change it permanently, you will need to go to the YAML.

**Mariana Marins:** But if you want to test before actually editing the YAML, you can edit it in the text box that appears once you click add.

**Mariana Marins:** And maybe like you will need to do this every time you add a new topic, but maybe run some three or four with like that manually pasting there just to see if it will take.

**Mariana Marins:** And once you are happy with that, you can then move it into the pipeline just so you don't have to copy and paste every time.

**Mariana Marins:** If you are copy and pasting assignment direction every time you click add, that's not a good idea.

**Mariana Marins:** Don't you?

**Mariana Marins:** You are wasting your time.

**Mariana Marins:** Second thing, Marcus, yesterday we were trying to troubleshoot something.

**Mariana Marins:** He made something that was like, oh my God, mind-blowing.

**Mariana Marins:** So someone, I don't remember who, was having a hard time with a specific row in the pipeline, in a specific step, if I'm not mistaken, and he was like, okay, let me look into this, and then he went to the inputs of that step, and he checked which two artifacts were being used as inputs into that step, and then he ran a conflict check, and those two artifacts were were conflicting.

**Mariana Marins:** That's why that step was taking much longer to run, and was just creating issues.

**Mariana Marins:** So I had not thought about that, it was a great way of like, okay, which two are conflicting?

**Mariana Marins:** And then, of course, you need to find the conflict, but then you are already being able to see fast which is, what is the problem.

**Mariana Marins:** and one more thing, I'm going to share my screen here.

**Mariana Marins:** Because

**Mariana Marins:** Yes, as I told you, I did a bunch of things this week, and this is Relay's assignment direction.

**Mariana Marins:** This is not anyone's fault, okay, because I am pretty sure this is the general one that comes with the pipeline.

**Mariana Marins:** You are going to see what's the issue here.

**Mariana Marins:** Formatting guidelines.

**Mariana Marins:** It's blank.

**Mariana Marins:** There's nothing here.

**Mariana Marins:** So this is kind of a template.

**Mariana Marins:** We need to put things here.

**Mariana Marins:** Like, what are the formatting guidelines?

**Mariana Marins:** And one more thing.

**Mariana Marins:** Outline draft.

**Mariana Marins:** I would probably remove this.

**Mariana Marins:** I don't know if Panzer agrees, but, like, maybe you can do this outline draft as, I want five sections.

**Mariana Marins:** I want a clear conclusion and a clear introduction.

**Mariana Marins:** I want key takeaways.

**Mariana Marins:** But I think that for us, when we say outline, it takes us back to air ops, and we think that we need to give it, like, Oh, I want this article to...

**Mariana Marins:** Talk about, I don't know, dysmenorrhea and PMS and cramps and paragraph A is cramps, paragraph 2 is PMS, etc.

**Mariana Marins:** No, don't do this.

**Mariana Marins:** I have been seeing, and Panzar, if you check the link that Lawrence shared there, we need to forget about outlines.

**Mariana Marins:** Like, outlines don't exist anymore.

**Matthew Panzarino:** I am maybe being too drastic.

**Matthew Panzarino:** Panzar, correct me if I'm wrong.

**Matthew Panzarino:** Yeah, no, it's not like that process of creating, like, hybrid detailed article briefs isn't valid, right?

**Matthew Panzarino:** Like, if you were doing this on your own, this process would be very helpful.

**Matthew Panzarino:** But this is what the article drafter does.

**Matthew Panzarino:** Like, you're writing a whole brief, and then the article drafter is just going like, yeah, okay, and then it's rewriting the entire brief.

**Matthew Panzarino:** Like, you know, it's like handing it a brief and saying, write a brief, and then write

**Matthew Panzarino:** An article on the second brief.

**Matthew Panzarino:** There's no reason to do it.

**Matthew Panzarino:** Like, otherwise, we would not have the article drafter, and we would just tell the brief to just, like, we would just one-shot Claude and say, hey, write an article on this brief.

**Matthew Panzarino:** Like, if you're doing that much work to create a hyper-detailed brief, then you could probably just fill in the blanks in 15 minutes with Claude, you know?

**Matthew Panzarino:** The whole purpose of this is give it an outline, very skeletal outline, of what you want, prompt it to do a thing, and then let the agentic drafter draft the article.

**Matthew Panzarino:** And it is pretty good at its job.

**Matthew Panzarino:** And I think it is actually worse at its job when you give it something that is not intended to be fed into it, like a hyper-detailed, very granular article brief.

**Matthew Panzarino:** Just putting that out there.

**Matthew Panzarino:** Throw it away and try nothing for a minute.

**Matthew Panzarino:** You know?

**Matthew Panzarino:** Like, I think one of the major issues with any fast-moving company and any, like, new product like this is that nobody has a baseline for anything, right?

**Matthew Panzarino:** Like, you were working off of, like, preconceived notions about the way the product used to work, but they've shipped two dozen updates since the last time you checked, right?

**Matthew Panzarino:** And so I think baselines can sometimes be very valuable.

**Matthew Panzarino:** And in this case, your baseline is very straightforward.

**Matthew Panzarino:** Delete the article directions and just run it blank with a topic and see what you get out of it.

**Matthew Panzarino:** I think you might be shocked at how capable it is.

**Matthew Panzarino:** And then, of course, you'll probably need to add client-specific stuff back in that you need.

**Matthew Panzarino:** Yeah.

**Mariana Marins:** No, here, there's nothing client-specific.

**Mariana Marins:** It's just a blank, basic one.

**Matthew Panzarino:** I will take care of this next week.

**Matthew Panzarino:** I haven't had the time.

**Mariana Marins:** Yeah.

**Mariana Marins:** And just one more thing is also if you don't want to...

**Matthew Panzarino:** Oh, I think you cut out, Nana.

**Matthew Panzarino:** Or you cut out for me.

**Matthew Panzarino:** Oh,

**Matthew Panzarino:** Oh, maybe it's me.

**Mariana Marins:** Okay, so, yeah.

**Najam Ahmed:** No, we didn't get here either.

**Ehtisham Hussain:** Yeah, it's everyone.

**Mariana Marins:** Oh, sorry.

**Matthew Panzarino:** I think you cut out for some people, Nana.

**Mariana Marins:** Just repeat your last couple of sentences, that's all.

**Mariana Marins:** Yeah, sorry.

**Mariana Marins:** Also, if you don't want something, you can also add that to the assignment directions.

**Mariana Marins:** So, in terms of structure, of course.

**Mariana Marins:** Like, I don't want FAQs.

**Mariana Marins:** I don't want common pitfalls.

**Mariana Marins:** And it's generally going to follow.

**Mariana Marins:** I have also found some success into fixing gimmicky headers.

**Mariana Marins:** So, we would always have conclusion headers that would be something like moving forward, your path forward, your next steps, etc.

**Mariana Marins:** And, like, I tried with Artifact, it didn't work that much.

**Mariana Marins:** But then I prompt the assignment direction real hard, and now I don't have those gimmicky

**Mariana Marins:** Miki's sentences for headers.

**Mariana Marins:** Normally, I don't talk much about the body of the article in assignment direction.

**Mariana Marins:** It's more structure, and structure involves headers.

**Mariana Marins:** And also, some people have told me, I need headers that are questions.

**Mariana Marins:** I need headers that follow these, these, and these.

**Mariana Marins:** Assignment direction works a little well for this as well, but you have to pair it with guidelines, with artifacts.

**Mariana Marins:** So, mostly writing guidelines, like, one reinforces the other, you know?

**Mariana Marins:** So, yeah, that's what I have found success in.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** I'll adjust this thing Marisol just brought up, too, which is, like, she says that they've defined certain structures that they do as artifacts.

**Matthew Panzarino:** This is totally possible.

**Matthew Panzarino:** The way that you would do this is by defining those structures as artifacts and then having the drafter call those artifacts and say, hey, we'd like, you know,

**Matthew Panzarino:** I to write this kind of article or that kind of article.

**Matthew Panzarino:** I think this is relatively advanced, and I wouldn't recommend most people start there because I think most of you just need to reset your expectations around article directions.

**Matthew Panzarino:** However, if you are creating articles of a specific type, like let's say you are doing what amounts to a semi-PSEO editorial engagement, you know.

**Matthew Panzarino:** I think Interwell is doing Ketamine for X, right, as an example, and Khalil and I were talking a bit about this.

**Matthew Panzarino:** You can just create a new pipeline that has assignment directions specifically targeted at that format, and then have the assignment directions pre-filled with that rough structure that you want.

**Matthew Panzarino:** And then you give it its new topic, and then run it, and then run it all day.

**Matthew Panzarino:** And your other pipeline maybe is more generalized editorial, top of funnel or mid-funnel editorial content, and then you can let it do its thing.

**Matthew Panzarino:** So there's nothing saying you can't have multiple pipelines with different pre-formatted assignment directions.

**Matthew Panzarino:** I think that is the best way to do it, like, today with almost no additional learnings or tweaking to the pipeline.

**Matthew Panzarino:** In the future, I think it would be valuable for assignment directions to live, honestly, in an artifact and then have it culled by the pipeline.

**Matthew Panzarino:** But that's a re-architecture of the way that Atlas works, and I'll leave that in Marcus's capable hands.

**Matthew Panzarino:** I don't want to make any promises on how that will evolve.

**Matthew Panzarino:** Frankly, the assignment directions is tied up in a larger project, which is the opportunities project that comes out of the content OS, and Daniel is working on that.

**Matthew Panzarino:** He's turned his attention from check that onto content OS, so we'll be getting some improvements there coming down the pike.

**Matthew Panzarino:** But the long story short is that we should be able to – we should have more tools for that beginning of the process soon.

**Matthew Panzarino:** But regardless, your assignment directions can be manipulated, as Nana said, manually by just typing in the box.

**Matthew Panzarino:** And tweaking it and running tests row after row.

**Matthew Panzarino:** If you come upon something where you're like, oh, actually, this is great.

**Matthew Panzarino:** This is what I want.

**Matthew Panzarino:** I would love for the pipeline to pre-fill this every time.

**Matthew Panzarino:** It's actually quite simple.

**Matthew Panzarino:** You can grab the pipeline, grab the pre-fill assignment directions, give them both the Claude and SoClaude, please insert this as the assignment directions, and then paste that back into your pipeline and you're good to go.

**Matthew Panzarino:** So, and once again, if you need help with that process, we can help.

**Matthew Panzarino:** It's not hard and it only took a couple minutes to show you how to do it.

**Matthew Panzarino:** And I've showed a handful of people this week how to do that.

**Matthew Panzarino:** So, I think that's like a, you know, that I think is a valuable exercise for everybody to do.

**Matthew Panzarino:** So, anybody have any questions on any of those three major things?

**Matthew Panzarino:** like, you I that's you know, it's So, Thank you.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** And, you there isn't a, I know what you're saying, Will, and I'm happy that people are getting good results.

**Matthew Panzarino:** And if you're getting good results, that's great.

**Matthew Panzarino:** But I see all too often that people are running into issues because there are really detailed assignment briefs that are giving instructions that cause conflict.

**Matthew Panzarino:** That's why we're having this conversation.

**Matthew Panzarino:** So if you have a process that's working for you, I'm happy.

**Matthew Panzarino:** That's great.

**Matthew Panzarino:** But the very next thing I want to talk about, and unless it's germane to this, Dana, I want to jump on to one more thing, one major topic.

**Mariana Marins:** I just wanted to share with people that I have started a page in the delivery area.

**Mariana Marins:** I'm going to send you the link later on with our cloud prompts from podf.

**Mariana Marins:** And, like with the, also the files that we give to the, those projects.

**Mariana Marins:** So you will have the pipeline for now, the pipe.

**Mariana Marins:** Client Builder, the Artifact, Data, and the Editor.

**Mariana Marins:** So if you guys want to copy, there's that.

**Mariana Marins:** I'm going to send the link later.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Okay, good.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** So what you're saying, Will, like, you know, if you end up needing to give it specific instructions about a section or about a client need or client desire, I'm not surprised.

**Matthew Panzarino:** I don't think that everybody is going to have great results with no instructions at all, right?

**Matthew Panzarino:** It's somewhere in between, and it is client-specific.

**Matthew Panzarino:** There's a reason that the box exists.

**Matthew Panzarino:** Otherwise, we would just have a topic, right?

**Matthew Panzarino:** So you're going to have to adjust per client.

**Matthew Panzarino:** As Kerry mentioned, you can even ask it questions you'd like the research to cover.

**Matthew Panzarino:** Like, it is a prompt, right?

**Matthew Panzarino:** It's just a prompt that goes into the pipeline that does the tasks.

**Matthew Panzarino:** So you can adjust it according to your needs.

**Matthew Panzarino:** However, I want to talk about, like, our major KPI.

**Matthew Panzarino:** I'll distribute something in more detail on KPIs.

**Matthew Panzarino:** But the major KPI for my organization, all EMEs, is time to delivery post-pipeline.

**Matthew Panzarino:** That's your KPI.

**Matthew Panzarino:** If that goes down, we win.

**Matthew Panzarino:** If that doesn't go down, we don't exist as a company.

**Matthew Panzarino:** So it is from the moment that the pipeline is finished running, how long does it take you to deliver that piece of content to client-ready state?

**Matthew Panzarino:** That's the prime directive.

**Matthew Panzarino:** Make that number go down.

**Matthew Panzarino:** Now, there are a bunch of levers that you can pull to make that number go down.

**Matthew Panzarino:** And we talked about some of them just now.

**Matthew Panzarino:** Artifact conflict, better assignment directions, manipulating the pipeline in some ways.

**Matthew Panzarino:** Eng is here to help.

**Matthew Panzarino:** I'm here to help.

**Matthew Panzarino:** Peer review is here to help.

**Matthew Panzarino:** Dan is here to help.

**Matthew Panzarino:** We'll figure out what needs to happen to the pipeline to help you.

**Matthew Panzarino:** But there are also other levers.

**Matthew Panzarino:** Process, which is you.

**Matthew Panzarino:** So like your experience and familiarity with the processes, with what the workflows do, all of that stuff.

**Matthew Panzarino:** And then of course, feedback.

**Matthew Panzarino:** Like if you're getting feedback, or basically you are generating feedback, as you edit the articles, you need to be really clear and articulate about what is not happening that you want to happen, or what is happening that you don't want to happen.

**Matthew Panzarino:** And then we find a way to parse that into which lever to pull.

**Matthew Panzarino:** Like it does that, is that an assignment direction problem?

**Matthew Panzarino:** Is it an artifact issue?

**Matthew Panzarino:** Is it a workflow that needs to be added?

**Matthew Panzarino:** Is it a workflow that needs to be removed?

**Matthew Panzarino:** Is it a workflow that needs to be updated or changed?

**Matthew Panzarino:** Is it an engineering issue?

**Matthew Panzarino:** Is it like this workflow is just failing at its job over and over, and maybe it can jump in and help you with either internal workflow adjustments, or adding an additional workflow that does something specific?

**Matthew Panzarino:** But earlier on, as Dan was mentioning, like sometimes it's useful to have a workflow that applies CTA specifically, this is completely possible.

**Matthew Panzarino:** Not only that, but it doesn't even require engineering, it'll

**Matthew Panzarino:** take you about 15 minutes to do, right?

**Matthew Panzarino:** So if you are, if you have in your assignment directions, please write a CTA, but you're like, ah, it's writing the wrong kind of CTA.

**Matthew Panzarino:** I really wanted to write this kind.

**Matthew Panzarino:** And you have five or six examples of good, you can drop those into an article and have a workflow that calls that artifact and then puts a CTA like that into your article for you automatically.

**Matthew Panzarino:** Like, why are you having, why do you have a Google Doc with a bunch of good CTAs that you're copying and pasting and then tweaking in your article every time?

**Matthew Panzarino:** That's 15 minutes, right?

**Matthew Panzarino:** That's 12 minutes.

**Matthew Panzarino:** Like, why are you doing anything manually that can be repeated over and over?

**Matthew Panzarino:** And so, like, that question, to fulfill that prime directive, to make that number go down, the question you need to ask every day is, hey, what did I do today that I cannot do tomorrow to this article, to this output?

**Matthew Panzarino:** And if there's anything in there that you cannot do tomorrow or that you don't want to do tomorrow that you know you're going to have to do tomorrow?

**Matthew Panzarino:** tomorrow, you

**Matthew Panzarino:** We'll find a way to eliminate it from your list of things to do, right?

**Matthew Panzarino:** So your post-processing checklist gets shorter and shorter until it's one item.

**Matthew Panzarino:** And that item is add my special sauce, je ne sais quoi, to this article.

**Matthew Panzarino:** That's your only task is to get a well-written article out and go, you know what?

**Matthew Panzarino:** Stylistically, I think this or I just think this is going to buy better or this will perform better.

**Matthew Panzarino:** Let's not forget performance, right?

**Matthew Panzarino:** Like, and you're going to make your tweaks and then you're going to deliver it to the client.

**Matthew Panzarino:** The golden path goal here for that metric is 15 minutes.

**Matthew Panzarino:** If you can't get a piece of content out of the pipeline and spend under 15 minutes on it before it's client ready, then you have work to do.

**Matthew Panzarino:** And we all have work to do together to figure out how to get you there.

**Matthew Panzarino:** I just want to put those things out there really clearly.

**Matthew Panzarino:** That's the number we want it to go down and the goal is 15 minutes.

**Matthew Panzarino:** Like, that's, that's where we're headed.

**Matthew Panzarino:** Now, to get there, we have to measure it, right?

**Matthew Panzarino:** And to measure it, we've been exploring different tracking options for that.

**Matthew Panzarino:** I've got a couple of options out there that have APIs, and I'm looking for ways to help them help get those set up.

**Matthew Panzarino:** That's my next meeting after this.

**Matthew Panzarino:** But we'll figure out ways to help you clock it.

**Matthew Panzarino:** Yeah, Will, like clocking it yourself is great.

**Matthew Panzarino:** Like, any way you can clock it yourself with, like, a Pomodoro timer or a simple timer on your, on your computer or an app, whatever you want to do for now to, to kind of start tracking it for yourself, that's great.

**Matthew Panzarino:** I'm trying to work on a more holistic method, long-term, that will help basically align with, like, specific assignments.

**Matthew Panzarino:** Assignments.

**Matthew Panzarino:** So, let's say you run something in Atlas, and you've got a, you know, you've got RAMP, and it's got this article, and you want to know how long it took you to get that article client ready.

**Matthew Panzarino:** There should be a way to...

**Matthew Panzarino:** Trigger, based on that task, hey, create a task for you to edit this article, and then you can start that timer, and then edit your article in whatever apps you choose.

**Matthew Panzarino:** I know we're all over the place still.

**Matthew Panzarino:** We're not all living in Atlas yet because ContentOS is not complete.

**Matthew Panzarino:** But you're going to do whatever you do, and then you're going to stop the timer, and we're going to get a view of what it takes to get those articles out on a holistic, real-world level across the organization station.

**Matthew Panzarino:** Yes, Carrie?

**Matthew Panzarino:** Yeah, pause.

**Carrie Chowske:** I don't know if it would be helpful to anybody.

**Carrie Chowske:** mean, not if you think that, like, me showing an example.

**Carrie Chowske:** Because I have two really good ones of, like, what the input is capable of doing, and then, like, what conflict will do to it if you have a conflict in there.

**Carrie Chowske:** I don't know if anyone wants to see that.

**Carrie Chowske:** If you want to see it and whatever, I'm happy to share my screen and show you, because I had this happen to me yesterday.

**Matthew Panzarino:** Yes, you're awake.

**Carrie Chowske:** Okay, now I'm just going to figure out which one I'm in.

**Carrie Chowske:** Hold on.

**Matthew Panzarino:** Yeah.

**Carrie Chowske:** So, this is...

**Carrie Chowske:** For Alex.ai, and they have like a very specific way they do their TLDR, and the pipeline has this step in here for adding a TLDR, and I have this in the guidelines here, and I'm still reviewing this one for Stevie, so I had the time to send this back and kind of ask her this question, but like, I'm thinking the answer here is actually to remove the FAQ step because it's doing it okay on its own, but I'm asking it, giving it the guidelines for the FAQ section because the drafter doesn't automatically add that, and I didn't even notice that it had an FAQ TLDR edition thing, but it has that here, and it also has the TLDR part in here as well.

**Carrie Chowske:** So, obviously, when it goes to do this, it's going to mess it all up, which it does, because it gives me the exact thing that I asked it for, and then when it goes to do the FAQ step, it adds in this crazy- TLDR thing here, and I end up with like...

**Carrie Chowske:** Twice as many FAQs, right?

**Carrie Chowske:** So that's the conflict that I'm having.

**Carrie Chowske:** But what's interesting is that this additional step doesn't seem to be any better at doing it than the original input was at doing it.

**Carrie Chowske:** So, like, for me, I'm like, can we just delete this step?

**Carrie Chowske:** It makes the run a little bit faster.

**Carrie Chowske:** But this is literally all I've given.

**Carrie Chowske:** This is the most.

**Carrie Chowske:** This is the most extensive guidelines I've given the agentic pipeline yet.

**Carrie Chowske:** And I don't think I'd ever get more complex than this, which is literally because they have so many specific formatting.

**Carrie Chowske:** Things for each section that I want to reinforce.

**Carrie Chowske:** That's writing guidelines, but it seems to help it to have a little more.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Anyway, I don't if anyone wants to go look at what I'm doing here.

**Carrie Chowske:** This is an Alex AI.

**Matthew Panzarino:** Yeah, sounds good.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** And, yeah, exactly.

**Matthew Panzarino:** Like, a step like that could be useful, but it could be unnecessary.

**Matthew Panzarino:** Like, and I would absolutely try the easier version first.

**Matthew Panzarino:** You know, just, like, put it in assignment directions, see how it does.

**Matthew Panzarino:** Does it deliver well?

**Matthew Panzarino:** And if it doesn't, or if they have some, like, crazy hyper-specific requirements where you...

**Matthew Panzarino:** You need to build like a detailed examples of good artifacts where it says like, do it like this, please don't do it like this, do it like this, which some clients do, we all know, they have very specific desires.

**Matthew Panzarino:** You can also implement it that way.

**Matthew Panzarino:** So whatever works, if you see a step though like that, especially if you walk through your workflow and you're like, this was good and then this step screwed it up, like, hey, easy call, right?

**Matthew Panzarino:** Don't do that step.

**Matthew Panzarino:** Take that workflow out or adjust the instructions or whatever you need to do.

**Matthew Panzarino:** And that's why walking through the workflow and seeing what it's actually doing is super important because you can see the before and after.

**Matthew Panzarino:** There's a reason there's an input and output for each section because you can say, hey, here's what this did and here's what that did.

**Matthew Panzarino:** So, you know, that's kind of where we're at.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** You know, Saskia, think, I think a lot of people would have a similar experience, but frankly, like there is a, I want to give you some wiggle room here.

**Matthew Panzarino:** I just don't want to give you too much lead because I feel people get themselves tangled in the rope.

**Matthew Panzarino:** I don't want to pull this analogy too far, but I think it's important to have some wiggle room.

**Matthew Panzarino:** So like if Will's having some success, putting in additional details, okay, cool.

**Matthew Panzarino:** You know, like it's not evil, but are you able to hit that 15 minute target with that?

**Matthew Panzarino:** Great.

**Matthew Panzarino:** If not, then maybe a re-negotiation of your approach is in order, right?

**Matthew Panzarino:** And it does not have to be you have to burn it all down and start over or whatever, but I just want to kind of be clear about some of the levers that you have to pull and that those levers are really important.

**Matthew Panzarino:** One other, this is almost a side note, but I want to mention it is like, if you are telling your, in your writing guidelines, if you're giving it instructions about things like headers or whatever, and then you explicitly write things like that in other artifacts.

**Matthew Panzarino:** Wait, search for those conflicts, too.

**Matthew Panzarino:** I'll give you one example.

**Matthew Panzarino:** In the writing guidelines for one client, it was like, don't use colons in headers or titles.

**Matthew Panzarino:** Fair enough, right?

**Matthew Panzarino:** I don't like them either.

**Matthew Panzarino:** I think they're a kludge.

**Matthew Panzarino:** The topic that was being fed to the workflow had a colon in it, right?

**Matthew Panzarino:** Like, you're basically prompting it, write like this, and then later on you're saying, don't write like that.

**Matthew Panzarino:** How does it decide, right?

**Matthew Panzarino:** Like, God told me not to eat meat, and then God told me to eat meat.

**Matthew Panzarino:** Like, which, you know, what do I do?

**Matthew Panzarino:** Do I eat or do I not eat?

**Matthew Panzarino:** You know, and you go around and around.

**Matthew Panzarino:** And like, I think that's, that is where we end up with an issue.

**Matthew Panzarino:** I think because the workflows and inputs and all of that are like laid out this way, we tend to think of them as divorced from one another, and they're not.

**Matthew Panzarino:** Like, it's all one prompt.

**Matthew Panzarino:** prompt.

**Matthew Panzarino:** Slash context package, right?

**Matthew Panzarino:** Because that's the way the workflows handle it in the backend.

**Matthew Panzarino:** They take all of your context and compile it, and then they take your instruction set and run it with that context.

**Matthew Panzarino:** And like it treats it as one big task.

**Matthew Panzarino:** So think about all of the things that you are telling it from the topic on down and be really, really clear and even use Claude or use other tools to identify any conflicts or incongruities or inconsistencies in logic between them or any potential to misinterpret your instructions.

**Matthew Panzarino:** So if you're like, blah, blah, blah, colon, blah, blah, blah.

**Matthew Panzarino:** And then in the writing guidelines, says, oh, don't use colons.

**Matthew Panzarino:** And you're like, why is my article so full of colons?

**Matthew Panzarino:** Well, well, so keep an eye on that stuff.

**Matthew Panzarino:** And frankly, for your topics, I don't care what the keyword research said.

**Matthew Panzarino:** Like as long as the keywords in the title, like write a good title, just write a good title, you know, right?

**Matthew Panzarino:** Put a normal human-readable title into the topic, and you will get better results.

**Matthew Panzarino:** You know?

**Matthew Panzarino:** Yes, Yana?

**Iana Medvedeva:** There's a little thing that I was doing with the writing guidelines.

**Iana Medvedeva:** I only started, but I think it's important to do.

**Iana Medvedeva:** Ask Cloud to check if all examples in the writing guidelines, proofreader checklist, everywhere where you put examples, follow these writing guidelines.

**Iana Medvedeva:** Because what Cloud likes to do is to provide an example that shows one rule, but breaks other rule in a way.

**Iana Medvedeva:** And this is where drafter can also break.

**Matthew Panzarino:** Yeah, yeah, exactly.

**Matthew Panzarino:** The other day I was looking, well, when I did my content audit, right?

**Matthew Panzarino:** So I was running an audit on some pieces.

**Matthew Panzarino:** I built an audit pipeline.

**Matthew Panzarino:** I'll try and publicize that as soon as I feel it's ready.

**Matthew Panzarino:** But I was running some content audits, and it was basically saying, hey, these contextual artifacts have examples of good in them that have m-dashes.

**Matthew Panzarino:** And And

**Matthew Panzarino:** And you're telling it, don't write M-dashes.

**Matthew Panzarino:** And it's like, then why are you giving examples of good that have M-dashes?

**Matthew Panzarino:** And they're unrelated to M-dash removal, right?

**Matthew Panzarino:** They may be in like a CTA section or in some other section where you're saying, hey, write like this.

**Matthew Panzarino:** And there's an M-dash in there, right?

**Matthew Panzarino:** And then you tell it later on, never use M-dashes.

**Matthew Panzarino:** But you've given it an example of good that has M-dashes.

**Matthew Panzarino:** And so you're like saying, never use garlic in my food.

**Matthew Panzarino:** And then you're like, you know, feeding it garlic.

**Matthew Panzarino:** And it's like, I don't know, you know, I don't know what to do.

**Matthew Panzarino:** So keep an eye out for that.

**Matthew Panzarino:** Yeah, yeah, exactly.

**Matthew Panzarino:** The writing guidelines, oh, yes.

**Matthew Panzarino:** Really, honestly, holistically, it should be this.

**Matthew Panzarino:** The writing guidelines should be written like the writing guidelines.

**Matthew Panzarino:** Like, don't use  in the writing guidelines.

**Matthew Panzarino:** Sorry, sorry, sorry.

**Matthew Panzarino:** Don't use stuff in the writing guidelines that you don't want to be used in the articles.

**Matthew Panzarino:** Because that is its context that it's working from.

**Matthew Panzarino:** So, you know, be careful.

**Matthew Panzarino:** Obviously, there's some formatting stuff that you need to have in there.

**Matthew Panzarino:** You know, bullet points, etc.

**Matthew Panzarino:** I get

**Matthew Panzarino:** But, you know, be careful about the context documents and stuff like that.

**Matthew Panzarino:** It's, you know, it could be a huge improvement.

**Matthew Panzarino:** So, oh, interesting, Kavishka.

**Matthew Panzarino:** That's an interesting take on it.

**Matthew Panzarino:** Yeah, I don't think I've done that, but that makes sense.

**Matthew Panzarino:** So, like, using the writing guidelines to run your context artifacts against and say, hey, do these artifacts, like, adhere to these writing guidelines?

**Matthew Panzarino:** But, yeah, be careful on that because I think it could be a major issue.

**Matthew Panzarino:** So, sweet.

**Matthew Panzarino:** Any other questions or anything in the last few minutes?

**Matthew Panzarino:** Just wanted to cover those major points today.

**Matthew Panzarino:** And I promised a return to on-screen demos and messing around and all that stuff.

**Matthew Panzarino:** But I wanted to establish some big anchor points for you to check.

**Matthew Panzarino:** I think all of these are vital and will improve your processes.

**Ehtisham Hussain:** So, maybe a stupid question, but I just wanted to make sure I have clarity on this.

**Ehtisham Hussain:** So, to do-

**Ehtisham Hussain:** Conflict checks on artifacts, do I just feed them into flawed and ask them to ask it to do a conflict?

**Matthew Panzarino:** Yeah, the word just is doing a lot of work in your sentence there, so yes, you do, but as I mentioned earlier, and I think you can go back and check the transcript, or we'll actually try and produce something for you based on this, like, hey, here's what we'd suggest.

**Matthew Panzarino:** Um, you can, yeah, you can do conflict checks very, at a base level, it's easy to do them in any project you already have set up with the artifacts themselves, especially if it's a project that you use to manipulate artifacts, like to add or remove stuff, you can give it, I actually just paste them right into the chat again, you know, even though it already has them in the project.

**Matthew Panzarino:** And say, hey, please run a conflict pass against these.

**Matthew Panzarino:** But once again, as I said earlier, I also think it is very important context for it to have the pipeline.

**Matthew Panzarino:** So you can just grab the YAML code of the pipeline and put that to your project.

**Matthew Panzarino:** Project context, because you're telling it this is the order in which these are applied, and these are taken as inputs together, these are taken as inputs sequentially, et cetera, because they can say to you, hey, this actually seems like a conflict because you're executing this after this, and in reality, it's going to correct these things that you told it to do earlier, right?

**Matthew Panzarino:** so I think that that's wise, and then I like to just kind of pump a bit, talk to it about its job, what it's about to do, you know, I've given you these contextual artifacts, would you go ahead and read them for me and see what's up?

**Matthew Panzarino:** It's like, cool, I've read them, okay, great, now I'd like you to do a conflict pass, I'd like you to check for internal conflicts within the documents themselves, you can even do those one at a time, if you wish, just for clarity, and then you can say, now I'd also like you to check for conflicts between these artifacts and these assignment directions, and tell me if there is any potential for collision, conflicts, looping, et cetera.

**Matthew Panzarino:** I also like to give it...

**Matthew Panzarino:** Personally, the agentic documentation, so like you can go grab the documentation in Notion under Atlas for agentic pipelines and what they do, we just wrote it, it's fresh, it's reasonably up to date, they ship updates all the time, but you can grab it and give that to the project as well, because then it understands the agentic process that these are being executed under.

**Matthew Panzarino:** And it can say, hey, there's a potential here for it to create unnecessary, you know, repetitions or loops or whatever.

**Matthew Panzarino:** So the more context you can give it about the job it's going to do, the better.

**Matthew Panzarino:** We probably should and will, and Marcus has already built some tools for himself, build a tool into Atlas to like run conflict checks.

**Matthew Panzarino:** And frankly, it should probably happen automatically, because humans are humans, and we're all busy, right?

**Matthew Panzarino:** And so it's probably a thing that should trigger.

**Matthew Panzarino:** And then it'll tell you, it'll give you a report in your client space where it's like, warning, red pill, neon, you've got

**Matthew Panzarino:** Some conflicts in your artifacts, right?

**Matthew Panzarino:** But for now, this is the process that I recommend.

**Matthew Panzarino:** That's the way I recommend you do that.

**Matthew Panzarino:** That make sense?

**Ehtisham Hussain:** Yeah, yeah.

**Matthew Panzarino:** That makes sense.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** Conflict between them and then conflict internally.

**Matthew Panzarino:** Because we all know that these artifacts tend to swell in size.

**Matthew Panzarino:** You know, the more feedback that the client gives us and the longer we've been servicing the client, they have more and more, you know, specific needs.

**Matthew Panzarino:** Sometimes they have stakeholders with a lot of opinions and you end up with a bigger document than you started out with.

**Matthew Panzarino:** And so internally, you can have conflicts.

**Matthew Panzarino:** Because that artifact could have been updated by a half dozen people by now, right?

**Matthew Panzarino:** And so you never know whether there was some issue there.

**Carrie Chowske:** It caught some things that I wouldn't have considered conflicts if I read it.

**Carrie Chowske:** Like, because it's kind of, it's interpreting it with its own, with an LLM's nuance, right?

**Carrie Chowske:** So it's not using a human brain to go, yeah, this friggin' makes sense.

**Carrie Chowske:** It's just going, this doesn't agree with it.

**Carrie Chowske:** Because it's not worded similarly enough for me to recognize it as the same.

**Carrie Chowske:** So like even that, like I had something where it's like to lowercase something as a concept, but, you know, uppercase as a feature name, right?

**Matthew Panzarino:** Very common thing that we have to do.

**Carrie Chowske:** And it caught that even though it said it correctly, it didn't clarify that, oh, but when you use the product name, you can capitalize it.

**Carrie Chowske:** And so it was giving a conflict every time on that.

**Matthew Panzarino:** And I wouldn't have thought that was a conflict because to me it was obvious.

**Matthew Panzarino:** Yeah, and you can have it help you write logic too.

**Matthew Panzarino:** I'll answer your question in a second, Saskia, but you can have it help you write logic as well, right?

**Matthew Panzarino:** So if you are saying, if it gives you something about a conflict there or whatever, you can say like, hey, help me write a logical instruction set that is, you know, to be interpreted by an LLM, right?

**Matthew Panzarino:** You know, like you, that explains this pretty tough concept.

**Matthew Panzarino:** Like as an example for Biologica, we needed saffron to be mentioned as an ingredient with a lowercase, but if...

**Matthew Panzarino:** was mentioned in the product context.

**Matthew Panzarino:** It was Afron, Saffron, TM, right?

**Matthew Panzarino:** And these rules get complicated, right?

**Matthew Panzarino:** Because like, oh, in this context, mention it as a product name.

**Matthew Panzarino:** In this context, don't mention it as a product name.

**Matthew Panzarino:** But in these instances, there can be a, you know, whatever.

**Matthew Panzarino:** You can have it help you write logic.

**Matthew Panzarino:** Have it help you untangle logic puzzles so that you're giving it the proper instructions.

**Matthew Panzarino:** Um, yeah, Saskia, so like, I do not know, I do not think it's about length necessarily.

**Matthew Panzarino:** mean, short is a byproduct of keeping it simple, you know?

**Matthew Panzarino:** Um, I don't know that, oh, examples, I mentioned this on a previous call of this, by the way, but if you give it examples, give it just a contextual example in a paragraph, and then leave it at that.

**Matthew Panzarino:** Don't give it like a bunch of random sentences.

**Matthew Panzarino:** It's like, don't write sentences like this, because it doesn't have context for how the sentences would be used.

**Matthew Panzarino:** So just give it like a paragraph and say, write like this, and then, you know, or don't write like this.

**Matthew Panzarino:** Um,

**Matthew Panzarino:** If you have specific formats that you needed to follow, it can be useful to have a separate workflow that adjusts the format of a section or inserts a section with hyper-specific formatting on its own so that you have the space to do that task holistically on its own, like, hey, just please do this.

**Matthew Panzarino:** It can be useful to isolate issues and to help you create a better outcome without having to be like, oh, no, how do I adjust this 2,000-word document to, like, produce this desired outcome?

**Matthew Panzarino:** I think one instance of it is we had a client that has a CTA that they wanted to be narratively integrated.

**Matthew Panzarino:** So instead of, like, hey, insert this CTA every time, which is fairly easy to do in writing guidelines, you can say, like, this is the CTA you use.

**Matthew Panzarino:** Just don't use a different CTA.

**Matthew Panzarino:** But in this context, they wanted basically to replace the...

**Matthew Panzarino:** Conclusion with like a weaving of a narrative conclusion and a CTA.

**Matthew Panzarino:** And to do that, it's like you would spend hours trying to write the logic of that out saying like write, you know, three sentences of narrative, insert a brief mention of the product and back to the narrative and then, you know, weave the product value in blah, blah, blah, blah, blah.

**Matthew Panzarino:** You don't have to do that.

**Matthew Panzarino:** You find a couple of examples of good that the client has approved and that they like and then you put those into an artifact.

**Matthew Panzarino:** And then you add a workflow that calls that artifact and adds a CTA.

**Matthew Panzarino:** write instructions for that workflow that says, hey, please add a CTA that is formatted like this and at this place in the article.

**Matthew Panzarino:** The danger with that is that it can feel disjointed.

**Matthew Panzarino:** It can be difficult for it to insert stuff later.

**Matthew Panzarino:** And, you know, and, and also remember the conflict and ordering matters here.

**Matthew Panzarino:** So you can be inserting something that doesn't.

**Matthew Panzarino:** Adhere to writing guidelines, or that creates a conflict with your writing guidelines, and those writing guidelines have already been applied, and then it's moving on with its day, and you're wondering, why does this have an M-dash, or why is this formatted this weird way?

**Matthew Panzarino:** Well, because you added it after.

**Matthew Panzarino:** Like, it has no context to the writing guidelines, or whatever.

**Matthew Panzarino:** So there are ways to combat that.

**Matthew Panzarino:** I would say you should try to just get it done with assignment directions, or writing guidelines, but if you run into issues, we can add that.

**Matthew Panzarino:** Sometimes it's very useful to add things like comparison tables, or things like that, that you need formatted in a very hyper-specific way.

**Matthew Panzarino:** And this is the way that many of the PSCO workflows work.

**Matthew Panzarino:** Like, they have a very specific structure they need to follow, and each workflow builds a thing, and then ships that thing into the overall deliverable, and then at the end, you've got it all packaged, right?

**Matthew Panzarino:** So this is totally possible, but I think it's wise to try to get it done in the assignment directions.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** right.

**Matthew Panzarino:** Writing guidelines first, and then if you're having a heck of a time, and you see that number could go down significantly if you just did this, then we can add a workflow.

**Saskia Wartnaby:** And what's, sorry, thank you for answering that question, but what's better, like, what do you put in the writing guidelines, and what would you put in the assignment direction that would be, like, different, if that makes sense?

**Matthew Panzarino:** Writing guidelines should be how, and assignment should be what.

**Matthew Panzarino:** So, I really just feel like, just boil it down to that.

**Matthew Panzarino:** If you can ask yourself, is this how I'm doing it, then it should live in writing guidelines.

**Matthew Panzarino:** Now, is some reinforcement, as long as it's not conflicting, fine in assignment directions?

**Matthew Panzarino:** Absolutely.

**Matthew Panzarino:** You know, you can say, like, hey, make sure the section's brief and concise, and then the writing guidelines also say, we want our writing brief and concise.

**Matthew Panzarino:** It is totally fine to do reinforcements, and many people have had some success with reinforcements in there because it is a prompt, right?

**Matthew Panzarino:** So, you're giving it a line.

**Matthew Panzarino:** So,

**Matthew Panzarino:** instructions throughout the thing, but you don't need to belabor the point, like don't rewrite writing guidelines in the assignment directions, that usually just means writing guidelines are not appropriately written, if you're having, you know, if it's not doing the thing it says in writing guidelines.

**Matthew Panzarino:** Cool.

**Mariana Marins:** I will just chime in, because CTAs for me are the hardest thing to do, because you guys have multiple clients, you'll probably see this.

**Mariana Marins:** Some clients will want one CTA at the end, and that's easy, that's the easiest one to do, but if they want something in the body of the article that fits naturally and stuff, it will be more difficult to do, both with a specific step and with the specific artifact of CTAs.

**Mariana Marins:** So, for CTAs or intros, because it's CTAs that come in the end, in the conclusion, let's say, and intros.

**Mariana Marins:** No.

**Mariana Marins:** Thank

**Mariana Marins:** Because it's the first paragraph.

**Mariana Marins:** So those things that you can easily isolate.

**Mariana Marins:** I would say that an artifact with examples of that.

**Mariana Marins:** So an artifact with intros, five intros, five CTAs, work well.

**Mariana Marins:** But if you want something naturally within the body of the article, I would say that the best artifact is the example articles.

**Mariana Marins:** So you have one artifact that has complete articles, two or three.

**Mariana Marins:** And that will show the pipeline, the complete structure, and how to naturally insert it.

**Mariana Marins:** Because once it's in the middle of the article, the pipeline needs the whole context of the article.

**Mariana Marins:** So if you just have one step to put it in the middle, it will not consider the rest of the article and the whole context.

**Mariana Marins:** So it is a bit tricky.

**Matthew Panzarino:** With CTAs, depending on where they are, it gets a bit tricky.

**Matthew Panzarino:** Yeah, if you're having issues with narratively integrated stuff like that.

**Matthew Panzarino:** I have had some success in giving, as Nana mentioned, putting an artifact with the articles in it, like a couple of good articles in it, and then integrating that in the article drafter.

**Matthew Panzarino:** So you can update the article draft workflow to say, please check this artifact as well, for examples of how narratively integrated, well-integrated CCAs are, or look.

**Matthew Panzarino:** And then it can apply that at the draft stage.

**Matthew Panzarino:** So remember that the article drafter is not sacrosanct either.

**Matthew Panzarino:** It can call additional artifacts for context.

**Matthew Panzarino:** By default, it calls writing guidelines, research, company context, and audience personas.

**Matthew Panzarino:** But it can call other artifacts if your client has specific needs.

**Matthew Panzarino:** And once again, this should be in service of reducing that time.

**Matthew Panzarino:** So if you're like, hey, I have to go insert this myself because I feel like only a human could do this.

**Matthew Panzarino:** Cool, how can we make a robot do it, right?

**Matthew Panzarino:** And we'll figure it out.

**Matthew Panzarino:** But, okay.

**Matthew Panzarino:** We have to go, I have to go prepare for next meeting, but thank you all very much.

**Matthew Panzarino:** I appreciate it.

**Matthew Panzarino:** We'll try and circulate some of those documents that we promised and all that, but ciao, ciao.
