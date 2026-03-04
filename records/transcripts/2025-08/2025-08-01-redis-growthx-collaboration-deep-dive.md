# Redis <> GrowthX — Collaboration Deep Dive

<metadata>
date: 2025-08-01
time: 18:02 UTC
duration: 31 minutes
organizer: Marcel Santilli (GrowthX)
participants: Marcel Santilli (GrowthX), Kyle Gaudreau (GrowthX), Cody Henshaw (Redis)
fathom_recording_id: 78032763
fathom_url: https://fathom.video/calls/368077291
share_url: https://fathom.video/share/UmFWigqDyrDqycaEiXMNUYx3tyz1mwMG
source: fathom
enriched_on: 2026-03-03 19:42 UTC
</metadata>

---

## Summary

GrowthX presented its end-to-end content strategy and execution approach to Redis leadership, focusing on refreshing Redis' 6,000-page content library and improving positioning in AI and vector database spaces. Marcel outlined GrowthX's research-first methodology, deep context artifacts, and workflow automation that enable rapid results — citing examples like Airbuy (300 pages refreshed in 3 weeks, nearly 2x impressions) and Augment Code (immediate AI overview citations). Cody identified Redis' core challenge: capacity constraints preventing reframing of existing content to align with AI/LLM positioning, and acknowledged GrowthX's end-to-end approach (including CMS integration and brand team alignment) as compelling. Next steps include Marcel sending a formal proposal and examples of technical content work, with Cody scheduling a follow-up involving Fung-Lin Wu (SEO budget owner) and a brand team representative.

---

## Context

Redis is an in-memory data structure store with ~6,000 pages of content (including extensive technical documentation) and ~1,300-1,400 non-docs pages. Majority of organic traffic comes from docs and technical tutorials, with benchmarking content performing exceptionally well. Redis is led by Cody Henshaw (Head of Growth, overseeing web, growth marketing, technical marketing, and product marketing teams). Redis uses Profound to track AI/LLM visibility scores and has observed that recently refreshed content (within the last 12 months) drives the most citations in AI tools. The company recently began a website replatform and is exploring opportunities to shift brand positioning from "caching" to AI/retrieval use cases, but faces capacity constraints and a strict brand review process for all published content. Currently working with an SEO agency that generates briefs, but execution has stalled with 60 unreviewed briefs in queue. This is GrowthX's first deep conversation with Redis leadership on a potential engagement.

---

## Relevance

**To GrowthX Delivery:**
- Large technical footprint (6,000 pages) with existing authority creates high-impact refresh opportunity — similar to Airbuy (300 pages in 3 weeks, 2x impressions) and Ramp models
- Prospect using Profound for visibility tracking aligns with GrowthX's multi-signal approach (Profound, GSC, GA, LLM referrals)
- Strict brand team review process requires GrowthX to position itself as extension of brand function, not just content factory — opportunity to use brand artifacts and tone frameworks
- Replatform project is active bottleneck; timing-sensitive opportunity to refresh content during infrastructure migration

**To CheckThat:**
- Redis is tracking LLM visibility and AI positioning shifts — direct alignment with CheckThat use cases (vector databases, AI stack reframing)
- Prospect explicitly interested in repositioning from "caching" to "AI/retrieval" — demonstrates demand for AI visibility and positioning intelligence
- Profound integration shows prospect is already monitoring AI overview citations; CheckThat could provide complementary category and competitor signals

**To GrowthX Business Development:**
- Enterprise-scale technical company with brand authority and dedicated growth team signals expansion potential beyond initial 8-week sprint
- Current SEO agency underperforming (60 unused briefs) creates opportunity to replace existing vendor relationship
- Cody's pain point (capacity constraints) matches GrowthX' pitch perfectly; high likelihood of decision if proposal aligns with budget authority
- Fung-Lin Wu (SEO budget owner) and brand team representation in follow-up suggests multi-stakeholder buy-in process — manage timeline expectations around procurement (2-week approval window)

---

## Overview

