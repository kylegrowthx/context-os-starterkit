# CMs Standup – Atlas Sync

<metadata>
date: 2025-09-17
time: 15:27 UTC
duration: 45 minutes
organizer: Patrícia Contreiras (GrowthX)
participants: Matthew Panzarino, Iana Medvedeva, Sucheta Biswas, Tiandra Burns, Jenn Peters, Patrícia Contreiras, Oluwatimilehin Ademosu, Mariana Marins, Bisera Stankovska, Fatima Tahir, Simran Sethi, Ehtisham Hussain, Usman Adepoju, Martha Martins, Ismail Ajagbe, Ademilade Shodipe-dosunmu, Josip Sovar, Matthew Alves-Hill, Carrie Chowske, Rachel Pasche, Saskia Wartnaby, Vivek Mishra, Usman Ghani, Nika Narimanidze, Jessalynn White, Feyisayo Adekunle, Sydney Go, Jenny Macrohon Dabon, Kavishka Kanayake, Bailey Seybolt, Nathalie Schrans
fathom_recording_id: 87898372
fathom_url: https://fathom.video/calls/412194872
share_url: https://fathom.video/share/CGUrzvAe7zyuW-Qe3sc-34c-iATsQc2U
source: fathom
enriched_on: 2026-03-03 18:30 UTC
</metadata>

---

## Summary

Matthew Panzarino led a deep dive on agentic pipelines, which are replacing the older segmentation-based pipelines by processing entire articles at once with built-in validation and post-processing workflows that achieve 80%+ confidence scoring. The team discussed how each CM should document their current manual editing processes and leverage Cloud Projects to capture the specific rules, prompts, and instruction sets needed for their client accounts — this documentation will directly inform the engineering of client-specific agentic pipelines. The core insight: all the repetitive work CMs do now (validation, CTA formatting, trademark consistency, etc.) should be systematized into prompt libraries and evaluation rubrics, which the pipeline will then automate at scale.

---

## Context

This is an internal GrowthX team standup for the content management (CM) team. Matthew Panzarino, who appears to lead the technical strategy for the Monograph project and pipeline architecture, brought the team together to explain a major technology shift from the old segmentation-based article pipelines to new agentic pipelines. The meeting was recorded by Patrícia Contreiras and attended by approximately 32 team members across various roles (CMs, engineers, and supporting staff). The context is that GrowthX has been delivering B2B content marketing services ($200k+/year engagements) with Monograph as a key client platform, and they're now transitioning to AI-powered workflows that automate the repetitive work CMs currently do manually — validation, formatting, consistency checks, and revision cycles. The agentic pipeline approach leverages newer LLM capabilities (larger token windows) that weren't available a year ago, making it possible to process entire articles in one coherent pass rather than segmenting and reassembling them.

---

## Relevance

- **To GrowthX Delivery:** Agentic pipelines are now rolling out across client accounts, replacing the 2-year-old segmentation approach. Each CM must document their client-specific editing rules, validation steps, and prompt libraries in Cloud Projects to enable engineers to build client-specific pipeline variants. Matthew emphasized that the post-processing validation workflow (confidence scoring to 80%+ before delivery) directly mirrors the manual QA work CMs currently do — systematizing this is critical. Monograph outputs are showing 80%+ confidence scores with correctly formatted CTAs, FAQ sections, trademark consistency, and SCTA formatting.

- **To CheckThat:** The discussion touched on research tool improvements for agentic pipelines — Perplexity is being used for Abnormal's vertical research, and there's interest in accessing Exa for more advanced research artifact selection. Sucheta Biswas was tasked with reaching out to Marisol for best practices on recent statistics retrieval, which informs how the pipeline sources and validates research claims.

- **To GrowthX Business Development:** Pipeline automation directly improves project margins by reducing CM hours spent on repetitive validation and revision work. Monograph articles are now achieving quality gates in 10-12 minutes of total pipeline runtime (vs. hours of manual editing previously), freeing CMs to focus on high-leverage strategy work and account expansion. This efficiency gain is a competitive advantage in B2B content delivery.

---

## Overview

- Agentic pipelines are being rolled out, offering improved article generation with built-in validation and post-processing steps
- CMs should focus on building leverage by automating repetitive tasks and documenting their editing processes
- Cloud Projects are recommended for efficient work and to inform future pipeline improvements
- Precise, quantifiable instructions are crucial for effective prompts and evaluation steps in agentic pipelines

---

## Key Topics

### Trends from One-on-One Conversations

  - Many team members have developed their own processes for completing work efficiently
  - Opportunities exist to increase leverage by utilizing available tools, especially for repetitive tasks
  - Some accounts still face challenges with pipeline outputs requiring significant manual editing
  - Recommendation: Use Cloud Projects to automate repetitive tasks and inform future pipeline improvements

### Agentic Pipelines Overview

  - New pipelines work on entire articles at once, eliminating segmentation issues
  - Built-in validation steps ensure adherence to client requirements
  - Post-processing workflow includes evaluation reports and confidence scoring
  - No assignment generator in the current version; separate agentic assignment generator in development
  - Average pipeline run time is 10-12 minutes, with initial runs taking longer due to knowledge base building

### Prompt Libraries and Instructions

  - Importance of building and refining prompt libraries for each client
  - Critical thinking required when reviewing AI outputs to avoid compounding errors
  - Precise, quantifiable instructions are crucial for effective prompts and evaluation steps
  - Separate projects recommended for different tasks to maintain context clarity

### Research Tools and Techniques

  - Discussion on using Perplexity and potentially Exa for industry-specific research
  - Suggestion to specify recent time frames for up-to-date statistics
  - Potential future feature to select specific research artifacts for pipeline inputs

### Cloud Projects Usage

  - Clarification on the purpose of Cloud Projects: to increase efficiency and document processes
  - Recommendation to create projects for tasks performed at least once a month
  - Goal is to reduce time spent on repetitive tasks and allow for more strategic thinking

---

## Action Items

**Iana Medvedeva (GrowthX)**
- Review and refine prompts in writing guidelines and proofreader checklist, ensure quantifiable and precise instructions to avoid evaluation loops


