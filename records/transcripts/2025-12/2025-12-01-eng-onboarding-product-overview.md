# Eng. Onboarding + Product Overview

<metadata>
date: 2025-12-01
time: 20:01 UTC
duration: 80 minutes
organizer: daniel@growthxlabs.com
participants: Daniel Lopes, Isaac Dudek, Sergey Kaplich, Tamy Macedo
fathom_recording_id: 105354340
fathom_url: https://fathom.video/calls/491827195
share_url: https://fathom.video/share/4M3r8H_zkB4sXuJpYio8itiMwb5KvQbs
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Daniel Lopes onboarded new engineers (Isaac Dudek, Sergey Kaplich, and Tamy Macedo) on GrowthX's product architecture, team structure, and operational processes. The session covered the three-layer platform strategy (Output framework, vertical interfaces like ContentOS and Check.ai, and a future human-in-the-loop marketplace), the planned migration from the monolithic Flow repo to dedicated product repos, and essential team tools (Slack channel structure, Linear project management, and Geekbot for async standup). All new engineers will spend 1–2 weeks on the Client Ops team before moving to their assigned product lanes to understand the service-to-platform model and customer-facing operations.

---

## Context

GrowthX is a one-year-old company built on a service-to-platform model. The company started by manually delivering AI-powered content marketing services while simultaneously building a scalable platform. Three new engineers (Isaac, Sergey, and Tamy) recently joined the team and needed a comprehensive onboarding to understand the company's technical architecture, product roadmap, and operational culture. Daniel Lopes, the engineering leader, structured the onboarding to walk through the company's evolution from pure services to a multi-product platform, explain the organizational team structure (divided into Client Ops, AI Framework, and Product lanes), and introduce the async-first communication practices (Slack, Linear, and Geekbot) that keep the distributed team coordinated without excessive meetings.

---

## Relevance

To GrowthX Delivery:
- New engineers (Isaac, Sergey, Tamy) now understand the Client Ops onboarding path and will spend 1–2 weeks embedded with the Client Ops team before moving to product lanes. This informs client handoff and training sequences.
- Slack channel structure (B- and D- prefixes) and Linear organization now documented for consistency across client-facing tickets and project coordination.
- Geekbot async standup discipline is now a known team expectation for all engineers, critical for Daniel's Claude-based leadership reporting.

To CheckThat:
- Check.ai architecture, roadmap, and the feature-build demo video have been explained. Isaac will connect with Daniel mid-week to dive into Check.ai workflows and contribute to an ML research study.
- The three-layer platform stack (Output framework, vertical interfaces, human-in-the-loop marketplace) directly supports Check.ai's development as a standalone public index and private tracker product.
- Public Index and Private Tracker features of Check.ai are being soft-launched in December 2025, with announcement planned for January 2026.

To GrowthX Business Development:
- Product roadmap now clear to new engineers: ContentOS (fka Atlas) soft-launch planned for December 2025, Check.ai for January 2026, and an undisclosed larger product planned for February 2026 with major marketing push.
- Company philosophy (service-to-platform model, custom enterprise work like Lovable and Augment Code) established for long-term planning and client positioning.
- Team structure and capacity planning now visible: Client Ops team (Kirkland lead), AI Framework team (building Output), and Product lane (Check.ai and ContentOS teams).

---

## Overview

- **Onboarding Path:** New engineers will spend 1–2 weeks on the Client Ops team to learn the service model before moving to product lanes (AI Framework, ContentOS, Check.ai).
- **Product Strategy:** A three-layer stack is being built: an open-source AI Workflow Engine (Output) for code-first development, vertical interfaces (ContentOS, Check.ai) for repeatable tasks, and a future human-in-the-loop marketplace for quality control.
- **Technical Roadmap:** The monolithic `Flow` repo will be migrated to the new `Output` framework, splitting into dedicated repos per product (Check.ai, ContentOS, GrowthX) to improve stability and prevent resource contention.
- **Async-First Culture:** The team minimizes meetings via Slack, Linear, and Geekbot. Detailed Geekbot updates are critical for Daniel to generate leadership reports using Claude, making them a key communication channel.

---

## Key Topics

### Company Strategy & Product Vision

  - **Service-to-Platform Model:** The company started as a service to manually close product gaps while building the platform. The goal is to shift clients to a self-serve model over time.
  - **Platform Architecture:** A three-layer stack is being built to enable scalable, high-quality AI content:
    1.  **Vertical Interfaces:** Dedicated UIs (ContentOS, Check.ai) for repeatable, high-volume tasks that chat interfaces cannot handle reliably.
    2.  **AI Workflow Engine:** A code-first framework built on Temporal to manage unreliable LLM APIs. It will be open-sourced as **Output** to enable rapid prototyping and full code control.
    3.  **Human-in-the-Loop Marketplace:** A future product to recruit, vet, and pay specialists for tasks like data labeling, fact-checking, and strategic input.

### Product Deep Dive: ContentOS & Check.ai

  - **ContentOS (fka Atlas):** The primary content marketing platform.
      - **Core Features:** Content Inventory (scrapes client sites), Context Artifacts (stores brand guidelines), and AI Pipelines (custom workflows).
      - **Roadmap:** The Content Inventory and a revamped AI editor are the top priorities to enable client self-service.
  - **Check.ai:** A public index and private tracker for AI tool visibility.
      - **Public Index:** Ranks companies (e.g., Copy.ai, ChatGPT) based on how often they appear in answers to common industry questions.
      - **Private Tracker:** Clients claim their company to track visibility against competitors and generate content roadmaps from a library of pre-researched prompts.

### Technical Roadmap: Migration to `Output` Framework

  - **Current State:** The `Flow` repo is a monolithic codebase containing all workflows for Check.ai, ContentOS, and custom clients.
  - **Problem:** The monolith creates resource contention, where a large client job can degrade performance for everyone.
  - **Solution:** Migrate to the new `Output` framework, which simplifies workflow definition and enables splitting the codebase.
      - **New Structure:** The monolith will be split into dedicated repos per product (Check.ai, ContentOS, GrowthX), each with its own Temporal workspace.
      - **Benefit:** This isolation prevents resource contention and improves stability.

### Team Processes & Tools

  - **Slack:** The primary communication hub.
      - **Channel Prefixes:** `B-` (Build/Engineering) and `D-` (Delivery/Client Ops).
      - **Key Channels:** `#b-epd` (general engineering/product announcements), `#b-client-ops` (client tickets), and lane-specific channels (e.g., `#b-ai-framework`).
  - **Linear:** The project management tool.
      - **Organization:** Kanban boards are used for most projects. The Client Ops team uses 2-week cycles to manage high-volume inbound requests.
  - **Geekbot:** The daily async standup tool.
      - **Purpose:** Provides a low-overhead way for Daniel to track progress and generate leadership reports using Claude, minimizing the need for status meetings.

---

## Action Items

- **Daniel Lopes (GrowthX):** Share the 4-hour feature-build video (Check.ai) with the new engineers covering Rails, React, and AI workflow development.
- **Daniel Lopes (GrowthX):** Create a dedicated onboarding channel for Isaac, Sergey, and Tamy during their first few weeks.
- **Isaac Dudek (GrowthX):** Connect with Daniel mid-week for a deep-dive on Check.ai workflows and machine learning research study contribution.
- **Sergey Kaplich (GrowthX):** Begin Client Ops onboarding with Kirkland and team.
- **Tamy Macedo (GrowthX):** Begin Client Ops onboarding with Kirkland and team.
- **Isaac Dudek, Sergey Kaplich, Tamy Macedo (GrowthX):** Review the 4-hour feature-build video to understand the tech stack, AI workflows, and GrowthX development patterns.

---

## Transcript
**Daniel Lopes:** This meeting is being recorded.

**Daniel Lopes:** So many faces here.

**Daniel Lopes:** Good to see you all.

**Daniel Lopes:** Good morning, good afternoon for some of you.

**Daniel Lopes:** Let me just authorize all these recorders here.

**Daniel Lopes:** Okay.

**Daniel Lopes:** All right, this is the first meeting that we are all having together?

**Daniel Lopes:** Did you guys have a new session in the morning or I haven't had the time to check the calendar?

**Daniel Lopes:** This is the first one?

**Daniel Lopes:** Okay, cool.

**Daniel Lopes:** No, we already had two together, yeah.

**Daniel Lopes:** Oh, okay.

**Daniel Lopes:** With whom?

**Tamy Macedo:** Kirkland and also the first onboarding call with instructions about what to do and, well, Slack and Oh, cool.

**Daniel Lopes:** Okay, so you have some tasks already, so I'm not late in the day, first person you see.

**Tamy Macedo:** Good.

**Daniel Lopes:** I was coordinating with Kirkland yesterday.

**Daniel Lopes:** So like for, I don't know if you all had the chance to introduce each other or, okay, cool.

**Daniel Lopes:** Yeah, so, Isaac, one thing that we've been trying to do lately is to get the, because the team is structured in different lanes, so we have the pro.

**Daniel Lopes:** We lanes and then we have the client ops lane that now Kirkland is the lead for the client ops engineering lane and we also have the AI framework they're working on so like we have like the splits on the team but one thing that really helps is like everybody that joins spend at least like a week or two weeks at least part time on that on the client ops team so you get used to the what the guys do on the work.

