# Atlas Training

<metadata>
date: 2025-06-16
time: 17:00 UTC
duration: 63 minutes
organizer: Mariana Montezzana (GrowthX Labs)
participants: Daniel Lopes (GrowthX Labs), Yousef Hamade (GrowthX Labs), Andi Bailey (GrowthX), Bridget McGillivray (GrowthX Labs), Matthew Panzarino (GrowthX), Marcel Santilli (GrowthX Labs), Ehtisham Hussain (GrowthX), Kirkland Gee (GrowthX), Carrie Chowske (GrowthX), Jess Scott (GrowthX), Cristina Caceres (GrowthX), Megan Dickey (GrowthX), Clint Shryock (GrowthX), Marcus Derencius (GrowthX), Darrell Etherington (GrowthX), Stéfano Zanata (GrowthX), Usman Ghani (GrowthX), Sydney Go (GrowthX), Brad Herman (GrowthX), Jo Kaminska (GrowthX), Kyle Gaudreau (GrowthX Labs), Bianca (GrowthX), Jason Gong (GrowthX), Felipe Lima (GrowthX), Georgemaine Lourens (GrowthX), Jessica Nicole Manificiar Gayo (GrowthX)
fathom_recording_id: 68616339
fathom_url: https://fathom.video/calls/326488314
share_url: https://fathom.video/share/1sFQvTPaRg6sqxyKG-xJhh-oB41apgJ1
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

Daniel Lopes led a comprehensive training session on Atlas, the new GrowthX platform replacing AirOps for content generation workflows, demonstrating the platform's core features including context artifacts management, configurable pipelines for assignments and article generation, and the grid interface for managing multiple content items. The team learned that all 40+ accounts have been successfully migrated from AirOps with functionality preserved, though minor bugs and Entropic API rate-limiting issues are being actively addressed. Key action items include setting up client-specific accounts, fixing existing pipeline configurations, and sending follow-up documentation with usage guides and testing instructions.

---

## Context

Atlas represents GrowthX's migration from AirOps to an internally-built content generation platform. The training was held after the team completed an all-nighter (working until 1 a.m.) to launch the platform in production. All 40+ customer accounts have been migrated with their data preserved in Google Drive for backup, and the team is now in rapid iteration mode, expecting to ship additional features (particularly the rich text editor and pagination improvements) within the week. Daniel Lopes, who leads the Atlas technical development, walked through the complete platform with the broader GrowthX team, which includes both GrowthX Labs staff (client operations and engineering) and GrowthX team members who will be managing accounts and troubleshooting in production.

---

## Relevance

### To GrowthX Delivery

- **Atlas is now the primary content generation platform** — all 40+ customer accounts migrated from AirOps; team should operate entirely within Atlas going forward for assignments, article generation, and refresher workflows
- **Configurable pipelines provide flexibility** — new "direction nudging" feature on assignments allows ops to guide content briefs without separate instructions; XML steps and tone controls now baked into workflows (relevant for dual-tone work like Rapid)
- **Rich text editor shipping this week** — currently limited to plain text outputs; will enable in-place editing similar to Notion with context-aware AI suggestions, significantly improving content workflow efficiency
- **Rate limiting from Entropic is currently constraining throughput** — batching to ~500 items at a time is recommended; this is a blocking issue for scaling that needs monitoring
- **Linear integration for bug reporting** — team should create tickets for platform issues to ensure rapid fixes during this critical post-launch period

### To CheckThat

- **Fact-checking pipeline requires attention** — Daniel flagged the "crappy fact checker" as needing fixes for client-specific use; this is blocking downstream output quality and should be prioritized (assigned to Daniel Lopes with other critical pipeline work)

### To GrowthX Business Development

- **Atlas transition is an operational risk that the team is actively mitigating** — early data shows no major functionality gaps vs. AirOps, but performance issues and missing features (like rich text editing) could impact client satisfaction until fully resolved
- **Account-level customization is now structured differently** — context artifacts, pipelines, and projects create a more modular architecture; ops team needs to understand this for onboarding new customers and supporting custom workflows (Adventurous Group and Zuplo setups specifically called out in action items)

---

## Overview

- Atlas (atlas.growthx.ai) is the new platform replacing AirOps, with similar core functionality but a new UI and expanded capabilities
- Accounts and data migrated from AirOps; some minor bugs and performance issues being addressed
- Key new features: configurable pipelines, improved artifacts management, and upcoming rich text editor
- Team should test Atlas, report issues via Linear tickets, and expect rapid improvements this week

---

## Key Topics

### Platform Overview and Access

  - Access via atlas.growthx.ai using growthx.ai or growthx.labs email
  - Accounts migrated from AirOps, organized into workspaces and projects
  - New UI with dashboard (features coming soon), context artifacts, and pipelines

### Context Artifacts

  - Replaces AI context, company context, personas from AirOps
  - Editable with version history (rich text editor coming soon)
  - Crucial for output quality; Marcel reviewing/improving all accounts

### Pipelines

  - Replace AirOps grids; configurable multi-step workflows
  - Common types: assignments, article generation, refresher
  - Can run entire pipeline or step-by-step manually
  - Inputs/outputs customizable per step; all context accessible

### Key Pipeline Types

  - Assignments: Single-step for content briefs
  - Article Generation: Multi-step (brief, research, outline, draft, fact-check, style, internal linking)
  - Refresher: Updates existing content with new data/research

### User Interface and Workflow

  - Grid view for managing multiple items
  - Timeline view for individual item progress and editing
  - Ability to archive/delete rows for organization
  - Inspect feature for detailed execution info and troubleshooting

### Performance and Known Issues

  - Some slowness due to rate limiting from Entropic
  - Rich text editor coming soon to improve editing experience
  - Pagination and sorting improvements planned

### Customization and Flexibility

  - Pipelines highly configurable via JSON-like structure
  - Can add/modify steps, inputs, outputs as needed
  - Team working on remaining client-specific customizations

---

## Action Items

**Daniel Lopes (GrowthX Labs)**
- Setup Adventurous Group account in Atlas with 5 projects; add real grids/stats for Adventurous Group & Zuplo
- Fix fact-checking pipeline for relevant client; adjust dual-tone & XML steps for Rapid; implement data grid post to Webflow; add title/metadata fields to All Workflows final output; setup Zoopo programmatic APIs grid
- Add URL generator/slug workflow to relevant client pipelines
- Send follow-up message with Atlas usage guides, testing instructions, and practice tasks
- Update Linear ticket template to include workflow URL or pipeline options

**Jess Scott (GrowthX)**
- Drop note with other client buckets needing setup in Atlas (those previously done in ChatGPT)

---

## Transcript
**Daniel Lopes:** Hello, everyone.

**Daniel Lopes:** Sorry for being a couple of minutes late.

**Daniel Lopes:** We are running the thinking production now.

**Daniel Lopes:** It started early this morning, and we're seeing some little bugs here and there.

**Daniel Lopes:** We're getting some rate-limiting errors from the entropic, and that's the main thing that's holding us back a little bit now.

**Daniel Lopes:** But this is enough for me to walk you through everything.

