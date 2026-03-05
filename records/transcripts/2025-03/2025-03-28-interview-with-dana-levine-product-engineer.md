# Interview with Dana Levine - Product Engineer

<metadata>
date: 2025-03-28
time: 17:01 UTC
duration: 135 minutes
organizer: Daniel Lopes
participants: Dana Levine, Daniel Lopes
fathom_recording_id: 54425149
fathom_url: https://fathom.video/calls/263323237
share_url: https://fathom.video/share/gEhXJXsso9LGgqs5xveYkHoo8Qoin3fz
source: fathom
enriched_on: 2026-03-04 12:45 UTC
</metadata>

---

## Summary

Daniel Lopes conducted a technical interview with Dana Levine for a Product Engineer role, including a practical coding exercise to build an article processing pipeline with summarization, translation, and fact-checking capabilities. Dana demonstrated strong product instincts and engineering experience building developer tools, completing the exercise while Daniel discussed GrowthX's scaling challenges, internal workflow infrastructure, and vision for AI-powered content automation. The interview concluded with Daniel indicating he would prepare an offer pending Dana providing professional references, with a follow-up discussion planned for the following week.

---

## Context

Daniel Lopes, VP of Product/Engineering at GrowthX, interviewed Dana Levine, an experienced product engineer with a background in building developer tools, for a senior engineering role. GrowthX is a B2B content marketing services company ($200k+ engagements) that has built proprietary AI-powered infrastructure for scaling content creation workflows. The company is currently growing to approximately 60 people on the services team with $22M revenue targets, but faces pressing challenges in automation, training, and operational efficiency as they scale. Dana's combination of product thinking, engineering rigor, and hands-on experience with developer tooling aligns with GrowthX's critical need for engineers who can operate close to the business, understand customer workflows, and help automate the services delivery process.

---

## Relevance

**To GrowthX Delivery & Infrastructure:**
- Dana has deep experience with product-oriented engineering and developer tooling, directly applicable to building the "cursor-like experience" for content teams that GrowthX is targeting
- Strong understanding of workflow automation, error handling, and building abstractions — key to scaling the current Temporal-based infrastructure
- Demonstrated ability to understand user pain points through direct engagement, which aligns with GrowthX's engineering-first approach to problem-solving

**To GrowthX Business Development & Growth:**
- Candidate is local to San Francisco and open to 2-3 days/week in-office, supporting GrowthX's hybrid model and team cohesion
- Strong professional network (has references available) and experience in adjacent technical markets could support future reference generation and network effects
- Interview positive signal suggests good hiring momentum; offer conversation next week indicates advanced stage in candidate pipeline

**To CheckThat & AI Strategy:**
- Dana's perspective on AI-powered workflows validated GrowthX's core thesis: AI coding is the killer app, but using that coding for downstream business problems (like SEO/content) is the real unlock
- Discussed how vertical specialization (content marketing) provides advantage over generic AI solutions, reinforcing CheckThat's approach to domain-specific AI visibility

---

## Overview

- Dana completed a coding exercise to build an article processing pipeline with AI-powered features
- GrowthX.ai has built an internal workflow engine and infrastructure for AI-powered content marketing services
- The company is scaling rapidly but faces challenges in automating processes and managing growth
- Dana's product and engineering background aligns well with GrowthX.ai's needs at this stage

---

## Key Topics

### Coding Exercise

  - Dana built a script to process articles, generate summaries, translate to Spanish, and extract fact-check items using AI APIs
  - Implemented error handling, file output, and used template strings/Liquid for formatting
  - Discussed potential improvements like separating logic, adding retries, and saving intermediate steps

### GrowthX.ai Infrastructure

  - Built internal workflow engine and scaffolding tools for AI-powered content workflows
  - Uses abstraction layers on top of Temporal for task management and error handling
  - Generates code, prompts, and documentation from high-level workflow descriptions
  - Aiming to create a "cursor-like experience" for content creation team

### Team Structure and Scaling

  - Currently \~60 people on services team, aiming for $22M revenue this year
  - Organized into pods with directors, managing directors, and helpers
  - Facing challenges in training and optimizing human processes as they scale
  - Working on automating more of the workflow to improve efficiency

### Engineering Approach

  - Engineers expected to be close to the business and understand customer needs
  - No dedicated product managers - engineers take on product thinking
  - Emphasis on building empathy with users by shadowing/doing their work
  - Remote-first with option for office time in San Francisco

---

## Action Items

- **Daniel Lopes (GrowthX):** Send offer and compensation details to Dana by end of day or Monday at latest
- **Dana Levine:** Provide professional references for background check
- **Daniel Lopes (GrowthX):** Follow up next week to discuss offer and any remaining questions from Dana

---

## Transcript
**Dana Levine:** Yeah, it's doing well.

**Daniel Lopes:** Happy, happy to be end of the week.

**Daniel Lopes:** Cool, I'm not going to take too much of your time.

**Daniel Lopes:** I'll show you the format for today that we usually, it's just like six minutes, like just 70 minutes each for you to like go to the exercise by yourself.

**Daniel Lopes:** Like I'm not going to be looking at your screen like you can do whatever you want.

**Daniel Lopes:** But I'll be in the chat, so if you have any questions, I'll be in the chat of, I'll turn off my camera and then I'll be in the chat here on the side.

**Daniel Lopes:** Okay, that sounds good.

**Daniel Lopes:** And then after that, maybe we'll spend like 50 minutes or so like going through the code base and then after that, we can spend whatever time we have left with like questions that can show you more stuff, talk about the team and all that.

**Daniel Lopes:** Cool, it's good.

**Daniel Lopes:** All right, let me show you my screen.

**Daniel Lopes:** And then I can walk you through the project.

**Daniel Lopes:** Yeah, so the project is essentially, so let me move you to the side, so let's see if can.

**Daniel Lopes:** The project is pretty much something that we do.

**Daniel Lopes:** It's part of, actually, one of the things we do on a regular is process content, receive articles, do something, like maybe translate the article, add some things, or add some text to the article, or extract things that we have, like our team has to do, like fact check things.

**Daniel Lopes:** In this case, it would be like article processing pipeline where we, like an API essentially that you can send a URL, and from this URL we scrape it, and we generate an e-brief.

**Daniel Lopes:** then translate Spanish, and then generate like a JSON, like a hash with like things that should be fact checked, and why, and here is the suggestion.

**Daniel Lopes:** The implementation is first article fetching and article parsing.

**Daniel Lopes:** There's this scraper called Gina that you can just pass whatever you're at the end.

**Daniel Lopes:** play with a little bit already. So, and then could you use OpenAI to generate the summary of the article at the top, that we can place at the top of the article.

**Daniel Lopes:** And then this finished translation, the fact check extraction.

**Daniel Lopes:** And if you could save the result in an output folder, that would be great.

**Daniel Lopes:** And we also have some suggestions here.

**Daniel Lopes:** And I have suggestions for how it could execute, but it could be different.

**Daniel Lopes:** Like, all these are just suggestions you can do in a different way.

**Daniel Lopes:** And this could be like the idea output of the API.

**Daniel Lopes:** at the end, I have here like some URLs that you could use to test it out.

**Daniel Lopes:** And there's like a boilerplate folder here as well that has some of the prompts.

**Daniel Lopes:** So, like the fact checking prompt is kind of tricky to get it, right?

**Daniel Lopes:** Yeah, that sounds good.

**Daniel Lopes:** So you can check it out and like download this before you see what you can and I can see that you can use cursor if you want it.

**Daniel Lopes:** So there's a cursor rules file inside of the folder that will like help guide cursor a little bit as well.

