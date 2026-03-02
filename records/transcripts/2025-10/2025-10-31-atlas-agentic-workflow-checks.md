# Atlas Agentic Workflow checks

<metadata>
date: 2025-10-31
time: 14:58 UTC
duration: 61 minutes
organizer: Jenn Peters
participants: Marcel Santilli, Jenn Peters, Megan Dickey, Katya Luscomb, Bailey Seybolt, Ifeoluwa Adekoya, Nathan Navidzadeh, Matthew Panzarino, Kirkland Gee, Mariana Marins
fathom_recording_id: 98337242
fathom_url: https://fathom.video/calls/455829790
share_url: https://fathom.video/share/BJfxmAj-tewnPEVMP2zZ1izvYPMDU8HW
source: fathom
enriched_on: 2026-03-02 14:30 UTC
</metadata>

---

## Summary

Marcel Santilli led the GrowthX Atlas team through troubleshooting agentic pipeline problems—specifically, the HX pipeline inserting irrelevant platform-vs-point-solution arguments into articles like actuarial coding, and the Outreach pipeline producing choppy semicolon-heavy sentences. The core recommendation: decompose monolithic artifacts (300+ rules) into focused documents with post-processors for conditional logic. Marcel shared concrete examples from his financelibrary.com test project, demonstrating how isolating one variable per test run, using version history, and starting with high-level direction before adding specifics reduces context overload and improves agent behavior.

---

## Context

This was a full-team working session for the Atlas agentic workflows project—the effort to automate and improve content delivery using AI agents. The team is in the thick of implementation, hitting real friction with two client pipelines (HX and Outreach) that were migrated from the old scripted architecture to Claude-powered agentic agents. The broader context: GrowthX is running high-velocity experiments with agentic workflows as a core delivery capability, and this meeting was about shared troubleshooting and pattern-finding across multiple projects to unblock the Client Ops team. Marcel is actively learning alongside the team by testing these patterns on his own portfolio project (financelibrary.com), so this session doubled as both problem-solving and methodology discovery.

---

## Relevance

- **To GrowthX Delivery:** The decomposition pattern (splitting monolithic artifacts into core principles + specific rules + post-processors) is immediately applicable to all agentic pipelines. Start with concise high-level direction, add post-processors for conditional logic (if X, then Y), avoid context overload. The Diligent team's structured product_matrix approach is a model to replicate.

- **To Agentic Pipeline Troubleshooting:** When debugging, isolate one variable per test run using version history. This prevents cascading breaks and saves time by skipping research steps. The platform leverages version history natively—use it. For stylistic issues (e.g., semicolon overuse), check for conflicting rules in writing_guidelines; add explicit logic rather than removing rules.

- **To Fact-Checking & Accuracy:** The pre-agentic fact_checker is unreliable for specific data. Always rely on the modern researcher (Exa/Tavoli-based) and add_source_links post-processor. Recently updated to handle broken links better. Pre-populate the researcher with trusted sources or specific research questions.

- **To Client Expectation Management:** Frame agentic AI as enabling an "abundance mindset"—5–30 shots on goal per week instead of minor edits. This shifts conversations from stylistic polish to strategic leverage of the technology. Demonstrated with the Clerc white paper on DSPM as a quality-at-scale example.

---

## Overview

- **Simplify Artifacts:** Agentic pipelines struggle with the complexity of monolithic artifacts (\~300 rules). Decompose them into focused documents (e.g., `writing_guidelines`, `product_matrix`) and apply specific rules via post-processors.
- **Isolate Variables for Testing:** To avoid breaking changes, modify only one variable per test run. Use the platform's version history to revert inputs and re-run a single step, which saves time by skipping the research phase.
- **Use the Right Tools for Fact-Checking:** The pre-agentic `fact_checker` is unreliable for specific data. For accuracy, rely on the agentic `researcher` (now using Exa/Tavoli) and the `add source links` post-processor.
- **Manage Client Expectations:** Frame the AI's value as enabling an "abundance mindset" for content, shifting focus from minor stylistic edits to the strategic advantage of producing 5–30 high-quality articles per week.

---

## Key Topics

### Troubleshooting Agentic Pipelines

  - **Problem:** The HX pipeline is inserting platform-vs-point-solution arguments into irrelevant articles (e.g., actuary coding), likely caused by conflicting instructions in the `review product integration and positioning` step.
  - **Solution:** Decompose monolithic artifacts into focused documents.
      - **Rationale:** Agents struggle to prioritize and resolve conflicts between hundreds of rules in a single artifact.
      - **Method:**
          - **Core Principles:** Keep `writing_guidelines` concise.
          - **Specific Rules:** Isolate hard-and-fast rules in a separate artifact.
          - **Post-Processing:** Use post-processors for checklists and conditional logic (e.g., `if X mentioned, then do Y`).
      - **Example:** The Diligent team's `product_matrix` is effective because it's a structured artifact, not a post-processor. This allows the drafter to integrate product use cases organically, preventing awkward insertions.

### Diagnosing Stylistic Issues

  - **Problem:** The Outreach pipeline's agentic version produces choppy, semicolon-heavy sentences, a significant change from the standard pipeline.
  - **Diagnosis:** The issue is likely a conflict in the `writing_guidelines` artifact.
      - **Hypothesis:** A rule to "remove em dashes" may be causing the agent to over-index on semicolons without explicit instructions on how to handle compound sentences.
      - **Solution:** Add explicit logic for compound sentences (e.g., "connect with commas") to guide the agent's behavior.

### Fact-Checking & Hallucinations

  - **Problem:** The `fact_checker` agent is unreliable, often failing to verify facts from paywalled articles or making unhelpful, out-of-context edits.
  - **Diagnosis:** The `fact_checker` is a pre-agentic tool with a simpler methodology (basic Perplexity searches) than the modern `researcher` (Exa/Tavoli with deep research loops).
  - **Solution:** Rely on the `researcher` and the `add source links` post-processor for accuracy.
      - **Note:** The `researcher` was recently updated to better handle broken source links.
      - **Pro-Tip:** Pre-populate the `researcher` with a list of trusted sources or specific research questions to improve focus.

### Client Expectation Management

  - **Context:** The AI's ability to produce complex, high-quality content (e.g., the Clerc white paper on DSPM) is a major advantage.
  - **Framing:** Shift client focus from minor stylistic edits to the strategic value of an "abundance mindset."
      - **Rationale:** The AI enables 5–30 "shots on goal" per week, a massive increase over traditional methods.
      - **Goal:** Move conversations to higher-level strategy, helping clients leverage this new capability effectively.

### Pipeline Review Process

  - **Task:** Review pipelines in the "in review" stage to unblock the Client Ops team.
  - **Method:** Focus exclusively on editorial quality of the final output.
      - **Do:** Evaluate writing style, tone, and structure.
      - **Don't:** Analyze prompts or code.
  - **Rationale:** This provides clear, actionable feedback that the Client Ops team can translate into technical fixes.

---

## Action Items

**Jenn Peters**
- Review Outreach pipeline writing guidelines; add compound-sentence rules re: em dashes/semicolons
- Rerun Outreach pipeline w/ writing_guidelines_2; set max_iterations 2–3; share output w/ Marcel & Matthew

---

## Transcript
**Jenn Peters:** I don't celebrate it in Brazil, so for me, it's like, I'm kidding, just a day.

**Jenn Peters:** You should celebrate it on your own.

**Mariana Marins:** Just go out and do it in some costume.

**Mariana Marins:** It's a bit more celebrated, but it's more like for kids and teenagers.

**Jenn Peters:** Yeah, it is.

**Jenn Peters:** It is here too, except there's lots of like club nights or bar nights or, you know, costume events for adults too.

**Mariana Marins:** But not for me tonight.

**Mariana Marins:** And I thought it was very fitting to be on a Friday.

**Mariana Marins:** Like, in my mind, it should always be a Friday.

**Jenn Peters:** Totally.

**Jenn Peters:** Yeah.

**Jenn Peters:** Yeah.

**Jenn Peters:** When it falls in the middle of the week, it's like, you know, you don't want to go out and like, you know, be up late and then go to work the next morning, right?

**Jenn Peters:** Yeah, exactly.

**Mariana Marins:** Friday or like Saturday maybe are the best days, I guess.

**Jenn Peters:** Totally.

**Jenn Peters:** Yeah.

**Jenn Peters:** Yeah.

