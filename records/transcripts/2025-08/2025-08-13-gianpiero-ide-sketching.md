# Gianpiero - IDE Sketching

<metadata>
date: 2025-08-13
time: 17:04 UTC
duration: 88 minutes
organizer: Daniel Lopes
participants: Daniel Lopes, Gianpiero Puleo, Ben Church
fathom_recording_id: 80363863
fathom_url: https://fathom.video/calls/378414200
share_url: https://fathom.video/share/pwCMzHor_rzNm7WY-nUs9PMRngghQFks
source: fathom
enriched_on: 2026-03-03 18:45 UTC
</metadata>

---

## Summary

Daniel walked the team through his real-world workflow for building AI agents, revealing critical pain points in current tools: constant context-switching between Studio, Temporal, LangFuse, and Anthropic Console. The team evaluated Mastra as a potential alternative and found that while it has elegant concepts and excellent documentation, the code generation is inferior to their own rule-based approach. The discussion established that the ideal IDE should integrate workflow execution, debugging, prompt engineering, and evaluation into a single interface, with particular emphasis on making the "run, inspect, iterate" loop dramatically faster and more intuitive than jumping between fragmented tools.

---

## Context

This is an internal GrowthX product strategy meeting about the IDE component of their AI workflow platform. Daniel Lopes, who leads product architecture at GrowthX Labs, has been building complex AI agents and workflows for several weeks and encountered significant friction in the development process. Gianpiero Puleo and Ben Church, part of the GrowthX core team, are evaluating competing solutions (particularly Mastra, a recently funded workflow platform) and designing the next generation of their own tooling. The goal of the call was to translate Daniel's ground-truth developer experience into concrete product requirements, ensuring that the IDE prioritizes the actual workflow lifecycle developers face—not just workflow creation, but debugging, iteration, and evaluation.

---

## Relevance

- **To GrowthX Product Development:** Daniel's workflow reveals that the run-inspect-iterate loop is the dominant mode once a workflow is created. Current tools (Studio, Temporal, LangFuse) force developers to jump between 4-5 applications to answer a single question about workflow behavior. The ideal IDE must integrate execution visibility, step-level input/output inspection, cost/performance metrics, and prompt rendering into a unified interface accessible in <10 seconds from any point in the workflow.

- **To Competitive Positioning:** Mastra (raised $10M, launched January 2025) is attempting to solve similar problems but with poor execution—excellent documentation and onboarding, but generated code quality is significantly worse than GrowthX's rule-based approach. Their IDE is visually polished but non-interactive (no node editing, limited drilling). GrowthX's CLI and workspace tools are already superior in code generation and developer experience; positioning should emphasize substance over visual design.

- **To Evaluation & Quality:** Daniel's workflow confirms that exemplars, success criteria, and evaluation should be built into the IDE from day one, not bolted on after. The discussion surfaced a key insight: developers need a natural-language-first approach to defining assertions and quality checks, not deterministic heuristics. Tools like Anthropic Console's good/bad example generation are valuable, but the IDE should make this pattern the default for workflow creation.

- **To Open-Source vs. Proprietary Strategy:** The team identified an opportunity to open-source the core workflow engine and local development tools while keeping cloud-based services (fine-tuning, dynamic prompt generation, advanced analytics) proprietary. This approach mirrors what Mastra is attempting, but with better engineering foundation.

---

## Overview

- Current tools (Studio, Temporal, LangFuse) each have strengths but require constant context-switching, hindering workflow efficiency
- Ideal IDE would integrate workflow execution, debugging, prompt engineering, and evaluation in a seamless interface
- Evaluation and quality checks should be built into the workflow creation process from the start
- There's a tension between local development and cloud-based services for AI workflow tools that needs to be balanced

---

## Key Topics

### Current Workflow and Pain Points

  - Daniel uses multiple tools in parallel: Studio, Temporal, LangFuse, and Anthropic Console
  - Constant context-switching between tools slows down the development process
  - Difficulty in tracing API calls and LLM interactions within the workflow
  - Limited visibility into cost and performance metrics during development

### Ideal IDE Features

  - Integrated view of workflow execution, including sub-workflows and individual activities
  - Easy access to input/output for each step, especially LLM calls and API interactions
  - Built-in prompt playground with context awareness of the current workflow
  - Ability to reset and re-run specific parts of the workflow without losing context
  - Improved visualization of metrics, errors, and evaluation results

### Evaluation and Quality Checks

  - Daniel starts with exemplars and success criteria when designing prompts
  - Anthropic Console's approach of generating good/bad examples is valuable
  - Need for dynamic, context-aware evaluation that can adapt to specific use cases
  - Potential for self-improving prompts and evaluations over time

### Tool Comparison

  - Maestro: Good documentation and onboarding, but limited functionality in practice
  - Anthropic Console: Excellent for prompt engineering, but recent UI changes have removed some useful features
  - LangFuse: Good for prompt tracing, but limited in scope compared to full workflow needs

### Open Source vs. Proprietary Considerations

  - Core workflow engine and local development tools could be open source
  - Cloud-based services for fine-tuning, dynamic prompt generation, and advanced analytics could be proprietary offerings

---

## Action Items

- Daniel to complete and share articles detailing his ideal workflow process
- Focus IDE development on expanding run, inspect, and iterate capabilities rather than initial workflow creation
- Explore ways to integrate evaluation and quality checks earlier in the workflow development process
- Consider how to balance local development experience with cloud-based services for advanced features
- Investigate potential for open-sourcing core components while maintaining proprietary advanced features

---

## Transcript
**Daniel Lopes:** And it's insane.

**Daniel Lopes:** It's expensive, though.

**Daniel Lopes:** So, yeah, maybe I can walk you through, show you guys how I did that.

**Daniel Lopes:** Because it actually has an impact.

**Daniel Lopes:** Because I was, like, thinking about the ideal experience.

**Daniel Lopes:** Like, I don't know if you wanted to walk through, like, whatever you have.

**Daniel Lopes:** But I was just, like, flipping.

**Daniel Lopes:** I was just, like, building the agent yesterday and building the draft one, which is a little easier.

**Daniel Lopes:** And then doing some other stuff.

**Daniel Lopes:** And, like, paying more attention on the experience.

**Daniel Lopes:** You know, like, what would be the ideal experience?

**Daniel Lopes:** And, like, I spent so much time jumping between studio and then looking at the output of the input and output of the workflows.

**Daniel Lopes:** And then looking at the input, like, the output of the APIs under the hood.

**Daniel Lopes:** So, in this case, output of EXA and before with Stavli.

**Daniel Lopes:** And also, like, trying to look at their costs and all this stuff.

**Daniel Lopes:** And then also looking at length is to see what.

**Daniel Lopes:** What is the rendered version of our prompts?

**Daniel Lopes:** So I'm jumping between like four or five of those.

**Daniel Lopes:** And that even though you get the option to reset things in Temporal, and that's really nice, it's not, like you don't see that.

**Daniel Lopes:** Like it's not designed for the scenarios first, you know, like it's not designed for observing the behavior.

**Daniel Lopes:** It's designed for just debugging.

**Daniel Lopes:** So it's not like, how did this behave?

**Daniel Lopes:** Like I'm usually looking at high level, did it perform or not?

**Daniel Lopes:** And then you go one level deep, which is like input and output, and then a level deeper, like what actually happened in the event.

**Daniel Lopes:** And that stuff, it's like, it's super hidden everywhere.

**Daniel Lopes:** And it's the same with all the other tools.

**Daniel Lopes:** So I was just writing like a bunch of stuff, like if I didn't, what would be the good experience?

**Daniel Lopes:** It's just in plain text without thinking about the implementation and like, and then how hard it would be. And that's what I was writing.

**Daniel Lopes:** So, like, maybe I can, I don't know if you have a chance to, I was just, like, writing everything while also coding the age because the thing's taking, like, 10 minutes to run the research.

**Daniel Lopes:** So I was running both things at once.

**Daniel Lopes:** So the article, the writing is pretty messy, but I don't know if that helps, you know.

**Gianpiero Puleo:** Actually, it does, like, Ben, please jump in if you have any different thoughts here, but you and I talked a little bit yesterday.

**Gianpiero Puleo:** I'm happy to share what we did.

**Gianpiero Puleo:** Like, I was telling Ben, I played a little bit with Basra, trying to recreate the React flow, just because I wanted to get a feeling, get a feel for, like, how it is to kind of work with other tools, like, experience-wise.

**Gianpiero Puleo:** That's where I spent a bit of time.

**Gianpiero Puleo:** But apart from sharing, like, our, you know, our own impressions there, for me at this point, I think it would be very useful to see, like, literally to sketch your workflow.

**Gianpiero Puleo:** Yeah, like we use workflows, like your way of working, your way of working to create workflows.

**Gianpiero Puleo:** Because I think what I realized is that some of the stuff that at least for me gets missed in translation or lost in translation between us is because you created so much more workflows that like you, I think, have a unique perspective per se to me in terms of like what the pain points are.

**Gianpiero Puleo:** Because like at the end of the day, like I've looked at many, but in terms of like actually working and creating stuff, I created two.

**Gianpiero Puleo:** And so I just didn't bump into all this stuff, like as you said, where you kind of need to jump into like in my case, I created it.

**Gianpiero Puleo:** And then like essentially between fixing the prompts a couple of times and then working on the HTML templates, like I had to go to Langfuse once just because like I wanted to see why one prompt wasn't working.

**Gianpiero Puleo:** But other than that, like I didn't have to really jump around too much.

**Gianpiero Puleo:** So to me, it would be very useful to basically...

**Gianpiero Puleo:** Get your way of working with workflows, like, out of your brain and, like, on virtual paper, because that, I think, will give us, like, a common language in terms of, like, where you think the evolves fit, like, why you think some stuff is a bump, like, that's my idea for today's hour.

**Gianpiero Puleo:** What do you guys think?

**Daniel Lopes:** Yeah, and I even have, like, some stuff open from, like, the failure from, like, I got the research agent to work, and now I'm, like, I'm reading the results, like, shoot, like, out of the 20 questions that the plan was generated, 19 were great, and one was completely off.

**Daniel Lopes:** And now I have to, like, well, I had to, like, paste this in Claude to make it format the data, and then jump into LinkFuse, and, like, was literally scrolling through trying to find the tracing where that happened, just to see where it was all.

**Daniel Lopes:** I kind of guessed.

**Daniel Lopes:** I don't know how to fix it, but I wanted to see it, you know.

**Daniel Lopes:** So, like, I have the whole system open here from yesterday, 1 a.m.

**Gianpiero Puleo:** session, so.

**Gianpiero Puleo:** Yeah.

**Daniel Lopes:** So, like, let's do.

**Daniel Lopes:** Yeah, do we want to start with sharing a little bit, like, our...

**Daniel Lopes:** Yeah, that would be awesome.

**Gianpiero Puleo:** Then we jump into your stuff.

**Gianpiero Puleo:** Then, Ben, if you don't mind, because I was starting, because I started telling you about Mestra, then maybe, like, I can just continue with that and finish that.

**Gianpiero Puleo:** But, so, while I open my cursor window, just to recap a couple of things that I was mentioning to Ben, is that, so I played with Mestra trying to recreate the CEO content agent, the article agent.

**Gianpiero Puleo:** And, I think my overall impression is that Mestra definitely looks more sleek than it actually is when you actually go and work with it.

