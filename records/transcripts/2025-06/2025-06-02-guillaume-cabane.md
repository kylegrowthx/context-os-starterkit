# Guillaume Cabane

<metadata>
date: 2025-06-02
time: 14:01 UTC
duration: 29 minutes
organizer: Marcel Santilli
participants: Guillaume Cabane, Marcel Santilli
fathom_recording_id: 65868246
fathom_url: https://fathom.video/calls/314508020
share_url: https://fathom.video/share/yaDXavpw_SZjtK8khM_7sKMtFSdwJUJU
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

Marcel and Guillaume caught up on GrowthX's evolution into a sophisticated AI workflow platform—now at $7M+ ARR with 12 newly hired principal engineers from top tech companies, planning to hit $12M by year-end and raise Series B in 3-5 months. They aligned on a July SF event collaboration, with Marcel offering GrowthX's office space and full logistics support, plus discussed Guillaume becoming a non-paying customer to build custom workflows for HyperGrowth (deal flow evaluator, startup scoring tool).

---

## Context

Guillaume Cabane is the founder of HyperGrowth, a growth advisory and event platform. Marcel Santilli leads GrowthX, a B2B content marketing and AI services company that has recently pivoted to building an internal AI workflow engine serving clients like Ramp, Abnormal Security, Bolt, VAPI, and others. They've known each other for several years and have been out of touch during Marcel's fundraising and platform-building phase. Guillaume is based in France but traveling to SF in early July; Marcel's team is in San Francisco. This call was a reconnection to explore how their companies can work together—starting with a joint event and potentially using GrowthX's workflow infrastructure to solve HyperGrowth's custom data and analysis challenges.

---

## Relevance

**To GrowthX Business Development:**
- Guillaume and Gonto (HyperGrowth co-founder) are high-signal strategic partners with direct access to growth leaders and CMOs
- Two concrete project opportunities: deal flow evaluator (ongoing challenge across venture platforms) and startup scoring/selection tool (HyperGrowth advisory business enabler)
- Potential reference case and co-marketing opportunity through July event
- Deal flow evaluator project addresses a validated market gap—Guillaume struggled to build this with low-code tools (Zapier, N8N) and LLM assistance

**To GrowthX Delivery:**
- Guillaume's experience with tool fragmentation and custom workflow complexity strongly validates GrowthX's positioning—customers need strategy + code-based execution, not templates
- Specific technical challenges Guillaume faced (Zoom webhook integration, Hue OAuth, LinkedIn API scraping, PitchBook data enrichment) are exactly GrowthX's core value prop
- Bolt.muse case study (data science analysis → use case generation → prompt engine for app generation) resonated as example of end-to-end workflow thinking
- Both recognized that rapid AI model changes (Claude 4 release) break months of integration work—GrowthX's code-based, modular approach is antidote

**To GrowthX Overall:**
- Guillaume's observation about decision paralysis in GTM (CMOs can't recommend tech stacks 12+ months out due to pace of change) is critical market insight
- Validates need for adaptable, future-proof solutions over rigid implementations
- HyperGrowth's need to connect 70+ APIs, CRM data, call recordings, and intelligently score opportunities is ideal proof point for GrowthX's infrastructure

---

## Overview

- Marcel's company (growthx.ai) has evolved into a sophisticated AI workflow engine with $7M+ ARR
- Plans for a joint event in SF in July, potentially using growthx.ai's office space
- Agreement to explore growthx.ai becoming a non-paying customer for HyperGrowth, starting with one clear use case
- Discussed challenges in the rapidly evolving AI landscape and its impact on growth strategies

---

## Key Topics

### Company Updates

  - growthx.ai progress:
      - Developed AI workflow engine and runtime layer for scalable, code-based workflows
      - Now at $7M+ ARR, aiming for $12M by year-end
      - Hired 12 principal engineers/designers from top tech companies
      - Focusing on platform investment over rapid growth
      - Considering Series B raise in 3-5 months

### Product Overview

  - Core offering: AI workflow engine with code-based system (activities, prompts, read types, workflows)
  - Key components:
      - Task hub for human interventions
      - Learn engine for data utilization
      - Content OS for assignment management
  - Use cases: From content creation to complex app building (e.g., Bolt.muse project)

### Market Positioning

  - Main competitors: AirOps, Daydream
  - Differentiation: More flexible, strategy-focused, and execution-capable
  - Target clients: Companies needing AI GTM solutions without in-house expertise

### Collaboration Opportunities

  - Joint event in SF (July):
      - Potential use of growthx.ai office space
      - Considering "HyperGrowth and Trends" theme with CMOs/marketers
  - Content creation:
      - Possibility of video content when G visits SF
  - growthx.ai as non-paying customer for HyperGrowth:
      - Potential projects: deal flow evaluator, startup scoring/selection tool

