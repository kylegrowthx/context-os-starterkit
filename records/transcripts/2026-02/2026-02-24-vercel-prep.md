# Vercel prep

<metadata>
date: 2026-02-24
time: 20:33 UTC
duration: 26 minutes
organizer: george@growthx.ai
participants: George Haikal, Marcel Santilli
fathom_recording_id: 125029207
fathom_url: https://fathom.video/calls/579541630
share_url: https://fathom.video/share/TYTDfyqJvXzagg2M2LVX9DnN__4kWPjm
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

George and Marcel finalized kickoff questions for Vercel's AI Gateway project, covering goals, competitor research, current content workflows (AROPS), and team collaboration. The core strategy is to dominate search for new AI model pricing and comparisons (e.g., "Claude Opus 4.6 pricing") by building a structured content hub with dedicated model provider cards, pricing pages, and comparison pages. Execution is urgent: a forward-deploy engineer must start immediately to avoid churn, and Marcel will prototype model pages and workflows for George before kickoff.

---

## Context

GrowthX is preparing for kickoff with Vercel, a major platform-as-a-service provider. Vercel operates AI Gateway, an open-source tool for routing API calls across multiple LLM providers, and is looking to dominate search visibility for AI model pricing and comparisons. Marcel (external, likely the Vercel point of contact or strategist) and George (GrowthX strategist) are finalizing the kickoff questions and alignment strategy. The engagement requires immediate execution to avoid churn risk — a forward-deploy engineer named Tammy must start work immediately, not wait 3 weeks, or the project will likely stall.

---

## Relevance

**To GrowthX Delivery:**
- Vercel's core pain point: generic AI Gateway pages underperform in search. Current Opus 4.6 pricing page has pricing buried in a table; a changelog ranks higher than the official page.
- Strategic approach: build a structured content hub with dedicated model provider cards, pricing pages, comparison pages (e.g., Vercel vs. Render), and FAQ pages — modeled after CheckThat's structure.
- Immediate need: execute workflows and prototype model pages before kickoff (3-week delay risks churn). Forward-deploy engineer Tammy must start now, not in 3 weeks.

**To GrowthX Business Development:**
- Vercel has internal team attending kickoff: Tristan, Eric, and Dan (plus other stakeholders). Kickoff questions designed to understand their workflow, current use of AROPS for content production, and relationship with freelancer John Henry.
- Competitors identified: Render (performing well), plus others Vercel cares about. Need to validate competitor list during kickoff.
- High-intent search strategy: dominance for "Claude Opus 4.6 pricing", "AI Gateway Opus 4.6", and similar model-specific searches is the core moneymaker.

---

## Decisions & Commitments

- **Kick-off questions finalized** with sections covering AI Gateway project, indexing strategy, AEO/AI visibility, and competitive landscape. George will send to Tristan, Eric, and Dan.
- **Strategic approach confirmed**: GrowthX will be the strategist, not just the executor. The team will proactively define the content roadmap rather than waiting for Vercel to prescribe requirements.
- **Execution timeline**: Tammy (forward-deploy engineer) must begin work immediately post-kickoff, not in 3 weeks. Speed is critical to avoid churn.
- **Post-kickoff gameplay session**: George and Marcel will schedule 30 minutes to play through the strategy and move fast on implementation.

---

## Open Questions

- Which specific competitors does Vercel consider their primary threat? (Render confirmed, others TBD)
- What pain points is Vercel experiencing with AROPS, and are there other tools/services they're using for content production?
- Will Vercel continue collaborating with freelancer John Henry, and if so, how should GrowthX coordinate with him?
- What success metrics will Vercel use for the AI Gateway content hub (traffic, rankings, conversion)?

---

## Overview

- **Kickoff Prep:** Kickoff questions are ready, covering goals, competitors, and current content workflows (e.g., AROPS, freelancer John Henry).
- **Strategic Focus:** The core strategy is to dominate search for new AI models (e.g., "Claude Opus 4.6 pricing") by creating high-quality, structured pages.
- **Urgent Risk:** The project is at risk of churn due to the need for immediate execution. A forward-deploy engineer (Tammy) must start work now, not in 3 weeks.
- **Content Plan:** The strategy requires building a structured content hub with dedicated pages for pricing, comparisons, and FAQs, moving beyond generic overviews.

