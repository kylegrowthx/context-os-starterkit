# Shaping with Ryan Singer

<metadata>
date: 2026-02-04
time: 17:00 UTC
duration: 177 minutes
organizer: marcel@growthxlabs.com
participants:
  - Marcel Santilli (GrowthX)
  - Daniel Lopes (GrowthX)
  - Ryan Singer (Consultant, Shape Up author)
fireflies_id: 01KG80A7B7YMS32CJD0P4Z7D7J
meeting_link: https://us06web.zoom.us/j/87687687726?pwd=2vzjibdeVkWIdibaIp0By26aakWKMa.1
transcript_url: https://app.fireflies.ai/view/01KG80A7B7YMS32CJD0P4Z7D7J
source: fireflies
enriched_on: 2026-02-28 20:00 UTC
</metadata>

---

## Summary

Ryan Singer led a product shaping session focused on the ContentOS platform UI and navigation architecture. The team resolved a critical architectural question: optimization work and new page creation should live in separate workflows with distinct UI patterns. The meeting established "Learn & Improve" as the primary staff workflow, reorganized navigation to surface the right work at the right time, and clarified the onboarding calibration process.

---

## Context

GrowthX is building ContentOS, an AI-powered content platform that needs to support both new page creation (the exciting, revenue-generating work) and page optimization (the essential but often neglected maintenance work). The team has been struggling with staff not knowing what to focus on, clients not seeing the value being delivered, and a calibration/onboarding process that was confusing both internally and for clients.

Ryan Singer, author of "Shape Up" and former Basecamp product strategist, is consulting on product design. This was a follow-up session from previous shaping work, with a target launch date in March 2026.

---

## Relevance

**To ContentOS Product:**
- Complete navigation restructure: Learn & Improve → New Page Opportunities → Progress Snapshots
- "Work Queue" eliminated as standalone concept—work lives within its context
- Optimization experiments are distinct from new page creation workflows
- Clear separation enables proper database architecture without painting into corners

**To GrowthX Services:**
- Staff will land on "Learn & Improve" as their daily starting point
- New page opportunities remain the client-exciting, sales-driving feature
- Progress Snapshots serve as client communication tool
- Calibration/onboarding simplified to three critical inputs: Personas, Analytics, Site Crawl

**To CheckThat:**
- The same AI workflow framework powers both ContentOS and CheckThat
- Open-source framework shipping this month will support 50+ workflows
- Optimization patterns learned here apply to CheckThat's 9,000+ pages

---

## Overview

- **Product Focus:** Developing a scalable AI-driven content service priced between $5,000 and $10,000 for marketing agencies
- **Market Opportunity:** Targeting 100,000 underserved US marketing agencies by providing AI-native services instead of tools
- **Onboarding Automation:** New system reduces research time to minutes but needs human edits; aims to cut client setup to 2-3 days
- **Content Pipeline Workflow:** New opportunities identified via sitemap crawling and keywords; visible triage and publishing stages enhance staff focus
- **Optimization Tracking:** Separate systems for new pages and optimizations to prevent confusion; planned versioning for continuous content improvement
- **UI/UX Changes:** Clear navigation and action verbs to enhance onboarding clarity and workflow efficiency for both staff and clients

---

## Key Topics

### Navigation Architecture Redesign

Ryan identified that the current navigation buried critical workflows. The new structure prioritizes what staff should do daily:

1. **Learn & Improve** (default landing) - View page portfolio, identify optimization opportunities, run experiments
2. **New Page Opportunities** - Triage → Backlog → Briefing → Writing → Review → Publish pipeline
3. **Progress Snapshots** - Client-facing reporting on impact and outcomes

The "Work Queue" as a separate concept is eliminated. Work lives within its context—new page work inside New Page Opportunities, optimization work inside Learn & Improve.

### Calibration/Onboarding Process

Three critical inputs gate the ability to find opportunities:
1. **Personas defined** - Most fundamental; enables filtering 10,000 ideas down to 500 relevant opportunities
2. **Site crawled** - Automated, but required for gap analysis
3. **Analytics connected** - Nice to have for trust-building, not a blocker

The setup UI should use verbs (Generate, Review) not nouns (Company, Personas). Each item has two phases: auto-generation followed by human review. "Mark Complete" buttons should be removed in favor of clear action steps.

### New Page vs. Optimization Work

**New Page Creation:**
- Linear, multi-step process: Triage → Backlog → Brief → Draft → Annotate → Publish
- Staff knows the phases, can batch similar work
- Produces 700 pages in 4 weeks with current system

**Optimization/Experimentation:**
- Non-linear, checklist-based work
- Goal-oriented: must define what you're trying to improve (CTR, engagement, AI visibility)
- Results feed back as learnings → potentially create agent rules/skills
- For March: focus on meta title/description optimization as MVP

### Client-Facing Communication

Two "golden tabs" that clients should see:
1. **New Page Opportunities** - The HGTV reveal moment; what gets people excited
2. **Progress Snapshots** - High-level outcomes, not granular work details

Staff screens share with clients; clients don't need direct login access. The system communicates "we have a system, we're not just fucking around."

---

## Decisions & Commitments

