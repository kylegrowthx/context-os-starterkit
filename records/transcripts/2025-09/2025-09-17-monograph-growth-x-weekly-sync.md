# Monograph <> Growth X - Weekly Sync

<metadata>
date: 2025-09-17
time: 17:00 UTC
duration: 35 minutes
organizer: matthew@growthx.ai
participants: Matthew Panzarino, Chris Morgan
fathom_recording_id: 87945412
fathom_url: https://fathom.video/calls/412195135
share_url: https://fathom.video/share/7iN3Ncxv7G9XceM8Ds2Pmp3NXPtbRV89
source: fathom
enriched_on: 2026-03-03 10:30 UTC
</metadata>

---

## Summary

Matthew outlined GrowthX's strategy for publishing Monograph content on Reddit using three post formats (utilization rate, time tracking, architect salary) designed with pithy, declarative language and minimal linking to measure LLM visibility impact. Chris requested refinements to post voice ("we" instead of "I") and flagged that Sexton Partners had churned and should be removed from the customer stories ingestion document. Matthew discussed GrowthX's content pipeline—which uses EXA research, a knowledge base built from past research and customer stories, and a feedback loop with validation scores—and recommended that Chris investigate EXA's API for building a local database query system to solve Monograph's content source management challenges.

---

## Context

Monograph is GrowthX's client, engaged for content marketing focused on architecture and engineering audiences. Matthew Panzarino (GrowthX VP of Content/Strategy) and Chris Morgan (Monograph's product/content lead) are iterating on a Reddit content strategy and working through deeper product challenges around content source management and querying. The meeting is part of an ongoing weekly sync where GrowthX walks Monograph through current work, gets feedback on direction, and collaborates on solving technical architecture problems in Monograph's publishing pipeline.

---

## Relevance

**To GrowthX Delivery:**
- Reddit content strategy test: Publishing three post formats on Monograph's Reddit account to measure LLM visibility impact; needs careful experimental design to avoid false signals and track relevant search clusters (utilization rates, time tracking for A&E, architect salaries)
- EXA integration working well: Outperforms Perplexity in detail-orientation; Matthew recommends Chris build a front-end using EXA's API for local database queries
- Content pipeline architecture: Using split guidelines/rules approach with multi-pass validation and confidence scoring to improve agentic reliability; storing artifacts in Redis with vector database considerations as context grows

**To GrowthX Business Development:**
- Account health signal: Monograph actively iterating on strategy and investing in technical infrastructure (customer story management, content querying systems); account appears engaged and growth-oriented
- Knowledge base maturity: Monograph's customer stories resource is competitive advantage Matthew rarely sees; GrowthX explicitly praises this, indicating potential expansion opportunity in content synthesis tooling

---

## Overview

- Matthew presented three Reddit post formats for testing (utilization rate, time tracking, architect salary) designed with pithy, declarative language and minimal linking to match Reddit conventions
- GrowthX's content pipeline uses EXA researcher to create research plans, ingest sources including Monograph's customer stories stored in Redis with query-based retrieval, and validate output with confidence scoring
- Matthew recommended EXA API as a solution for Chris's challenge of managing large context from scattered sources; Monograph exploring modular content packet approach similar to code libraries

---

## Key Topics

### Reddit Content Strategy

  - Developing three post formats: utilization rate, time tracking, and architect salary
  - Posts use pithy, declarative language with minimal linking—matches Reddit conventions better than internal cross-linking
  - Testing voice: "we" (attribution to Monograph) vs. purely factual statements; Matthew leaning toward declarative "this is fact" but open to "we" voice
  - Currently removing TM marks and adjusting tone from "I" to "we" perspective
  - Designing careful experimental metrics to measure LLM visibility impact: tracking search cluster questions (utilization rates, time tracking for A&E, architect salaries) before and after publishing
  - Running three formats in parallel to test performance before full rollout

