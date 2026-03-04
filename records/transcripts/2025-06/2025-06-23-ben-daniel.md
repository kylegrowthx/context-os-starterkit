# Ben + Daniel

<metadata>
date: 2025-06-23
time: 22:17 UTC
duration: 45 minutes
organizer: daniel@growthxlabs.com
participants: Ben Church (GrowthX), Daniel Lopes (GrowthX)
fathom_recording_id: 70033198
fathom_url: https://fathom.video/calls/334091169
share_url: https://fathom.video/share/Qf4XnRHTQsusyZWZavRY9byWk1PYxYzS
source: fathom
enriched_on: 2026-03-03 20:57 UTC
</metadata>

---

## Summary

Daniel Lopes onboarded Ben Church to the GrowthX engineering team, covering the transition from AirOps and Airtable to two new in-house systems: Atlas (a project management and workflow triggering UI replacing AirOps) and Flow (a workflow orchestration framework being built by Clint, Stefano, and Jumpy). Daniel emphasized a measured onboarding approach—Ben will spend the first week reading documentation and understanding the codebase, then move to hands-on work with mock workflows, with weekly check-ins planned for the first month to guide his ramp-up.

---

## Context

Ben Church is a new engineering hire at GrowthX, joining on June 23, 2025. This call is his formal onboarding with Daniel Lopes, the CTO/engineering leader. The context is urgent: GrowthX recently had to exit AirOps (a no-code platform) due to a relationship breakdown with the vendor, leaving the company with a hard deadline to move off their infrastructure. This forced a rapid build of two replacement systems: Atlas (a Next.js application for managing execution triggers and CSVs) and Flow (an orchestration framework for LLM interactions and API calls). Daniel had been in "battle mode" for three weeks shipping Atlas to feature-parity with AirOps. Ben joins a team of Clint, Stefano, Jumpy (focused on Flow and Flow Studio), Brad (generalist helping with Atlas), and Ren and George Main (working on Airtable replacements). Daniel's approach to onboarding is deliberate—he wants Ben to absorb documentation and context first before diving into code, to prevent early misdirection.

---

## Relevance

**To GrowthX Delivery:**
- Critical infrastructure transition in progress: AirOps exit deadline drove rapid 3-week build of Atlas replacement. Delivery timeline and client continuity depend on Atlas and Flow stability in the next 2-4 weeks.
- Ben's Airbyte experience (AI-related and workflow logic) maps directly to Flow framework development, a core strength area for the team.
- Onboarding cadence: weekly meetings for first month will help identify blockers and keep Ben unblocked on critical path items.

**To CheckThat:**
- Flow is being considered for potential open-source release and productization beyond GrowthX's internal use, representing a significant strategic product opportunity.
- Flow's design for LLM interactions and API orchestration aligns with CheckThat's AI visibility and automation work.

**To GrowthX Business Development:**
- Atlas shipping on-time signals delivery capability and reduces churn risk from the AirOps forced migration.
- Successful in-house tool development (Atlas, Flow) positions GrowthX to scale the agency model without third-party vendor dependencies.
- Long-term vision includes scaling to $12-20 million ARR on the agency side using AI-powered tools.

---

## Overview

- GrowthX.ai is transitioning away from AirOps and Airtable to in-house solutions (Atlas and Flow)
- Flow is a workflow orchestration framework with potential for open-source release
- Atlas is the client-facing application for managing content creation pipelines
- Long-term vision includes scaling the growth agency model and potentially productizing the Flow framework

---

## Key Topics

### Project Overview: Atlas and Flow

  - Atlas: Client-facing application for managing content creation pipelines
      - Replaces AirOps and Airtable functionality
      - Features include project management, pipelines, and context artifacts
      - Built with Next.js
  - Flow: Workflow orchestration framework
      - Handles LLM interactions and API calls
      - Potential for open-source release
      - Separate from Flow Studio (UI for Flow)

### Team Structure and Responsibilities

  - Clint, Stefano, and Jumpy: Focused on Flow and Flow Studio
  - Brad: Generalist, currently helping with Atlas
  - Ren and George Main: Working on Airtable replacement features

### Current Development Priorities

  - Completing Atlas features to replace AirOps functionality
  - Improving Flow Studio to make workflow creation more accessible
  - Refining the structure of the Flow framework for potential productization

### Future Vision and Goals

  - Scale the growth agency model using AI-powered tools
  - Potentially productize the Flow framework for other industries (e.g., recruiting, virtual assistants)
  - Aim for $12-20 million ARR from the agency side of the business

### Technical Considerations

  - Need to improve packaging of workflow files outside the Flow system
  - Considering a GitHub-based workflow similar to dbt for managing workflows
  - Balancing code-first approach with user-friendly interfaces for non-technical users

---

## Action Items

**Ben Church (GrowthX)**
- Talk to engineers and client-side people to understand product context and usage
- Chat with Jason Gong about how Flow/Flow Studio is used in practice
- Start editing in Flow/Flow Studio by end of day June 24
- Set up weekly check-in meetings with Daniel for the first month

---

## Transcript
**Ben Church:** Sorry, was chatting way too long.

**Daniel Lopes:** Oh, good.

**Daniel Lopes:** Nice.

**Daniel Lopes:** I had a chance to meet him already.

**Ben Church:** Yeah, he's my onboarding buddy, so we got some time.

**Ben Church:** Looks like he's traveling, so it's good.

**Ben Church:** I'm going to catch him tomorrow, the next day.

**Ben Church:** He's going through Flow Studio.

**Ben Church:** I haven't gone through Atlas yet, but he'll show me some of the prompt stuff he's working on.

**Ben Church:** Anywho, now after that call, you know when you get the itch, I'm like, okay, I need to make sure these tools are set up so I can just get in there and tinker.

**Ben Church:** Yeah.

**Ben Church:** My later tonight, probably.

**Ben Church:** How are you doing?

**Ben Church:** Yeah.

**Ben Church:** You shipped a, it sounds like you've been in a battle mode for like two weeks.

**Daniel Lopes:** Wow.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** This probably has been like the hardest amount of coding I've done in a short amount of period in a long, long time.

**Daniel Lopes:** Probably since my F days.

**Daniel Lopes:** Yeah.

**Ben Church:** Yeah.

