# Technical Deep-Dive on GrowthX // Radical

<metadata>
date: 2025-09-06
time: 18:00 UTC
duration: 68 minutes
organizer: Marcel Santilli
participants: Marcel Santilli (GrowthX), Daniel Lopes (GrowthX), Richa Mehta (Radical), Felipe (Radical), Bo Wang (Radical)
fathom_recording_id: 85451535
fathom_url: https://fathom.video/calls/402666632
share_url: https://fathom.video/share/5xjZFc4MmqAVZ2eeQ1eFQ9z8YsFfVgeT
source: fathom
enriched_on: 2026-03-02 01:30 UTC
</metadata>

---

## Summary

Marcel and Daniel walked Radical partners through GrowthX's core architecture: a vertical content marketing app layer, a general-purpose AI workflow engine built in TypeScript with self-contained agent folders, and a hybrid workforce combining high-leverage strategists with AI execution and marketplace-based last-mile work. The company achieves 70-72% gross margins (compute only 3%) by leveraging coding agents to handle bulk work, human experts to define processes and maintain quality, and plans to scale marketplace adoption to reduce per-client human dependency. Key challenges for 5x growth over two years include building a scalable marketplace to distribute specialized tasks, maintaining workflow quality as complexity grows, and expanding the vertical-specific product layer (currently content marketing) to support diverse client workflows.

---

## Context

Radical Ventures invited Marcel Santilli and Daniel Lopes to walk through GrowthX's technical architecture and business model. The meeting included Radical partners Felipe and Bo Wang, with Richa Mehta facilitating. GrowthX is a B2B content marketing services company that has grown to $11M+ in ARR by combining AI coding agents, human expertise, and proprietary workflow automation. The company was founded on Marcel's experience building content engines for companies like HashiCorp and ServiceTitan, which evolved into AI-native workflows. Daniel joined after spending seven years at Basecamp and IFTTT, bringing deep expertise in automation platforms and distributed workflows. This was a technical deep-dive aimed at helping Radical partners understand how GrowthX differentiates itself through its custom-built framework, hybrid workforce model, and approach to scaling services through technology.

---

## Relevance

**To GrowthX Delivery:**
- Confirmed that compute costs are only 3% of total opex — the real cost driver is human expertise (strategy, process architecture, quality control). This validates the services-software hybrid model and positions marketplace scaling as critical to margin expansion.
- Validated technical approach: workflows-as-code (TypeScript/REST API with 50-line-max structure) is more scalable than no-code/visual tools. All workflows now live in a single repository, allowing coding agents to auto-generate improvements and suggest PRs based on human feedback patterns.
- Key architectural bottleneck for scaling: not compute or core workflow logic, but the vertical app layer (content marketing UI) that must be rebuilt for each client. Building a micro-LookerStudio analytics dashboard for every new client takes 2-3 weeks per implementation.
- Marketplace strategy for last-mile execution (publishing, image selection, CMS integration) is foundational to hitting 5x customer growth while keeping strategist headcount flat. Current plan is to formalize task rubrics and evaluation metrics similar to data labeling platforms.

**To GrowthX Business Development:**
- Customers are highly sticky: major clients (Superhuman, Abnormal Security, Webflow, Sentinel) have been retained 12+ months despite being young company. Current pricing range $9K-$230K/month with several high-margin accounts (e.g., Abnormal paying $50K across 4 workstreams with 80%+ margins).
- Renewal risk is low because workflow maintenance complexity creates lock-in. Example: Superhuman merged with Grammarly and is now remigrating content across Superhuman, Grammaly, SoftRecord, Coda under single brand — estimated tens of millions to execute without GrowthX.
- New customer acquisition in forward-deploy phase is significant investment ($30K+ contracts for 6-8 week strategy sprints: interviews, knowledge base setup, content strategy design) but backloaded revenue through monthly retainers justifies it.
- Radical is evaluating as a potential investor/partner — Felipe and Bo Wang pushed on marketplace viability, cost structure, and biggest technical bottleneck for 2-year horizon, suggesting deep due diligence.

---

## Overview

- GrowthX has built an AI-native platform combining workflow automation, coding agents, and human expertise to deliver high-quality content marketing at scale
- Their approach uses a vertical-specific app layer, a general-purpose AI workflow engine, and a hybrid workforce model to balance automation with human oversight
- Key challenges include maintaining workflow quality as they scale, building out a marketplace for specialized tasks, and evolving their tech stack to support rapid growth

---

## Key Topics

### GrowthX Overview and Business Model

  - Evolved from AI workflow workshops to a full-service content marketing platform
  - Revenue of $11M+, working with brands like Webflow, Abnormal Security, Sentinel
  - Pricing ranges from $9,000 to $230,000 per month for clients
  - 70-72% gross margins, with compute costs only 3% of total

### Technical Architecture

  - Custom-built framework for creating coding agents and workflows
  - Uses TypeScript, REST API, and open-source components
  - Self-contained workflow folders with prompts, execution steps, and evaluation criteria
  - Internal tool (Atlas) for content inventory, AI-assisted editing, and pipeline management

### AI and Human Collaboration Model

  - AI agents handle bulk work (research, drafting, fact-checking)
  - Human experts focus on strategy, process architecture, and quality control
  - Marketplace planned for specialized tasks and last-mile execution
  - Aim to incrementally improve human interventions and AI capabilities over time

### Evaluation and Quality Control

  - Use "LLM as judge" for automated quality checks and self-improvement loops
  - Human review for critical tasks and final approvals
  - Working on auto-generating workflow improvements based on human feedback

### Scalability and Future Plans

  - Current focus on content marketing, with potential to expand to other verticals
  - Building out marketplace to match specialized tasks with qualified contractors
  - Exploring options to open-source parts of their framework or offer self-serve products

### Competitive Advantage

  - Full-stack solution combining AI, human expertise, and domain knowledge
  - Ability to handle complex, evolving content needs (e.g., catalog management, rebranding)
  - Continuous improvement of workflows and knowledge base

---

## Action Items

No explicit action items committed in this meeting. The conversation was exploratory with Radical partners asking clarifying questions about technical architecture, cost structure, scalability, and competitive positioning. Implicit next steps for GrowthX: finalize marketplace rubrics and task vetting process, expand vertical app layer beyond content marketing, and open-source framework components for ecosystem adoption.

---

## Transcript
**Felipe:** This meeting is being recorded.

**Daniel Lopes:** Oh, no, we weren't everything pretty much.

**Daniel Lopes:** It's not that big of difference.

**Richa Mehta:** Thank you all again.

**Richa Mehta:** I think what would be most helpful maybe is just Marcel and Daniel giving Felipe and Bo a quick overview of the company, what they're building, and then it'd be great to maybe just spend this time diving into the tech, showing them a little bit of the demo, sort of where all the code lies, all of that, and then we'll sort of have Felipe and Bo ask some questions if that works.

**Marcel Santilli:** But thank you all for taking the time.

**Richa Mehta:** I love it.

**Marcel Santilli:** I hope you guys are ready to geek out.

**Marcel Santilli:** But maybe I'll do, Daniel, just a quick three-minute and then take over.

**Daniel Lopes:** Cool.

**Marcel Santilli:** Yeah, yeah, this is good.

**Marcel Santilli:** So a quick background on me. I've been a CMO and growth leader for a little while at a couple of different companies like HashiCorp, ServiceTitan, ScaleAI, and a few others.

**Marcel Santilli:** And then along the way, the main way to grow organically was to build content engines for these companies, you know, and high quality content.

**Marcel Santilli:** And so I did that my whole career pretty much and was, I think, successful.

**Marcel Santilli:** But then most recently, I started to just build these kind of AI workflows to streamline a lot of my processes and how I thought about things a little bit, right?

**Marcel Santilli:** And then hiring the same people I normally would hire and put them in the loop.

**Marcel Santilli:** Did that at DeepGram and with 24XR traffic.

**Marcel Santilli:** And then it really took over or took off and started doing workshops teaching people how to build workflows from that.

**Marcel Santilli:** And after 170 people paid 500 bucks to come to them, realized people didn't want to learn how to build workflows.

**Marcel Santilli:** They wanted to actually help getting good quality work done that helps them grow.

**Marcel Santilli:** And that building workflows was really freaking hard. So we started as services software for growth and mostly focused on content.

**Marcel Santilli:** And along the way, you know, I'll let Daniel kind of talk about his background and whatnot.

**Marcel Santilli:** As Daniel kind of came in and really started thinking about, like, how do we approach this from our first principles?

**Marcel Santilli:** We really started to realize that in order to scale services, we needed to build the engine that builds the engine and really get back to code.

**Marcel Santilli:** And so we built a coding agent that kind of builds a lot of the workflows and continue to kind of scale that out.

**Marcel Santilli:** So I won't go too much into that detail because Daniel will cover a lot more.

**Marcel Santilli:** But the TLDR on the business now is we grew to a little over 11 million and we get to work with a lot of amazing brands.

**Marcel Santilli:** We just signed Lovable yesterday, I was mentioning, which is pretty exciting.

**Marcel Santilli:** But, you know, like Webflow, Abnormal Security, Sentinel, RAM, all the way to seed stage companies as well.

**Marcel Santilli:** And so I'll let Daniel kind of.

**Marcel Santilli:** Dig in a bit more, but happy to kind of jump in along the way if needed.

**Daniel Lopes:** Yeah, to give a little bit of my background.