### Content Generation Pipeline

  - Input phase: Topic, assignment direction, target personas (e.g., engineer), content requirements, sourcing guidelines, hyperlink rules
  - Research phase: EXA researcher generates research plan, formulates questions, executes searches, evaluates completeness (e.g., salary ranges for engineering disciplines + firm sizes), stores results in knowledge base
  - Ingestion: Monograph's customer stories ingested into Redis with query-based retrieval—not whole-context loading but targeted lookups (e.g., "find improvements related to time management")
  - Writing phase: Article draft uses research + direction + guidelines + customer stories artifact
  - Validation: Confidence scoring (Likert scale -2 to +2 on elements) with multi-pass evals; runs 10+ passes for adherence; finding manual calibration examples essential for LLM consistency
  - Knowledge base: Stores past research for reuse; subsequent runs drop from 20 minutes to 2-3 minutes once baseline research established

### Knowledge Management Challenges

  - Problem: Monograph has massive context across support docs, competitor research, customer case studies; can't fit into GUI LLMs
  - Current workaround: Using Cursor for grep-like searches that avoid loading full context
  - Desired solution: Modular content "packets" (like code libraries) that can be loaded independently, with diffs and change tracing (Git-like)
  - Dual need: Raw data storage AND meaning synthesis layer to extract patterns (e.g., "What efficiency improvements are we seeing across payroll, time management, employee management?")
  - Additional requirement: Ability to adapt source context and push to queryable system of record; bridge between raw ingestion and synthesized patterns

### EXA Research Tool

  - Matthew strongly recommends EXA as solution for Chris's content querying challenge
  - EXA performance: Outperforms Perplexity significantly in detail-orientation and depth; finds content behind paywalls and multiple link layers
  - Drawback: May be "too good"—retrieves paywall content that humans wouldn't access; GrowthX considering detuning
  - Cost: Not cheap but acceptable for Monograph's query volume (not millions of queries)
  - Recommendation: Build quick front-end using EXA API (bog-standard) with local database of Monograph's customer stories; can be prototyped with Cursor or Lovable
  - Note: As of October 2024, token context limits were 800 tokens max, now Claude supports 200k+; GrowthX still context-engineering documents to optimize efficiency

---

## Action Items

**Matthew Panzarino (GrowthX)**
- Update Reddit post drafts: remove TM mark after MoneyGant, shift voice from "I" to "we"
- Update ingested customer stories document: remove Sexton Partners (churned client)
- Ask GrowthX team about current best practices for storing and querying content artifacts; relay findings to Chris

**Chris Morgan (Monograph)**
- Investigate EXA API for local content database querying as suggested by Matthew

---

## Transcript
**Matthew Panzarino:** Yeah, no problem.

**Matthew Panzarino:** No problem.

**Matthew Panzarino:** It's actually a pretty, pretty light one because we're publishing, obviously, continuing to publish.

**Matthew Panzarino:** We've got, we've got five more for you this week that'll get published and we'll put a digest in there.

**Matthew Panzarino:** Working on an automation for Airtable so that we just get a digest of the stuff that gets published every week.

**Matthew Panzarino:** I've seen other integrations and I don't like them.

**Matthew Panzarino:** So I'm trying to figure out like a more elegant solution because the normal one is just like vomits all of these.

**Matthew Panzarino:** And because of the way Slack formats it, it it deletes your, your, um, a whole page of context.

**Matthew Panzarino:** And I'm like, yeah, I don't want all that mess.

**Matthew Panzarino:** Cause it, and then it ends up like you're looking for conversations in between and stuff like that.

**Matthew Panzarino:** So I'm trying to find a nice solution.

**Matthew Panzarino:** Just puts a little digest weekly.

**Chris Morgan:** I'm like, Hey, here's the five pieces we published or here's the 10 or whatever it is.

**Matthew Panzarino:** So we'll that done.

**Matthew Panzarino:** Um, Reddit stuff.

