# Zena/Marcel

<metadata>
date: 2026-03-02
time: 21:00 UTC
duration: 60 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Zena Dave
fireflies_id: 01KJQT320PSJ24DGSV0CG7HC6X
meeting_link: https://meet.google.com/csg-ohrq-egq
transcript_url: https://app.fireflies.ai/view/01KJQT320PSJ24DGSV0CG7HC6X
keywords: AI workflows, agent systems, skills and commands, markdown documentation, GitHub version control, knowledge management
source: fireflies
enriched_on: 2026-03-03 20:00 UTC
speaker_note: Fireflies frequently misattributed speakers mid-sentence throughout this call. Multiple lines where Zena's words were labeled as Marcel and vice versa have been corrected based on conversational context, question-answer flow, and self-identification cues.
</metadata>

---

## Summary

Marcel walked Zena through the full architecture of GrowthX's AI-powered context system -- from the knowledge graph indexing 600-700 historical meeting transcripts to the skills/rules/commands framework, Cursor vs. Cowork tradeoffs, and GitHub-based version control for team knowledge. They also aligned on protecting GrowthX's IP in upcoming workshops by sharing high-level concepts without revealing proprietary system design. Zena committed to sending Marcel her agent/role/skill distinctions document and running an AI session with her marketing team the next day, while Marcel agreed to support her team in setting up a shared GitHub repo.

---

## Context

This was a follow-up working session between Marcel Santilli (GrowthX founder/CEO) and Zena Dave, a marketing leader at a separate company who is learning GrowthX's AI workflow methodology to apply it within her own team. Marcel and Zena had previously met where Marcel introduced the context OS approach; since then, Zena has been exploring the GrowthX GitHub repo and preparing questions.

Zena came with a structured list of questions about how the system works -- commands vs. skills, Cursor vs. Cowork, skills folder visibility, agent docs, knowledge folder structure, and how to keep local files in sync when her team lives in Google Drive. Marcel answered each question live, screen-sharing and demonstrating the system in real time. Zena is preparing to run an AI session with her three-person marketing team the next day and wanted clarity before facilitating.

---

## Relevance

**To GrowthX Services/Delivery**
- Marcel's internal team session produced "deer in headlights" reactions, signaling the need to simplify onboarding materials before the workshop
- The study guide on skills/rules/commands is an active work product that needs further distillation for non-technical audiences
- Zena's questions directly map to the friction points new users hit -- commands vs. skills confusion, hidden dot-folders, Cursor vs. Cowork selection -- all of which should inform workshop content

**To GrowthX Business Development**
- Zena independently validated the productization potential: "You could just turn it into a product that teams buy"
- She compared the system to "selling a brain" and suggested pricing it at what Marcel's brain is worth ("probably $10 million") -- strong signal that the value proposition resonates with marketing leaders
- Zena's company uses Coda (not Notion or Google Docs), which Marcel identified as "miles better than Google Drive" for integration -- potential integration path to document

**To GrowthX Workshop Strategy**
- Marcel's CTO co-founder explicitly pushed back on revealing proprietary R&D in workshops, creating a clear constraint: share the 101, not the implementation
- Zena offered to help figure out "what do I share" for the workshop, making her a useful sounding board for content scoping
- Zena saw a LinkedIn influencer posting about skills files and called it "elementary" compared to Marcel's approach -- confirms GrowthX is ahead of public discourse on context engineering

**To CheckThat / Product**
- Marcel demoed the content quality scoring research workflow (three scratch pads, three expert roles, tiered factors) -- engineers are "a couple days away" from building this scoring into the product
- The research-to-study-guide-to-knowledge-doc pipeline Marcel demonstrated is a replicable workflow that could become a CheckThat feature or service offering

---

## Decisions & Commitments

- **Workshop IP protection**: Marcel and Zena aligned that the workshop should share high-level concepts (the "101") without exposing the proprietary system architecture. Marcel's CTO reinforced this constraint.
- **Zena to send her agent/role/skill distinctions doc** to Marcel as input for simplifying workshop explanations
- **Zena to run an AI session with her marketing team** (team of 3) the next day, applying what she learned in this meeting
- **Zena to explore creating a shared GitHub repo** for her marketing team's knowledge files
- **Marcel to support Zena's team** in setting up the shared GitHub repo and update processes
- **Commands = shortcuts, Skills = workflows**: Marcel and Zena explicitly settled on this framing as the clearest way to explain the distinction

---

## Open Questions

- How should the workshop content be scoped to share enough value without revealing proprietary system design? Zena offered to help figure this out through her team session.
- Can Zena's company (which uses Coda) integrate effectively with a GitHub-based context repo, or will there be adoption friction with a non-technical marketing team?
- What's the right pricing model for the context OS if it becomes a product? Zena raised this but no framework was discussed beyond the "selling a brain" analogy.
- How should access controls be layered (executive-only, leadership, build team, all employees, public) in the context repo -- Marcel is actively working on this but it's not finalized.

---

## Overview

- **Workshop IP Strategy:** Marcel's CTO pushed back on revealing proprietary R&D in workshops. Marcel and Zena aligned on sharing high-level concepts to establish credibility without exposing the system architecture.

- **AI Knowledge Graph:** Marcel has built an agent-driven system that indexed 600-700 historical meeting transcripts from Fathom, auto-enriches them with metadata, and creates detailed contact profiles that compound over time.

- **Skills, Rules, and Commands:** Clarified as three distinct layers -- skills are reusable workflows, rules are persistent behavioral guidelines (naming conventions, mandatory steps), and commands are shortcuts that trigger skill sequences.

- **Cursor vs. Cowork:** Cursor is faster, indexes files with RAG retrieval, and provides file system visibility. Cowork is more abstract (no file browser) but supports parallel agents and better connectors (Ahrefs, Gmail, HubSpot, Notion, Semrush, Slack, Zapier).

- **GitHub for Knowledge Management:** Marcel demonstrated how the GrowthX handbook lives as a GitHub repo with Mintlify rendering, using MDX files with front matter for CMS-like control. Branching and pull requests manage concurrent edits.

- **Google Drive vs. Local Files:** Zena's team is a Google Drive shop. Marcel recommended GitHub as the collaboration layer, noting that Google Docs require API calls and format conversion that make AI integration "10 times harder."

---

## Key Topics

### Workshop Strategy and Product Protection

Marcel's CTO co-founder directly challenged him: "Why the hell are you doing this workshop? You're giving away all the R&D you've done." This set the frame for the conversation. Marcel acknowledged the tension and asked Zena to help figure out what level of detail to share.

