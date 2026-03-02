# GP + Daniel + Marcel

<metadata>
date: 2025-11-07
time: 19:30 UTC
duration: 105 minutes
organizer: daniel@growthxlabs.com
participants: Marcel Santilli, Gianpiero Puleo, Daniel Lopes
fathom_recording_id: 100149593
fathom_url: https://fathom.video/calls/466492537
share_url: https://fathom.video/share/FVRNgZTszSezU6xs7KZjAsKYdzoi5rLz
source: fathom
enriched_on: 2026-03-02 03:45 UTC
</metadata>

---

## Summary

Marcel, GP, and Daniel reviewed GP's agent prototype — an MCP server integrated with Atlas to orchestrate workflows and solve the "blocking chat" problem that standard clients cannot handle — and concluded it was technically sound. They then pivoted to the core business issue: current prescriptive writing guidelines are failing clients through generic, context-insensitive content, causing churn. The team agreed that fixing writing style is the top priority this cycle, and decided GP should lead development of a new "Memory Bank" system that replaces rigid rules with curated examples and an example-based wizard for generating dynamic style guides. Daniel will direct the CheckThat team to focus on the prompt screen and data table, and will interview the former Jasper Head of AI for insights on the style problem.

---

## Context

This is a strategic planning meeting between GrowthX's key leadership and product development team. Marcel Santilli (external founder/advisor perspective, but marked external in the system), Gianpiero Puleo (GP, core engineer leading prototype work), and Daniel Lopes (CTO/product decision maker) are aligning on the company's next engineering focus. The backdrop is that GrowthX has been developing agent-driven workflow infrastructure using MCP servers and Atlas, with GP leading a proof-of-concept prototype. However, the bigger business problem emerged: their core B2B content marketing service is losing clients because of a fundamental unsolved challenge — how to make AI-generated content consistent, on-brand, and contextually appropriate. Current writing guidelines are too prescriptive and rigid, causing agents to produce generic or tonally inappropriate content (e.g., "quantify everything" rules making sophisticated content sound salesy). This meeting represents a pivot from pure infrastructure work toward solving the writing style problem as a core product differentiator and business blocker.

---

## Relevance

**To GrowthX Delivery & Core Product:**
- Writing style is the primary cause of current client churn — clients are leaving because AI-generated content doesn't match their voice or brand, regardless of research quality. This is a blocking issue for scaling the service.
- The new "Memory Bank" system shifts from prescriptive rules to example-based pattern matching, leveraging LLM strengths. MVP includes a workspace wizard that generates dynamic style guides from client reference articles.
- Drafting and post-processing agents will enforce style using curated examples as a "cheat sheet" rather than abstract guidelines, expected to significantly improve content consistency and client retention.
- Content type matters: broad, single-purpose rules (e.g., "quantify everything") don't adapt across different content genres or client personas, which the new system must address through context-aware example selection.

**To Architectural & Infrastructure Decisions:**
- GP's MCP server prototype successfully validates agent-orchestrated workflows, solving the "blocking chat" problem that standard clients (ChatGPT, Claude) cannot handle due to lack of MCP subscription support.
- Atlas frontend enables non-blocking execution with custom notifications, allowing users to continue interacting while workflows run in the background. This is a key differentiation for UX vs. traditional chat interfaces.
- Three layers of agent memory (fixed memory bank for processes/tools/style, transient conversation context, and dynamically retrieved knowledge via tools) provide a cleaner architecture than monolithic context, but style remains an unsolved challenge across the industry.

**To Business & Market Position:**
- The writing style problem is industry-wide and uncracked — none of existing AI competitors (Jasper, etc.) have solved this, creating a genuine product opportunity. Daniel plans to interview the former Jasper Head of AI for competitive insights.
- CheckThat (AI visibility product) requires focused work this cycle: Daniel will direct the team to prioritize the prompt screen and data table UIs over other features like public pages, to ship a focused MVP.
- The pivot to example-based style systems aligns with broader industry movement toward in-context learning and few-shot prompting over fine-tuning, positioning GrowthX ahead of current solutions.

---

## Overview

- **GP's agent prototype is a success.** It validates using an MCP server and Atlas to orchestrate workflows, solving the critical problem of non-blocking execution that standard clients (e.g., ChatGPT) cannot handle.
- **The top priority is fixing writing style.** Current prescriptive guidelines are failing clients by producing generic, inconsistent content. This issue is causing client churn and must be solved this cycle.
- **The solution is a new style system.** It will replace prescriptive rules with a "Memory Bank" of curated writing examples. An MVP will use a wizard to generate a dynamic, example-based style guide for each client.
- **GP will lead the writing style project.** This focus is a strategic shift from the broader agent prototype to deliver immediate business value. Panzer will provide content expertise.

---

## Key Topics

### Problem: Inconsistent Writing Style

  - Current writing guidelines are failing clients, causing churn.
  - **Root Cause:** Prescriptive rules are rigid and don't adapt to context.
      - **Example (Biologica):** A rule to "quantify everything" is applied too broadly, making content sound salesy.
  - **Goal:** Create a system that produces high-quality, on-brand content consistently, regardless of the writer or content type.

### Solution: Example-Based "Memory Bank" for Style

  - The new system will replace prescriptive rules with a "Memory Bank" of curated examples.
  - **Rationale:** LLMs excel at pattern matching. Providing good examples is more effective than giving abstract instructions.
  - **MVP Plan:**
      - **Wizard:** A new workspace setup wizard will generate a dynamic style guide.
      - **Inputs:** The wizard will take reference articles from a client.
      - **Output:** A "cheat sheet" of good/bad examples for specific content elements (e.g., intros, hooks, CTAs).
      - **Execution:** Drafting and post-processing agents will use this cheat sheet to enforce style.

### Prototype: Agent-Orchestrated Workflows

  - GP's prototype validates the technical feasibility of an agent-driven experience.
  - **Architecture:**
      - **MCP Server:** Orchestrates workflows by communicating with both Flow and Output APIs.
      - **Atlas Frontend:** Provides the UI, enabling custom notifications for long-running workflows.
  - **Key Achievement:** The prototype solves the "blocking chat" problem.
      - Standard clients (ChatGPT, Claude) lack MCP subscription support, forcing users to wait for workflows to finish.
      - Atlas enables custom notifications, allowing users to continue interacting while workflows run in the background.

### Decision: GP's Next Cycle Focus

  - GP's next cycle focus was decided by prioritizing the writing style problem.
  - **Option 1 (Chosen):** Lead the writing style project, building the "Memory Bank" MVP.
  - **Option 2 (Deferred):** Continue the broader agent prototype.
  - **Option 3 (Deferred):** Assist the Check That team.

---

## Action Items

- **GP:** Lead development of the writing style "Memory Bank" MVP.
- **Panzer:** Provide content expertise for the style system.
- **Marcel:** Continue research on agent architectures and context engineering.
- **Daniel:**
    - Interview the former Jasper Head of AI for insights.
    - Direct the Check That team to prioritize the prompt screen and data table.

---

## Transcript
**Marcel Santilli:** This meeting is being recorded.

**Marcel Santilli:** How's it going?

**Gianpiero Puleo:** Hey, Marcel.

**Gianpiero Puleo:** Good.

**Marcel Santilli:** How are you?

**Marcel Santilli:** Pretty good, man.

**Marcel Santilli:** Where in this beautiful world is GP?

**Gianpiero Puleo:** GP is in Portugal, probably for the last, what is it, five days or so.

**Marcel Santilli:** It's Lisbon, Porto, or where?

**Gianpiero Puleo:** We made home base in Lisbon, but then we've done, like, you know, one week we went and stayed left in the north another couple of days away.

**Marcel Santilli:** So Lisbon was sort of like the, yeah.

**Marcel Santilli:** Yeah, yeah, that's cool.

**Marcel Santilli:** You guys gone to Algarve?

**Gianpiero Puleo:** No, just only because we've been already.

**Gianpiero Puleo:** Like we had a, we had a summer vacation there, so we wanted to see stuff that we hadn't seen before.

**Marcel Santilli:** Nice, nice.

**Marcel Santilli:** Did you ever go to Madera?

**Gianpiero Puleo:** No, I wish.

**Marcel Santilli:** No, that was too, too long of a flight for just a, Like we did our honeymoon in, started a honeymoon in Oktoberfest in Germany, and then went to Lisbon, then drove down to Algarve, then took a flight to Madeira, then took a flight from Madeira to Porto, and then went to Porto and finished in Amsterdam and flight back to Assafs.

**Gianpiero Puleo:** That was our honeymoon.

**Gianpiero Puleo:** Super cool, super cool.

**Gianpiero Puleo:** No, Madeira now.

**Gianpiero Puleo:** It's definitely, that and the Azores, I think, are two things that I would like to.

**Marcel Santilli:** Do you like wine?

**Gianpiero Puleo:** Do you drink wine?

**Gianpiero Puleo:** Yeah.

**Gianpiero Puleo:** I don't know that.

**Marcel Santilli:** I just, I like asking now, because like nowadays.

**Marcel Santilli:** Some people don't drink at all, so it's almost like, how dare you sit and drink.

**Gianpiero Puleo:** I figure you did, but I just didn't want to assume.

**Gianpiero Puleo:** No, actually, I'm not exaggerating.

**Gianpiero Puleo:** I don't think there's been one day that we didn't drink.

**Marcel Santilli:** So the central market, what's it called?

**Marcel Santilli:** You know the little market in Lisbon that has a bunch of the food things?

**Gianpiero Puleo:** Yeah, it's that time-out market that you were talking about.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** So there's, like, this little place that has all the wines?

**Gianpiero Puleo:** Yeah, I've been, I've been.

**Marcel Santilli:** Have you been?

**Gianpiero Puleo:** Okay, so they have these crazy old, like, Madeira wines.

**Marcel Santilli:** They're, like, I don't know, like, 40, 50 euros, like, for one little shot thing.

**Marcel Santilli:** Have you had those?

**Gianpiero Puleo:** No, but what I did, so I don't think I told anyone, I think, but last month, my father had a heart surgery.

**Gianpiero Puleo:** I don't know.

**Gianpiero Puleo:** I don't think I told you guys.

**Gianpiero Puleo:** It's all good.

**Gianpiero Puleo:** But yeah, like, a quadruple bypass.

**Gianpiero Puleo:** Like, we got him, like, he passed, basically, one day he passed out, so he got to the hospital, and then whatever caused, like, passing out had nothing to do, actually, with his heart condition, but because they couldn't find what it was, because I think he just had, like, a drop in pressure or something, like, then they randomly found out that he had a heart problem.

**Gianpiero Puleo:** Luckily, the heart itself was actually in, still in perfect condition, but his coronaries were kind of all clogged, so he had a quadruple bypass.

**Gianpiero Puleo:** So, why am I telling this?

**Gianpiero Puleo:** Because you were asking about Madeira.

**Gianpiero Puleo:** So, my father is from 1954, so since we kind of saved him for, like, like, it was really close.

**Gianpiero Puleo:** So, at one of those shops that you're mentioning, I got a bottle of Madeira from 1954, which is when he was born, and I, and and I, and I, and brought it to him, so, we had, like, a little glass together with, uh, with some of the pastilles in the hotel.

**Gianpiero Puleo:** Yeah.

**Marcel Santilli:** Perfect time.

**Marcel Santilli:** So our neighbor opened this bottle of, no, it was a Madeira, I think it was a port wine, it was a vintage one, and I think it was like over 200 years old.

**Marcel Santilli:** It's so insane, like these wines, like essentially you can't age them forever.

**Gianpiero Puleo:** But anyway, I'll shut up now, Daniel's like, what the  are you guys talking about?

**Marcel Santilli:** But if go to that store, it was super cool, because like, you know, like you're not going to open, like if you buy a like $3,000 bottle of Madeira, you're not just having it randomly, you got to finish drinking, you can't open it.

**Marcel Santilli:** So it's cool, because like, you can literally just have a thing, you would never, yeah.

**Gianpiero Puleo:** They told me, I don't know if it's true, because I, Madeira is like a bit new for me, but they told me that compared to port wine, Madeira is different because of the climate, like where, and the fact that it was always traveling on, like on ships, etc.

**Gianpiero Puleo:** Even if you open it, like, it, like, it can stay there forever, basically.

**Gianpiero Puleo:** Like, it, really.

**Gianpiero Puleo:** Like,

**Gianpiero Puleo:** Doesn't matter.

**Gianpiero Puleo:** Like, that's what I've been told.

**Gianpiero Puleo:** But with that said, like, we also had a relatively new wine shop close to where we stay.

**Gianpiero Puleo:** Like, we just went in randomly once.

**Gianpiero Puleo:** They have, like, a huge selection of absolutely everything.

**Gianpiero Puleo:** And then what they install are those machines that you go there, like, with their card, and you can just try, like, a different bottle.

**Gianpiero Puleo:** So, yeah, we've done that a couple of times.

**Gianpiero Puleo:** And they add a station that is just, like, Ports and Madeiras and Muxcatel.

**Gianpiero Puleo:** think it's here, like, also pretty good.

**Gianpiero Puleo:** All right.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** We're done.

**Gianpiero Puleo:** We're done online.

**Gianpiero Puleo:** We're done online.

**Marcel Santilli:** Thinking out that he's in Portugal, and I wish I was in Portugal.

**Daniel Lopes:** Let's not talk about agents.

**Marcel Santilli:** Completely different topic.

**Daniel Lopes:** For today, I was just thinking, like, inviting Marcel here, because I know you've been working on the MCP stuff.

**Daniel Lopes:** And, like, trying to figure out a potential...

**Daniel Lopes:** Essentially, the reason why we've been doing this, Marcel, just to give a little bit of context, is that we talked about what if the experience was more like menace or more like cloud code where you can go back and forth.

