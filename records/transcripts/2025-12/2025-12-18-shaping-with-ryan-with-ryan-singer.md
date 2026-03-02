# Shaping with Ryan with Ryan Singer

<metadata>
date: 2025-12-18
time: 16:01 UTC
duration: 185 minutes
organizer: daniel@growthxlabs.com
participants: Marcel Santilli, Ryan Singer
fathom_recording_id: 109763779
fathom_url: https://fathom.video/calls/511554937
share_url: https://fathom.video/share/HbatPr682Usc3yUfScqhLsD4zukgjXns
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Marcel Santilli and Ryan Singer defined the problem and scope for building a feedback loop system to fix a critical bottleneck in GrowthX's content delivery. The core issue is that editor interventions and client feedback happen in Google Docs, making them invisible to the AI system and preventing learning. The January project focuses on a hybrid feedback tool—combining inline comments for specific errors and structured feedback for higher-level issues—plus an internal "Simulated Client Review" for editors to self-check against a "digital twin" of client preferences before external review.

---

## Context

This was a strategic working session between Marcel Santilli (GrowthX founder/CEO) and Ryan Singer, a noted product strategist and consultant who has advised companies on shaping and scoping ambitious product initiatives. The meeting occurred in mid-December 2025 as GrowthX was preparing to launch a major product initiative in January to address a scaling bottleneck in its content delivery operations. Marcel had previously worked with Ryan and wanted to leverage his expertise to validate the problem definition and scope a solution architecture. The discussion centered on GrowthX's core business—delivering high-quality B2B content at a 10x cost advantage through Marcel's strategic process and AI workflows—and a specific dysfunction: when client engagements transition from an intensive 8-week sprint phase (handled by a dedicated "hero editor") to a 12-month ongoing phase (handled by a new editor), quality and turnaround time deteriorate due to loss of undocumented context and editor expertise.

---

## Relevance

- **To GrowthX Delivery:** Validates the hypothesis that the sprint-to-ongoing handoff is a critical failure point causing 5+ hour turnaround times on articles when the baseline is 30 minutes. The hybrid feedback tool design (inline comments + structured feedback quiz) directly addresses two failure modes: system failures to apply correct inputs vs. incorrect inputs at the brief stage. The "digital twin" framing—positioning feedback capture as building a proprietary asset—may improve client buy-in and adoption. January scope is tightly bounded to feedback tool + internal simulation; client sign-off and advanced calibration are deferred to reduce complexity.

- **To GrowthX Product/Platform Development:** Ryan Singer's input shaped thinking about feature prioritization and scope discipline. The decision to split "Simulated Client Review" (internal QA tool for editors) from client-facing feedback collection prevents premature complexity and allows both features to mature independently. Monitoring simulations-per-editor will create the first direct signal on whether the tool is actually changing editor behavior.

- **To GrowthX Business Development:** Success with this system unlocks the ability to scale the editor pool beyond the current 60 people without proportional quality deterioration. This directly improves unit economics on ongoing engagements and reduces client churn from post-sprint quality dips—both material levers for retention and expansion revenue.

---

## Overview

- **The Core Problem:** The current workflow is a "black box" where editors use Google Docs, making client feedback inaccessible to the system. This breaks the AI learning loop and prevents scaling.
- **The Bottleneck:** This process fails during the handoff from the 8-week "sprint" (led by a "hero editor") to the 12-month "ongoing" phase (led by a new editor). The new editor lacks the undocumented context, causing quality drops, slow turnaround, and client churn.
- **The Solution:** A hybrid feedback tool in the platform will capture client comments (specific errors) and structured feedback (higher-level issues) to create a "digital twin" of the client's preferences.
- **The Scope:** The January project is tightly focused on building this feedback loop and a "Simulated Client Review" tool for editors. It explicitly excludes client sign-off and advanced quality calibration.

---

## Key Topics

### The Problem: A Bottleneck in the Content Workflow

  - **Current State:** GrowthX delivers high-quality content at a 10x cost advantage ($0.10–$0.20/word vs. $1.50/word) by combining Marcel's strategic process with AI workflows.
  - **The Bottleneck:** The editor team (60 people) is a "black box." Editors work in Google Docs, making their interventions and client feedback invisible to the system.
  - **The Critical Failure Point: The Handoff**
      - **Sprint Phase (Weeks 1–8):** A "hero editor" (e.g., Ada) manages the client. They internalize feedback from calls and Google Doc comments, making undocumented, heroic edits.
      - **Ongoing Phase (12-Month Contract):** A new editor takes over. Lacking the undocumented context, they struggle to meet the client's quality bar.
      - **Result:** This leads to slow turnaround (e.g., 5 hours/article vs. 30 mins), client churn, and an inability to scale capacity.

### The Solution: A Hybrid Feedback Tool

  - **Goal:** Capture client feedback directly in the platform to make it a structured, reproducible data signal for the AI.
  - **Hybrid Approach:** The tool will combine two feedback methods:
    1.  **In-line Comments:** For specific, localized errors (e.g., "replace 'help' with 'support'").
    2.  **Structured Feedback:** A quiz-like section for higher-level issues (e.g., "Did we use the right sources?").
  - **Rationale:** This captures two distinct types of failure:
      - **Comments → Application Failure:** The system failed to apply correct inputs.
      - **Structured Feedback → Input Failure:** The initial inputs (brief, research) were wrong.
  - **Client Framing:** Position the tool as building a "digital twin" of the client's experts. This frames the feedback process as an investment in a valuable, proprietary asset.

### The Scope: January Project & Future Work

  - **January Project Scope:**
      - **Primary Goal:** Ensure new editors do not repeat mistakes already flagged by the client.
      - **Core Feature:** The hybrid feedback tool for clients.
      - **Internal Tool:** A "Simulated Client Review" for editors to self-check drafts against the "digital twin" before client review.
      - **Monitoring:** Track the number of simulations run per editor to ensure process adherence.
  - **Out-of-Scope for January:**
      - **Client Sign-off:** A formal approval step is a separate project.
      - **Advanced Quality Calibration:** The "quiz-like" calibration guide shown for Engine.com is a separate, future initiative.

---

## Action Items

- **GrowthX Team:**
    - Share the session recording and whiteboard with the development team.
    - Focus the January project on the defined scope: the hybrid feedback tool and the "Simulated Client Review."
    - Defer work on client sign-off and advanced calibration to separate projects.
- **Ryan Singer:**
    - Send the whiteboard diagram to the GrowthX team.

---

## Transcript
**Marcel Santilli:** Boom, good.

**Marcel Santilli:** We literally are like using Fathom and then we try to like turn from Fathom to then, you know, then we're testing Fireflies and then we're testing another one and then now they all join, you know, it's like, dang it.

**Ryan Singer:** And there's like very little downside to just throwing more at it, you know, because it's just different ways of capturing stuff.

**Marcel Santilli:** So, yeah, yeah, but anyway, so nice to meet you and I feel like I already know you from watching all the videos and stuff.

**Ryan Singer:** Oh, okay.

**Ryan Singer:** Nice to meet you too.

**Ryan Singer:** I enjoyed hearing the whole backstory about everything you guys have been doing when I met up with Daniel, you know, last week.

**Marcel Santilli:** So, you know, looking forward to digging in together.

**Marcel Santilli:** Yeah, yeah, that's been awesome, man.

**Marcel Santilli:** I'm like, I said all the time, like, it's one of the best parts about starting the company is getting to work with Daniel too.

**Marcel Santilli:** So, it's been really fun, know, hard as hell, but fun.

**Marcel Santilli:** That was sweet.

**Marcel Santilli:** They're gone, basically.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** I was up until like one in the morning last night working on a pricing and monetization strategy for this other product.

**Ryan Singer:** launching, check that, you know.

**Ryan Singer:** Oh, man.

**Ryan Singer:** There's, I mean, a lot of stuff going on, right?

**Ryan Singer:** And also a lot of time pressure in the space you're in.

**Marcel Santilli:** Yeah, it feels like right now, I don't know if you're seeing this with other companies you've talked to, but it just feels like everything is so crazy, accelerated, man.

**Marcel Santilli:** It just feels like people can catch up to whatever you do so fast, you know, and it's like a group of three people could like catch up to something in like a month, it feels like, you know.

**Marcel Santilli:** Yeah.

**Ryan Singer:** Yeah, I guess when it's easy to see on the surface what to copy, then yes, right?

**Ryan Singer:** It's a question of whether there is some subtlety there or not, you know, and I think that's also part of the interesting question as we get into like, for example, what I looked at the brief.

**Ryan Singer:** Daniel, that you sent for today, and this is one of those things where like there can be these little experience things sometimes that are the reason why you always go here and you don't go there.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Of course, there's like a lot of low-hanging fruit, but when you start to get into like these kind of flows, there's some pretty interesting kind of experience questions, and it's, yeah, it's not always just raw functionality, right?

**Ryan Singer:** Like, so, but let's see.

**Ryan Singer:** Let's see.

**Ryan Singer:** We'll have to dig in and see where it's at.

**Marcel Santilli:** Yeah, that sounds good.

**Marcel Santilli:** One thing I wanted to do, what is I wanted to do, Daniel was saying, like, would it help to just do a super quick, like, background on me a little bit, or do you feel like, either way, it's okay to also just jump in?

**Ryan Singer:** Might be cool, yeah.

**Ryan Singer:** I got a really nice background from Daniel when we talked a week ago, but I would be curious just to kind of get your version, you know, of course, you don't.

**Marcel Santilli:** Sometimes there could be differences.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** Well, I'll do just the super, super fast.

**Marcel Santilli:** But the T.O.N.R.s paid my way through college doing graphic design and web design.

**Marcel Santilli:** So I like a Photoshop geek, you know, and they're going into marketing.

**Marcel Santilli:** But it was back when Flash websites were a thing, know, and all that good stuff, you know, but never was a good developer.

**Marcel Santilli:** I always gravitated more towards like design and creative and, you know, and then I was at IBM and started really building these kind of content programs.

**Marcel Santilli:** And it was like just every single step of my career, that's what I did.

**Marcel Santilli:** Like at IBM, I built a site called securityintelligence.com.

**Marcel Santilli:** was all like around like helping brands be more like publishers and build distribution.

**Marcel Santilli:** And then at HP, I built a contributor network that grew to like a million visitors a month.

**Marcel Santilli:** And so it's like, I just kept doing it in different ways, shape or form.

**Marcel Santilli:** And then I was lucky enough to be at a couple of startups.

**Marcel Santilli:** And.

**Marcel Santilli:** I up doing well, despite me, like HashiCorp, ServiceSight, and then Skill.ai.

**Marcel Santilli:** And I think there was always kind of like this pressure and like, you know, of got to find ways to grow and grow organically and grow more sustainably.

**Marcel Santilli:** And I always just kept going back to just like content and building your own distribution for brands.

**Marcel Santilli:** And then eventually, like, I started building AI workflows after, in my last job at DeepGram.

**Marcel Santilli:** And that's when we, 24XR traffic and really blew up in a good way.

**Marcel Santilli:** So then I started teaching workshops, you know, and then that's when like, we had about 170 people that paid like 500 bucks to come to these workshops.

**Ryan Singer:** Oh, interesting.

**Ryan Singer:** started with workshops.

**Ryan Singer:** Okay.

**Marcel Santilli:** Uh-huh.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And then like, education was always like, really important to me.

**Marcel Santilli:** And it's just like, I enjoy it.

**Marcel Santilli:** get energized from it.

**Marcel Santilli:** But really, the company started with people just saying, hey, can you just do this?

**Marcel Santilli:** What you're teaching me right now, this is awesome.

**Ryan Singer:** I get it.

**Marcel Santilli:** I don't have the time and I need help.

**Marcel Santilli:** And so that's like, that's kind of like what started growthx.

**Marcel Santilli:** And then since then, and especially when Daniel joined, was just like trying to really like figure out, like solve first a workflow problem because these local tools, like building workflows, which is not scalable, right?

**Marcel Santilli:** Yes.

**Ryan Singer:** And it's like the one person, the one person whose brain is in the workflow can do it, right?

**Ryan Singer:** But it doesn't scale up beyond that into something that you can like teach and get other people to participate in, right?

**Marcel Santilli:** Exactly.

**Marcel Santilli:** And like one last thing maybe I'll mention is just that I had built a lot of like wrap-offs functions.

**Marcel Santilli:** And so I had built a lot of like the old school like workflows, if you will.

**Marcel Santilli:** And, and like, it just kind of felt like that, right?

**Marcel Santilli:** Where they had like one person, like you said, that just knew everything.

**Marcel Santilli:** And this thing just looked like a real.

**Marcel Santilli:** Really messy couple of, and it's like, man, this is insane, and no one would use it, no one would know how to maintain it, you know.

**Marcel Santilli:** But the one that used that with next, I would say.

**Marcel Santilli:** Yeah, yeah, so, but anyways, that's just a little bit of the context, hopefully it's helpful.

**Marcel Santilli:** Yeah, I also heard that there was.

**Marcel Santilli:** second, my wife is dropping the dogs in the bed, so sorry, called like three times.

**Ryan Singer:** Calls from the wife are important, they get top priority.

**Marcel Santilli:** Are you feeling better from the old?

**Ryan Singer:** Yes, finally, you know, it's still there, but it's like over the worst part of it, yeah, yeah.

**Ryan Singer:** Nice.

**Ryan Singer:** Yeah.

**Ryan Singer:** So, you guys seem pretty awake, you know, for being early in the morning, so that's good at least.

**Marcel Santilli:** Yeah, Marcel arrives at 6 a.m.

**Marcel Santilli:** usually, but he has a small daughter and doesn't, he wakes up super early.

**Marcel Santilli:** I know, I'm on the opposite side.

**Ryan Singer:** Okay, so you're stretching it today.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** How would you – go ahead.

**Marcel Santilli:** No, go ahead.

**Marcel Santilli:** No, no, I was going to ask that – like, if you work with a lot of companies on the hard times.

**Ryan Singer:** So far, I have one – my main client right now is on East Coast time, which is super – like, I have way more overlap, you know.

**Ryan Singer:** And then I've got one other client that's on Pacific time, you know.

**Ryan Singer:** So – but thankfully, we didn't have too much booked, you know, like, this week.

**Ryan Singer:** So I have these hours available, you know.

**Ryan Singer:** It's like – it's – that's hard, you know, because, like, if – I mean, after you guys, like, it's already – you know what I mean?

**Ryan Singer:** It's like 7 or 8 p.m.

**Ryan Singer:** here, depending on daylight, you know.

**Ryan Singer:** And so I usually – I usually basically kind of get one – there's one window, you know, for Pacific each day.

**Marcel Santilli:** Yeah.-hmm.

**Marcel Santilli:** Do you want to cover the –

**Ryan Singer:** Well, I had one question around trajectory, which was just, and then I think we can dive pretty quick into the actual problem here, is the AI piece of the story.

**Ryan Singer:** So, Marcel, the way that you just told it was more around what it sounded to me like your domain expertise around kind of organic growth and, like, content first and focusing on building distribution that way.

**Ryan Singer:** Like, and then Daniel had mentioned that, that I think if I remember right, like, you were in a situation where, like, normally you would have had, I don't know if it was at DeepGram or somewhere else, where normally you would have had, like, more people and more time, but you had to kind of, you had to, like, kind of get things kicked up, like, under a compressed timeline, and then you built an AI workflow to do that.

**Ryan Singer:** And then that was kind of, like, is there some kind of, like, is there, like, an origin story to, like, you know, how much of this is, um...

**Ryan Singer:** How much of this is like AI is the new way, therefore we're doing it versus like you saw like some significant difference?

**Marcel Santilli:** Yeah, I think it's a little bit of both.

**Marcel Santilli:** So every single step in my career to build these content engines for companies, I started by hiring managing editors from publications.

**Marcel Santilli:** And then I would teach them how to come up with a brief, how do I figure out what topics, like really nail the audience we're going after, and then go and execute against those briefs.

**Marcel Santilli:** And in scale publication, we would do like 20 articles a week, all manual, right?

**Marcel Santilli:** Except for like when I was at HB, we spent like 2 million in the first year to produce, you know, 20 articles a week, you know, essentially the equivalent of writing two Bibles that year, right?

**Marcel Santilli:** And, but then by year three, like the traffic was like really ramping up.

**Marcel Santilli:** But every time it's like really, really hard because you're hiring managing editors, you're teaching them, you're building a lot of the traditional workflows.

**Marcel Santilli:** Like this is how you go from idea to publish and optimization.

**Marcel Santilli:** And then you have to hire a bunch of contributors.

**Marcel Santilli:** Freelance writers and people, and then you had copy editors, had like graphic designer freelancers, you had like, you know, somebody who staged the content and hit publish.

**Marcel Santilli:** So you just like had all these things that were like decomposed, 100% human, and the only efficiency gains were always like me building views into like Airtable for people, for me to know like the pipeline, essentially like managing content as a pipeline, essentially, like just like you would your deals in Salesforce, right?

**Marcel Santilli:** And so then at DeepGram, what I did was just like, take all the thought process of how you come up with a brief, how you research companies, topics, and things like that, and then take, programatize the crap out of that with AI workflows, and then take this guy that now works for us, and just be like, hey, here, I created this Airtable, and here's like each stage of the review process, and I integrated it all with, each one of them had a button, a thing, a trigger, and then a workflow.

**Marcel Santilli:** And then all you had to do was just like review each view, and for each view, I told them like what to review.

**Marcel Santilli:** And then it was like from essentially like finding, it was an AI apps catalog still out there.

**Marcel Santilli:** It's like deepgram.com slash AI apps.

**Marcel Santilli:** And then like he, we just published like 3000 pages that way.

**Marcel Santilli:** And then we started doing like a glossary and then guides and a bunch of things.

**Marcel Santilli:** So it was pretty much like one person that was, you know, offshore, but smart and awesome, but, you know, like fairly inexpensive compared to US standards and me and on autopilot for the whole thing, pretty much, you know, and that was what like got the model, which was like, Hey, people were willing to pay me 10 to 20 K a month to, you know, customize workflows for them, if you will.

**Marcel Santilli:** And they're willing to pay me 10 to 20,000 a month for me to just give them the quote unquote.

**Marcel Santilli:** Like a vision to just be in the loop, grinding and reviewing and publishing.

**Ryan Singer:** Sorry, Marcel, I just, there was a, there was a, there was a connectivity blip for a moment there.

**Ryan Singer:** And I lost you at, um, I heard willing to pay me.

**Ryan Singer:** 10 to 20 to customize workflows, and then willing to pay, and then I lost you.

**Marcel Santilli:** Something around giving them a quote, something.

**Marcel Santilli:** Yeah, so they're willing to pay me for the strategy.

**Marcel Santilli:** Oh, for the strategy.

**Marcel Santilli:** know, 10 to 20 to customize AI workflows, because people don't know how to do that, essentially.

**Marcel Santilli:** And then they're willing to pay, you know, 10 or so for having just a human in the loop that was, you know, decently smart, well-sourced, and whatnot, right?

**Marcel Santilli:** So it's like, I can do either one of those three, or I can combine those three for the cost of one of those, and it should be a no-brainer.

**Marcel Santilli:** And it turned out it was a no-brainer.

**Marcel Santilli:** Like, I probably said a 9,000, and everybody just, it was just like such a no-brainer that it just started flying off the shelf.

**Marcel Santilli:** Like, before I even quit my job, we were at a million and a half, you know, and 12 customers, including Ram and a few others.

**Ryan Singer:** Mm-hmm.

**Ryan Singer:** And that's your, is this like the AI is kind of like automating?

**Ryan Singer:** How much of it is automating your time versus is it about, like, what's the thing?

**Ryan Singer:** Is that they would have to do if they didn't have it?

**Marcel Santilli:** It's, they would need to take, first of all, it's my, a lot of my thought processes baked into workflows.

**Marcel Santilli:** Right.

**Marcel Santilli:** In addition to sourcing the right people and then training them to review it and have the human judgment in the right place in the right way, ideally, when it works, essentially, you know.

**Marcel Santilli:** And, and so it would have to be buying, hiring multiple freelancers, agencies, as well as tools, and knowing how to use the tools, like the AI workflow tools, like the NANs of the world, you know.

**Ryan Singer:** Yeah.

**Ryan Singer:** And so you are also, you're sourcing the, the people who are actually doing the writing for them as well and training them?

**Marcel Santilli:** Correct.

**Marcel Santilli:** Correct.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Today we have 60 people in the deliver side and then like 30 or so on the build side and, and on the deliver side, it's a combination of.

**Marcel Santilli:** Engagement managers that are like, you know, like one of them, Liz, has a master's in AI from UT, you know, like, and then, and then a lot of like editors, they're mostly editors, not writers, right?

**Marcel Santilli:** Like they're, they're editing, reviewing the content.

**Marcel Santilli:** I like to think of them as alpha bar racers, just like a bar racer in a hiring process.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** Yep.

**Ryan Singer:** Okay.

**Ryan Singer:** Um, and, uh, good.

**Marcel Santilli:** Okay.

**Ryan Singer:** Um, uh, so like, is this, is this kind of like your, um, if I, I'm probably over, this is probably overly simplified, but it kind of sounds like they, like they don't have a marketing operations and you're giving them like people and operations like all together in one lump.

**Marcel Santilli:** Yeah, that's one way to think about it.

**Marcel Santilli:** Another way that maybe a mental model there is, you know, most companies that need to grow, they need to do, you know, the sales only.

**Marcel Santilli:** approach like outbound and things like that.

**Marcel Santilli:** then when it comes to outside of that, when it comes to marketing, there's only like so many things they can do, right?

**Marcel Santilli:** Like they can go do events and things that don't scale, they can go do ads, or they can try to grow organically, right?

**Marcel Santilli:** And if you're to grow organically, the place you have the most influence and control is your website, right?

**Marcel Santilli:** And so a lot of what we do is like, hey, if you want to grow more sustainably in a way that compounds over time, it's mostly content through your website, right?

**Marcel Santilli:** And so you can think of like organic growth as the outcome, pages on your site as the output, content as the atomic unit that goes on those pages, and then the context and strategy, like context is understanding your company or personas who you're for, the product and things like that.

**Marcel Santilli:** And then strategies around like, what are the topics and opportunities, aka what kind of pages should you create, that will give you the best shot at the outcomes you care about.

**Marcel Santilli:** And then both creating net new pages as well as optimizing existing pages.

**Marcel Santilli:** That's kind of like the big picture mental model of like why we do and why what we do is value-wise.

**Marcel Santilli:** And often they will have like other emotions.

**Marcel Santilli:** They have like a team taking care of ads, like page traffic or outbound, and then we come in to support with whatever they don't have or to augment whatever they're already doing.

**Marcel Santilli:** Like Lovable, for example, we usually take like chunks of their websites and we run that part.

**Marcel Santilli:** So we're like augmenting their team.

**Marcel Santilli:** So it is, and keep in mind, like one thing that you might know this, but there's over 100,000 marketing agencies in the U.S.

**Marcel Santilli:** alone that list marketing as marketing services and over 40,000 marketing tools.

