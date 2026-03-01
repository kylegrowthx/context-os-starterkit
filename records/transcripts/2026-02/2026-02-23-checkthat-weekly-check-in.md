# CheckThat Weekly Check In

<metadata>
date: 2026-02-23
time: 18:30 UTC
duration: 36 minutes
organizer: marcel@growthxlabs.com
participants:
  - name: Marcel Santilli
    role: Founder/CEO (GrowthX), CheckThat Lead
  - name: Estevão Mascarenhas
    role: Engineering/Design (CheckThat)
  - name: Stevie Kim
    role: Engineering (CheckThat)
source: fireflies
fireflies_id: 01KHPN5Q6KJ6PZQR1B4BAPDM4Q
transcript_url: https://app.fireflies.ai/view/01KHPN5Q6KJ6PZQR1B4BAPDM4Q
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Marcel spent 200 hours in the past month prototyping CheckThat V2 (100 hours on UI coding), focusing on three core outputs: enhanced public pages with composite scoring, a single-brand audit report template, and dashboard redesign. Estevão committed to collaborating on automating the manual prototype into end-to-end workflows, establishing the audit as the golden standard for all categories. The team validated that CheckThat must pivot from a data-exploration dashboard to a narrative-driven audit product that aggregates deep research across visibility, perception, and competitive positioning.

---

## Context

CheckThat is GrowthX's strategic software bet, providing AI visibility indexing and competitive intelligence for B2B SaaS companies. Marcel has been investing heavily in product prototyping to transition from a data-exploration tool to a narrative-driven audit product that tells stories about brand positioning and perception. The team recently completed a detailed audit for Eon (a unicorn data backup/recovery company backed by Sequoia) that validated the methodology—showing how composite scoring, competitive landscape analysis, content efficiency metrics, and perception scoring can drive value. This meeting focused on establishing the prototyping workflow and design standards for scaling this approach across categories.

---

## Relevance

**CheckThat (Strategic Software Product)**
- Prototyping V2 product architecture centered on audit reports as the primary value output
- Validating three core deliverables: public pages, single-brand audit, redesigned dashboard
- Establishing automation workflows to move from manual one-off audits to scalable processes

**GrowthX Services (B2B Content Marketing)**
- Audits are core to every engagement kickoff—positioning CheckThat as internal tooling that could become external product
- Lead generation opportunity on both sides: draw attention to CheckThat via audit content, then convert to service engagements

---

## Decisions & Commitments

- **Prototype approach:** Build a front-end only prototype using one mature customer (webflow, augment code, or similar) to validate design and UX before full development
- **Three outputs:** (1) Public pages with composite scores (reputation + visibility + presence), (2) Single-brand audit report template (the "golden standard"), (3) Dashboard redesign (deferred; currently not adding value)
- **Automation strategy:** Use the one-off audit process to identify what should be systematically tracked across 200 categories × ~50 shortlist players = ~10,000 public profiles
- **Data sourcing:** Deep research aggregates findings from multiple models (analyst coverage, SEO analysis, content efficiency); public profiles pull from CheckThat's tracked data; audit layers these together
- **Monetization framing:** Public pages show lightweight scores + partial audit; full audit behind paywall or upgrade tier

---

## Open Questions

- What is the cadence for updating 10,000 public profiles (company descriptions, competitive positioning, etc.)? Marcel suggested monthly or less frequently for most fields.
- Should the full audit be a CheckThat-branded product or bundled with GrowthX services engagements?
- How does the audit integrate with CheckThat's MCP (model context protocol) to enable agents/automations for users to pull their own insights?
- Which customer should be the first prototype target (webflow, augment code, Eon)?

---

## Overview & Key Topics

1. **CheckThat V2 Prototyping Effort** — 200 hours in past month; 100 on UI, 100 on research, audits, and methodology refinement
2. **Audit as Core Product** — Moving away from dashboard-centric visualization to narrative-driven reports that aggregate visibility, perception, and competitive data
3. **Three Outputs** — Public pages (awareness), single-brand audit (value), dashboard (data layer for future)
4. **Automation & Scaling** — Establishing workflows to track ~10,000 profiles systematically and refresh on monthly cadence
5. **Lead Gen Opportunity** — Audits drive awareness for both CheckThat and GrowthX; audit content becomes shareable/marketing asset
6. **Methodology Validation** — Eon example showed composite scoring (perception + visibility + presence), competitive landscape, content efficiency, analyst coverage as compelling narrative

