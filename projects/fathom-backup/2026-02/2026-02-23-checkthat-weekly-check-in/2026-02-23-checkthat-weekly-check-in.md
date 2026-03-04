# CheckThat Weekly Check In

<metadata>
date: 2026-02-23
time: 18:30 UTC
duration: 32 minutes
organizer: Stevie Kim (stevie@growthx.ai)
participants: Marcel Santilli (marcel@growthxlabs.com, GrowthX), Daniel Lopes (daniel@growthxlabs.com, GrowthX), Jason Gong (jason@growthx.ai, GrowthX), Pedro Steimbruch (pedro@growthx.ai, GrowthX), Jose Farias (jose@growthx.ai, GrowthX), Estevão Mascarenhas (estevao@growthx.ai, GrowthX), Leonardo Carpenedo Steffen (leonardo@growthx.ai, GrowthX), Nigel (nigel@growthx.ai, GrowthX), Stevie Kim (stevie@growthx.ai, GrowthX)
fathom_recording_id: 124573868
fathom_url: https://fathom.video/calls/577931154
share_url: https://fathom.video/share/K-SenfV8SG1xsuW92SKxt-ssozXesjN6
source: fathom
enriched_on: 2026-02-27T10:15:00Z
</metadata>

---

## Summary

Marcel presented a new product vision to replace CheckThat's unusable dashboard with a shareable, programmatic "AI Audit" report, validated by a manual prototype for Eon (a $1B+ data recovery company). The team agreed on a phased approach: first build a V2 front-end prototype for one brand, then evolve it into three outputs (public lead-gen tool, paid deep-dive, redesigned dashboard).

---

## Context

CheckThat's current dashboard is a strong SEO asset but provides no user value—the raw data is incomprehensible without manual analysis, forcing users to export and process it externally with agents and MCPs. Marcel conducted a comprehensive manual audit for Eon, proving the concept works. The audit cost only ~$50 in API credits and revealed Eon has near-zero AI visibility despite being a Gartner-recognized vendor. The new strategy is to build a V2 front-end prototype for one well-established, data-rich brand (e.g., Webflow or Augment Code), validate the end-to-end user experience, then reverse-engineer the backend automation required. This single-brand prototype approach de-risks the full product roadmap.

---

## Relevance

- **Product Strategy:** Defines the path forward for CheckThat's core offering—moving from a broken dashboard to an actionable audit report format
- **Engineering:** V2 front-end prototype scope, brand selection, workflow automation requirements, backend architecture decisions
- **Go-to-Market:** Phased rollout (public lead-gen → paid deep-dive → dashboard redesign) creates multiple monetization vectors and marketing hooks
- **Data & Research:** Establishes audit methodology (competitive intel, SEO performance, content efficiency, visibility mapping) and validates cost structure (~$50/audit)

---

## Overview

- **New Vision:** Replace the unusable dashboard with a shareable, programmatic "AI Audit" report, validated by a successful manual prototype for Eon.
- **Core Strategy:** Build a V2 front-end prototype for one brand first. This validates the end-to-end user experience before committing to backend automation.
- **Phased Rollout:** The audit will evolve into three distinct outputs: a public lead-gen tool, a paid deep-dive report, and a redesigned dashboard.
- **Immediate Action:** Marcel will sync with Daniel, then Estevão, to finalize the plan for the V2 prototype.

---

## Key Topics

### Problem: The Current Dashboard Is Unusable

  - The current dashboard, while a strong SEO asset, fails to provide user value.
  - Its raw data is incomprehensible without manual analysis, forcing users to export data for external processing (e.g., with an agent and MCP).
  - **Conclusion:** The dashboard requires a fundamental redesign, not minor tweaks.

### Solution: The "AI Audit" Report

  - A manual audit for Eon (a $1B+ data recovery company) proved the concept.
  - **Key Findings:**
      - Eon has near-zero AI visibility despite being a Gartner-recognized vendor.
      - The audit cost was \~**$50** in API credits, demonstrating a viable cost structure.
  - **Report Structure:**
      - **Competitive Intel:** Landscape analysis and analyst perception scores.
      - **SEO Performance:** Audit of technicals, keywords, and traffic sources.
      - **Content Efficiency:** Benchmarks against competitors for traffic/page.
      - **Visibility & Category Mapping:** Analysis of AI perception and market position.

