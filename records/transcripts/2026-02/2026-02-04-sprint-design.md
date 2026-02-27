# Sprint design

<metadata>
date: 2026-02-04
time: 23:00 UTC
duration: 95 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, William, Leah, Ada, Daniel
fireflies_id: 01KGNCBC72J0RSQMAZEJZ44KB2
transcript_url: https://app.fireflies.ai/view/01KGNCBC72J0RSQMAZEJZ44KB2
</metadata>

---

## Summary

Deep working session on redesigning GrowthX's sprint delivery model. The team built out a health scoring system (green/yellow/red), defined pre-kickoff escalation processes, aligned on CheckThat integration strategy, and reviewed the Content OS platform for editorial workflows and client collaboration.

---

## Context

GrowthX is transforming its 8-week sprint delivery model for B2B content marketing engagements. This session focused on four critical areas: conversion health scoring to identify at-risk sprints early, a pre-kickoff escalation system, editorial workflow improvements through the Content OS, and how CheckThat fits into the sprint delivery without disrupting conversion rates. The team walked through detailed sprint milestones, client engagement signals, and the emerging platform that will automate content calibration and production.

---

## Relevance

**To GrowthX Delivery:**
- New health scoring system (green/yellow/red) based on client engagement and deliverable approvals within structured timeframes
- Critical sprint milestones defined for weeks 1-4: calibration article approval by week 2, content calendar by week 3, 3-5 articles/week by week 4
- Pre-kickoff process with SEO audits and escalation triggers in the 14 days before kickoff

**To CheckThat:**
- CheckThat access will be provided as a value-add to happy customers, not an upsell during sprints
- Revenue from CheckThat introduced at contract renewal or conversion, protecting sprint conversion rates
- Platform provides single source of truth for analytics including Google Search Console and crawl data

**To GrowthX Operations:**
- Content OS automating client-specific taxonomies, personas, and sample articles
- Multi-layered user roles (read-only, operator, admin) for client collaboration
- Target: MVP of Content OS and opportunity management system ready by early March

---

## Overview

- Health scoring system categorizes sprints as green, yellow, or red based on client buy-in, feedback, and scope clarity
- Weeks 3-4 focus on production ramp-up: content calendar approval and 3-5 articles per week delivery
- Pre-kickoff process formalized with SEO audits, tool setup, and escalation triggers
- CheckThat integrated as a value-add, not a revenue play during sprints
- Content OS demonstrated with automated taxonomy building, persona generation, and editorial feedback loops
- Sprint model potentially shortening from 8 weeks to 3-4 weeks with automation
- MVP target for Content OS is early March for live testing

---

## Key Topics

### Health Score & Risk Signals
- Green status requires strategy approval, content strategy approval, and active client engagement by end of week 2
- Yellow flags include missing context, unclear review processes, or delayed feedback
- Red status indicates lack of buy-in, scope creep, or major deliverable disagreement
- Positive signals: decision-maker involvement, client excitement over content quality
- Negative flags: tactical-only conversations, unclear stakeholder review processes

### Pre-Kickoff Escalation System
- 14 days before kickoff currently lacks formal operations
- New checklist includes SEO audits, CheckThat setup, monitoring tools, client material collection
- Escalation system clarifies when and who to escalate issues to
- Automated and manual signals trigger escalations (client responsiveness, system access readiness)

### CheckThat Integration & Pricing
- Access provided to happy customers without immediate extra charge
- Revenue introduced via contract amendments at renewal or conversion
- Platform serves as single source of truth for analytics (GSC, crawl data)
- Data feeds seamlessly into Content OS for editorial workflows

### Content OS Platform
- Automatically generates client-specific taxonomies, personas, and sample articles from website crawling and analytics
- Multi-layered user roles: clients get read-only, operators edit and annotate, admins manage workflows
- Page-level annotations, activity logs, and quality scoring for editorial feedback
- Executive summaries and impact reports showing published pages, impressions, traffic trends
- Clustering by content type, funnel stage, or persona for targeted improvements

### Sprint Transformation Vision
- Automated onboarding and calibration could reduce sprint length to 3-4 weeks
- Two client types: white-glove hands-off approach and self-serve content management
- Strategic advisory roles growing with EMs and MEs providing business insights
- Training and feedback loops with automated rubrics for editor improvement

---

## Action Items

**Marcel**
- Share detailed sprint structure and process documents with the team by end of week
- Continue building crawler and metric collection system for workspace setup
- Lead CheckThat integration exploration and client usage demo
- Oversee taxonomy and persona development for calibration automation
- Coordinate training plan for editorial quality feedback loop

**William**
- Prepare to manage new sprint customer workflows using updated tooling

**Leah**
- Develop custom Notion system for sprint product management workflows

**Ada**
- Engage in parallel testing and feedback on opportunity generation and calibration tools

**Daniel**
- Conduct CheckThat usage demo during sprint meeting follow-up

**Team-wide**
- Transition from Google Docs to Notion for sprint documentation
- Implement weekly minimum Slack updates including meeting summaries
- Adopt pre-kickoff SEO audit as standard best practice
- Establish systematic annotation and feedback capture for editorial and technical review
- Target first-week March for concurrent tool validation

---

## Transcript
**Golden Gate:** Choose and improve conversions.

**Golden Gate:** Ultimately, we want to come out of this a very clear system that the whole team can start using already next week, which gives clarity on risk and escalation and everything else.

**Golden Gate:** So what we're going to try and cover is these four sections, which is the health score and conversion risk signals, which is what you brought up, Bella.

**Golden Gate:** The escalation system pre kickoff, which is something that we're not doing yet.

**Golden Gate:** So I just added this from Marisol's doc as, like, what she had put as expectations for the EM.

**Golden Gate:** The ME in the 14 days prior.

**Golden Gate:** Oh, and this is probably because we only have, like, a week ahead right now.

**Golden Gate:** Right now we're a week ahead.

**Golden Gate:** Yeah, but.

**Golden Gate:** But Tyler was telling us he's.

**Golden Gate:** I think he's almost two weeks ahead now.

**Golden Gate:** I think he's getting closer to a recent.

**Golden Gate:** So that just means that, like, Panzer, you and I also have to be further ahead with who is the en.

**Golden Gate:** And any.

**Golden Gate:** Right.

**Golden Gate:** Anyway, this part is going to be a little tricky because we need to figure out how to, like, not just what is the minimum sort of checklist that we want to implement, but also, like, how do we integrate this into our current operations?

**Golden Gate:** And then I have two fives.

**Golden Gate:** There we go.

**Golden Gate:** And then editorial systems, basically, like quality communication, learning loop, and lastly, handoff after conversion.

**Golden Gate:** I don't know if we're going to get to all of these, but if we were to really just focus on a couple, what seems the most crucial to you guys?

**Golden Gate:** I think pre kickoff.

**Golden Gate:** That is one of them.

**Golden Gate:** Okay.

**Golden Gate:** Yep.

**Golden Gate:** There's a health score on conversion risk signals.

**Golden Gate:** I think we have to go through this one.

**Golden Gate:** Yes, exactly.

**Golden Gate:** Absolutely.

**Golden Gate:** I also think oscillation system is really important.

**Golden Gate:** Yeah, I think of those three.

**Golden Gate:** Let's try and knock those three out.

**Golden Gate:** Okay.

**Golden Gate:** So let's just start with the first one, then we zoom back in.

**Golden Gate:** So, defining sprints, health signals, what is green, yellow, and red specific for the sprints?

**Golden Gate:** Define any kind of forecasting that we can do and then agree on specific, like, trigger training warnings that will.

**Golden Gate:** That will override the score.

**Golden Gate:** So you gave an example of, like, the CEO, the main stakeholder leaves, that would override whatever score was there as like, okay, we got to do something.

**Golden Gate:** Just start with the first one.

**Golden Gate:** What is green, yellow, and red for this sprint?

**Golden Gate:** Okay.

**Golden Gate:** I think an easy.

**Golden Gate:** A simple way to define green, yellow, red would be to go.

**Golden Gate:** I think maybe every go every two weeks.

**Golden Gate:** So.

**Golden Gate:** Because it's different for every.

**Golden Gate:** I wouldn't say every week, but I think every two weeks, the stages of the sprint.

**Golden Gate:** As it progresses, the risks change.

**Golden Gate:** So I think the first two weeks, and I'm just saying this off the top of my head, so strategy isn't approved.

**Golden Gate:** So the, the, the client has a lot of feedback on the strategies with the direction.

**Golden Gate:** They're not happy with the direction of the strategy.

**Golden Gate:** They don't understand it or they're just not fully like bought in.

**Golden Gate:** So how do they react to the strategy on save, like in the first two weeks.

**Golden Gate:** So just, just to clarify, you're talking about in the first two weeks, red would be.

**Golden Gate:** They're not bought into the strategy.

**Golden Gate:** Yeah.

**Golden Gate:** So a lot of feedback.

**Golden Gate:** I have never really had this, but I would say like red would be not bought in.

**Golden Gate:** A lot of feedback.

**Golden Gate:** Scope creep, scope change.

**Golden Gate:** Yes.

**Golden Gate:** Requesting like pivot.

**Golden Gate:** Yeah.

**Golden Gate:** Okay.

**Golden Gate:** Not clear on deliverables, like all of a sudden going like, okay, so we're going to get like seven.

**Golden Gate:** Wait a minute, where did seven come from?

**Golden Gate:** Yeah, right.

**Golden Gate:** I wonder.

**Golden Gate:** I was wondering if it's useful just to say what green is and then kind of under each.

**Golden Gate:** What the reasons why it wouldn't be green.

**Golden Gate:** Yeah, that is that, that also is another way to like triage triggers also.

**Golden Gate:** So green would be artifacts approved, content strategy approved.

**Golden Gate:** Yes.

**Golden Gate:** And also calibration Oracle proves if we're moving it up, then potentially calibration Oracle also proves that's green.

**Golden Gate:** I would also.

**Golden Gate:** Let's.

**Golden Gate:** End of first two.

**Golden Gate:** Yes.

**Golden Gate:** Specifically, I think also to add to green, I would say that there has to be like a relationship element, meaning that they feel maybe not enthusiastic.

**Golden Gate:** I thought there's a sentiment.

**Golden Gate:** Yeah.

**Golden Gate:** There should be a sentiment of or.

**Golden Gate:** Yeah, they're like in it.

**Golden Gate:** Yeah.

**Golden Gate:** Responsive.

**Golden Gate:** Like it really depends on the personality type that you're dealing with.

**Golden Gate:** But it's important.

**Golden Gate:** Well, and so maybe it's maybe not relationship, but engagement signals equal, you know, active and proactive.

**Golden Gate:** It's not just us pushing things to the client, but the client is responding and ideating in slack to us.

**Golden Gate:** Green is they are showing up to meetings prepared, you know.

**Golden Gate:** Alignment on jobs to be done between the two parties.

**Golden Gate:** I've seen that happen.

**Golden Gate:** You know, they're like, oh, well, that's not our job.

**Golden Gate:** Like that's your job.

**Golden Gate:** Right.

**Golden Gate:** So do we have good alignment there?

**Golden Gate:** Like what are we doing for you and what do you need to bring in order for us to do our job?

**Golden Gate:** I think green is stakeholder and ownership is clearing that up.

**Golden Gate:** Because, you know, if I've like watched some of the Nazi calls, like people like start bringing people in and approvals Start to slow down or somebody introduces legal and free and like, you know.

**Golden Gate:** Or so and so was busy when it started, but now they're here and they're going to be the gate or they got access to everything that we need.

**Golden Gate:** Gsc, their attribution system.

**Golden Gate:** Yeah, they're.

**Golden Gate:** Oh, yeah, I get why we're doing it, like, on the week by week, but each one of these are just like, important milestones that we can look at, like, as just a milestone.

**Golden Gate:** If we get this done and it's green, the account is green and like, some can be pulled like you're already pulling the comp, the calibration earlier.

**Golden Gate:** So it's kind of agnostic of weak.

**Golden Gate:** It's more.

**Golden Gate:** So if we do the sheets.

**Golden Gate:** Yeah, right.

**Golden Gate:** We're in a good spot for success overall for the client.

**Golden Gate:** Yeah, exactly.

**Golden Gate:** I think, like, even if the person is not ticking every box, if at the end of those first two weeks they're looking at what is green, what is supposed to be green, then they get a good sense of what score they should be giving.

**Golden Gate:** You know, in.

**Golden Gate:** In the tracking document, they're like, okay, I've gotten 80% of these done.

**Golden Gate:** Cool.

**Golden Gate:** I think this is.

**Golden Gate:** This is great.

**Golden Gate:** Right?

**Golden Gate:** Yeah, Yeah, I agree.

**Golden Gate:** One other thing I would add here in the first two weeks, if we're looking at it by weeks, is like, we have all the context that we need from them.

