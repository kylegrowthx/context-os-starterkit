# Augment Code <> GrowthX Weekly Sync

<metadata>
date: 2026-01-07
time: 18:02 UTC
duration: 29 minutes
organizer: Liz Kushnereit (liz@growthx.ai)
participants_internal: Liz Kushnereit, Jason Gong, George Haikal
participants_external: Molisha Shah, Sylvain Giuliani
fathom_recording_id: 112502364
fathom_url: https://fathom.video/calls/523339586
share_url: https://fathom.video/share/CScnLwKbrFGxeFUW9k3Zdqc8JaV9nS33
source: fathom
enriched_on: 2026-02-28T00:00:00Z
</metadata>

---

## Summary

GrowthX and Augment Code aligned on three strategic shifts: a "no-trial" sign-up strategy driving higher-quality users despite lower volume, a shift to premium content focused on quality over volume following Google's core update, and a major product pivot to an AI agent orchestration platform (similar to LangChain) launching in ~6 weeks that will unlock significant content opportunities for technical tutorials and use-case guides.

---

## Context

This is a weekly sync between Augment Code's CTO Sylvain Giuliani and GrowthX's content and product team (Liz Kushnereit and Jason Gong). The meeting occurs during Augment Code's week of returning from the holidays, with Liz having just returned from Texas. The sync reviews performance metrics around Augment Code's sign-up strategy, discusses content quality standards and SEO positioning, and provides a strategic preview of Augment Code's upcoming product direction.

Augment Code is a coding assistant and intelligence platform that's evolving into a broader AI agent orchestration platform. GrowthX manages content marketing for this product with a focus on driving high-quality leads to sales and self-serve channels. The relationship is a content partnership with regular strategic check-ins.

---

## Relevance

- **Product launches and pivots:** The upcoming agent orchestration platform represents a major strategic shift with significant content implications for both tutorial and guide content.
- **Content strategy alignment:** GrowthX is shifting toward higher-quality, experience-driven content, which directly aligns with Augment Code's goal to attract higher-ARPU customers.
- **Marketing metrics and GTM:** The "no-trial" strategy is impacting all downstream metrics and requires CTA/messaging updates across all content.
- **Technical infrastructure:** Sanity tagging and PostHog integration will enable more granular performance reporting for code review and other product verticals.
- **SEO and core updates:** Google's core update is driving the shift to deeper, more authoritative, less AI-generated content.

---

## Overview

- **Sign-up data is skewed by a new "no-trial" strategy.** This shift to paid-only sign-ups is a deliberate trade-off for higher-quality, higher-ARPU users and reduced fraud.
- **Content strategy is shifting to high-quality, experience-driven articles.** This move is driven by Google's core update and will prioritize depth over the previous volume goal of 30 articles/week.
- **A major product pivot to an AI agent orchestration platform is coming in ~6 weeks.** This will create a large content opportunity for deep technical tutorials and use-case guides.
- **Sanity will be cleaned up and tagged.** This will enable granular PostHog reporting on content performance by funnel stage, product, and intent.

---

## Key Topics

### Performance & Strategy Shift

- **Problem:** Content traffic and engagement are up, but sign-up conversions remain low.
- **Cause:** A strategic shift to a "no-trial" sign-up process in early December.
    - **Rationale:** Attracts higher-quality, higher-ARPU users and reduces fraud.
    - **Impact:** Sign-up volume is down, but early data shows the change primarily filters out "tire kickers" without affecting the core buyer persona.
- **Action:** GrowthX will update all CTAs to remove "free trial" mentions.

### Content Strategy & Prioritization

- **New Direction:** Prioritize quality over volume.
    - **Rationale:** Align with Google's core update and the new high-quality lead strategy.
    - **Format:** Focus on anecdotal, experience-driven articles with rich media (screenshots, etc.).
- **Prioritization:**
    1. **Code Review Product:** High-priority due to strong self-serve and sales-led traction.
    2. **Bottom-of-Funnel Content:** Continue iterating on tool comparisons.
    3. **Top-Performing Articles:** Enrich and update evergreen content.
- **Volume:** Weekly output will likely drop from 30 to ~15 articles as quality standards rise.

### Product & Content Infrastructure

- **Website Redesign:** A new, product-focused website will launch Monday, Jan 12, after internal QA.
- **Sanity Cleanup:**
    - **Problem:** The current Sanity setup is broken, with two conflicting studio versions.
    - **Solution:** GrowthX will investigate and resolve the issue.
