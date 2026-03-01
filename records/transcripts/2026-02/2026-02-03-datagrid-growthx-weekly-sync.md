# Datagrid <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-03
time: 17:30 UTC
duration: 29 minutes
organizer: team@growthxlabs.com
participants:
  - name: Kaitlin Quimby
    role: Client contact (Datagrid/Procore)
    affiliation: Datagrid
  - name: Liz Kushnereit
    role: Content strategist
    affiliation: GrowthX
  - name: Thiago da Costa
    role: Engineering lead
    affiliation: Datagrid
  - name: Marcel Santilli
    role: CEO
    affiliation: GrowthX
source: fireflies
fireflies_id: 01KG0AWB9DZMSX0NNKVFCEJAZ5
transcript_url: https://app.fireflies.ai/view/01KG0AWB9DZMSX0NNKVFCEJAZ5
enriched_on: 2026-02-28 20:00 UTC
</metadata>

---

## Summary

GrowthX presented a major content strategy pivot for Datagrid (Procore) — moving from blog-led awareness to product-led discovery built around three lanes: agents as the discovery layer, connectors as a marketplace hub, and guides plus programmatic SEO as traffic engines. The team also aligned on a website redesign that will move the site out of Webflow.

---

## Context

Datagrid is a GrowthX client where Liz Kushnereit leads content strategy alongside client contacts Kaitlin Quimby and Thiago da Costa. This session presented the v1 of a new content strategy that fundamentally restructures how the website drives discovery and activation. The strategy treats the website as a knowledge graph, with agent-based content clusters replacing keyword-chasing blog content. Marcel joined late and added context on the website redesign approach, drawing on lessons from other GrowthX clients like Augment.

---

## Relevance

**To GrowthX Delivery:**
- Live example of GrowthX's evolving content strategy methodology
- Product-led content approach replacing traditional blog-led awareness
- Website redesign scope: migrate entire site out of Webflow, facelift (not rebrand)
- Lessons from Augment applied to Datagrid engagement

**To CheckThat:**
- Knowledge graph concept aligns with CheckThat's AI visibility framework
- Cross-linking and flat page structures optimized for both human buyers and AI agents

**To GrowthX Business Development:**
- Client engagement expanding from content to website infrastructure
- API integration and product embedding creating deeper client relationship
- Reference case: Webflow integration content engine producing 30 pages/week

---

## Overview

- Strategy pivot from blog-led awareness to product-led discovery across three lanes
- Agents become the canonical discovery layer with agent-based content clusters
- Connectors serve as a marketplace hub for enablement (modeled on Webflow success)
- Guides replace blogs as full-funnel SEO content linked to agents
- Programmatic SEO targets specific use cases at the agent level
- Website redesign moving from Webflow to code-based site for speed and maintainability
- API integration to embed Datagrid product experience directly on the website
- Knowledge graph approach: flat URL structure, strong cross-linking, dynamic page surfacing

---

## Key Topics

### Content Strategy Pivot
- Three lanes: agents (discovery), connectors (marketplace/enablement), guides + PSEO (traffic)
- Agent-based content clusters replace keyword-chasing strategy
- Content velocity driven by product rather than keyword research
- Full-funnel coverage: guides for informational, PSEO for high-intent, agents/connectors for product activation
- Internal linking, pre-configured workflows, deep links, and taxonomy keep everything interdependent

### Prototype & UX
- Landing page prototype for agents with deep search, chat, pre-configured workflows behind login wall
- Sidebar navigation for use-case-driven user journeys
- Connectors pages modeled on Webflow integration success (600 pages, 30/week output)
- Guides page replaces blog with new full-funnel SEO content
- Headless CMS consideration for better scalability

### Website Redesign
- Full site migration out of Webflow for speed and maintainability
- Design facelift, not rebrand — improving legibility and readability
- Augment cited as reference for design approach
- Once complete, any dev or designer can implement changes via the repo
- GrowthX scope: port and facelift content sections; not taking on product marketing or homepage redesigns

### API & Product Embedding
- Datagrid product as a "kit": knowledge, attachments, instructions, configuration
- API calls to programmatically create agents and push associated datasets
- Example: safety agent for California with OSHA standards pre-loaded
- Guides can hold compliance documents that agents pull from
- Goal: accelerate time to value, similar to Lovable's double-digit conversion rates from templates

---

## Decisions & Commitments