**Daniel Lopes:** So like when I met Marcel, I was taking a sabbatical after like seven years of bootstrapping a spinoff from Basecamp, 37 Signals.

**Daniel Lopes:** And with the realization that the next couple of years would be crazy.

**Daniel Lopes:** And that would probably be the craziest race that I have ever seen in our careers in the last 25 years that I've been in tech.

**Daniel Lopes:** And I wanted to be like in something that was designed from scratch to be like entirely AI native or enabled by what's going on instead of something that was getting built from the past.

**Daniel Lopes:** And the thing that I did before the Basecamp spinoff was helping build IFTTT, the automations platform that preceded Zapier.

**Daniel Lopes:** And I joined Marcel here.

**Daniel Lopes:** I was building a lot of these workflows that were very similar to what we actually prototyped inside of IFTTT. But when we tested with our 10 million user base, only a tiny fraction actually engaged with that, and IFTTT's goal was to be mainstream instead of being specific to businesses. We wanted it to be consumer-focused.

**Daniel Lopes:** So we ended up never shipping that.

**Daniel Lopes:** So when I joined Marcel, like, I was, like, the thesis was that we're going to build, like, these workflows and people will learn how to build them.

**Daniel Lopes:** And it's going to be, like, we can't train any person to do it.

**Daniel Lopes:** The realization is that the workflows got super complicated.

**Daniel Lopes:** All the small things in the last mile that LLMs couldn't do — a year and a half ago, it would do 70% and the other 30% was just garbage.

**Daniel Lopes:** So, and, like, covering that 30% was required a ton of complexity.

**Daniel Lopes:** And, like, those graph-based stitching together drag-and-drop stuff doesn't do justice to the complexity you need.

**Daniel Lopes:** So we ended up migrating all the stuff that Marcel and the team was trying to build.

**Daniel Lopes:** We built with local tools into just straight code base, and we ended up building a framework to create essentially coding agents through everything integrated, and it could be auto-generated, because we had to migrate 150 workflows in three weeks, essentially.

**Daniel Lopes:** And we also had to run them in super high volume, so it had to be super parallelizable.

**Daniel Lopes:** So very similar to the infrastructure we needed at IFTTT, but IFTTT, were doing one at a time, like one unit, and here we needed to do these larger units, that might run for like 20 minutes.

**Daniel Lopes:** So we ended up building on top of open source stuff, very similar to the premises we used at IFTTT. I was thinking about how to explain this, and the best thing I came up with is to walk you through the same onboarding process we use with our engineering team. We have a high-level overview, and normally there'd be a second session with pair programming on building workflows together.

**Daniel Lopes:** But I can just give you the architectural overview and maybe that will help you understand the whole thing.

**Daniel Lopes:** Let me share my screen.

**Daniel Lopes:** Let me open my Figma here.

**Daniel Lopes:** So we have a big jam with the whole thing.

**Daniel Lopes:** And it kind of covers a bit of what Marcel was doing as well because folks can sometimes not really grasp that, even though we're doing like content on the surface, under the hood is all very generalizable.

**Daniel Lopes:** So like what we cover is usually like what is our thesis?

**Daniel Lopes:** What is service as a software?

**Daniel Lopes:** Why are we doing content?

**Daniel Lopes:** And the content is one that's interesting because it was a conscious choice because it's doable and it looks easy at the surface.

**Daniel Lopes:** But when we actually start doing it professionally, you hit all these problems with consistency, accuracy, and tone. All these things are pretty hard to get to behave well. And at the same time, you've got people that will try to do it internally, and then they'll be happy to buy from somebody afterwards.

**Daniel Lopes:** And another thing, like, what's the scaling path for this?

**Daniel Lopes:** Can we build the infra, and can we build a team that's scalable?

**Daniel Lopes:** And then, like, we usually go into the technical architecture, and I walk people through all the GitHub repos and everything.

**Daniel Lopes:** But also, like, what's the staff expectation?

**Daniel Lopes:** are the teams supposed to expect from us?

**Daniel Lopes:** And, we're essentially building the team in a way that, like I was saying, I think this is, like, a race that we have, like, probably a couple of years to, like, get some get-aheads a bit.

**Daniel Lopes:** And the strategy has been to hire remote folks, but with San Francisco salary and folks that were here or folks that were, like, high-growth companies.

**Daniel Lopes:** But they do have super high expectations.

**Daniel Lopes:** So we have a team of 15 people today that we hired in just three months, and they're doing great. But essentially, the main thing we're thinking is that a year ago, Marcel and I were discussing: What are we going to do? Are we going to keep building this way? Are we going to do something in a different space? Is content the right place to be doing things?

But the main thing was always that LLMs are essentially small reasoning units that you can mix with different kinds of software. You can get natural language input and outputs that are pretty close to what somebody would do.

**Daniel Lopes:** So if you have small reasoning units like this and you can do a lot of automations like we were doing at my IFTTT days, but you have humans for critical judgment and training for the next loops, and you build a UI that's specific to that task but keep it as fast as possible — then the UI for that specific task is not the core. The core is what's under the hood. That surface layer is just to make sure people can use this new kind of user interface in the best way possible for the process. Then you can get to the experience that us programmers are getting, where you can just open Cloud Code and do a lot of things that would take many days. And then one person can be super, super productive.

**Daniel Lopes:** And our theory is like, if you do all these four things, then you can do that in pretty much any space.

**Daniel Lopes:** And content is one that we're like, we have experience with it and we know how hard it is.

**Daniel Lopes:** But essentially, like you all probably are super familiar with this.

**Daniel Lopes:** You probably thought about this a lot.

**Daniel Lopes:** But pure software is like, so hard to maintain.

**Daniel Lopes:** Just the UI side of it takes a huge amount of effort to get something that looks really great.

**Daniel Lopes:** And like, then you have to retrain the user every time you launch something, requires like a ton of maintenance.

**Daniel Lopes:** And the larger user base you get, harder it becomes to change things fast.

**Daniel Lopes:** So if you have 10 million users — Canopy, the Basecamp spinoff, has like 60,000 active users. And every couple thousand users you add is a group of folks that never use your new features. What's happening with LLMs is changing so fast that even the UI or the way you organize things has to shift almost weekly sometimes.

**Daniel Lopes:** And just doing self-serving products is going to move too slow. So that was one thing — having our own team, having our own users, and paying our own users to use our own product is a great way to get them trained all the time. But then you have the problem that pure service doesn't scale. So we asked: Can we figure out a way to scale? Can we decompose the parts that are less high leverage and figure out how to train the folks that are high leverage faster? I think the component where these two things combined could work.

**Daniel Lopes:** And that's what we've been trying to validate.

**Daniel Lopes:** And so far in the first year, I think we've done a pretty good job.

**Marcel Santilli:** But let me zoom out here super quick. I just took a quick screenshot and want to spend 60 seconds framing before we go into services software. Just on the approach you take to services software.

**Daniel Lopes:** We're going to touch that. Since we only have 30 minutes and a lot to cover, I think we'll get to that. I have examples with fine-tuning coming out of the workflows. But essentially, what we're thinking is we're going to have a bunch of vertical interfaces.

**Daniel Lopes:** In our case, vertical is content market, that's the one we chose.

**Daniel Lopes:** And then you have an AI workflow engine that's general purpose.

**Daniel Lopes:** And then you have a hybrid workforce that will interact with the AI workflow engine.

**Daniel Lopes:** And we have clients and high impact team that will use the vertical interface.

**Daniel Lopes:** So in content marketing, for example, they would be getting the reports of their content that's getting shipped.

**Daniel Lopes:** They're going to be seeing the status of their content.

**Daniel Lopes:** the...

**Daniel Lopes:** The work that's getting moved, they're going to be interacting with folks through that interface layer, but they're going to be interacting with like high leverage folks.

**Daniel Lopes:** They're going to be interacting with folks like Marcel, like our BPL growth, and like our strategists, our team of strategists we have.

**Daniel Lopes:** And those we don't expect we're going to have like 5,000 people.

**Daniel Lopes:** We might have like 200 when we're like at the $2 billion valuation, but we're not going to have like a boatload of like folks doing like that part of the work.

**Daniel Lopes:** And that happens sometimes, like sometimes throughout the year, but not all the time.

**Daniel Lopes:** And then you have the AI workflow engine.

**Daniel Lopes:** That's where like the high impact team will be helping us figure out what is the, what has to be automated and how.

**Daniel Lopes:** What is like an article outline that looks good?

**Daniel Lopes:** What does that mean?

**Daniel Lopes:** How you generate that?

**Daniel Lopes:** What's the research process for writing an article, for example?

**Daniel Lopes:** Or if you're doing sales, what is the process for like investing, like researching a lead or researching a company?

**Daniel Lopes:** So like those things are like the experts really understand that part.

**Daniel Lopes:** So they need to help.

**Daniel Lopes:** The creation of the workflows, creation of the agents, what are the evaluation metrics for that kind of agent?

**Daniel Lopes:** It's not going to be just groundness like the traditional ML evaluations have.

**Daniel Lopes:** You're going to have a specific LLM as a judge for that specific task, for example.

**Daniel Lopes:** And the experts actually know that part really well.

**Daniel Lopes:** And then the bottom part would be you still need a bunch of stuff that will be last mile or things that LLMs can never do, like choosing between or might not do for a long time, like choosing for an out of 20 images that we generate, which one has the better taste for the brand for it.

