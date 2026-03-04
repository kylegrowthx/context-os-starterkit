# Surge AI Current Content Workflow 'Demo'

<metadata>
date: 2025-12-22
time: 20:01 UTC
duration: 24 minutes
organizer: Ismail Ajagbe
participants: Tamy Macedo, Ismail Ajagbe
fathom_recording_id: 110487117
fathom_url: https://fathom.video/calls/515042143
share_url: https://fathom.video/share/GGBs5x1ggY6v3zhrm5-mL9Msp2xb-yhS
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Ismail demoed Surge AI's new proprietary content generation workflow, which uses transcribed interviews from founder Edwin as the knowledge base backbone to replace Atlas's generic public-scraped content. The key insight is that section-by-section generation with step-by-step prompts produces substantively different, founder-voice-aligned content compared to one-shot generation, and this approach will be replicated in the new Atlas pipeline. Tamy will build the new pipeline incorporating Edwin's interview transcripts and templated prompts, generate a sample article this week, and iterate based on Ismail's feedback.

---

## Context

Surge AI is a portfolio company where Ismail works on content generation. Two months prior, Surge had kicked off a high-volume content strategy with its subsidiary Data Annotation team to produce 30 articles per week using Atlas, focused on SEO volume. However, founder Edwin paused production citing that the output was "low-quality BPO material" — generic and lacking the unique perspective he wanted the brand to convey. This created an internal conflict: the Data Annotation team was optimized for volume, while the Search team (under Edwin) demanded quality aligned with his specific frameworks and voice. Rather than reverting to generic tooling, Ismail proposed and built a new solution: transcribing Edwin's interview videos (4-5 videos) into a Claude project alongside company docs and audience guidelines, then using step-by-step prompts to generate content that reflects Edwin's thinking. This meeting was a demo of that workflow for Tamy, an Atlas specialist at GrowthX, so he can replicate the same quality-focused approach in the new Atlas pipeline.

---

## Relevance

**To GrowthX Delivery:**
- Proprietary knowledge base approach (transcribed founder interviews + company docs) is the backbone of quality content generation — generic public scraping fails to produce brand-aligned output.
- Section-by-section generation with templated prompts is critical; one-shot prompts consistently produce generic or nonsensical content.
- Manual publishing to Webflow takes 20 minutes per article; Surge identified automation as a future enhancement.
- Manual image generation (featured + in-article) is also a bottleneck identified for automation post-launch.

**To GrowthX Business Development:**
- Demonstrates a proven workflow pattern for handling founder-voice-critical clients where content quality is the primary blocker.
- Replicable approach: combine unique source material (transcripts), step-by-step generation, and iterative validation against ICP alignment.
- Ismail producing 5 sample articles as quality benchmarks shows the client expects rigor and wants to set standards upfront.

---

## Overview

- **Problem:** Founder Edwin paused content production, calling it "low-quality BPO material." This stemmed from a strategy mismatch between the Search team and its subsidiary, Data Annotation.
- **Solution:** A new workflow was built around a proprietary knowledge base of Edwin's transcribed interviews, replacing Atlas's generic public scraping to capture his unique perspective.
- **Method:** Content is generated section-by-section in Claude, as one-shot prompts produce generic output. The workflow is guided by a complex step-by-step prompt template.
- **Goal:** Replicate this quality-focused workflow in Atlas, using the new knowledge base as the pipeline's "backbone" to produce non-generic content.

---

## Key Topics

### The Problem: Quality Mismatch

  - **Initial Strategy (2 months ago):** A high-volume (30 articles/week), SEO-focused strategy was set with the Data Annotation team, using Atlas.
  - **Founder Feedback:** Edwin paused production, calling the content "low-quality BPO material" that was generic and lacked his unique perspective.
  - **Root Cause:** A strategy mismatch between the Data Annotation team (focused on volume) and the Search team (focused on quality and founder voice).

### The Solution: Proprietary Knowledge Base

  - **Core Insight:** The key to unique content is a unique source of truth.
  - **New Knowledge Base:** Transcribed interviews (4-5 videos) and company docs (audience, guidelines) were loaded into a Claude project.
  - **Function:** This proprietary data now serves as the "backbone" for all content generation, ensuring it reflects Edwin's specific frameworks and language.

