# Pedro + Daniel

<metadata>
date: 2025-06-23
time: 23:04 UTC
duration: 45 minutes
organizer: Daniel Lopes (daniel@growthxlabs.com)
participants: Daniel Lopes (GrowthX), Pedro Steimbruch (GrowthX)
fathom_recording_id: 70038050
fathom_url: https://fathom.video/calls/334092182
share_url: https://fathom.video/share/S8zKX5FzHtXziLEekZ6ziqx-iaF-S3N_
source: fathom
enriched_on: 2026-03-03 18:45 UTC
</metadata>

---

## Summary

Daniel Lopes onboarded Pedro Steimbruch, a new engineer joining GrowthX's client ops engineering team. Daniel covered company structure and strategy—GrowthX's evolution from a growth agency to a multi-faceted AI company with three key pillars: agency services, Atlas (a Rails-based project management tool), and AI infrastructure (Flow and Studio for workflow creation). The team is prioritizing the migration from AirOps to Atlas, stabilizing client ops processes, and enabling non-technical team members to create custom workflows. Daniel also outlined Pedro's immediate priorities: complete local development setup, meet key team members (Andy, Jason, Kirk, Marcus), review the AirOps Migration project in Linear, and prepare to contribute to client ops 2-week cycles.

---

## Context

Pedro Steimbruch joined GrowthX as an engineer on the client ops engineering team, based in Brazil (conversation is in Portuguese). The call with Daniel Lopes, a founding engineer at GrowthX, serves as the formal onboarding—covering company strategy, current technical focus, and immediate expectations. Pedro came prepared, having already accepted invitations, read the entire handbook over the weekend, set up GitHub access, and begun downloading project repositories. This meeting reflects GrowthX's approach to structured onboarding: providing comprehensive documentation (handbook, GitHub repos) upfront while having senior engineers walk new hires through context and strategic priorities face-to-face.

---

## Relevance

- **To GrowthX Delivery:** Client ops engineering is the backbone of scaling custom workflows for agency work. Pedro's focus on Atlas migration and stabilization directly impacts ability to onboard new clients efficiently and customize workflows for high-value projects. The shift to 2-week client ops cycles creates predictable capacity for custom work.

- **To GrowthX Business Development:** Expanding client ops engineering capacity signals ability to handle more complex, custom client engagements—a differentiator from competitors with "cookie-cutter" service offerings. Each custom workflow Pedro ships improves positioning for enterprise deals requiring bespoke automation.

- **To Technology/Infrastructure:** Pedro will contribute to technical decisions on the codebase (e.g., Sorbet typing, tooling choices in Atlas). Early signals: team questioning Sorbet maturity suggests openness to technical debt cleanup. Flow and Studio are still evolving; non-technical workflow creation remains partially blocked until UI/chat interfaces mature.

---

## Overview

- GrowthX is evolving from a growth agency to a multi-faceted AI/automation company, with 3 key areas: agency services, tooling (Atlas), and AI infrastructure
- Current focus is on migrating from AirOps to Atlas, stabilizing client ops engineering, and improving workflow creation/management
- Pedro will primarily support client ops engineering cycles, but may contribute across projects as needed
- Team is considering removing Sorbet (Ruby typing) from Atlas codebase due to tooling immaturity

---

## Key Topics

### Company Structure and Strategy

  - GrowthX started as a growth agency, now expanding into AI tooling and infrastructure
  - Three key areas:
    1.  Agency services (content creation, marketing)
    2.  Atlas - project management tool for agency work
    3.  AI infrastructure (Flow, Studio) - for workflow creation and management
  - Goal: Validate hypothesis that AI tooling can make previously unscalable service businesses (e.g. design/SEO agencies) scalable
  - Opportunity to leverage "frontier data" from agency work to improve AI capabilities

### Current Challenges and Focus

  - Migrating from AirOps to Atlas for improved workflow management
  - Stabilizing client ops engineering processes
  - Improving ability to create custom workflows for complex client needs
  - Balancing "cookie-cutter" editorial work with custom, high-value projects
  - Scaling ability to onboard new clients and customize workflows efficiently

### Team Structure and Workflows

  - Client Ops Engineering team sits at intersection of multiple areas (tooling, workflows, client needs)
  - Moving to 2-week cycles for prioritizing and executing client ops work
  - Using Linear for project/task management across teams
  - Exploring ways to allow non-technical team members (e.g. Jason, Marcel) to create/modify workflows

### Technology Stack and Tools

  - Three main GitHub repos: Atlas (Rails), Flow (core AI/automation), Studio (UI for Flow)
  - Using Temporo for certain functionality
  - Considering chat interface in Studio for workflow creation
  - Currently using Sorbet for Ruby typing in Atlas, but reconsidering due to tooling challenges

### Onboarding Plan for Pedro

  - First week: Focus on understanding context, codebase, and team dynamics
  - Schedule intro meetings with key team members (Andy, Jason, Kirk, Marcus, etc.)
  - Review Linear board, particularly the "AirOps Migration" project
  - Next week: Begin hands-on coding work
  - Following Tuesday: Participate in first Client Ops End Cycle planning

---

## Action Items

