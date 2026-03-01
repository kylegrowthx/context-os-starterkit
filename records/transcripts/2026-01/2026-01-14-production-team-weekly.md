# Production Team Weekly

<metadata>
date: 2026-01-14
time: 15:59 UTC
duration: 35 minutes
organizer: jenn@growthxlabs.com
participants: Matthew Panzarino, Carrie Chowske, Mariana Marins, Nathan Navidzadeh, Marcus Derencius, Felix Morgan, Jenn Peters
speakers: Matthew Panzarino (product), Carrie Chowske (production), Mariana Marins (ops), Nathan Navidzadeh (production), Marcus Derencius (engineering), Felix Morgan (production), Jenn Peters (organizer)
fathom_recording_id: 114210810
fathom_url: https://fathom.video/calls/530900332
share_url: https://fathom.video/share/DzTQzzsezxPZVBs9g5AN2UmRHLvabi_3
source: fathom
enriched_on: 2026-02-28 16:45 UTC
</metadata>

---

## Summary

Matthew Panzarino led a production team synchronization to introduce three major initiatives: mandatory Time Doctor tracking for post-pipeline editing work, a new standardized Atlas pipeline for scraping Google Doc comments, and reinforcement of artifact conflict checking protocols. The meeting addressed workflow standardization challenges created by 200+ ad-hoc processes across production teams and focused on gathering empirical data to guide engineering resource allocation.

---

## Context

This meeting represents a shift toward measurement-driven process improvement within GrowthX's production operations. The Atlas pipeline system, which generates initial content from research and structure, requires consistent human editing before client delivery. Without empirical data on editing time, the team has been unable to prioritize engineering improvements effectively. Matthew acknowledged that team members have agency and are solving problems independently, but this has created fragmentation—over 200 different methods exist for scraping client feedback from Google Docs alone. The initiatives announced in this meeting are designed to standardize workflows while gathering data that will inform engineering decisions about where to invest resources. The framing emphasizes that slow times indicate process problems, not performance issues, and that honest reporting is critical for Atlas to improve.

---

## Relevance

This meeting is critical for all production team members who edit Atlas-generated content and interact with the post-pipeline workflow. It directly impacts how time is tracked, how client feedback is processed, and how pipeline quality is maintained. The mandatory nature of Time Doctor tracking and artifact conflict checks means compliance is expected. This is particularly relevant to Matthew Panzarino's team (product/engineering oversight), Mariana Marins and the ops team (workflow standardization), and all production editors (Carrie Chowske, Nathan Navidzadeh, Felix Morgan) who will implement these changes immediately.

---

## Overview

- **Mandatory Time Tracking:** Use Time Doctor to track post-pipeline editing time (from Atlas output to client-ready). This data will identify pipeline bottlenecks and guide engineering resource allocation. Setup is simple; tool runs in manual Pomodoro timer mode with no screenshots, video, or keylogging.
- **New Google Doc Comment Pipeline:** A new Atlas pipeline automates scraping client feedback from Google Docs, replacing 200+ non-standard processes and standardizing a common workflow. Self-service setup via YAML copy or support ticket.
- **Prioritize Artifact Conflict Checks:** Review the artifact conflict guide to ensure clean, efficient pipeline outputs. Unresolved conflicts create "weird tangles of logic trees" that degrade both performance and output quality, often in unexpected ways.
- **File Detailed Tickets:** When reporting issues, include specific Atlas URLs and pipeline logs to accelerate diagnosis and resolution by the growing client ops engineering team.

---

## Key Topics

### Time Doctor Implementation

- **Goal:** Gather empirical data on post-pipeline editing time to identify bottlenecks and prioritize engineering resources.
- **Scope:** Time tracked is the window from Atlas output to client-ready state. This excludes publishing tasks (e.g., Webflow checks), which are a separate process.
- **Tool:** Time Doctor, used in manual Pomodoro mode.
    - **Privacy:** No screenshots, video, or keylogging.
    - **Data Collected:** Time spent and apps used during active timers.
- **Workflow:**
    1. Run Atlas generations.
    2. Start a Time Doctor timer for each piece of content.
    3. Edit content to a client-ready state.
    4. Stop the timer.
- **Setup:**
    - Download and install Time Doctor.
    - Use a simple Atlas pipeline to populate deliverables with actual article titles, replacing generic placeholders.
