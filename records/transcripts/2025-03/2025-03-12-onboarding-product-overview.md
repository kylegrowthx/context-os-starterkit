# Onboarding: Product Overview

<metadata>
date: 2025-03-12
time: 18:02 UTC
duration: 35 minutes
organizer: daniel@growthxlabs.com
participants: Daniel Lopes, Dave Capone, Felipe Lima, Marília Caroline da Silva, Sydney Go, Ericksson Abad
fathom_recording_id: 51567138
fathom_url: https://fathom.video/calls/250659359
share_url: https://fathom.video/share/Wfm_AHmLoXk5ixHgJV5LHQ3MKi6ws7ys
source: fathom
enriched_on: 2026-03-04 17:15 UTC
</metadata>

---

## Summary

Daniel Lopes walked four new GrowthX team members (Felipe, Marília, Sydney, and Ericksson) through the company's "team-as-product" philosophy and the custom Flow AI workflow engine that powers their content automation. The team documented 32 workflows and aims to hit 100+ by mid-year, with the goal of enabling non-technical staff like Marcel to create workflows by end of year. The technical stack uses Flow (a proprietary engine built for rapid prototyping) plus AirOps as a temporary UI, with plans to build a unified internal tool to replace Notion, Airtable, and AirOps while eventually allowing model training on company-specific writing styles.

---

## Context

GrowthX is a B2B services company offering high-ticket content marketing engagements ($200k+/year), built on the insight that AI can enable marketing-level productivity gains similar to what programmers have achieved. Rather than build a traditional SaaS product immediately, Daniel and Marcel chose a "service as software" model: the delivery team operates as the product, identifying client problems and funding R&D to solve them. This onboarding session was for four newly onboarded team members learning the product and development philosophy they'd support in their new roles.

---

## Relevance

**To GrowthX Delivery:**
- Services team is intentionally the product, not a path to replacement — their client requests directly fund R&D priorities.
- Current bottleneck is design/image generation (multiple client requests this week for realistic images, art covers, diagrams).
- Two-phase workflow: strategy phase (documents and client alignment) → production phase (AirOps + LLM calls + manual QA + publication).
- Building unified internal tool prototype this week to replace Notion, Airtable, and AirOps UI fragmentation.

**To CheckThat / AI Visibility:**
- Workflow engine treats prompting as a programming language, uses GitHub for version control, approaching prompt engineering rigorously.
- Collecting instrumentation data from all edits to eventually train custom models for company writing style and client-specific variants (e.g., Claude variant for GrowthX voice).
- Image generation workflows use multi-step brainstorming (20 ideas → AI judge → parallel execution → client selects from 10) to handle rapid requests and client requests.

**To GrowthX Business Development:**
- All 32 documented workflows + expected 100+ in coming months represent expanding service capacity without proportional headcount or LLM cost concerns (fee structure absorbs tooling costs).
- Contractor management platform in planning phase to handle specialists (designers, doctors for medical reviews) at scale.
- Phase 2 (this year): opening self-service APIs to external users for image generation, research, SEO analysis — potential expansion revenue stream.

---

## Overview

- growthx.ai's approach: Team-as-product, combining service delivery with rapid AI workflow development
- Current focus: Content marketing automation, with plans to expand to other domains
- Tech stack: Custom AI workflow engine ("Flow") + AirOps as temporary UI, moving towards fully integrated platform
- Goal: Enable non-technical team members to create/modify AI workflows by end of year

---

## Key Topics

### Business Model & Market Positioning

  - Positioned as "service as software" to capture higher perceived value vs traditional SaaS
  - Leveraging AI to bring programmer-level productivity gains to marketing space
  - Services team acts as product manager + R\&D, identifying client needs and funding development

### Current Product Architecture

  - Custom AI workflow engine ("Flow") for rapid workflow creation (4-10 min setup time)
  - AirOps used as temporary UI layer (spreadsheet + API calls)
  - 32 documented workflows, expected to grow to 100+ in coming months
  - Examples: Content research, writing style analysis, image generation brainstorming

### Development Roadmap

  - Phase 1 (Current): AI-powered content marketing, internal use
  - Phase 2 (This year): Self-service APIs for external users (e.g., image gen, research, SEO)
  - Phase 3 (Future): Expand approach to other domains (e.g., sales, recruiting)

### Planned Platform Improvements

  - All-in-one tool to replace Notion, Airtable, AirOps for internal team
  - Contractor management platform for small, specific tasks (e.g., doctor review of article)
  - Data instrumentation to enable custom model training (e.g., client-specific writing styles)