**Marcel Santilli:** So it's like, it's a highly, highly fragmented space more than almost most other spaces and marketers are just used to hiring agencies very much, you know?

**Marcel Santilli:** Okay.

**Marcel Santilli:** And, and, and, and so that like.

**Marcel Santilli:** Like, it's a huge pain point.

**Ryan Singer:** Like, my whole life, I had to hire freelancers and agencies, and they all kind of sucked in the traumas, know.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** Okay.

**Ryan Singer:** Is this, like, the F1 car, and, like, you're the driver, and then this whole thing is your car?

**Ryan Singer:** Like, are they really hiring Marcel?

**Marcel Santilli:** Today, I would say, the way one of our customers described recently is there's a...

**Marcel Santilli:** Like, because, mean, there's kind of, like, this aura around the company, you know, is maybe one...

**Marcel Santilli:** I know that sounds very pretentious to say out loud.

**Ryan Singer:** No, at least that.

**Ryan Singer:** No, but we have to call it what it is, you know what I mean?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** It is, like, I have, like, $20,000 on LinkedIn, so it's not like I'm, like, this crazy influencer or anything like that.

**Marcel Santilli:** I think it's just the credibility of, like, and, like, these workshops and how deep I go and how hands-on I am, and the fact that I've been doing this for 15 years, and every one of the programs I built worked.

**Marcel Santilli:** Thank you.

**Ryan Singer:** Michael.

**Ryan Singer:** Thank

**Marcel Santilli:** It gives this, like, you're not just, like, hacking an SEO thing or, you know, it's like, you're a legit, like, operator that's also hands-on that, like, teaches people.

**Marcel Santilli:** And so in a lot of ways, that's why we haven't, we literally have hired our first AE three months ago and he's closed, like, $4 million and I'm barely involved in sales anymore, right?

**Marcel Santilli:** Like, so it's not like it only works because of me.

**Marcel Santilli:** It's more of, like, it's now created a brand for itself a bit more, you know?

**Ryan Singer:** Sure.

**Ryan Singer:** And does it only work if, I'm just poking at it a little bit, does it only work if, does it only work if you're the one kind of, so if you think just kind of, like, this whole thing is something that has to get prompted with, like, the context and strategy that you set in the beginning, is this, are there other people who are capable of doing that or just kind of this whole thing, is this whole thing downstream of you putting the right inputs into the start?

**Marcel Santilli:** I think there's, like, I combination of things where, one, there is, like, the process architect of this.

**Marcel Santilli:** The thing, which is like mostly, I would say, like me and Daniel, right?

**Marcel Santilli:** Like there hasn't been any, like anytime we try to delegate the process to architects of like, how do you go about doing the work, right?

**Marcel Santilli:** Like the thought process of like, how do you do really good research?

**Marcel Santilli:** Like Daniel like reinvented like our deep researcher like five times, you know, getting better and better.

**Marcel Santilli:** Like how you identify opportunities, why you do that, like all of that is like Daniel and I are the process architects of that.

**Marcel Santilli:** And it doesn't work if we try to delegate because people don't think first principles and don't have the experience and haven't like done the job with themselves at like at these companies, right?

**Marcel Santilli:** But then there's like what I like to think of it as a mental model of input calibrators, right?

**Marcel Santilli:** And then those, I don't do that.

**Marcel Santilli:** Like those are like the engagement managers, the people that are like, you know, asking questions, saying, hey, what's important to you?

**Marcel Santilli:** Why is it important to you?

**Marcel Santilli:** Who are you for?

**Ryan Singer:** Who's your ICP?

**Ryan Singer:** Why do you, like a lot of like what you're doing right now, right?

**Marcel Santilli:** Like you're probing, you're trying to get that impulse.

**Marcel Santilli:** And then you're, sure, you're using workflows, but you're also connecting the dots for people, right?

**Marcel Santilli:** And so that's a really important part of what we do because you go to, like, a Sentinel One, like, a public company, and you say, hey, do you have a doc with, like, all your products described?

**Marcel Santilli:** Like, no.

**Marcel Santilli:** Hey, do you have a doc with, like, your personas and who your audience actually is and why they should care?

**Ryan Singer:** It's like, no.

**Marcel Santilli:** Hey, people just don't have, like, your websites are outdated.

**Marcel Santilli:** So unless, like, you actually do this process that you're doing, right, like, just don't get it.

**Marcel Santilli:** That's really important.

**Marcel Santilli:** then the last piece is, like, the output bar raisers, and that's the production people, and that's ultimately, like, are the outputs good, or is there anything really off here, you know?

**Marcel Santilli:** And then the last mile execution, which is, like, staging the content sometimes, or something that can't be fully automated, that would take, like, so much work to automate that last 1% or 5%, you know?

**Marcel Santilli:** The way I think about this as well is just, like, a lot of the stuff that Marcel is coming off with is the stuff that you're saying that's, like, super hard to talk.

**Marcel Santilli:** That is his process.

**Marcel Santilli:** And a lot of people will do it different ways.

**Marcel Santilli:** And we tried to let people push their process into our systems, and it didn't work well.

**Marcel Santilli:** So we're embracing Marcel's process and then automating it as much as we can.

**Marcel Santilli:** So that's the top level.

**Marcel Santilli:** And then the bottom level, this output bar razor that Marcel is saying, that is the part that is also a big challenge for us.

**Marcel Santilli:** Because at the top, have one person now.

**Marcel Santilli:** So I removed all the other strategies we had, and I'm just looking at Marcel, and I'm automating Marcel.

**Marcel Santilli:** At the bottom, we have 60 people, and they all can, now you have, the tool has to really help them.

**Marcel Santilli:** Or they will not do the work, or they will fly it back, or they will not do the way you want them to do, with downstream impact.

**Marcel Santilli:** So we have this true force.

**Marcel Santilli:** Yeah, like one way to also think about how much progress this thing already is, is like when I was at HB and I built this type of tech.

**Marcel Santilli:** TechBeacon.com, and we had all these contributors and things, and I had managing editors.

**Marcel Santilli:** We were paying on average like $1.50 per word, right?

**Marcel Santilli:** It's very known in content, like you pay for word kind of for good writers or whatever.

**Marcel Santilli:** And then a way to think about what we do is our customers on average pay like $0.10 to $0.20 per word with what we do.

**Marcel Santilli:** And it comes already with the strategy and a bunch of other things, right?

**Marcel Santilli:** So in a lot of ways, like you're trying to like 5 to 10x the output while also like, you know, paying 90% less, right?

**Marcel Santilli:** Per output and with the same or better quality.

**Marcel Santilli:** And the only way that's possible is because of the leverage we have.

**Marcel Santilli:** And we're also like a 70% gross margin business.

**Marcel Santilli:** So it's like, how do you do softer margin, skill agency with people, which is really hard, and maintain the quality.

**Marcel Santilli:** And then the thing to make it even harder or better, however you want to think about it, is like we really try to do the trust cascade thing, right?

**Marcel Santilli:** It's like, hey, we do it for lovable.

**Marcel Santilli:** We do it for Webflow.

**Marcel Santilli:** We do it for RAM, for Rex.

**Marcel Santilli:** Everybody else is going to look up to those companies.

**Marcel Santilli:** And if we do it for them and we're good enough for them, we're good enough for everybody.

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** So question.

**Ryan Singer:** As we get into AI workflows, which are in the brief today, how much of when you tell the story of we're able to do it for 10 to 20 cents per word instead of $1.50 per word, how much of this is a, is, is a, is a, so like, for example, like I, I come into companies who need, who have like this big gap between business and engineering and they can't get ideas through from intent through to, through, through to build.

**Ryan Singer:** And like, I can, I can give them a 10 X speed up and I'm not doing it with AI.

**Ryan Singer:** I'm doing it because I know how to do things in the right order and not how to waste time on the wrong things.

**Ryan Singer:** Um, uh, how much of this is, is your better inputs and your better process.

**Ryan Singer:** And how much of this, like, is the AI part of what is getting you to the lower cost of the $0.10 to $0.20 per word?

**Ryan Singer:** Is there an efficiency gain from the AI side?

**Ryan Singer:** Or is the efficiency gain coming more from the process knowledge that you have in your way of working?

**Marcel Santilli:** Yeah, so it's almost like you have to be effective before you're efficient.

**Marcel Santilli:** So one is about going in the right direction.

**Marcel Santilli:** The other one is about speed, right?

**Marcel Santilli:** AI gets you, like, the speed, but not necessarily the effectives by itself, right?

**Marcel Santilli:** And our process and people make sure that, like, we're effective with the right quality.

**Marcel Santilli:** And so, like, another way to say it is when you're paying $2 a word for something and you have a limited budget and it's all human and there's not any automation at all, you really have to not mess up.

**Marcel Santilli:** Like, you have to pick the right opportunities.

**Marcel Santilli:** You have to do it in the right way.

**Marcel Santilli:** Like, I remember reviewing, like, hey, let's go back.

**Marcel Santilli:** Like, we have 20 shots on goal every week.

**Marcel Santilli:** Like, let's go back and figure out, like, which ones, like, how do we make the most out of this?

**Marcel Santilli:** So we really got it down.

**Marcel Santilli:** Like, I remember going through these briefs from my managing editors and going, hey, I need you to think of this brief as you're trying to find a gap, an information gap in the market.

**Marcel Santilli:** I need you to read the top 10 search results.

**Marcel Santilli:** And I need you to really think through, like, what is the gap of information for the audience we care about?

**Marcel Santilli:** And how is this going to be better than something that's out there?

**Marcel Santilli:** And if you can't clearly spell out in a couple of senses how this piece of content will fill a need that doesn't exist right now, don't write this piece of content.

**Marcel Santilli:** But there's a lot of that thought process of, like, 10 years of doing that and managing teams, you know, that was really important.

**Marcel Santilli:** And the other piece is also, like, companies are just really  at hiring.

**Marcel Santilli:** And they're really even shittier at hiring freelancers because, like, this is fractional work, right?

**Marcel Santilli:** Like, you're not going to hire 10 full-time writers.

**Ryan Singer:** They're not going to, you know, like, you need somebody to do an output and you're going to pay them for that output.

**Marcel Santilli:** And so, like, that's another really hard thing.

**Marcel Santilli:** So when you try to do the good strategy, the good process, and then also find the people that you can trust, what I found in my experience is very few brands in the planet were able to do that, and that was my special power, was pulling it all together.

**Ryan Singer:** So, yeah, go ahead.

**Marcel Santilli:** You know, one thing I was going to add is that a lot of what Marcel described is how to, like, add repeatable quality into the system, and that's really hard to, sometimes, like, multi-stack process, like what he just described, somebody had to click through 10 links, really, really, really understand, very few people will do that, but, and you also, you can only do that 20 times.

**Marcel Santilli:** But if you can't do that just 60% times 1,000, like the 20% that's going to get surfaced, then you can, you can do that a better quality.

**Marcel Santilli:** So we get more shots on goal, but we do have to take this process and really bake.

**Ryan Singer:** So the thing I'm struggling with is where is the bottleneck?

**Ryan Singer:** Where's the bottleneck that this AI automation is removing?

**Ryan Singer:** Is the bottleneck internal to your operations of doing this?

**Ryan Singer:** Is the bottleneck to, like, what is the thing if you take the AI out that breaks?

**Marcel Santilli:** Yeah, so maybe I can do two angles of this, like one from the customer side and one from our side.

**Ryan Singer:** Exactly.

**Marcel Santilli:** But maybe you tell me if, like, this is wrong or not.

**Marcel Santilli:** So let's take one of our customers, Outreach, right?

**Marcel Santilli:** They're a fairly decent-sized company.

**Marcel Santilli:** have 50 or 60 people in marketing.

**Marcel Santilli:** They have a full-time, two full-time SEO people.

**Marcel Santilli:** It's such content people, right?

**Marcel Santilli:** Two full-time.

**Marcel Santilli:** And I said, hey, you have almost 5,000 pages on your site.

**Marcel Santilli:** They're all getting stale.

**Marcel Santilli:** Like, how many pieces of content can you read?

**Marcel Santilli:** Refresh or publish every month, right?

**Marcel Santilli:** And they're like, on a good month, like five.

**Ryan Singer:** Yeah.

**Marcel Santilli:** This is with freelancers and agencies as well, right?

**Marcel Santilli:** And so think about that.

**Marcel Santilli:** have like two full-time people.

**Marcel Santilli:** You have a massive company with a massive service area with a, you know, let's call every page an asset, like decaying asset that's decaying faster and faster, right?

**Marcel Santilli:** They have a lot of getting shorter, right?

**Marcel Santilli:** And they're like incapable of that.

**Marcel Santilli:** And then you're like, why?

**Marcel Santilli:** It's just like, oh, like we just, they don't know what to focus on, what to prioritize.

**Marcel Santilli:** But also it's just like, they're just staring at a thing and they're like, okay, I got to go through this whole thing.

**Marcel Santilli:** And then I got to figure out how to log into the CMS and then I got to go stage it and I got to track this whole thing.

**Marcel Santilli:** And no one knows how to optimize this whole thing.

**Marcel Santilli:** to them, you know, and they might be editor background, so they can't write the words.

**Marcel Santilli:** don't care about the outcomes, right?

**Ryan Singer:** Or the outputs, right?

**Marcel Santilli:** They're just like, oh, I just want to make this one piece of content really good.

**Marcel Santilli:** And so like, there's no like director or orchestrator of the whole thing.

**Ryan Singer:** So then there's.

**Marcel Santilli:** It's like crazy inefficiency, right?

**Marcel Santilli:** So the bottleneck there is like, if you think of an e-commerce company, like let's say Amazon, right?

**Marcel Santilli:** They spend over a billion dollars on their catalog.

**Marcel Santilli:** They don't see their catalog as a page on the website, right?

**Marcel Santilli:** They see it as like literally a driver of business value.

**Marcel Santilli:** So that's kind of how I've always thought about it.

**Marcel Santilli:** It's like your website is a product.

**Marcel Santilli:** You know, your pages are your outputs that will drive the outcomes you care about and things like that.

**Marcel Santilli:** So the bottleneck there is like companies are just stuck not being able to do more outputs.

**Marcel Santilli:** and know what outputs to focus on.

**Marcel Santilli:** know, and it's not a function of like budget or people, right?

**Marcel Santilli:** And then agency.

**Marcel Santilli:** So then like most of those people then go and hire an agency.

**Marcel Santilli:** And then agencies will charge an insane amount, like 50 to 100 grand times a month to do like the same level of output.

**Marcel Santilli:** It's insane, right?

**Marcel Santilli:** And they won't understand their business very well and it will be garbage.

**Marcel Santilli:** So that's like the bottleneck there.

**Marcel Santilli:** And then the thing that just like through fuel at that is the fact that like all this buyer behavior,

**Marcel Santilli:** We're shifting towards AI answers.

**Marcel Santilli:** now people are probing an AI engine like ChatDBT, and whatever comes back, they're ingesting as expert advice.

**Marcel Santilli:** They're word of mouth expert advice, right?

**Marcel Santilli:** Like you're the ultimate expert in this.

**Marcel Santilli:** It's like you were personally there telling me what to do, you know?

**Marcel Santilli:** And so they see ChatDBT as that.

**Marcel Santilli:** And the problem is now every brand needs to figure out how to influence that, otherwise they're , right?

**Marcel Santilli:** And so now they're like the best way to influence that is content on their website.

**Marcel Santilli:** that's like the accelerant of that.

**Marcel Santilli:** And then on our end, the really like the biggest bottleneck has been like consistency and following our process, and then how quickly we can codify our stuff into our systems versus codify it into training for our people.

**Marcel Santilli:** And the problem with training with our people is that a moving target, right?

**Marcel Santilli:** You have five people today, tomorrow, two of those leave, and now you add five more on top of that.

**Marcel Santilli:** So now we have 70 people and three existing, and the three existing.

**Marcel Santilli:** I got so busy that I forgot what it was like, you know, and then our systems are evolving.

**Ryan Singer:** Oh, that's so interesting.

**Ryan Singer:** Okay, so you are basically, you're just a really premium agency that actually doesn't suck.

**Ryan Singer:** And at the speed, because you're able to move, this is going to be wrong, but I want to see if I can get closer to you and you can tell me where it's not right, you know.

**Ryan Singer:** Um, it sounds like you're like the, what an agency should be in terms of the speed and both speed and quality of what's needed, independent of the product and the software and everything like that.

**Ryan Singer:** Like, uh, people see you as like, you can actually come in and, um, I'm not going to be paying the hundred K a month to go to move at the same speed.

**Ryan Singer:** I'm paying the nine K a month.

**Ryan Singer:** I'm moving way faster and the stuff actually matches like the it's, it's strategically meaningful, let's say.

**Marcel Santilli:** Right.

**Ryan Singer:** but then on your side, like in order to move that fast and for this thing to be something.

**Ryan Singer:** That you can actually operate with, you need to have this, it seems that you already have a degree of automation because you've been able to understand how you do what you do.

**Ryan Singer:** And you've been able to kind of like tease out the places where you personally as the strategist have to integrate versus the places that you can modularize and bring in different people.

**Ryan Singer:** But when you bring in people into the modularized parts, there's this onboarding cost and there's also kind of this overhead cost of like keeping people on track, making sure they're doing it right and stuff like that.

**Ryan Singer:** So the real scale advantage from the AI automation is more, not exclusively, but it sounds like it's more back of the house internal to the agency so that you can provide the like insane accelerated agency experience to your customers.

**Marcel Santilli:** I would.

**Marcel Santilli:** Yes, but one thing that I would say is, think of the system as, the way we're thinking, like, the agents today, it's almost like our way of trying to put Marcel on every company.

**Ryan Singer:** Uh-huh, uh-huh.

**Marcel Santilli:** And, like, essentially, you have, even on our own team, like, we have people that are former CMO, like, former, like, heads of marketing and stuff like that, and they don't have the processes as well codified and well-struck.

**Marcel Santilli:** So, looking on our ideal path would be, like, we start with this system that's half-automated on each part just to make our lives easier, and we embed ourselves into these companies, and we show them, hey, like, you should be thinking about organic marketing this way, and then they can take it and run it.

**Marcel Santilli:** So, we have, and, like, the parts that are more automated, that you can see it happening, the parts that are less automated, that's where people, you have learning curve problems, you have repeatability problems.

**Marcel Santilli:** Problems and all that.

**Marcel Santilli:** So we think like, for example, the strategy part, it's not one and done.

**Marcel Santilli:** Like if we do as an agency, it would be one once every quarter for like $30,000 and we're going to come up with a thousand ideas for you.

**Marcel Santilli:** But ideally, the VP of marketing or like the head of marketing in the company would be doing that every week, you know, and they will be even more effective than our agency trying to do it for that.

**Marcel Santilli:** And then same thing with hiring freelancers.

**Marcel Santilli:** So like if you need to have a thousand articles refreshed, like Marcel was saying, ideally, you don't have to learn how to hire people.

**Marcel Santilli:** You don't have to learn how to monitor them.

**Marcel Santilli:** You don't have to learn how to make sure that product that they wrote matches your product.

**Marcel Santilli:** But there's all this thing is that because there is like no one system, you have to patch with people here and there.

**Marcel Santilli:** And we can see a path where we can patch all the way down, you know.

**Marcel Santilli:** So, yeah.

**Marcel Santilli:** Okay.

**Marcel Santilli:** The way we kind of.

**Marcel Santilli:** We were trying to tackle, like, decompose it from first principle and tackle one piece at a time.

**Marcel Santilli:** So we started with, call it like AI workflows as code, because managing workflows became unmanageable.

**Marcel Santilli:** that felt like where, that was the most unique part that was going to build the most leverage long term.

**Marcel Santilli:** And everything depended on that foundation, right?

**Marcel Santilli:** And that's like the framework we're going to open source soon, right?

**Marcel Santilli:** And in our, what everything goes through.

**Marcel Santilli:** And then after that, it was like, well, we're using these, like, tools to hit play and just ping these workflows and then take the output and then copy and paste these outputs into, like, a Google Doc.

**Marcel Santilli:** Problem is now, we don't know what's happening and we don't know, like, you know, we can't learn from it, right?

**Marcel Santilli:** So then we're like, let's just put it all in one single place, ideally, right?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And then we did that super fast because we had to, right?

**Marcel Santilli:** Put it all in one place.

**Marcel Santilli:** And then after that, was like, okay, now, like, we need to manage.

**Marcel Santilli:** What assignments and opportunities I'm going to go after is like, okay, let's just do that in Airtable because that's how I've been doing it.

**Marcel Santilli:** And, you know, use workflows as a major process.

**Marcel Santilli:** And then, and now it's like the customers are like, hey, by the way, like I need reporting.

**Marcel Santilli:** Like, is this thing working or not?

**Ryan Singer:** It's like, okay, let's just build Booker dashboards for now.

**Ryan Singer:** Right.

**Marcel Santilli:** Yep.

**Marcel Santilli:** And so like we kind of solved it in the let's deliver value because we're delivering as a service.

**Marcel Santilli:** Like we get to control that.

**Marcel Santilli:** And, you know, but now it's getting to a point of diminishing returns on people investment, right?

**Marcel Santilli:** Right.

**Marcel Santilli:** Yeah, exactly.

**Marcel Santilli:** And so now it's like, we have to just like systematize a lot more and codify it a lot more into the system because it's getting too complex to train 60 people how to do these things outside of the platform.

**Marcel Santilli:** know, so that's the same times also when the clients are asked, like, can I see the opportunities?

**Marcel Santilli:** Can I see the progress that was made?

**Ryan Singer:** Can I add?

**Marcel Santilli:** Yep.

**Marcel Santilli:** Can I run this?

**Marcel Santilli:** Can I go use our researcher?

**Marcel Santilli:** Yep.

**Marcel Santilli:** They're asking for access and we are.

**Ryan Singer:** Got it.

**Marcel Santilli:** Let me just add one quick thing, sorry, so don't forget, is that if you take the same words, okay, and you present those words to you in a Google Doc, and you have no idea how we came up with those words, right, there's a perception of value of that, and sometimes people might think, just want to chat to me,-Con, can paste this , right, even if it looks good, right, and so maybe like that is worth $50, $100, to you, right, because of that, but if you see the workflow, you see the execution, you see that we did like, you know, $30 worth of compute processing, you see the context, you see then also the results later on, like then that piece of output is now worth maybe like five times more, right, and you're like 10 times more likely to stay and continue to use this thing because you see that value, and today that's what's missing, like we're mostly just sharing Google Docs with people for them to review, you know.

**Ryan Singer:** Got it, okay.

**Ryan Singer:** Um, I want to propose a lot of this kind of went full circle into why we need the text editor.

**Ryan Singer:** That's, that's, that's good.

**Ryan Singer:** We were getting a segue into the actual, into the actual work.

**Ryan Singer:** I think, um, I think that's enough at a high level and let's dig into, let's, let's get into the concreteness of this thing that you're trying to do right now.

**Ryan Singer:** So, um, there's urgency, there's urgency enough around the text editor that you chose this as the thing for today.

