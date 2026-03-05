# Ben Church - Virtual Onsite | General Engineering (internal only)

<metadata>
date: 2025-05-13
time: 18:02 UTC
duration: 54 minutes
organizer: daniel@growthxlabs.com
participants: Ben Church, Daniel Lopes (GrowthX)
fathom_recording_id: 62375331
fathom_url: https://fathom.video/calls/298810370
share_url: https://fathom.video/share/hazsFjzYEf4SLxK_8zibvf-5yByyYZXh
source: fathom
enriched_on: 2026-03-03 00:00 UTC
</metadata>

---

## Summary

Daniel Lopes conducted a virtual onsite interview and coding exercise with Ben Church, a candidate for GrowthX's engineering team. Daniel briefed Ben on a content processing pipeline project involving TypeScript, GINA AI, and OpenAI APIs — tasks that represent core GrowthX use cases (in-briefs, translation, fact-checking). Ben outlined his systematic approach to the project and indicated strong interest in speaking with Marcel, GrowthX's co-founder, to understand the long-term vision before making a final decision.

---

## Context

This is a virtual onsite interview for Ben Church, an engineering candidate being evaluated by GrowthX. Daniel Lopes (GrowthX team) conducted the session, which consisted of two parts: initial conversation to build rapport and discuss the company, followed by a coding exercise. Ben is being assessed on his approach to a content processing pipeline project that mirrors everyday GrowthX work. The conversation opened with casual discussion about tools (Notion Calendar, Superhuman email) and Ben's previous interactions with other GrowthX team members. Ben expressed interest in understanding the company's long-term vision and strategy, suggesting he's seriously considering the opportunity if it aligns with his values.

---

## Relevance

- **To GrowthX Delivery:** Ben's proposed approach mirrors GrowthX's standard engineering practices — documentation-first, utility functions, tests for validation, debugger setup for iteration. His plan to set up docs for GINA AI, OpenAI SDK, and schema validation (Zod) directly addresses common integration patterns GrowthX uses in production.
- **To GrowthX Business Development:** Ben indicated positive reception to prior interviews ("they're both great to chat with") and explicit interest in a follow-up with Marcel on vision/strategy — suggesting strong candidate-to-offer conversion potential if messaging around long-term vision is clear.
- **To GrowthX Engineering:** Ben flagged potential gaps in the starter kit (VIT setup for better TypeScript compilation, debugger issues with current setup) and suggested improvements (SuperWhisperer for prompt optimization, Liquid.js templating for variable interpolation) — useful feedback for future iteration on onsite exercises.

---

## Overview

- Ben will work on a TypeScript project involving GINA AI and OpenAI APIs to create a content processing pipeline
- The project includes creating an in-brief, translating to Spanish, and fact-checking content from a given URL
- Daniel provided a starter kit with boilerplate code and necessary dependencies
- Ben will have about 50-60 minutes to work on the project, focusing on demonstrating his approach and thought process

---

## Key Topics

### Project Overview and Requirements

  - Input: URL of an article
  - Steps:
    1.  Fetch and convert article to Markdown using GINA AI
    2.  Create an in-brief (2-5 bullet points of key insights)
    3.  Translate content to Spanish (excluding URLs)
    4.  Extract fact-checkable statements
  - Output: Save results as JSON file
  - Tech stack: TypeScript, Node.js, OpenAI SDK, Zod for schema validation
  - Optional: Use of Liquid.js for prompt templating

### Development Environment and Tools

  - Starter kit provided with TypeScript setup and some dependencies
  - Cursor.sh recommended as code editor (with some preconfigured rules)
  - GPT-4 API key provided for OpenAI interactions
  - Ben plans to use SuperWhisperer for prompt optimization

### Ben's Proposed Approach

1.  Set up documentation files and update README
2.  Create utility functions for GINA AI and OpenAI
3.  Add tests to confirm functionality
4.  Set up debugger for iterative development
5.  Implement main logic and prompts
6.  (Optional) Optimize for parallel processing if time allows

### Additional Context

  - GrowthX.ai focuses on content creation, recruiting, and sales workflows
  - The company is building platforms to support various AI-driven tasks
  - This project represents a common use case in their business

---

## Action Items

- **Ben Church:** Work on the content processing pipeline project for 50-60 minutes during the coding exercise, focusing on demonstrating approach and thought process
- **Daniel Lopes (GrowthX):** Be available in chat to answer Ben's technical questions during the coding session; arrange follow-up meeting between Ben and Marcel to discuss GrowthX's long-term vision and strategy