### Technical Challenges

  - Rapidly changing AI landscape requires flexible architecture
  - UI/UX patterns for AI interactions still evolving
  - Balancing automation with human oversight and intervention

---

## Action Items

- **Daniel Lopes (GrowthX)** — Develop all-in-one internal tool prototype (in progress this week)
- **Felipe Lima (GrowthX)** — Assist with internal tool prototype validation starting next week
- **Daniel Lopes (GrowthX)** — Explore modular "building block" approach for workflow customization with Felipe
- **Engineering team (GrowthX)** — Expand team to support rapid development of Flow engine
- **All team members (GrowthX)** — Report bugs, issues, and workflow ideas via Slack #engineering-support channel

---

## Transcript
**Daniel Lopes:** This is cool.

**Daniel Lopes:** We'll have time to have one-on-one's or time to get you out in private.

**Daniel Lopes:** Let's see what else up here.

**Dave Capone:** The leap is here.

**Daniel Lopes:** Americans is here.

**Daniel Lopes:** I guess everyone is here.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Let me just make sure I record this.

**Daniel Lopes:** Oh, it's confused.

**Daniel Lopes:** If Feden is working or not, I think it is.

**Daniel Lopes:** All right.

**Daniel Lopes:** Well, welcome everyone.

**Daniel Lopes:** was very nice to have you all joining.

**Daniel Lopes:** think by now you probably had a few sessions already.

**Daniel Lopes:** You have a session with Marcel.

**Daniel Lopes:** You have a session with Bridget.

**Daniel Lopes:** And my session will be slightly different.

**Daniel Lopes:** bear with me because it's going to be the first time I do this one and I haven't.

**Daniel Lopes:** So it might change the format over time, but and we have a different set up, we have a different kind of product and that's on purpose.

**Daniel Lopes:** So I want to walk you through, it's going to be less of a traditional somebody just showing you where to click around, don't like send me a GUI or some user interface on the product.

**Daniel Lopes:** And we're explaining the where we are today and where we want, where we think we can be in like a few months and where we want to be by the end of the year and why you're taking this approach.

**Daniel Lopes:** So let me share my screen and I'll walk you through everything.

**Daniel Lopes:** And you can all like at any time, just like mute and ask questions or yeah, anything you want to stop, we can make this conversation as much as you want.

**Daniel Lopes:** One sec, my beautiful calendar, there we go.

**Daniel Lopes:** So you should be using my screen.

**Daniel Lopes:** All right.

**Daniel Lopes:** you probably have seen this.

**Daniel Lopes:** slides for Marcel.

**Daniel Lopes:** I'm not sure, like, did he show you all the parts of the teach deck or like explain that from the business perspective?

**Daniel Lopes:** Probably talked about like service, it was a software and probably talked about the potential and the size of the industry and the dam and all the stuff that Marcel likes to talk about.

**Daniel Lopes:** So that's the rationale for why we're doing things this way.

**Daniel Lopes:** So if you open our website, like a lot of people will say, oh, this is just an agency and that's kind of like the hack or like the unpredictable approach that we're taking.

**Daniel Lopes:** there are two angles to this.

**Daniel Lopes:** One is because it's actually what Marcel is always talking about.

**Daniel Lopes:** There's a huge spend on building new teams, training people, getting them to perform certain tasks and that has a completely different perceived value than signing up for a product.

**Daniel Lopes:** that will actually take you more work to do and take you time to learn and to get trained on that.

**Daniel Lopes:** So like the value that you get from a traditional software will probably take you months.

**Daniel Lopes:** If it's a bigger company, it might take like a full six months to roll out at least.

**Daniel Lopes:** If it's a smaller company, it will take probably like a couple of weeks or two a month.

**Daniel Lopes:** And if you somebody never mastered, you never get there.

**Daniel Lopes:** So you see this implementation phase and then the churn phase and traditional product is that most of the products they never really get adopted the way people wanted them to be from both sides.

**Daniel Lopes:** the client wanted to work, the product team wanted to work and you end up doing a product that doesn't do what the client wanted and vice versa.

**Daniel Lopes:** it never really, so you have this rare situation where they do both and then you have the perfect product and you have the perfect combination and that's what we call product market fit.

**Daniel Lopes:** But it's super, super, super hard to find in normal ways.

**Daniel Lopes:** And the space that we are today,

**Daniel Lopes:** in what's happening to L.A.L.M.s and GNAI in general, it became a lot harder.

**Daniel Lopes:** the benefits from before, business level already existed, but if you could create a business where a piece of software would help a part of your team perform a lot faster, that would be a lot of value, but that never materialized.