**Daniel Lopes:** the side or they could handle client inbound requests that kind of stuff just to get a sense of the that side of the org because once you move into product it's really hard to come back to do that so I hope that makes sense but yeah so for today what I was thinking there's quite a bit of there's quite a lot of context to share so feel free to keep your microphones unmuted and then you can just like stop me at any time but I was just thinking about going through

**Daniel Lopes:** And some basic stuff, like how we use linear and Slack and Geekbot, like how I use it, especially like to keep an eye on everybody, because we don't have meetings, we don't have a lot of meetings, but I do do a lot of like, async to check on how the different projects are moving, so we can move people around whenever we can and all that stuff.

**Daniel Lopes:** And I use Geekbot and linear quite a bit, so I can show you that.

**Daniel Lopes:** And I also want to give you all the, a little bit more background on our, where we are on our journey, one year-ish company, and where we want to be, and also all the products that we have in motion, and some of these things will be launched, like, soft launch this month, and some will be like, announced in January, probably.

**Daniel Lopes:** And we have another bigger thing that we're working on, probably towards February, that we're expecting to, to make more marketing around it.

**Daniel Lopes:** But, But,

**Daniel Lopes:** Yeah, hope that makes sense.

**Daniel Lopes:** Just from the sessions you had before.

**Daniel Lopes:** So what's, what did Kirkland share with you there?

**Daniel Lopes:** I haven't had the chance to catch up with him.

**Isaac Dudek:** He kind of previewed the Atlas and Flow Studio systems and just encouraged us to start diving into the code, looking around once we've got our like, you know, logistical accounts set up and all that stuff.

**Daniel Lopes:** Got it, cool.

**Daniel Lopes:** Okay, that makes sense.

**Daniel Lopes:** Yeah, I'll check the doc that he put it together.

**Daniel Lopes:** I haven't had the time yet.

**Daniel Lopes:** But let me just close all this thing that I have open here.

**Daniel Lopes:** I also have a Figma that I want to walk you through, a Figma file that I want to walk you through.

**Daniel Lopes:** All right, let's see if this works.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Give me one sec.

**Daniel Lopes:** So this is what I was thinking for today.

**Daniel Lopes:** So like this, you already have this done.

**Daniel Lopes:** One sec a our looking office is essentially our Slack cleaner and geekbot.

**Daniel Lopes:** I'm not not a

**Daniel Lopes:** I'm huge fan of Linear, it's better than Jira, and has a lot of cool things, I was a Basecamp user for the last 10 years before this, and Linear has a lot of interesting things that I wish Basecamp had, but the integration of Slack is the main reason why we use Linear, and you can see, most of the folks that are not an engineering team, they don't have to go to Linear to file tickets and things like that, and that really helps on the client.

**Daniel Lopes:** And you can have all the activity feed, like Marcel, for example, rarely opens Linear, but he can skim through the projects that we have in Slack and have an idea, that kind of sync is one of the main reasons why I use, and I'll select some other things, but our Slack is, let me just open Slack on the other screen here, so we have, you will see this EPD prefix, there's two prefix, there's B dash, and there's D dash.

**Daniel Lopes:** So we have, beverages.

**Daniel Lopes:** hi.

**Daniel Lopes:** So I don't know if anybody talked about this yet, or if had a chance to look at the Notion documents, but yeah.

**Daniel Lopes:** Okay, cool.

**Daniel Lopes:** Yeah, so the B is the build team, like all of us, the engineering team, are on the build team, and the client ops team kind of like bleeds into the delivery team a bit.

**Daniel Lopes:** So you're gonna be like interacting with their delivery channels more than the product folks.

**Daniel Lopes:** But we are, we should all be on the, on keeping an eye on all the B channels for sure.

**Daniel Lopes:** At least the BPD is the general one that we have all the engineering product and design folks.

**Daniel Lopes:** And that's where we share more like announcements and things like this.

**Daniel Lopes:** Or just like general, like, hey, we're struggling with some stuff or like what's going on.

**Daniel Lopes:** So we have some, our geekbot posts to this channel as well.

**Daniel Lopes:** And I will show you the geekbot.

**Daniel Lopes:** If you haven't used yet, but we also have these lanes, so the AI lane is responsible for the framework that we were working on, and I will show you that in a bit.

**Daniel Lopes:** We have the client ops, which is the team that Sergey and Tamy will be after the onboarding, and then we have the product lane.

**Daniel Lopes:** Product lane is two products we have today.

**Daniel Lopes:** One is Atlas that we're going to rename to ContentOS, and we have Check.ai, which is another product that I'll show you in a bit.

**Daniel Lopes:** And there will be more products.

**Daniel Lopes:** And we also have, let me see which one else is important for you.

**Daniel Lopes:** And another thing that we do quite a bit is when you have projects.

**Daniel Lopes:** Projects are temporarily, most of them.

**Daniel Lopes:** So we have, like, speed, depth.

**Daniel Lopes:** So we are working towards the version one of check.ai, and we're working towards this feature called content inventory on Atlas.

**Daniel Lopes:** Usually if you click on the project, for example, let's see, check that, I need to do a better job, but usually you would have a link to linear on the top here, they'll point you to the project that is the associated linear project.

**Daniel Lopes:** for this.

**Daniel Lopes:** And what that means, let me see if there's another one here.

**Daniel Lopes:** This one points to a notion document, but something like that would be what you usually see.

**Daniel Lopes:** And we also have, let me see if there's anything else interesting here.

**Daniel Lopes:** For the clients, for the client's tickets, we'll have the rest of the team file tickets in this channel, or sometimes they'll file

**Daniel Lopes:** It's directly in linear, but you can see all the tickets in this channel.

**Daniel Lopes:** So this channel is hooked to linear.

**Daniel Lopes:** And we also like change whoever is on call is in here on that engineering team.

**Daniel Lopes:** So we have two different on calls.

**Daniel Lopes:** We have the product on call and we have the client ops on call.

**Daniel Lopes:** And the client ops on call is like whoever is on call might be the first person to answer for any like bugs or anything that's confusing from the rest of the delivery team.

**Daniel Lopes:** I don't know if Kirkman's thinking about changing that or not, but.

**Daniel Lopes:** So I think that that is the gist.

**Daniel Lopes:** So keep an eye on all the B channels, see which ones you should join.

**Daniel Lopes:** You should just join everything that has an EPD in front of it.

**Daniel Lopes:** And then feel free to join some of the projects too.

**Daniel Lopes:** I need to archive some of these older ones, but I hope that makes sense a little bit.

**Daniel Lopes:** And I organize my Slack into sections.

**Daniel Lopes:** don't know if that would be relevant to you all.

**Daniel Lopes:** very much стало.

**Daniel Lopes:** So— Thank

**Daniel Lopes:** But I have the delivery, we have clients, all separate.

**Daniel Lopes:** We have some of this in Notion, so you can get a sense of how to structure things from Notion.

**Daniel Lopes:** That is our Slack.

**Daniel Lopes:** Our linear is organized, same idea.

**Daniel Lopes:** So we have an EPD team.

**Daniel Lopes:** This team has two groups.

**Daniel Lopes:** So we have product roadmap.

**Daniel Lopes:** This is just like a broad projects that we're considering.

**Daniel Lopes:** Essentially, bets and which bets we're taking.

**Daniel Lopes:** So we have, for example, this is the backlog of ideas.

**Daniel Lopes:** This is stuff that we're not thinking about at all.

**Daniel Lopes:** Like, we thought about it, but we're not going to execute it anytime soon.

**Daniel Lopes:** And this is what's work in progress.

**Daniel Lopes:** Those are like large areas.

**Daniel Lopes:** And then inside EPD here, we actually have the projects that are getting executed.

**Daniel Lopes:** So on Atlas, on ContentOS, we have this inventory version one.

**Daniel Lopes:** We have the entire product of check that version one or alpha, which is another thing, we have the output framework, another feature, this one is like completed, we should archive, and this is your two, your onboarding, I think like Sergey, I don't know if we're still using this, I don't know what's the, I need to catch up on if we still have the issues, tickets up to date and all that, but looks like we do.

**Daniel Lopes:** Yeah, this, okay, I'll catch up on that, but you can see the projects from onboarding here too, whenever we're running this, and this is another thing that we're doing, so this is a project for the client ops team, we're rolling out a new set of agents that we have, yep, I hope that makes sense, feel free to click around, look at the projects, this is the project that I was working on the most recently, and I acted as a PM,

**Daniel Lopes:** On every project that I'm in, so this one I at least know what's going on better, but it was like every project was slightly different, but we usually are organizing things like in combat mode, so you have, this one we're hiding the backlog, but we're hiding the backlog and complete, but you'll usually see something like this, where you have like milestones, milestones are the large areas that we want to tackle, and then you can open and see which ones are getting work done and which ones are done.

**Daniel Lopes:** So like most of the projects are set to Kanban, and in Linear you can have lists or Kanban, but we usually set everything to Kanban, and we set default for every one of the projects, so that might be the view that you're going to see, and Linear also has the option to post updates, so we haven't been super diligent on updates on this project yet, some projects are more diligent, ideally would be like posting updates on a regular,