**Matthew Panzarino:** Um, so in the agenda, you can use the agenda to look at that.

**Matthew Panzarino:** And Robert could take a look at his leisure.

**Matthew Panzarino:** It's not, you know, a hyper-emergency or anything, but we are kind of dialing in our take on what we think we should be publishing on Reddit.

**Matthew Panzarino:** So you can see a sampling of what we've worked with in the agenda there.

**Matthew Panzarino:** They've got the three Reddit posts, the utilization rate posts.

**Matthew Panzarino:** just, we, that post worked well on the site.

**Matthew Panzarino:** So we thought, okay, let's, let's see what a version of that looks like for Reddit.

**Matthew Panzarino:** Um, and then the time tracking and then, um, architect salary, uh, piece.

**Matthew Panzarino:** Now you'll notice, of course, these are pithy.

**Matthew Panzarino:** They're, they're relatively straightforward, um, pretty declarative language.

**Matthew Panzarino:** Um, there's a handful of things in here.

**Matthew Panzarino:** I'm not super happy about still, like, I don't think we should TM MoneyGant, you know what I mean?

**Matthew Panzarino:** Stuff like that.

**Matthew Panzarino:** So I'm working on that.

**Matthew Panzarino:** Obviously on your site, you would want to do that.

**Matthew Panzarino:** But here on Reddit, it does not feel like the right way to go.

**Matthew Panzarino:** So I actually, I had noted this.

**Matthew Panzarino:** I'm going to put just a quick note in here.

**Chris Morgan:** And this comes from Robert's voice on Reddit, or is it the Monograph account?

**Matthew Panzarino:** Yeah, it is.

**Matthew Panzarino:** So this is from the Monograph account.

**Matthew Panzarino:** So it is a third-person distant, like, Monograph person.

**Matthew Panzarino:** Yes, it would probably be Robert, right, like, as an avatar, but it's not his personal account.

**Matthew Panzarino:** So we want the voice to be a hybrid of, like, hey, we're talking about this from an authoritative place, so you sort of want to attribute that more to a person than an entity, you know?

**Matthew Panzarino:** But it is still, like, on the face of it, like, honest about, like, hey, you know, we're here to talk our book, right?

**Matthew Panzarino:** That post, the time-tracking post, let me look at this one.

**Matthew Panzarino:** Yeah, so the time-tracking post is like finding a core key metric, and then attributing it to a very specific source so people know, like, hey, this is where it came from, and you can click and look at the source.

**Matthew Panzarino:** This is very common on Reddit.

**Matthew Panzarino:** It's like, we, by the way, in all of these, this is one thing we haven't worked out with the pipe, because the pipelines are all keyed to internal link, right?

**Matthew Panzarino:** So we won't actually hyperlink any of this stuff.

**Matthew Panzarino:** Like, they'll just be typically one link per article, like this source link here, or the link to whatever key metric that we'll be talking about.

**Matthew Panzarino:** We don't think that, like, this kind of linking is going to play well on Reddit.

**Matthew Panzarino:** That's a personal take.

**Matthew Panzarino:** I could be wrong, but I don't think so.

**Matthew Panzarino:** This is just not the way that people share stuff on Reddit. Typically, they'll just hammer one link and then talk about it, right?

**Matthew Panzarino:** And then in the Architect Salary piece, this is a slightly different format that we're playing with around the same kind of thing, where it's like, here's a piece of data.

**Matthew Panzarino:** Like, you'll often see this in Reddit posts where it's like, here's a breakdown of the data that we are talking about.

**Matthew Panzarino:** Here's the facts.

**Matthew Panzarino:** And then it's like a hot take or mildly spicy take on it.

**Matthew Panzarino:** And then some CTA stuff where it's like, what do you think?

**Matthew Panzarino:** Like, we really want to know.

**Matthew Panzarino:** Like, is this what you're seeing?

