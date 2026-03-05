# CMs Daily Standup – Atlas Sync

<metadata>
date: 2025-06-17
time: 15:29 UTC
duration: 65 minutes
organizer: Saskia Wartnaby
participants: Oluwatimilehin Ademosu, Matthew Panzarino, Mariana Marins, Usman Adepoju, Ademilade Shodipe-Dosunmu, Nika Narimanidze, Jess Scott, Jenn Peters, Rachel Pasche, Matthew Alves-Hill, Andi Bailey
fathom_recording_id: 68858984
fathom_url: https://fathom.video/calls/328417463
share_url: https://fathom.video/share/1RzR93z1gtCt-3fZqDMuBegfKoYxaKQn
source: fathom
enriched_on: 2026-03-03 20:06 UTC
</metadata>

---

## Summary

GrowthX's Content Management team conducted a daily standup to address urgent priorities for Atlas, a new AI-powered content generation platform replacing AirOps. Matthew Panzarino emphasized that company context, personas, and writing guidelines must be meticulously ported from AirOps and expanded with detailed, "dense" information to produce quality outputs — the LLM can't generate good content from sparse inputs. The team discussed several critical bugs (missing outline outputs, incorrect company contexts), reporting procedures (Linear tickets + EBD Slack channel), and resource constraints (API rate limits, 3-8 minute processing per step). Next steps: each CM must review and update their artifacts by end of week, file Linear tickets for reproducible bugs, and leverage Notion records and Fathom transcripts with clients as reference material.

---

## Context

This is a GrowthX internal CMs (Content Managers) daily standup — not a client call. The team is transitioning from AirOps (an older AI workflow system) to Atlas, a new platform that powers the content generation process. Atlas has the same backend as AirOps but with a different user interface, so everything is being migrated. The transition is urgent because AirOps access could be shut off at any time. Atlas is still in beta — the EPD (Engineering/Product/Design) team is actively fixing bugs reported by the CMs, so feedback and Linear tickets are critical for product improvement. The CMs are the first and only users of this platform before external clients gain access.

---

## Relevance

**To GrowthX Delivery:**
- Critical workflow migration from AirOps to Atlas must complete by end of week to meet client deadlines; all CMs must have functioning, tested workflows by Friday
- Company context and personas need to be "dense" and detailed — sparse inputs (e.g., just company name) produce weak AI outputs that require heavy editorial lift
- Writing guidelines should be living documents, reviewed monthly or weekly as clients release new materials, press releases, or strategic shifts
- Artifact density directly impacts content quality: unclear company positioning, thin personas, or vague brand guidelines will degrade output and increase rework

**To CheckThat:**
- Team is using AI visibility and content quality principles in real-time as they discover the limits of sparse vs. rich context in LLM generation
- Bug reports and feature requests (e.g., article type picker, assignment direction mapping) will inform product roadmap for AI-driven content tools

**To GrowthX Business Development:**
- Successful Atlas launch depends on customer support: CMs need one-on-one training and documentation to avoid delays in service delivery, which protects renewal and expansion revenue
- Client-specific pods (external Slack channels, Fathom meeting transcripts) are the most up-to-date source of truth for refreshing company context and writing guidelines — leverage these in onboarding

---

## Overview

- Urgent priority to review and update all artifacts (company context, personas, writing guidelines) in Atlas
- Atlas workflows use same backend as AirOps but interface is different; aim to transition ASAP as AirOps access could be cut off any time
- Several bugs and issues reported; file Linear tickets and use EBD Slack channel for help
- One-on-one sessions available to help set up workflows and address any blockers

---

## Key Topics

### Atlas Workflow Setup

  - Check all artifacts were ported over correctly from AirOps
  - Company context, user personas, writing guidelines need to be detailed and robust
  - Can use GitPod artifacts as template if starting from scratch
  - Aim to have workflows set up to process articles by end of week

### Bugs and Issues

  - Several bugs reported, including missing outline outputs and incorrect company contexts
  - File Linear tickets for clear issues, especially if workflows are erroring out
  - Check Linear and EBD Slack channel for known issues before filing new tickets
  - Some issues may be due to API rate limits or backend changes during transition

### Resources and Training

  - Reference AirOps training video for workflow setup principles
  - Daniel's recent training video useful for understanding Atlas fields
  - More detailed documentation and Notion manual for Atlas coming soon

### Team Restructuring

  - Recent pod changes aimed at mixing competencies (technical SEO, editorial skills)
  - Goal is to create stable teams that can support all client needs
  - Intended to address gaps in training and reduce client churn

---

## Action Items

**Oluwatimilehin Ademosu (GrowthX)**
- Review and update artifacts (company context, user personas, writing guidelines). Ensure dense, robust information. Verify all items ported correctly from AirOps to Atlas.

**Jess Scott (GrowthX)**
- Review and update artifacts (company context, user personas, writing guidelines). Ensure dense, robust information. Verify all items ported correctly from AirOps to Atlas.

**Usman Adepoju (GrowthX)**
- Review and update artifacts (company context, user personas, writing guidelines). Ensure dense, robust information. Verify all items ported correctly from AirOps to Atlas.

**Nika Narimanidze (GrowthX)**
- Review and update artifacts (company context, user personas, writing guidelines). Ensure dense, robust information. Verify all items ported correctly from AirOps to Atlas.

**Ademilade Shodipe-Dosunmu (GrowthX)**
- Review and update artifacts (company context, user personas, writing guidelines). Ensure dense, robust information. Verify all items ported correctly from AirOps to Atlas.

**Mariana Marins (GrowthX)**
- Review and update artifacts (company context, user personas, writing guidelines). Ensure dense, robust information. Verify all items ported correctly from AirOps to Atlas.

**Jenn Peters (GrowthX)**
- Review and update artifacts (company context, user personas, writing guidelines). Ensure dense, robust information. Verify all items ported correctly from AirOps to Atlas.

**Rachel Pasche (GrowthX)**
- Review and update artifacts (company context, user personas, writing guidelines). Ensure dense, robust information. Verify all items ported correctly from AirOps to Atlas.

**Matthew Alves-Hill (GrowthX)**
- Review and update artifacts (company context, user personas, writing guidelines). Ensure dense, robust information. Verify all items ported correctly from AirOps to Atlas.

**Matthew Panzarino (GrowthX)**
- Check with EPD team regarding mapping of assignment direction field in Atlas pipelines. Clarify its function and proper usage.
- Follow up with Kirkland regarding blank outline output bug in Atlas. Ensure issue is addressed ASAP.
- Verify status of TERO workspace in Atlas. Ensure all necessary artifacts are present and correctly populated.

---

## Transcript
**Oluwatimilehin Ademosu:** Thank Thank you.

**Matthew Panzarino:** you.

**Matthew Panzarino:** This afternoon, this evening, et cetera.

**Usman Adepoju:** I'm doing good.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Okay, so pretty straightforward agenda for this meeting.

**Matthew Panzarino:** We're going to have these so that everybody can have a chance to kind of talk about where they are with the workflows or with the pipelines, how you're setting them up, you know, what they feel like.

**Matthew Panzarino:** I want to see, you know, kind of how it's going.

**Matthew Panzarino:** I it's going to be a process setting these up.

**Matthew Panzarino:** There is, there's some discrepancies that I've seen between what was ported over and what the latest article generation workflows were.

**Matthew Panzarino:** Some of them are, some of them are accurate, some of them have been ported over, the other ones, there seems to be a little bit of a mismatch.

**Matthew Panzarino:** So, on the agenda for you or on the docket for you should definitely be to immediately go through and check all of your artifacts, walk through, make sure that everything is...

**Matthew Panzarino:** This where it needs to be, and if not, update it.

**Matthew Panzarino:** The kind of gist of how I talk through the company contacts, user contacts, those fields, that stays the same.

**Matthew Panzarino:** So there's no changes there.

**Matthew Panzarino:** They still need to be fleshed out.

**Matthew Panzarino:** They still need to be fairly beefy and robust, so not to overuse the AI term.

**Matthew Panzarino:** The recording has stopped.

**Matthew Panzarino:** If you don't have enough density there, enough information, then the workforce will not produce good content.

**Matthew Panzarino:** They cannot produce it out of the ether.

**Matthew Panzarino:** If you give an LLM, like just a company name or something, it'll give you something.

**Matthew Panzarino:** But as we all know very well, it won't give you enough.

**Matthew Panzarino:** It won't give you an accurate or deep or precise piece.

**Matthew Panzarino:** So what I want to do is walk through all of those over the next couple of weeks.

**Matthew Panzarino:** And so you'll...

**Matthew Panzarino:** Getting some one-on-one invites from me about how to, or, and we can dive in on how to set up each of your workflows for your clients that you need to deliver for, because I don't want any delays there.

**Matthew Panzarino:** Outside of that, I'm here.

**Matthew Panzarino:** So never, like, suffer in silence about any of this.

**Matthew Panzarino:** If you're not getting it set up properly, if you're running into errors or issues, of course, if it's something that's clear, and you can define it, and you can document it, submit a linear ticket.

**Matthew Panzarino:** You know, you've got the link, Daniel pasted the link, or posted the link.

**Matthew Panzarino:** You can submit a linear ticket about a particular workflow, especially if it's erroring out, or you're missing something.

**Matthew Panzarino:** File those tickets.

**Matthew Panzarino:** Do review the tickets that have been filed.

**Matthew Panzarino:** There's a channel, there's a Slack channel for it, the EBD Slack channel, Help Slack channel, and then there's also, you can look at the linear filings on the linear homepage.

**Matthew Panzarino:** So double check.

**Matthew Panzarino:** Make sure that it isn't something that's already known, but file away, right?