---

## Key Topics

### Kickoff Prep & Questions

  - George created kickoff questions to align on Vercel's goals, covering:
      - AI Gateway project
      - Indexing strategy
      - AEO & AI visibility priorities
  - **Key Questions for Vercel:**
      - **Competitors:** Validate the pre-researched list (e.g., Render) and identify their top-of-mind concerns.
      - **Current Content Workflow:** Understand their use of AROPS and other tools.
          - **Goal:** Uncover pain points to position our service as a direct replacement.
          - **Question:** "What is AROPS doing for you, and where can it be improved?"
      - **Collaboration:** Clarify the relationship with freelancer John Henry.

### Strategic Focus & Urgency

  - **Primary Risk → Churn:** The project requires immediate execution. A 3-week delay for a forward-deploy engineer (Tammy) would likely cause churn.
  - **Strategic Mandate:** We are the strategists, not just executors. We must proactively define the path to success.
  - **Core Strategy → Dominate Search for New AI Models:**
      - **Goal:** Rank \#1 for high-intent searches (e.g., "Claude Opus 4.6 pricing").
      - **Rationale:** Vercel's current pages are weak and underperform.
          - **Example:** A changelog ranks above the official AI Gateway page for "AI gateway Opus 4.6."
          - **Problem:** Pricing is buried in a table, not a clear feature.

### Content Strategy & Structure

  - **Solution → Build a Structured Content Hub:**
      - **Model Provider Cards:** Create detailed, cross-linked pages for each model, similar to CheckDat's format.
      - **Dedicated Pages:**
          - `/pricing`: A clear, dedicated page for pricing details.
          - `/comparisons`: Head-to-head articles (e.g., `ai-gateway/comparisons/vercel-vs-render`).
          - `/answers` or `/faq`: A hub for common questions.
  - **Pre-Call Research:** George has already loaded the CheckDat workspace with:
      - AI Gateway docs
      - Guillermo's voice/tone analysis
      - Initial product overview

---

## Action Items

**Marcel Santilli**
- Review Vercel kickoff Qs; add missing items for Tristan, Eric, Dan
- Draft AI Gateway workflows; prototype model pages w/ pricing/comparisons/FAQs for George

**George Haikal**
- Schedule 30-min gameplay session w/ Marcel post-kickoff

---

## Transcript

**George Haikal:** Hey, what's up? I got you now.

**Marcel Santilli:** All right, cool.

**George Haikal:** How's it going?

**Marcel Santilli:** Good, crazy, but good. The camera looks way clearer than it usually is.

**Marcel Santilli:** Yeah, Will set me up with a DSLR today.

**George Haikal:** Okay, move it a little lower so your head's more in frame. If you get closer, you get too much.

**Marcel Santilli:** The monitor is right here, and the camera is kind of right here, so if you go any lower, you hit the monitor.

**George Haikal:** Yeah, it doesn't feel like you're talking directly to me. It doesn't matter for these. Your eyes are down a little bit the whole time.

**George Haikal:** So I kind of just want to jump into it. Everything's on the calendar invite, but let me show you what I did. Here are the questions I want you to review before the call. I didn't want to get too prescriptive, but I added sections for the AI Gateway project, indexing strategy, and AEO/AI visibility. From our earlier call, it sounded like he's doing some work internally, and I want to know what he cares about there. It's such a big space with so many options. I just sent you the link.

**Marcel Santilli:** I'm sharing my screen now.

**George Haikal:** These are the kickoff questions. This is the key thing I want you to review and add anything missing based on your conversations with him. I kept it broad because I do want to check in and understand his goals. They don't have customer docs yet or ICP messaging yet, but they said it'll be ready in March. I want to hear which competitors they care most about. I did research and added these to CheckThat, but I want to hear what's top of mind for him.

**Marcel Santilli:** Is it just him joining or other people?

**George Haikal:** There's two other people, Eric and...

**Marcel Santilli:** Dan didn't accept. It's Tristan and Eric. So I'm looking at the type of content here — how should we narrow that down?

**George Haikal:** Yeah, I looked at that too. For the type of customer we're creating content to reach, who really is that? What's happening to them? The focus is different for each project.

**Marcel Santilli:** That makes sense.

**George Haikal:** I think we'll still get the numbers here. What pressures are they facing? What metrics are moving?

