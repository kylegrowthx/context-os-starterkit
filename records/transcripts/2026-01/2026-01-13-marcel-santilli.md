# Marcel Santilli

<metadata>
date: 2026-01-13
time: 19:42 UTC
duration: 15 minutes
organizer: stevie@growthx.ai
participants: Marcel Santilli, Stevie Kim
fathom_recording_id: 113972948
fathom_url: https://fathom.video/calls/529338733
share_url: https://fathom.video/share/9LXtfaWo-ZhNMFgbCMT1e2MsiDE7MJs9
source: fathom
enriched_on: 2026-02-28T00:00:00 UTC
</metadata>

---

## Summary

Marcel and Stevie discuss Stevie's role as an orchestrator bringing order to CheckThat's chaotic, fast-moving environment while maintaining urgency around Q1 targets of 100 paying customers and $200k ARR. They establish that Stevie's job is to manage risk, enforce prioritization around PMF/GTM validation, and prevent missed decisions—not to slow down execution. Data vendor research (SimilarWeb, Bright Data) is secondary; it only proceeds if it doesn't delay the Q1 launch.

---

## Context

Stevie Kim joined GrowthX recently and is ramping on CheckThat, a B2B SaaS AI visibility index. Coming from slower-moving organizations (Human Signal used quarterly releases), Stevie is adjusting to continuous release cycles and the compressed decision-making required to hit PMF/GTM targets in Q1. The company is operating under a self-imposed urgency to validate that CheckThat can generate revenue through self-serve and organic paths—the only viable path to compete with well-funded alternatives like Profound (which spends $100M). Marcel frames this conversation to clarify Stevie's role: not to slow execution, but to bring clarity, manage risk, flag critical gaps, and ensure the team maintains relentless focus on PMF/GTM validation.

---

## Relevance

- **Role Clarity:** Defines Stevie's position as orchestrator and risk manager—essential for onboarding to a high-velocity startup.
- **PMF/GTM Strategy:** Articulates why speed and ruthless prioritization matter; establishes the bar for Q1 success (100 paying customers, $200k ARR).
- **Competitive Positioning:** Explains the business strategy: only self-serve and organic paths can compete with $100M+ funded rivals.
- **Decision-Making Norms:** Sets expectations on asynchronous decision-making risks and the importance of flagging missed context in Slack.
- **Data Strategy:** Evaluates vendor relationships (SimilarWeb, Bright Data) for cost, coverage, and competitive intelligence—secondary to Q1 launch.

---

## Overview

- **Stevie's Role:** Bring order to chaos by orchestrating teams, managing risk, and enforcing focus on the core goal: validating Product Market Fit (PMF) and Go-to-Market Fit (GTM).
- **Urgent Q1 Targets:** Achieve 100 paying customers and $200k ARR by quarter-end. This is a critical milestone; failure would force a major strategic pivot.
- **Data Vendor Research:** Continue evaluating vendors (e.g., SimilarWeb) for potential cost savings, data backfills, and competitive intelligence, but only if it doesn't delay the Q1 launch.
- **No Roadmap Before PMF:** The company's sole focus is achieving PMF. A multi-year roadmap is premature and will only be created once the business model is validated.

---

## Key Topics

### Challenge: Adapting to a High-Velocity Environment

  - Stevie is adapting to a continuous release cycle, a shift from slower quarterly releases at previous companies (e.g., Human Signal).
  - **Key Challenges:**
      - Avoiding assumptions; training to seek clarity even on seemingly obvious points.
      - Managing high randomization and context-switching.
      - Risk of errors from skimming documents or missing decisions made asynchronously in Slack.
      - **Example:** A task reassignment for the "AI overview" feature was decided in Slack, requiring Stevie to reassign it from Jose to Pedro and pull Pedro from the "citation" task.

### Solution: Stevie's Role as "Orchestrator"

  - Marcel defined Stevie's role as bringing order and clarity to the chaos, not slowing it down.
  - **Primary Responsibilities:**
      - Orchestrate communication between engineering, growth, and customer teams.
      - Manage risk by identifying and flagging critical issues.
      - Enforce focus on the core goal → validating PMF and GTM.
      - Proactively pull prioritization decisions from Marcel and Daniel.