**Matthew Panzarino:** Like this is a beta product that we are now beginning to test.

**Matthew Panzarino:** So make sure that you're filing those tickets.

**Matthew Panzarino:** Nobody's claiming it's perfect out of the gate.

**Matthew Panzarino:** So let's get that stuff noticed and notified immediately.

**Matthew Panzarino:** The same thing goes for you on a personal level.

**Matthew Panzarino:** If you're like struggling getting outputs or understanding how to set up your flow or anything like that, you know, reach out, dive in, start.

**Matthew Panzarino:** The good news is that like Daryl and Megan and I and Nana all kind of just went through an exercise on this.

**Matthew Panzarino:** It was with AIROPS, but it's the same principles.

**Matthew Panzarino:** So we can help you from a first principles perspective on setting up those fields.

**Matthew Panzarino:** But please, like, let me know immediately.

**Matthew Panzarino:** And if I can get to you immediately, I will.

**Matthew Panzarino:** If not, then we'll set up a call.

**Matthew Panzarino:** I'll have a lot of calls, obviously, and that's okay.

**Matthew Panzarino:** But the goal is to make sure that everybody is at least able to process articles through.

**Matthew Panzarino:** By the end of the week of their workflows, so that we can start delivering for clients next week, and some of you already still have to deliver for clients this week, so let's definitely lean in here and make sure that everybody is speaking up, you know, you're not alone, I'm here, we'll figure it out together, we'll figure out what's going on with the workflows, how to generate quality content, something that's within striking distance of editing, that you can get to the client and serve the work, so I am here.

**Matthew Panzarino:** That said, let's jump in, talk to me, and anybody can raise their hand, let's just do hand raises, make it easier, talk to me about anything that you've seen so far, anything that you need help with on setting up the workflows.

**Matthew Panzarino:** Everyone's perfect, nobody has any questions at all.

**Nika Narimanidze:** Oh yes, Jess, go ahead.

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** Thank you.

**Jess Scott:** Sorry.

**Matthew Panzarino:** I saw it.

**Matthew Panzarino:** Did somebody else want to speak up?

**Jess Scott:** No, I got it.

**Jess Scott:** Sorry.

**Jess Scott:** couldn't find the unmute.

**Matthew Panzarino:** I'm not used to Zoom.

**Matthew Panzarino:** I'm used to Google Meet.

**Jess Scott:** No, I'm just, like, full transparency jumping in, like, we've hit problems left and right, and I've flagged them.

**Jess Scott:** I just don't know, like, is Linear the best place to flag, like, might be a stupid question, but, or is there a, like, should we be leveraging a specific channel?

**Matthew Panzarino:** Like, because a lot of the things I've flagged so far have come back as, like, that's a bug.

**Matthew Panzarino:** We're working on it.

**Matthew Panzarino:** That's a bug, like.

**Matthew Panzarino:** Yeah.

**Jess Scott:** Yeah.

**Jess Scott:** Linear is the source of truth for bugs that have already been submitted.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** It doesn't mean that it isn't a bug that the EPD team has noticed and that they have noticed and are working on that may be not in that flow of, like, requests submitted by us, but it's a good place to visit.

**Matthew Panzarino:** If you look at the linear feed for the CPD tickets, you can look through them, stand through them, and see kind of various bugs and issues that have come up.

**Matthew Panzarino:** example, right?

**Matthew Panzarino:** You want at the Allez oun, this

**Matthew Panzarino:** The other questions that are more, like, process-related, like, where is this thing now, or things like that, just ask, and then we'll get to it.

**Matthew Panzarino:** Are there any ones that haven't been answered for you right now?

**Jess Scott:** No, as of right now, we've gotten quite a bit of clarity, but I think, like, the other half of my question being, like, so on the artifacts, does it matter, like, is there a format we need to maintain when we are editing them or updating them, or is it kind of just, like, because I noticed, like, one of my clients, the company context is, or, yeah, company AI context is wrong, it's pulled from an older draft, and so I don't, like, can I just delete and copy and paste, or is there a format it needs to mirror, are there any templates we can look for?

**Matthew Panzarino:** No, there's not a format, I mean, the only formatting you have to obey is that it's Markdown currently, right, and it will get updated, but Markdown is fairly straightforward, you know, I don't think it's a huge deal for that, but no, there isn't, so let me, appreciate it.

**Matthew Panzarino:** Me, what was I, I messed around with, hold on a second, uh, I'm gonna jump, open up something here to look at, oh, I remember now, I'm just gonna open up Git Pods, because Git Pod is one that is coming out of the sprint, and they, Marcel was, um, working on these artifacts, artifacts, and so I think they're, obviously, a way, a place to begin looking, um, so if you look at the artifacts here, um, the company context, so this is the rough, kind of, you know, outline that he has, right, company overview, elevator pitch, um, ideal customers, company characteristics, the primary verticals, the personas, uh, the jobs to be done analysis, core architectures, features, this is, you know, dense, it's, thing, Examples toys, reactions falou,

**Matthew Panzarino:** You know, not all encompassing, but it covers a large amount of information about the company.

**Matthew Panzarino:** And this is sort of what the dossiers should look like.

**Matthew Panzarino:** You can use this as a template if you want to start somewhere, okay?

**Matthew Panzarino:** And you can always speak from there.

**Matthew Panzarino:** It may not map one-to-one with all of your companies, like, okay, they don't really have this or this doesn't pertain, but you can at least get a start on what these should look like.

**Matthew Panzarino:** Even if you want to just seed something so you can start, like, whacking the generation button to see what happens, because you just need to use them, right?

**Matthew Panzarino:** It's not going to be perfect for your first time using any of them.

**Matthew Panzarino:** So if you need to seed something, just literally drop this into perplexity and say, hey, here's a template that I want you to use, but I want you to look at this company instead.

**Matthew Panzarino:** Give me something.

**Matthew Panzarino:** And then, of course, combine that with our hopefully detailed information that we have gathered at kickoff that lives in Notion or lives somewhere in your pod notes about this company.

**Matthew Panzarino:** And some of you have already done

**Matthew Panzarino:** I've this in Aerofs and therefore it has been ported over, but I'm just like noting that like if it didn't port over properly, like check everything, do not assume everything got copied over correctly.

**Matthew Panzarino:** It should, but double check it.

**Matthew Panzarino:** So double check to make sure everything got copied over.

**Matthew Panzarino:** If it is not as extensive or dense as this, fix it, like update it.

**Matthew Panzarino:** Priority one, right?

**Matthew Panzarino:** It needs to know in a detailed way what the company is we're trying to write content about, otherwise it'll get lost.

**Matthew Panzarino:** So that's the company context.

**Matthew Panzarino:** You can just look at Gitpod in here if you want to just at a glance, see what like the current state of the art on these artifacts are, according to Marcel.

**Matthew Panzarino:** The audience personas is a similar arrangement here.

**Matthew Panzarino:** So the audience persona is like an expanded version of like the customers, you know, that would be in the company context.

**Matthew Panzarino:** And it's like, you know, here's a little story about somebody named Alex and what their reality So

**Matthew Panzarino:** And what their fears are, and how you annoy them, what they really love, and like, he does this for each of this, so this is the Overwhelmed Platform Engineering Manager, this is the Paranoid CISO, Security Engineering Leader, you know, just these, this top three personas here, and then in the assignment creation, when you create assignments and do assignment generation, you can actually tell it which of the personas to target, you can just say, hey, I want to write this article for CISOs, right, for the Paranoid CISOs.

**Matthew Panzarino:** Please go at that, you know, and that would be in, when you're, when you're in your pipelines, and you're doing assignments, and you're creating an assignment, you've got, you know, your keyword, URL, that it'll stand for related keywords, and then your assignment direction, you can sort of like target, Paranoid CISO profiles, right, and it'll kind of aim it at that audience, to some degree.

**Matthew Panzarino:** We'll get more of this aiming, there's one.

**Matthew Panzarino:** That is in the works that will allow us to aim it at a, an article type.

**Matthew Panzarino:** So if you want a list, you want a comparo, you want a, you know, a guide, you know, right now, the way that the process works is it searches the keywords, sees what ranks for those keywords, and then picks the top performing format.

**Matthew Panzarino:** So you may be wanting a comparo and it's like the top performing format and this is listicles, right?

**Matthew Panzarino:** And boom, you get a listicle out, right?

**Jess Scott:** Like that's the way it works.

**Matthew Panzarino:** Now you can do that in the briefs.

**Matthew Panzarino:** can obviously change that, you know, and rewrite the brief to be a different kind of article and then go from there.

**Matthew Panzarino:** But it'd be so much nicer if that can, that's, it could be an exposed picker as an example.

**Matthew Panzarino:** So we can pick from like the five major formats.

**Jess Scott:** Can I ask one more question?

**Matthew Panzarino:** No.

**Matthew Panzarino:** Yes, of course.

**Jess Scott:** So, okay, this is actual in generation.

**Jess Scott:** How much direction are we meant to be putting in that like first little?

**Jess Scott:** So if you click like new?

**Jess Scott:** Yeah, like if you click add a new topic, assignment direction, how like you, you kind of said like point this at X persona, how much direction are we meant to be giving it because I started kind of like prompting away as if it was GPT and that seems to really, no, don't do that.

**Matthew Panzarino:** Yeah, it won't do that.

**Matthew Panzarino:** That's not productive for it.

**Matthew Panzarino:** Okay, right.

**Matthew Panzarino:** This, I think is extremely targeted towards personas at the moment, but I'm going to put an asterisk on that.

**Matthew Panzarino:** And I'll leave this as a note to follow up on, speaking to my note taker, because I do not know exactly how that's mapped.

