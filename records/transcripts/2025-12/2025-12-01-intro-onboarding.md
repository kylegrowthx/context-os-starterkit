# Intro + Onboarding 

<metadata>
date: 2025-12-01
time: 19:01 UTC
duration: 41 minutes
organizer: team@growthxlabs.com
participants: Kirkland Gee, Isaac Dudek, Sergey Kaplich, Tamy Macedo
fathom_recording_id: 105326757
fathom_url: https://fathom.video/calls/491833603
share_url: https://fathom.video/share/AsQuCu6GtM_sGM4WPsqwzcvG4vaBjWU1
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Kirkland Gee onboarded three new team members (Sergey Kaplich, Tamy Macedo, and Isaac Dudek) to GrowthX's Client Ops tech stack, walking through the core platform architecture (Atlas, Flow, Flow Studio), development tooling (Claude Code and LangFuse), and team structure. The team identified a GitHub access blocker for new hires and committed to a structured week: reading and setup through Thursday, a live workflow-building session on Wed/Thu, and a Friday check-in. All onboarding materials live in Notion and Linear, with Kirkland as the primary contact for questions.

---

## Context

Kirkland Gee leads the Client Ops Engineering team at GrowthX, which is responsible for building and maintaining the internal platform that powers client AI implementations. This meeting introduced three new team members — Sergey Kaplich, Tamy Macedo, and Isaac Dudek — to GrowthX's tech stack and development workflows. Isaac is joining from the Product side to work embedded with Client Ops, while Sergey and Tamy are new engineering hires. The onboarding session walked through the core architecture (Atlas, Flow, Flow Studio), development tooling (Claude Code, LangFuse), and set a structured learning plan for the week ahead, focusing on knowledge transfer before hands-on workflow development.

---

## Relevance

- **To GrowthX Delivery:** Team expansion signals preparation for scaling client delivery. Choice of Claude Code as the standard development tool reflects GrowthX's commitment to AI-first methodology. LangFuse integration provides production observability for AI workflows, critical for debugging non-deterministic LLM outputs.
- **To Internal Operations:** New hires blocking on GitHub access reveals onboarding process gap. Clear documentation and tool standardization (Atlas > Airtable, Claude Code > alternatives) enables faster ramp time.
- **To Team Continuity:** Structured onboarding with weekly milestones (reading → live build session → check-in) and designated onboarding buddy (Kirkland) reduces ramp risk. Isaac's cross-functional role (Product + Client Ops) creates alignment between product development and delivery.

---

## Overview

- **Core Stack:** The platform uses three interconnected apps: **Atlas** (customer UI), **Flow** (backend repo of \~150 workflows), and **Flow Studio** (dev observability tool).
- **AI-First Development:** Use **Claude Code** for all workflow development. It's the default and most effective tool, outperforming Cursor in company trials.
- **Critical Debugging Tool:** **LangFuse** traces all LLM calls in production, showing every step and retry. This is essential for debugging non-deterministic AI outputs.
- **Onboarding Plan:** This week is for reading and setup. Kirkland will lead a live workflow build session (Wed/Thu) and a Friday check-in.

---

## Key Topics

### Team & Onboarding Logistics

  - **Team:** Client Ops Engineering (Kirkland, Marcus, Nico, Sergey, Tamy) and Isaac (Product, onboarding with Client Ops).
  - **Onboarding Support:** Kirkland is the primary contact for all questions, acting as the onboarding buddy.
  - **Access Issue:** New hires are blocked from starting by a lack of GitHub access.
      - **Resolution:** Kirkland messaged Yousef (IT) to grant access.
  - **Onboarding Checklists:** The Linear and Notion checklists are generic. The focus this week is on reading and setup, not coding.

### Core Platform Architecture

  - **Atlas (Customer UI):**
      - The customer-facing tool for running AI pipelines.
      - Replaced Airtable to handle scaling needs.
      - Pipelines are YAML configurations that sequence workflows.
  - **Flow (Backend Repo):**
      - The central repository containing \~150 atomized workflows.
      - Workflows are built using AI-assisted development (Claude Code).
      - Core workflows (Research, Drafting, Post-processing) are used by most customers.
  - **Flow Studio (Dev Tool):**
      - A separate frontend for testing and observability.
      - **Library:** Browse all workflows with auto-generated docs and run samples.
      - **Observability:** Inspect live workflow runs. The "Inspect" button in Atlas links directly to the run's trace in Flow Studio.

### Key Tools & Workflows

  - **Claude Code:**
      - The default and recommended AI coding assistant.
      - The `flow` repo includes a `cursor_rules` file to enforce this preference.
      - Use personal API keys for individual usage tracking.
  - **Linear (Project Management):**
      - The source of truth for engineering tasks and sprints.
      - **Workflow Note:** Customer-facing teams often don't respond in Linear. To get their attention, create a Slack thread and link it to the Linear issue.
  - **Slack (Communication):**
      - The primary communication tool.
      - **Best Practice:** Use public channels for questions. Search (`Cmd+K`) before asking, as answers are often in past threads.
  - **LangFuse (LLM Observability):**
      - Traces every LLM call in production, showing inputs, outputs, and retries.
      - **Use Case:** Essential for debugging non-deterministic AI outputs by seeing the agent's full thought process.
  - **Notion (Documentation):**
      - A vast repository of information.
      - **Recommendation:** Explore the handbook for context. Treat older docs in `Build` and `Delivery` as historical context, not current process.

---

## Action Items

**Kirkland Gee (GrowthX)**
- Ensure Sergey Kaplich, Tamy Macedo, Isaac Dudek read Notion handbook/docs and Client Ops Engineering documentation
- Ensure Sergey Kaplich, Tamy Macedo, Isaac Dudek document onboarding blockers and questions in #onboarding channel
- Ensure Sergey Kaplich, Tamy Macedo, Isaac Dudek get GitHub access via Yousef (IT); then clone and run Flow, Flow Studio, Atlas locally
- Schedule 2-hour workflow-building session for Wed/Thu with Sergey Kaplich, Tamy Macedo, Isaac Dudek; then lead walkthrough

