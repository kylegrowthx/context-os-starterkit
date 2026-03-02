# Similarweb-GrowthX

<metadata>
date: 2026-01-15
time: 20:08 UTC
duration: 17 minutes
organizer: stevie@growthx.ai
participants:
  - name: Rob Reilly
    email: rob.reilly@similarweb.com
    company: Similarweb
  - name: Stevie Kim
    email: stevie@growthx.ai
    company: GrowthX
fathom_recording_id: 114701297
fathom_url: https://fathom.video/calls/534665351
share_url: https://fathom.video/share/w24K97Mf6mHqpviLmPa_iufLHuVyr2ZQ
source: fathom
enriched_on: 2026-02-28 14:30 UTC
</metadata>

---

## Summary

Stevie Kim (GrowthX) met with Rob Reilly (Similarweb) to explore a data partnership around Similarweb's AI prompt dataset—80M real user prompts/month globally, 8M US English/month. Similarweb offers two tiers: raw data ($7M+/year, 6-month implementation) or aggregated ($100k–$999k/year, faster legal approval). GrowthX must decide whether to augment or replace its current data, with C-suite approval required from both sides.

---

## Context

GrowthX is evaluating data partnerships to power its AI visibility product (CheckThat) and B2B content marketing services. The company currently has its own prompt collection efforts but at a much smaller scale. Similarweb's dataset represents a potential strategic asset—80M real user prompts monthly with coverage across ChatGPT (70%), Gemini, Perplexity, and Claude (in progress). This partnership discussion emerged as part of GrowthX's ongoing effort to enhance its AEO (AI Engine Optimization) capabilities and market research depth. Similarweb itself operates an AI product, so any licensing deal requires C-suite approval to ensure no competitive conflicts.

---

## Relevance

**Data & Content Strategy**
- Authentic real-user prompt data vs. API probing; directly supports AEO research and content strategy
- Volume scale (80M global, 8M US English) enables trend analysis for B2B clients
- Real typos and actual phrasing reveals true user intent—not guessed keywords

**Product Development**
- CheckThat AI visibility product could integrate aggregated prompt insights for deeper competitive analysis
- Augmentation path (vs. replacement) allows phased adoption without full tech overhaul
- Aggregated tier saves dev cycles and legal complexity vs. raw data modeling

**Business Model & Pricing**
- $100k–$999k/year aggregated pricing is within range for strategic data partnerships
- $7M+ raw data pricing highlights value—competitive risk premium reflects scarcity
- Custom engagement model (vs. API) aligns with GrowthX's enterprise B2B service approach

**Strategic Decision-Making**
- Augment current data: Lower cost, faster approval, complements existing collection
- Replace current data: Higher upfront cost but potentially deeper competitive insights
- C-suite approval gates on front-end vs. back-end use; front-end display of raw prompts unlikely approved due to privacy concerns

---

## Overview

- **Unique Data Asset:** Similarweb collects \~80M real user prompts/mo (8M US English) from a panel, providing authentic, un-guessed user intent.
- **Customizable Data:** The data is delivered via custom engagements, not a standard API, and can be raw or modeled to fit specific needs.
- **Pricing Tiers:** Raw data is $7M+/yr (due to competitive risk); aggregated data is $100k–$999k/yr, with price varying by scope.
- **Strategic Decision:** GrowthX must decide whether to augment its current data or replace it entirely, weighing the cost, implementation time, and legal complexity of each option.

---

## Key Topics

### Similarweb's AI Prompt Data

  - **Source:** Data is collected from a panel of real users, not via API probing.
  - **Volume:**
      - **Global:** \~80M prompts/mo (includes code blocks).
      - **US English:** \~8M prompts/mo (excludes code blocks).
  - **Engine Coverage:**
      - **Primary:** ChatGPT (\~70% of volume), Gemini.
      - **Other:** Perplexity.
      - **In Progress:** Claude.
      - **Not Covered:** Google AI Overviews (requires a dedicated client to fund the storage).