**Matthew Panzarino:** I can go in to the pipeline and look at it and see, we've got the assignment.

**Matthew Panzarino:** Yeah, I won't do it live on this call, but I'll go ask and see where that's the, where the assignment direction is mapped.

**Matthew Panzarino:** It's a rich text.

**Matthew Panzarino:** String, and then I don't know what pulls it.

**Matthew Panzarino:** So I'll have to go look.

**Jess Scott:** Okay, because in the examples I saw, it was like just a sentence or two.

**Matthew Panzarino:** Yeah, at the moment.

**Matthew Panzarino:** So the editor, just so you know, like the editor, the rich text editor that we will have to like edit, like briefs or drafts or things like that, it will also have an AI context window that will allow you to say, can you update this?

**Jess Scott:** Oh, how far is that?

**Matthew Panzarino:** Like what you're doing in ChatDVT right now, where you're pasting the article in and you're saying, hey, can I do this, right?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** It'll do that.

**Matthew Panzarino:** It'll be, I think, a sonnet window, right?

**Matthew Panzarino:** So basically, it'll allow you to edit, do the, you know, the feedback?

**Jess Scott:** Mm-hmm.

**Matthew Panzarino:** I know somebody was asking, where's feedback?

**Matthew Panzarino:** Well, that's what, you know, it's going to be a better version of it.

**Matthew Panzarino:** Instead of just, oh, do these things with this weird slash formatting and all that.

**Jess Scott:** Yeah.

**Matthew Panzarino:** So, A, it's bad.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** It's more, it's more natural for us to edit that way.

**Matthew Panzarino:** And we are, all used to it because we use LLMs.

**Matthew Panzarino:** Right.

**Matthew Panzarino:** We need to capture that.

**Matthew Panzarino:** Like we need to understand what you're typing in there, right?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Typing in a chattypt is going right out of our ecosystem and we have no idea.

**Matthew Panzarino:** So if you're typing the same instructions 50 times, we should learn from that.

**Jess Scott:** Right.

**Matthew Panzarino:** We should, we should be better about it.

**Matthew Panzarino:** And we should like correct that so that you don't have to type it 50 times.

**Matthew Panzarino:** And nor should it be something you manually have to say, oh, I've typed this 50 times today.

**Matthew Panzarino:** Can you please fix this?

**Matthew Panzarino:** Right?

**Matthew Panzarino:** So it needs to be in the loop.

**Matthew Panzarino:** So when did that happen?

**Jess Scott:** What's the timeline on that?

**Matthew Panzarino:** This, this week, theoretically.

**Jess Scott:** okay.

**Matthew Panzarino:** Dope.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** I'm not making any promises.

**Matthew Panzarino:** That's hinge.

**Matthew Panzarino:** But if they said it's coming very soon, it could be today or tomorrow, even so.

**Jess Scott:** Okay, cool.

**Jess Scott:** That's all my questions.

**Jess Scott:** Sorry, everybody.

**Jess Scott:** It just took up a lot of time.

**Matthew Panzarino:** No problem.

**Matthew Panzarino:** Anybody else?

**Matthew Panzarino:** Please raise your hand.

**Matthew Panzarino:** Let's talk.

**Ademilade Shodipe-Dosunmu:** Um.

**Ademilade Shodipe-Dosunmu:** So, I have a question about, like, bugs.

**Ademilade Shodipe-Dosunmu:** So, like, if I run into, like, a bug that has only happened, like, once, is that still worth reporting?

**Ademilade Shodipe-Dosunmu:** But I ran into one today on, like, the refresher flow for Firework, where the step was taking, like, 30 minutes to start.

**Ademilade Shodipe-Dosunmu:** Not to run, to start, like, it was rolling starting for, like, 30 minutes plus, which isn't normal.

**Ademilade Shodipe-Dosunmu:** And I looked at it, but it only happened, like, once today.

**Ademilade Shodipe-Dosunmu:** So, I didn't know if, I mean, I reported it anyways, but I just wanted to know whether it makes sense to report stuff that happens, like, rarely.

**Ademilade Shodipe-Dosunmu:** I don't know if it's happening again.

**Ademilade Shodipe-Dosunmu:** I'm still doing, like, more refreshes.

**Ademilade Shodipe-Dosunmu:** But, you know.

**Matthew Panzarino:** Yeah, if it's not duplicatable, if you can't do it more than once, like, if you can't do it again and it happens again, I would say wash it at this point.

**Matthew Panzarino:** Because we want high-priority blockers to be, like, the things that they tackle.

**Matthew Panzarino:** And so, it just creates a little bit of noise for them now.

**Matthew Panzarino:** They can prioritize, and they will prioritize on their end.

**Matthew Panzarino:** know, we blow tickets into their system, and then they're going to stack.

**Matthew Panzarino:** They're going to rank them according to what they think is urgent and what they can fix.

**Matthew Panzarino:** So I would say, don't be too reluctant to share, do it, like share, but maybe let's make the marker like, if it happens more than once, you know, flag it.

**Matthew Panzarino:** If it happens just once, it's very likely, and you can look into the logs, right, to the generation pipeline and see what's happening.

**Matthew Panzarino:** And if you look in there, and it'll show you what's running, and it'll show you the errors.

**Matthew Panzarino:** And if you look in there, and you see like a 500 error, or something that's obviously a rate limit error, it's most likely just a rate limit.

**Matthew Panzarino:** Like right now, we're having big rate limit issues, because we're like running a ton of things at once, there's a big backlog.

**Matthew Panzarino:** So I would say nine times out of 10, it's probably either rate limit, or if it doesn't error out right away, if it errors out right away, it's most likely input, right, like something we did, we sent into the system that it didn't like, that it didn't want.

**Matthew Panzarino:** So check that and see what it says.

**Matthew Panzarino:** If it's improper formatting, it's usually like escaped text, where it's

**Matthew Panzarino:** You know, out of the bracket or out of markdown formatting that it expects, and that's why it's error, if it takes like 30 minutes to even start something, my advice is like, your range should really be like seven minutes, like if it takes more than seven minutes, like cancel that, delete it, start a new one, move on with your life, right, because there's something going on there, when it eventually fails out, you can go back to it, right, but the pipeline right now is supposed to take between three and eight minutes, eight so, to run like each step, they're, they're speeding that up every day, there's new things that they're speeding up, there's an XML generation that they're deleting, that doesn't need to happen, that's taking like an extra minute and a half, so like they're, they will tweak this over time to be faster, but if it should not take more than like five or six minutes, seven minutes, now if it takes a little longer than that, you know, don't shoot me, it is what it is at this point, but it definitely shouldn't take 30, so if you run into that again, again, I would say document,

**Matthew Panzarino:** You can link the workflow, obviously, in the ticket, link the workflow you were running, even maybe the step you were running, and if it throws an error, then log the error as well, and then send that over.

**Matthew Panzarino:** But yeah, be aggressive about reporting, but not frivolous about reporting.

**Matthew Panzarino:** Just balance between the two.

**Matthew Panzarino:** But I'd say if it happens, again, do it.

**Matthew Panzarino:** Submit it.

**Matthew Panzarino:** We want to know.

**Matthew Panzarino:** You are our first line of defense.

**Matthew Panzarino:** There's nobody else using this platform at the moment.

**Matthew Panzarino:** Eventually, users will be using it, and I'm sure we'll get bug reports constantly.

**Matthew Panzarino:** But right now, you're it.

**Ademilade Shodipe-Dosunmu:** Okay, thank you.

**Matthew Panzarino:** Yeah, yeah.

**Mariana Marins:** Yes, Nika.

**Mariana Marins:** Matthew, just a second.

**Mariana Marins:** We have a question from Jan on the chat.

**Mariana Marins:** Oh, sorry.

**Mariana Marins:** I don't have my chat window open.

**Mariana Marins:** I apologize.

**Mariana Marins:** I'm going to read for you.

**Mariana Marins:** So, confirming that modifying brief or outline is a bug, so we can't currently do this.

**Matthew Panzarino:** No.

**Matthew Panzarino:** Wait.

**Matthew Panzarino:** Modifying brief or outline is a bug?

**Matthew Panzarino:** What do you mean by that?

**Matthew Panzarino:** Like, you can't edit your brief?

**Mariana Marins:** Yeah.

**Mariana Marins:** should be able to edit, Jen.

**Jess Scott:** I just flagged this with Kirkland.

**Jess Scott:** Right now, he's saying there's a bug where we can't edit outlines or the assignment brief.

**Jess Scott:** I flagged it, but I don't know.

**Jess Scott:** Do I need to drop it in linear?

**Matthew Panzarino:** I flagged it.

**Matthew Panzarino:** Let me look at it.

**Matthew Panzarino:** Let me look at it real quick.

**Matthew Panzarino:** So, which one would you, which one do you run issues into, Liz?

**Matthew Panzarino:** Jess?

**Jess Scott:** Show me.

**Jess Scott:** Here, I can share.

**Matthew Panzarino:** I'll share my No, don't show me.

**Matthew Panzarino:** I'm going to go look at it.

**Jess Scott:** So, just tell me.

**Jess Scott:** oh.

**Jess Scott:** Okay.

**Matthew Panzarino:** Can I just drop you the link?

**Matthew Panzarino:** Yeah, yeah, yeah.

**Jess Scott:** Wherever.

**Jess Scott:** Okay.

**Jess Scott:** Let me grab it.

**Jess Scott:** So, this is one that's already done, because I couldn't get generation going on any of the other ones.

**Jess Scott:** So, this is one that someone at GrowthX started, and I just tried to edit the outline to see if I could tweak it, and there's no outline output.

**Jess Scott:** Okay.

**Jess Scott:** So, you gave the inputs of the context and the research.