**Daniel Lopes:** That's something we need to get better, and the client ops team, Stevie and Kirkland, run that cycle there, and all of our projects, they don't run in cycles, with the exception of, like, they don't run in tight cycles, the product lane run on a four week cycle, with a two weeks cool down, and, but they're not aligned the release of anything, so the release will be like, some folks will release like halfway, through the cycle, spend the rest, like, polishing, some folks will release like, right at the end, and the definition of release is like, flexible, the client ops team runs on like, on a two week cadence cycle, because they get a lot more inbound, constantly changing priorities, so their tickets have to be calibrated, almost like, okay, like this client is almost churning, like this week, we work on them, like, or this client, there's a new opportunity that's gonna come over, your, uh,

**Daniel Lopes:** They rolled out like a month for now, but we're just talking about the sales, what can be done, so can we prototype some stuff, so your flow there is faster, so they do have the cycles section that the product doesn't, all the projects don't have, and if you go into the cycles, you can just click on issues and you're to see everything, or if you go into cycles, you can see what is part of the current cycle that was already picked by Stevia.

**Daniel Lopes:** Kirkland, and if you look at upgrades, it carries over automatically, whatever you have on the previous side, so that's just how the thing works.

**Daniel Lopes:** We don't have usually projects inside the client ops team, this is one of the exceptions that we're having, because we're migrating a lot of the older clients to a new version of like AI workflows that we have, so this is like a little bit different, but they're also getting, these tickets are also part of the cycles.

**Daniel Lopes:** There is linear projects for the rest of the company, I was a little confused about seeing the projects in here, because I usually put the EPD onboarding in here, but that's all good, I hope that makes sense, and then Geekbot is the other thing that we do, so Geekbot you're gonna get notified every day on your DM, and on Mondays, it's slightly different, so on Mondays we'll just ask, like, what did do last week, what's your plan for this week, and anything that you could share on, like, insights, or milestones, or challenges, something that you got stuck on that you didn't expect to happen, that kind of stuff, so the more you can share, the better, and, like, don't be afraid of, like, sharing, like, challenges, or, like, progress that you thought you were gonna make and you couldn't make, or, like, personal stuff that block you, it's, like, life happens.

**Daniel Lopes:** It's all right.

**Daniel Lopes:** And I read this on the regular, and the way I read it is I have an NCP on my workspace that I will, like, every day, at least, like, every week for sure, I need to send a report to the rest of the leadership team of what happened.

**Daniel Lopes:** So what I will do is usually I have a project that I can ask questions against using Claude.

**Daniel Lopes:** So I will do something like, every week pull a weekly digest, like, last week, I need actually to do for this week, so I will come here, open the reading of this project, and start a new Claude session and say, And that will generate the report with an update of everything that everybody did.

**Daniel Lopes:** And I also like often do that on a daily basis too.

**Daniel Lopes:** So whatever you write there will help me not have to ask you all the time or have to set up meetings just to see what you're doing.

**Daniel Lopes:** It's like a safety status update.

**Daniel Lopes:** And then any meeting that we'll have, I can just like look, like give me the last three weeks of what you did so I will know more closely to what happened and I will probably have questions just to like get me up to speed.

**Daniel Lopes:** but the system is like super helpful.

**Daniel Lopes:** That makes sense.

**Daniel Lopes:** Yeah, so stay on top of your geekbot please.

**Daniel Lopes:** I try to be consistent myself so you can see what I'm up to there.

**Daniel Lopes:** And feel free to like, if you want to use the same MCP, I can help you set that up so you can have an eye on the rest of the team.

**Daniel Lopes:** Yeah, so this is like a gist of, you know, just saving files and stuff like this.

**Daniel Lopes:** But that is essentially how I use

**Daniel Lopes:** That covers this, like, let me know if you have any questions so far, though I might be going super fast, but another thing that I was doing this weekend, I'm working on this project called Check That with, like, some of all the team members, and I had, like, I know, like, some of you use things in different ways, some of you are getting, like, really, like, starting with, like, figuring out how to use AI in, like, your development workflow, so I recorded the end-to-end development of an entire feature that I had to build, so it's, like, not, it's, like, probably four hours end-to-end, and split into multiple videos, but it's, like, a whole, like, two features built in parallel, plus all the AI workflows, so I, I, I will share with you the doc afterwards, if you could watch that this week, we'll probably help you both understand what Check That does, understand some parts of our stack, like, for Isaac, like, Rails would be natural, but then we have a React in the loop as well, and that

**Daniel Lopes:** And then in the second half of the videos is for building the AI workflows are a part of this feature, the power of the features.

**Daniel Lopes:** So that is on the other project.

**Daniel Lopes:** So I'll add the link here after this call.

**Daniel Lopes:** I just recorded it as I was working, so it's not polished.

**Daniel Lopes:** And it's just like, I'm trying to explain as I go, but probably there's some points where I'm talking too low.

**Daniel Lopes:** And if you have any questions, I happen to answer, share DMs or anything.

**Daniel Lopes:** And I think we, I don't know if we have a channel for you, for the three of you, I will add a channel if we don't have, just like an onboarding channel for us during this, at least like first couple of weeks where you're getting to learn everything.

**Daniel Lopes:** I'll add the video here later.

**Daniel Lopes:** And yeah, I hope so far that all makes sense.

**Daniel Lopes:** And the one thing that I wanted to share...

**Daniel Lopes:** I shared some of that during your interview process, but just to go through real quick, the background of the company, so probably, I don't know how much of that I've shared, but we never built the company to be an agency.

**Daniel Lopes:** The reason why we started this service as the first line of defense was to be able to build a platform step by step and close the gap on the parts of the platform that are unfinished or unpolished manually until we can get close to a point where clients could use in parallel or in a co-pilot mode with our team.

**Daniel Lopes:** So we are in this process still.

**Daniel Lopes:** So we have big parts of the software are in motion.

**Daniel Lopes:** So like we're still building a big part of it.

**Daniel Lopes:** But until that is fully done.

**Daniel Lopes:** I'm working So

**Daniel Lopes:** We have this big part of it, it's just our team operating the platform for the client, the reason why that happened, like the reason why we came up with this, like, let's just do this this way is because that's, it came out of, like, Marcel's background of trying to teach people how to do this and trying to get folks to use things, to do things themselves inside of their companies and then struggling, trying to stitch together multiple tools and then having to, like, train people.

**Daniel Lopes:** the team on how to do that and, and that not working out.

**Daniel Lopes:** So there's no way you can have six different tools and stay on top of the market that's changing so fast.

**Daniel Lopes:** So the, our shortcut was like, okay, we will do that for you.

**Daniel Lopes:** And then we will, like, eventually simplify the parts that are not changing so fast.

**Daniel Lopes:** And the parts that are still changing so fast, that's where we have our client ops engineering team to can can't.

**Daniel Lopes:** to can't.

**Daniel Lopes:** To always close the gap until we can build for that.

**Daniel Lopes:** And there might be things that you're never gonna build towards.

**Daniel Lopes:** Like there are some enterprise clients or special projects that we don't wanna build features in the product for that because it's so unique.

**Daniel Lopes:** And that is the case for clients like Lovable, where we create like custom workflows or custom product, custom websites to be connected to this custom workflows or custom agents.

**Daniel Lopes:** So we're still gonna do that.

**Daniel Lopes:** And that part will never be like the main source of revenue or it shouldn't be the goal to be the main source of revenue.

**Daniel Lopes:** That part is like an exploration path.

**Daniel Lopes:** And it's like a, almost like R&D path.

**Daniel Lopes:** And like some of it is also like large client revenue that we wanna like stretch and see how far we can push these things.

**Daniel Lopes:** And if there's anything that we can pull back into the, put back in that platform.

**Daniel Lopes:** So like Lovable is an example of this.

**Daniel Lopes:** Augment code is another one.

**Daniel Lopes:** Airbyte, Airbyte is like at the end.

**Daniel Lopes:** Edge, and we have Surge.

**Daniel Lopes:** Surge is a very unique one that I always don't consider a normal client.

**Daniel Lopes:** Lovable and Webflow and Augment Code, definitely there in the realm of enterprise clients that we want to do custom things if we need to.

**Daniel Lopes:** Everyone else falls into the category layer, the layer of the product that we can build for them.

**Daniel Lopes:** And whatever we have shortcomings, we need to fix that over time.

**Daniel Lopes:** Kirtland probably touched this already, and we talked about this in our interview, but we have, you'll see many tools out there, the way you handle LLM projects is by stitching things together in a GUI interface, like a graphical interface where you have nodes and you zap your style or N8N style that works to a certain point, but then when you have things that need to have self-examination,

**Daniel Lopes:** Evaluation, things that should be, like, has complex prompts or have multi-steps or have, like, loops or have conditions or workflows that will, like, call other workflows.

**Daniel Lopes:** It gets gnarly super fast.

**Daniel Lopes:** And we are in this age where, like, writing code, LLMs can help you do a lot of the work.

**Daniel Lopes:** So we got to the point where, like, we started like that, like, just, like, trying to, like, can I stitch together, like, all the tools and help clients run their own thing?

**Daniel Lopes:** And we did that for the first, like, four months of the company.

**Daniel Lopes:** Almost, yeah, four or five months.

**Daniel Lopes:** And we hit the wall on everything.

**Daniel Lopes:** So we hit the wall on, like, scalability of these tools, subscription that they wanted to charge us.

**Daniel Lopes:** They wanted to, like, hold us hostage to, like, contract fees, like, that were, like, completely out of whack.