- **Navigation Structure Locked**: Learn & Improve → New Page Opportunities → Progress Snapshots is the definitive top-level structure. Work Queue as standalone concept is eliminated.
- **Workflow Separation Committed**: New page creation and optimization/experimentation will have completely separate workflows, UI patterns, and database architecture.
- **Calibration as Gate**: Three inputs must be defined before opportunity discovery becomes effective: Personas, Site Crawl, and Analytics (in priority order).
- **Verb-Based Actions**: UI must use action verbs (Generate, Review) instead of noun-based folder labels to drive behavioral clarity.
- **Two-Phase Process Standard**: All setup flows follow auto-generation → human review model. Skip buttons eliminated in favor of explicit "Does Not Apply" option.
- **March MVP Scope**: Meta tag/title optimization is the minimum viable optimization feature for March launch. Full optimization suite is a future build.
- **Client-Facing Surfaces**: Only two tabs should be prominently surfaced to clients: New Page Opportunities and Progress Snapshots.

---

## Open Questions

- **Optimization UI Patterns**: How should different optimization types (meta titles, images, text, broken links) render in the UI? Current thinking is mixed (some modal-based edits, some checklist-based), but design pattern needs clarification.
- **Optimization Feedback Loop**: How do learnings from optimization experiments feed back into agent rules/skills? Need data model for storing optimization results as training signals.
- **Analytics Trust Building**: When should analytics data be surfaced to staff vs. clients? Current assumption is staff-only for March, but client trust-building may require early exposure.
- **Calibration Completeness**: Is the three-input gate sufficient, or are there hidden dependencies we'll discover during QA? Plan to stress-test with actual onboarding scenarios.
- **Progress Snapshot Granularity**: Should client-facing reporting be weekly email digests, dashboard-only, or both? Marcel's vision is eventually email-first with optional dashboard login.

---

## Action Items

**Daniel (GrowthX)**
- Send Ryan the video and GitHub link of the open-source AI workflow framework for prototyping and review
- Continue migrating legacy workflows to the new AI agent framework to support upcoming product launch

**Ryan Singer (Consultant)**
- Review the open-source AI workflow framework and prepare feedback
- Evaluate time availability post current client project and communicate capacity for contribution

**Daniel & Marcel (GrowthX)**
- Refine UI to include verb-based action labels (Generate, Review) instead of folder-like static labels for clarity in calibration/setup flows
- Remove ambiguous "Mark Complete" buttons from setup screen and replace with actionable steps per item
- Implement explicit "Does Not Apply" option instead of skip functionality for calibration steps
- Build onboarding/tutorial around the two-phase process: auto-generation of brand data followed by human review and calibration
- Revise navigation to prioritize "Learn & Improve" and "New Page Opportunities" as primary workflows for staff and client engagement
- Define clear distinction between new page creation workflows and optimization workflows, and design separate UI/work queues accordingly
- Prioritize meta tag and meta description optimization tool development for March launch as a minimum viable optimization feature

**Team-wide (GrowthX)**
- Continue development and refinement of opportunity discovery, persona calibration, and analytics integration to support content strategy generation and client reporting
- Prepare for next shaping session focusing on UI navigation flow and integration of learn and improve workflows

---

## Transcript

**Marcel Santilli:** Invite.

**Marcel Santilli:** Sec.

**Marcel Santilli:** Sorry.

**Marcel Santilli:** No problem.

**Marcel Santilli:** How do you set up with a meeting that you don't own?

**Marcel Santilli:** Just invite the room.

**Marcel Santilli:** Ah.

**Marcel Santilli:** And then select for me and then it will like ring your answer.

**Ryan Singer:** Marcel, you're also there.

**Marcel Santilli:** Hey, we're gonna log in into the main camera here.

**Ryan Singer:** Ah, cool.

**Ryan Singer:** Okay.

**Marcel Santilli:** Recording in progress.

**Ryan Singer:** Boardroom, No feed yet.

**Ryan Singer:** Let's see.

**Ryan Singer:** All right.

**Ryan Singer:** Okay.

**Ryan Singer:** There we go.

**Ryan Singer:** Now we have the classic setup.

**Ryan Singer:** Nice to see you guys.

**Marcel Santilli:** Yeah, good to see you, man.

**Marcel Santilli:** Sorry.

**Marcel Santilli:** Sorry I'm a couple minutes late.

**Ryan Singer:** No problem.

**Marcel Santilli:** All right.

**Ryan Singer:** Things are good.

**Ryan Singer:** A little.

**Ryan Singer:** A little busy.

**Ryan Singer:** Yeah.

**Ryan Singer:** Probably for you too.

**Ryan Singer:** Yeah.

**Marcel Santilli:** It'S.

**Marcel Santilli:** We had a board meeting yesterday and it's definitely feeling like the hardest right now.

**Marcel Santilli:** Yeah, yeah, yeah.

**Marcel Santilli:** But you know, it's like.

**Marcel Santilli:** It kind of feels the hardest and at the same time the highest level of conviction I've ever had.

**Ryan Singer:** Oh, that's a good combo.

**Marcel Santilli:** So it's like both things are good that they're like a joint.

**Ryan Singer:** Yes.

