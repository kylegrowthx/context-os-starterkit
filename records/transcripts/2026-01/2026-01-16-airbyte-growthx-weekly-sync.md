# Airbyte <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-16
time: 16:29 UTC
duration: 28 minutes
organizer: team@growthxlabs.com
participants:
  - name: Tanmay Sarkar
    affiliation: Airbyte
  - name: Nithin M
    affiliation: Airbyte
  - name: Mario Moscatiello
    affiliation: Airbyte
  - name: Kyle Gaudreau
    affiliation: GrowthX
  - name: Kushal Chatterjee
    affiliation: Airbyte
  - name: Erik O'Brien
    affiliation: GrowthX
fathom_recording_id: 114924760
fathom_url: https://fathom.video/calls/533454481
share_url: https://fathom.video/share/keL_uyGwsq1LiD8PYyxm7zTj7LLoGLxw
source: fathom
enriched_on: 2026-02-28 00:00 UTC
</metadata>

---

## Summary

Weekly sync between Airbyte product and GrowthX content teams to align on AI agents product launch strategy. Core topics: pausing "Agent Use Cases" content to prioritize technical "Connectors Pages," confirmed product roadmap (private beta next week, public beta late Feb, official launch May), and transitioning performance tracking from Scrunch to CheckThat.ai to better monitor agentic content effectiveness.

---

## Context

Airbyte and GrowthX have been collaborating on content and product launch strategy for Airbyte's new AI agents platform. This meeting occurred during the pre-launch phase, with the private beta rolling out the following week. GrowthX is responsible for content production (articles, TLDRs, thought leadership), while Airbyte product leadership provides go-to-market timing and technical requirements. The partnership requires close synchronization between content availability and product launch milestones to ensure supporting content is ready for each phase.

---

## Relevance

**Product Launch & Go-To-Market**
- Private beta launches next week (Jan 22 approx), public beta late February, official launch May
- Content strategy must align with these phases to support user acquisition
- Agent use case content can begin before official launch to drive awareness during beta phases

**Content Production**
- GrowthX has published 5 agentic articles, 6 DER articles, and 1 thought leadership piece; tracking on schedule
- Connectors Pages initiative shifts focus from use case content to highly technical product documentation
- TLDR refreshes continuing across 75 historical DER articles to improve SEO signal

**Performance & Analytics**
- Agentic content driving strong early traffic (250 sessions in week of Jan 15, 6x growth from December)
- Engagement rates below target; team exploring tactics to improve
- Moving prompt tracking from Scrunch to proprietary CheckThat.ai platform (launching Feb, design partnership with Airbyte)

---

## Overview

- **Content Focus Shift:** Pausing "Agent Use Cases" for now to prioritize building highly technical "Connectors Pages," which will auto-populate from GitHub content.
- **Product Launch Timeline:** The new product launches in phases: private beta (next week), public beta (late Feb), and official launch (May).
- **Performance Tracking:** Moving from Scrunch to GrowthX's new platform, CheckThat.ai, to improve prompt tracking for the agentic content strategy.
- **Traffic Growth:** Agentic content is driving strong traffic growth (250 sessions last week, 6x from Dec), but engagement is low.

---

## Key Topics

### Content Strategy & Production

  - **Production Updates:**
      - **Published:** 5 agentic articles, 6 DER articles, and 1 thought leadership piece ("Agentic data infrastructure must be open").
      - **In Review:** "Replication is the key for scaling agents" (due today).
      - **TLDRs:** Added to 25 existing articles; \~75 historical DER articles will be refreshed over the next few months.
  - **"Agent Use Cases" Paused:**
      - **Why:** To prioritize "Connectors Pages," which are easier to build by leveraging existing technical content from GitHub and Docs.
      - **Future Plan:** GrowthX will wireframe the use case template now to get a head start. Airbyte will provide a 1-month heads-up before engineering work begins.
  - **"Connectors Pages" Initiative:**
      - **Goal:** Create highly technical pages with auto-populating content (e.g., JSON code snippets) pulled directly from GitHub.
      - **Status:** Tanmay is finalizing a Webflow template and investigating the GitHub-to-Webflow API integration.
      - **Timeline:** Initial pages are expected to go live in a few weeks.