**Daniel Lopes:** Today will be a little bit less planned than how I usually like things to be, because we worked on this until 1 a.m.

**Daniel Lopes:** yesterday, so we didn't have much time to prepare.

**Daniel Lopes:** The training and everything the way we want.

**Daniel Lopes:** So we might have to do another session, maybe tomorrow, or maybe like a...

**Daniel Lopes:** I mean, this week, but we were able to import all the accounts, all the 40-ish accounts we have, and we were able to pretty much support all the things that AirOps had.

**Daniel Lopes:** We still have some things that we have to tweak this week and improve a little bit, but I will walk you through everything and give you a glimpse of how the whole thing works.

**Daniel Lopes:** Keep in mind that some stuff will be a little bit slow because of the rate limiting that we're getting from Entropic, but I will show you all that.

**Daniel Lopes:** But let me walk you through, first, the export path we had.

**Daniel Lopes:** So, like, everything that you had in your accounts is now saved in the folder, and we built the environment for all these accounts.

**Daniel Lopes:** So, like, don't worry that if you don't see maybe some of the rows or maybe some of the articles that you had in the past, if you want to have access to them, they're all in our Google Drive.

**Daniel Lopes:** And we still have access to your existing.

**Daniel Lopes:** Senior Office account, for now, like I don't know what they, if they're going to cancel the account, when are they going to do that, or what, but let me share my screen, giving you one sec, I'll keep the chat open here on the side too, so if you have any questions, I can see.

**Daniel Lopes:** Oh, there you go, I think I can see everyone here, and I'll move you all to the side as well.

**Daniel Lopes:** If you see, you're looking to the side, it's because I have two more answers.

**Daniel Lopes:** Thanks.

**Daniel Lopes:** I might have the microphone on, can you?

**Matthew Panzarino:** If you wouldn't mind the muting.

**Daniel Lopes:** Nice, let me share my screen, and they might walk you through everything.

**Daniel Lopes:** So today, what you can do now, all right, is like you can go to, you're going to go to atlas.growfax.ai, and then you're going to be prompted with this screen.

**Daniel Lopes:** I think still has the mic on.

**Andi Bailey:** Oh, can you mute her directly?

**Bridget McGillivray:** You need to mute yourself.

**Ehtisham Hussain:** The host can mute.

**Bridget McGillivray:** Yeah, Daniel, just make somebody else host, then we can do it if it happens again.

**Bridget McGillivray:** Maybe make Atlas host?

**Daniel Lopes:** Close the screen, share it.

**Daniel Lopes:** So if you go to atlas.growfax.ai, that's our code name for this project.

**Daniel Lopes:** Instead of visiting your ops every day, you're going to be visiting this URL, you're going to be prompted to log in with your Google account.

**Daniel Lopes:** has to be growfax.ai or growfax.labs, like either one of those.

**Daniel Lopes:** Gmail is not going to work.

**Daniel Lopes:** So if you were using your Gmail before, let us know we have to migrate you to one of those emails.

**Daniel Lopes:** Once you log in, you're going to see a screen like this.

**Daniel Lopes:** And then we'll have all of our accounts.

**Daniel Lopes:** We have some things that we're still like, we might see like some test accounts and things like that.

**Daniel Lopes:** In the future, we're gonna hide those and have an option to hide them.

**Daniel Lopes:** And then we're also gonna have a place for like putting the archived accounts.

**Daniel Lopes:** We are setting up the accounts ourselves, so everybody, like you don't have to worry about setting up any new future accounts, that's gonna be part of the strategy spring to folks.

**Daniel Lopes:** So, but in the future, we might start making this easier for everybody to set it up.

**Daniel Lopes:** In reality, it's super simple.

**Daniel Lopes:** For us, Just go here, click new account, and then create a workspace, and then you start creating the pipelines, and log in, like automatically, anybody that has a Growfax account, if you try to log in, you get an account created automatically, so you signed up.

**Daniel Lopes:** So we know who you are, and we know, like, if you want to log out, log out buttons here.

**Daniel Lopes:** So that's a little hidden, but this is a pretty basic, and then we have, if you go in, in my, in production, in this domain.

**Daniel Lopes:** That you guys are seeing, it's going to be slightly different, so like if I go in, for example, let me go to, let me pick a test account here, so we have, Zuplo is a good one, so we have like Zuplo, when you go in, you're going to see this grayed out dashboard, like there's a bunch of features here that we're still building, and these are things that will come up in the next couple of months, I think.

**Daniel Lopes:** But you don't have to worry about that, I can walk you through all that at the end, just to give you a key glimpse of what we're building in the future, but for now, you're going to have this dashboard that has nothing, but then you have context artifacts, so context artifacts is a lot of the stuff that we were building before in AeroOps, in the cells, like the AI context, and the company context, and the personas, and all those documents, they would leave in the cell inside of AeroOps, in our case, now they have the specific AeroOps, got good again!-bye!-bye, gonna AW11 on that

**Daniel Lopes:** Where we can build and maintain them separately, and in the case of Zooplo, for example, we have here personas, like we're still working on making a text editor work, like a rich text editor, similar to like word prayers, and similar to even like Aerofs, they had the markdown rich text editor that's still coming in, like we think we're gonna have that ready probably today or tomorrow or something like that, and it's pretty much done, but here you see like a long document with everything that we write, wrote for the personas for Zooplo.

**Daniel Lopes:** If you edit this, you see that there is types as well, so you can choose a different type, so there's type selector here, for facts, for guidelines, rules, page templates, those will be things like listicles, how-to guides, and a bunch of other templates that the client might have that are specific to them.

**Daniel Lopes:** We're not using this much yet, so everything will be guidelines for now in the accounts that are set it up for you, and for now you don't have to do this idea.

**Daniel Lopes:** We did for all the accounts, and Marcel is going through all the existing accounts that didn't have very well-defined artifacts, and we are creating this for the account, and we also have templates here for the future, where you would be able to choose one of this, so whoever is setting up a new account in the future would be able to do that.

**Daniel Lopes:** You don't have to worry about this, I'm just walking you through the whole process for you to understand where things are coming from.

**Daniel Lopes:** So essentially now I have this list of artifacts that all the pipelines will be able to use, and we're going to keep a close eye on all the things.

**Daniel Lopes:** This has a huge impact on the quality of the output.

**Daniel Lopes:** So if the artifact is not great, the output is not going to be great, and that's why Marcel is doing a pass on making everything better.

**Daniel Lopes:** So, and then the main thing we have today that we're launching is the concept of pipelines.

**Daniel Lopes:** Like before pipelines, we also have projects.

**Daniel Lopes:** So account can have many projects, and in this case it's just

**Daniel Lopes:** So we have a bunch of accounts that we have more than one project, the vast majority will be just one project with just one project called editorial.

**Daniel Lopes:** And inside of this project we have pipelines.

**Daniel Lopes:** So pipelines are the equivalent of the grids from air ops.

**Daniel Lopes:** So in this case you have Zooplo here, we have a pipeline for assignments and we have a pipeline for article generation.

**Daniel Lopes:** We could also have, you also will see like a bunch of our accounts will have a pipeline for refresher.