**Jenn Peters:** Always.

**Jenn Peters:** Well, you'll have to come over.

**Jenn Peters:** We're here to celebrate it.

**Katya Luscomb:** Hi, hi.

**Katya Luscomb:** How's it going?

**Jenn Peters:** Good.

**Jenn Peters:** How are you?

**Katya Luscomb:** Good.

**Katya Luscomb:** Friday morning.

**Jenn Peters:** Ready for...

**Katya Luscomb:** I can't believe it's Halloween today.

**Jenn Peters:** That's what I just said.

**Jenn Peters:** We're just talking about it.

**Jenn Peters:** Tomorrow's November.

**Jenn Peters:** I'm not ready.

**Jenn Peters:** What's happening?

**Katya Luscomb:** Me either.

**Katya Luscomb:** I need more time with this year.

**Jenn Peters:** Where are you, Katya?

**Katya Luscomb:** Where are you located?

**Katya Luscomb:** I'm out in Reno.

**Jenn Peters:** Oh, you're in Reno.

**Jenn Peters:** Okay, yeah.

**Jenn Peters:** So it's probably not feeling like cold.

**Jenn Peters:** Like, you know, you're not getting the weather indications.

**Katya Luscomb:** It's not snowy yet.

**Jenn Peters:** I grew up in Colorado, so I'm used to like...

**Katya Luscomb:** Oh, okay.

**Katya Luscomb:** We'll have snow at this point sometimes.

**Jenn Peters:** Right.

**Katya Luscomb:** This meeting is being recorded.

**Jenn Peters:** It's starting...

**Katya Luscomb:** yet.

**Jenn Peters:** Yeah.

**Katya Luscomb:** Chilly enough that it's weather weather and I'm happy.

**Jenn Peters:** Oh, yeah.

**Katya Luscomb:** What about you guys?

**Katya Luscomb:** Where are you based?

**Jenn Peters:** I'm in Vancouver, Canada, on the West West Coast.

**Katya Luscomb:** Geef, yeah, it's Colorado-y in some ways.

**Katya Luscomb:** you were in the U.S.

**Jenn Peters:** Me?

**Jenn Peters:** Oh, really?

**Jenn Peters:** Nope.

**Jenn Peters:** Nope.

**Jenn Peters:** I'm at the same time zone.

**Jenn Peters:** I am not.

**Jenn Peters:** Nope.

**Mariana Marins:** Oh, you weren't Canadian.

**Jenn Peters:** I am.

**Jenn Peters:** Yep.

**Jenn Peters:** There's not many of us.

**Jenn Peters:** That's all right.

**Marcel Santilli:** Good morning, everyone.

**Marcel Santilli:** How's it going?

**Katya Luscomb:** Good morning.

**Megan Dickey:** Hey, everyone.

**Megan Dickey:** Happy Halloween.

**Jenn Peters:** Happy Halloween for those who celebrate.

**Marcel Santilli:** We'll work on some scary workflows today.

**Jenn Peters:** Don't worry.

**Jenn Peters:** Everyone needs to put some kind of filter on there.

**Marcel Santilli:** Oh, yeah.

**Marcel Santilli:** I haven't done that in a while.

**Jenn Peters:** Neither have I.

**Jenn Peters:** I'm not even sure how you do it anymore.

**Marcel Santilli:** Hold on.

**Marcel Santilli:** Let's check this out.

**Marcel Santilli:** Like the avatars or no?

**Jenn Peters:** Yeah, yeah.

**Jenn Peters:** I think that's what it is.

**Marcel Santilli:** All right, everybody, put your filters on.

**Jenn Peters:** Oh, sweet.

**Jenn Peters:** Oh, my God.

**Megan Dickey:** All right.

**Marcel Santilli:** So we tried.

**Marcel Santilli:** If you don't have filters on, you're not allowed to be here.

**Marcel Santilli:** All right.

**Marcel Santilli:** We're going to do the whole session with filters on.

**Marcel Santilli:** So you go to video settings.

**Marcel Santilli:** And then there's, like, little filters.

**Megan Dickey:** Yeah, of course.

**Megan Dickey:** I'm a dog and Jen's a cat, which makes sense.

**Marcel Santilli:** Oh, you went, Jen went full-on avatar.

**Jenn Peters:** I don't know how to not.

**Marcel Santilli:** Now I'm going to take it off.

**Marcel Santilli:** Oh, my God.

**Jenn Peters:** Oh, my gosh.

**Marcel Santilli:** Avatars are too scary for me.

**Marcel Santilli:** They are.

**Jenn Peters:** I don't want it.

**Jenn Peters:** Oh, my gosh.

**Marcel Santilli:** Okay, I'm to work on this.

**Marcel Santilli:** That's a good way if you don't want to I do work in tech.

**Jenn Peters:** Works in tech, can't turn off the avatar.

**Nathan Navidzadeh:** You need a screenshot of everybody with their avatars on.

**Marcel Santilli:** Yeah, okay.

**Marcel Santilli:** All right, cool.

**Marcel Santilli:** Well, let's jump in.

**Marcel Santilli:** What are folks, anyone done anything since the last, for those joining, we're in Halloween spirit, so add your video filters on, you know, and have fun with that.

**Marcel Santilli:** But, yeah, anyone has done anything since last time that they want to share, because I don't want to talk the whole time, I still need more coffee, so, Bailey.

**Bailey Seybolt:** So, after the last call, Ife and I have sort of been tag-teaming, working through the HX pipeline, and trying to both diagnose kind of what's going on with the results, and also trying to figure out what step the breakdown is happening in.

**Bailey Seybolt:** And so I think one of the things we did is sort of identify, I think one of the issues is with the original pipeline before Agentec, we kept getting these weird results where it was telling it to build custom, even though the client offers like a platform.

**Bailey Seybolt:** And so the directions for the Agentec pipeline, like really tried to put a lot of guardrails around that about like making sure that we talk about platform solution and not point solutions.

**Bailey Seybolt:** And I think part of what's happening now is it's getting conflicting directions sometimes.

**Bailey Seybolt:** And it's like trying to jam this platform argument into like every one of the articles, even when it has absolutely like nothing to do.

**Bailey Seybolt:** Maybe it's about like actuary coding and then suddenly you get a section about like the platform versus point solution.

**Bailey Seybolt:** And I think one of the things that Ife did was kind of trace this to this, the review product integration and positioning step, which is.

**Bailey Seybolt:** Kind of where this is happening.

**Bailey Seybolt:** And so I did make a copy of the pipeline and I pulled the code out and was working with Claude to try and kind of update it.

**Bailey Seybolt:** But I'm wondering, like, if you have best practices for this kind of troubleshooting, because I find that sometimes when I'm updating the code, I'm like fixing one problem, but then I'm like breaking other things.

**Bailey Seybolt:** And so I'm just wondering, how do you do it when you kind of identify a specific problem, you think it's happening at a certain point?

**Bailey Seybolt:** Like, how do you kind of get the updates you want and check them in the code without kind of creating other problems?

**Bailey Seybolt:** Does that make sense?

**Marcel Santilli:** Yeah, and yeah, it does make sense.

**Marcel Santilli:** And let me see if also, like, let me just, it's being Kirkland, because I don't know if he got invited to this.

**Bailey Seybolt:** Any faith, there's any.

**Bailey Seybolt:** Anything else, feel free to jump into, because I kind of just tried to summarize what we talked about before this.

**Ifeoluwa Adekoya:** Yeah, I think that's like a pretty detailed summary.

**Bailey Seybolt:** Yeah, okay.

**Marcel Santilli:** Yeah, so the, what I like, or I started to do, I'm learning with you all, by the way, so I don't think I'm an expert in anything at this point anymore.

**Marcel Santilli:** But, but what has been helpful is kind of trying to hold as many things constant as possible.

**Marcel Santilli:** And, and so I had Kirkland help build a couple pipelines for me.

**Marcel Santilli:** I'm working on this thing.

**Marcel Santilli:** bought this to me called financelibrary.com.

**Marcel Santilli:** And then I've been trying to, like, build a site end-to-end, do a content strategy, and I'm doing and recording everything so that it becomes like a workshop in the community.

**Marcel Santilli:** But, but this is a good example.

**Marcel Santilli:** Let me just find.

**Marcel Santilli:** A couple ones that I think I ran in one of these, so let me just find which one I ran, a second version, just to show you the delta between the two.

**Marcel Santilli:** Let me see if it's this one.

