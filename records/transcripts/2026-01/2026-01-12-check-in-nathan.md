# Check-in: Nathan

<metadata>
date: 2026-01-12
time: 22:01 UTC
duration: 22 minutes
organizer: nathan@growthx.ai
participants: Matthew Panzarino (matthew@growthx.ai), Nathan Navidzadeh (nathan@growthx.ai)
fathom_recording_id: 113656376
fathom_url: https://fathom.video/calls/527925715
share_url: https://fathom.video/share/MDxzMNet8sz8SoxJxFJhLh42BFyWLoSh
source: fathom
enriched_on: 2026-02-28 02:14 UTC
</metadata>

---

## Summary

Matthew and Nathan discussed capacity improvements and workflow bottlenecks. Nathan's Gentic pipeline cut pre-processing time from 45 minutes to 5–10 minutes, freeing capacity for the upcoming programmatic page rollout. The primary remaining bottleneck is manual meta-tagging; Matthew advised filing engineering tickets to automate both meta-tagging and post-processing workflows, leveraging the new engineering capacity. Recent DataGrid team departures (Mara, Vivek, Nika) are unrelated individual career moves with no bearing on client satisfaction.

---

## Context

Nathan joined GrowthX to manage content production workflows. He recently implemented Gentic pipelines to automate article outline generation, cutting preprocessing time dramatically and enabling a new programmatic page expansion. However, he still spends 30–45 minutes per article on post-processing tasks. His key concern is whether recent departures from the DataGrid team indicate underlying account instability or client dissatisfaction. Matthew is the VP or senior leader with visibility into client health and engineering capacity allocation. The conversation reflects GrowthX's strategy of automating repetitive manual processes by filing engineering tickets instead of patching workarounds locally.

---

## Relevance

- **Workflow Automation Strategy**: Demonstrates GrowthX's shift from local workarounds to systematic engineering investments for team efficiency.
- **Bottleneck Identification**: Meta-tagging and post-processing manual work represent the current capacity constraint for content production scaling.
- **Agentic Workflow Pattern**: Illustrates the preference for agent-based solutions (with rubrics and iteration) over deterministic pipelines for quality control.
- **Team Stability & Trust**: Addresses concern about DataGrid departures and affirms that account health is strong despite turnover.
- **Engineering Capacity & Triage**: Reflects the importance of proactive ticket filing to prioritize work when engineering resources become available.

---

## Overview

- **Capacity is good:** Gentic pipelines cut pre-processing from 45 mins to 5–10, freeing up time for a new programmatic page rollout.
- **Meta-tagging is the top bottleneck:** Nathan's manual Claude process is inefficient; the solution is to file a ticket for an agentic pipeline workflow.
- **File tickets for process automation:** With new engineering capacity, Nathan should file tickets to automate manual processes, starting with meta-tagging.
- **DataGrid team changes are unrelated:** Recent departures (Mara, Vivek, Nika) are individual career moves, not a sign of client issues.

---

## Key Topics

### Capacity & Workflow Efficiency

  - Gentic pipelines cut pre-processing time from \~45 mins to 5–10 mins, resolving a capacity crunch.
  - This efficiency gain came just before the rollout of programmatic pages.
  - Post-processing time remains 30–45 mins/post, creating the next bottleneck.

### Bottleneck 1: Meta-Tagging

  - The pipeline's deterministic meta-tagging is low quality, forcing a manual workaround in Claude.
  - **Current Process:**
      - Feed article to a Claude project.
      - Use a template prompt for 5 options each for slug, meta title, meta description, and article title.
      - Copy-paste into a visual tool (e.g., Fangools) to check display in Google search results.
  - **Solution:** File an engineering ticket for an agentic workflow.
      - **Rationale:** An agent can iterate and self-correct against a rubric (e.g., character counts), unlike the current deterministic process.
      - **Ticket Details:**
          - Include the Claude prompt and examples of desired outputs.
          - Request multiple options for selection.
          - Suggest a visual preview feature (P2 priority).

### Bottleneck 2: Manual Post-Processing

  - Nathan uses a "bulk prompt" in Atlas to proofread articles for style (e.g., em dashes).
  - **Solution:** Automate this process by filing a ticket.
      - **Rationale:** Automate the most reliable steps first to get quick wins.
      - **Strategy:** Compartmentalize the prompt into separate steps to isolate errors and make troubleshooting easier.

