# Marcel Demos Personal Output system

<metadata>
date: 2026-02-19
time: 19:00 UTC
duration: 72 minutes
organizer: marcel@growthxlabs.com
participants: Clint Shryock, Stefano Zanata, Marcel Santilli, Ben Church, Daniel Lopes
fireflies_id: 01KH96HM55YEGA24Q7PTDEFXF6
transcript_url: https://app.fireflies.ai/view/01KH96HM55YEGA24Q7PTDEFXF6
</metadata>

---

## Summary

Marcel demonstrated a context engineering system that has delivered tenfold productivity gains through organized AI workflows, curated knowledge files, and automated processes. The team discussed a multi-stage research pipeline using Claude Cowork for high-quality outputs and the challenges of integrating complex AI workflows. Plans for company-wide workshops on context engineering were emphasized, along with strategies for evolving the AI framework to support modular, reusable workflows. A new archetype of "automation engineers" was identified, representing non-traditional engineers blending domain expertise with AI tooling.

---

## Action Items

**Marcel Santilli**
- Conduct workshops for company-wide AI coaching and onboarding on context engineering and workflow setup
- Share and maintain the company handbook and starter kit repositories for team access and adaptation
- Continue refining AI skills, rules, and folder structures to improve automation maintainability and accuracy

**Daniel Lopes**
- Focus on integrating reusable workflows/micro apps into the Output framework and consider API unification for workflow execution across products
- Prioritize essential framework features including Sentry integration and cost tracking before expanding large AI capabilities
- Recruit engineering manager for the 4Deploy team to support automation engineers with AI workflow development and deployment

**Stefano Zanata**
- Begin conceptualizing global API endpoints facilitating scalable, distributed workflow execution potentially supporting external Temporal servers

**Ben Church, Clint Shryock, Stefano Zanata, and Marcel Santilli**
- Have follow-up discussions for feedback on new ideas and roadmap refinement

**Unassigned**
- Explore packaging Marcel's complex workflows into reproducible, validated workflows or micro apps for easier company adoption and sharing

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