**Daniel Lopes:** There was like a little bug yesterday when I ran the import script that didn't install the refresher for everybody, but we will run that right after the session.

**Daniel Lopes:** And I can actually show how to add one, but you don't have to add pipelines.

**Daniel Lopes:** will be doing, the client ops engineering team will be doing the setting up of the accounts for now.

**Daniel Lopes:** But in this case, Zooplo, we have assignments and article generation.

**Daniel Lopes:** Let me open the assignments one.

**Daniel Lopes:** and give you an idea, which is just a single step pipeline.

**Daniel Lopes:** So in this case here, we have an assignment pipeline with using URLs.

**Daniel Lopes:** we loaded here a couple of thousand URLs and we support importing CSVs.

**Daniel Lopes:** So same way as aeroops.

**Daniel Lopes:** Let me just refresh this, give me a sec.

**Daniel Lopes:** Then we broke the import button.

**Daniel Lopes:** I think we just made it deploy.

**Daniel Lopes:** This is something that might have broken the import button.

**Daniel Lopes:** We'll figure it out.

**Daniel Lopes:** But anyway, like I was, this, what is loaded here came from importing CSV, and I can show that import in a separate session.

**Daniel Lopes:** And once you have the values imported, same idea as aeroops, you can select as many things as you want, and you can run then with this run button.

**Daniel Lopes:** So the run button has similar settings as Aerox, where you could just run all the rows in the grid, you can run just the selected ones, and you can run the pending ones or the rows with error.

**Daniel Lopes:** So if I click on this, it would rerun that one, but we don't have to do that.

**Daniel Lopes:** The main thing to remember is that, like, the same way as, like, running a thousand things in Aerox would, like, not be good for their servers, it's the same thing with our systems.

**Daniel Lopes:** So if you run, like, a 5,000 grid, it would probably not be great.

**Daniel Lopes:** But, so avoid doing that, try to run in batches.

**Daniel Lopes:** We have the screen we paginate at 1,000, so you can only run 1,000 things at once, but even that, like, try to do it maybe in batches of 500, but we should be able to handle that.

**Daniel Lopes:** Once we have the things to run, the way to add something manually, if you're not using the CSV, would be to click on the Add button.

**Daniel Lopes:** The Add button will show you a form, and this form is defined based on how we create the pipeline.

**Daniel Lopes:** So this can have any inputs that we want.

**Daniel Lopes:** So in this case, for assignments, we chose an input of a URL, the checkbox for checking if we validate the relevance of this URL to the persona or not, and you can also guide the direction of the assignment.

**Daniel Lopes:** So this is a new field that we added.

**Daniel Lopes:** We didn't have support for that in our workflows before, but you can nudge the direction of the assignments.

**Daniel Lopes:** If I wanted to say, for example, what is OpenAPI?

**Daniel Lopes:** I'll clone, I'll do the same.

**Daniel Lopes:** I'll just grab this, and I'll create another one.

**Daniel Lopes:** And one sec.

**Daniel Lopes:** And I'll add this one.

**Daniel Lopes:** I don't need to validate the relevance because I know this is relevant enough if it doesn't find the keyword I will let it search for one and then I could direct the assignment saying I need comparison between open schema or I need to write without you.

**Daniel Lopes:** Understand.

**Daniel Lopes:** In this case because I have a board load of things added here and we still have to tweak the pagination it got pushed to the top so you can see here. Let me show you how to run this step.

**Daniel Lopes:** Let this run, so like you can either run from the grid, like same way you had with drops, you can run these things from here, so if you hover over the play button, you can see run this step.

**Daniel Lopes:** We have, I think, a little bug with the sorting, there you go.

**Daniel Lopes:** So if I hover over the play button, I see the run this step, so clicking on this would start this step.

**Daniel Lopes:** You can start things through clicking individually, or you can start things by selecting the checkboxes.

**Daniel Lopes:** In this case, I'll just go in.

**Daniel Lopes:** I don't have to run from here, I can also just click on the cell or in here.

**Daniel Lopes:** And we're also going to make this look a little easier to understand, like right now it's mixing the URLs with like the other fields.

**Daniel Lopes:** But if I click on this, you will see a timeline, in this case a timeline with just one step.

**Daniel Lopes:** This is the beginning, this is the form, so you can change the form again if you want to.

**Daniel Lopes:** And then the next thing you have here, and every time you change the form.

**Daniel Lopes:** I'm going to have a save button here under it, so let's say if I wanted to switch this to maybe TypeScript instead of Python, and if I save this, that will impact here and the grid, so it's like the same as changing like a cell on a grid in a spreadsheet, so like you see here, you see there, so it changed to TypeScript, there's kind of a little bit squeezed at the end, but you can probably see it, so if I go back in, this is my input, so I haven't run that step yet, so if I click play here, it will execute, so I can execute both on the grid, or in this view, step by step, so in this case, like if I click on that step that's getting executed, you see that we, now we have an explanation of what the workflow does, so this is a kind of little documentation explaining what the SEO content assignment brief does, and how it works, and you can see here all the input values that the word passed.

**Daniel Lopes:** We only typed URL and the direction, but we have a bunch of predefined default values that we are always passing based on how the pipeline was set up.

**Daniel Lopes:** So like in this case, the pipeline is always passing the company name, it's always passing the user context, personas, and some of the other artifacts.

**Daniel Lopes:** So you can see here the checkboxes that we chose, and at the end we also have the about, like the context of the company.

**Daniel Lopes:** So these are all the inputs that the workflow took, and it's still running, this one runs for about two minutes, three minutes, and I can always click on the inspect button as well.

**Daniel Lopes:** So the inspect button will take you to the studio user interface, and you can see all the things that are happening in detail here.

**Daniel Lopes:** So you can see that it's now analyzing the competitors and performing all that.

**Daniel Lopes:** So that one will run for a little bit, and once it's done...

**Daniel Lopes:** You're going to have access to the output tab.

**Daniel Lopes:** I'll let this run, and I'll switch to another one that I already did, the assignments.

**Daniel Lopes:** And then you can see, end to end, the final input would look like.

**Daniel Lopes:** Yeah, have support for dark mode, but we haven't tested that at all, so there's like some white borders and stuff like that around still, but we're going to fix that.

**Daniel Lopes:** So, like in this case, we ran the assignment already, ran for like four minutes.

**Daniel Lopes:** The output is this, so you can see the full output, and you can add it in this text form.

**Daniel Lopes:** You also have the short description at the end.

**Daniel Lopes:** The thing that I will explain at the end is always configurable.

**Daniel Lopes:** So, like this pipeline was built to take in this search of inputs with those form fields, and then we run whatever kind of steps we want, and at the end, we run whatever kind of outputs we want.

**Daniel Lopes:** So it's all very configurable, and in this case, it's just a very simple one-step pipeline that just outputs this text form mini-article.

**Daniel Lopes:** We are going to add the rich text editor, so this will be like, you're going to be editing this the same way as you would in Notion.

**Daniel Lopes:** And this will also have, like, an AI option to, like, select things and change the topics, change the content, change whatever section you want from that result.

