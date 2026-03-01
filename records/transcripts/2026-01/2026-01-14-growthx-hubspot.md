# GrowthX <> HubSpot

---
date: 2026-01-14
meeting_id: 01KESSKHWB5ZNZ45G03689D8NX
fathom_url: https://fathom.video/calls/530886546
duration: 44 minutes
participants:
  - Marcel Santilli (GrowthX)
  - Tyler Pavlas (GrowthX)
  - Jenn Van Dam (HubSpot)
  - Adam Coccari (HubSpot)
  - Aja Frost (HubSpot)
organizer: marcel@growthxlabs.com
host: acoccari@hubspot.com
organizer_affiliation: GrowthX
transcript_url: https://app.fireflies.ai/view/01KESSKHWB5ZNZ45G03689D8NX
enriched_on: 2026-02-28 15:29 UTC
---

## Summary

Strategic product demo call between GrowthX leadership and HubSpot's SEO/AEO team, facilitated by Adam Coccari (HubSpot Ventures connection). Marcel Santilli presented GrowthX's context engineering approach, workflow engine, and client case studies (Lovable, Ramp, Biologica, WebFlow). Jenn Van Dam shared HubSpot's AEO maturity assessment (B grade, A on a curve) and articulated their primary pain points: isolating visibility changes in noisy data, connecting visibility to actions, and balancing content volume with quality standards. The team discussed the December 2024 Google algorithm update and differentiated between shallow programmatic content (penalized) and high-quality programmatic content with product integration (rewarded). GrowthX emphasized optimizing for audience value and human judgment in the loop.

## Context

HubSpot Ventures is an early investor in GrowthX. This call brought together HubSpot's SEO/AEO team (led by Jenn Van Dam, with support from Aja Frost and Adam Coccari as sponsor) with GrowthX leadership (Marcel Santilli, CEO; Tyler Pavlas, operations). The explicit goal: evaluate whether GrowthX's platform could address gaps in HubSpot's current content and visibility infrastructure (XFunnel, Botify, Air Ops, custom in-house tooling). Key backdrop: HubSpot is highly sophisticated in SEO/AEO but facing the same scaling and quality trade-offs that challenge all enterprise content teams.

## Relevance to GrowthX

Tier-1 strategic prospect meeting. HubSpot represents dual value: (1) validation from a mature, credible buyer of AI content tooling, and (2) potential seven-figure enterprise engagement. Outcomes highlight alignment with buyer maturity and reframe GrowthX's code-first philosophy as the answer to complex workflows that low-code tools (e.g., Air Ops) cannot support.

Key learnings:

- HubSpot's technical SEO team is sophisticated—they self-grade B, peers likely rate A—but face the same universal constraints: dirty tracking data, attribution gaps, quality-at-scale tension
- Air Ops limitation is now evident to them: works for templated blog content but cannot handle complex, fact-checked research workflows (e.g., 77-minute research supervisor runs)
- December algorithm update is a live concern; they're reassessing programmatic content strategy and open to approaches that prioritize user value over tactics
- Jenn's question about "how do you actually do it" signals she wants to understand the *mechanics* of quality, not just outputs—this is a strong buying signal
- Aja Frost's presence signals HubSpot marketing integration; follow-up action item routes through her and Adam

## Overview

### HubSpot's Current State

- **SEO Maturity:** Self-assessed at B grade; likely A-level when benchmarked against market. Using XFunnel as source of truth, Botify for technical crawl, custom bot-specific infrastructure.
- **Content Infrastructure:** In-house systems for mass page generation; Air Ops for blog content; experimenting with broader AEO tooling.
- **Primary Pain Points:**
  - **Tracking Noise:** Difficult to isolate visibility gains on high-value queries; data is messy and multi-causal.
  - **Attribution Gap:** Inability to connect visibility changes to specific actions (which content piece? which optimization?).
  - **Quality vs. Scale:** Need high-quality, differentiated content but pressure to ship volume.

### GrowthX's Approach

**Philosophy:** Marketing as context engineering. High-quality context (deep understanding of company, product, market, audience) is the foundation for high-quality content at scale.

