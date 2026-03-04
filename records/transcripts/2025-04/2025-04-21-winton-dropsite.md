# Winton (Dropsite)

<metadata>
date: 2025-04-21
time: 20:01 UTC
duration: 48 minutes
organizer: Daniel Lopes (GrowthX)
participants: Daniel Lopes (GrowthX), Winton Welsh (Dropsite)
fathom_recording_id: 58328601
fathom_url: https://fathom.video/calls/281015219
share_url: https://fathom.video/share/DvqayrgQ6MqNxTPFaExeFHGAux2pYE1m
source: fathom
enriched_on: 2026-03-04 18:25 UTC
</metadata>

---

## Summary

Daniel Lopes presented GrowthX's AI workflow engine (30+ workflows migrated from AirOps to Temporal/Rails) and a new content OS to replace Notion and Airtable, while Winton Welsh showcased Dropsite's pivot from building a comprehensive tool to AI Markdown workflows and LLMFS, a SQLite-based server for code execution. Both founders discovered they'd learned complementary lessons about service-first go-to-market strategies versus product-first approaches, and identified concrete collaboration opportunities leveraging each company's strengths in workflow orchestration, rapid prototyping, and AI-driven operations.

---

## Context

Daniel Lopes met with Winton Welsh, founder of Dropsite, to compare product strategies. GrowthX is a B2B content marketing services company that built an in-house AI workflow engine after the cost of AirOps became prohibitive. The company is now building a content OS (replacing Notion/Airtable) to support its delivery operations across five areas: data vault, strategy, production, staging, and performance tracking. GrowthX deliberately chose a services-first approach—using internal tools to deliver results for clients—before attempting to productize.

Dropsite started with the opposite hypothesis: build a comprehensive, highly configurable tool first and sell it to enterprises. After private beta feedback, Winton pivoted to a more developer-friendly approach centered on AI Markdown, a markdown-based workflow definition syntax, and LLMFS, an open-source SQLite-based server for file system operations and code execution. Both founders discovered they'd solved overlapping problems (workflow orchestration, code execution, rapid iteration) independently, and now see opportunities to combine their learnings on product strategy and technical implementation.

---

## Relevance

**To GrowthX Delivery:**
- Dropsite's AI Markdown syntax and LLMFS architecture offer patterns for defining workflows declaratively, avoiding GrowthX's current reliance on imperative Temporal code
- LLMFS approach to sandboxed code execution (systemd-based containerization per user) is directly applicable to GrowthX's planned marketplace for human-in-the-loop workflow execution
- Winton's experience building rapid front-end iteration tools (using AI and cursor rules) aligns with GrowthX's need to reduce the learning curve for internal tools (AirTable, AirOps UI complexity)

**To GrowthX Business Development:**
- Winton expressed strong confidence in GrowthX's service-first strategy and identified it as the path Dropsite should have taken—potential reference customer conversation opportunity
- Winton is open to contributing to GrowthX's development efforts, suggesting high expansion potential or partnership discussion
- Both companies target the same operator/technical founder personas but in different verticals (content marketing vs. general workflow automation)

**To CheckThat:**
- Neither company discussed AI visibility, prompt optimization, or AEO explicitly, though Dropsite's work with prompt libraries and fine-tuned models suggests latent interest in content quality measurement
- Potential future collaboration on evaluating and auditing AI generations within workflows (GrowthX's content OS, Dropsite's Markdown workflows)

---

## Overview

- GrowthX.ai has developed a robust AI workflow engine and content tools, focusing on reusable components and cost-efficiency
- Dropsite's approach centered on building a comprehensive tool, which proved challenging to market
- Both companies recognize the value of selling services first before transitioning to product-based offerings
- Potential for collaboration exists, leveraging complementary strengths and learnings from both companies

---

## Key Topics

