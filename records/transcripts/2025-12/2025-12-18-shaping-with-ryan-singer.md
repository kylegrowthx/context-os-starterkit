# Shaping with Ryan Singer

<metadata>
date: 2025-12-18
time: 16:00 UTC
duration: 180 minutes
organizer: marcel@growthxlabs.com
participants:
  - name: Marcel Santilli
    company: GrowthX
    role: CEO
  - name: Daniel
    company: GrowthX
    role: Engineering
  - name: Ryan Singer
    company: Felt Presence
    role: Product Strategist
fireflies_id: 01KCR1GCBQ9708B16NEMJNK9FR
transcript_url: https://app.fireflies.ai/view/01KCR1GCBQ9708B16NEMJNK9FR
source: fireflies
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX is bottlenecked on editorial capacity, not AI quality. Editors spend 5 hours per article instead of the 15–30 minute target, preventing growth past $2M annual revenue. Ryan Singer facilitated a redesign of the client feedback system to be structural (not Google Docs), adding tier-one text comments and tier-two strategic feedback (style, tone, accuracy). The team committed to building a rich text editor with submission control points, tokenized client access links, and a monitoring dashboard by January 2026—deferring legal/sign-off workflows to stay focused.

---

## Context

GrowthX transitioned from traditional $1.50/word agency model to AI-powered content production at 10–20 cents/word—a 90% cost reduction with 70% gross margins. The Deepgram engagement demonstrated scale: 3,000 pages produced with minimal manual overhead and $10–20k monthly contracts. But the business cannot grow without solving the editorial capacity problem. Editors lack visibility into time spent, consistent tools, and clear "publish-ready" criteria. Clients (Biologica, Clerk, others) churn when calibration fails. Marcel brought Ryan Singer in because he specializes in product strategy and workflow design—this is a systems problem, not a content problem.

The team has identified the bottleneck precisely: editorial review, not AI generation. The conversation focused on how to structure client feedback loops and track editorial effort so quality becomes repeatable and scaling becomes possible. Ryan's expertise in shaping and scoping work aligned perfectly with GrowthX's need to prioritize the right problem and avoid scope creep on legal/compliance workflows before January.

---

## Relevance

**GrowthX Services (Content Production Platform)**
- Editorial workflow bottleneck is blocking revenue growth and client retention
- Client calibration process (3-step: context setting, guidelines, sample reviews) is currently ad hoc and unreliable
- Feedback currently flows through Google Docs—unstructured, context-lost, unmeasured
- Solution requires tooling (rich text editor, structured forms, submission checkpoints) to support repeatable, scalable quality

**Product & Engineering**
- Daniel's text editor enhancements (comment features, revision tracking) are foundational to the feedback system
- AI agents for style, research, and structural feedback can process client input and refine prompts
- Monitoring dashboard needed to catch editorial bottlenecks in real-time
- Tokenized client access (Airtable/Figma-style shareable links) reduces friction and lowers engineering lift vs. full account provisioning

**Business Development & Client Success**
- Scaling editorial capacity directly enables growth from current $2M to $5M+ ARR
- Structured feedback mechanisms improve client satisfaction and reduce churn risk (Biologica, Clerk cases)
- Clear "publish-ready" criteria and sign-off process reduce client friction and disputes
- Proper calibration means better data for fine-tuning and supervised learning

---

## Decisions & Commitments

**Tier-One vs. Tier-Two Feedback**
- Tier-One: inline text comments for localized errors and clarifications
- Tier-Two: structured feedback forms (quiz/survey format) for strategic input on style, tone, accuracy, research quality

**Tooling Stack**
- Rich text editor (Tiptap-based) with comment/revision features
- Submission control points to trigger client review rounds and track revisions
- Structured feedback forms to guide clients away from unstructured Google Docs input
- Monitoring dashboard to visualize simulation runs and editorial throughput per editor

**Client Access Model**
- Tokenized/whitelisted shareable links (Airtable/Figma/Basecamp-style) to avoid full account provisioning
- Lightweight, friction-reduced client experience to improve adoption and feedback quality

**Scope Boundaries (January 2026)**
- IN SCOPE: Editorial transparency, client feedback capture, submission checkpoints, monitoring
- OUT OF SCOPE: Complex legal sign-off workflows, multi-stakeholder approval chains, full compliance integration
- Rationale: Solve the editorial bottleneck first; legal workflows can be layered in post-January

