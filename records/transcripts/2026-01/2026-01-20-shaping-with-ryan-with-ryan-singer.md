# Shaping with Ryan with Ryan Singer

<metadata>
date: 2026-01-20
time: 17:06 UTC
duration: 171 minutes
organizer: daniel@growthxlabs.com
participants: Daniel Lopes (GrowthX, CTO & Co-Founder), Marcel Santilli (GrowthX, CEO & Co-Founder), Ryan Singer (Product Strategy Advisor)
fathom_recording_id: 115652257
fathom_url: https://fathom.video/calls/537065394
share_url: https://fathom.video/share/QNyY-5b2Kbx9-33-DKGnJoacN1LERyok
source: fathom
enriched_on: 2026-02-28 17:00 UTC
</metadata>

---

## Summary

Marcel and Daniel met with Ryan Singer to reshape CheckThat's product strategy and address critical UI/UX gaps. The core insight: clients are "flying blind" on website performance because current dashboards fail to connect strategic opportunities with actual performance outcomes. The solution centers on making the **page** the unit of analysis, connecting opportunity identification, task assignment, and performance evaluation into a unified workflow.

---

## Context

This session was part of GrowthX's ongoing engagement with Ryan Singer on product strategy and the "Shaping" methodology. The meeting addressed urgent retention challenges—current operational-only client updates fail to demonstrate ROI, leading to churn. The team sought to reframe CheckThat from a data dashboard into a proactive, page-centric performance tool that proves value through rapid iteration and visible results.

---

## Relevance

**Product Strategy**
- Central unit of analysis shifts from dashboard metrics to individual pages
- "CRM for pages" model connects Opportunities → Assignments → Performance
- "Map at the Mall" UI pattern replaces fragmented tab-based navigation

**Business Impact**
- Addresses client churn caused by opaque reporting and lack of ROI proof
- Case studies show success when clients push for performance data (Lovable: $40k/mo)
- Failure mode identified: missed signals on high-performing pages (Ambient AI)
- Goal: deploy MVP in ~6 weeks to demonstrate retention value

**Technical Execution**
- Backend data pipeline for page signals (health, quality, visibility, traffic, engagement, conversion)
- Two critical UI views: per-page diagnosis and aggregate portfolio ROI
- Strategic clustering by content type/topic to identify working strategies

**Next Steps**
- Marcel to confirm availability for Feb 4 follow-up meeting
- Pause current analytics feature work; refocus on page-centric UI/UX
- Continue backend data pipeline development
- Refine UI strategy based on Map at the Mall model

---

## Overview & Key Topics

### The Problem: "Flying Blind" on Website Performance

- Clients lack visibility into website performance, relying on agencies for opaque updates.
- **Current GrowthX Workflow:**
  1. **Audit:** One-time SEMrush/Airtable snapshot identifies content gaps.
  2. **Work:** New pages are published based on audit.
  3. **Reporting:** Looker dashboard from GA (on-site behavior) and GSC (search visibility), but often ignored or broken.
- **Case Study: Lovable (Success)**
  - $25k/mo engagement grew to $40k/mo after client pushed for performance visibility.
  - Looker dashboard demonstrated clear ROI: 150 signups, ~$50k ARR in 4 months.
  - Flaw: Process was reactive, not proactive—success depended on client initiative.
- **Case Study: Ambient AI (Failure Mode)**
  - High-performing engagement with two top-performing pages driving 80% of traffic.
  - Pages began to decay but team missed the signal, continued publishing new content instead of fixing.
  - Result: Performance flattened and declined, leading to churn risk.

### The Solution: A "CRM for Pages"

- The **page** is the central unit connecting all parts of the content lifecycle.
- **Page Analytics Model:** Structured framework for evaluating each page:
  - **Health:** Technical vitals (speed, indexability).
  - **Quality:** Content relevance and depth.
  - **Visibility:** Impressions from search and AI.
  - **Traffic:** Inbound visits.
  - **Engagement:** On-page behavior (time on page, scroll depth).
  - **Conversion:** Progress toward business goals.
- **Two Critical Views:**
  - **Per-Page View:** For operators to diagnose issues and prioritize work.
  - **Aggregate Portfolio View:** For stakeholders to see high-level ROI and justify renewals.

### The UI Strategy: "Map at the Mall"

- The UI must reflect the core workflow, not just be a collection of tabs.
- **Core Workflow:** Opportunities (Hypotheses) → Assignments (Work) → Pages (Output) → Evaluation (Performance).
- **Proposed UI Structure:**
  - **Primary Navigation:** Global header with sections for `Opportunities`, `Assignments`, and `Performance`.
  - **`Performance` View:** Master-detail table of pages with key metrics.
    - Clicking a page opens a detail pane with the full analytics model.
    - Action buttons (e.g., `Create Opportunity`) enable immediate action from insights.
  - **Strategic Grouping:** The `Performance` view must support grouping by **Clusters** (topic, content type).
    - Clusters are the strategic unit, enabling users to see which content strategies are working and double down.

---

## Action Items

- **Marcel Santilli (GrowthX, CEO & Co-Founder):** Confirm availability for additional meeting on Feb 4 to accelerate progress
- **Daniel Lopes (GrowthX, CTO & Co-Founder):** Pause work on current analytics feature; focus on new page-centric direction
- **Daniel Lopes (GrowthX, CTO & Co-Founder):** Continue building backend data pipeline for page signals
- **Daniel Lopes (GrowthX, CTO & Co-Founder):** Refine UI/UX strategy based on "Map at the Mall" model

---

## Transcript

**Marcel Santilli** [00:00:00]
Today, you can prioritize all these things.

**Marcel Santilli** [00:00:02]
You can even do some of the work, but you need to actually have outputs, right?

**Marcel Santilli** [00:00:06]
And the outputs are either the destination is the website, and the outputs, a website is made out of pages, obviously.

**Marcel Santilli** [00:00:13]
And so the output is changes to pages or creating new pages.

**Ryan Singer** [00:00:17]
That's it.

**Marcel Santilli** [00:00:18]
That's simple, right?

**Marcel Santilli** [00:00:19]
But then...

**Ryan Singer** [00:00:21]
output is what we were talking.

**Ryan Singer** [00:00:22]
in our last session, when we were focused on a piece comes out and it shouldn't be touching the third rail of the thing that we already got feedback on, that was in the output step?

**Marcel Santilli** [00:00:34]
It's the work that drives the output step.

**Ryan Singer** [00:00:36]
Well, it's the work that drives the output.

**Ryan Singer** [00:00:38]
Yeah, okay.

**Marcel Santilli** [00:00:39]
Yeah, yeah.

**Marcel Santilli** [00:00:40]
It's the execution layer here, right?

**Ryan Singer** [00:00:42]
Yeah, okay.

**Marcel Santilli** [00:00:43]
But the execution, it's kind of like you can get to 99% done and not ship it, and it's still 0% shipped, right?

**Marcel Santilli** [00:00:49]
Yes.

**Marcel Santilli** [00:00:51]
It's kind of like that concept, right?

**Marcel Santilli** [00:00:53]
In other words, like, we have to be the...

**Marcel Santilli** [00:00:56]
Something has to be the forcing function to know that the thing is actually getting out.

**Ryan Singer** [00:00:59]
Because otherwise, like, it delivers no value and it will have zero influence on outcomes, right?

**Marcel Santilli** [00:01:05]
And then the outcomes that people care about are, I kind of have to hear, like, visibility, both AI visibility and search visibility, and traffic, right?

**Marcel Santilli** [00:01:18]
Like, are people actually visiting your site and the pages?

**Marcel Santilli** [00:01:21]
And then engagement, are they actually, like, interacting or going further in?

**Marcel Santilli** [00:01:25]
And then, most importantly, is, like, the convergence, Like, which can be, you know, so the way to kind of think about it is, like, there's, like, leading and lagging outcomes.

**Marcel Santilli** [00:01:36]
And if we focus on the lagging, then, like, we might not see any changes.

**Marcel Santilli** [00:01:41]
And so the work drives the outputs.

**Marcel Santilli** [00:01:44]
in some ways, the work is a controllable input that drives the outputs.

**Marcel Santilli** [00:01:48]
And then in some ways, the output, meaning changes to pages or net new pages, is the controllable input that drives the output, the outcome, right?

**Marcel Santilli** [00:01:57]
And so, in...

**Marcel Santilli** [00:02:00]
And so that's kind of like the big picture.

**Marcel Santilli** [00:02:04]
And then like contextual here for customers is that all our customers spend more money than they spend on us on web agencies to manage their website.

**Marcel Santilli** [00:02:15]
It's like a mess of like analytics, like GA, Search Console, and no one even looks at that.

**Marcel Santilli** [00:02:24]
Their CMS is like usually one or two people even have access to a CMS in their company, right?

**Marcel Santilli** [00:02:30]
yet they're spending hundreds of thousands of dollars on ads and all this work surrounding the website.

**Marcel Santilli** [00:02:36]
And then when it comes to the content that goes on their website, it's kind of like they're flying blind, right?

**Marcel Santilli** [00:02:42]
And so it's the equivalent, an analogy that I used on a doc that I was writing today is like imagine like the ideal experience is like Robin Hood for managing your portfolio but investments, you know?

**Marcel Santilli** [00:02:53]
And today, like if you think of a website as an asset as your portfolio and pages as your stock.

**Marcel Santilli** [00:03:00]
Like, they're essentially using, like, a super outdated, like, flying blind.

**Marcel Santilli** [00:03:04]
have no idea.

**Marcel Santilli** [00:03:05]
have to call my broker and be like, hey, broker, what's going on with my stocks?

**Marcel Santilli** [00:03:09]
You know, how's it going?

**Marcel Santilli** [00:03:10]
Oh, you're doing great.

**Marcel Santilli** [00:03:11]
Don't worry about it.

**Marcel Santilli** [00:03:12]
You know, we bought five shares yesterday.

**Marcel Santilli** [00:03:14]
It's like, oh, what?

**Ryan Singer** [00:03:15]
Like, why?

**Ryan Singer** [00:03:16]
Like, what the hell?

**Marcel Santilli** [00:03:17]
And so that's like, we're here, you know, today.

**Marcel Santilli** [00:03:21]
And eventually it needs to feel like we're the Robin Hood for websites is, like, my mental motto a little bit, you know?

**Marcel Santilli** [00:03:27]
It's almost like they don't call the broker, but if you had a Robin Hood for you to see the price of the stock, the price of today, and the projection, have to go in, like, four different tools.

**Marcel Santilli** [00:03:38]
Yeah.

**Marcel Santilli** [00:03:38]
They all suck.

**Marcel Santilli** [00:03:39]
Yeah, yeah, exactly.

**Marcel Santilli** [00:03:40]
You have to go to Yahoo Finance.

**Marcel Santilli** [00:03:42]
You have to go to, like, all these things.

**Marcel Santilli** [00:03:44]
today I've been using, like, Robin Hood.

**Marcel Santilli** [00:03:46]
It's just, like, super  magical, right?

**Marcel Santilli** [00:03:48]
I've been like, hey, auto investing, the insights, like, the summarized things.

**Marcel Santilli** [00:03:54]
And so then the question becomes, like, this is a pretty complex thing, and we have a lot of...

**Marcel Santilli** [00:03:59]
Data and a lot of signals, but we can easily be trapped into trying to build a Google Analytics V2 or a Google Search Console with slightly better filters type of thing, you know?

**Ryan Singer** [00:04:12]
Yeah.

**Ryan Singer** [00:04:13]
Okay.

**Ryan Singer** [00:04:14]
how, all right.

**Ryan Singer** [00:04:20]
When we talk about, okay, so let me see if I give my hands around this.

**Ryan Singer** [00:04:25]
We're talking about, specifically we're talking about the performance of the pages and the content that's hosted on the website, right?

**Ryan Singer** [00:04:38]
there's other things that are in the whole marketing system like ads and stuff like that, but that's not, those are external to the problem.

**Ryan Singer** [00:04:46]
Okay.

**Ryan Singer** [00:04:47]
And when, when you are doing this hands-on for a client, if you're the, if you're just the active portfolio manager, right?

**Ryan Singer** [00:04:58]
And like you, there's.

**Ryan Singer** [00:05:00]
Robin Hood, then you are measuring the things that you showed, like visibility, conversion, like traffic, and so on.

**Ryan Singer** [00:05:10]
And you have a kind of a model of how the cause and effect links connect, you know?

**Ryan Singer** [00:05:18]
Like, we're getting X amount of traffic in, and therefore, like, this thing should be happening on this page that is or isn't happening.

**Ryan Singer** [00:05:25]
it's like, there seems to be a combination of, like, what are the actual things that we should be tracking?

**Ryan Singer** [00:05:31]
But also, like, what is the cause and effect interpretation of, like, what should I be looking at?

**Ryan Singer** [00:05:40]
Because it, and this is what I picked up from the brief that Daniel gave, like, what should I be looking at or thinking about in order to move this number?

**Ryan Singer** [00:05:47]
Yeah?

**Ryan Singer** [00:05:49]
So, like, in the current world, so the current software doesn't do anything for this.

**Ryan Singer** [00:05:55]
Like, when you are working with clients in the current world, like, how

**Ryan Singer** [00:06:00]
do you actually do this?

**Ryan Singer** [00:06:02]
Like, are you the only one, Marcel, who does this today?

**Marcel Santilli** [00:06:07]
Yeah.

**Marcel Santilli** [00:06:10]
the scope here, by the way, is content pages, right?

**Marcel Santilli** [00:06:14]
And the content, so like, it's not your homepage, it's not product marketing pages.

**Marcel Santilli** [00:06:18]
It's not, you know, a feature page.

**Marcel Santilli** [00:06:21]
It's like content, like evergreen type of content, like informational pages.

**Marcel Santilli** [00:06:26]
It could be like your integration pages, but it could be like articles.

**Marcel Santilli** [00:06:29]
It could be a blog.

**Marcel Santilli** [00:06:30]
could be like, you know, those are the areas of the site that tend to create more content and need to be refreshed all the time, right?

**Marcel Santilli** [00:06:42]
And it's quite a mess.

**Marcel Santilli** [00:06:45]
And when I did this, we go and when we're kicking off an engagement, we go and do an audit using SEMrush, which finds like gaps, essentially.

**Marcel Santilli** [00:07:00]
So, and, and then we put that into an air table, right?

**Marcel Santilli** [00:07:06]
And so think of it as like a one-off audit snapshot of like their current pages all the way to like types of pages they could be creating in order to go through traffic essentially, right?

**Marcel Santilli** [00:07:20]
So, so we do kind of like a snapshot and then set their site and flag issues.

**Marcel Santilli** [00:07:25]
And this is when it's done, right?

**Marcel Santilli** [00:07:27]
Most of the time it's not done right to be honest, you know, meaning like most of the time people might not like that some things are not getting done, but it's a one-time .

**Marcel Santilli** [00:07:39]
Okay.

**Marcel Santilli** [00:07:40]
Then from that, we start the work and we also connect to Google Analytics or equivalent of and Google Search Console, right?

**Marcel Santilli** [00:07:54]
Google Search Console gives you like essentially like time.

**Marcel Santilli** [00:08:00]
Sometimes a link to your page showed up in search results, aka impressions, and how often people click through to your site, and what is the average rank that you've had.

**Marcel Santilli** [00:08:11]
But think of Search Console as the actual search visibility data, and Samrush has estimated, based on the entire market, estimation of the volume of searches and things like that.

**Marcel Santilli** [00:08:24]
Right, so Search Console is like search visibility, Google Analytics is your actual, like, what's happening on the site, right?

**Marcel Santilli** [00:08:34]
Yeah, so the Search Console is upstream from the actual pages, but then when they get to the pages downstream, then Google Analytics is telling you what happens there.

**Marcel Santilli** [00:08:42]
Exactly, like Google Analytics, there's a little bit of overlap, which is like, Google Analytics, can see how much, like, search referral trash you have, but then Search Console gives you more details on the queries, on the, like, you know, like, the,

**Marcel Santilli** [00:09:00]
Impressions, click-through rates, and average position, which I can't get.

**Marcel Santilli** [00:09:05]
And then, when we start to do the work, right?

**Marcel Santilli** [00:09:10]
Like, so every single week, ideally, and this is a normally simplified version, but, like, we're publishing, we're five pages, right?

**Marcel Santilli** [00:09:19]
Like, we're working on five assignments, and we're publishing five, right?

**Marcel Santilli** [00:09:24]
Some clients more, some clients less.

**Marcel Santilli** [00:09:26]
And then, what should happen at this point, on the engagement, should say, hey, you know how we're doing this work?

**Marcel Santilli** [00:09:38]
This work, remember, is based on the strategy,.k.a.

**Marcel Santilli** [00:09:43]
this audit, a.k.a.

**Marcel Santilli** [00:09:45]
table, right?

**Marcel Santilli** [00:09:47]
And our hypothesis was that, and because we did that, this is what happened.

**Marcel Santilli** [00:09:54]
We were right, or we were wrong about our hypothesis, and that's what we're doing to continue.

**Marcel Santilli** [00:10:00]
To, like, re-prioritize that, right?

**Marcel Santilli** [00:10:03]
Okay.

**Marcel Santilli** [00:10:04]
Traffic is going up, traffic is not going up.

**Marcel Santilli** [00:10:06]
And why is it going up?

**Marcel Santilli** [00:10:08]
Or why is it not going up?

**Marcel Santilli** [00:10:10]
And what are we doing about it?

**Ryan Singer** [00:10:11]
And how does that change what work we do next?

**Marcel Santilli** [00:10:14]
You know?

**Marcel Santilli** [00:10:15]
And that's the super overly simplified version of that.

**Marcel Santilli** [00:10:19]
Somewhere in the middle there, we said, hey, you know what?

**Marcel Santilli** [00:10:22]
There's too much going on here, and every client's slightly different.

**Marcel Santilli** [00:10:25]
We should just sync all of this data into a little prediction.

**Marcel Santilli** [00:10:30]
then we started to do it as a standard part of our engagement, a looker dashboard, a Google looker dashboard, right?

**Marcel Santilli** [00:10:39]
And it's pretty much just a VI tool, right?

**Marcel Santilli** [00:10:44]
And so it's pulling all this data and just, like, showing it in a standardized Sorry, let me check.

**Ryan Singer** [00:10:50]
In current engagements, you are at this step where you want to be analyzing what happened now that we've done the work.

**Ryan Singer** [00:10:58]
The way that you're doing that.

**Ryan Singer** [00:11:00]
Just in the current way, is by setting up the Looker dashboard in Google?

**Ryan Singer** [00:11:04]
Yeah, we set up a Looker dashboard that pulls some of the metrics on the website.

**Marcel Santilli** [00:11:09]
And you assume that's set up correctly and that it's pulled the right data, which is the biggest subject there.

**Marcel Santilli** [00:11:15]
And then you're assuming the engagement manager is actually looking at it, taking a screenshot, or summarizing the insights from it.

**Marcel Santilli** [00:11:24]
To give you a little bit more context there, Ryan, like the Looker dashboard was a big source of fame.

**Marcel Santilli** [00:11:30]
for us, so we decided to build a feature in the product that replaces the Looker dashboard.

**Marcel Santilli** [00:11:37]
that we have today, but we haven't rolled out yet, so people are not using it yet.

**Marcel Santilli** [00:11:43]
It's a high advantage to what we started to build and whether people are using it or not.

**Marcel Santilli** [00:11:47]
This is kind of like, for most standard engagements, this is the actual, like, on-the-ground reality.

**Ryan Singer** [00:11:53]
And that's what happens now.

**Marcel Santilli** [00:11:55]
we're building the system in parallel, you know?

**Ryan Singer** [00:11:57]
Yeah.

**Marcel Santilli** [00:11:58]
that's, like, on-the-ground reality.

**Marcel Santilli** [00:12:00]
Versus, like, reality of what we built is, like, I can cover that next, you know, versus the audio of what people are using, you know.

**Marcel Santilli** [00:12:09]
Okay.

**Ryan Singer** [00:12:13]
Quick question.

**Marcel Santilli** [00:12:15]
Who's the engagement manager is on your team or on their team?

**Marcel Santilli** [00:12:20]
On our team.

**Marcel Santilli** [00:12:21]
this is kind of like our evolution of our delivery model.

**Marcel Santilli** [00:12:27]
And so think of it as, like, this is ultimately the person that is on a call with a client every week, that is responsible for renewal, that is, like, dealing internally with our production teams, making sure we're delivering things, right?

**Marcel Santilli** [00:12:43]
Like, and they're ultimately responsible.

**Ryan Singer** [00:12:45]
They're account manager, but also part account manager, part customer success, part strategist.

**Ryan Singer** [00:12:51]
So, okay, question.

**Ryan Singer** [00:12:55]
There's an element of should in this story, which is supposed to be current.

**Ryan Singer** [00:13:02]
If we were to reach for an individual case where this wasn't a should, but a did, like this happened, would that be like because you were doing it as opposed to the engineering manager, as opposed to the engagement manager?

**Marcel Santilli** [00:13:19]
Can you tell me a story about like when this actually did happen as opposed to should be happening?

**Marcel Santilli** [00:13:24]
let's get two examples here.

**Marcel Santilli** [00:13:30]
One, I was just looking at in a call last week, Ambient AI, and so they, there's essentially like camera detection for like guns, like detecting guns in public-based places, essentially like, it's like a school, by the way, so think about it.

**Marcel Santilli** [00:13:49]
And the other one is Lovable, another client, right?

**Marcel Santilli** [00:13:52]
Like, so, Lovable is, it did, Ambient is, it should.

**Marcel Santilli** [00:13:56]
Yep.

**Marcel Santilli** [00:13:58]
And Lovable is...

**Marcel Santilli** [00:14:00]
We had George, who has the engagement manager here, and I was fairly involved, right?

**Marcel Santilli** [00:14:07]
we did that audit right, we connected all the things right, and from the beginning, it was a $25,000 a month engagement with Lovell, right?

**Marcel Santilli** [00:14:17]
And we followed all the steps that we should follow.

**Marcel Santilli** [00:14:21]
we did everything, and we published, we follow our strategy in Airtable, and it's kind of like content OS, if you will.

**Marcel Santilli** [00:14:32]
I can also turn my screen and show you this.

**Ryan Singer** [00:14:35]
Let's stay at high level, because I want to be able to contrast between cases, you know?

**Ryan Singer** [00:14:40]
let's see if we can just keep rolling through it.

**Ryan Singer** [00:14:42]
you did the audit piece with Lovell.

**Marcel Santilli** [00:14:45]
we set the whole strategy in Airtable, and I did that myself.

**Marcel Santilli** [00:14:50]
And so there was a lot of, like, flustering of opportunities and things like that, right?

**Marcel Santilli** [00:14:56]
Then I communicated to the team what the strategy was.

**Marcel Santilli** [00:15:00]
And to the client, and so I was on the call with George with Lovable, communicating why we're going towards this strategy.

**Marcel Santilli** [00:15:07]
was leading it, right?

**Marcel Santilli** [00:15:10]
George needed to escalate when things got blocked of like, hey, they don't have a place to publish.

**Marcel Santilli** [00:15:16]
Like, we should do something about it.

**Marcel Santilli** [00:15:17]
Okay, we fixed a lot of blockers to publishing, and then we got to publishing, right?

**Marcel Santilli** [00:15:23]
And then when we got to publishing, the client started asking, like, hey, what are the signals that we should be seeing?

**Ryan Singer** [00:15:31]
the client pushed us a little bit.

**Marcel Santilli** [00:15:34]
And George, like, asked me, I gave him some advice on, like, what to look at, right?

**Marcel Santilli** [00:15:40]
And what signals we should be looking at.

**Marcel Santilli** [00:15:42]
And from then on, they started to pull that into a looker dashboard and reporting on it and actually paying attention to it, you know, weekly, right?

**Marcel Santilli** [00:15:50]
In this case, luckily, everything  worked because Publish started doing well, and so, like, all our weekly charts are, like, up to the right.

**Marcel Santilli** [00:16:01]
From there, the client was like, hey, this is great, but I really need you all to tell me if it's driving any conversions.

**Marcel Santilli** [00:16:11]
then recently, this is like two weeks ago, they looked into their analytics tool.

**Marcel Santilli** [00:16:17]
I don't know which analytics tool that has the conversion data.

**Marcel Santilli** [00:16:21]
And then they started to pull that data.

**Marcel Santilli** [00:16:23]
And then at the same time, Lovable was like, whoa, this is amazing.

