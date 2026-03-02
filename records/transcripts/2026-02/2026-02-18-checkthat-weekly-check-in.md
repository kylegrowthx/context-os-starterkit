# CheckThat Weekly Check In

<metadata>
date: 2026-02-18
time: 20:30 UTC
duration: 48 minutes
organizer: stevie@growthx.ai
participants: Marcel Santilli, Jose Farias, Nigel Hammett, Stevie Kim
fathom_recording_id: 123502417
fathom_url: https://fathom.video/calls/571036697
share_url: https://fathom.video/share/8gs4J3dq61tzrs2f_xVDpvoLM9HUjLMG
source: fathom
enriched_on: 2026-03-01 00:00 UTC
speaker_note: Only 4 speakers actively contributed to discussion; other 5 calendar invitees (Daniel Lopes, Jason Gong, Pedro Steimbruch, Estevão Mascarenhas, Leonardo Carpenedo Steffen) were on the call but did not speak.
</metadata>

---

## Summary

CheckThat is pivoting from a traditional analytics dashboard to a brand research tool that measures AI perception using four composite scores (Presence, Reputation, Perception, Influence)—positioning itself as a "Gartner Magic Quadrant" for AI. The team aligned on immediate priorities: enriching the "Buying Graph" (market and category taxonomy) as foundational work, executing a database migration to support the flexible data model, and shifting product focus to AI-generated snapshot reports. Marcel will finalize the "AO Grader" lead-generation concept by Friday and push updated handbook documentation to the repo.

---

## Context

CheckThat is GrowthX's core software product and strategic bet—a B2B AI visibility index measuring how brands appear in AI model outputs (ChatGPT, Perplexity, Claude, etc.). This internal weekly sync reviews the product strategy, engineering roadmap, and go-to-market priorities for the CheckThat team. The meeting was called by Stevie Kim to align the team on a major strategic pivot: moving from complex dashboards to a qualitative brand research model that treats AI models as a survey audience. User adoption has been minimal so far (only 1 external user invite), but early interest from startups and opportunities to create public benchmark pages are driving momentum. The technical infrastructure needs significant work to support this new direction.

---

## Relevance

**To CheckThat Product & Engineering:**
- Shifting from dashboards to snapshot reports (AI-generated articles with charts) de-risks the data pipeline and simplifies UI development.
- Database migration is the critical blocker—required to support flexible data model for Presence, Reputation, Perception, Influence composite scores.
- Prompt taxonomy and tagging is essential for cost control and determining which prompts run weekly vs. on-demand across different AI models.
- Context Layer (Buying Graph) is the foundational priority—must capture market categories, buying categories, vendors, and analyst insights before scaling probes.

**To GrowthX Business Development:**
- Early user feedback shows strong interest from smaller startups unfamiliar with AI terminology, suggesting addressable market for SMB/mid-market segment.
- Public benchmark pages (comparable to Gartner Magic Quadrant) create SEO value and lead-generation opportunity through the "AO Grader" free report.
- "AO Grader" concept (launched by Friday) validates brand analysis before requiring sign-up—low-risk lead magnet combining deep research with public brand data.

**To GrowthX Delivery & Services:**
- New mental model positions CheckThat as qualitative brand research tool, not analytics tool—shifts how CheckThat can be integrated into client content strategies.
- Snapshot reports with actionable insights (weekly cadence) are more suitable for client communication than complex dashboards.
- Buying Graph approach mirrors GrowthX content strategy work (market research, vendor analysis, category mapping) and creates synergy with B2B content deliverables.

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

**Marcel Santilli**
- Push handbook repo updates; share w/ Jose, Stevie, Nigel

---

## Transcript
**Jose Farias:** Hello again.

**Stevie Kim:** Hey.

**Jose Farias:** Missed you all.

**Jose Farias:** It's been a while.

**Stevie Kim:** It's been a while.

**Stevie Kim:** Oh, update on metrics, because I hadn't checked since Friday.

