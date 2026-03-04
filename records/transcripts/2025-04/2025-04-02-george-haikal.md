# ✨ George Haikal

<metadata>
date: 2025-04-02
time: 18:14 UTC
duration: 47 minutes
organizer: daniel@growthxlabs.com
participants: Daniel Lopes, George Haikal
fathom_recording_id: 55177271
fathom_url: https://fathom.video/calls/267802774
share_url: https://fathom.video/share/4q6kzxt26322yyWsSyDQuiduzhcnF77J
source: fathom
enriched_on: 2026-03-04 12:30 UTC
</metadata>

---

## Summary

Daniel Lopes walked George Haikal through GrowthX.ai's AI-powered content marketing platform, demonstrating the layered technical architecture (orchestration engine, workflow framework, task hub, and learning engine) and rapid team expansion plans. George is being considered for a strategic generalist role—either Innovation Strategist or CX Strategist—with a trial project focused on implementing Jobs-to-be-Done methodology, potentially starting in mid-April at San Francisco market rate.

---

## Context

George Haikal is an external strategist experienced in Jobs-to-be-Done methodology who is exploring a full-time, undivided-attention role with GrowthX.ai. Daniel Lopes is the VP of Product & Engineering at GrowthX.ai, the AI-driven content marketing platform founded by Marcel (the CEO). The call was a strategic alignment discussion: Daniel introduced GrowthX's business model, technical stack, team structure, and ambitious scaling plans, while George evaluated whether the company's growth trajectory, generalist needs, and Jobs-to-be-Done opportunities align with his career interests. GrowthX is at an inflection point—preparing for a Series A announcement in a few weeks, scaling from ~30 to 100+ employees, and diversifying beyond SEO into multiple content marketing verticals. George's availability begins April 17th with some scheduling constraints (two weeks fully in-person unavailable, two weeks in May virtual-only), though he's willing to accelerate the start date if needed.

---

## Relevance

- **To GrowthX Business Development & Hiring:** George represents an immediate fill for a high-leverage generalist position that Daniel identified as a critical gap—someone who can manage across functions, operate at startup velocity, and navigate ambiguity. A successful trial project on Jobs-to-be-Done could establish a repeatable process for their 30+ new clients and inform their Series A pitch on ICP clarity and diversification strategy.

- **To GrowthX Delivery & Expansion:** George's expertise in Jobs-to-be-Done methodology directly addresses Daniel's stated priority: helping clients understand *why* their initiatives aren't working (wrong audience, product-market fit issues, tracking gaps) rather than just generating traffic. This applies immediately to 30 active clients and scales to future verticals (sales, recruiting, backlink outreach) beyond pure content generation.

- **To Product Innovation:** George has built nearly end-to-end JTBD automation work (transcript analysis, expert note synthesis, gap detection, prompt optimization) on another company's engagement. Daniel immediately saw the potential to bundle this with GrowthX's AI workflow platform, turning it into an internal offering and a future product line—indicating strong product-market validation.

---

## Overview

- GrowthX.ai is building an AI-powered content marketing platform with multiple layers: orchestration engine, workflow framework, task hub, and learning engine
- The company is rapidly scaling its engineering and marketing teams, aiming for 100+ people by year-end
- They're seeking to diversify beyond SEO into other content marketing areas and potentially sales in the future
- George Haikal is being considered for a strategic role, with a trial project focused on Jobs-to-be-Done methodology

---

## Key Topics

### GrowthX.ai Technology Stack

  - Built an AI orchestration engine and workflow framework for content creation
  - Uses distributed systems runtime (Temporal) for executing complex workflows
  - Developing a custom UI to replace AirOps/Airtable for workflow management
  - Building micro-apps for specific content creation tasks (e.g., assignment brief generation, image creation)

### Team Structure and Growth

  - Engineering team led by ex-Apple and HashiCorp engineers
  - Marketing team structured into pods, each led by experienced growth professionals
  - Aiming to hire 11 directors and 50 content managers by year-end
  - Engineering team targeting 15 high-caliber AI-focused engineers

### Business Model and Services

  - Primary focus on content marketing and SEO for clients
  - Expanding into programmatic SEO, editorial content, and other marketing services
  - Considering diversification into sales-related services in the future
  - Developing a learning engine to improve AI models based on user interactions and edits

### Potential Role for George Haikal

  - Discussing a strategic position (Innovation Strategist or CX Strategist)
  - Emphasis on being a generalist who can manage various aspects of the business
  - Proposed trial project focused on implementing Jobs-to-be-Done methodology
  - Potential start date in mid-April, with full-time commitment

---

## Action Items