**Success Metric**
- New editors do not repeat previously identified mistakes (measured through feedback categorization and model fine-tuning feedback loops)

---

## Open Questions

**Feedback Processing & AI Training**
- How should feedback be categorized (style, voice, factuality, research quality) for structured model fine-tuning?
- What supervised learning infrastructure is needed to convert client feedback into training signals?
- How do we measure the quality improvement from fine-tuning feedback loops?

**Editorial Capacity**
- What is the realistic throughput target for a trained editor per week?
- How do we onboard and train new editors to prevent repeating known mistakes?
- What skills/expertise gaps do existing editors have?

**Client Feedback Quality**
- How do we ensure clients actually use the structured feedback forms vs. reverting to ad-hoc comments?
- What guardrails prevent clients from over-specifying or creating scope creep through feedback?
- How do we balance client input with editorial independence and brand voice?

**Implementation Details**
- What is the MVP for the rich text editor before full feature richness?
- How should the monitoring dashboard surface editor activity and bottlenecks?
- Should tokenized links be time-limited or permanent?

---

## Overview & Key Topics

**Core Problem:** Editorial capacity is the bottleneck, not AI quality. Current manual processes and Google Docs feedback loops prevent scaling beyond $2M ARR.

**Key Topics Discussed:**
- Editorial capacity and time tracking (5 hrs/article vs. 15–30 min target)
- Client calibration process: 3-step (context setting, guidelines creation, sample reviews)
- Feedback system redesign: Tier-One (text comments) + Tier-Two (structured surveys)
- Rich text editor with inline comments and revision tracking
- Structured feedback forms to replace ad-hoc Google Docs
- Submission control points and workflow checkpoints
- Tokenized/whitelisted client access links (no full account provisioning)
- Monitoring dashboard for editor activity and throughput
- AI agents for style, research, and structural feedback processing
- Feedback categorization for supervised fine-tuning
- Scope boundaries: Defer legal/sign-off workflows to focus on editorial transparency by January 2026

---

## Action Items

**Marcel (GrowthX CEO)**
- Provide detailed context documents and structured calibration inputs for clients
- Implement time tracking mechanisms to measure editor effort per article
- Integrate client feedback capture directly into the platform
- Design and build formal submission workflow and staging process
- Collaborate on monitoring dashboard to visualize editor and simulation throughput
- Define success metrics and validate throughput improvements by January 2026

**Daniel (GrowthX Engineering)**
- Enhance text editor with comment and revision tracking features (Tiptap-based)
- Develop AI agents to process style, research, and structural feedback
- Contribute to the design of client feedback experience (forms, surveys, submission flows)
- Implement status management and submission control points
- Explore lightweight, tokenized client access models to reduce provisioning friction
- Build monitoring dashboard to surface editor activity and editorial bottlenecks

**Ryan Singer (Felt Presence, Product Strategist)**
- Facilitate identification of scope boundaries and prioritization to prevent feature creep
- Propose "editor on task monitor" solution for real-time throughput visibility
- Advocate for "digital twin" framing to motivate client investment in structured feedback
- Lead design brainstorming for client feedback integration (Tier-One vs. Tier-Two)
- Coordinate definition of "done" criteria and success metrics for new editors

---

## Full Transcript

### Opening and Context (16:00–16:15)

**Ryan Singer:** I notice you're using multiple recording tools—Fathom, Fireflies. There's little downside to capturing content in multiple ways.

**Marcel Santilli:** Good point. Today I want to dig into our biggest operational challenge: scaling high-quality content production while managing editorial efficiency. We've made huge progress on the AI side, but we're hitting a people bottleneck.

### The Business Model & Current Scale (16:15–16:45)

**Marcel:** Our old model: manual article production, multiple editors and freelancers. Cost us $2 million a year, produced only 20 articles per week. Now with AI workflows—Deepgram is a great example—we're producing 3,000 pages with minimal manual overhead. Monthly contract value: $10–20k per client.

**Daniel:** And we're hitting 70% gross margin at 10–20 cents per word. That's a 90% cost reduction vs. the traditional agency model ($1.50/word).

**Ryan:** But AI alone doesn't guarantee quality.

