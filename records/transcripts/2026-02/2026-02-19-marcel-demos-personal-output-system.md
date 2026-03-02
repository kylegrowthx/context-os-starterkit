# Marcel Demos Personal Output system

<metadata>
date: 2026-02-19
time: 19:00 UTC
duration: 72 minutes
organizer: marcel@growthxlabs.com
participants:
  - name: Marcel Santilli
    company: GrowthX
    role: CEO
  - name: Daniel Lopes
    company: GrowthX
    role: CTO
  - name: Ben Church
    company: GrowthX
    role: VP Product
  - name: Clint Shryock
    company: GrowthX
    role: VP Engineering
  - name: Stefano Zanata
    company: GrowthX
    role: Principal Engineer
fireflies_id: 01KH96HM55YEGA24Q7PTDEFXF6
transcript_url: https://app.fireflies.ai/view/01KH96HM55YEGA24Q7PTDEFXF6
source: fireflies
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Marcel demonstrated a context engineering system achieving 10x productivity gains through structured knowledge curation, AI workflows, and automated indexing. The team aligned on three priorities: packaging workflows as reusable micro-apps, building a scalable API gateway for unified workflow execution across products, and educating the company on context-native knowledge work. A new role emerged—"automation engineers"—bridging domain expertise and AI tooling, representing rapid market shift toward democratized AI development.

---

## Context

Marcel has spent months building a personal productivity system centered on "context engineering"—organizing company knowledge, voice guidelines, decision-making personas, and AI-native workflows into a structured workspace accessible to Claude and Cursor agents. This system powers GrowthX's content marketing service and informs the design of CheckThat (OpenAI visibility index). The leadership team (Daniel Lopes/CTO, Ben Church/VP Product, Clint Shryock/VP Engineering, Stefano Zanata/Principal Engineer) gathered to evaluate whether this personal model can scale into Output, the company's planned AI workflow automation product. The conversation explores both the technical architecture (storage, APIs, workflow composition) and organizational implications (new role types, skill distribution, knowledge management practices).

---

## Relevance

**CheckThat (Product Strategy)**
- Context engineering architecture informs design decisions for Output's workflow automation platform
- Storage and API challenges identified are core product infrastructure needs
- User research on "automation engineers" shapes go-to-market and feature prioritization

**GrowthX Services (Operations & Delivery)**
- Context curation approach directly enables high-quality content marketing delivery at scale
- Proposed company-wide workshops on context engineering directly impact team productivity
- Knowledge management practices model extends to scaling team across new engagements

**Technology & Infrastructure**
- Global API gateway design proposed for unified workflow execution across products
- Temporal server integration and distributed execution architecture discussed
- MCP (Model Context Protocol) server integration patterns identified as critical and unstable

**Team & Organization**
- New "automation engineer" archetype identified (George, Tammy, Sergey as examples)
- Shift toward democratized AI engineering suggests hiring and team structure implications
- Knowledge work productivity multiplier (10x claimed) impacts hiring needs and capacity planning

---

## Decisions & Commitments

**Agreed Priorities for Output Platform**
1. Package Marcel's workflows as reusable micro-apps with skill registry and reproducible validation
2. Design global API gateway for unified workflow execution, supporting bring-your-own Temporal server pattern
3. Establish dedicated storage service for context/metadata management separate from core product

**Sequencing & MVP Scope**
- Prioritize web product stabilization: cost tracking, Sentry integration, error monitoring before advanced AI features
- Defer complex storage/workflow embedding into framework; focus on best-practice documentation and education
- Personal/hyper-individualized workflows remain internal tools, not product features

**Organizational Commitment**
- Marcel to lead 5-hour company-wide workshop on context engineering and AI workflow setup
- Maintain and share company handbook and starter kit repositories for team adaptation
- Establish standardized VS Code workspace setup combining product code and handbook for AI-native development

---

## Open Questions

- How to handle MCP server integration stability and error handling at production scale?
- What storage abstraction best supports both short-term and long-term memory patterns for AI workflows?
- How to evaluate and maintain quality consistency for user-generated workflows via skill registry?
- What organizational structure best supports "automation engineers" (hiring, reporting, skill development)?
- How aggressive should Output pursue external user adoption vs. internal GrowthX use cases?

---

## Action Items

**Marcel Santilli (GrowthX/CEO)**
- Conduct 5-hour company-wide workshop on context engineering, AI workflow setup, and knowledge curation best practices
- Publish company handbook and starter kit repositories with documentation on folder organization and maintenance practices
- Continue refining AI skills, rules, and folder structures; document lessons learned for team adoption