**Daniel Lopes:** And that's super hard and probably not worth doing.

**Daniel Lopes:** Or publishing things on a CMS.

**Daniel Lopes:** We don't want to integrate with every CMS on Earth and every different kind of combination that they do under the hood.

**Daniel Lopes:** So that we might still have folks doing that part.

**Daniel Lopes:** And for that last part, we're thinking that would be like a marketplace and you have maybe a rubric of the tasks.

**Daniel Lopes:** It would be very similar to like data labeling or to other kinds of marketplaces that you do for distributing.

**Daniel Lopes:** Easier, shorter timeline life cycle tests.

**Daniel Lopes:** So that's kind of like the gist of our thinking things.

**Daniel Lopes:** And like I kind of touched a little bit on why we chose content.

**Daniel Lopes:** But we're thinking it's like it's a perfect  head.

**Daniel Lopes:** It's not super easy to do, but it looks easy on the surface.

**Daniel Lopes:** So folks who underestimate it, we're not going to get a ton of like super high quality competitors at the same time, like the same way as the folks at Cursor are getting competition from Cloud Code, for example, or they're getting competition from Winsurf.

**Daniel Lopes:** In our space, are not seeing the same.

**Daniel Lopes:** Like we're getting like folks that are competing with us from agencies, for example, or internal teams, because it looks easy.

**Daniel Lopes:** It looks like you can do it with ChatGPT and then you do it for a bit and take like freaking four hours to get the article to the state that you needed.

**Daniel Lopes:** So we kind of chose that on purpose.

**Daniel Lopes:** And AI answers, they're just accelerating everything so much faster than we expected.

**Daniel Lopes:** So now if you have a catalog of like a thousand pages, you need them to be super accurate.

**Daniel Lopes:** You need them to be updated.

**Daniel Lopes:** All the time.

**Daniel Lopes:** So you need that efficiency and scalability that's hard to do.

**Daniel Lopes:** And that's exactly what we do with our engine for.

**Daniel Lopes:** So that's like, it's just, it panned out pretty well so far.

**Daniel Lopes:** Under the hood, what we have is essentially, the goal is you have like one managing editor, for example, doing like the roadmap and the client strategy for the content.

**Daniel Lopes:** And then you have AI agents executing the bulk of the work, and you have maybe humans in the loop ensuring like the quality or the last mile.

**Daniel Lopes:** And like that will, the theory is that we're going to get a ton of productivity from that.

**Daniel Lopes:** And we've been able to test that and validate quite a bit in the last few months.

**Daniel Lopes:** And let's say, for example, going a step more focused, like what does that look in real life?

**Daniel Lopes:** You have a content marketing vertical app.

**Daniel Lopes:** That's like, that's our internet.

**Daniel Lopes:** And then you have a bunch of workflows.

**Daniel Lopes:** Like one client might use maybe like 20 different workflows.

**Daniel Lopes:** Some of those.

**Daniel Lopes:** might be agentic.

**Daniel Lopes:** Some of those are sequential.

**Daniel Lopes:** They are usually like 50 lines of code at most and a ton of prompts, but everything is organized as code.

**Daniel Lopes:** And I'm going to show you a little bit.

**Daniel Lopes:** And then also like everything that runs, instead of putting the tracing and putting the logs in a bunch of different tools, we're instrumenting everything to be in the file system local.

**Daniel Lopes:** And that later we can put in an S3 and we can have like a parquet files, or we can have something like DuckDB or things like that consuming.

**Daniel Lopes:** And we built a nice user interface on top.

**Daniel Lopes:** That part was still like moving out of all these tools.

**Daniel Lopes:** Like we tested essentially everything, which has like Datadog, BrainTrust, Galileo, LengFuse is the one that we're still using.

**Daniel Lopes:** And that's just for the tracing part.

**Daniel Lopes:** And then for the evals, we tested quite a bit of things as well.

**Daniel Lopes:** We ended up just like moving everything to just be part of the same ecosystem.

**Daniel Lopes:** But the idea is have everything in one place, in one folder.

**Daniel Lopes:** So every workflow is one folder.

**Daniel Lopes:** And the decision there is that Fath folder is something that a coding agent can understand.

**Daniel Lopes:** So you have like four files at most, including the prompts.

**Daniel Lopes:** You have the function that would decide the flow of how to execute things and the logic.

**Daniel Lopes:** And you have the execution.

**Daniel Lopes:** And you also have the human feedback whenever we connect with like the human in the loop part.

**Daniel Lopes:** So like you can actually give that to a coding agent.

**Daniel Lopes:** Like even a cloud code, if it's well-instrumented enough, it will be able to suggest improvements pretty well.

**Daniel Lopes:** And the result of that, I think like we can essentially automate anything.

**Daniel Lopes:** like automating content has been what we're focused on.

**Daniel Lopes:** And like in practice, the way we're thinking is that the people part of this, like the top of the funnel people part of this, we're always going to need to have folks getting trained, folks understanding how the context of content creation happens, the strategy and all that.

**Daniel Lopes:** So like Marcel and the rest of the team, they have the AI-led growth.com, which is a community to teach folks how to be AI-native as marketers.

**Daniel Lopes:** And then the day-to-day, if we, and then we can hire folks in that community and that the folks that join, they would be like using our internal tool.

**Daniel Lopes:** That for now, it's only available to GrowthX.

**Daniel Lopes:** Maybe in the future, if we validate that the process is repeatable with other agencies and folks can do that, we might actually make that whole internet available to other agencies.

**Daniel Lopes:** But that's not the goal.

**Daniel Lopes:** The goal there is super fast.

**Daniel Lopes:** And then the last mile apart in the marketplace, that's something that we're building.

**Daniel Lopes:** Like that would be like for early next year.

**Daniel Lopes:** But essentially, the loop looks like this.

**Daniel Lopes:** So you have a workflow performing the execution.

**Daniel Lopes:** Everything's file-assisted, self-contained.

**Daniel Lopes:** Most of it is already generated.

**Daniel Lopes:** And then you have generated output would show up at the edges.

**Daniel Lopes:** So like in our vertical app.

**Daniel Lopes:** So in this case, would be like the workflows will run things, generate the result, send the data via API to the edge app.

**Daniel Lopes:** In this case, we call it Atlas, which is our internal tool.

**Daniel Lopes:** And we also have another one that we're extracting, you know, that would be a self-serving tool.

**Daniel Lopes:** That also...

**Daniel Lopes:** We're going to use a bunch of our workflows, and the team interacts with that part more, and then they were always going to have things that they have feedback about.

**Daniel Lopes:** For example, this is the example, a classic one that everybody might have seen.

**Daniel Lopes:** This is actually a managing editor for our team, and she's complaining about M-dashes.

**Daniel Lopes:** And so that's the classic one, and they've all removed M-dashes a thousand times, and that's the perfect JSON-L.

**Daniel Lopes:** to be extracted for a fine-tuned GPT module, and that's what we did here.

**Daniel Lopes:** So you can see this.

**Daniel Lopes:** Oh, no.

**Daniel Lopes:** I have it here.

**Daniel Lopes:** So you can see here the traditional GPT-4 one.

**Daniel Lopes:** So we have, I was just testing actually the fine-tuned version, and I asked it to generate an article, and you have a bunch of M-dashes.

**Daniel Lopes:** So have M-dashes here, everywhere, and even when you ask it to remove, it's still adding a bunch.

**Daniel Lopes:** But if you have the fine-tuned one, it's like a super easy to fine-tune, but just getting all the edits that the folks did automatically, then you get the, so this is the first version, where I made a blog about Steve Jobs, and you get all the M-dashes, and then the second time that I asked the M-dash, the same question, now there is none anymore.

**Daniel Lopes:** So that works for all these smaller things, and you're getting that automatically from the folks just adjusting the text editor, and I will show that how they do that.

**Daniel Lopes:** And another thing that would come from this is that they're complaining, like, then you see my other colleague here, Jason, not using certain words or citing certain sources, and that is also something that we can solve by creating, like, specific micro-agents for this task only.

**Daniel Lopes:** So, like, in the case of augment code, for example, we have, we don't M-dash, so that's part of our document that has all the context for the things that augment code can

**Daniel Lopes:** So, first, would be writing guidelines, then replace end-dashes, then reduce the number of words per hyperlink, verify technical sources.

**Daniel Lopes:** So, for augment code, would be no blogs, except if it's like no personal blogs, unless it's somebody like Karpathy or Simon Williamson or somebody that's well-known in that topic.

**Daniel Lopes:** And then you have things like also improved readability.

**Daniel Lopes:** Some of this could actually be fine-tuned, but we have this as a microagent that would take this context and will loop until it makes all the six things pass.

**Daniel Lopes:** So, like, those are the kind of things that we can do, and it's super fast to do an infrastructure we have now.

**Daniel Lopes:** So, essentially, like, 20 minutes, you create one, and you deploy.

**Daniel Lopes:** But from scratch, or using tools like AIOps or the other stuff, or any, and it was taking forever for us, we ended up doing that out of necessity.

**Daniel Lopes:** The stack looks like this today.

**Daniel Lopes:** We have this internal tool called Atlas. It has insights and analytics. It has a knowledge base. The knowledge base uses a Neo4j graph database with vector retrieval. We started with graph database retrieval, but it's too slow. So we ended up switching to light retrieval, which is a variation of it. So it's a graph database tied with vector retrieval.

