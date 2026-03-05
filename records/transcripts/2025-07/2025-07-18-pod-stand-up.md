# Pod stand-up

<metadata>
date: 2025-07-18
time: 13:16 UTC
duration: 19 minutes
organizer: Saskia Wartnaby
participants: Darrell Etherington, Ehtisham Hussain, Feyisayo Odedeyi, Joe Sovar, Saskia Wartnaby
fathom_recording_id: 75051963
fathom_url: https://fathom.video/calls/355079532
share_url: https://fathom.video/share/YdJp81yCfYsAdegns_3r3XxKEUNx4SsJ
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

GrowthX's content delivery team reviewed critical improvements to Atlas — Darrell shared comprehensive feedback showing Atlas heavily underperforms Cloud Projects due to constraining configuration elements that override Claude's native capabilities. Engineering is removing these constraints and shipping a new chat interface, with the assignment direction feature now actually functional. On the client side, Town and Engine are pausing at the content management layer with Darrell acting temporarily, while Aimbit is ramping fully. Team is experimenting with Cloud Projects for better output quality and seeing success with detailed outlines in assignment briefs.

---

## Context

This is the weekly stand-up for GrowthX's content delivery pod — the team responsible for using Atlas (GrowthX's proprietary content generation platform) to produce articles and content for clients. The team includes content operations (Ehtisham), writers (Saskia, Joe), account managers, and engineers (with input from the Atlas engineering team). The meeting happened as the team was dealing with significant performance gaps between Atlas and Anthropic's Cloud Projects, which prompted engineering to conduct a thorough review and plan substantial improvements. New clients (Town, Engine, Aimbit) are ramping during this period, and the team is working with clients like Aftershoot and Prophecy on content strategy.

---

## Relevance

**To GrowthX Delivery:**
- Atlas performance crisis: overconfigured constraints (keyword stuffing, hard-coded elements) make it worse than Claude alone; engineering removing these, shipping chat interface and functional assignment direction feature
- Cloud Projects outperforming Atlas 10x+ on output quality and speed; team adopting Cloud Projects workflow for optimal results
- Detailed outlines in assignment briefs (tested by Saskia) significantly improve output; Ask.ai outline generation coming soon to Atlas
- New onboarding procedures: Town and Engine pausing at content management layer; Aimbit demanding but communicative client requiring specific product terminology training
- Aftershoot feedback mirrors Atlas issues; expected improvements from assignment direction fix will address their concerns

**To GrowthX Business Development:**
- Aimbit ramping fully with demanding requirements but positive relationship; opportunity to demonstrate improved tooling capabilities
- Aftershoot account health dependent on Atlas improvements; client satisfaction at risk without near-term performance gains
- Prophecy approving new thought leadership topics; Saskia's Cloud Projects experiments show feasibility for this content type

---

## Overview

- Atlas (internal tool) performance issues identified; engineering team implementing fixes based on comprehensive feedback
- New clients (Town, Engine, Aimbit) being onboarded with adjusted processes
- Cloud Projects outperforming Atlas in content generation; team adapting workflows
- Significant improvements to Atlas expected soon, including chat interface and better assignment direction handling

---

## Key Topics

### Atlas Performance Issues and Improvements

  - Darrell provided extensive feedback on Atlas's poor performance compared to Claude Projects
  - Engineering team acknowledged issues; removing constraining elements to leverage Claude's improved capabilities
  - New chat interface being tested for more intuitive user experience
  - Assignment direction feature now functional, honoring user input
  - Keyword stuffing and hard-coded elements causing over-fluffed content; to be stripped out
  - Ask.ai feature for outline generation in assignment direction coming soon

### New Client Onboarding

  - Town and Engine: Pausing at CM layer; Darrell acting as CM temporarily
  - Aimbit: Full ramp-up approved; demanding but communicative client
  - Specific product terminology important for Aimbit; team learning to adapt

### Content Generation Workflows

  - Team experimenting with Cloud Projects for better results
  - Saskia finding success with detailed outlines in assignment briefs
  - Joe reported significant improvements in Atlas's AI/SKI feature for editing