**Ryan Singer:** Um, I, I want to propose, is it fine if I hit, oh, probably I have to do, uh, ask you to do this.

**Ryan Singer:** I would suggest we start recording.

**Marcel Santilli:** Uh, yeah, it's been recording the whole time and there's like three different ones recording.

**Ryan Singer:** So we're good.

**Ryan Singer:** Okay.

**Ryan Singer:** And you're getting screen, screen recording as well as part of that.

**Ryan Singer:** Yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** Uh, uh, good.

**Ryan Singer:** Okay.

**Ryan Singer:** Um, so, uh, um, okay.

**Ryan Singer:** So I think the, what we're coming into is the first thing I would be trying to talk about with this text editor thing is the framing of it.

**Ryan Singer:** Um, so, uh, let me just ask a couple.

**Ryan Singer:** Fundamental questions, specifically about text editor, and then we can start to hit different angles on it and see what we can do.

**Ryan Singer:** Where's the urgency coming from out of all the different pain points where text editor is the thing that we're talking about today instead of, I'm sure there's a million other things that you can optimize.

**Ryan Singer:** Is it, is it more, is it more the, is it more the 60 people bottleneck?

**Ryan Singer:** And then, and then the like, and in the future, you know, this is going to make sense in the customer facing piece.

**Ryan Singer:** Or is there something else?

**Ryan Singer:** Like what's, what's, what's sort of driving the urgency where like, this is the thing that needs to happen in January?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** So maybe I'll give a couple of different answers because there's multiple reasons and then we can kind of maybe try to prioritize, you know, those, but the one piece is.

**Marcel Santilli:** Editors are this, like, capacity suck, if you will, right?

**Marcel Santilli:** Like, and it's like this black box, almost, right?

**Marcel Santilli:** So think of it as you could spend a year editing one single article if you really wanted to.

**Marcel Santilli:** Yes.

**Marcel Santilli:** You know what mean?

**Marcel Santilli:** Because it's like this infinite suck if you let it be, right?

**Marcel Santilli:** And today, we're flying blind.

**Marcel Santilli:** So it's just like, hey, all we know is that we kept adding more and more people.

**Marcel Santilli:** And people are like, we need more.

**Marcel Santilli:** We need more editors.

**Marcel Santilli:** We need more editors.

**Marcel Santilli:** We can't keep up with, like, the capacity.

**Marcel Santilli:** Like, we need more capacity or whatever, right?

**Marcel Santilli:** And we're like, wait, hold on.

**Marcel Santilli:** Like, how?

**Marcel Santilli:** Like, we used to be able to do this with, like, way better ratio.

**Marcel Santilli:** And, like, the ratio keeps getting worse, but the tech keeps getting better.

**Ryan Singer:** So, like, that doesn't work out, right?

**Marcel Santilli:** Yeah.

**Ryan Singer:** And so, like, we're doing things, like, we kicked off a time tracker last week.

**Marcel Santilli:** You know, because we're like, what the hell is happening?

**Ryan Singer:** What are people doing, right?

**Ryan Singer:** Yeah.

**Marcel Santilli:** And there's no way for us to know if the, I think of it as, I was in data labeling, right?

**Marcel Santilli:** Like, Scaly Eyes, Search is one of our biggest customers.

**Marcel Santilli:** So for me, I think of it as like human intervention.

**Marcel Santilli:** You know, you're like, ideally, like the human intervention is not just to do it and keep doing it, it's to find like, almost like failure modes into the content and then try to address those failure modes in a more repeatable way so that the next time around, hopefully, like, it's less likely that that failure mode happens again, right?

**Marcel Santilli:** And, but then editors just think of it as like, I don't know, I'm just making this content better.

**Marcel Santilli:** I'm just going to go spend five hours on it because it's way off.

**Marcel Santilli:** I'm actually copy and paste this into ChatGPT and improve it myself.

**Marcel Santilli:** I'm going to put it in Google Doc.

**Marcel Santilli:** And so we're flying blind on it.

**Marcel Santilli:** So that's one piece.

**Marcel Santilli:** And there's no way for us to increase, like, increase capacity to be, like, right now we're turning away business.

**Marcel Santilli:** Like, last week, we told our sales guy, hey, say yes a bit more.

**Marcel Santilli:** We closed five deals a million in ARR.

**Marcel Santilli:** Like, we're truly not the name constraint, you know?

**Marcel Santilli:** We're truly not

**Marcel Santilli:** turning away business.

**Marcel Santilli:** And so that's that one piece.

**Marcel Santilli:** Then the second piece is like the quality tends to be the bottleneck to getting to output.

**Marcel Santilli:** So if quality doesn't meet a certain bar or expectation for customers, then we can't publish.

**Ryan Singer:** If we can't publish, we can't achieve results.

**Marcel Santilli:** Right?

**Ryan Singer:** Okay.

**Ryan Singer:** Hold Let me pause you.

**Ryan Singer:** Capture something.

**Ryan Singer:** So we're turning away business because of the fact that editors are not turning around articles as fast as you think they should?

**Marcel Santilli:** We're turning away business primarily because we don't know how to create more capacity in a predictable way.

**Marcel Santilli:** Right now, the way we have been doing it was mostly just hiring more people, except like, think of it as like the next person you hire has a, you know, diminishing return than the previous one, you know, on building capacity, right?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Think of capacity as like...

**Marcel Santilli:** If every customer were doing five articles a week, a simplistic way, and you think one editor can do 30 a week, and then you start to scale, and now one editor can only do five a week, now the model breaks, right, essentially.

**Ryan Singer:** Yep, okay, so, okay, so you're turning away business, this is regarding, this is especially on the editors, are the place where you're feeling the crunch, more editors, okay.

**Marcel Santilli:** mean, it's the editors is the who, but it's ultimately, like, reliably publish high quality content for customers, you know, and at scale, you know.

**Ryan Singer:** Yep, yep, of course, of course, yeah, I'm just kind of looking, like, from a debugging lens, not from an outdoor lens.

**Ryan Singer:** Okay, and then still on the debugging lens, there's a quality piece that you were, that you were mentioning when I, when I interrupted you, when I tried to slow you down to capture this.

**Marcel Santilli:** Yeah, sorry, I talk fast, so please slow me down.

**Marcel Santilli:** Yeah, so then on the quality side is you, there's the process called calibration that we go through, just like in data labeling, right?

**Marcel Santilli:** Like you calibrate, you know, to make sure the taskers are doing the right thing, you know, like, and so today the way that works is like, it's all over the place.

**Marcel Santilli:** And we have to, an editor will essentially create a sample piece of content, a sample output, and then send it to a client to review and see if it's good enough or not, right?

**Marcel Santilli:** And then essentially label it.

**Marcel Santilli:** But then often customers that churn during the strategy spread process, which is the first eight weeks that they can still churn, has been because we weren't able to achieve the quality that they expected during the calibration process, right?

**Marcel Santilli:** And they didn't feel they were confident enough that we were able to reliably do that, you know, it's like way too off and things like that.

**Marcel Santilli:** And part of that process is...

**Marcel Santilli:** It's like really hard because like when it works, it's us putting, picking the right opportunity, writing that piece of content, putting it into Google Doc and sending it to them.

**Marcel Santilli:** And in that, there's like outside of the work of the editor itself, there is the choice of the topic as well.

**Marcel Santilli:** So like sometimes they, people might choose a topic that's way too hard for themselves to write or for the AI to write without calibration.

**Marcel Santilli:** So like, for example, let's say you pick a client like clerk, percent no one, they're in the security space, you can pick like how to do a login with security at a high level, or you can go all the way deep and write about a bunch of vulnerabilities.

**Marcel Santilli:** So if you tap into that, then it's also a choice of the topic as a problem, not just like, like imagine for a second, like you're trying to scale your consulting, you know, practice, if you will.

**Marcel Santilli:** And the first calibration piece would send you is like.

**Marcel Santilli:** How to, like, how to manage product teams to deliver, you know, better outcomes.

**Marcel Santilli:** Like, something super generic, best practice, right?

**Marcel Santilli:** And it's like, for us to exceed your expectations as the expert on that, we would have to literally, like, blow your mind, essentially, right?

**Ryan Singer:** It would be really hard because you just picked the first thing.

**Marcel Santilli:** And so there's more things you can do is, like, where you can nail and say, maybe the calibration we're talking about, like, best questions to ask in order to better frame a problem.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** Now we can probably win that.

**Marcel Santilli:** And we can probably do something that you're like, actually, this is really cool.

**Marcel Santilli:** Like, you took a bunch of my own things, you did some research, and you narrowed down the problem enough or the, you know, the scope enough to where we can all calibrate based on that, you know?

**Marcel Santilli:** So that's the making sure you pick the right opportunities.

**Ryan Singer:** All right.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** So let me just segment what I'm hearing and try to see if we can start to narrow problems.

**Ryan Singer:** I'm hearing two very, very, very different problems here.

**Ryan Singer:** One of these problems is around your editors working for you, the work they do in editing is too opaque.

**Ryan Singer:** There's this kind of black box thing of the editors are spending too much time than they should.

**Ryan Singer:** We can't just hire more to scale.

**Ryan Singer:** So what we need to do is kind of get more power efficiency out of the editors that we have.

**Ryan Singer:** So there's this piece.

**Ryan Singer:** Then there's this other piece, which is a quality piece.

**Ryan Singer:** So this is more about efficiency and time, and it's less about, of course, quality is always there, but that's what this problem is less about.

**Ryan Singer:** Then there's this other thing, which is like around customers churning, because like the stuff that you chose to focus on wasn't the thing that you were more likely to win on.

**Ryan Singer:** That, is that, is that also?

**Ryan Singer:** So, So, So, don't know.

**Ryan Singer:** So is that something that kind of comes to mind now, but it's not as pressing?

**Ryan Singer:** So if we can do one of these things in January and one of these things we don't do in January, is one of these things more clearly urgent than the other?

**Marcel Santilli:** Yeah, like the thing we're doing both in parallel.

**Marcel Santilli:** So we have like my specific team, like my time, my personal times is going on the bottom part, like choosing the topics, surfacing the opportunities and everything else.

**Marcel Santilli:** Because top part, the speed and efficiency part of the actual process of writing, that would be another key.

**Marcel Santilli:** So we're trying to double group at the same time.

**Marcel Santilli:** And they're not going to tap at the same level of results.

**Marcel Santilli:** Like I think the bottom part has so much room to keep improving.

**Marcel Santilli:** The top part is almost like a fire, you know?

**Ryan Singer:** Got it.

**Ryan Singer:** Yeah, the top part is...

**Ryan Singer:** This is the more urgent part, because like if you don't solve this, never grow.

**Ryan Singer:** But this is something you can keep getting better at as you grow.

**Marcel Santilli:** Yeah?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** And it's like the bar is really low because it's like manual already and people are sometimes not even doing it.

**Marcel Santilli:** And then on the top part, there's like two sides of it.

**Marcel Santilli:** And think of one side as like, how do you put more burden or more on the client to arrive at their definition of done and their definition of good?

**Marcel Santilli:** Okay.

**Marcel Santilli:** So that's almost like a labeling job, if you will.

**Marcel Santilli:** Calibrate, iterate, and label what your benchmark is for good and done.

**Ryan Singer:** So let me flip you from outcome back into debugging mode on that one again.

**Ryan Singer:** So what I'm hearing is there's a, with this capacity constraint and the diminishing returns of bringing more editors on, there's a problem with how long the editors spend per piece.

**Ryan Singer:** But then there's this other piece, this.

**Ryan Singer:** There's another aspect of the content feedback life cycle, which is on the client's side.

**Ryan Singer:** And I'm hearing that there's – so are you speaking to something which takes too long or is too – it's not in the editor's hands.

**Ryan Singer:** It goes into the client's hands, and then there's a step there that takes too long?

**Marcel Santilli:** Yeah, so think of it as if you skip calibration altogether, you don't even know what you're editing for to begin with, right?

**Marcel Santilli:** You have no basis for what the client expects and why they expect that, and you haven't even figured out what they want and why they want that in order to allow you to publish on their site, right?

**Marcel Santilli:** And so then it becomes a bottleneck, and then no matter how much you edit, you're just going to be spinning, right?

**Marcel Santilli:** And so that's the first step is like saying, hey, based on everything we heard during onboarding and everything we know about you and your brand, here's a sample output.

**Marcel Santilli:** Derekauchi.ankind

**Marcel Santilli:** Does that work?

**Marcel Santilli:** Is that getting close to your bar done and good?

**Marcel Santilli:** Yes or no?

**Marcel Santilli:** And if not, can you give me some comments as to what we've got wrong here to hopefully, like, get to a point where we like to call it the, like, first publishing, right?

**Marcel Santilli:** Like, get to a first output in the first several weeks.

**Marcel Santilli:** And then that process is usually an editor will create an output.

**Marcel Santilli:** And sometimes, by the way, that output will be fully created off our systems, which is not good, right?

**Marcel Santilli:** And then they will, it's not good because then you can't replicate it, right?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And assuming they're not doing that, assuming they're going into our systems, they're setting up the artifact, they're setting up a pipeline, they're outputting and then doing some editing.

**Marcel Santilli:** And then they copy and paste that into a Google Doc, for the most part, and then send it to the client and say, hey, here's your calibration article.

**Marcel Santilli:** Can you review it and put some comments, you know?

**Marcel Santilli:** And then after those comments, it becomes really hard for us to even know what to do, right?

**Marcel Santilli:** Because the editor...

**Marcel Santilli:** They're not AI engineers, right?

**Marcel Santilli:** They're not prompt engineers.

**Marcel Santilli:** They don't know, should I go update our artifacts in context?

**Marcel Santilli:** Should I go forward deploy engineers to tweak the pipeline or something else, right?

**Marcel Santilli:** Or writing guidelines or whatever.

**Marcel Santilli:** And then on top of that, also, like, those things can get lost.

**Marcel Santilli:** Like, people will put a, they might miss a comment in the Google Doc.

**Marcel Santilli:** And then the third thing is, like, we don't get that data.

**Marcel Santilli:** And so, like, later on, we can't go back and be like, oh, like.

**Marcel Santilli:** The way to think about this, Ryan, like, we have a, a workspace has a bunch of sets.

**Marcel Santilli:** So you have, like, context documents, you have calibration of the workflows and all those things.

**Marcel Santilli:** And you're going to get these comments from the client.

**Marcel Santilli:** And ideally, you'll be able to look at it.

**Ryan Singer:** Okay, like, this is the problem here.

**Marcel Santilli:** So essentially, you take the comments and you debug the system.

**Marcel Santilli:** But if the comments happen outside the system, and if the document was created with something,

**Marcel Santilli:** That's not even our process, then essentially it's very hard for the Poi team to come and say, okay, that's where we are just the clocks, you know?

**Ryan Singer:** So do I understand, right, when the editor creates the output outside your system, you are just in normal agency land with this feedback loop from the client, and you don't have any way to influence or accelerate this process, is that right?

**Marcel Santilli:** Pretty much.

**Marcel Santilli:** And then we have to reverse, try to reverse engineer that back into our system, you know?

**Marcel Santilli:** Okay.

**Ryan Singer:** Let's take an actual case.

**Marcel Santilli:** Can you guys think of an actual case when this happened recently?

**Marcel Santilli:** Yeah, I think we have the perfect one, which is a company called Biologica.com.

**Marcel Santilli:** It's the guy that started Allbirds, and it's like a hormone supplement.

**Ryan Singer:** Did you say Biologica?

**Ryan Singer:** Biologica?

**Ryan Singer:** Biologica.com, yeah, exactly.-huh,

**Marcel Santilli:** And think of it as like they developed these supplements for women in different phases of life, fertility, pre-menopausal, and post-menopausal.

**Marcel Santilli:** And so they had this like doctor, essentially Maggie, who developed the whole thing.

**Marcel Santilli:** Then there's Joey, who's the CEO.

**Marcel Santilli:** And then there's Liz, who's like his wife, also founder, right?

**Marcel Santilli:** And so you have like, and then a marketing guy and then a lawyer, right?

**Marcel Santilli:** And so you essentially have like two doctors, one lawyer, one marketer, and two founders, you know?

**Marcel Santilli:** And so we do the kickoff, and they really care about qualities.

**Marcel Santilli:** Like, hey, this is the content they just launched this week, right?

**Marcel Santilli:** That's why it's a good one.

**Marcel Santilli:** And they're like, look, this is the first impression of our brand.

**Marcel Santilli:** Like, we need to show that we know what we're talking about, how we care about the ingredients that we use, how they impact your health.

**Marcel Santilli:** Like, it has to be medically backed, science backed, and things like that, right?

**Marcel Santilli:** So then we're

**Marcel Santilli:** We're them, hey, can you walk us, we did this whole interview with Maggie and Joey, like, hey, how did you come up with this?

**Marcel Santilli:** Like, how did you pick the right ingredients, blah, blah, blah, and it was like this soup, an hour and a half deep dive, right?

**Marcel Santilli:** It was gold.

**Marcel Santilli:** And then it's like, what do you care about?

**Marcel Santilli:** How do you want to sound?

**Marcel Santilli:** They had like, what do you want your brand to look like and whatnot.

**Marcel Santilli:** Then from there, we got Is this what you call calibration?

**Marcel Santilli:** What is this work that you're describing to me that you did?

**Marcel Santilli:** What do you call that work?

**Marcel Santilli:** This is like pre-calibration is essentially like getting the right inputs.

**Marcel Santilli:** It's the context setting, if you will, like getting inputs and turning that into a context, and then to inform the calibration, essentially.

**Ryan Singer:** Okay, okay, uh-huh, got it.

**Marcel Santilli:** All right, okay.

**Marcel Santilli:** And then what happened next?

**Marcel Santilli:** So then, like, we shared with them, like, hey, here's the writing guidelines we came up with and the context.

**Marcel Santilli:** We get this right, tweak it a little bit, a couple comments.

**Marcel Santilli:** Then we're ready for calibration, which is like, let's create a sample output.

**Marcel Santilli:** Then we went and created a piece of content.

**Marcel Santilli:** All right.

**Ryan Singer:** Okay, so this is calibration?

**Ryan Singer:** This first loop of this?

**Ryan Singer:** Correct.

**Marcel Santilli:** Got it.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** So one is like input and context setting and making sure we heard them right.

**Marcel Santilli:** And then like the guidelines are right and things like that.

**Marcel Santilli:** personas right and all and how you want to sound.

**Marcel Santilli:** And then the other one is like them applying it and iterating to make sure we get it right.

**Marcel Santilli:** And so then we heard a piece of content, sent them a Google Doc, and maybe we still have the Google Docs anymore.

**Marcel Santilli:** can do the Slack of Maggie.

**Marcel Santilli:** Just search for Maggie comments.

**Marcel Santilli:** It's a good first thing, but I open all of them.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** Is the one from, there's one that's like more recent.

**Marcel Santilli:** Let me turn on.

**Marcel Santilli:** turn on.

**Marcel Santilli:** turn on.

**Ryan Singer:** So the thing I want to ask is, like, there's got to be something which is very much more top of mind.

**Ryan Singer:** like, detail aside, what went wrong here?

**Ryan Singer:** So far, everything is going fine.

**Ryan Singer:** Like, we made sure we heard them right.

**Ryan Singer:** We think we're ready to do calibrations.

**Ryan Singer:** So the editor creates the first piece of content.

**Marcel Santilli:** You send it to them in a Google Doc.

**Marcel Santilli:** Like, where does this thing break down?

**Marcel Santilli:** Like, where did the bad thing happen?

**Marcel Santilli:** Okay, so now Maggie posts, like, 33 comments.

**Marcel Santilli:** And this is, like, the example of, like, you're right, when it mostly went, right?

**Marcel Santilli:** So she posts 33 comments in this Google Doc.

**Ryan Singer:** Maggie's the client, yeah?

**Marcel Santilli:** Before that, like, you have two paths there at that beginning of the parentheses that you have.

**Marcel Santilli:** Like, one path would be you go into the system, you take all the notes that you heard, you write a context document.

**Marcel Santilli:** And then the other thing would be, like, you choose a topic that you think our assistants can handle.

**Marcel Santilli:** So you can take, like, maybe I can choose a topic.

**Marcel Santilli:** Sorry, hold on.

**Ryan Singer:** Daniel, got to interrupt you for a second, just because I don't want to get lost, because I can feel that I was on a track, and I want to make sure if we're on the same track or different tracks.

**Ryan Singer:** So what I'm trying to do here is get a single timeline of what actually happened, so I can understand, like, we did this, and then we did this, and then we did this, and then the problem happened or didn't happen.

**Ryan Singer:** So are you describing that there was a, is this something different that happened with this, with Maggie, with this particular client?

**Marcel Santilli:** Like, the case of Biologica, I don't know exactly what they did there.

**Marcel Santilli:** So there's, like, what they should have done, or what they, or what some folks might do.

**Ryan Singer:** Okay, so what I want to do is just for the moment, in order to get us grounded somewhere, because I really want to make sure that you guys get something out of this three hours today.

**Ryan Singer:** And what I need to do now, with the time that's left, is really get us into, like, here's a specific example of something that went wrong, that we think this new thing is going to stop from happening.

**Marcel Santilli:** Yeah, okay.

**Ryan Singer:** So that's what I'm trying to do.

**Marcel Santilli:** I think in Biology, they didn't calibrate the workspace, and they created everything probably via a GPT or Claude without using the system.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** But it's not always.

**Ryan Singer:** The parameters that you have there, you can't So in this case, let me capture that, because this is really important, because like this, for example, if the place where the fault happened was before we even got into Google, Google Docs, because they didn't use the calibration.

**Ryan Singer:** So this is the thing.

**Ryan Singer:** Did I hear right that you did this work of like defining all the context, but then when the editor created the output, the editor didn't, they didn't draw from the context we created?

**Marcel Santilli:** They didn't like, they think of it as like, you create these artifacts, which is like company description, product description, persona, and right.

**Marcel Santilli:** So one approach is like, and then you pick a topic to calibrate.

**Marcel Santilli:** And so one approach is you take this three docs, you throw it into Claude, and you say, I'm trying to create this.

**Marcel Santilli:** And then you go and perplexity, you do some manual research, copy and paste the research to that chat, and you say, create me an article.

**Marcel Santilli:** And then you hand-carve the F out of it.

**Marcel Santilli:** And then you copy and paste that into Google Docs.

**Marcel Santilli:** So that's one approach that happens quite often.

**Marcel Santilli:** Actually, even this week, I saw it happen during a kickoff.

**Marcel Santilli:** And then the other approach is like, they actually tried it.

**Ryan Singer:** I'm going to slow you down just so I can capture, because these are actually what's important here.

**Ryan Singer:** So one approach is this always happens.

**Ryan Singer:** So the same thing happened as usual.

**Ryan Singer:** But then you said that they took what happened here and put it into Claude code?

**Marcel Santilli:** Just Claude, and like Claude project, chat, essentially.

**Marcel Santilli:** Yep, uh And then maybe did some research and like perplexity, you know?

**Ryan Singer:** Yeah, okay.

