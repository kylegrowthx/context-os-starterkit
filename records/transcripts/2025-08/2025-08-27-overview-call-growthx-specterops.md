# Overview Call — GrowthX & SpecterOps

<metadata>
date: 2025-08-27
time: 20:01 UTC
duration: 30 minutes
organizer: tyler@growthx.ai
participants: Marcel Santilli, Tyler Pavlas, Ric Nguyen, Bryce Hein, Meshach Cisero
fathom_recording_id: 83397621
fathom_url: https://fathom.video/calls/391542863
share_url: https://fathom.video/share/AkXXeKYAzYuFsmqDG95bVYsAjUqxMLYH
source: fathom
enriched_on: 2026-03-03 16:45 UTC
</metadata>

---

## Summary

GrowthX and SpecterOps explored a partnership to help SpecterOps scale AI-assisted content production while maintaining technical credibility in red teaming and offensive security. Marcel detailed GrowthX's approach of building AI agents guided by deep domain expertise and fact-checking systems, emphasizing the need to target not just practitioners but also identity/IAM teams and CISOs as decision-makers. The team proposed an 8-week strategy and execution sprint to prove value, including 4-6 deep dives with SpecterOps technical experts and exploration of creative angles like writing from an attacker's perspective.

---

## Context

SpecterOps is a fast-growing cybersecurity company specializing in offensive security and red teaming, with a team of experts who understand attack methodologies and how adversaries think. Bryce Hein, their CMO (4 months into the role), is driving a category creation effort but faces a key gap: while SpecterOps excels at creating technical content for practitioners, their deals actually close through identity security teams and CISOs who need to understand the business and risk context. Marcel Santilli has deep experience in security content—building SecureIntelligence.com for IBM, TechBeacon, and currently working with security companies like SentinelOne and Abnormal Security—so the conversation was grounded in that shared domain context. This call was the second interaction with the SpecterOps team (Tyler and Rick had met the previous week) and marked Marcel's first engagement with Bryce, setting the stage to discuss a potential content partnership.

---

## Relevance

### To GrowthX Delivery
- **Technical credibility in specialized spaces:** The conversation reinforced that GrowthX's approach of keeping human experts in the loop is essential in cybersecurity. For SpecterOps, this means conducting 4-6 deep dives with their red team experts upfront to calibrate the AI system to their voice and ensure the final content maintains credibility with skeptical security audiences.
- **Multi-persona content strategy:** SpecterOps' gap between practitioner-level and buyer-level content is a common pattern. GrowthX should develop methodologies for creating multiple content tiers targeting different personas (practitioners vs. identity/IAM teams vs. CISOs) from the same research base.
- **Quality gating for complex technical topics:** Marcel's point about avoiding "trap topics" where even expert humans struggle is valuable—prioritize narrower focuses early (e.g., specific identity attack vectors) before scaling to broader security topics.

### To CheckThat / LLM Visibility
- **AI answers + security credibility:** The discussion around AI visibility in security is timely—security professionals are skeptical of LLMs but the market is shifting toward AI-powered research. Documenting how deep research, proper attribution, and authority signals make content rank in AI answers will be valuable case study material for CheckThat positioning.
- **Domain-specific research agents:** Marcel demonstrated CheckThat's research agent capability (using Exit AI, Perplexity, etc. with structured success criteria) as a core differentiator. SpecterOps is a good test case for whether these agents can maintain technical accuracy in red teaming.

### To GrowthX Business Development
- **Capacity-constrained model validation:** Marcel's mention of 100% conversion rate on 8-week strategy sprints and deliberately limiting to 2 kickoffs/week reinforces the power of the scarcity model. SpecterOps is deal-qualified and booking 4-6 weeks out, signaling high demand.
- **Series B funding moment:** GrowthX is actively raising Series B. A successful SpecterOps engagement ($30k for initial sprint per metadata) would be a strong security vertical reference and proof point for the AI-assisted content model.

---

## Overview

- SpecterOps excels in offensive security but needs to better target identity security teams and CISOs
- GrowthX offers AI-powered content creation with human expertise to maintain quality and credibility
- Collaboration could help SpecterOps scale content production while preserving technical accuracy
- Initial 8-week strategy and execution sprint proposed as starting point for potential partnership

---

## Key Topics

### SpecterOps Background and Challenges

