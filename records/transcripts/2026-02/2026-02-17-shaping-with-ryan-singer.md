# Shaping with Ryan Singer

<metadata>
date: 2026-02-17
time: 17:00 UTC
duration: 181 minutes
organizer: Marcel Santilli (GrowthX)
participants: Marcel Santilli (GrowthX), Ryan Singer (Basecamp/Shape Up), Daniel (GrowthX)
source: fireflies
fireflies_id: 01KH96HM54F1VYHKVAEH3YHXXE
meeting_link: n/a
transcript_url: https://app.fireflies.ai/view/01KH96HM54F1VYHKVAEH3YHXXE
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

A three-hour product shaping session for CheckThat using Ryan Singer's Shape Up methodology. Marcel and Daniel walked Ryan through the full CheckThat product — the strategic framework, the AI workflow system, Content OS, and the "Learn and Improve" optimization module. The most substantive work happened in the second half: Ryan helped the team define a clear mental model for content optimization (Fix, Improve, Refresh, Replace, Archive) and pushed for a signal-driven UI that surfaces urgent actions upfront rather than making users filter. Phased delivery targeting March was agreed, with Ryan's availability constrained until mid-March.

---

## Context

This is a Shape Up-style product shaping session with Ryan Singer, creator of Shape Up and former head of product at Basecamp. GrowthX is using Ryan as an external product advisor for CheckThat, their AI visibility and content intelligence platform for B2B. CheckThat has two core sides: the public AI visibility index (market monitoring) and the Content OS (internal workflow tool for managing content creation and optimization at scale). Ryan is helping shape the product direction, particularly the "Learn and Improve" optimization module, which is the newest and least defined part of the product.

---

## Relevance

**To GrowthX Services:**
- Content OS directly supports GrowthX's delivery — it's the internal system that powers content work for clients like Lovable, Brex, Vercel, etc.
- The optimization signal framework (Fix/Improve/Refresh/Replace/Archive) will help GrowthX proactively manage content health for all client engagements
- The "Progress Snapshots" concept (status reports showing content health trends) directly maps to client reporting needs

**To CheckThat:**
- Core session for shaping the "Learn and Improve" (optimization) module — the most underdeveloped part of CheckThat
- Ryan's mental model for optimization types is now the canonical framework for the product
- Signal-driven UI concept ("Fix Now", "Unrealized Potential", "Dead Zone") is the direction for March build
- Key data sources: Google Search Console integration underway, quality scores from style/persona alignment
- Ryan's availability: limited until mid-March (enterprise AI integration project); follow-up cadence to be confirmed by March 25th

---

## Overview

- Websites are the single most important growth lever — they influence multiple buyers and AI training simultaneously; manual scaling is impossible, AI automation is the only path
- GrowthX has 300+ AI workflows built on a file-system-based prompt structure; three business layers: CheckThat (market monitoring), Content OS (page creation/optimization), custom agent workflows for clients
- Content OS needs a cleaner separation between **Creation** and **Optimization** — they are fundamentally different workflows and should be distinct in the UI
- Optimization mental model (5 types): Fix Issues, Improve, Refresh, Replace/Refactor, Delete/Archive — each with distinct triggers, signals, and urgency levels
- Key metrics for optimization: Quality, Impressions, Traffic, Engagement, Conversion — with Engagement and Conversion as emerging/future
- UI direction: signal-driven heads-up display ("Fix Now", "Unrealized Potential", "Dead Zone") — no manual filtering; surface urgent items at the top with assignment ownership
- Clustering (by content type, topic, persona) should be nested inside signal categories, not replace them
- March delivery target: minimal viable "Fix Now" category — catch critical issues using existing data; defer clustering and advanced filtering
- Ryan's bandwidth limited until mid-March; follow-up sessions to be confirmed by March 25th

---

## Key Topics

### Strategic Framework: Websites as the Growth Engine

Marcel opened with the big picture: the website is now the most important lever for growth because it influences multiple buyer personas (human and AI) simultaneously. The shift from single-buyer to multi-buyer dynamics means content must be produced at scale and continuously refreshed. Manual production doesn't scale — AI automation is the only sustainable path. The goal is AI-driven production and learning with humans focused on strategy and quality oversight.

### Three-Layer Business Model

Marcel explained the layered architecture of the GrowthX + CheckThat business:
1. **CheckThat** — top-of-funnel market monitoring; the public AI visibility index tracking 10,000+ brands across 200 buying categories
2. **Content OS** — normalized page creation and optimization for clients; the internal workflow system
3. **Custom agent workflows** — complex, client-specific content tasks (e.g., audio-to-transcript, screenshot-to-React, template libraries for Lovable)

The solutions engineering team currently focuses on Content OS calibration but will shift to custom work as the product matures. GrowthX plans to open source the framework and build the agency business on top of it.

### AI Workflow Framework