**Daniel Lopes:** And we tested a bunch of different things in the past as well.

**Daniel Lopes:** We tested just like regular VV8 with like different types of chunk, you know, that ended up with this.

**Daniel Lopes:** So far, it's working well.

**Daniel Lopes:** But this is specific to growthx.

**Daniel Lopes:** So things like the way we chunk, the way we do the processing of the documents is like, it's specific to content marketing.

**Daniel Lopes:** It's not general purpose.

**Daniel Lopes:** So it's inside of our vertical.

**Daniel Lopes:** And then we have a content inventory, which is a place that will like scrape your entire website as a client and judge the pages, read, and try to understand how they could be improved.

**Daniel Lopes:** And so that will like understand your website, find opportunities, and also help track all the tasks that are moving along.

**Daniel Lopes:** And we have an AI assistant tax editor as well.

**Daniel Lopes:** Folks would spend so much time just copying things out.

**Daniel Lopes:** Go to the platform, paste in Google Docs or paste into chat, GPT, and tweaking things.

**Daniel Lopes:** And we ended up building like a cursor-like experience that you have the context of everything.

**Daniel Lopes:** You have access to the knowledge base, but it's inside of the platform.

**Daniel Lopes:** So you can say, adjust to my writing guidelines.

**Daniel Lopes:** We'll be able to know, okay, this is from the context from this client.

**Daniel Lopes:** And we have a set of documents that are handcrafted by the team, like the one I just showed you.

**Daniel Lopes:** So that's like a proofreader for Augment is different than a proofreader for a taxes company, for example.

**Daniel Lopes:** And then we also have all the AI pipelines.

**Daniel Lopes:** And the AI pipelines is where we stitch all the workflows together.

**Daniel Lopes:** And each workflow is this like chunks of code with a ton of problems.

**Daniel Lopes:** And the API calls you a separate service.

**Daniel Lopes:** And so that's our internal tool.

**Daniel Lopes:** And from that, like the goal there is to move super fast.

**Daniel Lopes:** So we hire the people fast.

**Daniel Lopes:** And we're not expecting the same level of like critical design or like the pull request review cycles and everything that you or SLO, SLA, that you would have for like a self-serving product.

**Daniel Lopes:** So we can move super fast there, but whenever we see things that are reusable over and over, then we can extract.

**Daniel Lopes:** So we're extracting a new product called Check.ai that will be our AI visibility tool, and that will be like self-serving.

**Daniel Lopes:** And so that's our internal stuff.

**Daniel Lopes:** And then our workflow engine is essentially a REST API that has our own internal framework, has a runtime for the needs we have, the distributed needs we have.

**Daniel Lopes:** And we're building a newer version of our IDE and the studio UI.

**Daniel Lopes:** And I can show you all the stuff.

**Daniel Lopes:** And like next year, end of this year, we're going to do the internal version for our marketplace to move all of our contractors to the marketplace.

**Daniel Lopes:** And then the next phase will be maybe opening up for other companies to use.

**Daniel Lopes:** And essentially, then I have a bunch of like user interface and stuff like that that I'll show to the folks.

**Daniel Lopes:** But this is just a little bit to show how the creation of the workflows go.

**Daniel Lopes:** So it's essentially there's a TypeScript framework prompting code.

**Daniel Lopes:** Everything is self-contained into a folder.

**Daniel Lopes:** So everything about the workflow is the folder of like four files-ish.

**Daniel Lopes:** The docs part is already generated, and it's generated mostly for AI to understand it.

**Daniel Lopes:** Building trace and evals, and enterprise-grade runtime under the hood.

**Daniel Lopes:** And it's everything open source that we depend on.

**Daniel Lopes:** And it usually goes like this.

**Daniel Lopes:** You install the NPM package, and you start the new projects.

**Daniel Lopes:** So in this case, would like output.space new space growthx, and then I can generate a workflow.

**Daniel Lopes:** In this case, let's say I'm generating a workflow called article draft, and I pass like a markdown file with the plan.

**Daniel Lopes:** Or I just paste the plan that would work as well.

**Daniel Lopes:** And the plan would usually be like a plain text, like natural language like this.

**Daniel Lopes:** Like I need an agentic React workflow that will take a topic, an outline, and write guidelines, and should use the Atlas research.

**Daniel Lopes:** So it knows about the Atlas APIs under the hood.

**Daniel Lopes:** So that's, it knows it can tap.

**Daniel Lopes:** That's for research, and you can run in exploration mode, it'll come up with its own questions.

**Daniel Lopes:** I could also pass questions as well, but, and then for the evaluation part, do like max 10 iterations, do a continuous self-reflection, LLM as a judge for four different requirements, like grounding is on the research, direction, acceptance, writing guidelines, and use clause four for everything, and the code will look like this.

**Daniel Lopes:** This is an example one, this is a simpler version, but just to give you like an idea of how the folder looks like, so it's a folder with prompts, so you have a version of the prompts as well, prompts are essentially YAML with a front matter on top, and then you have index steps, and you have the types, types will help understand which APIs can be called and what you expect out of it, and for the agentic one, you look more like this.

**Daniel Lopes:** So we have for the article one that I was just mentioning, you have the steps with the prompts, and you have the prompts for evaluations as well for self-elementation.

**Daniel Lopes:** As a judge, and then you have the usual steps, and then going a little bit deeper, when you run things, you would also get a data folder with the scenarios that you can use to rerun yourself for testing locally, but you also get the production data that you can sync from the run, and the workflow would actually look like, this is actually showing how the, this part doesn't work yet, this part is like we're finishing the API to pause the workflows, and wait for him to review, but the steps, I can show you all the workflows in production, but essentially that's the gist of the architecture, and I can also like talk a little bit about the team that we have, so on the product side, it's mostly product engineers and design engineers, and they're all like former founders, or people that are, been early stage at different companies, and want to be back at building, so we have, everybody has about like 20, like,

**Daniel Lopes:** 10 plus years of experience coming from a bunch of different places.

**Daniel Lopes:** And the stack we use there is Rails and React for the front end, because that's a really good monolith for you to move fast.

**Daniel Lopes:** But then on the runtime layer and the framework, that's distributed systems architecture.

**Daniel Lopes:** So we have folks from Heroku and HashiCorp, early stage HashiCorp.

**Daniel Lopes:** We have folks that did the brand monitoring part of Meltwater, really critical part of their infrastructure.

**Daniel Lopes:** a super high-volume distributed system, and folks from nearby as well.

**Daniel Lopes:** And we're starting to build the team for the help us create self-optimized prompts and creating workflows automatically.

**Daniel Lopes:** And then we also have the four deploy engineers.

**Daniel Lopes:** And they have a project manager there, so Stevie is a project manager, but she's also an engineer.

**Daniel Lopes:** And then we have folks that came from Aerox, came from ClickUp, that has done a bunch of growth-related automations.

**Daniel Lopes:** products Mobileівules.

**Daniel Lopes:** on echo想 Галини

**Daniel Lopes:** And I can show you some of the stuff we have.

**Daniel Lopes:** I'm almost out of time.

**Daniel Lopes:** Sorry.

**Marcel Santilli:** And then, like, this is our internal tool.

**Marcel Santilli:** I'll show you a bit of augment.

**Felipe:** And you know how to stop on my end.

**Felipe:** Please talk as much as you want.

**Bo Wang:** And I'm enjoying this a little bit.

**Bo Wang:** I have time, too.

**Daniel Lopes:** OK, cool.

**Daniel Lopes:** Yeah, so we have, like, this is our internal platform.

**Daniel Lopes:** You have to have a growthx account to see it.

**Daniel Lopes:** And, like, let's say augment, for example, the dashboard is not showing the real data, but the other stuff is actually real.

**Daniel Lopes:** So, like, we have different kinds of clients.

**Daniel Lopes:** So we've been, like, trying to decide what is our ICP and what should we do.

**Daniel Lopes:** And we've been landing on a bunch of different, like, client-related traits or, like,-related traits.

**Daniel Lopes:** But the stuff that I actually care from the technical side is the level of complexity of their content.

**Daniel Lopes:** So there's a spectrum of complexity that goes from, like, it's easy to do and ChatGPT can do it.

**Daniel Lopes:** So, like, that's too easy.

**Daniel Lopes:** That's great.

**Daniel Lopes:** If you can get that and they want to pay us, that's fine.

**Daniel Lopes:** We'll take it.

**Daniel Lopes:** And then the better one would be somebody that's like augmented, where it's easy, but it's not as easy that you can just scrape the whole internet.

**Daniel Lopes:** You still don't want to have medium from somebody that has a one post or a personal blog post or stuff from hacker news.

**Daniel Lopes:** So you need some level of accuracy and trust at the source level.

**Daniel Lopes:** And then you have medium complexity.

**Daniel Lopes:** would be like town.

**Daniel Lopes:** Town is a taxes-related topic.

**Daniel Lopes:** So it has to be like you have to fetch only data from IRS.

**Daniel Lopes:** You only have to fetch data from high trust places.

**Daniel Lopes:** And then you have biologica.

**Daniel Lopes:** Biologica is like in the realm of medical field.

**Daniel Lopes:** So you have, they will be making claims about like ingredients.

**Daniel Lopes:** You can't prescribe things.

**Daniel Lopes:** You have like the nuance of the topics that are like really important.

**Daniel Lopes:** So those are the three layers that if they check all the boxes for like the traits at the behavioral level that we like and they.

