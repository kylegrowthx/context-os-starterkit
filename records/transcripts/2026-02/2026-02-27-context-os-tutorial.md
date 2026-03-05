# Context OS Tutorial

<metadata>
date: 2026-02-27
time: 19:30 UTC
duration: 97 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Matthew Panzarino, Bridget McGillivray, Ella Dillon, Valentina Giraldo Morales, Kyle Gaudreau, Clint Shryock, George Haikal, Leo, Yousef, Stevie Kim
fireflies_id: 01KJ68DAMNBVQQB77W4PQHFDG1
transcript_url: https://app.fireflies.ai/view/01KJ68DAMNBVQQB77W4PQHFDG1
keywords: Context OS, AI agents, GitHub, Claude Cowork, MCP connectors, Skills marketplace, starter kit, onboarding
source: fireflies
enriched_on: 2026-03-03 15:00 UTC
</metadata>

---

## Summary

Marcel Santilli led a 97-minute internal tutorial walking the GrowthX team through Context OS — a centralized AI knowledge management system built on GitHub and Claude Code that he has been developing over several months, including processing 6,700 Fathom meeting transcripts in 48 hours. The team discussed personal context customization, AI skills sharing via a new handbook section, building custom MCP connectors, and a plugin marketplace. Key outcomes include aligning on a starter kit for new users, committing to centralize skills in the company handbook, and planning GitHub org access for non-developers.

---

## Context

This was an internal GrowthX tutorial session organized by Marcel Santilli to introduce the broader team to "Context OS" — his centralized AI knowledge management project. Marcel has been building this system for several months, structuring it as a GitHub repository with progressive context loading, automated enrichment pipelines, and reusable AI skills. The session was aimed at both technical and non-technical team members, with Matthew Panzarino (CTO) providing supporting commentary and encouragement throughout.

The timing coincides with GrowthX recently acquiring Claude enterprise plans, which unlock org-wide plugins and skills. Marcel had just completed a major milestone — backing up and processing 6,700 meeting transcripts from Fathom — and wanted to demonstrate the system's capabilities live while helping team members get started with their own setups.

---

## Relevance

**To GrowthX Operations & Productivity**
- Context OS provides a shared foundation for AI-assisted work across the company, reducing duplicated effort (e.g., multiple people processing the same transcripts)
- The starter kit and handbook lower the barrier for non-engineers like Ella Dillon and Bridget McGillivray to adopt AI tooling
- Automated context audits detected issues across 44,000 files in Marcel's project — this pattern can be applied to other company knowledge bases
- GitHub org access needs to be provisioned for all team members via the new productivity org

**To GrowthX AI Skills & Tooling**
- Three skills were shared during the session: Matthew's client snapshot skill, Kyle's Looker dashboard extraction skill, and Valentina's health scoring skill
- A new "AI Skills" section was created in the handbook to centralize skill documentation and downloads
- Clint Shryock proposed a marketplace/plugin infrastructure for automatic versioning and updates across Claude Code and Claude Desktop
- Claude enterprise plans now enable org-wide plugins and skills deployment

**To GrowthX Client Services**
- Matthew's client snapshot skill automates account status reports including stakeholder info, deliverables, performance history, and predictive health scoring using Looker data and semantic signals
- Valentina's health scoring skill integrates Marcel's prior documentation to enhance client risk assessments
- Combining these skills could produce automated weekly client reports

**To GrowthX Onboarding & Culture**
- The tutorial establishes a pattern for knowledge sharing sessions — Matthew suggested follow-up sessions with deeper dives
- Matthew emphasized that context quality matters far more than prompt engineering — "the age of being a prompt wizard came and went in 15 minutes"
- New team members can bootstrap their setup by asking AI what context it lacks, rather than building everything from scratch

---

## Decisions & Commitments

