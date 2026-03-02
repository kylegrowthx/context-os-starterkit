# Tobiah Rex -Agentic System Design | AI Engineer (Software Engineer, AI and Agent)

<metadata>
date: 2025-12-18
time: 21:02 UTC
duration: 69 minutes
organizer: ben@growthx.ai
participants: Ben Church (GrowthX), Tobiah Rex
fathom_recording_id: 109915439
fathom_url: https://fathom.video/calls/510283348
share_url: https://fathom.video/share/9QxYP-1AgYRz3FTXhEivkxqTVWx1nBwK
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Ben Church conducted an agent system design interview with Tobiah Rex, an experienced AI and software engineer. The discussion centered on designing an agentic system for generating long-form articles for GrowthX clients, using a "Narrative-First" architecture based on Gretchen Rubin's "Four Tendencies" framework to match client brand voice. Tobiah proposed a modular architecture with core services (DocService, FrameworkService) orchestrated by a TendencyMatchingController, combined with adversarial "Bug Engineer" agents to combat LLM hallucinations and ensure factual accuracy.

---

## Context

This was an agent system design interview between Ben Church, a GrowthX engineer (formerly at Airbyte), and Tobiah Rex, an experienced AI and software engineer with 8+ years in the field and previous fintech/trading background. The meeting explored how to architect an AI-powered content generation system for GrowthX's content marketing services. Tobiah was evaluating GrowthX as an opportunity to learn go-to-market strategy combined with AI, having identified this as a gap in his skillset (insight + idea without GTM strategy, per the Shazam founder model). The interview format was collaborative: Ben walked through system requirements while Tobiah proposed architecture decisions, with both parties learning from each other.

---

## Relevance

**To GrowthX Delivery:**
- Concrete architecture for agentic content generation: Narrative-First Design + Four Tendencies framework provides a reusable pattern for client projects, reducing iteration time on brand voice alignment.
- Adversarial validation approach (Bug Engineer agents) directly addresses hallucination risk in LLM-generated content—critical for client-facing deliverables.
- Modular service-oriented architecture (DocService, FrameworkService, TendencyMatchingController) enables incremental implementation and testing of content pipeline.
- Human-in-the-Loop workflow (Content Expert persona) aligns with GrowthX's internal-tool-first positioning and matches current agency operations model.

**To CheckThat:**
- Knowledge graph approach for research data storage offers faster, more precise retrieval than vector databases—relevant for improving CheckThat prompt generation and AI visibility analysis.
- Four Tendencies framework could be extended to characterize B2B content patterns and messaging styles in CheckThat's competitive intelligence work.

**To GrowthX Business Development:**
- High-caliber engineering talent pool: Tobiah's background (fintech, AI, capital markets) and growth trajectory suggest potential for expanded engineering capacity and specialized AI work.
- Architecture discussion demonstrates GrowthX's sophistication to candidates—hiring tool and signal of internal technical bar.

---

## Overview

- **Narrative-First Design:** The system's foundation is a "Tendency Matching Engine" that analyzes client documents to define a core narrative using the "Four Tendencies" framework. This provides a concrete, measurable standard for all subsequent content generation.
- **Adversarial Validation:** To combat LLM hallucinations, a "Bug Engineer" agent will be used. This agent's sole purpose is to find flaws in the system's output, forcing the main agents to improve their defensive posture and factual accuracy.
- **Human-in-the-Loop Workflow:** The system is designed for internal agency use. A "Content Expert" persona acts as the human interface, translating client strategy into specific topics and audiences for the AI to execute.
- **Modular Architecture:** The design uses a "middle-out" approach, building from core services (e.g., `DocService`, `FrameworkService`) orchestrated by a `TendencyMatchingController` to ensure a robust and scalable foundation.

---

## Key Topics

### Problem Definition & Success Criteria

  - **Goal:** Build an agentic system to produce long-form draft articles for clients.
  - **Key Requirements:**
      - **Factual Correctness:** A primary challenge due to noisy/contradictory sources.
      - **Brand Voice Adherence:** Must follow client-specific guidelines.
      - **Audience Utility:** Content must be useful to the intended audience.
      - **Minimal Human Edits:** A key cost-saving objective.
  - **Context:** The system is an internal tool for an agency (GrowthX), not a client-facing product. Agency editors and engineers manage the inputs and outputs.

### Solution: Narrative-First Design

  - **Core Insight:** The most ambiguous requirement ("useful to the intended audience") can be solved by first defining a concrete client narrative.
  - **Framework:** The "Four Tendencies" framework (Gretchen Rubin) provides a structured way to classify a company's personality and communication style (Upholder, Rebel, Obliger, Questioner).
  - **Process:**
    1.  **Corpus Collection:** Gather client documents (website, blogs, etc.).
    2.  **Narrative Analysis:** A "Tendency Matching Engine" analyzes the corpus to determine the client's dominant tendency.
    3.  **Validation:** The resulting narrative thesis is presented to the client for validation, ensuring alignment before content generation begins.

### System Architecture & Workflow

  - **Architecture:** A "middle-out" approach, starting with core services and building outward.
      - **`DocService`:** Manages document retrieval from a `CustomerCorpusRepo`.
      - **`FrameworkService`:** Contains the logic for applying the "Four Tendencies" framework.
      - **`TendencyMatchingController`:** Orchestrates the narrative analysis workflow.
  - **Workflow:**
    1.  **Content Expert Input:** An agency editor defines a `Topic` (thesis) and `Target Audience` for an article.
    2.  **Research Pipeline:** For topics outside the client corpus, a research agent executes a plan:
          - Pull data → Analyze → Vectorize → Store in a knowledge graph.
          - **Rationale:** Knowledge graphs are faster and more precise than vector databases for specific data retrieval.
    3.  **Article Generation:** A separate agent uses the validated narrative, topic, audience, and research to draft the article.

### Quality Assurance: Adversarial Agents

  - **Problem:** LLM hallucinations (e.g., fake links, incorrect facts) are a major risk.
  - **Solution:** Implement a "Bug Engineer" agent.
      - **Function:** This agent's sole purpose is to find flaws and break the system, acting as a malicious actor.
      - **Rationale:** This adversarial approach forces the main content-generating agents to develop a more robust, defensive posture, improving factual accuracy and reliability.
  - **Example:** The "Overwatch" system, a personal project for managing AI agents, was shown as a proof-of-concept for this adversarial design.

---

## Action Items

**Tobiah Rex**
- Email Ben Church SQLC resources and documentation links

---

## Transcript
**Tobiah Rex:** This meeting is being recorded.

**Ben Church:** Hey, Tobiah.

**Ben Church:** So sorry for being late.

**Ben Church:** I was the victim of a mandatory restart.

**Tobiah Rex:** That was fun.

**Ben Church:** So ill-timed.

**Ben Church:** got, like, I can't remember the name of the tool, but it's the one that's installed on the company laptops that tries to keep us up to date.

**Ben Church:** Maybe I'm in a minority.

**Ben Church:** It's very aggressive.

**Tobiah Rex:** Oh, that's not fun.