**Daniel Lopes:** So feel free to use cursor as much as you want because it's kind of a tool that helps with coding.

**Dana Levine:** So and so just want me to do like one off run.

**Dana Levine:** So I just run it with URL and it outputs.

**Dana Levine:** I don't need to build like a I don't need to build a service.

**Dana Levine:** I just need to basically write a script and handle this stuff.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** That's good.

**Daniel Lopes:** I want to do the same.

**Daniel Lopes:** That's fine.

**Daniel Lopes:** But like I think that's like out of like a harder.

**Daniel Lopes:** Yeah.

**Dana Levine:** probably just build a script because obviously once you have a script you could build like a, you know, because I'd have to, if I wanted to build service, I'd have to do like, you know, key to and like all sorts of stuff.

**Dana Levine:** So I'll probably, I'll probably just like, I'll probably just build a simple version and see how far I can get.

**Dana Levine:** Cool.

**Dana Levine:** Okay.

**Dana Levine:** So Borla Kade code.

**Daniel Lopes:** Then you.

**Daniel Lopes:** Yeah.

**Dana Levine:** I know that link, and then I'll let it started.

**Dana Levine:** It's good.

**Daniel Lopes:** Yeah, like I said, this is not meant to be like you have to have everything ready or anything.

**Daniel Lopes:** just going to get an idea of the project.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** Yeah, I can show you how we're actually doing production and you're going to get a better sense of you. That's good.

**Daniel Lopes:** All right.

**Dana Levine:** And I don't need to worry about like, like, I'm just hold on, let me see what's in this app in terms of like, okay, UCP, okay, UCP for, all right, sounds, sounds good.

**Dana Levine:** Perfect.

**Dana Levine:** Okay.

**Dana Levine:** Yeah.

**Dana Levine:** And I'll be in the chat.

**Daniel Lopes:** Like, I'll turn off my camera.

**Daniel Lopes:** Like, you can throw off your camera too if you want.

**Daniel Lopes:** But I hope you need help.

**Daniel Lopes:** All right.

**Daniel Lopes:** That sounds good.

**Daniel Lopes:** Yeah.

**Dana Levine:** just get started.

**Dana Levine:** then I can let you know if I need help.

**Dana Levine:** Great.

**Dana Levine:** All right.

**Daniel Lopes:** Thank you.

**Daniel Lopes:** right.

**Daniel Lopes:** Thanks.

**Dana Levine:** Talk to you in like 60 or 70 minutes or whatever.

**Dana Levine:** All right.

**Dana Levine:** You I'll just share a big screen so I can kind of show you everything that I did.

**Dana Levine:** Getting rid of a lot of extraneous here.

**Dana Levine:** Okay.

**Dana Levine:** Okay.

**Dana Levine:** Thank you.

**Daniel Lopes:** it's, it's a big, this is a big monitor.

**Daniel Lopes:** It's too big.

**Dana Levine:** I use a 43 inch for him, 4k to use monitor, because it gives me a lot of real estate, but like it might be too big for you.

**Dana Levine:** can put on my smaller screen.

**Dana Levine:** That's too much for you to see.

**Daniel Lopes:** I think if you if you increase the phone size, like command plus, I mean, yeah, why don't I just I want to do to my I'll just do to my laptop monitor.

**Dana Levine:** That actually like might be easier.

**Dana Levine:** Okay, cool.

**Dana Levine:** Let's just do that entire screen.

**Dana Levine:** There we go.

**Dana Levine:** Okay, cool.

**Daniel Lopes:** So here's my code.

**Daniel Lopes:** All right.

**Dana Levine:** Would you want me to just show you running first or do you want me to?

**Dana Levine:** And I tried on all three of like sample inputs you did.

**Dana Levine:** So like if I do this and this is like a th one.

**Daniel Lopes:** Yeah, the translation is the part that takes forever because they want to talk a while.

**Daniel Lopes:** Yeah, exactly.

**Dana Levine:** So anyway, it's not a big, okay, so the savers are at the one seven four nine five five nine.

**Dana Levine:** So it's this one, so here's the JSON output, we've got the original article, we've got the content.

**Dana Levine:** We've got the in brief.

**Dana Levine:** Um, this kind of transition and then we've got the fact check items that you that you Nice.

**Daniel Lopes:** Cool.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Let me just just walk me through the thing.

**Daniel Lopes:** Walk me through the code.

**Daniel Lopes:** Okay.

**Dana Levine:** So what I just did was I just I just created, um, honestly, like, I'm just putting everything in the honestly, just put everything in the input versus like putting more complicated context.

**Dana Levine:** Um, but I could have, like, obviously I could have, like, changed it so that, like, like, if

**Dana Levine:** Well, I just started with your, I started with your prompts, but then I like modified them a little bit because I'm getting things like outputting raw JSON, it takes a little bit of, without the tick, tick, tick, JSON, it takes a little bit of, a little bit tweaky sometimes.

**Dana Levine:** But anyway, yes, I did with, I just created an article, each one just uses the file responses, GBD4, and then it just, I just originally did with templates strings, but then I just switched it to, you use this liquid, and then, you know, you just put it in the article, and then, what else did I do that was of interest here?

**Dana Levine:** I mean, honestly, it was pretty, it was pretty straightforward, and then the prompts, like, I modified the prompts a little bit just to, like, to do a bit, like, to get it to work, you're, it only required a little tweak, and honestly, this one, I think it is complicated here.

**Daniel Lopes:** Very exact instructions.

**Daniel Lopes:** That one is a tricky one.

**Dana Levine:** Yeah, exactly, but sorry, there's a bare version of this again.

**Dana Levine:** See, I just use a template string at first, and then switch over to doing your liquid after.

**Dana Levine:** words after the fact, effectively it's the same.

**Dana Levine:** I mean, I guess Liquid gives you a little more flexibility in terms of like the formatting.

**Dana Levine:** But yeah, it's good to isolate the logic.

**Dana Levine:** probably could have like here, like, I did with a little bit of code repetition here because obviously, like, I repeated this code, but it wouldn't have been that hard for me to separate it out.

**Dana Levine:** I didn't do that much error handling.

**Dana Levine:** I just kind of like if there was an error.

**Dana Levine:** just caught a lot of error.

**Dana Levine:** Obviously, I wouldn't do this in any production system.

**Dana Levine:** Again, we probably have a queue.

**Dana Levine:** probably would put an error in the error log.

**Dana Levine:** If it's something that's like, if it's something that's recoverable, would probably do retries.

**Dana Levine:** We might even want to stay to intermediate steps because it's possible that any one output could fail.

**Dana Levine:** So right now, if anyone thinks it's going to bomb the whole thing, obviously, like, it'd be possible to either return partial

**Dana Levine:** If something fails, just by doing try capture on the individual things, or again, just retry the whole thing.

**Dana Levine:** it fails, I didn't get to that level of complexity in this kind of thing.

**Daniel Lopes:** How did you handle the, in the problems, how did you handle the URL translation?

**Daniel Lopes:** I don't know if you had time to.

**Daniel Lopes:** I just put in, how did not translate the URLs?

**Dana Levine:** I just said don't translate the URLs.

**Dana Levine:** Yeah, seemed to work.

**Daniel Lopes:** That would do.

**Daniel Lopes:** Yeah, make sure not to.

**Daniel Lopes:** Because you, you, you, you mentioned that.

**Dana Levine:** So I said, make sure not to translate the URLs and it, it seemed to not like, yeah, like I don't want look at one of them.

**Daniel Lopes:** yeah.

**Daniel Lopes:** How did you save this up to the disk?