### Aftershoot Client Update

  - New topics and lighter outlines being developed (10 planned for today)
  - 3 approved outlines for Jess to work on
  - Some articles require editing, one needs complete rewrite

### Prophecy and Aimbit Progress

  - Both clients approved new topics, leaning towards thought leadership
  - Saskia to work on Prophecy articles next week
  - Fey to start on Aimbit articles with approved topics

### Cloud Account Access Issues

  - Some team members experiencing expired links for Cloud.ai access
  - Darrell to investigate and provide updated access information

---

## Action Items

**Darrell Etherington (GrowthX)**
- Run experiments with tricky content in Atlas & Cloud Projects. Send results to engineering team.
- Post and pin Cloud.ai login instructions in team channel.

**Ehtisham Hussain (GrowthX)**
- Create 10 new topics and lighter outlines for Aftershoot. Send to client.
- Edit 2 Aftershoot articles. Rewrite 1 Aftershoot article with new structure.
- Review Aimbit account status. Check article count, delivery rate, etc.
- Edit 3rd Aimbit article. Send message to client regarding edits.

---

## Transcript
**Saskia Wartnaby:** Hi, Feyi, how are you?

**Saskia Wartnaby:** Yeah, I can see you now, Darrell.

**Darrell Etherington:** Hey, yeah, I think it's because I tried to accidentally join on another browser while I was trying to get Fathom in, but that worked.

**Darrell Etherington:** Thanks, everybody, for joining. Happy Friday.

**Darrell Etherington:** Okay.

**Darrell Etherington:** And yeah, let's quick rundown on some updates.

**Darrell Etherington:** I'll just start from my side because I think it will affect everybody, but the engineering team had me do a bunch of generation this week and record all of my thoughts, and my thoughts were not good or happy with them because it's in a really bad state, really bad state.

**Darrell Etherington:** So they had me and Matthew both do that, and I think I was shocked at how bad it

**Darrell Etherington:** It still was, so, but that was well heard, like Daniel yesterday responded after watching all my looms and was like, okay, this is perfect, this is the kind of comprehensive feedback we were looking for, we're going to change a whole bunch of stuff to fix this.

**Darrell Etherington:** And a lot of it will be actually kind of removing some of the things that they put in place to direct the output, because I think what he communicated to me was that he didn't realize how powerful and good Claude had become since.

**Darrell Etherington:** So, ironically, a lot of the stuff that they were putting on top of it was, yeah, like Ehtisham said, like, was actually, like, making it worse than just the thing as it operates, right?

**Darrell Etherington:** And you can go watch the looms, too, if you are curious, but, like, basically, I was just running in parallel the same generation in Atlas and also in Claude Projects, like, fully popular.

**Darrell Etherington:** related with all of the client artifacts and any other supplemental documents that I thought might be useful.

**Darrell Etherington:** One in particular, like, we have this client town that's coming on and they're doing tax stuff.

**Darrell Etherington:** And they were like, we would really like to address the big, beautiful bill, but it's complicated and we don't understand necessarily because it's a moving target.

**Darrell Etherington:** But like cloud projects would use a combination of like a bunch of best in class documents of like what the current state is and implications from like, certified accountants and then also would go out to the web to find most recent information and came up with stuff that was very like factual accurate, right?

**Darrell Etherington:** Like once I went through and fact checked it.

**Darrell Etherington:** So, you know, I articulated all that for them because I think they need sort of the similar thing where it's kind of acting like a closed notebook, but can go out to the web when it wants to as well.

**Darrell Etherington:** And rather than just right now, kind of like very like narrowly and specifically calling.

**Darrell Etherington:** And artifacts in and then using the artifact on that one particular task and then sending it away.

**Darrell Etherington:** Maybe you saw some of the updates from Matthew too.

**Darrell Etherington:** So those are some of the like more immediate, hopefully, like pain relieving steps that they took, which was, I mean, the big one was the assignment direction was not used.

