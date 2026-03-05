# Temporal.io <> GrowthX AI

<metadata>
date: 2025-02-12
time: 18:04 UTC
duration: 29 minutes
organizer: Marcel Santilli (GrowthX)
participants: Lauren Bennett (Temporal.io), Marcel Santilli (GrowthX)
fathom_recording_id: 46919449
fathom_url: https://fathom.video/calls/230987898
share_url: https://fathom.video/share/Gf-W1DymM8jeheS9cau5ztd1fEkWWoqU
source: fathom
enriched_on: 2026-03-05 14:32 UTC
</metadata>

---

## Summary

Marcel Santilli showcased GrowthX AI's sophisticated AI-powered content creation platform, which processes over 20 million words monthly using Temporal as the critical runtime layer orchestrating 200+ workflow steps per piece. Both parties aligned on a co-marketing case study for developers, with Lauren Bennett (Temporal's content marketing manager) to send guiding questions and Marcel's CTO to draft the blog post after GrowthX's 2-week due diligence period closes.

---

## Context

Temporal.io is an open-source workflow orchestration platform used by developers to build resilient, long-running applications. Lauren Bennett, their content marketing manager for the past 6 months, is building a technical content marketing funnel targeting developers. GrowthX AI is a B2B content marketing services company that has evolved beyond traditional services into a technology-driven platform: they handle complex AI-first workflows to generate high-quality content at scale, using AI agents augmented by human editors. The two companies share common investors (Madrona), and there were pre-existing connections through Temporal's Head of Product (Friti) and members of the GrowthX team. Marcel reached out to explore co-marketing because GrowthX's use case—using Temporal to power sophisticated AI workflows—is unique in the market and represents the kind of technical implementation story that resonates with developers.

---

## Relevance

**To GrowthX Delivery:**
- Marcel demonstrated how GrowthX's 200+ step workflows with embedded editor reviews, quality gates, and human-in-the-loop checks represent a best practice for AI-augmented content creation (not just raw AI output).
- The case study will illustrate GrowthX's proprietary framework that allows spinning up complex workflows in minutes rather than weeks, competitive advantage worth protecting but can be publicly shared at a high level.
- Processing 20M+ words monthly requires robust handling of API failures, retries, and parallel execution—all things Temporal enables.

**To CheckThat:**
- Not directly mentioned, though the discussion of AI visibility and how GrowthX content ranks in Perplexity and ChatGPT search results maps to CheckThat's core domain.

**To GrowthX Business Development:**
- Co-marketing blog post and potential webinar with Temporal positions GrowthX as a technical thought leader to developers and engineers, expanding brand awareness beyond current B2B content marketing clients.
- GrowthX is hiring 35 engineers this year—the visibility from Temporal's developer audience is strategically valuable for recruiting.
- Potential for deeper partnership: Temporal inquired about whether GrowthX could help with Temporal's own content needs (Lauren to discuss with Claire).

---

## Overview

- GrowthX AI uses Temporal as the runtime layer for their AI-powered content creation workflows, enabling complex, scalable processes
- Both parties are interested in co-marketing, with a focus on a technical case study highlighting GrowthX's unique use of Temporal
- GrowthX is rapidly growing, processing over 20 million words monthly for clients and planning to hire 35 engineers this year
- The co-marketing effort will target developers and showcase Temporal's capabilities in AI workflow orchestration

---

## Key Topics

### GrowthX AI's Content Creation Process

  - Utilizes complex AI workflows with 200+ steps per content piece
  - Leverages Temporal as the runtime layer for orchestration and execution
  - Processes hundreds of thousands of tokens per content piece
  - Incorporates human editors for quality control and brand alignment
  - Achieves rapid content production at scale (20M+ words/month)

### Temporal's Role in GrowthX AI's Stack

  - Critical for handling API failures, retries, and parallel processing
  - Enables long-running workflows and scales to meet high-volume demands
  - Integrated into GrowthX's custom framework for AI agent interactions
  - Powers visual workflow representations while executing via Temporal's API

