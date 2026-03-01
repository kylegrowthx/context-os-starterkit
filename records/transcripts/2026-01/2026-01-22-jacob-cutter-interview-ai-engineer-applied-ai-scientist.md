# Jacob Cutter - Interview | AI Engineer (Applied AI Scientist)

<metadata>
date: 2026-01-22
time: 20:28 UTC
duration: 64 minutes
organizer: katja@growthx.ai
participants:
  - name: Katja Wittfoth
    email: katja@growthx.ai
    affiliation: GrowthX
  - name: Jacob Cutter
    affiliation: Salesforce (AgentForce, Tenex acquisition)
fathom_recording_id: 116498195
fathom_url: https://fathom.video/calls/542308999
share_url: https://fathom.video/share/Gaav_wyScK6zxGkjXz2vabZY4T9A7bbv
source: fathom
enriched_on: 2026-02-28 17:30 UTC
</metadata>

---

## Summary

Jacob Cutter, tech lead for Salesforce's AgentForce voice agent reasoner, discussed applying his experience in low-latency ASR and agentic workflows to GrowthX's content quality challenges. He proposed a systematic approach using LLM-as-judge evaluation and iterative content regeneration to measure and improve marketing output quality, while also exploring brand visibility strategies for LLM search results.

---

## Context

Jacob Cutter brings deep expertise in building production AI systems at scale. At DeepGram (3.5 years), he specialized in low-latency ASR models for domain-specific use cases and led a patent-pending transformer architecture project. His work at Tenex and subsequent role as tech lead for Salesforce's AgentForce voice product exposed him to end-to-end agentic workflows including prompting strategies, RAG integration, tool-calling architectures, and voice-specific optimization challenges like interrupt handling and low-latency inference.

GrowthX faces a parallel challenge: how to systematically measure and improve the quality of AI-generated marketing content at scale. Cutter's background in evaluation frameworks (from particle physics signal detection through to LLM-as-judge scoring) provides a direct pathway to solving this problem through an agentic feedback loop.

---

## Relevance

**For Applied AI Scientist Role:**
- Directly applicable experience designing LLM-as-judge evaluation systems
- Proven ability to architect agentic workflows with feedback loops
- Track record of optimizing performance (latency, accuracy, cost) in production systems
- Deep familiarity with prompt engineering, RAG, and tool-calling at Salesforce scale

**For Content Quality Framework:**
- Proposes testable metrics (conciseness, specificity, grammar, tone, factual grounding)
- Agentic approach allows targeted regeneration of specific pipeline stages
- Evaluation-driven iteration aligns with GrowthX's engineering culture

**For LLM Search Visibility Strategy:**
- Practical cost optimization (AI Overviews scraping vs. direct API calls)
- Empirical approach recognizing LLM ranking volatility
- Comparative analysis framework (reverse-engineer top-performing content)

---

## Overview

- **Relevant Experience:** Jacob Cutter's background in low-latency ASR (DeepGram) and building Salesforce's voice agent (AgentForce) directly applies to GrowthX's need for a robust, high-quality content generation pipeline.
- **Proposed Solution:** To measure and improve content quality, Cutter suggested an agentic workflow using an "LLM as a judge." This system would score content on criteria like tone and factual grounding, then loop back to regenerate specific pipeline stages for targeted improvement.
- **Role Alignment:** The proposed solution aligns perfectly with the Applied AI Scientist role, which requires defining a quality evaluation framework, building the technical roadmap, and implementing the necessary platform changes.

---

## Key Topics

### Candidate Background

  - **Education:** PhD in experimental particle physics, focusing on signal-to-noise analysis for dark matter detectors.
  - **DeepGram (3.5 years):**
      - Built dozens of ASR models for specific use cases (e.g., phone calls).
      - Led a skunkworks project to develop a patent-pending, low-latency transformer ASR architecture, significantly boosting accuracy.
      - Built PyTorch pipelines for post-processing models to improve punctuation.
  - **Tenex (6 months):**
      - Worked on end-to-end voice agents (ASR, TTS, LLMs) with a strong focus on low latency for natural conversation.
      - Acquired by Salesforce.

### Salesforce: AgentForce Voice Agent

  - **Project:** Tech lead for the "reasoner" service, the "brain" of Salesforce's GA voice agent.
  - **Problem:** The existing text-based agent was too slow and lacked voice-specific logic (e.g., handling interrupts).
  - **Solution:** Built a new agentic workflow from scratch, optimized for low latency and natural conversation.
  - **Key Components:**
      - **Prompting:** Guardrails, dynamic context updates, and voice-specific output formatting.
      - **RAG:** Integrates customer-provided knowledge bases (chunked docs, embeddings) via Salesforce Data Cloud.
      - **Tool Calling:** Enables agents to execute actions in the Salesforce backend.
      - **Entity Confirmation:** A mechanism for slot filling and verifying spoken details (e.g., email addresses) before action execution.

### Case Study 1: Content Quality Scoring

  - **Goal:** Design a system to systematically score and improve the quality of AI-generated marketing content.
  - **Proposed Metrics:**
      - **Core Attributes:** Conciseness, specificity, grammar, readability.
      - **Marketing-Specific:** Tone, use of appropriate buzzwords, grounding in customer context, factual accuracy.
  - **Proposed System:**
      - **Method:** Use an "LLM as a judge" to score content against the defined criteria.
      - **Process:**
        1.  **Evaluate:** Score content on each metric.
        2.  **Loop:** If scores are low, regenerate the content.
        3.  **Refine:** Update prompts or context to improve future outputs.
      - **Implementation:** Integrate this evaluation loop into the existing agentic content pipeline, allowing for targeted regeneration of specific stages (e.g., a tone rewrite).