**Gianpiero Puleo:** So, I think because they have a good website and great documentation, it looks very mature.

**Gianpiero Puleo:** Then, actually, when I start to kind of trying to do stuff, it's, one, very basic, and even the IDE, once again...

**Gianpiero Puleo:** From a design perspective, it looks very cool.

**Gianpiero Puleo:** But actually, there's almost zero interaction, almost.

**Gianpiero Puleo:** Like, you can't, like, the graph, like, you can't do anything with it.

**Gianpiero Puleo:** Like, and even kind of drilling down doesn't really look very good.

**Gianpiero Puleo:** You can't create nodes.

**Gianpiero Puleo:** You can't create stuff.

**Gianpiero Puleo:** You can't create metrics.

**Gianpiero Puleo:** Like, you essentially do everything in code.

**Gianpiero Puleo:** And then in the IDE, you can see what you created.

**Gianpiero Puleo:** And the one thing that you can do there, which I think was cool, is that because it's all agent-based for them, then you can sort of interact with each individual agent in the IDE.

**Gianpiero Puleo:** And you can obviously kind of run the workflow.

**Gianpiero Puleo:** But even the workflow runs are, like, pretty basic.

**Gianpiero Puleo:** So, to me, Mastra, like, what does well, like, really well is onboarding and documentation.

**Gianpiero Puleo:** I know that it's kind of like a meta thing.

**Gianpiero Puleo:** But I'll show you.

**Gianpiero Puleo:** Let me just share my screen quickly.

**Gianpiero Puleo:** Sorry, where are you?

**Ben Church:** Here. Retinkering mostly in Maestro Cloud or in our machine?

**Gianpiero Puleo:** Local, yeah.

**Gianpiero Puleo:** Local first because I thought that that was kind of a little bit closer to how we want to start as in, like, we start on our local machines and then, yes, you can deploy it, obviously.

**Gianpiero Puleo:** Like, I didn't go there.

**Gianpiero Puleo:** One thing that I thought is really, really good from my perspective is that they basically have their own MCP server.

**Gianpiero Puleo:** You don't have to use it.

**Gianpiero Puleo:** So they have the NPX create master at latest, which we also are going to have, et cetera.

**Gianpiero Puleo:** But what I found, like, really, really cool, especially because we had a lot of onboarding problems, is that basically they have their MCP.

**Gianpiero Puleo:** And if you configure it and you add it to cursor, and by the way, if you start with the NPX create, you have an option in the guided process to actually add the MCP for you in your project.

**Gianpiero Puleo:** And then that actually has a tutorial mode.

**Gianpiero Puleo:** So you essentially can go from zero.

**Gianpiero Puleo:** To understanding Mestra, like in Cursor, with a step-by-step tutorial that is like provided by their MCP server.

**Gianpiero Puleo:** I thought that that was like a really cool way to do that.

**Ben Church:** Yeah.

**Ben Church:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** It's a cool idea.

**Gianpiero Puleo:** And then what didn't work though instead, and that's why I'm one of the things that makes me think like, you know, it's really not actually that mature.

**Gianpiero Puleo:** Even though then it has the MCP server that also offers the actual documentation to the agent about how to work with Mestra, like the code that it generates is really, really bad.

**Gianpiero Puleo:** Like our rules for our workflows, they're way better.

**Gianpiero Puleo:** Like I think, again, the MCP approach is good, but whatever they implemented in the MCP, it's way, way worse than our rules.

**Gianpiero Puleo:** Like when I try our scripts with our rules, it kind of almost one-shots it and then sure you need to take it.

**Gianpiero Puleo:** But here, like you can see my conversation with it.

**Gianpiero Puleo:** Like, I had to kind of go and pinpoint constantly, like, you you shouldn't do this.

**Gianpiero Puleo:** Like, for example, even something as basic as Ben, if you remember, you showed me, they have, like, a really, really nice fluent interface where you can chain, like, nodes with, like, dot branch and so forth.

**Gianpiero Puleo:** You can, like, it's very elegant to build the workflow in code like that.

**Gianpiero Puleo:** Like, their agent, even though he uses, well, sorry, Claude, using their MCP server, couldn't even do that.

**Gianpiero Puleo:** And was basically doing all the branching, like, inside one node.

**Gianpiero Puleo:** And I had to kind of point that out and sort of kind of get it to fix it.

**Gianpiero Puleo:** So, yeah, like, a lot of really good ideas in terms of how it could look.

**Gianpiero Puleo:** But the implementation, to me, really falls short.

**Daniel Lopes:** That's my sort of...

**Daniel Lopes:** Like, just for context, like, the stuff that you guys did with Claude Code, that's what I've been using yesterday and the day before all day.

**Daniel Lopes:** It's been working great for even, like, yeah.

**Daniel Lopes:** Oh, yeah?

**Ben Church:** Yeah.

**Daniel Lopes:** Really?

**Daniel Lopes:** It's almost like it works on the...

**Gianpiero Puleo:** Yeah, so again, this kind of wraps up what you just said.

**Gianpiero Puleo:** Like, our tools may be a little bit rougher on the edges, but we're getting much, much better.

**Gianpiero Puleo:** But they work a lot better in my short experience with Masra.

**Gianpiero Puleo:** Like, yeah, what they have, like, it's kind of elegant, but it takes actually longer to get there than with our tools because it just doesn't generate as good code as our rules is.

**Gianpiero Puleo:** And then, yeah, the idea is, like, smoke and mirrors.

**Gianpiero Puleo:** ahead.

**Gianpiero Puleo:** No, no, that's it.

**Gianpiero Puleo:** Like, the idea is just smoke and mirrors, basically, just visualization.

**Daniel Lopes:** So this is the entire, so you have tools, and you have workflows, and you have agents.

**Gianpiero Puleo:** Yeah.

**Daniel Lopes:** I see.

**Daniel Lopes:** So it kind of spreads out, so it spreads out the code in these three folders.

**Gianpiero Puleo:** it's almost like Rails or Next where you have the.

**Gianpiero Puleo:** Yeah, the folder structure is kind of forced on you.

**Gianpiero Puleo:** Like, this is not to say, mean, ultimately you can create whatever you want, but if you use their scripts and their tutorials and their agents, it kind of goes into these three folders.

**Gianpiero Puleo:** What's interesting is also they seem to create agents for, for example, in the React loop that you have in your content creation to recreate that, like you created separate agents for each of the activities, like the one creating the content, the one doing the evaluation, and then the sort of orchestrator, if you want, like the React planner.

**Gianpiero Puleo:** The tools are kind of pretty busy, but like, I don't like, it's not to be kind of too kind of nitpicky, but again, generates like a new stuff, like a lot of like regex and stuff like that that you don't really need kind of to do, like just the code that it generates.

**Daniel Lopes:** With their, again, rules, MCP servers, et cetera, this is not good.

**Daniel Lopes:** That's the thing that I think, like, the vast majority of the code should be in LLM, you know, as in, like, this LLM would do a much better job than just, like, qualifying this, if it's bigger or not, like, this is trying to be deterministic, while in reality, what we're trying to do here is, like, it's human judgment.

**Daniel Lopes:** So if you look at mine, it doesn't have this many, like, heuristics-based things.

**Gianpiero Puleo:** Yeah, it's just not good.

**Gianpiero Puleo:** And then, in fact, actually, the one thing that I would add is that, as I was looking also in their documentation, once again, from an interface and code design perspective, I think they have a very, very interesting evil approach, like, with a scoring class, et cetera.

**Gianpiero Puleo:** So, again, in terms of how they design the interface, it's pretty cool, I think.

**Gianpiero Puleo:** But then when you use their system, it doesn't even use it, like, it created, like, the entire scoring.

**Gianpiero Puleo:** This is kind of by hand, like with the analysis and stuff.

**Gianpiero Puleo:** So, yeah, it's a bit rough.

**Daniel Lopes:** Can you walk us through the, did you get a chance to play with their eval stuff and their tracing?

**Daniel Lopes:** Or do you have that or not yet?

**Gianpiero Puleo:** No, no, because I went through their documentation.

**Gianpiero Puleo:** But then when I tried to get the agent to implement it here, I didn't manage.

**Gianpiero Puleo:** It seems like, I don't know if the MCP server is kind of behind the SDK.

**Gianpiero Puleo:** And so, like, it's not aware of the scoring.

**Gianpiero Puleo:** So my next step, if I want to look, like, further into that is, like, I would have to create a small workflow myself.

**Gianpiero Puleo:** And then actually probably myself kind of go in code.

**Gianpiero Puleo:** Yeah, or, like, I didn't think about that.

**Gianpiero Puleo:** Sorry, like, I could, I guess, go into their pages and sort of copy and paste, basically, the scoring and eval section if I really want to try and get the LLM to do it.

**Daniel Lopes:** But, yeah, I didn't get to it.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So the deploy of this would be, like, that run SEO workflow would be the entry point, and you would deploy this in, like, a normal Node app?

**Gianpiero Puleo:** Yeah, pretty much, pretty much.

**Gianpiero Puleo:** So, and you can do it both from, sorry.

**Daniel Lopes:** How do they handle the deploy?

**Daniel Lopes:** Like, would we deploy on, like, whatever info we want?

**Daniel Lopes:** What's the master cloud do?

**Gianpiero Puleo:** It's their own platform.

**Daniel Lopes:** So it's a deploy to their platform.

**Gianpiero Puleo:** So it's, like, a DevOps play, basically.

**Gianpiero Puleo:** Yeah.

**Gianpiero Puleo:** So when you go, sorry, I don't know, actually, I'm not sharing my whole screen.

**Gianpiero Puleo:** Give me a second.

**Gianpiero Puleo:** So you probably don't see.

**Gianpiero Puleo:** So it gets into their IDE.

**Gianpiero Puleo:** You can, it's hidden by, yeah, it is local, and it's hidden by this annotation thing, but, like, you have, like, an option here to deploy to master cloud.

**Gianpiero Puleo:** But, yeah, if you, once again, like, it looks cool, but then.

**Gianpiero Puleo:** And if I go into the workflow, like, yeah, first of all, like for us, it's exactly the same.

**Gianpiero Puleo:** And I think we can do better here because this is tedious every time you want to rerun, like, something with different, like, yeah, I guess you could do JSON, but I think we can do better.

**Gianpiero Puleo:** But also, as I mentioned, like.

**Daniel Lopes:** One thing I've been doing for, like, all the new stuff is to have that kind of form, but I'm also doing, like, a step before that I think could be part of the framework for called instructions.

**Daniel Lopes:** So instructions would be, like, a special attribute name that would do a natural language and try to fill out the forms.

**Daniel Lopes:** People just, like, can't fill out the forms properly.

**Ben Church:** Yeah, for sure.

**Ben Church:** Yeah, amen.

**Gianpiero Puleo:** And, yeah, and then, like, like I mentioned, like, I'm, I mean, you can't see what I'm clicking and there's no, you can't do anything with the node.

**Gianpiero Puleo:** But here, like, because this improvement loop is supposed

**Gianpiero Puleo:** I think this to me is again like not good because if you remember our idea is that if you go into a nested sub-workflow, you actually get breadcrumbs and I think it's better because then you can work with this workflow.

**Gianpiero Puleo:** Here again, it's exploded and then actually if you go into a sub-sub-workflow, then you get like a dialog on top of a dialog on top of a dialog.