**Daniel Lopes:** If you look at the commit history of Atlas, see like three weeks ago and then, but yeah, it's going well.

**Daniel Lopes:** It's going, like I was super concerned like three weeks ago and because we had like the bulk of the functionalities, but there is always like that, all the details that come with like the creating close to shipping that actually is like 90% of the other 90%.

**Ben Church:** Yeah, yeah, the last 5% is the biggest part.

**Daniel Lopes:** Yeah, exactly.

**Daniel Lopes:** So, but it's, it's, it's there.

**Daniel Lopes:** Like I think now we are at the point where it's like pretty much feature complete compared to what we needed from AirOps.

**Daniel Lopes:** So I don't know how much you understand about how we were working already, but we have, we were using AirOps quite a bit as a user interface and AirOps would trigger the API calls to the, to the flow project that Clint is working on.

**Daniel Lopes:** That project has a user interface, but it's more for us to understand what's going on with the workflows without having to go into the temporal dashboard.

**Daniel Lopes:** It's like super technical and doesn't have some of the abstractions we use and things like that.

**Daniel Lopes:** So that UI was just almost like the beginning of an editor, like a mini IDE that we want to make into something bigger over time.

**Daniel Lopes:** We had no UI for the triggering and managing of the executions.

**Ben Church:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So that's the Atlas project.

**Daniel Lopes:** And it's essentially, we need to come up with better names.

**Daniel Lopes:** These are all just code names for the project.

**Daniel Lopes:** But we have Atlas, the way you think about it is what we were using for, we had like, if you go through all the oral documents, you see that we use Airtable quite a bit.

**Daniel Lopes:** We use Airtable is where the marketing team will put, like the delivery team will put all the keywords, all the things that they want to write about.

**Daniel Lopes:** And then choose.

**Daniel Lopes:** to the client.

**Daniel Lopes:** And then we have the Notion documents for that client.

**Daniel Lopes:** So each client gets a folder with their documents.

**Daniel Lopes:** And then we had AirOps as the place to trigger the API calls and input CSVs and get CSV out of it.

**Daniel Lopes:** And the people that copy and paste the results and post them to the CMSs and things like that.

**Daniel Lopes:** And I don't know how much you know about the backstory of why we're getting out of it so fast, but...

**Ben Church:** I heard there's, as I understand it, like a little bit of a falling out.

**Ben Church:** And then you got a deadline by them.

**Daniel Lopes:** Exactly.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So it was more like a perfect storm.

**Daniel Lopes:** So it was like a couple of mistakes here and there.

**Daniel Lopes:** One from Marcel, another one from the tool that Tucker was using that we tried to like hire some folks from their team by accident.

**Daniel Lopes:** So there were a few things that piled up to the CEOs.

**Daniel Lopes:** Like, what the ?

**Daniel Lopes:** In our CEOs?

**Daniel Lopes:** was like, what the ?

**Daniel Lopes:** You guys stealing our clients?

**Daniel Lopes:** So...

**Ben Church:** So...

**Ben Church:** So...

**Ben Church:** So...

**Ben Church:** Okay, how's, first question, because I know you're probably tired, and you probably have a lot to do.

**Ben Church:** Are you good to chat right now?

**Daniel Lopes:** Like, are you okay?

**Ben Church:** Like, do you need a breather?

**Ben Church:** I'm not sure if there's any fires going on.

**Ben Church:** I know you just released that.

**Daniel Lopes:** No, we have just one thing that I want to ship today, and then I have, like, some planned tasks for today, related to the release, but nothing.

**Daniel Lopes:** Related from the stuff that we shipped yesterday, but nothing crazy.

**Ben Church:** Cool.

**Ben Church:** When should we plan to jump off?

**Ben Church:** In 20 minutes?

**Daniel Lopes:** No, I have another call.

**Daniel Lopes:** I'm meeting everybody that's starting today, so I'm meeting with Pedro at 4, and then Jean-Pierre at 5.

**Ben Church:** Okay, great.

**Ben Church:** We'll plan to stop at least a little bit before 4, so you can take a breather in between.

**Ben Church:** Okay, and then what's the high-level goal for this call?

**Ben Church:** Wow, I've got, like, some, like, sneaky little questions.

**Daniel Lopes:** It's like always, but what do you typically want to get across?

**Daniel Lopes:** Yeah, like I just wanted to give you a quick tour of like the linear project and like usually the way we're on board folks, would be like first week, there's so much to absorb that this and folks sometimes will come in like super excited to do a ton and then they start like doing a ton in the wrong direction.

**Ben Church:** Like in the second week, it's like, hey, go back here and like read this first, you know?

**Daniel Lopes:** So it's almost like better to start a little slow and, but if you see opportunities and things that you want to do, like feel free.

**Daniel Lopes:** Like I saw you like jumping in and like some stuff around like an EPT channel or like, like you said, like if you want to have all the tools running on day one and just like poke around and feel free.

**Daniel Lopes:** There's a ton of documents in Notion and then there's the linear project.

**Daniel Lopes:** I can walk you through the linear tickets just to give you an idea.

**Daniel Lopes:** And there's like no, no expectation that you finish all that like super fast or like even that you finish everything, but it's more like.

**Daniel Lopes:** So there is the beginning, like the first milestone is essentially like all the things to read and then the second milestone, like all the things related to the code base.

**Daniel Lopes:** And then do some mock work trying to create some workflows and see how that works.

**Daniel Lopes:** By the way, to think about that part of the work there, it's almost like everything we have is just almost like an MVP of an MVP, you know?

**Daniel Lopes:** So a lot of the things ideally will like evolve, especially on the flow project.

**Daniel Lopes:** And the team today is structured as the team that would be most likely working most of the time on the flow stuff, like either the studio and the framework.

**Daniel Lopes:** And then we have, and so that's like Clint, Stefano, and Jumpy, I think it would be like mostly there as well, because like he has a ton of experience with building AI-based products.

**Daniel Lopes:** Thank you.

**Daniel Lopes:** Thank

**Daniel Lopes:** It's very strong UX sense, so it would probably be super useful having to figure out the user interface for that area, for the studio, and Clint and Stephanie both have a ton of experience with distributed systems, like doing a lot of stuff with Lambda, lot of stuff with high volume scraping, high volume parsing of social media data and stuff like that, so that's what he did before.

