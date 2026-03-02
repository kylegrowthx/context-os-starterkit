# Airbyte <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-23
time: 16:30 UTC
duration: 20 minutes
organizer: team@growthxlabs.com
participants:
  - name: Tanmay Sarkar
    affiliation: Airbyte
    role: Product/Strategy Lead
    email: tanmay@airbyte.io
  - name: Nithin Mahalingam
    affiliation: Airbyte
    role: Content/Product Lead
    email: nithin.mahalingam@airbyte.io
  - name: Kushal Chatterjee
    affiliation: Airbyte
    role: Product Manager
    email: kushal.chatterjee@airbyte.io
  - name: Erik O'Brien
    affiliation: GrowthX
    role: Senior Content Manager
    email: erik@growthx.ai
  - name: Kyle Gaudreau
    affiliation: GrowthX
    role: Analytics & Engagement Lead
    email: kyle@growthx.ai
fathom_recording_id: 116720917
fathom_url: https://fathom.video/calls/541148490
share_url: https://fathom.video/share/RcGxpD3u_-9_pY7YxBRki63MRgvD4SaF
source: fathom
enriched_on: 2026-02-28 14:32 UTC
</metadata>

---

## Summary

Weekly sync between Airbyte and GrowthX covering content production status, analytics insights, and platform development. Key accomplishments include 50 TLDR refreshes completed and Agent Connectors template now editable; main initiatives focus on optimizing low-performing pages, developing new diagrams for thought leadership articles, and positioning CheckThat.ai as an agentic competitor tracking tool.

---

## Context

This is a recurring weekly operational sync between GrowthX's content team (led by Erik O'Brien) and Airbyte's product and content leads (Tanmay Sarkar, Kushal Chatterjee, Nithin Mahalingam). The engagement involves B2B content marketing for Airbyte's Agentic platform, with focus on thought leadership, technical documentation, and competitive intelligence via CheckThat.ai platform. The team is in active execution mode, balancing content delivery, analytics optimization, and new product feature development. GrowthX is paid engagement ($40k/month); Airbyte provides both product context and design partnership feedback.

---

## Relevance

**For Content & SEO Strategy:**
- Demonstrates traffic growth validation through HockeyStack data (1.2–1.3x growth driven by new audience acquisition)
- Identifies engagement bottlenecks (e.g., "document chunking" page) requiring tactical improvements (new image formats, programmatic interlinking)
- Reveals need for GSC audit and low-performing page optimization across agentic articles

**For Product Development:**
- Agent Connectors template is now production-ready (prompt and entity sections editable), unblocking workflow for 15+ pages
- Agent Use Cases wireframe in review before pipeline build-out
- CheckThat.ai platform shifting focus to agentic competitors and prompts; Airbyte positioned as design partner

**For Operational Tracking:**
- Action items clearly assigned (Erik: briefs & workflow testing; Nithin: audits & GitHub updates; Kushal: diagram options)
- Diagram bottleneck for thought leadership article is known and scoped (simplify existing Airbyte diagram, remove connector-specific details)

---

## Overview

- **Content Production:** On track, with 50 TLDR refreshes complete. A new diagram for a thought leadership article is the only blocker; it will be a branded, simplified version of an existing internal diagram.
- **Agent Pages:** The template is now editable (prompt & entity sections), unblocking the workflow for 15 Agent Connector pages. The workflow will be tested with a single page first.
- **Traffic Analytics:** New HockeyStack data shows traffic is growing (\~1.2–1.3x) from new audience acquisition, not repeat users—a positive early signal. Nithin will audit Google Search Console (GSC) data to find low-performing pages for optimization.
- **CheckThat.ai Platform:** The platform is being updated with Agentic competitors and prompts. Airbyte will act as a design partner, providing feedback to shape the tool's development.

---

## Key Topics

### Analytics & Engagement

  - **HockeyStack Data:** Access granted, providing granular session vs. unique visitor data.
      - **Finding:** Traffic growth (\~1.2–1.3x) is driven by new audience acquisition, a positive early signal.
  - **Google Search Console (GSC) Audit:**
      - **Action (Nithin):** Pull GSC data (impressions, clicks) for all Agentic articles to identify low-performing pages.
      - **Goal:** Optimize these pages (add content, backlinks) to increase visibility.
  - **Engagement Rate Improvement:**
      - **Problem:** Low engagement on some pages (e.g., "document chunking").
      - **Action (Erik):** Discuss new engagement tactics with Kyle (e.g., new image formats).
      - **Suggestion (Tanmay):** Implement programmatic interlinking with relevant anchor text to improve SEO and user flow.