- Redis faces challenges with content refresh, AI-related positioning, and scaling technical content creation
- GrowthX offers end-to-end content strategy and execution services, with rapid results in AI/LLM visibility
- Redis team is interested in GrowthX's approach, particularly for refreshing existing content and improving AI-related messaging
- Next steps include involving key Redis stakeholders and reviewing a formal proposal from GrowthX

---

## Key Topics

### Redis Content Landscape and Challenges

  - Redis has \~6,000 total pages, \~1,300-1,400 excluding docs
  - Majority of organic traffic comes from docs and technical content (tutorials, benchmarking)
  - Current focus on creating new content rather than refreshing existing pages
  - Capacity constraints limit ability to reframe existing content (e.g., relating caching to AI stack)
  - Brand team has strict review process for content voice and style
  - Current SEO agency provides content briefs, but execution is challenging (60 unused briefs in queue)

### GrowthX Approach and Capabilities

  - End-to-end service: strategy, execution, AI workflows, tooling, and CMS integration
  - 8-week initial strategy sprint with option to continue or terminate
  - Rapid results: e.g., Engine.com seeing improvements by week 8
  - Deep research and context-building process (2-3 weeks for calibration and artifact generation)
  - Focus on efficient, high-quality content creation aligned with company context
  - Ability to quickly improve AI/LLM visibility through strategic content updates

### Potential Collaboration Areas

  - Refreshing and optimizing Redis' extensive content library
  - Improving Redis' positioning in AI and vector database spaces
  - Streamlining content creation and approval processes
  - Replacing or complementing current SEO agency services

### GrowthX Case Studies

  - Ramp: Consistent AI overview appearances, vendor catalog, per diem calculator
  - Augment Code: Immediate citations for new "Guides" section
  - Airbuy: 300 pages refreshed in 3 weeks, nearly 2x impressions

---

## Action Items

**Marcel Santilli (GrowthX)**
- Send Cody recording of 2-hr workshop on content strategy and GEO

- Send formal proposal to Cody for Redis engagement (including 8-week strategy sprint details)

- Share examples of technical content created for similar technical companies (references: Ramp, Augment Code, Airbuy)


**Cody Henshaw (Redis)**
- Schedule follow-up meeting with Fung-Lin Wu (SEO budget owner) and brand team representative to discuss GrowthX proposal

---

## Transcript

**Kyle Gaudreau:** It's going, you know, what we were trying to do is just get all the folks in the right room together.

**Kyle Gaudreau:** You know, we had a good conversation with Megan, you know, shared a lot of insights into, you know, opportunities, challenges, some, like, areas of focus.

**Marcel Santilli:** Hey, Marcel, hopefully you got a good drink of water or something.

**Kyle Gaudreau:** Not yet.

**Marcel Santilli:** I'll have a bathroom break after this.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** I was just a very high level updating, Cody, on our conversation with Megan.

**Kyle Gaudreau:** And, you know, it seems like you all have a ton of content, ton of opportunities, just so much surface area, super exciting.

**Kyle Gaudreau:** And so we were just sharing a little bit of how we work and collaborate with teams and it seemed to resonate quite well with Megan.

**Kyle Gaudreau:** And so our mindset today was just helping catch you up a bit on how we think, how we work, answer any questions you have.

**Kyle Gaudreau:** And we can always dive in deeper, you know, explore what kind of opportunities we could theoretically collaborate on.

**Cody Henshaw:** That was the mindset coming into today.

**Kyle Gaudreau:** Awesome.

**Kyle Gaudreau:** Marcel, Cody shared, he's just leaving SF, so we missed him.

**Kyle Gaudreau:** He's heading to the airport, so off camera, but with us here.

**Marcel Santilli:** Sorry, Cody.

**Marcel Santilli:** Are you back anytime soon?

**Cody Henshaw:** I'll be back in, I guess, yeah, exactly a month from today.

**Marcel Santilli:** All right, cool. That sounds good.

**Cody Henshaw:** Where are you based?

**Cody Henshaw:** Austin, Texas.

**Marcel Santilli:** Oh, no way. I'm a longhorn. And my parents live just outside of Austin. Are you native from Austin?

**Cody Henshaw:** I'm not.