**Stevie Kim:** One person now has invited someone to their workspace versus zero.

**Nigel Hammett:** Do we know who the invite came from, Stevie?

**Stevie Kim:** Hey, Stevie.

**Stevie Kim:** Hey.

**Stevie Kim:** No, no.

**Nigel Hammett:** Because I sent the invite out yesterday, so I don't know if it was me.

**Stevie Kim:** was me.

**Stevie Kim:** I

**Stevie Kim:** No, I filter out for internal users.

**Nigel Hammett:** Cool, cool, cool, cool, cool.

**Nigel Hammett:** Interesting.

**Nigel Hammett:** Okay.

**Stevie Kim:** Someone just added, you know, someone to their workspace.

**Stevie Kim:** But yeah, not a lot of movement from Friday to today.

**Nigel Hammett:** I hear you.

**Nigel Hammett:** I hear you.

**Nigel Hammett:** I've done three calls now, just in terms of folks that are interested.

**Nigel Hammett:** We have a lot of calls lined up.

**Nigel Hammett:** But yeah, so we'll kind of see how those conversations come about and get some learnings from them.

**Stevie Kim:** Yeah.

**Stevie Kim:** Any feedback so far, especially like around perceived value?

**Nigel Hammett:** Yeah, on the positive side, talking to maybe not our ideal ICP, but those smaller startups, like the smaller brands and businesses, they definitely see the value.

**Nigel Hammett:** They think it's great, you know, just in terms of AOG.

**Nigel Hammett:** I can tell they're not really as familiar, you know, with the terms.

**Nigel Hammett:** And this is kind of an issue.

**Stevie Kim:** Definitely for the pre-launch.

**Stevie Kim:** think this one wasn't canceled because it was a holiday.

**Stevie Kim:** So he moved it and didn't see it.

**Stevie Kim:** But I thought we could keep it one, just given some of your updates you gave Daniel and I Friday.

**Stevie Kim:** Just to give you a little heads up, I just gave the team a super high level overview of, you know, what you've been thinking about.

**Stevie Kim:** And that, you know, with a caveat that you're still shaping it.

**Stevie Kim:** And, you know, just synced on our priorities as far as focusing on some of the growth tickets that we haven't been able to get to.

**Stevie Kim:** And then, you know, we did want to call out that any of the growth tickets we focus on, that takes work away from maybe some of those building blocks that we talked about on Friday.

**Stevie Kim:** So I did want to mention that.

**Stevie Kim:** But I also wanted to mention that in order to have that flexibility that we need to have for the different ways we're aggregating this.

**Stevie Kim:** Data, we're going to have to do a database migration, and that will take a couple of days, and that'll be, like, very heads-down work.

**Stevie Kim:** So we won't get around to some of the, you know, other pieces right now.

**Stevie Kim:** And Pedro's out this week, so we're, you know, down to just two engineers.

**Stevie Kim:** So I just wanted to give a heads-up to everybody about that.

**Marcel Santilli:** Sounds good.

**Marcel Santilli:** I think what I can do is, like, I got a decent chunk done this past, this morning, and this past week.

**Marcel Santilli:** And so I was able to translate some of it into docs for us.

**Marcel Santilli:** And so I can share that and then walk through.

**Marcel Santilli:** And because I think it's, like, important context for everybody, right?

**Marcel Santilli:** Yeah, for sure.

**Marcel Santilli:** And so I got to push the latest changes live, but just know all of this here is available in...

**Marcel Santilli:** The Handbook repo, also in handbook.growthx.ai, and the password is AI-like-growth, all lower caps.

**Marcel Santilli:** And so this is meant to replace our Handbook in Notion.

**Marcel Santilli:** And so this is like all my context files, everything in here.

**Marcel Santilli:** And then these are obviously like the MDX files in MintLify, but then like this repo also has some of my context files and things that if anyone wants to use it for their own stuff that they're doing or to set up like personal operating system agents in Cursor or Cloud Code or whatever you're using.

