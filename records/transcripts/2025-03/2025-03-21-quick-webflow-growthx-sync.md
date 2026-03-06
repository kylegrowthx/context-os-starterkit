# Quick Webflow/GrowthX sync 

<metadata>
date: 2025-03-21
time: 18:44 UTC
duration: 14 minutes
organizer: Bridget McGillivray (GrowthX)
participants: Marcel Santilli (GrowthX), Bridget McGillivray (GrowthX), Bruno Santilli (GrowthX), Jessie Ouellet (Webflow), Steven Stasevych (Webflow), Josh Andrews (External Legal)
fathom_recording_id: 53236409
fathom_url: https://fathom.video/calls/258132039
share_url: https://fathom.video/share/5Yi1NUcv3aGYb6HFS32btwyfyUy2yyzx
source: fathom
enriched_on: 2026-03-04 03:30 UTC
</metadata>

---

## Summary

Marcel walked Webflow's legal team through GrowthX's AI workflows, explaining that GrowthX uses only publicly available data via APIs like OpenAI and Perplexity—never ingesting client proprietary information. Jessie Ouellet from Webflow's legal had concerns about whether GrowthX's models would train on Webflow's data; Marcel clarified the architecture uses a chain of LLMs with proprietary IP in prompts and human editors, with all inputs sourced externally. The team discussed how future data sharing scenarios would be scoped separately, similar to internal controls like not pasting company financials into ChatGPT, and agreed to move forward with the engagement.

---

## Context

Webflow is a GrowthX customer and partner on multiple fronts. GrowthX has migrated several of its own clients to Webflow and manages their CMS, making GrowthX both a customer and advocate of the platform. This meeting was called at Webflow's request to address Jessie Ouellet's (Webflow legal) concerns about GrowthX's AI usage and data handling practices as part of the ongoing engagement and MSA review. Josh Andrews, Webflow's external legal counsel, joined to hear technical details. The discussion was specifically to clarify whether GrowthX's AI workflows would train on Webflow's proprietary data or expose Webflow to liability, a common legal concern around vendor use of generative AI.

---

## Relevance

**To GrowthX Delivery:**
- Demonstrated DNAI (prospect research) workflow architecture using only public data sources, APIs, and website scraping—critical for explaining GrowthX's methodology to AI-conscious clients
- Deep researcher workflow example shows how GrowthX structures LLM chains with human editors for quality control and client-specific customization
- Process of avoiding proprietary data ingestion is now documented and repeatable for future client conversations

**To GrowthX Business Development:**
- Deal unblocked: Webflow's legal team moved from "uncertain" to "much more comfortable" with the MSA after understanding GrowthX's architecture
- Strong advocate relationship: Webflow team expressed enthusiasm about the engagement after the call
- Webflow as reference: GrowthX's ability to explain AI workflows without training on client data is now a differentiator vs. other content vendors

**To CheckThat:**
- Real-world validation that clients are asking about AI transparency and data usage before signing agreements
- CheckThat's AI visibility auditing methodology could address similar legal/compliance questions from other B2B SaaS customers

---

## Overview

- GrowthX uses only publicly available data and APIs (e.g., OpenAI, Perplexity) for their AI workflows
- No ingestion or training on client's proprietary data; focus on external sources
- Custom workflows developed for each client, guided by human editors familiar with the client
- Potential for future data sharing would be handled separately, with clear guidelines on non-proprietary info

---

## Key Topics

### GrowthX's AI Tools and Data Sources

  - Uses chain of LLMs with proprietary IP in prompts
  - Leverages APIs: OpenAI, Perplexity, SERP API
  - Scrapes public websites, sitemaps for relevant content
  - Generates queries based on learned info (e.g., "AI fraud prevention for banks")
  - Develops personas, jobs-to-be-done from public data

### Workflow Example: DNAI Prospect Research

  - Generates company overview: elevator pitch, executive summary, products, personas
  - Scrapes company website and sitemap (up to 200 pages)
  - Performs contextual searches based on initial findings
  - Develops detailed personas and jobs-to-be-done

### Custom Workflows for Clients

  - Adapted for each client (e.g., Webflow-specific context)
  - Managed by human editors and directors overseeing strategy
  - Example: Deep researcher workflow - breaks down topics, generates questions, finds answers
  - Stores only publicly available information for downstream use

### Handling Proprietary Information

  - Current process avoids ingesting any proprietary client data
  - For specific needs (e.g., popular prompts data), clients provide non-proprietary summaries
  - Similar to internal controls for employees (e.g., not pasting financials into ChatGPT)
  - Any future proprietary data handling would be a separate scope/discussion

### GrowthX's Relationship with Webflow

  - GrowthX is a Webflow customer and has migrated several clients to Webflow
  - Manages CMS for clients, advocating for Webflow's platform
  - Excited about potential engagement and synergistic relationship

---

## Action Items

**Jessie Ouellet (Webflow)**
- Review final pass of MSA with GrowthX, incorporating new AI/data usage understanding and internal controls language

---

## Transcript

**Bridget McGillivray:** Hey, Josh.

**Josh Andrews:** Hi.

**Bridget McGillivray:** How are you?

**Bridget McGillivray:** Hi, Jessie.

**Bridget McGillivray:** Nice to meet you.

**Jessie Ouellet:** Hi. Nice to meet you, Bridget.

**Jessie Ouellet:** She's our head of legal.

**Josh Andrews:** Yeah, I worked with her. She's great.

**Jessie Ouellet:** Yes, she definitely is. She's our fearless leader over here.