**Golden Gate:** So we do the kickoff bubble.

**Golden Gate:** We also always get a ton of materials.

**Golden Gate:** And there's kind of two types of clients.

**Golden Gate:** There's one that gives us nothing to start, which you have, which is elementum coming up, and it takes more effort from the em and it's like, still kind of a gray area of how successful we can be consistently with the climate because it's nothing.

**Golden Gate:** Ramp was a lot of customers, so we're thinking more standard.

**Golden Gate:** The more context, the better.

**Golden Gate:** But either way, you can bucket the clients until either or we have all the materials that we need from them.

**Golden Gate:** Have we done the deep dive, etc.

**Golden Gate:** That's still all under context gap.

**Golden Gate:** So, again, good context.

**Golden Gate:** Can you, Bruce Rank, if you weave one, can you one ever?

**Golden Gate:** I think that's another signal that we're in a better spot.

**Golden Gate:** So would we ever turn anyone yellow in a cup?

**Golden Gate:** Like, if they don't give us all of this and then you feel like you're starting week one a little behind that?

**Golden Gate:** Like, would you call it yellow or is it just.

**Golden Gate:** No, it's not yellow.

**Golden Gate:** It's just.

**Golden Gate:** No, we don't.

**Golden Gate:** It will be yellow.

**Golden Gate:** If we can't recover by the end of week two, I would say the lender.

**Golden Gate:** Yeah, I would say it depends because some clients, they just don't have the build up of themselves as a company yet.

**Golden Gate:** Which might be a little bit of a flag, but they're super.

**Golden Gate:** Yeah, but they're super open to whatever we can develop for them.

**Golden Gate:** Yeah, ideally we don't want those types of clients.

**Golden Gate:** Perfect world is, you know, some of what you want already, your brand, your style.

**Golden Gate:** You're telling them.

**Golden Gate:** It just has to be built into the.

**Golden Gate:** Yeah.

**Golden Gate:** Level of effort.

**Golden Gate:** For sure.

**Golden Gate:** Okay, let's talk about two to four.

**Golden Gate:** So at this point you're.

**Golden Gate:** You've approved the content strategy and now you are.

**Golden Gate:** You should be ramping up.

**Golden Gate:** Well, you should be doing the product deep dive and the CMS walk through.

**Golden Gate:** I guess that should have been done.

**Golden Gate:** Product deep dive is one ideally.

**Golden Gate:** But it would be a really weak too.

**Golden Gate:** So.

**Golden Gate:** Okay, so then.

**Golden Gate:** And the CMS is also.

**Golden Gate:** CMS should.

**Golden Gate:** At this point we should be given access before the kickoff.

**Golden Gate:** Filers were pushing to get us access here before the kickoff.

**Golden Gate:** So that's.

**Golden Gate:** I'm not talking about access.

**Golden Gate:** I'm leading the walkthrough.

**Golden Gate:** The little like meeting where they talk us through it.

**Golden Gate:** Oh yeah, we can.

**Golden Gate:** That'd be cool.

**Golden Gate:** Yeah.

**Golden Gate:** Depending.

**Golden Gate:** I've not been week one or two in the last couple that.

**Golden Gate:** I mean, depending on the cms, sometimes.

**Golden Gate:** You don't need them all through.

**Golden Gate:** Like if it's webflow, it's more press.

**Golden Gate:** Like it's really.

**Golden Gate:** Okay.

**Golden Gate:** Okay, well put those aside.

**Golden Gate:** Then two to four then we're talking about ramping up.

**Golden Gate:** So two to four is.

**Golden Gate:** So the content calendar is a big one.

**Golden Gate:** So early week three, that's when we like take the strategy and create the content.

**Golden Gate:** Okay.

**Golden Gate:** So green is content calendar is done and approved.

**Golden Gate:** Yeah, approved.

**Golden Gate:** Content OS is completed, reviewed and approved.

**Golden Gate:** Yeah, like not, you know, minimal feedback to topics.

**Golden Gate:** And the subtask of that would be keyword research.

**Golden Gate:** Yeah.

**Golden Gate:** The competitive analysis would be done in pre K off before for the strategy.

**Golden Gate:** I thought now.

**Golden Gate:** But for the week two it will be in the future it'll be before we even kick off.

**Golden Gate:** But for now it has wanted to the strategy.

**Golden Gate:** You do need it.

**Golden Gate:** Yeah.

**Golden Gate:** So I'm doing it before I build the strategy.

**Golden Gate:** So for the recent kickoffs, I've been doing it even before the kickoff.

**Golden Gate:** That's how.

**Golden Gate:** Right.

**Golden Gate:** Yeah, but now.

**Golden Gate:** But in the past it was before.

**Golden Gate:** You built the strategy that we would.

**Golden Gate:** Do the competitive analysis.

**Golden Gate:** Any concerns about that?

**Golden Gate:** No, I'm I'm just like absorbing this because it's like, oh, that didn't happen.

**Golden Gate:** That didn't happen this moment.

**Golden Gate:** Yeah, well, this is clearly why we need this.

**Golden Gate:** Okay.

**Golden Gate:** Yeah.

**Golden Gate:** So content OS is approved.

**Golden Gate:** Sorry, Sydney, just to clarify here, should this be week three to four and the content OS should ideally be approved by end of week two.

**Golden Gate:** Right, Right.

**Golden Gate:** Three, four.

**Golden Gate:** Also, if we're moving calibration to end of second week, then, like, we should also have something about calibration in the first two weeks.

**Golden Gate:** Like calibration article should be in.

**Golden Gate:** Customers should have at least seen it if not given feedback.

**Golden Gate:** That's right.

**Golden Gate:** Yeah.

**Golden Gate:** We're seeing calibration article proven in the first two weeks, but it's most likely not going to get approved.

**Golden Gate:** Generated.

**Golden Gate:** Created.

**Golden Gate:** Like set generated.

**Golden Gate:** There we go.

**Golden Gate:** Delivered.

**Golden Gate:** Deliver.

**Golden Gate:** There we go.

**Golden Gate:** Calibration article is approved.

**Golden Gate:** Approved.

**Golden Gate:** Okay.

**Golden Gate:** And then ramp up production.

**Golden Gate:** Right.

**Golden Gate:** By week four, you just want to ramp up production.

**Golden Gate:** Yes.

**Golden Gate:** So ideally week three would be doing three articles and then in week four we do three, five.

**Golden Gate:** Yeah.

**Golden Gate:** Okay.

**Golden Gate:** And also on the publishing side, so week three, it should be their cms, like ready to publish.

**Golden Gate:** Article in their.

**Golden Gate:** CMS st. Do you see Sydney Stoke too?

**Golden Gate:** No.

**Golden Gate:** So what did she say?

**Golden Gate:** Excellent.

**Golden Gate:** And published for calibration in week three, four.

**Golden Gate:** Yeah, yeah, sorry.

**Golden Gate:** Just ADA said it and then I typed it and disregard me, ignore me.

**Golden Gate:** Okay, what are some other of like the.

**Golden Gate:** Besides just our activities, what are some of the other signals?

**Golden Gate:** Sentiment, business.

**Golden Gate:** I would say for us to be green decision maker, the person paying the check is still involved somehow.

**Golden Gate:** Yes.

**Golden Gate:** Right.

**Golden Gate:** And are there any other sentiment or other signals, like stakeholders feel clear?

**Golden Gate:** I think a very clear signal for me is that they're happy and.

**Golden Gate:** Or excited about the calibration article because the opposite is true.

**Golden Gate:** Like it's red.

**Golden Gate:** At their first experience with our calibration, our first three articles is bad.

**Golden Gate:** That crushes their trust.

**Golden Gate:** Yeah.

**Golden Gate:** All right, so content quality, like, so the positive signals is they believe in content quality.

**Golden Gate:** The second, I would say like the reverse, which I'm probably not helping you with.

**Golden Gate:** The way I'm saying this.

**Golden Gate:** I said let's start with green and then like, whatever.

**Golden Gate:** But like I was just in a call with like a pod customer and we for sure have a word babysitter on the other end.

**Golden Gate:** To.

**Golden Gate:** His boss likes us, but he is absolutely keeping us from publishing, doing all the things.

**Golden Gate:** So that would be.

**Golden Gate:** Sorry.

**Golden Gate:** So you want me to put that in here?

**Golden Gate:** It's just kind of easier to test, I think.

**Golden Gate:** But it is like I. I have.

**Golden Gate:** Big older if you want to put that in like terms it's like that's operating at the wrong level.

**Golden Gate:** Like they're not thinking strategically.

**Golden Gate:** They're thinking way, way too great on leaders concepts or about the content.

**Golden Gate:** And like managing that has to be like well we need to managing it later.

**Golden Gate:** But like it's relationship management thing.

**Golden Gate:** But the assessment like reading red assessment would be like conversations are majority tactical versus regardless strategic.

**Golden Gate:** Right.

**Golden Gate:** Two more things here like Calvary article approved as an outcome.

**Golden Gate:** But what like we uncover during that process is their review process, the stakeholders review process and like how it actually works.

**Golden Gate:** That has changed multiple times from what we heard from kickoff to like when we're actually sending an article over.

**Golden Gate:** And then my founder actually look at this the first few times or we actually have the subject matter expert that we're pulling in to review.

**Golden Gate:** So like not having a clear understanding of how the reviews actually work to me would turn it yellow versus yellow.

**Golden Gate:** Yeah.

**Golden Gate:** So but that in the green would be clearly identified and working with their, with their review review process.

**Golden Gate:** Correct.

**Golden Gate:** And then what I've, what I've done with every stakeholder that I managed was by week four I always have like a one on one sidebar.

**Golden Gate:** Just checking in like helping them unblock anything for themselves.

**Golden Gate:** Like what you did with CRV with Krista.

**Golden Gate:** She was out for two weeks and struggling with keeping up with what to actually review.

**Golden Gate:** You just sat with her enough.

**Golden Gate:** Right?

**Golden Gate:** Guys, hey, let's look at this.

**Golden Gate:** Let's focus on this article.

**Golden Gate:** This is why reviewing up front is super important.

**Golden Gate:** I do that one on one sidebar.

**Golden Gate:** Outside of like the meetings as well by like lean forward just to make sure we're like still aligned on how everything's moving, that everything is operating the way it should be on our end and that they're happy with it.

**Golden Gate:** Still has not.

**Golden Gate:** She still hasn't.

**Golden Gate:** I have to I'm gonna call her tomorrow and like yeah.

**Golden Gate:** So positive signal getting back to.

**Golden Gate:** And she told me you promised me we were going to talk to folks is the like the magic sauce that we're.

**Golden Gate:** We're dripping where there's a magnetic pull.

**Golden Gate:** Of the customer to be proactively sharing.

**Golden Gate:** Thought leadership because of you know, we are sharing like hey we saw this observation or I heard of X, Y and Z in the marketplace or you know, I'd like to do better.

**Golden Gate:** I don't know who owns this.

**Golden Gate:** So it's kind of like an action for me.

**Golden Gate:** But if one of the desires was to have thought leadership in our community and teased out Things that Marcel system does and we can like read it to our customers and you know what I mean?

**Golden Gate:** Like there's things that we want to enable you all to do that raise the level of what this.

**Golden Gate:** What the conversation is.

**Golden Gate:** So when I, When Marcel does a lot of like look at my channel, you know what you actively see is he but puts into gold and then you see this proactive where they're like I just woke up last night.

**Golden Gate:** I had this great thought.

**Golden Gate:** Like that sentiment of there's a proactive push of the customer in the channel is very different than receiving activity updates from us and being proud of our activity.

**Golden Gate:** It's like just a different level.

**Golden Gate:** Yeah.

**Golden Gate:** I'm putting this into the sort of editorial system.

**Golden Gate:** This is a different section but it's.

**Golden Gate:** It's really.

**Golden Gate:** I'm just writing down here to say ultimately what I'm hearing is what we need to systematize is that it's.

**Golden Gate:** We are proactively your content strategist or your.

**Golden Gate:** Your organic strategist and we're proactively sharing information and that that needs to be in the ENS just ongoing role.

**Golden Gate:** Our magic Drip campaign.

**Golden Gate:** We could call that Magic Drift campaign.

**Golden Gate:** Love it.

**Golden Gate:** Yeah.

**Golden Gate:** Sharing.

**Golden Gate:** Proactively sharing.

**Golden Gate:** Yeah.

**Golden Gate:** It doesn't even have to be like brand new information or that much extra work.

**Golden Gate:** You're already.

**Golden Gate:** Or Cathy already put together a content strategy for Daylight.

**Golden Gate:** Yeah.

**Golden Gate:** Within that content Strategy she broke down 26000 keywords and 19 different competitors and like mapped a few different opportunities.

**Golden Gate:** You can just like give some insights.

**Golden Gate:** Hey, we did a bunch of this work.