### Partnership Options & Pricing

  - **Custom Engagements:** Delivery is via custom data science projects, not a standard API.
  - **Pricing Tiers (per year):**
      - **Raw Data:** $7M+
          - **Rationale:** High price reflects the competitive risk of licensing raw data.
          - **Implementation:** Requires a \~6-month modeling cycle.
          - **Legal:** More complex to approve.
      - **Aggregated Data:** $100k–$999k
          - **Rationale:** Lower cost and faster time-to-market.
          - **Implementation:** Similarweb models the data, saving GrowthX dev cycles.
          - **Legal:** Simpler to approve (saves \~3 months).

### Licensing & Approval Process

  - **Requirement:** C-suite approval is mandatory due to Similarweb's own AI product.
  - **Key Approval Questions:**
      - **Use Case:** Augment current data vs. replace it?
      - **Delivery:** Raw vs. aggregated data?
      - **Integration:** Front-end (displaying prompts to users) vs. back-end?
          - **Note:** Front-end use of raw prompts is unlikely to be approved due to security and privacy concerns.

---

## Action Items

**Rob Reilly (Similarweb)**
- Email Stevie C-suite approval questions re: use case (augment vs. replace), front-end vs. back-end integration, raw vs. aggregated data preference, scope, and insights to extract

**Stevie Kim (GrowthX)**
- Email Rob C-suite approval info; brief CTO/CEO on partnership options, decide strategic approach (augment or replace), schedule follow-up call with Rob and Similarweb data expert

---

## Transcript

**Stevie Kim:** Here we go.

**Rob Reilly:** Sorry about that. I had to get in transit from the office back home. I appreciate the flexibility.

**Stevie Kim:** Yeah, no worries. How's the start of the new year for you?

**Rob Reilly:** Everything's changing in this space every 10 minutes. How's the week been?

**Stevie Kim:** So incredibly busy. It's nuts, but it's powerful. 100%. It's insane. Like, you can't keep up.

**Rob Reilly:** Yeah, and we're on the data side of it. Everyone else is changing objectives, and we have to change our products. Our products change slower because we're doing the underlying data that's powering the products.

**Stevie Kim:** Engineering can build a lot faster, which is great. But making decisions in real time is wild.

**Rob Reilly:** So that being said, thank you for signing the NDA. In addition to our typical clickstream data points, we have a set of prompt and response data, probably the largest in the world. We're sitting on about 80 million real user prompts and responses a month.

**Stevie Kim:** That's the unique part. A lot of people are doing just proxies through APIs and getting responses. It's guesswork. We don't know what people are actually searching for.

**Rob Reilly:** Exactly. We have the real user inputs, typos and all. If you're used to looking at keyword data, start looking at prompt data.

**Stevie Kim:** When I search myself, I catch myself analyzing what I just typed, and it's not what you would expect. Real people aren't going to get their prompts right.

**Rob Reilly:** We are the major player in the background of the AI visibility space. We don't market it because it's sensitive and competitive. But if you see all these tools spinning up, we're usually involved.

**Stevie Kim:** So what do you provide to data partners like us? Would it be the actual response data or aggregated metrics based on topic?

**Rob Reilly:** That's the beauty of having the raw data. What are you guys interested in? We can model this however you need. This is a custom data set—we have a data science team that manages it. We do charge a premium, though.

**Stevie Kim:** What was the estimate? You mentioned six figures.

**Rob Reilly:** Anything raw is going to be seven figures because of competitive risk. But aggregated is anywhere from $100k to $999k, depending on scope.

**Stevie Kim:** Okay. What AI engines do you support or have data for?

**Rob Reilly:** We have all the major ones. We don't have Sparky and Rufus yet—which itself is an insight that no one's using Sparky. We have ChatGPT, Gemini, Perplexity. We're working on Claude, though I don't think that's relevant for this use case.

**Stevie Kim:** Google AI Overviews are the ones everyone's asking about. Are you scraping those?

