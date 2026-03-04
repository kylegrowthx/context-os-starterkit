# Atlas working session

<metadata>
date: 2025-06-18
time: 14:01 UTC
duration: 45 minutes
organizer: saskia@growthx.ai
participants: Carrie Chowske, Darrell Etherington, Ehtisham Hussain, Jenny Macrohon Dabon, Jürgen Linde, Jessica Nicole Manificiar Gayo, Josip Sovar, Matthew Alves-Hill, Saskia Wartnaby
fathom_recording_id: 69111307
fathom_url: https://fathom.video/calls/328432224
share_url: https://fathom.video/share/NSmZyjpnNwgh-ResVyFjqpwDxsWCZsxx
source: fathom
enriched_on: 2026-03-03 14:23 UTC
</metadata>

---

## Summary

GrowthX's Atlas content production platform launched with expected bugs and performance issues, but the team reported positive early results with output quality, particularly for external linking compared to the legacy Aerops system. The team discussed workflow adjustments including the critical role of the assignment direction field for controlling output, plans to reinstate editing and feedback capabilities, and pending improvements to internal linking, outline editing, and production/pre-production environment separation. Multiple content projects are transitioning to Atlas with ongoing client work for Zuplo, Yurko, Smith AI, and Good Call requiring careful management of word counts, custom workflows, and 1-on-1 follow-ups to align on assignments.

---

## Context

Atlas is GrowthX's new internal content production platform, launched to replace the legacy Aerops system. This meeting convened the delivery team shortly after Atlas went live to gather early feedback, identify blockers, and align on workflow changes. The meeting is led by Darrell Etherington (product) with heavy participation from Carrie Chowske, Saskia Wartnaby, and others who are actively using the platform on client projects including Zuplo, Yurko, Smith AI, and Good Call.

The context is a critical juncture: Atlas is functional but buggy, the team has pending client deliverables that depend on it, and the product team is rapidly iterating to resolve high-impact issues. The meeting surface both blockers (outline editing broken, internal linking missing, performance slow) and workarounds that teams have discovered (assignment direction field is powerful when properly formatted, rich text editor is now available). This is classic product-delivery tension — teams want to work, product is still building.

---

## Relevance

**To GrowthX Delivery:**
- Assignment direction field is a high-leverage workflow control that can enforce template structures and override keyword-driven defaults — teams should maximize its use, especially for clients with strict brand/format requirements (Zuplo, Yurko, Smith AI pattern)
- Word count inflation is a recurring issue requiring post-Atlas editing — Carrie flagged this as a blocker for Yurko (target 8-10 articles/week) and Smith AI; process must include external editing or Atlas hard-coding target overrides
- Outline editing is broken for most users and must be fixed before large content projects can rely on Atlas — currently blocks workflow control on longer-form content
- Internal linking is missing entirely; current workaround is adding links at the assignment brief stage, but this is not scalable for high-volume clients
- Markdown output formatting is cognitively harder to read than rich text; the rich text editor is live but buggy — continue pushing product for stability

**To GrowthX Business Development:**
- Atlas is in early-stage maturity with frequent breaking changes (production/pre-production environment still merged); clients should be prepared for workflow disruptions and extended timelines until stability improves
- Multiple active client projects are now on Atlas (Zuplo, Yurko, Smith AI, Good Call) and their success/failure will be visible in Q3 metrics — early wins matter for case studies and expansion

**To CheckThat/AEO:**
- Team uses multiple LLMs (Claude, GPT, Gemini) for different tasks; Perplexity AI platform mentioned as useful for model comparison — potential use case for CheckThat positioning around multi-model visibility

---

## Overview

- Atlas is buggy but expected; performance improvements and bug fixes are ongoing
- Internal linking and fact-checking steps need improvement; workarounds involve adding links in assignment brief stage
- Feedback column and editing capabilities to be reintroduced in future updates
- Airtable still used for project management; Atlas to eventually incorporate client-facing features

---

## Key Topics

### Atlas User Experience

  - Markdown formatting in output makes reading difficult; rich text editor introduced but still buggy
  - Assignment direction field crucial for controlling output; allows for template insertion and specific instructions
  - Performance issues noted; team working on improvements
  - Outline editing currently not functioning properly for most users

### Content Quality Comparison

  - Some users report better results from Atlas compared to Aerops, particularly for external linking
  - Others note missing features like image search/generation and internal linking
  - Word count tends to be high, requiring external editing

### Workflow Changes

  - Some custom steps (e.g., image generation for Smith AI) not carried over from Aerops
  - Style adaptation step removed due to issues with repetitive application
  - Editing/feedback step to be reintroduced

### LLM Usage and Preferences

  - Team members use various LLMs (Claude, GPT, Gemini) for different tasks
  - Perplexity AI noted as a useful platform for accessing multiple models
  - Discussion on personal preferences and biases in model selection

### Project Management

  - Airtable still used for tracking and client reporting
  - Atlas currently shows legacy content; users encouraged to archive completed items
  - Future state of Atlas to include client-facing surface with permissions

---

## Action Items

**Darrell Etherington (GrowthX)**
- File ticket - product improvement for hard-coding word count targets in Atlas

**Ehtisham Hussain (GrowthX)**
- Schedule 1-on-1s w/ Saskia & Jessica re Prophecy & Aftershooter Day planning

**Carrie Chowske (GrowthX)**
- Schedule 1-on-1 w/ Josip Sovar re Zuplo/Yurko/Good Call work assignments + Atlas transition
- Meet with Sadir (external) post-call re Yurko assignments. Determine 8-10 articles/week target. Prep for Josip Sovar
- Run Zuplo assignments by client contact. Prep for Josip Sovar post-approval
- Continue reviewing Yurko content. Prep feedback for Sadir/Josip Sovar

---

## Transcript
**Darrell Etherington:** For people feeling about this so far, Atlas, you know, buggy to be expected, they were working right up until go live.

**Darrell Etherington:** And it wasn't all there.

**Darrell Etherington:** Of course, close it up.

**Darrell Etherington:** Yeah, it's how software development works sometimes, especially in startups.

**Darrell Etherington:** Any thoughts, concerns?

**Carrie Chowske:** I think it's going to be a lot of playing with, like, that, like, like, in some cases, like, the initial input, like, but so far, the ones I've run are pretty good.

**Carrie Chowske:** I think it'll be easier to, like, see, too, once, like, you've got the, like, fix, so it's not all in markdown.