**Matthew Panzarino:** Because it's what we see.

**Matthew Panzarino:** You know, we've got this original data that we've presented with you.

**Matthew Panzarino:** Does it match up with the overall data?

**Matthew Panzarino:** Right.

**Matthew Panzarino:** And we're going to try these three kinds of formats, I think, to start out with and see which ones perform.

**Matthew Panzarino:** You know, see how they play, see how they work.

**Matthew Panzarino:** We're going to start generating more content in this vein and then give you folks some time to look at it.

**Matthew Panzarino:** Think about it, you know, give us any feedback, et cetera.

**Matthew Panzarino:** We are still designing the experiment because we have a data scientist that we're working with to make sure that we are finding ways to properly measure the impact of this.

**Matthew Panzarino:** Because the theoretical impact would be, okay, yes, some direct traffic.

**Matthew Panzarino:** Okay, that'd be nice if there's click-throughs, right?

**Matthew Panzarino:** But obviously the native traffic for the posts, if there's any uptake there, if there's any sharing, that kind of thing.

**Matthew Panzarino:** But then how do we design the experiment so that we have the proper cluster of questions around these topics to measure the LLM visibility impact?

**Matthew Panzarino:** So do we see any movement in this cluster of questions about, like, hey, utilization rates or, you know, time tracking for A&E firms or architect salaries for...

**Matthew Panzarino:** Our architects and engineers, that kind of work needs to be done carefully because I don't want to get any false signals and I don't want to miss any cool signals, you know.

**Matthew Panzarino:** So we're just, working with our data scientists to figure that out and we'll start tracking those clusters just previous to us starting to publish for you on Reddit.

**Matthew Panzarino:** Okay.

**Chris Morgan:** Do you think that we could look at like a different, instead of I?

**Chris Morgan:** Like, if it's coming from Monograph, do you think we should be looking at basically we?

**Matthew Panzarino:** Yeah, we can.

**Matthew Panzarino:** And I went back and forth on that myself.

**Matthew Panzarino:** And I was like, how should we position this?

**Matthew Panzarino:** And there's two ways to tackle it.

**Matthew Panzarino:** We could either do we or we could just take a really declarative stance and basically be like, hey, we're just stating the reality of the world.

**Matthew Panzarino:** Like, this is the fact of it.

**Matthew Panzarino:** There's no opinion here.

**Matthew Panzarino:** It's not like we think.

**Matthew Panzarino:** Or we feel, right?

**Matthew Panzarino:** It's just like this is.

**Matthew Panzarino:** But yeah, I think we is absolutely a fair fallback.

**Matthew Panzarino:** We can tweak it and see how that feels.

**Matthew Panzarino:** I don't think it'd be a huge problem.

**Matthew Panzarino:** Tenses, you know, tenses is or personas is generally not hard to tweak.

**Matthew Panzarino:** So we can do that.

**Chris Morgan:** Great.

**Chris Morgan:** Just a few, just like one call out is like, correct Sexton Partners, they have churned.

**Matthew Panzarino:** Okay.

**Chris Morgan:** And I don't have like a timesheet compliance metric from any other customer.

**Matthew Panzarino:** Oh, okay.

**Matthew Panzarino:** Got it.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** No problem.

**Matthew Panzarino:** And then this actually, um, uh, do you?

**Matthew Panzarino:** So we pulled this from the resource that you have.

**Matthew Panzarino:** Do you edit that resource to elide turn customers or no?

**Chris Morgan:** Yeah, show me that resource.

**Matthew Panzarino:** It's the customer stories document.

**Matthew Panzarino:** The architects and engineers review Monograph.

**Chris Morgan:** Yeah, I actually just took them off.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Out of that?

**Matthew Panzarino:** Okay, great.

**Matthew Panzarino:** This is great because it's just ‑‑ we'll do this.

**Matthew Panzarino:** Update.