**Marcel:** Exactly. Quality depends on expert input and process design. That's where we're stuck.

### The Editorial Bottleneck (16:45–17:30)

**Marcel:** The problem: editors spend up to 5 hours per article. Our target is 15–30 minutes. We're nowhere near throughput.

**Daniel:** And we don't have visibility. Editors are mixing Google Docs with our internal systems. No centralized time tracking. No clear "publish-ready" criteria.

**Ryan:** So new editors can't learn from past mistakes?

**Marcel:** Exactly. We can't reproduce quality at scale. And we're losing clients—Biologica, Clerk—because calibration fails.

**Ryan:** What does calibration look like?

**Marcel:** Three steps: (1) context setting—client provides domain, brand guidelines, audience; (2) writing guidelines—we draft editorial principles; (3) iterative sample reviews—client reviews 5–10 samples, we refine until "publish-ready" is defined.

**Daniel:** Problem is, we're doing this in Google Docs. Comments get lost, context disappears, and we can't track editor effort or measure quality trends.

### The Feedback System Redesign (17:30–18:30)

**Ryan:** So you need two layers of feedback.

**Marcel:** Yes, but we haven't structured it.

**Ryan:** Layer One: inline text comments for specific errors—typos, factual problems, style issues on individual blocks. Layer Two: structured feedback—quiz or survey format. Ask the client: "Does this match your brand?" "Is the research deep enough?" "Missing any topics?" That's your strategic input.

**Daniel:** And we collect that structured feedback into a form, not scattered Google Docs.

**Ryan:** Right. Then what?

**Marcel:** We categorize it: style, voice, factuality, research quality. Feed it into supervised fine-tuning for our AI models. Goal is reinforcement learning—automatically improve accuracy over time. But the manual approach right now—converting feedback into prompt adjustments—is unsustainable.

**Ryan:** The platform needs submission control points. Editor submits a draft. Client reviews. Feedback flows back into the system. You track revision rounds. You measure editor time per round.

**Daniel:** We could use a rich text editor—Tiptap has comment support. Structured feedback forms guide clients toward actionable input.

**Ryan:** And for client access? Do they need full accounts?

**Marcel:** No, that's friction. We want lightweight access.

**Ryan:** Tokenized links. Airtable does this, Figma, Basecamp. Shareable URLs that don't require signup. No account provisioning overhead.

**Daniel:** That works for us. We could implement it quickly.

### The Monitoring Dashboard (18:30–19:00)

**Ryan:** You also need a dashboard. Track editor activity. How many rounds of revision per article? Time per round? Which topics trigger the most feedback? Where are bottlenecks?

**Marcel:** And simulation runs. We need to see if new editors are repeating old mistakes or improving.

**Ryan:** That's your success metric. New editors don't repeat previously identified mistakes. Measure it through feedback categorization. If you see the same style error from two editors, you flag it and train.

**Daniel:** We can surface that in the dashboard. Show patterns in feedback, anomalies in editor time.

### Scope Boundaries (19:00–19:30)

**Ryan:** Here's what I'd defer. Legal sign-off workflows. Multi-stakeholder approval. Those are complex, and they'll drag your January timeline.

**Marcel:** How do we push back on clients asking for it?

**Ryan:** Frame it this way: "We're building a digital twin of your editorial process. You invest in good feedback, and we refine it continuously. Once you see the quality, we'll add formal sign-off." They'll buy it if quality improves.

**Daniel:** And legally, if we have documented feedback and version history, we're covered.

**Ryan:** Exactly. Scope for January: editorial transparency, client feedback capture, submission checkpoints, monitoring. That's the core. Everything else is phase two.

**Marcel:** Agreed. Clean prioritization.

### Closing: Action Items & Timeline (19:30–20:00)

**Ryan:** So Marcel, your job is to crystallize what "good calibration" looks like for a new client. Document the process. And measure editor time—start tracking now.

**Marcel:** On it. I'll also design the feedback forms. And work with Daniel on the dashboard.

**Ryan:** Daniel, the rich text editor with comments. Submission control points. Lightweight tokenized access. Timeline?

**Daniel:** Editor MVP by mid-January. Forms and dashboard follow.

**Ryan:** Ambitious but achievable. And remember—avoid legal workflows. Stay focused.

**Marcel:** Clear. This is going to unlock growth.
