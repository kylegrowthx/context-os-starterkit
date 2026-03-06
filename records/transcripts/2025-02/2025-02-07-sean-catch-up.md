# Sean - catch up

<metadata>
date: 2025-02-07
time: 19:02 UTC
duration: 28 minutes
organizer: santilli@fwd.digital
participants: Marcel Santilli (fwd.digital), Sean Linehan (Exec)
fathom_recording_id: 46234865
fathom_url: https://fathom.video/calls/227973315
share_url: https://fathom.video/share/JnN9aN2DRevzFohDyxS6P7JsgLx4MPq7
source: fathom
enriched_on: 2026-03-05 12:00 UTC
</metadata>

---

## Summary

Marcel demonstrated fwd.digital's code-based workflow platform—built to solve the scalability and versioning problems that plague tools like AirOps—and proposed a deal partnership with Sean at Exec. Sean showed interest but expressed concerns about production reliability and the technical challenges of integrating fwd.digital's framework with Exec's Python/GraphQL backend and database dependencies. Marcel committed to regrouping with Daniel to explore how fwd.digital could help accelerate Exec's new non-voice scenario creation product, with a follow-up early the next week.

---

## Context

Marcel Santilli (fwd.digital, co-founder) and Sean Linehan (Exec, founder/executive) caught up after both had become new parents. This was a relationship-building check-in that evolved into a product pitch. Marcel founded fwd.digital to address deep frustrations with low-code workflow platforms like AirOps—specifically around scalability, versioning, and the overhead of no-code UIs when building complex, multi-step AI orchestration systems. Sean at Exec has been running massive workloads on AirOps and is now building a new product that requires more complex database interactions and dynamic workflow management than AirOps can handle. The conversation positioned fwd.digital as a potential partner that could help Exec accelerate this work while using a code-first approach that aligns with their existing Python/GraphQL architecture.

---

## Relevance

**To fwd.digital Business Development:**
- Sean at Exec is a high-credibility early customer opportunity—he's running production-scale AI orchestration and deeply understands the pain points fwd.digital solves (versioning, scalability, database integration)
- Partnership potential framed as "deal partnership" suggests revenue-sharing or deep integration; Marcel identified Sean as one of the few people building at Exec's scale
- Key technical concerns blocking the deal: production reliability/pivot risk, Python/GraphQL backend compatibility, database loop-back mechanisms needed
- Strong signal of interest but with real hesitations—follow-up with Daniel needed to address technical integration questions

**To GrowthX Services & Delivery:**
- fwd.digital platform uses Temporal runtime for parallel processing, auto-generated docs, and API-first architecture—relevant if GrowthX clients face AirOps limitations
- Code-based approach versus GUI aligns with GrowthX's preference for version-controlled, scalable systems
- Customer pain signals: AirOps versioning is broken, drag-and-drop UI creates maintenance friction, scaling to thousands of parallel executions breaks the platform

---

## Overview

- Marcel demonstrated fwd.digital's opinionated code-based workflow framework built to solve AirOps' core problems: versioning, scalability, complexity management, and runtime reliability
- Sean showcased Exec's new non-voice scenario creation product and explained why it can't be built on AirOps due to database dependencies and the need for version control
- Marcel proposed a formal deal partnership to help accelerate Exec's development; Sean expressed strong interest but raised concerns about production stability and technical integration
- Action items: Marcel to regroup with Daniel to address technical questions (Python/GraphQL compatibility, database interfacing), and follow up early the next week

---

## Key Topics

### Personal Updates

  - Sean and Marcel exchanged updates about their newborns and early parenting experiences
  - Sean mentioned having a night nurse, which has been "game-changing" for their sleep schedule