**Cody Henshaw:** I was one of the many Bay Area transplants.

**Cody Henshaw:** Yeah, I spent my whole 20s in SF and then moved to just outside of Austin. Most people don't know the suburbs out there. I'm not in Round Rock.

**Cody Henshaw:** I'm south, in Dripping Springs.

**Cody Henshaw:** It's a lot of fun these days if you're outside of Austin. It's a nightmare.

**Marcel Santilli:** I imagine it hasn't changed. I used to take Mopac to school — the bottlenecks are insane.

**Marcel Santilli:** Every time I go to Austin, it's like a year in between and there are 30 new buildings. The downtown went from all flat to all high rises. Every time I go, there's five more being built.

**Kyle Gaudreau:** I noticed it too — I had a five, eight year gap between visits and it was completely different.

**Marcel Santilli:** But Cody, before we jump in — Megan shared a lot of things with us, but you guys just met. It would be awesome to understand some context on your end. If you had a magic wand, what's one thing you wish you had more help on?

**Cody Henshaw:** I don't know how much context she gave you on my role and the teams that I lead, but maybe that helps to set some of the context.

**Cody Henshaw:** I lead our growth function, which includes the website, web team, infrastructure, and growth marketers trying to get people to sign up for the cloud product. I also manage a technical marketing team that creates tutorials in multiple languages, and a product marketing team that handles marketing pages and anything outside of tutorials. My team spends a ton of time building and rebuilding technical content, especially since code pushes constantly make tutorials obsolete.

**Cody Henshaw:** We were kind of ahead of the curve on LLM tracking with Profound, and we track our visibility scores. We see that the most cited content is what we've refreshed in the last 12 months. So if I could wave a magic wand, I'd want a tool or service that helps my teams create refreshed technical content really quickly.

**Marcel Santilli:** That's perfect. I'm switching screens — can you see if I share my screen?

**Cody Henshaw:** Yeah, I can see it.

**Marcel Santilli:** There are so many areas to jump into, but one thing I want to mention — turns out we're using Redis for every single part of our platform. You guys are our caching layer, and it's really cool to potentially work with a company we use for every single aspect of everything we do.

**Cody Henshaw:** That's great to hear.

**Marcel Santilli:** What I could do is show you at a high level how we work and a bit behind the scenes. I just finished a two-hour workshop, so I can send you the recording in case anyone on your team wants to listen. It covers content strategy, how we do things, why we do it that way — basically a roadmap for replicating our approach.

**Cody Henshaw:** Oh, super cool.

**Marcel Santilli:** At a high level, this is especially our sweet spot for technical companies. We work with Metronome, Augment Code, Webflow, Abnormal Security, SentinelOne, Akna, Diligent, Strapi, and Airbuy — all technical companies. I've been doing technical marketing to technical companies my whole career: IBM, HP Software, HashiCorp, and Skill.ai. This is our sweet spot.

**Marcel Santilli:** One of the things we do is really go deep into understanding your space. We create company context that goes deeper into how you see your whole market. Even companies with amazing product marketing often lack this. We define personas concretely and understand their fears, motivations, and certainties. All these artifacts let us scale with quality and ensure everyone works from the same big picture. Without that alignment, there's no amount of human review that allows you to scale — you get stuck in line editing. But if we agree on the big picture, everything else scales.

**Marcel Santilli:** Part of that is understanding what your brand should sound like. Then we map out the entire ecosystem — companies, personas, industries — and map them against topic clusters. That's critical because you're using Profound — the queries you monitor are only as good as the prompts. If you're not mapped back to deep audience understanding and how that connects to your big picture, you end up tracking hundreds of topic clusters and thousands of prompts, and it becomes impossible to understand what's actually working. This makes planning much easier.

**Marcel Santilli:** Then we audit all your pages and everything you're doing, plus competitive audits. We go super deep. We create assignments in our system that show the step-by-step process. What lets us move faster is our workflow engine under the hood — streamlining the whole process. The assignment brief, research, outline, drafting, fact-checking are all really detailed. We create all the artifacts for you upfront, so you achieve quality and speed. You also have an editor in the loop who can say things like "add a TLDR and improve the first sentence to be more of a hook." Our editors use the artifacts, context, and business understanding to guide the process. With technical content especially, accuracy is critical.