### GrowthX.ai's AI Workflow Engine

  - Migrated 30+ workflows from AirOps to in-house infrastructure
  - Built on top of Temporal and Rails with a thin layer for workflow generation
  - Utilizes code-based workflow definition with prompts, activities, and types
  - Plans to add evaluation layers, runtime improvements, and workflow creation interface

### Content Tools and Services

  - Developing a content OS to replace Notion and Airtable
  - Five areas: data vault, strategy, production, staging, and performance tracking
  - Services team uses tools to deliver results to clients, avoiding UX challenges
  - Exploring expansion into other spaces like recruiting

### Dropsite's Journey and Pivot

  - Initially focused on building a comprehensive workflow tool
  - Shifted to a collaborative writing space with editable workflows
  - Developed AI Markdown concept for defining workflows in a structured, shareable format
  - Created LLMFS, a SQLite-based server for file system representation and code execution

### Potential Collaboration Opportunities

  - Complementary strengths in workflow engine development and front-end/back-end rapid prototyping
  - Shared experiences in navigating product development and go-to-market strategies
  - Potential for leveraging Dropsite's learnings in GrowthX.ai's planned projects

---

## Action Items

- **Daniel Lopes (GrowthX):** Schedule a follow-up meeting to discuss specific collaboration possibilities
- **Daniel Lopes (GrowthX):** Show Winton the GrowthX team structure, project lanes, and identify which areas Winton could contribute to immediately
- **Both:** Explore how Dropsite's expertise and rapid prototyping patterns can accelerate GrowthX's core projects (content OS, marketplace, workflow visualization UI)
- **Winton Welsh (Dropsite):** Consider contributing to GrowthX development efforts on selected project lanes

---

## Transcript
**Winton Welsh:** You know that before I would see this like still hard to get something Are you looking like north or east or We like this we can I don't know what to know the area like haven't been here Yeah, I lived in San Francisco for 10 years.

**Winton Welsh:** We love it Well, okay, actually kind of in like the holding pattern with where we're living currently and thinking about coming back to the bay So oh nice.

**Winton Welsh:** Yeah.

**Daniel Lopes:** Oh, we caught you at me But we were you thinking about we went to check I see if like I really like the same thing about mountain biking that everything is there But go from not to huge fan.

**Daniel Lopes:** So we we saw the really nice house, but Then we also checked I'm very interested in thinking all that I just also lead to or move out it's like the commute is not too bad But yeah, it's so far.

**Daniel Lopes:** Yeah, one of your back move out is so creative expensive.

**Daniel Lopes:** It's just it doesn't make it I like I find something great.

**Daniel Lopes:** Otherwise, it's just seven key for like a house

**Daniel Lopes:** Yeah.

**Winton Welsh:** Yeah.

**Winton Welsh:** Now my my mom lived in Pacifica for a while.

**Winton Welsh:** And I I really like Pacifica a lot.

**Winton Welsh:** I mean, you have to like fog, but I love the fog and the ocean and that's the thing that she hates.

**Daniel Lopes:** Like she's like, oh, too cold.

**Daniel Lopes:** she's right.

**Daniel Lopes:** She's like, I'm scared.

**Daniel Lopes:** Don't escape the cold my whole life.

**Winton Welsh:** Yeah.

**Winton Welsh:** Yeah.

**Winton Welsh:** It's hard with San Francisco because, you know, you just get so far out that the commute just becomes crazy.

**Winton Welsh:** Yeah.

**Winton Welsh:** I was in downtown Oakland, like that's as far away I got for a while.

**Winton Welsh:** You know, at least it's on the BART.

**Winton Welsh:** But yeah, that has challenges.

**Daniel Lopes:** Most of the folks here are there in Oakland and I can date, but they are like up the month and really struggle with the commute.

**Daniel Lopes:** So we check the place as well on Saturday.

**Daniel Lopes:** It's just like, what's more the daughter's birthday on Saturday action?

**Daniel Lopes:** we went to check the place right next to you.