**Marcel Santilli** [00:16:29]
We want to increase their scope.

**Marcel Santilli** [00:16:31]
they almost doubled the scope they signed last week, right?

**Marcel Santilli** [00:16:34]
they went from 25 to 40K a month.

**Marcel Santilli** [00:16:36]
And we tied at Driven already in just four months of work, 150 or so signups, and generated about 50K in incremental, I think it was ARR.

**Marcel Santilli** [00:16:50]
But it was, in other words, it was getting close to ROI positive already in only four months into the engagement.

**Ryan Singer** [00:16:56]
Lovable is a success story.

**Ryan Singer** [00:17:00]
In this workflow, in the fact that it worked and it led to them growing their scope with you, the place where it didn't work or it's not a model for the future is the fact that you, Marcel, had to jump in in order to actually give the judgment around what to be looking at at this moment.

**Marcel Santilli** [00:17:17]
And it wasn't run by George here.

**Marcel Santilli** [00:17:19]
Is that right?

**Marcel Santilli** [00:17:20]
And it was, and the thing here is that George knew to escalate to me and also the client pushed us.

**Ryan Singer** [00:17:30]
And that's what happens.

**Marcel Santilli** [00:17:32]
The client pushed us and was like, hey, you're doing all this work.

**Marcel Santilli** [00:17:36]
Is it working?

**Marcel Santilli** [00:17:37]
And then we're like, yeah, yeah, yeah.

**Marcel Santilli** [00:17:38]
Hold on.

**Marcel Santilli** [00:17:39]
I'll give that data real quick.

**Ryan Singer** [00:17:40]
It wasn't proactive.

**Ryan Singer** [00:17:42]
It wasn't proactive.

**Ryan Singer** [00:17:43]
It wasn't like operating procedure from your side.

**Marcel Santilli** [00:17:47]
wasn't like, hey, we're doing this work and these are the targets we're setting.

**Marcel Santilli** [00:17:51]
Does that seem right?

**Ryan Singer** [00:17:53]
Cool.

**Marcel Santilli** [00:17:53]
Hey, we're reporting against these targets.

**Marcel Santilli** [00:17:55]
By the way, we really need to tie this to conversions.

**Marcel Santilli** [00:17:59]
Yeah.

**Marcel Santilli** [00:18:06]
And there's a few clients where that was the same thing, right?

**Marcel Santilli** [00:18:09]
It was like, unless the client pushes us, we don't connect it all the way to conversions.

**Marcel Santilli** [00:18:14]
Because we're almost afraid of the answer, you know?

**Ryan Singer** [00:18:16]
And then when the answer is good, we're like, oh, I'm so glad we did, you know?

**Marcel Santilli** [00:18:20]
Yeah.

**Marcel Santilli** [00:18:20]
And this is the case where the client actually was tracking conversions.

**Marcel Santilli** [00:18:24]
There's many cases that clients don't even track their own conversions.

**Marcel Santilli** [00:18:27]
But it's like, why don't we tie back?

**Marcel Santilli** [00:18:30]
We don't know about that.

**Marcel Santilli** [00:18:30]
This is like the best case scenario where everything is positive, everything is working.

**Marcel Santilli** [00:18:35]
And even if the client points it out, we actually do it and we do it fast.

**Marcel Santilli** [00:18:40]
We're on top of it, right?

**Marcel Santilli** [00:18:42]
And the strategy was good and the strategy worked right away, you know?

**Marcel Santilli** [00:18:48]
And so obviously, you know, upselling from 25 to 40 a month.

**Marcel Santilli** [00:18:56]
And like within four months of the engagement is incredible.

**Marcel Santilli** [00:19:00]
You know, there's room here to go even bigger.

**Marcel Santilli** [00:19:04]
And so now on an ongoing basis, like the team is publishing more content, but they're also flying completely blind because the way they're operating now, it's like we have about, let's call it 100 pages published today in four months.

**Marcel Santilli** [00:19:23]
And now we're going from five a week to like 16 a week with this additional scope.

**Marcel Santilli** [00:19:29]
But it's like, and so what's happened in other engagements, like augmented code, for example, are we're up to the right, up to the right, up to the right, all of a sudden it starts to flatten out.

**Marcel Santilli** [00:19:40]
Like, oh, it might, it might just be a blub.

**Marcel Santilli** [00:19:42]
And then another flat week, it's probably a blub.

**Marcel Santilli** [00:19:45]
Let's just crank out more content.

**Marcel Santilli** [00:19:47]
Another week flat, another week flat, and then it starts to decline.

**Marcel Santilli** [00:19:50]
And then when you look back, it's because something, some page that was working, it started to not work as well.

**Marcel Santilli** [00:19:58]
And no one.

**Marcel Santilli** [00:20:00]
Figure out why.

**Marcel Santilli** [00:20:02]
And a lot of it is because you publish something and sometimes it rises to the top and starts to get traffic.

**Marcel Santilli** [00:20:09]
But if you don't go back and make that even better, then eventually it's going to decay, right?

**Marcel Santilli** [00:20:15]
And so think of it as like the half-life of the pages are becoming shorter with AI because all these systems are still dynamically changing all the time that we really need to look at like creating a page is the beginning, not the end.

**Marcel Santilli** [00:20:35]
It's like planting a seed.

**Marcel Santilli** [00:20:36]
And some seeds just like take off really well because the environment is really healthy.

**Marcel Santilli** [00:20:42]
But even with those, you can't just So does flying blind mean like I'm producing pages, but I don't know what effect they're having?

**Ryan Singer** [00:20:54]
Correct.

**Marcel Santilli** [00:20:55]
Uh-huh, okay.

**Marcel Santilli** [00:20:56]
Because you can't tie it to it because the opportunities are...

**Marcel Santilli** [00:21:00]
We're all in Airtable, right?

**Marcel Santilli** [00:21:03]
And you did the work, and you published the work, and the data on how that work is, or the outcomes of that work is in Google Analytics.

**Marcel Santilli** [00:21:13]
You have to literally go in Google Analytics, start to filter, and filter here, filter there, compare at different times, and you have to figure out pages are decaying, and how, and why is that?

**Marcel Santilli** [00:21:26]
Is it because the content sucks?

**Marcel Santilli** [00:21:28]
Is it because, like, you know, something is broken?

**Ryan Singer** [00:21:32]
Is it because there was a change to the page?

**Marcel Santilli** [00:21:34]
Or is it something else?

**Marcel Santilli** [00:21:36]
the algorithm.

**Marcel Santilli** [00:21:37]
Yeah, or was there an algorithm change?

**Marcel Santilli** [00:21:39]
Is it a systemic change due to results, you know?

**Ryan Singer** [00:21:42]
Okay.

**Marcel Santilli** [00:21:46]
And so it's, it sounds gnarly, but, like, I've been doing this for 15 years, and the, the TLDR here is every single thing I build,

**Marcel Santilli** [00:22:00]
If we follow this pattern, which is like, hey, you pick the right strategy, you create pretty good content, not perfect, pretty damn good, and you do it systematically all the time, and you also go back and continue to improve what's already there, and you focus on things that are almost coming to the top, meaning there's a lot of latent opportunity for results.

**Marcel Santilli** [00:22:30]
And you also focus on things that are already generating a ton of traffic, because you don't want that to drop, right?

**Marcel Santilli** [00:22:37]
Like, it's a pretty simple formula, right?

**Marcel Santilli** [00:22:39]
You go like, hey, the ones that are at the top, the top 1% of pages drive 20% of results, if not more.

**Marcel Santilli** [00:22:48]
make sure the top 1%, you never  it up, and you keep being it perfect.

**Marcel Santilli** [00:22:53]
And then the ones that are like, hey, it's getting impressions, but not quite clicks, but it has a lot of

**Marcel Santilli** [00:23:00]
opportunities keep doing a little bit of work to see if you can get it up a little, you know, and if you get it up, just a tiny little bit to the first page, kind of, and then it starts to drive, you know, a bunch of results.

**Marcel Santilli** [00:23:13]
The challenge is that, like, before it was like, search was kind of like the only game in town in some ways that you can control as a machine.

**Marcel Santilli** [00:23:23]
And now, with AI Answers, it's like...

**Ryan Singer** [00:23:28]
It plays a totally different role.

**Marcel Santilli** [00:23:32]
No, no.

**Marcel Santilli** [00:23:34]
Yeah, it's like, think of it as search.

**Marcel Santilli** [00:23:40]
AI is augmenting or adding to, it's additive to search.

**Marcel Santilli** [00:23:47]
it's not like search is going down, like the total number of searches is actually going up.

**Marcel Santilli** [00:23:52]
Some of the things that people use to search, they're actually going into AI for answers, but not all.

**Marcel Santilli** [00:24:00]
And on top of that, there's a bunch of things that you would never search before.

**Marcel Santilli** [00:24:04]
You would have like called someone and talked to someone like a salesperson that is also here, right?

**Marcel Santilli** [00:24:09]
it's like, it's growing and it's growing very fast.

**Marcel Santilli** [00:24:13]
And then here, it's like 200 citations, right?

**Marcel Santilli** [00:24:18]
it's pulling from 200 sources.

**Marcel Santilli** [00:24:19]
And it's no longer like best software for architects.

**Ryan Singer** [00:24:23]
It's like, hey, I'm an architect firm in Boston.

**Ryan Singer** [00:24:26]
I'm 30 employees.

**Marcel Santilli** [00:24:27]
I'm really struggling with like, if there's any software out there that I should use, it would be really nice if that software used AI and also wasn't too expensive.

**Marcel Santilli** [00:24:35]
Like, can you come up with a full list of what I need?

**Marcel Santilli** [00:24:38]
And then like, give me a link to all their websites and give me what questions I should ask them when I talk to sales.

**Marcel Santilli** [00:24:44]
That's kind of weird.

**Marcel Santilli** [00:24:45]
essentially, like before you had like what Marcel said, maybe you have like, out of 200 pages, have 10 that really matters and you can track them pretty well.

**Marcel Santilli** [00:24:53]
Yep.

**Marcel Santilli** [00:24:54]
Now you have that 10 plus 100 because everything turned super long because of LLS.-hmm.

**Marcel Santilli** [00:25:00]
Yeah.

**Marcel Santilli** [00:25:01]
And so the way to win the game with that lump search is like, you got to maintain the quality, but you got to crank up the volume, not for volume sake, but because you need to have answers to the personalized version of it, right?

**Marcel Santilli** [00:25:15]
if it was like, hey, that's AI coding tools, and so it would be just one page.

**Marcel Santilli** [00:25:22]
But now it's kind of like, hey, how do I manage my context in this AI coding tool?

**Marcel Santilli** [00:25:31]
And hey, how do I, you know, tell security that this thing is GPR compliant and blah, blah, blah.

**Marcel Santilli** [00:25:37]
Hey, which tools are best if I'm building a iOS app?

**Marcel Santilli** [00:25:43]
Like, you know, there's all these kind of like use case phase, persona, mapping out every possible question anyone will possibly have that's within your audience and within your domain and systematically becoming and continue to be the best answer to those questions on the web.

**Marcel Santilli** [00:26:00]
Like, legit best answers, proper research, properly reading, time on page, all those things still matter, you know, it's not just feeding LLM a potion.

**Ryan Singer** [00:26:09]
Are these citations actually, do they become click-throughs for you, or what causal role do these citations play in the funnel?

**Marcel Santilli** [00:26:20]
Great job, you know, poking at the north box, you know, but, so, the way to kind of think about it is, before, you do a bunch of searches and things, right, like, or people will come to your site and there's two distinctions, there's branded and non-branded search, right, like, meaning, if someone's searching for your brand, that's, like, the best traffic you can possibly get, and it tends, from my experience, to convert three to seven, right?

**Marcel Santilli** [00:26:53]
And so, the problem is, you can't influence that very easily, other than, like, tons of ads and...

**Marcel Santilli** [00:27:00]
And just people finding out about you.

**Marcel Santilli** [00:27:02]
And so when you show up in the search, the main way for you to get value from the search results is for you to click through and consume that information.

**Marcel Santilli** [00:27:13]
And so it's a very easy linear relationship.

**Marcel Santilli** [00:27:16]
But also even that relationship, from my experience, and there's studies on this as well, is that if you have 10 new people coming to your site this month or non-branded, at 10, 20, sometimes 30% of those 10, next month will actually search for your brand directly, right?

**Marcel Santilli** [00:27:38]
there's kind of this relationship, which is not a perfect relationship, and it's really, really hard.

**Marcel Santilli** [00:27:43]
But it's like, if you get people on your site in a non-branded way, later on, they're going to search for your brand.

**Marcel Santilli** [00:27:52]
And then that traffic number is really high.

**Marcel Santilli** [00:27:54]
it's kind of like that relationship.

**Marcel Santilli** [00:27:56]
With LLMs, it's even harder because...

**Marcel Santilli** [00:28:00]
Because you might be consumed by potentially, right?

**Marcel Santilli** [00:28:03]
Right.

**Marcel Santilli** [00:28:04]
And when you do get referral from LLMs, it's like the equivalent of brand traffic, right?

**Ryan Singer** [00:28:10]
even though the volume of click-through ratings is not as high.

**Ryan Singer** [00:28:16]
It's the equivalent of brand traffic in the sense that you've gotten the endorsement from the LLM?

**Marcel Santilli** [00:28:21]
Exactly.

**Marcel Santilli** [00:28:22]
It's like you didn't just get the endorsement.

**Marcel Santilli** [00:28:27]
It's like you got the endorsement, and they went through half of your sales process already by that point if you're doing it right.

**Marcel Santilli** [00:28:35]
And then by the time they talk to you, it's like, I know everything I need to know.

**Marcel Santilli** [00:28:38]
Okay.

**Marcel Santilli** [00:28:38]
Like, let's go, you know?

**Marcel Santilli** [00:28:41]
And so it's like from our client's side, by a decent chunk.

**Marcel Santilli** [00:28:46]
And that's confirmed by a lot of, like, studies and research.

**Ryan Singer** [00:28:50]
Okay.

**Ryan Singer** [00:28:51]
Dumb question for me just to understand this, just a little piece of context.

**Marcel Santilli** [00:28:56]
let's say I have an LLM result from, let's say, Google.

**Ryan Singer** [00:29:00]
Google's the AI search, okay?

**Ryan Singer** [00:29:03]
There are pages that are inputs to this as like, let's say, citations or whatever, right?

**Ryan Singer** [00:29:14]
And then there are clicks coming out from this two pages, right?

**Ryan Singer** [00:29:22]
Is there, are these the same pages, like, concerning an individual client's property?

**Marcel Santilli** [00:29:31]
Or is it like, you might have one page that you know is concerning, but that's referring you to a different page.

**Marcel Santilli** [00:29:37]
It's just that it's really hard to connect the relationship between, you know, you showing up and not getting clicks, right?

**Marcel Santilli** [00:29:49]
Are you in the answer, let's call it, but then no one can go into your site, and then later on in a completely separate session, actually playing.

**Marcel Santilli** [00:30:00]
And so it's very like correlation and it's really hard to establish cause and effect.

**Ryan Singer** [00:30:06]
I see.

**Ryan Singer** [00:30:06]
Yeah, this is Bob Mesta's whole thing about like the passive looking, active looking, like you're in a learning process where you're starting to learn names of things and stuff, but you might not actually pursue one of those options, but you've learned about it from the first run.

**Ryan Singer** [00:30:19]
Yeah, yeah, yeah.

**Ryan Singer** [00:30:20]
Yeah.

**Ryan Singer** [00:30:21]
Good.

**Marcel Santilli** [00:30:22]
Okay.

**Marcel Santilli** [00:30:22]
And so over time, so like I'll give you just like a super simple thing here.

**Marcel Santilli** [00:30:29]
when I was a service site and we were spending about half a million a month in ads, right?

**Marcel Santilli** [00:30:35]
And then Facebook had the worst conversions and the cost for like had massive issues with like spam form fills.

**Marcel Santilli** [00:30:44]
And so we literally like turn off Facebook for like, I think it was like six weeks, right?

**Marcel Santilli** [00:30:51]
Except our highest performing paid channel was brand searches.

**Marcel Santilli** [00:30:57]
it was like us bidding on our own brand.

**Marcel Santilli** [00:30:59]
competitive.

**Ryan Singer** [00:31:22]
The fact that it's actually a branded search is lagging indicator of other things that you're doing.

**Marcel Santilli** [00:31:28]
Exactly.

**Marcel Santilli** [00:31:30]
Yeah.

**Marcel Santilli** [00:31:30]
Yeah.

**Marcel Santilli** [00:31:31]
Which there's a lot of things I can influence that.

**Marcel Santilli** [00:31:33]
It's really hard to say it's because you have a product announcement or it's because you're publishing F's on a content that's doing well and you're showing up.

**Marcel Santilli** [00:31:42]
Okay.

**Marcel Santilli** [00:31:42]
Right?

**Marcel Santilli** [00:31:43]
then the last thing here that we didn't cover recently is the fact that then you get traffic.

**Marcel Santilli** [00:31:53]
But then traffic is just kind of like the beginning.

**Marcel Santilli** [00:31:56]
I mean, they actually internalize the information, first of all.

**Marcel Santilli** [00:31:59]
So.

**Marcel Santilli** [00:31:59]
So.

**Marcel Santilli** [00:31:59]
So.

**Marcel Santilli** [00:32:00]
Second, like, it doesn't mean that from that page, we're actually telling them where to go and what to do, you know, and what is the next best action, or that we even are measuring or tracking that at all.

**Marcel Santilli** [00:32:12]
And sometimes, like, if you're searching for very, like, like you said, like, very generic information, and you land on this page and you consume that information, you might not be ready to supply a credit card, which then means you need to either extend them to a, you know, kind of like leading conversion, not a, like, not a final event, you need to send them on a path, right?

**Marcel Santilli** [00:32:33]
And sometimes that path, if you're a lovable, is easy because it's just like such a low barrier to sign up and such a low price and such an easy value exchange that it's just like, yep, you got, you visited a blog about a random  thing, and then you sign up and just buy a credit card and pay like 50 bucks.

**Marcel Santilli** [00:32:50]
It's amazing, right?

**Marcel Santilli** [00:32:52]
But for 99% of, like, B2B companies, that's not the case, and, like, conversion is not even, like, final event.

**Marcel Santilli** [00:33:00]
That is kind of like, are they on this path that is in that path related to your actions?

**Marcel Santilli** [00:33:05]
That's where conversion is like a messy thing that is not a straightforward thing.

**Marcel Santilli** [00:33:10]
Got it.

**Marcel Santilli** [00:33:10]
Okay.

**Ryan Singer** [00:33:11]
like a given, maybe another way of framing it is like a given page, which you wrote for a strategic reason based on the work you did up here.

**Ryan Singer** [00:33:23]
A given page has kind of like a job in the sense of like, I expect this page to lead people onto this next leg in the thing.

**Ryan Singer** [00:33:33]
And I, and I'm going to, so what I want to be able to, I want to be seeing, first of all, I want to be seeing inbound to this page.

**Ryan Singer** [00:33:41]
And I want to know like, is it, is it, is it near the top?

**Ryan Singer** [00:33:44]
And therefore I have to keep pushing it to be perfecting it to stay in the 1% or is it not really making it?

**Ryan Singer** [00:33:50]
And I, I, I should be iterating on it to see if I can get it to pop.

**Ryan Singer** [00:33:53]
Those are the two things you mentioned before, but that's kind of the, that's sort of the left side of the inbound side of the page.

**Ryan Singer** [00:33:59]
And then there's the.

**Marcel Santilli** [00:34:00]
There's the outbound side of the page, which is like, is the other thing that I think should be happening, according to the job of this page, happening more or less than before as well.

**Marcel Santilli** [00:34:08]
Every page that we create comes out of the hypothesis that we call an opportunity in the system.

**Marcel Santilli** [00:34:15]
those are, today, most of it is based on keywords of the traffic of estimates.

**Marcel Santilli** [00:34:21]
And we calculate a percent, we usually calculate the percent of that estimate that would be doable for this client.

**Marcel Santilli** [00:34:30]
we're essentially putting the hypothesis out, so we need to see if the inbound is accurate to that hypothesis, to the opportunity assumption.

**Marcel Santilli** [00:34:40]
And then we also need to figure out if that is eventually going to the down the path that you're having.

**Marcel Santilli** [00:34:47]
we have this, we come up with the right hypothesis, we come up with the right opportunities at the top there of this strategy.

**Marcel Santilli** [00:34:53]
And then everything goes right through the workspace setup as well.

**Marcel Santilli** [00:34:56]
We know what the client cares about, like all their CTAs.

**Marcel Santilli** [00:35:00]
and other things, that we can start adding that to the page as we go.

**Marcel Santilli** [00:35:05]
the creation of the page is not just that the content is good and accurate and sounds right, sounds with their tone, the kind of stuff that we're doing last session, it's also like how we're leading to the right magnets, the right offerings.

**Ryan Singer** [00:35:19]
there's a certain thing.

**Ryan Singer** [00:35:20]
Got it.

**Ryan Singer** [00:35:21]
Okay.

**Ryan Singer** [00:35:21]
I think I'm up to date on the workflow that you're talking about.

**Ryan Singer** [00:35:26]
I think I'm up to date on a little bit of...

**Ryan Singer** [00:35:28]
Let me just try and talk back.

**Ryan Singer** [00:35:30]
like the problem today is...

**Ryan Singer** [00:35:35]
Okay, so the general issue is, of course, that like these things are happening.

**Ryan Singer** [00:35:41]
These things are happening.

**Ryan Singer** [00:35:43]
there's this new dynamic of you need to publish more and more.

**Ryan Singer** [00:35:46]
But if you're publishing more and more, then you have to be working harder to not be flying blind so that you're actually paying attention to what's the outcome.

**Ryan Singer** [00:35:54]
And if you're paying attention to the outcome, then you would be pushing the 1% up.

**Marcel Santilli** [00:36:00]
And up to stay on the top, you'd be pushing the laggards up to see if you can get them to work.

**Ryan Singer** [00:36:04]
And then there's something around the conversion piece, which is like, is this matching up or down against the hypothesis we had for what the action should be taking place from here?

**Marcel Santilli** [00:36:19]
Yeah, and so like, I'll give you the context to just know that conversion is like a known, like, challenge.

**Marcel Santilli** [00:36:28]
And so it's like, it's not an easy thing because there's multiple layers to that meeting.

**Marcel Santilli** [00:36:35]
In one scenario, there is you do everything right and you bring a  ton of people to the page.

**Marcel Santilli** [00:36:40]
And then that page has no CTAs, call to actions, and no life offers, and no opportunity for anyone to go anywhere anyways.

**Marcel Santilli** [00:36:50]
And so it's like, you know, so then that traffic's only value is that you're expanding your retargeting pool.

**Marcel Santilli** [00:36:57]
Meaning like, later on, you can retarget them.

**Marcel Santilli** [00:37:00]
Because now you pixel that user, and you can like, if you're doing that right, right?

**Marcel Santilli** [00:37:04]
And then from there, maybe there's like, really, you're sending them to a solution page, or to some other page, that even though it's not a conversion page, or, you know, they're not going to become a known user, at least they're going to go higher in intent, you know?

**Marcel Santilli** [00:37:20]
Like, so for instance, like, there might be a pricing page.

**Marcel Santilli** [00:37:24]
And so one of my most successful campaigns, last time when I was at DeepGram, was like, anyone that was visiting the pricing page, I would try to de-anonymize them and hit them up.

**Marcel Santilli** [00:37:35]
And we had like, reply rates of like 70%.

**Ryan Singer** [00:37:38]
let's take that as a case.

**Ryan Singer** [00:37:41]
In the current on the ground world, then how would you express that?

**Ryan Singer** [00:37:46]
not the inbound part, not how much traffic is the page getting part, but this other part of like, are we raising the intent?

**Ryan Singer** [00:37:54]
Or are we getting them to the pricing page?

**Ryan Singer** [00:37:56]
Is that something that, is that something you would be setting up in the data?

**Marcel Santilli** [00:38:11]
There's one customer called WebStacks.

**Marcel Santilli** [00:38:13]
They're a web agency.

**Marcel Santilli** [00:38:15]
they do that for other clients.

**Marcel Santilli** [00:38:18]
And so they really pushed us to be like, hey, we have these like pillar pages, if you will.

**Marcel Santilli** [00:38:23]
Every single piece of content you create has to align to a solution page and to a gated offer.

**Marcel Santilli** [00:38:28]
And so what we're looking for is like of your cluster of pages, like what is their click-through rate, if you will, to a solution page and their conversion rate into a gated offer.