### DataGrid Team Stability

  - Nathan asked about recent departures (Mara, Vivek, Nika) from the DataGrid team.
  - Matthew confirmed the departures are unrelated individual career moves, not a sign of client issues.
  - DataGrid is an important client, and Matthew has not received any negative feedback from the account's Engagement Manager.

---

## Action Items

**Nathan Navidzadeh (GrowthX)**
- File engineering ticket for meta-tagging workflow: Include Claude prompt and examples of desired outputs. Request agentic workflow with 3–5 options for slug, meta title, meta description, and article title. Priority P1 for core functionality; P2 for in-situ visual preview (SERP preview via Fangools).
- Audit post-processing prompts and file engineering ticket for agentic automation: Identify deterministic, low-risk steps suitable for pipeline automation. Compartmentalize steps to isolate errors. Maintain manual review for high-difficulty tasks.

---

## Transcript

**Nathan Navidzadeh:** How's it going? I'm all right. A bit under the weather today, actually, but...

**Matthew Panzarino:** Oh, I'm sorry about hearing that.

**Matthew Panzarino:** It is the season.

**Matthew Panzarino:** It's going around like wildfire right now.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** Yeah, we can say that globally, even, which is crazy, right?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah, those pesky vaccines, apparently, they're still important.

**Matthew Panzarino:** Give me one second.

**Matthew Panzarino:** I'm actually going to refresh my coffee.

**Nathan Navidzadeh:** Sorry.

**Nathan Navidzadeh:** No worries.

**Nathan Navidzadeh:** Yeah, go for it.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Sorry for the 30-second timeout.

**Matthew Panzarino:** I should have done it before, but I had been back to back, and I...

**Matthew Panzarino:** Missed my window, so sorry.

**Nathan Navidzadeh:** I'm easy.

**Matthew Panzarino:** Don't worry about it.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** So obviously catch up.

**Matthew Panzarino:** We don't have to make it too laborious.

**Matthew Panzarino:** I know you're not feeling that great, but I did want to hear from you just kind of like how are you feeling about capacity?

**Matthew Panzarino:** How are you feeling with your accounts?

**Matthew Panzarino:** We can kind of walk through them a little bit.

**Matthew Panzarino:** I want to help you clear blockers, obviously, and also strategize about how to do that properly and all of that.

**Matthew Panzarino:** Improve your life and your efficiency, etc.

**Nathan Navidzadeh:** So happy to about those things.

**Nathan Navidzadeh:** Yeah, no, totally.

**Nathan Navidzadeh:** I mean, honestly, everything you've been pushing the last month or so for getting things on Gentic and all the pointers on how to get the artifacts ready and working well and checking the issues between the artifacts and all that stuff using the tool.

**Nathan Navidzadeh:** And it looks like I did all of that before the holidays and got a Gentic running about a week before the holidays and have been using that ever since.

**Matthew Panzarino:** Okay, cool.

**Nathan Navidzadeh:** Problem free.

**Nathan Navidzadeh:** So my capacity is good.

**Nathan Navidzadeh:** It freed up just in time.

**Nathan Navidzadeh:** Because we're just about to roll out programmatic pages.

**Nathan Navidzadeh:** And I was like, okay, if I can't cut down my time, I don't know how I'm going to do these programatics when they come out.

**Matthew Panzarino:** So that's all good now.

**Matthew Panzarino:** So that's good.

**Nathan Navidzadeh:** In terms of, I mean, there's always things that I can improve on it.

**Nathan Navidzadeh:** Because I do still find myself spending 30 to 45 minutes on post.

**Nathan Navidzadeh:** But my time previously on setting up an outline, because we were using the deterministic pipelines, took me like 45 minutes to also set that up.

**Matthew Panzarino:** Yeah, so you had like the 45 minutes pre and then the post.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** And now it's like, you know, five to 10 minutes pre.

**Nathan Navidzadeh:** Because I already have the keyword and the topics that I want set up in content-wise.

**Matthew Panzarino:** Before you fire it off, right?

**Nathan Navidzadeh:** Tweak, yeah.

**Nathan Navidzadeh:** mean, I have like a template that I paste in.