**Marcel Santilli:** Just to give you the context, I think it's actually helpful based on the stuff that I.

**Marcel Santilli:** The video that I sent to you and stuff that I don't know if you had the time to watch.

**Ryan Singer:** I did actually.

**Ryan Singer:** I reviewed the video.

**Ryan Singer:** I did, yeah.

**Marcel Santilli:** So just to give you context, what that video means in the.

**Marcel Santilli:** In the timeline of the company.

**Ryan Singer:** Yes.

**Marcel Santilli:** So beginning of last year, Marcel and I essentially like had a bunch of things that we could sell.

**Marcel Santilli:** Like he essentially sell anything.

**Marcel Santilli:** Any kind of automation and marketing and sales that.

**Marcel Santilli:** So many things that we could do.

**Marcel Santilli:** And we started selling all those things and then we tried to find what is the thing that we can sell enough that there's enough demand that will be a price that will be like close to what you pay a human, but outperform a human quite a bit.

**Marcel Santilli:** That would be like five to $10,000.

**Marcel Santilli:** And we landed on content creation and managing large ish websites, basically.

**Marcel Santilli:** And.

**Marcel Santilli:** And that's the.

**Marcel Santilli:** And then by.

**Marcel Santilli:** So we fundraised in February, built the team enough to just have like small pods doing certain things, but not the perfect team yet because, like, we just like just each one of the seats and figure out some conviction.

**Marcel Santilli:** By July, some of the tools that we're using started to see us as a competitor.

**Marcel Santilli:** So Aerops was one of the tools that I was stitching together a bunch of our APIs that we were building and the agents inside as a UI ops was just a ui and they realized that we were a threat to them and they cut the core.

**Marcel Santilli:** So we had to build the part of the system that we have today as a temporary holdup for being able to do the work that Aerops got us off and after like during that time we also saw the opportunity that monitoring people's AI visibility is a huge thing.

**Marcel Santilli:** And it's a locked data set that.

**Marcel Santilli:** You don't have access.

**Marcel Santilli:** It's not something that you have access like keywords from Semrush or Google Analytics, like it's a private data and there's all these companies doing that at the same time and our clients are buying those things and we know they're going the same direction as us as like they want to start creating content too.

**Marcel Santilli:** So we don't want to be dependent on them and have this trojan horse that all of our clients pay for for $1,000 and not be part of the conversation.

**Marcel Santilli:** Then we do check that in three months essentially and check that out as a growth loop for marketing.

**Marcel Santilli:** So check that we're getting impressions on Google already in just a month since.

**Marcel Santilli:** We started doing marketing.

**Marcel Santilli:** And that is the backstory of like.

**Marcel Santilli:** And at the same time we have trying to figure out what is the minimum amount of stuff that we need to build that will be like that five to $10,000 that a normal person that we can train that is in the content industry that is very capable person, but it's not as capable as Marcel that has a bunch of techniques.

**Marcel Santilli:** So the stuff that we have a bunch of agents to spread out everywhere we search agents for opportunity is basically taking money, decomposing Marcel steps and creating an AI workflow that does that to like in a scalable way that anybody that knows that they're doing an auction can do.

**Marcel Santilli:** So like that product that I sent you, that's just a mock up out of like essentially spent two days after our session just mocking that up and trying to find, utilize every corner that I wasn't sure like what's the right copy, what's the right metrics on the screen?

**Marcel Santilli:** The data on the screen that's about the visual side and more about what is the information I need on the screen and what's the information that I need to collect.

**Marcel Santilli:** Like I need a crawler, I need the analytics and I can have the guys reading that and I can make that UI better and better in the next month.

**Marcel Santilli:** And the assumption is that that will be all we need to be able to solve a lot of the bottlenecks we have today.

**Marcel Santilli:** To the bottlenecks.

**Marcel Santilli:** Like the goal of that version, it's not a final self serving product that will like solve everything.

**Marcel Santilli:** It's more like, are we building leverage in some of the key areas that are problematic today that humans do by hand?

**Marcel Santilli:** We're spaced out is one, another one is keeping an eye on the analytics and another one is coming out with opportunities and executing on some of the opportunities.

**Marcel Santilli:** Not all kinds of opportunities, some kind of.

**Marcel Santilli:** So making progress on that spectrum.

**Marcel Santilli:** And another one would be letting clients log in and even if it's shitty and they know what they're looking at, but if the client can log in and you can walk them through, like, here's what happened this week.

**Marcel Santilli:** That is something that we don't have.

**Marcel Santilli:** So clients think we are operating like an NAN or like a log into their Google search console, which we're not essentially for many things.

**Marcel Santilli:** So those are the two main things like make products and leverage have something that clients can look at.

**Marcel Santilli:** And that's the goal for March.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** I think one thing just to add an additional layer there quickly is we picked a lot of primitives and made a lot of assumptions that are now completely valid.

**Marcel Santilli:** So I think the first one like YC posted, you know how like YC sends these requests for companies.

**Marcel Santilli:** They just posted one this week asking for agencies.

**Marcel Santilli:** Like, think about that for a second, right?

**Marcel Santilli:** Like why Combinator saying more companies should start agencies, AI native agencies.