**Marcel Santilli** [00:38:43]
And then in addition to that, we can also look at like in aggregate, like people that are going directly and filling out a form to talk to sales, right?

**Marcel Santilli** [00:38:52]
that's like the final destination.

**Marcel Santilli** [00:38:54]
But like, they're also okay with the fact that like, if they go in this in-between,

**Marcel Santilli** [00:39:00]
We know that people that go to a solution page, on average, if you look at just like across the board, that traffic converts at a higher pace.

**Marcel Santilli** [00:39:11]
It's in between steps that if we do that, we're doing our job.

**Marcel Santilli** [00:39:15]
On average, not in session, but on average, you know, like I'll give you an example.

**Marcel Santilli** [00:39:20]
I did this cohort analysis at DeepGram that I said, hey, I want to look at, I went in GA and I said, I want to look for only sessions that have at least one visit to a pricing page.

**Marcel Santilli** [00:39:32]
And then I looked at my conversion rate to sales forms.

**Marcel Santilli** [00:39:35]
It was seven times higher, seven times higher, right?

**Marcel Santilli** [00:39:38]
I know, so then I told my team, like, get people to look at the pricing page.

**Marcel Santilli** [00:39:43]
If you do that, on average, this cohort, I get it.

**Ryan Singer** [00:39:47]
This cohort is my highest over in cohort.

**Ryan Singer** [00:39:49]
there's, there's, there's like page, page, page, page in terms of where they could land.

**Ryan Singer** [00:39:53]
There's a pricing page.

**Ryan Singer** [00:39:55]
And then there's actually like sales contact or whatever.

**Ryan Singer** [00:39:58]
And what, what you're saying.

**Ryan Singer** [00:40:00]
saying is there's all of these ways to get into pricing page, but we don't actually have to measure a conversion in the sense that there's no real click-through that we're watching to get to sales, but what we're able to infer is that when we see more people coming to pricing, it explains why we see more things.

**Marcel Santilli** [00:40:21]
Yeah, think of it as, like, there's content pages, then there's, like, high intent pages, and then there's, like, offers, and then there's, like, right?

**Marcel Santilli** [00:40:35]
Like, so, like, a docs page sometimes can be high intent.

**Marcel Santilli** [00:40:41]
Yeah, totally.

**Marcel Santilli** [00:40:41]
Technical clients, example, technical websites, the docs page is there.

**Marcel Santilli** [00:40:47]
it.

**Marcel Santilli** [00:40:48]
Like, the installation docs, or offers, and you could distinguish, like, offers, like, for example, download this white paper, sign up for a webinar, or an event or something.

**Marcel Santilli** [00:41:00]
Versus, like, talk to sales, or actually, like, create an account on the product, right?

**Marcel Santilli** [00:41:04]
those were actually, like, legit conversions, like, you know?

**Marcel Santilli** [00:41:09]
And then conversions, offers don't have a monetary value.

**Marcel Santilli** [00:41:13]
Conversions can't have a monetary value, right?

**Marcel Santilli** [00:41:16]
Like, meaning, like, I know, for example, when I was at eGram, that, like, we had X number of contact sales, and I knew the average conversion of contact sales all the way to one.

**Marcel Santilli** [00:41:27]
And so, and I knew our average contract value.

**Marcel Santilli** [00:41:31]
I could estimate the value of a sign-up for me, right?

**Marcel Santilli** [00:41:35]
From a, like, standard.

**Marcel Santilli** [00:41:38]
And then, but I could, I'll be in there, driving net new opportunities.

**Marcel Santilli** [00:41:42]
And I know the cost for opportunity in all those channels.

**Marcel Santilli** [00:41:45]
But I also have the opportunity cost of one incremental one here.

**Marcel Santilli** [00:41:49]
that, the difference there is, like, if you're spending five grand to create an opportunity here, but then the value of an opportunity to you is only two grand, like, one way to look at it is, is, like,

**Marcel Santilli** [00:42:00]
What is the actual real value, actual value of the opportunity?

**Marcel Santilli** [00:42:04]
It's like two grand.

**Marcel Santilli** [00:42:05]
But also the opportunity cost is like if you're creating one here, you don't have to pay five here.

**Marcel Santilli** [00:42:10]
you're actually like creating two in value and say three, you know.

**Marcel Santilli** [00:42:14]
It's actually like 5,000 in value because you're willing to pay 5,000 here, right?

**Ryan Singer** [00:42:19]
No, that's good.

**Ryan Singer** [00:42:20]
what I'm hearing is that like if you were playing the role of the engagement manager, in order for you to make strategic choices around like where to be investing energy in, and according to all those possibilities, you would need to have some kind of a picture like this, which is telling you like these are the content pages that we did.

**Ryan Singer** [00:42:39]
This is our understanding of like how these should be converting to, for example, high intent pages.

**Ryan Singer** [00:42:45]
We're not actually going into GA and like tracking sales contact, right?

**Marcel Santilli** [00:42:51]
That's like something that's happening somewhere else.

**Marcel Santilli** [00:42:54]
A lot of what I just described, this is a simple, I just put a link here.

**Marcel Santilli** [00:43:00]
It's a simplified version of the quote-unquote ROI model.

**Marcel Santilli** [00:43:02]
Uh-huh, yep.

**Marcel Santilli** [00:43:04]
And so that would be built for a client before, right?

**Marcel Santilli** [00:43:11]
And so in a good case scenario like this one, we created this ROI model of like, you know, hey, how many pages we're going to publish?

**Marcel Santilli** [00:43:20]
What is the conversion rate?

**Marcel Santilli** [00:43:22]
What is your level of investment?

**Marcel Santilli** [00:43:23]
How many of those pages?

**Marcel Santilli** [00:43:24]
What is the brand list?

**Marcel Santilli** [00:43:25]
And all of this.

**Marcel Santilli** [00:43:26]
In a good case scenario, right?

**Marcel Santilli** [00:43:31]
And you're saying, here's how we're doing against these projections and what we can measure, you know?

**Ryan Singer** [00:43:37]
Yep, okay.

**Ryan Singer** [00:43:38]
But this is a level up in aggregate from what we started to talk about, which was, I need to be paying attention to the performance of individual pages.

**Ryan Singer** [00:43:48]
What I think this gets us to, if it starts to build some of a model of like, what might be buildable here, is that like, per, it's like,

**Ryan Singer** [00:44:00]
Per page, I've got the inbound piece of this, and I have the intent piece of this, right?

**Ryan Singer** [00:44:11]
Or the progress piece of this.

**Ryan Singer** [00:44:14]
is this up or down in terms of traffic coming in, and is this up or down the reason why we put this page in?

**Marcel Santilli** [00:44:22]
Is that right?

**Marcel Santilli** [00:44:23]
And even before the up and down, it's about visibility, right?

**Ryan Singer** [00:44:27]
What does visibility mean?

**Marcel Santilli** [00:44:30]
Yeah, so, well, actually, let start from the beginning.

**Marcel Santilli** [00:44:36]
First of all, discoverability, right?

**Marcel Santilli** [00:44:38]
If the page doesn't get indexed by Bing and Google, Bing drives a lot of the LLs will never show up anywhere because it's not an index, period, right?

**Marcel Santilli** [00:44:48]
Okay.

**Marcel Santilli** [00:44:48]
And so that's about, like, discoverability.

**Marcel Santilli** [00:44:51]
And once it's discoverable and has been discovered, right, then you have a shot at visibility.

**Marcel Santilli** [00:44:58]
Visibility is going

**Marcel Santilli** [00:45:00]
impressions, if you will, of like, it's there, whether you click it or not, right?

**Marcel Santilli** [00:45:05]
Whether it registers in your browser, and then, but if you have visibility, you have shot by getting a click.

**Marcel Santilli** [00:45:14]
If you don't have visibility, like you don't get impressions, like there's impossible for anybody to click on something they don't see, right?

**Marcel Santilli** [00:45:20]
And then if you have visibility and impressions, then that can potentially drive this thing's like position right.

**Marcel Santilli** [00:45:28]
And then once you get clicks, that's the inbound, up or down.

**Ryan Singer** [00:45:31]
I see.

**Marcel Santilli** [00:45:33]
In the visibility part, Ryan, there is impressions from Google's search, and there is impressions from that lab search, which is super hard to tell.

**Marcel Santilli** [00:45:45]
We essentially have an entire product.

**Ryan Singer** [00:45:47]
Yeah, I remember that.

**Ryan Singer** [00:45:48]
Yeah, uh-huh, good.

**Ryan Singer** [00:45:49]
Okay.

**Ryan Singer** [00:45:51]
Uh-huh, good.

**Ryan Singer** [00:45:52]
Okay.

**Ryan Singer** [00:45:53]
this is just a commentary on how this works, but really, this is, this a thing to be paying attention attention to.

**Marcel Santilli** [00:46:00]
To the extent that you can track it.

**Marcel Santilli** [00:46:01]
No, the discoverability is a stack that we should have as, like, when we do an audit of the webinar.

**Marcel Santilli** [00:46:08]
gets  and then, like, five months later or three months later, you're like, why is no the results?

**Marcel Santilli** [00:46:15]
It's like, there's all these, like, technical little gachas that.

**Marcel Santilli** [00:46:19]
And this is, like, an out-of-mainable stack.

**Ryan Singer** [00:46:22]
you can check from Bing and from Google to see if the data is there.

**Marcel Santilli** [00:46:27]
And that's a stack that we  up ourselves on our product.

**Marcel Santilli** [00:46:33]
Our own product of us doing this, we  up the stack for, like, six weeks.

**Marcel Santilli** [00:46:38]
Yeah, we lost six weeks.

**Marcel Santilli** [00:46:40]
Okay.

**Marcel Santilli** [00:46:41]
And hey, what's happening here?

**Marcel Santilli** [00:46:42]
Why is this, like, zero?

**Marcel Santilli** [00:46:45]
Yeah.

**Marcel Santilli** [00:46:46]
It's like, huh?

**Marcel Santilli** [00:46:48]
Did anyone thought to check this thing?

**Marcel Santilli** [00:46:51]
It's like, oh, , yeah, this is .

**Marcel Santilli** [00:46:53]
Oh, , my bad.

**Marcel Santilli** [00:46:54]
Like, Ryan is doing that all the time.

**Marcel Santilli** [00:46:57]
They change CMSs and then, like, stop it.

**Marcel Santilli** [00:46:59]
Like, a...

**Marcel Santilli** [00:47:00]
I'll give you an example, like, they have a new web agency, and the web agency does a complete revamp on their brand, makes a pretty new website, you know, a mass cold code somewhere that was the thing that was updating your sitemap with new pages, and someone forgot that that existed, and they either broke the sitemap, and now it's a 404, or it's no longer updating with that new pages.

**Marcel Santilli** [00:47:25]
And so now, Google's ways lower, or not at all, indexing that new content, and then no one caught that, because it was like, wow, it's a pretty new website, they must have lot of that.

**Marcel Santilli** [00:47:35]
totally, totally, okay, so, um, I, I, I, I, so, sorry, let me just mention one more one that suits you perfectly, because this one is, like, kind of relevant to this, it's like, another example of this is, like, they accidentally assigned an H3 to what should have been an H1, for example, and now they broke all H1s on all the pages, for example, like, it's a systemic thing.

**Ryan Singer** [00:48:00]
Yeah, so this is all at the implementation level, time.

**Ryan Singer** [00:48:04]
Kind of, right?

**Ryan Singer** [00:48:05]
Like, these are, like, set up problems.

**Marcel Santilli** [00:48:08]
They're not content issues.

**Marcel Santilli** [00:48:10]
They're, like, structure issues.

**Marcel Santilli** [00:48:11]
Yeah, yeah.

**Marcel Santilli** [00:48:12]
Versus, uh-huh.

**Marcel Santilli** [00:48:14]
They're  up everything.

**Marcel Santilli** [00:48:15]
Okay.

**Marcel Santilli** [00:48:16]
you need a healthy page with good hygiene that actually is discoverable to even, like, have a shot at anything else.

**Marcel Santilli** [00:48:26]
matter how, because you can have the mass content in the planet and be  up.

**Ryan Singer** [00:48:31]
Totally.

**Ryan Singer** [00:48:31]
Yeah, totally.

**Ryan Singer** [00:48:33]
Okay.

**Ryan Singer** [00:48:35]
Let me give a little read on where I think we are, and then I want to hand it to you to, like, articulate where you're seeing we are and then figure out what we have to solve together.

**Ryan Singer** [00:48:46]
Okay?

**Ryan Singer** [00:48:48]
The progress I'm kind of seeing here is when we came in to the session today, all I had as input was kind of, like, there's a lot.

**Ryan Singer** [00:49:00]
How to open questions here, you know what I mean?

**Ryan Singer** [00:49:02]
Like, there's all these things we kind of want to know, but like, how do we track it?

**Ryan Singer** [00:49:06]
And like, how do we expose it?

**Ryan Singer** [00:49:08]
And how do we enable the engagement manager to be more proactive, yada, yada?

**Ryan Singer** [00:49:13]
And how do we not let it balloon into becoming Google Analytics or something like that?

**Ryan Singer** [00:49:20]
What I feel like there's a toehold here with this concept, which is like, okay, if we're trying to solve the problem of, this is kind of like, what does it mean to not be flying blind?

**Ryan Singer** [00:49:36]
I think we've unpacked, not flying blind means I'm aware of this per page across the 15 things or the 100 things, and I have like a, I have a quick way to be aware of this, and this is different, this is not generic analytics, this is like, this is, these are the actual things that matter for the system that you're trying to enable to.

**Ryan Singer** [00:50:00]
happen, but it's on a per-page basis, and it sounds like these are things that you know how to wire in terms of what to be tracking at the, at the, there's a, each page, this, if this is the output step, right, or this, if this is the, if this is the, well, this is kind of the, yeah, output and outcome, I always get the mix, if this is the measurement step of what happened in the work, let's say, then every, every page has a history, it came from some strategy, right, like it was written at some point, so there was a moment, if, if any of these things needed to get populated, when there, where there was also like a moment to populate these things, you know, so like what I'm kind of getting to is I'm starting to, I can sort of picture a, like a, but it's like, there are,

**Ryan Singer** [00:51:00]
There are specific things that we thought were strategic to do.

**Ryan Singer** [00:51:04]
Those are pages.

**Ryan Singer** [00:51:06]
Now, like, which of those pages that we put time and energy into as a work step should we be circling back to, you know?

**Ryan Singer** [00:51:14]
And, like, according to these kind of bins of performance that you've described, like, the bins of performance, this I didn't write here, but let me see if I can capture it here.

**Ryan Singer** [00:51:25]
Here, it's like a pass-fail.

**Ryan Singer** [00:51:30]
Either it's broken or it's okay, right?

**Ryan Singer** [00:51:34]
And here, it's – well, I don't know about here, but what I heard, he pushing it up.

**Ryan Singer** [00:51:41]
Or is it still, like, potential but not realized, you know?

**Ryan Singer** [00:51:49]
Is that true across the board from all three of these steps?

**Marcel Santilli** [00:51:54]
Or is that Specific two clicks.

**Marcel Santilli** [00:51:57]
So, um, so what will happen –

**Marcel Santilli** [00:52:00]
happened is, like, you, like, let's say, check that, right?

**Marcel Santilli** [00:52:05]
Because we have 6,000 pages published on the check that.

**Marcel Santilli** [00:52:08]
Check that is our other product.

**Marcel Santilli** [00:52:10]
Yes, check that.ai.

**Ryan Singer** [00:52:12]
that's this.

**Marcel Santilli** [00:52:13]
That's the other product, Yes, yeah.

**Marcel Santilli** [00:52:17]
Yeah, so of those 6,000 pages, 2,800 are now indexed, which took, like, two months.

**Marcel Santilli** [00:52:23]
Now, we're getting about 50,000 or so impressions daily, right?

**Marcel Santilli** [00:52:32]
And, like, in about 30 clicks a day, right?

**Marcel Santilli** [00:52:40]
Across 2,800 pages.

**Marcel Santilli** [00:52:43]
now, what I have to do is I go into Search Console, and I know some URL patterns, right?

**Marcel Santilli** [00:52:52]
Luckily, because we built the site in a way that there's, like, very clear URL patterns.

**Marcel Santilli** [00:52:57]
And I told the team not to  up the URL patterns.

**Marcel Santilli** [00:52:59]
Okay.

**Marcel Santilli** [00:53:00]
And try to reinvent the wheel.

**Marcel Santilli** [00:53:02]
like for instance, any page that's related to pricing, there's the word pricing.

**Marcel Santilli** [00:53:06]
it's very, that's why I'm doing it.

**Marcel Santilli** [00:53:08]
I want to see how pricing pages are performing compared to the overall when it comes to click-through rates, right?

**Marcel Santilli** [00:53:18]
Okay.

**Marcel Santilli** [00:53:19]
And then when I apply that filter, then I go, okay, now let me turn it on and off that filter real quick, which is a pain in the .

**Marcel Santilli** [00:53:28]
And then I also do comparisons in time periods, right?

**Marcel Santilli** [00:53:32]
last seven days versus current seven days and those types of things.

**Marcel Santilli** [00:53:37]
And then I look at all that and I try to come to some pages, you know, given we've only done 100 pricing pages and we've done 5,000 brand pages and pricing pages is driving 50% of our clicks.

**Marcel Santilli** [00:53:51]
And on top of that, pricing pages grew where brand pages week over week are splashed.

**Marcel Santilli** [00:53:58]
That tells me to...

**Marcel Santilli** [00:54:00]
Probably doubled down on doing way more volume on pricing pages as opposed to trying to, like, improve the brand pages right now.

**Marcel Santilli** [00:54:08]
Like, that's a hypothesis whether it's right or not, we see spending 30 minutes acting around with it filters back and forth and seeing correlation of, like, mostly driving around what to do about the current pages or how to prioritize the next batch of what we're going to do.

**Ryan Singer** [00:54:23]
Was that a story about impressions or clicks?

**Marcel Santilli** [00:54:26]
It's a story about we're getting a ton of impressions and very little clicks right now on the site, and we're creating a ton of pages still, and we're trying to figure out what to do to get clicks to go up at a higher pace.

**Ryan Singer** [00:54:41]
Okay, I see.

**Marcel Santilli** [00:54:44]
Which means you want to find within your clicks what cohort of types of pages, like, are driving more growth in clicks and better click-through rates.

**Marcel Santilli** [00:54:59]
Okay.

**Marcel Santilli** [00:55:00]
that's just an example of the types of, like, I have to go into an analytics tool, apply a bunch of filters, but then the problem is both GA and GSC, they give you a URL, that's it.

**Marcel Santilli** [00:55:12]
They don't give you not even the page title, don't give you the content type, they don't give you anything.

**Marcel Santilli** [00:55:16]
They certainly don't tie it back to the work you did based on URL patterns only, and that's the only field I have available to me in all these tools.

**Marcel Santilli** [00:55:25]
And there's more around that as well, that's, like, sometimes you're not even getting searched, like, there is no impression.

**Marcel Santilli** [00:55:33]
Sometimes you might be doubling down on a topic, there is no search intent, and you get no impressions, and sometimes you get the impressions, and you don't get the clicks, because you're not on the first page, or maybe your meta description sucks, or your title is not properly.

**Marcel Santilli** [00:55:49]
isn't it, like, there is that split between, like, getting impressions, and then acting on impressions, you know?

**Marcel Santilli** [00:55:56]
Yeah, okay.

**Marcel Santilli** [00:55:59]
you

**Marcel Santilli** [00:56:00]
Your intuition of splitting between pages being the core thing to track and having these special phases and things that matter on the page is literally how we're thinking as well.

**Marcel Santilli** [00:56:11]
let me start mapping an entire system that's essentially a CRM for pages, where you have the whole lifecycle of the page and put all the potential problems with the pages and all that.

**Ryan Singer** [00:56:22]
Yeah.

**Marcel Santilli** [00:56:25]
Okay.

**Marcel Santilli** [00:56:26]
And I think, like, let me just add a quick tension here that's important to note, is that clients, for the most part, the ones that sign the contract and decide to work or not, they want to know that things are improving.

**Marcel Santilli** [00:56:42]
They really don't want to do this work on the per page level.

**Marcel Santilli** [00:56:46]
They wish they could track it on a per page level, and they want it done and improved.

**Marcel Santilli** [00:56:51]
They're really the only thing they want to, like, see.

**Marcel Santilli** [00:56:57]
Like, and I'm distinguishing here being...

**Marcel Santilli** [00:57:00]
using operator and stakeholder, page per page to see, hey, there's 37 pages of broken links.

**Marcel Santilli** [00:57:09]
What they want to know is that on average, we're fixing things that correlate to the impact, and they want to see the aggregate.

**Ryan Singer** [00:57:14]
then there's this extension of like, you need to be able to see this in order to do the work that impacts the results.

**Marcel Santilli** [00:57:21]
But if you don't create a view of the aggregate results, aka the big picture, they're eventually not going to renew.

**Ryan Singer** [00:57:28]
But the big picture is going to look bad.

**Ryan Singer** [00:57:31]
Of course, of course.

**Ryan Singer** [00:57:32]
this is the, you have to do the per page work at an implementation level in order to, this is where you can do the tuning in order to actually create the outcome here.

**Ryan Singer** [00:57:45]
If you don't do this, this is what, this is flying blind.

**Ryan Singer** [00:57:48]
Yes.

**Ryan Singer** [00:57:48]
But if you do this, you're not flying blind, and then you're able to create an, you're able to create an aggregate up or down here.

**Marcel Santilli** [00:57:54]
Yeah.

**Marcel Santilli** [00:57:55]
like, imagine like, everybody, one of our customers has 19,000 pages, and we can do

**Marcel Santilli** [00:58:00]
Go to them and say, hey, you, your aggregate, like, health score on all your pages used to be 62 last week, and we increased to 70% across all your 19,000 pages.

**Marcel Santilli** [00:58:14]
Like, if that's all we did, and if we never connected back to, like, and that has a tendency to have, and we could never prove that, if they'll be like, I don't care, like, we'll still get a term, and we don't care, you know?

**Marcel Santilli** [00:58:30]
Or, it feels like we should care, but, like, so what?

**Marcel Santilli** [00:58:33]
Like, it's worth nothing to me, because I still need to see this other thing up to the right.

**Ryan Singer** [00:58:38]
How does, so what is this today, this aggregate view?

**Ryan Singer** [00:58:41]
Is this something that the engagement manager is kind of making bespoke for them, like, at certain key moments?

**Ryan Singer** [00:58:47]
Or, like, what, does this not exist in any form?

**Marcel Santilli** [00:58:49]
like, is this, like, I don't know.

**Marcel Santilli** [00:58:51]
Like, when done right, at the bare minimum, it's, like, search traffic.

**Marcel Santilli** [00:59:02]
And LLM traffic to pages we worked on, and overall search traffic and overall LLM traffic, right?

**Ryan Singer** [00:59:10]
That's the bare minimum, ideally.

**Marcel Santilli** [00:59:12]
And often that bare minimum is not even recorded, even when it's set up, it's not reported regularly.

**Ryan Singer** [00:59:18]
And so, like, customers don't know what is happening.

**Marcel Santilli** [00:59:23]
And in the best case scenario, it's that and connected to your conversion or whatever thing they care about, right?

**Marcel Santilli** [00:59:33]
Like, sign up, could be, you know, sales lead.

**Marcel Santilli** [00:59:36]
could be something that proves to them that they're, like, you know, that there's, like, unit.

**Marcel Santilli** [00:59:43]
That we have these weekly meetings with clients, and our team is so operational that they forget to tie back to the high level that we're talking about.

**Marcel Santilli** [00:59:54]
yeah.

**Marcel Santilli** [00:59:55]
They forget to, like, hey, usually the updates will go something like that.

**Marcel Santilli** [01:00:00]
Hey, here's the five pages we worked on last week.

**Marcel Santilli** [01:00:04]
These are the five we're prioritizing for this week.

**Marcel Santilli** [01:00:06]
Any questions?

**Ryan Singer** [01:00:08]
Updates from engagement managers to clients are operational.

**Ryan Singer** [01:00:14]
Here are the five pages we worked on.

**Ryan Singer** [01:00:18]
the concern here is that there's like missed opportunities for that.

**Ryan Singer** [01:00:23]
There's churn risk here and there's missed opportunities for retention because you're not communicating the right things back to the client.

**Ryan Singer** [01:00:30]
You're not doing the right things in terms of actually producing the outcome.