**Gianpiero Puleo:** So I think we can get like a much better navigation structure.

**Daniel Lopes:** Yeah, but that's it, like really this is What is on the log drains there?

**Daniel Lopes:** How do they switch the whole UI to something else?

**Gianpiero Puleo:** What I'm assuming is that You would just have the runs?

**Gianpiero Puleo:** I get a run here.

**Daniel Lopes:** That is cool.

**Daniel Lopes:** Yeah, you can configure your runs here.

**Daniel Lopes:** Yeah, and you can click on input and output and see the input and output of each.

**Daniel Lopes:** Yeah, they're trying to solve.

**Daniel Lopes:** Similar.

**Daniel Lopes:** This is so similar to what we have.

**Daniel Lopes:** Kind of doing the same thing at the same time.

**Gianpiero Puleo:** Yeah, but...

**Daniel Lopes:** They started in January.

**Daniel Lopes:** They raised 10 million.

**Daniel Lopes:** We did it with, like, two people.

**Gianpiero Puleo:** And now we have...

**Ben Church:** Yeah.

**Ben Church:** It's kind of...

**Gianpiero Puleo:** That scores to be true on the side.

**Gianpiero Puleo:** Was that a study?

**Ben Church:** On the side there, that scores.

**Gianpiero Puleo:** Is that what was...

**Gianpiero Puleo:** This is what I was referring to.

**Gianpiero Puleo:** We can't do anything here.

**Gianpiero Puleo:** So I think if I go and create it in code, they're going to appear here.

**Ben Church:** But I haven't really spent time there yet.

**Ben Church:** Gotcha.

**Daniel Lopes:** Yeah, I think, like, a lot of tools are, like, standardizing around the name of scores.

**Daniel Lopes:** the BrainTrust does that.

**Daniel Lopes:** LengthFuse does that, too, I think, now, to the SDK.

**Daniel Lopes:** Yeah.

**Ben Church:** Okay.

**Ben Church:** Yeah, anyway...

**Gianpiero Puleo:** It was funny.

**Gianpiero Puleo:** funny.

**Gianpiero Puleo:** I feel better after trying them out, because when I was looking at the website, was like, , like, they got, they do everything I want do, and it was amazing.

**Gianpiero Puleo:** I mean, they got, like, some really, good ideas, but I think they're not, they're not, like, that far ahead as they, as they look.

**Gianpiero Puleo:** Yeah, it's a Wizard of Oz kind of thing.

**Daniel Lopes:** Yeah, it's, it's that, you know, like, um, sorry, Ben, like, Kim, you interrupted you.

**Ben Church:** Well, was just going to say, uh, just a minor note on the score side, your idea of, like, people are lazy, taking natural language, uh, prompting and turning into inputs.

**Ben Church:** I had a similar conversation with Stevie yesterday on, okay, how do you, like, both bring engineering concepts closer to less technical people, and then bring less technical people closer to engineering concepts, and I really don't know what we want to talk to you about today, but it's, like, you know, how many regular people?

**Ben Church:** We're going to start with a testing-first approach to the writing workflows and think about, oh, how do I validate that it's correct?

**Ben Church:** How do I actually encode my vibe check?

**Ben Church:** And an idea that I'm going to put a pin in, let's not dive deep on it, but just think on it.

**Ben Church:** For that score panel we just saw in Maestro, you can imagine a world where it's like, okay, describe how you'd...

**Ben Church:** We reviewed your workflow.

**Ben Church:** Here's all the assertions you might want to create in plain text.

**Ben Church:** You don't want just kick me off making the evaluator, making the score for you.

**Daniel Lopes:** Yeah.

**Ben Church:** Yeah, 100%.

**Ben Church:** That's what I was actually writing yesterday.

**Daniel Lopes:** So I was like, I don't know if you had a chance to read that kind of nonsense stuff that I sent you overnight, but I was trying to think like, what would be the experience from both angles?

**Daniel Lopes:** Because ideally, I can walk you guys through that a little bit as well, just real quick.

**Daniel Lopes:** Do you have anything you want to show?

**Daniel Lopes:** Hello?

**Daniel Lopes:** you.

**Ben Church:** Ben, or like, should we just jump into my day?

**Ben Church:** No, I'd honestly love to go on like the original thing, which is like, you know, how do you, like, what's your process for creating a workflow, trying to use the work?

**Ben Church:** Like, you know, how do you start thinking about it?

**Ben Church:** Like, what's the ideal?

**Daniel Lopes:** good.

**Daniel Lopes:** Yeah, so.

**Daniel Lopes:** So, yeah, I'll finish this document later, but I was essentially trying to write, as a separate note, when we were thinking about the experience, I was writing this as like, what would be the process of somebody trying to create, like, let's say, comparison pages, super fast, and then starting from the natural language.

**Daniel Lopes:** And then working with the test scenarios, interacting with it, and then handing that off to an engineer to, like, build a better system.

**Daniel Lopes:** So, I'll just finish this.

**Daniel Lopes:** It's better later, but I was essentially trying to think about the same stuff you just said, Ben, as a core principle.

**Daniel Lopes:** And then I was going a step below and trying to figure out what is the engineer experience.

**Daniel Lopes:** I could step down afterwards.

**Daniel Lopes:** But anyway, the stuff that I was doing, so what I usually have, so I'm working on the, where is my Ben Puleo and my cursor.

**Daniel Lopes:** Yeah, so this, I have this stuff for writing, and I was building this thing here.

**Daniel Lopes:** So we have the research executor and the research supervisor.

**Daniel Lopes:** So I wanted to switch it to use exit instead of tably.

**Daniel Lopes:** had tably.

**Daniel Lopes:** Tably is what is in production.

**Daniel Lopes:** So what I...

**Daniel Lopes:** I...

**Daniel Lopes:** I...

**Daniel Lopes:** What I'm doing here is essentially I run both projects.

**Daniel Lopes:** I'm just going to do it if you guys didn't know anything about it.

**Daniel Lopes:** But I'm running both projects.

**Daniel Lopes:** So first thing I did, branch, and then I'm running the flow studio and flow worker.

**Daniel Lopes:** And some folks, they don't run the studio.

**Daniel Lopes:** So that's where we start to diverge.

**Daniel Lopes:** And I start from the studio, even though the cloud stuff is working well for running.

**Daniel Lopes:** The running of the workflow, I'm not running from cloud code.

**Daniel Lopes:** The running, I still run to the studio.

**Daniel Lopes:** And then, so in this case, Do you use a curl or postman or anything like that anymore?

**Daniel Lopes:** Just the studio?

**Daniel Lopes:** No, no, just the studio.

**Daniel Lopes:** Yeah, so what I would do here is keep it open locally.

**Daniel Lopes:** I actually have the other screen with everything here.

**Daniel Lopes:** But I have length views on the side.

**Daniel Lopes:** But this is my local.

**Daniel Lopes:** So I was running everything.

**Daniel Lopes:** Everything through here, and all night, and I will just generate the catalog, generate the docs, so it shows up here, and then this case, had to add XAPI key, so I had to restart, I had to my miss.tomyml, and then restart, and I was iterating on the executor first, because I just wanted to get the executor to work, and the supervisors, the one that comes up with the plan.

**Daniel Lopes:** So, what I did was, I went to XAI, grabbed their docs, and went to the docs.

**Daniel Lopes:** Most things that are AI-first now, they have a copy page now.

**Daniel Lopes:** So, I copied the page, pull markdown, pasted my cloud code, gave the two folders.

**Daniel Lopes:** I think the idea of having folders containing the entire workflow is super helpful, and so I just...

**Daniel Lopes:** Just gave the two folders to CloudCode, gave the whole markdown of the documentation for both this and their guide about their research.

**Daniel Lopes:** So it was a shift of code and asked CloudCode to make a plan for how the replacement for Tavli would be.

**Daniel Lopes:** So it came up with a large plan, mostly made sense, I made a few tweaks, and then asked to make the change to the executor first.

**Daniel Lopes:** So the executor, it made a change, and it looked right.

**Daniel Lopes:** So the hot reload kicked in correctly, there was no syntax error or anything.

**Daniel Lopes:** So I jumped back into the studio, and I triggered probably, and I go into executions, and I select one if it was empty, if there was one for me to choose from.

**Daniel Lopes:** I usually just go from there, and then I go into input, and use that as my, we added this bug again, it's like showing table, but I will use the input from the past one, when I go, and there's like bug here that puts me back, but if I go to run workflow, I'll just grab the input here, like this, manually pop in case, and then run workflow, and then this one.

**Daniel Lopes:** Supports a bunch of stuff, can be instructions, or the rest, so just paste it here and run, so I was doing that, until I got the executor to work, and then I went to the supervisor, so the supervisor is the one above, and as I do that, I will be like, all the time, but I would go, let's say I'm working on this one that I just completed, this one is a bunch of, was a bunch of.

**Daniel Lopes:** I like And then,,- will be complete in

**Daniel Lopes:** Oh, this is the executor.

**Daniel Lopes:** Let's go to the supervisor.

**Daniel Lopes:** So supervisor, executions, last one from an hour ago, input.

**Daniel Lopes:** This is the input, so it's a hybrid search with a bunch of questions.

**Daniel Lopes:** That means we'll take those questions and make them add search guidance around them, but we use those questions per se, and then it will create more questions.

**Daniel Lopes:** So what I want to see here is like what happened, like what was the plan, know, like did the generator plan a way out on it?

**Daniel Lopes:** So the only way for me to do that is like I go to research here and then the output looks good.

**Daniel Lopes:** So this helps, so I can see it looks good, but it would be nice if I could see like with more detail, how long did it take?

**Daniel Lopes:** Something Mason is doing, it's good.

**Daniel Lopes:** I will also like often just jump into the board and just see like how long did it take, you know, because we don't have that information easily there or like did they fail how many times it started, something happened, and then it triggered.

**Daniel Lopes:** So something was off.

**Daniel Lopes:** And then you can see here the last failure.

**Daniel Lopes:** So the board has less failure, has information like this, but there's so much going on here that it's kind of hard to follow it for me.

**Daniel Lopes:** So like I would go in and figure out why it failed.

**Daniel Lopes:** So sometimes you feel like many times.

**Daniel Lopes:** So I click on that and I would be like input.

**Daniel Lopes:** Okay, looks good.

**Daniel Lopes:** Last failure.

**Daniel Lopes:** , failed.

**Daniel Lopes:** Then I have to scroll down and like figure out here like what happened.

**Daniel Lopes:** Like why did it fail multiple times?

**Daniel Lopes:** And then, okay, that makes sense.

**Daniel Lopes:** Like Claude was having rate limits.

**Daniel Lopes:** So this is actually all the time, you know, and then they're constantly having problems, especially Claude around their launches.

**Daniel Lopes:** And then after this, everything looks good.

**Daniel Lopes:** Nothing stands out, but it's hard to read here.

**Daniel Lopes:** So I would jump back into our stuff.

**Gianpiero Puleo:** Sorry, just want make sure I follow here on a couple of your thoughts.

**Gianpiero Puleo:** So basically, like at this stage, the happy path, so to speak, is that if it runs, what you're interested in is like, was the output good?

**Gianpiero Puleo:** And then a few key metrics here quickly, like as quickly, like now you need to kind of drill in and you can see, but ideally quickly from where you are there.