**Daniel Lopes:** Like, did you use the, what I have to do?

**Daniel Lopes:** Yeah, yeah.

**Dana Levine:** I just kind of like, I just kind of like, use this and honestly, I use honestly as cursor.

**Daniel Lopes:** It wasn't that hard.

**Dana Levine:** But then I just wrote out and then I just did, you know, I just did, as you suggested, I just did a timestamp and then use a file name and then I return the file name, which then I wrote to the, which then I showed you as if I output.

**Dana Levine:** to the user, what the results were saved to.

**Daniel Lopes:** Yeah, sounds good.

**Daniel Lopes:** How much of like a TypeScript type experience do you have?

**Daniel Lopes:** did you rely on cursor quite a bit?

**Daniel Lopes:** like, that's just curiosity question.

**Daniel Lopes:** I'm not an absolute anti-script.

**Dana Levine:** I'm like, I'm like enough to be, like, I've done a lot of, I honestly be doing a lot of coding without cursor lately.

**Dana Levine:** And that's just because like, a lot of people don't want cursor.

**Dana Levine:** I've just been practicing.

**Dana Levine:** I've been doing a lot.

**Dana Levine:** So I'm not an expert in TypeScript at all.

**Daniel Lopes:** I understand the general.

**Dana Levine:** I understand the general typings.

**Dana Levine:** if you were looking at code, it would be like, pretty good in terms of typing.

**Dana Levine:** For the stuff I'm not using, cursor on, I don't, like, there's all, TypeScript is a radical.

**Dana Levine:** You can go, like, really, really, really deep down.

**Dana Levine:** Do you see the guy who wrote Doom and who wrote Doom and TypeScript?

**Daniel Lopes:** Or what we can pile Doom and TypeScript?

**Dana Levine:** honestly, like, that's like, that's like crazy level.

**Dana Levine:** There's a website that I, that I, that I had, that I get emails from.

**Dana Levine:** There's like,

**Dana Levine:** Of course, to work on to use TypeScript, don't occasionally read those things.

**Dana Levine:** I use Flow in the past, is like very similar to TypeScript.

**Dana Levine:** I'd actually probably use Flow more than TypeScript, because I worked at a company for four years that used Type, know, use Flow like extensively.

**Dana Levine:** But my experience like having done a bunch of projects and stuff and using TypeScript is like, it's not that much different.

**Dana Levine:** My last company just used JavaScript.

**Dana Levine:** They didn't use TypeScript, which was interesting.

**Dana Levine:** But yeah, that's what I did with my previous company too.

**Daniel Lopes:** But now at this time, like, we're switching to TypeScript, because it's the community.

**Daniel Lopes:** Like when I'm along some things open stores, I think there's a huge benefit of TypeScript with like something like Perseverable Generation. I can show you some of this stuff we have.

**Daniel Lopes:** yeah, how do you feel about that person in general?

**Daniel Lopes:** the, like, things like Persever, like, would you use that?

**Daniel Lopes:** like, would use Perseverable?

**Daniel Lopes:** I love Perseverable.

**Dana Levine:** Like, I love Perseverable, I use it.

**Dana Levine:** I'm always skeptical of anything that it ever like tells me.

**Dana Levine:** I always want to check it.

**Daniel Lopes:** Like I would never, I would never like, I would never put cursor code into production without like, without going through with a fine booth comb.

**Daniel Lopes:** like the thing is that it's a great way.

**Dana Levine:** Like it, it definitely like, it definitely automates a lot of like this task things.

**Dana Levine:** Like honestly, like I'm building a React app.

**Dana Levine:** Like there's a lot of stuff that like I just tell cursor to Duke, it comes up with a reasonable starting point.

**Dana Levine:** And then I can like modify things.

**Dana Levine:** After that, I've kind of been like trying to play around with like, how can I, you know, get it better instructions and be like, okay, here's, here's like, here's more.

**Dana Levine:** Here's the, here's the output form, right?

**Dana Levine:** I'm like, and see if that gets closer.

**Dana Levine:** But honestly, yeah, I just, the thing I've actually found cursor to be the most useful for is debugging.

**Dana Levine:** It's not always helpful, but very often it's like, yes, when I was screwing around with the Docker and I wanted to, like, I would, I, my Docker file was like, right?

**Dana Levine:** And I was like, Hey, can you like fix this for me?

**Dana Levine:** And it did.

**Dana Levine:** So I feel like cursor is really helpful in like fixing little, little bugs, again, sometimes it does, it's not right.

**Dana Levine:** Like even during this time, this assignment, there was a least one time or as cursor.

**Dana Levine:** like with totally all face and have to figure it out on my own, but yeah, yeah, it's interesting.

**Daniel Lopes:** the reason I'm asking that is because there's so many things that I think it's very useful if you have this set up in the architecture properly.

**Daniel Lopes:** And the way we're thinking, I can actually show you how we could do that same assignment in our infrastructure.

**Daniel Lopes:** So yeah, that'd be awesome.

**Daniel Lopes:** Yeah, so does work for that we have like we like we get stuff like this all the time and we have a bunch of workflows are standard, common things that we do with all the clients where we have a bunch of custom things too.

**Daniel Lopes:** And like in this case, let's say if I just like use the exact same, almost the exact same prompt.

**Daniel Lopes:** So like the same thing we had.

**Daniel Lopes:** So like a generating green content in Spanish, a copy and paste pretty much from the notion document with the same output.

**Daniel Lopes:** And then we have a

**Daniel Lopes:** a project that has a bunch of scaffolds, and they will generate like a normal, like Rails would do or Django would do, like normal file with like a example.

**Daniel Lopes:** But then we'll take your plan file and a bunch of other directives, and trigger an LLM call and peel out the file.

**Daniel Lopes:** Because it's super structured, because the way that the folders are structured as well, and all the rules we have in the documentation we have, it usually works from the first try.

**Daniel Lopes:** So that's what we use, like this came from the need that we had, like we're using tools for like a billion workflows, using GUI, using like graphs and like drag-and-drop, like things like N-A-N and our air tape or retool, like all the things that are visual, and it's just taking so long time.

**Daniel Lopes:** we're going straight to code, was the thing that, like if I do, that added a lot of productivity for us.

**Daniel Lopes:** So we have a scaffold, and I'm just passing the name of the workflow that I want, and I'm passing the file, that file that I just showed you,

**Daniel Lopes:** be anywhere and this dash I triggers the AI generation process.

**Daniel Lopes:** So it creates the four files and the four files the way they are structured.

**Daniel Lopes:** We have a workflow we'll just manage the branching like looping and parallelization if else things like that.

**Daniel Lopes:** Activities are these steps like the functions like you did.

**Daniel Lopes:** Types are just for 40, like it's just types of types, but the way we were separate the four files like this, then you can use cursor with the cursor rules for each one of those separate.

**Daniel Lopes:** So when you're in the prompt file, it knows it will load a bunch of rules for prompt engineering.

**Daniel Lopes:** And the reason why we use a liquid is going to use a if else.

**Daniel Lopes:** So if you pass a variable can do something with that, it can make sense.

**Daniel Lopes:** And then the types, you also have the types for every API.

**Daniel Lopes:** So it knows the API is input and output.

**Daniel Lopes:** So like when you load the whole folder into cursor, it would know exactly what that whole workflow does.

**Daniel Lopes:** then we also

**Daniel Lopes:** generate the documentation and documentation is a flow chart with like the description of everything as well that we use for the for the folks in the team for the human the sales team and the managing errors and all that and but it's also very useful for cursor so yeah so like we have so this is the generator the result let's see if it works that most of the time it works just from the start we broke the hot reload yesterday so let me just see if it will pick it up if we fix that yeah so every workflow becomes an API so we get an API I'm running local but we have the same thing in production so you press the name of the workload that was created whatever inputs you have and if it's going to be synchronous or a synchronous so I'm running synchronous and this will be loaded here I'll open a localhost version of this