**Core Differentiators:**
- **Code-Based Workflow Engine:** Open-source, built on file systems and coding agents. Handles complex pipelines (e.g., 77-minute research supervisor runs with multi-source retrieval and confidence scoring) that low-code tools cannot sustain.
- **Research Supervision:** Multi-agent system with deep research APIs, semantic retrieval over client knowledge bases (graph RAG using Neo4j), and LLM "judges" that evaluate quality against client context.
- **Human in the Loop:** Strategists and editors provide calibration; failure modes are addressed in feedback loops, not hard constraints.
- **Product Integration:** Content is "productized"—embedded with APIs, calculators, templates, or proprietary data. Examples: Lovable's template library, Ramp's vendor database + calculator, Webflow's integration pages.

### Algorithm Update Reframing

**Finding:** The December 2024 update penalized *shallow* programmatic content (low-value listicles, generic comparisons) but not programmatic content itself. Wise.com (234K pages, still ranking), Canva (280M+ monthly visitors, programmatic-heavy) prove scale works when user value is prioritized.

**GrowthX's Counter-Position:** Avoid low-value templates; instead, "productize" content via proprietary data or API integration, creating a superior UX that Google's algorithms reward long-term.

## Key Topics

### HubSpot's AEO Maturity & Challenges

- **Tech Stack:** XFunnel (source of truth), Botify (crawl analysis), custom bot infrastructure for large-scale execution
- **Content Tools:** In-house mass page generation; AirOps for blog workflows
- **Maturity Self-Assessment:** B grade (A on a curve); sophisticated but facing universal scaling constraints
- **Pain Points:**
  - Tracking signal isolation in noisy data
  - Attribution (visibility ↔ action connection)
  - Balancing volume and quality

### Context Engineering & Content Strategy

- **Core Concept:** Understand company, product, market, audience deeply; use that context to prioritize opportunities (competitive gaps, brand mentions, persona needs) and guide execution
- **Methodology:**
  1. Context: Company, product, market, audience artifacts
  2. Strategy: Opportunity prioritization via competitive, citation, persona lenses
  3. Execution: Code-based workflows with human oversight
  4. Optimization: Ingest visibility/engagement signals to decide expand vs. improve
- **Principle:** "Best resource" positioning requires high-quality context as the atomic unit

### Workflow Engine & Research Supervision

- **Problem with Low-Code Tools:** Air Ops works for simple templates but breaks under complexity (e.g., fact-checking requirements, multi-source research, long-running inference)
- **GrowthX's Solution:**
  - File-system-based architecture; enables agent-based workflows (research planning, retrieval, validation, feedback loops)
  - Research Supervisor Agent: Plans research, retrieves from proprietary + public APIs, uses LLM judges to score against client context
  - Knowledge Integration: Graph RAG (Neo4j) over standard vector DBs for semantic retrieval of client data
  - Human Calibration: Editors flag failure modes; feedback is incorporated into next runs
- **Example (Biologica):** Healthcare content with proprietary medical databases; every claim is annotated and sent to doctor review. Net result: <15 min review per article (vs. 45+ min without AI prep)

### Client Examples

- **Lovable:** Template library with 19 AI workflows; integrated into product; users can customize templates, reducing time-to-value
- **Ramp:** Vendor library + per diem calculator; pages embed proprietary data (vendor discounts, category spend trends)
- **WebFlow:** Integration pages and developer site content; fact-checked against API docs
- **Biologica:** Healthcare content; proprietary medical databases; doctor-reviewed; <15 min review per piece
- **CheckThat AI:** 6,000+ programmatic pages powered by proprietary data; positioning as AI visibility index

### December Algorithm Update & Programmatic Content

- **What Happened:** Google penalized *shallow* programmatic content (low-value comparisons, generic listicles). Not a ban on programmatic content itself.
- **Proof:** Wise.com (234K pages, still ranking); Canva (280M+ visitors, programmatic-heavy)
- **GrowthX's Take:** "Productize" content—embed APIs, calculators, proprietary data. User value → algorithm reward. Focus on resilience via quality, not tactics.
- **Risk Example:** Zapier's listicle strategy may face long-term erosion if not paired with product integration or proprietary insights

### Collaboration Potential

- **HubSpot's Angle:** Platform could reduce time-to-quality for content, improve tracking/attribution, provide workflow oversight GrowthX brings
- **GrowthX's Angle:** HubSpot is a reference customer and potential product partner (integration opportunities, co-selling)
- **Next Steps:** Sync between Aja Frost + Adam Coccari, then deeper technical conversations if there's fit

---

## Action Items

