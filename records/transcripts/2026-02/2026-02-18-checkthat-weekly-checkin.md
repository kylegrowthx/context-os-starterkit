# CheckThat Weekly Check In

<metadata>
date: 2026-02-18
time: 20:30 UTC
duration: 53 minutes
organizer: marcel@growthxlabs.com
participants:
  - name: Marcel Santilli
    affiliation: GrowthX
    role: CEO, Founder
  - name: Nigel Hammett
    affiliation: CheckThat
    role: Sales
  - name: Stevie Kim
    affiliation: CheckThat
    role: Engineer
  - name: Jose Farias
    affiliation: CheckThat
    role: Engineer
fireflies_id: 01KH4KDKBC72Z8XKM9Y6XRS7WC
meeting_link: https://app.fireflies.ai/view/01KH4KDKBC72Z8XKM9Y6XRS7WC
source: fireflies
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

The CheckThat team reviewed user engagement (only one workspace invitation since Friday), engineering constraints (database migration underway, team down to two engineers), and Marcel's evolving brand intelligence framework. Marcel introduced a new composite scoring model across four vectors — presence, reputation, perception, and influence — and outlined plans for a curated brand report deliverable by Friday to support Nigel's sales outreach.

---

## Context

This is CheckThat's weekly product and strategy sync. CheckThat is GrowthX's AEO (AI Engine Optimization) measurement product — it tracks how brands appear and perform in AI-generated responses during buyer research. The team includes Marcel (CEO, defining product strategy and measurement framework), Nigel (sole sales driver), Jose and Stevie (engineers building the underlying system). This recurring meeting is where the product roadmap, measurement methodology, and go-to-market strategy are developed in real time, with Marcel actively shaping the product's conceptual framework while the engineering team builds the underlying systems.

---

## Relevance

**To CheckThat:**
- Only one workspace invitation since Friday — traction is very early-stage and engagement is limited
- Nigel is the sole sales driver; his calls with smaller startups are generating positive signal but surfacing terminology and roadmap questions
- Marcel introduced a four-vector measurement model: Presence, Reputation, Perception, Influence — each scored as a composite 0–10
- 3D bubble chart visualization proposed to map brands across presence × perception × reputation with trend arrows
- Data system migration to support multidimensional slicing (by Personas, tags, dimensions) — Jose estimates a few days of engineering
- Brand reports planned: single-page curated audit combining public brand data + deep research insights, partially gated (require signup for detail)
- Handbook repo shared with team to align on context and workflow — Marcel will push latest changes for workflow developers

**To GrowthX Services:**
- Brand report concept mirrors an enhanced version of existing AEO audit tooling — could be a lead generation asset for the agency
- Marcel sees CheckThat as a funnel entry point: brand report → strategy session → GrowthX services engagement

---

## Overview

- User growth concerns: only one workspace invitation since Friday; traction challenges at early stage
- Engineering capacity: database migration underway; team reduced to two engineers this week (Pedro absent)
- Strategic brand framework: new model positions AI agents as primary buyer influencers; emphasizes buying categories vs. market categories
- Measurement model: four composite vectors — Presence, Reputation, Perception, Influence — with 3D visualization
- Flexible data strategy: migration to new analytics system to support multidimensional brand performance views
- Brand reports development: single-page curated audit, partially gated, targeting lead generation and sales enablement

---

## Key Topics

### User Engagement and Early Traction

Only one user has invited another person to their workspace since Friday. Nigel's outreach calls with smaller startups are generating positive qualitative signal — users see value in filtering branded vs. non-branded contexts and agree with default Persona settings. Questions are emerging around future roadmap (what actions stem from insights?) and unfamiliarity with some terminology. This signals both genuine interest and a need for clearer onboarding and product education.

### Strategic Brand Intelligence Framework

Marcel articulated a layered mental model for brand analytics built around three audiences: buyers, AI agents, and training bots. The core insight is that AI agents are now primary influencers in buying decisions — brands need to understand how they appear and perform in AI-generated context, not just in human search results.