**Daniel Lopes:** So we ended up having a lot of services oriented businesses.

**Daniel Lopes:** So you have all different agencies or different kind of verticals, but those, they don't scale.

**Daniel Lopes:** So that's the well-known specter in our market that you can never get VC funding, like venture backed capital for agencies or services, because they don't scale.

**Daniel Lopes:** They've never had high turn of people, it's highly stressful for the employees, and you have to constantly

**Daniel Lopes:** to be getting your clients.

**Daniel Lopes:** So it doesn't scale.

**Daniel Lopes:** You're never going to see like the traditional Twitter path or like the task web path or like sales force, like the perfect example or snowflake, like you don't see the same route.

**Daniel Lopes:** So there were never, so like when we talk about how much value you can attach to your business, a service has been business at the most will have like maybe three to five times the value if it's growing.

**Daniel Lopes:** And, but a product company, it's not uncommon to have 10 to 30 to even sometimes 50 times the value of the current revenue.

**Daniel Lopes:** So it's a completely different ball game, but we are in this space now where like that starts to become possible.

**Daniel Lopes:** So it became very clear for programmers.

**Daniel Lopes:** So that's the thing that made me wanted to start this with more sales and became very obvious to programmers in the last couple of years that if you know what you're doing and if you know how to leverage the tools, right?

**Daniel Lopes:** You can be like, uh-huh.

**Daniel Lopes:** 100 times more productive for certain kinds of tasks and that didn't translate to the same way for all those cases and Marcel being an expert in marketing, I think like that was the perfect opportunity to try to be what happened to programmers to the space where Marcel was operating.

**Daniel Lopes:** And so that's where the idea of like tackling this as the service as a software came came from.

**Daniel Lopes:** It was not for like, let's find an opportunity that's like the perfect way to make money in the space was more like, how can we bring the kind of value and the kind of productivity that programmers are getting to the space that Marcel was operating and he had already started trying to do that with like deep gram and like some of the clients that he was bringing in September when I joined.

**Daniel Lopes:** But I was always thinking this from a different angle.

**Daniel Lopes:** So the angle was more like all the tools that we were using like we had we were still using a lot of the same tools under different things changed.

**Daniel Lopes:** But a lot of the tools that we're using

**Daniel Lopes:** When I joined Marsam in September, were things that you were like the traditional no-code, low-code tools, so you have things like air-ox, you have some of the more advanced things of air-table, for example, like if you're doing like API integrations and all that, we are doing some of that back then already, and we're using some other tools like it up here, N8 and then some of the other things that you can hook things together.

**Daniel Lopes:** But the thing is that AI is just moving too fast.

**Daniel Lopes:** So like six months ago, you have just normal models, now you have models that have a thinking phase and an execution phase.

**Daniel Lopes:** How do you implement that in your product?

**Daniel Lopes:** you do it a bunch of interface, you've coded a lot of React code for how the buttons work and how the grids work and all that.

**Daniel Lopes:** It's just moves too fast.

**Daniel Lopes:** And another problem is that the UX and the UI patterns don't exist.

**Daniel Lopes:** Like up to this point, in software history, we've been used to like click around, have buttons, you have a slider.

**Daniel Lopes:** because you have dropped, I don't know if have all the things.

**Daniel Lopes:** And now we have this chat UI.

**Daniel Lopes:** And you're talking to a chat interface that behaves completely different based on how much knowledge you have.

**Daniel Lopes:** And we see that all the time with our tools already.

**Daniel Lopes:** So like whenever I give people access to pumpkin, you can have somebody that will have an amazing result.

**Daniel Lopes:** And somebody that will have the worst result possible.

**Daniel Lopes:** They should probably have just another thing by hand instead of using the prompt.

**Daniel Lopes:** So that kind of interface is completely, you can't give that to normal people without a ton of training.

**Daniel Lopes:** So the UI and the UX pattern doesn't exist yet.

**Daniel Lopes:** That's the perfect solution.

**Daniel Lopes:** the chat interface will probably only work when we actually really reach the final role of the foundational models.

**Daniel Lopes:** Like you really reach like AGI and whatever you give it to you, won't be able to execute.

**Daniel Lopes:** We're far far away from that.

**Daniel Lopes:** another thing.

**Daniel Lopes:** I think that's happening now, it's opened up a lot of automation.

**Daniel Lopes:** It wasn't possible before.

**Daniel Lopes:** For example, this week, we're getting a ton of requests for people asking for different types of images.

**Daniel Lopes:** Some people want more realistic images.