**Daniel Lopes:** So that's already, like, baked in, and that will be shipped this week.

**Daniel Lopes:** So we will have, and also, like, when you're using the AI options in this environment here, we'll have access to all the context from the company and the writing guidelines and all the things, all the artifacts that we create.

**Daniel Lopes:** So it be contextualized.

**Daniel Lopes:** So in this case, this is the output of that step.

**Daniel Lopes:** It will also be the output of the final version of the whole thing at the end.

**Daniel Lopes:** So I think this one is pretty straightforward because it's just a single step pipeline.

**Daniel Lopes:** The more interesting one would be like an article generation pipeline.

**Daniel Lopes:** But that one I just wanted to show you how the assignments would work.

**Daniel Lopes:** We still have, like I said, a few things that we have to figure out of sorting and thinking up the resources of our servers, making the performance a little better in some of these screens that have more data.

**Daniel Lopes:** So this was the assignment, and I'll show you the article generation pipeline, and then I can answer any questions that you have, and then I can switch to showing how the pipelines are set up.

**Daniel Lopes:** Now I want to show you like a couple of...

**Daniel Lopes:** I want to show the article generation, I want to show an article...

**Daniel Lopes:** Refresher, almost everybody will have it set it up in their accounts too, and it works a little different, but article generation on Marcel, let me grab a URL directly to the right page here, because we need to make our pagination a little better.

**Daniel Lopes:** So this one, have, I will change the pagination already, nice, think, page two, maybe page one, okay, last thing on the page one, okay, so increase the pagination to a thousand, somebody just did it, Marcus, just deployed, I think.

**Daniel Lopes:** So we have, in this case, we have Zuplo, we loaded like 200, about 200 topics that we wanted to write about, and then you see that this pipeline has you're we'll

**Daniel Lopes:** It's multiple steps, so we have, starts with a brief, and then goes into the research, and an outline, and then a draft, fact checking, and then style, and then adds the internal linking.

**Daniel Lopes:** The thing to keep in mind now, is that the thing that changes with this compared to Aerofs, is if you run from the check boxes here, and you press this run button, you run all the way to the end.

**Daniel Lopes:** Like, you don't have to do anything, we just execute all the steps, one from another.

**Daniel Lopes:** So you can just press play, let it run for like, some of our stuff now might take like 10 minutes, because of like the rate limits that we're getting from, from Entropic.

**Daniel Lopes:** So you can just let it run, and then you come back and you fix whatever you wanted at the end.

**Daniel Lopes:** So like, in this case, I'm just going to run these three ones, and I'll let them execute, and I will show you the one that was executed already.

**Daniel Lopes:** So it'll be like, you run like this, and then we execute the next one, the next one, the next one.

**Daniel Lopes:** And you can always execute in manual mode as well, if you want.

**Daniel Lopes:** So we're going to make that more clear.

**Daniel Lopes:** It's distinct, but when you run from that checkbox, run in automated mode, but if you go like clicking cell by cell here, it will run to that step, pause, and then you can continue in the next step, so very similar to what we had with Aerofs before, or if you open like this in this view, in the open up view, you can, and you run step by step, you run step by step too, so we will add an option from here to like run continuously from this view.

**Daniel Lopes:** view from this view as often this screen, but in this case here we have fully empty, just the topic, so I would have to like type in the direction if I wanted to, and these are optional fields, so like all the, all the assignment, sorry, all the article generation and the refreshers are set up with internal linking, using some of the new workflows that Kirkland built, and we also have the fact check, and you have the option to define which domains to fact check again, against.

**Daniel Lopes:** So if the client has a documentation, we could put the docs here, and it will like narrow the search into that domain.

**Daniel Lopes:** So let me open up something that has already completed a few steps and I can show you on there.

**Daniel Lopes:** We have the last one.

**Daniel Lopes:** So this one, the initial input that Marcel added was ESPN API, and then just a rough direction for the assignment.

**Daniel Lopes:** Another thing we can do is that when we define the pipeline, we can define defaults.

**Daniel Lopes:** So this one didn't have any defaults for anything.

**Daniel Lopes:** I think it would have the default for the domains, actually.

**Daniel Lopes:** But we can also have the default for the direction of the assignment.

**Daniel Lopes:** So anything here that you see yourself typing too many times, we can make that a default in the settings of the pipeline.

**Daniel Lopes:** So...

**Daniel Lopes:** Oh, Kirkland is asking something, this issue, main thing is that...

**Kirkland Gee:** They just answered what I was looking at, that there are defaults for these things, I was just filing.

**Daniel Lopes:** I think we're good.

**Daniel Lopes:** Yeah, okay.

**Daniel Lopes:** There's like a little bug with like, not a bug, but there is something with the fact checker that is like very strict.

**Daniel Lopes:** So if you pass just one domain, it's going to just look at that domain only.

**Daniel Lopes:** Or if you pass an empty space here, we'll look at no domains, so we're going to fix that.

**Daniel Lopes:** But anyway, in this case, we passed this data.

**Daniel Lopes:** The first thing it did was to create the assignment brief.

**Daniel Lopes:** So the output of the brief was pretty much the same stuff that Marcel had asked, and at the end we have a proposed structure that will guide the outline.

**Daniel Lopes:** Then the next thing it did was the research.

**Daniel Lopes:** So like we have research, full mark down here, once we add the rich text, editor, will be easy to read what was the result and we'll be able to customize whatever you want.

**Daniel Lopes:** From the research here, can delete things, can add things, and then the outline, we're also going to add the XML editor, so you will be able to see things a little better here, but it's the same idea we had before, and you can always switch between input and output to know what came in, so like in this step, what came in was this step before, so the research data came in, and you can scroll down and see all the fields, so it was the research and the assignment, and let's see what else, I think that's it, and so like if scroll back to the top, I have the output of that, was this outline, so I will also show you how you can rerun the steps, and that will create attempts, and you can customize the input and output, so you have full control, the same way you have in Aerox, and then you have article draft, that was the next step, that took six minutes, if you're curious to see why it took six minutes, you can click and inspect, and you can see the breakdown,

**Daniel Lopes:** So the polishing of the article took three minutes.

**Daniel Lopes:** Everything else took like a minute in parallel.

**Daniel Lopes:** The polishing takes so long because it would take a ton of the instructions that we have and run that record for.

**Daniel Lopes:** So that's pretty slow compared to some of the other models, but the result is pretty good.

**Daniel Lopes:** So that's kind of the theme of like our last update is that everything is kind of pretty slow now because we're using Claude for almost everything, but the output is much better.

**Daniel Lopes:** So that's kind of a trade-off that we've made.

**Daniel Lopes:** We might have to add an option to switch models to like a simpler model when we don't have such a high bar for quality.

**Daniel Lopes:** But if you see here's like five minutes for the assignment, two minutes for the outline, six minutes for the draft, and then five minutes at the end to apply the style again.

**Daniel Lopes:** But fact-checking.

**Daniel Lopes:** the fact-checking token, so like I said, like we always have the...

**Daniel Lopes:** The description of what the workflow does, and if you actually want to see further, can always click on the inspect, like I reinforce that, like if you have a bug, if you have a problem, like always click on the inspect first before reporting, because that will give you some ideas of what might be the problem.