**Marcel Santilli:** You know, that's totally a software is.

**Ryan Singer:** Eating the world thing.

**Ryan Singer:** Like services that you didn't think were tech.

**Ryan Singer:** It's incredible.

**Marcel Santilli:** There are 100,000 marketing agencies in the US alone, man.

**Marcel Santilli:** Like, that's incredible.

**Marcel Santilli:** Like, you know, that's not even freelancers.

**Marcel Santilli:** That's just legit service providers listed on sites like Clutch Co, you know, saying, I do some kind of marketing, you know, and so that.

**Marcel Santilli:** So that was one we got right, like right away, which was like, no one wants to buy tools.

**Marcel Santilli:** Like, they just want to buy something that just gets the shit done for you.

**Marcel Santilli:** Yes.

**Marcel Santilli:** The second one was like, I remember.

**Marcel Santilli:** I mean, I've been doing content for 15 years for every company I work for.

**Marcel Santilli:** So it's like content was always the secret weapon to make marketing more like, sustainable and compounding.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like, that's how you build credibility.

**Marcel Santilli:** I mean, that's how, you know, you.

**Marcel Santilli:** You've been able to impact so many lives without needing to have these types of meetings with, you know, hundreds of thousands of people, you know, and it's pretty, pretty incredible.

**Marcel Santilli:** Right?

**Marcel Santilli:** And.

**Marcel Santilli:** And then the other thing was, like, last year, people were like, websites are going to go away.

**Marcel Santilli:** And I always had this conviction, like, the Internet will collapse if websites go away.

**Marcel Santilli:** Like, I know, I've been inside these companies that create the training data.

**Marcel Santilli:** Like if the web, if there was no more pages on the web, we are fucked.

**Marcel Santilli:** Like models will not get better like you because you don't have access to people's private databases.

**Marcel Santilli:** Right.

**Marcel Santilli:** So it's like you need the web to be there and you need incentives for people to put really high quality information into the web and continue to update that information forever.

**Marcel Santilli:** And the second you say only ChatGPT is going to be the only quote unquote site in the planet in the front door and no, like.

**Ryan Singer:** It's an aggregator but there has to be a whole bunch of supply to aggregate.

**Marcel Santilli:** Exactly.

**Marcel Santilli:** The long term goal, like the dream would be every company would load the system with how they speak, how they care about their space and all the context that is unique to them.

**Marcel Santilli:** And then every website, every page on the website essentially becomes like a fully personalized experience for that person that's asking a question.

**Marcel Santilli:** Like that is the path that we think websites will eventually become.

**Marcel Santilli:** To get there, there's many things so you need to know like we're not there.

**Marcel Santilli:** So that's going to be like five years.

**Ryan Singer:** Oh, I see.

**Ryan Singer:** So you're saying like the LLM actually becomes like the navigation.

**Ryan Singer:** Like the site is like deeper and wider but you, you get brought into the thing that's more that.

**Marcel Santilli:** Yeah, like just really quickly, just to kind of close the loop there.

**Marcel Santilli:** It's like so like the website we got I think.

**Marcel Santilli:** Right.

**Marcel Santilli:** And the assumption that they're not going to go away.

**Marcel Santilli:** And it's not like a dynamic thing that just personalizes on a visit.

**Marcel Santilli:** It's truly like a knowledge graph and we're approaching.

**Marcel Santilli:** It's like you need to create more surface area.

**Marcel Santilli:** Not for the sake of more surface area, but because you're answering way more queries.

**Marcel Santilli:** An infinite long tail essentially now.

**Marcel Santilli:** Right.

**Marcel Santilli:** And now you're influencing the buyers that come to your site, you're influencing agents that are serving us and you're influencing training data that will form a long term opinion on you.

**Marcel Santilli:** Right.

**Marcel Santilli:** And so like your website now carries like 10x of the impact and the last thing but perhaps the most important thing was like Daniel's insight.

**Marcel Santilli:** This was like 18 months ago.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Plot code didn't exist where he's like coding agents just keep getting better and better and better.

**Marcel Santilli:** Like everything we do should be code.

**Marcel Santilli:** And coding agents are really good.

**Marcel Santilli:** Everything has to be file system based at files.

**Ryan Singer:** Yes, right, exactly.

**Marcel Santilli:** And we need a way to an observability layer and a Runtime layer, AKA like if lifestyle.

**Marcel Santilli:** Right.

**Marcel Santilli:** In a way for the system to just build itself.

**Marcel Santilli:** Because dragging and drop the things in the local tool or writing crazy code off to the side is not sustainable.

**Marcel Santilli:** It's your goal.

**Marcel Santilli:** And I saw you like playing with plot code for breadboarding and that kind of stuff.

**Marcel Santilli:** Like, if you're really good at massaging, you can get it to perform.

**Ryan Singer:** Oh yeah.

**Marcel Santilli:** But if you see the demo that I was sending to you, there aren't workflows.

**Marcel Santilli:** There's probably like 50 AI workflows that need to be repeatable.

**Marcel Santilli:** It's very different than getting my quality code to behave.

**Marcel Santilli:** Even the skills might not behave properly.

