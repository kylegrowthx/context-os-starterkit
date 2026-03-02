# CheckThat Weekly Check In

<metadata>
date: 2026-02-18
time: 20:30 UTC
duration: 48 minutes
organizer: stevie@growthx.ai
participants: Marcel Santilli (GrowthX Labs), Jose Farias (GrowthX), Nigel Hammett (GrowthX), Stevie Kim (GrowthX)
actual_speakers: Marcel Santilli, Jose Farias, Nigel Hammett, Stevie Kim
fathom_recording_id: 123502417
fathom_url: https://fathom.video/calls/571036697
share_url: https://fathom.video/share/8gs4J3dq61tzrs2f_xVDpvoLM9HUjLMG
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

Marcel presented CheckThat's new strategic framework: a brand research tool measuring AI perception through four composite scores (Presence, Reputation, Perception, Influence) to create AI-driven buying benchmarks. The team aligned on foundational priorities—building a comprehensive "Buying Graph" of market and product categories, completing a critical database migration, and shifting product focus to AI-generated "snapshots" instead of complex dashboards.

---

## Context

CheckThat is evolving from a generic analytics tool into a specialized market research platform for understanding how AI systems perceive and recommend brands. The core insight is that AI agents (ChatGPT, Perplexity, Claude) are now the primary influencers of B2B buying decisions—more influential than traditional search. CheckThat applies proven brand research methodologies (traditionally used for Super Bowl ad effectiveness measurement) but inverts the research subject: instead of surveying humans, it surveys AI models to understand brand perception during evaluation and recommendation phases.

The strategic framework positions CheckThat as the "AI visibility index for B2B"—analogous to a Gartner Magic Quadrant, but built on real-time AI perception data. The product roadmap is pragmatic: immediate work focuses on building the foundational data graph (categories, vendors, competitive context) before more sophisticated measurement layers. Engineering bandwidth is constrained this week (Pedro out, database migration required), so the team is prioritizing SEO-valuable foundational work over feature development.

---

## Relevance

- **Product Strategy:** New framework reposition CheckThat from dashboard analytics to market research and lead generation (via "AI Grader" reports); clear shift from complex UI to AI-generated insights.
- **Engineering:** Immediate database migration necessary to support flexible data model; estimated 2-3 days of focused engineering time.
- **GTM / Sales:** Early user feedback positive with small startups; terminology barriers ("AOG", "AI visibility") require pre-launch messaging work; multiple outreach calls in progress.
- **Content / SEO:** Building a comprehensive "Buying Graph" serves dual purpose as foundational data AND organic search value.
- **Team Coordination:** Handbook documentation now live and available to team for context, skills, and roles; creates shared language and operating system for workflows.

---

## Overview

- **New Strategic Framework:** CheckThat is now a brand research tool measuring AI perception. It will use four composite scores (Presence, Reputation, Perception, Influence) to create actionable benchmarks, like a "Gartner Magic Quadrant" for AI.
- **Technical Pivot:** The current analytics system is too rigid. A database migration is required to support the new flexible data model. This will be a heads-down engineering task for a few days.
- **Immediate Priority:** Enriching the "Context Layer" by building a comprehensive "Buying Graph" of market categories and vendors. This is foundational for all other work and provides SEO value.
- **Product Strategy:** The focus shifts from complex dashboards to "snapshots"—AI-generated reports with charts. This de-risks the data pipeline and simplifies UI development.

---

## Key Topics

### Current State & User Feedback

  - **Metrics:** Minimal user activity (1 external invite), but internal testing is underway.
  - **User Feedback:** Early calls with smaller startups show strong interest, but they are unfamiliar with terms like "AOG" (AI-Generated Content).
  - **Engineering Bandwidth:** Limited to two engineers this week (Pedro is out). A database migration will consume their full attention for several days.

### New Strategic Framework: AI Brand Research

  - **Core Analogy:** CheckThat is like traditional brand research (e.g., Super Bowl ad surveys), but it surveys AI models (ChatGPT, Perplexity) instead of humans.
  - **Goal:** Measure a brand's presence, reputation, and perception within AI-driven buying decisions.
  - **Four Measurement Vectors:**
      - **Presence:** A composite score for AI visibility during evaluation.
          - **Metrics:** Visibility rate, position, stability, cross-engine coverage.
      - **Reputation:** A composite score from deep research on analyst and peer review sites.
          - **Metrics:** Trust, reliability, innovation, value for money, etc.
      - **Perception:** A structured qualitative score of AI's narrative on a brand.
          - **Method:** Uses 6 key attributes derived from analyzing 50+ analyst reports (Gartner, Forrester) to create a radar chart.
      - **Influence:** How internal and external actions affect the other three vectors.
  - **Benchmark:** A visual chart (like a Gartner Magic Quadrant) plotting Presence vs. Perception, with bubble size representing Reputation.

