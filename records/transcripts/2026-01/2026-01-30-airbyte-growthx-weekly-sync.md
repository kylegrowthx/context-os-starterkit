# Airbyte <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-30
time: 16:30 UTC
duration: 16 minutes
organizer: team@growthxlabs.com
enriched_on: 2026-02-28 14:15 UTC
fathom_recording_id: 118558062
fathom_url: https://fathom.video/calls/549738770
share_url: https://fathom.video/share/nAxBEcJAh-VDJ86Ex9fqBZXimdPAaRVD
source: fathom
participants:
  - name: Erik O'Brien
    email: erik@growthx.ai
    organization: GrowthX
    role: Content Strategist
  - name: Tanmay Sarkar
    email: tanmay@airbyte.io
    organization: Airbyte
    role: Engineering
  - name: Nithin M
    email: nithin.mahalingam@airbyte.io
    organization: Airbyte
    role: Engineering
  - name: Mario Moscatiello
    email: mario.moscatiello@airbyte.io
    organization: Airbyte
    role: Engineering
  - name: Kushal Chatterjee
    email: kushal.chatterjee@airbyte.io
    organization: Airbyte
    role: Content
  - name: Kyle Gaudreau
    email: kyle@growthx.ai
    organization: GrowthX
    role: Operations
</metadata>

---

## Summary

GrowthX and Airbyte aligned on completing the Data Engineering Resource (DER) article series, progressing with agentic article development, and designing new agent use case pages with a focus on technical depth and SEO performance. The team discussed performance metrics showing strong audience acquisition through agentic content, with ongoing optimization for underperforming clusters, and confirmed the soft launch timeline for CheckThat tool as a unified platform for competitive intelligence and prompt tracking.

---

## Context

This is a recurring tactical sync between GrowthX's content team (Erik O'Brien leading) and Airbyte's product marketing/engineering leadership (Tanmay, Nithin, Mario, Kushal) to coordinate on the joint content strategy for Airbyte's data integration and agentic capabilities positioning. The engagement has evolved from thought leadership and data engineering education into a broader SEO and audience acquisition play through agentic content and templated use case pages. Airbyte is investing in technical, content-rich SEO assets to compete in the emerging AI agent infrastructure space, while GrowthX provides strategic content direction, execution oversight, and performance analytics. CheckThat, a GrowthX-developed competitive intelligence tool, is being productized as a potential industry solution for prompt and competitor tracking.

---

## Relevance

**For Airbyte:**
- Content pipeline completion removes a blocker and enables rapid scaling to 12+ agentic articles with strong audience acquisition signals (1.25x new visitors).
- Agent use case pages represent a new distribution channel for SEO traffic, with Tanmay's long-form article experiment testing alternative content formats.
- CheckThat soft launch provides unified competitive and prompt tracking, replacing fragmented tools (Scrunch, Profound).

**For GrowthX:**
- Validates agentic content as a high-performing SEO category with >1,300 sessions/month and identifies underperforming clusters ("Enterprise Agents") for optimization.
- Demonstrates product-market fit for CheckThat beyond GrowthX's client use cases, signaling a potential standalone business opportunity.
- Establishes repeatable content-to-SEO workflow (DER → Thought Leadership → Use Cases) applicable to other client engagements.

**Cross-cutting:**
- Competitive intelligence and market positioning (Context Engineering dominance vs. Enterprise Agents underperformance) inform both content strategy and product roadmap decisions.
- Real-time performance dashboards (monthly engagement per article) enable data-driven iteration rather than batch-based reviews.

---

## Overview

- **Content Pipeline:** The final batch of Data Engineering Resource (DER) articles is published. The focus now shifts to the remaining 12 agentic articles and two thought leadership pieces.
- **Agent Use Case Pages:** A wireframe is ready, but the team will research competitors (Composio, Merge) to develop a content-heavy, technical template that avoids an "AI-generated" feel.
- **Performance:** Agentic articles are driving new audience acquisition (\>1,300 sessions/mo, 1.25x sessions:visitor ratio). The "Context Engineering" cluster dominates, while "Enterprise Agents" underperforms and requires optimization.
- **Tooling:** CheckThat is on track for a soft launch next week, aiming to replace Scrunch and Profound as the primary tool for tracking prompts, competitors, and market context.

---

## Key Topics

### Content Production & Pipeline

  - **DER Articles:** The final batch of 5 agentic and 6 data engineering articles is published.
  - **Thought Leadership:** 2 articles are reviewed and ready; a 3rd is due today.
      - The missing replication diagram is now complete.
  - **Next Focus:** The remaining 12 agentic articles.