**Dana Levine:** So it's running to be my sacred, I say sacredness if you run that one before you run the next one or if you're going to run a bunch in parallel.

**Dana Levine:** Is that how that one will be holding the connection open?

**Daniel Lopes:** Because this stuff we use like air table or air ops or like like retool, like they don't let you like send a web hook back the cell.

**Daniel Lopes:** So we just wait for the complete.

**Daniel Lopes:** This is not going to skew.

**Daniel Lopes:** Oh, I see because maybe I don't don't support web hook, like all that.

**Dana Levine:** Okay, I say makes sense.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So like it worked in the start.

**Daniel Lopes:** So the result was the original content, the in brief, the fact check items and the Spanish thing.

**Daniel Lopes:** They didn't get there, maybe, or maybe I didn't add the Spanish.

**Daniel Lopes:** We can remove this Spanish.

**Daniel Lopes:** But the code, let's see.

**Daniel Lopes:** So the way like we have the the runtime that executes everything, it's on top of the important show here.

**Daniel Lopes:** And then we have this GUI that help us visualize what's going on.

**Daniel Lopes:** on.

**Daniel Lopes:** And ideally here we also start building the interface where people there are less technical to start creating the workflows and send the request back to the project.

**Daniel Lopes:** So you can see the steps of the workflow.

**Daniel Lopes:** And you have like scrape article, generate the in-brief, translate to Spanish.

**Daniel Lopes:** this one failed.

**Daniel Lopes:** I need to check why sometimes it's worked like 99% of the time when I run this it works.

**Daniel Lopes:** Yes, I didn't.

**Daniel Lopes:** But it's close.

**Daniel Lopes:** And let's see the code.

**Daniel Lopes:** So the code is...

**Daniel Lopes:** So this is on top.

**Daniel Lopes:** There's a bunch of abstractions on top of Temporo.

**Daniel Lopes:** Temporo, let's do things like control retrieval errors, back off coefficient, like all the things that you would need for like API handling, like microservice handling essentially.

**Daniel Lopes:** Nice.

**Daniel Lopes:** Yeah, that makes sense.

**Daniel Lopes:** And it's parallelizing all the calls here automatically and returning the result.

**Daniel Lopes:** And then we have the prompt.

**Daniel Lopes:** The prompt, we keep it all in one file.

**Daniel Lopes:** then we have cursor rules for dealing.

**Daniel Lopes:** from engineering based on a bunch of front-engineer best practice.

**Daniel Lopes:** Like we used to use like a bunch of prompt generators, like, and Tropic has a really good prompt editor.

**Daniel Lopes:** But we, of course, just became much better with the things we did.

**Daniel Lopes:** And then the activities, those are the steps.

**Daniel Lopes:** Let's get cursor to generate all the prompts for you.

**Dana Levine:** Like, do you have to tweak them much, or is it like, or are they kind of like, or are they?

**Daniel Lopes:** We're using Claude under the hood to do the scaffold pass.

**Daniel Lopes:** And that has a bunch of instructions.

**Daniel Lopes:** then when you're here, cursor will load a bunch of the rules that we have for prompting.

**Daniel Lopes:** So cursor is like, really good at iterating on the prompt.

**Daniel Lopes:** The first pass is through Claude.

**Daniel Lopes:** I say, OK.

**Daniel Lopes:** Yeah, so there's like a bunch of practices.

**Daniel Lopes:** Like, in some cases, this is the part we actually want to improve a ton.

**Daniel Lopes:** And if we improve the IDE, the UI that I showed you, that's a place where we would improve a ton to make it easier to improve on the prompts.

**Daniel Lopes:** there's a bunch of techniques, like chain of thought, or like, tabular chain of thought.

**Daniel Lopes:** Like, depending on the need you have, like, we should be like.

**Daniel Lopes:** like generating different problems and helping people with prompting.

**Daniel Lopes:** But it's a curse which is pretty solid already.

**Daniel Lopes:** And then types, this is the types, and the activities are, we have a bunch of abstractions on how to render templates and how to scope the steps and things like that.

**Daniel Lopes:** And you can re-rind.

**Daniel Lopes:** if we're running this on top of this runtime called Temporo, and you can re-rind back to certain activities.

**Daniel Lopes:** So you can loop and you can iterate on like replay the activity when you're in development.

**Daniel Lopes:** So that's kind of infrastructure we have.

**Daniel Lopes:** And this is powering most of, pretty much powering the whole company.

**Daniel Lopes:** So we use it for writing content.

**Daniel Lopes:** If we're doing like content creation, we use it for helping us like three eyes, some of the resumes you get.

**Daniel Lopes:** We have the hundreds of applications from the services team at day.

**Daniel Lopes:** this, we have a workflow.

**Daniel Lopes:** with a bunch of rubrics to help us like how like what are the things we need to look for in this person upload a resume that's relevant to this person answer the questions that we have and how did they do that what are the things we should be thinking about when you're talking to them so yeah we're using that for the we're closing for the whole company essentially and the the mindset here is that we're starting with content marketing this is just like a vertical that that makes a ton of sense for LLMs is also ourselves background and we have a ton of expertise there but it can be used for anything so we're taking the approach of like what's the best way to describe the work and cold is amazing like and we're creating those engines to drive cold and it's just getting better and better so there's no point in creating GUI where you're going to be stitching together like little nodes and and so that's why we took the approach and like let's do this like a code first generation engine

**Daniel Lopes:** It's like if you like as programmers, we don't want like spend time thinking about the syntax or the types.

**Daniel Lopes:** don't want think about the architecture.

**Daniel Lopes:** That's why most of our interview process was like about the architecture, if you leap into the actual, the bulk of the work.

**Daniel Lopes:** But we're thinking about architectures, the thing that matters, and that applies to like content creation, sales and all that.

**Daniel Lopes:** So we're thinking now, essentially what we're appealing, I don't know if I've shown you this before, don't think so.

**Daniel Lopes:** I don't show this to many people.

**Daniel Lopes:** But we have the iWorkflow engine is generic.

**Daniel Lopes:** What I showed you is this framework that creates the project structure, you have all the abstractions.

**Daniel Lopes:** We have the runtime, which is would be like abstracted by the framework.

**Daniel Lopes:** If you launch this open source of someone else that do that on their own company, create features using these mechanisms.

**Daniel Lopes:** And then we have the IP, the cloud version that I showed you, like the UI, where you could have integrations with Workflow, help remain to maintenance, help create new workflows.

**Daniel Lopes:** So this stuff we have like functional.

**Daniel Lopes:** And we replaced a lot of our main vendors that were being a problem for us to move fast.

**Daniel Lopes:** And we're now creating the plans to make this reusable and applicable to any use case.

**Daniel Lopes:** And then we have the content OS that is a user interface we're working on now that will replace air cable, air ops and notion, the two things we use to collaborate with clients.

**Daniel Lopes:** And that's where we're going to be.

**Daniel Lopes:** That's going to be specific to marketing, specific to content marketing and have like a bunch of things to that vertical specifically.

**Daniel Lopes:** And we also want to have a marketplace where a lot of the small needs we have are like, hey, like this article here is this factual or is this made we need to have like a nurse practitioner to review something about an article for hands or like for webflow, they need a programmer or like there's a use case that we have.

**Daniel Lopes:** And now we're like finding these people to upwork, getting them into our slack and then having them work with us for a couple of weeks and then let it go.