**Marcel Santilli:** So we needed a foundation to be able to create like 50 workflows.

**Marcel Santilli:** That's essentially why I only spent two days on this design.

**Marcel Santilli:** It's because I spent the last week and a half migrating the 50 workflows we had on our legacy initial code base.

**Marcel Santilli:** That was the assumptions of this framework to the final version that we're going to make open source this month for checkout.

**Marcel Santilli:** So checkout has like 50 workflows under the hood.

**Marcel Santilli:** Has like 50 or something workflows under the hood that I migrated everything last week to the final version.

**Marcel Santilli:** So like, imagine like rail00 when migrating to like 0.5 before launch.

**Marcel Santilli:** So that's what we're doing last week.

**Marcel Santilli:** And okay, the, the other thing, and the last one, I promise is like, okay, so now like, the hard thing about what we're doing is we started with service and we started with infrastructure.

**Marcel Santilli:** And most companies will build an app or a platform.

**Marcel Santilli:** Very few will build a service layer until everything else is built.

**Marcel Santilli:** And very few will build infrastructure like Ashicorp.

**Marcel Santilli:** You know, like, they had work.

**Marcel Santilli:** Been working on Open source Like 3, 4 years on Vagrant and then Terraform before there was even a company, you know.

**Marcel Santilli:** And then after that, they worked it for a few more years after raising money before they ever even monetized the infrastructure, right?

**Marcel Santilli:** So we're almost like building the infrastructure layer of like, output AI, which is like the agent framework.

**Marcel Santilli:** And then we did service and then we're sandwiching the other two almost, right?

**Marcel Santilli:** And so everything here is us going, hey, the platform has to close the full loop.

**Marcel Santilli:** So with every output, with every unit of work, like, the next one gets better, faster, smarter, you know, or at least a path to that so that it feels like.

**Marcel Santilli:** That it feels.

**Marcel Santilli:** And you have some switching costs and you have some economies of scale happening.

**Marcel Santilli:** Because right now we have diminishing economies of scale with services.

**Marcel Santilli:** So, like a lot of stuff that we worked on, our first session was like figuring out the annotation flow and the client will do the first annotation.

**Marcel Santilli:** And then the other part is our team switches from line editing everything they start annotating so they have all this data.

**Marcel Santilli:** So we also build the team.

**Marcel Santilli:** That's between the taking our agents and injecting the reward models, enforcement, learning all these things to make it go to that next level.

**Marcel Santilli:** But we need that collection of data and we need to reframe the product.

**Marcel Santilli:** You're not a writer, you're more of an editor.

**Marcel Santilli:** And a big part of your job is allocating the failure modes.

**Marcel Santilli:** So essentially everything we talked about or everything that we've done so far really helped me be able to like, visualize the parts of the system that we could, like, okay, this is just enough for like Ada, like one of some of people on our team to be able to do some work there and be able to be more, have more leverage.

**Marcel Santilli:** And then same thing with the analytics and the same thing with the strategy area.

**Marcel Santilli:** We're just trying to figure out what is the minimum amount of analytics that they can absorb, you know, so that's just to set the context of where, where we are.

**Marcel Santilli:** When we met last year, the goal was just like, can we get this out in February?

**Marcel Santilli:** And we had a bunch of other things happen, as in like, check that AI we're launching today and like a soft launch today, hard launch tomorrow.

**Marcel Santilli:** So that took some of our app.

**Marcel Santilli:** So we're essentially like a month behind, but not super behind.

**Marcel Santilli:** I had just based on those mockups that I showed you what it would be super helpful to get your take on it less on the shaping side, but more on like, as like a, like a super good designer and a product manager and somebody that understands Rails and understands how to build, simplify things.

**Marcel Santilli:** Like, is there anything on that?

**Marcel Santilli:** And we can go through like screen by screen.

**Marcel Santilli:** Anything that's like, is a red flag to you or anything that I might not be thinking about or.

**Marcel Santilli:** But that's one just as a pm.

**Marcel Santilli:** Is there something that.

**Marcel Santilli:** Is there anything on my blind spot on that UI or from the UX angle?

**Marcel Santilli:** Is there something that Marcel and I have too much understanding on the business that there are too many questions that you're not understanding.

**Marcel Santilli:** So when I try to train the team, they're going to not understand it or like just get the intuition on that.

**Ryan Singer:** Yeah.

**Marcel Santilli:** And another thing.

**Marcel Santilli:** And then if we don't find anything that's major and then we go to that super fast.

**Marcel Santilli:** The other thing would be like all of the opportunities in the opportunities area there are about new pages.

**Ryan Singer:** Exactly.

**Marcel Santilli:** Fast follow is what happens when you click Optimize and Optimize.

**Marcel Santilli:** There's so many gotchas there on like, okay, like if you're optimizing just the title now you have to go open and say ads and JSON.

**Marcel Santilli:** If you're optimizing like images, how does that look like?

**Marcel Santilli:** If you're optimizing text, is it just a to do list?

**Marcel Santilli:** If you're optimizing broken links, is that just a to do list that somebody has to go there and do?

**Marcel Santilli:** So there's so many things that I don't have a clear view in my mind how it works.