---

## Transcript
**Ben Church:** I realized how long it's been since I opened this laptop, and what I didn't have was a notification set for my Notion Calendar.

**Ben Church:** It's very funny.

**Ben Church:** Let me make sure my camera connects here.

**Ben Church:** You're using Notion Calendar?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** It's funny.

**Ben Church:** I realize how often I've been doing personal projects on my work laptop.

**Ben Church:** I've got to reset up my camera here.

**Daniel Lopes:** I haven't had a chance to try it yet.

**Daniel Lopes:** I also know that they just came out with the email.

**Daniel Lopes:** The email one was interesting because Superhuman is one of our clients.

**Daniel Lopes:** And when they started, that was the trigger for them that they knew Notion was coming up with an email.

**Daniel Lopes:** They were afraid of it.

**Ben Church:** I can see that.

**Ben Church:** I can see that.

**Ben Church:** Have you tried out the Notion email yet?

**Daniel Lopes:** Not yet. I use Superhuman quite a bit, but I haven't tried Notion yet.

**Ben Church:** Yeah.

**Ben Church:** I'm stuck in this middle ground where...

**Ben Church:** And years ago, I was too cheap for Superhuman, and I was annoyed that they wanted to walk me through their product and didn't let me try it right away.

**Ben Church:** So I set up all, like, the hotkeys on my Gmail, and I saw the Notion email come out.

**Ben Church:** So it's been on my, like, little, like, personal to-do.

**Ben Church:** I'm ah, I should probably go back and revisit.

**Ben Church:** Who knows?

**Ben Church:** It might end up, like, my other to-do lists and, like, systems where you, like, add it in, and you use it for, like, a couple months, and then, like, regress.

**Daniel Lopes:** Yeah, exactly.

**Ben Church:** Exactly, exactly.

**Daniel Lopes:** Oh, man, thanks for doing this.

**Daniel Lopes:** Thanks for going through the whole process as well with the other guys.

**Daniel Lopes:** I hope you had a good time chatting with them.

**Daniel Lopes:** I haven't had the chance to check with them yet.

**Daniel Lopes:** Or, like, we also, like, usually record the calls.

**Daniel Lopes:** I don't mind if I record this.

**Daniel Lopes:** Yeah.

**Ben Church:** I thought it went well on my side.

**Ben Church:** I mean, they're both great to chat with.

**Ben Church:** Like, Felipe was sharp.

**Ben Church:** That was a fun conversation, I think.

**Ben Church:** Thanks for that.

**Daniel Lopes:** We've been pretty lucky so far with the whole team.

**Daniel Lopes:** It's a bummer that you don't get the chance to meet everybody when you're in the process, but once we're done today, let me know if there's anybody else you want to meet or if you want to chat with Marcel.

**Daniel Lopes:** You haven't had the time to chat with Marcel yet, have you?

**Daniel Lopes:** Okay, that would be great. If you want, we can set it up.

**Daniel Lopes:** He's on vacation now, but he's going to be back tomorrow, Thursday, actually.

**Daniel Lopes:** So yeah, up to you.

**Daniel Lopes:** But that would be more for you to get his side of the business and understand how he thinks about things, more than interviewing per se.

**Ben Church:** Yeah, I'd love to.

**Ben Church:** always like to, it's way nicer to get on the same page with the person who has the long, long-term vision, like yourself, like the founders, because then it's easier to make the small decisions.

**Ben Church:** So yeah, that'd be great.

**Ben Church:** Cool.

**Daniel Lopes:** Today, like, don't know, did Tucker show you the assignment up front or some material?

**Ben Church:** He gave me an email that basically outlined, like, hey, FYI, you're going into a TypeScript project.

**Ben Church:** You're going to be tinkering with GINA AI's APIs and OpenAI's APIs through its SDK.

**Ben Church:** And that was about it.

**Ben Church:** He was kind of like, hey, use Cursor or don't use Cursor.

**Ben Church:** But if you use cursor, don't use agent mode.

**Daniel Lopes:** Okay, okay.

**Daniel Lopes:** That's what I had told him as well. I mean, you can actually send the code from up front if he wanted to, since you guys work together. So there's some different expectation here.

**Daniel Lopes:** Let me share my screen. You can tell me your preference for how you want to do this. Sometimes people like to just work at their own pace. We can turn off the camera and I'll be here in chat to answer any questions. Or we can pair program, whatever you prefer.

