# Atlas Workflow & Pipeline Review - Saskia 

<metadata>
date: 2025-06-17
time: 16:39 UTC
duration: 40 minutes
organizer: saskia@growthx.ai
participants: Matthew Panzarino, Ehtisham Hussain, Saskia Wartnaby
fathom_recording_id: 68892274
fathom_url: https://fathom.video/calls/328424190
share_url: https://fathom.video/share/QFarjGtvuBtd3-GZ5xhab2W6p3_nZnMU
source: fathom
enriched_on: 2026-03-03 14:22 UTC
</metadata>

---

## Summary

Review Atlas workflow and pipeline for new CM Saskia, addressing challenges with output quality and efficiency.

---

## Context

This was an onboarding call between Matthew Panzarino (GrowthX Atlas product owner and workflow architect) and Saskia Wartnaby (newly promoted Content Manager), with Ehtisham Hussain (Strategic Operations) observing. Saskia had recently moved from the Unstructured client to Prophecy and was struggling to understand the Atlas workflow pipeline — specifically how inputs at each stage influence outputs, and why her writing guidelines weren't being applied early enough. Matthew walked her through the Atlas workflow architecture, explaining how the assignment stage, brief, outline, and final draft each consume different inputs and why upfront work on context, personas, and writing guidelines is critical for quality control. The call established shared understanding of Atlas as a tool that requires strategic inputs at multiple stages, not a black box that can be controlled via writing guidelines alone.

---

## Relevance

**To GrowthX Delivery:**
- Atlas workflow requires strategic input at assignment, brief, and outline stages to control output quality and length — not at the draft stage where writing guidelines apply
- Brief and outline editing are the critical control points; bulk of editing work should happen there, not in final polish
- Custom pipelines can target specific content types (technical vs. top-funnel) with separate personas, guidelines, and source restrictions
- New LLM-powered editor feature (launching this week) will enable in-line fact-checking and targeted revisions, reducing manual editing time

**To GrowthX Business Development:**
- Prophecy client using external tools (Claude/ChatGPT) outside Atlas suggests workflow or training gap — opportunity to establish Atlas as the standard and build stronger partnership
- Account health risk: Prophecy flagged as data-scientist audience requesting highly technical content that's difficult to verify; funnel strategy with broader topics first can build authority and early wins before tackling deep technical pieces

**To Content Strategy & Client Management:**
- GrowthX should establish content strategy expert positioning early in client relationships, not take orders reactively
- Funnel approach (broad → technical) is key for both SEO authority and managing client expectations and scope creep
- CMs have voice in strategy conversations and can push back diplomatically on misaligned requests (e.g., requesting only deep technical content without foundational pieces)

---

## Overview

- Atlas workflow requires strategic input at each stage (assignment, brief, outline) to control output quality and length
- Writing guidelines should focus on high-level structural guidance, with specific edits done later
- Custom pipelines can be created for different content types (e.g. technical vs. top-funnel)
- Importance of establishing GrowthX as content strategy experts with clients, balancing their requests with best practices

---

## Key Topics

### Atlas Workflow Overview

  - Assignment directions: Key for influencing initial output; use detailed prompts, not just keywords
  - Brief: Opportunity to remove unnecessary sections and control article length
  - Outline: Critical stage for structural edits before full draft
  - Writing guidelines: Focus on high-level instructions (tone, structure) rather than specific formatting
  - New feature coming: LLM-powered editor for targeted revisions and fact-checking

### Content Strategy Alignment

  - Challenge: Clients often request highly technical content that's difficult to verify
  - Solution: Propose a funnel approach, starting with broader topics to build authority
  - Tactic: Create separate pipelines for technical vs. general content
  - For technical content: Limit sources to client's official documentation/repos

### Improving Output Quality

  - Experiment with assignment directions to guide initial output
  - Utilize personas strategically (e.g., create a pipeline targeting specific audience)
  - Understand inputs for each stage to effectively influence results
  - Use LLMs externally to brainstorm article ideas from keywords

### Client Management

  - Establish GrowthX as content strategy experts early in relationship
  - Balance client requests with best practices for SEO and audience growth
  - Propose broader topics for "easy wins" to build trust before tackling highly technical content

---

## Action Items

**Matthew Panzarino**
- Record explanatory video/docs on Atlas system functionality, workflow, best practices

- Clarify w/ Kirkland re. new assignment direction field functionality, limitations, best use


**Saskia Wartnaby**
- Experiment w/ Atlas assignment directions field; test impact on brief/outline generation

- Prep for Prophecy call; gather Qs re. tech content, personas, writing style preferences

- Review/update Prophecy writing guidelines; align w/ tech audience, funnel strategy, SEO best practices

---

## Transcript
**Saskia Wartnaby:** Hi.

**Saskia Wartnaby:** Can you hear me fine?

**Matthew Panzarino:** I can.

**Saskia Wartnaby:** Hello.

**Saskia Wartnaby:** Awesome.

**Saskia Wartnaby:** Hello.

**Saskia Wartnaby:** I don't think we've had a one-on-one call yet, so it's lovely to chat with you.

**Matthew Panzarino:** Yeah, nice to meet you.

**Saskia Wartnaby:** Yeah, you too.

**Saskia Wartnaby:** I'll be upfront.

**Saskia Wartnaby:** I haven't had much chance to play around with Atlas, and this is also my first time.

**Saskia Wartnaby:** I've been moved to a new client.

**Saskia Wartnaby:** I came from unstructured.

**Saskia Wartnaby:** It was a bit hectic.

**Matthew Panzarino:** Yeah.

**Saskia Wartnaby:** So I started recently, and I've just been really struggling with getting the, well, aerobs to kind of get me a good output.

**Saskia Wartnaby:** I'm just really struggling with chatting with everyone, trying to figure it out, hearing everyone say, oh, we don't use the grid.

**Matthew Panzarino:** Yeah, yeah, yeah.

**Matthew Panzarino:** That's a huge problem, obviously, for the company as a whole, and also individual people, because it's a cascading thing.

**Matthew Panzarino:** So like, oh, yeah, we don't use the grids, we use ChatGPT.

**Matthew Panzarino:** And I'm like, okay.

**Saskia Wartnaby:** That's not helpful.

**Matthew Panzarino:** Yeah, yeah, exactly.