### Marcel Santilli (GrowthX)
- **Email Aja Frost** with links to Lovable guides/templates, AugmentCode citations, and CheckThat.ai platform preview (2026-01-14, timestamp 00:13:39)
- **Prepare technical deep dive** on research supervisor workflows and code-based engine for follow-up call with HubSpot team if requested

### Aja Frost (HubSpot)
- **Sync with Adam Coccari** to discuss next steps, timeline, and any internal stakeholder alignment needed re: GrowthX potential collaboration (2026-01-14, timestamp 00:42:29)
- **Update Marcel Santilli** with feedback and outline of HubSpot's decision criteria for tooling partnerships

### Adam Coccari (HubSpot)
- **Support Aja Frost** in evaluation and internal alignment; serve as ongoing liaison between HubSpot and GrowthX teams

### All Participants
- **Stay engaged** for follow-up discussions to discuss test cases, pilot structures, or deeper product integration opportunities

---

## Full Transcript

**Jenn Van Dam:** This meeting is being recorded.

**Jenn Van Dam:** Hey, Adam.

**Adam Coccari:** Hello.

**Adam Coccari:** How you doing?

**Jenn Van Dam:** Good.

**Jenn Van Dam:** How are you doing?

**Jenn Van Dam:** What?

**Adam Coccari:** Everyone's finally feeling good?

**Adam Coccari:** Back to school.

**Jenn Van Dam:** Oh, good.

**Adam Coccari:** Getting invaded by AI note takers.

**Jenn Van Dam:** I know.

**Jenn Van Dam:** There's so many.

**Tyler Pavlas:** Hey, how's it going, team?

**Adam Coccari:** Hi, Tyler.

**Jenn Van Dam:** Good.

**Jenn Van Dam:** How are you?

**Tyler Pavlas:** Good to see you again, Jen.

**Tyler Pavlas:** Nice to meet you.

**Tyler Pavlas:** How's the start of the new year been for you?

**Adam Coccari:** It's been good. We've had some. A lot of sick children, so it was like, we'll fall start and getting them back to school the first week, but now 10 days in, we're all. We're all okay. Back. Back to school.

**Tyler Pavlas:** There you go. There you go. Overcoming challenges in the first couple weeks.

**Adam Coccari:** And you're here in the Bay Area as well, Tyler, is that right?

**Tyler Pavlas:** I used to live out there. I definitely am coming to the Bay Area, like, once every month and a half, two months with this job, but I live in Houston where I was born and raised.

**Adam Coccari:** Oh, nice. Good spot.

**Tyler Pavlas:** Been to Houston?

**Adam Coccari:** I have been. Yeah.

**Tyler Pavlas:** Hopefully not in the summer, but we do have quite the restaurant scene. No doubt about it.

**Adam Coccari:** Good spot. Well, I'll be. I'll be pulling for the Texans. That's good. They look. They look scary the other day.

**Tyler Pavlas:** That defense is fierce.

**Jenn Van Dam:** Yeah.

**Adam Coccari:** Hey, Marcel.

**Jenn Van Dam:** Tyler.

**Jenn Van Dam:** I'm a Pittsburgher, so I don't know how I feel about that.

**Marcel Santilli:** Yeah.

**Adam Coccari:** Sorry, Jen. That was a dagger.

**Marcel Santilli:** Didn't mean to so insensitive, Adam.

**Adam Coccari:** It was.

**Tyler Pavlas:** I'm a closet Cowboys fan because my dad grew up in Dallas and it's like a quarterback in college. So, you know, Texans. I just live here.

**Adam Coccari:** That was my Patriot comment more than anything.

**Tyler Pavlas:** So there we go. There we go.

**Marcel Santilli:** I feel like football, most fans are just, like, fans of hating a team. More than fans of someone. They're more against someone than they're for somebody, you know, it's like, I don't really care as long as that one doesn't work.

**Adam Coccari:** Exactly. That's where I'm at.

**Marcel Santilli:** Awesome.

**Adam Coccari:** Still waiting on Asia.

**Adam Coccari:** There she is.

**Adam Coccari:** Hey, Asia.

**Jenn Van Dam:** Hey.

**Jenn Van Dam:** Oh, my God.

**Jenn Van Dam:** We got so many note takers.

**Adam Coccari:** I know. The army of note takers have just swarmed on us.