**Matthew Panzarino:** care.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** I was Bye.

**Matthew Panzarino:** Do you have any questions?

**Matthew Panzarino:** And then when you generated it, it said, cool, I generated it.

**Jess Scott:** And then you go to output and there's nothing there.

**Jess Scott:** So I essentially was, I went, so this whole article was generated by someone in dev.

**Jess Scott:** And then I went to just try and mess around with the outline piece.

**Jess Scott:** And you can see there's input, but there's no output for me to like, try and adjust an outline.

**Jess Scott:** I put it in the general Slack channel and Kirkland said that it's a bug they're working on fixing.

**Matthew Panzarino:** Okay, got it.

**Matthew Panzarino:** Well, cool.

**Matthew Panzarino:** If he's aware of it and it's a bug, it's probably a bug.

**Matthew Panzarino:** But you can edit those.

**Matthew Panzarino:** There's no reason you can't.

**Matthew Panzarino:** So if they're there, you should be able to edit them.

**Jess Scott:** Yeah, but can you see one?

**Jess Scott:** Like if you click that outline stage and then output.

**Jess Scott:** No, no, no, you're right.

**Jess Scott:** That's blank.

**Matthew Panzarino:** Oh, okay.

**Jess Scott:** But I think that's an error in the output.

**Jess Scott:** Not an, there's not, it's not an editing error.

**Jess Scott:** It's the output isn't there.

**Matthew Panzarino:** Yeah, yeah, Like it's messed up.

**Jess Scott:** Cool.

**Matthew Panzarino:** But yeah, if you, if you go into a pipeline and you look at article generation, go to something like brief and output, um, you should be able to edit it right.

**Matthew Panzarino:** That window, though, the reason that it's not there is because something broke, right, but the editing function of it is not broken, right, like you can edit all you want if it's actually there, right, like this is the output of a assignment brief in.

**Jess Scott:** Yeah, okay, so yeah, I've not seen that yet, okay, cool.

**Jess Scott:** exactly, exactly, so it's not like, oh, I can't edit this, it's, no, it's not there to edit.

**Jess Scott:** Okay.

**Jess Scott:** You can probably just type it manually in there.

**Jess Scott:** Well, I can't, wouldn't even, yeah, it's a whole thing, okay, cool.

**Matthew Panzarino:** Yeah, okay, well, I will get these other chat ones, but Nika, you, you had your hand up?

**Nika Narimanidze:** Yeah, hi, Matthew, hi, hi, LCMs.

**Nika Narimanidze:** Just wanted to share, Matthew, that I found that on Atlas, data grid space is missing.

**Nika Narimanidze:** I reported this, not big deal, but should, like, the primary assignee be someone from the strategy team, like sprint team, or should it be EPD?

**Nika Narimanidze:** Just wanted to make sure that it's a direct address.

**Matthew Panzarino:** The data grid one is missing?

**Nika Narimanidze:** JAREDA DataGrid, yes.

**Matthew Panzarino:** And the question about it, well, I mean, first of all, okay, that's priority one, that's P0, right?

**Matthew Panzarino:** We need it to exist.

**Matthew Panzarino:** So you told us, who'd you tell us?

**Nika Narimanidze:** I just created the ticket on linear.

**Matthew Panzarino:** JAREDA Okay, yeah.

**Nika Narimanidze:** We should probably raise a little bit more of a angsty notice about that.

**Matthew Panzarino:** So finally, the ticket's great.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** I appreciate it.

**Matthew Panzarino:** But an entire client space missing is a huge deal, right?

**Matthew Panzarino:** JAREDA we start messing with it, right?

**Matthew Panzarino:** So yeah, I'll flag that right after this call to make sure that we, could you note that for me?

**Matthew Panzarino:** And then I'll hop on that to make sure that it's there.

**Matthew Panzarino:** I can create a lot of stuff, and I can create spaces for these, but I just want to make sure that they do it, they know what's going on in case we have any other issues.

**Matthew Panzarino:** So I could create this for you, but I think it is worth telling them and having them look at what happened there.

**Matthew Panzarino:** GARCIA, Yeah, obviously.

**Matthew Panzarino:** Yeah, actually, Daniel mentioned that there was a couple that they were still getting around to, and Adventurers Group is one he mentioned, Mariana.

**Matthew Panzarino:** I don't remember him mentioning DataGrid, but it could be in the same bucket.

**Matthew Panzarino:** So they could just be getting around to that.

**Nika Narimanidze:** Okay.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** But it's good to flag, and I'll follow up on it to make sure that we get those in.

**Nika Narimanidze:** Because you need to start working on them, right?

**Nika Narimanidze:** You need to start polishing them.

**Nika Narimanidze:** You can't do that if they're not there.

**Nika Narimanidze:** I get Dude, I appreciate that.

**Nika Narimanidze:** Thanks a lot.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Let's see.

**Matthew Panzarino:** Let's see.

**Matthew Panzarino:** Yeah, even with no outline output, I plugged in my own and it still failed.

**Matthew Panzarino:** Okay, that's fine, Yeah, and that's on, that was, which one again?

**Jenn Peters:** For me, it's currently Dimmel is the one.

**Jenn Peters:** So, I kind of just assumed it was me putting it in the wrong format.

**Jenn Peters:** So, I didn't have the same issue as Jess.

**Jenn Peters:** Mine actually did have an output in mine.

**Jenn Peters:** But, yeah, like the format.

**Matthew Panzarino:** So, I guess it's a fun thing.

**Matthew Panzarino:** Yeah, Dimmel has this weird one, right?

**Matthew Panzarino:** Where they're specifically all competitive review art.

**Matthew Panzarino:** Sure.

**Matthew Panzarino:** Yeah.

**Jenn Peters:** Sure.

**Jenn Peters:** Yeah, for this batch.

**Jenn Peters:** We're currently in backlog, so yeah, for this batch, for sure.

**Jenn Peters:** But yeah, it sounds like it's like everybody's experiencing it.

**Jenn Peters:** So I thought it was me like formatting it wrong or whatever.

**Matthew Panzarino:** So I just was like, you know, making sure it was right.

**Matthew Panzarino:** But I think it's a bigger fish.

**Matthew Panzarino:** Yeah, I'll follow up on that for sure, because if the output's blank, then yeah, that's not, no bueno.

**Matthew Panzarino:** So there's obviously some sort of bug there.

**Matthew Panzarino:** So that's great to know.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** And this is the exact kind of stuff, like, if you file the ticket, wonderful.

**Matthew Panzarino:** But, you know, feel free to let me know as well, because I'm trying to keep a really close read on this.

**Matthew Panzarino:** Ultimately, I'm responsible for helping you get your job done.

**Matthew Panzarino:** And if I fail at that, you know, I'm gone.

**Matthew Panzarino:** So I'm here to help.

**Matthew Panzarino:** The idea that we have the outline and it's blank would say to me that there's something broken either in the inputs not being mapped or in the generation of flow itself.

**Matthew Panzarino:** But we'll...

**Matthew Panzarino:** Well, I'll log in the studio and check that out myself, but I'll still get with Kirkland and see where he's at with it, since he's already aware of it.

**Matthew Panzarino:** I'll take it out right off his call.

**Rachel Pasche:** I have a quick thing I just want to flag.

**Rachel Pasche:** I submitted a ticket for it.

**Rachel Pasche:** One of my workspaces was set up as the wrong company, which is something to be aware of if anybody's getting, like, funky results, because I couldn't figure out why my things were coming through completely wrong.

**Rachel Pasche:** And then I went in and I looked at, like, all the instructions, and I was like, this is not supposed to be an email marketing campaign.

**Rachel Pasche:** It's supposed to be, you know, a dentist hiring platform.

**Rachel Pasche:** Yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** No, that's I did submit a ticket for it, but I just wanted to kind of flag it in case anybody else notices that their stuff is completely incorrect.

**Matthew Panzarino:** The ticket filing part of that is, like, just, like, that's service to the devs so that they can understand if the reporting process went wrong.

**Matthew Panzarino:** The action on it would just be, like, delete all that and rewrite it, right?

**Matthew Panzarino:** Like, or report it over, paste it back in from there.

**Matthew Panzarino:** I'm sure you already have.

**Rachel Pasche:** I'm already

**Rachel Pasche:** Can I, yeah, I took everything out, and I've been putting stuff back in.

**Rachel Pasche:** The one thing I wasn't sure about was the writing instructions, like for tone and voice and stuff.

**Rachel Pasche:** I couldn't figure out where that was in Atlas, and maybe that's just, like, having a hard time.

**Matthew Panzarino:** Yeah, let's take a look at it really quickly, and I'll show you where it should be, right?

**Matthew Panzarino:** And then if it's not there, then we'll, that's a different story, right?

**Matthew Panzarino:** So if you go, what company was it?

**Rachel Pasche:** Hero.

**Matthew Panzarino:** I'm sorry, what?

**Rachel Pasche:** Hero, T-E-R-O.

**Rachel Pasche:** T-E-O.

**Matthew Panzarino:** I'm sorry, it's, the T was a little soft.

**Rachel Pasche:** I was looking for hero, I'm like.

**Matthew Panzarino:** On a call, my brain doesn't map to, like, customer names and stuff.

**Matthew Panzarino:** Okay, so you've got your context artifacts here.

**Rachel Pasche:** Yeah, I've done that one.

**Matthew Panzarino:** I haven't done the other two yet.

**Matthew Panzarino:** Yeah, company context and writing guidelines, right?

**Matthew Panzarino:** So these are the three that you need to update.

**Matthew Panzarino:** And yes, it looks like superhumans got ported into T-E-O, so obviously, no bueno.

**Matthew Panzarino:** So we can, we can.