**Daniel Lopes:** Like if you're seeing a bunch of errors here, we're likely hitting a problem with rate limiting with like with Entropic or OpenAI or whatever.

**Daniel Lopes:** If you actually want to go a step deeper into like the more technical side, then you can also click on workflow here.

**Daniel Lopes:** And then you see the stack trace, like the actual execution of everything.

**Daniel Lopes:** You don't have to do that.

**Daniel Lopes:** That's more for us on an engineering side.

**Daniel Lopes:** But always, please always read this so you have an idea of what that step does.

**Daniel Lopes:** So in this case, effect checked, and it rewrote the whole article.

**Daniel Lopes:** Let's see here, nothing special.

**Daniel Lopes:** And then

**Daniel Lopes:** And the next step is the adapting of this style.

**Daniel Lopes:** So adapting of the style.

**Daniel Lopes:** So all the accounts have this.

**Daniel Lopes:** This will be like heavily based on the writing guidelines in the artifact.

**Daniel Lopes:** So if I go to go back to Zuplo's artifact, we have this writing guidelines.

**Daniel Lopes:** Now we need to tweak our servers.

**Daniel Lopes:** They're running too slow.

**Daniel Lopes:** But sorry, I meant artifacts.

**Daniel Lopes:** So artifacts, we have writing guidelines.

**Daniel Lopes:** So for Zuplo, we have a bunch of examples of bad examples, good examples.

**Daniel Lopes:** If you have an account that does doesn't have this kind of setup, let us know, or try to improve that, and then let us know after.

**Daniel Lopes:** Because this makes a huge difference in that step.

**Daniel Lopes:** So we actually tried to do that for all the accounts.

**Daniel Lopes:** We or seven left that we still have to tweak a little, but the style adaptation here is taking in the writing guidelines, so if we scroll down here you can see inputs, and then you can scroll down and you can see what were the fields that were taken in, so it took the whole article and it took the additional style guidelines, so this is the writing guidelines, and the output will be the article, and this one we didn't run the internal links, so let's say I wanted to change this for example, so I could come here and edit anything that I don't like from the article, like for now, like I said, this is the main thing that I think almost makes it too hard to use, is the lack of the rich text editor here that we're going to add either today or tomorrow, but anything that you change here, you can save, and then it will be used.

**Daniel Lopes:** for the next.

**Daniel Lopes:** So this step, like, once this step hasn't, we haven't executed this step yet, they'll also, like, have a tutorial explaining what the step does, and then you hit play, and then it will start.

**Daniel Lopes:** So you see the attempt running, and then it will take in, and it will process the thing, and you can monitor the execution in there.

**Daniel Lopes:** One thing that you can always do, you can always go back, and you can always change the value, and, like, in this case, I changed the value, and you see, like, a modified little badge at the top, so I can revert to the original, so any change that I make, I can revert to the original, and I can save it, and then we'll, then I can run again.

**Daniel Lopes:** So I can stop this step, and I can run that step again.

**Daniel Lopes:** So, this case, now it will run with this, with the original version that had the community part, and any

**Daniel Lopes:** You can always also see like some of the other things we have that you don't have to parameterize that are already coming in with the default values from the pipeline.

**Daniel Lopes:** So this will try to look for like five links to add, and then you can also have the option to pass manual links and all that.

**Daniel Lopes:** It's just not set up in the pipeline.

**Daniel Lopes:** So a lot of the things are like hidden, so you don't have to worry about when you're clicking on adding things, like the form is predefined for you.

**Daniel Lopes:** But any of the things that you see as inputs in any of the steps are things that we can customize and have the default set for your account.

**Daniel Lopes:** So in this case, sorry, you don't need to see that.

**Daniel Lopes:** So you see that we have also two different attempts here.

**Daniel Lopes:** So there's this little drop-down with attempts on top.

**Daniel Lopes:** In this case, because I stopped the attempt, if I switch back, there will be no output.

**Daniel Lopes:** So the output is empty.

**Daniel Lopes:** But if I go to the attempt that is running now, it's still running.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Thank

**Daniel Lopes:** So, this is basically a pipeline that we'll be using on a daily basis.

**Daniel Lopes:** This is the full replacement for article generation.

**Daniel Lopes:** Let me show you one more, and then I can see if there's any questions in the meantime.

**Daniel Lopes:** Yeah, so Marisol asked if we can change the output of each step in the pipeline view before running the next step.

**Daniel Lopes:** Yeah, you can.

**Daniel Lopes:** So, like, it's like, like what I was saying.

**Daniel Lopes:** So, like, if you go, like, any, any moment here, I would change this one.

**Daniel Lopes:** Let me see if there's another one so I don't break this one that took a little bit too long.

**Daniel Lopes:** Let me see if there's what's the state of superhuman.

**Daniel Lopes:** And let's see the state of...

**Daniel Lopes:** These are the two ones that I had running before.

**Daniel Lopes:** Yeah, so this one had a bunch of problems because that was when Entropic was like really failing.

**Daniel Lopes:** So, let's say for example, I wanted to change the outline for this.

**Daniel Lopes:** So the first thing here, like we can see the input and output, the brief.

**Daniel Lopes:** So like if don't like the brief, we could.

**Daniel Lopes:** Change this a little.

**Daniel Lopes:** Save it.

**Daniel Lopes:** So saving it.

**Daniel Lopes:** You can see the modified.

**Daniel Lopes:** you hover over, you also will see what changed, but if it's too much text, then it's hard to follow.

**Daniel Lopes:** We might add some interface for that later.

**Daniel Lopes:** So I save that.

**Daniel Lopes:** So the next thing I would have to do is rerun the research, if I want to run the research.

**Daniel Lopes:** If I just wanted to do the outline, sorry, I changed the outline, so everything else below that, under it, became fresh steps.

**Daniel Lopes:** So I have to run them again.

**Daniel Lopes:** In this case, if I run the article draft now, you see that will come in with the new outline.

**Daniel Lopes:** I changed the brief.

**Daniel Lopes:** Yeah, I changed the brief.

**Daniel Lopes:** didn't run the research.

**Daniel Lopes:** I should have run the outline.

**Daniel Lopes:** Let me just run the outline again.

**Daniel Lopes:** So the outline is usually fast.

**Daniel Lopes:** Then you can see here that the brief changed.

**Daniel Lopes:** ahead, me break at

**Daniel Lopes:** Which if I scroll down, the brief is this, so whatever I do in the step before, in the output will be passed down, I hope that answers the question, and then I have to execute everything after that to take that into consideration, so I'll just run this one again, and let it run, this one is actually running, this one I want to see the cover image, because this one generates cover images as well, and I wanted to show you how the cover image works, but, let me go back to the refresher, so you see that like today, after this session, we will load all the accounts with article refresher, so the article refresher will be here, similar to the article generation, but the difference now, that it will take in a URL, and it will take refreshing instructions, so the refresher instructions, that are set.

**Daniel Lopes:** For everybody is just focused on updating the article with new research data or statistics and new data points for newer things.

**Daniel Lopes:** But it could be anything.