**Sucheta Biswas (GrowthX)**
- Reach out to Marisol for tips on effective research using Perplexity, focus on recent statistics for Abnormal's industry vertical articles


**Tiandra Burns (GrowthX)**
- Continue building Cloud Project library only for tasks done at least once a month, focus on frequently used processes

---

## Transcript
**Matthew Panzarino:** Good morning, everyone.

**Matthew Panzarino:** How's everybody doing today?

**Patrícia Contreiras:** Good morning.

**Matthew Panzarino:** Morning, morning.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** I will take some time a little bit later on to just open the floor and have anybody bring up anything they want to bring up.

**Matthew Panzarino:** But I wanted to take a few minutes at the start to kind of talk about...

**Matthew Panzarino:** ...

**Matthew Panzarino:** Thank

**Matthew Panzarino:** Oh, the agentic pipelines, which are on their way to you.

**Matthew Panzarino:** Hello, by the way, Patrícia and Tamara.

**Matthew Panzarino:** Hi.

**Matthew Panzarino:** Welcome.

**Matthew Panzarino:** Everybody welcome them to their first.

**Matthew Panzarino:** Oh, and Kavishka, I think this is your first stand-up as well, I believe, if you didn't lurk before.

**Matthew Panzarino:** We try to do these once a month or so, and I'll try and touch on mainline stuff.

**Matthew Panzarino:** We were doing the stand-ups every week, but I just did a round-robin of, you know, conversations with all of you, so all of you have had some base time, and we've had a chance to talk about individual issues and things like that, which I will try to do about on the cadence of every month and a half or so.

**Matthew Panzarino:** It's hard to do it every month, because 14 calls in a week and a half every month is a little tough, but I would definitely try to make some time on a regular basis, because those conversations were very valuable.

**Matthew Panzarino:** So, Agenda is basically...

**Matthew Panzarino:** I'm talk a little bit about agentic pipelines.

**Matthew Panzarino:** I actually have changed my mind on the order of this.

**Matthew Panzarino:** I'm going to talk first a little bit about the things that I found when I was talking to all of you, not on a specific basis, but some trends, and then we can open the floor.

**Matthew Panzarino:** So first of all, on like a trends basis, there were a handful of things that I saw many of you talk about.

**Matthew Panzarino:** One, it was good to see that you had found your own processes for getting the work done and for figuring things out and for getting work out on time, which is great.

**Matthew Panzarino:** But I did see a lot of opportunities still for many of you, and I talked with some of you specifically about it, to increase your leverage by utilizing whatever tooling is available to you.

**Matthew Panzarino:** So the scenario that some of the accounts are in is that the pipeline is a little rocky for the type of work that we're producing for the client, whether that's the exact format or type or desires that they have, the pipeline production.

**Matthew Panzarino:** So what is coming out of it is still in rough shape, and there's a lot of work to be done between there and client deliverable.

**Matthew Panzarino:** And that is usually the best place to build leverage.

**Matthew Panzarino:** And usually you can use your own tools, like Cloud Projects is the way that I choose to go about it, to kind of help you perform repetitive tasks in editing and in fine-tuning.

**Matthew Panzarino:** And that serves two major goals.

**Matthew Panzarino:** One, it helps you save time now to get your deliverables out on time and make it feel a little less anxiety-driven to get your work done.

**Matthew Panzarino:** And then two, if you use a Cloud Project, it learns, it will adapt, and you will be able to use it when it comes time to roll out the agentic pipelines to inform the dev team about what exactly it needs to be done between the end of the pipeline.

**Matthew Panzarino:** So stuff runs through, it gets drafted, it comes up to the end of the pipeline.

**Matthew Panzarino:** The in the output stage, what do you do between there and the time you deliver it to the client?

**Matthew Panzarino:** All of you have some sort of process here.

**Matthew Panzarino:** And if it is, hey, I only spent a few minutes editing because the pipeline is working pretty well, congratulations.

**Matthew Panzarino:** That's awesome, right?

**Matthew Panzarino:** That's great.

**Matthew Panzarino:** But I have seen it's not the state for everyone.

**Matthew Panzarino:** And so if you perform processes there to get it from the end of the pipeline to client deliverable, which some of those processes are just some human touch-ups and editing.

**Matthew Panzarino:** But for many of you, I have seen it, it's pretty laborious tasks.

**Matthew Panzarino:** Like, oh, it does this always, and I always have to fix this, this structural issue, or this tone problem, whatever.

**Matthew Panzarino:** Automate your way into that, right?

**Matthew Panzarino:** Like, build your leverage there using tools like CloudProjects.

**Matthew Panzarino:** I'm always happy to dive deeper on those with you for those of you that I have not done so.

**Matthew Panzarino:** So the delta between the end of the pipeline and the customer deliverable...

**Matthew Panzarino:** It's basically what the objective pipelines are designed to fill, but they cannot rectify that.

**Matthew Panzarino:** They cannot make that stuff much more deliverable without knowing what is missing from the pipeline.

**Matthew Panzarino:** So that is what you're doing.

**Matthew Panzarino:** You're kind of collating a list or a process of things that really should be handled by the pipeline.

**Matthew Panzarino:** Because the ideal should be the pipeline does its work, and then you spend a handful of minutes editing, and then it's ready for client delivery.

**Matthew Panzarino:** Now, that's possible.

**Matthew Panzarino:** I've seen it work.

**Matthew Panzarino:** But you need to do the work to figure out what it is that you're missing so that we can put it in the pipeline and make the pipeline do those things, either through a combination of prompting, engineering, or additional workflows that do specific things that are needed by the client.

**Matthew Panzarino:** Basically, it's all about making your life easier and building you leverage.

**Matthew Panzarino:** So this is not in service of some nebulous goal.

**Matthew Panzarino:** It's literally for you.

**Matthew Panzarino:** Yes, kind of to the video it's my

**Matthew Panzarino:** My, I had, we've put together a little doc from our pod that basically lists all of the things, I think Iana did this, that lists all of the things that you should probably collect now, so that we're ready for building an agentic pipeline for your clients.