- **PSEO/Batch Content:** Track as a single block of time for the entire batch.
- **Rationale:** Honest data is critical. High times are an opportunity for engineering help, not a performance metric. Hiding issues prevents Atlas from improving. Time tracking enables resource deployment decisions: short times (e.g., 15 minutes) receive lower priority; extended times (e.g., 2.5 hours) trigger engineering investigation into pipeline performance.

### New Google Doc Comment Pipeline

- **Problem:** Over 200 non-standard processes exist for scraping client feedback from Google Docs—ad-hoc implementations across the team creating fragmentation and inefficiency.
- **Solution:** A new Atlas pipeline automates this task, standardizing the workflow and reducing manual work.
- **Setup:**
    - **Self-Service:** Copy the pipeline YAML into your workspace (requires familiarity with pipeline creation).
    - **Support:** File a ticket if unfamiliar with pipeline setup.
- **Context:** This is an interim solution. The long-term goal is for clients to comment directly within Atlas's Content OS, which will make this pipeline obsolete.

### Workflow Standardization & Best Practices

- **Goal:** Move all external processes ("hacks") into standardized Atlas workflows.
- **Method:**
    - **Self-Service:** Implement post-processing steps directly in Atlas artifacts (e.g., proofreader checklists, assignment directions).
    - **Support:** File detailed tickets for complex tasks that require engineering help to migrate into Atlas.
- **Artifact Conflict Checks:**
    - **Action:** Review the detailed artifact conflict guide compiled by Nana.
    - **Why:** Unresolved conflicts create "weird tangles of logic trees" that degrade pipeline performance and output quality. These issues often appear unrelated to the underlying conflict, making diagnosis difficult.
    - **Impact:** Clearing conflicts can produce unexpected efficiency gains for teams who don't initially think they have this problem.

---

## Action Items

**Matthew Panzarino** (Product Lead)
- Review comments pipeline YAML; decide rollout strategy (self-serve vs ticket)

**Jenn Peters** (Organizer/GrowthX Team)
- Review artifact conflict checks guide; implement checks in workflows

**Mariana Marins** (Ops/Workflow)
- Review artifact conflict checks guide; implement checks in workflows

**Marcus Derencius** (Engineering)
- Review artifact conflict checks guide; implement checks in workflows

**Felix Morgan** (Production)
- Review artifact conflict checks guide; implement checks in workflows

**Nathan Navidzadeh** (Production)
- Review artifact conflict checks guide; implement checks in workflows
- Review comments pipeline docs; ask Marcus clarifying questions about implementation

**Carrie Chowske** (Production)
- Review artifact conflict checks guide; implement checks in workflows

**All Team Members**
- Install Time Doctor and begin tracking post-pipeline editing time immediately
- Use new Google Doc comment pipeline (self-service or via ticket for support)
- Include specific Atlas URLs and pipeline logs when reporting issues

---

## Transcript

**Matthew Panzarino:** Good morning, folks.

**Matthew Panzarino:** How's everyone doing today?

**Matthew Panzarino:** Good.

**Jenn Peters:** How are you?

**Matthew Panzarino:** Lovely January 14th.

**Matthew Panzarino:** Oh, man.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Let's give me a couple things in order here.

**Matthew Panzarino:** I am a little out of the weather, so if I sound a little froggy, that is what it is.

**Matthew Panzarino:** It's the typical January malaise when you have kids.

**Matthew Panzarino:** And when you don't, too.

**Matthew Panzarino:** It's just going around right now, it seems.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** So, handful of things.

**Matthew Panzarino:** I want to talk through a few new things and some new workflows and then kind of a larger topic.

**Matthew Panzarino:** So, one, there is a new pipeline, this will be in the agenda, available.

**Matthew Panzarino:** Nana kind of worked on it a little bit and developed this with Marcus based on a project that we had been using in Claude to scrape comments from articles, from docs.

**Matthew Panzarino:** Basically, you know, we all get client feedback in Google Docs and other forms, but Google Docs is a lot, is very common across all of the clients.

**Matthew Panzarino:** And we needed a way to grab those comments and the context in order to be able to parse them and understand whether or not they are applicable to artifacts or other pipeline inputs.

