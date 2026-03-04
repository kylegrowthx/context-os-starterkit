# Blaxel <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-12
time: 19:59 UTC
duration: 33 minutes
organizer: team@growthxlabs.com
participants: Aida Knezevic, Carly Piekos, Nicolas Lecomte, Paul Sinaï
fathom_recording_id: 122090601
fathom_url: https://fathom.video/calls/564313439
share_url: https://fathom.video/share/M2DPsgpXwjjT6b7yBCX3XuDgLXxnzCj9
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Review content pipeline improvements and define a strategy for AI search visibility.

---

## Context

Blaxel is a cloud development platform specializing in persistent sandboxes and Agent Drive, a storage solution optimized for AI agents. GrowthX is running a content marketing engagement for Blaxel focused on AI search visibility (via ChatGPT, Claude, Cursor, and similar tools) alongside traditional SEO. This weekly sync covers content pipeline improvements, article delivery status, and strategy refinement for targeting high-intent keywords around AI agent persistence and storage. Paul Sinaï (CEO) and Nicolas Lecomte (Growth & Product) lead Blaxel; Aida Knezevic (GrowthX) manages content, with support from Carly Piekos (GrowthX) on CheckThat prompt analysis.

---

## Relevance

- **To GrowthX Delivery:** V3 of the agentic article generation pipeline is now live, incorporating EXA research, Blaxel's product feature matrix, and quality gates (factual accuracy, no banned AI phrases, no unsourced claims). GrowthX should integrate Blaxel's GitHub documentation and support.blaxel.ai knowledge base into the research step for organic product mentions.

- **To CheckThat:** Blaxel's visibility is 1.5% (E2B competitor is at 7.1%). Action item: export and audit tracked prompts to remove broad, irrelevant queries that dilute performance metrics. Priority keywords: "persistent sandboxes," "stateful sandboxes," "agent context persistence," "storage."

- **To GrowthX Business Development:** Blaxel's upcoming Agent Drive feature aligns with emerging demand from LLM tool use (per Anthropic's recent paper). Content strategy is shifting to bottom-of-funnel listicles and comparisons. Paul requested a 3-6 month visibility growth target and roadmap in the next sync with Kyle and Talal (GrowthX forecasting team).

---

## Overview

- **New Content Pipeline:** GrowthX launched V3 of its article pipeline to fix quality issues (e.g., inaccurate product info), ensuring content is now fact-checked against a product feature matrix.
- **AI Search Is Top Priority:** Blaxel's primary goal is to dominate AI search (via ChatGPT, Claude, etc.), not traditional SEO. The immediate focus is on keywords like "persistent sandboxes" and "agent context persistence."
- **Check That Performance:** Blaxel's 1.5% visibility is flat. The next step is to analyze the tracked prompts to remove irrelevant ones that dilute the data and skew the performance metric.
- **New Content Focus:** The strategy will shift to bottom-of-funnel content (product listicles, comparisons) and educational posts on key persistence concepts, leveraging Blaxel's upcoming "Agent Drive" feature.

---

## Key Topics

### Content Pipeline & Quality Control

  - **Problem:** Previous articles required full rewrites due to factual errors (e.g., incorrect GPU capabilities), indicating a flawed content pipeline.
  - **Solution:** GrowthX launched V3 of its agentic article generation pipeline to improve quality and accuracy.
      - **Researcher:** Now uses EXA (vs. baseline Tavilli) for better research on technical topics.
      - **Fact-Checking:** Incorporates Blaxel's product feature matrix during research to ensure content aligns with product capabilities.
      - **Quality Gates:** Articles are graded against a rule set to prevent errors like unsourced claims or patronizing links.
  - **New Content Sources:** Blaxel will provide its documentation and knowledge base to enrich the AI research process.
      - **Documentation:** Public GitHub repo via Mintlify.
      - **Knowledge Base:** `support.blaxel.ai` (built on Pylon).

### AI Search Performance & Strategy

  - **Context:** Blaxel's target audience uses AI tools (ChatGPT, Claude, Cursor) to find solutions, making AI search visibility the top priority.
  - **Check That Performance:** Blaxel's visibility is 1.5% (vs. competitor E2B's 7.1%) and has been flat.
      - **Hypothesis:** The performance metric is skewed by tracking too many broad, irrelevant prompts.
      - **Action:** GrowthX will export and analyze the prompt list to identify and remove low-value queries.
  - **Keyword Focus:** The strategy will target keywords reflecting high-intent user needs, even if they lack traditional search volume.
      - **Keywords:** "persistent sandboxes," "stateful sandboxes," "agent context persistence," "storage."
      - **Rationale:** These terms are emerging in user conversations and social posts, driven by papers like the recent one from Anthropic on LLMs and tools.
      - **Blaxel's Advantage:** The upcoming "Agent Drive" feature (a Google Drive for AI agents) directly addresses these persistence needs.

