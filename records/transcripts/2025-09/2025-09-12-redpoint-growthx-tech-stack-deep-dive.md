# Redpoint <> GrowthX - Tech Stack Deep Dive

<metadata>
date: 2025-09-12
time: 17:30 UTC
duration: 31 minutes
organizer: Marcel Santilli
participants: Logan Bartlett, Adil Bhatia, Daniel Lopes, Marcel Santilli
fathom_recording_id: 86964425
fathom_url: https://fathom.video/calls/404282730
share_url: https://fathom.video/share/EQWyS1FP1KTHoGgDWTrXmqco1DXkskhX
source: fathom
enriched_on: 2026-03-03 21:15 UTC
</metadata>

---

## Summary

Marcel gave Redpoint investors Logan Bartlett and Adil Bhatia a deep dive into GrowthX's custom-built AI orchestration framework, positioning the platform as a proprietary alternative to generic tools like LangChain and N8N. The framework combines 200+ purpose-built microagents, a data-driven context engine, and a closed-loop learning system that captures human feedback to improve workflows. GrowthX is pursuing funding not from necessity (burning only $230K monthly while collecting $900K+ in the same period) but to scale two parallel product tracks: one for GTM engineers building workflows in code, and one for content strategists using a visual interface. Redpoint was impressed by GrowthX's outcome-oriented approach and plans to huddle internally, with GrowthX making a funding decision by the following week.

---

## Context

Redpoint Ventures is evaluating a potential investment in GrowthX, the B2B content marketing services firm that also builds CheckThat (an AI visibility index). This meeting was scheduled to address specific technical questions that Logan Bartlett had raised in a previous call but couldn't answer himself, requiring Adil Bhatia (a technical partner at Redpoint) to join. Marcel Santilli, GrowthX's founder, and Daniel Lopes, the VP of Product, walked through the platform's architecture to help Redpoint assess the investment. GrowthX is in a competitive funding environment where multiple VCs are interested, and they're also considering other partnerships. The team is being intentional about the decision—only pursuing capital if it provides strategic value for scaling, given their strong revenue traction and capital efficiency.

---

## Relevance

- **To GrowthX Business Development:** Redpoint is a tier-1 VC actively tracking AI/AEO frameworks and impressed by GrowthX's outcome-first approach. Logan and Adil explicitly noted that what GrowthX is building today ("pioneering how this can work across different functions") is what enterprises will catch up to in 2-3 years. Reference potential: strong fit for future customer introductions.

- **To GrowthX Delivery:** Daniel outlined the hybrid workforce layer (under development), which allows batch experts to review content asynchronously instead of via Zoom calls. Also flagged that microagent customization is parameterization-first (natural language configuration), not code-first, which reduces friction for forward deploy engineers working with clients like Clark and Town (IRS research use case, Office Zero sales adaptation).

- **To CheckThat:** Marcel and Daniel discussed the AEO/AI visibility strategy in detail. CheckThat grew out of the internal insights/monitoring module. They're still iterating on which prompts to track and how wording changes affect visibility rankings—a core insight that the context engine (understanding what topics to track) is as critical as the visibility tooling itself.

- **To GrowthX Strategy:** Daniel's explanation of the output.ai package and vibe code environment (for non-engineers to write workflows in natural language) is a major product differentiator vs. no-code tools. The closed-loop learning system (capturing human edits, running them through the coding agent to regenerate workflows) is unique and requires no Salesforce/proprietary data access—a major advantage for AEO/marketing use cases where results are publicly measurable.

---

## Overview

- GrowthX built a proprietary, end-to-end AI orchestration framework (output.ai) with 200+ microagents, less boilerplate than LangChain, designed from real marketing workflows rather than academic papers
- Platform combines runtime-based agent execution, human intervention loops, and closed-loop learning to deliver high-quality content at scale; knowledge base and context engine are custom-built, only third-party elements are Google Search Console APIs and LLM model access
- Company is executing a two-track product strategy: exposing workflow-building capabilities to GTM engineers through code-first tools, and to content strategists through a visual interface with pre-built components
- Redpoint impressed by outcome-oriented differentiation—GrowthX's human-in-the-loop system captures edits, regenerates workflows, and learns from human decisions; models outcome-based ACV (adding "two zeros" vs. tool-based pricing) without requiring access to proprietary customer data