**Marcel Santilli:** Yeah, I know. It's like we're testing two different ones. And haven't turned off the other two. And then it's just like. It's like. It's a nightmare. It's. It's always there, you know? But it's a nice layer. Yeah. But so good to connect directly, you know?

**Jenn Van Dam:** Yeah. Yeah. No, I'm Excited to hear a little bit more about the platform.

**Marcel Santilli:** Yeah. Also, I watched a while back your session at Inbound on ao and it was really good. It was like one of the more clear ones that I've ever watched. So great job on that. It was like, very, like, to the point. Good framework, simple, you know, I was. Like, okay, I like this. This is one of the few that. Are not trying to like, overplay or. Underplay and they're just more like grounded, you know. That was really, really good. Great job.

**Jenn Van Dam:** Yeah, thanks so much.

**Jenn Van Dam:** Yeah, it must have been like, like, I speak a lot. Like, not. Not in like, big stages, but like, I'm sure it. It was still a little scary to be in front of so many people. Right. Unless you're like, that's natural to you.

**Marcel Santilli:** I think being a little nervous is kind of, like, part of the creative process. You know, if you're not a little nervous, like, you're not giving it your all. You know what I mean?

**Jenn Van Dam:** Yeah.

**Adam Coccari:** There you go.

**Jenn Van Dam:** Yeah.

**Marcel Santilli:** But anyway, I think, you know, moving forward. I just thought, you know, the way you framed things was very good. So I was excited about this call. We're pumped to be here with you.

**Jenn Van Dam:** Yeah, I'm pumped to be here too.

**Jenn Van Dam:** I think like, at the Inbound. I was really thinking about this. There's lots of people doing ao, but like, most of them are doing it badly. And I think what. What I'm really interested in is, how do people actually do it well? And I remember you mentioning in one of our previous conversations, that you guys have workflow management software, right?

**Marcel Santilli:** Yes.

**Jenn Van Dam:** And I think that's the key differentiator in how do you actually do this well versus just slapping some templates together. So I'd love to hear about that. But yeah. Let me first give you a brief overview of how we think about. Aeo and our maturity in it.

**Jenn Van Dam:** Um, so like, we grade ourselves a B. Um, if I'm honest with myself, that's. That's being generous. I think if the curve is like, like, everyone's really bad at this, then maybe it's an A. Um, but the reality is we use X Funnel as our source of truth. Um, we use Bodify for, for crawl analysis. And then we have a lot of custom, um, bot-specific infrastructure that we've built. And then on the content side, we have, we have these in house systems that we use to, to do mass page creation. And then for blog content, um, we use Air Ops to kind of, to power that. Um, and I think the challenge really for us is, um, it's tracking, right?

**Jenn Van Dam:** Um, it's really hard to isolate, like, visibility changes on the things that really matter to us, which are like, you know, high value queries. And then it's also just really hard to connect, like, visibility changes that you see to any specific actions that you're taking. And then finally, like, there's the, you know, the tension between quality and volume.

**Marcel Santilli:** Yeah, it totally makes sense. You know, it's like, everyone's struggling with that. Um, I think, you know, the whole approach for us is, like, we kind of built this thing called context engineering, right? And it's kind of. The idea is that, um, most content today is kind of, like, generic.

**Marcel Santilli:** But if you take the time to understand what context, like, your customers are operating in, um, you can build a much stronger engine. And that gets to that core question you were asking about earlier, how do you actually do this well? I think the answer is marketing becomes context engineering. Um, and so what we're really trying to do is like, become the best resource for an audience, right? And that means deeply understanding their pain points and their use cases. Um, and then with that context, building an engine that delivers like the highest quality content.

**Jenn Van Dam:** Yeah. I love that. And it's actually. Um, it's actually what we've been doing, I think, you know, with our own marketing and it's kind of the. The driving philosophy, right? It's like, you know, we want to be a best resource.

**Marcel Santilli:** Yeah, exactly.

**Jenn Van Dam:** For our audience.

**Marcel Santilli:** I like that. And so like, the first step of that, you know, is like, getting really structured about context. So like, we work with our clients directly. We're like, what is your company like? What are your products like? What is your market like? What is your audience like? And we really dig in. We're like, okay, we're gonna build out these like, knowledge artifacts and that becomes our North Star. That becomes like, that baseline from which everything runs off of.