**Daniel Lopes:** people want to cover images for the art.

**Daniel Lopes:** Some people actually want images to alter the art.

**Daniel Lopes:** Some people want diagrams.

**Daniel Lopes:** all of these things, the reason why our key is asking that, is because that's where the bottleneck process is.

**Daniel Lopes:** So now that we have the motions to create a text-based material, high-speed, high quality for many clients, and they are getting stuck at the design and final production phase, how do we handle that?

**Daniel Lopes:** then we have like five different tools that we can try to use.

**Daniel Lopes:** And they all behave slightly different.

**Daniel Lopes:** They all have the same problems where like prompting is a challenge.

**Daniel Lopes:** How do you approach all the things in a different way?

**Daniel Lopes:** So you have to be like learning all the tools of a crazy fast phase, which for a programmer isn't too hard, but for

**Daniel Lopes:** where a marketer is pretty much impossible.

**Daniel Lopes:** So how do we staff the team, how do we build this product that solve all these challenges?

**Daniel Lopes:** Like how do we build a product that the UI is constantly changing, the tech underhood is constantly changing.

**Daniel Lopes:** Opportunities for integration is just like changing overnight and requires a super technical user operating it.

**Daniel Lopes:** That is a challenge that I think like everybody's approaching in the way that we want to approach this essentially.

**Daniel Lopes:** So you have tools like AirOps, for example, or you have tools like Docker, you have tools like Retool, or NaVin, they're all approaching like GUI-based.

**Daniel Lopes:** What we decided to do is the opposite.

**Daniel Lopes:** So like for now, our team is the product.

**Daniel Lopes:** is not a temporary thing.

**Daniel Lopes:** So if you look at the team composition might change over time and we build the tools and we make things more robust, but the goal is always to have the team as the product.

**Daniel Lopes:** So you

**Daniel Lopes:** We might have heard, I don't know if we had a call with Kyle already, or some of the people that could explain our service team, our staff, but we essentially have pods and the pods have strategists and have, now we're currently managing directors and they have also account managers, they have pod leads.

**Daniel Lopes:** So have a whole group of people helping the client and that is by design and that team we'll interface with the product and the technical team.

**Daniel Lopes:** So the services team, we're always going to be there.

**Daniel Lopes:** never going to be replaced by a size that we're building under the hood that will automate everything and we're going to fly everybody that's never been the planet that will never happen.

**Daniel Lopes:** So the goal is to always have a services team that will interface with our client, will operate things on behalf of our client, will essentially be like an extension of our clients.

**Daniel Lopes:** And we, on the deck,

**Daniel Lopes:** goes high.

**Daniel Lopes:** Our job is to figure out the way to support the next fast as we can.

**Daniel Lopes:** We hit the wall with the existing tools.

**Daniel Lopes:** We couldn't automate things fast enough using air ops for it.

**Daniel Lopes:** With all this, I spent like a year just learning all the different prompting techniques, all the different models.

**Daniel Lopes:** When they use cloud, when they use open AI models for different kind of models, that .

**Daniel Lopes:** That was taking me a week to do the somewhat simple workflow.

**Daniel Lopes:** But that didn't work ideally we should be creating the workflows to each client, each pod, the things that are specific today and the things that are general as well.

**Daniel Lopes:** might be a word where we're going to be creating workflows like thin workflows a day or more.

**Daniel Lopes:** So how do you do that in an environment like the docket?

**Daniel Lopes:** Just clicking around on the using the options to select exactly what it takes you a day, know, and testing and then it fails and you have to

**Daniel Lopes:** to go back and just so, so much work.

**Daniel Lopes:** So what we decided to do is to instead have our own services team is essentially our product manager in how NR&D combined.

**Daniel Lopes:** They're bringing in the revenue that helps support all the cost for running things without worrying about cost of LLN costs, for example.

**Daniel Lopes:** Maybe an article will cost 10 bucks.

**Daniel Lopes:** Who cares?

**Daniel Lopes:** So like we are charging for the same amount as a person or multiple people doing the work.

**Daniel Lopes:** So we don't have to worry about trying to squeeze as much money as possible that traditional agency would do.

**Daniel Lopes:** Like services team is not trying to be as profitable as possible.

**Daniel Lopes:** They're trying to bring us the problems that the clients are dealing with.

**Daniel Lopes:** And we'll have to figure out how to make that work with tech.

**Daniel Lopes:** So they're both telling us what we have to do.

**Daniel Lopes:** Like for now, they're telling us that we have to figure out images.

