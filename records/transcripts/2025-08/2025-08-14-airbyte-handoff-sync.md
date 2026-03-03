# Airbyte handoff sync

<metadata>
date: 2025-08-14
time: 18:02 UTC
duration: 27 minutes
organizer: carrie@growthx.ai
participants: Andi Bailey, Darrell Etherington, Jakub Rudnik, Carrie Chowske
fathom_recording_id: 80677117
fathom_url: https://fathom.video/calls/381445960
share_url: https://fathom.video/share/yPsrHqh6L8zzUX4jVZxAB1MUo4St-WD-
source: fathom
enriched_on: 2026-03-03 15:25 UTC
</metadata>

---

## Summary

The GrowthX team discussed a major scope expansion for the Airbyte engagement: the client wants ~7,000 page refreshes (620 Connectors pages plus 6,700 How to Sync pages), new PSEO content for industries and use cases, and editorial content tied to a new product launch. The core challenge is that both refresh and new content pipelines require significant engineering resources, forcing a prioritization decision. The team recommended prioritizing net new content (starting with industries pages) over refreshes because new pages drive immediate results, while proposing that GrowthX allocate dedicated engineering resources to handle multiple parallel workstreams. Leadership escalation is needed to secure engineering commitment before the August 26 client sync.

---

## Context

Airbyte is a data integration and ELT platform. GrowthX is executing a content marketing engagement that started with creating page templates and refreshing existing connector and sync documentation. Carrie Chowske was recently handed off the account from Jakub and is preparing for a client sync on August 26. This internal handoff meeting aimed to align the GrowthX delivery team (Carrie, Andi, Darrell, Jakub) on the actual scope and next steps before communicating with the client. The client (represented by Tanmay in previous communications) has been incrementally expanding requirements, and Carrie surfaced that what the client is now asking for significantly exceeds the original scope commitment of 25-100 pages per week.

---

## Relevance

**To GrowthX Delivery:**
- Programmatic refreshes of existing content are proving harder than anticipated — they require engineering pipelines and don't deliver quick wins like net new content does. This challenges the typical PSEO delivery model.
- New content type (industries and use cases PSEO pages) requires defining templates and data pipelines before execution. Jakub has v1 outlines prepared, but client input on page structure is needed.
- Deliverable pace will depend on content mix: expect ~25 pages/week for new content, ~100 pages/week for simple refreshes, but current scope (10,000+ pages) is infeasible without dedicated engineering.

**To GrowthX Business Development:**
- Account is healthy and expanding: Airbyte is investing budget for dedicated engineering resources and new content initiatives, signaling confidence in the engagement.
- Product launch timing (end of September) creates a near-term deliverable milestone for editorial content.
- Risk: without dedicated engineering resources allocated quickly, GrowthX will have no deliverables between late August and early September, risking client satisfaction at a critical juncture.

**To GrowthX Leadership:**
- This engagement justifies permanent engineering headcount or reallocation. Client is paying enough to cover dedicated engineering resource. Decision needed by August 26 sync.

---

## Overview

- Project scope expanded significantly; now includes \~7,000 page refreshes, new PSEO, and new editorial content
- Engineering resources are the key bottleneck for both refreshes and new PSEO pages
- Team recommends prioritizing new content over refreshes for better immediate results
- Need to create clear project timeline and deliverables plan to manage client expectations

---

## Key Topics

### Current Project Status

  - Data engineering resources batch nearly complete (\~70 pages remaining)
  - Next priorities from client:
      - Connectors refreshes (620 pages)
      - How to Sync folder refreshes (\~6,700 pages)
      - New PSEO for industries and use cases
      - New editorial content based on product research

### Refresh vs. New Content Strategy

  - Refreshes intended as stopgap but require same engineering effort as new pages
  - Team recommends prioritizing new content for better immediate results
  - Messaging needs to be careful not to completely dismiss value of refreshes
  - Proposal: Work on both but prioritize new content pipeline