**Golden Gate:** These initial insights that we got.

**Golden Gate:** Well then with myself when you were many times showing me is he would.

**Golden Gate:** When he was doing the food kickoff work, he basically had the entire library like kick ass stuff.

**Golden Gate:** And he did not feed it all at once.

**Golden Gate:** You would just start like feathering it in.

**Golden Gate:** So it's almost like you have like this great value material and so then.

**Golden Gate:** It'S just a judgment of when you.

**Golden Gate:** When you pull it in.

**Golden Gate:** Quickly contextualize everything for you.

**Golden Gate:** Marcel, we had a meeting this morning where we discussed everything you see back here.

**Golden Gate:** It was really the structure of how EMS and mes work together and make that stronger and tighter.

**Golden Gate:** And then the second part was around speeding up the calibration process.

**Golden Gate:** So we were very clear on those two bits and we came through I think with some good action items.

**Golden Gate:** And then lastly product management.

**Golden Gate:** That's been a challenge in the Sprint cycle is how we product management, what tools we use.

**Golden Gate:** So that was this morning.

**Golden Gate:** We got that sorted and then now we're really focusing on what do you mean, what tools you use.

**Golden Gate:** We're going to shift over to notion.

**Golden Gate:** Leah is going to build sort of a custom piece for us for the.

**Golden Gate:** Sprints.

**Golden Gate:** As opposed to linear.

**Golden Gate:** The world will still be enough in terms of all the things you manage.

**Golden Gate:** Been challenges with getting people to use linear.

**Golden Gate:** They just find it very frustrating.

**Golden Gate:** So stuff, we're just like, okay, let's.

**Golden Gate:** Let's create a good customized system for people to probably by the way, regardless of what you're using, like these linear stuff.

**Golden Gate:** So for instance, like linear.

**Golden Gate:** I also like using linear.

**Golden Gate:** But the fact that like I can be in a thread that has 50 things and you want a linear starter to take it from me for this client and it automatically puts it in the right place.

**Golden Gate:** Notion won't do that for you often.

**Golden Gate:** But anyways, like, but, but regardless, like, like asking cursor or plot code or something to just like create a something in notion or we can't do it in notion.

**Golden Gate:** I'm sorry, you.

**Golden Gate:** You can.

**Golden Gate:** Notion is not a good like text management system.

**Golden Gate:** So for instance, like there's, there's a bunch of little things.

**Golden Gate:** Like for example, a page is a page.

**Golden Gate:** Page is not like a task.

**Golden Gate:** A task is a completely separate thing.

**Golden Gate:** The notion that it's not well tracked.

**Golden Gate:** It doesn't have a lot of taxonomy around.

**Golden Gate:** So the, the, the, the.

**Golden Gate:** My macro point here is like the, there's ways to not have to almost interact with linear and still be able to track it, you know, but, but if you want to try, like, I mean, we started with notion and the main reason people wanted to get off notion.

**Golden Gate:** I don't want to get off notion, but the reason people want to get off notion is because there's like no way to like find all the tasks.

**Golden Gate:** Like so, so like you have a page and that page will have 10 tasks.

**Golden Gate:** That task will have like no owners and nothing.

**Golden Gate:** And it's just like they just are.

**Golden Gate:** Tests are just like out in the universe and you just can't find them.

**Golden Gate:** And you can't like create a view of only tasks.

**Golden Gate:** You can create a view of pages.

**Golden Gate:** You can have pages be like a holding thing, you know, like that.

**Golden Gate:** But then that's kind of different.

**Golden Gate:** You know what I mean?

**Golden Gate:** Okay, cool.

**Golden Gate:** Yeah.

**Golden Gate:** And then this session is really talking about like very specific process elements that we want to try and cover.

**Golden Gate:** So the first one was around health score and conversion risk signals.

**Golden Gate:** That's what we've been working through the escalation system.

**Golden Gate:** So when and how and who to escalate things to.

**Golden Gate:** That's also been a.

**Golden Gate:** Something's been missing.

**Golden Gate:** The pre kickoff, basically we're not doing this now.

**Golden Gate:** Those 14 days before the kickoff happened, we're not doing any of this.

**Golden Gate:** So we went to talk through process for integrating that and then something around the editorial system and then the handoff electric conversion.

**Golden Gate:** We decided we're probably not going to get through all this today.

**Golden Gate:** So we're really focusing on the health score, the escalation system and the pre kickoff.

**Golden Gate:** That's, that's where we're at right now.

**Golden Gate:** Can I just have a pretty, pretty please ask.

**Golden Gate:** Let's not use Google Docs ever.

**Golden Gate:** Please, please, please, please, please, please, like ever.

**Golden Gate:** Like 100 of companies in ocean.

**Golden Gate:** I really don't want to like I, I see it so much now in clients and it's just like everything's an ocean.

**Golden Gate:** Like everything's integrated in ocean.

**Golden Gate:** So it's like I will like for instance, if I wasn't in this room, I would never find it.

**Golden Gate:** Ever, ever be able to find this.

**Golden Gate:** And then it's lost, you know.

**Golden Gate:** Whereas like now like we have MCPS and Notion, like notion is integrated with Slack and it's like Google Docs are just get lost, you know?

**Golden Gate:** Yeah, I get that.

**Golden Gate:** No, but that's just like a side note.

**Golden Gate:** Yeah.

**Golden Gate:** For like our notion is though, where like the source of truth is this for me, is it working?

**Golden Gate:** It's like scribbling on a piece of paper.

**Golden Gate:** That's why I did it.

**Golden Gate:** Cool, cool.

**Golden Gate:** All right.

**Golden Gate:** So we were talking through the first two weeks, then three to four weeks, five, six, seven, eight.

**Golden Gate:** And what is green?

**Golden Gate:** What is red?

**Golden Gate:** And really the idea here ultimately is for us to get very clear on.

**Golden Gate:** Are we in the.

**Golden Gate:** Can you send me a link to this?

**Golden Gate:** Yeah.

**Golden Gate:** Are we in a good position right now with the clients?

**Golden Gate:** Is this something that we need to, you know, flag.

**Golden Gate:** One second.

**Golden Gate:** Here we go.

**Golden Gate:** Okay, so just jumping back to three and four.

**Golden Gate:** What is, what is red for us other than the content, I guess the content OS is not approved.

**Golden Gate:** We're not publishing.

**Golden Gate:** So therefore we won't be getting signals.

**Golden Gate:** Yeah, we're not publishing.

**Golden Gate:** And by the way, the, the, there are some, some of those things are already like written down in the eight week.

**Golden Gate:** Yeah doc.

**Golden Gate:** That have like the, like the risks that we're trying to mitigate in each.

**Golden Gate:** You know.

**Golden Gate:** And so like we can also use that a little bit too.

**Golden Gate:** Like for instance, like week four risk.

**Golden Gate:** We're targeting the risk of getting stuck in approval Cycles or publishing bottlenecks.

**Golden Gate:** Why does it matter?

**Golden Gate:** Is this the Marisol build?

**Golden Gate:** This is what I wrote.

**Golden Gate:** Like, I know you're not.

**Golden Gate:** October 2020.

**Golden Gate:** Yeah, it's called the.

**Golden Gate:** The, like.

**Golden Gate:** Yeah, I spent a lot of time on this one.

**Golden Gate:** But.

**Golden Gate:** But, like, so layer that in on additional learnings versus, like, I would encourage us to do that as well.

**Golden Gate:** Or say this was wrong because of X, Y and Z, you know, But I think that that's a good, like, frame into, you know, like.

**Golden Gate:** Because I think this is more granular, which is good.

**Golden Gate:** Right.

**Golden Gate:** But then, like, layering it in within that context, you know.

**Golden Gate:** Yeah, you're.

**Golden Gate:** You're just sort of like, yeah, why?

**Golden Gate:** It's great.

**Golden Gate:** And then this is sort of the.

**Golden Gate:** What do we need to listen for that makes us know that we're off track.

**Golden Gate:** Like, you know.

**Golden Gate:** Yeah, yeah.

**Golden Gate:** It's like.

**Golden Gate:** Like what.

**Golden Gate:** What you're doing is adding, like, a trigger to, you know, like.

**Golden Gate:** I see it.

**Golden Gate:** Yeah.

**Golden Gate:** Yeah.

**Golden Gate:** So for week four, let's see, for.

**Golden Gate:** What else do we have?

**Golden Gate:** I think let's say, like, on our end, red flags would be not keeping clients up to date with what we're doing, because there's a lot of activities in the first few weeks and we're like, constantly like, oh, here's the strategy, here's the content.

**Golden Gate:** OS Week 3, before, that's when we were kind of like, start publishing and start creating content.

**Golden Gate:** Things might feel like they're.

**Golden Gate:** We're not doing anything, and it's important that we're updating them on what we're doing, like, at least weekly.

**Golden Gate:** But, you know, we're, like, constantly kind of engaging.

**Golden Gate:** I would have.

**Golden Gate:** And, like, that's where Marcel said, I don't know if that's in your document about best practices, but, yeah, like, if it's happening, there's a lot of stuff happens off screen.

**Golden Gate:** But if it's not updated in Slack.

**Golden Gate:** Exactly.

**Golden Gate:** Yeah.

**Golden Gate:** Yes.

**Golden Gate:** And also, like.

**Golden Gate:** And I heard, like, I think I've pinged one or two of you.

**Golden Gate:** Like, hey, I'm not seeing anything slack.

**Golden Gate:** And I'm like, well, that's because we had a meeting.

**Golden Gate:** And like, I had.

**Golden Gate:** They wanted me an email.

**Golden Gate:** And so it's like, it felt sorted, but from the best practice behavior that we always wanted to do, it wasn't in his lack.

**Golden Gate:** So.

**Golden Gate:** And there should be minimum sort of meeting.

**Golden Gate:** Like, like Monday update.

**Golden Gate:** After the meeting, we send another, like, action item summary of the meeting.

**Golden Gate:** Like, that should be.

**Golden Gate:** Those two updates.

**Golden Gate:** Should be the minimum, I think.

**Golden Gate:** Yep.

**Golden Gate:** And I'm not as worried about you guys in general but anytime the only like if you get to week four or five and your only slack activity is reporting your only slack notifications are reporting activity and I know we're not getting results but there has to be like a different elevation of like what the.

**Golden Gate:** I can provide like an example example.

**Golden Gate:** So for Telera we just like published their calibration and I went into their Google search console and it's a refresh and you can see like when we published there's a spike in impressions and clicks and traffic and I just screenshotted it and shared it.

**Golden Gate:** Yeah.

**Golden Gate:** So it took me like five minutes.

**Golden Gate:** But it's something that we can do like like repeatedly.

**Golden Gate:** Yeah.

**Golden Gate:** And keep in mind like this is literally like March, like first week of March.

**Golden Gate:** Like this is the kind of thing that is like built into like the pages section of os like showing like impact on pages, you know and then being able to group those pages so like by a taxonomy.

**Golden Gate:** And the taxonomy is what's defined during the kickbox, you know, invite agents.

**Golden Gate:** So it's like think of the taxonomy as like a cluster by topic by you know, type or whatever, you know.

**Golden Gate:** So I would say not keeping it up to date on what we're doing.

**Golden Gate:** Slash the results.

**Golden Gate:** Yep.

**Golden Gate:** I mean early you, you may get.

**Golden Gate:** Yeah.

**Golden Gate:** In some cases you're going to get results but I think it's typically more in week five and six that you start to see something.

**Golden Gate:** I think if you are able to publish in week three, like I'm checking.

**Golden Gate:** Like within like within 10 days or.

**Golden Gate:** No, like in like three or four days if it's been indexed.

**Golden Gate:** Even if it's been indexed I'm like yes, like it's been indexed.

**Golden Gate:** So I like sure.

**Golden Gate:** O is there any flag?

**Golden Gate:** How many times has it happened?

**Golden Gate:** I feel like historically I been taught by you guys this happened a lot where if we don't check like we find out that their website's broken or we find out something sucks on their end.

**Golden Gate:** Yeah.

**Golden Gate:** I think oh the technical side of things.

**Golden Gate:** Then we got with Talal, he recorded a loom and a guy.

**Golden Gate:** We made it into a step by step guide for anybody to use the three tools.

**Golden Gate:** I'm doing it tonight for daylight and so there's no reason we shouldn't just be doing it either.

**Golden Gate:** Pre kick off early.

**Golden Gate:** I would add that as a, as.

**Golden Gate:** A best practice that's a, that's a pre kickoff thing.

**Golden Gate:** Ideally we should go into it knowing and again value add.

**Golden Gate:** We're telling them like you know your site's broken.

**Golden Gate:** There's only so much value.

**Golden Gate:** Add this.

**Golden Gate:** Yep.

**Golden Gate:** SEO audit.

