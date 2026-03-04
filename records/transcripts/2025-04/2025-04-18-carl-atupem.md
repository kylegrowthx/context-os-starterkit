# Carl Atupem

<metadata>
date: 2025-04-18
time: 21:01 UTC
duration: 31 minutes
organizer: Daniel Lopes (daniel@growthxlabs.com)
participants: Carl Atupem (Bytebot), Daniel Lopes (GrowthX)
fathom_recording_id: 58132664
fathom_url: https://fathom.video/calls/279515627
share_url: https://fathom.video/share/y5Xq1tTySztSvqzY9aCyEqNLGrX96Dv1
source: fathom
enriched_on: 2026-03-04 12:45 UTC
</metadata>

---

## Summary

Carl Atupem (founder, Bytebot) and Daniel Lopes (GrowthX) explored a collaboration to deploy Bytebot's AI agent platform for automating GrowthX's repetitive workflow tasks. Carl pitched Bytebot as a "drop-in digital worker" solution that can handle browser automation, file system access, and tasks without API integrations. Daniel outlined GrowthX's pain points: SEMrush data extraction ($1000s/month in API costs), Placid template creation, CMS publishing across diverse client platforms, and LinkedIn competitor monitoring. They agreed to start with a 2-3 month proof-of-concept focused on cost reduction (targeting $500-1000/month vs. current $1000-2000 VA spend), with potential to unlock growth-enabling automations later.

---

## Context

Bytebot is an open-source container-based platform for deploying AI agents that can interact with computer interfaces (keyboard, mouse, screen). The company recently hit a soft-launch influx (2,015 to 500+ GitHub stars) and is stabilizing its core offering: a drop-in container deployable within enterprise infrastructure with minimal onboarding friction, similar to hiring a remote worker. GrowthX is a B2B content marketing agency with a hierarchical content delivery structure (Chief Content Officer → Directors → Editors → Content Managers), serving 40+ clients with diverse CMS setups and workflow requirements. Daniel leads GrowthX's platform and automation efforts. The two teams connected to explore whether Bytebot can solve GrowthX's automation bottlenecks—particularly tasks that are 95% automated but stuck on repetitive manual work.

---

## Relevance

- **To GrowthX Delivery:** Bytebot can replace or augment VA hiring (currently $1000-2000/month) for client-specific CMS publishing, infographic/chart creation via Placid templates, and SEMrush keyword competitor analysis. Proof-of-concept will target highest-impact, browser-based use cases (SEMrush extraction, LinkedIn competitor monitoring).
- **To GrowthX Business Development:** Potential to unlock revenue-increasing workflow enhancements (e.g., automated template generation, competitor intelligence feeds) that differentiate service delivery beyond cost reduction. Opens new capabilities for client workflows.
- **To GrowthX Operations:** Budget flexibility: proof-of-concept at $500-1000/month vs. current VA cost, with option to scale to additional use cases (Slack integration, Salesforce automation, email workflows) if initial pilots succeed.

---

## Overview

- Bytebot offers an open-source container-based solution for deploying AI agents that can interact with computer interfaces
- growthx.ai has numerous use cases for automating repetitive tasks, particularly in content marketing and competitor analysis
- Both parties agreed to explore a proof-of-concept project, starting with cost-reduction tasks before moving to growth-enabling solutions
- Potential budget for the solution ranges from $500-$1000/month, with higher value for revenue-increasing automations

---

## Key Topics

### Bytebot's Recent Developments

  - Soft launch led to surge in GitHub stars (2015 to 500+)
  - Updates include:
      - Platform builds for Arm64 and AMD
      - Fixing agent loop
      - Container images for easier deployment
      - Workings of an agent system

### Bytebot's Vision and Capabilities

  - Aim: Create a "drop-in digital worker" indistinguishable from a remote worker
  - Core container: OS + integrations for remote control
  - Agent setup: Core container + Bytebot agent implementation
  - Flexibility to tailor for specific use cases (e.g., HIPAA-compliant workflows)

### growthx.ai's Current Workflow and Challenges

  - Structure: Chief Content Officer → Directors → Editors → Content Managers
  - Many tasks require manual work due to API limitations or absence
  - Examples:
      - Publishing on client-specific CMS
      - Creating infographics and charts
      - Using Placid for asset creation (API limitations for template creation)
      - SEMrush data extraction (API costs vs. manual extraction)

### Potential Use Cases for Bytebot

  - Browser automation for tasks without API access
  - File system access for downloading and processing data
  - Competitor monitoring on platforms like LinkedIn
  - Template creation in design tools
  - SEMrush data extraction and processing