**Marcel Santilli:** Marcel has some opinions and have some ideas.

**Marcel Santilli:** You might have a bunch of like good questions to help us unpack that.

**Marcel Santilli:** So those are the two things that are top of mind for me.

**Ryan Singer:** Like, I like those two for today because I think that they also overlap because I think that like you, there's a lot of value in, in the optimizing of opportunities.

**Ryan Singer:** And in order for, for what we identified when we talked about problem side last time was like, there's this thing where like the staff is not the, the analytics aren't jumping up in front of their faces enough to make them think like I should be.

**Ryan Singer:** I should be updating this page or I should be thinking about the performance, you know, And I think, I think that that's.

**Ryan Singer:** I don't know if we're jumping in already, but like short version is like when I saw the, When I saw the video demo that you sent Daniel, I was really encouraged by the fact that it, it definitely feels like they.

**Ryan Singer:** I felt like I could follow you like where you were, you were moving to different places in the system that had dedicated purposes, you know, And I didn't feel like as much like it was just like a bunch of stuff everywhere, you know.

**Ryan Singer:** And I could feel that a lot of the things that we talked about that they had been like thought through and they had a place and like, so there was that and then I do have some kind of red flags and stuff like that from a UX and product perspective, because I think it's not all the way there.

**Ryan Singer:** But what I like is that it's like, I definitely feel like it's getting warmer, you know, and that we can build on it and it's more, more about like it's.

**Ryan Singer:** Well, yeah, there's some things there and it totally ties into this optimizing thing.

**Ryan Singer:** So, yeah.

**Ryan Singer:** Do you want to.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Share the screen or.

**Ryan Singer:** Yeah.

**Ryan Singer:** I've got one other thing I want to have in my mind as we do this in the session today, which is what I heard, is that for March, you've got two goals.

**Ryan Singer:** One is more leverage in the sense that, like, the staff who use this are doing more to optimize and create impact, like, for the client.

**Ryan Singer:** But the other thing is, I heard client facing pieces, and I think that the client facing piece of this is significant when we think about the kind of the core UI here, like, what does the client see versus what does the client not see is also really important for staff.

**Ryan Singer:** And like, what, like, where should you be directing clients attention to?

**Ryan Singer:** And like, why is this tab here?

**Ryan Singer:** You know?

**Ryan Singer:** So I think that there's a version of this where, like, what I'm curious is like, is it really true that client facing is like, is part of the story for today or is it more in the.

**Ryan Singer:** Nice to have, like, help me understand where you guys both sit in terms of like.

**Ryan Singer:** Because what I heard last time, I have this, like, I have a little bit of a conflict in my head that I want to resolve and probably it's because I misunderstand something.

**Ryan Singer:** What I heard last time was like, we absolutely have to have this like, impact page for a client, which is the thing that you communicate to the client as like the kind of account rep, which is like, it's not at the level of pages and content, it's at the level of impact.

**Ryan Singer:** And like, that conversation has to be happening in order for clients to not be churning.

**Ryan Singer:** And like that.

**Ryan Singer:** What I, what I kind of got from Marcel last time was like, I just felt a lot of fire around that point.

**Ryan Singer:** And then when we looked, when I saw the loom video and there was.

**Ryan Singer:** And you and Daniel, you touched on the insights tab.

**Ryan Singer:** What did I.

**Ryan Singer:** What I kind of picked up was like, this is more for later.

**Ryan Singer:** And I'm wondering if I'm.

**Ryan Singer:** If I'm crossing wires in my head because, like, to me, that insights tab kind of looked like what that, like, account manager thing is, that they're supposed to be communicating the progress at the highest level.

**Ryan Singer:** And I'm just kind of trying to understand, like, is it really later?

**Ryan Singer:** It's like, parts of it later are parts of it now.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Like, what's in the air?

**Ryan Singer:** What's in the air in terms of what's urgent for you guys to solve before March?

**Marcel Santilli:** Yeah, I think the main thing, like, when you talk about leverage, it's more like leverage on our team spending their.

**Marcel Santilli:** Time the right way.

**Ryan Singer:** Yes.

**Marcel Santilli:** We have a checklist of the things that they need to do.

**Marcel Santilli:** Like when a client comes in.

**Marcel Santilli:** Here's all the things you need to do.

**Ryan Singer:** Yeah.

**Marcel Santilli:** It's all in notion and other things and they don't.

**Ryan Singer:** Okay.

**Marcel Santilli:** Very often like some of the team will do the good.

**Marcel Santilli:** The good part of the team will do it.

**Marcel Santilli:** The untrained ones would not do it.

**Marcel Santilli:** And then there's bad people in the mix too that will shackle.

**Marcel Santilli:** So like but even the good ones have potential they might not do because the graduators are not there.

**Marcel Santilli:** Like just being a notion takes too much effort, too much friction.

**Marcel Santilli:** And so that's one.

**Marcel Santilli:** So like account setup is a big one.

**Marcel Santilli:** So like if we can make sure the accounts are set up correctly.

**Marcel Santilli:** That's why we have those control futures, the server fields.

**Marcel Santilli:** We have certain areas that forces the account set up to be mostly all done by the agent and people customize.