- Zena validated that Marcel's approach is "very revolutionary" and ahead of what marketing influencers are posting on LinkedIn about skills files
- Zena independently suggested the system could be productized: "You could just turn it into a product that teams buy"
- Both agreed the workshop should share the high-level "101" without exposing proprietary implementation
- Zena's upcoming team session will serve as a test run for how to present the concepts to non-technical audiences

### AI-Powered Knowledge System

Marcel demonstrated the system live, showing how agents process and enrich meeting transcripts into a compounding knowledge graph.

- 600-700 historical transcripts from Fathom have been downloaded, converted, and enriched via agent scripts
- Each transcript generates/updates contact profiles with personal details, key quotes, career background, and relationship context
- Access controls are being built at five levels: executive-only, leadership, build team, all employees, and public
- Multiple concurrent Cowork sessions run in parallel to process and maintain the knowledge base
- Zena described it as "building your brain" and compared the complexity to studying neuroscience in medical school

### Skills, Rules, and Commands Framework

Zena came with prepared questions about how these three concepts differ. Marcel clarified with concrete examples from the system.

- **Skills** = core workflows or reusable task blocks (e.g., pull-meeting skill that has format-meeting and format-transcript scripts)
- **Rules** = persistent behavioral guidelines (e.g., "always follow this naming convention when creating a new file")
- **Commands** = shortcuts that trigger sequences of skills (e.g., `/pull-meeting` triggers confirmation then runs the pull-meeting skill)
- Commands are tool-specific: Cursor uses "commands," Claude uses the skills folder
- Marcel's recommended workflow for building skills: research, create knowledge, think through the approach, do it once, tweak, do it again, update the plan, then formalize as a skill

### Cursor vs. Cowork Comparison

Zena asked when to use each tool. Marcel provided a clear breakdown.

- **Cursor**: Faster, indexes all files with RAG retrieval, provides file system visibility, supports model switching, good for file-heavy editing work
- **Cowork (Claude)**: No file browser or path copying, but better connectors (Ahrefs, Gmail, HubSpot, Notion, Semrush, Slack, Zapier), supports parallel agents and agent teams, works well for broader tasks
- GrowthX just set up Claude Enterprise, enabling company-wide connector access
- Cost consideration: Cursor with premium models can run "thousands of dollars a month" -- Marcel and his CTO can expense it as R&D but recommended Zena limit usage

### Knowledge Folder and Research-to-Study-Guide Pipeline

Marcel demoed his research workflow for content quality scoring factors.

- Process: Write a prompt specifying research scope and scratch pad structure, run parallel agents, capture raw notes/sources/observations in three files, produce a tiered study guide, then create expert roles from the findings
- Study guides are written in Marcel's preferred format and automatically filed into the knowledge folder
- Knowledge docs serve as referenceable context for future agent sessions -- replacing vague instructions like "think like an SEO expert" with concrete, researched documents
- The process is self-improving: after tweaking outputs, Marcel updates the skill and rules so future runs incorporate the improvements

### GitHub for Team Knowledge Management

Zena's biggest question: how to keep local files in sync when her team lives in Google Drive.

