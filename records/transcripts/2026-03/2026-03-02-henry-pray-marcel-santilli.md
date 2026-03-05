# Henry Pray <> Marcel Santilli

<metadata>
date: 2026-03-02
time: 22:30 UTC
duration: 58 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Henry Pray
fireflies_id: 01KJKPWY5YNVSHFABYRGEZW9EN
meeting_link: https://growthx-ai.zoom.us/j/82542336775?jst=2
transcript_url: https://app.fireflies.ai/view/01KJKPWY5YNVSHFABYRGEZW9EN
keywords: Output AI, AI Workflows, Content Automation, Knowledge Work, SEO Optimization, AI Platform
source: fireflies
enriched_on: 2026-03-03 18:00 UTC
</metadata>

---

## Summary

Marcel gave Henry Pray a deep-dive walkthrough of GrowthX's full stack — from the AI shift disrupting B2B buying, through the five-layer company architecture (infrastructure, data, platform, services, distribution), to a live demo of the Output AI framework building a custom workflow on the spot. Henry, currently acting as interim CPO at 10.4 and general manager of his lab, asked sharp product and business questions and left with a strong understanding of how GrowthX's 332 workflows power 70 clients publishing 2,000 pages/week, with a follow-up demo from Daniel scheduled next.

---

## Context

This is a second conversation between Marcel Santilli (GrowthX co-founder/CEO) and Henry Pray, who is currently juggling three roles — interim CPO at 10.4 (a product he built), newly promoted general manager of his lab, and unfilled head of product for that same lab. Henry had a brief initial conversation with Marcel previously where he got a quick overview, and has since done independent research on GrowthX. This call was set up for Marcel to give a thorough, full-transparency walkthrough of the company's vision, technical architecture, and business model, followed by a product demo from Daniel (GrowthX co-founder/CTO).

The meeting fits into what appears to be an exploration of a deeper relationship — Henry is asking investor-grade questions ("if I were invested in GrowthX, what questions would I be asking?") and probing product-vs-service delineation, competitive landscape, and long-term vision. His product and AI background at his lab makes him a potential advisor, investor, or strategic partner.

---

## Relevance

**To GrowthX Business Development**
- Henry is asking investor-level questions about 5-year vision, competition, product-vs-service split, and revenue trajectory ($12M to $34M) — signals potential investment or advisory relationship, not just casual interest
- Henry's product background (building 10.4, running a product lab) makes him a credible advisor on the platform transition from service-heavy to agent-first
- He independently researched competition before this call and has "a bunch of questions around that" — engaged prospect who does homework
- The call ended with a warm handoff to Daniel for a product demo, maintaining momentum

**To Output AI / Open Source Strategy**
- Henry immediately grasped that Output AI is "industry agnostic" and "knowledge work agnostic" — validates the open-source positioning beyond marketing
- He compared Output AI to where Claude Code is heading, calling it "one step removed from the command line" with scripts/apps on top — useful framing for positioning
- His reaction to the live workflow build was strong ("if I tried to run this through Claude Code right now, it's just going to miss a lot of the hey, how do you actually productionize this") — direct validation of the framework's value proposition
- Henry asked about normalizing learnings across customers to build a moat — a strategic priority GrowthX hasn't started yet (Marcel said "not yet")

**To GrowthX Services/Delivery**
- Marcel disclosed that the service model "is not as sticky as it needs to be" and is "limited to the performance of one human" — transparent framing of the current gap
- Shared specific client examples: Vercel (5,000 pages, kicked off last week), Lovable (4-week programmatic template project), and Airbyte
- Referenced 70 customers, 60 forward-deploy engineers, 332 workflows, and 2,000 pages/week published — numbers Henry can use to evaluate scale

**To CheckThat**
- Marcel positioned CheckThat as both a lead gen tool and a data moat — collecting 2-3 million AI responses/month across buying categories
- Framed it as disrupting AEO tools that "3x the cost of just probing these engines yourself" with no API access

---

## Decisions & Commitments

- **Marcel committed to sending Henry the meeting notes and a longer strategic document** after the call
- **Daniel will demo the product** to Henry in a follow-up session (appears to have been scheduled immediately after this call on a separate Zoom)
- No formal business decisions were made — this was an exploratory/relationship-building conversation

---

## Open Questions

- Henry has unasked competition questions — he researched competitors before the call and said "I have a bunch of questions around that" but they never got to them
- Henry's exact relationship intent (advisor, investor, partner, or something else) remains undefined — he's asking investor-grade questions but no explicit framing was discussed
- How GrowthX will normalize learnings across customers to build a defensible moat — Henry flagged this, Marcel acknowledged it hasn't started yet
- The 3-5 year competitive landscape for Output AI as an open-source framework — Henry asked "what does competition look like?" but the conversation moved on before a deep answer

---

## Overview