**Marcel Santilli:** After we go through this whole process, we create artifacts, calibrate, and map to the right opportunities based on topics and audience-first mindset. We audit existing pages, create assignments, produce them, and learn from signals. The really interesting part is that signals are happening way faster than we expected. Sometimes we update or publish a page and almost immediately the language gets incorporated into AI overviews. Ramp is a great example — we've done hundreds of audience-first content pieces for them over the last year, like "how long do ACH transfers take."

**Marcel Santilli:** The content is consistent, stays fresh, cross-links well, and is highly cited with unique information. They show up consistently on AI overviews, Perplexity, ChatGPT, and organic search. We also built a vendor catalog with unique data to enrich articles. We do everything — planning, publishing, optimization, graphics. We remove bottlenecks for capacity-constrained teams. We built a per diem calculator that's interactive with state and city pages, tables, and up-to-date data, all highly cited. We've done expense category catalogs that perform well. All of these get cited and mentioned.

**Cody Henshaw:** Is that calculator something generated from your initial research, or did they ask for it?

**Marcel Santilli:** It's a combination. The per diem calculator was our suggestion. Expense categories were outdated, so we refreshed them. The vendor catalog was their idea initially, but we crafted the entire experience and scaling strategy. They said they had data and wanted to create pages based on vendors.

**Marcel Santilli:** With Augment Code, we created a new section called "Guides." We published it July 29-30 and it immediately started getting cited. It's a brand new section with not much domain authority, but it's so well researched it's insane. The language we used gets pulled almost verbatim in some of these tools. The signals are returning incredibly fast — it's wild.

**Marcel Santilli:** A lot of this comes from our deep research approach. We don't just take a topic and brief. We break down the topic within your company context into specific questions, do deep research on all of them, and use that research when drafting and executing. Our sweet spot is technical companies with large footprints where there are bottlenecks. You see results fast because of that. Airbuy is a great example — we refreshed 300 pages in three weeks and nearly doubled impressions.

**Cody Henshaw:** I don't know if you saw it, Marcel, but they just closed a 100k deal off of ChatGPT from some of the content we created.

**Marcel Santilli:** That's wild.

**Marcel Santilli:** We track not just visibility, but LLM referrals. We look at Profound data and pull our own data too. The quality of the queries and prompts you monitor makes a huge difference, so we make sure you have all the context and queries. We correlate reach and visibility, track engagement when people land on your site, and measure content quality through time-on-page, GSC and GA data, and conversions.

**Cody Henshaw:** What's the actual research process up front? That feels like the big investment, and then you can kind of crank after that.

**Marcel Santilli:** Most companies, as long as they give us access and are responsive, we're done with calibration and artifact generation by week two or three.

**Marcel Santilli:** Engine.com is at week eight now, we've published 24 pieces and they're already getting clicks, impressions, and improving LLM visibility. We have 30 more in production. They're very responsive. With larger technical footprints, it's about aligning on a few lanes of personas, audiences, or topics so you're not doing 50 calibration cycles. Week one, we schedule deep technical dives with experts and ingest information. But the benefit of Redis is the open source nature gives you tons of information, so we can move fast and aren't bottlenecked by internal expert interviews.

**Marcel Santilli:** Anything else on your end we didn't cover? Now we can switch into some of the unique opportunities we're seeing for you guys.

**Cody Henshaw:** I don't have specific questions yet, but I'm sure I will.

**Marcel Santilli:** The part that's really interesting is you guys have almost 6,000 pages if you include everything.

**Cody Henshaw:** It's an absurd amount of pages. We're doing a replatform right now, so it's been a nightmare.

**Kyle Gaudreau:** If you filter out docs content, which maybe we wouldn't focus there, it's still a large footprint — maybe 1,300 to 1,400 pages.

**Cody Henshaw:** That sounds about right.

**Marcel Santilli:** What has worked from a content and digital footprint perspective? From organic, mostly?

