# Sulaman Ahmed -Services Hiring Manager Interview | Publishing Operations Specialist

<metadata>
date: 2025-07-07
time: 21:56 UTC
duration: 29 minutes
organizer: matthew@growthx.ai
participants: Matthew Panzarino, Sulaman Ahmed Randhawa
fathom_recording_id: 72551774
fathom_url: https://fathom.video/calls/344315498
share_url: https://fathom.video/share/fyJVxmouxbsnBMGPhrx_xoXCTg9z7Qrw
source: fathom
enriched_on: 2026-03-03 01:30 UTC
</metadata>

---

## Summary

Matthew Panzarino interviewed Sulaman Ahmed for the Publishing Operations Specialist role, walking through GrowthX's mission of solving the "messy middle" of content publishing workflows using Temporal, Rails, Atlas, and Flow Studio. Matthew emphasized the need for high-agency engineers who can think from first principles, tackle diverse publishing endpoints (WordPress, headless CMSs, Git repos), and create automated solutions that let content creators publish at scale — dozens to hundreds of pieces weekly — with minimal technical intervention. Sulaman demonstrated strong understanding of the role, proposing a pragmatic approach to prioritize the most-used CMS platforms first and use creative workarounds for legacy systems, and the conversation confirmed reporting to Andy Bailey in Client Operations with access to all necessary AI tools and Cloud Pro instances.

---

## Context

Sulaman Ahmed Randhawa is a candidate for GrowthX's Publishing Operations Specialist role, a position that sits at the intersection of client services and internal engineering. Matthew Panzarino, conducting the interview, leads part of GrowthX's engineering efforts and directly works on the Services as Software strategy. This interview took place mid-hiring process, after Sulaman had completed an assignment brief that Matthew reviewed positively. The role exists because GrowthX produces dozens to hundreds of content pieces weekly across multiple client accounts, each with different CMSs and publishing requirements. Without automation, manually publishing this volume is unsustainable, so the Publishing Operations Specialist must design and build systems that abstract away technical complexity for content creators while handling the variety of real-world publishing endpoints they encounter. Sulaman's prior experience with APIs (like Upwork's), open-source systems, security workarounds, and creative problem-solving made him a fit for exploration.

---

## Relevance

**To GrowthX Delivery:**
- Publishing automation is a critical bottleneck for scaling content delivery — the Services team currently produces dozens to hundreds of pieces weekly and needs programmatic publishing to avoid manual work.
- Diverse client CMS landscape (WordPress, Sanity, headless CMSs, Git repos, legacy systems with unusual requirements) demands flexible engineering that prioritizes high-ROI platforms first while building reusable microservice architectures for cross-project leverage.
- High-agency culture expects candidates to own the entire cycle — writing the PRD, approving design, shipping the solution — without waiting for permission or detailed specifications.

**To GrowthX Business Development:**
- Client account retention depends on publishing speed and reliability — automating manual publishing steps removes friction and reduces context-switching overhead for team members managing multiple accounts.
- Reference-ability: successful publishing automation for one client becomes a productized offering, strengthening land-and-expand motion within existing accounts and improving pitch for new prospects with similar publishing pain.

**To CheckThat:**
- Publishing systems are a lever for AEO distribution — programmatic generation and publishing (like the Vappy API example) scales content across vertical variants, directly supporting AI visibility strategies and providing live demo generation at scale.

---

## Overview

- GrowthX uses Temporal, Rails, Atlas, and Flow Studio for content creation/publishing automation
- Seeking high-agency candidate to solve diverse publishing challenges across client CMSs
- Role involves creating scalable, automated solutions for content publishing and workflow optimization
- Position reports to Andy Bailey in Client Operations, with access to necessary AI tools and resources

---

## Key Topics

### GrowthX Tech Stack and Workflow

  - Backend: Temporal + Rails
  - Frontend: Custom-built Atlas for publishing workflows
  - Flow Studio: Backend for creating automations by linking workflows into pipelines
  - Focus on organizing "messy middle" of work processes
  - Applications beyond content creation (e.g., sales funnel enrichment, production pipelines)

### Client Work and Scalability Challenges

  - Context switching between clients is a major challenge
  - Producing dozens to hundreds of content pieces weekly
  - Need for automated, programmatic publishing solutions
  - Example: Vappy API project - programmatically generated voice agent demos for various industries