- **Skills will be centralized in the company handbook** — Marcel committed to creating an "AI Skills" section with documentation, downloadable files, and installation instructions for each skill
- **Matthew Panzarino will share his packaged skill files** with Marcel via Slack DM for integration into the handbook repository
- **Bridget McGillivray will coordinate GitHub access** with Yousef for all team members across both orgs (productivity and Marcel's repos)
- **Clint Shryock volunteered to set up the marketplace/plugin infrastructure** when the team is ready — this would enable automatic plugin updates and versioning
- **New GitHub productivity org created** — Bridget confirmed Yousef set up a new org that morning; needs to ensure everyone has access
- **Ella Dillon to set up GitHub account** and begin onboarding to Context OS projects
- **Marcel will continue processing the 6,700 Fathom transcripts** and work toward a shared repository of pre-processed transcripts to reduce redundant token usage

---

## Open Questions

- How should personal context files reference the handbook without duplicating content? Marcel suggested symlinks but was unsure if that was the best approach — needs input from technical team members.
- What is the right scoping model for context layers to prevent sensitive internal data from being exposed to wrong audiences? Matthew raised this but the group did not resolve it.
- Should the team standardize on Claude Code extension (in VS Code or Cursor) vs. native Cursor agents? Marcel recommended Claude Code for cost reasons but acknowledged Cursor's speed advantages.
- How will the shared transcript repository work at scale — who maintains it, and how do permissions work for client-sensitive data?
- What is the timeline for setting up Clint's marketplace plugin infrastructure, and does it depend on the enterprise plan configuration?

---

## Overview

- **Context OS Architecture:** Marcel demonstrated his centralized context project — a GitHub-based system with progressive context loading, automated enrichment, and tiered access rules that functions as a "brain" for AI-assisted work.
- **Transcript Processing at Scale:** Marcel processed 6,700 Fathom meeting transcripts in 48 hours using Claude Cowork, automatically creating and updating contact records, meeting records, and enriched summaries.
- **Automated Context Audits:** Live demo of auditing the 44,000-file project to detect broken references, stale content, and missing indexes — generating actionable update plans.
- **AI Skills Sharing:** Team members shared skills (client snapshot, Looker dashboard extraction, health scoring) and agreed to centralize them in a new "AI Skills" section of the company handbook.
- **Custom MCP Development:** Discussion of building MCPs for unsupported tools (Fathom, PhantomBuster, Ashby) and the challenges of connector reliability in Cursor vs. Claude.
- **Starter Kit & Onboarding:** Marcel demonstrated setting up a new Context OS project from the starter kit, connecting it to the handbook, and running a personalization plan for new users.

---

## Key Topics

## **Context OS Setup and Workflow**

The team focused on building a dynamic, self-updating contextual knowledge system to improve AI-driven project work and research.

- **Creation of a Context OS Project to Manage Dynamic Information**   
    - Marcel Santilli began by setting up a centralized project folder storing the latest context, avoiding outdated materials.  
    - He emphasized the challenge of keeping context current without manual updates, leading to a system with automated enrichment.  
    - The project structure includes folders with readmes and indexes to organize data for both humans and AI agents.  
    - This approach allows progressive context loading, rules for when and what to update, and tiered access to necessary information.  

- **Integration of AI Agents and Tools for Context Management**   
    - Marcel processed **6,700 meetings** from Fathom over 48 hours, enriching transcripts and batching AI analysis via Claude Cowork using local folder context.  
    - He demonstrated how the system automatically creates and updates contact and meeting records with contextual data extracted from transcripts.  
    - The system enriches contacts with personal details like locations and interests, enhancing AI understanding of relationships.  
    - Marcel showed how this pipeline supports live interactions and continuous updates, despite some brittleness and compute intensity.  

- **Technical Choices and Tools for Efficiency**   
    - Marcel recommended using either Cursor or VS Code with the Cloud Code extension, prioritizing Cloud Code for cost-efficiency and flexibility.  
    - Cursor offers speed and file context advantages but is more costly; Cloud Code is preferred for broader usage.  
    - The project uses markdown files (.cloudmd and .agentsmd) for context, with rules to keep Cursor and Cloud Code setups aligned.  
    - GitHub is used as the version control system for collaboration, history, and broad accessibility, especially for non-engineers.  

- **Process for Context Auditing and Updating**   
    - Marcel runs automated audits on context files to detect broken references, stale content, and missing indexes in a **44,000-file** project.  
    - These audits generate update plans that can be converted into skills and commands for ongoing maintenance.  
    - He demonstrated live updates pulling meeting transcripts using Fireflies MCP, highlighting some connector reliability issues but overall automated enrichment.  
    - This continuous cleaning and updating improve project accuracy and AI decision-making capabilities.  

## **AI Skills Development and Sharing**

The meeting explored building, combining, and sharing AI skills to automate reporting and analysis across teams.

- **Combining Quantitative and Qualitative Skills for Weekly Reporting**   
    - Valentina Giraldo Morales proposed combining skills from Kyle Gaudreau and Matthew Panzarino, integrating pipeline quality and health scoring for weekly summaries.  
    - Matthew explained his client snapshot skill automates account status reports including stakeholder info, deliverables, history, and predictive health scoring using Looker data and semantic signals.  
    - Valentina shared a health scoring skill that leverages Marcel's prior documentation to enhance client risk assessments.  
    - The team discussed the ease of sharing skills via Cowork and GitHub, with plans to centralize them in the company handbook repository.  

- **Centralizing AI Skills in the Company Handbook**   
    - Marcel proposed creating a dedicated "AI Skills" section in the handbook for documented skills with usage guides and downloadable files.  
    - This central library aims to reduce scattered file sharing and improve access for all team members.  
    - Skills can be installed into individual projects with clear instructions, fostering reuse and consistency.  
    - The handbook is maintained in GitHub, allowing version control and collaborative updates.  

- **Scoping and Context Control for AI Output**   
    - Matthew highlighted the importance of carefully scoping what AI outputs based on connected context layers to avoid exposing sensitive or irrelevant info to wrong audiences.  
    - Marcel emphasized compounding context quality over automation speed to improve skill building and reduce errors.  
    - The skills evolve through research, study guides, and continuous improvement cycles, enhancing both individual and company-wide knowledge assets.  

## **Personal Context OS Customization**

Each team member maintains a personalized context file set to tailor AI to their role, style, and responsibilities.

- **Building Individual Role-Based Context Files**   
    - Matthew described his personal setup reflecting his CTO role, communication style, and priorities, enabling AI to prioritize relevant information.  
    - He uses regular surveys and transcript reviews to update his rules and context dynamically, allowing continuous learning by the AI.  
    - Marcel and Matthew agreed that context is far more important than prompt engineering for accurate AI responses.  
    - This personalized context helps AI give actionable, relevant advice tailored to each user's function and style.  

- **Encouraging Self-Driven Context Development**   
    - Matthew advised users to ask AI what context it lacks for tasks, then provide that information to improve accuracy.  
    - Marcel shared that the system can audit projects and suggest cleanup or improvements, accelerating learning and avoiding repeated mistakes.  
    - The team stressed that the Context OS is a foundation to accelerate users' mental models, not a magic one-click fix.  
    - Users are encouraged to build their own tone, voice, and style references based on existing company context to speed adoption.  

## **Tool Integration and Connector Development**

The team discussed challenges and solutions for connecting company tools and systems to the AI workflow.

- **Building Custom MCPs for Missing Connectors**   
    - Marcel and Matthew showed how they built a custom MCP for Fathom to pull meeting transcripts due to lack of an official connector.  
    - Bridget expressed challenges connecting tools not supported out-of-the-box, such as Ashby, with plans to build or adopt community MCPs.  
    - Matthew suggested leveraging Claude code to debug and build MCPs, and recommended balancing time investment against task priority.  
    - Marcel encouraged resourcefulness in building personal integrations while cautioning against scaling custom solutions prematurely.  

- **Centralizing Transcript Storage and Processing**   
    - Marcel downloaded **6,700** Fathom transcripts as a backup and plans to centralize them for company-wide access and token savings.  
    - The goal is to avoid redundant processing by multiple users and create a shared repository of cleaned, enriched data.  
    - He highlighted ongoing work to create a customer database with health scores and notes without exposing personal data.  
    - This centralized data will power more reliable AI skills and reduce fragmented setups across the company.  

- **Marketplace and Plugin Management Plans**   
    - Clint Shryock introduced the idea of a Marketplace for plugins and workflows, enabling automatic updates and version control within Cloud Code or Claude desktop.  
    - Marcel confirmed recent cloud enterprise plans enable org-wide plugins and skills, which will improve scalability and shared tooling.  
    - Clint volunteered to set up the Marketplace infrastructure when the team is ready.  
    - This will standardize skills deployment and reduce manual update burdens across teams.  

## **Onboarding and Adoption Guidance**

The team shared practical advice and plans for getting new users started with the Context OS and AI tools.

- **Starter Kit and Demo Setup for Beginners**   
    - Marcel demonstrated how to create a new project folder, load the starter kit from GitHub, and open it in Cursor or VS Code with Cloud Code extension.  
    - He showed how to add multiple folders (e.g., handbook and context OS) to a workspace for parallel AI interactions.  
    - He recommended starting with a personalization plan by asking AI questions to tailor the context OS to individual needs.  
    - Marcel emphasized that much of the foundational context is already in the company handbook, reducing setup time.  

- **Guidance on Prompting and Context Usage**   
    - Marcel advised that well-organized context matters more than prompt complexity; he has largely stopped using prompt templates.  
    - Ella Dillon summarized that the company handbook should serve as the source of truth, with personal directories focused on individual style and preferences.  
    - Matthew encouraged new users to use AI tools to guide their onboarding by asking what context is missing and how to start.  
    - Marcel shared that AI can suggest step-by-step next actions when given meeting transcripts, accelerating adoption.  

- **Support and Follow-Up for Access and Permissions**   
    - Bridget flagged the need to ensure everyone has access to the new GitHub orgs and productivity repos.  
    - She also mentioned coordinating skills sharing within the productivity org and asked if any additional support from Yousef is needed.  
    - Marcel confirmed ongoing work on transcript processing and repo organization to support company-wide usage.  
    - The team agreed to have follow-up sessions to share advanced use cases and troubleshoot onboarding challenges.

---

## Action Items

**Marcel Santilli (GrowthX)**
- Continue improving and packaging AI skills into the shared handbook repository for easier company-wide access
- Collaborate with Clint Shryock to develop the skills/plugins marketplace leveraging the new Claude enterprise plans
- Prepare additional documentation for the skills catalog with consistent metadata and installation instructions
- Process and organize the 6,700 Fathom transcript backups into a shared repository

**Bridget McGillivray (GrowthX)**
- Set up GitHub access for all team members across both orgs (productivity and Marcel's repos); coordinate with Yousef on org membership and repository access
- Attempt building custom MCP connectors for tools like Ashby, with assistance from Marcel and Matthew if needed

**Matthew Panzarino (GrowthX)**
- Share packaged skill files (client snapshot, pipeline quality report) with Marcel via Slack DM for integration into company repositories

**Ella Dillon (GrowthX)**
- Set up GitHub account and begin onboarding to Context OS projects using the starter kit

**Leo and Yousef (GrowthX)**
- Facilitate onboarding of non-developers to the GitHub organization with appropriate access restrictions

**Clint Shryock (GrowthX)**
- Set up the marketplace/plugins infrastructure for automatic plugin updates and versioning across org projects when the team is ready

---

## Transcript

**Kyle Gaudreau:** Happy Friday.

**Marcel Santilli:** Hey, hey.

**Marcel Santilli:** Happy Friday.

**Bridget McGillivray:** Hey.

**Bridget McGillivray:** Happy Friday.

**Marcel Santilli:** Hello.

**Marcel Santilli:** What's up, everyone?

**Marcel Santilli:** Gosh, I have not been on this thing, and there's no way I'm going to have a voice at the end of this. There's zero chance. But give me a second. I've been back to back. I need to use the bathroom real quick and get some water.

**Marcel Santilli:** Cool.

**Marcel Santilli:** It's all right.

**Matthew Panzarino:** I wrote an agent for this, and it's going to take over from our cell while he's away.

**Kyle Gaudreau:** Is your orc gonna keep piping in just like yesterday?

**Matthew Panzarino:** Probably.

**Matthew Panzarino:** I'm working on something for Cindy right now, so the orc will probably chime in at some point.

**Kyle Gaudreau:** That was killing me.

**Marcel Santilli:** Work, work.

**Matthew Panzarino:** I attached orc sounds to my Claude code, so unfortunately, on calls, when I'm running Claude code agent operations, my agent keeps piping in with orc sounds in the background.

**Kyle Gaudreau:** Several times during call yesterday, just hearing random orc sounds.

**Marcel Santilli:** I'm not that kind of orc,

**Marcel Santilli:** basically, that.

**Kyle Gaudreau:** Dang, George.

**Kyle Gaudreau:** I just saw about the POC at Brecks.

**Marcel Santilli:** Curveball.

**George Haikal:** Constant curveballs, man.

**George Haikal:** But, yeah, we'll see.

**George Haikal:** I think it's all fine.

**Kyle Gaudreau:** Just.

**Marcel Santilli:** Yeah.

**Matthew Panzarino:** I mean, the good news is they're in a fight for their life right now, you know, and ramp is eating their lunch, so they need us in that.

**Matthew Panzarino:** Like, they can't take their foot off the gas.

**Matthew Panzarino:** It's just a matter of whether they decide to put that foot on the gas themselves.

**Matthew Panzarino:** You know what I mean?

**Matthew Panzarino:** Like, spin up their own operation.

**George Haikal:** But, yeah, I mean, they're getting a bunch of layers of compliance from Capital One, too.

**Marcel Santilli:** So we'll see.

**George Haikal:** We'll know more in.

**George Haikal:** In a few days.

**Clint Shryock:** Hey.

**Marcel Santilli:** All right.

**Marcel Santilli:** It's absolute fun.

**Marcel Santilli:** Everybody's ready?

**Marcel Santilli:** Let's do it.

**Marcel Santilli:** All right, cool.

**Marcel Santilli:** Let me clear out a bunch of my windows so I can share my whole desktop.

**Marcel Santilli:** All right,

**Ella Dillon:** Well, Marcel, I was like, I made the mistake in my head that we had a minute, and you weren't kidding. Like, you really do have to just go speak for another 90 minutes.

**Marcel Santilli:** No.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** So I want to start by giving everybody just, like, a high level of, like, what I set up. And before I do that, just give me two seconds. Let me push this out really quickly.

**Marcel Santilli:** All right. So what I set up. So one of the hardest things right now is that, like, when you go into a Claude chat, right, like, or any model or anything, I kept finding myself, like, setting up projects, and then those projects being having outdated context, right?

**Marcel Santilli:** And so if I go into — I'm in the wrong demo here. Give me a second. Back to my personal one.

**Marcel Santilli:** If I go into any of these projects, right, and there are certain, like, contacts that I would set and I would dump a bunch of contacts here. But then like, all these things start to get outdated, right? And like, for instance, like I set this up when we did a series A. And so I put the series A blog here and then all of a sudden it's like all the metrics in there are wrong, you know, and all these things are wrong. But now I don't have a way to have agents updating this, right?

**Marcel Santilli:** And then over time, as I started to kind of like play with this, it always felt like, okay, I can use AI for these things, but not those things, right? Or, hey, I need to go spend like two hours like getting all the best ingredients, curating the ingredients, like, you know, getting it all prepped, breaking them down to the sequence, putting them in little bowls, you know, they're ready to be used, writing out the recipe and then giving it to AI to do the work, right? And it's like, God damn it. Like, that feels like the hardest part.

**Marcel Santilli:** And so along the way, I started by coding like crazy, you know, using Lovable, V0. And then eventually made the scary jump for non-engineers, which was like setting up GitHub and, you know, pulling a project and building a prototype inside of a project, right? And that felt like, whoa, this is scary. And then about like a month later, it was like, okay, no, it's not that scary. It's like just there's just new terminology and new things, right?

**Marcel Santilli:** And so along the way as I was doing that, it became so clear how I would do that, right? Like, so I would open — and I'm going to walk through for those who are like newer or non-engineers, like kind of like the setup and everything, but I'm giving everybody else the full context, right?

**Marcel Santilli:** But every time I would do a prototype, I would, you know, like, pull a new project. So let's just say like, CheckThat, and I would, you know, pull up this project. And if I wanted to, like, prototype something, I would literally just create a new folder like this one called Context, you see, so that when I started to do prototypes it knew what context to pull related to CheckThat, right? So even though I was just building like UI inside the project of the actual product, I kept doing this. So then like over and over again, I'm like, okay, I'm having to go fetch the latest that I had from another thing.

**Marcel Santilli:** And then eventually I'm like, okay, I'm just going to create a project that's just context, right? So that I have one single folder in my computer that has the latest and greatest. And then for a while I was like, I'm just going to try to keep like our handbook updated, right? And then I could just pull from that, which is all of this. And then eventually was like, okay, this is also hard to keep updated because I'm having to pull these documents out of Notion into a markdown file in order to use in a project, right? So that's like how it all kind of compounded.

**Marcel Santilli:** And then like, so then what I wanted to start to do was saying like, hey, let me build a context project. That is kind of how I think, right? And that's what I started to build, which was like, this is how I was just working with AI, right? Like, I love doing deep research and I usually give it a lot of context. But then I started like, okay, let me go play with this.

**Marcel Santilli:** So then I started to do deep research to know how are people using Claude Code for knowledge work and what are the ways to set it up.

**Marcel Santilli:** So then I created a research guide on that.

**Marcel Santilli:** And then I was like, well, I don't want just a deep research.

**Marcel Santilli:** I want a deep research done this way, which is I want you to fetch a topic and then I want you to write your notes in a scratch pad.

**Marcel Santilli:** Then I want you to move it here and then think through it and then turn it into a study guide.

**Marcel Santilli:** And by the way, here's my how I like you to write, which how I like to consume information, right?

**Marcel Santilli:** Right.

**Marcel Santilli:** So I did that once.

**Marcel Santilli:** I was like, oh, this is awesome.

**Marcel Santilli:** Like, actually, why not just create a skill around it, right?

**Marcel Santilli:** So then I would, I would go into here for example, and, and say, hey, create.

**Marcel Santilli:** Create me the skill after I done it once, right?

**Marcel Santilli:** And then again like, I'm trying to give context.

**Marcel Santilli:** So then we'll jump in and I actually like, like show you how I was headed.

**Marcel Santilli:** I was doing that from beginning.

**Marcel Santilli:** So I was like, okay, cool.

**Marcel Santilli:** Like this, this works.

**Marcel Santilli:** And.

**Marcel Santilli:** And then I would use it.

**Marcel Santilli:** So now I'm like, this just works every time.

**Marcel Santilli:** And, and then like along the way, Claude Cowork showed up.

**Marcel Santilli:** And then Claude Cowork is even like amazing in this setup because now I can literally set up a project that is attached to my.

**Marcel Santilli:** To.

**Marcel Santilli:** To my folder, my Computer.

**Marcel Santilli:** Right.

**Marcel Santilli:** So let me just keep this one going.

**Marcel Santilli:** So.

**Marcel Santilli:** So then it becomes a lot easier for me to reference things.

**Marcel Santilli:** So I was just doing this one today.

**Marcel Santilli:** I essentially backed up 6,700 meetings from Fathom over the last 48 hours. And I built a script to pull all those and then I built another process to enrich those transcripts. And then I'm having Cowork batch through essentially a thousand of those, as you can see. And the only reason it's able to do that is because it's using my local folder to understand the full context. So I can use it the same way you would almost use a chat, but now I can do almost anything.

**Marcel Santilli:** So that's kind of like the big picture.

**Marcel Santilli:** I'm going to walk you through what my context like project looks like today and how it's set up.

**Marcel Santilli:** And then along the way we can actually hopefully take like specific things you

**Marcel Santilli:** all want to do.

**Marcel Santilli:** And I can even try to do a live, you know, and that will be fun to do.

**Marcel Santilli:** And then that's going to be a messy dump, a brain dump.

**Marcel Santilli:** So this is not yet a step by step, you know, replicate this.

**Marcel Santilli:** It's going to be a like, let's

**Marcel Santilli:** walk you through the whole, whole thing.

**Marcel Santilli:** Does that make sense so far for those that had no context on this meeting or, or like, kind of like everything.

**Marcel Santilli:** Any questions?

**Marcel Santilli:** Anything that would be helpful to clarify,

**Ella Dillon:** I was interested that you were in cursor.

**Ella Dillon:** Are you going to recommend, do we get to skip cursor?

**Ella Dillon:** Are you going to recommend that we're using that also?

**Marcel Santilli:** I'm thinking.

**Marcel Santilli:** So cursor is the fastest way to

**Marcel Santilli:** spend a lot of money,

**Marcel Santilli:** but it's also faster.

**Marcel Santilli:** So no, that's their way to spend a lot of money.

**Marcel Santilli:** And there is nothing you can do in there.

**Marcel Santilli:** There's very few things you need to do in cursor that you couldn't do a VS code.

**Marcel Santilli:** The there are however times when I use cursor for specific things because of like how it like looks at all your files and how it contextualizes that and how much faster it is, but you can achieve the same result.

**Marcel Santilli:** I'm just impatient and I'm running so many things in parallel.

**Matthew Panzarino:** So.

**Marcel Santilli:** But I think for today we can focus on setting up the project and like showing you, you all like how you can achieve both things within cursor or VS code.

**Marcel Santilli:** But I would ask everyone to lean into Claude Code extension.

**Marcel Santilli:** Whether it's in cursor, cursor it's like it is a fork of VS code, right?

**Marcel Santilli:** Like, so you can still use Cursor but like I would say use cursor but use the Claude Code extension, not the native cursor agents yet.

**Marcel Santilli:** You know, just because it's going to consume so much more,

**Marcel Santilli:** but it will

**Marcel Santilli:** achieve the same, the same things effectively.

**Kyle Gaudreau:** And hypothetically, like also this is maybe the nuance I'm not appreciating, but like you can also do this natively and even code like now they have code as a separate tab next to cowork and now you could do it in the terminal.

**Kyle Gaudreau:** You know, there's, there's just multiple ways of skinning this.

**Kyle Gaudreau:** Essentially what I don't, I guess I don't appreciate is like what does like a VS code unlock a bit more than what I mean doing in the terminal Claude Code.

**Kyle Gaudreau:** But that may be beyond scope of today.

**Marcel Santilli:** But that's where my cur.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** Okay.

**Matthew Panzarino:** So,

**Marcel Santilli:** so I have a few ideas we'll, we'll try to go through to

**Marcel Santilli:** show like what I'm, what I'm talking about.

**Marcel Santilli:** But I think setting up cursor, even, I think the free version or the

**Marcel Santilli:** $20 a month version and then installing the, the Claude Code extension will, will be, will be enough.

**Marcel Santilli:** But the most important thing is the principles way more than the tools.

**Marcel Santilli:** So okay, how I set up the project.

**Marcel Santilli:** So think of this project like my brain and how my brain works.

**Marcel Santilli:** So it was very progressive how I got to this point.

**Marcel Santilli:** And, and so the, the first thing to know here is there's slightly different ways that Claude code works and cursor works in, you know, so like Claude Code uses CLAUDE.md and then like Cursor might use something like AGENTS.md.

**Marcel Santilli:** Claude Code has a dot skills, cursor has a dot cursor.

**Marcel Santilli:** And so there's like a bunch of things that I've done to create rules to keep them close to 101, you know.

**Marcel Santilli:** So put that aside for a second.

**Marcel Santilli:** So the first thing here is this is when it comes to repo, this is the readme.

**Marcel Santilli:** This just is a very human readable

**Marcel Santilli:** explanation of like this project.

**Marcel Santilli:** Right.

**Marcel Santilli:** And, and so the way this project works right now, there's these different directories and the CLAUDE.md is the thing that's going to load 100% of

**Marcel Santilli:** the time when you're using Claude Code

**Marcel Santilli:** and the agents MD is like what's

**Marcel Santilli:** going to load every single time.

**Marcel Santilli:** So, so think of it as if you took this and literally like assume a, you know, cloud chat was plugged into your local machine and only had access to this one directory here, right here.

**Marcel Santilli:** And, and that the first prompt in your chat, the beginning of the prompt

**Marcel Santilli:** started with this copied and pasted over.

**Marcel Santilli:** Right.

**Marcel Santilli:** So just, just like that.

**Marcel Santilli:** That's kind of like the thing to know, right?

**Marcel Santilli:** With that it means you don't want to like flood the crap out of it.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like because agents just like humans were like kind of like a little bit like shaped in that we pay a lot of attention to the beginning, we kind of lose track of things in the middle and then we pay a little bit more attention at the end.

**Marcel Santilli:** Right.

**Ella Dillon:** Like so yeah, Ellis, I'll be the, I'll be the, the pansy that asks super basic questions.

**Ella Dillon:** Why are you in GitHub right now?

**Ella Dillon:** Like why do you have all this built in GitHub versus somewhere else and AK?

**Ella Dillon:** Should we be doing the same thing?

**Marcel Santilli:** Yes, absolutely.

**Marcel Santilli:** So think of GitHub as — it's just a little bit easier for me to show you this than it is for me to like show you the folder on my computer. This is simply a way to store, like, commit the version of your file on your computer to somewhere that's accessible in a lot of different ways, but that also has an insane amount of like version history insights, collaboration. Like I shared this one with Daniel. Daniel was able to use it. You know, there's an entire ecosystem of millions of developers using this as a version control. All this is, is like cloud version control for your files. That's at the end of the day.

**Marcel Santilli:** Yeah.

**Ella Dillon:** Again like super practically I have my little free GitHub thing I set up in advance.

**Ella Dillon:** I should get invited into the company, like the company thing.

**Ella Dillon:** So I like I'm.

**Ella Dillon:** And maybe I'm getting like super tactical but I like, I'm literally want to like leave with my how do I start setting all this up so I can do it thing.

**Ella Dillon:** But should I pause?

**Ella Dillon:** Are you still context building and I should just pause for a moment?

**Marcel Santilli:** No, this is good. I think the recommendation for everyone is like if you haven't set up GitHub, sign up for GitHub. I think other people that are smarter than me, they're developers and maybe Leo can even help as a follow up on this. Like just the non-technical people setting up GitHub, working with Yousef as well. If they run into any access issues, we are creating another organization in GitHub that's gonna be for the non-developers. So that we're not giving every single person in the company access to like do a pull request on one of our products, you know, that they don't need to do right now.

**Marcel Santilli:** But for all intents and purposes, there is a starter kit that I created that we'll go through right now and show you how to set it up. What I'm not going to do is show you how to install Cursor or how to sign up for GitHub essentially, right now.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Walk through the structure.

**Marcel Santilli:** I created a starter kit that hopefully is decent, but I actually haven't spent a lot of time, I'm like, like trying to set up from scratch again.

**Marcel Santilli:** So the overall structure, ignore these two files, they just accidentally slipped in there right now.

**Marcel Santilli:** But so we have the instructions on the agents.

**Marcel Santilli:** Every single directory has a readme which is something like this as well as an index.

**Marcel Santilli:** So the index is mostly for humans to be able to like, like open this and go, oh, okay.

**Marcel Santilli:** These are the files that are inside this folder, but in a way that also has like very short one sentence descriptions in case either a human or

**Marcel Santilli:** an agent needs to use it, you know.

**Marcel Santilli:** And so like this is the, in

**Marcel Santilli:** the like global index, roughly you know, of all the folders.

**Marcel Santilli:** So you can see it's just like very, very simple.

**Marcel Santilli:** It's just like that's all it is.

**Marcel Santilli:** And then there's like rules to start

**Marcel Santilli:** to update all the stuff all the time, right?

**Marcel Santilli:** So then the way I set it up now I have my context and the context are the things that you're going to use almost all the time.

**Marcel Santilli:** There is a context routing which my global rules or context, essentially the cloud MD tells it to look at.

**Marcel Santilli:** And so it's like tiered context loading.

**Marcel Santilli:** Again, I didn't write any of this.

**Marcel Santilli:** This is all me doing deep research on how to set this up and then like continuously improving it and making

**Marcel Santilli:** it better and better over time, right?

**Marcel Santilli:** So it's like test trigger on demand search only it has like a whole map on like what to like trigger and when.

**Marcel Santilli:** And it starts to gain a deeper and deeper understanding of all the folders and what to use and how to use it, right?

**Marcel Santilli:** Like, and as it's updating I can always like improve it, right?

**Marcel Santilli:** So I could like jump in here for example, and say study the.

**Marcel Santilli:** Let's study the whole project that I have here and every directory and then look at my context loading rules and recommend a plan if there's anything I need to improve or update.

**Marcel Santilli:** So like I Can do things like this to where, I don't know, it's

**Marcel Santilli:** taking longer just because I'm, you know, live demos, things just like, oh, there you go.

**Marcel Santilli:** Okay, so.

**Marcel Santilli:** And right now I have two projects running in parallel.

**Marcel Santilli:** I have the handbook in this.

**Marcel Santilli:** So we're talking only about this.

**Marcel Santilli:** So ignore the handbook for, for a second.

**Marcel Santilli:** And.

**Marcel Santilli:** And then you can always like, reference,

**Marcel Santilli:** like, I think it was like context routing.

**Marcel Santilli:** Yeah, there you go.

**Marcel Santilli:** So you can always like at mention a certain file when you're doing this.

**Marcel Santilli:** So context loading rules.

**Marcel Santilli:** So I'm going to just say context routing

**Marcel Santilli:** and then you can change the.

**Marcel Santilli:** To plan mode.

**Marcel Santilli:** And so you have like essentially like

**Marcel Santilli:** ask agent, plan, debug, you know, so

**Marcel Santilli:** plan mode is when it's like, that's the place to get started on everything.

**Marcel Santilli:** Like, don't just tell it to do something unless it's a very straightforward thing.

**Marcel Santilli:** Ask it to come up with a plan.

**Marcel Santilli:** Right.

**Marcel Santilli:** So I'm let this run.

**Marcel Santilli:** We're going to come back here in

**Marcel Santilli:** a second while I keep explaining the whole thing.

**Marcel Santilli:** Then like, one of the first things I did was set up my.

**Marcel Santilli:** My voice and.

**Marcel Santilli:** And then for the.

**Marcel Santilli:** The voice, like one of the things I did as I was doing this, I was like, well, I'm going to have multiple versions.

**Marcel Santilli:** Right.

**Marcel Santilli:** So, so then the.

**Marcel Santilli:** The next thing I did, and I

**Marcel Santilli:** don't know why it's being so slow.

**Marcel Santilli:** I'm just going to show you here.

**Marcel Santilli:** Okay, so records context.

**Marcel Santilli:** Okay, so I set up my voice and in the.

**Marcel Santilli:** What the hell is happening right now?

**Marcel Santilli:** Is that my Internet?

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** All right, There you go.

**Marcel Santilli:** Okay, so as you can see, as I click through, everything that shows here is like the readme.

**Marcel Santilli:** So every folder has a readme and an index.

**Marcel Santilli:** Like I said, this one is the, like the style guide of how I like to write or like how I want to read things.

**Marcel Santilli:** And this was highly informed by me doing a ton of deep research on people as well.

**Marcel Santilli:** Right.

**Marcel Santilli:** And which.

**Marcel Santilli:** I'll explain that in a second.

**Marcel Santilli:** Um, so this was one of the first things I did because I wanted everything I do to be written in the way I want it to be written anyways.

**Marcel Santilli:** And so that was like one of the first things.

**Marcel Santilli:** And this has a lot of, like, how I like to think, how I like to consume information.

**Marcel Santilli:** I'm like, hey, use this framework.

**Marcel Santilli:** You know, don't marry the lead.

**Marcel Santilli:** Like, these are just like very informed

**Marcel Santilli:** by what I liked, you know.

**Marcel Santilli:** And so.

**Marcel Santilli:** And then in order to do this, I literally did a deep research process

**Marcel Santilli:** in order to do this.

**Marcel Santilli:** So then as I was doing that I said, hey, can you do a deep research on like how to set up clock code?

**Marcel Santilli:** Okay.

**Marcel Santilli:** And, and so, so then, so then I did a, so give me a second here, a study guide on how to do that.

**Marcel Santilli:** And then as I did a first study guide, I, I go, okay, now that you did this, like turn this into a rule.

**Marcel Santilli:** So that's what I'm going to start to show you now is like how things start to compound over time once you have a good, good structure.

**Marcel Santilli:** Right.

**Marcel Santilli:** So going back to the top.

**Marcel Santilli:** So context, voice, it's like anything that's kind of like how, how I write, how I think, who, who I am, right.

**Marcel Santilli:** Knowledge.

**Marcel Santilli:** It's like study guides and learning material for myself and broken down into like topics.

**Marcel Santilli:** As it started to get bigger pipeline is like the work that's happening.

**Marcel Santilli:** It's like scratch pad research, raw research with not being processed all the way to outputs.

**Marcel Santilli:** And then hopefully from outputs it gets moved into knowledge or something else.

**Marcel Santilli:** Right.

**Marcel Santilli:** So it's just kind of like a data pipeline, if you will.

**Marcel Santilli:** And then records this.

**Marcel Santilli:** Readme is not updated.

**Marcel Santilli:** The customers transcripts, downloads, there's a bunch of other things.

**Marcel Santilli:** And then scripts are like every now and then you don't want an LLM to do something like actually writing a quick script in code does it way faster.

**Marcel Santilli:** Like, hey, I want you to like take these three files and convert it into this format.

**Marcel Santilli:** Like, you know, you don't want to

**Marcel Santilli:** use like millions of tokens to do that.

**Marcel Santilli:** Like you can just say write a script to do this and then like try it on one.

**Marcel Santilli:** Did it work?

**Marcel Santilli:** It didn't.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** Turn it into a skill that uses

**Marcel Santilli:** the script and then that's it.

**Marcel Santilli:** And then sources was really along the way.

**Marcel Santilli:** I asked it to start to create like a library of the kinds of

**Marcel Santilli:** people and sources I like, you know.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Of course, like this is just because

**Marcel Santilli:** I'm on a live demo.

**Marcel Santilli:** Like these things are happening that have never happened before.

**Marcel Santilli:** Like GitHub, like give me a 404 or you know, like these things just like nah.

**Marcel Santilli:** So, so give it, give it a second to see if this, this is loading or not.

**Marcel Santilli:** If not, like, but let me pause here.

**Marcel Santilli:** Does that make sense so far?

**Marcel Santilli:** I know it's like a lot of

**Marcel Santilli:** context building for leading up to then like digging in.

**Marcel Santilli:** All right, questions.

**Bridget McGillivray:** I mean maybe you're going to go into it, but just like, you know, this has taken you a few months, so how can we.

**Bridget McGillivray:** Same question as Ella, but Just like if we're starting in Cowork, for example, I don't know, using one of your folders, for example, like, where do you want to.

**Bridget McGillivray:** Where would we start?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Okay, so I'm just going to give

**Marcel Santilli:** you one example here because I noticed

**Marcel Santilli:** like the readme was outdated, right?

**Marcel Santilli:** And this thing is like not doing it.

**Marcel Santilli:** So.

**Marcel Santilli:** And.

**Marcel Santilli:** So.

**Marcel Santilli:** So it's an example of.

**Marcel Santilli:** Just to show you now, so I use Cowork and I selected the folder GrowthX, like the context folder that I have.

**Marcel Santilli:** And you can see here, the first thing it pulled was CLAUDE.md. The second thing it pulled was what I referenced here, which is like the context routing.

**Marcel Santilli:** Right?

**Marcel Santilli:** And then, then it started pulling the index here and.

**Marcel Santilli:** And then it's going to start putting things into a scratch pad, right?

**Marcel Santilli:** And doing.

**Marcel Santilli:** These are all rules that were set, right?

**Marcel Santilli:** And.

**Marcel Santilli:** And Bridget, to your point, like, I created a starter kit that has some of the scaffolding already done there.

**Marcel Santilli:** But the reason it's so good at this, like, this prompt was like, nothing, right?

**Marcel Santilli:** Like, this is nothing.

**Marcel Santilli:** This is literally like one sentence.

**Marcel Santilli:** And like, this is crazy that it's

**Marcel Santilli:** doing all this already, right?

**Marcel Santilli:** Like that it knows all this knowledge and as it's going, look how many more files it's pulling.

**Marcel Santilli:** See how it's pulling all the readmes and indexes for all the files now so it has an easier time.

**Marcel Santilli:** Like it's, it's doing all of these things because now it has access to it and all the folders.

**Marcel Santilli:** You, you just left all the breadcrumbs everywhere and you organize it all in the right ways.

**Marcel Santilli:** So then when you give it like a one thing, it like, knows how to like, make sense of it within the whole context, right?

**Marcel Santilli:** And the beauty of it is like you're in Cowork, so it's using all this context automatically, right?

**Marcel Santilli:** And, and the other thing is like, there's a ton of connectors now in coworkers in Cloud overall.

**Marcel Santilli:** So that will allow you to do a lot of different things, right?

**Marcel Santilli:** That we can do it live.

**Marcel Santilli:** So this one I'll let.

**Marcel Santilli:** Let it run.

**Marcel Santilli:** But maybe like a good way to kind of show you all, like, what unlocks here is to give an example of something that like, right now, like, would have taken like a long time

**Marcel Santilli:** even, you know, is there anything you want to use?

**Kyle Gaudreau:** Before you jump into that, just one quick question.

**Kyle Gaudreau:** I may have missed it, but what it would like or misread it, but what it was seeming to feed into the scratch pad was like the agents view Which I think was built for like cursor.

**Kyle Gaudreau:** Like if I was to think about that and make sure I'm like using context window, like efficiently.

**Kyle Gaudreau:** Yeah, the Agents md, would I tackle that via like a rule like, that's specific almost to like the tool set or something to that matter?

**Marcel Santilli:** No.

**Marcel Santilli:** So Scratchpad was just like me doing a deep research and saying like, hey, one of the most important things is progressive disclosures and for, for agents on.

**Marcel Santilli:** Let me quit this and restart because

**Marcel Santilli:** there's something else here.

**Marcel Santilli:** And, and then because of that, one of the things is like, when you're processing like really long files or a lot of things, think of it as like, imagine you're scraping a thousand sources, right, to do something agents are going to forget.

**Marcel Santilli:** Like that that doesn't fit.

**Marcel Santilli:** So then the scratch pad is just a strategy that I said at the beginning saying, hey, anytime you're doing things, use a scratch pad to take notes of what you're learning along the way.

**Marcel Santilli:** And don't try to reason through it.

**Marcel Santilli:** And then from there think about like, and then dump all this information in a raw file and then take those two things and then reason through what

**Marcel Santilli:** you want to do about it.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like, so, so it's kind of like trying to give that as, as kind

**Marcel Santilli:** of like a, an overall like, instruction, you know?

**Kyle Gaudreau:** Yeah, I think I was just misinterpreting because it seemed like the Agents MD was built for cursors purposes, but then, then Claude was coworkers.

**Marcel Santilli:** They're the same, those two piles.

**Marcel Santilli:** Exactly.

**Marcel Santilli:** And Claude, it's, it's exactly the same file.

**Marcel Santilli:** It's just that, like, I just set

**Marcel Santilli:** up some rules to keep both, like.

**Marcel Santilli:** Yeah, yeah, got it.

**Marcel Santilli:** Yeah.

**Kyle Gaudreau:** I'm just trying to like, think about like how efficient context window management basically.

**Kyle Gaudreau:** But yeah, that makes sense what you're saying, I think.

**Marcel Santilli:** Yeah, it's mostly like download everything.

**Marcel Santilli:** You're just giving like these commands to

**Marcel Santilli:** just say like, don't do this.

**Marcel Santilli:** Just like start like, you know, like, let's go update it.

**Marcel Santilli:** And that's like what I'm doing right now.

**Marcel Santilli:** It's like it's going through and doing

**Marcel Santilli:** all of this and there you go.

**Marcel Santilli:** Okay, so here's the context audit, you know, and then if I open this, it put it into my Scratchpad folder here, you see?

**Marcel Santilli:** And this is what it recommended.

**Marcel Santilli:** Like, the project now contains 44,000 files.

**Marcel Santilli:** Holy shit.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Oops.

**Marcel Santilli:** And top 10 directories.

**Marcel Santilli:** Catching up the docs of reality.

**Marcel Santilli:** Priority number of broken references.

**Marcel Santilli:** Priority number two missing directories and documentation.

**Marcel Santilli:** Okay.

**Marcel Santilli:** And Stale counts, minor inaccuracies, missing index.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Burn over four Context routing improvements.

**Marcel Santilli:** Gray.

**Marcel Santilli:** No tasks for blah, blah, blah.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Okay.

**Marcel Santilli:** All right.

**Marcel Santilli:** Everything looks reasonable.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** I just asked it to execute those now.

**Marcel Santilli:** So.

**Marcel Santilli:** So now, like, so I do this all the time.

**Marcel Santilli:** And if it's something that's happening, like, all the time like this, what I might do is if I feel confident enough, I might set this into a skill and then a rule or a command that says do this thing that then pulls that skill and do the

**Marcel Santilli:** redoes this process that I just did.

**Marcel Santilli:** You know, does that make sense?

**Marcel Santilli:** Like, because clearly, like, these are things that should have been already happening, like, and they weren't being updated as the project was evolving, right?

**Marcel Santilli:** And so it just makes it a

**Marcel Santilli:** lot easier to do that.

**Marcel Santilli:** Right?

**Marcel Santilli:** So, like, let me give another example and I'll show some of these in cursor.

**Marcel Santilli:** Assuming cursor fucking works to.

**Marcel Santilli:** To just show you it, like, because cursor shows you some of the process a little bit more visible as well sometimes.

**Marcel Santilli:** So let's just say, like, pull meeting each review meeting today.

**Marcel Santilli:** So this is a command.

**Marcel Santilli:** And so what it's doing, it's like pinging Fireflies MCP again, assuming it works,

**Marcel Santilli:** I guess it's connected all the time.

**Marcel Santilli:** A lot of the stuff, like, doesn't work 100% of the time.

**Marcel Santilli:** And like, see, like, this is a great example here.

**Marcel Santilli:** Like, okay, so what I'm going to do instead of.

**Marcel Santilli:** By the way, this is another thing.

**Marcel Santilli:** One of the annoying things, one of

**Marcel Santilli:** the things that cursor is good.

**Marcel Santilli:** I mean, Claude is good at and cursor sucks is like, MCPS don't work

**Marcel Santilli:** like 90% of the time.

**Marcel Santilli:** It's like, you see, it's connected.

**Marcel Santilli:** It's like, God damn it, it's connected.

**Marcel Santilli:** Like, try again.

**Marcel Santilli:** Like, sometimes you have to keep trying.

**Marcel Santilli:** And like, that part is really annoying.

**Marcel Santilli:** Whereas, see, okay, now it worked.

**Marcel Santilli:** It looks like it worked.

**Marcel Santilli:** Whereas any connector in Claude, like, works way, way, way more.

**Marcel Santilli:** More reliably.

**Marcel Santilli:** So,

**Marcel Santilli:** All right, so let me pull the meeting here in another session.

**Marcel Santilli:** So that's just to show you really quickly.

**Marcel Santilli:** All right, so this is running.

**Marcel Santilli:** I can start a new one.

**Marcel Santilli:** GrowthX Context Use Meeting Skill command.

**Marcel Santilli:** Full meeting on GTM View today.

**Marcel Santilli:** Should I firefly set up for this?

**Marcel Santilli:** Let's try and get us.

**Marcel Santilli:** And while that's running.

**Marcel Santilli:** All right, so now you can see it's like updating the root index and

**Marcel Santilli:** doing a bunch of other things.

**Marcel Santilli:** And all of this now is like

**Marcel Santilli:** cleaning up your entire project.

**Marcel Santilli:** For you.

**Marcel Santilli:** Right.

**Marcel Santilli:** Okay, let's keep going.

**Marcel Santilli:** Okay.

**Marcel Santilli:** I think it worked.

**Marcel Santilli:** Sweet.

**Marcel Santilli:** It worked awesome.

**Marcel Santilli:** Okay, perfect.

**Marcel Santilli:** So is this the meeting or not?

**Marcel Santilli:** So I have it essentially like confirmed that this is the meeting.

**Marcel Santilli:** As part of my rule, I'm going to say yes.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So what it did here, while this is running it like search fireflies through their mcp.

**Marcel Santilli:** And you can see, like, sometimes it doesn't work.

**Marcel Santilli:** So you have to, like, ask it to do it again, make sure the MCP is working and it's not like there's more reliable ways to do this at scale.

**Marcel Santilli:** But now it knows, like, to pull it and it knows to present the information this way to me and then I'm going to confirm.

**Marcel Santilli:** And then along the way, it started with just, just pull the transcript.

**Marcel Santilli:** And then I pull the transcript.

**Marcel Santilli:** And I was like, and then the LM's trying to rewrite the transcript and it was wasting so many tokens.

**Marcel Santilli:** So then I wrote a script that just said, like, copy and paste the stuff over and then run an enrichment process and then go update the meeting records and the contact records and the

**Marcel Santilli:** index and then report back the summary.

**Marcel Santilli:** Like, so I had to like, literally,

**Marcel Santilli:** like, build this process for me.

**Marcel Santilli:** Right?

**Marcel Santilli:** So now you can see it's running these scripts, is doing a bunch of stuff, and then when it's done running, it's all going to go into the records, transcripts.

**Marcel Santilli:** And then because it started getting kind of wild, I started essentially like having it do it, like using this naming convention.

**Marcel Santilli:** Right?

**Marcel Santilli:** And so these are all little patterns that like I converted into the starter kit.

**Marcel Santilli:** But along the way it's kind of like how you start to organize this, it starts to get crazy and it's like kind of trying to organize your.

**Marcel Santilli:** Your brain.

**Marcel Santilli:** Right.

**Marcel Santilli:** As well.

**Marcel Santilli:** And so, so now, like, if I look here in these, like, meetings that it's pulling.

**Marcel Santilli:** So let's just say this one with cc, right?

**Marcel Santilli:** This is kind of good.

**Marcel Santilli:** Okay, so I can start another agent here and say like this meeting with

**Marcel Santilli:** cc, it's like,

**Marcel Santilli:** summarize the action items here.

**Marcel Santilli:** Actually, I'm going to do a couple other things.

**Marcel Santilli:** Make sure there's a contact record for cc.

**Marcel Santilli:** If there isn't one, create one if there is one, updated with the context of this meeting.

**Marcel Santilli:** And also make sure the meeting record for this is there and that it's updated with the context of this meeting.

**Marcel Santilli:** Then give me all the action items so that in a format that I

**Marcel Santilli:** can post it to Slack in a message.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** So, so now you can kind of see like you, I started to create these things that start to get enriched

**Marcel Santilli:** more and more, right?

**Marcel Santilli:** Like, so as first I just had transcripts and I was like, okay, that's not enough.

**Marcel Santilli:** So then I started to create contacts, right?

**Marcel Santilli:** So now everybody has a contact file that gets automatically created anytime a transcript gets pulled or anytime a meeting record gets pulled.

**Marcel Santilli:** Then I connected this to my calendar.

**Marcel Santilli:** So now it's pulling every single meeting I ever had essentially for the last two years.

**Marcel Santilli:** And, and then now it's like updating essentially like a fact sheet on this person, you know, so it's like it's super powerful, right?

**Marcel Santilli:** Because now you're like, whoa, like this is insane.

**Marcel Santilli:** But like now like it's going to update all these things on this person and from every meeting it's going to automatically enrich my things I should remember

**Marcel Santilli:** about this person, right?

**Marcel Santilli:** So let me use Brian because Brian

**Marcel Santilli:** was a good one recently.

**Marcel Santilli:** So Brian is a prospect and we have a deal with them right now.

**Marcel Santilli:** But he lives in my neighborhood.

**Marcel Santilli:** Like so you can see here like there's all these things, right?

**Marcel Santilli:** Location, the wife, the kids, where they go to school.

**Marcel Santilli:** These are all things you mentioned on a call.

**Marcel Santilli:** You know, the interest where you're span and like the career, the background and, and then even like a timeline, right?

**Marcel Santilli:** And then extracted all these things based on things that either fed it or, or things from, from the transcripts, right?

**Marcel Santilli:** And then it started like link to

**Marcel Santilli:** other related records here, meetings and transcripts as well that are related.

**Marcel Santilli:** So now like an agent, like can understand these things better.

**Marcel Santilli:** So then I'm like, oh, okay, so there you go.

**Marcel Santilli:** And, but now like you almost have like this holding area for this, right?

**Marcel Santilli:** That will allow you to like enrich this further.

**Marcel Santilli:** You know, I'm going to try something

**Marcel Santilli:** I never done before.

**Marcel Santilli:** Look at my DMS with CC and Slack and pull the records and my conversations there, write those records into the Slack directory in records and then update

**Marcel Santilli:** her contact file based on that as well.

**Marcel Santilli:** I, I've never done this, so let's just see if it works.

**Marcel Santilli:** But that, that's kind of like the, the idea, right?

**Marcel Santilli:** Okay, so now this is all almost done running this one is like a little slow because it's not just doing the transcript is also enriching all the things, you know, and, and trying to like do a bunch of other items, right?

**Marcel Santilli:** Like, so obviously this is going to

**Marcel Santilli:** be very compute intense.

**Marcel Santilli:** None of these things are yet like at a place where it's like, okay, let's have the whole like company do

**Marcel Santilli:** this and, you know, and.

**Marcel Santilli:** And the system's still very, like, brittle,

**Marcel Santilli:** if you will, on.

**Marcel Santilli:** On a lot of it, but it's already makes a huge, huge difference, you know?

**Ella Dillon:** Cool.

**Marcel Santilli:** Let's see what are other examples I can pull here?

**Marcel Santilli:** Let's do a study guide, because the study guide is probably one of the

**Marcel Santilli:** most, like, powerful ones.

**Marcel Santilli:** So there you go.

**Marcel Santilli:** Like, it did the whole.

**Marcel Santilli:** Yeah, sorry, go ahead.

**Ella Dillon:** I was just gonna say.

**Ella Dillon:** Oh, never mind.

**Ella Dillon:** You're there.

**Ella Dillon:** I was gonna say if you could do it in Claude, but you're there, so never mind.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** So let me.

**Marcel Santilli:** This.

**Marcel Santilli:** Because I don't think this had.

**Marcel Santilli:** All right, what's a topic that y'

**Marcel Santilli:** all want to research.

**Marcel Santilli:** Or what's.

**Valentina Giraldo Morales:** All right, I'll.

**Valentina Giraldo Morales:** I'll be brave.

**Bridget McGillivray:** Okay.

**Valentina Giraldo Morales:** So actually, this is leveraging things that other people have built that I want to combine.

**Valentina Giraldo Morales:** So Kyle and Panzer both have, like, skills looking at performance, and Valentina has built a skill looking at, like, the five, like, health scoring pieces.

**Valentina Giraldo Morales:** We.

**Valentina Giraldo Morales:** I want to build a, like, output that you want to read at the beginning of every week or at the end of every week.

**Valentina Giraldo Morales:** Like, putting those skills together and leveraging, like, the preferences here.

**Valentina Giraldo Morales:** I don't even know where to start.

**Marcel Santilli:** Okay, so let me try to make sure I understand.

**Marcel Santilli:** What are the skills that Panzer and Valentina have built?

**Marcel Santilli:** Just.

**Marcel Santilli:** I understand.

**Ella Dillon:** Well, the pipeline quality report that Panzer built.

**Kyle Gaudreau:** So, Panzer, Panzer, I think you even mentioned, and I didn't realize this, that you were plugging in some of the quantitative data, basically.

**Matthew Panzarino:** Yeah, yeah, yeah.

**Marcel Santilli:** Oh, sorry, Go ahead, go ahead.

**Kyle Gaudreau:** I was just going to say real quick.

**Kyle Gaudreau:** What I built was basically something that is extracting a lot of the, like, key data points we want to see on, like, a weekly trending basis from the Looker dashboard, so we can get a pulse on, like, what's trending up, down, flat, etc.

**Kyle Gaudreau:** I didn't realize.

**Kyle Gaudreau:** Panzer, you already had some of the

**Matthew Panzarino:** quant in there, and so it's probably

**Kyle Gaudreau:** just like an alignment on logic more than anything.

**Matthew Panzarino:** Yeah, yeah, it's totally.

**Matthew Panzarino:** It is the only.

**Matthew Panzarino:** I built two major reports that I exported the skills of, packaged them and handed them over, like, hey, you can play around with these.

**Matthew Panzarino:** And the one was a client snapshot skill, which I think you saw one of those or two of those, Marcel, which is basically just a.

**Matthew Panzarino:** What is the state of this client right now?

**Matthew Panzarino:** And I feel it's something that can be and should be automated in a way that it runs every week and is available in every client either in HubSpot or someplace in the client space.

**Matthew Panzarino:** And it basically gives a complete rundown.

**Marcel Santilli:** Whereas every.

**Matthew Panzarino:** Any person, we just hired them yesterday, they could walk in and understand where that account is today.

**Matthew Panzarino:** That includes stakeholders, deliverables, history of management of the account, history of performance of the account.

**Matthew Panzarino:** It's a quantitative bit pulled from looker, like, what wins have we had for this account?

**Matthew Panzarino:** What losses have we had?

**Matthew Panzarino:** What are the critical issues that we need to address for the account right now?

**Matthew Panzarino:** And then a section on predictive, like a section on client health.

**Matthew Panzarino:** And then a section on predictive client health.

**Matthew Panzarino:** Like, hey, we know you rated this client health this way.

**Matthew Panzarino:** But given these semantic signals from the internal, external Slack channels, performance issues that ENG has, pipeline management, whatever, here's how we actually score the.

**Matthew Panzarino:** Or we think the score would be for this account if we took all those things into consideration.

**Matthew Panzarino:** As an example, hey, we haven't actually been able to report for them because the tag has been broken for two weeks or publishing has been delayed because of XYZ or.

**Matthew Panzarino:** Okay, the account score should actually be negative 1 or negative 2 from there instead.

**Marcel Santilli:** Right?

**Valentina Giraldo Morales:** Valentina, do you want to share the skill that you built on health scoring?

**Valentina Giraldo Morales:** Because it pulls in some of Marcel's, like previous docs on health scoring and things like that.

**Ella Dillon:** Stupid question is, where do people put these skills and then have just like drop them into my.

**Ella Dillon:** My own working session?

**Ella Dillon:** Do I just.

**Ella Dillon:** Yeah, that'd just be nice.

**Marcel Santilli:** You don't have it in a GitHub repo somewhere this goes.

**Valentina Giraldo Morales:** You know, my.

**Valentina Giraldo Morales:** It's on my.

**Valentina Giraldo Morales:** It's in my cowork.

**Valentina Giraldo Morales:** Yeah, I can share it here to the chat, if that's okay.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** Or yeah, drop it there.

**Marcel Santilli:** Anywhere I can download the file and

**Marcel Santilli:** then I can make it available.

**Marcel Santilli:** Like.

**Matthew Panzarino:** Yeah, I haven't committed mine to GitHub.

**Matthew Panzarino:** I packaged them as skills because people were using Cowork, so it was easier for them to import.

**Matthew Panzarino:** But I can absolutely commit them to the repo.

**Marcel Santilli:** But even with Cowork, right, It's still

**Marcel Santilli:** a file somewhere, right?

**Matthew Panzarino:** Oh, no, I have.

**Matthew Panzarino:** I have the skills files.

**Matthew Panzarino:** I can drop them for sure.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Do you want to just DM me on Slack or both of you, and then I'll.

**Marcel Santilli:** I'll just pull it real quickly and then.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** Okay, so I think the easiest thing

**Marcel Santilli:** is going to be like, give me a second here.

**Marcel Santilli:** Okay, so by the way, this finish running.

**Marcel Santilli:** So.

**Marcel Santilli:** So that's great.

**Marcel Santilli:** Like, it had like a lot of

**Marcel Santilli:** the details and whatnot.

**Marcel Santilli:** And then let's see.

**Marcel Santilli:** I'M gonna have this post this take away to the.

**Marcel Santilli:** The most annoying part I think about

**Marcel Santilli:** all of this is that like this

**Marcel Santilli:** mcps are so unreliable.

**Marcel Santilli:** You know, it's like you, you have this like.

**Marcel Santilli:** And it still doesn't freaking like sometimes post, you know.

**Marcel Santilli:** So it's, it's really, really annoying to

**Marcel Santilli:** sales channel on Slack.

**Marcel Santilli:** So let's hope that that works.

**Marcel Santilli:** And then I'm going to start another really quickly and say on the handbook, you and

**Marcel Santilli:** that new section under tools and the handbook for skills that are to.

**Marcel Santilli:** Put this in plan mode first.

**Marcel Santilli:** So that's the cool thing with the handbook by the way.

**Marcel Santilli:** For anyone that is not familiar, the handbook is what I'm constantly putting things

**Marcel Santilli:** in here that are like more on out, right?

**Marcel Santilli:** Like for instance, like I was trying to pull reports from HubSpot so I was like, hey, can you just go and tell me like all the objects in HubSpot, you know, like literally.

**Marcel Santilli:** And then like,

**Marcel Santilli:** like give me an entire architecture of how HubSpot is set

**Marcel Santilli:** up pretty much in a map.

**Marcel Santilli:** That way like I can reference later

**Marcel Santilli:** when I'm asking MCP server to do something for me in HubSpot, right?

**Marcel Santilli:** So like as I'm doing these things you can see I'm.

**Marcel Santilli:** I'm literally like putting everything in here.

**Marcel Santilli:** Like I just ran this one earlier today on LLM Writing Mastery because like

**Marcel Santilli:** we're thinking of like I was just

**Marcel Santilli:** like, let me just see like what

**Marcel Santilli:** this process will give me as far as like what's out there in the world as far as like how to,

**Marcel Santilli:** how to have LLMs.

**Marcel Santilli:** Right.

**Marcel Santilli:** Better than you know, or just as good as humans, if you will.

**Marcel Santilli:** And any research that's out there on it and you can see, it's like, it's really detailed, it's really good.

**Marcel Santilli:** And this might feel overwhelming to some

**Marcel Santilli:** of you, but this is the level of depth I want.

**Marcel Santilli:** And, and like it's so packed with like, you know, things I want to see.

**Marcel Santilli:** And by the way, like the mermaid, like diagrams and graphs are like the

**Marcel Santilli:** best thing ever because I'm a visual person.

**Marcel Santilli:** It's just like it's so helpful to

**Marcel Santilli:** have these everywhere, you know.

**Marcel Santilli:** And so.

**Marcel Santilli:** Okay, so give me a second.

**Marcel Santilli:** Let me pull whatever you all have DM me.

**Marcel Santilli:** Give me a second.

**Marcel Santilli:** And downloads.

**Marcel Santilli:** Give me a second.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** Got it.

**Marcel Santilli:** Okay, so they're all here.

**Marcel Santilli:** So this one looks like pretty easy to port over and then this one looks like it's a Claude skill.

**Marcel Santilli:** So let's just try to.

**Marcel Santilli:** I'm going to do Two things here.

**Matthew Panzarino:** You can just rename it as a zip and throw the files in there, or you can throw it the skill,

**Marcel Santilli:** have it unpack it itself.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Okay, so let me do this next.

**Marcel Santilli:** Three skills to my project, then create.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Let's see if it works.

**Marcel Santilli:** So I'm just taking these three.

**Marcel Santilli:** One of the file, the other ones dot skill.

**Marcel Santilli:** So, you know, it's the kind of stuff that's like, normally you would be like, oh, it's not going to work.

**Marcel Santilli:** Let me go rework this file, like to Panzer's point.

**Marcel Santilli:** But probably can't unzip something and do everything, so.

**Marcel Santilli:** All right, while it's loading, let's see here.

**Marcel Santilli:** It came up with a plan, so let's build it.

**Marcel Santilli:** So this is the plan to go update the.

**Marcel Santilli:** Create a catalog in the guides for skills.

**Marcel Santilli:** So this is like the handbook.

**Marcel Santilli:** So it's essentially like putting all the skills there so that it's easier for all of you to download it.

**Marcel Santilli:** So what else did it post us in the channel?

**Matthew Panzarino:** One thing I think is probably important to mention on this call, Marcel, and maybe I would love to hear how you handle it and think about it, but is scoping. Because when you connect your various context layers, it's important to think about scoping because of how powerful it is. It can be too potent at some points. So it's worth talking about. Like when you're connecting your accounts and MCPs, how to think about the scope of what the output is going to present and what audiences it has, et cetera. Like presenting internal documents to clients and vice versa, or different layers of the company.

**Kyle Gaudreau:** That kind of.

**Marcel Santilli:** Yeah, I think you probably have spent more time thinking about that.

**Marcel Santilli:** Like, for me, like, the biggest unlock for me is compounding my context, right?

**Marcel Santilli:** It's like, it's like what you just saw.

**Marcel Santilli:** Like, I just used this project to

**Marcel Santilli:** improve this project and clean up this project.

**Marcel Santilli:** You know, it's like the.

**Marcel Santilli:** The study guide, like, you know, like it's running this really quickly, but let's just go in here like, okay, it's almost done running it looked at 500 sources.

**Marcel Santilli:** You know, I just like set it

**Marcel Santilli:** and go do something else, you know, And.

**Marcel Santilli:** And now it's like, hey, here's the research to study guy best practices on

**Marcel Santilli:** building skills for Claude.

**Marcel Santilli:** And now it's going to go and do this crazy research on building skills, right?

**Marcel Santilli:** And then I convert that to a guide in the handbook, and then I use this guy to see, hey, is there any improvements I should make to my skills?

**Marcel Santilli:** But Then.

**Marcel Santilli:** And then I can build a skill

**Marcel Santilli:** that's called the skill Builder that's based

**Marcel Santilli:** on this study guide.

**Marcel Santilli:** That then now is a rule that every time I'm building a skill reference this, you know, does that make sense?

**Marcel Santilli:** Like, it's like the.

**Marcel Santilli:** That's what I use it the most is like to compound like that.

**Marcel Santilli:** And.

**Marcel Santilli:** And I, I have not spent a lot of time trying to take it like 100% automation because for me, like,

**Marcel Santilli:** this is what's really, really powerful.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like, I'll give you an example from

**Marcel Santilli:** that I did yesterday.

**Marcel Santilli:** I had it fetch every single calendar

**Marcel Santilli:** since GrowthX was created.

**Marcel Santilli:** And gosh, wasn't this one?

**Marcel Santilli:** No.

**Marcel Santilli:** Okay, there you go.

**Marcel Santilli:** There's this.

**Marcel Santilli:** Look at this.

**Marcel Santilli:** This was wild.

**Marcel Santilli:** Create a new command and skill to

**Marcel Santilli:** go through my calendar and create a record of every meeting that happened in the past.

**Marcel Santilli:** And then it built the skill.

**Marcel Santilli:** Now run this process for this whole

**Marcel Santilli:** month that was the run of February.

**Marcel Santilli:** Cool.

**Marcel Santilli:** 220 calendar.

**Marcel Santilli:** And by.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** Now I'm just like, cool.

**Marcel Santilli:** Like all those meeting, blah, blah, blah.

**Marcel Santilli:** Okay, awesome.

**Marcel Santilli:** And then I essentially had it run

**Marcel Santilli:** and go do this for.

**Marcel Santilli:** All right, now let's organize this by month in folders.

**Marcel Santilli:** It's like.

**Marcel Santilli:** And then.

**Marcel Santilli:** All right, now let's do the same

**Marcel Santilli:** for January just to make sure it was good.

**Marcel Santilli:** And then after it was good.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Now let's repeat the process and do

**Marcel Santilli:** the whole like all the way back.

**Marcel Santilli:** And then there's a couple of things where the session fail or whatever.

**Marcel Santilli:** This is just like cloud essentially going, hey, the session needs to be continued

**Marcel Santilli:** because there's so much context in here.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** And then it pulled January.

**Marcel Santilli:** And then I had to pull like all 14 months.

**Marcel Santilli:** So like 1300 meetings processed.

**Marcel Santilli:** You know, this is going through my

**Marcel Santilli:** entire calendar, you know, and then like.

**Marcel Santilli:** And then it's like, now give me

**Marcel Santilli:** some takeaways about the structure of my weekend.

**Marcel Santilli:** Basically, it's literally like analyze my entire

**Marcel Santilli:** calendar patterns for based on like every

**Marcel Santilli:** meeting I I've had since the beginning

**Marcel Santilli:** of times almost, you know, like, so

**Marcel Santilli:** it's the kind of stuff that's like

**Marcel Santilli:** super freaking powerful, you know?

**Marcel Santilli:** Cool.

**Marcel Santilli:** So let's see.

**Marcel Santilli:** All right, so it looks like this is working.

**Marcel Santilli:** And then the research should be done or close to being done.

**Marcel Santilli:** Let's see.

**Marcel Santilli:** Okay, it looks like it's almost done.

**Marcel Santilli:** And then now let's go back here.

**Marcel Santilli:** And.

**Marcel Santilli:** All right, the handbook skills are done and guide tools.

**Marcel Santilli:** So let me just spin up the local dev.

**Marcel Santilli:** By the way, it posted the.

**Marcel Santilli:** The meeting, all the notes Here, which

**Marcel Santilli:** is like, super, super good.

**Marcel Santilli:** You know, it's like, there's way more detail.

**Marcel Santilli:** If you compare this to Firefly notes, it's going to be like, you know, nowhere near as good.

**Marcel Santilli:** Like, to give you another example, like, I did this one the other day too.

**Marcel Santilli:** Or like, like this one, you know, it's like looking at so many opportunities, so many things, you know, so.

**Marcel Santilli:** All right, cool.

**Marcel Santilli:** So let's see what it did.

**Marcel Santilli:** AI Skills.

**Marcel Santilli:** Okay.

**Marcel Santilli:** The skills catalog.

**Marcel Santilli:** So now you can.

**Marcel Santilli:** You all can use the handbook and just pull the skills from here, and I'll just like, keep improving this and putting all the skills here.

**Ella Dillon:** So is that where.

**Ella Dillon:** Because there's been some comments in the chat about, you know, building out a library of skills as people create them.

**Ella Dillon:** Do we want people to make this the library or.

**Marcel Santilli:** Yeah, like, the handbook is.

**Marcel Santilli:** Where is the thing that I'm hoping

**Marcel Santilli:** will be shareable for everybody?

**Marcel Santilli:** You know, because it's already in GitHub, you know, and so.

**Marcel Santilli:** So I think it's like, actually let

**Marcel Santilli:** me improve this really quickly.

**Marcel Santilli:** Let's create a whole new section called AI Skills.

**Marcel Santilli:** And each skill should be a page

**Marcel Santilli:** with documentation what the skill is, a way to download the file itself directly,

**Marcel Santilli:** as well as, like, what command to use to install it in into their repo or whatever they're using, and so move everything there.

**Marcel Santilli:** All right.

**Marcel Santilli:** All right, cool.

**Marcel Santilli:** I'll.

**Marcel Santilli:** I'll create a new section here that's called AI Skills.

**Marcel Santilli:** You know, like, same way I'm creating like, like tutorials and guides and things like that.

**Marcel Santilli:** But that's the idea is like, hopefully,

**Marcel Santilli:** like, we all share the skills and

**Marcel Santilli:** put it in one place, because otherwise it's the issue we just ran into,

**Marcel Santilli:** which is like, people are sipping files and sending files along, and hopefully there's like an actual doc on.

**Marcel Santilli:** On the skill itself, you know?

**Marcel Santilli:** Cool.

**Marcel Santilli:** Okay, so this is running.

**Marcel Santilli:** Let's hope that.

**Bridget McGillivray:** All right.

**Marcel Santilli:** Why is this thing taking a little longer

**Marcel Santilli:** then?

**Marcel Santilli:** Okay, it looks like these skills all worked now.

**Marcel Santilli:** All done set up.

**Marcel Santilli:** I thought there was three.

**Marcel Santilli:** Isn't it Health scoring account?

**Marcel Santilli:** It's two, but I zipped one in

**Valentina Giraldo Morales:** case it was easier for you to pull it into like, or something.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** All right, cool.

**Marcel Santilli:** So after this is done running, I'll make sure, like, it also gets, like, added to here if it didn't, you know, but.

**Marcel Santilli:** But then this will be.

**Marcel Santilli:** Package it up here.

**Marcel Santilli:** All right, let me pause here.

**Marcel Santilli:** I know this is a lot.

**Marcel Santilli:** I know this is not super structured on, like, the step by step to replicate this but hopefully this gives folks

**Marcel Santilli:** a little bit of like kind of how powerful this is.

**Marcel Santilli:** You can see how much stuff is happening at once.

**Marcel Santilli:** Right?

**Marcel Santilli:** Like so this is like literally it's like on crazy like overload, you know,

**Marcel Santilli:** like this stuff that it's doing all at once is kind of pretty, pretty insane, you know, know.

**Marcel Santilli:** Questions.

**Marcel Santilli:** What would be helpful to go from here?

**George Haikal:** You maybe you showing like quickly end to end how you've used it for something.

**George Haikal:** Like what I'm thinking is you sent in the sales channel a really good like ROI calculator and sheet for a client.

**George Haikal:** Like did you use a bunch of these tools to put that together?

**George Haikal:** Like showing us how you went from idea.

**George Haikal:** You do all these tasks, you run the sales process, you want to make it easier and better to final deliverable.

**George Haikal:** Like that might be a good thing to run through.

**Marcel Santilli:** Okay, sounds good.

**Marcel Santilli:** So let me.

**Ella Dillon:** And then also I'm just thinking about to what Bridget's point about like you've done so much work on your own individual guides around your tone and your writing style and et cetera.

**Ella Dillon:** I feel like I have to start all that from scratch.

**Ella Dillon:** Or I can just pretend I'm Marcel and just use all of the things that you did.

**Ella Dillon:** So I guess any advice on as we're building out our own personal reference to expedite it, any guidance there would be really useful.

**Marcel Santilli:** Okay, let me, let me do that

**Marcel Santilli:** then first because I think that will help everybody else.

**Marcel Santilli:** So let me share my screen.

**Marcel Santilli:** I'm going to try to do it as fast as possible, so bear with me.

**Marcel Santilli:** Okay, so there is a starter kit

**Marcel Santilli:** repo that I'm pretty sure it's public.

**Marcel Santilli:** Public, yes.

**Marcel Santilli:** So it's public and it's in our

**Marcel Santilli:** repo

**Marcel Santilli:** and so I'm going to use this.

**Marcel Santilli:** So.

**Marcel Santilli:** Okay, so projects new folder.

**Marcel Santilli:** Let's call this.

**Marcel Santilli:** Context OS demo.

**Bridget McGillivray:** Cool.

**Marcel Santilli:** Drag and drop.

**Marcel Santilli:** Open a cursor new project.

**Ella Dillon:** Can you open it?

**Ella Dillon:** If I'm not supposed to using cursor you.

**Marcel Santilli:** You can open MPS code to set it up.

**Marcel Santilli:** You know from.

**Marcel Santilli:** Again, this is not the way.

**Marcel Santilli:** I'm sure engineers do this.

**Marcel Santilli:** This is the way I do it.

**Marcel Santilli:** So it's like.

**Valentina Giraldo Morales:** And.

**Marcel Santilli:** And all I'm doing is you can do this in.

**Marcel Santilli:** In the Claude Code extension here as well.

**Marcel Santilli:** So I'll show that in a second, but.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** So what it's doing now is should pull everything.

**Marcel Santilli:** See it pull the whole thing.

**Marcel Santilli:** You see here?

**Marcel Santilli:** Yep.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** I already have the handbook like done the same way in my local here.

**Marcel Santilli:** So assume you're doing the same thing

**Marcel Santilli:** with the handbook, right?

**Marcel Santilli:** Like, you're creating a folder and you're

**Marcel Santilli:** just pulling the handbook, assuming you have access to it.

**Marcel Santilli:** That one is like, should be the whole org.

**Marcel Santilli:** But Leo and Yousef can figure out

**Marcel Santilli:** if somebody doesn't have access to it.

**Marcel Santilli:** But it would be the same.

**Marcel Santilli:** Same thing as this.

**Marcel Santilli:** You can see, like, the whole repo got pulled

**Marcel Santilli:** and.

**Marcel Santilli:** Hold on one second.

**Marcel Santilli:** Let's make sure.

**Marcel Santilli:** What did I do wrong here?

**Marcel Santilli:** Oh, okay.

**Marcel Santilli:** Sorry.

**Marcel Santilli:** This is the wrong project.

**Marcel Santilli:** I was like, this does not look right.

**Marcel Santilli:** It's the context OS starter.

**Marcel Santilli:** Okay, let's start from scratch.

**Marcel Santilli:** Apologies.

**Marcel Santilli:** Do not do what I just did.

**Marcel Santilli:** Let me close this and then I'm going to nuke what I just did and I'm going to start again.

**Marcel Santilli:** I was like, this looks nothing like, you know, it's going to need something

**Marcel Santilli:** new just in case.

**Marcel Santilli:** All right,

**Marcel Santilli:** I cool.

**Marcel Santilli:** It's going to do that on this.

**Marcel Santilli:** And it should load up everything in here.

**Marcel Santilli:** That's what I would do first.

**Marcel Santilli:** Once it finishes loading this.

**Marcel Santilli:** There you go.

**Marcel Santilli:** It's all set up now.

**Marcel Santilli:** All right, so

**Marcel Santilli:** now, like, all the

**Marcel Santilli:** stuff, like, can be loaded differently.

**Marcel Santilli:** And so, like, what I'm going to

**Marcel Santilli:** do next is like, essentially like add folder to a workspace, actually save workspace s and then call this, like, essentially the same thing.

**Marcel Santilli:** Okay, so now this is a workspace,

**Marcel Santilli:** and then you can add folder to workspace.

**Marcel Santilli:** So essentially what you're doing is like, think of like a folder as like a project and you want to have

**Marcel Santilli:** two projects running in parallel.

**Marcel Santilli:** Right?

**Marcel Santilli:** So add folder to the workspace and

**Marcel Santilli:** then I'm gonna go grab the handbook.

**Marcel Santilli:** One growth text handbook.

**Marcel Santilli:** It's already here.

**Marcel Santilli:** So you would just follow the same process to do the same thing.

**Ella Dillon:** I'm assuming it's the same if I'm in Claude.

**Ella Dillon:** Same process.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** The only difference is, like, you're gonna do command shift P and open a new cloud window.

**Marcel Santilli:** And now there's a cloud conversation that works the same way as an agent.

**Marcel Santilli:** You know, they can do all these things and I'll.

**Marcel Santilli:** I'll show you in parallel here in a second.

**Marcel Santilli:** Okay, so now you have both.

**Marcel Santilli:** Right.

**Marcel Santilli:** So I'll put in plan mode and just say look at the.

**Marcel Santilli:** Handbook.

**Marcel Santilli:** And

**Marcel Santilli:** come up with how to.

**Bridget McGillivray:** Cool.

**Marcel Santilli:** And then I'm going to do kind of the same here

**Marcel Santilli:** to run in parallel.

**Marcel Santilli:** And.

**Marcel Santilli:** And all I'm doing is like asking

**Marcel Santilli:** it to look at the handbook and then tell me how to improve the demo, you know, but.

**Marcel Santilli:** But like, this just kind of show

**Marcel Santilli:** you, like, in parallel.

**Marcel Santilli:** So like this is Claude working, this is Cursor working, the same request.

**Marcel Santilli:** And also you can do a bake off on the plan.

**Marcel Santilli:** If it's in plan mode, it's okay to do that.

**Marcel Santilli:** If it's like an agent mode and

**Marcel Santilli:** they're actually taking actions, you don't want to do that because then one might override the other, you know, and find over.

**Marcel Santilli:** But it's like, man.

**Marcel Santilli:** Okay, so in the project demo you

**Marcel Santilli:** can see like the docs are just like scaffolding of the docs.

**Marcel Santilli:** So what I would do if I

**Marcel Santilli:** was you all is like something kind of like this nice, the context project demo.

**Marcel Santilli:** And then come up with a set

**Marcel Santilli:** of 21 questions to

**Marcel Santilli:** personalize this to

**Marcel Santilli:** me

**Marcel Santilli:** and I'll put it in plan

**Marcel Santilli:** mode first, you know, and like something like this, you got to start somewhere, right?

**Marcel Santilli:** Like, but the good news is like, you have an insane amount already in the handbook one to like, of context

**Marcel Santilli:** already in the docs, right?

**Marcel Santilli:** And so, so that makes it like way easier to do that, you know.

**Marcel Santilli:** So, okay, so you can see like both of them are thinking because they're

**Marcel Santilli:** reading through the two projects, right?

**Marcel Santilli:** So that's a lot of reading to do, you know.

**Marcel Santilli:** So this might take a minute, but does that make sense so far?

**Marcel Santilli:** Like, like to this point if you're

**Marcel Santilli:** trying to like start from scratch.

**Marcel Santilli:** And by the way, like, you can do like a new here too.

**Marcel Santilli:** And, and you can like do like research to study guide and like these commands already here that I already set up.

**Marcel Santilli:** And, and then like, and it's going

**Marcel Santilli:** to start loading a bunch of things,

**Marcel Santilli:** but obviously like they are probably not going to be fully there.

**Marcel Santilli:** Let me see.

**Marcel Santilli:** Yeah, Index has nothing.

**Marcel Santilli:** So.

**Marcel Santilli:** So it's like it's empty.

**Marcel Santilli:** But at least it's like, you know, with the handbook you can fill it up.

**Marcel Santilli:** Right?

**Marcel Santilli:** Okay, so now you have two things here in parallel.

**Marcel Santilli:** You have the personalization plan.

**Marcel Santilli:** Then there is like the like adapting the context os.

**Marcel Santilli:** This was cursor.

**Marcel Santilli:** You can see it got done first because it does a lot more stuff in parallel, AKA it uses a lot more credits a lot faster.

**Marcel Santilli:** And so it's like core identity, fill in cloud MD root files, blah, blah, blah, company name, voice port, writing style and social guides.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Role port.

**Marcel Santilli:** All 15 functional roles, Personas from the

**Marcel Santilli:** handbook Gray knowledge port, study guides and research.

**Marcel Santilli:** Cool.

**Marcel Santilli:** And I mean it's pretty much the

**Marcel Santilli:** whole thing, you know.

**Marcel Santilli:** The only thing here that I haven't figured out yet is like how to make sure like you all don't do that and not reference the handbook, because the handbook is like, the more accurate thing.

**Marcel Santilli:** So what I would do instead here is say,

**Marcel Santilli:** can you do some link

**Marcel Santilli:** to the handbook for all these things instead way in book?

**Marcel Santilli:** All right, so.

**Marcel Santilli:** That's what I would do.

**Marcel Santilli:** So, like, sim link or whatever.

**Marcel Santilli:** I don't know if that's the best

**Marcel Santilli:** way to do it.

**Marcel Santilli:** So technical people here can tell me if this is wrong or not.

**Marcel Santilli:** But.

**Marcel Santilli:** Yeah,

**Marcel Santilli:** Just try this.

**Marcel Santilli:** And this is in plan mode, so it's just going to adapt the plan to that.

**Marcel Santilli:** But you can see the difference.

**Marcel Santilli:** Like, cursor already finished running.

**Marcel Santilli:** And it's like you're like three steps

**Marcel Santilli:** ahead now, and this is almost done running, but then we'll be able to compare, like, what this comes up with and see, like, if it's any good,

**Marcel Santilli:** you know,

**Marcel Santilli:** Is this helpful?

**Marcel Santilli:** Okay.

**Marcel Santilli:** It's a little weird because, like, right now how I'm running in the main one is like the handbook.

**Marcel Santilli:** I almost never use the docs anymore because, like, I had already processed the docs into the handbook.

**Marcel Santilli:** I didn't delete it from here.

**Marcel Santilli:** But I keep saying, I keep, like, in my prompt, I'll say, look at the handbook or.

**Marcel Santilli:** Or look at this part of the handbook.

**Marcel Santilli:** So I say that all the time in my prompts, but that's all I have to do because, like, because I organize the handbook, I know where things are, and it's not gnarly.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like, the handbook, you're talking like a

**Marcel Santilli:** hundred pages max right now.

**Marcel Santilli:** Right.

**Marcel Santilli:** And.

**Marcel Santilli:** And so it makes it a lot,

**Marcel Santilli:** a lot easier to do that.

**Marcel Santilli:** So let's see.

**Ella Dillon:** So what are some of your prompts that you have in your directory over there?

**Ella Dillon:** What's an example of that?

**Marcel Santilli:** I stopped using it.

**Ella Dillon:** You did it.

**Ella Dillon:** Okay.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Like, I literally stopped using it because, like, prompts don't matter, just mostly how you organize the context.

**Ella Dillon:** Yeah.

**Marcel Santilli:** Yeah.

**Valentina Giraldo Morales:** Okay.

**Ella Dillon:** All right, so in terms of.

**Ella Dillon:** It sounds like we reference the context OS for sort of like all things truth.

**Ella Dillon:** It is also going to be the place where the company kind of contributes skills, like the things that all of.

**Ella Dillon:** All the questions all of us are asking.

**Ella Dillon:** If someone's built a great skill for us to answer the questions, we can reference it there.

**Ella Dillon:** So the only like, net new context I would have to build for myself to maximize this OS for me, again, is replicating some of the work you've done for yourself personally.

**Ella Dillon:** On, like, here's my tone, here's my voice, here's my style, here's what you should reference in the way I want to communicate, like, we should all have a point of view about how we build out that reference library for ourselves.

**Ella Dillon:** Anything else outside of what is built at the company level and the skill level that we'll be sharing, that for us to be fully optimized, we need to make sure our own mental model is clear and crisp and built out in a directory that maybe we can't just borrow from what you've already done outside of our own tone and voice.

**Marcel Santilli:** I've been trying to put as much as possible from my knowledge there, but there are things here in my scratchpad

**Marcel Santilli:** or knowledge that are not there.

**Marcel Santilli:** So, for instance, like, oh, shit, I'm in the demo one.

**Marcel Santilli:** Sorry, give me a sec.

**Marcel Santilli:** Yeah, so just to give an example here, the pipeline scratchpad, like, there's this one, for example, we just ran today, right?

**Marcel Santilli:** Like, and this is part of the scratch pad that then became the output, and these are some of the outputs.

**Marcel Santilli:** This is like the messy stuff, you know, and then there's stuff in the knowledge that I haven't really, like, shared yet, but I'm trying to as much as possible, you know, like, convert it.

**Marcel Santilli:** Like, I did one on, like, EA

**Marcel Santilli:** operating guide, like, study guide, you know, CEO email mastery, like, CEO schedule energy optimization guide, you know, calendar time management, you know, like, these are all, like, things that I'm doing because I'm trying to build some.

**Marcel Santilli:** Some level of, like, context or because

**Marcel Santilli:** I'm trying to use this some other way.

**Marcel Santilli:** Like, you know.

**Marcel Santilli:** Yeah, yeah, but.

**Marcel Santilli:** But this is all using the same thing, which is like, you know, going

**Marcel Santilli:** in here and saying, hey, research this.

**Marcel Santilli:** Right?

**Marcel Santilli:** Like, and then it did all of this stuff and then created this, like, insane.

**Marcel Santilli:** What the hell?

**Ella Dillon:** Hey, Panzer, do you have, like.

**Ella Dillon:** Similar to Marcel, I'm assuming, do you have, like, this entire personal directory of, like, your own style guides and such?

**Ella Dillon:** Like, what are some.

**Ella Dillon:** Some things that you've built that would not be in the OS?

**Ella Dillon:** And again, I'm not trying to be a PhD.

**Ella Dillon:** I'm more just.

**Matthew Panzarino:** Yeah, yeah, yeah. So I do — without looking like a conspiracy theorist with, like, all my red lines behind me and stuff — it's quite complex. But yes, at a base level, like, one of the first things I did when Marcel was like, hey, I got this Context OS I put together, was I asked Claude, hey, look at my setup. And look at Marcel's setup. Look at the context he's provided here. What's missing from my context that Marcel has provided? And there were absolutely things and it was like, hey, we can add this, we can add this. I said, that's great, please add that to my context.

**Matthew Panzarino:** But at the same time, I do have my personal roles and responsibilities and communication styles documents set up. My CLAUDE.md is set up to understand my scope. You know, I am the CTO. So like, here are the things that I do, here's my job, here's what I communicate about, here are the things that I care about. That way, when it is putting things together, it knows what's important and what's not. So if I'm saying, hey, evaluate client status, it knows I'm evaluating it from a perspective where I care deeply about like pipeline efficiency and content quality and that sort of thing. So the things that it chooses to surface are based on those rules, and the updating of those rules does not have to be manual. Like, you don't have to open up the CLAUDE.md and type words in there.

**Matthew Panzarino:** You can talk to it about the way that you work. You could even have it conduct a survey with you. So you can open Claude, whether it's Claude Code or Cowork, whatever, it doesn't matter as long as it has access to your context files. You could say, hey, conduct a survey with me about my job, my role is X at GrowthX, I do this, here's some things that I care about. Conduct a survey with me to help you better understand what I do every day, what I care about, how I communicate, etc. And it will ask you questions and you can answer them and you can do that on a regular basis.

**Matthew Panzarino:** You can also have it review transcripts from your last 10 calls, last 20 calls, last 50 calls, and say, hey, to help you understand what I do all day, here are some transcripts of calls. Go grab those and ask me any questions that you have. But update my rules, update my documents to help you understand what I do in more context, in better context. And so like, there's no reason that it can't learn about you and you can't prompt it to do so.

**Matthew Panzarino:** But it can also help you to understand what it doesn't know. So you could say, I want you to do these things. And do you have the context to do these things? If not, tell me what you need. And it's like, well, I notice I don't have access to transcripts. You're like, ah, I forgot to connect Fathom or Fireflies. Okay, let me connect that. Like you can ask it what it's missing to give you what you want.

**Matthew Panzarino:** Here's the thing that I caution everybody on. It will give you a result whether it has the right context to answer the question or not. So if you don't give it the right context, that's your fault, right? It will do its job. Like it's going to do a job. Because it will not tell you no unless you write specific rules. Mine has rules that tell me I'm stupid. It says like, if I ask you to do something you don't know how to do, or you don't have the right context to do, please tell me I'm an idiot. Like, I wrote those rules myself. But by default it will not do that. It'll just do the job and you'll be like, oh, this is cool. But it doesn't really — like this is not right or it doesn't know these things.

**Matthew Panzarino:** The very next question in your mind or that you can ask it is, what do you need to actually be more accurate about this? And like, you just give it more context. Nine times out of ten, it's more context. The age of being a prompt wizard came and went in 15 minutes, right? Like it's all about the context that it has to answer your questions because you can answer an insanely complex scenario with the dumbest shit prompt if it has the right context. You go like, oh, make me better at my job. If it knows everything about me, it'd be like, well, here's seven things you do poorly. Like, you don't communicate clearly. You talk too much.

**Marcel Santilli:** A great example of this was like I said, look at my project and tell me what I need to clean

**Marcel Santilli:** up in my project.

**Marcel Santilli:** And it gave me like the perfect plan and then it cleaned up the

**Marcel Santilli:** whole thing in you.

**Marcel Santilli:** The indexes were off.

**Marcel Santilli:** You knew how the project work.

**Marcel Santilli:** You knew everything because the scaffolding was

**Marcel Santilli:** already set up, right?

**Marcel Santilli:** And so like the, the I posted about this, but the, the way to think about it is there's like, think of this as I, I'm trying to accelerate everyone's like mental model a little bit and give everybody a handbook that

**Marcel Santilli:** has all the most important context you possibly need on GrowthX.

**Marcel Santilli:** What this is not meant to be

**Marcel Santilli:** is one click replicate like everything I've achieved.

**Marcel Santilli:** Because then you're going to skip the learnings, right?

**Marcel Santilli:** And so part of that process of like adapting and doing this and playing with it, how would I do this?

**Marcel Santilli:** And whatnot.

**Marcel Santilli:** Getting stuck like playing with it.

**Marcel Santilli:** It is like a little bit of like the, the thousand hours do over like do for everybody, you know, and, and that will, will help you.

**Marcel Santilli:** Now there are things I'm trying to

**Marcel Santilli:** work through which is like the handbook

**Marcel Santilli:** was one of them which was like making that share.

**Marcel Santilli:** The next one is like having a place for people to query transcripts directly or, or pull that or a share repo that has all the publicly available transcripts already pre processed so we're not wasting like LLM tokens on processing the same transcripts and analyzing the same transcripts.

**Marcel Santilli:** Then there's some things around like, like a customer like DB kind of thing that has like the latest and greatest from all the customers and all the data you might need.

**Marcel Santilli:** Not like the individuals like the pii,

**Marcel Santilli:** but more like how this account is

**Marcel Santilli:** doing, the health scores, the you know, like the notes, things like that.

**Marcel Santilli:** And, and then there's like a few others so, so that like people don't

**Marcel Santilli:** are not all setting up custom mcps, you know, like the last thing we

**Marcel Santilli:** want is like 92 people using an

**Marcel Santilli:** MCP to pull data direct and write data to HubSpot right now, you know.

**Marcel Santilli:** Okay, so what else

**Ella Dillon:** Andy, did we add answer your question?

**Marcel Santilli:** I know we went all the way

**Marcel Santilli:** around and probably not I have to

**Valentina Giraldo Morales:** watch again and I'll go through GitHub and see if I can find it.

**Valentina Giraldo Morales:** But I think parts of it I

**Marcel Santilli:** doubt I didn't do anything with the skill.

**Marcel Santilli:** So.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** One thing I will say as an encouragement, you can ask Claude how to do anything. And I know George mentioned this a little bit too, but like there's nothing, no question you've asked on this call, that if you have pre-populated it with at least the Context OS that Marcel has set up, that it cannot lead you to water. Like you can absolutely get there. So don't be intimidated. It's absolutely possible that you may get some results which are poor initially because it lacks the proper context. But you can just ask — you will get there.

**Marcel Santilli:** You will get there.

**Bridget McGillivray:** What?

**Bridget McGillivray:** Okay, Panzer, I'm going to ask this because I keep going to you on DM there.

**Bridget McGillivray:** Like I've been trying to.

**Bridget McGillivray:** I'm trying to use co work and connect.

**Bridget McGillivray:** Like they obviously don't have that many connectors out of the box right now and a lot of our tools are not included.

**Bridget McGillivray:** I struggle to connect stuff that's like not out of the off the shelf

**Matthew Panzarino:** yeah, you know what?

**Matthew Panzarino:** And I know you, you tried to use Claude to help you because I suggested that or Claude code to help you debug it.

**Matthew Panzarino:** But like anytime I have an issue.

**Matthew Panzarino:** So like I have, I have usually about three Claude code instances and then seven persistent agents running at any given time.

**Matthew Panzarino:** Not all of them are always active.

**Matthew Panzarino:** But like anytime I need to debug that system, I'd open a Claude code terminal and I'm like, hey, you know my system?

**Matthew Panzarino:** Like, you know what I'm working with here because it know it has all the files, it knows this is, this is broken.

**Matthew Panzarino:** Can you fix this?

**Matthew Panzarino:** And then it goes and fixes it for me.

**Matthew Panzarino:** So in these cases where you're like, I don't have a connector or I'm not sure or whatever, you can ask Claude code to help you in your Slack instance where you are unable to connect.

**Matthew Panzarino:** I think it's just email related.

**Bridget McGillivray:** Yeah, yeah, I can.

**Bridget McGillivray:** That one I'll figure out.

**Bridget McGillivray:** Like, I mean, Ashby doesn't have a connector and so.

**Matthew Panzarino:** Yeah, yeah, yeah.

**Matthew Panzarino:** The Ashby one is super, super tricky because like they have.

**Matthew Panzarino:** Technically there's an unofficial MCP on GitHub that seems reliable.

**Matthew Panzarino:** It's got good reviews and everybody likes it.

**Matthew Panzarino:** You could pull that and then have Claude code build you your own mcp.

**Marcel Santilli:** Right.

**Marcel Santilli:** For that I show you that because like I did that with Fathom today.

**Bridget McGillivray:** Please show me.

**Bridget McGillivray:** Because like I start getting lost.

**Bridget McGillivray:** I'm like going into another platform.

**Marcel Santilli:** I literally like, I, I'm.

**Marcel Santilli:** I'm going to have to find a session here.

**Marcel Santilli:** But I think it says.

**Bridget McGillivray:** Okay, there's actually like a lot of our.

**Bridget McGillivray:** I don't know, maybe it's just me and the tools that I've got on.

**Marcel Santilli:** Okay, so, so this is gnarly.

**Marcel Santilli:** This is my session.

**Marcel Santilli:** So I'm like, I.

**Marcel Santilli:** Okay, this one, it had a, A Fathom already, but it was like a

**Marcel Santilli:** custom one and whatever.

**Marcel Santilli:** Like, let's set up this MCP for Fathom, right?

**Marcel Santilli:** And then it cloned or whatever and then, and then I had to restart it and then it finally did and then I created a folder saying record slash fathom backup.

**Marcel Santilli:** And then I had to write a script.

**Marcel Santilli:** But like it's.

**Marcel Santilli:** Usually there's someone that already created some

**Marcel Santilli:** kind of like, you know, one.

**Marcel Santilli:** And then I think the one that I ended up.

**Marcel Santilli:** Excuse me.

**Bridget McGillivray:** And where would I find that?

**Bridget McGillivray:** That would be somebody in GitHub has, has created this and is sharing it.

**Marcel Santilli:** Yeah, like so, yeah, I sent you the Ashby one.

**Matthew Panzarino:** It was literally somebody else did this, had the same exact problem.

**Matthew Panzarino:** Ashby doesn't have it.

**Marcel Santilli:** Yeah, like, so.

**Marcel Santilli:** So this is the one I built today.

**Marcel Santilli:** It's a Phantom Buster mcp.

**Marcel Santilli:** And I built it and made it

**Marcel Santilli:** public or private, but then I can make it public so people can use it.

**Marcel Santilli:** Like, and.

**Marcel Santilli:** And all I did was like, hey,

**Marcel Santilli:** look at their API and build me an mcp.

**Marcel Santilli:** Because they don't have an mcp.

**Bridget McGillivray:** We're looking at your cursor.

**Bridget McGillivray:** Is that right?

**Marcel Santilli:** Oh, shit.

**Marcel Santilli:** Sorry.

**Marcel Santilli:** Am I not sharing my whole screen?

**Marcel Santilli:** Sorry.

**Marcel Santilli:** Like, I built this today, so this one was crap.

**Marcel Santilli:** It's gonna be hard to find.

**Marcel Santilli:** I have so many sessions here.

**Marcel Santilli:** But it's gotta be here somewhere.

**Marcel Santilli:** I think I might have archived it already.

**Marcel Santilli:** Yeah, I archived it already.

**Marcel Santilli:** But like, let's just do it real quick.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Actually like this.

**Valentina Giraldo Morales:** All right.

**Matthew Panzarino:** There also ends up being some of these little cul de sacs where you also.

**Matthew Panzarino:** I'm just being honest.

**Matthew Panzarino:** You have to do a personal evaluation of your time worth your time, your.

**Matthew Panzarino:** Your ltv.

**Matthew Panzarino:** Bridget, like, what is your time worth to do this?

**Matthew Panzarino:** Or you could say, hey, okay, I tried, but Marcus, can you go do this for me?

**Matthew Panzarino:** Or you know, Kirkland, do you have somebody with free capacity to just like tackle this little thing for me?

**Matthew Panzarino:** Because it would take probably about eight minutes, you know, for them to help

**Marcel Santilli:** you set this up and then you're good.

**Matthew Panzarino:** So I, like, self solving is amazing, but you know, for you, like, for your time, I think about all the things on your plate.

**Matthew Panzarino:** Like, setting up an MCP is absolutely doable by you, but it's just a matter of like, cost.

**Matthew Panzarino:** Sunk costs, you know.

**Marcel Santilli:** Yeah, like, I agree with that 100%.

**Marcel Santilli:** Where I think the trade off is not worth it.

**Marcel Santilli:** It's when you're trying to do it for everybody else.

**Marcel Santilli:** Like, I want to automate this for

**Marcel Santilli:** the whole population of the planet or

**Marcel Santilli:** the company, or I want to create a database where all the transcripts are there.

**Marcel Santilli:** I'm like, I'm not focusing on that.

**Marcel Santilli:** Or I want this to run on schedule every day and then I want it to do this and then this and then that.

**Marcel Santilli:** But it's like if you're doing for you individually, like, I need to figure out how this hiring pipeline is doing.

**Marcel Santilli:** Like, this is totally worth you being resourceful and wasting a little bit of time.

**Marcel Santilli:** Because, like, there's this feeling of building confidence of like, before I had ever used GitHub or cursor or anything in my life.

**Marcel Santilli:** If you said, build me an mcp, I'll be like, the Fuck you talking about?

**Marcel Santilli:** No way I can do this.

**Marcel Santilli:** And there's just something about going through that process and be like, okay, that wasn't that hard.

**Marcel Santilli:** Like, okay, you know, I'll give it a go.

**Bridget McGillivray:** I'll give it another go.

**Bridget McGillivray:** I was just.

**Marcel Santilli:** Yeah.

**Matthew Panzarino:** Once you pierce the veil, it like, it's.

**Marcel Santilli:** It's awesome.

**Matthew Panzarino:** It's like, worth it.

**Bridget McGillivray:** You know, it can do it, but it can't.

**Bridget McGillivray:** And that's.

**Marcel Santilli:** What do I have, for example, like the.

**Marcel Santilli:** I don't know if I probably.

**Marcel Santilli:** I don't think I've ever logged in to actually.

**Marcel Santilli:** But if I have API access, I can, you know, like, we can also do it together.

**Bridget McGillivray:** Yeah, I'll try.

**Bridget McGillivray:** I'll try on.

**Bridget McGillivray:** I'll try next week myself, but.

**Ella Dillon:** Okay.

**Bridget McGillivray:** Yeah, okay, that makes sense.

**Bridget McGillivray:** So I got to use Claude Code.

**Marcel Santilli:** I gotta run.

**Marcel Santilli:** But we can do another session with

**Marcel Santilli:** like, Panzer sharing his craziness, because his craziness beats my craziness and others throw me crazy.

**Marcel Santilli:** I'm.

**Marcel Santilli:** I'm like, mild, Mild, spicy.

**Marcel Santilli:** You know, like, Panzer is like ghost pepper probably.

**Marcel Santilli:** You know, the.

**Bridget McGillivray:** By the way, like, the two follow ups I'm just gonna go to Yousef with is like one, I think he made a new org this morning. So I just need to make sure everybody is in both orgs, but especially this productivity one and Marcel's repos are in there. And then the second one is I sent him what Clint linked, which is like some kind of way for us all to share skills in the productivity org as well. Is there anything else we needed Yousef to do?

**Marcel Santilli:** The other one is just going to be like the transcript piece that I'm processing. Like, I just downloaded 6,700 from Fathom. So I kind of backed up all of Fathom today because I just need to put that in a place, you know, with client.

**Matthew Panzarino:** And I will say, like, first thing you should do, action item off this call — I'll let Marcel interject if he thinks different — but action item is grab the transcript of this call, give it to your Cowork, and say, what do I need to do next? I'm confused. Like, where do I begin? And it'll tell you. It'll give you a step by step of where to go from here.

**Marcel Santilli:** So just pointing that out,

**Clint Shryock:** raise your hand.

**Clint Shryock:** Panzer.

**Marcel Santilli:** Jeez.

**Matthew Panzarino:** Oh, my God.

**Matthew Panzarino:** I'm so sorry.

**Matthew Panzarino:** I jumped the line.

**Marcel Santilli:** Sorry.

**Matthew Panzarino:** No worries, no worries.

**Clint Shryock:** I was just gonna say the thing I shared about the marketplace that needs to be set up, but it's a very generic, like, file system thing, and then you can install the Marketplace. The output team's using one. So that whenever you create a new output project, like, you get our plugin that we wrote for writing workflows, and then if things get pushed to it and change, like version changes, whenever you're running Claude Code or probably Claude Desktop, it can detect that there's newer versions and it can, like, offer to update your plugins. It's really simple. It's just a file system thing exactly like we saw. But yeah, I mean, Claude has an official one on their repo. I use their Marketplace plugins all the time.

**Clint Shryock:** It has to be set up by someone. I'm happy to do that whenever. But it doesn't exist yet.

**Marcel Santilli:** Yeah, that's.

**Marcel Santilli:** That's a great idea.

**Marcel Santilli:** I have to run, but I think we now have Claude enterprise plans, so we can have org plugins and org skills and a bunch of other things. So we just got it set up like last week or this week, and so I'm spending more time with that. But I'll pick your brain on that too, Clint.

**Marcel Santilli:** Okay, I'm gonna — Bridget, I'm gonna give you the host, but see you all. Thank you.

**Ella Dillon:** Thank you, Marcel.

**Ella Dillon:** I appreciate it.

**Bridget McGillivray:** I think we're done, right?

**Marcel Santilli:** Thank you.

**Ella Dillon:** We're done enough.

**Ella Dillon:** Dangerous off.
