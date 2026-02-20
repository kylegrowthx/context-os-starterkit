# Shaping with Ryan Singer

<metadata>
date: 2026-02-17
time: 17:00 UTC
duration: 181 minutes
organizer: marcel@growthxlabs.com
participants: Marcel, Ryan Singer, Daniel
fireflies_id: 01KH96HM54F1VYHKVAEH3YHXXE
meeting_link: n/a
transcript_url: https://app.fireflies.ai/view/01KH96HM54F1VYHKVAEH3YHXXE
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

**Ryan Singer:** Hey, marcel.

**Board Room:** All right.

**Board Room:** There you go.

**Board Room:** Hey, Ryan.

**Board Room:** Good to see you, man.

**Board Room:** All righty.

**Ryan Singer:** Good morning.

**Board Room:** There you go.

**Board Room:** Firefly, right?

**Board Room:** Yes.

**Board Room:** Okay.

**Board Room:** Make sure it's right.

**Board Room:** Yes.

**Board Room:** Fireflies.

**Board Room:** All the note takers and all the recorders, all the things.

**Ryan Singer:** But we're outnumbered.

**Board Room:** Ryan, I.

**Board Room:** You would be proud of me.

**Board Room:** I kind of try to, you know, draw my inner Ryan during all hands last week and presented the whole thing in tl.

**Board Room:** Draw.

**Ryan Singer:** Hey.

**Board Room:** I'm learning from you, my friend.

**Ryan Singer:** All right.

**Board Room:** I should show you.

**Board Room:** Super, super cool.

**Board Room:** It was actually like.

**Ryan Singer:** Yeah, let's see.

**Board Room:** I thought it was pretty decent.

**Board Room:** Okay.

**Board Room:** So I started here of like, here's the shift, you know, that we're seeing one buyer to now three buyers.

**Board Room:** The agents that influence the buyers.

**Board Room:** The reward function is like, what does every company want to grow and do more with less.

**Board Room:** One is about, like, growth, another one is leverage, you know.

**Board Room:** So where do you start?

**Board Room:** We believe the website is your biggest driver.

**Board Room:** It influences everything.

**Board Room:** It's what you can control.

**Board Room:** Most transactions happen here.

**Board Room:** Compounds have done right.

**Board Room:** It's measurable, and it drives both growth and leverage.

**Board Room:** But it's getting harder and harder to do because more pages to feed, more answers, got to stay fresh and high quality, always hard to manage.

**Board Room:** So the website went from important to existential and the job got 100 times harder.

**Ryan Singer:** Totally.

**Board Room:** Which then now what is the job to be done is drive compounding growth through your website, which means manage page, create pages optimized continuously, you know, and so you keep them organized, current, healthy and performing.

**Board Room:** Expend your surface area, more answers for buyers, more content for AI to site, more signals for training bots to learn.

**Board Room:** Every page continuously.

**Board Room:** Fresh quality, relevance, conversion.

**Board Room:** Not once every single week.

**Board Room:** That is impossible to do manually.

**Board Room:** And.

**Board Room:** And so.

**Board Room:** And how do you even know if it's working?

**Board Room:** And so you got to think about, like, leading to lagging.

**Board Room:** And ultimately, like the promised land is AI handles production, optimization and learning at scale.

**Board Room:** Humans provide strategy, quality, judgment where it matters.

**Board Room:** The system gets smarter.

**Board Room:** Every output, every page, every week, growth compounds across all three audiences.

**Board Room:** Buyers, AI and training bots.

**Board Room:** And then this is like, need to go into this.

**Board Room:** But this is kind of like.

**Ryan Singer:** Yeah, then you come into how.

**Ryan Singer:** So like you sort of sold them on, like, why, and now this is sort of the how of how you actually do it.

**Board Room:** Yeah.

**Board Room:** Then it's like connect.

**Board Room:** Try to.

**Board Room:** I try to connect it with, to like what we built because we have like, infrastructure, data, platform, services and distribution.

**Board Room:** And there's like all these layers.

**Board Room:** This is like, anyways, I.

**Board Room:** The house would be much easier if we had the product that I simply into it.

**Ryan Singer:** Yeah.

**Ryan Singer:** So like.

**Board Room:** But anyways, it's been, it's been fun.

**Board Room:** I even got a little pencil trying to of learn from me.

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

**Board Room:** Raw material for free.

**Board Room:** We actually just dropped one of the ones that we were helping for a while that was like kind of like a partner and we were doing essentially like a pro bono if you will, because it's like a, it was cool work but we should, we should think about that because.

**Board Room:** But anyways.

**Ryan Singer:** Yeah, but it's interesting to like feel the problem.

**Ryan Singer:** You know, it's like so clear that like the problem is literally getting all the material out there, you know, and, and being like doing it strategic.

**Ryan Singer:** Like the combination of taking some time to do it strategically, which you guys like help with on the front loading.

**Ryan Singer:** But then just all this work, you know, of like writing the articles and everything.

**Ryan Singer:** Like even when you have a lot of source material, you kind of know what you want to say, you know, it's.

**Ryan Singer:** I totally get it.

**Board Room:** Yeah.

**Board Room:** Yeah.

**Board Room:** I've been doing the same thing.

**Board Room:** I just built a company.

**Board Room:** I had like my context project and that had like all my files, all my knowledge and everything.

**Board Room:** And I was trying to massage it into like a handbook.

**Board Room:** But because I have so much of the good context and things, like I was able to write like essentially like 70 doc pages, like the equivalent of get labs, like handbook and you know, a single day.

**Board Room:** Pretty much.

**Board Room:** Yeah.

**Board Room:** It's the same setup that you have with like minclify and markdown files and all that.

**Ryan Singer:** Yeah, Yeah.

**Board Room:** I gotta clone your skills still.

**Board Room:** It's on my to do list.

**Ryan Singer:** Ah, yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** So I.

**Ryan Singer:** All right, so.

**Ryan Singer:** So what's, what's on the docket for today?

**Board Room:** Yeah.

**Board Room:** Did you have time to watch the.

**Board Room:** The first video that I sent you?

**Board Room:** The one that's like shorter one?

**Board Room:** I said like yesterday midnight, so I can.

**Ryan Singer:** You know, I actually didn't get an email from you.

**Board Room:** Huh.

**Ryan Singer:** I thought that.

**Board Room:** And maybe I didn't send.

**Ryan Singer:** I thought that I didn't get anything from that.

**Board Room:** Look at this.

**Board Room:** Let me share my screen.

**Board Room:** Which.

**Ryan Singer:** Which AI secretary do we have to fire?

**Board Room:** This is the.

**Ryan Singer:** This is literally the best thing I.

**Board Room:** Have on my screen.

**Board Room:** Oh, gosh.

**Ryan Singer:** So there are still some.

**Board Room:** The dog ate my homework, Ryan.

**Ryan Singer:** Yeah, Superhuman.

**Ryan Singer:** By the way, Superhuman has no idea who I am.

**Ryan Singer:** Rapper, songwriter from ports Port St. Lucie.

**Board Room:** This.

**Ryan Singer:** Look at his knives.

**Board Room:** Every time I see this guy, I'm like, oh, is it a rapper?

**Board Room:** Oh my God, that's amazing.

**Board Room:** Okay, so maybe I walk you through the.

**Board Room:** Through the progress that we've made.

**Board Room:** Just to give you context.

**Board Room:** I also.

**Ryan Singer:** Yeah, let's do that.

**Board Room:** Automating your workflow for like showing how the framework works and using your workflow as an example.

**Board Room:** Basically a scaffold.

**Board Room:** The thing is, the way to think about is like we have this AI framework that's all file system based, so prompts tracing the workflow.

**Board Room:** The steps of the workflow are all in code and in the file system.

**Board Room:** And we have a bunch of Claude skills and plugins that sits on top of this.

**Board Room:** So think of it as like a rail scaffold, but like on steroids.

**Board Room:** And you can essentially just create almost anything by just talking to it.

**Board Room:** So I did that in the video.

**Board Room:** So that's the second video.

**Ryan Singer:** Well, yeah, so if you can just send me the email once the blocking issue is fixed, then I'll spend time checking that out, you know, off the call, because probably it's not relevant for you guys for the time we have now, but I'll look forward to seeing that.

**Board Room:** Yeah, that is actually like another project.

**Board Room:** So we have these three things happening.

**Board Room:** We actually could talk about that at the end, but we have.

**Board Room:** There's something we're doing on Check that.

**Board Room:** That's like top of funnel and I saw you try to use Team Builder and like you check out the website and maybe we can go through that a little bit today.

**Board Room:** But at a high level we have checked that is a top of funnel, monitoring the market, monitoring how the LLMs perform.

**Board Room:** And then on the other side we have the content OS that we've been working on.

**Board Room:** And under those two things we have the framework and we've been doing a lot of custom work for content creation.

**Board Room:** That's much Harder than normal pages that you're not going to be able to do in the contentos project.

**Board Room:** So we have a team of five people, that's our four deploy team.

**Board Room:** They decide, okay, this goes into this pipeline kind of work or this goes into a custom agent kind of work.

**Board Room:** And we have this part of the business that we want to grow pretty aggressively, an agency on top of it as soon as we make the thing open source.

**Ryan Singer:** And just to give you an example.

**Board Room:** Of the kind of stuff we do, like Lovable is a good one.

**Board Room:** So Lovable, they came to us with the idea.

**Board Room:** We actually used the framework to investigate all the activity that happened on another player that was very similar to Lovable, one of the clients that we had.

**Board Room:** And we realized all these people are struggling with prompt.

**Board Room:** So instead of prompting, can we create a giant list of catalog of templates that you can use and you start from there.

**Board Room:** Problem is that Lovable was not really good enough.

**Board Room:** One shot in like high quality stuff.

**Board Room:** So you have to be a back and forth conversation.

**Board Room:** So we, until you create a website like a template.

**Board Room:** And for the template we also need a page around the template.

**Board Room:** So we ended up creating this.

**Board Room:** Isn't there a homepage?

**Board Room:** Yeah, right here.

**Board Room:** So discover templates, for example.

**Ryan Singer:** Sorry, the issue was that lovable as a GrowthX client didn't know what to prompt the OS tool or is this about Lovable's clients?

**Board Room:** Yes.

**Board Room:** So think of it as like you're, you're coming in and you're trying to get to something that's like good.

**Board Room:** Right.

**Board Room:** And they don't know how to prompt and all the user generated content was pretty garbage out there.

**Board Room:** And yeah, they, this is like the.

**Ryan Singer:** Content, this is like the content team on Lovable or this is the lovable user using the Lovable app.

**Board Room:** This is like a lovable user.

**Ryan Singer:** Got it.

**Ryan Singer:** Yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Board Room:** Going to Lovable or finding out about them?

**Ryan Singer:** Ah, totally.

**Ryan Singer:** Okay.

**Ryan Singer:** Yeah, no, this problem I know about.

**Ryan Singer:** Yeah, people don't know how to prompt.

**Ryan Singer:** Exactly.

**Ryan Singer:** And then they just kind of.

**Ryan Singer:** It's garbage in, garbage out.

**Ryan Singer:** Right?

**Board Room:** Yeah.

**Board Room:** And.

**Board Room:** But then also from an SEO perspective and growth perspective, they like, they're now competing with Wix who bought one of their competitors, Base44 and they have an F ton of traffic like millions and millions of people because they have all these templates and templates is like a.

**Ryan Singer:** Huge driver of traffic at wix, WIX and Squarespace.

**Ryan Singer:** They already understood this dynamic very well, which you know, because they knew they, they had all these website builders and they knew that if you didn't give people like a starting point that people didn't know what to do.

**Board Room:** Yeah, exactly.

**Board Room:** And it's where a lot of the traffic is.

**Board Room:** So from a content perspective we're like let's go create a template library that's more like a starter kit library of like.

**Board Room:** But how do you build that without having a network of highly qualified designers who built it on like a reusable foundation.

**Board Room:** It's like free fall shit garbage like prompts.

**Board Room:** And so, so we gave them essentially like the strategy how to like think about it.

**Board Room:** We created this experience as well as the actual individual template pages.

**Board Room:** And then what Daniel is going to show you is how we programatize going from ideation all the way to fully built website programmatically with like going from like seven hours of like design engineers like prompting, tweaking and polishing down to about an hour now.

**Board Room:** Amazing.

**Board Room:** Yeah, I see.

**Ryan Singer:** Because this isn't something that you can just do in a markdown file.

**Ryan Singer:** So that's why it's not possible to do it in content.

**Ryan Singer:** And the in was it content os but you needed to actually build out this custom workflow using output AI in order to orchestrate all that.

**Board Room:** Exactly, yeah.

**Board Room:** So we have this normal editorial clients that need normal pages on the website.

**Board Room:** That's fine.

**Board Room:** That's what we optimize and condent OS for.

**Board Room:** And then we have a bunch of clients that are like I need to create something that's very different or something that's very specific to my needs.

**Board Room:** In this case for lovable was like an agent that would have a back and forth, receive a screenshot, have a back and forth, turns the screenshot into react code and then test it with logo API to see if it's live.

**Board Room:** So like that is one another thing we do for Airbyte similar ideas.

**Board Room:** Airbyte has a bunch of plugins.

**Board Room:** When a plugin gets shows up in their app store we send a pull request if the documentation becomes a page on the website.

**Board Room:** So like we do a plugin like this, they're very, very unique and it's only possible because of the framework.

**Ryan Singer:** Yeah, I get it totally.

**Board Room:** And we're going to grow that team.

**Board Room:** We have four or five people there.

**Board Room:** As we finish the content OS to be like more self serving product, the solutions engineer team can shift to be an engineering team for this kind of custom work on top of the framework.

**Board Room:** Wow.

**Board Room:** So we have these three things in motion.

**Board Room:** The top of the product check that the content OS to normalize pages and intelligence on top of Your website and output AI for any kind of content or like any kind of agent in general.

**Board Room:** But we're trying to start with just focused on.

**Board Room:** Yeah, if you go to the studio and, and show them like the 27 workloads that power.

**Board Room:** This is pretty cool.

**Board Room:** You just search for lovable.

**Board Room:** So check this out, like lovable templates.

**Board Room:** These are all the different workflows decomposing it.

**Ryan Singer:** So is this a front end to output AI or what?

**Board Room:** Yeah, this is alpha that we're not going to launch.

**Board Room:** It's just for our internal inspection and then because we didn't have the time to make this look like legit and fine.

**Board Room:** So we're going to launch just the code part.

**Board Room:** But essentially we have like 27 chunks of code that we wrote for them specific to this problem.

**Board Room:** So like figuring out the typography, the actual words that go on this, these starter kit websites, the structure, the like page structure, the content generator, the image generator, the like, you know, like there's a cleanup part.

**Board Room:** There's like there's all kinds of things that are like essentially decomposing the process of building programmatically.

**Ryan Singer:** This reminds me of what is this, is this different from what like the DAS PI guys are talking about?

**Ryan Singer:** Like when they're like this idea of like you're supposed to kind of like break apart all of this like prompting and stuff into modular pieces.

**Ryan Singer:** This is like a different take on that.

**Ryan Singer:** Similar thought.

**Board Room:** Yeah, it's similar idea.

**Board Room:** DSPI has a lot of the self improving part of the prompts and our take was more like instead of thinking about the prompts, should we think about the workflow itself?

**Board Room:** Because sometimes you need.

**Ryan Singer:** Right.

**Ryan Singer:** Yeah.

**Ryan Singer:** So yeah, this is, this is more like, this is more like a practical software build like standing up systems stuff.

**Ryan Singer:** Right.

**Ryan Singer:** Like huh.

**Ryan Singer:** Yep.

**Board Room:** So you see that I will send you the code for the one that I did for the audio to transcript.

**Board Room:** Cool.

**Board Room:** And so it's essentially mini apps.

**Board Room:** They're like heavy on LLMs.

**Board Room:** So there's instead of like Views and Rails you have a prompts dot prompts file that has all the settings for temperature, the variables, the interpolation, everything and has all the things for like retrialing when LLMs fail has the judgment to go back and LLM is beyond below quality.

**Board Room:** So there's all these things baked in and the UI is essentially you don't have to code but you can if you want to.

**Board Room:** So.

**Ryan Singer:** Yeah.

**Board Room:** Cool.

**Board Room:** So this is a whole thing that we have like.

**Board Room:** So we have this user interface, we have like 300 plus workflows.

**Board Room:** Some are very custom to some clients.

**Board Room:** And then all the AI features that we're talking about on the contentos are also powered by the framework.

**Board Room:** So anyway, the plan is to launch the framework in this next month, and then we're going to grow the engineering team around this custom work for some of the more premium clients.

**Board Room:** And we start hiring solutions engineers for the content OS to do the workspace calibration and then kind of like split the lanes more clearly.

**Board Room:** So those are like essentially three business, three layers of the business that we have that I wanted to show you real quick just to give you the context.

**Ryan Singer:** Awesome.

**Board Room:** Yeah.

**Board Room:** So out of our session last time.

**Ryan Singer:** Hey, what is this new stuff?

**Board Room:** Yeah.

**Board Room:** Oh, man.

**Board Room:** Yeah.

**Board Room:** So out of your session last week, we changed everything and decided to redesign the whole product.

**Board Room:** Okay, real quick.

**Board Room:** Daniel doesn't sleep.

**Board Room:** Yeah.

**Board Room:** So the idea pretty much took what you share your ideas and try to implement here.

**Board Room:** So the setup now is two screens will take you to the place that you, you want, you want to do the work.

**Board Room:** And you can add notes if you're skipping or for whatever reason, even if you're not skipping.

**Board Room:** It's good to have the solutions team that will be setting up the workspace to explain what they did and then if it does not apply.

**Board Room:** So same idea from before.

**Board Room:** And then as you complete, you would like, finish the bar here at the top.

**Board Room:** I went ahead with exactly the same menu that we had thought about.

**Board Room:** So, like, learning, improve, learn and improve will be all of your pages, including the ones that are getting built.

**Board Room:** New page opportunities for new page opportunities and progress snapshots, essentially the report.

**Board Room:** There's like a few things that we have from the legacy project that folks are still going to be using for a while.

**Board Room:** That's the Airflow project.

**Board Room:** This is here just as.

**Board Room:** I don't even know if we're going to keep it.

**Board Room:** But that's the old analytics might be usable for inspecting if you're getting the data there or if like just poking around, but maybe we don't even have to surface.

**Board Room:** And then I also added meetings.

**Board Room:** Meetings is one thing that, as we were discussing last week, a couple of weeks ago, it was a challenge of like, not always you can just let AI do the research.

**Board Room:** There's like a lot of things that comes from the sales meetings for the intake, meetings with the client, the kickoff meeting with the client.

**Board Room:** They're sharing things of like, who are the competitors, who are their Personas.

**Ryan Singer:** And you're asking the right, you're asking the right questions to draw out things that they wouldn't have shared otherwise.

**Ryan Singer:** I totally have this in my workflows too.

**Ryan Singer:** Like, I have these interviews with people, and those interviews are like the gold that I need, like to extract like key requirements from and stuff like that.

**Board Room:** Yeah, exactly.

**Board Room:** So, like this I added last week.

**Board Room:** So the idea is something super simple for now that you would just like paste the transcript and you'd pick a set of recipes and the recipes would be like, for post sales, post kickoff, there's a set of like, things that we look for and it would process and create a bunch of notes out of those transcripts.

**Board Room:** But that's just one of the things that the calibration team would add here manually.

**Board Room:** But before they trigger the company, they trigger the generation for the rest of the setup here.

**Board Room:** So that.

**Board Room:** Sorry, go ahead.

**Board Room:** You're going to.

**Ryan Singer:** Just one little note.

**Ryan Singer:** One thing I would just think about is that, like, meetings is not very differentiated.

**Ryan Singer:** So I would just think about, like, what is this that makes it different than just any meeting?

**Ryan Singer:** You know what I mean?

**Ryan Singer:** So that it's clearer what the value is or like, what the function is of this thing.

**Board Room:** So like, or something like, yeah, there's.

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

**Board Room:** Yeah, no, that makes sense because every client has these two phases.

**Board Room:** One is the calibrate intake phase or the strategy sprint phase, how you call it.