**Daniel Lopes:** This is the theme of the week.

**Daniel Lopes:** So

**Daniel Lopes:** They're constantly bringing new demands, and they're also like telling us, bringing enough money that we can fund the cost for figuring things out, and doing those two things combined.

**Daniel Lopes:** That's why I'm calling it the product manager and the R&D, and the number one goal for us is to figure out on the technical side, how do we support them as fast as That's number one thing, and number two is figure out how do we reduce the amount of mistakes that they can make, so they're not stumbling around and struggling.

**Daniel Lopes:** That's a part where we still have a lot of room to improve, so that's what we're working on actively now, and today I'm trying to figure out some prototypes, and we're framing for Felipe to help out next week, and some of the other folks that are joining, and in practice, how does that look like?

**Daniel Lopes:** So if you have a session with Kai or some of the people, are more on the server system, and there you're getting on boarded on how to do the work, we have essentially...

**Daniel Lopes:** two phases.

**Daniel Lopes:** We have a strategy phase and you have a production phase.

**Daniel Lopes:** And the strategy phase will be a lot of things that are you knowing the domain, knowing the space, you're going to use different tools.

**Daniel Lopes:** But we are essentially writing a bunch of documents and presenting the documents to the clients, getting hired with them, what priorities for them and what they want to act as to icons.

**Daniel Lopes:** And then we put those things in different places and we execute some of the work.

**Daniel Lopes:** And the production space is not that different, but the tools that we use are slightly different.

**Daniel Lopes:** So there would be like more like you choose something in the air table, you pass that thing through like maybe a bunch of things in AirOps, will generate a bunch of LLM basins, you check, you customize, you make it better, you put in the Google Docs, you share with the person with the client that will be in charge of like one if you're in the content, and then you publish somewhere.

**Daniel Lopes:** So you have all the tools in the different phases.

**Daniel Lopes:** In reality, that's

**Daniel Lopes:** So we have, you don't have to read all the diagrams, everything, the goal is to like listen to what our team wants to be.

**Daniel Lopes:** They will have like many times they'll have different workers, but the goal is to like understand what are the priorities, how do how they do the work and try to translate that two ways that can be automated, so they can focus in the step in between.

**Daniel Lopes:** Let's say a part of the writing an article, a big part of it is like researching the material, then we should come up with a researcher that will reduce the amount of time that will take, but also like making you be able to do that 100 times.

**Daniel Lopes:** Instead of researching an outline, doing a couple of Google calls and like running manually Google search queries, can we do 100 Google search queries and combine that and have the better results.

**Daniel Lopes:** Where are the opportunities to just automate time but at the increased efficiency and the increased capacity that would be possible before.

**Daniel Lopes:** So that's the the diagrams the workflows.

**Daniel Lopes:** for our phases for generating an article.

**Daniel Lopes:** So it starts with a researcher and then we run a bunch of things around generating an outline and then we generate a potential title, a draft, then we adapt to this type of the client and then we run out of things for SEO.

**Daniel Lopes:** And then it keeps going from there to many other workflows.

**Daniel Lopes:** But under the hood, what's going on here, we have two things.

**Daniel Lopes:** if you were to create a workflow, I want to show you something real quick.

**Daniel Lopes:** So let's say, for example, today somebody in our Slack will say, hey, we need to do this.

**Daniel Lopes:** We got a request today for integrating this tool called Matkin.ai.

**Daniel Lopes:** I haven't had the time to do that yet, but it's essentially a tool that you give it a text and it will generate diagrams.

**Daniel Lopes:** It's perfect for many of our more technical clients.

**Daniel Lopes:** We don't support that yet, but we do support some other types of image generation.

**Daniel Lopes:** But let's say I had to work on this.

**Daniel Lopes:** The way we work today, we have this framework, this environment where we can write in plain text, the challenge we have, the workflow we want to do, and how we do it.

**Daniel Lopes:** So in this case, for example, let's say I wanted to have a client that they have a particular way of writing.

**Daniel Lopes:** So they write in this certain format.

**Daniel Lopes:** Like maybe they always open with a joke, or they always have like a, they use certain slang, or they have different formatting, have all this particular way of writing.

**Daniel Lopes:** How could I do that?

**Daniel Lopes:** would ideally would like read like maybe 10 articles of how they write, and then I will notice the particular things in the writing style.

**Daniel Lopes:** I would like annotate them, and maybe I extract examples.

**Daniel Lopes:** So what this file here is going be this.

**Daniel Lopes:** So like I have a display text file where I describe the work.

