# Kalil: Check-in 1

<metadata>
date: 2025-12-03
time: 19:04 UTC
duration: 69 minutes
organizer: Kalil Magtoto (GrowthX)
participants: Matthew Panzarino (GrowthX), Kalil Magtoto (GrowthX)
fathom_recording_id: 106062758
fathom_url: https://fathom.video/calls/493111138
share_url: https://fathom.video/share/zgFvyEzqKbFzd47n4Tvvx2dPYpiemgVB
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Matthew Panzarino and Kalil Magtoto reviewed Kalil's progress three weeks into their operator role managing content production for two healthcare clients: Interwell and Immubit. The core inefficiency is the current Atlas-to-Claude-rewrite workflow, which is unrepeatable and prevents learning feedback loops. The team agreed to pivot to direct editing of Atlas output in Google Docs, establish clear editorial checklists for both clients, simplify the Interwell pipeline prompt to produce more natural writing, and measure progress by timing article edits. Kalil will formalize Matthew's feedback into an Interwell editorial checklist, Nana will build an Immubit checklist, and the long-term strategy is to identify recurring manual edits and automate them as new post-processing steps.

---

## Context

Kalil Magtoto is a new operator at GrowthX, three weeks into their role managing content production for two healthcare clients: Interwell (medical writing) and Immubit (biotech/immunology). Matthew Panzarino oversees this work. Kalil took on Interwell fully over the past three weeks and just added Immubit yesterday. This check-in addresses a critical workflow problem: current editing takes 60-90 minutes per article when the target is 15-30 minutes (combined human and pipeline effort). The main bottlenecks are link validation (20-30 minutes per article) and incorporating qualitative editorial preferences from Matthew about tone, paragraph structure, and client fit. Additionally, Immubit lacks a defined editorial checklist, creating risk around quality standards and making the week's seven-article target a trial-and-error exercise. Matthew structured this conversation to reset the workflow approach, establish clarity around quality definitions, and help Kalil understand the reality of current performance so they can work toward realistic improvement.

---

## Relevance

- **To GrowthX Delivery:** The Atlas-to-Claude-rewrite workflow must be abandoned immediately. It is inefficient (redundant use of Claude when Atlas already uses Claude 4.5), prevents feedback loops that improve the pipeline, and produces irreproducible output. Kalil will edit Atlas output directly in Google Docs instead. This approach provides ground truth for identifying where pipeline prompts fail and allows Kalil to internalize client preferences while recording observations for future pipeline refinement.

- **To GrowthX Delivery:** Editorial checklists are the prerequisite for both efficient manual editing and effective automation. For Interwell, Kalil will formalize all of Matthew's feedback into a checklist. For Immubit, Nana is building a checklist for Kalil and Matthew to review before article generation. Without defined quality standards, Kalil cannot achieve efficiency targets and the pipeline cannot be improved systematically.

- **To GrowthX Delivery:** Kalil's current 60-90 minute editing time is expected for a Week 3 operator and will improve through practice and pipeline optimization. The 15-30 minute target is a combined efficiency bar (human work + pipeline output quality). Quantifying current time via self-timing on five articles will establish a realistic baseline and reveal whether bottlenecks are operator skill gaps or pipeline output quality issues.

- **To GrowthX Delivery:** Long-term efficiency strategy: identify recurring manual edits (CTA placement, link structure, tone adjustments), prototype solutions in Claude to prove they work, then automate via new post-processing steps in the Atlas pipeline. This systematic approach builds a repeatable, scalable system that reduces manual effort over time while improving output consistency.

---

## Overview