### Technical & Product Implications

  - **Database Migration:** Required to support the new flexible data model.
      - **Rationale:** The current system assumes a fixed data display, but the new framework requires dynamic slicing and dicing.
      - **Impact:** This is a heads-down engineering task for a few days.
  - **Product Focus Shift:**
      - **From:** Complex, data-intensive dashboards.
      - **To:** "Snapshots"—AI-generated reports with charts.
      - **Rationale:** De-risks the data pipeline and simplifies UI development.
  - **"AO Grader" Lead Gen Tool:**
      - **Concept:** A free, public report that combines deep research with existing brand data.
      - **Function:** Serves as a lead magnet, with some sections requiring signup to view.
      - **Status:** In early development; Marcel will have a more concrete version by Friday.

### Foundational Work: Context & Taxonomy

  - **Context Layer:** Building a comprehensive "Buying Graph" is the immediate priority.
      - **Components:** Company, product, competitor, market, and buyer context.
      - **New Terminology:** "Market Category" (the industry) and "Buying Category" (the specific problem/solution).
      - **Rationale:** A complete graph is essential for accurate insights and provides SEO value.
  - **Prompt Taxonomy:** Crucial for managing the prompt library.
      - **Rationale:** Tags (e.g., `type:perception`, `frequency:weekly`) determine how, when, and with what models prompts are run, which is key for cost control.

---

## Action Items

**Marcel Santilli (GrowthX Labs)**
- Push handbook repo updates to live repo and share access/password with Jose, Stevie, and Nigel
- Continue shaping "AO Grader" report design (lead gen tool); expected completion Friday
- Document and finalize "Buying Graph" architecture and taxonomy for market/buying categories
- Work with Jacob Stardy (DeepGram AIML expert) on prompt instrument taxonomy and tagging

---

## Transcript

**Jose Farias:** Hello again.

**Stevie Kim:** Hey.

**Jose Farias:** Missed you all. It's been a while.

**Stevie Kim:** It's been a while. Oh, update on metrics, because I hadn't checked since Friday. One person now has invited someone to their workspace versus zero.

**Nigel Hammett:** Do we know who the invite came from, Stevie?

**Stevie Kim:** No. I filter out for internal users.

**Nigel Hammett:** Cool. Interesting. Okay, someone just added someone to their workspace.

**Stevie Kim:** But yeah, not a lot of movement from Friday to today.

**Nigel Hammett:** I hear you.

**Nigel Hammett:** I've done three calls now, just in terms of folks that are interested. We have a lot of calls lined up. We'll see how those conversations come about and get some learnings from them.

**Stevie Kim:** Yeah. Any feedback so far, especially around perceived value?

**Nigel Hammett:** Yeah, on the positive side, talking to smaller startups and smaller brands and businesses—maybe not our ideal ICP—they definitely see the value. They think it's great in terms of AI-generated content. But I can tell they're not really as familiar with the terms, and that's kind of an issue.

**Stevie Kim:** Definitely for the pre-launch. This meeting wasn't canceled because it was a holiday, but Marcel moved it and didn't see it. I thought we could keep it, given some of your updates you gave Daniel and me Friday. I just gave the team a super high level overview of what you've been thinking about, with a caveat that you're still shaping it. We synced on our priorities, focusing on some of the growth tickets we haven't been able to get to. Any growth tickets we focus on takes work away from some of those building blocks we talked about Friday. But I also wanted to mention that in order to have the flexibility we need for different ways we're aggregating data, we're going to have to do a database migration, and that will take a couple of days—very heads-down work. Pedro's out this week, so we're down to just two engineers. I just wanted to give everyone a heads-up about that.

**Marcel Santilli:** Sounds good. I got a decent chunk done this morning and this past week, and I was able to translate some of it into docs for us. I can share that and walk through. I think it's important context for everybody. I pushed the latest changes live, and all of this is available in the Handbook repo at handbook.growthx.ai (password: AI-like-growth, all lower caps). This is meant to replace our Handbook in Notion and contains all my context files. The repo also has MDX files in MintLify, and if anyone wants to use it for their own stuff or to set up personal operating system agents in Cursor or Claude Code, that's available too.