**Cody Henshaw:** The majority comes from docs and technical content — tutorials and benchmarking. Benchmarking works really well. One of our top-performing blog posts is a vector database benchmarking piece.

**Marcel Santilli:** People like to see the proof and how to do things. That makes sense.

**Marcel Santilli:** What's really interesting is you have so much footprint between docs, learn, and blog — there's no way you're keeping it all up-to-date. You have the authority to go back and refresh that surface area. Refreshing helps maintain leadership and show up even more. It's about tweaking the language. Megan mentioned Pinecone has more brand awareness around vector databases and retrieval for AI, while people associate Redis with caching. How do we change that? The only way is to integrate it across everything you do — not changing your whole site, but surgically tweaking and addressing it at massive scale. Augment Code is an example. They weren't showing up for "coding tools for large code bases," but within a day of language changes in informational articles, they showed up as number one in many LLM queries. Nothing on the homepage changed.

**Cody Henshaw:** Completely agree.

**Cody Henshaw:** We have a tendency to just create net new content, but as you said, we're ranked well in caching but trying to build the AI story. There's a lot of existing content we could reframe — like updating the caching page to talk about AI and how caching relates to the AI stack. We're just capacity constrained there.

**Marcel Santilli:** One of the things we do is eight-week strategy sprints. At the end, you guys can fire us, we can fire you, but so far that hasn't happened. We go super deep — creating all the artifacts, content strategy, execution, and de-risking things. This situation would be really beneficial. We can knock it out of the park for you. We have good references from non-competitive but similar companies. We're working with companies in AI and LLM security like Abnormal and SentinelOne. The question is how long your procurement process takes. On our end, we can move super quickly to refresh content and craft the right strategy.

**Cody Henshaw:** It depends on which day you hit procurement. It's a nightmare, but once it's submitted, they have about two weeks to approve. Unless there's a security review — which I don't think there would be unless we're giving access to internal systems.

**Kyle Gaudreau:** Sometimes AI perks things up, but us sharing how we work and that we focus on public data usually alleviates concerns. We just have to go through a few things.

**Cody Henshaw:** One question came up: how do you keep content aligned with brand? We have a really strict brand team that cares about voice — every piece goes through them before publishing. Do you work with brand teams like that or build it into tools? We pay for Writer.AI but I've never used it.

**Marcel Santilli:** Many teams buy tools that don't get used because setup is time-consuming and creating the right artifacts through interviews takes work. We're end-to-end. We handle strategy, execution, AI workflows, and tooling. We buy API access and implement it all. We do all the lift on CMS access, publishing, optimization, and SEO audits. We meet weekly and become an extension of your team.

**Cody Henshaw:** That's cool.

**Marcel Santilli:** We try to give you no homework except ensuring we're heading in the right direction and calibrating. We're truly an extension of your team.

**Cody Henshaw:** Megan probably told you we work with an SEO agency. Do you work complementary to something like that? They give us content briefs but they're not very helpful — some writer writes them and the content is hit or miss.

**Marcel Santilli:** A lot of companies waste money on agencies. Ramp fired all theirs after working with us. Reddit did too. In-house helps a bit more because they share context. Our best engagements are where we can execute quickly. Engine.com switched from an agency called Graphi. These agencies charge a lot for briefs that don't actually help — you still have to do the work.

**Cody Henshaw:** Exactly. I have to review all the briefs and have my team review them for technical accuracy. It takes forever. We have 60 briefs sitting around with no action. It's a nightmare.

**Kyle Gaudreau:** A lot of us are former in-house marketers who've built teams and inherited agencies. We've felt that pain, so that's why we modeled things differently.

**Marcel Santilli:** I have to run — what's the logical next step? Should we do a deep dive and send a proposal?

**Cody Henshaw:** I think we definitely need Fung-Lin in this conversation. She owns the SEO budget and handles the briefs. Someone from the brand team should be involved too. Send a proposal, and I'd love to see examples of technical content you've created for companies similar to us.

**Marcel Santilli:** Perfect.

**Marcel Santilli:** We'll follow up and have a safe trip back.

**Cody Henshaw:** Thanks. Talk soon. Bye.