### Content Production & Workflow

  - **Thought Leadership Article:**
      - **Blocker:** A diagram is needed for one section.
      - **Guidance (Kushal):** Use an existing internal diagram as a basis, but simplify it for a generic audience by removing Airbyte-specific connectors.
  - **New Content Briefs:**
      - **Need:** More context from Airbyte to write new articles, as existing source material is insufficient.
      - **Action (Erik):** Send content briefs to Kushal for completion.
      - **Action (Kushal):** Fill out the briefs; schedule a follow-up call if more context is needed.
  - **Image Optimization:**
      - **Finding:** Agent image sizes were unexpectedly large (3MB), now compressed to \~50KB.
      - **Action (Nithin):** Audit all images to ensure proper compression.
      - **Action (Joe):** Check image sizes on TLDR articles during the refresh process.

### New Initiatives

  - **Agent Connectors:**
      - **Status:** Template is now editable (prompt & entity sections), unblocking the workflow.
      - **Plan:** Test the workflow with a single page before automating the remaining 14.
  - **Agent Use Cases:**
      - **Status:** Wireframe is in review; feedback will be incorporated before sharing.
      - **Plan:** Develop the wireframe and template before building the content pipeline.
  - **CheckThat.ai Platform:**
      - **Status:** Platform is being updated with new Agentic competitors and prompts.
      - **Action (Nithin):** Add other Airbyte prompts to the shared sheet for inclusion.
      - **Plan:** Provide Airbyte with access soon to act as a design partner and provide feedback.

---

## Action Items

**Nithin Mahalingam (Airbyte)**
- Audit agent image sizes post-compression
- Update GitHub repo with latest Agent Connectors template changes
- Pull Google Search Console (GSC) impressions and clicks for agentic articles; share findings with Erik
- Add new tab to shared prompts sheet with additional Airbyte prompts; share with Erik

**Erik O'Brien (GrowthX)**
- Build and test Agent Connectors workflow on 1 page; share results with Tanmay
- Notify Kirkland regarding Entity and Prompt sections now being editable in Agent Connector template
- Blend GSC click data into Looker dashboard to complement GA4 session metrics
- Share 2 new thought leadership articles in Slack with Tanmay and Kushal
- Send content briefs to Kushal for completion; follow up with call if needed for additional context
- Finish data engineering resource articles; provide Nithin with updated list

**Kushal Chatterjee (Airbyte)**
- Draft and share 2–3 diagram options for thought leadership article with Erik
- Complete content briefs sent by Erik with product context to support new article development

---

## Transcript

**Erik O'Brien (GrowthX):** This meeting is being recorded. We're still waiting for Kushal. I have a question for him, but if he doesn't join, I can just throw it through Slack. I figured it'd be easier to chat through live.

**Tanmay Sarkar (Airbyte):** I don't know if he joined. We can probably start. Once he joins, you can ask him that question.

**Tanmay Sarkar:** He's running a few minutes late, so we can start.

**Erik O'Brien:** All right. So long story short, all content production is on track for this week. The only thing holding up our latest thought leadership series article is getting a diagram for one section, which is my main question for Kushal. We'll have two more thought leadership posts to share today that Joe is working on. We completed 50 TLDR refreshes. I'm also having Joe audit image sizes on the TLDR articles to make sure they're not oversized like the agent images were. I don't believe it's the same issue as the pipeline we set up for agent images, but we'll double-check.

**Tanmay Sarkar:** For all agents, the new images have been updated with lower sizes, right?

**Tanmay Sarkar:** Lower sizes than previous. They went from about 3 megabytes to about 50 kilobytes.

**Tanmay Sarkar:** Nithin, you can cross-check and run an audit.

**Nithin (Airbyte):** Yeah.

**Erik O'Brien:** That was definitely a surprise because most of our images aren't close to that size. The team put a compression step after generation.

**Tanmay Sarkar:** Makes sense.

**Erik O'Brien:** For Agent Connectors, we talked about those yesterday, Tanmay. We'll build and test that workflow with a single connector page. Hopefully get something to you early next week. The only update needed was to make the prompt section and entity section editable in the template.

**Tanmay Sarkar:** Yes, they're in docs pages. I want to show you something. We have three connectors live now, so you can pick any outside those three. Yeah, Kirkland mentioned yesterday that this section should be editable. Nithin, did Diego make the changes to make this editable?

**Tanmay Sarkar:** Okay, it's done then, Erik. And the prompt section is also editable, Nithin?

**Nithin:** Okay, cool. Both have been edited. But we need to update the GitHub code.

**Tanmay Sarkar:** Yeah, they know. That's fine.

**Erik O'Brien:** Okay. So we'll continue working through that. I believe there are 15 for now, but once we get the automation set up, we'll push new ones through as they populate. For the Agent Use Cases, we have a teammate developing a wireframe. I'm giving feedback today before showing you guys. We'll make sure the wireframe and template are done before setting up the pipeline. I was able to get access to HockeyStack. I found an old email from last March with a link that still worked. It gives a great breakdown of overall sessions versus unique visitors. We grew about 1.2 to 1.3x, primarily from new audience acquisition rather than repeat users, which is a really good signal early on. Overall growth continues in the right direction.