### Collaboration Strategy

  - Start with a proof-of-concept focused on cost reduction
  - 2-3 month timeline to build and refine agents for specific use cases
  - Minimal integration required initially, using shared credentials for testing
  - Regular demos and feedback sessions
  - Gradual progression to more complex, growth-enabling tasks

### Budget Considerations

  - Current spend on VAs: Approximately $1000-$2000/month
  - Potential budget for Bytebot solution: $500-$1000/month
  - Higher value placed on automations that enable new capabilities or increase revenue

---

## Action Items

- Daniel to discuss priorities with Marcel and the team
- Carl to send Slack invite for async communication
- Identify highest priority, browser-automation-based task for initial proof-of-concept
- Schedule follow-up early next week to check on progress
- Explore open-source Bytebot solution if time permits

---

## Transcript
**Carl Atupem:** The soft launch took off when someone retweeted our project. They tweeted about it and we got a huge influx—it went from 2,015 stars to 500+ stars in a short period of time. So we changed our landing page, got documentation up and running, and I'm getting all sorts of requests for low-hanging bug fixes. We made sure the platform builds for both Arm64 and AMD. We're fixing the agent loop, getting more tweaks, making incremental improvements. It's all compounding into a better experience for developers to spin up a quick container. Now we have container images, so you don't have to build it manually. We've got the workings of an agent system.

**Daniel Lopes:** I've followed the project, but I haven't kept up with all the changes.

**Carl Atupem:** The grand vision we have is a drop-in digital worker that's indistinguishable from a remote worker. These AI agents can connect to the keyboard, screen, and mouse—with enough intelligence, they're just like a remote worker. You can onboard them the same way you'd onboard a person, so you don't have to reinvent the wheel with new tools. We're building this with a core container—OS plus integrations to control it remotely—and an agent setup that combines the core container with our Bytebot agent implementation that runs an agent loop using Anthropic, OpenAI, or whatever model, with storage for tasks.

The idea is to partner with companies to take this starting point and tailor it for their specific use cases. For example, there's a healthcare company running HIPAA-compliant workflows. They can either build integrations with healthcare providers (massive HIPAA compliance undertaking) or bundle their logic with our container and have providers run it within their infrastructure.

**Daniel Lopes:** We're essentially a workflow company. We look at how people do their work and build systems around it. Our structure is Chief Content Officer overseeing directors, who manage managing editors, who oversee editors, who have content managers executing the work daily. A lot of our tasks require VAs. Publishing to client-specific CMSs is a huge pain point—every client builds their CMS differently with different object structures, so you can't integrate via API easily. We end up with people manually publishing and building integrations. Then there's multimedia—we use Placid for creating infographics and charts, but a lot of that has no API and we have people doing it by hand. We've gone 95% automated on many workflows, but we still need VAs for the repetitive final steps. It would be cool to have computer use handle that kind of work for us.

**Carl Atupem:** You could have an automation log in and work outside the API if the API surface is limited.

**Daniel Lopes:** I've got so many use cases like that. Another one is SEMrush. There are things through the UI that are part of your user team, but through the API it's $1 per call. We're doing thousands of comparisons for clients—we have 40 clients. We thought about building a Selenium integration instead of paying thousands for this. We go 95% automated and then the team does the creative work, but they still have to do laborious boring things, so we hire VAs. It's also a time sink for our managing admins to hire the right VA. We end up with full-time VAs just clicking buttons, but you can't give them CMS access for security reasons.

**Carl Atupem:** Instead of just doing grunt work, VAs should oversee a fleet of agents. The agents do the work, then the VA double-checks: "That looks good." Or they can teleport into the agent's VM and correct something. This is meta-learning where it gets better and better. The one thing I'll say is we're still early with computer use—some things are much more suited for it than others. If you give it an open-ended task like "Build a report on tariff prices," it's not a deep research tool, it goes to websites and clicks links but doesn't really understand. But if you give it a specific direct task like "Go to CNBC, read the top 10 articles and summarize each," it can do that very quickly.

**Daniel Lopes:** We're a workflow company, so we're good at breaking down narrow tasks. One thing we wanted to do is monitor competitors every day on LinkedIn—see what they're writing about. You can't do that with API, and we wanted that for our activity feeds. Following competitors, seeing announcements. We have all these tasks broken down that we wanted to do but can't.