**Matthew Panzarino:** So, this pipeline will be available.

**Matthew Panzarino:** You can grab it, put it in your workspace, and then use it to parse comments from clients.

**Matthew Panzarino:** It's just tooling that now will exist in Atlas that many of us were doing ad hoc in various ways.

**Matthew Panzarino:** We're going to work on doing this for a lot of common tools and common processes so that we don't end up all having non-standard ways of doing this.

**Matthew Panzarino:** That's what we'll try to kind of work on generating best practices around this stuff.

**Matthew Panzarino:** We have collated all of the various, let's call them, you know, hacks or processes or just off-the-books things that you folks are doing.

**Matthew Panzarino:** And there's over 200 different ways that people are accomplishing these things.

**Matthew Panzarino:** And, you know, knowing Nana pulled together that list, I was not shocked, but at the same time, a little bit appalled.

**Matthew Panzarino:** Not that you're doing it.

**Matthew Panzarino:** That's great.

**Matthew Panzarino:** I'm happy about the agency and that everybody's just getting the job done.

**Matthew Panzarino:** But it's clearly an opportunity for us to clear up some lanes, to combine the different ways that people are doing things, to come to a best practice, and to move that stuff into Atlas and out of Claude and out of, you know, various processes that, for whatever reason, are probably less efficient than they should be.

**Matthew Panzarino:** Even though you're getting the job done, it's unlikely that it's probably the best or fastest way to do it.

**Matthew Panzarino:** So we'll help you kind of clean that up over time.

**Matthew Panzarino:** So anyhow, this is a great first kind of tranche of this.

**Matthew Panzarino:** We have to add this pipeline to Workspaces, and it must be configured a little bit.

**Matthew Panzarino:** So it would most likely be a ticket.

**Matthew Panzarino:** I have to kind of wrap my head around exactly how to add it, but I would guess a ticket where if you are already ready on how to create pipelines, you should be able to create it.

**Matthew Panzarino:** Nana, how would you characterize setting it up?

**Mariana Marins:** I didn't set up that one.

**Mariana Marins:** Actually, it was Martha, so I haven't looked at the YAML yet, but I believe it will pull each account's artifacts, so there should be some personalization happening in the YAML.

**Matthew Panzarino:** Yeah, okay, so it may have to be a ticket file that we can roll out.

**Matthew Panzarino:** I'll take a look at it a little deeper.

**Matthew Panzarino:** I hadn't had a chance to analyze what's actually being pulled, but it looks like, yeah, just for a quick scan, looks like it might not be that complex to roll out.

**Matthew Panzarino:** Marcus, are you here?

**Marcus Derencius:** I'm so sorry.

**Marcus Derencius:** I could have just asked you.

**Marcus Derencius:** Are you around?

**Marcus Derencius:** Oh, yeah.

**Matthew Panzarino:** How would you characterize rolling this out, Marcus?

**Marcus Derencius:** I'm sorry?

**Matthew Panzarino:** I would just say, like, for that comment pipeline that we have, that Felix is already testing, that you built for Nana, like, how would you characterize that if somebody else wanted to utilize that pipeline in their workspace?

**Matthew Panzarino:** How hard is it to set up for a new workspace?

**Marcus Derencius:** Oh, the one I made for Biologica?

**Mariana Marins:** Yes.

**Mariana Marins:** Yeah, the comments one.

**Marcus Derencius:** Okay, the comments one, the...

**Mariana Marins:** Yeah, there are two comments.

**Mariana Marins:** Yeah, the comments one that we give the article, like, we give the docx file, and then it does...

**Marcus Derencius:** Yeah, it is generic, so it is easy to set up for anyone, so it's...

**Matthew Panzarino:** Okay.

**Marcus Derencius:** Yeah, yeah, it is.

**Marcus Derencius:** Cool.

**Marcus Derencius:** It is simple, so, yeah.

**Matthew Panzarino:** Great.

**Matthew Panzarino:** So if you've set up a pipeline for yourself before, we can, you can look at the pipeline, it will be in the agenda, it'll be linked, and then you can copy and paste that into your workspace, and then you should have a comments pipeline.

**Matthew Panzarino:** If you are unfamiliar with that or uncomfortable with that, just file a ticket for it, and then we will triage that.

