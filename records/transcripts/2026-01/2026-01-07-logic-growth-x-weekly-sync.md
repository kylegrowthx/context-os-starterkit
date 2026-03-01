# Logic <> Growth X - Weekly Sync

<metadata>
date: 2026-01-07
time: 18:30 UTC
duration: 29 minutes
organizer: Bailey Seybolt (GrowthX)
participants:
  - Azzam Aijazi (Logic)
  - Bailey Seybolt (GrowthX)
  - Steve Krenzel (Logic)
fathom_recording_id: 112513238
fathom_url: https://fathom.video/calls/522936344
share_url: https://fathom.video/share/GP3pSi2CH2WUBc6rbXG54_ec2A_Fh6ZM
source: fathom
enriched_on: 2026-02-28T17:42:00Z
context: Weekly strategy sync between Logic (AI automation platform) and GrowthX (content marketing partner) to align on content positioning, product terminology changes, and calibration strategy.
</metadata>

---

## Summary

Bailey Seybolt (GrowthX) and Azzam Aijazi (Logic) aligned on critical content strategy updates following Logic's 12-day content push during the holidays. The team addressed misalignment in calibration articles (which lean toward build-first troubleshooting rather than "build vs. buy" positioning), introduced new product terminology ("Agent" and "Spec" replacing "Document"), and updated writing guidelines to use relative timelines instead of specific numbers and avoid model-specific references to prevent content staleness.

---

## Context

Logic is in an active content strategy pivot after launching 12 days of viral content over the holidays, which drove significant user acquisition and included a successful new AI-generated image style. GrowthX is supporting Logic's content marketing efforts with $200k+ calibration articles designed to frame automation as a "build vs. buy" decision, positioning Logic as the superior solution to building custom automation in-house. The partnership is at a critical calibration phase—articles are being refined for clarity and positioning, and new product terminology is being systematized across all content to unlock new SEO opportunities around "agent frameworks" and agent-building platforms.

---

## Relevance

- **Content Strategy (GrowthX):** Calibration article refinement, writing guideline updates, image generation pipeline integration, keyword research expansion
- **Product Positioning (Logic):** Transition to "Agent/Spec" terminology for SEO and user clarity, competitive differentiation against Langchain and other frameworks
- **Content Marketing:** New AI image style replication, FAQ length management, model-agnostic language updates, moving from specific timelines to order-of-magnitude language
- **Operations:** Weekly sync to bi-weekly cadence pending content stability, Airtable topic review for keyword research pipeline, collaborative content delivery timeline tracking

---

## Overview

- **Content Misalignment:** Calibration articles miss the "build vs. buy" premise, focusing instead on technical troubleshooting for a build-first approach.
- **New Terminology:** Product units are now "Agents" (the API-callable output) and "Specs" (the long-form instructions), replacing the ambiguous term "document."
- **Writing Guideline Updates:** Content will use relative timelines (e.g., "days vs. weeks"), avoid specific model numbers (e.g., GPT-4), and adopt a new AI-generated image style.
- **New Cadence:** Weekly syncs will shift to a bi-weekly schedule once the new content strategy is stable, with weekly project updates moving to Slack.

---

## Key Topics

### Content Strategy & Calibration

- **Problem:** Calibration articles miss the "build vs. buy" premise from their titles.
- **Analysis:** Content is skewed toward technical troubleshooting for a build-first approach, not a high-level comparison.
- **Root Cause:** A potential mismatch between the article's top-of-funnel goal and the technical persona it targets.
- **Solution:** Revise the article to frame building as a difficult path, then position Logic as the superior "buy" alternative. A second calibration article will also be created.

### New Product Terminology

- **Change:** "Document" is replaced by "Agent" and "Spec" for clarity and SEO alignment.
- **Rationale:** The term "document" was ambiguous, referring to both the API-callable output and the text-based instructions.
- **Definitions:**
    - **Agent:** The API-callable unit created in Logic.
    - **Spec:** The long-form instructions (schemas, APIs, tools) that guide the Agent's behavior.
- **Impact:** Unlocks new SEO opportunities by targeting keywords like "agent building platforms" and "agent frameworks."

### Writing Guideline Updates

- **Timelines:** Use relative terms (e.g., "days vs. weeks") instead of specific numbers (e.g., "8 weeks").
    - **Rationale:** Specific numbers are often unbelievable to engineers.