- **Workflow Reset:** The current process—using Atlas for research, then having Claude rewrite the entire article—is inefficient and unrepeatable. It must be replaced with a direct manual edit of Atlas's output.
- **Define "Good":** The primary blocker to efficiency is an undefined standard of quality. A specific editorial checklist is required for both Interwell and Immubit to provide a clear, objective target for the pipeline.
- **Pipeline Optimization:** The Interwell pipeline was updated to use a simpler, more effective prompt. The goal is to automate all repetitive edits by refining pipeline instructions and adding new post-processing steps.
- **Efficiency Target:** The 15–30 minute per-article editing target is a combined goal for human and pipeline performance. Kalil's current 60–90 minute time is expected for a new operator and will decrease with practice and pipeline improvements.

---

## Key Topics

### Current Workflow & Challenges

- **Interwell:** Editing takes 60–90 minutes per article.
  - **Primary Bottlenecks:**
    - **Linking:** 20–30 minutes spent manually checking link relevance.
    - **Qualitative Edits:** Incorporating subjective feedback from Matt (e.g., tone, paragraph structure).
  - **Current Process:** Using Atlas for research, then having Claude rewrite the entire article based on a "golden standard."
- **Immubit:** Generating 7 articles this week with no defined quality standards, which risks significant trial and error.

### The Problem: Inefficient & Unrepeatable Process

- The "Atlas → Claude Rewrite" workflow is fundamentally flawed.
  - **No Feedback Loop:** It prevents the Atlas pipeline from learning and improving, as its output is never directly refined.
  - **Inconsistent Results:** Claude's rewrites are not repeatable, making it impossible to establish a consistent standard of quality.
  - **Redundant Work:** The Atlas pipeline already uses Claude 4.5, so the post-processing step is a redundant and less controlled use of the same model.

### The Solution: A New, Repeatable Workflow

- **1. Define "Good" with an Editorial Checklist:**
  - **Interwell:** Kalil will formalize all feedback from Matt into a specific checklist.
  - **Immubit:** Nana will build a checklist for Kalil and Matt to review.
  - **Rationale:** A clear, objective standard is the prerequisite for both efficient manual editing and effective pipeline automation.
- **2. Adopt the Correct Workflow:**
  - **Process:** Run article in Atlas → Edit the output directly in Google Docs.
  - **Rationale:** This provides a clear feedback loop for improving the pipeline and allows Kalil to internalize client preferences.
- **3. Optimize the Interwell Pipeline:**
  - **Prompt Simplification:** The pipeline's prompt was updated to use a simpler, more effective structure.
    - **Old Prompt:** Overly prescriptive (e.g., "150 words," "mention X, Y, Z"), which forced the LLM to create dense, unreadable text.
    - **New Prompt:** Provides a high-level structure ("Define condition," "Mention symptoms") and lets the LLM fill in the details, resulting in more natural writing.
  - **Artifact Review:** The `company_context` artifact is too long (~8,500 words) and likely duplicated. Kalil will use Claude to trim it and check for conflicts between all artifacts (context, personas, guidelines).

### Long-Term Goal: Automate Repetitive Edits

- **Strategy:** Automate all repetitive edits by refining pipeline instructions and adding new post-processing steps.
- **Process:**
  1. **Manual Edit:** Identify a recurring edit (e.g., CTA placement).
  2. **Prototype in Claude:** Develop a reliable prompt for that specific task.
  3. **Automate in Pipeline:** Add a new post-processing workflow to the Atlas pipeline using the proven prompt.
- **Rationale:** This systematic approach builds a robust, repeatable system that reduces manual effort over time.

---

## Action Items

**Kalil Magtoto (GrowthX)**
- Time 5 Interwell article edits; log times
- Update Interwell pipeline: set programmatic default; remove 'maximum one'; move readability before validation
- Stop rewriting Atlas outputs in Claude; edit Atlas outputs directly
- Use colon-free titles in Atlas
- Create Interwell CTA artifact w/ 5–6 approved examples; then add CTA post-processing step
- Run 3–4 Interwell articles in new pipeline; compare outputs side-by-side
- Trim Interwell Company Context artifact; archive old versions
- Run Claude conflict check on Interwell artifacts (Company Context, Audience, Personas, Writing Guidelines)