**Daniel Lopes:** don't have to worry about what kind of workflows are available or how do you set up these things?

**Daniel Lopes:** Can I do in plain text and all that kind of stuff?

**Daniel Lopes:** So we kind of like set GP in this like random direct exploration, like can you see how hard it would be for us to have MCPs that trigger our workflows and if they would pass the right data and how far we from that?

**Daniel Lopes:** And then also like what could be the experience, but no like expectation of like we got to ship something this month.

**Daniel Lopes:** So it's more like two weeks and something like to figure that out.

**Daniel Lopes:** Because I think that would be like a mind-blowing experience later down the road.

**Daniel Lopes:** Let's say we're defining content types like we were talking about yesterday in the car where you could just have anything.

**Daniel Lopes:** To create this saying, how do I do it?

**Daniel Lopes:** Just write it, you know, and then you're having plain text, and then you execute the output to you do whatever you want with it, you know?

**Daniel Lopes:** So that's kind of like why JP was on this project, and just for us to see it, you know?

**Daniel Lopes:** So if could just walk us through that.

**Daniel Lopes:** And then another thing that I don't know what would be the best reason for the second half of this call, but there's two things.

**Daniel Lopes:** Like we have the next cycle starting Monday, and we have check that.

**Daniel Lopes:** Check that is high priority.

**Daniel Lopes:** We want to ship it this month.

**Daniel Lopes:** The guys there are like strong, like Stavum is really good on front end.

**Daniel Lopes:** We could use, probably could use more help on the front end too.

**Daniel Lopes:** We're going to have Jacopo join, and we have Peter.

**Daniel Lopes:** So I was thinking like these three guys can probably ship this, but you have a business perspective as well, JP.

**Daniel Lopes:** Like you jump on things and you connect the dots really well.

**Daniel Lopes:** Marcel is going to be helping there, but maybe having you full-time could help.

**Daniel Lopes:** Another option would be like, have you helped.

**Daniel Lopes:** That's also a gnarly project of so many areas.

**Daniel Lopes:** every time we put things together, keep finding more edge cases.

**Daniel Lopes:** And I'm thinking from the UI side there, having you there would help.

**Daniel Lopes:** So I can just do a bunch of things quick and give it to you and you can finish it.

**Daniel Lopes:** And you can get it to the actual final thing where I'm just vibe coding a  ton of mockups.

**Daniel Lopes:** So that's another area.

**Daniel Lopes:** So we have this.

**Daniel Lopes:** And then one more thing that's high priority for the business, too, is that everybody struggles with setting up writing guidelines.

**Daniel Lopes:** And that has such a huge impact that we're essentially losing clients left and right because of that.

**Daniel Lopes:** And it's essentially hard for prompt engineering that is basically a mini reinforcement learning.

**Daniel Lopes:** Like it's not like you can't let people do that manually.

**Daniel Lopes:** Like they will just like write the wrong examples and all that.

**Daniel Lopes:** There are so many best practices baked into that, that in my mind, that we might need a wizard, you know, like similar to what you did, where like you'd break it down to like, like we need to figure out a different system there, I think, at least for writing guidelines.

**Daniel Lopes:** So those are the three things that are on my mind.

**Daniel Lopes:** I know you can talk about that, figure out how we handle that.

**Daniel Lopes:** Yeah, personally, I'm open to any of them.

**Gianpiero Puleo:** So like they're all fun projects from my perspective for different reasons.

**Gianpiero Puleo:** So, you know, we can, yeah, we can go through this stuff and then like discuss where you guys would like to, for me to spend the next cycle.

**Gianpiero Puleo:** And as I told you also, like, you know, depending on the workload, for example, the spike itself was, because it was a prototype, wasn't taking my full time.

**Daniel Lopes:** That's why I was also able to stay on analytics and do stuff.

**Gianpiero Puleo:** So, so for me, the next cycle is the same, like, I have to even to be on two things, depending on like the nature of the, of the two projects.

**Gianpiero Puleo:** it's, it's, it's, it's, it's, it's, Thank you.

**Gianpiero Puleo:** But regardless, just in case we want to bring this forward with the infra team, when Ben came back, I actually gave him a walkthrough of the MCP server and everything.

**Gianpiero Puleo:** So he has at least the gist and his access to code, cetera, in case you want that team to continue working on this stuff.

**Daniel Lopes:** Perfect.

**Daniel Lopes:** Cool.

**Daniel Lopes:** All right.

**Gianpiero Puleo:** Sounds good.

**Gianpiero Puleo:** Okay.

**Gianpiero Puleo:** So I don't know what the...

**Gianpiero Puleo:** Let me give you, before I show you anything for your context also, Marcel, a bit, what I've done to you, Daniel.

**Gianpiero Puleo:** think I told you already to a certain extent, but I think it's better if I give at least a summary of how I approach the thing, and then I can show you where I am.

**Gianpiero Puleo:** So Daniel's context for me was like, is there a better experience that might replace how we do pipelines?

**Gianpiero Puleo:** Potentially kind of discussing with an agent, et cetera.

**Gianpiero Puleo:** And so I started looking into...

**Gianpiero Puleo:** What the infer team was doing with outputs, because the goal of that framework is for us or agents to be able to execute workflows a lot more seamlessly than we can do in flow.

**Gianpiero Puleo:** But then I wasn't sure like whether it would be something in Atlas, something potentially like that works directly with cloud code or whatever.

**Gianpiero Puleo:** And so that's why I started from an MCP server, because once I had the MCP server in place that can communicate and work with both output, but also flow, then we can use that anywhere.

**Gianpiero Puleo:** So, for example, first I tried it a little bit directly into cloud, and I made quite a bunch of progress there.

**Gianpiero Puleo:** But then the main blocker that I found with any of the existing clients, so this is true for everything, like cloud code, for chat GPT, for cursor, they don't, even though the MCP protocol supports subscription,

**Gianpiero Puleo:** To resources, meaning that we start to workflow and then our workflows are pretty long.

**Gianpiero Puleo:** And so we don't want to have a blocking experience where basically then your chat is just stuck like for 20 minutes with the, you know, the LLM like that keeps like checking and checking and checking and you cannot do anything else.

**Gianpiero Puleo:** So I needed a mechanism to say to when the workflow is done or fails or anything, so it's going to be notified back into the chat so that it can continue from there.

**Gianpiero Puleo:** So MCP, the protocol supports that, but apparently, unfortunately, no client has implemented it yet.

**Gianpiero Puleo:** And so that's why then I went the route of instead building something in Atlas, where instead we can then catch our own notifications and update things as they go.

**Gianpiero Puleo:** So, so, so, yeah, I think maybe I can show you our works in Atlas.

**Gianpiero Puleo:** Keep in mind, just the caveats, like one, as Daniel said.

**Gianpiero Puleo:** This is sort of like prototype level, not production code.

**Gianpiero Puleo:** So I'm pretty sure stuff will break as I show.

**Gianpiero Puleo:** And also, even from an experience perspective, like I focused for now on kind of more proof of concept, I'm making sure that things like the pieces can work together.

**Gianpiero Puleo:** So let me share my screen.

**Gianpiero Puleo:** And then also one question, do you want me to, or Marcel actually, actually it's a question for both.

**Gianpiero Puleo:** Like you want to know anything else about the technicalities of it or just see how it works?

**Daniel Lopes:** Like I'll leave it to you if guys tell me.

**Daniel Lopes:** Yeah, yeah.

**Gianpiero Puleo:** Okay.

**Gianpiero Puleo:** So for now, I put it here, like AI works just an answer point.

**Gianpiero Puleo:** Nice.

**Gianpiero Puleo:** But essentially in the space, what we will want is an area where essentially we have the chat and then there's going to be like a checklist.

**Gianpiero Puleo:** of, like, how the agent has come up with the plan that needs to be executed.

**Gianpiero Puleo:** And then, like, the running workflows, you can run multiples, et cetera.

**Gianpiero Puleo:** So let's say that I start and say, hey, I want to write a blog post explaining the concept of semantic chunking.

**Gianpiero Puleo:** So the backend is all done with Ruby LLM.

**Gianpiero Puleo:** So you can see that it's, like, creating the content plan.

**Gianpiero Puleo:** So it's having a plan mode and an act mode.

**Gianpiero Puleo:** So right now we're in plan mode.

**Gianpiero Puleo:** So the way that I designed this from a system perspective is that we have one or more, however we want, MD files.

**Gianpiero Puleo:** So I wanted to take the same approach that we have, for example, with things like Cloud Code.

**Gianpiero Puleo:** So in those MD files, we have a basic plan.

**Gianpiero Puleo:** And so that's.

**Gianpiero Puleo:** That's what this is using.

**Gianpiero Puleo:** Like once you say that you want to generate content, the basic plan is starting point.

**Gianpiero Puleo:** But then for example, let's say, so it says research and planning, content creation, and a cover image.

**Gianpiero Puleo:** So for the sake of argument, let's say, let's say this looks good, but what options do we have to create images?

**Gianpiero Puleo:** And so this is now, again, using the MCP servers.

**Gianpiero Puleo:** The MCP server is actually communicating with Flow, and it will go and find basically anything that we support for content creation.

**Gianpiero Puleo:** It recommends using this one with Recraft.

**Gianpiero Puleo:** I don't know actually how it makes its choice.

**Gianpiero Puleo:** I mean, that's the thing with agents.

**Gianpiero Puleo:** I'm not sure.

**Gianpiero Puleo:** Let's say, what was the chat GPT one?

**Gianpiero Puleo:** Let's say, I got it used.

**Gianpiero Puleo:** So when we do that, it will update the plan, as you see, like, it changed, like, the to-do list and how it's going to do.

**Gianpiero Puleo:** And you can do that with pretty much any step in there.

**Gianpiero Puleo:** So, again, this is what's, it's based on the MD file that I will show, like, in a bit.

**Gianpiero Puleo:** And then I would say, I don't know, at this point, I'll say, I could say, like, yes, looks good.

**Gianpiero Puleo:** So, let's start.

**Gianpiero Puleo:** And at this point, hopefully, it would switch into execute mode.

**Gianpiero Puleo:** And then it's going to start with find workflow to know exactly what parameters, because everything is going to be dynamic, like, it could find.

**Gianpiero Puleo:** And as you see, now it started the research workflow.

**Gianpiero Puleo:** So it's in there.

**Gianpiero Puleo:** What you see here is the problem that I was in the middle of.

**Gianpiero Puleo:** start.

**Gianpiero Puleo:** So, So, let's

**Gianpiero Puleo:** Trying to solve, which is, you know, you give it instructions not to do so, like at times, we'll just keep checking, like whether or not it's finished, whether or not it's finished, whether or not it's finished, and we don't want that.

**Gianpiero Puleo:** But again, like, I think what you see here is anyway, the skeleton and the sort of the scaffolding of how this thing can work.

**Gianpiero Puleo:** And based on what I'm seeing, like, I don't see any particular reason why this will not be able to kind of craft any sort of plan or kind of complex workflow.

**Gianpiero Puleo:** So, because what we give from the flow API and output API is, like, accepted information that the agent needs because there's a catalog of workflow.

**Gianpiero Puleo:** I implemented, like, the search tool so that it can go and look for workflows by keywords, et cetera, but then it gets accepted the schema that needs to be invoked, et cetera.

**Gianpiero Puleo:** And so I think everything that we build on top of

**Gianpiero Puleo:** It's just to make the experience better, things like what's going on here that we don't want, but in terms of like being able to construct and then execute and run and manipulate the workflow, I haven't really seen any reason that we wouldn't be able to do it.

**Gianpiero Puleo:** So I'll stop here at least for how things work and then, so yeah, questions, et cetera, then I can show a little bit of the code in the configuration as well if you want.

**Daniel Lopes:** That would be cool, but one thing that I'm thinking as you showed me this is like the content type, because that's one of the things that I've been thinking about, like how do we abstract pipelines so they are not, you don't have to like view them.

**Daniel Lopes:** We could come with like pre-baked content types, and the pre-baked content types are essentially a simple plan and the task checklist already predefined.

**Daniel Lopes:** So it would be, you open it.

**Daniel Lopes:** Like a content type, let's say it's like a glossary, and then you'd have a quick research with PurpleXity, and then write in this format of like some data that we pass for the brief, and then from the brief, the draft team this certain way, and then you open it, and that's like, if you just execute, you will run.

**Daniel Lopes:** So if you don't go into plan mode and you just execute, you could run, but you could iterate on a plan in this form, you know.

**Gianpiero Puleo:** Yeah, I mean, as long as you stay in plan mode, and again, like you can think if that's the mental model that we want, but for example, while you stay in plan mode, like you can iterate on the plan as much as you want, and you can keep switching between plan and execute.

**Gianpiero Puleo:** So I think it's completely up to us how we think that the conversation is better.

**Daniel Lopes:** Yeah, and then you could say that as a template, you know, because kind of similar to the, I don't know, like that guy that we're interviewing, although like, more about winter.

**Daniel Lopes:** Winter.

**Daniel Lopes:** Winter.

**Daniel Lopes:** He kind of came up with similar idea, like repeatable conversations.

**Daniel Lopes:** So we could essentially save the to-do list as like a template.

**Gianpiero Puleo:** And that's like a new kind of like workflow, next workflow.

**Gianpiero Puleo:** In the meantime, it seems that research task is done.

**Gianpiero Puleo:** So if I even fetch results again, like there's workarounds at this point, but essentially the research workflow has completed, so you can go and get the output.

**Gianpiero Puleo:** It marks the first step is done.

**Gianpiero Puleo:** And so it gets like all the context, of course, in terms of the research and moves on to the second step and, you know, so on and so forth.

**Gianpiero Puleo:** So again, like I think the wiring is all there.

**Gianpiero Puleo:** I think if we were to move from prototype to, you know, to production code, obviously we can make this like a lot more solid, but I think the pieces work.

