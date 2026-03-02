# Growth X Program Review /Update

<metadata>
date: 2026-02-18
time: 20:01 UTC
duration: 46 minutes
organizer: erik@growthx.ai
participants: Erik O'Brien, Brock Walters, John Jeremiah, Ashish Kuthiala
fathom_recording_id: 123485828
fathom_url: https://fathom.video/calls/570402049
share_url: https://fathom.video/share/_gzeyv_q2yTbhti3LbPxNQyHyC4fv1vn
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and FleetDM reviewed the content production program's critical bottleneck: only 6 of ~80 planned articles have been published due to review capacity constraints, despite 4 months of work. Ashish Kuthiala prioritized this as Brock Walters' top priority and committed to a new Google Docs-based workflow to accelerate reviews, with Adrian (a subject matter expert) added as a secondary reviewer. The team agreed to deliver new articles every Wednesday and identified concept-level errors as a key issue requiring tagging separately from accuracy fixes. As an immediate strategic priority, GrowthX will pause work on the main backlog to write 6 Linux management articles, leveraging Fleet's internal expertise for rapid reviews.

---

## Context

FleetDM and GrowthX are working together on a content marketing program targeting device management and IT operations. The program launched in November 2025 with a goal of publishing 20 articles per month (~80 total across four months), focusing on SEO and AI visibility. The collaboration involves GrowthX's content engine (powered by LLMs) producing draft articles, with Brock Walters (FleetDM's Product Education Manager) serving as the primary reviewer and quality gatekeeper. Ashish Kuthiala is FleetDM's CMO overseeing the initiative; John Jeremiah contributes subject matter expertise; Erik O'Brien leads GrowthX's delivery. Adrian, a part-time subject matter expert working with FleetDM, is now being brought in to help with reviews and is leading a parallel project on Linux management content.

---

## Relevance

**To GrowthX Delivery:**
- Content production workflow is being shifted from GitHub PRs to Google Docs for efficiency, requiring updates to Airtable status tracking and internal review processes.
- Feedback categorization (Accuracy, Positioning, Style, and now Concept) will help tune the LLM engine over time; concept-level errors are emerging as the most critical blocker.
- Weekly delivery cadence (Wednesdays) enables predictable content flow and faster feedback loops.

**To GrowthX Business Development:**
- Fleet demonstrates strong commitment to the program by elevating Brock's priority and bringing in Adrian as additional review capacity—signals account health and expansion potential.
- Ashish Kuthiala's request for monthly reporting on AI visibility metrics shows CFO-level interest in measurement and ROI, indicating this is a strategic investment.
- The Linux management series represents a high-value content opportunity leveraging Fleet's unique competitive position.

**To CheckThat:**
- The program serves as a live case study for AI visibility impact; GrowthX uses CheckThat to measure whether LLM-generated content improves keyword citation rates in AI responses.
- Monthly reporting on visibility gains and content attribution will provide valuable data for CheckThat's value proposition and feature development.

---

## Overview

- **Production is stalled:** Only 6 of a planned \~80 articles are published due to a review bottleneck.
- **New Google Docs workflow:** Brock Walters will clear the \~45-article backlog by Friday, using a new process to accelerate reviews.
- **Immediate priority shift:** Production will pause on the main backlog to write 6 Linux management articles, leveraging Fleet's internal expertise for rapid review.
- **New feedback tag:** A "Concept" tag will be added for articles requiring a full rewrite, distinct from simple "Accuracy" fixes.

---

## Key Topics

### Problem: Production Bottleneck

  - **Goal vs. Reality:** The program is significantly behind schedule (6 published vs. \~80 planned).
  - **Root Cause:** A review bottleneck, as Brock Walters was the sole reviewer and had other priorities.
  - **Resolution:** Ashish Kuthiala has made this program Brock's \#1 priority, clearing his other work to focus on the backlog.

### Solution: New Workflow & Backlog Plan

  - **Process Shift:** Reviews will move from GitHub PRs to Google Docs for efficiency.
  - **Backlog Clearance:** Brock will review the entire \~45-article backlog by Friday.
      - **Initial Test:** Brock will review 5 articles first to validate the new process before tackling the full list.
  - **Ongoing Cadence:** Growth X will deliver new articles every Wednesday for continuous review.
  - **Additional Reviewer:** Adrian, a subject matter expert, will also get access to the Google Docs folder to assist with reviews.