**Ryan Singer:** Okay, so let's just, well, just to approximate.

**Marcel Santilli:** But I just want the concreteness here and then they get so this is them doing their own research based on the context and then what and then they complete and then they copy and paste to a Google Doc and manually edit before sending it to the client, which is then.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** So I can just explain why this could be a problem.

**Marcel Santilli:** Our researcher, for example, takes about 40 minutes while Claude and perplexity optimize for speed.

**Marcel Santilli:** So we probably, if you do that, you get problems on factuality and you get problems on voice.

**Ryan Singer:** So, so what they, something happened here that they, that did they break away from your intent of what they were supposed to do at this, at this step?

**Marcel Santilli:** Yes.

**Marcel Santilli:** But also like, keep in mind, like our internal systems have been evolving so quickly and, and there's been things we just chose not to prioritize.

**Marcel Santilli:** And so that's like the danger of like having humans close the, the game.

**Marcel Santilli:** apps that the tech is closing, is that eventually they get used to doing it that way and don't want to revert back.

**Ryan Singer:** So what I understand is they ended up, they redid research that already happened, is that right?

**Marcel Santilli:** No, they just never even, so think of it as like.

**Ryan Singer:** What I'm trying to understand is what actually went wrong here.

**Ryan Singer:** So if the output wasn't what the client wanted because it didn't fully take advantage of the context that you did, like it didn't take into account the work that you did here, like what actually went wrong?

**Marcel Santilli:** It took into account that work, but the problem is they didn't try to do their first shot in our systems.

**Marcel Santilli:** So even if they end up getting to a good output here, it's not reproducible.

**Ryan Singer:** Uh-huh, uh-huh, okay.

**Ryan Singer:** So in this case, how was the output?

**Ryan Singer:** Was the output first?

**Marcel Santilli:** There's two layers there.

**Marcel Santilli:** So one is that it's not reproducible, and there's a higher chance of being.

**Marcel Santilli:** In fact, it's really wrong as well.

**Ryan Singer:** Uh-huh, uh-huh, okay.

**Ryan Singer:** So, what I'm hearing, what I'm hearing is everything went fine, but there's concerns about like how, that this doesn't scale or this could go wrong in the future, but am I understanding right that in this case that the output was actually fine?

**Marcel Santilli:** Depends, for this client.

**Ryan Singer:** For this client, was fine, good.

**Ryan Singer:** So can you tell me, is there a story where the output wasn't fine?

**Marcel Santilli:** Yeah, think we've this client even.

**Marcel Santilli:** So like, we don't send one calibration only.

**Marcel Santilli:** We'll start, we send one, and then we're like, oh, this is off here, this is wrong here.

**Marcel Santilli:** And then it can be wrong for two reasons.

**Marcel Santilli:** can be wrong for factuality, or for just like formatting and style.

**Marcel Santilli:** So formatting and style, you can get right if the notes from the beginning are right and all that.

**Marcel Santilli:** The factuality, if something like Biologica, will be very often.

**Marcel Santilli:** So in the case of biological, we might get like a positive once and then a negative right after.

**Marcel Santilli:** So like even during the calibration phase.

**Marcel Santilli:** So there's always just two things.

**Marcel Santilli:** And then if you get this factuality off, there is no way to get that right outside of our system.

**Ryan Singer:** That makes sense.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** So if they leave the system, it can introduce factual errors?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And it will introduce inconsistency, basically.

**Marcel Santilli:** So even if we get like a positive, then the next one might not be positive.

**Ryan Singer:** Okay.

**Ryan Singer:** When, as we talk about this workflow, what I'm hearing you describe is a quality problem.

**Ryan Singer:** And what this problem to me sounds like the problem we moved below the dotted line earlier.

**Ryan Singer:** So I want to call this out as like a red flag in terms of narrowing.

**Ryan Singer:** So is there a version of this story that has to do not with the quality dimension, but with the, like, is the, when you talk about editors spend too much time in the content, and it's a black box, and we don't have enough capacity, how does this relate to the capacity problem?

**Ryan Singer:** I'm not seeing the link to the too much time spent capacity problem.

**Marcel Santilli:** So, so in order for us to solve the capacity problem, we need to figure out what we're, like, targeting, right?

**Marcel Santilli:** Like, which is the definition of done, and that we know how to reproduce done again and again with the quality bar that is acceptable to them, right?

**Marcel Santilli:** There's no way to do that without actually going through this process and understanding what is their definition of done, and how do they define quality?

**Marcel Santilli:** Like, for instance, in biological terms.

**Ryan Singer:** They the editor, they being the editor, or who?

**Marcel Santilli:** Let's call it the editor, yeah, us, but let's call it the editor.

**Ryan Singer:** Uh-huh, uh-huh.

**Marcel Santilli:** And so in Biologica's case, like, their definition of done require, you know, medical research, fact-checking, it required, like, integrating the product description into the content, it required, like, there's, like, different things that were really important to them, right?

**Marcel Santilli:** Okay, uh-huh, And so we had to go and, like, go through that, and each one of those require an iteration.

**Marcel Santilli:** Like, get one right, but then the next two are off, and then you get the next one right, and then they give comments on the next one.

**Marcel Santilli:** And they're okay with going through that journey, but then the problem is, like, if you don't do it in our systems, then you don't know that you can actually reproduce it over and over again, and certainly you can't reproduce it if you have a new editor on that account.

**Marcel Santilli:** You're , essentially.

**Ryan Singer:** Uh-huh, uh-huh.

**Ryan Singer:** Okay, I think we're getting somewhere.

**Ryan Singer:** Let me capture that.

**Ryan Singer:** me that.

**Ryan Singer:** capture Thank you.

**Ryan Singer:** What I'm hearing is you can get through the process with an editor, one at a time.

**Ryan Singer:** The problem, okay, I think we're getting closer.

**Ryan Singer:** What about this process, when it's going right, is the thing that takes too long that doesn't scale, is it that you're more involved than you should be, or is it the teaching of it that you have to be involved?

**Ryan Singer:** Because you said, like, when we bring the next editor on, they're not going to be able to do it.

**Ryan Singer:** What is going to break down when you bring the next editor on?

**Marcel Santilli:** Think of it as if the comments are happening in a Google Doc, okay, from the client, as we're going through this process, then, and you have, like, this editor, Ada, right, who's assigned to the sprints, and then if the customer converts...

**Marcel Santilli:** They go into, like, a different team on the ongoing phase.

**Marcel Santilli:** And Ada is reading these comments.

**Marcel Santilli:** And she was also in the meeting where she did all these interviews with them.

**Marcel Santilli:** And she, like, internalized all this information.

**Marcel Santilli:** So as she's going through, like, she's internalizing and she's taking these shortcuts that are, you know, of, like, in Google Doc being, like, I'm going to accept this comment or I'm to edit this.

**Marcel Santilli:** I'm going to do that, right?

**Marcel Santilli:** And that will never capture anywhere or capture at all, right?

**Marcel Santilli:** The thought process of, like, hey, you have to rewrite this entire paragraph.

**Marcel Santilli:** You just did it.

**Marcel Santilli:** But, like, nowhere in the system was it captured because you did it in Google Doc, right?

**Marcel Santilli:** Okay, okay.

**Marcel Santilli:** You probably were up because it was substantially off because of this reason.

**Marcel Santilli:** And this is based on a comment that you read from Maggie three weeks ago, you know?

**Ryan Singer:** Got it.

**Ryan Singer:** Okay, I think I'm with you.

**Ryan Singer:** Let me see how I got it.

**Ryan Singer:** In the current world, one-to-one editor per client, you're getting...

**Ryan Singer:** Getting through the workflow, it's not that the editors take too long today or that it's too slow.

**Ryan Singer:** It's that as you look into the future, if you cannot extract the context that each editor has, if you can't make the context portable across editors, you're not going to be able to scale because you can't hire a new editor per client.

**Ryan Singer:** Is that right?

**Marcel Santilli:** Also, that editor is different when it gets transferred into the ongoing stream, essentially, by team.

**Marcel Santilli:** But then there's a transfer of accounts when they convert into 12-month contracts after the eight weeks.

**Marcel Santilli:** And so, like, they will have a lot of this stuff.

**Marcel Santilli:** They can go and listen to the calls, but they're not going to go open 12 Google Docs and try to look at comments from the past.

**Marcel Santilli:** I see.

**Ryan Singer:** So there's going to be, I think I got it now.

**Ryan Singer:** Okay.

**Ryan Singer:** So this calibration, this is part of the, there's this initial, there's this whole initial eight week, which is part of the initial sprint.

**Ryan Singer:** And then.

**Ryan Singer:** There's going to be this timeline is going to continue into the future, and then there's going to be a point in the future when the 12-month commitment starts, and that's – let me see if I got this right.

**Ryan Singer:** Now that's the bottleneck that we talked about.

**Ryan Singer:** That's actually where the bottleneck hits, because now you've lost all the context that you built in.

**Ryan Singer:** That's actually where the problem happens.

**Ryan Singer:** Aha.

**Ryan Singer:** Okay.

**Marcel Santilli:** All right.

**Marcel Santilli:** And, like, there's too much – there's, like, too much, like, heroics happening in the eight weeks.

**Marcel Santilli:** And, like, you know, highly skilled – it's our best people on the sprints, right?

**Marcel Santilli:** Like, is our best one, you know?

**Marcel Santilli:** And Sydney's our best one.

**Marcel Santilli:** And then it's, like, then they're no longer involved after week eight.

**Marcel Santilli:** And when you have a customer that's, like, low complexity, doesn't review the content, doesn't give a , like, we're fine.

**Marcel Santilli:** But then when you have a client – you know, a client that actually –

**Marcel Santilli:** And then we don't know why it dropped or why we're no longer meeting the bar of expectations because that wasn't documented anywhere, you know?

**Ryan Singer:** Yes, uh-huh, uh-huh, uh-huh.

**Marcel Santilli:** So then what you end up having is, like, in that side is, like, these editors now spending five hours to edit one piece of content, and you're just, like, you're supposed to spend 15 minutes or 30 minutes.

**Ryan Singer:** Matt, why are you spending a whole day on one piece of content?

**Ryan Singer:** So the editor spending too long is happening over here.

**Marcel Santilli:** Yes.

**Marcel Santilli:** Yeah, on the ongoing phase, you know, where they have to do five-ish outputs per week, and then each editor is assigned to three to four accounts.

**Marcel Santilli:** So they have to technically do, for a model to work, you know, 20 outputs a week, essentially.

**Ryan Singer:** Got it.

**Ryan Singer:** Got it.

**Ryan Singer:** At Okay, yep, uh-huh, got it.

**Marcel Santilli:** So like if you do 20 outputs a week and you're doing even one hour per, that's already pushing the envelope because you don't, people don't have more than 20 hours of like productive heads down time, know, between meetings and other things, you know.

**Ryan Singer:** Thank you.

**Ryan Singer:** Okay.

**Ryan Singer:** Okay.

**Ryan Singer:** Now I understand.

**Ryan Singer:** Okay.

**Ryan Singer:** So you believe that they, that there is something that can be done here where some kind of context that happened in this intensive heroic mode, something can be captured here that then can be leveraged here in order to create this speed up.

**Marcel Santilli:** That's right.

**Marcel Santilli:** Correct.

**Marcel Santilli:** so, so then like bringing back full circle is like the, the way like data labeling and post training and a lot of these things work, right?

**Marcel Santilli:** Where you're creating this data so that AI can improve the outcomes.

**Marcel Santilli:** It's like you have, it's not just like, let's say you have a pair.

**Marcel Santilli:** Just narrow it down to a paragraph.

**Marcel Santilli:** And let's say you make five small changes in that paragraph.

**Marcel Santilli:** That, and then you say AI and you tell AI, hey, here's the before and here's after.

**Marcel Santilli:** And the after is preferred, right?

**Marcel Santilli:** There's a lot of context lost there.

**Ryan Singer:** Yeah, it's not enough.

**Ryan Singer:** You need to know the actual things that the customer complained about or pointed out or suggested.

**Ryan Singer:** And that way you can kind of, because you need to actually model.

**Ryan Singer:** The thing you need to model is not like the transition of states.

**Ryan Singer:** You need to model actually what is the customer going to say if they appear over my shoulder right now.

**Ryan Singer:** So it's actually more of the signal is in the comments from the customer.

**Marcel Santilli:** Got it.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Can you click on this?

**Marcel Santilli:** Open this Google Doc that I just shared and then you see the kind of, it will click and think for sure.

**Marcel Santilli:** I'd send it to Zoom, the chat.

**Ryan Singer:** I'd send it to Zoom.

**Ryan Singer:** Bye.

**Ryan Singer:** I'll share my screen again, just so we're looking at the same things together.

**Marcel Santilli:** Then you should have, oh, you don't see the comments.

**Marcel Santilli:** I can share my screen, too.

**Ryan Singer:** There's some mode I need to be in to see comments.

**Marcel Santilli:** I'll switch it to the editor, so I can refresh the page now.

**Marcel Santilli:** I can share my screen.

**Marcel Santilli:** It might be easier.

**Ryan Singer:** Yeah, let's just switch.

**Ryan Singer:** Totally.

**Ryan Singer:** By the way, I've done editing on content before.

**Ryan Singer:** I've been the commenter here, and I totally get it.

**Ryan Singer:** When I'm the client, I want you to notice all the things I told you to change and never forget that.

**Ryan Singer:** And that's part of my quality expectation of the editor.

**Ryan Singer:** Do you know what mean?

**Ryan Singer:** You should know me now.

**Ryan Singer:** I'm totally with you.

**Ryan Singer:** I'm totally with you on this.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And I think the only thing here is that there's like these really, really nuanced things where it's like, for instance, like Clerk, they're like never use the word sign in or something or log in.

**Marcel Santilli:** You only use sign in because like log in means something else in our system and blah, blah, blah.

**Marcel Santilli:** Yes.

**Marcel Santilli:** There's just like little nuances.

**Marcel Santilli:** And then when we heard from customers that churn, like Rapid, for example, like, hey, you you guys did so good.

**Marcel Santilli:** guys did this, this, this, and this.

**Marcel Santilli:** But then it's like, we would tell you this.

**Marcel Santilli:** We put comments in docs and did all these things.

**Marcel Santilli:** And then like three months later, like you would, we still were catching those same mistakes.

**Marcel Santilli:** What the hell?

**Marcel Santilli:** Right?

**Ryan Singer:** Yes.

**Marcel Santilli:** And it would be like something that got lost in translation that is just so important to them.

**Marcel Santilli:** It's like those little like, you know, paper cut.

**Marcel Santilli:** That's just like, why do I keep, you know, why do you guys keep dropping the ball on this thing?

**Marcel Santilli:** You know, Totally.

**Ryan Singer:** Totally.

**Ryan Singer:** I think we got it.

**Ryan Singer:** I mean, like on the problem side.

**Ryan Singer:** I'm totally with you now.

**Ryan Singer:** Okay.

**Ryan Singer:** So this is about – okay.

**Ryan Singer:** So the question is, what is the – so on the outcome side, this thing is supposed to – we need to somehow know – we need to know – we need to remember and be able to apply the knowledge we have from the rounds of feedback we got from – from customers during the sprint phase.

**Marcel Santilli:** Is that right?

**Marcel Santilli:** And I would say that's the most important thing.

**Marcel Santilli:** And then the second to that is to understand what the F the editor interventions are doing.

**Marcel Santilli:** Because, like, we have no clue – the person that spent 15 minutes versus the person that spent five hours, what is the – like, why did you spend five hours?

**Marcel Santilli:** What exactly did you change and why did it take you five hours to change?

**Ryan Singer:** And we were just flying blind here.

**Marcel Santilli:** don't understand the before and after and the thought process behind the before and after of the human invention, which is the most expensive thing we have in the company.

**Ryan Singer:** Okay.

**Ryan Singer:** Okay.

**Ryan Singer:** So there's still another piece of the problem here, which is when the editors are spending the five hours, it's not only that the output is wrong and the customer gets pissed off because their expectations aren't met, but what is hard about this?

**Ryan Singer:** It sounds like a stupid question, but like, what is hard about like, hey, it's been five hours, like that took too long.

**Ryan Singer:** Is it, is it like, is it hard to measure?

**Marcel Santilli:** Is it that you don't know what to ask?

**Marcel Santilli:** It's happening off platform first.

**Marcel Santilli:** Okay.

**Ryan Singer:** Second.

**Marcel Santilli:** So we don't measure at all.

**Marcel Santilli:** So we don't measure.

**Ryan Singer:** Okay.

**Ryan Singer:** So, so, so, so when it, when it happens.

**Ryan Singer:** When it happens off-platform, you don't measure, okay, stupid question, but like, what's bad about that?

**Marcel Santilli:** We don't know if they're spending five hours or five minutes, one.

**Marcel Santilli:** Two, we don't know what they're doing with the time.

**Ryan Singer:** Three, we can't try, we can't make the next iteration easier, faster, better.

**Ryan Singer:** You don't know what to, you don't know what to do to fix it.

**Marcel Santilli:** Yeah, if they're spending five hours because actually the whole article was entirely off and had to rewrite the whole thing, that makes sense.

**Marcel Santilli:** They're spending five hours because they're like tweaking the intro over and over and over, I have no, like, this person should be fine, basically.

**Marcel Santilli:** know, so there's no way to.

**Marcel Santilli:** Exactly.

**Marcel Santilli:** Like, on one edge is like, we  up on the inputs.

**Marcel Santilli:** On the other edge is like, we  up on hiring this person.

**Marcel Santilli:** Yeah.

**Ryan Singer:** Uh-huh, uh-huh.

**Ryan Singer:** Yeah, yeah, totally, totally.

**Ryan Singer:** Uh-huh.

**Marcel Santilli:** But either way, we want to catch it.

**Marcel Santilli:** Yeah, yeah.

**Ryan Singer:** And then when it's going well, we also want to know, holy , this is amazing.

**Ryan Singer:** I just heard that.

**Ryan Singer:** We can catch when editors spend too much time on the wrong thing?

**Marcel Santilli:** Mm-hmm.

**Marcel Santilli:** Yes.

**Ryan Singer:** Okay.

**Ryan Singer:** Okay.

**Ryan Singer:** I kind of feel like this is concrete enough that I could imagine flipping over into solution space here.

**Ryan Singer:** Because I kind of feel like we finally got our hands around something.

**Marcel Santilli:** This is a story.

**Ryan Singer:** If I needed to go and retell this to somebody, I'm happy hear that.

**Ryan Singer:** We are almost halfway in.

**Ryan Singer:** You know, we've got 10 minutes until we're at the halfway point.

**Ryan Singer:** Let's just take a moment.

**Ryan Singer:** Let's

**Ryan Singer:** I wanted to actually check in and just make sure that, like, we're on track and this is progress for you with what we did so far.

**Ryan Singer:** So I heard that that's progress.

**Ryan Singer:** Can you just kind of give me a little bit of a, just give me some feedback.

**Ryan Singer:** Like, where are we versus where we started or where you started before we had the session for this problem?

**Marcel Santilli:** Like, this is an interesting, like, the whole dilemma for me here is one thing is solving the growthx problem.

**Marcel Santilli:** Like, a lot of those problems that we talked about is the challenge that we have running our own editors.

**Marcel Santilli:** Is there a path here where if the client is running the workspace, that they would have the same problems, you know?

**Marcel Santilli:** Like, is there a path here where, like, this whole calibration, like, assume that we can do the system, that the client is doing the calibration themselves, the system is learning what they're doing, and now the articles that we're doing when the client is operating will be right 80% of the time, you know?

**Marcel Santilli:** And then the tweets, like, if there is a legit problem where things are generating articles that...

**Marcel Santilli:** If five hours to edit, like, there's zero chance we can have this as a self-service product.

**Marcel Santilli:** If there is a calibration loss there that we can fix, and it turns into from five hours to five minutes, then there's a path.

**Marcel Santilli:** Like, hey, fine, you can also operate it, you know?

**Marcel Santilli:** So that's one thing that it's kind of off of this problem, but it's always stop of mind for our stuff.

**Marcel Santilli:** Like, are we building just a tool that's essentially an internet, a super powerful internet, or are we building a product that the client can operate more and more?

**Ryan Singer:** Well, this is kind of consistent with the whole forward deployed model, is that, like, you see the problems there, and then you bring them home, and then, like, Palantir, like, builds it into Foundry, and then it's there as a platform thing into the future, you know?

**Ryan Singer:** So that's kind of an understandable loop.

**Marcel Santilli:** And I think similar to Palantir, so far, what we hear from, I want to say at least 90% of clients, is that they do not want to do editing themselves.

**Marcel Santilli:** Even if the tool is incredible, even if it was 15 minutes, not five hours, right?

**Marcel Santilli:** Like, they just...

**Marcel Santilli:** Don't give a  enough, don't want to do it, and they don't feel like that's the thing they should spend their time on.

**Marcel Santilli:** They want to direct the work, they don't want to be in the weeds.

**Marcel Santilli:** Yeah, they would pick the opportunities, they would pick the strategy, and someone will execute for them.

**Marcel Santilli:** So that's where we think, even if a client operates the workspace, there will be an editor doing it.

**Ryan Singer:** It might not be direct employee from GrowthX, it might be from the market.

**Ryan Singer:** Uh-huh, yeah, uh-huh, uh-huh,-huh, yeah.

**Marcel Santilli:** But it feels like, to me, one of the most critical pieces in this whole thing is that if the client feedback is in our system, we figure out how to capture that and create a great experience for our clients to provide the feedback, a.k.a.

**Marcel Santilli:** like label where  is wrong and why it's wrong or why it's good.

**Marcel Santilli:** Like, then that one makes us way more sticky because if they churn, that's it, you don't get that.

**Marcel Santilli:** Yes.

**Marcel Santilli:** And that's like internal knowledge, internal black box that aren't even going to take it with you.

**Ryan Singer:** You're in the Dropbox model.

**Ryan Singer:** It's like, I'm never going to cancel.

**Ryan Singer:** My Dropbox account because I have the stuff in there, you know?

**Ryan Singer:** It's like the knowledge is there.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** Yeah.

**Ryan Singer:** But okay.

**Ryan Singer:** We're kind of riffing on like what will be great if we solve this.

**Ryan Singer:** So I think we should plan to steer back into the solving of it.

**Ryan Singer:** Let me propose we take five just to dehydrate and then pick up again.

**Ryan Singer:** All right.

**Marcel Santilli:** Copy up.

**Marcel Santilli:** Copy up.

**Marcel Santilli:** .

**Marcel Santilli:** Thank you.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** Thank Thank you.

**Marcel Santilli:** The main challenge is when we're mapping out the solution for this, I think we hit this point where it can't be not perfect anymore.

**Marcel Santilli:** Everything has to be super easy to learn, almost like you're doing a product-led, like a self-serving product.

**Marcel Santilli:** But in the beginning, could have things that a little changing because it would be a curtain operating or people that are close to us.

**Marcel Santilli:** Yeah, now it's it's kind of  for all that self-serving, you know?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** It's kind of like RBAI, you know, they started with like forward deployed and stuff like that.