### fwd.digital's Workflow Platform

  - Designed to address core AirOps pain points: complexity, scalability, versioning, reusability, and runtime reliability
  - Uses a code-first approach instead of GUI, positioning code structure as the key to power and maintainability
  - Opinionated workflow framework: represents workflows as filesystem structures (similar to Terraform config) that can fit in an LLM context window, enabling cursor or custom agents to generate entire workflows in minutes rather than weeks
  - Features include:
      - Auto-generated documentation from the framework code itself (no manual writing required)
      - API endpoints for all workflow components and activities
      - Temporal as the runtime layer for parallel processing, retries, and failure handling
      - Observation and instrumentation for cost tracking and error visibility
      - Custom models trained on workflow data to improve prompt writing and module orchestration
  - Real-world execution examples: resume review workflows, research workflows that generate structured research briefs with sources and analysis
  - Dramatically faster execution: complex tasks that take 30 minutes in AirOps run in 1 minute on fwd.digital's platform

### Exec's Product Development

  - Current product: voice-based scenario creation where an AI coach interviews users, then one-shots a scenario from the transcript using AirOps (works fine for this simple task)
  - New product in development: non-voice scenario builder that accepts document uploads (PDFs, markdown, tech specs) as context and generates:
      - Multiple scenario directions for users to choose from (based on their input and uploaded docs)
      - Structured evaluation criteria (auto-populated or user-defined)
      - AI character sheet and learner context—both grounded in and deriving questions from the uploaded knowledge base
  - Technical constraint: anything complex and database-backed is outside AirOps' design. New product requires interfacing with Exec's Python backend, GraphQL data-fetching layer, and production databases
  - Versioning problem: can't build in AirOps because new versions must be entirely separate workflows with endpoint changes; history isn't tracked in version control
  - Preference: everything should be checked into code (Git) so versioning and rollback are handled by standard VCS practices

### Collaboration Potential

  - Marcel's pitch: fwd.digital could help accelerate Exec's new product development by providing a battle-tested framework that solves all the AirOps pain points Exec is hitting
  - Marcel framed deal partnership as mutually beneficial: Exec gets a platform that actually works at their scale; fwd.digital gets feedback from one of the few people building sophisticated AI orchestration at production scale
  - Sean's concerns (legitimate technical blockers):
      - Production stability: fwd.digital is newer and less battle-tested than AirOps; a pivot or shutdown would be catastrophic since Exec's customers depend on this
      - Backend compatibility: all of Exec's backend is Python; front-end is TypeScript. Need to understand how fwd.digital integrates with Python services
      - Database integration: many workflows require pulling data from Exec's database. Needs either inline data in the first request or a loop-back mechanism via GraphQL
  - Context from the call: Sean mentioned AirOps is now hiring services teams to directly work with AirOps customers, which could increase vendor lock-in risks—a subtle motivator for exploring alternatives

---

## Action Items

- **Marcel Santilli (fwd.digital)** to regroup with Daniel about the partnership opportunity with Exec and identify solutions for Python/GraphQL integration and database loop-back patterns
- **Marcel Santilli (fwd.digital)** to follow up with Sean early the following week with technical recommendations
- **Sean Linehan (Exec)** to evaluate the technical feasibility of integrating fwd.digital's framework with existing Python backend and database architecture

---

## Transcript

**Sean Linehan:** Hey Marcel, what's going on? Good to see you. Congratulations—most importantly, how's the baby? How's the family?

**Sean Linehan:** Baby here we go, I'm gonna bring her into view. Hello baby girl, there you are. She's got her little feeding tube, but she's doing okay.

**Sean Linehan:** Yeah, we got our combo nursery slash office here. I love that she's getting burped. It's like one long cycle—diaper changing, sleep, not sleeping, feeding. We were having to wake her all the time.

**Marcel Santilli:** I had an app that measured when she was feeding, how many diapers, how many wet diapers, how many bottles, how much of each bottle she drank.

**Sean Linehan:** We used Huckleberry.

**Marcel Santilli:** Yeah.

**Sean Linehan:** We're using Huckleberry too. We're tracking her food now. We took her off the feeding tube for a bit and she was doing well, but then she got COVID, so we put it back in.

