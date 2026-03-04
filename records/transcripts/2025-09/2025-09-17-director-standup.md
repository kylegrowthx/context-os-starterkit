# Director Standup

<metadata>
date: 2025-09-17
time: 19:01 UTC
duration: 30 minutes
organizer: Matthew Panzarino (GrowthX)
participants: Andi Bailey (GrowthX), Jakub Rudnik (GrowthX), Kyle Gaudreau (GrowthX), Mara Leighton (GrowthX Labs), Matthew Panzarino (GrowthX)
fathom_recording_id: 88000232
fathom_url: https://fathom.video/calls/412195137
share_url: https://fathom.video/share/9nsy7T4oqiT4_qC82UzGemscjj2Grh59
source: fathom
enriched_on: 2026-03-03 17:35 UTC
</metadata>

---

## Summary

GrowthX's director team discussed how to scale delivery as the ME team grows from new hires (Bailey and Katya) and accounts multiply to 9+ per director. The core tension: directors are spending all their time on client calls and tactical relationship-building, leaving no capacity for strategic deep work. The team aligned on three solutions: selective director presence (monthly analytics reviews, strategic touchpoints vs. every call), automated reporting (templated ME updates with key blockers and account narratives instead of task-focused geekbot updates), and a customer sentiment dashboard built from call transcripts to flag account health signals without relying on manual team reporting.

---

## Context

This is an internal GrowthX director standup examining operational scaling challenges. The meeting was prompted by two new ME hires starting (Bailey and Katya, joining an already growing team), which raised an urgent question: how do directors manage 9+ accounts without defaulting entirely to client calls and losing the ability to do strategic work? Mara Leighton (an external advisor from GrowthX Labs with prior experience at Verbatim managing 20 accounts) joined to share context and learnings from scaling similar models. The meeting was a frank discussion among the delivery leadership team about the structural problem of time constraints and potential tooling and process solutions.

---

## Relevance

### To GrowthX Delivery
- **Scaling model under strain:** Directors are hitting capacity limits around 9 accounts; current structure (attending every call + strategic deep work) is not sustainable as ME team grows. Need decision on selective call attendance vs. reporting-based visibility.
- **Templated ME reporting:** Current geekbot updates focus on task counts, not strategic insights. Directors need key blockers, account narratives, and health flags to make decisions without attending every call. Jakub's monthly analytics review for city-state clients is a working example.
- **Account health scoring:** Kyle is manually pulling and analyzing transcripts per account to track sentiment and decision evolution. This needs to be automated (cloud project + Atlas dashboard) to scale.
- **Relationship-building differentiation:** Directors joining selectively (vs. every call) can create impact moments and one-on-one touchpoints; Mara shared evidence from Verbatim that 70% call attendance maintained relationships better than 100% while freeing director time.

### To GrowthX Business Development
- **Hiring timeline:** Two new MEs starting (Bailey, Katya). System needs changes before hires compound the workload problem. Next decision point: how many more accounts can current directors take without restructuring?
- **Director bottleneck for new clients:** If directors can't scale, client acquisition is limited by director capacity, not ME availability. This is a growth ceiling unless solved.

### To Tools & Systems (Atlas, Cloud Projects)
- **Customer sentiment analysis project:** Priority build: fork Panzarino's artifact updater cloud project to extract and aggregate sentiment per call, then dashboard in Atlas. This flags account health signals that directors miss when not on all calls. Panzarino has the spec; scope and roadmap needed.
- **Reporting integration:** Sentiment dashboard should connect to Andi's weekly leadership reporting and be accessible to Marcel for executive visibility across all accounts.
- **HubSpot / HockeyStack evaluation:** Andi to research CS tooling that may already solve sentiment/account health tracking; avoid building if mature COTS exists.

---

## Overview

- Directors are experiencing time constraints balancing client relationships, strategy, and deep work as account numbers grow
- Need for improved reporting and automation to maintain visibility and efficiency with increased workload
- Potential for reducing director presence on all client calls, focusing on key touchpoints and relationship-building opportunities
- Exploration of sentiment analysis tools and CS tooling to enhance client management at scale

---

## Key Topics

### Current Challenges with Scaling

  - Directors attending all client calls, limiting time for strategic work and deep dives
  - Difficulty maintaining depth on strategy across growing number of accounts (9+ per director)
  - Time constraints affecting ability to excel accounts vs. just keeping them afloat
  - Concerns about losing visibility into account health and client relationships with increased volume

