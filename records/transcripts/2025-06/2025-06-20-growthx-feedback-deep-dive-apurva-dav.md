# GrowthX Feedback Deep Dive (Apurva Davé)

<metadata>
date: 2025-06-20
time: 16:41 UTC
duration: 19 minutes
organizer: Marcel Santilli
participants: Marcel Santilli, Apurva Davé, Andi Bailey
fathom_recording_id: 69656405
fathom_url: https://fathom.video/calls/331284324
share_url: https://fathom.video/share/9WGGG9Bb4reaWiHuPc5-HaosCfz4XSbA
source: fathom
enriched_on: 2026-03-03 18:45 UTC
</metadata>

---

## Summary

Marcel and Apurva conducted a feedback deep dive on GrowthX's content strategy for Aembit, discussing the tension between content velocity (2 published in 6 weeks, 4 pending, goal 6-8/week) and technical accuracy (currently ~50% valid). The team introduced GrowthX's new platform with fact-checking, AI editor, and workflow capabilities to address quality concerns. Key insight: GrowthX excels at broad conceptual content but struggles with deep technical implementation; Apurva suggested infusing content with Aembit's perspective through sales call transcripts and voice notes. Marcel committed to a deeper 1-hour strategy session with Apurva and the team to rethink the approach without losing momentum.

---

## Context

Aembit is a security/secrets management company where Apurva Davé (product/marketing leader) has been an advisor. GrowthX has been engaged on content marketing to build topical authority and drive traffic, but the engagement has struggled with the core tension in technical B2B content: balancing broad appeal with deep accuracy. The six-week engagement has produced only 2 published articles—below expected velocity for a $200k+ engagement—though 4 more are pending. Apurva's feedback has been notably professional and constructive (compared to other clients), but pointed: the content feels generic, lacks Aembit's perspective, and often gets the technical details wrong. Marcel had previously worked in the secrets management space (at Vault, then HB Software access management) and has relevant domain expertise, which positioned him to drive the strategic reset.

---

## Relevance

**To GrowthX Delivery:**
- Current content output (2 published, 4 pending in 6 weeks) falls short of expected velocity for the engagement size; goal of 6-8 articles/week appears misaligned with current quality baseline (~50% technical accuracy)
- GrowthX's strength is conceptual/topical authority content (e.g., D-Graph's "depth first vs. breadth first search" article still ranking #1 a year later) rather than deep technical how-to; need to anchor Aembit strategy in this strength
- New platform capabilities (fact-checking staff, AI editor, dynamic artifact/context pulling, workflow-in-code) directly address Aembit's accuracy concerns and offer competitive advantage in client demos
- Client voice/perspective is critical unlock: infusing 5-minute voice notes or sales call context into workflows immediately elevates content from generic to authentic; suggested access to Aembit's recorded sales calls could feed this
- Technical accuracy on secrets management will require pairing GrowthX's process with Aembit domain expertise; Marcel's background (Vault era) and team expertise (Clint, sixth hire at HashiCorp) are credibility builders

**To GrowthX Business Development:**
- Aembit appears healthy and committed ("still very excited to work with you") despite criticism, indicating expansion potential if velocity/quality issues resolve
- Constructive feedback signal: Apurva's tone suggests refinement, not disengagement; opportunity to demonstrate learnings quickly
- New platform demo positioned as differentiator; Apurva's enthusiasm ("This is awesome") suggests Aembit could become reference customer for platform capabilities

**To CheckThat:**
- No direct mention, though fact-checking staff capability touched on (validation of claims against domain-specific sources, whitelisting/blacklisting, confidence scoring) could inform AI visibility/validation workflows

---

## Overview

- Content velocity is improving (2 published → 4 more pending), but technical accuracy remains a challenge (50% valid)
- Need to balance broad topics (where GrowthX excels) with deep technical content (where improvement is needed)
- Implementing client's perspective/voice crucial for less generic content
- New GrowthX platform features (fact-checking, AI editor) show promise for addressing issues

---

## Key Topics

### Content Velocity and Quality

  - Progress: 2 published articles in 6 weeks → 4 more pending publication
  - Goal: 6-8 articles/week (currently seems far off)
  - Issues:
      - Classic AI problems with content
      - Technical validity at \~50%
      - Concerns about scaling while maintaining quality

### Technical Depth and Accuracy

  - Example: Spiffy (open-source project) article
      - Initial draft rejected outright
      - New workflow developed, resulting in much more technical content
  - Challenge: Achieving technical accuracy for code snippets and usage instructions
  - Solution: Focus on concepts behind concepts (e.g., knowledge graph for D-Graph) to build topical authority

### Content Perspective and Uniqueness

  - Feedback: Content feels generic, lacks point of view
  - Suggestion: Incorporate client's perspective (e.g., 5-minute voice notes on topics)
  - Potential resource: Access to Aembit's recorded sales calls for authentic voice/angle