**Nana (GrowthX)**
- Build an editorial checklist for Immubit; send to Kalil and Matthew for review

---

## Transcript

**Kalil Magtoto:** Hey there. How are you? Nice jacket.

**Matthew Panzarino:** Oh, thanks. How are you doing?

**Kalil Magtoto:** Doing good? My brain has expanded about 3x, which is nice. That's exactly what I was looking for.

**Matthew Panzarino:** Good.

**Kalil Magtoto:** I'm on week three, day three, which gives us maybe 12 days of effectively learning new stuff. I'm getting the hang of things. I don't know what good looks like. I've taken on one client now fully, with Matt still in my work. I'm slowly calibrating towards the ideal. I don't know if I'm slow or fast or right in the right spot, so I think it would be nice to get a gauge. Matt's saying that I'm doing good and picking things up fast, but I don't know if he's saying that to be nice or if it's genuinely good work. Would be cool to get a gauge on how well I'm doing. But otherwise, I have been really liking my experience so far.

**Matthew Panzarino:** Yeah, that sounds good. And you're working on Immubit at the moment?

**Kalil Magtoto:** I'm working on Interwell, which is the one I'm most up to speed with. Immubit I just took on as of yesterday. I'm generating seven new articles. I'm kind of worried about that one because the definition of good isn't quite defined. Hopefully we can ship out the seven this week without any issues, but it's going to be a lot of trial and error.

**Matthew Panzarino:** Yeah, got it. Definitions of good in terms of quality are largely based on editorial checklists, deliverables, and expectations. That's pretty straightforward if they're defined. If they're not, then I think your P1 will be to get those things defined or P0, really get those things defined so you have clear expectations of what the client wants and what we view as good for that client. If not defined, get it defined and be explicit. Hey, where's the editorial checklist? What do I have to deliver here? Where are the clear definitions of good? We can't afford any hand-waving. That's not fair and it's not good for your efficiency.

Outside of that, the idea of good in terms of production would be: the pipeline is producing something I can edit in under 30 minutes to deliver to the client. Whether it's there or not, I'd encourage you to literally time yourself. Run five articles, time yourself. It's not about you or your performance. It's just to get a gauge for how far off you are so you can make progress. When you reduce the time, that's an important metric. It's one I'll be talking about to everybody, but it's useful for you to start clocking yourself and seeing what's up. If you understand the reality of operating that pipeline for that client, the deliverables, and how long it takes you, you can get a realistic expectation for yourself and then work towards the idea of good.

**Kalil Magtoto:** Yeah. For Interwell, which I'm getting more comfortable with, it's anywhere from an hour to 90 minutes. That 30-minute bar that you set at the very beginning, I noted that down. I literally stuck it as a sticky on my laptop: 15 to 30 minutes, 15 to 30 minutes. Then as I keep going, man, that bar is really high. That's fast. I think I just need more practice. I need to find ways to make the pipeline work even better to get to that. I have an eight prompt flow that gets me just about there, and then Matt has some final edits that are more tasteful choices that I need to get up to speed with so I can have a manual edit and be creative with it.

**Matthew Panzarino:** Immubit doesn't have an editorial checklist. So I'm having Nana build you one and she'll send that over to you and Matt. Then you guys can agree with it or disagree with it, but we're building it off the operating manual. You should get some headway there. As far as the efficiency bar, remember that that's a combined efficiency bar. You're just unfamiliar with the tooling and getting used to it, and that's understandable. Some of that 90 minutes is just familiarizing yourself, understanding the quirks of the system and being more efficient and focusing. But it is a combined performance bar with you and the pipeline. The pipeline's performance is supposed to eat into some of that time as well. So don't feel like you're on the hook for all of it. It's a combined efficiency bar. The thing you are on the hook for is saying, hey, it's 90 minutes—how do I get it faster? I don't know how, right? And I think it might be ever so slightly too early for you to really understand whether it's you or the pipeline or the operation yet. However, it doesn't mean we can't start working there. So what is it that takes you 90 minutes? Just pick a piece of content from Interwell and let's talk through what took you 90 minutes to get it to a place where it satisfied all of the editorial checklist and was ready for the client.