### Potential Solutions for Scaling

  - Selective attendance of client calls based on account stability and strategic importance
  - Implementation of consistent, efficient reporting formats from MEs to directors
  - Automation of key metrics and sentiment analysis from call transcripts
  - Monthly analytics reviews and targeted check-ins to maintain strategic oversight
  - Exploration of CS tooling and existing solutions (e.g., HubSpot, HockeyStack) for sentiment analysis

### Improving Reporting and Visibility

  - Current geekbot reporting focuses on task-oriented updates, lacking strategic insights
  - Need for templated reporting capturing key blockers, account narratives, and strategic concerns
  - Proposal for automated flagging of performance and sentiment signals from call transcripts
  - Discussion of creating a customer sentiment dashboard in Atlas

### Artifact Management and Feedback Integration

  - Panzar shared insights on cloud projects for artifact updates and feedback integration
  - Potential to adapt existing tools for sentiment analysis and strategic insights across accounts
  - Importance of centralizing insights for easy access by all stakeholders, including leadership

---

## Action Items

**Andi Bailey (GrowthX)**
- Research CS tooling, sentiment analysis tools, and client management software (e.g., HubSpot, HockeyStack) to identify existing solutions for tracking customer sentiment across calls and interactions before building in-house.

---

## Transcript
**Mara Leighton:** Cool.

**Mara Leighton:** Anser, how's it going?

**Matthew Panzarino:** Still good.

**Mara Leighton:** Good.

**Matthew Panzarino:** I feel like a million things that I want to get to, but I'm like, nope, client, client work.

**Matthew Panzarino:** And then I'm like, oh, client work.

**Matthew Panzarino:** And then I'm like, just kidding, got to do interviews instead.

**Matthew Panzarino:** Totally.

**Matthew Panzarino:** It just all stacks up and I ended up doing everything at 3 p.m.

**Mara Leighton:** Oh, I totally get that.

**Matthew Panzarino:** When I'm the least creative and most exhausted, that's when.

**Mara Leighton:** I totally get that.

**Mara Leighton:** Yeah.

**Mara Leighton:** The good thing is if you're finding a silver lining, when I get really like tired and overwhelmed, I'm never more efficient.

**Matthew Panzarino:** You know, I'm like, okay, we got to call it the gas.

**Matthew Panzarino:** Yeah, let's not care so much about this.

**Mara Leighton:** We're just going to get it done.

**Mara Leighton:** I just got to barrel through all of this.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah.

**Andi Bailey:** Thank I don't know if anybody else is joining.

**Andi Bailey:** Megan has something happening, house stuff that she has to deal with.

**Andi Bailey:** And Kyle or Jason accept.

**Andi Bailey:** Yeah.

**Andi Bailey:** and

**Andi Bailey:** Oh, Jason is not turning.

**Andi Bailey:** Okay.

**Andi Bailey:** We can get started.

**Andi Bailey:** I want to talk about two things today.

**Andi Bailey:** The first is like a question that it's like a continuation of a conversation that we keep having, but I just, uh, we have, so context here is what, like, and the reason that I'm bringing this up again in a different way is, um, we have two MEs starting, well, two MEs have started, uh, Bailey started last week.

**Andi Bailey:** She's on vacation this week, but she's gonna, uh, shadow Panzer next week and start taking over his accounts.

**Andi Bailey:** Um, and then Katya started this week.

**Andi Bailey:** She, um, she actually was working and she, at an unnamed, she was doing like.

**Andi Bailey:** Prompt Evaluation, I think, for an unnamed AI company.

**Andi Bailey:** So she's got, like, some really interesting experience.

**Andi Bailey:** But she started this week, and she's going to take over some of the accounts that are at the end of Strategy Sprint.

**Andi Bailey:** And I think she'll be in a holding pattern, like, kind of echoing Sydney and Strategy Sprint for now.

**Andi Bailey:** Oh, Kyle.

**Andi Bailey:** Hello.

**Andi Bailey:** So mysterious.

**Andi Bailey:** But we, obviously, like, the number of MEs is growing, the number of accounts is growing, the number of, like, slash account strategists who will also, like, kind of be owning a director-type role.