**Board Room:** And the first part of this phase is essentially if they go to this setup here and they do all this seven steps, record all your meetings, make sure you understand their company and products Record that in the system.

**Board Room:** Define their Personas, define their taxonomy, calibrate their style.

**Board Room:** Validate their style with sample articles by annotating them.

**Board Room:** Connect the Google search console, connect their.

**Ryan Singer:** Analytics and by the way, validate.

**Ryan Singer:** Validate their style is so much better than sample articles.

**Board Room:** That's a good.

**Ryan Singer:** Yeah, calibrate the verbs.

**Ryan Singer:** So calibrate their style.

**Ryan Singer:** Validate their style.

**Ryan Singer:** And sample articles is how you do it.

**Ryan Singer:** Like that's.

**Ryan Singer:** That's.

**Board Room:** Yeah, yeah, that's a good.

**Board Room:** Yeah, that makes sense.

**Board Room:** I'll make note of that for life anyway, and then to collect your website then we can start that.

**Board Room:** That's the minimum that we need to do the work.

**Board Room:** And if the team spends two weeks doing this, that's great, you know, like because from now on everything is going to be fine.

**Board Room:** But like yeah, they would just jump straight into this and then it's total, total shit.

**Ryan Singer:** Yeah.

**Board Room:** So the system.

**Board Room:** So that's how we do today different ways.

**Board Room:** So like we would like people will use notion airtable.

**Board Room:** Marcel has a bunch of things the notion that they need to follow.

**Board Room:** Then we're making that into the system now.

**Board Room:** So you have to go through this and click on these buttons and.

**Board Room:** And help.

**Board Room:** It will help you do some of the legwork here instead of having to go into perplexity and research that kind of stuff or post processor beans.

**Board Room:** So the meeting sport is for these two phases is the intake phase when you're calibrating and then you're testing with the client.

**Board Room:** And then afterwards we also want to have some sort of recipes that will look for.

**Board Room:** Is this client upset?

**Board Room:** Like, is this client showing signs of like positive sentiment?

**Board Room:** Are they hitting their goals?

**Board Room:** Did you ask their goals?

**Board Room:** But there's like a lot of like post processing ongoing meetings as well.

**Board Room:** Yeah, just put it out for now and just like not being part of the scope but that area will grow.

**Ryan Singer:** Yeah.

**Board Room:** And it's so interesting, you know.

**Ryan Singer:** Got it.

**Ryan Singer:** Yep.

**Ryan Singer:** Anyway, yeah.

**Board Room:** So okay, so this is a setup area and then the learning improve probably the resolution is actually.

**Board Room:** So when I send you the video you're going to see 4K so it's going to be better.

**Board Room:** But we have looks fine here.

**Board Room:** And then backlog briefing.

**Board Room:** This is the status of the work that is getting done and it will show both new and optimization in here.

**Board Room:** We also almost always want to see the page is clustered by the things you care about.

**Board Room:** They're optimizing for.

**Board Room:** So I baked in the clustering here.

**Board Room:** We might also want to add some charts for some of the core metrics.

**Board Room:** If you're focused on impressions, maybe we'll show the chart in the cluster here or something like that.

**Ryan Singer:** But yeah, like a Sparkline.

**Board Room:** Yeah, yeah, I Sparkline, exactly.

**Board Room:** We have the idea of helping you define the clusters.

**Board Room:** So that would be.

**Board Room:** You can combine things from the taxonomy or for some of the fixed fields that we have, like Personas is a drop down, for example, or some other things.

**Board Room:** So you can combine that and create the clusters.

**Board Room:** And you also have the.

**Board Room:** I don't know if you saw this last time.

**Board Room:** I don't think I had this last time actually.

**Board Room:** And then you have Smart View.

**Board Room:** Smart views essentially predefined filters with sorting.

**Board Room:** And those are the things that you want people to think about.

**Board Room:** And then when you go in, so.

**Ryan Singer:** Surging in almost top three is a smart view.

**Board Room:** Yeah, yeah, exactly.

**Ryan Singer:** Yeah.

**Board Room:** Cool.

**Board Room:** So you would click on that.

**Board Room:** So those are two Smart View combined.

**Board Room:** So those are checkboxes.

**Board Room:** So you could check them and you have multiple things combining filters basically.

**Board Room:** It might be too hard to do for this launch, but I think at least I can visualize the whole system now.

**Board Room:** And then we'll figure out what can be done in the next three weeks.

**Board Room:** And then we have the pages in here.

**Board Room:** There's some little bugs that we need to get the guys to fix the alignment here.

**Board Room:** But you can hover over and see things on the.

**Board Room:** On the right real quick or you can click and then switch to here and see we're going to have to clean up this.

**Board Room:** There's some things here that doesn't make sense anymore.

**Board Room:** Like the quick actions.

**Board Room:** Some of the quick actions you want to have is like categorize.

**Board Room:** This is the taxonomy part still makes sense.

**Board Room:** View on site still makes sense, but optimize it for here.

**Board Room:** I don't think it makes sense anymore because there's more work to be done there.

**Board Room:** But when you go into the page, let's say I we'll open one of these.

**Board Room:** Then we have the same.

**Board Room:** I think we had this before as well.

**Board Room:** So we have like a lot of like analysis that will be done on top of your core metrics.

**Board Room:** So the whole thing will be like on those core metrics at the page level.

**Board Room:** And then there's some other things that common mistakes that people do.

**Board Room:** Like they don't have their open graph set up, for example.

**Board Room:** That's super important.

**Board Room:** So like we're surfacing in here the keywords that article rank for and the taxonomy here as well.

**Board Room:** So taxonomy would want to edit.

**Board Room:** And then everything here, they're clickable.

**Board Room:** So you could just like, look at those things and you're like drilling down one of the pages that, that you created or that you shipped recently, or they're decaying all of them.

**Board Room:** We're like doing like, we have like AI workflows for taking in the data and taking context and creating a quick analysis of things.

**Board Room:** So that's going to be throughout the system.

**Board Room:** And then content is just a quick way for you to see what the content looks like in markdown form.

**Board Room:** And activity would be the feed of the work that was done on this page.

**Board Room:** And then if we go into backlog, backlog is where backlogging forward is where the work would get done.

**Board Room:** Same idea.

**Board Room:** So you can see the pages, same UI cluster the same way.

**Board Room:** With the sidebar, you'll be slightly different because you have like the name of the word icon.

**Board Room:** And then when you click on it could be like here or here or from here you would go into the place where a first step would be empty like this.

**Board Room:** So you would see where the opportunity came from, where the idea of this content came from.

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

**Board Room:** This is a new page.

**Board Room:** So this is an assignment for a new page or work item for creating a new page that you accepted as you're going through the opportunities.

**Board Room:** So the opportunities.

**Board Room:** Maybe I need to spell it out and say a new page or create a new page or create a new page, if that makes sense.

**Board Room:** Yeah.

**Board Room:** So this is essentially like a to do it, that is create this page.

**Board Room:** And the idea here is like the title is X best because you don't know how many should be in the article yet.

**Board Room:** So that's not the title of the article, that's just the name of the opportunity.

**Ryan Singer:** Okay.

**Board Room:** Create a listicle for this topic.

**Ryan Singer:** So this new page task doesn't live under new page opportunities.

**Ryan Singer:** It lives under learn and improve because.

**Board Room:** That you already accepted.

**Board Room:** So here would be where you'd find all the opportunities.

**Board Room:** So we would have like actual stuff that I made it work yesterday.

**Board Room:** But on the normal setup with like simple data here, you would have a list of keywords or list of ideas with their traffic, potential traffic with their estimated traffic that you can get from it.

**Board Room:** Based on your size and some other things.

**Board Room:** And then when you accept and also suggestion, this would be a listicle or this should be a comparison article.

**Board Room:** This came from a competitor, for example, or this came from a trending topic.

**Board Room:** There's like a bunch of ideas here.

**Board Room:** And then you pick the ideas that you want to work on.

**Board Room:** And that would be like when you click Accept, that would send the idea to the Learn and Improve area.

**Board Room:** Because now you're actually working on the.

**Board Room:** On the page.

**Board Room:** Now it's like it's a real page.

**Board Room:** Like you're.

**Board Room:** It's a draft page.

**Board Room:** But you accepted that this should be a page on your website.

**Board Room:** So like, learning, improve.

**Board Room:** It's all about the pages.

**Board Room:** And here is just ideas, you know, that might apply or might not apply.

**Board Room:** Maybe, maybe it's like learn and improve.

**Board Room:** Find new page opportunities and then create new pages or create content or like something that's like.

**Board Room:** It does feel like the three jobs to be done that I, you know, feels too buried a little bit.

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

**Board Room:** I think at the very beginning, I think like there would be assignments.

**Board Room:** So like, I'm assigned to this item, for example, when I accept or give it to someone else.

**Board Room:** And we're going to need for sure like a my stuff or like my assignments kind of thing that like the basecamp has or linear has, where you see all the things that are yours.

**Ryan Singer:** You know.

**Board Room:** That somewhere.

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

**Board Room:** Yeah, that's how I was thinking.

**Board Room:** So you would have here in page portfolio would see your existing pages and you'd see the ones that are creating and you'd see the ones that you're optimizing as well.

**Board Room:** And they would all be in the backlog as well.

**Board Room:** So if you switch to backlog, you would see create or improve.

**Board Room:** There would be different types of items in the backlog.

**Board Room:** But yeah.

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

**Board Room:** Know.

**Ryan Singer:** So you can think of this almost like.

**Ryan Singer:** There might be an objection of like, well, should my work be in two places?

**Ryan Singer:** But I think this is where floating up my work or assignments or whatever as a, as a, as a top level place.

**Ryan Singer:** So like, if I just want to see like work I could go to just work, you know, but if I want to see like what are the new pages that we're working on, then it would make, it's going to make more sense in new page opportunities to see like, here's, here's the opportunities and here's the opportunities that you've already sort of like claimed or said that you want to, you know, you've kind of prioritized that you want to do.

**Board Room:** Right?

**Ryan Singer:** So you can think of these almost like, think of like learn and improve and new page opportunities almost like filters on the same underlying data structure.

**Ryan Singer:** You know what I mean?

**Board Room:** Yeah, yeah.

**Board Room:** The thing that I'm thinking here though is that I wonder if just the menu items are wrong, the naming here.

**Board Room:** You know, like I was even thinking we want to sell things differently.

**Board Room:** Like creation is like a whole module within the os.

**Board Room:** Learn and Improve and Finding Opportunities is like a separate module because like there's a lot of people that are paying a half ton of money for agencies just give them briefs and, and help them identify issues on their site.

**Board Room:** If we go on that rabbit hole I think it's going to be like so hard to split the software just on based on add ons that people should perform.

**Board Room:** You know but like we could very easily just add like pay walls and stuff like that in this experience.

**Board Room:** But I think we should just optimize for like if you have all the add ons turned on what is yeah in it.

**Board Room:** I like the Learn and Improve is one mode that explore new opportunities and you're just like I was just on a one hour call with our strategy sprint team and it's just mostly like they're recording these 20 minute looms explaining the strategy and their strategy for new pages which is like content clusters, how they're organizing the new opportunities, how they're, you know, the, the reasoning behind the clusters and how they're organizing opportunities.

**Board Room:** The thought process they went into in order to find those opportunities.

**Board Room:** Like that is like strategy.

**Board Room:** Right.

**Board Room:** And then the creation is like a whole other game that is like very separate from those two modes.

**Ryan Singer:** Yeah.

**Board Room:** Like the problem that kind of sets that I don't have them the data here on the actual maybe production hub.

**Board Room:** But opportunities they have.

**Board Room:** There's a clear distinction between a bunch of ideas and like the fields are the data set.

**Board Room:** The data structure is different, the work you do is different.

**Board Room:** So you're dealing with like sometimes 2000 things on your air table for example and you're clustering them and you are dismissing them in bulk.

**Board Room:** You're accepting them in bulk.

**Board Room:** You're just like the names or things are not so very spelled out.

**Board Room:** It's more like X for Y for example.

**Board Room:** Literally like X products for some alternative that's literally like one of opportunity idea and has like a bunch of keywords attached to it.

**Board Room:** So like you have, you're in a different mode of like just triaging to a bunch of stuff, loading the things between the system and triaging them again.

**Board Room:** And you do some, some, some analysis automatically that will be like oh this is the Persona or not so automatically the system will be like filtering out the noise.

**Board Room:** And that already happens today in the what we have working, working here.

**Board Room:** And then when you accept that that goes into like it's almost like a different person does a job, you know.

**Board Room:** So maybe Here it's just like opportunities or ideas or something like this.

**Board Room:** And then page is when, then page is like actually when you want to do the work.

**Board Room:** You know, because that, that challenge happens at the, even at the split of the system as well.

**Board Room:** You know, like I'm.

**Board Room:** But I think like I, I feel like we're all seeing kind of like the same thing except like the Learn and improve.

**Board Room:** All we're saying is like that.

**Board Room:** That's what I struggle with too.

**Board Room:** It was like if you mix optimization and creation in the same views as just like a subtle drop down or filter or a label in the same view, the experience can be effectively the same that you have here.

**Board Room:** But I think it has to be separated.

**Board Room:** Yeah, we could have.

**Board Room:** That's what I'm saying.

**Board Room:** Maybe the main new could be different than there's a new view from those things, but the process is essentially the same.

**Board Room:** Like this could be like moved out of here into Create page.

**Board Room:** You know, that's what I'm saying.

**Board Room:** It's like learn, improve, find new product page opportunities.

**Board Room:** Create new.

**Board Room:** Yeah, you know, and then like create new or whatever.

**Board Room:** Yes, yes, create that and puts it there.

**Ryan Singer:** Create as a, as a, as a, as a sibling.

**Ryan Singer:** Yeah, learn and improve.

**Ryan Singer:** Find.

**Ryan Singer:** Find opportunities like or new page opportunities and then create.

**Ryan Singer:** Because the finding of the opportunities is a totally different mode.

**Ryan Singer:** It's a different, it's a different like different kind of work than the actual creation states.

**Board Room:** Right?

**Board Room:** Like different states as in like I just have a shit on the stuff now.

**Board Room:** I filter down now.

**Ryan Singer:** Yes.

**Board Room:** You know.

**Ryan Singer:** Yeah.

**Ryan Singer:** So let's say that creation.

**Ryan Singer:** Would that mean that creation actually doesn't show up here inside of Learn and Improve at all and we're only seeing optimization tasks?

**Ryan Singer:** That's kind of what I would assume that this structure is telling me like as a user, like if Learn and Improve is about experiments, I would expect everything here to be optimization work.

**Board Room:** Yeah, I think that could work.

**Board Room:** I think that, yes.

**Board Room:** Even the backlog breathing and writing that even be like the one is like refreshing.

**Board Room:** Another one might be like optimization.

**Board Room:** Another one might be like, I don't know.

**Board Room:** Right.

**Board Room:** Like.

**Ryan Singer:** Yeah, that's, that's the other thing is these pipeline stages, they sound very creation focused and they kind of don't really track to optimizing.

**Board Room:** Yeah, that's, that's, that is a good point.

**Board Room:** Like for instance, like in the study that Katya did.

**Board Room:** Right.

**Board Room:** Like citation is really important.

**Board Room:** Right.

**Board Room:** And referencing it.

**Board Room:** Right.

**Board Room:** Like so it's like.

**Board Room:** And then like the structure of the pages or whatever.

**Board Room:** Like so it's almost like addressing some of these things that that's another thing that I, that that's the main thing that I wanted to talk today was just like how does optimization look like?

**Board Room:** Because the creation I have here.

**Board Room:** So for example, let's let just like finish the flow.

**Board Room:** But like let's assume that this is.

**Board Room:** That's Assume we pull this out and we have a create menu here and all you've seen is a creation of new pages.

**Board Room:** When you go into creation mode, the flow is very specific.

**Board Room:** As in like you have a brief, you generate an outline, the outline, you work on the outline quite a bit and then you let the agent go do the research.

**Board Room:** And that might take a full hour.

**Board Room:** So like some of our agents will spend like a full hour just researching everything and putting the article together.

**Board Room:** And then you go into editing mode and then so like that I have and I can show you real quick, the optimization is completely different as in like once I finish this.

**Board Room:** But there's like specific tasks on optimization.

**Board Room:** So like this is the creation process, for example.

**Board Room:** So let's say this is the.

**Board Room:** The assignment that I'm taking is X best as an alternative for small teams working for a lovable creating a page for them.

**Board Room:** Let's say the idea.

**Board Room:** I can still see the idea where I came from, the search intent and all that.

**Board Room:** I don't need to do anything with this.

**Board Room:** The agent will do the work, just that for context, I can choose a content type.

**Board Room:** So it'll be automatically selected because it's a listicle suggestion.

**Board Room:** This like each one of these content types is a different agent.

**Board Room:** Like they perform different doing assembling the article in different ways and doing the research in different ways.

**Board Room:** But the user doesn't have to know that.

**Board Room:** And then you pick the Personas.

**Board Room:** The search intent is here.

**Board Room:** Just if you want to change it.

**Board Room:** Sometimes it might not be fully accurate how you see the space.

**Board Room:** You can give more directions.

**Board Room:** You can say like actually start with a hook in a different way or close with a CPA in a certain way, but you don't have to.

**Board Room:** And you can also give like a range of word count.

**Board Room:** And then when we hit that, it would generate the.

**Board Room:** The outline.

**Board Room:** And the outline is usually this format where you have the section and what should be under each section and how.

**Ryan Singer:** It should be written.

**Board Room:** And you can spell out as much as you want or you can keep it short.

**Board Room:** And then we have a writing agent that will take this, do the research under each one of these outlines.

**Board Room:** There's also research questions that will be performed.

**Board Room:** That's just for reference for the folks to see what's going to be researched.

**Board Room:** And then when you click Generate, then this will go through the work.

**Board Room:** Once it's done, then you have an interface like this where you have the meta, you have the article title.

**Board Room:** Now for real, you have the meta title that's sometimes different.

**Board Room:** Sometimes you can have a suffix like this and then you have slug meta description and the COVID image and you can regenerate them if you didn't like.

**Board Room:** And if you want to annotate the article with the problems that you have, you go and review and then you can highlight the problems and the problems are like the set of problems and they have severity.

**Board Room:** And you can write a comment if you want, but even if you don't write a comment, we would be able to do a lot with that already.

**Board Room:** And then once you're done and you finish the review, you can also write high level.

**Board Room:** So that's kind of the first thing we talked like last month was this screen.

**Board Room:** And then when you finish this, then you would then the agent, we have an admin agent that you take your feedback and try to apply it.

**Board Room:** And then you would be in a free form notion next, this is just like a temporary text area.

**Board Room:** It would be like a notion document that you can freeform right from here and save.

**Board Room:** And once you're done, you're back into here and you can, if you don't have your CMS connected, you could just export.

**Board Room:** If you have connected, it would have a button to publish.

**Board Room:** So that is the process for creation optimization would be like completely different.

**Board Room:** So I hope that all made sense or.

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

**Board Room:** Yeah, yeah, I think so.

**Board Room:** I think the creation I think we can crack and we can at least get the scheme that we have in the company.

**Board Room:** People that will be going to this workflow will be the folks that we train.

**Board Room:** So the set of like 50 people at most.

**Board Room:** So it's very trainable and we can continue to iterate on that.

**Board Room:** I think I can get out of the hole.

**Board Room:** The optimization is the part that I'm like, okay, this is a different piece in the system and can go in many different ways.

**Board Room:** What am I optimizing?

**Board Room:** Optimizing chunks of text in the article.

**Board Room:** Is it optimizing many things at once?

**Board Room:** Is it small to do's or is it a giant thing that you do everything at once?

**Board Room:** Where does it live?

**Board Room:** So there's that and then another part of the system that we deal with quite a bit is giving the clients or even giving our own team like a place to share what's happened.

**Board Room:** So like here's the thing that we did and so they're completely different topic.

**Board Room:** So those are the two things.

**Board Room:** Too many areas of the system that today I'm like, huh, that can be a rabbit hole in itself.

**Board Room:** Optimize is a fast follow that we have to do.

**Board Room:** Like as soon as I ship this in March, optimization has to start like almost right after, like figure out how to do the optimization part.