**Saskia Wartnaby:** It's not helpful.

**Saskia Wartnaby:** But then they're like, oh, and we're underwater.

**Matthew Panzarino:** I'm like, well, yeah, because you're using ChatGPT.

**Matthew Panzarino:** So like, the company pacing, like the SOWs for the clients, the pacing, frankly, the margins, and the hiring, all of it is based on this idea that, hey, we do a ton of upfront work, massaging the workflows to get into a place where they're getting something that's within 5% to 10% of shippable.

**Matthew Panzarino:** You know, like, close to editing, you know, within striking distance of editable.

**Matthew Panzarino:** My personal litmus test and goal is massage the work.

**Matthew Panzarino:** So you can get something out of it that you can edit within 15 minutes, like as an editor, you know, as a writer rewriting things.

**Matthew Panzarino:** If you know, you can easily spend a half an hour, 45 minutes, an hour writing any post we put out.

**Matthew Panzarino:** Understandable.

**Matthew Panzarino:** I can rewrite everything.

**Saskia Wartnaby:** I can take the best content we finished and rewrite it.

**Saskia Wartnaby:** And rewrite it.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** You know, that's that's cool.

**Matthew Panzarino:** But but what we need to do is meet client expectations by providing them something that they feel meet their bar of quality.

**Matthew Panzarino:** Our bar of quality should always be higher than the clients so that we start knowing that what we're delivering today is not as good as what we'll deliver tomorrow.

**Matthew Panzarino:** And that's what article refreshes are for.

**Matthew Panzarino:** That's what content is.

**Matthew Panzarino:** You know, we're like, hey, we have new state of the art.

**Matthew Panzarino:** We're going to go back and like, you know, retrench these pieces and update them, etc.

**Matthew Panzarino:** So the goal is spend an enormous amount of time on the company context, the personas, the writing guidebook.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Input that is, you know, as valid as it can be, as feature-rich, as important as it can be, then spend a bulk of your workflow time editing the briefs and the outline, and then spend a de minimis amount of time actually editing the final output, right?

**Saskia Wartnaby:** Because I think the main issue I found with that, so I did an article for Unstructure that I was actually quite happy with.

**Saskia Wartnaby:** It was like a top trends.

**Saskia Wartnaby:** But the main issue I'm having is that it's not, like, the outline and the first drop are not taking my writing instructions into account.

**Saskia Wartnaby:** Um, and then from, they will now.

**Matthew Panzarino:** They don't.

**Saskia Wartnaby:** Yeah.

**Saskia Wartnaby:** See, now, this is the biggest issue is that I end up with, like, a super long article.

**Saskia Wartnaby:** like, a article.

**Saskia Wartnaby:** None of it is formatted correctly.

**Saskia Wartnaby:** have to condense it.

**Saskia Wartnaby:** And condensing it, I'm finding, is just reducing the quality and making it so confusing.

**Saskia Wartnaby:** Because from my standpoint, I worked for one of the biggest SEO companies in America.

**Saskia Wartnaby:** And we used to do easily digestible, easily scannable, 1,100 word articles or 2,000 word articles.

**Saskia Wartnaby:** So that's kind of where I'm coming from.

**Saskia Wartnaby:** And this thing is spitting out like 4,000 word articles.

**Saskia Wartnaby:** And when you try and get it to reduce it, it's compacting everything into like, so it'll take like two separate sentences with two separate ideas and try and smush them into one sentence.

**Saskia Wartnaby:** And it's, you're, I'm, I'm finding that very difficult.

**Saskia Wartnaby:** I think it's important to understand the way the workflows actually work.

**Matthew Panzarino:** And that's why I've really poured more, you know, and we'll get some training and all this stuff.

**Matthew Panzarino:** But I think it is really important to understand what they're actually taking as input.

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** Then you won't be frustrated, you're changing the thing and nothing is changing.

**Matthew Panzarino:** Because it doesn't look, right?

**Saskia Wartnaby:** It's not looking at it, yeah.

**Matthew Panzarino:** Instructions are applied to the, the writing guidelines are applied to the draft.

**Saskia Wartnaby:** And I think you mentioned that you can give a little bit of instructions in the brief, but it's not like, like talking to an LLM.

**Saskia Wartnaby:** So I guess the question I have mainly for you is then like, how can you give it, can I give it a lot of instructions there or not really?

**Matthew Panzarino:** And how would I do that then?

**Matthew Panzarino:** You're, you're, the writing, the brief is your time to make sure that it does not have extraneous sections and like extraneous like information.

**Matthew Panzarino:** The brief and the outline are where you can really control length because it's going to put like, let me give you an example.

**Saskia Wartnaby:** Sorry, also, hello, Ehtisham, I hope I'm saying your name right.

**Saskia Wartnaby:** We haven't met yet.

**Saskia Wartnaby:** I haven't met Amy yet.

**Saskia Wartnaby:** I haven't realized you joined the call.

**Saskia Wartnaby:** We're just talking.

**Ehtisham Hussain:** Hello.

**Ehtisham Hussain:** Yeah, I've been

**Ehtisham Hussain:** Fly on the wall.

**Matthew Panzarino:** Yeah, yeah, it's all good, it's all good.

**Matthew Panzarino:** We'll just dive in, we'll just mess around.

**Saskia Wartnaby:** We'll probably need to have a meeting with you this week.

**Matthew Panzarino:** We will do more of these, right?

**Saskia Wartnaby:** This isn't like your last chance to ever talk to me about this.

**Matthew Panzarino:** Okay, yeah, because I haven't also played around with it yet, so I do want to pick your brains when like I have played around with it, yeah.

**Matthew Panzarino:** Let's do, so writing guidelines, what's your, well, let me talk to you a little bit about this from an ideal perspective, and then we can look at your client, or your, okay.

**Matthew Panzarino:** So this good call one, I wrote these, right?

**Matthew Panzarino:** So I know that, I'm not going to explain that they are the best ever, but like at least I know what I did here, right?

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** So the audience personas, you know, the, these are pretty straightforward for good call, like customer service managers, IT directors, digital transformation officers, small business owners, and healthcare administrators, right?

**Matthew Panzarino:** These have like objectives, motivations, pain points, decision drivers, relevant features and value.

**Matthew Panzarino:** The good news is...