**Golden Gate:** So hey Marcel, are you good with us just using going back and using this eight week plan, adding a pre kickoff and like adding this level of detail or do you want the sacrosanct and we have like a link to like more day to day behaviors.

**Golden Gate:** Do you care?

**Golden Gate:** Like add pre sprint?

**Golden Gate:** Well, we want to add pre sprint and we're really getting down to the nitty gritty of the behaviors we expect of ourselves, which is like you have like the broad like this is what break looks like and then translating into the.

**Golden Gate:** But do these actions and these are the risks look for these signals look like the things that are going to actually show up in the day to day behavior.

**Golden Gate:** So I just wanted to find out from you, do you want us just to pull it all into this as the one document bible or we can have a separate document that's more that has some disgrace and if you don't care, we'll figure out what works best for the team.

**Golden Gate:** But I just wanted to make sure we have a certain.

**Golden Gate:** I think ideally it's like there's separate objects.

**Golden Gate:** One is like the journey.

**Golden Gate:** Okay.

**Golden Gate:** And the high level of like what healthy looks like, you know, then it's like the definition of like.

**Golden Gate:** Okay, cool.

**Golden Gate:** Like the operator's guide too.

**Golden Gate:** Yes, exactly.

**Golden Gate:** Navigating the journey.

**Golden Gate:** Yeah, but you need to define the journey without overwhelming people in like a Bible, you know, and it's like you have the operator's guide and then you have the like the checklist on when a trigger happens based on the operator's guide.

**Golden Gate:** How to troubleshoot it.

**Golden Gate:** Right.

**Golden Gate:** Like a troubleshooting guide.

**Golden Gate:** The operator's guide and then the like the journey.

**Golden Gate:** Okay, we'll come back to the pre kickoff because that's one of the standalone topics that we discuss.

**Golden Gate:** Yeah, yeah.

**Golden Gate:** Let's talk a little bit about week five to six.

**Golden Gate:** Off the top of my head, content is index and performing by me getting impressions and clicks.

**Golden Gate:** Sydney, anything else on the editing side?

**Golden Gate:** I think this is when we start to like as we get into more topics, there could be things that like search has red flags on the editing side.

**Golden Gate:** Just making sure that all the feedback gets fed back into the pipeline, but also that there's not too many edits at this point.

**Golden Gate:** If we're still seeing a lot of edits from the customer, then we have to check if that's something wrong with our internal systems or if the customer is pivoting somewhat in their tone and their style and the messaging because that has happened where week three to four, great calibration, and then week five, suddenly the customer wants something new.

**Golden Gate:** So we do have to look at that.

**Golden Gate:** And the way that manifests is probably number of comments per piece, at least right now.

**Golden Gate:** You know, in our current system, future systems will have more metrics, but.

**Golden Gate:** Because you need a way to measure that, you know, rather than being like ad hoc or I don't know, they seem to be like, no, no.

**Golden Gate:** How many things are changing from a technical perspective.

**Golden Gate:** There's also like, when do you set up chat and when do you show to the client?

**Golden Gate:** Oh yeah, okay.

**Golden Gate:** So I think we're talking about setting up in pre kickoff checkpack.

**Golden Gate:** Yeah, should be set up like, because we have access to all of their systems, ideally pre kickoff, we can immediately file a local ticket and we can also set up their check back immediately.

**Golden Gate:** When it comes to presenting it, typically we don't have.

**Golden Gate:** I like to kind of space things out.

**Golden Gate:** Like I remember the guy from one of the stakeholders from Logic, he told us, I look forward to these meetings every week because every week there's something new and like I really like them.

**Golden Gate:** And we spaced out.

**Golden Gate:** So like one, like week three, after we present a strategy, week three, we show them the content os.

**Golden Gate:** If we have time, I'll show them Atlas.

**Golden Gate:** But typically Atlas is only 4 and check that as well.

**Golden Gate:** Or maybe even earlier, like check that might be like, I think it's more important.

**Golden Gate:** So I didn't check that week before.

**Golden Gate:** It makes sense to me.

**Golden Gate:** I don't know.

**Golden Gate:** I mean it's, it's, it's showing them like we could do in week two as well.

**Golden Gate:** So it's, for me it's, it's about like finding a balance because sometimes you just don't have time to go all together.

**Golden Gate:** Yeah, it's just I, I don't want, I definitely don't want to snowball us off topic, but I do have a quick question, Marcello, for you.

**Golden Gate:** But for check that in the pricing model, I had an EM ask me this and I didn't know how to answer it.

**Golden Gate:** They're like, well, what are we charging for them to have their own seats of check that or because for scrunch, we didn't charge customers for us using scratch.

**Golden Gate:** So like what, what the plan right now is to not charge extra, but it is to swap the revenue repeated and use it for existing clients as a leverage to get an early renewal.

**Golden Gate:** And what we can charge if we can.

**Golden Gate:** Right.

**Golden Gate:** Like you're not going to be mad if all Of a sudden we get.

**Golden Gate:** Fifteen hundred dollars extra a month, we wouldn't be mad.

**Golden Gate:** You're right.

**Golden Gate:** The.

**Golden Gate:** But if right now we have more clients that are at risk of churning.

**Golden Gate:** I know that's not in the Sprint.

**Golden Gate:** And then we have that are, you know, sweet, you know, like simple, whatever.

**Golden Gate:** And so like on that side, it's more of like using it as a.

**Golden Gate:** Think of it as like a dollar of checkout revenues worth 30x, a dollar of services worth 3x.

**Golden Gate:** And so like there's a 10x delta between those two revenues.

**Golden Gate:** That doesn't mean we.

**Golden Gate:** But the value of a dollar is still a value of a dollar in the bills.

**Golden Gate:** And so like you, you don't want to reduce the net that the net cash value, but the net valuation value of software is much higher.

**Golden Gate:** So like if and if you can use that as a value add of saying, hey, we have this thing, you set it up, it's collecting data.

**Golden Gate:** But in order for us to give you access, we just need to add some, you know, a small amendment to your contract and in an early renewal.

**Golden Gate:** You know, be a safely.

**Golden Gate:** But for these guys, is this something that Tyler is going to sell as of the REIT or say you get three months free.

**Golden Gate:** So these guys should be aware of.

**Golden Gate:** Hey, we're showcasing, we're going to help the conversion so that when you convert your new customer, there's no safe play.

**Golden Gate:** Like you're a new customer.

**Golden Gate:** Part of the conversion is great.

**Golden Gate:** Do you want seats per.

**Golden Gate:** Check that.

**Golden Gate:** And then they would do an addendum of the conversion upsell.

**Golden Gate:** Check that for new customers who are happy.

**Golden Gate:** So it's 1,500 extra.

**Golden Gate:** Is that a motion you want these guys to do?

**Golden Gate:** No, no.

**Golden Gate:** So we're gonna get right now.

**Golden Gate:** Okay, so think of it this way.

**Golden Gate:** Upselling before it's converted to ARR just means that we'll have more churn like if they don't convert or you know, so it's like it should be used as an extent because if it hasn't been sold by the time the kickoff AKA wasn't sold at all, then that like we can bring it up and use it as like an accelerant to convert them into ARR, you know, rather than a try to increase the net dollar and have to involve sales and have to involve like procurement and change the scope of the contract they signed.

**Golden Gate:** So they're basically just showcasing the awesomeness of check that.

**Golden Gate:** And if a customer is like I want seats to that we can have a separate conversation about.

**Golden Gate:** That's good.

**Golden Gate:** Okay, okay, I got it and I.

**Golden Gate:** Got what we're what would like.

**Golden Gate:** My intent is to add check that as a thing in the contract, right?

**Golden Gate:** Like that's like an extra 500 item that we just send it to them, you know like so that like we're a month, you know that that's just like there that hopefully like it means like when they're signing the contract, they're getting that and then very soon do the same thing with like content OS which then will give you access to check that as well as a full package.

**Golden Gate:** So think of it like right now when you get the invoice or you know it's like the skew is just like sprints and then growth execution and it's either one work stream or two work streams in growth execution.

**Golden Gate:** Right.

**Golden Gate:** So the skew is that versus that plus the platform fee essentially or two platform fees or whatever.

**Golden Gate:** Right.

**Golden Gate:** So that means like we're.

**Golden Gate:** It's already going to be there and so it's, it's going to be a lot like the expectation to be.

**Golden Gate:** It won't be about you all selling something that new like that that shouldn't happen, you know.

**Golden Gate:** But in the meantime, same way you would introduce crunch as something they're asking for and then they're asking you to do this thing.

**Golden Gate:** By the way, we have our own platform that already comes with your package.

**Golden Gate:** But if you want access to it and they don't already have it because it's this month and we haven't done it yet, then you can get it to like oh, we'll just do a quick amendment if you want to have it your own access.

**Golden Gate:** If not we'll run it ourselves instead of just screenshots and then you know, but if you want to have access just from like a legal and privacy perspective, we just need a quick.

**Golden Gate:** And that amendment will include like a quick swap of revenue, you know, so it won't be NFL for you.

**Golden Gate:** Swap of revenue meaning that you do less content or something a little less.

**Golden Gate:** Fifteen hundred dollar amount is going to be swapped discounted.

**Golden Gate:** One AB is coconut but that's your.

**Golden Gate:** I see.

**Golden Gate:** Okay, got it.

**Golden Gate:** Yeah.

**Golden Gate:** Can I take that?

**Golden Gate:** I mean this is a good question because I was also very.

**Golden Gate:** How do we self check that or talk about check that in spring.

**Golden Gate:** The question is always do I have access?

**Golden Gate:** And that's why I've been like in the past like two weeks have been bring it up because I don't know how to.

**Golden Gate:** So three months from now or so check that durable like feel great about it people ask.

**Golden Gate:** Yeah, I wanted to.

**Golden Gate:** If we can hit a pause and then, like, have Daniel do a quick demo.

**Golden Gate:** Yeah, sure.

**Golden Gate:** Okay, let's do that.

**Golden Gate:** And I'll come back.

**Golden Gate:** So my only thing, Marcel, not a safe play.

**Golden Gate:** Happy customer.

**Golden Gate:** We give them check that, like, they are able.

**Golden Gate:** Like, we.

**Golden Gate:** They don't have access.

**Golden Gate:** Check that.

**Golden Gate:** And like, you know, I really love it.

**Golden Gate:** It's all positive.

**Golden Gate:** You do not want to add incremental revenue even in that positive thing.

**Golden Gate:** It is.

**Golden Gate:** Let's just put it as like, tomorrow's thing to figure out.

**Golden Gate:** I added you to the thing in case you want to interrupt the meeting.

**Golden Gate:** No, no.

**Golden Gate:** Yeah.

**Golden Gate:** No.

**Golden Gate:** Like, your.

**Golden Gate:** Your point is, like, should we just upsell.

**Golden Gate:** Check that.

**Golden Gate:** Think of check that as we need that data no matter what, and no one else will give you that data today as an API.

**Golden Gate:** And that's going to be integrated into the os.

**Golden Gate:** Okay.

**Golden Gate:** And it's the same auth system between the two.

**Golden Gate:** Right.

**Golden Gate:** So what we don't want to do right now is just try to like people that already bought into the $200,000 package to try to upsell them for an extra thousand dollars on something that's meant to be a lean magnet or os.

**Golden Gate:** Like, check that if it brings us 0 revenue and 10x is our pipeline over here, we'll have done this job because we need the data no matter what.

**Golden Gate:** We need the learnings that we need the model no matter what.

**Golden Gate:** Right.

**Golden Gate:** Like, so.

**Golden Gate:** So this team should not be worried about pushing people from OS to check that.

**Golden Gate:** Like, absolutely not.

**Golden Gate:** Like, it is just a tool that we need to use right now.

**Golden Gate:** It's not pushing.

**Golden Gate:** It's like, if the customer's like, can I have some seats?

**Golden Gate:** Like, instead of giving it to them in exchange for the addendum, and we're talking like, four weeks.

**Golden Gate:** Like, well, okay, so we give them access in exchange for an addendum.

**Golden Gate:** Because we don't want to just give them something and not count it as revenue if they're truly, like, going to be using it, you know, like, we don't want it to be zero revenue.

**Golden Gate:** And so.

**Golden Gate:** But we don't need to upsell them right now, you know, like, now, if they're already past Sprint.

**Golden Gate:** Like, I do not want to upsell motions and Sprint that are like, right now, it's just not the priority.

**Golden Gate:** Like, I want conversions to be at 100% if that's the case, you know, I mean, if it's like, there's truly that value.

**Golden Gate:** Unless it's truly, like, meaningful revenue, meaning, like, it's like, you know, an additional work streaming, like what happened with Lava Vault, for example, in which case it's better for it to happen after the conversion because then it counts for an nrr if you do the.

**Golden Gate:** If you do the upsell during sprint, it doesn't count towards nrr.