**Board Room:** And another part is it's less pressing like this.

**Board Room:** But it's a, it's a thing that we need to figure out eventually is like how do you keep the clients in the loop?

**Board Room:** And people are not good at that.

**Board Room:** So that's what the progress snapshots is for here.

**Ryan Singer:** Yes.

**Board Room:** And we have the same thing on check that.

**Board Room:** So check that.

**Board Room:** We collect like a ton of data, but it's charts and data.

**Board Room:** So people to make sense of it, they need recipes.

**Board Room:** Basically like look at here, look at there, analyze what happened, analyze what changed, create a report in your mind or send that to your boss or something like that.

**Board Room:** But in essentially you need to be like doing status check on this product on the regular.

**Board Room:** And if we need to do that, might as well do most of the work and people just tweak it.

**Board Room:** So that's how we're thinking about the progress snapshot.

**Board Room:** So both tools will need the similar idea.

**Board Room:** And some of the knobs are the same as in like impressions or visibility or here's things that went up and the things that went down in this field.

**Ryan Singer:** Okay, let me.

**Ryan Singer:** Daniel, can I check if I understand right?

**Ryan Singer:** So there's a.

**Ryan Singer:** So first of all, this pipeline that we're looking at inside of Learn and Improve actually isn't.

**Ryan Singer:** Doesn't belong here because we don't have a pipeline for optimization yet.

**Ryan Singer:** This is really just page creation right now.

**Ryan Singer:** Is that true?

**Ryan Singer:** Okay, so let me just, I'm actually gonna, Let me take over for a moment and I want to start.

**Board Room:** I.

**Ryan Singer:** Just want to start capturing some of these things so we don't only have words on the, on the recordings.

**Ryan Singer:** Okay, so first thing, what is wrong today?

**Ryan Singer:** Okay, so like this doesn't belong here.

**Ryan Singer:** And this moves to.

**Ryan Singer:** There's a new thing which is something like create.

**Board Room:** Yeah, right.

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

**Board Room:** Yeah.

**Ryan Singer:** And so Learn and Improve is kind of like, how do I create an improvement?

**Ryan Singer:** And progress snapshots is like, how do I tell about an improvement that happened?

**Board Room:** Yeah, yeah, there's also like the progress snapshots today.

**Board Room:** Like if I just show you real quick, that's just like a rough mock up that I spent essentially no time on it at all.

**Ryan Singer:** But yeah, let's see.

**Board Room:** Essentially it's the email that we should be sending our clients every week, which would be like, we have 10 ideas, 10 cluster ideas with 100 pages each.

**Board Room:** We made progress on 20 of those ideas on each one of these clusters.

**Board Room:** Some of them are starting to get impressions.

**Board Room:** 10% are getting impressions, for example.

**Board Room:** The other 90% is too soon.

**Board Room:** And we also worked on improving 100 of your existing pages by adding the right meta tags, adding the right OG tags and that kind of stuff.

**Board Room:** And they're starting to get maybe 10 of those pages are getting better impressions on Google Search.

**Board Room:** So that would be like, if you present your meeting like this and if you send an agenda ahead, this proxy snapshot is essentially an agenda for what we should be sending ahead.

**Board Room:** Or if a client just logs in and see it, they would be able to see, okay, here's the progress we made.

**Board Room:** Here's the thing that we're still working on here, the progress on the data that we're seeing, here's the experiments we're running, and here's the metrics.

**Ryan Singer:** So yeah, here's one thing I would call out.

**Ryan Singer:** A brief can have a really different meaning based on is this a brief for me in order to make decisions or is this a brief for me to, to know that you're doing your job right.

**Ryan Singer:** So like, like the presidential brief is like, this is what's going on in all these different countries.

**Ryan Singer:** So that, the, so that, so that as an executive, you know, there's, there's actions that have to be taken.

**Ryan Singer:** And what I, what I actually see when I look at this right now as a first blast, as a first, as a first pass, when I see, especially on the top, which is weekly content intelligence brief.

**Ryan Singer:** Like if, if I'm supposed to make a decision about content, then I want an intelligence brief about what's been happening.

**Ryan Singer:** If, if I'm not here to make a decision, but I am here to see that like you're, you're doing what I paid you for, you know?

**Ryan Singer:** And like, or like things are, I don't need to intervene because like you're doing what I expected, you know.

**Board Room:** Yeah, yeah, yeah.

**Ryan Singer:** Then, then that would be a very, very different angle.

**Ryan Singer:** That would be more like, it should be more like status report in the sense of like a status report is like where you report up of like this is what I did.

**Ryan Singer:** You know what I mean?

**Board Room:** Yeah.

**Board Room:** I think if we're just focused on the content OS and how we operate it today, I think we would need both.

**Board Room:** I think we need a brief for decision making at least every large milestone of the engagement, like, maybe every three months.

**Board Room:** And you do need a status report probably every week.

**Ryan Singer:** Yeah.

**Ryan Singer:** I would guess.

**Ryan Singer:** I would guess that based on what we've been talking about so far, that the.

**Ryan Singer:** The.

**Ryan Singer:** The.

**Ryan Singer:** The core of progress snapshots is actually status.

**Ryan Singer:** No.

**Board Room:** Yeah.

**Board Room:** What do you think?

**Board Room:** What do you think?

**Board Room:** Where do you think we should spend our energy?

**Board Room:** So should we spend an optimize or should we go into the.

**Board Room:** Because you've been thinking about the progress.

**Board Room:** Yeah, I think, like, put snapshots aside.

**Board Room:** The snapshots are almost like a stopgap of our engagement.

**Board Room:** Managers are sending these Slack updates that are complete garbage that are just like.

**Board Room:** We publish five pages for you.

**Board Room:** Like, seriously, like, what the hell are you doing?

**Board Room:** Like, just like.

**Board Room:** But Llama was decent.

**Board Room:** Like, if you.

**Board Room:** If you look at.

**Ryan Singer:** This.

**Board Room:** Remkus or.

**Board Room:** Yeah, yeah.

**Board Room:** So it's like they send this.

**Board Room:** This their status update, right?

**Ryan Singer:** Oh, yeah.

**Ryan Singer:** Yeah.

**Board Room:** Gosh.

**Board Room:** Dear God.

**Board Room:** We're just crazy.

**Board Room:** And that's it.

**Board Room:** Like, well, this is just.

**Ryan Singer:** This is like commodity.

**Ryan Singer:** Commodity work.

**Board Room:** Commodity.

**Board Room:** Exactly.

**Board Room:** Yeah.

**Board Room:** Then they look at it and they go, cool, you did something.

**Board Room:** Seven.

**Board Room:** That's worth $700 to me.

**Board Room:** It's $100 per.

**Board Room:** Like, you know what I mean?

**Board Room:** That's your value to me.

**Board Room:** It's $700 this week.

**Board Room:** Yeah.

**Board Room:** I'm paying you 18 grand a month.

**Board Room:** Like, what the am I doing?

**Board Room:** Exactly.

**Ryan Singer:** Yeah.

**Board Room:** And.

**Board Room:** And instead, it should feel like, holy crap, you legit have an army of agents going through and doing all this stuff, and you're connecting the dots for me and you're going through and, like, showing, like, where, like, we're heading and how things are improving, essentially.

**Board Room:** Seven.

**Board Room:** That you took us out of exploring 10,000 ideas.

**Board Room:** Yeah.

**Board Room:** And validated all the six Personas and pick the one that made most sense for our product.

**Board Room:** And it's with the framework of, like, we've been building these kind of, like, context files and things like that.

**Board Room:** And when we run all our transcripts and all our data through one of those, like, what comes out is, like, so much better than this shit.

**Board Room:** Right.

**Board Room:** And then we're like, okay, why are we letting humans do this at this point?

**Ryan Singer:** Like, totally.

**Board Room:** And it's like the going back to our mental model of, like, where the work is outputs, but the outputs are to deliver Outcomes and there's leading and lagging outcomes.

**Board Room:** And we need to connect the dots between the context of the company and their goals, to the work we prioritize, to the this validate to the outputs we deliver to did we learn or is this having the impact on the outcomes that we said it was going to be?

**Board Room:** Yes or no?

**Board Room:** And what are we doing about it?

**Board Room:** Right.

**Board Room:** So snapshots is like a gnarly thing that as long as it's better than what you just saw, it's a win.

**Board Room:** And then improvement is the way I think about improvement is like finding failure modes in the existing pages and addressing those failure modes so that you addressed it once, but later on you turn it into a systematic approach to like addressing that.

**Board Room:** For instance.

**Board Room:** Right.

**Board Room:** Like when we.

**Board Room:** Like I was just reviewing actually a new customer, Blacksell.

**Board Room:** Yeah.

**Board Room:** B L A X E L. And one of the first piece of content we publish for them is like a listicle alternatives to Daily IO or some.

**Board Room:** One of their competitors.

**Board Room:** Right.

**Board Room:** There is like an agentic framework platform or whatever.

**Board Room:** And like the first sentence, like, we praise them, we link to their site and we link to a press release and it's like, dude, this is supposed to be like a fucking thing about alternatives to this thing.

**Board Room:** Like, why are you praising them in the first sentence and linking to two of their sources and sending them like equity like that.

**Board Room:** That's a very clear.

**Board Room:** Like, you know, like, you know.

**Board Room:** And the intro was pretty garbage, right?

**Ryan Singer:** Like, so this is an example of an optimization.

**Board Room:** Exactly.

**Ryan Singer:** Yeah, yeah, yeah, yeah.

**Ryan Singer:** Good.

**Ryan Singer:** Okay.

**Ryan Singer:** So.

**Ryan Singer:** Okay, so what I just heard was there's a million things that we could do around snapshots, but as long as the snapshot is not what we just saw in Slack, it's kind of doing the job for now.

**Ryan Singer:** And therefore we should focus over on optimization for today.

**Board Room:** Yeah, yeah, yeah.

**Board Room:** I think snapshot's pretty.

**Board Room:** Yeah.

**Ryan Singer:** Okay.

**Board Room:** It's a low bar.

**Board Room:** Yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** All right.

**Board Room:** And yeah, so I can share whatever context you think would be helpful on the.

**Ryan Singer:** Yeah, let's.

**Ryan Singer:** What I want to maybe suggest that we start with here is since we have kind of a blank sheet that we're starting from, you know, whenever I have a blank sheet, I want to start with work with use cases or example cases.

**Ryan Singer:** So can we just collect like, what are the types of optimizations that should be happening via Learn and Improve?

**Ryan Singer:** You know, and like what we want is like multiple concrete examples that are different.

**Board Room:** Yeah.

**Board Room:** So maybe a mental model here is like, there's no good to have Sentry set up on error logging and then look at it like a freaking like 50,000 things, right.

**Board Room:** That are alerts.

**Board Room:** Right.

**Board Room:** Like, what we're trying to do instead is like, group them in the right altitude.

**Board Room:** That makes it like, actionable enough but not too down in the weeds.

**Board Room:** That just becomes like, you're out of context.

**Board Room:** Right.

**Board Room:** So the grouping and the altitude of the grouping is really critical.

**Board Room:** The way like.

**Board Room:** Like the way I kind of think about it is potentially like, fixing issues versus, like, improving content versus, like, refreshing the content.

**Board Room:** And then the question mark for me is like completely refactoring, AKA like creating new and replacing.

**Board Room:** Creating.

**Board Room:** Replace it.

**Board Room:** You know, which is like more of the creation one, which is like, this is so garbage.

**Board Room:** This is so bad.

**Board Room:** But don't get rid of the surface area because there's already like, equity in this URL.

**Ryan Singer:** Yeah.

**Board Room:** And like, the URL slug can be repurposed and the last would be like, pruning the lead archives.

**Board Room:** Retract kind of like, you know, essentially like pruning.

**Ryan Singer:** Yeah.

**Board Room:** So what I want to do is fix issues.

**Board Room:** Improve Refresh.

**Board Room:** Refactor.

**Board Room:** I think you're missed.

**Board Room:** Delete.

**Board Room:** Fix issues.

**Board Room:** Yeah, yeah.

**Board Room:** Fix, Improve.

**Ryan Singer:** Improve is different than refresh.

**Board Room:** Yes.

**Board Room:** So like, improve it is like around, like the intro just is.

**Board Room:** Is just bad or.

**Board Room:** Or something like that.

**Board Room:** Whereas, like, refresh again, we can discuss to make sure, see if we want to consolidate.

**Board Room:** But refresh is truly like, this thing has not been touched for six months and it's going to decay if you don't touch it.

**Board Room:** You need to refresh new stats, add a couple of things.

**Board Room:** It's just truly just to say, because these engines look at last modified or dates quite a bit.

**Board Room:** So it's like just adding a couple new stats or a couple new things is just really important.

**Board Room:** Keep it fresh, essentially, you know.

**Ryan Singer:** Yep.

**Ryan Singer:** Huh.

**Board Room:** What about the issues?

**Board Room:** Can you talk more about the kinds of issues?

**Board Room:** Yeah, like the.

**Board Room:** The issues ideally are us finding like, the patterns that are significant in both SEO AEO as well as, like, engagement.

**Board Room:** Right.

**Board Room:** And.

**Board Room:** And so it just could be like broken links.

**Board Room:** It can be like factual inaccuracies.

**Board Room:** It could be, you know, like h too many H1s and H2s or like, just like that.

**Board Room:** The structure of it.

**Board Room:** Right.

**Board Room:** Technical issues as well.

**Board Room:** Right.

**Board Room:** Like slow to load images.

**Board Room:** Yes.

**Board Room:** But I think those are gonna have to be systematic.

**Board Room:** Systematic.

**Board Room:** It's like, it's very rare that, like.

**Ryan Singer:** It could be like a page.

**Board Room:** Broken image.

**Board Room:** Broken image can be a PA Page.

**Board Room:** Yeah, like, issue.

**Board Room:** Right.

**Board Room:** Whereas, like, you know.

**Board Room:** Yeah, like, it just could be like AI slob.

**Board Room:** Right.

**Board Room:** It could be like all the things that we're like labeling.

**Ryan Singer:** It's got to be.

**Ryan Singer:** It's got to be vertical to the page, not horizontal to the platform.

**Board Room:** Yeah.

**Board Room:** Like.

**Board Room:** Yeah.

**Board Room:** Faction accuracy.

**Board Room:** It could be like outdated product mentions.

**Board Room:** Right.

**Board Room:** Like, no cta, lack of cta, bad cta, you know.

**Ryan Singer:** So how is, how are these different than improvements?

**Board Room:** Improvements could be like, add an FAQ section at the bottom, you know, but.

**Board Room:** But where it's like.

**Board Room:** Think of it as like in a publishing pipeline.

**Board Room:** The.

**Board Room:** The fixed issues would block you from publishing and the improvements would be publish and then add and make it better.

**Board Room:** Never thought about that.

**Board Room:** That's it.

**Board Room:** Like, if you're introducing a critical bug, you shouldn't ship it.

**Board Room:** Right.

**Board Room:** But if you're not, you can ship it and then make it better.

**Board Room:** Like, so that you learn from it in the process.

**Board Room:** Don't stop yourself from learning, you know?

**Ryan Singer:** Okay, I see.

**Ryan Singer:** So the intro might be bad, but if not, if the, if the, if the links and the images aren't broken, the structure is correct and it's not factually inaccurate, then it doesn't block us.

**Ryan Singer:** Like, this is literally like this.

**Ryan Singer:** These are things where like, you should, you should not be live with any of these things happening.

**Board Room:** Yeah, exactly.

**Board Room:** That's a good way to think about it.

**Board Room:** Yeah.

**Board Room:** Yeah.

**Board Room:** Those are like, yeah, P1s, P0s to P1s, depending on it, you know.

**Board Room:** Or like, let's say it's missing like an open graph image or the meta description is a duplicate meta description or missing completely.

**Board Room:** The, you know, the, the meta title is wrong or missing or something.

**Ryan Singer:** So these are actually health checks that are like, must pass.

**Board Room:** Yeah, yeah.

**Ryan Singer:** In that.

**Board Room:** And what I think about it is like, this is very much like, there's like a set of patterns to look for here.

**Board Room:** It's.

**Board Room:** It's decently black and white here.

**Ryan Singer:** Yes.

**Board Room:** It's not like fuzzy, grayish, like, I don't know, you know, it's kind of like it's.

**Board Room:** It's fairly grounded on what works.

**Board Room:** What's like, you know, and things.

**Ryan Singer:** And it's also objectively, this is, this is like objectively, let's say, measurable that it's happen.

**Ryan Singer:** Yeah, yeah.

**Ryan Singer:** I mean, maybe this is a little bit harder than some of the other ones.

**Board Room:** Yeah, yeah.

**Board Room:** Bad CPA is also hard, but the other ones are.

**Board Room:** Huh?

**Board Room:** Yeah.

**Board Room:** Let's pull this, for instance.

**Board Room:** Like something in their guidelines, like with Clerk, for example, they're like, don't use login.

**Board Room:** You sign in or Some like that, you know, and it's like that's a hard rule, you know.

**Board Room:** Think of it as like cursor rules, hard rules.

**Board Room:** Like like plot rules.

**Board Room:** Right.

**Board Room:** Like, or like agent rules where it's just like do this every time.

**Board Room:** Right.

**Board Room:** Versus like a skill.

**Board Room:** So like this is more like hard rules that shouldn't be broken but that, that can have a reference doc that has a running list of these rules, you know, and for each page.

**Board Room:** And some of these are rules and some of these are like optimization patterns that are generalized that are important.

**Board Room:** Right.

**Board Room:** If you mention a stat and you don't want to trivia who that stat is from or how you found that stat, like that's bad.

**Board Room:** Like you know that that's like a very like established thing.

**Board Room:** You can turn it off and you can override it.

**Board Room:** But, but right.

**Board Room:** Like don't let traffic through, you know.

**Ryan Singer:** So is this, this is like a domain specific example that like for one client this might be true but not necessarily for everybody.

**Board Room:** Or, or that one is like a pattern for like how AI engines work.

**Ryan Singer:** Okay.

**Board Room:** Like other fetching information.

**Board Room:** They're very, a lot of them are very, very biased towards like quotation source attribution.

**Ryan Singer:** Yeah.

**Board Room:** Quality data sources that you're attributing an information to.

**Board Room:** You know, essentially you did your homework and you organized information and you're not like this is not slot.

**Board Room:** Yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** So we've got hard rules that can't be broken.

**Ryan Singer:** We've got, I think this, we understand we could say what this is and what it's not.

**Ryan Singer:** Right.

**Ryan Singer:** That there's a, there's a kind of a black and white test that is confident enough that you could actually block publishing on it.

**Ryan Singer:** Is that right?

**Board Room:** Yeah, I think so.

**Board Room:** Yeah.

**Board Room:** Yeah.

**Board Room:** Because they have levels of severity and some of the stuff we need to humans to check it can.

**Board Room:** And the way I kind of think about it is like it.

**Board Room:** If it's something that is optional, maybe you should go into improvement and exactly move out of our rules like standards, you know, and the standards can have like a strict mode and a flexible mode or something for that site or for that content type or that page type, you know, maybe I don't know that that way it's kind of like network rules.

**Board Room:** Right.

**Board Room:** Like, like it's sometimes like you might need to like.

**Board Room:** Yeah.

**Board Room:** Monitor and sometimes you might need to be okay with like some things like letting it pass, but then you need to establish globally that you're going to let that traffic pass forever.

**Board Room:** Yeah, yeah, yeah, yeah.

**Ryan Singer:** That's Crazy.

**Ryan Singer:** I didn't know that Teal Draw had markdown, actually.

**Ryan Singer:** That's crazy.

**Ryan Singer:** Okay.

**Ryan Singer:** Refresh.

**Ryan Singer:** I understand in the same.

**Ryan Singer:** I think refresh is like this in the sense that it's very, very clear what it means.

**Ryan Singer:** It basically means, like.

**Ryan Singer:** Like you're fixing a staleness problem, right?

**Board Room:** Yes.

**Board Room:** Yeah.

**Board Room:** Has not been touched in more than.

**Board Room:** And then you define a parameter for how.

**Board Room:** Ideally, like, you know, think of it as like, past due.

**Board Room:** You know, like, recently past due.

**Board Room:** Just like, okay, the.