- CMO Bryce Hein joined 4 months ago; company growing quickly and doing category creation
- Strong in long-form technical content for practitioners, but need to improve SEO/discoverability
- Excel at offensive security/red teaming, but deals often close through identity security teams
- Need to better target and communicate with identity/IAM teams and CISOs
- Challenge: maintaining technical credibility while expanding content for broader audience

### GrowthX's AI-Powered Content Approach

- Uses AI to scale quality content creation while keeping human experts in the loop
- Creates detailed artifacts on personas, products, writing guidelines to inform AI systems
- Employs coding agents to build deterministic workflows for research, drafting, and editing
- Fact-checking system verifies content against knowledge bases and trusted sources
- Aims for high-quality, personalized content that can perform well in both search and AI answers

### Potential Collaboration Strategy

- Start with 8-week strategy and execution sprint to prove value and set direction
- Focus on calibrating AI system to SpecterOps' voice and technical standards
- Begin with narrower topic focus to establish quality before scaling
- Conduct 4-6 deep dives with SpecterOps technical experts to build domain knowledge
- Prioritize content types and topics where AI can meet quality bar initially

### Content Distribution and Influence

- Build strong owned content engine as foundation before expanding to third-party sites
- Potential for repurposing content as answers to specific questions on platforms like Reddit
- Explore targeted outreach to update/improve mentions on relevant third-party sites

---

## Action Items

- **Marcel Santilli (GrowthX):** Follow up with more details on 8-week sprint offering and service scope
- **Bryce Hein (SpecterOps):** Consider timing and budget for potential engagement; identify primary persona focus for initial sprint (identity/IAM teams vs. CISOs)
- **SpecterOps team:** Explore creative content angles, such as writing from an attacker's perspective for the practitioner audience
- **Bryce Hein (SpecterOps):** Prioritize and confirm which personas to target first (identity/IAM teams and CISOs) for content strategy calibration

---

## Transcript

**Ric Nguyen:** Hey, everyone, good to see you again.

**Tyler Pavlas:** Pretty good. I am headed out of the office tomorrow afternoon for my bachelor party, so it is a bit tough to stay focused, if I'm being honest.

**Ric Nguyen:** Dad, dude, congrats. Hell yeah, that's going be so fun.

**Tyler Pavlas:** Yeah, thanks so much. Definitely different than it would have been if I got engaged in my 20s. We're going to, like, Oregon and, like, in this huge, you know, nice cabin out in nature, watching a bunch of college football, chasing waterfalls.

**Ric Nguyen:** So I think in my 20s, I probably would have been in Vegas or something regrettable like that. It's funny how things change, but honestly, that sounds so much better. There's something chill, you know?

**Tyler Pavlas:** Yeah, I mean, I'm sure I'll return hungover. Just getting some quality time with the boys this go around. I'm just going bring in Meshach and Bryce.

**Ric Nguyen:** Cool. I think there was some issue with the link. You had to click into the meeting and then click the Zoom link from there.

**Tyler Pavlas:** Gotcha. No worries.

**Meshach Cisero:** Hey, Bryce.

**Bryce Hein:** Hey, everyone.

**Tyler Pavlas:** Yeah, it's going great. I was just catching up with Ric. It's my last day in the office before I go on my bachelor party tomorrow.

**Meshach Cisero:** Where are you headed?

**Tyler Pavlas:** Going to Oregon. Yeah, we're going to do it out in nature. And I've never been there before.

**Bryce Hein:** So the Columbia River Gorge and all those trails and waterfalls, in addition to a lot of college football, is the agenda. I'm up in Seattle, so not too far from it.

**Tyler Pavlas:** Okay, nice. Yeah, last time I was out there, I went to Olympic National Park.

**Tyler Pavlas:** Marcel should be joining us shortly here. And I had a chance to catch up with Ric and Meshach last week. I guess as we're waiting for Marcel, we'd love to just kind of catch up on where you guys are at internally. Maybe do like an intro from you, Bryce, and I can give an intro as well.

**Bryce Hein:** Great. So I'll start with my intro. I'm Bryce, CMO, been here about four months now. Interesting ride. We are growing quickly as a company, and really, it's an opportunity for us to do category creation. The company has built a lot of content, but for human absorption and human practitioners, quite frankly. So as we think about up-leveling our positioning, we're making it more crawlable. That's sort of an opportunity for us. I feel like we have a source of strength with long-form content and good, solid kind of depth to it. But we're only now evaluating how do we get this really going with SEO.