**Golden Gate:** Right.

**Golden Gate:** Like, and so it's like upsells and sprints that are not a great thing necessarily, because it just means you're raising the bar and potential for.

**Golden Gate:** For.

**Golden Gate:** For not conversion.

**Golden Gate:** I guess.

**Golden Gate:** I.

**Golden Gate:** All right.

**Golden Gate:** And.

**Golden Gate:** And you're distracting from the work of proving yourself right, because you're now doing a sales motion instead of a go prove yourself motion.

**Golden Gate:** I'm sort of assuming it was at the point of conversion that, like, we're going to give everything in sprints.

**Golden Gate:** But then if they're like, hey, now I'm going to a pod and I want seats, what does the pod team do at that time?

**Golden Gate:** You just want it to be a straight.

**Golden Gate:** And we'll put this aside because I have, like, two or three things I want to make sure.

**Golden Gate:** Yeah.

**Golden Gate:** I feel like operationally we're not like, yeah, at the, like, holy shit.

**Golden Gate:** Everything.

**Golden Gate:** We got everything down.

**Golden Gate:** Like, that's what a lot of what we're doing right now, too.

**Golden Gate:** Right.

**Golden Gate:** Like, of just, like, we know, like, the triggers, the guides and things like that.

**Golden Gate:** And this is like, like, if we solve this, what the question you have right now on a product that hasn't launched until tomorrow at the service, at the disservice of, like, us speeding through and getting, like, everything else super figure out so that we really know how to go from two to three to four kickoffs, you know, like, we will figure out the rest.

**Golden Gate:** But I think it's, like, for everybody else, like, not necessarily more important than.

**Golden Gate:** Like, hey, yeah, we don't need your.

**Golden Gate:** Like, what are they?

**Golden Gate:** Calibration, things like that.

**Golden Gate:** But.

**Golden Gate:** But anyways.

**Golden Gate:** Oh, I invited you, but maybe didn't go through.

**Golden Gate:** Zoom should be like, like a call.

**Golden Gate:** Almost sounds like the answer.

**Golden Gate:** No.

**Golden Gate:** Try to add.

**Golden Gate:** Okay, yeah.

**Golden Gate:** Or who's that closer to me?

**Golden Gate:** I think you are.

**Golden Gate:** Oh, Yeah.

**Golden Gate:** I can do that.

**Golden Gate:** Yeah.

**Golden Gate:** Nice.

**Golden Gate:** You got it.

**Golden Gate:** Okay, great.

**Golden Gate:** Before we just transition real quickly, Marcel, like, with everything related to the sprint, what we.

**Golden Gate:** The reason why I came out as that ultimately is that we can take some clear learnings and structures around how we communicate, around how we organize and how we ensure that this runs as smoothly as possible and that we have a good transition in week 6, 7, 8, in order to convert.

**Golden Gate:** That's ultimately what we're what we've been working on.

**Golden Gate:** And so at the end of the week, I'm happy to share with you everything that we put together because, you know, there's bits that we haven't really gotten to share with you yet.

**Golden Gate:** But.

**Golden Gate:** Okay, that's what, that's what you're going to get out of this.

**Golden Gate:** Just want to close that loop.

**Golden Gate:** Sounds good.

**Golden Gate:** So we started the setup.

**Golden Gate:** Yeah, the setup.

**Golden Gate:** It doesn't look great.

**Golden Gate:** So that's fully working.

**Golden Gate:** But it's the beginning.

**Golden Gate:** Essentially every time you create a new workspace, you would type in a website and it would have this specific areas that would automatically start collecting the data for all the things.

**Golden Gate:** And the idea that you have specific places where you will calibrate outsource so the specific areas of the accompanying products.

**Golden Gate:** Personas a taxonomy system that would get generated after this preferences for writing sample articles.

**Golden Gate:** Connect Google Search Console and analytics and set up the crawler for the website.

**Golden Gate:** So like those are essentially the things we need to do to set up the context.

**Golden Gate:** All those things will also be accessible through whenever you click on those you sent to like the area where are you going to do that?

**Golden Gate:** So like we'll try to figure out who are the thought leaders in their space automatically.

**Golden Gate:** Then you delete or the confirm of them research sources like what kind of research source matter to them and the tier order nor the things that they should avoid.

**Golden Gate:** So we're going to try to like get as much as we can automatically.

**Golden Gate:** But we need to calibrate this with the whatever the client says and then tone and style.

**Golden Gate:** So this is we have under the hood here there's a spectrum from 10 different traits and as you this is going to be calibrated automatically as well based on their website and based on where we can have access to.

**Golden Gate:** But you can calibrate.

**Golden Gate:** This is cool.

**Golden Gate:** So essentially the whole thing and once you do that ideally we also get if they have example live example content of things that they like, we'll try to get that from.

**Golden Gate:** But from Google Analytics we'd be able to find what are the pages that the guests get the most traffic that are content pages, not like product marketing pages.

**Golden Gate:** So we could populate this and then offerings would also be what are the CTAs that they really care about and when to use and where to point it to.

**Golden Gate:** And if we have those five things plus the company overview the Personas in the taxonomy, we would be able to generate sample articles.

**Golden Gate:** So the sample articles will not be something for them to polish.

**Golden Gate:** It's something for us to get annotation on it.

**Golden Gate:** So it would be essentially, I don't have the UI for this in this computer, but a place where you get an article and it's read only and you just go annotating things very much how we do Check that.

**Golden Gate:** All these things are essentially extracted from.

**Golden Gate:** Check that.

**Golden Gate:** Then we're having pages here, for example, if you go to any of the pages.

**Golden Gate:** So Kavishka and Carrie are doing like they do a deep review and that's not going to be the UI for the, for the os.

**Golden Gate:** The UI for the OS would be labeling things.

**Golden Gate:** It would be like highlighting and defining and so you don't have to paste like Kavisika and Kerry has copy and paste.

**Golden Gate:** So this is the pain.

**Golden Gate:** But you have five types of things that are kind of problems.

**Golden Gate:** You have so research data congestion issues, linking issues, that kind of stuff.

**Golden Gate:** And you have critical, major, minor and general notes.

**Golden Gate:** So the UI for this will be very different on the OS side.

**Golden Gate:** Much simpler.

**Golden Gate:** This is what we could do in just like the time that we just shipped pages with this.

**Golden Gate:** If you do that for one article plus all the structure that we had before, that is enough to do a lot better than most things.

**Golden Gate:** If you do like a couple more times with this.

**Golden Gate:** Good.

**Golden Gate:** And, and that's just during the calibration phase.

**Golden Gate:** And then when you're producing the flow will be similar.

**Golden Gate:** So we can, we can continue to calibrate afterwards.

**Golden Gate:** There's a, there's a data structure for using that data in the, in the workflows.

**Golden Gate:** And the idea will be like to get to the same level of things that we're getting with like check that where CA and carry, like they spend 5 to 10% at most.

**Golden Gate:** The things that they have to do like change things manually.

**Golden Gate:** So if you get to that level, even if it's like a 15% on that, I don't know if it's general purpose means we're going to get to that Same level like 5% to probably higher.

**Golden Gate:** So but we need to measure that.

**Golden Gate:** And so that's what that calibration is supposed to do.

**Golden Gate:** You're going to have a very similar flow when you are in, in the production side.

**Golden Gate:** So this is what the setup area would be.

**Golden Gate:** So the setup would also connect.

**Golden Gate:** So set up.

**Golden Gate:** You have content types.

**Golden Gate:** So content types would be a bunch of predefined instructions for essentially replacement for pipelines.

**Golden Gate:** So your workspace would come in with like 20 different content types.

**Golden Gate:** So you have like the standard definition article, explain an article, list of articles, article where it fits into like the funnel stage, top of the funnel, middle, bottom.

**Golden Gate:** And if it's a awareness versus evaluation, that kind of stuff and how to do each one of those.

**Golden Gate:** So what Kirkland and team would do is just if there's a client that they want a different kind of content type or if they wanted to write things that always has a certain type of TRDR at the end, or if it's a comparison article that compares specific things, they will create new content types for that client only the way this thing works.

**Golden Gate:** But you create content types for pointing them to workflows.

**Golden Gate:** So you point the briefing workflow and you point an execution workflow and it can point to your employer basically.

**Golden Gate:** And as long as they respect the format it would work here analytics analytics providing Google Ga a search console and check that as an analytics provider.

**Golden Gate:** And then the color settings and the CMS settings.

**Golden Gate:** CMS settings would be a bunch of workflows because you essentially there's no way to like automate all workflows.

**Golden Gate:** Like every work.

**Golden Gate:** Sorry cms.

**Golden Gate:** Every CMS is automated slightly different ver so they map different entities and all this stuff.

**Golden Gate:** So I think we always going to have manual work from the client ops engineering team here doing creating workflows for publishing for that client based on that content type.

**Golden Gate:** So that's all the machinery that we do in the first like let's say first week of a client.

**Golden Gate:** Like we just like figuring out which content types we can do what's the calibration for the writing styles.

**Golden Gate:** And that kind of stuff is essentially like automating the writing guideline artifact as much as possible with less before things on it.

**Golden Gate:** Let's assume we do that.

**Golden Gate:** Next thing you're going to do is that you get a portfolio of pages or another thing I forgot to say.

**Golden Gate:** So we have the context, we have brand context.

**Golden Gate:** This is using the old sidebar but this is also cool to project that.

**Golden Gate:** So you have a company overview product product and features.

**Golden Gate:** It would be all.

**Golden Gate:** You can edit anything and this will be like all free form.

**Golden Gate:** And you also have Personas.

**Golden Gate:** So the Personas will be all generated but they are fixed.

**Golden Gate:** So you can select the Personas later on.

**Golden Gate:** So it's not reform a bunch of documents.

**Golden Gate:** And once you have those things we can auto generate the taxonomy.

**Golden Gate:** Every client has a different taxonomy.

**Golden Gate:** So it would be like for certain clients like loveable.

**Golden Gate:** It might be like the pillar and maybe like a few.

**Golden Gate:** Yeah like like engines engine.

**Golden Gate:** We have like group text right.

**Golden Gate:** Like sports team versus whatever.

**Golden Gate:** And then I'll show industry and then by topic cluster, then by content.

**Golden Gate:** Those are the four taxonomies for engine.

**Golden Gate:** Then all their pages are tagged by those four taxonomies.

**Golden Gate:** Right.

**Golden Gate:** In addition to stage of the funnel and an or content or something else.

**Golden Gate:** Right.

**Golden Gate:** So like you can start tagging everything that entire taxonomy.

**Golden Gate:** Yeah.

**Golden Gate:** And then you present the content strategy through the lens of that taxonomy.

**Golden Gate:** That taxonomy is contextually relevant to the brand.

**Golden Gate:** Right.

**Golden Gate:** To the company or the, you know, contextually relevant taxonomy.

**Golden Gate:** So like then once you plug in their website, we scrape the whole thing and auto autocategorize as much as we can.

**Golden Gate:** It's missing the checkboxes, but you would have a way to just like select all the pages, categorize them and then you can cluster them by any of the content, any of the taxonomy things that you created or Persona by creating clusters here.

**Golden Gate:** And the cluster can be combination of things.

**Golden Gate:** So it can be anything from the taxonomy like product X wor.

**Golden Gate:** Wor.

**Golden Gate:** Yeah, like create once, update everywhere on both pages and opportunities.

**Golden Gate:** Yeah.

**Golden Gate:** And at the closer level then you get all the things will be anchored on like metrics.

**Golden Gate:** So we have the health metrics.

**Golden Gate:** Is it getting crawled?

**Golden Gate:** Is it has a bunch of.

**Golden Gate:** Is it getting dexed?

**Golden Gate:** Does it have problems like broken links, that kind of stuff.

**Golden Gate:** Page fee, content quality, impressions and traffic.

**Golden Gate:** And you also have.

**Golden Gate:** So like some clients you're going to have like 20,000 pages here.

**Golden Gate:** So in that case, for example, how do you keep track of the things that are e.g.

**Golden Gate:** not indexed or low health score?

**Golden Gate:** So we have smart views that you have like localized scroll, thin content, stale content, surging, indicating.

**Golden Gate:** And you could select multiple and that decision is filtered.

**Golden Gate:** So filter out things and then if you zoom in then you are like in detail mode.

**Golden Gate:** So you get the og, the open graph.

**Golden Gate:** You have the open graph.

**Golden Gate:** So that's what we can.

**Golden Gate:** It makes a big difference.

**Golden Gate:** For impressions and click through you have some of the things in the taxonomy on the right side here.

**Golden Gate:** In every page we will have the four main entries in an overview one that's essentially a common aggregation.

**Golden Gate:** And we'll run everything through workflows so you can get like a highlight of what's going on.

**Golden Gate:** You get the impressions and traffic.