**Gianpiero Puleo:** While you were showing in Tamporo, I want to make sure I understand, like, do you go there, is there a problem?

**Gianpiero Puleo:** Or do you just go there like for other reasons too?

**Daniel Lopes:** I go there just to see what's going on, like what happened.

**Daniel Lopes:** You know, sometimes I'll be sitting here and it's like, oh, up, it's like two minutes.

**Daniel Lopes:** Sometimes it's like five minutes.

**Daniel Lopes:** What is going on?

**Daniel Lopes:** And Tamporo actually shows me that.

**Daniel Lopes:** So like when I'm looking.

**Daniel Lopes:** If this was, if I'm looking at this at the first set and it took like three minutes, I can see the pauses, you know, and then I will click, okay, what is going on?

**Gianpiero Puleo:** Oh, they're down.

**Gianpiero Puleo:** And then I'll go do some chance.

**Gianpiero Puleo:** What I'm hearing from you, you're shooting.

**Gianpiero Puleo:** Like, yes, it worked, but in this case, what you're seeing is there's an anomaly, which is maybe one step to like so long.

**Gianpiero Puleo:** So you go here and investigate.

**Gianpiero Puleo:** That's sort of like what you're doing to them for.

**Daniel Lopes:** But I wouldn't say it's like, I wouldn't say it's like troubleshooting because I didn't know there was a trouble yet.

**Daniel Lopes:** I'm just like looking at the whole thing, execute, and then just spot check, like pattern matching.

**Daniel Lopes:** You might go in and realize like 10 minutes actually engines because whatever.

**Daniel Lopes:** Yeah, right, yeah.

**Daniel Lopes:** So like I just, it's like if you were like building piping and you just want to run the water and see like if something's leaking.

**Daniel Lopes:** So I was just, I'm just clicking around everywhere and checking.

**Daniel Lopes:** And I also have link-throughs on the side.

**Daniel Lopes:** Okay.

**Daniel Lopes:** And, uh.

**Daniel Lopes:** Everything that makes LLM calls, I usually, I'm checking link fields, and it's like something more elaborate.

**Daniel Lopes:** This one, I wasn't too concerned, because I tested the plan a lot before.

**Daniel Lopes:** So I built the plan prompt outside of this, that's not what I forgot to say, but for hard prompts, I will use this.

**Daniel Lopes:** So this is where I created, and you can see me iterating on that prompt here.

**Daniel Lopes:** So I think it's on the Daniel.

**Daniel Lopes:** So I was using the console a lot, even before I created the workflow, just to land on a plan that would look like this.

**Daniel Lopes:** Like I was like, can't you think about what would a good plan for research look like?

**Daniel Lopes:** So, and you can see that I'm the only person that uses it, because that's my only, my stuff is only the only stuff that's showing up there.

**Daniel Lopes:** But I essentially created this prompt here through multiple iterations.

**Daniel Lopes:** And at the end, and I started in reverse, so I wrote the output of what I wanted for them.

**Daniel Lopes:** I wrote this with one of our clients by hand, and yeah, so I literally wrote this by hand, almost everything, and I came up with all the questions, and I asked, I'll just enhance the dates and stuff like that, and I reviewed everything by hand, and then I evaluated it, and then I grabbed this, when I was creating the workflow, the plan file included this, so just for context.

**Daniel Lopes:** So that, so like when I'm looking at this here, I already know that this is aligned with what I had created, know, it's like, okay, this looks like the stuff that I had, everything looks right, has all the enums that I needed that are critical, high, and medium, and low priority, has the parameters for advanced guidance here on all of them, because it's in hybrid, but I also want to test...

**Daniel Lopes:** I need to test Strict, so Strict, it wouldn't add this, Strict would just follow the exact questions we have, and Exploratory would just take it with like a huge grain of salt and come up with its own questions and its own guides.

**Daniel Lopes:** So I didn't test all three of them because it's hard, you know, so, but anyway, like this one, the plan worked, now I need to go see the synthesized, so this is the final thing, it took like, 10 minutes to run, it doesn't show here because it was sub-workflow, so if I click in, the whole thing took 15 minutes, so our student doesn't handle sub-workflow as well, it doesn't count, so, and I'm looking at it, like it dispatched 10 things, one took forever, and I'm like, why?

**Daniel Lopes:** And then I go look at this, and it's like a sub-workflow, and sub-workflows look hard here, hard to parse, but I'm looking at it, and they're looking in reverse because it's top-down,

**Daniel Lopes:** So, and then I go here and I'm trying to, why did it take so long?

**Daniel Lopes:** Okay, like they've iterated multiple times.

**Daniel Lopes:** So it didn't get one single perfect answer for an exit.

**Daniel Lopes:** So it did multiple calls to exit.

**Daniel Lopes:** So it did three calls.

**Daniel Lopes:** That makes sense.

**Daniel Lopes:** And then the first thing that I noticed, okay, we're overusing exit pro.

**Daniel Lopes:** So I had to like switch to exit normal because exit normal is actually pretty good.

**Daniel Lopes:** So if it's going to take this many calls, better to like use the exit normal one.

**Daniel Lopes:** And still took forever with the normal.

**Daniel Lopes:** So I changed it and re-ran the workflow with exit normal.

**Daniel Lopes:** It took like this before it was taking like 2x longer for just this one.

**Daniel Lopes:** And then I go through everything and I want to see, okay, like for each one of these, what was the instruction?

**Daniel Lopes:** Like what was the query, you know?

**Daniel Lopes:** And it's just like there's so much  on the left here.

**Daniel Lopes:** And like I have to like squint to like look what was the query that was sent.

**Daniel Lopes:** And there's no way for me to see the API call, because we don't, sometimes we're going to wrap the API call to X in an activity, so you just see the in and out of the activity, you don't see the trace of the API call.

**Daniel Lopes:** So for that, there's no way, I have to add logs and look at the logs in the terminal.

**Daniel Lopes:** And I also have no tracking on the cost, so I have like X dashboard of cost here, hoping that it will refresh their charts fast enough, but nobody ever does.

**Daniel Lopes:** So you don't really know how much you're spending, even in testing.

**Daniel Lopes:** Like today I woke up and it was like 30 bucks cost.

**Daniel Lopes:** And it's okay, takes like a day, 24 hours for them to aggregate the cost.

**Daniel Lopes:** So that's another thing that's kind of a pain yes when dealing with APIs.

**Daniel Lopes:** And then what I wanted to do is, also like they had a bunch of options for stuff that I wanted to try.

**Daniel Lopes:** So like, am I using the right attributes?

**Daniel Lopes:** I was asking the agents like, hey, this is the docs, are we using the right stuff?

**Daniel Lopes:** And it's okay, like maybe different parameters, it wouldn't be a good idea and all that.

**Daniel Lopes:** Because what this EXA agent does is pretty crazy, because it will use all their tools.

**Daniel Lopes:** So whatever you give, it might decide to crawl, it might decide to search, and it has input schema, it has a bunch of stuff that you can do.

**Daniel Lopes:** And so I was playing with that at the same time and resetting, but ideally, I would be able to reset at that level.

**Daniel Lopes:** And Temporal actually lets you do that, so I could just change the exit here, go in here.

**Daniel Lopes:** And I click on this, so now I'm inside this one, so I can reset from here, which is great.

**Daniel Lopes:** So I can change the parameter reset from here, the hot reload usually picks up.

**Daniel Lopes:** If it doesn't pick up for some bug, and I have to reset, we lose all the history.

**Daniel Lopes:** So all my executions are gone, and because of just the temporary database with the run, so I have to restart.

**Gianpiero Puleo:** Can you say again, like when you're here?

**Gianpiero Puleo:** Like, why we want to resect a specific step here?

**Daniel Lopes:** What was your intention?

**Daniel Lopes:** Because they had, like, let's say I'm iterating with XA API calls, and, like, I want to test different API calls.

**Daniel Lopes:** So in this case, we have tool calling in the executor.

**Daniel Lopes:** So the executor has, I think I should scroll to the session.

**Daniel Lopes:** So the executor has tool calling in this way.

**Daniel Lopes:** So, and the tool calling is assuming things like this, XResearch, XPro, IsRetry, Priority, and it will pass to this.

**Daniel Lopes:** So I changed, let's say I'm changing the params here, and I'm adding more params, you know, and I want it to reset just to execute the research tools.

**Daniel Lopes:** So I would go here and say execute research.

**Daniel Lopes:** ResearchTools, this one is activity, I never can find where to reset exactly, so I guess, that would be like, okay, like it's, that one is like research activity, execute tool, make research, this one, 53, there was another one before, this is in reverse, so it's a top down now, because I'm inside of a sub workflow.

**Daniel Lopes:** So each flips, you know, so, an ascending order, it's like, if you're in the parent one, it's in ascending, if you're in the child, it's in descending order.

**Daniel Lopes:** So, if I go here, and I, okay, research, so this is 89, 89, what's the name of it again?

**Daniel Lopes:** Okay, 89, so there's no button to reset from here, you know, so what I need to do is, scroll all way back to the top, if I change the API client, and reset at 89, or 88 to the one before.

**Daniel Lopes:** Okay.

**Daniel Lopes:** And then it will continue from there.

**Daniel Lopes:** But that doesn't reflect on the studio.

**Daniel Lopes:** So now it's a completely new fork that is running with this change.

**Daniel Lopes:** So if I want to run the whole thing again, I have to go back into the studio and input manually the original input, and then we'll start a fresh new one.

**Daniel Lopes:** Like if I reset from here, we'll pick up.

**Daniel Lopes:** And it will show up in the studio.

**Daniel Lopes:** But it has no parent.

**Daniel Lopes:** There's no supervisor above because it didn't start from the supervisor.

**Daniel Lopes:** started directly from there.

**Daniel Lopes:** So now I'm no longer testing the supervisor if I'm just using the studio.

**Daniel Lopes:** But it helps.

**Daniel Lopes:** So I'm doing all this stuff.

**Daniel Lopes:** And then let's say I did all that and I got to something that I'm happy with.

**Daniel Lopes:** The thing that I really wanted to see here is...

**Daniel Lopes:** you.

**Daniel Lopes:** At least in this mode would be this.

**Daniel Lopes:** So this looks good.

**Daniel Lopes:** This one passed in just one shot.

**Daniel Lopes:** Great.

**Daniel Lopes:** It has some problems, but makes sense.

**Daniel Lopes:** If I go into, like, the executor ones, there's no way for me to see here which ones are, like, they have, like, quality score.

**Daniel Lopes:** This is all great.

**Daniel Lopes:** But it's kind of hard to see.

**Daniel Lopes:** Like, if we're thinking, like, can I spot problems easier?

**Daniel Lopes:** Like, ideally, I would see, like, stuff like this in, like, in a more visible way.

**Daniel Lopes:** It could be even, like, I don't know how.

**Daniel Lopes:** I'm not thinking how, but, like, I have to, like, spot scroll here and, like, okay, where did we drop the ball?

**Gianpiero Puleo:** Well, I think this is similar to the previous point.

**Gianpiero Puleo:** Like, if you click on the flow, like, where you see the graph.

**Daniel Lopes:** Yeah.

**Gianpiero Puleo:** think what you're saying is in synthesized results, like, when you click on that node, you should have,

**Gianpiero Puleo:** Like a good summary of the key metrics and a good way to see the output.

**Daniel Lopes:** In my mind, like metrics or like however they are done in this kind of setting is very important.