### Publishing Operations Specialist Role

  - Tackle diverse publishing endpoints (headless CMSs, WordPress, Git repos)
  - Create automated systems for content creators to publish without technical intervention
  - Solve unique client problems (e.g., legacy systems, unusual publishing workflows)
  - Emphasis on first-principles thinking and creating leverage

### Company Culture and Work Approach

  - Tool-agnostic, focused on problem-solving and scalability
  - High agency expected: "writing the PRD, approving the PRD, shipping the PRD"
  - Services as Software model: client work funds internal software development

### Technical Resources and Reporting Structure

  - Position reports to Andy Bailey in Client Operations
  - Flat company structure with direct access to leadership
  - Access provided to AI tools, Cloud Pro instances, and necessary architecture/tooling

---

## Action Items

**Sulaman Ahmed Randhawa (candidate)**
- Send follow-up thank you email to Matthew Panzarino for interview

**Matthew Panzarino (GrowthX)**
- Follow up with Sulaman to schedule interview with Andy Bailey in Client Operations

---

## Transcript
**Matthew Panzarino:** Hey, how's it going?

**Sulaman Ahmed Randhawa:** Hey, greetings, Matthew.

**Sulaman Ahmed Randhawa:** Can you hear me?

**Matthew Panzarino:** I can hear you, yes.

**Sulaman Ahmed Randhawa:** All right, that's good.

**Sulaman Ahmed Randhawa:** How are you?

**Matthew Panzarino:** I'm doing pretty well.

**Sulaman Ahmed Randhawa:** That's good.

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** Crazy day, you know, jumping from client to client, topic to topic, but overall.

**Sulaman Ahmed Randhawa:** Yeah, definitely.

**Sulaman Ahmed Randhawa:** I understand that — when you initially explained everything.

**Sulaman Ahmed Randhawa:** I know being on a management position, it's always a lot on your plate.


**Matthew Panzarino:** You know, with client work, it's context switching that's been killer, right? So the focused work is one thing — getting in, I relish my chunks of deep flow, deep work time, because there are only a handful of those.

**Matthew Panzarino:** The rest of it is spent hopping from one context to another and being like, wait, what am I talking about?

**Matthew Panzarino:** Okay, yes, all right, let's talk about that.

**Sulaman Ahmed Randhawa:** So it's obviously different for each of every client.

**Sulaman Ahmed Randhawa:** understand that, like, since I've been involved in that team a few times, it's quite a tough task.

**Matthew Panzarino:** Yeah, you know, everybody's got their needs and desires and wants, and you just have to remember which one you're talking to so that you don't deliver on the wrong messaging.

**Matthew Panzarino:** Yeah, so hi, pleased to meet you.

**Matthew Panzarino:** I did have a chance to review your assignment, so I did, I was able to see you a little bit before we met, watched a recording, and went over your assignment brief.

**Matthew Panzarino:** I thought it was all handled very well.

**Matthew Panzarino:** I was, you know, impressed by the way that you tackled the problem.

**Matthew Panzarino:** You seem to kind of have, I think, the right take on it.

**Matthew Panzarino:** For the systems that we use, some of the more developer-centric folks here would be able to dive in a little bit deeper to kind of give you a little bit more of view of what we use.

**Matthew Panzarino:** We are using Temporal to serve the back end for the most part, along with, or to serve our rails.

**Matthew Panzarino:** And then we built our own front end, of course, Atlas for publishing workflows.

**Matthew Panzarino:** That stack works like, you know, Atlas as a front end allows me to manipulate pipelines a little bit using just YAML, you know, standard scripting.

**Matthew Panzarino:** It's too crazy.

**Matthew Panzarino:** And then on the back end it interacts with the pipelines created and served via Temporal and Flow Studio, which is our backend. Flow Studio allows us to create automations by linking various workflows together into pipelines — anything from content generation to research, fact-checking, publishing, image generation, and more.


**Matthew Panzarino:** So the nut of it is that we need somebody for the publishing position.

**Matthew Panzarino:** And I know you've done some work with Jason in the past, so you know kind of the way we work.

**Matthew Panzarino:** We work fast.

**Matthew Panzarino:** We work nimbly.