**Nathan Navidzadeh:** then I just tweak that a little bit.

**Matthew Panzarino:** And now you can define that template in the pipeline.

**Nathan Navidzadeh:** Yeah, yeah, yeah.

**Nathan Navidzadeh:** I tried to do that.

**Nathan Navidzadeh:** Oh, no, I did do that.

**Nathan Navidzadeh:** I tried to do that, and I did it.

**Nathan Navidzadeh:** Yeah, so it's in the pipeline now, too.

**Matthew Panzarino:** yeah.

**Matthew Panzarino:** And the only reason I mentioned that is if it's relatively similar with some tweaks, there's no sense just having to paste it.

**Matthew Panzarino:** You can put it in.

**Matthew Panzarino:** Obviously, if it's completely different every time where they're like, you're doing a variety of different articles, it makes total sense to just put something new in there each time.

**Nathan Navidzadeh:** No, no, no, yeah.

**Nathan Navidzadeh:** And I did exactly that.

**Nathan Navidzadeh:** So now it automatically populates in the assignment directions with that, and I just tweak the placeholders for whatever I want.

**Matthew Panzarino:** So that's good to go.

**Matthew Panzarino:** And if you had that, like, so if you had to characterize your biggest, I don't know, your biggest win that you sense is just over the horizon, if only you could get X off of your post-processing plate, what is that?

**Matthew Panzarino:** What's like your biggest comes up there?

**Nathan Navidzadeh:** Yeah, was trying to figure that out.

**Nathan Navidzadeh:** So the biggest ones right now, well, they feel big.

**Nathan Navidzadeh:** I didn't time it, but I feel like I spent too much time on meta.

**Matthew Panzarino:** Meta title, meta description.

**Nathan Navidzadeh:** And I don't know if that's just previous training in me that's like, no, man, you got to make sure you got good meta stuff going on that I spent too much time.

**Matthew Panzarino:** Your pipeline does not generate that for you?

**Nathan Navidzadeh:** It does.

**Nathan Navidzadeh:** It does and I don't like it.

**Nathan Navidzadeh:** But we had a previous method.

**Nathan Navidzadeh:** Sometimes I like it.

**Nathan Navidzadeh:** Sometimes I like the meta descriptions that it gives me.

**Nathan Navidzadeh:** But it's not my favorite for it.

**Nathan Navidzadeh:** And I don't know what's happening behind the scenes for it to generate them.

**Nathan Navidzadeh:** I didn't look that far into it.

**Nathan Navidzadeh:** But we have what I essentially do is I feed the article to my project in Claude.

**Nathan Navidzadeh:** And then I have a template prompt that I just send it all the time.

**Nathan Navidzadeh:** And then it gives me five options for Slug, five options for the meta title, for the meta description, and for the actual article title.

**Nathan Navidzadeh:** And then it also gives me its recommendation for the best one between those five.

**Nathan Navidzadeh:** And the prompt itself is like somewhat elaborate.

**Nathan Navidzadeh:** I mean, there's one that Vivek gave me.

**Nathan Navidzadeh:** It's got like multiple.

**Nathan Navidzadeh:** Bullet points of what it wants the meta to do, like include this, include that, try to make it punchy, try to do that.

**Matthew Panzarino:** Two paths for you here to get this off your plate.

**Matthew Panzarino:** You have two options, two paths before you.

**Matthew Panzarino:** One is take that prompt and some good results that you've liked, a good run of it, and put them in a ticket and say, hey, I don't like the current meta tagging that's in the pipeline.

**Matthew Panzarino:** Could we add a workflow that does something like this, or could we use an existing workflow to generate this?

**Matthew Panzarino:** The answer to that is yes, by the way, but you do not have to do it, right?

**Matthew Panzarino:** You can file your ticket and then go about your day, and then the client ops engine team will triage that and get to it.

**Matthew Panzarino:** We just hired a couple of extra people.

**Nathan Navidzadeh:** Kirkland's team is growing.

**Matthew Panzarino:** They have the capacity now to get these reps in the tank for you, so it's not like you and Nana kind of like trying to figure it out, you know, or cobble something together.

**Matthew Panzarino:** Not that that's a bad thing.

**Matthew Panzarino:** It's just like, you know, you have work to do, right?