### Content Delivery & Performance

  - **Delivery Pace:** The pace of new articles slowed while GrowthX built the new pipeline.
      - **Catch-up:** 5 new drafts are in the editing queue for delivery today/tomorrow.
      - **Revisions:** 3 articles are finalizing revisions; Natalie will request final sign-off.
  - **Article Performance:**
      - The "Code Sandbox alternative" article is performing well, driving clicks and ranking high in Google Search Console.
      - Blaxel's own analytics (Posthog) confirm this article is getting the most traffic.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Integrate Blaxel docs (GitHub) and KB (support.blaxel.ai) into article pipeline
- Consult Kyle & Talal re: AI search visibility targets; prep for next sync w/ Paul & Nicolas

**Nicolas Lecomte (Blaxel)**
- Convert Content Ideas doc to table (idea, URL, date)
- Build MVP CTA banner w/ PostHog tracking; notify Aida when live

**Carly Piekos (GrowthX)**
- Export and review CheckThat prompts; remove irrelevant; identify gaps

---

## Transcript
---

### Introductions and Context

**Nicolas Lecomte:** So yeah, we're two of the co-founders of Blaxel. Paul is the CEO and I'm running growth and product. So, yeah, it's mostly us working with you guys on the content. Plus, we have somebody in-house. His name is Vikram and he does our technical content as well — documentation, blog posts, that kind of stuff.

**Paul Sinaï:** Yeah, I'm Paul. I'm the CEO of Blaxel. I'm mostly technical and in charge of the business side. My background is as an entrepreneur. Blaxel is my third startup. I sold the previous one to the largest European cloud provider. I live in San Francisco.

**Nicolas Lecomte:** I'm based in New York, but I'm doing back and forth between New York and SF. The HQ and team is mainly in SF, and that's where we're hiring all our future growth and engineering teams.

**Carly Piekos:** Great. I'm really happy to join the team and I can't wait to build out your strategy.

---

### Main Discussion

**Aida Knezevic:** Well, I wanted to get us started with some pipeline updates because the last round of articles that we delivered had a couple that had to be completely rewritten. That's always a red flag for us because it means the pipeline isn't doing what it's supposed to be doing.

**Aida Knezevic:** So we spent some time developing a brand new pipeline and adding additional steps to the workflow to prevent these issues from happening again. The new pipeline, for example, should no longer suggest that Blaxel can do GPU compute or model training. Moving forward, it should also reference all Blaxel products that are relevant to the specific topic being covered, not just sandboxes. We revised the article generation pipeline to incorporate your product feature matrix during the research step. That allows the researcher to find information that's relevant to Blaxel's benefits, not just general information for that specific topic.

**Aida Knezevic:** So the researcher isn't just taking the topic we've given it, but it's also looking at your company context to research additional information so that we can incorporate Blaxel in a more organic way.

**Aida Knezevic:** So to show you what that looks like in practice, this is V3 of the agentic article generation pipeline. We're using EXA as a researcher. EXA is the most advanced researcher we use — we use it whenever we're dealing with technical topics. Typically, we use Tavilly as the baseline we start with, and then if we notice it's not working, we try EXA instead.

**Aida Knezevic:** So the articles are graded against a quality checklist based on feedback from your team. It includes banned AI phrases and banned corporate language to keep things authentic and natural.

**Paul Sinaï:** We have both documentation and a knowledge base we could leverage. Our documentation is using Mintlify and is plugged into our GitHub public repository, so you can access the entire documentation in Markdown format, which works well with agents. We're also using Pylon for support. And we have support.blaxel.ai where there are specific posts about workarounds and guides that aren't in the main documentation but can still be relevant to how people use our product or encounter limitations.

**Aida Knezevic:** Yeah, the documentation and knowledge base could definitely be incorporated as a separate step in the pipeline. That would be really valuable.

**Aida Knezevic:** The quality gates are mapped to feedback from your review team — Vikram, Nicolas, and yourself. We flag things like unsighted statistics, inaccurate product info, unsourced competitor claims, and patronizing concept explainer links. For example, just adding links that readers wonder why they're there. We can expand this with anything else that comes up. The key thing is managing context limits — we break the process into multiple steps so the AI can handle it all effectively.

**Aida Knezevic:** Because we had to regenerate articles and also started working on new ones at the same time, you'll get five new drafts either today or tomorrow — they're in the editing queue right now. We're also finalizing revisions on three articles.

**Aida Knezevic:** So Natalie will follow up with that in the external channel as well, just to get your final sign off.

**Nicolas Lecomte:** Okay, because I was going to ask, because it seemed that the pace of delivery of new articles had slowed down.

**Nicolas Lecomte:** So I was wondering, I assume that you guys were waiting first to fix the workflow before.

**Aida Knezevic:** Yeah, Natalie was really sick on Monday and Tuesday, and we had a couple of people involved in building the new pipeline. That slowed us down a bit, but we'll make it up. You're still going to get the articles you're due, but we wanted to fix everything and do it right rather than waste your time reviewing subpar content.

**Aida Knezevic:** We were working on getting new content this week. We've published four articles since our last sync, and they're all indexed with some already getting traffic. Looking at Google Search Console data, we can see week-over-week traffic growth as we publish. The Code Sandbox alternative article is doing quite well in terms of clicks and average position. We're also tracking this in PostHog, and that article is getting the most traffic overall. We need to filter by session source to understand where the traffic is coming from.