**Daniel Lopes:** It's like, I think it's Palo Alto or San Mateo, and it's just so far, like, yeah, yeah, yeah, the commute is pretty intense.

**Winton Welsh:** Maybe if you have like a full auto drive Tesla or something, but then you'd have to buy a Tesla in these times.

**Winton Welsh:** yeah, I think that's a good part of that.

**Daniel Lopes:** Anyway, like, I wanted to give you a quick overview of what we've built and what we want to do.

**Daniel Lopes:** And then if you could share more about what you've built, because I think there's overlap. I wanted to give you some context before we go deeper.

**Daniel Lopes:** We're having an important meeting tomorrow where we're presenting the strategy for the year and the team. It would be cool to mention to them that we're talking with you and exploring collaboration opportunities.

**Daniel Lopes:** The board is just me and the director, so it's not going to be a huge deal, but I want to give them a heads-up.

**Daniel Lopes:** And once you get here, I can show you more and we can talk about the higher-level vision if that makes sense.

**Daniel Lopes:** So on my side, when I joined, Marcel had created a bunch of workflows in AirOps and other tools. He had about 50 workflows that were doing different tasks, breaking down the process into well-defined components.

**Daniel Lopes:** He had workflows for research, search intent definition, assignment creation, outline generation, first draft, and polishing. He had this for each client, and with 10 clients, it meant a lot of duplication. When I joined, my goal was to avoid over-building because I've seen that mistake over and over—we build too much, it costs a lot, and we're late to market. This is even more obvious because we have the team internally using it all the time, and that creates problems.

**Daniel Lopes:** So I tried to take that system Marcel had and avoid duplication as much as possible.

**Daniel Lopes:** I started making the components more reusable so we didn't have to duplicate for every client. We'd have a spreadsheet—either Airtable or Coda or whatever we were using—that was shared across clients. The client-specific instance would reference the shared workflow, so maintenance happened once.

**Daniel Lopes:** This turned Marcel's workflows into a library of about 30 reusable workflows. Each one has 10 to 15 LLM calls with prompts and some calling between them.

**Daniel Lopes:** And then

**Daniel Lopes:** And the main challenge was that we're using this tool called AirOps and AirOps was costing us a lot of money.

**Daniel Lopes:** And some of the stuff that we had to run, for example, our assignment creation workflow takes a very long, essentially, it's a microact.

**Daniel Lopes:** There are plenty of steps, API calls, and integrations with Google and other services. It creates pages, merges them, and generates outputs that editors can review and add to.

**Daniel Lopes:** But this was costing us about $1.20 per week per assignment to run, taking several minutes. To run on 1,000 assignments—even during research phases to show clients what we're thinking—would cost $1,000 and take 24 hours.

**Daniel Lopes:** And AirOps wanted to charge us $1,000 a month for platform fees on top of that. That became the main blocker.

**Daniel Lopes:** So what we did was write a framework on top of Temporal and Rails to build a better system. I wrote a thin layer on top of Temporal with scaffolds that use LLMs to generate workflows from code—essentially we can write and create workflows much faster.

**Daniel Lopes:** We migrated all 30 workflows from AirOps to our own infrastructure, which was critical. It's now basically free to run.

**Daniel Lopes:** And then we build a UI on top of that. So we have this platform that hosts all our workflows and we make API calls from many places. The main one we use now is through AirOps, which makes calls to our backend and gets results.

**Daniel Lopes:** The workflows look like this. Here's a fact checker workflow that takes in an article or URL. If it's a URL, we fetch the content. If it's full text, we take it as-is, split it into chunks, and do parallel processing to extract facts. Then we use Perplexity Deep Research to find evidence for each fact and verify whether it's correct with confidence scoring.

**Daniel Lopes:** like a likert scale from minus 2 to plus 2, based on the confidence and then it puts to rewrite the sections that were confirmed both and combining general article.