**Daniel Lopes:** And Clint has a ton of experience with all the HashiCorp stuff, so, and I think that might be the place where I think like you would probably spend most of your time too, think would be like your experience with Airbyte and everything that you were doing, like AI related, all the things that you helped build for Airbyte has so much value in that space.

**Ben Church:** Yeah, it was fun when I was chatting with Clint, he's like, yeah, the Atlas workflows are going to be here in flow, but that's not right, because we have to...

**Ben Church:** I can jump, you know, these codes in the next year.

**Ben Church:** I'm like, oh, that's ringing a lot of bells there, right?

**Ben Church:** It's like, how do we take your logic?

**Ben Church:** How do we move it around?

**Ben Church:** How do we version it?

**Ben Church:** How we execute it safely?

**Ben Church:** Yeah, I got you.

**Daniel Lopes:** Yeah, exactly.

**Daniel Lopes:** And then we have the, so that team, I'm thinking, we wouldn't have, like, specific, folks are jumping around.

**Daniel Lopes:** So if you see, like, Stefan is helping on the, have the project, Clint is, like, helping with, like, some downtime that we had earlier today.

**Ben Church:** So people jump around and they will work in different things because we're still small.

**Daniel Lopes:** But it's almost like those are the kind of projects that you would be, that those folks would be thinking, they would probably be better skilled to do faster than, like, if I put, like, myself on, like, some of this stuff, you know?

**Daniel Lopes:** So, and then we have Brad.

**Daniel Lopes:** Brad is kind of a generalist.

**Daniel Lopes:** Like, he can do, like, a lot of UI stuff.

**Daniel Lopes:** He has a lot of expensive React.

**Daniel Lopes:** He had his own company a couple of times.

**Daniel Lopes:** So he can think of product and he can go pretty deep technically, too.

**Daniel Lopes:** So he's a super great engineer.

**Daniel Lopes:** So Brad, either way I'm thinking about him, is just like everything that's a lot user interface focused or large enough features that we need to have somebody start.

**Daniel Lopes:** Brad would be somebody that would be in this area.

**Daniel Lopes:** Right now, he's helping with Atlas a ton.

**Daniel Lopes:** And we have some other areas.

**Daniel Lopes:** Atlas right now is just like the Pipelines feature.

**Ben Church:** And I can actually show you that.

**Daniel Lopes:** But Pipelines feature is essentially AirOps replacement.

**Daniel Lopes:** But if you have this, I can actually do a quick screen sharing.

**Ben Church:** Yeah, please.

**Daniel Lopes:** to see.

**Daniel Lopes:** So today, if you log into a local account instead of the production account, it's slightly different.

**Daniel Lopes:** So we have a bunch of hidden data.

**Daniel Lopes:** So the production account, if you go to atlas.growthx.ai, and you open an interview account, you go straight, you only see context artifacts and you only see pipelines and projects.

**Daniel Lopes:** So you can create projects and you can see the pipelines that project has.

**Daniel Lopes:** And this project was so slow, need to figure out the performance of everything.

**Daniel Lopes:** And then we have context artifacts.

**Daniel Lopes:** So, but local, you see all the other things that we're thinking about.

**Daniel Lopes:** So those are just like mock data that I put just for people to understand how we're thinking because people are having a tough time understanding, okay, like we have these three projects, how do they fit together?

**Daniel Lopes:** And so you have like, imagine you are somebody on the delivery team running a client account, they would have a workspace with the client.

**Daniel Lopes:** And you essentially have a project management tool with everything you need to deliver the content.

**Daniel Lopes:** And you have like an inbox where you could send a message to the client about the updates of the week.

**Daniel Lopes:** You'd have pages and opportunities.

**Daniel Lopes:** So this is something that Ren and George Main are working on.

**Daniel Lopes:** And this is essentially the replacement for Airtable.

**Daniel Lopes:** So Airtable today, we load all your potential opportunities.

**Daniel Lopes:** We find opportunities from something like SEMrush.

**Daniel Lopes:** We kind of analyze your website with a tool like SEMrush, see what you wrote about and what you haven't.

**Daniel Lopes:** So you see that content gap.

**Daniel Lopes:** So we load all this.

**Daniel Lopes:** Like we run all these things through some workflows, and then we load everything into Airtable.

**Daniel Lopes:** But that's like a one-off thing.

**Daniel Lopes:** And what we want to do is like do that on the regular.

**Daniel Lopes:** And we want to get out of Airtable as well.

**Daniel Lopes:** So Airtable, pay a fortune.

**Daniel Lopes:** I think Airtable, pay more, probably more than like 8K a month or 10K a month.

**Ben Church:** Yeah, bet.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So, and it's very confusing.

**Daniel Lopes:** So like every time I

**Daniel Lopes:** Client starts or new employee starts.

**Daniel Lopes:** You have no control of what they're seeing, like no control of they're doing.

**Daniel Lopes:** There's no way to run things on the regular.

**Daniel Lopes:** So without a ton of API integrations, then you have like 40 accounts.

**Daniel Lopes:** have to replicate the automations on every account.

**Daniel Lopes:** It's a mess.

**Daniel Lopes:** So the thing is mess we have to deal with with AirOps.

**Daniel Lopes:** We have to deal with in Airtable.

**Daniel Lopes:** It's just a little less painful.

**Daniel Lopes:** And so this would replace Airtable.

**Daniel Lopes:** All these things, like the way we're thinking is like pretty much all the features, if we could rethink them, a new product that can have a bunch of like small reasoning features on every screen, you know.

**Daniel Lopes:** And those would be all API calls through Flow.

**Daniel Lopes:** So like let's say, for example, when you're creating a document that will be used as context for some of the writing we do.

**Daniel Lopes:** Like today we have this thing called context artifacts and you have like personas, you have the company context and you have like writing guards.

**Daniel Lopes:** Ideally, could just come here and say, improve, is this good enough for this account?

**Daniel Lopes:** Or make it better, or get from some other client that's similar, or rewrite this, or add more examples.

**Daniel Lopes:** Some of that we can do already because of the AI editor here with TipTact has integration with Flow, and will trigger custom workflow.

**Daniel Lopes:** So we were sprinkling a bunch of the workflow things that we can build with Flow everywhere in this product.