**Tyler Pavlas:** Awesome. Yeah, that's good.

**Marcel Santilli:** Hey, everyone. So sorry. Today's been one of those back-to-back days. It's like you're two minutes late to one, and then you're three minutes late to the next, and then four minutes, you know.

**Bryce Hein:** Cancel your last one right now.

**Marcel Santilli:** Let's see how many more I got. But this is fun. It's energizing. I like days like this.

**Bryce Hein:** I've got five more today.

**Marcel Santilli:** So sorry to jump in, but I think you were just giving a little bit more context, right?

**Bryce Hein:** Yeah. And we can talk a little bit about what you guys did last time. I missed that meeting, but I'm excited to be engaging with you guys.

**Tyler Pavlas:** Yeah, absolutely, Bryce. That overview helps. And Marcel, I can just do a quick recap of the conversation I had with Ric and Meshach last week to give us good context here.

**Marcel Santilli:** That sounds good. Yeah, and I'm super familiar with the space as well. It sounds like you guys have done quite a bit of content already, right? Happy to jump in and show more detail if you think would be helpful. But I'm always curious: What would be the limiting factor to more growth, more organic growth right now for you all?

**Bryce Hein:** Yeah, I would say that one of the things we're doing is having people reframe. A lot of times in cybersecurity, people think from the defenders' perspective — how do I understand my estate versus how do adversaries understand the estate? So one of the things we're trying to do is get enough content out there that it almost flips the mindset to, okay, now I'm going to look through the glasses of the adversary. Because once you do that, you see all the paths. And literally what our product does is it tells the adversary how to get to the goods and then how can you remediate that? So the lift for us is absolutely getting people to think differently.

**Marcel Santilli:** Yeah, yeah. I love that. And I don't know if you guys knew, but early on in my career, I built a site called SecureIntelligence.com. And it was the first off-domain site for IBM. It just got folded back into IBM.com. We had just acquired QRadar and another Israeli company called Trusteer, and my job was to consolidate all of that. And in the process, I realized they had way better content than IBM did. So I spun up another site and made that good. We got access to their research team's zero-day vulnerability content and POCs. And we would do a spin on that, then reach out to security analysts like Brian Krebs and be like, hey, we have this really cool zero-day vulnerability that Microsoft just patched. Do you want to cover it? And that stuff started getting crazy picked up because it was like primary data. The site gained a bunch of authority. After that, I built TechBeacon.com, which also covers security. Then I was at HashiCorp, and now we work with a lot of security companies like SentinelOne, Abnormal Security, and a few others. So security has been near and dear to my heart for a long time.

**Bryce Hein:** Excellent. So when we start geeking out, you understand what we're talking about.

**Marcel Santilli:** Yeah, yeah, yeah. I can't say I'm as technical as I used to be, but I understand conceptually and I've talked to a ton of security people. So I understand the nuances.

**Bryce Hein:** Good. In our thought leadership, when we put blogs out, it's very technical by design, and we end up getting like 3,000 to 5,000 views from it. But it's more SEO oriented, not AI visibility oriented. And we're trying to figure out where we need to tweak content and where we need to get it out into third-party sites. We think our sentiment is good on Reddit because we're very community-based, but we haven't measured it. So it's that kind of stuff where it's a multi-pronged problem, and we're trying to figure out where to start knocking down early opportunities.

