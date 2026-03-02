# John Russell (Anthropic) <> Leo Steffen (GrowthX)

<metadata>
date: 2026-02-19
time: 21:59 UTC
duration: 26 minutes
organizer: leonardo@growthx.ai
participants: John Russell (Anthropic), Leonardo Carpenedo Steffen (GrowthX)
fathom_recording_id: 123901955
fathom_url: https://fathom.video/calls/571843281
share_url: https://fathom.video/share/rPbY8LRnjgozLXzwzzq5icLXFfd-zazr
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Leo Steffen (GrowthX) and John Russell (Anthropic) discussed GrowthX's scaling challenges with Claude 4.5 rate limits and explored solutions including migration to Anthropic's Enterprise plan ($20/seat annual, pay-as-you-go tokens) and a formal commercial agreement for reserved capacity and volume discounts. Both parties aligned on a two-way partnership where GrowthX provides model feedback on Sonnet 4.6 and other Claude versions in exchange for Anthropic's technical support to optimize Claude usage and unlock new workloads.

---

## Context

GrowthX is an AI-native company building production applications on Anthropic's Claude models. As a high-growth startup, GrowthX has become increasingly dependent on Claude for core product functionality and is now experiencing rate limit constraints on Claude 4.5 that threaten to block further scaling. John Russell recently joined Anthropic's startup partnership team after four years building Google Cloud's startup program and was reaching out to meet with GrowthX's leadership to discuss partnership opportunities and explore solutions. This meeting was initiated by GrowthX's need for predictable billing, higher rate limits, and a clear migration path from their current Teams plan to a more scalable offering.

---

## Relevance

### To GrowthX Business Development
- **Partnership Framework:** Secured alignment on a two-way partnership with Anthropic for technical support, model feedback, and potential volume discounts — critical for supporting GrowthX's AI-native product scaling.
- **Commercial Agreement Opportunity:** Formal commercial agreement pathway defined, requiring GrowthX to provide a 12-month consumption forecast by which Anthropic will create a proposal for reserved capacity and volume discounts.
- **Billing Predictability:** Monthly invoice billing (vs. credit card) and Enterprise plan migration will replace rigid usage caps with transparent, user-level cost visibility and per-seat pricing ($20 annual + token consumption).
- **Account Health Signal:** Leo's engagement and request for partnership opportunities indicates strong satisfaction with Anthropic and high likelihood of expansion.

### To GrowthX Delivery
- **Platform Optimization:** Anthropic committed to providing technical support (prompt engineering, context engineering) to help GrowthX optimize Claude usage and unlock new workloads where Claude excels (text generation, code tasks).
- **Model Feedback Opportunity:** GrowthX positioned to provide comparative feedback on Sonnet 4.6 and other models, leveraging GrowthX's position as an early adopter and power user.

### To CheckThat
- **Competitive Research:** GrowthX disclosed using multiple providers including OpenAI alongside Anthropic, providing valuable data on model performance comparisons that could inform CheckThat's AI visibility indexing.

---

## Overview

- **Scaling Bottlenecks:** GrowthX's rapid growth is hitting rate limits on Claude 4.5, creating unpredictable costs and scaling risks.
- **Enterprise Plan:** A migration to the Enterprise plan ($20/seat + pay-as-you-go tokens) was proposed to replace the current Teams plan, which has rigid usage caps.
- **Commercial Agreement:** A formal agreement is required to secure reserved capacity and volume discounts, contingent on GrowthX providing a 12-month consumption forecast.
- **Partnership:** GrowthX will provide model feedback (e.g., on Sonnet 4.6) in exchange for Anthropic's technical support to optimize Claude usage.

---

## Key Topics

### GrowthX's Scaling Challenges

  - **Problem:** GrowthX's rapid growth is hitting rate limits on Claude 4.5, creating unpredictable costs and scaling risks.
  - **Needs:**
      - Predictable billing (monthly invoicing).
      - Higher rate limits and credit reloads.
      - A clear, predictable migration path to an Enterprise plan.
  - **Context:** GrowthX is an AI-native company building production applications on Anthropic, making a stable, scalable partnership critical.

### Proposed Solution: Enterprise Plan Migration

  - **Proposal:** Migrate from the current Teams plan to the Enterprise plan.
  - **Rationale:** The Teams plan's rigid usage caps create overhead and are not suitable for high-growth companies.
  - **Enterprise Plan Details:**
      - **Cost:** $20/seat (annual plan), comparable to Teams.
      - **Usage:** Pay-as-you-go for tokens at standard API rates.
      - **Benefits:**
          - **Predictability:** Replaces usage caps with a transparent, pay-as-you-go model.
          - **Control:** Provides user-level cost visibility and the ability to set individual or group usage caps.
          - **Upgrade Path:** A true upgrade; no user experience or limit downgrades.
  - **Action:** John will research the migration process and address a specific question from Yusef about user tiers.