**Carrie Chowske:** I don't know why those damn hashtags make it harder for me to read something, but it does.

**Carrie Chowske:** It really does.

**Saskia Wartnaby:** It's, yeah.

**Saskia Wartnaby:** I know.

**Darrell Etherington:** I think my brain translates them, but it's because I have to spend a lot of time writing directly on markdown and escape.

**Darrell Etherington:** Actually, I will say.

**Carrie Chowske:** Probably not the hashtag so much, it's really when it gets into the links and stuff, and that's where I, like, my brain just goes, but it skips over it, and so, like, trying to figure out, you know, but it's not the end of the world, you know.

**Darrell Etherington:** No, but believe it or I mean, the context wasn't, like, there was, it was from a time when even CMSs or, like, user-facing editors, like, didn't exist in the web, right?

**Darrell Etherington:** So you were just writing cold into HTML, which was uglier still, right?

**Carrie Chowske:** You should have heard me in, Jen, when she was teaching me how to do Zublo, because they do all their, I have to post all their blogs in GitHub using Markdown, and she was talking about, like, how you have to create a folder, and then you have to go here, and you drop here, I'm like, oh, so it's, like, old school FTP, got it.

**Carrie Chowske:** Yeah, yeah, it is like that, yeah, yeah, you're building all the structure from scratch, instead of any of it being there, where I didn't, yeah.

**Carrie Chowske:** For sure, I just, you know, I thought we were beyond that, that's, like, that's where I'm, like, please, make me do this.

**Carrie Chowske:** I worked so hard to get there, I didn't have to do that anymore.

**Darrell Etherington:** Well, I'm,

**Darrell Etherington:** I'm surprised, like, I guess it was maybe an app's limitation, because once Kirkland was like, hey, I can ship a rich text editor, he moved pretty quickly, and he shipped that, like, I mean, within hours, basically, right?

**Darrell Etherington:** think it's still got some bugs, but pretty impressive.

**Darrell Etherington:** What doesn't have bugs?

**Carrie Chowske:** Yeah.

**Carrie Chowske:** I mean, yeah, everything does.

**Darrell Etherington:** Even iPhone.

**Darrell Etherington:** So many.

**Darrell Etherington:** Weren't we talking about Siri being awful the other day?

**Darrell Etherington:** Was that you and I that were talking about that?

**Carrie Chowske:** Like, it just doesn't work.

**Carrie Chowske:** We weren't, I have, feel, I feel that, I have shared that opinion.

**Darrell Etherington:** Yeah, it's a mess.

**Carrie Chowske:** But yeah, I found, like, I did find with, like, the refresher that, like, that one really relies heavily, if anybody's trying to use that one, it relies really heavily on what you put in that very first input.

**Carrie Chowske:** When you, when it, when you add the line, like, it brings up a very small field.

**Carrie Chowske:** You go back in, there's a lot more room, and you can, like, format it, and giving it a lot of guidance on that.

**Carrie Chowske:** And that's true.

**Carrie Chowske:** true.

**Carrie Chowske:** Through all of all of them, but like specifically the refresher, like that one really seems to help give it more.

**Carrie Chowske:** Like if you're wanting it to do very specific things, you can control that pretty well.

**Carrie Chowske:** Otherwise you get very generic, like, you know, it doesn't really look like it updated much.

**Carrie Chowske:** Yeah.

**Darrell Etherington:** Yeah, I did.

**Carrie Chowske:** I was able to like, and if you have like templated, like structures, things, you're able to like, like, I wouldn't say you can manipulate directly what you're going to get the brief in terms of like when it recommends a structure, but you can certainly make sure that all the right information is there by changing that same, that field.

**Carrie Chowske:** I forget what the field is called.

**Carrie Chowske:** Why is my brain not remembering?

**Carrie Chowske:** I know which one you're talking about because we were just talking about it in one of the.

**Carrie Chowske:** It's the one that's under when you like, when you're in looking at the thing individually, it's the thing that's under input.

**Carrie Chowske:** Like if you click where it says input, it goes to that, but that's very top.

**Darrell Etherington:** This thing is so slow.

**Carrie Chowske:** It is slow.

**Carrie Chowske:** Yeah.

**Darrell Etherington:** Yeah, they are, they are working on performance improvements as well.

**Darrell Etherington:** think I jumped into one of the idiosyncratic threads, of course, so that means it doesn't happen.

**Darrell Etherington:** Yeah, they're working on performance improvements constantly, too.

**Darrell Etherington:** It's it's direction, assignment direction.

**Darrell Etherington:** that's right.

**Darrell Etherington:** Assignment direction.

**Darrell Etherington:** yeah.

**Carrie Chowske:** As I was preparing to, like, handoff discern, I was setting up, because we have very, it's PSEO, and it's very templated, and I was able to, like, basically just put my original template from, like, Word in there as the direction, and it actually, like, was giving us pretty good results so far.

**Carrie Chowske:** Yeah.

**Darrell Etherington:** that is the, the specific intent of that is to be able to override whatever the, the keyword-based one is going to generate, because it'll generate its standard thing to try to rank, right?

**Darrell Etherington:** And that thing will say, no, no, no, I don't care what else you're seeing in the SERPs, like this.

**Darrell Etherington:** This is the type of format I want, so use this instead, right?

**Darrell Etherington:** It's a very useful field to have.

**Darrell Etherington:** very lucky out of that.

**Darrell Etherington:** And a future state goal is to put in a drop-down optionally for specific pipelines if you have a fixed number of schema or whatever, right?

**Darrell Etherington:** If you're like, we only want to do this for this client every single time, that'll be baked right into the pipeline, right?

**Darrell Etherington:** So if it's a comparo or if it's a listicle or if it's something like that, right?

**Darrell Etherington:** This is very weird.

**Carrie Chowske:** Anyway, the ones I put in yesterday are all gone now.

**Carrie Chowske:** Oh, they are all gone?

**Darrell Etherington:** Yeah, I don't...

**Darrell Etherington:** This is weird.

**Darrell Etherington:** So, like...

**Darrell Etherington:** Hold on, let me...

**Carrie Chowske:** I don't mean to be, like, dominating conversation here, guys.

**Carrie Chowske:** No, no.

**Carrie Chowske:** Go ahead.

**Carrie Chowske:** So, like, right, this here, I had, like, a whole thing in here.

**Carrie Chowske:** I don't know where it went.

**Carrie Chowske:** Like...