**Daniel Lopes:** If fit in this spectrum, then we're good.

**Daniel Lopes:** If there are things that are first impossible to do, or that takes so much effort to do, like legal, for example, we had a few clients that would have to do like JIRA tickets inside of their environment for the lawyers to review.

**Daniel Lopes:** Like that, you're never going to publish enough to get value.

**Daniel Lopes:** So that we prefer not to do.

**Daniel Lopes:** But that's the spectrum.

**Daniel Lopes:** So like for Augment, for example, for them, we have like a list of products and services.

**Daniel Lopes:** that's a fact.

**Daniel Lopes:** And then we have a bunch of things that are guidelines as well.

**Daniel Lopes:** And we have templates.

**Daniel Lopes:** So those documents are handcrafted.

**Daniel Lopes:** The folks will like interview their users and understand what they do and what they care about.

**Daniel Lopes:** And then we'll create these guidelines, for example.

**Daniel Lopes:** And they might look like this.

**Daniel Lopes:** So it be like an engineering manager that's more interested in onboarding and like frustration of things not getting shipped or like code reviews taking too long to be unlocked.

**Daniel Lopes:** And then you have staff engineers with like similar pains.

**Daniel Lopes:** So we come up with this document and this document is used throughout.

**Daniel Lopes:** we're to about right.

**Daniel Lopes:** the project.

**Daniel Lopes:** So

**Marcel Santilli:** I think a super quick, underappreciated here is like, you all might be using like Cloud Code or Augment or Cursor, you know, like, and you might have great documentation, great code base with all this stuff, like knowledge workers don't have that.

**Marcel Santilli:** So you're coming in inside of these companies, they don't have any well-written documents on anything at all, you know, even a public company like Sentinel One, so a lot of the process is getting the right inputs to get to this point, even, you know, so it might look like just a plain document, but the amount of inputs that it takes to get to even this level of alignment is super, super critical.

**Daniel Lopes:** Yeah, so then, and then we also do a lot of stuff that we have examples, like from real conversations, and that will just help with the prompt engineering part of things, and then we have, in the case of Augment, we also want to do, sometimes we might want to fetch data from different places, so we have our internal knowledge base, the knowledge base is a wrapper around all the resources.

**Daniel Lopes:** So in the research we do might use, for a harder client, it might use EXA or Tavoli and run the research that might cost like $2 or $3 per topic, but we don't want to lose that, so we store all that data, and the clients we also sometimes do those internal documents, so we have this knowledge base, and this knowledge base is the implementation of life reg that I was talking about, and in the case of augment, we have a lot of stuff around like program topics, so you're going to have like a high cluster around something like Django, for example, and then, so like the reg will be based on top of this, and then if it doesn't find, we can like add more, more sources and more entities, and that can be manually, or that can be triggered by an automated workflow, and we also have an assistant internally that's similar to cloud projects, but with all your artifacts, the documents that I was showing before are already there, and when you have this thing open, you're

**Daniel Lopes:** We get, like, all of our editors, our text, have something similar to a cursor-like experience that you can select here.

**Daniel Lopes:** And the sidebar, we have the context with all the documents and the knowledge base.

**Daniel Lopes:** So you have this workspace, like, preloaded for you.

**Daniel Lopes:** And that's just, like, the general stuff.

**Daniel Lopes:** And then we have the, we have all the things about, like, the pages and opportunities, scraping your website, tracking the progress.

**Daniel Lopes:** And then we have the pipelines that stitch together the workflows.

**Daniel Lopes:** And in some tools, would see, like, Clay would have an interface like this.

**Daniel Lopes:** Some other tools, you have an interface like this.

**Daniel Lopes:** But in our case, this is because the team that's setting up the workspaces, they are for the deploy engineers.

**Daniel Lopes:** We actually have a YAML.

**Daniel Lopes:** So, and you define all the params, you define all the spec for how you want to stitch things together.

**Daniel Lopes:** So, in this case, it's going to start with, like, a form, and the form might have a UI of a text editor or a text editor.

**Daniel Lopes:** But the stitching together of the workflows, the steps, are functions.

**Daniel Lopes:** And then you're just defining what are the params you can pass to the functions.

**Daniel Lopes:** Like, you would never do that in a self-serving product, but in internal tool you can.

**Daniel Lopes:** So that saves those, like, months of building, like, big graph of stitching things together, like drag and drop and all that.

**Daniel Lopes:** And it's way more powerful.

**Daniel Lopes:** At the end, you get something like this.

**Daniel Lopes:** So you get each step that you see here on the left.

**Daniel Lopes:** It's a row, a column on that grid that I showed you.

**Daniel Lopes:** And now I'm seeing a row of that grid.

**Daniel Lopes:** And it starts with a research topic that will take in an input.

**Daniel Lopes:** So those are the params.

**Daniel Lopes:** In this case, you use Tably as a research tool.

**Daniel Lopes:** And under the hood, that will run an AI workflow from our environment.

**Daniel Lopes:** So this is the inspecting tool on top of our runtime.

**Daniel Lopes:** And this is all the steps that it took.

**Daniel Lopes:** And this is actually if I switch to JSON mode, and I can see the params that it took.

**Daniel Lopes:** And you can see the results.

**Daniel Lopes:** And I can also...

**Daniel Lopes:** can also...

**Daniel Lopes:** See which part of the code that came from.

**Daniel Lopes:** So this workflow is our supervisor agent that will spin off a bunch of executor researchers and perform maybe like 20 to 30 questions in parallel, triggering X or proplex and then combining everything at the end.

**Daniel Lopes:** So you ended up with like getting a pretty decent result stored in the knowledge base here.

**Daniel Lopes:** And then an article out of this would be another agent, similar idea.

**Daniel Lopes:** So this one we have taking the data, taking the research data, the topic, and a few other things.

**Daniel Lopes:** We generate the first pass and then we'll like evaluate for groundness.

**Daniel Lopes:** We'll like give itself feedback, verify if the claims match the context documents we shared, and then look for potential issues.

**Daniel Lopes:** And then it will clear depending on the threshold.

**Daniel Lopes:** So there's usually acceptable, great, or bad, but it would do that grading just to help us see internally. We will unlock a certain amount of iterations here.

**Daniel Lopes:** So at the end, we ended up with an article that takes sometimes like 10 minutes to finish.

**Marcel Santilli:** This one is actually one minute, 10 minutes to research, depending on the complexity of the client.

**Marcel Santilli:** People were executing our workflows early on, our employees, right, like delivering the service.

**Marcel Santilli:** Then they were copying and pasting a bunch of stuff over to a chat GPT or a or a Google Doc or a Notion to do a little bit of editing.

**Marcel Santilli:** You know, so it's almost like they're taking the output, then they were throwing it into chat GPT, tweaking a little bit, giving it  prompts, and then taking the output of that and putting it in Google Doc, tweaking it a little bit more, and then bringing it back into chat GPT.

**Marcel Santilli:** You know, like, it's like, this is silly, but also we're losing all that knowledge because we're not tracking all that activity.

**Marcel Santilli:** So having everything here — an editor, a context-aware assistant, as well as an execution layer that is based on the code that can run massive executions with tool calling and knowledge retrieval — it allows us to learn from the whole interaction.

**Daniel Lopes:** Exactly.

**Daniel Lopes:** So just to show you the final pipeline here, the last thing we do is a fact checker. For example, we have about 200 workflows that we can stitch together or create for customers. This one would split the article into chunks and then research the statements again. It would extract small passages and verify them. For each passage, it generates questions that should be searched and the confidence level — like whether it thinks it's false. Then it will suggest a rewrite. Sometimes it's very nuanced.

**Daniel Lopes:** And one thing we learned is if we search something with Excel or tabular data via Perplexity, you should invert that and do the fact check with another source, so you get a little more validation.

**Daniel Lopes:** And then we also do like a bunch of things on top of non-text-based APIs too.

**Daniel Lopes:** So for augment, like would you?

**Daniel Lopes:** Generate all their images.

**Daniel Lopes:** So we have a bunch of stuff on top of the GPT image that takes in like a bunch of reference images and edit things.

**Daniel Lopes:** Same thing for infographics, but it has to match the design language of the company.

**Daniel Lopes:** So that's something that we spend quite a bit of time figuring out.

**Daniel Lopes:** And that's like the easier client.

**Daniel Lopes:** And then the more complicated clients like Tao and Biologica.

**Daniel Lopes:** Biologica, we might create custom agents just for them.

**Daniel Lopes:** And that's the case for, let's say, an expert review.

**Daniel Lopes:** So they might get so many small things as a doctor or like a practitioner reviewing your article that we took all their comments and created a custom agent that will do evaluations to see if it's actually doing something similar that that person will do.

**Daniel Lopes:** So we'll split the article into distractions and we'll like look for oversimplified claims or oversimplified claims is kind of the classic one for their case.

**Daniel Lopes:** And then it will suggest that we auto-optimize that agent. So that's what the forward deploy folks would do.

**Daniel Lopes:** Like, look at their harder clients.

**Daniel Lopes:** Can we do that out of the box with our agents?

**Daniel Lopes:** If not, can we stretch the ones we have?

**Daniel Lopes:** If not, minimum, need to create a custom one.

**Marcel Santilli:** And that's an example.

**Marcel Santilli:** So we had done multiple deep dives, including their chief medical officer.

**Marcel Santilli:** And then we built a bunch of contacts and artifacts.