**Matthew Panzarino:** Edit this, delete this, and rewrite it.

**Matthew Panzarino:** This says extracted from pipeline, great, but it extracted it from the wrong pipeline, right?

**Matthew Panzarino:** So that's a place to begin.

**Matthew Panzarino:** Rewriting this is P0 for you.

**Matthew Panzarino:** Obviously, you're not going be able to get any work done until you get these updated properly.

**Matthew Panzarino:** I'm happy to help.

**Matthew Panzarino:** And that's what these one-on-one calls are for, like diving into each individual person's one.

**Matthew Panzarino:** But don't wait for me.

**Matthew Panzarino:** Like, you can start on this for sure.

**Matthew Panzarino:** As a default, like as a basic, you can grab the company context from your Notion, from the T.R.O.

**Rachel Pasche:** Notion.

**Rachel Pasche:** Yeah.

**Matthew Panzarino:** I took some of it from Notion.

**Rachel Pasche:** I didn't know if it was, like, not fleshed out enough because it was – they're, like, an early-days customer, so their Notion board is, like, a lot more sparse than – It might be.

**Matthew Panzarino:** Yeah, it's true.

**Rachel Pasche:** Some of the more recent ones, so I didn't know if that was a problem or if I should just kind of work with what I have.

**Matthew Panzarino:** Yeah, let's look at – let's just look at what was in Aerofs really quickly.

**Matthew Panzarino:** you.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** So, if we go into the article generation, and then, um, brain guidelines, company about, uh, Aerofs is a fantastic company that has no HOS experience.

**Matthew Panzarino:** Uh, okay.

**Matthew Panzarino:** I mean, here's a place to begin.

**Matthew Panzarino:** So, you can take this right from Aerofs.

**Matthew Panzarino:** Do you not have access to Aerofs anymore?

**Rachel Pasche:** No.

**Matthew Panzarino:** Well, I'm going to paste this right into your Slack.

**Rachel Pasche:** Oh, cool.

**Rachel Pasche:** Thank you.

**Matthew Panzarino:** And then, you can grab it from there.

**Matthew Panzarino:** So, at least you have something to begin with.

**Matthew Panzarino:** I'm not saying this is good.

**Matthew Panzarino:** I haven't even read it.

**Matthew Panzarino:** But, but it's something to begin with.

**Rachel Pasche:** Uh, you can start there.

**Rachel Pasche:** Okay, cool.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Yeah, of course.

**Matthew Panzarino:** And then, uh, what was the other one?

**Matthew Panzarino:** Oh, the writing instructions.

**Matthew Panzarino:** Um, I actually don't even know if Tiro had, cause some of them didn't, didn't really.

**Matthew Panzarino:** Yeah, like, brand guidelines is the closest to it.

**Matthew Panzarino:** But this is not, this really should be a part of those.

**Matthew Panzarino:** company context, but let me, I don't think this had, yeah, that's, wait, hold on, it might be, sometimes it's at the end, in some of the workflows, yeah, yeah, no, post-processing, wait, what's the post-processing calling, let me look, nope, that's not what I want, uh, brand guidelines is calling, yeah, so this doesn't even call, like, it would be a miracle if this turned out good work, to be honest, um, this doesn't even call writing guidelines, so, because there is none in this grid, that's why we created the, like, ideal grids, because, but, anyhow, this, this one here, this has, oh, here, good, I actually made one for this one, okay, hold on, um, here's the, here's the writing instructions, let's just start, let's start here, I don't know if these are good, I didn't write these, um, this is too short, I can already tell, but it's something to begin with.

**Matthew Panzarino:** So I'll just paste this for you as well.

**Matthew Panzarino:** Um, and we'll, we'll revamp from there.

**Matthew Panzarino:** Oh shoot, I think it, did it do it?

**Matthew Panzarino:** Was that the right one?

**Matthew Panzarino:** Yeah, that's the voice in tone.

**Matthew Panzarino:** Yeah, start there.

**Matthew Panzarino:** So.

**Rachel Pasche:** Okay.

**Matthew Panzarino:** Start with those and we'll go from there.

**Matthew Panzarino:** So that's where they live and that's what to put in there to start.

**Matthew Panzarino:** Um, okay.

**Matthew Panzarino:** yeah, Saskia.

**Matthew Panzarino:** but she's already gone by Saskia.

**Matthew Panzarino:** uh, Jess, and then Mariana, we'll get to that.

**Jess Scott:** Uh, just, sorry, quickly.

**Jess Scott:** Um, I obviously, Interwell, still have clients I'm generating for this week.

**Matthew Panzarino:** Mm-hmm.

**Jess Scott:** How long will we have, like, how long are we able to access Aerofs?

**Jess Scott:** Because it's probably faster for us to make sure we're getting those deliverables to them using Aerofs still while we learn.

**Jess Scott:** Aerofs can be shut off any second.

**Jess Scott:** Okay.

**Matthew Panzarino:** Our deadline was yesterday.

**Matthew Panzarino:** So the fact that I still have access to it is like.

**Jess Scott:** Yeah.

**Jess Scott:** still have access to it.

**Matthew Panzarino:** Their ops team sucks.

**Matthew Panzarino:** I don't know.

**Matthew Panzarino:** I don't know what to tell you.

**Jess Scott:** Okay.

**Matthew Panzarino:** So, I would say use it.

**Matthew Panzarino:** You can use it if you want, but in all honesty, like, if something is broken, literally broken, that's fine.

**Matthew Panzarino:** But otherwise, this is the same thing behind the scenes, right?

**Matthew Panzarino:** It's just a different interface for it.

**Matthew Panzarino:** So, if it's not broken, it's going to give you the exact same results as you would be getting in AirOps.

**Matthew Panzarino:** So, try and do your darndest to use Atlas.

**Matthew Panzarino:** And then if you need to, like, generate a handful while you have access, okay, I'll pretend not to see.

**Jess Scott:** Okay.

**Jess Scott:** Okay, cool.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Timmy, yeah.

**Oluwatimilehin Ademosu:** Hi, Panzer.

**Matthew Panzarino:** Yeah.

**Oluwatimilehin Ademosu:** Thanks for the demo.

**Oluwatimilehin Ademosu:** So, this isn't about the workflows.

**Oluwatimilehin Ademosu:** I just wanted to ask about the rationale behind the recent port changes and the scenes that were just moved around.

**Oluwatimilehin Ademosu:** So, this would be there.

**Matthew Panzarino:** Thank

**Matthew Panzarino:** So just some of these thought processes I went into those.

**Matthew Panzarino:** Andy is the keeper of the keys to that.

**Matthew Panzarino:** She spent a lot of time working on this and kind of like moving things around.

**Matthew Panzarino:** There was a lot of versions of this.

**Matthew Panzarino:** I can't speak to everything.

**Matthew Panzarino:** So you should probably ask her.

**Andi Bailey:** I'm here, Panzer.

**Matthew Panzarino:** I need to learn Atlas too.

**Andi Bailey:** Hi.

**Andi Bailey:** I was just going to say, Andy, that like the general rationale is we need to mix competencies.

**Matthew Panzarino:** You know, people that were aligned with like the technical SEO aspects, the workings of our workflows, and then the subject matter.

**Matthew Panzarino:** it was a very complex task.

**Matthew Panzarino:** You know, I didn't want to like speak out of turn or talk about a lot of the ways that you kind of went through this.

**Andi Bailey:** Yeah.

**Andi Bailey:** So if you guys think about when you onboarded and your onboarding classes were probably like 10 plus people, trainings were sort of do it when you can, read the circle docs.

**Andi Bailey:** And some people got more training or have been here for longer and had a chance to figure things out.

**Andi Bailey:** A little bit more.

**Andi Bailey:** And so obviously with that, we also have people with different levels of experience on the technical side and the editorial side.

**Andi Bailey:** With that, the way that we organize pods, because we had so many people joining at once and we didn't yet have, like Panzer's put together now, like a really clear way to establish where people's competencies and strengths are, we didn't have that yet when people joined pods.

**Andi Bailey:** So we kind of had mixed pods of more technical clients with people that had more editorial knowledge and vice versa, like more editorial clients with people who were like really SEO experts.

**Andi Bailey:** The goal now is to try and mix those skill sets, just as Panzer said.

**Andi Bailey:** So people with editorial skills and who have a little bit more experience and have seen some client success, so know what good really looks like.

**Andi Bailey:** And then people who might have seen some struggling clients didn't feel like they got enough help.

**Andi Bailey:** As they got scaled up, so that, hopefully, everybody can cover for each other, teach each other their strengths and skill sets.

**Andi Bailey:** So I know that it feels like a punishment when you get pulled from a pod where you've, like, made really strong relationships and you might be really close with your clients.

**Andi Bailey:** But the goal here, we've seen so much change, is to try and create stable teams that can, no matter what the client needs, there's somebody on that team who can step up and help them.

**Andi Bailey:** And that will lead to, I mean, you've seen that we've had some churn from clients in the last two months.

**Andi Bailey:** I think we've had, like, six clients churn.

**Andi Bailey:** And that's because not everybody here got the right level of training, and so we weren't able to support the clients.

**Andi Bailey:** that now, and give everybody who is getting up to speed on some of the areas where they didn't get enough training, the help from teams.

**Andi Bailey:** Members who have had that training and can share their knowledge and do a little bit of teaching on the fly, too.

**Andi Bailey:** So if you've had success, unfortunately, it probably means that we want to put you with other team members who need a little bit more help and vice versa.

**Andi Bailey:** So if you've been struggling, hopefully you'll be put with somebody who can help you learn more and leverage these workflows more effectively.

**Andi Bailey:** And the goal is to create some stability.