### Resource Allocation and Scope

  - Current scope of 25-100 pages/week not feasible with expanded project
  - Client paying enough to justify dedicated engineering resources
  - Need to create project tracker with timelines and work streams
  - Adjust weekly deliverable expectations based on content mix (closer to 25 for new, 100 for refreshes)

### Next Steps and Priorities

  - Create engineering tickets for both refresh and new content pipelines
  - Prioritize setting up new content pipeline (industries first)
  - Develop strategy to prioritize 7,000 How to Sync pages after initial 620 Connectors
  - Scope out editorial content for new product launch
  - Create project timeline and deliverables plan for client visibility

---

## Action Items

**Jakub Rudnik (GrowthX Labs)**
- Develop plan to prioritize 7,000 How to Sync pages post-initial 620 Connectors refreshes — use SEMrush data to identify high-performing pages, set prioritization criteria

**Andi Bailey (GrowthX)**
- Draft recommendation for client on next steps — new content vs refreshes, including engineering resource needs, deliverable mix per week, and timeline for each workstream
- Escalate need for dedicated client engineer on Airbyte account to leadership (George, Marcel, or Drew)

**Carrie Chowske (GrowthX)**
- Create project tracker (Linear or Notion) for Airbyte work — high-level overview, 4 workstreams (data engineering completion, Connectors refreshes, new PSEO, editorial), timeline estimates
- Link Linear ticket re: engineering resources to Andi for prioritization

---

## Transcript
**Carrie Chowske:** I'm not sure if Jakub even saw the invite yet, so this might be challenging, but I apologize for calling a last-minute meeting. I know that's annoying, but I wanted to figure out what to discuss at our sync tomorrow because scope-wise, what the client is asking us to do isn't going to fit within the original scope. I want to make sure I understand what they're asking for and that we're all aligned, because I have a lot of questions.

**Carrie Chowske:** Okay, so the issue is that what they're asking for — based on Tanmay's response from last week — is a batch of refreshes in two categories. The Connectors category has 620 pages, and the How to Sync folder has about 6,700 pages. That's linked in the shared document. Tanmay is also talking about PSEO. We discussed industries and use cases pages in previous syncs — those are net new pages. He also sent research on product market fit, tone, and aligning use cases with personas. So where this lands us is about 7,000 refreshes, plus new editorial, plus new PSEO. Even with our 25 to 100 pages per week capacity, that's nowhere near in scope.

**Carrie Chowske:** What I think they've asked us to do is move forward with the PSEO and the Connectors group — the 620 pages — which is totally doable. But we still need engineering to build a pipeline and decide whether the template stays the same or changes. I'm hoping it stays the same because that makes it more workable. They want us to do that first while we wait for performance data on the refreshes we've already done. That's a key question — I want to make sure we all understand it the same way. And then we need to have a conversation with them about prioritization because we're talking about 10,000+ pages. We can do it, but the engineering side makes it more difficult than standard PSEO.

**Andi Bailey:** Is the new content for PSEO or the refresh content more difficult?

**Carrie Chowske:** Both. They both require about the same amount of work because they both need new pipelines. We gave Airbyte a rough template, but they want to weigh in on details, and I'm not sure if the templates are finalized yet.

**Darrell Etherington:** The key problem is that the programmatic refreshes sound easy and high volume in theory, but in reality they're breaking in ways that either displease Tanmay or are pipeline and functionality problems. That throws a wrench into things because the original scope of 25 to 100 pages per week was created on the assumption that refreshes would be easier than new content. But they're not turning out to be.

**Andi Bailey:** So Jakub, I think the question here is an order of operations issue. We've got two areas for refresh that sum to about 10,000 pages — Connectors and How to Sync. Then there's editorial PSEO — new net new PSEO on industries and use cases — and new editorial.

**Andi Bailey:** What's the net new editorial on?

**Carrie Chowske:** That's research pages that the client gave us. I'm surfacing this because you guys aren't directly in the conversations I'm having with Tanmay. The client sent us research yesterday around product market fit, tone, and aligning use cases with personas. This looks like content for a new product possibly, but I'm not entirely sure. It's substantial.