### Product Launch Timeline

  - **Private Beta:** Next week (\~Tuesday).
      - No public announcement; direct outreach to initial customers.
  - **Public Beta:** Late February.
  - **Official Launch:** May.
  - **Implication:** Agent use case content can be published before the official launch to support the public beta.

### Performance Tracking & Tools

  - **Conversion Tracking:**
      - **Tool:** Hockey Stack dashboard.
      - **Challenge:** The single "Talk to Sales" form mixes leads for the new product with leads for the existing replication product, making attribution difficult.
  - **Prompt Tracking:**
      - **Transition:** Moving from Scrunch to GrowthX's new platform, CheckThat.ai.
      - **Why:** To improve tracking of agentic content performance.
      - **Timeline:** GrowthX will set up the account with new topics/prompts. Airbyte gets access the week of Jan 26 to provide feedback as a design partner.
  - **Looker Dashboard:**
      - **Status:** Updated to focus on agentic content performance.
      - **Metrics:** 250 sessions last week (6x from Dec).
      - **Top Drivers:** "Context Engineering for AI Agents" and "Building Production AI Agents Cohort."
      - **Challenge:** Engagement is lower than desired; GrowthX will explore tactics to improve it.

### Website Performance

  - **Issue:** Agentic article cover images are too large (\~3MB).
  - **Impact:** Slows website load times and consumes excess CDN bandwidth.
  - **Action:** GrowthX will compress all future images.

---

## Action Items

**Erik O'Brien (GrowthX)**
- Mark remaining DER topics in sheet; Nithin (Airbyte) takes remaining articles
- Send 'Replication is the key for scaling agents' to Kushal (Airbyte) for review
- Consult Kyle (GrowthX) re: agentic content engagement tactics to improve performance
- Compress agentic cover images to reduce KB/MB size and improve load times

**Tanmay Sarkar (Airbyte)**
- Send connectors page Figma design to Erik (GrowthX)
- Show connectors page template in internal call next week; then start Webflow build
- Share agentic topics/competitors/prompts with Erik (GrowthX); Erik will then set up CheckThat.ai account

---

## Transcript

**Nithin:** This meeting is being recorded.

**Erik O'Brien:** All right, just quick updates today with some discussion items.

**Erik O'Brien:** So production updates: we did get five agentic articles reviewed and published. We went back and added all the TLDRs to those 25 that were already published, so we should be good to go moving forward. And then six DER articles reviewed and published. We've also got one thought leadership piece: "Agentic data infrastructure must be open," which just got final approval from Mario. And "Replication is the key for scaling agents"—we should have that over to you today for review, Kushal.

**Kushal Chatterjee:** Sounds good.

**Erik O'Brien:** For the TLDR refreshes, we hit about 75 this week, so we're going to continue pumping through those for the historical data engineering resources as we remove the AI summaries. We'll have Joe work through that list and try to get that done in the next couple of months.

**Nithin:** Can you just mark on the sheet where the topics you're going to finish? After that, I'll take care of the remaining articles.

**Erik O'Brien:** Okay, will do.

**Erik O'Brien:** So for agent use cases, Tanmay, it sounds like we're pausing completely on that for now and just going to refocus efforts on these connectors pages.

**Tanmay Sarkar:** Yes, that's true. I can send you the Figma design. These pages should be very technical, right? If you look at our current connectors for the replication product, those aren't technical. But for this new product, we want these pages to be very technical. So we're starting with connectors pages because we currently have that content already on GitHub and Docs, so it'll be easier to populate the content and code. Once we have more and more connectors, it will auto-populate those pages in Webflow. I'm currently working with Webflow to figure out how to automate the JSON code snippets directly from GitHub.