**Andi Bailey:** I know that there's like six changes that happened all at once, and it is probably not helpful for confidence, but that was the reasoning behind why we did this.

**Matthew Panzarino:** Thanks, Adi.

**Matthew Panzarino:** Maria, let's see.

**Matthew Panzarino:** I went client in a bit, the last one I was from Generation 4.

**Matthew Panzarino:** Yeah, yeah, we, our transition period is as long as Aerox leaves.

**Matthew Panzarino:** the door open.

**Matthew Panzarino:** So, whatever you gotta do, like, generate your keyster off, and, you know, whatever you have available to you, use the tools to get the client work out, but really, really, really aggressively try and transition to Atlas, because it literally, you could be right in the middle of working with your apps, and it would go away.

**Matthew Panzarino:** So there's no guarantee it'll be there at any point.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** Well, there's no, like I said, there's no guarantee that any of those windows will happen.

**Matthew Panzarino:** I don't know why some people have access and some don't, they may be shutting them down in waves, you know, um, our license may be reduced, something like that, I have no idea.

**Matthew Panzarino:** If there's any information you need out of there, let me know.

**Matthew Panzarino:** Other than that, um, we can get together and figure out a game plan if you are unable to generate any articles right now, um, then we'll go from there.

**Matthew Panzarino:** Uh, Matt, yeah?

**Matthew Alves-Hill:** Yeah, I was just gonna say, on using Aerobs, I don't know if it's related, or it's just my grid, but,

**Matthew Alves-Hill:** I actually tried to run a VAPI article through Aerofs earlier, and I was getting, like, random errors that seemed like bugs.

**Matthew Alves-Hill:** It was telling me it couldn't find, like, certain fields.

**Matthew Alves-Hill:** So I don't know if that's part of, like, the decommissioning or whatever, but people might find that it's not going to work anyway.

**Matthew Panzarino:** Yeah, yeah, fair point, Matt.

**Matthew Panzarino:** And I would treat it as, like, deprecated, right?

**Matthew Panzarino:** So it's no longer going to be supported.

**Matthew Panzarino:** If you run into any errors, you're on your own.

**Matthew Panzarino:** And they could be changing endpoints.

**Matthew Panzarino:** They could be shutting down old endpoints that were being called by Aerofs, or they may be called differently.

**Matthew Panzarino:** So when I say it's the same backend system, that doesn't mean it's the same exact endpoints or the same deployments that Atlas is running off of that Aerofs was accessing.

**Oluwatimilehin Ademosu:** And so if those are being deprecated or shut down, it's very possible the Aerofs flows could not work at all.

**Matthew Panzarino:** So, but, yeah, Marina, about the...

**Matthew Panzarino:** of the...

**Matthew Panzarino:** So, Let's Let's Thank you.

**Matthew Panzarino:** About the getting your stuff out, like that's kind of what these, there are two avenues for you on that, like one, like the one-on-one trying to schedule a couple a day, I can't do more than about two a day, but we'll try and crank through everybody as much as we can, try and get through all your CMs, because I want to talk to you about what you need to, what you need to get set up and operating properly, and if you need ad hoc help, like reach out.

**Matthew Panzarino:** The other avenue is just tell me, right, here is great, but if you are unable to set up your workflows properly, hit up Nana, and we'll try and fit you in, and get you set up, so that you can actually start generating, because we don't want anybody to have any blockers.

**Matthew Panzarino:** I'm here, and that's, you know, that's what I'm here for, so we'll figure it out, figure it out together, even if I have to manually write your article, psych, I'm not going to do that, just kidding.

**Matthew Panzarino:** Anybody else have any questions at this point?

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Okay, this is not the end, we'll see each other again tomorrow, and I'll see some of you in between.

**Matthew Panzarino:** In between now and then, your only homework, of course, you have plenty to do, but your only homework for the next meeting is just collate questions.

**Matthew Panzarino:** You know, come with anything that you have, any pain points, any blockers, anything.

**Matthew Panzarino:** You're not alone, you're not out there, in a silo, trying to figure this thing out, we're all here together, I'll help you.

**Matthew Panzarino:** Sweet.

**Matthew Panzarino:** Thanks, folks.

**Andi Bailey:** Spencer, I don't even know where to start on this, so if you would start, like, can we just stay on, and you give me, like, an end-to-end?

**Matthew Panzarino:** Yeah, of course.

**Andi Bailey:** I do want to know how to do it.

**Matthew Panzarino:** Anybody can stay on if they want, do you want me to just kind of, like, walk you through the way that the thing is?

**Matthew Panzarino:** Yeah, like, how do we build one of these from start to finish?

**Andi Bailey:** Yeah, I know.

**Matthew Panzarino:** He said actually record this, and as I was mentioning in the chat, like, I am not actually confident enough to record a full tutorial, but I can walk through a little bit, just kind of jump through the workspace.

**Matthew Panzarino:** Anybody that wants to leave can leave, and I am not offended in any way, but I'm happy to just kind of poke around a little bit and show you what's going on here.

**Mariana Marins:** I want to just point one thing, Matthew, and to all of you guys, the ideal path that Matthew created in AirOps, even though we don't have the same fields, etc., I think you guys should focus more on the mindset of it, of this is what we should do with the tools that you have right now, with the fields that you have right now, then on the actual little names of things, and so on and so forth.

**Mariana Marins:** Especially because one thing that was said in the past, and I think many of you guys took too hard, and you shouldn't, is the length of the

**Mariana Marins:** So, that you are going to give to the tool.

**Mariana Marins:** In the past, it was said that it should be short, but we have come to the conclusion that it shouldn't, for example.

**Mariana Marins:** So, if you guys want to go back to the video that Matthew recorded about the flow in AirOps, I think it's going to help a lot in Atlas as well.

**Matthew Panzarino:** Yeah, that's a good point.

**Matthew Panzarino:** So, there's two resources that I think you should bookmark and, like, have at a moment to reference.

**Matthew Panzarino:** So, one, and I promise I'm not just advertising for myself, is that AirOps training that I had recorded, because it does show you kind of the depth and breadth of what each of those builds should contain.

**Matthew Panzarino:** If you don't have enough of that in there, it will never give you good results.

**Matthew Panzarino:** And I think that 70% of the time that I was having people dive in and say, like, oh, we haven't been generating anything in the AirOps because it sucks, I looked at their workflows, and for better,

**Matthew Panzarino:** Whether this was true, whether this would have fixed the issue or not, those fields, the company context, the AI context, or really the assignment context, the personas, they were all extremely short and very low detail.

**Matthew Panzarino:** And I think that's a huge problem because you're just not giving it enough context to put any rails in place.

**Matthew Panzarino:** Because at the back end, it has a bunch of rails that Daniel and his team have created, but you have to give it information for it to build those rails up and have it have some sort of directionality to the writing.

**Matthew Panzarino:** And I think there absolutely has been a moment in the past where that window, whether it was because of context window or API rate limits or whatever, was much shallower.

**Matthew Panzarino:** And so you literally had to put less text in those fields or it became an issue and the workforce would fail out.

**Matthew Panzarino:** Or it would stop reading the context, or whatever the case may be.

**Matthew Panzarino:** It still can't be books and books.

**Matthew Panzarino:** You can't put in 10,000 words in there.

**Matthew Panzarino:** It's not going to result in anything great.

**Matthew Panzarino:** But it can be a pretty strong outline of information about the company.

**Matthew Panzarino:** And it can go a little deeper than you would think.

**Matthew Panzarino:** And the writing guidelines is the same thing.

**Matthew Panzarino:** They can be really detailed.

**Matthew Panzarino:** You can get pretty aggressive about telling it the exact ways you want to write about the company.

**Matthew Panzarino:** And you can do, on average right now, this is just current state of the art.

**Matthew Panzarino:** I have to preface this by saying that we will always be pushing it.

**Matthew Panzarino:** But current state of the art, you can give it roughly 20 solid instructions about how to write about a company.

**Matthew Panzarino:** And it will take them all.

**Matthew Panzarino:** And it will generally do a pretty decent job.

**Matthew Panzarino:** And what it doesn't do, what it misses, you can then take care of in the edit phase, right?

**Matthew Panzarino:** But you need to have that filled out.

**Matthew Panzarino:** So check that recording.

**Matthew Panzarino:** The second thing is the training that Daniel did yesterday.

**Matthew Panzarino:** I've referenced it about six or seven times myself in just learning, so I just literally leave it open in a tab, and then I scrub it back and forth, but I'm like, wait, what was he saying about the, you know, about that field?

**Matthew Panzarino:** I would just scrub it and find it.

**Matthew Panzarino:** So I would say leave those open in a tab while you're setting this stuff up, just in case, for reference.

**Matthew Panzarino:** Or the transcript at the very least, right?

**Matthew Panzarino:** Search the transcript or scrub the transcripts.

**Matthew Panzarino:** They can be very helpful.

**Matthew Panzarino:** I know they've been very helpful to me.

**Matthew Panzarino:** So I just wanted to mention those two resources are extremely important to check.

**Matthew Panzarino:** So let me just jump in here and go over this a little bit.

**Matthew Panzarino:** So what am I sharing?

**Matthew Panzarino:** Oh, let me share this.

**Matthew Panzarino:** Just sharing just this one window.

**Matthew Panzarino:** This one window.

**Matthew Panzarino:** Yeah?

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** right.

**Matthew Panzarino:** So the, this is our new workspace, right?

**Matthew Panzarino:** This is what we're working in.

**Matthew Panzarino:** When you hit new here, and you name a workspace, I'm going to say, I'm going to do.

**Matthew Panzarino:** Most of you won't have to do this, right?

**Matthew Panzarino:** Because it should be set up for you.