**Carrie Chowske:** And you can see where it...

**Carrie Chowske:** You can see I had it because it's here.

**Carrie Chowske:** It's just in this stupid HTML crap here, but...

**Carrie Chowske:** And I'll a diagram.

**Darrell Etherington:** Yeah, this is another part that we haven't resolved yet, but hopefully we'll resolve after this.

**Darrell Etherington:** I know Panson said that that assignment direction, he's still not, like, sure what goes in it and what it does yet.

**Saskia Wartnaby:** Okay, maybe that was, maybe they're doing something with it, I don't know.

**Carrie Chowske:** It worked for me, but, like, it gave it, because, like, I was giving it research direction, kind of, like, I think one example he gave was if you could, say, target this one specific persona, but he hadn't really tested it with anything else, so he said you can just, like, play around with it for now, but he needs to take into it a bit more, like, what it actually does.

**Saskia Wartnaby:** Which step is this at, Karen?

**Saskia Wartnaby:** Which step was that in the flip?

**Darrell Etherington:** Oh, it's the very, it's the very first one, so, like, this is, like, when you first go to add, like, a field, you'll get, you get that, but I, oh.

**Carrie Chowske:** It up, because you can, like, actually, oh, yeah, yeah, what, and then, like, if you do that, and then go into it, it actually let you, like, format it, which I think, again, going back to the formatting thing, helped my brain to, like, wrap my head around what I'm trying to do, and so, like, you can, it just lets you put it here, but I had stuff there, and it was, like, but I don't know what happened to it, so that's fun, and I have to, like, redo that.

**Carrie Chowske:** Yeah, that's probably, they probably have it somewhere, but they're probably, like, just, like, writing over versions.

**Darrell Etherington:** This is, that's what I was alluding to, like, one thing that the team knows we need, and that we haven't had before with Arabs, but that we will have with this, is a distinct prod and pre-prod environment, so, you know, once they're set, all this, this will all be fixed, and the values will be fixed, and whatever, and then when they're working on new things or changes, those will happen in a pre-prod environment that doesn't touch our actual production environment, and

**Darrell Etherington:** And they'll deploy them once it's safe to do so, right, as opposed to just writing over your stuff constantly all the time because they're building it live, right, on our production fluff.

**Darrell Etherington:** But right now, there was, because we only have one.

**Carrie Chowske:** I know, I know, Jenny, you ran one for Zooplo, did you say, that you had, that you said that you felt share ops was a better, gave you a better result?

**Jenny Macrohon Dabon:** Yeah, I compared the two articles and the one in our ops was more superior overall so far, but I also think it was because it's the edited version already, so.

**Jenny Macrohon Dabon:** Oh, I see.

**Jenny Macrohon Dabon:** I think the linking is better, the external linking.

**Jenny Macrohon Dabon:** Can I just, sorry, keep going.

**Jenny Macrohon Dabon:** Yeah, it's okay, yeah, go ahead.

**Josip Sovar:** I also did one for Zuclo today, and I also used to carry, like you said, that direction.

**Josip Sovar:** I told him I want a listicle article, and I want all the tools to have the same structure, have pros, cons, and use best for, etc.

**Josip Sovar:** So yeah, it did great.

**Josip Sovar:** In the outline, everything for every tool was the same for every tool.

**Josip Sovar:** And sometimes in Europe, it had to do that manually to structure it, but this was very great.

**Josip Sovar:** Yep, I think the article I had so far, the formatting was also better.

**Jenny Macrohon Dabon:** The external links, before it repeated the same external links again and again throughout the article, it didn't occur that much now.

**Jenny Macrohon Dabon:** I think we just, maybe it's in the prompts, because for now, we cannot edit the outline.

**Jenny Macrohon Dabon:** So maybe it has something to do with that.

**Jenny Macrohon Dabon:** It just, for me, it's just blank, like the one that was flagged yesterday during the meeting.

**Jenny Macrohon Dabon:** But yeah, those...

**Jenny Macrohon Dabon:** Your observation so far, just wanted to like, maybe for it to add more codes to improve the authority and all that.

**Jenny Macrohon Dabon:** But yeah, I also remember Joe flagged it yesterday where you were stuck in the internal link step.

**Jenny Macrohon Dabon:** And I had the same issue yesterday, but I just figured to add the internal link in the assignment brief stage.

**Jenny Macrohon Dabon:** So yeah, both the internal link and fact checking.

**Josip Sovar:** So yeah, we need to put links in that.

**Josip Sovar:** So there is no link in the, in the first person how it's called.

**Josip Sovar:** So yeah, it won't, it won't give us a fact checking internal link.

**Jenny Macrohon Dabon:** So yeah, we need to put that link there.

**Josip Sovar:** Yep.

**Josip Sovar:** This, yeah, right now, it's not even loaded for me.

**Darrell Etherington:** So that's a problem.

**Darrell Etherington:** I'm just going to blue bar never complete on Zoopla.

**Darrell Etherington:** So I was going go and check, but another problem.

**Darrell Etherington:** Um, yeah, and are those things both, uh, I mean, do you feel like they are, like, linear ticket worthy, or is it just, like, a qualitative thing, or have you filed already linear tickets on it?

**Darrell Etherington:** Because they're also, like, I would err on the side of more rather than less, because they're consolidating on the back end if they have duplicative tickets and stuff, right?

**Darrell Etherington:** So don't be ashamed, or don't be afraid to have something.

**Darrell Etherington:** Daniel, Daniel responded to me yesterday.

**Josip Sovar:** He said that that's a broader problem, and it's quite common, so then they will fix it.

**Josip Sovar:** So she, he just placed mine as a result.

**Josip Sovar:** Okay.

**Darrell Etherington:** Yeah, Len and Joe filed ticket at this point.

**Darrell Etherington:** That's what they asked for, so don't be shy about.

**Ehtisham Hussain:** Yeah, filed one, I filed one yesterday, uh, and they filed it under duplicate, uh, because, uh, I was getting an outline in the raw form, but I couldn't edit it.

**Ehtisham Hussain:** Check

**Ehtisham Hussain:** And the field, the rich text editor field at the output stage was empty, but it was allowing me to move forward and move forward with the article.

**Ehtisham Hussain:** I had, I would just quickly summarize my experience with Atlas so far.

**Ehtisham Hussain:** I generated the same articles through Aeroops on Friday, and I forgot to save it somewhere.