**Marcel Santilli:** And then you get to the last mile, the chief medical officer reviews the piece of content and say, listically, great.

**Marcel Santilli:** Everything is great.

**Marcel Santilli:** But then she starts adding all these comments.

**Marcel Santilli:** They're nuanced medical claims.

**Marcel Santilli:** Right?

**Marcel Santilli:** It's like, hey, this is oversimplifying the relationship between hormones and this other receptor, blah, blah, blah.

**Marcel Santilli:** Things that would be like nearly impossible for us to do.

**Marcel Santilli:** So that's an example of where if it's not deployed as a service, the tool would have failed.

**Marcel Santilli:** Even no matter how great the tool is, it would have failed because you got to iterate to get closer and closer.

**Marcel Santilli:** So similar to autonomous vehicle, right?

**Marcel Santilli:** Like Zooks or whatever.

**Marcel Santilli:** It's like, hey, it's kind of like an incremental process to achieve.

**Daniel Lopes:** Great outputs.

**Daniel Lopes:** Yeah, and just to wrap up, one other thing that we have that we don't show usually at folks is that we have, because we control the whole space, then we can have a lot of visibility on everything that's happening.

**Daniel Lopes:** So that was one of the challenges that we had with using someone else's tools or using out-of-shelf stuff.

**Daniel Lopes:** You just can't control what's going on, and you don't get enough data on all the input and outputs of things.

**Daniel Lopes:** So we have, like, our own internal admin that you can see what's the work that's getting done at that client, how many executions are happening, who's doing most of the work, and then you can go at a deeper level.

**Daniel Lopes:** And then we also know who are the folks that are the best, and, like, editing or, like, writing, and then we can take their challenges and optimize and automate that stuff.

**Daniel Lopes:** So, like, that's kind of the gist of the whole set.

**Daniel Lopes:** I hope it helps.

**Daniel Lopes:** It usually takes, like, an hour and a half, and, like, I'm trying to compress the whole thing in, like, 30 minutes.

**Daniel Lopes:** But I don't want to take you all on Saturday.

**Daniel Lopes:** I hope it

**Felipe:** This is fascinating.

**Felipe:** I have a bunch of questions, topic to touch.

**Daniel Lopes:** I hope that's okay.

**Daniel Lopes:** Yeah.

**Felipe:** Okay.

**Felipe:** So first of all, congratulations.

**Felipe:** This is pretty sweet.

**Felipe:** I really love the idea and the signal that you have about with coding agents, things like Courser.

**Felipe:** I can understand that a lot of the design was inspired to the functional or unit components that you have in the domain.

**Felipe:** And a lot of the agents are designed in order to fill those gaps.

**Felipe:** So I see a lot of, I understand the intention of what you built, and I understand why it could deliver value.

**Felipe:** So I'm going to try to tackle questions in the directions that I have more concern.

**Felipe:** Yeah.

**Felipe:** And it's about evaluation and scalability.

**Felipe:** So those are the things that I would like to understand better.

**Felipe:** So in the first direction, sorry, let me just grab my notes.

**Felipe:** A lot of the advantages of Courser.

**Felipe:** Another of team of type of engines is that you have, you can ask them to create unit tests and you will have unit tests running accordingly in order to move the agent to the next step.

**Felipe:** The equivalent that you are doing here is LLM as a judge, it's kind of a blend of unit testing.

**Felipe:** So LLM as a judge at this point is still quite dependent of the prompts that you have.

**Felipe:** So there is a large degree of instability in LLMs as a judge.

**Felipe:** And also there is this problem of alignment with the human.

**Felipe:** Like LLM as a judge doesn't necessarily have a good alignment with the human.

**Felipe:** So as you think of LLM as a judge as a unit testing, how do you go about scaling the robustness of the LLM as a judge to have alignment with humans?

**Daniel Lopes:** Yeah, we're thinking it in three levels.

**Daniel Lopes:** Like as unit test would be one, and then the second one would be like, so let's say unit test in traditional dev mode would be like you run that locally or before it's deployed, or you run that in your CI.

**Daniel Lopes:** So we're thinking LLM as a judge can do some of that, and it will be helpful, especially for the.

**Daniel Lopes:** Edge cases, like prompt injections or things like the M-dashes, for example, that kind of stuff.

**Daniel Lopes:** And then you have the control flow, which is kind of the stuff that those agents are doing.

**Daniel Lopes:** And then for those, I think we can do like, as in like, it will loop.

**Daniel Lopes:** And is it good enough?

**Daniel Lopes:** And it's never going to be like really precise.

**Daniel Lopes:** And so like we're thinking like just optimizing enough that folks are not catching the easy things, that would optimize a ton of time.

**Daniel Lopes:** So it would be like, if this is below a certain threshold, and then we spend a ton of time like putting the prompt for just getting close enough, would be, it's all how we're thinking about just creating the agents to do that and customizing the prompts for those microagents.

**Daniel Lopes:** And then the second part would be for the critical tasks, then we should pause.

**Daniel Lopes:** So, and then we should send to humans for review, either in the loop of the agent, and then we were building the task hub that will receive all the requests from the agent.

**Daniel Lopes:** And folks on our team, from our CM layer, content manager layer, they will accept or edit and unlock that agent to continue working.

**Daniel Lopes:** Because there are things that are like, for example, right before publishing, we want folks to review the whole thing.

**Daniel Lopes:** We want folks to see which part of the LLM as a judge failed, which part of the fact checks failed, which part of the image generation failed.

**Daniel Lopes:** So that part will pause and maybe we'll wait for like 48 hours.

**Daniel Lopes:** So we're thinking like more like a reduction of the latency that folks have or like the inefficiencies that we have than a foolproof thing.

**Daniel Lopes:** And that's kind of like an advantage that we have that we don't have any users like using the product.

**Daniel Lopes:** It's our employees.

**Daniel Lopes:** So if it takes like 20 minutes to run because it's looping a bunch of times, or if it's because it's waiting a couple of days to be unlocked, that's not a problem.

**Daniel Lopes:** And at the end, like it would generate all the tracing.

**Daniel Lopes:** data that we can either have prompts auto-optimized based on the things that folks flag, this is bad, and we're planning to have the whole thing be self-contained, so we can probably auto-generate different PRs and suggest, hey, folks are changing this often, look at this prompt, or try to inject this example here as one of the exemplars for this prompt.

**Daniel Lopes:** Or another way would be like, this is a common change, you can extract this data for a JSON-L that you could fine-tune, but we don't expect it to be like completely 100%, especially in our space, I think it's going to be so nuanced, the prompts for ILM as a digital work, that it's going to be part of the, has to be part of the framework, I think, as like generating that and helping folks at it, and even have an IDE suggesting how to do it, you know, well.

**Felipe:** Yeah, like, that makes sense, like, I, I can foresee the need of human in the loop for certain

**Felipe:** You also have the variants coming from the LLMs changing all the time, or even just if they are using tools like search, they will bring different type of quality of content.

**Felipe:** like, I do see the need of something like that.

**Felipe:** So, but then that creates a, what is the word that I'm looking for?

**Felipe:** A point that the applications will, every time that you have these pipelines, the more complex they are, the more people they will require to be human in the loop.

**Felipe:** So, like, there is this scalability problem that you will have where you need to introduce commands all the time.

**Felipe:** I've seen the marketplace being one attempt to the solution of that or the strategy that you are planning on use.

**Felipe:** So, like, can you tell me a little bit more about how that strategy works?

**Felipe:** Because you need to educate the people.

**Felipe:** You are basically creating a new segment of the market in order to need to be people specializing in this thing in order to scale it.

**Felipe:** So, can you tell me a little bit more about it?

**Daniel Lopes:** Yeah, that kind of overlaps with Marcel's experience.

**Daniel Lopes:** about it the comments.

**Daniel Lopes:** And why are you thinking about a marketplace there?

**Marcel Santilli:** Yeah, so there's kind of a couple of things, I'll start at a high level maybe, that could be relevant here.

**Marcel Santilli:** So the first thing is my whole career, I was just talking to David and Richa earlier too, and it's like, my whole career, one of my cheats was having freelancer networks.

**Marcel Santilli:** And I was able to just create a group of people that I was just like, oh my God, these are my superpowers, right?

**Marcel Santilli:** They would just get work done super quickly, right?

**Marcel Santilli:** And then most recently, was building these AI workflows that replicate my thought processes.

**Marcel Santilli:** So those are my thinking blueprints that would enable me to be in the loop with those people without me actually needing to be in the loop because my thoughts were there.

**Marcel Santilli:** My source code was there, my thought processes were there, right?

**Marcel Santilli:** And so those are kind of like the two hacks of my career that kind of like, you know, like help us be successful.

**Marcel Santilli:** And so, so then now, like, if you look at like, pretend we don't exist.

**Marcel Santilli:** Like,

**Marcel Santilli:** What are choices for a company?

**Marcel Santilli:** They didn't have to go hire a bunch of engineers and go stitch together a bunch of AI workflows and bags and borrow engineering time if you're a marketer or whatever, right?

**Marcel Santilli:** And you still need the expert to create the expert process.

**Marcel Santilli:** And they need to then go into an Upwork-like system, right?

**Marcel Santilli:** Because there's no other systems out there that are an expert layer as an API, right?

**Marcel Santilli:** And then go find people that are AI native and then figure out how to delegate the unit of work to them that works with this.

**Marcel Santilli:** And that's just, like, not realistic, right?