**Carl Atupem:** The nice part is you have all the tools available. Most of the tasks you're describing are browser-based, so you could use pure browser automation, but some might need file system access or code writing. You want flexibility.

**Daniel Lopes:** For SEMrush, we'd need browser automation (click export button) and file system access. Keyword competitor analysis costs $1 per domain via API. We could do it for $1 and 100 comparisons per domain, but manually it's 50 domains for $500. The API doesn't make sense. We want to extract CSV, download it, and put it in Supabase or something we can consume through workflows.

**Carl Atupem:** Let me ask something. When you have a team of engineers building automations—I think it would be super beneficial if we could embed with your team. We pick one use case, build the agents end-to-end. Anywhere it gets stuck, we fix the agent loop, the context, the tool—keep iterating until it's really good for that use case. Then we build another one. If we get three or four use cases working well, we can talk about a deeper, more scalable setup. I think getting an immediate win without pulling heavy infrastructure is better—I'm sure you've built a whole infrastructure and tons to integrate, but if we could chop off one use case and get it working, that's valuable.

**Daniel Lopes:** Let me talk to Marcel and the team about priorities. The immediate ones were SEMrush and CMS stuff. There's a few others. Marcel runs workshops on marketing automation and AI—he had 200 people today. He's on top of things people want to do with Salesforce, interviewing folks, outbound with email, clicking around Salesforce. He has a bunch of ideas. I'm pretty sure SEMrush would be huge and probably not super hard—browser automation with quick file system access for downloading CSV. That would be huge for us. Right now I have a giant roadmap and eight engineers all onboarding this month. No bandwidth to try different things. Maybe I can think of something simple I could try, and if I have questions you guys can help.

**Carl Atupem:** You've got limited bandwidth and responsibilities. Here's what I'm thinking: proof-of-concept. Two, three months—we build stuff for you instead of needing access to all your internal systems. If there's a SEMrush account, share credentials with us and we build the whole thing without touching anything else. No onboarding, just building the agent. We meet asynchronously or weekly and I demo what we've got: "This is what we can do now, what other tasks would you like?" We define a real-world use case and get the agent to do it repeatedly and reliably.

**Daniel Lopes:** Let me think about the highest priority that humans are doing that isn't crazy amounts of work. Anything that's browser automation is somewhat simple. Maybe we can chat about it. I can add you to Slack or something. Sure, I can send you a Slack invite.

**Carl Atupem:** What's your budget for this type of tool? How painful is it? Is it nice-to-have with VAs doing it, or can it truly unlock and let you scale much faster?

**Daniel Lopes:** It really depends on the job to be done. If it's narrow things, the budget would be what we pay the VA. I actually have to check with the team because I'm not tracking this. But I'd assume we're paying $1000-2000/month at least. We have a handful of VAs across the team doing different things at different times. Anywhere between $500-1000/month even, or $10k a year easily. But if we can do things even VAs can't do, that would be mind-blowing. Creating templates where our system brainstorms the template ideas and your system just executes—that would be huge because it's revenue-increasing, not just cost-cutting.

**Carl Atupem:** So let's do the low-hanging fruit first. Get it working well, proof-of-concept around eliminating costs. After a couple months, move to higher priority—unlocking growth. Do it project by project. Once those things work, it's a no-brainer because everything adds to the bottom line.

**Daniel Lopes:** There's cost reduction and stuff we cannot do. Most social media doesn't have API access. If I could follow people on LinkedIn, see what they're posting, copy the text and put it in a table, that would be huge. I need to chat with the team—that's a priority. Some stuff we know is cost-cutting. Let me check with the team and follow up.

**Carl Atupem:** I'll follow up early next week.

**Daniel Lopes:** You're super busy, so async is better for me. I'm swamped with meetings and onboarding people.

**Carl Atupem:** That sounds good. I'll send Slack invites and we can chat there.

**Daniel Lopes:** Thanks for your time. You're building cool stuff. I'll play with the open-source solution too if I can find time.

**Carl Atupem:** The UI for the chat isn't quite there yet. We have a lead engineer focused on coding and structure, a lead designer, and some contract folks. Trying to run lean. The open-source approach lets people fork it and suggest changes. We already have commits making things better. AI code editors let us move at a much faster pace. Having LLM access is like having junior engineers with you.

**Daniel Lopes:** Our interview process is designed around hiring people with that mindset. There's a lot of resistance to it. I haven't touched it.

**Carl Atupem:** It's amazing. Hope you have a great rest of your day. Enjoy Friday. Have a great weekend.