**Ehtisham Hussain:** So I completely, I lost it like on Monday, and I had to use Atlas to generate the exact same article.

**Ehtisham Hussain:** That was for Smith AI.

**Ehtisham Hussain:** In the workflow, think, Elvis had another step in there, Aeroops, where the AI, I don't know what technology was being used at that step, but it searched for relevant images and then it recommended relevant images to be included in the article.

**Ehtisham Hussain:** But I didn't see that in Atlas.

**Ehtisham Hussain:** So I don't think that step at least.

**Ehtisham Hussain:** It's not there for smith.ai.

**Ehtisham Hussain:** The other thing is internal linking didn't work very well even though it took me through the step and it produced an output and it allowed me to get from internal linking to the next step but internal linking in aerobs was actually placing some seriously good internal links throughout the article and in this version I didn't even see like one internal link that was then the workflow placed in there.

**Ehtisham Hussain:** I placed it later on.

**Ehtisham Hussain:** So, and the total word count because I was unable to go and edit the outline the total word count was still pretty much on the heavy side with Atlas as well.

**Ehtisham Hussain:** So, overall I think with aerobs I think because Elvis had gone in there and he had done some serious customization of his own results were a little bit better and in this case I think a couple of steps were missing a couple of steps.

**Ehtisham Hussain:** steps were not working.

**Ehtisham Hussain:** The final

**Ehtisham Hussain:** The output was very similar to what I got from Aerox, but it didn't have images, didn't have internal links, and yet to shorten it, I have to go out of the system and use Gemini.

**Ehtisham Hussain:** That could be a feature request too, I think.

**Ehtisham Hussain:** At the end, there was an editing step as well in Aerox, where you could go in and you could, with four forward-facing slashes, you could put in an incredible amount of editing instructions in there.

**Ehtisham Hussain:** I don't think that's there in Atlas 2.

**Ehtisham Hussain:** Oh, interesting.

**Ehtisham Hussain:** I think they said that they're working on it, and they will give us something like a feedback column.

**Ehtisham Hussain:** Yeah, there should be, at least before the final draft or even after the final draft, there should be a step where we can go in with custom editing instructions.

**Ehtisham Hussain:** Yeah, you're right, because I was assuming that that was included.

**Darrell Etherington:** Isn't that a style adaptation?

**Saskia Wartnaby:** So, no.

**Saskia Wartnaby:** What was it like as of right now, that's not what the style adaptation does.

**Darrell Etherington:** And the style adaptation is there was a thread on this, too, because what it was doing was like basically reapplying the writing, writing, writing.

**Darrell Etherington:** Yeah, yeah, the writing guidelines.

**Darrell Etherington:** And it was introducing a lot of like, it's the thing where, like, once you start applying things over and over again, LLMs, you get very wonky results, right?

**Darrell Etherington:** Like, so, drift, basically.

**Darrell Etherington:** So, they eliminated that, I think.

**Darrell Etherington:** I think they went back and changed it to the default is not, like, it will not do that.

**Darrell Etherington:** In the old, in the air ops version of this, this step also did a bunch of SEO stuff, but I don't think it does that anymore.

**Darrell Etherington:** So, I think they might just be the process of eliminating it altogether from the flows and then adding back in that edits or feedback.

**Darrell Etherington:** Jack.

**Darrell Etherington:** you.

**Darrell Etherington:** Part.

**Darrell Etherington:** The internal linking I've heard consistently throughout that that is a problem.

**Darrell Etherington:** They are aware of that too.

**Darrell Etherington:** That one is interesting to me because I wonder if they've changed the stack.

**Darrell Etherington:** Because in theory, it shouldn't be any worse in terms of what models are falling underneath of it.

**Darrell Etherington:** But it clearly is.

**Darrell Etherington:** And then just on the Smith-A-A-S specifically, can still use, Aerofs has not actually technically cut off our access.

**Darrell Etherington:** So you can log into it.

**Darrell Etherington:** It didn't let me.

**Darrell Etherington:** It wouldn't let me.

**Saskia Wartnaby:** It wouldn't let me, Oh, it's letting me for some reason.

**Josip Sovar:** Yeah, in a meet with CMS and Panzer yesterday, he said that maybe a day or two and everybody will be cut off.

**Josip Sovar:** But for now, only like 20 people still have access to it.

**Josip Sovar:** Oh, well, I can find that article if you want to know which math it is.

**Darrell Etherington:** I'm happy.

**Darrell Etherington:** So, like, I'm halfway through it, anyway.

**Darrell Etherington:** Okay.

**Darrell Etherington:** Yeah, and on your point on the thing about the, like, which flows are reflected or which pipelines are brought over and which steps, like the image part, if you haven't, I would file a ticket about that because they are bringing over custom flows piecemeal.

**Darrell Etherington:** They just did one for us for Good Call that brought in, and they actually, like, replaced the auto-publishing stuff because they had to hard code a new tool, but they did that after I flagged it for them as an important thing, right?

**Darrell Etherington:** So, is that something specific to SmithAI or do all workflows have to have that step where?

**Ehtisham Hussain:** No, that one is specific.

**Ehtisham Hussain:** The image generation stuff is not universal.

**Darrell Etherington:** They used to have a, they had a set number of flows that they would introduce to grids depending on need.

**Darrell Etherington:** They built some image search or image generation flows, but some of them are really bespoke and specific to the content if they have different requirements that are about brand guidelines and brand kit and stuff like that.

**Darrell Etherington:** So I would just say, you know, we want this replicated exactly as it represented, including the image refresher or whatever else.

**Darrell Etherington:** And then they can bring that one up or update it, because in a lot of the cases, they were just like, well, we're going to grab the one that seems to be used the most or the one that's marked ideal path, but they didn't grab all of them.

**Darrell Etherington:** Right.

**Darrell Etherington:** So I'll talk to Elvis about it.

**Darrell Etherington:** Maybe he's already filed a ticket.

**Darrell Etherington:** Yeah.

**Ehtisham Hussain:** Because this is the last thing I'm doing for SMIT AI for now.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** Yeah.

**Darrell Etherington:** So I guess it won't matter after that.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** mean, I think we got to.

**Darrell Etherington:** We've got to address the like thing.

**Darrell Etherington:** Since it's consistently such an error, like, we have all those best practice workarounds that we have, too.

**Darrell Etherington:** So I think there's a discussion to be had with Eng about, like, you should hard code this as a step.

**Darrell Etherington:** Like, it shouldn't be a thing that we just repeatedly manually type into the thing.