---

## Key Topics

### GrowthX Platform Architecture

- Vertical interface with insights/monitoring, analytics (pulling from Google Search Console and Fathom), and knowledge base for content strategists and managing editors
- AI workflow engine: runtime plus coding framework with far less boilerplate than LangChain
- Hybrid workforce layer (in development): batch of hired experts (security content, editing) available on internal marketplace for asynchronous review instead of Zoom calls
- All components custom-built except Google Search Console and AI model APIs
- Knowledge base implemented as graph RAC with full-stack tracing: captures all API calls and LLM invocations, enabling iteration and code-generated workflow improvements

### Tech Stack Deep Dive

- Output.ai package: natural language plans generate folder structure (evals, prompts, workflow files, API client definitions)
- 200+ microagents for marketing tasks (researcher, drafter, fact-checker, infographics generator, etc.); 100 are fully reusable, 60 are prototypes for specific clients
- Parameterization: natural language configuration passed to agents and workflows without extensive code changes; used at Clark (SDK documentation for authentication vulnerabilities) and Town (IRS research focus)
- Full-stack tracing: every workflow run captures API responses and LLM data; coding agent uses this to regenerate workflows when human edits or feedback indicate a need for changes

### Differentiation and Competitive Strategy

- Built from real marketing use cases (Marcel's 15 years at DeepGram) rather than academic papers; avoids generic boilerplate
- Evidence from market: 170 people paid $500 each for Marcel's DeepGram workshops, less than 10 use the knowledge; customers with N8N/CloudCode access aren't building—only internal employees build, or they hire freelancers
- Code abstraction (vs. GUI-based workflow tools) is more scalable; new models require full refactoring in no-code tools but regenerate automatically in code-first frameworks
- Two parallel product tracks: (1) for engineers and AI deploy engineers building workflows in code using output.ai, (2) for content strategists using a library of pre-built components on the platform
- Vibe code environment (in progress): allow non-engineers to write workflows in natural language without traditional coding

### Human-in-the-Loop Closed-Loop Learning

- System captures human edits to articles, runs them through the coding agent, regenerates the entire workflow, then learns which version (A/B/C/D) humans prefer and why
- This loop doesn't require access to proprietary customer data (Salesforce, CRM) unlike customer support or sales automation; marketing outcomes are publicly measurable
- Self-hosted option: companies can run runtime and store all workflows, runs, and activities in their own repo, preventing loss of institutional knowledge
- Unique differentiator: competitors focus on agent or tool quality in isolation, but GrowthX connects human intervention, output ingestion, feedback signal, workflow recreation, and learning loops

---

## Action Items

- **Logan Bartlett (Redpoint Ventures)** and **Adil Bhatia (Redpoint Ventures)** to huddle internally and discuss investment decision
- **Marcel Santilli (GrowthX)** to continue meetings with other potential investors through the weekend
- **Marcel Santilli (GrowthX)** to make a go/no-go decision on the funding round by the following week

---

## Transcript
**Adil Bhatia:** It's a busy time.

**Adil Bhatia:** September is always a lot of stuff going on.

**Adil Bhatia:** This meeting is being recorded.

**Adil Bhatia:** Team has been traveling a bit over the last few weeks, too, so for deal stuff.

**Adil Bhatia:** So it's been busy.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** That's what happened.

**Marcel Santilli:** Like, July was good for us.

**Marcel Santilli:** And then August was like, whoa, crazy.

**Marcel Santilli:** And then September is like, what the ?

**Marcel Santilli:** It's like, everyone is just like, please, we need to start right now.

**Marcel Santilli:** I'm like, where have been all summer?

**Marcel Santilli:** Like, you know, it's like, everybody's like catching up and remembering they had a job kind of thing, you know?

**Adil Bhatia:** Yeah, yeah.

**Adil Bhatia:** There's like, there's like a short lull in August.

**Adil Bhatia:** And then, yeah, everybody's back at it at the same time.

**Adil Bhatia:** So, yeah, so it's been busy.

**Adil Bhatia:** But good to hear for you guys.

**Adil Bhatia:** I mean, that's awesome.

**Adil Bhatia:** You guys have obviously been growing well.

**Adil Bhatia:** And so it sounds like that demand is just going to keep going through the fall.

**Adil Bhatia:** So we got this week is a good week.

**Marcel Santilli:** We got Lovable, Base10, and Bubble as customers.

**Adil Bhatia:** Awesome.

**Marcel Santilli:** So maybe we can start with the punchline.

**Logan Bartlett:** Like, where are you guys in the process? When do you think you have to make a decision on stuff?

**Marcel Santilli:** So I think the way to kind of think about the problem—I know I mentioned this before—is we're trying to be super, super intentional.

**Marcel Santilli:** So we're having a couple more meetings today and then Sunday meeting with a couple, like one, one other investor that's pretty deep in kind of final steps.

**Marcel Santilli:** And then Monday, have a partnership meeting.

**Marcel Santilli:** We had another partnership meeting this week as well.

**Marcel Santilli:** And, and then hopefully by next week, we decide if we want to go ahead with the round or not, you know?

**Marcel Santilli:** But for us, it's less about the, trying to accelerate the process or trying to, it's more about like getting the right player and the right partner, if you will, because we're, we're pretty capital efficient.

**Marcel Santilli:** And so it's more, we weren't planning on raising right now.

**Marcel Santilli:** And, but I think like.

**Marcel Santilli:** There's a lot of players making a lot of noise in the market, plus there's a lot of links that we want to double down and build even more aggressively.

**Marcel Santilli:** So that's ultimately it.

**Marcel Santilli:** There has to be a strong benefit for us doing it now.

**Marcel Santilli:** It's only been four months since our Series A, so it's not like we're running out of money.

**Marcel Santilli:** We've only burned, I think, $230K last month, added over a million in that new.

**Marcel Santilli:** And so this month is only two weeks in.

**Marcel Santilli:** We've already collected almost $900K, so we're pretty in a good place, but we really think there's a lot of links we can double down on.

**Logan Bartlett:** Great.

**Logan Bartlett:** Okay, super helpful.

**Logan Bartlett:** Well, I know we spent a decent amount of time on the tech and what you guys are actually doing the last go-round.

**Logan Bartlett:** I thought it made sense for Adil to hear some of that stuff as well, and he had a few deeper questions that I wasn't totally able to answer.

**Logan Bartlett:** So I thought it made sense to get him on the horn and we could click into that stuff.

**Logan Bartlett:** Because I think that's an important consideration for us.

**Marcel Santilli:** Yeah, that's perfect.

**Marcel Santilli:** Shoot away.

**Marcel Santilli:** We're ready to go as deep as you want to go in.

**Marcel Santilli:** We love going deep.

**Adil Bhatia:** Awesome.

**Adil Bhatia:** Yeah, well, yeah, I know I missed that meeting.

**Adil Bhatia:** so I wasn't able to get some of the high level there.

**Adil Bhatia:** But yeah, I mean, like, I think I think maybe if we start overall, because I know in the memo that you sent, you had kind of the platform overview and you talk about the different components of it.

**Adil Bhatia:** And obviously, there's a lot of infrastructure underlying that that's also represented in that diagram.

**Adil Bhatia:** I don't know if you guys have any visuals that are helpful to walk through, but at a high level, like understanding, I guess, what you guys have built internally, what's really the proprietary stuff versus what you've used third party services for historically or still do.

**Adil Bhatia:** Just understanding that breakdown initially will be helpful.

**Adil Bhatia:** And then maybe we can double click into some of the more interesting parts of it.

**Daniel Lopes:** Yeah, maybe you want me to jump in and like walk in through some of the internals?

**Marcel Santilli:** That would be great.

**Marcel Santilli:** If we do that for like 10, 10 ish minutes, so we have plenty of time if we want to double click.

**Daniel Lopes:** Yeah, so just to give you the backstory—we have a pretty large product team for how long we've been around. The way we built the team is essentially a bunch of distributed systems engineers from HashiCorp, Airbyte, and Meltwater. They're in charge of our AI framework and our AI infrastructure, so think of it like our internal LangChain that we expect to make public next year.

**Daniel Lopes:** And then we have a bunch of product folks that are former founders or former CTOs who own entire features and move super fast whenever we need to build efficiency by creating apps to help our forward deploy content strategists and the clients we're onboarding, letting them use more as the things mature.

**Daniel Lopes:** The approach we're taking is essentially speed-running the Palantir play, where they spent 10 years figuring out the workflows for defense.

**Daniel Lopes:** And we have quite a bit of experience with the workflows for marketing already because of Marcel's 15 years of experience and what he did at DeepGram already.

**Daniel Lopes:** So when I joined, there were a bunch of things you need to do for marketing—individual components that vary a little bit from client to client or by client type.

**Daniel Lopes:** And so things like—think of it like a drafting agent or a researcher agent specific to content that always has citations with URL links in the markdown, for example.

**Daniel Lopes:** And then you have a fact checker for content and all the stuff that we knew we needed. So we build that as a layer first.

**Daniel Lopes:** And I'll show you a little bit how that looks. And then we started building the UI for the deploy folks to interact through a user interface instead of APIs.

**Daniel Lopes:** And now we're building the data loops to collect every edit and every change that happens—either to the UI or to the API—and it gets stored as a log file.

**Daniel Lopes:** So we have the vertical interface that I'm going to show you in a bit, and then we have the AI workflow engine, which is a runtime plus a coding framework similar to LangChain, but with much less boilerplate and less code so you can essentially vibe code workflows.

**Daniel Lopes:** So our forward deploy engineers that do client ops can vibe code workflows by forking our standard blocks.

**Daniel Lopes:** If there's something specific—like if you're doing medical field content—we might create a custom workflow for expert review that acts as a persona of an expert and removes prescriptions, for example.

**Daniel Lopes:** And then we have a layer we're building that's not live yet—a hybrid workforce where instead of jumping on a Zoom call for somebody to review an article, we have a batch of folks that we hire for security content or for editing certain types of content, and they're available on our internal marketplace.

**Daniel Lopes:** But essentially under the hood, what we have is—you might have seen a version of this.

**Daniel Lopes:** So our vertical layer that our forward deploy content strategists and managing editors use has an insights and monitoring area and analytics.

**Daniel Lopes:** We use the Google Search Console API to pull data from Google Search Console, and we're adding Fathom and Google Analytics data as well.

**Daniel Lopes:** And that's done. And then we have a GEO module as well, where we run your prompts and see where you get cited.

**Daniel Lopes:** And that part, we also have a knowledge base. Everything is custom—we don't use third party for anything.

**Daniel Lopes:** With the exception of the APIs for Google Search Console and APIs for models.

**Adil Bhatia:** And this is just around Google Search right now, right? I think we talked—Marcel, remember previously we talked about the AI or AEO category that's popping up, the AI visibility piece, which you guys are going to layer on or maybe have already, but it was kind of a near or medium term thing.

**Marcel Santilli:** Yeah, so we've ingested some of that data and we do it on behalf of customers. But what we started to realize is that the context engine we built is absolutely critical for understanding what topics you should be tracking and how, because it's all about the prompts you use.

**Marcel Santilli:** We've been changing the wording of which prompts you track and it completely changes how visible you are.

**Daniel Lopes:** Yeah, so essentially we spent the last few months using all the different tools, just validating how we want to use that.

**Daniel Lopes:** How the content strategists consume that. We built the building blocks internally for our team, and now we're extracting it as a separate tool that will also be a GTM tool.

**Daniel Lopes:** So this is the prototype—almost like a Figma. It works, but we're still iterating it and it doesn't look like the final version yet.

**Daniel Lopes:** But that's part of this chunk where we have a bunch of internal things that our clients and forward deploy folks use, and then things get extracted as external products.

**Daniel Lopes:** So CheckThat.ai, which is the GEO freemium tool, came out of our insights and monitoring module.

**Daniel Lopes:** And then we also have a company inventory that scrapes your site regularly to find opportunities to write, and we track if they're getting done, how they're getting done, and store context artifacts.

**Daniel Lopes:** So those are the things that we gather from the clients, and then they can take from there.

**Daniel Lopes:** And AI pipelines is where we stitch together all the agents and the AI workflows.

**Daniel Lopes:** And it's.

**Adil Bhatia:** And for the context element there, I mean, I know there's going to be a lot of documentation, like historical blog posts, historical collateral that you guys will ingest.

**Adil Bhatia:** What about, I guess, you know, in these engagements, you'll go through a period of, I don't know, four or six weeks, right, where you're iterating with the client to make sure you're hitting the exact objectives they're looking for.

**Adil Bhatia:** That sort of feedback, where exactly does that get ingested and how, if at all, can you automate some of that, I guess?

**Daniel Lopes:** Yeah, it depends.

**Daniel Lopes:** like, there will be feedback that rarely changes, and that would be, like, how they want their product to be perceived.

**Daniel Lopes:** So that will help them come up with.

**Daniel Lopes:** Like, for Clark, for example, we run our researcher on their website, get every information you have on their public data, and we show it to them.

**Daniel Lopes:** It's like, does that make sense?

**Daniel Lopes:** And then they might make edits.

**Daniel Lopes:** We update their artifacts, and that gets used throughout any of the content generation agents we have.

**Daniel Lopes:** If it is, if they have, like...

**Daniel Lopes:** Large, for example, Clark.

**Daniel Lopes:** Clark has a bunch of like SDK documentation for vulnerabilities that they want to cover, but only vulnerabilities around authentication.

**Daniel Lopes:** So for that, we have a knowledge base that every workflow we run will store things in that knowledge base on the topics we care about, or we can manually import.

**Daniel Lopes:** And the knowledge base, we're starting to let the clients use that more and more.

**Daniel Lopes:** And you can see the graph for Clark right now looks like this.

**Daniel Lopes:** takes a little bit to load the graph.

**Daniel Lopes:** And it will cluster around the things that are more, that will have more data.

**Daniel Lopes:** So we have a lot of data about Clark itself.

**Daniel Lopes:** So the cluster will be dense.

**Daniel Lopes:** We can write a ton about Clark.

**Daniel Lopes:** And then you can, and this is like a graph database with, it's an implementation of a graph RAC paper, essentially.

**Daniel Lopes:** And this is exposed to RAC and to APIs, and they can use in their cloud accounts if they want to, through MCP, or we use it through the platform.

**Daniel Lopes:** Where is this coming from?

**Logan Bartlett:** Like, how is this being generated originally?

**Daniel Lopes:** What do you mean?

**Logan Bartlett:** The artifacts or the...

**Logan Bartlett:** Yeah.

**Logan Bartlett:** I mean, all the different topical areas.

**Logan Bartlett:** Like, what is the starting point for something like this when they're getting up and going to get to this point?

**Marcel Santilli:** So, like, it starts with the kickoff where we are asking them, like, a lot of, like, about their business.

**Marcel Santilli:** It's an hour.

**Marcel Santilli:** That's the first day of the engagement.

**Marcel Santilli:** And then we do a ton of research on their competitors, the space, their audience.

**Logan Bartlett:** And then that's just kind of publicly available information that you guys are pulling in.

**Marcel Santilli:** Researching, correct.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And then they also send us docs, like, their brand guidelines.

**Marcel Santilli:** They'll send us, like, anything, like, product marketing, sales enablement.

**Marcel Santilli:** And they'll send us calls or give us access to Gong or whatever.

**Marcel Santilli:** And we'll ingest certain things from there as well.

**Marcel Santilli:** And then we essentially create a V0 of all these artifacts.

**Marcel Santilli:** And then that's when we start the kind of calibration process of them giving us feedback.

**Marcel Santilli:** And then as we start to calibrate on an output, we

**Marcel Santilli:** Start to realize that we need to generate additional artifacts potentially.

**Marcel Santilli:** So, for instance, with Biologica, it was like an ingredient bet check list, right?

**Marcel Santilli:** With Clerc, it's like code snippets or more details about the product or, you know, so these are essentially like artifacts that if you don't, in context, if you don't generate, you won't be able to.

**Logan Bartlett:** sense.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** Yep.

**Daniel Lopes:** So that's essentially this layer—a bunch of user interface—and this layer, the runtime layer, lets you create any kind of marketing-related agents in a couple of hours at most. We have the coding agent that generates the workflows. It's all custom built.

**Daniel Lopes:** There's nothing third party. The only thing we use that we build a framework on top of is Temporal, a distributed systems infrastructure tool (open source). That's the architecture.

**Adil Bhatia:** So you're saying this is basically a custom-built orchestration framework, top to bottom—is that the right way to think about it?

**Daniel Lopes:** Exactly.

**Daniel Lopes:** So we have an internal package called output.ai. You install it, create your project—you do output.new, like growthx, or whatever—and then you pass natural language plans, and it generates a folder with files that look like what we have here.

**Daniel Lopes:** So you have auto-generated evals, prompts for each step, the workflow itself, the steps of the workflow, and the types for the inputs and outputs of the APIs. The bulk of the work is generating good prompts, good steps, and API clients.

**Daniel Lopes:** That's why we have folks from Airbyte.

**Daniel Lopes:** So every time you run it, you get a runs JSON with the whole data for any kind of API.

**Daniel Lopes:** So you have things like LLM usage and tools, API and LLM API monitoring, tracing.

**Daniel Lopes:** We do full stack.

**Daniel Lopes:** So if you make an API to Google search, we get that data, and then we get the LLM data as well, and that is in the trace.

**Daniel Lopes:** That's what powers the ability to iterate on a workflow through a coding agent. So you can say, "I didn't like this result, the API response from Google Search wasn't good—what can I do?"

**Daniel Lopes:** And we'll create a new step or edit a prompt. We're also adding—this part is in progress—the ability to log whatever changes humans make as good or bad choices, and that will be in the same folder with the workflow.

**Daniel Lopes:** That's why we map all the workflows in code instead of building GUI-like tools, because we want to generate more workflows and new versions are created from code.

**Daniel Lopes:** And the complexity is much deeper—sophistication can go as much higher.

**Adil Bhatia:** Okay, got it.

**Adil Bhatia:** So the forward deploy engineering folks working with your clients are the ones utilizing the runtime.

**Adil Bhatia:** Is there an abstraction layer on top of the runtime that the experts on your platform can access to, or is that not necessary for how you're actually delivering?

**Daniel Lopes:** We figure out what are the common components every client needs versus what's specific to just that client. And then we end up with a library of common workflows.

**Daniel Lopes:** And that's a platform that a content strategist can come to and trigger. For example, we have a researcher where if they want to research a specific topic, they can run an execution choosing different tools.

**Daniel Lopes:** That sits on top of a runtime. Every workflow becomes a usable, independent component, and sometimes they want to be executed in sequence—that's when we use the other part.

**Daniel Lopes:** When we start onboarding clients straight to this in self-service, it'll be GTM engineers or forward deploy AI engineers using this.

**Daniel Lopes:** And the other part, Atlas.growthx, is what our clients—marketers—will operate as soon as we have the right onboarding.

**Daniel Lopes:** We're still figuring out who the precise ICP is that can operate this. We can operate anything—Marcel could operate both parts of the stack—but we can't expect a Marcel to exist.

**Daniel Lopes:** So we're trying, like, what's the minimum common sophistication that we can get to onboard folks?

**Marcel Santilli:** Yeah, and right now, to understand the gap where the market is—it's not about the tooling. The tooling was there.

**Marcel Santilli:** The reason I got 20% organic traffic with DeepGram wasn't because the tooling did the work.

**Marcel Santilli:** It was the strategy, connecting the dots, having the right context, and the right output quality bars to make sure it was good in the last-mile execution piece.

**Marcel Santilli:** That's the connecting tissue—over time, as customers feel confident they can be successful on their own with strategy and everything else.

**Marcel Santilli:** But it's also about how you capture value. Being outcomes-based as opposed to tool-based allows us to add two zeros to our ACV.

**Daniel Lopes:** A big part for us was figuring out the processes. What are the standard primitives that every marketer needs?

**Daniel Lopes:** Those are the microagents we build. Once we have 200 of them, you can stitch them together in different ways.

**Daniel Lopes:** That's too complex for most people, so we're not expecting them to create something like this.

**Daniel Lopes:** This one has 1, 3, 6, 9 steps, and we have agents that generate infographics, do research, and draft content.

**Daniel Lopes:** But we can expose those agents in an easier way for other folks—maybe in the next iteration managing editors could use them.

**Adil Bhatia:** Yeah, yeah.

**Adil Bhatia:** How much customization is involved, especially with the context piece—iterating with the client on the information that matters most when producing content?

**Adil Bhatia:** I get that's custom to every client. When it comes to the microagents or subagents—how much customization is there at that layer? How much is necessary? Have clients asked for that? And if they do, how do you instantiate it?

**Daniel Lopes:** It's very literal customization. We usually start by specializing.

**Daniel Lopes:** For example, Town (a Texas company) wanted content focused on IRS.

**Daniel Lopes:** So we built a general-purpose agent that focuses on certain sites for Town.

**Daniel Lopes:** Now we use it for Office Zero as well.

**Daniel Lopes:** Office Zero uses it in a different way.

**Daniel Lopes:** They wanted to do it for sales instead of marketing.

**Daniel Lopes:** Every agent is an import package you can use.

**Daniel Lopes:** You import the research agent, add configuration for sales instead of marketing.

**Daniel Lopes:** Most of it can be done through prompting. Some might be done through code, but very little.

**Daniel Lopes:** Out of 200, 60 are prototypes—what does this client mean, what do they become—and 100 are fully reusable.

**Daniel Lopes:** Infographics and drafting are fully reusable, but there's a ton of parameterization you can pass.

**Daniel Lopes:** Every workflow, agent, and sequential workflow can take a natural language list of what you want, and it transforms into the parameters it needs.

**Adil Bhatia:** That's helpful.

**Adil Bhatia:** I think we've spent a good amount of time with these frameworks, so that makes sense. Taking a step back—you've built out a lot of features, the strategy and business model appeal to many customers. We're seeing enterprises, particularly the higher growth tech-forward companies you're working with, start experimenting with different orchestration frameworks—building on top of LangChain, trying N8N, building their own—right?

**Marcel Santilli:** They've got the engineering to do it.

**Adil Bhatia:** But the more scaled, upper-mid-market ones like Abnormal have deep knowledge of how their growth marketing function works. The knowledge Marcel brings is valuable, but they have their own practices and ways of doing this.

**Adil Bhatia:** So the question is—will some of these folks try to build this end-to-end internally? Or what parts of the orchestration framework you've built are too proprietary or difficult for them to take on?

**Marcel Santilli:** That's exactly what I did. At DeepGram, I spent thousands of hours building workflows, then we did 170 workshops where people paid $500 and I spent five hours teaching people.

**Marcel Santilli:** Out of those 170 people, less than 10 actually use it. DeepGram is a customer—I've opened up their N8N instance and no one is building.

**Marcel Santilli:** I've opened up instances for some other customers, and they say, "We bought this workflow," but nobody's building. Only internal employees at those tool companies are building, or they hire networks of freelancers saying "Can anyone help me build N8N workflows?"

**Marcel Santilli:** So for us, it's unmaintainable to stitch together those things. What people do is use CloudCode to generate files to import to N8N.

**Marcel Santilli:** But then you go step by step, click, edit, confirm. And when a new model comes out, you have to refactor the whole thing.

**Marcel Santilli:** That's the wrong abstraction layer. Code is a better, more scalable abstraction.

**Marcel Santilli:** For us, building it as a service and outcome-based was the best way to understand what primitives we needed to scale.

**Marcel Santilli:** Daniel's got us on a really great iterative approach—build for engineers, then AI forward deploy engineers, then people like me, then standard users.

**Daniel Lopes:** The main differential for us is that my previous company came out of Basecamp, which created Rails. Django, Rails, and React came from real use cases because they solved real problems, not because they were selling technology first.

**Daniel Lopes:** We're trying to solve a real problem. Almost all our things ended up with the right premises because we're getting data from real experts in the market.

**Daniel Lopes:** We create agents for specific needs, so our agent framework makes sense. It's not abstract LangChain from papers.

**Daniel Lopes:** Now we have almost no boilerplate. The amount you have to write for a perfect agent is so small that our coding agent generates most workflows.

**Daniel Lopes:** Folks are just running natural language requests all day. The next layer will be a vibe code environment where Marcel can vibe code his own.

**Daniel Lopes:** Versions, and that's under the hood.

**Daniel Lopes:** And then we have the other part on top for marketers where they can start with analytics.

**Marcel Santilli:** We don't talk about it too much yet because it's not out there, and we don't want to give too much away. But it'll be a REPL-like experience for building full agents—higher quality than any agent on low-code platforms.

**Adil Bhatia:** So over the next year or two, you're exposing capabilities to customers so they can build content themselves.

**Daniel Lopes:** Exactly. It's two parallel tracks.

**Daniel Lopes:** Like one is a parallel track for the forward deploy GTM engineer.

**Daniel Lopes:** One is for forward deploy GTM engineers, the other for content strategists. Over time they'll move to be more internal and less dependent on our forward deploy folks. That's why we need the money—two lanes, both large.

**Adil Bhatia:** Honestly, as Logan alluded to at the start, you've built something special and robust. We haven't seen technology built this way yet, but it's exciting. We've been tracking these frameworks for a couple of years.

**Adil Bhatia:** We've seen people use CloudCode to stitch together workflows, but seeing something so outcome-oriented and data-first seems like the best way to build this. You're pioneering how this works across functions.

**Marcel Santilli:** One thing—because you get it—it's very unique. Even if CloudCode is perfect and N8N is great infrastructure, no one's thinking about the human intervention step. The full loop: ingest outputs, capture outcome signals, then the human intervention.

**Marcel Santilli:** Then recreating the workflows that agents and deterministic workflows do, then learning from those loops. When there's one intervention—say you fix a comment in an article—

**Marcel Santilli:** The coding agent rewrites the whole flow and brings it back. Then a network of people decides A, B, C, or D is better—"Why D?"

**Marcel Santilli:** Learning from that and closing the loop is what we're sprinting toward. No one has closed that loop—you still copy and paste to ChatGPT. That loop is really hard.

**Marcel Santilli:** You go to Upwork and vet thousands of freelancers to validate. The models are broken—people tackle the agent side in silos, separate from the expert side, production side, and output side.

**Marcel Santilli:** So we're trying to connect those dots.

**Adil Bhatia:** It's kind of like a perfect use case to pull this all together.

**Adil Bhatia:** We've looked at other applications like customer support—those are more reactive, focused on cost reduction. Maybe there's revenue output over time, but marketing is different.

**Adil Bhatia:** They don't require the human loop you're talking about or depend on output signals the same way.

**Marcel Santilli:** I love that. We can push something public and prove it worked.

**Marcel Santilli:** We can do that without Salesforce data or proprietary data, so we're not stuck anywhere.

**Adil Bhatia:** And you're not goal-seeking because it's marketing.

**Adil Bhatia:** There's a wide range of outcomes when people engage with the content. It's a really compelling use case. Thank you for walking through what you've built—it's exciting and impressive.

**Logan Bartlett:** We were talking before—regardless of the investment, we're super interested in your business. You're on the cutting edge commercially. We're definitely smarter after this, and what you're doing today is probably what enterprises will be doing in two years when they catch up.

**Marcel Santilli:** I appreciate it means a lot coming from you all.

**Marcel Santilli:** We think this model can power outcomes and it can already be self-hosted.

**Marcel Santilli:** You can have a repo with all your workflows, runs, and activities, and a runtime layer that runs inside your company. People aren't copying and pasting things to ChatGPT.

**Marcel Santilli:** You're not throwing things into Google Docs losing the learning loop. That's the big long-term unlock—can this be blueprints where you codify high-value expert work?

**Logan Bartlett:** For sure.

**Logan Bartlett:** Well, thank you, guys.

**Logan Bartlett:** We're going to huddle up later today and over the weekend.

**Marcel Santilli:** We'll be in touch.

**Marcel Santilli:** Sounds good.

**Daniel Lopes:** All right.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** Thanks, talk soon. Bye.