- **Pedro Steimbruch (GrowthX)** — Complete setup of local development environment, review Linear board and AirOps Migration project tasks, schedule and prepare for intro meetings with Andy, Jason, Kirk, Marcus
- **Daniel Lopes (GrowthX)** — Begin weekly 1:1 meetings with Pedro once current coding sprint concludes; facilitate team introductions
- **GrowthX Team** — Discuss and decide on removal of Sorbet from Atlas codebase

---

## Transcript

**Daniel Lopes:** This meeting is being recorded.

**Pedro Steimbruch:** It went really well, went really well. I already on Friday accepted the invites and went to Notion, I read the entire handbook during the weekend. And today I re-read it taking some notes, to do my memo at the end of the onboarding. And it went really well. Now, at the end of the day, I got access to GitHub. And now, before our call, I started downloading the projects and stuff, setting up the projects. I was really excited about the quality of the material, the documentation, man, really cool, and it gives a really nice overview, which normally we miss, you know, that overview when you join a business company, you know? You have to go after the business guys, ask questions left and right to understand something, and you guys have really extensive documentation there, really awesome.

**Daniel Lopes:** Yeah, so that's the part that, like, our way of thinking about the business is kind of complicated, you know? So the more documentation we have, the better.

**Daniel Lopes:** So let me make a brief introduction of what we do here. We started as a growth agency, doing content marketing, specifically. And we were doing quite well, but there was a limitation in scaling. Because the more you do, the more people you need. And that doesn't work so well. So we started to think about it. What if we use AI and automation to make it scalable? Right? So now we have three areas. One is the agency, which continues to do the work. Another is tooling, which is Atlas. And the third area is the infrastructure. So we have Flow and Studio. Flow is the core AI and automation, and Studio is the UI for that. And the idea is to make a previously unscalable business scalable through AI tooling. For example, a design agency or an SEO agency. That's a business that requires a lot of human effort to create these things.

**Daniel Lopes:** But if we can create tools and workflows to automate significant parts of the work, we make it scalable. That's the idea. Now, the business itself is complex because, like, we have three different areas. So the data that we're getting from the agency is what we call frontier data. It's very useful for improving our AI capabilities. So it's kind of a feedback loop. And since the business is complex, we need a good structure, which is why we have a lot of documentation.

**Daniel Lopes:** Now, at the client ops level, you're going to be sitting at the intersection of many areas. Because the client ops is the place where we integrate everything. You know, we need to make sure that the tools work, we need to make sure that the data is good, we need to understand client needs, and we need to create workflows.

**Daniel Lopes:** Right now, we are in the middle of migrating from AirOps to Atlas. So Atlas is our project management tool. It's written in Rails. And we're moving everything from AirOps to Atlas because we need more flexibility. AirOps is kind of limited. So we are in the middle of doing this. At the same time, we are trying to stabilize client ops, which is important. Because the way we operate right now is quite chaotic. We're doing a lot of ad-hoc things, and we need to stabilize it. One of the things we want to do is move to a 2-week cycle. So every two weeks, we plan, we prioritize, and we execute. And that way, we can be more predictable.

**Daniel Lopes:** And the big challenge is customization. We want to be able to do custom workflows for each client. But we don't want to spend hours and hours of engineering time to create that. So we're trying to find the balance between cookie-cutter editorial work and custom, high-value projects. And that's something that's going to be important for you to work on.

**Daniel Lopes:** Now, the infrastructure side, we have Flow, which is the core AI and automation, and Studio, which is the UI for Flow. One of the things we want to do is to allow non-technical people, like Jason and Marcel, to be able to create workflows. Right now, that's not really possible. Because to create a workflow, you need to write code. But we're working on ways to make it easier. For instance, we're thinking about a chat interface in Studio where you can just tell it what you want, and it creates the workflow for you.

**Daniel Lopes:** On the tech side, we have three main GitHub repos. We have Atlas, which is the Rails project. We have Flow, which is the core. And we have Studio, which is the UI. And we're also using Temporo for certain functionality.

**Daniel Lopes:** One thing that we've been discussing is whether to keep Sorbet in the codebase or not. Sorbet is Ruby typing. It's a tool that helps you type your Ruby code. But it's still quite young, and the tooling around it is not great. So we're kind of reconsidering whether it's worth keeping it or not.

**Daniel Lopes:** So for the first week, I think it's important for you to kind of understand the context, understand the codebase, and understand the team dynamics. We're going to schedule some intro meetings with some of the key people in the team. So Andy, Jason, Kirk, Marcus, and others. And you're going to kind of get a sense of what they do.

**Daniel Lopes:** You should also review the Linear board. You should look at the AirOps Migration project. It's a big project, so you should kind of understand what's going on there.

**Daniel Lopes:** And then next week, you can start doing some hands-on coding work.

**Daniel Lopes:** Following Tuesday is when we have the Client Ops End Cycle planning. So that's something that you should attend. And that way, you can see how we plan and prioritize things.

**Daniel Lopes:** Once I finish the current sprint, we can start having weekly 1:1s. I think that's important to kind of check in and see how things are going. And I can help you navigate any issues that come up.

**Daniel Lopes:** So to summarize, the next steps are: you should complete the setup of your development environment, you should review the Linear board and the AirOps Migration project, you should schedule the intro meetings, and we'll start having weekly 1:1s once I finish the sprint. And we'll also discuss as a team about whether to keep Sorbet or not.