**Matthew Panzarino:** The, so that's path one, is you can do that.

**Matthew Panzarino:** The second path...

**Matthew Panzarino:** Fathom is you could file that ticket.

**Matthew Panzarino:** Honestly, I think it's the same path.

**Matthew Panzarino:** a ticket.

**Matthew Panzarino:** But in that ticket, I would say, hey, here's what I'm currently doing.

**Matthew Panzarino:** Can we tweak the instruction set of the current meta tagging generator to do something more like this?

**Matthew Panzarino:** Or leave it alone because it's part of a fundamental workflow, and this is the engineer's job to answer that question, which I kind of know what they're going to say, but I think it's good to put it out there.

**Matthew Panzarino:** Say, hey, it's kind of weak sauce because of X, or Z.

**Matthew Panzarino:** Like, I'm getting meta results out of here that are bad because of ABC, right?

**Matthew Panzarino:** They don't adhere to these principles.

**Matthew Panzarino:** And I know this will take 30 minutes, 40 minutes of your time, but I think it's well worth it to get the – I mean, it may be less.

**Matthew Panzarino:** I'm just exaggerating.

**Matthew Panzarino:** But, like, it's going take some time for you to file this ticket.

**Matthew Panzarino:** But I think you need to give it this explicit example.

**Matthew Panzarino:** Say, the current meta tagging is falling down in this way.

**Matthew Panzarino:** Here's the way that I solve it.

**Matthew Panzarino:** I have a cloud project.

**Matthew Panzarino:** I feed it this prompt.

**Matthew Panzarino:** It gives me these results, which I like.

**Matthew Panzarino:** Or at least some examples of this.

**Matthew Panzarino:** There is no reason why that can't happen in the pipeline.

**Matthew Panzarino:** Even the options.

**Matthew Panzarino:** Like, hey, give me three options.

**Matthew Panzarino:** Absolutely, totally possible.

**Matthew Panzarino:** And then you could choose the one you like the best or some permutation of that and then make that part of the final output, right?

**Matthew Panzarino:** There's no reason that can't happen.

**Nathan Navidzadeh:** It's totally possible.

**Nathan Navidzadeh:** So, one thing that would also be really cool, and I'm going to put that in the ticket that you just made me think of, is like actually showing me, well, the character count is something, but like what it actually like looks like when it's popped in.

**Nathan Navidzadeh:** Because the character count isn't like set character count.

**Nathan Navidzadeh:** It's like, right, it's the viewport or whatever, but like.

**Matthew Panzarino:** Yeah, 100 to 150 or whatever it is, yeah.

**Nathan Navidzadeh:** Yeah, so we also have to, I also have to always copy paste it into like, I forget what the fangools or something that we use.

**Nathan Navidzadeh:** It's just like a random tool that lets you like see what it would look like in Google search visually and if it'll get.

**Matthew Panzarino:** Yeah, you know what I would do?

**Matthew Panzarino:** Put that as an appendix.

**Matthew Panzarino:** Hey, by the way, it would be lovely if it could be presented this way, you know?

**Matthew Panzarino:** And now, whether they get to it or not, you say, hey, the priority is give me good metadata.

**Matthew Panzarino:** Minor P1 is like, if it could be presented in situ, then we can see, you know, what it would look like.

**Matthew Panzarino:** Now, is that pipeline, does it have publishing attached to it?

**Matthew Panzarino:** It does, Yeah.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** So then, I would mention that.

**Matthew Panzarino:** It's important, because then you would say, and I would love for, like, once I pick an option to move forward through the pipeline.

**Matthew Panzarino:** This should happen right before publishing, would be my guess, right?

**Nathan Navidzadeh:** It does, yeah.

**Matthew Panzarino:** Yeah, pick one, and then that will get passed to the publisher so that it goes, and then...

**Nathan Navidzadeh:** It already does that.

**Nathan Navidzadeh:** So the existing one already does that.

**Nathan Navidzadeh:** So I guess I could specify to make sure they don't lose that functionality.

**Matthew Panzarino:** Yeah, can see it, yeah.

**Nathan Navidzadeh:** Yeah, yeah.

**Nathan Navidzadeh:** No, it does that, and it also lets me edit it there, which is what I usually end up doing, replacing whatever.

**Matthew Panzarino:** Yeah, Get one in, right.