---

## Transcript
**Kirkland Gee:** This meeting is being recorded.

**Kirkland Gee:** Hello.

**Sergey Kaplich:** Hey, hey, how is it going?

**Sergey Kaplich:** Hello.

**Tamy Macedo:** Hello.

**Kirkland Gee:** How are you all doing?

**Sergey Kaplich:** Pretty good.

**Isaac Dudek:** Good to see you all.

**Kirkland Gee:** Isaac, nice to meet you.

**Kirkland Gee:** Tammy and Sarah, I've met both of you guys before now.

**Isaac Dudek:** Yeah, likewise.

**Kirkland Gee:** How's the day going so far?

**Sergey Kaplich:** Feel overwhelmed?

**Tamy Macedo:** So far, so good.

**Isaac Dudek:** Lots of checklists.

**Kirkland Gee:** There's a lot of documentation that's probably not as clear as it should be.

**Kirkland Gee:** So there's probably too many checklists to actually be useful.

**Kirkland Gee:** But hopefully, between talking with me and Daniel and everybody else, can help give you guys a bit of a, like, just some guidance about, like, where to pay attention to more than anything.

**Kirkland Gee:** But just to quickly start off, you guys have been in meetings, a meeting already together today?

**Sergey Kaplich:** Done introductions, all that stuff?

**Sergey Kaplich:** Yeah, in the morning, yeah.

**Kirkland Gee:** Okay, great.

**Kirkland Gee:** Can we do a short version of that for me?

**Kirkland Gee:** I know, Tammy, I met you guys.

**Kirkland Gee:** But, if you can...

**Kirkland Gee:** So just remind me basically where you're from and just give me like one fun fact about you that I wouldn't already know.

**Kirkland Gee:** Preferably unrelated to work.

**Kirkland Gee:** Would love to just learn a little bit more before I start rambling for the next 10 minutes.

**Sergey Kaplich:** Okay, I can start.

**Sergey Kaplich:** My name is Sergey.

**Sergey Kaplich:** I live in New York City, like in suburbs of New York City.

**Sergey Kaplich:** And fun fact, I can play ukulele a little bit.

**Kirkland Gee:** Nice.

**Sergey Kaplich:** Yeah.

**Sergey Kaplich:** I lived in China and there like for a while.

**Sergey Kaplich:** And me and my wife, we went on the streets and we were playing ukulele and people were so happy and they gave us money.

**Kirkland Gee:** So it was fun.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** That's incredible.

**Sergey Kaplich:** I love that.

**Tamy Macedo:** Awesome.

**Tamy Macedo:** I can go next.

**Tamy Macedo:** I'm mostly based in Brazil.

**Tamy Macedo:** Funny fact about me.

**Tamy Macedo:** Hmm.

**Tamy Macedo:** Well, I mentioned that on the Slack channel.

**Tamy Macedo:** I like to build Legos a lot.

**Tamy Macedo:** Um.

**Tamy Macedo:** Yeah.


**Tamy Macedo:** I'm actually very entertained when I'm doing that, and I low-key spend a lot of money on this, more than I should, so yeah, that's a fun fact.

**Kirkland Gee:** Yeah, I have two or three of the, like, sculptures on my shelf over here.

**Kirkland Gee:** One of them broke into, like, a hundred pieces because the shelf literally fell off my wall, and I have not been able to figure out how to put it back together since, but...

**Tamy Macedo:** This already happened to me with one that had, like, 5,000 pieces, and I was like, yeah, it just died.

**Kirkland Gee:** Yeah, if it's not, like, we're never organizing this ever again, for sure.

**Isaac Dudek:** All right, I'm Isaac, based in Los Angeles.

**Isaac Dudek:** Fun fact about me, speaking of expensive hobbies, I'm into snowboarding, and we're going snowboarding with some friends for New Year's this year.

**Kirkland Gee:** Nice.

**Kirkland Gee:** Where would you go to snowboard from L.A.?

**Isaac Dudek:** We go to, like, North...

**Isaac Dudek:** In California, there's a resort area called Mammoth, which is where most of the LA people go versus Tahoe, which is where most of the San Francisco people go.

**Kirkland Gee:** Yeah, that was part of why I asked.

**Kirkland Gee:** Very cool.

**Kirkland Gee:** Awesome.

**Kirkland Gee:** My name is Kirkland.

**Kirkland Gee:** Isaac, we haven't met.

**Kirkland Gee:** So I'm one of the client ops engineers here, kind of stepping into something like a team lead role.

**Kirkland Gee:** I don't know if we're ready to call it that yet, but kind of will be helping you guys out with onboarding, helping make sure you guys have what you need over the next couple of weeks.

**Kirkland Gee:** And then, Isaac, sort of just helping you get a clear picture of how we operate on the client facing side, just so you have that context when you're working on product stuff.

**Kirkland Gee:** I'm based in a little town called Lynchburg, Virginia, so on the east coast of the US.

**Kirkland Gee:** And then kind of have a background partly in marketing, kind of moved into engineering in the last two or three years, more full time, but kind of have this weird hybrid background, which, weirdly enough, is very useful.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** The work that I end up doing most of the time.

**Kirkland Gee:** Fun fact about me, I have an almost 18-month-old son.

**Kirkland Gee:** His name's Lucas, and it's the best.

**Kirkland Gee:** He's also insane, and I can't keep up with him anymore, because he's too wired up.

**Kirkland Gee:** And for expensive hobbies, I play Magic at Gathering quite a lot, and that has become a very, very expensive hobby as of late.

**Kirkland Gee:** But very cool.

**Kirkland Gee:** I've been trying to, literally half of the day, I've been thinking about the best place to start, in terms of kind of giving you guys some direction.

**Kirkland Gee:** So I would do, is there anything that you're like, feel completely lost on that would be like good to clear up immediately?

**Kirkland Gee:** Or would it be helpful for me to just kind of go into an overview of a couple of things?