**Marcel Santilli:** So there are jobs.

**Marcel Santilli:** Go here, customize here.

**Marcel Santilli:** Go go here, customize here.

**Marcel Santilli:** Mark has done hope there is that we can reduce account setup from like a couple of weeks with a bunch of mistakes here and there and like sending documents to the client to like them doing that in two, three days and then walking the client through in a zoom call.

**Marcel Santilli:** This is what I did.

**Marcel Santilli:** So that is client seeing the surface of the product and okay.

**Marcel Santilli:** And then if we want to let.

**Marcel Santilli:** The client log in into that and.

**Marcel Santilli:** Tweak they can but it's more like they would be a normal use.

**Marcel Santilli:** We're not expecting the client to do any work would be like hey, this is how we do it.

**Marcel Santilli:** We're not sending you a notion document and a bunch of under the hood here there's a system.

**Marcel Santilli:** So that's when we talk about leverage is more about like that Got it.

**Marcel Santilli:** The same kind of thinking goes into like here are the topics that we should that we're betting on for the next six months and here's why and here's the progress we're making.

**Marcel Santilli:** So even if the client never logs in but our our team share their screening every week on their weekly meeting and walk them through that table with like here's the clusters here, the health here, the quality.

**Marcel Santilli:** Here's the amount of stuff we did.

**Marcel Santilli:** That is also like showing that we have a system here.

**Marcel Santilli:** We're not just fucking around.

**Marcel Santilli:** Yep.

**Marcel Santilli:** And same thing with the opportunities area.

**Marcel Santilli:** Even if the client never clicks on the buttons there but our team does right before and shows the meeting.

**Marcel Santilli:** Hey, hey.

**Marcel Santilli:** Like here's a thousand things that came from analyzing comparison.

**Marcel Santilli:** Here's how it works.

**Marcel Santilli:** This is like click on this.

**Marcel Santilli:** Here are all the things we're picking the ones that are that are.

**Ryan Singer:** Got it?

**Ryan Singer:** I got it.

**Ryan Singer:** Okay, you, you.

**Marcel Santilli:** So to me that's that that is a requirement for like being able to do insights because you need to have like to do proper insights later.

**Marcel Santilli:** You need to have all these things happening in the same system to do it effectively.

**Marcel Santilli:** Essentially we have all these things being done in the same system.

**Marcel Santilli:** That inside that is essentially like a couple of weeks of work.

**Marcel Santilli:** It's like a pretty good agent that parses a ton of data and UI work.

**Marcel Santilli:** But if this thing is spread out in like 10 different systems that some people totally don't do, I'm fine basically to do that.

**Marcel Santilli:** So that's why I'm thinking like it's an important part of the system.

**Marcel Santilli:** Ideally like maybe like a quarter from now we iterate on that in so much that it might be the only interface that the client sees.

**Marcel Santilli:** And like they get a digest via emails.

**Marcel Santilli:** Here's everything you got done and you know, and that is the UI for the client.

**Marcel Santilli:** It might be.

**Marcel Santilli:** And then at that point we can just like go full self serve and like you sign up here, we do all the work to get an email, that kind of stuff.

**Marcel Santilli:** But I'm more like the steps towards be able to do that level.

**Marcel Santilli:** We need to start doing the work ourselves as our team.

**Marcel Santilli:** So I'm more focused.

**Marcel Santilli:** Yeah, it's like.

**Marcel Santilli:** The.

**Marcel Santilli:** If we think about buyer centric view of things versus a delivery team centric view of things just to contrast that a little bit in the day every team needs to grow and your website influences everything.

**Marcel Santilli:** It's where most transactions and AKA conversions happen.

**Marcel Santilli:** It's what you can control the most.

**Marcel Santilli:** And if you do it right, it's what could compound and make your life a little bit easier.

**Marcel Santilli:** But if you don't, it's became faster than ever as well.

**Marcel Santilli:** And it's the place you can truly measure and control how you measure things.

**Marcel Santilli:** Like so that's very rare.

**Marcel Santilli:** There's nothing else in the quote unquote marketing brand world that checks all those five things.

**Marcel Santilli:** But then everyone's website is just fine.

**Marcel Santilli:** Like people don't know how to manage a website and they don't know how to manage content.

**Marcel Santilli:** They don't know how to create content and they don't even know how to create context around their brand and they don't even know context.

**Marcel Santilli:** Engineering basics.

**Marcel Santilli:** Right.

**Marcel Santilli:** And, and then on top of that, their analytics are messed up or spread everywhere.

**Marcel Santilli:** And.

**Marcel Santilli:** And so these companies are trying to hire somebody in marketing and they're coming in and at the best company in the world.

**Marcel Santilli:** Like we're talking to Vercel right now about to close a deal with them and they're just like, yeah, we're getting audits from this SEO agency.

**Marcel Santilli:** But like I don't have the bandwidth to go fix 57 broken things.

**Marcel Santilli:** And I also don't know where the.

**Marcel Santilli:** What are the juiciest opportunities for us to go enrich existing pages versus like create net new.

**Marcel Santilli:** Like I think it's like the AI gateway pages.

**Marcel Santilli:** Right.