### The Method: Section-by-Section Generation

  - **Process:** A complex, step-by-step prompt template guides the generation in Claude.
  - **Rationale:** This section-by-section approach is critical because one-shot prompts consistently produce generic or "gibberish" content.
  - **Validation:** Each section is reviewed for quality and ICP alignment before proceeding.

### Future Enhancements (Post-Quality Fix)

  - **Automated Webflow Publishing:** Automate the current 20-minute manual publishing process for the main blog collection.
  - **Automated Image Generation:** Automate the manual creation of in-article and featured images.
  - **Content-Type Templates:** Create distinct templates for guides, listicles, and comparison articles, similar to the "augment code" client's system.

---

## Action Items

**Tamy Macedo (GrowthX)**
- Build Atlas pipeline with Edwin transcripts + step-by-step prompts; generate 1 sample article; send to Ismail for review this week

---

## Transcript

**Tamy Macedo:** So let's discuss about the current workflow.

**Tamy Macedo:** I am responsible for creating one specific workflow for search on Atlas, and I do believe it would be pretty helpful for me to see how you do that today with your current system so I can replicate as much as possible with our internal workflow. So if you want me to walk through how you would do that today with the current resources, it would be very helpful to me.

**Ismail Ajagbe:** Okay. So I think I can just demo how I currently go about the content generation. Yeah, I think I can share my screen.

**Tamy Macedo:** Do you mind if I record? I'd like to have a reference for later.

**Ismail Ajagbe:** That's completely fine.

**Tamy Macedo:** Awesome. This meeting is being recorded. Perfect.

**Ismail Ajagbe:** Can you see my screen?

**Tamy Macedo:** Yeah, now I can see your screen.

**Ismail Ajagbe:** Can you see this Claude chat?

**Tamy Macedo:** Yes.

**Ismail Ajagbe:** Oh, fantastic. Okay. So let me give you a bit of context. Initially, our content production used to be in Atlas, and then...

**Tamy Macedo:** Yeah, I believe that this would be very helpful because I just started working here at the beginning of this month, so I don't have a lot of history of the current status of the project.

**Ismail Ajagbe:** Oh, okay. So let me chat through this.

**Ismail Ajagbe:** So, yeah, about two months ago, I think that's when we started content for Search, and the strategy was between Surge and the subsidiary company of Search called Data Annotation. So all the strategy we did was with the Data Annotation team. The Search team wasn't really active in the conversation.

Then the strategy was that we would produce about 30 articles per week. They just wanted us to move very fast, and we were using Atlas to scale production every week. Everything was based on volume and SEO perspective, and the articles were doing a great job from an SEO compliance standpoint.

But then all of a sudden, out of nowhere, we received a message from Edwin, the Search founder, and he was very blunt. He said, "Our content feels like low-quality BPO material. It's very generic and isn't what I wanted." The founder had a mission: a platform where AGI development is being pioneered. But our initial strategy was done with the Data Annotation team, so it was kind of like an internal conflict situation — there wasn't a sync between the Data Annotation team and the Search team.

When we received the message, we immediately paused content production to address the situation. We brainstormed and came up with a solution: we would use a different source of truth for writing articles. Atlas currently follows a template. Whenever an assignment is produced, it scripts public information. For example, for an article on how to avoid burnout, it scripts the same information and presents it the same way. So the way to approach this differently is to get inside Edwin's head and think about how he would approach every article.

I transcribed all the interviews I could get my hands on — about four or five videos — and put them all into a Claude chat. Let me show you.

**Tamy Macedo:** Can you see the screen?

**Ismail Ajagbe:** Yes.

**Tamy Macedo:** I can see your screen. Okay, let me ask — do you use Claude?

**Ismail Ajagbe:** So this is a transcript of an interview session he had. This transcript contains about four videos, plus all the entire documentation, the audience personality, the writing guidelines. After I added this into the project, I created a prompt template — a step-by-step prompt on how to use those transcripts as a source of truth to write the articles.