**Matthew Panzarino:** By the way, everything in here is fair game.

**Matthew Panzarino:** Like if you don't know, if you're like, I wonder what, oh, if so-and-so said they didn't have a great result, go look at their stuff.

**Matthew Panzarino:** Shamelessly copy it, right?

**Matthew Panzarino:** Like we're not in the silo, right?

**Matthew Panzarino:** There's no thing you can't copy somebody else's homework here.

**Saskia Wartnaby:** not competing.

**Matthew Panzarino:** And in fact, we need to create some best practices.

**Matthew Panzarino:** That's why I recorded the thing and I'll record the part.

**Matthew Panzarino:** Because like what was happening is a lot of people that were telling me I'm getting bad results out of air ops.

**Matthew Panzarino:** I'm like, oh man, that sucks, right?

**Matthew Panzarino:** Let me go look.

**Matthew Panzarino:** And it's like, no, no wonder because they were given a very random instruction.

**Matthew Panzarino:** Like you're at LLM and you're going to write a cool article.

**Saskia Wartnaby:** And I'm like, all right, that's not enough.

**Matthew Panzarino:** By default, it's going to do that.

**Matthew Panzarino:** So it's just like there's a variety of things that were happening here, past instruction.

**Matthew Panzarino:** Because the company is very young.

**Matthew Panzarino:** so like there's a lot of conflicting information.

**Matthew Panzarino:** The trainings were very haphazard.

**Matthew Panzarino:** So.

**Matthew Panzarino:** The past is the past.

**Matthew Panzarino:** So the audience personas here, that is kind of what that, like, when you're going in your pipeline and you are creating, you know, you're at these assignment directions, right, that you're here, you can say target the IT manager persona specifically, right?

**Saskia Wartnaby:** Yeah.

**Saskia Wartnaby:** Is that kind of, like, the extent of the direction?

**Matthew Panzarino:** Like, yeah, I'm not sure what direction you would recommend to give it.

**Saskia Wartnaby:** The assignment direction is brand new, by the way.

**Matthew Panzarino:** So I'm telling you what I believe to be true about this at the moment.

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** I need to find out if it's actually true.

**Saskia Wartnaby:** This is a brand new thing that they just introduced with Atlas.

**Saskia Wartnaby:** was not in Atlas.

**Saskia Wartnaby:** Right?

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** So I want to, this is why people are like, oh, you should record something.

**Matthew Panzarino:** I'm like, I will.

**Saskia Wartnaby:** I don't, yeah, when I know.

**Saskia Wartnaby:** don't like to talk out of my keister about stuff.

**Matthew Panzarino:** So I don't, I don't want to like tell you.

**Matthew Panzarino:** And because then it's, I don't know, like somebody who's in Africa is watching it at 3 a.m.

**Matthew Panzarino:** my time and thinking this is the ground truth.

**Saskia Wartnaby:** And I don't talk to them for a month and they, you know, I'm, I'm that somebody in Africa.

**Matthew Panzarino:** Yeah, yeah, exactly.

**Matthew Panzarino:** So I think that's, it's a, it's a literal thing with remote.

**Matthew Panzarino:** So I want to be sure, like I, I, when I, before I did the, the AirPods one, I literally had Kirkland walk me through what every field was, what it was mapped to, what it actually gave, et cetera.

**Matthew Panzarino:** So that I understood that most of that is still true here, but there's new things.

**Matthew Panzarino:** And I want to understand what those new things are.

**Matthew Panzarino:** that, and I think that some canonical explanation for what they are is important because you, you're expressing frustration and like, oh man, the length, like I'm telling it in the writing guidelines, don't do this.

**Matthew Panzarino:** It's not even taking the writing guidelines until the end.

**Matthew Panzarino:** And it's taking something where it's like, this should have been instructions you gave the outline, not the draft.

**Matthew Panzarino:** Because as you mentioned, it's just going to try and keep the outline and compact content, which is not always going to result in print.

**Matthew Panzarino:** So you could do this assignment direction.

**Matthew Panzarino:** I would say at this point, my best instruction for you is experiment a little bit here.

**Matthew Panzarino:** Okay.

**Saskia Wartnaby:** So I would have thought that that's where you put, because in the air ops, you gave it a keyword.

**Saskia Wartnaby:** And I know you said that that's more, I think, I think it was you or Darren said it's more like the title.

**Matthew Panzarino:** Article generation is kind of right.

**Saskia Wartnaby:** Oh, what is the assignment?

**Matthew Panzarino:** Assignment is when you dump the URL and you want it to do a SERP for keywords for it and create assignments based on that.

**Saskia Wartnaby:** This is the topic that you're entering here.

**Saskia Wartnaby:** Theoretically, you'd be getting this from the assignment.

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** Okay.

**Saskia Wartnaby:** this is, once again, something I have to record on, right?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Relationships between.

**Matthew Panzarino:** But, like, your assignment generation here, creating assignments, you're going to give it a URL.

**Matthew Panzarino:** Like, let me just do, I don't know, good call, I think, you're going to give it a URL that you have scraped using SEMrush or Ahrefs or something.

**Matthew Panzarino:** You've done keyword analysis on what they want to write about.

**Matthew Panzarino:** And they're like, hey, this is the company.

**Matthew Panzarino:** We want to write articles about these topics.

**Matthew Panzarino:** You have SEMrush do a keyword analysis for you.

**Matthew Panzarino:** You've got a bunch of URLs now.

**Matthew Panzarino:** You've exported them.

**Matthew Panzarino:** And the XML imports are here, by the way.

**Saskia Wartnaby:** I can.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** Okay, so you've got imports, but you've got a CSV that can import.

**Matthew Panzarino:** I'm sorry, I'm getting back here.

**Matthew Panzarino:** sorry.

**Matthew Panzarino:** I'm I'm

**Saskia Wartnaby:** Is that, sorry, is that something that you would do, Ehtisham, or is that something that I would be doing?

**Saskia Wartnaby:** I've never done the assignment generation thing before.

**Ehtisham Hussain:** I think this falls in my domain.

**Saskia Wartnaby:** Okay.

**Ehtisham Hussain:** Okay.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** I was like, I've never done this.

