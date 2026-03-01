# GrowthX <> ABK - Partnership Scoping

<metadata>
date: 2026-02-25
time: 22:00 UTC
duration: 43 minutes
organizer: marcel@growthxlabs.com
source: fireflies
enriched_on: 2026-03-01 00:00 UTC
participants:
  - name: Marcel Santilli
    title: CEO
    company: GrowthX
    email: marcel@growthxlabs.com
  - name: Tyler Pavlas
    title: Founding AE
    company: GrowthX
    email: tyler@growthxlabs.com
  - name: Alexander Kehaya
    title: Founder/CEO
    company: ABK
    role: Index Podcast Host
  - name: Pontus Andersson
    title: Chief of Staff
    company: ABK
fireflies_id: 01KJ5HCT0YXXBPJ3RGTW4JBXZZ
transcript_url: https://app.fireflies.ai/view/01KJ5HCT0YXXBPJ3RGTW4JBXZZ
</metadata>

---

## Summary

Marcel (GrowthX) and Alexander (ABK) explored a deep partnership around agent commerce and orchestration. ABK is building Interchange, a governance/security layer for multi-agent enterprise workflows that leverages HTTP 402 payment standards to enable agent-to-agent transactions. GrowthX and ABK agreed to collaborate on paid workshops (starting with GrowthX's March 20 CEO OS workshop), podcast appearances, and co-created content to validate product-market fit and build early adopter communities.

---

## Context

This is a scoping call between GrowthX (B2B content marketing and workflow-as-code thinking) and ABK (agentic commerce and Interchange platform). Alexander and Pontus have been operating ABK for ~2 years after Alexander's experience at Solana Labs and Solana Foundation (2016-present crypto background). Alexander runs the Index Podcast (120k YouTube subs), where he covers AI and crypto topics.

The connection: through Peter Griggs (mutual contact), Alexander and Marcel discovered alignment on agent orchestration, governance, and enterprise workflows. Alexander and Marcel previously worked together at Opus Logica in Santa Barbara, where they were mentored by Brian Fox (open source pioneer, Bash creator, GPL author). This is the first deep technical/business conversation since those early days.

---

## Relevance

**ABK & Interchange Platform:**
- Agent commerce infrastructure (governance, security, payment orchestration)
- HTTP 402 payment standard implementation
- Enterprise multi-agent workflow orchestration
- Policy enforcement, identity, auditing layer

**GrowthX Alignment:**
- Workflows as code (runtime infrastructure)
- Agent safety and guardrails (no unsupervised autonomy)
- Enterprise go-to-market validation
- Workshop-based community and credibility building

**Potential Collaborations:**
- Paid workshops introducing Interchange to enterprises
- Index Podcast appearances on agent workflows and AI-driven GTM
- Joint workshop development combining ABK's technical story and GrowthX's CEO/workflow framework
- Co-created content for early adopter distribution

---

## Decisions & Commitments

**Made During Call:**
1. ABK will explore ABK CEO/CTO internally coordinating on technical clarity around Interchange runtime
2. GrowthX + ABK agreed to pursue joint workshop collaboration (starting with March 20 CEO OS workshop)
3. Alexander + Marcel agreed to podcast appearance on Index Podcast
4. Both sides committed to use case validation and co-creation on GTM content
5. Workshop model chosen as near-term revenue + credibility play before full product monetization

**Timeline:**
- March 20, 2026: GrowthX CEO OS workshop (ABK to attend + explore joint workshop)
- Following week: Deep dive on use cases and technical specifics
- TBD: Index Podcast recording, joint workshop planning

---

## Open Questions

- **Technical Integration**: What specific Interchange runtime details are relevant to GrowthX's workflow framework? (ABK engineering to clarify)
- **Workshop Scope**: How will joint workshop differentiate? (Interchange governance + CEO OS workflow design?)
- **Revenue Sharing**: What's the commercial model for joint workshops vs. content co-creation?
- **Use Cases**: Which enterprise workflow problems should they target first for validation?
- **Timeline**: When can ABK move from prototype → design partner validation phase?

---

## Action Items

**Alexander Kehaya (ABK CEO)**
- Schedule Marcel's appearance on Index Podcast (target: Q1 2026)
- Attend GrowthX CEO OS workshop on March 20, 2026
- Coordinate with ABK CTO to clarify Interchange runtime technical details for GrowthX framework alignment
- Work with Marcel on joint workshop content and go-to-market strategy

**Marcel Santilli (GrowthX CEO)**
- Send ABK resources/code for historical AI growth workshops
- Share March 20 CEO OS workshop details and logistics
- Provide documentation on CEO OS framework and workflow methodology
- Coordinate with Tyler on joint workshop development and use case validation

**Tyler Pavlas (GrowthX Founding AE)**
- Lead follow-up discussions on workshop content development with Alexander and Marcel
- Support use case exploration and co-creation of GTM content

**Pontus Andersson (ABK Chief of Staff)**
- Coordinate internally on Interchange runtime technical documentation for GrowthX review
- Support external partnership development and dogfooding coordination

---

## Overview & Key Topics

**Topics Covered:**
- Agent commerce and autonomous agent-to-agent transactions
- HTTP 402 payment standard for server-to-server payments
- Interchange platform architecture (governance, security, orchestration)
- Enterprise multi-agent orchestration and workflow automation
- Policy enforcement, identity, and auditing for agent systems
- Design partner go-to-market validation strategy
- Workshop-based community building and early revenue
- Podcast content and thought leadership
- CEO OS framework and workflows-as-code methodology
- Collaboration opportunities on content, workshops, and product validation

**Key Themes:**
1. Agent safety requires governance layers, not full autonomy
2. Blockchain payment rails + open standards enable decentralized agent networks
3. Design partners → workshops → community → product monetization (sequential GTM)
4. Content + credibility (podcast, workshops) precedes product sales
5. Workflow frameworks (CEO OS) and technical orchestration (Interchange) are complementary

---

## Transcript

**Tyler Pavlas:** Thanks for bringing the recorders in. I'm the founding AE at GrowthX and I work really closely with our CEO Marcel. Pontus, would love a quick intro from you.

**Pontus Andersson:** Rock on.

**Tyler Pavlas:** Pontus has been working with Alex and the rest of the gang over at ABK for quite a while—almost five years. He leads operations, go-to-market, and strategy for ABK.

**Alexander Kehaya:** Yeah, we've got some stuff that I think is relevant to what you guys have probably already built in-house. It's called Interchange—that governance, policy, orchestration, and security auditing layer that we think ties directly into the economic side where agents are starting to transact with each other and buy things online. We started with payment rails, but we think this governance aspect is needed to make this all get adoption at Enterprise.

**Marcel Santilli:** Can you guys hear me okay?

**Alexander Kehaya:** Yeah, I can hear you fine. Good to see you. I think we talked a year or two ago through Peter Griggs. You probably remember we cut our teeth together as entrepreneurs at Opus Logica in Santa Barbara. My business partner was the original founder—Brian Fox. He wrote Bash back in the day, authored the GPL licenses. Really cool guy who took me under his wing when I was bootstrapping a SaaS business. That's how I met Peter Griggs—we were both entrepreneurs hacking together. Pontus is my chief of staff. We've been working together across multiple companies for about five years. We started ABK like two years ago. I was an early employee at Solana Labs and the Solana Foundation. I've been in crypto mostly since 2016. I have a podcast called the Index Podcast where we talk about the future of the Internet—AI to crypto. About 120,000 subs on YouTube.

**Alexander Kehaya:** This is important: about a year ago on my show, the head of developer relations at Coinbase told me about HTTP 402—payments over HTTP. 402 is a response code for "payment required." Tim Berners-Lee thought maybe people want to make payments server-to-server, so they built that into HTTP. But at the time, there was no technology to do it. Blockchain is perfect for this. Coinbase acquired Earn.com (which Lily ran with Balaji), and they were looking at 402. That idea got absorbed into Coinbase. Last year, somebody made an open-source specification for it.

**Tyler Pavlas:** So this is HTTP 402, the standard?

**Alexander Kehaya:** Exactly. The vision is that agents can now pay each other to use tools and services. If you have multiple agents working within an enterprise, they can discover new APIs and services. Instead of having a human approve and manage every interaction, agents can autonomously transact with each other. The governance and security layer Pontus and I are building manages this.

**Marcel Santilli:** So you're essentially building the operating system for agent commerce?

**Alexander Kehaya:** Exactly. We call it Interchange. It's modular, open-source, and chain-agnostic. Enterprises adopt it as the orchestration layer for their agent teams.

**Marcel Santilli:** I love this. It aligns with what we've been thinking about—workflows as code and runtime infrastructure. In my work with agents, full autonomy without guardrails is dangerous. You need policy enforcement, identity, auditing. That's what you're building.

**Alexander Kehaya:** Absolutely. That's the core. We're currently dogfooding internally to validate use cases.

**Marcel Santilli:** How far along are you in the product?

**Alexander Kehaya:** We're in prototype stage. Limited multi-agent orchestration so far, but we're seeing real value in simple agent "skills" for CEO-level productivity improvements. The long-term vision is enterprises running teams of agents that automate complex workflows.

**Tyler Pavlas:** What's the go-to-market strategy?

**Alexander Kehaya:** We're starting with design partners who can use Interchange internally to solve enterprise workflow problems. This validates product-market fit and builds credibility. Eventually we transition to product monetization through agent wallet transactions and API marketplace access.

**Marcel Santilli:** That's a solid approach. I'd recommend adding workshops to that mix. Based on my experience at Scale AI and HashiCorp, workshops validate demand, build community, and generate early revenue before scaling SaaS. I'm hosting a CEO OS workshop on March 20 that's been really successful. You should check it out.

**Alexander Kehaya:** Absolutely. I'd love to attend and explore doing a joint workshop with you.

**Marcel Santilli:** There's real synergy here. Your podcast plus my workshop platform could reach a lot of people interested in this space.

**Alexander Kehaya:** Yeah, we'd definitely love to have you on the Index Podcast to talk about agent workflows and AI-driven go-to-market.

**Tyler Pavlas:** This could be a real partnership.

**Marcel Santilli:** I'm going to send you some resources on the workshops. Maybe we can dive deeper on use cases next week.

**Alexander Kehaya:** Perfect. I'll follow up on scheduling the podcast appearance too.

**Pontus Andersson:** From our side, we'll get our engineering team to clarify technical details on the Interchange runtime that might be relevant to your framework.

**Marcel Santilli:** That would be great. There's real opportunity here to collaborate and advance the space.

**Alexander Kehaya:** Agreed. Let's stay in touch and keep this momentum going.

**Tyler Pavlas:** Thanks for the conversation. This has been really valuable.

**Pontus Andersson:** Yeah, excited about the possibilities.

**Marcel Santilli:** Me too. Talk soon, everyone.