**Daniel Lopes:** So in this case, it's saying I want to read, like it's a little bit more technical because it is meant for people like me and Sadie Pichich, right?

**Daniel Lopes:** But it seems like

**Daniel Lopes:** So we can say I want you to use this particular API to read the articles for us combined in a certain way, extract the quotes, and at the end generate a name of the archetype, like maybe it's a funny name, maybe it's like they are like a scientific writer, maybe they're like a authoritative writer, so like come up with a name, come up with a description of the archetype and come up with a giant list of quotes.

**Daniel Lopes:** What's this used for?

**Daniel Lopes:** But when we're going to, at the end of the process, we can give this series of examples to the LLM and ask you to try to adapt to how the author writes.

**Daniel Lopes:** So that's a step to optimize the things.

**Daniel Lopes:** And in practice, let me run this.

**Daniel Lopes:** So it takes four minutes, this is the only input we had, and it takes four minutes to generate the whole workflow and have an API that behaves like this.

**Daniel Lopes:** You know, it's a little bit fuzzy, let me open the screen, and I can explain as we go.

**Daniel Lopes:** because it's a little bit more technical, but I can best forward and I'm just typing some stuff there and like changing the text, but choosing some of the ball goes and coming up with more ideas at the spot on the spot, and then we run a command on the on our terminal, it would generate five files.

**Daniel Lopes:** These five files are essentially the API that now we can use anywhere.

**Daniel Lopes:** So we can use like, it will work pretty much almost always from the start, you basically have to not even change that code that much.

**Daniel Lopes:** Sometimes you might have to change the prompts, sometimes you might add to tweak a little bit, but that's like the first pass.

**Daniel Lopes:** And then you can iterate on this after if they come up with a new request later, or if you want to change, then then you will probably have to code normally and use some of the traditional tooling.

**Daniel Lopes:** But from the start, we have a collection

**Daniel Lopes:** side and then they can define the company name, the instructions about the company, and then you have a bunch of workflows.

**Daniel Lopes:** All the little blue columns are columns connected to workflow like they wanted that I just showed you and when you have hit the play button here, let's find one of these.

**Daniel Lopes:** So when you hit the play button, get one that has an image that's that some of their interesting ones you look at.

**Daniel Lopes:** So hit any of these play buttons on each one of the cells, it will make an API quality like the one that I just showed here and it will generate something and it will put the result back into the spreadsheet.

**Daniel Lopes:** So that's the user interface we use today.

**Daniel Lopes:** We use our office just as a user interface, essentially a spreadsheet with API calls.

**Daniel Lopes:** And in this case, for example, the client has a specific way of generating cover images and they want to have photos that are more realistic and always have this like purple, blueish.

**Daniel Lopes:** stone and but have all like kind of futuristic vibe and that's like you're not going to find that in the stock image.

**Daniel Lopes:** So I don't know what happens here.

**Daniel Lopes:** The work tool that actually is generating this.

**Daniel Lopes:** Like you might be thinking, why don't you just use me journey?

**Daniel Lopes:** Because me journey doesn't work.

**Daniel Lopes:** don't know how to use me journey.

**Daniel Lopes:** So that's the problem.

**Daniel Lopes:** If you're saying like a weak learning major, then you might be able to do something good, but it's still like, how do you come up with the better ideas based on work?

**Daniel Lopes:** Can you do that 10 times, like a hundred times if you have to put a hundred hours in one week?

**Daniel Lopes:** No.

**Daniel Lopes:** And the solution here was to automate actually how you would do the process of doing like a great image journey by, let me see, this one, how this version is kind of older.

**Daniel Lopes:** Let me get another one for today.

**Daniel Lopes:** Okay.

**Daniel Lopes:** So this is for on page N.

**Daniel Lopes:** we have this environment where you can see everything that's getting executed.

**Daniel Lopes:** I'm going to open this one.

**Daniel Lopes:** So you get an input, so the input is the title of the article.

**Daniel Lopes:** This one is not the best one.

**Daniel Lopes:** Let's get another one.

**Daniel Lopes:** The result is cool, but the steps are not as interesting.

**Daniel Lopes:** But they receive a title, and we generate an image in different formats for them.

**Daniel Lopes:** But let's say we have to brainstorm the image and come up with what to actually build.

**Daniel Lopes:** In this case, we have a workflow that does this.

**Daniel Lopes:** We received the whole article.

**Daniel Lopes:** We read the content of the article, come up with a bunch of ideas.

**Daniel Lopes:** What could be things that will help you illustrate this article?

**Daniel Lopes:** Then we have another LLM call.

