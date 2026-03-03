# Director Standup

<metadata>
date: 2025-08-13
time: 19:00 UTC
duration: 32 minutes
organizer: Andi Bailey
participants: Andi Bailey, Darrell Etherington, Jakub Rudnik, Matthew Panzarino, Megan Dickey, Mara Leighton
fathom_recording_id: 80404838
fathom_url: https://fathom.video/calls/378269899
share_url: https://fathom.video/share/sPR8eh7gQDbgJCxYH7s-k3zq9Az1K1ja
source: fathom
enriched_on: 2026-03-03 20:00 UTC
</metadata>

---

## Summary

GrowthX Directors aligned on content production workflows and identified Matthew Panzarino's approach as the operational standard: maintaining 30-40 approved topics with the client, batching article generation through Atlas in 5-8 topic increments, and staying 2-3 weeks ahead of publishing deadlines. The team confirmed that client approvals are not the bottleneck; instead, focus is on standardizing post-processing (custom prompt libraries per client), documenting manual processes so engineering can automate them into Atlas pipelines, and implementing time tracking to understand workflow variations. Andi will begin shadowing pods next week starting with Elvis's team to observe and surface hidden inefficiencies.

---

## Context

This is an internal GrowthX Directors Standup — a regular sync between the company's content delivery directors to align on production processes and efficiency. Andi Bailey, the Delivery Operations lead, ran this meeting to understand how each pod approaches content generation and to identify bottlenecks in workflow. The Directors present manage different client accounts and production teams. The core challenge: GrowthX content pods are producing high volume (10+ pieces per week per team), but processes vary widely, making it hard to optimize overall delivery and understand where time is actually spent.

---

## Relevance

**To GrowthX Delivery:**
- Matthew's approach (30-40 approved topics upfront, batch generation in 5-8 topic increments, 2-3 weeks ahead) is becoming the reference workflow; other pods should adopt similar patterns
- Custom prompt libraries (8-10 per client) are now standard for post-processing; documenting these is critical for knowledge transfer and engineering pipeline building
- Metronome and Monograph require outline approvals before article generation — these are exceptions that need specific client conversations about workflow
- Atlas pipelines currently don't include all post-processing steps; prototyping in Claude, then ticketing to engineering, is the documented workflow