- **Daniel Lopes (GrowthX.ai):** Send George a formal offer, role details, and internal memos/strategy documents by end of day or next day
- **Daniel Lopes (GrowthX.ai):** Research and align on final role title (Innovation Strategist vs. CX Strategist) before offer confirmation
- **George Haikal & Daniel Lopes:** Set scope, timeline, and budget (~$10k) for Jobs-to-be-Done trial project; target start April 17 or earlier
- **Daniel Lopes & George Haikal:** Finalize compensation expectations and confirm start date and schedule accommodations
- **Daniel Lopes & George Haikal:** Explore integration pathway for George's JTBD automation work into GrowthX.ai's product offerings in future; potentially invite Bob (GrowthX) to brainstorm productization

---

## Transcript
**Daniel Lopes:** Okay, let me share my frame and walk you some of our pitch deck and it gives you an idea and then I can walk you to the platform and all that that we have under the hood.

**Daniel Lopes:** So let me see this is the pitch deck to investors.

**Daniel Lopes:** No, this is our own.

**Daniel Lopes:** Okay, this is our internal stuff.

**Daniel Lopes:** Yeah, so like the long story short Marcel did a ton of like publication stuff we probably talked about this before IBM he helped create their security publication became their main sort.

**Daniel Lopes:** Lead generation, same thing for HP, and then he did a lot of events at scale AI and has your corpus more of traditional school doing many things equally paid traffic and all that.

**Daniel Lopes:** But it did Graham is where he got the idea from.

**Daniel Lopes:** So when I joined, he was doing a lot of stuff that.

**Daniel Lopes:** looked like a lot simpler than this.

**Daniel Lopes:** But essentially, he came up with the whole process of a deep gram material doing this programmatic SEO.

**Daniel Lopes:** So he came up with the idea of, OK, deep gram competes with 11 labs, complete whisper from OpenAI as all these competitors, their product is actually better.

**Daniel Lopes:** But they're getting all eyeballs, and they have no money to pay for ads or anything.

**Daniel Lopes:** So what can I do here that is asymmetric?

**Daniel Lopes:** So he came up with the idea of creating an AI app's directory, like everybody that could be working with any sort of LML or AI-based apps at the time, a couple of years ago, when it was just starting, catalog everybody, enrich their creative page for them, enrich this page with a ton of external resources, essentially create the current base of AI apps.

**Daniel Lopes:** And a lot of those are like,

**Daniel Lopes:** same able, a lot of those are not voice, like it was not deep rectal overlap with deep gram, deep gram is a voice agent, and like a voice API, text to speech and speech.

**Daniel Lopes:** But people were looking for things like AI app that does agenda, AI apps that do a gallery tracking, right?

**Daniel Lopes:** Like everything was a bunch of cheap AI apps, none of those pages have like good descriptive articles about the apps and what they do better and competitive alternative and all that.

**Daniel Lopes:** So he essentially created this way of deep gram to be top result for any AI related apps.

**Daniel Lopes:** that you're looking for and so that's what you see in the traffic that he was showing here.

**Daniel Lopes:** So this is the growth that that programmatic SEO, the director they created created and it became the main source of traffic to deep gram.

**Daniel Lopes:** And then he started trying to do that with other people and got similar results.

**Daniel Lopes:** A lot of it is programmatic, some of it became editorial content.

**Daniel Lopes:** So if you're just creating, I feel like they're creating like under pages a week.

**Daniel Lopes:** It doesn't need to be high quality, super well written. It's more like a structured record: what do they do, what are their features, specific bullet points about the founders, screenshots, and pipeline information.

**Daniel Lopes:** Then Marcel started creating things that were more editorial. If he wanted to publish five articles, what could be automated? So he had two work streams: one for programmatic SEO and one for editorial content. He started with Deep Gram and then applied it to other clients. That approach works for everything.

**Daniel Lopes:** When I joined, he had these two work streams, but they weren't sophisticated. They could have had logic, branching, flow, agent loops—more structure to the process.

**Daniel Lopes:** For example, with editorial workflows, programmatic SEO isn't that hard because you have one data source: you know the URL, you scrape it a few times, and create content from it. But when you're creating something from nothing—just a keyword or a URL you want to compete with—how do you generate an article that's actually accurate?

**Daniel Lopes:** So we came up with a research process that collects information, validates it, and stops when it's good enough. We created a researcher workflow, and then we realized every article needs a different outline. A listicle has one structure, but a tutorial, guide, or comparison piece needs a different outline.

**Daniel Lopes:** So we created a workflow that creates out.

**Daniel Lopes:** And then we did the same thing for titles.

**Daniel Lopes:** titles vary.

**Daniel Lopes:** you want to give people the choice of which part the titles here and which ones are better and less than customized.

**Daniel Lopes:** So we created the title generator that's like SEO friendly, but you can customize.

**Daniel Lopes:** And then the draft, same thing.

**Daniel Lopes:** the draft, and then when you start doing something like the draft, when you search it, start hitting it out to efficiency problems.

**Daniel Lopes:** Sometimes we take 10 minutes, or for a draft, if you're generating a draft that has an outline with 20 sections, each section might take a couple of minutes.

