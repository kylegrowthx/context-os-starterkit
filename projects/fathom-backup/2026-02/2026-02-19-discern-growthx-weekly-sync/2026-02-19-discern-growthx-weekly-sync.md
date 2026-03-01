# Discern <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-19
time: 17:01 UTC
duration: 21 minutes
organizer: team@growthxlabs.com
participants: Mike Bosserman (Discern), Carrie Chowske (GrowthX)
fathom_recording_id: 123759654
fathom_url: https://fathom.video/calls/571614059
share_url: https://fathom.video/share/hS9xTcotwYLtf7N9RP2NEtikh_fzZXRH
source: fathom
enriched_on: 2026-02-27T20:02:50Z
</metadata>

---

## Summary

Carrie and Mike aligned on Discern's content clusters, establishing guardrails to avoid misrepresenting the company's core Secretary of State services while addressing accuracy concerns. They approved implementing a sourcing block feature to boost content credibility with AI models and confirmed the contract renewal on the existing plan, with expansion discussions deferred to Q2 due to capacity constraints. Discern hit #1 AI visibility ranking this week, up from #2.

---

## Context

This is a recurring client sync between Carrie Chowske (GrowthX VP, content strategy lead) and Mike Bosserman (Discern CEO). Discern operates an AI-powered compliance filing platform focused on Secretary of State services, and GrowthX provides B2B content marketing to boost Discern's organic visibility and AI discoverability. The partnership involves writing state-specific compliance content across multiple clusters (healthcare, real estate, financial services, startup formation) to establish authority and drive pipeline. A recent internal GrowthX transition caused production delays, but the relationship is strong—this is Carrie's first client and first renewal, which both parties value.

---

## Relevance