### Long-Term Solution: Commercial Agreement

  - **Purpose:** Secure reserved capacity and volume discounts for GrowthX's long-term growth.
  - **Requirement:** A formal commercial agreement, which requires a 12-month consumption forecast from GrowthX.
  - **Process:**
    1.  GrowthX provides a 12-month consumption forecast.
    2.  Anthropic uses the forecast to create a formal proposal.

### Partnership & Feedback Loop

  - **Goal:** Establish a two-way partnership for mutual benefit.
  - **GrowthX's Contribution:** Provide feedback on Claude's performance (e.g., Sonnet 4.6) and comparative data against other providers.
  - **Anthropic's Contribution:** Offer technical support (e.g., prompt engineering) to help GrowthX optimize Claude usage and win new workloads.

---

## Action Items

**John Russell (Anthropic)**
- Research and share monthly invoice billing process steps with GrowthX via Slack
- Research and share Teams-to-Enterprise migration steps and address Yusef's question about user tier downgrades in the shared Slack channel
- Post Slack summary of meeting outcomes in GrowthX channel

**Leonardo Carpenedo Steffen (GrowthX)**
- Provide 12-month consumption forecast to John for Anthropic's commercial agreement proposal
- Gather and share model feedback from GrowthX team, especially on Sonnet 4.6 performance
- Share meeting recording and notes with John via Slack

---

## Transcript

**John Russell:** Hello?

**John Russell:** Hey, Leo, I think you're muted.

**Leonardo Carpenedo Steffen:** There you go. Wait, is it my connection that's cutting out?

**John Russell:** I don't know. It's a little choppy on my end, too, but I can hear you now.

**Leonardo Carpenedo Steffen:** Can you hear me? Yeah, good.

**John Russell:** Okay.

**Leonardo Carpenedo Steffen:** How are you doing today?

**John Russell:** Good, good. Nice to meet you. How are you doing?

**Leonardo Carpenedo Steffen:** Let's see if it's you or me. Maybe I'm going to move my laptop.

**John Russell:** I'm getting closer to my router. It's better for me right now.

**Leonardo Carpenedo Steffen:** Good. Let me just pull. Okay, how's this?

**John Russell:** Okay.

**Leonardo Carpenedo Steffen:** Yeah, cool.

**Leonardo Carpenedo Steffen:** Let me just find my notes here. I have a few things. Information on new customer programs and increasing usage.

**John Russell:** Let me introduce myself properly. I know you were working with my colleague Sophie. I just joined Anthropic a month ago, but I'm pretty deeply embedded in the startup community. I was at Google Cloud for four years working on our startup program, working with pre-seed through Series C companies helping them build on Google Cloud. Now I'm at Anthropic doing very similar work, but focusing entirely on AI natives. I've spent the first couple months here getting up to speed and meeting customers I'll be working with. I'm really excited to meet you and learn what you guys are working on at GrowthX. I'd love to spend this time getting to know your business better and share some of the new programs we're rolling out for our startup segment. Anything top of mind for you?

**Leonardo Carpenedo Steffen:** I didn't come with a lot of information today, but I have a presentation on something we've been discussing. We have early access programs and have been getting beta access to Claude 4.5 for a while. We're looking for partnerships and credit programs or benefits because we're growing a lot. We're a high-growth company using a lot of Claude for everything. We've been early adopters. We need credit reloads and higher rate limits due to constraints on Claude 4.5, potentially on other models as well. The team has also asked about a Teams or Enterprise migration path, so clarity on the plan and predictable scaling. We need to know we won't hit walls as we grow. We've had to change everything because of constraints that don't let us scale. We're AI native so we move fast, and we're building production applications on Anthropic. There's real value that you bring to us and we bring to you as well.

**John Russell:** That sounds like what I'm hearing is typical high-growth challenges. You're scaling fast and need our help with more predictable billing, pricing and volume benefits, and capacity for growth. All very doable things. We can definitely move you to monthly invoice billing instead of credit card. This will be my first time doing this at Anthropic, so let me get back to you on the exact steps. I'll take that on as homework. Are you currently on a Teams plan and looking to upgrade to our Enterprise plan?

**Leonardo Carpenedo Steffen:** Yeah, I believe so. I have a note here. Yusef asked Sophie about this: when we migrate Teams to Enterprise plans, some of our folks are on a higher tier personal plans. Would they be downgraded?

**John Russell:** Tag me in the channel and I'll wait to see it come through. Let me get back to you about the migration details. I'm not sure about Yusef's question specifically, but as far as migration from Teams to Enterprise, it's always going to be an upgrade. There's never going to be a downgrade in terms of user experience or user limits. The main difference between Teams and Enterprise is how we handle usage. Teams seats have a standard usage limit. If you hit that limit, you wait for it to reset or purchase additional usage. Enterprise is the way to go. We've greatly simplified Enterprise pricing: it's $20 per seat annually, comparable to Teams, and then you pay for all your user tokens at the same rate as our API. For 95% or more of your users, token costs will be minimal, around $5 or less per month. For power users and developers, you may see savings or an increase depending on their usage. If they're extreme power users hitting their Teams caps consistently, they'll probably cost more because they're using so many tokens. The benefit is you get visibility into exactly how much each user is spending at the user level, and you can set user caps at the individual seat level or group level. It's a better pricing model because Cloud Code users hitting caps creates organizational overhead. With Enterprise, you pay as you go. Does that answer your question about Teams versus Enterprise?