**Daniel Lopes:** It's going to take an hour to finish the saying.

**Daniel Lopes:** we start hitting parallelization problems.

**Daniel Lopes:** At the end, there's style matching. How do you match the voice of the client? We have a workflow for that too. So we created all these workflows. In the beginning, we were stitching together no-code tools like AirOps. AirOps was where we created workflows and connected them. I don't know if you've seen AirOps, N8N, or Zapier—Zapier is linear, but N8N lets you branch out. We started with that.

**Daniel Lopes:** It's just got super complex, and the prompts are super long. We want to see the changes we're doing over time. You want to measure the cost of each LLM call, iterate on the prompts, and AB test. That's not possible in those tools if you're doing things at proper production level.

**Daniel Lopes:** So we created this environment. We essentially created a framework where you write workflows in code. Workflows are for files—the steps that the workflow will do, the logic, the branching, parallelization, if-else statements. There's a separate file for prompts and a file for types. The types define the input and output from each API call. The prompt file is what you see on the right here. Workflows are atomic and self-contained. A workflow might be a researcher that takes goals and outputs data, or stores data in the database—it's essentially an API endpoint. Same thing for styling: you receive an article in a certain language and rewrite it for the client. The output is a new article.

**Daniel Lopes:** The workflows are standalone, self-contained four-file folders, and we have a code generator that creates them. You create a workflow design spec for Cursor, and we have Cursor rules that teach how the framework works: the four files, how they're sized, and how they load into the memory of a coding agent so it can iterate with you.

**Daniel Lopes:** We don't write the code ourselves; we talk to the AI on the right side of Cursor. The structure of the framework is all defined in our Cursor rules—how to write everything, rules for prompt engineering, and more. Workflows look like this—let me show you a real example.

**Daniel Lopes:** We usually start with a plain text file. This one is for generating cover images for an article. We just say, "I want to create a workflow that generates multiple cover images for an article." The input includes the information field, the art style we want, an optional color palette, optional art direction, and optional model. In this case, I was using Stability AI with their Ultra model, core, and aspect ratio. Then we list the steps and activities—what the activity has to do.

**Daniel Lopes:** All of this sits on top of a distributed systems runtime called Temporal. I'll show you why in a moment, but we have all the definitions here in our Cursor rules.

**Daniel Lopes:** Yeah, exactly. So it's not just generating one image—it comes up with 10 ideas in that style, then another step chooses the best idea based on what the client does, then calls Stability AI multiple times in parallel, stores the results in S3, and returns the collection. The editor can look at all the generated images and pick the best one with different prompts. So they don't have to write prompts themselves—we're removing the prompt barrier because prompting is hard. That's one example.

**Daniel Lopes:** So with this, we have a script that will take this in, taking all the, how the framework works, and a couple of templates, and then we generate the workflow for you.

**Daniel Lopes:** And then the programmer would just like, we view that and iterate on the prompt.

**Daniel Lopes:** in the case of like,

**Daniel Lopes:** image, the prompt will look like this.

**Daniel Lopes:** So this is kind of one of a complex one.

**Daniel Lopes:** Because we have different styles, have a photographic image generation prompt, we have abstract prompt, and we have a pop art prompt, and then we have the one that will select the best idea.

**Daniel Lopes:** So, and then you can come here because it knows how we write things.

**Daniel Lopes:** can say, like, I want to add a new style.

**Daniel Lopes:** And because this context is just this file, it knows all the other things that we have here.

**Daniel Lopes:** And if I want to treat it on the whole workflow, I could just drag the folder here.

**Daniel Lopes:** whole thing was structured to be coded by 8.

**Daniel Lopes:** The next step would be to improve the UI we have.

**Daniel Lopes:** So, me show you the UI.

**Daniel Lopes:** this is what we have running today.

**Daniel Lopes:** people are like, let's see here what's going on.

**Daniel Lopes:** So, we have, we use it for recruiting

**Daniel Lopes:** as well.

**Daniel Lopes:** recruiting, for example, we have, this is somebody's resume, so we're reviewing their resume.

**Daniel Lopes:** So we got this input from workable, and so we first get the person's ID, we validate that the resume is in PDF form, we're in PDF with forested resume, so we do like a OCR on their resume.

**Daniel Lopes:** We get the job requirements, so we have a notion document with the job requirements, the job expectation, and then we analyze the resume, is this resume matching the stuff we have in the machine, like for this role, I think it's a programmer role, we ask for experience with Ruby or Python, like any kind of back-end and dynamic languages.

**Daniel Lopes:** Leadership things are helpful, and so we create red flags and green flags, and that we don't disqualify unless it's like really bad.

**Daniel Lopes:** And then we put that in the workable, and it will help sort then based on this.

**Daniel Lopes:** And we go question by question, we have application questions, and we have a rubric for each question.

**Daniel Lopes:** So in this case, it's like squaring and like no red flags.

**Daniel Lopes:** like it's just like the bar is really low action.