**Daniel Lopes:** and

**Daniel Lopes:** Like, think, like, we could have, like, our, like, sanctioned workflows in this workspace.

**Daniel Lopes:** And then later on, if we'd ship, like, a registry of workflows, anything that you choose from the registry could be, like, called from here, you know?

**Daniel Lopes:** That kind of, like, experience.

**Gianpiero Puleo:** Yeah.

**Marcel Santilli:** Yeah, like, this is awesome.

**Marcel Santilli:** Well, one thing that I was just trying to figure out is, like, the, I'm very early in this, but just studying a lot of, like, context engineering and kind of how Menace does it, how Claude does it versus how, like, you know, cognition does it versus how Cursor does it.

**Marcel Santilli:** And, you know, like, it's, and I don't think anyone has to stand the level of depth that we have on words.

**Marcel Santilli:** Like, everyone is doing it for, for, like, code.

**Marcel Santilli:** So, like, I started playing, for example, with, like, Claude Code, and I'm like, hey, I'm going to write a study guide for Claude.

**Marcel Santilli:** For context engineering, right?

**Marcel Santilli:** So I created a folder.

**Marcel Santilli:** I gave it a set of links that I wanted to do.

**Marcel Santilli:** I said, okay, now let's create a folder called this, scrape all of this and put it here.

**Marcel Santilli:** It already started faking.

**Marcel Santilli:** And then I was like, okay, I'm going to put a scratch pad over here.

**Marcel Santilli:** And then I want you to think about this.

**Marcel Santilli:** And I was like, oh, my God, this is going to suck.

**Marcel Santilli:** This is horrible.

**Marcel Santilli:** It's not great with that because it's not set up for that, right?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And then Manus is really freaking good.

**Marcel Santilli:** Like, when I tell it to just, like, I want you to go and do this crazy thing, and then I want you to put it into a database, and then I want you to store it in this way, and it just does it, and it works for 30 minutes.

**Marcel Santilli:** It's, like, the most reliable one I've ever seen, right?

**Marcel Santilli:** Like, it's also, like, one of the best experiences by far.

**Marcel Santilli:** Like, and then you can see, like, how, like, essentially, ChatGPT with HMO, and I just played with it this morning, is, like, way behind.

**Marcel Santilli:** And it's just, like, the only give you, I have the next plan, and it only gives me, like, 40 credits a month.

**Marcel Santilli:** And then I'm, like, wow, like, you're super behind, you're still .

**Marcel Santilli:** Like, you know, and it's, like, super basic and whatnot.

**Marcel Santilli:** And then you ask all these experiences to do a research mode, and it takes, like, 20, 30 minutes.

**Marcel Santilli:** And then it gives you, like, the summary that's just, like, so, like, not, like, great.

**Marcel Santilli:** Like, the cloud is getting better, but, like, the deep researcher and all these experiences is, like, pretty meh, you know?

**Marcel Santilli:** But then, like, it really struggles to, like, figure out, like, all my preferences and context and essentially, like, you know, figure out, like, what to put and whatnot.

**Marcel Santilli:** And so, like, all of this to say, I think men is the best experience for, like, if you want to go into agentic mode, agent mode, right?

**Marcel Santilli:** None of the deep researchers are, like, really great.

**Marcel Santilli:** Like, they're good, but they just overdo it and, like, and then it's just, like, okay, you have 140 sources.

**Marcel Santilli:** Like, how do you, like, start asking questions of those sources?

**Marcel Santilli:** You know, it's, like, just not a great.

**Marcel Santilli:** Great experience, you know, and I think, like, for us, this connects back to the context piece, right, like, the artifacts, the writing guidelines, and things like that.

**Marcel Santilli:** It's like, I think we need to crack that, because I'm not concerned that, like, this experience, we can't get to an amazing experience.

**Marcel Santilli:** Like, you already have a prototype.

**Marcel Santilli:** It's like,  yeah, this is awesome.

**Marcel Santilli:** But it's just like, it's gonna, like, we gotta figure out, like, how, like, you know, how to, because there's, like, the knowledge of the project.

**Marcel Santilli:** Overall, right, like, which is the workspace, right?

**Marcel Santilli:** Then there's, like, all these other things, like, like, Daniel mentioned, like, that it might be related to the content type.

**Marcel Santilli:** might be, like, what knowledge to fetch, what, how do you know when to go enrich that knowledge and add more knowledge, and, you know, how do you plan it?

**Marcel Santilli:** How do you think through the tool calling, like, that I think if we nail it on, like, a piece of content, you know, and, like, prototype it within, like, one piece of content, maybe, like, because otherwise we might be at risk of, like, creating this amazing experience.

**Daniel Lopes:** That still results in, like, mediocre content, essentially.

**Daniel Lopes:** I think, Marcel, like, the way I think about it, like, this, like, experimented the, I agree with everything you said, but, like, this thing that GP did was more, like, is how possible would it be for a registry?

**Daniel Lopes:** Let's say we put Clint to rebuild the thing that he did with, like, workflows, and we have a marketplace of, like, sanctioned workflows, and we have our, like, microagents for, like, deep research that's content-focused.

**Daniel Lopes:** We have, like, a draft team that's, like, article-based.

**Daniel Lopes:** Like, we have all those things that we are, like, now people can use in cloud, can use in, like, and they don't even have to use content to us, but we get paid to the pass-through API calls or something like that.

**Daniel Lopes:** Like, how hard it would be to, like, build an MCP, and is our framework metadata structure that the guys are putting together enough to, like, build an app store with, like, the catalog, the descriptions, and all that?

**Daniel Lopes:** So, that valid.

**Daniel Lopes:** I think this validates that really well, and now we have to go back to like, because GP was involved with the search that Peter was working on, and now this work here, I think it's the perfect segue for us to think about what are the kind of context that we need, and I think we need, and I don't think that's different in our projects is that we need repeatable things, you know, where many, all these agents are beautiful, like everything time you join, you want something different, you know, in our case, it's like, we want you to follow a  to-do list, you know, and that to-do list can't deviate, or we have no normalization on the articles that get produced, or things like that, but there's almost always like, you free form for a bit, and like, you explore, and then you do like, okay, now this is the rubric, or like, this is the checklist that has to be performed, so that's another thing that's a challenge that our environment has, and the other environments don't have, like, they don't have we're producing we're

**Daniel Lopes:** So, but I think just like, and there's different kinds of context as well.

**Daniel Lopes:** So there's the context that's like, yes, you must know.

**Daniel Lopes:** And that's like the writing guidelines and like the core stuff.

**Daniel Lopes:** Like I think there was, in my mind, a brand kit, whereas like the company context, maybe personas are dynamic and they can be chosen differently on each piece.

**Daniel Lopes:** And then you have core writing guidelines and then you might have adjacent writing guidelines for whatever kind of content you're writing.

**Daniel Lopes:** So, and like to me, though, like that has to be, we had to learn that really well.

**Daniel Lopes:** It's almost like the Cloud MD on a project or the system prompt for this project out there.

**Daniel Lopes:** And like every client would have their own.

**Daniel Lopes:** And then we have the dynamic context that you have to do depending on the task, you know.

**Daniel Lopes:** It's kind of all kind of related.

**Marcel Santilli:** Yeah, that makes sense.

**Marcel Santilli:** Sorry, one second.

**Marcel Santilli:** All right, can you guys hear me okay?

**Daniel Lopes:** Yep.

**Marcel Santilli:** Yep.

**Marcel Santilli:** There's, like, contractors, like, making a lot of noise.

**Marcel Santilli:** I had to put it, but then my headphones, like, every time I talk, it mutes you all.

**Marcel Santilli:** So then I can't hear what you're saying if we're kind of, like, talking.

**Daniel Lopes:** I have a contractor with a leaf blower, right?

**Marcel Santilli:** Outside of my wheelchair.

**Marcel Santilli:** That makes a lot of sense.

**Marcel Santilli:** And, yeah, for me, I'm kind of, like, the way my brain works, it's kind of, like, I need to visualize it all, you know?

**Marcel Santilli:** And so I don't know if it could, like, almost, like, wideboarding in a fig jam a little bit of, like, okay, we're thinking, like, there's, like, the, like, to-do over here.

**Marcel Santilli:** And then, like, there's the project-wide, like, context.

**Marcel Santilli:** Is there, like, a caching or short-term piece?

**Marcel Santilli:** Is there, like, what is we consider context?

**Marcel Santilli:** Like, what is tool calling to a workflow?

**Marcel Santilli:** What do we consider a workflow?

**Marcel Santilli:** Because, like, some workflows are gnarly, they're going to take 50 minutes, right?

**Marcel Santilli:** Like, and then others are, like, really just, like, one little tool, right?

**Marcel Santilli:** Like, you know, like, is any of this, like, sub-agents, or is it mostly, like, you know, agentic, but, like, single agent, right?

**Daniel Lopes:** Like, there's a lot of those things that, like, yeah, but anyways, this is awesome.

**Marcel Santilli:** So I don't want to distract from, like, the progress here.

**Gianpiero Puleo:** no, it's super useful.

**Gianpiero Puleo:** mean, that's where we, that's where we need to go, like.

**Marcel Santilli:** Like, what I'm struggling with, personally, is that, like, when I'm writing a memo, I use everything, right?

**Marcel Santilli:** I try Cloud Code, I use Cloud, I use Cloud Projects, I use Skills, I can use this, I use Atlas, and it's just, like, it's so much  work to get it to sound like you, and then you're, I'm trying to bring, like, research in, like, right now, it's a great example.

**Marcel Santilli:** I'm trying to create a study, like, guide on context engineering.

**Marcel Santilli:** And I want to feed it some sources.

**Marcel Santilli:** I'm like, here's like 10 sources that I really want you to focus on.

**Marcel Santilli:** Enrich a little bit more.

**Marcel Santilli:** And I'm like, okay, now I want you to just create this temporary database that I can fetch from.

**Marcel Santilli:** But by the way, I want you to keep in mind how I want you to sound, essentially my guidelines of how I want to sound.

**Marcel Santilli:** And now I want to just work through the plan and shape it.

**Marcel Santilli:** Let's start with the intro.

**Marcel Santilli:** Okay, let's do this.

**Marcel Santilli:** And that experience is really hard.

**Marcel Santilli:** And all of them are different abstractions and they were purpose-built for different things.

**Marcel Santilli:** And none of them were purpose-built for learning and writing, essentially.

**Marcel Santilli:** And that's why they all struggle with it.

**Gianpiero Puleo:** Yeah.

**Gianpiero Puleo:** Because I think that the issue, for example, that someone like you would have with something like Atlas is that the pipeline is predetermined and it's always linear and that's not how you're working.

**Gianpiero Puleo:** But if instead we have this agent that can coordinate subagents, but each subagent is, let's say, specializing to one particular part of the process, then you can collaborate with the orchestrator.

**Gianpiero Puleo:** But then the orchestrator has access to all the different workflows, the different tools, and it pulls it in as needed, including the context.

**Gianpiero Puleo:** So for me, when I say just, I don't mean like, oh, it's super simple.

**Gianpiero Puleo:** I'm saying it's simple but not easy.

**Gianpiero Puleo:** Like, it's simple in a sense that it's that wideboarding exercise that you talk about, where we basically decide, like, what are the Lego blocks that we need to have at our disposal every time during this process.

**Gianpiero Puleo:** And then I think in the beginning, probably we'll need to be like, there's going to be like a little bit of trial and error to understand like how the agent reacts and orchestrates those things.

**Gianpiero Puleo:** But the reason why I was showing this file here is because I took this approach from a tool called Client, which Daniel knows because since he hired me, I keep kind of bringing it up.

**Gianpiero Puleo:** But it's because I think they really nailed, like for me, using Client is the one that I find the most reliable of all the tools like Cursor and other subagents, et cetera, in terms of following your instructions.

**Gianpiero Puleo:** And the reason why they do it is because they do a few things.

**Gianpiero Puleo:** They have this switch between plan and execute, which now pretty much everybody has.

**Gianpiero Puleo:** Then they have this concept of like a memory bank.

**Gianpiero Puleo:** Like in a memory bank in the project has like specific MD files for a specific concept.

**Gianpiero Puleo:** So like if I had to make a parallel with our system, we would have like.

**Gianpiero Puleo:** Like an MD that is specifically, let's say, the information about the brand.

**Gianpiero Puleo:** One MD that is specifically the information about whatever artifacts we have, et cetera.

**Gianpiero Puleo:** And because then each sub-agent works with the context of a particular MD, it can be a lot more precise because you remove all the added noise.

**Gianpiero Puleo:** And so, like, finding the right decomposition, I think that's probably where we're going to have to put more work for the system to work the way that you're imagining.

**Gianpiero Puleo:** That's the least I'm thinking about things right now.

**Marcel Santilli:** Okay, so, can you help me?

**Marcel Santilli:** Okay, so you have a memory bank, but then how do you, I don't know, if these systems or, so plan versus execution, that makes sense.

**Marcel Santilli:** Memory bank, I want to dig in, but then how do we think about context versus knowledge?

**Marcel Santilli:** Like, meaning, like, what's stored in a knowledge base, for lack of a better word, right?

**Marcel Santilli:** Like, permanent memory or whatever, you know.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like, memory or knowledge.

**Marcel Santilli:** knowledge.

**Marcel Santilli:** Versus what's like project context versus in-session context versus like short-term quick context that you pull like, you know, like, have you thought about that or?

**Gianpiero Puleo:** Yeah, for me, there's three layers.

**Gianpiero Puleo:** I don't know if the terminology is correct here, but what goes into the memory bank, so to speak, that's stuff that doesn't change often.

**Gianpiero Puleo:** So that's where you model your process, like you kind of like dictate how we want to work on stuff, what each piece does, etc.