**Marcel Santilli:** So maybe I can take a step back. I always like to start with a visual — I'm a visual person. There's a couple of things we've seen in order to scale quality. A lot of what's happening right now with AI answers is that it may be in security slightly less because security people are skeptical in nature, which is a good thing. But a lot of people are researching things in AI and getting AI answers, and they're almost considering that word of mouth from an expert, even though LLMs don't have a huge quality filter on the sources they're citing. So it's kind of like the early days of SEO, where you could just stuff keywords and call it a day. I think for us, we believe that optimizing for quality and credibility with the audience you actually want to serve will eventually be rewarded. And there are things you can do today to get that rewarded right away without breaking trust with your actual human readers. That's fundamentally what we try to do: scale with experts in the loop, work backwards from how experts achieve quality, and figure out where we can use AI to scale without abstracting humans, but to do an even deeper, better job while optimizing for scale and speed while maintaining or even increasing quality. And that's been true for 15 years — how do we serve people? How do we serve the right audience? How do we create resources that they would pay for, but instead we're giving away for free? That always comes from a deeper understanding of the audience. It's not just, hey, you're a security person. There's a way deeper way to understand their jobs to be done, the things they really care about, the pain points, what will cause them to get fired, who are the stakeholders they need to satisfy, what work products they have to deliver? And from that, we create a map of topics they care about, which is also the map of things we're going to track in LLM visibility. It's the things we need to execute against. So when we work with clients, we map out your audience, understand your business, map out the content we should be creating, and then create these artifacts that go deeper into understanding personas, companies, products, writing guidelines. From there, we can create pipelines that work differently for technical companies, achieving quality systematically with a human in the loop, an editor who has the context of your company. With technical spaces, we're never going to be more of an expert than your researcher or your security person who's been in the weeds for 20 years. What we're trying to do is understand your inputs, consistently execute against those inputs to scale quality, and continue to enrich it with your perspective. We can't come up with thought leadership out of thin air because it wouldn't be you. But we can find information, research it, figure out how to communicate it really well, understand how you see the market, the space, those topics, and match those two to ensure quality and raise the bar. And hopefully, if we need to add more unique view, we can do more interview-based work or process transcripts.

**Marcel Santilli:** What we built under the hood is a coding agent that writes processes in code in a runtime layer. Every one of our workflows is in code — our prompts, everything. That allows us to build agentic and deterministic workflows. For instance, we have an agentic researcher that generates a research plan, ingesting context and figuring out what tools to use. We have several APIs — Exit AI, Perplexity, Parallel, Deep Researcher from OpenAI, and Plot. It figures out the success criteria and the types of sources that make sense. For instance: look at OWASP only, or the vulnerability database, or only consider third-party blogs from notable security researchers. Don't use new sources. Then it evaluates that, runs through the process, generates additional questions, and compiles it all into a research brief. The research brief is super comprehensive. An editor can go in, use our assistant that's like a Cursor-like experience, and shape content while doing line edits. Then the same for the drafter. We take it all the way to the finish line. For example, with tax advice — it's technical because the IRS is your source of truth, but there are lot of technicalities. We take that source, apply it to the context of a specific person or business type, add writing guidelines for how we want to sound, and when you bring that all together with an expert in the loop, you achieve quality and personalization. We're seeing incredible success. The day before we published one article, they weren't showing up for a search query. The day after, they're showing up and using the exact language, and they're showing up in AI mode as well. So the factors that make a huge impact are the things we were already doing: deep research, good attribution, comprehensive answers that are well-formatted and well-structured, authority signals — hey, so-and-so said this and why they're an expert — and your brand reputation.

**Bryce Hein:** I try to get us super humble. There's a couple of things running through my mind. We are very good at offensive security. The team came from red teamers, so they know how to attack companies. Our whole brand is leading edge, getting to critical assets, the adversary point of view. And that's really good. But if you ask us how deals get done, deals get done because identity gets in the loop. The identity security team decides. Speaking to that persona can be clarified or simplified a bit.

**Marcel Santilli:** It can be about their IAM teams or user access identity.

**Bryce Hein:** Yeah. And so I think we're jumping over that audience a bit. We need to be doing that. What we're going to be doing is prioritizing our persona flow and content flow for that audience.

**Marcel Santilli:** That makes sense. Essentially, if I'm hearing it correctly, red teaming experts are very unique, it's really hard to win their trust, and there's not millions of them out there. And from a commercial perspective, you need to know how to talk to and resonate with different audiences that might be the budget owners. Is that maybe a way to think about it?

**Bryce Hein:** You nailed it. We bring all kinds of credibility and we don't want to distract from that or lower it, but we need to put it in the context of that other audience. So what you just described could help us accelerate it. We've also seen and heard that LLMs crawl a lot of third-party sites. So how does what you just described help us influence that as well?

**Marcel Santilli:** Yeah, this is coming up more and more. I think there's a lot of things we want to experiment with. But before you go influence the world, you need to have your content engine running well, putting out value every single day that builds trust with your audience and earns credibility. It's not a replacement for that. I was just talking to a company today where their traffic has been going down 50% in the last six months, but they wanted help hitting up third-party sites to mention them instead of focusing on their core content engine. Sure, that's not a bad strategy as long as you have an engine where you're earning credibility. Some of the things we're doing is taking content we're creating and later repurposing it as answers to specific questions. We've also done backlinking campaigns where we reach out to sites with good content and say, hey, I noticed this link is broken, can we help fix it? Here's how you can fix it, and by the way, we'll mention you. We're doing this for Reddit too. But full transparency, we've gotten so much demand for core work that we're not doing that for a lot of customers. I just don't want to be misleading. But I think once you have a good content strategy executing, repurposing or reaching out to someone to update their language gives you even more credibility. You can work out something where you cross-link as well. It's a give and take versus just spamming a thousand sites to talk about you.