**Nathan Navidzadeh:** Mm-hmm, mm-hmm.

**Nathan Navidzadeh:** Okay, yeah, there's no reason that you should have to do that, and if that can take seven to eight minutes, or seven to eight minutes off your clock, that's wonderful, you know, so.

**Nathan Navidzadeh:** Yeah, that would be a win.

**Nathan Navidzadeh:** It doesn't, but even the club thing doesn't always give me what I want.

**Nathan Navidzadeh:** It gives me something closer to what I want, but it doesn't always give me it in the side, like, I'll specify under this many characters, and I will still give it to me more than that many characters.

**Matthew Panzarino:** yeah, yeah, and look, the way I look at that, personally, is like, okay, if you can reduce it from every time to one in ten, you know, that's a material, know, and then.

**Nathan Navidzadeh:** it's a gentick, if it's a gentick, then I might be able to do that now, because it'll just iterate, it'll check itself, be like, oh, does it pass that check of.

**Matthew Panzarino:** Yeah, yeah, absolutely.

**Matthew Panzarino:** You could mention that and say, like, hey, I do this in Claude now, so I would love if this could be an agent instead of a deterministic outcome, because your current meta tagging workflow is deterministic.

**Matthew Panzarino:** It just basically says...

**Matthew Panzarino:** Hey, generate this thing based off this prompt, and then it gives you that result.

**Matthew Panzarino:** If it's an agent, like, for instance, the post-processor agent, right, that has, like, three or four iterations to do, yes, it can have a rubric, and it can check against that rubric for success.

**Matthew Panzarino:** So there's no reason that any workflow in the current pipeline that's not agentic should be looked at as, like, state-of-the-art.

**Matthew Panzarino:** It's probably not working as well as if it was an agent.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** So, and just, like, these are things like the fact-checker, right?

**Matthew Panzarino:** It's not an agent.

**Matthew Panzarino:** It does not work well, you know, obviously, as well as the drafter does.

**Nathan Navidzadeh:** Yeah, I took it out.

**Nathan Navidzadeh:** Yeah, exactly.

**Matthew Panzarino:** It just causes more grief.

**Matthew Panzarino:** But, yeah, I would say, I would say that's absolutely possible.

**Matthew Panzarino:** But I am speaking for engineers, so let them tell us what's possible.

**Nathan Navidzadeh:** I mean, everything's possible is what they usually say.

**Nathan Navidzadeh:** It's just a matter of time and...

**Matthew Panzarino:** Exactly.

**Matthew Panzarino:** It's a matter of time and priority.

**Matthew Panzarino:** That's it.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** Okay, cool, cool.

**Nathan Navidzadeh:** No, that's helpful.

**Nathan Navidzadeh:** I'll probably do that.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** One is like just other posts.

**Nathan Navidzadeh:** I have like a bunch of post-processing prompts that I end up going through depending on what the article looks like when I do my read-through, right?

**Nathan Navidzadeh:** So my usual process is like, you know, it generates everything for me and then I just look at the final version of the article that it gave me and I look at, I have one bulk prompt that I always put it through, which like rechecks for em dashes and all that stuff, even though it's in the writing guidelines and everything.

**Nathan Navidzadeh:** Proof checker, proof checklist.

**Nathan Navidzadeh:** It does a lot better now ever since I switched to Egentic and updated all my artifacts to make them smaller and no conflicts within each other, but there's still the odd, you know, whatever em dash or like colon that's used for no reason like to, you know, so I still have to kind of do a go over there, but I just do it once and I just tell it to go over the whole article thoroughly and it does a good job.

**Nathan Navidzadeh:** And it's a big bulk prompt that just does a bunch of things that I wanted to look over.

**Nathan Navidzadeh:** And the...

**Nathan Navidzadeh:** The thing I haven't done is think about, okay, what parts of this can I plop into like a post-processing step that does it for me automatically?

**Nathan Navidzadeh:** And which one of these do I still need eyes on?

**Nathan Navidzadeh:** Because when I get it to do it like this, the way that I articulated the prompt for whatever reason.

**Nathan Navidzadeh:** to be made or whatever.

**Nathan Navidzadeh:** Exactly, yeah.

**Nathan Navidzadeh:** It doesn't always get exactly what I mean.