**Tamy Macedo:** I think for the moment, for me, it would make sense an overview.

**Tamy Macedo:** I don't have a particular question in mind.

**Kirkland Gee:** Okay, cool.

**Kirkland Gee:** Every once in a while, you know you can.

**Kirkland Gee:** It started, you start digging through docs, and you're like, what the heck is happening over here?

**Kirkland Gee:** But if that's not the case, then I will spend a little bit of time just sort of giving you guys some perspective, maybe talking through some documentation.

**Kirkland Gee:** This will be super not as prepared as I'd like it to be, but the nature of a startup.

**Kirkland Gee:** just haven't had time to build all those documents yet.

**Kirkland Gee:** So, I think a good place to start, I sent this this morning, but I'll share this Notion doc, this sort of work in progress client ops engineering document.

**Kirkland Gee:** This was basically just like a brain dump of everything that I could think about related to how we work and how we operate that would be helpful for you guys.

**Kirkland Gee:** I'm sure there's a lot of things that are missing, but I do think it's not a bad place to start in terms of, like, how we think, how we work.

**Kirkland Gee:** So, there's, like, some stuff at the beginning.

**Kirkland Gee:** These are all super rough.

**Kirkland Gee:** Like, I don't feel like any of this needs to be explicitly stuck to going today.

**Kirkland Gee:** Read through some stuff.

**Kirkland Gee:** By the end of the week, be working in our environments, understanding our workflows, how they're structured.

**Kirkland Gee:** By the end of the first month, participating in a sprint and understanding how Atlas works, how our workflows work, like we'll be in a pretty good spot.

**Kirkland Gee:** But again, if things, if you move a little faster than this, a little slower than this, don't worry about it again.

**Kirkland Gee:** So when it comes to how the team is structured, I think you guys know this already, but just to recap, the client ops engineering team is sort of how we're all working for now.

**Kirkland Gee:** Isaac, you'll be moving over.

**Kirkland Gee:** don't know exactly where you'll end up on the product side of things, but I think Daniel, for at least the first couple of weeks, just wants you kind of working with us to see how we operate, how we work with customers, how we work with the delivery team.

**Kirkland Gee:** But there's the client ops team.

**Kirkland Gee:** So that's me, Marcus, and Nico, and now you guys.

**Kirkland Gee:** So super exciting, bringing in some new folks for the first time in a while.

**Kirkland Gee:** And we do a lot of work with our delivery team.

**Kirkland Gee:** And also in our various products and workflow engines and all that kind of stuff.

**Kirkland Gee:** But there's a lot of different projects happening all at the same time.

**Kirkland Gee:** To simplify it down, most of the work that we do is going to be either in Atlas.

**Kirkland Gee:** Have you guys seen that at all yet?

**Kirkland Gee:** Okay.

**Kirkland Gee:** Let me actually start there.

**Kirkland Gee:** So when we're thinking about how our delivery team is servicing clients, right?

**Kirkland Gee:** If our whole deal is that we're enabling our teams to support our customers better with AI workflows, with product, whatever, right?

**Kirkland Gee:** This is the main place that most of them are engaging with.

**Kirkland Gee:** So this is Atlas.

**Kirkland Gee:** Basically, each of our customers has their own sort of workspace.

**Kirkland Gee:** This was originally for a long time, GrowthX was using a product called Airtable when Marcel first started.

**Kirkland Gee:** That was kind of like how he was operating and it eventually just wasn't.

**Kirkland Gee:** enough for the level of scale that we were operating at.

**Kirkland Gee:** It just kind of broke.

**Kirkland Gee:** And so we built Atlas super quickly.

**Kirkland Gee:** Brad and Daniel, who has since moved on, threw this together so fast.

**Kirkland Gee:** it's been iterated on of, you know, for any given customer, a lot of this is still in progress.

**Kirkland Gee:** But Daniel's working on a lot of features that should be shipping, like, in the next couple of weeks for analytics and some other new things.

**Kirkland Gee:** But pretty much ignore a lot of this for right now because it's still sort of being developed.

**Kirkland Gee:** The core thing is people are going come into these little pipeline or these project sections down here.

**Kirkland Gee:** We have a bunch of different pipelines and all these are, are essentially configurations of workflows that we have created over in Flow.

**Kirkland Gee:** So you hear about Atlas, you hear about Flow, you hear about Flow Studio.

**Kirkland Gee:** Those are essentially three different code bases that all kind of interact with each other.

**Kirkland Gee:** Atlas being the main UI.

**Kirkland Gee:** Content OS that are sort of, I think delivery team, customer facing team, whatever you call it, the people that are creating content, you know, they're coming in here, let's just take this article generation pipeline, and they're saying, hey, I want to write an article about cursor versus distraction, I want to give it, it's going to go do a bunch of different steps of different workflows that we have written in our code base, like all of this lives as code, they're kind of interfacing with it through this, it's going to go draft the article, then it's going to add some internal links, it's going to resource it properly, validate some writing guidelines, blah, blah, blah, blah, maybe create some images, there are tons of different, I think we have 150 or something, different workflows that are all sort of maintained separately, and we kind of just stitch all of those together with this simple, I say simple, relatively simple YAML configuration of saying like, hey, here are the steps, we're going to call this workflow with these and

**Kirkland Gee:** Inputs and show them these outputs.

**Kirkland Gee:** Well, don't worry about any of the specifics, just trying to, like, generally.

**Kirkland Gee:** And each of these functions is gonna correlate to, this is our flow repository.

**Kirkland Gee:** You guys will get access to all this stuff.

**Kirkland Gee:** Flow that we have is gonna live down in these folders.

**Kirkland Gee:** Like, let's just say for an example, we wanted to look at, say, SEO, content, right, and there's an article drafting workflow.

**Kirkland Gee:** Again, we'll talk about all this more later, but, like, this workflow, right, this agentic article drafter is what's then called over here with these inputs and all that's running kind of in different places.

**Kirkland Gee:** Is this all kind of making sense?