**Kalil Magtoto:** Probably linking. Making sure that the links are good. That's 20 to 30 minutes just checking it out, making sure that Perplexity says the links are relevant. Then there are edits that Matt makes. Right now we're in a "hey, Matt, could you look over my work?" situation. Ideally Matt's not doing that, but right now that's where we're at. Then Matt will come in with recommendations and I'll clear through them. I think that's where it's slowest right now. We're making sure it fits these standards and then we get to that 90-minute mark. It's probably 60 to 90 minutes I've spent. I don't know how much time Matt has spent, so I have to factor that in too. It's like taste things: oh, let's break up this paragraph into chunks. Interwell is not going to like this phrasing. Let's try not to be too salesy. It's more qualitative. I have a document now literally called editorial preferences for Interwell. I make sure the language is warm, rows, bullet points are used appropriately but not too many, not too many m-dashes because it still throws them in there even if we instructed not to. These kinds of things are frustrating, but I have to understand why first. Then I could probably put it back into the pipeline and make fixes. I'm not at a point yet where I'm editing the actual pipeline. I'm editing prompts that I send off to Claude to get closer to the job done.

**Matthew Panzarino:** Okay. So it sounds to me like there's a couple of things going on here. One, you need a document provided to you by the previous operator of this account. Was that Matt?

**Kalil Magtoto:** I think so. No, Moses, but Moses left.

**Matthew Panzarino:** Yeah, but it's not just Moses though, right? It was like there was somebody who was his ME.

**Kalil Magtoto:** Was it Jessalyn or let me check. I don't know.

**Matthew Panzarino:** I think that would have been Matt. Find out. Maybe Matt.

**Kalil Magtoto:** Yeah, I think Matt's the one who's been working with this for the longest.

**Matthew Panzarino:** Okay. So you need to extract from Matt, either in conversation or him writing it down, all of the editorial preferences that he has for Interwell. Right? So that needs to be formalized as an editorial checklist. That's number one. Once you have that, then you know what good looks like. Once you know what good looks like, then you can edit to that standard. Right? And then you can time yourself and see how long it takes you. Once you have that time, you know where you are. And then you can make improvements. The second thing is that the process you're describing where you're taking the Atlas output and you're sending it to Claude for a full rewrite, that's the thing that I want to nip in the bud because fundamentally, the issue is that you're not editing the content—you're rewriting it. And once you rewrite it, you lose any signal on what the pipeline did right and what it did wrong.

**Kalil Magtoto:** Gotcha. Yeah.

**Matthew Panzarino:** So what I want you to do instead is take the Atlas output, drop it into Google Docs, and edit it directly. Just make the editorial edits that you need to make and then send that off to Matt. So the workflow is Atlas → Google Docs edit → send to Matt. Not Atlas → Claude rewrite → send to Matt. Because the second workflow, you're losing all of the signal. You're not getting any feedback on whether the pipeline is improving or not. And you're also not internalizing the patterns of what the client wants because you're just handing it off to Claude. But the best learning happens when you're doing the editing manually and you're thinking about why this is wrong and what this should be. And then you can take those learnings and feed them back into the pipeline prompts.

**Kalil Magtoto:** That makes sense.

**Matthew Panzarino:** Okay. So that's the workflow change. Now, the reason this matters is twofold. One, it gives you the best learning experience. Two, it means we can make the pipeline better based on real signals about what's wrong. Right? So when you're editing in Docs, you're also recording what you're doing so that you can then articulate that in instructions or updates or whatever. If you're just handing off the process to Claude, you're going to be in the wilderness, man. Like you'll never get to good because Claude may do some random thing tomorrow that's not the same as what it did today. And that's just not a path to good. It's not a path to higher efficiency.