**Tobiah Rex:** Did you get an update today or something?

**Ben Church:** I think I'd been ignoring it long enough, today was the day to move it over.

**Ben Church:** I must, like, instinctively, like, close the warning, you know?

**Ben Church:** Gotcha.

**Tobiah Rex:** Yeah.

**Ben Church:** It's in the way when you're coding, you're like, ah, it's true, it's true.

**Ben Church:** that.

**Ben Church:** It's fine.

**Ben Church:** My bad.

**Ben Church:** Anyway.

**Tobiah Rex:** How are doing, Ben?

**Tobiah Rex:** Yeah, I'm doing good.

**Tobiah Rex:** Yeah, it's been a long week of interviews and work trials.

**Tobiah Rex:** And so I'm looking forward to the weekend.

**Tobiah Rex:** But yeah, this is one of the discussions I was actually looking forward to because I love talking about age and stuff.

**Ben Church:** Amazing.

**Ben Church:** Amazing.

**Ben Church:** Well, at least like the gauntlet of like, you know, interviewing and hiring is going to make the holidays that much sweeter because it is pain, you know, so.

**Ben Church:** Yeah, Roman eggnog should feel great.

**Ben Church:** Okay, well, we can jump right in.

**Ben Church:** We can do like the intros.

**Ben Church:** I'll give you an idea of the interview, what we're looking for.

**Ben Church:** There's no trick questions.

**Ben Church:** And like more or less, this is an agent system design interview.

**Ben Church:** And I'm honestly hoping you teach me some things along the way.

**Ben Church:** Okay.

**Ben Church:** And at the end, we can go into like, you know, the reverse interview and you can ask me all the questions and I'll be as unfiltered as I can.

**Ben Church:** Can never talk.

**Ben Church:** So I can go first if that's helpful.

**Tobiah Rex:** Yeah, sounds good.

**Ben Church:** Excuse me, I'm going over some sickness.

**Ben Church:** So you probably see down here, my name's Ben Church.

**Ben Church:** Been an engineer here at GrowthX since early June.

**Ben Church:** Prior to GrowthX, I worked at a company called Airbyte, which was just a big data movement company down in San Francisco.

**Ben Church:** Yeah, yeah.

**Ben Church:** And did that for, I think, three years.

**Ben Church:** In the last year, I took on, like, their, what's called the Connector Builder.

**Ben Church:** So they're, like, little AI system that reads docs and then writes an API integration.

**Ben Church:** And then thought, I want to do more of that.

**Ben Church:** So then I came over here to GrowthX.

**Ben Church:** Outside of that, I live on the West Coast of Canada.

**Ben Church:** Try and get out skiing and mountain biking when I can.

**Ben Church:** And I got a nearly two-year-old daughter.

**Tobiah Rex:** Oh, nice.

**Tobiah Rex:** I got married two years

**Tobiah Rex:** So I'm looking forward to a daughter.

**Tobiah Rex:** In fact, today I was talking with my wife, and if we have a daughter, I'm in trouble.

**Ben Church:** Why do you say that?

**Tobiah Rex:** Because I'm just going to be a pushover.

**Ben Church:** That's fine.

**Ben Church:** You got to seem the role.

**Tobiah Rex:** Yeah, exactly.

**Tobiah Rex:** Just play your part.

**Ben Church:** Yeah, exactly.

**Tobiah Rex:** Yeah, so I've been a software engineer now for about eight years.

**Tobiah Rex:** I was in military before that.

**Tobiah Rex:** But it's funny, when I tell people I was in the military, they think I'm like this, yes, sir, roger that, sir, type of guy.

**Tobiah Rex:** And I mean, I can play that part.

**Tobiah Rex:** But it was actually that culture that I felt the need to leave.

**Ben Church:** Makes sense.

**Tobiah Rex:** Yeah, I'm much more of a creative person at heart.

**Tobiah Rex:** So the question that I was trying to answer during my military service was what was the instrument to then utilize to express my creative sort of spirit or whatever.

**Tobiah Rex:** And...

**Tobiah Rex:** And I had been coding since I was a kid.

**Tobiah Rex:** My dad was in tech.

**Tobiah Rex:** And I just never considered it in that framing.

**Tobiah Rex:** And so the light bulb went off towards the latter part of my military career.

**Tobiah Rex:** And my brother, I have an older brother, and he had contacts in the tech industry.

**Tobiah Rex:** And I came out to the Bay Area once and kind of validated some assumptions and then decided to go full force.

**Tobiah Rex:** So, yeah.

**Tobiah Rex:** So then my career has been oscillating between really my two primary curiosities, which are fintech and particularly trading and capital markets.

**Tobiah Rex:** My dad was also a day trader, and he taught me a lot of that as well.

**Tobiah Rex:** And then AI.

**Tobiah Rex:** And so that's been the two types of companies that I've always looked for.

**Tobiah Rex:** With GrowthX, it's been really a new learning for me.

**Tobiah Rex:** I don't know if you've heard of Augment.org.

**Tobiah Rex:** Yeah.

**Tobiah Rex:** So I recently watched, I don't know, right when they came out, I watched this presentation by the Shazam founder.

**Tobiah Rex:** And he said that you need three things to start a company.

**Tobiah Rex:** need an insight.

**Tobiah Rex:** You need an idea.

**Tobiah Rex:** And you need a go-to-market strategy.

**Tobiah Rex:** And I thought, well, the first two, I think I'm good.

**Ben Church:** The last one, I have no idea.

**Tobiah Rex:** And so I thought, wow, wouldn't it be amazing to go to a company and learn how to build go-to-market strategies with AI?

**Tobiah Rex:** That sounds like an amazing learning opportunity.

**Tobiah Rex:** So that's what drove me to be here with you.

**Ben Church:** That's awesome.

**Ben Church:** I like the way you weave that narrative.

**Ben Church:** Also, one of my favorite things about technology is, I guess, the absolutely vast areas you can find yourself in, whether it's like FinTech or marketing or, you know, veterinary things.

**Ben Church:** Same thing for the backgrounds of people, right?

**Ben Church:** Well, whether it's military or, you

**Ben Church:** We have Kirkland, who originally was in coffee.

**Ben Church:** I originally wanted to build boats.

**Ben Church:** There's definitely a type that's in tech, but there's also a huge variety that's across the background.

**Ben Church:** So I always love hearing new ones.

**Tobiah Rex:** I think the thing that unites us all, if I may be so bold to assume I know what unites us all, is an extremely strong curiosity to dig for truth.

**Tobiah Rex:** Anyways.

**Ben Church:** I like that one.

**Ben Church:** Yeah, I would say, like, you know, the best, we're all just trying to find the right answer.

**Ben Church:** Same thing, like, ego-less code reviews and stuff like that.

**Ben Church:** Again, it's like, we're all just trying to find the right answer.

**Tobiah Rex:** You're not your code.

**Ben Church:** Exactly.

**Tobiah Rex:** Cool.

**Ben Church:** Exactly.

**Ben Church:** Cool.

**Ben Church:** Well, so let's do a little time check.