**Daniel Lopes:** So it's a separate thing, you know, where should always have its own thing here at the top.

**Daniel Lopes:** I don't know how we do it.

**Daniel Lopes:** But I'm literally like doing this, like command G here and trying to look, is there anyone low?

**Daniel Lopes:** And then if there is like a 75, why?

**Daniel Lopes:** And then I would just like look at it manually, you know?

**Daniel Lopes:** And then same thing.

**Daniel Lopes:** And then if it's low, sometimes like, okay, how do I open this now?

**Daniel Lopes:** So I would be like, I go to the workflow and then I search for that, you know?

**Daniel Lopes:** So like, , now it's going to be hard to find.

**Daniel Lopes:** And then if there's a problem, like for example, I just like, I'm going to give you like one final one.

**Daniel Lopes:** And where, I think it's going to be the last execution.

**Daniel Lopes:** I was literally reading the last execution.

**Daniel Lopes:** Right before a call to see if there is a problem.

**Daniel Lopes:** And most people will not do this.

**Daniel Lopes:** So that's why when I have more complicated workflows, I kind of don't trust the team to do it.

**Daniel Lopes:** Because they're not going to read a 2,000 words document with six other tasks that they need to do for different clients.

**Daniel Lopes:** So that's why I'm doing the agent one.

**Daniel Lopes:** So like in this case, for example, execution two hours ago, it generated this gigantic final report, which is what I wanted.

**Daniel Lopes:** And then this doesn't have, if I'm in like in 3D mode, at the workflow level, the 3D mode happened.

**Daniel Lopes:** I think maybe I don't have it local.

**Daniel Lopes:** Sometimes it should have a 3D mode, but I think maybe I didn't pull on this computer.

**Daniel Lopes:** But in 3D mode, I would see it, but we truncate now because it was breaking the size.

**Daniel Lopes:** But I would just, I just grabbed this whole thing and I gave it.

**Daniel Lopes:** To Claude, to fix the formatting.

**Daniel Lopes:** And then I was reading this stuff like one by one and checking all the links and checking if it makes sense.

**Daniel Lopes:** Like, is there a real client?

**Daniel Lopes:** Is our Davis in TechCrunch?

**Daniel Lopes:** Like, I'm reading this like one by one, you know, and I've done this the whole night for like pretty much all the runs that it did.

**Daniel Lopes:** So I could spend almost more time reading the results and actually ending the prompts than in code.

**Daniel Lopes:** And then in code, I just asked Claude to do everything and pretty much did it.

**Daniel Lopes:** But then, like, I'm reading the whole thing.

**Daniel Lopes:** Everything makes sense.

**Daniel Lopes:** And then, like, look at this.

**Daniel Lopes:** At the end, this leadership part.

**Daniel Lopes:** One of the questions is, is it this one?

**Daniel Lopes:** I think it's another one.

**Daniel Lopes:** Yeah, this one.

**Daniel Lopes:** So, I have like...

**Daniel Lopes:** Multiple versions of the reports.

**Daniel Lopes:** And one of the questions here is this.

**Daniel Lopes:** Oh, man, I think I lost it.

**Daniel Lopes:** It was an open-ended question about leadership.

**Daniel Lopes:** And it just, XA thought it was just like a general question about leadership as a whole, not related to metronome.

**Daniel Lopes:** So my plan didn't, the prompt should be specified to make it more standalone.

**Daniel Lopes:** So the question gets the context of what is the broad thing we're trying to research.

**Daniel Lopes:** But now how do I do that?

**Daniel Lopes:** Like, do I extend the prompt or not?

**Daniel Lopes:** And it was just one in the mix.

**Daniel Lopes:** You know, it's like ideally I'll come to like link fuse.

**Daniel Lopes:** So that's what I was doing right before.

**Daniel Lopes:** I was like looking at my last execution in link fuse here.

**Daniel Lopes:** And I was, okay, synthesize, finding.

**Daniel Lopes:** This is.

**Daniel Lopes:** The executor, I need the supervisor.

**Daniel Lopes:** So the supervisor is here.

**Daniel Lopes:** The last one, okay, 30 cents, that's a lot.

**Daniel Lopes:** So like how much, I was here to just fix something else, but immediately like, oh, 30 cents, shoot, that's why it takes so long.

**Daniel Lopes:** So synthesizing sometimes takes six minutes.

**Daniel Lopes:** It makes sense.

**Daniel Lopes:** Like, okay, like what's the amount of input here?

**Daniel Lopes:** It's like a gigantic amount of tokens, you know?

**Daniel Lopes:** And am I using Opus here instead?

**Daniel Lopes:** So I had Opus before, so I switched.

**Daniel Lopes:** But, okay, the research plan, okay.

**Daniel Lopes:** Now I'm not doing something else.

**Daniel Lopes:** I'm just looking at this.

**Daniel Lopes:** But then if I go back and show, okay, supervisor of this, the whole cost of thing was 40 cents.

**Daniel Lopes:** Ideally, I would know 40 cents plus the cost of exit.

**Daniel Lopes:** How much did that cost?

**Daniel Lopes:** Is it for three bucks, four bucks?

**Daniel Lopes:** Might be.

**Daniel Lopes:** And then how do I find the executor that had the problem?

**Daniel Lopes:** You know, because now I

**Daniel Lopes:** to change the plan at the top level, and this is the prompt that I need to change, because I need to somehow change it to make the questions, if unclear, or if generic, make it be specific.

**Daniel Lopes:** So I would open the playground here.

**Gianpiero Puleo:** Yeah, I was going to ask, because you identified the issue from looking at the output, right?

**Gianpiero Puleo:** Like, you know, ideally, we would have better ways for you to spot it, like some metrics, and hopefully, maybe LLM is a judge that actually looks at the output and flags, like, a few problems.

**Gianpiero Puleo:** But either way, like, you spot an issue by looking at the output, so then you know that that's something that you want to fix in the prompt.

**Gianpiero Puleo:** So then what do you go to Langfuse for?

**Gianpiero Puleo:** Because you know where the prompt is.

**Daniel Lopes:** Yeah, I was going to go for, like...

**Daniel Lopes:** Like, trying out with the playground with all the data defined there.

**Daniel Lopes:** So, but like, this is the problem.

**Daniel Lopes:** So this is the exact one I was looking for.

**Daniel Lopes:** So leadership team research methodologies, it just made up a whole thing about general research.

**Daniel Lopes:** Confidence score is great, makes sense.

**Daniel Lopes:** But the question was just generic, but I don't see the question here.

**Daniel Lopes:** The question is gone.

**Daniel Lopes:** So ideally, I would be able to just, like, search for this.

**Daniel Lopes:** Like, or be able to see where that came from.

**Daniel Lopes:** And we don't have a way to do that easily.

**Daniel Lopes:** So I would have to, like, well, I can't find that.

**Daniel Lopes:** So I can't find that in link fields easily.

**Daniel Lopes:** I can't find that in temporal easily.

**Daniel Lopes:** In the studio, would probably get close.

**Gianpiero Puleo:** So that would be, like, for you, that would probably be the output from the prompt to the previous step.

**Gianpiero Puleo:** That generated.

**Daniel Lopes:** Leadership framework.

**Daniel Lopes:** There's something, now I have so many things open that I don't know which one I triggered.

**Daniel Lopes:** So, because I had to paste it here, because the hour stuff doesn't render, and Temporal doesn't render Markdown either.

**Daniel Lopes:** But if we're working with documents for humans, we should have a way to see that.

**Daniel Lopes:** But then I would go to linkfuse for like, okay, I kind of know that the questions are generic.

**Daniel Lopes:** I want to try changing this prompt.

**Daniel Lopes:** I don't want to copy this whole thing and paste and clothe again, because here it has my values, you know, and I can add more values.

**Gianpiero Puleo:** The prompt play around the clothe?

**Gianpiero Puleo:** Yeah.

**Gianpiero Puleo:** You would not?

**Daniel Lopes:** Here I have all my production data, so I can just like literally just like start a new one, and like maybe it was a problem.

**Daniel Lopes:** Or maybe I want to try a different version, or maybe I want to try a different temperature, you know?

**Daniel Lopes:** So you have all these things, and it's using...

**Daniel Lopes:** My input here.

**Daniel Lopes:** And one thing that I really like about Cloud, the console, Entropic console, is the ability to set a table with a bunch of stuff.

**Daniel Lopes:** GitHub model does that as well.

**Daniel Lopes:** So I could do this with this input, but I can also use other inputs.

**Gianpiero Puleo:** pictures are talking about, like a table of inputs that you can run with different models or even the same model, but different prompts or whatever.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** They do have that.

**Daniel Lopes:** Like if I go back, I can add to the data set.

**Gianpiero Puleo:** Yep.

**Daniel Lopes:** And I can create a data set and then I can play it in the playground with the data set.

**Daniel Lopes:** But you know what mean?

**Daniel Lopes:** Like I'm just jumping around everywhere to solve a simple thing.

**Daniel Lopes:** like pretty much nobody will do this.

**Daniel Lopes:** So unless you have a really high level of persistence.

**Gianpiero Puleo:** And like most of the tools don't happen.

**Gianpiero Puleo:** I thinking, no, when you were, I shouldn't say that in front of my boss, but like, when you show me what you did, it's like, I don't think I would have the fortitude of reading the same research report line by line for like 25 times.

**Daniel Lopes:** We shouldn't optimize it.

**Gianpiero Puleo:** Exactly.

**Daniel Lopes:** So ideally, we'd have like spot recognition, the parent matching the thing automatically, and I don't know.

**Daniel Lopes:** But like, essentially, like, I'm just jumping, like, Anthropoconsole, our studio, because it does a lot of things right, especially executions.

**Daniel Lopes:** So like, I used to have Postman for everything, and Bruno, but now I'm just using the executions from our stuff, because it's just better.

**Daniel Lopes:** And I also just go to like studio production here all the time, and I would just like grab the raw input, paste in my local stuff, and then I have exactly a reputation.

**Daniel Lopes:** Another thing I do sometimes is that I think most people don't know it's possible.

**Daniel Lopes:** And I would download temporal data.

**Daniel Lopes:** So I would just come here, and I do the download.

**Daniel Lopes:** And if you use encoded, you can run in your VS code.

**Daniel Lopes:** This I don't do as much.

**Daniel Lopes:** What I've been doing with Cloud quite a bit is just download it in readable and give it and say, what happened?

**Daniel Lopes:** Where is the bug here?

**Daniel Lopes:** And it will usually help.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** But ideally, would download this and be able to import in our studio.

**Daniel Lopes:** And you get that execution precisely.

**Daniel Lopes:** And then you can reset from there and iterate from there.

**Daniel Lopes:** So at least that would be the stuff that I've done.

**Daniel Lopes:** I avoided coding a lot of stuff because I really liked that part of Aops, where I could just go back to a node, rerun that node over and over and over, and then now it's done.

**Daniel Lopes:** And that's why I was looking for Temporal, because Temporal had the mechanisms to be able to do that.

**Gianpiero Puleo:** But anyway, if I can recap, I think, some of the patterns that I picked up from you describing your workflow is like, first of all, it sounds that what we have in studio here, it's right now a good starting point.

**Gianpiero Puleo:** Like, when you want to run a workflow, I think we're close.

