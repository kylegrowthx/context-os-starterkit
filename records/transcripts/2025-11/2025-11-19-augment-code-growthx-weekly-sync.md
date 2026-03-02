# Augment Code <> GrowthX Weekly Sync

<metadata>
date: 2025-11-19
time: 18:00 UTC
duration: 21 minutes
organizer: Jason Gong (GrowthX)
participants: Jason Gong (GrowthX), Sylvain Giuliani (Augment Code), Marisol Smith (GrowthX), Liz Kushnereit (GrowthX)
fathom_recording_id: 102879058
fathom_url: https://fathom.video/calls/479041214
share_url: https://fathom.video/share/Gr1ixczaXayaMt-zws6yN4ah21n_-tsX
source: fathom
enriched_on: 2025-03-02 11:00 UTC
</metadata>

---

## Summary

GrowthX and Augment Code aligned on content strategy priorities for December launches. A critical conversion bug is blocking signups despite strong traffic (200 visits/week to one top article yielded only one install), triggered by recent website changes and compounded by a missing download link until the final signup step. The team committed to two major product launches in December: a self-serve Code Review tool (with aggressive comparison articles) and a Context Engine MCP (Managed Context Provider) to make cheaper models perform like GPT-5, requiring new content clusters around MCP search intents and use cases. Augment Code will build an internal code wiki demo to showcase the Context Engine, while GrowthX will proceed with a newsletter experiment to nurture expired trial accounts (potentially thousands per week if the decision gate succeeds).

---

## Context

Augment Code is a developer tool company building an AI coding agent. GrowthX is providing content marketing services focused on driving organic traffic and conversions for Augment Code's website. The relationship is an ongoing engagement, with the weekly sync being the standing cadence to review performance metrics, align on content strategy, and coordinate launches. This meeting happened in the context of two major product launches scheduled for December (Code Review tool and Context Engine MCP), requiring significant content strategy pivots from Augment Code and new content production from GrowthX. The meeting also included discussion of internal Augment Code product decisions (like the code wiki demo) and strategy decisions (like the newsletter experiment for nurturing dormant users).

---

## Relevance

**To GrowthX Delivery:**
- Content strategy pivot required: shifting from 50% refreshes to aggressive focus on comparison articles (Augment vs. Greptile vs. CodeRabbit) and new MCP-related use case content for December launches
- Major conversion optimization opportunity: identified critical bug in signup funnel (90% drop-off due to missing download link until final step) — Jason committed to adding CTAs across key bottom-of-funnel pages
- Newsletter experiment framework established: if successful, could auto-populate thousands of nurture contacts per week from expired trial accounts, creating new content distribution leverage

**To CheckThat:**
- MCP search intents emerging as major opportunity: high-volume searches for "kilocode best models," "best MCP for client" suggest strong demand for AI visibility/prompt performance content
- Context Engine MCP launch in December: Augment Code positioning as a plug-in to make cheaper models (GLM 4.6, Kimi K2) perform like GPT-5 — opportunity to track how positioning and messaging evolve

**To GrowthX Business Development:**
- Account expansion signal: newsletter experiment and data quality investments suggest Augment Code is scaling sales and product infrastructure (indicating confidence in growth)
- Reference potential: Augment Code's success with content-driven conversions could serve as strong reference case for developer tool prospects

---

## Overview