**Ben Church:** We're 10 minutes in.

**Ben Church:** That gives us approximately, like, 40, 45 minutes.

**Ben Church:** I got a little bit of space to go over, potentially, but I'll try and keep it to the hour.

**Ben Church:** So I'll give you the overview.

**Ben Church:** We're going to go back into what I think you used, Excalibur.

**Ben Church:** We'll go right back in there.

**Ben Church:** So I'll share a link to basically just a blank session.

**Ben Church:** I'm going to find my Zoom chat.

**Ben Church:** There we go.

**Ben Church:** There's the Excalibur.

**Ben Church:** Let me know that you can see it.

**Tobiah Rex:** All right.

**Tobiah Rex:** I'm in.

**Ben Church:** Perfect.

**Ben Church:** Okay.

**Ben Church:** I'll drop the text editor.

**Ben Church:** It's very skinny, it?

**Ben Church:** Oh, that's Excel, isn't it?

**Ben Church:** Yeah.

**Ben Church:** Cool.

**Ben Church:** So I put a prompt in the middle.

**Ben Church:** Just let me know if you can see that as well.

**Ben Church:** And then I'll read through it.

**Tobiah Rex:** Yeah, I got it.

**Ben Church:** Okay.

**Ben Church:** So the shape of this interview is like, again, there's no trick questions.

**Ben Church:** Like the idea is to see how you think.

**Ben Church:** Okay.

**Ben Church:** Okay.

**Ben Church:** I'll

**Ben Church:** And for me to see how you break down problems, how you construct an agendic system, and what you know, and how that lines up with what I know.

**Ben Church:** I imagine because this is right at the edge of everyone's discovering how to work with LLMs and kind more durable systems, I'm hoping you're going to teach me something along the way.

**Ben Church:** So we're going go through this prompt, and it starts with us kind of going through success criteria and breaking down the problem.

**Ben Church:** Then it moves into, you know, like constraints and requirements, then into like the actual system design.

**Ben Church:** Like how would you put this together?

**Ben Church:** Afterwards, we'll probably dive a little deeper into how do you evaluate these systems?

**Ben Church:** How do you tweak these systems?

**Ben Church:** How do you think about them?

**Ben Church:** But generally, it's kind of like a back and forth.

**Ben Church:** So does that sound all right to you?

**Tobiah Rex:** That's great.

**Tobiah Rex:** Yeah.

**Ben Church:** So like at GrowthX, this is very on-brand.

**Ben Church:** Like, let's say you're

**Ben Church:** In the company, we're starting from scratch, maybe, because we have this system ourselves.

**Ben Church:** It's like, we want to build a system that produces long draft articles for clients.

**Ben Church:** Simple as that, right?

**Ben Church:** The key pieces are, like, we need to have them factually correct.

**Ben Church:** You know, that's a difficult thing to do.

**Ben Church:** They need to follow different brand voice and guidelines, right?

**Ben Church:** So it's not like we're making the system just for us.

**Ben Church:** We're making them for clients, right?

**Ben Church:** We need to bring in, like, those kind of differences and writing guidelines and brand voice and things to say, things to not say, competitors to mention and compares to not.

**Ben Church:** We'll have, like, the input of audience, because, like, your audience switches between long-form articles, right?

**Ben Church:** You have a different intent there.

**Ben Church:** And then the goal here is to have minimal human edits.

**Ben Church:** So we have humans available in the loop.

**Ben Church:** We can break the system and say, at this point, you know, under these criteria, we should bring in a human.

**Ben Church:** At the end, we should bring in a human or not, you know, kind of up to everything.

**Ben Church:** Editors are expensive.

**Ben Church:** People are expensive, so we try and minimize the use there.

**Ben Church:** Sources could be noisy or contradictory.

**Ben Church:** know, context size, latency, cost are all things to consider with these systems and monitor.

**Ben Church:** But for you in this process, like, you're a principal engineer coming in and you own the system end to end from, like, starting off the design all the way to seeing it implemented and monitoring it.

**Ben Church:** Awesome.

**Ben Church:** I was there.

**Ben Church:** Yeah.

**Tobiah Rex:** Yeah, so.

**Ben Church:** Questions?

**Tobiah Rex:** Yeah, definitely have a few questions.

**Tobiah Rex:** So, first off, I love this because it's basically, it's very complementary to the system that I built at Play, which was very, very concrete in its way to measure outcomes as successful or non-successful.

**Tobiah Rex:** This is complementary in that.

**Tobiah Rex:** it.

**Tobiah Rex:** Okay.

**Tobiah Rex:** It's much more subjective because it's a go-to-market strategy.

**Tobiah Rex:** It's like, let me sell you on my opinion of how I see the world, you know, from my business use case.

**Tobiah Rex:** So anyway, I think that's a way more flexible outcome definition, to be fair.

**Tobiah Rex:** But yeah, anyways, that was just a side thought.

**Tobiah Rex:** Okay, so factually correct.

**Tobiah Rex:** That's pretty simple to reason about, in my opinion.

**Tobiah Rex:** Because that's just taking a customer set of defined truths, if you will, and making sure that the narrative that we are producing as a system output include those opinions, really.

**Tobiah Rex:** So that should be easy.

**Tobiah Rex:** That could literally be extracted from, you know, a customer conversation or whatever.

**Tobiah Rex:** Like, what do you feel about this, this, this, about your, you know, whatever.

**Tobiah Rex:** Now, follow brand voice and guidelines.

**Tobiah Rex:** this, this, this, next time.

**Tobiah Rex:** Again, that's just a customer input that we would make sure that we try to represent.

**Tobiah Rex:** I'll go into more depth on how we'll do that.

**Tobiah Rex:** Are useful to the intended audience.

**Tobiah Rex:** That one was the one that really stuck out to me as being a bit ambiguous.

**Tobiah Rex:** So that's the one I felt I wanted to spend a little bit more time on, maybe.

**Tobiah Rex:** Require minimum human edits.

**Tobiah Rex:** That's fair.

**Tobiah Rex:** That's just going to be, I think, a byproduct of how well we sell our zero-shot answer.

**Tobiah Rex:** Like our first output, right?

**Tobiah Rex:** So I think if we do the first three well, the fourth one should take care of itself.

**Tobiah Rex:** This is kind of what I'm saying.

**Tobiah Rex:** Editors are available but expensive.

**Tobiah Rex:** Yeah, that's sort of complementary to number four, I think.

**Tobiah Rex:** Sources may be noisier or contradictory.

**Tobiah Rex:** That just is more evidence to me that this is a sales pitch more than it is trying to prove objectively correct answers.

**Tobiah Rex:** But I would assume that there's literature.

**Tobiah Rex:** Sure.

**Tobiah Rex:** Thank

**Tobiah Rex:** Or some type of corpus from the customer that is informing our subjective narrative as a system output.

**Tobiah Rex:** You own this system.

**Tobiah Rex:** Okay.

**Tobiah Rex:** So context size, latency, and costs all matter.

**Tobiah Rex:** Yeah.

**Tobiah Rex:** Okay.