**Matthew Panzarino:** We're building an architecture here that goes beyond just content creation.

**Matthew Panzarino:** It should, and it will, and hopefully should apply to a bunch of different modes of work and different applications.

**Matthew Panzarino:** So it could be like sales funnel enrichment.

**Matthew Panzarino:** It could be, you know, production pipelines.

**Matthew Panzarino:** There are a lot of different applications for what we're building.

**Matthew Panzarino:** It's basically taking and organizing the messy middle of work and building automation in between to handle a lot of the steps that we would normally kind of fall into the cracks or fall into the institutional knowledge of a single person.

**Matthew Panzarino:** And then when that person leaves, or maybe they change job positions, now they have to transmit a lot of that learning to someone else.

**Matthew Panzarino:** And so there's just not a lot of work done to organize the work that is being done and the processes by which we do it.

**Matthew Panzarino:** And that's what we're essentially building at a granular level.

**Matthew Panzarino:** Right now, the biggest application is content creation, content strategy, and growth strategy — building things like link magnets, dashboards, and directories. For example, with one client, Vappy, we did a programmatic rollout where we used their API to generate hundreds or thousands of examples of how their API could be leveraged to create a voice agent answering service. Vertical X refers to any one of thousands of verticals — we programmatically generated them so any visitor could see a live demo for their specific ICP.

**Matthew Panzarino:** So it could be an answering service for healthcare professionals, cosmetic salons, or the construction industry — any permutation. Are you just in framing? Cool, we've got an answering service just for you. Are you in concrete? We've got one for you.

**Matthew Panzarino:** And, like, that kind of programmatic work is very difficult for somebody who is, you know, they have their own thing that they're building, and it's difficult for them to sort of change modes, understand, okay, how can we drive growth based on this kind of programmatic work?

**Matthew Panzarino:** And that's what we could do.

**Matthew Panzarino:** Like, that's our specialty.

**Matthew Panzarino:** We're there to help scale all of that.

**Matthew Panzarino:** And of course, many components, many work streams that we have, really kind of the core of it is content.

**Matthew Panzarino:** So all of them must have publishing endpoints of some sort.

**Matthew Panzarino:** And those publishing endpoints can be wide and varied.

**Matthew Panzarino:** So there's a handful of CMSs, you know, that they work with.

**Matthew Panzarino:** Hopefully, I mean, you pray that most of them are headless these days.

**Matthew Panzarino:** But there's probably some examples that are not and will not be, at least when we come into the picture.

**Matthew Panzarino:** And then maybe we can convince them, hey, maybe stop using WordPress and start using Sanity or something like that, you know.

**Matthew Panzarino:** But those publishing, the publishing apparatus is really about taking our deliverables, whatever we're creating, and getting it shipped to them.

**Matthew Panzarino:** So that could be something as simple as, hey, let's just hook up to their API, especially headless CMS, and let's just ship.

**Matthew Panzarino:** Blog posts with all the proper fields, metadata, tagging, et cetera.

**Matthew Panzarino:** But it could be as.

**Matthew Panzarino:** Complex as, hey, we're going to publish to their Git repo, make sure that these things commit so that they go up in their next branch of publishing, and we have to adhere to their requirements.

**Matthew Panzarino:** And then it could be a branch of that that's more like, hey, we're publishing whole webpages for them in a directory or architecture, and we're doing it programmatically one after another.

**Matthew Panzarino:** And then building the systems to link the complexity of that to somebody who is, whose job is to create the content, create the workflow, and then release it to publishing with essentially no real technical intervention from them.

**Matthew Panzarino:** You know, building the ability for them to say, this is good, I release you into the wild, and for the rest of it to happen programmatically.

**Matthew Panzarino:** Because we could, and we are producing dozens of pieces of content every week, and for a variety of clients, and it can be hundreds, sometimes in a burst, even thousands per week.

**Matthew Panzarino:** And so publishing those manually is crazy.

**Matthew Panzarino:** You know, it's out of the question.

**Matthew Panzarino:** And really long-term, definitely a nice hack when you have to, but not sustainable.

**Matthew Panzarino:** And so that's kind of what we're looking for there.

**Matthew Panzarino:** I just wanted to dump you a little bit of context from my POV, and then I'm happy to chop it up and ask you questions, and provide more detail.