**Matthew Panzarino:** So I'll talk about the agentic pipelines in a second, but this document will, I wanted to shape it up a little bit, knock it around a little bit more, but it basically will give you a list of things to collect.

**Matthew Panzarino:** Things like, what is your prompt library?

**Matthew Panzarino:** What are the things that you do every time on this?

**Matthew Panzarino:** What are the additional contextual documents that you pull in to any cloud project or ChatGPT chat or anything that you're using to get the client, you know, deliverables done?

**Matthew Panzarino:** You need to collect those, because another thing that I've seen, a takeaway from what everybody's doing, is that it's all over the place, where like, oh yeah, I've got like a notes doc, you know, that I pull, that I, or Apple notes that I pull up.

**Matthew Panzarino:** Let's go,

**Matthew Panzarino:** prompts in it, or I've got, you know, this document in Google Docs and another one here, another one elsewhere.

**Matthew Panzarino:** That's just one of those things that needs to be collected because when it comes time to roll out the agentic pipeline or build it for your client, we need that information all in one place so an engineer can tackle it and engineer it into the pipeline.

**Matthew Panzarino:** So we'll get that document out and it'll probably take you, you know, half an hour, 45 minutes to put all the stuff together.

**Matthew Panzarino:** And it's not like every single thing in that document you will have or is necessary for your client, but many of the things will be applicable to almost everyone.

**Matthew Panzarino:** And the rationale for that, the reason for that is because we are starting to roll out the agentic pipelines to various accounts.

**Matthew Panzarino:** The way that the agentic pipelines work is significantly different from our current pipeline.

**Matthew Panzarino:** And I'll talk about kind of the ways that that is different.

**Matthew Panzarino:** So, uh,

**Matthew Panzarino:** In Monograph, as an example, we have the article generation pipeline.

**Matthew Panzarino:** This is the standard pipeline that many of you are still using and working with and are familiar with, where it goes through the kind of processes in these workflows and pulls your article forward through the various workflows, essentially sequentially.

**Matthew Panzarino:** One of the major things that I wanted to talk about, about the old pipelines, is that they work through a process called segmentation.

**Matthew Panzarino:** So they actually split the outline into sections, then they store the research done by the researcher in a Redis database, and then they perform the drafting task on each section, and then assemble it back later on.

**Matthew Panzarino:** So you can see this by looking at, looking at, looking at,

**Matthew Panzarino:** The prompts for this, so you can see that this article draft process is, hey, I have an article that I split into sections and gave to a different writer.

**Matthew Panzarino:** You're an editor-in-chief, you offer, this is, I think, not correct, but that's okay, we're moving on from these pipelines anyway, so I never got a chance to fix that, but the disjointed list of suggestions, I now need you to review this, make sure it's cohesive and easy to read.

**Matthew Panzarino:** And so, you can see what it's trying to do here, it's trying to make sure that there are transitions, remove redundant information that's already in other sections, identify and remove duplicate hyperlinks, keyword stuffing, you know, yada, yada, yada, punctuation, et cetera, right?

**Matthew Panzarino:** But this process of splitting the article into sections, working on each section, and then assembling it, I'm sure all of you have seen, at some point, this process does introduce oddities.

**Matthew Panzarino:** And it can be repetition.

**Matthew Panzarino:** It can be, you know, really hard left turns in transitions between one section and another.

**Matthew Panzarino:** You're like, wait a minute.

**Matthew Panzarino:** What are we talking about now?

**Matthew Panzarino:** And like that, it's just not, this was a byproduct of a couple of things, and I won't get too laborious about it, but the most important thing that it was a byproduct of is that the token windows were so much smaller August of last year.

**Matthew Panzarino:** You literally could not fit enough instructions into a command, into an instruction set to, an operation to enable you to work on the whole article at once.

**Matthew Panzarino:** So that is why the segmentation approach was necessary, but it is now outdated because we do have the ability to have a much larger token window.

**Matthew Panzarino:** So that is where the agentic pipelines are coming from.

**Matthew Panzarino:** They fix that problem by working on essentially the whole article at once.

**Matthew Panzarino:** They also do another thing in that they

**Matthew Panzarino:** They have validation built in.

**Matthew Panzarino:** So one of the things that I'm sure that you have all seen is that you can give it really well-written, precise commands, and it just ignores them, which is only natural, because this is the way LLMs work.

**Matthew Panzarino:** They prioritize, they act on things, and sometimes they lose the plot.

**Matthew Panzarino:** So there is a very important part of the agentic pipeline that I will point out here, and that is the post-processing workflow.

**Matthew Panzarino:** So in the validation step, the post-processing step, it basically says, hey, I could see the writing guidelines that you've given me.

**Matthew Panzarino:** I'm going to make some changes, and then I'm going to run a confidence scoring on those changes.

**Matthew Panzarino:** So you can see here, here's an evaluation report, right?

**Matthew Panzarino:** This article has good tone.

**Matthew Panzarino:** I see some critical issues in Monograph's instruction.

**Matthew Panzarino:** We have, of course, that they want MoneyGantt to have a trademark.

**Matthew Panzarino:** We want an SCTA in a very specific format.

**Matthew Panzarino:** And then we also want an FAQ that's saying, hey, you said you want these and they don't exist in this initial draft.

**Matthew Panzarino:** And then some high priority issues, EM dashes, long hyperlink text, dense text sections, things like that.

**Matthew Panzarino:** These are all born of our process to understand how the articles were coming out of the pipeline versus how we want to deliver them to Monograph, right?

**Matthew Panzarino:** So it runs this evaluation report and then goes back and fixes those changes, fixes those issues.

**Matthew Panzarino:** You can see here it fixed all that stuff.

**Matthew Panzarino:** Then it runs a confidence scoring, an evaluation on that.

**Matthew Panzarino:** And it says, hey, is this confidence score higher than 0.8 or basically is it 80% good?

**Matthew Panzarino:** And then if it's not, it runs it again.