**Gianpiero Puleo:** And it also contains instructions in terms of like when to go and look at other contexts.

**Gianpiero Puleo:** So then there's the transient stuff, and that's just the conversation.

**Gianpiero Puleo:** And there's knowledge, and the knowledge instead is the one that you get through the tools.

**Gianpiero Puleo:** And like in the memory bank, essentially, you have like, for example, what you see here, what you see here, not in this form necessarily, but this to me is an example.

**Gianpiero Puleo:** Or what you would put in the memory bank.

**Gianpiero Puleo:** Because we want, that's our process.

**Gianpiero Puleo:** Like, yes, we can iterate on it, but that's our process and we start from here.

**Gianpiero Puleo:** So then if I were to kind of keep working on this, there would be, let's say, one, like another piece of memory bank, which is specifically about research.

**Gianpiero Puleo:** And in that piece of memory bank, then we would have instead, what tools do you have at your disposal?

**Gianpiero Puleo:** When do we want you to kind of go and retrieve knowledge and from where?

**Gianpiero Puleo:** And then the knowledge stuff instead is the one that is completely dynamic and that's why it's retrieved to a tool.

**Gianpiero Puleo:** Because then we can play like we're having it through a RAG system or any other like mechanism at that point we will find.

**Gianpiero Puleo:** So that's how I'm thinking about knowledge in those three pillars.

**Gianpiero Puleo:** So memory bank, it's relatively fixed.

**Gianpiero Puleo:** That's how we shape the system.

**Gianpiero Puleo:** Then the transient is like what's kept in memory through the conversation, very short term.

**Gianpiero Puleo:** And then knowledge is like getting fetched on a need basis, but with clear instruction.

**Gianpiero Puleo:** From the memory bank, again, like it doesn't matter what we call it, like for the sake of this discussion.

**Daniel Lopes:** Yeah, and in my mind, the knowledge base that we have today, it would be the knowledge base that we have in Atlas, it would be a tool to be used as knowledge, or like long-term knowledge.

**Daniel Lopes:** And then you have the memory bank, to me, it would be like how we need to reshape the artifacts.

**Daniel Lopes:** And like some of these memories are so important that they need guidance when you're creating the memory.

**Daniel Lopes:** And then you have the transient stuff would be, if you were in, let's say you're in the assignment project, and you were creating an assignment for a new article, the brief would generate, and then if you have feedback for the briefs, like, oh , I don't like this, I don't to change it.

**Daniel Lopes:** That would be the transient conversation of the system, like iterating on the brief.

**Daniel Lopes:** And then if you have a draft out and you...

**Daniel Lopes:** Okay, like I want to make the intro shorter, like in this article, the persona is someone else, like that would be also like transient.

**Daniel Lopes:** So the chat we have in the sidebar would be that building this like temporary memory, the knowledge base is the vault that has a light graph, and then the context artifacts are the memory bank, like just relating to the architecture that Chippy is talking about.

**Daniel Lopes:** That's how I see the, and then we're kind of going that direction now already, and I can do it, you guys are like framing it in a better way.

**Marcel Santilli:** Yeah, so just to understand, okay, so I'm just doing this, sorry, I'm like a visual person, so if it doesn't connect, I'm just confused as , like in, here, let me add you guys to this.

**Marcel Santilli:** Okay, invited you guys, let me copy the link here.

**Marcel Santilli:** the here.

**Marcel Santilli:** Okay.

**Marcel Santilli:** This, okay, so let me know if you guys can, can you all see this?

**Gianpiero Puleo:** Almost there.

**Gianpiero Puleo:** One second.

**Marcel Santilli:** Okay, so I'm just trying to understand.

**Marcel Santilli:** Okay, so what pieces are missing here?

**Marcel Santilli:** Or, so, there's, like, a chat.

**Marcel Santilli:** Like, can you add me just, like, put all the building blocks here so I kind of understand a little bit?

**Gianpiero Puleo:** Yeah, just one question for me, Marcel.

**Gianpiero Puleo:** Like, when you say the pieces, like, are you thinking, because you mentioned chat, for example, are you thinking you retrieve the pieces of, like, you know, the user experience or, like, more from a model perspective or both?

**Marcel Santilli:** Yeah, think of this as more of, like, within one, let's call it a chat or, like, right?

**Marcel Santilli:** Like, if you start a new Manus chat, like, and you give it a task and it executes.

**Marcel Santilli:** Like, and all the way to completion, like, what is the, like, architect's architecture, essentially, of, like, the primitives that are used, or the, like, to make that experience work, essentially, you know?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And so it's not, like, the UI by any means, it's just mostly, like, what's a context, what's a brief, what's a to-do, like, you know, I'm trying to understand, like, because we're using a lot of, like, different terms, and so if we can at least, like, put it all there, and then start to define it together, then at least we'll refer to the same things in the same ways, and then we can, like, then, like, have a, at least a shared understanding of, like, does that make sense?

**Marcel Santilli:** And then, tell me if it's a waste of time, but it's just, like, for me, it will help me understand how we're thinking about things, you know?

**Gianpiero Puleo:** No, for me, no, absolutely.

**Gianpiero Puleo:** For me, it's not a waste of time I'm happy to go through this.

**Gianpiero Puleo:** It helps me think as well, and probably will reveal stuff that I didn't think about.

**Gianpiero Puleo:** Thank you.

**Gianpiero Puleo:** So I'm also going to talk as I do, because like I'm thinking out loud with you guys as I, so this orchestrator agent for me, that's your interface.

**Gianpiero Puleo:** So that's the entry point, like all the pieces that we're going to design now for me, like you as a user, don't interact directly with them.

**Gianpiero Puleo:** Like you interact with your orchestrator agent.

**Gianpiero Puleo:** Like this is not to say that in Atlas you couldn't go and do stuff directly in knowledge base, but ultimately if the pieces are there, you don't want to go, you don't want to have to go there and mess with them.

**Gianpiero Puleo:** So then in the memory bank, like what I put there is like process tools and style.

**Gianpiero Puleo:** So process is like to me, how we do things.

**Gianpiero Puleo:** Like that's a starting point, you know, like we can iterate on that, but that's sort where we codify how we do things.

**Gianpiero Puleo:** So tools is like what.

**Gianpiero Puleo:** Things can you do, and what, you as in, sorry, you, the agent, what are the things that you can do, what are the things that you can talk to, what are, what's the information you can go and retrieve.

**Gianpiero Puleo:** And then style, to me, is like everything that is a little bit more intangible, but specific to our work process, so like.

**Marcel Santilli:** Like preferences?

**Gianpiero Puleo:** Can you give me an access?

**Marcel Santilli:** Oh, sorry, you have two, you must have two different emails on Figma.

**Marcel Santilli:** I added one, but.

**Daniel Lopes:** Flex, sorry, I am.

**Marcel Santilli:** Yeah.

**Daniel Lopes:** So now style, Fathom Labs.

**Gianpiero Puleo:** And more specifically, that everything has to do with tone of voice, branding, how we write, et cetera.

**Gianpiero Puleo:** Because, to me, that's something that I don't think is, like, as you said, for example, if this thing is writing things for you, I don't think.

**Gianpiero Puleo:** think you're going to want to like constantly, like once you nail your style, to me that becomes a piece of information that is like consistently there for all the work.

**Gianpiero Puleo:** And it's not something that keeps changing and you need to kind of go and retrieve with tools like somewhere else.

**Gianpiero Puleo:** That's why I put it there.

**Gianpiero Puleo:** It's also very specific because we're talking about writing content.

**Gianpiero Puleo:** Like obviously this wouldn't be as important if you were doing kind of different type of work, like I don't know, where it's coding, et cetera.

**Daniel Lopes:** But I think for writing content.

**Daniel Lopes:** That is the thing that I think the parallel here is very similar to the differences between cursor and cloud.

**Daniel Lopes:** And cursor works better for fixed work if you have a cursor rule.

**Daniel Lopes:** So you always load the cursor rules in memory in the chat all the time where cloud might not.

**Daniel Lopes:** So that's why I have like code getting generated now by the team on the client ops side that doesn't really follow the best practices of the framework.

**Daniel Lopes:** Power is to we were switching to cloud.

**Daniel Lopes:** we You

**Daniel Lopes:** To me, that's where the distinction would be.

**Daniel Lopes:** So if we have this environment to create, let's say styling is one of the core things that we want to do as a memory fix.

**Daniel Lopes:** And that's why I think the context artifacts we have today, we need to evolve it.

**Daniel Lopes:** So we have some kinds of artifacts that are never not included.

**Daniel Lopes:** And those are the things that might vary.

**Daniel Lopes:** I think style is super broad.

**Daniel Lopes:** you have four things that you cannot talk about.

**Daniel Lopes:** We cannot talk about Bolt, for example.

**Daniel Lopes:** There are certain things that are like you never mentioned Vibe coding in a negative way.

**Daniel Lopes:** So there's some core things.

**Daniel Lopes:** The name of a company is X.

**Daniel Lopes:** You can't not remember that.

**Daniel Lopes:** And then you have things that are specific to that task that might need a different memory that you don't forget as well.

**Daniel Lopes:** And that would be like, if I'm writing a newsletter, the transition between sections doesn't

**Daniel Lopes:** matter as much, or like I'm not as opinionated as if I'm writing like opinion piece, you know.

**Gianpiero Puleo:** So what I added there then is the external knowledge.

**Gianpiero Puleo:** So to me, external knowledge, which you access through tools, is completely dynamic and fetched on a new basis.

**Gianpiero Puleo:** And I think in the memory bank, you dictate how that happens.

**Gianpiero Puleo:** I'll give you a concrete example for me in my own workflow.

**Gianpiero Puleo:** One thing that I hate when I do coding with agents is that because they have memory of code from like some months or years ago, they don't know like if the APIs have changed, et cetera.

**Gianpiero Puleo:** So for example, in my own memory bank, I wrote that every time they in plan mode, they need to design something that uses an external API, they need, like the agent has to go and fetch the latest documentation on Context 7.

**Gianpiero Puleo:** So that, to me, is an example of, like, the rule that you must look at Context 7 when you work with external API, it's in the memory bank, because that's part of how I want to work.

**Gianpiero Puleo:** But then Context 7 is the equivalent of our knowledge base, but for coding, in the sense that there's a tool to the MCP, the agent goes there and fetches the latest API with examples for pretty much like any external API that is out there.

**Daniel Lopes:** So to me, this should use Context 7 for our, we should have a workflow with Context 7 for code fact checking.

**Daniel Lopes:** That's, in fact, I don't know if you saw my comment on Slack, sorry, this is a tangent.

**Gianpiero Puleo:** Like, but yeah, I found that the fact checker is not performing very well with the technical stuff.

**Gianpiero Puleo:** And, in fact, like, what I did is using Context 7 a lot, like, after the article is finished, then I do, like, ulterior fact checking and refining using Context 7 and other stuff.

**Daniel Lopes:** So, but yeah.

**Gianpiero Puleo:** That's a good example.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Okay.

**Gianpiero Puleo:** And I mean, ultimately, for me, like, at a high level, these are the pieces, Marcel.

**Gianpiero Puleo:** Then I think we can decide where we put certain things, like, I don't company information.

**Gianpiero Puleo:** To me, it's probably, in my view, it's probably memory bank, but it depends, like, to me, there's a world in which, like, this is your agent, and you can use this one agent to work for any client that you want, or the agent is sort of, like, associated to a workspace and a client, et cetera, and that's, I think, a different setup, because then I think that dictates a little bit where you put some of that knowledge, if that makes sense, because if it's your agent that can work with absolutely anything, then probably we access, like, I will.

**Gianpiero Puleo:** Consider client and project information external knowledge, but if it's associated to a workspace and client, then to me, it's part of the memory bank.

**Gianpiero Puleo:** Does that make sense?

**Gianpiero Puleo:** you see why I'm saying that?

**Marcel Santilli:** Yeah.

**Daniel Lopes:** I think in our context, it's almost like we should always be thinking client first.

**Daniel Lopes:** So, like, this is almost for the same reason that we were talking about today in the analytics, as in, like, ideally, this is all client stuff.

**Daniel Lopes:** That's where everybody struggles.

**Daniel Lopes:** Like, you're producing content for a client.

**Daniel Lopes:** If you're content-focused, we should start with the clients first, and then you can add your personalization as a user of that client later, you know?

**Daniel Lopes:** But nobody should be like, oh, , like, somebody's using a different version of a writing guidelines for this client, you know?

**Gianpiero Puleo:** Because it's a different...

**Gianpiero Puleo:** No, for clients' work, we shouldn't.

**Gianpiero Puleo:** I think maybe when I think about you, Marcel, the situation is a little bit different because I think you also use that one for content that you write, I would imagine.

**Gianpiero Puleo:** So not just for content that you write for clients, or am I mistaken there?

**Marcel Santilli:** Yeah.

**Daniel Lopes:** But he's like, that is the same.

**Daniel Lopes:** Like in my mind, to me, when I write on our blog, I still work for GrowthX.

**Daniel Lopes:** And like if I'm writing on my LinkedIn, same thing.

**Daniel Lopes:** So that's why I have a personal writing guideline on our workspace.

**Daniel Lopes:** That's how I write.

**Daniel Lopes:** And then I have the company one.

**Daniel Lopes:** So if I'm writing for the newsletter, I want to load the company one.

**Daniel Lopes:** But if I'm writing perspective, I load my one, you know?

**Daniel Lopes:** So writing under GrowthX.

**Daniel Lopes:** Marcel, when he's blogging on LinkedIn, he's still thinking he's writing for us, just writing at his own way of writing, you know?

**Marcel Santilli:** Yeah, that's why like, they're up here.

**Marcel Santilli:** I was like...

