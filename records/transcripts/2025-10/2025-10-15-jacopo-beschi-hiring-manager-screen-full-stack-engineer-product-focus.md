# Jacopo Beschi -Hiring Manager Screen | Full Stack Engineer (Product focus)

<metadata>
date: 2025-10-15
time: 16:02 UTC
duration: 185 minutes
organizer: daniel@growthxlabs.com
participants: Daniel Lopes (GrowthX), Jacopo Beschi
fathom_recording_id: 94374308
fathom_url: https://fathom.video/calls/441179671
share_url: https://fathom.video/share/SD6Jnjzj3zDco4r1p3mP2eKt-UTQQ7sE
source: fathom
enriched_on: 2026-03-02 12:45 UTC
</metadata>

---

## Summary

Daniel Lopes walked Jacopo Beschi through GrowthX's technical architecture, products, and the full stack engineering opportunity, diving deep into the AI workflow framework built on Temporal that powers both Atlas (internal content creation) and CheckThat (AI visibility/competitor analysis). The team discussed the challenge of standardizing API client implementations across multiple Rails and React codebases, and Jacopo asked thoughtful questions about webhook reliability, error handling, and framework design patterns. GrowthX planned to send an offer within a day, with an ideal start date in early November following a few weeks of personal rest.

---

## Context

This was a hiring screen with Jacopo Beschi, a senior full stack engineer candidate, conducted by Daniel Lopes from GrowthX. Rather than a standard technical interview, Daniel opted for an exploratory working session where he could show Jacopo the actual architecture and codebase, then collaborate on a real challenge. The meeting lasted 3+ hours, reflecting Daniel's commitment to ensuring the candidate understood the depth and complexity of what the engineering team is building. GrowthX was actively recruiting for this role to support the CheckThat product launch and to backfill for another engineer (Jose) going on parental leave, while also having an opportunity to hire someone who could help standardize and improve their internal tooling and API client patterns—a known pain point across their codebase. Jacopo had recently left Basecamp and wanted to take a few weeks to recover before starting.

---

## Relevance