**Daniel Lopes:** Like, it would start to, like, yeah, it's, like, free with, like, X amount of LLM calls because we're partners and we're teaching these things in a network.

**Daniel Lopes:** the cool break.

**Daniel Lopes:** and

**Daniel Lopes:** Now we're to charge you 30k a month because you have high volume, and now I've completely locked into this product, so we have that happen at the same time that the products couldn't handle the volume that we're dealing, so like if you're doing like a thousand pages scraping for a client to understand what they have written in the past, essentially like no tool supports that without capping you somehow, so we built this framework on top of this other tool called Temporal.

**Daniel Lopes:** Temporal is an orchestrator, and you can write Temporal workflows for anything, so it's not meant for AI, so it was not designed for AI from the ground up, but it was designed for powering microservices on larger companies, where you have like an army of like smaller apps that have to talk to each other and they fail at different rates, they have different requirements and all that, and this just happens to be the perfect solution for be the for managing that, this just

**Daniel Lopes:** APIs that will crash all the time, or they're unreliable, or that's just the nature of LLMs.

**Daniel Lopes:** So we essentially build our framework on top of Temporal, and we try to simplify the Temporal interface to the point where we can have agents generate most of the workflows.

**Daniel Lopes:** So we didn't build on top of Temporal, just to do Temporal, the goal is always like, can we get to the point where you have the same fast development that you have on a tool like N8N, or AirOps, or Zapier, from the DragonDop that you can prototype real fast, but continue to evolve if you need to pop the hood and continue to code normal code.

**Daniel Lopes:** And can I do that first version as in natural language, since LLMs are getting so good at writing code.

**Daniel Lopes:** So that's the reason why we build an abstraction on top of Temporal.

**Daniel Lopes:** Temporal is a ton of boilerplate, it's a ton of complexity, it's ton of specific things that you need to do for it to work.

**Daniel Lopes:** So we build like a label.

**Daniel Lopes:** And I was extracting this layer on top to be an open source project.

**Daniel Lopes:** So when I say the AI framework team, it's the team that's extracting the code.

**Daniel Lopes:** Like they're like coming up with like, those are the boundaries of the framework to be open source.

**Daniel Lopes:** Those are the things that are specific to growthx.

**Daniel Lopes:** And this is the stuff that we want to ship and writing the docs and all that.

**Daniel Lopes:** So that is the emotion.

**Daniel Lopes:** Like we're essentially getting ready to, like we're in the process of migrating a lot of the workflows from the old code base to the new framework version.

**Daniel Lopes:** And we're writing the docs this week.

**Daniel Lopes:** So like next week I can have you all take a look on the new version and try to install and like use it.

**Daniel Lopes:** For now, we're like probably gonna be working on the same code base that Kirkland, Marcus, Nico are working on, which is our older code base that originated the framework.

**Daniel Lopes:** So that is the flow GitHub repo that I can show you in a bit.

**Daniel Lopes:** But the way we're thinking, let me show you the Figma file.

**Daniel Lopes:** I hope that all makes sense so far.

**Daniel Lopes:** Any questions, feel free to.

**Tamy Macedo:** So far, so good.

**Daniel Lopes:** So one thing that I wanted to show you is, this is actually like, it was not meant for onboarding, but I think it might be helpful.

**Daniel Lopes:** The way we're thinking is, the DLLMs enabled a bunch of use cases that are not possible before.

**Daniel Lopes:** And the AI workflow engine is essentially general purpose.

**Daniel Lopes:** You can use for anything.

**Daniel Lopes:** So you can use for content creation, you can use for topic research, you can use for sales enablement, you can use for anything that like N8N or Zapier, or BIFT, the company that I worked with for, did or does.

**Daniel Lopes:** And there are tools, like there is no in between today where people, you either have drag and drop tools, or you have frameworks for programming, like, and that's like Langchain, and Python frameworks, like TypeScript frameworks, there's nothing in between where like if you are a programmer like Kirkland, or Tamy, or Sergey, that you can have the best of both worlds.

**Daniel Lopes:** And we are in the setup that we think, like you see like how we can create workflows, and you have in the video that I created, that I recorded this weekend as well.

**Daniel Lopes:** With the right setup, you can create a workflow in 10 minutes, that does pretty advanced stuff that you wouldn't be able to do in any end.

**Daniel Lopes:** And, but you can also, you can't do that with Langchain, because Langchain is not instrumented for that type of work.

**Daniel Lopes:** So, we think the AI workflow engine is general purpose.

**Daniel Lopes:** That's why.

**Daniel Lopes:** We're thinking about making it open source, see if there's a way for us to like do the community around and maybe later next year we have like a marketplace of workflows where folks can publish their workflows and you can use that in clay, can use that in Zapier, you can use that whatever you want.

**Daniel Lopes:** And that is the layer that's under the hood that we don't, we're not thinking about how to productize that or how to make money out of that at this point.

**Daniel Lopes:** Like it's like we have a bunch of ideas on how that could happen, but we're more interested in like, let's just make this useful to other people and launch it and see if we can build a community around it.

**Daniel Lopes:** And then on top of this, for anything that's LLM based, we think you need vertical interfaces.

**Daniel Lopes:** If you want to do like high volume or repeatable work or high quality work, you can't rely on just like a chat interface.

**Daniel Lopes:** Chat interface is great for like one offs.

**Daniel Lopes:** So like if you want to do like write one article or if you want to do like one research.

**Daniel Lopes:** You're not a challenge.

**Daniel Lopes:** Sure.

**Daniel Lopes:** Or if you want to do like a very narrow thing, but the moment that you need to be like specific and repeatable, then you start getting like, oh, for coding, you need cloud code.

**Daniel Lopes:** And that thing has its own user interface with like different sub-agents, different features and all that.

**Daniel Lopes:** Same thing if you want to do like a research product, then you have Perplexit.

**Daniel Lopes:** In Perplexit, we have different buttons, have like different parts of the user, has a chat as part of the core there, but that chat does a lot more than just like freeform chat GPT.

**Daniel Lopes:** And anything that's like freeform, you can't do like reliable, repeatable results.

**Daniel Lopes:** So like, for example, if you're going to create articles, let's say you have 10,000 topics or like 1,000 topics that you need to write an article about how do you ensure the same steps, you know?

**Daniel Lopes:** So that's where like guiding people.

**Daniel Lopes:** As through this process, we think you need a dedicated user interface, most of the cases, and that is where the content OS part fits in.

**Daniel Lopes:** Like that project, you need to come up with the strategy of what you write about, you need to come up with the opportunities that might be worth taking, and then once you take an opportunity, need to research in a certain way that's always as accurate as possible, and then you need to probably draft an outline, and then once you have the outline, you have to like create the content, and that's just for creating new content.

**Daniel Lopes:** If you want to optimize the content, then there's like another set of things that you need to do, and like imagine doing that with a chat.

**Daniel Lopes:** You can do it, but it depends on how you prompt the chat, depends how you structure the whole thing, depends on how you set up the project for that chat session, depends on a ton of stuff.

**Daniel Lopes:** So that's where like we think.

**Daniel Lopes:** Something like a dedicated user interface for the challenge that you're dealing with makes it doable for normal people to use.

**Daniel Lopes:** For programmers, sure, you understand what a to-do list is, understand what a context window is, you understand what an API is, you can create a plan, and the agent under the hood is going to follow it.

**Daniel Lopes:** For somebody that's a writer or an editor that doesn't understand how these things work under the hood, good luck.

**Daniel Lopes:** So that is some of the challenge, I would think, like, vertical interface is still going to be super important, and then the last thing, the last part of the onion that we're thinking about, it's like, vertical interface is on top, ContentOS is an example of that, and then AI workflow engine in the middle, so we can build all the features that are AI powered, and then the last part would be, you're always going to need somebody to check on these things, it's like under-terministic, so you're going to have It can work, let's say you create the perfect workflow.

**Daniel Lopes:** You create the perfect user interface on top, 95% of the time you click on the button and it works, the other 5%, maybe it's like, what the heck happened here, you know, like, we're like, it's like halfway there, or like, or like 80% there, but then you botched the last part of the work.

**Daniel Lopes:** So we need to have ways to involve, or like ask for humans to unlock the workflows, or to train them, or to do the final, or to polish, or to make the decision of like, what is good and what is not good, and that is the part that is least developed on our system, like we haven't touched that at all, essentially.

**Daniel Lopes:** So we have, today, our main vertical interface for growthx will be ContentOS, we think we can let the clients start using it, and we have a bunch of milestones from now on to first week of February, that we can let clients use, it's going to be simpler for the team, the AI workflow engine is

**Daniel Lopes:** It's the part that is most developed.

**Daniel Lopes:** And the last part would be like, can we have those two areas make requests to a marketplace and have the folks not have to worry about, like, this is an AI-generated thing, or this is like a content OS for this certain client that I have no context about, where I don't know what the client does.

**Daniel Lopes:** Because, like today, everybody's combined, like writers, editors, everybody is like, they're joining the, they have to understand what the client does first, they have to onboard into the document, they have to be in Notion, they have to be in Slack, they have to be in a bunch of Zoom calls, just to get a sense for how to judge if that topic of choice is good or not, or if the draft is good or not, or like, if to fact check things properly.

**Daniel Lopes:** So we think like we can make the entire delivery team on the writing team and editorial team and the research team to be a lot more efficient if we can create this like ad hoc market.