**Marcel Santilli:** My wife had a brutal experience at the beginning with triple feeding—trying to get her to nurse, then using a nipple shield, then bottle feeding. And then pumping and cleaning the pump and sanitizing it. It was chaotic.

**Sean Linehan:** Triple work. But honestly, the one exorbitant expense that's been game-changing for us is the night nurse. Someone shows up at 10:30 p.m. and leaves at 7:30 a.m. We don't have to do anything at night.

**Marcel Santilli:** That's amazing. We didn't get one early enough. My co-founder found one he really liked, and she has family that also does night nursing, so if she's sick there's always someone who can come.

**Sean Linehan:** That's awesome. Alright, so let me show you some stuff we're working on. But before that, I really wanted to share some of what we've built and explore if there are ways you could leverage our platform.

**Marcel Santilli:** Can I show you some stuff first? As we built all this, we ran into issues with AirOps—complexity, scalability, versioning. You're probably hitting the same things.

**Sean Linehan:** Exactly. Especially versioning. Their versioning tool doesn't really work—you can only have one version. It's a big problem.

**Marcel Santilli:** It's garbage. The way we position this is: how do we take everything powerful about code and build that into a framework? Code has structure. We're starting with outcomes first, then creating a framework—like Terraform config files—that describes workflows but not in a drag-and-drop way.

**Marcel Santilli:** The framework represents all workflows in a file system that fits within an LLM context window. You plug it into Cursor, and it builds the entire workflow for you. Takes minutes. In AirOps, that's a week of engineer time plus a prompt expert.

**Marcel Santilli:** Everything's auto-documented by the framework. All activities, helpers, prompts, types—the framework generates the docs, not humans. For example, our research workflow: it validates input, generates research questions, does parallel processing, searches for sources, analyzes relevance, returns a structured research brief. All built in minutes.

**Marcel Santilli:** We use Temporal for the runtime layer. You can retry anything and run thousands of things in parallel. Right now we have a researcher workflow running for Galileo—one of our clients. It's generating an outline on AI agents, breaking down key questions, searching for sources, analyzing them. This thing's better than OpenAI's deep research.

**Marcel Santilli:** We're also using Weave for everything, instrumented for cost tracking. We have squirrel running everything in parallel with retries and error visibility. It's the combination of all that.

**Sean Linehan:** And it can be triggered by code. When you want to use deep research, you're going into their UI, which sucks.

**Marcel Santilli:** They'll make it available through API eventually, but not yet. Everything we build has API endpoints—all of it can be used as an API.

**Sean Linehan:** There's a tiny fraction of people who've actually scaled this. They don't know what it looks like when you're running a billion things. A lot of these companies, AirOps included, aren't dog-fooding. They're building a tool to help other people build, but they're not building anything themselves. Are you thinking fwd.digital lines up as a technical orchestration layer, or are you still thinking of it as a services business with this as secret sauce? Yeah, that's a great question man cuz like then you're not having to really like kind of thinking through this and I Think it's kind of like this onion

**Marcel Santilli:** a lot of layers and one of the biggest advantages is your spot on this, exactly the fact that we're building stuff that we're needing to use and that we need to deliver for a client, right?

**Marcel Santilli:** And because of that, when a client goes like, the  is this?

**Marcel Santilli:** we're like, you know, and we can be building fix and figure out.

**Marcel Santilli:** And then what we build is like our ability to fix and improve, like based on that, right?

**Marcel Santilli:** so like, for instance, like you pointed out, like, I was reading the description, we generated for you, right?

**Marcel Santilli:** and I thought it was actually really good up to that one job to be done related to SEO, right?

**Sean Linehan:** Well, there was some stuff earlier in it as well that was like, like it's clearly leaking your prompt is what it was doing.

**Sean Linehan:** And so there was like some stuff and, yeah, I think a failure mode there, if I to give the feedback of what I think, it was, it was good if you assume our public website is good, but I assume our public website is bad.