**To GrowthX Business Development:**
- Client approval processes vary significantly; Metronome's outline review is a known friction point that may impact project velocity going forward
- Pod shadowing (starting with Elvis's team) will uncover hidden inefficiencies and model improvements across teams
- Biologica's ingredient integration workflow is successful and portable to other accounts — document as a repeatable pattern

**To CheckThat / AI Visibility:**
- Multiple pods are using Claude directly for content generation because Atlas output quality is inconsistent — signals opportunity for AEO model improvement or better prompting
- Custom prompt libraries that drive good content outcomes should be studied to understand effective content patterns and frameworks

---

## Overview

- Pods vary in their content generation approaches, with some using custom prompt libraries and others relying more on manual editing
- Getting approved content from clients is generally not a bottleneck; the focus is on streamlining internal processes
- Time tracking will be implemented to better understand variations in workflow and identify areas for improvement
- There's a push to standardize and automate processes that are currently manual, with the goal of building them into Atlas pipelines

---

## Key Topics

### Content Approval and Topic Generation

  - Most pods have ample approved topics from clients
  - Some clients (e.g., Metronome) require outline approval, which can slow the process
  - Standard practice is to have 30-40 approved topics ready for content generation

### Content Generation Workflow

  - Typical workflow: Run 5-8 topics through Atlas for article generation
  - Output is exported to Google Docs in internal folders organized by week
  - Post-processing involves using custom prompt libraries in Claude or manual editing
  - Some pods are using Claude directly for generation, bypassing Atlas for quality reasons

### Post-Processing and Quality Control

  - Panzer's pod uses a custom prompt library (8-10 prompts) for each client to refine content
  - Other pods may use notes or guidelines but don't have formalized prompt libraries
  - Directors personally review all content before client delivery
  - Some pods integrate client call notes and feedback into artifacts for improved content alignment

### Efficiency Improvements and Standardization

  - Goal is to prototype processes manually, then have engineering build them into Atlas pipelines
  - Custom workflows (e.g., ingredient integration for Biologica) are being developed and standardized
  - There's a push to document and ticket custom processes for engineering implementation

### Time Management and Tracking

  - Time tracking will be implemented, starting with spreadsheets and potentially moving to more detailed systems
  - Some pods already have informal time tracking via Slack timestamps

---

## Action Items

**Andi Bailey (GrowthX)**
- Schedule and conduct shadowing session with Elvis's pod next week
- Set up initial time tracking system (Excel/Google Doc) for all team members

**Matthew Panzarino (GrowthX)**
- Document all prompt libraries and file tickets for workflow building
- Ask Nana to investigate scraping Slack timestamps for time tracking

---

## Transcript
**Andi Bailey:** Hello?

**Megan:** Hello.

**Darrell Etherington:** Hello.

**Andi Bailey:** Hello.

**Andi Bailey:** How's it going?

**Darrell Etherington:** It's been a client day.

**Andi Bailey:** Hmm.

**Andi Bailey:** Town is still...

**Darrell Etherington:** Shant and E messaged me separately, but he's blaming Edasham, but it's not Edasham's fault, because that is the fix that we should have made.

**Darrell Etherington:** He just likes rules.

**Darrell Etherington:** What's that?

**Darrell Etherington:** The other person put it in her hands.

**Darrell Etherington:** Because it was the right fix.

**Darrell Etherington:** It's the right fix.

**Darrell Etherington:** But Jean-Denis, I told Edasham this, I was like...

**Darrell Etherington:** You just have to understand that he is extremely rules and system-based, and so nothing can deviate from the established rules and systems without explicit direction.

**Darrell Etherington:** That's just the way he works.

**Darrell Etherington:** It doesn't matter if you have a good fix and you're just going to implement it.

**Darrell Etherington:** He doesn't want that an issue.

**Darrell Etherington:** He wants things to follow exactly the pattern we laid out.

**Darrell Etherington:** But I got dot, dot, dot on him right now because he texted and he DMed me separately and was like, I don't like Eda Shum.

**Andi Bailey:** Eda was better.

**Andi Bailey:** And I'm like, okay.

**Andi Bailey:** Oh, boy.

**Darrell Etherington:** Yeah.

**Andi Bailey:** Who is this, Daryl?

**Andi Bailey:** news?

**Darrell Etherington:** Jean Denis from town.

**Darrell Etherington:** He's a very smart guy.

**Darrell Etherington:** He's just extremely rules and system-oriented.

**Andi Bailey:** Yeah, we don't have anybody better than Eda Shum.

**Darrell Etherington:** No, I know.

**Darrell Etherington:** I was like, oh, I mean, I said, look, I think there are some specific tactical things that we'll work on.

**Darrell Etherington:** But, you know, he's actually very competent on other broader things, like project management.

**Darrell Etherington:** This isn't the thing that he usually spends time on.

**Darrell Etherington:** So that was the excuse.

**Darrell Etherington:** But like, I was like, we'll work on it.

**Darrell Etherington:** And if there is no improvement over the next couple of weeks, let me know.

**Andi Bailey:** But yeah, so is he like, should we put him with somebody who's like, super editorially focused then?

**Darrell Etherington:** Like, no, no, you should put him with someone who is like, just good at following very explicit directions and has no creative thought or agency whatsoever.

**Darrell Etherington:** So I don't know who that would be.

**Andi Bailey:** I don't either.

**Darrell Etherington:** Yeah.

**Andi Bailey:** All right.

**Andi Bailey:** Mara, I'm happy to have you here.

**Mara Leighton:** Me too.

**Andi Bailey:** This is usually.

**Andi Bailey:** Your conflict day, right?

**Mara Leighton:** Or is Thursday your conflict day?

**Mara Leighton:** Unfortunately, that's tomorrow.

**Mara Leighton:** Yeah.

**Andi Bailey:** Except this week.

**Mara Leighton:** Same.

**Mara Leighton:** What a week.

**Mara Leighton:** I have DataGrid at the same time tomorrow.

**Mara Leighton:** But, yeah.

**Andi Bailey:** God bless you, Jacob.

**Andi Bailey:** Your sneeze attack.

**Andi Bailey:** Like dying over here out of nowhere.

**Jakub Rudnik:** Sorry.

**Andi Bailey:** Okay.

**Andi Bailey:** Today, I have a really, we're going to do a really annoying exercise.

**Andi Bailey:** And so, just sorry ahead of time.

**Andi Bailey:** But, just so everybody, like, understands the context before we jump in.

**Andi Bailey:** Um, I, we all know I've been, like, trying to get efficiency, gain, like, efficiency in different places for, like, I, we're to really, really.

**Andi Bailey:** Thank you. Where we're bottlenecking in the process and trying to like fix things holistically.

**Andi Bailey:** We didn't get a lot of responses in the survey that I sent out and they were very unhelpful.

**Andi Bailey:** So I'm going to start shadowing pods and I'm going to start with Elvis's pod next week.

**Andi Bailey:** I think we're going to try and experiment with Jessalyn and Rachel.

**Andi Bailey:** I have to set up that time, but to try and get them ahead of publishing like Panzer has been able to do.

**Andi Bailey:** And I think Daryl's done with some of his accounts.

**Andi Bailey:** But in order to like really understand where like what we experiment with changing, I want to talk about like Monday to Friday, how are your teams, like what are your teams doing to get to 10 pieces of content?

**Andi Bailey:** And on a Friday, you know, or whatever number of pieces of content on a Friday.

**Andi Bailey:** And like, I want to really break it down step by step.

**Andi Bailey:** And also, like, I have a feeling it looks different with every team.

**Andi Bailey:** And so I also want to hear about that.

**Andi Bailey:** And like, if we can do that in 30 minutes here, then we don't have to do, I don't have to do as much like 30 minutes with every person.

**Andi Bailey:** So I would like to try and get that done.

**Andi Bailey:** But let's start with Panzer.

**Andi Bailey:** I'm going to throw it to you very quickly and say, okay, next Monday, you want to get ahead.

**Andi Bailey:** What's the first thing you're doing?

**Andi Bailey:** And like, I don't want to go all the way down the flow.

**Andi Bailey:** I just want to say, like, what's the first thing you're doing if you're thinking about getting ahead of publishing?

**Andi Bailey:** And then I want to hear how we're like varying within pods.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** I mean, guess there's, so like, Metrodome this week, I'm going to, I have to actually have this conversation with them tomorrow, which is basically like, if you want us to deliver these things, as many deliverables as you want, you know, and at the speed that you want, I need you to approve a bunch more outlines, and then one batch per week.

**Matthew Panzarino:** So, I think that's table stakes.

**Matthew Panzarino:** For other clients, it's a little different, because, because their version of that is just approved content for us to go after.

**Matthew Panzarino:** So, in the case of Metronome, they require us to give them outlines, which they then review.

**Matthew Panzarino:** And so, for them, it's going be, hey, I'm going to give you a month's worth of outlines, and I'd like you to do a focus session, and do as many of these as you can, because we need to get ahead of your deliverables to make sure that we can get you the best quality of the training,

**Matthew Panzarino:** Make any tactical adjustments.

**Matthew Panzarino:** is my positioning to them.

**Matthew Panzarino:** any tactical adjustments that we need to make.

**Matthew Panzarino:** And we just have a buffer so that if you have additional rounds of feedback or anything like that, we have some wiggle room.

**Matthew Panzarino:** I don't want to be handing publishing stuff to our publisher at 5 p.m.

**Andi Bailey:** on our Friday.

**Andi Bailey:** So if we're giving them, like, bulk outline approval, are you generating all of those outlines on Monday?

**Andi Bailey:** Like, how far in advance?

**Andi Bailey:** Like, what are you doing to get to that far ahead?

**Andi Bailey:** And then what else is ready to go?

**Matthew Panzarino:** Yeah, I think on a, so we're not ahead of metronome, right?

**Andi Bailey:** We're on pace for metronome.

**Matthew Panzarino:** So if you want me to talk about what we're doing now with other clients, we're on every Monday.

**Matthew Panzarino:** So what I did is I sprinted our pod one week to get two weeks ahead.

**Matthew Panzarino:** And then every week we do an additional one to one and a half weeks.

**Matthew Panzarino:** So now we're two to three weeks ahead.

**Andi Bailey:** Okay.

**Andi Bailey:** And what's your order of operations?

**Andi Bailey:** And I'm going to, like, interrupt you a lot to ask questions.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** So check the content OS to make sure that we have content either approved or rated for ranking.

**Matthew Panzarino:** So, for instance, Monograph, they like to rank high priority, low priority, medium priority, what they want to go after because they're targeting certain clusters of content.

**Matthew Panzarino:** So first step is to make sure that the client, I communicate with the client and say, hey, we're going to start sprinting to do a little work on this content.

**Matthew Panzarino:** Make sure you have three weeks worth, basically, like, 30 or 40 rated in here for us or approved to start.

**Matthew Panzarino:** So step one, get the client 30 to 40 pieces ahead, approved to start.

**Andi Bailey:** Okay.

**Andi Bailey:** And for other pods, how much, how many approved topics do

**Andi Bailey:** We have at any given point in time.

**Darrell Etherington:** For most of mine, tons, except for like a bit where they're like, oh, we just want to move super, super slow.

**Darrell Etherington:** They won't even improve their outlines and batches greater than like two or three weeks, and they don't approve most of them.

**Darrell Etherington:** I mean, you were on that call earlier, Andy.

**Darrell Etherington:** So I thought we would get alignment by switching to thought leadership, but a part of it doesn't think we can do thought leadership.

**Andi Bailey:** Yeah, that was weird.

**Andi Bailey:** I feel like we are, we're getting, yeah, that was a separate conversation, but I think we're on the same page on where we are with them now.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** But with the other ones, we have tons of approved topics, and similarly, we're doing this right now with Tanon, although John is still typing, so I do not like where this message is going.

**Darrell Etherington:** But we are getting ahead to build a buffer, We're sprinting this week to get ahead with them.

**Andi Bailey:** In terms of approved content?

**Andi Bailey:** Yeah, in terms of locked and loaded, like delivered, not even outlined.

**Andi Bailey:** So when you say you're starting to get ahead, are you just doing more of each one?

**Darrell Etherington:** Yeah, we're just going through the approved topics and then generating more articles because we have a huge backlog of approved topics.

**Andi Bailey:** This week you'll generate 20, but are you doing each stage in bulk?

**Andi Bailey:** I think that's a question that I have.

**Andi Bailey:** Like, are you doing 20 approved topics and then you do 20 outlines and then you do 20?

**Darrell Etherington:** Are you doing that?

**Darrell Etherington:** Well, most of the clients don't require the outlines.

**Darrell Etherington:** And I think this is unique maybe to the two that me and Matthew were referring to.

**Darrell Etherington:** Maybe there's one or two others that had that.

**Darrell Etherington:** Aftershoot had that for a while, but they've now given up on that and are very happy doing it with our bulk production.

**Darrell Etherington:** But yeah, those are the other ones that have the outline thing.

**Darrell Etherington:** On the topic thing, like we bring them up earlier.

**Darrell Etherington:** Just meeting to meeting, Edith Shum and Carrie will bring like new topic clusters if we're running low on the previous ones.

**Darrell Etherington:** But most of the other clients also don't have much to say or debate or go back and forth on when it comes to those.

**Darrell Etherington:** They're kind of like, ah, I would order this one above this one.

**Darrell Etherington:** But like, I agree.

**Darrell Etherington:** And they really don't even look at the subtopics under the cluster.

**Darrell Etherington:** They just kind of speak to the cluster.

**Darrell Etherington:** And then they kind of trust our guidance to the topics within the cluster.

**Andi Bailey:** Okay.

**Andi Bailey:** Um, so the, it seems like getting approved content and getting ahead on approved content is not the problem.

**Matthew Panzarino:** So then.

**Matthew Panzarino:** Yeah, I don't think it is for most people.

**Matthew Panzarino:** I think we're in a kind of unique case with Metrum.

**Matthew Panzarino:** Yeah.

**Andi Bailey:** And monograph is only because.

**Matthew Panzarino:** So let's do like the standard one.

**Andi Bailey:** Let's go standard.

**Andi Bailey:** Like not, not the, let's not talk about the, uh, outliers right now.

**Andi Bailey:** So.

**Andi Bailey:** So like, yeah.

**Matthew Panzarino:** We, so as an example, when we started sprinting with monographies.

**Matthew Panzarino:** Excuse me, in biologic, we have plenty of runway in approved topics already.

**Matthew Panzarino:** So we're establishing that.

**Matthew Panzarino:** Now we need a new beachhead because we are three weeks ahead.

**Matthew Panzarino:** Right.

**Matthew Panzarino:** So I need to get more.

**Matthew Panzarino:** But once you have the room, it is grab the topics and run.

**Matthew Panzarino:** We usually do them in batches of like eight or so, you know, five to eight at a time.

**Matthew Panzarino:** And you just run all the pipelines.

**Matthew Panzarino:** So run them through Atlas, five to eight at a time.

**Andi Bailey:** Get them all.

**Andi Bailey:** And that's the article, in the article brief workflow?

**Matthew Panzarino:** Article, just no, it's article generation.

**Andi Bailey:** Nothing special.

**Andi Bailey:** Oh, so we don't do a brief workflow first for most clients.

**Andi Bailey:** Okay.

**Matthew Panzarino:** Yeah, I don't even know what the brief is for anymore.

**Matthew Panzarino:** It used to be for generating assignments.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** It doesn't really do anything in their current flow the way most people work, I don't think.

**Andi Bailey:** Anybody using the article brief workflow?

**Andi Bailey:** Because it's in almost every workspace.

**Matthew Panzarino:** You're talking about like the one that's like a separate one that's just a stub that generates a brief?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah, no, I don't think anybody uses that anymore.

**Matthew Panzarino:** That was for bulk generating briefs at a different stage in our evolution.

**Matthew Panzarino:** It was basically, that's a vestige of air ops.

**Andi Bailey:** Okay, and so would you use the brief?

**Andi Bailey:** So we're not using outlines at all in any stage unless the client is requiring it, is what you're saying.

**Matthew Panzarino:** Yeah, for Metronome, as an example, we are pasting the outlines in article direction before we generate the articles.

**Matthew Panzarino:** And are you coming up with the outlines then?

**Matthew Panzarino:** We generate the outlines outside of Atlas.

**Matthew Panzarino:** There's a generation, so this is one of the things that I'm having to deal with, with these clients coming out of Sprint.

**Matthew Panzarino:** The process is usually just...

**Matthew Panzarino:** It's like, oh, do these 500 steps.

**Matthew Panzarino:** And so I'm like, all right, we're not going to be doing that, right?

**Matthew Panzarino:** Like, that's fine.

**Matthew Panzarino:** I'm glad you did that.

**Matthew Panzarino:** And I'm sorry that that happened to you.

**Matthew Panzarino:** But now we're going to take that and make this a pipeline.

**Matthew Panzarino:** So like this week, in and amongst trying to get everybody ahead and delivered.

**Andi Bailey:** Is this what you're talking about?

**Matthew Panzarino:** No.

**Matthew Panzarino:** No.

**Matthew Panzarino:** There's a separate, go to outlines maybe.

**Matthew Panzarino:** Yeah, there you go.

**Matthew Panzarino:** Outlines.

**Matthew Panzarino:** No, don't.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** So generating outlines for Metrodome.

**Matthew Panzarino:** Do you do this stuff, right?

**Matthew Panzarino:** Like this is the, now this is actually not, I don't actually think this is that involved.

**Matthew Panzarino:** But the generating outlines for some of the other clients can be a little bit hairy.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** This is not, it's not that bad.

**Matthew Panzarino:** It's just basically this like, put this idea in a clog with a prompt, basically.

**Matthew Panzarino:** And it creates outlines.

**Matthew Panzarino:** But just to give you an idea.

**Matthew Panzarino:** But

**Matthew Panzarino:** I actually don't even like this, personally, and I'm going to kind of wean them off of it, because I want to create a pipeline, first of all, that creates the outlines in Atlas, right?

**Matthew Panzarino:** Like, I want to be able to run a hundred of them, right?

**Matthew Panzarino:** And I don't want to go in, Claude, and do all this stuff.

**Matthew Panzarino:** It's actually a waste of time.

**Matthew Panzarino:** The second thing is, though, when I asked Sydney, wait, how'd you come up with this?

**Matthew Panzarino:** And this is just, I'm sorry, I'm not a marketer.

**Matthew Panzarino:** I always forget what it is.

**Matthew Panzarino:** What is it?

**Matthew Panzarino:** Grunt?

**Matthew Panzarino:** Chome?

**Matthew Panzarino:** Flood?

**Matthew Panzarino:** Crop?

**Matthew Panzarino:** It's some acronym.

**Matthew Panzarino:** What is the acronym for, like, crud?

**Matthew Panzarino:** don't know.

**Matthew Panzarino:** What?

**Matthew Panzarino:** Crap?

**Matthew Panzarino:** What is the acronym?

**Andi Bailey:** I don't know.

**Matthew Panzarino:** Is it There's some acronym for creating, I don't know, all marketers seem to know this, and I'm like, what is it?

**Matthew Panzarino:** I'm going ask you at TPT.

**Matthew Panzarino:** Acronym for creating content outlines.

**Matthew Panzarino:** Marketer?

**Matthew Panzarino:** Something like crud?

**Matthew Panzarino:** I think it's something like CRUD, I swear to God, I'm not joking.

**Matthew Panzarino:** you don't like this.

**Matthew Panzarino:** crazy?

**Matthew Panzarino:** Anyhow, it's basically just like a, yeah, it's CRUD.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** It's create, read, update, delete, or something like that.

**Matthew Panzarino:** I don't know, crop, dash, I don't know, you don't have to ask Sydney.

**Matthew Panzarino:** Anyhow, let's be short, it's some sort of basic content framework that everybody's like, who, but, where, where, right, for content marketers that they basically use to create outlines.

**Matthew Panzarino:** It's some sort of acronym that they, that she said to me, and I was like, oh, yeah, sure.

**Matthew Panzarino:** I was like, I have no idea what she's talking about.

**Matthew Panzarino:** But I see what she means when I look at it, right?

**Matthew Panzarino:** It's like, okay, cool.

**Matthew Panzarino:** It's like, basic body, copy, H3s, all that.

**Matthew Panzarino:** And she just uses that basic content framework.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** And throws it at the bottom with a rough prompt, and then asks to create outlines.

**Matthew Panzarino:** Then she shifts those outlines to them.

**Matthew Panzarino:** Remarkably, I guess they seem to be, like, fine with that, and that's cool.

**Andi Bailey:** So I'm going to just start there.

**Andi Bailey:** Yeah, for general.

**Andi Bailey:** Generally, you're generating a different kind of outline, I don't, like, we don't need to see it right now, but, like, you're generating a different outline in Claude, right?

**Andi Bailey:** Yeah, basically.

**Andi Bailey:** Okay, so, so before we run the topics, we're generating an outline in Claude, and do you have a standard?

**Matthew Panzarino:** Actually, no, I just want to let you know, I don't generate outlines.

**Matthew Panzarino:** Oh!

**Matthew Panzarino:** The only time I do is, is when they request it.

**Andi Bailey:** Every other time, I let the pipeline generate the outline.

**Matthew Panzarino:** So just put a topic in, and then it goes?

**Matthew Panzarino:** That is correct, yes.

**Andi Bailey:** Okay, and then what happens?

**Matthew Panzarino:** Uh, the pipeline runs, and produces content of variable quality.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** And then we run it from there, we take a batch of five, and, or five to eight, whatever, and they are exfilled to Google Docs, as if they were about to be presented to the client, but obviously they're not yet.

**Matthew Panzarino:** And we put those in an internal drive folder.

**Matthew Panzarino:** So for every client, have an internal space and an external space.

**Matthew Panzarino:** We dump those into an internal space by week.

**Matthew Panzarino:** So week of whatever, week of August 12th or week 8 or whatever, however you're doing.

**Matthew Panzarino:** Then those little docs will be in there.

**Matthew Panzarino:** Then we run our post-processing on those.

**Matthew Panzarino:** Okay, talk me through that.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah, have a prompt library for each client, which basically contains anything that is not yet built into the pipeline.

**Matthew Panzarino:** This is the way I look at it.

**Matthew Panzarino:** We're prototyping a process that we then get Eng to build, and then we put that in the pipeline.

**Matthew Panzarino:** So for an example, for Biologica, we need to integrate those ingredients.

**Matthew Panzarino:** So we have the ingredient doc as a piece of context in Claude.

**Matthew Panzarino:** So obviously, whatever other artifacts you need that are non-standard, and then we run the prompt library.

**Andi Bailey:** On that step-by-step.

**Andi Bailey:** Okay.

**Andi Bailey:** So you have like four or five prompts that you're like, do this, now do this.

**Matthew Panzarino:** exactly.

**Matthew Panzarino:** I think it's like eight or something on average.

**Andi Bailey:** Yeah.

**Andi Bailey:** Okay.

**Andi Bailey:** And then you're editing it.

**Matthew Panzarino:** Then from there, we'll end up with reviewed pieces.

**Matthew Panzarino:** We call those, you know, or updated pieces.

**Matthew Panzarino:** And then those updated pieces, I then review.

**Matthew Panzarino:** So I review every piece that goes out to the clients personally.

**Andi Bailey:** Okay.

**Andi Bailey:** And you're doing, are you doing batches of five?

**Andi Bailey:** So five through the generation workflow, five through the prompt library, five through the review, and then going back and doing, so you're doing five at a time rather than 20 through the prompt library, through the generation, 20 through the prompt library, 20 through.

**Andi Bailey:** Yep.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Honestly, I don't know if that'll change, right?

**Matthew Panzarino:** But the reason for that primarily has been the first week, we just needed to get that week's stuff done.

**Matthew Panzarino:** So we need get that week's stuff for everybody.

**Matthew Panzarino:** Then the next week...

**Matthew Panzarino:** I'm like, cool, I think we can do all of the generation for this week on a Monday.

**Andi Bailey:** And we did.

**Matthew Panzarino:** And I'm Friday, let's just generate next week's.

**Matthew Panzarino:** We did.

**Matthew Panzarino:** Then the next week, I'm like, let's do another week on Monday.

**Andi Bailey:** So now we're three weeks ahead.

**Andi Bailey:** Yeah.

**Andi Bailey:** So how long did it take you to put together the prompt library for each client?

**Matthew Panzarino:** Probably three, four hours of manually messing with the article, like one article to start.

**Matthew Panzarino:** Like, generate one.

**Matthew Panzarino:** Let's mess around with it.

**Matthew Panzarino:** Where do we need to get it from?

**Matthew Panzarino:** Pipeline output to actual ready for client review.

**Matthew Panzarino:** so I would say two to three hours or so of like going back and forth.

**Matthew Panzarino:** And we were working in parallel.

**Matthew Panzarino:** So we were all kind of like messing.

**Matthew Panzarino:** I did most of it initially because I wanted to kind of get real hands on with it to understand what the delta was in quality.

**Matthew Panzarino:** And then as I was doing it, I basically was just collating all of the stuff that I did and then refining those prompts semantically in a way where I felt like they were repeatable.

**Matthew Panzarino:** Like,

**Matthew Panzarino:** It would give me very similar results each time if I ran them on new articles.

**Matthew Panzarino:** So the first batch of five, I basically did start to finish.

**Matthew Panzarino:** The only thing that Nana or Yana were doing for me is just running them through the pipeline and putting them into Google Docs.

**Matthew Panzarino:** And then I did everything else there manually.

**Matthew Panzarino:** I either edited them completely manually or prompted, did the prompt library stuff.

**Matthew Panzarino:** I view that as my sprint process of like getting another client in the pipeline and understanding what the delta is, what's missing, matching it to expectations, learning what the client's expectations are.

**Matthew Panzarino:** I did pattern matching with older articles that they were happy with that had already been published.

**Matthew Panzarino:** So I was looking at those articles and looking at the articles I was working with and making sure that we were matching well.

**Matthew Panzarino:** And then there was a handful of things that needed to be done.

**Matthew Panzarino:** For monograph example, as an example, I took three articles where the CTAs were really well done.

**Matthew Panzarino:** And then I gave those to Claude's context and I said, this is what I want the CTAs to look like.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** And then built a prompt to integrate those, et cetera.

**Matthew Panzarino:** Okay, so now we're just going to have a library.

**Andi Bailey:** My sense is nobody else has a prompt library.

**Andi Bailey:** Please raise your hand if you have a prompt library.

**Darrell Etherington:** I have a notes thing that I use for cloud generation just in sequence.

**Andi Bailey:** Like just one page in notes.

**Matthew Panzarino:** I guess it's the same thing.

**Matthew Panzarino:** Yeah, I'm saying the word prompt library.

**Andi Bailey:** Yeah, but I mean like...

**Andi Bailey:** It's basically just notes, but it's in I know we have like brand guidelines or like preferences that clients like, but I don't know if we have like a list of prompts that we're applying to every client.

**Andi Bailey:** Like for each client, have a list of prompts that we're asking post-processing.

**Matthew Panzarino:** I think everybody's...

**Matthew Panzarino:** They should absolutely have.

**Andi Bailey:** Yeah, but it's my gut that everybody's just going in post-article generation and editing and not doing a lot of run it through cloud again and again.

**Andi Bailey:** But tell me if that's wrong.

**Megan:** Yeah.

**Megan:** Yeah.

**Megan:** Yeah.

**Megan:** I have instructed my CMs to do that with Claude, and so basically I've created Claude projects with essentially like all the artifacts with like specific instructions that it needs to take into account when editing the article.

**Megan:** But I'm not sure if they're actually using it, so I think that's the next step, but it is there for them.

**Megan:** Because that's just like, that's just my own process when I've had to generate articles like I've gone through Atlas, but then I'm also running it again through Pod essentially being like, are you sure that, are you sure you've actually followed all these instructions, like make sure you're looking for this.

**Megan:** And I've also imported like all of the Fathom calls into the project so that it's also taking into account feedback that we've received on those calls just to make sure that we're not, we're not missing anything.

**Matthew Panzarino:** Are you scraping Fathom calls and integrating them into artifacts, by the way?

**Megan:** In general, yeah.

**Darrell Etherington:** Yeah.

**Darrell Etherington:** Hmm.

**Matthew Panzarino:** Hmm.

**Matthew Panzarino:** Yeah, we do that on a weekly basis.

**Matthew Panzarino:** take client calls, any updates that they've given us, all comments that are scraped, and then those all get integrated into the artifacts that live.

**Matthew Panzarino:** We put them in Notion, Atlas, and Club Projects.

**Andi Bailey:** Okay.

**Andi Bailey:** And so let's talk, like, other pods.

**Andi Bailey:** Where does your pods process differ, aside from, like, the post-processing?

**Andi Bailey:** Like, you know, what are the variations that we see in this, like, content development process?

**Darrell Etherington:** So I think, I mean, there's some custom pipelines we're using that are in Atlas, but a lot of the generation, especially the generation that I'm doing, is happening just in Cloud, because eventually it gets too frustrating to try to use it in Atlas, because it was, like, even when...

**Darrell Etherington:** Atlas was doing a good job.

**Darrell Etherington:** If I looked at them side by side, I'm like, well, Claude's much better.

**Darrell Etherington:** So I'm going to use that one.

**Darrell Etherington:** This is my town one.

**Darrell Etherington:** And I'll place it as like, I guess, plain text or code or something so that it doesn't expand.

**Darrell Etherington:** But it's very simple.

**Darrell Etherington:** And then I just like run that over and over again.

**Darrell Etherington:** I changed the article topic.

**Darrell Etherington:** Each paragraph break represents like a new prompt because otherwise I find it doesn't follow those instructions very closely.

**Darrell Etherington:** Can you drop it?

**Darrell Etherington:** In the Ddirector's channel in Slack.

**Darrell Etherington:** But that's basically like I realized I was just doing this repetitively.

**Darrell Etherington:** So I put them in a thing and then pasted it.

**Darrell Etherington:** So like in theory, there's no reason you couldn't build that into a pipeline because all you have to do is call Claude Sonnet, which is what I'm using, and then do that with the project artifacts as reference.

**Darrell Etherington:** Documents, as long as it can access those agentically, whatever sequence it wants.

**Darrell Etherington:** But that produces stuff where, for everything else John Denis doesn't like about us, he does like the content, so they're very happy with that side of things, right?

**Andi Bailey:** Yeah.

**Andi Bailey:** I'm very afraid, please don't, everybody don't take this to your pods, unless you're, I mean, if you're panicking in a week, and we're very far behind, do this.

**Andi Bailey:** But I would say, let's not make this the standard practice, because it'll be really hard to unwind it.

**Darrell Etherington:** Yeah.

**Matthew Panzarino:** I do that for engine, too.

**Andi Bailey:** Yeah.

**Andi Bailey:** I mean, you're getting it done, right?

**Andi Bailey:** Yeah, exactly.

**Matthew Panzarino:** That was my only concern, any of us, the cloud stuff, is like, there are people that get that it's a stopgap, and get the articulation aspect, and there are people that don't.

**Matthew Panzarino:** Because, like, the fact is, it's like, okay, we went and created this prompt library, and are doing this post-processing in quad,

**Matthew Panzarino:** But the aim of that is not just generate a processing cloud that exists in perpetuity, it is create something that's repeatable here that we can then articulate.

**Matthew Panzarino:** I literally just give that chat to Pedro and say, hey, here's the spec for the product that I want you to build as a workflow that would go into my logic, right, or into this other one.

**Matthew Panzarino:** And that's going to exist for all of our clients.

**Matthew Panzarino:** So, like, this week for me is about documenting all of those and making sure a ticket is filed for it.

**Matthew Panzarino:** basically trying to wean ourselves off of that cloud process by building the things that need to exist.

**Matthew Panzarino:** This is where the knowledge-based thing came from and the ingredient thing, like, in biologica, and it's already paying forward into other accounts.

**Matthew Panzarino:** These things need to exist, but they will never get a note if people don't know we need them.

**Andi Bailey:** Yeah.

**Andi Bailey:** Okay.

**Andi Bailey:** Yeah.

**Andi Bailey:** Does anybody, like, just, I know we have two minutes left, so...

**Andi Bailey:** Off the top of...

**Andi Bailey:** Their head, where do we think, are we just losing time in editing in these processes, or where else are people feeling like this is a huge deviation from what their teams are doing, and, like, let's call out anything that's different from this process?

**Andi Bailey:** Or is it just an editing?

**Megan:** I mean, I think it's all about, right?

**Megan:** Like, I think just, yeah, what I've been seeing in my pod is just, yeah, just not a lot of speed around generating the actual content.

**Megan:** Not with every client, but with some, and so then other folks having to step in to generate that content.

**Megan:** And, but I think that's also partly because of some of the scope creep that's happening with the superhuman and Smith.

**Megan:** So it's just kind of...

**Megan:** So, exacerbating some issues.

**Andi Bailey:** Okay.

**Andi Bailey:** Yeah.

**Andi Bailey:** Well, I guess that will just, that's a problem we're going to have to solve case by case and just shadowing.

**Andi Bailey:** In the last minute, I will let you guys know that we're going to start doing some sort of time tracking, which I'm sure everybody's going to be super thrilled about.

**Andi Bailey:** We'll probably start in like an Excel spreadsheet or Google Doc, like how much time did you spend on each client?

**Andi Bailey:** And we've got dropdowns, but it's still going to be annoying and it's still going to take a lot of time.

**Andi Bailey:** If we, we may move to like a time doctor or some sort of like more detailed tracking, which, you know, I don't think anybody's going to be thrilled about, but we just need to really understand where the variation is here.

**Andi Bailey:** So we're going to be pushing on a couple of fronts and I just want to give you guys.

**Matthew Panzarino:** you.

**Matthew Panzarino:** A little heads up on that piece.

**Matthew Panzarino:** Yeah, I have some timestamps.

**Matthew Panzarino:** I can have Nana scrape those because we, basically we work in, my pod works in one single Slack.

**Matthew Panzarino:** So the internal channels are really used for like documenting really specific processes related to those clients or documents.

**Matthew Panzarino:** But we have a pod panzer channel that we do everything together in there, all three of us, or two of us, but now three of us.

**Matthew Panzarino:** And so everything is timestamped.

**Matthew Panzarino:** So I can have Nana maybe look at a way to scrape that for like, okay, I'm jumping into this now.

**Matthew Panzarino:** I'm going to edit these articles now.

**Matthew Panzarino:** And then, okay, I'm done.

**Matthew Panzarino:** You can take over, you know, that kind of thing.

**Matthew Panzarino:** Because they'll tell me, they're like, okay, I generated these.

**Matthew Panzarino:** You can look at them now and be like, cool.

**Matthew Panzarino:** I'll look at them in a minute.

**Matthew Panzarino:** And then I'll be like, okay, jumping in now.

**Matthew Panzarino:** I'll see if I have any of that movie that could be a seed or something for you.

**Matthew Panzarino:** But if not, I can actually just, we can start doing that.

**Matthew Panzarino:** We can start timestamping ourselves so that we can get an idea of how long it's taking us.

**Andi Bailey:** Okay.

**Matthew Panzarino:** Yeah, that think you're going to go with stuff, you know, that I think it does.

**Andi Bailey:** All right.

**Andi Bailey:** Anything else anybody wants to talk about?

**Andi Bailey:** All right.

**Andi Bailey:** Thanks, guys.

**Andi Bailey:** Thank you.