**Daniel Lopes:** Where maybe for a client like Augment or Airbyte, we need five editors, and they need to be experts in ETLs or technical things, while for another client who just needs one person, and that person is only thinking about tourism, you know, like that's the topic of the client.

**Daniel Lopes:** So we literally have the challenges, like how to allocate people to the right needs based on the content or based on the topic, not just based on the client, for example.

**Daniel Lopes:** So that is part of how we're thinking, and like ideally, we would be able to onboard a lot more people faster, because that is like, let's say we have a client like Airbyte, and they want to launch a new product that requires like a thousand pages that they want to produce.

**Daniel Lopes:** You can't just publish a thousand pages in the AI-generated pages.

**Daniel Lopes:** You have to have somebody review them.

**Daniel Lopes:** How do I get this many people into the company?

**Daniel Lopes:** Super hard.

**Daniel Lopes:** And how do I vet them?

**Daniel Lopes:** How do I make sure that they're working on the right tasks, that kind of stuff?

**Daniel Lopes:** So I can clearly see next.

**Daniel Lopes:** Last year, we're probably going to work on something that's our internal Upwork, our internal ODesk, and not everybody has to be full-time, like some people might be like working on this as a part-time job, some people would be full-time, so that will be like another product that we're going to work on in the future, but we're always going to have humans in the loop, like some other companies, they're going for a full-blown automation, we're to replace people.

**Daniel Lopes:** We're trying to figure out where is, how can we move people's agents higher and higher, and use human help where it's not possible for AI to do, and it's probably never going to be possible.

**Daniel Lopes:** Like choice of taste, it's very specific.

**Daniel Lopes:** So that's how we're thinking about things, so there's a potential marketplace for people help in the future.

**Daniel Lopes:** In the ideal setup, we have every, let's say, for example, every workflow...

**Daniel Lopes:** The would generate the tracing, and you have the whole front API call, each API call, each output of everything that happened, and we can use that tracing to power improvements of that workflow in the future.

**Daniel Lopes:** That is something that's tricky to do today with the existing tools.

**Daniel Lopes:** They're all kind of disconnected.

**Daniel Lopes:** So let's say you're using an API call to SendRush to just get a bunch of keywords, and then you make an API call to OpenAI to decide which ones of those make sense for the contents of this client.

**Daniel Lopes:** And then you get maybe like a subset of 10 keywords or topics, and now you want to research them.

**Daniel Lopes:** Now I make an API call to Perplexity, for example, and then, okay, like now I have 10 researched results, and I have a result, I have an output.

**Daniel Lopes:** You made three API calls, and like the tracing of each one got lost somewhere, and you have no way to track the cost, like how much it costs from SendRush.

**Daniel Lopes:** see see

**Daniel Lopes:** How much was the cost from OpenAI, how much was the cost for perplexity, and what's the slow point on each one, and what is the quality drop on each one too.

**Daniel Lopes:** So the quality drop on SendRush is probably not going to be that bad, but the quality drop on everything that you do LLM call, so both perplexity and OpenAI, would be something that you want to look back in retrospect and say, okay, like I can measure all those things in the past, and that's where we're, we need to improve our prompts on perplexity, for example, or we need to find a replacement for perplexity.

**Daniel Lopes:** That is the kind of visibility that's hard to do today, so we are, the new framework covers that.

**Daniel Lopes:** So everything that runs gets a trace file.

**Daniel Lopes:** So that is following this idea that every workflow execution generates an output that is stored on the edges at the vertical interfaces that I was talking about, but in between, ideally it would have a way for humans to intervene if it's like getting out of, out of, like, off the a the rails.

**Daniel Lopes:** That's I think so.

**Daniel Lopes:** Once that loop is complete, we have a way to go back and learn for everything to happen.

**Daniel Lopes:** So you see like in the new framework that we do this proactively, but that's gonna, for now it's gonna be a little bit abstract, which I talking about, so I hope that makes a little bit sense.

**Daniel Lopes:** In practical terms, what we have today is this.

**Daniel Lopes:** So we have, in fact, some of this, not fully.

**Daniel Lopes:** So this is just to give you the roadmap for the future and the parts of it that are already working.

**Daniel Lopes:** So ContentOS has the idea of insights, has the idea of like keeping tabs of your entire content inventory.

**Daniel Lopes:** So you plug in your website, scrape all your pages and understand all the things that you wrote, all the topics that you covered in the past.

**Daniel Lopes:** We also have a place to store things that are specific to your context.

**Daniel Lopes:** So your personas, your product,

**Daniel Lopes:** Your overview of your company, how you see your company, so that's like you see in the product called context artifacts, and we also have the concept of AI pipelines, so AI pipelines are usually workflows, so every client will get a bunch of like predetermined AI workflows, but if they want to create something different, that's like diverge quite a bit from the standard content types we have, that's the kind of, we can create new pipelines.

**Daniel Lopes:** for them, so those are like the main parts, and then we also have an AI assistant, like a text editor, AI power text editor inside of the platform, and we also think we need to store the data, specific to that workspace, this part is not, it's live, but we are not using it a lot, this part here is live as well, this one, I think it's like fully ready, the content inventory is the part that is most, it's the most, ,

**Daniel Lopes:** The important part that we've been working on for the last like a couple of months, and that is the part that once we cross here, these two things combined is enough to let clients use, and we can have, that is the point where we can switch from being like this opaque platform that the clients don't see, to be something that they at least see the traffic that they're getting and the reporting and the analytics and the work that's getting done.

**Daniel Lopes:** and which parts of their website, and then this part here we have to improve in parallel with this.

**Daniel Lopes:** Today we have an AI editor, has a lot of bugs, like this is another thing that we're working for, all those two things are our number one priority now, and this is kind of like good enough, but then one of the main challenges we have today is that we have a bunch of agents, have a bunch of like core agents, okay, like four or five core agents, and they all can take like free form prompts.

**Daniel Lopes:** team.

**Daniel Lopes:** back.

**Daniel Lopes:** And coming up with those free-form prompts, for example, for a writing guideline, is hard.

**Daniel Lopes:** So, like, the moment that we put non-technical people to do that, that document, like, that prompt can completely change the direction of the agents.

**Daniel Lopes:** So that is one of the parts that the client office team spends quite a bit of time, is, like, reviewing all the context documents when a new workspace is set up.

**Daniel Lopes:** Because somebody can go into, like, a writing guideline document that will be used by a post-processing agent and say, in capital letters, important, you must do this.

**Daniel Lopes:** And then it will stay in the loop trying to do that, for example.

**Daniel Lopes:** Or it would do that so hard that it would deteriorate the rest of everything else that happened.

**Daniel Lopes:** So there's, like, a bunch of things that we're working on there.

**Daniel Lopes:** Like, the ideal setup would be you have a wizard that will help set up these documents in a more, like...

**Daniel Lopes:** So it's not freeform for any person to change, and then we'd have the client ops engineering team being able to look at what happened under the hood and change freeform.

**Daniel Lopes:** So the idea is to reduce the levers from normal, non-technical people, while keeping the levers open for the client ops engineering team, if that makes sense.

**Daniel Lopes:** So that's the gist of the Content OS, and then we have under the hood, have the AI workflow engine, we have the open source project, we have some other ideas for the future.

**Daniel Lopes:** And like I said, maybe in the future, we're going to have a marketplace, and the marketplace will be responsible for recruiting folks, assessing their take homes and assessing who is good for that specific task.

**Daniel Lopes:** And then onboarding them into the tasks, seeing how they perform on the execution, having a place for that pod or their client team, or even like the client itself.

**Daniel Lopes:** we've got a of data to do

**Daniel Lopes:** Define the tasks and define who should be kind of profile that could execute that task and also have like payments involved.

**Daniel Lopes:** So you don't have to be onboarded into a deal or a remote.com and like have to be paid in a certain way.

**Daniel Lopes:** could be paid by a task, could be paid monthly, whatever makes more sense for you.

**Daniel Lopes:** And that whole marketplace could also, should also be used for data labeling.

**Daniel Lopes:** So that's another part of like onboarding a new client.

**Daniel Lopes:** Let's say, for example, they're not happy with the output of an article.

**Daniel Lopes:** Ideally, instead of sending that to the client to like tell us that they're not happy, we get somebody that's in the same space as the client and have that person label the output for us.

**Daniel Lopes:** And that gets fed back into like our internal system for improvement.

**Daniel Lopes:** And let's say we have like capacity.

**Daniel Lopes:** Let's say we have like a client that asked us to add like 500 people to the pool and they were in charge of creating a bunch of pages.

**Daniel Lopes:** Now this client that's like...

**Daniel Lopes:** Reducing the capacity, we can use that capacity for continuing to improve our workflows for everyone else.

**Daniel Lopes:** So by annotating the kinds of contents that we're going to create or creating contents from scratch and have us calibrate the rest of the workflows and our AI engine under the hood.

**Daniel Lopes:** So that's the gist of how we're thinking.

**Daniel Lopes:** So like, what is the path that we can take here to have humans to be super important for both calibration and for maintaining the quality of things and making the right strategic choices.

**Daniel Lopes:** And so that's the gist of the architecture and the way things are getting built is, let me just show you real quick here in practical terms.