Two key distinctions drive the framework:
- **Buying categories**: what buyers actually search for and purchase (e.g., "sales enablement software")
- **Market categories**: the broader competitive landscape brands compete within

A continuous, auto-improving graph system would capture brands, markets, and buyer personas — enabling actionable intelligence and SEO-style compounding benefits over time.

### Composite Scoring Model

Marcel introduced a four-vector measurement system:
- **Presence**: AI visibility and stability across engines during buyer evaluation stages (composite score)
- **Reputation**: aggregated analyst reviews and community feedback, tiered like Gartner Magic Quadrants (trust, innovation, support)
- **Perception**: AI-generated narratives on brand attributes across six buyer-relevant dimensions (0–10 composite)
- **Influence**: brand's ability to shape buyer decisions through onboarding, intelligence setup, and internal configuration

Visualization: 3D bubble charts combining presence × perception × reputation, with trend arrows showing trajectory. The goal is a quick visual read on brand positioning and risks.

### Technical System Migration

Jose is optimistic about migrating to a new, more flexible analytics backend. No technical blockers. Estimated lift: a few days of focused engineering. The new system will support slicing brand data by Personas, tags, and dimensions — enabling flexible quadrant views without heavy dashboard builds. The strategy favors report-style snapshots over data-intensive real-time dashboards, reducing engineering risk and complexity.

Pedro is out this week, leaving Jose and Stevie as the two active engineers. Stevie has a database migration requiring several days of focused work. Priority: growth tickets first; brand report shaping deferred to Marcel.

### Brand Reports Development

Marcel is building a "brand report" — a single-page curated audit combining public brand data with deep research insights. The report is partially gated: some content is public, detailed insights require user signup. Nigel confirmed it's useful for outreach and early sales conversations to spark interest. Marcel aims to have a more polished version by Friday.