**Strategy greenlit:** Three-lane content and product strategy approved (agents as discovery layer, connectors as marketplace hub, guides + PSEO as traffic engines).

**Website redesign approved:** Full migration from Webflow to code-based site; design facelift (not rebrand) focused on legibility and readability. GrowthX scope: content sections and design improvements. Not including product marketing or homepage redesign.

**Phased rollout confirmed:**
- Phase 1: Agents landing page optimization and content cluster prioritization
- Phase 2: Guides page and PSEO implementation
- Phase 3: Connectors marketplace expansion

**Product-website alignment:** Content updates on the website must sync with Datagrid product team. Kaitlin owns communication between teams; source of truth is Notion page.

**API integration approach:** Use Datagrid API to programmatically create agents with knowledge, attachments, instructions, and configuration. Agents can be "forked" on the website as pre-configured kits (e.g., safety agent for California with OSHA standards pre-loaded).

**Parallel workstreams:** Content team to begin agents prioritization while GrowthX design/dev scope website redesign. Non-blocking approach allows immediate value delivery.

---

## Open Questions

- What happens to the existing blog page? Maintain, optimize, and refresh, or sunset?
- How extensively should the connectors marketplace be fleshed out? Reference is Webflow (30 pages/week output), but may not be needed at the same volume for Datagrid.
- Headless CMS decision: Is Datagrid adopting a headless CMS for better scalability, or sticking with code-based approach?
- What level of custom design work is in scope for the homepage and product marketing pages post-redesign?
- Timeline: When is the website redesign and Webflow migration expected to complete?

---

## Action Items

**Liz Kushnereit (GrowthX)**
- Present detailed content and UX strategy to Kaitlin for full knowledge transfer
- Prioritize agents for content cluster development as phase one
- Develop prototype enhancements for agents landing page UX
- Continue fleshing out connectors marketplace content based on Webflow success
- Conceptualize and prepare guides page as new full-funnel SEO engine

**Kaitlin Quimby (Datagrid)**
- Ensure product and website agent content alignment
- Communicate content updates to product team as needed
- Own source of truth (Notion page) for agent library syncing between website and product

**Marcel Santilli (GrowthX)**
- Lead website redesign and migration planning away from Webflow
- Scope rapid facelift for legibility and readability improvements (reference: Augment site redesign)
- Coordinate design and dev team for parallel implementation
- Provide ongoing support for API and agent creation integration

**Thiago da Costa (Datagrid)**
- Coordinate embedding of Datagrid product experience in new website structure
- Collaborate on API-driven agents content and knowledge graph implementation
- Support agents kit creation (knowledge, attachments, instructions, configuration)

---

## Transcript

**Kaitlin Quimby:** This meeting is being recorded.

**Kaitlin Quimby:** I think originally the plan was for Marcel and Thiago to join, but that has changed. I think they talked separately. Maybe Marcel's still joining.

**Liz Kushnereit:** I think I gave Marcel a lot of context on Friday and then he had a conversation with Thiago over the weekend. We're kind of greenlit, but there's still a lot of information. Maybe I could still present it all to you because it's quite a lot.

**Kaitlin Quimby:** Yeah, yes. Because I got like 30 second brief from Marcel and he's like, "this is what we're doing." I'm like, okay. He's like, but actually you need to find out more info. I would like to get a little more caught up.

**Liz Kushnereit:** Okay, so the TLDR is that it's a big pivot from blog-led awareness to product-led discovery surface and activation layer. Basically agents becomes our canonical discovery layer, connectors becomes our marketplace-style hub for enablement, and then guides and PSEO become our main traffic engines and also overlap into enablement especially for agents in our use case guides.

**Liz Kushnereit:** This is basically three lanes of expansion. Guides and PSEO is editorial content. We'll be taking over this page and optimizing for UX and content. Connectors is basically the same story—optimizing UX and content. I'll have a lot of references especially on connectors.

**Kaitlin Quimby:** One thing on the agents: we want to make sure that whatever we're doing there—updating or changing—we want to reflect it on the product side too. So the agent library on the product matches the website. We can have more info on the website, but just FYI.

**Liz Kushnereit:** Yeah, we'll need to coordinate on that.

**Kaitlin Quimby:** Right now we have a Notion page as our source of truth. If we're updating it there, I'll let the product team know so they can update in the product. It's just all aligned.

**Liz Kushnereit:** Our next step is the prioritization of agents and confirming which ones we want to move forward with. This is where the content strategy comes in—we're building all of our content clusters at the agent level. There's a lot of opportunity there, and it moves the content strategy from chasing keywords to creating content velocity through product.

