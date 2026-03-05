# Daniel + Kirkland

<metadata>
date: 2025-03-24
time: 18:01 UTC
duration: 29 minutes
organizer: Daniel Lopes
participants: Daniel Lopes, Kirkland Gee
fathom_recording_id: 53481901
fathom_url: https://fathom.video/calls/260334539
share_url: https://fathom.video/share/UvAJPqRg6cyVLP1GxfCymsWRXMZPKtG9
source: fathom
enriched_on: 2026-03-04 14:32 UTC
</metadata>

---

## Summary

Daniel Lopes onboarded new engineer Kirkland Gee on his first day, walking through GrowthX's tech stack, development workflows, and project structure. Key focus areas included Circle (internal LMS), GitHub repositories (Flow and Flow Studio codebases), Intemporo (distributed runtime), and upcoming product initiatives like Atlas (a custom replacement for AirOps/Notion). Daniel emphasized that Kirkland should spend the first week absorbing context—watching client calls, exploring tools, and studying Chapter 5 on prompting engineering—before contributing code or productizing workflows.

---

## Context

Kirkland Gee is a new engineer joining GrowthX with prior experience in SEO and running agencies. Daniel Lopes, who leads engineering, is onboarding him on day one. The company operates in two main domains: GrowthX Services (B2B content marketing) and CheckThat (AI visibility software). Kirkland's role involves building and improving workflows, collaborating with Daniel on API development, and eventually productizing internal tools for broader use. This is an internal team alignment meeting to ensure Kirkland has access to all systems and understands the engineering stack before contributing.

---

## Relevance

- **To GrowthX Delivery:** New engineer focused on improving client-facing workflows (AirOps migrations, API clients, 404 removal, Kappa.ai integration for fact-checking). Daniel expects Kirkland will use agency and SEO background to identify efficiency improvements and help productize workflows into micro-apps.

- **To Engineering Infrastructure:** Kirkland gaining proficiency with Flow (workflow codebase), Flow Studio (React/Rails IDE), Intemporo (runtime), and GitHub-based development. Plan to set up local environment tomorrow and start collaborative workflow development sessions mid-week.

- **To Product Development:** Atlas project identified as critical—custom replacement for AirOps and Notion in pilot phase. Daniel will show working prototypes by end of week. Kirkland's input on UX and operations workflows valuable for GTM-focused product design.

---

## Overview

- Kirkland's first week: absorb context by watching client calls, exploring internal tools, studying Circle LMS courses, and reading Chapter 5 on prompting engineering
- Tech stack: Circle (learning platform), GitHub (Flow and Flow Studio repos), Intemporo (distributed runtime), Flow Studio (React/Rails IDE), AirTable (client strategy/assignments)
- Core projects: Flow (API-based workflow framework), Flow Studio (IDE for workflow visualization), Atlas (replacement for AirOps/Notion in GTM), and micro-apps/productized workflows
- Workflow examples: SEO content creation (3 minutes), article-to-illustration workflow, Kappa.ai integration for fact-checking generated code

---

## Key Topics

### Onboarding Progress and Access

  - Kirkland received access to Slack, Notion, Fathom, OnePass, Google account
  - Still needed access to Circle and AirTable (Daniel provided during meeting)
  - Basecamp projects access to be confirmed

### Key Learning Resources

  - Circle LMS: Contains courses on workflow creation and client management
  - Recommended book: Chapter 5 on prompting engineering crucial for team
  - GitHub repos: 'flow' (workflows) and 'flow-studio' (IDE) are primary codebases
  - Basecamp: Used for task management and project planning

### Workflow System Overview

  - Workflows built on Intemporo (distributed systems runtime)
  - Each workflow is a self-contained folder with steps, functions, and prompts
  - Execution viewable through Intemporo UI or custom Flow Studio interface
  - Example workflow: SEO content creation (3-minute process, multiple steps)

### Current Projects and Future Plans

  - Ongoing: Improving existing workflows, creating new API clients
  - Upcoming: Developing micro-apps and productizing workflows
  - Atlas: Project to replace AirOps and Notion with custom solution
  - Potential AI-driven email project in early planning stages