**Gianpiero Puleo:** I think we can do better with the inputs so that you don't have to keep copying and pasting, like, if you want to try and rerun the same thing, like, over and over.

**Gianpiero Puleo:** But ultimately, like, you get started here.

**Gianpiero Puleo:** And then once you have a run, then your investigative work starts.

**Gianpiero Puleo:** And then already, like, in the first, what you get back, like, in the execution, we could surface already, like, some of information a little bit more easily.

**Gianpiero Puleo:** That could be some quality metrics, some custom metrics, potentially, for that workflow.

**Gianpiero Puleo:** Some probably, like...

**Gianpiero Puleo:** ...

**Gianpiero Puleo:** ...

**Gianpiero Puleo:** ...

**Gianpiero Puleo:** ...

**Gianpiero Puleo:** ...

**Gianpiero Puleo:** Thank

**Gianpiero Puleo:** We call them, sorry, standard metrics, such as execution time, but accurate, so taking into account the sub-workflows, and also things probably from the model, like bias and all of that, that I think could be applying to any content.

**Gianpiero Puleo:** But then, when you start drilling down, that's when this falls apart, because then you start going to temporal.

**Gianpiero Puleo:** And I feel, again, like, I don't want to put words in your mouth, but like, with temporal, then you almost get the opposite problem, where now instead you got like too much information, and the one that you need instead is kind of like hidden really deep, and so we could actually simplify and extract.

**Gianpiero Puleo:** And perhaps to kind of also bridge, it sounds like here, for example, we should ideally be able, in the workflow, to drill down to the level of the single activity, basically kind of going into the temporal execution to the single activity run.

**Gianpiero Puleo:** So actually then you could do things with that particular run, like whether it's like rerun it or see what happened, et cetera.

**Gianpiero Puleo:** And then I think when you get to a point from there where it's like, okay, this is coming from one specific prompt, we could switch to now sort of prompt playground mode for that particular one.

**Gianpiero Puleo:** But it should take all the intelligence from the workflow because, for example, because I'm working on a run, like if that particular prompt has been fed with certain inputs, should be easy to kind of bring those inputs in.

**Gianpiero Puleo:** But like at that point, you're really like iterating on the prompt itself.

**Gianpiero Puleo:** And so, again, let's present the same metrics, but let's also make it easy to kind of work with a bunch of inputs, a bunch of parallel runs, and a bunch of different variations.

**Gianpiero Puleo:** And then I guess really you want to be able to traverse this hierarchy back and forth, like in the easiest possible way, because sometimes you want to see it at kind of a whole workflow level.

**Gianpiero Puleo:** But then again, like, you maybe do another run, and then you go into an activity, you do a run of that, then you go into prompt, you play a little bit with the prompt, then you kind of step back.

**Gianpiero Puleo:** And at each point, the last thing that I picked up on you is that really, I think, like, working together to identify what's the right information.

**Gianpiero Puleo:** Because, for example, here on a temporal run in an activity, if you scroll down a little bit, Daniel, sorry, where you get the, like, any of those steps, like, if you can expand any of those steps.

**Gianpiero Puleo:** Yeah, basically, here, for example, I would say, like, roughly speaking, it's kind of like almost everything is on the left.

**Gianpiero Puleo:** You kind of don't care, really.

**Gianpiero Puleo:** Yeah, then once it's like, did I get that right?

**Gianpiero Puleo:** What was the input?

**Gianpiero Puleo:** What was the output?

**Gianpiero Puleo:** And if there was, like, an error, like, that's, I think, where we can be really smart in connecting with code.

**Gianpiero Puleo:** It's like, where did it go wrong?

**Gianpiero Puleo:** Like, what was the API call, et cetera?

**Gianpiero Puleo:** So kind of bridging that gap.

**Daniel Lopes:** That's sort of the stuff that I picked up from you describing.

**Daniel Lopes:** The thing that I really wish it was possible, like in this case, for example, this is the executor workflow.

**Daniel Lopes:** So let's go in into the executor workflow and then probably be even better.

**Daniel Lopes:** So give me one sec, sorry.

**Daniel Lopes:** Workflow ID.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So let's see.

**Daniel Lopes:** So let me get one that has an LLM call.

**Daniel Lopes:** Yeah, data store data, synthesize to result.

**Daniel Lopes:** So this one is just one LLM call.

**Daniel Lopes:** So I can, I have an input for this activity.

**Daniel Lopes:** None of this matters much.

**Daniel Lopes:** And it takes 50% of the real estate.

**Daniel Lopes:** And then this, I don't care as well.

**Daniel Lopes:** But inside here, I know there is an LLM call.

**Daniel Lopes:** So the only way for me to find this now is to go into Langfuels.

**Daniel Lopes:** Like ideally you would get the, any API calls.

**Gianpiero Puleo:** Like I think there's like.

**Gianpiero Puleo:** You wouldn't know.

**Gianpiero Puleo:** Yeah.

**Gianpiero Puleo:** It was a prompt here.

**Daniel Lopes:** So you should be able to kind of jump into that prompt call and, again, like, just see the input, the output, and potentially play around with that particular, yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Like, in my mind, there's, like, primitives.

**Daniel Lopes:** There are two kinds of primitives in this space.

**Daniel Lopes:** We're essentially building, like, a heavy automation.

**Daniel Lopes:** Like, automation is a heavy system.

**Daniel Lopes:** And there's two.

**Daniel Lopes:** There's regular APIs and then there's LLM APIs.

**Daniel Lopes:** And to me, like, if there was a regular API here in the mix, like, if this is an agent in the loop and it's making API calls, I want to see them here, you know.

**Daniel Lopes:** And any LLM call, I want to see them as well.

**Daniel Lopes:** So there's no way for me to see the API calls to exit anywhere because, like, that's not in LinkFuse either.

**Daniel Lopes:** So, like, LinkFuse, we at least get the LLM stuff.

**Daniel Lopes:** There's no way to see the other API calls.

**Gianpiero Puleo:** So two calls are essentially opaque.

**Gianpiero Puleo:** Yeah, they're not in the same system for them.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And, like, another thing that, like, ideally, let's say, like, I'm looking at this and, like, you

**Daniel Lopes:** Doing like what you're saying, like maybe we can go into the prompt or I can go into the API as well.

**Daniel Lopes:** And then I can toy with the inputs for the API and change the values and see.

**Gianpiero Puleo:** Leto in API call to X, for example, like whatever we pass to that, what do we get back?

**Daniel Lopes:** Yeah, that would be the dream, but maybe we don't have to do that.

**Daniel Lopes:** But at least the link views one, if we have a prompt playground here, sorry, the LLM cause, if we have prompt playground and you go into that, ideally, we'll keep the context of like, where is this is running?

**Daniel Lopes:** Because you lose that the moment, like when the link views, if you're here, you have the context.

**Daniel Lopes:** And you can jump around and you can think about the moment that I go into the playground, it's disconnected.

**Daniel Lopes:** So I cannot even pull the data from this anymore, you know.

**Daniel Lopes:** This is cool, I think you can see the...

**Gianpiero Puleo:** So those API calls you refer to, let's say the one to XC, like are those API...

**Gianpiero Puleo:** Calls that the LLM is making, like the agent decides to call it.

**Gianpiero Puleo:** Because to me, for example, whatever is provided to the LLM as a tool would be actually relatively straightforward to kind of trace and include.

**Gianpiero Puleo:** But in here, like if it was an LLM kind of working here and the LLM made a call because it was a tool to kind of call the exit, then I think it would be more straightforward.

**Gianpiero Puleo:** But if it's our code outside of sort of the LLM lifecycle making an API code, that's the part that I think can be like tricky because then it's just like really going into analyzing code execution as opposed to the, yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah, that might be a tricky one.

**Daniel Lopes:** Like just seeing what was the, I think like ideally it would have that worker module we have today, it would have some sort of proxy or wrapper around that.

**Daniel Lopes:** So anytime the API code.

**Daniel Lopes:** We trace it, you know, so you would see the traces here, you know, so you at least can copy that, and I could go to access dashboard, and then use the same prams there, you know, or something like that.

**Gianpiero Puleo:** And then, Ben, with the stuff that you've been working on in terms of visualizing, essentially, so I forget what the acronym is, the AST, the...

**Ben Church:** Abstract Syntax Tree.

**Gianpiero Puleo:** Okay, so, because I think what you and I discussed, like, when you worked on that, you told me, if I remember correctly, that obviously, for the proof of concept, you cannot pretty much, like, print it out, so to speak, the entire AST, but then if we wanted to kind of show it as a graph view, we will probably kind of do it, like, a little bit more high level.

**Gianpiero Puleo:** But it sounds to me that that could be also something that is parameterized, because I think what, Daniel, you're doing here is essentially what you...

**Gianpiero Puleo:** Oh, in temporal, really, you're going down to a single execution of potentially a single instruction.

**Gianpiero Puleo:** And then I think I was thinking, okay, but how do you visualize it in a decent way?

**Gianpiero Puleo:** And that's where I think, like, maybe the AST can, the representation can help because I guess you could really go down to a single instruction there, right?

**Ben Church:** Yeah.

**Ben Church:** Yeah.

**Ben Church:** It's, like, how we, in that view, it's, like, okay, we can find all the nodes in the function calls, and then we can color those functions.

**Ben Church:** You know, it's an activity function.

**Ben Church:** It's a prompt function.

**Ben Church:** It's generic.

**Ben Church:** And then it's up to us to go, like, okay, that's the scaffold of the UI.

**Ben Church:** It's up to us to, like, apply meaning to that skeleton, which is, like, what code does it actually relate to?

**Ben Church:** Has it been run?

**Ben Church:** And what inputs has it been run for and passed?

**Ben Church:** were the outputs?

**Ben Church:** And then, like, how do you...

**Ben Church:** Say for an activity, do these actions for a prompt, you have a prompt playground, but we have the skeleton there in that experiment.

**Ben Church:** I've got a question in here, which is like a little bit different than our, how the UI works and more back on how Daniel thinks.

**Ben Church:** Do you think this is a good time to ask him?

**Ben Church:** Yeah, 100%.

**Ben Church:** Yeah, yeah, please.

**Ben Church:** Yeah, what was interesting in there was one of the many things, it's like, okay, we got to kind of like get these features together.

**Ben Church:** And one thing my brain caught on to was LangFuse, it's kind of tagging these runs, right, with latency and stuff like that.

**Ben Church:** And I can imagine at the beginning when you're saying, I've got to read all these things, all these outputs myself and discern if like they're good or not, right?

**Ben Church:** And we want to make many of these loops faster, but like discerning if the output.

**Ben Church:** What was quality is one of those loops.

**Ben Church:** So that's where like kind of our concept of evals come in.

**Ben Church:** And this is something I don't know.

**Ben Church:** Whereas, Daniel, when you're thinking about building a new workflow, at the beginning, are how to evaluate quality at all on your mind?

**Ben Church:** Or is like, does that step similar to me and maybe GP come, oh, now that the workflow is running, now I'm thinking about evals.

**Ben Church:** Like, at what point do you start thinking about how you'd measure or test if it's correct or not?

**Daniel Lopes:** Most of the times that I get the plan right faster, I start from the, at least from the example.

**Daniel Lopes:** Like that was what I did with the plan, where like I started, like I wrote the whole plan by hand.

**Daniel Lopes:** And then I got the system message in Entropic Console to behave like that.

**Daniel Lopes:** So same thing.