**To GrowthX Delivery:**
- Opportunity to hire senior engineer who can lead API client standardization across Atlas and CheckThat (currently multiple incompatible implementations—Jose's webhook-based approach in CheckThat vs. polling-based approaches in Atlas)
- Candidate demonstrated deep understanding of Temporal, Rails/React workflow patterns, webhook reliability challenges, and proposed concrete solutions (hybrid webhook + status check approach)
- Candidate has strong experience from Basecamp with async communication (musical second nature) and on-call rotation design patterns that emphasize developer accountability
- Critical need to reduce services team burnout by automating workflows; Atlas team facing imminent burnout risk without faster automation

**To CheckThat:**
- Critical hire for CheckThat product launch; team expects thousands of users in first month (competitors charge $1,000/month; GrowthX offering free product creates massive demand signal)
- Candidate asked pointed questions about webhook retry logic, request queuing at HTTP level, and hybrid polling approaches, suggesting he'll push for robustness in page scanning workflows (can process 100,000+ pages per client)
- Understanding of error handling patterns will be essential during chaotic launch period (first 2-3 weeks are typically messy; Jacopo witnessed this at Basecamp)

**To GrowthX Business Development:**
- Planned offer within one day; ideal start date early November (November 3-8 range, before Jose's November 15 Caesarean leave)
- Hiring at San Francisco-level salary with stock options; company break-even and exploring Series B ($30-40M raise under discussion with investors)
- Three major milestones planned for next 2-3 months: CheckThat launch, Atlas client accessibility, output framework open source—all will dramatically change investor narrative post-launch

---

## Overview

- growthx.ai has two main products: Atlas (internal content creation tool) and Check That (competitor analysis tool)
- Tech stack includes Rails, React, TypeScript, and a custom AI workflow framework
- Company is growing rapidly and looking to standardize processes and tooling
- Role would involve both product engineering and helping improve developer experience/tooling
- Flexible start date possible, with ideal timing around early November before another engineer goes on leave

---

## Key Topics

### Company Overview and Products

  - Two main products: Atlas (internal content tool) and Check That (competitor analysis)
  - Using Rails, React, TypeScript stack
  - Custom AI workflow framework built on Temporal
  - Growing rapidly, currently at break-even financially
  - Considering Series B funding to prepare for potential market changes

### Engineering Team Structure and Processes

  - Three main teams: AI framework, client-facing, and product
  - Using 4-week cycles with 2 week cooldowns for product work
  - Flexible PTO policy, aiming for at least 15 days taken per year
  - Async communication emphasized
  - On-call rotations still being formalized as team grows

### Potential Role and Responsibilities

  - Full stack engineering across Rails and React codebases
  - Help standardize API client usage across products
  - Review architecture decisions and large PRs
  - Potentially assist with AI framework development
  - Support Check That launch and backfill for engineer going on leave

### Development Practices and Tooling

  - Mac-based development environment
  - Mix of Docker and local setups, opportunity to improve onboarding
  - Using Linear for project management
  - Cloud Code for AI-assisted development
  - Render for hosting, may move to AWS in future

### Compensation and Benefits

  - Aiming for San Francisco-level salaries
  - Stock options offered
  - Flexible PTO policy
  - Potential for remote work

---

## Action Items

- growthx.ai to send offer, likely within next day
- Discuss potential start date, ideally early November
- Jacopo to consider length of break needed before starting
- Follow up on any remaining questions about role or company

---

## Transcript
**Jacopo Beschi:** Great.

**Jacopo Beschi:** You?

**Jacopo Beschi:** You are into traffic?

**Daniel Lopes:** This meeting is being recorded.

**Daniel Lopes:** Today I'm working from home.

**Daniel Lopes:** Today it's just like raining.

**Jacopo Beschi:** It's on here.

**Daniel Lopes:** Oh, nice.

**Daniel Lopes:** Yeah, it's like raining.

**Daniel Lopes:** Oh, wow.

**Jacopo Beschi:** Everything's good.

**Daniel Lopes:** Yeah, I live close to the city, but I live outside San Francisco.

**Daniel Lopes:** It's just like across the Golden Gate Bridge.

**Jacopo Beschi:** I don't know if you've been here before.

**Jacopo Beschi:** Never been to the West Coast ever.

**Jacopo Beschi:** Only to the East.

**Jacopo Beschi:** I've been to the East Coast and then to Miami and New Orleans.

**Jacopo Beschi:** I think that was it.

**Jacopo Beschi:** Yeah, for you, for the United States.

**Daniel Lopes:** We've got to get you here.

**Daniel Lopes:** San Francisco is a very pretty city, especially outside the city.

**Daniel Lopes:** But we need to get you here if you were to join us.

**Daniel Lopes:** Cool.

**Daniel Lopes:** They would be good.

**Daniel Lopes:** Sorry, I'm a couple of minutes late.

**Daniel Lopes:** I was just like for the stuff that I was talking to Tucker and like thinking about your background.

**Daniel Lopes:** So like the interview process that we have, it's not really set up for the new role that we're creating.

**Daniel Lopes:** So like I was still putting everything together and like thinking how we could do this.

**Daniel Lopes:** But for today, I was thinking like more, it would be cool to like kind of work together.

**Daniel Lopes:** So it's not a challenge or something that we've done with other people.

**Daniel Lopes:** But I have a couple of things in the product that I think it would be nice to like maybe rethink.

**Daniel Lopes:** And it would be great to take your, get your thoughts on this and like help me think about it.

**Daniel Lopes:** Sure, let's take a look.

**Daniel Lopes:** That makes sense.

**Daniel Lopes:** Let me make sure I have everything open here.

**Daniel Lopes:** I have so many.

**Daniel Lopes:** Tabs open.

**Daniel Lopes:** me close some of this.

**Daniel Lopes:** One sec.

**Daniel Lopes:** There we go.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Let me share my screen.

**Daniel Lopes:** And I can give you a quick context, quick tour of how everything works first, and then we can think about the challenge.

**Daniel Lopes:** So we have two different projects, two different, we essentially have three different Rails apps.

**Daniel Lopes:** This is our core one that we use that our editors and writers, the folks use every day.

**Daniel Lopes:** We have another place that we use to inspect the workflows that are running, but very similar to like a sidekick or solid mission control where you see everything that's happening.

**Daniel Lopes:** So this is a separate code base.

**Daniel Lopes:** But it's not related to Temporal or that's related to Temporal.

**Daniel Lopes:** This sits on top of Temporal.

**Daniel Lopes:** is an API, essentially a client for Temporal.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And then we have the project that Jose is working on.

**Daniel Lopes:** This is another one.

**Daniel Lopes:** So this is going to be a completely separate product.

**Daniel Lopes:** Okay.

**Daniel Lopes:** The thing that the first product, this one, Atlas, and check that have in common is that they all make a bunch of API calls to workflows.

**Daniel Lopes:** And those AI workflows are the things that uses the framework that we're creating and the same infrastructure.

**Daniel Lopes:** We will eventually turn that framework into something that you can essentially run very similar to like a Rails new and create a new project.

**Daniel Lopes:** You will be able to do like output space new and create a new project.

**Daniel Lopes:** And this thing has a way to generate workflows.

**Daniel Lopes:** And each workflow becomes an API endpoint.

**Daniel Lopes:** And you can start the workflows with an API call and workflow.

**Daniel Lopes:** can workflow.

**Daniel Lopes:** And start you And

**Daniel Lopes:** After that, have to monitor the status, and you have like, sometimes they will use webhooks, the workflow can call you back, or you can just call the API and see how the status is going.

**Daniel Lopes:** If it's working, if it's canceled, if it's still processing, if it's completed, so that there's a bunch of statuses.

**Daniel Lopes:** So, and just to show you how it works, I can create one workflow real quick here, and you're going to get a better idea.

**Daniel Lopes:** But, like, both of these products, like Check That and Atlas, they have like this API client inside of them that initiates workflows and make API calls to get responses.

**Daniel Lopes:** Today, the workflows are all in the same project.

**Daniel Lopes:** So there's this project in our code base called Flow, and it's a monolith with all of our workflows.

**Daniel Lopes:** So, like, I can show that real quick.

**Daniel Lopes:** So, this is the code base where we have a bunch of our workflows.

**Daniel Lopes:** And they're all inside of this packages, temporal, source, workflows, and then we have a bunch of workflows.

**Daniel Lopes:** Check that has a folder here with all the workflows that we need.

**Daniel Lopes:** And all the workflows are mostly for Atlas.

**Daniel Lopes:** And the way we, I can show you a little bit to explain some of those workflows, but every workflow you put in this folder, you put on the folder called workflows, they will be executable through an API call.

**Daniel Lopes:** And the API call is, I think it's workflow slash run, and then you pass the name of the workflow.

**Daniel Lopes:** And the name of the workflow is the function that defines the workflow.

**Daniel Lopes:** So, for example, in the case of check that, for example, we have a probing workflow that will make a bunch.

**Daniel Lopes:** of LLM calls to see which LLM call will surface different companies.

**Daniel Lopes:** So I can show you what that means in a bit.

**Daniel Lopes:** You don't have to worry too much about what it does, but it's essentially, this is the name of the workflow.

**Daniel Lopes:** So you would make like a post request with the params, would be like whatever you're going to pass to the function, and the name of the workflow.

**Daniel Lopes:** This will initiate the workflow, and then you can make a subsequent calls to know how the workflow is doing, or sometimes the workflow itself can send a webhook.

**Daniel Lopes:** So in the case of check that, for example, this is actually a project workflow that Jose created, and this will send a webhook back to the Rails app that he's doing, check that.

**Daniel Lopes:** And the send webhook code for this is, oh sorry, the send webhook code for this, just to give a little bit of the context there.

**Daniel Lopes:** But we're going to be just on the radio side, but just to show you what it does.

**Daniel Lopes:** So it has a query LLM function, has another function to analyze the mentions of companies and send a webhook.

**Daniel Lopes:** And just to explain what this means is that we have, the idea of this product here is that we're going to have a bunch of prompts.

**Daniel Lopes:** Like, for example, what's the best spend management tool?

**Daniel Lopes:** What is the best way to track your expenses?

**Daniel Lopes:** And this prompt, run them daily and see which components show up.

**Daniel Lopes:** So that's what that workflow does.

**Daniel Lopes:** So it's like receives the prompt, like best spend management app, for example.

**Daniel Lopes:** Runs it and runs it through like many different providers.

**Daniel Lopes:** So like ChatGPT, Claude, Gemini, perplexity, and then extract the components that are mentioned and send, analyze the sentiment.

**Daniel Lopes:** If they're being mentioned as good or bad, and send that back as a JSON to the Rails app.

**Daniel Lopes:** So that's what that workflow does.

**Daniel Lopes:** So we have dozens of workflows like this.

**Daniel Lopes:** And this is actually the running version of it.

**Daniel Lopes:** And workflows are essentially anything that you put in the folder workflows will show up here, and they are all triggered by API requests.

**Daniel Lopes:** And I can create one workflow real quick just for you to see.

**Daniel Lopes:** So we have a generator similar to Rails.

**Jacopo Beschi:** Sorry, just to understand the context a little bit more.

**Jacopo Beschi:** So basically, you have two apps that interact via API to basically, I'm not sure, but kind of a temporal API, is it?

**Jacopo Beschi:** Yeah, it's a...

**Jacopo Beschi:** run a workflow, and then the workflow will just connect with the AI provider, like ChatGPT or other provider, and then response back via webbook.

**Jacopo Beschi:** We

**Jacopo Beschi:** Information with the result, basically, is something like that, because I'm not totally fine with it properly, so just on a live level.

**Daniel Lopes:** That is perfectly summarized.

**Daniel Lopes:** And then we also have, so like we have two API endpoints.

**Daniel Lopes:** have one that starts a workflow, and that, if the workflow has a step that will send a web hook back, then your app is fine, you're going to get it.

**Daniel Lopes:** And you have another API endpoint where you can get the ID of the workflow that was returned from the one that starts.

**Daniel Lopes:** So the start one also sends you an ID of the workflow that was initiated.

**Daniel Lopes:** And then you can use that ID to query again for a status.

**Daniel Lopes:** So you can either do polling to check status, or you can implement inside of the workflow a web hook to your app.

**Daniel Lopes:** But, yeah, so like we don't have a standard way in the framework today to send web hooks.

**Daniel Lopes:** So Jose...

**Daniel Lopes:** I had to code that function to send the webhook back to check that.

**Daniel Lopes:** But that is one of the patterns that I think we should add to the framework, like an automatic way to get the responses as a webhook.

**Daniel Lopes:** But the thing that I want to show you is that we have these two different Rails apps, and Atlas has...

**Daniel Lopes:** So Jose implemented the way to initiate the workflows and receive the webhook on check that.

**Daniel Lopes:** Atlas has multiple areas where we use workflows, and some of the folks, are implemented in different ways.

**Daniel Lopes:** So we essentially have very, like, many different API clients to the same API that we own.

**Daniel Lopes:** And I'm thinking about, okay, this is the perfect situation for creating, seeing if we can extract a gem, or at least a lead that we can put in the lead folder from Rails, and we can use that.

**Daniel Lopes:** But then, like, over time, maybe we turn that into a nasty kit.

**Daniel Lopes:** And if we, once we make the framework open source, that could be the client SDK for Ruby, you know, to initiate workflows and listen to status and stuff like that.

**Daniel Lopes:** To show you how the framework works, I can do a quick generator one here, just for you to get more context about the thing.

**Daniel Lopes:** But the way, like, for example, imagine that this project that I have here, initialized, would have been created by, we're going to rename the whole thing.

**Daniel Lopes:** Like right now we use this code name called Flow.

**Daniel Lopes:** So everything that you see as Flow is the name of the, is the workflow, it's the framework.

**Daniel Lopes:** But imagine that this was created by the project generator and you have a scaffolded structure for how to organize your workflows.

**Daniel Lopes:** And in this case, like, this is the one that we have with all of our workflows, but if we're starting new, imagine that the folder would be empty and you would have a folder called workflows and you would.

**Daniel Lopes:** I would like something like output.run, and that would initiate the server, and then you can trigger API calls against your workflows.

**Daniel Lopes:** So that's how it's going to work.

**Daniel Lopes:** That's the version that the guys are working on right now that we think we're going to be ready by end of this month.

**Daniel Lopes:** The version we have today working, I would do, I initiated here, let me start the server.

**Daniel Lopes:** So this is just initiating the Temporal, initiating the API as well.

**Daniel Lopes:** So the API, we wrote this API, so it sits on top of the Temporal background job.

**Daniel Lopes:** Temporal also has a user interface as well.

**Daniel Lopes:** So it's kind of confusing, so we build our own that's simpler for less technical folks to understand.

**Daniel Lopes:** So that's that interface that I showed you that has the studio with the statuses and everything.

**Daniel Lopes:** So that's running.

**Daniel Lopes:** The next thing I would do here, for example, if I want to create a new workflow,

**Daniel Lopes:** So just from this, I could trigger post requests to the API, and I think it's localhost2000, yeah, this one, localhost2000, and I would be able to initiate workflows, I would be able to monitor them.

**Daniel Lopes:** If I wanted to create a new workflow, so for example, let's say I want to create one that does, let me create a new fire here, and then I can go step by step.

**Daniel Lopes:** Let me delete this.

**Daniel Lopes:** I was actually just running it before to see if it was going to do something, but imagine that we wanted to create, like, forget this part here, we'll get to that there.

**Daniel Lopes:** But imagine that we wanted to create an article processing pipeline, that the idea here would be that you would receive an existing article, for example, we have, like, some, let's say that's our...

**Daniel Lopes:** Technical, blog, let's say we have this, can pick any of the, let's say this, this one might be good, this one, yeah.

**Daniel Lopes:** So let's say I have this article, I want to pass this article to an AI workflow, and I wanted to create a TLDR to put at the top of the article, maybe I also want to add an FAQ to put it to the bottom, and I also want to translate it to like Spanish or Portuguese or Italian, whatever we choose.

**Daniel Lopes:** And so the way we would execute that, usually you would have to scrape the article first, convert it to mark it down, and then pass the article to an LLM to first do the, probably would break down into multiple LLM calls, but it does better if you decompose the work.

**Daniel Lopes:** So we would probably have a step called create a TLDR with like some instructions for how the TLDR should look like.

**Daniel Lopes:** So maybe with like 25 bullets.

**Daniel Lopes:** And how you format that.

**Daniel Lopes:** then have maybe another step that would be like create an FAQ.

**Daniel Lopes:** like understand the article, see what people usually have frequently asked questions about this topic.

**Daniel Lopes:** Come up with that, invent that yourself.

**Daniel Lopes:** Could even be like research the internet and see what people are searching about the things.

**Daniel Lopes:** And create an FAQ that we're going to attach to the bottom.

**Daniel Lopes:** So that would be a second step.

**Daniel Lopes:** Those two steps actually could be run in parallel because they're not dependent on each other.

**Daniel Lopes:** And then the third one could be like translate the full result that has the TLDR and the FAQ and the full article to the language of choice.

**Daniel Lopes:** So this would probably be a three-step workflow.

**Daniel Lopes:** You might even like want to do like a fourth one that would be just to assemble everything together and put in a nice JSON and return.

**Daniel Lopes:** Or so let's say like four steps.

**Daniel Lopes:** And...

**Daniel Lopes:** And the way we usually write this is that we have steps, our functions, and they're almost like independent functions.

**Daniel Lopes:** And then we have the workflow is the orchestration, how the functions are triggered and all that.

**Daniel Lopes:** So that's just the usual anatomy of a workflow.

**Daniel Lopes:** And the steps can be AI LLM calls, can be other API calls, can be anything that evolves I.O.

**Daniel Lopes:** is a step in our framework.

**Daniel Lopes:** And so I have here this plan.

**Daniel Lopes:** So our framework takes a plan file, and the plan file is a natural language.

**Daniel Lopes:** So you can define, like, for example, if you were creating this workflow, let's say like this project involves building an article processing pipeline that performs three key operations on a web article.

**Daniel Lopes:** And let's say the operations are, it's just like repeating what I just talked about.

**Daniel Lopes:** So these are the tests that we expect already, this is actually like one of our interviews.

**Daniel Lopes:** So we ask folks to do that in TypeScript, and then I show them how we do it internally.

**Daniel Lopes:** So that's why I have some language here that your application is expected to do that.

**Daniel Lopes:** But I'm just going to remove that.

**Daniel Lopes:** Steps, rename this to step.

**Daniel Lopes:** So fetch the article and parse it, receive a URL as an argument and pass parse the article, we recommend using GINA Reader API.

**Daniel Lopes:** So that's something that we already have in our system.

**Daniel Lopes:** GINA is an API for scraping.

**Jacopo Beschi:** And converts to Markdown.

**Jacopo Beschi:** Yeah, converts to Markdown, yeah.

**Daniel Lopes:** Okay.

**Daniel Lopes:** So like, for example, GINA, if I had our GINA.ai here, it will convert this article to Markdown.

**Daniel Lopes:** Our GINA.ai...

**Daniel Lopes:** Are they down now?

**Daniel Lopes:** now?

**Daniel Lopes:** they down

**Jacopo Beschi:** The timeline was too small, think, like, less than five seconds, I didn't think it was something else.

**Jacopo Beschi:** Let's see.

**Daniel Lopes:** Maybe our Cloudflare caught it.

**Daniel Lopes:** Ah, I canceled it.

**Daniel Lopes:** It's probably going to work fine.

**Daniel Lopes:** Let's see, I had actually this one from, yeah, so this one is a post for Jason, for example.

**Daniel Lopes:** Let's see.

**Daniel Lopes:** That was the original post.

**Jacopo Beschi:** Okay.

**Daniel Lopes:** And then if you just append Gina, it converts to Markdown.

**Daniel Lopes:** I suppose it was cached, so it works.

**Daniel Lopes:** Yeah, yeah, exactly.

**Jacopo Beschi:** Okay, now our hours work as well.

**Jacopo Beschi:** So I think ours is longer, so that's why I was saying that.

**Daniel Lopes:** Okay, yeah.

**Daniel Lopes:** Yeah, so, but it's almost free and it's super volume.

**Daniel Lopes:** It's pretty nice.

**Daniel Lopes:** So we use it for many things.

**Daniel Lopes:** So, yeah, step one.

**Daniel Lopes:** Be like, call Jenna, get that markdown back, step two, add a brief to the top, step three, Spanish translation, step four, like this is actually, I forgot about that.

**Daniel Lopes:** So that's actually another one that we usually have in the interview process with the other folks, is this.

**Daniel Lopes:** But I can just like run this and see what happens.

**Daniel Lopes:** Usually this is enough to generate the workflow that works.

**Daniel Lopes:** And it can be like as vague, like sometimes pretty vague and will do a pretty good job.

**Daniel Lopes:** So we just like save this in a workflow blend folder.

**Daniel Lopes:** So in the project here, we have, let me go back to workflow, workflow, we have workflow blends.

**Daniel Lopes:** I'm going to create one called particle MD.

**Daniel Lopes:** And then I run a scaffold like command in the terminal.

**Daniel Lopes:** So like it would be, let me see if I can get this.

**Daniel Lopes:** Right one here, I think I, yep, I have the, this is the right one.

**Daniel Lopes:** So let's say you do like, yarn run, actually, yarn run, OCLI generate, and then that will ask for the path where I wanna put this workflow.

**Daniel Lopes:** So I'm just gonna call this article demo, and then it asks me to paste, I can just generate an empty workflow, like kind of hello world with like nothing, where I can paste a plan here and it'll pop up a VI where you can paste the plan, or I can use a path to the plans, and I can, I think I'm gonna use the path to the plan to just save the thing.

**Daniel Lopes:** So we have workflow plans, and I think it was this one.

**Daniel Lopes:** I'm just moving things around here.

**Daniel Lopes:** So many, you know, pop-ups, so let's see, this is the one, yep, this is the one, so I'm gonna grab the path, I'm not sure, the right path, and use a plan file, and then I paste the file path, and then description, just to test, and then this will trigger a bunch of LLM calls, we'll do like normal code generation, static code generation, and then we'll the result of the code that was generated, like empty boilerplate code, so like Rails, for example, you'll generate like a scale code that would be like an empty boilerplate for like, maybe a model and a controller or something like that, but we do the same, but then we pick that result, and make a call to like Claude, and perform those requirements, so it starts to change the code to perform those requirements, and we have quite a few the that have

**Daniel Lopes:** Structions that will most of the time get really close to like what you wanted because it's kind of like self-contained.

**Daniel Lopes:** just like generating the workflow, now it's generating the documentation for the workflow as well.

**Daniel Lopes:** So we have like generates a readme, generates a bunch of other things, generates a flow diagram.

**Daniel Lopes:** So that's the same stuff.

**Daniel Lopes:** And then also updates the routes file, like an entry point kind of file.

**Daniel Lopes:** So it is going to generate Rails or, sorry, Ruby or TypeScript?

**Daniel Lopes:** TypeScript.

**Daniel Lopes:** Okay.

**Jacopo Beschi:** TypeScript, yeah.

**Daniel Lopes:** Okay.

**Daniel Lopes:** So this is all in the TypeScript code base where you create all these workflows and they get exposed as API endpoints.

**Daniel Lopes:** And that's what the Rails apps are consuming.

**Jacopo Beschi:** Okay, got you.

**Daniel Lopes:** So like this one is finishing.

**Daniel Lopes:** So if I get pushed to this, it would be available as an API, to the API to...

**Daniel Lopes:** Run it and get the article, new article back.

**Daniel Lopes:** So let's see if it worked.

**Daniel Lopes:** Yeah, so let just close the server.

**Daniel Lopes:** That's the only thing that we don't support yet is just hot reload when a new workflow is added.

**Daniel Lopes:** But let's see if this worked.

**Daniel Lopes:** So I have here, so this was the code base with all the workflows.

**Daniel Lopes:** So it updated this entry point here and added, this is from before, added this new one here, article demo.

**Daniel Lopes:** And then if I open the workflow, you can see on the left side here that we have a folder that has activities, prompts, types, workflow, a spec file, and documentation.

**Daniel Lopes:** This documentation is for your inspector user interface.

**Daniel Lopes:** It has a bunch of vlogs, this is something that I actually like, the guy that added recently that I don't really like.

**Jacopo Beschi:** But...

**Daniel Lopes:** So what we have now is a workflow that will just validate the input and then fetch the article, generate the summary to put at the top, convert to Spanish, because that's what I had on my instructions, and do some fact-checking as well.

**Daniel Lopes:** And fact-checking will be just extracted the potential claims and stuff like that.

**Daniel Lopes:** And I don't think this one performs the fact-checking, but let's see.

**Daniel Lopes:** And then we have the activities.

**Daniel Lopes:** So all of those things are functions.

**Jacopo Beschi:** The activities are implementation, then.

**Jacopo Beschi:** Yeah.

**Daniel Lopes:** So if I open the activities, we have all these little functions.

**Daniel Lopes:** the fetch article one, I already saw that we support Gina as one of our API clients.

**Daniel Lopes:** So use that and also use the write scraping function.

**Daniel Lopes:** This is actually not necessarily something that the guy has added recently.

**Daniel Lopes:** That's one thing that we're doing.

**Daniel Lopes:** We're going to isolate the framework a little more, so it's harder to change.

**Daniel Lopes:** So

**Daniel Lopes:** And without reviews, like today the guys are changing too fast, but this is not necessary because Temporo can handle all the errors by itself.

**Jacopo Beschi:** How does it handle error, like automatically, without knowing what to do with depending on the error?

**Daniel Lopes:** Is it like generic retries?

**Daniel Lopes:** Yeah, so it does that at the workflow level.

**Daniel Lopes:** So like if I go back to the workflow, it has a catch here, and handle workflow error has some automatically detection depending on the type of error.

**Daniel Lopes:** So the API clients will raise an API error.

**Daniel Lopes:** So like that GINA client internally will raise an API error.

**Daniel Lopes:** So this will know how to handle that.

**Daniel Lopes:** And they also have a bunch of predefined settings for the type of error.

**Daniel Lopes:** In this case, this one has just a default backup path, but the more we usually would have something like this also doesn't.

**Daniel Lopes:** Let me show you like a harder one, search supervisor, then you can do all the settings for start to close timeout, initial interval, oh, sorry, initial interval, maximum interval, backoff coefficient, how many times you can retry, and what is known retryable.

**Daniel Lopes:** So this is like, you can pass that in the beginning of any workflow.

**Jacopo Beschi:** So you can use exponential retries, or you can use also linear if you prefer.

**Jacopo Beschi:** Yeah, like, you know, it depends.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Yeah, so that is all baked into the thing.

**Daniel Lopes:** you don't pass anything, you're just going to do the traditional simulation.

**Daniel Lopes:** Okay.

**Daniel Lopes:** So this is the output.

**Daniel Lopes:** So like we have, let me just read all the slots.

**Daniel Lopes:** So we have linear for us to see.

**Daniel Lopes:** And this, so first one, call to GINA.

**Daniel Lopes:** Second one, call to OpenAI.

**Daniel Lopes:** We support OpenAI.

**Daniel Lopes:** OpenAI.

**Daniel Lopes:** We

**Daniel Lopes:** iCloud, Gemini, everything essentially, make a call to GPT, using the OpenAI chat service, return things as a JSON, this must create the types as well, with what we expect, and I'll show you that in a bit, and create the prompts as well, so the prompts are getting imported here at the top, from the prompts file, the types are getting imported from the types file, so we have, create this, one, two, three, four, core files, it's activities, prompts, types, and workflow, translation, same thing, so it's calling OpenAI, fact checking is also calling OpenAI, so it's just used OpenAI for everything, this, I would probably have put in a separate file, so the schema, usually it's a good idea to keep it in a separate file, so we usually put that in types, so that's something that the ELLM didn't, didn't do a good job, so it usually, used to do a good job, but we've been changing them.

**Jacopo Beschi:** Sorry, have a question, if you don't mind.

**Jacopo Beschi:** How does the framework, I mean, maybe it's not the framework, maybe it's just AI that decides it, but anyways, how does it decide whether to use AI to do something or just implement it straight away?

**Jacopo Beschi:** Like if it's something that you don't need AI to do it, like how does it decide that?

**Jacopo Beschi:** Because if you need to start something, you don't need to do it via AI, right?

**Daniel Lopes:** Yeah, you just need to like, we could have, like sometimes you're going to have things that you're just going to assemble the results or do like helper functions and stuff like that.

**Daniel Lopes:** So we usually would have, this one is, it's explicitly mentioned in OpenAI, translating it also knows.

**Daniel Lopes:** So it is, the framework is biased towards AI workflows.

**Daniel Lopes:** So if you explicitly say, I want, this can be just a...

**Daniel Lopes:** If you don't need to use AI for that, it would try to hold an if, else, or split and things like that.

**Daniel Lopes:** you can't do it, but things like it will know automatically based on how the prompts are set that if it's translation, you probably should use an LLM.

**Daniel Lopes:** If it's a simple math operation, it wouldn't be used.

**Daniel Lopes:** So it has a bit of ability to find the right thing.

**Daniel Lopes:** It has a bunch of examples as well in the prompt.

**Daniel Lopes:** So it's also pulling from the examples.

**Daniel Lopes:** So like in this case, it probably works.

**Daniel Lopes:** I'm seeing some type in the linter here, but it's just because the TypeScript isn't restored.

**Daniel Lopes:** But if I just run this, let's see if it shows up on my local version of the inspector.

**Daniel Lopes:** This is my local inspector, I can come up here, and we have the new workflow here at the top.

**Daniel Lopes:** I think this is the one, maybe it's this one, I think it's this one, I just used the same name twice.

**Daniel Lopes:** Yeah, fetch the work article, generate summary, translate Spanish, extract, fact-checking.

**Daniel Lopes:** So this was generated as part of the scaffolding process, the flow diagram as well.

**Daniel Lopes:** The input is the URL, you can see the activities, and you can see the prompts here as well.

**Daniel Lopes:** So there's another thing I forgot to show you.

**Daniel Lopes:** Prompts are also here, prompts are defined as arrays like this.

**Daniel Lopes:** We're changing this to be almost like views with like YAML, with a front matter on top, and then the text on there, so the new version will be slightly different.

**Daniel Lopes:** Those prompts are generated.

**Daniel Lopes:** And that's something that we would spend a ton of time is actually like iterating all the prompts manually, and I can run the workflow from here.

**Daniel Lopes:** So let's say if it worked one shot, then let's grab this one, and let's run this and see what happened.

**Daniel Lopes:** So this will make an API call to start the workflow.

**Daniel Lopes:** Failed.

**Daniel Lopes:** Let's see why it failed.

**Daniel Lopes:** Content found with URL.

**Daniel Lopes:** I think I have something on that.

**Daniel Lopes:** I think we have Cloudflare really blocking most of the calls.

**Daniel Lopes:** Let me try.

**Daniel Lopes:** That's why it failed on the, try this one for Jason because I know that.

**Jacopo Beschi:** Maybe some security filter on Cloudflare.

**Jacopo Beschi:** It's really annoying.

**Jacopo Beschi:** Like I remember having a lot of fish with that in base camp, like people posting code.

**Jacopo Beschi:** InBaseCamp document, and then weren't able to upload that because Cloudflash sees the code and is like, no, no, no, don't do that.

**Daniel Lopes:** Yeah, anyway, for some reason, I think my gene is not set up locally.

**Daniel Lopes:** Yeah, it's crashing locally.

**Daniel Lopes:** Anyway, this is like, I could massage it and it could work, but I don't want to take too much of our time.

**Daniel Lopes:** I just wanted to show, like, usually, so it would probably be another step to just, like, make this work.

**Daniel Lopes:** Or the whole thing, it's also, like, for example, the workflow to make to fix this would be usually inside Cloudcode.

**Daniel Lopes:** So we have quite a bit of infrastructure for how Clouds should interact with our framework.

**Daniel Lopes:** So we have a bunch of sub-agents for prompt engineering, for workflow building, for workflow debugging.

**Daniel Lopes:** We have special commands to create the workflow, to plan, to validate.

**Daniel Lopes:** They, so, Clouds, code.

**Daniel Lopes:** It has a bunch of instructions for how our things work.

**Daniel Lopes:** So with that bug that we had, I could just paste it here, and it usually will do the work to know which files to look for.

**Jacopo Beschi:** So it's like looking at the...

**Daniel Lopes:** This is very powerful.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** I mean, you just say, okay, it is not working, fix that.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Oh, yeah.

**Jacopo Beschi:** That's it.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Maybe you edited it.

**Daniel Lopes:** I think I messed it up when we were like...

**Daniel Lopes:** maybe.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Let's see.

**Daniel Lopes:** I think that's it, actually.

**Daniel Lopes:** And then that was just triggered again.

**Daniel Lopes:** Executions.

**Daniel Lopes:** Run.

**Daniel Lopes:** Load last run.

**Jacopo Beschi:** Okay.

**Daniel Lopes:** Nice.

**Daniel Lopes:** Cute.

**Jacopo Beschi:** Now it's running.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** I think think now now now it it it is.

**Daniel Lopes:** Thank

**Daniel Lopes:** So this is the, our friendly user interface.

**Daniel Lopes:** And then you can also pop open, yeah, let's see.

**Daniel Lopes:** I think I might not even have the API key on my computer for Gina, that might be the reason.

**Daniel Lopes:** Anyway, usually this thing would work.

**Daniel Lopes:** So we have like dozens of workflows like this, like all of our AI features go through this framework, through the code base, and that's how we do any LLM calls.

**Daniel Lopes:** We don't have LLM calls in the Rails apps, for example.

**Daniel Lopes:** So they all go through here because we have all this info for like how you manage your problems, how you manage the API handling, how you do the backups and all that kind of stuff.

**Daniel Lopes:** And we are, we're building new things of like, also like everything that we do, we, we get.

**Daniel Lopes:** things of we're building building we're we're we're

**Daniel Lopes:** In tracing on how the LLM did, like how much it cost, we get like the, how many tokens were used automatically as part of the, just calling the LLM cause from that, from our framework, we get, we get all the instrumentation and all the tracing there.

**Daniel Lopes:** So, for example, let's see, somebody is running this workflow here called Content Editorial SEO MetaTags Workflow.

**Daniel Lopes:** It costs three cents, you take in 10,000 tokens and you get 78 tokens out.

**Daniel Lopes:** The response was this.

**Daniel Lopes:** So you get all of this visibility automatically by just using the framework.

**Daniel Lopes:** And so like all the things that are LLM based or even like any API calls we do, we actually route through the same system.

**Daniel Lopes:** So just to give you a little bit more.

**Jacopo Beschi:** So the system also control, like, excessive use of token or issues like that?

**Jacopo Beschi:** Because maybe you trigger something that by mistake and it's going to use too many tokens and it's going to be too expensive.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** So, like, cost tracking, then we monitor in length use, which is the separate tool.

**Daniel Lopes:** It's like a datadog or sentry.

**Jacopo Beschi:** Okay, cool.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah, so, like, another thing we have.

**Daniel Lopes:** So, like, all the things that I, AI-based, any of our systems are routed through that, to this API that I'm talking about.

**Daniel Lopes:** And so, like, in the case of, like, let's say we're onboarding a new client, I would come here and, for example, let's say, I'm just going to grab this, just top of mine.

**Daniel Lopes:** So, let's say if they were to join us as a client, we would paste it here, create a workspace.

**Daniel Lopes:** Let's see, I think it's, I don't know if I can.

**Daniel Lopes:** Okay, that's a test, right, I guess, what is that, 37, no, and I create a workspace, let's call this general, and I can open their workspace, and one thing that we usually do is create a bunch of documents about the client, so it'd be like, I need to research what this company does first, and then after that, I need to research what would be their personas, if we are writing for them, what would be the products that they offer, and what is the writing guidelines that they usually write their content, and for that, we have a workflow that does the company research, for example, so this will trigger an API call to research providers, so the research provider we support a bunch, can be like perplexity, can be a few other that's like more advanced, so there's the one called XAI, that's the one that we usually use for this here, so if I click on this button,

**Daniel Lopes:** It would just take the company name, take the company website by default.

**Daniel Lopes:** If I don't provide, I was just going to paste it again.

**Daniel Lopes:** And this will trigger an API call to the flow framework and we initiate that workflow.

**Daniel Lopes:** So this is running a workflow now.

**Daniel Lopes:** So if I hover over, it's just like polling.

**Daniel Lopes:** So it's just initiated the workflow.

**Daniel Lopes:** And now it's like every five seconds, checking if it changed.

**Daniel Lopes:** Yeah, so it's running a polling here.

**Daniel Lopes:** And then if I open this, you can see here that this is the workflow that was initiated.

**Daniel Lopes:** So Atlas Artifacts Scaffold Company Research Workflow.

**Daniel Lopes:** So this, if I pop open the temporal, this one has a bunch of, this workflow is a bit more complicated.

**Daniel Lopes:** So it has a bunch of sub-workflows.

**Daniel Lopes:** So it's initiating a research agent here that has, comes up with a plan.

**Daniel Lopes:** Let me just show you from here, it's actually pretty easy to read from here.

**Daniel Lopes:** So this is the research.

**Daniel Lopes:** Fathom that took in, took in this as an input, that's just a string input, let me show you, so this is the input, the JSON that was sent from the Rails app, it's passing the research tool and that kind of stuff, and then the first step we would do is come up with a plan, so what are the main products and services, how does the solution work, and then what are the customers, main pain points, so it comes up with this plan, and now it's performing this plan in parallel, running multiple researches at the same time, and then we'll like, analyze, synthesize, and create a document, so that's like, one of the AI features we have here, and we have a bunch of those, so we have stuff like this for generating these artifacts, let me show you one that's already created, so in the case of Lovable, for example.

**Daniel Lopes:** Lovable.

**Daniel Lopes:** Lovable.

**Daniel Lopes:** So company research was, this is the result of that workflow running.

**Daniel Lopes:** So it ran the research and got their main products, their solution, all that stuff.

**Daniel Lopes:** So answer everything and has a little bit of a confidence score as well.

**Daniel Lopes:** So the person can come here and remove this stuff that has low confidence or fact check manually.

**Daniel Lopes:** Came up.

**Daniel Lopes:** So this is the issue.

**Daniel Lopes:** then you would come here and click on this.

**Daniel Lopes:** That would create another workflow that would perform, that would create this, this, this, this, and this.

**Jacopo Beschi:** And these are stored in the Rails app now.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And so the Rails app initiates the workflow on that API, waits for the response.

**Daniel Lopes:** When you get the response, you save as a normal model in the Rails app.

**Daniel Lopes:** So that's one example of like the workflows that we use.

**Daniel Lopes:** And like we're essentially like more and more of our products are becoming.

**Daniel Lopes:** LLM-based features.

**Daniel Lopes:** So if you have analytics, for example, we put on top of the analytics, hey, here's what we're noticing.

**Daniel Lopes:** Or here's some anomalies we noticed.

**Daniel Lopes:** So you can offload a lot of the reasoning and things like that, like manual labor, to the LLM hub.

**Daniel Lopes:** And you can build all these interesting features that would be hard to do before.

**Daniel Lopes:** And so the thing that I was saying is the challenge that we have today is that we have no standard for how to consume this API.

**Daniel Lopes:** And this API is usually like, it will take minutes to run away flow.

**Daniel Lopes:** So this one that we triggered before, it's still running.

**Daniel Lopes:** So it's going to probably take 10 minutes to complete this one.

**Daniel Lopes:** Because it's going to run 20 different questions.

**Daniel Lopes:** So it's performing all the questions here.

**Daniel Lopes:** So it completed like a bunch.

**Daniel Lopes:** Now it's completing the last one.

**Daniel Lopes:** But it took four minutes already.

**Daniel Lopes:** It's very common to have sometimes take an hour, like something to take an

**Daniel Lopes:** So if you're scripting an entire website, that's another thing we do, we often script an entire website from the clients, get all their pages stored in our database, and analyze each page.

**Daniel Lopes:** That might take a full hour, if you have like a client that is larger.

**Daniel Lopes:** So, and that's all going through the same thing, and everybody's like using the same API client, and I'm trying to think if we should probably normalize the API client on the Rails side, you know.

**Daniel Lopes:** So, does that make sense?

**Daniel Lopes:** In general, like a high level?

**Jacopo Beschi:** Yeah, yeah, for sure.

**Jacopo Beschi:** Okay.

**Daniel Lopes:** Yeah, so the thing that I was thinking is, I collected a bunch of the code base for how we do these things.

**Daniel Lopes:** So, let me show you real quick here, and then I give you, I send you the folder, and then I give you time to retune and think about, and I can turn off my camera and all that, but.

**Daniel Lopes:** Just to go here to go Fathom, let me open this in my editor, and I can walk you through everything.

**Daniel Lopes:** This is, I don't know if you can see that.

**Jacopo Beschi:** Yes, yes, I can see it.

**Daniel Lopes:** Yeah, so I created this folder that has the two projects that we have, Atlas and CheckDat.

**Daniel Lopes:** Atlas is the one that we're using, CheckDat is the one that does the probing, the analytics.

**Daniel Lopes:** And for CheckDat, there's a little readme here with just the combination of everything.

**Daniel Lopes:** So a flow client is the main API client.

**Daniel Lopes:** There's base client.

**Daniel Lopes:** There's a, and then...

**Daniel Lopes:** The place is where we call the API client, I also put it there.

**Daniel Lopes:** And Jose built a webhooks, a general purpose webhooks receiver, and it stores in the database, so I also included that.

**Daniel Lopes:** And there's a special process here for the Flow API, for the Flow webhooks.

**Daniel Lopes:** And he has some tests here as well.

**Daniel Lopes:** So this is Jose's take on the client.

**Daniel Lopes:** And then we have some more, like just describing a little bit of this code.

**Daniel Lopes:** This was the AI generator, so this is all the code in one file, so you can just skim through and look.

**Daniel Lopes:** Or if you prefer to look at the real files, they're all here.

**Daniel Lopes:** So let's say, for example, if you wanted to look at the routes.

**Jacopo Beschi:** But does Flow S, does Temporal always reply?

**Jacopo Beschi:** I mean, if you have a webhook implementation.

**Jacopo Beschi:** Can you ensure that temporal rules reply with the web code is like?

**Daniel Lopes:** No.

**Daniel Lopes:** I don't think so.

**Daniel Lopes:** It could fail.

**Daniel Lopes:** So it might be just on the waiting forever state, you know?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** I don't know if we're covering that.

**Jacopo Beschi:** It's like Stripe, you know, if you have a very integrated with Stripe, you have the web, and then you can also, like, ask proactively.

**Jacopo Beschi:** So you could end-end for, like, a developer dashboard and error listing for, like, webhooks error so you can monitor because it's going to happen that you're not going to receive the webhook for multiple reasons.

**Daniel Lopes:** can even be just a network issue.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** But maybe it's just on temporal also.

**Jacopo Beschi:** So, yeah.

**Jacopo Beschi:** I was wondering about implementation, like, if you maybe should use an hybrid approach or something else just to make sure that you aren't stuck.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** I think we would be able to.

**Daniel Lopes:** You could, like, I think the same status API can be used to proactively reach out if it's taking too long.

**Daniel Lopes:** But anyway, this is the code base for check that.

**Daniel Lopes:** This is the code base for check that.

**Daniel Lopes:** This is the API client.

**Daniel Lopes:** Flow client, application client, has probing that executes this workflow.

**Daniel Lopes:** There's another one that executes another workflow.

**Daniel Lopes:** Flow, so this is inherited from this application client, pretty simple, basic one.

**Daniel Lopes:** And then we have a bunch of things here.

**Daniel Lopes:** And I'll send that to you as a zip file.

**Daniel Lopes:** And then we also have the Atlas one.

**Daniel Lopes:** This is the artifacts feature that I showing you that has the research and the content suite.

**Daniel Lopes:** And this is, has the front end all the way from like the, the mode.

**Daniel Lopes:** Oh, that little modal that when I clicked on the research button that showed that little form.

**Daniel Lopes:** So this is the modal that shows that.

**Daniel Lopes:** That triggers a post request to the Rails backend.

**Daniel Lopes:** There's a backend here.

**Daniel Lopes:** The backend will have a controller.

**Daniel Lopes:** So receives the form.

**Daniel Lopes:** So this is the modal rendering.

**Daniel Lopes:** This is the starting.

**Daniel Lopes:** So it receives the modal post.

**Daniel Lopes:** And started the job.

**Daniel Lopes:** And then initiates the job to this one.

**Daniel Lopes:** So that one will consume this workflow client.

**Daniel Lopes:** So different kind of client here now.

**Daniel Lopes:** The client is in here.

**Daniel Lopes:** And we have a workflow client in here.

**Daniel Lopes:** I know this is like an insane amount of stuff to take in in just one hour.

**Daniel Lopes:** But maybe we can just...

**Daniel Lopes:** I can send this to you.

**Daniel Lopes:** Like you spend like 10...

**Daniel Lopes:** To 15 minutes, like, reading through everything, and then we can spend, like, 20, 30 minutes just, like, brainstorming how we could build this potential general API client that we can use for both code base.

**Jacopo Beschi:** Does that make sense?

**Jacopo Beschi:** Does that work?

**Jacopo Beschi:** Yes, yes, yes.

**Daniel Lopes:** Cool.

**Daniel Lopes:** Let me share this.

**Jacopo Beschi:** So I have this zipped here.

**Daniel Lopes:** Okay.

**Daniel Lopes:** I'll share this with you.

**Daniel Lopes:** I'm going access the link, edit, copy, or post in the chat.

**Daniel Lopes:** Let me know if you can access the chat.

**Daniel Lopes:** I'll be here, and I can...

**Jacopo Beschi:** Okay, I can see it.

**Daniel Lopes:** Let's see if you can open that, and if you can download the file.

**Jacopo Beschi:** Yes.

**Daniel Lopes:** We're able to unzip the file, did it work the...

**Jacopo Beschi:** Yes, I can.

**Jacopo Beschi:** Yes.

**Jacopo Beschi:** Yeah, I'm okay.

**Jacopo Beschi:** I can see that.

**Jacopo Beschi:** Yes, I downloaded it and opened it.

**Jacopo Beschi:** Yeah.

**Daniel Lopes:** Okay, cool.

**Daniel Lopes:** All right.

**Daniel Lopes:** So I'll give you time to read that and then you can go through it.

**Daniel Lopes:** Take as much time as you want.

**Daniel Lopes:** I'll turn off my camera and I'll turn off my microphone too.

**Daniel Lopes:** You can turn off yours if you want, but I will be here.

**Daniel Lopes:** And if you need help, I'll jump back in the chat.

**Daniel Lopes:** But maybe we check back in in like 15 minutes.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Sure.

**Jacopo Beschi:** All right.

**Jacopo Beschi:** I'm gonna add a timer.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Thanks.

**Jacopo Beschi:** Thanks, The end.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Thanks.

**Jacopo Beschi:** There

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Thank you.

**Jacopo Beschi:** Thank you.

**Jacopo Beschi:** Okay, maybe I can share my screen and we go together through the two implementation first, because I'm not sure I understood everything.

**Daniel Lopes:** Yeah, sounds good.

**Daniel Lopes:** Yeah, sounds good.

**Daniel Lopes:** I haven't actually, like, read all the different implementations of everything yet, so that's, I was, this was an interesting exercise for me as well as just, like, pulling together all the different ways folks are doing it.

**Daniel Lopes:** It's like, okay.

**Daniel Lopes:** It's like a little more than I expected.

**Daniel Lopes:** God damn it.

**Jacopo Beschi:** Okay, let me see.

**Jacopo Beschi:** I'll share the screen, because I totally forgot.

**Jacopo Beschi:** Then I get there.

**Jacopo Beschi:** Share.

**Jacopo Beschi:** Okay, I'm just going to share everything.

**Jacopo Beschi:** Okay, should be able to.

**Daniel Lopes:** Can you see it now?

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Okay, so starting from Jose implementation, which looks familiar to me.

**Jacopo Beschi:** So what I understand now, so far, is that basically, you have this class.

**Jacopo Beschi:** client, right, which two method, I noticed.

**Jacopo Beschi:** And basically what they do is call execute workflow, which is going to call the API, which I suppose is our internal service API.

**Jacopo Beschi:** Right.

**Jacopo Beschi:** It's correct.

**Jacopo Beschi:** And so, and then basically it's going to handle the response, like if there is an error, it's going to basically build an error response and return an execute workflow.

**Jacopo Beschi:** Sorry.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** It's execute workflow response with success false and basically the error, the global ID.

**Daniel Lopes:** I'm not sure how it's built, but it's a detail.

**Jacopo Beschi:** Anyways, and then we have a lot of, we have a bunch of like web books.

**Jacopo Beschi:** So I'm not sure.

**Jacopo Beschi:** I mean, I've seen the web book controller, so, but what I see here is that it's just logic to,

**Jacopo Beschi:** So I'm going be a route that gets cold from the TypeScript code because I can see them, but I suppose there is an end point that receives the web book.

**Daniel Lopes:** Yeah, there'll be a Rails route for these two actions, and I think the clerk one is for login only, it's unrelated.

**Daniel Lopes:** The flow one is whatever the workbook says.

**Jacopo Beschi:** And this is going to create a web book, which is basically this class, and what it does is basically initialize a processor, which is one of these.

**Jacopo Beschi:** So depending on the source, so I think it's a parameter for sure, somewhere like...

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Yeah, it should be somewhere like...

**Jacopo Beschi:** So that's the last parameter.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** They're not permit.

**Jacopo Beschi:** Okay, it's not the explicit.

**Jacopo Beschi:** This is a parameter, and so the webbook will basically call the right processor, right?

**Jacopo Beschi:** And depending on what you, which kind of processing you need to do, it calls a different class, basically, from my understanding, right?

**Jacopo Beschi:** Because you have the controller, it will create, and then the webbook will just, after create commit, will run a job, basically, to process.

**Jacopo Beschi:** And the job will just call the processor processor, which is basically going to figure out the class, based on the action, okay?

**Jacopo Beschi:** So you can use, you can run, no, sorry, wait, hold on, double check.

**Jacopo Beschi:** Yeah, search classifier processor, okay?

**Jacopo Beschi:** And so it can be, like, either, like, I suppose, basic research or flow or anything.

**Daniel Lopes:** Fathom, right?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So those are the two workflows we have.

**Daniel Lopes:** So it has a research workflow, research workflow, when somebody signs up.

**Jacopo Beschi:** Yes.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** But then those workflows, I mean, what, I'm not totally sure, like, just give me a sec, maybe.

**Jacopo Beschi:** Let me see where we use the flow client.

**Jacopo Beschi:** Probe, onboarding, okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** So the flow client is called from the probe or from the onboarding?

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** So when you create an onboarding, for example, you're going to do the basic research.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** I see.

**Jacopo Beschi:** Do the basic research.

**Jacopo Beschi:** And then the flow client, we call basically this and basically search workflow.

**Jacopo Beschi:** It's going to execute the workflow, but I don't, I don't understand how this works, to be honest, because you have the webhook controller that creates a webhook, right?

**Jacopo Beschi:** But then, but then the part that calls the API is not this, but it's basically either like, you know, the probe or the onboarding, right?

**Daniel Lopes:** Yeah, I think what's going on, going on here is that he will, from the controller, when somebody signs up, it will trigger an API called using the flow client, and flow client hands off.

**Daniel Lopes:** And then the flow API would trigger a webhook back and it will be caught by the webhook controller.

**Daniel Lopes:** Okay.

**Daniel Lopes:** And I think that one creates the data.

**Jacopo Beschi:** So then, then we create this.

**Daniel Lopes:** Okay.

**Daniel Lopes:** So we have a route that is called basic click.

**Jacopo Beschi:** I don't know which one, yeah, and then he basically then handles that, okay, okay, I got you, so it makes sense now, okay, okay, okay, okay, so, okay, okay, for example, onboarding, create onboarding, you just call the API, and then they would just call the API endpoint, and then the temporal types of code will just call back here, I'm not sure, either one of these, and is the logic, and the flow, and then, okay, cool.

**Daniel Lopes:** Clark is the provider we use for authentication, and I think the webhook as well, that's why, so that control, I think, is handling both.

**Jacopo Beschi:** Yeah, I see, because you have two type of source, and so, okay, so, for example, the flow processor, we call the processor class, and then process, so, okay,

**Jacopo Beschi:** For example, if you do a probe, you know, probe, yeah, for example, yeah, you just do a bunch of logic, like, you receive the payload somewhere, like, probably, payload is here, so, yeah, here, so, the payload is from the web book, and the web book is created here with the payload, okay, so yes, the payload, okay, I see, okay, now I see, okay, And then this one, instead, I haven't took it deeply, I haven't taken a look deeper at this one, but, I've seen that, we basically, this is the one you created.

**Daniel Lopes:** This is the one that someone else created, like, I created the, the feature that I did, is the artifacts feature, that uses this client, as well, so, okay.

**Jacopo Beschi:** Okay.

**Daniel Lopes:** And then, uses, uses,

**Jacopo Beschi:** Yeah, I mean, this is something we, this is the implementation data that we can decide.

**Jacopo Beschi:** From my understanding is, I mean, if we need to do a lot of parallel HTTP requests, maybe HTTPX might be a little bit better.

**Jacopo Beschi:** I've used HTTPX in the Action Push Native Jam, actually, because it supports a lot of stuff, such as HTTP2, persistent connection, and so on.

**Jacopo Beschi:** But I don't think we need any of them, right?

**Jacopo Beschi:** We're just doing HTTP calls, and, I mean, slow HTTP calls, basically, right?

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** So we don't have, the performance is not an issue in this case, I suppose.

**Daniel Lopes:** Yeah, I think the thing that, I don't know if I don't de-support, but if you see the,

**Daniel Lopes:** Okay, so this feature here, the Atlas project, it uses so many workflows.

**Daniel Lopes:** So that's why there's a bunch of other ways of doing things.

**Daniel Lopes:** Workflows catalog is the entry point file that I was showing you before.

**Daniel Lopes:** Remember when I created the workflow?

**Jacopo Beschi:** But it's not here.

**Jacopo Beschi:** We had a list.

**Jacopo Beschi:** It's not here, yeah.

**Daniel Lopes:** But this is just like we returned the collection of workflows that are available.

**Daniel Lopes:** So that's like not related to the stuff that Rosal was doing.

**Daniel Lopes:** The start sync and start async is, that was an API cause to, one will wait for the workflow to complete, and another one will like let it go.

**Daniel Lopes:** So like they don't have web hooks.

**Daniel Lopes:** Yeah, they're just like, they will do polling, I think.

**Jacopo Beschi:** That's in this code base.

**Jacopo Beschi:** There is no web hook.

**Jacopo Beschi:** Yeah, yeah, I see.

**Jacopo Beschi:** I see, I see, see there is a, um,

**Jacopo Beschi:** Methods to look for status, which I suppose, this is the logic for the polling on the status.

**Jacopo Beschi:** And there are similar parameters, of course, I suppose, because it's the same API.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Like I noticed that in the client, you have, sorry, we have a, where it was.

**Jacopo Beschi:** Sorry, I'm going a little bit quick, because there is a lot of context to learn.

**Jacopo Beschi:** yeah, yeah.

**Jacopo Beschi:** have to do it as quickly as possible, but I might lose some bits for sure.

**Jacopo Beschi:** No problem.

**Jacopo Beschi:** Okay, call it, oh, no, no, never mind.

**Jacopo Beschi:** No, I said something, I'm not sure about that, but the response, no, never mind.

**Jacopo Beschi:** Let me go back here.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** The entry point, I'm not sure, do you know what is the entry point here?

**Daniel Lopes:** When you could, yeah, so the, maybe we can focus.

**Daniel Lopes:** can look for that, but.

**Daniel Lopes:** Yeah, maybe we can focus.

**Daniel Lopes:** It was an artifact, so artifacts folder, if you go to the route snippet on the back end, there's a route snippet is the last file on the back end folder.

**Daniel Lopes:** Okay, this one.

**Daniel Lopes:** So that's the entry point of the feature.

**Daniel Lopes:** So we have a route to open up that modal, okay, shows you, like, type in the company name and the URL, and then if you hit post, we hit that create, and then there's a retry button as well.

**Daniel Lopes:** Those three things are inside the artifact generation controller.

**Jacopo Beschi:** Okay.

**Daniel Lopes:** This controller is the production one, so taking a program generation type, if nothing is passed, then we do a company research, this one, so if the type is...

**Daniel Lopes:** Search will pop up, this is the new one, so it's gonna pop up the modem.

**Daniel Lopes:** If it's content suite, we'll like start a different modem.

**Daniel Lopes:** And then the create button, the create action is right under, and that's the one that triggers the background job.

**Daniel Lopes:** See, like there's like a line 43, there's an artifact generation workflow.

**Daniel Lopes:** And that will kick off the creation process.

**Daniel Lopes:** That is the file, there, this one.

**Jacopo Beschi:** Okay, it's on the job here.

**Daniel Lopes:** Yeah, it's on the job, okay.

**Daniel Lopes:** So this one will prepare the workflow params, and then we'll create.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Prepare Prepare workflow params.

**Jacopo Beschi:** Prepare Prepare Prepare You

**Jacopo Beschi:** Based on the input, like if you do a company research or a content suite, you just buy a different, okay, and then, okay, and then you call the, okay, then you call the, think, okay, I see.

**Daniel Lopes:** Yeah, so that's where the client is getting, getting triggered.

**Jacopo Beschi:** Okay, and then you just, okay, then it's the job to pull, basically, this one.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** Okay.

**Daniel Lopes:** So there's like a check status one.

**Jacopo Beschi:** Okay, and then it's just gonna, okay, check status, right, if it's done, basically, so this should be if it's completed, okay, if it's done or failed, and then use the client here to pull, okay, I see.

**Jacopo Beschi:** Okay, okay.

**Jacopo Beschi:** I'm trying to understand, okay, I understand it more now.

**Jacopo Beschi:** Okay, and then here you have your logic based on the status, basic status name.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Completion and failure.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Okay.

**Daniel Lopes:** Okay.

**Daniel Lopes:** And then, if you look on the left side, there's a folder called Other Workflows.

**Daniel Lopes:** Those are the other features that are also dependent on our AI workflow.

**Daniel Lopes:** So there's a page import that will take the pages from the sites of our clients, and then there's all the URLs from their site map as page records.

**Daniel Lopes:** And then there's a page-scanning one that will go through each one of the pages and process them.

**Daniel Lopes:** And then we also have a knowledge-based search, research feature.

**Daniel Lopes:** So there's more features that use this thing, and there's the pipeline execution, so that's four features that uses the same stuff.

**Daniel Lopes:** The only catch here that I don't know the solution to this, feel like I'm just thinking about, so we have Jose is handling things to web.

**Daniel Lopes:** I'm handling things here through polling.

**Daniel Lopes:** My preferred option would be webhooks for most of things, I think.

**Daniel Lopes:** But then you have things like the page import and page scanning.

**Daniel Lopes:** The page import is a kind of simple one because it's going to be fast.

**Daniel Lopes:** It's just like processing, coming up, finding a sitemap, extracting all the URLs, and storing the database.

**Daniel Lopes:** The biggest scanning one, I think if it was 300,000 pages, for example, which is not uncommon.

**Daniel Lopes:** So we have clients like Webflow, Ramp, Airbytes, and they would have thousands of pages.

**Daniel Lopes:** So I don't know what would happen if we had a webhooks system here.

**Daniel Lopes:** It would probably be DDoS our Rails app with like thousands of posts back, you know?

**Jacopo Beschi:** So I think we...

**Daniel Lopes:** If you had a gen, you would probably have to support.

**Jacopo Beschi:** Yeah, but I'm wondering, like, I mean, the webbook is called when all the processing is done.

**Jacopo Beschi:** Yeah.

**Daniel Lopes:** Or, okay.

**Jacopo Beschi:** When the workflow is So if you have, when all the workflow is done.

**Jacopo Beschi:** But the workflow is made of multiple steps, right?

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** And they can end at different times.

**Daniel Lopes:** So, like, we could send maybe, like, let's say we're processing a client.

**Daniel Lopes:** Like, ramp, they have 200,000 pages.

**Daniel Lopes:** We could have, we could batch and, like, trigger maybe 50 pages at a time.

**Daniel Lopes:** And then you would send the webbook back when each one completes.

**Daniel Lopes:** And they'll complete at different times because the APIs will fail and that kind of stuff.

**Daniel Lopes:** And it's probably not, not a problem, but that's something that I know that this is the rationale.

**Daniel Lopes:** Now, why Brad, the person that was implementing this, decided to go with, like, he has a Redis here that will hold this state.

**Daniel Lopes:** Yeah, hold this state and do a bulk status check.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And that was the reason, because he wanted to not use Webhook to not risk overwhelming the Rails app with incoming calls, and he was going to do a bulk status check.

**Daniel Lopes:** Well, the thing is...

**Daniel Lopes:** don't know if that's a legit concern, you know?

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** I'm not sure.

**Jacopo Beschi:** Without the data, it's difficult to say, like, how problematic it will be.

**Jacopo Beschi:** But, no, because I'm wondering, like, if you can do, like, status updates more frequent via Webhook or something like that.

**Jacopo Beschi:** I mean, the polling is not bad, per se.

**Daniel Lopes:** Yeah.

**Jacopo Beschi:** But you're going to have a lot of jobs running.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** And maybe doing nothing, a lot of time, I suppose.

**Jacopo Beschi:** So it's a little bit of a waste.

**Jacopo Beschi:** But the webbook you said, I'm not following the part where you said that the webbook will just do us.

**Jacopo Beschi:** I mean, you can rate limit, do a bunch of work around for that, but I don't understand the fact that you said that we would do us the race up if it's called only at the end.

**Daniel Lopes:** Of the workflow?

**Daniel Lopes:** Like, it's at the end of, like, in this case, every page will be a workflow.

**Jacopo Beschi:** Ah, I see.

**Daniel Lopes:** Okay.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Sorry.

**Jacopo Beschi:** I'm not completely following everything.

**Jacopo Beschi:** Sorry.

**Jacopo Beschi:** So I'm just doing some stuff.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Okay.

**Daniel Lopes:** So we could change it to be processed at the end of processing the entire website, but I think it would probably be better to do a page-by-page level just for the atomic distribution of the work.

**Daniel Lopes:** So we don't risk losing, let's say you processed 150,000 pages, and then 151 fails, now we have to retry from 151, you know?

**Jacopo Beschi:** So I think that's why he did Atomic.

**Jacopo Beschi:** But let me see one thing, but the, sorry, the page scanning is the big one, right?

**Jacopo Beschi:** And check workflow start to job, I suppose it's what is on hold of taking a look at, I mean, just taking a look at the status, right?

**Jacopo Beschi:** And you said you have a lot of workflows, but how does it take sort of time?

**Jacopo Beschi:** Yeah, I'm just trying to understand, if it's just one job for each, so for thousands of pages, or it's just one job that takes multiple pages, I suppose it's thousands of jobs.

**Daniel Lopes:** No, batch size, okay.

**Jacopo Beschi:** So as you mentioned, so do you have one job for batching through the multiple workflows?

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Now I see what you mean.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** check any workflow.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** And this is going to do that.

**Daniel Lopes:** Ah, okay.

**Daniel Lopes:** It's totally ready.

**Jacopo Beschi:** the idea, I suppose.

**Jacopo Beschi:** Something probably that is.

**Jacopo Beschi:** Ah, okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** So you go to the idea, you extract the data from a JSON, retry count.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** So, okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** at some point, okay.

**Jacopo Beschi:** have max retries of five.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** I see.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Uh-huh.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Now I understand more.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** So to recap, the workflow, sorry, the webbooks approach can be problematic if you have a lot of workflows, because you have a lot of, I mean, honestly, it's going to be a problem.

**Jacopo Beschi:** I need to figure it out because, because it's like, what it's going to be like.

**Jacopo Beschi:** Basically, in this implementation, it's going to be like, each workflow completion is a code on this method.

**Jacopo Beschi:** And, I mean, they can complete at a different time.

**Jacopo Beschi:** Yeah, it's more expensive.

**Daniel Lopes:** Yeah, I'm more concerned about, like, request queuing at the HTTP level, you know?

**Daniel Lopes:** So, like, let's say, because you might have received bursts of, like, 50,000 requests.

**Jacopo Beschi:** But this process in the background, the workflow logic is in the background.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** So, it should be fast to respond, like, 100 MS or 200 or something like that, I suppose.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** So, you shouldn't have request queuing, and then you have one job.

**Jacopo Beschi:** For each, like, stats update, let's say.

**Jacopo Beschi:** So, it's quite similar, but you're going to have a lot of jobs, like...

**Jacopo Beschi:** I don't think, I'm not sure.

**Daniel Lopes:** I think we need to do some expectation.

**Jacopo Beschi:** I think I prefer the webhook approach because then you move all the complexity of batching and all that kind of stuff out of the code.

**Jacopo Beschi:** Yeah, the only problem with the webhook, I mean, not only, but one problem would be like, what's going to happen if you don't receive it?

**Jacopo Beschi:** You need to take care of that somehow.

**Jacopo Beschi:** Like, you can, you need to handle that in some way.

**Jacopo Beschi:** So if you want to follow, like, a webhook approach, you need to have some sort of long-term following to make sure that it's not going to be, like, left dead, you know?

**Jacopo Beschi:** It can even be a job, like, a recurring job that take a look at the webhook status and it is, like, processing more than whatever minutes you need to do something to handle that.

**Jacopo Beschi:** It could be either...

**Jacopo Beschi:** At this point, pull for the status of the workflow and see what's going on and all that.

**Jacopo Beschi:** So maybe you can do something like webhook, logic, and then figure a job.

**Jacopo Beschi:** Like the webhook creation, I'm just wondering.

**Jacopo Beschi:** So the webhook creation could just, for example, after create, commit, process later, and then also, I don't know, something like this.

**Jacopo Beschi:** Sorry.

**Jacopo Beschi:** I'm still learning this new editor.

**Jacopo Beschi:** Or remember, or very, very, I'll check, I don't like this name, but check tattoos later or something like that.

**Jacopo Beschi:** That's an idea.

**Jacopo Beschi:** And then it's going to enqueue a job.

**Jacopo Beschi:** Like, that's one idea, but they have also another, like, then you do this check status later.

**Jacopo Beschi:** And it is going to do, like, enqueue a check job in X minutes or something.

**Jacopo Beschi:** Because I don't if you have, like, an idea of how long it's

**Jacopo Beschi:** And this can, I don't love this pattern, so I'm going to go for the other one, but the pattern is your job in the future, like 30 minutes from now, okay, and it's going to check for the status.

**Jacopo Beschi:** If it's done, it's done.

**Jacopo Beschi:** If it's not done, let's see what's going on, and then check the status again later, or check the status again later if it's working, for example.

**Jacopo Beschi:** So, the other approach is you can, I don't love this approach because it has a lot of problems.

**Jacopo Beschi:** We had a lot of problems in basic account for this approach because it's very easy to implement, like, do this something in the future and then do it again and again and again, but if lose a job, you basically, you're blocked, you know?

**Jacopo Beschi:** So, you may be, it can happen because this is not, like, super reliable that you lose a job, and then you basically are left with that status.

**Jacopo Beschi:** Another approach is to have a cron job.

**Jacopo Beschi:** or something recurring, like a recurring job in a solid queue, I think there is also something similar, that just batches to the webhooks, through all the webhooks, and take a look at their status, like, you can store probably when it started, right?

**Jacopo Beschi:** So you can look for, like, jobs that started, you have, yeah, you have creation that did, you can use that already, so you can just look through all the jobs that are created, loop through all the, you don't have a status here, scope, processed, work, yeah, you have processed, so you can use processed, so you can loop through all the not processed jobs created 30 minutes ago, more than 30 minutes ago, and check for the status, basically.

**Jacopo Beschi:** You can do that, you can do do barge through that, you should be fine.

**Jacopo Beschi:** Unless you have million jobs, then you can't need to handle that differently, but you can just barge through all of them.

**Jacopo Beschi:** At this point, I don't know what the scale of the app, but batching should work.

**Jacopo Beschi:** And that's one option, like batching all the jobs that are created six minutes ago and are not done yet.

**Jacopo Beschi:** I mean, if you have like a million of job processing, okay, maybe you need to implement something else, but I don't think you're going to have them.

**Jacopo Beschi:** So batching to the job that are still processing and are way back, it's probably going to be an issue.

**Jacopo Beschi:** I mean, most of them would probably be broken or have some issues, so you need to take care of them.

**Jacopo Beschi:** So don't expect like a huge amount of these jobs to be fair.

**Jacopo Beschi:** So you can basically use the webhook approach, which is something on the line of these, paired with the status check, and you are covered from that job, I mean, that webhook call.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** And you have a lot of webhook.

**Jacopo Beschi:** You said that you can...

**Jacopo Beschi:** I have a lot of HTTP calls, but I don't think it's a big deal, to be honest.

**Daniel Lopes:** I mean, should be a good job.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Yeah, it should be cheap.

**Jacopo Beschi:** And the main difference is that basically as soon as something is done, you process it.

**Jacopo Beschi:** So the load will spread depending on when our workflows are completed.

**Jacopo Beschi:** And the other approach with the polling, you have this long-running job that's going to keep on polling.

**Jacopo Beschi:** And I don't think it's a difference in demo's performance, to be honest.

**Jacopo Beschi:** Because if the processing, actually, I believe that this one with the web scales more.

**Jacopo Beschi:** Because let's say you're using the polling, you need to process each workflow that is completed sequentially, right?

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** In the other case, if multiple workflows, like multiple page scan workflows completes in parallel, you can process them in parallel.

**Jacopo Beschi:** And then even if you have a lot of data to process, it's not a big deal, you have a queue in the job, right?

**Jacopo Beschi:** And queuing in the background job is a different issue compared to queuing in the HTTP server.

**Jacopo Beschi:** Yeah, you can handle that, can scale worker, you can do lot of things.

**Jacopo Beschi:** mean, it can happen, but you can deal with that, and it's not like something urgent.

**Jacopo Beschi:** You know, you can, if you have monitoring, see the alert, and you deal with it in one hour, it's fine.

**Daniel Lopes:** And if we had queuing at the HTTP level, we could handle that as well as a separate setup.

**Daniel Lopes:** It could even lower to like metal controller or like a very basic API controller to reduce the overhead from like 550 to lower.

**Jacopo Beschi:** It doesn't work separate to separate.

**Jacopo Beschi:** Yeah, you can also separate the server pool for this endpoint, yeah, as you mentioned, yeah.

**Jacopo Beschi:** And what I was saying, sorry, I forgot.

**Jacopo Beschi:** Yeah, okay.

**Daniel Lopes:** I think, like, my preference is probably the webhook approach.

**Daniel Lopes:** When, like, before, like, when we were, I actually, like, haven't, like, right before this call, like, yesterday, I was actually, like, a collection of uses just for me to look at how everybody's using things together.

**Daniel Lopes:** And when we are going through everything together now, I actually hadn't seen anything, everything.

**Daniel Lopes:** I had seen some of it, and I saw the ones that I did, like, the artifact was a feature that I built in, like, 30 minutes.

**Daniel Lopes:** But then I was looking at the other stuff, and I saw that they even have...

**Daniel Lopes:** Server-side events with like streaming, the knowledge-based research, if you go to that, inside of the other workflows folder, there is like knowledge-based research, research RB.

**Jacopo Beschi:** Yeah, this is an active model, which, okay, pull up data and save.

**Daniel Lopes:** Yeah, so, answer, let's see, what is the answer?

**Daniel Lopes:** We don't have to go through the whole thing, but while we are, like, I showed you something that I, while you were studying the code, I was doing the same, and like I, just out of curiosity, I gave this prompt here to my Claude, asking for, one sec, I was like, I have this API called Flow that we use.

**Daniel Lopes:** On both of our products, check.ai and Atlas, and I'm thinking about Ruby or Rails style gen to normalize the consumption.

**Daniel Lopes:** Can you review everything and help me think about it?

**Daniel Lopes:** So it did this, and it said, there are some interesting, I think there are some interesting ideas here.

**Daniel Lopes:** So it took a while, I read all the files, analyzed all the different use cases and everything, and it kind of pulled like an interesting doc.

**Daniel Lopes:** Let me share the doc with you, and maybe we can read it and think about it, if there's anything here.

**Daniel Lopes:** Like I, if, because there's like how the folks are doing things, and again, what I'm thinking is just like, if we had a gen that told the folks on Atlas, hey, you got to use this way, and like we go with the webhook, for example, that would at least normalize things a bit.

**Jacopo Beschi:** And yeah, yeah.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Yes, I see what you mean.

**Jacopo Beschi:** If you, I mean, the webhook approach, I think we can create a gem that, you know, you can do like abstract the webhook class.

**Jacopo Beschi:** Could be like, I don't know what is a good name, maybe.

**Jacopo Beschi:** Let's say application webhook for both.

**Jacopo Beschi:** And then you just basically, in your app, you inherit from that.

**Jacopo Beschi:** You can handle that by initiating from that.

**Jacopo Beschi:** then you just, if you expose like, it can even be like exposing like the process.

**Jacopo Beschi:** I mean, the webhook will handle all the retries in queuing the job to, sorry, in queuing the job to monitor the status, which is what I mentioned earlier.

**Jacopo Beschi:** And basically, sorry, I'm just thinking loud.

**Jacopo Beschi:** Yeah, yeah.

**Jacopo Beschi:** So if you want to extract this into a gem, think you can have like controller.

**Jacopo Beschi:** Like it can be a Rails engine, for example, okay, where you can define routes, okay?

**Jacopo Beschi:** And at that point in the engine, you can define a route for receiving the webhook.

**Daniel Lopes:** Yeah.

**Jacopo Beschi:** Which is, it doesn't have to be exactly this, but just something on the line of deals with different naming and maybe, okay, different naming.

**Jacopo Beschi:** mean, then we need to figure out like how to define like the endpoint, if it's just going to be one, and then some logic to dispatch.

**Jacopo Beschi:** Like, for example, in this case, you have the flow, and then you have the dispatch to figure the, sorry, the webhook process, webhook process job is going to call the webhook processor.

**Jacopo Beschi:** So, yes, so, right, okay, so you need to.

**Jacopo Beschi:** To figure out, like, okay, so, Ricardo, I was thinking it loud first.

**Jacopo Beschi:** Create a controller, create any, I would create an engine that exposes an endpoint, that endpoint and whatever class you want to use, okay.

**Jacopo Beschi:** It can even be actually configured, in my opinion, like, you can even have, like, optional configuration that you can add.

**Jacopo Beschi:** So, for example, like, given a certain input field, which is part of the payload, use this class, or it can even be, like, So, given this input, it's still outside speaking, so, given this input, you dispatch this class.

**Jacopo Beschi:** And then, you can create a base web class in the library that you need to inherit from, okay.

**Jacopo Beschi:** So, and then the client, basically, what he needs to do is install the engine, create his own web classes.

**Jacopo Beschi:** To figure out, like, okay, so, Ricardo, I was thinking it loud first.

**Jacopo Beschi:** Create a controller, create any, I would create an engine that exposes an endpoint, that endpoint and whatever class you want to use, okay.

**Jacopo Beschi:** It can even be actually configured, in my opinion, like, you can even have, like, optional configuration that you can add.

**Jacopo Beschi:** So, for example, like, given a certain input field, which is part of the payload, use this class, or it can even be, like, So, given this input, it's still outside speaking, so, given this input, you dispatch this class.

**Daniel Lopes:** And then, you can create a base web class in the library that you need to inherit from, okay.

**Daniel Lopes:** So, and then the client, basically, what he needs to do is install the engine, create his own web classes.

**Daniel Lopes:** That does whatever they want, okay, at this point the process is the actual implementation, so you don't do this here, it's the library, you don't care of this, okay, and then, sorry, and the client will be basically implement, like, plus, it can even be this, this, and then it will then air it, okay, and it implements the process.

**Daniel Lopes:** The calling logic is handled by the library, and the logic to dispatch is handled by the library, yeah.

**Daniel Lopes:** Yeah, I think that, that would be very similar to the architecture that I was thinking, and I could actually, like, if you take a look, like, I can give you, like, five minutes to go through this document at your own time, but, like, take a look at what was, this is, like, obviously auto-generated, so there's a lot of stuff here that probably doesn't make sense, doesn't make sense in the first version.

**Daniel Lopes:** But it's very similar to what you are thinking about in many areas.

**Daniel Lopes:** So that was, I was generating, I was letting that generate as we were reading the code together.

**Daniel Lopes:** So we identified the problem with like Fair Day and HTTPX, would have to choose.

**Daniel Lopes:** Then it came up with, sorry, go ahead.

**Daniel Lopes:** Please go ahead, if you want to.

**Daniel Lopes:** Yeah, and then identify a few problems, like any variables everywhere, five different ways of dealing with async workflows, multiple workflow clients, similar logic kind of stuff, and no reusable web component verification or status check.

**Jacopo Beschi:** Like what we're essentially talking about.

**Jacopo Beschi:** And then it came up with like a potential.

**Jacopo Beschi:** It included like the idea of tracking the status, because that's what Brad had with the Redis, but had like different patterns for webhook, pulling, and streaming.

**Jacopo Beschi:** So streaming is the one that the knowledge base uses, I didn't even know we were using streaming for that.

**Jacopo Beschi:** So that was interesting to see.

**Jacopo Beschi:** Then it was using a rail type for routes, had model concerns for dealing with the result, and a job helper for your application job, and some configurations.

**Jacopo Beschi:** There's some interesting ideas, you know, so I think.

**Jacopo Beschi:** Mm-hmm.

**Jacopo Beschi:** I mean, okay, um, let's see, fine, forget, Robo, okay, trackable, okay, this is the controller, and this is the Robo, okay, flow work with the Fathom workflow, okay, and process workflow, okay, controller, very powerful process, okay, okay, this is the logic to basically process depending on the payload, yeah, makes sense, okay, dedicated polling, chart import, begin import, schedule polling job, okay, check info status job, this is the job to check the status, okay, see,

**Jacopo Beschi:** That is the part I think we need it, like, if we just go through the webhook approach, that doesn't make sense.

**Jacopo Beschi:** Start with your workflow, tracking radius, okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** There are some design choices that I don't agree with, but I keep on reading.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Check the work of the job.

**Daniel Lopes:** Okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Mm-hmm.

**Jacopo Beschi:** Makes sense.

**Jacopo Beschi:** So, basically, you start a sync, you track the radius, the IDs, to monitor them afterwards, and then, okay, work of tracking workflow.

**Jacopo Beschi:** Okay, this is the job to, to, to pull, basically, okay, and then complete, okay, pattern D, okay.

**Jacopo Beschi:** Yes, Daniel, that true?

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** I'm going through.

**Jacopo Beschi:** Are you scheming quickly just to use?

**Jacopo Beschi:** Yeah, yeah, yeah, yeah.

**Jacopo Beschi:** Okay, this is the tracking, the track status, I suppose.

**Jacopo Beschi:** No, yes.

**Jacopo Beschi:** Okay.

**Daniel Lopes:** Okay.

**Jacopo Beschi:** Yeah, I will design this a little bit different, but it makes sense.

**Jacopo Beschi:** Yes, mean, it's an interesting grain down.

**Jacopo Beschi:** Completely different.

**Jacopo Beschi:** Yeah, but I mean, what I will do is create a record.

**Jacopo Beschi:** mean, generally, I wouldn't store in radius persistent information, like anything that can be lost.

**Jacopo Beschi:** Will be lost.

**Jacopo Beschi:** Yeah, because it can be lost, will be lost.

**Jacopo Beschi:** I've been, I mean, it depends how important it is, of course, but still, I will store every important bit in the database, because it's more reliable, reliable, and it also reduces.

**Jacopo Beschi:** So what I will do, let me just finish before speaking, okay, okay, I'm not sure about this, but okay, migration strategy, okay, let me pause it here, so what I would basically maybe do is something like, let me try to type, if I can, so I will create like a class, as I mentioned, I will repeat myself a bit, but I create a class like, it is the base class, that handles all the webbook status, so I don't, I'm not sure I'll name it webbook, but let me name it like webbook, in Rails, you just generally do like, webbook base, you do this kind of naming in library, like, webbook base, so in the library, you create a business class, I'm fiddling a bit, yeah, I'm fiddling a bit with this,

**Jacopo Beschi:** Okay, web-based class, and this will have basically a new status, you know, where I just define, like, probably, like, I don't think it's pending, so you can have, like, processing, right?

**Jacopo Beschi:** Maybe just this for now.

**Jacopo Beschi:** Maybe just processing a Fathom, maybe.

**Jacopo Beschi:** And then, you you'll have, like, a process method, which is what is on hold of taking care of all the processing on the high level, not what the actual processing is, but taking care of the high-level processing.

**Jacopo Beschi:** So, I mean, the default is, like, default.

**Jacopo Beschi:** I don't want to quote it all, but default will be, like, processing.

**Jacopo Beschi:** In this case, for example, it can be...

**Jacopo Beschi:** Something like this, sorry, this is the processing, and then you do like after create commit, okay, process later, okay, and process later, we'll do basically the job, you know, process, I don't know, webhook, base job, okay, but also, it should also include, like, remember to check later, something like this, it's a bit trash code now, okay, but that's the idea, and then remember to check later, we just, this will just include a job, like, webhook, check status job, I don't know, this can have the full wait time, or you can even set the year, like, set the wait, I don't

**Jacopo Beschi:** Default, wait, I don't know, I don't love this name, but, and this is going to be a constant, like 30 minutes from now, okay, I'm going to write it now, and this is basically the base class, and in your app you do the class, I don't know, basic search processor, inherit from, you can even implement, like, application, application, webbook, where you can define the configuration and stuff like that, that we didn't have, we don't have right now, but you can have them, like, for example, the default wait time can be configured, and whatever else, okay, and then here you just define, you do a private, you know, dev, do process, sorry, and you do whatever you want, you know, yeah, blah, blah, and, So that, you're thinking, thinking would be, like, in the models folder,

**Jacopo Beschi:** And it would be, um, this should be in the app.

**Jacopo Beschi:** So the app should be engine, my opinion, because you need routing, you need, uh, you need writing.

**Jacopo Beschi:** And you might even want to inject that into your application.

**Jacopo Beschi:** You might want to have like a generator or stuff like that.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Like to generate a processor if you want to, or whatever else.

**Jacopo Beschi:** So this will be like in the library app, uh, models folder, like Webboot.

**Daniel Lopes:** No, yeah.

**Daniel Lopes:** Sorry.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Okay.

**Daniel Lopes:** this is the, this is the.

**Jacopo Beschi:** In your project.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** And this is the, uh, live code.

**Jacopo Beschi:** And the, and the, and the generator would create the processor in the models folder.

**Jacopo Beschi:** And you can have as many as you want for whatever workflows.

**Jacopo Beschi:** So, yeah, so these can be generated, for example, also.

**Jacopo Beschi:** Then the workflow, so the problem of generating the workflow, finishing this part first, and then you're going to have a controller, like webhook controller, blah, blah, blah, webhooks controller, and this is going to have that create, something like this, it depends how we name the route, yeah, and this is going to do like the, you think you would mount this route in the routes file from the, and the gem would provide the controller, so this can be a route, you can have a route in the gem, and then you mount the routes in the app, so this belongs, I might try to visit this, as we go through this, to be honest, this is a, this this

**Jacopo Beschi:** Route in the live, and then you mount the engine in the app to expose it.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** But then thinking of the polymorphia dispatch, like, I don't like the fact that it shouldn't be done here.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** So you can have, like, so one option.

**Jacopo Beschi:** Is that it's not the web book that is on all of that, but some other class, like, so could be, like, web, I don't know, dispatcher, let me just name it like this, and this is going to receive an input, like, uh, it can even be a class method for now.

**Jacopo Beschi:** Okay, and this is going to be receiving an input payload, as a hash, so you can even name it as payload hash, and this is going to do the polymorphic dispatch, it can be automatic, you know, it can be like payload hash, action, or whatever, you know, and you do constantize, dot, uh, you know, um, yeah, dot create, you know, and then you pass an input, like, uh, the payload, you know, and I don't know, whatever else, I, um, maybe, I can think of additional parameter for now, because I don't know all the, you know, all the context, so it's difficult, to be honest, and then here, you just use a web dispatcher at this point, uh, it's not applicable to completing, okay,

**Jacopo Beschi:** Oh, okay, I did use a different case, but in order, .dispatch, you know, and then you just have the request, it can even be like payload, param, you know, so you can, or just push params to be simple like for now, okay?

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** And so this is going to create the class, and then the webhook is going to process in the background, right?

**Jacopo Beschi:** And remember to process later.

**Jacopo Beschi:** So that's what is exposed to handle the webhook thing, and then you need to have a logic to trigger the webhook.

**Jacopo Beschi:** So how can we do that?

**Jacopo Beschi:** It can be like, so how did do that to you?

**Jacopo Beschi:** Like, sorry, my screen is a mess.

**Jacopo Beschi:** So here you go the flow client, okay, of course this is going to be internal, so the HTTP client is going to be internal in the library, it's not going be exposed at this point, anyways, it can be like, I don't know, I don't love this name, I mean, I need to revisit it, but it can be like workflow, okay, it is a workflow, it creates workflow, trigger, triggers workflow, so, yeah, my name is a bit, but okay, that's just to give you an idea, so this is going to trigger the workflow, and again, this is going to be like, probably like, I don't think any distance variables, it can be also a static cluster, like, yeah, and then, and I don't know what we have, like, is it only a name, or maybe something more, I suppose, yeah.

**Jacopo Beschi:** Yeah, right.

**Jacopo Beschi:** And this is going to use the client, which is going to be like whatever.

**Jacopo Beschi:** Inside the library.

**Jacopo Beschi:** Yeah, client.process, I don't know, perform.

**Jacopo Beschi:** It's going to be actually, I don't know, perform.

**Jacopo Beschi:** It's going to do an HP call, so I've got to think about a good name.

**Jacopo Beschi:** But do request or, it's going to do request for now, okay?

**Jacopo Beschi:** Or request, request, and then you pass the, yeah, you can accept this.

**Jacopo Beschi:** Actually, why do we need this at this point?

**Jacopo Beschi:** I can see the controller, guess.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** I mean, you can.

**Jacopo Beschi:** I'm sure if we need.

**Jacopo Beschi:** Yes, I mean, you can use the, I don't like the fact that you use the client directly, you know what I mean, because you don't want to expose the HTTP client, it's an internal implementation detail at this point, so the class needs, but, okay, for now, let's do this, but I don't like the fact that you're just providing something, so it's bad, in my opinion, but leave it aside for a minute, to revisit.

**Jacopo Beschi:** The idea is this, you, in your app, you know, this is the app code, so, this is the class, and then you're going to have a controller, like, or I don't know where you want to do it, like, it can even be a model, like, I don't mind, in the code, app code, what you do is, workflow trigger, or, actually, it is this, actually, workflow.trigger, for example.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Trigger, right, and then you just...

**Jacopo Beschi:** Fathom, name, research, I don't know, and then params, I don't know what they are, whatever they are.

**Jacopo Beschi:** That's a very, very, very basic, I don't know if you can see it all, very basic idea of what I was thinking about.

**Jacopo Beschi:** And then there is basically, you need to update the status, but again, it can be this, like, when it's done, it can do, like, sorry, I forgot, processing, right, and processed or complete process, that I like more processed in this case, right, so when, sorry, this is not in the ear, right, again, the do process is going to do something, right, it can even be, like, fail at some point, like, for whatever reason, like, reason, so you can,

**Jacopo Beschi:** Yeah, you can handle this via exception, via exception, so rescue for now, so it's going to rescue whatever, you know, error.

**Jacopo Beschi:** This is going to rescue every standard error, for example, and then it's going to be like failed.

**Jacopo Beschi:** So now I realize maybe you need like a field to track the failure reason, for example.

**Jacopo Beschi:** Like, for example, it can be like, so it can be like, something like, not this, but update status failed, and then reason error.

**Jacopo Beschi:** Just, it might be something more smart, but let's do like this to give an idea.

**Jacopo Beschi:** So at least if it fails whilst processing, you know that it failed for whatever reason, and then in your app, you handle that via exception.

**Jacopo Beschi:** I mean, in your app, can, if error,

**Daniel Lopes:** That's what I mean.

**Jacopo Beschi:** This is the app code.

**Jacopo Beschi:** So in the app, you can handle error via exception, then the workflow engine, call it engine.

**Jacopo Beschi:** And then you can add a lot of stuff.

**Jacopo Beschi:** You can add, like, event tracking, for example, like, if you need to, logging and so on.

**Jacopo Beschi:** And then you need to implement also, like, the check status, right?

**Jacopo Beschi:** And this can be, like, a different, it can be handled, like, with probably, probably can be done from, I'm thinking, like, if you can be handling the web, because you might need a separate class, maybe a separate.

**Jacopo Beschi:** Or, it can, maybe even, for now, end of the year, like, I mean, oh, nice.

**Jacopo Beschi:** Yes, good point.

**Jacopo Beschi:** We need to have an ID to track.

**Jacopo Beschi:** Yeah, so when you trigger, need to get the...

**Jacopo Beschi:** Yeah, so when you do process, the do process actually is not as simple as this.

**Jacopo Beschi:** No, sorry.

**Jacopo Beschi:** When you trigger, as you mentioned, yeah, when you trigger, yeah, you need to have an ID.

**Jacopo Beschi:** So you can actually create...

**Jacopo Beschi:** No.

**Jacopo Beschi:** It would be nice to be able to pass your own ID so you...

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** backend actually can do that today.

**Jacopo Beschi:** So like the API, if you pass an ID, we use it.

**Jacopo Beschi:** So we could generate an ID from here and send it.

**Jacopo Beschi:** Yeah, so you can generate it here and then you can use it on the controller, like for, I don't know, let's say like ID, whatever, secure random dot...

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Okay, just to use something now.

**Jacopo Beschi:** And then in the response, in the control...

**Jacopo Beschi:** So here you can use, here you create the payload, but then you can extract the ID also, like, you can do, like, payload, I'm doing something naive, but, you know, ID, and then you just pass the ID payload, okay, and so here, now you have a, so sorry, you it's not going to be the ID, but it's going to be, like, the workflow ID, okay, so here now you have the workflow ID, and you can use it, like, in the logic to check the status, which is something I was implementing, it doesn't exist yet, okay, it's going to be probably a public method, like, it can be a separate class, but let's do it here, and then check status, and then

**Daniel Lopes:** Here it's going to be like, call the client, and at this point, the client can have like, can do like, for example, trigger, and then, get, or status, workflow status.

**Jacopo Beschi:** I don't know, might be redundant status is okay for now, and then you just pass the ID, and then you just have some payload.

**Jacopo Beschi:** But I don't know which payload it is for now, you know, and then you handle the payload here, like, handle payload, and whatever, like, you can do like, payload dot status, sorry, status, and then, you know, I don't know what to do here for now.

**Jacopo Beschi:** No, that makes sense.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Cool.

**Jacopo Beschi:** Yeah, I think, I think that, like, that's pretty close to how I would want it to look like.

**Jacopo Beschi:** And, yeah, I would.

**Jacopo Beschi:** It would of like a bulky-ish gem that you'd have routes, you'd have like models, you would have, but I get, like, what do you think?

**Daniel Lopes:** do you think, does it make sense to have a gem for this?

**Daniel Lopes:** Like, in my mind, it does, because there's, yeah, I don't know.

**Jacopo Beschi:** What we generally do, what I generally do is first put whatever can be extracted into lib, and then extract into lib.

**Jacopo Beschi:** And then if you need to use multiple apps, at this point, you make a gem, and then use the gem in every app.

**Jacopo Beschi:** But first, I do the move to the lib from the app code base.

**Jacopo Beschi:** So you have this, you know, single folder, let's say, that stores whatever you need, and then you extract to a gem before doing the extraction.

**Jacopo Beschi:** So you do a multiple-step work, and you can have an idea, because the extraction will also give you more information, like, what you actually really need to put into the lib before you...

**Jacopo Beschi:** And then you create the lib and yeah, probably it's going to be in an engine where you have the routes and the model.

**Jacopo Beschi:** You don't need anything else probably.

**Daniel Lopes:** And as concerning the client, I don't know what to do.

**Jacopo Beschi:** It needs a migration as well.

**Jacopo Beschi:** It probably makes sense to have like a migration generator with like how you store some of the stuff, right?

**Jacopo Beschi:** Oh, yeah.

**Jacopo Beschi:** You mean migration in a sense for the database models?

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** For storing like this.

**Jacopo Beschi:** Or to migrate from...

**Jacopo Beschi:** Yeah, yeah.

**Jacopo Beschi:** So in the engine, just have the...

**Jacopo Beschi:** Let me show you.

**Jacopo Beschi:** I want to make sure you have enough time because like we are over...

**Daniel Lopes:** Yeah, yeah.

**Jacopo Beschi:** Don't worry about my time.

**Jacopo Beschi:** It's not my concern in time.

**Jacopo Beschi:** If it's your concern, okay.

**Jacopo Beschi:** So it's very simple.

**Jacopo Beschi:** Like this...

**Jacopo Beschi:** And then you have your app controller, app model, you know, here you have, you don't have controllers, you have just jobs and model, but you can have app model, controller, jobs.

**Jacopo Beschi:** Sorry, and then you have, you know, the jobs here and the models and the controller, and then you have the lab where you define, you know, the whatever generator you might need if you want to generate something.

**Jacopo Beschi:** And then you, here you expose the basic methods, if you need, and here you're not going to put the client, the client is going to live here.

**Jacopo Beschi:** Like, it's going to be something similar to, yeah, so for example, here, what I did was like, depending on the services,

**Jacopo Beschi:** We use the same service, we just go on our API, so you don't need the separation, but you're to have one client, and so you're going to have, for example, this, this is going to be the client class, in this case, the trigger method and the status methods, and then internally, it's going to do whatever it needs to do, it's going to read, you can have a shared config if you want or not.

**Jacopo Beschi:** We can decide that later, and it's going to do the HTTP call, and return basically the hash, that's what it needs to do, and concerning the library to use, I don't know, but if it's something, something like simple HTTP calls, where you don't need persistent connection, you can even use just net HTTP, you know, because the way it is going to be working here, is that you don't need to, don't need and

**Jacopo Beschi:** Makes sense.

**Jacopo Beschi:** Have a pull, connection, connection pull, sorry.

**Jacopo Beschi:** I mean, not connection pull, but a pull of, you don't need to do parallel requests, okay?

**Jacopo Beschi:** Here, you just, you just client figure, that's one HTTP request.

**Jacopo Beschi:** Yeah, yeah.

**Jacopo Beschi:** It's not a performance concern, right?

**Jacopo Beschi:** And here, too.

**Jacopo Beschi:** And so, what you can do, if you want to make it faster, is use persistent connection and have a connection pull, but I don't think it's an issue in our case, right?

**Jacopo Beschi:** So, for example, in this library, you need to do a ton of requests.

**Jacopo Beschi:** So, the way it works is that it basically uses a connection pull, like, it's a session, HTTPX, for example, this was a session.

**Jacopo Beschi:** You call this a session, I think.

**Jacopo Beschi:** It's the, no, I call it a

**Jacopo Beschi:** Like, how many connections you're going to have, if you want to keep a persistent connection, and you basically save the round trip of the TCP and shake.

**Jacopo Beschi:** That's what you save.

**Jacopo Beschi:** But in our case, we don't need that.

**Jacopo Beschi:** We can just use HTTP, in my opinion, just do the pull, if it makes sense.

**Jacopo Beschi:** Like, it's not a constant.

**Jacopo Beschi:** Like, what is slow here is the workflow process, right?

**Jacopo Beschi:** I don't think you're going to, yeah, the scalability issue is there.

**Jacopo Beschi:** In the app side, you only need to worry about processing the web book async, so you don't overload the web server.

**Daniel Lopes:** You can do that in the background job servers.

**Daniel Lopes:** But that's the only concern.

**Daniel Lopes:** And again, if you're going to receive a lot, a lot, a lot of requests, you can handle that via rate limiting.

**Daniel Lopes:** So maybe you can rate limit the, actually, web book, right?

**Daniel Lopes:** Yeah.

**Jacopo Beschi:** Of course, you need to implement something on the client, but I don't think it's going to happen.

**Jacopo Beschi:** It's not like, you know, if it was like MailChimp, where you need to send a newsletter to a million of users, and then, of course, in that case, maybe you have a webhook, like, oh, tell me when they opened the email, something like that.

**Jacopo Beschi:** And then when you send this massive amount, you're going have a massive amount to request on the way back.

**Daniel Lopes:** Yeah, okay, then you might need read limiting and such, but really, like, I don't see the concern.

**Daniel Lopes:** And if you have any issue, you can handle that, even live, because it's a job.

**Daniel Lopes:** You're going to have queuing it.

**Daniel Lopes:** In what case, you and I have, like, a performance degradation issue, yeah, probably nobody will complain.

**Daniel Lopes:** mean, I don't think it's going a problem.

**Daniel Lopes:** It's kind of similar to what we did at EFT, for example, if this and that won't have, like, queuing.

**Daniel Lopes:** Yeah, exactly.

**Daniel Lopes:** By the way, did you know Trevor?

**Daniel Lopes:** Yeah, oh, Trevor.

**Daniel Lopes:** I hired Trevor.

**Daniel Lopes:** Oh, did you work with Trevor?

**Daniel Lopes:** Did you overlap with him?

**Daniel Lopes:** No, but the thing is that he opened some issue back a month ago, he opened it, you know, three weeks, yeah, he opened this on August 24th, this issue, so I watched it, I looked at him, and I saw, like, IFTTT, and I thought, like, ah, Daniel worked with that, too, so I thought, like, oh, maybe they know each other, so that's why I asked, just for that.

**Daniel Lopes:** Yeah, yeah, so Trevor, he built the Know Your Company, CodeBase, with Jonas, it was a base camp, and then, and then he left, I joined IFTTT, joined Trevor, and that was the beginning of the remote culture at IFTTT, was like, okay, like, I was convincing the CEO, hey, I can't bring one of the base camp guys, they're really good at, like, communicating, asynchronously, you see that they will perform as good as the local folks.

**Daniel Lopes:** And then Trevor's success story.

**Jacopo Beschi:** And then I left GIFT, took over the company code base.

**Jacopo Beschi:** So I worked on the code base afterwards.

**Jacopo Beschi:** Yeah, small.

**Daniel Lopes:** Cool, man.

**Daniel Lopes:** This is super helpful.

**Daniel Lopes:** I really appreciate everything.

**Daniel Lopes:** It's very similar to how I was thinking, like how the gem could be structured.

**Daniel Lopes:** And in my mind, it does make sense to have a gem because the two projects are similar.

**Daniel Lopes:** And if we're planning to extract the framework anyway, all the Ruby or Rails apps, we could use the same infrastructure as well.

**Jacopo Beschi:** But do you have anything else I can answer?

**Jacopo Beschi:** Like, do you want me to show you anything?

**Jacopo Beschi:** Like, I want to make sure you have time as well.

**Jacopo Beschi:** Like I said, I'm good on time.

**Jacopo Beschi:** Yeah, but do you have any more questions?

**Daniel Lopes:** Because I'm sorry, I struggled a little bit following all the code.

**Daniel Lopes:** Yeah, it's a ton of code.

**Daniel Lopes:** Like, yeah.

**Jacopo Beschi:** Yeah, and I thought that I messed at you know, HBM.

**Jacopo Beschi:** No, this is my worst.

**Jacopo Beschi:** No, no, no, this is super helpful.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Yes, maybe I'll stop the share if you don't mind.

**Jacopo Beschi:** Yeah, yeah.

**Jacopo Beschi:** Share screen, okay.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** We'll send you an offer probably tomorrow.

**Jacopo Beschi:** I'll talk to Tucker and we can plan anything out.

**Daniel Lopes:** Like what can I answer?

**Daniel Lopes:** What can I show you to get you excited about the potential?

**Daniel Lopes:** First, I want to ask you a few questions that I've written down just to put curiosity mostly.

**Daniel Lopes:** I mean, I have a ton of questions.

**Daniel Lopes:** I don't want to ask all of them, right?

**Daniel Lopes:** So the more important ones.

**Daniel Lopes:** You can ask them.

**Daniel Lopes:** Okay.

**Daniel Lopes:** This is the most important thing is recruiting for me.

**Daniel Lopes:** Thanks.

**Daniel Lopes:** I appreciate it.

**Daniel Lopes:** One question is about the development process, like how this is organized.

**Daniel Lopes:** Like I know maybe what I'm going to do is going to be slightly different from the team.

**Daniel Lopes:** I'm just curious about the general process.

**Daniel Lopes:** Like you design something in linear, I suppose, and then you start from there and create a PR.

**Daniel Lopes:** How does it work generally?

**Daniel Lopes:** And then someone reviews this or you just merge straight away?

**Daniel Lopes:** Yeah, that's a good question.

**Daniel Lopes:** Like we're still figuring out all the processes in the company.

**Daniel Lopes:** And like the thing, and like now I think the team is finally at the size where I can start to have like the lanes and which team does what.

**Daniel Lopes:** And like the code bases are like different areas.

**Daniel Lopes:** like you're going to, like people are longer on a separate, on a certain area.

**Daniel Lopes:** So we have four lanes.

**Daniel Lopes:** So we have, we have three lanes.

**Daniel Lopes:** So we have three three So lanes.

**Daniel Lopes:** lanes.

**Daniel Lopes:** AI framework team and folks that are working on the converting that monolith that has all the workflows and how we build the temporal abstraction and all that, turning that into a reusable NPM package that you can instantiate new projects and creating the CLI tool to generate the workflow, like improving the CLI tool to generate the workflows, all that kind of stuff, packaging the API as well as a Docker container.

**Daniel Lopes:** So we have three people working on that, and then we have the four deploy folks that work with the clients.

**Daniel Lopes:** So sometimes we have a client that wants a specific workflow or their process is different than ours for content generation, for example, or for some other clients, we even do things that are not even content generation, like we work with Auth0, Okta, and then they, we do sales.

**Daniel Lopes:** For example, will send us a name of a client or a name of a prospect, we'll do the research on the prospect and generate the summary for them.

**Daniel Lopes:** Completely different.

**Daniel Lopes:** that's an AI workflow we do for them specifically.

**Daniel Lopes:** So we have a team that does that kind of like, oh, this client uses Sanity CMS or this client uses Webflow, like how do we integrate those things?

**Daniel Lopes:** And like they do all this kind of custom work for the client.

**Daniel Lopes:** So that's three people there as well, plus a PM.

**Daniel Lopes:** And they are, they run in two-week cycles, like almost like a traditional sprint, but they have more of the cycles.

**Daniel Lopes:** We don't have any retro anything.

**Daniel Lopes:** It's more like every week they do a sync to see what priority changed for which new clients or clients are coming soon.

**Daniel Lopes:** And then they do a priority calibration.

**Daniel Lopes:** The framework team, they don't run in cycles.

**Daniel Lopes:** They are just, we came up with like, there's a milestone.

**Daniel Lopes:** So we want to have a V01 ready by end of this month and start migrating our code base, existing monolith, into the new version of the framework.

**Daniel Lopes:** And they've been, they had like essentially a month of like exploration to figure out what are the things we need.

**Daniel Lopes:** Like we need rendering, we need like support for multiple LLMs, LLM providers.

**Daniel Lopes:** We need to be able to handle API calls to different third party stuff like Gina and all that.

**Daniel Lopes:** So like they spent a month like figuring out the different packages.

**Daniel Lopes:** like think of it like Rails, have like active support, active model, and you have all the different action view and all that stuff.

**Daniel Lopes:** So like we ended up with something similar, but for the LLM world.

**Daniel Lopes:** So they spent like a month just trying a bunch of different stuff.

**Daniel Lopes:** And now they're spending a month and a half making that work and migrating our existing workflows to the new version.

**Daniel Lopes:** So they are running more like loose.

**Daniel Lopes:** And then we have a product lane, which is like all the product engineers.

**Daniel Lopes:** And have

**Daniel Lopes:** And designers, and that we have the two products, Atlas, the internal content creation tool, and check that.

**Daniel Lopes:** Check that is Jose and Steven and Marcel, our CEO.

**Daniel Lopes:** And they are, Marcel essentially, Marcel and I came up with like the rough, like here's what we're going to build.

**Daniel Lopes:** And the guys are like going with it.

**Daniel Lopes:** And there we run essentially very similar to the shape-up cycles.

**Daniel Lopes:** And we're doing four-week cycles and two weeks cooldown.

**Daniel Lopes:** And deciding whatever is shippable in that period.

**Daniel Lopes:** So for check that, what are we going to have is shippable for our first cycle.

**Daniel Lopes:** Actually, the first cycle ends next week.

**Daniel Lopes:** Will be a public version of the website.

**Daniel Lopes:** Like you can't log in on anything.

**Daniel Lopes:** Would log in would be like a wait list.

**Daniel Lopes:** But the idea is just push it live for Google to start indexing.

**Daniel Lopes:** And then...

**Daniel Lopes:** The following cycle, we're going to open up for clients to log in and track their prompts and all that.

**Daniel Lopes:** So two cycles there, we're thinking will be the, this one we're probably not going to do a cool down because it's not going to be like users trying things.

**Daniel Lopes:** It'll be more like, okay, we're done with this milestone, move to the next one, which is like finish the private area.

**Daniel Lopes:** So two folks there, plus Marcel, plus me sometimes.

**Daniel Lopes:** And then we have Apples, where most of the team is.

**Daniel Lopes:** And that's where we have multiple features and we're running the team in cycles as well.

**Daniel Lopes:** So we have two, we have one designer and one engineer, Pedro, working on an analytics area where you fetch data from Google Search Console and Google Analytics, combine everything and display to the, and they are running like four, same cycles, like four week cycles.

**Daniel Lopes:** They're to be done before, so like they're wrapping up this week.

**Daniel Lopes:** They're going to have one week of QA and polishing.

**Daniel Lopes:** They're

**Daniel Lopes:** And then they would be in cool down because there's other little things that they want to do.

**Daniel Lopes:** And then I'm working with Brad on another feature together.

**Daniel Lopes:** So I'm acting as a designer and he's acting as the programmer.

**Daniel Lopes:** And I'm also coding full stack on the thing with him.

**Daniel Lopes:** So we're split in like three pods on the product lane.

**Daniel Lopes:** Check that and two pods on Atlas.

**Daniel Lopes:** And so that's kind of the structure.

**Daniel Lopes:** And then we have, I can show you real quick, our linear.

**Jacopo Beschi:** So I was there when Ryan and Jason were thinking about the shape-up stuff.

**Jacopo Beschi:** So like I, and they were thinking about the process.

**Jacopo Beschi:** I'm very much aligned, but we use linear.

**Jacopo Beschi:** I don't love linear.

**Jacopo Beschi:** It's just that the integration of Slack is so good.

**Jacopo Beschi:** Let me pop.

**Daniel Lopes:** So we have here, we have essentially a rough roadmap where we have like a nice box of ideas, we have a backlog, and we have the stuff that we work in the cycle, so we have all this potential things, and then we have projects are the things that are actually happening.

**Daniel Lopes:** So inventory is the project that I'm working with Brad, check that is the project with Jose and Steven, and you can see here, status update, Jose usually posts every Friday, with screenshot, like very similar to the stuff that you guys had.

**Daniel Lopes:** We had the check-in, at least twice a week we had to do check-in, and then we had the project status updates that are not weekly, you can decide when you want to do them, as long as you do the check-ins to update.

**Daniel Lopes:** Right.

**Daniel Lopes:** More granular status, it's fine.

**Daniel Lopes:** But, yeah, I got you.

**Daniel Lopes:** Yeah, very similar idea.

**Daniel Lopes:** So we have, like, a pitch doc on other documentation inside of the notion.

**Jacopo Beschi:** have a channel for every project and a GitHub branch.

**Jacopo Beschi:** So we do, like, long-lived branches throughout the cycle instead of, like, continuous merge just to be easier to review things.

**Daniel Lopes:** Very similar to what David does for some larger stuff.

**Daniel Lopes:** And then the pitch doc is very much the same style where we have – this one doesn't have screenshots, actually.

**Daniel Lopes:** It has screenshots.

**Daniel Lopes:** The scope map is converted to milestones.

**Jacopo Beschi:** So those are the milestones in linear, very similar to the to-do list in Basecamp.

**Jacopo Beschi:** So let's say this case issues here.

**Jacopo Beschi:** We have the milestones of the probing, public directory, sign-up, and the stuff that is on school.

**Jacopo Beschi:** So that's, it's very, pretty similar to probably how you guys, guys worked.

**Jacopo Beschi:** Yes, yes.

**Jacopo Beschi:** I was about to ask about the big PR versus small PRs.

**Jacopo Beschi:** then, yeah, the general approach.

**Jacopo Beschi:** What's your feeling there?

**Jacopo Beschi:** Like, that's something that I've actually, like, introduced bigger PRs recently.

**Jacopo Beschi:** Like, because that's how we worked at IFTTT and Kanopy.

**Jacopo Beschi:** And, like, folks were merging things constantly before.

**Jacopo Beschi:** And, like, I just added cycles to the product team as well.

**Jacopo Beschi:** This is the first cycle that's going come to me.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** My take is that if you're building a new feature, for example, new functionality, whatever, it's easier to review and to see the bulk of changes with a one big PR.

**Jacopo Beschi:** And so I generally prefer that.

**Jacopo Beschi:** Approach versus a lot of small PR where you don't get the whole context.

**Jacopo Beschi:** There are some cases where small PR makes sense.

**Jacopo Beschi:** And it's when you're doing, especially when you're doing something less related to specific feature, more of like a migration approach or something like that that is naturally divided into multiple steps.

**Jacopo Beschi:** So, for example, back then, like a few years ago, I did some work to, we had an incident in Basecamp where we basically lost data from Redis.

**Jacopo Beschi:** Nobody figured out why in the Ops team, why that happened, but we lost data.

**Jacopo Beschi:** So we were used to store some data that is not a theme running Redis.

**Jacopo Beschi:** Like, I don't know if you ever used Basecamp.

**Jacopo Beschi:** Okay, you did.

**Jacopo Beschi:** Like, okay, for example, things like...

**Jacopo Beschi:** years.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** Yeah, I wasn't expecting that answer, but yes, just in case.

**Jacopo Beschi:** Anyways.

**Jacopo Beschi:** For example, the theme color and some settings that they were stored in Redis, right?

**Jacopo Beschi:** David implemented that in this way and he said, it's fine.

**Jacopo Beschi:** I mean, you can lose that information.

**Jacopo Beschi:** Well, turns out that when we actually lost that information was not something we could lose, like, without issues, like, you know?

**Jacopo Beschi:** so we spin off a work to migrate, basically, all the data, non-ephemeral, stored in Redis from Redis to the database.

**Jacopo Beschi:** And so in this case, where you basically have a bunch of application code base spread across different parts of the application, right?

**Jacopo Beschi:** It's not, like, one single feature.

**Jacopo Beschi:** have, like, notification logic.

**Jacopo Beschi:** You have theme settings.

**Jacopo Beschi:** You have whatever else.

**Jacopo Beschi:** It was, like, 20 different features, right?

**Jacopo Beschi:** And you need to change each of them.

**Jacopo Beschi:** In this case, it makes sense to just split the work in 20 whatever PRs and handle the deploy and the migration for each one separately because making one big PR is not going to work because you need to also take care, for example, of data migration, right?

**Jacopo Beschi:** So you need to have multiple steps, like one step where you basically read the, I mean, you can't just do one step migration because you're going to have some time where you don't have the data, right?

**Jacopo Beschi:** So you need to have like a double read, like read from the Redis database and read from the database, sorry, read from the database and for Redis as a fullback.

**Jacopo Beschi:** And that's the first thing that you deploy.

**Daniel Lopes:** Then you have like also with the same deploy, the data migration, you need to copy the data over from Redis to the database.

**Daniel Lopes:** And then you have to have the second deploy that is, okay, we migrated all the data, it's working fine.

**Jacopo Beschi:** Let's just cut off the part reading from the Redis.

**Jacopo Beschi:** And then you're going to also clear the Redis store, right?

**Jacopo Beschi:** Because you don't want to waste that space.

**Daniel Lopes:** Because it's not going to be evicted automatically.

**Jacopo Beschi:** It's not like a cache that is going to be evicted.

**Jacopo Beschi:** And you do it for each part of the app.

**Daniel Lopes:** And you want to deploy this separately.

**Daniel Lopes:** Because if you deploy all the changes together, it's going to be a pain.

**Daniel Lopes:** So this work makes sense.

**Daniel Lopes:** This kind of more infrastructure-related work makes sense to be split across multiple steps naturally.

**Daniel Lopes:** But a feature that is like, this is the old feature.

**Daniel Lopes:** You want to see this all together.

**Daniel Lopes:** Do you want to see the old code, all the code, sorry, together?

**Daniel Lopes:** And you want to play with it together.

**Daniel Lopes:** And it makes sense using one branch for that.

**Daniel Lopes:** And just...

**Daniel Lopes:** agree.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Sorry, I'm a bit tired.

**Daniel Lopes:** So I'm not explaining myself properly, but I hope you understand.

**Daniel Lopes:** No, 100%.

**Daniel Lopes:** Okay.

**Daniel Lopes:** I'm curious about the development environment.

**Daniel Lopes:** If you have any requirements.

**Daniel Lopes:** And I've noticed you use a Mac.

**Daniel Lopes:** I use a Mac too.

**Daniel Lopes:** Is it okay to use a Mac?

**Daniel Lopes:** Yeah, no, definitely.

**Daniel Lopes:** Like, I would prefer Mac.

**Daniel Lopes:** And we're still, like, we used to require folks to use cursor before because we were, at least for the framework, because we had a bunch of cursor rules that, that kind of stuff that I was showing you with, like, how to work with prompts, how to work with the, APIs and all that was done for cursor specific.

**Jacopo Beschi:** And cursor had, was the first AI coding editor that had the ways for you to define the rules.

**Jacopo Beschi:** But we're moving out of cursor to be cloud code focused.

**Jacopo Beschi:** So, and cloud code, you can trigger from anything.

**Jacopo Beschi:** So you can trigger from terminal, you can trigger from VS code.

**Jacopo Beschi:** VS code, they have a browser extension that has UI.

**Jacopo Beschi:** But if you're using NIL, or if you're using terminal, No.

**Jacopo Beschi:** They have the terminal interface, and they're all going to use the same rules.

**Jacopo Beschi:** So for coding workflows, that's the only thing that we have that's atypical, it's just like probably like we have to use cloud code.

**Jacopo Beschi:** And then web, like the development wise for the other areas, Mac ideal, in my opinion.

**Jacopo Beschi:** And then we have one person that I think uses Windows.

**Jacopo Beschi:** I think that, I think Stefano uses Windows, but I think we got him on Mac.

**Jacopo Beschi:** He should be using Mac, I think.

**Jacopo Beschi:** If I can give you an advice, it's good to have like, didn't meant to interrupt, but I forget stuff.

**Jacopo Beschi:** So I just, I'm sorry.

**Daniel Lopes:** I have this bad attitude of interrupting people.

**Daniel Lopes:** Sometimes I know it's annoying, and please say so like it is.

**Daniel Lopes:** It's not annoying at all.

**Daniel Lopes:** But sometimes I forget things, I want to say them rapidly.

**Daniel Lopes:** So if it matters, my honest, humble opinion is that if we have in the team, like in the company at least, know think.

**Daniel Lopes:** I if I

**Daniel Lopes:** One person that uses Windows, it's very good to test the UI because sometimes when you expose this to the public, I mean, in the future when we're going to expose the, you know, the Atlas or the apps also to the public, you want to make sure it looks good also on Windows because like most of the customers are going to be on Windows, like probably 60% or something like that.

**Jacopo Beschi:** I don't know the exact number, it depends, but you know, and sometimes you code on Mac and it depends also on Basecamp that designers were using Mac, everybody was using Mac and then you take a look on Windows, on Basecamp, it's like, yeah, yeah, it's not as good, you know, so you want to have someone testing also on Windows, that's my honest advice.

**Jacopo Beschi:** Yeah, no, no, I agree, yeah, so like, I think, yeah, so like Mac is ideal, it's what everybody gets when they join, so like, I think we have, that's the standard laptop we have, and then we have for development.

**Jacopo Beschi:** So the happy path for Rails, for the Rails apps is not non-Docker, but I know some folks use Docker for development as well.

**Jacopo Beschi:** That's one thing that would be, like if you were to join, it would cool to align is have you help us polish the setup of a new app and like document and like come up, have us come up with the happy path and that's the standard way and like have seeds and all that stuff.

**Daniel Lopes:** I so I know what I did a little bit of that, yeah.

**Daniel Lopes:** Yeah, Basecamp we have like a bin setup that is in hold of doing everything.

**Daniel Lopes:** had, basically we had a company tool called Shipyard, which is going to set up the Mac.

**Daniel Lopes:** So you just run Shipyard, it's going to install whatever you need to install, like VPN setup, everything on the Mac.

**Daniel Lopes:** And then for each app, you just run BIN Setup.

**Daniel Lopes:** It's going to install all the dependencies and install Ruby, upgrade Ruby if it's needed, install whatever you need.

**Daniel Lopes:** And then you do BIN Dev to boot the app.

**Daniel Lopes:** That's the approach.

**Daniel Lopes:** And it runs on Metal, not on Docker, usually.

**Daniel Lopes:** But for the legacy apps, like we have some, like PaceCamp 1, they run on Docker because it's difficult.

**Daniel Lopes:** Yeah, it's difficult to run on Metal.

**Daniel Lopes:** Yeah, no, it makes sense.

**Daniel Lopes:** Yeah, so that's it.

**Daniel Lopes:** And like this stack is just the problem, probably the thing that would be, that would take you a bit to learn.

**Daniel Lopes:** So it would be, we have TypeScript, so the front-end stack.

**Daniel Lopes:** So the true stack stack, the AI stack, we decided that the standard that everybody will use is Python.

**Daniel Lopes:** We made a decision to go with TypeScript instead because if we are, like the plan was to make this open source,.umuz.

**Daniel Lopes:** So

**Daniel Lopes:** But also to, the end goal is to create an environment similar to Lovable or Boat or VZ, I don't know if you've played with these tools, that you can.

**Daniel Lopes:** No, I'm sorry.

**Daniel Lopes:** Yeah, these tools are you essentially can create an app from scratch and it deploys the app for you.

**Daniel Lopes:** And that enabled people like Marcel or marketers or any person to create an app if the app is simple enough.

**Daniel Lopes:** But it is so instrumented on top of React that React works great.

**Daniel Lopes:** So it knows how to create a React app.

**Daniel Lopes:** So our AI framework, the goal is to do the same, but for AI workflows.

**Daniel Lopes:** And TypeScript just happens to be really good because it has types definition and all that stuff.

**Daniel Lopes:** And it's great for AI.

**Daniel Lopes:** So AI code generation.

**Daniel Lopes:** So we made all the technical choices off of like what can be auto-generated as close to ready as possible.

**Daniel Lopes:** And what is the language that...

**Daniel Lopes:** Everybody uses that doesn't require a shift of like, if you're using Next.js, if you're using other things, and you want to build an AI feature, might as well just be your workflow in the same language.

**Daniel Lopes:** So we ended up going with TypeScript for that reason, and Temporal has a great integration of TypeScript.

**Daniel Lopes:** So that side is TypeScript, and the front end of our Rails app are all in React with TypeScript as well.

**Daniel Lopes:** That was kind of a painful choice, because like I used Hotwire and Turbo, and like I've used the standard vanilla Rails.

**Daniel Lopes:** That was my preference most of my career.

**Daniel Lopes:** We just got to the point where like AI is so good with React code base.

**Daniel Lopes:** It's essentially fine-tuned for that, especially Claude.

**Daniel Lopes:** And you can move so fast on the front end side that it makes...

**Daniel Lopes:** So we have React, but we treat it as Turbo, where we have controllers, we use this thing called Inertia, which is the Turbo equivalent of Laravel, that we will render, every route will render a React page with the JSON serialized from the Rails side.

**Daniel Lopes:** So it's essentially the same, and it will do like, as you navigate, as you click around, it will replace the areas that change, just like Turbo links would do to replace the areas that change.

**Daniel Lopes:** So we use React on the front end, and TypeScript as the language.

**Daniel Lopes:** Let's just stack, database, use Postgres for everything, deploy server, we're using render for everything, but I don't know if you've seen render, render.com.

**Daniel Lopes:** It's very, so much of it, real cool, but...

**Daniel Lopes:** Okay.

**Daniel Lopes:** And yeah, but I don't know if we're going to be able to stay on that for forever.

**Daniel Lopes:** We're going to have to move to AWS or something eventually.

**Daniel Lopes:** So there's no ops team now?

**Daniel Lopes:** It's just a developer taking care of everything, right?

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** The folks on the AI infra team, they are more ops than the...

**Daniel Lopes:** So we have one of the early developers from Terraform is on the team.

**Jacopo Beschi:** And we have also one person that is pretty advanced with all the different AWS services and Kubernetes as well.

**Jacopo Beschi:** But they're coding the framework, the AI framework.

**Jacopo Beschi:** That one would be an interesting area to get your help to have one more person.

**Jacopo Beschi:** Even though you haven't done a lot of TypeScript work or AI work, it would be nice to have your library mindset and the taste for good, well-designed...

**Jacopo Beschi:** And framework to, to support there.

**Jacopo Beschi:** We're expecting to do like a big, like if you were to join, the two areas you probably would need your help would be the project that Jose is working on.

**Jacopo Beschi:** He's going to go in paternity leave soon.

**Jacopo Beschi:** So next month.

**Jacopo Beschi:** Jose?

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Oh, wow.

**Jacopo Beschi:** No, I didn't know that.

**Jacopo Beschi:** It's second.

**Daniel Lopes:** Yeah.

**Jacopo Beschi:** Second kid.

**Daniel Lopes:** No, I'm done with that.

**Daniel Lopes:** I got, I don't know if I told you like, this is, I got my second one and it's like, I'm done.

**Daniel Lopes:** My wife still thinks about, because I have two songs and my wife thinks about, oh, I miss a daughter, but on the other end, she's like, I'm too old and it's too tiring.

**Daniel Lopes:** My oldest is five years and a half and the youngest is six months now.

**Daniel Lopes:** So it's going to be seven months at 24th.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** But the thing, as I told you, the pregnancy was very tough for us because she had some issues and also the kid initially was not growing well.

**Daniel Lopes:** So it was very, very tiring and tough for all of us.

**Daniel Lopes:** And I love my kid and he's so nice and he sleeps always and he's the best kid you can ever have.

**Daniel Lopes:** But I think I'm done.

**Daniel Lopes:** There was a study that they surveyed people, how they feel about pregnancy and having a child in their first year and everybody has the same reaction.

**Daniel Lopes:** then two years later, they forget and they have another one.

**Daniel Lopes:** So that was a sensation in that.

**Daniel Lopes:** Everybody's like, done.

**Daniel Lopes:** And then two years later, okay, like everybody's having their second and third.

**Daniel Lopes:** Yeah, I hope that makes sense.

**Daniel Lopes:** Oh yeah, so like check that.

**Daniel Lopes:** So probably, we're probably going to have to pull more help.

**Daniel Lopes:** Jose is out.

**Jacopo Beschi:** Probably going to have like some of the other product guys join.

**Jacopo Beschi:** And if you were to join, we probably need your help to review whatever they do as well there.

**Jacopo Beschi:** That's the thing that I was thinking, like you being in the Italy time zone, you kind of overlap with a lot of the other folks that are in the East Coast.

**Jacopo Beschi:** So it wouldn't be a problem at all, even if we're doing like product stuff, because you overlap with like, we have in Italy, for example, as well.

**Jacopo Beschi:** So, and he's one of our product designers.

**Daniel Lopes:** So if you could help on product engineering, that would be a nice setup.

**Daniel Lopes:** then whenever we need, one thing that would be super helpful to get your take on it would be like on every larger, like let's say end of cycle that we're like merging, or every like large architecture decision, like there's this scraping stuff that you were just seeing from Brad.

**Daniel Lopes:** That would be nice to have you like review SPR and like share your take and stuff like that, regardless if you're on the project or not.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah, I hope that makes sense.

**Daniel Lopes:** Definitely, definitely.

**Daniel Lopes:** Yeah, that's cool.

**Daniel Lopes:** Did use, like, single database server or you replicated Postgres now?

**Daniel Lopes:** Because I'm thinking about, like, long thinking, like, long term.

**Daniel Lopes:** Because, for example, at some point, you might need, I mean, you might need to scale and then you might need to use replica, but right now you don't need them.

**Daniel Lopes:** I'm just curious, you know, you're not using any verification.

**Daniel Lopes:** Just single, okay.

**Daniel Lopes:** No, we have two Fs, so, with databases.

**Daniel Lopes:** The client UI that you see the Temporo job is executing, that has no database.

**Daniel Lopes:** That one, the Temporo has the database itself, and they handle that to their cloud provider.

**Daniel Lopes:** Temporo is open source, so it could self-host, but we have it, we use their cloud version.

**Daniel Lopes:** Right.

**Daniel Lopes:** Instead of self-hosted.

**Daniel Lopes:** Database, have two Postgres, like, one for check that and another one

**Daniel Lopes:** And Render has all the traditional backups and everything handled automatically, but no replicas.

**Daniel Lopes:** We do have Snowflake with cloning the database daily for analytics purposes.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** I was about to ask what you use Snowflake for because I was a little bit scared.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So we use Snowflake for, right now we don't even have the BI tool on top, but we're running, we're to run a study on extracting, like scraping a bunch of pages and running daily all the things that we're probing on CheckDat.

**Jacopo Beschi:** We're going to scrape the results and analyze the pages.

**Jacopo Beschi:** And like, what are the things that make, increase the probability of a page to, to be, uh.

**Jacopo Beschi:** Mentioned or not.

**Daniel Lopes:** So all the data is getting sent to Snowflake for a data scientist to create a logistic regression model for probability.

**Daniel Lopes:** You can basically analyze search engine behavior.

**Daniel Lopes:** Yeah, that's the goal.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And then we're going to publish as a page on check that.

**Daniel Lopes:** It's like, here's the current state of how LLMs are behaving.

**Daniel Lopes:** So if you had an FAQ or if you had a TLDR, increases the change, that kind of stuff.

**Daniel Lopes:** So let's see how that goes.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** What else can I answer?

**Daniel Lopes:** No, I'm okay.

**Daniel Lopes:** On call, you mentioned like back support on call.

**Daniel Lopes:** In Biscount, we had like the on call week where each programmer is, for one week, his on call is going to take care of basically all the, level two tickets.

**Daniel Lopes:** Do you?

**Daniel Lopes:** How do you handle the support tickets?

**Daniel Lopes:** Yeah, so we have, that's something we just added.

**Daniel Lopes:** So we had to on-call.

**Daniel Lopes:** The way we have today the team structure is that we have all the people doing the content creation.

**Daniel Lopes:** They are our users.

**Daniel Lopes:** So any bug that they have or any challenge that they have, they will file a ticket in linear to the, we have a Slack channel where they file linear tickets through Slack.

**Daniel Lopes:** And that is an inbox for the client ops team.

**Daniel Lopes:** So they are the first line of defense.

**Jacopo Beschi:** And if there are product issues, like if there's like a bug on Atlas or if there's like a bug on CheckNet, that would be like a ticket that we either would see through Sentry as an exception, or we would get a ticket report from one of our teammates to the client ops.

**Jacopo Beschi:** And they would pass that to the other side, to the product lane.

**Jacopo Beschi:** And we usually, we're thinking about, like, the way we're doing now, it's like we have one of the folks there on the cycle be the point of contact.

**Jacopo Beschi:** But we don't have the own call for, like, at down mid of the night.

**Jacopo Beschi:** I'm the only person on call for that.

**Jacopo Beschi:** So I'm going to, I get the first pager duty.

**Jacopo Beschi:** We're small enough.

**Jacopo Beschi:** But, like, it hasn't happened much.

**Jacopo Beschi:** So, and sometimes Marcos will pick up, he's in Portugal.

**Jacopo Beschi:** So he'll, like, get the other shifts automatically.

**Jacopo Beschi:** He will notice when things are down.

**Jacopo Beschi:** So, but I'm the U.S.

**Jacopo Beschi:** or the first line of defense for app down.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Yeah, well, the thing is that when you, now that most of the customers are internal, it's completely fine.

**Daniel Lopes:** But if one day you're going to expose the load, I mean, it's going to change a lot.

**Daniel Lopes:** Because, yeah, that's going to change the next month.

**Daniel Lopes:** Yeah, because you're going to have, like, customer.

**Daniel Lopes:** Input, not prepared customer input.

**Daniel Lopes:** My old colleague told me this, if you ask a mechanic to drive a car, it's not going to break it.

**Daniel Lopes:** But if you ask somebody else to drive a car, it's going to break it.

**Daniel Lopes:** Because the mechanic knows how the car works, knows how to break it, if it makes sense.

**Daniel Lopes:** So if a power user uses a tool, he knows how to use it, it's not going to break it.

**Daniel Lopes:** Or you know where it breaks, it's not going to break it anyway.

**Jacopo Beschi:** But if you open to the public, I mean, of course, I don't imagine things like, you know, in Basecamp where you have millions of users, a few minions, not that many, but still enough to do very weird edge cases or to have very weird issues.

**Jacopo Beschi:** But still, it's going to open a lot of doors for issues.

**Jacopo Beschi:** I think check that will be like that.

**Jacopo Beschi:** So that was kind of like, if it was like this, where like, at 10 million users, or like every...

**Jacopo Beschi:** If is like 30 minutes, it would be enough for the change to show up as a bug.

**Jacopo Beschi:** So I think check that, we're probably going to have thousands of users in the first month, I'm pretty sure.

**Jacopo Beschi:** Because that's what some of the competitors that we're competing with there get.

**Jacopo Beschi:** And our goal there is to ship a product that is essentially free, and the competitors are charging $1,000 a month.

**Jacopo Beschi:** so we expect to get a ton of demand there.

**Jacopo Beschi:** Wow.

**Jacopo Beschi:** Yeah, so that's why I'm like, oh, Jose is going to have opportunity to leave.

**Jacopo Beschi:** We're probably going to have to put most of the team there anyway, so for the launch.

**Jacopo Beschi:** The launch is the painful, more painful part.

**Jacopo Beschi:** I know because in this camp, every time there is a launch, it's a pain.

**Jacopo Beschi:** Like when they launched the launch date, it was a mess.

**Jacopo Beschi:** When they launched the calendar, it was a mess.

**Jacopo Beschi:** And now they're going to launch a new product in the future.

**Daniel Lopes:** And it's going to be every time there is.

**Jacopo Beschi:** The first, like, at least two or three weeks, at least even three weeks, probably, is going to be a lot of problems.

**Jacopo Beschi:** Like, the first weeks, for sure, but then also the following couple of weeks, it's going to be a lot of issues raising.

**Jacopo Beschi:** No, I was asking about the on-call because there was this issue in Basecamp where, you know, they have product programmer and they have SIP team.

**Jacopo Beschi:** Back in the days, the SIP team were the only people on-call.

**Jacopo Beschi:** So the programmer were only just, the product programmer would only be a new feature.

**Jacopo Beschi:** So what happened was that the product programmer, sometimes, to cut the scope, they cut the scope on error handling and potential issues.

**Jacopo Beschi:** And so the SIP team was on hold of taking care of all of them.

**Jacopo Beschi:** And I remember Rosa was, like, very tired because of that.

**Jacopo Beschi:** And Jorge, I don't know if you know him, but his ex-collegue was very tired of those things.

**Jacopo Beschi:** So he proposed, okay, now on-call needs to be handled by everyone, also by the product programmer.

**Daniel Lopes:** So they care more, you know, about...

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** If you can feel the pain, you need to feel the pain to actually take care of these at the design phase.

**Daniel Lopes:** Because if you've got to cut the scope, and it's very easy to cut the scope on things that get unnoticed when you show something, like the error handling, especially some edge cases, it's very easy to cut the scope there.

**Daniel Lopes:** But then somebody needs to take care of them.

**Daniel Lopes:** Yeah, sorry for the digression.

**Daniel Lopes:** No, 100%.

**Daniel Lopes:** Something very funny is also that Atlas.

**Jacopo Beschi:** Yeah, sorry.

**Jacopo Beschi:** Sorry, I was about to say something, but it's not important.

**Jacopo Beschi:** Yeah, I think I don't have any more questions, more important ones.

**Jacopo Beschi:** I mean, you answered all of them very clearly.

**Jacopo Beschi:** And I really appreciate, I mean, all the time you spent with me.

**Jacopo Beschi:** I know you're a busy person, so it matters a lot for me.

**Jacopo Beschi:** Sorry if I interrupted you a lot.

**Jacopo Beschi:** No, no, no.

**Jacopo Beschi:** No, don't worry about that.

**Jacopo Beschi:** I offend you or anything like that.

**Jacopo Beschi:** I'm just saying, no.

**Jacopo Beschi:** No, no, no.

**Jacopo Beschi:** I'm the same.

**Jacopo Beschi:** Let me think if there's anything else.

**Jacopo Beschi:** Yeah, let me know if there's anything else you need to talk to more.

**Jacopo Beschi:** Anybody else?

**Jacopo Beschi:** Anything?

**Jacopo Beschi:** I'll talk to Tucker.

**Jacopo Beschi:** I don't know how much you shared with him.

**Jacopo Beschi:** Where are you in your research process?

**Jacopo Beschi:** And if you were to join, when would you be able to start?

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** The search process.

**Jacopo Beschi:** mean, I told you the last time that basically what happened was that I left Basecamp and the week after I spoke with you.

**Jacopo Beschi:** And I was not happy to searching anything because it was like I need a little break before doing anything else.

**Jacopo Beschi:** After four years of uninterrupted work and also previously five years, same thing.

**Jacopo Beschi:** never had the chance to take a break.

**Jacopo Beschi:** Take a break.

**Jacopo Beschi:** Let's take a little break before starting to look for a new job.

**Jacopo Beschi:** But then Rosa just sent me an email.

**Jacopo Beschi:** I mean, I left on Monday, I think, and Rosa sent me an

**Daniel Lopes:** You know, Thursday, and I was like, okay, what are going to do?

**Daniel Lopes:** What are you going to do?

**Daniel Lopes:** Okay, I'm going to try, because I'm just curious.

**Daniel Lopes:** I don't want to lose the opportunity, you know, if it makes sense for you.

**Daniel Lopes:** So I really like to join, but I really also like to take a few weeks to recover, you know?

**Jacopo Beschi:** Yeah, for sure.

**Daniel Lopes:** Especially my wife asked me that too.

**Jacopo Beschi:** Yeah.

**Daniel Lopes:** Because she said I was, like, not at my 100% in the last few months due to, you know, what happened with the family, the work, and so on.

**Daniel Lopes:** I bet.

**Daniel Lopes:** So I haven't thought about starting it yet, but a few weeks to break.

**Daniel Lopes:** My wife asked for a month, maybe we can do three weeks.

**Daniel Lopes:** I don't know if you can negotiate that.

**Daniel Lopes:** Yeah, yeah, for sure, for sure.

**Daniel Lopes:** Yeah, but I want to start, like, next week.

**Daniel Lopes:** Next week is impossible.

**Daniel Lopes:** I need to wait a little bit for my, you know, I want to start 100%.

**Daniel Lopes:** And now I'm not 100%, to be completely honest with you.

**Daniel Lopes:** I'm, like, 80%, 70%.

**Daniel Lopes:** I need to relax a

**Jacopo Beschi:** Yeah, I can't imagine that.

**Jacopo Beschi:** Yeah, I was just going to say that, like, Jose is scheduled for November 15th, Caesarean.

**Daniel Lopes:** So probably it would be ideal to join, like, at least like a week before he leaves.

**Daniel Lopes:** So you guys are probably going to it.

**Daniel Lopes:** So November 3rd, you mean?

**Daniel Lopes:** Yeah, something like that.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Let me think if there's anything else.

**Jacopo Beschi:** Yeah, so, yeah, the time zone is not a problem.

**Jacopo Beschi:** Roles, like the role that I was like, titles and stuff like that, we're still pretty, like, early.

**Daniel Lopes:** But we, yeah, we don't have, like, hard titles yet.

**Daniel Lopes:** So that's something I'm probably going to add next year once we have everybody in place.

**Daniel Lopes:** Let me see if there's anything else.

**Daniel Lopes:** Any other questions or?

**Daniel Lopes:** I mean, I spoke with Tucker right about, he told me that you have a 20-day PTO, right?

**Daniel Lopes:** I wonder if...

**Daniel Lopes:** It's flexible, whatever you want.

**Daniel Lopes:** We recommend people to take at least 15 days.

**Daniel Lopes:** That's kind of like, please do it.

**Daniel Lopes:** But it's like, we have flexible vacation.

**Daniel Lopes:** Okay.

**Daniel Lopes:** No, because my question was like, for example, national holidays, like Christmas, Easter, and stuff like that.

**Daniel Lopes:** If I stay home, I need to use my PTO for that.

**Jacopo Beschi:** Is it correct?

**Jacopo Beschi:** You don't handle it?

**Jacopo Beschi:** No, you can...

**Jacopo Beschi:** Yeah, we don't track that.

**Jacopo Beschi:** So take whatever you want.

**Jacopo Beschi:** We usually have...

**Jacopo Beschi:** I don't know if we're going to do this year, but we used to do two weeks off by the end of...

**Jacopo Beschi:** The year, and we would just handle like on call.

**Jacopo Beschi:** So somebody would be on call for like part of that, but no active development or active work during that period.

**Jacopo Beschi:** I think we might do this year again.

**Jacopo Beschi:** I haven't talked to Marcel about that yet.

**Jacopo Beschi:** Yeah, but we don't track holidays either.

**Daniel Lopes:** So usually the American side would like take American holidays off.

**Daniel Lopes:** Like it was a holiday this week, but I worked, Marcel worked, some other folks were off.

**Daniel Lopes:** Yeah, I think like, yeah, I don't keep track of anything, to be honest.

**Daniel Lopes:** Like people, I think people just work hard, no matter what.

**Jacopo Beschi:** So if you hire the right people, so.

**Daniel Lopes:** Okay, because I was a little bit afraid, like my wife asked me like about the time off and so on, because for example, in Biscayne, we have the same thing, like 20 paid days, and then they say like, okay, you have 10 days that you can use for national holidays on top of that.

**Daniel Lopes:** For example, Christmas.

**Jacopo Beschi:** Massa, and I don't know, in Italy we have our own national holidays, so I was thinking, like, if I can take those days off, like, it doesn't need to be 10 days, but a few days at least for national holidays, and then, okay, you answered my question anyways.

**Daniel Lopes:** Yeah, we don't track.

**Daniel Lopes:** Like, in my mind, like, it has never been a problem.

**Daniel Lopes:** Like, I work with, like, Flexible Vacation on every company, and it was pretty much never happened that somebody abused as, like, taking a full month off straight or something like that.

**Daniel Lopes:** So it's more of a problem of people not taking enough, so we kind of have, like, at least, I'm also not tracking either, so, like, if people don't take, I'm not going to see it.

**Jacopo Beschi:** But they're just probably going to burn out by themselves.

**Jacopo Beschi:** So, try to take at least 10 days a year, minimum.

**Jacopo Beschi:** Yeah, whatever needs to be done.

**Jacopo Beschi:** And also, like, illness.

**Jacopo Beschi:** Usually, I'm never sick, but it happened that one day or two days I was sick.

**Jacopo Beschi:** can't do anything for that.

**Jacopo Beschi:** Okay.

**Jacopo Beschi:** No.

**Jacopo Beschi:** Okay, cool.

**Jacopo Beschi:** Funny enough, think, like, at Basecamp, I think the only person that...

**Daniel Lopes:** I think they probably get more strict over time with the time, the time, because I remember Trevor getting called out by, like, hey, you took four weeks straight, and then David was, like, not super happy.

**Daniel Lopes:** And I think after that, they added some limitations around that.

**Daniel Lopes:** But no, we don't have anything like that.

**Daniel Lopes:** That almost never happens.

**Daniel Lopes:** No, they have, like, you can take, like, five days off if you're sick.

**Daniel Lopes:** And then after then, after the five days, I think you have a salary cut of...

**Daniel Lopes:** You can...

**Daniel Lopes:** It takes 60% for up to one month, and then after one month, it's like 40%.

**Daniel Lopes:** If you have a very serious illness, like, I don't want to say any of them, but, you know,  happens.

**Daniel Lopes:** Then you can, maybe two, three months, I don't know exactly, at the 40%, something like this.

**Jacopo Beschi:** But I never was sick.

**Daniel Lopes:** I mean, it happened that I got COVID a few times, and I was not able to worry, but it's not common for me.

**Daniel Lopes:** But I was just asking in case, yeah, it's okay.

**Daniel Lopes:** Yeah, other stuff that we have, so we have, yeah, our salary, we try to pay close to San Francisco's salary.

**Daniel Lopes:** To me, it's like one thing that's really important for us is a sync communication.

**Daniel Lopes:** So, like, I don't think, like, that's the thing, like, with Basecamp, like, for you guys, is, like, music to do.

**Daniel Lopes:** That's the kind of second nature.

**Daniel Lopes:** For other folks, it's a little harder to get used to it.

**Daniel Lopes:** We do also, we have...

**Daniel Lopes:** So stock options, like any startup, I know Basecamp didn't have that, but they had the profit sharing.

**Daniel Lopes:** We don't do profit sharing yet because we don't expect to be, like we are break-even.

**Daniel Lopes:** This month we're actually broke-even.

**Jacopo Beschi:** It's pretty good for a startup.

**Daniel Lopes:** I mean, for a startup one year or something more old, break-even is very good.

**Daniel Lopes:** Yeah, so we're trying to, we're fighting, like we don't, like just to give you a little bit of context, like we're just going through, we had a ton of inbound investors last month.

**Daniel Lopes:** So we entertained an idea of like a Series B, and that's still kind of happening.

**Daniel Lopes:** We have a couple of investors that we're still going through the process with them.

**Daniel Lopes:** But we think if we're going to do that, we're probably going to, we're going to do it serious.

**Daniel Lopes:** Like if they, if they go through and they give us good terms, we probably would take it, but we didn't go on like a full-on multi-month.

**Daniel Lopes:** And so we want to stay in that realm where if we're going to burn, we burn just a little bit.

**Daniel Lopes:** So we're not dependent on investor money.

**Daniel Lopes:** But if there is a chance of getting good terms and something like $30 to $40 million in investment, then we would take it because we think there is a risk for an AI bubble or a recession.

**Daniel Lopes:** And we wouldn't want to have the company in the top spot because of that.

**Daniel Lopes:** But yeah, so we think like AI is legit game changer.

**Daniel Lopes:** It's not the same as blockchain or IoT.

**Daniel Lopes:** But there is a lot of money getting deployed, especially in Seed and Series A.

**Daniel Lopes:** and that money might dry out next year, end of next year.

**Daniel Lopes:** So that might change the dynamic.

**Daniel Lopes:** the space a little bit.

**Daniel Lopes:** So that's why we were like, okay, like their investors interested in on us, let's entertain idea.

**Daniel Lopes:** But I think the story will be like a lot different after we launch, check that and once we make Atlas be accessible by clients as well.

**Jacopo Beschi:** And after we make the output framework, open source.

**Daniel Lopes:** And those are the three things we have lined up for the next two to three months.

**Daniel Lopes:** So we're going to execute on that and see what happens after.

**Daniel Lopes:** But we're doing pretty well money-wise.

**Daniel Lopes:** We do have a lot of challenges, not going to lie to you.

**Daniel Lopes:** Because we are services first, a lot of the stuff we have to do to serve the services team.

**Daniel Lopes:** And like many times they will be overwhelmed until we get more clients than we can handle.

**Daniel Lopes:** So, and this is not a bad thing.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** And like, and they,

**Daniel Lopes:** They take the brunt of the challenge.

**Daniel Lopes:** So for us, it's more like how fast can we move to automate a lot of the work so they can breathe?

**Daniel Lopes:** So the Atlas team has a time pressure on like, , like the folks are about to burn out if we don't help them and launch this fast.

**Daniel Lopes:** So a lot of the things that I do, I did that in three minutes.

**Daniel Lopes:** It's essentially like cloud-coded as fast as possible to save like a couple of hours for the team that's onboarding clients every time they're onboarding somebody.

**Jacopo Beschi:** So there is like a lot of that need for like moving fast on Atlas.

**Jacopo Beschi:** On CheckNet is different.

**Jacopo Beschi:** So CheckNet is more like a traditional product.

**Jacopo Beschi:** So we have to move a little bit slower and like more careful.

**Jacopo Beschi:** But it's also like a heavily, the competition on that space is moving fast.

**Daniel Lopes:** So there's that kind of time pressure, but it's never from like, oh, we got to  this.

**Jacopo Beschi:** For just because I made up a date, it's more like, yeah, you see, we open Slack and folks are like, oh , like, I'm working 70 hours.

**Jacopo Beschi:** like, okay, we got to systematize the things for you to get you back to 40 hours on this client instead of that.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So the delivery team, the services team, depending on what we do, we make their life easier or their life is a mess, you know?

**Jacopo Beschi:** So it's a, the benefit of the product team should help.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** This is a transition phase, basically.

**Jacopo Beschi:** You need to move as quickly as possible to help them.

**Daniel Lopes:** And it also depends on the customer base if it keeps growing or at some point you're going to plateau or maybe just not, not, not go like, you know, linearly, but sublinearly.

**Jacopo Beschi:** Yeah.

**Jacopo Beschi:** Right.

**Jacopo Beschi:** Makes sense.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Cool, man.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** If you have any other questions, let me know.

**Daniel Lopes:** I'll let you go.

**Daniel Lopes:** I'm going to hold you for.

**Jacopo Beschi:** No, it's fine.

**Jacopo Beschi:** The computer, do you want me to use?

**Jacopo Beschi:** I have a computer, but I don't know if you want me to use it or get one.

**Daniel Lopes:** How does it work?

**Daniel Lopes:** Yeah, like, we ship one to you, but if you could use your personal one until the other one by rides or something like that, we're not super strict.

**Daniel Lopes:** Like I said, like, all this stuff, it's all internal.

**Daniel Lopes:** We don't have client user data, that kind of stuff.

**Jacopo Beschi:** So it's less of a security problem and anything.

**Jacopo Beschi:** But, okay, okay.

**Jacopo Beschi:** Sock compliant, do you need to, do you are afraid about that, like in the future?

**Jacopo Beschi:** Yeah, we might need to be Sock compliant in the future, but today we're not.