### Co-Marketing Opportunities

  - Blog post/case study showcasing GrowthX's use of Temporal
  - Potential webinar to dive deeper into the technical implementation
  - Focus on developer audience and Temporal's capabilities in AI workflows
  - Balance between showcasing technology and protecting GrowthX's IP

### Next Steps for Co-Marketing

1.  Lauren to send guiding questions and ideal angles for the case study
2.  GrowthX's CTO to draft a detailed blog post
3.  Collaborate on refining the draft after GrowthX's due diligence period (2 weeks)
4.  Explore additional co-marketing options based on the initial case study

---

## Action Items

**Lauren Bennett (Temporal.io)**
- Send case study questions/guidelines to Marcel for GrowthX's AI workflow use case, including ideal angles and framing for developers
- Discuss with Claire about exploring content production help from GrowthX AI team

**Marcel Santilli (GrowthX)**
- Brief GrowthX's CTO to draft a detailed blog post about Temporal's role in GrowthX's platform (after 2-week due diligence closes)
- Send meeting transcript to Lauren and add to Slack channel for reference

---

## Transcript
**Lauren Bennett:** Happy to do the same on my end. Okay, so I'm Lauren. This meeting is being recorded. I'm the content marketing manager here at Temporal. I've been here for about six months, and my main responsibility is the content marketing. I'm creating a full funnel campaign, trying to get us to have a really regular rhythm for what we're doing—create rich technical content and make sure that we're scaling it organically. I've been in tech for about four years. Before this, I was at a mobile-first company doing backend analytics. Our company and competitors were like DataDog, Firebase, things like that. What about you?

**Marcel Santilli:** That's awesome. Well, I'm originally from Brazil, born and raised, grew up in Texas. Started my career at IBM and HP, building massive content programs for technical audiences. At IBM we had securityintelligence.com, which became a really huge source of pipeline for those businesses. Then I joined startups—HashiCorp, where Friti was SVP of Product. She's your Head of Product now. Then after that, Service Tier, Skill AI, and most recently Deepgram. Along the way, pretty much every job I've had, I've built some kind of content program that helps the company grow organically. And every time it's the same thing you're probably experiencing: you hire a managing editor or content strategist, come up with a really strong overall strategy for the topics you want to tackle, recruit contributors and writers and editors, then ramp up on content production. By the time you're done, it's a dozen-plus people, you're spending tons of money, and you're six months in before you even start publishing at strong cadence. So a lot of what I'm building now with GrowthX is: how do we leverage AI to augment that process at every step? Our framework allows editors and strategists to guide both strategy and execution, with staging and quality checks built in. With AI, we use really robust workflows—instead of having an editor read the top five results, we go for a hundred sources, filter them based on relevancy and custom criteria, and summarize. We do that for every single piece of content. I'm not sure how much context Claire gave you, so I'd like to hear more about your priorities and bottlenecks.

**Lauren Bennett:** As far as our content production, my biggest pain point right now is the fact that we're a pretty small team. So our content needs are significant, and I can collaborate with technical team members on that. But it can be tricky working with developers to make sure we're balancing technical content and the actual writing itself.

**Marcel Santilli:** Well, I'm super excited to share some stuff because we're actually building everything on top of Temporal as our runtime layer. And we're huge customers. Not necessarily from a dollar perspective, but in terms of how much we use Temporal. Our lead investor, we just signed the term sheet for a Series A—our lead investor, Madrona, is also an investor in Temporal. So there's a lot of connections here that I was extra excited about. I want to show you a little bit of how we approach things, if you think it'll be helpful. Let me share my screen and show you what we build.

**Marcel Santilli:** A lot of the challenges we've had in the past: how do we do this quickly and at scale? In the past, I was building these programs for startups, and every single time it was the same thing—massive growth but a ton of work. Then in April last year, I started doing workshops showing people how to build AI workflows to augment their content process, taking all the learnings I've had over the last 15 years. We inserted experts in the loop, and the brands and companies that started doing that got amazing results. We realized: it's not just using AI and churning out crappy content. It's about building entirely complex AI workflows, being really thoughtful about inputs, and having editors in the loop to guide and improve the process and quality.