**Matthew Panzarino:** Um, okay, uh, artifact conflicts checks, um, we've kind of just, you know, they're, they're, we've definitely talked about this a lot, um, but there is a pretty detailed document that Nana put together on artifact conflict checks, I want you to check that over, and make sure you've actually done those things.

**Matthew Panzarino:** We've talked about various ways to do it and emphasize the importance here, um, kind of, uh, a handful of times, but I just want to kind of reemphasize that it is vital, uh, because it will save you time.

**Matthew Panzarino:** It has direct impact on how efficient the pipelines are in generating things, but also direct impact on how sloppy they are and how clean their output can be, because even if it is able to accomplish the task, it may not be accomplishing the task the best way it knows how, because it is trying to reconcile conflicts.

**Matthew Panzarino:** So please check that over.

**Matthew Panzarino:** I don't want to be over the head with that.

**Matthew Panzarino:** It is very important, and I can't stress enough how many performance wins I have seen there for people that could clear the decks for you in ways that are unexpected.

**Matthew Panzarino:** Like, you may think, oh, actually, I don't think that's my problem at all, but it actually may be your problem.

**Matthew Panzarino:** Like, I just want to make sure you understand that, that it's an easy way to attempt to get a nice win for yourself on efficiency, because it can create these weird tangles of logic trees and issues that don't seem related to conflict.

**Matthew Panzarino:** Between the artifacts or instructions, but in fact are.

**Matthew Panzarino:** So once again, please check that, check that guide.

**Matthew Panzarino:** But I wanted to get kind of around to the most important thing, and that is we are going to be instituting some time tracking for the edits.

**Matthew Panzarino:** And the time tracking is very specifically about the amount of time it takes you to edit something once it exits the pipeline.

**Matthew Panzarino:** To the moment that you are ready for client delivery.

**Matthew Panzarino:** That's the window.

**Matthew Panzarino:** That's what we're measuring.

**Matthew Panzarino:** We're going to be using a piece of software called Time Doctor.

**Matthew Panzarino:** We're going to be using it in basically manual Pomodoro timer style mode.

**Matthew Panzarino:** So it is not an overall tracker.

**Matthew Panzarino:** It's not going track everything you do on your machine.

**Matthew Panzarino:** It's not going to take any screenshots.

**Matthew Panzarino:** It's not going to take any video.

**Matthew Panzarino:** It's not going to take any key logging.

**Matthew Panzarino:** We basically paired it down to the bare minimum, which is you manually start a timer when you start editing your content.

**Matthew Panzarino:** For the week, for that, for your client, so let's say you run five articles, and you're going to edit those five articles to a state of good, you're going to start a timer when you start doing that work, and you're going to end a timer when you finish doing that work.

**Matthew Panzarino:** The way that it will work is that you will have a project that's populated with all of the deliverables for your account.

**Matthew Panzarino:** We've already put all of those deliverables into the system, so as an example, if you are running Biologica, Felix has tested this for us.

**Matthew Panzarino:** Thank you, Felix.

**Matthew Panzarino:** So if you're running Biologica, and they expect five articles or six articles per week, you will have those six articles as generic items in your project when you click on Time Doctor, and each of those are generic to start.

**Matthew Panzarino:** But then we also built a really cool Atlas pipeline that basically says, hey, just give me your five article titles for the week, and then it updates those in Time Doctor for you.

**Matthew Panzarino:** So it'll be about a one and a half minute process for you to actually click Play on a pipeline in Atlas that will then populate the actual article name.

**Matthew Panzarino:** So instead of like article one, article two, article three, you actually have the article names in there for you or the content names in there.

**Matthew Panzarino:** And the reason for that is, of course, for ease of tracking later on, we're like, you know, why did this article take so long?

**Matthew Panzarino:** What article was this?

**Matthew Panzarino:** Well, article three is hard to remember for anybody, right?

**Matthew Panzarino:** So it'd be like, oh, okay, it's specifically this article, you know, the effects of perimenopause or saffron perimenopausal heat flash.

**Matthew Panzarino:** Or whatever, and you will be able to look at that article and see what that actual title is.

**Matthew Panzarino:** We have a full guide on this, obviously, all written out, so you don't have to remember all of this.

**Matthew Panzarino:** But the long and short of it is you'll download Time Doctor, you'll install it.