**Sergey Kaplich:** Yep.

**Sergey Kaplich:** Yeah, a little bit, yeah.

**Kirkland Gee:** Okay.

**Kirkland Gee:** Okay.

**Kirkland Gee:** Again, super high level, but basically, like, you know, a lot of what we're doing is either creating,

**Kirkland Gee:** Creating kind of atomized individual workflows that are then being called in a sequence of steps in order to get whatever piece of content somebody wants out at the end.

**Kirkland Gee:** Some are going to be simpler, some are going to be more complex.

**Kirkland Gee:** Different customers have custom workflows just for things that they need, and then there are a lot of general workflows, right?

**Kirkland Gee:** Like some of the core ones are we have an agentic workflow for researching, for drafting an article, and for post-processing an article.

**Kirkland Gee:** Almost every single customer is going to have those three steps, right?

**Kirkland Gee:** Let's go do some research based on the topic, draft the article based on some guidelines that they have, and then do some sort of post-processing, whether that's maybe checking against the writing guidelines, making sure we're sourcing things correctly, adding internal links, validating that the code in the article is correct, if it's a more technical customer, stuff like that.

**Kirkland Gee:** But each one of those actions that's being taken is some individual workflow.

**Kirkland Gee:** Again, that's been defined somewhere in the flow code-based.

**Kirkland Gee:** And again, I'm not even gonna bother getting into all of this right now, but we have a certain way we go about it.

**Kirkland Gee:** A lot of this is AI-assisted in terms of how we structure these workflows.

**Kirkland Gee:** Like if I'm creating workflow today, I'm writing it in plain English and I'm using quad code to generate pretty much all of the code unless it's doing something like weirdly complicated.

**Kirkland Gee:** We have a lot of instructions and things in place to make that really simple.

**Kirkland Gee:** And then the third sort of code-based or tool you'll hear talked about is Flow Studio, it's studio.growthx.ai.

**Kirkland Gee:** This is essentially just like a separate front end, but you can look at this as a couple of things.

**Kirkland Gee:** One is the library of all those workflows that live in the Flow code base.

**Kirkland Gee:** So any workflow here is...

**Kirkland Gee:** Is going to be visible in this studio.

**Kirkland Gee:** So if we want to go look at SEO, content, right?

**Kirkland Gee:** We were just looking at that agentic article drafting.

**Kirkland Gee:** So this workflow also has like a visual sort of entry in this library.

**Kirkland Gee:** All of this documentation is auto-generated also, but essentially it's just a quick readme R, how they operate.

**Kirkland Gee:** So in this case, right?

**Kirkland Gee:** We're going to kind of get the research from the input, generate a draft, make sure it aligns with the research, and then do some evaluation.

**Kirkland Gee:** If it meets the quality threshold, we send it out to the output.

**Kirkland Gee:** If not, then the agent is going to go like improve that draft over and over again until it gets good enough.

**Kirkland Gee:** You can see like what inputs and outputs are in any given workflow, and you can also run samples of these in the studio.

**Kirkland Gee:** So it's kind of the easiest way to like see what workflows we already have,

**Kirkland Gee:** A lot of times maybe one of our customer success managers is going to say, hey, I need a workflow to do this thing.

**Kirkland Gee:** And it turns out we already have maybe two or three different workflows that already do the thing they're asking they don't know about.

**Kirkland Gee:** It's the easiest way to kind of see.

**Kirkland Gee:** All of these are currently running right now.

**Kirkland Gee:** These are all workflows that are happening from Atlas.

**Kirkland Gee:** So we can just pop into one of these.

**Kirkland Gee:** Like, let's go look at it.

**Kirkland Gee:** Here's another research workflow currently running and it's doing some valuations and that sort of thing.

**Kirkland Gee:** Here's that agentic article draft we were just talking about.

**Kirkland Gee:** So you can see what inputs went into that workflow, either as a pretty format or just the JSON.

**Kirkland Gee:** What the output was right now, this is still running.

**Kirkland Gee:** And this is essentially all just, again, observability.

**Kirkland Gee:** So you can kind of see what's going on if we were over an app.

**Kirkland Gee:** Right?

**Kirkland Gee:** And I wanted to look at one of these individual runs.

**Kirkland Gee:** Let's take this one.

**Kirkland Gee:** And I want to look at the research step.

**Kirkland Gee:** If you click this inspect up here, that opens up the studio URL to that individual execution of the workflow, right?

**Kirkland Gee:** So all these different pieces are like sort of weirdly tied together in a way that doesn't exactly make sense at first, but you start to get used to and you're like, okay, I kind of see how all these pieces play together.

**Kirkland Gee:** And again, don't feel like you have to like retain all of that at all.

**Kirkland Gee:** And just when you see Atlas, when you see Flow, when you see Flow Studio, those are kind of the three things we're talking about.

**Kirkland Gee:** Atlas being the customer team's tool that they're interfacing with day to day.

**Kirkland Gee:** Studio being primarily a debugging and testing tool for us, but sometimes can give some visibility to them as well.

**Kirkland Gee:** Like maybe in Atlas, they see like, for example, they're looking here and they're like,

**Kirkland Gee:** Okay, this is, you know, this has been going for 72 minutes, what's going on, they can click inspect, and they can see, in this case, this one's actually done, there's some weird bug preventing it from going back, stuff like that happens all the time, but is that, generally, you guys still tracking with me, did I lose anyone?

**Sergey Kaplich:** I'm still here.

**Kirkland Gee:** Cool.

**Kirkland Gee:** And then your flow, that's essentially just this primary code base of workflows.

**Kirkland Gee:** and API clients, a ton of other stuff, so it's our backend, that's all running on Render, all of our services are, so if you log into Render, at any point, you should have access, you'll get invites to this through GitHub, at some point, if you haven't already, Atlas, and then Studio, I think, just under the flow project as well, so all those deployments are here, if we make changes, things get pushed here, blah, blah, blah, blah.

**Kirkland Gee:** say.

**Kirkland Gee:** I didn't glad I to say next Okay.