**Daniel Lopes:** The project is essentially the same stuff we do all the time and the kind of stuff we're trying to build platforms to support in different areas. Let me show you the starter code. I hope you can see my screen.

**Daniel Lopes:** So essentially, the way we're thinking about the business, we have this layer of general AI workflows that we can use for content creation, recruiting, sales, anything. And on top of that, we're building a lot of platform stuff related to marketing.

**Daniel Lopes:** So content creation, content draft creation, and then humans in the loop to improve things. We also generate illustrations, images, FAQs, whatever you might need around content creation. One of the things we do a lot is take an article — either one we wrote from scratch or a client's article — and generate an in-brief, like a TLDR at the top. We also translate things to different languages. Some LLMs do a good job, and there are dedicated translation services, but for this exercise you can just use an LLM to translate to Spanish. And another thing we do quite a bit is fact-checking. Sometimes we perform it with LLM, and sometimes we extract the things that could be fact-checked by a person and give them to somebody to do the work. Over time we're going to build more stuff around those things, but these are the core things we do with content creation.

**Daniel Lopes:** And today, the project would be creating a pipeline that can do these three things.

**Daniel Lopes:** And I have here some suggestions for how to do it.

**Daniel Lopes:** So the first thing would be, let's assume the input is a URL, and you receive a URL as an argument.

**Daniel Lopes:** It's number one there.

**Daniel Lopes:** And then you use, I'll send you the Notion document after.

**Daniel Lopes:** And then you have GINA. If you haven't had a chance to play with it, essentially it takes any URL you pass and converts it to Markdown — like this Wikipedia article on prompt engineering. If you want to use other things instead of GINA, you can, but that's what we use for most of our scraping stuff.

**Daniel Lopes:** For crawling we use some other stuff, but for scraping use GINA.

**Daniel Lopes:** Then we create the in-brief — ideally two to five bullet points capturing key insights from the article. So step one is fetch, step two is create the in-brief, step three is do the Spanish translation. One thing that's challenging for us with translation is URLs — if you don't specify in the prompt not to translate URLs, you'll just get 404s. I've noted that in the assignment. Then fact-checking — we extract things that could be fact-checked.

**Daniel Lopes:** The fact-checking prompt is tricky, so I included the prompt already in the project. There's a starter kit — the zip file I sent you — with boilerplate stuff and the fact-checking prompt already included. Essentially, the idea is that we pass the content to the LLM to extract statements, statistics, code — anything that's binary and either true or false. It returns a JSON object with things to be fact-checked and why, so humans can review it. We can add UI on top to help humans review it, or have an LLM review it itself later. For the result, you don't have to build UI or an API — just save the output as a JSON file to disk. I've included code for that. If you're using something like Cursor, you can dump the code and ask it to read it and generate a decent README as an extra thing.

**Daniel Lopes:** The project structure is set up with TypeScript with dependencies already in the package.json. It has a src folder, a .env file with boilerplate to load it, a prompts file, and a utils.ts file where you can put logic to save things to disk. We can switch to GPT-4 or use GPT-4o — both work well. We have an OpenAI API key set up. Sometimes the API key expires, so I just created a new one. It should be good, but if you hit problems let me know. We also use Zod for schema validation. The reason we use it is to make sure the response always matches the expected format.

**Ben Church:** Right, you can use it for structured responses from the API — you just define what response you expect upfront.

**Daniel Lopes:** There's a link in the Notion doc to an OpenAI example. They have a helper for Zod inside their SDK. You just define the object and pass it to their function, and it will make sure responses always match that format. Another thing we do — but it's optional — is liquid.js for interpolating variables in prompts. Sometimes you want to conditionally add to the prompt depending on whether a variable is present or not. It's a bonus thing, and the logic is also in the boilerplate code if you want to use it. This is what we use in production.

**Daniel Lopes:** The execution is just a script — you run npm start and pass the URL you want to process through the pipeline. The output would be something like this, but it could differ based on your preference.

**Daniel Lopes:** There's a cursor rules file in the project that will help with some of the code and testing. There are also some test URLs you can use — you don't have to find your own. How you want to do this is up to you. If you want me to be live and pair program, we can do that. Or if you want to work alone since I personally don't do well with someone looking over my shoulder, we can turn off the camera and I'll be available on chat and audio to help.

**Ben Church:** I'm similar. I'll clarify a couple of these requirements, walk you through my general process, then go camera off, share my screen, and get at it.

**Ben Church:** How's that sound?

**Daniel Lopes:** Sounds good. I'm sending you the link so you can download the zip file. Let me know if it works for you. I'll post it in chat.