**Marcel Santilli:** Like, no company is going to do those two things, essentially, like, the same way, right?

**Marcel Santilli:** And so what we're trying to do is kind of like this interface.

**Marcel Santilli:** But then the reason we're trying to pick the right and be very intentional about the right primitives is because if the primitives in code and coding agents are really good and you have the activities and you have the interactions, then the interventions can actually inform the V2 of the next loop, right?

**Marcel Santilli:** And then over time, the goal is, like, almost...

**Marcel Santilli:** It's like an A-B test platform, right, where a coding agent can say, you know what, based on all these activities and the outputs and also the signals that I'm learning, like traffic, engagement, and things like that, let me try five different paths here, and let me select three, and then let me surfer these three to an L1 intervention, and the L1 intervention might pick the best one, and then an L2 might pick if the thought process of the L1 was actually good, you know?

**Marcel Santilli:** And so now it's like preference data as well, right?

**Marcel Santilli:** So over time, like maybe starts as like really complex process data that has to be more deterministic workflows with a lot of prompts, but then over time as you gain confidence, I think you can collapse it, and then over time the reviews and the interventions can take different shapes, you know?

**Marcel Santilli:** And so the delta between, I think, a company like Surge, which is our biggest customer, and what they're doing with expert data to train these models is that they're generating amazing expert data to train a model that then they hope someone will use it to actually do the work.

**Marcel Santilli:** We're getting paid to do the work, and

**Marcel Santilli:** And the messy middle byproduct is amazing data that we think will help create like positive feedback loops.

**Marcel Santilli:** You know, I don't know if that helps a little bit.

**Daniel Lopes:** I think like we're always going to have the challenge at the top.

**Daniel Lopes:** Like I think we have two layers.

**Daniel Lopes:** So we have like a high leverage folks that will require understanding strategy, understanding content as a whole, understanding the companies.

**Daniel Lopes:** That part, it's going to be hard to scale.

**Daniel Lopes:** So that was what we're solving with like the community training that.

**Daniel Lopes:** The bottom part, it's already happening for us.

**Daniel Lopes:** So like we started with a bunch of sequential workflows and like orders, like more steps.

**Daniel Lopes:** And then over time, we're able to like look at all the examples of things that they did and compressed in those agentic evaluation-based loops, like React agents.

**Daniel Lopes:** And it takes 25 minutes to complete an article, but it's almost one shot now.

**Daniel Lopes:** And they would just tweak little things.

**Daniel Lopes:** And I think the next pass will be like even less.

**Daniel Lopes:** So like just for that already worked, but I think we really have to pick one area.

**Daniel Lopes:** So that's why.

**Daniel Lopes:** I really like picking content marketing first, and this spectrum of content, because then we can go super narrow, and we can maybe hire 100 people, and have them be part-time, or contractors, and train them a little bit on just that part, and that is easy for us to do.

**Daniel Lopes:** So we have a bunch of hiring automations as well, so we have a lot of workflows for our recruits.

**Bo Wang:** I have a question similar to this.

**Bo Wang:** Is this human activity actually the biggest cost for each client, in terms of the components?

**Daniel Lopes:** No, not really. Marcel, you can cover that if you want, but the pre-deploy phase with engineers is maybe a day or two at most, on the harder spectrum of complexity. We often combine a bunch of complaints or challenges, and that might be a project that takes a week or two for them to adjust, create a new workflow, create a new version of the agents, and validate.

**Daniel Lopes:** But a specific thing to a client is very rare.

**Daniel Lopes:** And it usually will be like just integration of their CMS or like some specific custom workflows for the harder clients.

**Daniel Lopes:** And then we have the forward deploy part that is at the marketing and the content marketing part.

**Daniel Lopes:** That is the part that we do like a strategy sprint first, and that will be charged separate.

**Daniel Lopes:** And that's like up to eight weeks.

**Daniel Lopes:** And that is essentially account set up, workspace set up, knowledge base warming up, interviews of the client, coming up with the content strategy.

**Bo Wang:** So that part is expensive.

**Bo Wang:** That part we charge separate.

**Daniel Lopes:** That's a 30K contract.

**Marcel Santilli:** And like the way we think about like the human layer or the expert layer, there's a couple of different aspects to it.

**Marcel Santilli:** So one, there's strategy that's like shaping the strategy, understanding the business.

**Marcel Santilli:** Then there's process architecture. You're shaping the process. Our chief content officer ran TechCrunch for 10 years. There's a lot of processes in his mind. Those are the kinds of things that are really, really not like an average person you'd get off the street, right?

**Marcel Santilli:** And then you have an input calibration, which is like actually getting inputs from people.

**Marcel Santilli:** Right now, we depend on these forward deploy experts, but over time, you can do voice agents.

**Marcel Santilli:** There's a lot of different ways to get inputs.

**Marcel Santilli:** It's just right now, like you need to get the right inputs and ask people questions about their business and ingest their docs and things like that.

**Marcel Santilli:** And then you have output bar raisers.

**Marcel Santilli:** So think of it as like guiding the process along and improving the outputs and guaranteeing the outputs are good or sending it back.

**Marcel Santilli:** And then the last part is just last mile execution.

**Marcel Santilli:** So, you know, you might be 99.9% there, but there might be a little thing here that doesn't make sense to spend a month building an automation, you know, that a last mile execution will solve.

**Marcel Santilli:** Like just like a, you know, autonomous vehicle, there's still some humans that will take over in the very rare events that the car stops, right?

**Marcel Santilli:** Like, or they don't know what to do.

**Marcel Santilli:** And so that's kind of how we think about it.

**Marcel Santilli:** And over time, we're just constantly making sure we're delivering the best outputs.

**Marcel Santilli:** Outcomes, while also making this engine higher leverage and more efficient as well, you know.

**Bo Wang:** Yeah, but if you break down the cost for each client, which one is the biggest one, and which one is more grown linearly with per client, and which one is more fixed cost?

**Marcel Santilli:** Per client or overall?

**Marcel Santilli:** Per client.

**Marcel Santilli:** Per client.

**Marcel Santilli:** Per it varies, like blended, we're about like 70, 72% gross margin right now, and compute is only 3% of that, like 20-something percent, you know, but it's starting to kind of shift a little bit more, and it's getting more efficient, and I would say it started as almost kind of like a pyramid where you have a lot more of the production people at the bottom, and relatively fewer strategists per client, and I think it's going to kind of flip where the production and last mile execution will be more of a marketplace and fewer humans need it, but more specialized humans for specific tasks, like a, you know, a domain expert or an accountant.

**Marcel Santilli:** A dentist, a doctor, right?

**Marcel Santilli:** And then more strategies relative to, not overall, but like in relation to how many you need as executions.

**Marcel Santilli:** And then those strategies, though, can handle a bigger set of accounts.

**Marcel Santilli:** And so I would say, like, Augment Code is an example of the record, obviously.

**Marcel Santilli:** You know, they're paying us $50,000 for four different work streams.

**Marcel Santilli:** And we're, you know, their margin is well above 80%, actually, right now, because we've done so much good work on everything we're doing that we have one editor, essentially, Marisol, who also manages a few other accounts.

**Marcel Santilli:** And the strategist on it is actually focused on several other accounts.

**Marcel Santilli:** And so it's like very few humans, you know, and so it really depends.

**Marcel Santilli:** It's just like, right now, we're not at the phase of the company where we're trying to, like, micromanage for efficiency.

**Marcel Santilli:** We're trying to, you know, first make sure we're delivering the right value and learning from it and getting the right signals, you know, but obviously, like, we want to continue to build leverage.

**Bo Wang:** Every single day, you know?

**Bo Wang:** Yeah.

**Bo Wang:** I see your plan for 2025, expanding plan to 2027.

**Bo Wang:** You are expecting five times customers over the next few years.

**Bo Wang:** I just want to know that from technology or operation perspective, what's your biggest bottleneck you want to solve for the next two years?

**Marcel Santilli:** Two years?

**Bo Wang:** In the two years horizon?

**Bo Wang:** Yeah, because for the two years horizon, think you are expecting five times customers.

**Bo Wang:** I just want to see what's your biggest challenge in terms of technology as well as operation that you want to solve.

**Daniel Lopes:** Yeah, think the biggest challenge for us is, like, we are less concerned.

**Daniel Lopes:** It's crazy.

**Daniel Lopes:** the things are getting so cheap so fast that initially I was expecting that each article would cost, like, maybe $50 or something.

**Daniel Lopes:** If you did a lot of iterations and you did a lot of research and you consumed a lot of reg.

**Daniel Lopes:** But in reality, it's, like, maybe five bucks at most.

**Daniel Lopes:** So, like, the bad part is...

**Daniel Lopes:** Not being a problem.

**Daniel Lopes:** I think we definitely will have to spend quite a bit with things like fine tuning and custom things for specific tasks, small models for specific tasks.

**Daniel Lopes:** But the thing that's actually hard for us today is that layer of the vertical part where you have to, the vertical app that you have to like build for the person's way of working.

**Daniel Lopes:** So like, for example, folks would be like setting up Looker Studio and Google Analytics for every client.

**Daniel Lopes:** Okay, so now we have to build like, that takes them like every day for every new client.

**Daniel Lopes:** So let's build a micro version of that inside of the product.

**Daniel Lopes:** And if you don't check it on a regular, we know they are not doing their job.

**Daniel Lopes:** So like that took us two to three weeks to build.

