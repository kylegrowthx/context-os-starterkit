# Datagrid <> GrowthX - Weekly Sync

---
meeting_id: 01KFKHA4R9T07ZDTP67VW5J8RK
date: 2026-01-26
duration: 37 minutes
organizer: team@growthxlabs.com
enriched_on: 2026-02-28 16:45 UTC
transcript_url: https://app.fireflies.ai/view/01KFKHA4R9T07ZDTP67VW5J8RK
participants:
  - name: Marcel Santilli
    company: GrowthX
    email: marcel@growthx.ai
    role: Founder/CEO
  - name: Vivek Shankar
    company: GrowthX
    email: vivek@growthxlabs.com
    role: Account Lead (leaving end of week)
  - name: Liz Kushnereit
    company: GrowthX
    email: liz@growthx.ai
    role: Account Lead (taking over from Vivek)
  - name: Kaitlin Quimby
    company: Datagrid (formerly Toric)
    email: kaitlin@toric.com
    role: Marketing/Product Marketing (post-acquisition)
  - name: Thiago da Costa
    company: Datagrid
    email: thiago@datagrid.com
    role: Technical Co-founder/Engineering Lead
---

## Summary

Strategic transition meeting where Liz Kushnereit takes over Datagrid account from departing Vivek Shankar. Teams aligned on shifting engagement from blog-only content to deeper product integration via agent and connector pages. Marcel committed to delivering a priorities roadmap by end of week and scheduling a one-hour technical strategy session with Thiago to define API-driven agent-forking workflows and cross-linking strategy.

## Context

Datagrid, formerly Toric, was recently acquired by Procore, creating a critical window for cross-linking strategy and content consolidation with Procore's properties. Datagrid is still operationally independent (Kaitlin noted "day five") and actively hiring marketing and product marketing talent. Internally, GrowthX is experiencing transition: Vivek Shankar leaves at week-end and Liz Kushnereit assumes leadership. Datagrid's CEO Hugh has directed a shift toward product content and integration, signaling both resource investment and strategic clarity around the post-acquisition identity.

## Relevance to GrowthX

**Expansion of Core Capability**
This engagement validates the programmatic product integration playbook GrowthX has proven with Lovable (template libraries) and Ramp (vendor hubs). Datagrid's agent marketplace is a direct parallel to the "store of use cases" model.

**Technical Advantage**
Datagrid's APIs are fully public and support the required operations: agent listing, creation, knowledge base copying, and streaming responses for live demos. This eliminates custom integration work that slowed Lovable adoption.

**Revenue Opportunity**
A successful agents marketplace could unlock a new engagement tier: from blog-driven content ($15–20k/month) to product integration services ($30–50k+/month). This positions GrowthX to compete on outcome (revenue/traffic) rather than hours.