**Darrell Etherington:** We all know, like, I mean, generally speaking, it seems like the ideal targets are roughly the same, right?

**Darrell Etherington:** Like, 1,500, 2,000 words or whatever it's being.

**Darrell Etherington:** then, so if we could know that we, if we know we're always going to get 5,000 and we need to cut back 50%, we should be able to hard code that into the tool so that we'll get those results and then take that, oh, should we need any specific one-off unique cases?

**Darrell Etherington:** I think that's good feedback.

**Darrell Etherington:** That'll be like an overall product improvement thing rather than like a bug fix.

**Darrell Etherington:** But I can follow the ticket about that.

**Darrell Etherington:** Were any of you able to edit the outline?

**Josip Sovar:** Today I edited the conclusion on my end because mine was missing a conclusion.

**Josip Sovar:** I had frequently asked questions, nothing else.

**Josip Sovar:** So I added the conclusion, but I used GPT for it.

**Josip Sovar:** I think that's okay.

**Josip Sovar:** I gave my whole outline to chat GPT and told him to give me just the conclusion for that part.

**Josip Sovar:** So he gave me three bullet points to mention in the conclusion.

**Saskia Wartnaby:** I know Panza said they are looking at adding like a tool where it will pop up like a window to interact with an LLM to do that in the workflow.

**Saskia Wartnaby:** So hopefully that will be nice and you can do that inside it.

**Saskia Wartnaby:** But obviously that's going to take a while to come.

**Saskia Wartnaby:** So for now you probably will have to do that.

**Darrell Etherington:** But yeah, that's a chat we've had a lot about that when we were doing the workflow.

**Darrell Etherington:** I'm I'm going to

**Darrell Etherington:** One of the problems with this from like a UX perspective is, I mean, there's a reason why the consumer LLM tools designed that and have settled on the chat-based interface that is like, allows for back and forth and is like an open dialogue.

**Darrell Etherington:** Like, it's just a more effective way to manipulate these tools, right?

**Darrell Etherington:** So it's weird that we don't have that and we have like a linear, unidirectional step and we don't have any point at which you can, just prompt the dialogue, you know, chat interface with natural language like you would expect to be able to do.

**Darrell Etherington:** So, yeah, they are working on adding that in.

**Darrell Etherington:** Yeah, I'm just trying to find, you know, the length generated that I've done.

**Darrell Etherington:** Let's see if I can manipulate it, because I think that's still an artifact of the switch over to the plain text editor.

**Darrell Etherington:** Like, I think that is a bug that is actually being worked on, but I don't know that it's resolved anywhere.

**Darrell Etherington:** So, Yeah.

**Darrell Etherington:** Anything else?

**Darrell Etherington:** mean, the big thing is just like, do people feel like it's so far off that it's not even going to work?

**Darrell Etherington:** You know, and if you feel that, but I think they should have, they should have like included a feedback column.

**Matthew Alves-Hill:** Oh, yeah.

**Matthew Alves-Hill:** In these stages.

**Matthew Alves-Hill:** Yeah.

**Darrell Etherington:** Sorry, I think maybe I missed that.

**Matthew Alves-Hill:** Yeah, they're working on putting one in.

**Matthew Alves-Hill:** They just, they, I don't know why it didn't get carried over, but for some reason it wasn't included, but they are introducing that back.

**Darrell Etherington:** And then the other thing was they're going to take out the reapplication of the style because it was duplicative and weird and making things strange.

**Darrell Etherington:** Yeah.

**Matthew Alves-Hill:** I, um, I loaded in, like, I did a massive edit.

**Matthew Alves-Hill:** edit.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** on an article brief or assignment brief this morning, again, using, I actually used Cologne, not GPT, but after I did that, I plugged it back in, and I seem to have just like broken the entire BAPI.

**Matthew Alves-Hill:** Oh, really?

**Matthew Alves-Hill:** Yeah, so I've raised, I've raised, initially it was just one, on that specific article, then I tried to create a draft, and it just wouldn't, wouldn't like move to the next step, but now it's the other articles too, so I've raised a ticket, but I don't know if it was something, maybe new.

**Matthew Alves-Hill:** It probably wasn't you, it probably was just coincidental versus causal, in this case, because it's chugging a lot at the moment.

**Matthew Alves-Hill:** But yeah, that was my first like big, um, edit, and I actually, I ran it without, um, the article direction, because I wanted to see, I, Daryl, I lifted like the unstructured.

**Matthew Alves-Hill:** Writing guidelines that you mocked up for in Aerobs, I lifted them, used, applied to BAPI, and I was actually chatting with Usman earlier and comparing, like, his writing guidelines for Strapi to ones in BAPI, because he was, he was saying, I really want a feedback column.

**Matthew Alves-Hill:** And I think, like, the, basically, the, those writing guidelines that you provided for Unstructured, they're, like, much more in-depth.

**Matthew Alves-Hill:** So, seems to be working better by, like, prompting up front versus, um, Usman's now generating, so I'm interested to see what his, what, what he'll get out of it, because Strapi's writing guidelines that don't have examples, and they're a little bit, like, um, less fleshed out.

**Matthew Alves-Hill:** So, I'm going to check in with him, and I'll see what he finds.

**Darrell Etherington:** Yeah, and that, so those are the, I've done this for a few clients now, but, like, the way that I.

**Darrell Etherington:** We talked with Kirkland about there used to be a concern that that would be too much, that it would choke on the LLM side, but he says because of the way they do chunking now, that's actually no longer a concern, and that's what we've been finding, so, yeah.

**Carrie Chowske:** I'm going to tell everybody my favorite shortcut for going to another, like, chat thing, and actually use different LLMs, this perplexity lets you pick which one you're using, so you don't have to hop back and forth between GBT.

**Carrie Chowske:** I just do that all the time, because I get sick of switching platforms between, like, all the different tools we use, which drives me crazy.

**Carrie Chowske:** So, I just, like, when I want to use Claude, I just use it in perplexity and stuff like that.

**Darrell Etherington:** Perplexity does tune, though, so it is different.

**Darrell Etherington:** Now, I think it's a totally qualitative measure of whether that's good or bad, but there is a layer of post-tuning that, like, perplexity does on those modes.

**Darrell Etherington:** But, yeah, it's...

**Darrell Etherington:** I love them because they're all, I wrote a newsletter about it, but I love that the personality is such a core ingredient in all of these things.