**Saskia Wartnaby:** Yeah, in general, because the ME is like the tactical layer, right?

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Theoretically, the directors are the customer management and relationship in a high-level strategy layer where the customer is expressing their hopes and fears.

**Matthew Panzarino:** And then they're distilling it in a way that ME is like, okay, tactically, here's how we achieve those goals and then how we achieve those outcomes.

**Matthew Panzarino:** And then as a CM, you're like, oh, cool.

**Matthew Panzarino:** Like, I'm so happy to have the playbook.

**Saskia Wartnaby:** How do, let me execute on that.

**Saskia Wartnaby:** How do we execute on that?

**Matthew Panzarino:** And even, you know, there should be a dialogue with like, it's really hard to execute on this book because we've got some conflicts here.

**Matthew Panzarino:** And then Ehtisham is like, okay, let me talk to the director.

**Matthew Panzarino:** Because I think we've got a conflict, you know, let's adjust this.

**Matthew Panzarino:** Yeah, because in Structured, when I got it, there was issues with the context.

**Saskia Wartnaby:** And there was also issues with the type of articles that we were writing for them.

**Saskia Wartnaby:** And I kind of saw that from the beginning, just from a, because I did a lot of SEO content writing.

**Matthew Panzarino:** And the topics were setting us up for failure, I felt.

**Matthew Panzarino:** so, yeah, it is really, I thank you for thinking that way, because it is important that the CMs think very holistically about this.

**Matthew Panzarino:** Yeah, it is outcome oriented.

**Matthew Panzarino:** Our work is oriented, right?

**Saskia Wartnaby:** The line has to be happy.

**Matthew Panzarino:** And you have to get results.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** You can get lost in the sauce a little bit on like, okay, we've got deliverables, we've published X articles a week, and we're on track, right?

**Matthew Panzarino:** But if you feel like, hey, there's something here that is not aligned well.

**Matthew Panzarino:** With the outcomes that they want from a page views or traffic or click through, whatever, raise it, talk, like, definitely have a dialogue, you know, talk with Ehtisham about it, he can talk with the director about it, or you can both talk to them and be like, hey, you got some going on.

**Matthew Panzarino:** Now, that's the reason that we kind of did the mix and match with these pods and people with expertise, because, yes, like, a certain pod may have an ME that's, like, SEO wizard, but then they're, like, you know, I'm not really an editorial person, like, I just know what works from a fundamentals perspective, and, like, I'm a tactical person on this, and then vice versa.

**Matthew Panzarino:** And, like, that's why I did that.

**Matthew Panzarino:** So it's important to have that.

**Matthew Panzarino:** But, yes, you're thinking exactly the right way about it.

**Saskia Wartnaby:** Okay, that's good.

**Matthew Panzarino:** Yeah, if we're generating articles, and you're like, I don't think this is going to, I don't think this is going to work the way you think it's This is going to go fly, yeah?

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** Yeah, we'll keep it.

**Saskia Wartnaby:** Yeah, because I'm just really struggling with the, like, you know, um.

**Saskia Wartnaby:** That balance between the quality and the output speed.

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** But people, I think we should meet the client expectations for deliverable.

**Saskia Wartnaby:** That's important.

**Matthew Panzarino:** But the story here is any existing client, we are sort of having to shuffle backwards into alignment.

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** Content quality, because we have sort of like a patchwork of client expectations that have been set by different kinds of onboarding calls.

**Saskia Wartnaby:** Yes.

**Matthew Panzarino:** Like they were like more on point or less on point or more how they should be.

**Saskia Wartnaby:** So the client had a different idea than what we were.

**Saskia Wartnaby:** I think that was a huge issue with unstructured.

**Matthew Panzarino:** Yeah, exactly.

**Saskia Wartnaby:** It's different expectations and we're never going to really be in the middle.

**Saskia Wartnaby:** But then the other question I have for you is that I see I'm a.

**Saskia Wartnaby:** Nervous about this client, because I was having a look at the Slack channel, and I know that they were using Claude a lot.

**Matthew Panzarino:** They were going out of the grid a lot.

**Saskia Wartnaby:** Yeah.

**Saskia Wartnaby:** So I think the main, I've got a handoff.

**Matthew Panzarino:** Which client?

**Saskia Wartnaby:** It's Prophecy.

**Saskia Wartnaby:** So I have a call with them later, and obviously we can go through all of that.

**Saskia Wartnaby:** But I think maybe once I have, I think once I have that information, I would want to come to you to figure out how I can get the results that they're getting outside.

**Matthew Panzarino:** Obviously, at this time.

**Matthew Panzarino:** went and filled out these for you.

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** You don't have to take these as rote, right?

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** You can delete them all if you want.

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** But I did put something in here for you.

**Matthew Panzarino:** So the Prophecy audience personas, you can get updated information from like the Slack conversations or from a personal conversation with the client, you know, at the show, especially, you know, tell them, I need to know these, these, these, and he can grill them, right?

**Saskia Wartnaby:** Okay.

**Saskia Wartnaby:** you get the information.

**Matthew Panzarino:** You need to do your job properly, but the company context should be at least decent, and then so should be, the CTA, don't even know, I just grabbed it for a minute, I don't know what it is.

**Saskia Wartnaby:** Okay, where does it put that CTA, is that just something it dumps at the end?

**Matthew Panzarino:** I don't know.

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** I mean, I do know, it should theoretically put it at end.

**Saskia Wartnaby:** Okay, all right.

**Matthew Panzarino:** But whether or not it actually calls it, I don't know, I haven't done Oh, okay, so I need to experiment with that.

**Matthew Panzarino:** Theoretically, the flow that creates the, one of the drafts should call this, right?

**Matthew Panzarino:** Like that, that particular module, that, that column should call CTA and say, pop this at the end, please, thank you.

**Matthew Panzarino:** But that's, that's theoretically what this is.

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** And then the writing guidelines here, this is, do not treat this as like actually good.

**Matthew Panzarino:** I would definitely look at this.

**Matthew Panzarino:** Because this writing guideline, I actually would.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Crib from Gitpod, I think.

**Saskia Wartnaby:** So I don't know if they actually care about any of this.

**Matthew Panzarino:** So you can look at what the existing writing guidelines, there was none in here.

**Matthew Panzarino:** That's why I think I'll have to chat with the team actually, let's just look really quickly while I still have access to it to see what, if anything, was in here.