**Golden Gate:** You also get where the pages in the whole collection of pages.

**Golden Gate:** And then if you go into health then you have health score will be basically a parsing of their pages and some other things.

**Golden Gate:** We already have this working and then we have quality.

**Golden Gate:** Quality is like heavily semantic based.

**Golden Gate:** So that have to tag the page of like the Personas that they care about.

**Golden Gate:** When we're creating new pages, it'll be much easier for existing pages.

**Golden Gate:** It might take like a couple of days to parse all the pages.

**Golden Gate:** We're going to have to analyze every page.

**Golden Gate:** So when setting up your workspace, it'd be like we're categorizing and analyzing the entire website.

**Golden Gate:** If it's a gigantic website, then we might have to choose just part that's not in here, but you have a place where I have to set up the crawler in a certain way.

**Golden Gate:** So there's like a folder that we should monitor or like an area of website that we need to monitor every week.

**Golden Gate:** That's, that's going to be the one that we're going to do first.

**Golden Gate:** So there's like that kind of like structure call it send Rush looks like that.

**Golden Gate:** So if you ever set up like a call instant question.

**Golden Gate:** And then when a client like updates a Persona or adds a new target audience after the fact, after the setup does this auto update, it could do like all the.

**Golden Gate:** Rewrite it.

**Golden Gate:** Yeah.

**Golden Gate:** And like the way we think is that we would really run it to be either additional to not change past things or replace.

**Golden Gate:** Because if you do like manual things, you don't want to replace, you know, so you, you can manually categorize and, and adjust the taxonomic here.

**Golden Gate:** At this point, when will a customer be able to go in and do what he just said versus our team do it for a customer.

**Golden Gate:** Like the way we're thinking is that like we're going to do the UI just for the client is like center and all that.

**Golden Gate:** But that's, that's too much to add to the scope.

**Golden Gate:** So essentially we can just.

**Golden Gate:** We're building.

**Golden Gate:** This is in the clients who have login.

**Golden Gate:** So sorry.

**Golden Gate:** Second, the clients who have login, they can log in.

**Golden Gate:** It's just a pro.

**Golden Gate:** It's complex for them to use.

**Golden Gate:** So they can log in and click metric.

**Golden Gate:** Can I change things and break things?

**Golden Gate:** No.

**Golden Gate:** You should have read only mode.

**Golden Gate:** Yeah.

**Golden Gate:** So read only mode.

**Golden Gate:** So we have two.

**Golden Gate:** I need to remember the permission system.

**Golden Gate:** But we have like three layers.

**Golden Gate:** So there's an operator.

**Golden Gate:** There is a strategic layer that would be like folks that can do.

**Golden Gate:** There's an admin, there's an operator.

**Golden Gate:** Operator cannot change analytics, cannot change critical things and change the cross and.

**Golden Gate:** But they, they will create content, edit the content, annotate things.

**Golden Gate:** And then you have an ad workspace, admin and you have a client that's like upset reload on everything except annotations.

**Golden Gate:** Then you'll have the editor view on here.

**Golden Gate:** Right.

**Golden Gate:** The editor view is going to be the same.

**Golden Gate:** So I'm going to show you so impressions same idea traffic same idea.

**Golden Gate:** And we have content who can have a summary and have them full mark them have activity is there like an.

**Golden Gate:** Exact recording like show me yo gr what have you done for me like transmission.

**Golden Gate:** That's the thing that once we have at a page level doing this would be possible.

**Golden Gate:** I don't know how much of this would be able to do in this.

**Golden Gate:** In this batch where you have every week we generate the executive summary about everything that we touched everything that happened in your website that we didn't like your website in China.

**Golden Gate:** What happened.

**Golden Gate:** You're trying to grow or not Regardless of us touching things or not.

**Golden Gate:** What are the things that we published, what are the opportunities that we found and then what is going up, what is going down.

**Golden Gate:** If we after we track everything at a base level this is not that hard to do but doing at the page But I just don't know if we're going to be able to land.

**Golden Gate:** I'm not going to give UX for this little bit correctly but the meaning that we can do is generate something and the team comes here and edit.

**Golden Gate:** Yeah and they just reach lock their expert PDF.

**Golden Gate:** That is the way I build my reports now.

**Golden Gate:** So run in then I go back and just run edit everything.

**Golden Gate:** Yeah but like having that pre filled is.

**Golden Gate:** You know it's obviously nice pulling from all the context at once and ideally.

**Golden Gate:** Doesn'T share screen well and then additional questions that people have like show me where I rank compared to my competitors or things like that.

**Golden Gate:** That's not.

**Golden Gate:** Is that a thing that you can do or not a thing?

**Golden Gate:** Not a thing ever a thing or just not now a thing?

**Golden Gate:** No, not now.

**Golden Gate:** I think it makes sense.

**Golden Gate:** And then so like the portfolio is very.

**Golden Gate:** That's where you can see.

**Golden Gate:** See like this is essentially the airtable replacement where you have okay like we worked on four pages.

**Golden Gate:** This is our help and all that.

**Golden Gate:** And you also have opportunities.

**Golden Gate:** So opportunities same idea.

**Golden Gate:** You can cluster the same way you can have the views looking things that are relevant to opportunities and you have the research agents.

**Golden Gate:** So the research agents are competitive based domain.

**Golden Gate:** That's where it means do like okay, my competitors rank for all the things and I want to rank that.

**Golden Gate:** It's essentially going to find a bunch of opportunities and remove the ones that are not relevant to your Personas.

**Golden Gate:** You have search engines based on article URL, Persona topics and top players.

**Golden Gate:** This is basically like all the Data that Marcel uses in Sebra and simply my input here.

**Golden Gate:** And essentially here you would have.

**Golden Gate:** Can you use this to like prove a negative?

**Golden Gate:** And what I mean by that is like I was just listening to one of our EMS talk about the fact that they have a customer who's like new industry to the bottom line.

**Golden Gate:** And so they're like, oh, we want to use these keywords.

**Golden Gate:** But like when you go there is like no traffic.

**Golden Gate:** And so it'd be kind of cool to be like let's show you what it would look like and then why we would come up with these to different strategy recommendations.

**Golden Gate:** So yeah, you could.

**Golden Gate:** This version doesn't have the only we have in production that we actually never thought people to use.

**Golden Gate:** This is you can import the CSV so.

**Golden Gate:** So there will be there the.

**Golden Gate:** Essentially it's missing the CSV part.

**Golden Gate:** But you can import a CSV that you would have something like the traffic of.

**Golden Gate:** Of zero.

**Golden Gate:** So like this like the likely traffic here is like the total volume and percentage of the total volume.

**Golden Gate:** So it's 2% of total volume is like probably obtainable traffic.

**Golden Gate:** So if there's a bunch of stuff like.

**Golden Gate:** Like this is a good case that 90 visits and second one visit amount.

**Golden Gate:** Is it worth spending the time?

**Golden Gate:** Probably not.

**Golden Gate:** So I think we have the same year.

**Golden Gate:** So when you see like likely traffic it's the same idea.

**Golden Gate:** So you would see like load of volume difficulty.

**Golden Gate:** So you load something like if you load like a.

**Golden Gate:** Like we're using like check that as a client here and we load all the AO related things.

**Golden Gate:** There are no search.

**Golden Gate:** So what we had to do is just like okay, like what are these people looking for?

**Golden Gate:** Raise price, alternative to have st.

**Golden Gate:** So we had to go out of the Persona, come up with a new Persona.

**Golden Gate:** So that's something that all of the things.

**Golden Gate:** I think it will work pretty well in an established space.

**Golden Gate:** So the outer generation of the Personas, if they have a good website, the problems you get right.

**Golden Gate:** But it's.

**Golden Gate:** If it's a new client, it's a new space.

**Golden Gate:** They have to do a lot of massaging on the who are actually the Persona that they care about.

**Golden Gate:** So check that the person would be like marketers interested in ao.

**Golden Gate:** It's not enough of them to create content for that.

**Golden Gate:** So we went with like buyer's guide.

**Golden Gate:** It's not the buyer Persona that's we were creating content for.

**Golden Gate:** So the context area we have to calibrate for this unique Persona just for this.

**Golden Gate:** I don't, I don't know what you Guys think I was just another customer review and the CEO is kind of like what are you guys doing?

**Golden Gate:** I don't get it.

**Golden Gate:** And some of it seems been checked out and is coming back in.

**Golden Gate:** And I think the strategy is there.

**Golden Gate:** But I just see this actually being like a stakeholder buying mechanism of like if you show scenario it's like well we're doing the reason, let's show you.

**Golden Gate:** But we're doing this for the scenario.

**Golden Gate:** If we did the other thing we think it would do that.

**Golden Gate:** Like do you see it being used like that?

**Golden Gate:** I think so, yeah.

**Golden Gate:** That's the thing that these are opportunities for new pages.

**Golden Gate:** Ideally it'd be like the same.

**Golden Gate:** So we do with airtake when team can do it well long term is just go through this with the clients and this is the things that we're working on.

**Golden Gate:** And that's the reason why like when I was working with both they really wanted to know like why why are we doing this portfolio and catalogs and things like this Persona and what's the bet.

**Golden Gate:** So we had to come to templates and I wanted to create.

**Golden Gate:** So but we were essentially demoing this to the to the team backed by this and backed by this.

**Golden Gate:** So like sort by like what are the easy ones accept them and then they go into the work here.

**Golden Gate:** And the work here is essentially the check that version is kind of not the ideal one.

**Golden Gate:** But sure it's the same system with for the workflows.

**Golden Gate:** So check that when you're creating a page this already went to the work queue.

**Golden Gate:** But if I go to a new page creating forms.

**Golden Gate:** So it would look better than this.

**Golden Gate:** But when you're in the workflow you have content clusters the same way or whatever cluster that you want to pick from the ones that you define before.

**Golden Gate:** So you group them so you can see how many you're working on at a time.

**Golden Gate:** You have backlog, briefing, writing review and rank.

**Golden Gate:** The ones that are in briefing will be the equivalent of this.

**Golden Gate:** So you have the search intent.

**Golden Gate:** Instead of this would be the drop down of the Persona.

**Golden Gate:** Instead of this would be there but there would also be I think for the opportunity so actually have to.

**Golden Gate:** So it would be the screen would be closer to this where you have the opportunity came from.

**Golden Gate:** When you're in brief you have the title for the essentially the work the Persona that you want to choose the primary keyword and the overall direction that we want to give.

**Golden Gate:** And then you get the outline.

**Golden Gate:** The outline format will be this.

**Golden Gate:** This is the one that we validated that works well so you have square brackets, you have H2s, H3s and pre baked all the things from the writing guidelines that came from, from the calibration.

**Golden Gate:** And this is the pipeline under the hood here.

**Golden Gate:** The content type has the brief agent, it has the execution agent.

**Golden Gate:** So the brief agent is set up to output this for all the pricing pages on alternative pages.

**Golden Gate:** It's essentially only this kind of outline.

**Golden Gate:** So the client is doing that stuff or there's accepting the opportunity and then it's automatically doing that and then it's populating the outline.

**Golden Gate:** Yeah, like what you in v0.

**Golden Gate:** That's the thing that we have to decide like I don't think the clients.

**Golden Gate:** Whatever our end needs were.

**Golden Gate:** Yeah, the end needs will be.

**Golden Gate:** So this is the, the job like to me like the client.

**Golden Gate:** The dog footing process that we're following here is Marcel is the CMO of check that he came up with four ideas of continents.

**Golden Gate:** Can we create four content types that do well And Kavishka and Kerry are.

**Golden Gate:** And they've been.

**Golden Gate:** They cranked out 600 pages in the last month with 5% of the pace the only ones you had to change.

**Golden Gate:** And we got a million impressions in one 20 clicks per day.

**Golden Gate:** So that's the, the thing that I think the clients would be interested in is just like how much work did you do?

**Golden Gate:** What are the opportunities that you picked and why?

**Golden Gate:** And actually those tables have clustering and the numbers around.

**Golden Gate:** So you can like okay, we're doing this for clusters.

**Golden Gate:** We're betting that those four make sense and we're tracking impressions and analytics.

**Golden Gate:** So you can say okay, like we did 200 pages out of the 200, like 1/4 is getting in this cluster, 1/4 is getting impressions but not click twos.

**Golden Gate:** So now the work is improving meta tags.

**Golden Gate:** So if you question it as like how does this practically show up in contracts?

**Golden Gate:** Like it's not like five blogs a week anymore.

**Golden Gate:** Right.

**Golden Gate:** And so what, what is it?

**Golden Gate:** No, I'm not sure like what's the kind of state.

**Golden Gate:** And then something back and forth.

**Golden Gate:** Many times it was not update.

**Golden Gate:** I think now it's got a number of pages based on the Fed script what they want to do.

**Golden Gate:** And we have a gap of like editorial.