**Darrell Etherington:** Because then it's like, ooh, who's your favorite weird AI character in the movie or whatever?

**Darrell Etherington:** I could also be biased.

**Carrie Chowske:** Ehtisham and I actually both wrote a bunch of content for Perplexity when they launched their DeepSeek R1 integration.

**Carrie Chowske:** So then I got to know their whole platform really well.

**Carrie Chowske:** It's totally personal bias.

**Darrell Etherington:** And it's just like, what did you start with it?

**Darrell Etherington:** What are you used to?

**Darrell Etherington:** Yeah.

**Darrell Etherington:** And then I really try to like examine those priors when I'm doing it because I'm like, that information is out of date so quickly, depending, like based on how they put their, or tune their things or do their releases.

**Darrell Etherington:** So like, Claude, I used to be like religious on Claude for writing.

**Darrell Etherington:** And I still mostly, I can still mostly my preferred, but like some of the more recent Chachupiti models do interesting things.

**Darrell Etherington:** What's the one they released?

**Darrell Etherington:** That was, like, almost entirely focused on creative writing, but it also hallucinates a bunch.

**Darrell Etherington:** It's, like, very creative and expressive.

**Darrell Etherington:** It might have been 4.1, but, like, If you were right for me, I think, or something like that, that is called right for me.

**Josip Sovar:** I think it's called integrity.

**Darrell Etherington:** Yeah.

**Carrie Chowske:** I don't know if anybody else has tried this either, but me being, again, hating to switch platforms, I've tried playing with Gemini, like, directly in Google Docs.

**Carrie Chowske:** And it's really good for sometimes, like, when you want to tighten something up or, like, shorten it really quickly and just you want it to summarize because there's a really big, long paragraph that might be repetitive.

**Carrie Chowske:** It does a really good, like, I would say a good 8 out of 10 times I get something pretty directly usable and I don't have to, like, go and redo an entire, you know, just think.

**Carrie Chowske:** I don't want to say I want to think about it because I do, but, like, it takes a little extra step out of it for me.

**Carrie Chowske:** Yeah.

**Darrell Etherington:** Yeah, Gemini is really good, and it was like a dark horse because for a while it was kind of laggard, and then...

**Darrell Etherington:** Now they might have the best models out there, actually.

**Darrell Etherington:** They just released new, updated versions of them earlier this week.

**Darrell Etherington:** And if they pull an ad, they win, basically, because of what you're talking about.

**Darrell Etherington:** The fact that it's already present in the tools where you're using it, no brainer.

**Darrell Etherington:** It's certainly going be me to adopt it when I probably wouldn't have gone and tried it separately before.

**Carrie Chowske:** Do you know what I mean?

**Carrie Chowske:** Not that I'm their target.

**Carrie Chowske:** Maybe I am their target audience.

**Carrie Chowske:** The laziest person alive.

**Carrie Chowske:** have no idea.

**Saskia Wartnaby:** Oh, 4.5 is the one that I'm talking about for PSGPT.

**Saskia Wartnaby:** Yeah.

**Saskia Wartnaby:** Which LLM you guys using the most, or do you rely on the most, or do you kind of use different ones for different things?

**Saskia Wartnaby:** Well, I do use different ones for different things, but that's what I was just saying.

**Carrie Chowske:** I do it with perplexity, because it lets you see which model you want it to use.

**Carrie Chowske:** Or you can say, use the best one, and they'll, you know, kind of, based on what you're querying, like, give you either, I don't even, to be honest, like.

**Carrie Chowske:** Back end of that, I don't know much about, but my guess is it's either like doing a combo of like, you know, because you can see it's like thinking tokens or whatever when it does the thing.

**Carrie Chowske:** But when it does the thing, Carrie, geez, really technical.

**Carrie Chowske:** But you can tell like what it's doing and I think it's probably like determining based on the type of query and then also maybe cross-referencing thing.

**Carrie Chowske:** But I like it because I can say like if I'm looking for it to like rewrite something, I'm going to be like, well, use Claude.

**Carrie Chowske:** I'm, you know, trying to, you know, get it to like reason for me, I might choose like their reasoning mode or do something else.

**Carrie Chowske:** So, yeah.

**Saskia Wartnaby:** But so the answer is I use one platform, but I am also within that.

**Saskia Wartnaby:** Yeah.

**Saskia Wartnaby:** Thank you for that.

**Darrell Etherington:** Yeah, yeah, I'm similar.

**Darrell Etherington:** just, I pop around between them, but I think this is also just like a.

**Darrell Etherington:** A human thing, which I, it's always good to, first principles are question your product or whatever, because I don't use perplexity as much only because I hit it real early in its life cycle.

**Darrell Etherington:** And I was like, I don't love these results.

**Darrell Etherington:** And then that colored it.

**Darrell Etherington:** This is when I first launched.

**Darrell Etherington:** It's silly.

**Darrell Etherington:** It has nothing to do with product count.

**Darrell Etherington:** But I think, like, I think from a business perspective and from a strategy perspective, like Ironman and the whole company is very smart.

**Darrell Etherington:** And I think what they're doing is very interesting and unique from a lot of the other players.

**Darrell Etherington:** But it just meant that, you know, I got stuck or sticky in Claude first.

**Darrell Etherington:** Claude, again, not really about product, but more about company approach and company values.

**Darrell Etherington:** And then I think, but I think that's also reflected in product, especially with these things.

**Darrell Etherington:** So the fact that the founding brother-sister team there are very cautious and considerate.

**Darrell Etherington:** Not necessarily, like, super accelerationist, like in a Sam Altman way, made me have affinity for that product, and then I think it's reflective in its output, right?

**Darrell Etherington:** It's, like, reasonable, and, like, someone had a really good characterization of them that was just, like, here's their attitudes, and that one was, like, oh, that actually just has the most affinity for me.

**Darrell Etherington:** It's, like, somewhat risk-averse, and, like, you know, it's, like, oh, okay, like, there's just mirrors, and I'm picking the one that's mirror, which is telling.

**Darrell Etherington:** I we aren't a human, but, you know, how these things work.

**Saskia Wartnaby:** Love it.

**Darrell Etherington:** And I think, mean, eventually, I am very hopeful that we will have more in the way of, like, model selection as an accessible variable for us in these pipelines, because that would be good, depending on the type of content that we want to produce, right?

**Darrell Etherington:** If we're doing a whole bunch of coding tutorials.