**Matthew Panzarino:** But I'm going to guarantee you, because they're saying that they were running it in Cod, they probably never actually filled this out.

**Matthew Panzarino:** Which, it's one of those things that is chicken or egg.

**Matthew Panzarino:** Is it because they didn't fill it out properly that they were never able to use the word properly?

**Matthew Panzarino:** Yeah.

**Saskia Wartnaby:** Who knows?

**Matthew Panzarino:** So if you go in here, yeah, their polishing instructions, which is what this used to be called, is like, okay, I actually think I grabbed this from here and I put it in there.

**Saskia Wartnaby:** I was about to say that looks similar to what you just showed me.

**Saskia Wartnaby:** It's exactly what I put in.

**Saskia Wartnaby:** So this is what I did.

**Saskia Wartnaby:** I grabbed it from here and put it in there.

**Matthew Panzarino:** Because they may have had specific instructions.

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** Right, I hope.

**Matthew Panzarino:** From...

**Matthew Panzarino:** About what they want.

**Matthew Panzarino:** But I wouldn't lean into this.

**Matthew Panzarino:** Go look at Good Call, which I did myself, and see what this is.

**Saskia Wartnaby:** You can even start from scratch, right?

**Saskia Wartnaby:** And you can adapt what the client tells you into that, right?

**Matthew Panzarino:** To give you an idea, some of the instructions, like one of the ones that I did, I did a few, but I do remember Good Call being one I did.

**Matthew Panzarino:** So this Ideal Path, writing instructions here.

**Saskia Wartnaby:** Yes.

**Matthew Panzarino:** There's, it could take, like, a dozen, maybe more, major instructions with some context added.

**Matthew Panzarino:** It can't take, like, 50, 60 different instructions.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** It'll just forget things and not really...

**Saskia Wartnaby:** Yeah, because that's what I was noticing.

**Saskia Wartnaby:** Like, it just, like, I would say, like, use a serial comment, and it just wasn't doing, like, some of the instructions just wasn't using.

**Saskia Wartnaby:** Those specific things.

**Saskia Wartnaby:** They're better done at the end.

**Saskia Wartnaby:** At the end, okay.

**Matthew Panzarino:** That's why the new editor is going to incorporate an LLM window for you to, like, say, change this paragraph, remove that.

**Matthew Panzarino:** That would be amazing.

**Matthew Panzarino:** Make all EM dashes have a space before and after.

**Saskia Wartnaby:** Yeah, those are very specific things.

**Matthew Panzarino:** Exactly.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** It will not take – you can put it in here all you want, but you're – It wasn't.

**Saskia Wartnaby:** Okay, so this is for, like, the big structural things.

**Saskia Wartnaby:** Yes, exactly.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** the – imagine this, like, you were talking to a writer about how to write for this company, and they're just learning, and you're, like, you know what they love?

**Matthew Panzarino:** They love it when you make, like, you're really conversational about this, but you have a creditable angle.

**Matthew Panzarino:** They're not really stuffy.

**Matthew Panzarino:** They don't like highly technical language.

**Matthew Panzarino:** They love highly technical language because they speak to developers, right?

**Matthew Panzarino:** Like, you're explaining to a person about this.

**Matthew Panzarino:** Just think of it in a way.

**Matthew Panzarino:** Read it out loud to yourself in your head and, like, is this how I would explain this?

**Matthew Panzarino:** know, to say, like,

**Matthew Panzarino:** And so I did write in the task, hope and hope, I did put it, it's not really going to obey this, but it just might, you know, just like, and maybe it's better about, about that, you know, maybe we'll build in some rails.

**Matthew Panzarino:** But basically just kind of like, here's the objective.

**Matthew Panzarino:** Always use dates from 2025 when possible.

**Matthew Panzarino:** Tone, do's and don'ts, incredibly important.

**Matthew Panzarino:** LLMs love do's and don'ts.

**Matthew Panzarino:** You know, they really work very well on pattern matching, but they can't match patterns they don't know exist, right?

**Saskia Wartnaby:** Or they will just imagine their own, right?

**Matthew Panzarino:** And so I think it's like, enhance operational efficiency.

**Matthew Panzarino:** Don't say cheap or low cost, right?

**Matthew Panzarino:** Because they want their thing to be seen as cheap, right?

**Matthew Panzarino:** Focus on ROI, not bargain branding, right?

**Matthew Panzarino:** Or if they're like, oh, we're all about sales.

**Matthew Panzarino:** Like if you're Marshalls, if you're writing content for Marshalls.

**Matthew Panzarino:** It should be all about sales, right?

**Matthew Panzarino:** It should be all about deep discounts.

**Matthew Panzarino:** If you're writing for Nordstrom, you know, or Bloomingdale's, it should never say the word sale, right?

**Matthew Panzarino:** It should always be high quality, luxury, right?

**Matthew Panzarino:** Do's and don'ts.

**Matthew Panzarino:** 20, right?

**Matthew Panzarino:** Like this, you're telling it, don't use, this is your actual instructions right here.

**Matthew Panzarino:** This is the, like, what to do.

**Matthew Panzarino:** This is just the context, right?

**Matthew Panzarino:** So, is not 20 different instructions.

**Matthew Panzarino:** This is, like, here's what I mean, right?

**Matthew Panzarino:** You see what I mean, right?

**Matthew Panzarino:** You see what I mean, right?

**Matthew Panzarino:** Then, structure, title in the outline.

**Matthew Panzarino:** I like this, but it doesn't always obey that.

**Saskia Wartnaby:** Yeah.

**Matthew Panzarino:** I like titles to be, like, so I can vibe with it.

**Matthew Panzarino:** H2s, never use a colon in the headers.

**Matthew Panzarino:** hate that crap.

**Saskia Wartnaby:** Yeah.

**Saskia Wartnaby:** I so much.

**Saskia Wartnaby:** Don't use colons in headlines either.

**Matthew Panzarino:** That sucks, you know?

**Saskia Wartnaby:** Yeah.

**Saskia Wartnaby:** Do not use this, instead use this.

**Matthew Panzarino:** Like, you're the least something in the poll.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** I use this, instead use this.