**Nathan Navidzadeh:** I'm like, okay, maybe I can try to articulate the prompt better so it doesn't, you know.

**Nathan Navidzadeh:** But there's always like an edge case or something that I'm going to miss at some point.

**Nathan Navidzadeh:** So I'm, you know, I was like, it doesn't take too much time.

**Nathan Navidzadeh:** plop it in, you go through all the things.

**Nathan Navidzadeh:** And I love that feature of Atlas because you don't have that in Claude, right?

**Nathan Navidzadeh:** Where it actually like shows you like the, what it edited and when you can accept or deny, you know.

**Nathan Navidzadeh:** So that's like actually a really powerful feature.

**Matthew Panzarino:** cool, really cool that we have that.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** Makes it super easy.

**Nathan Navidzadeh:** So that's, but I think the meta stuff is probably, I'm going to move forward with that.

**Matthew Panzarino:** Yeah, I mean, take that win for sure.

**Matthew Panzarino:** And then on the post processor, I think that's the right way to think about it.

**Matthew Panzarino:** Like.

**Matthew Panzarino:** Think about the ones where you still need that human in the loop or human interaction where you could separate it out.

**Matthew Panzarino:** I think there's probably a case to be made for running your packet of, let's call it, this is probably going to work once, as a post-processing step.

**Matthew Panzarino:** And then adding an additional post-processing step that does your choice, like, you know, your particular ones where you're like, I want to keep a close eye on these.

**Matthew Panzarino:** There's no reason it can't run those separately.

**Matthew Panzarino:** And the reason for separating those out is obvious, right?

**Matthew Panzarino:** Because if it makes bad choices, you can isolate, you know, where those happened.

**Matthew Panzarino:** But I would say start with the first one.

**Matthew Panzarino:** think that's a good instinct to, like, get the stuff on the books or into the pipeline that you know will most likely be successful.

**Matthew Panzarino:** Especially with an agentic approach, with a rubric and a couple of loops, you know.

**Matthew Panzarino:** I would say that's probably your next ticket is like, hey, I have these four post

**Matthew Panzarino:** Processing steps, the six post-processing steps that are successful almost always with Opus, you know, with a kind of one shot.

**Matthew Panzarino:** So this seems like an ideal candidate for a post-processor in this pipeline.

**Matthew Panzarino:** And I would say that's a ticket as well.

**Matthew Panzarino:** Just start trying to clear out the deadwood and then leave the high level of difficulty stuff in the realm of like, I wonder, you know, and you can always engage with that.

**Matthew Panzarino:** But don't hesitate to like compartmentalize and file tickets for the ones that you feel are like, the ones that you feel are pretty straightforward in terms of like, I have gotten good results with this process.

**Matthew Panzarino:** It just doesn't exist in Atlas, right?

**Nathan Navidzadeh:** Like that's the decision tree.

**Matthew Panzarino:** And like, if you've gotten a process that's not, I typed it manually, which I understand some of the things are that.

**Matthew Panzarino:** But if you've got some sort of process, especially in automation, there's no reason that Atlas can't accomplish that.

**Matthew Panzarino:** Zero, right?

**Matthew Panzarino:** Because it's the same underlying models or similar ones.

**Matthew Panzarino:** It's just actually just additional guide rails.

**Matthew Panzarino:** So I...

**Matthew Panzarino:** think your mindset going forward into the new year should be like, hey, there are now engineering resources available, and I should file a ticket.

**Matthew Panzarino:** It may not get addressed immediately, but the triage is going to be a lot faster, a lot more aggressive, because they're paying close attention.

**Matthew Panzarino:** They're doing rounds on everyone.

**Matthew Panzarino:** And I have these conversations with a lot of people.

**Matthew Panzarino:** Everyone on one I have has one or two or three of these kinds of things where I'm like, I don't want to beat a dead horse, but file a ticket, you know, because they now have capacity.

**Matthew Panzarino:** And it also, of course, of course, helps them long-term to see, here's what we've got going on overall, and this workflow needs to be addressed.

**Matthew Panzarino:** It's really falling down on the job for a lot of people, and they're trying to patch it in this way or another, you know.

**Nathan Navidzadeh:** Yeah, that makes sense.

**Nathan Navidzadeh:** Yeah, that's cool.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** Yeah, I don't got anything else.