**Sulaman Ahmed Randhawa:** Sure thing.

**Sulaman Ahmed Randhawa:** All right.

**Sulaman Ahmed Randhawa:** So thank you so much for explaining this in quite a detail.

**Sulaman Ahmed Randhawa:** I understand that very well.

**Sulaman Ahmed Randhawa:** The problem you mentioned is unique. When we have particular security requirements in place, how quickly can we tackle that?

**Sulaman Ahmed Randhawa:** Or when it comes to WordPress — every company uses its own CMS, and most of the time the client is a non-technical person.

**Sulaman Ahmed Randhawa:** So we can't overwhelm them with technical details.

**Sulaman Ahmed Randhawa:** A good starting point is to list out the CMS platforms our clients are using and find the top ones — it comes down to WordPress, Sanity, and a few others. Since those represent the majority, it would be beneficial to start by automating those platforms.

**Sulaman Ahmed Randhawa:** If WordPress doesn't offer an API, that's not a problem. Since it's open source, we can inject a script into it.

**Sulaman Ahmed Randhawa:** We can have a webhook live on their server. We start with testing on our own space where we know things work, then when we have a WordPress client, we inject the code to open the door for automation.

**Sulaman Ahmed Randhawa:** That's the approach. Worst case, with abnormal security, we do manual interaction.

**Sulaman Ahmed Randhawa:** For example, I created a plugin to export Upwork hours. Upwork API requires approval and takes a month, so instead of waiting, we mimicked human interaction — simulating button clicks and user behavior — to work around the security constraints.

**Sulaman Ahmed Randhawa:** That varies by CMS. If we have 20 clients using Sanity and 2-3 on systems without APIs, we prioritize Sanity first to save time, then manually work on the rest while building reusable code for the most common CMSs.

**Sulaman Ahmed Randhawa:** On the Vappy product — from your discussion, I understand it was a dialing agent that varied the conversation based on the niche they work in?

**Sulaman Ahmed Randhawa:** Did we create the dialing agent, or does Vapi already provide that, and we customized it for different niches? What exactly are our roles in that?

**Matthew Panzarino:** We got API access, then created a programmatic generation pipeline to create dozens or hundreds of these entities. The actual creation and customization of the voice agent is what Vapi does — you give their API parameters and it returns a voice agent. Vapi acts as an interstitial layer between voice models like 11 Labs and whatever UI you're interfacing with for customer service.

**Matthew Panzarino:** We created the template — design work to match their branding, then built programmatic generation of the voice agent to launch a live demo. We generated content to flesh out each page: "You're in this industry, here's why this is awesome for you." We packaged them as pages, committed them to their Git repo, and they published from there.

**Matthew Panzarino:** That's how we did it.

**Sulaman Ahmed Randhawa:** Got it.

**Sulaman Ahmed Randhawa:** So at GrowthX, we don't just deal with content — we come up with ideas that scale up what they're already selling.

**Matthew Panzarino:** Exactly.

**Matthew Panzarino:** We're not an SEO agency even though we do SEO work. We're not a content agency even though a lot of what we do now is content. But long tail, we'll branch in many directions.

**Matthew Panzarino:** The cool thing is, we have really interesting problems to solve every day — that's what's fun for me. I've already run a massive publication, so I don't need to do that again. I was looking for new challenges, new stuff.

**Matthew Panzarino:** The way I can give you this context is because any job you came here to do

**Matthew Panzarino:** is really about understanding the process, breaking it into parts, and automating it. We're mostly tool agnostic — we have some frameworks and standards, but you'd need to discuss the eng team's preferences with them. Overall, we're tool agnostic.

**Matthew Panzarino:** Whatever gets the job done. It's great that you have technical chops, but the most important skill is first-principles thinking — how to create enormous leverage.

**Matthew Panzarino:** By that, I mean every human has finite energy — time and brainpower. But how do we create more leverage so the same person can execute at higher scale and impact?

**Matthew Panzarino:** If we do that across the org, we can live, thrive, and grow. Our leverage is already pretty good, and our tooling is just getting decent. We have high hopes for how much leverage we can create, so we need people with remarkably high agency.