**Erik O'Brien:** And so your team will be taking care of those pages and publishing them?

**Tanmay Sarkar:** Yeah, mostly. We just have to automate it from GitHub. If we need any help, we can let you know and you can talk to your engineering team.

**Erik O'Brien:** Sounds like a plan. Do we have an idea of when those might go live or at least start to go live?

**Tanmay Sarkar:** I'll have the template ready. I'll showcase it in our internal call next week. Then once I get approval, we'll start building. The initial process might take a bit of time because of the technicalities—you need Webflow API keys and all that to set up everything. But once that process is live and running, it will be much easier to build connectors directly from the GitHub repo.

**Erik O'Brien:** So a few weeks out before those start to populate.

**Tanmay Sarkar:** Yeah, kind of.

**Erik O'Brien:** The other dependency before we started on the agent use cases was the platform page. When do we think that might be ready?

**Tanmay Sarkar:** Are you talking about the new product platform?

**Kushal Chatterjee:** The official launch is going to be in May. But there will be a public beta available probably around late February, so people will be able to access it and start using it then.

**Erik O'Brien:** And we're saying before we would launch any of the agent use cases, we would want that launch to go live?

**Kushal Chatterjee:** No, actually we could probably start doing the use case pages before that. The public beta is already going to be up, and a lot of these agents and connectors will already be up. We're bringing on the first few users in the private beta this week, so I would start working on these sooner. Around the time the public beta launch in late February, we'd want to have some of these pages up for people to start using with the public beta.

**Erik O'Brien:** Given the amount of time it takes to get these PSEO projects up and running, I think we want to continue to move forward on the agent use cases—at least get the wireframe up and running, get that approved by you guys, work through any copy issues, and have a pretty solid foundation ready.

**Tanmay Sarkar:** I'll give you a heads up a month before we can start the engineering process. That will probably take you two or three weeks to set up everything for use case files. We've got over 100 agent use cases. We can set a goal like 20 use cases every week, and we can reach that goal very easily in one or one and a half months.

**Erik O'Brien:** I want to make sure we give our engineering team enough time ahead. In the short term, it might make sense to keep pushing on the wireframe and template in Webflow. Then whenever we have that one-month heads-up, we can get the engineering team started using that template to make sure everything's ready.

**Tanmay Sarkar:** Makes sense. I'd rather keep pushing on the design portion to make sure we get that locked in before we push it to engineering.

**Erik O'Brien:** All right. So for timing of launches, it sounds like we have a private beta next week, public beta in late February. Any other milestones?

**Kushal Chatterjee:** Private beta is actually going live next week around Tuesday. We'll be reaching out to customers directly—no major public announcements or marketing around it. The public beta will go live in late February, and the official launch, we're aiming for May.

**Erik O'Brien:** Got it. Those are a few milestones for us to keep in mind while we're thinking about content and where we might want to accelerate. For conversion tracking, I wanted to get a bit more information on how you guys are tracking the "Talk to Sales" form and other CTAs in the content.

**Tanmay Sarkar:** So currently we have a Hockey Stack dashboard that shows users/visitors and "Talk to Sales" leads and whether they're moving down the funnel. But the issue is we don't have two different forms on the website. We created a "Join Private Beta" form on a third-party platform, but we're also using our "Talk to Sales" form on Webflow. We added a dropdown—"What product are you interested in?" with an option "Airbyte for AI Agents." If people click that and reach out, we know they want to talk about AI agents. But the issue is even if people visit the agentic pages and fill out the form, it shows as one lead because we're using one form. We're only using first-touch attribution for now because multi-touch would mix it with replication product data. I can share the data if you want.

**Erik O'Brien:** Yeah, as we start to ramp up this agentic content, one of the goals from sprint kickoff was to 3x the outreach to "Talk to Sales." What metrics should we be tracking?