**Marcel Santilli:** And then the second step is like, okay, with all that context, let's go identify opportunities. And like, we use competitive lens. We use like, brand mentions and other things. We use, um, you know, persona based types of opportunities. But fundamentally, like, all of that is driven by context. So like, the output of that is like a list of like, I don't know, let's say topics and keywords that we think are really good for your business. And then from there, like, we need to have a really efficient execution engine, right? And this is where, um, the software comes in.

**Adam Coccari:** Got it.

**Marcel Santilli:** Um, and this is where like, um, I think the key part is like, most tools that are out there today are kind of like, um, they're not really designed for like, complex workflows. Um, and so like, we've kind of built, um, like, a code-based workflow engine, right? Um, and it's like, in fact, it's like, um, we're actually going to be open sourcing it, um, pretty soon, I think within the next month. Um, and it allows us to kind of, like, build really complex, um, like, multi-agent, uh, pipelines.

**Marcel Santilli:** And so, like, one example of that is like, um, what we call like, a research supervisor, which is, um, like, a multi-agent system, right? And like, the first part of that is like, the research agent plans out like, what kind of research should be done. And then like, from there, it's like, um, we have agents that retrieve from like, proprietary databases, um, public APIs, things like that. And then like, the last part is like, we have an LLM judge, right? And that judge is like, evaluating like, the quality of that research against your context. And like, that's what ensures quality.

**Tyler Pavlas:** And one more thing, just to add on that is the integration with client knowledge bases. So like, one example is like, we integrated Webflow's documentation into like, a graph RAG system, right? So instead of like, typical vector databases, we can kind of, like, intelligently traverse the knowledge base to get to the most relevant information.

**Jenn Van Dam:** Yeah. Okay, so like, that's. That's interesting because like, I think that's a key question. Like, how do you ensure quality at scale? Like, that's really what I'm thinking about. And so like, this research supervisor, right? Is this like, it's not fully automated, right?

**Marcel Santilli:** No, exactly. So like, the key thing is like, we still have strategists and editors, um, in the loop, right? And so like, they kind of, like, they're, um, they're providing calibration, um, and then feedback, right? So like, failure modes kind of get addressed, um, and then like, that feedback kind of gets incorporated into like, the next runs. And so like, the thing about this is like, it requires, um, like, human judgment, right? And we think like, that's actually like, the key to quality.

**Jenn Van Dam:** Yeah, for sure.

**Jenn Van Dam:** I totally agree.

**Jenn Van Dam:** I think like, that's. That's a really important point. And one of the things I'm thinking about is like, we have, I think, a lot of the components you're describing, right? But like, the thing that we're missing is like, a really efficient execution engine that can kind of, like, orchestrate all those things and ensure that like, the human feedback loops are built in and like, that quality is ensured at scale.

**Marcel Santilli:** Yeah, and like, one thing too is like, maybe like, you're not necessarily missing it, right? Like, maybe you're just like, spread across, um, like, a lot of different vendors. Right?

**Jenn Van Dam:** That's exactly right.

**Jenn Van Dam:** That's the problem. We're like, spread across X Funnel and Bodify and, and all these other tools and infrastructure and like, it's just, it's hard to have one, like, one accountable partner, right?

**Marcel Santilli:** Yeah.

**Jenn Van Dam:** So like, that's one of the reasons like, I'm really interested in this conversation.

**Marcel Santilli:** Yeah, totally makes sense. Um, I think, you know, another thing, um, that I think is really important for your business, um, is like, you know, integration of like, product data, right? Like, we've been working with like, a bunch of companies, and like, the way that we really differentiate is like, we integrate their product, um, data or like, proprietary data, um, into the content. And so like, one example is like, we work with a company called Lovable. Um, and like, they have like, a library of like, templates. And like, the content we created is like, a guides and like, templates, right? And so like, users can kind of, like, come to the site, like, create, like, their own, um, from like, a template, um, right, which like, kind of, like, dramatically reduces their time to value.

**Marcel Santilli:** Um, and then like, another example is like, we work with a company called Ramp. And like, they have this like, vendor library and like, we've created like, content that pulls like, their proprietary data. So like, we created like, a per diem calculator, and like, we populate that with like, their actual data. So like, it's a functional, like, it's a functional page, right? Like, a calculator, um, that like, helps the user, um, right? Um, and like, this is really important because like, um, this is, um, like, the key to like, whether you can actually like, do programmatic content, right?