**Daniel Lopes:** Yeah, this is more like how we're thinking about potential future roadmap, it's not going to be, it's not, it's never like this, so not even sure if it's worth.

**Daniel Lopes:** Show me, but I just want to give you like a bit of like, this is the kind of  that you show to like investors and say, hey, have everything figured out, this is going to be great.

**Daniel Lopes:** And then like, the reality is just nothing like that.

**Daniel Lopes:** But, so we essentially have two tracks, and like one track is CheckThat.ai, sorry, track one is content marketing platform, and our content marketing platform is split into two.

**Daniel Lopes:** So it's content.os and CheckThat.ai.

**Daniel Lopes:** CheckThat.ai is basically...

**Daniel Lopes:** Uh, Google Analytics for AI visibility.

**Daniel Lopes:** Uh, under the hood, have a bunch of core agents for content creation.

**Daniel Lopes:** These core agents would be like a research agent, a drafting agent, a post-processing agent, a fact checker agent, and you, like, those are the things that, like, Marcus, Nico, Kirkland are using a ton.

**Daniel Lopes:** And then we have a few other things, like, for example, tracking your analytics and all the other stuff.

**Daniel Lopes:** So this is just, like, trying to figure out how we could stack them in, like, in the...

**Daniel Lopes:** ...

**Daniel Lopes:** ...

**Daniel Lopes:** ...

**Daniel Lopes:** It's actually not different, not that different from how I mapped that out like two months ago, so like we're kind of aligned here still, and the marketplace would be something that we would think about, like next year, this is off, but this would be like, we are way, this would start like, skill to you next year, probably.

**Daniel Lopes:** And then the other track is the AI workflow engine, so the AI workflow engine is essentially, that goes to make the framework open source this year, then we can build some user interface on top to make it easier for folks to visualize some parts that are specific to the framework, and then like maybe like Q1 next year, we can figure out how to make a marketplace where programmers can host their, almost like an NPM or like a RubyGens for workflows, and then maybe like Q2, we can do the user There's an interface that will be like lovable for workflows, and then you can have marketers and programmers interact the same way as like lovable, you can.

**Daniel Lopes:** Be not a programmer at all, create an app, but you can get sync that app and have a programmer take over, and then send it back, so we have plans for how to do that, and that's the reason why we think we should own the framework, because we can do that on our base, but if we're trying to do that on something that's out there already, you have no control, so those are some of the things we're thinking about the frameworks, just to give us an overview.

**Daniel Lopes:** of why we're doing both, yeah, I hope that makes sense, I kind of went all over the place, like I usually do, and now I can actually show you the product, yeah, let me show you the easiest one first, so this one is very close to self-serving product, so this is check.ai, it's live, we haven't announced, and we don't have any traffic,

**Daniel Lopes:** on this yet, but let me open as a new user, so you get the logged out experience.

**Daniel Lopes:** So the logged out experience, the idea here is essentially you have something like G2 Crowd or Crunchbase, and instead of just being about reviews, like in the case of Crunchbase, it would be, sorry, the case of G2, or general data from funding, like in the case of Crunchbase, would be a profile, like essentially it would be like, what's the visibility of these companies on a bunch of common questions that people would ask when they're comparing, for example, AI agents, content generation tools, or when they're comparing, so this is a good one actually, so like if you type a bunch of different questions, common questions that people would care about when they're assessing,

**Daniel Lopes:** AI content generation tools, who are the products that show up the most, so a copy AI shows up 55% of the time, ChatGPT, 53% of the time, Grammarly, right there too, and then you can open one of those, and you get their profile, so you can see the story, the history of the company, you can see the visibility against their competitors, you can see some of the questions that we run to Caleb, which is like C, the answers, and see who gets extracted, so like this is an example, what are the best AI copywriting tools available, and it's mentioning Copy AI, Anthropoc, OpenAI, Jasper, and etc., so this is one, and then we run like thousands of those, and average out, and create the rankings, so, and then you can also see some other parts, so have product features, you have screenshots, you have the competitor landscape, you have the most recent most recent'd

**Daniel Lopes:** Business model and pricing.

**Daniel Lopes:** We have user sentiment coming from things like Trustpilot or G2.

**Daniel Lopes:** And this is all generated by our workflows.

**Daniel Lopes:** So we have thousands of pages, we have 7,000 6,000 companies, and we have 25,000 more to add, but we can do it slowly.

**Daniel Lopes:** And so that's the public area of it.

**Daniel Lopes:** And we have the private area.

**Daniel Lopes:** The private area would be, you have, you claim your company, or if you sign up, claim your company, add to your tracker, then you get, let me switch this to a client, for example.

**Daniel Lopes:** Let's say we're working for Ramp, Ramp is one of our clients.

**Daniel Lopes:** You could, we would set up the workspace for them.

**Daniel Lopes:** We would create a bunch of prompts.

**Daniel Lopes:** We have, the difference that we have compared to some of the other competitors is that because we tracked in

**Daniel Lopes:** entire market, we have data already for your space.

**Daniel Lopes:** So you don't start with an empty workspace.

**Daniel Lopes:** We have all the potential prompts, at least for the evaluation state, when you're comparing two different companies.

**Daniel Lopes:** you come up, like your workspace would have a bunch of prompts on the from library, essentially, and that's our library.

**Daniel Lopes:** You can customize, you can pick more prompts from the library, and everything that is from the library is essentially free.

**Daniel Lopes:** So you're going to, you can choose here, and you can like approve, and you're to have data on most of those already, and you don't have to pay beyond your flat fee, and the evaluation stage is free for everybody.

**Daniel Lopes:** That's what powers the public index, and you can also create your custom prompts, and you can create custom prompts by uploading a CSV, or you can also generate custom prompts out of our AI workflows.

**Daniel Lopes:** So that's another feature we have, and you also have support to group.

**Daniel Lopes:** So usually you would like to think about personas and like anything, like who are our personas?

**Daniel Lopes:** So that's another part of the system.

**Daniel Lopes:** So the system, because we know the companies already, we have profiles and everything.

**Daniel Lopes:** We have a company overview and we have a product features document and we all regenerate the personas.

**Daniel Lopes:** So the personas will be like, what are the kind of things they care about?

**Daniel Lopes:** What are the motivations or the typical questions that they ask?

**Daniel Lopes:** And with all this information, we can look up the right topics that people might be interested in something like Stenrush and extrapolate the topics that they might care about and the questions that they might care about and suggest, essentially come up with a content roadmap that they need to pay attention to the answers.

**Daniel Lopes:** So those are the things, all the things are powered by our AI workflows, like the personal generation, the company overview, the profile.

**Daniel Lopes:** And that is the part that the clients would be using.

**Daniel Lopes:** And that we also...

**Daniel Lopes:** We're gonna set up for the clients themselves.

**Daniel Lopes:** And we also have sources, that's another feature.

**Daniel Lopes:** So sources, anything that's coming from, that is mentioning the answers of the prompts that you track.

**Daniel Lopes:** Behind the scenes, there's a whole admin for this as well, where we do the categorization, we create the prompts for each category.

**Daniel Lopes:** A lot of this stuff is, has a prompt generation behind the hood here that is going, that will do like a bunch of research.

**Daniel Lopes:** It can be like research based on category, research based on competitors, research based on Reddit, things like that.

**Daniel Lopes:** And then you get a bunch of prompts.

**Daniel Lopes:** They can be different stages.

**Daniel Lopes:** So we have stage of evaluation, awareness, comparison, post-purchase, like five stages.

**Daniel Lopes:** We have all the brands.

**Daniel Lopes:** The brands are getting discovered automatically by the,

**Daniel Lopes:** And we extract the brands of LLM, and then from here, you have brand candidates, for example, so you can look at some of those and be like, yep, good, approved.

**Daniel Lopes:** And that will create the public profile for the company.

**Daniel Lopes:** So now it's researching Marketo.

**Daniel Lopes:** So that's going to make it an API call to our AI workflows and generate that profile and send back the result for the project.

**Daniel Lopes:** Just some analytics to see how many prompts are running.

**Daniel Lopes:** The bug here should be December 1st.

**Daniel Lopes:** But anyway, this is Check.ai.

**Daniel Lopes:** Check.ai is essentially AI visibility for your category and your company.

**Daniel Lopes:** And then we have ContentOS.

**Daniel Lopes:** ContentOS is accessible through this domain or through Fathom.

**Daniel Lopes:** Atlas was just a codename, internal codename for the product, while I was still figuring out how this thing would look like.

**Daniel Lopes:** Today, the way it looks today, it's very different to the way it's gonna look like in a couple of months.

**Daniel Lopes:** But just to give you a quick overview, Kirkland probably did that already.

**Daniel Lopes:** This is a mockup, this is not working.

**Daniel Lopes:** But this is when I was talking about, when I was talking about the context artifacts, this is where they live.

**Daniel Lopes:** They're freeform, you can generate some of them.

**Daniel Lopes:** you generate like company context, audience personas, writing guidelines, and it's proofreader checklist with this two buttons.

**Daniel Lopes:** But you can go in and change, and you can create more if you want to.

**Daniel Lopes:** And that's what I mean that people can come here, and they can like, just make the document like super long, and that could like derail the whole generation process.

**Daniel Lopes:** But...

**Daniel Lopes:** So that's one of the areas, another areas of knowledge base, it works, and that's where, like, we can ingest every research, and we'll vectorize, and you can do semantic search from here, instead of hitting perplexity, or exa.