**Daniel Lopes:** And so the context artifacts is this idea, activity feed would be just like a log of everybody's doing.

**Daniel Lopes:** Knowledge base would be a vector database for everything that we do research for you.

**Daniel Lopes:** It's like every time we write an article, spend like a dollar of like API calls to perplexity and a bunch of other things, combine this giant document, and we put it nowhere, we lose it.

**Daniel Lopes:** And the same thing with...

**Daniel Lopes:** Same thing with our, ideally you would be monitoring your competitors, the clients would be able to also say like, we like these sources, can you scrape these sources for me, or I have this bunch of PDFs that I want to create content from it, and then we don't have the way to do that today.

**Daniel Lopes:** So the knowledge base would be this collection of data sources that we can use for creating content or validating that the content is factual or not.

**Daniel Lopes:** So those are the top level features for the project.

**Ben Church:** Yeah, so those are kind of like the context, mostly like context loading with the exception of like inbox, but even then that's a bit of a context loading because you're going back and forth with a client.

**Ben Church:** Mm-hmm.

**Ben Church:** Okay, I got you.

**Daniel Lopes:** And then you would have like pipelines, and pipelines is what we build today.

**Daniel Lopes:** So pipelines, we have this thing called assignments that's like a big thing in the way people usually write, where like if you're going to write something, you usually start with like a newsroom or something like this, the managing editor would come up with an assignment for you.

**Daniel Lopes:** And then you have like research, and then you...

**Daniel Lopes:** Work on the outline, and then at the end, you work with the editor again to validate that it's good.

**Daniel Lopes:** So we have a workflow today that generates assignments.

**Daniel Lopes:** So if you go in any of the article generation pipelines you have, which is kind of a standard pipeline that almost all clients have, you see that the first step is an assignment brief.

**Daniel Lopes:** But this is a large enough thing that we do that I think we will plug it out and have a feature, a standalone feature here called Assignments, that will convert opportunities that we find in this area into assignments in that project that can be passed to the pipeline.

**Daniel Lopes:** And then once it's done in the pipeline, it could be staged for publishing, and that's when the client can come in and interact with it, and maybe change things in themselves and all that.

**Ben Church:** And those assignments, that's an area of the product currently?

**Ben Church:** Or is that one of the dummy dot spots?

**Daniel Lopes:** No.

**Ben Church:** Okay, so pipeline's what you got.

**Ben Church:** And these pipelines are all, I noticed the pipelines are all workflows in flow.

**Ben Church:** Is that right?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** It's a mix.

**Daniel Lopes:** So like the pipelines are essentially just stitching the workflows together.

**Daniel Lopes:** So, and the pipelines are defined like this.

**Daniel Lopes:** So you have an input schema with the form you want.

**Daniel Lopes:** And you also have some environment data that you can pass.

**Daniel Lopes:** And you can pass artifacts here.

**Daniel Lopes:** And you have the steps.

**Daniel Lopes:** The steps is essentially API calls.

**Daniel Lopes:** And they are all to flow.

**Daniel Lopes:** So whatever workflow we have on flow will be loaded here.

**Ben Church:** And you can reference them here.

**Daniel Lopes:** And so there's a little validation to make sure they exist.

**Daniel Lopes:** And then you can inform the input data that will be sent to that workflow.

**Daniel Lopes:** And you can manually define the output that you want out.

**Daniel Lopes:** And you can choose the user interface for that.

**Daniel Lopes:** that.

**Daniel Lopes:** And you can also flag it for human review, so if, and by default, the pipeline will execute continuously, so like we'll finish one workflow, pass the data to the next one, to the next one, to the next one, but if you put a human review there, we'll like pause and ask for the person to check, and we also have like a step-by-step mode that every step will just stop, and then you review and you save and continue.

**Daniel Lopes:** So, so like all these are like workflows in flow, this is the function, this is the workflow name, if you look in the flow code base, that we export functions as the, the workflow, and that's what getting executed, and, and then at the end, we have an output schema, and output schema is here at the top.

**Daniel Lopes:** So in this case is, the output schema is just one field called article, with a rich text, and the data for that is the data from this tab called internal links, so internal links is this one, so, yeah, so like we don't,

**Daniel Lopes:** have workflow code in Atlas, it just calls the the flow.

**Daniel Lopes:** So everything that's LLM, everything that's API based is all in flow.

**Daniel Lopes:** So does that make sense?

**Ben Church:** It does.

**Ben Church:** And this view that you have here of topic, assignment, brief, research, outline, article, draft, fact checking, internal links, that doesn't relate.

**Ben Church:** Does that relate to that must relate to a flow?

**Ben Church:** Yeah, yeah.

**Daniel Lopes:** like, each one of these is in a step.

**Daniel Lopes:** So like, if I open like this one, for example, I have all the steps here, each one of these is a workflow, and you can click here and inspect, and that will open this to you.

**Daniel Lopes:** And you can see that workflow executed, that workflow executed.

**Daniel Lopes:** So you can see the inputs and outputs.

**Daniel Lopes:** And you can see the workflow and the world as well.

**Daniel Lopes:** And you can see the code.

**Daniel Lopes:** And

**Ben Church:** So, yeah, each of these separate workflows are client specific.

**Ben Church:** Is that right?

**Ben Church:** Or some of them are generic?

**Daniel Lopes:** Not all.

**Ben Church:** Some of them are written.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So like, that's the thing that I can show you as well.

**Daniel Lopes:** Sorry, wrong project.

**Daniel Lopes:** But the flow project, the way to think about it, that took a while for folks to get it.

**Daniel Lopes:** But in my mind, it's more like the way I started thinking about it from the beginning is that we would have a bunch of like growthx specific things that if we're thinking like growthx as a marketing agency, we would have a bunch of stuff that's like marketing related and specific.

**Daniel Lopes:** And...

**Daniel Lopes:** And then you have also a bunch of stuff that would be like framework level things that you would, if we start a new company, let's say we want to do like the same idea, like let's say we have like a custom product specific for like a recruiting agency, for example, without the equivalent of Atlas for their space.

**Daniel Lopes:** Maybe that space doesn't need a pipeline system, for example, but these days, any new feature, any new product can be thought of like, what are the human extension things we can do with like this mini reasoning agents that we have now, and they will have a ton of things that overlap.