**Daniel Lopes:** to offer that.

**Daniel Lopes:** So we're going to essentially create something that's a mix of upwork and and mechanical torque and things like that but within the scope of the process and we're also creating a bunch of micro apps around some of these workflows.

**Daniel Lopes:** So one of the workflows we have, for example, let's see if somebody's running it now.

**Daniel Lopes:** we have, I think research one is interesting, we launched this now.

**Daniel Lopes:** Essentially you send a bunch of context about what you do as a company.

**Daniel Lopes:** The topic you want to research and what's your goal and in this case the goal is to write a long article about these things and then we come up with a bunch of questions and then we run a parallel deep research with perplexity on each one of these questions and assemble a data set at the end that you can use throughout.

**Daniel Lopes:** the the documentation was talking about the thing that the flow chart and everything is a visual visual.

**Daniel Lopes:** So you can view it here, but we also have the collection of workflows here.

**Daniel Lopes:** So let's see.

**Daniel Lopes:** The deep reserve meeting, we'll use like for cover image generation.

**Daniel Lopes:** It's also interesting.

**Daniel Lopes:** This one is actually more interesting.

**Daniel Lopes:** So for image generation, would have like a prompt to come up, read an article, and come up with 10 ideas for what would be good prompts for this.

**Daniel Lopes:** then another step would select the best idea and then run, if it's a simulation, run just one, or run multiple images and then store an S3 and return a collection for the editor to choose.

**Daniel Lopes:** So they don't need to know how to prompt or like what's the style to use or things like that.

**Daniel Lopes:** So like the article generation one is interesting.

**Daniel Lopes:** Let's see if somebody did it today.

**Daniel Lopes:** Like the one thing that we're missing, like a bunch of basic stuff, know, there's no pagination in the field.

**Daniel Lopes:** Yeah, yeah, totally.

**Daniel Lopes:** There's just seven months in, and we're trying to move as fast as we can, but let's see if this one, this one, this one,

**Daniel Lopes:** just one image.

**Daniel Lopes:** But that's the image that they generated and the input was input was this chunk of the article they want in part style.

**Daniel Lopes:** So we have a bunch of predefined styles, art direction predefined as well for this client that we remove some of the  and we have like some colors and single image to generate just one.

**Daniel Lopes:** That's why at the end they have just one.

**Daniel Lopes:** So we can see the outputs here and why I chose that image.

**Daniel Lopes:** So I think you get the idea.

**Daniel Lopes:** think it's not really easy to understand now that we're working on that assignment.

**Daniel Lopes:** Does that make sense?

**Daniel Lopes:** Yeah, I get it.

**Dana Levine:** totally makes sense.

**Dana Levine:** So you have all these different, is it like you have a set number of pieces or you always generating new pieces?

**Daniel Lopes:** We have a set of number of pieces and we use for most of the clients and a lot of it is very reusable.

**Daniel Lopes:** then there will be some things that

**Daniel Lopes:** but they're very specific to a certain client.

**Daniel Lopes:** then we have a folder here, for example, HN is a client of our Zuplo is an interesting one.

**Daniel Lopes:** they have one of the things that they like.

**Daniel Lopes:** They want to do is they generate, they have this crazy, they created their own CMS, and they have this crazy way of doing tagging for their articles.

**Daniel Lopes:** So we basically read this and turn this into a JSON and use an LLM step, and then we select the tagged automatically for them.

**Daniel Lopes:** So in this case, it's specific to them.

**Daniel Lopes:** So we do that at the edges.

**Daniel Lopes:** And but if somebody wants something that's completely different, then it's a different work stream.

**Daniel Lopes:** And then that might be like a project that will be staff different.

**Daniel Lopes:** So we have client ops engineers that we're hiring as well.

**Daniel Lopes:** They would be like creating the workflows and doing all that.

**Daniel Lopes:** And then we have the broad and runtime engineers, which would be like, where you, me, Felipe, some of the other folks fit in.

**Daniel Lopes:** That way.

**Daniel Lopes:** We're building for a structure for the client ops engineers, you know, yeah, I say.

**Daniel Lopes:** Yeah, I know like we're we're almost I don't know if you have more time, but I can go if you want, like we didn't have time to go over your questions.

**Dana Levine:** But yeah, I have till I have till about like maybe I could go to like New Year, maybe 12 15.

**Daniel Lopes:** Yeah, sounds good.

**Daniel Lopes:** I think I don't think I know.

**Daniel Lopes:** Yeah, I don't think I, yeah, we could chat for a few minutes.

**Daniel Lopes:** Chad mentioned that you were curious about the team structure and like who is involved.

**Daniel Lopes:** Yeah, and I pulled our chart and it's just too organizing the whole thing.

**Daniel Lopes:** But on my team on would be our team.

**Daniel Lopes:** We have me, Felipe Felipe.

**Daniel Lopes:** don't know if he told you to share much of his experience.

**Daniel Lopes:** He's like about 20 years of experience same as me and like a stripe Airbnb and Apple.

**Daniel Lopes:** So he was an Airbnb at the beginning of the mobile team.

**Daniel Lopes:** Subscribe to you there for a couple of years and do a bunch of smaller startups in the.

**Daniel Lopes:** between the profile of people who are looking for somebody that has seen both sides of the spectrum and also has like some entrepreneurial background or can do things on their own, because we're going to staff the team in a way that's probably going to be like mostly preschool level engineers or staff level engineers and take advantage that we are profitable and we can afford like a larger-ish company's salary and we can go off with people that have experience first instead of like doing what most of the AI companies are doing, many people share our college and then you have ask the kids, they're crazy, you have a infrastructure that doesn't make any sense, everything crashes, so we're trying to figure out that from the beginning a little bit.

**Daniel Lopes:** Then we have Clint.

**Daniel Lopes:** Clint is joining next week.

**Daniel Lopes:** He was employee number six at Hashi Corp helping build Terraform.

**Daniel Lopes:** Same idea, like super humble guy, super experienced, heavier on the backhand.

**Daniel Lopes:** Marcus is part-time, so Marcus is essentially doing support.

**Daniel Lopes:** port.

**Daniel Lopes:** But he's a pretty experienced engineer too and came from Doxie Mini.

**Daniel Lopes:** We work together before as well.

**Daniel Lopes:** Kirkland just joined.

**Daniel Lopes:** Kirkland is the first client ops engineer.

**Daniel Lopes:** We're probably not going to hire a ton of them.

**Daniel Lopes:** would be like probably two or three for now.

**Daniel Lopes:** And they are building the workloads and things like that.

**Daniel Lopes:** So they are more, they are a lot less experienced than the product than the runtime folks.

**Daniel Lopes:** But they bring experience from like SEO and growth and things like that that we don't have.

**Daniel Lopes:** So that's, then we will be like helping them.

**Daniel Lopes:** then on the other side, have Jason's head of growth came from Kite.

**Daniel Lopes:** I don't know if you remember Kite, was like a brief cursor, like an editor, like it was pretty popular with the Python folks.

**Daniel Lopes:** That's another year.

**Daniel Lopes:** Then Bridget, Bridget is our ops person.

**Daniel Lopes:** She's amazing.

**Daniel Lopes:** Vp of ops does all the operations help with recruiting and everything else.

**Daniel Lopes:** In front air bite and the head of recruiting is also from their air from their bite.

**Daniel Lopes:** So we decided to hire a recruiter.