**Marcel Santilli:** But actually, let me share my whole screen and I can kind of give you all a quick walkthrough of everything.

**Marcel Santilli:** Okay, so this is this, but I'll just show you my cursor.

**Marcel Santilli:** Okay, so what I have here, just so you all see, is like I have like two projects.

**Marcel Santilli:** This workspace, one is my personal context one, and then another one's the handbook, and I've been like translating stuff from my context to the handbook.

**Marcel Santilli:** And then the handbook has like, you know, like some skills and roles, but not a ton, trying to keep it like, you know, both Claude and Cursor compatible.

**Marcel Santilli:** It has some context stuff, like my voice and stuff like that, roles as well, if you want to use it, like when you're like asking to write like documentations on things, you know, it's nice to have like roles that you can, and then some knowledge stuff.

**Marcel Santilli:** And the knowledge is kind of like, it's like, ultimately, like the docs should be the knowledge, but sometimes there may be things that are not quite ready to be docs.

**Marcel Santilli:** It's like, docs is like the ultimately process thing, you know, but then I just, you all understand, like, I'm like my process of like, how I got to this was through my personal context, which was like.

**Marcel Santilli:** This whole gnarly thing I built, which has essentially like context, which is like personal context, roles, and voice.

**Marcel Santilli:** It has docs, which were like the first version of docs.

**Marcel Santilli:** And now most of these is essentially what I put from the, it's like the highlights from Notion, essentially.

**Marcel Santilli:** Like I pull like a bunch of them, but now they're what's in the handbook, right?

**Marcel Santilli:** So the handbook is better than this now.

**Marcel Santilli:** And then I have like essentially a pipeline.

**Marcel Santilli:** So think of pipeline as like, as I'm working on docs, there's like three phases of how I work on docs.

**Marcel Santilli:** It's like scratchpad, research, and then outputs, like when it's ready.

**Marcel Santilli:** And then from outputs, it can get processed into knowledge.

**Marcel Santilli:** And then knowledge is like a study guide, right?

**Marcel Santilli:** Like, so for instance, like here's a, like a study guide I created on writing good prompts, you know?

**Marcel Santilli:** Um, and, and so it's like, um, and, and so this is based on like D.

**Marcel Santilli:** Research I did, it's based on like a bunch of different things, right?

**Marcel Santilli:** Like, so it's like the physics of prompts, like sensitivity, like the architecture of kind of how we monitor prompts.

**Marcel Santilli:** so it's kind of like, think of it as like building blocks, right?

**Marcel Santilli:** Like there's the raw, tons of research, then it's like processed into an output, right?

**Marcel Santilli:** Like, and along the way, it might create like trails, like the agents might be creating like trails of research and notes and things like that.

**Marcel Santilli:** And then it's processed into an output.

**Marcel Santilli:** And then from there, it's like, okay, now I'll take like the context of my company and check that and all this other stuff and create a study guide.

**Marcel Santilli:** And then from the study guide and the knowledge and a bunch of things like, okay, now let's go write like our docs on like how to write prompts, essentially, you know?

**Marcel Santilli:** And so think of like the docs as like all of the stuff happened in order to get to the docs, you know?

**Marcel Santilli:** Does that make sense?

**Marcel Santilli:** I know it's like not quite getting to the point, but it's like, I just want you all to know that like by the time they did the docs, it's not like a one prompt thing.

**Marcel Santilli:** It's like, you know, I spent over a thousand dollars in credit in person in the last week.

**Marcel Santilli:** So just like put it in perspective, it's like, you know, some of these sessions are kind of like gnarly, like there's one here that was like a gnarly one, this one, 21 million tokens, $193.

**Marcel Santilli:** And so it's an early, but okay, so that's that.

**Marcel Santilli:** And then there's like things like records where I ingest a bunch of transcripts.

**Marcel Santilli:** So I have things where like I automatically pull transcripts from Fireflies and then it has a skill that processes them.