---

## Action Items

**Marcel Santilli (GrowthX)**
- Validate acceleration support for CheckThat V2 prototype with Daniel (CheckThat Engineering Lead)
- Continue refining audit methodology and prototype structure, integrating feedback from team
- Select the first prototype customer (webflow, augment code, or similar mature player)
- Sync with Daniel on next steps and keep Estevão/Stevie informed of direction

**Estevão Mascarenhas (GrowthX)**
- Collaborate with Marcel on shaping the audit report structure and UI/UX design
- Establish end-to-end automation workflows for audit generation (moving from manual one-off to scalable process)
- Lead iterative sketching and rapid prototyping sessions to validate design direction

**Stevie Kim (GrowthX)**
- Participate in prototyping and design sessions to absorb methodology and provide engineering perspective on automation feasibility

---

## Transcript

**Marcel Santilli:** So let me update you on where we are with CheckThat V2. In the last 30 days, I've spent 200 hours on CheckThat-related work. Of those, about 50-60 hours were connecting dots, researching, and understanding the space. The other 100 hours were UI coding—which I'll be honest, is not my strongest area. I spent 20 minutes today just getting a grid to look the way I wanted. It's tedious work.

But I think the approach is becoming clearer. I want to accelerate by getting Estevão to help me prototype. The idea is to create a front-end-only V2 using one mature customer where we have lots of data—something like Webflow or Augment Code. They're in well-established categories, so we can validate our design and then reverse-engineer what needs to happen behind the scenes.

**Marcel Santilli:** I'm taking two paths to get here. First, there's the handbook path—writing out the methodology, where we are, where we're going. It's getting clearer every day. I made big changes to the presence score today and I'm updating everything. The challenge is that I'm a very visual person. At some point, I hit a wall where I just need to see something built, or my brain stops working.

So the second path was doing these strategy sessions. We worked with a company called Eon—they're in data recovery and backup, well-funded by Sequoia (over a billion-dollar valuation), but basically invisible in AI visibility. They're a perfect validation case because they're new money with legit credentials but zero presence. I did a full end-to-end audit for them. I created prompt guides, did research on how analysts cover them, analyzed their whole space, did SEO analysis, looked at their CP server sources, classified them as vendors or analysts, analyzed their blog and their competitors' blogs. This was about $50 worth of API credits and compute—not crazy, but definitely wasteful. But the output is massive and it's all processable using CheckThat's methodology.

**Marcel Santilli:** I took two approaches to sharing all this work with Eon. One was: look at our entire methodology, refactor it, and forget CheckThat exists. Or: knowing CheckThat exists, create a new narrative experience just from the docs. For me, one-shot explorations are really helpful—even when they're not perfect, there are usually one or two things that feel right, and then I can iterate. It's harder to build component-by-component; it's easier to sketch the whole thing, tweak it, try different variations.

The first approach was much more digestible. It surfaces specific things—benchmarks, trends—and hides the methodology behind the scenes. The second approach created seven markdown files organized by the actual audit work: competitive intelligence (landscape, all players, our analysis), perception scoring (how analysts perceive each player), SEO performance audit, and content efficiency analysis.

The content efficiency analysis was the breakthrough. I looked at each competitor's authority score, keyword rankings, organic traffic, traffic value, backlinks, total content pages, and calculated traffic per page. You can see Eon gets almost zero traffic. Their competitors are different—you can see the pattern immediately. It's not just a volume game; traffic per page is the telling metric. And when you compare them against the medium, it becomes concrete: here's where you are, here's where competitors are, here's why they're winning. That kind of narrative is powerful because it's the only way to reach those conclusions.

This audit work was about $50 in API credits—not crazy, but definitely wasteful. But here's the thing: I can give the methodology to an AI model, ping all the models, aggregate findings from all of them. Unlike visibility, where we need to probe the web continuously, these other domains can be qualitative deep research. We don't need to probe everything—we can be smarter about it.

My ideal scenario: I shape this into a coherent prototype, Estevão takes it and creates the overall structure with me, we do sketching sessions and rapid mocks, and validate the design direction. The goal is to get an end-to-end prototype—not the final product, but working enough to see if this is the right direction before we hand it to the full team as backlog.