**Daniel Lopes:** And then you can see here the input and output of every stack.

**Daniel Lopes:** And this is essentially for us on the technical side to see the execution and validate the workflow working.

**Daniel Lopes:** In this case, it extracted the passage, generates the check questions, then triggers multiple Perplexity calls and rewrites as needed. That's one example of our workflows. We have about 40-41 now.

**Daniel Lopes:** The workflows are defined in code. We tried visual editors with arrow graphs, but the graph gets insanely complex with chains, parallelization, loops, and conditionals. Maintenance became harder than just writing code. We never wanted to build a drag-and-drop UI because it's a trap—not good for advanced users, not usable for mainstream users either.

**Daniel Lopes:** With AirOps, it would take me an hour to write a simple workflow. With our framework and AI code generation, that same task now takes about five minutes.

**Daniel Lopes:** We define workflows in a structured format with four files: prompts for all the instructions, activities for the workflow nodes and conditions, and types for API input/output so the system understands what to expect. We're currently hacking Cursor with custom rules—a long project context and rules for each file type—that load whenever we need to generate something.

**Daniel Lopes:** When editing, you can add instructions from the sidebar. You barely write any code. This is the first step toward a code generation UX. It's much easier to generate code today than JSON or XML-based graphs like Make, Zapier, or AirOps produce. And it's more powerful—if AI can generate React apps, it can generate workflows, which are essentially orchestrated API calls.

**Daniel Lopes:** So we have plans for this year. We have the AI workflow engine framework, and we want to add a few more things. We want evaluation layers—everything is already getting traced, and we have the option to add evaluations. That's critical to execute on.

**Daniel Lopes:** We also have the runtime and we're building the UI I showed you. Ideally, that interface is where you create workflows—coding online, then sending changes back to the GitHub repo as pull requests.

**Daniel Lopes:** Like, I think it's a lot more vulnerable to that, and like, wrap up with that too, but I want to make that UI that I showed you, the place where you can create new workflows, visualize the graph of the workflows, and visualize, like, help you, did one a little bit, like, in that environment.

**Daniel Lopes:** Because they say that when we went down to code, we removed people like Marcel and Jason, like the last technical people out of the loop.

**Daniel Lopes:** So now it's our only program, I think, can code work for us.

**Daniel Lopes:** ideally we'll be like, bring it a little set above.

**Daniel Lopes:** But without trying to make it all drag and drop and all that.

**Daniel Lopes:** And I think that's also coming from the experience of having built drag and drop.

**Daniel Lopes:** All the same as before, for if, and knowing how much work goes into that and how limited you can go.

**Daniel Lopes:** So that's the session that I worked for, Angel, that we're building.

**Daniel Lopes:** And we're also building the content to us.

**Daniel Lopes:** The content OS will replace Notion and Airtable that we use today. It has five areas specific to content marketing. First is a data vault storing all client data—what they send us plus what we scrape from their websites. Second is strategy. Third is production, which is essentially a Cursor-like interface for content creation with a sidebar showing workflow steps, where you can interact with inputs and outputs in a conversational way. That's the main focus right now.

**Daniel Lopes:** Fourth is staging, where clients can come in, edit, add comments, and modify content. Today we do that with Notion and Google Docs, which is messy. Fifth is performance tracking—today we manually pull Google Search Console data weekly and generate Looker reports by hand.

**Daniel Lopes:** The content OS is a decent-sized project, and it works with the AI workflow engine.

**Daniel Lopes:** We also want a human-in-the-loop marketplace for different workflow tasks. We manage freelancers today, which is a huge efficiency problem.

**Daniel Lopes:** We're building a lot of micro apps on top of our workflows. Ideally, workflows become API endpoints—like an app store. Hugging Face has this for spaces, and Retool has similar components. Each workflow you build can be deployed so any company can use it in Coda, Airtable, or through the UI.