**Matthew Panzarino:** This may be something you have to retcon, you know, in the final edit, but at least you can try it here.

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** And if you need to trim or move the least vital sections, this is something that really probably needs to be done by you in the outline.

**Saskia Wartnaby:** I was about to say, I don't think it can remove the decisions.

**Matthew Panzarino:** No, I can't.

**Matthew Panzarino:** But like, the outline, it generates something like case studies, like ditch that crap.

**Matthew Panzarino:** Unless they specifically export it, right?

**Matthew Panzarino:** Like, it won't go.

**Matthew Panzarino:** And then it won't generate it.

**Matthew Panzarino:** Then you won't end up with such a long article, right?

**Saskia Wartnaby:** Exactly, yeah.

**Matthew Panzarino:** You got to do that early before you get to 4,000 words.

**Saskia Wartnaby:** Oh, that's another thing I wanted to ask you.

**Saskia Wartnaby:** Like, when I was running for a structure that would, like, come up with these, like, for example, this company did this, and they got this percentage, and it would link to an article.

**Saskia Wartnaby:** And I could not find that information in the article.

**Saskia Wartnaby:** Is that it just coming up with things?

**Saskia Wartnaby:** Because I did include that hallucination thing that you added for Good Call.

**Saskia Wartnaby:** But it was.

**Saskia Wartnaby:** It's definitely, okay, I just wanted to check that.

**Saskia Wartnaby:** did include it or didn't?

**Saskia Wartnaby:** I did, I did include it.

**Matthew Panzarino:** Okay, well, if you did include it and it's still giving it to you, you can add instructions specifically about citations.

**Matthew Panzarino:** then also what the fact checker is for.

**Saskia Wartnaby:** Yes.

**Matthew Panzarino:** The checker should find those a lot of times.

**Matthew Panzarino:** Okay, okay.

**Matthew Panzarino:** they're internal links, external links, 50-50, but the fact checker is pretty good.

**Matthew Panzarino:** Okay, all right, that's good.

**Matthew Panzarino:** Always run the fact checker before you even really start to care about whether or not it's there.

**Saskia Wartnaby:** so it'll just lessen your time in edit, you know, where you're checking on those things.

**Saskia Wartnaby:** Yeah, because I think one thing I battled with and structured was that their target audience, I think this is just a bad strategy alignment, but their target audience, and I've noticed this is the same for prophecy, is like really like data scientists and like really technical people.

**Saskia Wartnaby:** And so it was spitting out these articles that were like super technical.

**Saskia Wartnaby:** And I know like from, I used to write super technical articles for my.

**Saskia Wartnaby:** But we took it from a point of like, I'm not going to be an expert on this, but I can write you a good SEO article that will get you to rank.

**Matthew Panzarino:** But the AI is like spinning out this super highly technical stuff.

**Matthew Panzarino:** And I just don't have the knowledge to say like, yes, this is right or no, it's not.

**Saskia Wartnaby:** And I think that's scaring me quite a bit that I have to rely on the fact checker to like catch those things.

**Saskia Wartnaby:** I don't know if have any advice.

**Matthew Panzarino:** I think it's, so I think there is an alignment thing.

**Matthew Panzarino:** And one thing that I have done or instructed directors to do and they've done with some success is basically talk to the client about funnel.

**Matthew Panzarino:** Like say, hey, we need to start out.

**Matthew Panzarino:** I know you want deeply technical articles, but we need to start out by capturing people that are just starting to learn about this topic as well.

**Saskia Wartnaby:** Yes, exactly.

**Saskia Wartnaby:** Because provides you with a base layer of traffic and rank authority.

**Saskia Wartnaby:** And it's just also good for like just.

**Saskia Wartnaby:** Just catching a wider audience and for making things understandable because, yeah, only one group of people would understand.

**Matthew Panzarino:** Yeah, I think one thing that people are forgetting to do, and usually I've been really, I'm speaking more at the ME and director layer, is they're forgetting to establish that we are the experts here.

**Saskia Wartnaby:** And like, these people are coming to us.

**Matthew Panzarino:** And I think in the calibration article or the calibration phase, a lot of times it was like, oh, what do you want?

**Saskia Wartnaby:** Yeah, not what we say we should do.

**Matthew Panzarino:** Yeah, it's more a mix of what do you want?

**Matthew Panzarino:** Okay, here's what we recommend.

**Saskia Wartnaby:** Yeah, I think that came too late with Unstructured.

**Saskia Wartnaby:** And I, yeah, I think, yeah, I think that's why I'm just panicking so much because I just had this experience with Unstructured.

**Saskia Wartnaby:** But I did hear that prophecy is in a good place.

**Matthew Panzarino:** So now I just need to figure out how to keep it that way.

**Matthew Panzarino:** The opportunity to offer broader topical content can give us easy wins and early wins.

**Matthew Panzarino:** It can alleviate some of the initial adjustment with the client of whether they're like, can these people actually deliver real value?

**Matthew Panzarino:** Because when it comes time to deliver technical content, they're not like buffing up their microscopes.

**Matthew Panzarino:** Yeah, that makes sense.

**Matthew Panzarino:** Yeah, it's like it won't stand up to a developer reviewing every single line just because they're going to be pedantic.

**Matthew Panzarino:** And a lot of times it comes down to philosophy.

**Matthew Panzarino:** And it's like, get real, people.

**Matthew Panzarino:** Like, you are saying you believe a certain thing to be true, but this is objective fact.

**Saskia Wartnaby:** Yeah.

**Matthew Panzarino:** What we have published in this article, and you are objectively saying, that's not the way I think about it.

**Saskia Wartnaby:** Yeah.

**Saskia Wartnaby:** You're right.

**Matthew Panzarino:** Like, yeah, who gives a , right?

**Matthew Panzarino:** Like, you know, you're, it's the, you could absolutely be capturing an audience that does believe this to be true.

**Saskia Wartnaby:** And then they come into your world, and then you can educate them otherwise, right?

**Saskia Wartnaby:** Yeah.

**Matthew Panzarino:** But like the, that, that kind of push, gentle.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** That

**Matthew Panzarino:** So, uh, diplomatic pushback and tangling is what the entry layer and director layer is supposed to And you, as a CM, have a voice in that conversation where you're like, can we pitch this to the client that we should do some funnel?

**Matthew Panzarino:** Because this is really much further down the funnel.