**Marcel Santilli:** Okay, so this is a good example, all right, so this is version one.

**Marcel Santilli:** Okay, your series B, zoom in a little, four meetings in three weeks, your lawyer just told you blah, blah, blah, blah, and I'm like, this is way too  specific.

**Marcel Santilli:** Whoa, like, that is way too specific, you know.

**Marcel Santilli:** This part was a little better, but it's kind of being like, this is, it's describing a scenario too much, right, and I was like, why is it constantly, like, describing a scenario versus just saying what you want to say, you know, describing a made-up scenario kind of everywhere, and so I went, and...

**Marcel Santilli:** And this is where you can do, there's like two things we can do here.

**Marcel Santilli:** One is you can just go modify the artifact, right?

**Marcel Santilli:** So let me just go find that, give me a second.

**Marcel Santilli:** Go back here, and this is finance library.

**Marcel Santilli:** Okay, so then I modify a couple of things.

**Marcel Santilli:** And what you can do is look at the delta between them.

**Marcel Santilli:** You know, this was like version two versus version three.

**Marcel Santilli:** And I think, yeah, this is what I modify.

**Marcel Santilli:** I made it like essentially more generic.

**Marcel Santilli:** Like your building process that didn't exist just months ago, blah, blah, blah, blah.

**Marcel Santilli:** It, you know, it's like, it just made it a little bit more generic.

**Marcel Santilli:** But then most of the changes I made were

**Marcel Santilli:** We're in, and this is just like beginning of my journey.

**Marcel Santilli:** kind of ran out of time, right?

**Marcel Santilli:** Like was in the writing guidelines, to be honest.

**Marcel Santilli:** So if you look at this, you can kind of see the diff and it's kind of nice.

**Marcel Santilli:** You know, I actually didn't even know before I just tried this, that there was a diff.

**Marcel Santilli:** is way more convenient.

**Marcel Santilli:** But templates over theory is like, you can download to this.

**Marcel Santilli:** Like, okay, this is a little bit too much, you know, like, and then good.

**Marcel Santilli:** But this model crashes 60 days earlier than, I'm like, 60 days is very specific.

**Marcel Santilli:** 20 minutes is very specific.

**Marcel Santilli:** Like, you know, so I try to like modify it a little bit.

**Marcel Santilli:** It's not great.

**Marcel Santilli:** It was just literally like one shot because I was trying to move fast, you know, and this is not a client.

**Marcel Santilli:** This is just a made up publication kind of, you know.

**Marcel Santilli:** Like, anyway, so I fixed some of the examples a little bit.

**Marcel Santilli:** And I think, and so, so then if we go back here, this is version one.

**Marcel Santilli:** And then this is version two.

**Marcel Santilli:** And it did decently better.

**Marcel Santilli:** The second section, like, wasn't as well organized, but it hasn't validated the writing guidelines, and there's a bunch of other things you can do here, so this is only, like, the first step, right?

**Marcel Santilli:** And then it goes through, like, a bunch of things.

**Marcel Santilli:** So then what I wanted to, yeah, Nathan?

**Nathan Navidzadeh:** When you modified the artifact to change, like, the good examples, do you find that that's, do you know or have any experience if that's the better approach to, like, generalize the statement so it's not, like, a concrete number?

**Nathan Navidzadeh:** Or is it better to have, like, a catch-all statement at the top of that thing that says something like, remember, all of the good things, you know, all of the hard numbers and the good examples should not be used as they're just fictitious, like, they're not universal truths, use them as examples only.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** The best thing I've seen is, and Panzer, I think, mentioned this last time, was try to decompose it.

**Marcel Santilli:** And if you need multiple artifacts to do different things, you can.

**Marcel Santilli:** Like, just know that the research is really comprehensive and, like, just assume the research is going to take a while, but it'd be really good, right?

**Marcel Santilli:** Like, if you assume that, you know, then that makes a lot easier.

**Marcel Santilli:** Then, with a lot of this stuff, it's just mostly taking inputs and directions and, like, reworking it, right?

**Marcel Santilli:** And all it's doing is, like, an artifact is just a variable.

**Marcel Santilli:** That's all it is.

**Marcel Santilli:** Like, it's just a piece of text that gets inserted dynamically, right?

**Marcel Santilli:** Like, if you go into the YAML plan, it's just, like, a little variable.

**Marcel Santilli:** And so, technically, like, you can even, like, instrument these to just be entire fields, right?

**Marcel Santilli:** Like, or be, you know, multiple fields, right?

**Marcel Santilli:** Like, and so, but if you do that and you make a tweak in one execution, then you won't have the history of that execution or, like, the history.

**Marcel Santilli:** of the version of that input.

**Marcel Santilli:** Does that make sense?

**Marcel Santilli:** So what I did in this one, sorry, take a step back.

**Marcel Santilli:** Does that answer your question a little bit?

**Marcel Santilli:** It's mostly like decomposing it down and then kind of playing with it.

**Marcel Santilli:** It's honestly so non-deterministic that if you're flooding the system with like so much instruction and the company contacts and the personas and everywhere else and your assignment is like super specific and then like it could be like you're just flooding the context window so much that like it might not follow the direction so closely in this first shot and then you might need to have multiple like validation like steps if you will, right?

**Marcel Santilli:** That only focus on that aspect of it.

**Marcel Santilli:** And so I think the it at least stylistically what I've been finding even playing with Claude is that if you give it too much direction to begin with, it like just goes way off the rails and then to fix it is like more work.

**Marcel Santilli:** It's

**Marcel Santilli:** Almost, like, better to start super, like, high-level direction with not too many examples, let it get to a point, and then later on, if we need to add, like, a post-processing or do it through the, through this, you know, chat here or assistant, then it might be a little bit better, you know.

**Nathan Navidzadeh:** Yeah, that makes sense.

**Marcel Santilli:** So then, like, what I did was, came, Kirkland taught me this, so, is, if you, you can go to these versions here, okay, and, I don't know if Kirkland had a chance to join that book, but if, even if he doesn't, so, okay, like, and you can go back into the input, I had no idea, so, that's what I'm saying, like, I'm trying to learn as well, you know, and, and spend as much time as I can, and I just changed.

**Marcel Santilli:** So, I'm to, like, 1500 maximum, and then change things here, essentially, for this third run.

**Marcel Santilli:** So, this is the input.

**Marcel Santilli:** And then what you do is after you finish modifying this, I added an outline, because I just wanted to play with it, and I just hit save.

**Marcel Santilli:** Do not hit save and continue, otherwise it will run the research again.

**Marcel Santilli:** Right?

**Marcel Santilli:** And then, have other folks, did other people know that?

**Marcel Santilli:** Am the first one to find out?

**Marcel Santilli:** Or the last one to find out, I should say.

**Marcel Santilli:** So everybody knew that?

**Marcel Santilli:** Okay, it was new to me.

**Marcel Santilli:** And then, you just go to that step, you just hit play it from that.

**Marcel Santilli:** So you could technically even modify the input and play others, but then, you know, it's kind of like trickle down the fact.

**Marcel Santilli:** So that's what I did.

**Marcel Santilli:** And this is version 3.

**Marcel Santilli:** And I haven't read it, but let's just see.

**Marcel Santilli:** Still a little specific, but...

**Marcel Santilli:** It's still got to work on the B2 specific, but...

**Marcel Santilli:** Um, but if follow the, um, the outline pretty closely.

**Matthew Panzarino:** Yeah, generally I find if you see something in there that's hyper-specific, the first thing you should do is check your artifacts to see if that example lives there, because it will prioritize those.

**Matthew Panzarino:** So if, if that example exists or that number exists somewhere in the artifacts that you composed, maybe just delete it.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And, and so, like, if, if you can just do this for a week, right, of just, like, even if you spin up a whole nother instance, um, or create a V2 of your workspace, right, use the same, um, artifacts and start playing with artifacts and just have it, like, off to the side and, and just kind of, like, modify it, like, the amount of learning and the speed of learning will be a lot, a lot faster.

**Marcel Santilli:** I think, you know, and if you're trying something wildly different, you can always do like a V2 of that artifact, you know, or if you really, really want to like play around a bunch with it, then maybe even instrument the inputs as like hard-coded inputs here that way, instead of pulling from the artifacts, that way you can like kind of like play with different variables.

**Marcel Santilli:** But at least this, we can kind of play with this a little bit more.