### Role Expectations for Kirkland

  - Initial focus on learning and absorbing context (1-2 weeks)
  - Future: Collaborating with Daniel on workflow creation and optimization
  - Leveraging SEO and agency experience for efficiency improvements
  - Logging ideas for small and large projects in Basecamp

---

## Action Items

- **Kirkland Gee (GrowthX)**: Explore internal tools (Circle, Basecamp, GitHub), watch client calls, review Notion documentation, and dive into client interactions to absorb context
- **Kirkland Gee (GrowthX)** and **Daniel Lopes (GrowthX)**: Set up local development environment tomorrow morning (30-60 minutes with Daniel)
- **Daniel Lopes (GrowthX)**: Show working prototypes of Atlas replacement project by end of week
- **Kirkland Gee (GrowthX)**: Study Chapter 5 on prompting engineering from the recommended AI engineering book (high priority)
- **Kirkland Gee (GrowthX)**: Log ideas for small and large workflow projects in Basecamp folders
- **Daniel Lopes (GrowthX)**: Follow up with people team to clarify onboarding document source

---

## Transcript

**Daniel Lopes:** How's day one so far?

**Kirkland Gee:** Just a lot of reading and watching, which is to be expected. But yeah, going really well. I can get myself immersed in all of the stuff. I'm one of those people who gets into things deeply. I was reading all the Notion docs in the evenings last week because I'm like that. I spent most of today watching the workshop that you guys did—I think it was six hours—maybe with clients or something back in November. It was really helpful just to see how you guys talk about all the animations and stuff in AirOps.

**Daniel Lopes:** Nice. Yeah, cool. What about the Basecamp stuff? Do you want to share your screen and talk through anything?

**Kirkland Gee:** I've never used Basecamp before, but I've worked with ClickUp, Notion, Monday, and other tools. They're not all the same, but everything made sense in terms of how the projects were set up. I appreciate you blocking all that out. It was very helpful just to have a direction of where to go.

**Daniel Lopes:** Yeah, the main thing is I can walk you through some of the GitHub stuff today if you want. I sent you the workshops first because that's how we talk about the work and how to teach people. And then there's this community called Circle that we use internally. That's how our team learns to use the workflows. I can show you that as well.

**Kirkland Gee:** So I'm missing access to Circle and AirTable.

**Daniel Lopes:** So what did you get from the rest of the team? I heard you got access to some stuff last week.

**Kirkland Gee:** Yeah, basically what a typical account manager would get. I got access to Slack, Notion, Fathom, OnePass, and Google account.

**Daniel Lopes:** Okay, let me add you to Circle. So Circle is organized this way and we have courses on workflow creation and client management. The article production course is the main one. Circle is a little bit wonky to work with, but it serves the purpose. I used to do LMS stuff at my agency years ago.

**Kirkland Gee:** We used a platform called Coassemble back then, and it was a nightmare.

**Daniel Lopes:** My last project was an LMS with videos, audio, a mobile app, and an AI chatbot agent inside to talk to all the content. It makes sense, right? That's the future.

**Kirkland Gee:** It's a perfect use case for that sort of thing.

**Daniel Lopes:** The main things we use with clients are AirOps, workflows, the client workspace where we share data, and AirTable for strategy and assignments. Let me add you to AirTable now as well.

**Kirkland Gee:** From a tool perspective, what does AirTable do that Notion doesn't accomplish?

**Daniel Lopes:** It's like a super-powered Google Sheets. We use it for storing all assignment data—what clients are going to write about, what's revealed that they should write. You have the UI for clients to interact with our account managers. They paste content, move things around. You have things like VLOOKUP and grouping that Notion's database doesn't support. Notion's database is really limited, so that's why we use AirTable. But the plan is to replace both AirTable and Notion with our own product. We're building something to replace a big chunk of it, especially AirOps. AirOps is super error-prone and people have a hard time learning it. I can show you by the end of the week what I'm working on to replace AirOps. We're essentially replacing the article production course with our own stuff, making it self-learning so you don't need a course to use it.