**Matthew Panzarino:** It will not record anything.

**Matthew Panzarino:** 98% of the time, if it's on your machine, it'll only record when you actually hit, I'm ready to start editing my articles.

**Matthew Panzarino:** So the process will be, you will run your generations.

**Matthew Panzarino:** If you want to run one at a time, if want to run all at a time, however your process is, you don't want to change that.

**Matthew Panzarino:** But the moment you start editing any piece of content, you're going to start the timer on that piece of content.

**Matthew Panzarino:** You're going to edit that piece of content to good, and then you're going to stop the timer.

**Matthew Panzarino:** If this requires some reorganization of your editing process where you need to, like, cluster it or, you know, get a focus time on it, do so, right?

**Matthew Panzarino:** Because we need to understand exactly how long it's going to take from beginning to end.

**Matthew Panzarino:** By beginning, I mean exiting the Atlas pipeline to client delivery.

**Matthew Panzarino:** And we need to understand it not in an ad hoc kind of way where, you know, I've all asked you, but we need to understand it empirically, right?

**Matthew Panzarino:** We need to know exactly what that is because then the plus side, what do I get out of it, is we can deploy engineering resources.

**Matthew Panzarino:** We can deploy, you know, client ops resources, can deploy human resources to you.

**Matthew Panzarino:** So to help you improve that time.

**Matthew Panzarino:** So if we're like, oh, wow, like you're at 15 minutes, cool, sorry, I love you, but we're going to move you low on the priority list.

**Matthew Panzarino:** If somebody else is at two and a half hours, we're going to say, okay, you know, let's get the engineers on this.

**Matthew Panzarino:** Let's figure out what's going on with the pipeline, why it's taking so long to get this done.

**Matthew Panzarino:** And this is not about like, you know, oh, who's slow?

**Matthew Panzarino:** It's whose processes are slow.

**Matthew Panzarino:** You know, what pipelines are not adherent?

**Matthew Panzarino:** What pipelines are not performing to spec?

**Matthew Panzarino:** And this is going to tell us a lot about what, you know, what Atlas pipelines are actually delivering stuff close to client ready, where they're bottlenecks in the workflow, improve and optimizing the pipelines, where's the low-hanging fruit, where are the biggest issues?

**Matthew Panzarino:** And that's basically will drive all of our decisions on how to deploy engineering resources.

**Matthew Panzarino:** Because right now, you know, I've definitely told plenty of you, like, oh, file a ticket for this, or, or you should tap so-and-so on the shoulder for that.

**Matthew Panzarino:** Or deployed Nana, or Hassan, or myself, or someone else to help you, or a peer review.

**Matthew Panzarino:** There's just no way for us to understand where the fires are without tracking this time.

**Matthew Panzarino:** So the brass tacks of it is, it's manual tracking.

**Matthew Panzarino:** So you have to start and stop the timer.

**Matthew Panzarino:** I know people will forget, but you can adjust the timing.

**Matthew Panzarino:** But you've got to do it, right?

**Matthew Panzarino:** It's mandatory.

**Matthew Panzarino:** We have to know.

**Matthew Panzarino:** Right now, we have no visibility.

**Matthew Panzarino:** This is a black box for us that I have to, like, collect when my personal calls with you, or somebody has to just raise it up at a channel.

**Matthew Panzarino:** Oh, it's taking me X long, right?

**Matthew Panzarino:** We need to know, right?

**Matthew Panzarino:** Because this will allow us to effectively deploy these resources.

**Matthew Panzarino:** This setup, I have done it myself.

**Matthew Panzarino:** It's very simple.

**Matthew Panzarino:** It's pretty straightforward.

**Matthew Panzarino:** The timer, when you start it, when you start the timer, it will record the apps that you're using to do it.

**Matthew Panzarino:** It will record the amount of time it takes to do it.

**Matthew Panzarino:** That's basically it.

**Matthew Panzarino:** It's not going to take screenshots, even during the timer.

**Matthew Panzarino:** It does not take screenshots.

**Matthew Panzarino:** It does not take video recordings, and it does not keylog.

**Matthew Panzarino:** I just want to emphasize that to everybody, just from a privacy perspective.

**Matthew Panzarino:** It's not about that.

**Matthew Panzarino:** It's just about, like, hey, how long did it take you?