**Daniel Lopes:** you're in the plan?

**Ben Church:** Huh?

**Ben Church:** Are it just quality outputs you put in the plan, or do you have evals, like how you measure if the output's good or not?

**Daniel Lopes:** Yeah, I started with just the plan, like what I wanted, and the input.

**Daniel Lopes:** Like what was the input that I wanted, what was the output that I wanted?

**Daniel Lopes:** So the example, mean, just like that, literally like that exemplar, if we're using like the ML nomenclature.

**Daniel Lopes:** And that one, so that's usually what I do.

**Daniel Lopes:** It's just like, what's the input and output that I would be happy with?

**Daniel Lopes:** And then if I just feed that into the generate prompt from the console from Entropic, they will create the placeholder.

**Daniel Lopes:** So the placeholder will be like, give an X, Y, and Z, look for whatever.

**Daniel Lopes:** They expand, and then I iterate on that expansion.

**Daniel Lopes:** So they're creating the placeholder using my example, and then they usually also put the...

**Daniel Lopes:** ...

**Daniel Lopes:** What is good and what is bad?

**Daniel Lopes:** So I get that automatically because I'm inside their console.

**Daniel Lopes:** But if I'm not, that's another thing that I see.

**Daniel Lopes:** Like the other folks, they will start from Claude, and Claude will just, or there's a certain cursor, and the cursor will write a couple of paragraphs of prompt only.

**Daniel Lopes:** And that's usually that's what goes live.

**Daniel Lopes:** That's why I created rules for prompts, trying to mimic the console philanthropic behavior of always including exemplars, including a placeholder and including what is good and what is bad in the prompt.

**Daniel Lopes:** So that is on one call, but ideally, we would have a check as well.

**Daniel Lopes:** So if you have any LLM call, ideally, we have a check system.

**Daniel Lopes:** And that check system should take some of that stuff from that initial prompt and create a dedicated one for that one.

**Daniel Lopes:** So like in my plan, for example, for if you see the plan that I was creating, I had...

**Daniel Lopes:** that as a success criteria attribute, because I wanted to, I knew I would wanted to check that.

**Daniel Lopes:** So like here, on the first version already, the original plan that I wrote had success criteria.

**Daniel Lopes:** So when I wrote this success criteria, for the, this one doesn't have the query.

**Daniel Lopes:** This one has, so this, and then success criteria, because I knew I want to have another prompt, just to check if it passed the success criteria.

**Daniel Lopes:** So I was doing essentially two prompts at the same, thinking about the two systems at the same time here.

**Daniel Lopes:** And I've been doing that quite a bit.

**Daniel Lopes:** So the, all the agents are like this, with their introspection check, you know.

**Daniel Lopes:** But yeah, even before I started thinking about, looking like we should probably run the second.

**Daniel Lopes:** An activity on every activity.

**Daniel Lopes:** I was always doing this.

**Daniel Lopes:** like, I was always, like, because I start always with the entropic, and they do that.

**Daniel Lopes:** So I would be, like, feed the example, and then they would do this.

**Daniel Lopes:** And then at the end, they usually put, like, a good and bad as well.

**Daniel Lopes:** And it's just, like, just a practice that came from using their stuff, because I think their stuff is way better than anything else.

**Daniel Lopes:** So if I just go here, it will force me in that direction.

**Daniel Lopes:** I generate prompt, and I just paste an example.

**Daniel Lopes:** Like, if I literally just copy this example here, it will generate the exact same thing.

**Daniel Lopes:** So if I get the input.

**Daniel Lopes:** Like, I continue to make it.

**Daniel Lopes:** You

**Daniel Lopes:** I don't know why they don't have this checked by default, thinking enabled, have the cloud and freezing by default.

**Daniel Lopes:** And then they will be lazy on the example.

**Daniel Lopes:** So if the example is long, I have to repaste the example.

**Daniel Lopes:** And Cursor does that a lot.

**Daniel Lopes:** So they removed the example, but the gist of it is there.

**Daniel Lopes:** So I'll continue here and then copy back and put it back there.

**Daniel Lopes:** But the definition of good and bad, they spelled it out pretty well.

**Daniel Lopes:** Sometimes you'll get it better because it just has more.

**Daniel Lopes:** This one is a long one, so I think that's why it stripped it out.

**Daniel Lopes:** But if the example is short, it will keep it.

**Daniel Lopes:** So like for titles, for meta descriptions, for introductions, for stuff like that, they usually keep all the examples.

**Daniel Lopes:** you give a bunch of the examples.

**Daniel Lopes:** And they made it worse, actually.

**Daniel Lopes:** They had a different interface before that it would do this for you, and have it in the code.

**Ben Church:** Have you shared this JSON plan generating?

**Ben Church:** Would you be willing to share the couple of prompts you have here?

**Ben Church:** Yeah.

**Ben Church:** Are you curious about the vendor system a little bit?

**Ben Church:** I think they can make it.

**Daniel Lopes:** That's a different type of Yeah.

**Daniel Lopes:** But, like, see, like, this is super cool.

**Daniel Lopes:** So you can keep generating test cases.

**Ben Church:** That's okay.

**Ben Church:** Oh, yeah.

**Daniel Lopes:** But it's messed up.

**Daniel Lopes:** So, like, research mode should be the ones that I gave.

**Daniel Lopes:** Secondary, hybrid, like, sorry, primary, strict, hybrid, and exploratory.

**Daniel Lopes:** So, like, made up the  here.

**Daniel Lopes:** But, and then you can run.

**Daniel Lopes:** So, that is.

**Daniel Lopes:** This is essentially what GitHub just implemented.

**Daniel Lopes:** They've had this for forever.

**Daniel Lopes:** And I think it's the best, other folks have that as well.

**Daniel Lopes:** HumanLoop has that.

**Daniel Lopes:** And you can iterate on the prompt here and you can see what was the prompt at the time.

**Daniel Lopes:** You can iterate on the prompt on the version and you can see the version that ran it, the temperature and the other settings.

**Daniel Lopes:** So, and then you can label it.

**Daniel Lopes:** So I use this quite a bit when I'm iterating on the prompts.

**Daniel Lopes:** And I think I'm the only one in the team because I've showed this, I teach, I taught this to everybody when they're on board and I only see my stuff here because this is the shared account.

**Daniel Lopes:** So if nobody's using this and then nobody's using length use, we're essentially iterating on prompts just blindly based on what we see in production and using cards.

**Daniel Lopes:** So that to me, like ideally, like the best system would be like, we would be able to flag, download, use that, and connect, you know?

**Daniel Lopes:** So it's such a hard, like I would write everything better in the documents that I was writing because I think it explains the, at least how I'm thinking about this as a whole.

**Daniel Lopes:** Because I think it's a completely different way of coding, that you code more based on outputs and you move more of the heuristics into the prompts than in algorithm, you know?

**Daniel Lopes:** And you see like there's this bias for code generation to generate in algorithm.

**Daniel Lopes:** And that's what just happened to Maestra using the system.

**Daniel Lopes:** we basically need to like force code generation to generate the minimal amount of code.

**Daniel Lopes:** And I think we're going to need a special thing for prompting.

**Daniel Lopes:** This is what Entropic has here, but we need to have a special for our kind of like use case, you know?

**Ben Church:** What is my opinion on quality here?

**Ben Church:** What's my systematic things to check for?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** It kind of sucks.

**Daniel Lopes:** changed the UI, but they had exactly that before.

**Daniel Lopes:** So that's why I was like, their prompt generation, they had a two-step phase where that modal that opened with just one text area now, it had before, describe what you want and give us an example of good.

**Daniel Lopes:** And that would generate the prompt, and they removed that.

**Daniel Lopes:** I don't know why.

**Daniel Lopes:** I think they wanted to make the evaluation table better and all that, but that was literally the beginning of like every prompt was the two-step.

**Daniel Lopes:** Describe roughly, give us one example.

**Daniel Lopes:** And then they also had another one that was like improve, a prompt improver.

**Daniel Lopes:** There was a second button here that...

**Daniel Lopes:** So I haven't heard of that that one.

**Daniel Lopes:** Yeah, so they had one that you could just feed it and give it like, you messed up the examples, or you made the examples, the examples here are too short, make them better.

**Daniel Lopes:** So I was always using these two things, you know.

**Ben Church:** I didn't know that I removed that.

**Ben Church:** I haven't used it for a while, but yeah.

**Ben Church:** That was the basis of the console.

**Gianpiero Puleo:** I need to go, but I'll be back after dinner.

**Gianpiero Puleo:** So if you guys want to feel free to go on, because anyway, it's recording.

**Gianpiero Puleo:** So I'll kind of catch up with whatever else you discuss in a little bit.

**Daniel Lopes:** I think I can just write, today I'll finish the two articles that I have, and then send it.

**Daniel Lopes:** Because I think it's the ideal process, regardless of how you do it.

**Daniel Lopes:** Because I'm thinking, yeah, you can just share the thinking there.

**Daniel Lopes:** No, for sure.

**Gianpiero Puleo:** I mean, even what you described, and even the discussion you just said with Ben, like, to me, kind of...

**Gianpiero Puleo:** Cleared out a lot of the stuff personally that I was, yeah, where I wasn't sure.

**Gianpiero Puleo:** Like, for me, it was hugely helpful.

**Gianpiero Puleo:** If you can also put it down, I think that's absolutely even better.

**Gianpiero Puleo:** would be thankful for that.

**Gianpiero Puleo:** But even just this call for me was really, really helpful to kind of understand where we could take things.

**Gianpiero Puleo:** And one thing maybe that I would repeat to see if you're still on the same page, because I think I talked about this with both of you, but separately.

**Gianpiero Puleo:** I think even where the SDK is going and all the CLI tooling is going and the cloud tooling is going, to me, we're in a really good spot for creation.

**Gianpiero Puleo:** And so probably for IDE, we should focus more on expanding the sort of run, inspect, and iterate part as opposed to the creation part.

**Gianpiero Puleo:** So essentially, enter point like it's along the lines of you got the workflow already from somewhere.

**Gianpiero Puleo:** And now, like you.

**Gianpiero Puleo:** Going to the IDE to kind of really figure out how it's working, where to improve things, and kind of like run it and so forth.

**Gianpiero Puleo:** Is that the fair, is that first thing where we are?

**Daniel Lopes:** I think so, yeah.

**Daniel Lopes:** Yeah, one thing that it's super hard for me is that as I write the thing, and as we talk about this, it's such a hard challenge that I'm constantly thinking like, is this even doable, you know, as in...

**Daniel Lopes:** Yeah, it is difficult.

**Daniel Lopes:** Like, are we looking at like a project that needs to be open source, and we need a thousand people contributing over three years, you know, or to get to the ultimate goal?

**Daniel Lopes:** Because like, you couldn't be able to, you wouldn't be able to build Django or Rails by yourself, for example.

**Daniel Lopes:** But, and like the length fuses of the word, it's four people, it makes sense, it's kind of a mess, and it looks like four people project, you know?

**Gianpiero Puleo:** Yeah, but they're taking on like a little slice of what we're talking about.

**Gianpiero Puleo:** mess, it's of Okay,

**Gianpiero Puleo:** Because LangFuse is essentially like they're really only talking about prompts.

**Gianpiero Puleo:** I'm oversimplifying, but essentially it's like, okay, when you get down to the prompt, that's the only thing that we take on.