**Darrell Etherington:** It was any effect that it had was strictly placebo effect on the user side.

**Darrell Etherington:** It was just not used.

**Darrell Etherington:** So that's a huge change.

**Darrell Etherington:** And then I don't know that they haven't shared any of this either, but I've seen it from Brad, who is, you know, one of the lead engineers over there.

**Darrell Etherington:** But they have like, they're testing a new interface that is like literally a chat interface.

**Darrell Etherington:** So it has a box and it's like, hey, what would you like to do today?

**Darrell Etherington:** And then you kind of like say, I want to write an article about blah, blah, blah.

**Darrell Etherington:** And then it goes from there, right?

**Darrell Etherington:** And taps the pipeline.

**Darrell Etherington:** So lots of big quality of life improvements coming and hopefully some of these will help sooner rather than later.

**Darrell Etherington:** Because, yeah, it was just immediately apparent once you start getting into it.

**Darrell Etherington:** It's like one is like doing something with one hand tied behind your back, and the other is like doing it with like a full service team at your disposal, right?

**Darrell Etherington:** Like it's night and day.

**Darrell Etherington:** So I think that's good news.

**Darrell Etherington:** Stay tuned for more out of that.

**Darrell Etherington:** And I'm going to continue to do some stuff here.

**Darrell Etherington:** And then if so, if you have anything tricky that you can send it my way and I'll run some experiments as well and use that to further inform them.

**Darrell Etherington:** I'm talking to this afternoon, but then I'm going out there next week.

**Darrell Etherington:** So that's another update for me.

**Darrell Etherington:** They'll be in San Francisco next week working on PT.

**Darrell Etherington:** But typically when I'm out there in PT, I still can't help but wake up on like ET hours and I don't really adjust anymore.

**Darrell Etherington:** So I should be around roughly the same time as I usually am.

**Darrell Etherington:** Okay.

**Darrell Etherington:** And then, yeah, other than that, like we went back and forth on how exactly we would be adding these new clients.

**Darrell Etherington:** But town and engine are.

**Darrell Etherington:** In terms of adding us to it, we're just still pausing at the CM layer because I'm acting in that capacity for now, but we'll probably have a changed way of doing that.

**Darrell Etherington:** I imagine we'll start bringing in CMs to do generation next week, but I'll confirm next week.

**Darrell Etherington:** And then the other one is Aimbit, and we are ramping, we can ramp fully on them.

**Darrell Etherington:** They're a demanding client, interesting client, but a very communicative client, so I'm hopeful that that will help also with this.

**Darrell Etherington:** then, again, in combination with this thing, because they have really specific ways they want to talk about the product and the specific, technically challenging product.

**Darrell Etherington:** But if we do more of this stuff that we can do in cloud projects in Atlas, then it should be, honestly, no problem.

**Darrell Etherington:** So, yeah, let's hope that works out.

**Darrell Etherington:** Cool, yeah, that's all for me.

**Darrell Etherington:** But, yeah.

**Darrell Etherington:** Open up the floor.

**Darrell Etherington:** Anybody else have anything they wanted to chat about this week?

**Darrell Etherington:** So I think we discussed after truth in detail yesterday.

**Ehtisham Hussain:** So I'm just going to, like today, I'm just going to come up with new topics for them as well as the new lighter outlines that we discussed with them.

**Ehtisham Hussain:** So hopefully I'm just going to hit them with 10 outlines today.

**Ehtisham Hussain:** And yeah, then Jess has three articles, three approved outlines that she's going to work on.

**Ehtisham Hussain:** Plus, I have a couple of articles that I need to edit and then one that needs like a complete rewrite, because they gave a new structure to it.

**Ehtisham Hussain:** But hopefully I'll tackle that today as well.

**Ehtisham Hussain:** With AIMBIT and Prophecy, the good thing is both parties approved the new topics that we sent them.

**Ehtisham Hussain:** So, and they're like more leaning towards thought leadership, especially the prophecy new topics.

**Ehtisham Hussain:** So I'm curious to see how Atlas is going to perform on at that front.

