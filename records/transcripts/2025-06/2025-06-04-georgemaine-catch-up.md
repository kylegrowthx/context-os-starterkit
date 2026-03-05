# Georgemaine Catch up

<metadata>
date: 2025-06-04
time: 17:03 UTC
duration: 44 minutes
organizer: Daniel Lopes (GrowthX)
participants: Georgemaine Lourens (new engineer), Daniel Lopes (GrowthX)
fathom_recording_id: 66488260
fathom_url: https://fathom.video/calls/317300884
share_url: https://fathom.video/share/QsG7kQHJzVRkW-ZZMXuVBq2U9y4y_YFV
source: fathom
enriched_on: 2026-03-03 18:39 UTC
</metadata>

---

## Summary

Daniel Lopes conducted an onboarding call with Georgemaine Lourens, GrowthX's new engineer (day 3 of employment), covering company architecture, product strategy, and immediate next steps. Daniel walked through GrowthX's two-product strategy (Flow workflow engine + Flow Studio IDE) and the Atlas project (content management and SEO tool for clients), explained the organizational split between strategy and execution teams, and clarified that Georgemaine should spend his first week with the client ops engineering team (Marcus and Kirkland) before joining the larger Atlas project. The company is actively moving away from AirOps and Airtable (deadline June 16) to build proprietary tools that reduce onboarding friction and cost.

---

## Context

Georgemaine Lourens just started at GrowthX as an engineer and is on day three of his onboarding. He met with Daniel Lopes to understand company structure, product direction, and team organization. The relationship is internal onboarding—Daniel is helping Georgemaine understand the big picture before he begins actual project work. GrowthX is a B2B content marketing agency ($200k+/year engagements) that's simultaneously building CheckThat (an AI visibility index tool) and internal software to scale their operations. The call happens during a critical period: the company has a June 16 deadline to fully exit AirOps (their previous workflow platform), the platform team is building Flow and Flow Studio, and the client ops engineering team is just beginning their first cycle. Georgemaine has already met several people (Kirkland, Marcus, Renato, Mara, Wolfram, Daryl, Matt) and expressed eagerness to start contributing.

---

## Relevance

**To GrowthX Delivery:**
- New engineer onboarding pattern: one week with client ops team (Marcus, Kirkland) to learn workflows and processes before platform work. This is a standardized ramp for all new engineers.
- Flow Studio is designed as a simplified IDE to help non-technical folks (Marcel, Jason, George) build and iterate on workflows without CLI friction. Current focus: visualization and debugging; future: workflow creation and editing.
- Client ops engineering team is the bridge between strategy team prototypes and execution team work—they build starter kit templates, micro-apps, and handle client requests (Webflow integration, Stripe workflows, etc.).
- Critical dependency: AirOps exit on June 16. Workflows and editor experience have already been moved off AirOps; remaining work is migrating content editing workflows out.

**To CheckThat:**
- Atlas dashboard includes AI visibility metric powered by Scrunch (Google Analytics for AI—tracks mentions in ChatGPT, Gemini, Perplexity). This is core to CheckThat's positioning.
- AI visibility is foundational to Atlas and to GrowthX's content strategy—validates whether content is reaching AI models and drives the "planting seeds" approach to content creation.

**To GrowthX Business Development:**
- Long-term vision: GrowthX as an incubator (like Tiny) with multiple verticals (marketing/content, recruiting, VA/EA services). Each vertical will have its own Atlas-like tool. Flow is the common infrastructure.
- Potential spin-offs: recruiting (source, parse, identify fake applications) and EA/VA workflows (summarization, tagging, Slack/Salesforce integration).
- Client relationship maturity: Moving from one-off SEO audits (Airtable) to continuous content management and refreshing. This is a product shift that increases stickiness and account value.

---

## Overview

- GrowthX is developing two core products: an AI workflow engine (Flow) and a web UI (Flow Studio) to support their agency operations and future verticals
- The company is transitioning away from third-party tools (AirOps, Airtable) to reduce costs and confusion
- Atlas project is the current priority, aiming to create a comprehensive content management and SEO tool for clients
- Georgemaine will spend his first week with the client ops engineering team before potentially assisting with the Atlas project

---

## Key Topics

### Company Structure and Organization

  - **Two main business teams:**
    - Strategy team (Marcel, George, Marisol, Jason): Ideation, client pitching, and eight-week strategy sprints that often compress to 2-3 weeks
    - Execution team: Content creation and project management; runs 2-3 hour weekly cycles on sprint work
  - **Two engineering teams:**
    - Platform team: Experienced engineers building core infrastructure (Flow, Flow Studio). High hiring bar.
    - Client ops engineering team (Marcus, Kirkland + 1 offer pending): Builds workflows, handles client requests, creates micro-apps on top of Flow. Lower hiring bar; hire for diverse backgrounds (SEO, journalism, etc.). All new engineers spend at least one week here as part of onboarding.
  - **Organizational pain point:** Rapid headcount growth without guardrails caused onboarding friction. Too many tools (AirOps, Airtable, Motion, Slack, CRM). Solution: client ops team enforces process; software (Flow, Studio, Atlas) provides guardrails.

### Product Architecture

**Flow (AI Workflow Engine)**
  - Core system for creating and running workflows
  - Currently combined with workflow code in one repo; plans to separate runtime into a package
  - Inspired by Django and Rails extraction pattern (frameworks developed inside products then extracted)
  - Potential for multiple verticals: marketing/content (primary), recruiting, VA/EA services
  - All workflows live in Flow repo as files; Flow Studio is the UI on top