**Matthew Panzarino:** And if it's not, it runs it again.

**Matthew Panzarino:** And if it's not, it runs it again.

**Matthew Panzarino:** it's not

**Matthew Panzarino:** So basically, it will run through, do a correction pass, do an eval, then make the correction pass again, then run an eval, et cetera, until it achieves a high confidence score.

**Matthew Panzarino:** And that's how you get an output that is adherent to the desires that you have.

**Matthew Panzarino:** So as an example, in this article here, scroll to the bottom, we've got an FAQ, right?

**Matthew Panzarino:** Oh, sorry.

**Matthew Panzarino:** File a ticket.

**Matthew Panzarino:** Okay, we've got an FAQ, you see here, frequently asked questions, right here, exactly as we asked it to.

**Matthew Panzarino:** And this CTA is exactly as we asked it to do for Monograph.

**Matthew Panzarino:** Monograph doesn't have traditional conclusions.

**Matthew Panzarino:** They have instead a concluding paragraph or two that segues into a CTA, and it does a really good job of it, typically, because of the instructions that we wrote.

**Matthew Panzarino:** And that is how you get this good, validated output, right?

**Matthew Panzarino:** And...

**Matthew Panzarino:** Like, you can see here, if you look, actually, it's not exposed here, sorry.

**Matthew Panzarino:** Internally, we can see it, but you can look at the actual evaluations and see what it's doing.

**Matthew Panzarino:** So if we might be able to show you here, if we look in flow, you can see the evaluation passes here, right, that it's done.

**Matthew Panzarino:** So it parses the instructions, it looks at the instruction set that you gave it, and we'll show it.

**Matthew Panzarino:** And then it will do the evaluation.

**Matthew Panzarino:** And you can see here, here's the report.

**Matthew Panzarino:** Here's the overall assessment, the strengths, the weaknesses, the requirements, and then the alignment score, right?

**Matthew Panzarino:** So it says, hey, does this have good alignment with the writing guideline validations?

**Matthew Panzarino:** Confidence score, 0.8, importance, critical, reasoning, article demonstrates strong adherence, right?

**Matthew Panzarino:** Then rule name, money gain consistency.

**Matthew Panzarino:** Each of these rules were things that we were...

**Matthew Panzarino:** Right?

**Matthew Panzarino:** It's like the stuff that you got to do to every article to get it compliant with what your client wants.

**Matthew Panzarino:** That process of deciding what these rules were, what these post-processing steps were, that came out of us actually working the articles manually, right?

**Matthew Panzarino:** Bare knuckling it until we figured out, okay, what makes a good article here?

**Matthew Panzarino:** And then we feed those instruction sets back in by putting them in the agentic pipeline, and now we're gold.

**Matthew Panzarino:** There are still some issues.

**Matthew Panzarino:** The agentic pipelines aren't rolled out to everyone because there are still some tweaks to be made.

**Matthew Panzarino:** But the overall results are much more adherent to what we want coming out of this pipeline within a handful of minutes of fact-checking or editing or doing your normal work.

**Matthew Panzarino:** But it's really dang good.

**Matthew Panzarino:** It's a lot better than it used to be.

**Matthew Panzarino:** And you'll notice another interesting thing about the agentic pipeline, it does not have

**Matthew Panzarino:** An assignment generator.

**Matthew Panzarino:** So it starts off at basically, hey, I'm going to start doing research on this topic and blast through.

**Matthew Panzarino:** You can do it this way, and it works fine.

**Matthew Panzarino:** But you can also provide it with assignment directions, and there's no assignment brief or outline generator to suddenly introduce any wackiness.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** Like, the problem with the outline generators is that they were working from a set number of templates.

**Matthew Panzarino:** And I don't want to go backwards too much.

**Matthew Panzarino:** This is more historical that I've talked to some of you about before.

**Matthew Panzarino:** But the way that the previous pipelines worked is they did a SERP analysis.

**Matthew Panzarino:** They found the top-ranking articles for that topic.

**Matthew Panzarino:** They looked at the format of those articles, and they tried to duplicate them, basically.

**Matthew Panzarino:** There's a little bit more fundamental weirdness there.

**Matthew Panzarino:** But this new agentic pipeline does not even have that process in it.

**Matthew Panzarino:** Instead, we are creating a separate agentic assignment generator, which will take content and tone input from you.

**Matthew Panzarino:** All

**Matthew Panzarino:** Or structure and tone input from you.

**Matthew Panzarino:** So TBD on that.

**Matthew Panzarino:** That's for another discussion.

**Matthew Panzarino:** But as far as the way that this pipeline works, you can see we give it like a rough prospectus for the kind of article that we want here.

**Matthew Panzarino:** And this is honestly probably more aggressive than it actually needs.

**Matthew Panzarino:** We're only doing this right now because there's no assignment generator, so we're trying to get specific.

**Matthew Panzarino:** And then you can just run that through.

**Matthew Panzarino:** And then, generally speaking, does a pretty damn good job.

**Matthew Panzarino:** I'm pretty happy with the outputs overall.

**Matthew Panzarino:** Our reviews are still showing some tweaks that need to be made, but that's the whole point, right?

**Matthew Panzarino:** You do the job of figuring out what needs to be done, and then you propose tweaks or tweak them yourself, and then we get to a place of deliverable.

**Matthew Panzarino:** So that's kind of how the agentic pipelines are structured and work a little bit differently.

**Matthew Panzarino:** The most important thing, of course, being that they have validators built in.

**Matthew Panzarino:** And the, I will stop talking for questions on this in just a second, promise.

**Matthew Panzarino:** I am now on a monologue warning from Fathom, which I get on every call, because I talk too much.

**Matthew Panzarino:** Okay, so this monograph article editor project in Claude was how we came up with that list of commands.

**Matthew Panzarino:** When we started this project, was, okay, I'm just going to do the normal process of manually editing an article, going through, looking at each of the things that need to be done, and then figuring out what a good article looks like.

**Matthew Panzarino:** That was back in the early days of this project.