- **Market Disruption:** AI is fundamentally changing how B2B buyers research and make decisions — brands that don't adapt their websites for both human visitors and AI agents risk losing visibility and relevance.
- **Website as the Core Asset:** GrowthX positions the website as the primary growth and leverage driver, managing pages at scale (health, content quality, SEO, internal linking, AI visibility) in a way that's impossible to do manually.
- **Output AI Framework:** An opinionated, TypeScript-based AI framework built in-house over 18 months to run 332+ workflows across the entire company — from recruiting to content generation to research synthesis. Preparing for open-source release.
- **Service-First Model:** Eight-week strategy sprints with forward-deploy engineers, currently serving 70 clients and publishing ~2,000 pages/week. Transitioning toward an agent-first platform.
- **Data & Scoring Systems:** Page-level scoring (health, content quality, engagement, conversion) and opportunity scoring (intent, difficulty, brand alignment, traffic potential) to automate prioritization. Principal data scientist Jacob joining the team.
- **Growth Trajectory:** Targeting $12M to $34M revenue this year. Current contract value ~$200K/customer. Market comparable: Semrush's 25,000 mid-market/enterprise customers at $40-60K/year for analytics-only.

---

## Key Topics

### Business Vision and Market Context

GrowthX is focused on addressing the fast-shifting B2B buying landscape impacted heavily by AI disruptions, aiming to become a critical growth driver through website optimization and AI-powered content management.
- Marcel Santilli emphasized the rapid disruption brands face as AI changes how buyers research and make decisions, requiring companies to adapt quickly or risk falling behind.
- The strategic focus is on leveraging websites as primary assets for conversion and growth, improving both human and AI agent interactions with content.
- GrowthX's service and platform aim to help clients sustainably update and optimize website content to influence AI agents and human visitors alike, creating compounding growth benefits.
- This approach addresses the overwhelming complexity brands face with large-scale content management, broken links, SEO, and page health, which is now impossible to manage manually.

GrowthX's product and service model marries AI-driven automation with human strategy to continuously improve content at scale, enabling smarter outputs with every iteration.
- Marcel described a layered approach involving infrastructure, data, platform, services, and distribution to build a comprehensive AI-powered growth system.
- Initial focus was on delivering service-driven strategy sprints with human-in-the-loop execution before evolving the platform into a customer-facing command center.
- They started in April 2024 with their first customer, quickly realizing low-code tools were insufficient for scaling complex AI workflows, prompting the creation of proprietary runtime infrastructure.
- The business model targets mid-market and enterprise customers who currently spend heavily on SEO tooling and agencies, positioning their offering as a full end-to-end solution rather than just analytics.

### Product Infrastructure and Output AI Framework

GrowthX developed an opinionated, TypeScript-based AI framework called Output AI to manage AI workflow execution, tracing, and evaluation at scale, which has powered their entire business for the last 18 months.
- Marcel explained the framework's technical design, operating on file systems with built-in tracing and evaluation features critical for debugging and improving AI workflows.
- Output AI handles hundreds of workflows daily, running complex multi-step processes such as recruiting assessments, research synthesis, and content generation.
- The framework enables the company's internal platform to orchestrate workflows like site crawling, content drafting, SEO optimization, and fact-checking automatically.
- This infrastructure was built in-house after evaluating existing tools as inadequate and is now being prepared for open source release to lower AI engineering barriers industry-wide.

The open-source strategy serves both as an engineering brand builder and a business opportunity by making AI workflow engineering accessible to junior engineers and external partners.
- Marcel emphasized the framework is how they run their company and deliver services, not just a product to sell, but with potential for monetization through cloud hosting and workflow marketplaces.
- They plan to support both private and public workflow directories, akin to Terraform providers, allowing companies to customize or share AI workflows easily.
- The open-source release will include primitives and tooling for workflow creation, evaluation, and deployment, enabling rapid AI-native operational scaling.
- The team includes experienced engineers from Hashicorp and other tech companies, underscoring the robustness of their infrastructure.

### Service Model and Client Engagement

GrowthX operates a service-first model where forward-deploy engineers build and customize AI workflows to meet specific client needs, delivering high-touch onboarding and strategy sprints.
- Clients receive eight-week strategy sprints involving context gathering, competitor and market research, opportunity mapping, and iterative content calibration.
- Marcel described detailed persona and keyword research workflows that identify content gaps and opportunities prioritized by intent, relevance, and potential traffic impact.
- The service extends to content creation, page optimization, and template generation, exemplified by a four-week project where they created programmatically generated website templates for a client.
- This hands-on approach enables clients to see quick wins and validate the AI-driven growth strategy, but current delivery remains heavily human-dependent.

There is a strategic plan to evolve from service-heavy delivery to a platform-centric model that exposes AI agents and scoring tools directly to clients for greater scalability and stickiness.
- Marcel acknowledged that while the service model drives fast revenue and deal closure, it limits scale and is reliant on individual human performance.
- The platform vision is to simplify complex AI workflows into an agent-first experience, reducing friction and enhancing value through automation and transparency.
- Current client interactions involve Slack and Google Docs for updates, but plans include dashboards and AI-powered scoring tools for real-time decision making.
- This transition is supported by ongoing advisory from Ryan Singer and extensive product design work focusing on user experience and workflow simplification.

### Data, Scoring, and Analytics