**Matthew Panzarino:** You can create an account.

**Matthew Panzarino:** They're very helpfully ordered in creation order.

**Matthew Panzarino:** I think they were originally alphabetical.

**Matthew Panzarino:** But once you've got a company, you can then add a workspace.

**Matthew Panzarino:** Let's name it company X.

**Matthew Panzarino:** Got a workspace.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** That's what you're working in.

**Matthew Panzarino:** These workspaces.

**Matthew Panzarino:** That's what these companies are, right?

**Matthew Panzarino:** That we've created.

**Matthew Panzarino:** So it's a client and then a workspace within that client.

**Matthew Panzarino:** And then we have the dashboard, which is blank, the context artifacts, and then the projects.

**Matthew Panzarino:** So obviously a new project would be would be um...

**Matthew Panzarino:** ...

**Matthew Panzarino:** ...

**Matthew Panzarino:** Yeah, let's get a company blog, and then within that, you've got the pipelines, create a pipeline, you see the pipeline configuration here, nobody's expecting you to know this or write this, but if you want to, you can just go grab one of the pipelines from one of the other workspaces and paste it in here, like article generation, as an example.

**Matthew Panzarino:** I don't think anybody needs to be doing all this stuff I just did, by the way.

**Matthew Panzarino:** It should be set up for you, and if it's not, let them set it up the first time, right?

**Matthew Panzarino:** Flag it, like these companies that don't exist yet, let them set it up.

**Matthew Panzarino:** I'm just showing you, like, this is just building blocks, right?

**Matthew Panzarino:** This is how these things are created.

**Matthew Panzarino:** The same thing for the artifacts.

**Matthew Panzarino:** If you create an artifact, it's got these fields that you fill out.

**Matthew Panzarino:** This one's like company personas, and then, you know, the display name, and the technical variable name.

**Matthew Panzarino:** This is just the plain text.

**Matthew Panzarino:** And then in here, it's just the same text that you would see in any other artifacts.

**Matthew Panzarino:** So I'll show you an example of this.

**Matthew Panzarino:** If I go into, say, Abnormal, and I go into the Context Artifacts, you've got Company Context, Writing Guidelines, Audience Personas, that sort of thing, right?

**Matthew Panzarino:** So if I wanted to create an Audience Personas artifact where there wasn't one previously, I can just copy this and paste it into that field that I just showed you.

**Matthew Panzarino:** It's the same thing.

**Andi Bailey:** It's just text.

**Andi Bailey:** Can we see the templates?

**Andi Bailey:** Like, so I'm curious, as a minimum, to really put really great output out, how, like, what artifacts should you always have?

**Matthew Panzarino:** So if, like, there's only two...

**Matthew Panzarino:** It's pre-populated with the artifacts.

**Andi Bailey:** Oh, sorry, go ahead.

**Andi Bailey:** Yeah, well, some of them have two, some of them have four.

**Andi Bailey:** So, like, what ones do you almost always want to have?

**Matthew Panzarino:** an how, how, how, how, how, how, how, Thank you.

**Matthew Panzarino:** In general, you need audience personas, company context, writing guidelines, and then theoretically CTAs, if the company wants the CTA.

**Matthew Panzarino:** So all of these should be in here already, and if they're not, then you should know they're missing, because when you went to fill them out, they'd be missing.

**Matthew Panzarino:** These would have been pre-populated by pulling these same fields from air ops, theoretically, that's the theory.

**Matthew Panzarino:** If they were pulled properly, you should already have all of these in here.

**Matthew Panzarino:** The contents of them should all be checked manually and strenuously by you, because this is the building blocks for everything you'll do from here.

**Matthew Panzarino:** These workflows are all about amplification of effort, so that means that any tweaks you make, small tweaks that you make at the beginning of this, result in large deltas of outcome.

**Matthew Panzarino:** If you don't get this right, you're going to be hundreds of articles in before you're like, you know, this is frustrating, I'm having to go out.

**Matthew Panzarino:** Okay, well, let's go back to the beginning.

**Matthew Panzarino:** Thank

**Matthew Panzarino:** The seed here, and let's look at these initial artifacts and see if they're correct.

**Matthew Panzarino:** So the artifacts, these are, and I have to say, it's really nice to actually have some documentation built in, right?

**Matthew Panzarino:** So these are the, you see the little guidelines here, things like personas, audience, and how we talk to those people and what they care about.

**Matthew Panzarino:** These could be better, we'll get better about documentation, but there's some.

**Matthew Panzarino:** So if we go into audience personas as an example, you've got this audience persona that was all about the people that you'll be talking to.

**Matthew Panzarino:** So this is the people you're writing for, your audience, effectively.

**Matthew Panzarino:** You, as an operator of these workflows, and the workflows themselves, are taking on the role of an editor and a writer for this company.

**Matthew Panzarino:** And if you're an editor or a writer, you're always speaking to someone, some audience of some sort.

**Matthew Panzarino:** You have to be talking to people, not just about.

**Matthew Panzarino:** For a topic, you need to understand the people that you're talking to.

**Matthew Panzarino:** That's what these personas are.

**Matthew Panzarino:** It is, who am I writing this article for, specifically?

**Matthew Panzarino:** And the detail that you can see here was not reflected in most of the Aerox workflows that I reviewed when I did my audit.

**Matthew Panzarino:** So this is where we should, this the state of the art now.

**Matthew Panzarino:** You should be looking for something this dense and this extensive for your audience personas.

**Matthew Panzarino:** You'll notice that these are broken down.

**Matthew Panzarino:** You know, this particular format is not, you need to be copied exactly, but this has, it literally creates a little bit of a persona of a person, what their daily routine is like, what their fears and uncertainties are, what motivates them, how to win their trust, how to annoy them and destroy trust.

**Matthew Panzarino:** So positives and negatives, what they care about, their biggest pain points and frustrations.

**Matthew Panzarino:** And then, of course, it goes on to a couple of others.

**Matthew Panzarino:** The paranoid seesaw as another example.

**Matthew Panzarino:** to them.

**Matthew Panzarino:** how old come 강

**Matthew Panzarino:** Where are they?

**Matthew Panzarino:** What is their daily reality, et cetera?

**Matthew Panzarino:** The reason that you give the AI this context is because when it's writing, it can choose topics that directly address these issues that are related to the company.

**Matthew Panzarino:** So if it's abnormal, or let's say it's Gitpod as an example, since this is Gitpod, they care about how to annoy them, promise to replace their entire infrastructure stack with simple AI solutions.

**Matthew Panzarino:** So when writing an article about Gitpod, the LLM is going to take this instruction and not say, you can replace your entire stack with Gitpod.

**Matthew Panzarino:** It's like a blank in a box, right?

**Matthew Panzarino:** It's just going to avoid those kinds of broad generalizations that would just annoy someone like this and cause them to tune out.

**Matthew Panzarino:** That's what these instructions are for, is to help guide the way we write the content.

**Matthew Panzarino:** Yeah.

**Andi Bailey:** So I'm seeing that we're missing potential CTAs and like, if we're missing any, as I'm just saying.

**Andi Bailey:** Clicking through these, it's potential CTAs in a lot of these.

**Matthew Panzarino:** Potential CTAs was one that was not created in a lot of AROPS grids.

**Andi Bailey:** Okay.

**Matthew Panzarino:** And frankly, there were a lot of AROPS grids that were missing writing instructions as well when I did my audit.

**Matthew Panzarino:** So it's quite possible that you won't have one or more of these.

**Matthew Panzarino:** And if you don't, and let's say you don't need CTAs, let's say your client does not use CTAs because they have it in their footer, right?

**Matthew Panzarino:** Like they don't require a CTA at the end of their article.

**Matthew Panzarino:** CTA, by the way, just so we're all on the same page, is, hey, if you need help with this, you should check out Gitpod, link to Gitpod, right?

**Matthew Panzarino:** Like that's whatever CTA that they normally want as a template.

**Matthew Panzarino:** There's none here in Gitpod because they haven't created one for them.

**Matthew Panzarino:** But if you don't need it, don't click, right?

**Matthew Panzarino:** It doesn't need to be here for anything to work.

**Matthew Panzarino:** It can be called by the writing instructions so that it embeds it at the end of your article automatically.

**Matthew Panzarino:** But it is not mandatory, but the audience persona.

**Matthew Panzarino:** Company Context and Writing Guidelines are mandatory.

**Matthew Panzarino:** If your artifacts do not include these three, you're in trouble and you need to add it right away.

**Matthew Panzarino:** You're missing one, just really quickly.

**Matthew Panzarino:** Let's say you're missing one, like Company Context, you can copy it.

**Matthew Panzarino:** Just copy from here.

**Matthew Panzarino:** So if you go into here and you look at Company Context, Guidelines, blah, blah, If you edit this here, you can see that it has the display name, Company Context, the variable name, Company Context.

**Matthew Panzarino:** The Type is Guidelines, always, for now.

**Matthew Panzarino:** These other things, don't worry about these yet.

**Matthew Panzarino:** And then Description is just what you want to write.

**Matthew Panzarino:** You could, I wrote the dates in the ones that I updated.

**Matthew Panzarino:** Company Context as of, you know, 616, Panzer's edit, right?

**Matthew Panzarino:** So that you can just, it's just context for you.

**Matthew Panzarino:** And then the content itself, whatever you want the context to be.

**Matthew Panzarino:** That's all this is.

**Matthew Panzarino:** So if you need to create an artifact, just put this information in up If big scene it,

**Matthew Panzarino:** And then put your context in there.

**Matthew Panzarino:** So if I needed to create a new one right now, I would do company context, company underscore context, guidelines, description, and then paste it in, and then create artifacts.