**Marcel Santilli:** Um, and like, there was like, a December Google update, right? And like, um, the whole thing was like, it kind of, like, penalized, like, shallow programmatic content. Um, and like, there are a bunch of companies like, Wise.com, right? Wise.com has like, 234,000 pages and like, they're still ranking really well. Right? Um, and like, the reason they're still ranking really well is like, because like, they use like, real data, right? Like, they use like, actual currency data. And like, Canva is another example, right? Like, Canva has like, 280, 350 million visitors and like, they're using like, a lot of programmatic content.

**Marcel Santilli:** Um, and like, the thing that like, Google is kind of, like, punishing is like, shallow, um, generic content, right? Like, content that's like, just like, a listicle or like, content that has like, no real user value, right? So like, the way that we think about it is like, we kind of, like, productize the content, right? Like, we kind of, like, embed the APIs and like, integrate the data into the content. Um, and like, this creates like, a superior user experience, right? Um, and that's like, what the algorithm like, rewards, um, you know, in the long run.

**Jenn Van Dam:** Yeah, I think I totally agree with that. And I think like, that's another point where like, I think we're really aligned, right? Like, we want to be, we want to be, like, audience first. Right? Like, we don't want to do things just because they, they drive traffic or they're tactical. Right? Like, we want to make sure that like, the content that we're creating is actually like, going to be valuable and useful to our audience.

**Marcel Santilli:** Yeah, exactly. I love that.

**Jenn Van Dam:** Um, and I think like, you know, there's been a lot of noise about programmatic content, and I think like, to your point, like, the key differentiator is like, whether you're creating like, valuable, um, user valuable content or just like, generic list icles, right?

**Marcel Santilli:** Yeah.

**Jenn Van Dam:** Um, and I think like, we're, we're actively, like, thinking about, you know, how to do that well. So I'm really interested in, like, your approach and like, how you think about integrating proprietary data or like, API-based content into, into your platforms.

**Marcel Santilli:** Yeah. And like, another thing is like, we've been working with like, a healthcare company called Biologica. And like, it's like, it's a great example of like, how deep this can get. Right? Um, and like, what we're doing is like, we're using like, proprietary medical databases. And like, every claim is like, kind of, like, annotated with like, a specific like, research paper or like, a specific source. And like, it gets sent to a doctor for review. And like, the amazing thing is like, the doctor review time is like, less than 15 minutes per article. Right? Um, and like, I think that's like, the thing that like, really like, illustrates like, the power of like, working with the right tools and like, the right kind of like, um, like, engineering, right?

**Jenn Van Dam:** Yeah. That's like, super interesting. I think like, that's a really great example of like, how, like, quality can actually like, scale. Right? Like, because like, without that like, level of like, preparation and like, fact-checking, like, a doctor review might take, like, an hour, right? Like, so like, this is like, a great example of like, how like, the software and like, the engineering kind of, like, enables that quality at scale.

**Marcel Santilli:** Yeah, exactly. And like, the other thing is like, we've been working with like, WebFlow, right? Um, and like, they have like, an integration page where like, um, it's like, a detailed like, integration guide, right? Like, you know, who uses like, this integration? Like, what is it good for? Um, and like, it's like, fact-checked against like, the actual integration API. And like, it's like, completely like, data-driven, right? Um, and like, I think this is like, a really good example of like, how like, product-integrated content like, drives like, value for the user.

**Jenn Van Dam:** Yeah.

**Jenn Van Dam:** And I think like, one thing that I'm thinking about is like, um, like, how do you, like, how do you go from like, one example or like, a few examples to like, like, really scaling that across like, a bunch of different like, use cases or like, different types of content? Like, that seems like, it would be really challenging. Right?

**Marcel Santilli:** Yeah, like, that's like, a really good question. Um, and like, the way that we think about it is like, we're kind of, like, building software that enables like, that kind of like, like, scaling. Right? Um, and so like, the specific thing is like, we're kind of, like, managing the context, right? So like, one thing that I'd like to walk through is like, a specific workflow that we have. Um, and like, this is like, a workflow for, um, for CheckThat, right? Which is like, a company that's like, um, a visibility index, um, right? So like, it's like, we have like, 6000 plus, um, like, programmatic pages. Right? Um, and like, we kind of, like, go through a very specific, um, like, process where we kind of, like, understand what these kind of pages are for, um, right? Um, and like, in this case, like, they're like, you know, they're kind of, like, SEO visibility queries where like, you kind of, like, type in like, a word or like, a phrase, and like, the page tells you like, the visibility. Right? So like, you come in, um, like, let me kind of, like, walk you through what the workflow would be like. Um, so like, you come in with like, a list of like, you know, 1000 queries, right? Um, and like, the workflow, um, kind of, like, processes that, um, like, in a very specific way.