The idea is: for this assignment, how would Edwin approach this article differently? How would Edwin write this article? That's fundamentally different, right? This is the prompt I used and am now using. I can share this chat with you so you can go through the prompts later. Should I send this on Slack so we can have a history of the conversation?

**Tamy Macedo:** Slack, so we can have history of the conversation.

**Ismail Ajagbe:** Okay, let me share this. So using this prompt, I go step-by-step to generate the content section-by-section. The idea is: for this topic, how would the person in this transcript approach it? This is like a template. The only thing I change is the title. The idea is to ensure that whatever we produce is fundamentally different from what already exists out there.

Let me fetch another resource for you. In this document, I've comprehensively documented everything. So these five articles are examples of what a good article should look like — the minimum benchmark for each article. The fundamental problem is that we need a library where the pipeline fetches information to write something different. I included that inside the workflow, which is like a flowchart diagram. I left the videos I transcribed inside the project as well.

So, fundamentally, I start by asking Claude to give me sections or a brief based on the transcript. One thing I always try to avoid is one-shotting the entire article. Any time I've one-shot an article, it produces generic content or gibberish. So I go through it step-by-step, making sure that the humanity of the thinking is thoroughly embedded in the process.

And as you can see, I got a brief. If the brief doesn't make sense, I prompt it to change things. I make sure there are ways to keep it SEO-compliant. So I go through section by section, validating each section, making sure that what it's suggesting would make sense with our ICP. I go through that section by section, step by step, up until I finish the entire article. Then I repeat the process for another article.

**Tamy Macedo:** Yes, it helps. It helps so I can understand the thought process of how you currently do it, so I can emulate the same behavior on Atlas.

**Ismail Ajagbe:** Yeah, yeah. So I think we're building a new pipeline, and we discussed some extra features as well. Currently, we do heavy work publishing articles in Webflow, and it's very resource-intensive. It takes about 20 minutes or so to publish an article. We're looking at adding an automated publishing feature to the pipeline. That's the first feature.

Then, right now, featured image generation is also being done manually. Same thing for in-article images. So we're looking at whether that's possible as well.

Lastly, the content types. These are our clients who work with Augment Code. Augment Code has a different template for each content type. Guides are different, listicles are different, comparison articles are different. So we're looking at whether we can have something like that as well. For comparisons, there's a template. For listicles, there's a template. For guides, there's a template. But the top priority for us right now is to get the quality and tone back.

**Tamy Macedo:** One question. For Webflow, I know that this is an extra feature that we'll be working on after we have the content pipeline working with the quality that you guys want. But just to clarify, do you use more than one collection? Or is automating mostly on the blog post collection? What collections do you use right now, and which would be most helpful to start with?

**Ismail Ajagbe:** So right now, we just use one collection in Webflow for everything. If you need login details, I can get them for you.

**Tamy Macedo:** Okay, awesome. I think you understood pretty well what the challenge is and the potential paths. It's very helpful that you already have the Notion documentation and that you're sending me the prompts so I can incorporate those into Atlas. Is there anything else that's important for me to know while I'm working on the new Atlas pipeline?

**Ismail Ajagbe:** I think that's pretty much it. But the fundamental problem is that it's very, very important for the pipeline to have a different knowledge base rather than just public scraping. That's where the fundamental problem is. Using this project knowledge, I'm writing from the transcript. If you look at the good articles I sent, you'll see they're fundamentally different from what already exists. The knowledge base is different. And I think that's going to be very important in the new pipeline. The public knowledge base is also helpful for scraping and seeing what competitors currently have, but this proprietary knowledge base is going to be the backbone of the pipeline.

**Tamy Macedo:** Awesome. I think it's pretty clear — the main pain point is making the content more personalized to their frameworks. What I'll do is generate one sample with the new pipeline. I'll likely do that this week so we can review. If everything is fine, we proceed. If there are points that could be better, send me specific feedback, and we can iterate from there. Thank you so much, Ismail, for explaining all of that. I'll definitely send you a sample and get your thoughts. But I feel pretty contextualized to start.

**Ismail Ajagbe:** Thank you. Yeah, thank you so much, Tamy. And like I said, if you have any questions, just reach out. For sure. Cheers.