**Andi Bailey:** Yeah, and then in the interest of like, okay, if we need to go in and somebody needs to add one of these artifacts, obviously, what are the, which models would you suggest that they go in and what are the prompts that you would say that they should do to generate, like, enough company context to drop in here?

**Matthew Panzarino:** Yeah, so I covered this in my other air ops training, so you can watch that and talk about all the ways that you could populate that field.

**Matthew Panzarino:** But the shorthand is it should technically be in the kickoff document.

**Matthew Panzarino:** There should be a full company context document already in there in Notion, company space, docs, company brief, right?

**Matthew Panzarino:** That should be a starting point for you.

**Matthew Panzarino:** All

**Matthew Panzarino:** However, there are other ways to generate it.

**Matthew Panzarino:** You can use perplexity to generate it.

**Matthew Panzarino:** You can use a template that already exists and then ask perplexity or odd to generate you company context based on that, and then you should review it.

**Matthew Panzarino:** If you want one right now that is fairly state-of-the-art, Marcel just wrote these for Gitpod.

**Matthew Panzarino:** You can look at the ones from Gitpod here and say, okay, cool, I'm going to at least start here, especially if you don't have any, right?

**Matthew Panzarino:** If you're starting from zero, you can definitely jump in here and look at what he's done for this company profile and say, okay, this is the place to begin.

**Matthew Panzarino:** If you just needed something where you can start generating articles 30 seconds after this call, copy this, paste it into Claude and say, hey, I have a new company that I'm writing articles for.

**Matthew Panzarino:** The context is, I need to feed this to an LLM to help it understand what this company is.

**Matthew Panzarino:** Please create this kind of document for this company.

**Matthew Panzarino:** Give it the name and your.

**Matthew Panzarino:** Oh, and a few bits of context about it, and then it'll create one in this template for you.

**Matthew Panzarino:** Simple.

**Matthew Panzarino:** So, at least a seed to begin with.

**Matthew Panzarino:** Some of you may already have extensive company context, either because I created them, or because you went in and created them, or because you've already grabbed it from Notion, or you've refined it over time.

**Matthew Panzarino:** That's great.

**Matthew Panzarino:** But if you don't have anything, you need to have something, and here's a place to begin.

**Matthew Panzarino:** The same thing goes for those personas we talked about.

**Matthew Panzarino:** This is a great template.

**Matthew Panzarino:** I think this is actually a really good state-of-the-art for where these personas, what they should look like here, with all of this coverage of fears and pain points and motivations.

**Matthew Panzarino:** And then the writing guidelines, I don't think that this is absolutely the exact example of what everybody should do, because you've talked to your clients, and you may have specific instructions about what your client likes or doesn't like.

**Matthew Panzarino:** That's what this is for.

**Matthew Panzarino:** However, this is a place to begin.

**Matthew Panzarino:** Fair enough.

**Matthew Panzarino:** Fairly, this is a place to begin, especially for technical clients.

**Matthew Panzarino:** There's a lot of instructions here.

**Matthew Panzarino:** That are applicable to a lot of your clients that are very technical clients.

**Matthew Panzarino:** So you can use this as a jumping off point.

**Matthew Panzarino:** But I think there's one huge thing that I should stress here.

**Matthew Panzarino:** These are living documents.

**Matthew Panzarino:** You cannot fill these out once and forget about them.

**Matthew Panzarino:** And I think what I've seen a lot of times is that the writing guidelines are the same on the first run as they are on the 200th run of a grid.

**Matthew Panzarino:** And that cannot be true.

**Matthew Panzarino:** I would defy anybody to say that they can do that.

**Matthew Panzarino:** If you have done it that way and it's good, it is most likely because your client wants a very specific templated style of output.

**Matthew Panzarino:** Fair enough.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** I get it.

**Matthew Panzarino:** If the work is coming out and it's being published and the client loves it, I don't care what you do.

**Matthew Panzarino:** Like if you've stapled two things together and it's working, you know, cool.

**Matthew Panzarino:** But it's just unfathomable to me that we would run our first workflow and get results and ship that.

**Matthew Panzarino:** And then 200 articles later.

**Matthew Panzarino:** Still.

**Matthew Panzarino:** Using the same exact version of the writing guidelines, or even personas, right?

**Matthew Panzarino:** And the company context may not change, but it probably should.

**Matthew Panzarino:** Like, we have a company, who is it?

**Matthew Panzarino:** Somebody is just releasing, God, who was it?

**Matthew Panzarino:** I don't there's a lot of companies in my head, but one of them is just releasing new features, right?

**Matthew Panzarino:** And they said, hey, we've got new context.

**Matthew Panzarino:** Somebody was actually getting, they're like, oh man, you know, like, you can't say this because we're not this yet.

**Matthew Panzarino:** There was somebody who was certified for data, I can't remember.

**Matthew Panzarino:** I can look at it in a moment, and I'm sure I can figure it out.

**Matthew Panzarino:** But the idea is they're releasing new features.

**Matthew Panzarino:** If they're releasing new features, their company context should change.

**Matthew Panzarino:** They have new features, right?

**Matthew Panzarino:** They do things differently now.

**Matthew Panzarino:** Sometimes, not sometimes, a lot of times, we work with startups, startup pivot.

**Matthew Panzarino:** If they have changed their, like, take, if they have issued a new press release, if they have a new, like, big interview where their CEO is talking about their new direction and all of this stuff, got We're

**Matthew Panzarino:** Our company context is now different than what it was when they signed up with us.

**Matthew Panzarino:** So these should be living documents.

**Matthew Panzarino:** You should review them, I would guess, at least monthly, if not weekly.

**Matthew Panzarino:** On the writing guidelines, that's something you could probably massage every time to get a little bit better.

**Matthew Panzarino:** Ideally, I would love a loop that allows you to do the edits at the end, and then that would inform your writing guidelines.

**Matthew Panzarino:** But for now, you're going to be manually at the end of these writing guidelines.

**Matthew Panzarino:** So if you're doing something over and over and over, make sure it's represented in your writing guidelines.

**Matthew Panzarino:** And if it's not, you know, that's step one.

**Matthew Panzarino:** Then from there, we can figure it out.

**Mariana Marins:** Guys, and the resources you can get to get these little things that are changing, scrape the external channel that you have with the client, and also scrape the meetings, the fathoms, recaps that you have with the clients.

**Mariana Marins:** Compile everything, and see if you have that on your...

**Mariana Marins:** If you don't have, please add.

**Mariana Marins:** I think that's the most updated resources that you are going to find, the external channel and the meetings, the weekly meetings, and so on.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** I mentioned that in that AirOps training as well.

**Matthew Panzarino:** I think that's on that reporting because that is like the client may have told you a bunch of stuff since we filled out the notion, right?

**Matthew Panzarino:** And maybe the notion is not that complete, but your most up-to-date client comms is going to be in that external Slack and with your fathoms.

**Matthew Panzarino:** So they may be telling you stuff all the time that you need to add to your writing instructions.

**Matthew Panzarino:** So you can generally find good information there.

**Matthew Panzarino:** But yeah, hey, we have another one of these tomorrow.

**Matthew Panzarino:** We can go over more.

**Matthew Panzarino:** We'll dive in.

**Matthew Panzarino:** And I hope to have enough confidence in what all of these fields do and are mapped to and all of that stuff to record something for you ASAP.

**Matthew Panzarino:** I'm going to try to get a recording this week that is basically an updated version of the AirOps thing so that we can go through it.

**Andi Bailey:** Yeah.

**Matthew Panzarino:** No problem.

**Andi Bailey:** You.

**Andi Bailey:** And other people can tell me that this isn't helpful, but, like, all the things that go into building this and, like, where you pull those, if those are in an AirOps call, like, in your AirOps reviews, cool, but, like, if we can say, like, and remember, this is where you pull your keywords or how you do this, because, like, how they're going to input the other parts that aren't the, like, Daniel referenced, like, uploading your keywords or your URLs, like, what's the specific process to that?

**Andi Bailey:** Because I think, like, we really are getting thrown in the middle here for some things, and people are getting thrown around, so how do they confirm that that's right?

**Matthew Panzarino:** Yeah, sounds good.

**Matthew Panzarino:** I think there's two major things that need to happen.

**Matthew Panzarino:** One is we need to understand all these things before we talk about it, and then the second thing is I'll record and document it.

**Matthew Panzarino:** Then, actually, there's a third thing, which is we now have places, as I showed, if there's at least a couple lines of context about what this field is, we can make that more extensive.

**Andi Bailey:** Yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** You can it more.

**Matthew Panzarino:** Well, keep saying robust,  LLN, pardon my French, but the, the, that can be a little bit more detailed, it's like, what should this field contain, and it links to the trainings and stuff like that, it's like, at a glance, if you have new CMs, or people that are coming in, or you're, you're like, what is this field again, then we'll have some reference, so.

**Andi Bailey:** Perfect, yeah.

**Matthew Panzarino:** As someone who's a learner by, like, manuals and reading, like, that would be awesome, and having to, like, keep going back to, like, fathoms and things like that, it would, that would be amazing.

**Matthew Panzarino:** The goal would be, too, to create, and this is something we, we didn't do for the AirOps one, only because we were, like, moving off of AirOps, but we're going to create, like, a, a Notion page manual version of the AirOps, of the Atlas training that I can record, like, and, you know, here's what the different pipelines are, and here's how to use them, and here's what all the fields are, we'll do all that, and then we'll, we'll flow it into a Notion doc, so we at least have a great, scanable reference.

**Matthew Panzarino:** Sweet.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Thanks, folks.

**Matthew Panzarino:** Ciao.

**Matthew Panzarino:** Bye-bye.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Bye.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Bye.