**Marcel Santilli:** And so that helps like capture things really quickly.

**Marcel Santilli:** So, so for instance, like I can do like a, I think this one was like a, anyway, don't do it live, but it's like a pull meeting and then it does a bunch of stuff.

**Marcel Santilli:** And then there's like sources.

**Marcel Santilli:** And then what I started to create is like an index of sources I like as well, people I like as well.

**Marcel Santilli:** Sources, I like.

**Marcel Santilli:** And so it's like, it's meant to like, know where to go fetch when doing a deep research, right?

**Marcel Santilli:** And so, okay, so that's that.

**Marcel Santilli:** And so all of this to drive us to the docs, which I'll explain.

**Marcel Santilli:** So overview hasn't changed a whole lot.

**Marcel Santilli:** And, but I would say like, the the main kind of like mental model that has changed is if you think about like brands, right?

**Marcel Santilli:** There's like this whole established market, which is like brand research.

**Marcel Santilli:** So when you do a Super Bowl ad, and you spend, you know, hundreds of millions of dollars on it, you have to measure if it worked or not.

**Marcel Santilli:** Right?

**Marcel Santilli:** And, and what you do is like you do surveys.

**Marcel Santilli:** is you do surveys.

**Marcel Santilli:** Of people in your space.

**Marcel Santilli:** Right.

**Marcel Santilli:** And, and so that's, that's kind of like the, the way you ask people questions, right.

**Marcel Santilli:** In a survey and you see if there's a native recall, right.

**Marcel Santilli:** Or what their perception is of the brand, if they were exposed to an ad and, you know, like all kinds of things.

**Marcel Santilli:** And so it's like a very well-established like practice is like brand research essentially.

**Marcel Santilli:** Right.

**Marcel Santilli:** And, and surveys, right.

**Marcel Santilli:** Like, how do you know when you say like, Hey, there's a, you know, this presidential candidate is going to, is estimated to be at 51% in the polls.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like, like that, that's like pretty well-established except you're serving humans and there's a whole methodology.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like, and so what we're doing ultimately, it's like, if you remember in the all hands last week, right.

**Marcel Santilli:** When I was walking through the mind, the mind map is like, we have three personas and audiences were now influencing.

**Marcel Santilli:** It's the buyer, it's AI agents and it's training bots.

**Marcel Santilli:** Right.

**Marcel Santilli:** And, and so you can think of.

**Marcel Santilli:** Check that as like the ultimate place to figure out like the AI agents layer, right?

**Marcel Santilli:** And agents are the biggest influencers of humans now, more than search.

**Marcel Santilli:** And agents are influenced by a bunch of things, right?

**Marcel Santilli:** But agents don't just do things, they have to be asked to do those things.

**Marcel Santilli:** And so you do need to understand the buyers and the markets they operate in, in order to understand like how AI would answer those things, right?

**Marcel Santilli:** And so that's the framework is like, it's kind of how like we think about it.

**Marcel Santilli:** So in a lot of ways, like what we're trying to measure is the presence, specifically within when buyers evaluate, does AI recommend you?

**Marcel Santilli:** And so that's the question we're trying to answer.

**Marcel Santilli:** Reputation, what does the world think about this brand, right?

**Marcel Santilli:** Within the context of this.

**Marcel Santilli:** Um, this buying category is at the end of the day is like, we're trying to help with buying decisions.

**Marcel Santilli:** That's like the core, right?

**Marcel Santilli:** Like we're not trying to just like generically like measure the world, right?

**Marcel Santilli:** Um, perception, what story does AI tell about your brand?

**Marcel Santilli:** And then how much impact can you have?

**Marcel Santilli:** And how do you impact those three things?

**Marcel Santilli:** Right.

**Marcel Santilli:** Um, and, and so like, that, that's kind of like the, if you will, like the, the, the mental model and, um, and then like the idea here is, like I said, it's like you have checked that does what I just mentioned before the consumers are the AI engines.