**Estevão Mascarenhas:** I think what you've shown me already gives me ideas for how to extend the app. But I want to clarify: are you thinking of building something entirely new from a UI perspective—using CheckThat's look and feel as inspiration? Or should we think about how to fit this into our current product experience?

**Marcel Santilli:** There are really three outputs, and I need to sequence them. First, the public pages: we want to show composite scores and trends—adoption over time, charts—not just visibility. Visibility only tells part of the story. If we layer in how AI perceives the brand, the overall market reputation, plus presence and visibility, it becomes way more concrete and contextualized.

But that's output two. Output one is simpler: nail a single report for a single brand. A customer comes in, they say "help me understand what's going on"—and we give them a snapshot. That's the hook. I'm modeling this after Amplitude's AI Visibility grader, which is simple but effective. They haven't updated it since November, and they clearly don't care about it—but it works because it's straightforward and actionable.

Output three is the dashboard redesign. Right now, from an SEO perspective, users want this information—they're searching for it. But from a usage perspective, nobody gets any value from the dashboard as it exists. Even I look at it and think "just give me the data so I can run an agent on it." The dashboard alone is too overwhelming. Unless we can turn it into narrative—like an audit—it's going to be less useful than an agent with MCP access to the raw data.

The dashboard is good as a data foundation, but it needs layers: data processing, data pipelines that turn raw information into "oh, I see what's happening." When you look at adoption year-over-year in the right way, suddenly you see the story: HubSpot is declining, Salesforce is stable. You couldn't reach those conclusions any other way. That's why visualization and narrative matter—it's not just data, it's interpretation.

**Estevão Mascarenhas:** This makes sense. If we nail one awesome report—figure out what goes on the public page, what goes behind the paywall—then it becomes a monetization and presentation problem. The data is all there; we just need to shape the product around it.

**Marcel Santilli:** Exactly. Let's start with one report and make it incredible. All the data exists; we figure out presentation and packaging after.

**Marcel Santilli:** The reports can pull data from multiple sources over time and could be packaged as GrowthX, not just CheckThat. But here's the thing: audits are core to every engagement kickoff we do. We have to analyze the brand, map the competitive landscape, understand the space. That's baseline work. Right now everyone's just prompting Perplexity or doing one-off Semrush lookups. We can do this way more systematically, and some of these components don't have to be perfect immediately—they're just ways to visualize outputs of work we're already doing. This is massive lead gen potential for both the services side and the product side.

**Stevie Kim:** So when you're doing the report, are you expecting to build this into the onboarding experience where we kick off workflows, or are you doing this separately? And when you launch it—is this for free users or paid? Where's the line?

**Marcel Santilli:** Once we have a solid report, we can figure out the monetization. But my hope is that this becomes the standard across all categories—something people start sharing publicly. A CEO will screenshot a page and link to it because it says "look at us." That's the virality hook. Public pages show lightweight scores plus a glimpse of the audit; full audits are for paid users. Look at Crunchbase—they do this well. You can see trends publicly, but lots of paywalls.

**Stevie Kim:** So lightweight scores and audit preview publicly, full audit behind paywall.

**Marcel Santilli:** Exactly. Show essential modules, unlock deeper modules. You're still showing the headline, but the depth is paid.

**Estevão Mascarenhas:** Let me make sure I understand. You have a manually-built prototype that's in good shape. Our job is to automate it—create workflows and presentation layers for an end-to-end working prototype. Not the final product, but real enough to validate direction. Then it becomes backlog for the full team.

**Marcel Santilli:** Yes. Though as we do this, let's be smart about what we systematize. If we're going to pull analyst data, we might as well pick a category—let's say it has 50 players—and make sure we create profiles for all 50 and track them all. We do it once to figure out what should live in our public data layer so deep research can fetch information externally. The math is actually reasonable: 200 categories × 50 shortlist players = 10,000 pages. Not crazy. And you don't need daily updates—monthly is fine for most things. Company descriptions don't change weekly. So deep research aggregates information, we pull mostly from our public profiles, but we validate end-to-end and iterate. I'm going to run to another meeting, but let me sync with Daniel and I'll get back to you both on next steps.