**Rob Reilly:** We could theoretically get AI Overviews, but no one's paid us to store that yet. It would be an enormous data storage task. We're looking at a sample of 1% to 3% of the digital population.

**Stevie Kim:** So how are you getting the data then?

**Rob Reilly:** For AI engines, we use the same methodology we use for ChatGPT. We can tell when an API is triggered, and we capture the user input. I have to be careful on the exact methodology because of competitive positioning.

**Stevie Kim:** That's tough. Everything is changing all the time. I can imagine your job is really difficult to stay on top of.

**Rob Reilly:** Even though we cover most engines, the volume is heavily ChatGPT and Gemini is picking up. But 70% of the usage is ChatGPT. So even though we have different engines, it's heavily ChatGPT skewed.

**Stevie Kim:** Yeah, that makes sense. So you have historical data and all these engines covered. What did you say about licensing?

**Rob Reilly:** With these type of deals, I have to get C-suite approval because we have an AI product ourselves. It's easier to do this via email, but I'm going to send you some key questions: How do you plan to incorporate this data, front-end or back-end? When I say front-end, do you plan to show raw prompts to your users? My C-suite is probably going to say no to that because of security concerns.

**Stevie Kim:** Right.

**Rob Reilly:** We're also going to get asked how you plan to use this and if you prefer raw or modeled data. Raw data is super powerful, but we can do the modeling for you and save you dev cycles and licensing costs. Most people opt for the modeled approach. With raw engagements, it usually takes a six-month implementation cycle to model the data correctly. That's my recommended approach, at least to start.

**Stevie Kim:** We're doing some of this on our own, but nothing like the actuals and nothing close to the scale you have. I'd have to think about whether it's a replacement for what we're doing or an augmentation. There's value in both.

**Rob Reilly:** From my experience, when we do aggregated, we can save about three months of legal cycle because lawyers struggle with raw data sometimes.

**Stevie Kim:** So we'd need to take this back to the CTO and CEO and figure out if we want to augment or completely replace. It's costly, and getting the right data is hard.

**Rob Reilly:** If you want to set up a follow-up call, I can bring on one of my counterparts. He's one of the experts in this space and can talk through the exact nuances of the data and how it can be modeled, whether in volume or shares.

**Stevie Kim:** Yeah, we're heads down on a couple of major projects right now. It might be a couple weeks, but I'll take this back to them. They have a board meeting next week, so depending on their schedules. I'll definitely get back to you, and email me those questions.

**Rob Reilly:** And just to share the correct numbers for your C-suite: 80 million prompts a month worldwide, all languages—some include code blocks. In US English, we're about 8 million a month, not including code blocks.

**Stevie Kim:** Okay, great. And you said 70% is ChatGPT.

**Rob Reilly:** Yes, we have other engines, but 70% of usage is ChatGPT. That's where our primary data collection is.

**Stevie Kim:** I think I have most of the information I need. Yeah, email me those questions. That would be helpful to prepare if we want another meeting.

**Rob Reilly:** And we totally understand these things don't happen overnight.

**Stevie Kim:** This usually takes quarters.

**Rob Reilly:** Yeah, for sure.

**Stevie Kim:** Prior to GrowthX, I worked on longer, year-long B2B enterprise engagements at DataRobot.

**Rob Reilly:** Is DataRobot a partner of ours?

**Stevie Kim:** I think they are, though they've changed since I left. They pivoted to the agentic side and away from AutoML. They're good partners—great at co-marketing.

**Rob Reilly:** Yeah, and just to be clear on those correct numbers for your C-suite.

**Stevie Kim:** All right. Well, thanks. I'll shoot you an email with the information I need for C-suite approval. Hopefully we can connect in the next few weeks.

**Rob Reilly:** Perfect. Thanks so much for your time, Stevie. I really appreciate it and look forward to reconnecting.

**Stevie Kim:** Thank you. Take care.