**Paul Sinaï:** We're fixing some trackers in our website implementation. We launched paid ad campaigns starting with LinkedIn and Google, and we're launching X and Reddit today. We're seeing that competitor-related content gets much more conversions. One thing we should consider — Anthropic published a paper at the end of last year about tools and LLMs. The paper essentially says that LLMs are getting so good that we might not need separate tools in the future — just give them simple commands and file system access. People are really interested in sandboxes right now because of that paper. It's great for us — the momentum is good. We'd like to go even faster. Maybe we should write some content related to the Anthropic paper.

**Nicolas Lecomte:** That Anthropic paper idea was actually one of the content ideas I had listed.

**Aida Knezevic:** Good, we have a few new ideas. We're doing additional keyword research this week for bottom-of-funnel topics. The market is getting crowded, so we need to get into product listicles and comparisons. Let me check the Content Ideas doc. I think we should turn this into a table with idea, URL, and date added to make it easier to track.

**Nicolas Lecomte:** Definitely.

**Aida Knezevic:** For the terms you brought up — persistent sandboxes and stateful sandboxes — they don't have search volume in SEMrush yet, but we can incorporate these keywords into the existing content so they're mentioned throughout, and if someone Googles them, our articles will show up.

**Nicolas Lecomte:** It could be because it's so recent. From my perspective, I keep hearing it more and more. A lot of people tell us that when we ask if they want to test Blaxel, they say they're looking for persistent sandboxes or stateful sandboxes.

**Paul Sinaï:** That's what I was going to say. It's going to ramp up — more people are asking about running agents inside a sandbox and how to persist context in different ways. There are several social posts about this. It's a hot topic right now. People are looking to persist context in different ways — not with vector databases or even graph databases, but just keeping a file system directly attached to the sandbox. Storage, persistence, and agent context persistence are the keywords we really want to push, and it's one of our strengths. In the coming days, we're releasing a new feature called Agent Drive — it's like Google Drive but optimized for AI agents. We're seeing increasing demand from customers and prospects around these concepts.

**Aida Knezevic:** Perfect. We should brainstorm some topic ideas. We can write an educational blog post, and if you want something more technical, we can do that and link between them. The key is being the first result when someone asks an AI tool about persisting context in a sandbox.

**Paul Sinaï:** Most of our users use AI tools when they're looking for solutions. So I'm less concerned about traditional SEO and more concerned about AI search — we want to be the first thing that pops up when someone asks ChatGPT or Claude: "How do I persist context within my sandbox?"

**Carly Piekos:** I looked up "Persistent Sandboxes" on Google and you came up as number one, then number three on a re-search. So you're in the top three for that keyword.

**Paul Sinaï:** That's good. I really want to be number one.

**Carly Piekos:** You should check it yourself — I didn't use incognito, so you might see different results.

**Nicolas Lecomte:** Yeah, since my Google account is tied to blaxel.ai, the search engine might filter results based on that.

**Paul Sinaï:** I wanted to ask about CheckThat performance. It's improving, but still pretty flat. What are your thoughts on how we can improve the performance?

**Aida Knezevic:** CheckThat performance depends on the prompts we're tracking, and we're tracking a lot of them. We need to understand where you're not showing up at all, and whether those prompts are important to you. If broader prompts show nothing for you, that's not a red flag as long as you're showing up for the prompts that really matter. Carly and I can export the prompts and analyze the dataset to see if any are less relevant and skewing the data. Looking at the data, your competitors like E2B have 7.1% visibility — also not super high — because we're tracking too many broad prompts. First, we need to clean the prompt list. Second, we want to look at high-value prompts where you're not showing or showing inconsistently, and improve visibility there. The good news is that product listicles show up very quickly in AI search. So the more of that content we publish, the more your visibility grows. But we do want to clean the prompts first to avoid diluting the data.

**Aida Knezevic:** I sent over the CTA options. When you have time to set up the MVP banner, just let us know.

**Nicolas Lecomte:** I'll work on it soon. I'm doing some website updates and plan to include that.

**Aida Knezevic:** Great. We can track clicks and how they progress to other parts of the site in PostHog. I think that's all the updates we had. Is there anything else we can help with?

**Paul Sinaï:** We covered most of the things. My biggest concern is improving our presence in AI search — our users use ChatGPT, Claude, Cursor to find tools like ours. We're at 1.5% visibility right now. What's reasonable for the next three to six months? I'd like to discuss a concrete objective and what it takes from everyone to achieve it at our next meeting.

**Aida Knezevic:** Definitely. The first step is cleaning the tracked prompts and understanding gaps. I also want to take this to Kyle and Talal — they've been working on forecasting plans and this seems like a great fit.

**Carly Piekos:** Sounds good.

**Paul Sinaï:** Thanks so much. Really nice to meet you, Carly. Good to see you again, Aida. See you next week.

**Aida Knezevic:** Thank you. Have a great rest of your day.