**Marcel Santilli:** And then the survey questions are the prompts.

**Marcel Santilli:** The perception is what CHPD, Perplexity, Flaw, Gemini say about the, when buyers ask those things, right?

**Marcel Santilli:** So it's like a, this is the equivalent here.

**Marcel Santilli:** Right.

**Marcel Santilli:** Um, and, and it's like a perfect like analogy essentially, you know?

**Marcel Santilli:** Um, and, and, and,

**Marcel Santilli:** And so we have these kind of like layers that for us to think about, and by the way, none of this is like pivoting the product, right?

**Marcel Santilli:** Like it's just like the foundation we built is like, it's like a next layer of abstraction on that foundation, if you will, right?

**Marcel Santilli:** Like, so the first one, so think of like, there's a foundation layer.

**Marcel Santilli:** So the first layer of that foundation is context.

**Marcel Santilli:** And context is about not just the company context or the buyer context, right?

**Marcel Santilli:** It's like, you have company, you have the products, you have their overall like position, the pricing, the differentiators, the personas.

**Marcel Santilli:** But then you also have like competitor context and market context.

**Marcel Santilli:** And so the market context is one we need to start to do that we haven't done, which is like, I was just on a call with Owen and they're in the like data recovery and backup category, you know, competing with like Cohesity and Rubrics and a bunch of those, right?

**Marcel Santilli:** And

**Marcel Santilli:** And there's, like, very specific context on that market that is, like, not, like, just that brand.

**Marcel Santilli:** That brand is, like, one slice of this broader market, right?

**Marcel Santilli:** And without that, it makes it really hard for us to get to this next layer of intelligence and insights and recommendation, right?

**Marcel Santilli:** And then you have the buyer context, which we're doing it in the context of the individual brands, but we're also not aggregating it yet on the market category, right?

**Marcel Santilli:** And so the way to think about it, by the way, is, and I'll start to use this more, market category is the equivalent of, think of this as market category and think of this as buying category.

**Marcel Santilli:** Does that make sense?

**Marcel Santilli:** Okay, so we can use that language moving forward.

**Marcel Santilli:** It will make it a lot easier versus subcategory.

**Marcel Santilli:** And so think of, like...

**Marcel Santilli:** Yep, spot on.

**Marcel Santilli:** Nigel was on the call.

**Marcel Santilli:** like all of these are the exact ones.

**Marcel Santilli:** It was spot on.

**Marcel Santilli:** So when we get that right, it's like bullseye.

**Marcel Santilli:** Good, right?

**Marcel Santilli:** Okay, so back to this.

**Marcel Santilli:** Then you have, so that's the first layer, it's like context.

**Marcel Santilli:** Well, context, the case, and if you don't have the full picture of the whole market and all the companies and everything else in it, and it's like partial picture or missing, then everything else we're going to talk about will be not as good, right?

**Marcel Santilli:** And it's going to lack.

**Marcel Santilli:** The good thing about this is that this is all SEO juice for us as well, right?

**Marcel Santilli:** And so this is all like distribution for us too, right?

**Marcel Santilli:** And so think of like what we need to do here that's foundational as how do we create a system that's like auto improving, that triggers things, that auto approves, that, you know, like this has to be way more autonomous.

**Marcel Santilli:** Think of it as like we're level two and we need to go to level three and then four, maybe not level five yet, you know, but like for when we have a certain level of confidence, we should be able to do things.

**Marcel Santilli:** We should be able to know when like these five brands clearly belong to the same entity or whatever, right?

**Marcel Santilli:** Like we need to continuously like enrich this.

**Marcel Santilli:** This is like a graph, right?

**Marcel Santilli:** This is like a buying graph, like a buyer's graph.

**Marcel Santilli:** This is like a market graph, you know, of intelligence.

**Marcel Santilli:** And the next one is like where we invested a lot of our engineering efforts, right?

**Marcel Santilli:** It's the instruments, if you will, right?