**Ryan Singer** [01:00:34]
that requires monitoring the pages correctly.

**Ryan Singer** [01:00:36]
But also then you have to be able to tell it to the client and talk at the right level.

**Marcel Santilli** [01:00:42]
I'll give you a very clear example of this.

**Marcel Santilli** [01:00:45]
augment code, up to the right, metrics look great.

**Marcel Santilli** [01:00:49]
And then somewhere along the way, like two pages that we had were driving like 80% of the traffic.

**Marcel Santilli** [01:00:56]
Right.

**Marcel Santilli** [01:00:57]
And those pages in one of those weeks.

**Marcel Santilli** [01:00:59]
Right.

**Marcel Santilli** [01:01:00]
It's In hindsight, we looked at it, right?

**Marcel Santilli** [01:01:04]
And it declined in traffic, not by a huge amount, but it declined a little.

**Marcel Santilli** [01:01:08]
And then the next week, it declined by a lot.

**Marcel Santilli** [01:01:10]
And then the next week, it stayed low.

**Marcel Santilli** [01:01:13]
And along the way, no one of you can spend a minute saying, hey, the top two pages, both declined in the same week.

**Marcel Santilli** [01:01:23]
And then continued with the client a week later, systematically, what the ?

**Marcel Santilli** [01:01:29]
Like, we should probably do something about it.

**Marcel Santilli** [01:01:31]
And if we had communicated that to the client first, and you caught it for the next two weeks, and just go make those pages  perfect, right?

**Marcel Santilli** [01:01:38]
Instead, the client didn't catch it, we didn't catch it, and we just said that, hey, results don't look up to the right this week, but you're never going to be always up to the right.

**Marcel Santilli** [01:01:48]
And that was like our conclusion.

**Marcel Santilli** [01:01:49]
You know, and we can't do it the same thing.

**Marcel Santilli** [01:01:52]
just kept publishing five more, five more, ten more, twenty more, twenty more, twenty more, you know, and that's it.

**Ryan Singer** [01:01:58]
Mm-hmm, mm-hmm.

**Ryan Singer** [01:02:00]
Okay.

**Ryan Singer** [01:02:03]
when we part of the challenge of the original of the brief that I had from Daniel, there was this kind of question around like, how much of this is around like, reporting, reporting of metrics, how much of this is about like AI to actually tell you what to be changing or what to be thinking about differently.

**Ryan Singer** [01:02:23]
And like what I'm hearing is that like the, this is more about surfacing the right things so that you can put that in front of an engineering manager and engagement manager and have them follow the guidance that you give them as opposed to like the AI like giving you the strategy.

**Ryan Singer** [01:02:46]
It sounds like this is less about like giving me the strategy of how to act on this and more about like there's major, major basics here, you know, like, like, so it's almost like there's a, there's a view of like, like,

**Ryan Singer** [01:03:00]
EM, talk to the client about this.

**Ryan Singer** [01:03:04]
EM, monitor and fix this.

**Marcel Santilli** [01:03:09]
Yeah.

**Marcel Santilli** [01:03:11]
We don't need to tell them, like, hey, I need you to change the H1 from X to Exactly.

**Marcel Santilli** [01:03:19]
It's more of like, hey, these 20 pages are getting murdered over here.

**Marcel Santilli** [01:03:26]
That's it.

**Marcel Santilli** [01:03:26]
Like, and then, like, that is way easier to train our exams on than right now being like, hey, did you look at the Looker dashboard?

**Ryan Singer** [01:03:35]
Well, I did, but it's been broken for two weeks and no one fixed Totally.

**Marcel Santilli** [01:03:38]
It's like, okay, hey, did you do, you know, like, we have to, like, have a 20 checklist of, like, things that could go wrong in order for them to even have to know what to look at us, you know?

**Marcel Santilli** [01:03:49]
I think to keep in mind as well is that all the challenges that we deal with internally is the same in your own company.

**Marcel Santilli** [01:03:56]
Yes.

**Marcel Santilli** [01:03:57]
So, like, so this is not just the fact that we're...

**Marcel Santilli** [01:04:00]
We're doing this consulting work, but we're eating the same problems that it would be if you had a lower level of director.

**Ryan Singer** [01:04:08]
We have that.

**Ryan Singer** [01:04:09]
We want check that.

**Ryan Singer** [01:04:10]
Check that is a perfect example.

**Marcel Santilli** [01:04:11]
It's internal product.

**Marcel Santilli** [01:04:12]
We are a company that does this for a living.

**Marcel Santilli** [01:04:15]
Our own team misses the boat on the same, on finding the right clusters, fixing the health problems.

**Marcel Santilli** [01:04:23]
even though we're thinking about YAMs, I think we should think about as well, if this was self-operated and like a marketing team signed out on another company, that is the kind of level of visibility that they would need as well.

**Marcel Santilli** [01:04:39]
That's why Marcel is always doing this internally.

**Marcel Santilli** [01:04:41]
But for him, it's always just like one tool, like one air table from one area and he knows how to do it.

**Marcel Santilli** [01:04:48]
Yeah, like let me give you like an example here that's like relevant.

**Marcel Santilli** [01:04:53]
when I was at IBM, I worked with this guy, Brian Casey.

**Marcel Santilli** [01:04:58]
He's awesome.

**Marcel Santilli** [01:04:59]
Now...

**Marcel Santilli** [01:05:00]
A lot of the work we did kind of informed the way he thought about it, and now he owns all of IBM.com.

**Marcel Santilli** [01:05:06]
And over the years, they essentially consolidated from like a 30 million page site to like a very content-happy page, and he's out more than 10x to traffic.

**Marcel Santilli** [01:05:17]
Last time talked to him, he essentially said he has an Airtable that has Airtable, they have an entire engineering team that has over 500 different columns, if you will, of processes that run on those pages.

**Marcel Santilli** [01:05:34]
There are like enrichment processes, monitoring processes, and things like that.

**Marcel Santilli** [01:05:38]
And that's literally their like data layer and contextual layer on top of their CMS.

**Marcel Santilli** [01:05:43]
It's not their CMS.

**Marcel Santilli** [01:05:44]
Yes.

**Marcel Santilli** [01:05:44]
They pull from their CMS, and then they do all these other things.

**Ryan Singer** [01:05:47]
this is what they built, and there's a team of 100 people on their hand right now.

**Marcel Santilli** [01:05:51]
Yes.

**Marcel Santilli** [01:05:52]
That just that, right?

**Marcel Santilli** [01:05:53]
And that informs the strategy, it informs the work, informs everything.

**Marcel Santilli** [01:05:57]
And that was like kind of my original.

**Marcel Santilli** [01:06:00]
like, oh , I think there's something there.

**Marcel Santilli** [01:06:02]
And so for us, this is a, let's not go boil the ocean there, but it's the, this is kind of like the foundation that should inform everything else.

**Marcel Santilli** [01:06:11]
CMSs have no contextual layers, they have no analytics, they're truly just like a, like a stupid, essentially, that then gets like rendered on a website based on the source code, right?

**Marcel Santilli** [01:06:26]
And then the analytics is like this thing in a vacuum that just looks at URLs, essentially, you know, and your CRM's over here with all this data, and then all the work that's happening is the same Google Doc over there, you know?

**Marcel Santilli** [01:06:38]
And it's like, this is crazy that that's your most, how do you manage your most valuable asset, right?

**Marcel Santilli** [01:06:43]
you're paying $500,000 a month to drive traffic to this thing, you're paying $50,000 a month for a web agency to make it look pretty, and you're paying another $20,000 a month for a CMS to hold all the fields.

**Marcel Santilli** [01:06:54]
And then like, and now you're paying us $25,000 a month to do that work?

**Marcel Santilli** [01:06:59]
Totally.

**Ryan Singer** [01:07:00]
the page is actually like the unit where this all threads together, like where the content in the CMS, the analytics from Google Analytics, the strategy coming in from the original Airtable or whatever, like the page is the unit where this all like lives or dies and plays out and, Exactly.

**Marcel Santilli** [01:07:18]
Yeah.

**Marcel Santilli** [01:07:22]
And like this thing is like only recently I think it's really connected as clearly because it's like we're approaching all these other stuff like the workflows and all those other things and I think like recently, at least in our habits, it's like pages are in.

**Marcel Santilli** [01:07:39]
Totally.

**Ryan Singer** [01:07:40]
Websites don't exist without pages, right?

**Ryan Singer** [01:07:42]
Yeah.

**Ryan Singer** [01:07:42]
The web page is just like the, like the chassis for like the page to be plugged in somewhere.

**Marcel Santilli** [01:07:49]
Yeah.

**Marcel Santilli** [01:07:50]
And the website is important because it's like it influences everything else, right?

**Marcel Santilli** [01:07:56]
It influences everything.

**Marcel Santilli** [01:07:58]
It's the thing you can.

**Marcel Santilli** [01:07:59]
Yeah.

**Marcel Santilli** [01:08:00]
With a certainty measure, you can't always measure things in social and other things, right?

**Marcel Santilli** [01:08:05]
Yeah.

**Marcel Santilli** [01:08:06]
And it's what you control the most.

**Marcel Santilli** [01:08:08]
And it's where most transactions still happen today, right?

**Marcel Santilli** [01:08:11]
And so it's like the most overlooked one because like the CMS layer is trying to be like the design layer, you know?

**Marcel Santilli** [01:08:20]
And anyways, so that's why we have so much conviction in this.

**Marcel Santilli** [01:08:24]
But it's super messy because it's hard not to boil the ocean here, right?

**Marcel Santilli** [01:08:28]
There's so many points of ingestion and things, you know?

**Ryan Singer** [01:08:32]
Mm-hmm.

**Ryan Singer** [01:08:33]
Okay.

**Ryan Singer** [01:08:36]
What?

**Ryan Singer** [01:08:40]
Let me think here.

**Ryan Singer** [01:08:41]
what I think we can do, I think we're all kind of like envisioning the same thing now, you know?

**Ryan Singer** [01:08:48]
Which is this kind of like almost like I think like this Airtable you described with a million columns for every page, which it kind of like summarizes, that's this idea, right?

**Ryan Singer** [01:09:00]
Like, the per page, what happened?

**Marcel Santilli** [01:09:04]
That's like what I would build, right?

**Marcel Santilli** [01:09:07]
Literally, that's the path I was in building before building the real text.

**Marcel Santilli** [01:09:11]
It's like a near table for what I  on the column.

**Ryan Singer** [01:09:15]
Yeah, yeah.

**Ryan Singer** [01:09:17]
So, but the concept here is that there's like a, it's like a, it's the page, it's a page analytics, not URL.

**Marcel Santilli** [01:09:30]
Right, yes.

**Ryan Singer** [01:09:32]
And page analytics has a more specific meaning that is a narrower thing than just general analytics.

**Ryan Singer** [01:09:38]
it's, and we sort of dug a little bit into what that means.

**Ryan Singer** [01:09:43]
There is an aggregate of that, which I think is an important part of the story here, right?

**Ryan Singer** [01:09:48]
Because if you only improve the page story and you don't have the aggregate view, there's the concern that the engagement manager isn't having the right conversation with the client.

**Ryan Singer** [01:09:59]
Yeah.

**Ryan Singer** [01:09:59]
Yeah.

**Marcel Santilli** [01:10:00]
like the portfolio view is that it's like an aggregate portfolio view versus like just a copy and paste of Google Analytics, right?

**Marcel Santilli** [01:10:10]
Because like there's a lot like this is meant to be the aggregate, I think, of the per page.

**Marcel Santilli** [01:10:19]
And like I'll give you an example, like, yes, your stock is down 20%, but the whole market was down 40%.

**Marcel Santilli** [01:10:25]
And we did all these effing things that mitigated our downside risk.

**Marcel Santilli** [01:10:31]
You should be literally upping our content right now, even though you're down 20%.

**Ryan Singer** [01:10:36]
You know what I mean?

**Ryan Singer** [01:10:38]
Okay, I think we can come back to that.

**Ryan Singer** [01:10:41]
Here's an idea about maybe what the work is here now in this session.

**Ryan Singer** [01:10:47]
It sounds like you, we can picture this from a front-end perspective, but what I'm hearing is like, is this actually something that you, we can go build that.

**Ryan Singer** [01:11:00]
Isn't boiling the ocean in the sense of like, do we have to build an, like, is there some actual short path to having this in a productized way that isn't rebuilding Google Analytics, right?

**Ryan Singer** [01:11:14]
Is that, do I understand, right?

**Ryan Singer** [01:11:15]
That's kind of like what the next question is here.

**Marcel Santilli** [01:11:18]
It's like, so the thing is, like, two days ago, like, so this is very, very recent, right?

**Marcel Santilli** [01:11:28]
Like, I did some.

**Marcel Santilli** [01:11:30]
Shaping on the page level stuff, right?

**Ryan Singer** [01:11:34]
But it's very, like, you know, two days old, essentially.

**Marcel Santilli** [01:11:44]
And I think, like, we're a little bit, like, I don't want say stuck, but, like, thoughtfully making sure that we don't, like, kind of boil the ocean is that even within this, There's that button.

**Marcel Santilli** [01:12:00]
And of like, whoa, like this, like, you know, like the health score, like that argument in it.

**Ryan Singer** [01:12:07]
Oh, yeah, yeah, this is, this is, uh-huh.

**Ryan Singer** [01:12:11]
I can, okay.

**Ryan Singer** [01:12:13]
hold on, but what are we, what am I looking at here?

**Ryan Singer** [01:12:17]
This is, this is something that you hacked together?

**Marcel Santilli** [01:12:20]
This is a prototype that I pulled together, you know, and so this is, I'm just a second to go to the main view.

**Marcel Santilli** [01:12:27]
this is like, you know, essentially like a high-level prototype of, here's a big picture of all the pages on your site.

**Ryan Singer** [01:12:36]
this is from one, we're looking, we're looking at one client right now.

**Marcel Santilli** [01:12:40]
Correct.

**Ryan Singer** [01:12:40]
Yeah, yeah.

**Marcel Santilli** [01:12:41]
Okay.

**Ryan Singer** [01:12:42]
And then we've got pages.

**Marcel Santilli** [01:12:44]
Okay.

**Marcel Santilli** [01:12:45]
Uh-huh.

**Marcel Santilli** [01:12:45]
And then pages, right, would be the ones that essentially like we're crawling based on your site map, right?

**Ryan Singer** [01:12:52]
Okay.

**Marcel Santilli** [01:12:53]
Or that we're watching somehow, or like groups of pages that we care about, essentially, because like, you know, we might not.

**Marcel Santilli** [01:13:00]
I want to track a million pages if your site has a million pages.

**Marcel Santilli** [01:13:03]
Yes.

**Marcel Santilli** [01:13:03]
And then, like, where I started this whole thing was here, which was like, hey, how do I think about simplifying the, like, the attributes, if you will, that then give me a performance score, some kind of score of a page, right?

**Marcel Santilli** [01:13:20]
Because, like, no one can make sense of, like, stuff like this.

**Marcel Santilli** [01:13:24]
Like, okay, like, don't tell me, like, there's 75 technical things I need to work.

**Marcel Santilli** [01:13:30]
Yeah, what is, like, do want to go up or down on average, right?

**Marcel Santilli** [01:13:33]
Is it healthy or not or whatever, right?

**Ryan Singer** [01:13:35]
this is across all pages or what?

**Marcel Santilli** [01:13:39]
This view right here is for this one page individually.

**Ryan Singer** [01:13:43]
Ah, you just clicked into a page.

**Ryan Singer** [01:13:45]
I just clicked into a The page is how to scale your SaaS business.

**Marcel Santilli** [01:13:48]
I see.

**Marcel Santilli** [01:13:49]
Yeah, so this is, like, let's assume you have 5,000 of these, right?

**Marcel Santilli** [01:13:54]
right.

**Marcel Santilli** [01:13:55]
Essentially, like, today, if doing a workspace setup, the idea of flow would be, like, first, you know,

**Marcel Santilli** [01:14:00]
Understand the client, the personas, analyze all that, and then create the writing agent last time.

**Marcel Santilli** [01:14:05]
Then the fourth step would be like, plug in your analytics, then collect all the data from GA and Google Search Console, and then you also plug in your website.

**Marcel Santilli** [01:14:12]
then we just collect all your pages.

**Marcel Santilli** [01:14:14]
And that index of pages that Marcel is showing is what we scraped out of your website and combined with GA and GST, and now we have this.

**Marcel Santilli** [01:14:27]
think of this as like, let's say you have a portfolio of 81 pages, and of those pages, let's say 13, I don't know if these numbers are wrong, but let's just say 13 or green, 7 or yellow, and whatever is red.

**Marcel Santilli** [01:14:49]
And so your average aggregate portfolio score is this.

**Marcel Santilli** [01:14:53]
And in health there, what Marcel means is the indexability, discoverability, and then quality.

**Marcel Santilli** [01:14:59]
Yep, totally.

**Marcel Santilli** [01:15:00]
Those are all different steps of that funnel that you were drawing, you know?

**Marcel Santilli** [01:15:03]
Yeah.

**Marcel Santilli** [01:15:04]
Yeah.

**Marcel Santilli** [01:15:05]
And so, like, so then, like, the help is the vitals of the page.

**Marcel Santilli** [01:15:11]
It's super slow.

**Ryan Singer** [01:15:12]
And then the discoverability, right?

**Ryan Singer** [01:15:14]
Got it.

**Ryan Singer** [01:15:14]
this is kind of like if something's wrong with the page, you want to dig into the detailed metrics so that you can maybe start to debug it, right?

**Ryan Singer** [01:15:22]
But you're not looking at these detailed metrics to determine if it's healthy or not.

**Marcel Santilli** [01:15:26]
This is more like where's the problem?

**Marcel Santilli** [01:15:29]
Yeah.

**Marcel Santilli** [01:15:29]
And most of these tend to be systemic.

**Marcel Santilli** [01:15:32]
Right.

**Marcel Santilli** [01:15:32]
Well, like, not page level, but you want to show it on a page level because sometimes there might be things.

**Marcel Santilli** [01:15:37]
Yeah.

**Marcel Santilli** [01:15:37]
that's a lot of put in the image there.

**Marcel Santilli** [01:15:39]
Yeah.

**Marcel Santilli** [01:15:39]
That's, like, not our work day to day.

**Marcel Santilli** [01:15:42]
That's more of, like, hey, our work won't have an impact if you don't go fix this , you know?

**Marcel Santilli** [01:15:46]
Yeah.

**Marcel Santilli** [01:15:47]
Yeah.

**Marcel Santilli** [01:15:49]
Yeah.

**Marcel Santilli** [01:15:50]
Okay.

**Marcel Santilli** [01:15:50]
And then the quality is the, like, you know, the intent of this is, like, how do we not boil the ocean?

**Marcel Santilli** [01:15:56]
And this is, like, today, even if you had just a very...

**Marcel Santilli** [01:16:00]
Very basic.

**Marcel Santilli** [01:16:00]
You took the scrape of every page and you took the context we have today and you just did one shot LLM call to just be like, is this good?

**Marcel Santilli** [01:16:10]
Is this relevant?

**Ryan Singer** [01:16:11]
Is this decent?

**Marcel Santilli** [01:16:13]
Does it have an H1?

**Marcel Santilli** [01:16:14]
You just ran a very basic call.

**Marcel Santilli** [01:16:16]
It would be obscenely valuable to customers and customers would pay for even that because for them to do that, they would have to set up our scraping pipeline, which is pretty hard to do.

**Marcel Santilli** [01:16:24]
They would have to like do a bunch of other things that are pretty hard and then they would have to put it in an air table and then have that air table run on the set every day and not save the historical backfield either, you know?

**Marcel Santilli** [01:16:36]
like, and then the visibility where it starts to get tricky because now it's like, hey, there's keyword level, then like this is like hard to figure out because there's like AI visibility and search visibility.

**Marcel Santilli** [01:16:52]
There's a lot here and then traffic is more straightforward because like you're either getting traffic or not and there's traffic.

**Marcel Santilli** [01:17:00]
Already comes with what the source of the traffic is.

**Marcel Santilli** [01:17:02]
it's pretty straightforward to say how much is it coming from search and things like that.

**Marcel Santilli** [01:17:06]
And it's also easier to say, hey, now that we have the context of this page, we know this page is a how-to page.

**Marcel Santilli** [01:17:16]
And we know this page is in the slash blog directory.

**Marcel Santilli** [01:17:19]
now you can later on drive insights of like, on average, pages and slash blogs get, you know, this.

**Marcel Santilli** [01:17:27]
And this is doing better or worse than the average for that kind of payoff, you know.

**Marcel Santilli** [01:17:32]
then you can, you know, that.

**Marcel Santilli** [01:17:35]
And then engagement and conversion can be like a future thing.

**Marcel Santilli** [01:17:39]
But I wanted to kind of like put it here because like...

**Marcel Santilli** [01:17:42]
Engagement we can track today already as well, based on Google Analytics.

**Marcel Santilli** [01:17:45]
That's like a time on page.

**Marcel Santilli** [01:17:47]
That would be the main engagement.

**Marcel Santilli** [01:17:49]
And the way to think about it is like a lot of these things, there's like...

**Marcel Santilli** [01:17:54]
There's a super simplistic thing, which is like, hey, this weighs 15%.

**Marcel Santilli** [01:17:58]
And this is like the things...

**Marcel Santilli** [01:18:00]
And it's very like, you know, very straight cut way to do it.

**Marcel Santilli** [01:18:04]
And even within those, there is a overall best practice in the world.

**Marcel Santilli** [01:18:08]
And then there's like in relation to the rest of your site.

**Marcel Santilli** [01:18:11]
And then there's a in relation to lookalike pages within your site, right?

**Marcel Santilli** [01:18:15]
Like, so there's some tradeoff decisions there of like, you know, this bounce rate looks horrendous, but this bounce rate is actually like the best you got on your whole site, you know?

**Ryan Singer** [01:18:25]
Yeah, yeah.

**Marcel Santilli** [01:18:25]
Yeah, the comparison across pages, sometimes the comparison across pages is what you actually need to see per page in order to know what it means.

**Ryan Singer** [01:18:33]
Yeah, yeah, yeah.

**Marcel Santilli** [01:18:36]
like, just this alone is just like, just explaining this matrix, it's gnarly, you know?

**Marcel Santilli** [01:18:42]
And we're doing this at the page level, and you saw how long, like, you were, you're picking this up faster than anybody that would have on your site.

**Marcel Santilli** [01:18:52]
like, the clients and the users of this have to pick up, so this page alone, we need a lot of work.

**Marcel Santilli** [01:18:58]
Yeah, and then like today,

**Marcel Santilli** [01:19:01]
today, the actual life experience is this.

**Marcel Santilli** [01:19:05]
This is our analytics.

**Ryan Singer** [01:19:06]
This is our analytics.

**Marcel Santilli** [01:19:07]
Oh, man.

**Ryan Singer** [01:19:08]
URLs.

**Marcel Santilli** [01:19:09]
Yeah.

**Ryan Singer** [01:19:09]
It's traffic, which is this, which I also like.

**Ryan Singer** [01:19:12]
yeah.

**Ryan Singer** [01:19:12]
It's all, it's all, yeah, it's all detached.

**Marcel Santilli** [01:19:15]
It's all detached from the work.

**Marcel Santilli** [01:19:18]
pages look like this, which is just like a dump on 19,000 pages.

**Marcel Santilli** [01:19:22]
And like, I have no idea what any of this.

**Ryan Singer** [01:19:25]
Dude, this is such a no-brainer.

**Marcel Santilli** [01:19:27]
I love this.

**Marcel Santilli** [01:19:27]
I love this project.

**Ryan Singer** [01:19:28]
I think this is amazing.

**Ryan Singer** [01:19:30]
This is such a no-brainer.

**Ryan Singer** [01:19:32]
I love it.

**Marcel Santilli** [01:19:34]
Oh, yeah.

**Marcel Santilli** [01:19:35]
how do we take where we are today and not boil the ocean so that we can get something deployed to all our workspaces in the next six weeks?

**Ryan Singer** [01:19:43]
I love it.

**Ryan Singer** [01:19:44]
Okay.

**Ryan Singer** [01:19:44]
let me see if I understood the problem right.

**Marcel Santilli** [01:19:47]
Now that we've talked it all through, it sounds like when you're saying boil the Can I do just a quick bio break?

**Ryan Singer** [01:19:53]
Unless you're like really.

**Ryan Singer** [01:19:54]
No, this is perfect time.