### Industry Challenges

  - Rapid pace of AI advancements causing decision paralysis
  - Difficulty in making long-term tech stack recommendations
  - Need for adaptable, future-proof solutions

---

## Action Items

**Marcel Santilli (GrowthX)**
- Send Guillaume Cabane link to video content example produced by GrowthX videographer

- Schedule kickoff meeting w/ Guillaume Cabane for HyperGrowth projects before July 4th

**Guillaume Cabane (HyperGrowth)**
- Prep 1 clear use case for GrowthX collab (e.g. deal flow evaluator, startup scoring)

---

## Transcript

**Guillaume Cabane:** What is going on, sir?

**Guillaume Cabane:** Hey, it's been a while.

**Marcel Santilli:** It's been way, way, way too long.

**Guillaume Cabane:** Yeah, man, I mean, since you fundraised, you've disappeared into another country, whatever it is, like another dark rock, man.

**Marcel Santilli:** Dude, it's been freaking hard.

**Guillaume Cabane:** So tell me anything, are you even still in the Bay Area or what?

**Marcel Santilli:** Yeah, yeah, we have an office here.

**Marcel Santilli:** We're in SF, but I'm coming to the office probably more often than not just because with the two-year-old at home, there's some home renovation projects going on. It's always loud, and so I just get in by 6:30.

**Marcel Santilli:** How's it? You're in France right now?

**Guillaume Cabane:** Yeah, yeah, I'm still in France.

**Guillaume Cabane:** I'll be there July 7th, though, so I'll see you then.

**Marcel Santilli:** Okay, let's do an event together, like a dinner?

**Guillaume Cabane:** I'll pay for it and help host. Gonto will be there, too. So it's going to be Gonto and myself. We'll both be in town. We've been wanting to organize something. We have a few different event themes in mind.

**Marcel Santilli:** I'm talking to Gonto later today. Check this out—this is our office. We just had a launch party last week, and it's pretty good. It's 50 people. We had a DJ, so we have the whole setup. I have an office manager that can organize the whole thing.

**Guillaume Cabane:** Oh, that's awesome. That could help a lot. We're thinking of doing something like HyperGrowth and Trends with the different CMOs, marketers, and things like that. Whether they're partners or not, but definitely you and other people around that.

**Marcel Santilli:** Would you be open to doing a HyperGrowth and GrowthX hosted thing?

**Guillaume Cabane:** Let me check with Gonto, depends on the goals and what we want to do. What's the theme, what's the vibe?

**Marcel Santilli:** Or we could do something completely separate. Either way, it would be good to do something together because the way we've done events is just invite people, no sales pitch, no presentation. Just come hang out, talk shop kind of thing.

**Guillaume Cabane:** I was thinking of doing something like that. It depends on who and which people. If you can handle logistics, then we could probably increase and widen it a bit.

**Marcel Santilli:** For sure. We don't have a full kitchen, just fridge and stuff. We've been catering, and it was really good. We could do something. If we wanted to do a fancy sit-down dinner, that's a different thing.

**Guillaume Cabane:** How's the company going, man?

**Marcel Santilli:** What's GrowthX up to?

**Guillaume Cabane:** I don't even know what the product is. I haven't received an update from you like since Tomas Tungus asked me last week. I was like, dude, I don't know.

**Marcel Santilli:** Let me give you the high level. As we started scaling and got into our office, everything started to break. It's just impossible to manage workflows and build workflows at scale in local tools. My co-founder and CTO built a lot of the distributed infrastructure at scale with 50 million users. So what we started to build is a coding agent that builds workflows as code and then a runtime layer.

**Marcel Santilli:** Every single workflow has this four-file system: activities, prompts, read types, workflows. Everything is represented in code and auto-documented. Our deep researcher, for example, pings a bunch of different APIs. All of this runs in our infrastructure. Last month we had over 336,000 runs, and now our coding agent is so good that all our recruiting processes and everything runs through workflows. By coding workflows instead of just an app, you need infrastructure that can run all of this. That's the core.

**Marcel Santilli:** Right now we're working on three things we're pretty close to launching. One is the task hub. If you think about executions, you have a human hitting play, and we're using tools like Airtable to manage the work. We're moving all of that into our infrastructure. Anytime you need a human intervention, you want to evaluate and give context to that intervention, and you want it all to happen in your platform. So the task hub orchestrates that—if step 71 of 100 needs human intervention, that intervention happens in a single hub.