**Daniel Lopes:** So like, and that's like the framework level things that I'm thinking.

**Daniel Lopes:** like, you have things like evaluation, which is like an area of the product today that we don't do, and it sucks.

**Daniel Lopes:** We have, but we do have a tracing, for example, you want to see, so tracing, use length use, we use, we have brain trust as well, but we haven't used it yet.

**Daniel Lopes:** So we have all the tracing inter.

**Daniel Lopes:** Faces there for you to choose your tracing product, for example.

**Daniel Lopes:** And then we have all the things around entering the prompts and all the things around being able to pass data to the prompts.

**Daniel Lopes:** All the usual stuff that you'd have to have link chain and things like that.

**Daniel Lopes:** On top of the thing that I consider the hard part for dealing with APIs is like the orchestration of them.

**Daniel Lopes:** You know, like, so that's the managing when they fail, when they should retry, all the rate limits, all the stuff that you probably have a lot of fun at Airbyte.

**Ben Church:** So that's the stuff that we built on top of Temporal.

**Daniel Lopes:** So, like, there's some common infrastructure around Temporal as well.

**Daniel Lopes:** So, but in the ideal world, we would have a full structure that would be slightly different than this.

**Daniel Lopes:** So today we have, you should see here on the left side, we have packages, and then packages has...

**Daniel Lopes:** The next app, this is the API interface that will talk to the workflow and all that.

**Daniel Lopes:** And then we have the SDK, which has to be built up more and has the API clients.

**Daniel Lopes:** I think the API clients should not be inside of the SDK.

**Daniel Lopes:** And that's a part that I'd love to pick your brain on this later.

**Daniel Lopes:** And then we have a bunch of common things that probably should be packaged in more specific areas.

**Daniel Lopes:** There's some stuff about just string manipulation.

**Daniel Lopes:** There's some stuff around asynchronous calls.

**Daniel Lopes:** There's some stuff around Temporo, for example.

**Daniel Lopes:** Maybe they should have little folders and little namespaces for this.

**Daniel Lopes:** And then you have services.

**Daniel Lopes:** And then you have Entropic-related stuff and OpenAI-related stuff.

**Ben Church:** And then you have MCP-related stuff.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And then, so this is all non-Grovax-related at all.

**Daniel Lopes:** And ideally, it would make this more...

**Daniel Lopes:** Robust, and we could use that at other places.

**Daniel Lopes:** And then we have all the application logic layer.

**Daniel Lopes:** So Temporal here should be named something else.

**Ben Church:** be named like X.

**Daniel Lopes:** Workflows.

**Daniel Lopes:** Exactly.

**Ben Church:** Yeah.

**Daniel Lopes:** And then here is everything that is specific to our workflows.

**Daniel Lopes:** So we have some migrations with WV8.

**Daniel Lopes:** We don't use WV8 anymore, but we used to have WV8 as a vector database.

**Ben Church:** Gotcha.

**Daniel Lopes:** And then we have the scripts.

**Daniel Lopes:** This should be in the SDK.

**Daniel Lopes:** These are like some generators we have.

**Daniel Lopes:** And this will create the workflow from scratch.

**Daniel Lopes:** This will like update the catalog of workflows you have.

**Daniel Lopes:** So this is definitely should be in the SDK.

**Daniel Lopes:** And then, and maybe the name is not even SDK.

**Daniel Lopes:** Maybe it's a framework.

**Daniel Lopes:** So we're like, we're just defining all the things.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And then we have like, we have all the workflows inside and the workflows have full.

**Daniel Lopes:** There's, like, this is where things get specific.

**Daniel Lopes:** Like, for example, if we're going to have a bunch of little features, AI features for Atlas, like stuff like that, like, review what's in the screen or, like, a logo for you through brand fetch and stuff like that, we would put those inside Atlas.

**Daniel Lopes:** Then we have all some stuff, specifically certain clients, we have some things that are totally unrelated, like status tracker.

**Daniel Lopes:** This is just, like, a little thing that we have that we've actually never used, but can hit status pages of any provider we have and analyze if it's up or down.

**Daniel Lopes:** And we have some internal stuff, like, for recruiting, we have a folder for recruiting.

**Daniel Lopes:** So, like, that's just, like, all over the place, you know.

**Daniel Lopes:** So, like, if we ever, like, make things open source, or we package this, it wouldn't take the workflow sold.

**Ben Church:** Yeah.

**Ben Church:** Yeah, I got you.

**Ben Church:** at some point, like, if flow will evolve where those, you solidify, like, what the SDK is or, like, superset of SDK is in those workflow files.

**Ben Church:** Go somewhere else.

**Ben Church:** whether they're passed in by the caller or you have generic ones that are always available, just registered outside the project.

**Daniel Lopes:** Yeah.

**Ben Church:** I gotcha.

**Ben Church:** Because it becomes like your, this is your, this is your super orchestrator in a way.

**Daniel Lopes:** Right.

**Ben Church:** Right.

**Ben Church:** And it's more opinionated for some of these loops that you got going on.

**Ben Church:** Now, I noticed the O Studio is a separate project.

**Ben Church:** Like, was there, was there a reason to that one or like, was it just like, okay, we're just getting stuff done?

**Daniel Lopes:** It was more like reflecting the same, like two projects that I've been like, that has been like an interesting inspiration.

**Daniel Lopes:** Like one is, we have one of the tasks here is study the current state of AI workflows and tools.

**Daniel Lopes:** And we have.

**Daniel Lopes:** It's a link chain you're familiar with.

**Daniel Lopes:** Master is another one.

**Daniel Lopes:** don't know if you've played it.

**Ben Church:** It's by the Gatsby people.

**Daniel Lopes:** Yeah.

**Ben Church:** I saw when it got announced.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So, like, Master is, like, very similar, but they have – the way of writing is slightly different.

**Daniel Lopes:** So it's, like, almost looks like Clojure at the end.

**Daniel Lopes:** But they do have an IDE as well.

**Daniel Lopes:** They've been building up.

**Daniel Lopes:** It's, like, three months ago, they didn't have anything, which was pretty unusable.

**Daniel Lopes:** They're moving pretty fast, and it's getting pretty interesting.

**Daniel Lopes:** And the core thing is open source.

**Daniel Lopes:** The IDE is not.