**Darrell Etherington:** It would be different than if we wanted to do general purpose information blog for non-technical audience or whatever.

**Darrell Etherington:** Yeah, I'm right now still having trouble getting into Filet Loads, doing the blue bar, not all the way.

**Darrell Etherington:** It's early on the West Coast, they're just getting up.

**Darrell Etherington:** But yeah, we don't need to take this whole time.

**Darrell Etherington:** just want to make sure we have some time to talk about it and poke around.

**Darrell Etherington:** And yeah, otherwise, obviously, everybody can continue doing that and can continue surfacing feedback however they wish.

**Darrell Etherington:** And then we will figure out how to wrap that to engineering.

**Darrell Etherington:** But big ones, please, please raise your hand if you're like, I'm in a production or like back or whatever, and I'm not able to do it.

**Darrell Etherington:** That's the most important stuff, right?

**Darrell Etherington:** So those those they will.

**Darrell Etherington:** It's right away.

**Darrell Etherington:** Like, I had highlighted the good call one.

**Darrell Etherington:** It's like, well, we need to publish.

**Darrell Etherington:** And they were like, okay.

**Darrell Etherington:** And they fixed it within, you know, 16 hours or whatever it was.

**Darrell Etherington:** So they will move quickly if we need to move quickly.

**Darrell Etherington:** Otherwise, I'll everybody go a little bit early.

**Darrell Etherington:** Have fun.

**Darrell Etherington:** Play with this stuff.

**Darrell Etherington:** Break it.

**Darrell Etherington:** My grid, my grid just got fixed.

**Darrell Etherington:** So that was prescient.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** We're back on.

**Josip Sovar:** Can I just ask one question regarding Atlas?

**Josip Sovar:** Yeah.

**Josip Sovar:** So what's with the Airtable and Atlas?

**Josip Sovar:** I'm not sure is there any use for Airtable anymore?

**Josip Sovar:** Because for me personally, I had their article title and everything I needed.

**Josip Sovar:** In Atlas, it's kind of weird for me personally.

**Josip Sovar:** I don't know if all the articles that are listed there are there for the generating.

**Josip Sovar:** Because in Airtable, we always had this week, I, for example, have 10 articles to generate.

**Josip Sovar:** And I knew.

**Josip Sovar:** Which one articles I had to generate, but in Atlas, there are 50 articles there, so I don't know which one to focus on that week, if that makes sense.

**Josip Sovar:** Oh, yeah.

**Josip Sovar:** does.

**Josip Sovar:** Oh, go ahead, Carrie.

**Darrell Etherington:** The art table is just like a tracking.

**Darrell Etherington:** Yeah, yeah, yeah.

**Carrie Chowske:** I was going to say, I was going to clarify first that you meant air cable or air ops, because air ops is what we use to generate the articles with, yeah.

**Carrie Chowske:** And just, we are still using air table.

**Carrie Chowske:** just wanted to make sure that we were like, yeah, yeah, making sure you meant air ops, which I think you did.

**Carrie Chowske:** I do that all the time.

**Carrie Chowske:** It's the only reason I caught that.

**Carrie Chowske:** was like, oh, no.

**Carrie Chowske:** But yeah, so we're just, yeah.

**Carrie Chowske:** I think right now, what you're seeing in Atlas, what I get the impression of, because I know this is what it is in Zooplo, is articles we've already generated in air ops.

**Carrie Chowske:** So they were testing that out and moving stuff over, and so we probably can archive pretty much most of what's there, so that we're starting fresh.

**Carrie Chowske:** Yes.

**Darrell Etherington:** Actually, that's a good point on just process, because remember in the Atlas training, Daniel asked that we do archive.

**Darrell Etherington:** Right now you're seeing a bunch of legacy stuff that they probably

**Darrell Etherington:** We brought over bulk just to run through the flows and see how they were doing when they were doing the standup.

**Darrell Etherington:** So you can take anything already completed and you can go ahead and archive them right now and they'll move to that other tab if you want to clean up your grid.

**Darrell Etherington:** But yes, the Airtable for us is a project management tool to see where we're at with this stuff and then also to report back to the client where we're at with this stuff.

**Darrell Etherington:** Like that's where the that's why we call it the content OS, like it's their operating system for getting a bird's eye view of what's going on with the various parts of their are deliverables and what's just there.

**Darrell Etherington:** And it's also extremely useful for me and for leadership to get that kind of like snapshot.

**Josip Sovar:** So we still use the information from Airtable, like keyword and the article title to generate our articles in Atlas.

**Darrell Etherington:** Yeah, yeah, yeah, but it's just a repository of information.

**Darrell Etherington:** I wish they were more connected.

**Darrell Etherington:** In a more automated way.

**Darrell Etherington:** They are not, unfortunately.

**Darrell Etherington:** But the nice thing is the future state of the Atlas is that Atlas will also contain that.

**Darrell Etherington:** Again, this is like a, they need to work and build and this will take quite a while, month, if not a year.

**Darrell Etherington:** But they want to have all of the client facing surface be in Atlas as well, a permissioned environment, right?

**Darrell Etherington:** So you can only access part of it depending on what your view of permissions are.

**Darrell Etherington:** So you will have access to the full production pipeline, but then the outputs will live over in this more sanitized client facing surface so they can review work being done and work to come, right?

**Darrell Etherington:** But it'll be linked.

**Carrie Chowske:** In terms of like, day-to-day production to Joe for like, working, working with like, I will assign things to you in Airtable and then you can go generate them in Atlas.

**Carrie Chowske:** And so you'll know, like, it'll be assigned to you so you can filter it and go, oh, these are all the things I have to, I have to look.

**Carrie Chowske:** So we'll go over that, too.

**Carrie Chowske:** Like, I'm so sorry that I missed the meeting yesterday, because I would have been like, hey, by the way, hello, hi, I'm going to be your managing editor, but, yeah, well, I stay really organized, because if I don't, I'll forget things.

**Carrie Chowske:** So you will never have to question, like, what you're supposed to be working on.

**Carrie Chowske:** I will make sure that you will know that.

**Carrie Chowske:** that's perfect.

**Carrie Chowske:** That's perfect.

**Josip Sovar:** Thank you, because it's much easier for me to know this week I had to do this, and I know what to do.

**Josip Sovar:** Yeah, for sure.

**Darrell Etherington:** Okay, actually, I mean, Carrie, since we have a little bit more time, oh, and Adisham, like, do you want to talk more about that, because we didn't get into too much of that, about how you work and how you like to work with your teams on kick-up call, and we can do that right now, if you want.