**Golden Gate:** There's an editorial package, there's a programmatic package.

**Golden Gate:** And if you can't be programmatic it might be a thousand pages.

**Golden Gate:** Focus on.

**Golden Gate:** It's more about like there is an opportunity for me and the editor has a, has a.

**Golden Gate:** Who can decide what's the size during this phase.

**Golden Gate:** And Ada and William And George just this is me, my inexperience asking her if one of our major issues we run into date is client's ability to review or on things and all of a sudden we're able to do 50, you know, like we're five.

**Golden Gate:** What's your.

**Golden Gate:** What's your how.

**Golden Gate:** Tell me about the customer experience here and the interaction with them and what you think this flow would look like.

**Golden Gate:** What do we need to prepare for to make this.

**Golden Gate:** I mean out of all the clients that I've worked with at Growth X Web Stacks would be basically the only one who was comfortable with us publishing without them reviewing the company content.

**Golden Gate:** Like we have like a couple more.

**Golden Gate:** Now, but yeah, yeah, but it's a smaller percentage like they, everybody wants to.

**Golden Gate:** And now we're even getting more clients.

**Golden Gate:** Like as we're getting into like more established companies, like we're getting into people who are saying like we want our.

**Golden Gate:** Product to review everything.

**Golden Gate:** So that's massive.

**Golden Gate:** Legal is common legal as well.

**Golden Gate:** Yeah.

**Golden Gate:** So I guess like what, what does a review queue look like?

**Golden Gate:** Yeah.

**Golden Gate:** So that's the thing that our original plan was that we're gonna gate everything and the client would see nothing other than insights and the review.

**Golden Gate:** And that might be the ideal flow.

**Golden Gate:** This might be too much for the client to click around but I think like for March we can see if they would be like, oh, just visit this link every day.

**Golden Gate:** That's the one I don't have.

**Golden Gate:** But it will be essentially like this where you would have, you have a CMS there, you can annotate the problems.

**Golden Gate:** You can.

**Golden Gate:** It will be a two step process.

**Golden Gate:** It's this.

**Golden Gate:** So you have a read only mode, you have the meta tags, you can change whatever you want and then the main things that you go into view mode and you would do a better version of what the team has to prepare today so that finally we're going to be editing things.

**Golden Gate:** My head coaches like, I don't like this, I don't like that, please don't have that.

**Golden Gate:** And there's like a bar that's like apply and we'll rewrite the whole article.

**Golden Gate:** But as they do that we're collecting the data and recalibrating all their preferences and storing all the things that they don't like.

**Golden Gate:** I mean the source that are problematic.

**Golden Gate:** So that's why I have this five things here.

**Golden Gate:** So as they do this we will be automatically like, okay, we need to recognize is there a worse log that like an ME can review on the updates that the system is making?

**Golden Gate:** To the contextual documents we don't have in this scope.

**Golden Gate:** But it's going to be stored in the database.

**Golden Gate:** Yeah, yeah.

**Golden Gate:** Like that's like we do have this.

**Golden Gate:** So we could have.

**Golden Gate:** Because like here's the thing, it makes an adjustment.

**Golden Gate:** The system says, cool, we're going to apply that feedback in X way and that produces maybe an unintended result.

**Golden Gate:** Yeah.

**Golden Gate:** Then it's like just like any, any incidental report, you know, you'd want to like.

**Golden Gate:** Yeah.

**Golden Gate:** Be able to track back.

**Golden Gate:** Yeah.

**Golden Gate:** Ideally we track both DME and the client.

**Golden Gate:** So like somebody reviewed here.

**Golden Gate:** So we have the activity log.

**Golden Gate:** Yeah.

**Golden Gate:** At the page level.

**Golden Gate:** And we'll be able to like the pages dropping traffic or impressions after we change something.

**Golden Gate:** Can we feed that to the floor?

**Golden Gate:** Nice.

**Golden Gate:** Probably not going to be always active, but at least be like, okay, things are changing.

**Golden Gate:** This page traffic nowhere going up.

**Golden Gate:** Well, I mean that also feeds our institutional knowledge.

**Golden Gate:** Right.

**Golden Gate:** It's like, hey, we changed this traffic went up.

**Golden Gate:** We should apply that learning across the model rather than being isolated to this one wing for one client in one organ.

**Golden Gate:** Yeah, yeah.

**Golden Gate:** So I think we're trying to do here as well as it's a GOX level, like ontology of things that we care about that we need to monitor for every client.

**Golden Gate:** And then there's a difference at the client level here.

**Golden Gate:** So the annotation at the calibration PA is to create the strap version of this.

**Golden Gate:** And as they annotate a means for the client, we get to the point where the client said, okay, like you guys have a thousand opportunities.

**Golden Gate:** We're doing like 50 a week and my annotations are getting taken consideration.

**Golden Gate:** They probably not going to review everything every time.

**Golden Gate:** So then they can just.

**Golden Gate:** Essentially it's calibrating that we're not using it in the data.

**Golden Gate:** We'll very likely not have something that we work with version.

**Golden Gate:** But we're trying to figure out the reinforcing learning loop and all that.

**Golden Gate:** Yeah, but what you just explained was like a future state.

**Golden Gate:** Like no one in Strategy Spur right Now is doing 50, 50 articles per week.

**Golden Gate:** And so like they'd be more custom.

**Golden Gate:** 1, 2, 3.

**Golden Gate:** And then getting up to five articles per week where they're like more manually in the review.

**Golden Gate:** I think like ideally we would be able to like say we publish this.

**Golden Gate:** So we would go into pages and here's all the pages we published.

**Golden Gate:** Here's the traffic that we're getting and here's.

**Golden Gate:** Here's the impression that we get.

**Golden Gate:** So we should anchor the conversation, like correct does over two.

**Golden Gate:** I think everything that we published.

**Golden Gate:** Here's the cluster level impressions, traffic.

**Golden Gate:** Here's the only consideration I have again to get.

**Golden Gate:** Like you guys tell me if it shouldn't be a consideration.

**Golden Gate:** I'd say 99.99 of our customers are Marcel and way down on the adoption curve of it.

**Golden Gate:** I mean, they're obviously interested is why they're engaging core effects, but the amount of giving up of control.

**Golden Gate:** Yeah.

**Golden Gate:** To do this, you know, it's humans that buy the product.

**Golden Gate:** And so humans feel like they have just like lost their job and like, we have to find a path.

**Golden Gate:** Yeah.

**Golden Gate:** I think like the Superhuman case is a good example.

**Golden Gate:** So I think there are two.

**Golden Gate:** Two types of clients.

**Golden Gate:** There's a client that will be like, oh, after a certain point, like everybody, like, you guys do it every morning.

**Golden Gate:** And then you have clients like Superhuman where they will be like, I want to write.

**Golden Gate:** Yeah, maybe like, help me come up with the cluster.

**Golden Gate:** Help me come up with the writing agent and help me find opportunities.

**Golden Gate:** Finding opportunities.

**Golden Gate:** Every day I want to write myself.

**Golden Gate:** And then, then that's why we're thinking like, we don't get the client.

**Golden Gate:** Let them do.

**Golden Gate:** We can just add a client here that's an operator.

**Golden Gate:** We just switch their checkbox to be operator as well.

**Golden Gate:** And we teach their team that.

**Golden Gate:** You go in the screen here and you do this yourself, you know, and the line added everything you want here if you want to.

**Golden Gate:** So that would be an option.

**Golden Gate:** Or don't use this.

**Golden Gate:** Use just the opportunity there and download this and go different.

**Golden Gate:** Your cms.

**Golden Gate:** I would say the one like, I don't know how it fits into this feedback loop or some larger, like reinforcement of accuracy here, but if I had to characterize the issues that people had, I think obviously 30 or 40% of it's stylistic, which this seems to take well into account.

**Golden Gate:** Oh, I'm going to change this stylistically to match more what I'd like.

**Golden Gate:** Great.

**Golden Gate:** We're going to learn from that.

**Golden Gate:** The very next thing you see from us will have that integrated automatically, which is amazing.

**Golden Gate:** However, the other 60% is factual.

**Golden Gate:** Yeah.

**Golden Gate:** Like broken links, factual errors, many of them related to their.

**Golden Gate:** Either their product or their industry.

**Golden Gate:** Right.

**Golden Gate:** And of course, that's where legal review or product team or technical teams reviewing will come in.

**Golden Gate:** And so is there like.

**Golden Gate:** Like, how are we thinking about the reinforcement loop?

**Golden Gate:** The knowledge base being built over time to understand their product, their taxonomies, their definitions of things, which we've all seen.

**Golden Gate:** Like, LLMs are going to hew to the broader definition.

**Golden Gate:** Yeah, but they have a very specific definition that maybe differentiates in some subtle way.

**Golden Gate:** Yeah, the ideal.

**Golden Gate:** I don't know if we're going to be able to do this cycle but what is going to collect all this data.

**Golden Gate:** Yeah.

**Golden Gate:** So that's the thing with like check that.

**Golden Gate:** So check that.

**Golden Gate:** Kavishka and Carry annotated the out of everything.

**Golden Gate:** So like in the first week I'm like, okay, like I can see exactly where the problems are and customize the research agent for that client manually.

**Golden Gate:** So like I did that manually a couple of times now.

**Golden Gate:** They don't change anything anymore on both the TOC and the content most of the time.

**Golden Gate:** But I think this will vary quite a bit client by client.

**Golden Gate:** And I don't know how much of this we're going to be able to automate.

**Golden Gate:** Like I don't know what's going to look like for the purpose team.

**Golden Gate:** Yeah.

**Golden Gate:** But at least they will have a data set.

**Golden Gate:** Yeah.

**Golden Gate:** Like you're never going to forget the comments.

**Golden Gate:** And you can reverse that into like the.

**Golden Gate:** Check the proofreader checklist for the, for the post processing or the things for the sources for the researchers.

**Golden Gate:** Many things that you can do that will be input for the agents but later on ideally that will be like automatically so you don't have to do the manual work.

**Golden Gate:** Yeah but I don't think you can do that.

**Golden Gate:** I mean at the very least you have a capture mechanism for a technical team of you.

**Golden Gate:** Yeah.

**Golden Gate:** As an example.

**Golden Gate:** So like hey, here's three pieces of content.

**Golden Gate:** Take your engineers very valuable time and you know, have them review these pieces and then we can take that factual.

**Golden Gate:** We have this, we have total number of pages published deep review that they've done in the last 30 days and you have the kind of issues that they flex and then from the critical major.

**Golden Gate:** Download this and then I can massage all the inputs for the, for the agents.

**Golden Gate:** Just really quickly.

**Golden Gate:** Sydney's still on the call.

**Golden Gate:** I'm not sure if she's needed here.

**Golden Gate:** I was thinking just maybe mindful of the time zone.

**Golden Gate:** Yeah, that's fair.

**Golden Gate:** Thank you.

**Golden Gate:** So maybe you, if you have other things to do and go back to bed.

**Golden Gate:** I will see you tomorrow.

**Golden Gate:** I got a question about this.

**Golden Gate:** Thank you.

**Golden Gate:** Supposed to get, you know, launched and share it out.

**Golden Gate:** How's that?

**Golden Gate:** How do you see the sprint changing?

**Golden Gate:** Yeah, that's the, that's the thing that we're going to have to test it out.

**Golden Gate:** Yeah.

**Golden Gate:** As in like how close can we get to generating this in a way that we feel like it's pretty good.

**Golden Gate:** As in, like, yeah, this is all self serve.

**Golden Gate:** This is them doing their own onboarding on kickoff, basically.

**Golden Gate:** Right.

**Golden Gate:** I mean that, that's.

**Golden Gate:** So that's why I'm so curious.

**Golden Gate:** When I'm seeing this full experience, I'm like, okay, well that completely transforms the idea of the Sprint.

**Golden Gate:** Maybe there's still some clients where we would do very white glove service and stay with them for eight weeks and work through it, but probably a big portion of them wouldn't.

**Golden Gate:** They would just go through this soft serve experience.

**Golden Gate:** Yeah, I think we would have to do that for them.

**Golden Gate:** This feels like work, you know, like, and I don't think they would do it or I don't think they'd still be on a call.

**Golden Gate:** You'd be like, okay, so what do you think of this timeline?

**Golden Gate:** Yeah, I think would be like more like, hey, Adrian, this, I thought about this, this and this.

**Golden Gate:** Does anything stand out to you immediately?

**Golden Gate:** Like, am I completely off here?

**Golden Gate:** Am I completely off here?

**Golden Gate:** Am I completely off on your offerings?

**Golden Gate:** That's the things that we got from the call, the call transcript, the documents you sent me and crawling your website.

**Golden Gate:** So that would be like one.

**Golden Gate:** And then like after they do that, say, okay, I measure three sample articles and I will send it to you and the client will interact on this.