**Matthew Panzarino:** And if we don't establish authority or establish breadcrumbs here, we're sort of plopping this at the top layer of their breadcrumb.

**Matthew Panzarino:** And the SEO results of this are going to be the minimum because we're not establishing ground rules.

**Matthew Panzarino:** So that's, we are strategists and we're strategists on the content level and the SEO level.

**Matthew Panzarino:** And like those things need to mate and we can have an analog.

**Matthew Panzarino:** So it's also not like, oh, you've been delivered a sandwich of expectations.

**Matthew Panzarino:** And then you are like struggling to deliver that with the workflows.

**Matthew Panzarino:** You should also have the voice to be able, I'm sorry for saying.

**Matthew Panzarino:** And you can get paid for this for that.

**Saskia Wartnaby:** I'm sorry.

**Matthew Panzarino:** But the, yes, we can have a dialogue about that and figure out what works there.

**Matthew Panzarino:** However, we should strive to establish a workflow and it could be a custom one, like a separate pipeline in the same project, like duplicate a pipeline, create a new pipeline in the same project.

**Matthew Panzarino:** Heck, even creating a project if you have to, that is just really hyper-geared towards like delivering technical deliverables.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** And then the resourcing is let's grab Kirkland and do a meeting with them about like specific needs on targeting this.

**Matthew Panzarino:** And they're actually maybe, this is one of my, I need to learn still.

**Matthew Panzarino:** There are actually maybe things for us to say, don't use any other sources for this article than Prophecy's GitHub repo and developer documentation.

**Matthew Panzarino:** Don't tell me anything that's not in there.

**Matthew Panzarino:** Anything that's done in there, in this article, and then you rewrite the writing guidelines and company context for that workflow that provides a very specific persona that you're writing for.

**Saskia Wartnaby:** Yeah.

**Matthew Panzarino:** A very specific way of writing about it that says you are going to write in a technical fashion.

**Matthew Panzarino:** You're going to use these words.

**Matthew Panzarino:** You're going to talk about it in these ways.

**Matthew Panzarino:** You're going, this is your philosophy, right?

**Matthew Panzarino:** This is from them.

**Matthew Panzarino:** We wouldn't invent this, we would say.

**Saskia Wartnaby:** Yes, exactly.

**Matthew Panzarino:** Like, do you have your head developer, like, writing about this in any fashion, or talking about it on the podcast, or anything that, you know, you have that says your philosophy towards data security implementation for access manager, identity access managers, right?

**Matthew Panzarino:** Like, aim bit it this way.

**Matthew Panzarino:** They're like, yeah, I all these opinions.

**Saskia Wartnaby:** And it's like, okay, great.

**Saskia Wartnaby:** Great, give them to me.

**Saskia Wartnaby:** know what those are and inject them, right?

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** We can create a custom one.

**Matthew Panzarino:** Basically says, like, limit your scope to these resources so that we know that there's accuracy and veracity.

**Matthew Panzarino:** Yes.

**Saskia Wartnaby:** Right?

**Matthew Panzarino:** Yeah.

**Saskia Wartnaby:** so there are ways to do that now to some degree in these existing flows, but if we need to get hyper-specific, we can.

**Matthew Panzarino:** I think these would be absolutely fine for top to mid-funnel, like the articles are closed as they stand.

**Matthew Panzarino:** When it gets to, like, the highly technical articles right now, the thing you can do is in your feedback, you can just say, hey, this is, maybe because they're still launching this, but they should launch it this week, hopefully, is the ability to edit the articles via the LLM box in Atlas.

**Saskia Wartnaby:** would be amazing.

**Saskia Wartnaby:** So that outline and you say, oh, this is a code block?

**Matthew Panzarino:** I don't know, you know?

**Matthew Panzarino:** And you can say, hey, check this against this URL.

**Matthew Panzarino:** This is, you know, Prophecy's GitHub repo or their developer documentation.

**Matthew Panzarino:** Can you verify this, that this code is correct?

**Matthew Panzarino:** And it's like, no, actually, I looked at the developer documentation and it's safe to do this instead.

**Saskia Wartnaby:** Yeah, that would be amazing.

**Saskia Wartnaby:** Well, see.

**Matthew Panzarino:** But ideally, it shouldn't even be you having to type it manually.

**Matthew Panzarino:** It should be built into the pipeline.

**Matthew Panzarino:** But I don't want to talk out of turn.

**Matthew Panzarino:** I want to like figure out where in this pipeline, like where in the article generation flow that needs to exist and whether we need to add a new artifact, you know, whether style adaptation is enough where we can like call URL in this as well.

**Matthew Panzarino:** Because right now, style adaptation calls as an input.

**Matthew Panzarino:** It doesn't show me here.

**Matthew Panzarino:** See, I don't want to fumble around.

**Matthew Panzarino:** I'm able to add a glance, see what each of these call.

**Matthew Panzarino:** But I think it's in pipeline.

**Matthew Panzarino:** Anyhow, I'll figure it out.

**Matthew Panzarino:** But you should be able to see like what these are calling as inputs after you run them to show you.

**Matthew Panzarino:** I want to see how I can figure out the ground for.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** But you

**Matthew Panzarino:** You can see that the outline calls the topic and it calls the context.

**Matthew Panzarino:** The context, yeah.

**Matthew Panzarino:** And then I think it calls the research.

**Matthew Panzarino:** And that's it.

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** Right?

**Saskia Wartnaby:** Okay, so I need to really go through all of those and just check what it's actually doing so I can put the instructions in the correct place.

**Saskia Wartnaby:** And I'm really grateful for you clarifying that, like, you know, the writing instructions aren't, you know, I need to make the brief an area where I use some structural things and then use my really nitpicky stuff for the end.

**Matthew Panzarino:** Yeah, and you'll have a brief section editor for this, like, stat, you know, so just suffer for, for the end.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** Like, if you do the outline and you look at this outline and you're like, oh, they don't need modular pipeline components.

**Matthew Panzarino:** This is, you know, terribly, right?

**Matthew Panzarino:** That's, like, 700 words right there.

**Saskia Wartnaby:** Yeah, yeah.

**Saskia Wartnaby:** So it's not going to, it's not going to, so let's, sorry, if I, so it's given me the brief outline, right?