**Tobiah Rex:** So I have the strong opinion in other system designs that latency should not be a first-order concern.

**Tobiah Rex:** At least it wasn't at play, and this was a hard sell, but I think I eventually proved it.

**Tobiah Rex:** Just because the human standard of acceptance right now over voice-to-voice conversations is so bad, I'll stay on the phone for an hour as long as when I hang out my problem solved.

**Tobiah Rex:** And as long as an agent can start there, there's always going to be room to improve that over time, and that's going to feel like the iPhone yearly update to the customer.

**Tobiah Rex:** In this scenario, latency, I guess I would need to know a little bit more about the user experience from...

**Tobiah Rex:** ...

**Tobiah Rex:** ...

**Tobiah Rex:** ...

**Tobiah Rex:** What Gather is offering the user as a UI or, you know, what the workflow for our customers are to know how to manage latency better.

**Tobiah Rex:** I think I'm a little, it's a bit opaque for me right now, so I'm going to not pretend.

**Ben Church:** Yeah.

**Ben Church:** I can expand on that.

**Ben Church:** You can feel free to ask me any questions about, like, the criteria around it.

**Ben Church:** So let's assume we'll take, like, GrowthX, like, verbatim, right?

**Ben Church:** So we, the company, what this system is going to be implemented for is an agency that does this work for multiple clients.

**Ben Church:** So we have editors, we have engineers, we own this pipeline end-to-end, and essentially a customer comes to us and says, I want you to make us a bunch of long-form articles, do it.

**Ben Church:** And they're not interfacing with the system at all.

**Ben Church:** It's more or less our engineers, our content editors, our content, you know, directors, feeding the inputs into the system and seeing the articles come out.

**Tobiah Rex:** So, okay.

**Tobiah Rex:** So, okay.

**Tobiah Rex:** Is it a good mock scenario to say that we'll just assume that we had that discussion you just explained over like a phone conversation and that's all the input we're going to take from that?

**Tobiah Rex:** And then we got to make the magic from that point.

**Tobiah Rex:** Is that a good question?

**Ben Church:** That's a good question.

**Ben Church:** So I would say it's fair to say that prior to us using the system for a client, we've had a conversation with them.

**Ben Church:** And we've talked through what are their, what does their company do?

**Ben Church:** What are their, what is their brand?

**Ben Church:** What is their writing style?

**Ben Church:** And, you know, what type of content do they want to create?

**Ben Church:** We have all that on hand for our customer.

**Tobiah Rex:** Yeah.

**Tobiah Rex:** So, okay, great.

**Tobiah Rex:** And then the way I would conduct that discussion structurally to get what I need as an engineer is I would come to that conversation with a predefined list.

**Tobiah Rex:** What I think are good answers to these questions and really trying to not pull from them as much as I would push to them, but then give them the option to always pull from me or push to me and overwrite my push, if that makes sense.

**Tobiah Rex:** So the way I would do that is I would say, you know, we did some preliminary, you know, look at what you guys have on like your website and some blogs that we found, and we did just like an initial first pass of what your guys' sort of narrative is as a company, and we have kind of something there, and we were wondering if you maybe want to validate that as like an initial thing.

**Tobiah Rex:** If you don't want to do that, and you just trust that your literature and your narrative is already out there at those destinations, then it sounds like we're already kind of aligned.

**Tobiah Rex:** But if you think that there's other sources of narrative from your perspective that you want to make sure that we include, then we're totally open to it.

**Tobiah Rex:** To getting that from you.

**Tobiah Rex:** So that's kind of, that would be my approach to that.

**Tobiah Rex:** The point is, is that we really need to get their subjective perspective concretely in a corpus of documents.

**Tobiah Rex:** So the question is just, what should we include?

**Tobiah Rex:** What shouldn't we include?

**Tobiah Rex:** Okay, so let's assume that we do that.

**Tobiah Rex:** We have all of that now.

**Tobiah Rex:** We've collected the corpus of documents.

**Ben Church:** Yeah.

**Ben Church:** What would be in that corpus of documents?

**Ben Church:** What's your inputs here?

**Tobiah Rex:** Yeah, so that's definitely, yeah.

**Tobiah Rex:** So typically in these scenarios, I try not to rely on intuition as much as I try to rely on pattern matching of frameworks from maybe related or orthogonal sources.

**Tobiah Rex:** So in this case, I think it would be interesting to start with.

**Tobiah Rex:** My intuition is leading me towards a framework and the framework will define my steps.

**Tobiah Rex:** that's the Thank you.

**Tobiah Rex:** So have you ever read a book called The Four Tendencies by Gretchen Rubin?

**Tobiah Rex:** You know what I'm talking about?

**Tobiah Rex:** haven't.

**Tobiah Rex:** Okay.

**Tobiah Rex:** So this is a fascinating framework.

**Tobiah Rex:** So the framework basically outlines human personalities in four regions.

**Tobiah Rex:** And I'll write this down.

**Tobiah Rex:** So basically you have something called an upholder.

**Tobiah Rex:** And then you have orthogonal to that or, you know, say opposite of that, you have a rebel.

**Tobiah Rex:** And then over here you have an obliger at the East Pole.

**Tobiah Rex:** And then at the West Pole you have a questioner.

**Tobiah Rex:** And the point is that there are two dimensions to this framework.

**Tobiah Rex:** Up here is outside.

**Tobiah Rex:** It's all about outside and inside expectations.

**Tobiah Rex:** Outside, expectations.

**Tobiah Rex:** And then inside, expectations.

**Tobiah Rex:** Inside, expectations.

**Tobiah Rex:** And then you have something about acceptance or rejection.

**Tobiah Rex:** Acceptance and Rejection.

**Tobiah Rex:** So, for example, we'll say that a rebel is someone who rejects outside and inside expectations.

**Tobiah Rex:** An upholder accepts or upholds outside and inside expectations.

**Tobiah Rex:** The questioner is all about upholding inside, and the obliger is all about upholding outside.

**Tobiah Rex:** Does that sort of intuition make sense?

**Ben Church:** Okay.

**Ben Church:** Yeah, I like the framework.

**Tobiah Rex:** I'm curious to see.

**Tobiah Rex:** So let's see if we can pattern match it.

**Tobiah Rex:** Yeah.

**Tobiah Rex:** So the application would be as a company, like a company is in essence like an organism, a social organism that is trying to interact with the social environment.

**Tobiah Rex:** And since we're in a subjective world, that is even more true, right?

**Tobiah Rex:** Your go-to-market strategy is all going to be about how you sell yourself as an organization, the same way a human would sell themselves.

**Tobiah Rex:** And so the question is, what message do you want to send?

**Tobiah Rex:** Are you a culture of move fast and break things?

**Tobiah Rex:** You're probably going to be more of a rebel.

**Tobiah Rex:** If you're a culture of pristine lack of risk-taking, like a fintech company, you're going to be an upholder.

**Tobiah Rex:** If you're a customer service company, you're going to be an obliger.

**Tobiah Rex:** If you're a cutting-edge research lab, you're probably going to be a questioner.