**Ryan Singer:** Okay, gentlemen.

**Ryan Singer:** So I've already got ideas as we go on to the solution side.

**Ryan Singer:** And both of my ideas don't involve a text editor.

**Marcel Santilli:** So...

**Ryan Singer:** What we usually do, the thing I'm always doing in a shaping session is, okay, so what we've been doing in the first half is if we just give it a word, it's framing.

**Ryan Singer:** What's the gap, just like with your content, like what's the gap that we're filling, you know, like this is our understanding of the gap.

**Ryan Singer:** like the, what, we're not just, we don't have to circle around one idea, there can be like ideas A, B, C, that we can have a bunch of like different ideas which we can then use to create contrast and see like what, what, what do we want and not want.

**Ryan Singer:** I'm just going to throw out a couple things, because I know, of course, we can dive into text editor changes.

**Ryan Singer:** First place where my head goes is, you are in, you are in a high touch situation here in the eight week sprint period.

**Ryan Singer:** where where be at head is I think it's

**Ryan Singer:** People, so like, okay, this is already a special high-touch world.

**Ryan Singer:** The people are going to reach for the tools that they know how to use.

**Ryan Singer:** Trying to make somebody use a different editor if they are inclined to have a workflow they already know how to use and they know how to interact with clients and so on.

**Ryan Singer:** I have like a million red flags around like why I'm not going straight first to editor.

**Ryan Singer:** I'm happy to go there if you guys, you know what I mean, like if we can go there.

**Ryan Singer:** But like I'm seeing so many reasons why that's not going to work.

**Ryan Singer:** And so I'm inclined to say like is there anything that comes into my head as alternatives if I purely take these as the outcomes, you know.

**Ryan Singer:** If we had a way to do this and we had a way to do this and we didn't have to tell anybody during the sprint phase, this is how you should be working.

**Ryan Singer:** Um, and me.

**Ryan Singer:** Maybe this all breaks down, but this is just kind of where my head starts.

**Ryan Singer:** So, like, the first question I'm asking myself is, like, if I'm just super high level, like, is there a version of this where, like, can we consume the Google Doc and comments for training?

**Ryan Singer:** Like, can we just, can we take that as an input to get what we need?

**Ryan Singer:** And for, for, on the, on the speed of editing side, on the commitment side, like, is there literally a, this is, this is going to sound ridiculous, but I'm, I'm okay with putting ridiculous things on the table.

**Ryan Singer:** Is there literally, like, a, like an egg timer per edit, like, editing, I don't know what you call, like, a piece of content that is in the editing phase?

**Ryan Singer:** for, for, for, for, you.

**Ryan Singer:** Uh, uh, um, that, that triggers, uh, intervention, like these, there's a version of this of like, you know, like we're not controlling the editing process, but we are wrapping it around some kind of, we're communicating, uh, time expectations with the person who works for us.

**Ryan Singer:** We have, uh, I'm almost imagining like a, like a dumb kind of Kanban, like status flow per edited piece with very, very clearly with a contract of time limitation at check-in moments, you know, and like literally like after this much time has elapsed, there's a check-in and then there's a rating of like, you used your time wisely or you used your time stupidly, you know what I mean?

**Ryan Singer:** And then like three strikes and you're out, you know what I mean?

**Ryan Singer:** Like that's a, that's a workflow that can get built around editing tool chain that isn't necessarily in editing tool chain.

**Ryan Singer:** Same thing with kind of Google Doc.

**Ryan Singer:** So the place I would just start is, like, this is a high-level, like, starting idea.

**Ryan Singer:** Can you find fault with these things?

**Marcel Santilli:** Where do these things break down?

**Marcel Santilli:** Or is it worth digging into them?

**Marcel Santilli:** I think you might be onto something.

**Marcel Santilli:** So my comments, I think, are not going to be to say, like, no, this wouldn't work.

**Marcel Santilli:** Yep.

**Marcel Santilli:** But where I go back to, like, big question mark, is enforceability.

**Marcel Santilli:** Uh-huh.

**Ryan Singer:** Enforceability where?

**Marcel Santilli:** In training people to consistently do the way they need to do it.

**Marcel Santilli:** So meaning, hey, are you actually putting the comments in Google Doc?

**Ryan Singer:** Like, or now it's going to be, like, Google Doc and Notion and something else, right?

**Marcel Santilli:** Are you actually going through the process when you're supposed to go through the process?

**Marcel Santilli:** Are you actually going to the time tracker that we're

**Marcel Santilli:** It forced people starting last week, right, to use, and are you actually hitting play, or is that time tracker stopped working?

**Marcel Santilli:** Are you using the right browser, whatever, right?

**Marcel Santilli:** know what mean?

**Marcel Santilli:** It's like then, and then it's just like the next person that logs in instead of saying, hey, this is the system.

**Marcel Santilli:** We log in and do this, and we control that, and we can, like, track every click and everything, and that's just because it's ours.

**Marcel Santilli:** Like, and again, the AI editor might not be a thing either, right?

**Marcel Santilli:** Like, there's other ways to maybe do it.

**Marcel Santilli:** But we can talk about, like, that's where my head goes into possible on those two things, and I even just quickly ran a search.

**Ryan Singer:** There is a Google Drive API where you can ingest.

**Ryan Singer:** I'm sure there is.

**Ryan Singer:** Yeah, that's why it's, you know, so it's like, yeah, so, but it's like, that's where I go to, you know, it's like, now, how do we enforce that they even doing that?

**Ryan Singer:** Right, okay.

**Marcel Santilli:** And then the second thing, sorry, is client experience.

**Marcel Santilli:** When you share a Google Doc, it seems like we don't have good tech, essentially.

**Marcel Santilli:** It's kind of like, okay, clearly, like...

**Marcel Santilli:** Oh, that's interesting.

**Marcel Santilli:** It's not a platform.

**Marcel Santilli:** Another thing I would add here, Ryan, is that there is comments.

**Marcel Santilli:** Like, there are different kinds of comments.

**Marcel Santilli:** And that is, like, one of the things that would get lost as well.

**Marcel Santilli:** So you have comments, you have suggestions, you have, like, what went well, what went wrong.

**Marcel Santilli:** So this is more of a labeling of content than just, like, somebody commenting freeform.

**Marcel Santilli:** And there's, like, a teaching how to write comments, teaching the client how to write comments.

**Marcel Santilli:** It almost needs to be, like, a more structured commenting experience.

**Marcel Santilli:** Like, asking clarifying questions, for example, you know.

**Ryan Singer:** Okay.

**Ryan Singer:** Let me untangle the solution and problem from there.

**Ryan Singer:** What I'm hearing is that in the...

**Ryan Singer:** So I'm trying to capture ways that this doesn't work.

**Ryan Singer:** In the case where it's only comments, you're imagining that the comments themselves don't give enough signal about the...

**Ryan Singer:** Yeah.

**Ryan Singer:** The big comment.

**Ryan Singer:** Because comment is sort of a catch-all versus you're imagining from one comment type, versus you're imagining that if you had custom tooling for this, that you could have like suggestion versus something else versus something else, and that you were going to somehow have richer semantics on the feedback from the client.

**Marcel Santilli:** But so in the case of the document that we sent you earlier, like you don't see the comments, but there's a comment from Maggie, for example, in one part saying like, replace discomfort with changes, like why?

**Marcel Santilli:** And then there's like another one down the road that was just like, help with PMS symptoms, and she switches from like, support monthly conference.

**Marcel Santilli:** There's like a bunch of stuff that like, is this factually wrong?

**Marcel Santilli:** Like I would have to ask a question to be able to do that again and again and again, moving forward.

**Marcel Santilli:** But what is stylistic, what is actually

**Marcel Santilli:** If you're doing, like, a labeling system, in my mind, you're building a labeling system more than an admin tool.

**Marcel Santilli:** So, a labeling system has different, you need to pull the thread, you know?

**Marcel Santilli:** Yeah, and a good mental model here is, like, Legora, which is, like, legal AI.

**Marcel Santilli:** Legal AI happens to be, like, adjacent, not adjacent, but, like, similar problems because, like, there's a lot of nuance to getting it right, you know?

**Marcel Santilli:** And, like, Legora did the approach, like, kind of what you're suggesting.

**Marcel Santilli:** Like, they're, like, lawyers are just going to use docs.

**Marcel Santilli:** Like, they'll try to change them using actual docs, not even Google Docs, like, just, like, Word documents.

**Marcel Santilli:** And so they'll, like, a plug-in or add-on to that that sits on top.

**Marcel Santilli:** And whereas, like, Harvey AI did everything into their system, you know?

**Marcel Santilli:** So, it's, like, I'll just say, like, you can do both if the behavior is so ingrained.

**Marcel Santilli:** And then there's, like, pros and cons of both.

**Ryan Singer:** Yeah, I see.

**Ryan Singer:** Okay.

**Ryan Singer:** So let's flip to, since this doesn't feel like a no-brainer and there's a lot of missing pieces here, let's flip over into the thing that you guys already have in mind here.

**Ryan Singer:** So what does editing in your tool actually mean in terms of the current functionality versus new functionality?

**Ryan Singer:** So do you have an editor already?

**Marcel Santilli:** We do.

**Ryan Singer:** Yeah, we do.

**Ryan Singer:** So why, if we plug the current editor into this, why does the current editor not do this?

**Marcel Santilli:** The current editor is almost like an off-the-shelf tricks kind of thing that you guys have at base game with shortcuts that call AI.

**Marcel Santilli:** That's it.

**Ryan Singer:** This is the tip-tap editor?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** The tip-tap.

**Marcel Santilli:** Yeah, I see.

**Ryan Singer:** Okay.

**Marcel Santilli:** So let's flip to, since this doesn't feel like a no-brainer and there's a lot of missing pieces here, let's flip over into the thing that you guys already have in mind here.

**Ryan Singer:** So what does editing in your tool actually mean in terms of the current functionality versus new functionality?

**Ryan Singer:** So do you have an editor already?

**Ryan Singer:** We do.

**Ryan Singer:** Yeah, we do.

**Ryan Singer:** So why, if we plug the current editor into this, why does the current editor not do this?

**Ryan Singer:** The current editor is almost like an off-the-shelf tricks kind of thing that you guys have at base game with shortcuts that call AI.

**Marcel Santilli:** That's it.

**Marcel Santilli:** This is the tip-tap editor?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** The tip-tap.

**Ryan Singer:** I can call out RAI, we're closing to do it.

**Marcel Santilli:** Okay, got it.

**Ryan Singer:** So there's no commenting system, there's no revision system, there's like no version of tracking, there's not.

**Ryan Singer:** I see, uh-huh, okay.

**Ryan Singer:** And it's totally free-form, you know.

**Ryan Singer:** So what would this actually look like as a solution?

**Marcel Santilli:** Like I saw that there were mock-ups here.

**Marcel Santilli:** I think these are kind of like, I can think of these as mock-ups, yeah?

**Ryan Singer:** Yeah.

**Ryan Singer:** Of what you're intending.

**Ryan Singer:** And so if we are talking about, we are talking about receiving comments here.

**Marcel Santilli:** So there's this idea here of we are going to, where am I going here?

**Marcel Santilli:** There's this concept that we're going to add comments in, which is basically just like Google style.

**Marcel Santilli:** And this is already supported by TipTap, is that right?

**Ryan Singer:** Pretty close.

**Ryan Singer:** Yeah, they support.

**Ryan Singer:** Yeah,

**Ryan Singer:** We have somebody working on the product, just to how far we can gather with it.

**Ryan Singer:** Oh, yes.

**Ryan Singer:** Okay, because I remember seeing, when I was looking at, I think I was looking at TipTap, and they, was it TipTap?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Did they even show comments, I think, on their demo here?

**Marcel Santilli:** Yeah, yeah, yeah.

**Marcel Santilli:** So there is some built-in.

**Marcel Santilli:** You have full control, okay.

**Ryan Singer:** Okay, okay.

**Ryan Singer:** Yeah, so I think it's a lot less, tell me if I'm wrong here, Daniel, but it's a lot less, like, we're worried that it'll be hard to build.

**Ryan Singer:** It's more of, like, what should the experience be?

**Ryan Singer:** Yeah.

**Ryan Singer:** Or, like, we've never had a client-long interest system ever.

**Ryan Singer:** Yeah.

**Ryan Singer:** Right?

**Ryan Singer:** Like, so, like, this is a big opening Pandora's box here.

**Ryan Singer:** Yeah.

**Marcel Santilli:** Okay, so this is just one little piece.

**Marcel Santilli:** So, like, let's say we have the TipTap TipTap app.

**Ryan Singer:** Editor, Editor, Editor, with comments added, okay?

**Ryan Singer:** And let's say all the comments are happening in TapTap, and that's not the hard part.

**Ryan Singer:** So then you don't have clients logging in at all today, okay?

**Ryan Singer:** Nope.

**Ryan Singer:** So.

**Ryan Singer:** That's a big, like, an article.

**Ryan Singer:** This will have two users, you know, one is our, is somebody adding comments for learning and for taking that for the future and improving the article.

**Ryan Singer:** Yeah.

**Ryan Singer:** And another one is that kind person, like, taking that and applying it.

**Ryan Singer:** Oh, totally.

**Ryan Singer:** Yeah, totally.

**Marcel Santilli:** Okay.

**Ryan Singer:** Well, so the first place my head goes is anytime you have, anytime you're trying to get clients to, like, do stuff, it's always, like, path of least resistance, you know, to get them into the system.

**Ryan Singer:** You never want them to get blocked at, like, forgot password or something like that, because they're not going to bother.

**Ryan Singer:** They're just going to be like, can't you just put it into a Google Doc, which I already know how to use.

**Marcel Santilli:** And stuff like that, you know, so like, there's a, okay, so first place my head goes, it is, oh, this is going to be interesting, because there's going to be, there's a, okay, a bunch of different things we can put on the table, of course.

**Marcel Santilli:** So let's say we share a tokenized link, which is like the equivalent of like, I give you the public Google link.

**Marcel Santilli:** You know what I mean?

**Marcel Santilli:** And you just click it, and it just loads.

**Marcel Santilli:** There's the, there's the, I mean, there's the whole like, you, you have an account, and you have kind of like the dashboard of things that need your review, because you're not only looking at one article.

**Marcel Santilli:** Right.

**Marcel Santilli:** Right.

**Marcel Santilli:** To add to that, there will be other features that they want to see as well.

**Marcel Santilli:** So we have like an analytics that they want to see the traffic of the things that we've changed.

**Marcel Santilli:** They also want to pick the topics.

**Marcel Santilli:** So like those are things that we know that they want to use that out, to see that out, right?

**Marcel Santilli:** Yeah, there's other areas of the product.

**Marcel Santilli:** Like I guess maybe to rephrase that, it's inevitable that clients will need to log into our platform.

**Marcel Santilli:** But the form factor of that is a work in progress that we feel we have a good sense and parts of it are built, but not yet presented in the right way.

**Marcel Santilli:** But yes, and I would also say that the idea of the tokenized link is still relevant because you might not have the same person that will be operating, like looking analytics, be the person that comments.

**Marcel Santilli:** So in a place of time, for example, we have a marketer working with us, this looks great, I love it.

**Marcel Santilli:** And then they send it to a security expert.

**Marcel Santilli:** you.

**Marcel Santilli:** And that guy is the one who was there in the comments.

**Marcel Santilli:** they both added comments.

**Ryan Singer:** Like in the case of the document that I shared with you, the marketer is there, but the doctor is also there.

**Ryan Singer:** Yeah, totally.

**Marcel Santilli:** Totally.

**Ryan Singer:** Yeah, and this experience is almost like, so there's this company, there's like, what do you call, Highspot or something, where when you're going to send like a prospect, like a link to like a deck or something, or some of the, like, I think it was the interest list.

**Ryan Singer:** It one of those where it's just like, you're sending them to a slide that is like private information, they have to put in their email.

**Ryan Singer:** And then if they put in the email that is whitelisted, then they are allowed in, and they already know who they are based on that.

**Ryan Singer:** But it's like very low security, isn't it?

**Ryan Singer:** Like being like, you know, like if you knew, if you had that link, which would be nearly impossible for you to just randomly know that link, and you knew what email is whitelisted, so it technically gets access.

**Ryan Singer:** So from a security, a pure security perspective, it's not super safe.

**Ryan Singer:** Yeah.

**Ryan Singer:** Before it does.

**Ryan Singer:** Document that, you know, doesn't have any AI, who gives a , essentially, you know.

**Ryan Singer:** Sure.

**Ryan Singer:** This is so funny because this is like exactly what like Basecamp like launched on.

**Ryan Singer:** I mean, it is the core problem that Basecamp like got its foothold market in was the fact that you needed clients to give you comments on creative assets.

**Ryan Singer:** It was literally, literally this problem and the way, it's really funny.

**Ryan Singer:** I mean, the thing that worked really well for us was, I think actually this is the kind of the modern version of the core loop.

**Marcel Santilli:** You had two loops in Basecamp.

**Ryan Singer:** One loop was, or I mean, like sort of two parallel aspects of client access.

**Ryan Singer:** One is, anytime I'm asking the client to react to something, the tool was actually firing off an email.

**Marcel Santilli:** And the client could literally interact just by reading the email and hitting reply.

**Marcel Santilli:** So they didn't have to sign into the tool.

**Marcel Santilli:** Of course, this is very 2004, but like it was foolproof.

**Marcel Santilli:** And then when you have a deeper relationship with the client and it's like, I've got four different things I want you to look at, or I want you to know that I have this stuff on the record or you know what I mean?

**Marcel Santilli:** Like then you could bring them in, but usually what you would see is that there was kind of like a different levels of engagement of the client.

**Marcel Santilli:** And some clients would be more like a partner with you and they would, and there would be kind of like that one person who is your person at the client who would actually care to log in.

**Ryan Singer:** And 80% of the time it was more like they're getting the email and they have no idea what their password is.

**Ryan Singer:** And like, do know what I mean?

**Ryan Singer:** Like they're, they're not actually clicking through.

**Ryan Singer:** Um, the, the email loop was absolutely the primary loop, you know?

**Ryan Singer:** Um, and I actually think like air table, um,

**Ryan Singer:** Has gotten like indecently where on the sharing piece, because like you can share like essentially as a link, but you can just share a slice or a view where you can share the whole table or the whole workspace.

**Marcel Santilli:** And within your admin panel, you can see like every user that is in your quote unquote system.

**Ryan Singer:** And if they're only like a workspace permission versus like a table only, I'm using the wrong words here, right?

**Ryan Singer:** Like, but it's kind of like, it's pretty much a tokenized link, but you can also share via email.

**Ryan Singer:** Like Figma is kind of like that a little bit too, but yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** I mean, this, this part is not too, it's not very hard, actually.

**Ryan Singer:** There's a lot of little stupid things to get right.

**Ryan Singer:** But let's just, let's just carve this off for a moment.

**Ryan Singer:** And say, say.

**Ryan Singer:** We know that there's maybe some future where you have enough of a relationship that somebody's logging in, but you're always going to have this problem anyway, so might as well just focus in on this problem.

**Marcel Santilli:** Yep.

**Marcel Santilli:** So, I mean...

**Marcel Santilli:** This is kind of idea as well.

**Marcel Santilli:** I mean, this is like, I, this feels pretty, you know, kind of mundane to kind of spell out, so I'm not sure if it's, if it's, if it feels valuable to you or not.

**Marcel Santilli:** But, um, uh, we can, I mean, we can sketch what this whole kind of flow looks like, um, just to, to see if we can surface some, some questions, you know, um, just to get into some concreteness before we do that.

**Marcel Santilli:** Is there some, is there some other, uh, other unknowns?

**Marcel Santilli:** Or issues around this, or does this kind of feel like, oh, like we're getting a lot of it, we're getting a lot of it out of here.

**Marcel Santilli:** What are the other things we're not talking about that have questions or that might be hard?

**Marcel Santilli:** there to just like, just probe it if like there's an option C here?

**Ryan Singer:** Yes.

**Marcel Santilli:** And the option C here would be more of like a quiz-like experience that decomposes the calibration process and where you get that information, but it doesn't look like an editor.

**Ryan Singer:** It's more like decomposing the outputs, getting feedback, and it kind of like, you know, more of like a quiz and you know when you're done calibrating and it's more of like a fully interactive experience.

**Ryan Singer:** But quizzes are so  easy with AI now, you know, where like you can take all the context, can see like A or B, like this or that, you know, it truly feels like magical experience.

**Ryan Singer:** And then you're sharing that quiz, not a doc.

**Ryan Singer:** Because a doc can be like so many  things, you know.

**Marcel Santilli:** True calibration would be like when you say that buy us like a ton of time and get the data.

**Marcel Santilli:** And also, like, one of my main concerns is if, like, does it have to be the same experience?

**Marcel Santilli:** You know, like, does the person just, like, sharing comments because we need to get the comments has to have the same experience as the person that's adding in the text?

**Marcel Santilli:** Because adding in the text does the job, you know, and we can just make it better.

**Marcel Santilli:** This is a great, this is a really good question because I think this comes to the core of what is the signal that you need?

**Marcel Santilli:** What is the signal that you need in order to create the customer satisfaction that, like, we understood the edits that you want us to be making?

**Ryan Singer:** So, like, in the Google Doc, Marcel, that you shared earlier, I mean, there were a lot of individual, no, that's not right.

**Ryan Singer:** No, that's not right.

**Ryan Singer:** This should be this word instead.

**Ryan Singer:** This should be that word instead.

**Ryan Singer:** I'm having trouble seeing, like, how do you get that information in a quiz experience.

**Ryan Singer:** Yeah, that's good point.

**Ryan Singer:** Yeah.

**Ryan Singer:** Like.

**Ryan Singer:** Like, you need to, okay, so think of it as, like, there's different layers, right?

**Ryan Singer:** And so there's, like, stylistic layers, there's factuality layers, there's, like, quality of sources in the research layer, there's, like, you know, and then there's, like, applying that to an actual example and then seeing if it was applied correctly layer, you know?

**Ryan Singer:** And then apply correctly could also mean, was it, you know, was the research applied correctly?

**Marcel Santilli:** Was the, how you communicated an idea applied correctly, stylistically correctly?

**Marcel Santilli:** Like, there's a lot of layers, you know?

**Marcel Santilli:** Oh, okay, I see there.

**Ryan Singer:** Okay, okay.

**Ryan Singer:** Let me try and capture that.

**Marcel Santilli:** And then, so, like, the idea here, okay.

**Marcel Santilli:** Okay, um, uh, so, comments, comments, comments, comments a, comments is a catch-all to get, like, concrete things that they.

**Marcel Santilli:** They see that are right or wrong.

**Marcel Santilli:** It's like a highlighted comment.

**Marcel Santilli:** I'm just trying to talk this back.

**Marcel Santilli:** Like a highlighted comment is not going to be like a meta observation of like, tonally, this isn't where I want it to be or stylistically or something like that.

**Marcel Santilli:** But of course, you will get with an individual comment, a highlighted comment, you will get like, we don't use that word here.