**Chris Morgan:** Do you know when you guys are intaking that, are you scraping through, like, to the Vue case study link and also grabbing that content?

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** Do you have a live link to it?

**Matthew Panzarino:** Let me take a look at that really quickly.

**Chris Morgan:** Yeah, here you go.

**Matthew Panzarino:** Yeah, this is that success stories.

**Matthew Panzarino:** So, yes, we do.

**Matthew Panzarino:** Yes, the version of it, that is, you're talking about like the click through where it's like you click in and you see the testimonial or of the case study that's two links down.

**Matthew Panzarino:** We have that customer story, like as an example, these.

**Matthew Panzarino:** I'm going to drop in chat.

**Matthew Panzarino:** So like this, right, is what you're talking about?

**Chris Morgan:** Yeah, basically just the last column has like the case study.

**Chris Morgan:** Sometimes it's a PDF, sometimes it's a.

**Matthew Panzarino:** A website?

**Chris Morgan:** A web article.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** So our researcher does.

**Matthew Panzarino:** EXA does take a look at the.

**Matthew Panzarino:** And this is in its body of things to look at.

**Matthew Panzarino:** So yes, it does take that into account.

**Chris Morgan:** I'm curious how you, if you could, I'd love for you to kind of explain a little bit more on the sources kind of picture.

**Chris Morgan:** Like how does that, you have this, you have this like link and somehow it gets brought in as one of the sources in your pipeline.

**Chris Morgan:** I'm curious how you, how you kind of chart out these sources and then how they get fed into that pipeline.

**Matthew Panzarino:** So I'll show you a little bit here.

**Matthew Panzarino:** So this is an experimental pipeline, but it's indicative of the way we do it now. We have on the input: a topic, assignment direction.

**Matthew Panzarino:** We're targeting it towards specific personas—in this case, the engineer persona, since this is an engineering-driven article.

**Matthew Panzarino:** We include content requirements, sourcing guidelines, hyperlink examples to prevent over-linking, and then send it through the pipeline to the research step.

**Matthew Panzarino:** The research step is an EXA researcher that takes the instructions and executes a series of research phases. It creates a plan, generates questions about what information is needed, executes the research, and provides all the raw material.

**Matthew Panzarino:** Then it evaluates the research: Is it comprehensive? Does it have salary ranges for engineering disciplines and firm sizes? This one succeeded validation with a 0.9 score, and then stores the research in our Atlas pipeline.

**Matthew Panzarino:** The article draft uses the research, article direction, and writing guidelines. We include artifacts like customer stories, proofreader checklists, and guidelines. The linking component handles connections to customer stories and scrapes them for additional information. That's how we ingest sources.

**Chris Morgan:** So EXA, does it only handle just, like, web research, or is it also getting fed effectively, like, our knowledge base?

**Matthew Panzarino:** We have a knowledge base project being built that allows us to store sources we want to reuse. Past research gets added so future articles can leverage it. We can also do one-time ingestions like customer success stories.

**Chris Morgan:** So that's not a just-in-time lookup of the customer story database?

**Matthew Panzarino:** No, it happens at the research phase, but it's not live. We ingest it once, which is why we need to update the document when customers churn. It's not currently live, although we can give EXA your domain.

**Matthew Panzarino:** We can give EXA Monograph's domain as a fact-check and research domain. I haven't found it necessary because we get enough from the knowledge base ingestion. But with regular updates to customer stories, there's an argument for treating it as a more live document, though it slows article generation. Initial runs take about 20 minutes, but once we have baseline research, subsequent runs take 2-3 minutes, so the ingested approach is more efficient.

**Chris Morgan:** That kind of like static doc that where you have ingested the customer stories.

**Chris Morgan:** Is that just a concatenated string of all content in one text file?

**Matthew Panzarino:** Yes, it's markdown-formatted. It's stored in a Redis instance, and then we run a query on that to find data that relates to the story.