### Case Study 2: LLM Search Visibility

  - **Goal:** Measure and improve a brand's visibility in LLM search results (e.g., ChatGPT, Gemini).
  - **Proposed Measurement Strategy:**
      - [**Method:** Simulate user queries by sending template prompts to LLMs (e.g., "What is the best \[product\] for \[use case\]?").](https://fathom.video/share/Gaav_wyScK6zxGkjXz2vabZY4T9A7bbv?tab=summary&timestamp=3081.0)
      - **Analysis:** Count brand mentions in the LLM's responses to create a statistical ranking of visibility.
      - **Cost Optimization:** Scrape AI Overviews from Google Search results to get free LLM summaries, avoiding direct API costs.
  - **Proposed Improvement Strategy:**
      - **Analysis:** Compare the content features of high-visibility brands (using the quality metrics from Case Study 1) against the client's content.
      - **Action:** Adjust the content generation pipeline to match the features of top-ranked content.
      - **Caveat:** This is an empirical process requiring A/B testing, as LLM search mechanisms vary and evolve.

---

## Action Items

- **Katja Wittfoth (GrowthX):** Discuss the interview with the team and follow up with Jacob Cutter (Salesforce).

---

## Transcript
**Katja Wittfoth:** Hi, Jacob.

**Katja Wittfoth:** This meeting is being recorded.

**Jacob Cutter:** Hi there.

**Katja Wittfoth:** How's it going?

**Katja Wittfoth:** Good.

**Katja Wittfoth:** You're also one of those people who are coming to the meeting earlier, right?

**Katja Wittfoth:** Yeah, I guess so.

**Katja Wittfoth:** Same for me too.

**Jacob Cutter:** Yeah.

**Jacob Cutter:** Yeah.

**Jacob Cutter:** And I just wanted to start by saying, you know, apologies for rescheduling.

**Jacob Cutter:** I had a little bit of a medical issue last weekend, so I'm still recovering, but happy to talk to you.

**Katja Wittfoth:** No worries at all, and I hope you feel better.

**Katja Wittfoth:** Yeah, let me know if you need anything during the interview.

**Katja Wittfoth:** So for today, the plan is to chat really more about you and your previous projects and work.

**Katja Wittfoth:** We'd love to, you know, understand your background more, learn more about you.

**Katja Wittfoth:** So, we will also, I'd like also to...

**Katja Wittfoth:** Thank you.

**Katja Wittfoth:** you.

**Katja Wittfoth:** So deeper into one of your projects, probably one of the recent ones.

**Katja Wittfoth:** And then I have a small growthx study I'd like to discuss with you.

**Katja Wittfoth:** My name is Katja.

**Katja Wittfoth:** So I'm an advisor, data advisor for growthx.

**Katja Wittfoth:** And I'm helping currently with hiring.

**Katja Wittfoth:** So Danielle asked me to interview Peter Rose.

**Katja Wittfoth:** And I'm also helping with a visibility study we are running.

**Katja Wittfoth:** So that's why I'm glad to meet you today and go for this interview.

**Jacob Cutter:** Yeah, likewise.

**Katja Wittfoth:** I'm glad to talk to you.

**Katja Wittfoth:** Sounds good.

**Katja Wittfoth:** So I'm also just maybe a couple of more words about myself.

**Katja Wittfoth:** So you kind of like know my background and why I'm interviewing you.

**Katja Wittfoth:** I'm a full stack data scientist.

**Katja Wittfoth:** So really in my career, I did a bunch of stuff from, you know, analytics, data engineering to data science, machine learning stuff, and also building LLM's applications.

**Katja Wittfoth:** Right now I work at a full-time at a fintech company.

**Katja Wittfoth:** So that's a little bit about myself.

**Jacob Cutter:** I'd love to hear more about you.

**Jacob Cutter:** Yeah, for sure.

**Jacob Cutter:** So, yeah, I'm a Bay Area kid.

**Jacob Cutter:** I got a PhD in experimental particle physics.

**Jacob Cutter:** So building dark matter detectors, analyzing, you know, the waveforms that the detectors were producing, and kind of processing a lot of the data to search for dark matter signals.

**Jacob Cutter:** So very, very much all about the signal to noise and that kind of thing.

**Jacob Cutter:** I, you know, kind of ramped up a lot of my programming skills and all that kind of stuff.

**Jacob Cutter:** In the physics realm, but kind of pivoted when I graduated to join up with Scott Stevenson, who was also a dark matter physics PhD, and he started DeepGram, which you probably, I don't know if you're familiar, but yeah.

**Katja Wittfoth:** I know that Marcel was working at DeepGram before.

**Katja Wittfoth:** That's why I was like, that's the connection to you.

**Jacob Cutter:** Yeah, and so he had started this DeepGram company, which is, you know, their main thing at the time, especially, was ASR or speech-to-text, you know, providing sort of frontier end-to-end trained models for ASR at sort of the enterprise level.

**Jacob Cutter:** And that's something they were excelling at, and I joined up with them, was there for three and a half years, did like a ton of like R&D work and sort of applied research, like developing new model architectures, training core models that we could ship to product.

**Jacob Cutter:** Um, and basically just honestly doing all kinds of different things.

**Jacob Cutter:** Um, sort of a mixture of what I would call AI engineering and data science.

**Jacob Cutter:** So like a lot of data curation for targeted model training and all that kind of stuff.

**Jacob Cutter:** Um, as well as a lot of evaluation work.

**Jacob Cutter:** I kind of got the itch to do something different.

**Jacob Cutter:** So I went to Tenex, uh, where I was for six months because they got acquired by Salesforce.

**Jacob Cutter:** Um, and at Tenex, we were working on, you know, the end to end voice agents.

**Jacob Cutter:** So voice agents that kind of leverage the different components, speech to text, text to speech, um, uh, in-house trained LLMs, like all that kind of stuff, um, to kind of create a sort of seamless low latency voice agent.

**Jacob Cutter:** Um, and then they got acquired by Salesforce and, um, the big project I've been working on in the last maybe, uh, eight months has been as sort of tech lead on this, um, low latency reasoner, which.

**Jacob Cutter:** So a text-based reasoner that we use for the voice applications in AgentForce.

**Jacob Cutter:** And so voice, we actually went to GA with the sort of full voice product semi-recently a couple months ago.

**Jacob Cutter:** So that was pretty exciting.

**Katja Wittfoth:** Yeah.

**Katja Wittfoth:** Sorry.

**Katja Wittfoth:** So like you're working on a voice agent to like control the sales force?

**Jacob Cutter:** Yes.

**Jacob Cutter:** Through voice or?

**Katja Wittfoth:** Yeah, that would be amazing.

**Jacob Cutter:** Yeah, yeah, yeah.

**Jacob Cutter:** So basically, there's this sort of Salesforce ecosystem, right?

**Jacob Cutter:** Because they already have pretty well-established like software with a lot of customers.

**Jacob Cutter:** And so they're basically CRM, right?

**Jacob Cutter:** Customer Relations Management software.

**Jacob Cutter:** So they store a lot of data about their, sorry, our customers, which are, you know, the enterprises or companies.

**Jacob Cutter:** They obviously have all of their customers.

**Jacob Cutter:** And so what they do.

**Jacob Cutter:** What is they have this software they use to kind of manage customer data.

**Jacob Cutter:** Nowadays, the big thing is AgentForce, which is the sort of agents that do a lot of operations within the Salesforce ecosystem.

**Jacob Cutter:** You could also think about conversational agents that people want to use in their sort of workflows or end users might call in for customer service, right?

**Jacob Cutter:** And instead they get an agent that they chat with over text, right?

**Jacob Cutter:** Instead of a human.

**Jacob Cutter:** And, you there's debate about whatever, you know, like whether people, whether end users want that, right?

**Katja Wittfoth:** Or whether customers want that.

**Jacob Cutter:** And so the goal with AgentForce has been like creating these agents that customers actually want to use, right?

**Jacob Cutter:** And for voice, that's an even bigger challenge because voice is just a very complex and difficult problem.

**Jacob Cutter:** And so basically one thing we were trying to do is sort of expand those conversational agents that could be used for customer service.

**Jacob Cutter:** do is we're we're we're we're we're trying

**Jacob Cutter:** And kind of bring them over to the voice modality, right?

**Jacob Cutter:** So in other words, a next-gen chat interface where you can click a button and suddenly you're talking through the microphone to an agent, to an AI agent, right?

**Jacob Cutter:** And so the agent has to be very natural, conversational, low latency.

**Katja Wittfoth:** How would they, like, basically, we also use Salesforce and I do support actually a revenue team.

**Katja Wittfoth:** Um, because they would need to provide this voice AI to actually customers like my company, right?

**Katja Wittfoth:** And then there will be a lot of, like, contacts needed, right?

**Katja Wittfoth:** Yeah.

**Katja Wittfoth:** For the company.

**Katja Wittfoth:** So that's, like, part of the reg or, like, what is the system behind it?

**Katja Wittfoth:** If you can share a bit more.

**Jacob Cutter:** Oh, I can.

**Jacob Cutter:** Yeah, sorry.

**Jacob Cutter:** I wasn't sure how specific to get.

**Jacob Cutter:** But, um, yeah, so effectively what's going on under the hood is you have this.

**Jacob Cutter:** just, like.

**Jacob Cutter:** So let's say you have a tenant or a customer, one of Salesforce's customers.

**Jacob Cutter:** Let's just take that as an example.

**Jacob Cutter:** So let's say there's a company that wants to use AgentForce for their customer service for, I don't know, let's say they're a shoe store or something, right?

**Jacob Cutter:** So a customer has a problem, they need to be able to talk to an agent, let's say over voice, right?

**Jacob Cutter:** So let's actually take the, since this is the most recent use case, let's take the telephony use case, right?

**Jacob Cutter:** Where the agents are actually talking to the end user over the phone rather than in like a chat interface.

**Jacob Cutter:** So if they're calling over phone, they can't see the transcript readout, right?

**Jacob Cutter:** They can only hear what the agent is saying.

**Jacob Cutter:** And if you want some details about how that kind of a stack would work, I can go into the rag and everything else that we do.

**Jacob Cutter:** But basically the idea is that that

**Jacob Cutter:** So an end user calls us in, there's some kind of routing that happens, right?

**Katja Wittfoth:** That is configurable by our customer.

**Jacob Cutter:** And basically, there's an inbound routing flow that determines which agent they get sent to, for example, right?

**Jacob Cutter:** Based on which channel they're calling in from or whatever, right?

**Katja Wittfoth:** Or which channel.

**Jacob Cutter:** So let's say they get hooked up to an agent, right?

**Jacob Cutter:** Then you start a session.

**Jacob Cutter:** And once you start a session, you have session-level metadata.

**Jacob Cutter:** You know, you have, like, on the back end of Salesforce, you have information about that customer, like the company that the user is calling into, right?

**Jacob Cutter:** Yeah.

**Jacob Cutter:** And so it was basically at design time, there's sort of design time and runtime concerns.

**Jacob Cutter:** Yeah.

**Jacob Cutter:** So at design time, our customer can configure an agent to talk to a user about specific topics and execute specific actions within the Salesforce ecosystem, right?

**Katja Wittfoth:** right.

**Jacob Cutter:** Okay.

**Jacob Cutter:** It can also do something called creating an Einstein, or sorry, now it's called Agent Force Data Library, where the user can upload a document.

**Jacob Cutter:** And they can literally, that document will automatically get like, you know, chunked and embeddings will be created in some database, right?

**Jacob Cutter:** Or some vector database or whatever.

**Jacob Cutter:** And so on the back end, Data Cloud will already have that sort of, those sort of contextualized embeddings.

**Jacob Cutter:** For the information that the company has already provided at design time, right?

**Jacob Cutter:** And so basically what will happen is in real time, at runtime, when an agent gets, or when a session gets instantiated, the agent will have access to data cloud knowledge, right?

**Katja Wittfoth:** Like these contextualized embeddings and be able to do things like similarity search on the user's query.

**Jacob Cutter:** Yeah.

**Jacob Cutter:** They'll have access to the, what we call.

**Jacob Cutter:** Well, like the agent force or planner config, which is basically the details of how the customer originally set up the agent.

**Jacob Cutter:** So which topics can be routed to, right?

**Jacob Cutter:** And which topics map to which Salesforce actions, actions that may update a record in the company's database, right?

**Jacob Cutter:** Things like that.

**Jacob Cutter:** And so there's some complexity there because there's basically a lot of back-end integration work.

**Jacob Cutter:** But yeah, I hope that sort of starts to answer your question.

**Katja Wittfoth:** And it is not available yet, right?

**Jacob Cutter:** Oh, it is.

**Katja Wittfoth:** It is.

**Jacob Cutter:** Yeah.

**Jacob Cutter:** So the voice agent is actually GA right now.

**Jacob Cutter:** We have a number of customers that are using them and we're kind of like in the middle of refining.

**Jacob Cutter:** But the voice agent, you can call it.

**Jacob Cutter:** This is something we demoed at Dreamfort.

**Katja Wittfoth:** Dreamfort.

**Katja Wittfoth:** You can call the agents.

**Jacob Cutter:** They can perform actions in the Salesforce backend.

**Jacob Cutter:** You can upload a knowledge base, and you can actually have the agent be aware of that context.

**Jacob Cutter:** And that context basically gets included in the agentic workflow.

**Katja Wittfoth:** Wow.

**Jacob Cutter:** And part of the piece that I worked on, because there are the speech components.

**Katja Wittfoth:** That was my next question, which part you worked on.

**Katja Wittfoth:** Yeah.

**Jacob Cutter:** So the part that I worked on, you could argue, is sort of the brain of the agent.

**Jacob Cutter:** The speech-to-text and text-to-speech components.

**Jacob Cutter:** Well, I'll take a step back.

**Jacob Cutter:** So there's a service that we have, which was effectively kind of ported over from the Tenex days.

**Jacob Cutter:** This is the piece that we kind of made it to Salesforce, was this GSM service that effectively is kind of like a middleman.

**Jacob Cutter:** Thank

**Jacob Cutter:** For a lot of the voice agent-like operations, so for example, it takes incoming requests, opens a web socket with the reasoner service, and then it basically is a go-between with the speech-to-text and text-to-speech services at Salesforce.

**Jacob Cutter:** So when it receives a request, it can transcribe the audio by, you know, hitting this other service, the Speech Foundation service.

**Jacob Cutter:** It can transcribe the audio, it gets a transcript back, and then it sends it to the reasoner service, or the planner service, which is what I work on.

**Katja Wittfoth:** So the reasoning part, you were also working?

**Jacob Cutter:** Yeah, so the reasoner part is actually what I've spent, like, the majority of my time on for the last, like, eight months.

**Katja Wittfoth:** Would that be, like, a lot of, it's probably a combination, right, like, of prompting and techniques, like, if you just, like, can name the few techniques you worked with.

**Katja Wittfoth:** Without, I guess, revealing all the secrets.

**Jacob Cutter:** Yeah, so, right.

**Jacob Cutter:** Yeah, there's a lot here.

**Jacob Cutter:** So maybe I'll kind of describe, like, kind of how we're handling the inputs, basically, right?

**Jacob Cutter:** So we receive, so we basically have this planner service, right?

**Jacob Cutter:** And there was already, like, these sort of text agents that AgentForce had already developed by the time 10X was acquired.

**Jacob Cutter:** And so one decision I kind of had to make right away after I kind of volunteered to be a tech lead on the reasoner part of this, a voice stack, one thing I had to decide right away was, like, okay, we have something already built, right, in Salesforce.

**Jacob Cutter:** course, it's a text agent, but it's prohibitively slow, right?

**Jacob Cutter:** And it's just not, and it doesn't really tie in a lot of the voice logic that you need.

**Jacob Cutter:** Right?

**Jacob Cutter:** The sort of nuances.

**Jacob Cutter:** For example, if I interrupt you, or you interrupt me, or I say something, and the ASR triggers like an end of utterance, but then I say something else while the agent is still processing, so concurrent request handling, all these subtle things, right, that a voice agent needs to be able to handle, the existing solution could not handle it.

**Jacob Cutter:** And it was just too, it was almost too hard coded and too baked into this sort of text modality, right?

**Jacob Cutter:** And it was, it was more optimized for reasoning and like thought than it was for like voice interactions.

**Jacob Cutter:** So I made the kind of, not executive decision, because I had a team of people, you know, I was working with, but I basically was like, guys, we need something new, right?

**Jacob Cutter:** We got to, we got to build something from scratch.

**Jacob Cutter:** Um, so we basically built an agentic workflow from scratch that tied in all of the sort of business logic and All Thank

**Katja Wittfoth:** Voice specific logic.

**Jacob Cutter:** And what that entailed was we're calling LLM APIs, right?

**Jacob Cutter:** Like you said, a lot of prompting work, right?

**Jacob Cutter:** So things like guardrail prompting and because Salesforce was really big, you know, safety.

**Jacob Cutter:** So guardrail prompts, dynamic prompting, like kind of updating the prompt with context when needed, right?

**Katja Wittfoth:** For certain use cases.

**Jacob Cutter:** Um, voice specific prompting.

**Jacob Cutter:** So like how to output the text in a way that the text could then be synthesized.

**Katja Wittfoth:** Right.

**Jacob Cutter:** And there's kind of a lot that goes into that design.

**Jacob Cutter:** Um, and, and so basically there was a lot of prompting work and early on my, uh, so this is all to say, I basically was the tech lead on this part of things.

**Jacob Cutter:** So kind of a big undertaking in the sense that like the brain really controls, um, like this is really entirely controlling the content of.

**Katja Wittfoth:** What the agent is saying before the text gets synthesized into voice, right?

**Jacob Cutter:** So, and like I said, it also needs to be able to handle these voice-specific features, like interrupts, concurrent requests.

**Jacob Cutter:** Right.

**Jacob Cutter:** And so, you know, various people on my team worked on various pieces of that.

**Jacob Cutter:** But kind of really early on, I had my hands in sort of the design and the, I spent a lot of time talking with like the architects about, you know, how to build this thing so that it was optimized for latency, that people would not really detect like a long lag and like be more prone to the system.

**Jacob Cutter:** And then there was also pieces, like you said, like RAG, like retrieval, right?

**Jacob Cutter:** So that's kind of where all the backend integration stuff happens.

**Jacob Cutter:** So like retrieving knowledge from data cloud, including it in the prompts or including it in the agent context.

**Jacob Cutter:** And then...

**Jacob Cutter:** here we go.

**Jacob Cutter:** Thank

**Jacob Cutter:** Using the chat history as context, right?

**Jacob Cutter:** So the agent was aware of what already happened, including tool calls, right?

**Katja Wittfoth:** So like there's a lot of tool calling happening because that's actually how the agent decides to invoke certain actions.

**Jacob Cutter:** And that's something where you have to kind of craft the tool descriptions.

**Jacob Cutter:** You have to like, you know, there's a lot of work there as well to sort of optimize and make sure that the actions can be invoked.

**Jacob Cutter:** Um, and, and also, uh, one, one really complex thing, which I probably don't want to get too detailed about is, um, like entity confirmation.

**Katja Wittfoth:** So nice.

**Jacob Cutter:** Let's say I want to do something simple, like make a reservation, right?

**Katja Wittfoth:** Right.

**Jacob Cutter:** The end user says, I want to make a reservation for tomorrow at noon.

**Jacob Cutter:** And the LLM has to decide, uh, via tool calling and whatever else, like, uh, did I capture the necessary arguments to invoke the Salesforce function or the Salesforce API?

**Katja Wittfoth:** Right.

**Jacob Cutter:** And...

**Jacob Cutter:** And so we have a mechanism in the planner for deciding if all the arguments have been provided, know, kind of like slot filling, have the arguments been provided?

**Jacob Cutter:** No, then you have to actually emit an entity confirmation message.

**Jacob Cutter:** So like, or sorry, you have to basically ask for the additional information.

**Jacob Cutter:** Once the person provides all of the information necessary to invoke an action, because these things are spoken, there are certain entities we want to also confirm are correct, right, over phone.

**Jacob Cutter:** So that's another thing we did was entity confirmation.

**Jacob Cutter:** So like, oh, just to just to repeat, your email is you mean this?

**Jacob Cutter:** Yeah, your email is info at Salesforce.com.

**Jacob Cutter:** Yes.

**Jacob Cutter:** And then it once it confirms that it moves on to the like action execution and the other steps involved with the workflow.

**Katja Wittfoth:** Yeah, yeah, that sounds really super cool.

**Katja Wittfoth:** It sounds also like, I don't know if Daniel or Marcel shared, but it's kind of like the space of Salesforce, right?

**Katja Wittfoth:** It's not like similar to growthx, but the growthx kind of like wants to become a system like Salesforce for marketing, right?

**Katja Wittfoth:** So that would be, that's amazing that you had this experience at Salesforce.

**Katja Wittfoth:** Before the Salesforce, the company that got acquired, did they develop actually the same product or was it like, and what was the purpose of the product?

**Katja Wittfoth:** Was it specifically for Salesforce type?

**Jacob Cutter:** That's a good question.

**Jacob Cutter:** It was a bit different.

**Jacob Cutter:** Let me think.

**Jacob Cutter:** It's a great question.

**Jacob Cutter:** So Salesforce, I don't think they, I mean, obviously I don't think they were consciously building towards a Salesforce type product.

**Jacob Cutter:** But I think the main, one of the things I really liked about Tenex was that they were very, they almost overemphasized latency because they really want, like, they really were focused on a natural sounding agent.

**Katja Wittfoth:** And I think they actually did a great job of that.

**Jacob Cutter:** And that's part of why Salesforce, like, acquired them was that Tenex was very diligent about optimizing ahead of time and being proactive about latency to get that natural feel that end users inevitably want.

**Jacob Cutter:** Because I find that people tend to focus too much on accuracy or things that LLMs more and more are able to handle naturally, right, as the tech evolves.

**Jacob Cutter:** And not as much on, like, and the sort of the optimizing the workflow flows, right, so that the customer can get to where they want quickly.

**Katja Wittfoth:** And so I think that's one thing Tenex did really well.

**Jacob Cutter:** But I will say the...

**Jacob Cutter:** Reasoner service that I've been working on at Salesforce is like a whole different thing from what Tenex built because the tech stack that Tenex built was, it wasn't really constructed the same way and it didn't include a lot of the business logic that Salesforce needs, right?

**Katja Wittfoth:** Right.

**Jacob Cutter:** So for example, I think of Tenex as like, it was an agent that you could kind of, that we were kind of building specific implementations of for different customers, right?

**Jacob Cutter:** And we were getting, we were just starting to get to a place where we could kind of automate the sort of building of these agents when we were acquired, but Salesforce, they make it so that customers can configure everything kind of from head to toe, right?

**Jacob Cutter:** So I want an agent that does this specific thing or is limited to these set of Salesforce, you know, actions and all that kind of stuff.

**Jacob Cutter:** And so if you're already familiar with Salesforce, it kind of hooks naturally.

**Jacob Cutter:** And so it's almost more of a product-first thing or a use-case-first thing rather than a generic agent that we would tailor towards specific customers, if that makes sense.

**Katja Wittfoth:** Yeah, totally makes sense.

**Katja Wittfoth:** And maybe let's talk a little bit more about DeepGram.

**Katja Wittfoth:** So it sounds like your last two years were really cutting-edge technology, LLMs, which is all amazing and wonderful and exactly applicable for GrowthX and what you will be doing.

**Katja Wittfoth:** But we'd love to understand the DeepGram experience because that sounds more like a traditional ML and which is also so valuable to have this traditional ML experience.

**Katja Wittfoth:** And we'd love to understand what types of experience and what types of models you worked with, what were the projects, etc.

**Jacob Cutter:** Yeah.

**Jacob Cutter:** Man, it feels like a long time ago.

**Jacob Cutter:** Yeah, for sure.

**Jacob Cutter:** So there were a lot of things that happened in three years, three and a half years.

**Jacob Cutter:** I kind of went through like a lot of different projects.

**Jacob Cutter:** So I can kind of go through, I can kind of go through them and kind of give an overview of what I worked on first.

**Jacob Cutter:** Yeah, the first project I really kind of sunk my teeth into when I started at DeepGram was I came in as a data scientist.

**Jacob Cutter:** But really what they wanted to do, I almost think about it a little bit as like a mixture of like data science, like product engineer, AI engineer, like basically building the initial core models that were kind of used for different use cases.

**Jacob Cutter:** So for example, when I came in, right.

**Katja Wittfoth:** Oh, you know what, like I told you about traditional ML, but I realized like I actually did misunderstood.

**Katja Wittfoth:** And I'm reading through your LinkedIn.

**Katja Wittfoth:** I thought ASR meant other regressive models, but it's speech recognition.

**Katja Wittfoth:** So you did work actually primarily on speech, right?

**Katja Wittfoth:** And I'm less familiar on that, but we'll love to hear more about it.

**Jacob Cutter:** sure.

**Jacob Cutter:** Yeah, sorry.

**Jacob Cutter:** So I guess the point I was getting to is that I did actually early on train a number of ASR models.

**Jacob Cutter:** And by a number, mean like dozens.

**Jacob Cutter:** So basically, you know, they had these PyTorch tools they were developing to train specific types of end to end architectures, right?

**Jacob Cutter:** And so I kind of got my hands dirty, like using those in combination with a lot of data curation, kind of expand our ASR product offerings to like many different kinds of models.

**Jacob Cutter:** So for example, a phone call model that's good on phone call audio, and so on, right?

**Jacob Cutter:** So like lots of different use cases that would satisfy our initial customers during that kind

**Jacob Cutter:** But I think what basically ended up happening was, from a product perspective, it kind of, the accuracy improvements and the things that I was doing to those, like, core model, like, retrainings, it kind of plateaued after a while, right?

**Jacob Cutter:** Because eventually you sort of start to plateau and you really have to bust out some new, like, architectures to really make improvements on the existing models with the existing data.

**Jacob Cutter:** And so there was sort of a skunkworks project where I was heavily involved, and this is actually what the patent is for in my resume, basically creating a transformer-based ASR architecture that was, like, highly accurate, but also low latency so that we wouldn't sacrifice, you know, latency for our customers and kind of, you know, incur.

**Jacob Cutter:** However, I like to say that latency, with latency often comes a price increase because it means there's some...

**Katja Wittfoth:** Reputationally intensive stuff happening, right?

**Jacob Cutter:** So kind of keeping models somewhat lightweight, low latency, but still boosting the accuracy was a big goal.

**Jacob Cutter:** And we were able to do that as part of this Skunk Works project.

**Jacob Cutter:** I didn't do the model training primarily for that.

**Jacob Cutter:** I did a lot of like data science and sort of evaluation work on that side to help kind of rapidly iterate, you know, through these different architectures and whatnot.

**Jacob Cutter:** And what we ended up settling on was a product that customers really liked, because it was fast and accurate, and boosted our product offerings from there.

**Jacob Cutter:** And I did do a number of other projects where I was like, kind of building my own PyTorch pipelines from scratch.

**Jacob Cutter:** So for example, there was also a case where customers are complaining about our punctuation, right?

**Jacob Cutter:** And, you know, because our punctuation was at the time built into the ASR.

**Jacob Cutter:** Models themselves.

**Jacob Cutter:** And so one thing I did was a research project around how do we train post-processing models that are really fast, that can fluctuate text as it's being streamed or whatever, right?

**Jacob Cutter:** And so I actually, like, you know, got my hands dirty with a number of different architectures there, training transformer-based models in PyTorch, doing the text cleaning pipelines and all the things necessary to kind of create the training data for that.

**Jacob Cutter:** Yeah, so that was an interesting project as well.

**Jacob Cutter:** That was where I kind of worked more in the dirt with the PyTorch code and whatnot.

**Jacob Cutter:** Let me think.

**Jacob Cutter:** Yeah, there's a lot of different things I worked on.

**Katja Wittfoth:** Yeah.

**Katja Wittfoth:** I bet.

**Katja Wittfoth:** And then for almost four years, so that sounds like a lot of stuff.

**Katja Wittfoth:** Awesome.

**Katja Wittfoth:** That, that gives me a really good overview.

**Katja Wittfoth:** Maybe we'll, we'll switch to GrowthX and chat, brainstorm stuff around GrowthX.

**Jacob Cutter:** Sounds good.

**Katja Wittfoth:** So as you know, growthx generates long form content for clients, right?

**Katja Wittfoth:** So of course, what is really important is to measure the quality of the content and systematically improve it all the time.

**Katja Wittfoth:** So maybe let's brainstorm and talk about how would we design a system that would score the content quality and basically use those scores to improve the content over time.

**Jacob Cutter:** Okay.

**Jacob Cutter:** Yeah.

**Katja Wittfoth:** So just kind of an open-ended like project thing.

**Katja Wittfoth:** I would love to hear like your ideas on that.

**Katja Wittfoth:** How would you approach it?

**Katja Wittfoth:** And please ask me any questions you have.

**Jacob Cutter:** Yeah.

**Jacob Cutter:** Sorry.

**Jacob Cutter:** Can you repeat it one more time?

**Jacob Cutter:** Just so, yeah.

**Jacob Cutter:** Yeah.

**Jacob Cutter:** Yeah.

**Katja Wittfoth:** Of course.

**Katja Wittfoth:** So basically we generate content, like marketing content for clients, right?

**Katja Wittfoth:** And at the end, it's important that it's not just like some hallucinated LLM content, but it's really a quality piece that clients are also happy about.

**Katja Wittfoth:** So here in this question, I'm looking for how would we design this course for the content quality and use this course to have a system that we can improve the quality over time?

**Jacob Cutter:** I see.

**Jacob Cutter:** Yeah, so just because I'm not super familiar with marketing content, I'll probably need to ask questions.

**Jacob Cutter:** But yeah, so the first thing...

**Katja Wittfoth:** If you can imagine, it's basically like it will be a blog post.

**Katja Wittfoth:** That's one of the marketing content.

**Katja Wittfoth:** And it can be really about anything, right?

**Katja Wittfoth:** It's what is the best spend management.

**Katja Wittfoth:** How to do spend management for small businesses, something like that.

**Jacob Cutter:** Right.

**Jacob Cutter:** Okay.

**Jacob Cutter:** Yeah.

**Jacob Cutter:** So I'm guessing, I feel like for this kind of thing, the first thing that comes to my mind is that we kind of want to start on the marketing or sales funnel kind of side of this.

**Jacob Cutter:** Because I feel like it's hard for me to picture how we would know that we're successful unless the end, our customers are actually seeing the results in like the click-through rate or the like page visits or, right.

**Jacob Cutter:** Because the content has to attract the customer.

**Katja Wittfoth:** Yeah.

**Jacob Cutter:** And I'm guessing that the goal, and this is kind of where I might need some help.

**Jacob Cutter:** The, I'm guessing that the goal is to actually see that the customer, that the content is actually convincing them of something, enticing them to kind of click through to some product page or something, right.

**Jacob Cutter:** And so there must be some metrics there that we are really trying to optimize on kind of the product side.

**Katja Wittfoth:** Yes, but let's, and I love how you think about this.

**Katja Wittfoth:** This is like basically we're doing content for something, right?

**Katja Wittfoth:** And so it's not only for being a quality content.

**Katja Wittfoth:** This is like a second case I wanted to chat through with you about.

**Katja Wittfoth:** So it's about like AI visibility.

**Katja Wittfoth:** So maybe let's set it aside and think now about just a content from the perspective of like we deliver this content to the marketing team of, you know, Ramp, for example.

**Katja Wittfoth:** And they will immediately tell us it's like they like it or not like it.

**Katja Wittfoth:** So kind of like this is the content quality for this use case.

**Katja Wittfoth:** And I absolutely love your idea to connect that it's like, yeah, even if we create.

**Katja Wittfoth:** like, like, yeah, even create.

**Katja Wittfoth:** think

**Katja Wittfoth:** It moves your needles, you know, be a better argument, but for now it's only like the client decides to post it on their website or not.

**Jacob Cutter:** I see.

**Jacob Cutter:** Yeah, so that's interesting.

**Jacob Cutter:** It seems like a difficult problem because how, like, in order to determine in an, so are we looking to determine in an automated way that a piece of content is good?

**Jacob Cutter:** Or are we like, is this like, okay, we're going to have humans that review this marketing content after it's been generated by an AI system?

**Katja Wittfoth:** Like, which way are we kind of going here?

**Katja Wittfoth:** I think it could be both, you know, and that's something that we really want to design in growthx is like, that's what I'm hearing from Daniel.

**Katja Wittfoth:** How do we label this in the future?

**Katja Wittfoth:** How we can actually know for sure that the end product is quality and satisfactory?

**Katja Wittfoth:** But for now, let's say that we don't have this before leaving and going into this human in the loom details, how do we take a piece of text and try to score it in terms of like, is it good or not?

**Jacob Cutter:** Oh, sure.

**Jacob Cutter:** I mean, I've worked on systems in the past where, you know, like we're using LLM as a judge, right?

**Jacob Cutter:** But the trick there, though, what's tricky about that is that it is, you have to have a set of criterion that the model can like reliably judge about the content, right?

**Jacob Cutter:** Or like you have to have like a set of criterion of things that you specifically care about that content in order to determine that it's good.

**Jacob Cutter:** And you have to be fairly like specific with the model, right?

**Jacob Cutter:** You can't just like prompt a model to tell you if it's good or bad.

**Jacob Cutter:** So I think that's where maybe I need a little...

**Jacob Cutter:** A more context to provide this evaluation model, but you could set up an evaluation pipeline, right?

**Jacob Cutter:** Okay.

**Katja Wittfoth:** Maybe let's brainstorm first about what type of scores and metrics would be developed.

**Katja Wittfoth:** So imagine the beginning of the whole workflow and pipeline of content generation is the requirements and prompt, okay, we want to write an article about my example, spend management for small business, and we want XYZ facts in it.

**Katja Wittfoth:** So we plug it in, and then the whole growthx pipeline develops the article, and at the end, we have this text.

**Katja Wittfoth:** Let's brainstorm the scores to measure, was it successful?

**Katja Wittfoth:** Was it okay?

**Katja Wittfoth:** Bad?

**Jacob Cutter:** That's interesting.

**Jacob Cutter:** Yeah, so...

**Jacob Cutter:** How do we know if a piece of content is good?

**Jacob Cutter:** Do we have data on previous content that has been successful?

**Katja Wittfoth:** Yes, for other clients.

**Katja Wittfoth:** if they accept, we currently also have content of, like, they gave feedback, what did we change, what was acceptable, and we're trying to build a system of, like, basically tracing those feedbacks and changes.

**Jacob Cutter:** Yeah.

**Jacob Cutter:** Yeah, because one thing we could do, actually, is, like, a similarity measure or, like, some kind of judge of, like, you know, does this content, is this content similar to content, past content that was successful or, like, was high quality based on either human judgment or our customers?

**Jacob Cutter:** But I think what- I

**Jacob Cutter:** If I'm not mistaken, what you're kind of asking is more about the, like, let's actually create some, some criterion that the model can use to judge, right?

**Jacob Cutter:** Yeah.

**Jacob Cutter:** Like, absolute criterion.

**Katja Wittfoth:** Yes.

**Jacob Cutter:** That's interesting.

**Jacob Cutter:** I mean, what things do marketers care about, right?

**Jacob Cutter:** Like, what things, I mean, do they care about conciseness?

**Jacob Cutter:** Do they care about specificity?

**Jacob Cutter:** Um, verbosity, or verbosity is inverse of conciseness, right?

**Jacob Cutter:** So, yeah, so basically, like, things like, is it short and sweet?

**Jacob Cutter:** Is it catchy?

**Jacob Cutter:** Yeah.

**Jacob Cutter:** Is it, which, I don't know how you telemodel that, but maybe you could ask, you know, does it contain certain, like, buzzwords that are appropriate for that domain or that space?

**Jacob Cutter:** Um, let's see.

**Jacob Cutter:** And actually, not all LLMs don't have to be used for all of this, right?

**Jacob Cutter:** Some of this could be more lightweight NLP models or things that, yeah, or just simple keywords.

**Katja Wittfoth:** Searches even.

**Jacob Cutter:** Let's see.

**Jacob Cutter:** What else?

**Jacob Cutter:** They might care about, does it contain, ah, that's one thing that would be major.

**Jacob Cutter:** Does it contain the contextualized information that we're actually providing from the customer itself?

**Katja Wittfoth:** Right.

**Jacob Cutter:** Is it kind of hitting all those checkboxes, right, or checkboxes?

**Jacob Cutter:** So, like, if the customer gives us a bunch of grounding information, like grounding context, right?

**Jacob Cutter:** Like, they're in this industry, and this is what we do, and this is the product we're selling, and all of these details, like, we want to make sure the model's output is grounded in all of that sort of information that we provided.

**Jacob Cutter:** That's one thing.

**Jacob Cutter:** Let me think.

**Jacob Cutter:** Are there any other, is there anything obvious I'm missing about the content?

**Katja Wittfoth:** I think you, you named a lot of good things.

**Katja Wittfoth:** maybe how would you think about, like, just generic, right?

**Katja Wittfoth:** Like someone writes an essay, like, how do I know that it's good or bad, right?

**Jacob Cutter:** Yeah, like, does it communicate, I mean, does it communicate its thoughts well?

**Jacob Cutter:** Like, does it, does it provide a good summary?

**Jacob Cutter:** Let me see.

**Jacob Cutter:** Grammatical?

**Jacob Cutter:** Like, or grammar issues?

**Jacob Cutter:** Like, is it, I mean, the funny thing is, I feel like we're getting into the territory of some other vendors which specialize in these things, you know, like Grammarly and these other companies, but yeah, like, is it grammatically correct?

**Jacob Cutter:** Is it syntactically correct?

**Jacob Cutter:** Yeah, does it, is it digestible to someone who doesn't know about, you know, that specific?

**Katja Wittfoth:** Yeah, that, I think we have pretty, pretty much a good list.

**Katja Wittfoth:** So maybe let's, let's think about how can we systematically use those to, to make improvements.

**Katja Wittfoth:** And you, you named already one of the solutions could be LLM as a judge.

**Katja Wittfoth:** Maybe we can elaborate the solution or anything else where you're.

**Jacob Cutter:** Right.

**Katja Wittfoth:** I think.

**Jacob Cutter:** Oh, by the way, one more thing I just thought of was Tone.

**Jacob Cutter:** Yeah, love it.

**Jacob Cutter:** This is actually the major one, what I'm hearing, like companies want their own tone.

**Jacob Cutter:** Right.

**Katja Wittfoth:** Yeah.

**Katja Wittfoth:** So like to hit this.

**Jacob Cutter:** Sorry, I didn't mean to interrupt.

**Katja Wittfoth:** No, no, you're going.

**Jacob Cutter:** Yeah, Tone is a big one.

**Jacob Cutter:** But yeah, so you were asking about how do we, sorry, what was your question again?

**Katja Wittfoth:** Use those scores to, to improve the content.

**Jacob Cutter:** Yeah, there's kind of different ways to go about it.

**Jacob Cutter:** I guess one way, well, there's kind of easy to hard.

**Jacob Cutter:** So the easier ways might be take less work, but might end up in the long run being more computationally expensive or more, there might be more human involvement, but the long term, you know, I could see how like you might, someone might jump to like, okay, well, maybe we should fine tune these models, you know, either fine tune a lightweight LLM or, or create some lighter weight NLP models that can kind of capture these specific metrics or, or whatever you want to say.

**Jacob Cutter:** these specific metrics or traits about

**Jacob Cutter:** A piece of content so that we can kind of execute those in real time and run inference like, you know, I mean, my understanding is latency isn't as important here.

**Jacob Cutter:** I'm used to low latency applications, but here we care more about accuracy and like, right, the quality of the generated content.

**Jacob Cutter:** So I suppose the LLMs can do, I think those would be used more for things that are involved kind of ingesting the entirety of the content and being able to maybe like conceptualize things about it or things that involve like analyzing a larger chunk of text.

**Jacob Cutter:** Um, but I think that there are, I think fine tuning though, whenever it comes to fine tuning, I'm a little skeptical because like, you know, things change a lot and it's not clear that if you fine tune something, it's going to be worth it.

**Jacob Cutter:** You know, um, there's also just like prompt updates and sort of iterative workflows where maybe you like reason through, you know, like, okay, like.

**Jacob Cutter:** based on the evaluation, how do I update the prompt, for example, for this domain?

**Jacob Cutter:** Or how do I make the prompt dynamic so that I can instruct the model that, no, it needs to behave more in this way?

**Jacob Cutter:** There are ways to use like agentic workflows, like chaining sort of LLM calls together so that you are refining the content itself, right?

**Katja Wittfoth:** So they're already, if Daniel shared it with you, but the whole current system, how growthx generates the content, it is an agentic workflow with like multiple pieces of pipeline from like reiteration, factual checkers.

**Katja Wittfoth:** I don't even know a lot about like the specifics, but like one.

**Katja Wittfoth:** One be a checker, one could be like a tone evaluator and rewrite this with a proper tone.

**Katja Wittfoth:** Another gigantic piece of the workflow would be like checking the grammar, etc.

**Jacob Cutter:** Yeah, it makes sense to compartmentalize it because you can think about each, well, we can call them agents or LLMs or whatever, but you could think about each stage as kind of being its own prompt, its own like sort of, you know, needing its own context, right?

**Jacob Cutter:** So maybe, yeah, maybe you break it down into steps or stages and you have agentic workflows kind of for each stage.

**Jacob Cutter:** So maybe there's like an evaluation step where you can go back to a previous stage and like regenerate the content, perhaps even update the prompt or the context so that you are maybe even generating things for different customers better.

**Jacob Cutter:** you.

**Jacob Cutter:** Like, if there's some kind of shared prompt templates or something that are being used.

**Jacob Cutter:** Yeah, that's a difficult problem.

**Katja Wittfoth:** Yeah.

**Jacob Cutter:** Yeah.

**Jacob Cutter:** I guess, am I missing something?

**Katja Wittfoth:** I guess, yes, what you said is, like, it's basically one of the approaches, what you suggested, is to, like, go and evaluate each piece, right?

**Katja Wittfoth:** And based on this final score, is that what you're saying?

**Katja Wittfoth:** Based on the final score, go and, like, actually evaluate each of the piece or rerun the pieces?

**Jacob Cutter:** Right.

**Jacob Cutter:** Like, maybe there's a loop somewhere, right?

**Jacob Cutter:** So it doesn't have to be all the stages, right?

**Jacob Cutter:** Or all the steps in this sort of, like, content generation cycle.

**Jacob Cutter:** Maybe there's, like, a loop back from the evaluation step to, like, maybe there is a step where you're, like you said, generating a final score effectively.

**Jacob Cutter:** And then, or maybe you want to keep it as separate.

**Jacob Cutter:** Like, I evaluate, I have different evaluation scores for different traits or different attributes that I'm optimizing for.

**Jacob Cutter:** And then based on those, you can go back and regenerate at a different stage, right?

**Jacob Cutter:** Or go back and regenerate the content and do whatever evaluations or grounding you need, right?

**Jacob Cutter:** In those earlier stages.

**Katja Wittfoth:** Yeah, and this is something that is probably will be one of the first projects to figure out.

**Katja Wittfoth:** And it's like, think about systematically.

**Katja Wittfoth:** And most likely, first step would be for growth access is really to set up a foundation.

**Katja Wittfoth:** So evaluation system.

**Katja Wittfoth:** That's why I was saying, like, at the end, we want to probably just know, like, what is the output, right?

**Katja Wittfoth:** But also, like, actually have evaluation system for each of the parts as well.

**Katja Wittfoth:** And first, probably like monitor over time, okay, we have the final score of the eye.

**Katja Wittfoth:** Content is, you know, on the average 80%.

**Katja Wittfoth:** This week we did some changes.

**Jacob Cutter:** Do we see any improvements there?

**Katja Wittfoth:** And then for each also piece of the pipeline, we do extra evaluation.

**Katja Wittfoth:** And this, this like, likely this first part would be not about re-running and improving the one piece of the article, but more of like evaluation of the whole system and seeing which part of this pipeline it is needed to systematically go and like reiterate on that for all the clients.

**Katja Wittfoth:** Or maybe sometimes we see on X clients and they have XYZ traits, we see the tone is usually the problem.

**Katja Wittfoth:** So how we can go and like fix the tone issue, maybe it's, you know, fine-tuned.

**Katja Wittfoth:** Maybe it's reinforcement learning part.

**Katja Wittfoth:** Maybe it's something else.

**Katja Wittfoth:** like systematically figuring out from evaluation to like what is the next step, the roadmap for the whole thing.

**Jacob Cutter:** Yeah, and I'm sure there's a way to incorporate reinforcement learning into this somehow, but it's like you basically just need some kind of reward model, right?

**Jacob Cutter:** And that alone is kind of, I guess, a little bit tricky here because you have to figure out, like you have to have a good sense of what will actually tell the model that this is going to be successful content.

**Jacob Cutter:** And so, yeah, if the scores are LLM generated, it can get a little messy, but yeah, that makes sense.

**Katja Wittfoth:** Yeah, maybe let's switch to the second case study I'd like to discuss with you.

**Katja Wittfoth:** And here as well is more high level.

**Katja Wittfoth:** I'd like to understand like your way of thinking about this.

**Katja Wittfoth:** So we touch base a little bit about like what is the good context.

**Katja Wittfoth:** And essentially, we, growthx, try to help brands improve their visibility, right?

**Katja Wittfoth:** And one of the parts right now in becoming most important, actually, is visibility in LLM search, right?

**Katja Wittfoth:** How the clients of growthx can be visible by, you know, chat GPT, cloud, Gemini, or whatever agent people are using.

**Katja Wittfoth:** So whenever someone is asking these questions of, like, what do I choose as a, you know, banking system for my small business, we would see some of the clients growthx is working with.

**Katja Wittfoth:** So first question to you, how do you, what do you think about the brand visibility in LLM search?

**Katja Wittfoth:** And how could we essentially measure this?

**Katja Wittfoth:** We don't have any data because OpenAI, et cetera, they don't share what are people usually searching.

**Jacob Cutter:** Yeah, sorry, just so I'm understanding the question.

**Jacob Cutter:** So we're talking about, like, if I go to Google and I search what is the best thing for this whatever use case, how often does the AI summary give, like, mention, like, a specific customer?

**Jacob Cutter:** Or are we talking about, like, if they ask, like, ChatGPT?

**Jacob Cutter:** Like, is it, like, over the, are you talking about, like, a web browser, like a search engine, or are you talking about?

**Katja Wittfoth:** So I'm talking about anywhere where you can trigger an LLM search.

**Katja Wittfoth:** So in ChatGPT, if you, it doesn't trigger automatically, there is a button, right?

**Katja Wittfoth:** But if I go there and say, like, find me five best alternatives to iPhone.

**Katja Wittfoth:** You know, it will start web search, most likely, hopefully.

**Katja Wittfoth:** And then it will, like, look for stuff and then come back with suggestions.

**Jacob Cutter:** I see.

**Jacob Cutter:** Interesting.

**Jacob Cutter:** Yeah, I guess there's a couple ways that I could approach it.

**Jacob Cutter:** One, I'm not sure if this is the best way, but you could brute force it.

**Jacob Cutter:** And what I mean by that is you could, like, you could ask something like that, right?

**Jacob Cutter:** Like, you could, like, have basically, like, a template, like, input prompt for the model or a template, like, query.

**Jacob Cutter:** Like, oh, like, for this domain, we have this kind of question that we want to ask, you know, to see, like, what the results are.

**Jacob Cutter:** So you're basically, like, simulating what the end user is doing.

**Jacob Cutter:** And so you could, like, basically, like, feed that to the model with some.

**Jacob Cutter:** Non-zero temperature, basically, and then see, like, and then do some kind of statistics on the results that you get.

**Katja Wittfoth:** So you could do that, like, many times.

**Jacob Cutter:** Yeah.

**Jacob Cutter:** And that would be, like, I don't know, yeah, effectively, like, bootstrapping it.

**Jacob Cutter:** And you could see, like, how many times you get a specific customer mentioned in those results versus other customers.

**Jacob Cutter:** And then you could basically, like, rank it based on the statistics that you get from that.

**Jacob Cutter:** So, like, how frequently is this customer mentioned versus this customer?

**Jacob Cutter:** And you could kind of form a hierarchy from that or, like, a ranking system.

**Jacob Cutter:** Yep.

**Jacob Cutter:** And that would be, like, so that would be, like, use case or domain and customer specific, right?

**Jacob Cutter:** And that would just involve, like, having, like, prompting the model to tell you, right, who's the best, who gives the best haircuts, whatever.

**Katja Wittfoth:** I don't know.

**Katja Wittfoth:** Yeah.

**Katja Wittfoth:** Yeah.

**Jacob Cutter:** Yeah.

**Jacob Cutter:** But the.

**Jacob Cutter:** There's probably other ways of, I'm trying to think if there are, like, ways of doing it that aren't so computationally intensive.

**Jacob Cutter:** Because that, right, obviously every forward pass to an LLM is, like, expensive.

**Jacob Cutter:** But if, I mean, guess if we can afford it, that's probably the most reliable way because we're, it's empirical, right?

**Jacob Cutter:** Like, we're getting straight from the model.

**Katja Wittfoth:** Yeah, I heard there's, like, some providers that do, like, they have people, basically, and they do, like, observation on those people and basically just, like, see, install stuff on their computer and see what they're searching.

**Katja Wittfoth:** then storing this data and you could buy this.

**Katja Wittfoth:** But I think what you were suggesting in the first place is probably the most reliable version so far.

**Jacob Cutter:** Sorry, I actually thought of one more thing.

**Jacob Cutter:** This is kind of, I don't know if this is really in line with your question, but,

**Jacob Cutter:** Like I'm thinking, I keep thinking about it from a browser perspective because I know that when I look things up, right, I'm always typing into Google and, you know, people are becoming, I think, more and more reliant on these like AI summaries and whatnot to point them to resources.

**Jacob Cutter:** So one thing that would be interesting is because it wouldn't involve LLM computation on our end, right?

**Jacob Cutter:** It would involve leveraging the fact that AI overviews are automatically provided when you search in Google, for example.

**Jacob Cutter:** You could do, you could also do something like that where you query Google and then you scrape the page, you know, for, I don't know, maybe you can scrape the page for the AI overview and the results and then you can do that repeatedly.

**Jacob Cutter:** So treat the Google Chrome, you know, as like a, as.

**Katja Wittfoth:** That's essentially the same.

**Katja Wittfoth:** It's like either asking ChatGPT or Gemini, right?

**Katja Wittfoth:** Right.

**Katja Wittfoth:** The prompts and then storing it.

**Jacob Cutter:** Yeah, but I guess the point is.

**Jacob Cutter:** Like, you're not handling the computation or the cost on our side, right?

**Jacob Cutter:** Because that's happening on the back end, right?

**Katja Wittfoth:** The AI overviews.

**Katja Wittfoth:** You're saying, like, basically it's hit the Google and then scrape the AI version, but that's the same.

**Katja Wittfoth:** Or not.

**Jacob Cutter:** Maybe I'm not getting what you're saying.

**Jacob Cutter:** Yeah, well, so, for example, I thought you were talking about, like, using ChatGPT, for example.

**Jacob Cutter:** Uh-huh.

**Jacob Cutter:** Like, when you submit a query to ChatGPT, right, that's, like, effectively, like, you're paying per token, right?

**Jacob Cutter:** Yes.

**Jacob Cutter:** Yeah, so I'm saying, if you, doesn't the, whatever, the Google mechanism, like, for generating the AI overview, that would effectively be free, right?

**Katja Wittfoth:** Oh, like, basically just, uh, uh, starting the Chrome, uh, Chrome, and then do it for free, instead of being in the API.

**Jacob Cutter:** Yeah, they might actually, like, throttle it.

**Jacob Cutter:** see.

**Jacob Cutter:** let's

**Katja Wittfoth:** Or something, they might bottleneck it, but it was just a thought, you know, like, there's different ways to do it, yeah.

**Katja Wittfoth:** To really reduce the cost.

**Katja Wittfoth:** But let's say we did this, and we have a data set.

**Katja Wittfoth:** So we have a data set look like this.

**Katja Wittfoth:** We have prompt.

**Katja Wittfoth:** Let's say, what should I use as a Vype coding tool?

**Katja Wittfoth:** So we run it through all the possible AIs, or the main ones, Gemini, LLM, CharGPT, sorry, and Co.

**Katja Wittfoth:** And we have basically a data set of, like, okay, Lovable comes up, you know, I don't even know, like, what is the second one from Lovable?

**Katja Wittfoth:** Any other tools?

**Katja Wittfoth:** Okay, like, tool X comes up, tool Y does...

**Katja Wittfoth:** It doesn't come up, and it should, because we did a Google search with the same prompt, so I used that as a kind of counterfactual.

**Katja Wittfoth:** So we have a data set of prompt, tool comes up, not comes up in terms of brand, and we create the features of the content.

**Katja Wittfoth:** And features of the content could be exactly what we discussed with you about the quantity and extended version of that.

**Katja Wittfoth:** Is it concise?

**Katja Wittfoth:** Does it have summary?

**Katja Wittfoth:** Does it have backlinks?

**Katja Wittfoth:** Is it punchy?

**Katja Wittfoth:** Etc.

**Katja Wittfoth:** What would we do, or can we do with this to figure out what actually LLMs love about the content?

**Katja Wittfoth:** What type of content we should produce for our clients to really boost their visibility?

**Jacob Cutter:** Yeah, that's interesting.

**Jacob Cutter:** I would actually start by analyzing what the top results are, even if it's not the customer we care about, right?

**Jacob Cutter:** So for example, if lovable, whatever, is the top ranked in terms of results that we get back, you can do the same whatever LLM evaluations or whatever judgment to generate those same scores and see, okay, which thing does it actually care about, right?

**Jacob Cutter:** Like which metrics?

**Jacob Cutter:** And then optimize for those metrics potentially.

**Jacob Cutter:** That's like one way of going about it.

**Jacob Cutter:** So in other words, like relative or comparative, like get a sense of like, okay, if I then sort of tweak the prompts or the generative part to like match so that the scores kind of match what I'm getting from the top ranked one, then if I re-rank, like how does it stack up, right?

**Jacob Cutter:** That kind of thing.

**Jacob Cutter:** But that would also, it's effectively almost like it would be like experimentation, like A-B experiment from a product standpoint, because you wouldn't know until you actually ship that new marketing content, right, that the results would change.

**Katja Wittfoth:** Right.

**Jacob Cutter:** And also, another question I have is like, we also need to understand how ChatGPT versus Gemini versus the different models, what, like how their search results, like the mechanism they use is different.

**Jacob Cutter:** So are they doing a straight web search?

**Jacob Cutter:** Or are they like using the context that they've been trained on mostly, right?

**Jacob Cutter:** Like, what are they relying the most on?

**Jacob Cutter:** Because it might actually be difficult for certain models to even change those results if they're not relying on like dynamic web search as much.

**Jacob Cutter:** You know what I mean?

**Katja Wittfoth:** Like.

**Katja Wittfoth:** Yeah, yeah, absolutely.

**Katja Wittfoth:** And we would trigger the search right away, but you're right, sometimes it would just like tell from.

**Katja Wittfoth:** The knowledge, especially if there's no, like, specific guide, guidelines for, for users to, like, search the web now, you know.

**Jacob Cutter:** Right, right.

**Katja Wittfoth:** So we'll just use their trained data versus what is, what is new.

**Jacob Cutter:** Right.

**Jacob Cutter:** I see.

**Jacob Cutter:** Yeah, sorry, I'm just trying to think.

**Jacob Cutter:** What else?

**Katja Wittfoth:** We're, we're running a little bit in time with, we're on time right now, but I'm happy to stay for another five minutes if it's okay with you, if you have time.

**Katja Wittfoth:** Maybe just a couple minutes, yeah.

**Katja Wittfoth:** Yeah, that's fine.

**Katja Wittfoth:** I just want to actually give you some time to ask me questions and we can wrap up.

**Jacob Cutter:** Yeah, no, this is, this is fun.

**Jacob Cutter:** Thank you.

**Jacob Cutter:** Um, yeah, so I, uh, I think I already got a lot of questions answered by Marcel.

**Jacob Cutter:** So.

**Jacob Cutter:** So.

**Jacob Cutter:** So.

**Jacob Cutter:** In the last meetup, but I think in terms of like the case studies we're kind of doing right now, so would you say that that's probably the majority of the work that someone coming in would be tackling?

**Katja Wittfoth:** Yeah, yeah.

**Katja Wittfoth:** So definitely the first one, I think this is for the role of AI scientists to really understand like the baseline of current quality and measuring the content output and figuring out like where we should improve the pipeline, where we should improve the product.

**Katja Wittfoth:** And the visibility part, this is something that mostly will come later and figuring out like how can we actually use this as part of our product as well.

**Katja Wittfoth:** So like we should monitor and run this kind of like analysis on the regular.

**Katja Wittfoth:** in an automated way and figure out what is, because, you know, everything is changing in the search domain.

**Katja Wittfoth:** And today might be a trend to use TLDR, and this is what LLM loves to pick up.

**Katja Wittfoth:** Tomorrow might be not anymore.

**Katja Wittfoth:** So we need to constantly observe what tactics are right now bringing the most visibility for the client and implement that for all clients.

**Jacob Cutter:** I see.

**Jacob Cutter:** Yeah, it's interesting.

**Jacob Cutter:** Yeah, so because I guess what I'm wondering is, like, roadmap-wise, like, for an, like, I guess, applied AI scientist or an AI engineer coming in, which is kind of the direction I would lean as opposed to, like, data science these days, just based on, like, the amount of back-end and building I've been doing, would there be, like, component?

**Jacob Cutter:** of it that's kind of focused on replatforming and that kind of thing, like kind of building sort of a new system based on the feedback that I would be getting from whatever valuations, yeah, yeah.

**Katja Wittfoth:** Totally, that's exactly the job of how we see it and how, you know, Daniel, it is to really come in as an AI scientist, AI engineer, define this pipeline.

**Katja Wittfoth:** and develop the roadmap, what we need to change and go implement it and go change.

**Katja Wittfoth:** Cool.

**Jacob Cutter:** I think that makes sense, yeah.

**Katja Wittfoth:** Awesome.

**Jacob Cutter:** Yeah, I have to hop, actually.

**Katja Wittfoth:** I'm sorry, but...

**Katja Wittfoth:** No worries.

**Katja Wittfoth:** It's in the middle of daytime work time.

**Katja Wittfoth:** So thank you so much, Jacob.

**Katja Wittfoth:** That was fun and thanks for meeting me.

**Katja Wittfoth:** And Taka had his note taker, so he will be hearing from him.

**Katja Wittfoth:** Okay.

**Jacob Cutter:** Awesome.

**Katja Wittfoth:** Thank you so much.

**Katja Wittfoth:** Sounds good.

**Katja Wittfoth:** Thank you.

**Katja Wittfoth:** Bye.

**Katja Wittfoth:** you for the time.