This approach got validated more and more across the board. Almost everyone we talk to says the same thing: "Agencies are expensive, my team is super small, I need help, but tools are all over the place. I need a partner that helps me deliver outcomes, not just gives me tools to figure out how to use, or slow services that are expensive and don't scale."

So we built an AI-first approach to everything we're doing, delivering as outcomes. Here's an example: we go through a kick-off process, do a ton of research on you and your company, develop your entire content strategy, and calibrate the quality so we have a bullseye of what quality should look like. Then we ramp up content quickly.

Underneath the hood, we build a library of components and workflows that are highly adaptable. We built a framework that represents AI workflows as code. We ran into so many limitations with workflow tools out there that we wanted to represent everything as code. Everything's in code—the workflow, the logic, everything. And we're using Temporal as the runtime layer. We have this growing library of components for all the different jobs in the content process: competitor research, context generation, competitor link cleanup, style adaptation. Our framework plugs into coding agents like Cursor, so we can spin up really complex workflows in minutes. The full process looks like this: research, outline generation, editor review, title generation where an editor picks the right angle and sees the reasoning for different options, then article generation, post-processing, and a final editor pass. We have additional components later on like path tracking and cross-linking for other pages on your site.

**Lauren Bennett:** I know you guys have over 3,000 pages.

**Marcel Santilli:** It's really cool because everything we're doing, we're storing all these sources into a vector database, and then we're retrieving all that throughout the process for just one piece of content. So for one piece of content, we're processing probably hundreds of thousands of tokens. What that allows us to do is have editors in the loop to guide the process, while the process ensures high-quality output. The editor in the loop then ensures the voice is consistent, aligned with your brand, checks for anything that matters to you. You can be part of the process however you want at any step, and we do all the legwork—statement in the CMS, hitting publish, updating content, all of that.

**Lauren Bennett:** Yeah, I like the sound of it. It definitely sounds useful. What would you say is your best, heaviest-hitting use case that illustrates the value?

**Marcel Santilli:** I'd say it's tutorials and programmatic content, especially in technical spaces. Let me show you a couple of examples. Take Ramp—they've seen a ton of organic growth. And Homebase as well, answering very specific questions. When you search for these things in Perplexity or ChatGPT, they're more likely to show up. You can see these sources—these are articles we generated. We figure out searches that are super relevant for them, then generate answers to those specific technical questions. Like, when to use depth-first search versus breadth-first search—that's the kind of content that does really well on the technical side. We're also working with companies like Freetrope, a headless CMS where we've done enrichment for their integration pieces, PromptFoo in the LLM security space, Prophecy.io in the data/movements space, and Abnormal Security just signed with us. We're working with a lot of technical clients.

**Lauren Bennett:** Well, I like the sound of all of that. I know you want to talk co-marketing opportunities, right?

**Marcel Santilli:** Yeah, because when I met with Claire last year and she came to one of our dinners, we hadn't even started using Temporal. Then we discovered all these common connections. It'll be really cool to show how we're using Temporal as our runtime and how it powers the process that helps with content creation. Either way, we're huge fans and we love the product.

**Lauren Bennett:** As a content marketing manager, that makes my heart sing.

**Marcel Santilli:** And I think our use case is really unique. Not a lot of people know how to use Temporal the way we are with AI agents and workflows. We have so many startups that are blown away when we show them what we do.

**Lauren Bennett:** I feel like at this company and my previous one, content marketing functions and teams are warming to using AI for their content processes. When I use ChatGPT for thought partnership or to align my thoughts, I have to rewrite everything—it needs a lot of editing. This seems a lot more advanced.

**Marcel Santilli:** For one single piece of content, we go through over 200 steps, including lots of editor reviews. The real thing that's relevant here is that without a really powerful runtime layer, all these processes break. When you're going through 200 steps with AI models and API calls, things don't work perfectly. You need retries, parallel processing, and long-running workflows. Temporal is the only thing we could find that handles all of that at a crazy scale. We're already publishing over 20 million words a month for clients.

**Lauren Bennett:** That's a really good set. Okay, as far as co-marketing, do you want to jam for a second on what we could do?