**Daniel Lopes:** So you can take in, like, trusted sources of knowledge, curate, and use it for the content generation.

**Daniel Lopes:** We hit a pause on this project for a bit, because it's a, we need to validate it more, and we ran out of time on it, but it's pretty close to ready.

**Daniel Lopes:** And then we have the analytics, analytics connects to your Google Analytics, your Google Search Console, and will power, if you don't have Google Analytics, we also support Fathom, it's like, not all companies have Google Analytics these days, but this will, like, keep track of your traffic, and keep track of your keywords from Google Search Console as well.

**Daniel Lopes:** This is our test account, our blog, and, like, we haven't, this is our tech blog, we haven't announced, or.

**Daniel Lopes:** Or like haven't pushed any traffic in here, but we use it to dog food.

**Daniel Lopes:** So this is all legit content that we created ourselves for engineering team.

**Daniel Lopes:** And then we have assistant.

**Daniel Lopes:** Assistant is kind of like a cloud slash chat GPT with all the context artifacts and access to your internal knowledge base.

**Daniel Lopes:** It works quite well for certain things, but that is one of the parts that I said we need to improve.

**Daniel Lopes:** The things that are core, that were like the main blockers for us to go live with clients using the platform, it's these three areas here.

**Daniel Lopes:** Pages is where you enter your domain and you, it's where you enter your domain and it will like trigger the, this scraping on the regular and opportunities will be the understanding of those pages.

**Daniel Lopes:** And you have essentially like keyword opportunities.

**Daniel Lopes:** domain and your you your domain and your and enter enter

**Daniel Lopes:** would be like different URLs of competitors that you should probably try to compete against.

**Daniel Lopes:** And then you also have LLM opportunities.

**Daniel Lopes:** LLM opportunities would come from check that.

**Daniel Lopes:** So those would be the topics that we discovered.

**Daniel Lopes:** And we can connect the API here and list all the topics from your workspace in here.

**Daniel Lopes:** And once you choose an opportunity, then you would work through the opportunity.

**Daniel Lopes:** And that's the part where our assignments would come in.

**Daniel Lopes:** Assignments, we have the design for everything, so I can show you real quick just for you to get an idea on how things would look like in a couple of months.

**Daniel Lopes:** But we have inventory.

**Daniel Lopes:** We have...

**Daniel Lopes:** We have...

**Daniel Lopes:** have...

**Daniel Lopes:** One of those.

**Daniel Lopes:** It seems like I forgot to update, so...

**Daniel Lopes:** So...

**Daniel Lopes:** So...

**Daniel Lopes:** We have this.

**Daniel Lopes:** This is the design that Marcel put together.

**Daniel Lopes:** So pages would be overview of all the kinds of pages you have, the crawl health, any issues we've found.

**Daniel Lopes:** that's a lot of, like, this, have the data for all this already.

**Daniel Lopes:** And then you'd have the crawled pages, which is essentially the same page that I showed you with a new design, with good collections, like your blog posts, your product pages, your docs, landing, whatever.

**Daniel Lopes:** And this would be, like, technical issues.

**Daniel Lopes:** All the information is there.

**Daniel Lopes:** We're just going to redesign it this week, probably.

**Daniel Lopes:** And then opportunities would be, this would be closer to the user interface we want.

**Daniel Lopes:** And then you would see the keywords and the volume and the URL that that came from, and that kind of stuff, how relevant it is to your personas, match to, like, topic clusters and stuff like this.

**Daniel Lopes:** And then you also have assignments.

**Daniel Lopes:** So assignments would be, like, tasks that are approved.

**Daniel Lopes:** To be started, tasks that are in production, as in like we're working on it, so somebody on the team is like drafting the brief, for example, once the brief is approved, it's like actually getting created, then we have ready to publish, publish and archive.

**Daniel Lopes:** So basically like a linear board for the tasks about existing pages, and once you click on this, then you would have, let's say you're creating the content, the first step would be a content brief, and the brief is essentially the outline and angle you want to take and why it matters, and then you would, through your content generation agent, the agent will do the research and then create the first draft, and then the team would come here and improve.

**Daniel Lopes:** And once it's fully ready, and could send it, change the status for the client to review, and once it's fully ready, send for publishing.

**Daniel Lopes:** So that is the gist.

**Daniel Lopes:** of the assignments area, it's designed to be like human in the loop, so it's not designed for like, press a button and send publish, you know, so it's meant to be like this, like, I need to check first, you know.

**Daniel Lopes:** This is pretty different than the kind of stuff we do today.

**Daniel Lopes:** Today, we'll use this feature called pipelines.

**Daniel Lopes:** So pipelines is essentially free form, connect any workflow you want.

**Daniel Lopes:** You have like a YAML file where you can configure the workflow however you want, and you can stitch together as many workflows as you want.

**Daniel Lopes:** So that is just like, put something out super fast, and get it out, so we can continue to do the work we do while we finish the inventory area.

**Daniel Lopes:** We're always going to have the option to do this, because like, let's say we're doing like something that is more complex, or something that doesn't fit in that flow, or something that's like sales enablement.

**Daniel Lopes:** Well, let's say we want to do like, in the case of Lovable, Lovable we had this.

**Daniel Lopes:** This.

**Daniel Lopes:** We built this for them, and it's essentially, first we need to build a website, so like we did that, and the other thing would be like, we need to come up with topics, so that alone is not a content generation assignment, that is like a research pipeline, and then another one would be like, now that we have the topics, how do I create this website, essentially like every one of those, we have an agent that will take in another idea, and a screenshot, and we'll have a back and forth of their API, to create something that is acceptable, and from there you can remix, like that kind of stuff, like we still need to do like, 20 a week, like 100 a week, ideally in the future when they're fully ready, so you need the matrix, or the structure, from like a reproducible number of settings, but you don't need the settings,

**Daniel Lopes:** You're not going to publish this to a CMS, for example, or you're not going to have a fact-checker have to come here and look at the code, for example, or you don't have to have a writer come here and adjust the intro or adjust the CTA and that kind of stuff to match their tone.

**Daniel Lopes:** So it's a completely different workflow, and it's not also based on SEO keywords, for example.

**Daniel Lopes:** It's not based on LLM opportunities, it's not based on, like, it's just based on taste sometimes, because, like, that's an idea that they have internally.

**Daniel Lopes:** So it kind of breaks the mold a bit.

**Daniel Lopes:** So for when we break the mold, that's where the existing pipelines feature would be there under the hood, basically feature flagged to only, like, enterprise clients.

**Daniel Lopes:** And normal clients would go through, like, analytics, context artifacts on a cleaned up version that's easier to set up, and the inventory feature that has pages, opportunities, and a second.

**Daniel Lopes:** I think that covers the two main products, and yeah, then the last thing that we're working on, just to give you guys a context, this is the repo where like all the workflows live today, so Flow has the workflows for Check Deck, has the workflows for Atlas, for ContentOS, and has workflows for clients, so it's a giant monolith with like, all the workflows, and you can see all the workflows running in studio.glowfax.ai, and like this, all the things here is like workflows for Atlas, and if you scroll down a little bit, you have workflows for clients, if you go into the library, you can see all the different types of workflows we have, and if you open some of these, you can see the, you can see the in-browning, so like for example, for Check Deck, I'm going generate the brand content,

**Daniel Lopes:** So, into you can screen executions, the last runs.

**Daniel Lopes:** And, you can see how they executed.

**Daniel Lopes:** So, you can see input and output of the workflow and then you can see at the step level.

**Daniel Lopes:** And, you can see input and output at the step level.

**Daniel Lopes:** You can see the description of the workflow, or the step.

**Daniel Lopes:** Of the step, but you can also see the description of the workflow.

**Daniel Lopes:** And, you can trigger workflows from here too.

**Daniel Lopes:** So, you can start your own workflows.

**Daniel Lopes:** So let's say I want to run that same workflow and change the params a little bit.

**Daniel Lopes:** I can come here, switch to raw, copy this, run workflow, switch to raw, and then customize.

**Daniel Lopes:** That is one way of doing it.

**Daniel Lopes:** Another way is to run, sorry, another way to see how this workflow works in Temporal would be to click on that button, and then you have the whole execution of the workflow.

**Daniel Lopes:** And you can see where things failed, whenever it's tried, and this is like the more

**Daniel Lopes:** More side of things, but, so that is the, the, the gist of the current structure we have, so we have these two projects, is like Flow Studio, is that user interface that I was showing, that we build, on top of Temporal, so it's essentially a Temporal API client, and then we have Flow, has all the workflows, but it's a monolith, and it's been like, stuff that we've been working on for the past year, so there's like, a lot of workflows that are not used anymore, some workflows are two years, some workflows are custom for clients, and kind of like, a little bit all, all over the place, and then the output, repo, is the one that we're extracting, the open source project, from Flow, so this one has, a bunch of packages, that are specific to things like, rendering, dealing with multiple LMs, dealing with API clients, dealing with like, than to and we just up...

**Daniel Lopes:** So, that

**Daniel Lopes:** Bing workflows or tracing the execution, all those things are split into packages, so for isaac, this will be very similar to Rails, where Rails has active support, has active record, it's a bunch of things, it's the same idea, so output is the name of the framework, it has five different core packages inside, and everything that we do today that you guys will learn with Kerpen this week will not look like this.