**Ryan Singer** [01:19:55]
Let's do, let's do, let's take five, all of us.

**Ryan Singer** [01:19:58]
And then, and then we'll do second.

**Ryan Singer** [01:20:00]
Chapter is like what to do next, now that we're on on the problem.

**Marcel Santilli** [01:20:04]
Awesome.

**Marcel Santilli** [01:20:04]
Awesome.

**Marcel Santilli** [01:20:05]
Makes sense.

**Marcel Santilli** [01:20:30]
Thank

**Marcel Santilli** [01:22:00]
Thank you.

**Marcel Santilli** [01:22:36]
Thank you.

**Marcel Santilli** [01:23:02]
Yeah, it's like, the, I was talking to, I went to the wars game with Mario yesterday, um, but, um, but dude, like, I was kind of like, telling him, kind of like, the pitch here of this, and he's like, this is like, it's impossible to set this up in a table, and it's like, setting it up in a table is gnarly, because you don't have a schedule to run things, they don't work on a schedule, you know, and so, so it's just like, there's no way to build this, there's just no way to build it, and all the other things we built, add up to being able to do this, and so it's kind of like, really like, we took the right approach, and so like, we have this edge right now, and like, just having checked that as well, opens up the opportunity for this 50% part of this is in the no bias act.

**Marcel Santilli** [01:23:58]
Yeah, and Ryan, like,

**Marcel Santilli** [01:24:00]
What I was saying is like, this is such a massive opportunity and it's like everything here, first of all, wouldn't be possible if we didn't have like the output AI framework of like that we built, essentially how we execute workflows, right?

**Marcel Santilli** [01:24:16]
Yes.

**Marcel Santilli** [01:24:17]
And none of this wouldn't have been possible if we didn't have already like an ability and know-how and pattern recognition and all this stuff, right?

**Marcel Santilli** [01:24:26]
And today, if you're a company like IBM or any of our customers, if you're trying to like say, if you realize this is a problem, right, and you're already investing all this money onto your website, essentially, and driving traffic to your website.

**Marcel Santilli** [01:24:41]
it's like, it's an easy like leap to go from that to like, yeah, I should probably like manage this asset, right, this group of assets.

**Marcel Santilli** [01:24:48]
Then like if you're trying to like get a hold of this and understand all of this, it's like really hard to do this.

**Marcel Santilli** [01:24:53]
It's like the options are like use clay.com and you build a row there and you use one.

**Marcel Santilli** [01:25:00]
One single LLM call and it's like really like hacky or you legit build it from end to end, which would be crazy.

**Marcel Santilli** [01:25:06]
Or you build it on top of an Airtable, which has integrations, but then like it's a pretty gnarly problem that like should be solved and there's a lot of value in solving.

**Ryan Singer** [01:25:17]
It's huge.

**Ryan Singer** [01:25:18]
It's huge.

**Ryan Singer** [01:25:19]
for me, like I feel like this is when what we've been talking about today is actually like it's almost like it's the spine of the whole everything that you do.

**Ryan Singer** [01:25:29]
You know, it all runs through the page actually.

**Ryan Singer** [01:25:32]
And, um, uh, it's what you're actually doing is like, this is what like gets me excited about this company, what you guys are doing is like, you're actually a vertical integrator.

**Ryan Singer** [01:25:46]
like what you're really doing is like, like you're like all these horizontal layers exist.

**Ryan Singer** [01:25:54]
This missing thing is what is the vertical thing that drives you down through it so that it all means something and works.

**Ryan Singer** [01:26:00]
And the page is actually the vertical line through the whole stack.

**Ryan Singer** [01:26:06]
It's the thing you have to have a strategy for.

**Ryan Singer** [01:26:09]
It's the thing you have to write.

**Ryan Singer** [01:26:10]
It's the thing that you have to check for voice.

**Ryan Singer** [01:26:12]
It's the thing that performs or doesn't perform.

**Ryan Singer** [01:26:15]
You know what I mean?

**Ryan Singer** [01:26:16]
It's like everything centers on the page.

**Marcel Santilli** [01:26:19]
And you know what's crazy?

**Marcel Santilli** [01:26:20]
It's like because we chose to have a service delivery model up front, we didn't corner ourselves into anything.

**Marcel Santilli** [01:26:30]
And we got like way more insights to come to this conclusion now in addition to like years of working related to this.

**Marcel Santilli** [01:26:37]
Whereas like none of our potential competitors out there, one, have been built in the last year or can arrive at this conclusion very easily because like they're cornered themselves as like, hey, if you're building an analytics tool, you're going to be an analytics tool.

**Marcel Santilli** [01:26:53]
And now you corner yourself into an analytics tool.

**Ryan Singer** [01:26:55]
You know what I mean?

**Ryan Singer** [01:26:56]
That's the horizontal trap.

**Ryan Singer** [01:26:57]
Everybody's making the horizontal thing.

**Ryan Singer** [01:26:59]
Or this, I'm the CM.

**Ryan Singer** [01:27:00]
No, I'm the analytics tool.

**Marcel Santilli** [01:27:01]
No, I'm the strategy piece.

**Marcel Santilli** [01:27:03]
it's it's it's customers care about outcomes and services is the only thing that solves for outcomes today.

**Marcel Santilli** [01:27:11]
Exactly.

**Ryan Singer** [01:27:11]
you don't get paid unless you deliver outcomes, you know, exactly, exactly.

**Ryan Singer** [01:27:16]
And that's what allows you to scale to internal service, internal service departments in the future.

**Ryan Singer** [01:27:22]
Right.

**Ryan Singer** [01:27:22]
Because at the end of the day, somebody has to provide the service, whether it's you or whether it's like you hand off to another team or the internal team or whatever.

**Ryan Singer** [01:27:30]
that's all that all makes a lot of sense.

**Ryan Singer** [01:27:32]
So, OK, what I what I think where we got to before the break was.

**Ryan Singer** [01:27:39]
Is it true that this is actually just a UX problem?

**Ryan Singer** [01:27:43]
It's like because what I saw from your demo was that it seems possible to already wire this data together.

**Ryan Singer** [01:27:50]
what I'm wondering is like it is this primarily about the UX problem?

**Ryan Singer** [01:27:55]
And then when it comes to like how do we actually get Google Analytics wired into the page?

**Marcel Santilli** [01:28:00]
Blah, blah.

**Marcel Santilli** [01:28:00]
That's kind of like, we'll figure it out type stuff?

**Marcel Santilli** [01:28:04]
Yes.

**Marcel Santilli** [01:28:05]
Yeah.

**Marcel Santilli** [01:28:05]
today we have analytics pipeline working.

**Marcel Santilli** [01:28:13]
It's presented horribly, but it's working in someone who needs to physically authenticate, obviously, you know, and we have, and correct me if I'm saying anything wrong here.

**Marcel Santilli** [01:28:23]
And we also have the pipeline to ingest Google Search Console data as well set up.

**Marcel Santilli** [01:28:30]
those two things are true and are working and can be set up, but need to be set up.

**Marcel Santilli** [01:28:35]
Meaning like somebody should click a button, you know, and authenticate Google Search.

**Marcel Santilli** [01:28:38]
the wall's low, have the API integration and all that.

**Marcel Santilli** [01:28:41]
It's already there.

**Marcel Santilli** [01:28:42]
we have that data.

**Marcel Santilli** [01:28:45]
Today, it is also true that we have a crawler on steroids set up, right?

**Marcel Santilli** [01:28:52]
And I say crawl on steroids because it's like, I mean, yeah, we have, as soon as you plug into your website, we speak to your entire website and run into it.

**Marcel Santilli** [01:29:01]
That's to get the sitemap and all the pages and stuff like that.

**Marcel Santilli** [01:29:04]
Yeah, yeah.

**Marcel Santilli** [01:29:05]
we're doing a semantic understanding of each page.

**Marcel Santilli** [01:29:08]
Like, we also do the baseline.

**Marcel Santilli** [01:29:09]
We count words.

**Marcel Santilli** [01:29:10]
hit some APIs, like the Google page speed kind of API, like, but the post-processing is very, like, basic, and we haven't done a ton of post-processing, meaning, like, we're not, like, yet doing a workflow that, like, qualitatively judges the input of that page.

**Marcel Santilli** [01:29:29]
could.

**Marcel Santilli** [01:29:29]
The infrastructure is there.

**Marcel Santilli** [01:29:31]
We're doing, like, a simple path.

**Marcel Santilli** [01:29:33]
But if we have, like, a data scientist that would define, or if we define between ourselves what quality means, it's just, like, it's one day of work to get that data into the data.

**Marcel Santilli** [01:29:42]
Yeah.

**Marcel Santilli** [01:29:42]
today, this is the data.

**Marcel Santilli** [01:29:45]
This is an actual customer.

**Marcel Santilli** [01:29:46]
This is the actual data, right?

**Marcel Santilli** [01:29:48]
This is live.

**Marcel Santilli** [01:29:49]
So, like, you have content, which is, like, the screenshot, the HTML, and the markdown, and some basic information about it, like, including, like, the, you know, like,

**Marcel Santilli** [01:30:00]
The structure, timeline, if it's available, and then you, when there is traffic and when it's connected, or like in this case, like.

**Marcel Santilli** [01:30:08]
This one is connected, it's just a bug that the blank slate is assuming that if there's no data, it's connected.

**Marcel Santilli** [01:30:14]
Okay, so let me, let me pick a page then just to kind of show you so you know what's there, that.

**Marcel Santilli** [01:30:20]
Scroll to the left, and you can see, there's just a scrolling here.

**Marcel Santilli** [01:30:23]
On the left?

**Marcel Santilli** [01:30:24]
Scroll to Oh, sorry, sorry.

**Marcel Santilli** [01:30:25]
Okay, okay.

**Marcel Santilli** [01:30:27]
All right.

**Marcel Santilli** [01:30:28]
That one.

**Marcel Santilli** [01:30:29]
Yep.

**Marcel Santilli** [01:30:30]
Does this work?

**Marcel Santilli** [01:30:31]
I don't know.

**Marcel Santilli** [01:30:34]
Okay, perfect.

**Marcel Santilli** [01:30:35]
Okay, so, okay, their homepage, maybe.

**Marcel Santilli** [01:30:38]
All right, actually, like, let's just go into, like, this page.

**Marcel Santilli** [01:30:41]
Okay, so this page has traffic, you see?

**Marcel Santilli** [01:30:45]
Like, and it's not yet correlating to the search console data, you know, and then there's, like, content, right?

**Marcel Santilli** [01:30:54]
there's, like, a screenshot of how the page looks like.

**Marcel Santilli** [01:30:56]
if it was broken, like, you could see it here, right?

**Marcel Santilli** [01:30:59]
Okay.

**Marcel Santilli** [01:30:59]
Okay.

**Marcel Santilli** [01:30:59]
Okay.

**Marcel Santilli** [01:31:00]
This is a page based on the screenshot that we worked on most likely because the screenshot looks like one of the ones we take.

**Marcel Santilli** [01:31:07]
Then there's like the HTML, but also like the markdown, which is the extracted version of like the page, you know, like just the text that you, that's what you could analyze, you know, and, and then there's like, you know, like the search related to this.

**Marcel Santilli** [01:31:22]
you can see what keywords that are generating the clicks.

**Marcel Santilli** [01:31:25]
This looks wrong by the way, this table, but it's like, technically you should be able to see for this page that there's like the traffic, right?

**Marcel Santilli** [01:31:33]
Like, which again, like you need to validate that this also looks wrong down here, but, but it's like, it's there.

**Marcel Santilli** [01:31:40]
And then there's the tech report that should be triggered automatically.

**Marcel Santilli** [01:31:43]
don't know why it's not, but it will, you know, it's possible to.

**Marcel Santilli** [01:31:45]
hit all sorts of limits.

**Marcel Santilli** [01:31:47]
That's why we don't trigger an entire website.

**Marcel Santilli** [01:31:49]
that's not a problem.

**Marcel Santilli** [01:31:49]
like if you have 20,000 pages in the case of AirPy, you need to find more than important, which pages are actually important.

**Marcel Santilli** [01:31:56]
They can't do it.

**Marcel Santilli** [01:32:00]
Because there are limits on every single API, like Google has a limit on paid speed API calls, so that portfolio definition and the pages you care about would help with it, you know, where we can't just run paid speed on every single page 20,000 times.

**Marcel Santilli** [01:32:18]
And so, like, you can see you can have, like, it's there, it's a little disjointed to be generous here, you know, and then like...

**Ryan Singer** [01:32:29]
What is opportunities again?

**Marcel Santilli** [01:32:32]
Yeah, so opportunities, this is actually working too, it's kind of like how we take the context we have on a company, like the brand context, like the company, the product, the personas, right?

**Ryan Singer** [01:32:46]
Opportunities are your ideas of improvements that would be meaningful to make.

**Marcel Santilli** [01:32:50]
These are the things that you think you could do, okay.

**Marcel Santilli** [01:32:53]
And then it's like going in, I think this is probably finished running, but it's like been stuck on this, but it's like...

**Marcel Santilli** [01:32:59]
Thank you.

**Marcel Santilli** [01:32:59]
Thank you.

**Marcel Santilli** [01:33:01]
I'll just trigger anyone so you can kind of see, but like a persona-based VP of engineering, you know, and start the research, and now it's running through a workflow and doing a bunch of stuff to then identify opportunities, see, like 15 topics, and then it's like 540, 60 words from this and this and that, and then turning them into legit opportunities, like, you know, like X best data engineering tools for enterprises.

**Ryan Singer** [01:33:30]
What does it mean for an opportunity to, so we were looking at a page, so here an opportunity could be, for example, writing a new page, right?

**Ryan Singer** [01:33:39]
This is net new, this is opportunities for net new, not yet for optimization.

**Ryan Singer** [01:33:44]
Okay, and then when we were on the page, and there was an opportunity section, that would be an opportunity that somehow is filtering up as an improvement of the page?

**Marcel Santilli** [01:33:54]
This would be, like, yeah, like, this would be, hey, this one is easy, and...

**Marcel Santilli** [01:34:00]
And relevance is high, so I'm going to accept and create this page.

**Marcel Santilli** [01:34:06]
then later on, ideally, you'll be able to see what work was done to originate the page or to improve the page.

**Marcel Santilli** [01:34:14]
if I go here, the opportunity should be like, hey, there's a net new opportunity that actually is the reason this page even exists.

**Ryan Singer** [01:34:24]
Or later on, it's the reason this page got improved.

**Ryan Singer** [01:34:27]
this could also be historical opportunities in the sense of like, this is why this page was created, but this opportunity is kind of like, met?

**Marcel Santilli** [01:34:36]
The opportunity step there is kind of like, it's up for debate, but every page that we create should have been originated by an opportunity.

**Marcel Santilli** [01:34:46]
The opportunities are how we have the data, it's backed by hypothesis, and then drives the work.

**Marcel Santilli** [01:34:52]
Yeah, and then at the page level, the reason why we have that there is that we couldn't be the place where we would have...

**Marcel Santilli** [01:34:58]
Ah, that's the hypothesis.

**Ryan Singer** [01:35:00]
No, no, I'm with you now.

**Ryan Singer** [01:35:02]
Now I remember you explained this.

**Marcel Santilli** [01:35:04]
Sorry.

**Marcel Santilli** [01:35:05]
Yeah, opportunities is the hypothesis.

**Marcel Santilli** [01:35:08]
Assignments are the prioritized work.

**Ryan Singer** [01:35:11]
Yes.

**Ryan Singer** [01:35:12]
And then pages are the output of that work when it's done.

**Ryan Singer** [01:35:15]
Okay.

**Marcel Santilli** [01:35:16]
And creating a new page is one output.

**Marcel Santilli** [01:35:20]
Changing an existing page is another output.

**Marcel Santilli** [01:35:23]
And because most of our work is net new pages, most of what we built so far is for net new opportunities and not optimization yet.

**Marcel Santilli** [01:35:31]
We pushed optimization opportunities as a separate thing to think about later because we're doing both at the same time.

**Marcel Santilli** [01:35:38]
We've got to get this part right.

**Ryan Singer** [01:35:39]
Otherwise, like, you can't optimize what you don't even measure yet, you know?

**Marcel Santilli** [01:35:43]
Yeah, sure.

**Marcel Santilli** [01:35:44]
That's why we're trying to figure this part out, you know?

**Ryan Singer** [01:35:48]
Okay.

**Marcel Santilli** [01:35:51]
It's a lot.

**Ryan Singer** [01:35:53]
It's, it's, it's, oh man, this is interesting.

**Ryan Singer** [01:35:59]
So.

**Ryan Singer** [01:36:00]
What I'm seeing here is, okay, there is a mental model where all of this stuff makes sense as a one thing.

**Ryan Singer** [01:36:14]
There's opportunities that lead to assignments, which lead to the creation of pages, and then pages are work that has to be done.

**Ryan Singer** [01:36:21]
But then after you do the work, then you have to be evaluating, like, is it actually performing?

**Ryan Singer** [01:36:26]
Like, there is this clear model or the method to the madness, like, which is what we kind of were drawing out in the first half of the call.

**Ryan Singer** [01:36:36]
The, the, what the UI should be doing here, and this is going to be, there's a, there's definitely a way to do this.

**Ryan Singer** [01:36:46]
And it's going to, it's, you want to feel like the UI is, is flashing your brain with the model again, where you're like, oh yeah, that's how we work.

**Ryan Singer** [01:36:55]
Right.

**Ryan Singer** [01:36:56]
Right.

**Ryan Singer** [01:36:57]
So, so like, um, the.

**Ryan Singer** [01:37:00]
The thing that we do naturally is we just kind of start filling in – we use all the software things like sidebars and navbars and tabs, right?

**Ryan Singer** [01:37:12]
And we naturally just kind of start populating these sidebars and tabs with stuff.

**Ryan Singer** [01:37:19]
And then if you have the secret key in your mind of like, this is what we're doing here, then you know what it means to go click on opportunities and click on pages and click on this.

**Ryan Singer** [01:37:30]
know what I mean?

**Ryan Singer** [01:37:32]
And like the classic, you know, the classic kind of UI principle is that good software is like a good stove.

**Ryan Singer** [01:37:41]
you see four burners, you see four knobs, and the knobs are like in the same position relative to each other as the burners.

**Ryan Singer** [01:37:47]
You know what I mean?

**Ryan Singer** [01:37:48]
And you don't even – like you look at it and you see like burners and heat levels, and you just turn it.

**Ryan Singer** [01:37:55]
You don't even think, right?

**Ryan Singer** [01:37:56]
like you've got a stove here, and the stove –

**Ryan Singer** [01:38:00]
Is this actual physical process that humans are doing that you are teaching people to do, which is like identify opportunities, make assignments, write pages, evaluate page performance, and then up a level, report to the client, aggregate performance.

**Marcel Santilli** [01:38:21]
Yes.

**Ryan Singer** [01:38:21]
Perfect.

**Marcel Santilli** [01:38:22]
Right?

**Ryan Singer** [01:38:23]
Perfect.

**Ryan Singer** [01:38:24]
This is what the UI should be.

**Marcel Santilli** [01:38:30]
And I would just add that it's like ideally it's, hey, we're trying to do this outcome.

**Marcel Santilli** [01:38:41]
We're trying to, you know, drive this outcome.

**Marcel Santilli** [01:38:43]
And that's like for everything, what you just described, it's like, that's the reward function.

**Marcel Santilli** [01:38:51]
You know what mean?

**Ryan Singer** [01:38:53]
Yeah.

**Marcel Santilli** [01:38:54]
The reward function is like the name growth isn't our name.

**Marcel Santilli** [01:38:57]
It's like we have to grow, help people grow.

**Marcel Santilli** [01:39:00]
Essentially, you know, the reward function, the macro reward function is like help company building this engine so that it builds compounding growth for companies, you know, over time.

**Ryan Singer** [01:39:11]
Yep, yep.

**Ryan Singer** [01:39:13]
Okay.

**Marcel Santilli** [01:39:14]
So, um...

**Marcel Santilli** [01:39:18]
Sorry, at the risk of being, like, too prescriptive, it's like, the reason this is so, so, so, so  valuable is that, like, this is the only marketing channel that compounds.

**Marcel Santilli** [01:39:30]
Like, ads, you stop, it goes to zero.

**Marcel Santilli** [01:39:32]
Like, most ads, you stop, it goes to zero.

**Marcel Santilli** [01:39:34]
A page doesn't decay immediately.

**Marcel Santilli** [01:39:36]
Traffic doesn't go to zero overnight.

**Ryan Singer** [01:39:38]
Like, yeah, it's an asset.

**Marcel Santilli** [01:39:40]
It's not just spend.

**Marcel Santilli** [01:39:41]
Yeah.

**Marcel Santilli** [01:39:42]
And so if you get this engine right, it's the most valid, it's the most powerful.

**Marcel Santilli** [01:39:47]
if you look at Canva.com, right, like, so, so Canva.com gets 280 million visitors a month.

**Ryan Singer** [01:39:53]
They've been profitable for 10 years straight.

**Marcel Santilli** [01:39:55]
And the reason for that is they have 44,000 pages.

**Marcel Santilli** [01:40:00]
Essentially, you know, the reward function, the macro reward function is like help company building this engine so that it builds compounding growth for companies, you know, over time.

**Ryan Singer** [01:40:11]
Yep, yep.

**Ryan Singer** [01:40:13]
Okay.

**Ryan Singer** [01:40:14]
So, um...

**Ryan Singer** [01:40:18]
Sorry, at the risk of being, like, too prescriptive, it's like, the reason this is so, so, so, so  valuable is that, like, this is the only marketing channel that compounds.

**Ryan Singer** [01:40:30]
Like, ads, you stop, it goes to zero.

**Ryan Singer** [01:40:32]
Like, most ads, you stop, it goes to zero.

**Ryan Singer** [01:40:34]
A page doesn't decay immediately.

**Ryan Singer** [01:40:36]
Traffic doesn't go to zero overnight.

**Ryan Singer** [01:40:38]
Like, yeah, it's an asset.

**Ryan Singer** [01:40:40]
It's not just spend.

**Ryan Singer** [01:40:41]
Yeah.

**Ryan Singer** [01:40:42]
And so if you get this engine right, it's the most valid, it's the most powerful.

**Ryan Singer** [01:40:47]
if you look at Canva.com, right, like, so, so Canva.com gets 280 million visitors a month.

**Ryan Singer** [01:40:53]
They've been profitable for 10 years straight.

**Ryan Singer** [01:40:55]
And the reason for that is they have 44,000 pages.

**Ryan Singer** [01:41:00]
on their site that for the last 10 years they've invested in and improved.

**Ryan Singer** [01:41:04]
And now every single month they get $800 million worth of traffic for free.

**Ryan Singer** [01:41:09]
Amazing.

**Ryan Singer** [01:41:10]
For doing nothing.

**Ryan Singer** [01:41:11]
That's what the guys at 37signals did.

**Ryan Singer** [01:41:15]
mean, like Jason and David, they wrote so much stuff on the blog in the early days, and then they actually just sold into the blog traffic.

**Ryan Singer** [01:41:21]
know?

**Ryan Singer** [01:41:22]
Okay.

**Ryan Singer** [01:41:23]
what I want to do here is, okay, so I'm actually doing this right now for another client.

**Ryan Singer** [01:41:28]
my fractional CPO client, and like literally what happened was they were, they've got really good hands-on sales, and they've been adding on, they're in like the sort of like strength training for sports teams industry.

**Ryan Singer** [01:41:46]
And they have really, really deep knowledge of what coaches and athletes need, and so they built like a million features that cover every edge case.

**Ryan Singer** [01:41:55]
And the sales is really good at navigating people through that maze of like this.

**Ryan Singer** [01:42:00]
This is exactly what you need.

**Ryan Singer** [01:42:01]
And they're like, well, you really understand me.

**Ryan Singer** [01:42:03]
And the software does everything I need.

**Ryan Singer** [01:42:05]
And then they buy.

**Ryan Singer** [01:42:07]
What started to happen was that like the fact that that everything was just kind of somewhere in the app, it kind of reached a tipping point where there's just too much sprawl.

**Marcel Santilli** [01:42:16]
And now it's like nobody can kind of trial and convert because they can't make any sense out of what they're looking at because there's just too much stuff everywhere.

**Ryan Singer** [01:42:25]
there's like a point where like we needed to be able to like go up in the helicopter and like, can I create a big view of what this all is that makes sense to anybody who walks in the door?