- **Model References:** Avoid specific model numbers (e.g., GPT-4).
    - **Rationale:** Models quickly become outdated, making content look stale.
- **Image Style:** Adopt a new AI-generated style developed during the "12 days of content" push.
    - **Rationale:** The style is editorial and human-like, avoiding the "AI slop" feel.
    - **Implementation:** GrowthX will test replicating the style in their pipeline using Logic's "spec" document.

### Operational Updates

- **Airtable Review:** Azzam to review ~25 new article topics in Airtable by tomorrow.
    - **Purpose:** Feedback will inform the next round of keyword research and help resume the 5-article/week cadence.
- **Meeting Cadence:** Syncs will shift from weekly to bi-weekly.
    - **Timing:** The change is on hold until the new content strategy is stable.
    - **New Format:** Live syncs → Strategy & performance; Slack → Weekly project updates.

---

## Action Items

**Bailey Seybolt (GrowthX)**
- Update writing guidelines to reflect agents/specs terminology, order-of-magnitude timelines (days vs. weeks), and exclude specific model numbers (GPT-4, etc.)
- Revise calibration articles to use agents/specs language and strengthen "build vs. buy" framing; send revised version to Azzam for approval
- Send Slack recap of meeting to Azzam and Steve with key decisions and timeline expectations

**Steve Krenzel (Logic)**
- Share the image-style Logic spec/agent documentation to Bailey for GrowthX integration testing
- Coordinate with Bailey on image generation pipeline integration; share preliminary results once GrowthX tests the style in their system

**Azzam Aijazi (Logic)**
- Review approximately 25 new article topics in shared Airtable and provide feedback (approve/comment) by January 8
- Deliver second calibration article with alternative "build vs. buy" framing to Bailey by January 8 for review

---

## Transcript

**Azzam Aijazi (Logic):** This meeting is being recorded.

**Bailey Seybolt (GrowthX):** Hey, happy new year, Logic team.

**Azzam Aijazi:** How are you doing?

**Bailey Seybolt:** I'm good. How are you all doing?

**Azzam Aijazi:** Can't complain. Life's good.

**Steve Krenzel (Logic):** Hey, happy new year. You were in the Galapagos, right?

**Bailey Seybolt:** Yes, I was. It was so amazing. I feel like I'm now trying to remember who I am and what I do—not just someone who wakes up and snorkels with sea lions every morning.

**Steve Krenzel:** Nice.

**Bailey Seybolt:** It was pretty awesome. I didn't realize the degree of uniqueness in the ecosystem. We slept on a boat, waking up on a new island every morning. There were naturalists on the boat who really put everything into context. It was a bucket list trip for sure.

**Steve Krenzel:** They pretty heavily regulate the number of people that can visit.

**Bailey Seybolt:** Yeah, it's really heavily regulated—which islands, how many people on the islands at one time. And even the companies are regulated on how often they can take people.

**Steve Krenzel:** Like they can't revisit the same site more than once every two weeks.

**Bailey Seybolt:** Everything is limited and regulated, which is amazing for the impact on the ecosystem. But it can certainly make planning tricky.

**Steve Krenzel:** Yeah. Very special trip.

**Bailey Seybolt:** Galapagos gets a gold star from me. How about you all? Did you have a nice, restful holiday?

**Steve Krenzel:** Yeah, it was good. Stayed local in Seattle, but tons of back-to-back celebrations.

**Bailey Seybolt:** Usually we stay local for the holidays. This was out of the ordinary for us. I feel like that's more restful. Sometimes when you do a big trip, you need a recovery from your vacation.

**Bailey Seybolt:** All right. Let me share our agenda.

**Bailey Seybolt:** So in terms of content, let me jump into the calibration doc. I think we're getting close on calibration. Azzam, I reviewed it—I know Rachel made some updates, and I also took a look at your feedback. It seems like where we're still falling short is in positioning Logic more explicitly in the content. It reminds me of before our first round of content, where we had to do a little more work on redefining what automation was and making sure Logic fits into that conversation, especially in comparison articles like "Zapier versus Logic."

**Bailey Seybolt:** We need to be more explicit about how we define the "build versus buy" conversation and position Logic clearly.