**Board Room:** The.

**Board Room:** They didn't release the payment.

**Board Room:** Like, you know, then 30 days past due, it's like, yo, what's going on?

**Board Room:** And then like, night gate past due.

**Board Room:** It's like, what the.

**Board Room:** Like.

**Board Room:** Yeah, like, send them the.

**Board Room:** It's like the.

**Board Room:** Where's my money?

**Board Room:** You know, where's my money?

**Board Room:** Scenes from like.

**Board Room:** Yeah.

**Ryan Singer:** Okay, so now let me take these, I think are a good start.

**Ryan Singer:** I mean, all this is good, but I mean, these ones are like, like, solid in the sense that we understand them.

**Ryan Singer:** This feels fuzzier.

**Ryan Singer:** I would love if we could be more clear about this.

**Ryan Singer:** Can we.

**Ryan Singer:** Can we just collect a couple more examples?

**Board Room:** Let's put a pin on that one.

**Board Room:** Because, like, let's laugh out one for less, because I think it might make it a little bit easier.

**Ryan Singer:** Like, it might shake out.

**Board Room:** If it doesn't fit in anywhere else, it won't fit there.

**Board Room:** Yep.

**Board Room:** The, like, replacing.

**Board Room:** It's like, usually it's just shallow content, but the opportunity behind it was, like, decent, you know, so.

**Board Room:** So for instance, like, there is, like, sometimes in some of these sites, it's like legacy content that hasn't been touched for, like, three, four years, and it's literally like two paragraphs, and it's like, what the fuck is this?

**Board Room:** But then the URL slug was actually pretty good, and it has, like, a ton of links to it.

**Board Room:** You know, that is the case with Vercel, for example, for their AI gateway.

**Board Room:** Yeah.

**Board Room:** Literally, like two words.

**Board Room:** Yeah.

**Board Room:** Yeah.

**Board Room:** And so it's kind of like the page should exist.

**Board Room:** A page like this should exist.

**Board Room:** This is not it.

**Ryan Singer:** Yeah.

**Board Room:** Huh.

**Board Room:** This is like so many miles away that there's nothing, no substance in this page that should be repurposed.

**Board Room:** It's just like, hit reset.

**Board Room:** Right?

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** Huh.

**Ryan Singer:** How do you.

**Board Room:** It's truly a refactor.

**Board Room:** A like, you know, rip and replace, but in the same room.

**Board Room:** Not like, exactly.

**Ryan Singer:** Yeah, yeah.

**Board Room:** URL is the most important thing.

**Board Room:** Yeah.

**Board Room:** Like, because you.

**Board Room:** You don't need to set up, like, redirects.

**Board Room:** You don't need to, like, you Know, it's just easier to do that and the likelihood of that URL doing well because it's already established URL that has already like, also there's like, you know, cross linking within your site and backlinking to that URL potentially, you know, Whereas like, if it's the URL slug sucks, there's no links from within your site and no links externally, then it's most likely a delete and archive kind of situation.

**Board Room:** Right?

**Board Room:** Because it's just like, okay, like, yeah, maybe the idea here was good, but it's like this is a shitty URL slug.

**Board Room:** There's no equity in this URL, you know, and then it's like a.

**Board Room:** So you're talking about the delete and archive, right?

**Board Room:** Yeah.

**Board Room:** Then it's like a prune and prune and redirect, you know.

**Board Room:** Aha.

**Ryan Singer:** Got.

**Ryan Singer:** Got it.

**Ryan Singer:** Okay, let me just capture that.

**Ryan Singer:** I was, I was, I was honestly spinning on replace URL.

**Ryan Singer:** So this is like, it's, it's, it's, it's not, it's not, it's not well linked.

**Ryan Singer:** There isn't.

**Board Room:** Yeah, it's not well linked internally or externally.

**Board Room:** It has no sign of life, like, no, you know.

**Ryan Singer:** Yeah.

**Board Room:** And, and then the substance of it, there's no value to the substance of it.

**Board Room:** Tap into traffic and impressions as well.

**Ryan Singer:** Right?

**Board Room:** Yeah, it's usually like if you have a site that has.

**Board Room:** There's been a lot of studies on this, right.

**Board Room:** Like, and so like, think of it as like crawl budgets for SEO, but for agents, it's the same thing.

**Board Room:** And so you have limited crawl budget that is tends to be directly proportional to your site's authority and how it's perceived or your brand's authority in some cases.

**Board Room:** And so like the more you spread, the less signal you're going to get.

**Board Room:** And so you're a lot better.

**Board Room:** Like if you have like, let's say 10,000 pages that you're just like, no, it's fucking good.

**Board Room:** But, but like you have no signals, right?

**Board Room:** Like you're better off picking like the 100 that are the most.

**Board Room:** No brainer for Google to be like, well, there's nothing else in the world about this and yours is really good.

**Board Room:** And then you have this like really high quality signal and then it learns from that.

**Board Room:** Signals go, whoa, this is good, give me more, give me more, give me more of this.

**Board Room:** And you give it a little bit more and a little bit more and a little bit more, a little bit more.

**Board Room:** Until there's diminishing returns and you work your way through it.

**Board Room:** Whereas, like, if you just like say here's 10,000, it's.

**Board Room:** It won't even know how to prioritize it.

**Board Room:** So that's just gonna randomly prioritize it and ingest a lot of bad signals.

**Board Room:** Potentially.

**Ryan Singer:** Yeah.

**Board Room:** Right, because it's not going to send you like the cram or the cram, like traffic.

**Board Room:** It's going to send you the shitty traffic to those and then it gets like a bounce or something.

**Board Room:** Yeah, this kind of sucks, you know, and so you're better off like pruning aggressively anything that's like at the bottom.

**Board Room:** Right.

**Board Room:** And then the only cases where that's not it is that if it historically had traffic and it went down to zero, or like there's a ton of backlinking or a ton of linking internally.

**Ryan Singer:** Right.

**Board Room:** In which case you don't want a bunch of oral force, you know?

**Ryan Singer:** Yeah, that's part of this.

**Ryan Singer:** Yeah, yeah, yeah.

**Board Room:** Sorry, that was a long explanation of.

**Ryan Singer:** No, that's, that's, that's good.

**Ryan Singer:** How.

**Ryan Singer:** Let's, let's leave improved to the side for the moment.

**Board Room:** We should post process this, meaning as a blog post of how crawling and Google works.

**Ryan Singer:** This is literally how we see it.

**Board Room:** Happening on our clients.

**Board Room:** How the replace URL should have been the.

**Board Room:** Yeah, like replace.

**Board Room:** Yeah, replace URL.

**Board Room:** Yeah, replace and keep the URL.

**Board Room:** Replace the code and keep the URL.

**Board Room:** Yeah, it's like refactor.

**Board Room:** Yeah, exactly.

**Ryan Singer:** So these have what I can picture.

**Ryan Singer:** I can picture the tests that surface these.

**Ryan Singer:** This one also we have a clear test we could.

**Ryan Singer:** For how to surface it.

**Board Room:** Yeah.

**Ryan Singer:** How do you, how do you surface this?

**Board Room:** So this is once upon a time, this was good.

**Board Room:** It's clearly been dead for a while.

**Board Room:** Right.

**Board Room:** You know, and, and the, the only way to revive it is to like create a clone and you know, start from scratch here.

**Board Room:** But because this once upon a time was good and had some sign of life and.

**Board Room:** Or some sign of value, then you might as well keep the URL because it makes our lives a little bit easier, you know?

**Ryan Singer:** Okay, so how is this literally, like.

**Board Room:** This is truly like shallow content, you know, like.

**Board Room:** Yeah, like, like what the f is this?

**Board Room:** Like, like low work count.

**Board Room:** Like, like just, just like clearly nowhere near, like the quality bar that we have for the rest of the site.

**Board Room:** Yeah.

**Ryan Singer:** Okay, so if we were to like metricify this, it was good once, it's been bad for a while.

**Ryan Singer:** That's a traffic thing over time.

**Board Room:** Let me give you a quick example.

**Board Room:** This is a page for Vercel AI models.

**Board Room:** For example, and it's a great.

**Board Room:** This page should definitely be there, has the right URL as not even one paragraph of text and everything else is completely irrelevant to search engine.

**Board Room:** We're in contact with them to essentially like enrich these pages.

**Ryan Singer:** Yep.

**Board Room:** So that.

**Board Room:** That is an example of one.

**Board Room:** Okay, so the rip and replace is first of all.

**Ryan Singer:** Did you say rip and replace?

**Board Room:** Yeah.

**Ryan Singer:** It'S a good one.

**Board Room:** It's like no traffic is usually like a good indicator.

**Board Room:** First of all, no current traffic.

**Board Room:** But in the last 12 months, at some point there was traffic.

**Board Room:** Some URLs are some links, internal links and backlinks, not zero, you know?

**Ryan Singer:** Yeah.

**Board Room:** Huh.

**Board Room:** And.

**Board Room:** And then ideally is doing some work on understanding the intent of this page to see if it's like an opportunity we would have.

**Board Room:** Like, does this match like an opportunity that we would have surfaced as new if this URL didn't exist, you know, AKA like don't cannibalize.

**Board Room:** Like.

**Board Room:** And so this is more of like, in the example of like the Vercel one, it would be like Opus 4.5.

**Board Room:** The intent is you're looking for the stats on the model, like the details of it.

**Board Room:** You're looking for evals on it.

**Board Room:** You're like trying to understand blah, blah, like that's a legit intent.

**Board Room:** It's like a legit opportunity that should belong here in this page.

**Board Room:** Right.

**Board Room:** But this page is not doing that.

**Board Room:** So that was a little bit more fuzzy.

**Board Room:** Whereas like the leap one is no current traffic, like low to no linking internal or external.

**Board Room:** And there was never any sign of life, or there hasn't been a sign of life for more than a year or something?

**Board Room:** You know, this thing was never valuable at all.

**Ryan Singer:** Yep.

**Ryan Singer:** Huh.

**Ryan Singer:** What is, Is there.

**Ryan Singer:** Is there an example of intent match that you can actually do with the systems you have already with the info, with the knowledge you have?

**Ryan Singer:** Like, how would you.

**Board Room:** You.

**Ryan Singer:** How would you do that?

**Board Room:** Just looking at the URL and then looking at what is actually on the page, even if it's very, very, very little, tends to be like, okay, like that you can kind of understand.

**Board Room:** And then you can reverse engineer what searches related to this would be.

**Board Room:** And then look what at those pages that are live, that are actually ranking for what that would be, and it becomes really like a finite game of what that intent would have been.

**Board Room:** Right.

**Board Room:** Like, so the URL slug tends to tell you a lot.

**Board Room:** And if the URL slug is garbage, then most likely it's in the category of delete anyways.

**Board Room:** You know, like, it's Like a one word slug.

**Board Room:** You know, like.

**Ryan Singer:** Okay, so could I say some intent match from URL Slug.

**Board Room:** Yeah.

**Ryan Singer:** And this is something that you would do.

**Ryan Singer:** You couldn't do with.

**Ryan Singer:** With the AI as opposed to with a human.

**Board Room:** You could.

**Board Room:** Yeah.

**Board Room:** Actually, like, the more I'm thinking about this, I think we can put these two together.

**Board Room:** Rip and replace or archive.

**Board Room:** And it's mostly like the action you determine based on a human judgment, I think.

**Ryan Singer:** Yeah.

**Ryan Singer:** But here's the thing is, I think that if we come back to when we were looking at this.

**Board Room:** Yeah.

**Ryan Singer:** The, the number one question I had in my mind when I was playing user was what am I supposed to do?

**Ryan Singer:** So I think the action is actually kind of maybe the leading thing when it comes to identifying what these things are.

**Ryan Singer:** Do you know what I mean?

**Board Room:** Yeah, it's like fix, improve, refresh.

**Ryan Singer:** Right.

**Board Room:** And then this one is like, replace or archive.

**Board Room:** And.

**Ryan Singer:** So fix, refresh.

**Ryan Singer:** Refresh is a little.

**Ryan Singer:** Okay, we'll come back to that.

**Ryan Singer:** Replace.

**Board Room:** And I'll say replace it or archive.

**Board Room:** Because it's just kind of.

**Board Room:** It's like in the same mode.

**Board Room:** It's just like.

**Ryan Singer:** Yeah, but it's such a different.

**Ryan Singer:** But it's totally different work, isn't it?

**Board Room:** Any little human things that, that like, you can look at something and very quickly, like.

**Board Room:** Yeah, no brainer.

**Board Room:** Whereas, like, I think this is one of those where human judgment is the way easier than like one of the two buckets to put something under.

**Ryan Singer:** No, I get it, I get it.

**Ryan Singer:** Yeah, I get it.

**Ryan Singer:** So there's actually a different work step of decide versus.

**Board Room:** Yeah, yeah, exactly.

**Ryan Singer:** Right.

**Board Room:** Yeah, yeah.

**Board Room:** It's like, this is the queue of like, garbage can and you just decide if, like, you want to recycle or if you want to just like dump it.

**Board Room:** You know, it's like, come on.

**Board Room:** Yeah, yeah.

**Ryan Singer:** So this, this is it.

**Ryan Singer:** This is different work.

**Board Room:** Just call it like recycle or dump.

**Board Room:** Yeah, we should have some phone.

**Ryan Singer:** Yeah, totally.

**Ryan Singer:** Okay.

**Board Room:** And when you archive, we need to also decide if it's going to be a redirect or just.

**Board Room:** It almost always should be a wild card redirect or something, you know, because it's just like a good practice to have it.

**Ryan Singer:** Yeah, let's.

**Ryan Singer:** Let's take.

**Board Room:** Let's.

**Board Room:** And then it improve is the only one missing.

**Board Room:** Oh, yeah.

**Ryan Singer:** Let's.

**Ryan Singer:** Let's take it.

**Ryan Singer:** Let's.

**Ryan Singer:** Let's leave improve still and let's take another spin through the exact same material with this other question.

**Ryan Singer:** What's wrong?

**Ryan Singer:** Okay, so this is from the action lens.

**Ryan Singer:** Let's look at it from the, from the failure lens, you know.

**Board Room:** Yeah.

**Ryan Singer:** So like this was like a rule was broken.

**Board Room:** Yeah, Important rule was broken.

**Board Room:** Yeah.

**Ryan Singer:** This is stale, expired.

**Board Room:** Yeah.

**Board Room:** Yeah.

**Board Room:** This is decaying and losing engagement.

**Board Room:** Not effective.

**Board Room:** Yeah.

**Board Room:** This is like garbage.

**Ryan Singer:** Well, no, not yet.

**Ryan Singer:** Garbage.

**Ryan Singer:** This is garbage.

**Board Room:** I mean, it's garbage.

**Board Room:** It's just.

**Board Room:** Do you want to recycle or not?

**Ryan Singer:** Ah, okay.

**Board Room:** It's garbage no matter what.

**Board Room:** It's just a matter of like you want to reuse material.

**Ryan Singer:** Yeah.

**Ryan Singer:** Here's the thing.

**Ryan Singer:** Like, like, isn't there a sense when you find this that it's a little bit like you found like gold?

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Like it's garbage.

**Ryan Singer:** But like there's opportunity here because of the fact that it's like.

**Board Room:** That.

**Board Room:** The vercel one is kind of like that.

**Ryan Singer:** I mean the vercel one you showed.

**Board Room:** Me felt like it's just the vercel one is almost like the exception.

**Board Room:** Like what you end up with here is like founder, early stage, created some like blog at the beginning that had the right title and the bad execution on like home base or just like single paragraph product announcements.

**Board Room:** But the title was like an intent that was like, you know, very, very good.

**Board Room:** Like it's like what is blah blah, blah.

**Board Room:** But it was about a product announcement.

**Board Room:** It was like, what the hell?

**Board Room:** This doesn't match.

**Board Room:** Right.

**Board Room:** Like it's actually like pretty rare that you're gonna see.

**Board Room:** It's more rare that you're gonna find things like that.

**Board Room:** Or like the vercel one, which like an entire area of the site is the right area.

**Board Room:** It's just the execution of the content is, you know, to be improved.

**Board Room:** But then I see, you know, I see different, you know.

**Board Room:** Okay, yeah, this is more of like candidate for garbage, you know.

**Board Room:** And what's wrong is just like, it's just bad, you know?

**Board Room:** Yeah, it's like best case bad, worst case toxic, you know?

**Ryan Singer:** Uh huh.

**Ryan Singer:** Uh huh.

**Ryan Singer:** So this is like that is maybe.

**Board Room:** Even though it's like useless, let's just like call it useless, you know, which is very different.

**Board Room:** It's like, yeah, like legit.

**Board Room:** Like instead of bad, useless and then toxic.

**Board Room:** Like, whereas like toxic could be like this is a virus, you know, like.

**Ryan Singer:** Okay, so what's right?

**Board Room:** In what sense?

**Ryan Singer:** For each one of these, if I'm fixing it, something's right with it.

**Ryan Singer:** Right.

**Ryan Singer:** Otherwise, because I'm not throwing it away.

**Board Room:** Yeah, got it.

**Board Room:** Yeah, the like proof there's traffic and engagement and or there's visibility to it.

**Board Room:** There's Impressions and the.

**Board Room:** The opportunity.

**Board Room:** Yeah, there's potential.

**Board Room:** Except like the case.

**Board Room:** Yeah, there's potential.

**Board Room:** Yeah.

**Board Room:** A genuine judgment on potential.

**Board Room:** You know, there's like unrealized potential.

**Board Room:** Yeah.

**Ryan Singer:** What do you call.

**Board Room:** Because if there's like fulfilled potential, then there's nothing you should do.

**Board Room:** Right.

**Board Room:** Like, unrealized potential is like, hey, we think this could be realized even more even.

**Board Room:** Even in a measurable way.

**Board Room:** Right.

**Board Room:** For example, like when you're picking a topic in the opportunities area today, it's coming from research on keywords.

**Board Room:** They are getting search volume.

**Ryan Singer:** So that's.

**Ryan Singer:** Is that what potential means?

**Board Room:** Yes.

**Board Room:** Yeah.

**Board Room:** You voice the article somehow.

**Board Room:** Like, maybe the meta type is wrong, the content is wrong, it's not indexed.

**Board Room:** Then there's potential with zero.

**Board Room:** Yeah.

**Board Room:** Like there's potential for better quality content.

**Board Room:** There's potential for more impression and visibility, more citations, there's potential for more traffic, there's potential for deeper engagement and there's potential for higher conversion.

**Board Room:** Yeah.

**Board Room:** Depends.

**Board Room:** Yeah.

**Board Room:** Yeah.

**Ryan Singer:** Huh.

**Ryan Singer:** Okay.

**Board Room:** Is it.

**Ryan Singer:** Would it be.

**Ryan Singer:** Meaning that felt important, but I'm not sure if we're getting on a sidetrack.

**Ryan Singer:** Would it be meaningful to capture those different types of potential?

**Board Room:** Yeah, because they align to like our scores.

**Board Room:** Essentially.

**Board Room:** That's are on the page.

**Board Room:** Right.

**Board Room:** Like they are.

**Board Room:** They're all like aligned to it, you know?

**Ryan Singer:** So what are they?

**Ryan Singer:** What are the types of potential?

**Ryan Singer:** Again, just give those to me one more time.

**Board Room:** Potential for quality.

**Board Room:** There's AKA there's potential to improve the quality of the page.

**Board Room:** There's potential for impressions and there's potential for more traffic and there's potential for engagement and there's a potential for conversions or actions to.

**Ryan Singer:** Can you give me a quick, A quick lesson?

**Ryan Singer:** What's the difference between impressions and traffic?

**Board Room:** Yeah, like, like impressions, for example, are like when you search something on Google and a page is like the last one on the page and people don't scroll down, that's still an impression.

**Board Room:** Right.

**Ryan Singer:** I got it.

**Board Room:** Yeah.

**Board Room:** Okay.

**Ryan Singer:** Yep.

**Board Room:** And so like, we know that there's people searching for a certain keyword, but you're not even showing up because you're like on the fifth page.

**Board Room:** Right.

**Board Room:** On the first page you would get a ton of their pressure.

**Board Room:** Right.

**Board Room:** Whereas like, traffic is about, like the impressions give you a shot at traffic.

