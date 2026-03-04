# Igor Jankov - Hiring Manager Screen - Panzer | Managing Editor

<metadata>
date: 2025-11-19
time: 20:00 UTC
duration: 25 minutes
organizer: matthew@growthx.ai
participants: Matthew Panzarino (GrowthX), Igor Jankov (Proofed)
fathom_recording_id: 102941680
fathom_url: https://fathom.video/calls/479702655
share_url: https://fathom.video/share/WytucAPbcUho1c2fhCsmw2zgERW3Ez5G
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Screening interview for GrowthX's Managing Editor role. Matthew Panzarino assessed Igor Jankov (Service Delivery Support at Proofed) on his editorial philosophy, AI-generated content experience (CopyPress and AI fact-checking with Perplexity), and large-scale editorial workflows (1M words/month on Chinese web novels). Igor demonstrated strong understanding of prompt engineering and style guide development as leverage-building tools, and Matthew explained GrowthX's content pipeline model—where the ME role focuses on reducing manual work through better prompts and context engineering rather than direct editing, starting from a 70/30 manual-to-prompt split and shifting toward 30/70 over time.

---

## Context

Igor Jankov is a candidate for GrowthX's Managing Editor role. He currently works at Proofed (a content services company) in Service Delivery Support, where he manages editors, develops style guides, and performs quality assurance—skills directly applicable to the ME position. Matthew Panzarino, GrowthX's Chief Content Officer, conducted this screening interview as part of the hiring process. Matthew explained that GrowthX treats writers as pipelines and the ME role as managing those pipelines for quality and efficiency, not managing people—a distinctly different model from traditional editorial organizations. The conversation focused on Igor's editorial philosophy, his hands-on experience improving processes for large teams, and his background working with AI-generated content from clients like CopyPress.

---

## Relevance

**To GrowthX Delivery:**
- Candidate brings proven methodology for identifying and fixing process bottlenecks (XML training for JPMorgan Chase team, Perplexity automation for fact-checking). This aligns well with GrowthX's need to improve AI pipelines incrementally.
- Strong grasp of "AI-isms" (clichéd language, keyword stuffing, repetition) and how to address them via prompt/context engineering—core skills for the ME role.
- Demonstrated ability to train large teams (40+ editors) on new workflows and tools in compressed timelines.

**To GrowthX Business Development:**
- Candidate's experience at Proofed handling high-volume client work (1M words/month on Chinese web novels, 35-40 SEO articles/week) suggests he can manage scaling issues GrowthX may encounter as the content business grows.
- Background with Perplexity and make.com automation shows initiative in exploring tools for efficiency gains—values-aligned with GrowthX's Atlas platform philosophy.

---

## Overview

- **Candidate Profile:** Igor Jankov (Proofed) has direct experience managing AI-generated content (CopyPress) and large-scale editorial workflows (1M words/mo).
- **Core Philosophy:** Editorial quality hinges on clear style guides and iterative prompts, which prevent "AI-isms" like clichés and keyword stuffing.
- **GrowthX Role:** The job is to build leverage by improving AI pipelines, not to perform manual edits. The goal is to shift from a 70% manual/30% prompt-engineering split to the reverse over time.
- **GrowthX Tech:** The company is building "Atlas," a unified platform for the full content lifecycle (production, analytics, opportunities) to replace its current tool stack (Notion, Airtable, Linear).

---

## Key Topics

### Candidate Experience & Philosophy

  - **Current Role:** Service Delivery Support at Proofed, managing editors, developing style guides, and performing QA.
  - **Core Belief:** Unclear style guides are the root cause of most editorial issues, whether for human editors or AI prompts.
  - **Quality Improvement Process:**
      - Identifies underperforming editors via metrics.
      - Analyzes their work for consistent issues.
      - Provides targeted feedback and resources to correct process or knowledge gaps.