### Agent Use Case Pages

  - **Wireframe:** A draft is ready for the "IT Onboarding Agent" use case.
  - **Feedback (Tanmay):**
      - **CTA:** "Deploy your onboarding agent" is too strong for the current stage.
      - **Visuals:** Replace placeholder stars with product screenshots.
      - **Content:** Must be technical and content-heavy to provide value and avoid appearing "AI-generated."
  - **Research:** Erik will research competitor pages (Composio, Merge) for inspiration.
  - **Idea (Tanmay):** Experiment with long-form articles for use case keywords to test SEO performance against dedicated pages.

### Performance & Optimization

  - **Agentic Article Performance:**
      - **Traffic:** \>1,300 sessions in January.
      - **Audience:** 1.25x sessions:visitor ratio → strong new audience acquisition.
      - **Engagement:** The "agent data platform" article showed unusually high engagement (73 min), which requires investigation.
  - **Cluster Performance:**
      - **Dominant:** "Context Engineering."
      - **Underperforming:** "Enterprise Agents and Governance & Security" (11.6% engagement).
          - **Action:** Review content for readability and tone to boost engagement.
  - **GSC Top Performers:** "LLM hallucinations" and "context window limits" articles continue to lead in Google search.

### Tooling & Workflow

  - **Connectors Page Workflow:**
      - **Problem:** The auto-publish workflow failed for new connectors, as it lacked a "previous state" to compare against.
      - **Fix:** Kirkland implemented a fix in two days.
      - **Result:** New and updated connectors will now auto-publish pages from the GitHub repo.
  - **CheckThat Tool:**
      - **Goal:** Replace Scrunch and Profound as the primary tool for tracking prompts, competitors, and market context.
      - **Status:** Soft launch planned for next week; Marcel will grant access.
      - **Blocker:** A bug is preventing prompt tracking; Erik is updating prompts manually in the interim.
      - **Category:** Erik is requesting a change from "ETL" to a more relevant category for market visibility.

---

## Action Items

**Erik O'Brien (GrowthX)**
- Email Tanmay wireframe link + content brief/examples; then Tanmay reviews/decides template
- Email Nithin DER articles list
- Research competitor use case pages (Composio, Merge) for inspiration

**Tanmay Sarkar (Airbyte)**
- Build monthly engagement dashboard per article
- Review agent use case wireframe and research page templates
- Decide on final page template after Erik shares research

**Kushal Chatterjee (Airbyte)**
- Receive content brief format and examples from Erik for thought leadership articles

---

## Transcript

**Nithin:** This meeting is being recorded.

**Erik O'Brien:** My camera's resetting.

**Erik O'Brien:** All right, let's jump into it. So, as typical, we've got five agentic and six data engineering resource articles reviewed and published this week. That was the final batch of data engineering resource articles, so we'll move to those 12 agentic articles next week.

**Erik O'Brien:** We've got two thought leadership series reviewed and ready, I think, Kushal, if I'm not wrong there. We've got all comments addressed. And finally got that diagram for the ones from last week for replication.

**Kushal:** Yep. Sorry that took so long.

**Kushal:** I think we're good for time for the next couple of weeks. So thank you.

**Erik O'Brien:** Absolutely. And then we should have one more coming out today. So we'll still be pretty ahead, but we'll send it over and we can start review next week.

**Erik O'Brien:** Tanmay, I'm not sure if you saw Kirkland's latest note, but he ran into an issue with the workflow for the connectors page. It was missing a previous state for those connectors, so it just assumed nothing had changed. He's already fixed it, so all of the latest connectors should be populated with pages now.

**Tanmay Sarkar:** Got it.

**Erik O'Brien:** Now when we get new connectors up and running, or if those existing connectors have updates, we will be able to auto-publish those. So things are looking good on that end.

**Tanmay Sarkar:** So whenever we add any new connectors on our GitHub repo, it will be automatically added?

**Erik O'Brien:** Yep. Which is great that he was able to do that in like two days.

**Tanmay Sarkar:** Yeah, he's good.

**Erik O'Brien:** For the agent use cases, we had the team create a mock-up wireframe using your template. We're working with the IT onboarding agent as an example. A few questions: we want to remove these placeholder stars and link to the new GitHub for agent connectors. Also, "Deploy your onboarding agent" feels like a heavy CTA for the current stage.

**Tanmay Sarkar:** Yeah, we can change those. This is just a format, that's fine. I want to see what will be in the place of the dashboard section—some product screenshot ideally. For each use case, we can't add different screenshots, so it'll likely be static. But to rank more of these pages, it should be content-heavy and technical. Otherwise, it will look like AI-generated pages with not much value. So we should think about how we can provide real value. I'll have a look and research some templates.