**Daniel Lopes:** This is the new version, so the new version you have, a workflow is defined like this, and that's it, you have a function, and they have steps, and a step looks like this, and you can also have evaluators, so evaluators will be functions that will run to test the output, and we have some examples here as well, so let's say, we have something like, this one for example is a very basic one,

**Daniel Lopes:** It's a little bit not quite, the one that has a prompt, nested, nested, this one I think is good, so we have, the workflow will look like this, so we just import the three lines at the top, and then we import the steps, and then you have this schema that you want out of it, and then you have a description, and you have a name for the workflow, description is not required, and these are just like types that are getting imported, and then we have the function that will be executed, and all of this you have, this one doesn't have prompts, but we also have a prompt rendering part of things here, that you will write your prompts in, in Markdown, with like the settings on top,

**Daniel Lopes:** And you can interpolate things with liquid, and you can do things the same, and then you can load the prompts in a step, so a step would be like, explain this topic, this is just going to make an LLM call, generate text with LLM, pass the prompt name, pass the variables, get a response out.

**Daniel Lopes:** Then another one, same step here, this one has the schema in line here, we usually put in a separate file, but these are the steps.

**Daniel Lopes:** This is a bit different than what you're going to see this week, but it's compatible, so it's running on the same foundation, so like it's still temporal in the same way, everything you're going to learn will apply, and we're probably going to need all three of you to help with the migration of the existing code base to this new version, and this new version we're going to split into three.

**Daniel Lopes:** So it'll be like a check that.

**Daniel Lopes:** that.

**Daniel Lopes:** Workflows project will be like an Atlas or ContentOS Workflows project, and a GrowthX Workflows project, and each one of them will have their own temporal workspace, they will have their own APIs and stuff like this, so we don't step on each other's and if somebody runs onboarding Webflow with 200,000 pages and runs a scraper on that, it's not gonna take everyone else down.

**Daniel Lopes:** So, that's some of the stuff that we deal with today, but I hope that all makes sense, it's like I know it's a lot to take, and especially on day one, but once you start playing with things, you're gonna get a good, a better grip, but I, it's probably gonna take a month to get used to all this, and, yeah, like, sorry, I'm over 10 minutes, and have any questions, I'm happy to answer anything, or, yeah.

**Tamy Macedo:** Yeah, I think the information is still, like, sinking in, honestly.

**Tamy Macedo:** I might have questions in the next few days, but for the moment, it's like information being processed.

**Tamy Macedo:** Overloads.

**Tamy Macedo:** Yeah, a little bit.

**Sergey Kaplich:** Yeah, it was a lot, but I have a question about, I know that Ramp is a client, and you just showed that you're building something or it's already in production for Brax, and I know they're kind of competitors in the tech theme.

**Sergey Kaplich:** So I want to like, how do you actually work with competitors?

**Sergey Kaplich:** Because there could be some overlaps, I suppose, or something like that.

**Daniel Lopes:** Can you please explain a little bit?

**Daniel Lopes:** Yeah, so like that is something that they, it depends on the clients.

**Daniel Lopes:** Like for example, some clients like Engine versus Ramp.

**Daniel Lopes:** Engine, when they have that, like Engine really doesn't want to have any overlap with Ramp at all.

**Daniel Lopes:** In that case, we usually separate the pods.

**Daniel Lopes:** So the riders that ride for Ramp and Engine are completely different.

**Daniel Lopes:** They're not the same people.

**Daniel Lopes:** These strategies.

**Daniel Lopes:** These

**Daniel Lopes:** Strategists might have awareness because the strategist pool is shared, but they were not going to create a content strategy for Ramp and then use that same one with Brex.

**Daniel Lopes:** And it's usually in practice, they're pretty different.

**Daniel Lopes:** It looks the same on the surface, but each one has their own topics that they want to address, their own areas.

**Daniel Lopes:** So, like, we haven't had the problem yet.

**Daniel Lopes:** Sometimes, like, Engine and Ramp was, like, actually, Engine said, like, I know you guys work with Ramp.

**Daniel Lopes:** And then our solution there is, like, the teams don't overlap.

**Daniel Lopes:** That said, the engineering team overlaps.

**Daniel Lopes:** So if we need to do, but we're not sharing data among the workspaces, if that makes sense.

**Daniel Lopes:** But when we create a workflow, like, most of our workflows are general purpose.

**Daniel Lopes:** So our agents for the core parts, all the clients use the same.

**Daniel Lopes:** It's just the settings for that client.

**Daniel Lopes:** It would be different or their personas would be different and all that.

**Daniel Lopes:** And the thing that is wild that I think like over time we're gonna fix it is that the calibration really depends on the people doing the calibration today.

**Daniel Lopes:** So like if that team understands Brex really well and it's aligned with Brex, they will create the artifacts and the writing guidelines that will like produce one thing and the RAM team will produce something completely different because it's the same agent taking different inputs.

**Daniel Lopes:** But, and the calibration can be all the way from like, you use the same, they all use the same researcher under the hood.

**Daniel Lopes:** Like let's say they're all using X as the provider so we can choose different vendors on the research agent we have and it still produces different results because the type of like parameterization is different.

**Daniel Lopes:** So we haven't had the problem, but that's usually how we do it.

**Daniel Lopes:** So if there's like a high overlap, we separate the teams.

**Daniel Lopes:** Sometimes Sometimes there is.

**Daniel Lopes:** Overlap, but we want to keep on the same team.

**Daniel Lopes:** And that was the case for like augment code or lovable and both.

**Daniel Lopes:** Like I worked on both, they build different things.

**Daniel Lopes:** So we do different things for them, but like there's a possibility of like, what kind of work, what kind of agents can we build for them?

**Daniel Lopes:** So like, or like, let's say strappy and augment code, like they're both technical, like they're both talking about the APIs and they're talking for different angles.

**Daniel Lopes:** Like one is all about like being more technical, the other one's like making the topic easier for non-technical people.

**Daniel Lopes:** So the technical person in the team, in the editorial team can do both and they will be able to own the space better.

**Daniel Lopes:** So that's the gist, but long-term, the more we can put, like the plan is you have the strategy part, like that whole part with like pages, opportunities, and assignments, have that be handed off to the client.

**Daniel Lopes:** And Be you.

**Daniel Lopes:** Have that part be as more automated as possible, and have our strategists just be like, hey, you probably should take a look in these areas, and you should probably consider LLM opportunities over normal keyword opportunities, and then let the client choose, and then our editorial team would just work more on, like, does the brief make sense before we generate, is this aligned, roughly, and then when we execute, the editorial team calibrates.

**Daniel Lopes:** but the client would be the one choosing the strategy, so that's why we're trying to make the push for clients have access to the workspace, and they can pick the pages that they care about, pick the opportunities they care about, and ask the team, like, hey, generate this for me, you know, or, like, editorialize this for me, like, do the final pass, or, like, or write the entire from scratch, if it's, like, something that they want to do.

**Sergey Kaplich:** Got it, got it.

**Sergey Kaplich:** Okay, okay, thanks.

**Sergey Kaplich:** Thanks.

**Sergey Kaplich:** It makes sense, yeah.

**Daniel Lopes:** All right.

**Daniel Lopes:** So, yeah, if you all have any questions, let me know.

**Daniel Lopes:** I'm always available on Slack.

**Daniel Lopes:** Feel free to DM me.

**Daniel Lopes:** Like, people are like, oh, I'm afraid to disturb you.

**Daniel Lopes:** Like, don't worry.

**Daniel Lopes:** I'm here for this.

**Daniel Lopes:** And I might just be a little slower to answer sometimes.

**Daniel Lopes:** But I'll put together.

**Daniel Lopes:** Like, Kirkland will be a good source for asking questions, especially in these first two weeks.

**Daniel Lopes:** I'm happy to answer anything that you have, any questions you have, too.

**Daniel Lopes:** Isaac, I think probably, like, by Wednesday or Thursday, I want to give you, like, an overview of some of the workflows that we have for Check.ai.

**Daniel Lopes:** And one thing that we're doing there is, like, a research study that we're building a machine learning model to predict the probability of your page being cited based on a bunch of different traits that a page might have and And...

**Daniel Lopes:** I've been the one, so we have a data scientist working on that as a contractor, and I've been the one maintaining the workflows for her, and I'm kind of a bottleneck, so it would be cool if I could, like, have you, like, onboard you on that part of the workflows.

**Daniel Lopes:** They're not complicated, like, they're not simple, but it's not nothing different from the things that you're to learn from Kirkland this week, and I have most of it done.

**Daniel Lopes:** We'll have a couple of bugs that we need to fix, and then a couple of other things we'll start to build, but yeah, like, probably for the next couple of weeks, it would be cool to get your hands dirty here.

**Isaac Dudek:** Sure, let's do it.

**Daniel Lopes:** Cool.

**Daniel Lopes:** All right, thanks everyone, yeah, and hope you have a good week, and I will send you that video with the building of the lifted features that I did this weekend.

**Tamy Macedo:** Awesome.

**Tamy Macedo:** Awesome, great.

**Tamy Macedo:** Thank you, thank you so much.

**Tamy Macedo:** Cheers.

**Tamy Macedo:** Thanks.

**Tamy Macedo:** Bye.

**Tamy Macedo:** Bye.