**Matthew Panzarino:** Now, later on in the project, we don't need it as much anymore, because we have the agentic pipeline, but now we can just run the commands found in our post-processing sequence, and it'll kind of walk through each one of them.

**Matthew Panzarino:** These post-processing instructions that we built...

**Matthew Panzarino:** Here, you'll notice these are familiar, right?

**Matthew Panzarino:** Because look, here's the MoneyGantt thing that the Agentic Pipeline now does.

**Matthew Panzarino:** Here's the CTA and FAQ thing that the Agentic Pipeline now does.

**Matthew Panzarino:** We didn't know we needed these until we did our editing job and we recorded these steps and we understood, hey, what is it that we wanted to do?

**Matthew Panzarino:** What do we need it to do?

**Matthew Panzarino:** Now, some of you may get lucky and your articles may turn out just fine coming out of the standard Agentic Pipeline.

**Matthew Panzarino:** I doubt it, but you might, right?

**Matthew Panzarino:** So, really what you want to do is look at the client output from the existing pipelines, do your normal work that you would do to edit it.

**Matthew Panzarino:** The only difference is find a way to record that work.

**Matthew Panzarino:** Like, don't lose what you do.

**Matthew Panzarino:** And a cloud project is a great way to kind of collate the work you're doing because you can, in a project, utilize the project's memory to search all of the chats in the project.

**Matthew Panzarino:** This is something you cannot do in any individual.

**Matthew Panzarino:** Visual chat once it reaches limit.

**Matthew Panzarino:** So your memory is lost at that point.

**Matthew Panzarino:** And then you have to like copy the output and then paste it in and say, hey, let's continue working from here.

**Matthew Panzarino:** Annoying, right?

**Matthew Panzarino:** Use the project because you could also ask the project things.

**Matthew Panzarino:** So once you get down the road and you've done a bunch of editing and you've done a bunch of work to figure out where your good is, I can now go and say, hey, what are the instructions I give you about editing?

**Matthew Panzarino:** And then it says, I'm going to go look.

**Matthew Panzarino:** Now, I will be honest with you here.

**Matthew Panzarino:** It's going to look in the project knowledge and find our list of post-processing instructions because we put them in there.

**Matthew Panzarino:** But if it didn't have them, it would search the previous chats and it would say, hey, here's all the things that you've told me to do, right?

**Matthew Panzarino:** You did.

**Matthew Panzarino:** You asked me to do these things, compliance check, money GAN, CTA and FAQ, internal links.

**Matthew Panzarino:** So when you're working in a project, you have a note taker, so to speak, that is watching the way you work.

**Matthew Panzarino:** It's learning from the way you work.

**Matthew Panzarino:** It will execute better on those commands the more you work in that project.

**Matthew Panzarino:** And you are able to query the entire project to do things like build a starter prompt library.

**Matthew Panzarino:** So when I started out, I actually built this in my private and then moved it here.

**Matthew Panzarino:** But when I started out, I was just like line by line editing these articles with Claude until I figured out what semantically was the right prompt to ask it to get the desired result.

**Matthew Panzarino:** And then I was like, cool, copy, paste into my prompt library, right?

**Matthew Panzarino:** And then so on and so forth until I had built up an instruction set.

**Matthew Panzarino:** And the way to do that for you now, if you already are working either in a cloud project or chat GPT chat with a particular client or a custom GPT with a client is go query.

**Matthew Panzarino:** cool.

**Matthew Panzarino:** cool.

**Matthew Panzarino:** 3.

**Matthew Panzarino:** And say, hey, tell me everything that I do, every article, or most of the time.

**Matthew Panzarino:** And it'll say, oh, well, you always tell me to do these things.

**Matthew Panzarino:** Boom, starter prompt library, right?

**Matthew Panzarino:** Now, then refine that, tweak it, don't just believe that, right?

**Matthew Panzarino:** I also, at some point, we need to have a real serious discussion in this group and across the company about people not thinking critically about AI outputs and just running AI outputs and going like, oh, this looks like it's in the proper format.

**Matthew Panzarino:** And then copying it, pasting it in, and then running that as a part of another process.

**Matthew Panzarino:** If you don't think critically at each juncture, you will end up with garbage and you won't know where it came from because you've got three layers of garbage.

**Matthew Panzarino:** So check your prompt libraries, look at them, think about the processes critically, because when we do ingest those into automated processes that you will then process dozens or hundreds of articles on, the force multiplier can be amazing, but the garbage multiplier can also be amazing, right?

**Matthew Panzarino:** So please, please.

**Matthew Panzarino:** Think critically about all of these things as you go.

**Matthew Panzarino:** Yeah, that's what I have to say about that.

**Matthew Panzarino:** Questions about any of that stuff?

**Matthew Panzarino:** No?

**Matthew Panzarino:** None?

**Matthew Panzarino:** Zero?

**Matthew Panzarino:** Zed?

**Matthew Panzarino:** Nobody has any questions.

**Matthew Panzarino:** It's completely crystal clear.

**Jenn Peters:** There's a hand up.

**Iana Medvedeva:** I just have a note.

**Iana Medvedeva:** I'm fighting with our authentic pipeline today in the morning.

**Iana Medvedeva:** think Daniel changed something in a step with verifications.

**Iana Medvedeva:** So right now it's running for 20 minutes, evaluating, rechecking.

**Iana Medvedeva:** So it's very sensitive.

**Iana Medvedeva:** So whatever, how you're phrasing it, it's very sensitive.

**Iana Medvedeva:** And especially in the writing guidelines, in this proofreader checklist, you're kind of...

**Iana Medvedeva:** Prompt library is going to be very sensitive to every word that you put there.

**Iana Medvedeva:** And every wrong word can make it circle back for 20 minutes trying to fix it when it's actually not possible to fix just because it's phrased incorrectly.

**Iana Medvedeva:** So you need to be very careful about how you phrase your requests and your prompts.

**Matthew Panzarino:** Yeah, the 25 minutes thing is a byproduct of two things.

**Matthew Panzarino:** One, yes, like it can get triggered on keywords, but we've switched to a new researcher.