**Daniel Lopes:** But this for the engineering side is not that important, but for the service side, because we hire like four or five people a month, super important.

**Daniel Lopes:** I've got the NASA day.

**Daniel Lopes:** So like that's the example.

**Daniel Lopes:** this is running a workflow similar to what I showed you.

**Daniel Lopes:** If I open the workflow here, it'll point to the runtime.

**Daniel Lopes:** So this is a distributed system, runtime that we use.

**Daniel Lopes:** So it's like, you can see the steps getting executed sometimes within parallel.

**Daniel Lopes:** So it's analyzing all the questions in parallel here.

**Daniel Lopes:** Then it makes a final assessment update workable post to Slack.

**Daniel Lopes:** And I could at any time, if I was the beginning, is I could come here and reset to that stage iterate on the prompt and retry locally as well.

**Daniel Lopes:** And I can see the code of this workflow.

**Daniel Lopes:** We actually added about a couple of days ago.

**Daniel Lopes:** But this will be in main packages, then Poro packages, then Poro source, that was hiring resume, I think was a product engineer role.

**Daniel Lopes:** So this is the workflow for, I need to update that about, but this is essentially the whole pumps for that.

**Daniel Lopes:** So this one is like fetching a lot of stuff from Notion, so we don't have the rubrics here, but we have the pages in Notion where our recruiters can adjust the expectations and everything, and this is the workflow.

**Daniel Lopes:** So it's pulling from, job expectations from Notion.

**Daniel Lopes:** So like for example, this is the Notion document that we have broad qualifiers, the leveling of the person and all that, and you have the application evaluation.

**Daniel Lopes:** So you can see the rubrics or the rubrics on XML to just define like the introduction, like what do we look for, and the question about automated tests and what do we look for, question about very specific, like we have like the whole thing there.

**Daniel Lopes:** And so that's essentially the background of how we're doing things.

**Daniel Lopes:** And we use AirOps as a spreadsheet that triggers API calls.

**Daniel Lopes:** And the API calls are to our back end.

**Daniel Lopes:** So in the case of, let's see, the image one that I was talking about.

**Daniel Lopes:** There's a client here called DataGrid.

**Daniel Lopes:** DataGrid.

**Daniel Lopes:** We don't use AirOps workflows anymore.

**Daniel Lopes:** Let me show you.

**Daniel Lopes:** So we have this.

**Daniel Lopes:** So they have March 31st.

**Daniel Lopes:** Let's see if they have any images here.

**Daniel Lopes:** March 24th, the Ohab stuff.

**Daniel Lopes:** But we have a bunch of work.

**Daniel Lopes:** Those teach together, all these blue columns are were closed.

**Daniel Lopes:** If I edit this, all it does is an API call to our backend.

**Daniel Lopes:** So this just cleans up the code and generates a URL, makes an API call to our backend, and I can see that running.

**Daniel Lopes:** If I double-click here, I can check the logs and execution URL—it's pointing to our backend. I can see that. Let's get a newer example so it's not cached. This one is the most recent. The execution URL shows that the logs are still old, but I think you get the idea. We expire some URLs after time, but we're using it to generate the image. It's in our workflow, taking in the article, style, and input. It's using the art direction. In this case, it generates images and there's a predefined input of pop art. We have a pop art art style executing on our backend.

**Daniel Lopes:** We still use AirOps and Airtable as a place to store things. The next step is to replace all that with our own products.

**Daniel Lopes:** The next step is replacing AirOps and Airtable with our own products. We're building an environment where instead of a spreadsheet in AirOps, you have a UI with a bunch of items. You can run them all at once if you're doing programmatic SEO, repeat at the end, or run them in human steps—pause on one step, continue on another. The pipeline is dynamic. You define a pipeline by sharing the context you need for the whole spreadsheet, then define each step. For example, step one might be assignment generation using our assignment generation workflow—those are the inputs, those are the outputs. For the output, I want to edit with a rich text editor. For other things like image selection, I want a carousel or array. The UI here changes based on what you're editing. When I click on this, I can see the pipeline and every step executed. I could come here and chat with it and say, "I actually want more depth."

**Daniel Lopes:** I want to actually expand this with another research.

**Daniel Lopes:** So we'll be using API, there's this thing called mspeed today that you can use LMS to chat with API calls.

**Daniel Lopes:** So we would be chatting with all the workflows here or chatting with API's like SCM brush and something like that.

**Daniel Lopes:** So essentially cursor for brush.

**Daniel Lopes:** you'll be able to come here and select the images.

**Daniel Lopes:** This is different UI.

**Daniel Lopes:** this one is a carousel and at the end, you would have the whole article here.

**Daniel Lopes:** then you can just still iterate on the article here and you could publish or stage it for the client to review.

**Daniel Lopes:** So we're going to have an area for the client to review and improve and then do more iterations on the thing.