**Ryan Singer** [01:42:37]
The way that we kind of characterize the project is like, so it's literally like the overhaul of the overall UI organization of the thing so that it makes sense.

**Ryan Singer** [01:42:46]
And the way that we characterize that project is it's the map at the mall.

**Marcel Santilli** [01:42:50]
You know what I mean?

**Ryan Singer** [01:42:50]
I need to walk into the mall and I need to instantly be like, you are here and H&M is there.

**Ryan Singer** [01:42:55]
You know what I mean?

**Ryan Singer** [01:42:56]
And that's where I buy the giant cookie or whatever.

**Ryan Singer** [01:42:57]
like, yes.

**Ryan Singer** [01:43:00]
I'm seeing the exact same moment here where the surface area has reached a kind of a breaking point, and there needs to be a UI approach that reminds you of how this all hangs together so that you feel where you are in it and it makes sense to you.

**Ryan Singer** [01:43:19]
I kind of feel like where this should go is that analogy, you need a shopping list so that you don't forget to pick up the milk.

**Ryan Singer** [01:43:26]
Yes, exactly.

**Ryan Singer** [01:43:28]
Exactly.

**Ryan Singer** [01:43:29]
What's cool about that is that the better we do, the more the map of the mall looks like your actual process, the more differentiated it is, and the more that the app also looks like you.

**Ryan Singer** [01:43:43]
Do you know what I mean?

**Ryan Singer** [01:43:44]
I'm not just looking at yet another kind of React app and another sidebar.

**Ryan Singer** [01:43:50]
Yeah, yeah, yeah, exactly.

**Ryan Singer** [01:43:52]
I love that.

**Ryan Singer** [01:43:53]
So, like, I'm, this is mainly just a perspective thing.

**Ryan Singer** [01:43:58]
think it's not rocket science.

**Ryan Singer** [01:43:59]
And- I think

**Ryan Singer** [01:44:00]
What I'm going to do is just throw some very kind of obvious things on the table, you know, to maybe get us started.

**Ryan Singer** [01:44:07]
Because I kind of think that we can maybe sketch some things together.

**Ryan Singer** [01:44:10]
Are you ready for that?

**Ryan Singer** [01:44:11]
Yeah, do it.

**Ryan Singer** [01:44:12]
Love it.

**Ryan Singer** [01:44:13]
All right.

**Ryan Singer** [01:44:15]
I'm going to go back to the whiteboard here.

**Marcel Santilli** [01:44:19]
And so what I'm literally going to do is I'm just going to draw.

**Marcel Santilli** [01:44:24]
I'm going to try and draw the process with the idea of, like, we're going to make this software, okay?

**Marcel Santilli** [01:44:33]
So, like, there's, there's, and I'm just going to do this in a very simple way first.

**Marcel Santilli** [01:44:40]
Let's just say, I'm just going to capture what we already talked about.

**Marcel Santilli** [01:44:46]
There's opportunities, which is like the hypothesis.

**Marcel Santilli** [01:44:51]
There's assignments.

**Marcel Santilli** [01:44:54]
There's, uh, pages.

**Marcel Santilli** [01:44:56]
Let me make this all a little bit smaller and tighter.

**Marcel Santilli** [01:44:59]
There's, there's,

**Ryan Singer** [01:45:00]
There's pages, then there's the, we need a name for this.

**Ryan Singer** [01:45:11]
What is the bigger picture conversation that a manager has with the client of like, this is what this adds up to and this is where we're at and this is what we should be new?

**Ryan Singer** [01:45:22]
Like, ultimately, you could call it signals or you can call it like visibility and traffic, you know, or, you know, it's kind of like they are, ultimately they're signals, right?

**Ryan Singer** [01:45:40]
And those signals are signals that, like, you are, that your work is having an impact on the outcomes you care about.

**Ryan Singer** [01:45:53]
But the outcomes are different for every company, like the goals, right?

**Ryan Singer** [01:45:56]
Like, there's signals and then there's like goals and things.

**Ryan Singer** [01:46:00]
Essentially, like, right, like, but, but, so, but, but I, yeah, but that's okay.

**Marcel Santilli** [01:46:07]
Sometimes it's, you know, like, it's better to have a verbose name for something that means what it means, you know, and then we can get to the short name in the future, you know, so we can kind of.

**Marcel Santilli** [01:46:18]
And maybe say, like, impact on the outcomes instead of goals, because, like, goals can be, like, achieved this.

**Marcel Santilli** [01:46:25]
Outcomes is, like, an ongoing.

**Marcel Santilli** [01:46:27]
Yeah, that's good.

**Marcel Santilli** [01:46:27]
Yeah, like, goals felt, like, finite and outcomes is the length.

**Ryan Singer** [01:46:32]
So, like, what I got out of our kind of conversation so far today is that pages is, like, there's the work of, like, I've got to, I've got to, I've got to write the page, you know, or, or I need to, or, like, create the page or, like, revise the page.

**Marcel Santilli** [01:46:53]
Like, there's, there's this, like, there's kind of, like, the work piece to this.

**Ryan Singer** [01:46:58]
I'm to call it, like.

**Marcel Santilli** [01:47:00]
There's the work on the page, and then there is the evaluation of the page, which is like, how's it doing?

**Marcel Santilli** [01:47:09]
Does it need attention or not?

**Marcel Santilli** [01:47:12]
This is the opposite of flying blind.

**Marcel Santilli** [01:47:14]
Do you have a better word for this?

**Marcel Santilli** [01:47:17]
Yeah, I think, like, mean, email is good, because, like, you need to evaluate the page, and I think people understand that.

**Marcel Santilli** [01:47:26]
And I think, like, the work is really, like, create or update, that's it.

**Marcel Santilli** [01:47:33]
Or delete, actually.

**Marcel Santilli** [01:47:34]
Like, create, update, like, archive, or delete, you know?

**Marcel Santilli** [01:47:39]
Like, those are not only the reactions that you can truly take, you know?

**Marcel Santilli** [01:47:45]
And, um, uh...

**Marcel Santilli** [01:47:49]
And then evaluate is, um, the things we had are, like, health, quality, yeah, health, quality, visibility.

**Marcel Santilli** [01:48:00]
I just want to make these separate.

**Marcel Santilli** [01:48:02]
Quality, visibility, traffic, engagement, conversion.

**Marcel Santilli** [01:48:12]
And a way to think about it, as well as that quality leads to traffic, and if the quality is high, sorry, quality leads to, there should be strongly correlated to engagement, and eventually conversion, and visibility should lead to traffic, you know, like, so it's like, like, the content is garbage, no one's going to read it, right?

**Marcel Santilli** [01:48:45]
if it looks like , you know?

**Ryan Singer** [01:48:48]
And people reading it impacts visibility.

**Marcel Santilli** [01:48:52]
the engagement would triple that.

**Ryan Singer** [01:48:55]
And people, high engagement on a page, sense positive signals.

**Marcel Santilli** [01:49:04]
engagement has a positive signal back to visibility, and one of the highest acts you can have here, it's like when you put a tool on that page, the reason those things do so well is because people stay on that page forever, because now they're like using a UI essentially, right, I love to get so much good signals, because it's just like you come in, and then you start working with the prompt, and then you get an app, you're like, holy , and then the next thing you know, two hours went by.

**Marcel Santilli** [01:49:33]
There is a, there is a, when you told the story about, you know, the pages were underperforming, but nobody paid attention to it, and we would have stopped making new pages if we had noticed that those two pages were declining, the two top pages.

**Marcel Santilli** [01:49:50]
It's a visibility drop, or a traffic drop.

**Ryan Singer** [01:49:56]
Yeah, want to, I want to, I want want to come up a level from that.

**Ryan Singer** [01:49:59]
there

**Ryan Singer** [01:50:00]
was a problem in here at the page level, right?

**Ryan Singer** [01:50:04]
But what I understood was that there's a flow here of like create, create, create.

**Marcel Santilli** [01:50:12]
Yes.

**Ryan Singer** [01:50:13]
There's not like a clear story around like a flow here that is up there.

**Ryan Singer** [01:50:19]
We haven't, we spend like very little cycles on that because like this level of clarity, even though we have today, even prior to the session, and even more now during the session, like I don't think on like what work and how we prioritize the work because there's so many layers to this thing, you know, and how do we simplify it, you know, because it can be like, and it can be on the level of like fix the site now, across your whole site, and it can be at the level of like there's a broken link on your page, and it can be at the level of like rewrite the whole thing.

**Marcel Santilli** [01:50:57]
there's so many layers to this.

**Ryan Singer** [01:50:59]
Like, where am I?

**Ryan Singer** [01:51:00]
My head is going to, this feels like a bug to me that assignments are considered something outside of pages because actually an assignment could be we are in pages and you need to make a new one or we are in pages and you need to update one because fixing those one page is more important than anything else.

**Ryan Singer** [01:51:22]
That's even how the data model today in the back end works.

**Ryan Singer** [01:51:26]
Uh-huh.

**Ryan Singer** [01:51:27]
what I want to do then, if that's a first draft above, then I want to already expand this out to an alternate idea.

**Marcel Santilli** [01:51:45]
And this is where, if I come into pages, now, we don't know yet, but you know what I mean?

**Marcel Santilli** [01:51:53]
I'm trying to get to something where it's like, um...

**Ryan Singer** [01:51:57]
Thank you.

**Ryan Singer** [01:51:59]
You

**Ryan Singer** [01:52:01]
And what I think we see here is that opportunities can tell me that I should create a page, right?

**Ryan Singer** [01:52:14]
But a visibility problem could tell me that I should update a page.

**Marcel Santilli** [01:52:18]
Yes.

**Marcel Santilli** [01:52:21]
when I'm somehow doing eval, either like at the kind of I'm scrolling through the whole air table or I'm in detailed in on one page, you know, it's kind of like, how do I assign based on what I'm seeing?

**Marcel Santilli** [01:52:42]
Yeah.

**Marcel Santilli** [01:52:44]
way we were mapping this before would be that you would have optimization opportunities and then new opportunities.

**Marcel Santilli** [01:52:53]
And dropping traffic would be like an optimization opportunity.

**Marcel Santilli** [01:52:59]
Uh-huh.

**Marcel Santilli** [01:53:00]
Uh-huh.

**Marcel Santilli** [01:53:00]
Okay.

**Marcel Santilli** [01:53:02]
How is an assignment different than an opportunity?

**Ryan Singer** [01:53:05]
Assignment are the opportunities that you took as, like, I actually want to work on this.

**Ryan Singer** [01:53:10]
Why opportunities are the ones that I do?

**Ryan Singer** [01:53:12]
Okay.

**Ryan Singer** [01:53:13]
Dumb question.

**Marcel Santilli** [01:53:14]
Why not just do it?

**Ryan Singer** [01:53:15]
Why do I need to track it as an assignment in between?

**Ryan Singer** [01:53:20]
Mostly because that's just a downstream effect of, like, we want to see the tickets.

**Marcel Santilli** [01:53:28]
You want to see the tickets.

**Marcel Santilli** [01:53:31]
You want to be able to account for what's being done and what's not being done.

**Marcel Santilli** [01:53:34]
Yeah, yeah.

**Marcel Santilli** [01:53:34]
Yeah, like, you can do a pull request, right, like, and fix a bug.

**Marcel Santilli** [01:53:41]
I see.

**Marcel Santilli** [01:53:41]
then, like, you ideally want to know, like, that at some point someone made a decision to say, yes, this is a good opportunity.

**Marcel Santilli** [01:53:50]
Yes, we're going to prioritize.

**Marcel Santilli** [01:53:52]
Yes, we're going to do it.

**Marcel Santilli** [01:53:54]
It's like, how do you measure what's happening in with, you know?

**Marcel Santilli** [01:53:59]
Got it.

**Marcel Santilli** [01:53:59]
it.

**Marcel Santilli** [01:54:07]
if I'm evaluating and I see a problem here, actually I would be creating an opportunity, and it's opportunity to optimize, let's say.

**Ryan Singer** [01:54:17]
This opportunity to optimize should actually live here side by side with the other opportunities to create so that I know which I'm conscious which one I'm choosing.

**Ryan Singer** [01:54:30]
There is a level here that's like, should this even be tracked in the sense of like, let's say there's a page that is not discoverable, not indexed, and that has got no traffic, like should you really create an opportunity to delete a page, like that feels kind of silly, but then at the same time it's like, hey, if you systematically prune like 20% of your site, like you will improve overall performance of your site, because it's like, whatever, right, like,

**Ryan Singer** [01:55:01]
And so it's like, that is like a good thing.

**Ryan Singer** [01:55:04]
And if you told them to do that and they did it and they improved results, you do want to know that.

**Marcel Santilli** [01:55:08]
But there's actions that feel more like batch mode actions that you should go through systematically versus like page level, you know, insight, you know.

**Marcel Santilli** [01:55:20]
So, okay.

**Marcel Santilli** [01:55:20]
I'm just going to start drawing some stuff that's in my head that makes this feel simple for me.

**Ryan Singer** [01:55:26]
So, like, what I'm trying to get to now is like, what is the UI unit, you know, that we like repeat and show again all the time?

**Marcel Santilli** [01:55:37]
So, like, when you have like a unit, like this is a post on X, like then it's like, okay, I know what this is.

**Marcel Santilli** [01:55:44]
I know wherever it appears that this is a post and this is what it has.

**Marcel Santilli** [01:55:47]
So, like, there's one thing stands out to me is I'm trying to, I'm trying to get to the through line of the page as being like the thing that's the, that connects everything.

**Marcel Santilli** [01:55:59]
another thing.

**Ryan Singer** [01:56:00]
And I'm picturing opportunities, and I'm almost picturing, like, so let's say there's a description.

**Ryan Singer** [01:56:11]
What's an example of, like, how would you call it out?

**Ryan Singer** [01:56:14]
Like, is it, like, a title of the opportunity or a sort of short summary of, like, what it is?

**Marcel Santilli** [01:56:18]
Just think of it as, like, a templatized headline of, like, X best practices for designing a UI.

**Ryan Singer** [01:56:28]
Mm-hmm, mm-hmm.

**Ryan Singer** [01:56:29]
And that's an interesting opportunity.

**Marcel Santilli** [01:56:31]
Yeah, so let's say we have...

**Marcel Santilli** [01:56:33]
Or the most common pitfalls of, like, redesigning your UI.

**Ryan Singer** [01:56:38]
Yeah.

**Ryan Singer** [01:56:38]
And let's say that this is the opportunity.

**Ryan Singer** [01:56:41]
let's say this is the...

**Ryan Singer** [01:56:42]
And then we also kind of put, like, the title of the page.

**Marcel Santilli** [01:56:47]
sometimes it would be, like, a how-to or, like...

**Marcel Santilli** [01:56:49]
Sure.

**Marcel Santilli** [01:56:50]
A comparison.

**Marcel Santilli** [01:56:51]
Yeah.

**Marcel Santilli** [01:56:51]
I'm not going to cover everything right now, but I want to just do is say, like, I just want to capture this idea.-hmm.

**Ryan Singer** [01:57:03]
This is, so let's say we have, you know, XXX how-to tips for whatever, right?

**Ryan Singer** [01:57:12]
And this is on the what page?

**Marcel Santilli** [01:57:14]
What's the realistic page name that we were shortening?

**Marcel Santilli** [01:57:19]
article?

**Marcel Santilli** [01:57:21]
Yeah.

**Marcel Santilli** [01:57:23]
Let's say this is a specific new existing page that has a reason that it's an opportunity.

**Marcel Santilli** [01:57:29]
There's a reason why we want to optimize it.

**Marcel Santilli** [01:57:34]
you're looking for like the URL, the slug, the page This is exactly the question.

**Marcel Santilli** [01:57:40]
How do we refer to a page whenever we need to refer to it in a short way throughout the system?

**Marcel Santilli** [01:57:47]
Today is a page title.

**Ryan Singer** [01:57:49]
Page title.

**Ryan Singer** [01:57:50]
Page title is like what it is specifically, but then like it.

**Ryan Singer** [01:57:54]
The slug is going to.

**Ryan Singer** [01:57:55]
Either the slug or the...

**Marcel Santilli** [01:58:00]
Page type, if you don't need it to be specific to that page individually, you know, but the slug.

**Ryan Singer** [01:58:06]
Yeah, does every page have a slug?

**Ryan Singer** [01:58:08]
is like, yeah.

**Ryan Singer** [01:58:10]
And is the slug kind of like your internal shorthand for like what that page is, if you need to talk about it?

**Marcel Santilli** [01:58:17]
Not contextually, it's just like what the external world, it's a shortcut to the external world, but it doesn't have enough contextual, like, you know.

**Marcel Santilli** [01:58:28]
The headline plus the slug will give you a lot.

**Marcel Santilli** [01:58:32]
The headline plus the slug plus the page type will give you like 95%.

**Marcel Santilli** [01:58:37]
I think the slug at the URL is essentially the name of the product.

**Marcel Santilli** [01:58:43]
Yeah, yeah, exactly.

**Marcel Santilli** [01:58:43]
then the name of the product, you don't talk about this.

**Marcel Santilli** [01:58:46]
Exactly.

**Marcel Santilli** [01:58:47]
You about the book and the inventory, you don't talk about the title.

**Marcel Santilli** [01:58:49]
Exactly.

**Marcel Santilli** [01:58:50]
But you care about this.

**Marcel Santilli** [01:58:51]
So, like, if this is a new, if this is something new, like, we will have a type.

**Marcel Santilli** [01:58:58]
Right.

**Marcel Santilli** [01:58:59]
Right.

**Marcel Santilli** [01:59:00]
An idea for that, a suggested type.

**Marcel Santilli** [01:59:03]
Uh-huh.

**Marcel Santilli** [01:59:04]
Yep.

**Marcel Santilli** [01:59:04]
Okay.

**Marcel Santilli** [01:59:05]
headline could be X tips for.

**Marcel Santilli** [01:59:10]
It's the headline of the opportunity then.

**Marcel Santilli** [01:59:12]
like here, this is like a new page.

**Marcel Santilli** [01:59:14]
If it's an optimization, it's going to be the probably repeating the headline of the page.

**Marcel Santilli** [01:59:19]
It be repeating, but it could also be what you need to do on that page if it's an optimization.

**Ryan Singer** [01:59:26]
That's how I would see it.

**Ryan Singer** [01:59:26]
Okay.

**Marcel Santilli** [01:59:27]
the headline.

**Marcel Santilli** [01:59:29]
Face is broken.

**Marcel Santilli** [01:59:30]
Uh-huh.

**Marcel Santilli** [01:59:31]
Uh-huh.

**Marcel Santilli** [01:59:31]
Yeah.

**Marcel Santilli** [01:59:31]
in Airtable specifically, it's like you were existing, the two.

**Marcel Santilli** [01:59:39]
And then like the page, there's like kind of like page type.

**Marcel Santilli** [01:59:47]
there's slug if it's only sure existing.

**Ryan Singer** [01:59:50]
Otherwise there's no like.

**Ryan Singer** [01:59:52]
That's right.

**Ryan Singer** [01:59:52]
That's right.

**Ryan Singer** [01:59:54]
And then after that, it's mostly around kind of like assignment.

**Ryan Singer** [02:00:00]
Type or page type in this case, and also the how we're clustering it, right?

**Ryan Singer** [02:00:07]
Which gets into the facts on me.

**Ryan Singer** [02:00:09]
And so what I mean by that is clustering by easy versus average versus hard opportunities.

**Ryan Singer** [02:00:15]
You might be clustering by, you know, topics, or you might be clustering by content types.

**Ryan Singer** [02:00:21]
And so like right now I'm staring at an air table for lovable where we have by difficulty, by content type.

**Marcel Santilli** [02:00:29]
And there's hundreds in each one of these buckets.

**Marcel Santilli** [02:00:33]
And then ideally within these you just have a button to say like, then like physically right now it's a checkbox that says assignment.

**Marcel Santilli** [02:00:43]
And when I click that checkbox, it's like create or prioritize, you know, accept or whatever.

**Marcel Santilli** [02:00:50]
Yeah, okay.

**Marcel Santilli** [02:00:52]
one thing I just want to ask before, I don't want to dive too deep here because otherwise we design the whole system.

**Marcel Santilli** [02:00:58]
And there's a million things all over.

**Marcel Santilli** [02:01:00]
But I want to just kind of get a sense of what this is.

**Marcel Santilli** [02:01:04]
What do you look at in opportunities to actually judge, I should be doing this instead of the other things?

**Marcel Santilli** [02:01:10]
if I've got like the 10 new things, but you said I've got the one optimization that's really, really important.

**Marcel Santilli** [02:01:17]
Is there something that would be escalating to you?

**Marcel Santilli** [02:01:20]
this is actually really important because this is a one percenter that's dipping?

**Marcel Santilli** [02:01:26]
Right now, we look at potential traffic when we're doing the audits.

**Marcel Santilli** [02:01:32]
And the potential traffic, there's a very specific way you do it with new pages.

**Ryan Singer** [02:01:38]
And there is a very specific way you do it with existing.

**Marcel Santilli** [02:01:42]
With existing, you're taking the actual search traffic from search console.

**Marcel Santilli** [02:01:51]
And then you are estimating what the...

**Marcel Santilli** [02:01:57]
In the meantime, wife started talking.

**Marcel Santilli** [02:01:59]
And I'll

**Marcel Santilli** [02:02:00]
And then you're estimating what the, if you had 100% market share, if you were like the top search result here, what your traffic could be, right?

**Marcel Santilli** [02:02:11]
And then you're taking the delta for existing, meaning like this is your realized traffic versus your potential truck.

**Marcel Santilli** [02:02:19]
If you did everything perfect on this page and everything went according to plan, what it could be, right?

**Marcel Santilli** [02:02:25]
the unrealized potential.

**Marcel Santilli** [02:02:27]
And so for NetNew, your unrealized potential is like total potential minus zero, which is total potential.

**Marcel Santilli** [02:02:35]
And then for existing is realized potential compared to total potential, you know?

**Marcel Santilli** [02:02:40]
will you be able to...

**Marcel Santilli** [02:02:41]
And that's for search, right?

**Ryan Singer** [02:02:43]
so then later on, you could add like the AI traffic and AI visibility and other things.

**Ryan Singer** [02:02:50]
But that's like the easiest way is through search because...

**Marcel Santilli** [02:02:54]
Got it.

**Ryan Singer** [02:02:56]
You don't have to worry about it.

**Marcel Santilli** [02:02:57]
Physically, how do we do it at an air table?

**Marcel Santilli** [02:02:59]
Except...

**Marcel Santilli** [02:03:00]
In Airtable, it's a one-off snapshot, so like five months from now, you don't have five months of traffic in there, so then you have to redo the entire snapshot, which is, you know, a lot of things.

**Marcel Santilli** [02:03:11]
Okay.

**Marcel Santilli** [02:03:14]
There are some things that, for example, updating a page, I think, fits in this model, but if you have systemic problems, how would you group them?

**Marcel Santilli** [02:03:26]
That's the reason why I was pushing on optimizations for later, because if you have something like, every page sucks at the super ability here, it's an urgent provider that should don't supersede everything else, you know?

**Marcel Santilli** [02:03:39]
Got it.

**Marcel Santilli** [02:03:39]
Okay.

**Marcel Santilli** [02:03:39]
And they don't, like, do they always correlate to a page?

**Marcel Santilli** [02:03:43]
They might, but I'm not quite sure.

**Marcel Santilli** [02:03:45]
Okay.

**Marcel Santilli** [02:03:46]
I want to put this to the side, because I think that it's possible to fall into the rabbit hole of specifically opportunities.

**Marcel Santilli** [02:03:54]
So- So- Is that one quick thing here?

**Ryan Singer** [02:03:57]
that, like, for those-

**Ryan Singer** [02:04:00]
If you just have some basic, like, screen somewhere or something somewhere that just says, hey, you went from five out of 100 pages  to 50 out of 100 pages , the rest is, like, is digging.

**Ryan Singer** [02:04:17]
Like, right?

**Ryan Singer** [02:04:17]
Like, you go review the source, go to me, like, oh, this is , this is , this is .

**Ryan Singer** [02:04:21]
And now I understand why it went from five, from five to enough, whereas, like, the harder part is when, like, you know, like, for instance, like, a very specific one at Airbuy, was talking to the VP of marketing yesterday, and he's like, you know, we just launched this product, and we just update these three other products, and we talk about it completely different.

**Ryan Singer** [02:04:43]
I would love to know, out of my 90,000 pages, which ones that get traffic and are important pages are completely mentioning how our product is wrong right now, that we should go update, you know?