**Tobiah Rex:** So the question is, what kind of customer are you and where do you fit in this matrix?

**Tobiah Rex:** And then that is going to be a way that we can put implicit guardrails on the LLM trips that we ask it to produce certain inferences.

**Tobiah Rex:** Because as long as we can give it a concrete definition that is not necessarily just per our own opinion as engineers, but per an outside objective framework, we can get certain guarantees.

**Tobiah Rex:** And it's all about the guarantees in these environments, in my opinion.

**Tobiah Rex:** Where can you find and extract a concrete guarantee for your system?

**Tobiah Rex:** And because we're in this super non-deterministic...

**Tobiah Rex:** Those are like the number one things that I usually look for first.

**Tobiah Rex:** So this is really, I mean, in the context of this really short timeline, this is the first thing I would reach for.

**Tobiah Rex:** And so that gives us now a really interesting way to confidently move forward, I think.

**Tobiah Rex:** So following brand voicing guidelines.

**Tobiah Rex:** So the next thing I would do is I would take the corpus of documents.

**Tobiah Rex:** I would run it through, this is probably where I should start drawing physical system components.

**Tobiah Rex:** So, okay, so we have a corpus of documents, let's say.

**Tobiah Rex:** And this is just like a DB of corpus or, I don't know, original corpus.

**Tobiah Rex:** And then I tend to build these things middle out, like, or bottom up, you can say.

**Tobiah Rex:** so I'm going to start with, like, the most obvious parts and then add on the...

**Tobiah Rex:** the necessary parts.

**Tobiah Rex:** So there's got to be like a first step is to get a, it's almost like, it's like an intent, like if a customer is on a phone call and they were talking to the play system, the way that the first thing I had to build was an intent matching engine, right?

**Tobiah Rex:** And this is a similar pattern where you take in some unstructured input and you match it to something that you know that you can do.

**Tobiah Rex:** So we have our framework.

**Tobiah Rex:** So we're going to call this like maybe a customer narrative matching engine or something.

**Tobiah Rex:** Or let's say it's, let's see, Gretchen Rubin for tendencies, like a tendency.

**Tobiah Rex:** Yeah, let's call it a tendency matching engine, tendency matching engine.

**Tobiah Rex:** And then what this is going to do is it's going to take in, it's going to scan in documents and there's needs to be, you know, some type.

**Tobiah Rex:** Of concrete limitation on how much of that, how many documents we parse at any given time, but basically it's like an initial first scan.

**Tobiah Rex:** So maybe it's, I would start with something like maybe a React pattern where I have like, I have a prompt set up such that, I'm just sort of enumerating now, I'm not sure exactly which one I like most, but React is really easy to start with.

**Tobiah Rex:** The system prompt would describe the Gretchen Rubin framework.

**Tobiah Rex:** would describe that we have this MCP endpoint that the system can call.

**Tobiah Rex:** So there's like a backend system here, let's call it.

**Tobiah Rex:** This is our API layer with MCP endpoints.

**Tobiah Rex:** And maybe one of those endpoints is get documents.

**Tobiah Rex:** Get Doc.

**Tobiah Rex:** Doc.

**Tobiah Rex:** Doc.

**Tobiah Rex:** Doc.

**Tobiah Rex:** And then limit equals, I don't know, 10.

**Tobiah Rex:** And that is going to be how the agentic system can dynamically and systematically iterate over.

**Tobiah Rex:** Wow, mixing this up.

**Tobiah Rex:** That's how it can pull in documents in a systemized way, systematic way.

**Tobiah Rex:** So the tendency matching engine is a service, and it has access to this API layer that will pull in the documents.

**Tobiah Rex:** The API layer calls another system to do that, which is going to be our, I don't know, doc service.

**Tobiah Rex:** And it's really...

**Tobiah Rex:** really...

**Tobiah Rex:** It's really...

**Tobiah Rex:** ...

**Tobiah Rex:** ...

**Tobiah Rex:** ...

**Tobiah Rex:** ...

**Tobiah Rex:** This guy over here is talking to this guy here, and yeah, so we have like an in-house API layer, two services.

**Tobiah Rex:** A tendency matching engine is going to have, yeah, so then it's not, it's got a, need an orchestration layer.

**Tobiah Rex:** So we're going to have an orchestrator here, and this is probably the tendency matching, oops, let's call it a tendency matching controller, and that is sort of the engine, and the controller is orchestrating these services.

**Tobiah Rex:** The service on this side now.

**Tobiah Rex:** Come on, is going to have like a framework service, framework service.

**Tobiah Rex:** And the logic for composing this workflow lives here.

**Tobiah Rex:** Composes workflow, which is going to pull docs, push into framework definition, and then pull from LLM a thesis about tendency, or let's say narrative.

**Tobiah Rex:** Let's say narrative.

**Tobiah Rex:** There it is.

**Tobiah Rex:** So the output of this set of two services, one controller, and this data layer is to...

**Tobiah Rex:** Output a narrative about our customer and the customer's tendencies relative to this framework.

**Tobiah Rex:** So now we have a narrative outline, and all future work must abide by the output that that tendency matching controller produces as an output.

**Tobiah Rex:** So let me think about this for a second.

**Tobiah Rex:** I'm going to add a little bit more structure here.

**Tobiah Rex:** This is a data layer.

**Tobiah Rex:** I tend to think in domain-driven development, just so you know.

**Tobiah Rex:** There's probably a repo layer that sits between the service and the data layer.

**Tobiah Rex:** So I'd say that there's a, there's a doc, there's like a customer, maybe I'd call it customer corpus repo.

**Tobiah Rex:** perfect.

**Tobiah Rex:** Okay.

**Tobiah Rex:** .

**Tobiah Rex:** I think, and that is actually the ORM wrapper around the data layer.

**Tobiah Rex:** I actually hate ORMs.

**Tobiah Rex:** I go for, I usually go for SQL C, which I don't know if you've heard of that or whatever, but it's, yeah, it dynamically, well, first it allows you to write SQL C file, SQL files.

**Tobiah Rex:** So you write raw SQL, the best, most declarative language you've ever come up with.

**Tobiah Rex:** And according to, what's his name?

**Tobiah Rex:** Design, designing data intensive application book.

**Tobiah Rex:** Anyways, he had, he makes that assertion in book.

**Tobiah Rex:** Yeah, but you can write raw SQL and then SQL C will parse the raw SQL and convert it into either Python app layer bindings dynamically, automatically, or Golang.

**Tobiah Rex:** And so you can actually get all of the.

**Tobiah Rex:** of if short文,

**Tobiah Rex:** Typing and application layer definitions for free out of the box, and you can just worry about that.

**Tobiah Rex:** It's amazing.

**Tobiah Rex:** So anyway.

**Tobiah Rex:** I'll forward you on some stuff on that afterwards.

**Ben Church:** Okay.

**Ben Church:** Project you might find interesting.

**Ben Church:** So while I'm looking at this, I'm going to say we're at the halfway point.

**Ben Church:** I'm going to interject with just some clarifying questions and see.