**Daniel Lopes:** And then publish to like Contentful, Sanity, Webflow, Strapi, all these workflows, all the CMSs.

**Daniel Lopes:** So that's the platform we're building.

**Daniel Lopes:** So we have this AI orchestration engine here, the runtime.

**Daniel Lopes:** where we can use for anything.

**Daniel Lopes:** And that's kind of a lower level where we have code, you have an IDE that we're building.

**Daniel Lopes:** So the thing that I showed you, this will become an IDE where you can create your flows here, you can be bugged in, you can send pull requests back to your repo, essentially something similar to DBT, I don't know if you've heard of them, but DBT is the same idea for data analytics.

**Daniel Lopes:** So you can create DUs and tables and all that and the UI, the UX is very similar what I'm going for.

**Daniel Lopes:** So we have given this layer in the middle, which is a general use orchestration.

**Daniel Lopes:** LSM is an API orchestration layer.

**Daniel Lopes:** We have a framework, an IDE, and a runtime on top of the same code.

**Daniel Lopes:** And this, I think we're going to be able to launch some of these parts as open source.

**Daniel Lopes:** And on top of this, we're going to build a bunch of vertical businesses.

**Daniel Lopes:** So we're starting with marketing, content marketing, that's the UI that I

**Daniel Lopes:** Showed you that that alone would be like a product that would be probably the whole year a bunch of like super skilled people working on that That's like the scope is hard that alone is like a startup on itself And then we have a task hub like where like we work today with up work And fiber and thanks so much a effort ideally.

**Daniel Lopes:** We just want to have like hey nurse Review like nurse practitioner review this article we wrote for him and see if the references are correct Hey designer just like pick the best image from this or create a new image in this style That's all they do is like it would be like a task API Where you can you have people that go through an assignment process a process and they they get qualified and after that they receive work Yeah, and it's small small contain they have no context around It's just like any tasks that they would be implemented into whatever vertical we use So for the marketing side will be like a lot of content editing a lot of content review a lot of fact checking a lot of like small things like that

**Daniel Lopes:** Well, verticals, let's say if we're doing sales, or if we're doing recruiting, would be actually validating the evaluation, know?

**Daniel Lopes:** So those are the two main things on the surface.

**Daniel Lopes:** We have the iWorkflow and you know, we don't have a lot of like micro apps as well.

**Daniel Lopes:** So we have this one, for example, that every time we create an article, let's see, human, super human is a client.

**Daniel Lopes:** I'm not very happy with all their running there.

**Daniel Lopes:** They're bored, so let's know what's happening here.

**Daniel Lopes:** There's two ramping up.

**Daniel Lopes:** So we have an assignment brief generation process that we'll take him a URL or a keyword, we'll figure out the target audience, do a ton of research and figure out the top organic results, roughly.

**Daniel Lopes:** What was the input here?

**George Haikal:** it a website?

**George Haikal:** Was it a keyword?

**Daniel Lopes:** It was just the communication trends.

**Daniel Lopes:** Yeah, and it takes in the super human name, and what they do in their website as well, and then we'll do a bunch of research.

**Daniel Lopes:** So in the...

**Daniel Lopes:** In this case, I can actually pop up.

**Daniel Lopes:** This is the output.

**Daniel Lopes:** So you have a proposed content structure based on the competitors and all that.

**Daniel Lopes:** And the execution was this.

**Daniel Lopes:** So the execution was fetched to organic results.

**Daniel Lopes:** got like 20 something, analyze each one of them, get the traffic.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Then read the article, clean it up to remove headers and noise, score whether it's relevant to the client, analyze, and at the end, create an assignment brief to help people compete with that. That alone is a micro app. We put a UI on top of it, and it becomes something people can use. Same with the image generation stuff I showed you. We have a ton of micro apps we're going to build, making a micro app store for content creation.

**Daniel Lopes:** And we have another layer: our learning engine.

**Daniel Lopes:** Everything we do—when someone adds an outline, adds an article—is essentially data annotation. We have a data annotation layer that learns from all the edits happening, including edits to the workflows themselves. If someone improves a prompt on a workflow, we should learn from that. We're building smaller models for specific things: fine-tune models for assignment creation, outline generation, style matching, tone, brand alignment. We can learn from the whole website how you write and fine-tune on that.

**Daniel Lopes:** So we're building this learning engine, and we need to track input and output of every LLM call. We need to monitor exceptions and threshold violations. That's another layer. We're building the first layer now. The second layer is functional but has room for improvement. We're hiring hardcore engineers to build this, plus product engineers. Later in the year, we'll build more of this. And I need to find a couple of ML and data science people to start building the foundation.

**Daniel Lopes:** That's the direction we're going. I hope this gives you a breakdown of how the whole thing works. And the reason we're fundraising is that each of these four layers would be a whole startup on its own, but we're building all four at the same time.

**Daniel Lopes:** So let's go.

**Daniel Lopes:** I love it.

