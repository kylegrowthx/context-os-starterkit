# Tamy / Nathalie - Parloa pipeline build

<metadata>
date: 2026-01-27
time: 22:03 UTC
duration: 21 minutes
organizer: nathalie@growthx.ai
participants:
  - name: Tamyres Ogasawara
    email: tamy@growthx.ai
    affiliation: GrowthX (Content Engineer)
  - name: Nathalie Schrans
    email: nathalie@growthx.ai
    affiliation: GrowthX (Delivery)
fathom_recording_id: 117633623
fathom_url: https://fathom.video/calls/547221309
share_url: https://fathom.video/share/zvtA7PMfMy1eqUoz-MgN6uy5Nc62Z5wi
source: fathom
enriched_on: 2026-02-28 00:15 UTC
</metadata>

---

## Summary

Tamy presents a standardized MVP (minimum viable agentic) pipeline as the baseline for Parloa content delivery and discusses how to adapt it to client-specific needs. The conversation covers pipeline composition, the role of the Assignment Direction as a control mechanism, and the decision-making framework for when to collaborate vs. independently update artifacts. Key takeaway: test the pipeline against published content, log specific examples of changes needed, and escalate only substantial changes (new steps, template rewrites, major instruction modifications) to Tamy via Linear ticket.

---

## Context

Nathalie is responsible for delivering the Parloa content pipeline this week so the team can begin calibration article work. The challenge is defining the right process for building pipelines under GrowthX's new review standards. Tamy (the content engineer) has created a reusable MVP pipeline with eight core steps (Research → Draft → Internal Links → Source → Proofread → Metadata → SEO Metadata → Fact-checking) designed to serve as a starting template. The conversation reveals an important architectural principle: the Assignment Direction repeats key instructions across all pipeline steps to ensure the AI model prioritizes them without overloading context windows, as opposed to calling full artifacts repeatedly. This efficiency-over-comprehensiveness approach underpins how GrowthX builds scalable content pipelines.

---

## Relevance