**Matthew Panzarino:** Instead of taking the whole document, we query for specific entries—for example, "find improvements related to time management"—and the query returns contextual results like "company X saw a 33% increase in efficiency in this area," which we then use in the article.

**Matthew Panzarino:** Honestly, you're way ahead of the game having this resource—most clients don't. We usually have to extract customer stories from Gong, email, or scattered places and collate them manually. Your customer stories are very well-organized, and from what I've reviewed, the pipeline does a good job picking the right context. It generally nails when an improvement is relevant to the article topic, even if the customer has churned.

**Chris Morgan:** Is it a vector database chunking by meaning?

**Matthew Panzarino:** It's a standard RAG scenario but not vectorized currently. We're actually discussing whether to vectorize because our artifacts have gotten so big—you can't put 5,000 tokens of guidelines into a pipeline and expect consistent results; the model will pick and choose what it adheres to.

**Matthew Panzarino:** The alternative is running massive numbers of validation passes—we do 10+ passes on agentic pipelines to get adherence. Either way, we need to context-engineer these documents. They're 4,000-5,000 tokens each, which is unwieldy. A few months ago we thought artifacts needed to be 800 tokens max, but then Claude released 200k context windows, so our thinking on document size is evolving. For now, we're still figuring out the right balance.

**Matthew Panzarino:** Our approach: split documents into guidelines and rules instead of vectorizing. Guidelines are examples of good and bad writing; rules are specific actions like "put TM after MoneyGant" or "always use brand name Saffron, never generic." Running these in separate workflows rather than one large batch makes validation much more reliable and evaluation easier.

**Matthew Panzarino:** We're still testing this pipeline heavily—not delivering to you yet, but the output is very close. The validator uses a Likert scale confidence score (-2 to +2 on each element) with reports like "multiple MoneyGant references missing trademark" or "missing CTA/FAQ." We don't manually write CTAs and FAQs; instead, we calibrate with examples and let the model adapt them to each article so they feel natural rather than formulaic. The pipeline runs evals iteratively until hitting a high confidence score.

**Chris Morgan:** I need a system that can be live and accessible to our internal team and partners. Last week I was trying to compare our support docs with competitors' support docs—it's massive context that won't fit in GUI LLMs. I can only work with it in Cursor because it greps through files without loading everything into context. But I'm thinking bigger: I want to treat content like code libraries—load in modular packets maintained independently, trace diffs like Git, but also synthesize the patterns across them. I don't want to load everything; I want summaries that let me query across meaning.

**Matthew Panzarino:** Let me ask our team about storage architecture. We use Redis for real-time access, but I can check what we want long-term. I'd recommend you try building a front-end for EXA with a local database. EXA is way better than Perplexity, very detail-oriented, and while not cheap, your query volume is manageable. Fair warning: it's almost too good—it finds content behind paywalls and deep in pages, which can be a problem if Google penalizes paywall access. The API is straightforward, so you could build this quickly with Cursor or Lovable. Try it with your customer stories database and define your key queries. We've had very positive experiences with it so far.

**Chris Morgan:** I'll look into that.

**Matthew Panzarino:** I'll ask about storage architecture on my end too. What are the best practices for content storage and querying?

**Chris Morgan:** Yeah, the core problem is I need to jump into source context, adapt it, and push it to a queryable system of record. It's two layers: raw data and meaning synthesis. With customer case studies, some are long-form, some short-form, but we could extract patterns across them—like "here's what improved payroll efficiency." The challenge is they're not precisely formatted, so we need fuzzy matching.

**Matthew Panzarino:** Right, so you're looking for patterns like "efficiencies in payroll or time management" across case studies with different formats.

**Chris Morgan:** Exactly.

**Matthew Panzarino:** That makes sense. I'm not an engineer, so I'll ask the team and let you know what I find.

**Chris Morgan:** Thanks a lot!

**Matthew Panzarino:** Thanks, Chris. Have a good one!