**Daniel Lopes:** And they're going to charge for the IDE, I think, over time.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So similar to, like, DBT, for example.

**Daniel Lopes:** I don't know if you've used DBT before.

**Ben Church:** Yeah.

**Daniel Lopes:** And then another one is Moshe.

**Daniel Lopes:** Moshe is another one.

**Daniel Lopes:** Moshe, the studio is –

**Daniel Lopes:** So the playground is inside the repo, and it's combined, the masterguise is not, and same thing with Temporo, so Temporo has the Temporo SDK in the infrastructure, and it's the on folder, and ship it as an NPM package and all that, or they ship as a Go library or Python library, then, but their cloud stuff, even though it's fully open source, and you can run it locally as well, it's a separate GitHub rule, so, so that's the, and like the way I'm also thinking that.

**Ben Church:** Very similar to AirBite.

**Daniel Lopes:** So AirBite has this, oh yeah, AirBite has the UI and everything, and you guys are open source and all that, yeah, very similar.

**Ben Church:** Yeah, yeah, it's like, it's open source, a lot of the features are still, yeah, you know, good luck using them without paying something.

**Daniel Lopes:** Exactly, so it's the same idea.

**Daniel Lopes:** Yeah.

**Ben Church:** I hope that makes sense.

**Ben Church:** sense.

**Ben Church:** Okay, cool.

**Ben Church:** then so long term wise, what's your primary goal for like the next phase of the product?

**Ben Church:** Because there's like slow the SDK and studio the thing that you bundle up?

**Ben Church:** Or is it Atlas becomes more and more robust and people can self-sign up?

**Ben Church:** What's your preference?

**Daniel Lopes:** Yeah, think there's like two paths there.

**Daniel Lopes:** Our long term path is that we would be able to get the growth agency.

**Daniel Lopes:** Like what we're actually trying to validate here is that can you make things that are heavily based on like people time, something that can be scalable with today's tech, you know, like with LLMs and all that.

**Daniel Lopes:** And that's what we're trying to validate on the agency side.

**Daniel Lopes:** We're not trying to

**Daniel Lopes:** At the biggest agency in the world of like make the most amount of money there.

**Daniel Lopes:** were trying to talk about can we have a team of like a couple of people for a company like Airbuy or like a company like Abnormal or Augment Code and have them be like super productive and outperform like a large internal team or an external team that underperforms.

**Daniel Lopes:** And so that we started with just workflows.

**Daniel Lopes:** It became very clear that like workflows are like a lens are great, but you need the user interface that will go a way with that specific domain task, you know?

**Daniel Lopes:** So in this case, like if you're creating an assignment brief, maybe you need the text header, you know?

**Daniel Lopes:** And if you're picking images, you need the multiple choice thing.

**Daniel Lopes:** And like it's not, it's not a chat window for everything.

**Daniel Lopes:** And so like you ended up having to build this vertical focused apps.

**Daniel Lopes:** So I asked.

**Daniel Lopes:** It's just that.

**Daniel Lopes:** So it would be the vertical tool for making a growth agency scalable.

**Daniel Lopes:** And if we can make that thing a self-serving product, that would be amazing.

**Daniel Lopes:** But the moral of a short to mid-term goal there is I get that to the point that it's powerful enough that one person, that's maybe this person's heavily trained by us, like in the same way as like there's quite a few companies that do that.

**Daniel Lopes:** Like I'm not going to put the name of the company.

**Daniel Lopes:** And just like we escaped.

**Daniel Lopes:** But yeah, but like just like you're training like people to operate the tool for you, you know, instead of you operating it yourself.

**Daniel Lopes:** So if we get to that point where like we hired people that would be running the tool for you, and if you want to have access or you want to do it yourself, that's fine.

**Daniel Lopes:** But that wouldn't.

**Daniel Lopes:** We like the immediate focus.

**Daniel Lopes:** That's why we have like stuff like YAML settings for your pipeline.

**Daniel Lopes:** And you would never do that if you're doing like a self-serving product for normal people.

**Daniel Lopes:** So whatever we can do to get shortcuts there and get the folks on boarded fast, that's what we're doing.

**Daniel Lopes:** And we think just that side of the business, just the agency side, the growth and content agency alone, can get us to like $20 million in AR.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Like this year, you know.

**Daniel Lopes:** And a little bit of a stretch going on because we decided to like slow down so we don't like just grow too fast.

**Daniel Lopes:** But like I think like $12 million you can get there for sure.

**Daniel Lopes:** And then, but the thing that we're hitting all the time is like if we wanted to try to do that again for recruiting, for example, that's another thing that we're doing a ton and we see the needs.

**Daniel Lopes:** Or if we want to do that for...

**Daniel Lopes:** Or

**Daniel Lopes:** Virtual assistants is another thing that we use quite a bit to support all these pods that we have for the accounts.

**Daniel Lopes:** All these things could use the same infrastructure we have in the middle, where the workflows and everybody's hitting the same problems.

**Daniel Lopes:** have all these clients, and essentially in the AI space, we have Town, which is the company for the ex-CTO from Plaid.

**Daniel Lopes:** I'm meeting with him tomorrow, and they're all trying to figure out the same stuff.

**Daniel Lopes:** What's the infrastructure that I need, and how do I build this?

**Daniel Lopes:** It feels like we're back in 2004, where everybody's like, we need to build web apps, and what do we use?

**Daniel Lopes:** So we have Earl here with some crazy frameworks.

**Daniel Lopes:** We have some stuff with Seaside and Smalltalk, and some PHP stuff here, Cake.

**Ben Church:** And then there's Django and Rados, and what does it work?

**Ben Church:** They're going to get to the 2014 side of like, okay, we've got to send push notes.

**Daniel Lopes:** So the flow framework, the flow side of the product, way I'm thinking is in the next couple of months, we can get the studio to the point where people just look at it and say, okay, this makes sense.

**Daniel Lopes:** I could use it if it was set up for me, and I could create workflows.

**Daniel Lopes:** Like, for example, like, we completely removed Marcel and Jason, some of the guys that were creating workflows before in our office.

**Daniel Lopes:** We completely removed them out of the equation when we went in the direction of, like, you can only build stuff in code, you know?