**Erik O'Brien:** Yeah, I was trying to look across Composio and Merge and a few others. They have use case pages, but they're very document-heavy, so not as useful as what we're trying to do. I'll continue looking around for inspiration that we can pull in.

**Tanmay Sarkar:** We can showcase our identity customers in this section. This template we have on our website, so the team just adapted it. Let me have a look, then we can decide on the final page template. I'll also do research from my end.

**Erik O'Brien:** Okay. I want to get that in place so we can create the template in Webflow and then pipeline it. Yeah, so Kushal, I still owe you the content brief that we use to populate context for the other thought leadership articles. I'll get that over to you today with a couple of examples as reference.

**Tanmay Sarkar:** I have one more idea. I know use case pages are something I've seen and generated in my previous companies. But I was thinking to experiment with those use case keywords in long-form content as well—for example, "IT Onboarding Agent" as a topic for a long-form article with content blocks for engagement. It should be content-heavy and technical, not look like a typical AI-generated page. I'll see what I can do and probably test one to see how it performs.

**Erik O'Brien:** Yeah, I was also thinking about Jacob's idea of domain-specific PSL opportunities. Maybe we can reference that for agent accounting use cases and have a more in-depth list for individual use cases. We've got quite a few ideas for next week that we want to push out and explore where else we want to place bets outside our current keyword groups.

**Erik O'Brien:** Now looking at performance for the agentic articles, we're seeing really rapid growth, which is awesome. We're heading over 1,300 sessions in January with quite a few unique visitors, so we have a 1.25x sessions-to-visitor ratio. This shows we're driving primarily new audience acquisition for these articles.

**Tanmay Sarkar:** Yeah, and overall with time this number will increase because we're adding more articles. But we also should see each article's performance and engagement for every month. If that grows, that means the article is doing well. We'll build that dashboard so you can see monthly data, not just URL-based analytics.

**Erik O'Brien:** Yeah, there was this agent data platform article with ridiculously high engagement time—I forget exactly what it was.

**Tanmay Sarkar:** Yeah, that's one issue. It was showing 73 minutes, which seems wrong. I was like, is this one session from one person? That can't be right.

**Erik O'Brien:** We'll continue to look at which ones are performing really well and try to enrich those so we can maintain high engagement for top performers. Overall, from a cluster view, Context Engineering is the dominant cluster—no surprise there, it's a super hot topic right now. MCP servers and agent data access show decent growth. We have quite a few content ideas for that pipeline. But overall, engagement rates for Enterprise Agents and Governance & Security are lower than we want—11.6% engagement. We'll take a look at boosting readability and voice and tone for that cluster. From GSC data, "LLM hallucinations" and "context window limits" are still leading in Google search results.

**Tanmay Sarkar:** I have one or two questions. Will you be writing articles on the topics I shared this week?

**Erik O'Brien:** Yep, for next week.

**Tanmay Sarkar:** And we have shared the list of prompts that you want to track. Will you be adding those in CheckThat?

**Erik O'Brien:** Yes. We've run into a few bug issues we're trying to resolve before the soft launch next week.

**Tanmay Sarkar:** I pinged Marcel and he said he can give me access next week.

**Erik O'Brien:** Yeah, that's the plan. I've been going in and updating the prompts manually. You guys are still listed in the ETL category, so I'm asking the team if we can get that updated for better market visibility. But prompts, contacts, competitors—all that stuff I've been updating on the side. In the meantime, we still have access to Scrunch, and that's been fully updated to the new direction we're going.

**Mario:** I have one question. Once CheckThat is fully released, is that a one-to-one replacement for Profound or Scrunch?

**Tanmay Sarkar:** Marcel said we're launching as a private preview.

**Mario:** But once it's fully launched, Erik, do you expect your clients to be able to rely on CheckThat without needing Profound or Scrunch?

**Erik O'Brien:** Yeah, that's the goal. We're trying to have a larger view of each market that clients and their competitors are in, and then have a separate space specific to which competitors we're actually targeting and the prompts we want to target specifically for our brand.

**Mario:** That makes sense. Thank you.

**Erik O'Brien:** Anything else on your mind?

**Tanmay Sarkar:** No, I think we're good.

**Erik O'Brien:** Okay. Nithin, we'll get you that list of where we left off for the DER articles early next week.

**Nithin:** Yeah.

**Erik O'Brien:** Wonderful. Feel free to reach out with any questions or anything that comes up. In the meantime, I'll send over that link for the wireframe.

**Tanmay Sarkar:** Thanks, Erik. Good evening, everyone.