**Matthew Panzarino:** We actually have a three-tiered research system now.

**Matthew Panzarino:** It uses Exa.

**Matthew Panzarino:** Oh my God, I forgot the other two.

**Matthew Panzarino:** They just completely vanished from my brain.

**Matthew Panzarino:** It doesn't matter.

**Matthew Panzarino:** The primary is Exa instead of Prophecy because Exa is actually a lot better.

**Matthew Panzarino:** It's a lot more thorough.

**Matthew Panzarino:** It has a more intense process.

**Matthew Panzarino:** It can also do some weird things, which is one of the reasons the agentic pipelines aren't completely rolled out yet.

**Matthew Panzarino:** So we're working on how to mitigate those.

**Matthew Panzarino:** But it's more thorough than perplexity, which is what we were using previously.

**Matthew Panzarino:** The 25-minute thing is also related to the fact that we, the knowledge-based project, is basically designed to create a knowledge base for clients that will store the research that you do every time you run an article.

**Matthew Panzarino:** So when you run an article, will do research on the topic and store it so that the next time you run an article, it's faster.

**Matthew Panzarino:** So the initial runs on any account or runs when something has been changed or when the knowledge base, you know, has been reset, et cetera, will always take longer.

**Matthew Panzarino:** All of these runs will organically take longer than previous runs.

**Matthew Panzarino:** So running five or ten and then moving on to your next client and doing whatever you're doing with them and then coming back to them should be the norm working with these because they have to run these dollars.

**Matthew Panzarino:** It's naturally going to take longer.

**Matthew Panzarino:** So it's going to go do its process, run its checks, run its validations, and then iterate on that as many times as needed to achieve confidence scoring, unless there's a bug, you know, or an issue like we're seeing right now, or Iana's seeing right now.

**Matthew Panzarino:** But outside of that, it should run those checks and tests.

**Matthew Panzarino:** And I think the average pipeline run is about 10 to 12 minutes once it's like it when it's actually working correctly, so to speak.

**Matthew Panzarino:** But it can, it can run longer.

**Matthew Panzarino:** The validation loop is very tough to get right.

**Matthew Panzarino:** That's why we're still working on them and Daniel's still tweaking.

**Matthew Panzarino:** It's hard, right?

**Matthew Panzarino:** It's a hard thing to do because you have to get adherence and validate.

**Matthew Panzarino:** It's also a reason why your prompt library, if it's like tried and tested, and you have worked out the semantics, and you know this produces a relatively reliable result for you, it's so valuable when we go.

**Matthew Panzarino:** The into making the agentic pipeline, because otherwise it's engineers kind of trying to divine from you waving your hands about what you wanted to do, what the prompt should read.

**Matthew Panzarino:** And our engineers are great, but they're not editors.

**Matthew Panzarino:** They're not writers.

**Matthew Panzarino:** They're not content people.

**Matthew Panzarino:** And some of them are better at it than others.

**Matthew Panzarino:** But I'm just warning you, like Kirkland used to be a journalist.

**Matthew Panzarino:** Great.

**Matthew Panzarino:** You know, he's really good at prompting for article creation, but he's not always the one working on these projects.

**Matthew Panzarino:** And so like there are, there's a variation of skills there, just like there are a variation of skills on the delivery side.

**Matthew Panzarino:** So make sure that you are doing your best to give them really crisp, clear, well-formulated instructions on what you needed to do.

**Matthew Panzarino:** That's your best chance of success.

**Matthew Panzarino:** So that you're not leaving it up to them to decide how to phrase something.

**Matthew Panzarino:** And then you end up with unpredictable results, right?

**Matthew Panzarino:** Any other questions?

**Matthew Panzarino:** questions?

**Matthew Panzarino:** About the Gentic pipelines or process or anything like that.

**Matthew Panzarino:** But as a reminder, I've told a lot of you this, but you can always go look in our Claude instance and see how we are utilizing these tools.

**Matthew Panzarino:** We have separate tools for every job, so don't hesitate to go look and see what we've done.

**Matthew Panzarino:** Generally speaking, you should have one project per task if you are doing multiple tasks for a client.

**Matthew Panzarino:** Do not just have one project for a client.

**Matthew Panzarino:** That's a recipe for mixed contexts and kind of, you know, awkwardness.

**Matthew Panzarino:** So if you're trying to do, for instance, editing articles, scraping comments from client feedback, doing brainstorming, doing a PSEO project, doing keyword research, all in the same project for a client.

**Matthew Panzarino:** Let's go.

**Matthew Panzarino:** It's a mess.

**Matthew Panzarino:** It's just going to, like, lose the plot.

**Matthew Panzarino:** You're going to have bloated context with a ton of different contextual documents, and it may pull from context that you don't want it to pull from at the wrong times.

**Matthew Panzarino:** So make sure that you have very specific projects for each task that you do for a client, and feel free to go in here and look at any of these, and you can always ask Nana or Yana about how we're using these and what the purpose is.

**Matthew Panzarino:** You can log into our pod project by logging into pod-f at growthx.ai, and then Nana or Yana can send you a link, or I can send you a link to the project.

**Iana Medvedeva:** Go ahead, Yana.

**Iana Medvedeva:** You can say it out loud.

**Iana Medvedeva:** Yeah, about prompting, especially when you're preparing for a GNS pipeline.

**Iana Medvedeva:** If something quantifies, quantify it.

**Iana Medvedeva:** If you don't want more than one bullet list per section, write it down, not just write, like, I don't want a lot of bullets.

**Iana Medvedeva:** lists, because when it runs evaluation step, it's still evaluation, and when there is no criteria to evaluate, it may always evaluate in a different way.

**Iana Medvedeva:** This is why our verification rate now stuck, because of a CTA step.

**Iana Medvedeva:** We don't have it exactly written down how it should look like, so every time it analyzes our examples, it seems like every time it comes to different conclusion how it's supposed to look like.

**Iana Medvedeva:** So if it's possible to quantify or explain very precisely how it should look like, it's better to do it, to not get stuck in this endless circle of evaluations, just because model evaluates every time differently.