**Marcel Santilli:** And if you're trying to play with it, like stylistically, you can always just like make this like way, way like shorter, if you will, right?

**Marcel Santilli:** And then like remove specific directions if you want and kind of play with it.

**Marcel Santilli:** Or at least that's how I've been starting to learn from the process, you know?

**Marcel Santilli:** So it's like decompose, like narrow it down to one variable, one thing that you're trying

**Marcel Santilli:** I learn and then kind of like play around with the artifacts, play around with different things, you know, and hopefully that that helps a little bit.

**Marcel Santilli:** Panzer, is this how you've been doing it?

**Marcel Santilli:** You've been doing this for a lot longer.

**Matthew Panzarino:** Yeah, yeah, pretty much.

**Matthew Panzarino:** I mean, I put this in the chat, but highly encourage people.

**Matthew Panzarino:** I mean, you can start from Daniel's auto-generated artifacts, like from scratch, which might actually lead you to a better conclusion than starting with your existing artifacts and trying to trim them down.

**Matthew Panzarino:** Either approach is viable.

**Matthew Panzarino:** I've done it both ways.

**Matthew Panzarino:** But the way that has worked for us is to just really understand that, like, the agentic pipelines do not need an enormous amount of hyper-specific detail because the researcher goes out and generates research questions and comes up with a pretty solid body of research and will come up with what it needs to write the article.

**Matthew Panzarino:** example, the agentic pipeline artifacts should start from, like, a base level of, like, the...

**Matthew Panzarino:** High, line, most important things your client cares about, and then work in the additional detail as needed.

**Matthew Panzarino:** I think it's good to do a reset there.

**Matthew Panzarino:** If you just take the existing artifacts and drop them into the agentic pipeline, you will find that your life will be a little hard because you'll end up with conflicts, logic loops.

**Matthew Panzarino:** It'll try to, like, juggle these dozens and dozens of instructions and execute them, and you'll end up with issues.

**Matthew Panzarino:** And the thing that you mentioned earlier, Marcel, about splitting the artifacts has been useful to us to think of the artifacts.

**Matthew Panzarino:** Like, you don't have to think of them as, like, well, all we have are writing guidelines, and I have to shove everything in there because the agentic pipelines have the post-processors available, and you can add multiple post-processors to any given pipeline.

**Matthew Panzarino:** So my advice is think, think, think, think before you do anything, but then break them up into the writing guidelines or the overarching principles.

**Matthew Panzarino:** A guide, the kind of writing you want to do for that client, and then you have perhaps a set of rules, which are hard and fast rules, and then perhaps a post processor that says, hey, I've got a checklist of things.

**Matthew Panzarino:** Could you go back and make sure that all of these things are good and split those into separate documents?

**Matthew Panzarino:** And this, the reason I say think, think, think is because you need to think logically about the order of operations.

**Matthew Panzarino:** The writing guidelines will be applied at the draft, and then any post processing will be applied later.

**Matthew Panzarino:** So make sure they're not in conflict, that they logically flow.

**Matthew Panzarino:** Just use your editorial mindset and say, hey, what would I do first?

**Matthew Panzarino:** Something that affects the entire article or reflows entire sections, I would do that first.

**Matthew Panzarino:** Before I went and said, hey, could you specifically check to make sure that this brand name has a TM attached to it in every instant that it appears?

**Matthew Panzarino:** Or some sort of conditional logic, like if X is mentioned, then do Y, that has to happen later, right?

**Matthew Panzarino:** So that's one thing that has worked well for us.

**Matthew Panzarino:** Is to not to try to cram 4,000 words into the writing guidelines and pray, and instead say, hey, let's just window this down to the guiding principles, and then split out really hyper-specific rules, or fact-checking, or post-processing to later on in the pipeline.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Bailey, did that help?

**Bailey Seybolt:** Yeah, that does help a lot.

**Bailey Seybolt:** think just thinking about how to break down the steps, and I think what's pulling from where.

**Bailey Seybolt:** So I think we have some ideas of what to try next.

**Bailey Seybolt:** We're getting there.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** All right.

**Marcel Santilli:** What if, has anyone done anything that then they felt was either, that was like either a breakthrough or significantly improved, or where they sent some output?

**Marcel Santilli:** has that they felt they felt felt they they

**Marcel Santilli:** Um, to a customer and they were pretty, pretty happy with it this week without requiring like hours and hours of crazy amount of editing.

**Marcel Santilli:** We have to be publishing stuff, so we have to have published something.

**Marcel Santilli:** Are folks publishing with old pipelines mostly?

**Marcel Santilli:** Or trying it off platform or like?

**Jenn Peters:** I think with the one that we're using, um, Timmy and I for one of the clients, um, we're finding it decent, um, but one thing that it seems to do differently is, um, than the regular workflow is like tone of voice is kind of off and like the way that it's kind of constructing sentences is a little bit off.

**Jenn Peters:** Like it kind of like...

**Jenn Peters:** over indexes on like...

**Jenn Peters:** like

**Jenn Peters:** Like, choppy language or, like, parsing things down into, like, a stream of, like, semicolon-type sentences and, like, we're not really figuring out why because it is the same.

**Jenn Peters:** Like, nothing would be wildly different there in terms of, like, the docs or, like, you know, anything like that.

**Jenn Peters:** So, um, the content itself, itself is okay.

**Jenn Peters:** mean, apart from, like, mad hallucination of, of stats and things like that.

**Jenn Peters:** But, like, we're, one thing we're kind of curious backtracker is the hallucination.

**Jenn Peters:** Yeah, yeah, yeah.

**Jenn Peters:** Um, but it's, like, the way the sentences are constructed is a bit different and a little bit, like, just kind of, like, yeah, like, choppy and just not, like, not kind of a tone.

**Matthew Panzarino:** And maybe, um, somebody or, or, or Panzer, maybe you have insight on that?

**Matthew Panzarino:** have a question for you on that, Jen.

**Jenn Peters:** Um, you say it has changed, this is a new thing, you mean the Agentec Pipeline is doing this?

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** Does it

**Matthew Panzarino:** In the pipeline, is that?

**Jenn Peters:** Yeah, it's different from the standard, yeah, how it was writing, style.

**Matthew Panzarino:** I would say a close read of your writing guidelines is probably the most vital thing to look at.

**Marcel Santilli:** Would you customize this?

**Marcel Santilli:** Sorry, just so I can look at it while you're talking.

**Jenn Peters:** It's outreach, and the writing guidelines don't do this for the regular pipeline.

**Jenn Peters:** It's not written in the guidelines to, you know.

**Matthew Panzarino:** Well, what I mean is, like, that's why I was saying that the agentic pipeline guidelines are just, they need to be treated as completely new, because just because the old pipeline didn't do this doesn't mean that the new pipelines won't do this.

**Matthew Panzarino:** Right.

**Matthew Panzarino:** have proper instruction, so.

**Jenn Peters:** So, like, how would you, if I was to look at the writing guidelines, like, how, like, what would I be looking, like, like, what would be in there that would kind of be a flag for kind of this.

**Matthew Panzarino:** I have to look at it, right, that's why I have to do a close read of it and say, like, what, what's the law.

**Matthew Panzarino:** Project that is here that's doing this or not there, by default, do you have stuff that says, like, remove em dashes as an example?

**Jenn Peters:** I'm not sure.

**Matthew Panzarino:** I wouldn't be surprised, but I'll have to take a look at that.

**Jenn Peters:** Is that something that the agent does?

**Matthew Panzarino:** With semicolons.

**Matthew Panzarino:** So, if you say, hey, remove em dashes, by default, it will just throw semicolons at you.

**Jenn Peters:** That's what it will be.

**Jenn Peters:** Yeah, within one sentence, that would make sense, but this is kind of, like, joining separate.

**Jenn Peters:** Anyways, I'll take a look, but, yeah, I'm wondering if there was something on that.

**Matthew Panzarino:** think maybe I thought you remove em dashes, you need logic that talks about compound sentences and how to handle them, and be very explicit.

**Matthew Panzarino:** Say, hey, if you remove em dashes from this, I'd like you to handle compound sentences in this way.

**Matthew Panzarino:** Connect them with commas, you know, et cetera.

**Jenn Peters:** So, yeah, I'll take a look at that.

**Jenn Peters:** Check it out.

**Jenn Peters:** Thanks.

**Marcel Santilli:** Yeah, and just to kind of give you, just kind of play with this, and then, but I don't want

