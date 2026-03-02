# Daniel - Sync on Delivery Scaling Plan

<metadata>
date: 2025-10-06
time: 22:01 UTC
duration: 67 minutes
organizer: Marcel Santilli
participants: Daniel Lopes, Jason Gong, Marcel Santilli
fathom_recording_id: 92218649
fathom_url: https://fathom.video/calls/433061562
share_url: https://fathom.video/share/jaP27x2NYFSMtApi_Riyk-xhYmsKULvS
source: fathom
enriched_on: 2026-03-02 14:30 UTC
</metadata>

---

## Summary

Marcel, Daniel, and Jason aligned on a major restructuring of GrowthX's service delivery: splitting into Path A (selective, high-end services) and Path B (scalable, lower-touch offerings combining mini-sprints at $6-12K, an AI-led growth community subscription, and the Check That AI visibility product). The goal is to monetize demand that GrowthX currently turns away while reducing operational strain on the delivery team until agentic workflows deploy. Path A will validate the platform and focus on ideal-fit clients; Path B will serve broader market demand with a simplified offering while supporting Check That as a standalone product competing against Profound.

---

## Context

GrowthX operates two business models: high-ticket services (Path A, currently $200K+/year engagements) and CheckThat, an AI visibility product still in development. The immediate challenge: the delivery team is overextended, burning 70-hour weeks until agentic automation launches, while simultaneously rejecting qualified leads due to ICP constraints. Marcel has been running listening tours with team members and proposed a solution: introduce Path B, a more scalable package that bundles mini-sprints (3-month projects at $6-12K), access to an AI-led growth community (cohorts, office hours, educational content), and CheckThat as a free-to-paid tool ($0 free tier tracking industry prompts, ~$100/month for custom prompt tracking). This allows Tyler (the account executive) to monetize leads GrowthX currently discards, recruits top talent via the community, and funds platform development without hiring a large sales team. The three-person leadership team—Marcel (CEO/Strategy), Daniel (VP Product/Engineering), Jason (VP Operations/Engineering)—needs to finalize the packaging, messaging, and engineering roadmap before the board meeting.

---

## Relevance

**To GrowthX Delivery:**
- Path B mini-sprints ($6-12K, no ongoing services) will alleviate pressure from 70-hour weeks and content staging bottlenecks (Mariana currently spends 2 hours/day staging for Adventurers group)
- Three-stage qualification process will improve lead fit: ICP validation → excitement confirmation → capability check
- Pre-kickoff phase (audit work, research, strategy deep dives) can be done before client engagement, reducing sprint workload
- Targeting 20 mini-sprints/month across a lean team (4 people) is achievable with automated artifact generation and agentic deployment

**To CheckThat Product:**
- Launch with AI visibility as the primary value prop, competing directly against Profound's weak-but-growing offering
- Free tier tracks industry category prompts; $100/month tier for custom prompt tracking
- Expand features over time: content inventory (site auditing), competitive intelligence, social listening, brand monitoring—all features Daniel is already building for Path A clients
- Path B bundling ($6-12K upfront mini-sprint + community subscription) will include access to CheckThat environment pre-built
- Higher-value bundling ($500-2000/month) possible once product features mature