### Project Examples & Scale

  - **JPMorgan Chase (XML Training):**
      - **Problem:** A 40-editor team was assigned a project editing XML manuals with no prior experience.
      - **Solution:** Igor learned XML, created training materials, and ran rapid workshops to enable the team.
      - **Outcome:** The project is ongoing, using Igor's original guides.
  - **Search Lab (AI Fact-Checking):**
      - **Problem:** Editors were manually fact-checking specs in AI-generated car articles, which was slow and costly.
      - **Solution:** Integrated Perplexity via Google Sheets and make.com to automate fact-checking, highlighting only data needing human review.
  - **Chinese Web Novels (Large-Scale Editing):**
      - **Scale:** 1 million words/month.
      - **Challenge:** Required editors to understand Chinese idioms, adapt content for a US audience, and maintain a sprawling character/plot database for continuity across 600+ chapters.

### GrowthX Role & Philosophy

  - **Primary Function:** Managing Editor (ME) manages content pipelines (AI writers), not people.
  - **Key Metric:** Success is measured by building leverage and reducing manual work, not by the volume of edits made.
  - **Workflow Evolution:** The role is expected to shift from a 70/30 manual-to-prompt split to the reverse as pipelines improve.
  - **Core Task:** Prompt and context engineering to improve AI outputs.
      - **Prompt Engineering:** Direct instructions to the LLM.
      - **Context Engineering:** Providing representative examples (e.g., CTA formats) for the LLM to learn from.

### GrowthX Team & Tech Stack

  - **Team Structure:**
      - **ME:** Manages AI pipelines.
      - **Engagement Manager:** Client-facing; develops strategy.
      - **Editorial Director:** Manages hiring, onboarding, and training.
  - **Tech Stack:**
      - **Current:** Notion, Airtable, Linear, SEMrush, PageRank.
      - **Future:** "Atlas," a proprietary platform to unify the content lifecycle (production, analytics, opportunities) and replace the current tool stack.

---

## Action Items

**Matthew Panzarino (GrowthX)**
- Follow up with Igor Jankov regarding next steps for the Managing Editor role

---

## Transcript

**Igor Jankov:** Hello.

**Matthew Panzarino:** How are you doing?

**Igor Jankov:** Pretty good.

**Matthew Panzarino:** Wonderful.

**Igor Jankov:** Thank you for taking the time to meet and chat.

**Matthew Panzarino:** My name is Matthew. I'm the chief content officer here at GrowthX. So my focus is largely on content quality and the process that leads us to quality. We use internal tooling to create content, but we also use humans and people—kind of the intersection of those two. I'm happy to hear a little bit about you and I want to talk through a handful of things. I would love to anchor the discussion mostly in some practical experience that you've had in these areas. I think that's the best way to go about it.

**Matthew Panzarino:** Talk to me a little bit about editorial quality and judgment. How do you personally judge whether a piece of content is high quality and how do you know when it's good enough?

**Igor Jankov:** Sure. So I'm Igor. I currently work at Proofed as a service delivery support. It's a role where we wear many hats—there's a little bit of editor management, style guide development, and QA (quality assurance) of the content. When it comes to evaluating quality, I'd say a very clear style guide is a big part of it. I think most of the issues when managing editors come down to unclear style guide requirements. And I think that also transfers to writing requirements for AI to generate content. Most of the issues can be traced back to just having better briefs and better explanations to the AI—what you want done, how you want it done, what you want it to avoid, and iterations as well.

**Igor Jankov:** For AI-generated content specifically, one of our biggest clients is CopyPress. They deliver a lot of AI-generated content—a big workload. I have a lot of experience not just editing it, but nailing down the style guide for how it should be edited, what editors should think about, quality checking their work, reviewing their work, and providing feedback and training through workshops.

**Matthew Panzarino:** Yeah, that makes sense. You mentioned this process—talk to me a little bit about the work you've done to improve it or define it. Walk me through that.