**Marcel Santilli:** What I'm hearing is that in the Quizluck experience, there's other things that you want to ask about that are different from like, don't use that word.

**Marcel Santilli:** And I have an actual example of this as well, if you want, if I can show you how we know the calibration.

**Marcel Santilli:** Because I think this might click for you of like, why this hypothesis, where this hypothesis comes from.

**Marcel Santilli:** let's see it.

**Marcel Santilli:** So one of our clients, engine.com.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So, you know, we went through and then, you know, this is like what our artifact is like.

**Ryan Singer:** Hey, did we get this right?

**Ryan Singer:** You know, then we...

**Marcel Santilli:** We do the kickoff session with them, and it's like, hey, after the kickoff and some of the interviews, here's what we heard.

**Marcel Santilli:** Is this right?

**Marcel Santilli:** And then they can comment on it and say, like, did we get this right or not, right?

**Marcel Santilli:** And then after that, we're like, hey, this is the audience.

**Marcel Santilli:** Did we get this right?

**Marcel Santilli:** The personas, right?

**Marcel Santilli:** And then they're like, I'm just replaying what we said earlier and giving you an example, right?

**Marcel Santilli:** Then we're like, hey, this is what we're thinking for your writing guideline.

**Marcel Santilli:** Does this look roughly right?

**Marcel Santilli:** And then hopefully about that point, they're like, yeah, this looks great, but, like, let's see it, kind of, right?

**Marcel Santilli:** And then this is what I came up with as a calibration guide, right?

**Marcel Santilli:** And then my hypothesis here is, like, you're true.

**Marcel Santilli:** And then there's a whole process underneath it a little bit, but it's, like, very much like, hey, position, decompose things at the beginning in spectrums first, right?

**Marcel Santilli:** Like, and then, because it's, like, this is inspired by brand exercises where you're trying to create, like, almost like, hey, you want your...

**Ryan Singer:** Brandon, on this side of the spectrum and that side of the spectrum, you know, kind of, and it just forces people to not think in broad terms and more like pick where in the spectrum you think you should be, you know, and so this is, we just did it and show them so that they saw like our thought process.

**Ryan Singer:** But then this is the part that I thought was really good.

**Ryan Singer:** It was like, hey, now this is the calibration.

**Ryan Singer:** So then what I did is I took an existing piece of content they actually had and I ran it through our guidelines and everything else and I rewrote it.

**Ryan Singer:** But then I asked it to AI to just give me it in a table and then decompose it into like sentence level with a little bit of context.

**Ryan Singer:** Like, hey, this is the article that you had already and this is how we would have written it.

**Ryan Singer:** And this is what you had and this is what we did and this is why we did that.

**Ryan Singer:** Is this thing right or not?

**Ryan Singer:** You know, like, so that's like why that was informed and then this, when we presented to them, they were like, oh, whoa, this is so much better.

**Ryan Singer:** Wait, this is on our website?

**Ryan Singer:** And then it's like, it builds.

**Ryan Singer:** Trust with us.

**Ryan Singer:** it's just like, you know, okay, we're good, you know, but it's, it's hard to get right too.

**Ryan Singer:** What I'm seeing here, when I flip back to our frame, I think I'm seeing, there's a million ideas for how to level up all over this process, you know, and I think that this, I think that what, what, if we flip back to concretely what we would want to solve for January, it's, this loss of, this loss of like, we told you, and we're still seeing it.

**Marcel Santilli:** I think like, that's, so like, so the, so the thing is, if we, if we try to, so, so just talking about comments versus quiz, this is a little high level.

**Marcel Santilli:** If try to segment in terms of like, what are the specific changes that they are telling us?

**Marcel Santilli:** So what is the feedback?

**Marcel Santilli:** We.

**Marcel Santilli:** We to capture and not forget that they won't, because they'll get mad at us if we forget that, you know?

**Marcel Santilli:** I think that's different from what you just showed me.

**Marcel Santilli:** I think what you just showed me, it could play a really interesting role all throughout the lifetime of the relationship.

**Ryan Singer:** That's fair.

**Marcel Santilli:** Do know what I mean?

**Marcel Santilli:** Yeah, I think you're I think what you're talking about is kind of a recalibrating, it's a higher level thing than an individual piece.

**Marcel Santilli:** And this is more like the, there's these little touchy raw points that people have of like, do not make that same mistake again, you know?

**Ryan Singer:** Yeah, that's, you're right, and it's all based on the level of complexity.

**Ryan Singer:** So the more technical, the higher complexity ones.

**Marcel Santilli:** You do need to be deep into that topic to be able to like probe it, you know, to be able to find the failure modes and then label where the failure modes are, you know?

**Marcel Santilli:** But we want people to be in the mode of like failure mode, not little new ones.

**Marcel Santilli:** Hey, you know, this comment here could have been over there.

**Marcel Santilli:** That's like not super.

**Marcel Santilli:** What's valuable is you keep saying help, and you need to use the word support, because support signifies that you are a human being with a very complex system, and there's a lot of things playing a factor here, and it's not A leads to B here, it's like, you know, and B needs to understand, like, this supports this thing, but it can also, like, not be enough support to actually make an impact on the outcome.

**Marcel Santilli:** Okay, let me, I want to, I want to take a swing at oversimplifying this, and see if it's actually true.

**Marcel Santilli:** Is this about, like, you need to speak my language?

**Marcel Santilli:** It's, in this case, specifically, in a lot of cases, it's about applying your understanding of the nuances of their space.

**Marcel Santilli:** So for Clark, it's like, hey, you didn't actually understand my product, go read our docs and know that, like, we don't talk like that.

**Ryan Singer:** Yeah, that's not how our product works, right?

**Ryan Singer:** And the way you describe it makes it seem like you haven't even read my docs, right?

**Marcel Santilli:** In this case, it's like, hey, you're oversimplifying the relationship between supplements and health, you know?

**Ryan Singer:** And, like, there's so many more layers here.

**Marcel Santilli:** And when you're giving medical advice, you have to be really, really specific on what you're saying.

**Marcel Santilli:** You can't just, like, make these generic, like, statements.

**Marcel Santilli:** Yeah, like, first one is the health one, and the second one is the authentication clerk.com.

**Marcel Santilli:** So those are the, like, real examples.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** One churned, and the other one didn't, essentially.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Which one churned?

**Marcel Santilli:** This one?

**Marcel Santilli:** Clerk.

**Ryan Singer:** Yeah.

**Ryan Singer:** That, this one.

**Ryan Singer:** Yeah, no, the bottom one.

**Ryan Singer:** The bottom one churned, yeah, yeah.

**Ryan Singer:** Yeah, the bottom one is essentially...

**Ryan Singer:** Or the first sentence, you didn't understand my product, where it's, like, the oversimplifying relationship and supplements is, like, separate thing, but, yeah.

**Ryan Singer:** Ah, uh-huh.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** This is a separate thing.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Uh-huh.

**Marcel Santilli:** Uh-huh.-huh.

**Marcel Santilli:** Got it.

**Marcel Santilli:** Okay.

**Ryan Singer:** Yeah.

**Marcel Santilli:** There are different types of comments.

**Marcel Santilli:** You have comments about the language.

**Marcel Santilli:** You have comments about, like, indicates that we didn't understand their context.

**Ryan Singer:** You have comments on, this is factually wrong about, like, our product or the topic that we're writing about.

**Marcel Santilli:** Sometimes it's not about the product themselves.

**Marcel Santilli:** Uh there's all these, like, types of failure goals, you know?

**Ryan Singer:** Yeah.-huh.

**Marcel Santilli:** That will signify different solutions here in future.

**Marcel Santilli:** Or for the system that's going to create the next piece, you know?

**Marcel Santilli:** So, if we play this concreteness back into, into quiz versus comments, I'm, I'm, to me, it looks like quiz is going to be good at other things.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And, uh, um, and, and this is.

**Marcel Santilli:** This isn't about Google Docs.

**Marcel Santilli:** This is about the fact that the feedback is always referring to something you said.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Right?

**Marcel Santilli:** Feedback is always referring to something you said.

**Marcel Santilli:** Yes.

**Marcel Santilli:** It's reacting to some output.

**Ryan Singer:** Yeah.

**Ryan Singer:** Uh-huh.

**Marcel Santilli:** Uh-huh.

**Marcel Santilli:** Yeah.

**Ryan Singer:** Good.

**Ryan Singer:** Okay.

**Ryan Singer:** The one thing with editor, you're writing an editor, you can go deeper, and you're going to most, more likely expose failure modes of applying the knowledge and the inputs to an output.

**Ryan Singer:** Yes.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** Whereas, but it's bad at exposing the inputs.

**Ryan Singer:** So you won't catch failures of wrong inputs.

**Ryan Singer:** For instance, you won't catch, hey, you used the wrong  source here to do your research.

**Ryan Singer:** Two, you asked the wrong research questions here.

**Ryan Singer:** Like, right?

**Ryan Singer:** Like, or, like, it won't, or, hey, you applied.

**Ryan Singer:** The wrong, like, style or persona here, right?

**Ryan Singer:** Hey, your brief was completely off.

**Ryan Singer:** That's why this is wrong.

**Ryan Singer:** Your instructions to the system were wrong, right?

**Ryan Singer:** I see.

**Ryan Singer:** it catches the, your inputs are right.

**Ryan Singer:** Is the application of your inputs good?

**Ryan Singer:** Whereas the other one catches, like, did we get the inputs right?

**Ryan Singer:** Got it.

**Ryan Singer:** So we actually need It's so  hard, man.

**Ryan Singer:** I actually think, I think it's, I think we can boil, I think we can totally distill this into one idea.

**Ryan Singer:** So there's, we, we need to capture.

**Marcel Santilli:** So there's, there's these two different types of, of feedback that we're trying to capture.

**Marcel Santilli:** And it's kind of like, is it, is it like a kind of a commission versus omission thing?

**Marcel Santilli:** Like, like, so, so we need to be able to capture errors in, in, in, in, in what we wrote specifically.

**Marcel Santilli:** So what I'm doing is I'm just extracting a couple of requirements.

**Ryan Singer:** Daniel, think of this like a test suite, like I want to fail and pass, you know, so we need to be able to capture errors in what we wrote specifically, like support, not help, this kind of a thing, right?

**Ryan Singer:** Right.

**Ryan Singer:** But then what I'm hearing, Marcel, is that like, this isn't enough, because there are really important things that we could get wrong, which is like, you didn't even talk about blah, which is like the thing that you need to be highlighting when we are on this topic.

**Ryan Singer:** Is that the kind of thing that you meant when you referred to inputs?

**Ryan Singer:** Yeah, like by the time that that comment was there, we had gotten so many other things right, you know, that then it's like, you gave them the opportunity for that comment to even matter, you know, but if, if like, our research was wrong, or we use wrong sources, like, that, you're, you're effed, you know?

**Ryan Singer:** That is the example of a clerk, where they didn't care about certain types of vulnerabilities, didn't care about.

**Ryan Singer:** And we got the templates wrong because we weren't we ask that much.

**Ryan Singer:** Got it.

**Ryan Singer:** Very good.

**Ryan Singer:** Okay.

**Ryan Singer:** So I think B and C are both failing if they're alternatives to each other.

**Ryan Singer:** And I think what we're seeing instead is, so first of all, what we're seeing is that there's a piece of any of this, there's a piece of any of this, which is the tokenized link, whitelisted email.

**Ryan Singer:** There's some kind of a loop there, which is, which is the same regardless.

**Ryan Singer:** This is a, this is a separate subsystem, right?

**Ryan Singer:** Um, uh, but when it comes to the actual editing, I think what we, what it seems that we need is, is a, is a, let me pitch a hybrid.

**Ryan Singer:** Yeah.

**Ryan Singer:** Which is, um, tell us how we did, you know what I mean?

**Ryan Singer:** Like give feedback, whatever you guys are going to have better language.

**Marcel Santilli:** And it's like, um, uh, um, uh, step one, like.

**Ryan Singer:** Um, how do I say this?

**Ryan Singer:** It's like, I, I, I didn't even want to, I don't, honestly, I don't want to dig, I don't want to like fuss with layouts and stuff like that.

**Ryan Singer:** So I'm just going to do this with blocks, which is like, um, uh, um, fix localized errors by commenting in place.

**Ryan Singer:** Okay.

**Ryan Singer:** So imagine we've, we're doing that and, um, we have, um, present, um, a, um, uh, specific, how do I say this?

**Ryan Singer:** Present space for more general feedback.

**Ryan Singer:** But what I, what I think when I say more general feedback, I imagine Marcel saying, no, it's not general feedback.

**Ryan Singer:** I've got specific ways I don't ask, like, did we use the right sources?

**Ryan Singer:** And, uh, you know what I mean?

**Ryan Singer:** So let's say, we got, yeah, that's a more general would be like, higher level things that are not specific to the word.

**Ryan Singer:** Higher level.

**Ryan Singer:** I'm going to use higher level feedback.

**Ryan Singer:** And this is, I think this is actually the hybrid of the quiz and the comments.

**Ryan Singer:** What I'm picturing, just if I think of this in terms of a workflow, so I'm just kind of getting, I'm trying to get a little bit more concrete UX wise.

**Ryan Singer:** If they land on, there's a piece for review.

**Ryan Singer:** The piece for review has, just if I'm breadboarding this, it has, there's got to be like a, like a, like a thing that shoots off into the sharing loop.

**Ryan Singer:** For example, the client needs to be able to do that too.

**Ryan Singer:** Right.

**Ryan Singer:** Because like, it turns out they haven't, they want someone else to look at it or there's an SME that I didn't notify or whatever.

**Ryan Singer:** Right.

**Ryan Singer:** So like the client has a way to jump off to the share loop.

**Ryan Singer:** Then there is the read and, and comment on specific errors.

**Ryan Singer:** There is answer to tell us on a higher level how we did, which, by the way, I love this from a satisfaction point of view because nobody's ever – a Google Doc never asks this, right?

**Marcel Santilli:** And this is a thing where it's like the fact that you're asking and listening is already a satisfaction increase.

**Marcel Santilli:** Of course, you have to follow up on it later, but the fact that you're asking is huge.

**Marcel Santilli:** And then what I'm picturing, which I think is also missing from a Google Doc, is submit.

**Marcel Santilli:** Right.

**Marcel Santilli:** There isn't a moment, you know what mean, when, like, I'm done.

**Marcel Santilli:** I think this presents interesting questions because what does this mean if multiple parties need to review?

**Marcel Santilli:** So this is like – is this like I as Ryan?

**Marcel Santilli:** I'm done.

**Marcel Santilli:** Mark, that, you know what mean?

**Marcel Santilli:** Like, I have a submission from Ryan that this is okay, and like, I might get, do I have one submission per piece, or do I have multiple submissions per piece?

**Marcel Santilli:** I mean, those are the kind of questions my head goes to here, but I'll pull back and let you guys react to this.

**Marcel Santilli:** It comes up less often than you would think, and when we do it right, and when I say when we do it right, it's like, so when we go and actually do the deep dives with the SMEs, the subject matter experts, and the people, and we go spend the time with them, like, doing that hour-long, ask questions, figure out what they care about, why they care about those things, tell me about the product more, tell me about, like, you know, all those things, and we actually use those transcripts and actually process it and put it into the context that we have, and it drives a lot of the strategy prior to getting to this piece, then it's already, like, kind of, like, baked into everything a lot more.

**Ryan Singer:** It's just, when, like, clerk example, we didn't do that.

**Ryan Singer:** Like, we had a marketer who wasn't technical, who up to week four was just like, yeah, let's

**Ryan Singer:** That's good.

**Ryan Singer:** Yeah, that's fine.

**Ryan Singer:** Yeah, that's fine.

**Marcel Santilli:** And then you had editors that didn't think to, like, wait, wait, time out.

**Marcel Santilli:** It's the  technical product.

**Ryan Singer:** Like, this is not okay.

**Ryan Singer:** There should not be no feedback here in this process.

**Ryan Singer:** And you did no technical deep dive in the first four weeks.

**Ryan Singer:** What is wrong with you, right?

**Ryan Singer:** Like, then at that point, these things, like, always, like, will spiral out of control.

**Ryan Singer:** And this experience won't fix that because we didn't get input, any inputs, right?

**Ryan Singer:** So if you have zero inputs, you're going to fail here.

**Ryan Singer:** But assuming we do our job right, which is a separate problem, and we get inputs, then by the time you get here, it's more about, like, the nuances and what did we not ask and what did you not tell us?

**Ryan Singer:** Like, you know, it's like finding gaps in failure modes here in this way.

**Ryan Singer:** Like, like, but this won't replace, like, all the inputs we're getting from that, right?

**Ryan Singer:** Like, we're doing, like, six or five, seven, like, hour long interviews with these people.

**Ryan Singer:** This is, this is the, this is the fine tuning.

**Ryan Singer:** This is, this is, this is the fine.

**Marcel Santilli:** Okay.

**Ryan Singer:** So like supervised fine tuning is the way to think about it.

**Ryan Singer:** Like supervised fine tuning.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** Totally.

**Marcel Santilli:** So this, this is the, this is the fine tuning, but it's, it's also, let's, let's, let's capture what this is doing.

**Marcel Santilli:** This, this is happening inside of the sprint, right?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** So we're in the sprint.

**Marcel Santilli:** This is not just some general, it's not like this solves your quality issue.

**Ryan Singer:** This, this is, you expect to have gaps and things that you want to get feedback on when you're inside the sprint.

**Ryan Singer:** You expect to do a good job going up to this, right?

**Ryan Singer:** That you're providing, you've done everything up to this to, to provide the good inputs.

**Ryan Singer:** And then crucially, when, no, I don't know what this, when the submission happens, what is, there's something happening under the, behind the hood.

**Ryan Singer:** Which is remembering and now doing the actual fine-tuning, right?

**Ryan Singer:** So, like, what does that actually mean?

**Ryan Singer:** Yeah, it's almost like you can think of it as, like, you do this, like, supervised fine-tuning, in some ways, a mix of, like, almost, like, learning, you know, like, human feedback piece here.

**Marcel Santilli:** And then you have to, like, retrain the pipeline, essentially, or figure out how to apply all these things to the pipeline.

**Marcel Santilli:** So let me ask you this.

**Ryan Singer:** Yeah.

**Ryan Singer:** Let's make it concrete.

**Ryan Singer:** So, Daniel, this, if this is a place that I go as a front-end experience in the app, and this is something that happens in the back-end, behind the scenes, what has to happen after a client submits their specific errors and their general higher-level, you know, feedback?

**Ryan Singer:** What has to get done?

**Ryan Singer:** Like storing, processing, blah, blah, blah.

**Ryan Singer:** Just like what needs to happen?

**Ryan Singer:** And then where does that get surfaced in the future?

**Marcel Santilli:** So that like, because we did this, you know what mean?

**Marcel Santilli:** Like this is happening later on.

**Marcel Santilli:** There's a few different layers.

**Marcel Santilli:** So it depends.

**Marcel Santilli:** So if it's like stylistic, essentially everything boils down to settings for either style or research.

**Ryan Singer:** Those are usually the two things that we're going to adapt.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So you're going to capture style issues.

**Marcel Santilli:** You're going to capture, what is the other class?

**Marcel Santilli:** Factuality issues.

**Marcel Santilli:** Okay.

**Marcel Santilli:** You're going to capture factuality issues.

**Marcel Santilli:** And the styling one is a little bit nuanced too because you might have formatting versus way of writing.

**Marcel Santilli:** So there's a lot of stuff in between.

**Marcel Santilli:** So there's kind of style versus voice.

**Marcel Santilli:** Like where style is like we don't put a comment there and voice is like this is what we would say, this is how we would talk.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** And then you have a bunch of layers within that.

**Marcel Santilli:** So you'd be like how you talk about the product versus how you talk about the space and etc.

**Marcel Santilli:** Usually like today, this is like one of the big parts that we're trying to solve here.

**Marcel Santilli:** Or some of the things today would turn them into documents that get fed into the prompts.

**Marcel Santilli:** So it's a change in the prompts basically.

**Marcel Santilli:** Add in context to the So we have a few agents.

**Marcel Santilli:** We have a style agent that will do post-processing.

**Marcel Santilli:** So some of the comments will be injected into that style agent.

**Marcel Santilli:** And we have a research agent that will do sources.

**Marcel Santilli:** Sort of like calibrate the sources.

**Marcel Santilli:** And we have a drafting agent that will calibrate structure and things like that.

**Marcel Santilli:** But even that alone, like the way we do today isn't enough.

**Ryan Singer:** As.

**Marcel Santilli:** And like, many of the things will have to be actually retrained in the model, like reinforcement learning.

**Marcel Santilli:** So it's not traditional off-the-shelf models.

**Marcel Santilli:** And that's the last 10% that's super hard to get it right.

**Marcel Santilli:** In my mind, this to me, if we crack that part, that is the part that's uncharmable, where you're actually getting a super, like, you don't want people to manually calibrate this.

**Ryan Singer:** Like, today we're manually calibrate.

**Ryan Singer:** So we take these comments and we write these documents that say, do this, do that, do it.

**Ryan Singer:** Like, we're manually creating these settings, documents that get fed into prompts.

**Ryan Singer:** But that shouldn't be done by humans.

**Ryan Singer:** So like, for example, like, let's say a client says, never use support, never use help, won't use support.

**Ryan Singer:** Today, one of our people will go into the artifacts, documents, their one called writing guidance.

**Ryan Singer:** They will edit the writing guideline and they'll put a comment saying, never use help, use support, but that document can't grow into infinity.

**Ryan Singer:** So that is a common problem.

**Ryan Singer:** People would just add all the comments in that context document and that would set the agent to fail it.

**Ryan Singer:** So there needs to be an opaque black box system that will be able to understand the comments that you're able to do, that humans don't touch, unless it's a former employee engineer.

**Ryan Singer:** So, so here's, here's an important place in the shaping where we hit an issue.

**Marcel Santilli:** We, what I want to do is for the, for the, for a moment, just so just temporarily in order to make progress on this, I want to black box how we remember and how this gets embodied into the knowledge of what to do.

**Marcel Santilli:** And I want to just get to the other side of this and then we can, we can, we can triangulate around it to figure out what the requirements are and what's enough progress in January.

**Marcel Santilli:** So like

**Marcel Santilli:** If this happened, whether it was, however it happened, where would we actually see this?

**Ryan Singer:** Is this going to be like pre-screening what the, so there's the hero editor and then there's the like normal editor in the 12-month commitment, right?

**Marcel Santilli:** So like, where is the moment when like human versus hero, like when the normal human editor, are they getting like a pre-screen on these things?

**Marcel Santilli:** Or like, how does this actually surface so that this doesn't happen?

**Marcel Santilli:** So like the way I would think about it is maybe like you go through this process and let's say you do round one, right?

**Marcel Santilli:** And you share this calibration with the right person and then I go through and then let's just assume this black box here in the middle, we're going to do a bunch of voodoo magic manually, right?