**Daniel Lopes:** immediately and somebody experienced because there's two paths here like first we need to build a super strong team and also there is a path where well exactly what we're doing is also applicable to recruiting so might as well just like if there's an opportunity here we like in the recordings also core part of the services side so and then on the service side we have oh yeah Kyle was head of growth for the trade.ai he's like taking over sales now he was with the services team before Matthew Matthew was a editor in chief for that crunch he joined us a couple of weeks ago yeah so Matthew is amazing and he will be leading he's like for his role as chief of contents and he'll be leading all the services folks so and under him we have folks that were former growth people at SEMrush, TripAdvisor, Insider, G2 Crowd, active campaign and some other people and everybody under them have experience as well as

**Daniel Lopes:** then managers and managing editors.

**Daniel Lopes:** And then under that we have help.

**Daniel Lopes:** They're doing like the day-to-day operations of each account, running the flows and like sharing things with clients and stuff like that.

**Daniel Lopes:** And the services side will probably grow a ton.

**Daniel Lopes:** Our side, I'm expecting to have like maybe 10 engineers by the end of the year, 10 to 15.

**Daniel Lopes:** And I'm also thinking about designing engineers in the mix.

**Daniel Lopes:** So it would be like every maybe like like that's a setup that I saw in the third services that I really liked was two programmers where every two product engineers of people actually do new features and things like that for every designer.

**Daniel Lopes:** And the designers were technically enough to be in the mix and like being collaborating on the day-to-day like holding some planes and like in the loop instead of just like handing you a Figma file and then you figure out.

**Daniel Lopes:** So that's what I'm shooting for.

**Daniel Lopes:** So I hope that gives you an idea of like who we have on the team today and the type of people we're trying to hire.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Yeah.

**Dana Levine:** Yeah, totally.

**Dana Levine:** Just what kind of question you manage like scaling.

**Dana Levine:** So I'm kind of curious, how far do you think you can scale with like what you currently have set up?

**Dana Levine:** And at what point are you gonna have to like kind of totally redesign things to keep scaling?

**Daniel Lopes:** You mean you scale at the number of employees or scale on the amount of effort we are at the level?

**Daniel Lopes:** I mean more like, I mean more like number of cost version revenue.

**Dana Levine:** But you're gonna have to, in order to scale cost of the revenue, I assume you're gonna need to scale, you're gonna need to scale, at very least the right kind of the right side of that chart and maybe at least you need to scale sales.

**Dana Levine:** But like, yeah, I guess the question is like, if you were gonna like double, Yeah.

**Dana Levine:** And what point does it start to break down?

**Dana Levine:** Cause like, it seems like it's a human intensive process.

**Dana Levine:** So it's like, yeah.

**Daniel Lopes:** How do you see that?

**Daniel Lopes:** Let me see if you can see if I have the, I don't have, that was on the teach deck for the investors, but I don't have it here.

**Daniel Lopes:** But yeah, the margins.

**Daniel Lopes:** like right now the margins are actually super healthy.

**Daniel Lopes:** So like we're at 75% margin.

**Daniel Lopes:** So the main problem that we're dealing with is more on the training side and on the using the tools on the day to day.

**Daniel Lopes:** And a lot of the challenges like people like getting people up to speed fat, like we were like hiding was not a problem and more it was a problem in the beginning.

**Daniel Lopes:** So with the fact that we're remote with the fact that we can afford a higher pay than most of the agencies and with the fact that we have the pipeline and the recruiting team to like triage well so we're hiring essentially two to three people a month for the services team and we haven't had a problem getting like anywhere anybody under from the brown line below like everybody's super skilled and so I'm not too concerned about the skills like and hiring side of things and the margins like right now we are not even like forcing the margins to be, are we not squeezing the margin?

**Daniel Lopes:** like I know I'm optimizing on almost anything.

**Daniel Lopes:** like we're, like everybody's full time for like what would be like typically freelancing at other places, everybody's full time because there's so much of the automations that removed out of the, like one person's extremely productive with what we have today already.

**Daniel Lopes:** And the planets to essentially have a cursor like experience for the, the, the, the, the content creation team.

**Daniel Lopes:** And like we have the, the features and have the roadmap and everything, some of the designers already in motion.

**Daniel Lopes:** And I think we're going to get there.

**Daniel Lopes:** So we kind of hacked everything together with air table and things like that, and it's no, by no means like easy to learn for the folks in the services and they're making it work.

**Daniel Lopes:** And the fact to make it, they're more productive is like very clear.

**Daniel Lopes:** So I, we think we can get to like this year, I forget the head count exactly.

**Daniel Lopes:** That's like something that Bridget has.

**Daniel Lopes:** But I think we're going to have about 60 bonus services team.

**Daniel Lopes:** And that is enough for us.

**Daniel Lopes:** to get a very doable for us to hit like 22 million, like the more revenue this year, 22 million in revenue with these 50 people in the services team, and it would be super profitable.

**Daniel Lopes:** And next year, I think we can hit the 100 million.

**Daniel Lopes:** And so the model doesn't break.

**Daniel Lopes:** And that was the pod size structure we have today.

**Daniel Lopes:** every, here's like every director has three managing directors, every managing director has like two or three pounds, and they have the helpers under.

**Daniel Lopes:** And I think every step of the way as we're optimizing, we can reduce the number of helpers.

**Daniel Lopes:** So it says about the money problem, it's more about like the human management side.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** get it.

**Dana Levine:** That's kind of what I mean is that like what I see here is the is the management is the human management at some scale, like it's probably it's going to get twice as many people.

**Dana Levine:** You probably need twice as many people.

**Dana Levine:** on in the brown and in the green, right?

**Daniel Lopes:** Like today, we could double if we had training with people more.

**Daniel Lopes:** So they're not a maximum capacity. clinics should reduce the training complexity by making the software.

**Daniel Lopes:** Yeah, yeah.

**Dana Levine:** That's the real thing is building, making the software smarter such that the people, it's easier for the people who are actually doing the work to do the work.

**Daniel Lopes:** That's definitely the challenge.

**Daniel Lopes:** way to think about is like, that's the thing that we're always thinking.

**Daniel Lopes:** It's just like, okay, this is the service as a software business, cracking the service is the challenge.

**Daniel Lopes:** real thing we're trying to solve is, can you make service scalable?

**Daniel Lopes:** And we are choosing content marketing as the first way to try, because it's scheme where everybody's already used to hiring an agency.

**Daniel Lopes:** we think it's possible.

**Daniel Lopes:** But I'm not going to hide and say it's going to be smooth.

**Daniel Lopes:** So the human side of the part is a huge challenge and thinking out the right way to hand off the tasks and like monitor the input and output the quality like that we like that's where all the like a lot of the automation and like the work we're going to have to turn the product side, it will be.

**Daniel Lopes:** And like so far, we did the easier part, which is like defined the working code and execute it.

**Daniel Lopes:** But now we have to actually view the UI.

**Daniel Lopes:** So I think making AI useful is a mix of like, it's both engineering problem, like running things that scale and retrialing, know, all that distributed systems.

**Daniel Lopes:** And then also GUI.

**Daniel Lopes:** like, yeah, of course, like the UI side is like, Oh, huge challenge.

**Daniel Lopes:** The UX side. hope that answers your questions kind of like vague.

**Dana Levine:** Yeah, mostly after they're like, I'm not expecting like, I'm not expecting like a, like a, like like a particular answer.

**Dana Levine:** I'm just kind of like more like curious.

**Dana Levine:** I was chatting with a friend before this, he's got us, a startup and they're like, but they're what they do is very

**Dana Levine:** very service intensive as well.

**Dana Levine:** And he's figuring out, like, we can't handle any more business, because they have to ex-humans do certain pieces.

**Dana Levine:** And they're trying to figure out how to automate it with AI.