**Andi Bailey:** We're, we are not finding as many of those as quickly.

**Andi Bailey:** Um, and so they're, but the ME role still, I think...

**Andi Bailey:** Needs to report into or like, we'd like to keep the pod structure the same, having them work with an account director or strategist to like have somebody helping them think high level long term about like account health and building relationships.

**Andi Bailey:** So my question to you guys is, you know, there are two more Emmys that are each taking on three more accounts, what would need to be true for you to feel comfortable taking on another Emmy with additional accounts?

**Andi Bailey:** Like, where would you feel squeezed?

**Andi Bailey:** Where would you need support?

**Andi Bailey:** What would be your concerns?

**Kyle Gaudreau:** I think for me, the concern would be just

**Kyle Gaudreau:** It's like having the the right level of depth on like strategy and like what we're actually doing.

**Kyle Gaudreau:** I'm finding like I can do that to some limiting degree today, but not as much as I would like to.

**Kyle Gaudreau:** And so I would worry by adding another that that's just like compounding that issue.

**Kyle Gaudreau:** So then it's like, how do you solve within that model?

**Kyle Gaudreau:** There needs to whatever that looks like, finding more capacity within that structure to ensure those things are covered.

**Kyle Gaudreau:** So is that some other, you know, type of role alongside the ME?

**Kyle Gaudreau:** Is that a different style of ME or whatever it is?

**Kyle Gaudreau:** But I'm finding like, you know, the coaching I'm at least giving is providing some is bearing some fruit.

**Kyle Gaudreau:** Um, but my hunch is there, there's like a layer deeper I need to.

**Kyle Gaudreau:** Go for this to, like, really work well from a strategic perspective, and what am I on, like, nine accounts now?

**Kyle Gaudreau:** Something like that.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** I'm still, like, kind of, like, forming my perspective and, like, you know, trying to see, like, these ideas, if they work, but it's fairly high level, but that's, like, one of the initial things that come to mind.

**Andi Bailey:** Yeah, I mean, that's helpful, because, so, just so you know, Katia's gonna take Udemy from Matt, and then she's gonna take two other accounts, so she's gonna, like I said, stay in a holding pattern under, like, strategy sprint, but she'll be supporting Udemy starting next week, and then she'll have Sentinel-1 and Understory.

**Kyle Gaudreau:** Got it, cool.

**Jakub Rudnik:** To Kyle's point, the, when I took on the, like, Justice pod, it was, like, third pod.

**Jakub Rudnik:** For however long that was, it certainly crams your schedule more, just the three additional calls, plus any one-on-ones and stuff, so you just lose a couple hours right away, and then prep and reviewing agendas, so there's just some level that gets sliced off your week there.

**Jakub Rudnik:** But I think the bigger one was, I couldn't get, Interval, I had to throw so much time on, so that is a little bit of an outlier, but for instance, Seat was strong enough, so strategy-wise, I could only do one, dive in to one account maybe a week, and so some strategies to revisit, where are we?

**Jakub Rudnik:** It was like, I just have to trust that some of this is going, and I think, like, now I'm feeling some of that, like, I didn't get to some of those pieces, because it was, like, keeping things afloat more than, like, how do they really excel, and I think that just got lost, and so even the accounts that I had been doing that for more often, it was, like, I was doing it once every six weeks for them or something, where I was, like, spending dedication.

**Jakub Rudnik:** So some of that's like, do they need that strategy if you get handed like a, like if someone got handed Tiro from me, like things just are moving really smoothly.

**Jakub Rudnik:** The MEs are all in, you just have to like be there to kind of answer questions and add a little bit of support.

**Jakub Rudnik:** But if someone needs like, if their strategy is unclear or it's in mixed state, and I think that's happening less with how strategy sprints are going.

**Jakub Rudnik:** But just in general, there are accounts like that, that stuff's kind of murky or they've had less attention or things are going wrong.

**Jakub Rudnik:** If you have some of those, like you can't, adding three more becomes like, can't, you just get really stretched.

**Jakub Rudnik:** So I think the type of account does matter.

**Jakub Rudnik:** It's on there, but the deep work falls off when you start adding all the extra week to week stuff.

**Mara Leighton:** Yeah.

**Mara Leighton:** Just to like kind of piggyback on what both of you have said, I would agree that I feel like it either, like if all of these variables are stable, consistent, you have like a more like senior level or.