- **Sanity Tagging for PostHog:**
    - **Goal:** Enable granular performance reporting in PostHog.
    - **Method:** Add tags to Sanity for:
        - Product (e.g., Code Review)
        - Funnel Stage (e.g., Top of Funnel)
        - Intent (e.g., AI code review keyword)
    - **Benefit:** Allows slicing data (e.g., "conversion rate for top-of-funnel content for the Code Review product") without manual URL lists.
- **Auggie CLI:** Deprioritized. The product team is exploring a new "plugin" concept that may make the CLI obsolete.

### Future Product Pivot: AI Agent Platform

- **Strategic Direction:** A major pivot to an AI agent orchestration platform, similar to LangChain but focused on software agent development.
- **Product:** An SDK and APIs for building, customizing, and deploying agents for tasks like incident management, security reviews, and automated documentation.
- **Content Opportunity:** A large volume of deep technical tutorials and use-case guides.
- **Timeline:** The pivot is ~6 weeks out. GrowthX will need a 2–3 week runway to build the content pipeline and standards once the launch date is set.

---

## Action Items

**Liz Kushnereit (GrowthX)**
- Update CTAs/copy across content to remove free-trial references
- Test redirects; ping Sylvain async if issues
- Prioritize code-review product content for next quarter
- Investigate Sanity dual-studio issue; follow up with Sylvain
- Draft Sanity tagging schema (intent/product/funnel-stage); share with Sylvain

**Sylvain Giuliani (Augment Code)**
- Share staging site link for website redesign + incident-responder example in Slack with Liz and Jason

---

## Transcript

**[Opening remarks - removed personal conversation not relevant to meeting context]**

**Liz Kushnereit:** So today we'll go over performance data as usual, a bit of an update on content, and a quick note on the CTA experiment—the control group lost. We'll also check in on Auggie CLI.

**Liz Kushnereit:** For performance, we're seeing a lot of improvement in engagement and traffic with all the work on content refreshes, but we're still not seeing a ton of sign-ups from that. We're still dealing with lower click-through rates. Our overall strategy is to produce content while also seeing what quality looks like and being responsive to what performs well. We're continuously enriching our top-performing article.

**Sylvain Giuliani:** There's a lot happening on our side. We made the decision to shift our sign-up process to a no-trial, paid-only model. Obviously, sign-up goals that we set for ourselves have been completely impacted because you can only create an account if you pay. All those numbers are down and need to be reviewed.

The benefit is that the people who do sign up are very high quality and have higher ARPU. We ran an A-B test starting in early December, and after seeing the results, we realized that getting fewer users but more active, higher-paying users is a worthy trade-off, especially given fraud reduction.

And I was looking at the data—SEO is actually doing pretty well, all things considered. When you think about how aggressively we rolled out this new flow and how it's not super well-designed, we're still pumping decent numbers. It's not as bad as I thought it would be.

During the holiday, I've been working on a complete rebranding and redesign of our website. I've redesigned all the guide pages and learn pages that you all created. This should go live Monday. We're doing final QA this week. It will change the sign-up experience and the install page, and that should hopefully have a positive impact on our numbers. But yes, these low numbers are partly because of the no-trial approach.

**Liz Kushnereit:** Going into this quarter, we'll probably want to set different OKRs keeping that strategy in mind. I'll work with the editors since I'm not sure how many of our CTAs mention the free trial. I'll prioritize getting that updated so we don't have any issues.

**Sylvain Giuliani:** We've updated a lot internally, but there's still content in Sanity mentioning free trial. Let's make sure we fix that in the coming weeks.

**Jason Gong:** After you do this update, if it changes who buys and who we care about, that would be good info to have.

**Sylvain Giuliani:** We'll learn that as we go. The interesting thing about the no-trial experience is that in our early December test, we haven't seen a change in who buys—just kicked out all the tire-kickers and people who were trying to abuse the trial. There are good people we likely lost, and we're going to add a system to give selective trial access to certain people. But so far, the experiment shows that no-trial just removed the problem users, and all the good ones are still going through.

**Liz Kushnereit:** That sheds a lot of light on it. I'll test the redirects again and ping you async if there are issues.

**[Content Strategy Discussion]**

**Liz Kushnereit:** The biggest thing is moving into higher quality content. Google's recent core update is a black box, but the natural move is away from obviously AI-generated content. For something like the "8 best AI coding assistants" article, we're moving toward anecdotal, experience-driven pieces with more screenshots and rich media—which take longer to write. But there's an incentive: better traffic and engagement. It's not just about raising the quality bar; it adds long-term value and aligns with what you all are moving toward in terms of higher-quality, more valuable leads.

