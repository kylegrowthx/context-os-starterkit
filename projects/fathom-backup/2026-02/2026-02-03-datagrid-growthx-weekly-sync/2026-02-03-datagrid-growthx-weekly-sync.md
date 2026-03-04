# Datagrid <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-03
time: 17:31 UTC
duration: 24 minutes
organizer: team@growthxlabs.com
participants: Liz Kushnereit (GrowthX), Marcel Santilli (GrowthX), Kaitlin Quimby (Datagrid), Thiago da Costa (Datagrid)
fathom_recording_id: 119362429
fathom_url: https://fathom.video/calls/547566938
share_url: https://fathom.video/share/WfnFpQMy7esjGBe2NwP6JfNxm-gqFzAC
source: fathom
enriched_on: 2026-02-27 15:32 UTC
</metadata>

---

## Summary

GrowthX presented a major website transformation: moving from a blog-driven awareness model to a product-led discovery and activation platform. The redesign will rebuild the site outside Webflow, embed the Datagrid app directly, and organize content around agent-based clusters using a three-phased rollout (Agents, Guides & PSEO, then Connectors). Users will fork pre-configured agents directly from the website, dramatically reducing time-to-value.

---

## Context

Datagrid is GrowthX's technology partner for a strategic website and content overhaul. The relationship centers on embedding Datagrid's AI agent platform directly into Datagrid's public-facing website, turning it into a product-led discovery surface. Datagrid's product team (Kaitlin, Thiago) needed to align with GrowthX's broader strategy: repositioning the website as a knowledge graph that serves both human buyers and AI agents training on Datagrid's brand. This meeting was the detailed walk-through where Liz Kushnereit (GrowthX's Head of GTM) and Marcel Santilli (CEO) presented the full taxonomy, content strategy, and implementation roadmap to get Datagrid's buy-in on the timeline and scope division.

---

## Relevance

**GrowthX Delivery**
- Website overhaul reduces Webflow constraints; enables rapid iteration and design refresh for all future client work
- Knowledge graph approach (flat URL structure, dynamic tagging, cross-linking) is reusable pattern for other product clients (e.g., Augment, Lovable examples cited)
- Agent-based content clustering moves from keyword-chasing to product-velocity model—scalable methodology for other AI product companies

**CheckThat / AI Visibility**
- PSEO and guide-based content strategy expands Datagrid's AI visibility across training datasets and agent search
- Pre-configured agent kits ("fork" workflows) directly address time-to-value friction; model proven with Lovable templates (double-digit activation rates)

**Business Development**
- Scope clarification (GrowthX owns website refactoring + content infrastructure; Datagrid owns product marketing decisions) prevents scope creep
- Parallel work streams (immediate PSEO/Guides rollout vs. longer Webflow rebuild) unlock faster value and content indexing wins

---

## Overview

- **Strategic Pivot:** The website will shift from a blog-led awareness channel to a product-led discovery and activation layer, with "Agents" as the central hub.
- **Content Engine:** Content will be built around "Agent-based clusters" to create velocity, moving from keyword-chasing to a product-driven strategy.
- **Website Overhaul:** GrowthX will rebuild the site outside Webflow to enable rapid development and a design refresh, while Datagrid will embed the live app for a seamless user experience.
- **Accelerated TTV:** The site will use the Datagrid API to let users "fork" pre-configured agents directly from the website, dramatically reducing time-to-value (TTV).

---

## Key Topics

### Strategic Pivot: Product-Led Discovery

  - **Goal:** Shift the website from a blog-led awareness channel to a product-led discovery and activation layer.
  - **Three Lanes of Expansion:**
      - **Agents:** The canonical discovery layer.
      - **Connectors:** A marketplace-style hub for enablement.
      - **Guides & PSEO:** The main traffic engines.

### Content Strategy: Agent-Based Clusters

  - **Core Principle:** Content clusters will be built around specific agents, moving from keyword-chasing to a product-driven strategy.
  - **New Site Taxonomy:**
      - **Agents:** Keep existing URL structure.
      - **Connectors:** Keep existing structure, but link directly to the connected integration page (not docs).
      - **PSEO (Programmatic SEO):** New pages for specific use cases (e.g., `agents-for-X`).
      - **Guides:** A new section for full-funnel informational content.
  - **Execution Phases:**
    1.  **Agents:** Prioritize agents and finalize the landing page UX.
    2.  **Guides & PSEO:** Build out the new sections and PSEO templates.
    3.  **Connectors:** Expand integration pages with detailed setup content.

### Website Overhaul & Product Integration

  - **Rationale:** The current Webflow site limits development speed and design flexibility.
  - **GrowthX's Role:**
      - Rebuild the entire website outside Webflow.
      - Refresh the design and improve content readability.
      - Create a maintainable code repo for future updates.
  - **Datagrid's Role:**
      - Embed the live Datagrid app directly into the website.
      - This ensures a consistent design system and provides a seamless user experience.

### Accelerating Time-to-Value (TTV)

  - **Mechanism:** The site will use the Datagrid API to let users "fork" pre-configured agents directly from the website.
  - **Agent Kits:** These kits include knowledge bases (e.g., OSHA standards), attachments, and instructions.
  - **Benefit:** This dramatically reduces TTV by providing users with a ready-to-use agent environment, a strategy proven to drive high activation rates (e.g., Lovable templates see double-digit conversions).

---

## Action Items

**Kaitlin Quimby (Datagrid)**
- Notify product team re: Notion-to-product sync for Agent library

**Liz Kushnereit (GrowthX)**
- Prioritize initial Agents with Thiago & Kaitlin; then build Agent landing page UX

**Marcel Santilli (GrowthX)**
- Scope parallel out-of-Webflow rebuild; share design and dev plan with Thiago & Kaitlin
- Define embed/API integration strategy with Thiago; then implement "Try this agent" CTAs using Datagrid API

---

## Transcript

**Liz Kushnereit:** Well, I guess I'll screen share. There's a lot to cover. Let me walk through the whole strategy.

**Liz Kushnereit:** So the TLDR is that it's a big pivot from blog-led awareness to product-led discovery, service, and activation layer. There's a lot of moving pieces, but basically agents becomes our canonical discovery layer. Connectors becomes our marketplace-style hub for enablement, and then guides and PSEO become our main traffic engines, and also overlap into enablement, especially for agents in our use case guides.

**Liz Kushnereit:** This is basically three lanes of expansion. Guides and PSEO is more of our editorial content. Agents—we will be taking over this page and optimizing for UX and content. And then Connector is basically the same story: optimizing UX and the content.

**Kaitlin Quimby:** And so I'll have a lot of references, especially on Connector. And then just one thing on the agents: we just want to make sure that we have it aligned. So like whatever we're doing there, updating or if we're changing, we want to reflect it on the product side too. So then the agent library on the product is just matches.

**Kaitlin Quimby:** Right now, for example, we have a Notion page and that's kind of our source of truth. So for updating it on there, I'll let the product team know and then they know to go update in the product. So it's all aligned.

**Liz Kushnereit:** Our next step is prioritizing agents and confirming which ones we want to move forward with. That segues into our content strategy, which is agent-based clusters.

**Liz Kushnereit:** Building all of our content clusters at the agent level moves the content strategy from chasing keywords to creating content velocity through product. Guides and PSEO are our editorial, full-funnel content. PSEO gets more high intent at specific use cases. Everything's linked through internal linking, pre-configured workflows, deep links, and taxonomy to keep them all interdependent.

**Liz Kushnereit:** For Agents: we keep the existing taxonomy. For Connectors: we keep the existing structure but move the link to the connected integration instead of docs. For use cases (PSEO): we'd have "agents for [specific use case]"—could be tool comparisons, integration promotions, whatever. And a new Guides page: moving away from blogs, thinking about how guides drives traffic and relates to everything else.

**Liz Kushnereit:** Any questions so far about how they connect?

**Thiago da Costa (Datagrid):** Hi, can you hear me? Sorry I'm a couple minutes late. I'm following along—SEO pages, agent pages, connector pages. That's cool.

**Liz Kushnereit:** Yes, three lanes of expansion: guides and PSEO, agents and connectors, improving through content and UX. Each content cluster comes from a specific agent, then we build backwards into guides and forward into our use case guides.

**Liz Kushnereit:** For phase one: we prioritize the workforce agents.

**Liz Kushnereit:** This is the spine of our content strategy. We need to prioritize which agents we go after first and nail the page UX. I have a prototype to walk through. Once we lock agents, we jump to phase two: guides and PSEO. Phase three is the connectors marketplace. For reference, we did 600+ pages for Webflow integrations with high-intent setup content and strong traffic. We'll do something similar for connectors with better fleshed-out integration setup content, internal links to pre-configured workflows, guides, and agents.

**Thiago da Costa (Datagrid):** Okay, this is starting to make sense.

**Liz Kushnereit:** Here's the agent landing page prototype. You click on an agent like "deep search," you have chat, content about it, and a "Try this agent" CTA. These CTAs link to pre-configured workflows. Some content about the agent, key capabilities, a sidebar for use cases, related guides, common use cases (our programmatic SEO), and links to connectors.

**Liz Kushnereit:** For connectors, like Procore: we show integration-specific content. We've done 600+ pages for Webflow integrations—30 per week output. We want to flesh out more content about the integration's usefulness and link back to agents. And then the guides page, which is new, with CTAs taking users back into agents.

**Liz Kushnereit:** So that's our V1 strategy, infrastructure, and prototype UI/UX.

**Thiago da Costa (Datagrid):** What do you call a "guide"? Is that like a blog?

**Liz Kushnereit:** Guides are like a new page section for full-funnel SEO content based on agent-based clusters. Moving away from the existing blog. Open question about what we do with the old blog, but guides is the new SEO content engine.

**Marcel Santilli:** The key is navigational experience and cross-linking. Instead of deep hierarchical URLs (slash guide, slash category, slug, slash more), keep everything flat with tags. Dynamically surface pages everywhere. We're building the website as a knowledge graph for the brand—all the pages, all the questions people ask, content that influences both human buyers and AI agents training on your brand. We learned from Augment Code: adding new site sections opens opportunities. With Augment, we created a slash tools section with the same template, and it took off. It's a great way to open new opportunity areas.

**Thiago da Costa (Datagrid):** Got it. One thing I didn't see is an uplift on the design of the site overall. Not a complete change, but iterate and improve. You had criticism on the current design, so I'd love for you guys to take over some of that.

**Marcel Santilli:** Absolutely. Augment is a great example—it didn't look like this when we started. We can make a lot of improvements. They started dark mode everywhere, but we can keep a dark feeling in places while improving legibility and readability of content. We have examples. We've briefed the team and are pulling in design and dev to scope it out. My recommendation: create the surface area in the fastest way possible—get those sections created, content calibrated, things indexed. Then in parallel, we rebuild the website outside Webflow, which adds real speed. Once we agree on look and feel, we can spin up sites fast. It's not a rebrand—it's a facelift. With design engineers and coding agents, we can move much faster than dragging and dropping in Webflow. As long as you're cool with that, we'll start in parallel without blocking the immediate value delivery.

**Thiago da Costa (Datagrid):** How much work are you taking off our plate? You're basically taking over most of the website?

**Marcel Santilli:** We're proposing to take over and refresh the entire website outside Webflow, refactoring pages to best practices. You'll have a repo anyone can modify. But here's where we draw the line: we're not taking on product marketing work or homepage updates. We're porting everything to a better place and facelifting the content sections we own. That sets you up to hire dev and designers to spend weeks redesigning the homepage or adding animations—work we can't take on because it's a black box with endless iterations. But we unlock the future: any design is easier to implement, you can prototype in Cursor, and our components are super easy to use.

**Thiago da Costa (Datagrid):** One thing we want is to connect and embed our product into this experience. We'd like the actual Datagrid app embedded, same design system, same look, really the app.

**Marcel Santilli:** We use your API to programmatically create agents. Agents are context, instructions, datasets, and tools. It's like a package. When someone clicks "Try this agent," it creates the environment and uses your API to fork that agent into their workspace.

**Thiago da Costa (Datagrid):** Exactly. It's a kit: knowledge, attachments, instructions, agent configuration, planning instructions. Call the API, create the object, push all the data sets and knowledge so users get started fast. Like a safety agent for California with OSHA standards—PDF attached—ready to go.

**Marcel Santilli:** The guides section could hold all those files. A guide on OSHA compliance in California, in-depth, with files. Agents relate to and pull from those guides. We build a true knowledge graph that accelerates time-to-value for your users. It's not just traffic and AI visibility—it's time-to-value acceleration. Lovable templates do this: double-digit conversions and activations because it's what users wanted to build anyway.

**Marcel Santilli:** Liz and team worked incredibly hard on this—really thoughtful, in-depth. We care deeply. Liz is our best. We'll knock it out of the park for you all.

**Kaitlin Quimby:** Yeah, it looks great.

**Marcel Santilli:** Thanks, team. We'll follow up soon.