GrowthX collects extensive data across content performance, SEO, AI visibility, and user engagement to build robust scoring systems that guide content prioritization and optimization efforts.
- They score pages on health, content quality, engagement, and conversion potential, enabling clients to identify which pages need urgent attention or have unrealized potential.
- Opportunity scores factor in intent, difficulty, brand alignment, and traffic potential to help clients prioritize work efficiently.
- Marcel highlighted the integration of traditional ML and data science, with a principal data scientist joining soon to enhance model accuracy and close the performance loop.
- This data-driven approach is fundamental to their goal of continuous learning and autonomous improvement of AI workflows.

### Strategic Growth and Market Positioning

Marcel framed GrowthX's growth strategy as targeting a massive combined market of content marketing, SEO agencies, and AI tooling, with a current average contract value of about $200,000 and a potential market opportunity in the billions.
- He compared their approach to competitors like Semrush, but stressed they provide a full end-to-end solution including content production, not just analytics.
- Their vision includes owning the category of website AI as a force multiplier that compounds client gains autonomously but guided by human judgment.
- GrowthX plans to expand from 12 to 34 million in revenue this year by focusing on growth, leverage, and website assets as key business drivers.

---

## Action Items

**Marcel Santilli (GrowthX)**
- Send meeting notes and the longer strategic document to Henry Pray after the call
- Coordinate Daniel's demo session for Henry to see the current product sprint in action

**Henry Pray**
- Join follow-up demo session with Daniel (GrowthX co-founder/CTO)
- Share competition questions that didn't get covered in this session

---

## Transcript

**Henry Pray:** Trying to hire a CPO right now for 10.4, which is the product that the company I just built. So I'm having to act as kind of interim CPO. And then I was just promoted general manager, so I'm managing like our whole lab. But then we also haven't backfilled my head of product role for the lab. So I'm also doing that right now. So it's just kind of crazy.

**Marcel Santilli:** That's wild, dude.

**Marcel Santilli:** Well, I appreciate you taking the time too, because I'm really excited to spend more time right now and also for you to meet Daniel here in a little bit as well. He can kind of demo you the product and things like that. And I think we could do a couple of things. I wanted to walk you through the big picture, the mental model.

**Henry Pray:** Yeah.

**Marcel Santilli:** Of the company overall because there's so many layers to the onion, if you will. We somewhat touched on this when we last talked, but I think that would help. And then this is honestly more for you to probe and go deeper and understand everything, full transparency, open up everything. So you feel like, okay, I get a really good sense of what this thing is, where you all are. But anything else you think would be helpful to cover in addition to that for this hour?

**Henry Pray:** No, I think that's good. I mean, I've basically 10x'd my knowledge on what you guys do since we last talked, but that's still like a very tiny amount. I went a little deeper last night on it. So I think that all sounds great. And then I would love to understand at some point from a business perspective, what is your vision? What does this look like in the next five years, what is success? Like if I were invested in GrowthX, what questions would I be asking? I have a lot of those, but I would love to understand where the product is today. What is product? What is services, where that delineation comes. I went a little into competition last night. I have a bunch of questions around that. But yeah, let's just kind of go from there.

**Marcel Santilli:** All right, perfect. So I want to start with the whiteboard that I presented. I can't remember if I showed you anything from this last time.

**Henry Pray:** Yeah, you did. You went through it really quickly. But I'd love to see it now that I have a little more understanding.

**Marcel Santilli:** Okay, cool. Let's do that. And then I can do a super high level of where the product is today and then Daniel can spend a lot more time on where we're at — we're dead in the middle of this 6-week sprint. We do a Basecamp style. Are you familiar with Basecamp?

**Henry Pray:** Yeah, I do similar things.

**Marcel Santilli:** And then Ryan Singer is an advisor to us, so we've been doing four-hour sessions with him once or twice a month. It's life changing honestly.

**Henry Pray:** Marcel, can you send me the notes after this call? Not to be writing furiously.

**Marcel Santilli:** Yeah, I'll do that as well. That's perfect.

**Marcel Santilli:** Okay, so the main thing right now — when I look at companies like HashiCorp or Scale AI, regardless of whether you agree with everything or not, they pick the right shift. If you pick the right shift and the shift is important enough to enough people, that's half the battle. If you pick the wrong shift, the wrong market, it's way harder. For me it was that this feels like a continuation of everything that's happened in my professional life.

**Marcel Santilli:** The shift is essentially every single person making any kind of purchase decision, especially B2B — they're changing how they make those decisions today, how they consume information. Obviously we all know that, but it's having a bigger impact a lot faster than brands thought would happen. People knew AI is taking over but I don't think any brand was like, yeah, my entire business is going to get disrupted overnight and then compound. All these entrants to the market, more noise. They're getting hit from every direction — the go-to-market side, how people buy and discover them, and also from competitors. Everybody's just fucked, essentially. They're trying to figure it all out. And fundamentally, I don't think there's a comeback here. There's going to be human buyers still involved in bigger decisions. But then there's what I'm calling agents — anyone or any system that's fetching information for you, deciding, or helping you think through it.

**Marcel Santilli:** And then there's training bots — you saw Block just talking today about her husband, 40% RIP. And I'm like, that guy is incredible. If somebody like that is getting hit, I can't even imagine. Every company is trying to figure out how to grow and how to do more with less. Everybody's in the same boat and they're all confused.