For bottom-of-funnel content, we're working on tool comparisons with benchmark content pieces. We're iterating, moving away from TLDR structures, with more personal language like "I'm here to help because I've dealt with this myself." We include screenshots and FAQs. With this higher quality threshold, we probably won't hit 30 articles a week super quickly. Right now we're doing about 3 a day, which is 15 a week. We're working toward something closer to 30, but we won't sacrifice quality. We'll look at data and prioritize which articles to fix. Weekly output will be a give-and-take based on what's most valuable.

**Sylvain Giuliani:** The volume thing is fine by me. If we just publish one hit piece a week, that's better than 30 mediocre pieces. But I understand we need some volume.

One question: how's the code review product doing? We launched in early December and it's working really well—strong self-serve and sales-led traction. What's the pipeline for code review content?

**Liz Kushnereit:** That's something we want to invest more in. I was also thinking about it. We could establish tracking in PostHog specifically for that product, depending on how much of a priority it is.

**Sylvain Giuliani:** We're planning to clean up and tag Sanity. I noticed the Sanity setup is broken—there are two conflicting studio versions. I want to solve that mess.

I also want to add tagging to Sanity content: product (e.g., Code Review), funnel stage (top/middle/bottom), and intent (e.g., "AI code review keyword"). That way, in PostHog, I can slice and dice really easily—like "show me the conversion rate for top-of-funnel content for the Code Review product." If we just add those three fields in Sanity, we get everything else for free.

**Liz Kushnereit:** That's a great idea. Some content serves both top and bottom of funnel, so we'd want to track that nuance. It would be meaningful to see if our thesis is correct versus having this scattered across different places.

**Sylvain Giuliani:** On Auggie CLI, basically, forget about it for now from your side. Internally, we're exploring a new "plugin" concept that might make the CLI obsolete. This is an us problem. Consider it done on your side for now.

**[Website and Product Pivot]**

**Sylvain Giuliani:** On our side, we're redesigning the entire website to be more product-focused. We redesigned the guides, learn pages, and everything else. It should go live Monday after QA. There are still some cleanup tasks with Sanity, but that's not a big deal. As long as 90% is done, we can fix things as we go.

The key thing I want to highlight is a major shift toward AI automation. We're not just staying a coding assistant. We're shipping a bunch of APIs for people to orchestrate agents. Think of it like giving you the building blocks to build an agent for security review or incident management. You define the agent, define the triggers, and can run it in any environment. You can have a fleet of agents always running, all powered by our context engine.

For you, Liz, this means a slew of technical tutorials. Here's an example: one of our design partners is using our APIs to do incident management. So the conversation becomes: "What is incident management? How does AI help? How do you use Augment Code APIs to build your own bespoke version instead of buying an off-the-shelf product?"

That's the type of content: what-is pieces, deep-dive technical how-tos, use-case guides. I wrote an example article on building an incident responder with our new API. There's going to be a lot more of this type of content, as we productionize these APIs.

Website-wise, we're finishing QA this week. I'll share the staging link in Slack. The goal is to go live Monday with the new site.

**Liz Kushnereit:** With these how-to pieces, we can talk async about expectations, volume, and prioritization.

**Sylvain Giuliani:** I'm just giving you a heads up. There's no action on your side right now. I'm putting together what I call the "season of automation"—lots of SEO work, tutorials, video content. Right now we have 20 design partners. APIs are still in alpha/beta. It's probably six weeks out before everything is GA and we can hit the ground.

When you're ready, we can work backward from a launch date to figure out when to start building the content pipeline and standards. You'll need a 2-3 week runway to get everything calibrated, similar to what you did for Webflow.

**Jason Gong:** Is this more like AI cloud code skills, or are you building a platform for people to build on?

**Sylvain Giuliani:** It's very much a platform—like LangChain, but focused on software agent development. It's not that we're stopping coding agents. That's still our bread and butter for the next 6-12 months. But we're seeing demand for a platform to build any kind of software agent: docs, incident management, etc. Right now, people are hacking around it. So we're building the platform.

It's like Pusher, back in the day, with "How to build an incident management bot with PHP, Python, React"—we're back to that era, but with agents.

**Jason Gong:** There's a lot of content surface area there.

**Sylvain Giuliani:** Exactly. Excited about this direction.

**[Closing]**

**Sylvain Giuliani:** I'll share the website with you. Liz, ping me if there are pull requests that need merging. If you want me or someone to review content, let us know. Otherwise, best to just publish and tell us—if we need to unpublish, that's fine too.

**Liz Kushnereit:** Sounds good.

**Sylvain Giuliani:** All right, perfect timing. Thanks for the sync.