**Ryan Singer:** But at least we have the inputs to do the voodoo magic and figure out if that's the right voodoo magic to then automate later, right?

**Ryan Singer:** So then at the end of that, we're going to rerun the whole piece again, and then see, hey, did we get this right, or run through this process again, and see, hey, this time around, like, is this good or not?

**Ryan Singer:** Okay, we're still in the first loop inside of the sprint.

**Ryan Singer:** Right.

**Ryan Singer:** But then an exit criteria.

**Ryan Singer:** That exit criteria is like, this is good to publish.

**Ryan Singer:** Like, that's the exit criteria.

**Marcel Santilli:** And once you hit that exit criteria, now, it's like most clients are like, this is good.

**Marcel Santilli:** Now, this piece is good to publish.

**Marcel Santilli:** Now, let's do it again.

**Ryan Singer:** And then again, and again.

**Ryan Singer:** And then by the fifth or so, they're like, cool, I don't need to review this as much.

**Marcel Santilli:** And then others are like, no, this is so nuanced, I need to keep reviewing.

**Ryan Singer:** But it's okay, because like, I usually need to spend an hour.

**Ryan Singer:** We're reviewing your .

**Ryan Singer:** And now I'm only spending 50 minutes and catching almost nothing.

**Ryan Singer:** I see.

**Ryan Singer:** And that's okay for some clients.

**Ryan Singer:** Let me, let me, let me try to capture this in another way.

**Marcel Santilli:** So there's a loop here.

**Ryan Singer:** There's a.

**Ryan Singer:** The loop here, which is like, there needs to be a decision.

**Ryan Singer:** I don't know where this happens.

**Ryan Singer:** I'm going to call this like state management of piece for review.

**Ryan Singer:** Sometimes I use a verbose name when I don't have a name.

**Ryan Singer:** And it's like needs another round or ready to publish or like approved or there's this kind of, you know what I mean?

**Ryan Singer:** Maybe there's a submit, apply, rerun, like some version of that, you know what mean?

**Ryan Singer:** So this is from the client's perspective.

**Ryan Singer:** Right.

**Ryan Singer:** Yeah.

**Ryan Singer:** Yes.

**Ryan Singer:** Okay.

**Ryan Singer:** So then there is some state management piece that happens from the, is this the editor making the judgment based on the feedback they got?

**Ryan Singer:** Or, uh, who makes this judgment?

**Ryan Singer:** You can be, Hey, today I have.

**Ryan Singer:** Okay, so let's say that there is some, so this is, we're already exposing more things that have to get solved here, but that's our job in this shaping session, right?

**Ryan Singer:** So there's some kind of, this needs another round, this is good to go, are there any other states?

**Ryan Singer:** That's basically it, right?

**Ryan Singer:** If it needs another round, if it needs another round, then the, there's going to be a, there was a, what I'm going to do is I'm just going to do like, there's going to be a editor produces draft step, right?

**Ryan Singer:** And then the editor is actually going to share this.

**Ryan Singer:** Let me, let me make, give us some more room.

**Ryan Singer:** Now we're starting to actually kind of see this whole thing.

**Ryan Singer:** This is all, we know that this is in the sprint context.

**Ryan Singer:** I don't need that anymore.

**Ryan Singer:** Let's make some more space.

**Ryan Singer:** So there is a share.

**Ryan Singer:** I'm going to.

**Ryan Singer:** I'm going to elide this because there's TBD share UI and process there, right?

**Ryan Singer:** Actually, better, let's be stronger about that.

**Ryan Singer:** Like share flow TBD, let's actually just kind of call that out as a whole.

**Ryan Singer:** And that way we see that that's where work is and go in there.

**Marcel Santilli:** There we go.

**Marcel Santilli:** Okay.

**Marcel Santilli:** And there's a share flow TBD.

**Marcel Santilli:** So then what we've got is there's also, by the way, a share flow there.

**Ryan Singer:** The editor, if it needs another round, they actually have to go make that other round, right?

**Ryan Singer:** And they're going to have to fire off share again because they're going to have to, again, it's not a Google Doc.

**Ryan Singer:** Google Doc is just ongoing access.

**Ryan Singer:** This is actually, this is a key thing for us to observe that share isn't share.

**Ryan Singer:** Share is actually like share, like with request to review.

**Ryan Singer:** You know what mean?

**Ryan Singer:** It's like, it's more like an an ask.

**Ryan Singer:** It's an ask that happens to entail access and a token and blah, blah, blah, you know?

**Ryan Singer:** So I'm going to even call this like ask slash request review flow.

**Marcel Santilli:** And then that's going to be the same thing, share, ask, et cetera.

**Marcel Santilli:** Then there's a lot of what's the share ask here on the client side?

**Marcel Santilli:** Yeah, ask an expert or like someone else in their team that doesn't have log in, like in the case of Clark, for example.

**Marcel Santilli:** So if I have flagged still, let me just grab this, sorry, just for- Because it gets in.

**Marcel Santilli:** I'm always happy later if I bother to do this very visible thing.

**Marcel Santilli:** I think there's unknowns here around like, is this important?

**Ryan Singer:** Do you need this?

**Ryan Singer:** If you do it, what does it mean to submit if you have multiple people involved?

**Ryan Singer:** Do you know what mean?

**Marcel Santilli:** Like-

**Marcel Santilli:** I don't think this is automatically in scope and good, but I wanted to raise it as something that could bite us or needs thought.

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** In the case of biological, for example, Ryan was giving feedback, and then Maggie jumps in and gives more feedback, and they're all like, who is sharing that?

**Ryan Singer:** You know, do we send it to two people?

**Ryan Singer:** Do they send internally?

**Ryan Singer:** I think right now, though, like, what I've observed is that, for the most part, like, we know who needs to be the go-no-go here, and that we need input from in this round.

**Ryan Singer:** And so it's, like, it's a single person, and they know when, like, they're out of their scope.

**Ryan Singer:** Like, so I think, like, we can, I personally think we can remove.

**Ryan Singer:** Let's do it.

**Ryan Singer:** Perfect.

**Ryan Singer:** Let's do it.

**Ryan Singer:** Now, that loop is important, where you still need an editor to decide there's more here to be done.

**Ryan Singer:** Yeah, exactly.

**Ryan Singer:** not done yet.

**Ryan Singer:** So this is actually the editor reviewing the review, right?

**Ryan Singer:** Right.

**Ryan Singer:** Yeah, that's perfect.

**Ryan Singer:** Yeah, exactly.

**Marcel Santilli:** Yep, yep.

**Marcel Santilli:** And then making a judgment call that later on we can figure out if it was the right or wrong judgment call.

**Marcel Santilli:** So this is actually, this is another, this is an important thing.

**Marcel Santilli:** This is, this is like, this is a, this is actually the creation of a review.

**Marcel Santilli:** Do you know what mean?

**Ryan Singer:** This isn't just, because, because what's going to happen is this should happen.

**Marcel Santilli:** And then, so this is going to raise questions.

**Marcel Santilli:** If, if there's another round, does this mean that after sharing again the new round, that it's a blank, it's a blank sheet?

**Marcel Santilli:** Because that's a different expectation than in Google.

**Marcel Santilli:** So in Google, you make a comment, you tell me it should be support, not help.

**Marcel Santilli:** And then I, I mark it as like, it's like done.

**Marcel Santilli:** And you sort of see that that happened.

**Marcel Santilli:** Like, do we care about, do we need to actually try?

**Marcel Santilli:** Rack, you know, like here's where you said it should change and here's where it changed or.

**Marcel Santilli:** I don't like, so, so there's two different things, right?

**Marcel Santilli:** Like, and I think what we're trying to do is one, the other.

**Marcel Santilli:** And then let me explain.

**Marcel Santilli:** So there is change this thing in order to hit publish.

**Marcel Santilli:** Then there is learn why I asked to change this thing and try to rerun this thing.

**Marcel Santilli:** And see if it got it right the next time around.

**Marcel Santilli:** that you have higher confidence that you can consistently get it right in other use cases or the other applications of it.

**Marcel Santilli:** And we're trying to do that.

**Marcel Santilli:** Then later on, it's a completely separate thing.

**Ryan Singer:** If there's a reviewer in the loop, like, like a lawyer, like a senior partner is always going to, like, do not  send this document to a client, like without my review, check off, right?

**Ryan Singer:** And that is like, in a lot of complex, like environments, that's always going to happen.

**Ryan Singer:** Like, because people just do.

**Marcel Santilli:** are not going to trust anyone, you know, like I'm, you know, I don't trust my copywriter to post the LinkedIn post on my behalf.

**Marcel Santilli:** I might never do that, even no matter how good I think the system is kind of thing, you know, I'll that example.

**Marcel Santilli:** But so like, we're not trying to say this is going to fix that quote unquote, and then you never need to review anything.

**Marcel Santilli:** It's just like, like many clients that a lawyer still needs to read it.

**Marcel Santilli:** Even if it's like 100% of the time, there's zero comments, a lawyer still needs to review it, right?

**Marcel Santilli:** So what we're trying to catch is like, hey, right now this is getting a 70% right, and that's not good enough to publish.

**Marcel Santilli:** And we need this calibration to get us to like publish ready.

**Marcel Santilli:** And publish ready or, you know, acceptable level of quality so that like ongoing it's okay based on their complexity, their, you know, appetite for risk.

**Marcel Santilli:** Let me see if I understood.

**Marcel Santilli:** So this is, this is, this is more about that it's directionally right, and it's less about like, like.

**Marcel Santilli:** Every word final approved?

**Marcel Santilli:** Correct.

**Marcel Santilli:** Exactly.

**Marcel Santilli:** Okay.

**Marcel Santilli:** It's published.

**Marcel Santilli:** Yeah, yeah, exactly.

**Ryan Singer:** Yeah.

**Ryan Singer:** It's like, think of it as like, no one will ever get 100% because it's subjective, right?

**Marcel Santilli:** And the closer you get to trying to get to 100%, the more it's an infinite hole.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Right?

**Marcel Santilli:** And then every company has a level of complexity and a appetite for risk, right?

**Ryan Singer:** So if you are a public company in a highly regulated industry with a highly picky like audience in a very technical topic, then that bar is super  high and really hard to get to, right?

**Ryan Singer:** And the opportunity cost of getting it wrong is really high, right?

**Ryan Singer:** Or like the, you know, and so then you're trying to solve for that differently, right?

**Ryan Singer:** Whereas like, if you're in a consumer, like lovable as a client, they don't give a .

**Ryan Singer:** Like they're like just public.

**Ryan Singer:** We just need to grow, like, we're okay with slight slop here or there, like, just  go as long as, you know.

**Ryan Singer:** So there is a different workflow for that, like, legal needs to see this and ensure that this word changed to that word.

**Ryan Singer:** It's not what we're trying to solve here.

**Ryan Singer:** Is that right?

**Ryan Singer:** Correct.

**Ryan Singer:** And then later on, there is things we can do to make that process less cumbersome of, like, when a lawyer posts a comment that, hey, you need to have this thing here.

**Ryan Singer:** Don't ever make this claim this way, you know.

**Ryan Singer:** Yeah, yeah.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** Separate.

**Ryan Singer:** And that's not what we're solving for a year right now.

**Ryan Singer:** Perfect.

**Ryan Singer:** Got it.

**Ryan Singer:** Okay.

**Ryan Singer:** That's excellent.

**Ryan Singer:** That really belongs in the frame, which is like, well, I'll do it like this.

**Ryan Singer:** Not perfect final review, e.g.

**Ryan Singer:** by lawyer.

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** Yeah.

**Ryan Singer:** So, okay.

**Ryan Singer:** Okay.

**Ryan Singer:** Um, I want to, um.

**Ryan Singer:** Call out a couple things as we, I'm seeing a few missing things that I want to make sure we hit, seeing that we have 30 minutes left.

**Marcel Santilli:** I've got one little thing here, and then I want to jump into like what's actually happening in this loop and where does it lead.

**Marcel Santilli:** But, you know, I'm even going to hold back the little thing just so that we make sure we don't lose time.

**Marcel Santilli:** Let's say we get through a round, we do another round, we reach a point where it's good to go.

**Marcel Santilli:** Now, some black box process, which is important, which needs to be shaped, but it's not, it's, something is happening where we are now learning from this.

**Marcel Santilli:** The question is, when does that learning actually show itself in the experience again?

**Marcel Santilli:** Are we, are we out of the eight-week sprint and we are in the 12-month commitment?

**Marcel Santilli:** And where are we when it's like, oh, I'm really glad that this happened here instead of in Google Docs, because now it's surfacing or it's preventing something from happening.

**Marcel Santilli:** Yeah, I think the, oh, man, this is tough.

**Marcel Santilli:** So we don't know yet is maybe a good place to start of what is the right control, like what is the right signal that will tell us whether this is having a meaningful impact.

**Ryan Singer:** What we do know is like, if we can measure whether editors are spending five hours or five minutes, then hopefully this will have a positive influence on that.

**Ryan Singer:** But we don't even have that data yet.

**Ryan Singer:** Right.

**Ryan Singer:** So we can't even know, like we wouldn't be able to know if this is working or not.

**Ryan Singer:** But the easiest thing to know overall is like outputs are not getting bottlenecked.

**Marcel Santilli:** AKA we are contractually signing up to do five articles a week and we are delivering.

**Ryan Singer:** Five hours a week with the capacity we had allocated for this client, right?

**Ryan Singer:** So that's the easiest, like, to, like, things are not getting  and clients are not being, like, what the hell, this is garbage, you know?

**Ryan Singer:** And, you know, but, like, is there a metric today that we look at every day?

**Ryan Singer:** Absolutely not.

**Ryan Singer:** Yeah, and I wonder what the shape that could be.

**Ryan Singer:** Like, is there something that the client would see or if it's just an internal thing, you know?

**Ryan Singer:** Uh-huh.

**Ryan Singer:** Like, number of interventions or, like, Let me, let me, let me, me, I want to, I want to propose that we carve this into two different problems.

**Ryan Singer:** I think that there is, there is a problem.

**Ryan Singer:** So actually what's happening is there's, I think there's, there's two different projects here that are just so close in the same workflows in the same tech that that's why they're coming together into one project.

**Marcel Santilli:** And it might be fine.

**Ryan Singer:** But this problem is different than this problem.

**Ryan Singer:** Yep.

**Ryan Singer:** Yeah.

**Ryan Singer:** Absolutely.

**Ryan Singer:** Exactly.

**Ryan Singer:** Finished solving this problem yet.

**Ryan Singer:** So what I want to do is stay with that problem for a moment, knowing that we have the too much time spent problem under this line.

**Ryan Singer:** So my dumb solution would be if we can model the client and we want the client to be sitting over your shoulder, even if you are now the new editor and you weren't there before, then we should have basically a simulated client review.

**Ryan Singer:** Right.

**Ryan Singer:** So like I'm going to do – if I – I don't know where that lives, but basically it's something like I've got a – I need to – I've got a – here, I'll do a dumb version of it.

**Ryan Singer:** Yeah, yeah, yeah.

**Marcel Santilli:** Let's say you were required somehow – I think also this is an interesting enforcement question, by the way.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Get simulated client review.

**Marcel Santilli:** I'm going to, here's a dumb version.

**Marcel Santilli:** Paste your article.

**Ryan Singer:** Submit.

**Ryan Singer:** Okay.

**Ryan Singer:** Simulated client review.

**Ryan Singer:** What is this?

**Ryan Singer:** What are we actually going to see here?

**Ryan Singer:** So we're going to see, we should see probably comments.

**Ryan Singer:** It's almost like we should see the same thing the client did, right?

**Ryan Singer:** Like, it's almost like this.

**Ryan Singer:** No, not this.

**Ryan Singer:** It's almost like, you know what mean?

**Ryan Singer:** Like, like, uh, uh, uh, That's literally how we built the, for Biologica, based on the comments, we built

**Ryan Singer:** Like was a medical reviewer that literally decomposes the article into passages and then annotates the passages and then suggests improvements to all those passages and then it goes through that loop over and over again until it passes the thing kind of, So this just surfaced an unknown.

**Ryan Singer:** There's a UI question about when the editor reviews the review, what do they see?

**Ryan Singer:** There's a version, like my option A would be they literally see just the review itself.

**Marcel Santilli:** Do you know what mean?

**Marcel Santilli:** Like they see the review and they see, they see both of these things.

**Marcel Santilli:** Like they almost like see this thing as an artifact.

**Marcel Santilli:** Like imagine this is a piece of paper that the, that the client submits to you, you know, and it's, and it's, it's, got their pen handwriting all over it.

**Marcel Santilli:** And you're just like literally looking at the worksheet, you know, I'll just, I'll just capture that so that we have it, which is, this could literally just be like, um, um, um,

**Marcel Santilli:** Yeah.

**Marcel Santilli:** The worksheet, you know what I mean?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Then what we could be doing is we could be showing you the simulated worksheet.

**Marcel Santilli:** Right.

**Marcel Santilli:** And then we could have the same thing, needs another, like, mark as, like, needs edit or good to go, right?

**Marcel Santilli:** Same thing again.

**Ryan Singer:** know what's funny?

**Ryan Singer:** Like, everything you're describing here is literally what we whiteboarded when the APD was here and we had the whiteboard, which was, like, the way data labeling works in some ways.

**Ryan Singer:** It's, like, in some cases, like, once you establish a reward function, like, you know, then you're, like, re-looping and then you're self-optimizing because now you've gained confidence that your reward function is good, right?

**Ryan Singer:** And then what we're doing here in some ways is, like, putting an expert in the loop and then later on.

**Ryan Singer:** Like figuring out like, hey, who's the reviewer of the review?

**Ryan Singer:** Like it can be like a level two editor, then a level three editor reviews.

**Ryan Singer:** That's how we did it at scale and others like, you know, because, and then, you know, and then eventually you consolidate and then you can do better like one shot attempts.

**Ryan Singer:** You know, right now you don't have the confidence to do a one shot attempt yet, you know?

**Ryan Singer:** Yeah, yeah.

**Marcel Santilli:** So this is the first moment where I kind of feel like I'm, I'm seeing, I'm seeing an end to end story, you know, of like, this is where we learned never do that.

**Marcel Santilli:** And this is where the system told the editor never do that.

**Marcel Santilli:** The thing that I'm missing here as I think an important unknown is, um, uh, how do we enforce that this loop happens?

**Marcel Santilli:** Right.

**Marcel Santilli:** Um, have another one too, that I want to flag after your thought.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** So, um, just, just to, to, to play this out briefly.

**Marcel Santilli:** I'm imagining that there needs to be something like a – if you don't click submit here in this app – so I'm looking for a control point in the flow, right, or a gate.

**Marcel Santilli:** If there is a place in the app which is like if you don't submit here, you didn't do the work, that would be the place where this could happen.

**Marcel Santilli:** So do you have such a place today?

**Marcel Santilli:** No, and just so I don't forget, I just want to flag one thing that's really critical is that there is no equivalent of like a sign-off, right?

**Marcel Santilli:** Like so an editor-in-chief in a publication would normally have to sign off on something depending on how the publication is run.

**Marcel Santilli:** And right now, like in many of our clients, there is this informal sign-off that happens in Airtable at times.

**Marcel Santilli:** And what's happening to most clients, if you go to our Slack channels which share clients, it's like an editor will pay –

**Marcel Santilli:** It's five links to five Google Docs and say, hey, this is ready for your review.

**Marcel Santilli:** And then they'll sometimes paste the comments, sometimes go, hey, just a few comments on two out of the five.

**Marcel Santilli:** The rest is ready to go.

**Marcel Santilli:** It's good to go.

**Ryan Singer:** Let's hit publish, right?

**Ryan Singer:** And then someone has to take that and actually, like, hit publish, you know?

**Marcel Santilli:** And so right now we don't have this.

**Ryan Singer:** Let's call it, like, staging and sign-off area for clients.

**Ryan Singer:** And that staging and sign-off areas could be our editor-in-chief doing that.

**Marcel Santilli:** It could be our client doing that.

**Marcel Santilli:** It could be a stakeholder of that client doing that, right?

**Ryan Singer:** And that was always, like, very critical for me in pre-AI era.

**Marcel Santilli:** And because we don't have that control point, which maybe touches on some of that stuff, then it's like we don't actually know when done was done and if done was done right ever.

**Marcel Santilli:** Because, like, you could go through this in an editor and just make a judgment call.

**Marcel Santilli:** Let's just hit publish.

**Marcel Santilli:** Or it's just sitting in this, like, you know, they still need, like, like, they're good to go, they would still have to copy.

**Marcel Santilli:** And then still go back to the clients, like, did we get this right?

**Marcel Santilli:** Can I actually publish this?

**Ryan Singer:** You know?

**Ryan Singer:** That's really interesting.

**Ryan Singer:** And they never get a formal approval in the system or a signal that we can measure in the system if it's not in our system.

**Ryan Singer:** That is interesting.

**Ryan Singer:** Okay.

**Marcel Santilli:** This editor.

**Ryan Singer:** It's gnarly cookie thing.

**Ryan Singer:** Oh, it's totally solvable.

**Ryan Singer:** It's just amazing how there's so many layers to it and there's so many, the system stretches really far.

**Ryan Singer:** This person works for you, right?

**Marcel Santilli:** Yep.

**Ryan Singer:** Yes.

**Ryan Singer:** So this is definitely solvable in the sense of, like, do this step or you're fired, right?

**Ryan Singer:** Yes.

**Ryan Singer:** Yep.

**Ryan Singer:** Yeah.

**Ryan Singer:** That part is.

**Ryan Singer:** But what is not captured today is a formal approval.

**Ryan Singer:** This is public from the client.

**Ryan Singer:** sign off from the client.

**Ryan Singer:** From the client.

**Ryan Singer:** From the client.

**Ryan Singer:** To know if, like, we actually did hit that publish ready.

**Ryan Singer:** Not all.

**Ryan Singer:** Clients would want to do it.

**Ryan Singer:** Some would be like, just do whatever you want.

**Ryan Singer:** But like, it would be important to have that lever to say.

**Ryan Singer:** So guys, here's what I want to propose.

**Ryan Singer:** My instinct when I hear all this is to say, again, I'm always bouncing back to the frame and to the time constraint.

**Ryan Singer:** If we're looking at like January, solving this problem, then I think what happened is we raised something, something very constructive, which is that there's this, there's this other problem.

**Ryan Singer:** Yeah.

**Marcel Santilli:** There's this other problem that needs to get solved, which is around, which is all about client sign-off.

**Marcel Santilli:** Yes.

**Marcel Santilli:** And this is not about this, in this scope, in this project, in this thing we're solving right now.

**Marcel Santilli:** Right.

**Ryan Singer:** And for the time being, there was some kind of a like, like you must do this understanding with the editor.

**Marcel Santilli:** I don't know exactly what that looks like.

**Marcel Santilli:** So there's still...

**Marcel Santilli:** I think this is still a red flag, but this isn't a rabbit hole of how the heck are we going to handle client sign-off.

**Marcel Santilli:** I think this is a boundable, you know what mean, thing of like, but there is a need to introduce a checkpoint.