**Daniel Lopes:** Chapter Five on prompting engineering is really important. Most people think you can just get anything out of LLMs, but there's nuance and technique. The whole book is amazing—really worth reading. Chapter One and Two are good intros, but Chapter Five is essential for all of us. Now the GitHub repos: we have two main codebases. We have Flow, which is where all our workflows are. We used to have workflows in AirOps, but they got super complex, so we created a workflow framework on top of Intemporo, which is a distributed systems runtime. Every workflow is a self-contained folder with steps, functions, and prompts. For example, we have workflows for client research where we do company research and analysis. You can see all the prompts for a workflow in one place. It's designed so you can look at the folder inside Cursor and Cursor will have the context for the whole workflow. It's executed as an API. We make API calls to our backend, and the backend uses Intemporo, which makes calls to our APIs. We have the Intemporo UI that you can see what's being executed.

**Daniel Lopes:** We have this UI here, that we use the team I found.

**Daniel Lopes:** So you can just get that from our one-classroom.

**Daniel Lopes:** If we see one of the media platforms, one-classroom.

**Daniel Lopes:** It's not a lot of data.

**Daniel Lopes:** But intemporo has this web UI that you can see what's going on, and what is getting executed.

**Daniel Lopes:** these are all running now.

**Daniel Lopes:** some of the things are completed.

**Daniel Lopes:** You can have a sense, you can understand what it's happening.

**Daniel Lopes:** So it's doing a bunch of stuff in parallel.

**Daniel Lopes:** You can see the input here.

**Daniel Lopes:** It doesn't have an output yet because it hasn't finished.

**Kirkland Gee:** I just try logging in through the team Google account, and it wants an iPad 2FA.

**Kirkland Gee:** Do you have that?

**Kirkland Gee:** Yeah, so that's in one password.

**Daniel Lopes:** Oh, duh, Yeah.

**Daniel Lopes:** And so sometimes you will ask for a device.

**Daniel Lopes:** the bottom right of Google, you have like a tri-different ways, and then you can get the Google authentic error.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** Yeah.

**Daniel Lopes:** So 10.4 is this, but we also have this UI here.

**Daniel Lopes:** But this is on top of 10.4.

**Daniel Lopes:** So again, it's a major friendly, and it's designed for our space.

**Daniel Lopes:** So this is the ID that we're building to make possible for people like Marcel, and even for ourselves, research and people other than it.

**Daniel Lopes:** You need to see what's going on.

**Daniel Lopes:** on then and temporal.

**Daniel Lopes:** So, for example, like they're running now an assignment creation.

**Daniel Lopes:** If I click on this, I can see the input of the API, the workflow, the output hasn't finished yet, and I can see the description.

**Daniel Lopes:** So, the description here is pulling the XML file from here.

**Daniel Lopes:** So, we have this XML.

**Daniel Lopes:** They read me already using XML with a mermaid outline and the description.

**Daniel Lopes:** And this is how to generate it.

**Daniel Lopes:** But this is getting loaded here.

**Daniel Lopes:** So, this is exactly what's getting displayed here.

**Daniel Lopes:** And every activity, you can see the input and output.

**Daniel Lopes:** So, this is an API called 2SC and rush.

**Daniel Lopes:** This was the result.

**Daniel Lopes:** And then we analyze that.

**Daniel Lopes:** And then next step is trying to see if there is any keyword traffic for that.

**Daniel Lopes:** It didn't have.

**Daniel Lopes:** And then another one, another one.

**Daniel Lopes:** And then it starts creating the top URLs.

**Daniel Lopes:** And then cleaning.

**Daniel Lopes:** the three articles, and then analyze the entire data content.

**Daniel Lopes:** So it's analyzed in each one of the cleaned pages.

**Daniel Lopes:** Like this workflow takes like three minutes, and you can see the code here.

**Daniel Lopes:** So in GitHub, you'll be able to find the workflows.

**Daniel Lopes:** Also, sorry, in 10.4, I'm sorry, in Studio, you can come here and it can click code, and it will take you to the folder where it should be.

**Daniel Lopes:** I hope I need to change the place, so now it should be packages.

**Daniel Lopes:** There's a missing folder here, but it should be search, packages.

**Daniel Lopes:** We added a packages folder, so I need to fix that.

**Daniel Lopes:** But you can see the name of the workflow here.

**Daniel Lopes:** You can find that in the code base.

**Daniel Lopes:** So, for example, that one was called SEO.