**Marcel Santilli:** The last part of the puzzle is the learn engine, which takes all the data that's now in our platform and learns from it.

**Marcel Santilli:** We built the AI workflow engine and essentially a Lovable-meets-Cursor tool for building workflows as code. All workflows are exposed via API endpoint. We can expose fact checkers, deep researcher, and others. The closest thing we're launching is the content OS. It's where companies like Ramp see all the assignments, pages we're monitoring, contributors, keywords, topics.

**Guillaume Cabane:** Who's the persona for this? Are you guys still deploying this as an agency model?

**Marcel Santilli:** People come to us and they're all under this directive—they need AI. They try tools like N8N and AirOps, then realize they need an AI GTM engineer, except that person doesn't exist. We had Unstructor.io churn from AirOps to join us, and they had a full-time engineer just building and managing workflows. So we use the service to figure out when to expose the workflow building engine. Right now, no one would know how to use it. UIs are so easy to build now that we're using our best workflows, personalizing and adapting them to companies, and giving them an OS that we run ourselves.

**Guillaume Cabane:** So it's running as an agency model for now, but on your own infrastructure instead of like the others.

**Guillaume Cabane:** Who do you compete with these days? AirOps directly? Daydream?

**Marcel Santilli:** Mostly AirOps and Daydream right now, but it's just so different. With AirOps, the strategy is missing and the day-to-day execution is missing. The successful accounts seem to just have their own engineers building and running workflows for people. Daydream is fully programmatic—they set variables and have very custom workflows, which is a fixed use case.

**Guillaume Cabane:** It's a very fixed use case, essentially, right?

**Marcel Santilli:** For us, the thing that's resonating is we built a Bolt.muse workflow in one day. Their data science team had no idea what their most common use cases were. We went through and processed all their usage data.

**Marcel Santilli:** We figured out other common use cases, then built another workflow that turned those cases into a one-shot prompt to build a fully functioning app. We put an AI engineer in the loop to review, deploy, and create landing pages. We're producing a bunch of pages. We built a prompt engine that takes a use case, builds an entire plan with a good stack, and creates an app or website that's way better. They were pretty shocked. We started doing strategy sprints—four or eight-week sprints doing full strategy and scoping. Then they either go into content or growth execution. Cases like Bolt or VAPI are different and require a different team than content execution work like Ramp.

**Guillaume Cabane:** What are you seeing as the gap? What are the things you wish existed?

**Marcel Santilli:** I'm curious, since you talk to so many companies.

**Guillaume Cabane:** I'm actually going to do some workflow coding myself for HyperGrowth for the next couple weeks. I was just playing around with Zapier, N8N, and a simple project, but it didn't work as planned. The level of complexity is actually multiple hours even with an LLM assistant. I wanted to turn my Hue lights red when I'm on a call. That's complex because there's no trigger for Zoom—you have to create a REST API that receives a webhook from Zoom, handle OAuth, and Hue's OAuth changed too. It's super complex.

**Guillaume Cabane:** I also had a project a year ago where I tried to connect all my LinkedIn inbound messages, invite requests, and score them against my ICP, then put LLM responses and book meetings. But it's maybe one in ten that are qualified. That's horribly complex because there's no API for the LinkedIn inbox—you have to use a headless browser, store auth somewhere, and handle anti-scraping measures. They're obfuscating endpoints. A lot of these projects, if you go outside templates, are very hard to build.

**Guillaume Cabane:** At HyperGrowth, we want to revisit which tools we should use for recording calls, storing recording information, which CRM to use, and how to use that data to make better judgment calls. That's not obvious. We've talked about probably 10 different products, but tools don't link them to CRM objects. If I go to the Lovable object in our CRM, it won't say that Marcel and I talked about it on this date. Someone has to manually update it.

**Marcel Santilli:** That's exactly what happened with Bolt. Their data science team had no insights, just old-school dashboards. We ran a workflow that did what you're describing.

**Guillaume Cabane:** Very hand-carved—take this transcript or data, here's session data, dissect it against a library of use cases with criteria and company context, then do API enrichments. The output was so much richer, and analysis was easier afterward. It's custom workflows. For another project in a few weeks, I'm connecting to PitchBook—we don't have expensive API accounts, so we'll scrape with my credentials and compare companies like Qualifx versus Datum versus AirOps, then get PitchBook data and traction data.

**Guillaume Cabane:** One-page summary. Let me look at my notes. There's no way to say that I got an email in February from Marcel about the updates showing you were at $5M ARR, and now it's $12M. How do we prep a templated email for me to ask you good questions to get an update? That's very easy to envision and very hard to pull off properly.