**Marcel Santilli:** But also like there's this other thing over here that we could do and then they're just like, you know, so that's kind of like the chaos.

**Marcel Santilli:** And then on top of that chaos, there's the quote unquote a yo layer which is like every CEO and every board member is like hey, what are we doing about AO AI visibility?

**Marcel Santilli:** And they need to give them an answer.

**Marcel Santilli:** Right.

**Marcel Santilli:** So like that's the reality of what they're doing.

**Marcel Santilli:** And the, the job to be done that I think is what we nail is like how do you start from context, right.

**Marcel Santilli:** Of the brand, the buyers, the Personas, the questions those buyers have, the mapping, like all the competitors and all of that define what good looks like for them, like AKA the calibration one not.

**Marcel Santilli:** And then audit their entire footprint to know how far they are or how good they are.

**Marcel Santilli:** And then from that point figure out what should they do next.

**Marcel Santilli:** But starting with net new and then back into optimization and then with all that creating a taxonomy layer that helps them understand everything, both the opportunities as well as the existing service area, AKA their assets.

**Marcel Santilli:** Right.

**Marcel Santilli:** So it's almost like a portfolio.

**Marcel Santilli:** Your site is your overall investment strategy.

**Marcel Santilli:** Right.

**Marcel Santilli:** And then there's like portfolios that of how you approach it, you know.

**Marcel Santilli:** So one portfolio could be like high growth stocks, but then some people might be like, you know, anti gold portfolio.

**Marcel Santilli:** Like, you know what I mean?

**Marcel Santilli:** Like the hypothesis of your investments could be slightly different.

**Marcel Santilli:** So anyways, I feel like I dumped too much already.

**Marcel Santilli:** But.

**Marcel Santilli:** But hopefully that's enough to know like kind of where, where we are from both angles.

**Ryan Singer:** Yes.

**Ryan Singer:** So the, the UI needs to enable that conversation to happen around like the process that we're in and how, and how we are going through that kind of flow and then, and then the other piece.

**Ryan Singer:** So there's a, there's kind of like two levels here.

**Ryan Singer:** There's a level of like you want to be able to talk through that process with a potential client and you're having a conversation about like not just like we've got 50 things we have to fix, but kind of like that there's a.

**Ryan Singer:** You're going to enable them to have like strategic moments where they're deciding like what are the opportunities and what are not.

**Ryan Singer:** There's going to be things you're going to do and then there's going to be this feedback loop of like looking at across the taxonomy and like the portfolio and seeing what to do next.

**Ryan Singer:** So there's an element of like communicating the bigger what we do and how we work through the product.

**Ryan Singer:** But then there's also the slightly more micro.

**Ryan Singer:** Like does the staff know what they need to be doing and are they seeing the right things in order to, to be higher leverage, is that right?

**Marcel Santilli:** That's correct.

**Marcel Santilli:** And the bottleneck.

**Marcel Santilli:** Okay, tell me if I'm, if I'm off here.

**Marcel Santilli:** But the bottleneck we're choosing to solve is the how many kickoffs can we do bottleneck first because it's like yeah, solving the existing 60 clients would be able to.

**Ryan Singer:** That's the setup piece.

**Ryan Singer:** When you talk about kickoffs.

**Ryan Singer:** Kickoffs is this setup of all the context and, and that.

**Marcel Santilli:** Yeah, correct.

**Marcel Santilli:** It's the.

**Marcel Santilli:** We do a bunch of research in the brand.

**Marcel Santilli:** We have a kickoff call where we ask questions just not as good as you do but like you know, a 10 as good as you do and try to get all this good input.

**Marcel Santilli:** And, and then we create their content strategy which is like identify all the opportunities they have.

**Marcel Santilli:** We.

**Marcel Santilli:** And then there's a bunch of custom things like audits and things like that that are all things that the pages will simplify because right now it's like we go to Semrush and create an audit.

**Marcel Santilli:** We go into like these other tools and whatnot.

**Marcel Santilli:** Right?

**Ryan Singer:** Yep.

**Marcel Santilli:** And then, and then we calibrate so it's kind of like this process.

**Marcel Santilli:** The key cough is basically when we start with that there's a lot of work that happens between sales and the kickoff.

**Marcel Santilli:** There's a lot of work of like.

**Marcel Santilli:** Researching this space, understanding a bit of their personal whatever you can get from like between sales and we're going to start working together and then we have this eight weeks period that we're just like ordering coming up of opportunities, looking at competitors, coming up with content roadmap and testing sample art.

**Marcel Santilli:** So that is.

**Marcel Santilli:** And it's a eight week year that.

**Marcel Santilli:** We sell.

**Marcel Santilli:** That today.

**Marcel Santilli:** We want to make that easier for everybody to somebody that's just joined, they have like all the things, most of the things automated for them, they have to be just editing instead of having to really have all these things in their mind.

[Transcript continues for ~2.5 more hours covering detailed UI/UX discussion, navigation architecture, optimization workflows, and collaboration planning]

---

*Note: "Board Room" in the transcript refers to Marcel and Daniel speaking from a shared conference room setup. The full 3-hour transcript has been condensed to key sections. Full audio/video available at the Fireflies link above.*