**Market Timing**
Procore-adjacent revenue (40% of Datagrid's base) is a defensible, lower-churn segment. Capturing this cohort in Q1–Q2 2026 before Autodesk competition intensifies is critical.

## Overview

**Primary Objective:** Transform Datagrid's website from isolated content silos (blogs, agents, connectors) into an integrated product-driven experience that converts search traffic into product signups and agent forks.

**Three Content Surface Areas:**
1. **Blog/Articles:** Strong traffic and momentum; lacks links back to product agents or connectors.
2. **Agents Marketplace:** Launched ~8 days ago; 50+ agents with minimal content, no videos, poor SEO, no clear fork/signup path.
3. **Connectors Pages:** Outdated (still reference "Toric" branding), missing documentation, poor user experience.

**Strategic Constraints:**
- Datagrid still independent from Procore on day 5 post-acquisition; messaging alignment TBD.
- Marketing team understaffed; hiring underway but not yet in place.
- Wonderup (external agency) handles some website work but context switching and bandwidth constraints slow progress.

**GrowthX Scope:** Own end-to-end strategy and execution for agents and connectors, treating these as owned surfaces with SEO and conversion optimization built in (vs. product marketing support role).

## Key Topics

### 1. Current State Problems

The website has three disconnected surface areas:
- **Blog/articles:** Strong momentum, good traffic, but no links back to product
- **Agents section:** Brand new (launched ~8 days ago), minimal content, no videos, poor SEO
- **Connectors pages:** Outdated (some still say "Toric"), lacks documentation

No cross-linking between content and product. No clear path from blog readers to product sign-ups.

### 2. The Opportunity

Replicate the Lovable model: use Datagrid's API to programmatically create agent templates that users can "fork" into their own workspaces. The API supports:
- Listing and creating agents
- Copying knowledge bases to new workspaces
- Streaming chat responses for live demos on the site

The vision: website as a "store of use cases" with pre-configured agents (e.g., OSHA compliance for California) that include manuals, knowledge bases, and system instructions.

### 3. Market Focus

- **Built world:** Construction, manufacturing, insurance—not just Procore's project-based construction
- **Procore overlap priority:** ~40% of Datagrid revenue comes from non-Procore customers, but focusing on Procore-adjacent segments reduces churn and maximizes ROI
- **Autodesk customers:** Expect churn—Autodesk is now a competitor

### 4. Website Ownership

Currently fragmented:
- External team (Wonderup) handles some website work
- Updates are slow due to bandwidth constraints
- No dedicated product marketing to coordinate between product and marketing teams

GrowthX can own end-to-end: strategy, execution, and integration—but needs clear handoffs for product marketing scope.

## Action Items

### Kaitlin Quimby (Datagrid)
- Confirm with Thiago whether Smartlead software is still in use or can be turned off
- Coordinate with Datagrid marketing and product marketing teams to clarify messaging alignment post-acquisition
- Deliver product videos for each agent card to improve agents marketplace presentation

### Liz Kushnereit (GrowthX)
- Assume full account ownership from Vivek Shankar (departing end of week)
- Connect with Marcel to align on account priorities and next steps

### Marcel Santilli (GrowthX)
- Deliver high-level priorities document to Thiago by end of this week
- Coordinate with Liz and forward deploy engineer (Nico) to finalize site access and begin agents/connectors audit
- Schedule and facilitate one-hour strategic session with Thiago next week to review roadmap and resource allocation

### Thiago da Costa (Datagrid)
- Support GrowthX with programmatic agent creation and "fork" workflows via API
- Clarify API capabilities: agent listing, knowledge base copying, streaming chat responses
- Collaborate on cross-linking strategy between blog content and agents/connectors marketplace

---

## Full Transcript

**Kaitlin Quimby:** This meeting is being recorded.

**Vivek Shankar:** Hey, Kaitlin.

**Kaitlin Quimby:** Hi.

**Vivek Shankar:** How are you?

**Kaitlin Quimby:** I'm good. How are you?

**Vivek Shankar:** Good, good. I think we're gonna have a pretty full call today.

**Kaitlin Quimby:** Yeah, Sorry, there's someone. The maintenance guy was at my door. My dog was freaking out. No worries.

**Vivek Shankar:** We noticed a software called Smartlead in Thiago's name that's being billed to us. It's likely a remnant from the old Outbound days. Are you still using it, or can we turn it off?

**Kaitlin Quimby:** I don't think we're using it anymore. Let me confirm with Thiago to be sure.

**Vivek Shankar:** Before Thiago and Marcel join, I want to quickly introduce Liz. As mentioned, I'm leaving GrowthX at the end of this week, and Liz will be taking over the Datagrid account.

**Liz Kushnereit:** Hi, Kaitlin. Nice to meet you. I'm excited to take over. I've been researching the account background and I'm genuinely excited for this conversation. Looking forward to working together.

**Kaitlin Quimby:** Yeah. Nice meeting you as well.

**Kaitlin Quimby:** Thank you. It's been a busy few weeks.

**Liz Kushnereit:** I've been in the background, but I know one reason we moved this meeting was to talk about path forward. Are you taking the lead on that, or are we waiting for Thiago?

**Kaitlin Quimby:** Thiago wants to be part of this. He's on another call but should be here in a couple of minutes. Things have changed on our end too—with the transition from Vivek to Liz, it feels like a good time to reset. I don't think we've actually met before.

**Marcel Santilli:** From my conversations with Thiago, the main thing is looking at work we've done for Lovable and others where we tightly integrate product with programmatic content creation. The goal is to evolve beyond just pumping blogs into a more integrated strategy. I want to understand your priorities better. I've heard there's more resources and aggressive targets for this year. I need to understand how the team is thinking about hitting those goals and what's already worked. Then we can rework the plan and move fast. A few questions: Is there any Procore integration strategy? Are there other considerations? Is it still okay to cover Autodesk topics?

**Kaitlin Quimby:** That's not totally clear on our end either. I'm just starting to meet with marketing and product marketing leadership. We have more resources in the pipeline, but we don't have them yet. We're still operating independently from Procore—we're only five days in post-acquisition. We're still figuring out what we're allowed to say about Autodesk and to what extent. We're open to exploring other things, but alignment is still happening. We're hiring several marketing roles to fill gaps. Hugh wants to see more product on the website. Getting a dedicated product marketing person who can work with you instead of us having to ping Miles on product updates will help smooth things. But that team isn't in place yet.

**Marcel Santilli:** As we wait for Thiago, a quick context question: If you had a magic wand for top-of-funnel and traffic growth, where do you want to focus? When we started, we did a lot of work beyond just construction. So is the goal now to narrow to construction specifically, or continue broader than what Procore serves?

**Kaitlin Quimby:** We need to hit our numbers within the built world, but it's not just construction—manufacturing, insurance, and other sectors count too. We're focusing on the built world broadly. I just got off a call with Diana about phase two messaging for the site. It uses broad terms so it doesn't feel industry-specific, but the examples stay in the built world. We're avoiding language that makes people think "this doesn't apply to me." What we've found is that smaller GCs like that the tool works across the whole company, not just for on-site teams. Other team members can use it for different functions. That's our sweet spot.

**Kaitlin Quimby:** Can you walk me through what you did for Lovable? I don't have that context.

**Marcel Santilli:** For Lovable, we built their entire templates library programmatically using their API. We created template pages with the design team in the loop, plus guides similar to your article approach. The results are strong—we're averaging 400–500 clicks a day. We also did their vendor catalog and various hubs. We did similar work for Ramp's vendor hub.

**Kaitlin Quimby:** Our connectors pages are a good example of what needs work. A lot of them still say "Toric" instead of "Datagrid." Clicking into the cards, they need an audit and revamp.

**Marcel Santilli:** Who's managing the website end-to-end right now? Who's in charge of it, or is it more reactive—whatever gets touched last?

**Kaitlin Quimby:** Wonderup helps with the website, but things move slowly because they need input from me or Miles (product). We've had a lot going on the last few months, so updates are sparse or waiting for our input. I've been trying to put together a webinars and events page for three weeks but haven't had the bandwidth.

**Kaitlin Quimby:** The agents marketplace is our newest addition. I'm trying to get product videos for each agent—most don't have them yet, only the deep dive one does. That's a priority.

**Marcel Santilli:** The agents page isn't strong from a search and visibility perspective. But the surface area is there and we can improve and scale it. There's pretty much no traffic to it currently, whereas your blog has strong upward momentum.

**Kaitlin Quimby:** The agents marketplace launched about eight days ago—right before the acquisition announcement. It's new. We're working on getting videos for each agent. Most don't have them yet. The challenge is figuring out how to surface product information effectively and make it searchable and successful.

**Marcel Santilli:** Thiago, you there? I think you're on mute.

**Thiago da Costa:** Can you guys hear me?

**Marcel Santilli:** We can help in multiple ways, but where we do best is owning end-to-end sections of the site. We handle strategy, AI visibility, organic growth, and day-to-day execution. We're less focused on broad product marketing like homepage repositioning. I showed Kaitlin some of what we did for Lovable—their entire templates library. We researched what templates people search for, looked at competitors like Wix and Webflow, and designed and executed the strategy. We're seeing 3,000–4,000 clicks per week on guides and templates combined with strong upward momentum. For Datagrid, we've done a lot of guide content already and need to keep cross-linking and creating topical hubs. But what's most critical from your perspective? You launched an agents section—what would make the biggest impact for your numbers this year, just focusing on search visibility and discovery?

**Thiago da Costa:** Two parts. First, product content and communication on the website. Our blog articles aren't linked back to the agents. We'll talk about RFI in a blog but never connect it to "Here's the RFI agent with a demo video." That's a huge miss on high-traffic pages. Second, the agent marketplace needs heavy development—it's where people have the most questions and interest. The connectors marketplace also needs work; some pages still say "Toric" instead of "Datagrid," and there's missing documentation on how to install connectors. We need to keep building content, but align it with Procore-adjacent topics and broader built-world content—like data centers, how they're built, who builds them (hyperscalers). That audience overlap creates more funnel and visibility. So it's really about integrating product with content and evolving both for this new phase of the company.

**Marcel Santilli:** Still mostly the broader built world, not just what Procore serves, right? Procore is project-based construction. They don't serve manufacturing as an end-to-end platform.

**Thiago da Costa:** Right, we do serve manufacturing. We'll continue to, but strategically. We're not writing about Ford Motors. But why not write about suppliers of piping and fittings? Or electrical equipment manufacturers? Or HVAC and mechanical engineering systems that go into buildings?

**Marcel Santilli:** What percentage of your revenue comes from customers who'd never buy from Procore?

**Thiago da Costa:** About 40%.

**Marcel Santilli:** That's significant. My point is there's huge opportunity with Procore-adjacent customers now that you have their awareness. It almost seems wasteful to dilute effort elsewhere. For the next two quarters, let's capture that awareness everywhere and focus on overlaps with potential Procore customers.

**Thiago da Costa:** That's the right strategy. A smaller non-Procore base is actually more protective. Customers in the Procore ecosystem have lower churn. Autodesk customers, I expect those to churn next year—they're now a competitor.

**Marcel Santilli:** Let me recap what I'm hearing: You've built a lot of blog content. Now you need to connect it to the product. You have two main surface areas besides blogs—agents (brand new, little content, no product integration) and connectors (also needs work). The key is connecting everything in a use-case driven way. Blog → agents → connectors, with each linking meaningfully. Agents as templates you can fork into your workspace, not just standalone docs. Does that capture it?

**Thiago da Costa:** On the Procore overlap—we can also reach out and say "Your top-ranking blog page should link back to Datagrid." Procore's open to suggestions. We can tell them what to do and they'll listen.

**Marcel Santilli:** Here's a key question: If someone comes to your site and types "agent for RFI or RFC for construction project," what happens?

**Thiago da Costa:** Right now it just takes the prompt after login. It doesn't create a specialized agent for that task. We wanted a UI that automatically creates a task-specific agent with connectors and question templates, but we don't have that yet. The idea is speed—someone types the prompt and gets a working agent in seconds, not a blank canvas.

**Marcel Santilli:** Here's what we could do as an intermediate step. You already have agents built in a workspace. We can programmatically create templates that users fork rather than build from scratch. For example, we did this for Lovable—you click "Use Template," it says "Include Project History or Not," you click "Remix," and it forks the entire project into your account. That's much easier than a blank canvas. If Datagrid's API supports programmatic agent creation, we can build workflows to create these pre-configured agents on your website and let users fork them in.

**Thiago da Costa:** Check developers.datagrid.com—there are APIs to create custom agents. The create-agent API is documented, and there are knowledge and data APIs.

**Marcel Santilli:** Good. With Lovable, their API isn't even public—they only gave us access. Is yours public?

**Thiago da Costa:** Yes, it's public. Lots of people use it.

**Marcel Santilli:** Okay. If you create an agent in a workspace, can you make it public so others can programmatically fork it? Or is each fork a separate create call with no public concept?

**Thiago da Costa:** You use the list-agents API. It returns all agents in the team space with full configuration—system instructions, tools, knowledge corpus—everything. You can display them however you want.

**Marcel Santilli:** That's private workspace data, right? Not public?

**Thiago da Costa:** You generate an API key in Settings > API. That key lists all your team's agents. You create them in Datagrid, list them via API. It works.

**Marcel Santilli:** So on a public page, if a new user wants to fork that agent, they'd log in and create it?

**Thiago da Costa:** Yes. Use the create API with the same settings. List all the properties and replicate them.

**Marcel Santilli:** That's not a true fork like what we did with Lovable—where we grabbed everything (files, history, settings) and forked it entirely. What you're describing is an API call that copies settings as JSON. Like we did with VAPI voice agents—just a JSON payload that gets ingested and rendered.

**Thiago da Costa:** Right. We could build a fork workflow that copies the agent and knowledge to another workspace. You don't want the project history, just the knowledge—SOPs, manuals, recipes, connectors. The knowledge API handles that.

**Marcel Santilli:** Can you copy knowledge from one workspace to another? If an agent has access to sample knowledge, can you replicate that on a new account?

**Thiago da Costa:** We can build a create-knowledge API that takes a destination workspace and pushes the knowledge there.

**Marcel Santilli:** Okay. Technically it's all possible. We just need to do it without a three-month product roadmap.

**Thiago da Costa:** We can augment APIs quickly if needed. The vision I like is making the website a store of use cases. For example, "OSHA compliance for California"—the manual is there, the agent is there, everything is ready to go.

**Marcel Santilli:** Exactly. It's like what we did with VAPI—a widget with pre-configured settings for a voice agent. It's really just the JSON payload.

**Thiago da Costa:** Exactly. Download the JSON, post the create call. Straightforward. Can be on your server or ours.

**Marcel Santilli:** Okay, I'm crystal clear on what we need to do. Liz and I will connect offline, bring Nico or another forward deploy engineer, and then plan the integration. The key is: you're already winning with blogs. We embed use cases more deeply, cross-link to agents, make agent pages template-like, strengthen the path to product signup, and improve connectors. Over six months, that's significant upside. The power move is: user searches, finds an article, clicks an agent template, goes straight into the product. Long session, no bounce. They see value immediately. One last thing before I run—do you have streaming for chat responses in the API?

**Thiago da Costa:** Yeah, we have full streaming support. Lots of partners are building on the API already.

**Marcel Santilli:** Perfect. This'll be a fun project. By end of week, we'll send a high-level priorities doc. We'll also align on resource allocation so you feel good. Then we'll grab an hour next week for a detailed strategic review.

**Thiago da Costa:** Sounds good. Let's do it.

**Marcel Santilli:** Thanks, Thiago.

**Thiago da Costa:** Thank you. Talk soon.