**To GrowthX Business Development:**
- Tyler can monetize 50+ leads currently being rejected, generating $3M ARR potential at 20 mini-sprints/month
- AI-led growth community serves dual purpose: brand building (like Aerofs' community) and recruitment funnel for delivery talent
- Keeps sales lean: GrowthX is 3% sales vs. competitors at 30-40% (Aerofs ~20 AEs, Profound ~40 salespeople)
- Opportunity to convert CheckThat accounts to Path A services by cherry-picking best-fit accounts for high-end delivery
- Path A remains selective: focus on ideal clients, use services to validate platform, reduce churn risk from forced fits

---

## Overview

- Introduce "Path B": a more scalable, lower-touch offering combining mini-sprints, AI-led growth community, and Check That tool
- Maintain "Path A" as selective, high-end services to validate the platform
- Launch Check That as AI visibility tool, expand features over time
- Bundle offerings strategically to create compelling, high-value packages

---

## Key Topics

### Path B: Scalable Offering

  - Introduce mini-sprints ($6-12K) bundled with AI-led growth community subscription
  - Launch Check That as AI visibility tool, expand features over time (e.g., content inventory, competitive intelligence)
  - Target 20 mini-sprints per month, potential $3M ARR
  - Leverage existing demand, monetize leads currently being turned away
  - Reduce pressure on high-touch services, allowing focus on ideal clients

### Path A: High-End Services

  - Continue selective approach, using services to validate platform
  - Address current challenges:
      - Long hours (70hr weeks) until Agentic deployment
      - Content staging inefficiencies (2hrs/day for Adventurers group)
  - Overall client satisfaction remains high despite challenges

### Check That Product Strategy

  - Launch focusing on AI visibility, competing directly with Profound
  - Offer significant free value, charge \~$100/mo for custom prompt tracking
  - Expand features over time (e.g., site auditing, competitor monitoring, social listening)
  - Potential to bundle with other offerings for higher-value packages ($500-2000/mo)

### AI-Led Growth Community

  - Keep separate from product offerings for brand association and growth potential
  - Use as training ground to recruit top talent for delivery
  - Offer cohorts, office hours, and educational content

### Sales and Monetization

  - Allow Tyler (AE) to monetize and nurture leads through Path B offerings
  - Maintain lean sales team (currently \~3% of headcount vs. competitors' 30-40%)

### Engineering Priorities

  - Complete Check That project
  - Finish content inventory with Brad
  - Replace Looker, add PostHog for analytics
  - Develop client visibility features (assignments, opportunities, reporting)
  - Create framework for external workflow creation and deployment

---

## Action Items

- Finalize packaging and launch plan for AI-led growth community + mini-sprints
- Develop 3-month roadmap for Check That launch and feature expansion
- Align on product strategy: decide on level of integration vs. separation for offerings
- Continue Path A optimization and selective client approach
- Recruit 2-3 directors to backfill key roles (Kyle, Panzer, Jason)
- Present aligned strategy at upcoming board meeting

---

## Transcript
**Daniel Lopes:** Thank you.

**Daniel Lopes:** I'm still reading the doc that Marcel sent.

**Jason Gong:** Marcel is still in a call.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** Yo.

**Marcel Santilli:** Sorry guys.

**Daniel Lopes:** How's it going?

**Daniel Lopes:** Good.

**Jason Gong:** Should I just come to your room, Marcel, or that'd be easier?

**Marcel Santilli:** Probably easier.

**Marcel Santilli:** I'll resume.

**Marcel Santilli:** know it's kind of weird because we're on the same building, but update.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Daniel, did you have a chance, Jason, to just do a quick, I know it's a lot, but do a quick read on the stuff a little bit on the doc, if not, it could take a couple minutes.

**Jason Gong:** I read it.

**Daniel Lopes:** I read most of it.

**Daniel Lopes:** I didn't read the jobs to be done.

**Marcel Santilli:** Yeah, don't worry about the jobs to be done.

**Daniel Lopes:** And the teams part.

**Marcel Santilli:** The TLTR here that I wanted to align is, so, I don't think this is kind of crazy new, right?

**Marcel Santilli:** But it's kind of going off of, like, I can't remember where you wrote this, Daniel, but it's kind of like, how do we put more on the client?

**Marcel Santilli:** This is kind of an evolution of that, which is, I think the...

**Marcel Santilli:** The biggest thing that I'm kind of trying to suggest here is today we go new prospect, qualification, we're trying to have this crazy bar on ICP, which is fine, which is the right thing to do, but also we're learning so much, right?

**Marcel Santilli:** Okay, and it's kind of like us telling people to F off is also like, you know, potentially an opportunity to not now, but later.

**Marcel Santilli:** But today, we can't just be like, hey, here's Atlas, good luck.

**Marcel Santilli:** That's like too much of a leap to go from where we are to here's Atlas, good luck, right?

**Marcel Santilli:** And also, we need safer ways for people to have shots on goal.

**Marcel Santilli:** And today, like we give people when we're hiring like an assignment, but at that assignment, although a little bit more predictive than no assignment is also not giving them enough like practice essentially and enough reps, right?

**Marcel Santilli:** So then they come in and they go and choose strategy sprint.

**Marcel Santilli:** So then what I'm trying to do is raise the bar on

**Marcel Santilli:** What fit looks like for full service.

**Marcel Santilli:** And then also split some of the legwork into pre-kickoff.

**Marcel Santilli:** And pre-kickoff be mostly things that short of a quick 30-minute alignment meeting, we can do without much input from the client, which is mostly grunt work that we're saving from the strategy sprint.

**Daniel Lopes:** Could then have like a client take in form or something.

**Marcel Santilli:** Yeah, it's mostly this stuff that says pre-kickoff right here.

**Marcel Santilli:** And it's kind of like on a rolling basis.

**Marcel Santilli:** So in other words, like there might be things that you can't do, for instance, get access to systems before the kickoff.

**Marcel Santilli:** But a lot of these things like you can at least schedule and do, right?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Do SEO audit, content audit, an AI visibility audit, company research, brand perception, like whatever these are, right?

**Marcel Santilli:** They're all things you can do and they're really valuable.

**Marcel Santilli:** And then you would do, like, the strategy deep dive.

**Marcel Santilli:** And then from there, you can do the actual content strategy, right?

**Marcel Santilli:** And so the goal is to have a meeting team here doing the pre-kickoff.

**Marcel Santilli:** And so, like, take Redis.

**Marcel Santilli:** We told Redis, hey, sorry, they just signed today.

**Marcel Santilli:** Like, we can't kick off for another five to six weeks.

**Marcel Santilli:** Sorry about that.

**Marcel Santilli:** They're kind of annoyed.

**Marcel Santilli:** But don't worry.

**Marcel Santilli:** We'll have a pre-kickoff meeting, and there's a lot of things we do prior to the kickoff.

**Marcel Santilli:** And now, all of a sudden, they're okay with six weeks out, you know?

**Marcel Santilli:** And then that lessens the load, so then the strategy sprint can be handled by higher value people like Ada's of the world because Ada's not having to delegate the most important part.

**Marcel Santilli:** Because right now, what Ada's having to do is, like, she's delegating the artifact generation and the kickoff call.

**Marcel Santilli:** Both are, like, super critical.

**Marcel Santilli:** Not clicking the first version, but taking the first version and shaping it into, like, client-ready.

**Marcel Santilli:** And then being on that first call and taking everything that the research told us and actually asking the right questions.

**Marcel Santilli:** Double-clicking on the right places is like one of the most critical things in shaping.

**Marcel Santilli:** just don't know how anyone could possibly do a good job for a client and not internalizing that information, right?

**Jason Gong:** Yeah.

**Jason Gong:** Clients don't pay for any of the pre-kickoff stuff, right?

**Marcel Santilli:** They don't pay, but it's not additional work.

**Marcel Santilli:** It's just shifting when we do the work.

**Marcel Santilli:** So instead of doing 20 hours of work week one and another 20 hours of work week two, that's 40 hours of work.

**Marcel Santilli:** And then in that work, because Ada doesn't have 200 hours a week, she has to delegate a lot of that, right?

**Marcel Santilli:** And because she's having to delegate a lot of that, it's being delegated to like the CM layer.

**Marcel Santilli:** And because they only have one shot to get it right, if they don't get right, then Ada's just like killing herself or delivering, you know, subpar work.

**Marcel Santilli:** So then if you take those 40 hours of work, let's call it, and you spread it out across six weeks, or you take 30 of those 40 hours and you spread it out four weeks prior to the kickoff, anything goes wrong here, there's still multiple layers of potential review and catching mistakes and things like that, because it's not.

**Marcel Santilli:** Like this crazy pressure, but then this little pod over here gets really good at that because, you know, if they have capacity, they can work on people that are in pipeline.

**Marcel Santilli:** And by the way, this is great work to do anyways, in order to qualify sales anyways, you know, like, so it's not like wasted work, you know, but then the whole idea is you take, we take that work.

**Marcel Santilli:** And then we package that work after we've done a couple of these pre-kickoffs into a downsell, which is essentially like off of like what Carol, right?

**Marcel Santilli:** Like the other day, was like, right, like, I think I told you right, Daniel, she's like, hey, I'm kicking off with this customer.

**Marcel Santilli:** Any chance you can do some of your research work on this?

**Marcel Santilli:** And I deliver this very basic artifacts and she's like, holy , this is amazing.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** This is amazing.

**Marcel Santilli:** You're amazing.

**Marcel Santilli:** And they're like, this is nothing.

**Marcel Santilli:** Like this took like less than an hour.

**Marcel Santilli:** Right.

**Marcel Santilli:** And so the idea is like, we package that and bundle it so that it's, it's like the pre-kickoff mostly with the.

**Marcel Santilli:** Like content strategy, and it can be handled by people that are training and ramping up.

**Marcel Santilli:** They're not ready to do strategy sprints, and you sell that as a subscription, a bundle subscription with two AI-led growth and or check that, essentially, you know, for 6K.

**Marcel Santilli:** Yeah.

**Jason Gong:** And so then, yeah.

**Jason Gong:** You're saying during pre-kickoff, we could decide to downs up, to downs up?

**Jason Gong:** No, it's, so, there's this whole, there's the whole whole stages of qualification, right?

**Jason Gong:** It's written here.

**Marcel Santilli:** If they don't qualify, they go into this other path.

**Marcel Santilli:** And this path is essentially Tyler selling, instead of saying, instead of Tyler saying, sorry, you're not good enough to work with us.

**Marcel Santilli:** It's like, by the way, you're not ready for this full service, but we have this other thing here that is the strategy sprint, right?

**Marcel Santilli:** It's a light strategy sprint, essentially.

**Marcel Santilli:** And it's sold that way.

**Marcel Santilli:** It's a super low risk because it's like, we don't care if they turn.

**Marcel Santilli:** It's like 6K.

**Marcel Santilli:** It's literally a rounding error, even for a C-stage company to give us 6K.

**Marcel Santilli:** So we're essentially like getting to do the same work that we're doing in the pre-kickoff here, except we're bundled it along with access to AI-led growth.

**Marcel Santilli:** And so same way, you know, with AI-led growth, we would go and like, sorry, one second, like the same way you go here and say, become a member.

**Marcel Santilli:** It would be something kind of like this, except it would say $6,000 instead, and it would have like, you know, a mini kickoff, and then it would have mostly just like what we deliver today in an ocean space, right?

**Marcel Santilli:** And that's kind of it.

**Marcel Santilli:** So that's kind of the idea.

**Marcel Santilli:** And then once checked that as launch, which is very, very soon, and it might even be before we even start doing that, it can be bundled to where, you know, like, for instance, I just signed up for Ahrefs versions.

**Marcel Santilli:** signed Ahrefs version of, like, AI visibility.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** It is like $600 for garbage.

**Marcel Santilli:** It is so bad.

**Marcel Santilli:** It's like actually like laughable how bad it is.

**Marcel Santilli:** Like you go in here and you type in your brand like ramp and you try to find your competitors like Brax, you know, or, you know, or I don't know, like Navon and you explore and it's so bad.

**Marcel Santilli:** It actually thinks it's about wheelchairs because it's like thinks it's a wheelchair ramp.

**Marcel Santilli:** Like it's that bad.

**Marcel Santilli:** And this is $700 a month right here.

**Marcel Santilli:** Like it's insane, like absolutely insane how bad it is.

**Marcel Santilli:** And then, and so like we have so much value in the highlighted growth community alone that people are paying for it already, right?

**Jason Gong:** And we're going to be even more value once we start adding even more cohorts and training, right?

**Jason Gong:** I guess mentally it's like it's the self-serve version.

**Jason Gong:** And like we'll release little tools, maybe, you know, to write an assignment brief or even to write content.

**Marcel Santilli:** able able You're you.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And so over time, the goal would be check that would have more tools, right?

**Marcel Santilli:** And so this is just a five-coded version, right?

**Daniel Lopes:** We could even have a lot of the, I don't know if it makes sense, but a lot of the stuff people would be preparing during that pre-kickoff, instead of doing a notion, we would put that in a login experience.

**Jason Gong:** I guess for me, I would just think about how to package that entire product as like, here's the growthx light, where you have to do a bunch more work for yourself, but like, we're still setting you up for success.

**Marcel Santilli:** Yeah, exactly.

**Marcel Santilli:** And so like, the whole idea here is like, I don't have the context here, right?

**Marcel Santilli:** Like, but, but like, most of the work is kind of like, so natural for it to be in something like this.

**Daniel Lopes:** Because like, yeah, need all your competitors and everything.

**Marcel Santilli:** You need personas and all the opportunities, you know, or whatever you,

**Marcel Santilli:** You know, it's just like, it's all kind of there eventually, but the MVP here is literally like, what you're delivering is some version of like, what we've done for Engine, right, which is mostly like, you're delivering this, pretty much.

**Marcel Santilli:** Yeah, right.

**Marcel Santilli:** right here.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** What we're delivering.

**Jason Gong:** Yeah.

**Daniel Lopes:** course, it's going to tell you how to use this stuff, too, right?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And like, I have a little bit of a tough time visualizing some of this stuff inside of check that because it will conflate with the visibility parts.

**Daniel Lopes:** We really have to think about the UI properly, but we can put together like super fast, like a mini product that has just this, you know, and then you can consume that as a URL inside of check that or ask for like, what's your log or if you're logged in already on both, you get the data from there, you know, because we already have shared logins.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So micro app, like one cycle, we use a micro app that looks great and has like your personas, your artifacts, your research, all the outcome that you share.

**Jason Gong:** I think we share.

**Jason Gong:** I don't know, again, like that whole thing is a product, like check that, the community, it's like you're, like somebody needs to like manage that on the Sizzler thing, right?

**Marcel Santilli:** Yeah, exactly.

**Marcel Santilli:** My whole thing is like right now, the MVP here, or step one, I talked to Andy already, is build a mini team for pre-kickoff and validate that we can deliver, like the way I was thinking about it is, if you can spend, you know, 10 hours of human time to deliver this pre-kickoff, and we'll validate it because then the strategy sprint team will say if it's good or not, essentially, and so it's mostly the risky strategy sprint to go from zero to one.

**Marcel Santilli:** Once we validate that, that this little team here, that's like mostly junior people, mostly people that are not fully ramped can do that, then what you're doing is you're taking like access capacity of this to deliver this, and you're throwing over here and getting paid for that.

**Marcel Santilli:** And so the math roughly works out to like, you know,

**Marcel Santilli:** Four people, I believe, this is what we got to validate, can do at least 20 of these mini sprints a month because it's like so self-serve and there's almost no human interactions, like one meeting only, or two meetings at best, right?

**Marcel Santilli:** So two hours of meetings essentially, right?

**Marcel Santilli:** So 20 a month means 40 hours of meeting.

**Marcel Santilli:** That's like super doable for a team of four, right?

**Marcel Santilli:** And it's going to be so automated.

**Marcel Santilli:** Like even today, the way artifacts are generated with one click, cut down the work by like 70% already, right?

**Marcel Santilli:** And the deep researcher and stuff like that.

**Marcel Santilli:** And with every cycle here, we'll also learn because we'll be doing higher volume with things we need to do here.

**Marcel Santilli:** And everything we do here, we'll be learning what to do there.

**Marcel Santilli:** And then over time, the MVP is you deliver in an ocean, which is today, if we sold that today for the people we're turning down, they're begging us to take them on as bad clients, like they would pay 10k even for that, right?

**Marcel Santilli:** Like, because the delta though, between this and this is that we're not doing content for them.

**Marcel Santilli:** We're not doing...

**Marcel Santilli:** Celebration articles, we're not doing any articles, and we're not hitting publish on anything for them.

**Marcel Santilli:** We're giving them assignments, and we're giving them three months of strategy, and we're giving them the artifacts, that's it.

**Marcel Santilli:** But in exchange for that, we are giving them access to a bunch of cohorts and a masterclass on how to do all this , and later on, an entire check that environment fully set up already.

**Daniel Lopes:** The thing that I'm working on this month, like the inventory, I think we'll find that it will be part, that can be part of the packaged notion that we sent to you, you know?

**Daniel Lopes:** All the pages that are broken, like all the technical SEO problems, gap opportunities, plus LLM citations, automatically, instead of like people trying to learn how to do that in their table, you know?

**Daniel Lopes:** So that will make that process as easy as the generation of artifacts, I think.

**Jason Gong:** Did you find a spot for artifacts in there?

**Jason Gong:** Did I get interested?

**Jason Gong:** Or that's a part of

**Jason Gong:** Is Artifacts, which is a part of what we're delivering here, part of the content inventory, or is that a part of Atlas?

**Daniel Lopes:** Can we deliver articles to them there, too?

**Daniel Lopes:** I think they could have, like the team building this, maybe they just use Atlas, and they create the workspace, and then we have an export button that they can load in the separate app for now.

**Daniel Lopes:** You know, there'd just be like a simple admin that you load to the templates for the clients.

**Daniel Lopes:** And maybe it's just CSV for your strategy, for example, and then they report in AirTable or something like that, and they can show how to do that, have a little room or something.

**Marcel Santilli:** There's just so many little pockets of like things that we can deliver value, like doing a like, there's like so many things to deliver value here.

**Marcel Santilli:** But what I'm, in doing the research and vibe coding for Check That, mostly for fun and for my own learning, like I started signing up for all of them.

**Marcel Santilli:** And they're just all so  bad.

**Marcel Santilli:** Like, all of them, all they do is tell you, like, this visibility score.

**Marcel Santilli:** And, like, when you want to actually take action, it's so hard to come up with actions and, like, insights from it.

**Marcel Santilli:** You know?

**Marcel Santilli:** It's, like, it's just impossible.

**Marcel Santilli:** It's just, like, really, really hard and really bad.

**Marcel Santilli:** And none of them do a good job with context.

**Marcel Santilli:** They're just so bad at context.

**Marcel Santilli:** It's, like, it's laughable how bad they are in context.

**Marcel Santilli:** Like, just...

**Daniel Lopes:** Why did you have every open, you were going to say something and then I cut you off?

**Jason Gong:** I think every is a good packaging of content and tools together a little bit.

**Marcel Santilli:** Okay.

**Jason Gong:** Which one is it?

**Daniel Lopes:** Not every?

**Marcel Santilli:** Every.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah, like, every does, like, bundle.

**Marcel Santilli:** this is, like...

**Marcel Santilli:** one, does this make sense?

**Marcel Santilli:** Are we aligned?

**Marcel Santilli:** can action, but this is super high level.

**Marcel Santilli:** This is mostly, like, it's, like, if we can reduce the burden on the high end...

**Marcel Santilli:** And this is what I...

**Marcel Santilli:** Like, it's like, hey, Path A, it's like, why are we doing this?

**Marcel Santilli:** Like, why does this path even exist to begin with?

**Marcel Santilli:** And then what does this path do over here, right?

**Marcel Santilli:** And then it's like, there's essentially we're creating two paths.

**Marcel Santilli:** And then we can shape one path and we can shape another path.

**Marcel Santilli:** But today, just putting a bottleneck on one path is, I think, not enough.

**Jason Gong:** Yeah, it makes sense.

**Marcel Santilli:** Like, Profound is such a horrible proposition that it's like, we need to give somebody an alternative to Profound.

**Marcel Santilli:** Because Profound is like growing like wildfire with a bad proposition because there's literally no alternative in place at all, you know?

**Marcel Santilli:** And, like, when SEMrush and AHRFs and PKI and Profound all are that bad, I'm just like, this is insane.

**Marcel Santilli:** This is crazy that no one is doing this, like, you know?

**Daniel Lopes:** The right perspective.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** yeah.

**Daniel Lopes:** And I think, like, the Path A, the reason why I have a lot of, like, ideas for how to package things is because...

**Daniel Lopes:** We're doing Path A, you know, so we can, like, the idea of, like, oh, we're to organize these things, we're going to do, like, strategy like this, and, like, and we're doing Path A and trying to build a platform for that.

**Daniel Lopes:** That's how we find the path to shorten the time to build these things.

**Daniel Lopes:** Like, I wouldn't be able to do, like, a content inventory that does, like, 70% of the work after, without realizing that trying to replicate Marcel's our table 50 times is just, like, every, not even the smartest person messes that up.

**Daniel Lopes:** So, yeah, I think it's also, like, not just funding, it's the part that enables Path B, you know.

**Marcel Santilli:** But then it allows us to take, like, people that are paying a $6 to $8K a month, and, like, I was talking, I'm doing the ME listening tours, I did four today, and it was, like, it's insane.

**Marcel Santilli:** Like, the  that we're doing for some of these people, like, web stacks, we're doing CRO analysis, we're doing SEO audit, we're doing LLM tracking, we're doing long-form content, we're doing design briefs times eight a week.

**Marcel Santilli:** We're publishing eight pieces of content.

**Marcel Santilli:** And they don't want to pay us a single dollar more or sign a long-term contract.

**Daniel Lopes:** It's like, this is  insane.

**Daniel Lopes:** Like, this is crazy.

**Marcel Santilli:** This is insane.

**Marcel Santilli:** Like, this is absolute insanity.

**Marcel Santilli:** Like, you cannot get that value anywhere else.

**Marcel Santilli:** And if they don't see that, then we can just give them this other path to be very easy to, like, churn into this other path, you know?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And so then it's like, then if we're roughly aligned with this, the details obviously matter here, then the idea would be, like, to figure out what is the best way to package this thing, you know, and staff it in some ways, right?

**Marcel Santilli:** And then I can focus on Path A, which is what I've been doing, right?

**Marcel Santilli:** Which is, like, continue to, like, work on the ICP, the, I don't know what the emoji is.

**Marcel Santilli:** Path A.

**Daniel Lopes:** Nah.

**Marcel Santilli:** Path A sucks.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** services.

**Marcel Santilli:** services, like.

**Marcel Santilli:** And then Path A.

**Marcel Santilli:** B, like, I think we can think of it as, like, a little bit differently instead of thinking of it as, like, AI-led growth community or check that versus something else.

**Marcel Santilli:** Like, it can just be, like, a bundle, however we want to build this bundle and however we want to monetize this bundle, that's up to Jason, right?

**Marcel Santilli:** Like, and Jason, this path.

**Marcel Santilli:** And, like, I feel just so confident that even with the leads that were disqualifying, all of them would pay $6,000 to $12,000 up front for this.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And without Jeff.

**Daniel Lopes:** I think we can build, like, we can build a legit engineering team under Jason to serve him there.

**Daniel Lopes:** So, like, we'll keep Steven, we'll have Jose, and maybe we'll get, like, one or two more and then do everything, you know?

**Jason Gong:** That makes sense.

**Jason Gong:** I mean, I think this, like, solves a lot of problems.

**Jason Gong:** It brings, like, cohesion to, like, all these separate little projects we've been kind of scoping recently.

**Jason Gong:** And the North Star is a little bit more clear.

**Jason Gong:** It's, like, I mean, again, to me, this is, like, this is the self-serving.

**Jason Gong:** Like, you know, growthx.ai, that you need to get results.

**Marcel Santilli:** Yeah, like, just to put it into perspective, if you do, like, 20 a month of 12,000, there's, like, 3 million in ARR.

**Marcel Santilli:** And that's, like, and then as check that has even more paths where it doesn't require the mini sprints, like, that is even higher, you know.

**Marcel Santilli:** But then this allows us to monetize and get, like, 12-month contracts for the platform.

**Marcel Santilli:** And so essentially what we're doing is, do you remember, Daniel, like, Sean from exec.com was telling us that people do?

**Marcel Santilli:** They're like, hey, people will pay 12K for this mini sprint.

**Marcel Santilli:** You sell the mini sprint, but you discount the mini sprint to zero, and you sell them the subscription to the platform, essentially, you know.

**Marcel Santilli:** And then you use that as an excuse to onboard them into your platform, you know, or to this other thing that then is the thing that people care about long term.

**Marcel Santilli:** But I think this can also be a money printing machine and highly profitable piece as well.

**Marcel Santilli:** That can fund us quite a bit, you know.

**Daniel Lopes:** I think so, yeah, that makes sense.

**Marcel Santilli:** And so then that begs one question, though, that, like, and I don't think it's too late for us to decide, but I do think it would be good with this in mind if we're aligned to just think about, like, in a world of, like, check that versus, like, AI-led growth, like, are we screwing ourselves by having two separate things?

**Marcel Santilli:** Is there a lot of benefits to having?

**Marcel Santilli:** I go back and forth, and I can make an argument either way, you know, and then is some of this content tooling and things, should long-term live on AI-led growth, or should AI-led growth be community-only and completely separate, and then we find ways to kind of integrate it, you know, or should, like, that be one umbrella?

**Marcel Santilli:** Like, I don't know, but I just want to make sure before we launch this thing that...

**Marcel Santilli:** Yeah.

**Marcel Santilli:** We really think hard about it, you know, I don't think there's a, like, we'll make it work either way, but I do think it's good for us to think like a year ahead a little bit on like, hey, if we go this path, we'll check that and AI like growth, what are the pros and cons?

**Marcel Santilli:** If we went with one only umbrella, you know, what are the pros and cons of doing that, you know, because it's easy to create community features into an app, it's a lot harder to sell people into a community and then tell them, by the way, go over there to sign in to this other thing over there, you know, so I don't know if that makes sense, right?

**Marcel Santilli:** Like, if someone signs up for, like, this, and they log in here, it's a lot harder to explain to them that they can go somewhere else, you know, for other tooling or whatever, you know, essentially.

**Marcel Santilli:** Like, if they're in this environment, it's a lot harder to explain to them that there's this other tool over there.

**Jason Gong:** I feel like the way we're thinking about the community is like, okay, so I think we should think it through.

**Jason Gong:** I don't think it's that big of a deal.

**Jason Gong:** We separate the content and the community from the tooling because they already feel quite separate.

**Jason Gong:** Like I know some products do like, oh, here's Surfer SEO Academy, but that almost like undersells like what we're trying to build the community into.

**Jason Gong:** I think the thing we want to avoid is like having too many products that are separate.

**Jason Gong:** Like if Atlas output, you know, check that content inventory, like those are like four different products.

**Jason Gong:** I think that might be a bad experience.

**Jason Gong:** So that might be worth thinking through if we want all those things to be part of this package.

**Marcel Santilli:** But like, if we're going towards like the Surfer SEO, which I think to me is like the best of the models of all of them is like Surfer SEO.

**Daniel Lopes:** just too much.

**Daniel Lopes:** I just logged in a few times.

**Marcel Santilli:** Say that again.

**Daniel Lopes:** I haven't used much.

**Daniel Lopes:** just logged in a few times.

**Marcel Santilli:** It's decent quality, right?

**Marcel Santilli:** And here, had just signed up, so give me a second.

**Daniel Lopes:** Don't they just have the content creation part, or do they have, like, community stuff to you and all this stuff?

**Marcel Santilli:** Yeah, if I could figure out how to sign out.

**Marcel Santilli:** I can log in to the right one, but apparently, you can't sign out of it.

**Marcel Santilli:** So much for a good experience.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Your user?

**Daniel Lopes:** If click on your user avatar.

**Marcel Santilli:** Where is the user avatar?

**Marcel Santilli:** M, the bottom, the last thing.

**Marcel Santilli:** Oh, there's this thing on top here.

**Marcel Santilli:** What the ?

**Marcel Santilli:** I'm not sorry.

**Marcel Santilli:** There's, like, an icon to draw on top of it.

**Marcel Santilli:** That's what I could see.

**Marcel Santilli:** I just upgraded a team map to play with it.

**Marcel Santilli:** By the way, this thing is like, again, the same thing is like insanely expensive.

**Marcel Santilli:** And look at this AI tracker.

**Marcel Santilli:** It's like you get like 25 props to track for like 200 bucks.

**Marcel Santilli:** And like, this is all you get.

**Marcel Santilli:** This is it.

**Marcel Santilli:** Done.

**Marcel Santilli:** That's it.

**Marcel Santilli:** It's all you get for 200 bucks a month.

**Marcel Santilli:** You get this.

**Daniel Lopes:** Very excited to launch the other one.

**Daniel Lopes:** It's ridiculous.

**Marcel Santilli:** Like the bar is so low and it's so bad that it's just like kind of silly how bad it is.

**Marcel Santilli:** Like this is, it's just so bad.

**Marcel Santilli:** It's just so basic and so shallow.

**Marcel Santilli:** And none of them try to even remotely do good contacts on anybody.

**Daniel Lopes:** Yeah, everybody's rushing.

**Daniel Lopes:** And like we have a bit of an advantage because you guys have a ton of experience in this.

**Marcel Santilli:** But then what they do here, you see like they have tools.

**Marcel Santilli:** And so like topic researcher, keyword researcher, rank tracker, AI humanizer, right?

**Marcel Santilli:** So.

**Marcel Santilli:** So, like, what I was thinking was, like, you can add, like, you know, tools under here, too.

**Marcel Santilli:** And in that case, you know, like, this would be long-term a bit more.

**Marcel Santilli:** Like, for instance, like, the fact-tracker even, right?

**Daniel Lopes:** You don't think that we're going to end up with, like, a Stemrush-like experience that's...

**Daniel Lopes:** I mean, we can make it look good.

**Daniel Lopes:** We can make it be...

**Marcel Santilli:** Yes and no, like...

**Daniel Lopes:** Because Salesforce does that.

**Marcel Santilli:** Like, it works.

**Marcel Santilli:** I think the only way to make it work is, like, you're giving a taste of the Atlas platform without connecting all the dots.

**Marcel Santilli:** So you're trying to create some friction in place on purpose.

**Marcel Santilli:** Otherwise, like, they should just buy Atlas, right?

**Daniel Lopes:** Access to Atlas.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** No, no, like, I mean more, like, if we have checked that and, like, we launched this in, like, end of this month or, like, first week of November.

**Daniel Lopes:** And it goes live and everybody has the perception of this is an AI visibility tool.

**Daniel Lopes:** And it's the best one and has this public area, which is also a big part of it.

**Daniel Lopes:** And if we start bolting on top of this, like a fact checker and like a content creation tool and like an SEO, like an analytics for Google Search Console, like what is the kind of the boundaries there?

**Daniel Lopes:** Is this always going to be related to AI visibility or do we just any kind of content creation?

**Jason Gong:** Like if we have an AI editor, for example, next editor, where does that go?

**Jason Gong:** I think we should think about the goals.

**Jason Gong:** I think like branding check is just AI visibility benefits us in the short term because it's clean, right?

**Jason Gong:** It's like small, it's medial, you're saying, but if we're trying to go to a world, like our goal is to make something that merges all these together eventually, then I think it would benefit us more into like creating that association now.

**Jason Gong:** And like, I don't know what you would call that.

**Jason Gong:** You would call it like, like, I don't know what that umbrella is.

**Jason Gong:** We want that to be outputs.

**Jason Gong:** It would be like AI awareness by output or something like that.

**Jason Gong:** It would be more clear to subfeature, you know, than there's a standalone product.

**Daniel Lopes:** Yeah, like the way I was thinking about it.

**Daniel Lopes:** My own?

**Marcel Santilli:** Go ahead, Marcel, I'm sorry.

**Marcel Santilli:** No, I was just saying like the way I was thinking about it, I actually think that Aerofs simplified it in a way, as shallow as their version is.

**Marcel Santilli:** They did simplify it in an easy way, which is just like opportunities and tracking visibility.

**Marcel Santilli:** It should plus auditing your site equals identifying opportunities for you to act on and then creating very shallow tools or very simple tools to act on those opportunities.

**Marcel Santilli:** But then what this doesn't do and it shouldn't do is then connect all those dots so that you have like ability to create like more complex workflows.

**Marcel Santilli:** It's like, it's truly like, hey, for instance, like back last year, I created these like little Aerofs mini apps.

**Marcel Santilli:** to used to to to Right.

**Marcel Santilli:** That was just like, put any URL here, and it will audit that content for you and tell you how to improve that piece of content.

**Marcel Santilli:** And it went super viral on LinkedIn, and I had like 2,000 people using it, right?

**Marcel Santilli:** Like little things like that, I do think there's value because it gives them the taste for the bigger thing that they should be doing more programmatically, you know?

**Marcel Santilli:** But then the hope would be like there's a good CTA to drive them.

**Marcel Santilli:** But the truth is like when they launched ChatDBT, they thought it was just going to be a test too, and then it became much bigger.

**Marcel Santilli:** So we also don't know yet, right?

**Daniel Lopes:** Like, but I don't know.

**Daniel Lopes:** Yeah, like a couple of things.

**Daniel Lopes:** Like one, like I think there is a legit risk of like on like trying to not be AI visibility now.

**Daniel Lopes:** But we can just park that.

**Daniel Lopes:** The second thing is some of the stuff that they're doing is like it's crazy intensive on cost and things like that.

**Daniel Lopes:** So like scraping your entire website and hitting it 8HRF.

**Daniel Lopes:** SendRush to know your keywords or technical audits and, like, extracting your markdown and, like, analyzing.

**Daniel Lopes:** Like, that is not a small feature.

**Daniel Lopes:** Or even, like, can a few websites that has, like, 600 pages, you know?

**Daniel Lopes:** So if you have Webflow and you can plug in something gnarly here, it's going to be, like, that should be expensive, you know?

**Marcel Santilli:** But that's okay.

**Marcel Santilli:** Like, so, like, let me give you an example, right?

**Marcel Santilli:** Like, you know how we used to do the assignments and it was, like, hitting a bunch of things and do a bunch of stuff?

**Marcel Santilli:** Like, a version I would expose here would be, like, a mini model version of that.

**Marcel Santilli:** Yeah, yeah.

**Daniel Lopes:** Lighter?

**Daniel Lopes:** Yeah, no, no, no.

**Daniel Lopes:** I get that.

**Daniel Lopes:** I'm just saying that, like, some of the stuff that we're doing to power the Path A, it's, there is, like, a path to simplification, to have a freemium version or, like, almost, of course, self-serving version.

**Daniel Lopes:** But the delta is a little bit...

**Daniel Lopes:** Okay.

**Daniel Lopes:** I'm

**Daniel Lopes:** Some of the stuff that we'll actually make, like, make your entire content strategy automated, like, that will cost us probably, like, at least $500, like, on, like, processing power, you know?

**Marcel Santilli:** So, yeah, we can move that to the self-service, but we're probably going to have to charge $1,000 a month, you know, like, something like that.

**Marcel Santilli:** But also, like, just to give an example, right, like, Aerofs posted this library that's, like, everyone that's done their certification, and in order to pass their certification, they have to record this, like, 15-minute loom.

**Marcel Santilli:** with their object to graduate, so people are all showcasing their workflows that they built, so a lot of it, and it's just, like, this one person was showcasing this 200-step workflow to generate a piece of content that goes from keyword all the way to publish content, and I'm just, like, .

**Marcel Santilli:** Like, that's insane, like, you know, that people are spending, you know, I don't know, like, a thousand hours doing all of that, and, like, next week that's going to be outdated, essentially, right?

**Marcel Santilli:** Like, or, and so, essentially, in Atlas, we're starting with...

**Marcel Santilli:** Client intake.

**Marcel Santilli:** And we're figuring out all the jobs to be done and all the messy stuff to set the right strategy from the beginning and then executing that strategy.

**Marcel Santilli:** With Check Dad, I feel like we're starting with AI visibility and the questions people are asking that make their brand show up.

**Marcel Santilli:** And then we can incrementally hit up like all the different little jobs to be done in a much more like lighter way.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Just a little incremental value.

**Daniel Lopes:** Yeah, we can figure it out for sure.

**Daniel Lopes:** Like, what do you guys think about that thing that I was saying?

**Daniel Lopes:** Like, because there is a very easy path to say, look at all these companies here that charge you 500 bucks and you get  nothing, essentially.

**Daniel Lopes:** Here's ours.

**Daniel Lopes:** The free side, you almost, you get more than that already.

**Daniel Lopes:** And here's the other thing.

**Daniel Lopes:** But if you say like, hey, you do a lot of all the same things that are not ready, plus we have a community and you have, like, well, I think we can start with the profound direct hit.

**Daniel Lopes:** And then add the other stuff as soon as possible.

**Daniel Lopes:** Maybe bundle the AI-led community or something already, but I think they should use the momentum of AI visibility.

**Marcel Santilli:** No?

**Daniel Lopes:** What do you think, Jason?

**Daniel Lopes:** Because Jason had the point of bundling now, and I just don't see how would we do that, you know, without the risk of money.

**Jason Gong:** I think, so, like, just, like, my thoughts are, we should keep the community separate.

**Jason Gong:** I know Aerofs is doing this, like, bundled thing for almost enablement and branding, but I so much of what we want to do in the community involves, like, bringing other people in, founding members, like, that flywheel is already there.

**Jason Gong:** Like, I don't know if Webflow comes on our podcast, if it's bundled in with a product that's, like, an Aerofs tool, you know?

**Jason Gong:** Or maybe they would.

**Jason Gong:** Some people won't.

**Jason Gong:** And I think for us to own, like, AI growth, like, I think our best shot is to have it associated like that.

**Jason Gong:** My only thought is on the product side, like, do we...

**Jason Gong:** We want to avoid having something that ends up looking like LemList, or you have like LemWarm, LemList, know, like Lemwhatever.

**Jason Gong:** Like, we just want to make one thing now, even if you don't, even if you do carve a piece of it to like brand it separately, like at least it's associated with everything.

**Marcel Santilli:** Yeah, like, and don't forget, right, like, like, agree with all of that, like that the goal here, by the way, it's not to try to change the packaging for launch for Check That.

**Marcel Santilli:** The goal is to, like, create the smaller package that we can deliver as part of AI-led growth, drive subscription to AI-led growth, and then launch Check That, let that grow.

**Marcel Santilli:** And then over time, if we want to bundle a 12-month contract of Check That, once the product has enough features that are monetizable, with this over here, which is the AI-led growth plus mini sprint, then we can do that, and it would be really powerful.

**Marcel Santilli:** But the goal is like, that's why I said there's two bundles.

**Marcel Santilli:** One bundle was 6K for the year, 6 to 10K for the year for a mini sprint, plus subscription to AI-led growth for five people that has cohorts and office hours type of things, right?

**Marcel Santilli:** Great.

**Marcel Santilli:** That I can sell today.

**Marcel Santilli:** It requires zero engineering time and requires nothing.

**Marcel Santilli:** It just requires us moving around a couple people, right?

**Marcel Santilli:** On the other side is like launching check that, and you're giving a ton of value for all those industry prompts and categories because you can track all of those for free.

**Marcel Santilli:** And then we're charging essentially only for them to track those 100 prompts, their custom, and you're charging 100 bucks a month just to cover costs mostly.

**Marcel Santilli:** And then over time, we need to just add additional things that will be the excuse for them to go from paying 100 bucks a month to, you know, 6 to 12K a year, which is still way less than profound, but it will offer so much more essentially.

**Marcel Santilli:** And so the goal is like, take the attention away from number of prompts you're tracking, because that's just.

**Marcel Santilli:** Like so silly and then create value in other ways with check that, but not instead of it.

**Marcel Santilli:** So those are two separate bundles.

**Marcel Santilli:** then later on, when both can stand on their own, then we can bundle them together and say, hey, you get a sprint, you get check that, and you get ALS growth subscription as a bundle.

**Marcel Santilli:** And it's 12K a month, a year, you know, and it's still a no brainer because it's like people are willing to pay that just for the sprint alone, essentially, you know.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And then you can sell 500 of that a year, and in two years, you're 100, you know, 100 million in ARR just from those extensions, essentially, you know.

**Marcel Santilli:** And hopefully one makes the other more sticky.

**Daniel Lopes:** That makes sense to me.

**Jason Gong:** What do you think, Jason?

**Jason Gong:** I think, I mean, like, there's a reason I think there's been a trend away from like freemium products.

**Jason Gong:** It's just like with AI, can't be successful with like a freemium self-serve product.

**Jason Gong:** It's like 20 bucks a month, right?

**Jason Gong:** So you force people to pay you an amount where they're committing and learning.

**Jason Gong:** So my main thought is like, do we want to force people so they can't just buy?

**Jason Gong:** AI-led growth on its own, or check that on its own, and make it a package, or do we let them be standalone?

**Jason Gong:** Because I think if you let them be standalone, then we don't have to create that super strong association.

**Jason Gong:** We could keep them as separate brands.

**Marcel Santilli:** Yeah, we can just do a coupon code for people that are AI-led growth.

**Marcel Santilli:** If they want to sign up for check that, they get a crazy discount.

**Marcel Santilli:** It's just like, we're forgetting how many companies, $500 a month, even $6,000 for the year is literally a rounding error.

**Marcel Santilli:** Like, it's literally, even like a pre-seed company, $6,000 is a rounding error.

**Marcel Santilli:** Like, on the first month of this company's operation, I would have spent $6,000.

**Marcel Santilli:** Like, I spent $15,000 for a website on the second month that this company existed, like last April, right?

**Marcel Santilli:** Like, $6,000 is literally nothing.

**Marcel Santilli:** It's like a rounding error for like 99% of companies we care about.

**Marcel Santilli:** And that's why Profound is growing so fast is because it's such a rounding error that people

**Marcel Santilli:** We're just signing 24K and 36K up front.

**Marcel Santilli:** And there's like, whatever.

**Marcel Santilli:** I don't care if anybody uses it.

**Marcel Santilli:** It's just the insurance policy, right?

**Marcel Santilli:** It's just that our insurance policy is going to be so much better than everybody else's.

**Marcel Santilli:** And the free version is going to be so much more value than everybody else's that it's going to cause everybody to stop paying 24K a year for this thing while we're building more value for something else, you know?

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** I think, like, there's a real value in, like, making very hard for Scrunch or Profound to compete with this, as in, like, make it as cheap as possible, you know?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And our biggest bottleneck right now is that we have the demand, and we have no way to monetize that demand in a way that's more scalable.

**Marcel Santilli:** So then the mini sprint plus AI-led growth community monetizes a slightly more scalable way.

**Marcel Santilli:** Not 10x more scalable, but at least 2x 3x more scalable, and it lessens the load.

**Marcel Santilli:** So it's like, in an ideal scenario, if AI-led growth can drive, like, 5 million in

**Marcel Santilli:** ARR next year, right?

**Marcel Santilli:** With the mini sprints.

**Marcel Santilli:** And then check that drives are another 10.

**Marcel Santilli:** Now that's like 50 million less of  hard  clients that we need to serve over here, you know?

**Marcel Santilli:** And then that allows us more breathing room to actually build the platform at much faster so that, you know, but right now we're  if we keep like, it's like, there's no way to solve this thing other than rejuggling the packages and how we're changing it, you know, a little bit.

**Marcel Santilli:** And then I think on check that, there's this other thing too.

**Marcel Santilli:** It's like that I think Stefano did, right?

**Marcel Santilli:** It's probably a meltwater, but it's like the social listening piece.

**Marcel Santilli:** What are people saying about your brand?

**Marcel Santilli:** know, that to me all makes sense.

**Marcel Santilli:** Auditing my site, you know, like monitoring, like competitors, like there's all these kinds of like competitive intelligence, competitive listening, social listening, and brand listening.

**Marcel Santilli:** On top of AI visibility that that's like the check that name was like.

**Marcel Santilli:** I'm sorry.

**Marcel Santilli:** Perfect for as well, you know, that can add a lot of like value so that you have these like higher bundles, essentially like packages, right?

**Marcel Santilli:** Like there are like 500 to 2000 a month, you know, that, that you can create as well.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** No, that makes sense.

**Daniel Lopes:** But they're all things that we actually have planned as potential opportunities for the inventory.

**Daniel Lopes:** then you can start there and do that in a non-scalable way, less scalable way there, and then move to the lighter version.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So good news is, if we're aligned here, Andy's already on the Path A, and I'm spending a lot of time on Path A.

**Marcel Santilli:** And so now Path B, know, Jason, like the goal is like, how do we unfuck your bandwidth to be able to focus on Path B, pretty much, you know?

**Marcel Santilli:** And, and then the engineering lanes are already well-defined, you know, so there's

**Marcel Santilli:** Like big thing here.

**Marcel Santilli:** I think it's mostly like planning out a proper AI-led growth launch, a packaging so Tyler could, you know, and like, it doesn't need to be next week, but like what Tyler could sell here, you and I can work on that.

**Marcel Santilli:** And then the check that launch plan and packaging and kind of like, you know, just three months out, doesn't need to be six months out, you know, like just like the next two months, if you will.

**Jason Gong:** um, and, um, yeah, I think like roadmapping what path B looks like is a helpful exercise, but it still doesn't feel like we've totally decided on like how many separate pieces there are or is it just one, you know, so I think we should, we should decide on that.

**Jason Gong:** And then it sounds like the first phase is just AI-led growth plus a mini sprint, right?

**Jason Gong:** From the sounds of it, whether that lives in our own tool or just a notion, I guess it doesn't matter.

**Jason Gong:** And then at some point, hopefully soon we'll have checked that and peace.

**Jason Gong:** This is the content inventory, and then that's the part where, like, I think we need to think through, like, what this thing looks like, and what to build.

**Marcel Santilli:** Yeah.

**Jason Gong:** That makes sense.

**Marcel Santilli:** mean, I think about this math, because, like, literally, yesterday I spent, like, four hours just for fun, like, Vibe coding in Figma, and I was, like, Vibe coding here, and then going to these other apps and playing with it, and being like, this is so garbage here, I wish I did this.

**Marcel Santilli:** And I would just put that instructions to Figma, and it would build us so much better with one prompt, and I know it's, like, obviously that's just front end, but it's just, like, man, people are getting the experiences so wrong, and they're so out of touch with reality, because they've never done the job, and we've all done the job, and we have the services to do, and the revenue from the services allow us to do things that no one else can do.

**Marcel Santilli:** Even with  You VC money, they can't do that, you know, that I think that puts us in a good place.

**Marcel Santilli:** And so, my number one.

**Marcel Santilli:** One priority right now is like, like, action, Path A, and, and like, and honestly, it's like, right now, like, the delivery side is actually not that bad.

**Marcel Santilli:** Like, and, like, for the most part, even the MEs, like, the worst things I've heard so far in the listening tours is, until Agentic is deployed, I'm working 70 hours a week.

**Marcel Santilli:** That's the worst I've heard so far.

**Marcel Santilli:** But I love the people I work with.

**Marcel Santilli:** I believe in the company.

**Marcel Santilli:** It's like, I'm really excited.

**Marcel Santilli:** I get to work on really cool clients and really smart people.

**Marcel Santilli:** Like, you know, like, so it's like, Jocelyn was just like, I'm working 70 hours a week because, you know, I need the Agentic workflows and requires a lot of me working.

**Marcel Santilli:** That's the worst I've heard.

**Marcel Santilli:** And then the other part is just like, staging is really hard.

**Marcel Santilli:** And Mariana is not delegating to Solomon fast enough on staging and she spends two hours a day staging content for the Adventurers group.

**Marcel Santilli:** Like, those are the two, but it's like, it's like, not that crazy bad.

**Marcel Santilli:** Most clients are actually fairly happy, you know, very few exceptions, and it's mostly some of those exceptions are like, like bad alignment internally, like the CEO fired the entire marketing organization on Prophecy.

**Marcel Santilli:** And so it's like, you know, like, what can you do there?

**Marcel Santilli:** Like, you know, like, or CodeRabbit from day one, the stakeholder was like, we're not going to give you any of the good opportunities, we're going to give you the leftovers, and I don't even know why we brought you.

**Marcel Santilli:** It's just because of investor introduced you, like, you know, so from day one, I wanted to fire them kind of, you know, like, so it's like, but for the most part, it's fairly, like, good, given everything.

**Marcel Santilli:** And so these other two lanes working just lessens the load as us trying to keep 100% retention on that side, because keeping 100% retention on the side means we're going to do really  things for  people that don't get it.

**Marcel Santilli:** Yeah, whereas like, if we have another alternative path, the faster that path is viable, the more we can have.

**Marcel Santilli:** And that's why I did the three stages of like qualification in the Oh, yeah.

**Marcel Santilli:** Second stage is like, are they actually excited to work with us?

**Marcel Santilli:** And then can we actually like serve them?

**Marcel Santilli:** And they're actually good potential clients.

**Marcel Santilli:** And so by doing it in three stages, it will allow us to get mostly the good people, you know, and then give a path to everyone else, you know?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** How does this align with Tyler?

**Daniel Lopes:** Tyler, it's like this, like the freemium part of it, or the cheaper package.

**Marcel Santilli:** I think that's great news, because it means like he can monetize and keep those leads warm and nurture by delivering Fathom.

**Marcel Santilli:** He makes a slightly higher percentage commission.

**Marcel Santilli:** It's less money, but it's like he's making money, you know?

**Marcel Santilli:** And I don't think he's too worried about making money.

**Marcel Santilli:** He's probably going to be the highest paid person in this company if he keeps selling this much.

**Marcel Santilli:** So it's like, you know, and for us, it's great.

**Marcel Santilli:** Like, I don't care.

**Marcel Santilli:** I would rather have just one AE, the whole company.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** That's all we need, you know?

**Marcel Santilli:** Like, Aerox has 20 E's.

**Marcel Santilli:** Profound has almost 40 already.

**Marcel Santilli:** Like 40 people in the sales organization already.

**Marcel Santilli:** Like, so it's like, like imagine if like 30% you ever had count as salespeople, you know, and for us it's like 3%.

**Daniel Lopes:** And then from the technical side, I finished, like we finished the Check That project.

**Daniel Lopes:** I finished the content inventory with Brad this month.

**Daniel Lopes:** And next month, we also finished the Looker replacement.

**Daniel Lopes:** And we'll try to add PostHog as well for you, Jason.

**Daniel Lopes:** And next month, we add client visibility so they can log in and see assignments, see maybe opportunities and their report.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And comment on the output.

**Daniel Lopes:** So that's the things that we're working on.

**Daniel Lopes:** And next month, I also start the framework team to figure out a way for folks to create workflows outside of the GrowthX and deploy them.

**Daniel Lopes:** Yep.

**Marcel Santilli:** So, I mean, does this.

**Marcel Santilli:** this.

**Marcel Santilli:** I would love for the board meeting, Daniel, for us to just agree on this, roughly, even if we don't share with Karan.

**Marcel Santilli:** But the way I summarize it is I use services more selectively to validate platform, right?

**Marcel Santilli:** And drive everyone else to check that in AI-led growth, what we just talked about.

**Marcel Santilli:** Convert, check that accounts to service by cherry-picking the best ones we want to service, if any of them, right?

**Marcel Santilli:** Yep.

**Marcel Santilli:** While keeping services high-end and selective, a.k.a.

**Marcel Santilli:** apply to work with us.

**Marcel Santilli:** Use the AI-led growth community as a training ground to recruit the best people for delivery.

**Marcel Santilli:** And let customers operate more of the platform over time and eventually hire talent via Marketplace.

**Marcel Santilli:** Release Output.ai to have anyone build and run workflows at scale.

**Marcel Santilli:** Create a mode and network effects with the Output.ai by making a more, like, hugging face-like Marketplace and a strong ecosystem, a.k.a.

**Marcel Santilli:** NAN and Zapier, and then this part is less common.

**Daniel Lopes:** But it's like, you know, keep building playgrounds for us to learn, right?

**Marcel Santilli:** Yeah.

**Daniel Lopes:** Like, last question.

**Daniel Lopes:** That makes sense to me.

**Daniel Lopes:** Like, I would just think a little bit more, but it generally does make sense.

**Daniel Lopes:** Like, the last question that I have is, like, we have the three roles, right?

**Daniel Lopes:** Directors, strategists, and editors.

**Daniel Lopes:** Now editors have levels.

**Daniel Lopes:** How do you see the directors?

**Daniel Lopes:** Because, like, what do you have, like, so if we scale PFA, strategists make sense to me.

**Daniel Lopes:** You're going to have a bunch of them.

**Daniel Lopes:** You need them for all accounts, essentially.

**Daniel Lopes:** And then editors are the ones performing the work.

**Daniel Lopes:** Directors, let's say you have, like, clients.

**Daniel Lopes:** Like, we add another 50 clients.

**Daniel Lopes:** Would you have, like, four directors?

**Daniel Lopes:** Or is it, like, not, are they acting more like consultants on special accounts?

**Daniel Lopes:** Or are they are, do they start to report to them?

**Marcel Santilli:** Like, what's the strategy?

**Marcel Santilli:** So, like, what I arrived at, and I told Andy this, is, like.

**Marcel Santilli:** Doing nothing is worse than moving forward with the next best thing we think it is today.

**Marcel Santilli:** And so what that means is like my version of what we need for directors is not necessarily what we need for the next 12 months is what we need this month.

**Marcel Santilli:** Like, which is, you know, Backfill, Kyle, and Panzer pretty much, right?

**Marcel Santilli:** And Jason.

**Marcel Santilli:** so we need, yeah.

**Marcel Santilli:** And so we need, and Jason.

**Marcel Santilli:** Like, so we need like two to three directors.

**Marcel Santilli:** And today, the best version of directors by far is Megan because Mara is pretty much a strategist and Jacob is based on, you know, today was like clear.

**Marcel Santilli:** was in the soliciting tour with, with both, with.