**Mara Leighton:** A really, you know, strategy-minded ME who's, like, very comfortable with the day-to-day, then I feel like it's easier to expand volume where you can kind of dip into the accounts that need the most attention.

**Mara Leighton:** But if generally, like, there's not more than, like, two or three at a time that need, like, heavy hands-on, then I feel like more accounts is feasible.

**Mara Leighton:** But if you need, if you have, like, you know, a couple MEs that need more coaching or, you know, like three or four accounts that are, you know, at a time, then I think it gets difficult to do, like, an adequate amount of support.

**Mara Leighton:** But if you have a really good team and the strategy is set and you just have to kind of pay attention and, like, drop in where necessary, then it's a nice model.

**Mara Leighton:** I think for me too, I would probably just need to figure out what kind of visibility am I losing by gaining, you know, like three extra, if it gets to, you know, like 11 or something, like what kind of visibility am I missing?

**Mara Leighton:** Like what questions do I typically have?

**Mara Leighton:** And then I would probably want to create some type of consistent reporting within the team of like, whether it's documentation or we just, I mean, you're going to lose time getting up to speed anyway.

**Mara Leighton:** But just more of like a repeatable, really like efficient format for those, whether it's like the discussions we have with MEs or what are, what context am I missing consistently by expanding volume?

**Mara Leighton:** And how do I like create a process where it doesn't take a ton of fun?

**Mara Leighton:** Time for me or the ME to communicate that information so I can like do a pseudo level of that visibility.

**Andi Bailey:** That's really helpful.

**Andi Bailey:** So I don't know, do the rest of you guys agree with that?

**Andi Bailey:** Because maybe we could dive into what kind of documentation we would need.

**Andi Bailey:** I feel like geek bots right now are a lot of like task slash action oriented reporting.

**Andi Bailey:** It's like three articles for X and not nobody's thinking like this look or look weird have to figure that out or like I don't see a lot of that in geek bot reporting from anybody besides directors.

**Andi Bailey:** So yeah, like what, where, how would you want that kind of templated reporting?

**Mara Leighton:** I feel like typically, like, I guess it just depends on, like, what pops up when we scale up, but just assuming, just making assumptions, I feel like for me, would probably be, like, if I'm attending every call as I am now, this doesn't necessarily factor in.

**Mara Leighton:** But if we start kind of triaging calls, I would want to go through the client database, probably, with my MEs or team at every call and just get a sense of, like, you know, what's the tenor of the last conversation?

**Mara Leighton:** Did they mention, I don't actually, I don't know, this is all, like, speculative, but, yeah, I don't know.

**Mara Leighton:** I guess it just depends on what we do less of, and then we would need to find a time, a way to compensate for that with communication, but.

**Andi Bailey:** Yeah, that's a good flag.

**Andi Bailey:** Are you guys all joining all the client calls right now?

**Mara Leighton:** Yeah.

**Andi Bailey:** Yeah.

**Andi Bailey:** And I think, like, to me, that's the most important.

**Andi Bailey:** And Marcel said something similar to me this week, like, relationship building is a huge part of the director's role.

**Andi Bailey:** think, Kyle, you probably really have leaned in on this and seen this, most of any of us.

**Andi Bailey:** But, like, that relationship building piece is, like, so core to growthx that then, but then that becomes, like, calendar Tetris.

**Andi Bailey:** there's, to something Jakub said before, there's not a lot of time for deep work.

**Andi Bailey:** So you're either relationship building or you're doing deep work and there's not time for both when you get to, like, a critical mass.

**Kyle Gaudreau:** I mean, there's probably a way of what does it look like for a director to not have to be on each call and what are the times?

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Naturally, it makes most sense for it.

**Kyle Gaudreau:** Are those like, you know, some sort of like cadence of repeatable touch points, you know, like, for example, like, doesn't seem like we're yet at a phase, maybe I'm off on this, but like, on like doing like monthly review data check-ins, like, let's look back at August kind of thing.

**Kyle Gaudreau:** Not limited to that, but just using that as an example of like, oh, that could be a good time for the director to join, right?

**Kyle Gaudreau:** I think there's going to be some accounts where it's just like, for a whole variety of reasons, should aim to join most calls.