### GrowthX Platform Showcase

  - New platform launch with integrated workflows
  - Features:
      - Artifacts: Templates, guidelines, personas dynamically pulled into workflows
      - Pipelines: Multi-step content generation process
      - Fact-checking staff: Verifies content against multiple sources, including client's domain
      - AI Editor: Allows for quick adjustments (e.g., brand alignment)
      - Expert hub (in development)

---

## Action Items

**Marcel Santilli (GrowthX)**
- Schedule 1-hour deep dive meeting with Apurva and team to rethink content approach and review account strategy

**Apurva Davé (Aembit)**
- Arrange access to Aembit's recorded sales calls for GrowthX team and determine format needed

---

## Transcript

**Marcel Santilli:** Another company just a few days ago, and literally, someone said the same exact thing, almost. Her words were like, "Can you just be more opinionated and more forceful?"

**Marcel Santilli:** Push harder. That's super, and I think this goes back to the same thing, right? I've been a CMO, and I know where I would have been comfortable being pushed.

**Marcel Santilli:** I'm comfortable pushing you at certain calls, right?

**Marcel Santilli:** Whereas if someone has never reported to a CEO, it's really hard to be pushing, because the only way you're successful and don't get fired reporting to a CEO is if you're pushing enough, right?

**Apurva Davé:** But not too pushy, you know? You got to hit that limit, because if you're not pushy, you're not doing your job. I mean, that's why you're so good at what you do, right?

**Marcel Santilli:** Yeah, it's knowing when to push and when to say, okay, got it, let's go do it.

**Apurva Davé:** And even when you bring somebody in for onboarding, it could be that person's job to set that tone a little bit because they're not responsible for the week-to-week after that. They set the tone and then they can move away from it. So it seems like you might be headed in the right direction.

**Marcel Santilli:** Let me move on to a few other topics.

**Apurva Davé:** Pro is I already see that you're going to up our content velocity. As I mentioned, we're at two published articles in six weeks. I think we're way behind where you would expect a client to be. We're about to potentially publish four more, so getting better. There's no way I would have gotten to this volume just doing what I was doing before. Once we get a little bit better at this, we're going to hit that velocity. Now, the team is talking about getting to six to eight articles a week. On the flip side, that seems very far off due to the quality of the content itself.

**Apurva Davé:** This may be a general issue with your clients, but what I see is classic AI problems with content, and then some specific to us. Technically, I think the content is maybe 50% technically valid. We have a lot of times where it's just plain wrong. Your team has been responding to that. We've picked a couple of places that are super deep and super technical that we're going to try and solve, but it concerns me about really hitting the scale numbers we were talking about.

**Marcel Santilli:** Can you dig in on that really quickly? So two vectors here: AI problems and technical accuracy or depth?

**Apurva Davé:** I think it's both. For example, there's this open source project in our space called Spiffy. Your team had a first go at this article, and it was like, I rejected it outright. It was enough where your team said, "Okay, we have to go back to the drawing board." Out of that, your development team built a new flow, and now I've got a much more technical article. In fact, it's so technical that I can't even review it, which I think is a good thing. I have to get someone else because on the top level it smells right, but I can't actually assess the correctness because it's gone really deep.

**Apurva Davé:** There are a lot of these topics where we're going to go through this same cycle unless we do something differently. Where it's technical enough that you're not trying to tell someone what it is, you're trying to tell them how to use it. And you're trying to get them to a point where code snippets and things like that have to be dead-on accurate.

**Marcel Santilli:** Yeah, and I think the challenge here is picking the lanes where we can be successful early on. Let me give you an example. We were working with a company called D-Graph. I don't know if you're familiar with them.

**Apurva Davé:** Technically, I think I'm still in the books as an advisor to D-Graph. Do you work with Kevin?

**Marcel Santilli:** Pre-Kevin taking over? Okay, cool. So you're super familiar with them, right? We'd 10x'd their traffic. We're not working with them anymore because they focus on hyper mode now, but instead of doing code snippets, we said, let's understand what are the concepts behind the concepts of what you do. It was knowledge graph concepts. For instance, there's an article—if you search right now, "depth first versus breadth first search" is still the number one result a year later. It goes into how these are building blocks that we do really well with. But on top of that, it starts to build topical authority with the right building blocks that will lead to the how.

**Marcel Santilli:** But if you start with the how, you're kind of stuck because there's no way we can be better than you at how to use your own product.

**Apurva Davé:** So first of all, agreed. And in fact, if you go through our Slack channel, you'll see this discussion. I think you guys do better with broad topics than really deep topics, and that's fine. The top-level thing is give me traffic that's relevant to my space. If you came back and said, "Hey Apurva, forget about Spiffy. You need to talk about delivering certificates"—which is essentially what Spiffy does—if that's the topic behind the topic and that's going to deliver 10x more traffic to people who care about this space, done.