**Igor Jankov:** I would use metrics to identify editors that are underperforming or have inconsistent performance. Then I would look through their documents to see what works and what doesn't, identify consistent issues, and write up feedback and guidelines for them to follow along with resources. So I take a hands-on approach to correcting either process issues or knowledge gaps from editors.

**Matthew Panzarino:** And can you talk to me about a time that you did that? I'd love to hear how you handled that—how you identified the issue first and then how you identified an improvement to the process.

**Igor Jankov:** Sure. One of the more recent things was when JPMorgan Chase sent us internal technical manuals, and only a few days before the pilot project started, they told us it was all going to be in XML. By that point, we already had a group of about 40 editors, none of whom knew XML. So I took it upon myself to get a crash course in XML, write down the requirements, and train the editors through rapid workshops. To this day, that project is still ongoing, and they're still using the videos and guides I made. A lot of the editors didn't have any coding experience—middle-aged women, stay-at-home moms—so I really had to make it legible and accessible.

**Matthew Panzarino:** Yeah, formatting and unexpected formats are always a fun challenge in client delivery.

**Igor Jankov:** Always a surprise. Maybe they should have let us know before we got 50 editors together.

**Matthew Panzarino:** Exactly. Okay, let's talk about the AI and LLM aspects of the work you've done. Can you talk about a time you've used AI or LLM-based tools to improve a content process or workflow?

**Igor Jankov:** Yeah, for the Search Lab client, we got AI-generated content focused on car articles for car dealerships. This involved comparisons and specs—very numbers-heavy. Freelance editors paid by the hour were spending a lot of time fact-checking everything by hand. So I implemented a rudimentary Perplexity integration where we'd get highlights of what's correct and what's not, and it would flag the parts that still needed double-checking. That removed a lot of the manual fact-checking work for engine specs and car features.

**Matthew Panzarino:** Nice. Did you use Zapier for the automation?

**Igor Jankov:** No, it was through Google Sheets and make.com. We'd drop the specs in, have Perplexity check them, and return the results.

**Matthew Panzarino:** Yeah, that makes sense. What about other LLM tooling you use in your day-to-day work?

**Igor Jankov:** I've been passionate about AI-generated content since Google Deep Dream was producing fractal images of dogs. When DALL-E first came out, I was so impressed seeing it generate simple images. I use ChatGPT and Claude regularly—Claude especially when I was on the tech team at Proofed for coding projects. In preparation for this role, I got deeper into make.com to set up end-to-end content generation. I built a sheet that takes a keyword, finds related keywords, and uses those to generate and iterate on content. I set up a rudimentary system to understand how GrowthX works.

**Matthew Panzarino:** When you're generating AI content, how do you look at quality? What issues do you look out for?

**Igor Jankov:** I call them AI-isms. When you use the same models without high-quality prompts, the content tends to have clichéd language and repetition. With keywords, I watch out for keyword stuffing—they need to appear naturally. These things tip me off that we need to iterate again or clarify the starting prompts.

**Matthew Panzarino:** Yeah, certain phrases are hard to get away from.

**Igor Jankov:** Exactly. It's a consistent pattern.

**Matthew Panzarino:** What kind of volume of content have you worked with? Talk about the scale of projects you've managed.

**Igor Jankov:** My biggest project involved delivering around 1 million words per month—about 250,000 words per week. We were editing machine-translated content from Chinese web novels. Before that project, I'd never heard of web novels. They're incredibly popular in China—imagine a book that just keeps going for 600-700 chapters. Beyond the language challenges, we needed editors to understand Chinese idioms and adapt content for an American audience while maintaining continuity. We had to keep a massive spreadsheet of character relationships and plot points because after 600 chapters, even the writer forgets what's happened.

**Matthew Panzarino:** I never thought about a novel that sprawling needing a character database.

**Igor Jankov:** Yeah, it starts easy in chapter 50, but by chapter 600, you have hundreds of characters with previous interactions. The writer tends to slip on details.

