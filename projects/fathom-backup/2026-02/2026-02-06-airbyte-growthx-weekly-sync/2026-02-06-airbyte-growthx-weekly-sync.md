# Airbyte <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-06
time: 16:29 UTC
duration: 21 minutes
organizer: team@growthxlabs.com
participants: Tanmay Sarkar (Airbyte), Nithin Mahalingam (Airbyte), Mario Moscatiello (Airbyte), Kyle Gaudreau (GrowthX), Kushal Chatterjee (Airbyte), Erik O'Brien (GrowthX), Team GrowthX
fathom_recording_id: 120432734
fathom_url: https://fathom.video/calls/557887406
share_url: https://fathom.video/share/dqZB_QxnZPhdtZxYP-YfigeE-x5vn2Uk
source: fathom
enriched_on: 2026-02-27T18:18:02Z
</metadata>

---

## Summary

Airbyte and GrowthX aligned on Agent Engine's soft-launch strategy (Monday, public beta at app.airbuy.ai) and major campaign push scheduled for May. The team shifted AI tracking focus from explanatory prompts to high-intent queries using check.ai, targeting user evaluation phases. January content performance hit 1.6k sessions with strong developer engagement on "Building Production Agents," signaling readiness for technical content expansion and on-page optimization using new Webflow analytics tools.

---

## Context

This is the weekly coordination sync between Airbyte's product and growth teams and GrowthX, the B2B content marketing partner. The session focused on three interconnected initiatives: preparing the public beta launch of Agent Engine (the product that powers Airbyte's AI capabilities), optimizing content performance metrics for an emerging technical audience, and refining the AI visibility strategy through smarter prompt tracking.

Agent Engine's launch strategy reflects a phased approach. The soft launch on Monday (February 10) is designed for early adopter feedback at low volume; the major amplification campaign with PR, paid ads, and conference presence happens in May. This timing creates space for internal iteration and customer learning before scaling.

---

## Relevance

- **Product Launch**: Agent Engine soft launch Monday (February 10) with article, product page, beta signup flow (app.airbuy.ai), and sales conversation pathway. Tracking live through HockeyStack conversion events.
- **Content Performance**: 1.6k January sessions, 1.1k unique visitors. "Building Production Agents" pillar showing exceptional developer retention (low bounce rate). Traffic expected to double in February with 12 new articles in review.
- **AI Tracking Strategy**: Pivot from tracking generic explainer queries ("What is AI?") to high-intent tool/platform recommendations ("Which tools provide connectors for AI agents?"). Using check.ai instead of Scrunch, leveraging Query Fanouts feature for prompt discovery.
- **Content Optimization**: Bounce rates above industry average (30–40%) require technical depth. New Webflow Analyze & Optimize features provide click-level data for interactive element placement and engagement improvements.
- **Stakeholder Coordination**: Cross-functional handoff between Airbyte (product, strategy, content review) and GrowthX (execution, tracking, analytics) with clear ownership and timelines.

---

## Overview

- **Agent Engine Soft Launch:** The public beta (`app.airbuy.ai`) launches Monday with a new article. This "soft launch" is for early customer feedback before a major campaign in May (PR, ads, conferences).
- **AI Tracking Strategy Shift:** The focus is moving from tracking explanatory prompts to high-intent prompts that trigger tool/platform recommendations, aiming to capture users in their evaluation phase.
- **Content Performance:** January traffic hit 1.6k sessions. The "Building Production Agents" pillar has a low bounce rate, signaling strong developer interest and a need for more technical content.
- **On-Page Optimization:** New Webflow tools will provide click data to guide on-page improvements (e.g., interactive elements) to reduce high bounce rates, which currently exceed the 30–40% industry average.

---

## Key Topics

### Agent Engine Launch & CTAs

  - **Launch Plan:** A "soft launch" on Monday for the public beta (`app.airbuy.ai`) will gather early customer feedback. A major campaign (PR, ads, conferences) is planned for May.
  - **CTA Updates:** All articles will be updated with new CTAs linking to:
      - Product Page: `airbuy.com.ai`
      - Public Beta Sign-up: `app.airbuy.ai`
      - Launch Article (publishes Monday)
      - Talk to Sales
  - **Tracking:** Public beta sign-ups will be tracked as a HockeyStack conversion event, mirroring the current "cloud signup" for the Replication Engine.

### Content Performance & Optimization

  - **January Traffic:** 1,600+ sessions, 1,100+ unique visitors.
  - **Pillar Performance:**
      - **High Engagement:** "Context Engineering," "MCP Servers," "Building Production Agents."
      - **Low Bounce Rate:** "Building Production Agents" → signals strong developer interest.
      - **Low Engagement:** "Enterprise Agent Governance and Security" → may require a topic rethink.
  - **Optimization Strategy:**
      - **Goal:** Reduce high bounce rates (currently above the 30–40% industry average).
      - **Tactics:**
          - Add more developer-centric content (e.g., code snippets).
          - Use new Webflow tools to analyze click data and guide on-page improvements (e.g., interactive demos).