**Nathan Navidzadeh:** That's helpful, though.

**Nathan Navidzadeh:** It's just been in the back of my mind, so it's good having some check-ins to be like, yeah, just do it.

**Nathan Navidzadeh:** Yeah, yeah, yeah.

**Nathan Navidzadeh:** File the ticket.

**Nathan Navidzadeh:** This is how it will, this is why it will work if you do it.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** I mean, like the, the, we don't know what we don't know thing is super real.

**Matthew Panzarino:** So when people talk to me about things, I can, obviously the things that I talk about in like our big meetings are generally ones that I've heard more than once.

**Matthew Panzarino:** You know, somebody has mentioned something or whatever, and I'm like, oh, I need to talk to people about this.

**Matthew Panzarino:** But sometimes it's, everybody's just suffering in silence separately.

**Matthew Panzarino:** And like, that's, it's just one of those things where you could be filing a ticket based on metadata and everybody's like, oh, thank God.

**Matthew Panzarino:** Somebody filed a ticket on this metadata because we have the same problem and we can deploy the workflow for them too.

**Matthew Panzarino:** So, so win, you know, for everyone.

**Matthew Panzarino:** And, you know, you clearly have a process oriented mindset and like articulate this stuff fairly clearly.

**Matthew Panzarino:** So I think that's a great thing to pay forward into the system and, and, you know, you'll help your peers out and yourself at the same time.

**Nathan Navidzadeh:** So that's good.

**Nathan Navidzadeh:** Cool.

**Matthew Panzarino:** I appreciate that.

**Nathan Navidzadeh:** Sweet.

**Nathan Navidzadeh:** Do you have any insight at all with data grid in my situation with, I feel like I joined.

**Nathan Navidzadeh:** I joined, and then the team that I've been part of has been in constant flux.

**Nathan Navidzadeh:** I've been, like, the only constant.

**Nathan Navidzadeh:** You know what I mean?

**Nathan Navidzadeh:** Like, Mara left, Vivek's leaving, Nika's leaving.

**Nathan Navidzadeh:** It's like, I don't have any insight on where that's going.

**Matthew Panzarino:** What specifically about it?

**Matthew Panzarino:** Like, what the work is that data did?

**Nathan Navidzadeh:** Is there something going on that I don't know about, like, behind the scenes?

**Nathan Navidzadeh:** Like, should I be worried about anything?

**Nathan Navidzadeh:** Is DataGrid a tough client?

**Matthew Panzarino:** Or are these people...

**Matthew Panzarino:** Oh, I see.

**Matthew Panzarino:** No, no.

**Matthew Panzarino:** Honestly, the Mara thing was, like, a mutual thing.

**Matthew Panzarino:** Vivek thing was, you know...

**Matthew Panzarino:** I mean, not Vivek.

**Nathan Navidzadeh:** Who did you say?

**Nathan Navidzadeh:** Vivek, yeah, yeah.

**Matthew Panzarino:** Vivek.

**Nathan Navidzadeh:** Oh, yeah, Because he's leaving end of month, yeah.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** He found something else, you know?

**Matthew Panzarino:** Like, wasn't...

**Matthew Panzarino:** That wasn't us.

**Matthew Panzarino:** That was him.

**Matthew Panzarino:** He was going, ah, I got this opportunity.

**Matthew Panzarino:** Actually, I don't even know the specifics, but I think that's what...

**Nathan Navidzadeh:** It wasn't us.

**Nathan Navidzadeh:** Let's put it that way.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** But no, I don't think so.

**Matthew Panzarino:** I honestly think that it's...

**Matthew Panzarino:** Um, it's not like actually a, a, uh, it's not like a poison pill client or anything.

**Matthew Panzarino:** Um, it's kind of an important one and it's an, it's an interesting one.

**Matthew Panzarino:** Um, there is, is, and has been a lot of back and forth on it, on that engagement over the time that we've had it, but not through any fault of anybody internally, right?

**Matthew Panzarino:** It's like sort of data grid trying to figure  out, you know?

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** So no, no, not at all.

**Matthew Panzarino:** And, and certainly nothing from my perspective on, um, and I would have brought it to this call, like, or if it calls like this, where I've been like, you know, Nathan, here's the thing you got to focus on.