**Kirkland Gee:** Like I said, feel no need to retain or remember any of that, but when it comes back up, you'll at least have seen it.

**Kirkland Gee:** So, again, all three of those repositories are on GitHub.

**Kirkland Gee:** You can clone those.

**Kirkland Gee:** can run all that stuff locally if you're doing testing or if you just want to, like, especially this week, like, if you're just exploring and, like, a good thing would just be to get Flow, Flow Studio, and Atlas all running locally at the same time so you can kind of see, like, how they interact with each other.

**Kirkland Gee:** That might be more complicated than it should be just from, like, outdated readmes and things that might be missing here and there, so I'll help you guys if you need any, like, you know, maybe there's an environment variable that's missing somewhere.

**Kirkland Gee:** Like, I would not be surprised if you run into something that you're like, I'm doing everything right and this isn't working.

**Kirkland Gee:** It's probably not your fault.

**Kirkland Gee:** So, that's all of that.

**Kirkland Gee:** When it comes to how, you we talked about AI-assisted development, mean, AI-led development for that matter.

**Kirkland Gee:** Avoid it's Thank

**Kirkland Gee:** We, you'll find some people use different tools, you know, people have experimented with all kinds of stuff, but generally, like, we are set up to use cloud code, so if you're building workflows in particular, if we go back to the flow repo, I'll actually switch my screen share again, and this would be probably something good to just read up a little bit and kind of see how this is set up, But we have a cursor rules file, but it basically says don't use cursor, is all this was.

**Kirkland Gee:** were using it at one time, but just over time, cloud has just performed a lot better.

**Kirkland Gee:** So if you go in here, you'll see there's a bunch of individual agents that we've set up with specific guidelines for how to write prompts, for how to work with how to build a workflow, how to plan a workflow, so all of this documentation, if you're using cloud code, will just make your life way easier.

**Kirkland Gee:** There, there's also like specific skills.

**Kirkland Gee:** And commands to, for example, debug a workflow, to plan a workflow, all different kinds of stuff.

**Kirkland Gee:** Validating pipelines, like we were looking in Atlas, right?

**Kirkland Gee:** You saw those YAML pipelines.

**Kirkland Gee:** The documentation for those is a little bit finicky, like what's available, what's not available, like what you can actually do here.

**Kirkland Gee:** There's a cloud scale in the flow repo to validate whether that pipeline will work or not, that sort of thing.

**Kirkland Gee:** So generally, unless you're testing something for some purpose or whatever, like cloud code is going to be the default.

**Kirkland Gee:** And I think the idea is we want, everyone will get, you should expect to get like a cloud developer account, invite to your email, set up your own API key, and then use it that way.

**Kirkland Gee:** Versus like logging in, we'll just all use our own API key so we can track that kind of stuff.

**Kirkland Gee:** But like, feel no pressure.

**Kirkland Gee:** to not use it.

**Kirkland Gee:** Please use it as much all the time.

**Kirkland Gee:** It's worth every penny in our experience.

**Kirkland Gee:** Okay.

**Kirkland Gee:** Again, we'll talk a lot more about how to actually build workflows and how that stuff works.

**Kirkland Gee:** But other tools and things to think about.

**Kirkland Gee:** Linear is where all of our issues are tracked.

**Kirkland Gee:** There are a couple different teams set up in there.

**Kirkland Gee:** Tomorrow, you guys got an invite to our cycle kickoff.

**Kirkland Gee:** So you'll kind of see more of how that's structured in that meeting.

**Kirkland Gee:** I won't bother digging into that right now, because it will be pretty clear.

**Kirkland Gee:** We work in two-week cycles on the client ops team.

**Kirkland Gee:** Everything's tracked in Linear.

**Kirkland Gee:** It's honestly such a dream to work with after spending a lot of time in other PM systems.

**Kirkland Gee:** Like, I don't know what you guys come from, but Linear is just the best.

**Kirkland Gee:** Slack is where a lot of communication happens.

**Kirkland Gee:** There's something I say in here that I think is worth calling out.

**Kirkland Gee:** Linear is how we work.

**Kirkland Gee:** You can talk to all of the customer-facing people in Linear.

**Kirkland Gee:** They very often will not respond to you in linear, right?

**Kirkland Gee:** Like that's just not where they live day to day.

**Kirkland Gee:** So very, very often what I end up doing is creating a Slack thread in a channel that's relevant to that customer and then linking it to the linear issue, which is super easy to do.

**Kirkland Gee:** And again, this is not going be relevant probably even this entire week, but just know that Slack is the way to get ahold of people most of the time.

**Kirkland Gee:** I think most of us on the engineering team are pretty active in linear, but that's kind of where that ends, I think, a lot of the time.

**Kirkland Gee:** Okay.

**Kirkland Gee:** We talked about GitHub stuff, Cloud Code, IDE.

**Kirkland Gee:** I mean, feel free to use whatever.

**Kirkland Gee:** You'd prefer VS Code.

**Kirkland Gee:** Cursor's fine.

**Kirkland Gee:** Anything like that.

**Kirkland Gee:** There's a Cloud Code extension that works in any VS Code fork that's really nice.

**Kirkland Gee:** I often use Cloud Code in my terminal.

**Kirkland Gee:** Like none of that matters.

**Kirkland Gee:** Whatever is more comfortable for you.

**Kirkland Gee:** A couple of things we have set up.

**Kirkland Gee:** Sentry is doing like issue.

**Kirkland Gee:** Monitoring for Atlas.

**Kirkland Gee:** I don't think it's set up for anything else right now.

**Kirkland Gee:** On the workflow side, we use LengthFuse for monitoring all of our workflow executions.

**Kirkland Gee:** So, have you guys ever used LengthFuse before or any kind of LLM eval?

**Kirkland Gee:** Okay.

**Kirkland Gee:** This is one of those things that, like, I'm going to take a minute to show you today because I know a lot of people that, like, didn't know this existed for the first three or four months they were here, and it would have saved them a lot of headache.