**Marcel Santilli:** From our perspective, regardless of this AI shift, the first thing I would always do when I come into a company — let's take UpKeep — the first thing I did was like, how do I fix this fucking website so I can actually create better pages faster and have a better surface area that I can control that will drive everything else? It wasn't the only thing I did, but it was the first thing I did. Wait, who's managing the website? What the hell? We have seven different WordPress instances. Why the fuck do we do that? And it was always because the website is your biggest driver. Conversions are happening there. It's how people perceive you. You can measure it, you can control it.

**Marcel Santilli:** But now it's becoming way more important because it's also how agents fetch information and they're hungry for more and higher quality information. If you do it right, it's both growth and leverage at the same time. If you figure out a sustainable path to update your pages, improve your content, improve your surface area in a way that influences how AI agents talk about you, when you show up, how you show up, as well as influence how people convert when they do come to your site — that's the ultimate holy grail.

**Marcel Santilli:** The problem is now there's so much more context in the agents and a way longer tail. When I'm doing research on something, it's not one thing — it's literally researching tons of things and it's not pulling a little bit of context. It's pulling an insane amount of files. And that's where the future is going. It's getting way harder.

**Marcel Santilli:** So where we nailed it when we first started — content we knew was part of it, and I'll explain more on why content. But what we ended up getting to as we worked with these 70 customers is the website just felt like the right place that was so critical that everybody's willing to pay for and they're wasting a lot of money on. It's really an impossible job to do this manually now. It's truly impossible. Vercel just kicked off last week. They're like, hey, there's 5,000 pages here, I don't know what the fuck to do. We're Vercel, but we don't know what to do. Help us.

**Marcel Santilli:** And a lot of this is just managing pages — keeping them organized, current, healthy, and performing. The factors that go into that are insane. Do you have duplicate H1s? Does the content of your page match the intent it's meant to serve? Is it linking to the right things? Is there a broken link? Is it loading slow? So many different things. And then creating net new pages to increase your surface area, your sphere of influence, and constantly optimizing based on your reward targets. It's kind of like our dev setup — Sentry plus Render MCPs constantly running on a cron job, listening for alerts and fixing silly bugs. That's what you need for a website, but it doesn't exist today.

**Marcel Santilli:** At the end of the day, every brand cares about revenue and conversions. For that to happen, there needs to be traffic, engagement, and visibility. What we're building for our platform is a way that AI can handle the production, the optimization, and the learning at scale. Humans still provide the strategy, quality, and judgment. The system gets smarter with every output. That's a huge part to think about — how do you create a system that rides the model wave? As Claude gets better, as models get better, your company benefits from it, not threatened by it. That was one broad principle from the beginning. And the second one: how do we do it in a way that with every output for every client, things get smarter and better — both for a client, but also for us overall as a company.

**Marcel Santilli:** And so that's what we're building towards. If you think about what we build, it's almost like five layers — infrastructure, data, platform, services, and distribution. It sounds crazy, but we started in the infrastructure and service layers. And now as we gain confidence, we're ingesting the data that only we can generate. The platform is no longer just internal — it's evolving into a command center for customers. The reason we didn't start with the platform is that unlike engineering, people didn't want more tools. There's 40,000 martech tools and a hundred thousand marketing agencies. Nobody wants that.

**Marcel Santilli:** So we started as a service. Very simple: hey, you need to grow, we create content for you and help you with your strategy. We do this eight-week strategy sprint. Week one we're getting the inputs, processing that, creating context files. Week two, setting the entire strategy and opportunities. Week three, starting calibration. Week four, publishing and continuing calibration. Week five, starting to wrap up. It's literally like building an agentic pipeline for them with humans in the loop. You need context, the plan, execution, all of it.

**Marcel Santilli:** When we started doing that — April 2024 was the first customer — what we quickly realized a few months later was low-code tools do not scale at all. Taking an n8n or whatever, adding a node, typing something up — that just doesn't work. It works in a very small spectrum. But the second you bring other people in who don't understand your logic, the second you need to run this times 100, need tracing, need evals, need loops — it just does not work.

**Marcel Santilli:** My co-founder, when we paired up, we met through a mutual best friend. He had taken a year off from a Basecamp spinoff that he co-founded, to study and go super deep. Earlier in his career he was very involved with the Basecamp folks, teaching Rails and things like that. He was also at IFTTT. He saw what a real runtime layer firing a billion runs a month looks like — precursor to Zapier. He saw early on, 18 months ago, the infrastructure we needed had to be different.

**Marcel Santilli:** Let me pull this up. Daniel will share more of this with you.

**Marcel Santilli:** So the way to think about it — we named it Output AI framework and we're open sourcing it in the next couple of weeks. It's an opinionated AI framework with tech choices for code generation and production at scale. TypeScript framework, prompts in code, self-contained for context window. It works on a file system because that's how coding agents work. Docs are a core part — auto-generates the docs. Built-in traces for evals and a bunch of other things. Essentially you just npm install. It connects to your coding agent. I'll show you it running locally. This allows us to build all the workflows we have, and for every single run it generates the scenarios, all the tracing, all the steps. You can do the runtime and the inspection. This is what has run the whole company for the last 18 months. Sorry, go ahead.

**Henry Pray:** Well, if I think about a typical run, especially on the LLM side and the eval side — it's like, hey, how does this content that we just did, how does a generic LLM react to it? What does it get out of it? How does it compare to other things? Is that kind of what you're doing?