**Kyle Gaudreau:** And then, you know, the in-between can be like, how do you have those check-ins with those people, sending them a note, getting, you know, just keeping a convo going, but also just like finding those right moments to like, if a one-on-one makes sense.

**Kyle Gaudreau:** I have a hunch, like, you know, if we've...

**Kyle Gaudreau:** Feel comfortable on who's leading the calls that are set up for success.

**Kyle Gaudreau:** Like we don't need to have the directors on each call.

**Kyle Gaudreau:** It's just like, it's kind of been a band-aid for us as like we're trying to like get everyone up to the right level and like more repeatable process.

**Kyle Gaudreau:** And I don't know.

**Mara Leighton:** I would agree.

**Mara Leighton:** Oh, sorry.

**Kyle Gaudreau:** Continue, Kyle.

**Kyle Gaudreau:** No, I was probably just going to ramble.

**Mara Leighton:** I was going to say, would agree with everything.

**Mara Leighton:** Something that might be useful or just like to consider something that we did like at verbatim when at one point it was like, I think I'd like 20 accounts.

**Mara Leighton:** What we could do or what something to consider would be like, you know, the ME is the like daily touch point and tactical like or like in the weeds essentially of like the daily processes of CMs.

**Mara Leighton:** And obviously the director needs to have visibility as well.

**Mara Leighton:** But like something that we could do is if they're at a really stable point.

**Mara Leighton:** right a very

**Mara Leighton:** There's a really good relationship between the ME and that team.

**Mara Leighton:** You know, maybe the director needs to be on, or just depending on the relationship, depending on, you know, if it's really steady or if it's like leaning towards more like lukewarm, then you would need to be on 100% of the calls.

**Mara Leighton:** Maybe otherwise the director, use your best judgment, it's 70% of the calls.

**Mara Leighton:** I do think sometimes it's useful to not be on 100% of them if the client relationship is really stable, just so that in the same way that we could pull like Marcel in for a certain type of conversation, the director can join to kind of like help lend some weight or like escalate a conversation by attending, like dropping in.

**Mara Leighton:** And you get that benefit of like, not like not having full context, but kind of like a, a little bit of a, not like a tension breaker, but turning a new chapter also opens up the opportunity for you to DM the main stakeholder for like.

**Mara Leighton:** Like, hey, like, sorry, I've missed a couple calls.

**Mara Leighton:** Things have been wild, but like, can we catch up for five, 10 minutes?

**Mara Leighton:** I'd love to just hear from your perspective, like how things are going.

**Mara Leighton:** Not that we can't do that if we're attending 100% of the calls, but I think that's like how, like, I would think about it of like, how do I keep building a relationship or like leverage this differently if I'm out of the day-to-day?

**Mara Leighton:** And then obviously, if you're local, that's nice too.

**Mara Leighton:** You can meet up with them in person and all that stuff.

**Mara Leighton:** But that's one way that we did it would be kind of like, okay, I'll ping someone to say like, hey, this is a conversation I think you should really be a part of or you don't need to join today.

**Andi Bailey:** Yeah.

**Jakub Rudnik:** To add a couple more things that were talked about there, Kyle, I do the analytics thing monthly for, and like at the first week of each month, it's like the penciled in time and we push it if we need to, but that's worked with my city-state clients.

**Jakub Rudnik:** And so that one's been really good.

**Jakub Rudnik:** We like.

**Jakub Rudnik:** Came up with some other ideas to make each call try to be more impactful.

**Jakub Rudnik:** Like one was like, I'll do a conversion analysis and we'll talk conversion each month.

**Jakub Rudnik:** And then there wasn't enough data to like have any meaningful talk.

**Jakub Rudnik:** Like after the first one, you know, it like kind of fell flat.

**Jakub Rudnik:** So I don't know what the other recurring ones, but that one has worked really well.

**Jakub Rudnik:** So just so people aren't doing it, I think it's a valuable one, regardless of the rest of this conversation.

**Jakub Rudnik:** To like something Mara said, I think, but like, I do think there's, and then especially Andy, what you're saying about the, I don't get much at all from the, those daily check-ins, but if they were like, Jessalyn does this where she is sending the agenda for the week over.

**Jakub Rudnik:** And again, there's probably, there's like a lot of noise in there, but if it was just like, here's the flags or here's what we need, like if there were a set four or five questions that you could skim and like, these are the things I'll need to either put out this week or the performance.