**Ryan Singer** [02:04:55]
Like, yeah, that would be, like, your quality of the page load, because...

**Ryan Singer** [02:04:59]
Got it.

**Ryan Singer** [02:05:01]
Okay.

**Ryan Singer** [02:05:02]
what I want to do is I'm going to zoom back out.

**Ryan Singer** [02:05:06]
What I'm hearing is that actually there's just a ton of future work to do here, and there's a million ways that this can get better and better and better.

**Ryan Singer** [02:05:13]
I think talking about that makes me start to think about this differently.

**Ryan Singer** [02:05:18]
I'm almost picturing the map of the mall.

**Ryan Singer** [02:05:21]
I'm landing on the homepage of the app, and what I'm picturing is there's – so I'm almost thinking about maybe this translates into the sidebar.

**Ryan Singer** [02:05:31]
Maybe it replaces the sidebar.

**Ryan Singer** [02:05:33]
I can't see that yet.

**Ryan Singer** [02:05:35]
But what I'm picturing is that there's – actually, there's – when we talk about assignments, this is actually what work is, which is different.

**Ryan Singer** [02:05:47]
I'm out of how we evaluate what to do and pages and stuff like that.

**Marcel Santilli** [02:05:53]
There's – pages actually isn't really the top-level section.

**Marcel Santilli** [02:05:58]
It's like –

**Marcel Santilli** [02:06:00]
What work do I have to do that's actually assigned?

**Marcel Santilli** [02:06:05]
Okay?

**Ryan Singer** [02:06:06]
So, like, this might be creating pages or updating.

**Marcel Santilli** [02:06:09]
In the future, it might be optimizing pages.

**Marcel Santilli** [02:06:11]
So, like, what are the opportunities?

**Marcel Santilli** [02:06:14]
These are not assignments.

**Marcel Santilli** [02:06:16]
This is, like, I'm figuring out what to assign.

**Marcel Santilli** [02:06:19]
This is, like, what's assigned?

**Ryan Singer** [02:06:21]
I'm going to, like, get some work done today, you know?

**Ryan Singer** [02:06:24]
And then what we've been talking about, the eval, it's actually, like, because what you should be doing is, like, if you think you're done, you know what I mean?

**Ryan Singer** [02:06:36]
Like, you should be checking this, right?

**Ryan Singer** [02:06:39]
And not just kind of, like, going to pages to just, like, I'm going to go look at pages today.

**Ryan Singer** [02:06:44]
But it's, like, I should actually be monitoring.

**Ryan Singer** [02:06:49]
You know what I mean?

**Ryan Singer** [02:06:50]
Like, I need, there's this Can I suggest one quick thing here?

**Marcel Santilli** [02:06:54]
Please.

**Marcel Santilli** [02:06:55]
Instead of evals, call it experiments or hypotheses.

**Marcel Santilli** [02:07:02]
Because, like, you're doing a unit of work based on an initial hypothesis, which is opportunities.

**Marcel Santilli** [02:07:09]
if you think of opportunities, it's an ADS, and if you're doing the work, you set the experiment, and then the experiment is, like, you've to run it for a period of time, and they can auto-expire.

**Marcel Santilli** [02:07:23]
Is that, okay, does that not contradict the idea of, like, even if I'm in the 1%, like, is there really a moment where you can say, like, I've made it?

**Marcel Santilli** [02:07:34]
Because an experiment kind of implies that there's a moment when it's over, and I don't need to be paying attention anymore.

**Marcel Santilli** [02:07:40]
And what I've been hearing is that, like, what you want the engagement manager to be doing is, like, sure, maybe open experiments is something that I want to be seeing here, but this is, this isn't about only experiments, this is about, like, are you paying attention to performance?

**Marcel Santilli** [02:07:58]
yeah, no, no, you're, you're, you're.

**Marcel Santilli** [02:08:00]
You're right that maybe performance is a separate bucket, but what we're trying to find is experiments that tell you what patterns work so you can double down on doing more of that pattern.

**Marcel Santilli** [02:08:17]
Like, for instance, like, hey, we, like, listicles around best of within this context, a.k.a.

**Marcel Santilli** [02:08:29]
a strategy cluster.

**Marcel Santilli** [02:08:31]
Like, we're going to test out five of these clusters and then see if it has an impact on performance, a.k.a.

**Marcel Santilli** [02:08:38]
set an experiment.

**Marcel Santilli** [02:08:39]
And if that experiment, quote-unquote, it, throwing it out, you know, then that informs, like, a whole cluster of work because it's not a one-to-one.

**Marcel Santilli** [02:08:50]
It's more of, we're trying to find, like, clusters, you know what I mean?

**Marcel Santilli** [02:08:54]
Like, because otherwise it's impossible for you to, like, really scale this thing.

**Ryan Singer** [02:08:59]
It's not, like, a one

**Ryan Singer** [02:09:00]
One-off, you know, you're not starting an opportunity from blank.

**Ryan Singer** [02:09:03]
It's more of like, it's like, hey, like, for instance, for Lovable, our hypothesis was we looked at five of those, okay, 3,085 to be specific.

**Ryan Singer** [02:09:18]
Those 3,085 opportunities represented potential traffic of 12 million net new visitors per month for them, if they were number one, okay?

**Ryan Singer** [02:09:26]
And we cluster those by easy, average, and hard.

**Ryan Singer** [02:09:31]
And then within those, we cluster those 3,000 by content types, tools, templates, comparisons, how to, what is, listicles, and blocks.

**Ryan Singer** [02:09:40]
And for each one of those, we're like, each week, we can go and, like, plant, you know, like, X or Y within each one of these clusters.

**Ryan Singer** [02:09:51]
And then we want to know, like, which cluster is doing the best so that we can go prioritize the opportunities.

**Ryan Singer** [02:09:58]
This is great, you know?

**Ryan Singer** [02:09:59]
Yeah.

**Ryan Singer** [02:10:01]
Maybe experiments is the wrong word here, but it's like, you know, then it'll work.

**Ryan Singer** [02:10:08]
Do more or do less of this?

**Ryan Singer** [02:10:10]
Oh, that's interesting.

**Ryan Singer** [02:10:12]
That's interesting.

**Ryan Singer** [02:10:15]
Okay.

**Ryan Singer** [02:10:16]
Well, we can prototype with a few different words.

**Ryan Singer** [02:10:19]
Here's what I'm getting to.

**Ryan Singer** [02:10:20]
I think that what this is in terms of a page.

**Ryan Singer** [02:10:27]
first of all, like, imagine that this is literally the main navigation.

**Ryan Singer** [02:10:34]
And then imagine that every time I'm moving, like, imagine this is across the top.

**Ryan Singer** [02:10:41]
Like, I'm almost picturing that this is like a global header.

**Ryan Singer** [02:10:44]
Okay.

**Ryan Singer** [02:10:46]
And these things can even have, like, a subline to explain what they are or whatever, you know?

**Ryan Singer** [02:10:52]
it's hitting you over the head, like, what these things are.

**Ryan Singer** [02:10:54]
Then when I'm in experiments or I'm in, like, do more or less or whatever this is,

**Ryan Singer** [02:11:00]
This is monitor, this is performance, this is eval, this is experiments, it's all these things, it needs a name, right?

**Ryan Singer** [02:11:08]
But I think we're getting to what it is.

**Ryan Singer** [02:11:11]
I think this is where your prototype lives as far as the content of your prototype, right?

**Marcel Santilli** [02:11:18]
that's what that is, it's not assignments.

**Ryan Singer** [02:11:22]
And then if I'm in here, what I'm picturing is like, give me the, give me the, I'm going to start stupid, like I'm going to give me the air table of like, this is like, these are pages.

**Marcel Santilli** [02:11:40]
And then what are all the different things that I would be looking at that we could start with what we sketched, which is, again, like every page kind of has this pipeline of like health, visibility, traffic.

**Marcel Santilli** [02:11:58]
And there's no...

**Marcel Santilli** [02:12:04]
Yeah, so let's say I'm here, okay, and then let's say I've got, these actually, these should just be, I should just write these, let's suppose that this is a table, and these are literally the columns, do you know what mean?

**Marcel Santilli** [02:12:25]
And this, traffic, engagement, and like, these things are, and like the page, of course, maybe it has like slug and name, blah, blah, blah, but we're not going to worry about that right now.

**Ryan Singer** [02:12:46]
Can I just say one idea, really quickly?

**Ryan Singer** [02:12:49]
Yes.

**Ryan Singer** [02:12:50]
Like, if you're here, and you see a page, right, that is working.

**Ryan Singer** [02:12:59]
Yeah.

**Ryan Singer** [02:12:59]
Like,

**Ryan Singer** [02:13:00]
If there is a button that says create lookalikes, then it's just like  magical, right?

**Ryan Singer** [02:13:08]
Because then you're just like, show me your top performers, and then you go like, this is a top performer, and you just click a button, and it's just like, go multiply, be a multiply, multiply yourself.

**Ryan Singer** [02:13:21]
And then it creates opportunities, or like, it fetches opportunities, because like, recently, one of the insights, three different people have told me, separately, without editors, is that when you're measuring a prompt, there is create an opportunity from a prompt, and I had three different prospects, and customers said, I really like that about that.

**Ryan Singer** [02:13:42]
Yes.

**Marcel Santilli** [02:13:42]
And it's the only thing they've ever praised about one of our competitors.

**Marcel Santilli** [02:13:45]
Actually, I'm going to do it like this.

**Marcel Santilli** [02:13:51]
This is a dumb way of doing it, but imagine this is just like a button, or a drop down, or a trigger or something, and I get to choose what kind of opportunity it is.

**Marcel Santilli** [02:13:59]
Fix.

**Marcel Santilli** [02:14:00]
It's do more of, you know what I mean?

**Ryan Singer** [02:14:02]
Yeah.

**Ryan Singer** [02:14:02]
delete.

**Ryan Singer** [02:14:05]
And so the key, I think the key observation here that was not, maybe not obvious when we, we have to kind of zoom out and show way less, but the right things at a time, you know?

**Marcel Santilli** [02:14:17]
when we, what we're saying here is this isn't just experiments.

**Marcel Santilli** [02:14:23]
This is like looking at stuff in order to actually, this is like, this is actually where opportunities come from.

**Marcel Santilli** [02:14:29]
You know what I mean?

**Marcel Santilli** [02:14:30]
Not after the, after the strategy wave, there's an initial strategy wave that populates this, right?

**Marcel Santilli** [02:14:37]
But then there is the like monitoring of like, what do we need to do based on what's actually happening based on the performance?

**Marcel Santilli** [02:14:44]
like a picture.

**Marcel Santilli** [02:14:46]
Yep.

**Marcel Santilli** [02:14:47]
Is there like a, if you send me a link and I can copy and paste something, or I don't know if there's a way for me to.

**Marcel Santilli** [02:14:55]
We can do whichever one there.

**Marcel Santilli** [02:14:58]
Here, I just put it in the chat.

**Marcel Santilli** [02:14:59]
I don't

**Marcel Santilli** [02:15:00]
If you can copy and paste what I'm looking at.

**Marcel Santilli** [02:15:02]
here.

**Marcel Santilli** [02:15:05]
I think I can copy and paste it here.

**Marcel Santilli** [02:15:08]
Let me see.

**Marcel Santilli** [02:15:09]
Boom.

**Marcel Santilli** [02:15:11]
Yeah.

**Marcel Santilli** [02:15:12]
What is this?

**Marcel Santilli** [02:15:14]
And then, like, this is the Airtable for Lovable, you know?

**Marcel Santilli** [02:15:20]
And so, like, this is what we managed to do a lot, except this is static snapshot.

**Marcel Santilli** [02:15:28]
then, like, then when you, because then when you go into assignments, it's, like, it's all the work in progress.

**Marcel Santilli** [02:15:36]
But you can never connect the work in progress to how, like, this was the, think of this as, like, this is your temp.

**Marcel Santilli** [02:15:44]
This is your total addressable opportunity market, you know, here.

**Marcel Santilli** [02:15:48]
These are opportunities for new pages, right?

**Marcel Santilli** [02:15:50]
That's why it's showing, like, different domains there.

**Marcel Santilli** [02:15:53]
But it could be for existing, too, right?

**Marcel Santilli** [02:15:55]
Like, it's, like, the only delta between the two is, like, you're trying to do it.

**Marcel Santilli** [02:16:00]
Some work to make it improve, you know, or go higher.

**Marcel Santilli** [02:16:04]
The URL there, that means that we identify that that page will use this much traffic, and doing something similar will be relevant to our personas.

**Marcel Santilli** [02:16:14]
And the one I'm going to send you right now, it's like, what we actually share.

**Marcel Santilli** [02:16:22]
The problem is, the insight we need people to drive is, like, on a cluster level, within, like, one is, like, within this cluster of, like, 300 opportunities or something here, right?

**Marcel Santilli** [02:16:39]
Like, for example, the templates cluster, right?

**Marcel Santilli** [02:16:43]
There's 171 opportunities there.

**Marcel Santilli** [02:16:45]
Which one should you go work on next, the next five or six?

**Marcel Santilli** [02:16:49]
But then also, is that the right cluster?

**Marcel Santilli** [02:16:51]
Should you keep going on this cluster?

**Marcel Santilli** [02:16:54]
Or is this cluster underperforming, and you should double down on a different cluster, you know?

**Marcel Santilli** [02:16:58]
The cluster is like the

**Marcel Santilli** [02:17:00]
a way to like group these opportunities to make sense of these opportunities, right?

**Ryan Singer** [02:17:06]
We don't know, but in the direction that you're going with your UI, like I think there is a grouping at the pages level, so you understand what you have out there, and then there might be a grouping at the opportunity level as well, you know?

**Ryan Singer** [02:17:23]
And what I'm saying here is that now that I'm thinking about it, is that the majority of my insights, even though they might be, hey, they started at a page level, they have to connect back to the cluster level.

**Ryan Singer** [02:17:40]
Otherwise, it's really hard to like understand, because it could be just a, like, a draw of four, it's like, oh wow, pricing pages are doing so much better than brand pages.

**Ryan Singer** [02:17:52]
We should go do, you know, we should go do way more in this cluster, you know?

**Ryan Singer** [02:17:57]
The cluster doesn't have to do.

**Ryan Singer** [02:18:00]
Based on page times.

**Ryan Singer** [02:18:01]
Exactly.

**Ryan Singer** [02:18:02]
Yeah, what I'm hearing is that the opportunity is an orthogonal dimension to the page grouping, right?

**Marcel Santilli** [02:18:12]
The page might be like a blog page or whatever.

**Marcel Santilli** [02:18:15]
might be like a how-to category, but the opportunity is cutting across in a different way.

**Marcel Santilli** [02:18:22]
The key thing that's important for this to feel like – so there's this kind of like rule of thumb that I usually find works for this kind of UI design, which is that like what I need is like this – it's like I can't – I don't want to have more.

**Marcel Santilli** [02:18:41]
I need to pick the like less than 10 things that are like the relevant things at the scale that I'm at and then give me a way to understand how I'm drilling down to give me the next – you know what I mean?

**Marcel Santilli** [02:18:52]
Yeah.

**Marcel Santilli** [02:18:53]
10 things to drill in, right?

**Marcel Santilli** [02:18:55]
Okay, so we don't – I think what you're getting to –

**Ryan Singer** [02:19:00]
Which feels like progress is like this isn't the 1,000 rows or 1,000 columns.

**Ryan Singer** [02:19:05]
And this is the top level of what to do more or less is like what are the things I need to look at to judge what's working and not working?

**Ryan Singer** [02:19:15]
This is for one of our customers called engine.com.

**Ryan Singer** [02:19:18]
And we came up with all these clusters.

**Ryan Singer** [02:19:21]
And within each one of these clusters, like you have – this is more topic clusters than content type clusters.

**Ryan Singer** [02:19:29]
We generated an assignment.

**Ryan Singer** [02:19:31]
And each assignment had like a total volume attached to what's actually performing.

**Ryan Singer** [02:19:37]
Each one of these clusters is performing.

**Ryan Singer** [02:19:39]
And so like – and so clearly you see we paused these other clusters.

**Ryan Singer** [02:19:44]
Yes.

**Ryan Singer** [02:19:44]
And now we only have three active clusters here.

**Ryan Singer** [02:19:47]
And later on we can actually charge per cluster, by the way.

**Ryan Singer** [02:19:50]
Like, you know, because like how many active clusters we can experiment with, you know, and map monitor and, you know, and do things.

**Ryan Singer** [02:20:00]
Yeah.

**Ryan Singer** [02:20:01]
Yeah.

**Ryan Singer** [02:20:02]
So, okay.

**Ryan Singer** [02:20:04]
what we get to is, I'm going to keep kind of playing this out, this line of thinking.

**Ryan Singer** [02:20:15]
Let me just move this stuff so we can refer to it to the side.

**Ryan Singer** [02:20:20]
And then what I want to picture here is if we kind of keep going and let's say that I see something here.

**Ryan Singer** [02:20:30]
Suppose like all of this is clickable, right?

**Ryan Singer** [02:20:33]
You know, so let's say I see something here, which is like health is bad.

**Ryan Singer** [02:20:38]
Okay.

**Ryan Singer** [02:20:39]
And I want know like what's going on or like maybe even there's like a whole bunch of these words like you said it can be systemic, right?

**Ryan Singer** [02:20:44]
I could have like bad, bad, bad.

**Ryan Singer** [02:20:47]
Yeah.

**Ryan Singer** [02:20:47]
Um, I, um, and, and of course, let's just, something can be good.

**Ryan Singer** [02:20:52]
Also, let's say, um, I, uh, again, I know that I'm oversimplifying it, but I think because there's so much.

**Ryan Singer** [02:21:00]
What I'm trying to give you guys is like the macro ideas where you are already going to know how to run with it, you know?

**Ryan Singer** [02:21:05]
like if I click anywhere here, what I'm picturing is like if I click on a value, if I click on the actual page name, like whatever it is, you know what I mean?

**Ryan Singer** [02:21:19]
there's a state, what I'm missing in the UI today that also makes this hard to do, which I think is kind of a really low-hanging thing, is like, okay, top level, I'm in figuring out what to do more or less of.

**Marcel Santilli** [02:21:38]
if I'm in evaluation mode, here's the place where now, in addition to this, a breadcrumb can work for me, which is like everything, and then this is like page, x ways to boost your whatever, right?

**Marcel Santilli** [02:21:57]
And now I'm looking at a page.

**Marcel Santilli** [02:22:00]
And it's almost like, again, this is kind of very, actually, there's probably even a better way to do this that really hits you over the head, which is actually like, page, X ways to boost your whatever.

**Marcel Santilli** [02:22:16]
This is a dumb thing, but like, when we look at the current UI, the page name is the headline, you know, but like, this is so stupid, but it's like, it just like never says page.

**Marcel Santilli** [02:22:28]
And it's one of those little things where like, oh, I'm looking at a page, you know what I mean?

**Marcel Santilli** [02:22:32]
like, always make the headlines domain-specific to your system and not the content.

**Marcel Santilli** [02:22:38]
Yeah, yeah.

**Marcel Santilli** [02:22:38]
You know what mean?

**Ryan Singer** [02:22:39]
And then this is just a kind of thing.

**Ryan Singer** [02:22:41]
There's like this little gotcha that I do in a table and we don't want, like, is that I always give the assignments a generalized name, not the specific name.

**Ryan Singer** [02:22:55]
it's like, you know, X, like.

**Ryan Singer** [02:23:00]
Like, instead of 13, and I used, like, how to guide, instead of, like, you know, it's like, it gives you the general sense of, like, the intent of the assignment and what kind of, it's not, it's like, particular words, so that, like, it feels like, oh, I'm inclined to give you pointers on this headline.

**Ryan Singer** [02:23:25]
It's more of, like, if you were coming through a page that already exists, you would be, like, page, the title of the screen's page, and then you have the actual title of that page.

**Ryan Singer** [02:23:37]
And if it's a new page, and you assign it, it would be an explanation.

**Ryan Singer** [02:23:41]
what I'm going to do here is So what I'm just going to do here is a...

**Ryan Singer** [02:23:48]
let's say I clicked on a bad page.

**Ryan Singer** [02:23:52]
What I'm doing now is what I'm...

**Ryan Singer** [02:23:53]
What I want to do is I'm going to try and repeat the same structure of...

**Ryan Singer** [02:24:00]
we're trying to say what is a page?

**Ryan Singer** [02:24:03]
A page is a physical thing.

**Ryan Singer** [02:24:05]
It's grouping.

**Ryan Singer** [02:24:07]
It's performance.

**Ryan Singer** [02:24:09]
And there's stuff I can do to it.

**Ryan Singer** [02:24:11]
But if this is what a page is, and there's always a performance chunk here, what we can do is we could, for example, this is just one idea, but we could expand out this same organizing principle so I recognize what I'm looking at.

**Ryan Singer** [02:24:31]
So, like, the detailed version of this might be, you know, there's a URL, there's a group, you know what mean?

**Ryan Singer** [02:24:39]
There's an opportunity cluster, you know what mean?

**Ryan Singer** [02:24:43]
This is the spelling out of what was in the first section of the table here.

**Ryan Singer** [02:24:48]
And then in performance, I can, again, have the exact same high level, kind of like what's in the prototype.

**Ryan Singer** [02:24:57]
There's these, like, big dials, you know?

**Ryan Singer** [02:25:01]
imagine I've got, like, inside of, inside of, this is health, okay?

**Ryan Singer** [02:25:11]
Like, health is bad, and I've got a, let's say for every one of these, I can, I can select it, you know?

**Marcel Santilli** [02:25:23]
this would be a different way of doing the drill-in to diagnose or debug or whatever.

**Marcel Santilli** [02:25:38]
Why is this health thing happening?

**Marcel Santilli** [02:25:40]
You know what I mean?

**Marcel Santilli** [02:25:41]
And again, this is visibility.

**Marcel Santilli** [02:25:44]
You know what mean?

**Marcel Santilli** [02:25:45]
This is visibility.

**Marcel Santilli** [02:25:49]
This is traffic.

**Marcel Santilli** [02:25:52]
This and then imagine action.

**Marcel Santilli** [02:25:55]
This is where we could have, and again, I'm just-

**Ryan Singer** [02:26:00]
I'm just using my usual patterns to see if this starts to feel like something that, like, you know, you know where you are and it starts to make sense, which is, like, create opportunity based on this.

**Marcel Santilli** [02:26:11]
And here we could just have one click, one click for, like, the different types, you know what mean?

**Ryan Singer** [02:26:17]
Yeah, it kind of reminds me of a certain thing where we're looking at the customer, you know?

**Ryan Singer** [02:26:21]
Yeah, you can create an opportunity from contact, you know, or you can add an activity to contact.

**Ryan Singer** [02:26:30]
Yeah, it's like, exactly, it's just like acting on a contact, right?

**Ryan Singer** [02:26:35]
Like, oh, I need to reach out again.

**Marcel Santilli** [02:26:36]
Yeah, like, I like the CRM analogy because it's just like, there's a couple of different ways to work, right?

**Marcel Santilli** [02:26:47]
And it feels to me a lot of these explorations and a lot of these thoughts here are really like, do you work and attach activities and contacts to an opportunity and then move the opportunity along?

**Marcel Santilli** [02:26:58]
on?

**Marcel Santilli** [02:26:59]
Or are you

**Marcel Santilli** [02:27:00]
Or are you auditing everything that's already there and then figuring out what your opportunities are based on the performance?

**Marcel Santilli** [02:27:06]
yeah, yeah.

**Marcel Santilli** [02:27:07]
it's like, you can see, there's like not right or wrong.

**Marcel Santilli** [02:27:12]
It's more of like, what will be most valuable to drive?

**Marcel Santilli** [02:27:19]
That's the map of the mall idea.

**Marcel Santilli** [02:27:20]
Like, look, maybe you are hungry and you have to go to the food court before you shop, or maybe you're going to shop until you get hungry and then you're going to eat, you know?

**Marcel Santilli** [02:27:28]
But like, if you know where everything is, you can make your own plan.

**Marcel Santilli** [02:27:32]
But if you don't know where everything is, and you can't get around, you know what I mean?

**Ryan Singer** [02:27:36]
Then, like, you are just lost until somebody like kicks you and says, hey, I need to go.

**Ryan Singer** [02:27:41]
Let me share one side that I think is important here.

**Ryan Singer** [02:27:43]
what I want to do is that, like, when I'm selling or when I'm with customers, the thing that removes the inertia and the thing that shifts the conversation is competitive FOMO.