**Ehtisham Hussain:** So Saskia is going to pick that up next week, and then Fey can get started on the 8-bit articles that we have.

**Ehtisham Hussain:** We have a bunch of approved topics, so plus I need to get a more kind of a lay of the land.

**Ehtisham Hussain:** When it comes to 8-bit, I need to see what condition the account is in, how many articles we have delivered, how many have we been delivering, etc.

**Ehtisham Hussain:** I had three of their articles with me that I needed to edit, so I edited two of them yesterday.

**Ehtisham Hussain:** And then the third one, I'm going to edit right now after this call, and then I'm going to send them a message.

**Ehtisham Hussain:** So their comments were like, I feel like they really know their product inside out, and that's why they are very particular about how we use different phrases and different terms in there.

**Ehtisham Hussain:** And that's something that I think they are very communicative about it, plus people learn over time how they use different terminologies.

**Ehtisham Hussain:** that should be.

**Ehtisham Hussain:** That should work out.

**Darrell Etherington:** Yeah, I think on the after shoot, you reminded me, a lot of their comments, that's an interesting call too, if people want to go watch it, I recommend.

**Darrell Etherington:** Uncomfortable, I think.

**Darrell Etherington:** But their comments were, like, reading between the lines were all the same feedback I had about Atlas, basically.

**Darrell Etherington:** So, I think there's a lot we can do there with, hopefully, some of the fixes that we've made, particularly around assignment direction.

**Darrell Etherington:** Now that that will actually be honored, hopefully that can help there significantly.

**Darrell Etherington:** So, maybe try rerunning with some of that.

**Saskia Wartnaby:** I chatted with Ehtisham yesterday about all of this, and I also sent a ticket last week about giving the assignment brief quite a detailed outline. Yesterday I did try and create an article for Prophecy in Atlas, and I give ChatGPT everything that Atlas had, and it generated better articles for me.

**Saskia Wartnaby:** I've been taking those, and I've been putting them in today.

**Saskia Wartnaby:** Yesterday, I put that into the assignment brief, and it actually flowed through all the way to the end.

**Saskia Wartnaby:** Like, it kept an outline, and it filled it in.

**Saskia Wartnaby:** It's still a bit weird with formatting and the length of the content and stuff, but I'm fixing that.

**Saskia Wartnaby:** But it does seem to be getting a little bit better.

**Saskia Wartnaby:** So, yeah, I'm having, in summary, having a little bit of success with putting a nice outline with instructions in the assignment brief.

**Saskia Wartnaby:** Yeah, it is honoring that.

**Darrell Etherington:** And then the thing they want to do now, too, because they don't love that the stuff is being generated outside and then brought in for the outline.

**Darrell Etherington:** But I don't know if they pushed this yet, but they're working on a fix whereby, in the assignment direction, you can use the Ask.ai feature to have it generate an outline based on a prompt.

**Darrell Etherington:** So you technically can hopefully do that right there, and it will have the same exact.

**Darrell Etherington:** Output effect as if you were doing it in ChatGPT or COD, right?

**Darrell Etherington:** I'll definitely see if that comes in on Prophecy.

**Saskia Wartnaby:** Yeah, I can't remember if it's actually live.

**Darrell Etherington:** I don't think it is yet, but as soon as it is, I'll let you know, or they'll put it in Learning Atlas or somewhere else.

**Darrell Etherington:** Great.

**Saskia Wartnaby:** Cool.

**Saskia Wartnaby:** Thank you so much for doing all of that, because, Lish, I think I sent you that message about my thoughts on it, and it seems like you've discovered the same thing, and I'm glad that they've got all that feedback.

**Darrell Etherington:** Well, yeah, it wasn't, it wasn't, like, unavailable information, which is part of the frustration, but, you know, sometimes people just need to be told in the right way.

**Saskia Wartnaby:** Yes, exactly.

**Saskia Wartnaby:** Yeah, so thank you for doing that.