**For Delivery Teams (Nathalie's role)**
- How to structure the first pipeline test: compare against published content, document edits, decide minor vs. major changes
- When to self-fix vs. escalate: minor tweaks (tone, style) don't need Tamy; major changes (new steps, template rewrites, 2x instruction scaling) do
- The Assignment Direction as the primary control lever for output quality, not secondary detail

**For Content Engineers (Tamy's role)**
- Pipeline architecture: MVP baseline + optional customizations (image generation, CMS publishing) = faster client onboarding
- Risk management: substantial instruction changes need cross-check to prevent downstream conflicts or AI hallucination
- Feedback loop: specific before/after examples from the delivery team enable faster, more precise pipeline improvements than vague feedback

**For GrowthX Process**
- Clear ownership model: delivery team owns artifacts; content engineers are accountable for pipeline implementation and quality
- Efficiency principle: Assignment Direction reuse across steps avoids context overload and improves AI instruction priority
- Calibration phase scope: image generation and CMS publishing deferred until after initial content delivery

---

## Overview

- **Start with the MVP Pipeline:** Use the standard MVP pipeline (Research → Draft → Internal Links → Source → Proofread → Metadata → SEO Metadata → Fact-checking) as the baseline for Parloa.
- **Assignment Directions are Core:** The Assignment Direction is the central control, repeating key instructions across all steps to ensure Atlas prioritizes them and to avoid context window overload from calling full artifacts.
- **Involve Tamy for Major Changes:** File a Linear ticket for Tamy's review before adding new steps (e.g., image generation), making substantial instruction changes (e.g., doubling link count), or overhauling the Assignment Direction template.
- **Provide Specific Feedback:** When reporting issues, provide concrete examples or "before/after" rewrites. This gives Tamy objective data to train the AI, enabling faster, more precise fixes than vague feedback.

---

## Key Topics

### Parloa Pipeline Status

  - **Goal:** Build the Parloa content pipeline by this week to enable calibration article delivery.
  - **Blocker:** Uncertainty on the best process for building pipelines, especially with new review standards from Kirkland.

### Standard Pipeline & Customization

  - **MVP Pipeline:** Tamy has created a standard MVP agentic pipeline as the starting point.
      - Research → Draft → Internal Links → Source → Proofread → Metadata → SEO Metadata → Fact-checking
  - **Optional Customizations:** Add steps based on client needs and preferences.
      - **Image Generation:** AI-generated vs. manual sourcing.
      - **CMS Publishing:** Direct pipeline publishing vs. manual copy-pasting.

### Artifacts & Assignment Directions

  - **New Artifact:** Tamy created an "AI Business Editor" artifact for post-processing.
      - **Purpose:** Improve readability by flagging passive voice, AI phrasing, and other stylistic issues.
      - **Action:** Nathalie must customize the Brex-based guidelines for Parloa.
  - **Assignment Direction Strategy:** The Assignment Direction is the core control for the pipeline.
      - **Rationale:** It repeats high-priority instructions (e.g., voice, style) across all steps, ensuring Atlas prioritizes them without overloading the context window by calling full artifacts.
      - **Template:** The standard template covers Overview, Goal, Topic, Brand Integration, Voice & Style, and Key Differentiation.

### Collaboration & Feedback Process

  - **Ownership:** The delivery team is the primary owner of artifacts; content engineers are accountable for their pipeline implementation.
  - **When to Involve Tamy (Linear Ticket):**
      - Adding new steps (e.g., image generation).
      - Substantially changing the Assignment Direction template.
      - Making major instruction changes (e.g., doubling internal link count), as this requires new rules to prevent poor placement.
  - **Feedback Method:** Provide specific examples or "before/after" rewrites, not just vague descriptions.
      - **Why:** This gives Tamy objective data to train the AI, enabling faster and more precise fixes.

---

## Action Items

**Nathalie Schrans (GrowthX - Delivery)**
- Test Parloa pipeline against published content
- Log specific edits and changes needed (before/after examples preferred)
- File Linear ticket to Tamyres if major changes required (new steps, template rewrites, 2x instruction scaling)
- Apply minor improvements independently (tone, style, voice customizations)

---

## Transcript

**Nathalie Schrans:** I'm wondering what would be a good process for building these pipelines.

**Nathalie Schrans:** Because right now it's week two for Parloa and typically by Monday or Tuesday is when we would have a pipeline set up so that we can start working on the calibration article and see what problems there might be or what we need to customize to deliver the calibration this week.

**Nathalie Schrans:** In the past, I haven't been building pipelines and strategy sprints for long. I've just asked for examples from people—like, oh, this is the client I'm working on. Do you have similar clients that you've worked on and good pipelines?—and then just kind of copied what they did and customized from there.

**Nathalie Schrans:** But now that Kirkland and the rest of you are going to review all the pipelines that have been created, I understand that the best process would probably be different.

**Tamyres Ogasawara:** I created what I believe is the minimum viable agentic pipeline: research, draft, internal links, source, proofread, metadata, SEO metadata, and fact-checking. I believe this is where we can start to build on top.

**Tamyres Ogasawara:** Some clients want us to generate images with AI, some want to search for images, some want publishing as part of their pipeline, and some don't. All of these are things I would rely on the primary point of contact of the delivery team to tell me, because some clients like AI-generated images and some don't. Some are comfortable with sharing API information so we can publish directly from the pipeline, and some don't feel comfortable with that.

**Tamyres Ogasawara:** First things first: understand if there are any elements on this base pipeline that you think could be added to make it more helpful on a daily basis. Usually these are related to images. I didn't put anything related to images in the base pipeline.

**Nathalie Schrans:** Yeah, we haven't talked about that with them yet either.

**Tamyres Ogasawara:** So we have two elements for images: we can either generate those with AI or search for them, depending on the preference of the client.

**Nathalie Schrans:** And the publishing one is usually something we debate after. If we already have access to their CMS and they feel comfortable, we can add that to save time on copy-pasting information.

**Tamyres Ogasawara:** That's something you'll likely discuss with them in the future, but since we're still in the calibration phase, I don't think this is something we'll discuss this week. Those are the two customizations that usually come on top of the base pipeline.

**Tamyres Ogasawara:** The second thing we can check whenever we're doing a pipeline is: do we have all the artifacts we need? I've already created those for us. There's only one you don't have that the main pipelines usually have—the AI Business Editor.

**Tamyres Ogasawara:** I created this because it's a good resource for post-processing, specifically for the final proofread phase. It helps replace N-dashes, avoid passive voice and favor active voice, and flag other AI-phrasing issues that diminish readability. The guidelines are pretty generalistic—things like connection phrases, avoiding punch-after-punch introductions, and reducing AI phrasing. I created them for us, but you can review and let me know if you agree or disagree.

**Nathalie Schrans:** The guidelines are good, but this is from Brex, so I would need to customize it to Parloa. I just want to highlight that in case it comes up.

**Tamyres Ogasawara:** You're correct. It's an optional artifact, but I think it helps a lot with post-processing efficiency and getting more readable, natural text.

**Tamyres Ogasawara:** The other major point is to check if you agree with the assignment directions I put as a baseline. You can edit them—if you want shorter text or to target a specific persona, or if the integration rules don't make sense, let me know. This is one of the most important points: nailing down the assignment directions for end text quality. The heavy lifting of "I want you to sound like this, not like that" is done in the assignment direction. It's a core aspect we need to brainstorm to make sure it makes sense as is, or if you'd like me to change something.

**Tamyres Ogasawara:** The only thing we need to be careful with is not to overload the assignment direction with information. I've included sections that are the 80-20 rule. You can add one or two additional sections if you think they're necessary, but let's not go beyond that because it makes the AI more prone to hallucination or unclear instructions when trying to encompass too much at once. The template I've seen work on a lot of clients has: overview, goal, topic to cover, brand integration, voice and style, and key differentiation angles—these are usually the more delicate spots when writing. You can add one or two more if needed.

**Nathalie Schrans:** I have a question about this. I've noticed that a lot of pipelines have the default assignment direction include notes on writing a professional yet accessible tone, and things like voice and style guidelines and key differentiation angles. But shouldn't those already be covered thoroughly in the artifacts? Is there a reason they should be added to the assignment direction? From what I understand, the assignment direction is the thing that supersedes all the artifacts. So if it's in the assignment direction, Atlas will definitely do it. Is that why—to make sure Atlas doesn't forget?

**Tamyres Ogasawara:** Yeah, kind of. The way this works behind the scenes is that we can take the assignment direction and repeat it on multiple operations. For example, on proofreading, fact-checking, etc., we can put it over there as all-encompassing—this is the highest priority thing you need to check. Because if we add every artifact for each workflow—company research and so on—these are very long, so we might lose what the core highest priority aspects of the instructions are.

**Nathalie Schrans:** Okay, so there is a benefit. With other clients, what I focus on in the assignment direction is topics to cover—customized every article—and maybe the article structure like product alternatives, listicles, and templates for conclusions. And things like how we talk about their product and CTAs. So I'm not incorporating the voice and style guidelines like you've added here. But you're saying that's the best practice? Because you can't call on every artifact in every workflow without overloading the context window?

**Tamyres Ogasawara:** Yeah. We actually can call them, but it might not be the most efficient way.

**Nathalie Schrans:** "Can't" is a relative term, right? So moving forward, when I'm revising the default assignment direction, it's good to incorporate these because they're the highest priority tasks or things that Atlas needs to incorporate in all these steps. In proofreading or other post-processing, Atlas does call on the assignment direction.

**Tamyres Ogasawara:** Yeah.

**Nathalie Schrans:** I think the only thing I would have left to do is test this pipeline since I haven't done that yet. I'll make notes on anything I would need to change. Since they do have published content, I can compare against that. And then, would it be helpful if I fix minor things in the pipeline or artifacts myself, and only file a Linear ticket for major changes?

**Nathalie Schrans:** And then go from there?

**Tamyres Ogasawara:** Yes. But what do you consider minor?

**Nathalie Schrans:** In the assignment direction, if there's something about tone of voice, voice, or style guidelines, that can be changed.

**Tamyres Ogasawara:** Okay.

**Nathalie Schrans:** But what would be an example of something where I should collaborate with you instead of trying to fix it myself? I don't want to use Claude and have it work on the surface but create a bigger problem later.

**Tamyres Ogasawara:** The most obvious one is adding something new, like image generation. The second is completely changing the assignment direction template. If you disagree with everything and delete it to make a new one, that's when I should double-check, because new information might conflict with other steps and generate hallucinations. Changing one paragraph is fine, but completely changing the template needs review. The third is changing step instructions substantially. For example, internal links currently say six to eight. If you want to change that to 2x, I should flag that because we'd need additional instructions to prevent placing three links in the same paragraph or other formatting issues. These are the three main things: adding new steps, completely rewriting the assignment direction template, or substantially changing step instructions like 2x scaling or switching from H3s to H2s. That type of stuff is good to collaborate on so we can avoid conflicts with other steps.

**Nathalie Schrans:** Do we have an artifact conflict-checking process? Is that something I should manage as the delivery person, or should I incorporate you in that?

**Tamyres Ogasawara:** I asked Kirkland the same question. There's an overlap because you think about what's coming from the client and feedback to change, and I think about artifacts as resources for the pipeline. Kirkland said the delivery team is primarily responsible for artifacts. You can change them. But we as content engineers are accountable for keeping the main artifacts used in the pipeline and for checking when you make big changes—if you're unsure whether it will affect output or if a change does change the output, come to me and I can check what happened.

**Nathalie Schrans:** Especially if there are issues in the convergence report or in specific steps.

**Nathalie Schrans:** Those are all the questions I have. I'll test the pipeline and let you know if something needs to be changed that would need your help. I'm good on my end.

**Tamyres Ogasawara:** The main thing for me as a helpful resource: if you think the output isn't good on some points, show me the edit—even if it's just one calibration text. Instead of saying "readability is not good," show me an example of good readability. That's very helpful because I can tie it back to something objective and pass the example to the AI for training. This makes pipeline enhancements faster and more efficient.

**Nathalie Schrans:** That's a good note. When I post-process, I take notes on changes. If there's a concrete example, I try to incorporate it. I'll be as specific as possible, though I'm not anticipating many changes on this first test.

**Tamyres Ogasawara:** Even if you can't articulate what's off, if you can rewrite it the way you think sounds better, I can compare it as a before-and-after example.

**Nathalie Schrans:** Thank you so much, Tamy. I appreciate it.

**Tamyres Ogasawara:** I appreciate you helping us. This will make everyone's pipelines way better. I'll do my best to help you guys.

**Nathalie Schrans:** Thanks, Tamy.

**Tamyres Ogasawara:** Thank you. Cheers. Bye.