Current AEO grader alternatives (like HubSpot's) are inadequate — the brand report is designed to be meaningfully better: more curated, more actionable, more AI-native.

---

## Decisions & Commitments

- Marcel will walk the team through the handbook repository to align on context and workflow standards
- Stevie will prioritize growth tickets over brand report feature work while database migration is underway
- Jose and Stevie will complete the database migration and analytics backend upgrade within the week
- Marcel will have a refined brand report version ready by Friday for sales use
- Nigel will use the brand report template in outreach conversations to establish early demand signals
- Team will check in daily on migration progress to ensure Friday deadline is met

---

## Open Questions

- What specific actions will users take based on brand report insights? (unclear from early customer conversations)
- How will Personas and dimension slicing work in practice once the analytics backend is migrated?
- Should the handbook repo be version-controlled as a separate product component or integrated into the main codebase?
- What constitutes a "polished" brand report for Friday's deliverable?

---

## Action Items

**Marcel Santilli**
- Share and walk team through new handbook repository documentation for context and workflow understanding
- Continue shaping brand reports and public page presentation to refine lead generation and user engagement features — target Friday
- Push latest workflow and handbook repo changes to assist developers

**Stevie Kim**
- Focus on growth tickets to free other engineers for complex technical tasks; defer brand report shaping for now

**Jose Farias**
- Continue discussions with Jacopo to migrate to a new flexible analytics system supporting multidimensional data visualization
- Assess engineering lift needed for new data pipelines; prioritize based on value and effort asymmetry

**Nigel Hammett**
- Use emerging brand report tool for outreach and initial sales conversations to demonstrate value

---

## Transcript

**Marcel Santilli:** Alright, let's get started. Quick check on user engagement this week, Nigel. Where are we?

**Nigel Hammett:** Hey, so we've got one workspace invitation since Friday. It's pretty early. I've had some good calls with smaller startups though. They really get the value of filtering branded versus non-branded contexts, and they're cool with our default Persona settings.

**Marcel Santilli:** One invite. Okay. That's the reality of early stage. What are the questions coming up?

**Nigel Hammett:** Mostly around roadmap — what actions can they take from the insights? And some terminology confusion. But the interest is real. People are signing up to demos.

**Stevie Kim:** From the engineering side, we're in the middle of the database migration. Pedro's out, so it's just me and Jose this week. We're prioritizing growth tickets right now.

**Jose Farias:** Yeah, the migration is progressing. No blockers. I've been talking to Jacopo about moving to a new analytics backend that's way more flexible. We can slice data by Personas, tags, dimensions without building heavy dashboards.

**Marcel Santilli:** How long on the migration?

**Jose Farias:** A few days of focused work. Maybe three to five, depending on complexity.

**Stevie Kim:** I'm focused on growth tickets. Brand report shaping can wait until we're past this.

**Marcel Santilli:** That's smart. So let me walk you through what I've been thinking on the brand framework. This is the mental model I want to lock in.

**Nigel Hammett:** Cool, I'm ready.

**Marcel Santilli:** So we have three audiences: buyers, AI agents, and training bots. The core insight is that AI agents are now the primary influencers in buying decisions. Brands need to understand how they show up in AI-generated context, not just Google results.

**Jose Farias:** That's the premise for why CheckThat exists.

**Marcel Santilli:** Exactly. And there's a key distinction: buying categories versus market categories. Buying categories are what people actually search for and buy — like "sales enablement software." Market categories are the broader competitive landscape.

**Nigel Hammett:** So we're helping brands understand which buying categories they own?

**Marcel Santilli:** Right. And over time, we build this continuous graph system that captures brands, markets, buyer personas. That's what enables compounding growth.

**Stevie Kim:** And the data model supports that?

**Jose Farias:** Not yet, but that's the migration I'm planning.

**Marcel Santilli:** Okay, so here's the measurement model. Four vectors. Presence: AI visibility and stability across engines during buyer evaluation stages. Composite score.

**Nigel Hammett:** How do we score that?

**Marcel Santilli:** It's a 0-10 composite. Reputation is next — aggregated analyst reviews, community feedback. Think Gartner Magic Quadrants but for brands. Tiers: trust, innovation, support.

**Jose Farias:** We have data on that?

**Marcel Santilli:** Some. We're scraping analyst reports, feedback sites. Perception is AI-generated narratives. What does an AI agent say about the brand across six buyer-relevant dimensions? Also 0-10 composite.

**Nigel Hammett:** And the fourth?

**Marcel Santilli:** Influence. Brand's ability to shape buyer decisions. Comes from onboarding, intelligence setup, internal configuration. That's the hardest to measure but also the most valuable.

**Stevie Kim:** So we're visualizing this how?

**Marcel Santilli:** 3D bubble charts. Presence on X, perception on Y, reputation on Z. Bubbles show trend arrows. You see the brand's position and trajectory at a glance.

**Jose Farias:** That's going to require some custom rendering.

**Marcel Santilli:** Yeah, but it'll be unique. And the reports I'm building — brand reports — they're a single-page audit. Public brand data plus deep research. Partially gated. Public stuff free, detailed insights require signup.

**Nigel Hammett:** I can use those for outreach immediately.

**Marcel Santilli:** That's the idea. I'm targeting Friday for a more polished version. I've also pushed the handbook repo so you all have context and workflow docs.

**Jose Farias:** I'll check it out. This should help when I'm refactoring the data pipelines.

**Stevie Kim:** Good, I need that for understanding the dimension structure.

**Marcel Santilli:** Alright. So action items: I'm walking everyone through the handbook and pushing the latest changes. Stevie, you're on growth tickets. Jose, keep pushing on the migration and assess the lift for the new data pipelines.

**Nigel Hammett:** And I'm using the brand report for outreach and sales conversations?

**Marcel Santilli:** Exactly. Show people what's possible. That's how we get traction.

**Jose Farias:** When does the migration need to be done?

**Marcel Santilli:** By next week ideally. We need the flexible data slicing to support the brand report properly.

**Stevie Kim:** We can do it if we stay focused.

**Marcel Santilli:** Great. I'll have the handbook updates pushed by tonight. Let's check in daily on the migration.

**Nigel Hammett:** Works for me. I'll get those early conversations going with the brand report template.

**Marcel Santilli:** Perfect. That's the week. Let's ship.