**Ryan Singer** [02:27:58]
Not yet capturing, like...

**Ryan Singer** [02:28:00]
Those are the things that shift the conversation from like, there's so much to do, to like, hey, can we double the scope?

**Ryan Singer** [02:28:08]
Like, how can we go fast?

**Ryan Singer** [02:28:10]
Sure.

**Ryan Singer** [02:28:10]
And that is the magical switch, right?

**Ryan Singer** [02:28:13]
Like, if you can, and that comes from, like, the magic of doing these audits, everyone's searching that ended up in your customers that don't see you because you don't have surface area that matches that.

**Ryan Singer** [02:28:29]
here's.

**Ryan Singer** [02:28:30]
And if you were to do well with that and capture all of that, you could be, like, three axing your results.

**Ryan Singer** [02:28:38]
And by the way, your competitors are going to be doing it.

**Ryan Singer** [02:28:40]
here's another angle on this.

**Ryan Singer** [02:28:45]
Um, one UI.

**Ryan Singer** [02:28:49]
I select anything I'm interested in.

**Ryan Singer** [02:28:52]
I get a detail pane.

**Ryan Singer** [02:28:55]
I can scroll here.

**Marcel Santilli** [02:28:58]
You know what I mean?

**Marcel Santilli** [02:28:59]
I can find.

**Marcel Santilli** [02:29:00]
Find something else that might be similar, or I could click through different things in the same cluster, for example, right, to see, like, if I'm seeing similar things.

**Marcel Santilli** [02:29:10]
And then maybe I can, you know, I can just X out to close the pane here.

**Ryan Singer** [02:29:16]
here you've got three levels of scale in one view, and it's this UI I got.

**Ryan Singer** [02:29:25]
Like, I am clearly, like, this is clearly made for this task.

**Ryan Singer** [02:29:30]
You know?

**Ryan Singer** [02:29:31]
You mean, like, this would be like a scroll table above, and then it wouldn't come out?

**Ryan Singer** [02:29:36]
Yeah, yeah, so imagine, imagine if, imagine that I've got the, the before here, I think I've been drawing everything on it.

**Ryan Singer** [02:29:47]
For some reason, TLO draw is getting very slow today.

**Ryan Singer** [02:29:50]
Let's see if, if I can get it to behave, escape.

**Ryan Singer** [02:29:54]
imagine that before I select something.

**Marcel Santilli** [02:29:59]
Anything.

**Marcel Santilli** [02:29:59]
Everything.

**Marcel Santilli** [02:30:01]
Just table rows, nothing is selected.

**Marcel Santilli** [02:30:08]
Got it.

**Marcel Santilli** [02:30:09]
it's a master detail.

**Ryan Singer** [02:30:12]
are clusters at the top, not pages.

**Ryan Singer** [02:30:18]
there's a level of detail that I don't know how to get into with the time we have in a single session here.

**Ryan Singer** [02:30:26]
However, I think that if you think of this as, I need to have a distinct place in the UI, which is like, you should be like, if I'm not visiting this every day, or you know what I mean, like regularly, like something's wrong, right?

**Marcel Santilli** [02:30:44]
And like, this is the thing I need to be looking at to know like, what should be doing, what's working and what's not working.

**Marcel Santilli** [02:30:51]
This is basically performance at the end of the day.

**Marcel Santilli** [02:30:55]
Yeah.

**Marcel Santilli** [02:30:55]
And then like, I'm looking at, I'm even inclined just for this moment,

**Marcel Santilli** [02:31:01]
If you show, Ryan, the prompts page for check that has groupings and all that, that's hard.

**Marcel Santilli** [02:31:10]
Yeah, so, this is where you would, if you wanted to see different, you're basically, you're kind of pivoting almost on different groupings or something like that, you know, then this is natural here.

**Marcel Santilli** [02:31:22]
So, I'm not trying to say kind of what happens in this table.

**Marcel Santilli** [02:31:25]
But what I'm trying to say is that, like, I'm looking at pages, that's the unit of key metrics that are important, right?

**Marcel Santilli** [02:31:34]
And then, like, I'm clicking a page to get down to the next level, and then here's where I can drill in to what specifically is not right here.

**Marcel Santilli** [02:31:44]
You see?

**Marcel Santilli** [02:31:45]
Yeah, yeah.

**Marcel Santilli** [02:31:45]
Like, so, in my head, I'm having, like, this clear, kind of picture kind of thing, which is, like, imagine you have, like,

**Marcel Santilli** [02:32:00]
Clusters, right?

**Marcel Santilli** [02:32:02]
Within a cluster type, let's just play with it for a little bit and just imagine like cluster is just a groupie, right?

**Marcel Santilli** [02:32:09]
And instead of each of these clusters, you have identify, with, done, near, and then you have like performance aggregates of those.

**Marcel Santilli** [02:32:20]
And it's essentially like you're clicking in each one of these rows, and each one of these rows is like the cluster.

**Marcel Santilli** [02:32:28]
And when you click on that, you see like a list of potential pages, right, or existing pages.

**Marcel Santilli** [02:32:34]
And every page is either, you know, not execute it, executing, done, or needs of like that cluster because that's what we try to tell clients, right?

**Marcel Santilli** [02:32:49]
It's like, hey, except what happens is we only show them the cluster at the beginning when we identify it, and we never show like the progress against it.

**Marcel Santilli** [02:33:00]
That cluster, because it's so hard to pull that data.

**Marcel Santilli** [02:33:02]
Cluster is just like an impact cluster.

**Marcel Santilli** [02:33:06]
The impact of the cluster is either high impact, average impact, low impact, no impact of that cluster.

**Marcel Santilli** [02:33:15]
And eventually you prioritize the whole cluster because you're like, that's not a focus right now.

**Marcel Santilli** [02:33:20]
you prioritize an entire work stream, you know, because it's just like, you're not on yet, you know.

**Marcel Santilli** [02:33:26]
And there's a limited number of clusters you can focus on at any time, you know.

**Marcel Santilli** [02:33:31]
But the cluster level is how we currently operate when we're doing well.

**Marcel Santilli** [02:33:36]
Because the cluster would be like whatever, and then there's states of the cluster that we're in, or states of the impact Yeah, like, so right now the clusters are, we identify 100 opportunities in this cluster that total to 40,000 monthly traffic, right?

**Marcel Santilli** [02:33:55]
But then that cluster is actually like, hey, we identify 100, and we're currently working.

**Marcel Santilli** [02:34:00]
working on 10, and we already finished 10, and of the 10, all of that aggregate is realized versus unrealized potential, and it is that potential, and then for each one of those, it's either surging, like growing the  up, growing, stable, decaying, or , and we just have to figure out what words to use here instead, you know, and it's kind of like, it's either like, you know, like it's one of those, and that's the aggregate, and that's all the total potential of like 100,000, you realize five, and that five is decaying very fast right now, and it's decaying because click here to find out more, you know, and then from this click down view that you have under here, then that's where you go prioritize work, prioritize work, prioritize work, prioritize prioritize work, or add it to a queue, and and then later on

**Marcel Santilli** [02:35:00]
One, you have to prioritize it, you know, and start the work, you know.

**Marcel Santilli** [02:35:06]
So, kind of, Marcel, based on the way that you just sort of, like, it was like, like all this, like, stuff spilled out of you, like, I feel like, I take that as a sign that this kind of, like, you're seeing ideas of how to run with this.

**Ryan Singer** [02:35:23]
Because I couldn't track all the detail that you shared, you know, because that was very good.

**Ryan Singer** [02:35:28]
Like, but is this, did we get out of, and I'm also, I'm conscious of the fact that we have 20 minutes left.

**Ryan Singer** [02:35:35]
Did we get out of the, like, oh my God, there's, like, so much here, like, we're going to boil the ocean.

**Ryan Singer** [02:35:39]
Did we get out of the woods there?

**Ryan Singer** [02:35:41]
I think so, but I think Daniel and I need to spend, like, a couple hours, like, on, like, refining this a little bit more.

**Marcel Santilli** [02:35:50]
Like, I think, like, I'm just going to use Marcel, but I think, like, that would be, let me see if I'm getting this right.

**Marcel Santilli** [02:35:57]
Like, Ryan, let's see if you can help me with this.

**Marcel Santilli** [02:35:59]
But.

**Ryan Singer** [02:36:00]
But opportunities, assignments, and performance, the way we have there, performance is the same, the pages you have, assignments are the work, opportunities are the ideas, what Marcel just basically is, so.

**Ryan Singer** [02:36:18]
Yeah, and like, I don't want to ask, if I can show you two seconds.

**Ryan Singer** [02:36:24]
Hold on, think, let me, let me, let me, let me, let me draw it back and see if I got it, because I think I attract that.

**Ryan Singer** [02:36:32]
That's where, if, that's what, that was this notion of state, right, like, something that's, okay, I, oh, yeah, I see what you mean, actually.

**Ryan Singer** [02:36:47]
Yeah, yeah, yeah, that's, it's, it's actually.

**Ryan Singer** [02:36:51]
Yeah, target, and, and, and and even if, it has not been created yet, it's still a target, it's still a page, it's just has not.

**Marcel Santilli** [02:37:00]
And so it's just a state of, like, not creating.

**Ryan Singer** [02:37:04]
Yeah, um, I'm, okay, um, what, what I'm missing in that is, um, okay, so, like, there's a version of this where it's, like, it's all in the, in the master table if you just cluster correctly, you know, which I like from a power, precisely, pages is the core, you know what I mean?

**Ryan Singer** [02:37:27]
It's, like, which, which I think is that, yeah, that's actually, like, really interesting, so it's almost like, like, I'm gonna overdo this to, for the, I'm gonna, I'm gonna, like, overpush it to, for clarity, suppose that this is literally, like, home, okay, like, I'm either looking at, like, or, like, I'm almost, like, it's, like, I'm either in, like, like, slash, I'm gonna call it operate for, for the client, you know, like, you know, and then, and then, what I'm, what I'm, what one thing I would be thinking about is, like, like,

**Ryan Singer** [02:38:00]
Filter shortcuts, let's say, let's suppose that you've got exactly, so like you've got like, how do I do this, like if there are, if this is clustered by state, meaning like opportunity, like not created yet, like, you know what mean?

**Marcel Santilli** [02:38:34]
all these things, like it's work in progress, it's already done, it needs improvement, etc.

**Marcel Santilli** [02:38:41]
If this is all clustered by that, the one thing I would think about doing is like, can we help you to sort of see that workflow, not only manually doing it, but that you've got the equivalent of assignments, right?

**Marcel Santilli** [02:39:02]
That's a state, right?

**Marcel Santilli** [02:39:03]
I could be looking at, let's say, assignments as the chosen thing here, right?

**Marcel Santilli** [02:39:09]
Versus, like, identified opportunity.

**Marcel Santilli** [02:39:12]
You know what I mean?

**Marcel Santilli** [02:39:13]
Versus, like, done, or, like, you know, we think that we're done, but, like, kind of, like, needs monitoring.

**Ryan Singer** [02:39:22]
We could even have, like, I should be looking at it, you know, but whatever those top-level things are.

**Marcel Santilli** [02:39:30]
Yeah, yeah, in my head, like, this whole is, like, it's, there's three tabs by cluster, by page, by state, or something, right?

**Marcel Santilli** [02:39:45]
Because, like, it's that, like, that is the content strategy.

**Marcel Santilli** [02:39:49]
That is your strategy, right?

**Marcel Santilli** [02:39:51]
It's, like, it's, how you define everything, and, and then, like, at some point,

**Marcel Santilli** [02:40:00]
When your clusters are really stable and doing really well, like, you do want to drill down by, like, page, right?

**Marcel Santilli** [02:40:08]
But then, like, by clusters, really, like, how it's what gets people excited.

**Marcel Santilli** [02:40:14]
It's what makes sense of the strategy.

**Marcel Santilli** [02:40:17]
It's what the right level of abstraction is for customers.

**Marcel Santilli** [02:40:20]
That's what we do in the strategy sprint, and we focus.

**Marcel Santilli** [02:40:26]
I see.

**Marcel Santilli** [02:40:30]
The cluster is the strategic unit.

**Marcel Santilli** [02:40:33]
It's, like, instead of just looking at lines of code, I'm looking at features.

**Marcel Santilli** [02:40:36]
problem with the cluster today is that the cluster is a snapshot of one in time, and it never gets reinforced throughout, because it's, like, we don't pull real-time data, we don't pull any data, and we don't attach it to the work being done.

**Marcel Santilli** [02:40:53]
And, like, within that cluster, cluster, all it is is, like, a set of pages, and those pages.

**Marcel Santilli** [02:41:00]
Fathom are either identified, being worked on, live, or needs improvement, or needs work, you know?

**Ryan Singer** [02:41:11]
And then within that, like, the growing or surging, you know?

**Ryan Singer** [02:41:21]
And it's kind of, I don't know, like, I know I'm kind of confused, Raymond, or confusing me if he's throwing at it, but it's like, in my head, it's it's like, it's how we operate today with the Airtable, but it's super confusing, and there's a simplified version of this that it's like, oh, easy, because there's this magical thing that happens when I present topic clusters to a client, and I explain why we came up with the clusters the way we did, and when we're grouping in that way, and then I show them how much potential there is in that cluster, they go, holy , this is awesome.

**Ryan Singer** [02:41:59]
And how fast?

**Ryan Singer** [02:42:00]
We to do it, you know?

**Ryan Singer** [02:42:02]
Yeah, I get it.

**Ryan Singer** [02:42:04]
just connect to, like, did it pin out or not?

**Marcel Santilli** [02:42:07]
And why did it work, did it not, did it not?

**Marcel Santilli** [02:42:10]
Yeah, yeah.

**Marcel Santilli** [02:42:11]
I'm just kind of circling back here where there's kind of like, these aren't the right things, this is, there's something, this is more about cluster, actually.

**Marcel Santilli** [02:42:21]
there's some, like, grouping mechanisms of the page, natural indication, and then there's some work state indication, right?

**Marcel Santilli** [02:42:31]
Like, in progress, like, still needs to happen, like, it's done.

**Marcel Santilli** [02:42:36]
And then we're really at that high level where you're talking about the important things.

**Marcel Santilli** [02:42:41]
Yeah.

**Marcel Santilli** [02:42:42]
Yeah, it's like, and if the page doesn't exist and you click on the page, it's really, there's like certain tabs are just not there, or, you know, or.

**Marcel Santilli** [02:42:53]
Yeah, totally, like.

**Marcel Santilli** [02:42:54]
in the .

**Marcel Santilli** [02:42:56]
Oh, yeah, right, right.

**Marcel Santilli** [02:42:58]
the view is different if it doesn't exist.

**Marcel Santilli** [02:43:00]
Yeah, if it doesn't exist, yeah, it's like, yeah, that's really interesting.

**Marcel Santilli** [02:43:05]
Yeah, totally.

**Marcel Santilli** [02:43:06]
So, like, this is, this is like, um, essentially it's like, why is if it doesn't exist, and if a project exists, what it can perform, you know, and what to do next.

**Marcel Santilli** [02:43:20]
Yeah, and they actually, okay.

**Ryan Singer** [02:43:22]
Just, I think, and I, this simplifies so much if we're like, there's just pages, like, there's just pages and text on me, you know, and everything's  pages, that's it, like, you know, and it's just like, so much easier, you know, it simplifies a lot.

**Ryan Singer** [02:43:39]
Yeah, we need to, it's hard, but it's like, it's, I don't think this is ready for me to change the scope of the current cycle, I will just let the guys.

**Ryan Singer** [02:43:49]
But the stuff we're doing in pages is, like, it's super important.

**Ryan Singer** [02:43:53]
It leads to this.

**Ryan Singer** [02:43:55]
I will pause the work in analytics, as in, like, , that is not part of the cycle.

**Marcel Santilli** [02:44:00]
And we just keep going on whatever we have, and then we should do this out.

**Marcel Santilli** [02:44:04]
Yeah, I think if we can get the signals, the six signals.

**Marcel Santilli** [02:44:08]
We can figure out the, we don't spend a lot of cycles on like, maybe the analytics part, or like the grouping of the analytics.

**Marcel Santilli** [02:44:16]
That's what I saying, yeah.

**Ryan Singer** [02:44:19]
Because this impacts everything when we go into the reaction.

**Ryan Singer** [02:44:23]
Ryan, can we clone you somehow?

**Ryan Singer** [02:44:28]
Come help us more.

**Marcel Santilli** [02:44:35]
I think for starting, the gaps actually help us, you know what I mean?

**Ryan Singer** [02:44:41]
Because it creates the contrast, right?

**Ryan Singer** [02:44:43]
you get time to run, and then like, I can contribute something because I've been away, you know, for the month.

**Ryan Singer** [02:44:51]
I think it's a, I think for bang for the buck, I think it's a really good balance right now, the monthly cadence.

**Ryan Singer** [02:44:59]
But let's...

**Ryan Singer** [02:45:00]
Let's revisit it after we do the third one.

**Marcel Santilli** [02:45:02]
Sounds good.

**Marcel Santilli** [02:45:03]
I'm open to that.

**Marcel Santilli** [02:45:06]
What is the next one?

**Marcel Santilli** [02:45:09]
February 17th.

**Ryan Singer** [02:45:10]
17th?

**Ryan Singer** [02:45:11]
Yeah.

**Ryan Singer** [02:45:11]
Is there any chance to move it up a week?

**Ryan Singer** [02:45:14]
Let me look.

**Marcel Santilli** [02:45:15]
If not, it's okay.

**Ryan Singer** [02:45:19]
We're going to work on this and we're to show you next.

**Ryan Singer** [02:45:22]
Yeah.

**Ryan Singer** [02:45:24]
Oh, man.

**Marcel Santilli** [02:45:26]
I'm totally booked that week.

**Marcel Santilli** [02:45:27]
Yeah, that week is slammed.

**Marcel Santilli** [02:45:28]
And the, the, so the reason we, yeah, that's, we, I can't do, I can't do, um, we couldn't move it the whole session to next week.

**Marcel Santilli** [02:45:40]
What I could do is, um, I could do the week of February 1st, um, this second through sixth, I've got, I've got, um, I've got enough slack that I could.

**Ryan Singer** [02:45:57]
I mean, I, I think we could add.

**Ryan Singer** [02:46:00]
Add instead of move, if it's possible.

**Ryan Singer** [02:46:03]
Yeah.

**Marcel Santilli** [02:46:06]
Keep the 17, and if we add, you know, that would be...

**Marcel Santilli** [02:46:12]
Let me make a note and look at what I would have to move around to make this work.

**Marcel Santilli** [02:46:17]
worries.

**Marcel Santilli** [02:46:18]
And then I'll write you guys back to confirm if I can do If we did add, which day would it be?

**Marcel Santilli** [02:46:26]
Could we do third?

**Marcel Santilli** [02:46:28]
It's a board meeting, but that's okay.

**Marcel Santilli** [02:46:31]
Actually, I could also do fourth.

**Marcel Santilli** [02:46:35]
The fourth is perfect because, like, the third is, like, board meeting, but it's in the afternoon.

**Marcel Santilli** [02:46:42]
either could work.

**Ryan Singer** [02:46:43]
fourth is better.

**Ryan Singer** [02:46:46]
I'm already prepping for the board meeting, so I'm not concerned.

**Ryan Singer** [02:46:50]
In our board meetings, I don't do slides.

**Marcel Santilli** [02:46:52]
We just do a...

**Marcel Santilli** [02:46:53]
Okay.

**Marcel Santilli** [02:46:54]
it's like, no, not Let me see if I can move something, and if I can...

**Marcel Santilli** [02:47:00]
And I'll confirm, you know, by tomorrow to let you know if I can do it or not.

**Marcel Santilli** [02:47:05]
Yeah.

**Marcel Santilli** [02:47:06]
And just so you understand a little bit of the urgency, it's less of like, oh, let's just get this right, is that our entire fiscal plan for the year depends on us closing this loop because retention is decaying faster than we go to market.

**Marcel Santilli** [02:47:26]
It depends on us showing something to customers, you know, that feels complete enough end to end.

**Marcel Santilli** [02:47:32]
And, like, and everything we do between now and the end of this quarter will, like, either cause us to go, , let's rethink this thing or let's go put more fuel in the fire, I think, you know.

**Marcel Santilli** [02:47:47]
Yeah, I see.

**Marcel Santilli** [02:47:49]
Tell me, in the eight minutes we've got left, like, help me understand what is the value that you want?

**Marcel Santilli** [02:47:56]
We've got from today.

**Ryan Singer** [02:47:58]
So, the...

**Ryan Singer** [02:47:59]
So, The...

**Marcel Santilli** [02:48:00]
In my perspective, it was like, it was starting to feel very overwhelmed, and we were starting to find core pieces, but it still felt like, , we've got to go build 13 sections of this  project, you know?

**Marcel Santilli** [02:48:18]
And we got to think through all the details in 13 sections, and I think from it, it helped to kind of like, you know, approach this.

**Marcel Santilli** [02:48:29]
Let's not be so tied to the tabs, you know, that to me was the biggest aha, it's like, stop thinking tabs and sections and names, and like, how do we, what are different ways to approach the work, and the impact of the work that we'll have on the outcomes, in a way that's just like, the UI just slaps you in the face.

**Ryan Singer** [02:48:48]
The biggest thing I kind of like, the down is like, daily visit, like, let's nail the daily visit, you know?

**Ryan Singer** [02:48:57]
Like, and if we nail that one screen that if you don't log in,

**Marcel Santilli** [02:49:00]
And every day, you're  up really bad.

**Marcel Santilli** [02:49:02]
Then everything else can be built from there and can be drilled down or other things from it.

**Marcel Santilli** [02:49:07]
to me, was a core insight of keep going.

**Marcel Santilli** [02:49:12]
Keep like, okay, let's try another one, let's try another one, let's try another one.

**Marcel Santilli** [02:49:15]
Then be like, whoa, hold on, there's something here.

**Marcel Santilli** [02:49:18]
That was the value for me.

**Marcel Santilli** [02:49:21]
Yeah.

**Marcel Santilli** [02:49:22]
I mean, this is such a large vertical integration problem.

**Marcel Santilli** [02:49:28]
There's like things everywhere, but the idea of like consolidating into less things and exposing less, if we can land on that, to me, that would be the holy grail.

**Marcel Santilli** [02:49:38]
Because I don't want to build like sales source.

**Marcel Santilli** [02:49:40]
Ideally, we would build like Trello, you know, for, yeah.

**Marcel Santilli** [02:49:46]
And right, well, I think like, well, not a toy, a Trello that starts as a Trello, but you can go down.

**Marcel Santilli** [02:49:52]
Well, you need, you need to have a Trello at the top and a sales force on the bottom.

**Marcel Santilli** [02:49:56]
Exactly.

**Marcel Santilli** [02:49:56]
And a path in.

**Marcel Santilli** [02:49:59]
Yeah.

**Marcel Santilli** [02:49:59]
And I know.

**Marcel Santilli** [02:50:00]
You're kind of like figuring out the parts of the sales force, but then what we're doing, so that's why like analytics might be it, or like it's insights or analytics, but then when you group everything into the core of the page, that does the job.

**Marcel Santilli** [02:50:12]
We had ideas about smart views and all that, and we kind of like went full circle, we ended up, we wanted to have the session about smart views, and what we came up with there, at the end of like Ryan was like doing the groupings, the same thing, smart views, you know, and yeah, yeah, there is something there, and like to be that, that's the value, but at the same time, like, we all, I also have to get the guys building the sales force database on there, even if the UI doesn't get it right, the sales force on there is pretty hard to build it as well, so that is where I need to move the roadmap, like build this, don't give a  about how it looks for a bit, until we nail the Spartan top, so we, when we do the rewrite, it's not a full rewrite off the back end of the rewrite, you know?

**Marcel Santilli** [02:50:55]
Yeah.

**Marcel Santilli** [02:50:55]
Yeah.

**Marcel Santilli** [02:50:56]
Yeah.

**Ryan Singer** [02:50:57]
Yeah.

**Marcel Santilli** [02:50:59]
Awesome.

**Ryan Singer** [02:51:00]
Yeah, this is awesome, man.

**Ryan Singer** [02:51:02]
It's extremely valuable.

**Marcel Santilli** [02:51:04]
And, like, yeah.

**Marcel Santilli** [02:51:07]
Also, if you know any good product people that kind of, like, feel, like, a little bit of, like, boots on the ground, you know, or, yeah.