**Azzam Aijazi:** I think the positioning of Logic itself is good when I just read the parts mentioning Logic. My concern is the setup of the article itself. The first pass was all about how you'd build it yourself, and then Logic was an afterthought—"if you want to just use Logic instead, you can do that too." It didn't feel compelling. This one is much better on that axis, but the content still doesn't quite match the title premise. The title's great, the way Logic is described is great, but there's a mismatch. It still leans toward how you'd build it yourself. I had in mind something like: here's a problem you have to solve. Two ways to do it. Here's what building looks like. Here's what buying looks like. Pros and cons of both. If you're going to buy, Logic is the best option. Here's why. Right now it's still leaning toward troubleshooting after you've decided to build.

**Bailey Seybolt:** I agree. The content isn't totally matching. It's over-indexing on problem-solving for building rather than a high-level "build versus buy" comparison.

**Azzam Aijazi:** Yes, it's more like troubleshooting for a build-first approach. We should frame it differently: if you're earlier in your journey and haven't decided what to do yet, looking into what building takes, here's what you might not realize about how hard it will be. Let's lay out the pain if you choose to build.

**Bailey Seybolt:** That makes sense. Some of this may be because we're looking at the SERP and keyword and trying to match that to personas. We might be over-indexing on technical content for a technical persona versus a higher-level build versus buy conversation. We may need to adjust personas to make it clear that top-of-funnel content can be high-level. I think we'll update this, and I still think a second calibration article would be valuable.

**Azzam Aijazi:** Yeah, absolutely. One thing I wanted to call out is we've decided to stop calling the unit of things Logic creates a "document." We're calling it an "agent" now. Logic creates agents. You call the agent via an API and embed it into workflows. It's a more natural way to refer to this, easier to understand, and avoids confusion where you're processing documents using a document.

**Steve Krenzel:** When an agent is composed of things like schemas, APIs, and tools, we're calling the content of the agent a "spec." As we shift to a more technical audience, this is the vocabulary they use, so they can draw lines more quickly.

**Azzam Aijazi:** When you go into Logic and create something, you've created an agent, guided by a spec—written instructions you provide. In other places you might see "prompt," but we call it a spec to show it can be longer-form, with appendices. It's not just a little text box.

**Bailey Seybolt:** Makes sense. Were we using Logic Docs and Workflows interchangeably? Do we want to talk about both in terms of creating an agent?

**Azzam Aijazi:** Yes. We unfortunately used "document" in two different ways: the thing you plug into a workflow, and the text you edit that controls behavior. We called both "docs," which makes sense once you get it, but isn't obvious. So the simple rule is: you create an agent and you write the spec.

**Steve Krenzel:** You create an agent and you write the spec.

**Bailey Seybolt:** Super simple. We'll update our writing guidelines to make sure this is clear and update the calibration articles to use the right terminology.

**Azzam Aijazi:** Another thing—I noticed we use language like "you thought it would take two days, you scheduled two weeks, and now you're in week eight." That's cool and evocative, but people don't believe specific timelines. They think "eight weeks, not BS—that would never happen to me." I lean toward saying "days or weeks" instead of specific numbers. It's more believable to engineers.

**Steve Krenzel:** Yeah, orders of magnitude rather than precise numbers.

**Bailey Seybolt:** That makes sense. AI loves to attach specific timelines. We can explicitly steer it away from that in writing guidelines.

**Azzam Aijazi:** And one more thing: stop referring to specific models. Don't mention GPT-4 or any model with a number. Just say GPT, OpenAI, Anthropic. These become outdated in three months and make content look stale.

**Bailey Seybolt:** Good callout. We'll update writing guidelines for that too.

**Bailey Seybolt:** I noticed articles are getting longer with FAQs included, but at around 2,500 words, it's not a big concern. With AEO versus SEO, longer thorough articles are more likely to get cited and push up LLM traffic, so length seems fine for now.

**Azzam Aijazi:** I mentioned before the break we did a 12 days of content push over Christmas to New Year. It was a ton of work and went really well. Some articles went viral on Hacker News. We got sponsored content pointed to it, and got new users. Over that time, we developed an image style. We encoded this style into a Logic agent and had Logic generate images using Nano Banana. These are all AI-generated. We got good feedback that the art was really good. With a little prompting and encoding the style this way, we can say: every 500 words, make sure there's at least an image. With the Logic agent embedded for preview, it should break up long text and avoid monotony.