**Marcel Santilli:** Yeah, definitely. Have you guys done anything like this before? What would be helpful to you all? We can talk about it quite publicly, and our CTO can talk about it too. There's also this crazy connection—I mentioned Friti, but one of our early employees is actually related to Friti's husband. So there are all these free connections that are really cool.

**Lauren Bennett:** Okay, so my favorite co-marketing opportunity—and I'm biased because I'm the content person—is a down-and-dirty case study. I think you guys have a great opportunity to illustrate what you're doing. Even the diagrams and growth graphs you've shown me—even if we anonymize those and say it's "X company doing X thing"—I think that could be great. Did you have anything in mind, or were you thinking more of a webinar?

**Marcel Santilli:** I think we can do a blog-style case study. We could do a webinar together too. It really depends on what audience you care about. For us, the benefit of doing the technical angle is that we're hiring a ton—about 35 engineers this year. The more exposure to what we're building and how we're building it, that's great. The only limit is being thoughtful not to give too much IP away, but our CTO can figure out the right level where we show how powerful our runtime layer is without giving away the secret sauce.

**Lauren Bennett:** My target audience is similar to yours—the generalized developer persona, hands-on keyboard. I like your idea of a blog-style case study. We have a series going right now talking about customers building AI use cases, and you'd be a perfect fit. We're definitely conscious of not giving away your secret sauce, but I think we could get really rich content. Here's an example case study we have on the site.

**Marcel Santilli:** Yeah, we can definitely do something like this with way more screenshots. This is just the first iteration. For the ones we have in flight, I definitely want schema diagrams, code examples—yes, exactly. This is our process right now, just part of it. It would be impossible to run without Temporal. We have some things we need to filter out a little bit, but the main thing is that everyone's obsessed with AI. For us, we built a framework. You all are the orchestration and execution layer for us. We have this file system in our framework that allows us to plug into coding agents like Percher. The entire workflow process went from taking a month with drag-and-drop tools to minutes. But you need a way to run all of it. We have a ton of really cool details to share. The visual representation pulls from your API—it's just a more visual way to represent workflows, but it's all powered by our runtime. We can even do little demos or show things like this.

**Lauren Bennett:** That would be amazing. Okay, so next steps. I know your schedule is very busy. Going into the rest of February and top of March, we're going to be busy on our end because of Replay, the conference at the top of March. What would be easiest for you? I prefer to do case studies over a call—about an hour. But if you're super busy, I can write out the questions and send them over.

**Marcel Santilli:** What would be helpful is if you can send anything that helps guide what you're ideally hoping we can touch on, especially from a platform perspective. We can go super in depth or a little bit less, whatever gives you the angles or framing that's ideal for you. Then on our end, I can ask our CTO to write a really good blog post with details. We're in the middle of due diligence right now, so we won't be able to publish before that closes—just two more weeks. But after that, we can go back and forth on drafts and make sure you feel good about it. We'll look at your example and any others.

**Lauren Bennett:** That sounds great. It should be pretty low lift for you all.

**Marcel Santilli:** Yeah, I'll pass it on to my CTO.

**Lauren Bennett:** Are you going to Replay? It's my first time.

**Marcel Santilli:** I've been several times. I have a lot of restaurant recommendations if you need them.

**Lauren Bennett:** I'm a very food-motivated person, so I'll definitely figure it out.

**Marcel Santilli:** Book the food first, then the flights—that's what my wife and I do.

**Lauren Bennett:** It was really lovely talking to you. We'll talk soon.

**Marcel Santilli:** I'm excited. Thanks, that sounds good. I'll look for questions from you and give my CTO a heads up as well.

**Lauren Bennett:** Can I also get the recording?

**Marcel Santilli:** Yeah, I'll send it to you. There are a few things I showed you—I want to make sure we protect our IP, but I can send the transcript and add it to a Slack channel.

**Lauren Bennett:** Sure.

**Marcel Santilli:** The transcript will make it a lot easier. I also know Claire reached out to you about exploring content help from GrowthX. Obviously it's up to you if you want to explore that further.

**Lauren Bennett:** I'll talk to her about that later today. We have a meeting scheduled.