**Ben Church:** Great.

**Ben Church:** Great, I can see the link. That's awesome. I'll bookmark it. Let me download the zip file and open it. I'm going to move it to my development folder under repos so it's in a proper spot. I'll rename it to growthx-project. Let me start sharing my screen now.

**Ben Church:** So first thing to clarify — as I understand it, we're doing a few generations in sequence from one source: grab the article, make a brief for it, translate it, and extract facts. Those can all be parallelizable, which is good, but for time purposes I'll add that optimization at the end if I have time. For translating content, we only want to translate the content, not the brief.

**Ben Church:** Is that right?

**Daniel Lopes:** Yeah, we could start with just the content.

**Daniel Lopes:** Otherwise, it will be a blocker, like it would be not paralyzable.

**Daniel Lopes:** OK, great.

**Ben Church:** Storage-wise we're just using JSON — it's mostly a CLI script. We don't need to worry about a database, so I don't need to figure out Prisma again. That's handy. I'll need to update Node to 22 though.

**Ben Church:** When extracting fact-checkable statements, you mentioned claims and statistics — is it useful to make subcategories, or can I just consider all facts the same?

**Daniel Lopes:** Can you open the prompt? It's in this folder, inside the src folder.

**Ben Church:** Got it. Let me look for it. I'm opening the growthx-project folder now.

**Daniel Lopes:** This is the first time I'm using TypeScript for production in a long time. Some of the boilerplate stuff is not super great — the way we have some of the package.json set up.

**Ben Church:** I see good typing in there. Where's the prompts file?

**Daniel Lopes:** So the fact-checking prompt — that's the output. If you just write a paragraph, keep it super simple. You can extract anything that's factual and populate that part with whatever LLM logic you want.

**Ben Church:** Cool. I tried a tool last night called SuperWhisperer. Have you used it?

**Daniel Lopes:** I haven't, but some folks here use it.

**Ben Church:** I created a mode for it — a prompt optimizer that does meta-prompting. You give it a prompt and it improves it. I think it could be useful here.

**Daniel Lopes:** We have a Cursor rules file for our projects that does that, but it's not in this one.

**Ben Church:** And then you said use liquid.js for templating?

**Daniel Lopes:** Yeah, if you check the utils folder, we have the rendering logic there. If you want to use liquid, you can, but you could also just do JavaScript string interpolation if you prefer.

**Ben Church:** Yeah, the agent should be able to figure that out.

**Ben Church:** So, process-wise, I'm going to take some notes on my approach. First, I'll set up some documentation files and doc sources — probably for GINA AI, OpenAI, and structured responses. The rules look pretty good, I'll do a pass over them. Then I'll create some utilities around GINA AI and OpenAI. I'll add some tests to confirm they're working. Then I'll set up the debugger so I can pause and step through. I'll add a test entry point so I can iterate quickly — run and confirm, run and confirm. Then I'll do a first pass at the main logic and prompts.

**Ben Church:** Cool.

**Daniel Lopes:** That all makes sense.

**Ben Church:** Doesn't seem too crazy, but let's see when we get in here.

**Ben Church:** The debugging step might take longer than I expected. I ran into issues yesterday with attaching the debugger — I'd set breakpoints but it wouldn't attach properly.

**Daniel Lopes:** Yeah, that's the only thing we want to change in this project later — add Vite so we can do just-in-time TypeScript compilation. Breakpoints would work better in that setup.

**Daniel Lopes:** Let me know if you have any questions. If you want to turn off the camera and mic, I'll be in chat. Usually people spend about an hour on this. We've already spent quite a bit of time, so I want to make sure we have enough time for questions. I don't have a hard stop. Maybe 50 minutes of coding time works? You don't have to finish everything — it's more to see how you think and your approach. We're trying to build a pipeline that can handle dozens of these kinds of workflows.

**Ben Church:** That sounds perfect. I'll turn off my camera now.

**Ben Church:** One more thing — I might use Cursor's agent mode to set up some of that, though I know that's not what you're evaluating me on.

**Daniel Lopes:** Agent mode has improved a lot since we tested it at the beginning of interviews. Sometimes it can overdo things and generate code you have to delete, but that's part of it. The important thing is that you understand what's happening, not just that code gets generated.

**Ben Church:** Right, I'll understand what's going on. I'll turn on the debugger since I can skip that setup step with an agent if needed.

**Daniel Lopes:** All right, sounds good. See you in a bit.

**Ben Church:** See you in a bit.