**Flow Studio (Web IDE)**
  - Web UI for workflow visualization and execution; currently a debugging/inspection tool
  - Inspired by DBT Studio: code-first (not drag-and-drop) with text-based abstractions for non-technical users
  - Future roadmap: execution from UI → history tracking → workflow creation from UI → PR generation to GitHub → chat-based workflow creation
  - Goal: Balance between code (engineers) and visual interfaces (non-technical folks like Marcel)
  - Metaphor: DBT started as CLI + SQL; built web UI on top; doing the same with workflows (code + text-based UI, not WYSIWYG)

**Atlas (Content Management and SEO Tool)**
  - Comprehensive platform for managing client content lifecycle
  - **Core features in development (Ren's focus):**
    - Dashboard: Metrics (AI visibility, published content count)
    - Pages and opportunities: Content inventory with SEO audit, keyword rankings, search volume, Google Search Console traffic, persona matching
  - **Future features (mocked for feedback):**
    - Inbox: Client communication integration with Slack posting
    - Assignment manager: Track content creation pipeline (draft → review → scheduled → published)
  - **Key innovation:** Continuous refreshing cycle. Today: one-off Airtable audits. Tomorrow: automatic crawling, content enrichment, opportunity tracking, and refreshing suggestions.
  - **AI visibility metric:** Powered by Scrunch (Google Analytics for AI). Tracks mentions in ChatGPT, Gemini, Perplexity.

### Product Strategy and Verticals

  - **Vertical one (primary):** GrowthX agency (marketing/content). Atlas is the management tool.
  - **Vertical two (exploring):** Recruiting. Workflows for sourcing, resume parsing, identifying fake applications. Potential separate tool (like Atlas) later.
  - **Vertical three (exploring):** VA/EA services. Workflows for summarization, Slack tagging, Salesforce syncing, team management. Potential separate company.
  - **Long-term vision:** GrowthX as a holding company (like Tiny) owning multiple vertical-specific products, unified by common Flow infrastructure. Possibly licensable to external companies.

### Business Transitions

  - **Moving away from AirOps:**
    - Relationship soured when AirOps copied GrowthX workflows and marketed them to GrowthX clients
    - Marcel had helped with AirOps investment and roadmap; conflict of interest
    - December 2024: Moved workflow execution out of AirOps; built proprietary Flow engine
    - June 16, 2025 deadline: Exit content editing workflows from AirOps platform
    - Status: On track, but some risk remains. Daniel is full-context owner.
  - **Moving away from Airtable:**
    - Currently used for one-off content audits (URLs, keywords, opportunities, SEO issues)
    - New approach: Atlas provides continuous, automated auditing and refreshing
    - Reduces costs and confusion; improves client experience

### Onboarding and Team Dynamics

  - **Georgemaine's onboarding plan:**
    - Week 1: Client ops engineering team (Marcus, Kirkland). Learn workflows, processes, real client requests.
    - Week 2+: Potentially Atlas project (if not overloaded). Large project with hard deadline; needs ramp time.
  - **Client ops team strengths:**
    - Marcus: Full-stack engineer with broad experience across GrowthX tech stack
    - Kirkland: 1-2 years engineering experience, but strong SEO, marketing, and journalism background. Career switcher.
    - Low barrier to entry compared to platform team; hires for potential and diverse backgrounds
  - **Onboarding philosophy:** Hands-on work with real workflows beats documentation. Test vs. production; everyone spends time here.

---

## Action Items

- **Georgemaine Lourens (GrowthX):** Complete onboarding and watch Marcel's workshop videos (5 hours on AI workflows) before joining client ops team
- **Georgemaine Lourens (GrowthX):** Spend next week (week of June 9-13) with client ops engineering team to understand workflows and processes
- **Georgemaine Lourens (GrowthX):** Watch Daniel's demo of the fact-checker app next week to understand micro-apps built on Flow
- **Georgemaine Lourens (GrowthX):** Potentially assist with Atlas project development in weeks 3+, pending capacity and project needs
- **Georgemaine Lourens (GrowthX):** Prepare for San Francisco in-person team meeting at end of July

---

## Transcript

**Georgemaine Lourens:** Oh yeah, I a rant on you.

**Georgemaine Lourens:** Yeah, and Felipe told me as well.

**Daniel Lopes:** Yeah, so give me the context of who you've met so far.

**Georgemaine Lourens:** Yeah, well obviously it's day three, so I haven't met that many people.

**Georgemaine Lourens:** But my goal for this week was kind of just like go through onboarding and also just build some relationships.

**Georgemaine Lourens:** So I wanted to meet everyone in the team.

**Georgemaine Lourens:** I met I met Kirkland, I met Marcus, Renato, and Renato also mentioned like, hey, you're probably going to work a lot with POTS, so try and meet a couple of people there as well.

**Georgemaine Lourens:** And he gave me a few people.

**Georgemaine Lourens:** So I met Mara today, Wolfram, gave me a lot of insights as well.

**Georgemaine Lourens:** I think I met Daryl too.

**Georgemaine Lourens:** And.

**Georgemaine Lourens:** Thank you.

**Georgemaine Lourens:** And.

**Georgemaine Lourens:** Thank you.

**Georgemaine Lourens:** Thank

**Georgemaine Lourens:** Matt.

**Georgemaine Lourens:** Matt earlier today.

**Georgemaine Lourens:** So not that many, but I'm trying to keep a diverse group.

**Daniel Lopes:** Yeah, got it.

**Daniel Lopes:** Yeah, so just to give you the update from the last month since the last talk, I think.

**Daniel Lopes:** It's been more than, it's probably more than a month, I think two months, maybe.

**Georgemaine Lourens:** Yeah.

**Daniel Lopes:** man, so much happened.

**Daniel Lopes:** So we have, we had the on-site.

**Daniel Lopes:** I can walk you through some of the stuff that we covered to give you a little bit of context.

**Daniel Lopes:** It might be too much for you to absorb in just one call.

**Daniel Lopes:** But yeah, so that was, what we realized is that we have essentially four areas of the company, four areas of the architecture of what we're building.

**Daniel Lopes:** And it's kind of too much for everybody to just get that on their own.

**Daniel Lopes:** So the on-site was pretty helpful for people to just get together and we just go through all the things.

**Daniel Lopes:** Things that Marcel and I were thinking about, and then we think about all the different things we could build in the future, and then just focus on one thing, or focus on a couple of things.

**Daniel Lopes:** And that's what we're doing right now.

**Daniel Lopes:** So the project that Felipe and Brad are working on, actually wasn't clear to them that this project is actually a small feature of a much larger product we're building, that is the platform to make the agency scalable.

**Daniel Lopes:** And so that will combine a bunch of things that we're super opinionated about on how to run an agency like ours, and like the agents we have is a pilot for doing that and seeing if we can make that business grow and be replicable on itself, and that's what we're struggling with right now, so like at the business level.

**Daniel Lopes:** So we have a bunch of clients, and we have a bunch of pods, and we have a bunch of people onboarding people that were onboarding.

**Daniel Lopes:** So we kind of grew that layer too much, too much too fast, and the plan was to overstep it and then have the capacity there and then slowly build them up so they could catch up and learn and then be useful in like a couple of months, three months later.

**Daniel Lopes:** But without the guardrails, without the systems for them to learn, it's relying only on human process to teach people, and that's very like, it depends on the manager on the pod, depends on the client that's coming in, depends on too many variables, know, and then also depends on like people learning all these different tools we use.

**Daniel Lopes:** So we use air ops, use air tape, use motion, use Slack, and all this stuff, and we also use like recording notes for the meetings sometimes that we share with clients, and we have the CRM as well, there's all these things that like everybody needs to be like juggling, so, and so that's the thing that that's one.

**Daniel Lopes:** Part of the project, so Felipe and Brad were working on that, Felipe especially, he's been working on that for a couple of months already, like just building our path out of air ops, because that was the part that was too hard for people to learn, and we also had quite a bit of, like the relationship with air ops was starting to sour over time, because they were like looking at our workloads and doing features of that, and then marketing it, and then they started like hitting our clients, like contacting our clients to go straight to them.

**Daniel Lopes:** Yeah, yeah, exactly, and Marcel had a close relationship with them, and like we helped them get their investors, the person that lead the investment was introduction from Marcel, and so it was pretty close relationship, Marcel was helping them with roadmap and all that we had then in our Slack to share like ideas, but then they started like looking at what we were doing with their product with like the workflows itself and baking the net side templates for people to use.

**Daniel Lopes:** Thank you.

**Daniel Lopes:** And that's some of the things that triggered us moving out of our ops in December on top of their platform and running 12 things in parallel.

**Daniel Lopes:** So they were struggling and everything was crashing.

**Daniel Lopes:** So we moved all the workflow execution out of it and we built our own thing.

**Daniel Lopes:** And then we were already in the process of moving up of the experience of editing the content there.

**Daniel Lopes:** Because now the workflows are out and all what people use their ops for is essentially coming up with ideas, like using workflows to generate ideas out of like scraping URLs or like enriching topics or keywords and trying to like do the research on those and create an article out of that.

**Daniel Lopes:** And in the process of actually creating the article, like generating the outline and generating the type and then iterating on it and then generating the article itself and then iterating on the article and all that.

**Georgemaine Lourens:** So it's kind of like a more friendly, it's kind of like them wireframing and just, it's kind of like a playground.

**Georgemaine Lourens:** For them to figure out what they eventually want to get to, because it's just a more user-friendly interface.

**Daniel Lopes:** Yeah, so it's more like for them, AeroOps, we have two kinds of people on the team.

**Daniel Lopes:** that's like, actually, now we are like enforcing that, and we are like baking that into the organization structure.

**Daniel Lopes:** But if I were you, I wouldn't spend time with the execution team of the pods yet, would spend time with the strategy team.

**Daniel Lopes:** So we have two teams, and we have the strategy team is Marcel, George, Marisol, and I'm forgetting, but there's one more person, and Jason as well.

**Daniel Lopes:** those are the people that are like coming up with ideas, how the client, what is important for the client, what is possible.

**Daniel Lopes:** And we have engineers in the mix as well, to validate if what they are pitching to the client is doable, and help them iterate on the contents.

**Daniel Lopes:** And so now we have this idea of a strategy sprint, that is up to eight weeks.

**Daniel Lopes:** But in reality, it's been like much shorter.

**Daniel Lopes:** Like Marcel can crank up a bunch of stuff in like a couple of days, and then the team hits on that.

**Daniel Lopes:** We ended up doing that in like maybe a couple of weeks, three weeks, but not full time.

**Daniel Lopes:** So the idea is that we have this thing first.

**Daniel Lopes:** They will come up with ideas, we'll prototype, they will like figure it out.

**Daniel Lopes:** And then they will set up the system where execution team to perform the creation of the articles.

**Daniel Lopes:** And their work will be more on like making sure that the project is on track on the deliverable role.

**Daniel Lopes:** So like maybe it's like 20 articles a week, or maybe it's 100 articles a week if it's like programmatic.

**Daniel Lopes:** Helping find the person that will be, if we need like a special fact checker, like a developer that will be reviewing quotes snippets.

**Daniel Lopes:** We need to hire this person somehow.

**Daniel Lopes:** And also like making the communication of the client and making sure the things is like on track.

**Daniel Lopes:** And we also might need to have like part time designers helping come up with the illustrations and things for the article that match their design system.

**Daniel Lopes:** So we have some workflows that we're trying to figure out.

**Daniel Lopes:** But it's like 80% there, but not quite fully for some of the bigger clients.

**Daniel Lopes:** So that's kind of the split we have today on the agency side.

**Daniel Lopes:** And the software that we're building is meant to support the execution team more than anything.

**Daniel Lopes:** It will help the strategy team too, but it's more like the guardrails for the execution team to not have to learn all the new tools.

**Daniel Lopes:** So, and what Brad and Felipe have been working on, and it only clicked to them like this week when I joined the project actually.

**Daniel Lopes:** So that was a huge mistake in my end of like not really like giving the full vision of the thing.

**Daniel Lopes:** And because I didn't spend time like designing the whole like the extra features around of the thing that they're doing, like they were not seen as a part of a project team.

**Daniel Lopes:** Okay.

**Georgemaine Lourens:** And so I can walk you through that And with the generic, you're referring to the stuff that you shared in the large beds in Ocean Dog, right?

**Georgemaine Lourens:** Where you walk through the whole...

**Daniel Lopes:** Yeah, exactly, but so that's the area of Spark, we were already planning to move, and then they got pretty upset by a couple of accidents, a couple of mistakes we made, where Tucker, our recruiter, was using an AI tool to do outbound sourcing for engineers, and we ended up hitting some of their engineers, because they're like, an AI workflow.

**Daniel Lopes:** So things started to go south, and then, so we have like a deadline for exiting their platform in the fall week, so 16, June 16.

**Daniel Lopes:** Things are going fairly well, I think we are on track, there's still like, still, there is still risk, so that's where I'm spending all my time this week, just making sure we are going the right direction, because I'm also the only person that has, the full context on how we,

**Daniel Lopes:** Use workflows, how we use our grid, what the business does, and now most of the guys that joined like a month ago, like Brad joined a month ago and I got thrown into this project, I think it has been for a couple of months.

**Daniel Lopes:** For them it's still pretty early.

**Daniel Lopes:** So, and I'm also doing the work of the client ops engineer.

**Daniel Lopes:** So like on our engineering side, we have two teams as well.

**Daniel Lopes:** And the two teams is like the platform team.

**Daniel Lopes:** And that's everybody that will be building these tools, these features dedicated to this part.

**Daniel Lopes:** And then we have the client ops, ops engineering team, which are the folks that run in like a cycle format that we actually kick off the first cycle this week.

**Daniel Lopes:** And they receive requests from our internal team, the directors, from the managing editors.

**Daniel Lopes:** And they also come up with like new workflows.

**Daniel Lopes:** They come up with like potential micro apps we can build on top of those workflows.

**Daniel Lopes:** It will work on some of the more strategic clients, for example, Bolt as one of our clients.

**Daniel Lopes:** So we were coming up with ways to generate starter kit templates for them that creates pretty cool apps with just one shot.

**Daniel Lopes:** And we are also creating the small apps around that just to show how it works.

**Daniel Lopes:** And they might have to figure out the web flow integration for them.

**Daniel Lopes:** So they are doing all these things to make the clients move.

**Daniel Lopes:** And this team right now is Marcus and Kirkland are the ones full-time on it.

**Daniel Lopes:** And then one thing we've been doing is everybody that joins, we ask them to spend at least one week on that team.

**Daniel Lopes:** So you get the swing of building workflows and things like that with real work.

**Daniel Lopes:** Because doing the onboarding project is all like a test things.

**Daniel Lopes:** And we also have an offer out for another engineer.

**Daniel Lopes:** So it's going to be three folks soon.

**Daniel Lopes:** And I think we might, the team, we might.

**Daniel Lopes:** Another one next week.

**Daniel Lopes:** it's going to be like four folks full-time, and they're also going to be the bridge, like whatever agency we might need to hire.

**Daniel Lopes:** So if we need to have an agency to do like web flow work or strappy work or like any front-end stuff that we don't think it's necessary to have like one of our folks full-time on that, they would be the one like getting the request from the client, distilling it into something that an agency can do, and then monitoring the results.

**Daniel Lopes:** So that's the split of the teams we have today.

**Daniel Lopes:** Okay.

**Daniel Lopes:** But everybody on the client ops team, they're also like Marcus is full-stack engineer with a ton of experience on all the different things we use in our stack.

**Daniel Lopes:** Kirkland is pretty good with like workflows.

**Daniel Lopes:** So like they will be also contributing everywhere else.

**Daniel Lopes:** And so it's not like a super like rigid split.

**Daniel Lopes:** But it's more like that the people on the platform team, the bar for joining was super.

**Daniel Lopes:** So everybody is super experienced, and that's what I wanted to do first, and then we build around them, and the client ops team, the folks are a little bit less experienced.

**Daniel Lopes:** Kirkland, for example, has one or two years of experience as an engineer, but he has a ton of experience as an SEO director and running a marketing agent.

**Daniel Lopes:** So he has, and then he's also a has background in journalism, so like a lot of stuff that we do, he has a boatload of experience.

**Daniel Lopes:** So, and he wanted to, and he wanted to make the switch to be an engineer, so he's a perfect person for that time.

**Daniel Lopes:** So like, in the client ops, that's where we're getting people with different profiles, where it would probably not pass a system design interview, for example, with Felipe, if we're shooting for the same levels.

**Daniel Lopes:** Does that make sense?

**Georgemaine Lourens:** Yeah, no, I think that makes sense.

**Georgemaine Lourens:** Like, was speaking to Kirkland today.

**Georgemaine Lourens:** And he explained.

**Georgemaine Lourens:** In his background, and he mentioned that he used to work in agencies and he kind of wanted to make the switch making things, so I kind of got a glance at this experience, but I also feel like the client ops, that team, they need someone that kind of helps with iterating on all of the prompts, so I think it makes sense that you guys have made this.

**Daniel Lopes:** Yeah, and that team will also be a team that everybody should be able to write prompts, and everybody will be a heavy user of what we're building on the other side, so maybe I can give you a quick walkthrough of the two different products.

**Daniel Lopes:** Yeah, sure.

**Daniel Lopes:** And that might give you a better understanding of things.

**Daniel Lopes:** Yeah, go for it.

**Daniel Lopes:** Yeah, so we have, let me show you from the doc.

**Daniel Lopes:** I just actually updated this doc and I added this screen.

**Daniel Lopes:** I think I showed you this during our chat, but that was a while back.

**Daniel Lopes:** Yeah,

**Daniel Lopes:** Yeah, so the idea here is that we have the AI workflow engine, and this is what we refer in all the conversation, the GitHub repos and everything as flow.

**Daniel Lopes:** Flow is the whole thing.

**Daniel Lopes:** And then we have a studio product inside, which is the web UI on top of the executions.

**Daniel Lopes:** But the AI workflow engine is essentially anything that's related to creating workflow, the code base to generate the workflows, and also where you keep the workflows, and how you run them.

**Daniel Lopes:** That's the runtime.

**Daniel Lopes:** And then the developer experience is the studio project that I was talking about.

**Daniel Lopes:** So if you look in GitHub, have flow is one repo, that's where all the workflows are.

**Daniel Lopes:** And then you have flow studio, that's a second repo, which is a tailwind, sheds, and react app with like a back end in Rails.

**Georgemaine Lourens:** And so, yeah, because the way that I kind of looked at it right now, when I was setting up the code basis with Marcus, is that Flow is kind of like the container of all of the workflows, and that's also where all of the workflows run.

**Georgemaine Lourens:** And the workflows themselves are just kind of like files within that repo, and they're running there.

**Georgemaine Lourens:** But I didn't quite understand what Flow Studio was.

**Georgemaine Lourens:** was kind of like, I don't know, like an overview, like a pipeline of all of the workflows that were running in real time or something.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So the Flow Studio is, let me explain it.

**Daniel Lopes:** So like the, one thing on the Flow repo, like right now, it's all the code base for the workflows and all the necessary code to run them.

**Daniel Lopes:** In the future, we want to extract the part that is about running the workflows into a package.

**Daniel Lopes:** It would be a separate package and all you would have in your project folder would be the workflows.

**Daniel Lopes:** And the reason for that is because we want to have other companies creating workflows in the same way, like even ourselves.

**Daniel Lopes:** So we have the growthx agency is our first vertical for like testing the idea of like workflows and AI agents making a big part for people's jobs and make people more efficient.

**Daniel Lopes:** The second vertical that we were a couple of other verticals we were thinking about, one is a recruiting to help recruiters source, parse resumes, identify fake applications, things like that.

**Daniel Lopes:** Most of what we already do, but now it's all inside of the same folder with all the growthx related things, like all the marketing related things.

**Daniel Lopes:** And then the third vertical that we were...

**Daniel Lopes:** Considering would be something related to VAs or EAs, where you could have a lot of things around summarization, around keeping tags on things like Slack, keeping tags on things like Salesforce.

**Daniel Lopes:** We have a bunch of workflows that would make an EBA like Alice.

**Daniel Lopes:** We have a few in the team that helps with a ton of different things.

**Daniel Lopes:** And there's a bunch of things that we could do for them, and that could be a separate company.

**Daniel Lopes:** So that we're thinking like, it's almost like an incubator, and the project, the code base we have today, it's all together.

**Daniel Lopes:** think of it like when Django was getting created, I think it was like Chicago Tribune, like the code base for the Django framework was inside of the website for a while until they got it out and made it reusable.

**Daniel Lopes:** The same thing with Rails.

**Daniel Lopes:** in 37 Signals was built in Basecamp, the code base of Rails was embedded into the Basecamp code base for like the first year.

**Daniel Lopes:** And then they pulled it out and made it open source.

**Daniel Lopes:** So...

**Daniel Lopes:** Same idea.

**Daniel Lopes:** So that's why the running part is stitched together with the code base for the workflows now.

**Daniel Lopes:** But we're starting to try to separate the folders already.

**Daniel Lopes:** The next step would be to pull it out.

**Daniel Lopes:** So that's on that side of the code.

**Daniel Lopes:** And then we have the studio.

**Daniel Lopes:** Studio is essentially...

**Daniel Lopes:** Let just move you to the side so I can make sure I see.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** The studio part is essentially...

**Daniel Lopes:** Sorry.

**Daniel Lopes:** I have a giant monitor here.

**Daniel Lopes:** But the studio part is a way for us to see the workflows executing.

**Daniel Lopes:** And in the future, we'll also be the place where you could vibe code workflows.

**Daniel Lopes:** Right.

**Georgemaine Lourens:** And essentially like prototype.

**Daniel Lopes:** And depending on the complexity of the workflow, create all the way to the end.

**Daniel Lopes:** And then you only need an engineer to like make it like more efficient, cost less or...

**Daniel Lopes:** Different models and things like that.

**Daniel Lopes:** So today, all it does, like you can see the workflows that are getting executed, you can see the steps, and you can see the description of each step, you can also see the graphs of that workflow.

**Georgemaine Lourens:** Right, so it's just a visual way of looking at what the inputs are and the outputs are and kind of like the description is kind of like the visual diagram of all of the steps that you can learn from it, right?

**Daniel Lopes:** Yeah, so today is essentially a debugging tool and like an inspecting tool.

**Daniel Lopes:** What we want to have in the future is this should become more like a proper IDE.

**Daniel Lopes:** So there is this tool that like, most of the inspiration from this came out of it, and it's this tool called DBT.

**Daniel Lopes:** It's kind of a technical tool, it's kind of hard to explain, but it started as a CLI tool.

**Daniel Lopes:** So, for...

**Daniel Lopes:** For...

**Daniel Lopes:** It started as a consulting company that was joining product teams and helping them organize their data warehouse.

**Daniel Lopes:** So data analysts and product teams could have like an organized data warehouse for their reporting, their BI tools or for their machine learning projects.

**Daniel Lopes:** So, and what they realized is like every company needed a way to run essentially cron jobs to extract things from different places, combine them into a new table in a polished instance of like Snowflake or Fospers or something like that.

**Daniel Lopes:** And so they started as a CLI tool where you just write the SQL, like in plain SQL, the tables that you want and the sources that you want.

**Daniel Lopes:** So you'd annotate the sources and all that and be your editor.

**Daniel Lopes:** So like in cursor or in like in VS code and then have this script that would run it to all different places, creates the table for you and run that on the web.

**Daniel Lopes:** And you could just self-post that yourself.

**Daniel Lopes:** And then, and that took.

**Daniel Lopes:** It went super viral, all the data analysts, all the data teams were using it, and then they build a UI on top of this after to make your life easier to visualize.

**Daniel Lopes:** So this, for example, is the one that I would have from my previous company.

**Daniel Lopes:** I still have it running because I help them sometimes.

**Daniel Lopes:** And that will give you an idea of how I think, the direction that I...

**Daniel Lopes:** This might be too much to show you in your first poll, but...

**Georgemaine Lourens:** Oh, I would love to look at something else than Marcel pilling it in workshops.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** Let me show you.

**Daniel Lopes:** So, DBT was essentially open sourcing, and they were struggling to make money, and they were struggling to have some of the less technical folks get involved.

**Daniel Lopes:** And then they came up with the web UI.

**Daniel Lopes:** And the web UI is the way I'm thinking about the studio.

**Daniel Lopes:** Like, we use this thing called Temporo, and the route is super technical.

**Daniel Lopes:** It's to understand.

**Daniel Lopes:** Even our engineers are like, what?

**Daniel Lopes:** Why do you need this?

**Daniel Lopes:** And then the UI that we build is a way to simplify that thing so people can expect the workflows happening.

**Daniel Lopes:** And all of our non-technical folks like Marcel, Jason, George, they're looking at that and they understand.

**Daniel Lopes:** They're pitching the workflows, they're showing to the client that all the time.

**Daniel Lopes:** The next step for that would be like letting them do some of the work too, and that's what DBT does.

**Daniel Lopes:** So DBT has this studio part of their project that will just connect to the GitHub that has all the SQL code and has a bunch of abstractions on top to make things easier to understand.

**Daniel Lopes:** So for example, for my company before, we're using Salesforce as our CRM and we had our database.

**Daniel Lopes:** So all the things we're doing is just like combining the Salesforce with our CRM and also Stripe.

**Daniel Lopes:** So we could know who are the clients, who are the business of churn, and then create the tables for churn, create the tables for high potential clients and things like that.

**Daniel Lopes:** So you would essentially define the tables in SQL like this, plain text, and this code is in GitHub, and it's just syncing the GitHub repo here, and whenever you make changes, it creates a new branch, so it's essentially a Git client, but has a bunch of niceties on top, like for example, it's visualizing all the dependencies for the SQL, and then it can highlight and see, and then you can make changes and preview.

**Daniel Lopes:** Yeah, so it can make changes and execute just that chunk, and then I can also write my SQL here, and it will have things for like checking the code quality, formatting, and like writing the queries for me, so now they have their SQL where it just essentially writes the things for you, they have the co-pilot, and so you can like, you have all things combined, you you don't have to be using like the CLI for Postgres to try to see the UI, so that was a big part of the pain for like data analysts, it's like, okay, I need the UI, to see the data, and like

**Daniel Lopes:** I need to be able to download this CSV.

**Daniel Lopes:** I need to sort things and all that.

**Daniel Lopes:** So that's the same.

**Daniel Lopes:** This is the metaphor that I'm thinking.

**Daniel Lopes:** So while everybody's building workflows like Aeroops, there's so many tools that are UI-based workflow building tools.

**Daniel Lopes:** Aeroops is one.

**Daniel Lopes:** Another one is Velen.

**Daniel Lopes:** So Velen is a lower level.

**Daniel Lopes:** There's a spectrum of workflow companies.

**Daniel Lopes:** And you have link chain on the one end, where you can code your workflows, and that's it.

**Daniel Lopes:** It's just like open source library, code, no UI, essentially no code.

**Daniel Lopes:** They got funding and all that.

**Daniel Lopes:** So they're trying to figure out some products around it, but started as plain code.

**Daniel Lopes:** And then you have, in the other spectrum, you have things like Aeroops and NAN and time.

**Daniel Lopes:** And Aeroops is little bit, it's like time focused on the marketing space and SEO space.

**Daniel Lopes:** And then as you go into the middle, you have...

**Daniel Lopes:** This here on this side is for engineers.

**Daniel Lopes:** This thing is for like non-technical folks.

**Daniel Lopes:** As you go into the middle, you have something like Vellum.

**Daniel Lopes:** So Vellum is a workflow creation tool for engineers.

**Daniel Lopes:** So this is how you create AI features for products.

**Daniel Lopes:** And then they have an SDK.

**Daniel Lopes:** They still, they also have the GUI for building the workflows like this.

**Daniel Lopes:** And, but they are GUI first.

**Daniel Lopes:** They started as GUI first.

**Daniel Lopes:** And we are doing the opposite.

**Daniel Lopes:** We're starting code first, but with the idea that we want to have a GUI to help non-technical folks build things.

**Daniel Lopes:** But instead of being drag and drop, make it text-based, you know, the same way as V0, Bolt, and all those folks are like, it's, they're not trying to create a WYSIWYG, like we tool.

**Daniel Lopes:** They're trying to just make code easier to generate, you know, and closer to what you want.

**Daniel Lopes:** So it's the same idea.

**Daniel Lopes:** So, so that's the way I'm thinking about this studio.

**Daniel Lopes:** Studio right now is just like an...

**Daniel Lopes:** action tool.

**Daniel Lopes:** The next step would be to start building the things for letting you execute the workflows from there.

**Daniel Lopes:** And then the next one is to help keep track of the history of that workflow in one place.

**Daniel Lopes:** And the next step would be to let you create a new workflow from scratch and send a PR to the original GitHub repo.

**Daniel Lopes:** And then the last one would be maybe you can just chat and create your workflow from sharing.

**Daniel Lopes:** And then the next one would be letting you edit the workflow by sharing, to what we can do with Cursor Vizier.

**Georgemaine Lourens:** You know, so now it makes sense because I was missing this part because I felt like, OK, we have we have Atlas here where everyone can manage the work with can run the sprints and work with the clients.

**Georgemaine Lourens:** And then we have studio over here where every single workflow is housed.

**Georgemaine Lourens:** But in the end, you kind of want people to be able to iterate on all of those workflows and make their own.

**Georgemaine Lourens:** Right.

**Georgemaine Lourens:** Because otherwise you constantly just have to have someone like Kirk make all this stuff.

**Georgemaine Lourens:** Yeah, exactly.

**Georgemaine Lourens:** But if this part is kind of like the metaphor that you're thinking about.

**Georgemaine Lourens:** Because I feel like you have either people who can work with code, which is the best, but not everyone can do that, or you have the very visual thinkers who are on the other side of the spectrum, and then you get into the models where you connect this with that and this with that, but that gets messy really quickly.

**Georgemaine Lourens:** And then there's the metaphor that seems to really work, where you just kind of use text and you just talk to someone, it's conversation-based.

**Georgemaine Lourens:** Exactly.

**Georgemaine Lourens:** And if you mix that in the right way, that could work.

**Georgemaine Lourens:** That could really work.

**Georgemaine Lourens:** Yeah.

**Daniel Lopes:** So that's the two areas, the two products we have now.

**Daniel Lopes:** And like the way for us to think about is that like Atlas is the vertical project management tool to manage all of our accounts for the marketing side.

**Daniel Lopes:** We would, if things go well, let's say like next year or like end of this year, we would probably have a separate vertical tool.

**Daniel Lopes:** For like recruiting, completely separate from Atlas, and another one from EAs, and like we start prototyping these different potential businesses, and maybe they will spin off and be their own companies, or maybe they will be inside of GrowthX, or we haven't understand yet that side of things.

**Daniel Lopes:** But the way we think is that we'll be more like, if things pan out in the way that we're thinking, like five years from now, ideally, we would have a company that's like Tiny, where you have like a group, and then under Tiny, you have a bunch of different companies, you know?

**Georgemaine Lourens:** Yeah, mean, they own the MetaLive guy, right?

**Daniel Lopes:** Yeah, exactly, and you, yeah, like they own Dribbble, they own like a bunch of, they own even like AeroPress, and like, they, but they also have a bunch of like, softer products, and ideally, we would have that, but using our common infrastructure, and we could even like, the plan is to also like, figure out the ways to make our common infrastructure accessible to other folks outside the company, so that is this chart here.

**Daniel Lopes:** so.

**Daniel Lopes:** Let me actually see if there's something else that I can walk you through, but did you have a chance to look at these videos here and all that?

**Daniel Lopes:** Yeah, I watched them all.

**Georgemaine Lourens:** I found them very useful.

**Georgemaine Lourens:** I'm just dying to help out.

**Georgemaine Lourens:** I do know that I have to go through my own boarding and watch all of the videos, and they're super useful.

**Georgemaine Lourens:** So I'm watching all of the workshops that Marcel is doing right now, which is kind of like five hours of him, like, owning everyone with AI workflows, which is really inspiring to see.

**Georgemaine Lourens:** But obviously, I want to get to the point where I can start helping out, and help with eBay, and then Brad move faster.

**Daniel Lopes:** Yeah, think, like, it would be cool to, like, maybe next week, we could get you to help the guys that are on the...

**Daniel Lopes:** And top cycle with like some of the small tickets and just to get the hang of like using a couple of workflows.

**Daniel Lopes:** And we also have some things that we're thinking about apps that will be built on top of our workflows, like similar to what you did for your recruiting.

**Daniel Lopes:** And the first one that we're thinking about is our fact checker.

**Daniel Lopes:** I did, I've quoted this in like 30 minutes just to give it a try.

**Daniel Lopes:** But this is on top of our workflow.

**Daniel Lopes:** I can walk you through that next week.

**Daniel Lopes:** But I think like throwing more people into the access project might not be the good time for that.

**Daniel Lopes:** Yeah, that's right.

**Daniel Lopes:** It would be nice to have you like on board and understand the pain of the client ops team and understand the kind of requests that they get by being part of that cycle just for like one week.

**Daniel Lopes:** And then after that, then we could get your help on.

**Daniel Lopes:** The Atlas project, because the Atlas project is pretty gigantic.

**Georgemaine Lourens:** Yeah, and I know that you guys have the deadline, so kind of like, if you throw me on that right now, then it will only delay everything, then it will do any good.

**Georgemaine Lourens:** So I think that makes sense.

**Daniel Lopes:** Yeah, like the Atlas project, the way we're thinking is that we have multiple areas, you know, it's like, this is the main areas you have.

**Daniel Lopes:** So like right now, that's what we're executing on, and that's what we've got to do no matter what.

**Daniel Lopes:** This is what Ren is trying to figure out now.

**Daniel Lopes:** So this is the part of the product today that I have it here that's just like faked a bunch of parts of the tool.

**Daniel Lopes:** So like, this is not working, this is just fake data, but this is working.

**Daniel Lopes:** So if I go into an account, let's say there's like Webflow or Abnormal or both any of the accounts you have, you can go in and then we'll have like a dashboard where this is all fake data too.

**Daniel Lopes:** Just walking out so folks can understand what's happening, what's the plan.

**Daniel Lopes:** And ideally, we'd have a dashboard for that account with number of pages we published for them, what's their AI visibility for.

**Daniel Lopes:** AI visibility is based on AI mentioning your website, for example, on questions and answers.

**Daniel Lopes:** So that's something that we are also thinking about.

**Daniel Lopes:** We're building a wrapper around Scrunch.

**Daniel Lopes:** Scrunch is this other product.

**Daniel Lopes:** Scrunch is AI.

**Daniel Lopes:** It's essentially Google Analytics for AI questions.

**Daniel Lopes:** Then you can see how many times your company was mentioned by ChatGPT, Gemini, Perplexity, and things like that.

**Daniel Lopes:** So that's AI visibility is core.

**Daniel Lopes:** And then we have some other metrics that we're thinking about.

**Daniel Lopes:** And you have some of the articles that are in draft stage, in review, and scheduled to publish.

**Daniel Lopes:** And what the folks on our team would be, like, recently doing.

**Daniel Lopes:** And so that would be just the dashboard.

**Daniel Lopes:** board.

**Daniel Lopes:** And you would have maybe like in the future, the hope, like I just mopped this up so folks would understand what are the potential future features.

**Daniel Lopes:** The really thing that's actually working is the projects that come in production.

**Daniel Lopes:** But just to give you the tour, so the inbox would be like where folks could like talk to the client maybe in the future and have that posted to the Slack channel.

**Daniel Lopes:** And then pages and opportunities is what Ren is working on right now, trying to figure out how that will look like.

**Daniel Lopes:** And that is this project here.

**Daniel Lopes:** So idea here is for some freaking reason, there's no way today, there's no system today that you can just input the URL of your website and will keep it in sync with like keywords you rank for, if the text is well written, if there are opportunities for the personas you care about, if there are like SEO issues even, like there's like a mix of content inventory.

**Daniel Lopes:** your text.

**Daniel Lopes:** And SEO audit and persona matching based on your offerings.

**Daniel Lopes:** And some of this stuff was also not possible to do before.

**Daniel Lopes:** There's a lot of it that's just like parsing the text and understanding the text.

**Daniel Lopes:** But that's essentially what we use Airtable for today.

**Daniel Lopes:** But it's like a one-off.

**Daniel Lopes:** So we do the audit and do like this generation of content and we find opportunities and we pull the URLs from the client and pull the URLs from competitors of the client.

**Daniel Lopes:** And we do that once.

**Daniel Lopes:** And ideally, would be doing that on the regular.

**Daniel Lopes:** It's just too hard.

**Georgemaine Lourens:** that they can kind of like constantly look at it themselves and then kind of keep themselves busy so we don't have to do that.

**Georgemaine Lourens:** Exactly.

**Daniel Lopes:** Like a big part of content creation is like planting the seeds.

**Daniel Lopes:** So you don't have to have the super baked articles.

**Daniel Lopes:** You just like do like a somewhat half-assed article and see which one's getting next.

**Daniel Lopes:** And then the next thing is, okay, now we actually need to make this a lot better.

**Daniel Lopes:** So then you put an editor to like do manual work on that article, for example, make it a ton.

**Daniel Lopes:** And that's what we call refreshing.

**Daniel Lopes:** Refreshing is a big part of it, but it's so hard to track that we barely do it, and it should be like 70% of the work for most of the clients that have something published, or at least for the clients that we also publish a ton for them.

**Daniel Lopes:** So that's something that is part of the things that we're not thinking about, like net new opportunities, refreshing opportunities, views where you have property discovery, like automated crawling, and then content enrichment, like each URL gets enriched with traffic from Google Search Console, Search Volume, Keyword Rankings, and all that.

**Daniel Lopes:** And so that's the big part that we think the next step would be like our air cable exit.

**Daniel Lopes:** Air cable is hard for people to understand the way we use it.

**Daniel Lopes:** So we're slowly moving away from the stuff that both costs a ton of money and also causes a lot of confusion.