**Marcel Santilli:** I want break too many things here, right?

**Marcel Santilli:** Okay, so I ran the content suite, if you will.

**Marcel Santilli:** And so this is the content suite version versus your version currently, right?

**Marcel Santilli:** So this is the content suite version.

**Marcel Santilli:** And you can see it's like pretty basic, right?

**Marcel Santilli:** And then this is the version you're currently using, which is hyper-specific.

**Marcel Santilli:** And before it made sense because it was just like an insane rule, right?

**Marcel Santilli:** But like there is no way an agent can hold this much context and be able to reason through how many, if you decompose this, there's probably about 300 rules here, right?

**Marcel Santilli:** So an agent would have to somehow decompose this down to three or four.

**Marcel Santilli:** 100 rules or goals to optimize for and then figure out which weight to put into each one of those and then reason through in which sequence and if any of them conflict even remotely and it's thinking then it's going to like try to make a trade-off decision or get you know stuck right so it becomes like not agents are not good for everything at all right like agents are good for for when you need to go through repetitively through something right for the most part because you need a supervisor agent and you know and then ideally like if you were trying to do this you were you know building like an army of sub agents for different things and then multiple layers of supervisor agents to figure out like you know how to trade it off and then the supervisor agents can hold more context than the sub agents and then it can check back in with the supervisor agent that holds most of the context and it's just giving enough context to the sub agent right like it's just to like

**Marcel Santilli:** Like the, the, it doesn't work for, for this level.

**Marcel Santilli:** right.

**Marcel Santilli:** Like city, right.

**Marcel Santilli:** So then what I would do is like, so if you go into the, your pipeline, which one have you been using?

**Jenn Peters:** It's the article agent one, but I was under the impression that wasn't the writing guidelines that it was, think Stevie turned that one off and let it go back to the other one.

**Jenn Peters:** But, but yeah, you can definitely confirm that.

**Marcel Santilli:** Um, meaning like you're manually putting the guidelines in here?

**Jenn Peters:** No, um, like originally there was, um, she had added, uh, there was two copies, like two sets of the same, of the guy, of the guidelines.

**Jenn Peters:** Um, and it wasn't, and the number two wasn't working.

**Jenn Peters:** So I think she, she switched it.

**Jenn Peters:** Yeah.

**Jenn Peters:** So maybe that's the original.

**Matthew Panzarino:** Yeah, it is using those.

**Matthew Panzarino:** It's using writing underscore guidelines.

**Jenn Peters:** It's not using.

**Matthew Panzarino:** Yeah, not number two.

**Matthew Panzarino:** Writing underscore guidelines one.

**Jenn Peters:** Yeah, I just created the number two.

**Marcel Santilli:** Yeah, but, like, if we go into here, and I just updated there, it might take a long time here to run, but I updated it.

**Matthew Panzarino:** Well, one of the reasons it's taking 20 minutes, by the way, is that the agent has to run through that entire contextual document several times to resolve conflicts, and it's inherently done.

**Matthew Panzarino:** So this will be faster.

**Jenn Peters:** Cool, yeah, we'll check it out.

**Marcel Santilli:** So hopefully, like, you see, like, what I did, did everybody see what I did there?

**Marcel Santilli:** I just went, found where it referenced that, changed it to replace all into, you know, underscore two, right?

**Marcel Santilli:** And now I can rerun just this step for this one, and you still have the other executions here as well, you know, so you can kind of reference back and forth a little bit more, you know.

**Jenn Peters:** Well, hopefully, hopefully that helps.

**Marcel Santilli:** Yeah, thank you,

**Marcel Santilli:** I think both of you have your hands up.

**Ademilade Shodipe-Dosunmu:** Okay.

**Ademilade Shodipe-Dosunmu:** I just wanted to talk about the Agencic pipeline for Diligent.

**Ademilade Shodipe-Dosunmu:** That's the refresher.

**Ademilade Shodipe-Dosunmu:** We don't have Agencic for NetNew yet.

**Ademilade Shodipe-Dosunmu:** But it's actually gotten better, especially now that we have like EXA in there for like research.

**Ademilade Shodipe-Dosunmu:** like the quality of like the external links and sources are really great.

**Ademilade Shodipe-Dosunmu:** And that was something that used to slow us down.

**Ademilade Shodipe-Dosunmu:** So now, like probably put it at about like 20 minutes to 30 saved on like working on a refresh.

**Ademilade Shodipe-Dosunmu:** Then we had this thing where we, because Diligent like has like a lot of products, like over 24 different products and solutions, which have like wide applicability across like different article clusters and all.

**Ademilade Shodipe-Dosunmu:** So we created this product matrix for them.

**Ademilade Shodipe-Dosunmu:** And like added that to our writing guidelines.

**Ademilade Shodipe-Dosunmu:** So that made the guidelines really long.

**Ademilade Shodipe-Dosunmu:** But even with like that much more context, give you a fresher experience.

**Ademilade Shodipe-Dosunmu:** Performing way better in terms of understanding product positioning and knowing what to reference or what type of article.

**Ademilade Shodipe-Dosunmu:** So it's actually saving a bit of time now, like around 20 to 30 minutes on your refresh.

**Ademilade Shodipe-Dosunmu:** So that's like, that's been a big win this week.

**Marcel Santilli:** That's really cool.

**Marcel Santilli:** And where is the matrix?

**Ademilade Shodipe-Dosunmu:** this the matrix?

**Ademilade Shodipe-Dosunmu:** Yes, it's inside our writing guidelines.

**Marcel Santilli:** Oh, cool.

**Ademilade Shodipe-Dosunmu:** Okay.

**Ademilade Shodipe-Dosunmu:** I think ideally it should be a post-processing step.

**Ademilade Shodipe-Dosunmu:** Yeah, yeah.

**Ademilade Shodipe-Dosunmu:** Yeah.

**Ademilade Shodipe-Dosunmu:** Yeah.

**Matthew Panzarino:** No, I would say don't put it as a post-processor.

**Matthew Panzarino:** That's actually ideal to have it defined as an artifact and then called by the drafter alongside writing guidelines, which that's a little bit of pipeline adjustment, but it can be done.

**Matthew Panzarino:** It's not incredibly complex, but it allows you to call it alongside the drafter.

**Matthew Panzarino:** The reason you don't want to post-process it is.

**Matthew Panzarino:** Because you need the article built around the use cases, right?

**Matthew Panzarino:** Like, you need to integrate into it so that it's not suddenly going, why is this product being mentioned randomly now?

**Matthew Panzarino:** You know, that's what a post-processor would do.

**Matthew Panzarino:** So, you can define it.

**Matthew Panzarino:** If this is working for you, don't change it.

**Matthew Panzarino:** Like, fine.

**Matthew Panzarino:** But if you want to, especially if the product matrix gets larger, or if you find that it's, like, only mentioning one or two of them because, like, picks the top couple and then forgets the rest or anything like that, think about defining it in a structured artifact that is separate, and then calling it during the agent or the drafting step.

**Ademilade Shodipe-Dosunmu:** Okay.

**Ademilade Shodipe-Dosunmu:** Okay.

**Ademilade Shodipe-Dosunmu:** That makes sense.

**Ademilade Shodipe-Dosunmu:** Okay.

**Ademilade Shodipe-Dosunmu:** Marcel, actually, it's in company context, no rights and guidelines.

**Marcel Santilli:** My bad.

**Ademilade Shodipe-Dosunmu:** Oh, perfect.

**Ademilade Shodipe-Dosunmu:** Okay, cool.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** This new thing that auto-organizes my tabs and it makes it slightly harder sometimes to, okay, company context.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** Yeah, so just to give you an idea of.

**Marcel Santilli:** What we did for Clerc, even though they ended up not proceeding in archive, that for anyone that's technical or very complex, it might be a good reference point for folks.

**Marcel Santilli:** So if you look at the, we went through and did a deep researcher step using Exa and extracted like all the different code snippets and almost like created this cheat sheet.

**Marcel Santilli:** Um, and it's pretty complex, um, and, and then, uh, products and services kind of similar to, to what you, you mentioned a little bit, but that high level, right?

**Marcel Santilli:** And, um, and then the proofreader, and then there's a bunch of other things here, um, and like how it works, you know, like just a high level of how like Clerc actually works.

**Marcel Santilli:** And, um, and, um, I believe the editorial, um, if we go.