**Daniel Lopes:** Like the fact checker I showed you—we built a UI for it. You can pass a URL and get back a rewritten article with detailed analysis using the same workflow. The system shows the reasoning for the fact checks and a full rewrite at the end. Our team can review and interact with it.

**Daniel Lopes:** We're building micro apps on top and also have an SDK so companies can hire AI engineers or automation specialists to use our SDK in their infrastructure—creating workflows for Salesforce, Slack, and other tools.

**Daniel Lopes:** That's part of the big picture here. The micro apps and endpoints, plus the workflow engine for companies like Notion in other verticals.

**Daniel Lopes:** I hope that gives you an idea of the direction we're heading.

**Daniel Lopes:** We've been trying to dogfood and scale with the smallest team possible. The goal is: how much can we do with a small team and validate that? Then we fundraise and build the team to execute all the things that have been painful to do manually—like weekly performance reports or complex workflow configuration.

**Daniel Lopes:** So that's the state where we are.

**Daniel Lopes:** So now we have a bunch of lanes where I execute on each one of those things that I showed you.

**Daniel Lopes:** And that's why we're trying to find people like Brad.

**Daniel Lopes:** It's like, Brad, drew the marketplace so hard.

**Daniel Lopes:** He did a bunch of things almost by himself in like large complexity space.

**Daniel Lopes:** if I bear Brad.

**Daniel Lopes:** It's like somebody like the designers we have.

**Daniel Lopes:** Can we do a large part of the Condo S, for example?

**Daniel Lopes:** Or so that's the mindset.

**Daniel Lopes:** So we're going to have like maybe like six or seven small pods like that, and they will be executing on all the four lanes that I showed.

**Daniel Lopes:** One final lane we have as well that I didn't talk about is every change we are making, an intervention that our editors make, this is data that we are collecting.

**Daniel Lopes:** So we should essentially differentiate data that we can use and also like ways to improve, like fine-tuned models, they're amazing, like fine-tuned outline, like a fine-tuned version of GPT for all does great for like generating very specific things like an out of line or a draft or like the tone of the client, all of a sudden we could be dealing with the data that we are generating.

**Daniel Lopes:** We have a whole layer of like a learned layer that we have like a machinery engineer and property.

**Daniel Lopes:** We'll be getting data scientists making our pumps better, making our finding models, creating like a distilled models and things like that.

**Daniel Lopes:** Does that make sense?

**Daniel Lopes:** Yeah, no.

**Winton Welsh:** So I just want to recap where you're currently making money with these integrations through like motion and air ops.

**Winton Welsh:** And then you've kind of built, you took what were these kind of really expensive automations to run and built out kind of your own system for running these workflows on temporal and rails.

**Winton Welsh:** And those are still kind of like the UX for them is still running through notion and air ops.

**Winton Welsh:** Is that kind of how it works?

**Daniel Lopes:** Yeah, exactly.

**Daniel Lopes:** Exactly.

**Daniel Lopes:** But the main thing is that our clients, I don't think that the way we're thinking about things is that this space is moving too fast to put UI in front of the users.

**Winton Welsh:** And so

**Daniel Lopes:** So, our clients are eyeing our services team and the services team uses the tool.

**Daniel Lopes:** and a lot of the challenge that we have like a learning curve and like understanding how to where to click on those like air table, like we have just a super complex air table, grades that people have to open in a certain way to click and create the API call, same thing with air ops.

**Daniel Lopes:** Our services team presents results to clients, showing what's possible and what we can do quickly. Sometimes we create custom workflows instead of using the reusable ones. Services are our defense against the poor UX right now. And honestly, selling a $10,000 service is easier than selling a $10,000 tool unless the tool is perfect.

**Winton Welsh:** So, that's

**Daniel Lopes:** This is intentional. We want to do this across many verticals. We're starting with content marketing and have a pilot for recruiting. We're thinking about other areas where the same model applies—service-first, then reduce manual work over time. Right now we might need a team of five to operate for a client, but eventually that could be a team of one or two.