**Matthew Panzarino:** Nothing stands in your way, you figure out how to get the job done. We don't care how you did it — we just want to know so we can scale it and roll it out to everyone.

**Matthew Panzarino:** That's the most important thing — people comfortable writing the PRD, approving the PRD, shipping the PRD.

**Sulaman Ahmed Randhawa:** You have to be comfortable living there, right?

**Matthew Panzarino:** There are incredibly talented people who don't work that way — if you give them a focused task, they execute brilliantly, but they don't create the framework. We need people who think earlier: "I have this weird edge-case CMS, plus we need to publish to their official blog and an internal site. Let me think about that and come back with a solution."

**Sulaman Ahmed Randhawa:** That opens a lot of options. If you tell me the end goal — "get this content published in the most automated way" — then language, cloud, frameworks, everything is open to me. That gives flexibility.

**Sulaman Ahmed Randhawa:** If an approach doesn't work, I try the next one. For example, with Upwork, I started with API — it wasn't working, so I came up with the next approach.

**Sulaman Ahmed Randhawa:** The tricky part was that Upwork images expire after five minutes. So I created a multi-processing approach: as soon as you get an image, GPT processes it immediately instead of waiting until the end.

**Sulaman Ahmed Randhawa:** You have to think out of the box — that's how I work. I always like to be on the safe side, so my style is: understand the end goal, then make sure to avoid anything with privacy, security, or specific client recommendations.

**Sulaman Ahmed Randhawa:** That leaves room for technology selection. I'll use microservice architecture so whatever I develop is easy to incorporate — even if they use PHP and I write Python, I create an endpoint they can access. Full-fledged project, but easily incorporated into theirs.

**Matthew Panzarino:** That's exactly the right way to think about it.

**Matthew Panzarino:** We have people with varying technical aptitude, so creating complex solutions with straightforward endpoints is critical. On the client side too — stakeholders might be the engineering team and CMO, or just a founder saying "I don't know, I have none of that."

**Matthew Panzarino:** "We don't have a blog, I don't even know how to do this." So we're providing ground-up solutions.

**Matthew Panzarino:** You won't be bored building the same WordPress plugin over and over.

**Matthew Panzarino:** There's enormous variety. Fortune 500 companies have a dev team in Poland updating their blog — they email a doc and someone posts it.

**Matthew Panzarino:** There's all sorts of weird permutations. And because we're a client services org that views itself as "services as software" — a relatively new trend — we get to see all of it.

**Matthew Panzarino:** It's doing client work to fund software creation — a feedback loop that makes software more durable and relevant to actual client needs, rather than building in a vacuum and hoping someone uses it.

**Sulaman Ahmed Randhawa:** Exactly.

**Matthew Panzarino:** Yeah.

**Sulaman Ahmed Randhawa:** So that's the opposite of software as a service.

**Matthew Panzarino:** It's a trend from a couple years ago. Instead of offering cheap solutions at massive scale and hoping they work — creating churn and PMF issues — we found PMF for our services and use AI and automation to create leverage.

**Matthew Panzarino:** Once we create enough leverage, we can offer it to the public as self-service. But we're not there yet — we're still doing client work for now.

**Sulaman Ahmed Randhawa:** I have a few questions on the technical side. If we move forward, who would I report to? How do I get access to tools? Would the company provide hosting and API keys?

**Matthew Panzarino:** You'd report to Client Operations, which sits at the intersection of what the eng team is doing and what clients need. That's Andy Bailey — she's excellent, came from client ops at Tango and Uber. She reports to Marcel. It's a flat company, so direct access to leadership. And yes, we provide all tooling.

**Matthew Panzarino:** You'd have immediate access to all API keys, Cloud Pro instances, and any AI tool you need. We have multiple Cloud Pro accounts because they get upset if too many people share one.

**Sulaman Ahmed Randhawa:** That makes sense.

**Matthew Panzarino:** I really liked your example. I showed it to the eng team, and they said it's how they'd handle it, so no major issues. And you've worked a bit with Jason, so you understand how we work. More of a head start than most people get.

**Sulaman Ahmed Randhawa:** Thank you. This was really helpful.

**Matthew Panzarino:** We'll do more interviews and keep talking. Thanks.

**Sulaman Ahmed Randhawa:** Thank you for your time. Bye.