**Daniel Lopes:** Wanting the tutorial article draft, a zero content, the tutorial, article draft.

**Daniel Lopes:** We are looking for the workflow file.

**Daniel Lopes:** But this is the workflow file.

**Daniel Lopes:** Your profile is usually small.

**Daniel Lopes:** So this one, if I go into the folder, and then I have the activities, the activities is actually what does the work.

**Daniel Lopes:** And you can see the models get used.

**Daniel Lopes:** Like this is opening up, you have a perplexity, and all that stuff.

**Daniel Lopes:** So if you just started looking around and reading the sources of flow, that would give you an idea of how our workflows are done today.

**Daniel Lopes:** And in base scan, we have a full load of workflow request.

**Daniel Lopes:** And there are some things about how we use the workflows as well.

**Daniel Lopes:** All the generators that will create your workflow for you.

**Daniel Lopes:** And the first version, and then you can, there's like a way of like using it inside cursor that you barely have, you barely have to, like you don't have to write almost any code.

**Daniel Lopes:** You're just like talking to the workflows and all orchestrated based on the personal rules and a bunch of other stuff we did.

**Daniel Lopes:** So you have, like we have the cursor rules here, describing how the framework works, know, of cool, do we write it.

**Daniel Lopes:** cursor is speaking up all that automatically while us knowing which folders to load.

**Daniel Lopes:** So the check window with cursor is pretty powerful in the setting.

**Daniel Lopes:** We have a bunch of tickets here that we need to work on.

**Daniel Lopes:** But I was thinking like maybe today you just go through the base team stuff, like we did it from engineering capture, like take a look on our tools, like snack notes, and you did some of that already.

**Daniel Lopes:** Watch the circle, especially the production class that edit where all the content production class.

**Daniel Lopes:** And then tomorrow.

**Daniel Lopes:** I have a freaking all day, yeah, yeah, so that's going to take me the whole day, but you can, yeah, maybe I can get you here just to leave it to set up the environment, set up your local environment free with you.

**Daniel Lopes:** And you can have everything running and he can explain you some of the, I will do some other stuff, but at least maybe like 30 minutes or one hour, I'll see if that's available.

**Daniel Lopes:** And yeah, and then maybe on Wayne is they all thinking like we work on some of the workflows together so you should understand like my way of using this stuff.

**Kirkland Gee:** Sure.

**Daniel Lopes:** And then from there we can give you like a smaller workflow just for you to get an idea of how everything works and give something in here first week.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** that make sense?

**Kirkland Gee:** Yeah, does.

**Kirkland Gee:** Yeah.

**Daniel Lopes:** Yeah, so a lot of stuff we have is just like improving on existing workflows some stuff we have to do new API client.

**Daniel Lopes:** and spring images or combine workflows.

**Daniel Lopes:** Some stuff like, for example, we want to remove the 404s, and then they stuff that we generate, so that's another meaning workflow that we would have to do.

**Daniel Lopes:** We have some stuff seen in the AirOps that we want to migrate.

**Daniel Lopes:** This client here, for example, they use this tool called capital.ai, and Kappa is a chat agent for their developer docs.

**Daniel Lopes:** They want to have that as a fact check at the end of the process to rewrite any of the scripts, any of the codes and intents that we include in the articles.

**Daniel Lopes:** Well, that's another workflow we'd have to do.

**Daniel Lopes:** These are the smaller tests and the workflows.

**Daniel Lopes:** Everything that the folks are asking, so we get people asking for some of the engineers to support.

**Daniel Lopes:** Where everybody's making their requests, sometimes they will make a request for a workflow, or most of the time they are talking about issues that

**Daniel Lopes:** experience.

**Daniel Lopes:** But it's also up to us to look at how they're using things and come up with bad ways of joining those stuff.

**Daniel Lopes:** So that's the workflow side of the thing that I'm thinking that it would be you and me building a lot of these workflows.

**Daniel Lopes:** there you have that Felica does some of it, Marcus does some of it, but Felipe is better at orchestrating an architecture in larger systems.

**Daniel Lopes:** Marcus is doing support.

**Daniel Lopes:** So Marcus is part time of us.

**Daniel Lopes:** Marcus is a senior engineer, super experienced, but he's like his part time of us working only like two or four hours a day.