**Marcel Santilli:** Yeah. So this is just a random workflow I picked from the runtime. This one runs on Ashby — it's for recruiting. This is all in code, but it's just a mermaid diagram. It starts, gets the Ashby data, and then you can see the whole flow here. And this is the output. You can see the recommendation — move to the next round. What it did is analyze the resume of this applicant, analyzed the questions and answers, the strengths to each. And then it marks the final assessment: demonstrated strong background in technical recruiting. We're hiring another technical recruiter. And then it posts to Slack.

**Marcel Santilli:** These were the inputs. If you go into this specific workflow in the repo, these are literally the files of this workflow. You can see the inputs and outputs all well defined, the activities, the prompts, the steps. You can run it. You can load the last execution — this one is running right now, live. Look how many executions just in the last day. This runs our entire company. We have 332 workflows. Every product, every feature in our products is a workflow.

**Marcel Santilli:** I'll show you another one we use a lot — our research supervisor. It's agentic, so you can see it has iterations, elements of judge loops. For example, this execution is a legal CRM market update for legal firms. It creates a research plan, synthesizes results, evaluates based on the context of that company — one of our clients. It can generate additional questions, store it in the knowledge base. And the output is super detailed, really well cited.

**Marcel Santilli:** Most of our clients won't see this today. We're open sourcing the core because this is a way of thinking: what if knowledge work was represented in code and was a shared resource for coding agents to use? I'm calling them coding agents, but Claude Code is a coding agent — it's an LLM agent, they're really good in code and file systems. And this is 18 months ago. Pre-Claude Code. We were like, this is the future.

**Marcel Santilli:** So we built an infrastructure team. Clint was at HashiCorp, took them to IPO. He was at Roku before. He built a lot of Terraform and Terraform providers. Stefano, his last company got acquired by Meltwater. He's a badass. Ben was at Airbyte. That's the team that built the core of this.

**Marcel Santilli:** So that's the infrastructure layer. And then this layer is our platform that we run everything on. I'll show you a few sections. Think of these as context files — like Lovable, this is just a company context that can be pulled. There are workflows to generate more, but you can also just put any context files here. And then we set up these pipelines that run something based on an assignment. Think of this pipeline as the research I just showed you — it ran for 48 minutes. Then it drafts an article, adds internal links, adds sources, validates writing guidelines, generates SEO stuff, does fact checking, generates a cover image and even infographics based on the content.

**Marcel Santilli:** That's the end to end, but there's so much engineering that goes into it. Today the way it works is a YAML file that a forward-deploy engineer tweaks based on workflows. If we need custom workflows, they just have Output AI running locally, create a new workflow, and deploy to our studio. This is not where the platform is going to be when it's exposed to the rest of the world, but that's how we publish 2,000 pages a week for our 70 clients.

**Henry Pray:** Yeah.

**Marcel Santilli:** And then today the service — if you go into Lovable for example, we set the strategy but we're in there with them. Sharing updates, this is Megan from our team, hey this is what we're doing, this is how it's going. We're an extension of their team.

**Henry Pray:** So if I think about this — I'm going to dumb this down a lot, just so I can understand a lifecycle. I'm Widget Company X. Depending on the strategy, you provide a list of the common questions. What are the common searches people are doing within an agentic flow to figure out where do I come up? Let's say I'm a law firm. "What are the best law firms?" "Does this law firm do X?" "How does this law firm compare to Y?" And then you target specific content to replace or optimize those answers. And then you use elements of judge or whatever to rate that content, see how it's performing, and constantly optimize by rerunning that pipeline. Is that directionally right?

**Marcel Santilli:** Directionally, yes. Think of it as mapping out your entire context. First, we're doing research to understand the context of your company — who you're for, what your product does, how you want to sound to the market. Then we're doing that with all your competitors. And understanding your market and buying categories. That's the context engine.

**Marcel Santilli:** Then we're thinking through the personas you're going after and creating a map of all the things they care about — pain points, jobs to be done, terminology, what kind of questions they ask, what are all the things they're going to need answers to. And you want to position yourself as the best answer. Those are your opportunities. Then we quantify all those opportunities. Some are net new pages, some are improving existing pages.

**Marcel Santilli:** If you kick off an agent doing persona keyword research to come up with opportunities, it would start to run and generate them here. But this isn't set up in this environment. Let me show you Airbyte. It's generating all these opportunities, but Daniel can give you a better demo — we're deep in this this week and it's moving fast.

**Marcel Santilli:** I wrote a longer doc I can send to you. But the way to think about GrowthX services and platform — are you familiar with Semrush?

**Henry Pray:** Like a SimilarWeb for SEO kind of?

**Marcel Santilli:** Yeah, exactly. So this tool has 25,000 mid-market and enterprise customers paying about $40-60K a year. And one way to think about what we do is that tool only tells you keyword-based things and roughly how sites are doing from an SEO perspective — but it doesn't actually help you do anything about it. We're doing the end to end. Our contract value right now is about $200K. At $200K that would be about $5 billion a year in ARR for those 25,000 customers.