**Tanmay Sarkar:** The more content we put out, hopefully we'll see compounding traffic and unique visitor growth. I'd also run an audit, Nithin. Pull Google Search Console data in terms of impressions and clicks for all published agentic articles. That way we can see which pages are getting visitors and which aren't so we can optimize them.

**Nithin:** We should add content, create backlinks, and build mentions to increase visibility.

**Erik O'Brien:** In our Looker dashboard, we can see which pages get the most sessions and engagement rate. Through this week, it looks like...

**Tanmay Sarkar:** Can you add clicks here, right, Erik?

**Erik O'Brien:** This is GA4 data, so not GSC.

**Tanmay Sarkar:** Oh, okay. It's not GSC. But I think you can pull GSC data into Looker too.

**Erik O'Brien:** Yeah, I'll see if I can blend the data and get a clicks count in here.

**Erik O'Brien:** Engagement rate isn't great for the document chunking article. I'm talking to Kyle in about an hour to see what else we can test to boost engagement or hold people longer. We could introduce new images, like more diagrams versus just infographics. We're looking to set up that pipeline.

**Tanmay Sarkar:** One thing I have in mind is interlinking with relevant anchor text and keywords. We can interlink across all these pages, which helps pass link value and improve ranking from Google. We can automate the interlink structure programmatically. We've done that before.

**Erik O'Brien:** Yeah, I'll talk to Joe. For data engineering resources, we can target that subfolder and have it find relevant articles to interlink. Now that we have about 25 agentic articles, we can start interlinking between those. We can also weave in new terminology from the Thought Leadership Series, like "What is an entity graph?" and "replicated index," define them, and link back to the thought leadership articles.

**Tanmay Sarkar:** That makes sense. We can also do cross-linking from thought leadership to agentic category, from Substack to blog and vice versa.

**Erik O'Brien:** Hey, Kushal. Sorry, I didn't see you join.

**Kushal Chatterjee (Airbyte):** Hey, how's it going?

**Erik O'Brien:** Good. I have a question on the diagram we need. I saw Jean's Loom video, which clarifies how the system works. From a diagram perspective, do we just clean up your version and make it more branded, or do you have different ideas about what we want?

**Kushal:** I feel like you could use our diagram and improve it a bit. The thing is, it might not be clear what the direct connectors versus replication connectors are. I'd say don't include everything in the diagram, just the stuff relevant to a more generic system that doesn't necessarily use our connectors.

**Erik O'Brien:** Gotcha. I wanted to make sure we were aligned so I can ping our designer today. I'll get a couple of different versions so we have choices. I think that's the only thing holding it up for being production ready.

**Kushal:** I'll get it. We've been good on content. It's fine if we get them next week. But I need context for new content briefs. Is there a form I could fill out that would help answer your key questions?

**Erik O'Brien:** I think it would be helpful if you give me a doc with a few questions or information you need. I can fill that out quickly using our knowledge base and internal AI. I'll send the content brief template. Can you fill it out? If you have questions, we can jump on a call and I can walk through them.

**Kushal:** That works. Yeah, let me fill out the brief.

**Erik O'Brien:** Okay, awesome. That's mostly updates for this week. Anything else top of mind?

**Tanmay Sarkar:** Yeah, one thing. We shared those prompts. When do you think you'll add them to CheckThat.ai?

**Erik O'Brien:** CheckThat.ai, right? I need to get the new competitors added since they weren't in there. I'm waiting for the team to get those added.

**Tanmay Sarkar:** Do you need data from us?

**Erik O'Brien:** No, not from you. We've been tracking your previous competitors, so they're already loaded. But with the new agentic competitors, they weren't on the platform yet, so I put in a request to add them to the index.

**Tanmay Sarkar:** So CheckThat.ai will only track agentic prompts or both products?

**Erik O'Brien:** Based on the direction, we're going with agentic only. I set up six competitors in Scrunch this morning.

**Tanmay Sarkar:** Those are fine. You've also updated Scrunch?

**Erik O'Brien:** Yeah, this morning. It'll take a while to populate. I added the key topics you sent over. Are there additional Airbyte prompts you're tracking in Profound outside the article-based ones?

**Tanmay Sarkar:** Yeah, there are a few. Nithin, add another tab to the sheet with those prompts.

**Erik O'Brien:** CheckThat.ai is still in beta, so we'll get you access soon. We want you guys to be design partners—tell us what you want, what's missing compared to Profound. I'll get you access sooner than later. Just know I'm updating the backend to focus on agentic versus old competitors.

**Tanmay Sarkar:** Makes sense. Sounds good.

**Erik O'Brien:** Anything else top of mind?

**Tanmay Sarkar:** No, I'm good. Nithin, Kushal, any questions?

**Erik O'Brien:** Nothing from my end. Nithin, we'll finish the data engineering resource articles through next week and update you on where we are.

**Nithin:** Yep. Thanks, Erik.

**Erik O'Brien:** Awesome. All right, guys, appreciate the time.

**Tanmay Sarkar:** Have a good weekend. Bye.

**Erik O'Brien:** Bye.