**Ben Church:** So remember, we own the start and end of the system holistically, right?

**Ben Church:** Like we have basically someone employed by this company at the beginning, and someone employed more or less at the end, right?

**Ben Church:** Someone has to hit that button to say publish to Webflow.

**Ben Church:** Same way someone has to hit the button to say, okay, go make me an article.

**Ben Church:** So where are the ins and outs around this?

**Ben Church:** I know you're kind of building middle out on that.

**Tobiah Rex:** I'm just saying, Totally fair question.

**Tobiah Rex:** To me, this part that we've just designed is the...

**Tobiah Rex:** Is the narrative production, which is the foundational step.

**Tobiah Rex:** We haven't even gotten to like building out the actual article flow yet.

**Tobiah Rex:** So this is just us establishing a concrete set of guarantees of how we are going to measure ourselves from here on out, right?

**Tobiah Rex:** So like anything that we produce from this point, we got to go back to this output that we just created and say, does it fit with that narrative?

**Tobiah Rex:** Now, honest to God, at the end of this tendency matching controller, I would get back on the phone call with a customer and I would ask them to validate this output if they would be willing.

**Tobiah Rex:** Now, if part of our, you know, whatever customer relationship is to just not do that right now, I get that.

**Tobiah Rex:** Maybe we skip it, whatever.

**Tobiah Rex:** But the point is that this is fundamental.

**Tobiah Rex:** Okay.

**Tobiah Rex:** So let's say that this is working.

**Tobiah Rex:** They accept whatever.

**Tobiah Rex:** The next step is, are useful to the intended audience.

**Tobiah Rex:** Right.

**Tobiah Rex:** So the intended audience, we need to figure out who that is.

**Tobiah Rex:** And now I would assume that the company has figured out who their audience is and they've sort of tailored their tendency bias to that particular type of customer.

**Tobiah Rex:** Now, if what comes out of this tendency matching controller process is something that the customer doesn't align with or agree with, to me, that's a side effect that the customer doesn't have a clear tendency definition.

**Tobiah Rex:** Right.

**Tobiah Rex:** They're too ambiguous about that.

**Tobiah Rex:** And that would inevitably create the problem of us not knowing how to be useful to the intended audience.

**Ben Church:** So for us, it's true.

**Ben Church:** And their, their tendency and their target audience can, can change.

**Ben Church:** So there you go.

**Ben Church:** You know, they're your enterprise customer, say for zoom is a different.

**Ben Church:** Profile and a different target than your startup or single developer or therapist one.

**Ben Church:** So their intended target changes basically content to content.

**Ben Church:** They typically have a preset list of their types of targeted audience and targeted potential customers, but they do shift content to content.

**Tobiah Rex:** So what that sounds like then is that we need to, in a P1 or something, modify the tendency matching engine to produce maybe multiple outputs.

**Tobiah Rex:** Meaning that in the scenario where our intended audience is X, our narrative perspective should be X prime.

**Tobiah Rex:** If it's our intended audience is Y, we need to come from a Y prime narrative source location, so to say, or mindset.

**Tobiah Rex:** But yeah, so I think you can kind of maybe see the writing in terms of how we'll solve, or I think we could solve intended audience matching.

**Tobiah Rex:** It's just really coming back down to we need to start as a company narrative from the right location to ensure that we're going to target the right audience as an implicit side effect, right?

**Tobiah Rex:** Or as a reaction, like just chemical reaction is kind of where my mind is going.

**Tobiah Rex:** Okay, so now for the actual document, production.

**Tobiah Rex:** So there, okay, to start with for publishing articles, long form draft articles.

**Tobiah Rex:** Okay, so is the question, is the customer expecting us to come up with the theses for these articles?

**Tobiah Rex:** Or do they have messages that they want us to put a body and color and dress it up in?

**Ben Church:** I think for this, you can assume the customer has a proxy at the company called like, let's call them a content editor, who sets up the strategy for them.

**Ben Church:** And that content editor is kind of our translation layer between, hey, the customer wants to rank higher for, let's say they're Zoom and they want to rank higher for a Zoom enterprise or video conferencing enterprise.

**Ben Church:** And that content editor is taking that wish from the client and transforming it into, oh, we need more articles on this topic, targeting this brand persona, right?

**Ben Church:** Using these writing guidelines that I know about the customers.

**Tobiah Rex:** Okay.

**Tobiah Rex:** Would you, would you, to me, that sounds very like, like the, the most intuitive pattern match in my brain is like an SEO driven pipeline or something.

**Tobiah Rex:** if I'm.

**Ben Church:** I'm.

**Ben Church:** I'm.

**Tobiah Rex:** Yeah, that seems okay.

**Tobiah Rex:** Okay, so then we have a targeted list of the impact that we want to generate as a customer that we're giving to GrowthX.

**Tobiah Rex:** Is that fair to say?

**Ben Church:** Yeah, I'd say that's fair to say.

**Ben Church:** And then you, in this process, as an engineer designing the system, you can kind of set the inputs you need from the content editor.

**Ben Church:** Because you're not necessarily directly pulling it from a customer, and you don't have to force a customer to do anything.

**Ben Church:** It's up to this content expert who's like, I'm a content expert, and I'm trying to help out this company create some kind of content with some underlying intent of moving the needle.

**Ben Church:** I will say, like, you're hitting on something that's interesting that I'll ask about here in a little bit, which is like, you know, how do you evaluate these systems, right?

**Ben Church:** How do you know that they're producing content that hits some measure of quality, whether that's...

**Ben Church:** That's, you know, adhering to brand guidelines or just ranking higher on SEO.

**Ben Church:** But I'll leave that aside.

**Ben Church:** I'm just giving you a sneak preview on that kind of thing.

**Tobiah Rex:** Gotcha.

**Tobiah Rex:** Okay.

**Tobiah Rex:** I realized when you were talking, I left out the LLM part.

**Ben Church:** That's all good.

**Tobiah Rex:** That's all good.

**Tobiah Rex:** Yeah.

**Tobiah Rex:** I'd probably start with a React pattern or something.

**Tobiah Rex:** The other ones that I think come to mind could be, like, plan and execute would probably be good.

**Tobiah Rex:** Predefining a set of steps of documents that we feel go together.

**Tobiah Rex:** There could be, like, there could be some ideas of, you know, sub-batching docs that feel, or subjectively, according to the LLM's output, semi-belonged together, that feel similar.

**Tobiah Rex:** Yes.

**Tobiah Rex:** Anyways, my point is, is that there's a, there's a sub, there's maybe a subsystem expression that basically solves the problem of organizing the documents, yeah, as like a pre-step to producing narrative.

**Tobiah Rex:** Okay.

**Tobiah Rex:** Okay, so the key entity that you invoked in your answer there that stuck out to me was, I think you called it, what'd you call it?

**Tobiah Rex:** Content expert?

**Tobiah Rex:** Is that what you said?

**Tobiah Rex:** Yeah.

**Tobiah Rex:** Yeah.

**Ben Church:** Content editor, content expert.

**Tobiah Rex:** Got it.

**Tobiah Rex:** So I love that.

