# Lovable <> GrowthX Weekly Sync

<metadata>
date: 2026-02-25
time: 16:30 UTC
duration: 22 minutes
organizer: team@growthxlabs.com
participants: Megan Dickey (GrowthX), Georgemaine Lourens (GrowthX), Nicolas Castellanos (GrowthX), Sam Vinden (Lovable), Vikas Bhagat (Lovable)
fathom_recording_id: 125284656
fathom_url: https://fathom.video/calls/578565745
share_url: https://fathom.video/share/PotjdqzQGxx4YrTq9gz2cLDAQ63HdJXH
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

GrowthX and Lovable aligned on three core initiatives: creating blog posts and guides for Lovable's top 5–10 use cases, automating integration documentation generation using a 3-part source of truth (PRDs, PMM briefs, technical docs), and establishing quality benchmarks for template creation through Lovable-provided examples. Content volume will adjust from 15 to 10 items weekly starting in two weeks.

---

## Context

This weekly operational sync between GrowthX's content and engineering teams (Megan, Georgemaine, Nicolas) and Lovable's product leadership (Sam, Vikas) addresses scaling challenges in template and documentation production. GrowthX uses Atlas (internal OS) to automate template spec generation from research artifacts and personas, but lacks quality standards. Lovable is working to improve upstream documentation (PRDs and PMM briefs) to enable accurate automation. The collaboration centers on establishing inputs and quality bars that allow both teams to work efficiently and maintain content accuracy at scale.

---

## Relevance

- **Content Strategy**: New use-case content initiative targets Lovable's top 5–10 templates; cross-referenced with keyword research for SEO alignment
- **Product Marketing**: Integration docs automation reduces manual workload; depends on improved PRD and PMM brief quality from Lovable
- **Engineering**: Workflow automation (Nico) estimated at 3-day build; requires well-structured source documents and calibration time
- **Process Improvement**: Quality benchmarks for templates established via Lovable examples; Notion/Airtable artifact sharing enables feedback loops
- **Capacity Planning**: Content volume decrease (15→10 items/week) reflects smaller task list and allows for quality focus

---

## Overview

- **New Content Initiatives:** GrowthX will create content (blogs, guides) for Lovable's top 5–10 use cases and automate integration doc generation.
- **Template Process Refinement:** Vikas will provide quality examples to set a consistent standard for GrowthX's template creation, which currently lacks a benchmark.
- **Source of Truth:** Vikas will provide the 3-part source of truth for integration docs (PRD, PMM brief, technical docs) by EOW, enabling Nico to build the automation workflow.
- **Content Volume Adjustment:** The steady-state content volume will decrease from 15 to 10 items/week, starting in two weeks, to match a smaller remaining task list.

---

## Key Topics

### Template Creation Process Review

  - GrowthX's template creation process uses Atlas, an internal OS, to feed LLMs with artifacts (personas, research) to generate specs.
  - **Problem:** The process lacks a consistent quality benchmark for app templates, which vary widely in complexity.
  - **Solution:** Vikas will provide 2–3 examples across the complexity spectrum to establish a clear quality bar.
  - **Action:** Megan will share the Notion/Airtable source documents for these artifacts, allowing Vikas to review and provide feedback.

### New Content Initiative: Use Cases

  - **Goal:** Promote Lovable's top 5–10 use cases to showcase the platform's capabilities.
  - **Format:** Blog posts and guides.
  - **Action:** Vikas will send the project brief with the use case list.
  - **Strategy:** GrowthX will cross-reference the list with keyword research to prioritize content that aligns with user search intent.

### New Content Initiative: Integration Docs

  - **Goal:** Automate integration doc generation to scale production beyond the current manual process.
  - **Source of Truth:** Vikas defined a 3-part input for the automation workflow:
      - Product Requirements Doc (PRD)
      - PMM Brief (messaging, audience)
      - Technical Docs (product docs)
  - **Constraint:** The current quality of PRDs and PMM briefs is low, which could compromise the accuracy of the automated output.
  - **Action:** Vikas will provide a handful of these source documents by EOW for initial testing.
  - **Timeline:** Nico estimates a 3-day build for the workflow, followed by a calibration period to refine outputs.

---

## Action Items

**Vikas Bhagat (Lovable)**
- Send Megan use-case brief with top 5–7 list by EOW; Megan then cross-checks against keyword research
- Send Georgemaine 2–3 template quality examples (spanning simple to complex) to establish quality bar
- Send Megan 3-doc integration packages (PRD + PMM brief + technical docs) for 3–5 integrations by EOW; Nico then builds automation workflow

**Megan Dickey (GrowthX)**
- Grant Vikas access to Airtable/Notion workspace containing source artifacts (personas, research, products)
- Point Vikas to specific artifact locations for review and feedback
- Integrate new use cases into content plan after keyword research validation

---

## Transcript

**Megan Dickey:** This meeting is being recorded. [Brief small talk and personal updates omitted]

---

**Megan Dickey:** I'm a director here at GrowthX, taking lead on the Lovable account. I've been working with Sam for about two to three months. We also have Georgemaine and Nico—they're our two lead engineers on the Lovable account.

**Megan Dickey:** Nico is often tasked with building out workflows—he's been working on the tools workflow. Georgemaine takes lead on the templates and making sure those are all getting created and looking good. She has a design background.