**Marcel Santilli:** Um, so like, the first thing is like, we kind of, like, scrape like, the SERP results. Um, and like, we get like, kind of, like, all the information about the ranking pages and the ranking sites. Um, and then like, the workflow kind of, like, fetches like, the top 10 like, ranking competitors. Um, and like, it sends that like, along with like, the query and like, the company context to like, Claude, and like, it generates like, some copy. Um, and then like, the copy then like, get's evaluated by like, a research supervisor agent. Um, and like, the research supervisor, um, like, actually like, fetches like, data from like, CheckThat's proprietary API. Um, and then like, it kind of, like, validates the, the copy against like, that data. Um, and then like, if it like, fails, um, like, it like, feeds back, and like, the copy gets re-written. Um, and like, the amazing thing is like, we can, um, like, achieve like, a 95% pass-rate after like, the feedback loop.

**Marcel Santilli:** Um, and like, this is like, I think like, a really, um, like, um, interesting example of like, how like, you can, um, like, productize like, programmatic content, right? And like, ensure quality at scale.

**Jenn Van Dam:** Yeah. That's really interesting. So like, it sounds like, um, like, the key insight is like, you're leveraging like, your clients' proprietary data to like, ensure quality, right? Like, that's like, the engine that like, drives that validation. Right?

**Marcel Santilli:** Yeah, exactly. And like, I think the question of like, how do you do it well? Like, it all boils down to like, you know, context and like, good engineering. Right? And like, I think like, the thing that like, makes this possible is like, you know, we have like, a workflow engine that allows us to do like, multi-agent stuff, and like, we have like, you know, proper infra, like, proper infra to like, kind of like, manage these large scale, like, workflows.

**Jenn Van Dam:** Yeah, I think that's like, really compelling. Um, and I think like, let me kind of like, zoom out and think about like, you know, like, what this means for HubSpot and like, how we might like, explore a partnership. Um, so like, you know, you have like, a lot of what we do already, right? Like, we have like, an audience-first philosophy. We have like, um, like, deep context about our business and like, our product. But like, the thing that we're missing is like, a really efficient, um, like, workflow orchestration engine. Um, and like, I think the other thing is, um, is like, the integration, um, of like, proprietary data in like, a way that's like, efficient and like, scalable. Um, and like, I think if we could like, bring those things together, um, like, it could be like, a really compelling, um, like, partnership or like, opportunity.

**Jenn Van Dam:** Um, and like, thinking about next steps, um, like, right now, I think what I want to do is like, I want to like, share this with like, Aja, um, and like, have like, a quick sync with like, Adam, like, you know, to kind of like, think about like, how we want to like, you know, explore this, um, moving forward.

**Adam Coccari:** Absolutely.

**Jenn Van Dam:** Um, and like, you know, I think like, the next thing would be like, um, you know, maybe like, get into like, a deeper technical, um, like, discussion. Um, and then like, you know, if there's alignment, then like, maybe we could like, explore, like, a test case or like, a pilot together.

**Marcel Santilli:** Yeah, absolutely. I think that sounds great. Um, and like, I think, you know, for our end, like, I can, like, you know, send over like, some more, like, resources, um, you know, around like, the platform and like, examples, right? Um, and like, I think like, the other thing is like, we have like, a ton of like, examples of like, Lovable and like, Ramp and like, other like, things we've done, right? And like, I'd be happy to like, walk through like, those with like, um, like, more specificity. Um, and like, if there's any like, questions about like, you know, the code-based kind of like, like, um, like, workflow engine, um, like, we can like, um, walk through like, that.

**Jenn Van Dam:** Yeah. I think that'd be great.

**Jenn Van Dam:** Thanks so much for like, taking the time to like, walk through, like, all of this.

**Marcel Santilli:** Yeah, for sure. Thanks for like, having us.

**Adam Coccari:** Thanks for coming out, everyone. Really great conversation. See you soon.