**Matthew Panzarino:** Like, I'm not, I'm not seeing this or we are seeing that.

**Matthew Panzarino:** So not, not yet.

**Matthew Panzarino:** And I will be proactive about it, obviously, if I, if I hear anything or, um, typically what would happen is, you know, EM on the account would come to me and be like, Hey, I think we really need to work on this.

**Matthew Panzarino:** Can you help me with that or whatever?

**Matthew Panzarino:** I have not received anything like that.

**Matthew Panzarino:** So, so no, no, nothing, nothing I could see.

**Matthew Panzarino:** I think it's honestly, there was a handful of, and Nika, I think it was a, actually, no, I know Nika was also just like, I found a thing, you know?

**Matthew Panzarino:** Like inherently people are.

**Matthew Panzarino:** We're going to get other opportunities.

**Matthew Panzarino:** That happens, you know.

**Nathan Navidzadeh:** Okay.

**Nathan Navidzadeh:** And VFAC and Nika, been with you guys for a while now, I guess.

**Nathan Navidzadeh:** It just felt odd for me.

**Nathan Navidzadeh:** I'm like, I'm joining this team and everybody's just like leaving.

**Matthew Panzarino:** like, it's something.

**Nathan Navidzadeh:** Like you look around and you're like, Yeah, I know the stability thing is, it's, yeah, it feels weird when it's like all of a sudden there's a lot of ships at once.

**Matthew Panzarino:** But no, honestly, these are unrelated, you know, they really are.

**Nathan Navidzadeh:** Okay.

**Matthew Panzarino:** Not related to DataGrid and honestly not related to each other.

**Nathan Navidzadeh:** Okay, good.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** I mean, you know, from the external channel for DataGrid, they seem great.

**Nathan Navidzadeh:** And from the meetings that I've watched or, you know, scanned through, they seem, they seem fine.

**Nathan Navidzadeh:** So I was just like, this is something, I don't know, just, you know, I just had to check because it's like, what's going on?

**Nathan Navidzadeh:** It just felt a little weird, but, but that's good.

**Nathan Navidzadeh:** It's good to hear.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** Cool.

**Nathan Navidzadeh:** Cool.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** That's great.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** And like the, my only thing on, you know, my only task for you is just be proactive about like, process oriented.

**Matthew Panzarino:** Or any other blockers that you have or anything, raise your hand.

**Matthew Panzarino:** It's not like, oh, it's a failure if I raise my hand and say, like, you know, I can't figure this out or this is costing me, you know, costing me a bunch of time or whatever.

**Matthew Panzarino:** Just be proactive about it.

**Matthew Panzarino:** That's all I ask.

**Matthew Panzarino:** You know, it's obviously I don't want you to get into a hole and be, like, you know, over your skis or underwater is probably the more apt analogy on any sort of work.

**Matthew Panzarino:** And not me, not just me, but, like, us not know, right?

**Matthew Panzarino:** Like, there's no reason that anybody should feel, like, weird about that because it's going to happen.

**Matthew Panzarino:** You know, the clients have weird requests that are just, like, ebb and flow.

**Matthew Panzarino:** A stakeholder gets wonky about something and all of a sudden it creates a capacity issue.

**Matthew Panzarino:** There will be things like that.

**Matthew Panzarino:** Just be transparent.

**Matthew Panzarino:** You know, just be proactive.

**Matthew Panzarino:** Communicate.

**Matthew Panzarino:** We'll figure it out.

**Nathan Navidzadeh:** Sounds good.

**Nathan Navidzadeh:** Now you know me.

**Matthew Panzarino:** I'm always asking questions and talking.

**Nathan Navidzadeh:** Yeah, I'll wait.

**Matthew Panzarino:** All good.

**Matthew Panzarino:** Ask away.

**Matthew Panzarino:** I don't know.

**Matthew Panzarino:** I'm not one of those how-dare-you-ask-a-question kind of people.

**Nathan Navidzadeh:** Cool, cool.

**Matthew Panzarino:** Sweet.

**Matthew Panzarino:** Thanks, Nathan.

**Matthew Panzarino:** I appreciate it.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Hope you feel better, sir.

**Nathan Navidzadeh:** Thanks.

**Nathan Navidzadeh:** See you.