**Marcel Santilli:** Let me share my screen and walk through everything. I have two projects: one is my personal context, and the other is the handbook—I've been translating stuff from my context to the handbook. The handbook has skills and roles (keeping it compatible with both Claude and Cursor), some context stuff like my voice and roles, and some knowledge stuff. The knowledge is kind of the bridge—ultimately the docs should be the knowledge, but sometimes things aren't quite ready to be docs yet. So the handbook is better than my personal context now.

I essentially have a pipeline: scratchpad, research, and then outputs when it's ready. From outputs, it can get processed into knowledge, which becomes a study guide. For instance, I created a study guide on writing good prompts based on deep research into the physics of prompts, sensitivity, and how we monitor prompts. Think of it as building blocks—raw research, processed into an output, then used with company context to create a study guide, and then the docs. The docs are everything that happened to get there—it's not a one-prompt thing. I spent over a thousand dollars in credits in the last week; some sessions are gnarly. I have one here with 21 million tokens, costing $193.

I also have records where I ingest transcripts—I automatically pull transcripts from Fireflies and have a skill that processes them. And I've created an index of sources and people I like to know where to go for deep research. All of this drives us to the docs.

**Marcel Santilli:** So the overview hasn't changed a whole lot, but the main mental model that has changed involves thinking about brands through the lens of brand research. There's an established market for brand research—when you do a Super Bowl ad costing hundreds of millions of dollars, you measure if it worked through surveys. You ask people in your space questions to measure unaided recall, perception, and other attributes. That's well-established practice.

What we're doing is adapting that framework but inverting the research subject. If you remember the all-hands last week, we have three personas influencing AI: buyers, AI agents, and training data sources. CheckThat is the place to measure the AI agents layer. Agents are now the biggest influencers of humans—more than search. But agents don't just act; they have to be asked. To understand how AI answers questions, you need to understand the buyers and markets they operate in.