**Leonardo Carpenedo Steffen:** Yeah, it does. But you're going to give me more details on this, right?

**John Russell:** Yeah, if you're on Teams and want to upgrade, I need to figure out the exact steps, but I think you can essentially cancel your plan early and upgrade to Enterprise. That's the path you want to go, and we can outline the steps.

**Leonardo Carpenedo Steffen:** So that's going to give us more volume? It's going to be the same cost or maybe a little more. Is that what I'm hearing?

**John Russell:** Yeah. When we think about rapid scaling, there's capacity limits — that's rate limits — and then pricing discounts, volume discounts. They go hand in hand. You're at a point where your growth and volume are so significant that we want to reserve capacity for your business to future-proof your growth trajectory. For volume discounts, since you're becoming one of our larger customers, the framework is a commercial commitment, a commercial agreement with us. I can pull together a proposal, but what would really help is for you to give me a sense of what you're expecting for growth this year. Where do you see yourself landing in terms of overall Claude consumption for the next 6-12 months?

**Leonardo Carpenedo Steffen:** Can I give you that information later? I want to double-check and gather data to confirm I can send it over and you come up with a plan.

**John Russell:** Yes, you can come back to me. You don't have to do it right now. Just give me a forecast and I can create a proposal. Are you interested in us working as committed customers where we can get deeper on these things?

**Leonardo Carpenedo Steffen:** Yeah, definitely. I had on my list that I wanted to ask if you had technical partnership opportunities and feedback loops. We've been growing rapidly and will scale, so we can provide good feedback. We're engaged in data and features, building production applications on Anthropic. There's real customer value. Our team moves pretty fast. We're early adopters, so new features are quick to launch. We do use other providers, including OpenAI. I don't know how much I can disclose right now, but I can bring data later at another point. We can schedule another call.

**John Russell:** Yeah, definitely. Companies like yours are always on the frontier testing models. We're asking from a place of wanting to know where Claude is doing well and where it's doing less well. That feedback helps us train the next generation of models. For instance, multimodality is an area where other models are doing better. But where we can win is in text generation where Claude is generally strong. That's where we could bring in our Claude AI team to help with prompt engineering, context engineering, or dig deeper to fully unlock Claude's capabilities.

**Leonardo Carpenedo Steffen:** Yeah, that's one of the things we could partner on. I'm personally involved in tracking how much money we spend on providers, and your dashboard is one of my favorites. It's complete enough for me to see the information I want. I've been using Pods for your chat.

**Leonardo Carpenedo Steffen:** But I'll see what more information I can bring to you, as long as it's going to help with what we're trying to.

**Leonardo Carpenedo Steffen:** And I guess we've already been in feedback loops, so I don't think there's going to be any problem in sharing more info with you.

**John Russell:** Okay.

**John Russell:** But the idea is to make this as something that's good for us and good for you as well, right?

**Leonardo Carpenedo Steffen:** We want growing customers, and we want to scale fast.

**Leonardo Carpenedo Steffen:** So...

**Leonardo Carpenedo Steffen:** We need a partner of this, is there to support us and not just drag us down every time we need something.

**John Russell:** Yeah, absolutely.

**John Russell:** Okay, well, Leo, think it sounds like we have a few things.

**John Russell:** I'm going to follow up with you on invoice billing and the steps to upgrade to enterprise if you want to do that.

**John Russell:** But from your side, would love to just, if there's any feedback from the team on Claude, especially the newest models, like if you have feedback from the field or your teams about Sonnet 4.6, for instance, always collecting that right now.

**John Russell:** And then send me your forecast for your consumption for the next year, and I can spin up a proposal for a commercial agreement.

**Leonardo Carpenedo Steffen:** Feedback for the models?

**Leonardo Carpenedo Steffen:** I'm going to look for that data. So just to make it clear, what we really need is first a good partnership where we can toss ideas back and forth, billing predictability, and rate limits. That's how we're going to scale. I will fetch the data you asked me for. I'm going to send you a summary later and we can keep in touch in Slack. I may or may not reply right away, but Daniel is good at keeping track of everything. Anything else I didn't tell you?

**John Russell:** No, I think that's it. I'll send my notes in Slack and send a summary of what we talked about so we can keep it all there.

**Leonardo Carpenedo Steffen:** Yeah, right. I've recorded this meeting and I'm going to share it with you. I have notes as well that I'll share later. I'm going out for dinner now but will keep working later.

**John Russell:** Awesome. Slack is great. I'm always there.

**Leonardo Carpenedo Steffen:** Thanks for your time.

**John Russell:** Nice to meet you. We'll talk soon. Take care.

**Leonardo Carpenedo Steffen:** All right, see you later. Take care.