**Marcel Santilli:** What are they feeling? Who are "they"?

**George Haikal:** Anyone who's...

**Marcel Santilli:** Okay, just making sure there's no other stakeholders.

**George Haikal:** Beyond that, their CheckThat workspace is set up. I did a ton of research on their AI Gateway feature from all their docs. The only customer information they had was the platform company archetype, but we need more. I also researched Guillermo extensively — his LinkedIn, X, blogs — to understand his voice, brand, and how he wants to come across. I broke it down by platform and tone. Then I scraped their docs to create an initial product overview we can research further. Those are all loaded in, and I created their CheckThat workspace.

**Marcel Santilli:** They're getting competitive. Render is doing really well, and we use Render a lot too. But Vercel built a lot of features like AI Gateway, the AI SDK, and open-sourced shadcn. Next.js is super widely used on the web. They have a lot of open source projects. Their core service is a hosting platform on top of AWS, but it's obscenely expensive. If you're hosting a massive app on Vercel, you're paying three to four times what you'd pay on AWS.

**George Haikal:** How were they using AROPS before? What wasn't working?

**Marcel Santilli:** From the sales call, they might still be using it. We want to position ourselves as a replacement they can switch to after we set them up.

**George Haikal:** I don't know what wasn't working for them with AROPS from the transcripts.

**Marcel Santilli:** We could ask: what is AROPS doing for you? Is it breaking down anywhere? Where can it be improved? Are there other tools you're using for content production? Start broader.

**George Haikal:** Remove the "what would better than AROPS look like in the first 30 days" question.

**Marcel Santilli:** Right, it's awkward to ask about AROPS on the kickoff. Let them mention how they're using it, what else they're doing for content, what tools they're using. Are there other agencies or service providers? For example, he mentioned using John Henry, a freelancer who's super respected. He wants us to play nice with them.

**George Haikal:** It makes sense. How are you feeling about it?

**Marcel Santilli:** Good, but we need the right capacity. The workflows for AI Gateway should be done already. If we wait three weeks for a forward-deploy engineer, they'll churn for sure. Speed is obscenely important. If we don't have capacity now, we're already two weeks behind.

**George Haikal:** I talked to Tammy's manager. Tammy can run it, but I need to be clearer on what exactly it is.

**Marcel Santilli:** This is such a clear use case, like the MCP one. We didn't wait for anyone to give us the MCP requirements. We know what we need to do to rank number one for it. We're the strategists, not them. They want to rank number one for all model names and every search about them, as soon as they launch. So: how do we create these pages and enrich the information?

**George Haikal:** When someone searches "Claude Opus 4.6", how do we get Vercel's page to show up? That's the answer.

**Marcel Santilli:** For instance, what search variants exist for Opus 4, 4.6, pricing? Number two for "Claude Opus 4.6 pricing" is Reddit. Number three is CodeAcademy. Vercel should be number one or two. If you search "AI Gateway Opus 4.6", their changelog ranks first — not their actual page. That's insane. The page itself is just one paragraph. There's nothing. The pricing is buried in a table in an "output" column next to "input". It's not obvious. That's the strategy: figure out all the search variants, understand the volume, improve the page structure, and create FAQ sections like "/answers".

**Marcel Santilli:** Generic overview pages don't perform well. Pricing drives most of the traffic. We can do comparisons like we did for Ramp vendors — "/comparisons/vercel-vs-render", etc. Every comparison uses the same data, so they all need to follow the same approach.

**George Haikal:** That makes sense. Dan accepted the kickoff invite.

**Marcel Santilli:** I'll prototype something too. Any gaps from CheckThat so far?

**George Haikal:** CheckThat workspace is created. The competitors section was wrong initially — the public data wasn't accurate. I added the competitors I know he cares about from our calls, but I didn't have time to prune the prompts that don't apply.

**Marcel Santilli:** There are duplicate workspaces. Why not enroll all admins through the admin panel instead of inviting them individually?

**George Haikal:** You have to use the admin panel so they don't have to accept terms. I added us three from the admin panel.

**Marcel Santilli:** Everyone showed up in the users list. We can clean it up later.

**George Haikal:** Right. After the kickoff, we'll need 30 minutes for gameplay so we can move fast on implementation.