**Marcel Santilli:** I'm curious if there's a need to introduce a checkpoint, does this give us a measurable moment down here?

**Marcel Santilli:** Is there any, is there any, do we get any leverage on this?

**Marcel Santilli:** It seems like there's overlap.

**Marcel Santilli:** If you're still in calibration, right?

**Marcel Santilli:** So there's like three separate things.

**Marcel Santilli:** There's like calibration and feel like the system is repeatable enough to now go in steady state of execution.

**Ryan Singer:** Like, and this is mostly what I think we're solving for here.

**Ryan Singer:** Is this, by the way, is this also called calibration?

**Ryan Singer:** This sprint time?

**Ryan Singer:** Yes.

**Ryan Singer:** It's not only, calibration is one of the several things we do to do about eight-week sprints.

**Ryan Singer:** But yeah.

**Ryan Singer:** Yeah, got it.

**Ryan Singer:** Okay.

**Ryan Singer:** Calibration is the process of, like, do we know how to get something to publish ready?

**Ryan Singer:** Ideally, get 12 months to already calibrate it, you know?

**Ryan Singer:** Yeah, it's like an exit criteria, ideally, right?

**Ryan Singer:** once you're calibrated, which means, like, you calibrated, you hit publish, then you try it again, and then you try it again, and now, by week 8, you're publishing daily, one piece of content a day.

**Ryan Singer:** Basically, during the calibration, you're building the simulator.

**Ryan Singer:** Like, if we're going to build, like, I'm thinking, like, how do we solve that, like, what's in gray area?

**Ryan Singer:** Like, a practical way of doing this now, it would be to be building the simulator, and then you get it out, and the simulator exists, you know?

**Ryan Singer:** Okay, let me, let me throw, I want to just throw something on the table, solution-wise, into this area, and then, and then let's just kind of lift up our heads with 15 minutes left to see how we can tie this off as a single set.

**Ryan Singer:** I've got one dumb idea for this area, which is, the dumb idea I have is like, I'm thinking of it as a probationary period.

**Ryan Singer:** Like when there's a handoff, you know what I mean?

**Ryan Singer:** You don't just like drop it from your hand completely and it's like, now it's your problem.

**Ryan Singer:** But it's kind of like, how do I, how does the hero editor or a more senior person, when we talk about enforcement, somebody has to be the enforcer, right?

**Ryan Singer:** And to be the enforcer, you need to be like, there's got to be something that you can look at and watch.

**Ryan Singer:** So the dumbest thing that I can think of is, is, is, is almost like a new, I don't know what to call this.

**Ryan Singer:** I'm going to call it like new, new editor on task monitor.

**Ryan Singer:** And the new editor on Task Monitor is literally like, I want to, it's like a log of pieces produced with timestamps of simulations run, you know?

**Ryan Singer:** and like, and then, and then, um, with, um, aggregate of, um, uh, um, like if you, if, if I have to do this per piece, you know what I mean?

**Ryan Singer:** Like, then I should also be seeing three simulations ran on three, three pieces in the last day.

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Or, or one simulation ran on one piece in the last week, which would be a red flag.

**Marcel Santilli:** You know what I mean?

**Marcel Santilli:** Like some kind of like an aggregate of like, of pieces simulated per time unit.

**Marcel Santilli:** I don't know what that is, but.

**Marcel Santilli:** Basically, I'm picturing like the minimal version of this is like a single report, which is kind of per, do you know what mean?

**Ryan Singer:** And there's a threshold here of like what that is.

**Ryan Singer:** So like if I'm seeing less than X pieces per T unit time, you know what I mean?

**Marcel Santilli:** Like, then it means either you're not simulating, you might be producing fine, but you're not simulating.

**Marcel Santilli:** Or like you are simulating, but you're not getting enough pieces through.

**Marcel Santilli:** Like your throughput is too low.

**Marcel Santilli:** You know what I mean?

**Marcel Santilli:** Like, so this is kind of the throughput piece of it.

**Marcel Santilli:** And this is something where we're, we're leaning on this.

**Marcel Santilli:** And then we're doing kind of like, think of it like the bare minimum admin panel that the higher level editor or the overseer is looking at.

**Marcel Santilli:** Yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** We'll be spending definitely next three hours a month.

**Ryan Singer:** Daniel was like, before the session, like, you know, if we have more time, we can tackle two or three.

**Ryan Singer:** We can tackle the whole company.

**Ryan Singer:** Yeah, pretty much.

**Ryan Singer:** If I zoom out, you know, and I look at kind of what did we solve and what did we not solve, I On that note, on the simulator part, when you were putting it, like, are you visualizing something in your mind?

**Ryan Singer:** Or, like, I'm trying to picture the same report that you're thinking.

**Marcel Santilli:** And, like, what would be the user workflow here?

**Marcel Santilli:** Here?

**Ryan Singer:** Yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** So, like, let's say, for example, you have 10 articles to produce.

**Ryan Singer:** You go, like, you press the button, they're drafted, you go there, and you hit the button to simulate what the client would do, and then you address everything.

**Ryan Singer:** That is a simulation complete, right?

**Ryan Singer:** That's what you're thinking.

**Ryan Singer:** So, what I'm thinking is, um, uh.

**Ryan Singer:** No, there are unknowns here.

**Ryan Singer:** There are limits to what we can do in three hours.

**Ryan Singer:** My first thought here is if, so let's get a little more, let's just get concrete for a moment.

**Ryan Singer:** If the thing that I get is, so let's just take like, what does a review look like?

**Ryan Singer:** A review, just in general, whether it's human or simulated, let's, let's treat it as the same object.

**Ryan Singer:** Right.

**Ryan Singer:** Right.

**Ryan Singer:** Because I, I, it's the same information.

**Ryan Singer:** Yeah.

**Ryan Singer:** It's the same, it's the same loop.

**Ryan Singer:** Right.

**Ryan Singer:** I'm going to have to have actual text with individual problems of a, you use the wrong word.

**Ryan Singer:** And I'm going to have to have, um, uh, these, um, higher level questions that you deem to be the right.

**Ryan Singer:** Right.

**Ryan Singer:** Questions to ask where somebody can fill in and say, you missed the mark on this, but this was good.

**Ryan Singer:** You didn't do this right, but this was right.

**Ryan Singer:** Or you know what I mean?

**Ryan Singer:** These are the high level quiz questions, right?

**Ryan Singer:** Okay.

**Ryan Singer:** So then this is the place where my head goes first from a UX standpoint is that there's a version of this, which is the worksheet, which is like just ink, no pen.

**Ryan Singer:** And then there's the filled out worksheet, which is ink and pen.

**Ryan Singer:** So there's going to be just ink, you know, which is like this.

**Ryan Singer:** And then there's going to be ink and pen.

**Ryan Singer:** And then this is what I'm looking at as a reviewer.

**Ryan Singer:** This is going to raise questions because if I'm here and I'm not in Google Docs and I actually have these localized edits, I do need to track them.

**Ryan Singer:** Right?

**Ryan Singer:** Right?

**Ryan Singer:** Right?

**Ryan Singer:** Right?

**Ryan Singer:** So I think that this is a place where getting concrete surfaced an issue.

**Marcel Santilli:** Let me just capture that.

**Marcel Santilli:** I think this does raise a question around how do we track?

**Marcel Santilli:** How do we make sure that I nailed all these individual things?

**Marcel Santilli:** These things are not the individual things that I can nail.

**Marcel Santilli:** This is the, like, you didn't use the right sources, go try it again.

**Marcel Santilli:** But this stuff shouldn't fall through the cracks.

**Marcel Santilli:** You know what I mean?

**Ryan Singer:** So these specific things, let me just, I just want to, like, I'm specifically referring to this.

**Ryan Singer:** Yeah.

**Ryan Singer:** I need to somehow not get lost, right?

**Ryan Singer:** So what I'm picturing is that the simulated client review is paste your article, hit submit, see this.

**Ryan Singer:** And the AI is going to tell me the same answers that I would normally be asking.

**Ryan Singer:** And then I think the same question applies.

**Ryan Singer:** Yeah.

**Ryan Singer:** Of, there is a question or a follow through of how do I track this, right?

**Marcel Santilli:** Does that answer your question?

**Marcel Santilli:** Yeah, it does, it does.

**Ryan Singer:** Like a lot of this, like we're getting into too, in the simulation is like, there's several kind of startups of like literally an entire startup just build them, building these, potentially like digital twins and synthetic users to automate it for different use cases here, but like to kind of simulate that stuff.

**Ryan Singer:** Yep, yeah.

**Ryan Singer:** but that's one of those things where it's gonna feel, it's gonna feel like one of those normal things, like everybody who has a SaaS app in 2004, like knew how to write to a database.

**Marcel Santilli:** And it's kind of like, you know what I mean?

**Marcel Santilli:** Like this is kind of one of the new things.

**Marcel Santilli:** It's not really a product.

**Marcel Santilli:** It's actually just a slice of a vertical thing that you, it's a thing you have to integrate into an other workflow, right?

**Marcel Santilli:** For it, that's where the value is.

**Marcel Santilli:** You have to calibrate the idea.

**Marcel Santilli:** Because you can, all the value is in the loop here, right?

**Marcel Santilli:** And this is actually a big part of the hard part of like the things that you choose to learn on.

**Marcel Santilli:** And the fact that you have a moment when you surface it to the right person later and it's actionable, okay.

**Marcel Santilli:** So when you think about the throughput metric there, you're thinking about how many simulations the person ran, right?

**Marcel Santilli:** Yeah, so what I'm doing, I'm grabbing for data that I think we have if we do this.

**Marcel Santilli:** And I'm just asking, like, can we just hack it out of that data?

**Marcel Santilli:** Is that enough to give us an indicator?

**Ryan Singer:** And I think it's enough, it's a good poor man's throughput indicator, especially because I think that all, there's a lot of scope here.

**Ryan Singer:** Assume the research is good.

**Ryan Singer:** Yeah.

**Ryan Singer:** There's a lot of scope here.

**Ryan Singer:** I the research is good because, like, some of these might be, like, depending on the level of complexity, to have, I'm going to call it digital twin that can simulate an actual expert.

**Ryan Singer:** Like, sometimes it might be, like, fetching the right data.

**Ryan Singer:** It might be, like, a rag problem versus, like, you know, um...

**Ryan Singer:** Like, for instance, like, if you're trying to build a digital twin of a lawyer, obviously that's, like, you're building, like, a whole, you know, massive company.

**Ryan Singer:** I think, like, even if don't nail the digital twin, people's judgment to say this is ready for approval is enough for, like, this person thinks this is good, you know?

**Ryan Singer:** Yeah.

**Ryan Singer:** So that is, like, a part of the system that we're getting here to manage.

**Ryan Singer:** I think there is an open question here around, like, there is a question here of, like, how much of a gap does this reduce in, you know, of loss of, there's a loss that's happening between the hero editor and the normal editor.

**Marcel Santilli:** And I think there are questions around how much of the gap that you can reduce.

**Marcel Santilli:** But the thing is that what you don't have at all today is any kind of plumbing or UX framework where that kind of, you can give any kind of a diving catch at the last moment to be like, don't say that word.

**Marcel Santilli:** You know what I mean?

**Marcel Santilli:** Like, so I kind of think.

**Marcel Santilli:** Like, the framing of this as a first project in order for it to not get out of control has got to be more around, like, don't touch the third rail with this client.

**Marcel Santilli:** You know what I mean?

**Marcel Santilli:** And, like, there's going to be probably a long tail of, like, how do you actually help this editor to be more and more successful?

**Marcel Santilli:** And it's going to involve a lot of strategies.

**Marcel Santilli:** It's going to be bigger than the scope of this, of what we're doing right now.

**Marcel Santilli:** But you should feel that you have some kind of a – I think an important outcome here is that, like, we know where to surface those things or, like, where that back and forth happens, you know?

**Ryan Singer:** Yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** Cool.

**Ryan Singer:** I guess, like, the only big question mark for me, if we take a step back, is, like, what that experience looks like in that loop of the piece for review client POV to submit.

**Ryan Singer:** Like, that, to me, is, like, big question mark of, like, you know, that feels like it needs to be understood.

**Ryan Singer:** Is it like a quiz?

**Ryan Singer:** it an article?

**Ryan Singer:** Is it an article with a commentary?

**Ryan Singer:** it A, B, and C?

**Ryan Singer:** Is it A, B, and C plus a comment?

**Ryan Singer:** it A, B, and C?

**Ryan Singer:** know what I mean?

**Ryan Singer:** I'm trying to read a comment for specific errors, but you need to give instructions.

**Ryan Singer:** You need to give context of what the thing they're reading is.

**Ryan Singer:** Right?

**Ryan Singer:** Does this look like, you know, maybe it is quiz-like, you know, and more like a, there's just like, I can see this going multiple directions potentially, depending on what.

**Ryan Singer:** see.

**Ryan Singer:** There's a, there's a lot of room for different ways to do this.

**Ryan Singer:** What I would propose just to start with a simple, just to give, just to give us a starting point would be, um, um, so like what literally, literally this.

**Ryan Singer:** Um, uh, so this is, this is like, so

**Ryan Singer:** This is the piece.

**Ryan Singer:** This is tip-tap with, you know, with ability to comment, okay?

**Ryan Singer:** Like, this is, then here we're saying, like, this is ready for you to review.

**Ryan Singer:** It's the blah, blah, blah you were expecting.

**Ryan Singer:** Do know what mean?

**Ryan Singer:** Like, there's going to be, there can be, like, a hello, this is what you're doing here.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** To your question, Marcel, I think there is room here for, now, I'm just, like, you know, this could be a whole, we could spend an hour just on this, but just to get, like, some fundamentals in place, it could be basically, like, first, like, catch any specific errors.

**Ryan Singer:** You know what I mean?

**Marcel Santilli:** Yeah.

**Ryan Singer:** And, like, second, second, tell us, like, what we got wrong.

**Ryan Singer:** Now, you're going to have better language for all this, and this isn't the right thing, but you see what I mean?

**Ryan Singer:** Like, right thing, be

**Ryan Singer:** We're basically saying, like, we need review from you.

**Marcel Santilli:** The other thing that I would think about, if I'm just thinking about this from a UX point of view, is I would think about, can I contextualize this as being about, this is like, I almost want to brand this as like, like, deep sprint mode.

**Ryan Singer:** Do you know what mean?

**Ryan Singer:** Week two.

**Ryan Singer:** Like, I don't know exactly what this is, but what I'm trying to say is like, don't expect this every time we ever create content for you.

**Marcel Santilli:** You are, you are in a, you are in a certain, like, what we are doing is we are learning from you in order to get you set up to scale.

**Marcel Santilli:** Right?

**Marcel Santilli:** So like, that's why we're asking this from you.

**Marcel Santilli:** That's why you should, you should feel motivated to really lean into this.

**Marcel Santilli:** And like, think about it.

**Ryan Singer:** And give us feedback here.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** And then the end of this is like, you know, submit my review.

**Ryan Singer:** I think if we position this as like, we're building a digital twin of your experts, and you are one of the experts we're trying to build a digital twin of.

**Ryan Singer:** Yes.

**Marcel Santilli:** Then people are going to feel like this is an investment to like, clone my thought process, you know?

**Ryan Singer:** I think that's really important.

**Marcel Santilli:** Like, this is not just some general content feedback.

**Marcel Santilli:** This is an investment.

**Marcel Santilli:** It's specifically for you.

**Marcel Santilli:** Like, you know what I mean?

**Marcel Santilli:** Like, you're building an asset that we can talk about in a tangible way.

**Ryan Singer:** It's like, hey, why does this get wrong?

**Marcel Santilli:** It's like, well, we built a digital twin of, you know, Alex over there or whatever.

**Marcel Santilli:** But then we didn't build a digital twin of this other person you didn't tell us.

**Marcel Santilli:** Needed to be a digital twin of, right?

**Ryan Singer:** Like, so, like, that's why we got this part wrong, you know?

**Ryan Singer:** Exactly.

**Ryan Singer:** And then this is where also, you know, you can communicate, like, when you're inside of a sprint, you can even set expectations.

**Ryan Singer:** Like, after we get this, we are going to be extracting from it, and we're going to, you know what I mean?

**Ryan Singer:** Like, blah, blah, blah, right?

**Ryan Singer:** So, yeah.

**Ryan Singer:** It's like, hey, we built a digital twin of an endocrinologist, but not of a holistic doctor.

**Ryan Singer:** Like, you need to tell us that we need to build a digital twin of a holistic doctor to review the endocrinologist.

**Ryan Singer:** Like, yeah.

**Ryan Singer:** Marcel, does that answer the...

**Marcel Santilli:** Yeah, that's helpful.

**Marcel Santilli:** I think we just need to spend a lot of time on that because, like, I don't know if it's, like, multiple rounds.

**Ryan Singer:** You do one round, then you go next, and then you give more context, and then you address that, you know, and you rerun it between step one and two.

**Ryan Singer:** Or if really, like, one long guess, 5,000-word article, and then at the bottom of that, there's, like, there's some experiences there to feel magical.

**Marcel Santilli:** Cheers, Cheers, folks.

**Marcel Santilli:** Give people a little bit of feedback so that they're not in this one-hour session without feedback.

**Ryan Singer:** Yeah.

**Ryan Singer:** This alone is something that you can, there's no limit.

**Ryan Singer:** It's like your editor problem you were talking about.

**Marcel Santilli:** There's no limit to how good this can get.

**Marcel Santilli:** The way that I would flip this around in order to move faster would be to say, what is the minimum we need here in order to perform this loop?

**Marcel Santilli:** Okay.

**Marcel Santilli:** That's helpful.

**Marcel Santilli:** Because this loop, this whole loop, the reason this stuff is on the page today and we wrestled to get to it in this three hours is because you need to do this whole loop in order for this problem to stop.

**Ryan Singer:** Yeah.

**Ryan Singer:** And that's what this project is about.

**Ryan Singer:** So if you keep going back to the frame of like, if we do this, when are we done?

**Ryan Singer:** When are we done?

**Ryan Singer:** When are we done?

**Ryan Singer:** We're done for the first cut of this when like the new editor isn't making stupid mistakes mistakes that they should definitely are, that they have already heard they shouldn't do.

**Ryan Singer:** Yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** That's super helpful, reframing.

**Ryan Singer:** I'm even going to rewrite this as, like, the new editor will not repeat mistakes that they were already told about.

**Marcel Santilli:** We can be sure the new editor will not repeat mistakes they're already told about.

**Ryan Singer:** So, like, this is what this project is about.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** Okay, cool.

**Ryan Singer:** That's helpful.

**Ryan Singer:** Yeah, because, like, we flagged essentially those other two buckets we flagged, and then we also flagged the other one, on the top right there, not about.

**Ryan Singer:** There's, like, three other buckets that later on I need to address.

**Ryan Singer:** Yeah, so every time.

**Ryan Singer:** That bucket, yeah.

**Ryan Singer:** Exactly.

**Ryan Singer:** Every time you're working on a project at the founder level, you're always, you can't help but see all the other things that you want to improve, right?

**Marcel Santilli:** So then what we're doing here is we're hitting those things, but then, like, what I'm doing every time I draw this line is we're touching the wall, and we're saying that's a wall, and that's a separate resource allocation and a separate time commit.

**Marcel Santilli:** But

**Marcel Santilli:** Do you know what mean?

**Marcel Santilli:** And that's the thing that enables us to ship is to make those, is to do that kind of carving down.

**Marcel Santilli:** Okay, guys, I do have a hard stop.

**Marcel Santilli:** This is awesome.

**Marcel Santilli:** Please don't lose this sheet that you just came up with.

**Marcel Santilli:** Okay.

**Marcel Santilli:** I'm hitting the download button right now so that we don't lose anything there.

**Marcel Santilli:** And I will send that in an email on to you.

**Marcel Santilli:** And just any, you know, I could just take a little, like, two minutes here.

**Marcel Santilli:** I just, I really want some feedback from you guys.

**Marcel Santilli:** Like, what happened today?

**Marcel Santilli:** What did you get that you didn't have, you know, going in before we started?

**Marcel Santilli:** So if we reverse three hours, where are you now versus three hours ago?

**Marcel Santilli:** And how is this different than if you maybe had done the session yourselves?

**Marcel Santilli:** I think it's better clarity, not even better, clarity on what we're solving and understanding that there's a bunch.

**Marcel Santilli:** Take care.

**Marcel Santilli:** of other things we thought we were solving that we were not, and really kind of nailing within the big picture, why are we solving this and how we're solving it and what really matters without ever getting into the layouts, which for me, that was different.

**Marcel Santilli:** I'm like, man, I need to prototype this really quickly.

**Marcel Santilli:** Yeah, to me, that's the main, I'll get the guy that's working on it to watch the session, because I think we jump too fast into the code, even not just your wireframe, so like, and then we go in different routes.

**Marcel Santilli:** Yeah, we're jumping too fast into that, and we need to do a better job of like doing this session within ourselves as well.

**Ryan Singer:** So it's like, for me, if we could do like two or three, based on your availability, Ryan, and different tackles, you know, I feel like I would be better equipped to try to do a better job of like reframing, shaping, and not jumping into solutions so fast, you know.

**Ryan Singer:** I feel like this helps, but I don't think that I could replicate the session.

**Ryan Singer:** Marcel, to me, is just at even a higher level than the other guys.

**Ryan Singer:** The programmers and designers who have jumped straight into Figma or straight into Code.

**Ryan Singer:** We're no planning.

**Ryan Singer:** So we get stuck in rabbit holes all the time.

**Ryan Singer:** this is super helpful.

**Ryan Singer:** And just on this project as well, I haven't been working on this project, so it helped me clarify a lot of things around how to do even the training part.

**Ryan Singer:** I wasn't thinking about a simulated person, but that is actually how we do with a lot of the clients.

**Marcel Santilli:** there is a workflow creation there for simulator based on feedback that even at the technical level is there.

**Ryan Singer:** A way that you could start to think about this is the role that I'm playing here is what a good product person should do for you in the team.

**Ryan Singer:** And there's three levels.

**Ryan Singer:** There's a high level, which is like strategic intent.

**Ryan Singer:** Like we need to be...

**Ryan Singer:** Like editors aren't scaling and like we're saying no and blah, blah, blah, right?

**Ryan Singer:** Then there's like actual build.

**Marcel Santilli:** This is what the layout's going to be.

**Marcel Santilli:** This is what the code's going to be.

**Marcel Santilli:** We need a linking layer in between where we have, because the layer we're at today, this is the actual product layer.

**Marcel Santilli:** This is the layer in between where you make trade-offs about what's in the scope, what's out of the scope, what's actually the concept.

**Marcel Santilli:** Is this hitting it or not?

**Ryan Singer:** Like, you know, what's important here?

**Ryan Singer:** So this is, you can start to think of this as that, it's the product layer.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** When you asked me last week, like, why did you think of me?

**Marcel Santilli:** And I was exactly because of that.

**Marcel Santilli:** Like I was like, I want the whole company to learn to do that part better and myself as well.

**Ryan Singer:** You know, I've in of the team.