**Iana Medvedeva:** One time it says, yes, it's good.

**Iana Medvedeva:** Next time it evaluates, it says, no, you know, it's not.

**Iana Medvedeva:** Change it.

**Iana Medvedeva:** And it keeps changing back and forth.

**Matthew Panzarino:** Yeah, yeah, it's a good point.

**Matthew Panzarino:** The validation steps mean that your prompts are.

**Matthew Panzarino:** going to be sort of like read multiple times, right?

**Matthew Panzarino:** So it's important that precision comes into play where you might have been trying to do a catch-all before because you think, oh, I got one shot at this.

**Matthew Panzarino:** You know, think about it in terms of, hey, this is going to be adhered to very, very closely.

**Matthew Panzarino:** So be precise, you know.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Any other questions?

**Matthew Panzarino:** And not just about this.

**Matthew Panzarino:** So any other questions about anything you've got going on, any blockers, anything weird?

**Matthew Panzarino:** And, you know, also, too, as you see things, you know, don't hesitate to call them out.

**Matthew Panzarino:** Like, I know Usman sent me a couple of messages about, like, hey, wouldn't it be great if we had X or Y?

**Matthew Panzarino:** And it turns out we are already working on those things.

**Matthew Panzarino:** They're on a roadmap.

**Matthew Panzarino:** But it could just as easily be something that we, that aren't, that is not on a roadmap.

**Matthew Panzarino:** So never hesitate to call out feature sets or features or things like that that you think might be interesting.

**Matthew Panzarino:** interesting to pursue, especially if you're seeing them.

**Matthew Panzarino:** As a result of like client asks or just to get your job done better.

**Matthew Panzarino:** We're still building the product.

**Matthew Panzarino:** So those are always welcome as well.

**Matthew Panzarino:** They may not be prioritized, you know, over or alongside of the things right away, but it's always helpful to know and you're at the ground level using the product.

**Matthew Panzarino:** So you are product researchers as well as you're doing your job.

**Matthew Panzarino:** So always feel free to reach out and say that stuff.

**Matthew Panzarino:** Um, it's an interesting question.

**Matthew Panzarino:** So in what capacity are you using perplexity for article generation?

**Matthew Panzarino:** Are you talking about for briefs, like creating outlines and briefs?

**Sucheta Biswas:** No.

**Sucheta Biswas:** So actually there are many, you know, industry vertical articles for abnormal.

**Sucheta Biswas:** For example, five ways threat detection can help manufacturing or professional services.

**Sucheta Biswas:** So they kind of have kind of the same template, but to make each one different, and I need.

**Sucheta Biswas:** Like different set of statistics or, you know, deep research, but sometimes perplexity does not give me the, you know, satisfactory results.

**Sucheta Biswas:** So how can I like leverage AI more with that?

**Matthew Panzarino:** Okay, so it could be, it's, that's, it's hard to say because it could be the way you're using perplexity.

**Matthew Panzarino:** You know, I would need to take a look at your, your chats to see what's going on there.

**Matthew Panzarino:** And there may be some skillshare that we can do on how to do good research with perplexity, because it is quite capable.

**Matthew Panzarino:** We're using Exa for some very specific reasons.

**Matthew Panzarino:** I don't know if we have like an accessible version of Exa, like an account or if we just have like API level access.

**Matthew Panzarino:** But let me, let me check on that for you.

**Matthew Panzarino:** And maybe you can try using Exa as well.

**Matthew Panzarino:** But as far as the industry verticals go, are you doing, how many articles are you doing for each vertical?

**Sucheta Biswas:** Oh, like industry or?

**Sucheta Biswas:** Yeah.

**Sucheta Biswas:** It's kind of like five to six or seven at most.

**Sucheta Biswas:** So it's a list of industries, but yeah, like we're just doing a bunch of those.

**Matthew Panzarino:** Yeah, yeah, yeah.

**Matthew Panzarino:** The reason I ask about this is because I filed a ticket yesterday about being able to select artifacts as you file, as you fire off a pipeline, because, and this is a prime example of that.

**Matthew Panzarino:** You really need a body of research that you can go to for, you know, relevant and verified statistics about a particular vertical, but you only need it for the next six articles, right?

**Matthew Panzarino:** And you don't need it for, you don't need to create a whole new pipeline just to run those five.

**Matthew Panzarino:** You could, you know, you could do it, but it's kind of annoying, you know, then you got to manage the pipeline and then eventually just archive the pipeline because you're not using it anymore, right?

**Matthew Panzarino:** Yeah, but it could be a thing where we use our own researcher.

**Matthew Panzarino:** There's no reason that our workflow researcher can't do this task, right?

**Matthew Panzarino:** But the...

**Matthew Panzarino:** The to that researcher is the inputs that we give it and the article directions that we give it.

**Matthew Panzarino:** And I'm thinking in terms of the agentic pipeline, right?

**Matthew Panzarino:** Because I'm really thinking about the future of this.

**Matthew Panzarino:** But the inputs could be that.

**Matthew Panzarino:** And then the artifact that you select could be like a database of research that you've done on a particular industry vertical.

**Matthew Panzarino:** And so you could say, hey, don't use this context for this.

**Matthew Panzarino:** Use this one, right?

**Matthew Panzarino:** And I think that's an interesting application of something like this because you would then run five or six articles based on that research and then switch your database, right?

**Matthew Panzarino:** And then run five or six articles based on a new one.

**Matthew Panzarino:** But as far as the thing that's closer to the ground here for you, yeah, I think it's, you know, perplexity is fairly capable.

**Matthew Panzarino:** So it could be just that we need to do a little bit of work on research.

**Matthew Panzarino:** Have you asked Marisol about how she.

**Sucheta Biswas:** Does research?

**Sucheta Biswas:** No, but I can check that.

**Matthew Panzarino:** Yeah, I would say reach out to and say, hey, you know, I want to do some research with Perplexity, and I'm doing it for these verticals, and I'm not getting enough, I haven't had you articulate it, but is it not enough information density, is it not the right statistics, what is it that you're lacking?