- **Critical Conversion Bug:** A top-ranking article on AI coding tools (ranking #9, ~200 visits/week) drove only one signup in the last week. Recent website changes appear to have triggered the issue, compounded by missing download CTAs until the final signup step (causing a 90% funnel drop-off).
- **December Product Launches:** Two major launches scheduled: (1) self-serve Code Review tool with aggressive "Augment vs. Greptile vs. CodeRabbit" comparison content, and (2) Context Engine MCP to make cheaper models (GLM 4.6, Kimi K2) perform like GPT-5, targeting high-intent "kilocode best models" and "best MCP" search intents.
- **Content Strategy Pivot:** Shifting focus from the current 50/50 mix of refreshes and new content to aggressive comparison and use-case content for MCP and Code Review. New site structure (content organized under `/tools`) is already driving traffic.
- **Newsletter Experiment:** Proceeding with test using Dominic Kent for content. Success gate will trigger auto-enrollment of expired trial accounts (potentially thousands per week) into nurture newsletter.

---

## Key Topics

### Performance & Conversion Bug

  - Traffic is performing well and on target, but a critical conversion bug is blocking signups across the site.
  - **Evidence:** A top-ranking article for "AI coding systems" (ranking #9, ~200 visits/week) yielded only one signup in the last week. This is bottom-of-funnel content with high intent.
  - **Root Cause Hypothesis:** The bug is linked to recent website changes rolled out by Augment Code.
  - **Contributing Factor:** The signup funnel lacks a download link until the final step, causing approximately 90% of users to drop off before conversion.
  - **Data Quality:** Augment Code is kicking off an internal PostHog QA project to ensure the accuracy of signup metrics, acknowledging that current numbers may not be entirely reliable.

### December Product Launches

  - **1. Self-Serve Code Review Tool**
      - **Launch Timeline:** December 2025.
      - **Content Strategy:** Aggressive comparison articles positioning Augment Code against direct competitors (Greptile, CodeRabbit, etc.).
      - **Proof Point:** Initial benchmarks show Augment Code's Code Review tool outperforms competitors. Sylvain committed to providing GrowthX with the benchmark draft for content foundation.
      - **Differentiation:** Will have dedicated landing page for benchmark comparison to drive bottom-of-funnel conversions.
  - **2. Context Engine MCP (Managed Context Provider)**
      - **Launch Timeline:** December 2025 (MCP version); January 2026 (full API).
      - **Function:** A plug-in module that integrates with any coding agent (Claude, cursor, etc.) to augment cheaper AI models (e.g., GLM 4.6, Kimi K2, Sonnet 4.5) to perform competitively with GPT-5-level performance.
      - **Monetization Model:** Free trial → paid plan based on usage credits.
      - **User Workflow:** Install MCP → Connect GitHub repository → Augment Code automatically indexes codebase → Context Engine provides intelligent code context to agent.
      - **Search Intent Strategy:** Target high-volume searches like "kilocode best models," "best MCP for agents," "cheaper models as good as GPT-5."

### Content Strategy & Programmatic SEO

  - **Current Content Mix:** 50% content refreshes (updates to existing high-performing articles) + 50% new content (comparison articles, alternative listicles, use case pieces).
  - **New Site Structure:** Content is being organized into thematic sections (e.g., `/tools` for all tool comparisons and listicles). This restructuring is already generating traffic lift.
  - **Programmatic SEO Opportunity — AI-Powered Code Wiki:** A community suggestion emerged to build an AI-powered code wiki as a hub for developer documentation.
  - **Augment Code's Internal Plan:** Augment Code is already building this wiki internally as a product demo/proof-of-concept for the Context Engine API launch.
      - **Rationale:** To demonstrate that Augment Code's Context Engine is superior to competing solutions (e.g., Cognition's "DeepWiki"), which suffer from accuracy issues and have gating restrictions on which repos can be indexed. Community comments on DeepWiki reveal significant inaccuracies and trust issues.

### Newsletter Experiment & Nurture Strategy

  - **Objective:** Test a newsletter as a nurture channel for expired trial accounts (users who signed up but didn't convert).
  - **Decision:** Proceed with experiment. Dominic Kent will create/manage content.
  - **Success Criterion:** A "decision gate" will evaluate performance metrics. Jason (GrowthX) believes newsletter isn't highest-leverage for direct conversion, but valuable if tied to dormant account reactivation.
  - **Scaling Plan (if successful):** Automatically enroll all expired trial accounts into the newsletter. Current estimate: potential of thousands of contacts per week from this source alone.
  - **Audience & Segmentation:** Newsletter currently targets AI enthusiast and professional developers. Future gated content (if deployed) will target enterprise buyers (CTOs, VPs) and use a separate nurture list to avoid mixing audiences.
  - **Constraint:** Gated content is not a priority for the developer audience, as developers resist paywalls and prefer open access.

---

## Action Items

**Jason Gong (GrowthX)**
- Add download CTAs across key bottom-of-funnel pages and articles to address 90% funnel drop-off
- Send Sylvain top 20 content summary covering the last 30 days, including ranking position, traffic volume, and signup metrics (even though accuracy is being QA'd)

**Sylvain Giuliani (Augment Code)**
- Share code review benchmark draft with Jason Gong; GrowthX will then draft comparison/alternatives content based on benchmarks
- Prioritize Context Engine MCP work with AJ (team member); then coordinate with GrowthX to map MCP search intent clusters and develop programmatic SEO strategy

---

## Transcript

**Jason Gong:** This meeting is being recorded.

**Marisol Smith:** Hi, Jason. Hi, Liz. You're on mute. I'm sorry. I just moved 500 of the keywords to the content OS. I am mapping them to the content strategy, and it generates the path. And I was trying to create a Looker Studio dashboard for the refreshes, for the metrics, but I will ask Vivek for help.

**Liz Kushnereit:** Okay. Yeah, we can communicate more, I think. Topic clusters specifically and what we're going to do there, but yes.

**Sylvain Giuliani:** Recording in progress.

**Jason Gong:** Recording in progress. How's it going?

**Sylvain Giuliani:** How much is that person — did that voice get paid from Zoom? Or is it like AI and nobody's getting paid?

**Jason Gong:** Or did they give their rights away for $5? Every time he says it, it's a couple of cents.

**Sylvain Giuliani:** I mean, that is a lot of money. I'll be the new voice if they want a French accent. You know, it's like ways you can download, like, a voice pack.

**Jason Gong:** If they want to just license Snoop Dogg's voice or something, that is probably what it costs.

**Sylvain Giuliani:** Oh, yeah.

**Jason Gong:** You're coming today, right? What?

**Sylvain Giuliani:** Huh? What?

**Jason Gong:** What?

**Sylvain Giuliani:** Is somebody coming?

**Jason Gong:** Is it just going to be me, Jason? Lot of people coming. Did we send the guests this? I don't remember if Gloria sent it out. Yeah, yeah, no, I think you did. It'll be a good time. Okay, cool. Let's just dive in.

**Jason Gong:** So we're tracking to the target. This week, traffic is doing well. But something's messed up with people downloading and we're looking into that. I feel like it lined up with all the website changes we rolled out. So I don't know exactly what the problem is, but take this article for example. It's ranking ninth for "AI coding systems," gets about 200 visits a week. It's totally bottom of the funnel. And it got only one install in the last week. So something's broken there.

**Sylvain Giuliani:** When you're saying that, you mean a signup, right?

**Jason Gong:** Yeah, I think a signup. I'm using PostHog event tracking for that.

**Sylvain Giuliani:** Right, which is what happens after the whole flow.

**Jason Gong:** Yeah, so you go through the website, then you go to the IDE, and it connects. When I was looking at the funnel, about 10% of people get to the final step, but then they don't make it to the end. There's basically no download link until you get to the very final step. Even when you get there, there's no link. So there's a lot of stuff to fix there. The traffic's good, but I think there's a lot of conversion things to do.

**Sylvain Giuliani:** We have an internal project to make PostHog our source of truth for data accuracy. That's literally the next project our analytics team is going to take on. The metrics might already be correct, but right now I can't say that with confidence because we haven't invested in QA for all the data that goes into those.

**Jason Gong:** Intuitively, from our side, there's a lot to do in the content, so we're prioritizing that. We've pulled some numbers and are tracking progress to them. I think we're showing up in a lot of prompts now. We're getting traction in the prompts we want. But a big jump is that we've started moving a lot of content to different sections on the website. All the listicles now live under `/tools`, and `/tools` is already getting a bunch of traffic. So good progress there. On our end, refreshes are working really well. We're doing half refreshes, half new content. Is that right, Marisol?

**Marisol Smith:** Yeah, we're doing that.

**Jason Gong:** Some of what we're doing — conversion is probably new from this week. I'm going to pay more attention to that. We're also doing screenshots, tables, restructuring, rewriting.

**Sylvain Giuliani:** Okay.

**Sylvain Giuliani:** Since we have Marisol on the call, what kind of content themes are coming up in the next three weeks? There's a lot of things changing in our product strategy, and I want to make sure we're aligned. I can also feed you more intel.

**Marisol Smith:** Yeah, we're going to be focused deeply on comparison articles and alternative listicles, based on the keywords Liz shared.

**Jason Gong:** Yeah, we went pretty deep on those. There's also use cases and best practices.

**Sylvain Giuliani:** Yeah, we're doing a lot there, too. The reason I asked is because there are two big things happening in December. I wanted to put that on your radar. We have the Code Review product launch, which will be self-serve. I can share content with you — we're running benchmarks. Our benchmarks show we're the best on code review compared to alternatives. Let's invest even more in comparison articles: Augment vs. Greptile vs. CodeRabbit — all those code review tools. I can give you the first draft of the benchmark. The numbers will likely improve, but in the initial benchmark, we're already better than them. You can start using that as the proof point. We'll have our own dedicated landing page for the benchmark you can use down the line. So that's one big launch we're having.

**Sylvain Giuliani:** The other big bet we're doing in December is releasing a Context Engine MCP (Managed Context Provider). The full API is a January release, but in December we're releasing the MCP version. This means you can make code smarter by using our context retrieval — you can plug into any coding agent. The thinking from our side is how do we get people using Kilocode to install our Context Engine MCP? The MCP has a free trial, but ultimately you pay with credits on a paid plan. So everyone searching for "Kilocode plus GLM 4.6," "Kilocode best models," "best MCP for clients" — how do we show up in those searches? This conversation just happened in the last 10 days, so it's not fully formulated yet, but there's already a lot of volume on those intents. We have a huge opportunity here because our messaging is strong: we make mid-level models like Kimi K2, GLM 4.6 perform as smart as Sonnet 4.5. We have benchmarks proving that. You can have a cheap model, and Augment makes it smart and as good as GPT-5. It's a big bottom-of-market opportunity.

**Jason Gong:** That'd be good for us. The MCP integrates with anything that supports arbitrary MCP integration, right?

**Sylvain Giuliani:** Yeah, there are a couple of things you have to set up behind the scenes — you still need code indexing — but the workflow is simple. You install the MCP, we say "connect your GitHub repo so we can index the code," and once that's done, it works out of the box. That's a huge new research intent we can create. This decision just came down yesterday, so this is fresh.

**Jason Gong:** That's a crazy move, opening up your product like that.

**Sylvain Giuliani:** The goal is to be part of a bigger platform where we're releasing APIs for people to build code agent capabilities. That's a big customer request. The Context Engine API will be the first API on that platform. That's the January thing.

**Jason Gong:** So for now, let's focus on these launches. We can map new clusters for the refreshes. We're also revisiting MCP, and we have some programmatic ideas. Marcel threw something over this morning — something about a code wiki. We found something interesting.

**Sylvain Giuliani:** Even Google's building AI code wikis now. That's something we're thinking of building ourselves internally as part of the Context Engine API launch. It's a way to prove we have the best context. Look at DeepWiki from Cognition — it's actually wrong. They don't let you add custom repos because they review things with human feedback to avoid showing incorrect information. But you read community comments on DeepWiki and there's a ton of misinformation. It's a big SEO play, but the context quality is weak. That's why it's a great product demo for us — showing our Context Engine is superior.

**Jason Gong:** Yeah, that makes sense. If you're building that internally, we can support on the SEO side if needed.

**Sylvain Giuliani:** Yeah, we have to use our own API, handle fraud vectors, make sure everything's fine. But that's the plan.

**Jason Gong:** Marcel has great intuition on these things. That's the learning here.

**Jason Gong:** On the newsletter — my take is it's probably not the highest leverage thing if we use it as just a conversion tool. I'd much rather push people to sign up directly. But I think it's valuable if you're thinking of doing something with all the dormant accounts you have. If you want us to help create content that nurtures those accounts, we can do it. Otherwise, I don't think it's the most helpful thing for conversion optimization. We'd probably come to it later. There are ideas, but I wouldn't prioritize them now.

**Sylvain Giuliani:** I like the idea to run it as an experiment. The decision gate makes sense to me. We want to do more things with Dominic Kent going forward, so there's no reason not to do this experiment. My other idea: if we pass the decision gate, let's sync all the expired trial accounts to the newsletter. Anyone who signs up and doesn't convert after 30 days gets added. It's a way to reactivate them and nurture them. That's how we grow the newsletter — calls to action from the website, events, content. We could add all non-converting people. That's probably thousands of people per week.

**Jason Gong:** Go for it. For enterprise, do you guys gate anything that works exceptionally well? That's probably the most effective way to add people to a newsletter.

**Sylvain Giuliani:** No, we don't gate anything. I don't believe in gated content for our developer audience. They hate that. We'll probably do gated content for CTOs and VPs, but the newsletter isn't made for those folks anyway. The newsletter is for AI enthusiast developers and professional developers. We started with the webinar program, so people from webinars can be added to the list. Let's do the decision gate first, and if that works, we can bring more people in.

**Jason Gong:** Any questions on your side, Liz?

**Liz Kushnereit:** No, I think we're moving forward with testing. That's my understanding, right?

**Jason Gong:** Okay, then all good. These site sections are up now, we're publishing into them to keep content organized, and it's working well.

**Sylvain Giuliani:** Yeah, right now the big thing is the Context Engine MCP is new and changed our priorities, so I need to prioritize work with AJ on that.

**Jason Gong:** Cool. We're doubling down on rewriting and content work since traffic is going in a good direction. After this meeting, can you send Sylvain a quick summary of the top 20 content pieces that performed in the last 30 days? Include ranking, traffic, and signups, even though we know the signup numbers might not be accurate yet.

**Sylvain Giuliani:** Yep, sounds good. Just send that async so I can review.

**Jason Gong:** Okay.

**Sylvain Giuliani:** All right. Thanks, gang. I appreciate the time. Bye.