### Implementation: Phased Rollout Plan

  - The audit will evolve into three distinct outputs:
    1.  **Public Lead-Gen Tool:** A shareable, high-level report (e.g., like Amplitude's AI Visibility tool).
    2.  **Paid Deep-Dive Report:** The full, detailed audit for paying customers.
    3.  **Redesigned Dashboard:** A future evolution of the current dashboard, built on the audit's insights.

---

## Action Items

**Marcel Santilli (GrowthX)**
- Sync with Daniel Lopes to validate V2 prototype strategy
- Update Estevão Mascarenhas and Stevie Kim on outcomes and next steps

---

## Transcript

**Jose Farias:** Thanks, everyone.

**Estevão Mascarenhas:** Everyone, thanks.

**Pedro Steimbruch:** Hey.

**Marcel Santilli:** I think Daniel might not be able to join today, so I don't know if you're waiting on anyone else.

**Stevie Kim:** No. We have our engineering check-in on Mondays where I bring everyone up to speed on what we discussed between you, Daniel, and me on Fridays—the overall strategy and any priority changes.

**Marcel Santilli:** Okay, cool. Well, Nigel, Pedro, Jose—feel free to drop off. Estevão, Stevie, I'd like you to stay on if you're interested.

**Pedro Steimbruch:** Bye.

**Stevie Kim:** Bye.

**Marcel Santilli:** Okay, so let me walk you through where I am right now. I've taken a couple of different paths. One was the handbook path—documenting my thoughts on where we are, where we're going, and how I'm thinking. That's getting better every day. I made some big changes to the presence score methodology, for example. I'm getting closer to something really solid.

The challenge is I'm a very visual person. I need to see something working, or my brain stops functioning. So I decided to do an end-to-end audit for a company called Eon—one of our strategy session customers. They're in data recovery and backup, backed by Sequoia, worth over a billion dollars. Despite being a Gartner vendor with massive credibility, they have near-zero AI visibility. That's the perfect test case.

I spent about two hours doing a comprehensive manual audit—reviewing their analysts, analyzing their SEO performance, benchmarking their content efficiency against competitors, mapping their visibility and market position. The cost? About $50 in API credits. Not crazy.

The result is something way more digestible than our current dashboard. I created two report structures. One follows our methodology end-to-end. The other breaks down into sections: Competitive Intel with landscape analysis and analyst perception scoring, SEO Performance with technical audits and keyword rankings, Content Efficiency comparing them to competitors on authority, traffic, backlinks, and pages per content, and Visibility & Category Mapping showing AI perception and market positioning.

**Estevão Mascarenhas:** That's awesome. I'm trying to visualize the workflow. Your idea—should we build something entirely new from a UI perspective, or fit it into the current CheckThat app experience?

**Marcel Santilli:** There are actually two separate questions here. There are potentially three outputs. First, updates to the public area—making public pages more actionable with composite scores and trends beyond just the visibility score. We've already improved this, but visibility alone only tells part of the story. If we add how AI perceives the brand, their reputation, presence, and visibility together, it becomes way more concrete and contextual.

But that's not the first output. First, I need to nail a good view for one brand, one audit. I'm trying to nail the snapshot—a customer comes in and asks, "Help me. Tell me what's happening." That's what Amplitude's AI Visibility tool does. Simple, shareable, hook-like. Their last update was November 3rd, so they don't even maintain it, but it's simple enough that people share it and talk about it.

The third output is evolving our current dashboard. From an SEO perspective, people want this information. But from a usage perspective, no one gets value. I struggle with it myself. I just export the data and run an agent on it because the dashboard is incomprehensible. Unless we get to an audit-level presentation, the dashboard just becomes raw data that's less powerful than an agent with an MCP. So we're not doing a slight tweak—we're fundamentally rethinking how users interact with this data.

**Estevão Mascarenhas:** So to clarify: you have a manually-created prototype, and the idea is for us to automate it, create the workflows and presentation end-to-end as a working prototype—not the final thing, but something you can validate and then hand off to the team as backlog?

**Marcel Santilli:** Yes, exactly. Along the way, we'll figure out how to systematize the deep research. For our single brand prototype, let's pick one category—say it has 50 players. We create profiles for all 50, make sure we're tracking them, do it once, then figure out how to pull from our public pages over time. If we scale that thinking: 200 categories, 50 players each, that's 10,000 pages. Not far off from what we have. We don't need daily updates—monthly is fine for most company descriptions. The deep researcher becomes an aggregator, pulling mostly from our public profiles, with external validation.

The prototype validates end-to-end, and then we reverse-engineer what automation we actually need. I'll sync with Daniel to validate the strategy, then we'll connect to start sketching and mocking the V2.

**Estevão Mascarenhas:** Awesome.

**Marcel Santilli:** Let me run to my next meeting, but I'll ping you later, Estevão. I'll also sync with Daniel and update you both.

**Estevão Mascarenhas:** Perfect. See you all.