### Rationale: The Urgency of PMF/GTM Validation

  - The company is operating with a "running out of cash" mindset to maintain urgency, though cash flow is not an immediate issue.
  - **Strategic Goal:** Validate PMF and GTM through self-serve and organic paths.
  - **Why:** This is the only way to compete with well-funded rivals (e.g., Profound's $100M spend).
  - **Q1 Targets:**
      - **100 paying customers**
      - **$200k ARR**
  - **Consequence of Failure:** A major strategic pivot would be required.
  - **Fiscal Year ARR Targets:**
      - **Low-end:** $2M
      - **High-end:** $6M–$7M

### Data Vendor Research: Status & Strategy

  - Research is ongoing; Stevie has POCs signed up with free credits.
  - **SimilarWeb:** Requires an NDA for a second call to discuss details.
  - **Bright Data:** Focused on web scraping, not historical panel data.
  - **Panel Data Overview:**
      - Collected from user behavior via browser extensions.
      - Provides "ground truth" data for ML model validation.
      - **SimilarWeb:** Offers aggregated, topic-level data (e.g., "Nike shoes"), not granular, per-prompt details.
  - **Strategic Value:**
      - **Cost Savings:** Potentially cheaper to buy historical data than collect it.
      - **Data Backfills:** Fill gaps in historical data.
      - **Competitive Intelligence:** Understand how rivals operate.
  - **Priority:** Continue research, but deprioritize if it delays the Q1 launch.

---

## Action Items

**Stevie Kim (GrowthX)**
- Sign SimilarWeb NDA and schedule 2nd call to discuss panel data, historical prompts, coverage, and costs
- Continue data vendor evaluation (SimilarWeb, Bright Data POCs) only if it does not delay Q1 launch
- Implement organizational systems (reminders, trackers) to avoid dropped tasks in high-velocity environment

---

## Transcript

**Stevie Kim:** It's been pretty chaotic. It's hard getting used to product being built in such a fast way. I worked on slower companies with quarterly releases, and Human Signal had continuous release for some parts and quarterly for on-prem. I'm just getting used to what it means to move so much faster with engineering and product capacity. I'm definitely used to having fully fleshed-out PRDs and all the milestones planned out, and now it's such a good learning experience. But it's a lot to ramp up on both the space and understanding how marketers will use the product. One of the hardest things has been not making assumptions based on previous experience or just what makes sense to me. I need to train myself to get clarity even if I think I know the answer. And then there's the typical engineering lead thing of getting randomized and pulled in many different directions. I'm making mistakes because I'm not reading messages fully or I'm skimming docs when I have 20 to read at any given time. I need to slow down to make sure I have the context and I'm not making assumptions. I'm trying to train myself to move fast but slow down where I'm making mistakes and keep on top of everything. Like the AI overview—it was assigned to Jose, Jose got put on onboarding, that decision happened in Slack, not in the meeting. So I'm trying to remember where all this information is and remember that I needed to reassign it to Pedro and pull him off citation. I've been trying to automate some of these things with reminders so I don't drop the ball.

**Marcel Santilli:** Your job is to bring order and clarity to the chaos, not necessarily slow it down, but rather make sure important things aren't being missed and people understand the context and prioritization. You're an orchestrator and traffic controller between me, Daniel, and the rest of the teams—engineering, growth, and delivery/customers. The thing is, we're trying to find product market fit and go-to-market fit. We're operating with a "running out of cash" mindset, though we're not actually. But we're not moving fast just for the sake of it. We're moving fast to validate things. Your job is to be the police of that. If we can't prove that this product can generate revenue on its own through self-serve and organic paths, there's truly no way we can compete with Profound spending $100 million. We have to play a different game and this has to work. We would have to pivot differently if it doesn't. Last week Jason was asking me about the product roadmap and I said, "What are you talking about? There is no roadmap." What seed-stage company has two years of roadmap? They have no product market fit. There is no roadmap until you get PMF. Your roadmap is: get PMF and get GTM. Proof that you can make this sustainable. Every day is about that. If we need to drop everything and do this, we do it. But there are critical things we might be missing. Your job is to get those inputs, have all the context, know where the risks are, and flag them. Make sure prioritizations are right. If we need input from me or Daniel on prioritization, pull it out of me in whatever way you can. The risk is a whole week where we didn't do something because we didn't know, or we didn't prioritize it because we didn't think it was relevant, or we decided to do something else but under-communicated it and it was hidden in some thread. Right now, a week is critical because we're halfway through the month. By the end of the month, we're one-third through the quarter. By the end of the quarter, we have to be at 100 paying customers and $200k ARR. If we're not, this has to be changed in a different way. It doesn't mean it will be shut down, but I think we have really good chances. You can see a world where we take six more weeks to polish the product before launch, zero revenue, and burn an extra $400k before we even validate that this can't get revenue. I'm working on a fiscal plan. High-end, we want $6-7M ARR. Low-end, at least $2M ARR this year. Let's race towards onboarding, monetization, figure out all those things, get it live, implement support and ticketing, then start to get feedback.

**Stevie Kim:** And then I'll push the growth team and keep a close eye on that. As far as prioritization, I wanted to ask about the data vendor. I had to pause that to do other work. I have some POCs to sign up. They'll give me free credits after the initial calls. SimilarWeb wants me to sign an NDA to have a second call to discuss panel data details. The last couple of days have been wild, but I plan to get back to them today. That's a chunk of time to use these products and do more discovery. I wanted to make sure that should still be on my plate.

**Marcel Santilli:** Yes, but if it's a decision between something that will delay launch and growing faster, don't prioritize it. If it's spending one more hour on planning versus this, that's a reasonable tradeoff. Every single player in the space seems to be buying data from providers. I have a feeling there's something big we're not doing. It doesn't feel like all these vendors are just going direct to OpenAI and buying from the API. Every player seems to be using something.

**Stevie Kim:** Yeah, there are a couple that have panel data and either use it as a benchmark or base their prompts off it. But it sounds like most people are doing what we're doing.

**Marcel Santilli:** That's the main thing. Getting cost and understanding the value of panel data—I don't fully understand it. From what I understand, panel data comes from Chrome extensions that monitor people's behavior and see exactly what they're typing in their prompts, where they go, how often they click, that kind of thing.

**Stevie Kim:** Yeah, exactly. You're getting the actuals. In machine learning, you always need the actuals—ground truth data to understand how accurate you're getting.

**Marcel Santilli:** But it's a subset of the actuals. What I don't understand is what data you have on who that user is to determine what kind of user they are.

**Stevie Kim:** SimilarWeb and Bright Data are different. Bright Data is scraping. SimilarWeb has demographic data for their panel, but it's private—we don't get access to it. They provide aggregated citations and mentions based on topic. For example, Nike shoes or Air Jordans as a topic cluster, then you get the aggregated data.

**Marcel Santilli:** So you don't get granular metadata per prompt. That's specifically SimilarWeb. They're all a little different. Some are used for trending and volume estimates, others for figuring out prompts. Are there any other use cases?

**Stevie Kim:** Is anyone selling historical prompt probes?

**Marcel Santilli:** Yeah, pretty much everybody except Bright Data because they're scraping. So they might have a library of probes they've had data on that we could buy for the last 30 days?

**Stevie Kim:** SimilarWeb has historical data. But Bright Data is more focused on scraping, so they're less on historical data.

**Marcel Santilli:** How much overlap is there for the kinds of prompts we care about?

**Stevie Kim:** I don't know because I haven't done that second call with SimilarWeb yet, after I signed the NDA.

**Marcel Santilli:** Okay. I've got to run—my in-person customer just came in. This has been super useful. Keep pushing. If there's a leverage point—cost savings, better data, data backfills, anything like that—that would be really good. Just understanding how they work, how they probe, cost per query. If they have historical data and it's cheaper than collecting it ourselves, it could actually save us money. Keep on it.

**Stevie Kim:** For sure.

**Marcel Santilli:** Thank you.