**Marcel Santilli:** And two, some of the latest ones was pretty good, I want to say.

**Marcel Santilli:** And I mean, this is like a pretty difficult topic to get right, like DSPM, it's like, it's like related to essentially like how you manage your security posture, it's like pretty, pretty complex , you know, like, and, and so pretty, pretty freaking crazy.

**Marcel Santilli:** And, you know, um, let me find one that's a little bit more technical, maybe as an example.

**Marcel Santilli:** Um, yeah, there you go.

**Marcel Santilli:** This one might be interesting to see, um, how to implement passwordless authentication.

**Marcel Santilli:** I mean, this stuff, by the way, at this level would take like a technical writer, probably like two months of onboarding and learning about the company and the solutions and trying it out themselves.

**Marcel Santilli:** Right.

**Marcel Santilli:** And then probably.

**Marcel Santilli:** Like, multiple rounds of iterations to write.

**Marcel Santilli:** This is equivalent of, like, a white paper, essentially.

**Marcel Santilli:** Like, you know, like, this is the thing to set context with your customers when you're dealing with it is, like, what would the equivalent of, like, imagine you have either no AI or very little AI, right?

**Marcel Santilli:** Like, if you took, like, a technical person writing on this topic, like, how many steps would this person have to take and how much context and onboarding in order for them to deliver a really high-quality something, right?

**Marcel Santilli:** Like, Panzer, I was talking to Brian from Biologica several weeks back when I talked to him, and that was the thing that brought it up.

**Marcel Santilli:** was like, all right, like, because we had everything right, and he was, like, annoyed about some stylistic things.

**Marcel Santilli:** I'm like, dude, like, we got all these really hard things.

**Marcel Santilli:** Your medical review barely has to do anything.

**Marcel Santilli:** Like, that's insane, right?

**Marcel Santilli:** Like, and so normally it's like, how long would it take and how many people would have to be involved?

**Marcel Santilli:** But also if you just hire a person, like, a really good technical writer, like...

**Marcel Santilli:** They would still need edits.

**Marcel Santilli:** They would still need to learn about your product.

**Marcel Santilli:** They would still need to fact-check things, right?

**Marcel Santilli:** They would still need to verify your sources, like, and they're still probably charging $100 to $150 an hour if they're in the U.S., right?

**Marcel Santilli:** Like, at least that's what, you know, many companies like IBM and large enterprises I used to work for or used to pay for, like, really, you know, really strong, like, technical writers.

**Matthew Panzarino:** Like, you know, this is, I cannot stress enough how important what you just said is for client expectation setting, for talking to them, for helping them to understand how remarkable what we're doing for them is.

**Matthew Panzarino:** Because we, you're able to take a marketer or CMO or content person or whatever on their side and then flip the switch in their brain to help them think in an abundance mindset when it comes to content.

**Matthew Panzarino:** Because normally, it's so expensive and so time-consuming to create this kind of content that you're only able to choose a handful of shots on goal any given month or

**Matthew Panzarino:** And we're able to provide them with 5 to 10 to 30 shots on goal per week, which is insane.

**Matthew Panzarino:** It's like an incredible paradigm shift in how they can attack their market, how they can talk to customers on a more niche level, all of that stuff.

**Matthew Panzarino:** But it also means they need to flip that abundance mindset switch when it comes to changing this comma to that comma.

**Matthew Panzarino:** It's like, chill out, you know, like you're getting dozens of shots on goal here and able to attack this in so many new ways.

**Matthew Panzarino:** And that also means that when you have conversations with them about strategy, they need to think abundance mindset strategy and not get too, like, obsessed with a particular cluster or another cluster or whatever.

**Matthew Panzarino:** But it also allows you to start moving the conversation to the bigger picture, which takes their eyes off of whether this sentence should be below this sentence.

**Matthew Panzarino:** And it just allows them to, like, move back from it a little bit and, like, you know, go from the pointillism to the big picture.

**Matthew Panzarino:** And I think that's that's an important thing long term for people.

**Matthew Panzarino:** Managing accounts and managing their clients to, like, to talk about when it comes to content quality.

**Matthew Panzarino:** Just wanted to fill that in.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And that really, really helps.

**Marcel Santilli:** And, like, just to kind of give folks a little bit of going back to what we were saying before, Jen, on your stuff and outreach.

**Marcel Santilli:** Like, this is the execution.

**Marcel Santilli:** It's almost done running.

**Marcel Santilli:** And it still went through.

**Marcel Santilli:** But, by the way, like, when you're testing, if you want, just, like, have it go through only two cycles.

**Marcel Santilli:** I think this had a maximum of, let me just find it here.

**Matthew Panzarino:** Let me just see the eight plus three, I think.

**Marcel Santilli:** But sometimes we give it max iterations ten.

**Marcel Santilli:** Like, and so, like, that's too much, right?

**Marcel Santilli:** Like, so, like, if you set the max iterations to, like, three, three, it will for sure go faster, or even two.

**Marcel Santilli:** But it's going to try to go through, right?

**Marcel Santilli:** And so a great way to learn is, like, if you look, like, the very first shot, like, groundness was, like, 0.98, you know, and it found a bunch of potential issues.

**Marcel Santilli:** Like, that's a lot it's trying to run through, which is just, like, as they grounded on the research.

**Marcel Santilli:** And then writing guidelines was 0.5.

**Marcel Santilli:** And then direction acceptance was, like, 0.65.

**Marcel Santilli:** Right?

**Marcel Santilli:** And so what it's doing, then, on the second one, it, like, decayed the groundness a little bit, you know, in order to improve the writing guideline and, like, the direction acceptance.

**Marcel Santilli:** Okay, so it kind of, like, got everybody even, you know?

**Marcel Santilli:** And then, like, the, and then here, this third try, it got, you know, here it was running a fifth time, a fourth time now.

**Marcel Santilli:** So that's why it's taking so long, right?

**Marcel Santilli:** Okay, like, now 0.95.

**Marcel Santilli:** Okay.

**Marcel Santilli:** And then, writing guidelines, .85, and then, let's see, I mean, it should have stopped here.

**Marcel Santilli:** I don't know why it's trying to go any higher than this.

**Jenn Peters:** It's trying too hard.

**Jenn Peters:** Good enough, like, keep going.

**Marcel Santilli:** Yeah, it's trying too hard, right?

**Marcel Santilli:** But I think, like, go into the spectrum, right?

**Marcel Santilli:** it's super intense.

**Marcel Santilli:** Like, instead of just like, ah, it didn't work, like, you should be able to kind of see what it's doing, the logic behind it.

**Marcel Santilli:** can see the inputs, you can see, like, what it's trying to improve.

**Marcel Santilli:** This is insanely powerful, right? We're just overwhelming it by saying: do a hundred things and follow a thousand rules. It's like, I don't know what to do—and we wouldn't either.

**Marcel Santilli:** And it's just that it's dealing with so much research and so much context.

**Marcel Santilli:** And ultimately, like, when we first implemented this, I think Daniel had, like, five different evals.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** But this is the level of feedback that will be really helpful, when you get down to this nitty-gritty piece, and you say, hey, let me get it down to one or two rounds of evals only, or three rounds of evals only, and then maybe be more specific or narrow your research down to be more strict versus exploratory.

**Marcel Santilli:** So, for instance, if you go back here to this, like, the way this ran is EXA, and then the research mode was not set, right?

**Marcel Santilli:** Like, it is, let's see, exploratory, you know, and so a lot of these things, they're going to be super exploratory, and they're going to go and try a lot of different things, right?

**Marcel Santilli:** Like, so, and then when you can see, also, it's, like, it is something, like, I haven't had time to do, but I want to play around with this concept.

**Marcel Santilli:** Is the fact that, like, if you start to work with a customer and you learn their space, like, I can come up with a short list of who is legit and who's not in a space, like, very quickly, right?

**Marcel Santilli:** And so, like, and even how we do some of our research is kind of interesting, or kind of, was playing around with this, but it was, oh, fine.

**Marcel Santilli:** Okay, I think it was this one.

**Marcel Santilli:** Yeah, like, okay, so here's an example, right?

**Marcel Santilli:** Like, I'm, and I teach this in a lot of the workshops, so, like, folks haven't listened to the ones that we have in our community.

**Marcel Santilli:** Just sign up for our community, you know, like, growth.com, and, like, there's a lot of stuff there, too, you know, but this one is just doing research on a role, right, like a persona, and this is what I'm doing for financelibrary.com, and then it's kind of defining their...