**Marcel Santilli:** And those 25,000 customers aren't the whole market. That's just people willing to pay and be a mid-market to enterprise customer for one company that went public and got acquired by Adobe recently. Another way to slice it — content marketing plus agencies plus SEO agencies plus tooling combined, it's a massive TAM. And then there's this new category called AEO. And Output AI, I think of as engineering plus framework. We're not trying to monetize it short term, so we're not projecting a ton of revenue from it. But these agents truly have potential to be a Replicate for knowledge work.

**Henry Pray:** Yeah. So Output AI — when I say industry agnostic, the other ones are very marketing focused. Output AI, you're getting into generic AI outputs, working tools. Is that a way to think about that?

**Marcel Santilli:** Yeah, exactly. Let me open this up. I'm going to run it locally so you can see. Build workflow — this is the framework already set up locally. These are the plans, and these are the workflows we'd already built, mostly for tests. I'm going to create a new workflow. Is there a workflow you can think of recently?

**Henry Pray:** Like just for any generic thing?

**Marcel Santilli:** Yeah, any generic thing.

**Henry Pray:** Yeah, we can go through content. One of the things I've been working on is basically doing a lot of ethnographic interviews, coming up with key findings, figuring out what frameworks are common among those findings, and then posting a LinkedIn article about product knowledge. Is that the kind of workflow you would do?

**Marcel Santilli:** Yeah. Okay, explain it to me again.

**Henry Pray:** First step would be to extract a summary of a research interview. Second step, are there any product frameworks or AI frameworks talked about that could either solve what they're discussing or that directly relate? And then comparing those to a dictionary of other interviews you've done to see if there's a common theme or connections across them. I'm kind of cheating because it's something I'm thinking about building right now.

**Marcel Santilli:** Yeah, that's great. All right, so I just put that in. This is a cheap version — super one-shot, call it a day. Let's do test text.

**Henry Pray:** Yeah, built over time.

**Marcel Santilli:** Okay, so what this is going to do is plan this workflow. There's a lot of things baked into the framework already — scenarios, pre-flight checks, design workflow architecture, design individual steps, design evaluator, design LLM prompt, testing strategy, generate final plan and document, run post-flight checks. A bunch of stuff baked in with the primitives already.

**Marcel Santilli:** While it's doing that, I can show you — it has scenarios. Like transcript-to-LinkedIn — takes a transcript and turns it into a LinkedIn post. You can see the prompts, the steps, the evaluators with LLM-as-a-judge, and the overall workflow. Open any of these and it's all in code. The prompts follow really good best practices.

**Marcel Santilli:** This is what powers everything. This is the process a forward-deploy engineer follows to create a workflow and deploy it. That gets pulled into our product. This has a lot of the bells and whistles we didn't find anywhere else in other frameworks.

**Marcel Santilli:** The only other piece we didn't talk much about is CheckThat, which is our AEO open index. Think of CheckThat as — we need to do research on every single company in every buying category that our customers are in. We needed that anyway. And we also needed AI visibility data. So if we're going to do that anyway, we might as well give it away for free and disrupt the rest of the space. You can track all the prompts — we're collecting about 2-3 million AI responses a month across all the different buying categories. These are evaluation-type prompts — "what are the best..." — and you can see if you're Flodesk, whether you're mentioned or not. Where are you mentioned? Where are you cited? What are the sources? Across all the different AI services.

**Marcel Santilli:** The idea is for this to be a reinforcing flywheel. GrowthX service at $200K a year. CheckThat drives awareness, leads, and data we need anyway — the data layer.

**Henry Pray:** Yeah.

**Marcel Santilli:** None of the AEO tools had an API and they were 3x-ing the cost of just probing these engines yourself. So we just built it ourselves. Output AI is the AI engineering we need anyway to build workflows for clients and power all our products. Turning it into an open-source framework with cloud deployment has revenue implications later, but also builds an engineering brand to attract the best talent long term. All products share data, customers, and brand.

**Marcel Santilli:** For this year we're going from about $12M to $34M. The TLDR: the world changed, three audiences. Every company needs growth and leverage. Website is the asset that drives both. The job is to make it compound. We build four layers — services to learn, infrastructure to scale, data to see what AI sees, community to own the category. Website AI as a force multiplier, compounding, always getting better, autonomously but guided.

**Marcel Santilli:** The outcomes we're driving: visibility, traffic, conversion. The outputs are pages — pages are content assets and code. Work through AI agents and workflows with human inputs and evals, but agents first. The inputs are context, plan, strategy, knowledge, and signals from all the data you're ingesting.

**Henry Pray:** So back to Output AI — maybe this will be good questions for your co-founder. I understand you need to build this infrastructure anyway, so why not open it up. But it does seem like the ICP or target customer, even the vision for Output AI — what you're building is not marketing specific. It's knowledge agnostic. It's work product agnostic.

**Marcel Santilli:** Which also runs the whole company. Every process we have — your GitHub repo has your code for only your product, but all your knowledge work, all your processes are spread out everywhere. Anything you need to reproduce more than once, anything that AI needs to use, it has to do tool calling, fetching, a bunch of things. This is a way to codify knowledge work.

**Henry Pray:** Right. If I think about where the future of Claude Code is going, in a way it's similar. One step removed because it's not quite in the command line, but a similar process of codifying where all your knowledge is. The only difference is you're creating — I'm going to call them apps or scripts — on top to actually run them. Is that how you'd think about it?