**Board Room:** Traffic is you hit like you convince someone to click.

**Board Room:** Right.

**Board Room:** You convince someone and do something.

**Board Room:** Right.

**Ryan Singer:** Yeah.

**Board Room:** Go through with it.

**Board Room:** And so one is about like positioning correctly and a bunch of other factors.

**Board Room:** The other one is about, like selling them on the promise.

**Board Room:** And then engagement is Delivering or over delivering on the promise of what you.

**Board Room:** And the promise is your headline and your description, right?

**Ryan Singer:** Yep.

**Board Room:** And so, so, and then hopefully your promise matches the intent of the user.

**Board Room:** And when you over deliver on that promise, it's like, whoa, I'm here.

**Board Room:** This is amazing.

**Board Room:** I'm going to, I'm clicking through, I'm spending a bunch of time.

**Board Room:** And then conversion is like, holy.

**Board Room:** You built so much credibility and you deliver so much value.

**Board Room:** I want more, I want to go deeper.

**Board Room:** I want to talk to you.

**Ryan Singer:** Yep.

**Ryan Singer:** Coming, coming back to let's say, kind of instrumenting opportunities for optimization.

**Ryan Singer:** Are there things here that are, that are you expect to be measuring and populating in the learn and learn and improve section?

**Board Room:** Yes.

**Board Room:** So quality is around alignment.

**Board Room:** And the same thing with like the improve area, by the way, is around alignment.

**Board Room:** Right.

**Board Room:** Like, so think of alignment as like you have a grounding document or grounding truth and it's about like how much like this deviates from that truth.

**Board Room:** Right.

**Board Room:** And where does it deviate?

**Board Room:** And, and so for instance, like there's a company description.

**Board Room:** Well, is this thing aligned to that company description?

**Board Room:** There is a writing guideline.

**Board Room:** Is this aligned to that writing guideline?

**Board Room:** Right.

**Board Room:** Like, so think of it as like rounding evals, almost like, I don't know if that's even a term, but it's like, yeah, yeah.

**Board Room:** But then there's like, there's like an opportunity grounding of like, this is the opportunity.

**Board Room:** This is the intent of what we're trying to do.

**Board Room:** This is the brief, this is, is the research.

**Board Room:** So there's like research grounding, you know, and alignment.

**Board Room:** There's like opportunity and intent alignment.

**Board Room:** And then there's like the company product Persona and guidelines alignment, which is like your context files, if you will.

**Board Room:** Right?

**Ryan Singer:** Yeah.

**Board Room:** And so it's like, it's like a drift, right?

**Board Room:** And then a drift can happen, you know, because of like context poisoning or you know, over compressing or, you know, or like missing a point or it, you know, so some, some version is.

**Ryan Singer:** That this, is this, is this misalignment?

**Board Room:** So improve is misalignment that needs to be realigned because there's a need for like, there's a reason the alignment is there.

**Board Room:** Right.

**Board Room:** And then.

**Board Room:** Okay, hold on.

**Board Room:** Sorry.

**Ryan Singer:** Okay.

**Ryan Singer:** All right.

**Board Room:** Yeah, like, and, and hopefully like over time, like we're building these kind of like best practices and evals based on studies and a lot of data we're collecting across a lot of customers so that like we can make more recommendations on the kinds of misalignments that, that we should do.

**Board Room:** Like, you know, the quality one has like so much potential for a very unique ip.

**Board Room:** Yeah.

**Board Room:** And just so very subjective and a hard problem.

**Board Room:** One quick thing on, on kind of how like check that I'm going like, it's almost like I did a bunch of research on how analysts thinks about it and users and peer reviews and things like that.

**Board Room:** And there's kind of like these attributes, if you will.

**Board Room:** Right.

**Board Room:** Like, and this is.

**Board Room:** And I'll connect doc here in a second.

**Board Room:** But it's like usability, capability, usability, value, trust, support, innovation.

**Board Room:** So over time that's for like brand perception.

**Board Room:** Right.

**Board Room:** And how AI engines think of that.

**Board Room:** And whereas like for here there can be attributes that kind of like matter to them.

**Board Room:** Right.

**Board Room:** If you will, at the content level, you know, and those attributes are you know, personalized based on the context of the company.

**Board Room:** But then there's also like global things as well.

**Board Room:** Right.

**Board Room:** That are like for instance, like the, like the attribution, you know, better attribution or more examples or you know, but there's like having images or things like that like are actually like enrichment things.

**Board Room:** Right.

**Board Room:** That, that we know are like well known patterns.

**Board Room:** Create a rubric.

**Board Room:** Yeah.

**Board Room:** But then there's also Ryan, like the things we're going to learn about them, right.

**Board Room:** And their baseline, right.

**Board Room:** Like so, so for instance, like if you have 10,000 pages and you look at only your blog pages and within those blog pages you understand the type of content it is and you have all this data on it, right.

**Board Room:** Like you can then figure out, hey, for pages that have higher engagement and a higher percentage or propensity for people to go to the bottom of the page and click through to the next page.

**Board Room:** These are the patterns we learned from it.

**Board Room:** And then those are the patterns that then you can suggest improvements to the other ones.

**Board Room:** And so think of it as like this is the baseline.

**Board Room:** These are like your top performers in any metric and these are like your low bottom performers.

**Board Room:** And you learn from what patterns can be reproduced here so that these can be higher to here so that your baseline increases.

**Board Room:** Does that make sense?

**Board Room:** Got it.

**Ryan Singer:** Yeah, that makes sense.

**Ryan Singer:** I think.

**Board Room:** Sorry.

**Ryan Singer:** It'S all like interesting.

**Ryan Singer:** And so in the scope of what we're trying to solve right now, we're trying to figure out kind of how to present opportun these as work items.

**Ryan Singer:** And so let's, let's just call quality quality for the moment.

**Ryan Singer:** And I just want to see if we can kind of, if we can just kind of maybe spell out how to measure these things, we might get to a point where I think we have like a pretty solid picture of like what we might be looking at, what we might be surfacing, what the action is and so on.

**Ryan Singer:** And then this could be an input for us to then look at, you know, look at solution ideas.

**Board Room:** I think Quality.

**Board Room:** Right.

**Board Room:** You can even spell out as like score on the rubric of traits that we can.

**Board Room:** Yeah.

**Board Room:** Every page is going to have a quality score and that quality score is going to be.

**Ryan Singer:** That's actually this a trend line.

**Board Room:** Yes.

**Board Room:** And so just think of it as just like the quality dropped or the quality has been low for a long time.

**Board Room:** Always has been low.

**Board Room:** And so like, as far as this is concerned, we almost don't even need to think about the rules.

**Board Room:** And that's why I'm trying to create these composite scores everywhere, because otherwise super defined rules everywhere, you know?

**Ryan Singer:** Yeah.

**Ryan Singer:** I think, I think it's just good to know that like, if.

**Ryan Singer:** If something has been flagged as improve because of a quality issue, you know, is that what this is?

**Board Room:** Yeah.

**Board Room:** Like low quality score or a big dip.

**Board Room:** Yeah.

**Board Room:** You know?

**Ryan Singer:** Yeah.

**Board Room:** So.

**Board Room:** And then don't worry about it.

**Board Room:** This is going to be determined by the scoring.

**Ryan Singer:** Yeah.

**Ryan Singer:** Yep.

**Ryan Singer:** But then we just, if, if we're getting into the work step of an improvement, then we're just going to want to know that we have the ability to unpack what that particular score means so that we know what to actually do as an action.

**Ryan Singer:** Good.

**Ryan Singer:** Okay.

**Ryan Singer:** I'm guessing the rest of these are easier.

**Board Room:** Even if it's not a human doing the improvement for the quality, it still has to.

**Board Room:** We have to unpack even more.

**Ryan Singer:** Oh yeah, totally.

**Ryan Singer:** Yeah, totally.

**Ryan Singer:** Huh.

**Ryan Singer:** Okay.

**Ryan Singer:** Are these worth spelling out or do we just want to take it for granted that like those are very measurable?

**Board Room:** I think the only one that the engagement and conversions are probably like coming soon.

**Ryan Singer:** I think.

**Board Room:** I think it is worth, like even didn't like, I think I can guess.

**Board Room:** But our team didn't understand that impressions, low impressions equals shitty meta tags, for example, you know, uncheck that.

**Board Room:** Yeah.

**Board Room:** Like, let me just show a quick example because this is.

**Board Room:** So there's a set of things that are related to impressions, a set of things that related to traffic.

**Board Room:** Right.

**Board Room:** This is for a page on cursor pricing.

**Board Room:** Okay.

**Board Room:** Let's just check that for.

**Board Room:** Check that.

**Board Room:** So we have thousands of.

**Board Room:** And you can see like it went.

**Board Room:** And we got like clicks and impressions and then it pretty much went to zero.

**Ryan Singer:** Yeah.

**Board Room:** Right.

**Board Room:** So this is what we're trying to flag.

**Board Room:** Like we.

**Board Room:** Like someone caught this manually somehow.

**Board Room:** But.

**Board Room:** But like it's highly unlikely in the sea of shit and, and signals that someone would catch this.

**Board Room:** And had we not acted, this wouldn't have happened.

**Ryan Singer:** Totally, totally.

**Ryan Singer:** Back on the whiteboard here.

**Ryan Singer:** I'm actually pasting that.

**Ryan Singer:** I'm just dropping this in.

**Ryan Singer:** What is this in terms of this?

**Board Room:** This is a.

**Board Room:** There was a rise in impressions and then a rising clicks, which is traffic.

**Board Room:** Right.

**Board Room:** Followed by a dip in both.

**Board Room:** So when, when clicks drop but impressions don't, that means your promise is off.

**Board Room:** Like you're.

**Board Room:** No one's clicking on your ad.

**Board Room:** Right?

**Board Room:** Yeah, like when, when impressions and clicks drop, then it's usually like the signal is bad.

**Board Room:** Like.

**Board Room:** Like they came in your contest pile of garbage.

**Board Room:** Right.

**Board Room:** And that usually the.

**Board Room:** The leading indicator of that.

**Board Room:** Because that's lagging.

**Board Room:** Right.

**Board Room:** You're already fucked.

**Board Room:** It's already went to zero.

**Board Room:** Right.

**Board Room:** The leading indicator of that is like the day that thing spiked the first time you could have seen the engagement.

**Board Room:** And the bounce rate, like time on page bounce rate.

**Board Room:** How many of the visitors that landed, AKA enter the site through this page ended up doing more things.

**Board Room:** Right.

**Board Room:** And was the average session time compared to everything else?

**Board Room:** Right.

**Board Room:** Specifically for this channel, AKA like SEO in organic.

**Board Room:** And if it was like way lower than anything else, like lookalikes, similar type of page or overall baseline for the site, then it's telling me the content was bad essentially.

**Board Room:** Like it wasn't good.

**Board Room:** Right.

**Board Room:** And so had we addressed that at that spike, there's a likelihood that we would be even higher now.

**Board Room:** Right.

**Board Room:** But it's.

**Board Room:** No, it's better to address it fast like we did.

**Board Room:** But it's like it wasn't that fast.

**Board Room:** It was like a week later.

**Board Room:** That was also manual.

**Board Room:** So everything there was check that has 10,000 pages.

**Board Room:** We're struck in gold in some places, like anthropic one of the pages, cursor pricing and people are not catching.

**Board Room:** So.

**Ryan Singer:** This should be surfacing and learn and improve.

**Board Room:** Yes, yes, it should.

**Ryan Singer:** Okay, so what I think is, I think that we've gone warmer with this kind of.

**Ryan Singer:** I think we shared a lot of domain knowledge with what we did here.

**Board Room:** Yeah.

**Ryan Singer:** But I want to make sure is that we don't think that we've solved it when like this kind of thing is the real problem.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Like this is like a real case.

**Ryan Singer:** So I want to check like, does this actually map to what we talked about?

**Ryan Singer:** And is all this like general stuff, like real or is it more complicated than that?

**Ryan Singer:** In reality.

**Board Room:** Sorry, it's called a little fire drill.

**Board Room:** My.

**Board Room:** My EA accidentally share comp information on a public or like an executive that we're hiring.

**Board Room:** Like, what the.

**Board Room:** What the hell?

**Board Room:** Sorry.

**Ryan Singer:** Brutal.

**Board Room:** Can you repeat that?

**Board Room:** I apologize.

**Ryan Singer:** Okay, so the thing is, okay, so briefly, what happened was like, we.

**Ryan Singer:** We've been kind of sketching it, like, sketching out a lot of what's in your head, Marcel, around what optimization means.

**Board Room:** Right.

**Ryan Singer:** And my concern is we might not have gone deep enough.

**Ryan Singer:** And what I want to do is I want to use this as a test case of like, this is a real kind of thing that we want to be able to surface, right?

**Ryan Singer:** So I think what we want to be able to say is, like, what is this?

**Board Room:** Right?

**Ryan Singer:** And then this is the kind of like, concreteness of specific cases of like, this is the kind of thing we should be surfacing in terms of detection and action.

**Board Room:** Yeah.

**Board Room:** Like there.

**Board Room:** Okay, so if you look.

**Board Room:** If you think back of like what Daniel was showing on the filters and things like that, right?

**Ryan Singer:** Yep.

**Board Room:** Normally it's like you do a bunch of stuff, you publish a bunch of pages or whatever when you're actively doing it, like what we're doing, and check that, like, there would be signals, right?

**Board Room:** And those signals will tell you we did something.

**Board Room:** Right?

**Board Room:** And usually those signals would be like, oh, look, this got indexed.

**Board Room:** That's good.

**Board Room:** Like, you know, and then it was like, followed by, whoa, this got some impressions.

**Board Room:** Index is not even bad impressions.

**Board Room:** It's just got indexed.

**Board Room:** Yeah, yeah.

**Board Room:** And then like, okay, so this thing got impressions, but it's not getting clicks now all of a sudden, right?

**Board Room:** So now it's like, okay, if you do nothing, let's just say there's one page, that page is getting impressions consistently and no clicks.

**Board Room:** There are many pages on Google Search Console, Ryan, that they will not gonna have the purple.

**Board Room:** Like, you see the impressions.

**Board Room:** Shit ton of impressions and zero clicks, you know?

**Ryan Singer:** Yeah.

**Board Room:** That's about a concrete example.

**Board Room:** So, so.

**Board Room:** So then you're like, look, we got impressions.

**Board Room:** That means probably we got the opportunity, right?

**Board Room:** And we got the intent somewhat right.

**Board Room:** But it either means like the.

**Board Room:** The headline or, you know, the.

**Board Room:** The.

**Board Room:** The promise of the page is still off from the intent that we're getting.

**Board Room:** It also means, like, there.

**Board Room:** It could also mean that you just need to do something a little bit more to drive the like, average position a little bit higher.

**Board Room:** Right?

**Board Room:** Like, and so then it's like, truly, you know, like, hey, we need to link to it a little bit more.

**Board Room:** You need to like, try to Get a little bit higher because sometimes you're getting a click.

**Board Room:** This is truly like a garbage search.

**Board Room:** And it's like positioned solo on the page.

**Board Room:** No one's seeing it, right?

**Board Room:** Like an impression doesn't mean somebody actually saw it, right?

**Board Room:** And the thing within your control is like, go optimize the meta title, headline, meta description, things like that, and see if it improves, right?

**Board Room:** See if you actually get some clicks, you know, if not, wait a little longer and if you see nothing, then try like some other optimizations.

**Board Room:** Normally my hack here is like link to it and try to like force it to.

**Board Room:** For Google to think this is really important to try to force Google to like rank you a little bit higher to see if you get clicks, right?

**Board Room:** But I usually do the headline first and that's second, right?

**Board Room:** And this is just like one, one page.

**Board Room:** Then let's say you start to get clicks.

**Board Room:** The second you get clicks, it's like now all of a sudden you're in like watch mode, right?

**Board Room:** And you're ideally, if you only had one page on your site and that's the only page you care about, like, you're just like watching it like a hawk, right?

**Board Room:** And the second you get clicks, you're like, is this like, are people like spending time on this?

**Board Room:** Are they.

**Board Room:** Is the bounce higher?

**Board Room:** Right?

**Board Room:** Best case scenario is like, can I just like record the fucking session and see what happened?

**Board Room:** Right?

**Board Room:** And those signals are like the most.

**Board Room:** It's like your first impressions to Google on this page, right?

**Board Room:** They're like super, super, super, super important.

**Board Room:** And you want to watch it like a hawk.

**Board Room:** And then very, very, very, very quickly respond to it.

**Board Room:** And, and the response to it is either, holy crap, like people are spending three minutes on this and it's three times higher than every other page on the site.

**Board Room:** We did something right, hey, let's go try to do this again in other places.

**Board Room:** Or hey, we read this and this is pretty shallow.

**Board Room:** We should rethink this content completely, which is what we did with Cursor.

**Board Room:** But it's very subjective because for instance, the same pipeline that generated this cursor page also generated this HeyGen page.

**Board Room:** And, and the hey, gen page never had a dip in.

**Board Room:** And so like, if you look at this, it's like this page never had a dip, you know?

**Board Room:** And so you're like, okay, this is like the same pipeline, you know?

**Board Room:** And it's just like a audience for Cursor.

**Board Room:** You know, Anecdotally I think it's because an audience for agent, like, it's kind of like lower.

**Board Room:** It's just like random consumers kind of thing.

**Board Room:** Whereas cursor is like, highly sophisticated.

**Board Room:** Like people that are doing really deep research.

**Board Room:** Research and care a lot about the details, how it's presented and whatnot.

**Board Room:** Whereas, like, agents, like, a little bit more, like, generic.

**Board Room:** Like, you know, that's my hypothesis.

**Board Room:** Just like the audience.

**Board Room:** Right.

**Board Room:** One audience is, like, more technical than the other and cares more about services, you know, like.

**Board Room:** But you can see, like, you know, like finding the Pretty.

**Board Room:** Pretty hard at scale.

**Ryan Singer:** Yeah.

**Board Room:** Okay.

**Board Room:** Yeah.

**Ryan Singer:** We'Ve.

**Ryan Singer:** I'm looking at where we're at with time.

**Ryan Singer:** Let's.

**Ryan Singer:** Let's take five.

**Board Room:** Yeah.

**Board Room:** Is.

**Ryan Singer:** Is.

**Ryan Singer:** Is five enough or do you guys need 10 works?

**Board Room:** Five work?

**Board Room:** Yeah.

**Ryan Singer:** Okay, let's do five and we'll see in five.

**Board Room:** This is such a complex domain.

**Board Room:** Yeah.

**Board Room:** There's so much things back into every corner of the.

**Board Room:** There's so much loading through.

**Board Room:** You're almost in the first stage.

**Board Room:** What's going on?

**Board Room:** It.

**Board Room:** That's.

**Board Room:** Yeah, Just Open Office was like one of the crane.

**Board Room:** Look, I love.

**Board Room:** Yeah, I like how they name the room.

**Board Room:** Was it happening?

**Board Room:** You know, it's like when you're like, a couple of set functions away from, like, cracking it.

**Board Room:** Imagine that, like, Brian doing this and having to do, like, interviews with users in order to get to this truth.

**Ryan Singer:** Oh, man.

**Board Room:** You know, that's why we have so much confidence in what we're doing, because it's just like, so many years of, like, doing this for so many different companies that are all successful, you know?

**Board Room:** And like, that's what's fun about this.

**Ryan Singer:** Project is it's like, it's.

**Ryan Singer:** I feel like it's all about, like, how do we.

**Ryan Singer:** How do we, like, funnel all this stuff that you already know into this product?

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** It's not like the head scratching of how does it work.

**Ryan Singer:** It's like, we know how this works.

**Ryan Singer:** How the heck do we, like, get.

**Board Room:** It in here, you know, like, simplify it and give, like, customers, like the end user, like, a sense of control versus, like, there's things where truly, like, we don't kind of need their opinion.

**Board Room:** And then there's like, little nuanced things like what you were saying, like, should you archive this or should you, like, repurpose?

**Board Room:** Like, it would probably be a gnarly agent, but then a human judgment is actually decently easier here, you know?

**Board Room:** Like, it's kind of like this weird thing about AI sometimes there's things that are like, agents are 100 times better on really hard to do.