**Daniel Lopes:** So if you have something that you need to do with a specific article, like if you need to, like, in your case, if you're always adding new sections, or if you're always adding quotes for certain people, we can parameterize that for you.

**Daniel Lopes:** And then you have that default value, or you can change that yourself here and see how that behaves, and then you can send us the data after and we can add that to your pipeline.

**Daniel Lopes:** So in this case, we had this article from Superhuman that had a bunch of data.

**Daniel Lopes:** I don't think we wrote this, but I just found something on their blog that had a bunch of data around metrics and things.

**Daniel Lopes:** So in this case, if we run the refresh instructions, we'll just try

**Daniel Lopes:** You can see here there's some things about nofollow if you're adding citations to other websites and things like that.

**Daniel Lopes:** This is all customized.

**Daniel Lopes:** This is a prompt, so it can be anything.

**Daniel Lopes:** And then we're also going to try to add more internal links.

**Daniel Lopes:** So in this case, we ran a simple SEO analysis here just to see what are the keywords that we are ranking for.

**Daniel Lopes:** And then you see the output for this one is slightly different.

**Daniel Lopes:** The output here is outputting a list.

**Daniel Lopes:** So it's showing here the two keywords that it's already ranking for.

**Daniel Lopes:** And it tries to fetch up to 30 organic keywords.

**Daniel Lopes:** If you don't know how that works, you can go back to the input and you can read what it does.

**Daniel Lopes:** And then if you, like I said, you can always click on the inspect.

**Daniel Lopes:** And I really recommend you to click on the inspect.

**Daniel Lopes:** And then research generation.

**Daniel Lopes:** So it did research to try to figure out what is valuable for this article.

**Daniel Lopes:** So you can see here the goal for the refresher was I'm working on improving this article and it has the whole article there.

**Daniel Lopes:** care.

**Daniel Lopes:** And then at the end, it has what we're trying to do with this article, with those instructions that we had about extending the article.

**Daniel Lopes:** And you can see the other values that we're using.

**Daniel Lopes:** So we used perplexity, deep research, and some of the other attributes we could pass for our deep research that we didn't use in this case.

**Daniel Lopes:** The next thing that happen automatically is just to go into SEO analysis, research generation, article refresh, applied internal links, and we're also adding an FAQ at the end.

**Daniel Lopes:** So that's a step that all the refreshers have.

**Daniel Lopes:** You don't have to use the FAQ, but the last thing that we'll get here in this case will be the full article with all the new updates.

**Daniel Lopes:** So the article was from 2021, I think.

**Daniel Lopes:** And then we have a few new metrics updated here because of the deep research that we ran.

**Daniel Lopes:** So, and then...

**Daniel Lopes:** In this case, we're not outputting the FAQ, that's something we're going to add, like it should have outputted, but you can see the FAQ results here, so FAQ was added here, what are some effective strategies for implementing wellness challenges in hybrid remote work environment, so a couple paragraphs, and you can always make the FAQ shorter or longer, that's part of the inputs that we can take, and yeah, so that's the result of the FAQ, but not everything that will be part of the input and output of the steps will be part of the full output, so we just, we curate whatever you think is valuable for the final output, and then, like I said, in a couple of days, we'll have an editor here that you can come in, and you can edit things in line, you know, with AI Assist, and we can also add as many steps as we want.

**Daniel Lopes:** We can have a step for posting things to web flow, posting things.

**Daniel Lopes:** Let me see if there are any questions here.

**Daniel Lopes:** Should we have versioning here?

**Daniel Lopes:** For example, when I go in and change the writing guidelines, can be saved as version one?

**Daniel Lopes:** Yeah, have version already for the artifacts.

**Daniel Lopes:** So you see there, for example, Let's say if I change the writing guideline here, you see there is a history with versions.

**Daniel Lopes:** We just don't have a way to switch to that version and use that for a certain pipeline.

**Daniel Lopes:** Whatever you have as the last version will be used, you know?

**Daniel Lopes:** And we also have a way to show the difference between the versions yet, but that's easy to add and then we can add some.

**Daniel Lopes:** Here, is there a way to tell which pipeline you're in?

**Daniel Lopes:** Looks like...

**Daniel Lopes:** Once you're in the pipeline, you can see which clients, oh, that's a good, yeah, that's an easy one.

**Daniel Lopes:** I'll just post that in the Slack, and then I'll create a ticket for that after.

**Daniel Lopes:** I'll share with you at the end how you can file your questions and feedback and requests.

**Carrie Chowske:** I think Kirkland said they already got it.

**Daniel Lopes:** Nice, cool, yeah, this one is taking eight minutes, let's see why.

**Daniel Lopes:** SEMrush data, so SEMrush seems to be stuck.

**Daniel Lopes:** The recording has stopped.

**Daniel Lopes:** Yeah, something is off with SEMrush.

**Daniel Lopes:** If something looks off like this, you can always, and if you need that, you can always stop.

**Daniel Lopes:** And run again.

**Daniel Lopes:** There's no way to...

**Daniel Lopes:** Heap a step for now, so that's something that we are considering, which at least let you manually set the values for that step without running it, so that's something that we have in the pipeline that we could ship even like this week if we need to, so yeah, let's see the refresher, refresher, yep, see if there are any other questions, what is the FAQ generation pulling from David's question, so like in this case you can see here, so it's a pulling a bunch of things from perplexity, and it can also be based on fixed questions that you have, so in this case we are not using fixed questions, we're just trying to guess the questions out of the content, and then we will run a bunch of perplexity queries of Sonar Pro, Sonar

**Daniel Lopes:** SonarPro is the in-between.

**Daniel Lopes:** So there's like three models for research with perplexity.

**Daniel Lopes:** One is super light, and it can be off, and it can be not the most up-to-date things.

**Daniel Lopes:** And then you have the SonarPro model, and then you have the deep research one that runs very slow, takes like five minutes or more, and gets everything right.

**Daniel Lopes:** So, or almost everything right.

**Daniel Lopes:** So in this case here, we run the first step with deep research.

**Daniel Lopes:** So if you scroll down, you see a sonar deep research.

**Daniel Lopes:** So the initial research for improving the article comes from there, and then the FAQ questions come from the simpler one.

**Daniel Lopes:** If that makes sense.

**Daniel Lopes:** And if you want to see how that happens, you can go to inspect, and you can click in description.

**Daniel Lopes:** So, and then you can zoom in here.

**Daniel Lopes:** We need to make this interface better.

**Daniel Lopes:** But you can see if it hits the number of maximum questions.

**Daniel Lopes:** If you want the JSON-LD or if you want markdowns and things like that.

**Daniel Lopes:** So that's kind of the gist of the default workspace for everybody.

**Daniel Lopes:** So you have like these three pipelines with an editorial project, some more complex clients, for example, Webflow, for example, has multiple projects.

**Daniel Lopes:** We have this like little hidden placeholders that are for future features. I'm going to remove that just so the interface is cleaner.

**Daniel Lopes:** So you don't see like these empty spots.

**Daniel Lopes:** But in the case of Webflow, they have a glossary, they have an editorial stuff.