**Marcel Santilli:** Yeah. Honestly, it wasn't like some grandiose thing. It was truly like, hey, I'm building AI workflows. This is hard as hell. Why isn't this in code? Is there anything out there that does this? No. Why not?

**Henry Pray:** I don't know.

**Marcel Santilli:** How would we do it? Well, we need it for ourselves to deliver a service. Just kill an agency. Okay, let's just do it. Oh, shit, this actually works. Well, we need a runtime layer. Should we build or buy? Temporal has it, it's open source. But there's too much bloat — let's abstract away from Temporal, but Temporal still powers it. And we need tracing. And evals. Okay, Langfuse does tracing. Then we tested every fucking tool in the market and they were all garbage, didn't do what we needed. Okay, let's just bake it into the framework, the infrastructure layer. That was the last 18 months — everything we needed to run this company in an AI-native way. And then it was like, hey, we should open source this. This is sick.

**Henry Pray:** Yeah, it's really interesting. The open-source technology infrastructure you're making is what's basically needed now. If you think about the next three to five years, what does competition look like? But that's not what you're selling — that's just something you're offering on top.

**Marcel Santilli:** Yeah, it's not even that we're offering it for what we're selling. It's more like, this is how we work. If somebody else wants to use it, great. But there's also the business opportunity — everybody needs to hire AI engineers and there's not enough of them. This lowers the bar for what an AI engineer needs to know. A junior engineer can be a really powerful AI engineer with this framework, and that's what we have in our forward-deploy team. Junior engineers doing insane custom work.

**Henry Pray:** For the open source — I'm guessing the current skills or scripts running your business, that's kind of your IP along with the data you're collecting. The knowledge on how to do these and set them up. Is that going to be open source as well?

**Marcel Santilli:** Think of it as a framework you can run locally. After it's open source, the next steps are a directory where you can register workflows — privately for your company or publicly.

**Henry Pray:** Yeah.

**Marcel Santilli:** Like Terraform providers, or connectors. All these workflows can be exposed via MCP or API.

**Marcel Santilli:** The biggest friction is deploying this if you want to collaborate around it — that's the cloud-hosted version. But that's not our number one priority. We have three infrastructure engineers who've been working on this for six months, distilling the primitives. Now that it's done, we swapped all our products to use the framework. We'd built the scaffolding and that's what powers the whole company. Then these three engineers took it for six months and figured out all the primitives, got it ready to open source. Now we swapped our product to the framework, which was an upgrade. That's on steroids, man.

**Marcel Santilli:** Daniel can show you, but the OS — what we're calling the platform — goes through your entire site, scrapes every single page every single day, and does all kinds of analysis. It's all workflows. Stuff like that wouldn't be possible otherwise — or it would be a ton of custom code and a nightmare. Having a runtime that can retry things enables everything.

**Henry Pray:** Because there's all this customization — if I think about continuing to build a moat, it would be normalizing learnings. If you're servicing the top payment providers or the top accounting providers, whoever your customers are, are you normalizing learnings and do you have a pipeline to use those for your next customer, specifically for the custom flows?

**Marcel Santilli:** Not yet. But really quickly — the workflow finished running. There's so much stuff here you wouldn't have thought of.

**Henry Pray:** Totally. If I tried to run this through Claude Code right now, it's just going to miss a lot of the "how do you actually productionize this?" or "how do you actually get it working?"

**Marcel Santilli:** Yeah, look at this. Find connections, load interview dictionary, generate entry metadata, update interview dictionary, schema design, prompt design. I need to reset to the latest models, but then there's a testing strategy, and as you load data you can turn it into scenarios as well. It generated this fake one — if you look at the prompts, this is a one-shot, obviously you'd improve this. But it's really good because you can actually run it.

**Marcel Santilli:** Anyway, Daniel can show you a few others. But to your question on learning — right now because we have all the tracing, we're able to see things like pipeline usage. We haven't started to do anything with the pipeline usage data yet, or user activities. All the tracing is there, all the executions.

**Marcel Santilli:** The idea is how do you create a process so that it gets better with every output? You need traces, observability, inputs, context. But you also need the data on the outputs — the pages themselves, which is what we're collecting now. Scraping the pages, understanding them, contextually processing them. And then the outcomes: traffic, engagement, AI visibility, search visibility, conversion events. The OS is one use case, but from that we could technically do any other use case. We're trying to stay focused — we don't have infinite money or bandwidth. But we're so close to closing the loop, and there's no way we could have closed it without this framework.

**Henry Pray:** Yeah.

**Marcel Santilli:** Everything runs on our workflows. Our ability to build them, run them at scale, and learn from them at scale is everything. And it just so happens that content is language. Language is the interface to AI. And language formatted as code is the surest way to use AI to do anything. If you get good at content and coding agents, you get good at everything.

**Marcel Santilli:** Let me give you an example. Lovable. We built workflows and a strategy to programmatically generate website templates and app templates for them. This is a template that was programmatically generated — an entire website. And this is the page that describes it. If you go into our studio, these are the workflows that power it. Kind of gnarly.