So our editorial content includes agent-based cluster pages: guides and PSEO. Guides is full-funnel, especially informational content at the top. PSEO gets a bit more into high intent. We're still capturing organic search into agents and connectors pages, which will be much higher intent.

These are all linked through internal linking, pre-configured workflows, deep links, and taxonomy. That's how we keep them all interdependent. Agents keep the existing taxonomy. Connectors keep the existing structure. PSEO moves to `/agents/{agent-name}/{use-case}`.

Programmatic SEO is a different approach than you discussed before. It could look like tool comparisons, promoting specific integrations—a lot of flexibility. But it still links out to guides and workflows to keep users moving through the system.

An entirely new page we need to stand up is guides—moving away from blogs and thinking about how guides relates to everything and drives traffic.

Any questions so far about how they connect?

**Kaitlin Quimby:** Cool.

**Thiago da Costa:** Hi, can you hear me? Sorry I've been a couple minutes late. I'm just pulling up here and seeing what you have. SEO pages, agent pages, connector pages. Yeah, that's cool.

**Liz Kushnereit:** Yeah, you just joined. So it's three lanes of expansion: guides and PSEO, agents, and connectors—improving through content and UX, especially on agents and connectors. That's what the interdependency looks like. The content strategy is agent-based, so each content cluster comes from a specific agent. We build backwards into guides and forwards into use case guides. Guides is our new page that we'll stand up.

For what this looks like in terms of building it out: Phase One is agents. Since agents are the spine or backbone of the entire content strategy, we need to think through prioritization and what the page looks like from a user perspective. I have a prototype we can walk through. There's still some more work we can do in terms of UX, but that would be our primary focus to ensure we're prioritizing the correct agents.

Phase Two is guides and PSEO. Guides pages would be new. This is our full-funnel informational content—higher volume keywords that still relate to the agent. Programmatic SEO moves more into those use cases at the agent level.

Finally, our Connectors marketplace. This needs a bit more fleshing out—it's the final enablement phase: set up your integration and actually start using it. I tagged Webflow here because we did a really good job on Webflow integrations. Different business model, but we've seen a lot of traffic to these pages. We've done about 600 pages for them. We're looking to do the same for connectors—flesh out "how to set up your integration" content that still captures that high intent traffic. Internal links move into pre-configured workflows to drive to either guides or agents.

**Thiago da Costa:** No, this is exciting. Yeah, great.

**Liz Kushnereit:** Okay, so this is what we put together for agents. You'll forgive me because I do think we can build better UX if we go with a headless CMS, but this is the landing page for agents. You click on your deep search agent, you have your chat, some content about it, and you can try the agent. Pre-configured workflows lead directly into trying it. These take you to the login wall. Key capabilities are detailed there.

I'm hoping we can get some kind of sidebar navigation that takes the user directly into their use case. Related guides are down here as well. Common use cases would be our programmatic SEO—I'd probably bump this up when we actually launch this. We also have our link into connectors.

For the connectors page, we take a look at Procore. Our Webflow integration content serves as a reference. We've already developed the content engine—we do about 30 pages per week output. We'll flesh out the content and optimize it with guides and more informational content about the usefulness of the integration, or work into use case guides. Pre-configured workflows lead you back into the agent. Some linking to agents and setup requirements. This would be expanded into actual content linking to related guides.

The guides page is our new page. We have CTAs taking us into the agents. We can explore what we want this to look like because it's moving into product enablement. So this is our v1 of the strategy, the infra, and what the prototype UI/UX would look like.

**Thiago da Costa:** Okay, cool.

**Marcel Santilli:** Hey Thiago. Sorry I'm a few minutes late.

**Thiago da Costa:** This is great. What do you call a guide? There's a part in there I say it goes into a guide. What is a guide in that case?

**Liz Kushnereit:** So I would think of guides as basically like a blog, but this would be a new page for full-funnel content that moves away from the existing blog page. There's definitely an open question about what we do with the existing blog page. Do we maintain, optimize, refresh, and keep that going? But guides is basically just SEO content that we'd be pushing out based on our agent-based content clusters.

**Thiago da Costa:** Okay. Yeah, yeah, yeah.