**Kirkland Gee:** Because, again, a lot of our workflows, a lot of what we're doing is not, like, building new business logic.

**Kirkland Gee:** It's just tweaking prompts and, like, working with LLMs to get whatever output that we want.

**Kirkland Gee:** And LengthFuse is, remember how I'm supposed to log into LengthFuse.

**Kirkland Gee:** Should just be this.

**Kirkland Gee:** Okay, great.

**Kirkland Gee:** It's basically tracing every single LLM call that's happening across all of our workflows in production.

**Kirkland Gee:** So, anytime I want to

**Kirkland Gee:** We looked at Flow Studio as a place you can go see the workflow execution, the steps, blah, blah, blah.

**Kirkland Gee:** But let's say that I know of a specific workflow I'm working on.

**Kirkland Gee:** You know, I just want to look at my, I think I can just, no, I can't do that.

**Kirkland Gee:** Let's just look at this agentic article draft workflow.

**Kirkland Gee:** And again, you can figure out more of how this is set up.

**Kirkland Gee:** But here I'm just saying, hey, for my trace name, I just want to look at traces of this agentic article draft workflow.

**Kirkland Gee:** And then I want to look at the one that happened, you know, X time.

**Kirkland Gee:** This one looks like it just didn't.

**Kirkland Gee:** Okay.

**Kirkland Gee:** I can go look and see, hey, here was the exact input to that workflow.

**Kirkland Gee:** There's the, yeah.

**Kirkland Gee:** And here's the response.

**Kirkland Gee:** Here's all the details.

**Kirkland Gee:** This one looks a little, I feel like something's not being tracked on this unless this just works.

**Kirkland Gee:** Worked on the first try.

**Kirkland Gee:** This is going back to like, ah, there we go.

**Kirkland Gee:** This is what I would have expected to see of like, we're gonna generate a draft.

**Kirkland Gee:** This probably didn't get evaluated highly enough.

**Kirkland Gee:** And so it generated a second draft.

**Kirkland Gee:** And then there's some planner and then it's improving.

**Kirkland Gee:** You can see the inputs and outputs of each of these steps.

**Kirkland Gee:** And at any point, you can also like go create a playground and tweak that input or output and rerun everything with all the context that was happening.

**Kirkland Gee:** This is more useful, I mean, you're trying to test, trying to understand like what's going on.

**Kirkland Gee:** If you want to test if a different model maybe is gonna perform better or worse.

**Kirkland Gee:** I don't use this like all the time, but just knowing that this is there at any point, customer execution that you're like, it should be doing this and it's just not.

**Kirkland Gee:** Playing Fuse is super, super useful.

**Kirkland Gee:** Super helpful to track all that stuff down.

**Kirkland Gee:** Okay.

**Kirkland Gee:** That was that.

**Kirkland Gee:** This isn't super important.

**Kirkland Gee:** Temporal, I'll get to in a minute.

**Kirkland Gee:** Slack, linear, and then there's a lot of documentation in Notion.

**Kirkland Gee:** You guys should have already probably gotten into Notion and seen some of the stuff in there.

**Kirkland Gee:** There's so much, like, this week, like, prioritize spending a lot of time just digging and reading and absorbing information in here from all different places.

**Kirkland Gee:** Again, a lot of it is, like, pretty laid out in the handbook section of, like, big picture stuff.

**Kirkland Gee:** It's definitely all worth reading, all this stuff from Marcel.

**Kirkland Gee:** And then if you go down into these areas of build and delivery, I'd say our documentation here is, like, it's okay.

**Kirkland Gee:** I wouldn't, like, rely on really anything in any of this as, like, you know, this is exactly correct to what's happening today.

**Kirkland Gee:** But I think there's a lot of useful context.

**Kirkland Gee:** Like, there's documents.

**Kirkland Gee:** Talks about different pieces of projects that we were working on at certain times, or just, like, things that we were looking into for different things like that.

**Kirkland Gee:** That's a really confusing sentence, but there's a lot of information here.

**Kirkland Gee:** So, again, don't feel like you need to, like, memorize, but just generally, like, exploring, perusing is a valuable use of your time, for sure.

**Kirkland Gee:** Where was I?

**Kirkland Gee:** Okay, that's all of that.

**Kirkland Gee:** Talked about debugging stuff.

**Kirkland Gee:** There's a couple of resources linked here.

**Kirkland Gee:** We have access, there's a login and 1Password for this AI engineering book, if you haven't read it, by Chip Nguyen, I think is how you pronounce her last name.

**Kirkland Gee:** In particular, the chapters on, like, product engineering and evaluations are super, super good.

**Kirkland Gee:** And you can just log in with your 1Pass and read this.

**Kirkland Gee:** It's highly recommended.

**Kirkland Gee:** It's recommended.

**Kirkland Gee:** And at least the prompt engineering chapter, it helped me a lot, just sort of understanding how to think about that stuff.

**Kirkland Gee:** And then, yeah, there's a couple things in here on some of, like I mentioned, the cloud code subagents, or how we think about prompting.

**Kirkland Gee:** It's not a ton, but like just a few things to think about.

**Kirkland Gee:** We don't write a lot of tests for workflows, at least not unit tests, because so much of it is non-deterministic, and based on what an LM decides to do, that like a test isn't really a good test if it's just testing a, like a static input to the workflow, because it's going to change depending on what the LM sends us back, so we do a lot more of just like testing in the real world, so to speak.

**Kirkland Gee:** And then as you go this week, like this is mostly a request from me, but like document things as you go, things that are, things that you're not clear on, things that don't make sense, places where you feel like information

**Kirkland Gee:** Again, have not brought new people onto the ClientOps team since May or June or something, and so we're bringing you guys on and looking to probably bring a few other people on in the next, you know, three to six months, something like that.

**Kirkland Gee:** And so any ways that you can help us both clarify things for you and clarify things for people in the future will be super appreciated for me.

**Kirkland Gee:** And then, yeah, if you're getting stuck at any point, a couple places to look, whatever repo you're in, the readme is pretty comprehensive.