**Sean Linehan:** It's weird to be referred to as Exact Holdings Inc.—that's not how we stylize our name. Once it got to the job-to-be-done section, it went off the rails. But me and Nick generated a really good one. We recorded a sales call, I asked targeted follow-up questions based on your rubric, and fed that to your system. Much better.

**Marcel Santilli:** Right. The critical failure was garbage in, garbage out. Your website doesn't capture your real narrative anymore. We're iterating by using sales calls as input instead.

**Marcel Santilli:** The cool thing is that with this engine, you can not only change prompts, but train custom models that are really good at writing prompts or finding the right modules and orchestrating. Imagine something like Kaggle for workflows—network effects could be really powerful. Custom GPTs are black boxes; I never use them because you can't understand the logic or fork and iterate.

**Sean Linehan:** Exactly. I started with custom GPTs for scenario work, but it was insufficient. I needed to break tasks into tractable steps and fine-tune each one. Custom GPTs can't do that level of instruction-following or per-step iteration.

**Marcel Santilli:** Here's what I want to throw out: be a deal partner with us. You're the first person I'm offering this. A lot of the things you've hit with AirOps, this framework solves. You're one of the few people actually building at this scale and understanding where we are.

**Sean Linehan:** Let me show you a product we're working on—an extension of our existing role-play product. I'll share my screen.

**Sean Linehan:** Our current product is voice-chat-based scenario creation. An AI coach asks questions about your scenario, records the transcript, and one-shots a scenario. The workflow is on AirOps because it's simple, but other workflows aren't on AirOps because they need database backing. It becomes a Frankenstein where some things are in their system, some in version control. I'd radically prefer everything in version control.

**Marcel Santilli:** Right. Workflows you can write as code, all represented, with API endpoints.

**Sean Linehan:** And they're checked in. With AirOps, if I want to version something, I have to create a whole new workflow and change the endpoint, but the version specifics aren't checked into the PR. I have to check two places; history is lost.

**Sean Linehan:** We're now building the non-voice version. You type in what you want and upload documents—PDFs, markdown, whatever. Gemini parses them. Then you get three potential scenario directions to choose from. Then you define evaluation criteria, which can be auto-populated, imported, or manual. From there, we generate the character and learner context, grounded in the uploaded docs. We generate questions we need to answer from that context, then produce the final scenario.

**Sean Linehan:** The tricky part is people can upload anything—product knowledge, example transcripts. We need to extract and generate a character sheet from it. It's the same pattern you described: what questions do we need to answer, answer them, then generate the character brief that drives the scenario.

**Marcel Santilli:** Everything you're describing, we've already solved. Not at your level of expertise and flow architecture, but we've solved it. Things taking 30 minutes in AirOps take one minute in our system. The versioning aspect is insane. We use Weave for everything, instrumented for cost tracking, and Squirrel for parallel processing with retries and visibility.

**Marcel Santilli:** You're the only person I'd trust to try this and give us feedback on the right abstraction layer for the world. I'm personally fine with that as long as you won't rebuild and sell it. But honestly, AirOps is pissing us off—they're hiring services teams to coach all our clients. You've experienced all these pains and you're ahead. No one's building at your level.

**Sean Linehan:** We don't even intend to build this in AirOps. This new one is too much; we don't trust it. There are too many distinct failure modes to not have this checked into code. I'm definitely interested, but my main fear is we're in production and our customers rely on us. If you pivot or stop supporting something, we'd have to rebuild. The other concern is our backend is all Python—TypeScript front-end, but Python back-end services deployed as APIs. Most of our workloads need database interfacing. Data either has to be sent in the first request, or there needs to be a loop-back through our GraphQL server for data fetching.

**Marcel Santilli:** I'll regroup with Daniel about this. I hadn't talked to him yet, but this could be the perfect way to build together and help you all. Send me a text or email, and we can dive deeper.

**Sean Linehan:** Sounds great, man.

**Marcel Santilli:** I'll hit you up early next week.

**Sean Linehan:** Talk to you soon.