**Daniel Lopes:** So that's the first step is just read the article, up with ideas.

**Daniel Lopes:** So you come up with maybe 20 ideas.

**Daniel Lopes:** Each one is like a different prompt.

**Daniel Lopes:** And then we have another LLM that will act as a judge.

**Daniel Lopes:** and select what is the best idea based on what this client does, and like some other judging criteria we have, and then we process all the images in parallel.

**Daniel Lopes:** So you generate things out of one image you generate, like five, and then you can store all these images in our own storage in Amazon, and then we put that in our ops and let our ad virtues.

**Daniel Lopes:** So for instead of them having to figure out what's the right prompts to call, we automate the whole thing, and we generate 10 images, and they select one of the 10.

**Daniel Lopes:** So that's kind of the example thing we can do.

**Daniel Lopes:** And like I showed you, it takes like, if you're using our framework properly, you can do that 95 minutes or 10 minutes.

**Daniel Lopes:** So that's the gist of how we are leveraging AI for automating a lot of the workflows.

**Daniel Lopes:** So for now we have this framework that we call Flow, where it's written for programmers.

**Daniel Lopes:** We are not this stage where you can let somebody.

**Daniel Lopes:** like Marcel create his own workflows or some of our managing director create their own workflows yet.

**Daniel Lopes:** hope it's to get there and we have a plan to get there.

**Daniel Lopes:** But that's what I'm saying that the expectation is that we get there by the end of the year and we're essentially, this is essentially how the workflow looks like.

**Daniel Lopes:** We have a giant file of prompts as you can see here on the right.

**Daniel Lopes:** The prompts are versions.

**Daniel Lopes:** So we use all the normal programming practices where you use GitHub, GitHub, use pull request and we take prompting seriously because prompting is actually a programming language.

**Daniel Lopes:** So we're approaching prompting as a programming language and the steps of executing the prompt is another thing that we approach slightly different than everyone else.

**Daniel Lopes:** But the main goal here is this year, we're calling our phase one, we have start with AI part content marketing.

**Daniel Lopes:** That's our expertise.

**Daniel Lopes:** That's how we're staff in our service to seem to be like all super great content creators and we

**Daniel Lopes:** Find all the boring stuff that they're bottlenecks in their workflows and would figure out which to automate that.

**Daniel Lopes:** And from there, maybe next year, we increase efficiency and we start adding, not even next year, even earlier than that, we start letting some of the folks outside of our services team to do self services, like start getting access to some of the APIs that I just showed you, like maybe you want to do our image generation like what some of our folks do.

**Daniel Lopes:** So then we have an API for that.

**Daniel Lopes:** We can have an API for researching things or have an API for SEO analysis, improvement and all that.

**Daniel Lopes:** So that we hope to have that this year.

**Daniel Lopes:** And then maybe the phase is to start like, can we do the same approach in different different domains?

**Daniel Lopes:** Maybe we can do that, for example, for say, we can do that for recruiting or in certain areas and we can start like seeing if we can use the same approach in other areas.

**Daniel Lopes:** In practice, what we're doing today is we have this.

**Daniel Lopes:** AI workflow engine is functional, and we're using that for all of our clients.

**Daniel Lopes:** That's what I was showing you.

**Daniel Lopes:** If you have access to this, the access thing one password, your feature log in and it's going to ask for admin password, and that password is in one password.

**Daniel Lopes:** can open and click around, and then you can see all the things getting created there, all the things are getting executed.

**Daniel Lopes:** You can click in an input, see what we receive, you can see the output of the whole workflow, and you can see each step, and you can also see the description of the whole workflow here as well.

**Daniel Lopes:** You will also have on the left side here, there's a library of all the workflows we support that are documented and published.

**Daniel Lopes:** We have a list of 32 workflows.

**Daniel Lopes:** probably grow to more than 100 in a couple of months.

**Daniel Lopes:** But that's the AI workflow engine.

**Daniel Lopes:** We have the framework, have the runtime, and we hope to view the better developer experience where somebody like Marcel or somebody like...

**Daniel Lopes:** a more junior programmer could build these workflows for us faster and can iterate faster there.

**Daniel Lopes:** So we're staffing the team to help build this and to continue to build this, we're working on this today.

**Daniel Lopes:** So this is the specific tool for markers.

**Daniel Lopes:** the idea here is to replace notion, air table and the air ops, but in a way that's 100% focused on how we do things and how folks like our managing directors, like our strategists and our managers doing things.

**Daniel Lopes:** So instead of them having to like freaking click around in the air ops and air ops constantly changing their UI and breaking things, some of them have basically learned all these like different six tools, would be like all in one place.