**Matthew Panzarino:** Oh, okay, cool.

**Matthew Panzarino:** It took you two and half hours.

**Matthew Panzarino:** You used Claude.

**Matthew Panzarino:** You used Atlas.

**Matthew Panzarino:** You used Google Docs.

**Matthew Panzarino:** It makes sense, right?

**Matthew Panzarino:** Like, used Safari to do some searching because you're trying to verify links, yada, yada.

**Matthew Panzarino:** That's what we kind of want to know.

**Matthew Panzarino:** It's like, hey, okay, cool.

**Matthew Panzarino:** Like, this is two and half hours.

**Matthew Panzarino:** You spent so much of it in Atlas using SGI.

**Matthew Panzarino:** Spent so much of it in Google Docs, and then that's it, right?

**Matthew Panzarino:** So, like, we have to kind of understand that basically we want to be honest with ourselves.

**Matthew Panzarino:** How good is Atlas, right?

**Matthew Panzarino:** Like, how good is it at these jobs, at these tasks we've given you?

**Matthew Panzarino:** How much better can it be?

**Matthew Panzarino:** And where can we deploy the resources to make it better?

**Matthew Panzarino:** And this is what we find to be the least intrusive way to gather that empirical evidence.

**Matthew Panzarino:** They're just like, hey, we need to, like, start...

**Matthew Panzarino:** You manually start and stop even the timer.

**Matthew Panzarino:** We have definitely come up with a handful of questions about this and tried to answer those in an FAQ, but I'm sure there will be more, and I'm happy to answer some after I finish my rant, but we will address those as we come up across it, because there's definitely been some process questions, and the answer is your process may have to adapt a little bit to this, right?

**Matthew Panzarino:** You may have to just set aside a block if you don't block now.

**Matthew Panzarino:** If you do processes in parallel, start them in parallel, right?

**Matthew Panzarino:** If you edit all your articles at once, fire them all off, and then start editing and doing all that.

**Matthew Panzarino:** That's cool.

**Matthew Panzarino:** I get it, right?

**Matthew Panzarino:** Like, because we can treat that as a block.

**Matthew Panzarino:** And sometimes it's like, okay, am I supposed to keep this running if, like, Claude is working?

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** Like, you know, you're still in edit mode.

**Matthew Panzarino:** It's basically that gap that we're measuring between the time Atlas says, hey, here's something I think is good, and you're like, no, no, no, this is actually good, you know, for the client.

**Matthew Panzarino:** So that's what we want to measure.

**Matthew Panzarino:** Yes, you can pause it, Patricia.

**Matthew Panzarino:** You can pause it.

**Matthew Panzarino:** If you're away, if you just step away for a second, you can pause the timer, right?

**Matthew Panzarino:** So the idea is you just only manually start and stop when you are truly working on something and truly finished with something, right?

**Matthew Panzarino:** That's basically it.

**Carrie Chowske:** So like, if I'm waiting for Claude to finish, do I keep the timer running?

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** Yes.

**Carrie Chowske:** That helps.

**Matthew Panzarino:** Because you're still in that editing window, right?

**Matthew Panzarino:** You're still trying to get from Atlas output to client-ready.

**Matthew Panzarino:** Claude is part of that process for you.

**Matthew Panzarino:** So yes, keep it running.

**Matthew Panzarino:** Absolutely.

**Carrie Chowske:** Yeah, that makes sense.

**Nathan Navidzadeh:** What's happening with the optional edits?

**Nathan Navidzadeh:** Is the time track going to be required?

**Matthew Panzarino:** Yeah, it's mandatory for everyone, right?

**Matthew Panzarino:** So that goes back to the visibility issue, right?

**Matthew Panzarino:** Like, we don't have a way to understand where the problems are unless we can see the data.

**Matthew Panzarino:** So yeah, it's mandatory.

**Matthew Panzarino:** I get that people will forget sometimes, and you can go back and adjust, but it's mandatory.

**Nathan Navidzadeh:** Got it.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** So there's going to be an onboarding guide, a full guide on how to set it up, how it works, frequently asked questions, all that stuff.

**Matthew Panzarino:** We have a dedicated Slack channel for Time Doctor questions and issues.

**Matthew Panzarino:** So if you have a question, just bring it to that channel, and we will address it there.