**Kirkland Gee:** There may be some places that, like, need to be updated or whatever, but, like, should be pretty straightforward.

**Kirkland Gee:** And then talking to Cloud Code about the repo that you're in is a really, really good way to, like, get a feel for how things are set up, how things are organized, what the patterns are being used there.

**Kirkland Gee:** Notion is there to search up for things.

**Kirkland Gee:** And then in Slack, for the most part, I'm going to see if you have questions, if you have things in that onboarding channel.

**Kirkland Gee:** Don't you Okay, Thank

**Kirkland Gee:** Feel free to just shoot messages or questions there for this week and probably for next week, too, rather than, like, trying to figure out exactly where you need to go for something, just asking the onboarding channel, ping me, at me, and my plan is to kind of be available to help you guys with anything you need for the next week or two as my sort of top priorities to help you guys get onboarded and get what you need.

**Kirkland Gee:** Some other stuff in here.

**Kirkland Gee:** I don't need to go through any of that.

**Kirkland Gee:** Okay.

**Kirkland Gee:** That was a lot of information, so I'm going to take a beat.

**Kirkland Gee:** Any immediate questions that come to mind?

**Kirkland Gee:** Anything you want to dive a little bit deeper into from any of that super high-level overview stuff?

**Tamy Macedo:** Honestly, no.

**Kirkland Gee:** Okay, Isaac, anything from you guys you're thinking about?

**Sergey Kaplich:** No, no, no, don't have any questions right now.

**Sergey Kaplich:** I mean, like, as you told, like, a lot of information, so just a little bit time to process it, but overall...

**Kirkland Gee:** Like, don't have any questions for now.

**Kirkland Gee:** Okay.

**Isaac Dudek:** Yeah.

**Isaac Dudek:** Same here.

**Kirkland Gee:** Okay.

**Kirkland Gee:** Let me just take a beat and think for a second.

**Kirkland Gee:** If I were you guys, what's the next thing that I want to make sure somebody told you, right, if I was in your shoes?

**Kirkland Gee:** I guess, would it be, because I know you guys have a meeting with Daniel in a little bit, and he's going to go over a bunch of stuff.

**Kirkland Gee:** And I don't want to overwhelm you with too much information.

**Kirkland Gee:** Where are you guys at on logistics onboarding stuff when it comes to, like, getting access to everything, getting invites to Slack channels, like, all that basic stuff?

**Kirkland Gee:** Is that going well?

**Kirkland Gee:** Do you have any of that?

**Kirkland Gee:** Do you have all of that?

**Kirkland Gee:** Like, I realize that could be a really wide spectrum.

**Sergey Kaplich:** The only thing I'm missing right now is, like, GitHub access.

**Sergey Kaplich:** And overall, I think everything is set already for me.

**Sergey Kaplich:** At least I found almost...

**Sergey Kaplich:** Everything, yeah, just GitHub fixes.

**Tamy Macedo:** Okay, Yeah, same, same.

**Isaac Dudek:** Yeah, I also need GitHub, but I guess the issue is I don't know what I'm missing, right?

**Isaac Dudek:** Like, I think I was invited to a lot of stuff automatically on Slack.

**Isaac Dudek:** was added to groups, which added me to channels, but are those all the ones I need?

**Kirkland Gee:** I don't know.

**Kirkland Gee:** Yeah, that's a very, very good question.

**Kirkland Gee:** So, yeah, and I think you guys are in most of the places.

**Kirkland Gee:** Like, you guys got added to the, like, main EPD channel.

**Kirkland Gee:** I'm just going to check a few of them that are probably worth checking.

**Kirkland Gee:** Yeah, that one, the Client Ops EPD Lane channel.

**Kirkland Gee:** There's that onboarding channel.

**Kirkland Gee:** There's also, like, you guys will see the way our Slack is set up.

**Kirkland Gee:** And depending on where you come from, this might make total sense, but it's a little bit different.

**Kirkland Gee:** Like, we, there's a lot of channels.

**Kirkland Gee:** don't I

**Kirkland Gee:** And most of them are trying to be isolated to a very specific use case, right?

**Kirkland Gee:** It's like every customer, for example, has an IMT and EXT version of their channel.

**Kirkland Gee:** So one that's just internal team members and one that includes, you know, their team.

**Kirkland Gee:** You don't need to worry about any of those right now because you're not working with any customers.

**Kirkland Gee:** But as you go to like, let's say you take on a ticket next week and it's for, you know, Okta, for example.

**Kirkland Gee:** All you have to do is just command K in Slack, go look for Okta, join that channel, and send something.

**Kirkland Gee:** Like pretty much everything is public.

**Kirkland Gee:** So don't feel like you need to like, get in every single channel right now, because people will just add to you as needed.

**Kirkland Gee:** And again, anytime, if you want to just like search for anything with EPD in it, like that's going to be most of the relevant channels, at least for the short term.

**Kirkland Gee:** And then as things come up, you'll want to get into the customer channels that are relevant.

**Kirkland Gee:** But at least for now, it's not going to be too much.

**Kirkland Gee:** And then you guys are in the

**Kirkland Gee:** Vimear, yes, and the only thing you need is GitHub, okay, let me just send a message in that channel to Yousef, he's gonna be your IT guy for anything access related, if you're having any issues there.

**Kirkland Gee:** Okay, so there was a message to try and get that resolved, because I think that's like a big part of how I spent my first couple weeks was just like reading through the code base, you know, and just like trying to understand how things are, like, the quicker you guys can get in there and start setting

**Kirkland Gee:** And up and playing around, the easier your life will be.

**Kirkland Gee:** Because reading documentation about code is not the same as actually looking at the code itself.

**Kirkland Gee:** Okay.

**Kirkland Gee:** That's all of that.

**Kirkland Gee:** I think that makes sense.

**Kirkland Gee:** And then can you guys, what is, do you have like an onboarding checklist that you were given in Notion or something like that?

**Tamy Macedo:** Yeah, we have one in linear.