**Daniel Lopes:** I love it.

**Daniel Lopes:** I hope that makes sense, and it's not amazing, Daniel.

**Daniel Lopes:** Too much information.

**Daniel Lopes:** Yeah, so, like, we'll see how that goes.

**Daniel Lopes:** But so first, we're moving, and I'm pretty happy with the team, as I'm to show you the art chart.

**Daniel Lopes:** I can give you a glimpse of who is on the team now so we have this is an outdated one where is mine okay this is mine so we have marketing on an engineering team i have failed mobile team for an Airbnb was principal engineer at Apple as well just now and then we have claimed claims in the engineer number six at a HashiCorp help good terraform markets at four times worked with us with me and you know market is on the support is a support engineer they're just transferring tickets and helping stuff like that Kirkland helped build a lot of the growth for a cop so Kirkland is kind of like a growth engineer and we're going to be adding like three more

**Daniel Lopes:** this month I hope.

**Daniel Lopes:** And then on this right side here we have Bridget is our VP of ops and chief of staff for Marcel and me basically but she has so much on her plate.

**Daniel Lopes:** Came from AirBite, Tucker, our lead recruiter came from the AirBite as well, it was amazing.

**Daniel Lopes:** And we have a recruiter in charge of the services team and we have on the left side, Head of Growth from Trade.AI runs are starting to run our sales team.

**Daniel Lopes:** He was in charge of the services team before, was switching to sales.

**Daniel Lopes:** We have Jay, Jay's Head of Growth from Bardeen and Kite.

**Daniel Lopes:** Kite thought AI was a it shut down recently but it was a cursor before cursor.

**Daniel Lopes:** And then we have a bunch of people on the right side.

**Daniel Lopes:** This is like a bunch of marketing, like skilled marketing people.

**Daniel Lopes:** So we have Matthew he was chief editor for TechCrunch, just joined like a couple of weeks ago, but he's

**Daniel Lopes:** charge of content in general, and you have people that have a growth from SEMrush, we have people that are running SEO for TripAdvisor, have people that are inside their G2 Crowd, and like a bunch of people that are in growth, successful growth programs at different companies, and they run their pods, so their pods would be like three, they will have like three pods, they'll have like, sorry, like each one of these is a pod, so they have like six pods now, it's missing a couple here, we added a couple more, and each one of those we have managing editors, then managing editors have a bunch of content managers under them, so that's the structure that we're going for, we're probably going to need, I forget to have cons, but I think the service side will be like 50 content managers by the end of the year, like this bottom layer, and we probably, I think we're here, we need 11 directors, and we have like nine for the whole year.

**Daniel Lopes:** So we are overstepping this role first, and then for the managing errors, it's like three for each.

**Daniel Lopes:** So the service side would be like 100 plus people.

**Daniel Lopes:** And the engineering side, I think it's going to be like 15.

**Daniel Lopes:** It all goes well, because we have, we're going a lot slower here.

**Daniel Lopes:** And that's where a lot of the cost will go.

**Daniel Lopes:** These people are not cheap.

**Daniel Lopes:** So like, I'm trying to go for less people, people, engineers are excited about AI.

**Daniel Lopes:** They can use things like cursor, but are experienced.

**Daniel Lopes:** they don't make mistakes in entire lane.

**Daniel Lopes:** So they cost like three times the cost of a normal engineer.

**Daniel Lopes:** But today with like stuff like cursor, you can produce 10,000 lines of code.

**Daniel Lopes:** If you're sprinting the right direction.

**Daniel Lopes:** So that's the cool thing we're going for engineering.

**Daniel Lopes:** We're going for the density first and then maybe.

**Daniel Lopes:** Over time, we had more folks, but I think that's a smart approach.

**Daniel Lopes:** Yeah, we'll see.

**Daniel Lopes:** But that's the way we're going.

**Daniel Lopes:** I hope that makes sense.

**Daniel Lopes:** that answer your, your, because I bet your excuse, like, how, how was this thing where, you know, a hundred percent?

**Daniel Lopes:** Yeah.

**George Haikal:** It was a lot, but it was really good information and really exciting as well.

**George Haikal:** Like what, what you all are doing to grow, how you're thinking through all these things, I'm super impressed.

**George Haikal:** Cool.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** I can think of the, like I was saying, like there is like, there specific projects, like the jobs should be done.

**Daniel Lopes:** Stuff like, like I said, like we need that for ourselves.