**Darrell Etherington:** Yeah.

**Ehtisham Hussain:** Yeah, so I'm going to set up meetings with Saskia and Jessica, too, hopefully, like, I'm just going to get, like, completely organized about the two songs, Prophecy and Aftershooter Day, and then tomorrow we can have one-on-one, hopefully, and we can plan out for, we'll go forward.

**Ehtisham Hussain:** Yeah, I'm kind of, I'm kind of in the same boat.

**Carrie Chowske:** Like I'm pretty, um, I'm, Zuplo is going to be like, I don't know, everything's such in a, like a transitional state, so it's kind of difficult, but I'm most familiar with Zuplo, then, then Yuriko, and then Good Call, which I think, um, Good Call is the one that Juergen and Matthew are helping us on.

**Carrie Chowske:** Is that right?

**Carrie Chowske:** Okay.

**Carrie Chowske:** Um, so I think we'll have plenty, like, there'll be, there'll be plenty to do, but I just don't have that ready to go yet, because I've got to still figure out, um, what are the next steps with, like, Zuplo and their, when we're changing, like, what we're, our deliverables are for them.

**Carrie Chowske:** Um, I don't know when that change is happening.

**Carrie Chowske:** But anyway, my point being that I try to, like, communicate as much as I can.

**Carrie Chowske:** I'll set up a one-to-one with you, Joe.

**Carrie Chowske:** So, uh, and I missed ours yesterday, because I was running late all day.

**Carrie Chowske:** But, um, we, I, I also will, you know, um, message you on Slack and stuff, too, occasionally.

**Carrie Chowske:** But, um, in general, I try to keep what.

**Carrie Chowske:** You're working on in Airtable, which eventually I think we'll be using linear a lot more, Darrell, is that the plan?

**Carrie Chowske:** I think that is the plan for specific tasks and projects, but we'll still have the content to list in Airtable, so another surface.

**Darrell Etherington:** I would get comfortable there for no other reason than, like I'm somewhat allergic to it too, but it is designed to how engineers think, and it's very useful to understand that kind of ticketing system, especially if you're going to be working in tech while there.

**Darrell Etherington:** Yeah, no, I didn't, I just, it's very exciting for that.

**Carrie Chowske:** Go ahead, Joe, sorry.

**Josip Sovar:** What are my expectations for this week?

**Josip Sovar:** Do I need to generate any number of articles for Zoopla or for Yurko?

**Josip Sovar:** Let me look.

**Carrie Chowske:** Yurko will need, I believe they do, like, we're doing like eight to ten a week for them, and I'm going to get with, I'm meeting with Sadir right after this, and I will find out and I will have more information for you.

**Carrie Chowske:** Right now I've got to run assignments.

**Carrie Chowske:** By our contact at Zuclo, but once I do that, I can probably have some things for you to work on.

**Carrie Chowske:** And then I think Good Call is more up in the air at this point, but we'll start there.

**Carrie Chowske:** Like, I think Yurko might be a good place to start, know, because it's more straightforward, I think, than the other two at the moment.

**Darrell Etherington:** Sorry, Darrell, go ahead.

**Darrell Etherington:** Oh, I just, I think that one's in good shape, like, because Sidira, I think, has been acting under the impression that she is still hailing up for this week.

**Darrell Etherington:** But, yeah, Carrie will know more after that, for like, that's for Yurko specifically.

**Darrell Etherington:** For Good Call, I would like to get us to produce at least some, because we are in a deficit, and that will help with Bob, the stakeholder, when we meet with him tomorrow.

**Darrell Etherington:** But Marcel is also trying to get time on his books.

**Darrell Etherington:** He just put another buzz to get there, so that will hopefully.

**Darrell Etherington:** Help, because there's some additional stage setting to be done there.

**Darrell Etherington:** But if we can get producing and carry, you know, about the area code stuff, if we can find a way to replicate that in Atlas and at least start putting out like one or two test articles that represent or that show that we can do that, that would be ideal.

**Darrell Etherington:** Okay.

**Carrie Chowske:** You're talking about the one, the grid that Martha was using right before we...

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Okay.

**Darrell Etherington:** But if we, even if, even if we can't use that grid, like even if we have to use just a generic grid and see if we can use the assignment direction to mimic that format or something, then, you know, we can do that.

**Darrell Etherington:** But should have ported that over.

**Darrell Etherington:** They should be in the process of porting that over because that ticket is being worked on.

**Darrell Etherington:** I know Daniel and Kirkland are going back and forth on the, just the publishing step, but it was specific to that.

**Darrell Etherington:** I'll keep an eye on it.

**Darrell Etherington:** Yeah.

**Carrie Chowske:** But yeah, I can probably give you some stuff with Yerko so you can keep experimenting a little bit with Atlas and making sure that We're getting what we want because we're actually, I found out from yesterday from Cedera.

**Carrie Chowske:** Ahead on your code, but only because the way that they, it's to give their, to give our point of context, time to review, so we're not really ahead, but anyway, but we did not really fully pause publishing for her there, so.

**Josip Sovar:** Yeah, I chatted with Zadira for a brief moment yesterday, and she told me that she can revise the first batch of articles for first week once I start, so that we know are we on the right path or not.

**Josip Sovar:** Right, yeah, and I've been reviewing some content for her all day, too, so I've got a pretty good handle on it.

**Carrie Chowske:** You know, we're in the middle of two of kind of revisiting their strategy a little bit also, which is part of why I allegedly were plotting this week, so I'm trying to figure out where to, so anyway, I've got to meet with Zadira and find out more, and then I'll have even more information for you, but I'm glad you talked to her because she's on top of things, and she has way more information about your co at this point than I do, because I had just taken on, you know, from her a couple weeks ago, so.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Okay.

**Darrell Etherington:** All right.

**Darrell Etherington:** Cool.

**Darrell Etherington:** Well, yeah, let's call it here then and get to work on this stuff, and we'll have more updates to come.

**Darrell Etherington:** have, yeah, iCall with Yorko is later today to Joe, so I'm sure we'll have updates out of that.

**Darrell Etherington:** It's just in a little bit.

**Darrell Etherington:** Cool.

**Darrell Etherington:** Take care, everybody.

**Darrell Etherington:** Bye.

**Darrell Etherington:** Bye.

**Darrell Etherington:** Bye.