- Marcel recommended starting with a shared GitHub repo for the marketing team's core context (estimated ~10 markdown files for a marketing team)
- GitHub provides branching, pull requests, and conflict detection for concurrent edits
- The GrowthX handbook runs on this model: MDX files with Mintlify rendering, version-controlled, with the entire CMS living in the repo
- Marcel demonstrated live conflict resolution on a pull request to show how simple it can be
- For data that updates in real time (e.g., conference registration pacing), Google Drive connections may still be warranted
- Marcel suggested Coda (which Zena's company uses) would be "miles better than Google Drive" for AI integration

---

## Action Items

**Marcel Santilli (GrowthX)**
- Clarify and simplify workshop content to share the high-level "101" without revealing proprietary system design
- Continue refining the study guide on skills, rules, and commands for non-technical audiences
- Improve skills folder visibility -- Zena couldn't find it due to dot-folder hidden file conventions
- Support Zena's marketing team in setting up a shared GitHub repo and establishing update processes
- Finalize access control layers (executive, leadership, build team, all employees, public) in the context repo

**Zena Dave**
- Send Marcel her document outlining agent, role, and skill distinctions with practical examples
- Prepare for and run AI session with her marketing team (team of 3) the next day
- Explore creating a shared GitHub repo for marketing team knowledge files with individual ownership and update cycles

---

## Transcript

**Marcel Santilli:** Yo, how's it going?

**Zena Dave:** Good, how are you?

**Marcel Santilli:** Good. It's been a heads down Monday, trying to reorganize my schedules. So it's like, yeah, like, Monday I had more meetings and so now it's like, trying to do -- we're trying to switch to like, make Mondays the no meetings days. Because a lot of the meetings I needed, I wanted to have on Monday. You know, Tuesday, less of a meetings day. People needed to prepare first. It's like, we can't do Monday. Monday's really hard. The team's getting like, really stressful. Okay, yeah, flip it a little bit.

**Zena Dave:** No, I get that. I wish I had just one day or even a half day of no meetings, but it's really hard.

**Marcel Santilli:** Hold on one second. Let me get more coffee. Yeah, yeah, you're good. All right. I did not look at your list.

**Zena Dave:** You're good. Thank you first of all, for jumping on with me.

**Marcel Santilli:** Yes. I took my internal team through a few things, kind of like, similar to what we did. Yeah, I didn't feel -- it was like, there's a lot of deer in the headlights looks, you know. So I gotta -- I still gotta figure out how to like, make this more approachable, you know. And then transparently, I'm trying to do it in a way, essentially -- like, my CTO co-founder was like, dude, like, what the f? Like, why the hell are you doing this workshop and doing this, it's like you're giving away, like, all the R&D you've done, you know. So trying to figure out like, you're safe, like, but for the workshop, it's like, how do I not give away -- agree.

**Zena Dave:** To be honest, like, I've been thinking non-stop since we met, and I feel like the way you're approaching this is like, very revolutionary. Like, I actually just saw someone post on LinkedIn today, like, one of those marketing influencers, and it was like, all these things I've done and like, how I've set up my, you know, skills files. And like, that's what the whole thing is about. It's like, skills files. And I'm like, oh, you're so elementary. Like, you're not thinking about, you know, like, agents and rules and, you know, how you're storing your files. Like, I don't think most people are aware of, like, a lot of what you have already put together. And I also think that what you put together, you could just turn it into a product that teams buy, you know? So, like, I do agree with your co-founder. Like, I feel very lucky that I've gotten to learn from you. And I'm like, I don't think you should, like, give this away.

**Marcel Santilli:** Help me figure out, by the workshop, what do I share?

**Zena Dave:** Yeah, for sure.

**Marcel Santilli:** Like, how do we share the -- like, so this exercise with your team could be useful of, like, how do we share, like, the 101, the very big picture, roughly? It's insane. Even just since our last meeting, it's just, like, absolutely insane now. Like, I had just -- just to give you an idea, like, we're trying to migrate from Fathom to Fireflies. I had an agent go through and write a script to download every single transcript of every single call that we ever had in Fathom. So it was like, six, seven hundred calls. And then, like, I'm having an agent go through and enrich every single transcript. And then as part of that, like, update a contacts MD file for every single person that's been on every single meeting, and then creating a meeting record of every single meeting that has ever happened. And it's just like, an insane mind map that is just so powerful. And I'm just like, I have, like, three or four Cowork sessions happening right now, and I'm just -- it's just like, oh, really good stuff. Like, you know.

**Zena Dave:** Well, I was actually talking to my partner about this last night because I was like -- I was literally talking about, like, what I've learned from you just in, you know, whatever, an hour. And I was like, basically, what this is, is you're building your brain. Like, you're building, like, multiple people's brains, I guess. And, like, it is science, because when you think about a human brain, it's like this thing connects to that thing, and if you turn that thing off, then that thing goes off. And like, understanding how all those pieces go together is why you go to medical school for seven years. Like, it's so crazy what this is empowering people to do. And so you can't really, like, price it like SaaS or, like, consumption, because you're just selling a brain. And so in a way, I was like, I feel as though you should sell this for just, like, whatever you think your brain is worth, which is probably $10 million. How else do you price something like this? I don't know.

**Marcel Santilli:** So I don't know how you would price it. But it's -- it's almost like the way I kind of think about it is like, we're trying to map out, using context engineering best practices as well as like just how agents work and some of the standards, right? Like with skills, rules, commands, like, whatever. Like, you're trying to map it. It's also a data pipeline exercise. It's also a knowledge graph exercise and it's also a -- how do you build rules and muscles and skills so that like it auto-maintains the project because it just rips, right? Everything just drifts. Like you add more things now every -- this thing over here is outdated. Like you give it a commit to like, hey, can you change the naming of this this way? Or like, can you add this thing this way? Like for instance, like today, this morning I was working on access controls, right? So I was trying to define -- let me share my screen really quickly. I was trying to define like access levels, I think. Let me try to find it here. Like, this is gnarly. There's so much here. But I'm not going to find it, but -- oh yeah, like this one was like syncing between my handbook and my like other project here. But then I was trying to figure out like, how do I create access for like the different layers? Oh, here it is. Access controls -- more so only me, the executive team, the extended leadership, the build team, all employees, or anyone. And then I started to use that in my repo because like, I don't want it to accidentally like pull a thing from my board deck or from my board memo. And so like, but then now that I have like -- it's insane. Like if you look at my transcripts, like, look at this. Every single month, like, look at this. Every single, like, you know, all the way to like, you know, you can click on any of these and you can see, you know, everything here enriched, ready. And then now there's these like context files on every single -- like if you look at records now there is contacts.

**Zena Dave:** Oh my God. These are all the people you talk to.

**Marcel Santilli:** Yeah, yeah. So like I can go here and be like, okay, this is what I've had so far on this person, right? Like, so crazy. So it's like starting to just kind of go through and the more meetings I have, it just like writes things down like this. So like, for instance, like this one is like a neighbor and also like a prospect right now. But it's like just the one that I use as the test. But you know, like, he mentioned things like how I met him and things like that. Key quotes. But then there's like hey -- he lives in the East Bay, you know, walking distance from Montclair. So his wife, his name is Katie, she grew up in Oakland, attended Bishop. His two sons, 13 and 15, they both went to Montclair Elementary. He's a Warriors fan. I gave him a ticket to go to the Warriors game on the 23rd with his wife. You know, he mentioned he saw them up close. Surprise Dubs win. Neighbors with Marcel. Like, career background, like, crazy.

**Zena Dave:** Like, it's like the new lead record.

**Marcel Santilli:** Like, but then, like, as this compounds, obviously there's going to be things here that might be a little bit like, kind of like on the personal side as well. Right. It's just like, oh, okay. I actually don't want to share this part with them, you know?

**Zena Dave:** Yeah, right, right, right. So you need -- you need to layer in, like, access control.

**Marcel Santilli:** Yeah, that makes sense.

**Zena Dave:** All right, well, maybe I can -- I hope, like, hopefully these questions help as you're thinking through, like, how you're structuring this. Also, I'll send you this doc I created, which, like, for me, one of the things I was struggling with when I was trying to read through your -- yeah, like, how should I -- like, how can I think about the difference between agents, roles and skills in, like, real world examples. So I feel like it can get a little confusing, like, how to apply, like, the definition of those things across, you know, various tasks that you need to do or workflows you're building. So I can send you what I put together in case it's helpful for, like, the beginner's guide. But these were the main questions I had for you, and I can zoom in a little bit. So, and this is just again, based on, like, going through your GitHub repo and then thinking about, like, okay, how would I actually start filling it in for our team? So, like, first one was commands. I wasn't actually sure. And actually, maybe I should pull up your GitHub too, just to look at it side by side.

**Marcel Santilli:** Okay, so let me do this. Let's try this out so we can do a live -- incredible screen. I have your questions bookmarked already, so. No, I'm good. Beautiful, beautiful. New task. And this -- help me write a quick answer to these questions in relation to how to think about these things in first principles, as well as in relation to kind of how this project is set up. This directory, this -- and then what I'm going to do is also --

**Zena Dave:** Is this Cowork, by the way?

**Marcel Santilli:** Oh, yeah, yes. Cowork. Yeah. Kind of find where my -- I had done another -- okay, I'll just let this one run really quickly and then there is another one that -- gosh, I need to find a better way to like, keep -- like when I need to find -- you know, it's mostly when I'm showing other people because I can always -- anyone -- but that makes sense. Because I had done a study guide on like how skills work. Yeah, there you go. Okay. It was this. I think so when you texted me or whatever -- I just set this to run earlier and it was just kind of like, hey, create a research study guide on this. I'm trying to teach others how to replicate what we've done here because it's working amazing. The problem is that blah, blah, blah -- is that the study guide will explain all the building blocks and how to connect them. So I just kind of like the shitty prompt.

**Zena Dave:** Yeah.

**Marcel Santilli:** So it kind of explains things. It probably needs to be distilled down a little bit more. You know, it's like having a billion-dollar assistant who gets amnesia every morning. System describing problem -- instead of starting from zero every time. A good reference.

**Zena Dave:** Yeah, I love that. Oh, that's good. It's like the smartest person on earth who wakes up every morning not knowing anything.

**Marcel Santilli:** Yeah. To be like -- said ChatGPT should be Amnesia GPT or something.

**Zena Dave:** Literally.

**Marcel Santilli:** Okay, so the core insight -- context is the product, quality of your AI output -- the terms, blah blah, two mental models and then it starts -- like there's like these layers. Maybe they help understand.

**Zena Dave:** Yeah.

**Marcel Santilli:** README -- this is the map that tells the AI where to find things. Context -- this is the knowledge the AI draws from. Skills and rules -- these are the books and policies, you know, and then tools -- these are the hands that do the work, if you will.

**Zena Dave:** Yeah, that makes total sense. That's a great way to think about it.

**Marcel Santilli:** And then I had to kind of create a mini glossary of things for people, you know. And then like explain some of the things you mentioned. Like skills.

**Zena Dave:** Yep.

**Marcel Santilli:** Rules. So rules are more like -- think of rules as like persistent behavioral guidelines. So it's like anything, make sure this happens. And these are mostly like -- yeah, like just like if you're creating a new file, always follow this naming convention. Right. And then commands are like push and commit or pull a meeting or you know, it's like a set of behaviors that will follow skills and rules or will follow like a playbook. It's kind of like a workflow, if you will.

**Zena Dave:** The rules, that makes sense to me. Totally. But the commands piece, I think maybe still feels like, what would be the difference between a command and just like an agent? Or maybe -- maybe like it could be like a pull meeting.

**Marcel Santilli:** Right. Like, it's kind of like a command and then -- and then interview with --

**Zena Dave:** Oh, so these are like shortcuts.

**Marcel Santilli:** Yeah. Like, Tony -- is trying to remember this guy. Interview Tony. And so, so that's like, oh, I see.

**Zena Dave:** Okay.

**Marcel Santilli:** Triggers a bunch of things to happen or a sequence of things to happen in a certain way. And then those things could also be skills inside of them as well. Right. Like, so skill can be more like a block that can be used in a lot of different ways. Where command is like trigger a workflow to run. Right. Or set of things to happen. Right. See this, I asked it to always ask me to confirm before pulling the meeting. And so it confirms this. It's like, yes.

**Zena Dave:** Would you say, like, for example, I don't know, write a LinkedIn post -- would that be a command? Or would that be too big of a thing to put into a command?

**Marcel Santilli:** Like, the way I would approach it is like, do the research, create the knowledge you need to do a good job on that thing for yourself and then use that knowledge. Then help you think through how to do the thing, the work product, and then have it create a plan on how to do it. Then have it do it one time. Then you tweak it and improve it. Then once you do it one time, now have it do it a second time and then improve it, update the plan that you created to begin with, which is like, are you going to replicate this? And then validated that. Okay, now can you turn this into a skill? And then a command would be like a way to trigger that skill that then maybe adds a few more things to it, more than that skill. Right. Which in this case the skill is like pull meeting. Like, the skill here is like the actual, like, way that it -- like where is it? Like, it pulls the meeting. But it's -- yeah, it's like -- and you see it has these scripts, format meeting, format transcript. And then the skill is like this, you know. And then, so there's a lot of overlap, but then there might be some more like, formal ones or like bigger ones that actually have like multiple skills inside of them. And so it's like pulling together a bunch of skills, you know, but it can also be, use this command so I can trigger this skill faster, you know, like, forward slash, do it like, okay, cool. Now I don't have to type like, hey, use that skill that does blah, blah, blah, you know.

**Zena Dave:** Totally. Yes, yes. This makes perfect sense. Okay, cool. I love it. Okay, so that's a Claude command. But then the --

**Marcel Santilli:** Yeah, okay. Actually that makes perfect sense. I think that answers number one, actually.

**Zena Dave:** And so you just name it. You would name it and -- but then you would give it a guide for, like, what to pull. It's basically just another markdown file.

**Marcel Santilli:** Yeah. Okay, cool. Yeah, so it's like commands are, by the way, for, like, Cursor. And then like, you have like, skills folder, you know, in Claude. So it's kind of like --

**Zena Dave:** I see. So the commands are more so for like, whatever tool you're using to run.

**Marcel Santilli:** Yeah. So like in Claude, commands are like, almost like shortcuts. They're just shortcuts. That's it. Just think of commands as shortcuts. Yeah, yeah. Skills is like the core thing, you know. Skills are workflows, essentially, you know?

**Zena Dave:** Yep. Okay, cool. That makes perfect sense. So then I guess that's a good lead then into the second piece. This felt like maybe a little unclear, is like when we were going through this -- and maybe this will help with your workshop -- but, like, when would you use Cursor versus just Claude? And is it based on your preference or do you really have a strong POV on, like, you should be using Cursor because it's way more efficient for XYZ thing?

**Marcel Santilli:** So the main thing with Cursor is that it is way faster. Way faster spending money.

**Zena Dave:** Cool.

**Marcel Santilli:** Fundamentally, it's just a different harness that works differently. Cursor does a good job of it -- it indexes all your files. It has RAG retrieval, essentially. Think of it as it's trying to index everything in your files in your directory and trying to create some semantic understanding of it. Then on top of that, we also are creating this scaffolding for this whole project that will make sure, like, no matter what, like, agents know what to do better. You know, that's more opinionated and, like, more rigid on, like, this is where to go for what. Whereas, like, Claude Code does, like, searching in your repo. Right. Like, so it's like doing like, a bunch of different searches in your file system to go like batch a bunch of files and then read through those files or understand those files. Right. Or understand parts of those files. Right. So it's like doing that on the spot with everything. It just like, it works incredibly well because the models got so much better. But it's not going to be as fast. But to make up for that, like, Cowork and others now have parallel agents and agent teams. So then, like, it makes up for some of that speed. But like, if you truly need to do something, like, super fast, Cursor's probably going to be a lot faster. But then at the same time, now there's like all of these like connectors that just work way, way better. And also, like, I just set up Claude Enterprise for our company, so now I have like, all these things that I'm enabling for, like, connectors, you know, for everybody. So, so for instance, like Ahrefs, Gmail, HubSpot, Notion, Semrush, Slack, Zapier, like, you know, like these are -- there's just like so many connectors you can enable, you know?

**Zena Dave:** Yeah, yeah. So it's like -- would you say, like, Cowork is somewhat comparable to Cursor then?

**Marcel Santilli:** I don't know. Yes, but like, you don't have the visibility in Cowork. Right. Like, so Cowork, for example, like, there's no way to know what's in your file system. Like, you -- okay, but it's like, have to like, open up that folder and look at this and go, oh, okay, I see. And then like, let's say you want to reference a file here. You would have -- oh, actually, like, you know, like, there's no like, copy path here, you know. And so it becomes a lot harder to kind of manage file system. But also, like, Cursor is just like a nice UI. And then you just open up, like, Claude Code here. And then it's just like you're here, you know, and then now it's like you can ask it anything you want, you know?

**Zena Dave:** Yeah, a hundred percent.

**Marcel Santilli:** Yeah. Like, organize the whole repo or something. You can do it in Cowork. I did it today. But like, you won't see the files and then you can't like, reference the files here and you know, like, and forward slash something. And it's like, you know, so it's a little bit more of like local, you know, or it's more based -- it's more like an editor for your files. Whereas, like, Cowork is more like an extra layer of abstraction that you're not going to see all your files here side by side. You're not going to open a bunch of tabs of the files. It's just like, just a different interface, you know?

**Zena Dave:** Yeah, no, this makes perfect sense. Okay, cool. Should I just roll through the rest of these?

**Marcel Santilli:** Yeah. Okay, cool.

**Zena Dave:** Then next one is the skills file. I think in your context OS GitHub is empty. Is that just because, like, you're encouraging people to enter their own files in, or do you have, like, a template for how you, like, recommend building skills?

**Marcel Santilli:** I realize it's empty, but what else I think it is?

**Zena Dave:** At least let me -- it's empty in your computer. But that's because, like, any file that has a dot in it is meant to be hidden on your computer.

**Marcel Santilli:** A dev thing. I didn't know that either, so don't feel bad. So like, .env is like environment file. That's like all your keys and stuff, for example. Right. And so these files over here, they're like .agents, .claude, .cursor, skills -- they're like, if you drag and drop them into Cursor or VS Code, you would see them. But then if you go into, like, your Finder, like, you don't see a dot, any of that here.

**Zena Dave:** Got it. Yep, makes sense. But that's, like, intentional because there's like, all these -- they're not meant to be things you see in your normal, like, Finder.

**Marcel Santilli:** Yeah, sure.

**Zena Dave:** Is that just like the access control piece?

**Marcel Santilli:** There's just like a global setting for operating systems, essentially, you know.

**Zena Dave:** Okay, okay, got it. So your skills files then, like your markdown files for all the skills that you've built, they should be there.

**Marcel Santilli:** Like, if you go to the repo --

**Zena Dave:** I might just be opening it wrong, to be honest.

**Marcel Santilli:** Yeah, so if you go here, you see they're here. Skills. Yeah. Oh, this one's linked to -- yeah, no, it's like it's linking to the Cursor version of it, not the --

**Zena Dave:** Oh, okay. Okay. And you can -- it's symlinked to it because they're similar, but you can also have it --

**Marcel Santilli:** Oh, I do have a skill template. It's right there. Okay.

**Zena Dave:** Yeah. But, yeah, it's okay. It's not great. It's like -- it's not --

**Marcel Santilli:** That's okay. That answers my question then. I was just wondering, like, should I -- am I downloading this wrong or whatever. So, yeah, I have the file naming, push, commit, research to study guide and writing content. So it's just in the Cursor folder. That's the answer.

**Zena Dave:** Okay, cool. That's super helpful. But if it's helpful for you, if you want to put that into the skills folder --

**Marcel Santilli:** Yeah, now I have both. I need to figure out, like, this was like my first attempt at turning into a starter kit, but I haven't spent any cycles on like, you know, how do I make the setup a little bit easier, you know?

**Zena Dave:** Yeah, well, I mean, I'd say it's like 95% of the way there. Okay, cool. That is an easy one then. Okay, the next one is -- when you're loading an agent in Cursor or Claude, whatever, do you have to say, like, load this agent and this role and this skill? Or can you just say like, is that what the markdown -- is that with the like, whatever MD --

**Marcel Santilli:** Or if you want to be specific. I haven't been doing the role stuff much, to be honest. So, like, we're trying to like redo, for instance, like some of our scoring inside of our product. Right. And so I had done a ton of research on like, quality, like content quality factors that impact SEO and AEO and a bunch of other stuff. And so like, this is the prompt I wrote. Okay, but you see, like, it loaded the CMO role, so --

**Zena Dave:** Interesting. Yeah, okay, it loaded a bunch of stuff in your starter kit. For example, you're not necessarily being super prescriptive and saying like -- I think best practices is to not be very prescriptive in that way all the time. But maybe if what Claude spits out is not to your liking, then you might like, be more prescriptive.

**Marcel Santilli:** Yeah, but like, what I'm usually more prescriptive on is like the thought process I wanted to go through. Like, I wanted to write three scratchpads, so I'm like, hey, launch several parallel agents to do this faster. Be very -- I just wanted to reinforce, be very biased towards 2026 or 2025, you know, like, look at these types of things. I want you to look at what the engines say, like, not just like a bunch of random sources. And then for the scratchpad notes, write everything along the way in the following scratchpads for each -- raw notes, observations, etc. Raw top sources and people, raw research stats, quotes and observations. Between these three raw files should be able to run further analysis without needing to redo the entire research. I just literally type this, right? Then we -- the research and final study guide. The final study guide should include three tiers of factors as well based on the importance. Blah, blah, blah. Like this is like how I'm thinking about it already, you know. And I was like, hey, link to the sources everywhere to make it easier to click and read more because sometimes it will, like, cite it later or not do it. And then after all of that, create three expert roles for each topic and one decider role to come up with a methodology for scoring content quality, blah, blah, blah. And then these are all the outputs from this. So it has, like, all the raw -- so, for instance, like, this is the raw that I found, like, and, you know, pretty good. It's always written in my way, you know, so it's like, I can still, like, read it because it's, like, formatted how I like already, you know. And then, like, all of these, you see, like, here's the sources it's writing down, you know, why it's good or not, what sources it's going to use. So then I can go back and be like, oh, these are the sources you ended up using, you know.

**Zena Dave:** Got it. You know, you're telling it, like, document each --

**Marcel Santilli:** Yeah. Document your process along the way so I don't lose it so I can, like, rerun it later, you know. And then -- yeah, so it has, like, raw notes as well. You see, like -- yeah, yeah. Getting along the way. Key observations and patterns, you know. And then this is the study guide. And so then the study guide is written the way all my study guides are written, you know, like. And, you know, I asked for the three tiers, and then each tier, it's telling you, like, what's important, you know?

**Zena Dave:** Yeah. Gain factor two, factor three, semantic completeness, you know, like factor five, whatever. It's going through all the factors you researched, you know. No, this is great.

**Marcel Santilli:** And then it's creating, like, an expert on each one of these study guides, essentially from it.

**Zena Dave:** And then you would theoretically use those experts as roles moving forward.

**Marcel Santilli:** Yeah. And then here I was just like, cool, now let's just, like, write a consolidated doc on all those things with, like, our framework for content quality, which has so much of my stuff already in it. Right. So it's not just like, I'm defaulting, like, my product thinking to this. This is more like, there's this specific thing. The engineers are, like, a couple days away from starting to build this stuff. And my CTO was like, hey, can you look at how I'm thinking about this and make sure, like, it follows. And so this is like, what I built.

**Zena Dave:** Like, wow. Yeah.

**Marcel Santilli:** And then once this is done, how do you then interact with putting this into your file system?

**Zena Dave:** It's already doing that. So it's already going into, like, my knowledge folder.

**Marcel Santilli:** Yeah.

**Zena Dave:** How does it know what to put in your knowledge folder versus not? Or is that like part of your markdown?

**Marcel Santilli:** It should be in the rules already or it should be in the instructions for like the research-to-study-guide.

**Zena Dave:** Okay, so anytime you run like a research-to-study-guide, but you can just tell it. Yeah, sure. You just say create this as a file.

**Marcel Santilli:** Hey, anytime I do this, I want it to go here. Where should this instruction live?

**Zena Dave:** Okay. Yeah, cool. It's so funny. It's like the answer is always just ask.

**Marcel Santilli:** Yeah, exactly. Just ask and make it your own. Like, if it doesn't make sense, put it somewhere else, you know, like. And then normally what I would do is like take something like this and then I would process it further into our handbook. Right. And the handbook is what's available to the whole company.

**Zena Dave:** Got it, got it, got it, got it. Okay, cool.

**Marcel Santilli:** This one was a study guide on like, LLM writing essentially, like mastering LLM writing based on like all the findings, all the best practices currently, you know, to not generate AI slop, you know.

**Zena Dave:** Yeah.

**Marcel Santilli:** Then this is turned into like a doc, you know.

**Zena Dave:** Yes. It's super cool. Yeah, this is excellent. Like, so because like you have it -- you're using Mintlify and then Mintlify has like a doc writing skill and also a skill that has all the components that are available in Mintlify. And then you ask it to also create Mermaid graphs as this, you know. And then like, then later on you can take like -- this is a fun one. You're going to get a kick out of it. Take the Mermaid graphs and create a -- and then I think it says use, like, I have a scope for this and then let me switch to Gemini Pro because I'm trying to use -- but I think you'll get a kick out of this one. It might take a minute so we can keep going, but I'm excited to see the outcome.

**Marcel Santilli:** Okay, this is super helpful.

**Zena Dave:** Okay. All right. Well, while it's loading, I'll ask you the next one. So for the agent docs that you have -- agent docs folder, I assume these are just kind of like samples to get started with. But I'm curious if you feel like there is like a finite -- I don't know, maybe not finite, but like, if you think there's a good way to think about all the agent docs you might want to create or if there's any like, framework for how to think about when you need to create another agent doc versus when you probably have like 95% of what you need.

**Marcel Santilli:** For example, like, docs overall you're talking about, right?

**Zena Dave:** I'm referring to your -- you have like, the agent docs folder in your GitHub repo. Yeah, maybe it's that one. I just see it's named agent-docs.

**Marcel Santilli:** Hold on, let me find which one you're talking about. Where is it?

**Zena Dave:** Yeah, that one.

**Marcel Santilli:** Yeah. Like, this was like the docs I had -- or these were like, ways to adapt all the knowledge I had and all the stuff I had into things that could be used. Whereas, like, some of these things are like -- or like knowledge files that then got decomposed down to, like, you know, this. So, like, I don't think you need this too much. It was more like -- yeah, like, it feels more like instruction for agents that, like, I don't think I have this here. So it was more like turning some of the ways I had set up this because, like, what I did was essentially have an agent figure out, like, how to turn my entire repo into, like, a starter kit.

**Zena Dave:** Like, but look at this. Oh, my God. Yeah. So I had to see -- this is super cool.

**Marcel Santilli:** And then it, like, takes the Mermaid graphs and writes it in the style. It's not perfect, but it's just like --

**Zena Dave:** Oh, this is super cool.

**Marcel Santilli:** What's possible, you know, like, crazy. Creating, improving on a loop in this field, you know. But it's using Napkin AI with like, our colors or kind of how I wanted it to look.

**Zena Dave:** Yeah. And that's part of this, like, really hard to get it consistent, you know, like. And it's able to do this consistently because you have that, like, Mermaid-to-graphic skill.

**Marcel Santilli:** Yeah. Like, look at this. The Science of Engagement. Like, insane. Like, it tells you something. Right? Like, it's like, okay, so it could be like, take that and make it more detailed with more context. Anyways, so you can see how it's possible. Because, like -- and that's one thing with Cursor, like, you can switch it to a different model.

**Zena Dave:** Yeah, totally. So that's helpful. You know, you can't do that in Claude Code. Right, right, right, right. But that's not worth thousands of dollars a month for someone.

**Marcel Santilli:** Yeah, well, that's because, like, the CEO and I can expense it and, you know, it's R&D. But yeah, like, I would limit your usage of this, you know.

**Zena Dave:** Yeah. 100%. We'll get flagged. Okay, that makes sense about agents then. And then -- I was trying to think about how to -- sorry, there's only two more questions, I promise. I was trying to conceptualize like how to think about the knowledge folder. And maybe this is the same answer about the agents folder, but there's like, I guess, would you just consider this sort of like the knowledge base, like your product marketing docs and I don't know, sales stages, you know, as like --

**Marcel Santilli:** I always think about it is I think of docs as like context and knowledge as context with instruction based on like real experience kind of thing. You know, like -- you can tell an agent, think like an SEO expert. What the fuck? I mean, nothing, right? Like, you can generate a really good description of an SEO role. Okay. But you can also just have it research a specific topic on like, for instance, like context engineering. Right. And then anytime you like, you want to reference the best practice or the topic of context engineering instead of you saying, hey, by the way, follow best practices of context engineering -- like, what does that really mean? So instead what I've done is I create the process to research, the process to write it in a study guide in a way I can also learn. And then process those study guides into like a knowledge document that's even better formatted and more distilled. And then that becomes like a knowledge reference for agents or anything you're doing. Right. So then in the future I'm like, I don't have to tell it like, hey, think like an SEO expert. I'm like, no, I have this doc that literally says like, what are the ranking factors that matter the most for SEO? And I'm like, I just want you to reference that now. Right, but -- and then your roles can then reference those things and not have to carry so much weight of like the knowledge of what that role needs to know, you know?

**Zena Dave:** Totally. That makes so much sense. You're activating nodes, you know, in a neural network of like this agent's -- it's almost like you want to shine a light in the right ballparks, you know, hey, go here, go here, go here, go here within this file cabinet system or whatever, you know, and here's the lens you're going to use. That's so smart. That makes --

**Marcel Santilli:** So it's because you're basically like, you're going to get a way better output the more deconstructed it is, it seems. So like, even if you could deconstruct this even more, like, you probably have an even better outcome.

**Zena Dave:** Yeah, that makes sense.

**Marcel Santilli:** So the knowledge base -- cost prohibitive. Also the models are getting so good. You also don't want to over-decompose. But if something is important enough for the work you're doing, like you should just go do a research guide on something, you know, like. And now I'm just doing research guides on everything. And it's just like, why would I run a Perplexity research and then copy and paste the output one time? I'm just like, run it and then it runs and it updates my sources. It updates everything. It puts it in the right folders. It does all the things. It knows me better. Right. It has the context of my company. It adapts already. Yeah, it's all there. All the traces are there. The transcript of how it thinks is there. I can use it again, right? And then if I ever need to tweak it, I can say, okay, now see how I tweaked this -- now update my skill and update all the rules. The next time I do this again, like, you do what I just did.

**Zena Dave:** Got it. Right. It compounds a lot more, you know.

**Marcel Santilli:** 100%. No, that makes sense.

**Zena Dave:** Okay. I love it. All right, last question then. Which is maybe the biggest one that I'm like, help. So as I told you, we are a Google Drive shop and a lot of people right now I think are leveraging Claude by saying, hey, connect to Google Drive and read all this unstructured stuff. And you know, they're probably not going to like what they get out. Because I think you've totally sold me on the local file storage system. So the issue is like people will make updates to docs or things in Google Docs or sheets or whatever, but obviously it's unrealistic to expect that they're going to download it every time and update it. And so I'm curious how you think about keeping your local files up to date. I think you showed me the version control stuff maybe, but for a team that's updating things all the time, like this feels like maybe the biggest blocker to the local file storage concept.

**Marcel Santilli:** Yeah. So like for instance, like right now the reason I built the handbook is because like I wanted to have one single place that is not my entire context files that has way too much -- that everyone is using. That now, like our chief customer officer is using now. Like everybody just like started using and now it's like the latest and greatest are always there. And now my co-founder is using it as well and then updating and pushing changes to it and now I can pull the changes. Right. Like so, it's just like, you know, it just works. Yeah. So but if your team is not quite there, I would just do it for yourself first and -- or if your team is all doing it, then great. But it's like it's going to be a little tricky. So one option is can you have a GitHub repo that has like the equivalent of like your shared context with your team? And like, I know it might be tricky too, but it could literally just be like your own GitHub repo, you know, and it's just like, hey team, this is like what we're using for testing. You know, don't make it too official. Just be like, hey, it's like our shared context whatever. Right. If that's too risky or you can't do that, then you can still do it for yourself.

**Zena Dave:** Yeah.

**Marcel Santilli:** And then it just becomes like where do you push it live? Google Docs are just like not -- it can be exported to a file, but it's like it's very black-boxy, you know. You just are not going to be able to move through it as fast at all. Even with the connectors. You're going to do an API call, it's going to download the file, it's going to have to like then convert the file into something that's more readable or try to read it in that way. It's just going to be like 10 times harder and worse.

**Zena Dave:** Yeah.

**Marcel Santilli:** For you like -- also docs are changing, but they're not changing in real time. And in your context for your company and your team -- crazy, like talking after everything I've done, it's maybe like, let me see how many files I have here in this context. But it's not that many. It's like -- this is a company, it's not just marketing. Right. Like talking like 50 MD files. Like you know, like you're -- as context for your entire company. So for a marketing team could be like 10. Those 10 are really like the gold standard. That everyone can at least have that, you know.

**Zena Dave:** Totally. For everything they do, anywhere they do it. You know, I guess then for -- this makes sense. I think like a lot of the context doesn't change all the time and you're not updating, you know, some of these like knowledge base files or skills files or whatever in real time. And if you are and if you're the owner of that skills file, then when you do make an update, like, commit that as a change to our shared GitHub repo. So like everyone has the latest and greatest. Maybe though, like, for example, we will have like a Google Sheet that tracks pacing toward a reg target for a conference we're running. And that's updating in real time. Right. So like, maybe certain files warrant having like a Google Drive connection.

**Marcel Santilli:** Yeah. Like right now, does your team in the company not have like a wiki or any, like, knowledge sharing, like, note taker, Confluence, Notion, anything?

**Zena Dave:** Yeah, we have like, Coda.

**Marcel Santilli:** Okay. So like, even Coda would be like miles better than Google Drive to do this.

**Zena Dave:** Really?

**Marcel Santilli:** Yeah. The only challenge with like, larger organizations with things like that is if, like, they lock it down and there's no integrations with anything. And this is like, anything you need, you need to ask permission, you know, like. Yeah, because it's like, I'm barely using Notion now because of this. Because it's just like so much more work. And then if the MCP integration fails all the time to update a doc, and then it's not really markdown. It can be exported as markdown, but it's not really markdown. So it's like the formatting gets off. The keeping in sync is awful. So that's why I'm like, going to be in doc site. Like, that's it.

**Zena Dave:** Can you edit your markdown file in GitHub so you don't have to like, download it, edit it, load it back in?

**Marcel Santilli:** Yeah, like, these are all legit markdown files. The repo is downloaded and all it is is that in that repo I'm using Mintlify, but they're what's called .mdx. So it's markdown with like a front matter. And the front matter is like essentially like publish and control. It's like the CMS matter. It's like a couple of things at the beginning of the doc that determine if they're like, you know, published or not. Right. Like, so if you look, the handbook looks like this, but then the repo for the handbook is literally what's in my workspace next to my context repo.

**Zena Dave:** Yeah.

**Marcel Santilli:** Like, it has all the things here and then all it does is like anywhere where there's, like, How We Work, for example, these are all MDX files. And then it looks like markdown, it is markdown. The only difference it has is like this, you know, like, just there's a couple of things which is just this front matter, you know. And then every -- but that's all it is. And then there's like, things like -- and other things are just how components get rendered in the handbook. But you can see it's just like text, like very well formatted text. And it renders like rich text because it's markdown.  And so everything here is just markdown. And so you technically don't even need a site for this. People can just literally go in here and just like click here and be like, oh, okay, cool. Mental models. Okay, awesome. Cool. First principles thinking, oh, let me read this. This is awesome. And you can really like share this, you know.

**Zena Dave:** MDX is just like a readable -- like you can read it like a web page, basically.

**Marcel Santilli:** It's just the standard that a lot of doc sites use to -- like a CMS. Like, so this replaces the CMS. It's essentially -- it's like replaces the CMS.

**Zena Dave:** I see. Okay. It's markdown, but then it has like front matter, which is just like at the beginning it has these like, essentially this and then fields in your CMS essentially, you know.

**Marcel Santilli:** I see. Okay, cool. And then the handbook also has like a couple of other things that are just like -- gosh, where is it? There's like things for Mintlify to ignore. There is like this, which is like the navigation, you know.

**Zena Dave:** Interesting. So this repo is for your handbook, and your handbook is just the repo.

**Marcel Santilli:** Yeah, yeah, exactly. Like so -- and it uses Mintlify so that it looks pretty and I don't have to hire a dev. It's just literally like -- and then if I want to change anything, like the style or anything, I just ask my agent, like, change it, you know. But it's like this is literally a website. It's like a website essentially, but with the core of the website -- the whole CMS is here, the content is here, versus like being a blank thing that then has to ping an API to pull the content off the CMS.

**Zena Dave:** I totally got it. Okay. Yeah, that makes perfect sense. Oh, this is so cool. Yeah, I love it. Okay, so you like -- I'm thinking about basically creating a shared GitHub repo for our little marketing team where we all commit to it and we, you know, maybe we each own a certain part of it or whatever. And like, we are responsible for keeping that thing up to date. But you still run this locally for your Claude, right? Meaning you just download it ever so often and keep your files updated.

**Marcel Santilli:** Yeah, it kind of does that somewhat automatically. And so then there's like different branches and then if people are working on those branches, you know.

**Zena Dave:** Oh, so you would create a branch to like, make major updates on their local --

**Marcel Santilli:** Yeah, it's like you're essentially creating a branch and you're doing a bunch of stuff. And then once you're done doing a bunch of stuff, you do a pull request, which is just essentially a request to like, merge back to main. And then if there's conflicts, it will get flagged here automatically. Like, but honestly, like, this stuff, there's not that much -- there's not that many dependencies. Like, it's literally like the dependencies happen where it's just like, for instance, like I was running this, my Claude app on my phone and the Claude app on your phone. It does a pull request, right. And so it creates a branch, does all the work, and then does a pull request. Right. So these are all Claude branches. Right. And then like, you can see it's like two behind, you know, and so now it's like, if I click on here, I think it can create essentially a pull request to merge that. It will say what it was. This was literally a remote session. But then it might say, hey, this has a conflict because one of the files it's asking to update, actually the main has a different version of that file. It's like resolve conflict. Right. And so now you're just like, hey, like, okay, how do I accept both changes?

**Zena Dave:** The conflict is just like, your update doesn't match the current one.

**Marcel Santilli:** Yeah, yeah. Your update is either going to need to replace something that's now further ahead, or you're going to need to merge both and resolve it. But it's all a file system, right? Like, and all this is, is that it's like trying to insert a new thing, right? Which essentially moves this link here to here. And then like, it's trying to add this here. You see, like, this is the thing that I added.

**Zena Dave:** Yeah.

**Marcel Santilli:** And then before that, these things weren't there. So now it's like, accept both changes. Okay, cool. Like, now, like, that's it. Like conflict mark as resolved. Like, that's it done, like, you know, and now it's merged. Like this thing. And now like, no conflicts, blah, blah, blah. And like, and then that's it. Confirm.

**Zena Dave:** So you would have theoretically, like, everyone could be allowed to accept a pull request. Like, there's no point in centralizing that.

**Marcel Santilli:** I wouldn't worry too much about it. But it's essentially like, that's how, you know, engineers manage, like, complex code bases. You have like a hundred thousand files and, you know, a million dependencies on everything. You can't just like modify the files. Like you have like a ton of different -- like, you know, like for instance, like, just if you look at one of our -- just use one of our repos, like I'll pull up right now one of our products. If you look at like these are all the 11 branches active right now. You know, and that means that someone's making an -- then I can pull this branch as well in case I want to see what they're doing locally. And then these are like the pull requests right now, you know.

**Zena Dave:** That's so cool. So basically you would say like, hey, if you want to make an edit, like an update to something -- you see bots that run, you know, that then check a bunch of things, you know, like the packages have installed. Like, you know, like there's a bunch of things that run and it's like, okay, cool. And it passed everything now and then. Like, anyways, the stuff is over my head too. But you know, and then there's rules to like, you have to get at least one reviewer, you know.

**Marcel Santilli:** Yeah, that makes sense.

**Zena Dave:** So there's things you can set at that level. Super, super, super cool. It makes so much sense. Like, pull request, you can see exactly what changed, right? What files and how it changed. You see like, like that's it.

**Marcel Santilli:** When you're downloading the updated file system, does that whole request history exist locally too, or --

**Zena Dave:** No, it's not. It's not relevant. But you can say, hey, pull this branch or rebase it on this other branch and then it will like swap out. You know, if you're ever nervous, just like, create a new folder on your computer that's just called backup. And then like copy and paste that entire directory into that directory and then name it as backup. Put the date, dash, whatever date. And then you have it like it's locally. It's there just so that, like, that's what I did one time when I was going to do like a major refactor. I was like, I don't know what's going to happen.

**Marcel Santilli:** Yeah, yeah.

**Zena Dave:** So you're good. That makes perfect sense. This is so helpful. I'm so excited. I mean, yeah, I'll be up all night working on building this for our little AI session tomorrow. So I'll let you know how it goes. We're -- I mean, we're a team of three. So like, it's not going to be anything insane. But I'll let you know, like how it's -- how it's --

**Marcel Santilli:** Yeah, that'd be helpful. This gives me a couple of things for me to go focus on, you know, to make it a little bit easier.

**Zena Dave:** It's absolutely excellent. So my free Google plan is going to cut us off, but perfect timing. We're already at time. I so appreciate you.

**Marcel Santilli:** Yeah.