**Bryce Hein:** Makes sense. Meshach and Ric, I've been talking a lot. Any questions?

**Meshach Cisero:** I definitely wanted you to get as much context as possible. We walked through a lot of this in Tyler's conversation last week. One thing I did want to talk about is verification flow. Right now, a lot of our technical content has eyes on it from our technical experts, researchers, and product members. How do you build out that kind of verification flow into content being produced? Because sometimes that content could be quite a bit, and I want to make sure we're pulling in the right folks earlier so we can get trust from our counterparts on the business side, so the marketing team is putting out really good quality AI-driven content. How does that flow work?

**Marcel Santilli:** Yeah, so there's a couple of different things we think about. There's definitely calibration processes where we show you how our application of how we want to sound will look and make sure we're aligned based on inputs we get. Then the other piece is ingesting a knowledge base and understanding where your source of truth is. For instance, with documentation sites like a Strapi CMS, we look at their doc site and put it into a knowledge base so we can retrieve it and verify it. We have a fact-checker that breaks content into chunks, extracts passages from each chunk, does research, and verifies statements. If anything has a high confidence level that it's not true, it flags it with a confidence score and suggests a rewrite. It's really nuanced. Where things don't go right in gaining trust of technical stakeholders is when they don't know what they're reviewing and we haven't done calibration or ingested enough domain expertise. With technical companies like SentinelOne, we try to do four to six deep dives with technical experts and narrow down to one space initially to make sure we can get to quality before scaling. We also understand different types of topics — what is a vulnerability versus a how-to within your product — and stay away from trap topics where even a security expert might not hit the bar themselves. Let's pick things we can win trust early on and build knowledge to tackle more complex, harder things.

**Meshach Cisero:** Okay.

**Marcel Santilli:** That's how we've seen it work, but it can change. Let's collaborate and be in it together. We don't have all the answers, and this stuff isn't easy to solve even without AI.

**Meshach Cisero:** Yeah.

**Bryce Hein:** I don't want to make you three minutes late to your next meeting, but I have one final question. Are you guys looking to expand right now?

**Marcel Santilli:** Are we looking to expand, particularly in cybersecurity? Yeah, yeah. So a couple of things. We do this eight-week strategy and execution sprint. It's a way for us to deliver a ton of value and set everything in good motion. And then from there, it goes into a longer-term commitment. So far, knock on wood, we've had a 100% conversion rate on those. But we do capacity constrain ourselves on purpose. We only do two kickoffs a week because there's a dedicated team to each engagement. It takes a lot of context to dive deep into understanding your business. You can't have one meeting and pretend to know everything about your space. That's the intentional bottleneck we put on the business. So we're normally four to six weeks out booked. But because those eight weeks is the only thing you're committing to unless you decide to continue, it's kind of a no-brainer for people. And it's almost like a loss leader for us because we know we can prove ourselves in those eight weeks.

**Bryce Hein:** Cool model.

**Marcel Santilli:** And we are definitely expanding because we're in the middle of raising our Series B. Every deal matters, but not at the expense of quality and breaking trust. But we'd love to help. Security is near and dear to me. It's what I've spent most of my career on. So anytime I can help a security company that's doing really cool stuff, that would be really cool.

**Bryce Hein:** I'll leave you with this. We talked about IAM quickly, but also CISOs. We are so used to grinding and creating credibility at the practitioner level that we haven't been able to uplift it yet. And I know we've got a great story to tell. So those would be our two personas.

**Marcel Santilli:** Yeah. I also think there's some really cool creative things you can do. I love your idea of looking from an attacker's perspective and reverse-engineering to write content as if you were the attacker explaining how something works. That can be that persona. There's some cool stuff we can do. I think that would be really cool. And then not hide that we're using AI, but really lean into it.

**Bryce Hein:** Very cool. All right, guys.

**Marcel Santilli:** Thanks so much for your time. Appreciate it. We'll follow up.

**Bryce Hein:** Good to meet you.

**Marcel Santilli:** Take care.