**Jakub Rudnik:** And some of them wouldn't have to come from MEs.

**Jakub Rudnik:** Like they could be automated from analytics or something like that, that could just like put.

**Jakub Rudnik:** The core metrics or flags right in front of you.

**Jakub Rudnik:** when you do have deep work, because that's how I find like, okay, have 30 minutes between a call.

**Jakub Rudnik:** Like I can't even get set up to do my deep work because I'm like just every other all day.

**Jakub Rudnik:** But if you had some of that, you could like move some things forward much quicker.

**Jakub Rudnik:** And so when you do have that gap, I think those reports could be setting us better.

**Kyle Gaudreau:** I think there's a lot to unpack with that general theme.

**Kyle Gaudreau:** I've been trying to, I feel like this is related, but I've been trying to get in this cadence now with Carrie and Edasham on like Mondays where, you know, deeper dive on like the key things that are top of mind that are in that vein of like, you know, what are some of like the key blockers, you know, areas where basically what I'm trying to get to is like that they have a clear narrative of like what is going on with each account.

**Kyle Gaudreau:** How does that like relate to the work we're doing each week?

**Kyle Gaudreau:** How does that relate to the discussion in the call?

**Kyle Gaudreau:** That makes it easier for me to.

**Kyle Gaudreau:** Understand, like, where to dive in and help and, like, focus time.

**Kyle Gaudreau:** Because otherwise, if it's just, like, broadly, like, number of articles, I don't really know what to do with that.

**Kyle Gaudreau:** But then I really, I really like is, like, also, like, what are the different things we can automate that are, like, flagging signals that, like, we all may miss because we're all really busy.

**Kyle Gaudreau:** That can be data signals, that can be sentiment signals.

**Kyle Gaudreau:** I really, like, it's something that I just, you know, we've all been so busy and, you know, had to focus on other things.

**Kyle Gaudreau:** But, like, I do think there's some pretty good unlocks in there of, like, how do we flag performance signals that are of a concern?

**Kyle Gaudreau:** Maybe our Atlas work is, like, one of the key prerequisites to making that easier.

**Kyle Gaudreau:** But, like, no doubt, like, there's got to be stuff in those transcripts we can do around sentiment signals.

**Kyle Gaudreau:** Like, if we can, whatever that looks like, it's probably a decent project.

**Kyle Gaudreau:** I don't know who the right engineer is, but I feel like we put our heads together and scoped it.

**Kyle Gaudreau:** We could at least get

**Kyle Gaudreau:** Put it on the roadmap and figure out when it would be helpful.

**Kyle Gaudreau:** Like, for example, where this has been really useful for me, and it's like stupid manual, like for each of these accounts, I've pulled out each transcript.

**Kyle Gaudreau:** Sometimes I'll segment them into different note files.

**Kyle Gaudreau:** I'll upload them into projects.

**Kyle Gaudreau:** I'll then like use that and prompt it to like get like an understanding of like the evolution of the account and like the discussion.

**Kyle Gaudreau:** It's super helpful.

**Kyle Gaudreau:** Like, there's a lot of context in there that, and that's like a super low-fi version of what's possible with this, to be clear.

**Matthew Panzarino:** Yeah, it should be on an internal dashboard, like in an atlas.

**Matthew Panzarino:** It should be a customer sentiment dashboard.

**Kyle Gaudreau:** It was like, hey, 70% of the discussion in this was negative about content quality, you know, or whatever.

**Matthew Panzarino:** Yeah, that's awesome.

**Kyle Gaudreau:** Because then, then we can start to play around with like, how do you flag these things for the directors to not just be reliant on self-reporting from the team, but also like find accountability for the team as well.

**Kyle Gaudreau:** Of like, hey, what's going on with this?

**Kyle Gaudreau:** we have a plan?

**Kyle Gaudreau:** This has been, you know, this has now been talked about for a bit.

**Kyle Gaudreau:** So generally, I'd say like the theme for me around that is like, I think the better we can get away from like the always on noise that isn't super helpful to always understand.

**Kyle Gaudreau:** And that's when it's like obvious, like, oh, , we haven't published anything or whatever.

**Kyle Gaudreau:** It's like, what are the, you know, what are the key things that should be top of mind for each one of these accounts based off a variety of qualitative, quantitative things?