**Tanmay Sarkar:** We should track this in Scrunch, but I know we're moving away from Scrunch anyway.

**Erik O'Brien:** Yeah, we're actually launching our own proprietary platform similar to Scrunch called CheckThat.ai, just for prompt tracking—similar to Profound and Scrunch. We're probably a couple of weeks from official launch. We're getting your account transferred from Scrunch to CheckThat. I just got access a couple of days ago. We'll set up your space with new agentic topics and prompts, and then hopefully in two weeks—the week of the 26th—we can start granting you guys access so you have full control.

**Tanmay Sarkar:** When do you guys plan to launch Atlas for the public beta?

**Erik O'Brien:** We had it on the roadmap for Q1, but we got an update this week that it's probably going to be later Q1, which is probably Q2. It's been almost a year since they started building it. We're getting to the point where you don't need internal knowledge to use the platform—it'll be pretty self-serve. We've got a couple more engineering sprints to go, but I want to have you guys as a design partner for CheckThat. Getting you guys access early so you can give us feedback on what's working versus what features are missing compared to Profound. You'd be an early customer guiding the roadmap for features we should add. We want to get you guys access as quickly as possible so you can start playing around and giving us feedback.

**Tanmay Sarkar:** That makes sense.

**Erik O'Brien:** I want to share a quick snapshot of our analytics performance. Coming into the new year, we had a pretty good week—250 sessions, which is 6x from December. "Context Engineering for AI Agents" and "Building Production AI Agents Cohort" are driving about half the sessions. We're continuing to double down on those to drive more sessions.

**Tanmay Sarkar:** Which data is that from?

**Erik O'Brien:** This is from the Looker dashboard. I've updated it to track agentic content instead of data engineering resources.

**Tanmay Sarkar:** Is it the one with overall band, conversion events, cohorts?

**Erik O'Brien:** Yeah, this one. You have only AI agents data now, not the replication product.

**Tanmay Sarkar:** Or do you have both?

**Erik O'Brien:** I switched it to just agentic, but we can switch it back or add filters to look at both if we want. Since we're focusing mostly on agentic, I kept it there. We're pulling data from GA4, which shows organic referrals, email, PPC, and CPC. You can filter out what you don't want to see.

**Tanmay Sarkar:** With time it will grow. We just have to produce more and capture that demand. It'll be compounding.

**Erik O'Brien:** For one and a half months in, this is pretty good signals. We're capturing keyword and intent. One thing I'm going to check with Kyle and the team is what we can do to boost engagement. It's not emergency-low, but it's lower than I'd like. I want to get input on tactics or strategies to improve engagement—maybe more visuals.

**Tanmay Sarkar:** Yeah. Once we stop replication articles and produce more of these new product articles, it will be faster and we'll capture more demand. And once we launch those use case pages—we've seen those have really good volumes—we'll capture that demand and pull traffic to the website.

**Erik O'Brien:** Absolutely. Anything else top of mind?

**Nithin:** Yeah, Rick. One small thing. The cover images you post for agentic content are too large—almost 3 MB per image. It's taking a load on the website.

**Erik O'Brien:** Got it. I'll compress them.

**Tanmay Sarkar:** When loading larger images through CDN in Webflow, it also consumes overall bandwidth and multiplies each time. You should shrink the size.

**Erik O'Brien:** Yeah, definitely. That's a quick to-do for myself.

**Erik O'Brien:** Anything else as we wrap up?

**Tanmay Sarkar:** No, I think we're good.

**Kushal Chatterjee:** The content's been great on both sides. Great job, guys.

**Erik O'Brien:** Well, thanks for the time, as always. Have a great weekend, and I'll talk to you guys next week.

**Kushal Chatterjee:** Sounds good.

**Tanmay Sarkar:** You too. Thanks.

**Erik O'Brien:** Bye-bye.
