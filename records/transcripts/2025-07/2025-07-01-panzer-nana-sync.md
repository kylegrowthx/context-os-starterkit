# Panzer / Nana sync

<metadata>
date: 2025-07-01
time: 17:45 UTC
duration: 53 minutes
organizer: Matthew Panzarino (GrowthX)
participants: Matthew Panzarino (GrowthX), Mariana Marins (GrowthX)
fathom_recording_id: 71611476
fathom_url: https://fathom.video/calls/340241549
share_url: https://fathom.video/share/JKKwK1vQFhEQq24zA1-_xqr85TXPM6sg
source: fathom
enriched_on: 2026-03-03 08:30 UTC
</metadata>

---

## Summary

Matthew and Mariana aligned on three major content infrastructure initiatives: building a library of fine-tuned "virtual authors" (starting with PansGPT, based on Matthew's writing style), scaling a content quality score evaluation pipeline to assess article adherence to outlines and guidelines, and creating client-specific artifact templates to guide content generation at scale. Matthew demonstrated the custom GPT and quality scorer, showed how results flow into Airtable, and discussed plans to automate artifact creation and integrate the quality pipeline into existing article generation workflows.

---

## Context

This is a GrowthX internal sync between Matthew Panzarino (Chief Content Officer) and Mariana Marins (Delivery/Operations) focused on content operations and infrastructure. Matthew has been experimenting with AI-assisted content creation workflows and wanted to show Mariana two major systems he's built: a custom GPT trained on his writing style (for use as an editor/writer in pipelines), and an automated quality evaluation pipeline that scores finished articles against outlines and guidelines. The context is GrowthX's push toward scalable, repeatable content delivery systems that can serve both internal "dog food" needs and potentially be offered as services to clients.

---

## Relevance

- **To GrowthX Delivery:** PansGPT and the quality scoring pipeline represent foundational systems for scaling content production. Matthew's goal is to embed the quality scorer into all content pipelines (Good Call, Sunbit, client work) so every article gets automatically evaluated for outline adherence, language quality, and structure. The virtual authors concept (library of fine-tuned writing styles) could transform how GrowthX approaches client engagements and onboarding for new content managers.

- **To CheckThat:** The quality evaluation pipeline uses structured rubrics to assess content (forbidden terms, specificity, formatting, technical accuracy). This methodology aligns with CheckThat's mission to automate content auditing at scale. As the pipeline matures, it could become a CheckThat feature (AI-powered content review for B2B sites).

- **To GrowthX Business Development:** The virtual authors system could become a premium service offering — helping clients build "signature voice" AI assistants from their thought leaders' writing samples, then plugging those into content pipelines. This positions GrowthX as a platform for scalable executive/thought leader content.

---

## Overview

- Created a custom GPT (PansGPT) as a first step towards fine-tuning Matthew's writing style for potential use in content pipelines
- Implemented a content quality score evaluation pipeline to assess article adherence to outlines and writing guidelines
- Explored process for creating client-specific artifacts and pipelines to run quality evaluations on different client content
- Identified need to regularly update client artifacts with new information to improve content generation

---

## Key Topics

### Custom GPT Development

  - Matthew created PansGPT, a custom GPT based on his writing style
  - Next step is fine-tuning using 2,500+ articles to create a full assistant
  - Goal: Plug into content pipelines as an editor/writer for GrowthX's site and potentially offer as a service to clients
  - Long-term vision: Build a library of "virtual authors" for different writing styles and technical expertise

### Content Quality Score Evaluation Pipeline

  - Implemented pipeline to assess article quality post-fact-checking
  - Evaluates adherence to outline, language, headlines, structure, formatting, and specificity
  - Outputs overall score (out of 5), sectional scores, strengths, and improvement priorities
  - Results stored in Airtable for analysis
  - Next step: Run multiple articles through to populate results and assess effectiveness

### Client-Specific Artifact Creation

  - Demonstrated process for creating client-specific artifacts (audience personas, company context, writing guidelines)
  - Emphasized importance of thorough research and prompting to create comprehensive artifacts
  - Identified need to update artifacts monthly with new client information
  - Discussed potential to codify and automate parts of the artifact creation process

### Image Generation Workflows

  - Gian Piero Puleo (design engineer) working on improving image generation workflows
  - Goals: Build image picker, generate header and inline images, combine design and engineering expertise
  - Aim to create scalable solution rather than relying on manual designer work for each client

---

## Action Items

**Mariana Marins**
- Share cleaned Notion doc in all announcements channel

- Clean up Notion doc from Matthew's presentation - remove speaker notes, format intro, delete times/quotes, add icon, match schema, place in handbook delivery area (likely first 12 weeks)

- Run multiple Good Call articles through new content quality score evaluation pipeline, populate results in Airtable

- Run multiple Sunbit articles through new content quality score evaluation pipeline, populate results in Airtable

---

## Transcript
**Matthew Panzarino:** Show up for work.

**Matthew Panzarino:** This meeting is being recorded.

**Matthew Panzarino:** Pretty good.

**Matthew Panzarino:** Yeah, pretty good.

**Matthew Panzarino:** Yeah, just juggling lots of stuff.

**Matthew Panzarino:** Keep adding things to my linear pocket.

**Matthew Panzarino:** They're adding faster than I can kick them off, but that's okay.

**Matthew Panzarino:** We'll figure it out.

**Matthew Panzarino:** How do I get out of...

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** I'm going to share...

**Matthew Panzarino:** I'm going change this access to growthx.

**Matthew Panzarino:** This slideshow is kind of slapdash that I created, but we can just include it as a link.

**Matthew Panzarino:** But I'll give you this, and then that's the slideshow that I presented.

**Matthew Panzarino:** Then this is the doc, the Notion doc.

**Matthew Panzarino:** You can include a link to the Fathom at the top of this doc.

**Matthew Panzarino:** I put in a little cup.

**Matthew Panzarino:** Well, TKTK is here for the recording and for the deck.

**Matthew Panzarino:** You can rename it to fit the schema of our, like, learning and onboarding section.

**Matthew Panzarino:** We really need to rebuild that whole section.

**Matthew Panzarino:** So put this, like, right at the top so it's, like, prioritized.

**Matthew Panzarino:** I think it's under the handbook delivery area, maybe first 12 weeks.

**Matthew Panzarino:** I don't know where.

**Matthew Panzarino:** I actually don't know where onboarding and stuff lives now.

**Mariana Marins:** I will figure it out.

**Matthew Panzarino:** No problem.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** But basically create this doc and then we can share.

**Matthew Panzarino:** You can just share it into the all announcements or whatever.

**Matthew Panzarino:** Say, hey, great talk today.

**Matthew Panzarino:** Here's the actual doc if you want to reference it.

**Matthew Panzarino:** And then it'll be in our onboarding so that we can, for new CMs, anybody coming in, they can use that.

**Matthew Panzarino:** And that'll be sort of the anchor piece of

**Matthew Panzarino:** Content of our new onboarding.

**Matthew Panzarino:** And then from there, we can go into like how to use Atlas and, you know, like the actual click here, click there stuff.

**Matthew Panzarino:** We can do a little of that and all of that.

**Matthew Panzarino:** So I think this will be the first.

**Matthew Panzarino:** So on that dock, the only thing that really I would like you to do is clean up the speaker notes, the cold open, the 30 seconds, the time.

**Matthew Panzarino:** You can remove the times.

**Matthew Panzarino:** You can, you know, just leave the, you delete cold open and just make that more of an intro.

**Matthew Panzarino:** Remove the quotes, you know, just be like, Hey, this is like, it's not me speaking.

**Matthew Panzarino:** It's just the documents for me.

**Matthew Panzarino:** But that's it.

**Matthew Panzarino:** Just a couple of things like that.

**Matthew Panzarino:** Just remove those presentation notes.

**Matthew Panzarino:** I don't think there's anything else other than that. I'm pretty happy with it.

**Matthew Panzarino:** It's fine.

**Matthew Panzarino:** And the speaker notes at the bottom, can ditch those as well.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Yeah, that's about it.

**Matthew Panzarino:** And then that, that can be shareable and just match it to the little schema with a little icon and all that, and then drop it into the wherever it belongs.

**Matthew Panzarino:** And that'll tie that one off.

**Matthew Panzarino:** And then as I do these week by week, we can keep adding them to that section.

**Matthew Panzarino:** I'm sure anything I do as a learnings thing would be probably prime for the onboarding.

**Matthew Panzarino:** So get that done.

**Matthew Panzarino:** I'm continuing to chip away when I get a moment in between other stuff.

**Matthew Panzarino:** I'm continuing to chip away at the fine-tuning my voice model.

**Matthew Panzarino:** I don't think – so what did is I created a hand GPT as a tool.

**Matthew Panzarino:** Yes, that's what I was going to ask you about.

**Matthew Panzarino:** Yeah, I created it as a custom GPT, which is not as powerful as a full assistant.

**Matthew Panzarino:** You can't do it in the app either, so log into the web and let me look at where I'm at here.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** Here, I'll just kind of show you what I've – app.

**Matthew Panzarino:** this.

**Matthew Panzarino:** What I've done here, where I'm at.

**Matthew Panzarino:** So this is PansGPT.

**Matthew Panzarino:** This is a custom GPT that I created.

**Matthew Panzarino:** And this custom GPT that you can make is not as powerful as a full assistant.

**Matthew Panzarino:** It has some limitations.

**Mariana Marins:** You can provide it some...

**Mariana Marins:** created one in Pans.

**Matthew Panzarino:** I would like to know what you are going to do with this.

**Matthew Panzarino:** Yeah, yeah, yeah.

**Mariana Marins:** The end result.

**Matthew Panzarino:** The tool, yeah, the tool here, you know, I've provided it with a set, a curated selection of my articles as context.

**Matthew Panzarino:** And then given it web search and if it needs it, I haven't even done any of that.

**Matthew Panzarino:** But then that's the tuning.

**Matthew Panzarino:** And then I have my writing deadlines here that I've written, right?

**Matthew Panzarino:** This is how to write like me.

**Matthew Panzarino:** What it.

**Matthew Panzarino:** This is a good first step, and I've done some generations with it, and it's not bad.

**Matthew Panzarino:** It's pretty good.

**Matthew Panzarino:** Ballpark-y, kind of cool, all that.

**Matthew Panzarino:** So now I'm going to do the next step, which is fine-tuning.

**Matthew Panzarino:** So I'm going to take all 2,500 articles I have or whatever, and then use batches of those to fine-tune this, and create it as a full assistant, I think they call them, which is basically use the OpenAI API to create an assistant because then it can be called as an API.

**Matthew Panzarino:** So we can plug it in to things like pipelines.

**Matthew Panzarino:** So I was talking a little bit with Jason about this where I was like, hey, I would love to be able to plug this into a pipeline as an editor, right, or as a writer, because my thought process on this is, yes, near-term it would be cool to have like me,

**Matthew Panzarino:** As a GPT, or me as an assistant, so that I can send me off to edit a piece, like for our site, right?

**Matthew Panzarino:** For the output, as an example, right?

**Matthew Panzarino:** Okay, write an article in the style of Matthew Panzarino about this topic, right?

**Matthew Panzarino:** And then, or edit this article, you know, to be more like me, or whatever.

**Matthew Panzarino:** Just to be able to plug that into our workflows, so that we can, like, generate content for our dog food.

**Matthew Panzarino:** know, create content for our own sites, using that as an input.

**Matthew Panzarino:** But long-term, I would love to be able to create these, do this process of, like, getting writing samples, doing a fine-tuning, creating an assistant, and then plugging it in as an API to a workflow so that we could do it as a service, right?

**Matthew Panzarino:** Offer it either to clients or just build the pipeline for ourselves, because let's say a client is like, hey, exec, as an example.

**Matthew Panzarino:** They write about leadership topics and that sort of thing.

**Matthew Panzarino:** And let's say they really love

**Matthew Panzarino:** You know, I know, like, Daniel's a big fan of 37 Signals and, you know, how David runs that company and, like, his writing on leadership and all that.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** Let's ingest his stuff and then basically be able to apply that kind of writing style on a more fine-tuned basis.

**Matthew Panzarino:** And so build a library of writers or personas that we can use, or authors, I would guess you'd call them virtual authors, that we can then type into different topics.

**Matthew Panzarino:** Like, what if that's an engineer, like a highly technical engineer that writes about a lot of AI topics and is very good at that?

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** Can we find out how they write, break that down, fine-tune it, and then plug that into our technical workflows?

**Matthew Panzarino:** So I really think it could be a really awesome thing to basically have a, like, in our pipelines, you're selecting, you're like, okay, the, the.

**Matthew Panzarino:** Here's the topic and all that.

**Mariana Marins:** And then what persona are we having writing this?

**Matthew Panzarino:** Or what author are we having to write this?

**Matthew Panzarino:** Is it like the technical guru?

**Matthew Panzarino:** Is it the product reviewer?

**Matthew Panzarino:** Is it the leadership thought leader?

**Matthew Panzarino:** Whatever, you know, like Marcel has done that little card based thing with all the different like personalities, you know, it's like, oh, what kind of personality is your company?

**Matthew Panzarino:** Just as like an illustrative guide when he's talking to clients.

**Matthew Panzarino:** What if that was actually like, okay, choose this one.

**Matthew Panzarino:** And this one is how your content gets written.

**Matthew Panzarino:** So this is my experiment to like, say, okay, let me start with me, because I have my own content.

**Matthew Panzarino:** And I know I can judge whether or not I've done a good job fine tuning.

**Matthew Panzarino:** And then we can, we can kind of go from there and start creating more.

**Matthew Panzarino:** I think it would be really cool to do it, figure out how to ingest it into a pipe or connect it to a pipeline as essentially a writing guideline, right?

**Matthew Panzarino:** Like, that's what it is.

**Matthew Panzarino:** It's a writing guideline, how to write like this person.

**Matthew Panzarino:** Rather than trying to write like, we imagine that company writes.

**Matthew Panzarino:** It's like, how

**Matthew Panzarino:** Hey, here's some examples.

**Matthew Panzarino:** Here's a library of voices.

**Matthew Panzarino:** And here's how they write.

**Matthew Panzarino:** Which one do you think align?

**Matthew Panzarino:** Well, I think this, you know, this would align really well.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** And then we can start drafting their articles and calibrating from there.

**Matthew Panzarino:** And then we can always tweet the guidelines from there.

**Matthew Panzarino:** But I think this will provide us with like a library of authors, so to speak, a library of voices.

**Matthew Panzarino:** So I'm going start with me.

**Matthew Panzarino:** So I'm going to work on that.

**Matthew Panzarino:** If it gets to points where I think I can like hand off or involve you, I will.

**Matthew Panzarino:** Right now, it's still, I'm trying to tie a bunch of pieces together.

**Matthew Panzarino:** So I'm going to, I'm going to try and find some time to do that.

**Matthew Panzarino:** And then I will keep you abreast so that you know where I'm at.

**Matthew Panzarino:** I think, I think as a, I thought, I thought, I you could share custom GPTs.

**Matthew Panzarino:** Let me see if I can share this with you.

**Mariana Marins:** I the link.

**Matthew Panzarino:** Oh, I did?

**Mariana Marins:** Okay, cool.

**Mariana Marins:** I think, because we did this in my previous company, I think we need to be logged into the same account so that I can use it, you know?

**Matthew Panzarino:** Are you sure about this?

**Matthew Panzarino:** Because it says anybody with a link.

**Mariana Marins:** Yeah, but like, it didn't work that well.

**Mariana Marins:** It was like, okay, I can use it, but I have to go to the link all the time.

**Mariana Marins:** And it's not there on my sidebar for me whenever I I see what you're saying.

**Mariana Marins:** You have to like, bookmark this and go directly to it.

**Mariana Marins:** Exactly, yeah.

**Matthew Panzarino:** Like, it works, but it's not the most comfortable app that you could have it.

**Matthew Panzarino:** I see what you're saying.

**Matthew Panzarino:** But anyhow, yeah, this is just a temporary plug.

**Matthew Panzarino:** You don't need to go too crazy with it, because it was just like, I wanted to see if it would do any good at all, right?

**Matthew Panzarino:** And then from there, the fine-tuning should only be better from this point.

**Matthew Panzarino:** So that's my goal is to try and find some time to fine-tune this.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Second, there is a, so the, the content quality score evaluation pipeline, the one that.

**Mariana Marins:** I saw that you, you marked the two-do as done.

**Matthew Panzarino:** So what happened?

**Matthew Panzarino:** Yeah, I saw, I marked it as done because we're sort of like, oh yeah, hey, look at this.

**Matthew Panzarino:** And I looked at it.

**Matthew Panzarino:** I'm done.

**Matthew Panzarino:** Now I need to actually, I think the next step is to really get some content flowing through here so that we can see what it looks like at scale.

**Matthew Panzarino:** Like get a pipeline going with this on the end of it so that it, we can like have this judge a bunch of content, right?

**Matthew Panzarino:** And like, almost like a fact checker, but I don't know, quality checker.

**Matthew Panzarino:** exactly.

**Matthew Panzarino:** would be, live at the end.

**Matthew Panzarino:** After fact checking, after all of that, this workflow would take as an input.

**Matthew Panzarino:** The, it takes, well, it takes two specific things as input.

**Matthew Panzarino:** It takes the, well, four things.

**Matthew Panzarino:** The client name, the article name.

**Matthew Panzarino:** I'll show you this.

**Matthew Panzarino:** You can see it in my sandbox as well.

**Matthew Panzarino:** But it takes the article name, the client name, the final draft, post fact-checking, all of that.

**Matthew Panzarino:** And it takes the outline.

**Matthew Panzarino:** So what this is really doing is it's judging, okay, how well did the workflow, did the pipeline perform between outline and final draft?

**Matthew Panzarino:** So it does not judge how well the outline was made.

**Matthew Panzarino:** It judges the adherence from the outline to the final output.

**Matthew Panzarino:** So this would be, of course, article generation, writing guidelines.

**Matthew Panzarino:** Application, fact-checking, and I'm thinking is really a side note.

**Matthew Panzarino:** So it basically takes the how well did those steps work.

**Matthew Panzarino:** So this is not how well did the brief work, you know, or to generate the outline.

**Matthew Panzarino:** This is how well, how closely did it follow the outline.

**Matthew Panzarino:** And if you look at the output here, you can see it's got this detailed analysis, and it gives it a score of 3.7.

**Matthew Panzarino:** But if you look at the analysis...

**Mariana Marins:** What's the maximum of the scores?

**Mariana Marins:** Is it 5?

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Yeah, I'll show you how it works.

**Matthew Panzarino:** So it basically...

**Matthew Panzarino:** Where's the...

**Mariana Marins:** nice because it says what you have to do to make it better to get to the level.

**Matthew Panzarino:** Exactly.

**Matthew Panzarino:** I don't know why that's not exposed here.

**Matthew Panzarino:** It should be exposed here.

**Matthew Panzarino:** Why am I not seeing it?

**Matthew Panzarino:** It should be shown here somewhere.

**Matthew Panzarino:** Here, I wonder where that.

**Matthew Panzarino:** That's weird.

**Matthew Panzarino:** Because, like, yeah, it should show somewhere.

**Matthew Panzarino:** Maybe there's just a field that needs to be exposed.

**Matthew Panzarino:** I'll talk to Kirkland about that.

**Matthew Panzarino:** But, yes, exactly.

**Matthew Panzarino:** Like, the output here shouldn't just be the score.

**Matthew Panzarino:** It should also be the feedback.

**Matthew Panzarino:** And so, like, the feedback is there on this tab just to scroll down.

**Matthew Panzarino:** Yeah, no, no.

**Matthew Panzarino:** It's here.

**Matthew Panzarino:** It's here.

**Mariana Marins:** But, like, it should be in the output.

**Mariana Marins:** It should be presented right below the, you know, this is not the end.

**Mariana Marins:** for people to see.

**Matthew Panzarino:** Exactly.

**Matthew Panzarino:** This is not the end, right?

**Matthew Panzarino:** The end is the end.

**Matthew Panzarino:** The output is the output.

**Matthew Panzarino:** This is the output of this step.

**Matthew Panzarino:** But then it needs to be formatted and presented well.

**Matthew Panzarino:** So, in the output here, it be overall score, score by section, input per section, or feedback by section.

**Matthew Panzarino:** So, if you look here, it is the...

**Matthew Panzarino:** Um, what, why we, we care about it, what's the improvement, remove language, upgrade headlines, yada, yada, yada.

**Matthew Panzarino:** And you can see here, it scores individually for these characteristics.

**Matthew Panzarino:** Language, headline, structure, technical, formatting, specificity, and outline adherence.

**Matthew Panzarino:** Outline adherence, I think, is the total overall.

**Matthew Panzarino:** But, like, you see, that's, that's what these sections correspond to, right?

**Matthew Panzarino:** Right, language is the first one, um, or maybe technical is the first one.

**Matthew Panzarino:** I don't know how he ranked these, but that's the idea, though.

**Matthew Panzarino:** Each of these are scored individually.

**Matthew Panzarino:** Then they have strengths.

**Matthew Panzarino:** So these are the things that are good about them.

**Matthew Panzarino:** This is good, you know, this is good.

**Matthew Panzarino:** So it's, like, wins and losses, right?

**Matthew Panzarino:** And then, um, just some meta around it.

**Matthew Panzarino:** And then here's the overall score, overall grade, um, recommendation, major revision, right?

**Matthew Panzarino:** So it's, like, hey, you should, you should do this.

**Matthew Panzarino:** Um, contains forbidden terms, streamline, you know?

**Matthew Panzarino:** Like, we don't like the word.

**Matthew Panzarino:** But ensure, maximize, pitfalls, streamline.

**Mariana Marins:** know, words that we take.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** Whatever you've got in there that we decide to add to the grading rubric.

**Matthew Panzarino:** So the output here, okay, let's do this.

**Matthew Panzarino:** So I think that the output should expose the section-by-section scores.

**Matthew Panzarino:** It should expose the improvement priorities by section, and then the strengths by section.

**Matthew Panzarino:** So basically, you should just present all those at the output step here.

**Matthew Panzarino:** The score, the reason that this is presented just as a score, I would just like those all on the screen so people can see them, you know.

**Matthew Panzarino:** And the reason the score is here is because...

**Matthew Panzarino:** And it ends up in an Airtable like this.

**Matthew Panzarino:** So this content quality scoring Airtable, this basically just is where it would dump out, right?

**Matthew Panzarino:** And this has all these fields, right?

**Matthew Panzarino:** It exposes all these fields that they're working with.

**Matthew Panzarino:** What's the executive summary?

**Matthew Panzarino:** Not ready for a location, score of 3.7 out of 5, major revisions necessary, critical issues including yada, yada, yada, right?

**Matthew Panzarino:** Prioritize all this stuff.

**Matthew Panzarino:** It's basically like, hey, how far off are you, right?

**Matthew Panzarino:** And the same thing goes for, like, you've got overall score, you've got your overall grade, that sort of thing.

**Matthew Panzarino:** And then publish ready is that tick box.

**Matthew Panzarino:** And then here's the scores per, scores by section.

**Matthew Panzarino:** So it's all exposed in Airtable, which is...

**Matthew Panzarino:** How do you side scroll in Airtable?

**Matthew Panzarino:** Is it just arrow?

**Matthew Panzarino:** God dang it, I never know how.

**Matthew Panzarino:** What's the side scroll thing in?

**Matthew Panzarino:** How do you scroll to the side?

**Mariana Marins:** I think it's control and then the arrow.

**Matthew Panzarino:** Try it.

**Matthew Panzarino:** No.

**Matthew Panzarino:** I don't know whether it's just because I'm in Safari or something.

**Mariana Marins:** I I think it's maybe...

**Matthew Panzarino:** I never remember, and it's always so annoying to me.

**Mariana Marins:** Like, I need to be there doing it, and then it comes naturally.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** I think you can highlight a cell and just move over, so that works.

**Matthew Panzarino:** But, yeah, AI, exactly.

**Mariana Marins:** Muscle memory, right?

**Mariana Marins:** I'm the same way.

**Matthew Panzarino:** How do do that?

**Matthew Panzarino:** I don't know.

**Mariana Marins:** Let me get the keyboard.

**Matthew Panzarino:** My wife hates that.

**Matthew Panzarino:** Like, let me get the keyboard.

**Matthew Panzarino:** So just tell me.

**Matthew Panzarino:** I'm like, I don't even know.

**Mariana Marins:** Let me just touch it.

**Matthew Panzarino:** But, yeah, so all of those things I was talking about are exposed here.

**Matthew Panzarino:** I just think that they should be exposed in the outfield in Airtable as well.

**Matthew Panzarino:** Or, excuse me, in Atlas as well.

**Matthew Panzarino:** But it's good that it's here.

**Matthew Panzarino:** You we have all this stuff here.

**Matthew Panzarino:** But I want to basically just start running a bunch through here.

**Matthew Panzarino:** So I want...

**Matthew Panzarino:** Just to be full of articles.

**Mariana Marins:** Then we can judge how well it's working and all that stuff.

**Mariana Marins:** So to do that.

**Mariana Marins:** And these articles are going to be the ones that exist already?

**Mariana Marins:** Or you were going to create some just to go through this?

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** So there's two ways to do it.

**Matthew Panzarino:** You can hit add here and just input article, the title, content, client name, content, and outline.

**Matthew Panzarino:** So if we go to an existing workflow, we could grab these manually and do it, put it in here, or hit create and run it.

**Matthew Panzarino:** would do it, right?

**Matthew Panzarino:** But I think what we should do is in my sandbox, we can just create a new pipeline.

**Matthew Panzarino:** Let's just call it.

**Matthew Panzarino:** Let's just do this.

**Matthew Panzarino:** Actually, let's do this.

**Matthew Panzarino:** Let's do this.

**Matthew Panzarino:** Edit this.

**Matthew Panzarino:** I think, I think, I think.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Okay, yeah, I think I need all of this stuff.

**Mariana Marins:** Is steps no?

**Matthew Panzarino:** No, I need the steps too, but it's just about where they go.

**Matthew Panzarino:** So, okay, input schema, environment input schema, and then steps of the schema, okay.

**Matthew Panzarino:** Because we need to wire it up, right?

**Matthew Panzarino:** So if we go to article generation and then edit this, so input schema, I think we need to add some content here.

**Matthew Panzarino:** So I don't know what I'll do here.

**Matthew Panzarino:** I'm going to stop sharing for a second.

**Matthew Panzarino:** But yeah, I think I'll figure out.

**Matthew Panzarino:** I can figure this out.

**Matthew Panzarino:** So we need to input the input schema into here.

**Matthew Panzarino:** I just basically want to add this to the end of this workflow, right?

**Matthew Panzarino:** But then, of course, we have to adjust the inputs and outputs.

**Matthew Panzarino:** Okay, where does it take these from?

**Matthew Panzarino:** You know, grab the outline from the outline, that sort of thing.

**Matthew Panzarino:** But I think we can do it.

**Matthew Panzarino:** I think we can figure it out.

**Matthew Panzarino:** Because then...

**Matthew Panzarino:** Let's see.

**Matthew Panzarino:** I'm going to try and be really hacky about this.

**Matthew Panzarino:** Let's see if it works.

**Matthew Panzarino:** I'm to try again.

**Matthew Panzarino:** Steps, I think that works.

**Matthew Panzarino:** Okay, I'll figure out how to reflow that.

**Matthew Panzarino:** But basically, I want to tack it on to the end of this pipeline.

**Matthew Panzarino:** If you want to take a crack at it, you can.

**Matthew Panzarino:** Otherwise, I'll get around to it as soon as I make my way through some of my list.

**Matthew Panzarino:** So the article generation pipeline here, I'll basically just grab – I'll pick a company and duplicate their artifacts into here.

**Matthew Panzarino:** We can just do like –

**Matthew Panzarino:** Or something.

**Matthew Panzarino:** Doesn't have to be anything special.

**Matthew Panzarino:** And then grab their artifacts and duplicate it.

**Matthew Panzarino:** You might actually want to just do it from scratch so we don't get confused.

**Matthew Panzarino:** So let's do this.

**Matthew Panzarino:** Let's create a new project.

**Matthew Panzarino:** Let's call it ContentEval.

**Matthew Panzarino:** Let's see.

**Matthew Panzarino:** That way it has a new project with its own new pipelines.

**Matthew Panzarino:** We can just grab this pipeline by default to start with.

**Matthew Panzarino:** I think this was Good Call is originally where I grabbed this from.

**Matthew Panzarino:** So we can just do Good Call.

**Matthew Panzarino:** That's fine.

**Matthew Panzarino:** We don't have to change anything additional.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Got that pipeline.

**Matthew Panzarino:** So the content evaluation testing has its own article generation pipeline here.

**Matthew Panzarino:** It's going to grab these defaults.

**Matthew Panzarino:** This is all a good call, so we can just leave it all.

**Matthew Panzarino:** It's fine.

**Matthew Panzarino:** It's going to grab these, which is totally fine.

**Matthew Panzarino:** Then we need to tack this on to the end of this article generation workflow.

**Matthew Panzarino:** Yeah, so this workflow specifically, the content quality score evaluation, we need tack this on to the end of the article generation pipeline here.

**Matthew Panzarino:** Yeah, let's call it, let's do this.

**Matthew Panzarino:** We're going to do this, article generation with quality.

**Matthew Panzarino:** That way we can not call the same everywhere.

**Matthew Panzarino:** That way we know what we're looking at.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** This just needs to get tacked on to the end of that, and I need to figure out how to add this YAML.

**Matthew Panzarino:** Here, to the end of that other pipeline.

**Matthew Panzarino:** And this may be something that, like, we can ask Claude, hey, I've got this.

**Mariana Marins:** Just basing it in the end, it's not going to cut it.

**Matthew Panzarino:** No, yeah, that won't work because it needs to establish the schema for the inputs and outputs at the top of the YML.

**Matthew Panzarino:** And then it needs to, okay, how about you do it anyway?

**Matthew Panzarino:** I said so.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Wait, is this?

**Matthew Panzarino:** Okay, yeah, whatever it is.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Hi.

**Matthew Panzarino:** How are you?

**Matthew Panzarino:** I am fine.

**Matthew Panzarino:** Um...

**Matthew Panzarino:** am I the comments

**Matthew Panzarino:** Okay, let's see what it does here.

**Matthew Panzarino:** Let's see how, let's see if can one-shot this.

**Matthew Panzarino:** Okay, so workflow step we want to add is this one.

**Matthew Panzarino:** And then we need to grab...

**Matthew Panzarino:** Thank

**Matthew Panzarino:** Which one did I give it?

**Mariana Marins:** Oh, yeah, I gave it that.

**Matthew Panzarino:** Okay.

**Mariana Marins:** Yeah, that's I going to say.

**Matthew Panzarino:** Which one did I just give it?

**Matthew Panzarino:** There we go.

**Matthew Panzarino:** Here it is.

**Matthew Panzarino:** Enjoy.

**Matthew Panzarino:** Because the variables are named the same things, I think it has a good chance to succeed because the inputs that the content quality checker taking are named the same thing, right?

**Matthew Panzarino:** They are in outline, client name, article name, you know, that kind of thing.

**Matthew Panzarino:** is.

**Matthew Panzarino:** is.

**Matthew Panzarino:** Thank

**Mariana Marins:** Is this the procedure the CMs need to do every time they watch?

**Matthew Panzarino:** I don't want any CM ever doing this.

**Mariana Marins:** Okay.

**Matthew Panzarino:** Just asking.

**Mariana Marins:** Yeah, it would cause more issues.

**Mariana Marins:** Exactly.

**Mariana Marins:** I read somewhere that we shouldn't create any new pipelines or something like that.

**Matthew Panzarino:** Right.

**Matthew Panzarino:** So here's the story about this.

**Matthew Panzarino:** This can get confusing.

**Matthew Panzarino:** I mean, it's confusing to me, you know, and I understand exactly what it's doing, right?

**Matthew Panzarino:** And obviously, the ENG team, it's very, it's like reading English to them, right?

**Matthew Panzarino:** So they're fine with it.

**Matthew Panzarino:** But there's a limited number of people that basically Daniel trusts to mess around with these, because then we don't get off so far off into the wilderness that we end up being unable to end our way back.

**Matthew Panzarino:** And there was a big chunk of time there where he was making broad changes to all of the pipelines at once.

**Matthew Panzarino:** And...

**Matthew Panzarino:** Needed to know what steady state they were all in in order to make those changes.

**Matthew Panzarino:** So people were sort of like creating custom versions of them.

**Matthew Panzarino:** And then, of course, that would create forks, which were then unable to be, you know, edited.

**Matthew Panzarino:** So it's not so much that it's like, it's not going to break anything.

**Matthew Panzarino:** You know, it's not going to mess anything up to do this.

**Matthew Panzarino:** But it also is not going to really do anybody any favors.

**Matthew Panzarino:** So he just said, please stop doing it for now.

**Matthew Panzarino:** Or let Daryl or Matthew or whoever play with it if you really need it.

**Matthew Panzarino:** But this is exactly what Kirkland's doing when he's doing like PSCO workflows for people.

**Matthew Panzarino:** You know, he's creating artifact on the back end and then linking it to this.

**Matthew Panzarino:** Okay, let me adapt.

**Mariana Marins:** see.

**Mariana Marins:** And speaking of which, did you have a chance to take a look at the schema that I wrote for PSO?

**Mariana Marins:** Or do you need me to?

**Mariana Marins:** Because it's not on your to-do's yet.

**Mariana Marins:** I can't put there so you can remember.

**Matthew Panzarino:** remember.

**Mariana Marins:** So we had a meeting with Kirk and Daniel.

**Matthew Panzarino:** yeah, yeah.

**Matthew Panzarino:** You wrote up like, hey, I'm not so sure about this, but check this out.

**Matthew Panzarino:** Exactly, yes.

**Matthew Panzarino:** Yeah, you can have that to introduce because that'll be great raw material for me to use when we talk about PSEL workflows.

**Matthew Panzarino:** I'll go in and make sure that its statements are correct, that it follows the actual story, and then we'll go from there.

**Matthew Panzarino:** But yeah, sounds good.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** What's one more?

**Matthew Panzarino:** Hey, it took it.

**Matthew Panzarino:** Okay, so this has the evaluation score right here.

**Matthew Panzarino:** Let's try something.

**Matthew Panzarino:** This is not right though.

**Matthew Panzarino:** This is not right.ul Version 3.

**Matthew Panzarino:** This is not right.

**Matthew Panzarino:** This one wrong.

**Mariana Marins:** Thank

**Mariana Marins:** It maybe created something, like Fathom created something that it wanted and not really what you wanted.

**Matthew Panzarino:** You're absolutely right.

**Matthew Panzarino:** I love how it does that.

**Matthew Panzarino:** Well, if I'm right, and you know I'm right, why didn't you do it in the first place?

**Matthew Panzarino:** Cracks me up.

**Matthew Panzarino:** What was it?

**Matthew Panzarino:** What is it called?

**Matthew Panzarino:** It's not called Topic, right?

**Matthew Panzarino:** It's called...

**Matthew Panzarino:** Oops.

**Matthew Panzarino:** Oh, it's called Topic.

**Matthew Panzarino:** I?

**Matthew Panzarino:** It's called Topic.

**Matthew Panzarino:** called?

**Matthew Panzarino:** is thebild, What What

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Okay, so let's give this a try.

**Matthew Panzarino:** If this doesn't one-shot it, then I'll go off and edit it.

**Matthew Panzarino:** But this is a project, basically, I would love for you to, like, if I can get this running once, I would love for you to kind of run a bunch.

**Matthew Panzarino:** You can just grab topics from, like, Good Call and just run a bunch of them through here so that we can populate this.

**Matthew Panzarino:** With some results to see where we are, if we like it, we don't like it, you know, all of that stuff.

**Matthew Panzarino:** We're not doing that here.

**Matthew Panzarino:** That's not edit our original.

**Matthew Panzarino:** Quality analysis has no default value.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** I'll put schema for quality analysis.

**Matthew Panzarino:** I don't know.

**Matthew Panzarino:** Okay, go on.

**Mariana Marins:** quality on the variable?

**Matthew Panzarino:** Yeah, it is, but it doesn't have, let's see, let's see what it has to say about this.

**Matthew Panzarino:** It doesn't, it's not attached to the proper output.

**Matthew Panzarino:** I'm sure, and this is just for testing of the quality eval, so I would not deploy this anywhere.

**Matthew Panzarino:** I'm sure that Kirkland could do this in a few minutes.

**Matthew Panzarino:** air.

**Matthew Panzarino:** are stuff That I

**Matthew Panzarino:** But this way, we don't have to burden them, and we just get some results.

**Matthew Panzarino:** just want to get some results.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Yeah, add it back.

**Matthew Panzarino:** This is crazy sometimes.

**Matthew Panzarino:** It's so wild.

**Mariana Marins:** It's like, you know, I did it wrong.

**Matthew Panzarino:** of its own.

**Mariana Marins:** Yeah.

**Mariana Marins:** I did it wrong.

**Matthew Panzarino:** I could do it right.

**Mariana Marins:** I just don't want to.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** I don't want to.

**Matthew Panzarino:** I just want to mess with you.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** I mess I don't don't

**Matthew Panzarino:** Probably not correct either, let's see, yeah, no, it's so funny, it's the same one, here, let's just try this.

**Matthew Panzarino:** Yeah, okay, um, yeah, that's what it was, it was calling it as a Boolean, not a string.

**Matthew Panzarino:** Okay, so let's see, direction, category, it still doesn't have a topic.

**Matthew Panzarino:** Oh, wait, here it is.

**Matthew Panzarino:** It's just, it's all messed up.

**Matthew Panzarino:** So it's like wrong order, but I don't really care about that.

**Matthew Panzarino:** As long as the inputs and outputs are fine.

**Matthew Panzarino:** Okay, so let's do this.

**Matthew Panzarino:** Let's just test one together and then we can part ways.

**Matthew Panzarino:** Okay, good call.

**Matthew Panzarino:** Let's grab just one of their recent topics.

**Matthew Panzarino:** Oh, this is their DSC workflow, think, isn't it?

**Mariana Marins:** Probably because the topics are very, very similar and straightforward.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Oh, well, it is.

**Matthew Panzarino:** It's okay.

**Matthew Panzarino:** Just for testing purposes, it's not going to lie.

**Mariana Marins:** So let me ask you something.

**Mariana Marins:** If I grab things, because the one you used to create the code was good call.

**Mariana Marins:** If I use things from...

**Mariana Marins:** Other clients, it's not going to work.

**Matthew Panzarino:** No, we need to create new artifacts for those clients and then attach those to a separate pipeline.

**Matthew Panzarino:** duplicate the pipeline and then attach those artifacts to that separate pipeline.

**Matthew Panzarino:** So if, for instance, you want to say, okay, I want to run a bunch of Sunbit through this.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** So we have to copy Sunbit's artifacts over to ours.

**Matthew Panzarino:** You can just name them, you know, company context underscore Sunbit.

**Matthew Panzarino:** Then you have to copy the pipeline so that it's a new Sunbit article generation pipeline.

**Matthew Panzarino:** With corrections, with content quality assessment.

**Matthew Panzarino:** And then you have to add the inputs of that, those artifacts to match the names of the three artifacts you just created.

**Matthew Panzarino:** That's the process.

**Matthew Panzarino:** It's not too hard.

**Matthew Panzarino:** If you need me to walk you through it, I can, but it's not that complex.

**Matthew Panzarino:** So let's do this.

**Matthew Panzarino:** Let's do this input.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** See, they're doing this, like, really specific assignment direction.

**Matthew Panzarino:** And.

**Matthew Panzarino:** And...

**Matthew Panzarino:** Situation here, but let's just do this, just a, oops, good call, good call.

**Matthew Panzarino:** Let's run it and see what happens, so to, let's just do, let's say we want, let's just call it CET, so these names don't get all sunbitch.

**Matthew Panzarino:** Make a new project for that.

**Matthew Panzarino:** We can take this pipeline that we don't even know if it works yet or not.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** We copy that.

**Matthew Panzarino:** So you hit edit and you copy that.

**Matthew Panzarino:** The whole pipeline, just all the YAML.

**Matthew Panzarino:** Then you come out here and go to our new Sunbit pipelines.

**Matthew Panzarino:** We have none, right?

**Matthew Panzarino:** So we create a new one.

**Matthew Panzarino:** Drop that in.

**Matthew Panzarino:** Sunbit.

**Matthew Panzarino:** So that it pre-populates that field with Sunbit.

**Matthew Panzarino:** Might as well do that.

**Matthew Panzarino:** Then search for all references of good call.

**Matthew Panzarino:** I think it's sunbit.com.

**Matthew Panzarino:** So

**Matthew Panzarino:** Yeah, namespace, fun bit, this is for the SEO check, oops, I think that, I think that's it, let's see, yeah, that should be it.

**Matthew Panzarino:** So we're going to, okay, I'm just going to create this, we're going to to come back to this in a second and change it.

**Matthew Panzarino:** Go to artifacts, right, and then audience personas right here, so it says artifacts audience personas, so create a new one, call it sun bit audience personas.

**Matthew Panzarino:** Thank very much for Bye.

**Matthew Panzarino:** Bye.

**Matthew Panzarino:** Bye.

**Matthew Panzarino:** Bye.

**Matthew Panzarino:** Bye.

**Matthew Panzarino:** Sunbit, audience personas.

**Matthew Panzarino:** Guidelines, it's always guidelines for now.

**Matthew Panzarino:** Sunbit, personas.

**Matthew Panzarino:** We use...

**Matthew Panzarino:** Let's do that for now.

**Matthew Panzarino:** See this Sunbit, audience personas here, right?

**Matthew Panzarino:** We got to go over to...

**Matthew Panzarino:** I would create all three, but once you create them, then you go to the pipeline.

**Matthew Panzarino:** And then you find Sunbit.

**Matthew Panzarino:** Sorry, persona.

**Matthew Panzarino:** The artifacts, audience personas, and then you got to do Sunbit like that.

**Matthew Panzarino:** That's it.

**Matthew Panzarino:** You just find all...

**Matthew Panzarino:** It's like literally replacing word for word with the very...

**Matthew Panzarino:** Well, the artifact we've created, the artifact variable we've created, and then find, I think that's it.

**Matthew Panzarino:** It's like only a couple of places that it calls personas, right?

**Matthew Panzarino:** And the same thing goes for the rest of the stuff, right?

**Matthew Panzarino:** So, or the other two artifacts.

**Matthew Panzarino:** So save that, and obviously we would need to go then actually put something in those fields into the actual personas, just blah, blah for now.

**Matthew Panzarino:** But same thing for company context, right?

**Matthew Panzarino:** So for company context, it's artifacts, company underscore context, right?

**Matthew Panzarino:** So we can just create an artifact.

**Matthew Panzarino:** That's it, right?

**Matthew Panzarino:** And then guidelines, whatever the context is here.

**Matthew Panzarino:** Blah, blah, blah.

**Matthew Panzarino:** They can just copy that text from the one that already exists on the existing pipeline.

**Matthew Panzarino:** Yeah, in the SunBit pipeline, correct.

**Matthew Panzarino:** In their workspace.

**Matthew Panzarino:** Yes, exactly.

**Matthew Panzarino:** And I would guess that most of them are going to be sort of good, sort of bad, but you just grab it for now.

**Matthew Panzarino:** And whatever their current one is, right, that's really what we should be evaluating.

**Mariana Marins:** Yeah, exactly.

**Mariana Marins:** That's what I was saying.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** So even if it's bad, we need to know.

**Matthew Panzarino:** Exactly.

**Matthew Panzarino:** So then you would go here, hit edit, find company.

**Matthew Panzarino:** Context.

**Matthew Panzarino:** Yeah, specifically.

**Matthew Panzarino:** And then you would just, right?

**Matthew Panzarino:** Mm-hmm.

**Matthew Panzarino:** I think it's just the one because it just calls it in the full context, I think.

**Matthew Panzarino:** Pretty sure.

**Mariana Marins:** Oh, no, there.

**Matthew Panzarino:** Oh, yeah, here it is.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah, Thank you.

**Matthew Panzarino:** I guess it's only those two pieces.

**Matthew Panzarino:** So save, and then same thing goes for the third one, which was writing guidelines.

**Matthew Panzarino:** Okay, so same concept for that.

**Matthew Panzarino:** Let's go check, see what we've got here.

**Matthew Panzarino:** At least these bits aren't broken yet.

**Mariana Marins:** Yes.

**Matthew Panzarino:** This one I think is a human review step, so it should drop up.

**Mariana Marins:** me ask you something.

**Mariana Marins:** Because we do have the image generator on the flow, but now we have a designer.

**Mariana Marins:** So what's going to happen with this?

**Matthew Panzarino:** So right now.

**Matthew Panzarino:** now.

**Matthew Panzarino:** Um, if you, like, over in the, over in EPD land, um, he's starting to look at all of the image generator workflows to make sure that we have, that those things are built out.

**Matthew Panzarino:** Like, it's a combination of engineering and design resources to help make sure, like, they produce good content that's actually useful, but also, like, we need an image picker built, right, in the image generation workflows.

**Matthew Panzarino:** Right now, it's, like, the URLs.

**Matthew Panzarino:** That's not useful, you know?

**Matthew Panzarino:** need an image picker.

**Matthew Panzarino:** It also needs to be able to generate header images as well as inline images.

**Mariana Marins:** So it's a combination of design and engineering work.

**Mariana Marins:** That's the way that that's going, going to happen.

**Matthew Panzarino:** Um, so I think it's, uh, his name starts with a G.

**Matthew Panzarino:** Who is it?

**Matthew Panzarino:** Um, I don't remember.

**Mariana Marins:** started.

**Mariana Marins:** I mean, just, uh, Gian Piero, maybe.

**Mariana Marins:** Yes, Gian Piero Puleo.

**Mariana Marins:** Ah, is the, he's the designer.

**Mariana Marins:** Okay, cool.

**Matthew Panzarino:** Got it.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** If you, yeah, if you look at, well, he's, he's...

**Matthew Panzarino:** Specifically, design engineer, which is what we need, right?

**Mariana Marins:** need, like...

**Matthew Panzarino:** Now I understand.

**Matthew Panzarino:** Because what was told to be was exactly, ah, he's a designer.

**Matthew Panzarino:** So I was like, okay, so why are students generating images?

**Matthew Panzarino:** Right, right.

**Matthew Panzarino:** Yeah, no, the goal should not be, like, every client gets a designer to open Figma and write, you know, and draw something for them.

**Matthew Panzarino:** That would be impossible to scale, right?

**Matthew Panzarino:** so while it's, like, we have designers around that could do one-offs or work with us to do, like, prototypes, especially, or presentations for clients.

**Matthew Panzarino:** This is the Slack that I was referring to because he's like, hey, I'm going to be working on this workflow.

**Matthew Panzarino:** And so his job as a design engineer is like, okay, now, like, I understand what the semantics of design are and how to prompt for good images and then how to build the workflows for them.

**Matthew Panzarino:** That's what we need.

**Matthew Panzarino:** And this is essentially what we need as a publisher.

**Mariana Marins:** Same kind of thing.

**Matthew Panzarino:** Right, where it's, like, somebody who can build the tools to help us publish but also understands the new

**Matthew Panzarino:** This is a publishing, and in a pinch, they're to be like, don't worry about it, I got it, and they get something published for us, you know, whatever the case may be, so.

**Matthew Panzarino:** Okay, got it.

**Mariana Marins:** Well, so.

**Matthew Panzarino:** Oh, let's see, this is, okay, it's generating the draft, it's going, we'll see what happens in the end of this, but yeah, that's the kind of, none of it, I would love to run like a dozen articles through for a good call, and maybe a dozen through for Sunbit, and see what kind of quality scores we're getting.

**Matthew Panzarino:** I just want to, I want to start using it, I got to start seeing whether it works or really want to help you with the artifacts, because I think it's like just some mechanic thing that I can do for, and then like it's ready, and everyone can use it, but I need to study this.

**Matthew Panzarino:** a separate topic, that's a separate topic.

**Matthew Panzarino:** has done this, right, and I need to understand.

**Matthew Panzarino:** It's yes, and you and I can walk through it together, we can like go through through together.

**Matthew Panzarino:** Will.

**Matthew Panzarino:** So I think a place to begin, if you wanted to start with some automation that you can do to pull out some information, is grab one of the sprint calls where he ran through that process.

**Mariana Marins:** Because he did it for us in person in the office.

**Mariana Marins:** Yeah, that's what I was going to ask.

**Matthew Panzarino:** We didn't record it, alas.

**Matthew Panzarino:** Exactly.

**Matthew Panzarino:** I could also build a guide for people, you know.

**Matthew Panzarino:** I might have recorded it.

**Matthew Panzarino:** And granola.

**Matthew Panzarino:** So I'll go look for that.

**Matthew Panzarino:** I might have him talking about it, but it doesn't have any of the visuals.

**Matthew Panzarino:** But essentially, the process is, like, multifaceted.

**Matthew Panzarino:** He's pulling deep research.

**Matthew Panzarino:** He's combining that with good prompting that asks, like, hey, what kinds of topics have been written about this company before?

**Matthew Panzarino:** What kind of people were writing about those topics?

**Matthew Panzarino:** Give me, like, an example of a bunch of them.

**Matthew Panzarino:** And you go through and you go, like.

**Matthew Panzarino:** I really like these three.

**Matthew Panzarino:** Could you build a persona off of these as somebody who would be reading about this?

**Matthew Panzarino:** You know, who are the readers of these authors?

**Matthew Panzarino:** Like it's a multifaceted approach to creating a more holistic view.

**Matthew Panzarino:** And he didn't even include in that process, which I think we should, things like grabbing the transcript.

**Matthew Panzarino:** Actually, he did some of it.

**Matthew Panzarino:** Grabbing transcripts of a recent client call, putting that in there and saying, hey, pull out wants and needs.

**Matthew Panzarino:** Make sure we integrate this into their voice and tone or writing guidelines, things like that.

**Matthew Panzarino:** And so that process is the one that needs to be done for all the artifacts.

**Matthew Panzarino:** And right now, essentially, none of them have had that done.

**Matthew Panzarino:** Maybe the ones Jason has worked on a little bit or some of the ones that I've done, but that majority of them, no.

**Matthew Panzarino:** So they are nowhere near as good as they could be, which means that the outputs are a lot worse than they could be.

**Mariana Marins:** So, yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Let's definitely do that.

**Mariana Marins:** I want to codify that.

**Mariana Marins:** If I manage to understand, I can do, because then it's something that I can.

**Matthew Panzarino:** Take off everyone's plates, and then people are free to do what they have to do.

**Matthew Panzarino:** I would love for us to red team those, and get a process going, and divide and conquer, and just refresh everybody's artifacts.

**Matthew Panzarino:** Because the thing is, we can create new artifacts for them, and the old artifacts remain, right?

**Matthew Panzarino:** They can version back to the old ones if they want to, but they'll have new ones that we made, all of that stuff.

**Mariana Marins:** should update them frequently, right?

**Matthew Panzarino:** Which I also think it's something they are not doing.

**Matthew Panzarino:** I think they should be adjusted monthly, you know, because like the clients have been telling them stuff every week.

**Matthew Panzarino:** Okay, have they told you nothing new about their company in four weeks?

**Matthew Panzarino:** No new products, no new worries, no new concerns, no new existential threats.

**Matthew Panzarino:** Really?

**Matthew Panzarino:** You know, that's crazy, right?

**Mariana Marins:** And if you haven't, ask them those questions.

**Mariana Marins:** That's what I was going to say.

**Mariana Marins:** Maybe the matter is asking the correct questions, right?

**Matthew Panzarino:** Yeah, yeah, yeah, exactly.

**Matthew Panzarino:** All right, let me go jump to this Sucheta thing, and then...

**Matthew Panzarino:** I have a...

**Mariana Marins:** She told her that you are a bit late, but it's okay.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** Thank you.

**Mariana Marins:** Yeah, I'm going to go refresh my coffee and then go do that.

**Mariana Marins:** We'll catch up later then.

**Matthew Panzarino:** Okay, sounds good.

**Matthew Panzarino:** It looks like running the content quality score eval right now on this first one.

**Matthew Panzarino:** So let's follow up on that.

**Mariana Marins:** Let's run a few more through here and see what happens.

**Mariana Marins:** And then let's also check to see if the Airtable populates.

**Mariana Marins:** Ah, can you send the link?

**Matthew Panzarino:** I don't have the link to these in table, please.

**Matthew Panzarino:** Yeah, yeah, yeah.

**Matthew Panzarino:** Kirkland just made it ad hoc.

**Matthew Panzarino:** But I think it's shared with the whole org.

**Matthew Panzarino:** Let me, you should be able to access that.

**Matthew Panzarino:** If not, let me know.

**Matthew Panzarino:** Kirkland controls the keys, I think.

**Matthew Panzarino:** But I would love to see if this pipe actually drops it out there as it's supposed to.

**Mariana Marins:** So we'll see what happens.

**Matthew Panzarino:** All right, let me go refresh my coffee and then I'll jump over to that meeting.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Thanks.

**Mariana Marins:** Appreciate it.

**Mariana Marins:** Bye-bye.