**Marcel Santilli:** Like it's the prompts aren't random questions.

**Marcel Santilli:** They're research instruments, classify for analysis, right?

**Marcel Santilli:** And so, and then there's like access of like doing this, right?

**Marcel Santilli:** Like there's the market, there's the intent, there's the buying stage, there's the question type, and there's context modifiers.

**Marcel Santilli:** And then there's like measurement purpose.

**Marcel Santilli:** Let me pause here.

**Marcel Santilli:** Does that make sense?

**Marcel Santilli:** Cool.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And like, this is not perfect and this is not set in stone, but I think like the mental model here is solid.

**Marcel Santilli:** And I've been like maturing this for the last two, three weeks.

**Marcel Santilli:** And so like, again, this is not like a one prompt thing, right?

**Marcel Santilli:** Like this is like literally like a lot of thinking into it.

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

**Marcel Santilli:** of like brand overview and then now pricing and reviews to now like creating this like, you know, like the markets, the buying categories, all the vendors within those, if they're missing, like essentially like if you do a deep research, you're using Perplexer or anything and you go like, hey, help, look at what Gartner says about this category, look at what Forrester does, look at all these reputations and then you look at like every vendor mentioned in those, it's like those should be a no-brainer, those who should capture, right?

**Marcel Santilli:** Like there's kind of like that kind of stuff that's just like building some of that logic a little bit, you know, and removing more and more of the bottleneck to continuously make this graph like stronger.

**Marcel Santilli:** And then from this graph, as we start to create these composite scores of reputation and perception and presence, now there's like a way to show it in a way that's like competes with magic quadrants, competes with like, and it becomes a source, right?

**Marcel Santilli:** So at first it's like a source of intelligence and then later on we become the reputations.

**Marcel Santilli:** It's driver for all these categories, essentially, you know, because they are public pages.

**Marcel Santilli:** So then it kind of creates this full circle thing that is, and then the dashboard is like, you know, like the platform itself and the intelligence will be so much easier once you have all these public pages and contacts on all of things, because then you can just like ping those, you know, in return.

**Marcel Santilli:** So a lot of the qualitative stuff, it's like, it's more like one-off deep research snapshots, you know, whereas the probing is actually reducing the burden on the probing, almost, you know, like the probing won't be like tens of thousands of prompts and things like that.

**Marcel Santilli:** In a lot of ways, it's like, it's the categories and getting the categories right, which are valuation and aided.

**Marcel Santilli:** And the other stuff is like 10 or 20, and they, for every brand, it will fit within like a very, like limited scope under 500 prompts per brand, you know, for the paying brands, essentially, you know, or the leaders.

**Jose Farias:** Okay, yeah, that's interesting because you're saying if we need to prove that much less, then there's that much less data to deal with and thus we might not need these very robust data pipelines to render the charts and whatnot.

**Marcel Santilli:** But I think it's like you don't need it for the probes as much, like you need it for the composite scores and the composite scores are going to like summarize them all essentially, right?

**Marcel Santilli:** Like so, so like you don't like in how I'm seeing this, it's almost like the prompt library.

**Marcel Santilli:** It's like, it's like the closet all the way in the back.

**Marcel Santilli:** Like it's advanced mode all the way in the back.

**Marcel Santilli:** Don't worry about it.

**Marcel Santilli:** You know, like in a lot of ways.

**Marcel Santilli:** It's like the drill down as backup, you know, as opposed to having to carry all these charts and computations and things like that, you know, it becomes that there might later on be views that are important where like there's.

**Marcel Santilli:** These very specific like prompts that someone wants to watch like a hawk and things like that, but it will drive a lot more of the rest.

**Marcel Santilli:** And so it's like, and then the other thing is like, if you all look in the OS channel, there is like this concept of snapshots.

**Marcel Santilli:** And so there's a lot of things we can do with snapshots that will be a lot, like almost like kind of a judo move, you know, on things.