**Megan Dickey:** Hey, Vikas, how are you doing?

**Vikas Bhagat:** Good. It's great to meet you all.

**Megan Dickey:** Sam had mentioned that you had some thoughts on the template creation process. That's why I wanted to bring Georgemaine and Nico since they handle everything from the engineering perspective.

**Vikas Bhagat:** Yeah, I'll walk you through what I'm hoping to get done and see if GrowthX could help support. We have a lot of use cases for Lovable that people just aren't aware of. We have a list of about a hundred use cases, and I've narrowed that down to the top 5 to 10 use cases—specifically the top 5 to 7 that are more of our core segment—that I really want to get out into the world.

**Megan Dickey:** Are you envisioning them as templates, as guides, or any type of content?

**Vikas Bhagat:** I think blog posts and guides would be what I'm thinking.

**Megan Dickey:** Okay. Would you be able to send me that specific list so we can match it up with some keyword research to make sure we're targeting the right things?

**Vikas Bhagat:** Sure. I can send you the project brief with the list.

**Megan Dickey:** Great. And regarding the templates—Georgemaine, you have a question?

**Georgemaine Lourens:** You mentioned that internally you're working on the top 100 use-case templates. If we're going to produce those, some will be apps and some will be tools. Do you have quality bar examples that we can aim to hit? Because they can be feature-rich, right?

**Vikas Bhagat:** I don't think we have a consistent example of what best-in-class high quality is. They do range in maturity and power. Some are very lightweight, whereas others are really robust. Why don't I source maybe 2 to 3 examples across that spectrum and share them with you all?

**Georgemaine Lourens:** That will be perfect.

**Megan Dickey:** Georgemaine and Nico, can you walk us through the template creation process?

**Georgemaine Lourens:** Sure. We start with a list of keywords that you handpick. Based on those, we start generating. This is Atlas—it's kind of our OS. We've gathered a lot about your company: contacts, research, products, services, and personas. All of these are artifacts that we feed to the LLM. Depending on the keyword, I either start with our assistant and go through use cases that would be usable for your personas. Based on those ideas and the complexity of the template—like if it's for a photographer or music artist, those are simple and photography-heavy—I would generate a spec. We make a new task, describe what we want to build, give it detail, add a category, primary keyword, and the tag that Lovable uses. Then we run a job and get a spec that we can feed to Lovable.

**Georgemaine Lourens:** The personas you have can be tailored more to what you've identified. By updating these artifacts, the outputs will be way better.

**Vikas Bhagat:** Can I easily access these inputs you're using?

**Georgemaine Lourens:** We can definitely do an export and share. It's an internal tool, so I'm not sure about shared access, but I can follow up by the next meeting.

**Megan Dickey:** We have all this information in Notion. Everything we have there, we've already moved into Atlas. I can share with you and make sure you have access to Notion and Airtable. I can point you to specific artifacts. You can check them out and leave comments. Then we can update it in Atlas.

**Vikas Bhagat:** That's perfect. That sounds fantastic.

---

**Megan Dickey:** So we're looking to automate integration doc generation. The main question from our side is: what is the source of truth for those docs? Are there internal docs at Lovable you're using as that source of truth? Should we rely on public API docs? How can we ensure our work is accurate?

**Vikas Bhagat:** There are three docs I'm trying to improve. There's the product requirements doc—the bare bones product source of truth. There's a PMM brief on top of that: messaging, audience, pain points, value props. And the third input is technical docs—actual product docs. The combination of those three feel like the right inputs for the integration content that needs to get spun up. I'll be honest: the quality of the PRDs and PMM briefs are pretty low right now, so I'm trying to get those to a higher bar so the input we provide is accurate, at the right altitude, and the right depth. Limitations are a great example. Have we documented that in one single place? No. So I'm trying to get to that point.

**Megan Dickey:** We would want to make sure we are very clear about limitations in any document. Does that resonate?

**Vikas Bhagat:** Yeah. Those three feel like the right inputs.

**Megan Dickey:** Nico, you would probably be tasked with building out that workflow. Does that sound manageable and doable?

**Nicolas Castellanos:** Yeah. I'd say about three days, and then it might take some time to calibrate and refine the outputs.

**Megan Dickey:** When do you think you might be able to get us those documents so we can start?

**Vikas Bhagat:** It depends on which integrations we want to focus on first. Let me do some homework on my side, but let's aim for end of this week for at least a handful. Then we can see if they're the right flavor and figure out what's working, what's not, and iterate.

**Megan Dickey:** Great. And can you also get us the most popular Lovable use cases?

**Vikas Bhagat:** Yeah. I think I can send you the full list, and we can pick and choose which ones make the most sense. I love cross-tagging with keyword search, too. What are people actually searching for? Then we can prioritize those.

**Megan Dickey:** Perfect. That sounds good. Sam, did you have anything else?

**Sam Vinden:** No, nothing from my side.

**Megan Dickey:** Okay. Thanks, Vikas.

**Vikas Bhagat:** Thank you. I'll send the doc over later today.

**Megan Dickey:** Perfect. Thanks, Georgemaine and Nico, for joining. I appreciate it. See you all next time.