So the mental model: we measure Presence (does AI recommend you when buyers evaluate?), Reputation (what does the world think about the brand in this buying category—we're helping with buying decisions), and Perception (what story does AI tell about your brand?). The framework is simple: CheckThat surveys AI engines instead of humans; prompts are the survey questions; and AI responses are the perception data. It's the perfect analogy.

This is NOT a product pivot—it's a next layer of abstraction on the foundation we built. The first foundation layer is Context. Context includes company, products, position, pricing, differentiators, personas, competitor context, and market context. We haven't done market context yet—for example, data recovery and backup is a market category with Cohesity, Rubrics, and others competing. Without that market context, it's hard to get good insights. We're also doing buyer context for individual brands but not yet aggregating on market category.

Let me use clearer language going forward: market category is the industry (data recovery and backup); buying category is the specific problem or solution (disaster recovery for enterprise). Without the full picture—all companies, categories, context—everything else will be weaker. The good news is this is all SEO value for us too.

Foundationally, we need an auto-improving system that triggers and auto-approves. We need to move from level two to level three or four—the system should know when five brands belong to the same entity, continuously enriching the graph. This is a buying graph, a market graph of intelligence.

The next layer is instruments—prompts are research instruments, not random questions. There are axes: market, intent, buying stage, question type, and context modifiers, plus measurement purpose. This is solid thinking, and I've been maturing it for the last two or three weeks. It's definitely not a one-prompt thing.

**Marcel Santilli:** And then layer three is the measurement.

**Marcel Santilli:** And then the measurement is where probably like the most evolution is going to feel like, whoa, this is different or new or change.

**Marcel Santilli:** Right.

**Marcel Santilli:** And, um, and, and ultimately, like I boil it down into four vectors of measurement, if you will, presence, reputation, perception, and influence.

**Marcel Santilli:** And, um, and so presence is like kind of what we think about today, but, but it's not only visibility.

**Marcel Santilli:** It's, it's, it's trying to, you're still measuring those things by the way, but these are like composite scores.

**Marcel Santilli:** And so presence is about like, um, their AI presence overall.

**Marcel Santilli:** And.

**Marcel Santilli:** It's specifically focused on evaluation stage and unaided, and it's about the visibility rate or presence rate, their position, the stability.

**Marcel Santilli:** It's like 100% versus zero, right, like very unstable, and then cross-engine coverage, right?

**Marcel Santilli:** And the aggregate of that becomes like one single thing that you should worry about, right?

**Marcel Santilli:** And then this is going to click a little bit later.

**Marcel Santilli:** Then reputation is the deep research on what does the external market actually think about you?

**Marcel Santilli:** So this is what I did for Owen, for example.

**Marcel Santilli:** So give me a second.

**Marcel Santilli:** And this is like they are in the cloud backtop and data protection space, you know, and then I did an obscene amount of deep research, essentially going through every single analyst and peer review site out there and report out there.

**Marcel Santilli:** And So Okay.

**Marcel Santilli:** To understand every single category.

**Marcel Santilli:** And then I started to go through every single brand and do the same thing and then define them into this composite score, which is like, so that we can put them into kind of like tiers.

**Marcel Santilli:** Almost like a, this is like the, our version of the Gartner Magic Quadrant, essentially, or the G2 grid, right?

**Marcel Santilli:** Because then it becomes actionable, right?

**Marcel Santilli:** It becomes like real, becomes like, you know, digestible, right?

**Marcel Santilli:** Versus like a bunch of numbers and charts everywhere, right?

**Marcel Santilli:** And so, so that's reputation.

**Marcel Santilli:** Reputation is like, what are analysts saying about like these factors, right?

**Marcel Santilli:** Like trust, reliability, innovation, ease of use, value for money, customer support, security, compliance, stability, integration, thought leadership, product quality, speed, time to value, transparency, customer centricity, things like that, right?

**Marcel Santilli:** And, and that's like their reputation in the market.

**Marcel Santilli:** And it's mostly driven by the analyst reviews and community.

**Marcel Santilli:** Right.

**Marcel Santilli:** And leaders in the space.

**Marcel Santilli:** Right.

**Marcel Santilli:** Then perception is different.

**Marcel Santilli:** So perception is what does the AI say overall.

**Marcel Santilli:** Right.

**Marcel Santilli:** And it's influenced by reputation.

**Marcel Santilli:** And if you have no presence and you're not influencing that, then it like somebody else's.

**Marcel Santilli:** Right.

**Marcel Santilli:** But that's the what is the narrative AI constructs, but across these six buyer relevant attributes.

**Marcel Santilli:** And so what I did is like I did an obscene amount of deep research this past week on every single methodology for all of these, like Forrester Waves, Magic Quadrant, Pure Insights from Gartner, CV Insights, like Giga Ohm, G2, Trust Radius, like you name it.

**Marcel Santilli:** Right.

**Marcel Santilli:** So I analyze over 50 of them and study every single one of them on like, what are the attributes?

**Marcel Santilli:** How do they rank it?

**Marcel Santilli:** What is their methodology, if any, that they talk about publicly?

**Marcel Santilli:** And then distill it down to 10 and then to six attributes.

**Marcel Santilli:** And so these are like the attributes and the reason for.

**Marcel Santilli:** This is because I wanted it to fit into a hexagon radar chart.

**Marcel Santilli:** But there's a seventh one that I was like, ah, but, you know, so it's at six.

**Marcel Santilli:** And so the, think of these as like, these are going to inform the prompts that are then going to tell you like what the perception is.

**Marcel Santilli:** So think of like, Ohm, Eon, or whatever, it's like, okay, the, what is their capability?

**Marcel Santilli:** And there's like very specific questions.

**Marcel Santilli:** What is their value, the ROI and whatnot, right?

**Marcel Santilli:** And so then think of this as like a zero to 10 score on all of these, and then combine makes up a composite perception score.

**Marcel Santilli:** And then you can compare that with all your other competitors.

**Marcel Santilli:** And, and this is more qualitative, but it's structure, qualitative research on your brand and how you're perceived in the market.

**Marcel Santilli:** Make sense.

**Marcel Santilli:** And then influence like.

**Marcel Santilli:** This is kind of like the last one, but it's about like, if you look at the study that Katya already started to do, right?

**Marcel Santilli:** It's like, how do you influence these things, you know?

**Marcel Santilli:** And it's about internal versus external.

**Marcel Santilli:** And so, and then there's like three experience layers here, right?

**Marcel Santilli:** So there's like views, there's like onboarding, it's like, how do you set it up?

**Marcel Santilli:** How do you get it to value?

**Marcel Santilli:** And then there's like intelligence, like essentially like what to do about it, you know?

**Marcel Santilli:** So that's just like the mental model, right?

**Marcel Santilli:** And then the benchmark is ultimately like, I got to figure out what name we're going to use.

**Marcel Santilli:** I'm confident on this.

**Marcel Santilli:** I'm confident on this.

**Marcel Santilli:** Kind of confident on this.

**Marcel Santilli:** And then this, I don't know if it's going to be at risk or something else.

**Marcel Santilli:** But think of this as like, it's three attributes.

**Marcel Santilli:** So it's charting perception and presence.

**Marcel Santilli:** And then the size of the, I need to update this, but the size of the bubble will be reputation.

**Marcel Santilli:** The instrument and the collecting of the data and the context management is foundational to all of this.

**Marcel Santilli:** And then the taxonomy and tagging is super, super, super important because you can't do any of those things.

**Marcel Santilli:** So for instance, if you look at, this one's one I did manually, but the perception prompts, these are brand prompts.

**Marcel Santilli:** And they cannot be mixed in with like, like your evaluation prompts, right?

**Marcel Santilli:** Like this is like, these also don't need to run daily, by the way, you know?

**Marcel Santilli:** And, and so these are more like, they're going to be deeper research prompts.

**Marcel Santilli:** They're going to be like more advanced.

**Marcel Santilli:** They should use better models.

**Marcel Santilli:** They should, you know, and they should run way less frequent, right?

**Marcel Santilli:** And, and, and obviously like, this is like, for the off map ones, like there's a set of players within this map, right?

**Marcel Santilli:** And maybe we need to.

**Marcel Santilli:** We're the number of players because we're going to need to run this for all of them in order for them to be able to compare, right?

**Marcel Santilli:** And so, but because they're weekly, I'm confident, like, we can manage costs a bit more here, right?

**Marcel Santilli:** But you can see, like, there's essentially, like, a whole prompt writing methodology here, right?

**Marcel Santilli:** That is, like, how we think about, like, writing the prompts and the variables in the prompt, the prompt patterns, the, you know, and so the taxonomy and tagging these prompts are going to be really important, right?

**Marcel Santilli:** Like, based on, if you go back here, if you think of, like, I it was the ontology, right?

**Marcel Santilli:** It's, like, the where, what, when, what, who, why, right?

**Marcel Santilli:** Like, and so a prompt is not just a prompt, a prompt has to carry a certain, like, taxonomy that fits within this, like, ontology over here because based on what it is.

**Marcel Santilli:** It determines, like, how it's used, where it's used, how often it needs to be probed, and things like that, you know, and, and so, that's it.

**Stevie Kim:** Thanks, that, that was, yeah, I feel like you've done a lot of thinking just since we last met on Friday, so.

**Marcel Santilli:** All right, I'm really curious, Jose, Estevão, reactions, and.

**Jose Farias:** Fairly optimistic, loving this, this direction, this framing of things, I immediately, my instinct is, like, how to, how to translate it into code, and, like, actual features.

**Jose Farias:** I think it's become evident that, so, the system that we designed for analytics, sort of assumed that we would know, up front, how to display the data that we're capturing.

**Jose Farias:** And this is not how we.

**Jose Farias:** Picture doing it.

**Jose Farias:** It's okay, though.

**Jose Farias:** What that entails is we need to migrate into a new system that Jacopo and I have been talking about for a while.

**Jose Farias:** It's not easy, but it is doable.

**Jose Farias:** And my hope is that it won't take too long, not because it's easy, but because, frankly, we have a very good team.

**Jose Farias:** So all that to say, I think no technical, like, reservations or worries about whether we're going to be able to do it.

**Jose Farias:** We will need a couple days to adjust.

**Jose Farias:** And once we have that, I'm confident we'll have a very flexible system that will allow us to slice and dice the data in any way that we need to render these quadrants and, like, have these views of how brands are performing across different, like, personas, and tags, etc.

**Marcel Santilli:** Yeah, in, um, maybe for whatever.

**Marcel Santilli:** If we think about what we're doing as a graph, at least on the context layer, think of the public pages as delivering value for that graph early on, and so think of it as like, it's not just a pricing page, it's like you're gathering pricing information to determine the grounding truth of that brand.

**Marcel Santilli:** Right, like, or, and so then a lot of it is like, the, the workflow and ingestion of the context.

**Marcel Santilli:** And then there's kind of like, organizing it.

**Marcel Santilli:** And then there's like knowledge extension.

**Marcel Santilli:** And so like, that's kind of like, maybe a way like, so to me, it's like, on the probing stuff.

**Marcel Santilli:** Yes, there's a lot of stuff to do.

**Marcel Santilli:** I think the low hanging fruit here, because it's going to also help with like content and public pages.

**Marcel Santilli:** Is the like, how do we go from, we do an incredible job.

**Marcel Santilli:** We're moving from brand overview and pricing/reviews to creating markets, buying categories, and all vendors within those. If we do deep research using Perplexity—looking at what Gartner and Forrester say about a category and every vendor mentioned—those should be no-brainers to capture. We're building that logic to remove bottlenecks and make the graph stronger. From this graph, as we create composite scores of reputation, perception, and presence, we can show it like a Magic Quadrant. We become an intelligence source first, then a driver for categories because we're publishing public pages. Once we have all these public pages, the platform and intelligence become easier because we can reference them.

Most of the qualitative stuff will be one-off deep research snapshots. The probing is actually reducing burden—it won't be tens of thousands of prompts. For every brand, we're limiting it to under 500 prompts per brand for paying brands or leaders. The categories and getting them right are the key.

**Jose Farias:** If we need fewer probes, that's less data to deal with, so we might not need very robust data pipelines to render charts.

**Marcel Santilli:** Right, you don't need it for the probes as much—you need it for composite scores, which summarize them. The prompt library is like the back closet, advanced mode in the back. Don't worry about it. It's a drill-down backup versus carrying all these charts and computations. Later, there might be specific prompts someone wants to watch, but that's the exception.

And then there's this concept of snapshots. Think of them as reports with rendered charts—written articles with charts. We can do a lot through snapshots, weekly on a schedule, telling users what's changing, the insights, what to do about it. No need for entire UIs forcing users to draw conclusions themselves.

**Jose Farias:** I see. I need to digest the technical implications. I do think it de-risks the data-intensive stuff. Immediately, we need to double down on context building—market context and buying context. That's essential, relatively simple, and we have the plumbing for it. Depending on how this new information changes our approach—moving from complex dashboards to distilled reports—I need to think through the technical implications.

**Marcel Santilli:** What these tools do is come up with better questions or create digital twins of the audience. Instead of serving a thousand humans, you create a thousand digital twins and ask them infinite questions. That's similar to what we're doing, except right now we're not creating digital twins of buyers yet. We're probing services within the context of buying markets, buying categories, market categories, and brands to understand how AI engines think about them and influence buyers. Later, we could expand to digital twins. But the mental model is clear: CheckThat is a qualitative and slightly quantitative brand research tool, not an analytics tool.

That's one direction. The other direction is experimentation. Once you have insights, you want A-B testing—if I create a page or do this, will it influence? Luckily, we have the next best thing: research itself. Because we're already probing, we can draw the same insights from massive research studies. We also have Jacob Stardy, an amazing AIML person from DeepGram, joining us to help with this work.

**Stevie Kim:** Awesome.

**Jose Farias:** Amazing.

**Stevie Kim:** The priorities we aligned on look good. One question: the brand reports you mentioned—do you want to do more shaping, or should I take what you've done and shape them for next focus areas?

**Marcel Santilli:** Let me give input to everyone.

**Marcel Santilli:** HubSpot has an AI Grader that's a really bad version—so bad it returns Spanish text. I don't understand how they messed up a prompt that badly. But the ideal scenario is we do this deep research—even if manual—using an agent, combine it with what we already have for that brand, and present it as a report or audit that's open but requires signup for certain sections. I'm trying to make it a single page, showing information better than a Notion doc. I need a bit more shaping, but it solves two things: lead gen and conversion, plus delivering value and validating before every user signs up gets it.

**Marcel Santilli:** It's like snapshots but more like an AI Grader. Daniel's idea was: can we make public pages more like that? You'd send them this public page, or we do more work to present it better. Ideally, someone does the AI Grader, fills out their info, and we return a version of the report.

**Nigel Hammett:** And the outreach and phone calls help spark interest.

**Marcel Santilli:** Yeah, I'm almost there. By Friday I'll have more, but hopefully it doesn't block anything. The context enrichment, buying categories, market categories, and taxonomy work are key. The prompt library taxonomy and tagging every prompt in our library will determine which prompts to grab for composite scores.

**Stevie Kim:** Honestly, it's more about my bandwidth. If I'm shaping, I can't take growth tickets. If I'm not shaping, I can take them and let other engineers focus on complicated work.

**Marcel Santilli:** Got it. For anyone working on workflows: I'm pushing changes to the handbook repo now. The docs there are good context files. You can grab them or symlink if using Claude Code to plan scenarios.

**Stevie Kim:** Awesome. Thanks, team. We'll talk soon.

**Marcel Santilli:** See you.

**Stevie Kim:** Bye.

**Jose Farias:** Bye.