**Winton Welsh:** And then so I think we in the scenario that you outlined where it's like building the tool and like trying to do a really good job at that and knowing that that's like, you know, not the right path.

**Winton Welsh:** That's the path we went.

**Winton Welsh:** So like, you know, I think you you've brought a lot of expertise and you're like, you know, already having like built a company that like builds workflows and we didn't have that part.

**Winton Welsh:** So we were like, Oh, we're going to.

**Winton Welsh:** build this awesome tool, we just need to surface this operational process that we developed through code through this tool.

**Winton Welsh:** And I think part of our whole private beta rounds with everyone was learning that that wasn't the right path to go, which you guys had already kind of known from the beginning.

**Winton Welsh:** But yeah, I think kind of just a lot of the other stuff that you're talking about is very similar to thought processes we've had about everything.

**Winton Welsh:** I think you just went to market with real things faster than we did.

**Winton Welsh:** we were kind of like, we were doing the engineering thing where it's like, OK, all the problems we can solve, and then build the tool that can solve all of them, and work back and forth with these more enterprise clients to try to build something that they can eventually use and pay for.

**Winton Welsh:** That's a hard approach, and we learned it the hard way.

**Daniel Lopes:** So here's what I'm thinking. You've built so much that's applicable to our internal team first. We validate with them, then we bring clients in with platform access—they get the tools but don't have to build workflows yet. Maybe next year they can start creating their own, but we stay focused on the service team delivering results. Direct access to the output is what matters.

**Winton Welsh:** Yeah.

**Winton Welsh:** Yeah.

**Winton Welsh:** That's where we were before we decided to stop going down that road. I'll show you the road we took instead—a collaborative writing space. You start like a normal chat, but the chat itself becomes an editable workflow tool. We built this and iterated. It's like a communal space where you can see runs and popular workflows with an activity feed. We have a concept of defining variables within the chat. As you run through iterations and define variables, it prompts you for them, and you continue on.

**Winton Welsh:** You build the first version of a conversation you can replay. When you replay, it prompts for variables again. You can see the history of each version and how long they took, all the steps. Over time you build a library of workflows. Workflows can call each other—not just tools or APIs, but other conversations. Since they have variables as inputs, you can map variables across calls. We were working on if-then logic and iterating over results, running sub-conversations in parallel. But we bit off more than we could chew—this was our eighth iteration.

**Winton Welsh:** We started with a prompt library concept that we thought was amazing, but advisors pushed us toward enterprise, so we shifted tactics. I wish I could show you the interactions when we meet, but we archived it and changed strategy.

**Winton Welsh:** So we we um let's see I can pull up this spec.

**Winton Welsh:** We pivoted to AI Markdown—defining workflows in a single markdown file. You guys took an amazing approach that I wish we'd taken. You've found the sweet spot: something simple but complex enough to do the job, so people have to learn it. We're doing something similar with Markdown, hoping it becomes the internal way to define workflows. Your approach—team builds the workflows, sell the service, not the tool—is genius.

**Winton Welsh:** The concept uses tags with dedicated keywords, identifiers, and options. You define variables, mark where AI generates content, add custom instructions. Tags have options that get processed away in the final document but inform the generation. You can call external APIs (like GitHub REST) or other AI Markdown workflows, transforming variables and previous outputs. It's like running programs.

**Winton Welsh:** The foundation does file system operations, SQL, and code execution—which I think MCP is trying to do now. You can iterate over variables, AI generations, and call results, then generate new document sections. There are conditionals and includes. The output is valid markdown with all results, but also structured output. You can use it as a document or access it programmatically as structured data. The idea is that non-programmers can also manage these, though they need to learn the syntax. It's a bit programmer-y, but a really interesting approach.