**Sergey Kaplich:** Yeah, and in Notion as well.

**Kirkland Gee:** think it's everywhere.

**Sergey Kaplich:** Okay.

**Sergey Kaplich:** They're almost the same, yeah.

**Kirkland Gee:** You have one in linear and one in Notion.

**Sergey Kaplich:** Yeah, I guess we have like something like that, yeah.

**Kirkland Gee:** Okay.

**Kirkland Gee:** I just want to take a, I want to make sure I know where those are so I can like see what's happening.

**Kirkland Gee:** And make sure that's all clear.

**Kirkland Gee:** I see.

**Kirkland Gee:** Those are the milestones.

**Kirkland Gee:** Here's the, okay.

**Kirkland Gee:** Very cool.

**Kirkland Gee:** Yeah, Team Directory.

**Kirkland Gee:** So one thing to note, just so you guys know, when it comes to these checklists, those checklists are the same, they get auto-generated, they're the same for engineering and for delivery.

**Kirkland Gee:** Some of the stuff in this is, like, relevant for you, but, like, may not be as straightforward as it is, you know, for someone on the delivery side.

**Kirkland Gee:** So, like, you know, for example, you know, a one-to-one with your manager and a one-to-one with your onboarding buddy.

**Kirkland Gee:** You can essentially think of me as your onboarding buddy for the first couple of weeks, just because our team's a lot smaller than theirs, right?

**Kirkland Gee:** Like, they have, like, 40 or 50 people.

**Kirkland Gee:** We have, like, 12.

**Kirkland Gee:** And then in terms of manager, Daniel is, like, all of your manager.

**Kirkland Gee:** For the first couple of weeks, most things that you need that aren't, like, payroll-related, you can ask me first.

**Kirkland Gee:** Just because Daniel is going be harder to get a hold of.

**Kirkland Gee:** know he's doing...

**Kirkland Gee:** don't doing...

**Kirkland Gee:** I

**Kirkland Gee:** Way more things than I have my hands in, so like, any questions you have, literally anything, just ask me, and I can probably help you figure it out, and if I can't, I probably know who can help you figure it out, and then otherwise, I think there's a ton of just like, read and watch stuff in here, and I really would say like, do all of that this week.

**Kirkland Gee:** Like, prioritize reading and watching that stuff over like, trying to get started on actual work, or trying to, like, there is no expectation for you guys to write a single line of code this week at all.

**Kirkland Gee:** If you want to, if that's like a helpful way for you to learn, awesome, but like the expectation is just to like, ingest, take notes, ask questions, and get clear on everything that you need to get clear on.

**Kirkland Gee:** So then hopefully next week, we can really start like, jumping into some more things, with more context in mind.

**Kirkland Gee:** So- So-

**Kirkland Gee:** Plan from here.

**Kirkland Gee:** You guys have a ton of stuff to work through.

**Kirkland Gee:** I know I put a, I'm working on, if I haven't already, putting a meeting on our calendars to kind of touch base towards the end of the week and just like see how things have gone.

**Kirkland Gee:** We'll have our Climops kickoff tomorrow to kind of talk through issues and tickets and that sort of thing.

**Kirkland Gee:** All hands is tomorrow as well.

**Kirkland Gee:** Probably Wednesday or Thursday.

**Kirkland Gee:** I don't have it on there yet because we'll see.

**Kirkland Gee:** I'm still kind of working on cycle planning.

**Kirkland Gee:** But what I'm thinking is I'll pick something that's kind of more straightforward, not a super complicated issue, maybe a workflow that needs to be generated, set up a meeting for all of us to kind of work on that together where more or less like I can kind of walk through both how I think about it, how we build the workflow, how we get it like all the way through to production and we can just do that in like a two hour session or something, either Wednesday or Thursday, but that is like the closest you guys need to get to making workflows or anything this week.

**Kirkland Gee:** But that's sort of my rough plan is to let you guys like do your own thing.

**Kirkland Gee:** Explore, learn, and we'll do that Wednesday, Thursday, check in on Friday, and then next week, hopefully, I can give you guys something to kind of tackle on your own and take your time working through, but that's sort of the timeline we're working with.

**Kirkland Gee:** Does that all make sense?

**Kirkland Gee:** Feel clear to you guys?

**Tamy Macedo:** Yep.

**Sergey Kaplich:** Yeah, absolutely.

**Kirkland Gee:** Sounds great.

**Isaac Dudek:** Awesome.

**Isaac Dudek:** Works for me.

**Kirkland Gee:** Very cool.

**Kirkland Gee:** Well, I won't take up these last five minutes of your time.

**Kirkland Gee:** I'll let you guys go and read for the next three days.

**Kirkland Gee:** And again, like I said, please in that onboarding channel, just a little thing you'll see about the way we operate in Slack is like generally don't DM people unless it's something that needs to be sensitive or needs to be private, which in which case, obviously.

**Kirkland Gee:** But if you're just like asking for information, like don't feel like you need to DM someone because you don't want to ask a question or look stupid in public, like, please don't worry about that.

**Kirkland Gee:** Like, ask the question in a public channel, because then probably someone else was thinking about it and they get the answer too.

**Kirkland Gee:** And also if someone needs to look for it later, they can.

**Kirkland Gee:** And on that note, you're ever looking for something, before you ask a question, just do a quick command F in Slack and search for it.

**Kirkland Gee:** You might be able to find an answer to the question you're looking for because there's so much in public channels over the time we've been working.

**Kirkland Gee:** Yeah, ask questions.

**Kirkland Gee:** Let me know what you guys need.

**Kirkland Gee:** And otherwise, have a great rest of your first day.

**Sergey Kaplich:** Awesome.

**Tamy Macedo:** Thank you so much.

**Kirkland Gee:** Thank you.

**Isaac Dudek:** Thanks, everyone.

**Kirkland Gee:** Talk soon.

**Sergey Kaplich:** Bye.

**Sergey Kaplich:** Bye.

**Sergey Kaplich:** Bye.