**Matthew Panzarino:** I will be assigning someone from the team to be a point person on Time Doctor, and they will help you manage any questions that come up or any process questions, right?

**Matthew Panzarino:** And there's going to be some manual adjustments that need to happen, potentially, because I know that, you know, some of these processes are going to be a little weird at first.

**Matthew Panzarino:** Matthew, we talked about this, and I'm going to have you finalize the process for requesting a manual edit in Time Doctor.

**Matthew Panzarino:** So the way that you can go back and say, hey, I need to adjust the time on this timer, or I need to modify this entry in Time Doctor, that's going to be managed through a process.

**Matthew Panzarino:** And Matthew will finalize that process.

**Carrie Chowske:** So like I have to be online to be able to edit the time in Time Doctor?

**Matthew Panzarino:** That's a good question.

**Matthew Panzarino:** I think what Matthew is going to figure out is how to manage those adjustments in a coordinated way, right?

**Matthew Panzarino:** So you'll file a request, and then Matthew can make the adjustment for you.

**Matthew Panzarino:** I think that's actually the setup, right?

**Matthew Panzarino:** I'm not 100% sure, but I think that's what we're envisioning.

**Carrie Chowske:** Great.

**Matthew Panzarino:** So that's the Time Doctor stuff.

**Matthew Panzarino:** I guess we will be rolling this out, I don't know if we have a specific date yet, but the goal is to start getting people onboarded ASAP, hopefully within the next few weeks.

**Matthew Panzarino:** If anyone has concerns about this or questions, obviously bring them up now or in the dedicated Slack channel.

**Matthew Panzarino:** And we will address those as we go.

**Nathan Navidzadeh:** Is there a guide to the artifact conflict checks?

**Matthew Panzarino:** Yes, Nana has a detailed document on artifact conflict checks.

**Nathan Navidzadeh:** Can I get a link to that?

**Matthew Panzarino:** I will make sure that is in the agenda, and I will post it in the production Slack channel as well.

**Matthew Panzarino:** Everyone should review that document.

**Mariana Marins:** It's in our workspace.

**Mariana Marins:** Everyone can access it there.

**Matthew Panzarino:** Great.

**Matthew Panzarino:** Yes, so it's available in the workspace.

**Nathan Navidzadeh:** Perfect.

**Carrie Chowske:** So when we're checking for artifact conflicts, are we doing this before or after we edit the content?

**Matthew Panzarino:** It's a good question.

**Matthew Panzarino:** Ideally, you'd check for conflicts as you're setting up your pipelines.

**Matthew Panzarino:** This is something that should be done proactively, not reactively.

**Matthew Panzarino:** But if you identify conflicts while you're editing, absolutely fix them.

**Matthew Panzarino:** This is an ongoing practice.

**Matthew Panzarino:** I would strongly recommend building this into your workflow from the start.

**Felix Morgan:** I had a question about the comments pipeline.

**Felix Morgan:** Can I test it on a small batch before rolling it out to my whole project?

**Matthew Panzarino:** That's a smart approach.

**Matthew Panzarino:** Yeah, Marcus and I can help you set that up.

**Matthew Panzarino:** We can do a trial run, and then once you're confident in it, you can expand it.

**Marcus Derencius:** Yeah, absolutely.

**Marcus Derencius:** Happy to help with that, Felix.

**Felix Morgan:** Great, thanks.

**Matthew Panzarino:** Alright, I think that's the key stuff for today.

**Matthew Panzarino:** Again, review the artifact conflict guide, install Time Doctor, and start using the comments pipeline if you work with Google Doc feedback.

**Matthew Panzarino:** Questions?

**Mariana Marins:** This is awesome.

**Mariana Marins:** I think the comments pipeline will save us a lot of time.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** That's the whole idea, right?

**Matthew Panzarino:** We standardize these processes and then we can actually measure and improve them.

**Matthew Panzarino:** Thanks everyone.

---

## Related Documents

- [Artifact Conflict Checks Guide](link_to_guide) - Detailed guide by Nana on identifying and resolving conflicts
- Time Doctor Setup Guide - Onboarding documentation (available in team Slack)
- Google Doc Comments Pipeline YAML - Available in workspace
- FAQ: Time Doctor Implementation - Common questions and answers