**Golden Gate:** Ideally.

**Golden Gate:** Or if they're doing something that you have done enough experience already, like if we have the user in the team and we're doing clerk, we don't have to give the client to do this.

**Golden Gate:** It could just have them use it to annotate all 3D particles and then generate again.

**Golden Gate:** The articles are going to look good to the client and that will recalibrate the whole thing.

**Golden Gate:** So it will definitely change how we do the calibration of articles and stuff like this.

**Golden Gate:** The other thing, we have to really have to do that.

**Golden Gate:** Once we have the Personas, we're gonna have to do this.

**Golden Gate:** So figure out their taxonomy, figure out their Personas, and figure out their product that you review.

**Golden Gate:** Once you have that, the next thing is to generate a bunch of opportunities and see if the opportunities that are aligned.

**Golden Gate:** So I think it's going to be more time spent in like, are the opportunities looking good?

**Golden Gate:** Am I clustering your pages correctly?

**Golden Gate:** Are the pages that I'm thinking about grouped in the right way?

**Golden Gate:** Let's say like AirByte, for example.

**Golden Gate:** AirByte has like thousands of pages about connectors.

**Golden Gate:** They have thousands of pages about all the things too.

**Golden Gate:** They all have problems as if they are outdated.

**Golden Gate:** Which ones you want me to.

**Golden Gate:** If I wanted to optimize it, which ones you want me to take a look?

**Golden Gate:** So if we're going to do an audit, like, when we do the audit, we'll be able to just like low ball.

**Golden Gate:** The baiting is like, hey, they're categorized this way.

**Golden Gate:** Does it look right?

**Golden Gate:** So.

**Golden Gate:** So, William, and let's just say in three weeks, you got a Sprint customer coming through and you're walking through this.

**Golden Gate:** What needs to be true for you to manage that experience?

**Golden Gate:** Yeah, everything you just showed us was operational.

**Golden Gate:** I mean, what needs to be true?

**Golden Gate:** I guess just broadly speaking, my reaction to this is like, this is a cleaner experience than what we're currently doing where we're jumping around airtable and we're doing this and we're showing them bits.

**Golden Gate:** So I don't know, there's nothing specific that needs to be true other than that this needs to work.

**Golden Gate:** Right.

**Golden Gate:** Like when I get the one, does.

**Golden Gate:** Anything change around this?

**Golden Gate:** Are there any customer hurdles?

**Golden Gate:** That changes everything.

**Golden Gate:** Yeah, yeah, it changes everything.

**Golden Gate:** Because if this is operational, then the speed, I don't even think we need eight weeks.

**Golden Gate:** I think we reduce it down to like three or four weeks and get them to that space faster.

**Golden Gate:** Yeah, that's what comes to mind for me.

**Golden Gate:** But what doesn't change is needing to download the context that they already have in the kickoff or whatever that experience is.

**Golden Gate:** Like when we make first impression to get all these inputs right with them, because we can do a bunch of research outside of it, but they'll always have materials that they share and different ideas and different priorities.

**Golden Gate:** And so being able to incorporate that into the setup and show them how.

**Golden Gate:** I think the one thing that maybe changes if I think about it is like, humans like to talk to humans.

**Golden Gate:** Right?

**Golden Gate:** So like the clients like to be able to say, okay, I look at this article and they put feedback in the comments, the Google Doc, but then they want to talk about it and they want to explain what they're seeing, broadly speaking.

**Golden Gate:** And I think that we just need to figure out how to do that.

**Golden Gate:** Right.

**Golden Gate:** Because in a way, what you were saying is we're disconnecting the human to human.

**Golden Gate:** We're saying, just put it in here and the system will learn.

**Golden Gate:** But sometimes the system can't know the thoughts.

**Golden Gate:** And it's in the conversation that I'm having with the client that the subsidy comes in.

**Golden Gate:** And then I translate that information from the managing editor.

**Golden Gate:** And the managing editor uses critical thinking to be like, okay, now this is how I need to change the pipeline that's maybe the disconnect.

**Golden Gate:** Yeah, that's the.

**Golden Gate:** Like I think like ideally we would do the work and then walk the client through.

**Golden Gate:** Like here's how we did the calibration of your.

**Golden Gate:** Like, here's the tooling that we're using.

**Golden Gate:** How we.

**Golden Gate:** Here's the framework that we use that's baked into our tool for how we think about calibration.

**Golden Gate:** Partnership in your space, the articles you care about, your research providers and then the sample article.

**Golden Gate:** It's not in the UI in this thing that I have working, but the same particle you have the annotation.

**Golden Gate:** You could do the annotation with that.

**Golden Gate:** Like in the call.

**Golden Gate:** You could.

**Golden Gate:** Okay, let's walk through together.

**Golden Gate:** What do you think about this?

**Golden Gate:** That's.

**Golden Gate:** And then you do the annotation and you select things and at the bottom it will have like a text area that you could just like press the whisper sing for something you.

**Golden Gate:** It's like tell me what.

**Golden Gate:** How did we do this and what did I get wrong At a high level.

**Golden Gate:** Okay, that's pretty cool.

**Golden Gate:** So like it would be walking the client through the calibration.

**Golden Gate:** That would be one way.

**Golden Gate:** And if you have a client that's like more hands off.

**Golden Gate:** Like I've been called sales.

**Golden Gate:** Yeah, we do everything just like hey, one call.

**Golden Gate:** Like there's everything we did.

**Golden Gate:** Because all the opportunities can I choose.

**Golden Gate:** Do you see for every customer?

**Golden Gate:** Like when thinking about the transcription of.

**Golden Gate:** The role.

**Golden Gate:** It feels like the heightened ability for the team to be strategic and be able to talk about emerging trends and like know their business and make sure, you know, like I should have like a strategic advisory about how to use the tool.

**Golden Gate:** So it's like really like more business acumen versus you know, and like how do you translate it into the tool versus the other stuff?

**Golden Gate:** Is that.

**Golden Gate:** Do you feel like that's an accurate transformation?

**Golden Gate:** Like where the weight of the.

**Golden Gate:** That would be the ideal.

**Golden Gate:** That's something that I don't think we are ever going to get.

**Golden Gate:** Not ever.

**Golden Gate:** But this is obviously too hard for somebody to use.

**Golden Gate:** Maybe not.

**Golden Gate:** But without training, maybe like we would do like a few polishing.

**Golden Gate:** It's definitely easier than Air ops.

**Golden Gate:** Oh, I can use this.

**Golden Gate:** I've been saying better than air Ops.

**Golden Gate:** Because I was a client of theirs that if I always like comparing the two experiences.

**Golden Gate:** What I'm really trying to get at is Air Ops and things like it like NH10 and some of these other tools are prohibitively difficult.

**Golden Gate:** But.

**Golden Gate:** But people in High Wall still try to use it.

**Golden Gate:** We still, we still do the best that we can to try and use it.

**Golden Gate:** So this is like miles and a user experience.

**Golden Gate:** Could somebody with the patience and desire, but also the content and SEO experience use this?

**Golden Gate:** Yes.

**Golden Gate:** Like, I think if they have like a writing internal writing team.

**Golden Gate:** That's the case of Grammarly.

**Golden Gate:** Right now that they bought Super Dunion.

**Golden Gate:** Yeah.

**Golden Gate:** They want to write themselves, then we can teach them how to use.

**Golden Gate:** Totally.

**Golden Gate:** Even if it's one guy.

**Golden Gate:** It was Jonathan Brett's.

**Golden Gate:** He would use this.

**Golden Gate:** Yeah, he's different.

**Golden Gate:** Use yourself.

**Golden Gate:** Yeah, yeah.

**Golden Gate:** What about the me is what needs to be true for them?

**Golden Gate:** I don't think it would be difficult for them to use, I think training they could get up to get up to speed because they were using Air Ops before.

**Golden Gate:** And again, they're annotators.

**Golden Gate:** Right.

**Golden Gate:** They're not like, yeah, writing.

**Golden Gate:** Oh, yeah, exactly.

**Golden Gate:** They need to have a good sense of what good looks like.

**Golden Gate:** I need to really need to know what quality content is because, I mean, it's basically the same.

**Golden Gate:** Like now they're exporting stuff, you know, from Atlas that they've edited and they might like in the Sprint, they'll send it to Sydney and then Sydney will detect things that they did not detect when they were reading and reviewing the process of the article.

**Golden Gate:** So there's a level there that, you know, we need to.

**Golden Gate:** Escalation, essentially.

**Golden Gate:** If somebody has a contrary.

**Golden Gate:** Escalates to somebody.

**Golden Gate:** That's.

**Golden Gate:** Yeah.

**Golden Gate:** That's why I love that funding audit pipeline Atlas, because it's like if somebody's like, hey, okay, I think I got this edited.

**Golden Gate:** I run through it and it basically puts my editorial rubric against it.

**Golden Gate:** It's like, hey, you missed seven things.

**Golden Gate:** You know, and those seven things aren't really like, oh, that trouble.

**Golden Gate:** It's not about that.

**Golden Gate:** It's like, hey, stylistically speaking, you've missed a trick here.

**Golden Gate:** Like, there's just lack of a transition between these two sections.

**Golden Gate:** There's things like that.

**Golden Gate:** And so like, I think building something like that into there, where it's like, oh, you're in training mode.

**Golden Gate:** You're gonna get feedback.

**Golden Gate:** Like, you're gonna make your edits and then you're gonna get feedback from the system.

**Golden Gate:** Yeah, I can clearly see that path.

**Golden Gate:** But I were thinking about that in the UI how to do layer.

**Golden Gate:** But after you do the annotation.

**Golden Gate:** Yeah, there would be a free form.

**Golden Gate:** So people could free form.

**Golden Gate:** Right.

**Golden Gate:** That's my ideal.

**Golden Gate:** Because essentially that you're changing again on that.

**Golden Gate:** Right.

**Golden Gate:** But like, that was the one thing that would going to be annotation only.

**Golden Gate:** But is it going to actually work all the time?

**Golden Gate:** Unfortunately in the real world clients have some crazy hyperspecific stuff then like you could prompt all day or you could just change the sentence and ship, you know.

**Golden Gate:** So I think that's the direction that we want.

**Golden Gate:** We had four hours discussion in the morning structure.

**Golden Gate:** Just to get in there.

**Golden Gate:** It's not always but I also need to get the guys doing this asap.

**Golden Gate:** So what I'm going to get to work on is essentially the crawler and collecting all the metrics and give you all the proposals until we figure out the ui.

**Golden Gate:** So.

**Golden Gate:** So even the setup like what George was just saying we want to have baking here and like I said faces and they're like we get a.

**Golden Gate:** That a data set like a bunch of conf.

**Golden Gate:** From them.

**Golden Gate:** You dump that into here and then generate.

**Golden Gate:** It's not just crawling your website there you put first crawl.

**Golden Gate:** Yes.

**Golden Gate:** And then you get the whole thing and then.

**Golden Gate:** And then we review them.

**Golden Gate:** But I think a lot of our job switch to be like sharing with them.

**Golden Gate:** So I think this is where we getting input and.

**Golden Gate:** And if the system can take it then we figure out how to make it.

**Golden Gate:** So that's the part that I think we're going to be operating with them sharing screen now and if they want to log in we should encourage them to log in.

**Golden Gate:** And even if they want to annotate, I mean we annotate until we have.

**Golden Gate:** That's who we're thinking.

**Golden Gate:** What are your reactions on the experience like Ada you think you're looking a little longer.

**Golden Gate:** I would love to get into it.

**Golden Gate:** I would love to like at this point of time as I'm building just trying to sort of climb the way that we're now doing it.

**Golden Gate:** I would love to be able to put it cloud here.

**Golden Gate:** Yeah, I would love that too because then I think we'll like we'll kind of work around the edges of the.

**Golden Gate:** What needs to be true.

**Golden Gate:** That's what I mean that that's to me should be the milestone for first week of March at the latest is to get like.

**Golden Gate:** It's just that like we're trying to.

**Golden Gate:** Use it in parallel.

**Golden Gate:** In parallel, yeah.

**Golden Gate:** And specifically though on the opportunities I think that part you don't need to.

**Golden Gate:** There's no way this could be this like it's like right now it's just like.

**Golden Gate:** A nightmare.

**Golden Gate:** And then keeping the context through a building strategy.

**Golden Gate:** Keeping the context context feed and the calibration piece I think could be done parallel like.

**Golden Gate:** And so we validate that.

**Golden Gate:** It's, like, better, you know?

**Golden Gate:** Yeah, right.

**Golden Gate:** Reason.

**Golden Gate:** Yeah.

**Golden Gate:** Why are you still here?

**Golden Gate:** Go to the, you know, like, the dead plaza.

**Golden Gate:** So if I have, like, down where I think this is going to buy the most deeds, obviously.