**Daniel Lopes:** And that's a good use of his time is just to answer everybody's needs here and touch little stuff.

**Daniel Lopes:** But you and me, we have like business understanding, you have experience with SEO, you have experienced running agencies, a lot of stuff that I don't have.

**Daniel Lopes:** So like you building workflows and like seeking out ways to make the team more efficient is

**Daniel Lopes:** another level, and so we have this workflow wise.

**Daniel Lopes:** It's also small stuff, it's not just a workflow.

**Daniel Lopes:** So I think there's a kind of bugs, for example, like we just found a bug.

**Daniel Lopes:** I would just log the bugs here, as far as we'll get actually.

**Daniel Lopes:** I would give you the nomenclature of everything too.

**Daniel Lopes:** So we have, flow is the code base, no UI, it's an API of workflows, it's the one that I showed you.

**Daniel Lopes:** And then flow studio, that's the IDE is a separate project, it's a React app with a Rails backend, so there's auto-github repo for that.

**Daniel Lopes:** So we found a bug in the studio, and I'm using this emoji to make it easy to scan, which one is stuff that we're dealing with.

**Daniel Lopes:** So, a code button, that's bug, right?

**Daniel Lopes:** It's more.

**Daniel Lopes:** And so that's all the small stuff we put here, and those are things that we can do in like a day to day is maybe three days, but everything that's smaller than like a week, and then we have the bigger stuff is what we're putting here.

**Daniel Lopes:** And I think like a lot of the stuff that we, you and me, would be working together would probably also be productizing a lot of the workflows coming up with micro apps and things that we could make available to any person.

**Daniel Lopes:** So that's what I'm putting here as a store, we have things like one of the workflows that want, that one of our clients once today is read an article and come up with illustration ideas and photo ideas, you know, yeah, like that could, that would.

**Daniel Lopes:** we already have.

**Kirkland Gee:** Just turning that into something with you know, easy to use.

**Kirkland Gee:** Somebody can just go in and.

**Kirkland Gee:** Yeah, exactly.

**Daniel Lopes:** So if you have any ideas for small or large stuff, feel free to log them here in Basecamp. We have folders for larger and smaller projects. Just put your ideas there and we can discuss. The way we divide it is: Flow is the command-line slash API framework, and then we have the store for micro-apps. Atlas is a project we're still building up that will replace AirOps and Notion—it's GTM-specific. We have three lanes: the clear ones where we know how we want to do things, a miscellaneous section for things like email and AI stuff that don't have their own category yet, and a learning section. The plan is to design mockups and UI for everything. The first functional screen will be the AirOps replacement. From there, we'll start a new Basecamp project with the timeline, task breakdown, and micro-previews of everything.

**Kirkland Gee:** That all makes sense. I'm in the EPD project now.

**Daniel Lopes:** Good. Do you have anything else you want to talk about? We're almost out of time and I talked too much. But this week, the goal is just to sponge and observe. Get a good idea of everything going on. I don't feel like you have to produce anything. Just get a sense of how our client team works. Watch some client calls if you have time, pay attention to channel discussions, explore client Notion docs, and play around with the tools. We'll do a workflow together. The goal is just to get as much context as possible.

**Kirkland Gee:** That's the priority.

**Daniel Lopes:** Yeah, that's priority number one. Everyone who joins the team wants to do something, but it's better to get context first so you don't spend energy in the wrong direction. This week or next, don't worry about delivering anything. Just pick your own pace to learn. And make sure we set aside some time to study the theory of AI engineering. Chapter Five is important.

**Kirkland Gee:** Do I have access to the whole book?

**Daniel Lopes:** Yes, the whole book. It's really worth reading the whole thing. Chapter One and Two are good intros, but Chapter Five is essential.

**Kirkland Gee:** That book is great.

**Daniel Lopes:** It's still pretty up to date. She launched it about six months ago.

**Kirkland Gee:** That's wild.

**Daniel Lopes:** It's gorgeous. Feel free to ask any questions. We're always here to help each other. The engineering chat is there with Marcus and me. We're available in different time zones.

**Kirkland Gee:** I appreciate it. I'm super excited to be here.

**Daniel Lopes:** Thanks, and thank you.