**Matthew Panzarino:** That's a unique challenge. What about more recent projects?

**Igor Jankov:** More recent work is focused on SEO blog articles—about 35-40 articles per week.

**Matthew Panzarino:** Got it. Do you have any questions for me about how we work?

**Igor Jankov:** Yeah, I was reading the job description and wondering how much of the Managing Editor role is designing prompts versus reviewing and refining outputs.

**Matthew Panzarino:** Good question. It's variable week to week. If your pipelines are in good order and delivering high-quality content, you can edit something within a handful of minutes and have it ready for client delivery. Then there's not much prompt engineering to do. However, if the pipeline isn't in good shape, your job skews heavily toward improving the inputs—the prompts and context—so you have less manual work. I view that as integral to the role. There's no reason delivery should feel as tough on day one as day 60. You should be building efficiency.

**Igor Jankov:** Right. Building leverage every day.

**Matthew Panzarino:** Exactly. I'd say it starts at about 70% manual, 30% prompt engineering, and flips closer to 30/70 over time. Prompt engineering and context engineering are separate but interrelated—they're how you build leverage. And I want to be clear: there's no higher value attached to manual work here. Some organizations say "you didn't do enough if you didn't change enough words," but for us it's the opposite. We value how well you reduce manual labor while maintaining quality.

**Igor Jankov:** I like that perspective. That's really good.

**Matthew Panzarino:** It's refreshing. There's a lot of stigma around LLM-constructed content in the industry, but we've found that with proper constraints and human intervention, we can deliver high-quality, readable, useful, factually accurate copy at scale. That's the company's premise. We've had success, though we're not at 100% yet. But there's evidence it's possible, and we're happy with the direction.

**Igor Jankov:** That sounds fantastic. Another question—how is the editorial team structured?

**Matthew Panzarino:** The basic structure is that we view writers as pipelines. You as a Managing Editor manage the pipeline, not people. Managing Editors work within pods alongside Engagement Managers, who are client-facing and develop strategy. You have a conversational relationship with the EM—you should have opinions on content shape and function, but the onus isn't on you to manage client calls. The Editorial Director handles hiring, onboarding, and training, and reports to me.

**Igor Jankov:** That makes sense. I understood Liz mentioned you use Linear and Notion?

**Matthew Panzarino:** Yes, we use those. Our main tech stack is Notion, Airtable, and Linear. We'll probably always use Slack and Notion, and likely Linear. If you've used anything like Trello or Asana, you'll be fine with Linear. But the tools we're really building are in Atlas, our proprietary platform. Not all components are ready yet, so some functions living in Airtable, Notion, and Looker dashboards will eventually move into Atlas. We're developing it because you need a holistic view of performance and opportunities alongside production. You can't produce in isolation—you need data feeding the funnel and identifying opportunities.

**Matthew Panzarino:** Imagine opening Atlas each morning and seeing the content you've produced, how it's performing, your production pipeline, and opportunities Atlas has identified—content gaps, keyword gaps, traffic patterns worth exploring. Right now it's a mix of SEMrush, Airtable, and PageRank. Atlas will eventually unify the entire cycle from research through delivery and analytics.

**Igor Jankov:** So more of a holistic, end-to-end view?

**Matthew Panzarino:** Exactly. You need analytics to understand performance, opportunities to leverage those analytics, production to create the content, and feedback loops. Atlas will be a big lift in connecting those pieces.

**Igor Jankov:** That sounds really interesting.

**Matthew Panzarino:** Great. I think we're good from my end. Do you have any more questions?

**Igor Jankov:** No, I think that clears it up. I'm satisfied with my questions.

**Matthew Panzarino:** Great. We'll reach out with next steps and go from there. Thanks, Igor.

**Igor Jankov:** Sounds good. Thanks for your time.

**Matthew Panzarino:** All right, you too. Bye.