**Andi Bailey:** I wonder if this is something we can turn into comparison pages, like Ramp does for different vendors. That's a lot of their general content strategy.

**Carrie Chowske:** I'm not even sure how it works on the back end. There are a lot of layers to understand.

**Andi Bailey:** Jakub, where did you understand we're starting this next phase?

**Jakub Rudnik:** First time seeing this research, but there's a new product or a new vertical-focused packaging of their current product with a product launch to simplify things. They want new content around that. That's in our bread and butter — it should be straightforward. But wasn't that planned for much later?

**Darrell Etherington:** Or am I misremembering?

**Carrie Chowske:** He's giving us a timeline of end of September, but I couldn't tell what he meant — whether that's the target launch or when we start. Let me go through this quickly. This might give everyone more clarity now that we're connected on the product launch piece.

**Carrie Chowske:** The data engineering resources phase is basically done. We're starting the last batch. There were some code glitches our engineering team is working on, but that's being handled and nobody needs to worry about it.

**Carrie Chowske:** Based on the last two Slack messages in the client channel — my update and their research response — they want us to finish the data engineering resources batch next week. Then they want us to do the Connectors refreshes, which is 620 pages. I've got a Linear ticket started to set that up because we need to restructure the pages. I gave them the information we had, including the three template pages Jakub created. When I pulled the How to Sync folder, it's about 6,700 pages.

**Andi Bailey:** Can we look at performance data to prioritize? I think that's what we did for the engineering pages — we only pulled the performant ones. Matt helped with a recording on how to use SEMrush to prioritize. Obviously 7,000 is ridiculous — 620 is pretty big too.

**Carrie Chowske:** There's another layer to this. The Connectors pages are structured as source and destination pairs, with separate pages for each combination. That structure creates complexity.

**Carrie Chowske:** If you go to Facebook as a source, you can sort it, but there are hidden pages that aren't immediately visible. The back-end structure isn't just tagging — it's more complex.

**Darrell Etherington:** Some are source and destination, some are just destination. I think we're focusing on the main pages.

**Andi Bailey:** So we're tracking the main URL. They want us to refresh and enhance these according to best practices.

**Jakub Rudnik:** Both Connectors and How to Sync have outlines with suggestions. There are v1 templates for both, plus we need to work out the development side. We have two that need additional eyes — the Connectors and How to Sync templates — side by side.

**Jakub Rudnik:** I shared all the reference materials. Some were my manual recommendations, some came from ChatGPT and other sources. The five main templates together represent what they want to do. Now that there's budget, the key is making sure they all work together. When I was doing them separately, I was thinking about how to future-proof them so Connector pages interlink with the other page types. That's where I need their guidance — to understand which page types should connect and whether our content structure makes sense from a user standpoint. The other reference documents you found are probably working notes, but they might have useful details.

**Jakub Rudnik:** The final thing I've been working from is the five templates together.

**Carrie Chowske:** That's what I thought. The core issue is engineering resources.

**Carrie Chowske:** Engineering resources is where the time gets eaten up. The bandwidth and complexity don't scale well at 100 pages per week unless we've already built the pipeline. But they're paying us enough to cover dedicated engineering. That puts us in a tough position though — once we finish the last 70 pages of data engineering, we have nothing to deliver to them until we get the new pipelines set up.

**Jakub Rudnik:** My understanding, aligned with Tanmay, is that we work on both. We finish this last refresh batch and simultaneously do keyword research to build the plan for the new content area they outlined. New content should scope to about 25 pages per week, not 100. We need to set up the new page type in parallel because it takes time. I believe new page types are better than refreshes for a few reasons: they already have the first two refresh attempts with mixed results, but new content drives net new clicks and impressions. I'd recommend starting with industries pages first, not personas.