**Marcel Santilli:** That's so validating. Even for people like you and me—and you're more technical—the learning curve is huge. You go through all that, then Claude 4 comes out and changes something. You have to refactor the whole thing and a month of work is out the door. There's no reinforcement loop because you're not learning.

**Guillaume Cabane:** And you don't want to spend time connecting a bunch of APIs. We already have 70 different APIs. I was at SaaStr a few weeks ago, and it's interesting—CMOs are freaking out because the pace of change is so rapid you can't make good recommendations to your CEO anymore. What team skills do you hire for? I don't know what will be automated six months down the line. Do you need growth engineers? Probably not. What do you bet on?

**Guillaume Cabane:** Ten years ago I recommended Segment and Customer.io—good for two to three years, solid stack. Could I make that recommendation for the next 12 months? No way. I have no clue what will work 12 months from now. But implementation time and costs have gone up while implementation stays the same—six months to a year to change your stack. Because implementation is slow and tools change fast, everybody is frozen.

**Marcel Santilli:** I think people need a really good database, good retrieval, a good orchestrator, and then an intelligence layer. Some workflows are well-defined, others have agentic steps. When you research a hundred things, that's agentic. But when you have a hundred logical steps, you don't want an agent making that entire decision.

**Guillaume Cabane:** UI is so easy right now.

**Marcel Santilli:** It's insane. I take the output of our workflows, prescribe the stack, say "here's my workflow output, create a presentation layer," and it just does it. UI is instant, exactly what you want.

**Guillaume Cabane:** Where are you now on ARR?

**Marcel Santilli:** A little past $7M, but we've decided to focus less on growth at all costs and invest in platform. We hired 12 principal engineers and designers—Ran was head of design at Grammarly, Clint built Terraform at HashiCorp (hired number six), Felipe was early at Stripe, Airbnb, Apple, and EPPO which just got acquired. We're treating services as R&D, not growth at all costs. We're shooting to end the year at $12M and raise Series B in three to five months. We're already talking to Iconic and others. We're heads down for three months building this vision further. We have pieces but haven't put them in a presentation layer. We still want to grow but we're being selective. Strategy sprints started because bad clients are so distracting.

**Guillaume Cabane:** What success stories do you bring to prospects or VCs?

**Marcel Santilli:** Companies like Outreach, SentinelOne, Webflow, VAPI, StackBlitz—more on use cases than just growth. Growth is fine but might not last. People want to know what to do and what playbooks exist. Bolt is a good example. For bigger companies like Abnormal Security, we refresh thousands of pages and run their entire content playbook.

**Guillaume Cabane:** Should we do content together?

**Marcel Santilli:** Yeah, I'd love to. We have a videographer. When you're in town, we can do some recordings. I'll send you a link to an example—really good.

**Guillaume Cabane:** Let's do it.

**Marcel Santilli:** And what if you all became a non-paying customer?

**Guillaume Cabane:** For the custom stuff you're describing? If you want to build our workflows and we talk about it, I'd love it. We're trying to run super lean ops with some technical and non-technical people. Gonto has a few hours a week to evaluate deal flow, same for me. We need a deal flow evaluator from different sources—third-party data, PitchBook, Crunchbase, emails, recordings—to summarize opportunities. We also need help selecting which companies to work with as HyperGrowth advisory, evaluating the top 100-200 B2B SaaS startups. Scoring and outbound projects.

**Marcel Santilli:** Why don't we do a proper kickoff? Do you want to do it in person when you're in SF?

**Guillaume Cabane:** I'm sure your schedule is crazy. We can kickstart before. I'm based in SF starting July 4th, giving us about a month. We could do something for a few weeks and make sure it works when I'm in person.

**Marcel Santilli:** Perfect. Let's start with one clear use case—maybe the deal flow evaluator you mentioned. Then we can go from there.

**Guillaume Cabane:** Cool. Let me work with the team.

**Marcel Santilli:** We're doing a couple of kickoffs today and next Monday, but I'm sure we can fit in. You'll get exposed to the stack and how different it is from hand-carving things. Good validation.

**Guillaume Cabane:** Awesome. Let's do that.

**Marcel Santilli:** Did you get paid by Reddit? Are you still working with them?

**Marcel Santilli:** They're churning but we're trying to save them. Laura wants to continue, Chirag took over and hired Brian, then he got fired or left. I think we've been paid, but engagement is not super high.

**Marcel Santilli:** They're such a mess. They don't know what they want. They have so much potential but can't get out of their own way.

**Guillaume Cabane:** It's sad.

**Guillaume Cabane:** Okay, man.

**Marcel Santilli:** All right, sounds good, Guillaume.

**Guillaume Cabane:** I'll be in touch. See you.