**Marcel Santilli:** So think of the snapshots as these like reports that also have charts render, but they're just like a written article with charts, you know.

**Marcel Santilli:** And so the idea is like, there's a lot of things we can do through those snapshots, weekly snapshots, and on a schedule that will tell them how things are changing, the insights, what they should do about it, versus having to create like entire UIs to try to get someone to draw the line, you know, in their heads of what you do about it.

**Jose Farias:** Yeah, I see what you mean.

**Jose Farias:** Okay, I need to sort of digest what that means technically.

**Jose Farias:** It does, I do think it de-risks the data intensive stuff.

**Jose Farias:** The one thing I'll add finally, and that's the end of what I would like to say, is I think there is, there might be an asymmetry of effort to like value in some things.

**Jose Farias:** It sounds like immediately we need to like double down on the context building, you know, with the market context and the buying context and that kind of thing.

**Jose Farias:** That's essential.

**Jose Farias:** And also, that's relatively simple.

**Jose Farias:** And we have the plumbing for that.

**Jose Farias:** So that's great.

**Jose Farias:** We should double down on that.

**Jose Farias:** And then, depending on what I, where I end up with this new information regarding the data and how we're not building like dashboards with complicated UIs anymore, but rather distilling into reports.

**Jose Farias:** I need to think through, like, does...

**Marcel Santilli:** And a lot of what these brands are, these tools are doing, they're coming up with better questions to ask people, or they're creating digital twins of who would be the audience for these brands.

**Marcel Santilli:** And then asking, like, think of it as like, instead of serving a thousand humans, like, why not create like a thousand digital twins of like, you know, humans, and then ask those humans infinite questions, and then take all that data.

**Marcel Santilli:** So like, that is literally what we're doing, right?

**Marcel Santilli:** Like, like, it's very similar to what we're doing, except right now, our focus is not creating digital twins of the buyers yet.

**Marcel Santilli:** It's creating, it's probing the services to within the context of the buying market, the buying category, the market category, and the brands, in order to understand how this one audience, the engines think about it, and will answer it and influence the buyers.

**Marcel Santilli:** And then later on, like, this is a, I can see this being.

**Marcel Santilli:** An area where it goes to.

**Marcel Santilli:** But then because of that, like, this is a good mental model of like, like, this is more of like a qualitative and a little bit quantitative brand research tool than it is like a analytics tool.

**Jose Farias:** That makes sense.

**Marcel Santilli:** So that's one direction.

**Marcel Santilli:** And then the other direction here and at the risk of like, you know, like giving too much away into the future is experimentation, right?

**Marcel Santilli:** And so the next layer, once you get all these insights, is like the A-B testing of it all, right?

**Marcel Santilli:** Like the, like if I create a page, if I do this, will it influence or not?

**Marcel Santilli:** And, you know, like, and, but luckily, like we have the next best thing to an experiment, which is the research, right?

**Marcel Santilli:** That, and because we're already probing and doing all these things, you can draw a lot of the same insights that you would from an experiment by running essentially like a massive.

**Marcel Santilli:** you.

**Marcel Santilli:** Like, like study like this, you know, and, and also we have an AIML, amazing person, Jacob Stardy, I don't know if Daniel announced, but I work with him at DeepGram and he's a badass.

**Marcel Santilli:** He's awesome.

**Marcel Santilli:** So we have help on the way on that site.

**Stevie Kim:** Awesome.

**Jose Farias:** Amazing.

**Stevie Kim:** So I did have a question around, so yeah, yeah, the priorities that I talked to the team about a little bit on Friday and then today are, I think everybody's aligned there.

**Stevie Kim:** The one question I have around the, the brand reports that you were talking about on Friday and you mentioned here, were you going to do any more shaping around those?

**Stevie Kim:** Or did you want me to take what you've done in that larger, bigger picture doc and do the shaping for those different reports that you were wanting us to kind of focus on next?

**Marcel Santilli:** So,