**Daniel Lopes:** Their glossary is essentially refreshing, like much more focused on refreshing.

**Daniel Lopes:** And then they have editorial, which is like normal publishing.

**Daniel Lopes:** And they have an integration page that's more like programmatic.

**Daniel Lopes:** So like all those things are set up as different pipelines. So we can build whatever type of workflows work best for each customer. So in this case, it's just one call, it's like a step with like one call, and we'll generate everything at the end.

**Daniel Lopes:** Let me see another one, that could be interesting.

**Daniel Lopes:** Prophecy is another one that has podcasts, so Prophecy, the pipeline behaves different.

**Daniel Lopes:** So we start with like a URL for a podcast, and then it finds opportunities out of the transcript.

**Daniel Lopes:** So we transcribe the whole audio file into opportunities, and then you choose the opportunities you want to work with, and then you get an outline, and you get sections from that, and then the post-processing, and then do the internal linking.

**Daniel Lopes:** One thing that I wanted to show as well is this, now we have the idea of archiving roads.

**Daniel Lopes:** So in air ops, you would have like these super long grids of stuff that you already finished. In Atlas, we can clean that up going forward.

**Daniel Lopes:** So one thing that I ask you to do now is like every time you finish something end-to-end and you put it in their table or you published, just archive that.

**Daniel Lopes:** That will give us an idea like of how many things you're completing and like what got done in that account and also just going to clean up your grid.

**Daniel Lopes:** So let's say, for example, for Zuplo, which was right in here.

**Daniel Lopes:** The ESPN one.

**Daniel Lopes:** Like everybody in the engineering channel, they're seeing all the stages that are loading a little slow and they're like looking at how to fix it though, right?

**Daniel Lopes:** So that's the benefit of having our own internal team.

**Daniel Lopes:** So like everything that you're seeing today will be like quite different by the end of the week.

**Daniel Lopes:** So let's see in a better way, like all the little bugs and the slowness.

**Daniel Lopes:** And all that should be fixed pretty easily. Then we have, like in this case, for example, let's say I'm done with this, or let's say I don't want to work with this. We have two options: archiving and deleting.

**Daniel Lopes:** So if you don't want to work on these three rows there, you could just delete them.

**Daniel Lopes:** So the three rows are deleted.

**Daniel Lopes:** So that's gone.

**Daniel Lopes:** There's no way to restore that.

**Daniel Lopes:** If I want to archive something in the sense of saying that I'm done with it, and I don't need to see it anymore.

**Daniel Lopes:** You can just come here, and then you have an archive button at the end.

**Daniel Lopes:** So everything that's archived will be here in a separate tab.

**Daniel Lopes:** So as you go through, archive everything, close it.

**Daniel Lopes:** Over time, we're going to also add a separate place for staging the content.

**Daniel Lopes:** So like your client could come in and interact with you, like, almost like replace the need for sending people, sending stuff here.

**Daniel Lopes:** may WHO there withal it's It's I've you're giving to me…

**Daniel Lopes:** But that's for later, and the staging we also publish in the different CMSs, but that's for the future.

**Daniel Lopes:** I think that kind of covers the most, the day-to-day operations of things, like how to execute the grids and how to interact with the outputs and all that.

**Daniel Lopes:** Like I said, I think the main thing missing here is the rich text editor.

**Daniel Lopes:** The other thing that I wanted to cover is that all these things are super flexible.

**Daniel Lopes:** So setting up the pipelines for us now is super fast, and we can stitch together whatever mix of workflows we want.

**Daniel Lopes:** And it's all written in text.

**Daniel Lopes:** So if you're curious to see, it's kind of a dangerous change, like don't save this.

**Daniel Lopes:** But if you want to see how the pipeline is set up for anything that you have, you can click here and edit pipeline.

**Daniel Lopes:** And then you see all the steps, and you see the form, and you see all the output fields as well.

**Daniel Lopes:** So this is how we define the pipeline.

**Daniel Lopes:** So you.

**Daniel Lopes:** So, in this case, for example, we have an input schema that has these four fields for the form.

**Daniel Lopes:** So, when I click here and I click Add, those are the four fields I see.

**Daniel Lopes:** So, the form is fully customizable.

**Daniel Lopes:** whatever we want can be like regular fields, text area, multiple choice, checkboxes, URLs, like all these things.

**Daniel Lopes:** And then the output is whatever I want at the end.

**Daniel Lopes:** So, the output, in this case, I'm saying I want a rich text.

**Daniel Lopes:** The rich text is not there yet because it hasn't shipped, but the moment that we ship, we've got to switch to rich text.

**Daniel Lopes:** And the default value of that will be that value from this output step called internal links.

**Daniel Lopes:** So, we can just like parameterize this however you want.

**Daniel Lopes:** And then the steps here are our workflows.

**Daniel Lopes:** So, function name is the name of the workflow.

**Daniel Lopes:** So, we have, today it's all pretty red because of entropic, but if I open.

**Daniel Lopes:** In the studio, see, like, this is all the workflows we have, we have 100 workflows, and we can stitch them together however we want.

**Daniel Lopes:** So, like, those are the steps in the pipeline.

**Daniel Lopes:** And then you have all the things that you can parameterize.

**Daniel Lopes:** Some steps, we can, like, pass default values and all that, that's how we are passing all the things that you don't have to worry about as you're just executing.

**Daniel Lopes:** But everything is customizable.

**Daniel Lopes:** So, I hope that explains most of the system.

**Daniel Lopes:** It's 43 new messages here.

**Daniel Lopes:** Let's see what I missed.

**Daniel Lopes:** Mariana.

**Daniel Lopes:** Yeah, Mariana, two clients that we're missing.

**Daniel Lopes:** So, yeah, your client is the one that we're missing.

**Daniel Lopes:** if you, the one that I didn't have the time to finish.

**Daniel Lopes:** But we have the spreadsheet here with, let's see.

**Daniel Lopes:** Give me one sec.

**Daniel Lopes:** Give

**Daniel Lopes:** I'll pull this spreadsheet now and explain the state of all the clients.

**Daniel Lopes:** Yeah, so we migrated all the 39, 37 clients.

**Daniel Lopes:** The two that they were missing is the Adventurous Group and the Zooplo.

**Daniel Lopes:** Zooplo has a simple editorial and the Adventurous Group, I think, as well.

**Daniel Lopes:** If I didn't add like a web, so you can just play with it, but we will add the real grids with the real stats for like all the different accounts.

**Daniel Lopes:** The only reason is that we ran out of time, but Adventurous Group has essentially like five different projects inside.

**Daniel Lopes:** So we're going to have, once I set it up, you see them as projects on the side of the Adventurous Group workspace.

**Daniel Lopes:** So, I'll set up that for you in the morning, so you can play with like, if

**Daniel Lopes:** If you want to try something before you have your account set up, you can do things with MySpace.

**Daniel Lopes:** So I have an account here called Daniel Sandbox.

**Daniel Lopes:** And you can play around with the article generation there.

**Daniel Lopes:** Let's see, what else?

**Daniel Lopes:** Yep, Matthew's asking if the research outline work closes direct lift from the Aerobs.