**Henry Pray:** So you have a forward-deploy engineer going through and creating each one of these workflows?

**Marcel Santilli:** Yeah, decomposing it into first principles and all of that.

**Henry Pray:** And when you kicked off with Lovable — was that their idea to optimize their templates, or was that you guys?

**Marcel Santilli:** We gave them the strategy, the idea, the execution, the design. We implemented the website, did all the integrations, built the workflows, and did it in four weeks.

**Henry Pray:** And during discovery and onboarding, you're essentially running your other workflows to figure out what are the most searched-for things, what types of templates people would want to see. What to optimize.

**Marcel Santilli:** Yeah, exactly. Those are the opportunities — what templates to generate. The data isn't loading right now, but to give you a sense of what we kicked off for them.

**Henry Pray:** And are you running pre-publish analysis? Like how would this perform for AEO and various other things?

**Henry Pray:** How would this perform for typical click-through rates? You're running that pre-publish as well, and then in real time?

**Marcel Santilli:** Yes and no. What we're building right now is scoring. Every page gets a health score plus scores on content quality, later engagement (traffic, visibility), and then conversion. Those give you an overall page score. And we're scoring opportunities based on intent, relevance, difficulty, brand alignment, and potential traffic.

**Marcel Santilli:** In one sense it's stack-ranking your opportunities — which ones do you go after, why? On the other side it's which pages are the most fucked and what should you do about it? Pretty simple: high value falling off the click cliff — stop everything, go do it. High value with indicators of decline — be proactive. Stable — do nothing. Low value but with unrealized potential and you're close to realizing it — you just need to do these specific things. It's a decision matrix for 5,000 pages: what do you do about it? Plus agents that can actually do those things over time.

**Marcel Santilli:** You have to ingest all this data: analytics, page crawl and processing and semantic understanding, search console and SEO data, AI visibility data (the CheckThat stuff), the brand context that's constantly evolving, the market context and competitors (also always evolving — we're monitoring that, and it costs a lot). Then you have all the possible opportunities, all the inputs and outputs that led to each page, what's happening with that page, the metrics and signals. And now you have all the traces, all the evals. At that point you can actually try to close the loop, which we're this close to.

**Henry Pray:** Do you guys have traditional ML and data science as well for some of the scoring and closing the loop?

**Marcel Santilli:** Jacob — I worked with him at Deepgram — he actually starts next week. He's our principal data science, ML, and AI lead. Daniel, although he's not a data scientist, is pretty up there. And then temporarily, Jacob's partner Katya is a senior data scientist at Mercury. She's been consulting with us and helping because it's a ton of data. But Jacob is next level good.

**Henry Pray:** That makes sense. Do as much as you can through LLMs and scoring, and now that you've created this huge repository of data and outcomes, you can make the scoring that much better. But I assume marketers love scores, so your scoring is probably pretty well received as-is today?

**Marcel Santilli:** Well, transparent about where we are — it's delivered as a service, which allows us to close deals fast and get a lot of revenue. But it's not as sticky as it needs to be. You're still limited to the performance of one human. That human closes the loop of things that don't need to be 100% polished on the tech side, but also hinders your ability to show value because you're only as good as that person's communication in Slack or whatever.

**Marcel Santilli:** That's the jump we're making — how do we expose this platform to people? When we demo this, people are like, "yes, I need this, this is amazing." But then their day-to-day is getting five Google Docs and we publish content for them. And they're like, what's the value of this? That's the gap we're closing.

**Henry Pray:** Got it. So none of your customers are using software you build today?

**Marcel Santilli:** No, it's all our 60 forward-deploy people.

**Henry Pray:** Do you have a framework for how you'd think about deploying to customers? I always think about insights, action, automation. So first, simple dashboards or overview — right now that's in Google Docs and Slack messages, it sounds like.

**Marcel Santilli:** Yeah, that's a good segue. We can jump on with Daniel in a second, but that's what Daniel and I spend most of our mental bandwidth on, along with Ryan Singer, over the last four or five months. How do you simplify this to be an agent-first platform? Not AI bolted on. Not humans first with a bunch of features. Truly, how do we build this differently?

**Marcel Santilli:** That's where we are today. A lot of it comes from learnings of onboarding clients. But the thing that's really relevant to your background is we're sitting on this gold mine with this framework. There are so many companies slapping us in the face to go build things. I think of this as more of a Bending Spoons / Tiny kind of approach to building a company rather than a monolithic Rippling-style platform. Content OS is one thing. GrowthX is one service. Output AI can be monetized and could turn into a Replit and explode. It could also not, but it still powers everything we do. We built this crazy amount of workflows for vetting applicants — that's a startup right there with a recruiter in the loop. There are so many opportunities everywhere, which is exciting but also — how do you manage it all?

**Henry Pray:** I'm putting the pieces together.

**Marcel Santilli:** It's a lot of layers. At first it can be both overwhelming and "why are you distracted?" But it's really just solving our own problems.

**Henry Pray:** Totally.

**Marcel Santilli:** Cool. Hold on, let me check — I think we have a different Zoom. Do you want to jump on that one?

**Henry Pray:** Yeah, give me three minutes and I'll jump on.

**Marcel Santilli:** All right, sounds good, man. See you in a little bit.