### AI Tracking Strategy

  - **Problem:** Tracking explanatory prompts (e.g., "What is X?") yields low product traction, as users consume the answer directly from the LLM.
  - **Solution:** Shift focus to high-intent prompts that trigger tool/platform recommendations (e.g., "Which tools provide connectors for AI agents?").
  - **Implementation:**
      - **Tool:** Using `check.ai` to track prompts, replacing `Scrunch`.
      - **Process:**
        1.  Airbyte team will mark high-intent prompts in the existing list.
        2.  Erik will upload the refined list to `check.ai`.
        3.  Erik will use `check.ai`'s "Query Fanouts" feature to find similar high-intent queries.

### Content Production & Review

  - **Article Pipeline:**
      - **This Week:** 12 articles for review (5 new, 1 in progress).
      - **Pending:** "Why agents need ontology" (awaiting Kushal's review).
  - **Wireframe Review:**
      - **Problem:** Tanmay cannot comment on the wireframe in `Lovable`.
      - **Solution:** Erik will request comment access from designer Talal. If unsuccessful, Erik will upload a page image to Notion for feedback.

---

## Action Items

**Tanmay Sarkar (Airbyte)**
- Review 5 new Airtable articles from Joe; send go-ahead to Erik
- Join Erik's check.ai workspace and add Airbyte context
- Mark high-intent prompts in shared sheet; send updated list to Erik
- Research and identify additional high-intent prompts for expansion

**Erik O'Brien (GrowthX)**
- Ping Kushal re: "Why agents need ontology" article review
- Update CTAs across all articles to new Agent Engine links (product page, beta signup, launch article, sales)
- Coordinate with Talal to enable Tanmay's wireframe commenting in Lovable; if blocked, upload page image to Notion for feedback
- Notify Joe re: Agent Engine CTA links and ensure updates across articles
- Grant Tanmay edit access to check.ai workspace
- Upload refined, high-intent prompt list to check.ai once Tanmay marks it
- Use check.ai's Query Fanouts feature to identify similar high-intent queries
- Send DER (Data Exchange Router) articles list to Nithin

**Nithin Mahalingam (Airbyte)**
- Receive DER articles list from Erik
- Continue research on high-intent prompt identification
- Support Tanmay in marking and curating prompts from shared list

---

## Transcript

**Erik O'Brien:** Hey, Nithin.

**Nithin:** How's your week been?

**Erik O'Brien:** Good. Just confirming, did you see all 11 of those articles that we sent through Airtable?

**Tanmay Sarkar:** I think I saw six which you sent earlier, right?

**Erik O'Brien:** Yeah, so Joe uploaded five more for review. And then he's working on one more to get done today, so we'll have 12 for this week.

**Erik O'Brien:** And then "Why agents need ontology" is still in review. I haven't seen any comments come through on that yet, but I'll ping Kushal just to remind him. We're still working through the TLDR refreshes, 50 a week, as planned.

**Tanmay Sarkar:** I'll check those.

**Erik O'Brien:** Did you have a chance to take a look at this wireframe this week at all?

**Tanmay Sarkar:** Yeah, I checked that. But the issue is I can't leave any comment there. In Lovable, I can't leave comment. How do you want to go ahead with this?

**Erik O'Brien:** Let me see if we can open that up or if Talal can invite you to it so we can work on it together. If that doesn't work, I'll find a different approach for us to leave feedback.

**Tanmay Sarkar:** Yeah, if that doesn't work, I think what I can do is if you can upload the whole page image to Notion, then I can comment directly on Notion.

**Erik O'Brien:** Gotcha. I'll check with Talal, and if that doesn't work, I'll just upload it to Notion and we can go from there.

**Tanmay Sarkar:** There are three main links for Agent Engine. One is the product page, airbuy.com.ai. Two is the sign-up page, the public beta at app.airbuy.ai. Third is the launch article, which we'll publish on Monday because Monday is our launch. And also "Talk to Sales."

**Erik O'Brien:** I will let Joe know and we will get those updated, and we'll watch for the launch article on Monday. Sounds like the private preview is pretty short.

**Tanmay Sarkar:** Yeah, it's pretty short. The public beta we're launching is kind of a soft launch. We're not making too much noise, but in May there will be big campaigns, including PR, ads, and conferences. So this is kind of a soft launch to test the water and onboard some early customers, and we'll go ahead from there.

**Erik O'Brien:** How many customers are in the beta so far, or using what's available?

**Tanmay Sarkar:** For beta, there would be around 50 people. And there's an open source MCP that's already there, which people are using. We can see it on GitHub.

**Erik O'Brien:** For these CTAs, I know we can track "Talk to Sales" as a conversion event. Is the public beta page able to be tracked through HockeyStack?

**Tanmay Sarkar:** Yeah, just like currently we have "cloud signup" for Replication Engine, there will be cloud signup data for Agent Engine as well.

**Erik O'Brien:** Okay, cool. I was talking to Mario on Monday. We'd love to get closer to being able to see those conversion events. The private beta one was off the main site.

**Tanmay Sarkar:** Yeah, I think initially once we set up and make this live, the data team will set up everything in MetaBase and then we will run it.

**Erik O'Brien:** Looking at traffic through January, we had over 1,600 sessions with 1,100 unique visitors. We're seeing steady growth compounding as we continue to publish. We expect February, given the scaled efforts here, to hopefully double this amount if not more. There are 38 pages live, and we'll get 12 from this week live as soon as you give us the go-ahead.

**Erik O'Brien:** Three pillars are dominating most of the sessions: Context Engineering, MCP Servers, and Building Production Agents. Building Production Agents has a really low bounce rate, which signals strong developer interest. I was talking to Mario and thinking about how we can include more technical, developer-centric content in these articles.

**Erik O'Brien:** Enterprise Agent Governance and Security is the lowest engagement. We might need to rethink topics in that cluster. For AEO, we've got a couple weeks of tracking data against the prompts across both Scrunch and Check.ai. We're seeing about 5% visibility, which is pretty good for this early. About 20 articles are showing up as citations in prompt responses, so about half of what we published are already getting cited.

**Tanmay Sarkar:** I saw the launch yesterday that Marcel posted. How do you want to go ahead with this? Will you be using both platforms or moving forward, shutting down Scrunch and only using check.ai?

**Erik O'Brien:** For me, I'm continuing to monitor both. I'm personally invested in check.ai. So we'll be using it pretty frequently and giving feedback to the team about improvements we want to make to get feature parity with Scrunch and then eventually Profound. I invited you to check.ai, so you should have an invite in your inbox.

**Tanmay Sarkar:** I already signed up yesterday. But I need to add more context. And is there any limit in check.ai?

**Erik O'Brien:** If you sign up by yourself, there's probably a limit of 75 custom prompts. In the space we have set up for you, you've got unlimited.

**Tanmay Sarkar:** Yeah, I'll just join that space. And so I was telling Nithin the other day, we should track prompts where the reply will be a platform or a tool, not like "What is the difference between MCP versus something else?" Those are explanatory questions. People ask them but don't find your website. Hardly anyone goes to your website. They just consume the answer from the LLM and close.

**Tanmay Sarkar:** But we need intent from the LLM. So for example, "Which are the tools that provide connectors and real-time data for AI agents?" Then Airbyte and other tools will come. We need those kinds of prompts where the reply will be a tool or platform.

**Erik O'Brien:** So more of the evaluation phase versus general advice.

**Tanmay Sarkar:** Yeah. For explanatory prompts, we might rank but it's not our goal because we won't get anything from that. It will help the LLM but not the product. People can read and stay longer in the LLM but we won't get any traction. What we're doing internally is we have a list of prompts that we've already shared with you. Those prompts are in Scrunch. We can mark those separately and share with you, then update that list in check.ai.

**Tanmay Sarkar:** We will do more research to find more prompts. Nithin is working on that. Once we share the first list, you can feed that data into check.ai and get more similar queries. Profound has a feature called Query Fanouts. So if I ask "What is data integration?" it extends the query to multiple different queries like "What does data integration do?" and "What are the types of data integrations?" We can collect those from Profound, then make a list and share with you.

**Erik O'Brien:** Awesome. Yeah, with Scrunch when you're starting from zero and have to do that research, it would take a few hours to create a list. But yeah, I can take the existing ones and find similar prompts. Those Query Fanouts really help because that's something I've been curious about but haven't found a tool to do it. Obviously we don't use Profound, but that's perfect.

**Tanmay Sarkar:** Yeah, and in this list there are many prompts which are not directly related to that intent. So we can share the final updated list or mark it in the sheet, and then you can upload those. How many prompts have you added in check.ai in the Airbyte workspace?

**Erik O'Brien:** All the prompts that you shared with me. I cleared out the existing prompts that they had for legacy data replication and replaced them with these ones. These 99 were the ones that were high-intent.

**Tanmay Sarkar:** Got it. Yeah, I can also edit as you give me access.

**Erik O'Brien:** Cool. Any other questions or things top of mind for this week outside of getting some of these articles published?

**Tanmay Sarkar:** So we now have Webflow Optimize and Analyze, which we purchased during our renewal with them. Inside Webflow, we'll have more data in terms of what people are clicking on, whether they're clicking CTAs, and how we can improve page engagement and lower bounce rates. Currently, content articles are long but have no interactive elements like demos. We have to spend time optimizing those as well. I'm very busy for the launch, but after that I'll have more time to think about those.

**Erik O'Brien:** That's something I was even asking Kyle about. Our bounce rates are pretty high compared to what we want them to be. I think 30 to 40% is industry average, and we're a little bit lower on average. He has some ideas but a lot is guessing. I think once you guys get that data and as the product launches, we can go back and include YouTube videos or other interactive stuff. We're trying to figure out how to include more developer-friendly content in these articles so it's not just a wall of text.

**Tanmay Sarkar:** Absolutely.

**Erik O'Brien:** Any other questions, Nithin?

**Nithin:** No, this sounds good.

**Erik O'Brien:** We still owe you that list of DER articles, so we'll get that to you.

**Tanmay Sarkar:** Okay. I think we're good. Thanks, Erik.

**Erik O'Brien:** Thanks for the time. Talk to you next week.