**Daniel Lopes:** So, but if we're using Cursor, like, I don't touch the code at all, pretty much, like, 99% of the time for workflows.

**Daniel Lopes:** The same way that Cursor can generate React apps, like, really decently, it can generate workflows.

**Daniel Lopes:** Just a little bit of massaging, like a 99.9% right.

**Daniel Lopes:** It's better than React apps, for example.

**Daniel Lopes:** If the massaging is right, the context is loaded correct and all that.

**Daniel Lopes:** So the way I was thinking is if we have enough of the infrastructure of the framework defined, like the boundaries and how to encapsulate the workflows and all that, and we also move the studio in the direction where you can do some of the basic operations there.

**Daniel Lopes:** Today you can actually trigger workflows.

**Daniel Lopes:** Like a month ago you couldn't, so you had to use Postman.

**Daniel Lopes:** Now you actually have a form to submit the thing.

**Daniel Lopes:** But another thing would be like can we see the prompts that are getting executed?

**Daniel Lopes:** Can I get a little bit of tracing there?

**Daniel Lopes:** And can I maybe start a workflow there?

**Daniel Lopes:** You know, and then it will like bootstrap a folder for you and maybe like maybe in the future, like maybe in like three months from now we can like check.

**Daniel Lopes:** And then you can have, like, instead of using cursor and trying to, like, load the folders manually all the time and drag the files to be loaded into context, like, knows that you're working with that folder, it always loads that folder and loads the README as well, for example, you know.

**Daniel Lopes:** So, and then you can chat with that and change the code there.

**Ben Church:** I got you.

**Ben Church:** Okay, cool.

**Ben Church:** So, like, what I'm hearing is, like, originally chatting with Clint and seeing, like, okay, Flow and Flow Studio are separate, and I had a little laugh when Flow's API was built with Next.js and Flow Studio's friend was built with else.

**Ben Church:** It's, like, a very fun, like, swap.

**Ben Church:** I was, like, that's good.

**Ben Church:** But what I'm hearing is, okay, we want them a separate code base is because you might do open source for Flow, but Flow Studio being separate, we open the door if you want to go close source with the studio, and eventually, like, that's the payment gate.

**Ben Church:** Maybe, maybe not.

**Ben Church:** Who knows?

**Daniel Lopes:** Yeah, exactly.

**Ben Church:** And what I'm hearing is, like, a primary thing for Flow.

**Ben Church:** We have to figure out the packaging of workflow files outside the system, at least in a partial way, sooner than later.

**Ben Church:** Because you can imagine Flow Studio, if you want to iterate on a workflow or create a workflow, we can't just be editing the repository and redeploying on the fly.

**Daniel Lopes:** It's got to come from somewhere else.

**Daniel Lopes:** Is that fair?

**Ben Church:** Summary, as I work back at it?

**Ben Church:** Yes, yeah.

**Daniel Lopes:** Yeah, the two inspirations for the way of working in there, at least in my mind.

**Daniel Lopes:** So you have like one spectrum of this space is AirOps, or AirOps and N8N, and even like ZAC and IFT.

**Daniel Lopes:** IFT a little less because they haven't been able to move super fast in the AI space.

**Daniel Lopes:** But where you can just create agents, can create bots, you can create workflows, and your...

**Daniel Lopes:** Like any person, like random known technical person can do it.

**Daniel Lopes:** AeroOps is focused on the go-to-market space and SEO stuff.

**Daniel Lopes:** And then you have Zachary's generic and all that.

**Daniel Lopes:** And then you have, when you're on this extreme, you have Langchain, where you code everything and you can do anything with it.

**Daniel Lopes:** And then you go towards the middle, you have Vellum.

**Daniel Lopes:** Vellum is another one.

**Daniel Lopes:** Vellum is worth checking.

**Daniel Lopes:** Like they started as like a GUI-based thing and now they have an SDK.

**Daniel Lopes:** And the SDK controls the GUI space.

**Daniel Lopes:** But, so that's like the whole LLM space and AI workflow space.

**Daniel Lopes:** And then you have similar paradigm and way of working would be DVD, where you can, you have a GitHub repo.

**Daniel Lopes:** So in my, and the way I'm thinking is like, just to back up a little bit, like all the GUI-based stuff like Zapier and AeroOps, they are great for five years ago.

**Daniel Lopes:** Now that you.

**Daniel Lopes:** But coding agents that perform so well, you can actually express a lot of that crazy complexity that would have to do in like GUI-based stuff with flowcharts.

**Daniel Lopes:** You can express that in code much easier.

**Daniel Lopes:** And LLM can reason about that and can write for you.

**Daniel Lopes:** While drag-and-drop stuff, you're still asking the person to do it, you know.

**Daniel Lopes:** So, and LLMs can't do that that well.

**Daniel Lopes:** You need to do the language in between like a JSON translation or a YAML translation, something like that.

**Daniel Lopes:** They're not getting trained on that.

**Daniel Lopes:** You'd have to train them in yourself.

**Daniel Lopes:** Like you make LLMs work in that space much harder.

**Daniel Lopes:** So, but if you go like code first and that's your first line of like building on top, then we have a path where you can have like a chatbot that you can actually do super powerful things.

**Daniel Lopes:** And maybe in the future, like five years from now or like years from now, you can have that for anything, you know.

**Daniel Lopes:** So you can have a chatbot that will be building workflows for lawyers, building workflows for internal tool optimization and things like that.

**Ben Church:** know, so.

**Ben Church:** Yeah.

**Daniel Lopes:** And then an abstraction that I'm thinking that's very interesting is what dbt does.

**Daniel Lopes:** So dbt, you have a GitHub repo, and you can use it locally, and you can code with your VS code, whatever you want to use.

**Daniel Lopes:** But they also have dbt cloud that has the workspace environment that will almost be like a Git client that will pull from the same GitHub repo.

**Daniel Lopes:** Every change you're going to make creates a branch, and the cloud IDE just enriches the experience.

**Daniel Lopes:** So you have preview of the tables, you have the graph of all the dependency layers of the tables and all that.

**Daniel Lopes:** So it makes it much better to use the remote version than locally your VS code.

**Daniel Lopes:** So like I use dbt for my last two companies, and I pretty much now use the local editor for that, even though like I'm a programmer, you know, so.

**Ben Church:** Yeah.