**Kalil Magtoto:** Yeah, that makes sense. I understand that now.

**Matthew Panzarino:** Okay. So we're going to stop the Claude rewrite process and go straight to Docs. Now, the other thing is the pipeline itself. So when you look at the pipeline, we've updated the Interwell pipeline with a new prompt. The old prompt was overly prescriptive—like 150 words, mention X, Y, Z—which forced it to create dense, unreadable text. The new prompt is higher level. It says like, define condition, mention symptoms, and lets the LLM fill in the details. So it should produce more natural writing. The question is whether the artifact is still interfering. So the company_context artifact is like 8,500 words. That's way too long. And it's probably duplicating information from other artifacts. So what I want you to do is trim that down. And you should use Claude to check whether there are conflicts between the company context artifact, the audience artifact, the personas artifact, and the writing guidelines artifact. Because those things are supposed to be complementary, but if there are conflicts, then the pipeline's going to be confused.

**Kalil Magtoto:** Got it. So I need to trim the company context and check for conflicts between the artifacts. And then run the pipeline with the new prompt.

**Matthew Panzarino:** Exactly. Run a few articles through the new pipeline and see what the output looks like. Compare it side-by-side with the old prompt output. See if there's improvement. But don't rewrite it in Claude. Just edit it in Docs and see how long that takes. And then we can iterate from there.

**Kalil Magtoto:** Okay, makes sense.

**Matthew Panzarino:** The last thing I want to mention is the idea of getting to good is a long-term game. Right? So linking is one of your big bottlenecks. That's a 20 to 30-minute process. Now, when you're editing in Docs, you might think, okay, how do I get faster at checking links? Right? But if it's a fundamentally structural thing—like, this link is three words and I need all links to be two words—then your question shouldn't be, how do I make this more efficient for myself manually? It should be, how do I not have to do this ever again? And the answer is usually to refine the instruction set. Right? Refine the way that the pipeline is writing this article so that you don't have to do this again. But dropping it into Docs and editing it is table stakes for understanding what's going on with any of it. Like, why is this typo there? Why is this link three words when it should be two? I don't know. But understanding what's happening with each one of these things is so important because you need to ground truth for what's right. And not only that, it allows you to get your work done because you're just editing the article. Cool, I'm going to send this off. I think this is good now. We're good. But you're recording what you're doing and you're internalizing it so that you can then articulate that in instructions or updates or whatever. If you are just handing off the process to Claude, you're going to be in the wilderness, man. Like you'll never get to good because Claude may do some random thing tomorrow that's not the same as what it did today. Right? And like, that's just not a path to good. It's not a path to higher efficiency.

**Kalil Magtoto:** Yeah, I get it now. Stop rewriting in Claude and edit in Docs. Identify patterns and feed them back into the pipeline.

**Matthew Panzarino:** Exactly. I'm sorry for info dumping on you, but I just want to give you a reset on this because I don't think that process of taking your article, dropping it in Claude, saying, hey, here's a golden path, rewrite this entire article—I don't think that's going to be beneficial long-term. So I'm going to nip that in the bud.

**Kalil Magtoto:** Sounds good.

**Matthew Panzarino:** Okay, go forth. Let's see what happens with these. I would run a couple more in that new pipeline. See what happens. Step away, do your stuff. I know you've got to get a workout in for the week and move on. But then see what results are there and we can make some continuing tweaks.

**Kalil Magtoto:** Sounds good.

**Matthew Panzarino:** Yep. Reach out to Nana if you need any more assistance, too.

**Kalil Magtoto:** She's good at this stuff, too.

**Matthew Panzarino:** Sweet. Will do. Thanks, Kalil.

**Matthew Panzarino:** Thank you. Ciao, ciao. Bye.