**Daniel Lopes (GrowthX/CTO)**
- Lead technical design for Output platform: integrate reusable workflows as micro-apps, plan API unification for cross-product execution
- Establish MVP scope: prioritize Sentry integration, cost tracking, and error monitoring before advanced AI features
- Recruit engineering manager for 4Deploy team to mentor automation engineers on AI workflow development and deployment

**Stefano Zanata (GrowthX/Principal Engineer)**
- Conceptualize global API gateway architecture supporting distributed workflow execution with bring-your-own Temporal server pattern
- Design storage service abstraction for context, metadata, and long-term/short-term memory management

**Ben Church (GrowthX/VP Product)**
- Gather team feedback on "automation engineer" archetype (role definition, skill requirements, career path)
- Document emerging user archetypes and market signals for product strategy refinement

**Cross-Functional (Ben Church, Clint Shryock, Stefano Zanata, Marcel Santilli)**
- Schedule weekly follow-up meetings to refine roadmap, implementation approach, and organizational structure
- Establish standards for VS Code workspace setup and multi-folder AI development practices

**Unassigned/Next Sprint**
- Package Marcel's complex workflows as reproducible, validated micro-apps for skill registry and team sharing
- Define evaluation criteria and quality assurance process for user-generated workflows in Output platform

---

## Overview & Key Topics

**System Architecture & Design**
- Context engineering model: folder structures, voice/persona/knowledge curation, automated indexing, MCP server integration
- Multi-stage research pipeline: input → scratchpad → output → study guides (with Claude Cowork execution)
- Storage challenges: context metadata, chunk overlap, short-term vs. long-term memory abstractions
- Proposed solutions: dedicated storage service, global API gateway, Temporal server integration for distributed execution

**Workflow Composition & Packaging**
- Current: modular local file I/O with remote execution
- Target: reusable skills/micro-apps via registry, composable workflows (workflows calling other workflows)
- QA approach: offline evaluation loops using Phoenix frameworks, consistent voice/persona outputs for testing

**Organizational & Market Dynamics**
- Emerging "automation engineer" archetype: non-traditional coders with domain expertise learning AI tooling
- Examples: George, Tammy, Sergey rapidly adopting Cursor and Claude for workflow automation
- Market signal: split between web app users and technical users narrowing faster than expected
- Implication: hiring, team structure, skill development strategies must adapt

**Output Platform Product Implications**
- Use case fit: repeatable, consistent workflows well-suited; hyper-individualized use cases better as personal tools
- MVP priorities: stabilize core product, cost tracking, error monitoring before advanced AI features
- Scaling strategy: education on context curation, folder organization, best-practice guides over embedded complexity
- Integration pattern: VS Code workspaces combining product code and handbook for multi-folder AI sessions

**Company Knowledge Management**
- Company handbook converted to AI-readable workspace (methodology, benchmarks, product vision, operational context)
- Starter kit created for replication (2-hour setup reveals significant "aha moments")
- Ongoing requirements: regular cleanup, rule updates, context integrity maintenance

---

## Transcript

**Marcel Santilli:** Hey everyone, thanks for joining. I wanted to walk through some recent productivity gains we've achieved through AI integration.

**Daniel Lopes:** Great, we're excited to see what you've built.

**Marcel Santilli:** So I created a Context OS starter kit after investing dozens of hours curating and organizing knowledge. The system uses curated voice, roles, and personal context files with automated indexes and readme updates. This structured context allows complex multi-step workflows, deep research, and integration with MCP servers for tools like HubSpot.

**Ben Church:** That sounds powerful. What kind of productivity gains are we talking about?

**Marcel Santilli:** About 10x productivity boost. The system is built on consistent voice, personas, and folder structures that enable AI to generate highly accurate, on-brand outputs. I've been able to process hundreds of sources for high-quality research results that outperform traditional tools.

**Clint Shryock:** How is this structured? What does the folder organization look like?

**Marcel Santilli:** It includes readmes, indexes, skills, and rules. Everything is automated to update and maintain context files. For example, I have a deep research workflow that operates in stages: input, scratchpad note-taking, output, and polished study guides. Each stage uses Claude Cowork and integrates with MCP servers to pull real data.

**Stefano Zanata:** What are the main challenges you've encountered?

**Marcel Santilli:** Complex workflows with many thought steps expose gaps in current AI skill capabilities. Rules effectively maintain file system indexes and archives, but they don't cover nuanced multi-step logic. MCP server integration is promising but unstable, requiring ongoing skill tuning and error handling. I cap Cloud MD files to under 60 lines to optimize prompt efficiency.