**Andi Bailey:** Hmm.

**Andi Bailey:** I'm trying to think.

**Andi Bailey:** I we would do that.

**Andi Bailey:** Panzar, was thinking about how you had Nana go through, like, all the feedback calls and just take, like, take notes.

**Andi Bailey:** I'm like, could we get an EA just to, like, parse everybody's calls?

**Matthew Panzarino:** Yeah, I mean, we did, we definitely built tools for that.

**Andi Bailey:** mean, by built tools, I mean, we put together a cloud project for those things.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Because we, when, when I took over those clients, asked around, like, hey, how are, how's everybody gathering comments from the calls or comments from the articles?

**Matthew Panzarino:** And people were like, oh, like, copy and paste, or I guess I just, like, write, I remember, or write a sentence.

**Matthew Panzarino:** It was like, really, I'm like, wow, this sucks.

**Matthew Panzarino:** I would never do that.

**Matthew Panzarino:** You know what mean?

**Matthew Panzarino:** Like, no wonder you're, you're at a loss for time.

**Matthew Panzarino:** You're copying and pasting comments out manually to, like, update your artifacts?

**Matthew Panzarino:** That's wild.

**Matthew Panzarino:** And so we just immediately built tools for that.

**Matthew Panzarino:** And I, I have fully credit, like, I just gave Nana.

**Matthew Panzarino:** I spec, was like, Hey, here's what the tool needs to do.

**Matthew Panzarino:** Here's what, here's the logic.

**Matthew Panzarino:** And then she went and did those things.

**Matthew Panzarino:** Then I tested them and I think they work great.

**Matthew Panzarino:** But yeah, at the very least, you have a cloud project that you could throw.

**Matthew Panzarino:** And its only purpose is to do that sentiment analysis for each of the client calls and to gather feedback.

**Matthew Panzarino:** So we use the closest analogy we have right now is our artifact updater cloud project.

**Matthew Panzarino:** So we have a cloud project for each client that all it does is update their artifacts.

**Matthew Panzarino:** So we have taught it what those artifacts look like, what we are looking for in terms of updating the artifacts.

**Matthew Panzarino:** We are able to sort of have the exist and we refresh all of our artifacts.

**Matthew Panzarino:** time we update them, we refresh them in all our cloud projects and in Atlas.

**Matthew Panzarino:** And we say, Hey, this is the latest version of the, the artifacts.

**Matthew Panzarino:** So remember that.

**Matthew Panzarino:** And I was like, yeah, yeah, I remember that.

**Matthew Panzarino:** I got those.

**Matthew Panzarino:** I know what you're doing.

**Matthew Panzarino:** And then we give it the comment, the scrape comments and we.

**Matthew Panzarino:** Well, the comment scraper separately, but it basically scrapes the context in which the comment was left, the comment itself, and the commenter.

**Matthew Panzarino:** And then it basically takes those and ingests them and says, hey, based on this, I can suggest these enhancements to the writing guidelines, or I believe these are already covered by these writing guidelines.

**Matthew Panzarino:** In both cases, it's an action item for us.

**Matthew Panzarino:** We either decide whether to integrate those if it says it's net new, or we say, well, they're still leaving the feedback, and you say it's in there, so semantically, this is probably wrong, right?

**Matthew Panzarino:** Like, we need to improve this prompt, so to speak, or this instruction.

**Matthew Panzarino:** So that process is done every time, and we do it with client calls, too, because, like, a lot of times, they'll jabber on client calls about the article, and I'm like, oh, it would have been great if you'd left this as a comment, because then we could just scrape it.

**Matthew Panzarino:** But they didn't, so we take the transcript of that call, put it in the artifact updater, and say, hey, they gave us feedback.

**Matthew Panzarino:** Could you look at this and see what feedback they gave us, and if it's viable for ingestion?

**Matthew Panzarino:** So you can see.

**Matthew Panzarino:** It a branch of that project where it would just be like, hey, this is a recent client call.

**Matthew Panzarino:** Here's how we think about sentiment, right?

**Matthew Panzarino:** Like, here's a document on sentiment analysis, and here's our spec for that.

**Matthew Panzarino:** Take a look at this call.

**Matthew Panzarino:** How are they feeling about the content?

**Matthew Panzarino:** Do they feel positive or negative about it?