**Board Room:** Complex things, like snapshots.

**Board Room:** And then like on the simplest thing, it's just like, no, no, just have a human review.

**Board Room:** It's like.

**Board Room:** It'll take 10 seconds.

**Board Room:** Like, don't worry.

**Board Room:** Totally, totally.

**Board Room:** This is very counter, you know, so.

**Ryan Singer:** Okay, so what I want to do is I want to step back and.

**Ryan Singer:** Because I feel like we could just kind of talk about optimization as a science all day, you know, And I want to.

**Ryan Singer:** What I want to do is I want to bring this kind of back to you, Daniel.

**Ryan Singer:** Around kind of.

**Ryan Singer:** Where's the question?

**Ryan Singer:** So my understanding was that like.

**Ryan Singer:** Like we moved the pipeline for creation out of Learn and improve, and now there's like a missing piece, which is like the pipeline piece is kind of missing there.

**Ryan Singer:** And I'm wondering, like, do we want to take all this kind of shared context that we built up now and do we want to look at what is that pipeline of work inside of Learn and improve, or is it a different question?

**Board Room:** I think that would be an interesting experiment because.

**Board Room:** There are tools in the market that try to do the included part and they're definitely better than nothing.

**Board Room:** And they've done really well financially, everything, because it's a real hard problem and the bar is so low.

**Board Room:** Like what Marcel is driving, that is the whole holy grail of like organic content, like tracking everything, knowing where things are getting traffic.

**Board Room:** None of the tools do that.

**Board Room:** They just do at the page level.

**Board Room:** The most basic things, just like fix your broken links, fix your.

**Board Room:** Your headings.

**Board Room:** That alone is valuable.

**Board Room:** The closer we can get to the stuff that Marcel is describing.

**Board Room:** Yeah, that is mind blowing for what the public is used to, you know.

**Ryan Singer:** Oh, it's huge.

**Ryan Singer:** You know, it's totally huge.

**Board Room:** An example here, really quick.

**Board Room:** And I think that place where we have in the system today, if the learning improve, if the create is out of it, and that's a different problem.

**Board Room:** And we can crack that if there is a path to make that concrete in that same user interface with the same simplicity of the separation that we have now.

**Board Room:** I think we're really close to something that's way better than server SEO, for example, that is closer to achieving what Marcel is.

**Board Room:** The pipeline there can work.

**Board Room:** It's worth trying.

**Board Room:** Yeah.

**Board Room:** And just so you understand how relevant this is right now, Ramp is a customer and then Brex is a customer, and then we just kicked off, or we're kicking off today with Spendesk, which is like a European version of it.

**Board Room:** Right.

**Board Room:** And essentially, like, this is what we're dealing with.

**Board Room:** Like, like their traffic is like in Free Fall.

**Board Room:** And they hired us essentially, and a highly competitive space, right?

**Ryan Singer:** And.

**Board Room:** And like, we did all this manually.

**Board Room:** Like, everything you see here is just like, like manually done to try to like, give them, like, what you go focus on.

**Board Room:** It's all based on new opportunities.

**Board Room:** And I was like, guys, what the.

**Board Room:** What the f. Like, they have 700 pages.

**Board Room:** Like, you know, and so you go here and you go like, hey, like, like this is.

**Board Room:** It's.

**Board Room:** It's in the climb.

**Board Room:** It's in like free fall.

**Ryan Singer:** And.

**Board Room:** And like, how do you know what to do here?

**Board Room:** There's 712 of them, right?

**Board Room:** Like, all these are dropping.

**Board Room:** Which one should you focus on?

**Board Room:** And why.

**Board Room:** Why is this.

**Board Room:** Yeah, is that a good thing or bad thing?

**Board Room:** It's like.

**Board Room:** Or, you know, is that like even just the realization of that you have 700 pages?

**Board Room:** You shouldn't be thinking too much about creating your pages.

**Board Room:** Just go fix that.

**Board Room:** Having the place in the app that tells you that that is also something that even our team isn't thinking about it.

**Board Room:** And our team is really good compared to the rest of the market.

**Board Room:** So then what people will do here, Right, Exactly.

**Board Room:** They'll come here and they'll just hit export on this, and this is all the data you have, and then they'll do an analysis completely absent of the context of the company.

**Board Room:** And anything else just looks at this, right?

**Board Room:** And all you have is a URL and it has no context of anything else.

**Board Room:** No signals or anything else.

**Board Room:** And it's just like, fuck, this is so bad.

**Board Room:** And this is literally what our team does too.

**Board Room:** And what I've had to do, right?

**Board Room:** There's nothing else.

**Board Room:** And so then the next best thing I would do is I would build a scraper to go through each URL and do a summary of the content of the URL, and then build all these play tables or processes or whatever.

**Board Room:** But then those didn't have GA data, right?

**Board Room:** Or GSC data.

**Board Room:** It was just this data.

**Board Room:** So anyways, like, it's just truly a pain point.

**Ryan Singer:** Oh my God.

**Ryan Singer:** My, my.

**Ryan Singer:** Like, my eyes are watering.

**Ryan Singer:** There's so much opportunity here.

**Ryan Singer:** Like, I can't handle it.

**Board Room:** It is like every site on the planet is dealing with this and there is no good solution in this.

**Board Room:** Like, like, this is like, I have so much conviction in this, man.

**Ryan Singer:** Okay, yeah, like, I'm.

**Ryan Singer:** I'm like, I'm a million percent with you on the conviction.

**Ryan Singer:** Okay, so here's the question.

**Ryan Singer:** What are we trying to solve for March?

**Board Room:** Low hanging fruit.

**Board Room:** Urgent.

**Board Room:** Like, do this or you're like improvement metrics based, right?

**Board Room:** Like metric space.

**Ryan Singer:** Okay.

**Board Room:** Or like this is bad, right?

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Board Room:** So for instance, like if your biggest traffic driver just dipped, you should just drop everything you're doing.

**Board Room:** This is a P0 critical bug.

**Board Room:** Go fucking fix it.

**Board Room:** Right.

**Board Room:** And we should publish nothing until like we figure out what just happened there with our.

**Board Room:** One of our biggest customers augment code that happened to two of our biggest traffic diver.

**Board Room:** We didn't catch it for four weeks and then we didn't fix it for another four.

**Board Room:** And it really cost us like a lot.

**Board Room:** Yeah, essentially.

**Ryan Singer:** So what.

**Ryan Singer:** What else?

**Ryan Singer:** Like literally, like what's the list of things where it's like, we can do that for march?

**Ryan Singer:** Those are the things that we can catch that you absolutely should be catching.

**Board Room:** I think like the, the fixed stuff is just super no brainer because it's just very like rules based and we can start with a few rules and then build more rules and the refresh is truly just expired label on it.

**Board Room:** And then the improve is based on those like those filters that Daniel already built, which is like almost to the first page.

**Board Room:** You know, traffic dipped, impressions dip like, like again, it's like very rules based.

**Board Room:** But metrics, your biggest.

**Ryan Singer:** Your biggest traffic page just dipped.

**Ryan Singer:** Is that included in that?

**Board Room:** Yeah, yeah, that.

**Ryan Singer:** It's.

**Board Room:** It's just like, like improve is.

**Board Room:** Is like the dude.

**Ryan Singer:** So give me the top three.

**Ryan Singer:** Give me the top three smart filters for improve that like are real.

**Ryan Singer:** For.

**Ryan Singer:** For March, your.

**Board Room:** Traffic just dip.

**Board Room:** Your engagement.

**Board Room:** It is just dipped for as.

**Board Room:** Because that's like a leading indicator of everything else that's gonna happen soon, you know, and impressions, no clicks or you drop average rank or you're almost in the first page, which is kind of like all similar actions, which is just like you're almost there, you know, like, it's like you.

**Board Room:** But you didn't quite get the signals you needed to make it to the next.

**Ryan Singer:** Okay.

**Board Room:** You know.

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

**Board Room:** Let me grab a critical thing.

**Ryan Singer:** Let me say like possible states per page.

**Ryan Singer:** Okay.

**Ryan Singer:** Possible diagnoses per page.

**Ryan Singer:** I'm going to paste these.

**Board Room:** Your.

**Ryan Singer:** Your biggest traffic page.

**Ryan Singer:** This is.

**Ryan Singer:** This is a, A big traffic page that dipped.

**Board Room:** Yeah.

**Ryan Singer:** Engagement dip died impressions, but no clicks.

**Ryan Singer:** You're almost there.

**Ryan Singer:** Then here was.

**Ryan Singer:** I'm going to say rule broken.

**Board Room:** Yeah.

**Ryan Singer:** And expired, out of date, past good, whatever, you know.

**Board Room:** Yeah.

**Board Room:** It's like, think of it as like, some of these are preventive and some of these are like, you're.

**Board Room:** You're already sick.

**Board Room:** Like, now you gotta go, you know, it's like some of these are like, you know.

**Board Room:** Yeah, yeah.

**Ryan Singer:** But severity.

**Board Room:** Yeah.

**Ryan Singer:** What.

**Ryan Singer:** What's the severity?

**Board Room:** So any.

**Board Room:** Anything that is not preventive, it's going to be pretty high.

**Ryan Singer:** But.

**Board Room:** And then the.

**Board Room:** The further it is on, like, you know, if we had conversion pixels already, it would be like, conversion is the highest, you know, engagement is the second.

**Board Room:** Because you already got people through the site.

**Board Room:** You know how many things have to happen for them to get to the fucking site?

**Board Room:** Like so much.

**Board Room:** Right.

**Board Room:** Like, and then you just like, fuck that up.

**Board Room:** Right?

**Board Room:** And then like, traffic dip is like, oh, bro.

**Board Room:** Like, if you don't get traffic, there's no chance you're ever gonna get conversions.

**Board Room:** You know, Impressions like, dude, the first one is like a high alert, high severity.

**Board Room:** Yeah.

**Board Room:** That is like the secret.

**Board Room:** You did nothing, but you just keep improving your biggest traffic drivers.

**Ryan Singer:** Yeah.

**Board Room:** What I was saying is like, if we had conversion, it would be the highest thing.

**Board Room:** Oh, yeah, okay.

**Ryan Singer:** Like, because it's like there might be.

**Board Room:** A broken link to your cta.

**Ryan Singer:** Go.

**Ryan Singer:** Fucking given.

**Ryan Singer:** Yeah.

**Ryan Singer:** But given what we have, because we're in the March conversation of these, just how could we flag these as, like, let's say, let's say like severe or like worth looking at because maybe you can pick up something, you know what I mean?

**Ryan Singer:** Versus, like when you have time.

**Board Room:** Yeah.

**Board Room:** It's like the first one is important energy.

**Board Room:** The second one is important and will be urgent if you don't do anything about it.

**Board Room:** This is like the.

**Board Room:** And then the.

**Board Room:** The rest is like, like.

**Ryan Singer:** Is it more.

**Ryan Singer:** Are the rest more, like opportunities?

**Ryan Singer:** But rule broken is.

**Ryan Singer:** Is.

**Board Room:** Rule broken is a big deal.

**Board Room:** Yeah.

**Board Room:** Yeah.

**Ryan Singer:** Sorry.

**Board Room:** Rules broken is important if it's a high impact page, but if it's like a dead in the water page, who gives a.

**Board Room:** Like, don't go.

**Ryan Singer:** Okay.

**Board Room:** Not fix the first one, right?

**Board Room:** Yes.

**Board Room:** Or don't do optimization on pages are almost there.

**Board Room:** Because you're trying to fix a thing that has dead in the water.

**Ryan Singer:** And so let me.

**Ryan Singer:** Let me rename this fix.

**Ryan Singer:** High impact are high impact rule broken.

**Board Room:** Yeah.

**Board Room:** Yep.

**Ryan Singer:** Needs fix.

**Board Room:** Yeah.

**Ryan Singer:** Can we expire?

**Board Room:** It's just like, who cares?

**Board Room:** Like, like everybody, one of our customers has 10,000 pages.

**Board Room:** Like, who cares?

**Board Room:** They have like so much signal.

**Board Room:** There is almost like a modifier Here, if it's a high impact page, almost everything bumps the priority.

**Board Room:** Yeah.

**Ryan Singer:** Do we already have the ability today to say which page is high impact and which page isn't?

**Board Room:** This is based on traffic right now.

**Board Room:** That's what we're working right now.

**Board Room:** So, like, this, all the UI that we have with the metrics and everything will enable us to do that.

**Ryan Singer:** Right.

**Ryan Singer:** But where are we for March?

**Ryan Singer:** Like, what, what of this can we actually translate into?

**Ryan Singer:** Like, this is data we have in some.

**Ryan Singer:** Some version of this where we could actually.

**Ryan Singer:** Here's what I'm picturing.

**Ryan Singer:** I want to have.

**Board Room:** Yeah, yeah.

**Ryan Singer:** So high impact.

**Ryan Singer:** Just.

**Ryan Singer:** Just translate this then make this more concrete.

**Ryan Singer:** This is, this is like, well trafficked.

**Ryan Singer:** Like, what is this?

**Board Room:** Yeah, let's just assume everything is high traffic.

**Board Room:** Yeah.

**Board Room:** Fully engaged.

**Board Room:** And the thing is, like, Ryan, like, right now it's going to be high traffic, but in the future it's like high traffic.

**Board Room:** And with the qualifier of like, the intent of the page.

**Board Room:** Right.

**Board Room:** Like, so high traffic to like, what is a CFO versus a CEO do is like low intent traffic.

**Ryan Singer:** Yes.

**Board Room:** Which I have, like, high volume.

**Board Room:** So high volume, low intent.

**Board Room:** Whereas like, a high volume, high intent is like, like at the highest.

**Board Room:** Right.

**Board Room:** Like, but, but that's like.

**Board Room:** Because that is where.

**Board Room:** Because I don't think we're tracking that.

**Board Room:** And it's easy to track, actually.

**Board Room:** Yeah, it's like, it's like.

**Board Room:** So there's a few things, like we.

**Board Room:** For opportunities, we track intent.

**Board Room:** Yeah, I think.

**Board Room:** And then we track relevance.

**Board Room:** But then for pages, we're literally writing the page analysis this week, so I want to make sure I don't forget.

**Ryan Singer:** Yeah.

**Ryan Singer:** So for new page opportunities, high volume, high intent is a thing because you're tracking intent for new page opportunities.

**Ryan Singer:** But here in optimization, we have.

**Board Room:** Okay, so we can still figure out the intent on the existing pages because we're going to analyze the existing pages too, the semantics of it.

**Board Room:** So that works.

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Board Room:** I think I would have everything.

**Board Room:** The only thing we don't have, I guess, expired.

**Board Room:** We could have to, by the way, just to note relevance is really important.

**Board Room:** There's a lot of sites, like Deep ram, for example, where there's like, a lot of, like, pages are just not that relevant.

**Board Room:** And they were there for more, like, traffic boosts.

**Board Room:** You know, they're just like, not relevant to your audience at all.

**Board Room:** Yeah, like the low relevance, you know, so relevance fits into high intent.

**Board Room:** Right.

**Board Room:** They're just.

**Ryan Singer:** Okay, let me, let me, let me, let me try and, Let me try and simplify this.

**Ryan Singer:** Let's boil this down.

**Ryan Singer:** Assuming, let's take, let's say there's a first cut, right.

**Ryan Singer:** Of pages that are high traffic or were or were recently.

**Ryan Singer:** Right.

**Ryan Singer:** Like high traffic now or recently high relevance.

**Board Room:** Is.

**Ryan Singer:** Is relevance different than intent?

**Board Room:** Yeah.

**Board Room:** So for instance, with Lovable, we have a alternatives, right.

**Board Room:** Or a comparison page where it's just like Zapier versus make and that's us trying to grab that traffic.

**Board Room:** That traffic is high intent and high relevance to Zapier, if that was on Zapier's page.

**Board Room:** To Lovable, it's like a high intent type of query.

**Board Room:** But it's like low relevance or lower relevance because it's just like we're trying to go after people searching on comparisons of two apps, hoping that they eventually will connect the DOT to.

**Board Room:** I should just fucking build this myself because it's AI and I can just buy code of, you know, okay, our.

**Ryan Singer:** Relevance in different things that you.

**Board Room:** Versus Lovable.

**Board Room:** That's high intent, high relevance and high importance because it's our third biggest traffic driver on the site.

**Board Room:** So that would be like the whole grill.

**Ryan Singer:** Which, which of these do you.

**Ryan Singer:** Do you have these things already today that you could report per page?

**Ryan Singer:** Or is this a future.

**Board Room:** But we can run that page.

**Board Room:** We're building that for pages.

**Board Room:** And this is part of the milestone UI that I showed you from UP includes scraping your entire website and analyzing everything.

**Board Room:** So we're going to.

**Ryan Singer:** Okay.

**Ryan Singer:** Okay.

**Board Room:** The first follow for any optimization will have access to the space.

**Board Room:** It's mostly taking the workflow that's the post processing, but the crawler is right there.

**Ryan Singer:** So here's a question.

**Ryan Singer:** Is our relevance and intent?

**Ryan Singer:** Now let me ask this carefully.

**Ryan Singer:** Do I have to have high relevance and high intent for anything to qualify as an optimization, or do I optimize to improve relevance and intent?

**Board Room:** No.

**Board Room:** So relevance and intent are more about the opportunity under the hood of that surface area.

**Board Room:** And you know, there are cases where, like it could be fake.

**Board Room:** Right?

**Ryan Singer:** Like.

**Board Room:** So, for instance, like.

**Board Room:** Yeah, yeah, I'm.

**Ryan Singer:** You're already.

**Ryan Singer:** I, I, I just.

**Ryan Singer:** Because time is going so fast, I want to.

**Ryan Singer:** What?

**Ryan Singer:** I want to.

**Ryan Singer:** What?

**Board Room:** I.

**Ryan Singer:** What I think, I think we just captured something really important, which is that when it comes to opportunities, there's, there's a.

**Ryan Singer:** If, if these.

**Ryan Singer:** Sorry, if.

**Ryan Singer:** Opportunities.

**Ryan Singer:** Optimizations.

**Ryan Singer:** Optimizations.

**Ryan Singer:** When it comes to learn and improve optimizations, there are pages that are not, they don't.

**Ryan Singer:** Out of the 712, we shouldn't even be looking at them because.

**Ryan Singer:** Because a underlying opportunity isn't there.

**Board Room:** Right, Right.

**Board Room:** That Is very, very good point.

**Board Room:** Yeah.

**Ryan Singer:** So this is a very different degree of freedom in the system.

**Ryan Singer:** Right.

**Ryan Singer:** This is orthogonal to like what is the thing I'm trying to fix.

**Board Room:** Yeah.

**Board Room:** And, and I.

**Board Room:** That, that's a really cool thing which is like, I like this mental model which is like every page should have an opportunity brief under the hood that backs it.

**Ryan Singer:** Yes.

**Board Room:** The page context.

**Board Room:** That part of the context is the opportunity context of that page.

**Board Room:** Then there's like where the pageant is today, you know, because it's like opportunities will quantify.

**Ryan Singer:** It's like it's like a ball and a glove.

**Ryan Singer:** Like the opportunity is the glove and then like the ball is like, you know, but like you, you.

**Ryan Singer:** They're.

**Ryan Singer:** They're different things.

**Ryan Singer:** Given that the underlying opportunity is there, then these different things become relevant.

**Ryan Singer:** So what happens was what I want to do is I want to take away high traffic from needs fix.

**Ryan Singer:** I want to take away high traffic from expired and I want to say possible diagnoses per.

**Ryan Singer:** I'm going to call it page with opportunity.

**Board Room:** So just one thing here.

**Board Room:** It's.

**Board Room:** There's a very important distinction of realized versus unrealized opportunity.

**Ryan Singer:** Okay.

**Board Room:** And so if the aggregate opportunity here is let's say 10,000 visits a month and you're at like 9,700, like it's pretty realized and any fuck ups there will like hurt you where.

**Board Room:** So it's more urgent.

**Board Room:** Whereas like unrealized opportunities, it's a lot more like optimizations to try to realize more of it, you know, but there's less to lose.

**Board Room:** Like, like you have nothing to lose essentially.

**Board Room:** Right.