- **Content Strategy & Product Accuracy:** Critical discussion on narrowing cluster focus to Discern's actual capabilities (Secretary of State filings) to prevent customer confusion and legal risk.
- **AI Visibility & SEO:** Introduction of sourcing block feature to improve content credibility signaling and increase likelihood of AI model picks.
- **Client Renewal & Expansion:** Contract renewal confirmed; expansion deferred to Q2, critical for revenue and capacity planning.
- **Account Health:** Strong relationship, hitting performance milestones (now #1 in AI visibility); accuracy spot-check needed due to previous writer quality issues.
- **Conversion Tracking:** Partnership moving to next phase with pipeline and revenue reporting; requires GTM team coordination.

---

## Overview

- **Content Strategy:** New compliance clusters must focus exclusively on Discern's Secretary of State services to avoid misrepresenting the product's scope.
- **Accuracy & AI:** A new sourcing block will be added to articles. This improves content accuracy and boosts AI visibility by signaling credibility to models.
- **Renewal:** The contract will renew on the current plan. An expansion was deferred to Q2 due to Discern's limited internal capacity.
- **Performance:** Discern is now the \#1 AI visibility result for its tracked prompts, up from \#2 last week.

---

## Key Topics

### Content Strategy & Accuracy

  - **Problem:** New compliance clusters risk misrepresenting Discern's product scope by covering topics beyond its Secretary of State services (e.g., annual reporting, franchise taxes).
  - **Solution:** A new sourcing block will be added to all articles.
      - **Function:** Lists official sources (e.g., Dept. of Revenue, Secretary of State) with direct links.
      - **Benefits:**
          - **Accuracy:** Provides a clear reference for future updates.
          - **AI Visibility:** Signals credibility to AI models, increasing the likelihood of content being used in AI-generated answers.
  - **Implementation:** GrowthX will investigate adding the block as a Webflow CMS component for automated publishing.

### Content Clusters & Focus

  - **Healthcare Compliance:** A high-priority cluster, as healthcare is a major Discern customer segment.
      - **Rationale:** Healthcare companies frequently use Professional Corporations (PCs) and PLLCs and often operate across state lines.
      - **Examples:** Warby Parker, Cure Care, Moxie, Brave Health, Fae Nutrition.
  - **Startup Formation & Compliance:** Will be general-purpose, not industry-specific.

### Performance & Reporting

  - **AI Visibility:** Discern's ranking improved from \#2 to \#1 for its tracked prompts.
  - **Production:** A recent slowdown (14 articles published vs. 26 in progress) is temporary and due to an internal GrowthX transition.
  - **Accuracy Spot-Check:** Mike will review recent articles for accuracy after GrowthX flagged formatting issues (e.g., broken links) from a previous writer.
  - **Conversion Reporting:** The next phase of the partnership will track pipeline and revenue. Mike will connect Carrie with Danny (Go-to-Market) to define reporting access.

### Renewal & Expansion

  - **Decision:** The contract will renew on the current plan.
  - **Rationale:** An expansion was deferred to Q2 due to Discern's limited internal capacity.
  - **Action:** GrowthX will draft and send the new renewal agreement.

---

## Action Items

**Carrie Chowske**
- Consult Stages engineering re: Webflow citations; then implement template/component and test on 2 articles
- Send 5–10 AI visibility prompts to Mike for approval
- Draft and send renewal agreement to Mike

**Mike Bosserman**
- Review recent articles; send feedback to Carrie (esp. Keystone/Financial Services); then GrowthX updates healthcare cluster
- Intro Danny to Carrie re: conversion/pipeline reporting access

---

## Transcript

**Mike Bosserman:** Hey, sorry about that. I was on with a customer. It's so busy. The sales manager that I hired just had a baby, so he is gone for like a month, and it means that I am getting crushed.

**Carrie Chowske:** Okay, well, we can keep it tight to make sure we're not wasting your time. Let me just skim over the performance stuff quickly—we had a little slowdown last week because of internal transitions and a calibration article, so we're a bit behind. But we have 14 articles to publish and another 26 in progress. Once we get aligned on these clusters, we should be fine.

**Mike Bosserman:** Sounds good.

**Carrie Chowske:** So I went through and mapped which topics we're covering. They're all state-specific variations of healthcare, real estate, and financial services compliance. Some are largely done. Are there any red flags, or anything that needs clarification on how Discern fits in?

**Mike Bosserman:** The main thing I'm concerned with is that these clusters make sense, but articles cover all kinds of compliance. Really, the only place we fit in is on the Secretary of State side. So I want to avoid people thinking we do all these other things. And I'm a bit nervous about keeping this variety of information up to date.

**Carrie Chowske:** Got it. I have a couple things that might make that easier.

**Carrie Chowske:** Since we do calibrations at each cluster, if you give us the angle or tell us it's not good, we can work that in. The design is replicable so each cluster can be easily updated state-by-state. The other thing—and this has two benefits—is adding citation sourcing to the bottom of articles. First, it gives you exact links to reference material for manual updates. Second, AI models see structured sourcing blocks as credible signals and are more likely to pick up content. We could test it on a couple articles using Department of Revenue and Secretary of State links, which are the only two relevant offices in most states.

**Mike Bosserman:** That sounds like a great idea. The question is implementation. Simplest is putting it in the article at the bottom. I'm not sure if Webflow CMS can handle a separate component on the site itself, but if it can, we can try that.

**Carrie Chowske:** It should be able to. I'll talk to our engineering team since we auto-publish to your site through Stages. We might be able to add it as part of the workflow and implement it as a template component. We've done similar things for other Webflow clients. Either way, we can start working this in. AI models love structured data, and it gives us quick reference links for updates.

**Carrie Chowske:** I want to make sure we're tying back properly. We worked closely on annual reporting to ensure we only cover what Discern actually does.

**Mike Bosserman:** I read the Keystone article you sent. A block of text made it sound like we handle all those things mentioned in the article. That's a disaster waiting to happen because it's super complex.

**Carrie Chowske:** Got it. Just continue giving us feedback like that and we can work it into the pipeline. With cluster-by-cluster calibration, we integrate notes directly without manual rework. Once the pipeline is set up, it flows automatically.

**Carrie Chowske:** We had a writer who generated formatting issues—broken links, weird formatting—on articles from the last two weeks. The formatting issues made me question accuracy. I want to make sure we're using the right sources, since source errors cascade into incorrect information.

**Mike Bosserman:** I have a list to review articles and spot-check recent publications.

**Carrie Chowske:** Please do. We can go back and audit everything if you spot something.

**Carrie Chowske:** Financial services compliance—is that the one with the problematic paragraph? Or should that be more tied to healthcare?

**Mike Bosserman:** One of our big segments is healthcare. Healthcare companies have a lot of professional corporations and PLLCs. For example, Warby Parker is a customer—they have PCs from their eyeglass optometry business. We also work with Cure Care, a home healthcare business for hospice patients. Moxie helps people form med spas. Brave Health is a mental health product. Fae Nutrition. We have tons of healthcare companies.

**Carrie Chowske:** That makes sense. They're often owned by a larger hospital system or physician's group and stationed across states—like chains operating in multiple states.

**Carrie Chowske:** And startup formation and compliance—are those general-purpose or industry-specific?

**Mike Bosserman:** General.

**Carrie Chowske:** Got it. Next, I want to cover conversion reporting.

**Carrie Chowske:** At the QBR, we talked about moving to the next phase. We've got traction with compounding content growing traffic and leads. Now we need to track the financial and pipeline output to make sure it's profitable for you. I think you mentioned Danny handles go-to-market? We could get reporting access on our side to track this together.

**Mike Bosserman:** Let me loop him in with you directly, and we can talk about what to do there.

**Carrie Chowske:** Perfect.

**Carrie Chowske:** For AI visibility, I want to narrow down to 5-10 core prompts as our baseline for success—the things you absolutely want to show up for. I can suggest them based on what I know about your product. Would that be helpful?

**Mike Bosserman:** Sure.

**Carrie Chowske:** Great. With SEO, you track individual keywords and search volume. With AI visibility, you want to be there before the search happens. It's about what you want to be known for if someone asks. Your input is valuable—what language do you hear on sales calls from customers? That's how people use AI now for product discovery.

**Carrie Chowske:** Last thing—renewal. Did you review the slide deck? We can renew on the current plan, or we can explore expansion. What's your take?

**Mike Bosserman:** We'll stick with the renewal of the existing plan rather than expanding. It's possible in Q2 I might change my mind with more resourcing, but right now, I don't have capacity to increase what we're doing. It's working well.

**Carrie Chowske:** Perfect. Should we draft the new agreement and send it?

**Mike Bosserman:** Yeah.

**Carrie Chowske:** Great. This is my first renewal and you were my first client. There's a nice symmetry there.

**Mike Bosserman:** It's beautiful. Glad to be working with you again.

**Carrie Chowske:** Performance is really good. Everything's in the positive direction. One thing to highlight: last week Discern was #2 for AI visibility. This week, you're #1.

**Mike Bosserman:** Nice.

**Carrie Chowske:** We'll get you the prompts I promised. Once you send feedback on the calibration article, we'll launch the pipeline. We're wrapping up the healthcare and real estate clusters now. If we're waiting on the pipeline, I'll have production double-check those healthcare articles to make sure they're solid.

**Mike Bosserman:** Sounds good.

**Carrie Chowske:** Great talking to you.

**Mike Bosserman:** You too. Bye.