**Daniel Lopes:** We've thought about that too. Did parsing and processing the markdown get complex?

**Winton Welsh:** Yeah, that's what we're working through now. I have a basic interface where you click on variables and edit metadata inline. It's still markdown-based, you generate and see results, and you can share the API calls or the document. That's what we're working on now. We have the code generation process down. The foundational piece—LLMFS—is actually on our GitHub. It's the open-core component of Dropsite, kind of our version of MCP.

**Winton Welsh:** LLMFS is a SQLite-based server that runs one per user. For on-prem, every user gets their own instance with access controls, sharing, and authentication. The core idea: SQLite represents the file system, and the user's process executes code written to that file system. You can execute SQL files on the database. It's a broad system for file operations, SQL, and code execution, all centered on the user.

**Winton Welsh:** For sandboxing, I'm kind of a Linux nerd. We built this to run on a single server with multiple LLMFS instances per user, all sandboxed using systemd and Linux-level tools. For on-prem deployments, users can trust each other, so we're not worried about malicious code attacks—mostly guarding against resource overuse.

**Winton Welsh:** If anything, it's more guarding against like, you know, CPU utilization and stuff like that.

**Winton Welsh:** Right.

**Winton Welsh:** We shifted from on-prem (each user running their own instance) to CloudFlare. I really like that ecosystem. I'm not sure what path you're taking on the cloud side, but CloudFlare is what we're planning for the AI Markdown editor launch. We also got into using Cursor rules to generate workflows—basically our own version called Cloudflow. It's separate from the Markdown concept. We're also building TypeScript workflow code we can deploy as workers. We're not sure how we'll use that beyond internal use, but the thinking is: some workflows might be too complex for AI Markdown. Try AI Markdown first, make it editable by users, then if we need something more complex, call a generated worker.

**Winton Welsh:** You're probably missing some stuff. What was your team structure when you started? Was it mostly you, or did you have a product person?

**Winton Welsh:** Primarily me as the engineer with help from engineer friends running ideas by me. AI has helped me build everything—10x to myself with AI. But it's so easy to go in many directions and get down a road without thinking it through, which is why you see all the sprawling concepts we tried. It was a crazy learning experience. We ran through user scenarios, built betas, and had people try them—tons of time and learning to see all the use cases. My co-founder is a product guy, a Figma wizard who helped me build Bleacher Report and Inverse. We've worked together over a decade. He helped me think about UX and MVP, but we still went off the rails and worked too long on things we shouldn't have.

**Winton Welsh:** That was a symptom of being isolated. We were just focused on "to make money, we need to build this." So we did. It was me, my co-founder, advisors, and friends. I wish we'd started with a specific problem instead of trying to solve everything. You guys did that right.

**Daniel Lopes:** I'm jealous of so many things you did that we thought about. All your learning is super powerful. Tomorrow I can show you the direction we're thinking, the different projects, and the lanes. I think you could pick whatever you want to work on, and you'd be super helpful with the core things we need to move fast on—because you've actually built similar things. Even if we don't use your codebase, the experience and everything you've learned is huge.

**Winton Welsh:** I'm super confident in my ability to build front-end and back-end fast and MVP concepts quickly. Our internal workflows around building the product itself are the most valuable things we have. I know how to build powerful front-ends we can iterate on quickly with AI. I'm definitely excited that you guys figured out all the things we couldn't. And now you have all the things we figured out. Together we can do something amazing.

**Daniel Lopes:** Something has to happen tomorrow and then we can talk more. Thanks for your time and sharing everything. Looking forward to having you back in the Bay.

**Winton Welsh:** It's been a while. It would be fun if we had more people around. My wife and I have talked about moving back a lot. All our friends are there. It's mostly just our families here. But yeah, it's definitely a possibility.

**Daniel Lopes:** Awesome. I'll let you go. Thanks for everything.

**Winton Welsh:** Thanks. Talk soon. Bye.