**Ben Church:** Yeah, and very similar to, I'll drop one if you haven't seen mage.ai in the data space.

**Daniel Lopes:** I haven't used it.

**Ben Church:** I heard of it, but I haven't used it.

**Ben Church:** Code and then like the ID has got some great preview features.

**Ben Church:** So it's kind of that thing, like if the atom for these workflows remain code, what that means is your agent can intuitively understand it.

**Ben Church:** And then in there, we can layer in like your classic validation functions and preview functions and hooks and things like that to make the experience more robust or like get the LN to a correct answer quicker.

**Ben Church:** Right.

**Ben Church:** Okay.

**Daniel Lopes:** Does that all make sense?

**Ben Church:** Yeah, that one I'm sitting on because I'm like, my brain's going to, okay, but who is really the end customer at the content?

**Ben Church:** And yeah, how familiar would they be with a branching model?

**Ben Church:** My brain didn't go to make sense.

**Ben Church:** was starting to go to like, okay, what's the user going to be seeing in here?

**Ben Church:** And like, whatever they want.

**Ben Church:** So that's.

**Ben Church:** It tells me I'm like, either I'm like wildly off or like, understand it and I'm on to the next spot, but it's coming together.

**Ben Church:** My next phase is like, I want to understand all the product side of it.

**Ben Church:** So I'm to talk to some of the engineers, get a hold of some people on the client side.

**Ben Church:** Clint said I should go chat with his name, Jason Gong.

**Daniel Lopes:** Yep.

**Ben Church:** And just see how they're all being used today, how they stand up.

**Ben Church:** And then I want to get into some type of editing with this by end of day tomorrow, depending on how far into the context I go, where I feel the pull.

**Ben Church:** Clint was showing me he wants to do prompt previews in Flow and was getting analysis paralysis on like, what's the best way to really like hydrate that prompt and .

**Ben Church:** So I could take a stab at that.

**Ben Church:** And yeah, that's generally my process.

**Ben Church:** I want

**Ben Church:** Understand how these are used and like who are the people who use it and then start walking into it and see if can make some edits.

**Ben Church:** Yeah, that makes sense.

**Daniel Lopes:** Yeah, the users here, I think the way to think about it, it's almost like the way the company is structured.

**Daniel Lopes:** So we have the user of Flow and Flow Studio would be Kirkland and Markets.

**Daniel Lopes:** So if we ever launched that as like a product or a paid product or whatever or open source or whatever, you know, they would be the users.

**Daniel Lopes:** They would be the ones like, okay, I work for ClickUp or I work for GrowthX.

**Daniel Lopes:** I work for like different companies and they need to build all these AI things.

**Daniel Lopes:** And like my options are Aerox and Zapier and maybe in some cases would be like actually building a feature and I need to do like transcription or I need to do like some smart LLM-based feature.

**Daniel Lopes:** And our only option to have is LangChain and Master.

**Daniel Lopes:** So like that flow is essentially a mix of like growth engineer, sales engineer, like this new kind of LLM based engineering that's like starting to exist, LLM automations engineer, all the way to like hardcore engineering building features, you know, and that's the audience.

**Daniel Lopes:** And then we have, and maybe over time, the audience there will also be like Marcel and Jason.

**Daniel Lopes:** So that's like, we have this audience that's mixed, you know, where like you think of both works, both versus cursor, both you have people that are like Marcel and Jason, they can create apps in that thing.

**Daniel Lopes:** While cursor, they can start in both and they can pass it down to us to continue their work.

**Daniel Lopes:** So the way I'm thinking about the LLM workflows would be similar where you could have people like Philippe and Brad build features in a tool like Atlas could be users of that.

**Daniel Lopes:** And then they will start with the harder part.

**Daniel Lopes:** Or we could have somebody like...

**Daniel Lopes:** That's like just started as a programmer like a year ago, but did a bunch of stuff already with Zapier and things like that.

**Daniel Lopes:** And it wants to start doing like more advanced things.

**Daniel Lopes:** And then they eventually like they, that's why I think like GitHub example of DBT is so interesting because like it doesn't create like a toy.

**Daniel Lopes:** Like if it was essentially a toy, you know, and we tried to like make it more powerful and like our toy users could never really get used to using complex graphs.

**Daniel Lopes:** So we do the graphs the same way as air ops.

**Daniel Lopes:** never really shipped because like we exposed that to 10 million users on like a 1% became users of that.

**Daniel Lopes:** So get rid of it, you know?

**Daniel Lopes:** So you have this like jump that you can never cross.

**Ben Church:** So yeah.

**Ben Church:** Yeah.

**Ben Church:** Yeah, exactly.

**Ben Church:** I didn't get there.

**Ben Church:** Okay.

**Ben Church:** I realize I know you got to jump here the next call.

**Ben Church:** Yeah.

**Daniel Lopes:** I hope that was helpful.

**Daniel Lopes:** We should book more time for sure.

**Daniel Lopes:** Like at least next week.

**Ben Church:** Yeah.

**Daniel Lopes:** And we should probably try to meet them once.

**Daniel Lopes:** For at least the first month.

**Ben Church:** Yeah, I'll work to set that up.

**Ben Church:** I'm just going to stand in once a week.

**Ben Church:** And then, yeah, in terms of this, it seems like Foe might be a good spot for me.

**Ben Church:** One thing I'd highlight is I do like doing the front-end product stuff, too.

**Daniel Lopes:** So if you ever need hands in there, let me know.

**Ben Church:** And, yeah, man, I'll ping with any questions that only you can answer, but I'll try and stare at your inbox where I can.

**Daniel Lopes:** Nah, don't worry about it.

**Daniel Lopes:** I need to just make time for me to not be this busy with, like, IC work, and I should just be helping everybody.

**Daniel Lopes:** So that's my focus for next week once we are out of the woods.

**Ben Church:** Yeah, you had a big fire.

**Daniel Lopes:** It was understandable.

**Ben Church:** All right, Daniel.

**Ben Church:** This is awesome.

**Ben Church:** See you, man.

**Ben Church:** Thanks again, man.

**Daniel Lopes:** Appreciate it.

**Daniel Lopes:** happy to have you here.

**Daniel Lopes:** Me too, man.

**Daniel Lopes:** Me too.

**Daniel Lopes:** Take care.