**Bailey Seybolt:** I love this style. It feels very illustrative and editorial in a way that doesn't feel like the typical tech design feel. Very human. These are cool. I'm wondering if you want to share what generated them. I could share that with our designer and see if we can build it into our image generation pipeline so images automatically generate with content.

**Azzam Aijazi:** I'm a fan because it looks hand-drawn. The more we do to avoid AI slop, the better.

**Steve Krenzel:** It looks human and hand-drawn, but it's fuzzy enough that weird artifacts look like watercolor strokes. We can send you the doc we wrote to generate these and see if your system can replicate it. If not, we could insert a Logic image tag and post-process it.

**Bailey Seybolt:** Why don't you share the Logic doc. If our pipeline can create it, especially once we have automatic publishing, that's one less step for you.

**Steve Krenzel:** Let's take a stab at it and see what we come up with.

**Azzam Aijazi:** And Steve, any concern about costs?

**Steve Krenzel:** No, these were about two to three cents per image generation.

**Bailey Seybolt:** We'll test it. On our end, we usually generate at least five options and pick the best, but as we nail down the style, we can include all of them.

**Azzam Aijazi:** What does your pipeline look like for image generation? Maybe we share a prompt or style, and you use whatever tools you're using already.

**Bailey Seybolt:** Recently they've been building on GPT. I know they made updates to improve it. If you share what you created with Logic, I can add our art designer.

**Bailey Seybolt:** So I was going to flag that we updated some articles with new positioning, but don't look at those yet. Given the new naming conventions—agents and specs—we should revise the articles to be consistent.

**Azzam Aijazi:** I appreciate you hanging in as we're moving rapidly. Every time we push forward and see it in action, we realize something isn't quite there yet and we adjust and improve.

**Bailey Seybolt:** From the outside, this pivot has been very streamlined and organized compared to other companies I've seen. We're happy to be on the journey with you.

**Bailey Seybolt:** In terms of what's coming down the pipeline, we need you to view the new Airtable. We have a first round of about 25 articles. Leave some feedback—approve topics, leave comments. This will help us hone the editorial calendar and inform our next round of keyword research.

**Azzam Aijazi:** I skimmed through them. I can thumbs up or thumbs down them by tomorrow. Is there a number I should hit?

**Bailey Seybolt:** I think we want to get back to five a week, hopefully next week. In this first round, it's also about positioning—not just right keywords, but right framing for each article. Feedback helps us do better rounds.

**Azzam Aijazi:** Going from "documents" to "agents" will unlock new SEO. Now people searching for "agent building platforms" will find us. Competitors like Langchain already use this language.

**Bailey Seybolt:** Do you have concerns about clarifying where Logic fits in with agentic AI?

**Azzam Aijazi:** No. We're updating the website to better frame how Logic works, but if people jumped straight into the product, it's intuitive. The mental model fits well.

**Bailey Seybolt:** This will unlock new keywords around agent building. It could also unlock ChatGPT recommendations for agent frameworks—that'd be a win.

**Azzam Aijazi:** Our goal is to grow like hell and have SEO and AEO be major parts of inbound. So far, this aligns with that.

**Bailey Seybolt:** For you, we've been having many of these conversations as we pivot. Separate session may not be needed yet, but if things shift, especially as we see performance, we can talk later.

**Bailey Seybolt:** One ops thing: we're shifting to biweekly cadence for check-ins to focus on strategy and insights versus project management. We'll wait until end of month—there's a lot going on and we should be solid on the new content stream first. We'll still do weekly Slack updates covering project management, then focus live syncs on reporting, insights, and performance.

**Azzam Aijazi:** Yeah, let's wait.

**Bailey Seybolt:** Anything else on your minds?

**Azzam Aijazi:** No.

**Bailey Seybolt:** I'll send a Slack recap since we have a bunch of action items.

**Azzam Aijazi:** We should have the second calibration article to you hopefully today, but I'll check in with Rachel. It may be today or tomorrow.

**Bailey Seybolt:** Thanks a bunch, everyone.

**Azzam Aijazi:** Bye.

**Bailey Seybolt:** Bye.