**Gianpiero Puleo:** We don't care about how to visualize the rest.

**Gianpiero Puleo:** We don't care about basically anything else.

**Gianpiero Puleo:** We just work on prompts.

**Gianpiero Puleo:** I think that on the flip side, we probably need less than what LangFuse gives on prompts, but we need a lot of stuff in other places.

**Gianpiero Puleo:** So, yeah, I do think it's.

**Daniel Lopes:** Yeah, like I think like LangFuse and almost everyone else has started like, oh, prompts, there's an infoprompt playgrounds.

**Daniel Lopes:** And then they build the prompt playground and the tracing, and then they try to add the other stuff after.

**Daniel Lopes:** And I'm trying to think, what is everything?

**Daniel Lopes:** And then what is the beginning that we can start from there and deliver the value, but keep an eye on everything else?

**Daniel Lopes:** And we slowly progress toward that.

**Daniel Lopes:** And it might take four years and a thousand people, you know?

**Daniel Lopes:** So what is the baby version of that that is useful today?

**Daniel Lopes:** Maybe it doesn't, maybe it's not even an ID.

**Daniel Lopes:** You know, like maybe it's like a tracing visibility thing that you just see things there.

**Ben Church:** But anyway.

**Ben Church:** Let's hear a rewrite quickly.

**Gianpiero Puleo:** All right, guys.

**Gianpiero Puleo:** I'll jump off.

**Gianpiero Puleo:** All right.

**Daniel Lopes:** See you, man.

**Daniel Lopes:** I hope this was helpful, Ben.

**Daniel Lopes:** I have a bunch of art because I'll finish them in the next couple hours and I can share it with you.

**Ben Church:** No, no.

**Ben Church:** This is one I'll always read what you got.

**Ben Church:** this is really helpful, particularly from like the UI side.

**Ben Church:** Like just seeing like we're all on the same page of like just getting those inputs quicker and like the feedback loop.

**Ben Church:** We're all on the same page for like there's a bunch of disparate useful information in temporal that we want to get access to.

**Ben Church:** And then the evals still need to explore what the best way to do it is in code.

**Ben Church:** But I'm getting closer to an opinion on what we do for it in UI and I think GP is as well.

**Ben Church:** The only other question I had before I let you leave was just in terms of evaluation.

**Ben Church:** Evaluating LLM outputs, how many scorers or like human as a judge functions do you imagine?

**Ben Church:** Like is it there's a new one per workflow or is it mostly we've got like generic patterns for evaluating stuff and like say for example, human as a judge, we're just changing the prompt and the labels?

**Daniel Lopes:** Yeah, that's the thing that I'm not sure like I need to research more because just yesterday I was reading a bunch of stuff like best practices on LLM as a judge but in my mind it's almost like in the ideal system we would have the judging having dynamic exemplars as there's for sure there's a bunch of standard stuff like there's like almost static things like poison or like since

**Daniel Lopes:** Explicit content and all that stuff, that's pretty much figured out.

**Daniel Lopes:** So there's definitely like a library of things.

**Daniel Lopes:** But then after that, let's say you deploy this and you're running, ideally it will calibrate.

**Daniel Lopes:** So even if you start with like explicit content, like we get hit all the time by the security defense for all the models when we're working for a security company, like Sentinel One and others.

**Daniel Lopes:** So we need, like ideally those things would use the standard and then we would be able to say, this is not bad, this is not bad, this is not bad.

**Daniel Lopes:** And then it would inject in the judge saying, this is fine, don't abort, you know, and like these examples are considered good.

**Daniel Lopes:** So ideally it would be dynamic.

**Daniel Lopes:** As in like, and that's the same for like clients too.

**Daniel Lopes:** So like, let's say you have like writing guidelines adherence is like something that we have in, that it's kind of becoming like from the drafting agent, one of, like there's like four metrics.

**Daniel Lopes:** One is like following the writing guidelines.

**Daniel Lopes:** Another one is following the general direction for the request.

**Daniel Lopes:** So like following the direction is kind of like a general thing, I think.

**Daniel Lopes:** And like some of the metrics frameworks would have that.

**Daniel Lopes:** So, and they call, I think that's under usefulness.

**Daniel Lopes:** It's like a variation of usefulness, but the writing guidelines, ideally that would be also dynamic as in like, oh, I didn't think about this.

**Daniel Lopes:** And like when you're like reading the production stuff, and then you start to see when you had something like don't ever use end dashes.

**Daniel Lopes:** And then there's a use case where it makes sense.

**Daniel Lopes:** like, it's like, okay, same thing for code formatting.

**Daniel Lopes:** It's like, it's like, put all the code formatting in, like, triple ticks.

**Daniel Lopes:** And then there's some cases that, like, where we actually didn't want that.

**Daniel Lopes:** We just want to double, like, inline code, you know?

**Daniel Lopes:** So, like, and ideally, you would be, like, expanding on that.

**Daniel Lopes:** But I don't know where the split is.

**Daniel Lopes:** Like, if you should have that dynamic example being part of the generation or the judge or both, you know?

**Ben Church:** Yeah.

**Ben Church:** But what's very funny, there's an extreme tension point between, like, new world and old world and things in code and things referenced by code.

**Ben Church:** So, like, I think prompts is right at the middle of it.

**Ben Church:** Yesterday, we got into a rabbit hole on prompt versioning, which is, like, a fun topic.

**Ben Church:** I'm like, yeah, I mean, like, you want to probably test out multiple prompts.

**Ben Church:** And then, like, what happens on the other side when one prompt is the winner?

**Ben Church:** Like.

**Ben Church:** Like, how do we go back and prune the code?

**Ben Church:** Same thing, same problem here.

**Ben Church:** It's like, I put out a prompt and a score.

**Ben Church:** Okay, we're doing the loop.

**Ben Church:** We're doing the loop.

**Ben Church:** It's improved.

**Ben Church:** We're doing the loop.

**Ben Church:** But our code is still old prompt.

**Ben Church:** But we want to be able to edit the prompts locally.

**Ben Church:** So then, like, how do you bring the self-healing function back in?

**Ben Church:** That's probably a whole other product to build at some point.

**Ben Church:** Yeah, that's the part.

**Daniel Lopes:** Yeah, I was like, a whole can of worms.

**Daniel Lopes:** But Bridget was, like, I was writing this whole thing and thinking, this thing should be open source.

**Daniel Lopes:** Because this is way too large for us to build by ourselves.

**Daniel Lopes:** And there's so many things at the edge that would provide value that you can't, that it doesn't make sense to be open source.

**Daniel Lopes:** And, like, in the self-healing system would be the kind of stuff that you can't just run that on your machine, you know?

**Daniel Lopes:** Like, essentially, the idea would be fine doing it.

**Daniel Lopes:** And you get, like, a remove out of the prompt.

**Daniel Lopes:** You're going to end up with a small prompt, and over time, keep adding examples, and you're going to hit the ceiling.

**Daniel Lopes:** Today, at least a year ago, the ceiling was between 10 and 20 exemplars on a prompt.

**Daniel Lopes:** After 20 starts to decay, and less than 10, it sometimes will be biased.

**Daniel Lopes:** Let's say you're doing dynamic prompts, for example, and it's injecting things.

**Daniel Lopes:** In code, have the static mask with a placeholder for injecting dynamic exemplars, and then you're putting exemplars from a cloud product based on the input.

**Daniel Lopes:** That, to me, makes sense to be a pain thing that you do.

**Daniel Lopes:** And then you could also have, like, over time, have fine-tuned versions that has that big, so you have, like, a small model just for that task.

**Daniel Lopes:** You know, like, it just does this, and has, it ran through, like, 10,000.

**Daniel Lopes:** And got labeled by the LLM as a judge as good for like 80%.

**Daniel Lopes:** And the humans judged the other 20, create a fine tune that just do writing guidelines for your company, you know.

**Daniel Lopes:** That is a custom model to you.

**Daniel Lopes:** It costs $2,000 to set it up.

**Daniel Lopes:** Now it costs $100 a month for you to use it, you know.

**Daniel Lopes:** Like there's so many things around this ecosystem that it's impossible to run local.

**Daniel Lopes:** That the coding part, I'm like, that is huge and hard, but it's, it doesn't make sense to charge subscription for just deploying like a Node.js app.

**Ben Church:** deploy that anywhere you want, you know.

**Daniel Lopes:** But all the other models stuff is just like that we should charge, you know.

**Ben Church:** Absolutely.

**Ben Church:** But no, I mean, it's like good to be aware about like that.

**Ben Church:** Ooh, like, oh, I think it's going to go here.

**Ben Church:** We're not to build there yet, but I'm not going to block this from there.

**Ben Church:** But yeah, on the prompt side, it's like, that would be a fun product.

**Ben Church:** You know, like one of those where it's like, it's local.

**Ben Church:** You can still edit it and then like, yeah, if you want to use, you know, the self-improver and we make the mechanism where, you know, it feels local, but we pull things down.

**Daniel Lopes:** Anyway, it sends a PR to you with the new version.

**Ben Church:** Yeah, yeah, or like you're always got like the seed version, but, you know, if you have your API key, it's just overriding it and letting you know.

**Daniel Lopes:** Yeah, it's kind of wild.

**Daniel Lopes:** Like if everything was in text files in the folder, something like CloudCode would outperform all these web apps.

**Daniel Lopes:** And I think the calls for MCP API endpoints, let's say we moved all the prompts to like web hosted database and you put an MCP in front of it.

**Daniel Lopes:** You know, it's, I think it's still not as good as like Cloud being able to just like, okay, it's 500 lines.

**Daniel Lopes:** I need to get the first 20, then the next 50.

**Daniel Lopes:** And then it's like chunking the file on the fly with file systems, know, and.

**Daniel Lopes:** If all the infrastructure was in text files, it could probably work.

**Daniel Lopes:** Like I was thinking like tracing, like we don't have like something like parquet files and it's like automatically in the file system.

**Daniel Lopes:** Like, no, like you're running it locally, maybe it's creating the tracing and then you can just point, hey, these are good ones.

**Daniel Lopes:** Look at those.

**Daniel Lopes:** Let's improve the prompt locally, you know?

**Daniel Lopes:** And then if we have something running production, just pull down the changes that you, you saw to the web UI as a good ones, you know?

**Daniel Lopes:** So I don't know if that is a good abstraction, but I like, I'm, I think it's interesting.

**Daniel Lopes:** The whole thing is kind of like wall cloud is so good at managing files, you know?

**Daniel Lopes:** And it wouldn't be hard for us to do the same with our own thing, not to minimize what cloud does as instance.

**Daniel Lopes:** But we can even just put it in the container, you know, call it itself with the guardrails.

**Ben Church:** Just let it go.

**Ben Church:** Yeah.

**Ben Church:** I have a thing about the container side of this.

**Ben Church:** Yeah.

**Ben Church:** Anyway, this was useful.

**Daniel Lopes:** I'm going to.

**Daniel Lopes:** Yeah, I'll send the articles in a bit.

**Daniel Lopes:** And I think that might help.

**Ben Church:** That's good.

**Daniel Lopes:** Yeah, you need to get some of you even updated.

**Ben Church:** Yeah, I'll finish the agent as well.

**Ben Church:** I'm excited about that one.

**Ben Church:** See ya.

**Ben Church:** All right, man.

**Ben Church:** Bye.