**Marcel Santilli:** Their job description and, you know, kind of the context for them.

**Marcel Santilli:** And one, this gives you, like, ton, like, whatever persona the company you're working with, right, a customer is targeting, you should be able to create literally an obscene amount of, like, topics.

**Marcel Santilli:** Because, like, every persona just has so much, like, you start digging into, like, all the different topics they care about, right?

**Marcel Santilli:** Like, their job description, the skills required to do their jobs well, the work products they need to do, like, the terminology they need to understand, the regulations they need to stay on top of.

**Marcel Santilli:** Like, that right there just gave you, like, three years worth of content, you know, on just these three things for one persona, right?

**Marcel Santilli:** And then you adapt that to finance manager for startups, finance manager for an e-commerce, a bootstrap company, finance manager for, you know, whatever, right?

**Marcel Santilli:** A finance manager for a startup in Europe.

**Marcel Santilli:** Okay, that's a whole other thing, right?

**Marcel Santilli:** Like, when you start doing that, now all of a sudden, like, there's an infinite number.

**Marcel Santilli:** But back to the point I was making was that as I try to develop voices, like, this is amazing research, but for the kinds of sources you want to actually save as well, right?

**Marcel Santilli:** So, for instance, like, leading authors and thought leaders, okay, like, and then you can create kind of like a database of, like, all of these, and you can use perplexity.

**Marcel Santilli:** Manus is pretty good as well, but perplexity has, like, agentics as well, where you can essentially say, like, create a database of the top 100 authors and sources for this audience, and in this database include who they are, the URL, and then some sample topics that they cover.

**Marcel Santilli:** Put it all on a table for me, like, you can do something like this, and I almost guarantee you it's going to, like, give you, like, a really great starting point.

**Marcel Santilli:** And it's going to go to work for, like, 20 minutes or whatever, right?

**Marcel Santilli:** And it's going to return, literally, like, a database for you to start with, right?

**Marcel Santilli:** And then, so you can do this, like, Claude and ChatGPT are pretty slow in doing things like this.

**Marcel Santilli:** And so I find, like, perplexity is the fast and decent.

**Marcel Santilli:** And then Manus is, like, and if we need to create, like, a company account, Panzer4, for Manus, we can.

**Marcel Santilli:** But, like, Panzer, I mean, sorry, Manus is really good at that.

**Marcel Santilli:** Like, just to give people an idea, like, my wife's going through some legal stuff with her ex-employer, and I had to look at 40,000 text messages.

**Marcel Santilli:** And I created an entire app that sorted through 40,000 text messages and then classified all of them and then created a score of relevance to the case and then bucketed all of them into different parts of the claims.

**Marcel Santilli:** Like, you know what mean?

**Marcel Santilli:** Like, that's the kind of thing.

**Marcel Santilli:** And it's possible, right?

**Marcel Santilli:** Like, but, so, so you can see, like, it's already finding, like, good things.

**Marcel Santilli:** Like, these are legit sources, you know, A16Z, like, VCs, and you can, like, then classify all your sources, right?

**Marcel Santilli:** And now, one, that's amazing research.

**Marcel Santilli:** Two, you should go read some of the stuff for your customer because, like, you should go invest those upfront hours and you should figure out, like, what voices resonate and why do they resonate, you know?

**Marcel Santilli:** And three, like, that can be amazing calibration because now you can take, like, I really like how this one is done.

**Marcel Santilli:** And you can see, like, after you read, it's, like, wine, right?

**Marcel Santilli:** It's, like, if you taste, like, a bunch of really amazing wine and then you taste, like, a  one, you're going to immediately tell.

**Marcel Santilli:** But if you only taste, like, mediocre wine, it's just, like, you can't really tell a lot of them from a park.

**Marcel Santilli:** So you kind of have to taste a lot of good and bad.

**Marcel Santilli:** And then, like, over time, you build a muscle memory of, like, what great should look like for this space.

**Marcel Santilli:** Right?

**Marcel Santilli:** But then, like, you can start to validate, like, like,

**Marcel Santilli:** Hey, I really like this, but, like, these are very two different approaches.

**Marcel Santilli:** Which one resonates with you?

**Marcel Santilli:** And you show them, like, one single, like, thing, you know?

**Marcel Santilli:** And so if you're having stylistic issues with any customer that you're working with, like, go look at what we did for, I set up a new computer, so I've to log into a bunch of things.

**Marcel Santilli:** But we'll go look at what we did for, like, Engine, and Ada probably has, and the team have, like, a bunch more, lovely, okay, I'm not able log in.

**Marcel Santilli:** But in Engine, there's a calibration guide that we did where it created, essentially, a table, and it took one of their existing pieces of content, and it rewrote, like, essentially paragraph by paragraph what the, like, the new style guide would look like, right, and kind of defined their voices a lot better.

**Marcel Santilli:** So I don't know if anyone can share their screen—I'm logged out of Notion.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** Computer, but, and just pull up Engine and kind of show folks, because this is what you need to do in order to get down to the essence, and then when that essence is clear in your mind, and you can, like, articulate the essence of what it needs to sound like, you'll do a much better job in describing it in the fewest words possible, what it needs to, like, do as far as the writing guidelines for your pipelines, you know, if that makes sense.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Well, we have Kirkland and Marcus here, but Kirkland, you don't have a costume, so you get a, in order to contribute, you need to have a costume.

**Kirkland Gee:** Well, I guess I just won't say anything, then.

**Marcel Santilli:** That's fine.

**Marcel Santilli:** No, no.

**Marcel Santilli:** I'm kidding.

**Marcel Santilli:** I'm kidding.

**Kirkland Gee:** I gotta figure out how to do this.

**Marcel Santilli:** And add a filter, but, all right, folks have questions for Kirkland or Marcus on anything that they're stuck on?

**Nathan Navidzadeh:** I had noticed something that I wanted to bring up when you mentioned, think Jen was talking about the researcher and the hallucinations, and then you were like, how come the fact checker didn't pick them up?

**Nathan Navidzadeh:** Like, what happened?

**Nathan Navidzadeh:** I was like, oh, yeah.

**Nathan Navidzadeh:** So what I realized was when the hallucinations would, and I just wanted to point this out, and I'm sure you guys probably, I hope you guys already know about this, when the hallucinations would show up, the fact checker would find them sometimes, most of the time, let's say.

**Nathan Navidzadeh:** But the adjustments that it would make were not helpful.

**Nathan Navidzadeh:** So the suggested change that it would make would not be helpful.

**Nathan Navidzadeh:** So it would find the, it would say, this is not correct, and it would reword it kind of nicely, so that it's not making a hard claim, it's more of a general statement, and, you know, removes any kind of link that was hallucinated.

**Nathan Navidzadeh:** But then it would say something like, so let's say the hallucinated fact came from a Harvard Business Review article.

**Nathan Navidzadeh:** It would say, but Harvard Business Review did not say that this is actually true.

**Nathan Navidzadeh:** Like, you know, it would like, and this is out of context for the, in the article itself, because you're reading the article and you're like, why is it talking about Harvard Business Review not saying that this thing cost $12 million?

**Nathan Navidzadeh:** So that sort of thing was happening.

**Kirkland Gee:** So it's important to keep in mind a couple of things.

**Kirkland Gee:** Is one, the fact checker has been touched, but like that was a pre-agentic workflow design in the sense that it's not as good as the agent, period.

**Kirkland Gee:** Like the researcher agent and the drafting agent are going to be more, other than the issues that Daniel's trying to solve, should be more factually accurate than the fact checker.

**Kirkland Gee:** Because the fact checker is just using perplexity searches and not even perplexity deep research.

**Kirkland Gee:** So that's really all that's happening there.

**Kirkland Gee:** The researcher is using Exa or Tavoli, better search engines, blah, blah, blah, with HN.

**Kirkland Gee:** Loops, all these kinds of things.

**Kirkland Gee:** The problem we were running into is a lot of the sources in those platforms are 404-ing or redirected, and, like, it doesn't tell us that.

**Kirkland Gee:** And so that's kind of an issue.

**Kirkland Gee:** Daniel, literally, night before last, I think, put a whole, like, did a whole round of revisions on the researcher to try and prevent that from happening in the future.

**Kirkland Gee:** But it's not uncommon, it makes sense to me that the fact checker and the research are not, like, playing well together, because they're two completely different methodologies, and really trying to solve two different problems, right?