**Bridget McGillivray:** Okay, will you be able to answer the questions?

**Jessie Ouellet:** Well, thank you all for going through our edits and working with us. We definitely appreciate it. Really, my questions are a little deeper than the answers provided about how you use generative AI, what tools are in your product, and whether those tools will train models based on our data. What's your process for using gen AI? At what point do you start turning it on?

**Bridget McGillivray:** She's wanting a summary of what AI tools we're using, which LLMs, how data gets fed into the LLMs, and whether we're training any models. Kind of that overall picture.

**Marcel Santilli:** Hey, Jessie. Thanks for joining. Yeah, of course. Those are similar questions Reddit asked us last year. The best way to think about it is: are you familiar with ChatGPT's Deep Research? The way to think about it is the only thing we're using to feed into our workflows is externally available data, right? When we're planning how to enrich a page or what content to create, our workflows ping different APIs like Perplexity's API, OpenAI, SERP API, and find different sources to understand the topic better. Then we run them through our tools to understand if they're relevant to Webflow. And as we're processing it, think of it as a chain of LLMs that take all that input and have a lot of proprietary IP in terms of expert knowledge on how to think through it—that's represented in the prompts. It goes through the whole process with an editor familiar with the client—in this case, Webflow—guiding that process along. So it's all externally available data. We're not trying to ingest anything internal or proprietary.

**Jessie Ouellet:** Gotcha, thank you. I appreciate that. When you say externally available data, what's an example of that?

**Marcel Santilli:** Yeah, let me do an example that might be helpful. I can share my screen. I think illustrating is always better. This is one of the workflows we're running for a client—it's our DNAI, or prospect research tool. It's doing research on a company, understanding the elevator pitch, executive summary, overview, products, personas. It did this by going into their website, scraping their website and sitemap to understand what other pages would be relevant—up to 200. It scrapes the content and understands it better. Then it does queries and searches related to what it's learning. For instance, one context is for financial institutions looking to enhance fraud detection. It generated queries like "AI fraud prevention for banks." Our workflows take those queries, search for them, and start to understand and learn from the results. Then it develops personas and understands what the jobs to be done are for those personas—for example, "provide real-time fraud detection." It comes up with even more queries around jobs to be done. This is one example of one workflow, and all it's using is publicly available APIs—Perplexity's API does some of the research itself as well.

**Jessie Ouellet:** Got it. Okay. That was very helpful. Thank you.

**Marcel Santilli:** And this is an example of the workflows we would custom develop for Webflow. Think of it as a managing editor and director overseeing the entire strategy for how we enrich pages and create high-quality content. The editors and experts use these workflows, but they're adapted to each client. With Webflow, we would feed in context about what Webflow is, what it does, the product features—all publicly available information. This is an example of our deep researcher workflow where we take a topic, break down the research, generate research questions, and find answers. As it finds sources, it stores that information for downstream use. But again, it's only storing publicly available information.

**Jessie Ouellet:** Okay, yep. That makes sense. That definitely helps. Thank you. And then, I think Bridget mentioned something on the MSA: if Webflow ever wanted data ingested, or if we wanted to say okay, put in confidential information or give you other data than what's publicly available, is that a separate scope?

**Marcel Santilli:** We've run into this more recently in one of the projects we haven't kicked off yet. In that case, our solution is: don't give us proprietary information, give us a report of what we need to know that wouldn't be proprietary. For example, a coding agent platform wanted us to use data about the most popular prompts on their platform to figure out what pages to build templates for. Traffic data isn't proprietary—we can estimate that. But code snippets people are using—that's not truly proprietary. It's mostly usage of an iframe or certain code snippet that we can generalize. We take the most popular one and create pages for Webflow so that when people use those code snippets, they have pre-packaged ones that can be reused and found more easily. We're looking for those kinds of use cases versus ones that are truly IP or have some crazy logic. If that came up later, it would be better to cross that bridge then, because otherwise we wouldn't know what we're dealing with.

**Jessie Ouellet:** Yeah, exactly. That makes sense. It's more internal controls on your side to make sure that data isn't given to us. Just in case someone wanted to pass it along.

**Marcel Santilli:** Very similar to what our employees do—we don't allow copying and pasting to GitHub. Like, don't copy and paste company financials to ChatGPT. Same thing: we're not asking for your financials.

**Jessie Ouellet:** Yeah, exactly. That makes sense. Well, I feel much more comfortable. I'll go back and review the final pass to make sure that aligns. Thank you. I definitely appreciate you all taking the time to speak with me.

**Bridget McGillivray:** Steven, is there anything on your side? Any open questions?

**Steven Stasevych:** No, not on my side.

**Marcel Santilli:** I think we're almost there then. We're super excited. We love Webflow. We're a customer on a small scale, but we've also migrated several of our customers to Webflow. Because everything we do publishes and we manage people's CMS, we're a huge advocate of Webflow. It's one of the reasons we're really excited for this engagement.

**Jessie Ouellet:** Awesome. Well, I know the team's really excited too.

**Marcel Santilli:** Yeah, same thing with Webflow. They're an investor, a customer, and we're a customer of them. We love these kinds of relationships where we can use the product and help them grow and vice versa. So we're excited to hopefully get to work soon.

**Jessie Ouellet:** Yeah, definitely. Same.

**Jessie Ouellet:** Well, happy Friday, everyone.

**Jessie Ouellet:** Thanks so much. I'll get that back to you.

**Jessie Ouellet:** Thank you, Jesse.

**Jessie Ouellet:** Thank you. Bye.