**Marcel Santilli:** I input here from everyone.

**Marcel Santilli:** So HubSpot has this AO grader that is essentially like a really   version.

**Marcel Santilli:** Like, it's so  and it's so bad that the stupid thing has things in Spanish.

**Marcel Santilli:** Like, I don't even know how they  up a prompt so bad that the model returns something in Spanish.

**Marcel Santilli:** Like, I was just like, what the ?

**Marcel Santilli:** Like, you have to try to be this bad.

**Marcel Santilli:** Like, you legit have to try to get this bad.

**Marcel Santilli:** Like, they must be using, like, I don't understand.

**Marcel Santilli:** Like, I don't even know how this is possible at all.

**Marcel Santilli:** But it's so garbage that it's just like, but the ideal scenario is like, we would do this, even if it's manual, like this deep research like I did, right?

**Marcel Santilli:** Using an agent, then combine that with, like, what we already have for that brand.

**Marcel Santilli:** Which is this, you know, and then present it in a kind of like a report or audit that is open, but then they need to sign up to view certain parts of it, right?

**Marcel Santilli:** Like, so this is like super early and I'm trying to make it like a single page, you know, but the idea is like, how do we present this information as a way to validate it?

**Marcel Santilli:** Um, and, and that's kind of like the, the idea, this is literally just taking the mark down, dumping it into V0 and saying like, help me present this information a little bit better, you know, than a Notion doc, you know?

**Marcel Santilli:** So, so I need a little bit more shaping, Stevie and, you know, but, but the, this will solve two things, um, which would be the lead gen and conversion, as well as like holding off on like delivering value and validating before that value is for every user that signs up immediately, you know?

**Marcel Santilli:** And so,

**Marcel Santilli:** So, and it's more like snapshots in some way, but it's more like an AO grader.

**Marcel Santilli:** And so what I'm trying to figure out here, Stevie, is like, is there a way for us to, and this was Daniel's idea yesterday, was just like, is there a way for us to like make that, make the public pages or at least the set of public pages more like that and present it in that way?

**Marcel Santilli:** That way it's like, you're sending them this essentially, you know, which is a public page anyways, or, or there are more things we need to do, you know, to, you know, to present it.

**Marcel Santilli:** And, and, but, but the ultimate thing would be you do AO grader, right?

**Marcel Santilli:** And, and ideally someone comes here and they fill out their information.

**Marcel Santilli:** And when they hit this, we return a version of either this.

**Nigel Hammett:** Outreach and even kind of having those initial phone calls and kind of just sparking that interest.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** So I'm almost there, Stevie.

**Marcel Santilli:** I think by Friday I can have more, but hopefully that doesn't block anything because, like I said, the context, the enriching, the buying categories, the market categories, you know, like all of that, the taxonomy work as well.

**Marcel Santilli:** So because, like, the taxonomy of a prompt and tagging every prompt in our share library will determine, like, which prompts to grab in order to do these, like, you know, composite scores anyways.

**Stevie Kim:** So yeah, no, honestly, it was really more affecting my bandwidth.

**Stevie Kim:** Like, if I was shaping, I wouldn't be able to, like, take on some of the growth tickets.

**Stevie Kim:** If I'm not, I can take on some of the growth tickets so the other engineers can, you know, focus on, like, the more complicated work.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** And then anyone that's working on workflow...

**Marcel Santilli:** I'm going to push the changes right now to the handbook repo, but the docs there, I think, are good context files to use.

**Marcel Santilli:** So, like, if you're, you can even just grab that or just do a symlink if you're using Output AI and use that to plan your scenarios and do things like that, you know, for anyone that's developing workflows.

**Marcel Santilli:** Awesome.

**Marcel Santilli:** Thanks, team.

**Stevie Kim:** We'll talk soon.

**Stevie Kim:** Thanks so much.

**Marcel Santilli:** See ya.

**Stevie Kim:** Bye.

**Jose Farias:** Bye-bye.