300+ workflows built on a file-system-based prompt structure using Claude skills and plugins. Enables "mini apps" for specialized tasks — transcription, code conversion, content analysis. Daniel showed an alpha internal UI that decomposes client workloads (like Lovable's template generation) into modular chunks: typography, content generation, image generation. Not intended for public launch yet. Ryan asked for code examples for the audio-to-transcript project to review offline.

### Content OS Interface Walkthrough

Marcel and Daniel walked Ryan through the Content OS product:
- **Workspace setup and calibration** — transcript processing with recipe-driven analysis; paste a meeting transcript, select a recipe (post-sales, kickoff, etc.), generate structured notes
- **Smart views** — cluster pages by taxonomy and metrics; Ryan noted UI bugs and the need for clearer workflow identification
- **Meetings module** — Ryan pushed on the unique value: what does this do that a generic meeting notes tool doesn't? The answer: captures client personas, taxonomy, and competitive intel for calibration — not just notes

### Creation vs. Optimization: The Core Distinction

This was a major clarifying moment. Creation and Optimization are two fundamentally different workflows:
- **Creation**: Brief → Outline → Research → Write → Edit → Publish. Well-understood. The current UI handles this adequately.
- **Optimization**: Ongoing, continuous refinement of existing pages based on signals. Poorly defined. Currently mixed with Creation in "Learn and Improve," causing confusion.

Ryan's recommendation: move all Creation tasks to a dedicated "Create" module. "Learn and Improve" should be exclusively about optimization.

### Optimization Mental Model (5 Types)

Ryan helped the team crystallize five distinct optimization categories:

1. **Fix Issues** — High-severity, rule-based problems that block quality: broken links, multiple H1 tags, missing meta tags, schema errors. These are hard constraints — you can't ship until they're fixed. Binary: either fixed or not.

2. **Improve** — Content quality issues that are addressable post-publication: weak introduction, missing FAQ section, thin coverage. These are style/persona alignment problems. Score-driven.

3. **Refresh** — Updating stale content to maintain freshness signals and prevent ranking decay. Time-sensitive but not urgent in the same way as Fix. Data-driven (last updated, traffic trend).

4. **Replace/Refactor** — Deep rewrite or structural replacement of low-value shallow content. Must consider URL equity — you want to keep the URL, rewrite the content. Distinct from Refresh in scope and effort.

5. **Delete/Archive** — Removing pages with no traffic, no links, no SEO value. Improves crawl budget and overall site quality. Requires human judgment — cannot be automated.

### Key Metrics

- **Quality** — alignment with company style, persona, and content guidelines. Quantifiable via scoring.
- **Impressions** — SEO signal: how many times the page appeared in search results.
- **Traffic** — actual clicks/visits. Indicates whether impressions convert to engagement.
- **Engagement** — time on page, scroll depth, interaction. Emerging metric, needs more development.
- **Conversion** — downstream business impact. Emerging metric, not yet integrated.

Impressions + Traffic are the most actionable pair right now. A page with high impressions and low traffic has unrealized potential. A page with high traffic that's dropping is a red alert.

### Traffic Drop Case Study

Marcel showed a real example: a high-traffic page (Cursor pricing) that experienced a sharp traffic drop due to shallow content — detected too late. This case drove home the need for proactive optimization alerts rather than reactive discovery. The product needs to catch these drops early, flag them urgently, and get them assigned.

### Prioritization Framework

Ryan introduced the realized vs. unrealized opportunity distinction:
- **Realized opportunity** (high traffic, high value) — requires defensive maintenance. A free-fall on these pages is a critical emergency.
- **Unrealized potential** (strong impressions, low traffic) — growth opportunity. Pages that should rank but don't yet.
- **Dead zone** (no traffic, no impressions, no links) — candidates for pruning.

Rule violations on high-impact (realized) pages are always critical. Rule violations on low-impact pages have lower priority.

### Signal-Driven UI Design

Current UI relies on manual filtering, which creates cognitive load. Ryan's recommendation: replace generic filters with a domain-specific "heads-up display" with clear signal categories:
- **Fix Now** — Red. Critical issues demanding immediate attention. Rule violations on high-impact pages. Free-falling pages. Who is on call? Who has this assigned?
- **Unrealized Potential** — Green. Pages with growth opportunity not yet captured.
- **Dead Zone** — Gray. Candidates for pruning or archiving.

Clusters (by topic, content type, persona) should be nested inside signal categories, not replace them. At the "Fix Now" level, flat lists are better than clusters — urgency matters more than organization. Don't hide urgent items inside collapsed clusters.

### March Delivery Plan

Agreed on a phased approach:
- **March target**: Simple, minimal viable "Fix Now" view using existing data. Show critical signals, assignment states, who owns what. No complex filtering or clustering yet.
- Daniel to deliver initial UI mockups and backend implementation to support March release.
- Google Search Console integration underway to feed traffic/impressions data into prioritization.
- Clustering and Smart Views deferred to a future cycle.

### Ryan's Availability

Ryan has a major enterprise AI integration project through mid-March that will limit his availability. He proposed confirming his schedule for ongoing involvement by March 25th. Proposed cadence going forward: 1–2 deep sessions per month + brief weekly check-ins as needed. Marcel to continue sharing materials and problems for Ryan to review async between sessions.

---

## Decisions & Commitments

**Committed Decisions:**
- **Optimization module ownership**: Ryan's 5-type mental model (Fix, Improve, Refresh, Replace, Archive) is now the canonical framework for CheckThat's "Learn and Improve" product
- **UI direction for March**: Signal-driven heads-up display with three primary categories: "Fix Now" (red), "Unrealized Potential" (green), "Dead Zone" (gray)
- **Creation vs. Optimization separation**: Content OS will have a distinct "Create" module separate from "Learn and Improve" to avoid workflow confusion
- **March MVP scope**: Deliver minimal viable "Fix Now" view using existing data; defer clustering, Smart Views, and advanced filtering to future cycles
- **Google Search Console integration**: Underway to feed traffic and impressions data into the optimization prioritization engine
- **Ongoing engagement structure**: Ryan to confirm capacity and cadence by March 25th; target 1–2 monthly deep sessions + async feedback on materials

**Stakeholder Commitments:**
- Ryan: Available post-March 18th; will review code examples and materials asynchronously between sessions; will finalize optimization signal definitions with measurement criteria
- Marcel: Will continue iteration on UI, focus on data pipeline and signal surfacing for March; will share documentation and problems for async review
- Daniel: Will deliver UI mockups and backend implementation for optimization features; will coordinate on future Smart Views and clustering functionality

---

## Open Questions

**Product & Strategy:**
- **Engagement and Conversion metrics**: How will these emerging metrics be integrated into optimization prioritization in future phases? What triggers would warrant changes to the Fix/Improve/Refresh/Replace/Archive framework once these metrics are available?
- **Clustering UI complexity**: Should clustering be nested inside signal categories or offered as a separate filtering layer? How will this affect user mental models?
- **Smart Views scope**: What predefined filters and sorts should be offered in the initial Smart Views launch? How will these evolve based on usage patterns?
- **API integrations beyond GSC**: Which additional data sources (Analytics 4, CMS platforms, competitive intelligence) should feed into the optimization signals in future quarters?

**Implementation & GTM:**
- **Email delivery issue**: Videos demonstrating the AI framework weren't sent to Ryan — how should this be resolved, and what's the async review process going forward?
- **Audio-to-transcript code sharing**: Daniel to provide code examples for Ryan's review — timeline and format TBD
- **Create module design**: How should the "Create" module's pipeline stages (Brief → Outline → Research → Write → Edit → Publish) map to the Backlog, Briefing, Writing, Review states in the initial design?
- **Lovable template library strategy**: How will the template generation workflow (screenshot → React → testing) scale across other client accounts? Should this become a product feature?

**Measurement & Success:**
- **March success metrics**: What would constitute a successful "Fix Now" view launch? How will early adoption and engagement be measured?
- **Optimization impact tracking**: How will GrowthX measure the value delivered to clients via the optimization framework (e.g., traffic recovery, crawl budget savings, quality score improvements)?
- **Ryan's impact attribution**: How should Ryan's strategic input be reflected in product decisions and company attribution?

---

## Action Items

**Marcel**
- Share documentation and context for CheckThat and Content OS with Ryan for async review
- Continue refining the UI for "Learn and Improve" optimization view — focus on data collection and signal surfacing for March cycle
- Share materials and current problems being worked on in CheckThat with Ryan for async feedback

**Daniel**
- Share code examples for the audio-to-transcript project with Ryan
- Deliver initial UI mockups and backend implementation for optimization features for March release
- Coordinate with Marcel and Ryan on Smart Views and clustering functionality for future iterations

**Ryan Singer**
- Review sent videos and materials on the AI framework when email delivery is resolved
- Provide feedback on the "Learn and Improve" workflow — clarify creation vs. optimization paths
- Help finalize key optimization signal definitions (Fix, Improve, Refresh, Replace, Archive) and measurement criteria
- Confirm availability for ongoing deep-dive sessions post-March 18th; update Marcel and Daniel by March 25th

---

## Transcript

**Ryan Singer:** Hey, Marcel.

**Marcel:** All right.

**Marcel:** There you go.

**Marcel:** Hey, Ryan.

**Marcel:** Good to see you, man.

**Marcel:** All righty.

**Ryan Singer:** Good morning.

**Marcel:** There you go.

**Marcel:** Fireflies, right?

**Daniel:** Yes.

**Marcel:** Okay.

**Daniel:** Make sure it's right.

**Daniel:** Yes.

**Marcel:** Fireflies.

**Marcel:** All the note takers and all the recorders, all the things.

**Ryan Singer:** But we're outnumbered.

**Marcel:** Ryan, I—

**Marcel:** You would be proud of me.

**Marcel:** I kind of tried to channel my inner Ryan during our all-hands last week and presented the whole thing in timeline format.

**Daniel:** (overlapping)

**Ryan Singer:** Hey.

**Marcel:** I'm learning from you, my friend.

**Ryan Singer:** All right.

**Marcel:** I should show you.

**Marcel:** Super cool.

**Marcel:** It was actually like—

**Ryan Singer:** Yeah, let's see.

**Marcel:** I thought it was pretty decent. Okay, so I started here with the shift we're seeing—from one buyer to now three buyers, including AI agents that influence those buyers. The reward function is what every company wants: to grow and do more with less. That's about growth on one side, and leverage on the other. So where do you start? We believe the website is your biggest driver. It influences everything. It's what you can control. Most transactions happen here. It compounds if you do it right. It's measurable and drives both growth and leverage. But it's getting harder and harder because there are more pages to feed, more answers needed, and you have to stay fresh and maintain high quality—that's always hard to manage. So the website went from important to existential, and the job got 100 times harder.

**Ryan Singer:** Totally.

**Marcel:** So the job to be done is to drive compounding growth through your website, which means managing pages and creating pages optimized continuously. You keep them organized, current, healthy, and performing. You expand your surface area—more answers for buyers, more content for AI to ingest, more signals for training bots to learn. Every page, continuously. Fresh, quality, relevant, converting. Not once every week—that's impossible to do manually. How do you even know if it's working? You have to think about leading and lagging indicators. Ultimately, the promised land is: AI handles production, optimization, and learning at scale, while humans provide strategy, quality, and judgment where it matters. The system gets smarter. Every output, every page, every week—growth compounds across all three audiences: buyers, AI, and training bots. And then we get into how we actually do this.

**Ryan Singer:** Yeah, so you sort of sold them on the why, and now this is the how—how you actually do it.

**Marcel:** Right. So I try to connect it to what we've built. We have infrastructure, data, platform, services, and distribution—all these layers.

**Marcel:** This is like, anyways, I.

**Marcel:** The house would be much easier if we had the product that I simply into it.

**Ryan Singer:** Yeah.

**Ryan Singer:** So like.

**Marcel:** But anyways, it's been, it's been fun.

**Marcel:** I even got a little pencil trying to of learn from me.

**Ryan Singer:** That's nice.

**Ryan Singer:** I, I realized that I like I need growth fix because like I, I'm not, I'm.

**Ryan Singer:** I'm just doing.

**Ryan Singer:** I'm just doing like real work now and I, I don't, I'm not doing any like teaching or training or anything like that and I, I don't want to spend time on like writing.

**Ryan Singer:** I understood that.

**Ryan Singer:** Basically, like, I don't think I should write the next book.

**Ryan Singer:** I think instead I should have like a, like a lot of articles on my website.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** That like basically captured from all the transcripts I have of answering people's questions and stuff like that, you know, like there's just like so much.

**Ryan Singer:** It's such a no brainer.

**Ryan Singer:** There's like, so there's so much like.

**Marcel:** Raw material for free.

**Marcel:** We actually just dropped one of the ones that we were helping for a while that was like kind of like a partner and we were doing essentially like a pro bono if you will, because it's like a, it was cool work but we should, we should think about that because.

**Marcel:** But anyways.

**Ryan Singer:** Yeah, but it's interesting to like feel the problem.

**Ryan Singer:** It's so clear that the problem is literally getting all the material out there and doing it strategically. You guys help with the front-loading, but then there's all the work of writing the articles and everything. Even when you have a lot of source material and you know what you want to say, it's a lot of effort. I totally get it.

**Marcel:** Yeah, I've been doing the same thing. I just built a company, and I had my context project with all my files, knowledge, everything. I was trying to massage it into a handbook, but because I had so much good context, I was able to write essentially 70 doc pages—the equivalent of a handbook like GitLab's—in basically a single day. It's the same setup you have with Minclify and markdown files.

**Ryan Singer:** Yeah.

**Marcel:** I gotta clone your skills still. It's on my to-do list.

**Ryan Singer:** So what's on the docket for today?

**Marcel:** Did you have time to watch the first video I sent you—the shorter one? I sent it yesterday around midnight.

**Ryan Singer:** You know, I actually didn't get an email from you.

**Marcel:** Huh. Maybe I didn't send it. Let me share my screen.

**Ryan Singer:** Which AI secretary do we have to fire? This is literally the best thing I've seen. *[Screen share showing a humorous AI email notification]* So there are still some issues.

**Marcel:** The dog ate my homework, Ryan. *[Looking at the screen]* Every time I see this guy, I'm like, oh, is he a rapper? Oh my God, that's amazing.

**Marcel:** Okay, so maybe I walk you through the.

**Marcel:** Through the progress that we've made.

**Marcel:** Just to give you context.

**Marcel:** I also.

**Ryan Singer:** Yeah, let's do that.

**Marcel:** Automating your workflow for like showing how the framework works and using your workflow as an example.

**Marcel:** Basically a scaffold.

**Marcel:** The thing is, the way to think about is like we have this AI framework that's all file system based, so prompts tracing the workflow.

**Marcel:** The steps of the workflow are all in code and in the file system.

**Marcel:** And we have a bunch of Claude skills and plugins that sits on top of this.

**Marcel:** So think of it as like a rail scaffold, but like on steroids.

**Marcel:** And you can essentially just create almost anything by just talking to it.

**Marcel:** So I did that in the video.

**Marcel:** So that's the second video.

**Ryan Singer:** Well, yeah, so if you can just send me the email once the blocking issue is fixed, then I'll spend time checking that out, you know, off the call, because probably it's not relevant for you guys for the time we have now, but I'll look forward to seeing that.

**Marcel:** Yeah, that is actually like another project.

**Marcel:** So we have these three things happening.

**Marcel:** We actually could talk about that at the end, but we have.

**Marcel:** There's something we're doing on Check that.

**Marcel:** That's like top of funnel and I saw you try to use Team Builder and like you check out the website and maybe we can go through that a little bit today.

**Marcel:** At a high level, we have CheckThat, which is top-of-funnel market monitoring—tracking how LLMs perform across different domains. And then on the other side, we have the Content OS, which we've been working on. Underneath both of these, we have the framework, and we've been doing a lot of custom work for content creation. That's much harder than normal pages and not possible to do in the basic Content OS. So we have a team of five people—our solutions engineering team. They decide: does this go into the standard Content OS pipeline or does it require custom agent work? And we want to grow this business pretty aggressively, building an agency on top of it once we open-source the framework. To give you an example of the kind of work we do: Lovable is a great one. They came to us with an idea. We used the framework to investigate all the activity on a competitor similar to Lovable, one of our existing clients. We realized that users were struggling with prompting. So instead of asking people to write prompts, we thought: can we create a catalog of templates they can start from? The problem is that Lovable's one-shot output isn't high-quality enough—you need a back-and-forth conversation. So we had to create not just templates, but pages around each template. We ended up creating a "Discover Templates" experience.

**Ryan Singer:** So the issue is that Lovable users—the people using the Lovable product—didn't know how to prompt?

**Marcel:** Exactly. They're trying to get something good, but they don't know how to prompt, and all the user-generated content is pretty garbage. These are Lovable's end users.

**Ryan Singer:** Got it. Yeah, I know this problem. People don't know how to prompt. It's garbage in, garbage out.

**Marcel:** Right. And from an SEO and growth perspective, Lovable is competing with Wix. Wix acquired Base44, one of Lovable's competitors, and they have millions and millions of visits—all because they have templates. Templates are a huge traffic driver for Wix and Squarespace. They understood this dynamic very well: if you don't give people a starting point, they don't know what to do. So we said, let's create a template library—more like a starter kit library. But how do you build that without a network of highly qualified designers working from a reusable foundation? You end up with garbage prompts. So we gave Lovable the strategy on how to think about it, created the experience, and built the individual template pages. And then Daniel will show you how we've programmatized the entire process—from ideation all the way to a fully built website. We went from seven hours of design engineers prompting, tweaking, and polishing down to about an hour now.

**Ryan Singer:** Because this isn't something you can just do in a markdown file—it requires custom orchestration.

**Ryan Singer:** And the in was it content os but you needed to actually build out this custom workflow using output AI in order to orchestrate all that.

**Marcel:** Exactly, yeah.

**Marcel:** So we have this normal editorial clients that need normal pages on the website.

**Marcel:** That's fine.

**Marcel:** That's what we optimize and condent OS for.

**Marcel:** And then we have a bunch of clients that are like I need to create something that's very different or something that's very specific to my needs.

**Marcel:** In this case for lovable was like an agent that would have a back and forth, receive a screenshot, have a back and forth, turns the screenshot into react code and then test it with logo API to see if it's live.

**Marcel:** So like that is one another thing we do for Airbyte similar ideas.

**Marcel:** Airbyte has a bunch of plugins.

**Marcel:** When a plugin gets shows up in their app store we send a pull request if the documentation becomes a page on the website.

**Marcel:** So like we do a plugin like this, they're very, very unique and it's only possible because of the framework.

**Ryan Singer:** Yeah, I get it totally.

**Marcel:** And we're going to grow that team.

**Marcel:** We have four or five people there.

**Marcel:** As we finish the content OS to be like more self serving product, the solutions engineer team can shift to be an engineering team for this kind of custom work on top of the framework.

**Marcel:** Wow.

**Marcel:** So we have these three things in motion.

**Marcel:** The top of the product check that the content OS to normalize pages and intelligence on top of Your website and output AI for any kind of content or like any kind of agent in general.

**Marcel:** But we're trying to start with just focused on.

**Marcel:** Yeah, if you go to the studio and, and show them like the 27 workloads that power.

**Marcel:** This is pretty cool.

**Marcel:** You just search for lovable.

**Marcel:** So check this out, like lovable templates.

**Marcel:** These are all the different workflows decomposing it.

**Ryan Singer:** So is this a front end to output AI or what?

**Marcel:** Yeah, this is alpha that we're not going to launch.

**Marcel:** It's just for our internal inspection and then because we didn't have the time to make this look like legit and fine.

**Marcel:** So we're going to launch just the code part.

**Marcel:** But essentially we have like 27 chunks of code that we wrote for them specific to this problem.

**Marcel:** So like figuring out the typography, the actual words that go on this, these starter kit websites, the structure, the like page structure, the content generator, the image generator, the like, you know, like there's a cleanup part.

**Marcel:** There's like there's all kinds of things that are like essentially decomposing the process of building programmatically.

**Ryan Singer:** This reminds me of what is this, is this different from what like the DAS PI guys are talking about?

**Ryan Singer:** Like when they're like this idea of like you're supposed to kind of like break apart all of this like prompting and stuff into modular pieces.

**Ryan Singer:** This is like a different take on that.

**Ryan Singer:** Similar thought.

**Marcel:** Yeah, it's similar idea.

**Marcel:** DSPI has a lot of the self improving part of the prompts and our take was more like instead of thinking about the prompts, should we think about the workflow itself?

**Marcel:** Because sometimes you need.

**Ryan Singer:** Right.

**Ryan Singer:** Yeah.

**Ryan Singer:** So yeah, this is, this is more like, this is more like a practical software build like standing up systems stuff.

**Ryan Singer:** Right.

**Ryan Singer:** Like huh.

**Ryan Singer:** Yep.

**Marcel:** So you see that I will send you the code for the one that I did for the audio to transcript.

**Marcel:** Cool.

**Marcel:** And so it's essentially mini apps.

**Marcel:** They're like heavy on LLMs.

**Marcel:** So there's instead of like Views and Rails you have a prompts dot prompts file that has all the settings for temperature, the variables, the interpolation, everything and has all the things for like retrialing when LLMs fail has the judgment to go back and LLM is beyond below quality.

**Marcel:** So there's all these things baked in and the UI is essentially you don't have to code but you can if you want to.

**Marcel:** So.

**Ryan Singer:** Yeah.

**Marcel:** Cool.

**Marcel:** So this is a whole thing that we have like.

**Marcel:** So we have this user interface, we have like 300 plus workflows.

**Marcel:** Some are very custom to some clients.

**Marcel:** And then all the AI features that we're talking about on the contentos are also powered by the framework.

**Marcel:** So anyway, the plan is to launch the framework in this next month, and then we're going to grow the engineering team around this custom work for some of the more premium clients.

**Marcel:** And we start hiring solutions engineers for the content OS to do the workspace calibration and then kind of like split the lanes more clearly.

**Marcel:** So those are like essentially three business, three layers of the business that we have that I wanted to show you real quick just to give you the context.

**Ryan Singer:** Awesome.

**Marcel:** Yeah.

**Marcel:** So out of our session last time.

**Ryan Singer:** Hey, what is this new stuff?

**Marcel:** Yeah.

**Marcel:** Oh, man.

**Marcel:** Yeah.

**Marcel:** So out of your session last week, we changed everything and decided to redesign the whole product.

**Marcel:** Okay, real quick.

**Marcel:** Daniel doesn't sleep.

**Marcel:** Yeah.

**Marcel:** So the idea pretty much took what you share your ideas and try to implement here.

**Marcel:** So the setup now is two screens will take you to the place that you, you want, you want to do the work.

**Marcel:** And you can add notes if you're skipping or for whatever reason, even if you're not skipping.

**Marcel:** It's good to have the solutions team that will be setting up the workspace to explain what they did and then if it does not apply.

**Marcel:** So same idea from before.

**Marcel:** And then as you complete, you would like, finish the bar here at the top.

**Marcel:** I went ahead with exactly the same menu that we had thought about.

**Marcel:** So, like, learning, improve, learn and improve will be all of your pages, including the ones that are getting built.

**Marcel:** New page opportunities for new page opportunities and progress snapshots, essentially the report.

**Marcel:** There's like a few things that we have from the legacy project that folks are still going to be using for a while.

**Marcel:** That's the Airflow project.

**Marcel:** This is here just as.

**Marcel:** I don't even know if we're going to keep it.

**Marcel:** But that's the old analytics might be usable for inspecting if you're getting the data there or if like just poking around, but maybe we don't even have to surface.

**Marcel:** And then I also added meetings.

**Marcel:** Meetings is one thing that, as we were discussing last week, a couple of weeks ago, it was a challenge of like, not always you can just let AI do the research.

**Marcel:** There's like a lot of things that comes from the sales meetings for the intake, meetings with the client, the kickoff meeting with the client.

**Marcel:** They're sharing things of like, who are the competitors, who are their Personas.

**Ryan Singer:** And you're asking the right, you're asking the right questions to draw out things that they wouldn't have shared otherwise.

**Ryan Singer:** I totally have this in my workflows too.

**Ryan Singer:** Like, I have these interviews with people, and those interviews are like the gold that I need, like to extract like key requirements from and stuff like that.

**Marcel:** Yeah, exactly.

**Marcel:** So, like this I added last week.

**Marcel:** So the idea is something super simple for now that you would just like paste the transcript and you'd pick a set of recipes and the recipes would be like, for post sales, post kickoff, there's a set of like, things that we look for and it would process and create a bunch of notes out of those transcripts.

**Marcel:** But that's just one of the things that the calibration team would add here manually.

**Marcel:** But before they trigger the company, they trigger the generation for the rest of the setup here.

**Marcel:** So that.

**Marcel:** Sorry, go ahead.

**Marcel:** You're going to.

**Ryan Singer:** Just one little note.

**Ryan Singer:** One thing I would just think about is that, like, meetings is not very differentiated.

**Ryan Singer:** So I would just think about, like, what is this that makes it different than just any meeting?

**Ryan Singer:** You know what I mean?

**Ryan Singer:** So that it's clearer what the value is or like, what the function is of this thing.

**Marcel:** So like, or something like, yeah, there's.

**Ryan Singer:** There'S something that's happening.

**Ryan Singer:** There's something that's happening in that meeting that doesn't happen in a normal meeting.

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** It's not status.

**Ryan Singer:** It's not, what are we doing tomorrow?

**Ryan Singer:** It's not like negotiation.

**Ryan Singer:** It's what I mean, like, so there's, there's, there's an element of like, what is the knowledge that's in this meeting that's relevant to me as, like, because remember, like, one of the challenges, if, if I remember right, was that, like, you're trying to get staff to go through all this process inside content OS when the staff doesn't fully appreciate, like, the reasons for doing everything.

**Ryan Singer:** So we're trying to like, dangle like the shiny object in front of them that's like, this is why this matters, right?

**Ryan Singer:** Like, learn and improve and new page opportunities.

**Ryan Singer:** Like, we're, we're trying to make it clear, like, what I get out of this and why it helps me, you know, so that's just something to think about here.

**Marcel:** Yeah, no, that makes sense because every client has these two phases.

**Marcel:** One is the calibrate intake phase or the strategy sprint phase, how you call it.

**Marcel:** And the first part of this phase is essentially if they go to this setup here and they do all this seven steps, record all your meetings, make sure you understand their company and products Record that in the system.

**Marcel:** Define their Personas, define their taxonomy, calibrate their style.

**Marcel:** Validate their style with sample articles by annotating them.

**Marcel:** Connect the Google search console, connect their.

**Ryan Singer:** Analytics and by the way, validate.

**Ryan Singer:** Validate their style is so much better than sample articles.

**Marcel:** That's a good.

**Ryan Singer:** Yeah, calibrate the verbs.

**Ryan Singer:** So calibrate their style.

**Ryan Singer:** Validate their style.

**Ryan Singer:** And sample articles is how you do it.

**Ryan Singer:** Right, that makes sense.

**Marcel:** Yeah, that's good. I'll make note of that for the future. And then to collect your website data, we can start the optimization work. That's the minimum we need to do the work. If the team spends two weeks on this calibration, that's great—everything downstream will be solid. But if they just jump straight into optimization without it, it's a total mess. How we handle this today is different for each client. We'd have people use Notion, Airtable, or I've got a bunch of processes in Notion they need to follow. Now we're turning that into a system. So the team goes through steps and clicks buttons, which helps with the legwork instead of having to search Perplexity or do manual research. The meetings feature serves both the intake phase—when you're calibrating and testing with the client—and the post-engagement phase. We want recipes that can identify: Is the client upset? Are they showing positive sentiment? Are they hitting their goals? Did we clarify their goals? There's a lot of post-processing in ongoing meetings too. For now, I'll keep it simple—meetings are out of scope for the immediate release, but that area will grow.

**Ryan Singer:** Got it.

**Marcel:** So this is the setup area, and then "Learn and Improve" is the main interface. When I send you the 4K video, it'll be clearer. But the backlog briefing—that's where you see the status of work in progress. It shows both new and optimization tasks. We want pages clustered by what you care about—whatever you're optimizing for. I've baked in clustering here. We might also add sparklines for core metrics. If you're focused on impressions, we could show a chart in the cluster. We have the idea of letting you define clusters dynamically—combining fields from the taxonomy. Personas is a dropdown, for example. You combine those and create clusters. And then you have Smart Views.

**Marcel:** Smart views essentially predefined filters with sorting.

**Marcel:** And those are the things that you want people to think about.

**Marcel:** And then when you go in, so.

**Ryan Singer:** Surging in almost top three is a smart view.

**Marcel:** Yeah, yeah, exactly.

**Ryan Singer:** Yeah.

**Marcel:** Cool.

**Marcel:** So you would click on that.

**Marcel:** So those are two Smart View combined.

**Marcel:** So those are checkboxes.

**Marcel:** So you could check them and you have multiple things combining filters basically.

**Marcel:** It might be too hard to do for this launch, but I think at least I can visualize the whole system now.

**Marcel:** And then we'll figure out what can be done in the next three weeks.

**Marcel:** And then we have the pages in here.

**Marcel:** There's some little bugs that we need to get the guys to fix the alignment here.

**Marcel:** But you can hover over and see things on the.

**Marcel:** On the right real quick or you can click and then switch to here and see we're going to have to clean up this.

**Marcel:** There's some things here that doesn't make sense anymore.

**Marcel:** Like the quick actions.

**Marcel:** Some of the quick actions you want to have is like categorize.

**Marcel:** This is the taxonomy part still makes sense.

**Marcel:** View on site still makes sense, but optimize it for here.

**Marcel:** I don't think it makes sense anymore because there's more work to be done there.

**Marcel:** But when you go into the page, let's say I we'll open one of these.

**Marcel:** Then we have the same.

**Marcel:** I think we had this before as well.

**Marcel:** So we have like a lot of like analysis that will be done on top of your core metrics.

**Marcel:** So the whole thing will be like on those core metrics at the page level.

**Marcel:** And then there's some other things that common mistakes that people do.

**Marcel:** Like they don't have their open graph set up, for example.

**Marcel:** That's super important.

**Marcel:** So like we're surfacing in here the keywords that article rank for and the taxonomy here as well.

**Marcel:** So taxonomy would want to edit.

**Marcel:** And then everything here, they're clickable.

**Marcel:** So you could just like, look at those things and you're like drilling down one of the pages that, that you created or that you shipped recently, or they're decaying all of them.

**Marcel:** We're like doing like, we have like AI workflows for taking in the data and taking context and creating a quick analysis of things.

**Marcel:** So that's going to be throughout the system.

**Marcel:** And then content is just a quick way for you to see what the content looks like in markdown form.

**Marcel:** And activity would be the feed of the work that was done on this page.

**Marcel:** And then if we go into backlog, backlog is where backlogging forward is where the work would get done.

**Marcel:** Same idea.

**Marcel:** So you can see the pages, same UI cluster the same way.

**Marcel:** With the sidebar, you'll be slightly different because you have like the name of the word icon.

**Marcel:** And then when you click on it could be like here or here or from here you would go into the place where a first step would be empty like this.

**Marcel:** So you would see where the opportunity came from, where the idea of this content came from.

**Ryan Singer:** Sorry, hold on.

**Ryan Singer:** I'm lost.

**Ryan Singer:** I'm lost with what we're looking at.

**Ryan Singer:** Can you go back?

**Ryan Singer:** What.

**Ryan Singer:** So here's a dumb question and maybe because it's sample data X best asana alternatives for small teams.

**Ryan Singer:** What is the work?

**Ryan Singer:** What's the task I'm supposed to perform here?

**Ryan Singer:** I'm supposed to write the article or I'm supposed to change something or.

**Ryan Singer:** What is this?

**Marcel:** This is a new page.

**Marcel:** So this is an assignment for a new page or work item for creating a new page that you accepted as you're going through the opportunities.

**Marcel:** So the opportunities.

**Marcel:** Maybe I need to spell it out and say a new page or create a new page or create a new page, if that makes sense.

**Marcel:** Yeah.

**Marcel:** So this is essentially like a to do it, that is create this page.

**Marcel:** And the idea here is like the title is X best because you don't know how many should be in the article yet.

**Marcel:** So that's not the title of the article, that's just the name of the opportunity.

**Ryan Singer:** Okay.

**Marcel:** Create a listicle for this topic.

**Ryan Singer:** So this new page task doesn't live under new page opportunities.

**Ryan Singer:** It lives under learn and improve because.

**Marcel:** That you already accepted.

**Marcel:** So here would be where you'd find all the opportunities.

**Marcel:** So we would have like actual stuff that I made it work yesterday.

**Marcel:** But on the normal setup with like simple data here, you would have a list of keywords or list of ideas with their traffic, potential traffic with their estimated traffic that you can get from it.

**Marcel:** Based on your size and some other things.

**Marcel:** And then when you accept and also suggestion, this would be a listicle or this should be a comparison article.

**Marcel:** This came from a competitor, for example, or this came from a trending topic.

**Marcel:** There's like a bunch of ideas here.

**Marcel:** And then you pick the ideas that you want to work on.

**Marcel:** And that would be like when you click Accept, that would send the idea to the Learn and Improve area.

**Marcel:** Because now you're actually working on the.

**Marcel:** On the page.

**Marcel:** Now it's like it's a real page.

**Marcel:** Like you're.

**Marcel:** It's a draft page.

**Marcel:** But you accepted that this should be a page on your website.

**Marcel:** So like, learning, improve.

**Marcel:** It's all about the pages.

**Marcel:** And here is just ideas, you know, that might apply or might not apply.

**Marcel:** Maybe, maybe it's like learn and improve.

**Marcel:** Find new page opportunities and then create new pages or create content or like something that's like.

**Marcel:** It does feel like the three jobs to be done that I, you know, feels too buried a little bit.

**Ryan Singer:** It feels too buried.

**Ryan Singer:** It feels too buried.

**Ryan Singer:** And it also feels like.

**Ryan Singer:** I don't understand why, like, just from, you know, like we, we bracket out what we know, we look at it fresh.

**Ryan Singer:** It's like, how do I.

**Ryan Singer:** How do I get to the.

**Ryan Singer:** That new page that I'm working on, go to Learn and Improve?

**Ryan Singer:** It's like, what?

**Ryan Singer:** Yeah, you know what I mean?

**Ryan Singer:** Like, it's like, it's so.

**Marcel:** I think at the very beginning, I think like there would be assignments.

**Marcel:** So like, I'm assigned to this item, for example, when I accept or give it to someone else.

**Marcel:** And we're going to need for sure like a my stuff or like my assignments kind of thing that like the basecamp has or linear has, where you see all the things that are yours.

**Ryan Singer:** You know.

**Marcel:** That somewhere.

**Ryan Singer:** What would make sense then is because there's two things that I'm.

**Ryan Singer:** That I think are going wrong here that are fundamental.

**Ryan Singer:** First of all, like, I love that we're.

**Ryan Singer:** The fact that we're having this problem is because everything else got clearer.

**Ryan Singer:** So this is good progress.

**Ryan Singer:** So what's happening is like, I've got a new page that I need to write.

**Ryan Singer:** It's very surprising that that is not to be that I can't find that under new page opportunities just because I know it's a new page.

**Ryan Singer:** Then.

**Ryan Singer:** If there's an improvement, like an experiment from Learn and Improve, if there's something I found that I should be fixing on a page, and I found that in Learn and Improve, I would expect that Improvement as opposed to creation.

**Ryan Singer:** Improve a page versus make a page.

**Ryan Singer:** I would expect that improvement to also be like findable again from learn and improve, because that's kind of like where I sourced it.

**Ryan Singer:** And then of course, like if.

**Marcel:** Yeah, that's how I was thinking.

**Marcel:** So you would have here in page portfolio would see your existing pages and you'd see the ones that are creating and you'd see the ones that you're optimizing as well.

**Marcel:** And they would all be in the backlog as well.

**Marcel:** So if you switch to backlog, you would see create or improve.

**Marcel:** There would be different types of items in the backlog.

**Marcel:** But yeah.

**Ryan Singer:** So here's a first thought here.

**Ryan Singer:** I don't know if we need to jump to the whiteboard to draw it yet.

**Ryan Singer:** I can just say it for the moment, which is like, okay, very, very first thing is if improvements and new pages are mixed here, they should definitely be clearly labeled in terms of what work is this?

**Ryan Singer:** Because it's very different work.

**Ryan Singer:** Right?

**Ryan Singer:** Yeah.

**Ryan Singer:** And I need to know like what work I'm reaching for, you know, and like what?

**Ryan Singer:** So, so that's, that's a key thing.

**Ryan Singer:** The other thing is I would definitely think here about basically having the exact same pipeline under both learn and improve and new page opportunities.

**Ryan Singer:** But you're filtering by what you're looking at.

**Ryan Singer:** So if I go into new page opportunities, I should basically have like a pipeline there, backlog briefing, writing, review ready for all the new pages also, you.

**Marcel:** Know.

**Ryan Singer:** So you can think of this almost like.

**Ryan Singer:** There might be an objection of like, well, should my work be in two places?

**Ryan Singer:** But I think this is where floating up my work or assignments or whatever as a, as a, as a top level place.

**Ryan Singer:** So like, if I just want to see like work I could go to just work, you know, but if I want to see like what are the new pages that we're working on, then it would make, it's going to make more sense in new page opportunities to see like, here's, here's the opportunities and here's the opportunities that you've already sort of like claimed or said that you want to, you know, you've kind of prioritized that you want to do.

**Marcel:** Right?

**Ryan Singer:** So you can think of these almost like, think of like learn and improve and new page opportunities almost like filters on the same underlying data structure.

**Ryan Singer:** You know what I mean?

**Marcel:** Yeah, yeah.

**Marcel:** The thing that I'm thinking here though is that I wonder if just the menu items are wrong, the naming here.

**Marcel:** You know, like I was even thinking we want to sell things differently.

**Marcel:** Like creation is like a whole module within the os.

**Marcel:** Learn and Improve and Finding Opportunities is like a separate module because like there's a lot of people that are paying a half ton of money for agencies just give them briefs and, and help them identify issues on their site.

**Marcel:** If we go on that rabbit hole I think it's going to be like so hard to split the software just on based on add ons that people should perform.

**Marcel:** You know but like we could very easily just add like pay walls and stuff like that in this experience.

**Marcel:** But I think we should just optimize for like if you have all the add ons turned on what is yeah in it.

**Marcel:** I like the Learn and Improve is one mode that explore new opportunities and you're just like I was just on a one hour call with our strategy sprint team and it's just mostly like they're recording these 20 minute looms explaining the strategy and their strategy for new pages which is like content clusters, how they're organizing the new opportunities, how they're, you know, the, the reasoning behind the clusters and how they're organizing opportunities.

**Marcel:** The thought process they went into in order to find those opportunities.

**Marcel:** Like that is like strategy.

**Marcel:** Right.

**Marcel:** And then the creation is like a whole other game that is like very separate from those two modes.

**Ryan Singer:** Yeah.

**Marcel:** Like the problem that kind of sets that I don't have them the data here on the actual maybe production hub.

**Marcel:** But opportunities they have.

**Marcel:** There's a clear distinction between a bunch of ideas and like the fields are the data set.

**Marcel:** The data structure is different, the work you do is different.

**Marcel:** So you're dealing with like sometimes 2000 things on your air table for example and you're clustering them and you are dismissing them in bulk.

**Marcel:** You're accepting them in bulk.

**Marcel:** You're just like the names or things are not so very spelled out.

**Marcel:** It's more like X for Y for example.

**Marcel:** Literally like X products for some alternative that's literally like one of opportunity idea and has like a bunch of keywords attached to it.

**Marcel:** So like you have, you're in a different mode of like just triaging to a bunch of stuff, loading the things between the system and triaging them again.

**Marcel:** And you do some, some, some analysis automatically that will be like oh this is the Persona or not so automatically the system will be like filtering out the noise.

**Marcel:** And that already happens today in the what we have working, working here.

**Marcel:** And then when you accept that that goes into like it's almost like a different person does a job, you know.

**Marcel:** So maybe Here it's just like opportunities or ideas or something like this.

**Marcel:** And then page is when, then page is like actually when you want to do the work.

**Marcel:** You know, because that, that challenge happens at the, even at the split of the system as well.

**Marcel:** You know, like I'm.

**Marcel:** But I think like I, I feel like we're all seeing kind of like the same thing except like the Learn and improve.

**Marcel:** All we're saying is like that.

**Marcel:** That's what I struggle with too.

**Marcel:** It was like if you mix optimization and creation in the same views as just like a subtle drop down or filter or a label in the same view, the experience can be effectively the same that you have here.

**Marcel:** But I think it has to be separated.

**Marcel:** Yeah, we could have.

**Marcel:** That's what I'm saying.

**Marcel:** Maybe the main new could be different than there's a new view from those things, but the process is essentially the same.

**Marcel:** Like this could be like moved out of here into Create page.

**Marcel:** You know, that's what I'm saying.

**Marcel:** It's like learn, improve, find new product page opportunities.

**Marcel:** Create new.

**Marcel:** Yeah, you know, and then like create new or whatever.

**Marcel:** Yes, yes, create that and puts it there.

**Ryan Singer:** Create as a, as a, as a, as a sibling.

**Ryan Singer:** Yeah, learn and improve.

**Ryan Singer:** Find.

**Ryan Singer:** Find opportunities like or new page opportunities and then create.

**Ryan Singer:** Because the finding of the opportunities is a totally different mode.

**Ryan Singer:** It's a different, it's a different like different kind of work than the actual creation states.

**Marcel:** Right?

**Marcel:** Like different states as in like I just have a shit on the stuff now.

**Marcel:** I filter down now.

**Ryan Singer:** Yes.

**Marcel:** You know.

**Ryan Singer:** Yeah.

**Ryan Singer:** So let's say that creation.

**Ryan Singer:** Would that mean that creation actually doesn't show up here inside of Learn and Improve at all and we're only seeing optimization tasks?

**Ryan Singer:** That's kind of what I would assume that this structure is telling me like as a user, like if Learn and Improve is about experiments, I would expect everything here to be optimization work.

**Marcel:** Yeah, I think that could work.

**Marcel:** I think that, yes.

**Marcel:** Even the backlog breathing and writing that even be like the one is like refreshing.

**Marcel:** Another one might be like optimization.

**Marcel:** Another one might be like, I don't know.

**Marcel:** Right.

**Marcel:** Like.

**Ryan Singer:** Yeah, that's, that's the other thing is these pipeline stages, they sound very creation focused and they kind of don't really track to optimizing.

**Marcel:** Yeah, that's, that's, that is a good point.

**Marcel:** Like for instance, like in the study that Katya did.

**Marcel:** Right.

**Marcel:** Like citation is really important.

**Marcel:** Right.

**Marcel:** And referencing it.

**Marcel:** Right.

**Marcel:** Like so it's like.

**Marcel:** And then like the structure of the pages or whatever.

**Marcel:** Like so it's almost like addressing some of these things that that's another thing that I, that that's the main thing that I wanted to talk today was just like how does optimization look like?

**Marcel:** Because the creation I have here.

**Marcel:** So for example, let's let just like finish the flow.

**Marcel:** But like let's assume that this is.

**Marcel:** That's Assume we pull this out and we have a create menu here and all you've seen is a creation of new pages.

**Marcel:** When you go into creation mode, the flow is very specific.

**Marcel:** As in like you have a brief, you generate an outline, the outline, you work on the outline quite a bit and then you let the agent go do the research.

**Marcel:** And that might take a full hour.

**Marcel:** So like some of our agents will spend like a full hour just researching everything and putting the article together.

**Marcel:** And then you go into editing mode and then so like that I have and I can show you real quick, the optimization is completely different as in like once I finish this.

**Marcel:** But there's like specific tasks on optimization.

**Marcel:** So like this is the creation process, for example.

**Marcel:** So let's say this is the.

**Marcel:** The assignment that I'm taking is X best as an alternative for small teams working for a lovable creating a page for them.

**Marcel:** Let's say the idea.

**Marcel:** I can still see the idea where I came from, the search intent and all that.

**Marcel:** I don't need to do anything with this.

**Marcel:** The agent will do the work, just that for context, I can choose a content type.

**Marcel:** So it'll be automatically selected because it's a listicle suggestion.

**Marcel:** This like each one of these content types is a different agent.

**Marcel:** Like they perform different doing assembling the article in different ways and doing the research in different ways.

**Marcel:** But the user doesn't have to know that.

**Marcel:** And then you pick the Personas.

**Marcel:** The search intent is here.

**Marcel:** Just if you want to change it.

**Marcel:** Sometimes it might not be fully accurate how you see the space.

**Marcel:** You can give more directions.

**Marcel:** You can say like actually start with a hook in a different way or close with a CPA in a certain way, but you don't have to.

**Marcel:** And you can also give like a range of word count.

**Marcel:** And then when we hit that, it would generate the.

**Marcel:** The outline.

**Marcel:** And the outline is usually this format where you have the section and what should be under each section and how.

**Ryan Singer:** It should be written.

**Marcel:** And you can spell out as much as you want or you can keep it short.

**Marcel:** And then we have a writing agent that will take this, do the research under each one of these outlines.

**Marcel:** There's also research questions that will be performed.

**Marcel:** That's just for reference for the folks to see what's going to be researched.

**Marcel:** And then when you click Generate, then this will go through the work.

**Marcel:** Once it's done, then you have an interface like this where you have the meta, you have the article title.

**Marcel:** Now for real, you have the meta title that's sometimes different.

**Marcel:** Sometimes you can have a suffix like this and then you have slug meta description and the COVID image and you can regenerate them if you didn't like.

**Marcel:** And if you want to annotate the article with the problems that you have, you go and review and then you can highlight the problems and the problems are like the set of problems and they have severity.

**Marcel:** And you can write a comment if you want, but even if you don't write a comment, we would be able to do a lot with that already.

**Marcel:** And then once you're done and you finish the review, you can also write high level.

**Marcel:** So that's kind of the first thing we talked like last month was this screen.

**Marcel:** And then when you finish this, then you would then the agent, we have an admin agent that you take your feedback and try to apply it.

**Marcel:** And then you would be in a free form notion next, this is just like a temporary text area.

**Marcel:** It would be like a notion document that you can freeform right from here and save.

**Marcel:** And once you're done, you're back into here and you can, if you don't have your CMS connected, you could just export.

**Marcel:** If you have connected, it would have a button to publish.

**Marcel:** So that is the process for creation optimization would be like completely different.

**Marcel:** So I hope that all made sense or.

**Ryan Singer:** Okay, so.

**Ryan Singer:** What I think we need to do is step back for a moment and figure out what are we trying to solve today.

**Ryan Singer:** So that I want, I want to make sure that we go into the thing that needs the most solving.

**Ryan Singer:** Because as soon as you showed me all of that, I wanted to like give you a whole bunch of reactions around that creation flow itself.

**Ryan Singer:** Because it's another case where I'm seeing huge opportunities to make the UI actually like the workflow you described.

**Ryan Singer:** I never saw like, I only saw like this like one slice.

**Ryan Singer:** Like now like I'm in review versus edit.

**Ryan Singer:** But there was kind of this whole chain, you know, and it was like you've got that in your head, but like I'm not seeing it in the product, you know, which means that it's going to be hard for other people to learn and to hold in their heads like that.

**Ryan Singer:** This is how it works.

**Ryan Singer:** But what I don't want to do is just kind of jump into optimizing the UX flow for creation if that's kind of not the problem to solve right now.

**Ryan Singer:** If there's like the deeper problem is how to even handle optimization.

**Ryan Singer:** Because it sounds like with creation at least you kind of understand the stages and maybe it's a smaller improvement from where you sit today to present that more clearly, but it's like you know what it is and you understand it versus it sounds like maybe optimization is more of a blurry thing or a hole today.

**Ryan Singer:** Is that right?

**Marcel:** Yeah, yeah, I think so.

**Marcel:** I think the creation I think we can crack and we can at least get the scheme that we have in the company.

**Marcel:** People that will be going to this workflow will be the folks that we train.

**Marcel:** So the set of like 50 people at most.

**Marcel:** So it's very trainable and we can continue to iterate on that.

**Marcel:** I think I can get out of the hole.

**Marcel:** The optimization is the part that I'm like, okay, this is a different piece in the system and can go in many different ways.

**Marcel:** What am I optimizing?

**Marcel:** Optimizing chunks of text in the article.

**Marcel:** Is it optimizing many things at once?

**Marcel:** Is it small to do's or is it a giant thing that you do everything at once?

**Marcel:** Where does it live?

**Marcel:** So there's that and then another part of the system that we deal with quite a bit is giving the clients or even giving our own team like a place to share what's happened.

**Marcel:** So like here's the thing that we did and so they're completely different topic.

**Marcel:** So those are the two things.

**Marcel:** Too many areas of the system that today I'm like, huh, that can be a rabbit hole in itself.

**Marcel:** Optimize is a fast follow that we have to do.

**Marcel:** Like as soon as I ship this in March, optimization has to start like almost right after, like figure out how to do the optimization part.

**Marcel:** And another part is it's less pressing like this.

**Marcel:** But it's a, it's a thing that we need to figure out eventually is like how do you keep the clients in the loop?

**Marcel:** And people are not good at that.

**Marcel:** So that's what the progress snapshots is for here.

**Ryan Singer:** Yes.

**Marcel:** And we have the same thing on check that.

**Marcel:** So check that.

**Marcel:** We collect like a ton of data, but it's charts and data.

**Marcel:** So people to make sense of it, they need recipes.

**Marcel:** Basically like look at here, look at there, analyze what happened, analyze what changed, create a report in your mind or send that to your boss or something like that.

**Marcel:** But in essentially you need to be like doing status check on this product on the regular.

**Marcel:** And if we need to do that, might as well do most of the work and people just tweak it.

**Marcel:** So that's how we're thinking about the progress snapshot.

**Marcel:** So both tools will need the similar idea.

**Marcel:** And some of the knobs are the same as in like impressions or visibility or here's things that went up and the things that went down in this field.

**Ryan Singer:** Okay, let me.

**Ryan Singer:** Daniel, can I check if I understand right?

**Ryan Singer:** So there's a.

**Ryan Singer:** So first of all, this pipeline that we're looking at inside of Learn and Improve actually isn't.

**Ryan Singer:** Doesn't belong here because we don't have a pipeline for optimization yet.

**Ryan Singer:** This is really just page creation right now.

**Ryan Singer:** Is that true?

**Ryan Singer:** Okay, so let me just, I'm actually gonna, Let me take over for a moment and I want to start.

**Marcel:** I.

**Ryan Singer:** Just want to start capturing some of these things so we don't only have words on the, on the recordings.

**Ryan Singer:** Okay, so first thing, what is wrong today?

**Ryan Singer:** Okay, so like this doesn't belong here.

**Ryan Singer:** And this moves to.

**Ryan Singer:** There's a new thing which is something like create.

**Marcel:** Yeah, right.

**Ryan Singer:** And this, this stuff.

**Ryan Singer:** Actually, let me, let me, let me just do this a little bit better.

**Ryan Singer:** Let's just say, like, let's say all this stuff is going to move.

**Ryan Singer:** It's going to move here, right?

**Ryan Singer:** And it.

**Ryan Singer:** And it and it and it doesn't live here.

**Ryan Singer:** So there's a question of.

**Ryan Singer:** And this was just me noting what you were describing about creation.

**Ryan Singer:** But this, this is, this is more or less known.

**Ryan Singer:** So it's not the subject for right now known enough for today.

**Ryan Singer:** But there's these questions around optimization and progress snapshots.

**Ryan Singer:** And if I understood what I just heard was like, for optimization, we have to form opinions around like the little bit like what's the framework of what we optimize?

**Ryan Singer:** So like what are the things that we kind of like measure or track or kind of the types of optimization.

**Ryan Singer:** And then if I understood right, you said the other side of that coin, which is like a different project, but it's linked, is what do we report on in progress snapshots?

**Ryan Singer:** Because they're both kind of the same thing, right?

**Ryan Singer:** They're both like, what do we consider to be change that is like improvement of some kind, right?

**Marcel:** Yeah.

**Ryan Singer:** And so Learn and Improve is kind of like, how do I create an improvement?

**Ryan Singer:** And progress snapshots is like, how do I tell about an improvement that happened?

**Marcel:** Yeah, yeah, there's also like the progress snapshots today.

**Marcel:** Like if I just show you real quick, that's just like a rough mock up that I spent essentially no time on it at all.

**Ryan Singer:** But yeah, let's see.

**Marcel:** Essentially it's the email that we should be sending our clients every week, which would be like, we have 10 ideas, 10 cluster ideas with 100 pages each.

**Marcel:** We made progress on 20 of those ideas on each one of these clusters.

**Marcel:** Some of them are starting to get impressions.

**Marcel:** 10% are getting impressions, for example.

**Marcel:** The other 90% is too soon.

**Marcel:** And we also worked on improving 100 of your existing pages by adding the right meta tags, adding the right OG tags and that kind of stuff.

**Marcel:** And they're starting to get maybe 10 of those pages are getting better impressions on Google Search.

**Marcel:** So that would be like, if you present your meeting like this and if you send an agenda ahead, this proxy snapshot is essentially an agenda for what we should be sending ahead.

**Marcel:** Or if a client just logs in and see it, they would be able to see, okay, here's the progress we made.

**Marcel:** Here's the thing that we're still working on here, the progress on the data that we're seeing, here's the experiments we're running, and here's the metrics.

**Ryan Singer:** So yeah, here's one thing I would call out.

**Ryan Singer:** A brief can have a really different meaning based on is this a brief for me in order to make decisions or is this a brief for me to, to know that you're doing your job right.

**Ryan Singer:** So like, like the presidential brief is like, this is what's going on in all these different countries.

**Ryan Singer:** So that, the, so that, so that as an executive, you know, there's, there's actions that have to be taken.

**Ryan Singer:** And what I, what I actually see when I look at this right now as a first blast, as a first, as a first pass, when I see, especially on the top, which is weekly content intelligence brief.

**Ryan Singer:** Like if, if I'm supposed to make a decision about content, then I want an intelligence brief about what's been happening.

**Ryan Singer:** If, if I'm not here to make a decision, but I am here to see that like you're, you're doing what I paid you for, you know?

**Ryan Singer:** And like, or like things are, I don't need to intervene because like you're doing what I expected, you know.

**Marcel:** Yeah, yeah, yeah.

**Ryan Singer:** Then, then that would be a very, very different angle.

**Ryan Singer:** That would be more like, it should be more like status report in the sense of like a status report is like where you report up of like this is what I did.

**Ryan Singer:** You know what I mean?

**Marcel:** Yeah.

**Marcel:** I think if we're just focused on the content OS and how we operate it today, I think we would need both.

**Marcel:** I think we need a brief for decision making at least every large milestone of the engagement, like, maybe every three months.

**Marcel:** And you do need a status report probably every week.

**Ryan Singer:** Yeah.

**Ryan Singer:** I would guess.

**Ryan Singer:** I would guess that based on what we've been talking about so far, that the.

**Ryan Singer:** The.

**Ryan Singer:** The.

**Ryan Singer:** The core of progress snapshots is actually status.

**Ryan Singer:** No.

**Marcel:** Yeah.

**Marcel:** What do you think?

**Marcel:** What do you think?

**Marcel:** Where do you think we should spend our energy?

**Marcel:** So should we spend an optimize or should we go into the.

**Marcel:** Because you've been thinking about the progress.

**Marcel:** Yeah, I think, like, put snapshots aside.

**Marcel:** The snapshots are almost like a stopgap of our engagement.

**Marcel:** Managers are sending these Slack updates that are complete garbage that are just like.

**Marcel:** We publish five pages for you.

**Marcel:** Like, seriously, like, what the hell are you doing?

**Marcel:** Like, just like.

**Marcel:** But Llama was decent.

**Marcel:** Like, if you.

**Marcel:** If you look at.

**Ryan Singer:** This.

**Marcel:** Remkus or.

**Marcel:** Yeah, yeah.

**Marcel:** So it's like they send this.

**Marcel:** This their status update, right?

**Ryan Singer:** Oh, yeah.

**Ryan Singer:** Yeah.

**Marcel:** Gosh.

**Marcel:** Dear God.

**Marcel:** We're just crazy.

**Marcel:** And that's it.

**Marcel:** Like, well, this is just.

**Ryan Singer:** This is like commodity.

**Ryan Singer:** Commodity work.

**Marcel:** Commodity.

**Marcel:** Exactly.

**Marcel:** Yeah.

**Marcel:** Then they look at it and they go, cool, you did something.

**Marcel:** Seven.

**Marcel:** That's worth $700 to me.

**Marcel:** It's $100 per.

**Marcel:** Like, you know what I mean?

**Marcel:** That's your value to me.

**Marcel:** It's $700 this week.

**Marcel:** Yeah.

**Marcel:** I'm paying you 18 grand a month.

**Marcel:** Like, what the am I doing?

**Marcel:** Exactly.

**Ryan Singer:** Yeah.

**Marcel:** And.

**Marcel:** And instead, it should feel like, holy crap, you legit have an army of agents going through and doing all this stuff, and you're connecting the dots for me and you're going through and, like, showing, like, where, like, we're heading and how things are improving, essentially.

**Marcel:** Seven.

**Marcel:** That you took us out of exploring 10,000 ideas.

**Marcel:** Yeah.

**Marcel:** And validated all the six Personas and pick the one that made most sense for our product.

**Marcel:** And it's with the framework of, like, we've been building these kind of, like, context files and things like that.

**Marcel:** And when we run all our transcripts and all our data through one of those, like, what comes out is, like, so much better than this shit.

**Marcel:** Right.

**Marcel:** And then we're like, okay, why are we letting humans do this at this point?

**Ryan Singer:** Like, totally.

**Marcel:** And it's like the going back to our mental model of, like, where the work is outputs, but the outputs are to deliver Outcomes and there's leading and lagging outcomes.

**Marcel:** And we need to connect the dots between the context of the company and their goals, to the work we prioritize, to the this validate to the outputs we deliver to did we learn or is this having the impact on the outcomes that we said it was going to be?

**Marcel:** Yes or no?

**Marcel:** And what are we doing about it?

**Marcel:** Right.

**Marcel:** So snapshots is like a gnarly thing that as long as it's better than what you just saw, it's a win.

**Marcel:** And then improvement is the way I think about improvement is like finding failure modes in the existing pages and addressing those failure modes so that you addressed it once, but later on you turn it into a systematic approach to like addressing that.

**Marcel:** For instance.

**Marcel:** Right.

**Marcel:** Like when we.

**Marcel:** Like I was just reviewing actually a new customer, Blacksell.

**Marcel:** Yeah.

**Marcel:** B L A X E L. And one of the first piece of content we publish for them is like a listicle alternatives to Daily IO or some.

**Marcel:** One of their competitors.

**Marcel:** Right.

**Marcel:** There is like an agentic framework platform or whatever.

**Marcel:** And like the first sentence, like, we praise them, we link to their site and we link to a press release and it's like, dude, this is supposed to be like a fucking thing about alternatives to this thing.

**Marcel:** Like, why are you praising them in the first sentence and linking to two of their sources and sending them like equity like that.

**Marcel:** That's a very clear.

**Marcel:** Like, you know, like, you know.

**Marcel:** And the intro was pretty garbage, right?

**Ryan Singer:** Like, so this is an example of an optimization.

**Marcel:** Exactly.

**Ryan Singer:** Yeah, yeah, yeah, yeah.

**Ryan Singer:** Good.

**Ryan Singer:** Okay.

**Ryan Singer:** So.

**Ryan Singer:** Okay, so what I just heard was there's a million things that we could do around snapshots, but as long as the snapshot is not what we just saw in Slack, it's kind of doing the job for now.

**Ryan Singer:** And therefore we should focus over on optimization for today.

**Marcel:** Yeah, yeah, yeah.

**Marcel:** I think snapshot's pretty.

**Marcel:** Yeah.

**Ryan Singer:** Okay.

**Marcel:** It's a low bar.

**Marcel:** Yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** All right.

**Marcel:** And yeah, so I can share whatever context you think would be helpful on the.

**Ryan Singer:** Yeah, let's.

**Ryan Singer:** What I want to maybe suggest that we start with here is since we have kind of a blank sheet that we're starting from, you know, whenever I have a blank sheet, I want to start with work with use cases or example cases.

**Ryan Singer:** So can we just collect like, what are the types of optimizations that should be happening via Learn and Improve?

**Ryan Singer:** You know, and like what we want is like multiple concrete examples that are different.

**Marcel:** Yeah.

**Marcel:** So maybe a mental model here is like, there's no good to have Sentry set up on error logging and then look at it like a freaking like 50,000 things, right.

**Marcel:** That are alerts.

**Marcel:** Right.

**Marcel:** Like, what we're trying to do instead is like, group them in the right altitude.

**Marcel:** That makes it like, actionable enough but not too down in the weeds.

**Marcel:** That just becomes like, you're out of context.

**Marcel:** Right.

**Marcel:** So the grouping and the altitude of the grouping is really critical.

**Marcel:** The way like.

**Marcel:** Like the way I kind of think about it is potentially like, fixing issues versus, like, improving content versus, like, refreshing the content.

**Marcel:** And then the question mark for me is like completely refactoring, AKA like creating new and replacing.

**Marcel:** Creating.

**Marcel:** Replace it.

**Marcel:** You know, which is like more of the creation one, which is like, this is so garbage.

**Marcel:** This is so bad.

**Marcel:** But don't get rid of the surface area because there's already like, equity in this URL.

**Ryan Singer:** Yeah.

**Marcel:** And like, the URL slug can be repurposed and the last would be like, pruning the lead archives.

**Marcel:** Retract kind of like, you know, essentially like pruning.

**Ryan Singer:** Yeah.

**Marcel:** So what I want to do is fix issues.

**Marcel:** Improve Refresh.

**Marcel:** Refactor.

**Marcel:** I think you're missed.

**Marcel:** Delete.

**Marcel:** Fix issues.

**Marcel:** Yeah, yeah.

**Marcel:** Fix, Improve.

**Ryan Singer:** Improve is different than refresh.

**Marcel:** Yes.

**Marcel:** So like, improve it is like around, like the intro just is.

**Marcel:** Is just bad or.

**Marcel:** Or something like that.

**Marcel:** Whereas, like, refresh again, we can discuss to make sure, see if we want to consolidate.

**Marcel:** But refresh is truly like, this thing has not been touched for six months and it's going to decay if you don't touch it.

**Marcel:** You need to refresh new stats, add a couple of things.

**Marcel:** It's just truly just to say, because these engines look at last modified or dates quite a bit.

**Marcel:** So it's like just adding a couple new stats or a couple new things is just really important.

**Marcel:** Keep it fresh, essentially, you know.

**Ryan Singer:** Yep.

**Ryan Singer:** Huh.

**Marcel:** What about the issues?

**Marcel:** Can you talk more about the kinds of issues?

**Marcel:** Yeah, like the.

**Marcel:** The issues ideally are us finding like, the patterns that are significant in both SEO AEO as well as, like, engagement.

**Marcel:** Right.

**Marcel:** And.

**Marcel:** And so it just could be like broken links.

**Marcel:** It can be like factual inaccuracies.

**Marcel:** It could be, you know, like h too many H1s and H2s or like, just like that.

**Marcel:** The structure of it.

**Marcel:** Right.

**Marcel:** Technical issues as well.

**Marcel:** Right.

**Marcel:** Like slow to load images.

**Marcel:** Yes.

**Marcel:** But I think those are gonna have to be systematic.

**Marcel:** Systematic.

**Marcel:** It's like, it's very rare that, like.

**Ryan Singer:** It could be like a page.

**Marcel:** Broken image.

**Marcel:** Broken image can be a PA Page.

**Marcel:** Yeah, like, issue.

**Marcel:** Right.

**Marcel:** Whereas, like, you know.

**Marcel:** Yeah, like, it just could be like AI slob.

**Marcel:** Right.

**Marcel:** It could be like all the things that we're like labeling.

**Ryan Singer:** It's got to be.

**Ryan Singer:** It's got to be vertical to the page, not horizontal to the platform.

**Marcel:** Yeah.

**Marcel:** Like.

**Marcel:** Yeah.

**Marcel:** Faction accuracy.

**Marcel:** It could be like outdated product mentions.

**Marcel:** Right.

**Marcel:** Like, no cta, lack of cta, bad cta, you know.

**Ryan Singer:** So how is, how are these different than improvements?

**Marcel:** Improvements could be like, add an FAQ section at the bottom, you know, but.

**Marcel:** But where it's like.

**Marcel:** Think of it as like in a publishing pipeline.

**Marcel:** The.

**Marcel:** The fixed issues would block you from publishing and the improvements would be publish and then add and make it better.

**Marcel:** Never thought about that.

**Marcel:** That's it.

**Marcel:** Like, if you're introducing a critical bug, you shouldn't ship it.

**Marcel:** Right.

**Marcel:** But if you're not, you can ship it and then make it better.

**Marcel:** Like, so that you learn from it in the process.

**Marcel:** Don't stop yourself from learning, you know?

**Ryan Singer:** Okay, I see.

**Ryan Singer:** So the intro might be bad, but if not, if the, if the, if the links and the images aren't broken, the structure is correct and it's not factually inaccurate, then it doesn't block us.

**Ryan Singer:** Like, this is literally like this.

**Ryan Singer:** These are things where like, you should, you should not be live with any of these things happening.

**Marcel:** Yeah, exactly.

**Marcel:** That's a good way to think about it.

**Marcel:** Yeah.

**Marcel:** Yeah.

**Marcel:** Those are like, yeah, P1s, P0s to P1s, depending on it, you know.

**Marcel:** Or like, let's say it's missing like an open graph image or the meta description is a duplicate meta description or missing completely.

**Marcel:** The, you know, the, the meta title is wrong or missing or something.

**Ryan Singer:** So these are actually health checks that are like, must pass.

**Marcel:** Yeah, yeah.

**Ryan Singer:** In that.

**Marcel:** And what I think about it is like, this is very much like, there's like a set of patterns to look for here.

**Marcel:** It's.

**Marcel:** It's decently black and white here.

**Ryan Singer:** Yes.

**Marcel:** It's not like fuzzy, grayish, like, I don't know, you know, it's kind of like it's.

**Marcel:** It's fairly grounded on what works.

**Marcel:** What's like, you know, and things.

**Ryan Singer:** And it's also objectively, this is, this is like objectively, let's say, measurable that it's happen.

**Ryan Singer:** Yeah, yeah.

**Ryan Singer:** I mean, maybe this is a little bit harder than some of the other ones.

**Marcel:** Yeah, yeah.

**Marcel:** Bad CPA is also hard, but the other ones are.

**Marcel:** Huh?

**Marcel:** Yeah.

**Marcel:** Let's pull this, for instance.

**Marcel:** Like something in their guidelines, like with Clerk, for example, they're like, don't use login.

**Marcel:** You sign in or Some like that, you know, and it's like that's a hard rule, you know.

**Marcel:** Think of it as like cursor rules, hard rules.

**Marcel:** Like like plot rules.

**Marcel:** Right.

**Marcel:** Like, or like agent rules where it's just like do this every time.

**Marcel:** Right.

**Marcel:** Versus like a skill.

**Marcel:** So like this is more like hard rules that shouldn't be broken but that, that can have a reference doc that has a running list of these rules, you know, and for each page.

**Marcel:** And some of these are rules and some of these are like optimization patterns that are generalized that are important.

**Marcel:** Right.

**Marcel:** If you mention a stat and you don't want to trivia who that stat is from or how you found that stat, like that's bad.

**Marcel:** Like you know that that's like a very like established thing.

**Marcel:** You can turn it off and you can override it.

**Marcel:** But, but right.

**Marcel:** Like don't let traffic through, you know.

**Ryan Singer:** So is this, this is like a domain specific example that like for one client this might be true but not necessarily for everybody.

**Marcel:** Or, or that one is like a pattern for like how AI engines work.

**Ryan Singer:** Okay.

**Marcel:** Like other fetching information.

**Marcel:** They're very, a lot of them are very, very biased towards like quotation source attribution.

**Ryan Singer:** Yeah.

**Marcel:** Quality data sources that you're attributing an information to.

**Marcel:** You know, essentially you did your homework and you organized information and you're not like this is not slot.

**Marcel:** Yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** So we've got hard rules that can't be broken.

**Ryan Singer:** We've got, I think this, we understand we could say what this is and what it's not.

**Ryan Singer:** Right.

**Ryan Singer:** That there's a, there's a kind of a black and white test that is confident enough that you could actually block publishing on it.

**Ryan Singer:** Is that right?

**Marcel:** Yeah, I think so.

**Marcel:** Yeah.

**Marcel:** Yeah.

**Marcel:** Because they have levels of severity and some of the stuff we need to humans to check it can.

**Marcel:** And the way I kind of think about it is like it.

**Marcel:** If it's something that is optional, maybe you should go into improvement and exactly move out of our rules like standards, you know, and the standards can have like a strict mode and a flexible mode or something for that site or for that content type or that page type, you know, maybe I don't know that that way it's kind of like network rules.

**Marcel:** Right.

**Marcel:** Like, like it's sometimes like you might need to like.

**Marcel:** Yeah.

**Marcel:** Monitor and sometimes you might need to be okay with like some things like letting it pass, but then you need to establish globally that you're going to let that traffic pass forever.

**Marcel:** Yeah, yeah, yeah, yeah.

**Ryan Singer:** That's Crazy.

**Ryan Singer:** I didn't know that Teal Draw had markdown, actually.

**Ryan Singer:** That's crazy.

**Ryan Singer:** Okay.

**Ryan Singer:** Refresh.

**Ryan Singer:** I understand in the same.

**Ryan Singer:** I think refresh is like this in the sense that it's very, very clear what it means.

**Ryan Singer:** It basically means, like.

**Ryan Singer:** Like you're fixing a staleness problem, right?

**Marcel:** Yes.

**Marcel:** Yeah.

**Marcel:** Has not been touched in more than.

**Marcel:** And then you define a parameter for how.

**Marcel:** Ideally, like, you know, think of it as like, past due.

**Marcel:** You know, like, recently past due.

**Marcel:** Just like, okay, the.

**Marcel:** The.

**Marcel:** They didn't release the payment.

**Marcel:** Like, you know, then 30 days past due, it's like, yo, what's going on?

**Marcel:** And then like, night gate past due.

**Marcel:** It's like, what the.

**Marcel:** Like.

**Marcel:** Yeah, like, send them the.

**Marcel:** It's like the.

**Marcel:** Where's my money?

**Marcel:** You know, where's my money?

**Marcel:** Scenes from like.

**Marcel:** Yeah.

**Ryan Singer:** Okay, so now let me take these, I think are a good start.

**Ryan Singer:** I mean, all this is good, but I mean, these ones are like, like, solid in the sense that we understand them.

**Ryan Singer:** This feels fuzzier.

**Ryan Singer:** I would love if we could be more clear about this.

**Ryan Singer:** Can we.

**Ryan Singer:** Can we just collect a couple more examples?

**Marcel:** Let's put a pin on that one.

**Marcel:** Because, like, let's laugh out one for less, because I think it might make it a little bit easier.

**Ryan Singer:** Like, it might shake out.

**Marcel:** If it doesn't fit in anywhere else, it won't fit there.

**Marcel:** Yep.

**Marcel:** The, like, replacing.

**Marcel:** It's like, usually it's just shallow content, but the opportunity behind it was, like, decent, you know, so.

**Marcel:** So for instance, like, there is, like, sometimes in some of these sites, it's like legacy content that hasn't been touched for, like, three, four years, and it's literally like two paragraphs, and it's like, what the fuck is this?

**Marcel:** But then the URL slug was actually pretty good, and it has, like, a ton of links to it.

**Marcel:** You know, that is the case with Vercel, for example, for their AI gateway.

**Marcel:** Yeah.

**Marcel:** Literally, like two words.

**Marcel:** Yeah.

**Marcel:** Yeah.

**Marcel:** And so it's kind of like the page should exist.

**Marcel:** A page like this should exist.

**Marcel:** This is not it.

**Ryan Singer:** Yeah.

**Marcel:** Huh.

**Marcel:** This is like so many miles away that there's nothing, no substance in this page that should be repurposed.

**Marcel:** It's just like, hit reset.

**Marcel:** Right?

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** Huh.

**Ryan Singer:** How do you.

**Marcel:** It's truly a refactor.

**Marcel:** A like, you know, rip and replace, but in the same room.

**Marcel:** Not like, exactly.

**Ryan Singer:** Yeah, yeah.

**Marcel:** URL is the most important thing.

**Marcel:** Yeah.

**Marcel:** Like, because you.

**Marcel:** You don't need to set up, like, redirects.

**Marcel:** You don't need to, like, you Know, it's just easier to do that and the likelihood of that URL doing well because it's already established URL that has already like, also there's like, you know, cross linking within your site and backlinking to that URL potentially, you know, Whereas like, if it's the URL slug sucks, there's no links from within your site and no links externally, then it's most likely a delete and archive kind of situation.

**Marcel:** Right?

**Marcel:** Because it's just like, okay, like, yeah, maybe the idea here was good, but it's like this is a shitty URL slug.

**Marcel:** There's no equity in this URL, you know, and then it's like a.

**Marcel:** So you're talking about the delete and archive, right?

**Marcel:** Yeah.

**Marcel:** Then it's like a prune and prune and redirect, you know.

**Marcel:** Aha.

**Ryan Singer:** Got.

**Ryan Singer:** Got it.

**Ryan Singer:** Okay, let me just capture that.

**Ryan Singer:** I was, I was, I was honestly spinning on replace URL.

**Ryan Singer:** So this is like, it's, it's, it's, it's not, it's not, it's not well linked.

**Ryan Singer:** There isn't.

**Marcel:** Yeah, it's not well linked internally or externally.

**Marcel:** It has no sign of life, like, no, you know.

**Ryan Singer:** Yeah.

**Marcel:** And, and then the substance of it, there's no value to the substance of it.

**Marcel:** Tap into traffic and impressions as well.

**Ryan Singer:** Right?

**Marcel:** Yeah, it's usually like if you have a site that has.

**Marcel:** There's been a lot of studies on this, right.

**Marcel:** Like, and so like, think of it as like crawl budgets for SEO, but for agents, it's the same thing.

**Marcel:** And so you have limited crawl budget that is tends to be directly proportional to your site's authority and how it's perceived or your brand's authority in some cases.

**Marcel:** And so like the more you spread, the less signal you're going to get.

**Marcel:** And so you're a lot better.

**Marcel:** Like if you have like, let's say 10,000 pages that you're just like, no, it's fucking good.

**Marcel:** But, but like you have no signals, right?

**Marcel:** Like you're better off picking like the 100 that are the most.

**Marcel:** No brainer for Google to be like, well, there's nothing else in the world about this and yours is really good.

**Marcel:** And then you have this like really high quality signal and then it learns from that.

**Marcel:** Signals go, whoa, this is good, give me more, give me more, give me more of this.

**Marcel:** And you give it a little bit more and a little bit more and a little bit more, a little bit more.

**Marcel:** Until there's diminishing returns and you work your way through it.

**Marcel:** Whereas, like, if you just like say here's 10,000, it's.

**Marcel:** It won't even know how to prioritize it.

**Marcel:** So that's just gonna randomly prioritize it and ingest a lot of bad signals.

**Marcel:** Potentially.

**Ryan Singer:** Yeah.

**Marcel:** Right, because it's not going to send you like the cram or the cram, like traffic.

**Marcel:** It's going to send you the shitty traffic to those and then it gets like a bounce or something.

**Marcel:** Yeah, this kind of sucks, you know, and so you're better off like pruning aggressively anything that's like at the bottom.

**Marcel:** Right.

**Marcel:** And then the only cases where that's not it is that if it historically had traffic and it went down to zero, or like there's a ton of backlinking or a ton of linking internally.

**Ryan Singer:** Right.

**Marcel:** In which case you don't want a bunch of oral force, you know?

**Ryan Singer:** Yeah, that's part of this.

**Ryan Singer:** Yeah, yeah, yeah.

**Marcel:** Sorry, that was a long explanation of.

**Ryan Singer:** No, that's, that's, that's good.

**Ryan Singer:** How.

**Ryan Singer:** Let's, let's leave improved to the side for the moment.

**Marcel:** We should post process this, meaning as a blog post of how crawling and Google works.

**Ryan Singer:** This is literally how we see it.

**Marcel:** Happening on our clients.

**Marcel:** How the replace URL should have been the.

**Marcel:** Yeah, like replace.

**Marcel:** Yeah, replace URL.

**Marcel:** Yeah, replace and keep the URL.

**Marcel:** Replace the code and keep the URL.

**Marcel:** Yeah, it's like refactor.

**Marcel:** Yeah, exactly.

**Ryan Singer:** So these have what I can picture.

**Ryan Singer:** I can picture the tests that surface these.

**Ryan Singer:** This one also we have a clear test we could.

**Ryan Singer:** For how to surface it.

**Marcel:** Yeah.

**Ryan Singer:** How do you, how do you surface this?

**Marcel:** So this is once upon a time, this was good.

**Marcel:** It's clearly been dead for a while.

**Marcel:** Right.

**Marcel:** You know, and, and the, the only way to revive it is to like create a clone and you know, start from scratch here.

**Marcel:** But because this once upon a time was good and had some sign of life and.

**Marcel:** Or some sign of value, then you might as well keep the URL because it makes our lives a little bit easier, you know?

**Ryan Singer:** Okay, so how is this literally, like.

**Marcel:** This is truly like shallow content, you know, like.

**Marcel:** Yeah, like, like what the f is this?

**Marcel:** Like, like low work count.

**Marcel:** Like, like just, just like clearly nowhere near, like the quality bar that we have for the rest of the site.

**Marcel:** Yeah.

**Ryan Singer:** Okay, so if we were to like metricify this, it was good once, it's been bad for a while.

**Ryan Singer:** That's a traffic thing over time.

**Marcel:** Let me give you a quick example.

**Marcel:** This is a page for Vercel AI models.

**Marcel:** For example, and it's a great.

**Marcel:** This page should definitely be there, has the right URL as not even one paragraph of text and everything else is completely irrelevant to search engine.

**Marcel:** We're in contact with them to essentially like enrich these pages.

**Ryan Singer:** Yep.

**Marcel:** So that.

**Marcel:** That is an example of one.

**Marcel:** Okay, so the rip and replace is first of all.

**Ryan Singer:** Did you say rip and replace?

**Marcel:** Yeah.

**Ryan Singer:** It'S a good one.

**Marcel:** It's like no traffic is usually like a good indicator.

**Marcel:** First of all, no current traffic.

**Marcel:** But in the last 12 months, at some point there was traffic.

**Marcel:** Some URLs are some links, internal links and backlinks, not zero, you know?

**Ryan Singer:** Yeah.

**Marcel:** Huh.

**Marcel:** And.

**Marcel:** And then ideally is doing some work on understanding the intent of this page to see if it's like an opportunity we would have.

**Marcel:** Like, does this match like an opportunity that we would have surfaced as new if this URL didn't exist, you know, AKA like don't cannibalize.

**Marcel:** Like.

**Marcel:** And so this is more of like, in the example of like the Vercel one, it would be like Opus 4.5.

**Marcel:** The intent is you're looking for the stats on the model, like the details of it.

**Marcel:** You're looking for evals on it.

**Marcel:** You're like trying to understand blah, blah, like that's a legit intent.

**Marcel:** It's like a legit opportunity that should belong here in this page.

**Marcel:** Right.

**Marcel:** But this page is not doing that.

**Marcel:** So that was a little bit more fuzzy.

**Marcel:** Whereas like the leap one is no current traffic, like low to no linking internal or external.

**Marcel:** And there was never any sign of life, or there hasn't been a sign of life for more than a year or something?

**Marcel:** You know, this thing was never valuable at all.

**Ryan Singer:** Yep.

**Ryan Singer:** Huh.

**Ryan Singer:** What is, Is there.

**Ryan Singer:** Is there an example of intent match that you can actually do with the systems you have already with the info, with the knowledge you have?

**Ryan Singer:** Like, how would you.

**Marcel:** You.

**Ryan Singer:** How would you do that?

**Marcel:** Just looking at the URL and then looking at what is actually on the page, even if it's very, very, very little, tends to be like, okay, like that you can kind of understand.

**Marcel:** And then you can reverse engineer what searches related to this would be.

**Marcel:** And then look what at those pages that are live, that are actually ranking for what that would be, and it becomes really like a finite game of what that intent would have been.

**Marcel:** Right.

**Marcel:** Like, so the URL slug tends to tell you a lot.

**Marcel:** And if the URL slug is garbage, then most likely it's in the category of delete anyways.

**Marcel:** You know, like, it's Like a one word slug.

**Marcel:** You know, like.

**Ryan Singer:** Okay, so could I say some intent match from URL Slug.

**Marcel:** Yeah.

**Ryan Singer:** And this is something that you would do.

**Ryan Singer:** You couldn't do with.

**Ryan Singer:** With the AI as opposed to with a human.

**Marcel:** You could.

**Marcel:** Yeah.

**Marcel:** Actually, like, the more I'm thinking about this, I think we can put these two together.

**Marcel:** Rip and replace or archive.

**Marcel:** And it's mostly like the action you determine based on a human judgment, I think.

**Ryan Singer:** Yeah.

**Ryan Singer:** But here's the thing is, I think that if we come back to when we were looking at this.

**Marcel:** Yeah.

**Ryan Singer:** The, the number one question I had in my mind when I was playing user was what am I supposed to do?

**Ryan Singer:** So I think the action is actually kind of maybe the leading thing when it comes to identifying what these things are.

**Ryan Singer:** Do you know what I mean?

**Marcel:** Yeah, it's like fix, improve, refresh.

**Ryan Singer:** Right.

**Marcel:** And then this one is like, replace or archive.

**Marcel:** And.

**Ryan Singer:** So fix, refresh.

**Ryan Singer:** Refresh is a little.

**Ryan Singer:** Okay, we'll come back to that.

**Ryan Singer:** Replace.

**Marcel:** And I'll say replace it or archive.

**Marcel:** Because it's just kind of.

**Marcel:** It's like in the same mode.

**Marcel:** It's just like.

**Ryan Singer:** Yeah, but it's such a different.

**Ryan Singer:** But it's totally different work, isn't it?

**Marcel:** Any little human things that, that like, you can look at something and very quickly, like.

**Marcel:** Yeah, no brainer.

**Marcel:** Whereas, like, I think this is one of those where human judgment is the way easier than like one of the two buckets to put something under.

**Ryan Singer:** No, I get it, I get it.

**Ryan Singer:** Yeah, I get it.

**Ryan Singer:** So there's actually a different work step of decide versus.

**Marcel:** Yeah, yeah, exactly.

**Ryan Singer:** Right.

**Marcel:** Yeah, yeah.

**Marcel:** It's like, this is the queue of like, garbage can and you just decide if, like, you want to recycle or if you want to just like dump it.

**Marcel:** You know, it's like, come on.

**Marcel:** Yeah, yeah.

**Ryan Singer:** So this, this is it.

**Ryan Singer:** This is different work.

**Marcel:** Just call it like recycle or dump.

**Marcel:** Yeah, we should have some phone.

**Ryan Singer:** Yeah, totally.

**Ryan Singer:** Okay.

**Marcel:** And when you archive, we need to also decide if it's going to be a redirect or just.

**Marcel:** It almost always should be a wild card redirect or something, you know, because it's just like a good practice to have it.

**Ryan Singer:** Yeah, let's.

**Ryan Singer:** Let's take.

**Marcel:** Let's.

**Marcel:** And then it improve is the only one missing.

**Marcel:** Oh, yeah.

**Ryan Singer:** Let's.

**Ryan Singer:** Let's take it.

**Ryan Singer:** Let's.

**Ryan Singer:** Let's leave improve still and let's take another spin through the exact same material with this other question.

**Ryan Singer:** What's wrong?

**Ryan Singer:** Okay, so this is from the action lens.

**Ryan Singer:** Let's look at it from the, from the failure lens, you know.

**Marcel:** Yeah.

**Ryan Singer:** So like this was like a rule was broken.

**Marcel:** Yeah, Important rule was broken.

**Marcel:** Yeah.

**Ryan Singer:** This is stale, expired.

**Marcel:** Yeah.

**Marcel:** Yeah.

**Marcel:** This is decaying and losing engagement.

**Marcel:** Not effective.

**Marcel:** Yeah.

**Marcel:** This is like garbage.

**Ryan Singer:** Well, no, not yet.

**Ryan Singer:** Garbage.

**Ryan Singer:** This is garbage.

**Marcel:** I mean, it's garbage.

**Marcel:** It's just.

**Marcel:** Do you want to recycle or not?

**Ryan Singer:** Ah, okay.

**Marcel:** It's garbage no matter what.

**Marcel:** It's just a matter of like you want to reuse material.

**Ryan Singer:** Yeah.

**Ryan Singer:** Here's the thing.

**Ryan Singer:** Like, like, isn't there a sense when you find this that it's a little bit like you found like gold?

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Like it's garbage.

**Ryan Singer:** But like there's opportunity here because of the fact that it's like.

**Marcel:** That.

**Marcel:** The vercel one is kind of like that.

**Ryan Singer:** I mean the vercel one you showed.

**Marcel:** Me felt like it's just the vercel one is almost like the exception.

**Marcel:** Like what you end up with here is like founder, early stage, created some like blog at the beginning that had the right title and the bad execution on like home base or just like single paragraph product announcements.

**Marcel:** But the title was like an intent that was like, you know, very, very good.

**Marcel:** Like it's like what is blah blah, blah.

**Marcel:** But it was about a product announcement.

**Marcel:** It was like, what the hell?

**Marcel:** This doesn't match.

**Marcel:** Right.

**Marcel:** Like it's actually like pretty rare that you're gonna see.

**Marcel:** It's more rare that you're gonna find things like that.

**Marcel:** Or like the vercel one, which like an entire area of the site is the right area.

**Marcel:** It's just the execution of the content is, you know, to be improved.

**Marcel:** But then I see, you know, I see different, you know.

**Marcel:** Okay, yeah, this is more of like candidate for garbage, you know.

**Marcel:** And what's wrong is just like, it's just bad, you know?

**Marcel:** Yeah, it's like best case bad, worst case toxic, you know?

**Ryan Singer:** Uh huh.

**Ryan Singer:** Uh huh.

**Ryan Singer:** So this is like that is maybe.

**Marcel:** Even though it's like useless, let's just like call it useless, you know, which is very different.

**Marcel:** It's like, yeah, like legit.

**Marcel:** Like instead of bad, useless and then toxic.

**Marcel:** Like, whereas like toxic could be like this is a virus, you know, like.

**Ryan Singer:** Okay, so what's right?

**Marcel:** In what sense?

**Ryan Singer:** For each one of these, if I'm fixing it, something's right with it.

**Ryan Singer:** Right.

**Ryan Singer:** Otherwise, because I'm not throwing it away.

**Marcel:** Yeah, got it.

**Marcel:** Yeah, the like proof there's traffic and engagement and or there's visibility to it.

**Marcel:** There's Impressions and the.

**Marcel:** The opportunity.

**Marcel:** Yeah, there's potential.

**Marcel:** Except like the case.

**Marcel:** Yeah, there's potential.

**Marcel:** Yeah.

**Marcel:** A genuine judgment on potential.

**Marcel:** You know, there's like unrealized potential.

**Marcel:** Yeah.

**Ryan Singer:** What do you call.

**Marcel:** Because if there's like fulfilled potential, then there's nothing you should do.

**Marcel:** Right.

**Marcel:** Like, unrealized potential is like, hey, we think this could be realized even more even.

**Marcel:** Even in a measurable way.

**Marcel:** Right.

**Marcel:** For example, like when you're picking a topic in the opportunities area today, it's coming from research on keywords.

**Marcel:** They are getting search volume.

**Ryan Singer:** So that's.

**Ryan Singer:** Is that what potential means?

**Marcel:** Yes.

**Marcel:** Yeah.

**Marcel:** You voice the article somehow.

**Marcel:** Like, maybe the meta type is wrong, the content is wrong, it's not indexed.

**Marcel:** Then there's potential with zero.

**Marcel:** Yeah.

**Marcel:** Like there's potential for better quality content.

**Marcel:** There's potential for more impression and visibility, more citations, there's potential for more traffic, there's potential for deeper engagement and there's potential for higher conversion.

**Marcel:** Yeah.

**Marcel:** Depends.

**Marcel:** Yeah.

**Marcel:** Yeah.

**Ryan Singer:** Huh.

**Ryan Singer:** Okay.

**Marcel:** Is it.

**Ryan Singer:** Would it be.

**Ryan Singer:** Meaning that felt important, but I'm not sure if we're getting on a sidetrack.

**Ryan Singer:** Would it be meaningful to capture those different types of potential?

**Marcel:** Yeah, because they align to like our scores.

**Marcel:** Essentially.

**Marcel:** That's are on the page.

**Marcel:** Right.

**Marcel:** Like they are.

**Marcel:** They're all like aligned to it, you know?

**Ryan Singer:** So what are they?

**Ryan Singer:** What are the types of potential?

**Ryan Singer:** Again, just give those to me one more time.

**Marcel:** Potential for quality.

**Marcel:** There's AKA there's potential to improve the quality of the page.

**Marcel:** There's potential for impressions and there's potential for more traffic and there's potential for engagement and there's a potential for conversions or actions to.

**Ryan Singer:** Can you give me a quick, A quick lesson?

**Ryan Singer:** What's the difference between impressions and traffic?

**Marcel:** Yeah, like, like impressions, for example, are like when you search something on Google and a page is like the last one on the page and people don't scroll down, that's still an impression.

**Marcel:** Right.

**Ryan Singer:** I got it.

**Marcel:** Yeah.

**Marcel:** Okay.

**Ryan Singer:** Yep.

**Marcel:** And so like, we know that there's people searching for a certain keyword, but you're not even showing up because you're like on the fifth page.

**Marcel:** Right.

**Marcel:** On the first page you would get a ton of their pressure.

**Marcel:** Right.

**Marcel:** Whereas like, traffic is about, like the impressions give you a shot at traffic.

**Marcel:** Traffic is you hit like you convince someone to click.

**Marcel:** Right.

**Marcel:** You convince someone and do something.

**Marcel:** Right.

**Ryan Singer:** Yeah.

**Marcel:** Go through with it.

**Marcel:** And so one is about like positioning correctly and a bunch of other factors.

**Marcel:** The other one is about, like selling them on the promise.

**Marcel:** And then engagement is Delivering or over delivering on the promise of what you.

**Marcel:** And the promise is your headline and your description, right?

**Ryan Singer:** Yep.

**Marcel:** And so, so, and then hopefully your promise matches the intent of the user.

**Marcel:** And when you over deliver on that promise, it's like, whoa, I'm here.

**Marcel:** This is amazing.

**Marcel:** I'm going to, I'm clicking through, I'm spending a bunch of time.

**Marcel:** And then conversion is like, holy.

**Marcel:** You built so much credibility and you deliver so much value.

**Marcel:** I want more, I want to go deeper.

**Marcel:** I want to talk to you.

**Ryan Singer:** Yep.

**Ryan Singer:** Coming, coming back to let's say, kind of instrumenting opportunities for optimization.

**Ryan Singer:** Are there things here that are, that are you expect to be measuring and populating in the learn and learn and improve section?

**Marcel:** Yes.

**Marcel:** So quality is around alignment.

**Marcel:** And the same thing with like the improve area, by the way, is around alignment.

**Marcel:** Right.

**Marcel:** Like, so think of alignment as like you have a grounding document or grounding truth and it's about like how much like this deviates from that truth.

**Marcel:** Right.

**Marcel:** And where does it deviate?

**Marcel:** And, and so for instance, like there's a company description.

**Marcel:** Well, is this thing aligned to that company description?

**Marcel:** There is a writing guideline.

**Marcel:** Is this aligned to that writing guideline?

**Marcel:** Right.

**Marcel:** Like, so think of it as like rounding evals, almost like, I don't know if that's even a term, but it's like, yeah, yeah.

**Marcel:** But then there's like, there's like an opportunity grounding of like, this is the opportunity.

**Marcel:** This is the intent of what we're trying to do.

**Marcel:** This is the brief, this is, is the research.

**Marcel:** So there's like research grounding, you know, and alignment.

**Marcel:** There's like opportunity and intent alignment.

**Marcel:** And then there's like the company product Persona and guidelines alignment, which is like your context files, if you will.

**Marcel:** Right?

**Ryan Singer:** Yeah.

**Marcel:** And so it's like, it's like a drift, right?

**Marcel:** And then a drift can happen, you know, because of like context poisoning or you know, over compressing or, you know, or like missing a point or it, you know, so some, some version is.

**Ryan Singer:** That this, is this, is this misalignment?

**Marcel:** So improve is misalignment that needs to be realigned because there's a need for like, there's a reason the alignment is there.

**Marcel:** Right.

**Marcel:** And then.

**Marcel:** Okay, hold on.

**Marcel:** Sorry.

**Ryan Singer:** Okay.

**Ryan Singer:** All right.

**Marcel:** Yeah, like, and, and hopefully like over time, like we're building these kind of like best practices and evals based on studies and a lot of data we're collecting across a lot of customers so that like we can make more recommendations on the kinds of misalignments that, that we should do.

**Marcel:** Like, you know, the quality one has like so much potential for a very unique ip.

**Marcel:** Yeah.

**Marcel:** And just so very subjective and a hard problem.

**Marcel:** One quick thing on, on kind of how like check that I'm going like, it's almost like I did a bunch of research on how analysts thinks about it and users and peer reviews and things like that.

**Marcel:** And there's kind of like these attributes, if you will.

**Marcel:** Right.

**Marcel:** Like, and this is.

**Marcel:** And I'll connect doc here in a second.

**Marcel:** But it's like usability, capability, usability, value, trust, support, innovation.

**Marcel:** So over time that's for like brand perception.

**Marcel:** Right.

**Marcel:** And how AI engines think of that.

**Marcel:** And whereas like for here there can be attributes that kind of like matter to them.

**Marcel:** Right.

**Marcel:** If you will, at the content level, you know, and those attributes are you know, personalized based on the context of the company.

**Marcel:** But then there's also like global things as well.

**Marcel:** Right.

**Marcel:** That are like for instance, like the, like the attribution, you know, better attribution or more examples or you know, but there's like having images or things like that like are actually like enrichment things.

**Marcel:** Right.

**Marcel:** That, that we know are like well known patterns.

**Marcel:** Create a rubric.

**Marcel:** Yeah.

**Marcel:** But then there's also Ryan, like the things we're going to learn about them, right.

**Marcel:** And their baseline, right.

**Marcel:** Like so, so for instance, like if you have 10,000 pages and you look at only your blog pages and within those blog pages you understand the type of content it is and you have all this data on it, right.

**Marcel:** Like you can then figure out, hey, for pages that have higher engagement and a higher percentage or propensity for people to go to the bottom of the page and click through to the next page.

**Marcel:** These are the patterns we learned from it.

**Marcel:** And then those are the patterns that then you can suggest improvements to the other ones.

**Marcel:** And so think of it as like this is the baseline.

**Marcel:** These are like your top performers in any metric and these are like your low bottom performers.

**Marcel:** And you learn from what patterns can be reproduced here so that these can be higher to here so that your baseline increases.

**Marcel:** Does that make sense?

**Marcel:** Got it.

**Ryan Singer:** Yeah, that makes sense.

**Ryan Singer:** I think.

**Marcel:** Sorry.

**Ryan Singer:** It'S all like interesting.

**Ryan Singer:** And so in the scope of what we're trying to solve right now, we're trying to figure out kind of how to present opportun these as work items.

**Ryan Singer:** And so let's, let's just call quality quality for the moment.

**Ryan Singer:** And I just want to see if we can kind of, if we can just kind of maybe spell out how to measure these things, we might get to a point where I think we have like a pretty solid picture of like what we might be looking at, what we might be surfacing, what the action is and so on.

**Ryan Singer:** And then this could be an input for us to then look at, you know, look at solution ideas.

**Marcel:** I think Quality.

**Marcel:** Right.

**Marcel:** You can even spell out as like score on the rubric of traits that we can.

**Marcel:** Yeah.

**Marcel:** Every page is going to have a quality score and that quality score is going to be.

**Ryan Singer:** That's actually this a trend line.

**Marcel:** Yes.

**Marcel:** And so just think of it as just like the quality dropped or the quality has been low for a long time.

**Marcel:** Always has been low.

**Marcel:** And so like, as far as this is concerned, we almost don't even need to think about the rules.

**Marcel:** And that's why I'm trying to create these composite scores everywhere, because otherwise super defined rules everywhere, you know?

**Ryan Singer:** Yeah.

**Ryan Singer:** I think, I think it's just good to know that like, if.

**Ryan Singer:** If something has been flagged as improve because of a quality issue, you know, is that what this is?

**Marcel:** Yeah.

**Marcel:** Like low quality score or a big dip.

**Marcel:** Yeah.

**Marcel:** You know?

**Ryan Singer:** Yeah.

**Marcel:** So.

**Marcel:** And then don't worry about it.

**Marcel:** This is going to be determined by the scoring.

**Ryan Singer:** Yeah.

**Ryan Singer:** Yep.

**Ryan Singer:** But then we just, if, if we're getting into the work step of an improvement, then we're just going to want to know that we have the ability to unpack what that particular score means so that we know what to actually do as an action.

**Ryan Singer:** Good.

**Ryan Singer:** Okay.

**Ryan Singer:** I'm guessing the rest of these are easier.

**Marcel:** Even if it's not a human doing the improvement for the quality, it still has to.

**Marcel:** We have to unpack even more.

**Ryan Singer:** Oh yeah, totally.

**Ryan Singer:** Yeah, totally.

**Ryan Singer:** Huh.

**Ryan Singer:** Okay.

**Ryan Singer:** Are these worth spelling out or do we just want to take it for granted that like those are very measurable?

**Marcel:** I think the only one that the engagement and conversions are probably like coming soon.

**Ryan Singer:** I think.

**Marcel:** I think it is worth, like even didn't like, I think I can guess.

**Marcel:** But our team didn't understand that impressions, low impressions equals shitty meta tags, for example, you know, uncheck that.

**Marcel:** Yeah.

**Marcel:** Like, let me just show a quick example because this is.

**Marcel:** So there's a set of things that are related to impressions, a set of things that related to traffic.

**Marcel:** Right.

**Marcel:** This is for a page on cursor pricing.

**Marcel:** Okay.

**Marcel:** Let's just check that for.

**Marcel:** Check that.

**Marcel:** So we have thousands of.

**Marcel:** And you can see like it went.

**Marcel:** And we got like clicks and impressions and then it pretty much went to zero.

**Ryan Singer:** Yeah.

**Marcel:** Right.

**Marcel:** So this is what we're trying to flag.

**Marcel:** Like we.

**Marcel:** Like someone caught this manually somehow.

**Marcel:** But.

**Marcel:** But like it's highly unlikely in the sea of shit and, and signals that someone would catch this.

**Marcel:** And had we not acted, this wouldn't have happened.

**Ryan Singer:** Totally, totally.

**Ryan Singer:** Back on the whiteboard here.

**Ryan Singer:** I'm actually pasting that.

**Ryan Singer:** I'm just dropping this in.

**Ryan Singer:** What is this in terms of this?

**Marcel:** This is a.

**Marcel:** There was a rise in impressions and then a rising clicks, which is traffic.

**Marcel:** Right.

**Marcel:** Followed by a dip in both.

**Marcel:** So when, when clicks drop but impressions don't, that means your promise is off.

**Marcel:** Like you're.

**Marcel:** No one's clicking on your ad.

**Marcel:** Right?

**Marcel:** Yeah, like when, when impressions and clicks drop, then it's usually like the signal is bad.

**Marcel:** Like.

**Marcel:** Like they came in your contest pile of garbage.

**Marcel:** Right.

**Marcel:** And that usually the.

**Marcel:** The leading indicator of that.

**Marcel:** Because that's lagging.

**Marcel:** Right.

**Marcel:** You're already fucked.

**Marcel:** It's already went to zero.

**Marcel:** Right.

**Marcel:** The leading indicator of that is like the day that thing spiked the first time you could have seen the engagement.

**Marcel:** And the bounce rate, like time on page bounce rate.

**Marcel:** How many of the visitors that landed, AKA enter the site through this page ended up doing more things.

**Marcel:** Right.

**Marcel:** And was the average session time compared to everything else?

**Marcel:** Right.

**Marcel:** Specifically for this channel, AKA like SEO in organic.

**Marcel:** And if it was like way lower than anything else, like lookalikes, similar type of page or overall baseline for the site, then it's telling me the content was bad essentially.

**Marcel:** Like it wasn't good.

**Marcel:** Right.

**Marcel:** And so had we addressed that at that spike, there's a likelihood that we would be even higher now.

**Marcel:** Right.

**Marcel:** But it's.

**Marcel:** No, it's better to address it fast like we did.

**Marcel:** But it's like it wasn't that fast.

**Marcel:** It was like a week later.

**Marcel:** That was also manual.

**Marcel:** So everything there was check that has 10,000 pages.

**Marcel:** We're struck in gold in some places, like anthropic one of the pages, cursor pricing and people are not catching.

**Marcel:** So.

**Ryan Singer:** This should be surfacing and learn and improve.

**Marcel:** Yes, yes, it should.

**Ryan Singer:** Okay, so what I think is, I think that we've gone warmer with this kind of.

**Ryan Singer:** I think we shared a lot of domain knowledge with what we did here.

**Marcel:** Yeah.

**Ryan Singer:** But I want to make sure is that we don't think that we've solved it when like this kind of thing is the real problem.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Like this is like a real case.

**Ryan Singer:** So I want to check like, does this actually map to what we talked about?

**Ryan Singer:** And is all this like general stuff, like real or is it more complicated than that?

**Ryan Singer:** In reality.

**Marcel:** Sorry, it's called a little fire drill.

**Marcel:** My.

**Marcel:** My EA accidentally share comp information on a public or like an executive that we're hiring.

**Marcel:** Like, what the.

**Marcel:** What the hell?

**Marcel:** Sorry.

**Ryan Singer:** Brutal.

**Marcel:** Can you repeat that?

**Marcel:** I apologize.

**Ryan Singer:** Okay, so the thing is, okay, so briefly, what happened was like, we.

**Ryan Singer:** We've been kind of sketching it, like, sketching out a lot of what's in your head, Marcel, around what optimization means.

**Marcel:** Right.

**Ryan Singer:** And my concern is we might not have gone deep enough.

**Ryan Singer:** And what I want to do is I want to use this as a test case of like, this is a real kind of thing that we want to be able to surface, right?

**Ryan Singer:** So I think what we want to be able to say is, like, what is this?

**Marcel:** Right?

**Ryan Singer:** And then this is the kind of like, concreteness of specific cases of like, this is the kind of thing we should be surfacing in terms of detection and action.

**Marcel:** Yeah.

**Marcel:** Like there.

**Marcel:** Okay, so if you look.

**Marcel:** If you think back of like what Daniel was showing on the filters and things like that, right?

**Ryan Singer:** Yep.

**Marcel:** Normally it's like you do a bunch of stuff, you publish a bunch of pages or whatever when you're actively doing it, like what we're doing, and check that, like, there would be signals, right?

**Marcel:** And those signals will tell you we did something.

**Marcel:** Right?

**Marcel:** And usually those signals would be like, oh, look, this got indexed.

**Marcel:** That's good.

**Marcel:** Like, you know, and then it was like, followed by, whoa, this got some impressions.

**Marcel:** Index is not even bad impressions.

**Marcel:** It's just got indexed.

**Marcel:** Yeah, yeah.

**Marcel:** And then like, okay, so this thing got impressions, but it's not getting clicks now all of a sudden, right?

**Marcel:** So now it's like, okay, if you do nothing, let's just say there's one page, that page is getting impressions consistently and no clicks.

**Marcel:** There are many pages on Google Search Console, Ryan, that they will not gonna have the purple.

**Marcel:** Like, you see the impressions.

**Marcel:** Shit ton of impressions and zero clicks, you know?

**Ryan Singer:** Yeah.

**Marcel:** That's about a concrete example.

**Marcel:** So, so.

**Marcel:** So then you're like, look, we got impressions.

**Marcel:** That means probably we got the opportunity, right?

**Marcel:** And we got the intent somewhat right.

**Marcel:** But it either means like the.

**Marcel:** The headline or, you know, the.

**Marcel:** The.

**Marcel:** The promise of the page is still off from the intent that we're getting.

**Marcel:** It also means, like, there.

**Marcel:** It could also mean that you just need to do something a little bit more to drive the like, average position a little bit higher.

**Marcel:** Right?

**Marcel:** Like, and so then it's like, truly, you know, like, hey, we need to link to it a little bit more.

**Marcel:** You need to like, try to Get a little bit higher because sometimes you're getting a click.

**Marcel:** This is truly like a garbage search.

**Marcel:** And it's like positioned solo on the page.

**Marcel:** No one's seeing it, right?

**Marcel:** Like an impression doesn't mean somebody actually saw it, right?

**Marcel:** And the thing within your control is like, go optimize the meta title, headline, meta description, things like that, and see if it improves, right?

**Marcel:** See if you actually get some clicks, you know, if not, wait a little longer and if you see nothing, then try like some other optimizations.

**Marcel:** Normally my hack here is like link to it and try to like force it to.

**Marcel:** For Google to think this is really important to try to force Google to like rank you a little bit higher to see if you get clicks, right?

**Marcel:** But I usually do the headline first and that's second, right?

**Marcel:** And this is just like one, one page.

**Marcel:** Then let's say you start to get clicks.

**Marcel:** The second you get clicks, it's like now all of a sudden you're in like watch mode, right?

**Marcel:** And you're ideally, if you only had one page on your site and that's the only page you care about, like, you're just like watching it like a hawk, right?

**Marcel:** And the second you get clicks, you're like, is this like, are people like spending time on this?

**Marcel:** Are they.

**Marcel:** Is the bounce higher?

**Marcel:** Right?

**Marcel:** Best case scenario is like, can I just like record the fucking session and see what happened?

**Marcel:** Right?

**Marcel:** And those signals are like the most.

**Marcel:** It's like your first impressions to Google on this page, right?

**Marcel:** They're like super, super, super, super important.

**Marcel:** And you want to watch it like a hawk.

**Marcel:** And then very, very, very, very quickly respond to it.

**Marcel:** And, and the response to it is either, holy crap, like people are spending three minutes on this and it's three times higher than every other page on the site.

**Marcel:** We did something right, hey, let's go try to do this again in other places.

**Marcel:** Or hey, we read this and this is pretty shallow.

**Marcel:** We should rethink this content completely, which is what we did with Cursor.

**Marcel:** But it's very subjective because for instance, the same pipeline that generated this cursor page also generated this HeyGen page.

**Marcel:** And, and the hey, gen page never had a dip in.

**Marcel:** And so like, if you look at this, it's like this page never had a dip, you know?

**Marcel:** And so you're like, okay, this is like the same pipeline, you know?

**Marcel:** And it's just like a audience for Cursor.

**Marcel:** You know, Anecdotally I think it's because an audience for agent, like, it's kind of like lower.

**Marcel:** It's just like random consumers kind of thing.

**Marcel:** Whereas cursor is like, highly sophisticated.

**Marcel:** Like people that are doing really deep research.

**Marcel:** Research and care a lot about the details, how it's presented and whatnot.

**Marcel:** Whereas, like, agents, like, a little bit more, like, generic.

**Marcel:** Like, you know, that's my hypothesis.

**Marcel:** Just like the audience.

**Marcel:** Right.

**Marcel:** One audience is, like, more technical than the other and cares more about services, you know, like.

**Marcel:** But you can see, like, you know, like finding the Pretty.

**Marcel:** Pretty hard at scale.

**Ryan Singer:** Yeah.

**Marcel:** Okay.

**Marcel:** Yeah.

**Ryan Singer:** We'Ve.

**Ryan Singer:** I'm looking at where we're at with time.

**Ryan Singer:** Let's.

**Ryan Singer:** Let's take five.

**Marcel:** Yeah.

**Marcel:** Is.

**Ryan Singer:** Is.

**Ryan Singer:** Is five enough or do you guys need 10 works?

**Marcel:** Five work?

**Marcel:** Yeah.

**Ryan Singer:** Okay, let's do five and we'll see in five.

**Marcel:** This is such a complex domain.

**Marcel:** Yeah.

**Marcel:** There's so much things back into every corner of the.

**Marcel:** There's so much loading through.

**Marcel:** You're almost in the first stage.

**Marcel:** What's going on?

**Marcel:** It.

**Marcel:** That's.

**Marcel:** Yeah, Just Open Office was like one of the crane.

**Marcel:** Look, I love.

**Marcel:** Yeah, I like how they name the room.

**Marcel:** Was it happening?

**Marcel:** You know, it's like when you're like, a couple of set functions away from, like, cracking it.

**Marcel:** Imagine that, like, Brian doing this and having to do, like, interviews with users in order to get to this truth.

**Ryan Singer:** Oh, man.

**Marcel:** You know, that's why we have so much confidence in what we're doing, because it's just like, so many years of, like, doing this for so many different companies that are all successful, you know?

**Marcel:** And like, that's what's fun about this.

**Ryan Singer:** Project is it's like, it's.

**Ryan Singer:** I feel like it's all about, like, how do we.

**Ryan Singer:** How do we, like, funnel all this stuff that you already know into this product?

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** It's not like the head scratching of how does it work.

**Ryan Singer:** It's like, we know how this works.

**Ryan Singer:** How the heck do we, like, get.

**Marcel:** It in here, you know, like, simplify it and give, like, customers, like the end user, like, a sense of control versus, like, there's things where truly, like, we don't kind of need their opinion.

**Marcel:** And then there's like, little nuanced things like what you were saying, like, should you archive this or should you, like, repurpose?

**Marcel:** Like, it would probably be a gnarly agent, but then a human judgment is actually decently easier here, you know?

**Marcel:** Like, it's kind of like this weird thing about AI sometimes there's things that are like, agents are 100 times better on really hard to do.

**Marcel:** Complex things, like snapshots.

**Marcel:** And then like on the simplest thing, it's just like, no, no, just have a human review.

**Marcel:** It's like.

**Marcel:** It'll take 10 seconds.

**Marcel:** Like, don't worry.

**Marcel:** Totally, totally.

**Marcel:** This is very counter, you know, so.

**Ryan Singer:** Okay, so what I want to do is I want to step back and.

**Ryan Singer:** Because I feel like we could just kind of talk about optimization as a science all day, you know, And I want to.

**Ryan Singer:** What I want to do is I want to bring this kind of back to you, Daniel.

**Ryan Singer:** Around kind of.

**Ryan Singer:** Where's the question?

**Ryan Singer:** So my understanding was that like.

**Ryan Singer:** Like we moved the pipeline for creation out of Learn and improve, and now there's like a missing piece, which is like the pipeline piece is kind of missing there.

**Ryan Singer:** And I'm wondering, like, do we want to take all this kind of shared context that we built up now and do we want to look at what is that pipeline of work inside of Learn and improve, or is it a different question?

**Marcel:** I think that would be an interesting experiment because.

**Marcel:** There are tools in the market that try to do the included part and they're definitely better than nothing.

**Marcel:** And they've done really well financially, everything, because it's a real hard problem and the bar is so low.

**Marcel:** Like what Marcel is driving, that is the whole holy grail of like organic content, like tracking everything, knowing where things are getting traffic.

**Marcel:** None of the tools do that.

**Marcel:** They just do at the page level.

**Marcel:** The most basic things, just like fix your broken links, fix your.

**Marcel:** Your headings.

**Marcel:** That alone is valuable.

**Marcel:** The closer we can get to the stuff that Marcel is describing.

**Marcel:** Yeah, that is mind blowing for what the public is used to, you know.

**Ryan Singer:** Oh, it's huge.

**Ryan Singer:** You know, it's totally huge.

**Marcel:** An example here, really quick.

**Marcel:** And I think that place where we have in the system today, if the learning improve, if the create is out of it, and that's a different problem.

**Marcel:** And we can crack that if there is a path to make that concrete in that same user interface with the same simplicity of the separation that we have now.

**Marcel:** I think we're really close to something that's way better than server SEO, for example, that is closer to achieving what Marcel is.

**Marcel:** The pipeline there can work.

**Marcel:** It's worth trying.

**Marcel:** Yeah.

**Marcel:** And just so you understand how relevant this is right now, Ramp is a customer and then Brex is a customer, and then we just kicked off, or we're kicking off today with Spendesk, which is like a European version of it.

**Marcel:** Right.

**Marcel:** And essentially, like, this is what we're dealing with.

**Marcel:** Like, like their traffic is like in Free Fall.

**Marcel:** And they hired us essentially, and a highly competitive space, right?

**Ryan Singer:** And.

**Marcel:** And like, we did all this manually.

**Marcel:** Like, everything you see here is just like, like manually done to try to like, give them, like, what you go focus on.

**Marcel:** It's all based on new opportunities.

**Marcel:** And I was like, guys, what the.

**Marcel:** What the f. Like, they have 700 pages.

**Marcel:** Like, you know, and so you go here and you go like, hey, like, like this is.

**Marcel:** It's.

**Marcel:** It's in the climb.

**Marcel:** It's in like free fall.

**Ryan Singer:** And.

**Marcel:** And like, how do you know what to do here?

**Marcel:** There's 712 of them, right?

**Marcel:** Like, all these are dropping.

**Marcel:** Which one should you focus on?

**Marcel:** And why.

**Marcel:** Why is this.

**Marcel:** Yeah, is that a good thing or bad thing?

**Marcel:** It's like.

**Marcel:** Or, you know, is that like even just the realization of that you have 700 pages?

**Marcel:** You shouldn't be thinking too much about creating your pages.

**Marcel:** Just go fix that.

**Marcel:** Having the place in the app that tells you that that is also something that even our team isn't thinking about it.

**Marcel:** And our team is really good compared to the rest of the market.

**Marcel:** So then what people will do here, Right, Exactly.

**Marcel:** They'll come here and they'll just hit export on this, and this is all the data you have, and then they'll do an analysis completely absent of the context of the company.

**Marcel:** And anything else just looks at this, right?

**Marcel:** And all you have is a URL and it has no context of anything else.

**Marcel:** No signals or anything else.

**Marcel:** And it's just like, fuck, this is so bad.

**Marcel:** And this is literally what our team does too.

**Marcel:** And what I've had to do, right?

**Marcel:** There's nothing else.

**Marcel:** And so then the next best thing I would do is I would build a scraper to go through each URL and do a summary of the content of the URL, and then build all these play tables or processes or whatever.

**Marcel:** But then those didn't have GA data, right?

**Marcel:** Or GSC data.

**Marcel:** It was just this data.

**Marcel:** So anyways, like, it's just truly a pain point.

**Ryan Singer:** Oh my God.

**Ryan Singer:** My, my.

**Ryan Singer:** Like, my eyes are watering.

**Ryan Singer:** There's so much opportunity here.

**Ryan Singer:** Like, I can't handle it.

**Marcel:** It is like every site on the planet is dealing with this and there is no good solution in this.

**Marcel:** Like, like, this is like, I have so much conviction in this, man.

**Ryan Singer:** Okay, yeah, like, I'm.

**Ryan Singer:** I'm like, I'm a million percent with you on the conviction.

**Ryan Singer:** Okay, so here's the question.

**Ryan Singer:** What are we trying to solve for March?

**Marcel:** Low hanging fruit.

**Marcel:** Urgent.

**Marcel:** Like, do this or you're like improvement metrics based, right?

**Marcel:** Like metric space.

**Ryan Singer:** Okay.

**Marcel:** Or like this is bad, right?

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Marcel:** So for instance, like if your biggest traffic driver just dipped, you should just drop everything you're doing.

**Marcel:** This is a P0 critical bug.

**Marcel:** Go fucking fix it.

**Marcel:** Right.

**Marcel:** And we should publish nothing until like we figure out what just happened there with our.

**Marcel:** One of our biggest customers augment code that happened to two of our biggest traffic diver.

**Marcel:** We didn't catch it for four weeks and then we didn't fix it for another four.

**Marcel:** And it really cost us like a lot.

**Marcel:** Yeah, essentially.

**Ryan Singer:** So what.

**Ryan Singer:** What else?

**Ryan Singer:** Like literally, like what's the list of things where it's like, we can do that for march?

**Ryan Singer:** Those are the things that we can catch that you absolutely should be catching.

**Marcel:** I think like the, the fixed stuff is just super no brainer because it's just very like rules based and we can start with a few rules and then build more rules and the refresh is truly just expired label on it.

**Marcel:** And then the improve is based on those like those filters that Daniel already built, which is like almost to the first page.

**Marcel:** You know, traffic dipped, impressions dip like, like again, it's like very rules based.

**Marcel:** But metrics, your biggest.

**Ryan Singer:** Your biggest traffic page just dipped.

**Ryan Singer:** Is that included in that?

**Marcel:** Yeah, yeah, that.

**Ryan Singer:** It's.

**Marcel:** It's just like, like improve is.

**Marcel:** Is like the dude.

**Ryan Singer:** So give me the top three.

**Ryan Singer:** Give me the top three smart filters for improve that like are real.

**Ryan Singer:** For.

**Ryan Singer:** For March, your.

**Marcel:** Traffic just dip.

**Marcel:** Your engagement.

**Marcel:** It is just dipped for as.

**Marcel:** Because that's like a leading indicator of everything else that's gonna happen soon, you know, and impressions, no clicks or you drop average rank or you're almost in the first page, which is kind of like all similar actions, which is just like you're almost there, you know, like, it's like you.

**Marcel:** But you didn't quite get the signals you needed to make it to the next.

**Ryan Singer:** Okay.

**Marcel:** You know.

**Ryan Singer:** These are very meaningful.

**Ryan Singer:** Okay.

**Ryan Singer:** Dumb question.

**Ryan Singer:** Do they have.

**Ryan Singer:** Do these happen?

**Ryan Singer:** Like all.

**Ryan Singer:** Are there multiple of these?

**Ryan Singer:** If.

**Ryan Singer:** If this wasn't a filter.

**Ryan Singer:** Yeah, but this was a.

**Ryan Singer:** This was a like label.

**Ryan Singer:** Yeah, but if this was a diagnosis.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Let me, let me, let me grab all these.

**Marcel:** Let me grab a critical thing.

**Ryan Singer:** Let me say like possible states per page.

**Ryan Singer:** Okay.

**Ryan Singer:** Possible diagnoses per page.

**Ryan Singer:** I'm going to paste these.

**Marcel:** Your.

**Ryan Singer:** Your biggest traffic page.

**Ryan Singer:** This is.

**Ryan Singer:** This is a, A big traffic page that dipped.

**Marcel:** Yeah.

**Ryan Singer:** Engagement dip died impressions, but no clicks.

**Ryan Singer:** You're almost there.

**Ryan Singer:** Then here was.

**Ryan Singer:** I'm going to say rule broken.

**Marcel:** Yeah.

**Ryan Singer:** And expired, out of date, past good, whatever, you know.

**Marcel:** Yeah.

**Marcel:** It's like, think of it as like, some of these are preventive and some of these are like, you're.

**Marcel:** You're already sick.

**Marcel:** Like, now you gotta go, you know, it's like some of these are like, you know.

**Marcel:** Yeah, yeah.

**Ryan Singer:** But severity.

**Marcel:** Yeah.

**Ryan Singer:** What.

**Ryan Singer:** What's the severity?

**Marcel:** So any.

**Marcel:** Anything that is not preventive, it's going to be pretty high.

**Ryan Singer:** But.

**Marcel:** And then the.

**Marcel:** The further it is on, like, you know, if we had conversion pixels already, it would be like, conversion is the highest, you know, engagement is the second.

**Marcel:** Because you already got people through the site.

**Marcel:** You know how many things have to happen for them to get to the fucking site?

**Marcel:** Like so much.

**Marcel:** Right.

**Marcel:** Like, and then you just like, fuck that up.

**Marcel:** Right?

**Marcel:** And then like, traffic dip is like, oh, bro.

**Marcel:** Like, if you don't get traffic, there's no chance you're ever gonna get conversions.

**Marcel:** You know, Impressions like, dude, the first one is like a high alert, high severity.

**Marcel:** Yeah.

**Marcel:** That is like the secret.

**Marcel:** You did nothing, but you just keep improving your biggest traffic drivers.

**Ryan Singer:** Yeah.

**Marcel:** What I was saying is like, if we had conversion, it would be the highest thing.

**Marcel:** Oh, yeah, okay.

**Ryan Singer:** Like, because it's like there might be.

**Marcel:** A broken link to your cta.

**Ryan Singer:** Go.

**Ryan Singer:** Fucking given.

**Ryan Singer:** Yeah.

**Ryan Singer:** But given what we have, because we're in the March conversation of these, just how could we flag these as, like, let's say, let's say like severe or like worth looking at because maybe you can pick up something, you know what I mean?

**Ryan Singer:** Versus, like when you have time.

**Marcel:** Yeah.

**Marcel:** It's like the first one is important energy.

**Marcel:** The second one is important and will be urgent if you don't do anything about it.

**Marcel:** This is like the.

**Marcel:** And then the.

**Marcel:** The rest is like, like.

**Ryan Singer:** Is it more.

**Ryan Singer:** Are the rest more, like opportunities?

**Ryan Singer:** But rule broken is.

**Ryan Singer:** Is.

**Marcel:** Rule broken is a big deal.

**Marcel:** Yeah.

**Marcel:** Yeah.

**Ryan Singer:** Sorry.

**Marcel:** Rules broken is important if it's a high impact page, but if it's like a dead in the water page, who gives a.

**Marcel:** Like, don't go.

**Ryan Singer:** Okay.

**Marcel:** Not fix the first one, right?

**Marcel:** Yes.

**Marcel:** Or don't do optimization on pages are almost there.

**Marcel:** Because you're trying to fix a thing that has dead in the water.

**Ryan Singer:** And so let me.

**Ryan Singer:** Let me rename this fix.

**Ryan Singer:** High impact are high impact rule broken.

**Marcel:** Yeah.

**Marcel:** Yep.

**Ryan Singer:** Needs fix.

**Marcel:** Yeah.

**Ryan Singer:** Can we expire?

**Marcel:** It's just like, who cares?

**Marcel:** Like, like everybody, one of our customers has 10,000 pages.

**Marcel:** Like, who cares?

**Marcel:** They have like so much signal.

**Marcel:** There is almost like a modifier Here, if it's a high impact page, almost everything bumps the priority.

**Marcel:** Yeah.

**Ryan Singer:** Do we already have the ability today to say which page is high impact and which page isn't?

**Marcel:** This is based on traffic right now.

**Marcel:** That's what we're working right now.

**Marcel:** So, like, this, all the UI that we have with the metrics and everything will enable us to do that.

**Ryan Singer:** Right.

**Ryan Singer:** But where are we for March?

**Ryan Singer:** Like, what, what of this can we actually translate into?

**Ryan Singer:** Like, this is data we have in some.

**Ryan Singer:** Some version of this where we could actually.

**Ryan Singer:** Here's what I'm picturing.

**Ryan Singer:** I want to have.

**Marcel:** Yeah, yeah.

**Ryan Singer:** So high impact.

**Ryan Singer:** Just.

**Ryan Singer:** Just translate this then make this more concrete.

**Ryan Singer:** This is, this is like, well trafficked.

**Ryan Singer:** Like, what is this?

**Marcel:** Yeah, let's just assume everything is high traffic.

**Marcel:** Yeah.

**Marcel:** Fully engaged.

**Marcel:** And the thing is, like, Ryan, like, right now it's going to be high traffic, but in the future it's like high traffic.

**Marcel:** And with the qualifier of like, the intent of the page.

**Marcel:** Right.

**Marcel:** Like, so high traffic to like, what is a CFO versus a CEO do is like low intent traffic.

**Ryan Singer:** Yes.

**Marcel:** Which I have, like, high volume.

**Marcel:** So high volume, low intent.

**Marcel:** Whereas like, a high volume, high intent is like, like at the highest.

**Marcel:** Right.

**Marcel:** Like, but, but that's like.

**Marcel:** Because that is where.

**Marcel:** Because I don't think we're tracking that.

**Marcel:** And it's easy to track, actually.

**Marcel:** Yeah, it's like, it's like.

**Marcel:** So there's a few things, like we.

**Marcel:** For opportunities, we track intent.

**Marcel:** Yeah, I think.

**Marcel:** And then we track relevance.

**Marcel:** But then for pages, we're literally writing the page analysis this week, so I want to make sure I don't forget.

**Ryan Singer:** Yeah.

**Ryan Singer:** So for new page opportunities, high volume, high intent is a thing because you're tracking intent for new page opportunities.

**Ryan Singer:** But here in optimization, we have.

**Marcel:** Okay, so we can still figure out the intent on the existing pages because we're going to analyze the existing pages too, the semantics of it.

**Marcel:** So that works.

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Marcel:** I think I would have everything.

**Marcel:** The only thing we don't have, I guess, expired.

**Marcel:** We could have to, by the way, just to note relevance is really important.

**Marcel:** There's a lot of sites, like Deep ram, for example, where there's like, a lot of, like, pages are just not that relevant.

**Marcel:** And they were there for more, like, traffic boosts.

**Marcel:** You know, they're just like, not relevant to your audience at all.

**Marcel:** Yeah, like the low relevance, you know, so relevance fits into high intent.

**Marcel:** Right.

**Marcel:** They're just.

**Ryan Singer:** Okay, let me, let me, let me, let me try and, Let me try and simplify this.

**Ryan Singer:** Let's boil this down.

**Ryan Singer:** Assuming, let's take, let's say there's a first cut, right.

**Ryan Singer:** Of pages that are high traffic or were or were recently.

**Ryan Singer:** Right.

**Ryan Singer:** Like high traffic now or recently high relevance.

**Marcel:** Is.

**Ryan Singer:** Is relevance different than intent?

**Marcel:** Yeah.

**Marcel:** So for instance, with Lovable, we have a alternatives, right.

**Marcel:** Or a comparison page where it's just like Zapier versus make and that's us trying to grab that traffic.

**Marcel:** That traffic is high intent and high relevance to Zapier, if that was on Zapier's page.

**Marcel:** To Lovable, it's like a high intent type of query.

**Marcel:** But it's like low relevance or lower relevance because it's just like we're trying to go after people searching on comparisons of two apps, hoping that they eventually will connect the DOT to.

**Marcel:** I should just fucking build this myself because it's AI and I can just buy code of, you know, okay, our.

**Ryan Singer:** Relevance in different things that you.

**Marcel:** Versus Lovable.

**Marcel:** That's high intent, high relevance and high importance because it's our third biggest traffic driver on the site.

**Marcel:** So that would be like the whole grill.

**Ryan Singer:** Which, which of these do you.

**Ryan Singer:** Do you have these things already today that you could report per page?

**Ryan Singer:** Or is this a future.

**Marcel:** But we can run that page.

**Marcel:** We're building that for pages.

**Marcel:** And this is part of the milestone UI that I showed you from UP includes scraping your entire website and analyzing everything.

**Marcel:** So we're going to.

**Ryan Singer:** Okay.

**Ryan Singer:** Okay.

**Marcel:** The first follow for any optimization will have access to the space.

**Marcel:** It's mostly taking the workflow that's the post processing, but the crawler is right there.

**Ryan Singer:** So here's a question.

**Ryan Singer:** Is our relevance and intent?

**Ryan Singer:** Now let me ask this carefully.

**Ryan Singer:** Do I have to have high relevance and high intent for anything to qualify as an optimization, or do I optimize to improve relevance and intent?

**Marcel:** No.

**Marcel:** So relevance and intent are more about the opportunity under the hood of that surface area.

**Marcel:** And you know, there are cases where, like it could be fake.

**Marcel:** Right?

**Ryan Singer:** Like.

**Marcel:** So, for instance, like.

**Marcel:** Yeah, yeah, I'm.

**Ryan Singer:** You're already.

**Ryan Singer:** I, I, I just.

**Ryan Singer:** Because time is going so fast, I want to.

**Ryan Singer:** What?

**Ryan Singer:** I want to.

**Ryan Singer:** What?

**Marcel:** I.

**Ryan Singer:** What I think, I think we just captured something really important, which is that when it comes to opportunities, there's, there's a.

**Ryan Singer:** If, if these.

**Ryan Singer:** Sorry, if.

**Ryan Singer:** Opportunities.

**Ryan Singer:** Optimizations.

**Ryan Singer:** Optimizations.

**Ryan Singer:** When it comes to learn and improve optimizations, there are pages that are not, they don't.

**Ryan Singer:** Out of the 712, we shouldn't even be looking at them because.

**Ryan Singer:** Because a underlying opportunity isn't there.

**Marcel:** Right, Right.

**Marcel:** That Is very, very good point.

**Marcel:** Yeah.

**Ryan Singer:** So this is a very different degree of freedom in the system.

**Ryan Singer:** Right.

**Ryan Singer:** This is orthogonal to like what is the thing I'm trying to fix.

**Marcel:** Yeah.

**Marcel:** And, and I.

**Marcel:** That, that's a really cool thing which is like, I like this mental model which is like every page should have an opportunity brief under the hood that backs it.

**Ryan Singer:** Yes.

**Marcel:** The page context.

**Marcel:** That part of the context is the opportunity context of that page.

**Marcel:** Then there's like where the pageant is today, you know, because it's like opportunities will quantify.

**Ryan Singer:** It's like it's like a ball and a glove.

**Ryan Singer:** Like the opportunity is the glove and then like the ball is like, you know, but like you, you.

**Ryan Singer:** They're.

**Ryan Singer:** They're different things.

**Ryan Singer:** Given that the underlying opportunity is there, then these different things become relevant.

**Ryan Singer:** So what happens was what I want to do is I want to take away high traffic from needs fix.

**Ryan Singer:** I want to take away high traffic from expired and I want to say possible diagnoses per.

**Ryan Singer:** I'm going to call it page with opportunity.

**Marcel:** So just one thing here.

**Marcel:** It's.

**Marcel:** There's a very important distinction of realized versus unrealized opportunity.

**Ryan Singer:** Okay.

**Marcel:** And so if the aggregate opportunity here is let's say 10,000 visits a month and you're at like 9,700, like it's pretty realized and any fuck ups there will like hurt you where.

**Marcel:** So it's more urgent.

**Marcel:** Whereas like unrealized opportunities, it's a lot more like optimizations to try to realize more of it, you know, but there's less to lose.

**Marcel:** Like, like you have nothing to lose essentially.

**Marcel:** Right.

**Marcel:** You have a lot to gain and nothing to lose.

**Marcel:** Whereas like realized opportunities, you're 97 realized you have a lot to lose and very little to gain.

**Marcel:** Okay.

**Ryan Singer:** So when we, when we like offense.

**Marcel:** Versus defense a little bit.

**Ryan Singer:** Totally.

**Ryan Singer:** When we surface pages again, we're looking at the 712.

**Marcel:** Yeah.

**Ryan Singer:** When we, when we surface pages from the 712 to go work on first is that remove anything where there's no underlying opportunity.

**Ryan Singer:** Remove anything where there is a well realized opportunity and just give me unrealized opportunity.

**Marcel:** No, no, on the realized opportunity you're trying to prevent fuck ups.

**Marcel:** So it's like those you shouldn't.

**Marcel:** That is the highest.

**Marcel:** Highest is like realized opportunities with things that you can prevent now from causing pain in the future.

**Marcel:** Yeah.

**Marcel:** Huh.

**Ryan Singer:** Okay.

**Ryan Singer:** What it is that now tell me like what.

**Ryan Singer:** Okay.

**Ryan Singer:** Okay.

**Ryan Singer:** So underlying opportunity has two classes here.

**Ryan Singer:** There's realized and unrealized.

**Marcel:** Yes.

**Marcel:** Sorry.

**Ryan Singer:** Yeah.

**Marcel:** Let me just really quickly so there's realized and unrealized or realized.

**Marcel:** There is.

**Marcel:** This is a free fall.

**Marcel:** Drop everything.

**Marcel:** That's the highest tier.

**Marcel:** And then there's like, hey, it's realized.

**Marcel:** And these are like screaming alerts.

**Marcel:** They're going to churn if you don't do something about it right now.

**Marcel:** And you can still prevent it.

**Marcel:** Right?

**Marcel:** That's the next one.

**Marcel:** And then after that is everything else screaming alerts.

**Ryan Singer:** You can prevent it.

**Ryan Singer:** What's that?

**Marcel:** Like, this page is broken.

**Marcel:** There's a 404 as the ultimate.

**Marcel:** Right.

**Marcel:** Like.

**Marcel:** Or it could be like, you know, like the things you collective.

**Marcel:** Like, then there's one in this page.

**Ryan Singer:** Yeah, yeah, yeah, totally.

**Ryan Singer:** Okay, got it.

**Ryan Singer:** Okay.

**Marcel:** Somebody.

**Marcel:** The bucky redesign off the website and switches page one, stage two.

**Marcel:** Yeah, got it.

**Ryan Singer:** Okay.

**Ryan Singer:** So if I have a realized opportunity.

**Ryan Singer:** Okay, I have a realized opportunity.

**Ryan Singer:** I need to.

**Ryan Singer:** If.

**Ryan Singer:** If it's in freefall, then I have to.

**Ryan Singer:** I have to.

**Ryan Singer:** I have to immediately jump on it to try and fix it.

**Ryan Singer:** And if there's an alert on it where something is broken, I have to jump in and fix it.

**Marcel:** Yeah.

**Marcel:** Center for paper.

**Marcel:** Right now it's century, but very soon it becomes a B.

**Marcel:** Testing.

**Marcel:** Yeah.

**Marcel:** Yeah.

**Marcel:** You know, once you get into the.

**Marcel:** You fixed and you maintain everything.

**Marcel:** Now it's about experimentation.

**Marcel:** Yeah.

**Ryan Singer:** Okay, so here's.

**Ryan Singer:** Here's what.

**Ryan Singer:** Here's where my head is going.

**Ryan Singer:** Okay.

**Marcel:** That's like the best kind of.

**Marcel:** It's like, there's so much to be done, so much to do, so much opportunity.

**Ryan Singer:** Yeah, there's a lot here.

**Ryan Singer:** All right.

**Ryan Singer:** At a minimum, like.

**Ryan Singer:** Okay, I'm just going to zoom out for a second.

**Ryan Singer:** Like, here's.

**Ryan Singer:** This is just my UX instinct speaking, and I don't even know how to explain it right yet.

**Ryan Singer:** When I.

**Ryan Singer:** When I see, like, filter by.

**Ryan Singer:** What was it?

**Ryan Singer:** Is it even in the screenshot here?

**Ryan Singer:** No.

**Ryan Singer:** When we were looking at learn and improve or.

**Ryan Singer:** No, we were looking at.

**Ryan Singer:** Where were we?

**Ryan Singer:** We were learning improve, but we were on page portfolio and there was a smart filter and it was kind of like.

**Ryan Singer:** Like top performers, but like something.

**Ryan Singer:** What was it?

**Ryan Singer:** Yeah, sharing.

**Marcel:** I have.

**Marcel:** So we are in the portfolio, surging.

**Ryan Singer:** In almost top three.

**Ryan Singer:** Yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** Good.

**Ryan Singer:** Okay.

**Ryan Singer:** Okay, good.

**Ryan Singer:** Here, let me just take a.

**Ryan Singer:** Can you move your mouse away?

**Ryan Singer:** And I'm going to take a screenshot of what we're looking at here.

**Ryan Singer:** I'm just going to capture this.

**Ryan Singer:** Boom.

**Ryan Singer:** Okay.

**Ryan Singer:** That's exactly what I wanted.

**Ryan Singer:** I'm going to go back to the whiteboard and I'm going to paste that up here.

**Ryan Singer:** All right, so here's what I'm seeing when I look at this.

**Ryan Singer:** What I'm seeing is this feels really important.

**Ryan Singer:** This is like, like you made this a smart filter because it's something important about these pages, you know?

**Ryan Singer:** But the mismatch in my, in the experience is that like, if I don't look at this tiny little box, all this stuff looks the same as it always does.

**Ryan Singer:** Unless I like, have like some like LLM in my head that can just scan all these and tell me what the numbers mean.

**Ryan Singer:** Okay.

**Ryan Singer:** Like, so what's happening is that, like there's a mismatch here.

**Ryan Singer:** And my first thought about how to address that is to, is to take the thing that is being caught on the filter and make it data.

**Ryan Singer:** So like, if, if this was.

**Ryan Singer:** So, okay, let's replace this with our top again.

**Ryan Singer:** We're filtering the 710, right.

**Ryan Singer:** If there's any of these, we want to fix them first, right?

**Marcel:** Yeah.

**Ryan Singer:** So what I, what I, what I want to see just naively is.

**Marcel:** Giant.

**Ryan Singer:** And.

**Marcel:** I think it's the.

**Marcel:** Is this status state or something.

**Ryan Singer:** It's, it's.

**Ryan Singer:** Yeah.

**Ryan Singer:** So like, I don't know what it is yet.

**Ryan Singer:** It's, it's a kind of smart, Not a smart filter.

**Ryan Singer:** It's a smart status.

**Marcel:** Yeah.

**Ryan Singer:** So this is like.

**Ryan Singer:** Now, this isn't the right word, but what I want to say is realized, like, like.

**Ryan Singer:** And realize.

**Ryan Singer:** We're totally not going to say realize.

**Ryan Singer:** Nobody knows what that means.

**Ryan Singer:** But what I want to say is like, needs fix now.

**Ryan Singer:** Like red alert.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** And then there's gonna be.

**Ryan Singer:** So let's say we've got three of those now.

**Ryan Singer:** If, if we knew that we had this to show anywhere on the page, we wouldn't even ask you to be filtering.

**Ryan Singer:** Like, we would, we would just be like surfacing those.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Like at the very, very, very top.

**Ryan Singer:** So what now?

**Ryan Singer:** Now that, that, that, that naturally jumps us to like a next step in the way of thinking about the UI here, which is like, if I'm just thinking about that, like I would be segmenting on the very top again.

**Ryan Singer:** I'm just thinking about the 712.

**Marcel:** Yeah, right.

**Marcel:** Red alerts.

**Marcel:** 12,000.

**Ryan Singer:** Exactly.

**Ryan Singer:** Yeah, whatever it is.

**Marcel:** Right.

**Ryan Singer:** But you know, we know what I mean.

**Ryan Singer:** We have the reference there.

**Marcel:** Yeah.

**Ryan Singer:** I just want to take anything that's a red alert and I want to put it on the top.

**Ryan Singer:** And you never have to touch a filter because you should never not be seeing that.

**Marcel:** Yeah, right.

**Marcel:** Yeah.

**Ryan Singer:** And then there's like.

**Marcel:** Right.

**Ryan Singer:** And then there's like there's a point, I don't know where the cutoff is.

**Ryan Singer:** There's a cutoff at some point where it's like, like actually, actually I don't even like this.

**Ryan Singer:** I, I don't like the idea that there's ever like now go dig yourself to figure out what to do.

**Ryan Singer:** Like, like, like what is that?

**Ryan Singer:** Like we, the whole point of being in the tool is that like we're not asking you to do this.

**Ryan Singer:** So what I'm, what I'm kind of thinking is that like we should actually have an opinion about what to float up here based on, on this like very specialized domain knowledge that we have.

**Marcel:** Right.

**Ryan Singer:** So like.

**Ryan Singer:** Yeah, this is opinion.

**Ryan Singer:** Yeah.

**Ryan Singer:** These are pages that are working.

**Ryan Singer:** Are working and fucked.

**Ryan Singer:** Do you know what I mean?

**Marcel:** Yeah.

**Ryan Singer:** Like, like right now, like, you know, and then there's going to be this next class which is actually, I'm going to call it a green alert.

**Ryan Singer:** Just because the idea here is like meaningful, unrealized opportunity.

**Ryan Singer:** Yeah.

**Ryan Singer:** Like, you know, and then, and then, and then like again, if I'm looking at the 712 or I'm looking at the 7012, what I want to know is like there's like 518 pages we think are useless.

**Ryan Singer:** Yeah.

**Ryan Singer:** And then, and then like what I want to do in here is like recycle or purge or whatever.

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Like whatever it is like this is that decision that we were talking about earlier.

**Ryan Singer:** So like what, what I'm getting at is that like the fundamental structure of I think learn and improve.

**Ryan Singer:** It's like, it's not a filter, it's not an action.

**Ryan Singer:** It's, it's like this is, this is, this is Marcel's brain that we are trying to turn into a heads up display.

**Marcel:** Yes.

**Marcel:** It's like fix now.

**Marcel:** Unrealized potential dead zone.

**Marcel:** Right.

**Marcel:** Kind of thing.

**Ryan Singer:** Fix, fix now.

**Ryan Singer:** So unrealized potential dead zone.

**Ryan Singer:** Dude.

**Ryan Singer:** So this is like, I love these moments where like I like, I'm trying to like reflect Marcel's brain back at Marcel and then Marcel is like, I'm gonna put the perfect word on that thing because like I know what that is.

**Ryan Singer:** And like whenever that happens, those are, those are really magical moments because these words have a lot of power.

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Like it's Marcel's voice and it's like it's, it's, it's Marcel's voice tied to the domain model, tied to the data Model.

**Marcel:** Right?

**Ryan Singer:** So like, when this, when this UI becomes fix now unrealized potential dead zone, it's like, dude, no app looks like this.

**Ryan Singer:** And it's so meaningful.

**Marcel:** Right?

**Ryan Singer:** And, and, and now it's kind of like where my, where my head goes is like, I feel like the.

**Ryan Singer:** There's work to be done on, like.

**Ryan Singer:** Okay, so what's the pipeline that these things go into, you know?

**Marcel:** Yeah, you can always have like, under the hood, like go explore everything else, like your entire portfolio.

**Marcel:** But like, if you lead with the portfolio, then it's just like you're back at the same thing, which is overwhelming sense of like, I don't know.

**Ryan Singer:** Exactly.

**Ryan Singer:** And like the, the, the.

**Ryan Singer:** The.

**Ryan Singer:** The go digging is the Lee is the least value and, and the better you're doing at turning your brain into software, the less you should ever ask anybody to go go digging.

**Ryan Singer:** It's almost like the.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Like the, the kind of like dig and filter and explore mindset, I feel like, is like the failure state that every other piece of software is in.

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Like, every piece.

**Ryan Singer:** That's.

**Ryan Singer:** That's like, that's.

**Ryan Singer:** That's Google Analytics.

**Ryan Singer:** Like, we don't know what you want.

**Ryan Singer:** We don't know what you want.

**Ryan Singer:** We don't know how to help you.

**Ryan Singer:** But here's your data, right?

**Ryan Singer:** And like, you guys are trying to be the exact opposite of that to the extreme of like, we know what you want.

**Ryan Singer:** We know how this works.

**Ryan Singer:** Works.

**Ryan Singer:** We have all the context.

**Marcel:** The ideal state, to repeat it back to you is like, you should never need to apply a filter.

**Ryan Singer:** Yeah, exactly, exactly.

**Marcel:** The ideal state is like, you have all the contacts.

**Marcel:** Like, that's what LLMs are good at.

**Marcel:** You have.

**Ryan Singer:** Exactly.

**Marcel:** We have all the data, we have all the, you know, like, like the ideal state is like, you should never have to prompt anything.

**Marcel:** You should never have to apply a filter.

**Ryan Singer:** Right?

**Ryan Singer:** You know, so when we go into pipeline already, I feel a little more relaxed because I kind of feel like nailing pipeline is less important when, you know, when the thing that's in the pipeline has clear meaning.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** So like, so we, we talked about these as sections.

**Ryan Singer:** Fix now unrealized potential dead zone.

**Ryan Singer:** I think when it comes to pipeline, what we can do is.

**Ryan Singer:** This is.

**Ryan Singer:** This is a page.

**Ryan Singer:** Okay?

**Ryan Singer:** This is.

**Ryan Singer:** This is.

**Ryan Singer:** This is page.

**Ryan Singer:** Numbers.

**Ryan Singer:** Number.

**Ryan Singer:** Number 512.

**Ryan Singer:** This particular page needs to be fixed now, right?

**Ryan Singer:** Fix now and then, and then.

**Ryan Singer:** Why high traffic, let's say high performer in free fall or whatever.

**Marcel:** Right.

**Marcel:** Yeah.

**Ryan Singer:** And then there's like, so, so the things that I have taken on and clicked to somehow.

**Ryan Singer:** So somehow these things have a.

**Ryan Singer:** Like a.

**Ryan Singer:** You know, there's like a do action on each one of these, right.

**Ryan Singer:** And like, which is like, put into my backlog or like, take this on or assign it to me or I don't know.

**Ryan Singer:** Right.

**Ryan Singer:** Like, accept this as work.

**Marcel:** Yeah, yeah.

**Marcel:** Right.

**Ryan Singer:** So we need to have a state in each one of these of like, okay, if this is fixed now and this is like, we're screwed if we don't fix this.

**Ryan Singer:** Like, is somebody on this?

**Ryan Singer:** Right.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** So that's the thing that we also don't see today.

**Ryan Singer:** Like, if this is truly this important, it's like there's.

**Marcel:** It should be on the side.

**Ryan Singer:** Why am I even going to a backlog?

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Like, like, I'm almost wondering if, like, I want to see.

**Ryan Singer:** Like, like this is totally not the right word.

**Ryan Singer:** Claim.

**Marcel:** Yeah, yeah.

**Ryan Singer:** But like, do you know what I mean?

**Ryan Singer:** Like, like, like what I want is like, like, like, like Jill is on it.

**Ryan Singer:** You know what I mean?

**Marcel:** It's almost like who's on call and on fire?

**Ryan Singer:** Exactly.

**Ryan Singer:** Yeah.

**Ryan Singer:** Like, who's.

**Ryan Singer:** Yeah.

**Ryan Singer:** Who's on it?

**Marcel:** Right?

**Ryan Singer:** Because this is literally, like, this isn't work for later.

**Ryan Singer:** This is like the fix now is the emergency room.

**Ryan Singer:** So I need to know, like, where's the patient?

**Ryan Singer:** Where's the doctor?

**Ryan Singer:** Like, what's going on?

**Marcel:** Right.

**Ryan Singer:** And.

**Ryan Singer:** And if we, if we, if we express this urgency around, like, who is doing it and what is the state?

**Marcel:** It.

**Ryan Singer:** It's very.

**Ryan Singer:** Again, like, it's tying it all together.

**Ryan Singer:** Like what this thing is now.

**Marcel:** This.

**Ryan Singer:** I think it still makes sense.

**Ryan Singer:** Yeah.

**Marcel:** Make sure I'm visualizing the same stuff as you.

**Marcel:** So what you have on the right side, that.

**Marcel:** Those would be the cells of the table that you're thinking the fix now.

**Ryan Singer:** Yeah.

**Ryan Singer:** Sorry.

**Ryan Singer:** So.

**Ryan Singer:** So.

**Ryan Singer:** So this is what.

**Ryan Singer:** What I was.

**Ryan Singer:** Exactly what I was.

**Ryan Singer:** I was.

**Ryan Singer:** I was starting to think about these once they're in the pipeline, but it's the same thing everywhere actually.

**Marcel:** Right.

**Ryan Singer:** Like as a row.

**Ryan Singer:** So let's do that.

**Ryan Singer:** Let's actually just like take this and put it here.

**Marcel:** Can I just one quick think of this.

**Marcel:** Just writing this down.

**Marcel:** That's like.

**Marcel:** Can you zoom into fix now really quickly here on the right side where you have like page five?

**Ryan Singer:** Yes, yes.

**Marcel:** And so in my mind, it's kind of like if you did fix now and you put a box around it and then and then you have high performer and you put another box around it and.

**Marcel:** And then in.

**Marcel:** And then you put another box in it.

**Marcel:** It's essentially like, fix now versus, like, you know, all the other actions then high performance, like high average, low performer or dead in the water.

**Marcel:** And then in free fall can be in free fall, likely to fall, decaying, stable, rising or surging.

**Marcel:** You know, like.

**Ryan Singer:** Yeah.

**Marcel:** Does that make sense?

**Marcel:** Like, and, and then like, like, we just.

**Marcel:** That's it, right?

**Marcel:** Like, that's kind of it.

**Marcel:** That's like, all you should care about.

**Marcel:** Like, everything else is details and backup.

**Ryan Singer:** Yeah, yeah, that's.

**Ryan Singer:** That's.

**Ryan Singer:** That's.

**Ryan Singer:** I.

**Ryan Singer:** Like, yeah, yeah.

**Marcel:** Does that make sense?

**Marcel:** I don't know.

**Marcel:** I was trying to write it down as we were talking.

**Marcel:** So it's like, wait, hold on.

**Marcel:** There might be something here to simplify the out of this versus, like 50 numbers everywhere in a table.

**Ryan Singer:** No, that's.

**Ryan Singer:** That's.

**Marcel:** That's exact.

**Ryan Singer:** No, that.

**Ryan Singer:** Exactly.

**Ryan Singer:** No, like, exactly.

**Ryan Singer:** So this coming back to this, this is exactly what we shouldn't have to look at.

**Marcel:** Like, I don't know what to do with this.

**Marcel:** Like, I don't know what to do with this power.

**Marcel:** That.

**Marcel:** Right.

**Marcel:** Yeah.

**Ryan Singer:** This, this is, this is back in that Google Analytics thing of like, we don't know what you want, we don't know what you need.

**Ryan Singer:** So, like, good luck.

**Ryan Singer:** Here's the data.

**Marcel:** Yeah, it's like, slightly more abstracted, but.

**Marcel:** But, like, not actionable.

**Ryan Singer:** It's still assuming that you have a.

**Ryan Singer:** This.

**Ryan Singer:** The model of, like, what matters and what am I looking for is in the head of the user.

**Ryan Singer:** And this is just the.

**Ryan Singer:** The data.

**Ryan Singer:** And the user has to be the LLM, you know, So I think, I think that's actually huge, which is.

**Ryan Singer:** I think that's really huge to call that out.

**Ryan Singer:** That, like, it's not just about the, like, smart labels.

**Ryan Singer:** It's also about killing the numbers.

**Ryan Singer:** Now, okay, we can.

**Ryan Singer:** You can click through to this page and we can show you numbers in the context of this problem.

**Marcel:** Right.

**Ryan Singer:** So we can say, like, this is a high performer because, you know, and it's in free fall because, look, like.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Like, here's the, like, exactly what you.

**Ryan Singer:** Like, you know, like, here's the chart.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Like, yeah, like, this is why you're seeing this.

**Ryan Singer:** But, but.

**Ryan Singer:** But this is totally.

**Ryan Singer:** Like, I don't even need this if I trust this.

**Marcel:** Yeah, right.

**Marcel:** Yeah, it's all relative.

**Marcel:** Right?

**Marcel:** Like, you can put something at like 1500 or whatever, you know, yeah.

**Ryan Singer:** Now the, the one, the place where I would say is that if I look at this in isolation, I want to have all these pieces and if I'm, if, if we have a kind of a triage view, we probably subtract the things that are true for all of them.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Like, because these are all probably high performers if they're in fixed now.

**Ryan Singer:** Yeah, actually it doesn't matter.

**Marcel:** They are, but it just doesn't matter because it's just like.

**Ryan Singer:** It doesn't matter.

**Marcel:** Like free fall.

**Marcel:** It's still like free fall and likely to fall or, or decaying are like three negative things, right?

**Ryan Singer:** Yep.

**Marcel:** And it's assuming most of these are high performer or either way, the logic, as long as you put it in these buckets right.

**Marcel:** Then there's only three buckets of actions here.

**Marcel:** Right.

**Marcel:** Like now green alerts, that zone.

**Marcel:** And that's kind of it.

**Marcel:** And then later on you can go into the explore all and advanced mode and whatever the fuck, you know, like.

**Ryan Singer:** Yeah.

**Marcel:** Marshall mode to just like go find new patterns.

**Marcel:** Yeah, that is, that is always my, my, my concern or like my, my like.

**Marcel:** No, dude, but it's like if we make it like too simplistic that like listen, we have to listen to this this morning.

**Marcel:** William is our best.

**Marcel:** Yeah, okay.

**Marcel:** William is our best on this call on Spend Ask.

**Marcel:** We did not have access to Google Search console and he didn't even think of asking for it and he didn't even look at the data before doing an entire content strategy that we're presenting today like to an entire new client.

**Marcel:** Like he did it and he's our best.

**Marcel:** Like he's awesome, you know, but it didn't even cross his mind.

**Marcel:** It's like we have spokes that we have are extractions of existing marketing teams and product companies.

**Marcel:** So it's not consulting people.

**Marcel:** That's how internal marketing is performing.

**Marcel:** Is this like the bar here?

**Marcel:** It's not like engineering where there's like really good engineers out there.

**Marcel:** It's just like the bar here is just like no one has mental models form because there's so many marketing channels and marketers.

**Marcel:** I'm always trying like to decide are we building like Photoshop where you have a learning curve but once you crack it you're like awesome.

**Marcel:** Or are we building like no os, Mac OS Preview, you know, And I.

**Ryan Singer:** Think, dude, I'm 100%, I'm 100% sure you're building macOS preview.

**Ryan Singer:** I'm 100% sure.

**Ryan Singer:** Because the only reason you can Do.

**Ryan Singer:** The thing is nobody can do it.

**Ryan Singer:** Making preview in this market, in this vertical, requires you to be a genius because you have to be so good at figuring out how to actually automate the presentation.

**Ryan Singer:** Like making it.

**Ryan Singer:** It's too many signals.

**Ryan Singer:** So like, that's what agents are for.

**Marcel:** Like, agents are for exactly extracting that.

**Marcel:** And then your logic, your human judgment is where the place is leveraged, which is like some central place where the logic lives.

**Marcel:** Right.

**Marcel:** Like AKA like your plot nd or your MD or whatever the fuck.

**Marcel:** Right?

**Marcel:** Like that's where the human judgment can go.

**Marcel:** Like looking at the table.

**Ryan Singer:** Exactly.

**Ryan Singer:** And the difference here is that this isn't.

**Ryan Singer:** These aren't generic statuses like the, the.

**Ryan Singer:** I think what we got to today was that these are highly, highly specific, meaningful statuses that map to specific actions that are domain specific.

**Ryan Singer:** So like, Daniel, like, if.

**Ryan Singer:** If these things were just saying urgent, like, I would be like, like, this is.

**Ryan Singer:** This is a toy.

**Ryan Singer:** This isn't real.

**Ryan Singer:** Like, we should be showing the numbers instead.

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** But like, because it's actually saying like this specific.

**Ryan Singer:** This is a signal detection.

**Ryan Singer:** This is a specific signal detection.

**Marcel:** Right.

**Ryan Singer:** I would even think of this as.

**Marcel:** Like, yeah, this happened like a malware.

**Marcel:** It's like in your network.

**Marcel:** It's just like, go fix it.

**Marcel:** Like, drop everything you're doing.

**Marcel:** Go.

**Marcel:** Like address.

**Marcel:** Yeah.

**Marcel:** This is almost like a security tool.

**Marcel:** Yeah, it's a sim.

**Ryan Singer:** It's really like a security tool.

**Ryan Singer:** It really is.

**Ryan Singer:** And it's funny, actually, I have a client who's a sophisticated security tool maker that's like, with a very, very big footprint.

**Ryan Singer:** And it's like so many similarities now that I think about it.

**Ryan Singer:** You know, it's like they have this deep, deep, deep expertise in tradecraft of like how hackers try to trick you and then they have to translate those into like signals that get surfaced and they literally like use all the same language and stuff like that.

**Ryan Singer:** And it's.

**Ryan Singer:** Yeah, that's actually really interesting.

**Marcel:** Like, my first job was a security intelligence.com building LA for IBM Security.

**Marcel:** And the whole theme of the company, security intelligence.

**Marcel:** Because you had like app security versus like network security versus endpoint security versus like, you know, there's like all these like vectors that you had to protect.

**Marcel:** Anyways, there's a lot of parallels here.

**Ryan Singer:** Yeah.

**Ryan Singer:** So I think, I think this is not even a.

**Ryan Singer:** We were originally talking about like smart status or something.

**Ryan Singer:** I wouldn't even call this a status.

**Ryan Singer:** This is actually like a.

**Ryan Singer:** It's like a signal detection.

**Marcel:** Bringing to like what the guys are on the ground building today.

**Marcel:** I think this like what we're doing today, even if we build what we have on the left, like if we build and we don't spend too much time on like making it look awesome or something like this, a redesign.

**Marcel:** Like if the foundation is there for the right metrics, which all these things are on top of the right metrics.

**Marcel:** Doing a facelift in March to create an optimization area that has all the things we talked about feels very doable.

**Marcel:** So it doesn't feel like this, like I need to scrap everything that we have lined up for the next three weeks to go do this.

**Marcel:** You know, I think it's.

**Marcel:** You already have the filters in some ways and you were already going to build the logic.

**Marcel:** Let's put a create.

**Marcel:** Let's put the create menu and like I'll go on the right side because right side is the optimization one.

**Marcel:** Yeah.

**Marcel:** On the next, for now, this cycle.

**Marcel:** And then the optimization area.

**Marcel:** Then we do this.

**Marcel:** And then for the optimization area, I think there is a quick judo move here, which is like where it says pages by pillar, it's like pages by.

**Marcel:** And then it will be like whatever those fields are or something.

**Ryan Singer:** Pages by signal.

**Marcel:** Yeah, pages by signal or something.

**Marcel:** And then it's just like.

**Marcel:** And then each of these things that collapse are the fix now and the.

**Marcel:** Do you think we should still build the clustering system?

**Marcel:** Because that is a hard system to build.

**Ryan Singer:** That's what I wanted to ask about is how does this coexist with clustering?

**Marcel:** So keep in mind, there is almost never in successful sites where it's one page type and that page type is just for instance, even Spindex 700 blogs or sorry, 700 pages.

**Marcel:** 400 of those are blog, 60 of those are glossary and the rest is whatever the fuck.

**Marcel:** And but even within those 400 blogs, it's just like it's not just blogs, it's just like there's so much nuances of like content type intent that there's like topics, right.

**Marcel:** And then the.

**Marcel:** Some of those will be really important to them.

**Marcel:** Right.

**Marcel:** Like for instance, like compliance is really important because Spendesk is in the uk, it's their main market.

**Marcel:** And so like all things VPR compliance and things like that are there like edge over, ram it and whatever.

**Marcel:** Right.

**Marcel:** And so that's like a cluster or something that's just like has the lens of like being able to communicate something because it's really hard.

**Marcel:** Like imagine you have these alerts and everything's Perfect.

**Marcel:** Right.

**Marcel:** But then imagine you have 500 pages and.

**Marcel:** And there's like 72 in red alerts.

**Ryan Singer:** Okay.

**Marcel:** And.

**Marcel:** Okay, 230 in green alerts.

**Marcel:** Like, what the fuck?

**Marcel:** I don't know what to do with this.

**Marcel:** But, you know, so this.

**Ryan Singer:** What I'm hearing is the.

**Ryan Singer:** So the clustering is of course, like the clustering.

**Ryan Singer:** The function of clustering is to deal with too many results that are all kind of comparable to each other.

**Ryan Singer:** They're all similar to each other.

**Marcel:** Right?

**Marcel:** Exactly.

**Ryan Singer:** So I think structurally what that means is that you need to nest the clustering inside of the signal category.

**Marcel:** Exactly.

**Marcel:** So.

**Marcel:** So within the mode of that category, like random, is a mode, you know, so here mode, you might need to stack some clusters, like for a check that it would be like content type pricing versus review versus brand overview.

**Marcel:** And then within that would be a like category of page.

**Marcel:** Like, you know, like.

**Ryan Singer:** Exactly.

**Marcel:** And finance versus like, CRM versus marketing tools.

**Marcel:** And then that will give you the insight that you were looking for.

**Ryan Singer:** So, but.

**Ryan Singer:** But the cluster.

**Ryan Singer:** But I think we should be.

**Ryan Singer:** What that would mean.

**Ryan Singer:** I just want to spell it out and make sure that it's clear.

**Ryan Singer:** What that would mean is we would be repeating clusters.

**Ryan Singer:** Possibly.

**Marcel:** I was going to ask that.

**Marcel:** Yeah, yeah.

**Ryan Singer:** And I think it's important to call that out as a feature, not a bug.

**Marcel:** Right.

**Ryan Singer:** So like my.

**Ryan Singer:** If I'm.

**Ryan Singer:** Because.

**Ryan Singer:** Because if it's red alerts, I've got to act on it and it doesn't matter, like, where it lives.

**Ryan Singer:** I need it surfaced separately, you know, and then if.

**Ryan Singer:** If I'm in the mode of looking for unrealized opportunities, you know, then I can use my clustering as a way for me as a human to deal with the fact that there's 200 of them.

**Ryan Singer:** So I can understand what the heck I'm looking at.

**Marcel:** Right.

**Marcel:** Yeah.

**Marcel:** I almost don't know if we need clustering at the fix now layer.

**Ryan Singer:** Actually, that's true.

**Ryan Singer:** We shouldn't.

**Ryan Singer:** We shouldn't.

**Ryan Singer:** It should be flat, Right.

**Ryan Singer:** Unless you need it for context to understand what the meaning of the pages.

**Marcel:** Yeah, yeah.

**Marcel:** It's just like the second you cross over, like, mature sites, it's just like you're gonna need puzzles for everything because it's unmanaged to like.

**Marcel:** Yeah, yeah, it's 50, it's 500, you know, and it's.

**Marcel:** It's just like.

**Marcel:** Yep.

**Marcel:** It's the lens through which you, like, validate also that your strategy is working.

**Marcel:** Right.

**Marcel:** Like, hey, pricing is driving most of the traffic on our site.

**Marcel:** Right.

**Marcel:** But like, how do you know?

**Marcel:** Why are some pricing pages rising and some are not?

**Marcel:** Why are some.

**Marcel:** Right.

**Marcel:** Like, it's so hard to answer those questions, you know?

**Ryan Singer:** Yeah.

**Marcel:** Or even within the like red alert, potentially.

**Marcel:** Yeah.

**Marcel:** Yeah.

**Ryan Singer:** Good.

**Ryan Singer:** Okay, so what I'm going to do then is I'm going to, I'm going to say, well, actually all of this is changing, but the other thing I just want to call out is that we're actually like, I think, I think this is a bold and important move to consciously not do filters.

**Ryan Singer:** You know, even though there's a lot of smart ideas here.

**Ryan Singer:** Because the, of the, the, the bigger macro structural win of taking this approach.

**Marcel:** Yeah, yeah.

**Marcel:** I mean it's literally like.

**Marcel:** Yeah.

**Marcel:** So the three work.

**Marcel:** Three workflows and it's like it's a classifier and those are three fields in the table.

**Marcel:** Am I oversimplifying that?

**Marcel:** I think so.

**Marcel:** Because when you're dealing with 12,000 things.

**Marcel:** Yeah, but the main thing that I'm thinking is that this.

**Marcel:** Because like literally like yesterday I created all the linear tickets and the design, the mockups.

**Marcel:** What I showed you is essentially all static views every on a.

**Marcel:** The app.

**Marcel:** And the guys are starting to do the, the back end.

**Marcel:** So by the way, the scoring will all be important because like the scoring, Ryan, it's like.

**Marcel:** Yeah.

**Marcel:** So the two things that I think I'm trying to figure out what is not part of the scope, what can I cook this call?

**Marcel:** Because it's 14 areas and it's just four engineers including me there.

**Marcel:** So a lot of the stuff, we're not going to make it.

**Marcel:** So clustering is a big part that's not easy to do.

**Marcel:** The smart views are not easy to do.

**Marcel:** So again with the smart views constantly kit, I move the backlog out of the learning brutal area for the creation of new pages.

**Marcel:** Removing smart views cuts the scope.

**Marcel:** Collecting the data is too important.

**Marcel:** Showing the data doesn't matter that much.

**Marcel:** So we don't have to get that user interface super.

**Ryan Singer:** Right.

**Marcel:** Sorting doesn't matter anymore.

**Marcel:** Pagination doesn't matter anymore.

**Marcel:** So the configuration, 12,000 records with like time series stuff, it's working hard.

**Marcel:** So there's all these things that I can cut from the scope and then allows us to do that on the next cycle right away.

**Marcel:** Yeah, yeah.

**Marcel:** Just know that like somewhere there, the new page opportunity, like where we're missing in week two of these engagements is that like we have no view into their surface area.

**Ryan Singer:** Yeah.

**Marcel:** And.

**Marcel:** And so if we're giving them like a map of opportunity with, like, completely ignoring what their current service area is, it really puts those accounts at risk.

**Marcel:** Yeah, yeah.

**Marcel:** So understand your entire site is really important.

**Marcel:** Yeah.

**Marcel:** So it's like, it doesn't need to be this, but we need to have, I think, something to show their inventory pages in some way or at least the overall help, you know, like even saying, like, you know.

**Marcel:** But.

**Marcel:** Yeah, okay, well.

**Marcel:** But I think we can wrestle with it a little bit and cut, cut, cut.

**Marcel:** And then, like, see if, like, there's a way to kind of simplify the learn and improve.

**Marcel:** Because, like, what were you thinking for learn improve for this cycle?

**Marcel:** That user interface.

**Marcel:** Yeah.

**Marcel:** Actually, that's what I'm going to work today.

**Marcel:** I'm like, I'm gonna go as fast as I can on the first UI that we're showing.

**Marcel:** So, like, that changes it quite a bit.

**Marcel:** So.

**Marcel:** Okay.

**Marcel:** And so if we cut the filtering, you still have to do this.

**Marcel:** You still have to do all the scores, right?

**Marcel:** For everything.

**Marcel:** Yeah.

**Marcel:** And then all the three things here are essentially, like, what to do about the score.

**Marcel:** Right.

**Marcel:** So it's like two layers of instruction.

**Marcel:** Yeah.

**Marcel:** Right.

**Marcel:** It's like versus hot.

**Marcel:** Right.

**Marcel:** Like, the hot is like you're taking the scores and the changes in the scores and then like, drawing that.

**Marcel:** Yeah.

**Marcel:** And then the warm is the, like, the scores, which are kind of like indicators.

**Ryan Singer:** Yeah.

**Marcel:** That then have, like, a ton of.

**Marcel:** It's more like it didn't change the underlying data model.

**Marcel:** It does change the amount of effort we would put on the user interface for, like, I think we can have a flat table now with just clusters, not worry too much about sorting, imagination, that kind of stuff.

**Marcel:** And knowing that we got to do a second pass to build, like, the intelligence layer that we walked out there.

**Marcel:** And we might have to have a place to do what you're saying, just, like, see the whole inventory.

**Marcel:** So that is still basically the first screen.

**Marcel:** Is there a way to just have one of the three as a signal field so that the default of the view is like, filter bind.

**Marcel:** I think we can add it.

**Marcel:** If the default view is clustered and we show the metrics on the cluster level, that is something we can do.

**Marcel:** If I just do that, then that will help adding.

**Marcel:** Figuring out the workflow to go through all your pages, sorted by traffic, and then rank them and group them in the user interface later?

**Marcel:** It's.

**Marcel:** It's not hard because Ryan, like, one of our competitors, already has this, what they call page 360, and it's gaining some traction.

**Marcel:** And all it is is like a smart View with like, crazy amounts of filtering that then when you select it, applies all the filters and allows you to edit the actual details of those filters.

**Marcel:** And we think it's like the wrong approach, but it achieves a similar result, essentially.

**Marcel:** Yeah, it's like a filter template, you know, and almost, you know.

**Marcel:** Yeah, we can figure out a shorter or a future.

**Marcel:** That's easy.

**Marcel:** Like, I just don't want to spend like a whole week making that table perfect, you know?

**Marcel:** Yeah, it would be easy to do that.

**Marcel:** Like, tables are hard to do.

**Marcel:** And if you have like collapse and all that stuff, that volume, you're going to be spending days on, like, fixing performance issues and scrolling browser behavior and sorting patterns.

**Marcel:** Like, if I don't do any of that and I just focus on collecting the data and getting the detail page right, then we layer right after you finish this with the opinionated areas, you know, and also use the snapshots later to cover up anything if needed.

**Marcel:** Snapshots?

**Marcel:** Yeah.

**Marcel:** Meaning like if you have a table that literally just had three fields or three columns, right.

**Marcel:** And they're all cluster and it's like it had no data in it whatsoever, and if you click on it, you can see the full view.

**Marcel:** But, like, there's no aggregate reporting on anything.

**Marcel:** Like, any needs for aggregate reporting, which you do eventually need, like, to say, hey, traffic is growing or not.

**Marcel:** Like, you know, that can be done in snapshots is what I'm saying.

**Marcel:** Oh, broken snapshots.

**Marcel:** Yeah, that's what I'm saying.

**Marcel:** Yeah.

**Marcel:** You know what I mean?

**Marcel:** So it's like you don't.

**Marcel:** The table itself, I don't think to carry like this crazy amount of data.

**Marcel:** Like, it doesn't need to look like.

**Marcel:** Check that prompt table.

**Marcel:** Yeah, yeah, yeah, yeah, yeah.

**Marcel:** Sorry, Rand.

**Ryan Singer:** No, it's good because it means that we, We.

**Ryan Singer:** We unblocked something.

**Ryan Singer:** When you guys suddenly talk a lot, you know, I always take that as a positive sign, actually, you know, there.

**Marcel:** Yeah.

**Marcel:** Yeah.

**Marcel:** Okay, good.

**Marcel:** So much work, so much opportunity, so little time.

**Marcel:** We need more agents working 247 around the.

**Marcel:** We sleep.

**Marcel:** We need more R time.

**Ryan Singer:** I know.

**Marcel:** More R time.

**Marcel:** How do we grab the next three, four tickets?

**Marcel:** You know, it's like when you're in the, you know, at the grocery, grab your ticket, you know.

**Ryan Singer:** Like at the butcher.

**Marcel:** Yeah, yeah, yeah.

**Marcel:** Oh, cool.

**Marcel:** Okay.

**Marcel:** Should we look at upcoming.

**Marcel:** I think we have one more schedule.

**Marcel:** Right, Right.

**Ryan Singer:** No, this is the last one.

**Marcel:** Yeah.

**Marcel:** No.

**Marcel:** How's your life, Ryan?

**Marcel:** Yeah.

**Marcel:** How hardly.

**Marcel:** You said you were gonna, like, already kick off the.

**Ryan Singer:** Yeah.

**Ryan Singer:** It's interesting, you know, I, I'm just about to hopefully get like kind of a scope of work commitment and some signatures from like an integration partner on this big gnarly thing we're starting and we're doing like an AI integration at like a recruiting, like an enterprise recruiting software service thing.

**Ryan Singer:** And it's, I'm not out of the woods, you know what I mean?

**Ryan Singer:** But like, it's like we, we.

**Ryan Singer:** I can draw it on a napkin now, you know?

**Marcel:** Yeah.

**Ryan Singer:** So it's like, it's, it's, it's, it's, it's feeling more tractable, but I still kind of can't tell, especially in the first few weeks, like how crazy it's going to be in terms of needing to do a lot of code design with the integration partner, in which case I have to carve out time.

**Ryan Singer:** My us overlap hours are going to get eaten up really fast.

**Ryan Singer:** So I kind of cleared the deck to see what happens as we get rolling in the first one or two weeks ahead.

**Ryan Singer:** I actually have said no to all my upcoming training, like shaping sessions.

**Ryan Singer:** Like, so any of these like three hour sessions that are not you guys, I like cleared out.

**Ryan Singer:** And the thing I have to determine is if I can, if I need to keep space for this one project, you know, to, to, to spill over the edges or if I can, if I can start to picture something like you know, every other week a session like this or something like that, you know, that's kind of of like.

**Marcel:** Yeah.

**Ryan Singer:** I need to.

**Ryan Singer:** The.

**Ryan Singer:** My partner on this integration has been holding back on getting into full technical detail before they have a commitment signed.

**Ryan Singer:** So there's a little bit of some chicken neck going on there that we're.

**Marcel:** Working through, you know.

**Marcel:** Got it, got it.

**Ryan Singer:** Okay, so that's the current status here.

**Marcel:** Sounds good.

**Marcel:** Yeah.

**Ryan Singer:** Do.

**Marcel:** Would it be helpful to try to even like super tentative, like pencil in or you prefer to just like not anything and follow up offline?

**Ryan Singer:** Let's, let's, let's, let's take a moment and just talk through like what, what are the, what kind of help do you feel that you need in the coming weeks?

**Ryan Singer:** And like what.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Like what, what sort of deadlines are coming to you?

**Ryan Singer:** Just what's going on in terms of the urgency that you find yourself in specifically or like now, you know, like, what are the things that you need me for?

**Marcel:** Yeah, like, like from, from, from my perspective, like there's this like I for instance, like on.

**Marcel:** Check that.

**Marcel:** Right.

**Marcel:** Been juggling with this thing And I probably spent already like 50 hours of my time trying to like, shape something and not get into these aha moments that we get to in three hours.

**Marcel:** And.

**Marcel:** And it's often in the last like, like hour that they happen.

**Marcel:** Right.

**Marcel:** And so it's like I'm adding a zero to how much time it's.

**Marcel:** It's taking if I ever get there.

**Marcel:** Right.

**Marcel:** And that's just like me personally, you know, and.

**Marcel:** And so like, the thing is, like, if we were talking about one of our engineers, like, fine, whatever.

**Marcel:** Right.

**Marcel:** Like, but because it's like mine and Daniel's time, that that's zero of like three hours instead of 30 is like really meaningful.

**Marcel:** Like, like consequential to like the company because it can mean like months multiply later.

**Marcel:** Right?

**Ryan Singer:** Yeah.

**Marcel:** So the leverage that you bring us is like extremely valuable, like I would say, like, you know, at the highest, most important level.

**Marcel:** Because it's like there's no question of the opportunity and how big the opportunity is.

**Marcel:** There's no question on life, like the jobs to be done and how to do those jobs.

**Marcel:** It's all about, like, translating that into how the we put this in market.

**Ryan Singer:** It's all those.

**Marcel:** It's all how to crack those nuts, you know?

**Ryan Singer:** Yeah.

**Marcel:** And it's what you're the world class best in the world at.

**Marcel:** And you know, and, and so like, that's the help.

**Marcel:** It's like truly, like, just show up, you know, kind of help.

**Marcel:** That is.

**Marcel:** That is one.

**Marcel:** But.

**Marcel:** But it's also like, there's so many things though, like.

**Marcel:** Sorry, that is one.

**Marcel:** But it doesn't have to be with us in the room as well.

**Marcel:** Right.

**Marcel:** As in, like, if you don't have time with like us overlap.

**Marcel:** I'm pretty sure that if you like, if you get like Marcel's docman that he's struggling with on check that.

**Marcel:** Because this is just the area that we overlap and it's so critical that Marcel and I have to be in a room with you because this part of the system is so important.

**Marcel:** Marcel is shaking one thing, I'm shaking some other thing.

**Marcel:** On the framework, there's all these things happening at the same time, but I can check that for the case that he's giving.

**Marcel:** If he just gives you all the things that he's been working on, I'm.

**Ryan Singer:** Pretty sure I'm pretty doubtful of that because what I notice is that it's like Marcel just said, usually the first two hours is me like probing and probing and probing.

**Marcel:** Yeah, I agree with that.

**Ryan Singer:** Not only Absorbing.

**Ryan Singer:** It's tacit knowledge that you guys have that I'm pulling out so it wouldn't be in the document.

**Marcel:** Yeah.

**Marcel:** But I believe you also have like an amazing like that is on the product level.

**Marcel:** You also like seemingly helpful on the UX and the practical side of things when they're like yeah.

**Marcel:** As well.

**Marcel:** But I almost think like given how little time.

**Marcel:** Yeah.

**Marcel:** You have.

**Marcel:** Yeah.

**Marcel:** Like this is like if we had to fully multiplier.

**Marcel:** This is like a 10x amplifier and we're aligning between us.

**Marcel:** Yeah.

**Marcel:** So it's accomplishing multiple things at once and it's like reducing rework later which like.

**Marcel:** Yeah.

**Marcel:** And, and waste in 15.

**Marcel:** Yeah, yeah, for sure.

**Marcel:** That's the movement.

**Marcel:** So it's like if I only have three hours of your time once a month, I'll take it.

**Marcel:** If I had two of those sessions.

**Marcel:** Sessions, like you know, three hours, you know, and maybe just like 8:30 minute a week, you know, just like respond to a couple of things or you know, just like a couple questions, a couple thoughts like, you know, that would be like worth, you know, like anything.

**Marcel:** And then also like we would like.

**Marcel:** Personally I would love to make sure you get equity as well so that you're, you know, motivated long term, you know.

**Ryan Singer:** Yeah.

**Marcel:** Because our valuation is super low, man.

**Marcel:** So it's like there's a lot of, you know, I like.

**Ryan Singer:** Yeah, I like that idea a lot.

**Ryan Singer:** Next couple weeks are tough for me. Let me set a specific timeline for this. Basically, I'll have some time opening up again after March 18th. Before then, unless something changes and I can delegate a chunk of my client project work, it's going to be tight. But it could go either way. So here's what I'll do: I'm going to set a deadline for myself for Wednesday the 25th to get back to you with a clear answer on whether I have capacity in the coming weeks. At a minimum, we can stake out the next deep-dive session for mid-March after the 18th.

**Marcel:** Next couple weeks we're busy too with all of this work.