**Dana Levine:** But it's like, you still need to make sure that the results are high enough quality, even when it's automated with AI.

**Dana Levine:** So it's like, yeah, I think it's an interesting problem to think about how you combine humans and computers to provide the best possible to provide a product, especially when it's been something it's traditionally been very human intensive like this.

**Dana Levine:** So I think is there someone who's in charge of operations and figuring that out?

**Dana Levine:** that Matthew?

**Dana Levine:** is it like, how's that getting figured out at the company, kind of the company?

**Daniel Lopes:** Yeah, so that has been Kyle and Marcel.

**Daniel Lopes:** Matthew was just like stepping in and trying to help that get into place.

**Daniel Lopes:** And that's the reason why we're in.

**Daniel Lopes:** What we did immediately was to hire a bunch of directors so they can handle the pre-automation part until we automate it out of the way.

**Daniel Lopes:** So like most companies will start to get like an army of like people who are getting an army of directors first and they can figure out until we have the perfect solution.

**Dana Levine:** And everybody's going to break because it's going to break very soon like it sounds like if you don't, if you don't have someone who's thinking about how do we manage this and how we build, the building a better organ than it's going to get you part of the way there.

**Dana Levine:** Like building the right org structure and then it's just going to be like, well, we can only scale like to a certain number of people before the whole thing gets unwieldy and then it's going to be like, well, how do we automate to make ourselves more efficient so that we can continue to like, continue to scale our business without having to scale people quite as fast.

**Daniel Lopes:** That's exactly the discussion we were having yesterday.

**Daniel Lopes:** We should like, first it's a human process and then once you have like a very solid human process then you figure out how to automate that and like we are literally like

**Daniel Lopes:** re-work the whole project management side.

**Daniel Lopes:** In the future, we'll be like a lot of that will be part of the platform before we have that, what's the setup in the short term.

**Daniel Lopes:** So a lot of the stuff we're doing is like, figure out the short term, good enough, and then replace with software, and then like, bloop, so that has been the case.

**Daniel Lopes:** And we're doing that literally right now with the project management tool for each pod here.

**Daniel Lopes:** Because they were using motion, and I sent people forgetting to do things.

**Daniel Lopes:** So like, a lot of it is also just like, okay, we're migrating everybody to linear, and then we have select procedures, and we have their day list end-ups, and we have the pod leader here, we'll have a check-in every week for them to check the quality, and me and we'll work first.

**Daniel Lopes:** then later we can like, okay, transcribe the clients and look for production issues, or look for concerns, where sentimental analysis and how the client is thinking about.

**Daniel Lopes:** So we get more signals.

**Daniel Lopes:** But that's the way we're thinking, and that's before we have.

**Daniel Lopes:** and you like to make the process of production be easier.

**Daniel Lopes:** So like we're trying to do things on both angles, like use existing tools, automate a little bit, also like find ways to completely change how the process works, it's possible.

**Dana Levine:** Yeah, yeah, makes sense.

**Daniel Lopes:** But it's definitely a human issue, like the organization issue, to be able to get out as a solid.

**Dana Levine:** Like, so just like one more question, is how are engineers, how do you want engineers to be involved in understanding the requirements and deciding what to build?

**Dana Levine:** What's your sort of perspective about how the engineering team will be involved in that?

**Daniel Lopes:** Yeah, that's the part that's still figuring out.

**Daniel Lopes:** Like, in the world, everybody in the engineering team will be...

**Daniel Lopes:** doing part of the workflow creation and like thinking about automation and every step of the way.

**Daniel Lopes:** And so the structure we have today is essentially this, Felipe and Clint will be having on AI workflow engine.

**Daniel Lopes:** But the three of us will be also doing the content OS.

**Daniel Lopes:** like it's very, that's the question actually I was going to ask you is just like, what's your preference in the stack to be?

**Daniel Lopes:** Like if you like building like project like features or like if you prefer to be on the back end and like building like CLI tools or things like that.

**Daniel Lopes:** So like I think the people that will be building UI and automation to the to solve the human problem that we're talking about, we're going to have to be like very business-minded and like product-minded and be involved with understanding whatever we are in time to automate.

**Daniel Lopes:** So that's and that's why we have the, if you look at our careers page, you have like two job postings, one is for back end and the

**Daniel Lopes:** distributed systems and the other one is more like product engineer, but essentially we're all doing the both things today and I could see where it starts specializing more, but the product engineers in my mind, we're always going to have to be very close to the business and how we are all writing things.

**Dana Levine:** Yeah, I think that's, yeah, I think it's going to be important, especially because I don't see any product management, which I think is fine, but I don't think company product managers when they're, when they're this small, it's like, because I think that the engineering team can be, can be really close to the customer.

**Dana Levine:** And like, yeah, my interest is like product, my interest is product engineering.

**Dana Levine:** With that said, I'm like, happy to like do like some, you know, some percentages of like, of like infrastructure as well.

**Dana Levine:** But yeah, like I, I enjoy talking to customers, understanding requirements, like I, you smart resume as a PM for a while.

**Dana Levine:** So I kind of like, yeah, kind of like understand that.

**Dana Levine:** I like, it's like really what I'm trying to find out is like taking some of like, the being able to talk to customers and understand the requirements and decide what to build with the actual being able to build it.

**Dana Levine:** So.

**Dana Levine:** That's like, that's what I'm looking for and it seems kind of like that's what you need now anyway.

**Daniel Lopes:** When I saw your resume and I saw a project, switching between product and engineering in music, this is precisely what we need.

**Daniel Lopes:** And yeah, I was very excited.

**Daniel Lopes:** And like the way I'm thinking, it's also like very similar to how basecamp operated and how I look at it, if that's all for a while, is that you don't need games if the people involved.

**Daniel Lopes:** So that's actually my question we have in our application is just, who do you think should write this back for the thing at this stage of a startup and whatever I get somebody that's like, I need this back already and somebody should do the talking to the client.

**Daniel Lopes:** Like that's a red flag at our stage.

**Daniel Lopes:** And I think that applies all the way to especially what we're trying to solve.

**Daniel Lopes:** It's a mix of human automation and all that and the engineering part.

**Daniel Lopes:** So like as close as possible to the client as possible.

**Dana Levine:** Like I was really the engineer should be doing a certain amount.

**Dana Levine:** of like of like either moonlight or actually doing a little bit of like the jobs of like the people who are doing we're doing the end like like the content content verification just to get to get empathy for like how they do it like like I think that's like very important is building that entity with those people and really understanding their pain points because like sometimes an engineer will shadow someone and be like oh I can make this tweak and that will save like a minute every time they have to do something and that's like you know across every across the number of calf things that need to be done that could be like a topic that could be like hours or weeks you know say yeah say if there's something like that um so I think it is very important to like build that empathy um especially this stage yeah yeah and there's like there's so much time spent in like small things they're like relevant to programming like bike shedding of little programming stuff and like huge things that are not being paying attention on the business side because we are not talking to the to the product to the people using the product so yeah that's like I ran

**Daniel Lopes:** for a long time, both if and the company before.

**Daniel Lopes:** Like I was like feeling the empathy of everybody and I did something as an engineer, it's like 100% agree with that.

**Dana Levine:** Yeah, and I tell you that I may have told you but I have a lot of experience like building dev tools and that's like, so I have a lot of experience working with developers and like trying to understand their pain points and the things that are challenging for them because I think that's kind of what this is.

**Dana Levine:** It's like just like understanding directly like the customer pain points and the users are pretty technical.

**Dana Levine:** Like my some of these people are fairly technical.