### Challenge: Content Quality & Strategy

  - **Quality Issues:** Articles require significant edits, often due to fundamental "Concept" errors (e.g., confusing declarative code with Apple's Declarative Device Management).
  - **SEO Rationale:** Similar-sounding titles (e.g., "Apple MDM" vs. "Apple device management") are intentional, targeting distinct, high-volume keywords.
  - **Prioritization:** Erik O'Brien will provide a list of articles ranked by keyword volume to guide Brock's review order.

### New Initiative: Linux Management Content

  - **Strategic Need:** Fleet's strong Linux management capabilities are a key competitive advantage and entry point into organizations.
  - **Project:** Growth X will write 6 articles for a Linux management series.
      - **Guidance:** The engine will be trained on 2 already-published articles and outlines from Adrian.
      - **Review:** Adrian, Brock, and Alan (internal expert) will provide rapid review.
  - **Future Idea:** Explore bundling existing articles into gated assets (e.g., white papers) for lead generation.

---

## Action Items

**Erik O'Brien (GrowthX)**
- Add Ashish Kuthiala to monthly reporting distribution
- Update Airtable workflow: remove "Ready for GitHub"; add "Ready for review" and "Second review" statuses
- Grant Adrian and Brock Walters folder access to GrowthX Google Docs
- Deliver new articles every Wednesday (ongoing cadence)
- Send keep/merge + pillar list to Brock Walters today or tomorrow morning; then Brock reviews the canonical article for each cluster
- Prioritize Linux management series: draft chapters 3–6 using Adrian's outlines as starting point; send to Adrian for review
- Evaluate e-book/white paper bundling service; report findings back to Ashish Kuthiala

**Brock Walters (FleetDM)**
- Send first 5 Google Docs with feedback to Erik; confirm process works before tackling full backlog
- Clear entire ~45-article backlog with feedback by Friday

**Ashish Kuthiala (FleetDM)**
- Message Adrian re: review coordination and bandwidth availability; tag Erik in Docs when Adrian completes reviews

---

## Transcript
**Ashish Kuthiala:** Hey Ashish, how are you?

**Erik O'Brien:** How's your week going?

**John Jeremiah:** Oh, that's a fun question.

**Ashish Kuthiala:** I'm not feeling too good, but other than that, great.

**Erik O'Brien:** Dealing with the flu like most other people?

**John Jeremiah:** Erik, you're the only meeting he's taking today.

**Erik O'Brien:** Oh, wow.

**Erik O'Brien:** I really appreciate the time.

**Ashish Kuthiala:** So I think that's everyone, right?

**Erik O'Brien:** Yep.

**Erik O'Brien:** That is everyone.

**Erik O'Brien:** Should we just jump straight into it?

**Ashish Kuthiala:** Yeah.

**Ashish Kuthiala:** All right.

**Erik O'Brien:** So I spoke with John a couple weeks ago and kind of just set up the agenda to recap on our goals, talk through status, some challenges we're having, and path forward. At least, you know, where we started back in October, and I wanted to kind of just open it up to see if this still aligns with where we want to go, and if there are many updates from planning sessions or other high-level goals you guys want to focus on for 2026?

**Ashish Kuthiala:** I think the goal and the problem that we plan to solve remains the same.

**Ashish Kuthiala:** The, I'm going to turn to John to ask this, because I haven't been involved at this level, is, did we do any baseline measuring, I know that we looked at different tools to see if are not appearing, but is there a way to measure if we're getting better as we do this?

**Ashish Kuthiala:** I know we haven't published a lot, but once we do start doing that, how do we know we are getting better at this?

**John Jeremiah:** Erik, you guys have the ability to measure, you've got an LLM tracker, don't you?

**Erik O'Brien:** Yep.

**Erik O'Brien:** So we've got you guys set up with, this is our new product we just launched a couple weeks ago.

**Erik O'Brien:** But essentially we track different prompts that query the LLMs on a daily basis.

**Erik O'Brien:** And over time we can kind of see, are we improving in just visibility?

**Erik O'Brien:** So are we showing up for those questions that B2B buyers might be asking?

**Erik O'Brien:** If not, how do we kind of look at the different sources that are being cited?

**Erik O'Brien:** And then create content to fill the gap there.

**Erik O'Brien:** And so once we get into a regular publishing cadence, that's where we've seen, you know, companies like Redis that I work with improve, you know, 5% of visibility over a three month period.

**Erik O'Brien:** The content that we produce starts to get cited in those answers.

**Erik O'Brien:** And so, yes, we have a way to monitor and then kind of keep track of overall visibility.

**Erik O'Brien:** And are we getting kind of cited as a source for some of these questions?

**Ashish Kuthiala:** What's a good frequency to monitor this, once a month, once in three months?

**Erik O'Brien:** We typically report out once a month on overall metrics, so that everything from traffic and engagement rate to cohort performance and AI visibility.

**Erik O'Brien:** So, yeah, typically, you know, publish consistently and then check about once a month to see if we're moving the needle.

**Ashish Kuthiala:** Right.

**Ashish Kuthiala:** So I don't know if you're already doing that.

**Ashish Kuthiala:** If not, I would love to be part of that.

**Ashish Kuthiala:** Right.

**Ashish Kuthiala:** Checkpoint.

**Erik O'Brien:** Yeah.

**Ashish Kuthiala:** And, all right, so that was, that's good.

**Ashish Kuthiala:** I just wanted to ask that question.

**Ashish Kuthiala:** My next question is, I know we kind of, like, signed the agreement in October.

**Ashish Kuthiala:** We kind of started in November-ish time frame.

**Ashish Kuthiala:** Okay.

**Ashish Kuthiala:** So, November, December, January, almost February, four months, at the rate of 20 articles, 20 blogs a month, we should have had 80 published, theoretically.

**Ashish Kuthiala:** Okay.

**Brock Walters:** The only thing I'll say about this number, Erik, is that I feel like it should be revised, given the list of redundant titles that I just gave you.

**Brock Walters:** But you tell me.

**Erik O'Brien:** Yeah, I'm doing analysis on that with some recommendations, but not quite finished with that yet.

**Brock Walters:** Okay, so the articles drafted really isn't 50, assuming that all of those really are duplicates.

**Brock Walters:** And in my estimation, there's quite a few.

**Brock Walters:** So I think it's more like 30, but I don't know.

**Ashish Kuthiala:** So more or less, we should have been on track for around 40 of them.

**Brock Walters:** Yeah.

**Ashish Kuthiala:** Even if it's not 50, but we have done six, which is, you know, there's an issue of, you know, why this pipeline isn't working.

**Ashish Kuthiala:** So let's talk about that.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So I think the, the real kind of what it comes down to is, you know, we've got...

**Ashish Kuthiala:** Was it last week?

**Ashish Kuthiala:** No, last week, yes.

**Brock Walters:** It was last week.

**Ashish Kuthiala:** And so when Brock is also brand new to this team, was doing a lot of things, and this became one of the many things that were on his plate.

**Ashish Kuthiala:** And what we did last week was we cleared his other things off of his plate, and this is one of his highest priorities to work on.

**Ashish Kuthiala:** So he's, you know, that was on me, and I've helped Brock get rid of everything else.

**Ashish Kuthiala:** In fact, so much so that this is his number one priority, and to get the black backlog cleared so that we get to a point where he can do one a day.

**Ashish Kuthiala:** He's almost not touching any other projects.

**Ashish Kuthiala:** So that's the left-hand side.

**Ashish Kuthiala:** And in addition to that, I'm also looking for other technical content experts who can hire on a contract basis, who can come and help.

**Ashish Kuthiala:** Do things like reviewing these articles, but the challenge becomes finding somebody with the domain expertise who understand these articles.

**Ashish Kuthiala:** I did find one or two people.

**Ashish Kuthiala:** They're willing to work.

**Ashish Kuthiala:** They're ex-JAMF employees, for example.

**Ashish Kuthiala:** I cannot hire them for another two or three months.

**Ashish Kuthiala:** So we don't even want to touch them because we've had issues in the past where, like, they come nipping at our heels if we talk to such people.

**Ashish Kuthiala:** I'll leave it at that and let you read between the lines.

**Ashish Kuthiala:** I am not supposed to tell you to go hire them or anything, right?

**Ashish Kuthiala:** And then I can't.

**Ashish Kuthiala:** So I'm still looking, but if you find some, you know, folks like that, and if we will talk about that off after this, but if, if, if there's a way that, you know, you could use some extra help and you want to pass through that charge to us for a temporary period of time, let's consider it.

**Erik O'Brien:** Okay.

**Brock Walters:** Which was, and I want to give a big shout out to Erik for this because we did a meeting very late on Friday night, which he took at the last minute.

**Brock Walters:** So again, thanks for doing that, Erik.

**Brock Walters:** I thought that was a really good customer service experience.

**Brock Walters:** So what I haven't done is put anything in the format we discussed on Friday, which is I'm going to use their Google Docs and mark everything up there.

**Brock Walters:** And, you know, that doesn't mean, I do want to say that I think that there's a sense in which doing this first set of edits, having read all of the articles at this point, is going to take as much time as it would to rewrite them.

**Brock Walters:** But I'm committed to doing this and I'm, I will probably be done with all, everything in the backlog in next couple of days.

**Brock Walters:** So, um, and, and Erik has.

**Brock Walters:** He that the way it would make the most sense for them is to either do inline edits or comments in the Google Docs rather than doing editing in GitHub.

**Brock Walters:** I know, John, that we had talked about using GitHub for the editing process.

**Brock Walters:** I'm not sure that the folks on the GrowthX side are...

**Brock Walters:** I don't think that would be as efficient.

**Brock Walters:** And Erik, I think, agrees with that.

**Brock Walters:** And the only reason they exist as PRs is so that they can get published to the website.

**Brock Walters:** So I'm fine with doing the editing where...

**Ashish Kuthiala:** Brock, what I'm hearing is you're solely working on the feedback right now, and you are working in the format that Erik would like it to be so that he can make them better.

**Ashish Kuthiala:** And then in about two days, let's say by Friday, you should be able to give feedback to all of the backlogged ones, which are around 45 articles.

**Brock Walters:** Yep.

**Brock Walters:** Well, less if we're weeding...

**Ashish Kuthiala:** So you should be able to clear the backlog on your end to give feedback by Friday.

**Brock Walters:** Exactly.

**Ashish Kuthiala:** That's really cool.

**Ashish Kuthiala:** My suggestion would be to pick five and give feedback, like, say, by today or something.

**Ashish Kuthiala:** So Erik can give you feedback, if that's the way I want it or not, rather than get all 45 and say, yeah, this isn't going to work, we should do it some other way.

**Brock Walters:** I mean, just that's my suggestion.

**Brock Walters:** I'll let the two of you work.

**Brock Walters:** No, that's fine.

**Brock Walters:** I'm happy to do that.

**Ashish Kuthiala:** Right.

**Ashish Kuthiala:** And then, Erik, you know, we'll see, you know, how much time.

**Ashish Kuthiala:** So what I'm interested in knowing is, like, how long does that feedback loop take?

**Ashish Kuthiala:** It may take longer initially.

**Ashish Kuthiala:** Yeah.

**Ashish Kuthiala:** But what I would love to do is when you get feedback, you know, we're not going to do this going forward.

**Ashish Kuthiala:** Don't wait to give Brock feedback on all 45 again.

**Ashish Kuthiala:** I mean, as soon as you see one, you know,

**Ashish Kuthiala:** to do, that's great.

**Ashish Kuthiala:** Send it back to him.

**Ashish Kuthiala:** Send it back to him.

**Ashish Kuthiala:** Just open that pipeline.

**Ashish Kuthiala:** I think you know what I'm saying.

**Ashish Kuthiala:** I want him to get them back as soon as you're working on them and make a steady stream of articles back for his review rather than him getting 45 back in one chunk as well.

**Erik O'Brien:** Yep.

**Erik O'Brien:** Yeah, absolutely.

**Erik O'Brien:** We'll definitely take them as we get them and make updates and then push back for, you know, second review.

**Erik O'Brien:** So we'll make a couple updates just in the way that we manage those documents in Airtable.

**Erik O'Brien:** Brock, so he's familiar with kind of how we run the.

**Brock Walters:** And by the way, is all the stuff that I did in there, did everything make sense that I did in there?

**Erik O'Brien:** Yeah, did.

**Erik O'Brien:** Yeah, I went through and checked that yesterday.

**Brock Walters:** So we'll add a couple extra steps.

**Brock Walters:** Let me ask you something.

**Brock Walters:** Oh, sorry, go ahead.

**Brock Walters:** Go ahead.

**Erik O'Brien:** I would say we'll just add a couple steps so that, you know, we'll remove the ready for GitHub and update these client views.

**Erik O'Brien:** So.

**Erik O'Brien:** We'll have it ready for review, it'll come back to growthx, and then we'll push it for second review.

**Erik O'Brien:** And then once it's passed through to that, then we'll have it kind of pushed for, then ready to upload to GitHub.

**Brock Walters:** Okay.

**Brock Walters:** But we still need that step, because it won't get published on the website without that, but it just doesn't need to be ever really sitting in that step.

**Brock Walters:** If something is getting to the PR, it's going to be published.

**Ashish Kuthiala:** I want to get to the converting into PR process and step just a bit later.

**Ashish Kuthiala:** Right now you write something, it shows up as a Google Doc for Brock, Brock marks it up, sends it back to you, it goes through one cycle or a couple of cycles, whatever it is, then it gets turned into a PR.

**Ashish Kuthiala:** So between the two, it should remain in a Google Doc.

**Brock Walters:** We all agree on that, right?

**Erik O'Brien:** Yeah.

**Ashish Kuthiala:** Okay, awesome.

**Ashish Kuthiala:** What we are also doing, Eric, I have another person working, he's been working with us part-time, he's a subject matter expert.

**Ashish Kuthiala:** You may have met him at one point.

**Ashish Kuthiala:** I'm trying to get his help to help Brock so that Adrian can help.

**Ashish Kuthiala:** So he's also going to work off of Google Docs.

**Brock Walters:** And I did give him access to the articles, the comparison articles.

**Brock Walters:** He should have Google.

**Brock Walters:** In other words, he's going to be working out of the same Google Docs that I am.

**Ashish Kuthiala:** So he should have access to that.

**Ashish Kuthiala:** Instead of giving him, do they land in a folder, Erik?

**Erik O'Brien:** Yep.

**Ashish Kuthiala:** Can we give Adrian and Brock access to the whole folder?

**Ashish Kuthiala:** Yep.

**Ashish Kuthiala:** Instead of article by article.

**Ashish Kuthiala:** The reason I say that is once he's done with the comparisons, if he has bandwidth to, because he spends about four hours a week with us.

**Ashish Kuthiala:** And if he has bandwidth, then maybe we can get him to start reviewing some documents as well.

**Erik O'Brien:** Yeah, absolutely.

**Ashish Kuthiala:** Okay.

**Ashish Kuthiala:** Awesome.

**Erik O'Brien:** Yeah, I saw him comment on a Kanji article.

**Erik O'Brien:** Great.

**Erik O'Brien:** So I will use his email and just grant him access.

**Brock Walters:** Yeah, kind of think that I must have access to everything already.

**Erik O'Brien:** Yeah, you should, but I'll double check.

**Ashish Kuthiala:** I'm going to send a message to Adrian saying, because the other thing is Adrian has a full-time job doing other things, but I don't know how we don't step on each other's toes.

**Ashish Kuthiala:** mean, so once Brock or Adrian reviewed, what do they do?

**Ashish Kuthiala:** They just move it in the air table that's ready to be reviewed, or what do they do?

**Erik O'Brien:** They can just tag me.

**Erik O'Brien:** It's like, hey, review's done.

**Erik O'Brien:** Like, in the Google Doc.

**Erik O'Brien:** So they'll just tag my name, say review's done, then we'll move it through air table and through our internal editing and review process.

**Ashish Kuthiala:** Okay.

**Erik O'Brien:** You managed to able to take that.

**Erik O'Brien:** Yeah, we manage the air table.

**Erik O'Brien:** Brock can manage things from, like, approving articles that are in the backlog.

**Brock Walters:** But I'd rather not.

**Erik O'Brien:** Production, yeah.

**Brock Walters:** Also, all I'd rather do is just set the status to let you guys approve.

**Brock Walters:** Approving the titles in there is fine.

**Ashish Kuthiala:** The reason I asked about that part of the process is Adrian, and I don't talk, he's working on a project for me writing articles on some Linux management by Fleet, but when he's done, he has said he can help with the reviews of this.

**Ashish Kuthiala:** So just trying to figure out how that would work.

**Ashish Kuthiala:** So that helps me.

**Erik O'Brien:** So we can keep moving.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Yeah, so for reviews, Brock, I kind of was talking to John about like, how do we ensure that we're making progress and be able to track kind of what type of feedback we're getting.

**Erik O'Brien:** And so this is just a proposal of like, if we're flagging accuracy, like using that as a tag before you kind of leave feedback.

**Erik O'Brien:** If it's positioning, like kind of how we were going from cross-platform to multi-platform, that type of framing issue.

**Erik O'Brien:** Style, I think is.

**Erik O'Brien:** It's stuff that we'll be able to tune, more feedback we get, but it's just tone, word choice.

**Brock Walters:** that's the least of my worries.

**Brock Walters:** The style has not been the problem.

**Erik O'Brien:** Yeah.

**Brock Walters:** Accuracy is doing a lot of work there.

**Brock Walters:** Yeah.

**Brock Walters:** Because, again, I wouldn't, I am not meaning to be the one that's in the bus pulling the emergency brake, but it's, again, I don't want to go too deep into this.

**Brock Walters:** But this is, it's, it's deeper than, like, this fact is wrong.

**Brock Walters:** It's like the whole conceptual, conceptual framework is wrong sometimes.

**Brock Walters:** And, and that's, so, I mean, I guess you could say that it's inaccurate if the conceptual framework is wrong.

**Brock Walters:** If you're confusing declarative code with Apple's declarative device management framework, and the whole article has been written so that those two concepts are completely fused together.

**Brock Walters:** But I, you know, that's, that's different than an accuracy problem.

**Ashish Kuthiala:** So, Brock and Erik, I think at some point, if it's possible, it's more work, but not at a granular level, but even at a broad, higher level.

**Ashish Kuthiala:** If we can get a sense of, of the act, of the feedback given, 80% of them were wrong, you know, in terms of accuracy, or 80%, you know, or 20% were wrong on accuracy, the others on the framing, I think it might help us understand how to fine tune the engine.

**Brock Walters:** Sure.

**Brock Walters:** Are these the only attributes, Erik?

**Brock Walters:** I mean, are these meaningful attributes for you, or were these just ones you guys came up with?

**Erik O'Brien:** These are just ones I came up with, the ones that we see most often, and kind of in the earlier stages.

**Erik O'Brien:** so, yeah, and rank them as, accuracy is obviously our blocker.

**Brock Walters:** Well, I would add one other, I would add one other, which would be concept.

**Brock Walters:** Right?

**Brock Walters:** That the concept has to be right.

**Brock Walters:** And that's something that it's not, it's not that I've seen it once.

**Brock Walters:** I've seen it in 10 or 15 of the articles where the title, you know, the concept of the title is in the article, but it's just mishmashed with 10 other IT things.

**Brock Walters:** Which is exactly the way you would expect an AI to write an article about this stuff that didn't know.

**Brock Walters:** So I would say concept.

**Brock Walters:** And concept to me, if I put that, if I'm going to put that tag on something, it's a complete rewrite.

**Brock Walters:** You know what mean?

**Brock Walters:** Because you have to start over.

**Brock Walters:** These other ones, those are easy to fix.

**Brock Walters:** And I hope this is, you know, I hope this is the way they go from this point forward.

**Brock Walters:** What I've read so far, you know, which is basically every single thing you guys have.

**Erik O'Brien:** And technical marketers for VR content, and it was pretty ugly at the beginning.

**Brock Walters:** I can imagine, because you can ask five software engineers, five different software engineers what Redis does, and you would get five different answers.

**Erik O'Brien:** Yes, absolutely.

**Brock Walters:** Because it does all sorts of different things.

**Brock Walters:** It's a database cache.

**Brock Walters:** It's a caching mechanism.

**Brock Walters:** It's a queuing mechanism.

**Brock Walters:** Yeah, I get it.

**Erik O'Brien:** And now they're getting into AI and vector databases and all the new products that they're trying to launch.

**Erik O'Brien:** And similar to Fleet, like the LLMs know what Redis has been, not what it wants to be.

**Brock Walters:** Yeah, yeah.

**Erik O'Brien:** And so we had to do a lot of different tooling to fix that.

**Brock Walters:** Okay.

**Brock Walters:** Well, I mean, that gives me some confidence that, you know, that's a high technical hurdle, and I feel like this one is the same, or maybe slightly lower, but high, you know.

**Erik O'Brien:** Just as important, though.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Okay.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Yeah, think given we've ramped through most of the kind of post-solution, like getting the Google Docs workflow, I think I want to, you know, try to get on a weekly cadence of like, hey, we deliver on X day, and that way you guys know when they're coming.

**Erik O'Brien:** For us, you know, I think Wednesday is probably a good target to give Gabby like a couple days in the beginning of the week to ramp up on production, and to be able to deliver them by Wednesday, so you just know that they're consistently going to be there on that same day.

**Erik O'Brien:** And then this is something we discussed early on in the engagement, and I think hopefully we can get to here, but if we start reviewing articles by cluster, really deeply in the beginning, and then hopefully as the model improves, and we get better outputs, then it's more of a spot.

**Erik O'Brien:** Check before we can get to submitting to GitHub, obviously this is not near-term, but once we get through a comfortable stage, then hopefully we can get to a better volume.

**Brock Walters:** So I guess I just want to go back to, this is not me trying to get out of work, it's me trying to deliver closing out the backlog.

**Brock Walters:** What are we going to do about the titles that I flagged as duplicates for articles that have already been written?

**Brock Walters:** Is there a way that we have, and this is something Ashish and I talked about yesterday, it's like, you guys are the experts on the headlines that you've given us.

**Brock Walters:** Because what I'm assuming, we all assuming you're doing is maximizing the SEO benefit.

**Brock Walters:** So I guess, and maybe this is a dumb question, I don't know, but the question is, can you help us pick the best headline under which to collapse subjects that we think?

**Erik O'Brien:** Yes, absolutely.

**Erik O'Brien:** We'll go for the highest search volume that has the same intent and same kind of keyword alignment.

**Erik O'Brien:** There are some that you proposed condensing that have basically, you know, it's the same concept, if you will, but completely different keyword targets.

**Brock Walters:** Yeah.

**Brock Walters:** And that's, I guess, what I'm concerned about, right?

**Brock Walters:** Because I don't understand this game.

**Brock Walters:** I'm willing to try and play it.

**Brock Walters:** But I also, I don't want to lose the benefit of that if you guys are saying that that's valuable.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Well, I have an opinionated point of view on some of those.

**Erik O'Brien:** For like the Apple device management cluster that you pointed out, there's several of those can be condensed into one canonical article.

**Brock Walters:** Right.

**Erik O'Brien:** So, yeah, just a preview.

**Erik O'Brien:** Like I'm going through each one and saying like keep or merge into the above.

**Brock Walters:** Okay, cool.

**Brock Walters:** So you're, that's amazing.

**Brock Walters:** Okay.

**Brock Walters:** So if you can just give me the ones that you're going to use, like the one we're going to collapse everything under as soon as possible, that would be great.

**Erik O'Brien:** Yeah, absolutely.

**Brock Walters:** That would be super helpful.

**Erik O'Brien:** I should be able to get that over to you today.

**Brock Walters:** Okay, awesome.

**Erik O'Brien:** If not, tomorrow morning at the latest.

**Brock Walters:** And then, I guess this is maybe a Captain Obvious question, but is everyone on board with me reviewing that article and not the other ones?

**Brock Walters:** And then will you guys make adjustments for, meaning if we've decided that these seven articles are really on the same topic, we've picked one headline for its maximal SEO value.

**Brock Walters:** Is it okay if we review just that one and then get whatever benefits we get from the keywords by putting them in the article or something?

**Brock Walters:** Is that how it's going to work?

**Erik O'Brien:** Sort of.

**Erik O'Brien:** So let's just take this for example, like all these are basically the same article with different trailers.

**Erik O'Brien:** Apple device management is what we're targeting.

**Erik O'Brien:** Apple MDM is a slightly different keyword target just because some people type it into Google differently.

**Erik O'Brien:** And then how to manage Apple devices at scale is also a different keyword target.

**Brock Walters:** Okay.

**Erik O'Brien:** So we'll come up with rationale of like why we keep things versus what gets merged.

**Brock Walters:** So, John, maybe this is a question for you because you've schooled me up on why the headline should say Linux MDM.

**Brock Walters:** But Apple device management and Apple MDM are the same thing.

**Brock Walters:** So do we really need three different guides because we're trying on the exact same topic?

**Brock Walters:** question right type of And we're trying trying the same thing

**Brock Walters:** Different keywords.

**Brock Walters:** Like, I'm happy to do it however it's going to benefit Fleet the most.

**John Jeremiah:** just...

**John Jeremiah:** The rationale, the reason you do it is people search for that term.

**John Jeremiah:** If they type that into Google, you want to, in playing this game, part of the goal here is to have content that talks, that answers that question.

**John Jeremiah:** And in the same way, if somebody types that into an LLM...

**John Jeremiah:** So, yeah, I mean, it's...

**Brock Walters:** If you have three definitive guides, you don't have a definitive guide.

**John Jeremiah:** That's fine.

**John Jeremiah:** But it is for that person who finds it.

**Brock Walters:** I just want to figure it out.

**Brock Walters:** How do we have a definitive guide if we have three of them?

**John Jeremiah:** Yeah, I mean, it is for the person who finds it definitive for them.

**Brock Walters:** Okay.

**John Jeremiah:** You know, at the end of the day, I mean, the goal ultimately of doing this is, and this is always a challenge when it comes to marketing is, and frankly, we're wrestling with it here.

**John Jeremiah:** I've wrestled with...

**John Jeremiah:** With it everywhere is somebody who's a founder or a product manager thinks, oh, I'm going to call, you know, I'm going to call it, I don't know, device, I don't know, I'm trying to think of something on the fly that would be different, but they come up with their own unique witty way of talking about it and they want to message around it.

**John Jeremiah:** It doesn't work like that.

**John Jeremiah:** People aren't searching for your witty way of talking about it, but they are searching for it using the terms that they feel comfortable with, and so, therefore, the challenge as a marketer is, how do you get in front of them?

**John Jeremiah:** It's the joke about the guy who's searching in the parking lot underneath the light looking for his keys, and the guy comes out and says, what are you doing?

**John Jeremiah:** Well, I'm searching for my keys.

**John Jeremiah:** Well, where'd you last have them?

**John Jeremiah:** Well, had them over there, but well, why are you searching here?

**John Jeremiah:** Well, because this is under the light, you know, you got to go where the keys are to go find the people, not just where you want to be.

**Brock Walters:** I agree.

**Brock Walters:** completely agree that we should be using accepted terms that the market is familiar with.

**Ashish Kuthiala:** So, here's the thing.

**John Jeremiah:** And terms that we don't agree with that people use.

**Brock Walters:** mean, it's like LytxMDM is a great example of something.

**Brock Walters:** terms that we don't agree with that come from all directions.

**Ashish Kuthiala:** I'm going to time out this discussion.

**Brock Walters:** Please.

**Ashish Kuthiala:** I want Erik to go through the rest of his presentation and I want, Erik, if you have time, like 10 minutes with you towards the end.

**Erik O'Brien:** Yeah, absolutely.

**Ashish Kuthiala:** So, let's go through what else that you have.

**Erik O'Brien:** Yeah, I think just kind of on that, like to expand.

**Erik O'Brien:** So, we take this topic clusters approach and really what that does is we plant the seeds, like John was saying, based off keyword volume.

**Erik O'Brien:** So, how often is that keyword searched per month for the audiences we're going after?

**Erik O'Brien:** What that's really trying to do is, you know, based off, you know, not only people searching, but also LL.

**Erik O'Brien:** Is how do we start to talk about the different solutions that are out there for Apple MDM versus Apple device management, specifically looking at how do we manage it, given that we probably have an Apple MDM, and start to target maybe enterprise buyers versus a complete how-to guide.

**Erik O'Brien:** So there's different angles we can take, even though titles may seem very similar.

**Erik O'Brien:** I think it's just the kind of long tail that we need to update and not have as consistent across different...

**Ashish Kuthiala:** In terms of priority, Erik, do you, because we are behind, do you prioritize the standard, sorry, if you go back to that slide, do you prioritize the pillar one first and the rest of them, you know, if we need to write them come later, or do you want to finish that cluster and then go to the next cluster and then go to the next cluster?

**Erik O'Brien:** So we typically, especially early on, try to target whatever the highest...

**Erik O'Brien:** So Apple device management probably has 2,000 4,000 search on a monthly basis.

**Erik O'Brien:** So we'll definitely target the highest keyword as the pillar, and then we can go after these standalone articles that are in the same cluster.

**Erik O'Brien:** But ideally, we, especially early, try to put out different topics across all clusters.

**Erik O'Brien:** And that gives us, you know, as we start to look at performance to see what are people actually searching and reading.

**Ashish Kuthiala:** I guess I was asking the question as to, like, because we have a bottleneck here with Brock, if we can prioritize even within this?

**Erik O'Brien:** Yeah.

**Ashish Kuthiala:** So, you know, that's what I was thinking about.

**Erik O'Brien:** Yeah, I've got a different sheet I'm working through that's a lot messier, but it not only has kind of the category and article title, but has keyword volume with it.

**Erik O'Brien:** So I'll go through that and prioritize, these are the.

**Erik O'Brien:** The we're keeping, and these are the ones that are pillars with the highest search volume, so we can prioritize reviewing those first.

**Brock Walters:** Okay.

**Brock Walters:** If you can get me this list, I'll work with it, you know, whatever you give me.

**Erik O'Brien:** Okay.

**Brock Walters:** And, you know, if you need to keep ones that I've flagged as duplicates, that's not an issue.

**Brock Walters:** I understand the system now.

**Erik O'Brien:** Okay.

**Erik O'Brien:** Yeah, I think that's really the kind of gist of a lot of the points I wanted to talk through today.

**Erik O'Brien:** think there's a whole other kind of presentation that I put together just based off Marcel's talking points about, like, why we do the things we do the way we do.

**Erik O'Brien:** But I think it'd be better delivered by Marcel when we do kind of a larger educational kind of session with the team.

**Ashish Kuthiala:** I'm going to ask you a different question.

**Ashish Kuthiala:** I wasn't involved in the content strategy and the topic cluster.

**Ashish Kuthiala:** to ask you I'm

**Ashish Kuthiala:** And this is generally bringing traffic to our website, looking at the search volumes.

**Ashish Kuthiala:** One of the things that might be in here, but I think what's missing here is our main go-to-market this year is to go after Jamf, which is the Apple ecosystem, right?

**Ashish Kuthiala:** They manage Apple, and we're trying to win most of our revenue from that.

**Ashish Kuthiala:** But in the world of MDM, I'll just use that term, in the world of, you know, managing different kinds of operating systems, there are not many vendors who manage Linux workstations and devices in corporate environments.

**Ashish Kuthiala:** And we are kind of, like, one of the really good ones, and we tend to win those deals, and they act for us as an entry point into the organization to maybe expand into other areas. We're not putting a lot of effort into marketing that, but I've been working as fast as I can with my knowledge, kind of building content to build an online presence and attract traffic looking for Linux management to our site.

**Ashish Kuthiala:** We have a few how-to articles and technical articles already there, but, you know, we don't have, for example, a web page on the main website that kind of says, hey, we do Linux management, and this is how we do it.

**Ashish Kuthiala:** We have some of the more how-to articles.

**Ashish Kuthiala:** So we've solved it kind of on this side, but not like on the, you know, marketing side, if that makes sense on the website.

**Ashish Kuthiala:** So I've been doing my own mini-project unrelated to yours, trying to kind of write some stuff there, and Adrian has been helping me.

**Ashish Kuthiala:** So we have...

**Ashish Kuthiala:** We have a strategy around a blog series around Linux management.

**Ashish Kuthiala:** How many are there, Brock?

**Brock Walters:** think six or eight.

**Brock Walters:** There's three are written, and I think there's seven planned.

**Ashish Kuthiala:** Right.

**Ashish Kuthiala:** So around 10 blogs that we will write, Erik, that for me is good enough for the website.

**Ashish Kuthiala:** And then I am working with our web designer to put a main web page up for Linux management.

**Ashish Kuthiala:** I wanted to ask you, because Adrian is kind of busy in his day job.

**Ashish Kuthiala:** He was supposed to write those seven other blogs.

**Ashish Kuthiala:** Whether it's possible, I mean, can we get your help in writing the seven other blogs and getting Adrian to kind of review them and add to them? If that makes sense, instead of him writing them from scratch, he has written some outline of what each one of those blogs will talk about.

**Ashish Kuthiala:** If I can find it, I'll share with you.

**Ashish Kuthiala:** I don't know, Brock, if you have it.

**Brock Walters:** Yeah, I have it.

**Erik O'Brien:** I guess the short answer is absolutely.

**Ashish Kuthiala:** Right.

**Ashish Kuthiala:** Because I think, like, that's a quick, we have somebody who can review it.

**Ashish Kuthiala:** Brock's been reviewing them too, but, you know, let's, we have Adrian kind of ready.

**Ashish Kuthiala:** I mean, he's not finding the time to write them.

**Ashish Kuthiala:** So this was kind of like his plan and outline for the series.

**Ashish Kuthiala:** So he's already written one.

**Ashish Kuthiala:** We have published it.

**Ashish Kuthiala:** He's already written two.

**Ashish Kuthiala:** We have published it.

**Ashish Kuthiala:** Have you published it, Brock?

**Ashish Kuthiala:** Yep, there's two published ones.

**Ashish Kuthiala:** And so here's kind of like, you know, chapter three, chapter four, five, six.

**Ashish Kuthiala:** Well, I guess there's only six.

**Ashish Kuthiala:** I thought there were more.

**Brock Walters:** I thought, I thought, no, there's only six chapters.

**Ashish Kuthiala:** I was wrong.

**Ashish Kuthiala:** Okay.

**Ashish Kuthiala:** So.

**Ashish Kuthiala:** So I'm just thinking about this, and given that we have written one and two, if you feed that into your engine and give them guidance for, you know, the rest of them, this is something we can get back fairly quickly from you, and we can get Adrian to kind of like review them and do this.

**Ashish Kuthiala:** So this would be off our plate to kind of have a Linux.

**Ashish Kuthiala:** It's not in your clusters and your keyword research, et cetera, but I do still want these published.

**Erik O'Brien:** Yeah.

**Ashish Kuthiala:** Okay.

**Ashish Kuthiala:** So, okay, we have the links to...

**Brock Walters:** And I just shared it with you, Erik.

**Erik O'Brien:** Wonderful.

**Ashish Kuthiala:** Okay.

**Brock Walters:** I mean, you could create another cluster, though, right, for Linux management?

**Erik O'Brien:** Yeah, I think we had Linux under cross-platform device management.

**Brock Walters:** I see, but not as a separate cluster.

**Erik O'Brien:** Not as its own, yeah.

**Ashish Kuthiala:** The reason I brought this up is like we are waiting for feedback from Brock on 45.

**Ashish Kuthiala:** So instead of continuing to produce others, pick this stream up and develop this and I have Adrian and then I'm talking to somebody tomorrow and then I have Brock like who know Linux and we have somebody internally, Alan as well who knows Linux so we can get these published faster.

**Erik O'Brien:** Yeah, we will put these in the priority queue for next week.

**Brock Walters:** Cool.

**Ashish Kuthiala:** So chapter three is written?

**Brock Walters:** I didn't know that.

**Ashish Kuthiala:** Yep.

**Brock Walters:** He was working on it last night.

**Brock Walters:** I haven't looked at it yet, but he did this draft last night.

**Ashish Kuthiala:** One and two have been published, Erik?

**Brock Walters:** One and two, yes.

**Ashish Kuthiala:** And I think two is maybe a PR, but they've been published.

**Ashish Kuthiala:** You're welcome to look at them and suggest any changes to have the maximum impact.

**Ashish Kuthiala:** Related to that, Erik, is maybe you have the expertise.

**Ashish Kuthiala:** I never thought about it, but we have a lot of how-to and technical articles on our website.

**Ashish Kuthiala:** And I have been hunting, and I think I've found somebody, but somebody who has some bit of expertise that can bundle some of these existing articles and create standalone assets.

**Ashish Kuthiala:** So what I mean by that is if there's a series of articles that talks about Linux management blogs, can somebody take it and put it together as a white paper or as an e-book?

**Ashish Kuthiala:** Then I can kind of hand it over to John as a downloadable or gated asset that he can use for the website.

**Ashish Kuthiala:** Is that something you also do?

**Erik O'Brien:** We have been exploring.

**Erik O'Brien:** Exploring that, it's been a request from multiple clients recently, like literally coming into the new year.

**Erik O'Brien:** So let me check to see kind of where we're at with being able to ingest those.

**Erik O'Brien:** I don't see why we couldn't.

**Ashish Kuthiala:** I think you could.

**Ashish Kuthiala:** I mean, it's a bandwidth issue.

**Ashish Kuthiala:** You have the expertise.

**Ashish Kuthiala:** I say that because if I had the bandwidth, I could take some of them and use some AI and put together a little e-book, and then I would need somebody to review it.

**Ashish Kuthiala:** I just don't have the bandwidth to do it myself.

**Ashish Kuthiala:** Brock doesn't have it.

**Ashish Kuthiala:** There have been emails in my inbox of vendors proposing that to me, and I've kind of like not entertained them yet.

**Ashish Kuthiala:** So I thought I'll ask you.

**Ashish Kuthiala:** Let me know if you can do that.

**Erik O'Brien:** I will.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** I'll get back to you.

**Ashish Kuthiala:** One small test.

**Ashish Kuthiala:** We'll how that works.

**Ashish Kuthiala:** Because, you know, creating content is hard, but activating that content and distributing is

**Brock Walters:** Yeah, obviously, but only if I'm involved.

**Ashish Kuthiala:** All right.

**Ashish Kuthiala:** You have a few minutes, Erik, 10, 12 minutes, I can talk to you.

**Erik O'Brien:** Yeah, absolutely.

**Ashish Kuthiala:** Awesome.

**Ashish Kuthiala:** All right.

**Ashish Kuthiala:** Thanks, John and Brock.

**Erik O'Brien:** All right.

**Erik O'Brien:** See you, John.

**Erik O'Brien:** See you, Brock.

**John Jeremiah:** I see an end button.

**John Jeremiah:** I am going to press it.

**John Jeremiah:** if I end...

**Ashish Kuthiala:** John, you can stay if you want.

**John Jeremiah:** I'd like to...

**Ashish Kuthiala:** I'll...

**John Jeremiah:** Okay, I'll stay.

**Ashish Kuthiala:** I want the recording to stop, if you can.

**Erik O'Brien:** Are you able to kick that out, John?

**John Jeremiah:** Yeah, I'm gonna remove it.