**Marcel Santilli:** Global workspace user versus task, like, I think there's, like, different, you know, pieces to that, like, and the parameters might be the same, but there's, like, different, there's things that are global, there's things that workspace, there's things that are user-related, there's things that are, like, task-related, maybe, you know, I don't know if task is the right thing, or even conversation-related.

**Marcel Santilli:** I don't know if task conversations are different here, or, you know, like, like, like, it's a session, like, an agent session, like, you know, maybe it's, like, a session instead of task, even, you know, like, and, yeah, and that, like, what I'm trying to figure out, like, like, let give an example, right, like, in my, my mind, like, biological, right, there's all these amazing sources that we're pulling every time we do a research, and over time, like, like, I, there's,

**Marcel Santilli:** There's knowledge storage, right, where I'm putting that there, but, like, there's patterns that you're starting to learn about, like, these are the types of sources that are good, and they're already there, right?

**Marcel Santilli:** Like, and I'm enriching them, and I'm learning and, like, extending that knowledge, essentially, right?

**Marcel Santilli:** Like, it's not just, like, what you fetched and stored.

**Marcel Santilli:** It's, like, you're, like, enriching it so that, like, you can learn more.

**Marcel Santilli:** Like, essentially, like, I think Tiago, like, who's, like, was talking about how they did it for DataGraphs, like, knowledge extension or call this something else, right?

**Marcel Santilli:** Like, I think we do something similar for how we store it or whatnot, but, like, there's things there, and then when you're in a session like this, like, hopefully, like, you're fetching external, but you're checking here as well, and then, like, you're pulling just what you need in memory, and then there's, like, the active memory versus almost, like, inactive memory, maybe, of, like, within that, because, like, if you just make everything active, then you're , right?

**Marcel Santilli:** Like, so, yeah, so that's what I'm trying to, like, kind of figure out is, like, the, like...

**Marcel Santilli:** How do we think mentally about it?

**Marcel Santilli:** Because, like, you said, like, for example, the tool calling makes sense, right?

**Marcel Santilli:** Like, everything is a tool calling, MCP, like, that makes sense.

**Marcel Santilli:** But then it's, like, the to-do versus, like, the style for it.

**Marcel Santilli:** You call it style.

**Marcel Santilli:** Like, is that a preference?

**Marcel Santilli:** Is that, like, a context?

**Marcel Santilli:** Is that, like, a user?

**Marcel Santilli:** You know, like, trying to understand, like, how do we define that?

**Marcel Santilli:** And where does that store?

**Marcel Santilli:** Is that store, like, in constantly changing or, you know?

**Marcel Santilli:** And then there's, like, the content itself, right?

**Marcel Santilli:** Like, which is, like, what we haven't talked about, but it's, like, the actual output itself, right?

**Marcel Santilli:** Output might be a brief.

**Marcel Santilli:** Output might be the draft, like, you know?

**Daniel Lopes:** To me, like, I think there might be two different kinds.

**Daniel Lopes:** That's the thing that I'm coming to with, like, if we have to redesign the whole context of Apples today.

**Daniel Lopes:** To me, there's, like, clear, distinct things that are, like, preformed memories.

**Daniel Lopes:** that you should know about, that are fixed.

**Daniel Lopes:** And that's like, oh, proofreader checklist is one of those things.

**Daniel Lopes:** Another one might be like, here are all the docs from Sentinel-1 or for Clark.

**Daniel Lopes:** It's not, yeah, I don't want you to be ragging different docs.

**Daniel Lopes:** I want you to always know about this, like a cheat sheet.

**Daniel Lopes:** And I've heard of the top projects we care about, like fixed memories or some important stuff.

**Daniel Lopes:** But then style is so specific.

**Daniel Lopes:** The way you write style, to me, is an uncracked challenge that none of the agents can do it right.

**Daniel Lopes:** And that's why our writing guidelines are so impactful.

**Daniel Lopes:** And to me, writing, because our stuff is so dependent on writing, that the writing style is a unique thing, in my mind.

**Daniel Lopes:** And it will vary.

**Daniel Lopes:** So it's almost like a context for writing style somewhere here.

**Daniel Lopes:** That's why I was thinking the writing guidelines should be, it's a subsistence of our existence.

**Daniel Lopes:** Today, that will vary depending on what you're writing.

**Daniel Lopes:** It has a specific way of writing.

**Daniel Lopes:** Like, you have to, like, I think it's all prompt engineering, but the prompt has to be dynamically built, not manually built.

**Marcel Santilli:** I think, maybe, but, like, I was using the, like, the Atlas, right?

**Marcel Santilli:** I like to do research on this stuff, right, which is kind of cool.

**Marcel Santilli:** It's, like, the deep researcher is great, right?

**Marcel Santilli:** And it's going through, like, if you get to the end of it, the, like, it will, it's almost like you have a reference point as a guideline, right?

**Marcel Santilli:** But then there's so many things that are coming into play for this specific task or whatever that you're working on, right?

**Marcel Santilli:** Right?

**Marcel Santilli:** That it's just like a reference point, right?

**Marcel Santilli:** That you're pulling, but you're going to have to adapt so much that it's almost like it's a reference point that then an agent is going to need to figure out how to adapt it and pull it into the memory bank or something, right?

**Marcel Santilli:** Like, because it's just so different.

**Gianpiero Puleo:** Are you talking, sorry, Marcel, are talking about figuring out how to pull in the results of the research into the memory bank?

**Marcel Santilli:** Is that what you're saying?

**Marcel Santilli:** Or even how to sound, right?

**Marcel Santilli:** Like, because, like, like, every time, like, I give it, like, a set of instructions on styles, like, this isn't Claude, this is everywhere, right?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** The same set of instructions might work one time, and then you do another session, and you use the same set of instructions, but with slightly different contacts or slightly different things you're It's just, like, horrible.

**Daniel Lopes:** And it's, like, oh, , garbage.

**Daniel Lopes:** That's why I'm saying that the problem there is that now you're in a different environment, and you don't have examples for that.

**Daniel Lopes:** And it doesn't know how to behave in that environment.

**Daniel Lopes:** Or so it's...

**Daniel Lopes:** It's biased based on the examples you had before.

**Daniel Lopes:** It's almost like you have to keep building the style.

**Daniel Lopes:** So you have to be constantly, almost as reinforcement learning loop, but it has to be, it's its own thing.

**Daniel Lopes:** essentially, I don't know the solution here, if it's reinforcement learning or prompting engineering.

**Daniel Lopes:** And I think first we should start with prompting and have dynamic prompts.

**Daniel Lopes:** So if that happened in an ideal scenario, you would have the instructions, you don't have to see the instructions.

**Daniel Lopes:** You'd say, well, now this sounds wrong with this article.

**Daniel Lopes:** And then you just make a comment and it would like, okay, I'll add these.

**Daniel Lopes:** How do you want me to sound here?

**Daniel Lopes:** And it would add, and if you want me to sound like an example in every situation, yes.

**Daniel Lopes:** And then there will be, every situation gets similar to this, you say yes.

**Daniel Lopes:** And then it adds to the exemplars table, you know?

**Daniel Lopes:** And then if that exemplars and the prompt becomes too long, then you can start doing like fetching in chunks of like, then you can break that down, the whole giant style thing for that person or their client to give it.

**Daniel Lopes:** Finding the chance, the same way that Claude will grab the codebase, while Cursor will do GraphNet navigation on the codebase, or read the codebase.

**Daniel Lopes:** Eventually, we'll have to figure out that.

**Daniel Lopes:** Because today, one of the problems we have, the silos are getting so long, based on just people editing them manually.

**Daniel Lopes:** That, to me, is such a unique problem, how you sound, nobody's cracked that.

**Daniel Lopes:** And, and that's how I'm thinking, like, the writing guidelines is the place to start thinking about it, and we need that now.

**Daniel Lopes:** But I was like, we have a entire system, I think it doesn't make sense.

**Daniel Lopes:** We're plucked out the writing guidelines, and we're thinking about style, how do we solve it, you know?

**Gianpiero Puleo:** Because we need that system.

**Gianpiero Puleo:** might be a fair take on that one, Daniel.

**Gianpiero Puleo:** It's not completely different, but it's, I think it might be a little bit more towards what you were saying, Marcel, if I don't misunderstand you.

**Gianpiero Puleo:** Like, to me, where I found better results is not with prompts.

**Gianpiero Puleo:** better Thank you.

**Gianpiero Puleo:** So for me, the reason why the writing guidelines are becoming so long is because we're using them as prompts.

**Gianpiero Puleo:** And instead of what I found, for me, like my experience, what I found working better is having prompts just from the perspective of, like, again, orchestration, what to go to look and where, because the LLM is really good at pattern matching.

**Gianpiero Puleo:** So to give you an example, let's say, Marcel, if you, instead of those writing guidelines, like you said, you have the writing guidelines, you bring them to another project, and, like, they give you, like, a slightly different result.

**Gianpiero Puleo:** If, instead of that, you just had, like, a prompt that is, like, look at this four MD files, and those four MD files are four articles that you wrote, and then, basically, the prompt is just try to match them in style as close as possible.

**Gianpiero Puleo:** For me, that actually, I noticed a lot better.

**Gianpiero Puleo:** And an example of that goes with what you were saying too, Daniel, which is when you build more of that, like in a code base, the more your code is consistent in a certain style, like whatever DLM produces that is new, becomes more and more like adherent to the code style that you already have in the code base.

**Gianpiero Puleo:** So this is not to say that we don't need any sort of like rules slash prompts, but I think for me, we haven't used enough of like examples that DLM can pattern match on.

**Daniel Lopes:** I'm kind of like, don't think about prompt as like us writing the prompt.

**Daniel Lopes:** I'm thinking more about like, it's.

**Gianpiero Puleo:** Yeah, yeah, but what I'm saying is like.

**Daniel Lopes:** It's just like in context learning, like I'm talking more about in context learning versus fixed versus model learning and DLLM stuff.

**Daniel Lopes:** Like if you ask to like, look at this four articles, we'll look at the four articles every time different.

**Daniel Lopes:** But if you do a, I think we need to have like a post-processing, you know, and as this, like, if it was random, like code is kind of random.

**Daniel Lopes:** And like, in the terms of code, it has so much knowledge of that already.

**Daniel Lopes:** So like, OpenAI will perform better with Python.

**Daniel Lopes:** And that was the first thing that they baked it.

**Daniel Lopes:** So it's baked into your knowledge.

**Daniel Lopes:** So it even knows what's the definition of a function.

**Daniel Lopes:** In our case, it kind of doesn't know what's the definition of a good hook on an intrap, for example.

**Daniel Lopes:** So it doesn't know what's the definition of a...

**Daniel Lopes:** Model training, though, that's different.

**Daniel Lopes:** Yeah, but like, think like, before you do model training, I think you can do in-context learning if you do post-processing.

**Daniel Lopes:** So we could do like, here's four articles.

**Daniel Lopes:** Then we have a pipeline under the hood that will convert those four articles into like examples where in-context learning are effective.

**Daniel Lopes:** And so we will translate like four articles that are like 5,000 words each or combined to translate into 500 words.

**Daniel Lopes:** They're precisely described.

**Daniel Lopes:** Like books, CVAs, lists, like this kind of content, you know?

**Gianpiero Puleo:** When I said that we have like 4MD files, I don't think they need to be like each of them, like a realistic, like full-length article.

**Gianpiero Puleo:** Like they can be like a bunch of paragraphs that are written though exactly in the style that we need.

**Gianpiero Puleo:** What I'm saying though, even if the prompt is dynamic, I think there's a different performance, which I think we could test and like and see if we actually notice anything different there because it might just be like my bias.

**Gianpiero Puleo:** But there's a different performance coming up with like even dynamically with a prompt that says you should write like this, this, and that, as opposed to here are these four examples of good writing and we want just matching.

**Daniel Lopes:** I think we should, should not have that kind of prescriptive, that's the problem of our writing guidelines today.

**Gianpiero Puleo:** That you should have just examples.

**Daniel Lopes:** What I'm saying is we should reduce the writing guidelines and switch things.

**Gianpiero Puleo:** Provide examples of what we want and let the LLM do the pattern matching.

**Daniel Lopes:** Yes, exactly.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** It's essentially we turn the articles or people's references into proper examples that are bucked in the right places, and then we let the LLM handle it.

**Daniel Lopes:** That's exactly how you're thinking.

**Daniel Lopes:** And to me, that's the difference why Cursor is so much better at, like, today still at, like, performing consistent things because they do rag the code base semantically in different areas.

**Daniel Lopes:** So, like, they will look at your packages and they will look at your RouseFile or NextGen different, you know, while, or MakeFile, while Cursor, Claude would just, like, chunk the files.

**Daniel Lopes:** And, like, use the Claude ideas of, like, I kind of like trying to figure that out, and then I would chunk as I go, you know?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So, there's no pre-processing.

**Daniel Lopes:** Pre-processing.

**Marcel Santilli:** Yeah, like, in a...

**Marcel Santilli:** I think, like, we need to, like, translate that equivalent to what we're doing.

**Marcel Santilli:** Like, right, like, if there's, like, a different programming language or a different file type or whatever, like, for us, like, this is an introduction.

**Marcel Santilli:** Introduction is different, right?

**Marcel Santilli:** Like, a headline or, like, formatting is different from, you know, style versus tone versus, like, the, like, sentence structure versus, you know, the persuasiveness of whatever versus, like, the audience.

**Marcel Santilli:** And, you know, I don't know, like, we got to figure out, like, what does that look like and create, like, a semantic layer or, like, a, like, and this is global, right?

**Marcel Santilli:** Like, a global way to just approach it the same way as everybody else does, right?

**Marcel Santilli:** And so that, like, when someone says, remember, I like short sentences better.

**Marcel Santilli:** It's like, okay, like, what does that actually mean, you know, to the system?