**Carrie Chowske:** That confirms what I was thinking too. Jakub, can you answer some of these questions async? I think we need to filter down to a smaller set. The client was supposed to deliver a prioritized list of programmatic SEO page types, but we're working with what's in this doc. I ordered them per his input. We're starting with industry pages.

**Carrie Chowske:** My recommendation is that new content always outperforms refreshes.

**Carrie Chowske:** The refreshes were meant as a stopgap, but they're not — they take the same time as building new pages. The infrastructure is broken.

**Darrell Etherington:** I don't want to tell them that refreshes are a bust though.

**Andi Bailey:** We need to be careful with our messaging. There's research showing old content over a year old is stale, and we've been pushing that message. But we need to be strategic.

**Carrie Chowske:** I agree. But resource-wise, if we're spending the same effort on refreshes versus new content, and new delivers better results, why not push them toward new content?

**Carrie Chowske:** Either way, whether we do refreshes or new content, we can't hit 100 pages per week without dedicated engineering. So the question is which would they prefer? I'd like us aligned internally first before we propose anything. Darrell and I were thinking: should we spend engineering resources on refresh pipelines, or on new content that we know will deliver faster results? Both need engineering, so why not prioritize what shows results faster?

**Andi Bailey:** Let's make a recommendation rather than asking them which they prefer. Put both tickets in, but prioritize one over the other.

**Andi Bailey:** Our messaging is that we want to get signals from the refreshes before scaling — that's a point they wanted to discuss anyway. We actually already pushed them in this direction on the last call, so this isn't at odds with our current thinking. We need to figure out how to prioritize the 7,000 How to Sync pages after the initial 620 Connectors. We should have that decided before we submit the request for the first pipeline.

**Darrell Etherington:** That could be as simple as picking the top X pages by performance.

**Carrie Chowske:** I'm not trying to block anything. I just want to make sure that the communications I've had since taking over align with what you all decided and what Jakub was working on with them. There are a lot of moving pieces.

**Andi Bailey:** It would be useful to create a project tracker in Linear or Notion — a high-level overview with order of operations, decisions, and key dates. When Marcel, George, or Drew ask how Airbyte is going, you can point to the four workstreams, where you are, and the timeline. That visibility is always helpful.

**Carrie Chowske:** I was moving everything into Airtable last week because I can't fit 10,000+ pages in a spreadsheet. The mix will change week to week, but we need the infrastructure in place. If what I'm hearing is that their budget covers the engineering for all these pipelines, that's great news. I have a Linear ticket started but haven't gotten a response — I'll link it to you after this. The key point is we need engineering to move on something before August 26, so we have deliverables for the client sync.

**Darrell Etherington:** We need to clearly state how many pieces we'll deliver each month and the mix of new vs refresh content. That visibility is critical for the project.

**Carrie Chowske:** That clarifies things. We have a week and a half to set up deliverables or we're in trouble. We need to tell them our recommendation and let them react. We may need someone above my pay grade to push engineering for prioritization.

**Darrell Etherington:** This scope merits a dedicated client engineer on the account to action the work.

**Andi Bailey:** They're paying enough to justify strategy sprint resourcing.

**Carrie Chowske:** I love that idea.

**Jakub Rudnik:** Make sure we frame it right — with new content, there will still be deliverables. We're doing editorial instead of just programmatic work.

**Carrie Chowske:** And we scale based on the mix. New editorial runs closer to 25 pages per week, refreshes closer to 100. We can revisit that mix monthly. The bottom line is we need to get this to engineering with clear direction so we can move forward on the Connectors refreshes, new PSEO, and keyword research.

**Darrell Etherington:** The editorial content for their new product launch is another concrete deliverable we can scope quickly. Since they've given us the launch timing, we can commit to a specific number of articles for that month.

**Carrie Chowske:** I feel a lot better about this. I'll follow up async with Jakub and Andi if I need clarification on anything. This conversation really helped clear my head. I was having a panic moment, but now I understand what we need to do next.

**Carrie Chowske:** Thank you all for your time.

**Andi Bailey:** Thanks.

**Darrell Etherington:** All right, bye everyone.