**Darrell Etherington:** That was, that also, the length thing was also the big thing that I pointed to them, because it was, I didn't, my testing methodology was, like, I'm not going to do all the things that you ask us to do up front to try to massage this, because that's not a fair comparison.

**Darrell Etherington:** A real comparison is,

**Darrell Etherington:** I spend two minutes at the start of the pipeline, and I spend two minutes on the prompts in cloud projects, it's equivalent time in, and then I don't touch anything, and then I get my result, right?

**Darrell Etherington:** So which one wins in that scenario?

**Darrell Etherington:** That's a fair comparison.

**Darrell Etherington:** Not a, like, do I spend an hour and a half trying to set up the workflow at the beginning so that it produces something okay at the end, right?

**Darrell Etherington:** That's exactly it.

**Darrell Etherington:** I was spending more time in Atlas trying to get a better result than it was just to go into cloud and give it the same stuff, yeah, essentially.

**Darrell Etherington:** Yeah, so they, because the one thing, they kept saying, oh, well, you didn't try to affect that, because I said, every time it was three, three to four thousand words, and I'm like, okay, and they're like, you didn't try to adjust the length, and I'm like, yeah, I didn't, I didn't in cloud either, and it gave me 1,200 to 1,500 word articles every single time, so what's going on?

**Darrell Etherington:** but it was, it's the keyword stuffing, and the, like, the hard-coded, to Edisham's point earlier, like, all the hard-coded stuff that they, in,

**Darrell Etherington:** This, that it includes, that over-fluffs it now.

**Darrell Etherington:** So, once they strip out some of that rigging, it'll work better.

**Darrell Etherington:** Okay, anything else?

**Darrell Etherington:** We kind of sidetracked there, Ehtisham.

**Darrell Etherington:** Were you finished your thought on?

**Ehtisham Hussain:** I just remembered the Cloud account links that you sent out in email expired for me. I got two different emails, but when I clicked the link, it had already expired. Please send those out again.

**Saskia Wartnaby:** Yeah, it's weird, Darrell. I keep getting emails saying you need to join this, you need to sign up. And when I click on it, the link just doesn't work, or it says it's already been used.

**Darrell Etherington:** Yeah, I just used it yesterday and this morning and it worked fine. But let me investigate. I don't have access to the Cloud accounts for the pod yet. I have access to the group, so I can do member additions. You should have access, Feyisayo. You're missing the actual email and instructions. I'll post them and pin them to the channel — they're buried somewhere in Slack where Yusuf had outlined them for us.

**Feyisayo Odedeyi:** Okay, let me see.

**Joe Sovar:** I want to say that I tried the AI feature, SKI feature, today on my articles, and it's excellent, really.

**Joe Sovar:** It works.

**Joe Sovar:** The edit part is much faster now. You don't have to go to ChatGPT and turn this into bullet points or something — Atlas will do that for you. It can also turn some parts into H3s for better readability.

**Darrell Etherington:** Yeah, I was using it a bit and it was doing some unusual activity but working a lot better than before. I don't love that it does the track changes thing and requires an approval flow. When I do Cloud edits, it just flows the edits right into the live document. I much prefer it, but the track changes approach would highlight in green and leave a lot of unintentional detritus. The other big known bug is that external links is broken.

**Joe Sovar:** Yeah, they fixed that. It gave me a clean text after my prompt.

**Joe Sovar:** Yeah, they're fixing it hour by hour, so a lot of changes going on.

**Darrell Etherington:** Yeah, I had it cut the thing in half very aggressively. So that also wasn't perfect, but at least it did cut. A lot of the stuff is like that — you try it, it won't work, then you don't want to use it anymore, but they fix it the next day.

**Joe Sovar:** Yeah, because it's faster with some other tools when you know that it will work.

**Darrell Etherington:** Okay, I'm going to go ahead and try to get this pod thing fixed because that is important for all of us right now. All right, well, thanks, everybody. I hope Atlas is much better by this time next week and we're all celebrating it and using it exclusively.

**Ehtisham Hussain:** Enjoy your weekend. Bye.