**Daniel Lopes:** And I, even in just that example, it would be smart enough to say, okay, I have this collection of.

**Daniel Lopes:** Types of sentences.

**Daniel Lopes:** It's like headlines are for one thing and then like for interests and other things.

**Daniel Lopes:** And then they would be able to say, if that's enough, it would be like smart enough to like adjust the examples for short sentences.

**Daniel Lopes:** But if it was ambiguous, would be able to say, okay, so like, you want me to have shorter headlines or you want me to have shorter?

**Marcel Santilli:** Yeah, like what Harvey does, right, from what I understand, is like they have actually like a lot baked in around like case law and things like that, you know?

**Marcel Santilli:** Right.

**Marcel Santilli:** As far as like how to pull the right knowledge, what to do with it, like how to use it, what not to do, like hard rules and things like that.

**Marcel Santilli:** And like a lot are heartening in some ways, right?

**Marcel Santilli:** And I think like we're having to build that, but it's very different if you're doing research and exploring versus if you're planning versus if you're actually writing, you know?

**Marcel Santilli:** Right.

**Marcel Santilli:** And I think like that is part of like the challenge is like the, like.

**Marcel Santilli:** It's almost like the model for each one of these modes is completely different, but there are global ones that it applies, you know?

**Daniel Lopes:** I think just that's why the pipeline is broken down today.

**Daniel Lopes:** The core agents are research, draft, post-process, and the draft and post-process both know about sentence styling, writing shape, you know?

**Daniel Lopes:** Ideally, we figure out how to do that writing style or formatting, you know, like the model for writing well as a thing that those two can consider, you know?

**Daniel Lopes:** And like today, it's just shoehorning context artifacts, which are essentially just prompts into the core prompt, but that's not the better way of doing it.

**Daniel Lopes:** I think that's like, if that all makes sense, like that is, I think we have to figure that out sooner than later, because that to me is like, the three things that we have, the four things that we have impacted content OS.

**Daniel Lopes:** A lot is lack of the data, lack of pages, lack of opportunities, tracking all that, tracking the work.

**Daniel Lopes:** Analytics is there already, so that we have.

**Daniel Lopes:** The other one is being able to generate high-quality factual .

**Daniel Lopes:** That is working out as well.

**Daniel Lopes:** So that is done.

**Daniel Lopes:** It's just super slow, but we can figure it out over time.

**Daniel Lopes:** And then the third one, how do I sound like a proper person?

**Daniel Lopes:** So we nailed, for example, biological, we nailed the factuality, that's solved.

**Daniel Lopes:** We're nailing the work to be done now.

**Daniel Lopes:** Although we nailed the, we write better than anyone else and you can never match this, that shouldn't be a component on itself that we don't have a good answer.

**Daniel Lopes:** And every time that part is botched, because we didn't set up the workspace correctly, it's a completely disaster.

**Daniel Lopes:** Because the writing guideline was saying things like, it was nothing wrong with the writing guideline.

**Daniel Lopes:** I actually, me show you.

**Daniel Lopes:** you.

**Daniel Lopes:** That's going to blow your mind, but it was well-written, and it's correct, but because of this, it's probably unable to follow them.

**Daniel Lopes:** No, it's following precisely.

**Daniel Lopes:** That's the problem.

**Daniel Lopes:** the first thing is, write as an experience of engineers solving real products, and it says, quantify everything.

**Daniel Lopes:** Show partnership, not sales pitches.

**Daniel Lopes:** And then you have, partnership is here, and it's saying, quantify everything.

**Daniel Lopes:** So it's using this almost everywhere.

**Daniel Lopes:** There's this partnership, quantify everything, and not sales.

**Daniel Lopes:** So this is going every post, and it's becoming super salesy, because it says, quantify everything, show partnership as the first name.

**Daniel Lopes:** So it's doing great, but it's really enforcing it.

**Daniel Lopes:** So there's so many examples of this.

**Daniel Lopes:** And then there's, these things are, they shouldn't be pulled on every article, you know?

**Daniel Lopes:** So there's this, there's the description that we're having, it should be pulled depending on

**Daniel Lopes:** What it needs and all that, we need to figure that out.

**Marcel Santilli:** What would be helpful, I think for me personally, is for us to almost go through and decompose this process with one topic and one client and one thing.

**Marcel Santilli:** And then along the way, step one, this is how it's going to work.

**Marcel Santilli:** then along the way, show in this diagram what is being activated here and where things would go.

**Marcel Santilli:** Because then if we go end-to-end and it was like, okay, cool.

**Marcel Santilli:** Now the system works.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** We don't need to build the system.

**Daniel Lopes:** We're just like, okay, this direction here would go here or something.

**Daniel Lopes:** You know, I'm in a conversation with the guy that was head of AI for Jasper.

**Daniel Lopes:** And maybe you and me can interview him, GP, on this.

**Daniel Lopes:** How would your architect us?

**Gianpiero Puleo:** We have this problem here.

**Daniel Lopes:** And we need to solve this problem ourselves too.

**Daniel Lopes:** So, like...

**Daniel Lopes:** So, like...

**Daniel Lopes:** like...

**Daniel Lopes:** like...

**Daniel Lopes:** you.

**Marcel Santilli:** Yeah, like, I think, like, there's the interesting piece here is that, like, it's almost like the good examples, like, to GP's point, it can be almost, like, universal in some ways and knowing, like, how to pull examples of writing, not for facts, right?

**Marcel Santilli:** Like, you're not pulling content from a knowledge retreat, but, like, it's almost...

**Daniel Lopes:** I think there's layers.

**Daniel Lopes:** I think there's, like, a layer of, like, you are cancer, and, like, everybody should write as well as cancer.

**Daniel Lopes:** And then you have a second layer, like, now you're writing for base 10, and you should know the same, so how base 10 writes.

**Daniel Lopes:** And within that, there was a third layer as well.

**Daniel Lopes:** Now I'm, like, Daniel writing an opinion piece within this.

**Daniel Lopes:** So I should be able to pull, navigate up and down, you know?

**Daniel Lopes:** So, like, if I say, like, I don't give a  about not writing...

**Daniel Lopes:** In a certain way, because that's Panzer style, like I'm writing in my own way, then you should be able to override that, you know, but you should start writing as well as Panzer baseline, you know.

**Gianpiero Puleo:** But that's the part where I'm a little bit confused, though.

**Gianpiero Puleo:** Like, if we're doing it for clients, so that was my, that kind of was my question before.

**Gianpiero Puleo:** So, like, I mean, I understand that if you write or Panzer writes, like you two as two individuals have a different style, but ultimately, what, should take over either of your styles, it is a biologics style.

**Gianpiero Puleo:** Like, when you have content for a brand, the content should be on brand, and it doesn't really matter to a point, like, who's writing it, unless...

**Daniel Lopes:** Yeah, but that's why I'm saying it depends on the content type.

**Gianpiero Puleo:** So, like, so if you're writing, if you're writing a piece...

**Gianpiero Puleo:** That's what I'm saying, not on the person.

**Gianpiero Puleo:** Like, it shouldn't depend on if it's you or Panzer.

**Gianpiero Puleo:** Like, if it's an opinion...

**Gianpiero Puleo:** opinion piece for Biologica, it should kind of sound the same, whether you write it or Panzer writes it, unless you are the CTO of Biologica, and then we want you to have your voice.

**Daniel Lopes:** That's what I mean.

**Daniel Lopes:** So I think we should have GrowthX for writing premises, then you have a client for writing premises, and then you have thought leadership writing premises.

**Daniel Lopes:** And that's where we get the Tribe.ai, we have Marcel writing on LinkedIn, me writing how I think the process of the company should work.

**Daniel Lopes:** That's when I mean that that should override whatever, not criminally override, just take a little bit of precedence over it.

**Daniel Lopes:** You know, and And

**Gianpiero Puleo:** Yeah, I would try to, yeah, but I would try to approach it in, like, for example, I, everything that you said, personally, I would try to nail the, the brand one first.

**Daniel Lopes:** Yeah, I agree.

**Daniel Lopes:** I agree.

**Daniel Lopes:** Yeah.

**Gianpiero Puleo:** And I think there's like a layer on the rest.

**Daniel Lopes:** Yeah, yeah, I agree.

**Daniel Lopes:** I think like landing the brand one is the correct way starting.

**Daniel Lopes:** Like, if we solve that this month, so like something like based in writing guideline doesn't create a completely different outcome than Clark, for example.

**Daniel Lopes:** Even though they're actually, they're describing this, not Clark, but based in, we got which one?

**Daniel Lopes:** We had another GPU one, was Rumpod.

**Daniel Lopes:** The Rumpod outcome is completely different, but they're describing the same stuff.

**Daniel Lopes:** It should have got almost like a similar output, you know?

**Daniel Lopes:** I see.

**Daniel Lopes:** The way it was written there, man holding, it's just up it up, so.

**Gianpiero Puleo:** I see.

**Gianpiero Puleo:** On Biologica, the example that you show me, where you have.

**Gianpiero Puleo:** Those writing guidelines, which ironically became too prescriptive, now he follows it so well that you get that stuff.

**Gianpiero Puleo:** Do we now have biological pieces that we think are well-written, even though we have to kind of do it manually, et cetera?

**Daniel Lopes:** Yeah, we do.

**Gianpiero Puleo:** Yeah.

**Gianpiero Puleo:** That's usually how I do it.

**Daniel Lopes:** When I set up our writing guidelines, I will load a bunch of articles, and I will ask them to create examples.

**Daniel Lopes:** So there's no description.

**Daniel Lopes:** It's just good and bad.

**Daniel Lopes:** So it's essentially interest, good and bad.

**Daniel Lopes:** So I get the client's examples, and they become good, but nothing is prescriptive, saying you must do this.

**Daniel Lopes:** So that's why my writing guidelines tend to work better than the rest of the team is doing.

**Daniel Lopes:** So even the way we do basic things like this would have a significant outcome, I think, create a simple wizard that would take in references of the person, translate that to...

**Daniel Lopes:** The set of examples are written in a way that are not colliding, you know, and the prompt is written in a way that the LLM would be smarter.

**Daniel Lopes:** Okay, like he's talking about interest.

**Daniel Lopes:** I have, you know, this authentic example, so interest will just look at that, you know.

**Daniel Lopes:** LLMs can do that.

**Daniel Lopes:** If we have a giant prompt with like 5,000 tokens or even like 100,000 tokens, they will be able to navigate sort of well, you know, but the tokens don't have to be well written.

**Daniel Lopes:** If it's like a jumbo mess with important exclamation marks everywhere, it will struggle, you know, and that's what's happening now.

**Marcel Santilli:** So I fed this like a researcher and a bunch of stuff on context engineering, plus some of what we were talking about.

**Marcel Santilli:** So this is what I was working on earlier this morning, but then I already had a lot of like the research I was doing on my study guide for context engineering and a bunch of stuff.

**Marcel Santilli:** But I feel like this is getting close.

**Marcel Santilli:** I mean, we got to obviously like work on this a lot more.

**Marcel Santilli:** But, you know, is this, like, roughly?

**Marcel Santilli:** Like, a little bit?

**Marcel Santilli:** I was reading through it, I'm like...

**Gianpiero Puleo:** Yeah, I mean, high-level it is for me.

**Gianpiero Puleo:** Yeah, it has pieces that I didn't think about, like, would that make sense?

**Gianpiero Puleo:** Like, the quasi-cates or the caching strategy.

**Gianpiero Puleo:** But yeah, I think high-level, yes, that's pretty much.

**Marcel Santilli:** One of the things that I was trying to do here, this is why I think it's going to be good to do as well, is, like, I was trying to create these, like, study guides, you know, on, like, different concepts, but then also, like, failure modes and approaches to it as well.

**Marcel Santilli:** Yeah, just started this morning, so I did, yeah, yeah, just, I just started, but, but, like...

**Marcel Santilli:** In here, but pretty much, like, I was trying to find, like, the, I'm trying to find, sorry, like, the different, like, failure modes that it has.

**Marcel Santilli:** Yeah, there you go.

**Marcel Santilli:** Okay, there you go.

**Marcel Santilli:** So first of all, I like, hey, give me, like, doing this, too, right?

**Marcel Santilli:** Like, so I trying to do an analysis, but, but it was kind of, like, wanted to understand, like, what are the failure modes?

**Marcel Santilli:** What are the techniques or patterns or principles, right?

**Marcel Santilli:** Like, and defining some of them, like, for instance, like, context confusion, irrelevant information, the great response quality, blah, blah, blah.

**Marcel Santilli:** And then, like, just started asking it to, like, just kind of go do a bunch of research.

**Marcel Santilli:** But I fed it a lot of, like, what to look at, like, the sources already, you know, which are, like, what everybody else is saying, like, these are the legit ones, you

**Marcel Santilli:** These are like the top ones, but they also contradict with each other on a few things, too, right?

**Marcel Santilli:** Like, for instance, like, they're contradicting on these things, right?

**Marcel Santilli:** Like, offload versus reduced versus retreat versus isolates versus cache, right?

**Marcel Santilli:** Like, and you can see, like, how, like, different ones have different approaches, you know, to certain things.

**Daniel Lopes:** They're kind of how they're...

**Marcel Santilli:** They're different.

**Daniel Lopes:** And, yeah, yeah.

**Daniel Lopes:** And so that's where it's like, we gotta agree on our stuff, too, a little bit.

**Marcel Santilli:** But this plus, like, the Atlus stuff and a few other things, and then started, like, asking questions and did a very bad, like, you know, how would you architect an AI agent for research, blah, blah, blah.

**Marcel Santilli:** then, like, started, like, asking questions and things like that.

**Marcel Santilli:** But because it had already so much research from, like, the good sources, which is, like, essentially trying to pattern match, like, what, you know, ideally, like, we do the deep research on, like, how to curse, like, you