**Apurva Davé:** Now, I will keep pushing on technical content. Secrets managers, secrets vaults—that's a huge space, been around for a decade, and it's the legacy technology we replace. In that case, I do expect you to be good at that. When I read the content we've created, it talks about secrets managers the way they should work, not the way they actually work.

**Marcel Santilli:** Exactly. I would like to propose we do an hour deep dive with me and the team, where we'll go into your account and really make sure we're rethinking how we're approaching this in the right way, without losing momentum. Let the team keep executing in parallel, and pretty quickly we can say, okay, here's the new artifacts, the strategy, and everything else. I can spend an hour together with you and the team because I know this space. I was at Vault, then IBM doing access management for several years, then HB Software. I know the space not like you, but enough to understand where we got it wrong.

**Marcel Santilli:** By the way, the sixth hire at HashiCorp that built most of Terraform is now one of our principal engineers, Clint, at Thrifio.

**Apurva Davé:** Yeah, that's cool. But before we go, I wanted to say one other thing. One of the comments from my team members, particularly my technical marketer, is that the content still often feels generic, where it doesn't have a point of view. And I think that's something people have always associated with AI-generated content, because it's derivative in many ways. But I wanted to flag that for you. That's still an issue for us. Part of it might simply be the human layer—we should go in with our "so what," our interesting point of view, and then use the machine to get us there.

**Marcel Santilli:** You're spot on. I was just on a call with Andi before this with a company that's not as technical as yours, and they had similar feedback. They've been with us for nine months. Right now, LLM referrals drives the majority of their leads every day, and we've more than 10x their traffic. If you ask them three months in, their feedback was way rougher than what you're receiving. But one of the biggest unlocks was when they created five-minute voice notes on some topics about what their angle is. When we used that as context, it inserted their perspective. Even a document doesn't have that soul of like, if we have three minutes of your CEO talking about it, that little bit more nuance turns the corner. All the planning, all the research we do, has that architecture behind it of what the angle is.

**Marcel Santilli:** For instance, if I say, "How AI is impacting marketers," if we use any of our workloads, no matter how good we prompt, it's going to be garbage. I just wrote a five-minute voice note on my thoughts on that, and it is gold. I'm like two minutes away from hitting publish on this thing already.

**Apurva Davé:** Yeah, I got it. So we could do a couple of things. One, we should talk to the team on how we'd implement something like this. Two, I could probably get you guys access to all of our sales calls that we record through our sales tool. I should figure that out with your team and what format they want.

**Marcel Santilli:** Yeah, that's perfect. Andy, do you be okay starting our next call? I'll stay on for five more minutes if that's okay.

**Apurva Davé:** Okay. Bye, Andy.

**Marcel Santilli:** Okay, I did want to share with you because I'm just so excited about our platform, so you can understand how things work behind the scenes. We just launched our platform this week. All this underlying technology was already there, right? We were essentially triggering our workflows through an API and using another platform to interact, then copy and paste it in a Google Doc. Now it's all in one place.

**Marcel Santilli:** The way it works is we have our artifacts—these are your artifacts right now. There's a history of these artifacts over time, and we need to improve them. But the idea is these artifacts are dynamically pulled into the workflows. Think of these as templates, guidelines, personas, writing guidelines—everything you need. We also have a knowledge base. Then there's the pipeline, which is all in code. It's essentially a configuration file. When we're generating content for you, it's going through multiple different steps.

**Marcel Santilli:** All our workflows are in code, so we can run and change them a lot faster. The inputs grab all the context you need and dynamically pull the context from your instance. It's figuring out search results, keywords, intent—not just any intent, but intent within the context of your company and the personas you're going after.

**Marcel Santilli:** The really cool part is we have a fact-checking staff. It's not just fact-checking against the World Wide Web, but it can be pointed towards very specific things. It can blacklist or whitelist certain things. So it takes an article still in draft, breaks it down into chunks, extracts every passage, and goes passage by passage researching it through multiple APIs, looking at your own domain and verifying it with a confidence level on whether it's false or true. It's not just false or true delete, right? It's nuanced. For example, "The evidence states that while validating workflows, job identity is blah blah, but the evidence only supports a reduction, not elimination of secret distribution in storage." It's wrong not because it's completely wrong, but because you're misattributing things.

**Marcel Santilli:** And then it rewrites everything to fix those things. Then there's style adaptation, internal linking. But the really cool thing with the output is we have an AI Editor. You can essentially go in and say, "Brand rule, align with brand guidelines." These shortcuts take the entire context of the whole thing and re-trigger workflows. There's also an AI chat that editors can work with. What we're building separately is called an expert hub.

**Marcel Santilli:** Hey, I apologize. I've got a Gartner call now.

**Apurva Davé:** This is awesome. So just two things. One, we're still very excited to work with you, and we'll keep working hard with you. Two, let's do the deep dive—one hour with the team, and we'll go through that. Thank you so much.

**Marcel Santilli:** Thanks for having me.

**Apurva Davé:** Bye.