**Daniel Lopes:** So like we're building all these little things and they're trying to do like as fast as possible.

**Daniel Lopes:** And that's how we build the team to be like super experienced and form a founder so they can do it for like one or two people.

**Daniel Lopes:** But that's actually where like a lot of our effort is going.

**Daniel Lopes:** We're just doing these little things to work to build efficiency into the process, but not on the scalability.

**Daniel Lopes:** This is kind of crazy because my job at Fathom, we had like 10 million users and we were doing like a billion runs a month.

**Daniel Lopes:** And here we have 50 users.

**Daniel Lopes:** still do a lot of parallelization and still run pretty efficient, but it's different than the product-led effort where you sweat a lot more on the infrastructure side of things.

**Marcel Santilli:** Yeah, then like in the two-year horizon, like I think that one of the bigger unlocks here, in addition to what Daniel mentioned, is like the marketplace, but it's not just the marketplace, right?

**Marcel Santilli:** Like it's ultimately how do you get the right people in with the right diversity of skill set, right?

**Marcel Santilli:** Like how do you vet them and get them to be the right people?

**Marcel Santilli:** And then how do you break down the task, the unit of the task and set the right calibration, the right evaluation, and how do you match them to the right person?

**Marcel Santilli:** And then how

**Marcel Santilli:** If you evaluate that that person did the right unit of work, that will actually deliver that output.

**Marcel Santilli:** And so, but once you unlock that, then you're in a really strong virtual cycle because now with truly with every single run, you're getting better, you know, and you don't need to do that forever.

**Marcel Santilli:** It's like you do one run and then you do two runs and now your confidence level that that's the right person increases the, your next loop, the agent or the workflow will be better.

**Marcel Santilli:** And, and now you know that this person can be elevated to a next level of, of intervention that will add even more value.

**Marcel Santilli:** And so it's like the human intervention incrementally gets better in, in higher leverage over time.

**Marcel Santilli:** And so it's not like a linear data labeling thing where it's like, all right, we're labeling a thousand images now.

**Marcel Santilli:** Now let's go label 10,000.

**Marcel Santilli:** Now let's go label 10 million.

**Marcel Santilli:** It's not like that, right?

**Marcel Santilli:** Like it's, it's truly like more of a virtual cycle.

**Marcel Santilli:** And then as models get better, it's like, we're benefiting because we're writing that model wave as

**Marcel Santilli:** And then that process data and that intervention data gives us like kind of the data mode and that work effects of like improving the whole as well.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** I have just one more question.

**Felipe:** So the other direction of scalability is maintenance of the flows that you are creating for each customer.

**Felipe:** So as the customer evolves, especially if they're startups, their strategy may change, their content strategy, like all the strategy changes.

**Felipe:** That means that you need to redo the work, update the documents, update the conversations.

**Felipe:** So like are the customers willing to pay 30K every time that they are pivoting a company?

**Marcel Santilli:** Well, so right now there's a lot of things playing into our advantage here and why service is actually way, way better.

**Marcel Santilli:** And so our customers pay between $9,000 and $230,000 a month and many of them have been with us for a year or close to a year.

**Marcel Santilli:** And we've only been in existence for just over a year, you know.

**Marcel Santilli:** And so a few reasons for that.

**Marcel Santilli:** One, they know that it's a full-time job to maintain workflows, and our engine of maintaining workflows and improving them is better.

**Marcel Santilli:** Two, it's really hard.

**Marcel Santilli:** Marketing requires a lot of specialists.

**Marcel Santilli:** Most teams can't hire seven different specialists, and that's why I've always relied on freelancers, and it's really inefficient to go find a bunch of specialists and manage them, whereas for us, we're taking that away for them.

**Marcel Santilli:** But then the next part is, if you think of e-commerce, like a catalog, Amazon spends a billion in a catalog, and so they're enriching, de-duping, improving the catalog.

**Marcel Santilli:** Sure, it's compounding, and it creates network effects, but it's also decaying, and the half-life of that catalog is essentially getting shorter, because with AI answers, you need more answers, and you need to be more fresher, better research, and things like that.

**Marcel Santilli:** And so that creates this incentive that the more seeds you plant, and the more things you do, the more you need to maintain, and the more they need us to maintain, because now we have all the context of how it's maintained.

**Marcel Santilli:** All the people that they need.

**Daniel Lopes:** And for them to reach that, it becomes harder.

**Marcel Santilli:** So a quick example here, Superhuman didn't want to hire a head of content.

**Marcel Santilli:** They hired us.

**Marcel Santilli:** And now they got to acquire or whatever, merge with Grammarly.

**Marcel Santilli:** And now Grammarly wants us to essentially do it.

**Marcel Santilli:** And now they're migrating Coda, Grammarly, and SoftRecord, and Superhuman all into it under the Superhuman brand.

**Marcel Santilli:** And they need to do that for thousands and thousands of pages.

**Marcel Santilli:** They need to update every link.

**Marcel Santilli:** They need to do this.

**Marcel Santilli:** It could be impossible for them to do it without us, or it will cost tens of millions of dollars for them to do it.

**Felipe:** So basically, the aestheticiness will come from the complexity that is involved in this domain.

**Felipe:** They won't be able to absorb the complexity, but want to give them a way around the complexity.

**Marcel Santilli:** It's the process data, the knowledge, the experts, also the knowledge base, because we're constantly ingesting high-trusted sources of knowledge.

**Marcel Santilli:** And then it's the signals, too.

**Daniel Lopes:** I would also add that we might, once we're moving super fast, so we're exposing just the things that we think folks can absorb.

**Daniel Lopes:** So we're...

**Daniel Lopes:** We're the reports, we're exposing the artifacts, so they can edit the artifacts, they can consume the artifacts in an MCP cloud, for example, but we might start exposing more and more as our internal app starts to be more easier to use, or we see the repeatable things, and then there's also things that we're to start exposing more, like for example, with the new version of the framework, you would be able to just like NPM install one of our agents.

**Daniel Lopes:** So you could use our researcher, or you could use our drafter, or you could use our post-processing.

**Daniel Lopes:** So if you want to internally have one of your, let's say in the future, have like AI engineers on every company, or GTM engineers on every company, they could use that.

**Daniel Lopes:** And we might also like even make the whole framework open source, and have an ecosystem around with like a registry of like workflows, and things like that.

**Daniel Lopes:** So we see a bunch of opportunities where we could build the ecosystem or extract products. Actually, I think for folks who don't want us to run for them, it might be like the cost of one employee but performing for a hundred people. But if they want to run it themselves, maybe we're going to have a cheaper self-serving product for agencies if we find the common denominator for everybody.

**Felipe:** So who's your closest competitor?

**Daniel Lopes:** That's a good question.

**Marcel Santilli:** Internal teams that are afraid for their jobs.

**Felipe:** Internal teams, I got it.

**Marcel Santilli:** Yeah, like we come in and like the CMO brings us in or the founder brings us in and there's like some low-level person that hasn't reinvented themselves.

**Marcel Santilli:** They're super nervous.

**Marcel Santilli:** They're like, no, no, we don't need help.

**Marcel Santilli:** Like, we're fine.

**Marcel Santilli:** And, you know, like they're kind of like really nervous.

**Marcel Santilli:** So we're navigating that.

**Marcel Santilli:** It hasn't been an issue like, you know, that we can't be successful, but it's definitely like a, you know.

**Marcel Santilli:** One of the traits, yeah.

**Daniel Lopes:** On our ICP matrix that we look for.

**Felipe:** We say we have experiences like that, like, oh, no, we can do it ourselves.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** Right.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah, exactly, but, well, I appreciate it.

**Marcel Santilli:** Again, like, if anything pops up, too, like, we're happy to, we're open book, you know, we're even thinking of open sourcing some of these frameworks that we built.

**Marcel Santilli:** And so we're, you know, hopefully this was helpful and happy to spend as much time as needed, you know.

**Felipe:** Super helpful.

**Felipe:** I'm good with my questions.

**Felipe:** I don't want to take more of your time.

**Felipe:** Thanks a lot for taking the time to explain this to us.

**Felipe:** Congratulations.

**Felipe:** It looks pretty cool.

**Felipe:** And actually thinking about mentioning this to my boss.

**Felipe:** So, yeah, that's all for me.

**Felipe:** don't know if you have any other questions.

**Bo Wang:** No, I don't have any questions.

**Bo Wang:** Yeah, this is amazing.

**Bo Wang:** mean, I'm so, this is a great product.

**Marcel Santilli:** Thank you both so much.

**Marcel Santilli:** It's, you know, it means a lot, too, that you all care so much to go this deep, you know.

**Marcel Santilli:** I was just telling Richard the same thing, too, so I appreciate it.

**Marcel Santilli:** This is our life's work.

**Marcel Santilli:** This is not like us, like, building a quick startup to sell.

**Marcel Santilli:** So we're super motivated to build something that's going to live for a very long time and hopefully bring the same 100x productivity that engineers have now.

**Marcel Santilli:** If you think of engineers 10 years ago to today, they're 100x, and the knowledge workers, I think, are not experiencing the same thing.

**Marcel Santilli:** I think there's more unlocks that need to happen for that to be true.

**Felipe:** That's true.

**Felipe:** All right.

**Daniel Lopes:** All right.

**Daniel Lopes:** Thanks, everybody.

**Marcel Santilli:** Take care.

**Marcel Santilli:** Bye.