**Tobiah Rex:** That sounds like a human, but representing that level of agency in our system feels like the right move to me.

**Tobiah Rex:** Uh...

**Tobiah Rex:** Yeah, so the content experts input, I'm going to say content, I'm just going to say expert controller for now, it feels a little weird, but yeah, there's something here.

**Tobiah Rex:** So the input to this controller that would need to come from a database is a customer narrative.

**Tobiah Rex:** So over here in our data model, we need to, I'm going to just sort of DB entities.

**Tobiah Rex:** So we have, it's a little fuzzy, to be fair, but on the horizon, I can see a customer narrative entity.

**Tobiah Rex:** And then that schema, yeah, we could spend a lot of time on that, but let's just assume that we feel like we're confident about that that should exist.

**Tobiah Rex:** The input, that becomes the input.

**Tobiah Rex:** The content expert controller workflow.

**Tobiah Rex:** So the content expert controller is gonna go pull.

**Tobiah Rex:** Let's see.

**Tobiah Rex:** It's gonna pull from that.

**Tobiah Rex:** We need to use that.

**Tobiah Rex:** So let me think.

**Tobiah Rex:** We pull that in.

**Tobiah Rex:** And then we have, in another DB entity, I would assume, we have some targeted, we have like a target, target audience, probably.

**Tobiah Rex:** And, but then with a target audience, the edge that connects a narrative to an audience is a message or something, something specific that we want to say to that audience.

**Tobiah Rex:** So that would be.

**Tobiah Rex:** Um, customer narrative, topic.

**Tobiah Rex:** Let's call it a topic narrative.

**Tobiah Rex:** I like that.

**Tobiah Rex:** Customers, topics, audience.

**Tobiah Rex:** This feels good.

**Tobiah Rex:** So a topic is the thesis that we will build the article around.

**Tobiah Rex:** And the relationship between, uh, so we have a, sorry, I'm trying to go faster.

**Tobiah Rex:** Um, so we have a narrative, customer narrative, which should produce topics.

**Tobiah Rex:** And the, uh, topics need to have some type of relationship to an audience.

**Tobiah Rex:** Um, so an audience, the owner, let's say of an audience, uh, is a customer.

**Tobiah Rex:** Um, and the, uh, owner of.

**Tobiah Rex:** Topics is also a customer, a narrative, I should say.

**Tobiah Rex:** All right.

**Tobiah Rex:** Yeah.

**Tobiah Rex:** Yeah.

**Tobiah Rex:** A customer lives atop a narrative.

**Tobiah Rex:** Right.

**Tobiah Rex:** And yeah, so that makes sense.

**Tobiah Rex:** Every narrative should have an audience.

**Tobiah Rex:** Every narrative can have topics.

**Tobiah Rex:** Every topic can have articles.

**Tobiah Rex:** Uh, so there's a natural branching strategy here that I'm starting to see.

**Tobiah Rex:** Um, and the target audience, ooh, that's an interesting question.

**Tobiah Rex:** One-to-one or one-to-many?

**Tobiah Rex:** Um, it feels like the better the narrative, the less audience you have.

**Tobiah Rex:** Um, unless your intention is to be very appealing to, like, so that's an interesting question.

**Ben Church:** But, um, so.

**Ben Church:** So there's an interesting, so there's one that is interesting and fun for me and painful in a way because this interview script, you're my first person going through it.

**Ben Church:** I knew it was going to be, could be like longer.

**Ben Church:** So I want to say you're doing just fine.

**Ben Church:** I'm going to switch to ask some probing questions just to condense it and pull some information out.

**Ben Church:** So you're right on the money here when you're kind of like making this hierarchy and kind of like these extra inputs that come after, right?

**Ben Church:** You can imagine the content expert, like you're showing here, gives you a narrative and a topic and an audience, right?

**Ben Church:** Out of there, you're seeing the explosion of things to consider.

**Ben Church:** And right at the end here, you mentioned articles.

**Ben Church:** So say if you have designed a system like this and you're explaining it back to me, imagine when you ask an LLM to go write an article on a certain topic, that topic...

**Ben Church:** It's pretty dynamic, right?

**Ben Church:** Say, for example, like Webflow could want to write an article about video codecs or state-of-the-art video LLM models, right?

**Ben Church:** So in a system like this, what would you do or add to, say, go and get information on these topics that we might not have in our own database?

**Ben Church:** How does that fit into the pipeline?

**Tobiah Rex:** Yeah, we need a research pipeline.

**Tobiah Rex:** And if you don't mind, to expedite, given the interest of time, can I just share with you a research system design that I built in Figma?

**Ben Church:** Yeah, of course.

**Ben Church:** Yeah.

**Ben Church:** Okay.

**Ben Church:** We don't have be constrained by this at all.

**Tobiah Rex:** All right.

**Tobiah Rex:** Let me log in real quick.

**Tobiah Rex:** Hopefully this is super easy.

**Ben Church:** And just now I've got one more question after this one that we can condense down, and then we can switch it over to the reverse interview as well.

**Tobiah Rex:** Okay, for sure.

**Tobiah Rex:** Let me share.

**Tobiah Rex:** Let Let

**Tobiah Rex:** Let me share this.

**Tobiah Rex:** So this is just me being a very curious cat.

**Tobiah Rex:** This is something I've collected and built over the years of getting into this whole flow.

**Tobiah Rex:** This is a research pipeline system design that I built.

**Tobiah Rex:** And yeah, so basically it starts off, there's like an upper loop here that just manages the ability for this to happen dynamically.

**Tobiah Rex:** So that's not really relevant to the current process.

**Tobiah Rex:** But basically the research procedure that the system goes through is it determines a type of answer that we are supposed to generate.

**Tobiah Rex:** It's either, like I said, it's like multi, it's appealing to a large audience or a very niche audience.

**Tobiah Rex:** We create the plan, we get the approval from potentially a supervisory agent that cross-checks it against...

**Tobiah Rex:** Some type of objective criteria.

**Tobiah Rex:** And then we start the research plan.

**Tobiah Rex:** We pull the data.

**Tobiah Rex:** We analyze the data.

**Tobiah Rex:** By analyze, I mean we summarize.

**Tobiah Rex:** We ask questions about the data, given the summary, like, did this piece of data satisfy our need for X, to find X, to find Y?

**Tobiah Rex:** After that, we vectorize the data, which is just a, you know, an atomization process.

**Tobiah Rex:** Yeah.

**Tobiah Rex:** And then in this design, I had a knowledge graph.

**Tobiah Rex:** I felt like knowledge graphs are the fastest.

**Tobiah Rex:** This is something I learned at Ario, where, you know, it's like buckshot, hunting with buckshot or hunting with a sniper rifle.

**Ben Church:** So that's, I think, the intuition is there.

**Tobiah Rex:** Okay.

**Tobiah Rex:** And then we have to make a determination if the data that we found and we did all of this for is answering our, is an answer to our goal.

**Tobiah Rex:** And if it is, then we can move on.

**Tobiah Rex:** If it isn't, we got to reset.