**Marcel Santilli:** Master, Manes, and all of these do context engineering, how do they do memory, how do they do blah, blah, blah, how are they architected, you know, maybe we do something similar for Harvey, and then at least that gives us a lot of the pieces, so as we're thinking about it, it might flag some, not blind spots, but things.

**Daniel Lopes:** the whole system, ideally, this would be under the two new people that we're hiring.

**Daniel Lopes:** It's an applied AI scientist and a dedicated AI engineer, and me and GP would be working on that as well.

**Daniel Lopes:** building the thing on top of whatever they come up with, because this is full-time iteration, you know, like, you have to be, okay, like, oh, , like, we're getting context poisoning here, we need to, like, combat that, or, like, the RA is not good enough for this use case, like, that's, that's a whole team there the whole time, and, and that we on the product side, I think we can't have, we can't start, we must start, and we need to, like, start building it, and we need to, like,

**Daniel Lopes:** Hire these people and have an opinion on who we need to hire out of this.

**Daniel Lopes:** But this process, I think, is the two roles that we're hiring for.

**Marcel Santilli:** And I think for me, it's like just having, for example, like what you built, GPT, as a prototype, right?

**Marcel Santilli:** Which is like, hey, we have a to-do system and we need to have like some kind of memory bank for this or whatever, right?

**Marcel Santilli:** And if we don't have quality gates or whatever, we already have a knowledge base, Like, so it's mostly like an orchestrator agent.

**Marcel Santilli:** So maybe it's like a simple, you're already doing tool calling to work close, you know, like.

**Daniel Lopes:** But I was thinking like, even like now, what we need to do is essentially the memory bank for writing style, you know?

**Daniel Lopes:** And like, and then that replaces our artifacts.

**Gianpiero Puleo:** Here, yeah, all the pieces that you have here, I mean, again, aside from the fact that the code itself needs to be...

**Gianpiero Puleo:** Or production level, not a prototype, but the memory bank is probably the one that we don't have of all of this, specifically for writing content.

**Gianpiero Puleo:** I would say that the Q-system is basic, but it's a sole problem, like a lot of other platforms.

**Gianpiero Puleo:** So the whole system, the memory bank, agree with you, Daniel, is the bit.

**Marcel Santilli:** So just to get practical.

**Daniel Lopes:** Because I'm thinking that the whole system, like the stuff that GP was showing, for it to be like better than Manus, to be better than Claude and all that four-hour space, we would need all the pieces working well.

**Daniel Lopes:** It's very close, all right.

**Daniel Lopes:** So like I think that there are things that we could immediately use, like the MCP things for calling workflows, all that stuff.

**Daniel Lopes:** The stuff that we needed ASAP is how do we get our articles to sound right.

**Daniel Lopes:** And that is part of the whole thing.

**Daniel Lopes:** And like in my mind, ridiculous.

**Daniel Lopes:** Propose that to like, let's try to do the memory bank for writing style this month when we ship it, this cycle, knowing that we're going to get help for the other part.

**Daniel Lopes:** And then like next month or the following month, now we have instead of just GP trying to code all these four things, we have four people on it, you know, like we have him and three more people doing it, you know, and I can help us.

**Marcel Santilli:** Let me just ask, right, like, for me, it's like, even if this thing doesn't work, like, perfect, but all this complexity is tracked that away, essentially, and you have like an AI edit, like this experience plus an AI editor, right?

**Daniel Lopes:** Like, at some point, because like, at some point, the editors are still going to need to like tweak something and give feedback.

**Daniel Lopes:** Yeah, yeah, that would be the output.

**Daniel Lopes:** Yeah, for sure.

**Marcel Santilli:** But even within that, you still want the whole context of the whole conversation, essentially, right?

**Daniel Lopes:** I don't how he arrived at that point.

**Marcel Santilli:** Yeah.

**Daniel Lopes:** Output.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** I think it's what you said, like, import the, I can't remember, like, what you call it, but it's

**Marcel Santilli:** It's like import it into the chat or import the research into like the chat, right?

**Marcel Santilli:** What we're trying to do, I think, short term, right, is like what you said, Daniel.

**Marcel Santilli:** It's like, how do we abstract away a lot of these things so that our editors who are like, you know, super struggling all over the place and don't even know anything and, you know, to just like, hey, your job is to take a idea, an assignment, all the way to publish ready.

**Marcel Santilli:** With the system and then like, that's it.

**Daniel Lopes:** Like, you don't worry about the system.

**Daniel Lopes:** Don't worry.

**Daniel Lopes:** What's an artifact or anything.

**Marcel Santilli:** You're just like going to take that and you're going to go through this process and you have essentially, GP, we have 30 essentially like beta testers, like, you know, every day, like we're recording their sessions and figuring out like what to.

**Daniel Lopes:** I think like that entire system is too complex as in like solving as a whole, like there's problems everywhere.

**Daniel Lopes:** There's a whole features of.

**Daniel Lopes:** Topics, how do you write a brief, and then how you write the article at the end to sound like the right person.

**Daniel Lopes:** To me, the ideal setup that we need to track ASAP is just like, I had a new client, there was a workspace setup process that you go through.

**Daniel Lopes:** And maybe this process, that's the thing that I think we need to track now.

**Daniel Lopes:** It's just like, do you feed four articles?

**Daniel Lopes:** Like, how do you set up the workspace?

**Daniel Lopes:** And then as you go into that, you don't know that it's creating like a memory bank of writing styles and whatever, you know.

**Daniel Lopes:** It doesn't know that it has a growthx, the writing style standard that will be mutated to the client and all that kind of stuff.

**Daniel Lopes:** And then as you go through, like maybe you like press buttons multiple times.

**Daniel Lopes:** Now, okay, like now you're polishing the, now you're writing, like you're calibrating the writing style for the brand.

**Daniel Lopes:** And then once that's done, black box hidden away, only Kirkland's TV and like they can open it.

**Daniel Lopes:** And then, and, and the client's just like, and then the post-processing process and the drafting process will consume that.

**Daniel Lopes:** So like the first shot at it, Mike, 85.

**Daniel Lopes:** And then they're post-processing, we're really validated to make sure it's right, you know?

**Daniel Lopes:** Because, like, we don't have to rebuild the whole system, we just rebuild the writing style part that we're struggling, you know?

**Marcel Santilli:** And I think, like, the very first whiteboarding session we did, Daniel, like, I keep going back to that session, I know, it long time ago, so, but, like, my instinct from listening to a lot of things is, like, the reason RBI is doing well and doing good is because, like, they probably have a ton of, like, global, private, like, system-wide things.

**Marcel Santilli:** Like, for instance, like, for me, like, if I was building what you're describing right now, I wouldn't, like, the first thing I would do is, like, I would create the ultimate database of all the best writers, all the styles, I would tag the  out of that database, I would, like, decompose it into sentence, I would create another database of sentence structures, another one of, like, and, like, I would try to, like, essentially create this ultimate...

**Marcel Santilli:** The knowledge base of what's high quality patterns and principles and examples and archetypes and styles and define styles, right?

**Marcel Santilli:** Like explain what styles are and all of that, right?

**Marcel Santilli:** And then like this is like our IP essentially for the drafter or editor, right?

**Marcel Santilli:** Like, and then from there, then like the bridge and that bridge is like, how do you fetch from this knowledge base that's highlighted by our chief content officer who like literally that's how he learned how to be, you know, what he does.

**Marcel Santilli:** And I also have good taste and we have other people that have good taste, right?

**Marcel Santilli:** Like, but it's like, you know, it's like literally that it's like decomposing all the patterns and everything else here.

**Marcel Santilli:** And then it's like the wizard will pull from that and calibrate and adapt it to that client, right?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Right now, if you try to do that on the web based on like a few examples.

**Marcel Santilli:** It's just going to be so garbage.

**Marcel Santilli:** It's like the way I do my styles, I always go like, okay, I want to do a little bit of Jason Free with Paul Graham with Adam Grant.

**Marcel Santilli:** Like, you know, it's like that's how I do my styles.

**Marcel Santilli:** And it's the only thing that works.

**Marcel Santilli:** It's just like, hey, make this more like Paul Graham meets Jason Free meets Jeff Bezos CEO memos.

**Daniel Lopes:** Like, I think there's, yes, to all of that, and there is a lot more than this, but that's part of what we're trying to do about the scoring.

**Daniel Lopes:** Like, what's the scoring as a company for scoring quality of writing?

**Daniel Lopes:** So we have a bunch of questions about, this one is not relevant anymore, but headline, headline specific things, how they should be.

**Daniel Lopes:** And then we have structure flow, and then we have specificity for authorizations as part of the...

**Daniel Lopes:** Writing scoring already in all the questions, but what you're saying is essentially this even for, not just for the scoring, because this is just for the scoring, but for the examples, you know, like, I think we need the scoring, we need the scoring too.

**Gianpiero Puleo:** But by listening to what you said, like, I would love to combine the two, but like, we would need to have our own, in my opinion, we would need to be one, opinionated in terms of how we think we want to evaluate writing.

**Gianpiero Puleo:** I don't think there's a right approach to do so.

**Gianpiero Puleo:** I think we need to pick ours, but then what we would do is we would decide what are the right dimensions to be able to annotate all the data that we will collect from writing.

**Gianpiero Puleo:** for example, because fact-checking is like, it's very kind of, to a point, cut and dry.

**Gianpiero Puleo:** So correctness, for example, I think it matters to a point.

**Gianpiero Puleo:** When we're talking about style, think we need to identify like a.

**Gianpiero Puleo:** Is it tone?

**Gianpiero Puleo:** And then maybe within tone, we decide that we have whatever dimensions we want.

**Gianpiero Puleo:** But I think, again, they need to be opinionated.

**Gianpiero Puleo:** So it could be like a level of weakness, a level of dryness, a level of seriousness, like whatever.

**Gianpiero Puleo:** Because I think what we want is to kind of evaluate each of those dimensions, score them on a scale.

**Gianpiero Puleo:** Because then that's how you can start manipulating like how much you want a certain style.

**Gianpiero Puleo:** Like essentially getting a style becomes giving thresholds for scores to each particular dimension.

**Gianpiero Puleo:** In like a unique combination becomes a unique writing style.

**Gianpiero Puleo:** And then you take like, let's say, programs like essays, like a bunch of them.

**Gianpiero Puleo:** And you actually run them through the system.

**Gianpiero Puleo:** And then you collect scores for that.

**Gianpiero Puleo:** And that score profile becomes like the score profile for program style.

**Gianpiero Puleo:** And then you collect like a bunch of them.

**Gianpiero Puleo:** I think it would be like a really interesting system, but we would need someone, which is not me, I'm not a good writer, unfortunately, to actually think like what are the actual dimensions that we would want to look at.

**Daniel Lopes:** I think, yeah, I agree.

**Daniel Lopes:** I think that this is like an always improving system.

**Daniel Lopes:** You know, this is like, this is the non-privial thing.

**Daniel Lopes:** And I think that might be an easy thing for us to do it in the short term.

**Daniel Lopes:** What is MVP of this?

**Daniel Lopes:** And an MVP of this is just like a large catalog of like ranges of styles.

**Daniel Lopes:** Like we pick like maybe a dry, like Lovable, for example, is whimsical and more fun and like uses a bunch of slangs.

**Daniel Lopes:** Like while they stand is just PhD writing, you know, so.

**Gianpiero Puleo:** Then we have, like, examples of things.

**Gianpiero Puleo:** But we would need, even in the MVP, though, I think we should create a B0 of our, whatever our model is.

**Gianpiero Puleo:** We can change it later.

**Gianpiero Puleo:** But, like, even for MVP, like, what are the dimensions?

**Gianpiero Puleo:** We can start with just a diagram.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** So I think we need, like, every chunk of writing as, like, headlines, interests, CTAs, hooks, whatever, you know, lists.

**Daniel Lopes:** It's FAQs, like, all the different, like, of a potential piece.

**Daniel Lopes:** And then we have variations.

**Daniel Lopes:** Maybe it's, like, three columns.

**Daniel Lopes:** Like, serious in the middle extreme.

**Daniel Lopes:** And then with good examples of each.

**Daniel Lopes:** And then we create simulated bad examples of each as well.

**Daniel Lopes:** And then during the calibration process, you get that cheat sheet that's just a set of examples from.

**Daniel Lopes:** keep add

**Daniel Lopes:** And I think that would be that I already outperformed this  that we have now.

**Gianpiero Puleo:** We don't have to go to life.

**Gianpiero Puleo:** think most likely.

**Gianpiero Puleo:** It's just that the MVP probably we would have, I mean, if I think about the MVP version of it, when we really want to set up the foundation for, you know, to see how it works, I'll probably want a human to score them across the...

**Daniel Lopes:** Yes, yes.

**Gianpiero Puleo:** Because that becomes the benchmark.

**Gianpiero Puleo:** Then from there, we can start, like, running a model with that benchmark as a reference kind of score, other stuff.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** That's very similar to the stuff that I was working on yesterday.

**Daniel Lopes:** Yesterday, was, funny enough, I was like, I was taking the, trying to figure out the writing scoring, and I took Panzer's work, and he was working with Kirkland on this for a while, and I was figuring out how to do the, that kind of create the model.

**Daniel Lopes:** And the body was missing, and the body is missing, I was well, I'm not going

**Daniel Lopes:** Yeah, I've got enough time for this, this job, generate a bunch and have PN their flag, you know, that's the qualified label.

**Gianpiero Puleo:** Yeah, yeah, like, one thing that, like, I need to go.

**Daniel Lopes:** Yeah, yeah, need to go.

**Gianpiero Puleo:** Exactly, with my wife, sorry.

**Marcel Santilli:** Have a good weekend.