**Saskia Wartnaby:** If I delete a section.

**Saskia Wartnaby:** It's not going to try and make the other sections longer to get to some, I don't know what length.

**Saskia Wartnaby:** if you delete that section, it's going to make it shorter.

**Matthew Panzarino:** Yeah, because if you look at the brief output, you can see, like, Yeah.

**Matthew Panzarino:** So in this brief, like, lists, common tickles and how to troubleshoot them.

**Matthew Panzarino:** This thing is so common in briefs.

**Saskia Wartnaby:** Yes.

**Matthew Panzarino:** I hate this.

**Saskia Wartnaby:** Yeah.

**Matthew Panzarino:** This is like a thousand words, right?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** You can ditch stuff like this or, like, it may be, it may be a thing where you can even prompt it in, you know, when you're doing the assignment, like, you can try that, like, assignment directions, like, don't include common pitfalls, right?

**Matthew Panzarino:** But deleting this out of this and then continuing on from there is like a win right away on length, right?

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** I think that this is really interesting to, like, go through this and to understand what it's trying to do.

**Matthew Panzarino:** Like, read through these things to see what it's actually saying.

**Matthew Panzarino:** And I think after a little while, you'll realize, like, some of this can be influenced by your inputs, right?

**Matthew Panzarino:** The inputs for this one, once again, are the URL, if it's a URL, or the keyword, it's a keyword, that little direction field, right, that you can populate.

**Matthew Panzarino:** And then the company name, and then the personas, right?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** So if you're, like, finding that it's really writing in a funky way, and you're like, I need a batch of articles that are really all targeted towards data analysts, just create a separate pipeline that's just for the data analyst thing.

**Saskia Wartnaby:** And delete all the other personas, right?

**Matthew Panzarino:** Okay.

**Saskia Wartnaby:** Just remember what you're saying, you can't create a dozen pipelines for each kind of article you want to write.

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** You don't have to create these, think these are one size fits all.

**Matthew Panzarino:** One size, okay.

**Matthew Panzarino:** And they probably won't be, right?

**Saskia Wartnaby:** Yeah.

**Saskia Wartnaby:** all.

**Matthew Panzarino:** And then what else does it take?

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Executive summary.

**Matthew Panzarino:** Take the company summary.

**Saskia Wartnaby:** A way to influence it.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** That's fair.

**Matthew Panzarino:** But that's it, right?

**Matthew Panzarino:** That's all it takes from there.

**Matthew Panzarino:** So those are the only inputs that you have to, like, manipulate what you're going to get as a brief.

**Matthew Panzarino:** So it helps to understand what's coming in so that you know what you're actually influencing.

**Matthew Panzarino:** Because it can be frustrating to change variable acts and not see any.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Well, no wonder.

**Saskia Wartnaby:** It's not even looking at variables.

**Matthew Panzarino:** So I think that's a cool thing to look to.

**Saskia Wartnaby:** For sure.

**Saskia Wartnaby:** Yeah.

**Matthew Panzarino:** And then, yeah, like, the outline is a genuine way to influence.

**Matthew Panzarino:** Oh, when you do your inputs, like, you're creating these things, these previously were, like, people were just going, like.

**Saskia Wartnaby:** Yeah, I think Daryl mentioned that to me.

**Saskia Wartnaby:** And there's no.

**Matthew Panzarino:** No wonder you're getting stressed.

**Matthew Panzarino:** short-tail keyword.

**Matthew Panzarino:** It's not going to do anything.

**Matthew Panzarino:** It's to give you something.

**Saskia Wartnaby:** Something, but probably not what you want.

**Saskia Wartnaby:** No.

**Matthew Panzarino:** So that's a huge thing.

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** Make sure that that's...

**Saskia Wartnaby:** help a lot.

**Matthew Panzarino:** Yeah.

**Saskia Wartnaby:** that's what you want, right?

**Saskia Wartnaby:** Or compare this thing to this thing.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** And just keyword stuff it.

**Matthew Panzarino:** Yeah, your keyword stuff is all you want, but it does not have to be just the raw keyword.

**Matthew Panzarino:** I think in a of cases, the earliest versions of these workflows or the trainings was just run a search for authority, sort that by authorities below 80 and above 30 that we could target the wins on, copy those keywords, drop those into the assignment brief workflows, and run all of them.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** And then take all of those assignments, which are essentially keywords, you know, that they were generated off of that, and then run those as articles.

**Matthew Panzarino:** Articles, yeah.

**Matthew Panzarino:** And it's like, no wonder, you know, that you're really broad and meandering results, right?

**Matthew Panzarino:** Yeah.

**Saskia Wartnaby:** So, like, honestly, this doesn't even have to be something you write manually.

**Matthew Panzarino:** If you want to generate a dozen articles at a time, you can take the keywords.

**Matthew Panzarino:** And that's a great case for, like, asking an LLM for a minute, like, for some help.

**Matthew Panzarino:** And hopefully, eventually, you stop that brainstorming on platform.

**Matthew Panzarino:** But you can say, here's 10 keywords.

**Saskia Wartnaby:** Convert these into how-to titles.

**Saskia Wartnaby:** Okay.

**Matthew Panzarino:** And then you can use those to populate the fields and then run your information there.

**Matthew Panzarino:** So, those are all ways that you can fiddle.

**Matthew Panzarino:** So, I would say jump in and start messing.

**Matthew Panzarino:** This is not going be the only time we talk about this.

**Matthew Panzarino:** Perfect.

**Matthew Panzarino:** We're to like, many, many more meetings in the next week.

**Saskia Wartnaby:** Yes, sure.

**Saskia Wartnaby:** So, let me go prep for that.

**Matthew Panzarino:** But it gives you a little bit of context.

**Matthew Panzarino:** Yeah, this was really helpful.

**Saskia Wartnaby:** Thank you so much, Matthew.

**Saskia Wartnaby:** And it was lovely to meet you in the shop.

**Ehtisham Hussain:** Also, I'm sure I'll chat to you guys sometime soon.

**Matthew Panzarino:** Thank you very much again.

**Saskia Wartnaby:** And we'll see each other tomorrow morning too.

**Saskia Wartnaby:** Yes, we will.

**Saskia Wartnaby:** Cool.

**Saskia Wartnaby:** Bye, everyone.