**Board Room:** You have a lot to gain and nothing to lose.

**Board Room:** Whereas like realized opportunities, you're 97 realized you have a lot to lose and very little to gain.

**Board Room:** Okay.

**Ryan Singer:** So when we, when we like offense.

**Board Room:** Versus defense a little bit.

**Ryan Singer:** Totally.

**Ryan Singer:** When we surface pages again, we're looking at the 712.

**Board Room:** Yeah.

**Ryan Singer:** When we, when we surface pages from the 712 to go work on first is that remove anything where there's no underlying opportunity.

**Ryan Singer:** Remove anything where there is a well realized opportunity and just give me unrealized opportunity.

**Board Room:** No, no, on the realized opportunity you're trying to prevent fuck ups.

**Board Room:** So it's like those you shouldn't.

**Board Room:** That is the highest.

**Board Room:** Highest is like realized opportunities with things that you can prevent now from causing pain in the future.

**Board Room:** Yeah.

**Board Room:** Huh.

**Ryan Singer:** Okay.

**Ryan Singer:** What it is that now tell me like what.

**Ryan Singer:** Okay.

**Ryan Singer:** Okay.

**Ryan Singer:** So underlying opportunity has two classes here.

**Ryan Singer:** There's realized and unrealized.

**Board Room:** Yes.

**Board Room:** Sorry.

**Ryan Singer:** Yeah.

**Board Room:** Let me just really quickly so there's realized and unrealized or realized.

**Board Room:** There is.

**Board Room:** This is a free fall.

**Board Room:** Drop everything.

**Board Room:** That's the highest tier.

**Board Room:** And then there's like, hey, it's realized.

**Board Room:** And these are like screaming alerts.

**Board Room:** They're going to churn if you don't do something about it right now.

**Board Room:** And you can still prevent it.

**Board Room:** Right?

**Board Room:** That's the next one.

**Board Room:** And then after that is everything else screaming alerts.

**Ryan Singer:** You can prevent it.

**Ryan Singer:** What's that?

**Board Room:** Like, this page is broken.

**Board Room:** There's a 404 as the ultimate.

**Board Room:** Right.

**Board Room:** Like.

**Board Room:** Or it could be like, you know, like the things you collective.

**Board Room:** Like, then there's one in this page.

**Ryan Singer:** Yeah, yeah, yeah, totally.

**Ryan Singer:** Okay, got it.

**Ryan Singer:** Okay.

**Board Room:** Somebody.

**Board Room:** The bucky redesign off the website and switches page one, stage two.

**Board Room:** Yeah, got it.

**Ryan Singer:** Okay.

**Ryan Singer:** So if I have a realized opportunity.

**Ryan Singer:** Okay, I have a realized opportunity.

**Ryan Singer:** I need to.

**Ryan Singer:** If.

**Ryan Singer:** If it's in freefall, then I have to.

**Ryan Singer:** I have to.

**Ryan Singer:** I have to immediately jump on it to try and fix it.

**Ryan Singer:** And if there's an alert on it where something is broken, I have to jump in and fix it.

**Board Room:** Yeah.

**Board Room:** Center for paper.

**Board Room:** Right now it's century, but very soon it becomes a B.

**Board Room:** Testing.

**Board Room:** Yeah.

**Board Room:** Yeah.

**Board Room:** You know, once you get into the.

**Board Room:** You fixed and you maintain everything.

**Board Room:** Now it's about experimentation.

**Board Room:** Yeah.

**Ryan Singer:** Okay, so here's.

**Ryan Singer:** Here's what.

**Ryan Singer:** Here's where my head is going.

**Ryan Singer:** Okay.

**Board Room:** That's like the best kind of.

**Board Room:** It's like, there's so much to be done, so much to do, so much opportunity.

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

**Board Room:** I have.

**Board Room:** So we are in the portfolio, surging.

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

**Board Room:** Yeah.

**Ryan Singer:** So what I, what I, what I want to see just naively is.

**Board Room:** Giant.

**Ryan Singer:** And.

**Board Room:** I think it's the.

**Board Room:** Is this status state or something.

**Ryan Singer:** It's, it's.

**Ryan Singer:** Yeah.

**Ryan Singer:** So like, I don't know what it is yet.

**Ryan Singer:** It's, it's a kind of smart, Not a smart filter.

**Ryan Singer:** It's a smart status.

**Board Room:** Yeah.

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

**Board Room:** Yeah, right.

**Board Room:** Red alerts.

**Board Room:** 12,000.

**Ryan Singer:** Exactly.

**Ryan Singer:** Yeah, whatever it is.

**Board Room:** Right.

**Ryan Singer:** But you know, we know what I mean.

**Ryan Singer:** We have the reference there.

**Board Room:** Yeah.

**Ryan Singer:** I just want to take anything that's a red alert and I want to put it on the top.

**Ryan Singer:** And you never have to touch a filter because you should never not be seeing that.

**Board Room:** Yeah, right.

**Board Room:** Yeah.

**Ryan Singer:** And then there's like.

**Board Room:** Right.

**Ryan Singer:** And then there's like there's a point, I don't know where the cutoff is.

**Ryan Singer:** There's a cutoff at some point where it's like, like actually, actually I don't even like this.

**Ryan Singer:** I, I don't like the idea that there's ever like now go dig yourself to figure out what to do.

**Ryan Singer:** Like, like, like what is that?

**Ryan Singer:** Like we, the whole point of being in the tool is that like we're not asking you to do this.

**Ryan Singer:** So what I'm, what I'm kind of thinking is that like we should actually have an opinion about what to float up here based on, on this like very specialized domain knowledge that we have.

**Board Room:** Right.

**Ryan Singer:** So like.

**Ryan Singer:** Yeah, this is opinion.

**Ryan Singer:** Yeah.

**Ryan Singer:** These are pages that are working.

**Ryan Singer:** Are working and fucked.

**Ryan Singer:** Do you know what I mean?

**Board Room:** Yeah.

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

**Board Room:** Yes.

**Board Room:** It's like fix now.

**Board Room:** Unrealized potential dead zone.

**Board Room:** Right.

**Board Room:** Kind of thing.

**Ryan Singer:** Fix, fix now.

**Ryan Singer:** So unrealized potential dead zone.

**Ryan Singer:** Dude.

**Ryan Singer:** So this is like, I love these moments where like I like, I'm trying to like reflect Marcel's brain back at Marcel and then Marcel is like, I'm gonna put the perfect word on that thing because like I know what that is.

**Ryan Singer:** And like whenever that happens, those are, those are really magical moments because these words have a lot of power.

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Like it's Marcel's voice and it's like it's, it's, it's Marcel's voice tied to the domain model, tied to the data Model.

**Board Room:** Right?

**Ryan Singer:** So like, when this, when this UI becomes fix now unrealized potential dead zone, it's like, dude, no app looks like this.

**Ryan Singer:** And it's so meaningful.

**Board Room:** Right?

**Ryan Singer:** And, and, and now it's kind of like where my, where my head goes is like, I feel like the.

**Ryan Singer:** There's work to be done on, like.

**Ryan Singer:** Okay, so what's the pipeline that these things go into, you know?

**Board Room:** Yeah, you can always have like, under the hood, like go explore everything else, like your entire portfolio.

**Board Room:** But like, if you lead with the portfolio, then it's just like you're back at the same thing, which is overwhelming sense of like, I don't know.

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

**Board Room:** The ideal state, to repeat it back to you is like, you should never need to apply a filter.

**Ryan Singer:** Yeah, exactly, exactly.

**Board Room:** The ideal state is like, you have all the contacts.

**Board Room:** Like, that's what LLMs are good at.

**Board Room:** You have.

**Ryan Singer:** Exactly.

**Board Room:** We have all the data, we have all the, you know, like, like the ideal state is like, you should never have to prompt anything.

**Board Room:** You should never have to apply a filter.

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

**Board Room:** Right.

**Board Room:** Yeah.

**Ryan Singer:** And then there's like, so, so the things that I have taken on and clicked to somehow.

**Ryan Singer:** So somehow these things have a.

**Ryan Singer:** Like a.

**Ryan Singer:** You know, there's like a do action on each one of these, right.

**Ryan Singer:** And like, which is like, put into my backlog or like, take this on or assign it to me or I don't know.

**Ryan Singer:** Right.

**Ryan Singer:** Like, accept this as work.

**Board Room:** Yeah, yeah.

**Board Room:** Right.

**Ryan Singer:** So we need to have a state in each one of these of like, okay, if this is fixed now and this is like, we're screwed if we don't fix this.

**Ryan Singer:** Like, is somebody on this?

**Ryan Singer:** Right.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** So that's the thing that we also don't see today.

**Ryan Singer:** Like, if this is truly this important, it's like there's.

**Board Room:** It should be on the side.

**Ryan Singer:** Why am I even going to a backlog?

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Like, like, I'm almost wondering if, like, I want to see.

**Ryan Singer:** Like, like this is totally not the right word.

**Ryan Singer:** Claim.

**Board Room:** Yeah, yeah.

**Ryan Singer:** But like, do you know what I mean?

**Ryan Singer:** Like, like, like what I want is like, like, like, like Jill is on it.

**Ryan Singer:** You know what I mean?

**Board Room:** It's almost like who's on call and on fire?

**Ryan Singer:** Exactly.

**Ryan Singer:** Yeah.

**Ryan Singer:** Like, who's.

**Ryan Singer:** Yeah.

**Ryan Singer:** Who's on it?

**Board Room:** Right?

**Ryan Singer:** Because this is literally, like, this isn't work for later.

**Ryan Singer:** This is like the fix now is the emergency room.

**Ryan Singer:** So I need to know, like, where's the patient?

**Ryan Singer:** Where's the doctor?

**Ryan Singer:** Like, what's going on?

**Board Room:** Right.

**Ryan Singer:** And.

**Ryan Singer:** And if we, if we, if we express this urgency around, like, who is doing it and what is the state?

**Board Room:** It.

**Ryan Singer:** It's very.

**Ryan Singer:** Again, like, it's tying it all together.

**Ryan Singer:** Like what this thing is now.

**Board Room:** This.

**Ryan Singer:** I think it still makes sense.

**Ryan Singer:** Yeah.

**Board Room:** Make sure I'm visualizing the same stuff as you.

**Board Room:** So what you have on the right side, that.

**Board Room:** Those would be the cells of the table that you're thinking the fix now.

**Ryan Singer:** Yeah.

**Ryan Singer:** Sorry.

**Ryan Singer:** So.

**Ryan Singer:** So.

**Ryan Singer:** So this is what.

**Ryan Singer:** What I was.

**Ryan Singer:** Exactly what I was.

**Ryan Singer:** I was.

**Ryan Singer:** I was starting to think about these once they're in the pipeline, but it's the same thing everywhere actually.

**Board Room:** Right.

**Ryan Singer:** Like as a row.

**Ryan Singer:** So let's do that.

**Ryan Singer:** Let's actually just like take this and put it here.

**Board Room:** Can I just one quick think of this.

**Board Room:** Just writing this down.

**Board Room:** That's like.

**Board Room:** Can you zoom into fix now really quickly here on the right side where you have like page five?

**Ryan Singer:** Yes, yes.

**Board Room:** And so in my mind, it's kind of like if you did fix now and you put a box around it and then and then you have high performer and you put another box around it and.

**Board Room:** And then in.

**Board Room:** And then you put another box in it.

**Board Room:** It's essentially like, fix now versus, like, you know, all the other actions then high performance, like high average, low performer or dead in the water.

**Board Room:** And then in free fall can be in free fall, likely to fall, decaying, stable, rising or surging.

**Board Room:** You know, like.

**Ryan Singer:** Yeah.

**Board Room:** Does that make sense?

**Board Room:** Like, and, and then like, like, we just.

**Board Room:** That's it, right?

**Board Room:** Like, that's kind of it.

**Board Room:** That's like, all you should care about.

**Board Room:** Like, everything else is details and backup.

**Ryan Singer:** Yeah, yeah, that's.

**Ryan Singer:** That's.

**Ryan Singer:** That's.

**Ryan Singer:** I.

**Ryan Singer:** Like, yeah, yeah.

**Board Room:** Does that make sense?

**Board Room:** I don't know.

**Board Room:** I was trying to write it down as we were talking.

**Board Room:** So it's like, wait, hold on.

**Board Room:** There might be something here to simplify the out of this versus, like 50 numbers everywhere in a table.

**Ryan Singer:** No, that's.

**Ryan Singer:** That's.

**Board Room:** That's exact.

**Ryan Singer:** No, that.

**Ryan Singer:** Exactly.

**Ryan Singer:** No, like, exactly.

**Ryan Singer:** So this coming back to this, this is exactly what we shouldn't have to look at.

**Board Room:** Like, I don't know what to do with this.

**Board Room:** Like, I don't know what to do with this power.

**Board Room:** That.

**Board Room:** Right.

**Board Room:** Yeah.

**Ryan Singer:** This, this is, this is back in that Google Analytics thing of like, we don't know what you want, we don't know what you need.

**Ryan Singer:** So, like, good luck.

**Ryan Singer:** Here's the data.

**Board Room:** Yeah, it's like, slightly more abstracted, but.

**Board Room:** But, like, not actionable.

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

**Board Room:** Right.

**Ryan Singer:** So we can say, like, this is a high performer because, you know, and it's in free fall because, look, like.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Like, here's the, like, exactly what you.

**Ryan Singer:** Like, you know, like, here's the chart.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Like, yeah, like, this is why you're seeing this.

**Ryan Singer:** But, but.

**Ryan Singer:** But this is totally.

**Ryan Singer:** Like, I don't even need this if I trust this.

**Board Room:** Yeah, right.

**Board Room:** Yeah, it's all relative.

**Board Room:** Right?

**Board Room:** Like, you can put something at like 1500 or whatever, you know, yeah.

**Ryan Singer:** Now the, the one, the place where I would say is that if I look at this in isolation, I want to have all these pieces and if I'm, if, if we have a kind of a triage view, we probably subtract the things that are true for all of them.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Like, because these are all probably high performers if they're in fixed now.

**Ryan Singer:** Yeah, actually it doesn't matter.

**Board Room:** They are, but it just doesn't matter because it's just like.

**Ryan Singer:** It doesn't matter.

**Board Room:** Like free fall.

**Board Room:** It's still like free fall and likely to fall or, or decaying are like three negative things, right?

**Ryan Singer:** Yep.

**Board Room:** And it's assuming most of these are high performer or either way, the logic, as long as you put it in these buckets right.

**Board Room:** Then there's only three buckets of actions here.

**Board Room:** Right.

**Board Room:** Like now green alerts, that zone.

**Board Room:** And that's kind of it.

**Board Room:** And then later on you can go into the explore all and advanced mode and whatever the fuck, you know, like.

**Ryan Singer:** Yeah.

**Board Room:** Marshall mode to just like go find new patterns.

**Board Room:** Yeah, that is, that is always my, my, my concern or like my, my like.

**Board Room:** No, dude, but it's like if we make it like too simplistic that like listen, we have to listen to this this morning.

**Board Room:** William is our best.

**Board Room:** Yeah, okay.

**Board Room:** William is our best on this call on Spend Ask.

**Board Room:** We did not have access to Google Search console and he didn't even think of asking for it and he didn't even look at the data before doing an entire content strategy that we're presenting today like to an entire new client.

**Board Room:** Like he did it and he's our best.

**Board Room:** Like he's awesome, you know, but it didn't even cross his mind.

**Board Room:** It's like we have spokes that we have are extractions of existing marketing teams and product companies.

**Board Room:** So it's not consulting people.

**Board Room:** That's how internal marketing is performing.

**Board Room:** Is this like the bar here?

**Board Room:** It's not like engineering where there's like really good engineers out there.

**Board Room:** It's just like the bar here is just like no one has mental models form because there's so many marketing channels and marketers.

**Board Room:** I'm always trying like to decide are we building like Photoshop where you have a learning curve but once you crack it you're like awesome.

**Board Room:** Or are we building like no os, Mac OS Preview, you know, And I.

**Ryan Singer:** Think, dude, I'm 100%, I'm 100% sure you're building macOS preview.

**Ryan Singer:** I'm 100% sure.

**Ryan Singer:** Because the only reason you can Do.

**Ryan Singer:** The thing is nobody can do it.

**Ryan Singer:** Making preview in this market, in this vertical, requires you to be a genius because you have to be so good at figuring out how to actually automate the presentation.

**Ryan Singer:** Like making it.

**Ryan Singer:** It's too many signals.

**Ryan Singer:** So like, that's what agents are for.

**Board Room:** Like, agents are for exactly extracting that.

**Board Room:** And then your logic, your human judgment is where the place is leveraged, which is like some central place where the logic lives.

**Board Room:** Right.

**Board Room:** Like AKA like your plot nd or your MD or whatever the fuck.

**Board Room:** Right?

**Board Room:** Like that's where the human judgment can go.

**Board Room:** Like looking at the table.

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

**Board Room:** Right.

**Ryan Singer:** I would even think of this as.

**Board Room:** Like, yeah, this happened like a malware.

**Board Room:** It's like in your network.

**Board Room:** It's just like, go fix it.

**Board Room:** Like, drop everything you're doing.

**Board Room:** Go.

**Board Room:** Like address.

**Board Room:** Yeah.

**Board Room:** This is almost like a security tool.

**Board Room:** Yeah, it's a sim.

**Ryan Singer:** It's really like a security tool.

**Ryan Singer:** It really is.

**Ryan Singer:** And it's funny, actually, I have a client who's a sophisticated security tool maker that's like, with a very, very big footprint.

**Ryan Singer:** And it's like so many similarities now that I think about it.

**Ryan Singer:** You know, it's like they have this deep, deep, deep expertise in tradecraft of like how hackers try to trick you and then they have to translate those into like signals that get surfaced and they literally like use all the same language and stuff like that.

**Ryan Singer:** And it's.

**Ryan Singer:** Yeah, that's actually really interesting.

**Board Room:** Like, my first job was a security intelligence.com building LA for IBM Security.

**Board Room:** And the whole theme of the company, security intelligence.

**Board Room:** Because you had like app security versus like network security versus endpoint security versus like, you know, there's like all these like vectors that you had to protect.

**Board Room:** Anyways, there's a lot of parallels here.

**Ryan Singer:** Yeah.

**Ryan Singer:** So I think, I think this is not even a.

**Ryan Singer:** We were originally talking about like smart status or something.

**Ryan Singer:** I wouldn't even call this a status.

**Ryan Singer:** This is actually like a.

**Ryan Singer:** It's like a signal detection.

**Board Room:** Bringing to like what the guys are on the ground building today.

**Board Room:** I think this like what we're doing today, even if we build what we have on the left, like if we build and we don't spend too much time on like making it look awesome or something like this, a redesign.

**Board Room:** Like if the foundation is there for the right metrics, which all these things are on top of the right metrics.

**Board Room:** Doing a facelift in March to create an optimization area that has all the things we talked about feels very doable.

**Board Room:** So it doesn't feel like this, like I need to scrap everything that we have lined up for the next three weeks to go do this.

**Board Room:** You know, I think it's.

**Board Room:** You already have the filters in some ways and you were already going to build the logic.

**Board Room:** Let's put a create.

**Board Room:** Let's put the create menu and like I'll go on the right side because right side is the optimization one.

**Board Room:** Yeah.

**Board Room:** On the next, for now, this cycle.

**Board Room:** And then the optimization area.

**Board Room:** Then we do this.

**Board Room:** And then for the optimization area, I think there is a quick judo move here, which is like where it says pages by pillar, it's like pages by.

**Board Room:** And then it will be like whatever those fields are or something.

**Ryan Singer:** Pages by signal.

**Board Room:** Yeah, pages by signal or something.

**Board Room:** And then it's just like.

**Board Room:** And then each of these things that collapse are the fix now and the.

**Board Room:** Do you think we should still build the clustering system?

**Board Room:** Because that is a hard system to build.

**Ryan Singer:** That's what I wanted to ask about is how does this coexist with clustering?

**Board Room:** So keep in mind, there is almost never in successful sites where it's one page type and that page type is just for instance, even Spindex 700 blogs or sorry, 700 pages.

**Board Room:** 400 of those are blog, 60 of those are glossary and the rest is whatever the fuck.