**Matthew Panzarino:** Are we doing, you know, what do you feel our relationship is at?

**Matthew Panzarino:** Have they mentioned more pros or cons with our, you know, whatever.

**Andi Bailey:** So that seems like a version of that report.

**Andi Bailey:** Yeah.

**Mara Leighton:** I'm curious.

**Mara Leighton:** Sorry.

**Andi Bailey:** Go ahead, Andi.

**Andi Bailey:** No, go ahead.

**Andi Bailey:** I didn't, I don't have anything.

**Mara Leighton:** I was going to ask, and it sounds like maybe this is like emergent, or maybe you're not doing it exactly this way, but I'd be interested, Panzar, in like, are you doing customer sentiment analysis per call?

**Mara Leighton:** And are you tracking like aggregate?

**Mara Leighton:** Because I feel like I wouldn't, my initial assumption would be like aggregate if I'm dropping like all the calls into the cloud project.

**Mara Leighton:** And I ask it generally for analysis.

**Mara Leighton:** I feel like I wouldn't trust it, but if I do it.

**Mara Leighton:** I'm and I'm

**Mara Leighton:** Per call, and then roll up in some way to like a here's the last month sentiment, and I trust that, but yeah, are you doing it per call and aggregate?

**Matthew Panzarino:** I'm not doing that at all.

**Matthew Panzarino:** I'm not doing sentiment analysis at all, but yes, you're right.

**Matthew Panzarino:** That's it.

**Matthew Panzarino:** That's the way I'd approach it.

**Matthew Panzarino:** The sentiment analysis part is I'm mentioning it was like it could be a fork of the project that we use to up the artifacts because we're already adjusting the call and asking it for commentary, and then we could say, hey, what is the sentiment around this commentary?

**Matthew Panzarino:** You know what I mean?

**Matthew Panzarino:** So we are not doing that, just to put that out.

**Mara Leighton:** We're not doing it, but I think you're right.

**Mara Leighton:** Yeah.

**Mara Leighton:** Yeah, cool.

**Mara Leighton:** Sounds good.

**Matthew Panzarino:** My sentiment analysis is just me.

**Matthew Panzarino:** I'm the only stakeholder on my side, so I'm the only person all of our clients talk to, so I know, you know.

**Mara Leighton:** Totally.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** We'd also ideally, I'd say, not to get us too down the rabbit hole in scoping this live, but like where does this information live?

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** So...

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** You know, it shouldn't just be contained in cloud, like we should all know it, it should be a place where Marcel can pop in if he needs to, it can connect to your eventual, like weekly reporting you do, Andy, in some meaningful way.

**Kyle Gaudreau:** Obviously, these are like down the road things, but there's just all these different, like if I'm thinking about how to like make this a more repeatable, scalable system, like there's no doubt some time savings into just like how we synthesize these insights.

**Matthew Panzarino:** We'll have to start little and build bigger, but.

**Matthew Panzarino:** It's so important, I think, for, for managing large numbers of clients, and if you think about this in terms of Atlas eventually being able to support other business processes, it's not like any client management for, or sales process wouldn't want this, you know, like, oh, what's the sentiment across all of our sales calls, you know.

**Andi Bailey:** What about HubSpot?

**Andi Bailey:** I mean, like, yeah, I think there are, we should look into some CS tooling, like there's, also, what is HubSpot?

**Andi Bailey:** Like, doesn't HockeyStack.

**Andi Bailey:** HockeySack, I know, is, like, a sales tool, but I wonder if they have, like, some stuff in there.

**Andi Bailey:** Like, there's got to be, maybe there's just a tool for this.

**Matthew Panzarino:** Yeah, there might be.

**Andi Bailey:** So, okay, I'll start doing some research there.

**Andi Bailey:** This was really helpful.

**Andi Bailey:** And, yeah, like, I want to, again, we've had this conversation a million times, but this was really useful feedback.

**Andi Bailey:** And I think, like, this question is the main question of, like, how do we make sure that you guys aren't just, like, joining more calls and doing less strategic work as we scale up?

**Andi Bailey:** Because, obviously, like, that's what's happening right now if we keep adding accounts the way that we are.

**Andi Bailey:** Okay, thanks for your time, guys.

**Andi Bailey:** Good conversation.

**Andi Bailey:** See you.