**Sucheta Biswas:** It says that I'm doing it manually, I go to news sources, and Abnormal really likes their statistics to be recent, so I like to do it manually, but if there was a shortcut, or it could save me some time, it would be great.

**Matthew Panzarino:** Well, you you can specify that when you're doing your research, right, you can say return research within the last 12 to 18 months, you have to enable web search on the Perplexity interface, because it will then use the web search to do the research, otherwise it will use stored data, and may pull old statistics.

**Matthew Panzarino:** Exa also is very good at finding recent stuff, so once again, it might be an opportunity to use that if we have access.

**Matthew Panzarino:** I'll ask for that and see, and I'll drop it in the channel if we do.

**Matthew Panzarino:** Sure, that's okay.

**Matthew Panzarino:** Thanks, Max.

**Matthew Panzarino:** Yeah, yeah, of course.

**Matthew Panzarino:** Any other questions or anything?

**Matthew Panzarino:** The last few minutes here?

**Tiandra Burns:** I have a question on the cloud projects.

**Tiandra Burns:** So the goal for the, what is the goal for everyone to have an extensive library in their cloud project?

**Tiandra Burns:** Should we just continue to build that out, even if we're not using it much for other processes per se?

**Matthew Panzarino:** Don't use anything, don't build anything you're not going to use.

**Matthew Panzarino:** Okay, okay.

**Matthew Panzarino:** I'm trying to create, I'm not trying to create busy work for you.

**Matthew Panzarino:** It's just that, like, if you have a need for a task that you do more than once a week, right?

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Or once a month, frankly, then build a project for it.

**Matthew Panzarino:** Like, there's no reason that you should not do that because it's just, it frees up time.

**Matthew Panzarino:** Even if it's something that's...

**Matthew Panzarino:** Easy for you to do.

**Matthew Panzarino:** Why?

**Matthew Panzarino:** You know what mean?

**Matthew Panzarino:** Like that's just takes time away from you being able to do things like step back and think critically about whether a piece is headed in the right direction or whether or not the last five pieces are really driving towards the goal, right?

**Matthew Panzarino:** Of the client is going after.

**Matthew Panzarino:** And I understand you may not have time to do that because you're like, you know, I've got these 12 things to do.

**Matthew Panzarino:** Well, what if those 12 things took two minutes, right?

**Matthew Panzarino:** Like that's the premise.

**Matthew Panzarino:** And it's the idea of building out like an article editor project, I think is the most vital one because it just helps you collate all of the context, prompts, and instructions and process to understand what is missing, what is not in the pipeline now that should be.

**Matthew Panzarino:** Because the fact is you should not be having to spend an hour to an hour and a half on a piece after it comes out of the pipeline.

**Matthew Panzarino:** We do not succeed as a company if you have to do that.

**Matthew Panzarino:** If you have to do it in the near term, which is the reality for many people.

**Matthew Panzarino:** That's because the pipeline's not good enough.

**Matthew Panzarino:** That's why we're creating these authentic pipelines and rolling them out, right?

**Matthew Panzarino:** For some people, that's already very close to reality.

**Matthew Panzarino:** They're like, hey, I put in a really detailed outline, and I get a pretty decent article, and then I edit it for a few minutes, and then the client's happy.

**Matthew Panzarino:** That's great.

**Matthew Panzarino:** That's just not the reality for everyone, right?

**Matthew Panzarino:** And we need to work towards that reality.

**Matthew Panzarino:** But the idea that you would take an article coming out of the pipeline and then bare-knuckle it into shape for a client, and it would take you an hour, hour and a half for each piece, that's wasted labor.

**Matthew Panzarino:** Not in the near term.

**Matthew Panzarino:** It's great that you're there doing the work.

**Matthew Panzarino:** But if you are not recording that information, helping yourself to understand, and then eventually an engineer to understand what it is you're doing that is not getting done by Atlas, like, that is super vital work.

**Matthew Panzarino:** Because it means, hey, you are suffering now to have joy later and build leverage for yourself and for the company.

**Matthew Panzarino:** But it is, but it.

**Matthew Panzarino:** It it's.

**Matthew Panzarino:** It's.

**Matthew Panzarino:** It's, it's.

**Matthew Panzarino:** It's It's fun.

**Matthew Panzarino:** It's.

**Matthew Panzarino:** It's,

**Matthew Panzarino:** It enables you to get the work done faster and more efficiently, and that's what the cloud projects are about.

**Matthew Panzarino:** It's not about, hey, I want you all, your homework is to go create 50 cloud projects.

**Matthew Panzarino:** Those projects were created organically because we felt a need to perform a process.

**Matthew Panzarino:** They were not created because I felt like I needed additional homework.

**Matthew Panzarino:** You know what mean?

**Matthew Panzarino:** It's like a, it's a pressure release valve that you can use to fill a gap.

**Matthew Panzarino:** And it serves a double purpose of articulating very clearly what is missing from the pipeline so that when we do build the agentic pipeline out for your client, it has the right prompts, it has the right instructions, it has the right context, and it can deliver really great, high-quality work out of the pipeline.

**Matthew Panzarino:** Did I answer your question?

**Matthew Panzarino:** Did that make sense?

**Matthew Panzarino:** Or was I answering a different question than you were actually asking?

**Matthew Panzarino:** How about the current Was answering saying?

**Matthew Panzarino:** into results.

**Matthew Panzarino:** Thank

**Matthew Panzarino:** Silence is golden.

**Matthew Panzarino:** Silence is acquiescence.

**Matthew Panzarino:** Oh, I always forget to look at the chat.

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** No, it's okay.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** I always forget the people who are talking in the chat.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Any more questions?

**Matthew Panzarino:** Anything about anything?

**Matthew Panzarino:** Sweet.

**Matthew Panzarino:** Thanks, folks.

**Matthew Panzarino:** Appreciate it.

**Matthew Panzarino:** Have a good day.

**Matthew Panzarino:** Ciao, ciao.

**Patrícia Contreiras:** Bye, everyone.