**Ben Church:** The question I have in here is like, this makes sense from like, you're going out and finding research and coming back.

**Ben Church:** In this plan that you have, is there any feedback loop in here around confirming the research itself is correct?

**Ben Church:** So the reason I'll give you the preview why I asked that question is, we have found in many of our systems, you know, those hallucinations creep in.

**Ben Church:** And often we can get like, bad links inserted into articles or facts that are not facts or facts that never existed in the source material.

**Ben Church:** So I'm just, I'm curious, like in this one to kind of like skip ahead.

**Ben Church:** Have you encountered that yourself?

**Ben Church:** And if not, that's okay.

**Tobiah Rex:** just wanted to see.

**Tobiah Rex:** be honest, I haven't.

**Tobiah Rex:** I haven't.

**Tobiah Rex:** So the closest I've got to this problem was when I built this system that a customer could show up to, ask the system a question, and the system was supposed to only look at a very bespoke set of corpus documents that are generated by that person to then answer the question.

**Tobiah Rex:** And so what I learned from that experience was that there's two types of questions the user will always ask.

**Tobiah Rex:** One is objectively answerable, the other is subjectively.

**Tobiah Rex:** Recommendation versus what was the last thing I did on X date.

**Tobiah Rex:** And so the only way you're going to get the objective criteria to be measurable is if you have like a testable data set that you can produce that you know should converge on an objectively correct answer.

**Tobiah Rex:** then just try to make sure that that is always passing and hope that that somehow pattern matches to the use case.

**Tobiah Rex:** And so it's really important for the engineering.

**Tobiah Rex:** To always be questioning whether or not their testing pipeline is, in fact, a good proxy for what the customer's objective answer workflow looks like, right?

**Tobiah Rex:** So that's as close as I've gotten, but that doesn't feel like a good answer to your, like, it doesn't feel like that's a guarantee.

**Tobiah Rex:** Yeah, so it just feels like it's just, it's getting as close as we can.

**Tobiah Rex:** But one pattern that I've picked up over the last six months is adversarial techniques.

**Tobiah Rex:** So you literally try to, you produce an agent, I call it a bug engineer, and its whole entire purpose is to break the system, is to break, is to act like a malicious actor and try to trip it up.

**Tobiah Rex:** And I've found that that is incredibly useful, because your defensive posture immediately just starts to index way more, and that's exactly what...

**Tobiah Rex:** Need in those objective criteria scenarios.

**Tobiah Rex:** So for example, if the malicious agent asked a question that it knows that the system can't answer, does the system respond by saying, sorry, I'm not sure I can get able to answer that question right now, you know, maybe you could, but what I could answer is A, B, C, or D, you know what I mean, like lead them towards a different path than the one that they're trying to go down, because the one that they want to go down, you can't help them.

**Tobiah Rex:** And so does the system act like that?

**Tobiah Rex:** That's just prompt engineering, to be fair, but the bug engineer will help you make sure that those types of phrases are in your system prompts.

**Ben Church:** That's kind of fun.

**Ben Church:** There's like the concept of LOM as a judge, and then there's the concept of like LOM as an evil actor slash judge, right?

**Ben Church:** Because it tries to trick you.

**Ben Church:** It's like an undercover cop.

**Tobiah Rex:** And, you know, the way I came across this idea, I was at a...

**Tobiah Rex:** That bar, actually, and I was talking to this random guy who writes ML pipelines.

**Tobiah Rex:** It's like a machine learning concept where, what is it called?

**Tobiah Rex:** It's game theory, and it's like two opponents are trying to beat each other, and the system just tries to get stronger as a result of that.

**Tobiah Rex:** So, anyways, I thought, why not build that into the system architecture itself?

**Ben Church:** Yeah.

**Ben Church:** So, did you implement an adversarial agent?

**Tobiah Rex:** I have one in a different context.

**Tobiah Rex:** So, what I did as a product of feeling like, despite all these LLM tools, I'm still too slow, is I built something called Overwatch, similar to my military experiences.

**Tobiah Rex:** So, this is my Overwatch system.

**Ben Church:** I don't know if you can see this.

**Tobiah Rex:** Yeah, that's good.

**Tobiah Rex:** Yeah.

**Tobiah Rex:** So, basically, what it does is it carves out, so I can add projects here.

**Tobiah Rex:** And these projects are just code bases.

**Tobiah Rex:** And then atop these code bases, this system lives in a different location.

**Tobiah Rex:** But what it can do is it – I can instantiate roles.

**Tobiah Rex:** And these roles are just bespoke roles.

**Tobiah Rex:** And then these roles take on a very specific type of level of responsibility.

**Tobiah Rex:** And, like, the bug engineer here can – I think my server's not on right now.

**Tobiah Rex:** But basically, there's a role definition.

**Tobiah Rex:** I can maybe actually pull it up for you if you want.

**Tobiah Rex:** Bug engineer.

**Tobiah Rex:** Role.

**Tobiah Rex:** Yeah.

**Tobiah Rex:** Open preview.

**Tobiah Rex:** Yeah.

**Tobiah Rex:** So it's just key responsibilities: investigation, diagnosis, proactive code-based quality assurance, and basically just trying to poke holes in people's work on the team.

**Tobiah Rex:** And, yeah, so this has been amazing. Basically what I'll do now is I have an architect in here that actually builds out, like, a ticketing structure in my own data layer, and he's coordinating and carving out work requests for all these different roles and then assigning them.

**Tobiah Rex:** And then the actors go and they do their job.

**Tobiah Rex:** And then the bug engineer goes in and he observes what they do, and then he qualifies that work as being passed or not.

**Tobiah Rex:** And typically what happens is that they come up with an output called gaps.

**Tobiah Rex:** And these gaps are just logical, you know, fallacies or whatever.

**Tobiah Rex:** That's been really great.

**Tobiah Rex:** Really cool.

**Ben Church:** So we've got five minutes left.

**Ben Church:** We can switch into a reverse interview.

**Ben Church:** I've got maybe 10 minutes I can go over if there's an additional question I could ask, or we can just switch over.

**Tobiah Rex:** I'd say I'd leave it up to you.

**Tobiah Rex:** Yeah, sure.

**Tobiah Rex:** I actually...

**Tobiah Rex:** So I do have like a structure on this that maybe help us go a little bit organized.

**Tobiah Rex:** So I'll just paste in these questions.

**Tobiah Rex:** So my first question is usually this one.

**Tobiah Rex:** It's a multiple choice question.

**Tobiah Rex:** And if you don't like the option, they're all subjective.

**Ben Church:** They're meant to be subjective.

**Ben Church:** So if no problem, let me do two things.

**Ben Church:** I'm going to turn off the recording because I think it's always fair if I can turn this off.

**Tobiah Rex:** And then, you know, I'm giving you as much unfiltered as I can.

**Tobiah Rex:** Oh, that's cool.

**Ben Church:** I'm in a new app. We use Fathom, which wraps Zoom. Zoom's already hard enough from a UX perspective.

**Ben Church:** There it is.

**Ben Church:** Yeah, there you go.