**Daniel Lopes:** This is exactly what we need to think about for the Output platform. How do we scale this to company-wide adoption?

**Marcel Santilli:** Workshops are key. I'm planning a five-hour workshop to scale knowledge work productivity. The company handbook now lives as a curated workspace accessible by Claude and Cursor. This approach promises to make the company 10x more productive by enabling AI-native workflows across roles.

**Ben Church:** What about packaging these workflows?

**Marcel Santilli:** That's critical. My pipeline is modular with local file inputs/outputs and remote executions. The vision includes wrapping workflows as reusable skills and sharing them via a registry. This supports composability, where workflows can invoke other workflows to build complex AI-driven processes. Non-technical users could leverage technical workflows without deep coding knowledge.

**Daniel Lopes:** Storage and context management is a core challenge though.

**Marcel Santilli:** Absolutely. Storage of context, metadata, and chunk overlap is a hard problem. The current storage approach on OS needs rethinking due to complexity. We should consider a separate dedicated storage service integrated with the framework for adding and pulling context. This would support short-term and long-term memory abstractions and be scalable.

**Daniel Lopes:** I'm thinking we should publish common workflows like transcript post-processing and role creation to a registry. This reduces random workflow creation and ensures quality reproducibility across the company.

**Stefano Zanata:** What about API design? Should we create a global API gateway?

**Daniel Lopes:** Yes. We should enable a scalable global API to unify endpoint access across products. Users could bring their own temporal servers but use a common API for communication. This would enable seamless integration across the company and external users.

**Ben Church:** I want to highlight something here. We're seeing a new class of engineers emerge who aren't traditional coders but have an engineering mindset.

**Marcel Santilli:** Exactly. Examples include George, Tammy, and Sergey. They're learning coding and automation to build AI workflows. This bridges the gap between technical and non-technical roles, enabling faster AI-driven innovation.

**Daniel Lopes:** Users previously seen as non-technical are rapidly adopting tools like Cursor and Claude. The split between web app users and technical users is narrowing faster than expected.

**Clint Shryock:** What about quality assurance for these workflows?

**Stefano Zanata:** Consistent voice and persona outputs open opportunities for sophisticated offline evaluation. Integrating evaluation loops could improve quality and consistency across AI-generated content. We could use Phoenix evaluation workflows and offline testing frameworks.

**Marcel Santilli:** Some AI workflows might not map well to Output's core product though. Output excels with repeatable, consistent workflows but may not serve hyper-individualized use cases. Personal productivity workflows might be better suited as personal or internal tools.

**Daniel Lopes:** That's important to distinguish. Let's prioritize stabilizing the web product with cost tracking, error monitoring, and basic AI features first. Advanced ideas like Marcel's are exciting but not immediately feasible for the first release.

**Ben Church:** What about documentation?

**Marcel Santilli:** The company handbook is central. I converted it into a highly curated AI-readable workspace with methodology, benchmarks, product vision, and operational context. It serves as the primary source for AI agents to generate consistent outputs. I also built a generalized starter kit to help others replicate the context setup. It's a two-hour effort but reveals many aha moments.

**Clint Shryock:** How do we share best practices?

**Marcel Santilli:** Rather than embedding complex storage/workflow into the framework, we should share best practice guides. Education on context curation, folder organization, and cleanup improves adoption and output quality. Maintaining context integrity requires ongoing cleanup, rule updates, and planning.

**Daniel Lopes:** Integration across tools is important too. I use VS Code workspaces combining product code and handbook folders for multi-folder AI sessions. This allows Claude and Cursor agents to access all required context in one session.

**Stefano Zanata:** We should standardize this setup across teams and products.

**Marcel Santilli:** Agreed. This cultural shift will position the company as an AI-native organization with a competitive edge.

**Ben Church:** One more thing - I shared an anecdote about a veterinarian owner who developed internal apps and faced typical engineering frustrations. This highlights how domain experts across industries are becoming accidental engineers.

**Daniel Lopes:** The market trend toward democratized AI engineering supports our approach. Understanding these shifts helps prioritize building accessible, reusable AI workflow tools.

**Marcel Santilli:** So to summarize, we should focus on three areas: packaging workflows as micro-apps, building a scalable API for integration, and fostering a culture of AI-native knowledge work through workshops and documentation.

**Daniel Lopes:** Let's schedule follow-ups to refine the roadmap and discuss implementation details.

**Stefano Zanata:** I'll start conceptualizing the global API and distributed workflow execution.

**Ben Church:** And I'll gather feedback on the automation engineer archetype and how to support this emerging role.

**Marcel Santilli:** Perfect. Let's reconvene next week to align on priorities.