**Marcel Santilli:** Thiago, I think the most important thing is the navigational experience and how strongly we cross-link things. That's far more important. We also want to keep a lot of pages relatively flat. Instead of having `/guides/{category}/{slug}`, you keep everything flat and then everything is just like a tag. You dynamically surface pages in a bunch of places. So we're trying to create a knowledge graph for brands. We need to fill in the gaps of all the pages, all the questions people have, all the things you want to influence both human buyers and AI agents. Training data on your brand is the mental model there.

Some lessons we learned from Augment and others: creating additional sections of the site opens up opportunities, especially once you go really heavy on one section with hundreds and hundreds of pages. For instance, with Augment we did a `/tools` section with the exact same template, and it really took off. It's a great way to think about it—opening up additional places of opportunity.

**Thiago da Costa:** Got it. Makes sense.

**Marcel Santilli:** The other thing is the design uplift overall.

**Thiago da Costa:** Yeah, I think the only thing I didn't see is an uplift on the design of the site overall. Not a complete change, but an iteration and improvement. You had some criticism on the design, so I assume you had an opinion. Would love for you guys to take over some of that.

**Marcel Santilli:** Yeah, for sure. With Augment, this is not how it looked when we first started. There are a lot of improvements we can make on individual pages. Augment is a great example—they started with dark mode everywhere. But overall, there are ways to keep a dark feeling in places while improving legibility and readability of the core content. We have examples of that. That's what we talked about. I gave the team a heads up and we're pulling in our design and dev to quickly scope it out.

The main lift is creating the surface area in the fastest way possible to start getting those sections created and content calibrated, so things start to get indexed. In parallel, we take over and redo the website outside of Webflow—that will really add speed. Once we agree on look and feel and design, we can spin up sites really fast. It's not a rebrand, it's a facelift—an overall improvement to the experience. We can move really fast with coding agents and design engineers in the loop instead of dragging and dropping in Webflow.

So as long as you're cool with that in parallel, we'll start that work. We don't want to block on defining that work—we just want to add a tiny bit of scope and start delivering value immediately.

**Thiago da Costa:** Awesome. Okay, so just summarize: how much work are you taking off Webflow? You're basically taking over most of the website, right?

**Marcel Santilli:** We're proposing to take over and refresh the entire website out of Webflow. Refactoring the entire website out of Webflow and redesigning the pages to be best practices. At that point you have a repo that anyone else can make changes to. But we're drawing the line so we're not taking on product marketing work or updates to the homepage after that. We're porting everything to a better place and facelifting the sections of content that we own. That sets you up for any dev and designers to spend time redesigning the homepage or creating animations for product pages—that's work we can't take on because it's a black box with millions of iterations. But at least we'll unlock you so in the future any design can be implemented way easier. You can prototype directly in Cursor or whatever you're using, and it makes it super easy to use our components however you want.

**Thiago da Costa:** Great. Awesome. It makes a ton of sense. One of the things we're going to want to do is connect our product to this experience and embed our product to some degree. We'd like it to be the Datagrid app that gets embedded—always the same design system, always the same look, integrating the page with the actual app.

**Marcel Santilli:** We're using our API to programmatically create agents. Agents are knowledge, instructions, potentially data sets and tools. So if someone is in an experience and clicks on something, it will create the environment and use the API to add that agent to their environment—essentially fork that agent.

**Thiago da Costa:** It's like a kit, right? You have knowledge, attachments, instructions, the configuration of the agent—what's on, what's off, planning instructions. You call the API to create that object and push all the associated data sets and knowledge so the user can get started with something. One example would be a safety agent for California with OSHA safety standards—a document with OSHA safety standards already attached as a PDF. Things like this kick it off quickly.

**Marcel Santilli:** Liz, what we can do is the guides section can hold a lot of the files. For instance, a guide to OSHA compliance in California—an in-depth guide with files that agents can pull from. That way we're approaching it truly like a knowledge graph that will also accelerate time to value for your users. It's not only a way to capture traffic and AI visibility, but also accelerate time to value. That's what we're seeing with Lovable templates—they have double-digit conversions and activations because it's what users were thinking of building anyway.

Awesome Liz. Amazing work. Liz and team worked really hard. I know we didn't cover everything, but it was really thoughtful and in-depth. Liz is our best, so whatever we need to do to knock it out of the park for you all, we're here.

**Kaitlin Quimby:** Yeah, it looks great.

**Marcel Santilli:** Awesome. Thanks team. We'll follow up soon.

**Kaitlin Quimby:** Thanks a lot. Bye all.

**Thiago da Costa:** Thank you.