**Nathan Navidzadeh:** Yeah, that makes sense.

**Kirkland Gee:** hopefully, the research should be a lot better now, but anything that's happening before yesterday, like, I wouldn't, there were some bugs that Daniel tried to resolve.

**Nathan Navidzadeh:** Okay, sounds good.

**Nathan Navidzadeh:** And the other angle of the fact checker not playing well with the researcher is, I just noticed, obviously, is that the, if the article is behind a paywall, then it doesn't know what to do.

**Nathan Navidzadeh:** So it basically gives you an evaluation of unknown or something, and then just returns a null value, so it doesn't make any changes.

**Nathan Navidzadeh:** And so there could, again, be a hallucination that's made, and it would go through because of that.

**Kirkland Gee:** Yeah, the fact checker is good at checking basic facts of, like, is this code snippet, is this kind of correct?

**Kirkland Gee:** Or did the iPhone 17 come out this year?

**Kirkland Gee:** Like, recency stuff it can usually fix.

**Kirkland Gee:** But if you're talking about very specific data points from some research document, like, that's going to be a tough thing for it to catch.

**Kirkland Gee:** In theory, the research agent and the drafting agent.

**Kirkland Gee:** And then we also do a post-processing step called add source links in most pipelines that looks at the article and looks at the research and makes sure every claim is cited.

**Kirkland Gee:** That's essentially what should be your fact checker for the time being.

**Kirkland Gee:** I know some people are still using the fact checker.

**Kirkland Gee:** If you're having sort of, I think...

**Kirkland Gee:** And Panzer said this earlier.

**Kirkland Gee:** If it works, keep doing it.

**Kirkland Gee:** Like, a lot of this stuff is very black boxy, and we think something's going to work better, and then it turns out some other thing does.

**Kirkland Gee:** It's like, if something works, please do not change it based on some feedback that I said.

**Kirkland Gee:** Oh, God, what is happening?

**Kirkland Gee:** But, in general, I would try to, like, lean on that, if that makes any sense.

**Nathan Navidzadeh:** I also don't know what's going on now.

**Marcel Santilli:** I was trying to take a screenshot, and I was like, oh, this looks cool.

**Marcel Santilli:** All right, everybody turn on their cameras.

**Marcel Santilli:** Happy Halloween.

**Kirkland Gee:** Wait, wait, wait, wait, no, no, no, no.

**Marcel Santilli:** Yeah, there we go.

**Marcel Santilli:** Okay.

**Marcel Santilli:** All right.

**Marcel Santilli:** What if I was a panda instead?

**Marcel Santilli:** Yeah, I like that.

**Marcel Santilli:** Let me take all these out of here.

**Marcel Santilli:** All right.

**Marcel Santilli:** Smile if you're not in an inventory.

**Marcel Santilli:** Okay.

**Marcel Santilli:** We Bye

**Marcel Santilli:** All right.

**Marcel Santilli:** There you go.

**Marcel Santilli:** All right.

**Marcel Santilli:** Back to business.

**Marcel Santilli:** Sorry.

**Marcel Santilli:** I'm a squirrel over here.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Nathan, like in some, which customer was having like a lot of hallucinations on the stats or whatever?

**Nathan Navidzadeh:** It was data grid.

**Nathan Navidzadeh:** And I was just running experimental stuff on an agent pipeline.

**Nathan Navidzadeh:** Yeah.

**Marcel Santilli:** One thing I also haven't done.

**Marcel Santilli:** So, so there's a few things that like, one is, um, we can, like the researchers is trying to come up with like a plan and do a bunch of stuff.

**Marcel Santilli:** Right.

**Marcel Santilli:** And, um, but one thing I haven't tried, would be kind of interesting if, if like the kind of content we're all generating has a lot of stats and things, you might want to give it instructions.

**Marcel Santilli:** Uh, I haven't tried it.

**Marcel Santilli:** So, so if you want to try and like tell, tell me how it works.

**Marcel Santilli:** Um, and like, almost like save, like extract from your research.

**Marcel Santilli:** Research and return all the stats in a table or something along with like the URL and the source or something, right, like in the context of that.

**Marcel Santilli:** And I bet you like it would be pretty decent at that and then say, hey, drafter only use facts or stats that are in this table or something, you know, like I bet you there's like ways to do something like that, you know, that could be kind of interesting if you really want the stats, you know.

**Marcel Santilli:** If not, like can always try to say, don't use any stats on anything and then do it as a post-processing and say, okay, now look back at the research and see, are there any places where you could insert like a stat to, to like boost like my, not claim, but like, you know, like what I'm.

**Nathan Navidzadeh:** Authority in the space, yeah.

**Marcel Santilli:** Yeah, that could be, that could be kind of fun and interesting, you know.

**Matthew Panzarino:** Yeah, and remember too, like the research, when you research runs, you can always go look at the research.

**Matthew Panzarino:** look

**Matthew Panzarino:** At the bottom, the researcher will provide you with a complete bibliography.

**Matthew Panzarino:** This can sometimes be useful if a client is asking you for a list of sources that you're using for it.

**Matthew Panzarino:** can easily provide it to them.

**Matthew Panzarino:** It can also be a quick way to scan it and be like, hey, I need to add some instructions to the article directions under like researcher instructions that says, you know what?

**Matthew Panzarino:** I want you to use these sources for me because it will.

**Matthew Panzarino:** It'll look at those and it'll say, okay, I'm going to generate these questions and I'm going to utilize these primary sources.

**Matthew Panzarino:** That does work.

**Matthew Panzarino:** You can specify questions, too, in the article directions or assignment directions that you would like the researcher to research.

**Matthew Panzarino:** It will still think of its own, but you can tell it, I would really like you to research these questions.

**Matthew Panzarino:** So if you really need some body of knowledge in the article, for sure, for sure, go ask it to look up that knowledge for you, just as you would a human researcher tackling the topic.

**Marcel Santilli:** All right.

**Marcel Santilli:** Well, any final things before we wrap up?

**Andrea (Client Ops):** I wanted to ask if Kirkland or Marcus could give us an outline of best practices for reviewing pipelines. A couple have been in queue waiting to get reviewed, and I’m not sure everybody knows what we’re looking for.

**Kirkland Gee:** Yeah, for sure.

**Kirkland Gee:** Honestly, all we need from you guys when we're setting these things up is very simple.

**Kirkland Gee:** Most of the time, like, at least for the ones I've done, like, I've already run four or five example articles from Airtable, like, articles that were maybe ready to write or something like that.

**Kirkland Gee:** just look

**Kirkland Gee:** Look at the outputs and document any issues.

**Kirkland Gee:** Like, don't think about pipelines.

**Kirkland Gee:** Don't think about prompts.

**Kirkland Gee:** Please, like, don't even consider any of that.

**Kirkland Gee:** Just look at the final outputs and focus primarily on, like, writing guideline adhesion.

**Kirkland Gee:** Like, does this sound correct?

**Kirkland Gee:** Does the article structure make any sense?

**Kirkland Gee:** Treat it as though you're just editorially reviewing those articles.

**Kirkland Gee:** Because we can translate that feedback into, like, fixing the prompts and all the artifacts and that kind of stuff.

**Kirkland Gee:** To save you guys time, just focus on the editorial.

**Kirkland Gee:** Is this good?

**Kirkland Gee:** Is this not good?

**Andrea (Client Ops):** So when a pipeline’s in review, that’s when Client Ops has dedicated time to it. Try to get reviews done quickly—that’s when you’ll get the most help and collaboration. The ticket’s actively being worked on at that moment.

**Marcel Santilli:** All right, let's wrap up. We're going to do two scores like last time. First: how much fun did you have, one to five—one is half asleep, five is great. Second: how useful, one is waste of time, five is extremely useful. Put your scores in the chat and we'll hit enter together. Great—we did okay on fun. Maybe we'll make avatar classroom a new tradition. This was actually kind of fun.

**Marcel Santilli:** Well, I appreciate you all.

**Marcel Santilli:** It's Halloween in the U.S., so I'm going to go trick-or-treating later today with my daughter.

**Marcel Santilli:** And I hope you all have a lovely weekend.

**Megan Dickey:** See y'all.

**Kirkland Gee:** Thanks, everyone.

**Mariana Marins:** Bye, everyone.

**Mariana Marins:** Bye, guys.