**Board Room:** And but even within those 400 blogs, it's just like it's not just blogs, it's just like there's so much nuances of like content type intent that there's like topics, right.

**Board Room:** And then the.

**Board Room:** Some of those will be really important to them.

**Board Room:** Right.

**Board Room:** Like for instance, like compliance is really important because Spendesk is in the uk, it's their main market.

**Board Room:** And so like all things VPR compliance and things like that are there like edge over, ram it and whatever.

**Board Room:** Right.

**Board Room:** And so that's like a cluster or something that's just like has the lens of like being able to communicate something because it's really hard.

**Board Room:** Like imagine you have these alerts and everything's Perfect.

**Board Room:** Right.

**Board Room:** But then imagine you have 500 pages and.

**Board Room:** And there's like 72 in red alerts.

**Ryan Singer:** Okay.

**Board Room:** And.

**Board Room:** Okay, 230 in green alerts.

**Board Room:** Like, what the fuck?

**Board Room:** I don't know what to do with this.

**Board Room:** But, you know, so this.

**Ryan Singer:** What I'm hearing is the.

**Ryan Singer:** So the clustering is of course, like the clustering.

**Ryan Singer:** The function of clustering is to deal with too many results that are all kind of comparable to each other.

**Ryan Singer:** They're all similar to each other.

**Board Room:** Right?

**Board Room:** Exactly.

**Ryan Singer:** So I think structurally what that means is that you need to nest the clustering inside of the signal category.

**Board Room:** Exactly.

**Board Room:** So.

**Board Room:** So within the mode of that category, like random, is a mode, you know, so here mode, you might need to stack some clusters, like for a check that it would be like content type pricing versus review versus brand overview.

**Board Room:** And then within that would be a like category of page.

**Board Room:** Like, you know, like.

**Ryan Singer:** Exactly.

**Board Room:** And finance versus like, CRM versus marketing tools.

**Board Room:** And then that will give you the insight that you were looking for.

**Ryan Singer:** So, but.

**Ryan Singer:** But the cluster.

**Ryan Singer:** But I think we should be.

**Ryan Singer:** What that would mean.

**Ryan Singer:** I just want to spell it out and make sure that it's clear.

**Ryan Singer:** What that would mean is we would be repeating clusters.

**Ryan Singer:** Possibly.

**Board Room:** I was going to ask that.

**Board Room:** Yeah, yeah.

**Ryan Singer:** And I think it's important to call that out as a feature, not a bug.

**Board Room:** Right.

**Ryan Singer:** So like my.

**Ryan Singer:** If I'm.

**Ryan Singer:** Because.

**Ryan Singer:** Because if it's red alerts, I've got to act on it and it doesn't matter, like, where it lives.

**Ryan Singer:** I need it surfaced separately, you know, and then if.

**Ryan Singer:** If I'm in the mode of looking for unrealized opportunities, you know, then I can use my clustering as a way for me as a human to deal with the fact that there's 200 of them.

**Ryan Singer:** So I can understand what the heck I'm looking at.

**Board Room:** Right.

**Board Room:** Yeah.

**Board Room:** I almost don't know if we need clustering at the fix now layer.

**Ryan Singer:** Actually, that's true.

**Ryan Singer:** We shouldn't.

**Ryan Singer:** We shouldn't.

**Ryan Singer:** It should be flat, Right.

**Ryan Singer:** Unless you need it for context to understand what the meaning of the pages.

**Board Room:** Yeah, yeah.

**Board Room:** It's just like the second you cross over, like, mature sites, it's just like you're gonna need puzzles for everything because it's unmanaged to like.

**Board Room:** Yeah, yeah, it's 50, it's 500, you know, and it's.

**Board Room:** It's just like.

**Board Room:** Yep.

**Board Room:** It's the lens through which you, like, validate also that your strategy is working.

**Board Room:** Right.

**Board Room:** Like, hey, pricing is driving most of the traffic on our site.

**Board Room:** Right.

**Board Room:** But like, how do you know?

**Board Room:** Why are some pricing pages rising and some are not?

**Board Room:** Why are some.

**Board Room:** Right.

**Board Room:** Like, it's so hard to answer those questions, you know?

**Ryan Singer:** Yeah.

**Board Room:** Or even within the like red alert, potentially.

**Board Room:** Yeah.

**Board Room:** Yeah.

**Ryan Singer:** Good.

**Ryan Singer:** Okay, so what I'm going to do then is I'm going to, I'm going to say, well, actually all of this is changing, but the other thing I just want to call out is that we're actually like, I think, I think this is a bold and important move to consciously not do filters.

**Ryan Singer:** You know, even though there's a lot of smart ideas here.

**Ryan Singer:** Because the, of the, the, the bigger macro structural win of taking this approach.

**Board Room:** Yeah, yeah.

**Board Room:** I mean it's literally like.

**Board Room:** Yeah.

**Board Room:** So the three work.

**Board Room:** Three workflows and it's like it's a classifier and those are three fields in the table.

**Board Room:** Am I oversimplifying that?

**Board Room:** I think so.

**Board Room:** Because when you're dealing with 12,000 things.

**Board Room:** Yeah, but the main thing that I'm thinking is that this.

**Board Room:** Because like literally like yesterday I created all the linear tickets and the design, the mockups.

**Board Room:** What I showed you is essentially all static views every on a.

**Board Room:** The app.

**Board Room:** And the guys are starting to do the, the back end.

**Board Room:** So by the way, the scoring will all be important because like the scoring, Ryan, it's like.

**Board Room:** Yeah.

**Board Room:** So the two things that I think I'm trying to figure out what is not part of the scope, what can I cook this call?

**Board Room:** Because it's 14 areas and it's just four engineers including me there.

**Board Room:** So a lot of the stuff, we're not going to make it.

**Board Room:** So clustering is a big part that's not easy to do.

**Board Room:** The smart views are not easy to do.

**Board Room:** So again with the smart views constantly kit, I move the backlog out of the learning brutal area for the creation of new pages.

**Board Room:** Removing smart views cuts the scope.

**Board Room:** Collecting the data is too important.

**Board Room:** Showing the data doesn't matter that much.

**Board Room:** So we don't have to get that user interface super.

**Ryan Singer:** Right.

**Board Room:** Sorting doesn't matter anymore.

**Board Room:** Pagination doesn't matter anymore.

**Board Room:** So the configuration, 12,000 records with like time series stuff, it's working hard.

**Board Room:** So there's all these things that I can cut from the scope and then allows us to do that on the next cycle right away.

**Board Room:** Yeah, yeah.

**Board Room:** Just know that like somewhere there, the new page opportunity, like where we're missing in week two of these engagements is that like we have no view into their surface area.

**Ryan Singer:** Yeah.

**Board Room:** And.

**Board Room:** And so if we're giving them like a map of opportunity with, like, completely ignoring what their current service area is, it really puts those accounts at risk.

**Board Room:** Yeah, yeah.

**Board Room:** So understand your entire site is really important.

**Board Room:** Yeah.

**Board Room:** So it's like, it doesn't need to be this, but we need to have, I think, something to show their inventory pages in some way or at least the overall help, you know, like even saying, like, you know.

**Board Room:** But.

**Board Room:** Yeah, okay, well.

**Board Room:** But I think we can wrestle with it a little bit and cut, cut, cut.

**Board Room:** And then, like, see if, like, there's a way to kind of simplify the learn and improve.

**Board Room:** Because, like, what were you thinking for learn improve for this cycle?

**Board Room:** That user interface.

**Board Room:** Yeah.

**Board Room:** Actually, that's what I'm going to work today.

**Board Room:** I'm like, I'm gonna go as fast as I can on the first UI that we're showing.

**Board Room:** So, like, that changes it quite a bit.

**Board Room:** So.

**Board Room:** Okay.

**Board Room:** And so if we cut the filtering, you still have to do this.

**Board Room:** You still have to do all the scores, right?

**Board Room:** For everything.

**Board Room:** Yeah.

**Board Room:** And then all the three things here are essentially, like, what to do about the score.

**Board Room:** Right.

**Board Room:** So it's like two layers of instruction.

**Board Room:** Yeah.

**Board Room:** Right.

**Board Room:** It's like versus hot.

**Board Room:** Right.

**Board Room:** Like, the hot is like you're taking the scores and the changes in the scores and then like, drawing that.

**Board Room:** Yeah.

**Board Room:** And then the warm is the, like, the scores, which are kind of like indicators.

**Ryan Singer:** Yeah.

**Board Room:** That then have, like, a ton of.

**Board Room:** It's more like it didn't change the underlying data model.

**Board Room:** It does change the amount of effort we would put on the user interface for, like, I think we can have a flat table now with just clusters, not worry too much about sorting, imagination, that kind of stuff.

**Board Room:** And knowing that we got to do a second pass to build, like, the intelligence layer that we walked out there.

**Board Room:** And we might have to have a place to do what you're saying, just, like, see the whole inventory.

**Board Room:** So that is still basically the first screen.

**Board Room:** Is there a way to just have one of the three as a signal field so that the default of the view is like, filter bind.

**Board Room:** I think we can add it.

**Board Room:** If the default view is clustered and we show the metrics on the cluster level, that is something we can do.

**Board Room:** If I just do that, then that will help adding.

**Board Room:** Figuring out the workflow to go through all your pages, sorted by traffic, and then rank them and group them in the user interface later?

**Board Room:** It's.

**Board Room:** It's not hard because Ryan, like, one of our competitors, already has this, what they call page 360, and it's gaining some traction.

**Board Room:** And all it is is like a smart View with like, crazy amounts of filtering that then when you select it, applies all the filters and allows you to edit the actual details of those filters.

**Board Room:** And we think it's like the wrong approach, but it achieves a similar result, essentially.

**Board Room:** Yeah, it's like a filter template, you know, and almost, you know.

**Board Room:** Yeah, we can figure out a shorter or a future.

**Board Room:** That's easy.

**Board Room:** Like, I just don't want to spend like a whole week making that table perfect, you know?

**Board Room:** Yeah, it would be easy to do that.

**Board Room:** Like, tables are hard to do.

**Board Room:** And if you have like collapse and all that stuff, that volume, you're going to be spending days on, like, fixing performance issues and scrolling browser behavior and sorting patterns.

**Board Room:** Like, if I don't do any of that and I just focus on collecting the data and getting the detail page right, then we layer right after you finish this with the opinionated areas, you know, and also use the snapshots later to cover up anything if needed.

**Board Room:** Snapshots?

**Board Room:** Yeah.

**Board Room:** Meaning like if you have a table that literally just had three fields or three columns, right.

**Board Room:** And they're all cluster and it's like it had no data in it whatsoever, and if you click on it, you can see the full view.

**Board Room:** But, like, there's no aggregate reporting on anything.

**Board Room:** Like, any needs for aggregate reporting, which you do eventually need, like, to say, hey, traffic is growing or not.

**Board Room:** Like, you know, that can be done in snapshots is what I'm saying.

**Board Room:** Oh, broken snapshots.

**Board Room:** Yeah, that's what I'm saying.

**Board Room:** Yeah.

**Board Room:** You know what I mean?

**Board Room:** So it's like you don't.

**Board Room:** The table itself, I don't think to carry like this crazy amount of data.

**Board Room:** Like, it doesn't need to look like.

**Board Room:** Check that prompt table.

**Board Room:** Yeah, yeah, yeah, yeah, yeah.

**Board Room:** Sorry, Rand.

**Ryan Singer:** No, it's good because it means that we, We.

**Ryan Singer:** We unblocked something.

**Ryan Singer:** When you guys suddenly talk a lot, you know, I always take that as a positive sign, actually, you know, there.

**Board Room:** Yeah.

**Board Room:** Yeah.

**Board Room:** Okay, good.

**Board Room:** So much work, so much opportunity, so little time.

**Board Room:** We need more agents working 247 around the.

**Board Room:** We sleep.

**Board Room:** We need more R time.

**Ryan Singer:** I know.

**Board Room:** More R time.

**Board Room:** How do we grab the next three, four tickets?

**Board Room:** You know, it's like when you're in the, you know, at the grocery, grab your ticket, you know.

**Ryan Singer:** Like at the butcher.

**Board Room:** Yeah, yeah, yeah.

**Board Room:** Oh, cool.

**Board Room:** Okay.

**Board Room:** Should we look at upcoming.

**Board Room:** I think we have one more schedule.

**Board Room:** Right, Right.

**Ryan Singer:** No, this is the last one.

**Board Room:** Yeah.

**Board Room:** No.

**Board Room:** How's your life, Ryan?

**Board Room:** Yeah.

**Board Room:** How hardly.

**Board Room:** You said you were gonna, like, already kick off the.

**Ryan Singer:** Yeah.

**Ryan Singer:** It's interesting, you know, I, I'm just about to hopefully get like kind of a scope of work commitment and some signatures from like an integration partner on this big gnarly thing we're starting and we're doing like an AI integration at like a recruiting, like an enterprise recruiting software service thing.

**Ryan Singer:** And it's, I'm not out of the woods, you know what I mean?

**Ryan Singer:** But like, it's like we, we.

**Ryan Singer:** I can draw it on a napkin now, you know?

**Board Room:** Yeah.

**Ryan Singer:** So it's like, it's, it's, it's, it's, it's feeling more tractable, but I still kind of can't tell, especially in the first few weeks, like how crazy it's going to be in terms of needing to do a lot of code design with the integration partner, in which case I have to carve out time.

**Ryan Singer:** My us overlap hours are going to get eaten up really fast.

**Ryan Singer:** So I kind of cleared the deck to see what happens as we get rolling in the first one or two weeks ahead.

**Ryan Singer:** I actually have said no to all my upcoming training, like shaping sessions.

**Ryan Singer:** Like, so any of these like three hour sessions that are not you guys, I like cleared out.

**Ryan Singer:** And the thing I have to determine is if I can, if I need to keep space for this one project, you know, to, to, to spill over the edges or if I can, if I can start to picture something like you know, every other week a session like this or something like that, you know, that's kind of of like.

**Board Room:** Yeah.

**Ryan Singer:** I need to.

**Ryan Singer:** The.

**Ryan Singer:** My partner on this integration has been holding back on getting into full technical detail before they have a commitment signed.

**Ryan Singer:** So there's a little bit of some chicken neck going on there that we're.

**Board Room:** Working through, you know.

**Board Room:** Got it, got it.

**Ryan Singer:** Okay, so that's the current status here.

**Board Room:** Sounds good.

**Board Room:** Yeah.

**Ryan Singer:** Do.

**Board Room:** Would it be helpful to try to even like super tentative, like pencil in or you prefer to just like not anything and follow up offline?

**Ryan Singer:** Let's, let's, let's, let's take a moment and just talk through like what, what are the, what kind of help do you feel that you need in the coming weeks?

**Ryan Singer:** And like what.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Like what, what sort of deadlines are coming to you?

**Ryan Singer:** Just what's going on in terms of the urgency that you find yourself in specifically or like now, you know, like, what are the things that you need me for?

**Board Room:** Yeah, like, like from, from, from my perspective, like there's this like I for instance, like on.

**Board Room:** Check that.

**Board Room:** Right.

**Board Room:** Been juggling with this thing And I probably spent already like 50 hours of my time trying to like, shape something and not get into these aha moments that we get to in three hours.

**Board Room:** And.

**Board Room:** And it's often in the last like, like hour that they happen.

**Board Room:** Right.

**Board Room:** And so it's like I'm adding a zero to how much time it's.

**Board Room:** It's taking if I ever get there.

**Board Room:** Right.

**Board Room:** And that's just like me personally, you know, and.

**Board Room:** And so like, the thing is, like, if we were talking about one of our engineers, like, fine, whatever.

**Board Room:** Right.

**Board Room:** Like, but because it's like mine and Daniel's time, that that's zero of like three hours instead of 30 is like really meaningful.

**Board Room:** Like, like consequential to like the company because it can mean like months multiply later.

**Board Room:** Right?

**Ryan Singer:** Yeah.

**Board Room:** So the leverage that you bring us is like extremely valuable, like I would say, like, you know, at the highest, most important level.

**Board Room:** Because it's like there's no question of the opportunity and how big the opportunity is.

**Board Room:** There's no question on life, like the jobs to be done and how to do those jobs.

**Board Room:** It's all about, like, translating that into how the we put this in market.

**Ryan Singer:** It's all those.

**Board Room:** It's all how to crack those nuts, you know?

**Ryan Singer:** Yeah.

**Board Room:** And it's what you're the world class best in the world at.

**Board Room:** And you know, and, and so like, that's the help.

**Board Room:** It's like truly, like, just show up, you know, kind of help.

**Board Room:** That is.

**Board Room:** That is one.

**Board Room:** But.

**Board Room:** But it's also like, there's so many things though, like.

**Board Room:** Sorry, that is one.

**Board Room:** But it doesn't have to be with us in the room as well.

**Board Room:** Right.

**Board Room:** As in, like, if you don't have time with like us overlap.

**Board Room:** I'm pretty sure that if you like, if you get like Marcel's docman that he's struggling with on check that.

**Board Room:** Because this is just the area that we overlap and it's so critical that Marcel and I have to be in a room with you because this part of the system is so important.

**Board Room:** Marcel is shaking one thing, I'm shaking some other thing.

**Board Room:** On the framework, there's all these things happening at the same time, but I can check that for the case that he's giving.

**Board Room:** If he just gives you all the things that he's been working on, I'm.

**Ryan Singer:** Pretty sure I'm pretty doubtful of that because what I notice is that it's like Marcel just said, usually the first two hours is me like probing and probing and probing.

**Board Room:** Yeah, I agree with that.

**Ryan Singer:** Not only Absorbing.

**Ryan Singer:** It's tacit knowledge that you guys have that I'm pulling out so it wouldn't be in the document.

**Board Room:** Yeah.

**Board Room:** But I believe you also have like an amazing like that is on the product level.

**Board Room:** You also like seemingly helpful on the UX and the practical side of things when they're like yeah.

**Board Room:** As well.

**Board Room:** But I almost think like given how little time.

**Board Room:** Yeah.

**Board Room:** You have.

**Board Room:** Yeah.

**Board Room:** Like this is like if we had to fully multiplier.

**Board Room:** This is like a 10x amplifier and we're aligning between us.

**Board Room:** Yeah.

**Board Room:** So it's accomplishing multiple things at once and it's like reducing rework later which like.

**Board Room:** Yeah.

**Board Room:** And, and waste in 15.

**Board Room:** Yeah, yeah, for sure.

**Board Room:** That's the movement.

**Board Room:** So it's like if I only have three hours of your time once a month, I'll take it.

**Board Room:** If I had two of those sessions.

**Board Room:** Sessions, like you know, three hours, you know, and maybe just like 8:30 minute a week, you know, just like respond to a couple of things or you know, just like a couple questions, a couple thoughts like, you know, that would be like worth, you know, like anything.

**Board Room:** And then also like we would like.

**Board Room:** Personally I would love to make sure you get equity as well so that you're, you know, motivated long term, you know.

**Ryan Singer:** Yeah.

**Board Room:** Because our valuation is super low, man.

**Board Room:** So it's like there's a lot of, you know, I like.

**Ryan Singer:** Yeah, I like that idea a lot.

**Board Room:** So.

**Ryan Singer:** Let'S.

**Ryan Singer:** Yeah.

**Ryan Singer:** Next couple weeks are tough.

**Ryan Singer:** Let me do this.

**Board Room:** Next couple weeks we're busy too, so we're doing all this stuff.

**Ryan Singer:** So yeah, basically what's going to happen is I'm going to have, I'm gonna have some, some time opening again after the 18th of March.

**Ryan Singer:** And before then it's like unless something unlocks and I suddenly feel like I got to delegate a chunk of stuff that I thought I would have to like unstick myself, you know.

**Ryan Singer:** And it can go either way with this, with this client project that I have.

**Ryan Singer:** So let me do this.

**Ryan Singer:** Give me, I'll.

**Ryan Singer:** I'll give you.

**Ryan Singer:** I'm going to set a deadline for myself for, for Wednesday the 25th, just next, next Wednesday to, to get back to you with like, you know, do I have any capacity in the coming weeks or not?

**Ryan Singer:** You know, and then what we can do is at a minimum we can stake out the next session in mid March after.