**Gianpiero Puleo:** Oh, Yeah, let me know if you want to continue this next week to decide what we want to focus on for the cycle.

**Gianpiero Puleo:** But this was, this was, yeah, that sounds, that sounds good.

**Marcel Santilli:** Then you want to stay on for just a minute?

**Daniel Lopes:** Yeah, yeah.

**Marcel Santilli:** I asked you to be, see you, man?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Like, I, because, like, our, our big vision, ultimately, I think this is going to be, like, essentially, like, reinforcement learning, right?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And so, like, the way I was kind of thinking is, like, it is, like, if you, maybe it is right now, like, just a stylistic workflow, right?

**Marcel Santilli:** everybody.

**Daniel Lopes:** But one that we define the rules a little bit, like, let me give you an example, just like I was just like, yeah, yeah, that's what we were discussing before, like, we have to, we need, like, the way we're thinking, like, we need to fix the disaster, like, we're going to keep failing clients in regards of how good the agents will be, because they'll enforce the wrong stuff.

**Daniel Lopes:** What we need to do is take, like, Kirkland and Spencer, they kind of started, but there are sections of an article, it's not in detail, as in detail as it must be, but we essentially need to, like, decompose any kind of pieces into, like, intros, headlines, hooks, like, a bunch of different subsections of things.

**Daniel Lopes:** And then we need to come up with, like, a lever, like, dry in the middle, maybe it's just three categories, know, like, it's dry in the middle, like, professional in the middle, and whinsic.

**Daniel Lopes:** And then we have a lovable in one end, that has a bunch of slangs and stuff, and then we have base standards, PhD writing, or, like, clerk, or, like, tribe, whatever.

**Daniel Lopes:** You know, on the other end, and then for each one of those, we create all these examples, and then the workspace setup for the writing guidelines will be just a wizard saying, like, which one do you prefer, and generating from those, and you create this cheat sheet that's just a set of exemplars under the hood that's, like, good and bad.

**Daniel Lopes:** Like, there's, like, no, you must use that, you know, it was just, like, shipment of examples, you know, and then the other one can pull from, like, okay, I've been writing a hook.

**Daniel Lopes:** What is the good examples of a hook?

**Daniel Lopes:** And then we're, like, did what you find that section in the context, you know?

**Marcel Santilli:** Yeah, I think, I think we, if we try a couple of different approaches, like, no matter what, I just don't see any scenario where for everything, we don't need examples, right, of patterns from, like, the best, essentially, right?

**Marcel Santilli:** Like, for instance, I don't think it's going to be, like, three ways to do an introduction.

**Marcel Santilli:** It's going to be, like, hey, for introductions, here's, like, like, let me give you an example over here, right?

**Marcel Santilli:** Like, um, it,

**Marcel Santilli:** Like, what are the different, like, archetypes of introduction patterns, right?

**Marcel Santilli:** So the first one is, like, the contradiction stack, right?

**Marcel Santilli:** And then here's the second one.

**Marcel Santilli:** It's called the forensic cold opener, right?

**Marcel Santilli:** Whatever.

**Marcel Santilli:** This might be overengineering, right?

**Marcel Santilli:** And so, like, you can create, like, these archetypes for, like, let's say, introduction pattern, right?

**Marcel Santilli:** Then, like, once you have, and you can apply this to so many things, and then it's just like, hey, now it's style.

**Marcel Santilli:** Now it's sentence structure.

**Marcel Santilli:** Now it's whatever, right?

**Marcel Santilli:** Like, and then you apply it sequentially.

**Marcel Santilli:** But, like, for instance, like, if you don't get the pattern first of a section, like, right?

**Marcel Santilli:** It's like, hey, when I'm writing a thing, it's like, hey, I'm going to start with the hook.

**Marcel Santilli:** Then I'm going to go into a personal story.

**Marcel Santilli:** And then I'm going to, like, bring it back around.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** That's a pattern, right?

**Marcel Santilli:** And if you get the pattern right, then you can get the, like, you know, nuances of the sentences.

**Marcel Santilli:** Do you want short sentences?

**Marcel Santilli:** Do want long sentences?

**Marcel Santilli:** Do you want, like, short paragraphs?

**Marcel Santilli:** Long paragraphs?

**Marcel Santilli:** you want, like, you know?

**Marcel Santilli:** Now, do you want to sound, like, edgy?

**Daniel Lopes:** Or do you want to sound blah, blah?

**Daniel Lopes:** And then you can apply that at the end.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** The problem with the pattern, though, is that it varies so much.

**Daniel Lopes:** You can see on our own blog where we have, if I'm writing a newsletter, the pattern is one.

**Daniel Lopes:** If I'm writing an opinion piece, the pattern is another one.

**Daniel Lopes:** If I'm writing a social media post, the pattern is another one.

**Daniel Lopes:** I'm a deep dive, the pattern is another one.

**Marcel Santilli:** But let me show you an example, right?

**Marcel Santilli:** This is for what I was writing or generating here, right?

**Marcel Santilli:** And, like, this pattern is horrible, right?

**Marcel Santilli:** Like, and not because, like, it's always horrible.

**Marcel Santilli:** Like, it might be okay.

**Marcel Santilli:** But in this case, it's like, you're building an AI agent.

**Marcel Santilli:** It keeps giving you generic, unhelpful responses.

**Marcel Santilli:** You missed the mark completely.

**Marcel Santilli:** Sound familiar?

**Marcel Santilli:** It's like, this is useless, right?

**Marcel Santilli:** It's like, and so, so then it's like, it's good.

**Daniel Lopes:** Which screen are you sharing?

**Marcel Santilli:** I think you might be sharing that.

**Marcel Santilli:** Oh, sorry.

**Marcel Santilli:** My bad.

**Marcel Santilli:** I'm sharing probably the wrong screen.

**Marcel Santilli:** The.

**Marcel Santilli:** The.

**Marcel Santilli:** It's like the atlas execution, like the content is good, but it's like, this introduction, for example, it's like, it picked the wrong pattern for this content.

**Marcel Santilli:** We need to convince them that like, and explain to them, right?

**Daniel Lopes:** Yeah, but if you go to the writing guidelines, you see why it's doing it.

**Marcel Santilli:** The writing guidelines is completely wrong for this kind of piece.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** So that's what I'm saying.

**Daniel Lopes:** So the pattern broke because the writing outline was written in like a broad sense and essentially applied everywhere, you know?

**Daniel Lopes:** So that's the challenge that we have to figure out.

**Daniel Lopes:** We have to figure out, there's, I think there might be, like you might bring me a good point.

**Daniel Lopes:** So I think there is content type, and then I think there is, oh, you're right, you know?

**Marcel Santilli:** Okay.

**Marcel Santilli:** That's content type.

**Marcel Santilli:** It's almost like the way I'm thinking about it, it's like, put styles aside and voice aside.

**Daniel Lopes:** And the first thing you need to figure out is like, Maybe we're not talking in same terms.

**Daniel Lopes:** When I say style, I'm just talking about whatever you see it, does it sound right?

**Daniel Lopes:** So that's what I mean.

**Daniel Lopes:** It's just like, it's using the wrong examples.

**Marcel Santilli:** It's using the wrong, everything is off.

**Marcel Santilli:** Yeah, and this is bad, but it's like, I guess for my head was like, If we decompose it down to like very simplistic patterns, right?

**Marcel Santilli:** And we curate the patterns, curate the examples, we curate the voices or archetype voices, right?

**Marcel Santilli:** And we figure out what are the primitives of like, how to, the primitives of style, or right?

**Marcel Santilli:** Like, or the primitives to- Yeah.

**Marcel Santilli:** To writing, essentially, right?

**Marcel Santilli:** Then I think we can have, like, a database of these primitives, of what great primitives look like, you know?

**Marcel Santilli:** And then, like, then you can figure out when to pull these primitives and then adapt it to the context of that workspace and to the context of that specific, like, task, if you will, for like a better word, right?

**Marcel Santilli:** And within the context of that specific section that it's working on, right?

**Marcel Santilli:** The active part of the end.

**Marcel Santilli:** But the good news is, like, the research is great.

**Marcel Santilli:** Like, you know, a bunch of other things are great.

**Marcel Santilli:** And so it's like, this part is, like, very, I think, solvable, you know?

**Marcel Santilli:** Because if you just start from good writing, it's like, you're going to get pretty good already, you know?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah, I think there's two components here.

**Daniel Lopes:** What we talk about.

**Daniel Lopes:** I think one is the same.

**Daniel Lopes:** Skeleton, like the patterns, and another is how you feel out in this basis of this, you know, where the drafting agents would be more focused on the patterns, and it might miss on the tone and stuff like that, but the post-processing one has to enforce the right, you can try these variations, you know, of the mode.

**Marcel Santilli:** Because that's actually how people write, yeah.

**Marcel Santilli:** Yeah, exactly.

**Marcel Santilli:** I think I had, I think I had one of these.

**Marcel Santilli:** I have an interview.

**Daniel Lopes:** Okay, cool.

**Daniel Lopes:** But yeah, I think, I think this is also, and I think GP is the right person to think about it, and so we probably should, I think we can detach him from that super complex, figure out agents for everything, because he was going in the right direction.

**Daniel Lopes:** But I think we can bring it back to like, okay.

**Daniel Lopes:** Skeleton, like the patterns, and another is how you feel out in this basis of this, you know, where the drafting agents would be more focused on the patterns, and it might miss on the tone and stuff like that, but the post-processing one has to enforce the right, you can try these variations, you know, of the mode.

**Daniel Lopes:** Because that's actually how people write, yeah.

**Daniel Lopes:** Yeah, exactly.

**Daniel Lopes:** I think I had, I think I had one of these.

**Daniel Lopes:** I have an interview.

**Daniel Lopes:** Okay, cool.

**Marcel Santilli:** But yeah, I think, I think this is also, and I think GP is the right person to think about it, and so we probably should, I think we can detach him from that super complex, figure out agents for everything, because he was going in the right direction.

**Marcel Santilli:** But I think we can bring it back to like, okay.

**Marcel Santilli:** Okay, we need to ship a chunk of that that will be related to the output, producing output.

**Marcel Santilli:** And the production of output, I think there might be an MVP here that we just need to quote the MVP in a way that's not rash it and starts from scratch in a month from now.

**Daniel Lopes:** Once we have the apply AI person and they can collaborate on this together.

**Marcel Santilli:** And I think the meme here is just like, if the writing guidelines are just written with examples and you have variations of writing guidelines, then you can pull that in a second point, more dynamic.

**Marcel Santilli:** It will be probably outperforming everything, all right?

**Daniel Lopes:** Outperforming the best that have today.

**Daniel Lopes:** And we don't have Marcel people like writing those things, the system writing those things.

**Daniel Lopes:** Yeah, yeah, exactly.

**Daniel Lopes:** I think we have like, I think in this next cycle, we're pulling Panzer from everything.

**Daniel Lopes:** Right?

**Daniel Lopes:** Mm-hmm.

**Daniel Lopes:** And there can be 50% on.

**Daniel Lopes:** Creating content for the community and things like that.

**Daniel Lopes:** I think there's some of this.

**Daniel Lopes:** On this, working with, like, someone.

**Marcel Santilli:** GP, yeah.

**Marcel Santilli:** And their whole thing.

**Marcel Santilli:** It has to be GP, like, Kirkland is true.

**Daniel Lopes:** Because, like, I think I've spent enough time with AI, too.

**Daniel Lopes:** And it depends on how to do, but I think we might think about it slightly different.

**Marcel Santilli:** Yeah, you're technically, he's not.

**Marcel Santilli:** He doesn't understand the terms and everything.

**Daniel Lopes:** Like, you were thinking the right premises and everything.

**Marcel Santilli:** Yeah, and then I'll experiment a bunch as well with this.

**Marcel Santilli:** But, like, one part of this project is building a database of writing examples.

**Marcel Santilli:** Yeah.

**Daniel Lopes:** That, like, as a start.

**Daniel Lopes:** It doesn't even have to be super extensive.

**Marcel Santilli:** You know, it's just, like, a handful of people.

**Marcel Santilli:** And a handful of examples and a handful of, like, sections for each kind of content type and how they would write.

**Marcel Santilli:** You know, like, that would be, like, enough to be, to outperform what we have today.

**Marcel Santilli:** We always have to think about how we all perform today.

**Marcel Santilli:** You know.

**Marcel Santilli:** You

**Marcel Santilli:** And then if there's a path to like, to continue to evolve, and yeah, yeah, yeah, you can always like, enrich the database, way I think about it, right?

**Marcel Santilli:** Like, you can add more, you can add more archetypes and styles, you can add more, whatever, can even fine tune a model on that person after, you know, like, oh, I fine tune, because I think that's what's going to end up happening.

**Daniel Lopes:** It's like, you're, we're going to have a bunch of like, little fine tune models that are going to be for what they might be like, you tool call to this one fine tune model plus custom instructions to do this, just like, that's just like, tune to like, yeah, this architecture, way to do it.

**Daniel Lopes:** You know, like, cool, right?

**Marcel Santilli:** Cool.

**Daniel Lopes:** All right.

**Daniel Lopes:** I got it.

**Daniel Lopes:** All right, man.

**Daniel Lopes:** Sounds good.

**Daniel Lopes:** I'll think through a little bit.

**Daniel Lopes:** I think check that is like, it's, it's, it's good.

**Daniel Lopes:** I told them, like, don't focus on the overview, focus on the prompt screen and the data table, because if you had the data table, right, and like, essentially what I had for, for the prompt, and then

**Daniel Lopes:** If on for the sources for URLs, then the overview is just pulling that, but if you get the overview without getting the sections right, then it's just like the wrong sequence, like, oh, okay.

**Marcel Santilli:** And then he wanted to do, like, the public, like, prompt pages, and I was like, no, no, no, don't focus on that right now, like, focus.