**Dana Levine:** So like, it's like really, really just like, like, and they'll have ideas.

**Dana Levine:** So I'm sure they'll have ideas and some of it is just being like, just like, hey, I talk to these five people and they all were having trouble doing this thing and like, oh, I think I can fix it by doing this.

**Dana Levine:** Like I think there's a lot of opportunity for like, especially at this point for like, for like creative solutions to like, yeah, to improve these workflows.

**Daniel Lopes:** But yeah, yeah.

**Daniel Lopes:** Cool.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Before we ran out of time, like.

**Daniel Lopes:** do you have anything else that you need my ask or anything that I wanted to share or oh no I think you've like answered I think you've answered most like questions I really thought like I really wanted to see the org chart that was that was key because kind of understanding the company a little bit more and yeah I'm trying to think is there anything else that I want to that I want to know where is everybody's distributed is that is that kind of like like we're people we're we're our people in general yeah Marcel me Jason and Kyle we have four people here in the Bay Area and a few meetings in Seattle most people are distributed okay and that had been like a huge advantage or like shooting like everybody's forcing people back into the office and we have the policy of trying to pay close to San Francisco salary or like at San Francisco salary at least for our team and from anywhere and it's been amazing how many great people you can find

**Dana Levine:** Yeah, yeah, um, yeah, I agree.

**Dana Levine:** mean, the last company I worked for was, was everybody was remote.

**Dana Levine:** And like, they had an awesome Santa Cruz, but everyone was remote.

**Dana Levine:** I went to the office like maybe half a dozen times.

**Dana Levine:** Um, well, I was, you know, we have an office here too.

**Daniel Lopes:** So yeah, whenever you want to come to the office, but you're here, right?

**Daniel Lopes:** Where are you based?

**Dana Levine:** I'm in San Francisco. I'm looking to comment.

**Dana Levine:** I'm looking to come in the office like, you know, two, maybe two days a week, maybe three days a week on, on flexible, but like, yeah, I was like the, I like being in person and seeing people and like, yeah, there's nothing that replaces like having conversations.

**Dana Levine:** Like, like I had an engine, one of my engineering leads, like we were working together on my last company and like, we both happen to be in like, we both happen to be in Santa Cruz, like the same day.

**Dana Levine:** And we just like did this white boarding session and figured out this like really complicated project.

**Dana Levine:** Um, it was like an API design, we just figured it out.

**Dana Levine:** And it was just like, great.

**Dana Levine:** And I was like, if we had done this like virtually, like we could have done it, but it was definitely, definitely more to just be there in person.

**Dana Levine:** So I think it's like that's the, I think

**Dana Levine:** It's a trip, but I mean, it sounds like the company is profitable, so I think it's like, I think there's definitely like how you bring people in person like a certain freak, know, have everybody meet up like a certain frequency at whenever possible and just like share, share knowledge and just.

**Daniel Lopes:** Yeah, that's, you know, out the policy actually, like this week was like, we're going to get the whole company together once a year for sure, and then for, and then we have the budget to do the smaller teams whenever they want, and like people that can fly, come fly here to it.

**Daniel Lopes:** let me see.

**Daniel Lopes:** So Chad mentioned that you are, you have some other companies, and you're very close to the, to an offer with other places, right?

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** Okay, so I can get together with the rest of the team, and I can send you something today, or I can send you a reply today, or a Monday at the latest, but I think I can do it today.

**Daniel Lopes:** I'm off, but after 2 p.m., but I.

**Dana Levine:** It's okay.

**Dana Levine:** Don't worry about it.

**Dana Levine:** I'm not, I'm not in like that.

**Dana Levine:** I'm not in like that much of a hurry, probably next, probably next week is when I'm likely to have to start thinking about some decisions.

**Dana Levine:** So it's like, yeah, that's what I would say.

**Dana Levine:** Do you have sounds good?

**Daniel Lopes:** Do you happen to have any people that you can use as reference, make a couple of references?

**Daniel Lopes:** Yeah.

**Dana Levine:** Okay, cool.

**Daniel Lopes:** So that would be the only thing.

**Daniel Lopes:** Yeah, I'm happy to say you.

**Dana Levine:** I'm happy to say you have the references you can check.

**Dana Levine:** I mean, obviously.

**Daniel Lopes:** But I can send you a email before just for you to have an idea of the numbers and things like that.

**Daniel Lopes:** But I would love to make an offer.

**Daniel Lopes:** Like, I talked to Felipe already into the rest of the team.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Okay.

**Daniel Lopes:** background is exactly what we need.

**Daniel Lopes:** not cool.

**Dana Levine:** Cool.

**Dana Levine:** sounds good.

**Dana Levine:** Great.

**Dana Levine:** Yeah.

**Dana Levine:** Yeah.

**Dana Levine:** Yeah.

**Dana Levine:** It's been a really nice shot.

**Dana Levine:** Really nice shot.

**Dana Levine:** was a fun exercise.

**Dana Levine:** I enjoyed doing it.

**Dana Levine:** So, and it's just been cool.

**Dana Levine:** talking about this.

**Dana Levine:** mean, I think this like kind of AI, like, like, or string AI workflows, like this is this is where things are going.

**Dana Levine:** Like, I think everything is going to be, I think everything is going to be done this way in the future.

**Dana Levine:** It's like, I think so too.

**Daniel Lopes:** We are very optimistic that we, I think we have like a year where not a lot of people figure out that the service is like, you can put service in front and then do the work first and then try to flip it.

**Daniel Lopes:** Yeah, so there's like a small window for us to figure this out fast.

**Daniel Lopes:** We're still in the timeline, but I think the future is in this direction.

**Daniel Lopes:** And many people will be trying to do the same.

**Daniel Lopes:** So we got it wrong.

**Daniel Lopes:** Oh, yeah, definitely.

**Dana Levine:** think this is going to be, I mean, I think the advantage that you have is you figured out a flow, you figured out a, you figured out a like a good starting vertical.

**Dana Levine:** Like, I think some people for these sorts of things are starting out kind of with the generic problem.

**Dana Levine:** And I think that you, it's an advantage to be like, you know, you decided content marketing is like, is like the place to start because I think that it's one of the big market.

**Dana Levine:** There's a lot of

**Dana Levine:** money being sent on content marketing, but two, it's a place to really learn.

**Dana Levine:** how do you do this the right way?

**Dana Levine:** And then, like, in the future, like, like, that could just be the starting point.

**Dana Levine:** Yeah.

**Daniel Lopes:** And it's also not space where everybody wants to handle that.

**Daniel Lopes:** Like, if you're trying to solve coding, you have 10 people trying to solve what the cursor is doing. code to market, like, especially, like, SEO, it's like, everybody's like, Oh, Chris, their nose, they know they need to be doing, but nobody does.

**Dana Levine:** And yeah, yeah, it's like, actually, I think the first killer app for AI is coding.

**Dana Levine:** And it's like, or maybe it's the killer app, or maybe it's the killer app, because I think someone was saying that about, and I'm like, but what you're doing is you're actually using that coding to, like, do other things, you know, to, like, get other tasks done, which think is smart versus just being like, Hey, we're just going help people write code, helping people write code is useful.

**Dana Levine:** But like, um, doing the coding for, like, for, you know, for purposes is like, yeah, I think that's cool.

**Daniel Lopes:** So anyway, um, yeah, thanks for your time.

**Daniel Lopes:** Yeah, just adding a bit.

**Daniel Lopes:** All right.

**Daniel Lopes:** All right.

**Daniel Lopes:** Yeah, cool.

**Daniel Lopes:** Talk to you soon then.

**Daniel Lopes:** All right.