**Daniel Lopes:** We need to calibrate our ICP. We only have capacity for so many clients. We've seen two kinds of clients: giant enterprise clients and ramp, and startups. Giant clients—like folks starting next week—we know what we're doing there. But relationship-based clients take forever for Marcel to build—he's been creating them for four years. Then you have startups that come inbound. The question is, who do we take? We're making our Series A announcement in a couple of weeks, and I expect the pipeline will get a lot easier. We're already super busy, and sometimes we choose the wrong ones. We need to figure out our ICP and calibrate it. Jason Bruno is trying to figure that out, but they don't have the Jobs-to-be-Done skills, which I think is super high leverage. On the flip side, Jobs-to-be-Done is something we should apply everywhere. Clients are unhappy for different reasons. Sometimes we grow traffic in an audience they thought was good but wasn't. You spend four months getting them a hundred thousand views a month and nobody buys anything. Why? Because the product is wrong, or the audience is wrong, or the website is broken, or they can't track the purchase. So many things can go wrong.

**Daniel Lopes:** So we're essentially doing Jobs-to-be-Done at scale with 30 clients, trying to help them grow. It's figuring out: which direction should we go? Do you even know where you want to go? That's why Jobs-to-be-Done alone is a huge project.

**Daniel Lopes:** What we want to do is diversify from SEO. SEO is huge, and I think the pitch is strong there, but we can also run design generation, case studies, interview content, and other things in the same infrastructure. Jobs-to-be-Done is one work stream we're focusing on. Another work stream we're building now is backlinking—reaching out to people and saying, "Your article is actually similar to ours, we have focused domain authority, why don't we partner and exchange links?" We've done that.

**Daniel Lopes:** It's not the works team we're building parallel.

**Daniel Lopes:** So we wanted to diversify from just like content generation, and we don't want to go into sales yet, but that could be something we do next year.

**Daniel Lopes:** That was my next question, yeah.

**Daniel Lopes:** Yeah, like sales, was a little bit, got a little bit of a barn reputation all because of well, 11x.

**Daniel Lopes:** don't know if you saw the, uh, people were like, sales are super hard, you can spend your whole, uh, end with the wrong message and screw up the whole pipeline.

**Daniel Lopes:** Uh, so like we want to do sales after, but there are ways to do that.

**Daniel Lopes:** We can't figure it out, but we're just going to focus on content marketing first, but try to build the things that's like around it, know, but also yeah, and don't actually fit that, you know, so.

**Daniel Lopes:** So that's why I was thinking like we have like this two immediate projects in the meantime, probably like 30% of the time is also just a history thing is a startup so it's stop happening everywhere and it's like we I need people there are generalists and willing to do anything and jump everywhere.

**Daniel Lopes:** Where programmers, they can do that, they should do that at their own project.

**Daniel Lopes:** I don't want them to be distracted jumping everywhere.

**Daniel Lopes:** They're too expensive.

**Daniel Lopes:** They should be like focused, you know.

**Daniel Lopes:** The patient is bad as gold.

**Daniel Lopes:** So like last week, for example, our program, I left him without giving any items.

**Daniel Lopes:** He rewrote the whole thing in Docker, which is  amazing.

**Daniel Lopes:** Like you have people like that.

**Daniel Lopes:** Like I don't want them to be like solving things that other stuff.

**Daniel Lopes:** Yeah, like they're free time.

**Daniel Lopes:** They're just like  fixing the whole thing.

**Daniel Lopes:** Like that's that's that's awesome.

**Daniel Lopes:** Like please do that.

**Daniel Lopes:** know, I'll do the tickets for you.

**Daniel Lopes:** I'll join the calls and I'll do whatever it takes to like speed you up.

**Daniel Lopes:** I need more people with this mindset. Everyone has their expertise—marketing people are heavy on growth, engineers are great at engineering. We need somebody in between. We need people who are great at sales, good at getting things moving, good at operations. It's just me and Bridget right now. We make things work, but we need more people with that generalist, outcome-oriented, results-oriented mindset. That's why I'm looking for someone with 20 years or 10 years of experience who's grown companies. If that interests you, I can pull together an offer and send it today or tomorrow. We could use Jobs-to-be-Done as a trial project, set the scope and timeline whatever works for you. We could budget around 10k for the trial. We don't have to commit to a long-term engagement—just a month or so of working together to see if we're a good fit.

**George Haikal:** I like the team and the scope makes sense to me. It's great that you're here in San Francisco too—we have one more person here. I've been following you the entire time, and we're really aligned. With Jobs-to-be-Done, there's a ton of applications both immediate and ongoing. It'll augment and help all these experts you're bringing in who are focused on their verticals and pods. That's really exciting—figuring out why big companies and startups churn, why things aren't working, and evaluating future markets for the other directions you mentioned.

**George Haikal:** On the second piece—the generalist role, fixing things, managing—that's also what I love doing and where I've always fit in. So the trial run makes sense for both of us. I'm open to earlier than June. I have two weeks locked off for in-person stuff, but April 17th forward I'm available. There are two weeks in May where I'm virtual-only, but I have to be in person for some other relationships I'm closing out. Neil's aligned on that. I'm just super grateful and excited, and willing to do whatever it takes.

**George Haikal:** Cool.

**Daniel Lopes:** right.

**Daniel Lopes:** yeah, let's think about this.