**Daniel Lopes:** And that's what I'm working on this week, trying to come up with a prototype for the first few steps there.

**Daniel Lopes:** We also have the challenge that dealing with like a lot of contractors is super hard.

**Daniel Lopes:** So like dealing with designers, dealing with like coffee riders that you need for specific small things takes too much time.

**Daniel Lopes:** So

**Daniel Lopes:** We have the plan to start also building an API in a platform where you can request small needs.

**Daniel Lopes:** So if you need a doctor to review an article, can we find doctors and they just receive that specific request?

**Daniel Lopes:** That's something we are also thinking about and we are planning on how to tackle that.

**Daniel Lopes:** Another layer that we have is, can we instrument everything?

**Daniel Lopes:** we learn about every change that so we can start like, let's say you receive a draft and the writer will be like, oh my god, this draft sucks and then they start changing the whole thing.

**Daniel Lopes:** That's a learning opportunity.

**Daniel Lopes:** Can we instrument that can collect that data and can we start creating versions of the foundational models that are out there?

**Daniel Lopes:** Can we create a version of Claude?

**Daniel Lopes:** Is it specific to that way that that client writes or the way that we write as a whole company?

**Daniel Lopes:** Can we create the smaller model for creating outlines, for example, or assignment brief, like the way people research the whole thing.

**Daniel Lopes:** That's a big part of our all-week do too.

**Daniel Lopes:** So there's all these opportunities for creating specific models for what we do, but for the order to do that, we need to change to prevent the whole thing and have access to everything.

**Daniel Lopes:** So if to do that, we can't be using AirOps and Notion and Slack and things like that.

**Daniel Lopes:** So over time, that's the path for the platform.

**Daniel Lopes:** Right now, it's just like, let's get this in working, no matter what, do whatever it takes to support the services team.

**Daniel Lopes:** We'll look at a little hacky, we'll be a little bit different, you don't have a lot of UI, it's pretty cool to click around.

**Daniel Lopes:** But we will have programmers helping every step of the way.

**Daniel Lopes:** So if you're having a situation where you're like, should I bother with Daniel, should I message this in support?

**Daniel Lopes:** You should definitely shoot like it.

**Daniel Lopes:** So when the services team, that's number one priority, like complain as much as you can, and we're here to support.

**Daniel Lopes:** Sorry I went a little over, any questions?

**Daniel Lopes:** I talked a lot, so that was like a full model.

**Daniel Lopes:** I'm probably different than Mercile and everyone else.

**Dave Capone:** questions is there that's making the little more clear or yeah this is super helpful I guess more of an observation maybe a question but it seems like the overall goal is to create a front end that is static that has your workflow of place but the technology behind the workflow can change based off of the needs of the client or needs of the the managing director or editor so yeah potentially like having to say on the technical side maybe client isn't the right AI to use for that particular client maybe it's you know grocker you know chat DPT that stuff would be invisible to us and it would just you know automatically swap out the different services or components based off of at the moment that's a great question that's something that Felipe and I were discussing yesterday like how should we approach this should be approached is more of a

**Daniel Lopes:** like blocks and that's kind of a year approach or should we figure out how to build in like more like domino or like building blocks that you could choose and you have control and like the voice you always have is the bill again.

**Daniel Lopes:** See which ones are data used which from tools used and be able to intervene into it.

**Daniel Lopes:** But we also do that in a way that you can like swap things like and why.

**Daniel Lopes:** So it would definitely coming here up and like we have to have this crazy graphs with like crazy arrows everywhere super hard to maintain.

**Daniel Lopes:** So that's the challenge we're trying to figure out.

**Daniel Lopes:** I think we have a good idea of how to do that and but we are in like prototype phase that this weekend X will be there some validating if that works.

**Daniel Lopes:** But I'm optimistic.

**Daniel Lopes:** I think we're going to have both the best of both words that the components will be there and you can move in around just a different client.

**Daniel Lopes:** All right everyone if you have any questions let me know.

**Daniel Lopes:** I'm always available on Slack and we also have an engineering

**Daniel Lopes:** Support channel you can always follow and never questions you have and that we have people like me Marcus Always there to to answer any questions, and if you have find bugs you find the issues or if you have ideas for Workflows you automate doesn't have to be marketing related.

**Daniel Lopes:** That's have to be content related It can be like about meetings can be about recruiting anything you need can be about Compliance anything but anything that you mean let us know and we can Figure it out All right, thank you everyone welcome and I hope you have a good rest of the week Thank you