**Daniel Lopes:** Yeah, so everything is the exact same stuff we have in the Aerobs.

**Daniel Lopes:** The only thing that changed is how we stitch them together in the new user interface.

**Daniel Lopes:** Jess, can we edit the outline?

**Daniel Lopes:** Kirkland already answered.

**Kirkland Gee:** So Kirkland pretty much answered all the questions there.

**Kirkland Gee:** I really tried to address, I think, oh, I think I addressed all of the questions here.

**Kirkland Gee:** The only one that it's probably worth talking about is like running pipelines to a certain step.

**Kirkland Gee:** So if you wanted to only run up into the outline and then pause it, I wasn't quite sure how that would work.

**Daniel Lopes:** Yeah, that we don't have support for.

**Daniel Lopes:** So like, what I would recommend now is just like, let it run all the way to the end, and then come back to that point and then run again after.

**Daniel Lopes:** But we can add that, it's like a couple of days, you know, so that's something that we wanted to add, we just didn't have the time to do it.

**Daniel Lopes:** So like, there's like, there's all these things about the running of things and running them automated versus running the manual that we need to tweak.

**Daniel Lopes:** But yeah, so if I were to do that, like in this case, I would just like hit this, run, let it run.

**Daniel Lopes:** So this will run all the way to the end, and then I would come back in the outline phase, and then change it, and then run again, and then let it run all the way to the end.

**Daniel Lopes:** to end.

**Daniel Lopes:** Let's see, maker on folders, have clients that get editorial glossary, yes, Jess, like, in this case, like, file that with us first, like, let us do that for you, and then, like, one thing we're gonna do in the next couple of weeks is add a few that you let people know, set up the pipelines themselves, but setting up the projects now, setting up the pipelines, requires understanding this, which is a little bit too much, you know, too complex.

**Daniel Lopes:** So, any of the clients that you need to set up different, or that you need to add, like, I try to port all the things that we had from Aero Ops, and, like, they are the same steps that you had there.

**Daniel Lopes:** It's like, for example,

**Daniel Lopes:** Maybe I might have missed some, but if you go to, like, let's say, Rapid is one that has a different step.

**Daniel Lopes:** So you see that they are not just the same over and over, they are slightly different.

**Daniel Lopes:** So like Rapid has different stock cover image and has this dual tone effect at the end.

**Daniel Lopes:** it's just missing their XML.

**Daniel Lopes:** So I have a little list of, like, a couple of clients that need customization.

**Daniel Lopes:** And those are these ones here.

**Daniel Lopes:** Let me show you.

**Daniel Lopes:** So the ones that you still need to tweak a bit.

**Daniel Lopes:** this crappy fact checker, they have their special fact checker that wasn't working in the new system that we need to adjust.

**Daniel Lopes:** The dual tone and the XML steps from Rapid we need to tweak today.

**Daniel Lopes:** The data grid post into Webflow.

**Daniel Lopes:** We don't have that.

**Daniel Lopes:** don't that.

**Daniel Lopes:** Let's do

**Daniel Lopes:** We support for that.

**Daniel Lopes:** So we have to do the posting by hand for now.

**Daniel Lopes:** All the workflows, want to add the title and metadata as a field to the final output.

**Daniel Lopes:** And Zoopo has the programmatic APIs grid that we haven't set up yet.

**Daniel Lopes:** And Tag, have to, the adventures group, have to set up everything.

**Daniel Lopes:** So those are the last over ones.

**Jess Scott:** Okay, that makes sense.

**Jess Scott:** Thank you.

**Jess Scott:** The other, so some of my clients I've been, like, we've been doing mostly in ChatGPT, so I'll just drop a note with, like, the other buckets we need.

**Jess Scott:** Can we also get, like, a URL generator?

**Jess Scott:** Or, like, the slug?

**Daniel Lopes:** Yeah, we have that.

**Daniel Lopes:** So that's what I mean.

**Daniel Lopes:** I forgot you had that.

**Kirkland Gee:** Yeah, there's one workflow, I think, from AirOps that does title, meta description, slug, and one or two.

**Daniel Lopes:** But that one also does a full rewrite of the article.

**Daniel Lopes:** don't need that.

**Daniel Lopes:** Right.

**Daniel Lopes:** That's why I didn't add.

**Daniel Lopes:** It can be much faster without the FURI, right?

**Daniel Lopes:** Yeah, let me see.

**Jess Scott:** Cool, Any other questions?

**Daniel Lopes:** Yeah, I know this is a lot.

**Daniel Lopes:** We'll send you a follow-up with things for you to try and things for you to play with and how to test your environment.

**Daniel Lopes:** Like I said, I cannot remotely prepare like I wanted to.

**Daniel Lopes:** I wanted to have practice sessions and let you all try the interface and all that.

**Daniel Lopes:** We'll send you a message.

**Daniel Lopes:** After this call with like guides of how to use this and Essentially like today just play with it.

**Daniel Lopes:** See if we can generate some stuff, click around and see see how it works and One final thing if you have any Things that you want to report, you can just go into the client ops Team here you can just file Anywhere actually you can just click on this compose button at the tip can it

**Daniel Lopes:** At the top, select one of the templates that Andy created, I would probably, they will probably fit in these two categories, is either like something that you want to do with workflows, or it's an app bug, in this case, an app is Atlas, or this studio, those are the two apps we have.

**Daniel Lopes:** And if you have something that you want improve workflows, this would be the choice.

**Daniel Lopes:** This week, I think we're going to get a lot of those.

**Daniel Lopes:** So pick this, and then if you have a specific client you want to describe, that you want to, you're working with, like, please share here, and share the workflow URL, or the, I'll update the template to be either workflow URL, or pipeline.

**Daniel Lopes:** Just send us as many links as possible, and share as much context as possible.

**Daniel Lopes:** And then you can also message us in Slack after you do that.

**Daniel Lopes:** So start with the linear ticket first, and then send us the linear ticket in Slack in the same channel.

**Daniel Lopes:** So we can use the same channel from before, so like if you do that.

**Daniel Lopes:** Click our request, create your linear ticket first and then link to it here and then we can figure out where to put it out to triage and all that.

**Daniel Lopes:** So this week will be pretty much all of us in bug mashing focus and just paying attention to everything that's happening and improving the product as fast as we can.

**Daniel Lopes:** Cool, everybody.

**Daniel Lopes:** Sorry for being a couple of minutes late.

**Daniel Lopes:** I hope this helps a little.

**Daniel Lopes:** I know it's like a drastic change.

**Daniel Lopes:** It's a change of user interface.

**Daniel Lopes:** It's a change of like how you do things.

**Daniel Lopes:** And at the same time, like we haven't really, really, really key away the product a ton.

**Daniel Lopes:** I expect that today and tomorrow will be a little bit bumpy, but this thing's like get ironed out pretty fast.

**Daniel Lopes:** Cool.

**Daniel Lopes:** Thanks, everybody.

**Daniel Lopes:** you very

**Daniel Lopes:** I think that's it.

**Daniel Lopes:** And if you have any questions, file them in the request and feedback for now, and we will send you a follow-up message with things a little bit more.