**Daniel Lopes:** Like, do you have any like Comp range expectations or anything that you like that you have like I we have cart uh, we can But the thing that I'm like, I'm trying to figure out the role, you know, like because Compared to comparison.

**Daniel Lopes:** I can find it will be like weird because I was like You know, I did some research as well.

**George Haikal:** It's something we can talk about, right?

**George Haikal:** But the way I was thinking about it was like I want to be able to give you all like my full and undivided Attention and focus Right, I just exclusively You know try to drive the value for you do nothing but level up learn grow like whatever it takes.

**George Haikal:** I You know, I know how to

**George Haikal:** Prioritize and I know how to say no, but I usually just say yes and figure it out But it's completely in value for something I can pass off.

**George Haikal:** I also understand how to do that.

**George Haikal:** So Basically, I know how to grow and learn and take feedback.

**George Haikal:** And so I also just like love the growth opportunity like can see Can see the growth in the future with you and the company and I want to be a part of it like I want you all to be proud of Letting me join team early and like going to distance together and so I mean, I did research on on roles like the two titles that we kind of talked about briefly the CX strategist and the innovation strategists I have ideas on the titles in general and like My first question I guys is How are you thinking about the titles themselves and why did you go with CX strategists over innovation strategists?

**Daniel Lopes:** Yeah, just like coming out of whatever I could find because like if I just like I was just looking stuff like Carta and

**Daniel Lopes:** like some of the other things we have they all like they basically don't have that role and everything would be like project manager would be like UX researcher and all that you know so it's a different I could you know so that's like I'm thinking like the practical idea of this I was thinking like the day to day like the CX strategist is something that some companies like intercom have done and some others have tried to do and and large companies are now implementing those roles I was doing some research bigger companies like uber other companies they're starting to pull them in which is interesting I'm open like I this is I'm happy to just have a discussion about it what it sounds like is it art either innovation strategist there's CX strategist and part like most chief of staff is like the other things and you were talking about right right so I'm trying to figure out how to

**George Haikal:** package that into a title.

**George Haikal:** But for me, innovation strategist feels more broad than encompasses those other aspects maybe little more than customer experience strategist.

**George Haikal:** Yeah, this one's good.

**Daniel Lopes:** Yeah, let me do some research and then I'll and then we can see if we're aligned there.

**Daniel Lopes:** Yeah, definitely, full-time, undivided attention, they're not going to be like, the core trying to do is just like pay San Francisco market salary for everybody, including all the remote folks.

**Daniel Lopes:** it doesn't matter that you're here, you know, that doesn't create any imbalance anywhere else.

**Daniel Lopes:** So, yeah, got it.

**Daniel Lopes:** I see the vision.

**George Haikal:** I'm willing to do whatever it takes. Let you get back with the team and we can talk numbers after. Does that earlier start date work for you?

**Daniel Lopes:** You seem like you're busy and underwater. I have someone starting already, but I want to know if the earlier date works. That would work great. Cool, man. All right, this is awesome. I'll follow up with you in writing.

**George Haikal:** Is there anything you have in the meantime, materials-wise or things I can learn outside of that deck or that I should be learning or diving into outside of that deck?

**Daniel Lopes:** I'll put together some stuff.

**Daniel Lopes:** We have some memos and some internal documents I can share.

**Daniel Lopes:** I'm so excited, man.

**George Haikal:** I've been working on JTBD automation on another company's engagement. We're very close to end-to-end automation outside of the interview itself. We take the interview transcript, extract expert notes, analyze it, run different prompts—all automated. The model can now detect where you should have dug deeper based on the transcript and notes, finding gaps. We're pretty close.

**Daniel Lopes:** I can even see a scenario where you see that live on the screen as you're listening, and it's giving you suggestions. Like, "Maybe we should ask about that."

**George Haikal:** Yeah, what's irreplaceable is the interview itself. The clustering, analysis—you need a real person doing the interviews because it's so hard to do well.

**Daniel Lopes:** Then you could have suggestions on the side—guidance on probing questions, open-ended questions, just listening. It's awesome.

**George Haikal:** Yeah, I'm working on that on the side too. It won't affect this engagement, and obviously we'll put it on pause if my full-time attention is here. That's exciting.

**George Haikal:** We're thinking about these problems the same way.

**Daniel Lopes:** I bet if we add one of our engineers on this with you, we could turn it into an offering.

**George Haikal:** In the future, we can pull Bob in to get his insight on how to productize this. There's no limit to what we could do.

**Daniel Lopes:** This is very exciting. I'll get something back to you today or tomorrow at least.

**George Haikal:** Fantastic.

**George Haikal:** Thank you, Thank you for running me through everything, shoot over those materials that you want me to look through as well.

**George Haikal:** I appreciate it and we'll talk soon.

**George Haikal:** Sounds good.

**Daniel Lopes:** Thanks, man.

**Daniel Lopes:** Thanks for your time.

**Daniel Lopes:** Have a go.
